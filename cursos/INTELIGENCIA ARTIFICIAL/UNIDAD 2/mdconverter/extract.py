import re, os, glob, html

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAT = os.path.join(BASE, 'material')


def limpiar_html(texto):
    texto = re.sub(r'(?is)<(script|style)[^>]*>.*?</\1>', ' ', texto)
    texto = re.sub(r'(?i)<br\s*/?>|</(p|div|li|h[1-6]|td|tr)>', '\n', texto)
    texto = re.sub(r'<[^>]+>', ' ', texto)
    texto = html.unescape(texto)
    return [l.strip() for l in texto.split('\n') if len(l.strip()) > 2]


out = []
for f in sorted(glob.glob(os.path.join(MAT, '*.html'))):
    out.append("\n\n# ===== %s =====\n" % os.path.basename(f))
    with open(f, encoding='utf8', errors='ignore') as fh:
        lineas = limpiar_html(fh.read())
    vistas, unicas = set(), []
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
