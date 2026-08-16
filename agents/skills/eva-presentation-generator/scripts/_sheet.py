"""Hoja de contactos 2x2 a escala 0.45 para revisar un pack completo en una captura."""
import os, sys

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(SKILL, "_packsmoke")

pack = sys.argv[1]
slides_dir = os.path.join(OUT, pack, "presentation", "slides")
names = sorted(n for n in os.listdir(slides_dir) if n.endswith(".html"))

W, H, S = 1280, 720, 0.30
cells = "".join(
    f'<div class="cell"><iframe src="{pack}/presentation/slides/{n}"></iframe></div>'
    for n in names
)
html = f"""<!DOCTYPE html><meta charset="utf-8"><style>
body{{margin:0;background:#1c1c1c;font-family:system-ui;}}
.wrap{{display:grid;grid-template-columns:repeat(2,{int(W*S)}px);gap:10px;padding:10px;width:max-content;}}
.cell{{width:{int(W*S)}px;height:{int(H*S)}px;overflow:hidden;}}
iframe{{width:{W}px;height:{H}px;border:0;transform:scale({S});transform-origin:0 0;}}
</style><div class="wrap">{cells}</div>"""
path = os.path.join(OUT, "sheet.html")
open(path, "w", encoding="utf-8").write(html)
print(path)
