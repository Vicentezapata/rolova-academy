import json, re, os, glob, html, zipfile

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAT = os.path.join(BASE, 'material')
out = []

for f in sorted(glob.glob(os.path.join(MAT, '*.ipynb'))):
    out.append("\n\n# ===== %s =====\n" % os.path.basename(f))
    nb = json.load(open(f, encoding='utf8'))
    for i, celda in enumerate(nb.get('cells', []), 1):
        fuente = ''.join(celda.get('source', [])).rstrip()
        if not fuente:
            continue
        tipo = celda.get('cell_type')
        out.append("\n--- celda %d (%s) ---\n%s" % (i, tipo, fuente))

for f in sorted(glob.glob(os.path.join(MAT, '*.pptx'))):
    out.append("\n\n# ===== %s =====\n" % os.path.basename(f))
    z = zipfile.ZipFile(f)
    names = [n for n in z.namelist() if re.match(r'ppt/slides/slide\d+\.xml$', n)]
    names.sort(key=lambda n: int(re.search(r'(\d+)', n.split('/')[-1]).group(1)))
    for i, n in enumerate(names, 1):
        xml = z.read(n).decode('utf8', errors='ignore')
        lineas = []
        for p in re.findall(r'<a:p>.*?</a:p>', xml, re.S):
            t = ''.join(re.findall(r'<a:t>(.*?)</a:t>', p, re.S))
            t = html.unescape(t).strip()
            if t:
                lineas.append(t)
        if lineas:
            out.append("\n## Slide %d\n" % i + "\n".join("- " + l for l in lineas))

dest = os.path.join(BASE, 'mdconverter', 'material_procesado.md')
os.makedirs(os.path.dirname(dest), exist_ok=True)
with open(dest, 'w') as fh:
    fh.write("\n".join(out))
print('OK', os.path.getsize(dest), 'bytes')
