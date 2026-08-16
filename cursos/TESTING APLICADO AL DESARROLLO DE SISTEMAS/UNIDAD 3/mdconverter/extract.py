import zipfile, re, os, glob, html

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = []
for f in sorted(glob.glob(os.path.join(BASE, 'material', '*.pptx'))):
    out.append("\n\n# ===== %s =====\n" % os.path.basename(f))
    z = zipfile.ZipFile(f)
    names = [n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n)]
    names.sort(key=lambda n: int(re.search(r'(\d+)', n.split('/')[-1]).group(1)))
    for i, n in enumerate(names, 1):
        xml = z.read(n).decode('utf8', errors='ignore')
        lines = []
        for p in re.findall(r'<a:p>.*?</a:p>', xml, re.S):
            txt = ''.join(re.findall(r'<a:t>(.*?)</a:t>', p, re.S))
            txt = html.unescape(txt).strip()
            if txt:
                lines.append(txt)
        if lines:
            out.append("\n## Slide %d\n" % i + "\n".join("- " + l for l in lines))
        nn = n.replace('slides/slide', 'notesSlides/notesSlide')
        if nn in z.namelist():
            nx = z.read(nn).decode('utf8', errors='ignore')
            nt = ' '.join(html.unescape(t).strip() for t in re.findall(r'<a:t>(.*?)</a:t>', nx, re.S))
            nt = re.sub(r'^\s*\d+\s*', '', nt).strip()
            if len(nt) > 10:
                out.append("\n> NOTAS: " + nt)

dest = os.path.join(BASE, 'mdconverter', 'material_procesado.md')
with open(dest, 'w') as fh:
    fh.write("\n".join(out))
print('OK', os.path.getsize(dest))
