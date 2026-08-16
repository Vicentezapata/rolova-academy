import json

RUTA = "visual_plan.json"
plan = json.load(open(RUTA, encoding="utf8"))
s = plan["slides"][29]["slots"]
antes = len(s["CODE"].split("\n"))
s["CODE"] = s["CODE"].replace("encode(trozos)\n\nindice", "encode(trozos)\nindice")
json.dump(plan, open(RUTA, "w", encoding="utf8"), ensure_ascii=False, indent=2)
print("slide 29: %d -> %d lineas" % (antes, len(s["CODE"].split("\n"))))
