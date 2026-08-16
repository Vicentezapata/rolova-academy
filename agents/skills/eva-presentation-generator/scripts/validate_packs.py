#!/usr/bin/env python3
"""Valida theme packs y planes antes de generar. Barato, determinista, sin capturas.

Uso:
    python scripts/validate_packs.py                      # valida todos los packs
    python scripts/validate_packs.py --plan ruta/visual_plan.json   # valida además un plan
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pack_renderer import ThemePack, PackError, render_slide, SLOT_RE, REPEAT_RE

SKILL_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKS_DIR = os.path.join(SKILL_PATH, "theme-packs")

# Slots que resuelve el propio frame/renderer y por tanto no debe aportar el plan.
RENDERER_SLOTS = {"EXTRA_CSS", "SHARED_CSS", "BODY", "SLIDE_NUM", "TOTAL", "SLIDE_TITLE"}
MAX_CONSECUTIVE = 3
# Únicos colores literales admitidos en los arquetipos compartidos: semáforo de la
# ventana de código y fondo blanco del QR, que no dependen del tema.
COLOR_ALLOWLIST = {"#ff5f57", "#ffbd2e", "#28ca41", "#fff"}
COLOR_RE = re.compile(r"rgba?\([0-9.,\s]+\)|#[0-9a-fA-F]{3,8}\b")


def validate_shared() -> tuple[list[str], list[str]]:
    """Los arquetipos compartidos deben ser 100% token-only para que un pack nuevo
    sea solo _frame.html + pack.json."""
    errors, warns = [], []
    shared = os.path.join(PACKS_DIR, "_shared")

    for required in ("_base.css", "archetypes.json"):
        if not os.path.exists(os.path.join(shared, required)):
            errors.append(f"_shared/{required}: falta")

    for name in sorted(os.listdir(shared)):
        if not re.match(r"a\d{2}-.*\.html$", name):
            continue
        raw = open(os.path.join(shared, name), encoding="utf-8").read()
        if "<!--CSS-->" not in raw or "<!--BODY-->" not in raw:
            errors.append(f"_shared/{name}: falta el marcador <!--CSS--> o <!--BODY-->")
            continue
        # Se escanea el archivo COMPLETO: los colores tambien se filtran por los
        # <script> del cuerpo (p. ej. la paleta de Mermaid), no solo por el CSS.
        for literal in COLOR_RE.findall(raw):
            if literal.lower() not in COLOR_ALLOWLIST:
                errors.append(f"_shared/{name}: color literal '{literal}' — usa un token del contrato")
        if "<!DOCTYPE" in raw or "<html" in raw:
            errors.append(f"_shared/{name}: no debe traer <!DOCTYPE> ni <html> (eso lo pone el frame)")

    return errors, warns


def validate_pack(pack_id: str) -> tuple[list[str], list[str]]:
    errors, warns = [], []
    pack = ThemePack(PACKS_DIR, pack_id)

    rhythm_keys = set()
    for variant in pack.rhythm:
        rhythm_keys |= set(variant)

    frame_slots = set(SLOT_RE.findall(pack.frame))
    unresolved = frame_slots - RENDERER_SLOTS - rhythm_keys
    if unresolved:
        warns.append(f"{pack_id}/_frame.html: slots sin cubrir por background_rhythm: {sorted(unresolved)}")

    for required in ("SHARED_CSS", "BODY", "SLIDE_NUM"):
        if required not in frame_slots:
            errors.append(f"{pack_id}/_frame.html: falta el marcador {{{{{required}}}}}")
    if "forward-key" not in pack.frame:
        errors.append(f"{pack_id}/_frame.html: falta el script que reenvía teclas al visor")

    # El frame debe declarar todos los tokens que consumen las primitivas y los arquetipos.
    declared = set(re.findall(r"(--[a-z0-9-]+)\s*:", pack.frame))
    used = set(re.findall(r"var\((--[a-z0-9-]+)\)", pack.base_css))
    for name in pack.archetypes_meta:
        css, _ = pack.archetype(name)
        used |= set(re.findall(r"var\((--[a-z0-9-]+)\)", css))
    for missing in sorted(used - declared):
        errors.append(f"{pack_id}/_frame.html: no declara el token '{missing}' que sí se usa")

    for name, entry in pack.archetypes_meta.items():
        path = os.path.join(pack.shared_dir, entry["file"])
        if not os.path.exists(path):
            errors.append(f"{pack_id}.{name}: falta el archivo _shared/{entry['file']}")
            continue

        css, body = pack.archetype(name)
        combined = css + "\n" + body

        declared_slots = set(entry.get("slots", [])) | set(entry.get("repeats", {}))
        # Slots que quedan fuera de los bloques REPEAT: los debe aportar el plan.
        outside = REPEAT_RE.sub("", combined)
        used_slots = {s for s in SLOT_RE.findall(outside) if s.isupper()} - RENDERER_SLOTS

        for missing in sorted(used_slots - declared_slots):
            errors.append(f"{name}: usa {{{{{missing}}}}} pero archetypes.json no lo declara en 'slots'")
        for extra in sorted(declared_slots - used_slots - set(entry.get("repeats", {}))):
            warns.append(f"{name}: archetypes.json declara '{extra}' pero el template no lo usa")

        for rep_name, fields in entry.get("repeats", {}).items():
            block = re.search(rf"<!--REPEAT:{rep_name}-->(.*?)<!--END:{rep_name}-->", combined, re.DOTALL)
            if not block:
                errors.append(f"{name}: archetypes.json declara repeat '{rep_name}' pero no existe el bloque")
                continue
            inner_fields = {s for s in SLOT_RE.findall(block.group(1)) if not s.isupper()}
            for missing in sorted(inner_fields - set(fields)):
                errors.append(f"{name}.{rep_name}: campo '{missing}' no declarado en archetypes.json")

    return errors, warns


def validate_plan(plan_path: str) -> tuple[list[str], list[str]]:
    errors, warns = [], []
    with open(plan_path, encoding="utf-8") as f:
        plan = json.load(f)

    pack_id = plan.get("pack")
    if not pack_id:
        errors.append("El plan no declara 'pack' en la raíz.")
        return errors, warns

    pack = ThemePack(PACKS_DIR, pack_id)
    slides = plan.get("slides", [])
    if not slides:
        errors.append("El plan no tiene slides.")
        return errors, warns

    run_name, run_len = None, 0
    for idx, slide in enumerate(slides):
        label = f"slide {idx:02d}"
        name = slide.get("archetype")

        if not name:
            if not slide.get("html_content"):
                errors.append(f"{label}: sin 'archetype' ni 'html_content'")
            else:
                warns.append(f"{label}: usa html_content a mano (escape hatch) — fuente de deriva visual")
            run_name, run_len = None, 0
            continue

        if name not in pack.archetypes_meta:
            errors.append(f"{label}: arquetipo '{name}' no existe")
            continue

        # Los slots interpolados dentro del bloque CSS son estructurales: si faltan,
        # la regla queda inválida (p. ej. `repeat(,1fr)`) y la retícula colapsa sin avisar.
        css, _body = pack.archetype(name)
        slide_slots = slide.get("slots") or {}
        for critical in sorted({s for s in SLOT_RE.findall(css) if s.isupper()} - RENDERER_SLOTS):
            if not str(slide_slots.get(critical, "")).strip():
                errors.append(
                    f"{label}: '{name}' interpola {{{{{critical}}}}} en su CSS y el plan no lo aporta "
                    f"— la regla queda inválida y la retícula colapsa"
                )

        # Cadencia: nunca más de MAX_CONSECUTIVE del mismo arquetipo seguidos.
        run_len = run_len + 1 if name == run_name else 1
        run_name = name
        if run_len > MAX_CONSECUTIVE:
            warns.append(f"{label}: {run_len} slides seguidas de '{name}' — rompe el ritmo visual, intercala otro arquetipo")

        try:
            _, slide_warns = render_slide(pack, slide, idx, len(slides))
            warns.extend(slide_warns)
        except PackError as exc:
            errors.append(str(exc))

        if not str(slide.get("notes") or slide.get("speaker_notes") or "").strip():
            warns.append(f"{label}: sin notas de orador")

    names = [s.get("archetype") for s in slides]
    if names and names[0] != "cover":
        warns.append("La slide 00 no es 'cover'")
    if "section" not in names:
        warns.append("El deck no usa ninguna 'section' — sin separadores el ritmo se aplana")
    if "quiz" not in names:
        warns.append("El deck no incluye ningún 'quiz' — se pierde la verificación de comprensión")

    return errors, warns


def main() -> int:
    parser = argparse.ArgumentParser(description="Valida theme packs y, opcionalmente, un visual_plan.json")
    parser.add_argument("--plan", help="Ruta a un visual_plan.json a validar")
    parser.add_argument("--pack", help="Validar solo este pack")
    args = parser.parse_args()

    all_errors, all_warns = [], []

    e, w = validate_shared()
    all_errors += e
    all_warns += w
    print(f"[{'FAIL' if e else 'OK'}] arquetipos compartidos (_shared)")

    pack_ids = [args.pack] if args.pack else sorted(
        d for d in os.listdir(PACKS_DIR)
        if os.path.isdir(os.path.join(PACKS_DIR, d)) and not d.startswith("_")
    )
    for pack_id in pack_ids:
        e, w = validate_pack(pack_id)
        all_errors += e
        all_warns += w
        status = "FAIL" if e else "OK"
        print(f"[{status}] pack '{pack_id}'")

    if args.plan:
        e, w = validate_plan(args.plan)
        all_errors += e
        all_warns += w
        print(f"[{'FAIL' if e else 'OK'}] plan '{args.plan}'")

    for w in all_warns:
        print(f"  [WARN]  {w}")
    for e in all_errors:
        print(f"  [ERROR] {e}")

    print(f"\n{len(all_errors)} errores, {len(all_warns)} advertencias")
    return 1 if all_errors else 0


if __name__ == "__main__":
    sys.exit(main())
