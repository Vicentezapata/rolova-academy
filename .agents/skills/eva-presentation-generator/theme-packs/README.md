# Theme Packs — Catálogo de Arquetipos

> **Este archivo es de lectura obligatoria en Fase 2 y Fase 4.** Define QUÉ arquetipo usar para CADA tipo de contenido. Si eliges bien aquí, no hay que iterar después.

## Por qué existen los packs

Se midieron las 4 presentaciones de referencia de la academia (Testing U2, DSW U2/U3/U4). Resultado:

| Deck | Slides | Clases presentes en **100%** de las slides |
|---|---|---|
| DSW U3 | 25 | `warm-wash`, `stripe-top`, `stripe-bottom`, `grain`, `slide-inner`, `slide-num` |
| DSW U4 | 26 | las mismas 6 |
| Testing U2 | 20 | `grid-texture`, `glow`, `slide-num` |

**Conclusión: esos decks NO son diseño único por slide. Son un marco fijo + ~6 arquetipos repetidos.** Aproximadamente el 45% de cada archivo es idéntico entre slides.

Por eso el agente **no escribe HTML**. Escribe solo strings de contenido; el `_frame.html` del pack se inyecta byte a byte idéntico en todas las slides. Eso es lo que elimina la deriva visual a partir de la slide ~8 y hace el resultado certero al primer intento.

---

## Packs disponibles

**28 packs**, todos con **exactamente los mismos 30 arquetipos**. Cambiar de pack no cambia el contenido ni la estructura: solo la piel.
Para verlos, abre `gallery/index.html` (se regenera con `python scripts/make_gallery.py`).

| `pack` | Nombre | Ideal para |
|---|---|---|
| `bauhaus_block` | Bauhaus Block | Diseño, educación creativa, talleres, arquitectura |
| `blue_white` | Blue White | Corporativo, formación, empresa |
| `botanic_forest` | Botanic Forest | Sostenibilidad, medio ambiente, outdoor, diario de campo |
| `candy_pastel` | Candy Pastel | Repostería, lifestyle, infantil, marca de consumo |
| `champagne_gold` | Champagne Gold | Eventos, bodas, lujo |
| `chrome_y2k` | Chrome Y2K | Web3, retrofuturismo, gaming |
| `cyberpunk_neon` | Cyberpunk Neon | Gaming, ciberseguridad, Web3, hackathon |
| `dark_tech` | Dark Tech | Tecnología, Testing/QA, sistemas, IA, desarrollo |
| `earth_concrete` | Earth Concrete | Arquitectura, construcción, industria, portafolio de estudio |
| `editorial_paper` | Editorial Paper | Académico, legal, investigación, informes, texto denso |
| `fresh_green` | Fresh Green | Sostenibilidad, salud y bienestar, agroindustria, marca artesanal |
| `gov_authority` | Gov Authority | Sector público, normativa, informes institucionales, comités |
| `ink_jade` | Ink Jade | Humanidades, filosofía y ética, cultura y patrimonio |
| `kindergarten_pop` | Kindergarten Pop | Educación infantil, talleres, divulgación, onboarding amable |
| `liquid_glass` | Liquid Glass | XR/visionOS, producto Apple, lanzamientos, diseño de interfaz |
| `luxury_purple` | Maison Noir | Lujo, alta gama, ceremonias, marca premium |
| `medical_pulse` | Medical Pulse | Salud y medicina, biotecnología, datos clínicos, SaaS técnico |
| `minimal_gray` | Minimal Gray | Ensayo y opinión, informes de investigación, arquitectura y diseño |
| `mocha_editorial` | Mocha Editorial | Ensayo largo, investigación y ciencia, documentación reflexiva |
| `nocturne_violet` | Nocturne Violet | Producto digital, release notes, estudio creativo |
| `noir_film` | Noir Film | Fotografía y cine, portafolio de autor, retrospectiva, narrativa visual |
| `retro_70s` | Retro 70s | Retro, café, música |
| `retro_warm` | Retro Warm | Programación web, frameworks, contenido con mucho código |
| `royal_red` | Royal Red | Ceremonia y protocolo, patrimonio cultural, gala y premios |
| `safari_savanna` | Safari Savanna | Expedición y campo, geografía y naturaleza, bitácora, revista de viaje |
| `sakura_wabi` | Sakura Wabi | Filosofía y contemplación, mindfulness, cierre de sesión |
| `vibrant_rainbow` | Vibrant Rainbow | Keynote de producto, fintech, lanzamiento, evento y conferencia |
| `xiaomi_orange` | Xiaomi Orange | Lanzamiento de hardware, ingeniería y specs, keynote técnico |

> `minimal_gray` y `mocha_editorial` son parientes cercanos (papel cálido + serif). Elige `minimal_gray` para un tono más se-
co y periodístico, `mocha_editorial` para uno más cálido y de autor.

### Arquitectura

```
theme-packs/
  _shared/               ← los 30 arquetipos + primitivas, sin un solo color literal
    aNN-*.html
    _base.css
    _runtime.js          ← iconos Lordicon y normalización de gráficos, inyectado en cada slide
    archetypes.json      ← slots y listas de cada arquetipo (consúltalo antes de escribir el plan)
    icons.json           ← catálogo de iconos Lordicon verificados contra el CDN
  <pack>/
    _frame.html          ← tokens del tema + decoraciones de firma
    pack.json            ← identidad + ritmo de fondos
  TOKENS.md              ← solo si vas a crear un pack nuevo
```

Un pack son **2 archivos**. Los arquetipos no se duplican por tema, así que añadir un arquetipo lo gana cada pack a la vez y es imposible que se desincronicen.

---

## Matriz de decisión: contenido → arquetipo

Usa la **primera fila que encaje**. Si dudas entre dos, elige el de más arriba.

| Si el contenido de la slide es… | Arquetipo | Nota |
|---|---|---|
| La apertura de la unidad | `cover` | Siempre slide 0, una sola vez |
| El mapa de sesiones / temario | `toc` | Slide 1, una sola vez |
| El inicio de un bloque temático nuevo | `section` | 1 cada 4-5 slides. **Obligatorio** para dar respiro |
| Un principio o ley + sus factores + casos | `principle` | ★ Panel grande con número fantasma + 2 casos con cifra al lado |
| Una cifra, porcentaje o dato de impacto | `metrics` | ★ 2-4 números grandes. No lo entierres en un párrafo |
| Un dato comparado entre categorías | `chart-bars` | ▲ Columnas a pantalla casi completa. Cuando el dato **es** el mensaje |
| Un ranking donde la cifra exacta importa | `chart-split` | ▲ Barras + tabla de valores + lectura |
| Varias lecturas a la vez de un mismo periodo | `chart-grid` | ▲ Panel 2×2: donut, columnas, apilado, sparkline |
| Porcentajes contra una meta | `gauges` | ▲ Anillos de progreso. El valor se lee siempre sobre 100 |
| Evolución de una cifra en el tiempo | `trend` | ▲ Línea con área + hitos al lado |
| Dos enfoques opuestos (A vs B, antes/después) | `comparison` | Trae divisor central y badge "VS" |
| N opciones × M criterios con ✓/✗ | `feature-matrix` | ★ Tabla comparativa de herramientas o frameworks |
| Malas prácticas frente a buenas prácticas | `dodont` | ★ Con snippets de código a cada lado |
| Avisos, riesgos, tips sueltos | `callouts` | ★ info / tip / warn / danger / note |
| Un proceso con fases o pasos ordenados | `timeline` | ★ Nodos numerados conectados |
| Un flujo con ramas o decisiones | `diagram` | ★ Mermaid + leyenda lateral |
| Fases con estado (hecho / en curso / futuro) | `roadmap` | ★ Carriles con píldoras de estado |
| Clasificación en 2 ejes, 4 cuadrantes | `matrix` | ★ Cuadrantes + reglas de lectura |
| Clasificación en 2 ejes, 9 niveles de calor | `heatmap` | ★ Rejilla 3×3 + zonas explicadas |
| Código que hay que explicar línea a línea | `code` | Pasos numerados + ventana de código |
| Código largo + checklist de criterios | `code-criteria` | ★ Gherkin/YAML + siglas tipo INVEST al lado |
| La estructura interna de un artefacto | `anatomy` | ★ Campos etiquetados + notas ancladas |
| Muchas filas de datos (rúbrica, RTM) | `table` | Cabecera fija + pills de estado |
| Panorámica mixta de cifras y conceptos | `bento` | ★ Rejilla 6×6 con tiles de distinto tamaño |
| Una afirmación de autoridad / idea a fijar | `quote` | ★ Pantalla completa. Úsalo tras 2-3 slides densas |
| Verificar comprensión del alumno | `quiz` | ★ Interactivo: clic o tecla `R` revela |
| Un ejercicio práctico con casos | `activity` | Cabecera + 2-3 tarjetas de caso |
| 2-4 conceptos paralelos del mismo nivel | `concept-cards` | El caballo de batalla. **Máx. 3 seguidas** |
| Lecturas, enlaces, material extra | `resources` | ★ Lista + código QR generado al vuelo |
| Síntesis final + próximos pasos | `closing` | Última slide de contenido |

★ = arquetipo nuevo, no existía en los decks originales.
▲ = arquetipo de gráfico. **Entrega siempre el valor crudo** (`"38.5"`), nunca un porcentaje ni una altura: `_runtime.js` normaliza contra el máximo de la serie — o contra 100 en `gauges` — y calcula alturas, ángulos y trazados. El color codifica categoría; la longitud codifica magnitud.

### Iconos animados

Cualquier slot `ICON` / `icon` acepta un emoji (queda como texto) o un **ID de Lordicon de 8 caracteres**, que `_runtime.js` convierte en icono animado coloreado con `--a1` y `--a2` del pack. Usa solo IDs de `_shared/icons.json`: están verificados contra el CDN. **Un ID inventado o retirado se renderiza como un hueco vacío, sin error.** Muéstralos con `gallery/icons.html`.

---

## Densidad: cuántos elementos por arquetipo

Los arquetipos están calibrados para el lienzo de 1280×720. **Quedarse corto deja huecos muertos; pasarse desborda.** Respeta estos rangos.

| Arquetipo | Lista | Mínimo | Óptimo | Máximo | Si te quedas corto… |
|---|---|---|---|---|---|
| `cover` | `CHIPS` | 2 | 3 | 4 | — |
| `toc` | `ITEMS` | 3 | 4 | 6 | Ajusta `ROWS`/`COLS` (4 ítems → `2`/`2`; 3 o 6 → `1`/`3` o `2`/`3`) |
| `section` | `AGENDA` | 2 | 3 | 4 | — |
| `concept-cards` | `CARDS` | 2 | 3 | 4 | `COLS` debe igualar el nº de tarjetas |
| `comparison` | `LEFT_POINTS` / `RIGHT_POINTS` | 2 | 3 | 4 | Añade `RIGHT_TAGS` para rellenar la columna derecha |
| `activity` | `CASES` | 2 | 3 | 3 | `COLS` = nº de casos |
| `code` | `STEPS` | 3 | 4 | 6 | Sube `SPLIT` a `1fr 1.2fr` para dar más peso al código |
| `table` | `ROWS` | 4 | 6 | 9 | Con menos de 4 filas usa `concept-cards` |
| `metrics` | `METRICS` | 2 | 3 | 4 | `COLS` = nº de métricas |
| `timeline` | `STEPS` | 3 | 4 | 5 | `COLS` = nº de pasos |
| `matrix` | `RULES` | 2 | 3 | 4 | Los 4 cuadrantes son obligatorios |
| `quiz` | `OPTIONS` | 3 | 4 | 4 | `COLS` = `2` con 4 opciones, `1` con 3 |
| `dodont` | `BAD_POINTS` / `GOOD_POINTS` | 3 | 4 | 5 | **Con 3 bullets cortos queda hueco**: alarga los textos o sube a 4-5 |
| `anatomy` | `FIELDS` / `NOTES` | 5 / 2 | 7 / 3 | 9 / 4 | Marca 1-2 campos con `"highlight": "hi"` |
| `closing` | `TAKEAWAYS` / `NEXT_STEPS` | 3 / 2 | 4 / 3 | 5 / 4 | — |
| `principle` | `FACTORS` / `EXAMPLES` | 3 / 2 | 4 / 2 | 5 / 2 | `EXAMPLES` debe ser exactamente 2 |
| `heatmap` | `CELLS` / `ZONES` | 9 / 3 | 9 / 3 | 9 / 4 | `CELLS` **siempre 9** (rejilla 3×3), en orden fila superior → inferior |
| `code-criteria` | `CRITERIA` | 4 | 6 | 8 | Marca la fila clave con `"highlight": "hi"` |
| `bento` | `TILES` | 4 | 6 | 8 | `col`/`row` en sintaxis grid (`"1 / 4"`); cubre las 6×6 celdas sin huecos |
| `callouts` | `CALLOUTS` | 3 | 4 | 5 | Varía el `kind`; 4 avisos iguales pierden fuerza |
| `feature-matrix` | `ROWS` | 4 | 6 | 8 | Marca la columna ganadora con `class="best"` en su `<th>` y `<td>` |
| `diagram` | `STEPS` | 3 | 4 | 5 | `SPLIT` recomendado `1.3fr 1fr` |
| `roadmap` | `LANES` | 3 | 4 | 4 | 2-3 tarjetas por carril; `items` es HTML de `.rd-item` |
| `resources` | `RESOURCES` | 3 | 4 | 5 | `QR_DATA` debe ir URL-encoded |
| `chart-bars` | `BARS` | 3 | 5 | 7 | `COLS` = nº de barras. `tone`: vacío, `alt`, `mute`, `warn` |
| `chart-split` | `BARS` / `ROWS` | 3 / 3 | 4 / 4 | 6 / 6 | `SPLIT` recomendado `1.15fr 1fr` |
| `chart-grid` | `PANELS` | 2 | 4 | 4 | `COLS: "2"`. `series` con 3-6 puntos por panel |
| `gauges` | `GAUGES` | 2 | 4 | 4 | `value` de 0 a 100. `COLS` = nº de anillos |
| `trend` | `SERIES` / `MILESTONES` | 4 / 2 | 12 / 3 | 16 / 4 | `SPLIT` recomendado `1.25fr 1fr` |

Regla transversal: los campos `COLS` y `ROWS` **deben coincidir con la longitud real de la lista**. Si mandas 3 tarjetas y `COLS: "4"`, queda una columna vacía.

`COLS`, `ROWS` y `SPLIT` se interpolan **dentro de una regla CSS**. Si el plan no los aporta, la regla queda inválida (`repeat(,1fr)`) y la retícula colapsa sin que se vea un error en pantalla. Por eso `validate_packs.py --plan` los marca como `[ERROR]`, no como aviso.

---

## Reglas de cadencia (no negociables)

Estas reglas evitan el fallo más común: 20 slides de `concept-cards` seguidas.

1. **Nunca 4 slides seguidas del mismo arquetipo.** Máximo 3, y solo para `concept-cards`.
2. **Una `section` cada 4-5 slides de contenido.** Marca el cambio de bloque y da respiro visual.
3. **Tras 2-3 slides densas** (`table`, `matrix`, `code`, `concept-cards` de 4 columnas) **va una ligera** (`quote`, `section`, `metrics`).
4. **Al menos un `quiz`** por cada bloque temático, al cierre del bloque.
5. **Al menos un `metrics`** por deck si el material contiene cualquier cifra.
6. `cover` y `toc` solo una vez, al principio. `closing` solo una vez, al final.

### Esqueleto recomendado para una unidad de 25 slides

```
00  cover
01  toc
02  section          ← Bloque 1
03  principle
04  heatmap
05  metrics
06  activity
07  quiz
08  section          ← Bloque 2
09  concept-cards
10  code
11  dodont
12  quote            ← respiro
13  callouts
14  quiz
15  section          ← Bloque 3
16  diagram
17  anatomy
18  feature-matrix
19  timeline
20  quiz
21  section          ← Evaluación
22  table
23  resources
24  closing
```

---

## Buenas prácticas ya incorporadas en el frame

Estas van en `_frame.html`, así que **aplican automáticamente a los 30 arquetipos** sin que tengas que hacer nada:

| Práctica | Qué resuelve |
|---|---|
| `prefers-reduced-motion` | Desactiva animaciones para personas con sensibilidad vestibular |
| `:focus-visible` | Contorno de foco visible al navegar con teclado |
| `@media print` + `print-color-adjust` | El deck se exporta a PDF con los colores intactos |
| `<main role="region" aria-label>` | Cada slide se anuncia correctamente en lector de pantalla |
| `aria-hidden` en decoraciones | Glows, texturas y grano no ensucian la lectura asistida |
| `<meta name="color-scheme">` | Evita el flash de tema incorrecto al cargar |
| `.sr-only` | Clase disponible para texto solo-lector si un arquetipo lo necesita |
| `font-variant-numeric: tabular-nums` | Las cifras no bailan al cambiar de slide |

Además, a nivel de contenido:
- **Contraste**: las paletas de ambos packs superan 4.5:1 en texto de cuerpo sobre su fondo.
- **QR en `resources`**: se genera al vuelo, no hay que crear imágenes a mano.
- **`quiz` operable por teclado**: la tecla `R` revela sin depender del ratón.

---

## Cómo se escribe una slide en `visual_plan.json`

El agente aporta **únicamente texto**. Cero HTML, cero CSS.

```json
{
  "pack": "dark_tech",
  "title": "Unidad 3 — Automatización de Pruebas",
  "slides": [
    {
      "archetype": "metrics",
      "title": "El coste real de no automatizar",
      "notes": "Aquí va la explicación extensa para el profesor…",
      "slots": {
        "TAG_LEFT": "Sesión 01 · Datos",
        "TITLE": "El coste real de no automatizar",
        "TAG_RIGHT": "S1",
        "LEAD": "Tres cifras para justificar la inversión ante un comité.",
        "COLS": "3",
        "SOURCE": "Fuente: World Quality Report 2025",
        "METRICS": [
          { "label": "Reducción de regresión", "value": "87", "unit": "%",
            "desc": "Tiempo del ciclo completo tras automatizar.", "pct": "87%" },
          { "label": "Defectos en producción", "value": "3.2", "unit": "×",
            "desc": "Menos incidencias críticas que con testing manual.", "pct": "64%" }
        ]
      }
    }
  ]
}
```

Reglas del `slots`:
- Los slots en **MAYÚSCULAS** son valores simples (string).
- Los slots que en `_shared/archetypes.json` aparecen bajo `repeats` son **listas de objetos**; sus campos van en minúscula. Las listas van **dentro** de `slots`, no como hermanas suyas.
- Se permite HTML inline mínimo dentro de un string: `<br>`, `<b>`, `<em>` (renderiza serif itálica de acento en `dark_tech`).
- Si omites un slot de texto, queda vacío y el renderer emite un `[WARN]` — no rompe el build.
- **Excepción:** `COLS`, `ROWS` y `SPLIT` se interpolan dentro de una regla CSS. Si faltan, la regla queda inválida y la retícula colapsa sin aviso visible, por eso el validador los marca como `[ERROR]`.

### Consultar los slots exactos de un arquetipo

Están declarados en `theme-packs/_shared/archetypes.json`, campo `archetypes.<nombre>.slots` y `.repeats`. **Léelo antes de escribir el plan**; no adivines nombres de slot.

### Colores dentro del contenido

Algunos slots aceptan un `color` (`FACTORS[].color` y `EXAMPLES[].color` en `principle`; `ZONES[].color` y `ZONES[].bg` en `heatmap`; `LANES[].color` en `roadmap`). Ese valor se inserta **crudo dentro del CSS**, así que escribe la expresión completa, no el nombre del token:

```json
{ "name": "Complejidad", "text": "...", "color": "var(--a1)" }
```

Escribir `"color": "a1"` produce `background:a1`, que el navegador descarta en silencio: el elemento se queda sin color y nadie te avisa. Y si escribes `#22D3EE`, ese color sobrevivirá al cambio de tema y desentonará en los otros 27 packs.

---

## Escape hatch

Si un contenido no encaja en ningún arquetipo, la slide puede traer `html_content` con un documento HTML completo en vez de `archetype` + `slots`. Úsalo como **excepción**, no como norma: cada slide escrita a mano es una fuente de deriva visual. Si necesitas el mismo caso dos veces, conviértelo en un arquetipo nuevo del pack.
