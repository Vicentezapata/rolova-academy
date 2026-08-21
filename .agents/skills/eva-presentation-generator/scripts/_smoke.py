import json
import os
import subprocess
import sys

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(SKILL, "_packsmoke")

SLIDES = [
    {"archetype": "cover", "slots": {
        "EYEBROW": "UNIDAD DEMO", "TITLE": "Prueba de pack",
        "SUBTITLE": "Validación visual del contrato de tokens",
        "CHIPS": [
            {"label": "Tokens", "accent": "a1"},
            {"label": "Arquetipos", "accent": "a2"},
            {"label": "Packs", "accent": "a3"}]},
     "notes": "Portada."},
    {"archetype": "principle", "slots": {
        "TAG_LEFT": "CONCEPTO", "TITLE": "Un principio central", "TAG_RIGHT": "02",
        "GHOST": "80/20", "KICKER": "La regla",
        "PRINCIPLE": "El 20% de las causas produce el 80% de los efectos.",
        "PRINCIPLE_BODY": "Cuerpo de apoyo con detalle suficiente para juzgar la legibilidad real sobre este fondo.",
        "LIST_TITLE": "Factores",
        "FACTORS": [
            {"name": "Frecuencia", "text": "Cuántas veces ocurre el caso.", "color": "a1"},
            {"name": "Impacto", "text": "Qué tan grave es cuando ocurre.", "color": "a2"},
            {"name": "Costo", "text": "Cuánto cuesta corregirlo tarde.", "color": "a3"}],
        "EXAMPLES": [
            {"title": "Defectos", "text": "Concentrados en pocos módulos", "value": "80%"},
            {"title": "Soporte", "text": "Tickets por una sola causa", "value": "64%"}]},
     "notes": "Principio."},
    {"archetype": "concept-cards", "slots": {
        "TAG_LEFT": "ESTRUCTURA", "TITLE": "Tres conceptos", "TAG_RIGHT": "03", "COLS": "3",
        "CARDS": [
            {"badge": "01", "title": "Primera",
             "body": "Contenido de la tarjeta uno con texto suficiente para evaluar el ritmo.",
             "note_label": "Nota", "note": "Detalle secundario."},
            {"badge": "02", "title": "Segunda",
             "body": "Contenido de la tarjeta dos con texto suficiente para evaluar el ritmo.",
             "note_label": "Nota", "note": "Detalle secundario."},
            {"badge": "03", "title": "Tercera",
             "body": "Contenido de la tarjeta tres con texto suficiente para evaluar el ritmo.",
             "note_label": "Nota", "note": "Detalle secundario."}]},
     "notes": "Tarjetas."},
    {"archetype": "section", "slots": {
        "PART_LABEL": "PARTE 02", "TITLE": "Cierre de sección", "SUBTITLE": "Separador",
        "AGENDA": [
            {"label": "01", "text": "Primer bloque"},
            {"label": "02", "text": "Segundo bloque"},
            {"label": "03", "text": "Tercer bloque"}]},
     "notes": "Sección."},
]


def main():
    for p in sys.argv[1:]:
        d = os.path.join(OUT, p)
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "visual_plan.json"), "w", encoding="utf-8") as f:
            json.dump({"pack": p, "slides": SLIDES}, f, ensure_ascii=False)
        r = subprocess.run(
            [sys.executable, os.path.join(SKILL, "scripts", "generate_presentation_template.py"),
             "--unit-path", d, "--pack", p],
            capture_output=True, text=True)
        warn = [ln for ln in (r.stdout + r.stderr).splitlines() if "WARN" in ln or "Error" in ln]
        print(f"[{p}] rc={r.returncode} " + (" | ".join(warn) if warn else "sin avisos"))
    print("OUT:", OUT)


main()
