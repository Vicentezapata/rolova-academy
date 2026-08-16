# Recipe de Slide Autocontenida (Bespoke, un archivo por diapositiva)

> **Lectura obligatoria en Fase 4**, antes de escribir la primera slide del deck.

## Por qué existe este documento

La arquitectura antigua (componentes inyectados desde `assets/base.css` + `assets/themes/<theme>.css`) producía decks genéricos, todos con las mismas clases `.stage / .headline / .label / .deck-footer`, el mismo espaciado y la misma sensación de "plantilla SaaS reciclada" — es lo que se ve en `TESTING APLICADO AL DESARROLLO DE SISTEMAS/UNIDAD 3/presentation`.

El estándar real a igualar es el de estas presentaciones (ábrelas y compáralas visualmente antes de generar nada):
- `TESTING APLICADO AL DESARROLLO DE SISTEMAS/UNIDAD 2/Presentacion unidad 2`
- `DESARROLLO DE SOFTWARE WEB I/UNIDAD 2/Presentacion unidad 2`
- `DESARROLLO DE SOFTWARE WEB I/UNIDAD 3/Presentacion unidad 3`
- `DESARROLLO DE SOFTWARE WEB I/UNIDAD 4/Presentacion unidad 4`

Todas comparten un mismo patrón arquitectónico: **cada `slides/slide_NN.html` es un documento HTML 100% independiente**, sin `<link>` a ningún CSS compartido, con fuentes vía Google Fonts CDN, una paleta `:root` propia de la unidad y 2-3 motivos decorativos de firma repetidos en todas las slides de esa unidad. Ese es el patrón que debes replicar.

---

## 1. El "Theme Recipe" — defínelo UNA VEZ antes de la slide 0

Antes de escribir cualquier slide, decide (y anota mentalmente o en un comentario en tu primer borrador) estos 4 elementos. Luego cópialos literalmente en el `<style>` de cada slide de la unidad:

1. **Fuentes** (Google Fonts, `<link>` en `<head>`): 1 display/heading, 1 body, 1 mono (para tags/labels), opcionalmente 1 serif itálica para énfasis.
2. **Paleta `:root`**: 4-8 variables cortas (`--bg`, `--bg2`, `--text`, `--text-sec`, `--accent1..4`, `--border`).
3. **2-3 motivos decorativos de firma** (elige un combo y repítelo siempre):
   - Textura de fondo (grid-dot, grano SVG `feTurbulence`, warm-wash radial)
   - Un "glow"/orbe difuminado o una franja de rayas (`stripe-band`)
   - Un elemento de esquina o marco (corner brackets, sello, folio)
4. **Convenciones de nombre de clase** propias de esa unidad (`.card`, `.tag`, `.part-num`, `.slide-num`, `.content-area`...). No hace falta que coincidan con las de otra unidad — cada deck tiene su propio pequeño "sistema" interno, consistente solo consigo mismo.

---

## 2. Ejemplo Real #1 — Tema "Dark Tech" (cyan/índigo, técnico)

Extraído de `TESTING APLICADO AL DESARROLLO DE SISTEMAS/UNIDAD 2/Presentacion unidad 2/slides/slide_01.html`. Úsalo como plantilla de arranque para temas tech/SaaS/IA.

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Slide 01 — Tabla de Contenidos</title>
<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800&family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{--bg:#050b1f;--bg2:#0a1f3d;--border:rgba(34,211,238,0.2);--text:#fff;--text-sec:rgba(255,255,255,0.65);--accent1:#22D3EE;--accent2:#6366f1;--accent3:#FDE047;--accent4:#10b981;}
*{margin:0;padding:0;box-sizing:border-box;}
html,body{width:100%;height:100%;overflow:hidden;font-family:'Inter','Inter Tight',sans-serif;background:var(--bg);}
.slide{width:100%;height:100%;position:relative;overflow:hidden;background:radial-gradient(100% 80% at 90% 110%, #082f49 0%, var(--bg) 80%);}
.grid-texture{position:absolute;inset:0;z-index:0;background-image:radial-gradient(rgba(14,165,233,0.08) 1px,transparent 1px);background-size:40px 40px;}
.glow{position:absolute;width:400px;height:400px;border-radius:50%;background:rgba(14,165,233,0.2);filter:blur(70px);top:-60px;right:-60px;z-index:0;}
.header{position:absolute;top:36px;left:48px;right:48px;z-index:10;display:flex;align-items:center;justify-content:space-between;}
.tag{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:0.18em;color:var(--accent1);text-transform:uppercase;}
.title{font-family:'Inter Tight','Inter',sans-serif;font-size:24px;font-weight:800;color:var(--text);letter-spacing:-0.015em;}
.divider{position:absolute;top:80px;left:48px;right:48px;height:1px;background:linear-gradient(90deg,var(--accent1),transparent);opacity:0.4;z-index:10;}
.content-area{position:absolute;left:48px;top:100px;right:48px;bottom:48px;display:grid;grid-template:1fr 1fr / 1fr 1fr;gap:18px;z-index:10;}
.card{background:linear-gradient(135deg,rgba(34,211,238,0.08),rgba(99,102,241,0.04));border:1px solid var(--border);border-radius:8px;padding:28px 32px;display:flex;flex-direction:column;gap:12px;}
.part-num{font-family:'JetBrains Mono',monospace;font-size:11px;letter-spacing:0.18em;text-transform:uppercase;margin-bottom:4px;}
.card-icon{width:48px;height:48px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:20px;margin-bottom:8px;}
.card h3{font-family:'Inter Tight','Inter',sans-serif;font-size:18px;font-weight:700;color:var(--text);line-height:1.25;}
.card p{font-size:13px;color:var(--text-sec);line-height:1.65;}
.topics{display:flex;flex-wrap:wrap;gap:6px;margin-top:4px;}
.topic{background:rgba(255,255,255,0.06);border:1px solid rgba(255,255,255,0.1);border-radius:4px;padding:3px 8px;font-size:10px;color:var(--text-sec);}
.c1 .part-num{color:var(--accent1);} .c1{border-color:rgba(34,211,238,0.3);} .c1 .card-icon{background:rgba(34,211,238,0.12);}
.slide-num{position:absolute;bottom:20px;right:36px;font-family:'JetBrains Mono',monospace;font-size:10px;color:rgba(255,255,255,0.2);z-index:10;}
</style>
<script src="https://cdn.lordicon.com/lordicon.js"></script>
</head>
<body>
<div class="slide">
  <div class="grid-texture"></div>
  <div class="glow"></div>
  <div class="header">
    <span class="tag">Unidad 2 — IF203IINF</span>
    <span class="title">Contenido de la Unidad</span>
    <span class="tag">2026</span>
  </div>
  <div class="divider"></div>
  <div class="content-area">
    <div class="card c1">
      <div class="part-num">Sesión 01</div>
      <div class="card-icon"><lord-icon src="https://cdn.lordicon.com/wxnxiano.json" trigger="loop" delay="1500" colors="primary:#ffffff" style="width:1.5em;height:1.5em;"></lord-icon></div>
      <h3>Selección Estratégica de Tipos de Prueba</h3>
      <p>El Testing depende del contexto. Evaluación de riesgo como inversión de negocio.</p>
      <div class="topics"><span class="topic">Contexto</span><span class="topic">Matriz de Riesgo</span></div>
    </div>
    <!-- ...más .card c2/c3/c4 con la misma estructura... -->
  </div>
  <div class="slide-num">01 / 20</div>
</div>
<script>
document.addEventListener('keydown', e => {
  if (['ArrowLeft','ArrowUp','ArrowRight','ArrowDown',' '].includes(e.key)) e.preventDefault();
  window.parent.postMessage({ type: 'forward-key', key: e.key }, '*');
});
</script>
</body>
</html>
```

**Puntos clave a imitar**: header con `<span class="tag">` a los lados y `<span class="title">` al centro (fijado con `position:absolute`), `.grid-texture` + `.glow` como fondo, `.content-area` con `position:absolute` en vez de flujo normal, cards con `part-num` + icono Lordicon + `h3` + `p` + pills `.topic`, y `.slide-num` discreto en la esquina.

---

## 3. Ejemplo Real #2 — Tema "Warm Retro / Kindergarten" (crema, marrón, naranja)

Extraído de `DESARROLLO DE SOFTWARE WEB I/UNIDAD 4/Presentacion unidad 4/slides/slide_00.html`. Úsalo como plantilla de arranque para temas cálidos/lúdicos/editoriales retro.

```html
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<title>Slide 00</title>
<link href="https://fonts.googleapis.com/css2?family=Bagel+Fat+One&family=Inter+Tight:wght@600;700;800;900&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
<script src="https://cdn.lordicon.com/lordicon.js"></script>
<style>
:root {
  --bg-cream: #f4e9d0; --brown: #6b4423; --orange: #e07a3e; --mustard: #d4a82a; --vermilion: #c14d3f; --ink: #2a1810;
  --display-font: 'Bagel Fat One', 'Inter Tight', sans-serif;
  --body-font: 'Inter', sans-serif;
  --mono-font: 'JetBrains Mono', monospace;
}
* { margin: 0; padding: 0; box-sizing: border-box; }
html, body { width: 100%; height: 100%; overflow: hidden; background: var(--bg-cream); color: var(--ink); font-family: var(--body-font); position: relative; }
.warm-wash { position: absolute; inset: 0; background: radial-gradient(ellipse 60% 45% at 18% 22%, rgba(212,168,42,0.18) 0%, transparent 60%); z-index: 0; }
.stripe-band { position: absolute; left: 0; right: 0; height: 14px; background: repeating-linear-gradient(90deg, var(--brown) 0 36px, var(--orange) 36px 72px, var(--mustard) 72px 108px, var(--vermilion) 108px 144px); z-index: 1; }
.stripe-top { top: 0; } .stripe-bottom { bottom: 0; }
.grain { position: absolute; inset: 0; opacity: 0.08; z-index: 9; pointer-events: none; }
.slide-num { position:absolute; bottom:24px; right:48px; font-family:var(--mono-font); font-size:11px; color:var(--brown); z-index:10; }
.gradient-text{background:linear-gradient(135deg,var(--vermilion),var(--orange),var(--mustard));-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.cover{text-align:center}
.slide-inner { z-index: 10; position: relative; width: 100%; max-width: 1000px; }
.slide { position: relative; display: flex; align-items: center; justify-content: center; padding: 4rem 5rem; height: 100vh; }
.cover-badge{display:inline-flex;gap:.5rem;background:rgba(107,68,35,.04);border:1px solid rgba(107,68,35,.15);border-radius:50px;padding:.45rem 1rem;font-family:var(--mono-font);font-size:.72rem;margin-bottom:2rem}
.cover-title{font-size:clamp(2.5rem,6vw,4.5rem);font-weight:900;line-height:1.08;font-family:var(--display-font);color:var(--brown);text-shadow:2px 2px 0 rgba(193,77,63,0.18);}
.cover-sub{font-size:1.2rem;color:rgba(42,24,16,0.62);margin-top:1rem}
.s-card{background:rgba(255,255,255,0.4);box-shadow:4px 4px 0 rgba(42,24,16,0.85);border:2px solid var(--ink);border-radius:10px;padding:1.5rem;}
</style>
</head>
<body>
<div class="warm-wash"></div><div class="stripe-band stripe-top"></div><div class="stripe-band stripe-bottom"></div>
<svg class="grain" preserveAspectRatio="none"><filter id="g"><feTurbulence type="fractalNoise" baseFrequency="0.85" numOctaves="2"/></filter><rect width="100%" height="100%" filter="url(#g)" fill="#6b4423"/></svg>
<div class="slide cover"><div class="slide-inner">
  <div class="cover-badge">Desarrollo de Software Web I · Unidad 4</div>
  <lord-icon src="https://cdn.lordicon.com/wzwygmng.json" trigger="loop" delay="1500" colors="primary:#6b4423,secondary:#e07a3e" style="width:120px;height:120px;margin-bottom:1rem;"></lord-icon>
  <h1 class="cover-title">Laravel Enterprise:<br><span class="gradient-text">Arquitectura Avanzada</span></h1>
  <p class="cover-sub">Patrones, Testing, Jobs y DevOps</p>
</div></div>
<div class="slide-num">00 / 25</div>
<script>
if (typeof lucide !== 'undefined') lucide.createIcons();
document.addEventListener('keydown', e => {
  if (['ArrowLeft','ArrowUp','ArrowRight','ArrowDown',' '].includes(e.key)) e.preventDefault();
  window.parent.postMessage({ type: 'forward-key', key: e.key }, '*');
});
</script>
</body>
</html>
```

**Puntos clave a imitar**: `stripe-band` arriba/abajo con `repeating-linear-gradient`, textura de grano vía SVG `feTurbulence`, sombra "hard shadow" (`4px 4px 0 var(--ink)`, sin blur) en cards y título, tipografía display juguetona (`Bagel Fat One`) reservada solo para títulos grandes, `.gradient-text` con `-webkit-background-clip:text` (permitido, no lo elimines).

---

## 4. Checklist antes de guardar cada `html_content`

- [ ] `<!DOCTYPE html>` presente y es un documento completo (no un fragmento).
- [ ] `<link>` de Google Fonts propio (no depende de ningún `assets/fonts.css`).
- [ ] `<style>` incluye el mismo bloque `:root` que las demás slides de la unidad (theme recipe).
- [ ] Al menos 2 motivos decorativos de firma del tema presentes (glow/grid/grain/stripes/corners).
- [ ] `html, body { width:1280px... }` o el patrón `.slide{width:100%;height:100vh}` según el recipe elegido — consistente con el resto del deck.
- [ ] `.slide-num` o equivalente en una esquina, discreto.
- [ ] Script final con el listener `keydown` que hace `window.parent.postMessage({ type: 'forward-key', key: e.key }, '*')`.
- [ ] Nada de `<link href="../assets/...">` ni clases genéricas `.stage/.headline/.label/.deck-footer` copiadas de otra unidad sin adaptar.
- [ ] Colores agrupados en la paleta `:root` de la unidad — no colores sueltos improvisados.
