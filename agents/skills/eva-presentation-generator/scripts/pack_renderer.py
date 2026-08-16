"""Renderiza una slide autocontenida a partir de un theme pack + arquetipo + contenido.

El agente NUNCA escribe HTML: solo aporta strings de contenido en `slots`.

Arquitectura de tokens:
  theme-packs/_shared/aNN-*.html   estructura + CSS escrito SOLO con tokens
  theme-packs/_shared/_base.css    primitivas comunes
  theme-packs/<pack>/_frame.html   tokens del tema + decoraciones de firma

Por eso crear un pack nuevo son 2 archivos (_frame.html + pack.json) y no 25.
"""

from __future__ import annotations

import json
import os
import re

REPEAT_RE = re.compile(r"[ \t]*<!--REPEAT:([A-Z0-9_]+)-->\n(.*?)[ \t]*<!--END:\1-->\n", re.DOTALL)
SLOT_RE = re.compile(r"\{\{([A-Za-z0-9_]+)\}\}")
CSS_MARK = "<!--CSS-->"
BODY_MARK = "<!--BODY-->"
SHARED_DIR = "_shared"
# Marcadores que el renderer inyecta al final con `replace` literal, no vía regex.
INJECTED_SLOTS = {"SHARED_CSS", "EXTRA_CSS", "BODY"}


class PackError(Exception):
    pass


class ThemePack:
    def __init__(self, packs_dir: str, pack_id: str):
        self.id = pack_id
        self.dir = os.path.join(packs_dir, pack_id)
        self.shared_dir = os.path.join(packs_dir, SHARED_DIR)

        if not os.path.isdir(self.dir):
            available = sorted(
                d for d in os.listdir(packs_dir)
                if os.path.isdir(os.path.join(packs_dir, d)) and not d.startswith("_")
            )
            raise PackError(f"Theme pack '{pack_id}' no existe. Disponibles: {', '.join(available)}")

        with open(os.path.join(self.dir, "pack.json"), encoding="utf-8") as f:
            self.meta = json.load(f)
        with open(os.path.join(self.dir, "_frame.html"), encoding="utf-8") as f:
            self.frame = f.read()
        with open(os.path.join(self.shared_dir, "archetypes.json"), encoding="utf-8") as f:
            self.archetypes_meta = json.load(f)["archetypes"]
        with open(os.path.join(self.shared_dir, "_base.css"), encoding="utf-8") as f:
            self.base_css = f.read()
        with open(os.path.join(self.shared_dir, "_runtime.js"), encoding="utf-8") as f:
            self.runtime_js = f.read()

        self.rhythm = self.meta.get("background_rhythm") or [{}]
        self._archetype_cache: dict[str, tuple[str, str]] = {}

    def archetype(self, name: str) -> tuple[str, str]:
        """Devuelve (css, body) del arquetipo compartido, cacheado."""
        if name in self._archetype_cache:
            return self._archetype_cache[name]

        entry = self.archetypes_meta.get(name)
        if not entry:
            raise PackError(
                f"Arquetipo '{name}' no existe. "
                f"Disponibles: {', '.join(sorted(self.archetypes_meta))}"
            )

        path = os.path.join(self.shared_dir, entry["file"])
        with open(path, encoding="utf-8") as f:
            raw = f.read()

        if CSS_MARK not in raw or BODY_MARK not in raw:
            raise PackError(f"{path}: falta el marcador {CSS_MARK} o {BODY_MARK}")

        css = raw.split(CSS_MARK, 1)[1].split(BODY_MARK, 1)[0].strip("\n")
        body = raw.split(BODY_MARK, 1)[1].strip("\n")
        self._archetype_cache[name] = (css, body)
        return css, body


def _expand_repeats(template: str, slots: dict, warnings: list[str], label: str) -> str:
    """Sustituye cada bloque REPEAT por una copia del sub-template por cada item."""

    def render_block(match: re.Match) -> str:
        name, inner = match.group(1), match.group(2)
        items = slots.get(name)
        if items is None:
            warnings.append(f"{label}: falta la lista '{name}' — el bloque queda vacío")
            return ""
        if not isinstance(items, list):
            raise PackError(f"{label}: '{name}' debe ser una lista de objetos, no {type(items).__name__}")

        out = []
        missing_fields: set[str] = set()
        for item in items:
            if not isinstance(item, dict):
                raise PackError(f"{label}: cada elemento de '{name}' debe ser un objeto")

            def take(m: re.Match) -> str:
                key = m.group(1)
                if key not in item:
                    missing_fields.add(key)
                return str(item.get(key, ""))

            chunk = SLOT_RE.sub(take, inner)
            out.append(chunk)
        if missing_fields:
            warnings.append(
                f"{label}: '{name}' sin los campos {sorted(missing_fields)} — se dejaron vacíos"
            )
        return "".join(out)

    return REPEAT_RE.sub(render_block, template)


def render_slide(pack: ThemePack, slide: dict, index: int, total: int) -> tuple[str, list[str]]:
    """Devuelve (html_completo, warnings) para una slide del visual_plan."""
    warnings: list[str] = []
    label = f"slide {index:02d}"

    archetype_name = slide.get("archetype")
    if not archetype_name:
        raise PackError(f"{label}: falta el campo 'archetype'")

    css, body = pack.archetype(archetype_name)
    slots = dict(slide.get("slots") or {})

    body = _expand_repeats(body, slots, warnings, label)
    css = _expand_repeats(css, slots, warnings, label)

    rhythm = pack.rhythm[index % len(pack.rhythm)]
    context = {
        **rhythm,
        **{k: v for k, v in slots.items() if not isinstance(v, list)},
        "SLIDE_NUM": f"{index:02d}",
        "TOTAL": f"{total - 1:02d}",
        "SLIDE_TITLE": slide.get("title", f"Slide {index:02d}"),
    }

    missing: set[str] = set()

    def substitute(text: str) -> str:
        def repl(m: re.Match) -> str:
            key = m.group(1)
            if key in INJECTED_SLOTS:
                return m.group(0)  # se inyecta después, no se toca aquí
            if key in context:
                return str(context[key])
            missing.add(key)
            return ""
        return SLOT_RE.sub(repl, text)

    # Se sustituye cada pieza por separado y los bloques grandes se inyectan al final
    # con `replace` literal: así el CSS/HTML insertado nunca se vuelve a escanear.
    html = substitute(pack.frame)
    html = html.replace("{{SHARED_CSS}}", pack.base_css)
    html = html.replace("{{EXTRA_CSS}}", substitute(css))
    html = html.replace(
        "{{BODY}}",
        substitute(body) + f"\n<script>\n{pack.runtime_js}\n</script>",
    )

    for key in sorted(missing):
        warnings.append(f"{label}: slot '{{{{{key}}}}}' sin valor — se dejó vacío")

    return html, warnings
