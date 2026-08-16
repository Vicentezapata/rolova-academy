import json, sys

ruta = sys.argv[1]
plan = json.load(open(ruta, encoding="utf8"))

cambios = 0
for i, slide in enumerate(plan["slides"], start=1):
    slots = slide.get("slots", {})
    if "TAG_RIGHT" in slots:
        nuevo = "%02d" % i
        if slots["TAG_RIGHT"] != nuevo:
            slots["TAG_RIGHT"] = nuevo
            cambios += 1

json.dump(plan, open(ruta, "w", encoding="utf8"), ensure_ascii=False, indent=2)
print("slides: %d · TAG_RIGHT corregidos: %d" % (len(plan["slides"]), cambios))
