import glob
import os

BASE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "_packsmoke")
h = ['<html><body style="margin:0;background:#1b1b1b;font-family:sans-serif">']
for p in sorted(os.listdir(BASE)):
    slides = sorted(glob.glob(os.path.join(BASE, p, "presentation", "slides", "*.html")))[:4]
    if not slides:
        continue
    h.append(f'<h2 style="color:#eee;padding:6px 16px;margin:18px 0 4px;font-size:15px">{p}</h2>')
    h.append('<div style="display:flex;gap:10px;padding:0 16px">')
    for s in slides:
        h.append(
            '<div style="flex:0 0 384px;width:384px;height:216px;overflow:hidden;border-radius:4px">'
            f'<iframe src="file://{os.path.abspath(s)}" scrolling="no" '
            'style="width:1280px;height:720px;border:0;transform:scale(0.3);transform-origin:0 0">'
            '</iframe></div>')
    h.append('</div>')
h.append("</body></html>")
out = os.path.join(BASE, "grid.html")
with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(h))
print(out)
