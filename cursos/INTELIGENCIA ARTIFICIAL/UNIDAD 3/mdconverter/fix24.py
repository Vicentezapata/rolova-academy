import json

RUTA = "visual_plan.json"

def kw(t):  return "<span class='c-kw'>%s</span>" % t
def num(t): return "<span class='c-num'>%s</span>" % t
def s(t):   return "<span class='c-str'>%s</span>" % t
def cm(t):  return "<span class='c-cm'>%s</span>" % t

CODE = "\n".join([
    "base = tf.keras.applications.MobileNetV2(",
    "    input_shape=(%s, %s, %s), include_top=%s,   %s" % (num(224), num(224), num(3), kw("False"), cm("# sin su ultima capa")),
    "    weights=%s)                             %s" % (s('"imagenet"'), cm("# con lo que ya aprendio")),
    "",
    cm("# -- FASE 1 - el chef no toca nada, solo aprende la carta nueva --"),
    "base.trainable = %s" % kw("False"),
    "modelo = tf.keras.Sequential([",
    "    base,",
    "    layers.GlobalAveragePooling2D(),",
    "    layers.Dropout(%s)," % num("0.3"),
    "    layers.Dense(N_CLASES, activation=%s)    %s" % (s('"softmax"'), cm("# TUS clases")),
    "])",
    "modelo.compile(optimizer=Adam(%s), loss=%s)" % (num("1e-3"), s('"..."')),
    "modelo.fit(X_ent, y_ent, epochs=%s)" % num(10),
    "",
    cm("# -- FASE 2 - afinar con tasa MUY baja --"),
    "base.trainable = %s" % kw("True"),
    "%s capa %s base.layers[:-%s]: capa.trainable = %s   %s" % (kw("for"), kw("in"), num(30), kw("False"), cm("# solo las 30 ultimas")),
    "modelo.compile(optimizer=Adam(%s), loss=%s)        %s" % (num("1e-5"), s('"..."'), cm("# 100x menor")),
    "modelo.fit(X_ent, y_ent, epochs=%s)" % num(5),
])

CODE = (CODE.replace("ultima", "\u00faltima").replace("aprendio", "aprendi\u00f3")
            .replace("ultimas", "\u00faltimas").replace("100x", "100\u00d7")
            .replace("--", "\u2500\u2500"))

plan = json.load(open(RUTA, encoding="utf8"))
plan["slides"][24]["slots"]["CODE"] = CODE
json.dump(plan, open(RUTA, "w", encoding="utf8"), ensure_ascii=False, indent=2)
print("slide 24 -> %d lineas" % len(CODE.split("\n")))
