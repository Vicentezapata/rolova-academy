import zipfile, re, os, glob, html

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAT = os.path.join(BASE, 'materiales')
out = []


def limpiar_html(texto):
    texto = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', texto)
    texto = re.sub(r'(?i)<br\s*/?>|</(p|div|li|h[1-6]|td|tr)>', '\n', texto)
    texto = re.sub(r'<[^>]+>', ' ', texto)
    texto = html.unescape(texto)
    lineas = [l.strip() for l in texto.split('\n')]
    return [l for l in lineas if len(l) > 2]


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
        nn = n.replace('slides/slide', 'notesSlides/notesSlide')
        if nn in z.namelist():
            nx = z.read(nn).decode('utf8', errors='ignore')
            nt = ' '.join(html.unescape(t).strip() for t in re.findall(r'<a:t>(.*?)</a:t>', nx, re.S))
            nt = re.sub(r'^\s*\d+\s*', '', nt).strip()
            if len(nt) > 10:
                out.append("\n> NOTAS: " + nt)

for f in sorted(glob.glob(os.path.join(MAT, '*.html'))):
    out.append("\n\n# ===== %s =====\n" % os.path.basename(f))
    with open(f, encoding='utf8', errors='ignore') as fh:
        lineas = limpiar_html(fh.read())
    vistas = set()
    unicas = []
    for l in lineas:
        if l not in vistas:
            vistas.add(l)
            unicas.append(l)
    out.append("\n".join("- " + l for l in unicas))

dest = os.path.join(BASE, 'mdconverter', 'material_procesado.md')
os.makedirs(os.path.dirname(dest), exist_ok=True)
with open(dest, 'w') as fh:
    fh.write("\n".join(out))
print('OK', os.path.getsize(dest), 'bytes')
