import os
import shutil
import json
import argparse
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pack_renderer import ThemePack, PackError, render_slide

# Configuration defaults: resolved relative to this script's own location so the
# skill works regardless of machine/OS/username (no hardcoded absolute path).
SKILL_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKS_DIR = os.path.join(SKILL_PATH, "theme-packs")

# Safety-net script injected only if a hand-written slide forgot the keydown forwarder.
FALLBACK_KEY_SCRIPT = """
<script>
  document.addEventListener('keydown', e => {
    if (['ArrowLeft', 'ArrowUp', 'ArrowRight', 'ArrowDown', ' ', '+', '-'].includes(e.key)) e.preventDefault();
    window.parent.postMessage({ type: 'forward-key', key: e.key }, '*');
  });
  window.addEventListener('message', e => {
    if (e.data && e.data.type === 'text-zoom') {
      const content = document.querySelector('.content') || document.querySelector('.slide') || document.body;
      if (content) content.style.zoom = e.data.scale;
    }
  });
</script>
"""


def parse_args():
    parser = argparse.ArgumentParser(description="EVA Presentation Generator - Theme Pack Assembler")
    parser.add_argument("--unit-path", required=True, help="Path to the unit directory")
    parser.add_argument("--pack", default=None, help="Theme pack id (overrides visual_plan.json)")
    return parser.parse_args()


def load_plan(unit_path):
    plan_path = os.path.join(unit_path, "visual_plan.json")
    if not os.path.exists(plan_path):
        plan_path = os.path.join(unit_path, "outline.json")

    if os.path.exists(plan_path):
        with open(plan_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    print(f"Warning: No visual_plan.json or outline.json found in {unit_path}.")
    return {"slides": []}


def ensure_standalone_document(html_content, idx):
    """Escape hatch only: validates a hand-written `html_content` slide is a full document
    and adds the keydown forwarder if missing. Pack-rendered slides never reach this."""
    lowered = html_content.lower()
    if "<!doctype html>" not in lowered:
        print(f"[WARN] Slide {idx:02d}: html_content no es un documento HTML completo. "
              f"Prefiere usar 'archetype' + 'slots' en vez de escribir HTML a mano.")
    if "forward-key" not in html_content and "</body>" in html_content:
        html_content = html_content.replace("</body>", f"{FALLBACK_KEY_SCRIPT}</body>")
    return html_content


def fallback_slide_html(idx):
    return (
        "<!DOCTYPE html><html lang='es'><head><meta charset='UTF-8'>"
        f"<title>Slide {idx:02d}</title></head><body style=\"margin:0;background:#0a0a0a;color:#fff;"
        "display:flex;align-items:center;justify-content:center;height:100vh;font-family:sans-serif;\">"
        f"<h1>Falta contenido — Slide {idx:02d}</h1></body></html>"
    )


def main():
    args = parse_args()
    unit_path = args.unit_path
    presentation_path = os.path.join(unit_path, "presentation")
    slides_path = os.path.join(presentation_path, "slides")

    # Clean and recreate presentation directory
    if os.path.exists(presentation_path):
        shutil.rmtree(presentation_path)
    os.makedirs(presentation_path)
    os.makedirs(slides_path)

    # Copy images generated/collected for the deck (slides reference them as images/<file>).
    # No shared assets/base.css/themes folder is copied: every slide is standalone.
    images_src = os.path.join(unit_path, "images")
    if os.path.exists(images_src):
        shutil.copytree(images_src, os.path.join(presentation_path, "images"))

    plan_data = load_plan(unit_path)
    # Support both list of slides or dict with metadata and slides
    slides = plan_data.get("slides", plan_data) if isinstance(plan_data, dict) else plan_data
    total_slides = len(slides)

    pack_id = args.pack or (plan_data.get("pack") if isinstance(plan_data, dict) else None)
    pack = ThemePack(PACKS_DIR, pack_id) if pack_id else None
    if pack:
        print(f"[PACK] {pack.meta.get('name', pack.id)} — {len(pack.archetypes_meta)} arquetipos disponibles")

    speaker_notes = {}
    slide_wraps = []
    all_warnings = []

    for idx, slide in enumerate(slides):
        # Ruta preferente y determinista: theme pack + arquetipo + slots de contenido.
        # El agente aporta solo texto; el frame se inyecta idéntico en todas las slides.
        if slide.get("archetype"):
            if not pack:
                raise PackError(
                    f"Slide {idx:02d} usa 'archetype' pero el plan no declara 'pack'. "
                    f"Añade \"pack\": \"dark_tech\" (u otro) en la raíz de visual_plan.json."
                )
            html_content, warns = render_slide(pack, slide, idx, total_slides)
            all_warnings.extend(warns)
        else:
            # Escape hatch: slide escrita a mano para un caso que ningún arquetipo cubre.
            html_content = slide.get("html_content", "").strip()
            if not html_content:
                print(f"[WARN] Slide {idx:02d}: sin 'archetype' ni 'html_content'. Usando fallback.")
                html_content = fallback_slide_html(idx)
            else:
                html_content = ensure_standalone_document(html_content, idx)

        slide_filename = f"slide_{idx:02d}.html"
        with open(os.path.join(slides_path, slide_filename), "w", encoding="utf-8") as f:
            f.write(html_content)

        speaker_notes[idx] = slide.get("notes", slide.get("speaker_notes", ""))
        slide_wraps.append(f'''<div class="slide-wrap" onclick="goToSlide({idx})"><iframe class="slide-frame" src="slides/{slide_filename}"></iframe></div>''')

    for w in all_warnings:
        print(f"[WARN] {w}")

    # Write JS notes
    with open(os.path.join(presentation_path, "notas_orador.js"), "w", encoding="utf-8") as f:
        f.write(f"window.speakerNotes = {json.dumps(speaker_notes, ensure_ascii=False, indent=2)};")

    # Create preview.html
    preview_src = open(os.path.join(SKILL_PATH, "templates", "core", "preview_template.html"), "r", encoding="utf-8").read()
    preview_src = preview_src.replace("{total_slides}", str(total_slides))
    preview_src = preview_src.replace("{slide_wraps}", "\n  ".join(slide_wraps))
    with open(os.path.join(presentation_path, "preview.html"), "w", encoding="utf-8") as f:
        f.write(preview_src)

    # Create presenter.html
    presenter_src = open(os.path.join(SKILL_PATH, "templates", "core", "presenter_template.html"), "r", encoding="utf-8").read()
    presenter_src = presenter_src.replace("{total_slides}", str(total_slides))
    with open(os.path.join(presentation_path, "presenter.html"), "w", encoding="utf-8") as f:
        f.write(presenter_src)
        
    # Create serve.py for local testing to avoid CORS issues
    serve_py_content = """import http.server
import socketserver
import webbrowser

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"\\nIniciando servidor EVA IPSS local en http://localhost:{PORT}")
    print("Abre 'preview.html' o 'presenter.html' en tu navegador.")
    print("Presiona Ctrl+C para detener el servidor.\\n")
    try:
        webbrowser.open(f"http://localhost:{PORT}/preview.html")
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\\nServidor detenido.")
"""
    with open(os.path.join(presentation_path, "serve.py"), "w", encoding="utf-8") as f:
        f.write(serve_py_content)

    print(f"[OK] Presentacion generada con exito en {presentation_path}")

if __name__ == "__main__":
    main()
