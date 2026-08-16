import json, re

RUTA = "visual_plan.json"
plan = json.load(open(RUTA, encoding="utf8"))
s = plan["slides"][29]["slots"]

viejo = ("    <span class='c-kw'>return</span> llm(<span class='c-str'>f\"Responde SOLO con este contexto. Si no esta, \"</span>\n"
         "               <span class='c-str'>f\"di que no lo sabes.\\n\\n{contexto}\\n\\nP: {pregunta}\"</span>)")
nuevo = ("    orden = <span class='c-str'>\"Usa SOLO el contexto. Si no esta, di que no sabes.\"</span>\n"
         "    <span class='c-kw'>return</span> llm(<span class='c-str'>f\"{orden}\\n\\n{contexto}\\n\\nP: {pregunta}\"</span>)")

assert viejo in s["CODE"], "no se encontro el fragmento"
s["CODE"] = s["CODE"].replace(viejo, nuevo)

json.dump(plan, open(RUTA, "w", encoding="utf8"), ensure_ascii=False, indent=2)

sin_tags = re.sub(r"<[^>]+>", "", s["CODE"])
lineas = sin_tags.split("\n")
print("slide 29: %d lineas, la mas larga %d caracteres" % (len(lineas), max(len(l) for l in lineas)))
