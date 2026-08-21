# EVA Presentation Generator

Generador determinista de presentaciones web para EVA IPSS. A partir de un theme pack y una carpeta de material produce un deck HTML completo — visor, vista de presentador y notas de orador — sin que el modelo escriba una línea de HTML.

**28 packs · 30 arquetipos · 16 iconos animados · lienzo 1280×720**

---

## Ver los templates antes de elegir

El muestrario está en **`gallery/`**. Se genera, no se edita a mano.

| Abre esto | Para ver |
|---|---|
| **`gallery/index.html`** | Los 30 arquetipos con contenido real (las diagramaciones) y los 28 packs con las mismas 3 slides (la estética) |
| **`gallery/icons.html`** | Los 16 iconos Lordicon verificados, animados, con su ID copiable y alternancia claro/oscuro |

Clic en cualquier miniatura para abrirla a tamaño real. Los HTML sueltos están en `gallery/archetypes/` y `gallery/packs/<pack>/`.

```bash
# Regenerar tras tocar cualquier frame, arquetipo o _base.css
python3 scripts/make_gallery.py            # arquetipos en dark_tech
python3 scripts/make_gallery.py ink_jade   # o en el pack que quieras
```

> El muestrario pesa ~28 MB por las capturas de los packs. Es reproducible: puedes borrar `gallery/` y regenerarla cuando la necesites.

---

## Uso mínimo

> "Hazme la presentación de la Unidad 3 con el pack `dark_tech`. El material está en `cursos/.../UNIDAD 3/material`."

El flujo completo está en **[SKILL.md](SKILL.md)**. En resumen, tras escribir el plan:

```bash
python3 scripts/validate_packs.py --plan [ruta_unidad]/visual_plan.json
python3 scripts/generate_presentation_template.py --unit-path [ruta_unidad]
```

Y se abre `[ruta_unidad]/presentation/preview.html` (tecla `O` para el overview).

**Corrige todo `[ERROR]` antes de generar.** Los errores más frecuentes son slots que faltan y que el navegador no señala: `COLS`, `ROWS` y `SPLIT` se interpolan dentro de una regla CSS, así que si faltan la retícula colapsa sin aviso visible.

---

## Dónde está cada cosa

| Ruta | Qué es |
|---|---|
| **[SKILL.md](SKILL.md)** | El flujo completo por fases. Empieza aquí. |
| **[theme-packs/README.md](theme-packs/README.md)** | Catálogo de packs y arquetipos, matriz de decisión, densidad y cadencia. **La referencia central.** |
| [theme-packs/TOKENS.md](theme-packs/TOKENS.md) | Contrato de tokens. Solo si vas a crear un pack nuevo. |
| `theme-packs/_shared/archetypes.json` | Los slots exactos de cada arquetipo. Consúltalo antes de escribir el plan; no adivines nombres. |
| `theme-packs/_shared/icons.json` | Catálogo de iconos Lordicon verificados contra el CDN. |
| `references/principles/` | Carga cognitiva, jerarquía visual, modos de fallo. Apoyo para las fases 1-2. |
| `scripts/` | Motor, ensamblador, validador y generador del muestrario. |
| `gallery/` | El muestrario generado. |
| `_unused/` | Arquitecturas anteriores en cuarentena. **No leer ni ejecutar.** |

---

## Estado conocido

- **4 packs sin identidad propia**: `blue_white`, `champagne_gold`, `chrome_y2k` y `retro_70s` siguen con un preset genérico. `retro_70s` es casi un clon de `retro_warm`.
- **`minimal_gray` y `mocha_editorial` son parientes cercanos** — papel cálido con serif. Es fiel a sus referencias, no un fallo. `minimal_gray` para un tono más seco y periodístico; `mocha_editorial` para uno más cálido y de autor.
- **No hay QA de píxeles automatizado.** El que existía dependía de Pillow y de un layout que ya no se genera; está en cuarentena. La verificación es abrir `preview.html` y mirar.
