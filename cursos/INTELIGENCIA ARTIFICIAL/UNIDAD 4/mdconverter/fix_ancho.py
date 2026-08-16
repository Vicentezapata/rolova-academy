import json, re

RUTA = "visual_plan.json"
plan = json.load(open(RUTA, encoding="utf8"))

reemplazos = [
    (8,
     "layers.Embedding(num_words, <span class='c-num'>100</span>, weights=[matriz], trainable=<span class='c-kw'>False</span>)",
     "layers.Embedding(num_words, <span class='c-num'>100</span>,\n                 weights=[matriz], trainable=<span class='c-kw'>False</span>)"),
    (48,
     "<span class='c-kw'>from</span> tensorflow.keras.preprocessing.image <span class='c-kw'>import</span> ImageDataGenerator",
     "<span class='c-kw'>from</span> tensorflow.keras.preprocessing.image <span class='c-kw'>import</span> (\n    ImageDataGenerator)"),
]

for i, viejo, nuevo in reemplazos:
    c = plan["slides"][i]["slots"]["CODE"]
    assert viejo in c, "slide %d: fragmento no encontrado" % i
    plan["slides"][i]["slots"]["CODE"] = c.replace(viejo, nuevo)

json.dump(plan, open(RUTA, "w", encoding="utf8"), ensure_ascii=False, indent=2)

for i, s in enumerate(plan["slides"]):
    c = s["slots"].get("CODE")
    if not c:
        continue
    ls = re.sub(r"<[^>]+>", "", c).split("\n")
    print("slide %02d  max=%2d  lineas=%2d  %s" % (i, max(len(l) for l in ls), len(ls), s["title"][:34]))
