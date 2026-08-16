# Guía de Estilos EVA — Referencia para la IA

> **LECTURA OBLIGATORIA en Fase 0.** Este archivo define las reglas de uso de temas para la generación de HTML.

---

> **Nota de arquitectura**: Este archivo YA NO describe un sistema de CSS compartido inyectado por script. Cada slide es un documento HTML autocontenido (ver `references/playbooks/bespoke-slide-recipe.md`). Las reglas de abajo se aplican **dentro del `:root` que tú mismo defines una vez por unidad** (el "theme recipe"), no a un archivo `assets/themes/<theme>.css` compartido — ese archivo ya no se enlaza desde las slides.

## Regla Fundamental #1: Variables `:root` propias de la unidad, nunca colores sueltos

Cuando generes las slides de una unidad, **define una vez el `:root` con la paleta del theme recipe** y reutiliza esas variables en todas las slides de esa unidad (copiando el mismo bloque `:root` en cada `<style>`). Evita colores sueltos fuera de esa paleta para que el deck se vea cohesivo — pero los nombres de las variables son tuyos, no tienen que llamarse igual que en otra unidad.

### Variables típicas que conviene definir por unidad (ajusta nombres/valores libremente):

```css
/* Fondos */
--bg-primary        /* Fondo principal de la slide */
--bg-secondary      /* Fondo secundario / cards */

/* Colores de texto */
--text-primary      /* Texto principal (títulos, números) */
--text-secondary    /* Texto secundario (descripciones) */

/* Colores de énfasis */
--accent-1          /* Color de acento principal */
--accent-2          /* Color de acento secundario */
--accent-3          /* Color de acento terciario */
--accent-4          /* Color de acento cuarto (si existe) */

/* Tarjetas */
--card-bg-from      /* Gradiente inicio de tarjeta */
--card-bg-to        /* Gradiente fin de tarjeta */
--card-border       /* Borde de tarjeta */
--card-radius       /* Radio de esquinas de tarjeta */

/* Tipografía */
--display-font      /* Fuente para títulos grandes */
--body-font         /* Fuente para cuerpo de texto */
--mono-font         /* Fuente monoespaciada (código) */
--serif-italic-font /* Fuente serif itálica para énfasis */
```

### ❌ Prohibido:
```html
<!-- MAL: Color hardcoded -->
<h1 style="color: #22D3EE;">Título</h1>
<!-- MAL: Gradiente hardcoded -->
<div style="background: linear-gradient(135deg, #6366f1, #22D3EE);">
```

### ✅ Correcto:
```html
<!-- BIEN: Variable CSS -->
<h1 style="color: var(--accent-1);">Título</h1>
<!-- BIEN: Variables de gradiente -->
<div style="background: linear-gradient(135deg, var(--accent-3), var(--accent-1));">
```

---

## Regla Fundamental #2: Qué escribe la IA (todo) vs. qué escribe el script (casi nada)

El `generate_presentation_template.py` ya **NO inyecta** CSS de tema, decoraciones, footer, ni scripts. La IA escribe el documento HTML COMPLETO de cada slide en `html_content`, incluyendo:

1. `<!DOCTYPE html>`, `<head>` con `<link>` de Google Fonts y scripts (Lordicon/Lucide/Mermaid si aplica).
2. El `<style>` completo: `:root` del theme recipe + decoraciones (glow/grid/grain/stripes) + clases de esa slide.
3. El `<body>` con las decoraciones de fondo, el contenido y el footer/`.slide-num`.
4. El `<script>` final con el listener `keydown` que reenvía teclas al padre (`forward-key`) — es lo único que el visor realmente necesita de ti.

El script solo escribe ese `html_content` tal cual en `slides/slide_NN.html` — no lo envuelve, no lo modifica, no lo sanea.

---

## Regla Fundamental #3: Coordenadas del Canvas

`html, body` deben fijar `width:1280px; height:720px; overflow:hidden`. Dentro de eso:

- **SÍ puedes usar `position: absolute`** para el layout principal (header fijo arriba, `content-area` absoluta, decoraciones que sangran fuera del padding) — así es como lucen las presentaciones de referencia (`UNIDAD 2`, `DESARROLLO DE SOFTWARE WEB I` U2-U4).
- Usa `display: grid`/`flex` donde tenga sentido (grillas de cards, listas).
- Tú decides el padding/estructura de tu propio `.stage`/`.slide` — no hay un wrapper externo que te imponga `72px 96px`.

### Ejemplo de estructura (ver el recipe completo en `references/playbooks/bespoke-slide-recipe.md`):

```html
<div class="content-area">
  <div class="card c1">
    <div class="part-num">Sesión 01</div>
    <h3>Título de la tarjeta</h3>
    <p>Descripción breve del contenido.</p>
  </div>
  <div class="card c2">...</div>
</div>
```

---

## Los 26 Temas Disponibles

> Escribe el `style_id` exacto en el campo `"theme"` del `visual_plan.json`.

| # | `style_id` | Nombre | Mejor para |
|---|------------|--------|------------|
| 1 | `dark_tech` | Dark Tech | IA, SaaS, Tecnología |
| 2 | `xiaomi_orange` | Xiaomi Orange | Hardware, IoT, Automotive |
| 3 | `luxury_purple` | Luxury Purple | Lujo, Alta Gama |
| 4 | `nocturne_violet` | Nocturne Violet | Diseño, Producto digital |
| 5 | `cyberpunk_neon` | Cyberpunk Neon | Gaming, Web3 |
| 6 | `chrome_y2k` | Chrome Y2K | Web3, Retro-futurismo |
| 7 | `noir_film` | Noir Film | Cine, Arte, Documental |
| 8 | `blue_white` | Blue White | Empresa, Formación, Corporativo |
| 9 | `fresh_green` | Fresh Green | Salud, Bienestar, Ecología |
| 10 | `minimal_gray` | Minimal Gray | Académico, Legal, Consultoría |
| 11 | `mocha_editorial` | Mocha Editorial | Publicaciones, IA ética |
| 12 | `medical_pulse` | Medical Pulse | Salud, Farmacia, Seguros |
| 13 | `earth_concrete` | Earth Concrete | Arquitectura, Industria |
| 14 | `champagne_gold` | Champagne Gold | Bodas, Eventos, Lujo |
| 15 | `liquid_glass` | Liquid Glass | XR, AR/VR, Apple |
| 16 | `vibrant_rainbow` | Vibrant Rainbow | Marketing, Creadores |
| 17 | `kindergarten_pop` | Kindergarten Pop | Educación infantil |
| 18 | `bauhaus_block` | Bauhaus Block | Diseño, Educación creativa |
| 19 | `candy_pastel` | Candy Pastel | Repostería, Lifestyle |
| 20 | `royal_red` | Royal Red | Formal, Institucional, Gobierno |
| 21 | `sakura_wabi` | Sakura Wabi | Japonés, Minimalismo |
| 22 | `ink_jade` | Ink Jade | Estilo oriental, Cultura |
| 23 | `botanic_forest` | Botanic Forest | Outdoor, Sustentabilidad |
| 24 | `safari_savanna` | Safari Savanna | Viajes, Aventura |
| 25 | `retro_70s` | Retro 70s | Retro, Café, Música |
| 26 | `gov_authority` | Gov Authority | Gobierno, Eventos oficiales |

---

## Matriz de Decisión para EVA IPSS

| Tipo de Contenido | Tema Recomendado | Alternativa |
|---|---|---|
| Seguridad Social / IPSS / Previsión | `gov_authority` | `blue_white` |
| Salud y Medicina | `medical_pulse` | `fresh_green` |
| Economía / Finanzas | `blue_white` | `minimal_gray` |
| Tecnología / Sistemas | `dark_tech` | `xiaomi_orange` |
| Derecho / Legislación | `minimal_gray` | `mocha_editorial` |
| General / Sin preferencia | `blue_white` | `dark_tech` |

---

## Clases de Referencia (inspiración, no un framework a enlazar)

Estas clases ya NO existen en un `base.css` compartido — son solo nombres típicos que puedes reutilizar/adaptar al escribir el `<style>` de cada slide (defínelas tú mismo en cada archivo):

| Clase | Uso |
|---|---|
| `.card` | Tarjeta estándar con fondo, borde y radio |
| `.card-accent` | Tarjeta con borde de acento superior |
| `.kicker` / `.tag` | Texto eyebrow (pequeño, mayúscula, acento) |
| `.eyebrow` | Texto meta-info (pequeño, gris) |
| `.pill` / `.topic` | Etiqueta pill gris o de color |
| `.gradient-text` | Texto con gradiente (`-webkit-background-clip:text`) — permitido, la exportación es por captura de pantalla |
| `.dim`, `.dim2` / `.text-sec` | Texto secundario / terciario |
| `.divider-accent` | Línea divisora de acento |
| `.slide-num` | Número de página en la esquina, discreto |

> `references/legacy/pipeline-compat.md` describe restricciones de un pipeline SVG que ya no aplica al ensamblaje de slides (que ahora es 100% HTML autocontenido + captura de pantalla para PPTX). No es necesario evitar `blur()`, `mask-image` ni `background-clip:text`.
