"""Uso único: genera un theme pack (_frame.html + pack.json) por cada tema de style-gallery.

El mapeo paleta -> tokens es curado a mano; el script solo lo materializa para que
los 26 packs salgan estructuralmente idénticos.
"""
import json
import os

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PACKS = os.path.join(SKILL, "theme-packs")


def rgba(hexv, a):
    h = hexv.lstrip("#")
    r, g, b = int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)
    return f"rgba({r},{g},{b},{a})"


# --- Estrategias visuales -----------------------------------------------------
# Cada preset fija cómo se comportan bordes, sombras y superficies. Las 26 pieles
# caben en cuatro.
PRESETS = {
    "dark_glow": dict(
        bw="1px", rule="1px", radius="8px", radius_lg="14px",
        shadow="none", shadow_sm="none", heavy="800", title_shadow="none",
        card=lambda t: f"linear-gradient(135deg,{rgba(t['a1'],0.08)},{rgba(t['a2'],0.04)})",
        border=lambda t: rgba(t["a1"], 0.20),
        inset_bg="rgba(255,255,255,0.04)", inset_border="rgba(255,255,255,0.08)",
        hairline="rgba(255,255,255,0.06)", zebra="rgba(255,255,255,0.02)",
        code_bg="rgba(0,0,0,0.45)", code_fg="#e2e8f0",
        text=lambda t: "#ffffff", text_sec=lambda t: "rgba(255,255,255,0.65)",
        text_ter=lambda t: "rgba(255,255,255,0.35)", strong=lambda t: "#ffffff",
        alpha=(0.13, 0.34),
    ),
    "light_soft": dict(
        bw="1px", rule="1px", radius="10px", radius_lg="16px",
        shadow=lambda t: f"0 2px 10px {rgba(t['ink'],0.07)}", shadow_sm="none",
        heavy="800", title_shadow="none",
        card=lambda t: "#ffffff",
        border=lambda t: rgba(t["ink"], 0.13),
        inset_bg=lambda t: rgba(t["ink"], 0.035), inset_border=lambda t: rgba(t["ink"], 0.10),
        hairline=lambda t: rgba(t["ink"], 0.09), zebra=lambda t: rgba(t["ink"], 0.025),
        code_bg=lambda t: rgba(t["ink"], 0.05), code_fg=lambda t: t["ink"],
        text=lambda t: t["ink"], text_sec=lambda t: rgba(t["ink"], 0.66),
        text_ter=lambda t: rgba(t["ink"], 0.40), strong=lambda t: t["ink"],
        alpha=(0.10, 0.30),
    ),
    "print_rule": dict(
        bw="1px", rule="2px", radius="2px", radius_lg="3px",
        shadow="none", shadow_sm="none", heavy="700", title_shadow="none",
        card=lambda t: "#ffffff",
        border=lambda t: rgba(t["ink"], 0.18),
        inset_bg=lambda t: rgba(t["ink"], 0.04), inset_border=lambda t: rgba(t["ink"], 0.14),
        hairline=lambda t: rgba(t["ink"], 0.14), zebra=lambda t: rgba(t["ink"], 0.03),
        code_bg=lambda t: rgba(t["ink"], 0.05), code_fg=lambda t: t["ink"],
        text=lambda t: t["ink"], text_sec=lambda t: rgba(t["ink"], 0.68),
        text_ter=lambda t: rgba(t["ink"], 0.42), strong=lambda t: t["ink"],
        alpha=(0.09, 0.30),
    ),
    "bold_block": dict(
        bw="2px", rule="3px", radius="10px", radius_lg="14px",
        shadow=lambda t: f"4px 4px 0 {rgba(t['ink'],0.85)}",
        shadow_sm=lambda t: f"3px 3px 0 {rgba(t['ink'],0.85)}",
        heavy="900", title_shadow=lambda t: f"2px 2px 0 {rgba(t['a2'],0.20)}",
        card="rgba(255,255,255,0.45)",
        border=lambda t: t["ink"],
        inset_bg="rgba(255,255,255,0.55)", inset_border=lambda t: rgba(t["ink"], 0.35),
        hairline=lambda t: rgba(t["ink"], 0.16), zebra=lambda t: rgba(t["ink"], 0.05),
        code_bg="rgba(255,255,255,0.72)", code_fg=lambda t: t["ink"],
        text=lambda t: t["ink"], text_sec=lambda t: rgba(t["ink"], 0.62),
        text_ter=lambda t: rgba(t["ink"], 0.38), strong=lambda t: t["strong_c"],
        alpha=(0.20, 0.85),
    ),
}

# --- Decoraciones de firma ----------------------------------------------------
DECOS = {
    "grid_glow": lambda t: f""".deco-a{{position:absolute;inset:0;z-index:0;background-image:radial-gradient({rgba(t['a2'],0.08)} 1px,transparent 1px);background-size:40px 40px;}}
.deco-b{{position:absolute;width:400px;height:400px;border-radius:50%;background:{rgba(t['a1'],0.20)};filter:blur(75px);z-index:0;{{{{GLOW_POS}}}}}}
.deco-c{{display:none;}}""",
    "scanline": lambda t: f""".deco-a{{position:absolute;inset:0;z-index:0;background-image:linear-gradient({rgba(t['a1'],0.05)} 1px,transparent 1px),linear-gradient(90deg,{rgba(t['a1'],0.05)} 1px,transparent 1px);background-size:44px 44px;}}
.deco-b{{position:absolute;width:520px;height:360px;border-radius:50%;background:{rgba(t['a2'],0.22)};filter:blur(90px);z-index:0;{{{{GLOW_POS}}}}}}
.deco-c{{position:absolute;left:0;right:0;bottom:0;height:2px;z-index:1;background:linear-gradient(90deg,transparent,{t['a1']},{t['a2']},transparent);opacity:.65;}}""",
    "wash": lambda t: f""".deco-a{{position:absolute;inset:0;z-index:0;background:radial-gradient(ellipse 62% 46% at 18% 20%, {rgba(t['a1'],0.13)} 0%, transparent 62%),radial-gradient(ellipse 56% 42% at 84% 82%, {rgba(t['a2'],0.11)} 0%, transparent 66%);}}
.deco-b{{position:absolute;width:380px;height:380px;border-radius:50%;background:{rgba(t['a3'],0.14)};filter:blur(80px);z-index:0;{{{{GLOW_POS}}}}}}
.deco-c{{display:none;}}""",
    "stripes": lambda t: f""".deco-a{{position:absolute;inset:0;z-index:0;background:radial-gradient(ellipse 60% 45% at 20% 22%, {rgba(t['a3'],0.18)} 0%, transparent 60%),radial-gradient(ellipse 55% 40% at 84% 82%, {rgba(t['a1'],0.14)} 0%, transparent 65%);}}
.deco-b{{position:absolute;left:0;right:0;top:0;height:14px;z-index:1;opacity:.78;background:repeating-linear-gradient(90deg,{t['strong_c']} 0 36px,{t['a1']} 36px 72px,{t['a3']} 72px 108px,{t['a2']} 108px 144px);}}
.deco-c{{position:absolute;left:0;right:0;bottom:0;height:14px;z-index:1;opacity:.78;background:repeating-linear-gradient(90deg,{t['strong_c']} 0 36px,{t['a1']} 36px 72px,{t['a3']} 72px 108px,{t['a2']} 108px 144px);}}""",
    "rules": lambda t: f""".deco-a{{position:absolute;top:0;left:0;right:0;height:4px;z-index:1;background:{t['a2']};}}
.deco-b{{position:absolute;top:14px;left:48px;right:48px;height:1px;z-index:1;background:{rgba(t['ink'],0.16)};}}
.deco-c{{position:absolute;bottom:34px;left:48px;right:48px;height:1px;z-index:1;background:{rgba(t['ink'],0.16)};}}""",
    "vignette": lambda t: f""".deco-a{{position:absolute;inset:0;z-index:0;background:radial-gradient(ellipse 75% 65% at 50% 42%, transparent 0%, {rgba(t['bg'],0.85)} 100%);}}
.deco-b{{position:absolute;width:440px;height:440px;border-radius:50%;background:{rgba(t['a1'],0.14)};filter:blur(100px);z-index:0;{{{{GLOW_POS}}}}}}
.deco-c{{position:absolute;inset:22px;border:1px solid {rgba(t['a1'],0.18)};z-index:1;pointer-events:none;}}""",
}

GLOWS = [
    "top:-80px;right:-60px;", "top:-60px;left:-60px;", "bottom:-80px;right:-40px;",
    "top:50%;left:50%;transform:translate(-50%,-50%);", "bottom:-60px;left:20%;", "top:-70px;right:25%;",
]

# --- Especificación curada de los 26 temas ------------------------------------
F_INTER = "Inter:wght@400;500;600;700;800"
F_TIGHT = "Inter+Tight:wght@500;600;700;800;900"
F_MONO = "JetBrains+Mono:wght@400;500;700"
F_SERIF = "Instrument+Serif:ital@0;1"

T = [
  # id, nombre, preset, deco, bg, bg2, ink, a1, a2, a3, display_xl, fonts_extra, para
  # bauhaus_block se escribió a mano (regla suiza, sin radio ni sombra): no regenerar.
  ("blue_white","Blue White","light_soft","wash","#ffffff","#f6f8fb","#0a1d3a","#2563EB","#1D4ED8","#64748b",None,[F_SERIF],["Corporativo","Formación","Empresa"]),
  # botanic_forest se escribió a mano (display serif + cordillera): no regenerar.
  # candy_pastel se escribió a mano (display cursivo + orbe brillante): no regenerar.
  ("champagne_gold","Champagne Gold","light_soft","wash","#faf6ed","#f3ead0","#2a2218","#c9a35a","#b88d3a","#8e6a25","Playfair Display",["Playfair+Display:wght@500;600;700"],["Eventos","Bodas","Lujo"]),
  ("chrome_y2k","Chrome Y2K","dark_glow","scanline","#0a0518","#1a0d3a","#e8eef6","#00d4ff","#ff6bcd","#a0a0e8",None,[],["Web3","Retrofuturismo","Gaming"]),
  # cyberpunk_neon se escribió a mano (esquinas clip-path + aberración cromática): no regenerar.
  # earth_concrete se escribió a mano (grano de cemento + marcas de corte): no regenerar.
  # fresh_green se escribió a mano (hojas botánicas + filetes): no regenerar.
  # gov_authority se escribió a mano (franjas bicolor + escuadras): no regenerar.
  # ink_jade se escribió a mano (aguadas de tinta + sellos + pincel): no regenerar.
  # kindergarten_pop se escribió a mano (blobs pastel + radio 28px): no regenerar.
  # liquid_glass se escribió a mano (vidrio esmerilado sobre malla): no regenerar.
  # luxury_purple se escribió a mano (noir + oro, cero radio): no regenerar.
  # medical_pulse se escribió a mano (retícula + halo + traza de ECG): no regenerar.
  # minimal_gray se escribió a mano (filete de 2px + marco interior): no regenerar.
  # mocha_editorial se escribió a mano (papel moca + cursiva Instrument): no regenerar.
  # nocturne_violet se escribió a mano (aurora desenfocada + vidrio violeta): no regenerar.
  # noir_film se escribió a mano (grano de emulsión + perforaciones 35 mm): no regenerar.
  ("retro_70s","Retro 70s","bold_block","stripes","#f4e9d0","#ebdcb2","#2a1810","#e07a3e","#c14d3f","#d4a82a","Bagel Fat One",["Bagel+Fat+One"],["Retro","Café","Música"]),
  # royal_red se escribió a mano (laca oxblood + escuadras de oro): no regenerar.
  # safari_savanna se escribió a mano (doble marco + horizonte): no regenerar.
  # sakura_wabi se escribió a mano (washi + punto de sakura): no regenerar.
  # vibrant_rainbow se escribió a mano (esferas de vidrio con especular): no regenerar.
  # xiaomi_orange se escribió a mano (brasa al pie + ticks): no regenerar.
]

FRAME = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="color-scheme" content="{scheme}">
<title>{{{{SLIDE_TITLE}}}}</title>
<link href="https://fonts.googleapis.com/css2?{fonts}&display=swap" rel="stylesheet">
<style>
/* ===== TOKENS DEL PACK — ver theme-packs/TOKENS.md ===== */
:root{{
  --bg:{bg}; --bg2:{bg2};
  --text:{text}; --text-sec:{text_sec}; --text-ter:{text_ter};
  --strong:{strong};

  --a1:{a1}; --a2:{a2}; --a3:{a3};
  --ok:{ok}; --warn:{warn}; --err:{err};
  --a1-t:{a1t}; --a1-b:{a1b};
  --a2-t:{a2t}; --a2-b:{a2b};
  --a3-t:{a3t}; --a3-b:{a3b};
  --ok-t:{okt}; --ok-b:{okb};
  --warn-t:{warnt}; --warn-b:{warnb};
  --err-t:{errt}; --err-b:{errb};

  --card-bg:{card}; --border:{border}; --bw:{bw}; --rule-h:{rule};
  --radius:{radius}; --radius-lg:{radius_lg};
  --shadow:{shadow}; --shadow-sm:{shadow_sm};
  --inset-bg:{inset_bg}; --inset-border:{inset_border};
  --hi-bg:{hi}; --hairline:{hairline}; --zebra:{zebra}; --thead-bg:{thead};

  --code-bg:{code_bg}; --code-fg:{code_fg};
  --c-kw:{a2}; --c-fn:{a1}; --c-str:{ok}; --c-cm:{text_ter}; --c-num:{a3};

  --display:{display};
  --display-xl:{display_xl};
  --body:{body};
  --mono:{mono};
  --serif:{serif};
  --title-shadow:{title_shadow};
  --em-family:var(--serif); --em-style:{em_style}; --em-weight:400;
  --heavy:{heavy};

  --mermaid-primary:{bg2}; --mermaid-text:{text}; --mermaid-border:{a1};
  --mermaid-line:{a2}; --mermaid-secondary:{bg}; --mermaid-tertiary:{bg2};
}}
{{{{SHARED_CSS}}}}

/* ===== DECORACIONES DE FIRMA DEL PACK ===== */
{deco}
.slide{{background:{{{{BG}}}};}}

{{{{EXTRA_CSS}}}}
</style>
<script src="https://cdn.lordicon.com/lordicon.js"></script>
</head>
<body>
<main class="slide" role="region" aria-label="{{{{SLIDE_TITLE}}}}">
  <div class="deco-a" aria-hidden="true"></div>
  <div class="deco-b" aria-hidden="true"></div>
  <div class="deco-c" aria-hidden="true"></div>
{{{{BODY}}}}
  <div class="slide-num">{{{{SLIDE_NUM}}}} / {{{{TOTAL}}}}</div>
</main>
<script>
  document.addEventListener('keydown', e => {{
    if (['ArrowLeft','ArrowUp','ArrowRight','ArrowDown',' ','+','-'].includes(e.key)) e.preventDefault();
    window.parent.postMessage({{ type: 'forward-key', key: e.key }}, '*');
  }});
  window.addEventListener('message', e => {{
    if (e.data && e.data.type === 'text-zoom') {{
      const content = document.querySelector('.content') || document.querySelector('.slide');
      if (content) content.style.zoom = e.data.scale;
    }}
  }});
</script>
</body>
</html>
"""


def resolve(v, t):
    return v(t) if callable(v) else v


built = []
for (tid, name, preset_id, deco_id, bg, bg2, ink, a1, a2, a3, dxl, extra, best) in T:
    p = PRESETS[preset_id]
    dark = preset_id == "dark_glow"
    t = dict(bg=bg, bg2=bg2, ink=ink, a1=a1, a2=a2, a3=a3, strong_c=ink)

    ok = "#6ee7b7" if dark else "#166534"
    warn = "#fcd34d" if dark else "#a16207"
    err = "#fca5a5" if dark else "#9f1239"
    lo, hi = p["alpha"]

    fonts = "&".join(f"family={f}" for f in dict.fromkeys([F_TIGHT, F_INTER, F_MONO] + extra))
    display = "'Inter Tight','Inter',sans-serif"
    serif = f"'{dxl}',Georgia,serif" if dxl else "'Instrument Serif',Georgia,serif"
    if dxl and "family=Instrument" not in fonts and dxl not in ("Orbitron", "Bagel Fat One"):
        pass
    display_xl = f"'{dxl}',{display}" if dxl else display

    frame = FRAME.format(
        scheme="dark" if dark else "light",
        fonts=fonts,
        bg=bg, bg2=bg2,
        text=resolve(p["text"], t), text_sec=resolve(p["text_sec"], t),
        text_ter=resolve(p["text_ter"], t), strong=resolve(p["strong"], t),
        a1=a1, a2=a2, a3=a3, ok=ok, warn=warn, err=err,
        a1t=rgba(a1, lo), a1b=rgba(a1, hi),
        a2t=rgba(a2, lo), a2b=rgba(a2, hi),
        a3t=rgba(a3, lo), a3b=rgba(a3, hi),
        okt=rgba(ok, lo), okb=rgba(ok, hi),
        warnt=rgba(warn, lo), warnb=rgba(warn, hi),
        errt=rgba(err, lo), errb=rgba(err, hi),
        card=resolve(p["card"], t), border=resolve(p["border"], t),
        bw=p["bw"], rule=p["rule"], radius=p["radius"], radius_lg=p["radius_lg"],
        shadow=resolve(p["shadow"], t), shadow_sm=resolve(p["shadow_sm"], t),
        inset_bg=resolve(p["inset_bg"], t), inset_border=resolve(p["inset_border"], t),
        hi=rgba(a1, 0.07 if dark else 0.10),
        hairline=resolve(p["hairline"], t), zebra=resolve(p["zebra"], t),
        thead=rgba(a2, 0.18 if dark else 0.12),
        code_bg=resolve(p["code_bg"], t), code_fg=resolve(p["code_fg"], t),
        display=display, display_xl=display_xl,
        body="'Inter',sans-serif", mono="'JetBrains Mono',monospace", serif=serif,
        title_shadow=resolve(p["title_shadow"], t),
        em_style="normal" if dxl in ("Bagel Fat One", "Orbitron") else "italic",
        heavy=p["heavy"],
        deco=DECOS[deco_id](t),
    )

    tints = [rgba(a1, 0.10), rgba(a2, 0.08), rgba(a3, 0.09)]
    rhythm = []
    for i in range(4):
        bgv = (f"radial-gradient(100% 80% at {['70% 120%','90% 110%','10% 110%','70% -10%'][i]}, "
               f"{tints[i % 3]} 0%, var(--bg) 78%)")
        rhythm.append({"BG": bgv, "GLOW_POS": GLOWS[i % len(GLOWS)]})

    pack = {
        "id": tid, "name": name,
        "source": f"Generado desde style-gallery/{tid}.html sobre el contrato de tokens",
        "best_for": best,
        "preset": preset_id, "decoration": deco_id,
        "palette": {"bg": bg, "text": resolve(p["text"], t), "a1": a1, "a2": a2, "a3": a3},
        "_comment_rhythm": "El renderer rota estas variantes por índice de slide.",
        "background_rhythm": rhythm,
    }

    d = os.path.join(PACKS, tid)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "_frame.html"), "w", encoding="utf-8") as f:
        f.write(frame)
    with open(os.path.join(d, "pack.json"), "w", encoding="utf-8") as f:
        json.dump(pack, f, ensure_ascii=False, indent=2)
    built.append(tid)

print(f"{len(built)} theme packs generados:")
for b in built:
    print("  -", b)
