import json, glob, os, re, sys

RAIZ = "/Users/vzapaco/Desktop/Testing Tools/rolova-academy/cursos/INTELIGENCIA ARTIFICIAL/DINTA 2025 4 V17-01-20260720T213252Z-1-001/DINTA 2025 4 V17-01"
CLAVES = ["Clase 10", "Clase 12", "Clase 13", "Clase 14", "Clase 16", "Clase 18", "Clase 20"]

out = []
for ruta in sorted(glob.glob(RAIZ + "/**/*.ipynb", recursive=True)):
    nombre = os.path.basename(ruta)
    if "Vicente Zapata" in nombre or "V2" in nombre or "V3" in nombre:
        continue  # quedarse con la version base, no con las resueltas
    if not any(k in ruta for k in CLAVES):
        continue
    try:
        nb = json.load(open(ruta, encoding="utf8"))
    except Exception:
        continue
    out.append("\n\n# ===== %s =====" % ruta.replace(RAIZ + "/", ""))
    for celda in nb.get("cells", []):
        fuente = "".join(celda.get("source", [])).strip()
        if not fuente:
            continue
        if celda.get("cell_type") == "markdown":
            # solo encabezados y primeras lineas: interesa el temario
            titulos = [l for l in fuente.split("\n") if l.startswith("#")]
            if titulos:
                out.append("\n".join(titulos))
        else:
            imports = [l for l in fuente.split("\n")
                       if re.match(r"\s*(from|import)\s", l)]
            if imports:
                out.append("    [código] " + " | ".join(i.strip() for i in imports[:4]))

dest = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diplomado_temario.md")
open(dest, "w").write("\n".join(out))
print("OK", os.path.getsize(dest), "bytes")
