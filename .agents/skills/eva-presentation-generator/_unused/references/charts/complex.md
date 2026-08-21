# Gráficos complejos: 4 visualizaciones a nivel de ECharts

> Este documento contiene 4 tipos de **gráficos complejos de clase mundial**: coropletas de mapas mundiales, redes de relaciones, diagrama de Sankey y calendario térmico.运行时**——以保持 `html2svg → svg2pptx` 管线零偏移.
>
> La complejidad se logra a través de **geometría presupuestada a mano + rutas SVG + muchas etiquetas de posicionamiento absoluto HTML**. Cada imagen es una instantánea de datos única (estática) y no admite interacción/animación.
>
> **Convenciones recomendadas** (ya no hay restricciones de pipeline SVG — la exportación a PPTX es por captura de pantalla):
>
> - Evita `<text>` dentro de SVG cuando sea posible — las etiquetas superpuestas con HTML `<div>`/`<span>` renderizan de forma más consistente entre navegadores
> - Colorea con variables CSS (`--accent-1` / `--accent-2` / `--card-border` ...) del theme recipe de la unidad, no codificadas sueltas
> - Numérico en `font-variant-numeric: tabular-nums`
> - `conic-gradient` / `mask-image` / `mix-blend-mode` / `filter: blur()` están permitidos
> - Deshabilitar JavaScript / etiqueta `<script>`
>
> La plantilla HTML de cada imagen se puede pegar directamente en cualquier estilo (dark_tech / royal_red / minimal_gray...), y las variables CSS se adaptan automáticamente.

---

## Tabla de contenido

| # | Gráfico | gráfico_id | Cuándo utilizar |
|---|------|---------|-------|
| 15 | Coropletas del mapa mundial | `world_choropleth` | Visualización de datos globales (color por país) |
| 16 | Red de relaciones | `gráfico_de_red` | Nodo + conexión (estructura organizativa/gráfico de conocimiento) |
| 17 | Diagrama de Sankey | `sankey_flow` | Tráfico/Ruta de conversión/Asignación presupuestaria |
| 18 | Calendario de calor | `calendario_mapa de calor` | Densidad de datos de 365 días (contribución/historial de DAU) |

---

## 15. Coropletas del mapa mundial (`world_choropleth`)

**Cuándo utilizar**:



**Formato de datos**:

```json
{
  "metric": "月活跃用户 (MAU)",
  "unit": "万",
  "max": 4800,
  "regions": [
    {"id": "usa",       "name": "美国",   "value": 4800, "intensity": 1.00},
    {"id": "canada",    "name": "加拿大", "value":  720, "intensity": 0.18},
    {"id": "mexico",    "name": "墨西哥", "value":  410, "intensity": 0.12},
    {"id": "brazil",    "name": "巴西",   "value": 1850, "intensity": 0.42},
    {"id": "europe",    "name": "欧洲",   "value": 3200, "intensity": 0.72},
    {"id": "russia",    "name": "俄罗斯", "value":  280, "intensity": 0.10},
    {"id": "china",     "name": "中国",   "value": 4200, "intensity": 0.92},
    {"id": "india",     "name": "印度",   "value": 2400, "intensity": 0.55},
    {"id": "japan",     "name": "日本",   "value":  980, "intensity": 0.24},
    {"id": "sea",       "name": "东南亚", "value":  870, "intensity": 0.22},
    {"id": "australia", "name": "澳洲",   "value":  340, "intensity": 0.10},
    {"id": "africa",    "name": "非洲",   "value":  520, "intensity": 0.14}
  ]
}
```

`intensity` ∈ [0, 1] es la intensidad visual ajustada manualmente después de `value/max` (el mapeo lineal hará que todos los países pequeños estén "atenuados", y `Math.pow(value/max, 0.6)` se usa a menudo para iluminar la sección central).

**Plantilla HTML** (completa y ejecutable):

```html
<div class="chart-world-choropleth" style="position:relative; width:100%; aspect-ratio: 16/9; padding: 24px 28px 56px;">

  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom: 8px;">
    <div>
      <div style="font-size:11px; letter-spacing:0.18em; text-transform:uppercase; color:var(--accent-1); font-weight:600;">— GLOBAL DISTRIBUTION</div>
      <div style="font-size:20px; font-weight:600; letter-spacing:-0.01em; color:var(--text-primary); margin-top:6px;">月活跃用户 (MAU)</div>
    </div>
    <div style="text-align:right;">
      <div style="font-size:32px; font-weight:700; letter-spacing:-0.02em; color:var(--text-primary); font-variant-numeric: tabular-nums;">2.46<span style="font-size:14px; color:var(--text-secondary); font-weight:500; margin-left:4px;">亿 / 月</span></div>
      <div style="font-size:11px; color:var(--text-secondary); letter-spacing:0.05em; margin-top:2px;">合计 12 个区域 · 2026Q1</div>
    </div>
  </div>

  <div style="position:relative; width:100%; height:78%;">
    <svg viewBox="0 0 1000 500" preserveAspectRatio="xMidYMid meet" style="width:100%; height:100%; display:block;">
      <defs>
        <pattern id="wm-grid" x="0" y="0" width="50" height="50" patternUnits="userSpaceOnUse">
          <path d="M 50 0 L 0 0 0 50" fill="none" stroke="var(--card-border)" stroke-width="0.4" opacity="0.18"/>
        </pattern>
      </defs>
      <rect x="0" y="0" width="1000" height="500" fill="url(#wm-grid)"/>

      <path d="M 60 110 L 120 92 L 200 96 L 260 108 L 280 142 L 240 178 L 180 196 L 130 184 L 95 168 L 70 144 Z"
            fill="var(--accent-1)" fill-opacity="1.00" stroke="var(--card-border)" stroke-width="0.8"/>
      <path d="M 70 60 L 180 48 L 290 52 L 320 78 L 280 104 L 200 92 L 130 88 L 80 92 L 60 78 Z"
            fill="var(--accent-1)" fill-opacity="0.18" stroke="var(--card-border)" stroke-width="0.8"/>
      <path d="M 130 200 L 200 196 L 250 218 L 232 252 L 178 268 L 138 248 L 122 220 Z"
            fill="var(--accent-1)" fill-opacity="0.12" stroke="var(--card-border)" stroke-width="0.8"/>

      <path d="M 270 280 L 320 268 L 360 290 L 380 340 L 372 396 L 332 420 L 290 412 L 268 372 L 254 326 Z"
            fill="var(--accent-1)" fill-opacity="0.42" stroke="var(--card-border)" stroke-width="0.8"/>

      <path d="M 460 100 L 510 88 L 560 96 L 588 116 L 580 142 L 530 152 L 480 144 L 452 126 Z"
            fill="var(--accent-1)" fill-opacity="0.72" stroke="var(--card-border)" stroke-width="0.8"/>

      <path d="M 580 70 L 720 60 L 850 70 L 920 92 L 880 122 L 760 118 L 660 110 L 590 96 Z"
            fill="var(--accent-1)" fill-opacity="0.10" stroke="var(--card-border)" stroke-width="0.8"/>

      <path d="M 720 152 L 800 142 L 858 168 L 870 210 L 832 244 L 776 240 L 728 218 L 712 184 Z"
            fill="var(--accent-1)" fill-opacity="0.92" stroke="var(--card-border)" stroke-width="0.8"/>

      <path d="M 660 230 L 720 224 L 752 252 L 740 296 L 692 308 L 660 282 L 650 252 Z"
            fill="var(--accent-1)" fill-opacity="0.55" stroke="var(--card-border)" stroke-width="0.8"/>

      <path d="M 870 178 L 906 172 L 920 198 L 906 220 L 878 218 L 866 198 Z"
            fill="var(--accent-1)" fill-opacity="0.24" stroke="var(--card-border)" stroke-width="0.8"/>

      <path d="M 780 270 L 832 264 L 858 290 L 842 320 L 800 322 L 776 298 Z"
            fill="var(--accent-1)" fill-opacity="0.22" stroke="var(--card-border)" stroke-width="0.8"/>

      <path d="M 838 360 L 900 350 L 932 374 L 916 408 L 868 416 L 838 392 Z"
            fill="var(--accent-1)" fill-opacity="0.10" stroke="var(--card-border)" stroke-width="0.8"/>

      <path d="M 480 200 L 540 192 L 590 208 L 612 252 L 600 320 L 562 372 L 520 388 L 478 364 L 458 312 L 462 252 Z"
            fill="var(--accent-1)" fill-opacity="0.14" stroke="var(--card-border)" stroke-width="0.8"/>
    </svg>

    <div style="position:absolute; left:14.5%; top:30%; transform:translate(-50%,-50%); text-align:center; pointer-events:none;">
      <div style="font-size:11px; font-weight:700; color:var(--text-primary); letter-spacing:0.04em; text-shadow:0 1px 2px rgba(0,0,0,0.4);">USA</div>
      <div style="font-size:13px; font-weight:700; color:var(--accent-1); font-variant-numeric: tabular-nums; letter-spacing:-0.01em; margin-top:1px;">4 800</div>
    </div>
    <div style="position:absolute; left:17%; top:14%; transform:translate(-50%,-50%); text-align:center;">
      <div style="font-size:10px; color:var(--text-secondary); letter-spacing:0.04em;">Canada</div>
      <div style="font-size:11px; font-weight:600; color:var(--text-primary); font-variant-numeric: tabular-nums;">720</div>
    </div>
    <div style="position:absolute; left:18.5%; top:46%; transform:translate(-50%,-50%); text-align:center;">
      <div style="font-size:10px; color:var(--text-secondary);">Mexico</div>
      <div style="font-size:11px; font-weight:600; color:var(--text-primary); font-variant-numeric: tabular-nums;">410</div>
    </div>

    <div style="position:absolute; left:32.5%; top:69%; transform:translate(-50%,-50%); text-align:center;">
      <div style="font-size:11px; font-weight:700; color:var(--text-primary); letter-spacing:0.04em;">Brazil</div>
      <div style="font-size:12px; font-weight:700; color:var(--accent-1); font-variant-numeric: tabular-nums;">1 850</div>
    </div>

    <div style="position:absolute; left:52%; top:24%; transform:translate(-50%,-50%); text-align:center;">
      <div style="font-size:11px; font-weight:700; color:var(--text-primary); letter-spacing:0.04em;">Europe</div>
      <div style="font-size:13px; font-weight:700; color:var(--accent-1); font-variant-numeric: tabular-nums;">3 200</div>
    </div>

    <div style="position:absolute; left:74%; top:18%; transform:translate(-50%,-50%); text-align:center;">
      <div style="font-size:10px; color:var(--text-secondary);">Russia</div>
      <div style="font-size:11px; font-weight:600; color:var(--text-primary); font-variant-numeric: tabular-nums;">280</div>
    </div>

    <div style="position:absolute; left:79%; top:39%; transform:translate(-50%,-50%); text-align:center;">
      <div style="font-size:11px; font-weight:700; color:var(--text-primary); letter-spacing:0.04em;">China</div>
      <div style="font-size:13px; font-weight:700; color:var(--accent-1); font-variant-numeric: tabular-nums;">4 200</div>
    </div>

    <div style="position:absolute; left:70.5%; top:54%; transform:translate(-50%,-50%); text-align:center;">
      <div style="font-size:11px; font-weight:700; color:var(--text-primary);">India</div>
      <div style="font-size:12px; font-weight:700; color:var(--accent-1); font-variant-numeric: tabular-nums;">2 400</div>
    </div>

    <div style="position:absolute; left:89%; top:39%; transform:translate(-50%,-50%); text-align:center;">
      <div style="font-size:10px; color:var(--text-secondary);">Japan</div>
      <div style="font-size:11px; font-weight:600; color:var(--text-primary); font-variant-numeric: tabular-nums;">980</div>
    </div>

    <div style="position:absolute; left:81%; top:59%; transform:translate(-50%,-50%); text-align:center;">
      <div style="font-size:10px; color:var(--text-secondary);">SEA</div>
      <div style="font-size:11px; font-weight:600; color:var(--text-primary); font-variant-numeric: tabular-nums;">870</div>
    </div>

    <div style="position:absolute; left:88.5%; top:78%; transform:translate(-50%,-50%); text-align:center;">
      <div style="font-size:10px; color:var(--text-secondary);">Australia</div>
      <div style="font-size:11px; font-weight:600; color:var(--text-primary); font-variant-numeric: tabular-nums;">340</div>
    </div>

    <div style="position:absolute; left:53%; top:58%; transform:translate(-50%,-50%); text-align:center;">
      <div style="font-size:10px; color:var(--text-secondary);">Africa</div>
      <div style="font-size:11px; font-weight:600; color:var(--text-primary); font-variant-numeric: tabular-nums;">520</div>
    </div>
  </div>

  <div style="position:absolute; left:28px; bottom:14px; right:28px; display:flex; align-items:center; gap:14px;">
    <span style="font-size:10px; letter-spacing:0.12em; color:var(--text-secondary); text-transform:uppercase;">Less</span>
    <div style="display:flex; flex:1; height:8px; border-radius:2px; overflow:hidden;">
      <div style="flex:1; background:var(--accent-1); opacity:0.10;"></div>
      <div style="flex:1; background:var(--accent-1); opacity:0.28;"></div>
      <div style="flex:1; background:var(--accent-1); opacity:0.50;"></div>
      <div style="flex:1; background:var(--accent-1); opacity:0.75;"></div>
      <div style="flex:1; background:var(--accent-1); opacity:1.00;"></div>
    </div>
    <span style="font-size:10px; letter-spacing:0.12em; color:var(--text-secondary); text-transform:uppercase;">More</span>
    <span style="font-size:10px; color:var(--text-secondary); font-variant-numeric:tabular-nums; margin-left:8px;">0 — 4 800 万</span>
  </div>

</div>
```

**Puntos de implementación**:

- **Los datos de ruta son polígonos simplificados a mano** (6-12 puntos por área), no por precisión geográfica sino por reconocibilidad visual. Si necesita GeoJSON real, se recomienda utilizar Natural Earth Low Res + `topojson-simplify` para generar la ruta sin conexión y luego insertarla. El viewBox de esta plantilla es `1000 × 500` (estilo equirectangular), lo que facilita el mapeo lineal de longitud y latitud.
- **`fill-opacity` es el valor de los datos** - escribe `intensidad ∈ [0, 1]` directamente en el atributo `fill-opacity`. Todas las rutas usan el mismo `fill="var(--accent-1)"` y el color cambia automáticamente con el estilo.
- **La etiqueta es HTML en posición absoluta** (coordenadas porcentuales), no dentro del SVG. Los países importantes (intensidad ≥ 0,4) muestran números; Los países menores solo muestran nombres + números. China / Estados Unidos / Brasil / India / Europa 5 etiquetas principales **Amplía el tamaño de fuente y usa colores de acento**; el resto se retira a la secundaria para evitar la sobrecarga visual.
- **La parte inferior de la cuadrícula** usa `<pattern id="wm-grid">` para las líneas de longitud y latitud, 50×50 unidades, trazo 0,4/opacidad 0,18, para darle al mapa una "sensación geográfica", de lo contrario, los bloques de color se verán como un mosaico.
- **Los 5 segmentos de la leyenda** corresponden a `[0,10, 0,28, 0,50, 0,75, 1,00]`: no están divididos uniformemente, sino perceptivamente calibrados (el ojo humano no es sensible a diferencias de opacidad < 0,3, por lo que los segmentos bajos son densos y los segmentos altos son escasos).

**Autocomprobación**:

- [] Existe una correspondencia uno a uno entre la "opacidad de relleno" de 12 rutas y la "intensidad" de los datos.
- [ ] Todas las etiquetas son HTML `<div>`, **Ceros internos SVG `<text>`**
- [] numérico en `font-variant-numeric: tabular-nums`
- Las etiquetas `left`/`top` de [] son porcentajes (sensible), no px
- [] Leyenda 5 segmentos + Menos/Más + rangos numéricos están todos completos
- [] país héroe (el 4-5 con el valor más grande), el tamaño de fuente es un paso más grande y el color es `--accent-1`

**Futuras expansiones (v2)**:

- Contornos de países reales: use `scripts/world_map_paths.py` para generar rutas por lotes desde Natural Earth GeoJSON después de la simplificación (`topojson-simplify -s 0.5`), reemplazando las 12 formas simplificadas en línea
- Mapeo de dos colores (como "crecimiento versus declive" dividido con `--accent-1`/`--accent-3`)
- Superposición de burbujas: superponga puntos por ciudad en la coropleta (usando SVG `<circle>` + etiqueta de número HTML)

---

## 16. Red de relaciones (`network_graph`)

**Cuándo utilizar**:

- Organigrama (CEO → C-suite → Equipo)
- Relación gráfico de conocimiento/concepto (5-12 nodos son los mejores)
- Red de relación de cartera (Fondo → Empresa participada → Canal de salida)
- Linaje de datos (fuente → ETL → mart → BI)

**No utilice esta plantilla cuando el número de nodos > 12**: el límite del análisis de conexiones por ojo humano es 12 nodos/18 aristas. Utilice en su lugar un diagrama de Sankey o un árbol jerárquico.

**Formato de datos**:

```json
{
  "title": "组织架构 · 2026Q2",
  "nodes": [
    {"id": "ceo",  "label": "CEO",         "x": 50, "y": 16, "size": "lg", "tier": 1},
    {"id": "cto",  "label": "CTO",         "x": 22, "y": 42, "size": "md", "tier": 2},
    {"id": "cfo",  "label": "CFO",         "x": 50, "y": 42, "size": "md", "tier": 2},
    {"id": "cmo",  "label": "CMO",         "x": 78, "y": 42, "size": "md", "tier": 2},
    {"id": "eng1", "label": "Platform",    "x": 10, "y": 74, "size": "sm", "tier": 3},
    {"id": "eng2", "label": "AI / ML",     "x": 28, "y": 80, "size": "sm", "tier": 3},
    {"id": "fin",  "label": "FP & A",      "x": 46, "y": 76, "size": "sm", "tier": 3},
    {"id": "ops",  "label": "Ops",         "x": 60, "y": 80, "size": "sm", "tier": 3},
    {"id": "grw",  "label": "Growth",      "x": 74, "y": 76, "size": "sm", "tier": 3},
    {"id": "br",   "label": "Brand",       "x": 90, "y": 80, "size": "sm", "tier": 3}
  ],
  "edges": [
    {"from": "ceo", "to": "cto"}, {"from": "ceo", "to": "cfo"}, {"from": "ceo", "to": "cmo"},
    {"from": "cto", "to": "eng1"}, {"from": "cto", "to": "eng2"},
    {"from": "cfo", "to": "fin"}, {"from": "cfo", "to": "ops"},
    {"from": "cmo", "to": "grw"}, {"from": "cmo", "to": "br"}
  ]
}
```

`x`/`y` son coordenadas de 0 a 100 por ciento, **presupuesto manual** (simulando un diseño estable después de una convergencia dirigida por la fuerza); considérelo como una "captura de pantalla estática", sin JS ejecutando simulación física.

**Plantilla HTML** (completa y ejecutable):

```html
<div class="chart-network" style="position:relative; width:100%; aspect-ratio: 16/9; padding: 28px 32px; overflow:hidden;">

  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom: 12px;">
    <div>
      <div style="font-size:11px; letter-spacing:0.18em; text-transform:uppercase; color:var(--accent-1); font-weight:600;">— ORG STRUCTURE</div>
      <div style="font-size:20px; font-weight:600; letter-spacing:-0.01em; color:var(--text-primary); margin-top:6px;">组织架构图 · 10 个核心节点</div>
    </div>
    <div style="display:flex; gap:14px; align-items:center; font-size:11px; color:var(--text-secondary); letter-spacing:0.04em;">
      <span style="display:inline-flex; align-items:center; gap:6px;"><span style="width:14px;height:14px;border-radius:50%;background:var(--accent-1);box-shadow:0 0 8px var(--accent-1);"></span>Tier 1</span>
      <span style="display:inline-flex; align-items:center; gap:6px;"><span style="width:11px;height:11px;border-radius:50%;background:var(--accent-2);"></span>Tier 2</span>
      <span style="display:inline-flex; align-items:center; gap:6px;"><span style="width:8px;height:8px;border-radius:50%;background:var(--text-secondary); opacity:0.6;"></span>Tier 3</span>
    </div>
  </div>

  <div style="position:relative; width:100%; height:88%;">

    <svg viewBox="0 0 1000 500" preserveAspectRatio="none" style="position:absolute; inset:0; width:100%; height:100%;">
      <line x1="500" y1="80"  x2="220" y2="210" stroke="var(--accent-1)" stroke-width="1.6" stroke-opacity="0.55"/>
      <line x1="500" y1="80"  x2="500" y2="210" stroke="var(--accent-1)" stroke-width="1.6" stroke-opacity="0.55"/>
      <line x1="500" y1="80"  x2="780" y2="210" stroke="var(--accent-1)" stroke-width="1.6" stroke-opacity="0.55"/>

      <line x1="220" y1="210" x2="100" y2="370" stroke="var(--accent-2)" stroke-width="1.2" stroke-opacity="0.40"/>
      <line x1="220" y1="210" x2="280" y2="400" stroke="var(--accent-2)" stroke-width="1.2" stroke-opacity="0.40"/>

      <line x1="500" y1="210" x2="460" y2="380" stroke="var(--accent-2)" stroke-width="1.2" stroke-opacity="0.40"/>
      <line x1="500" y1="210" x2="600" y2="400" stroke="var(--accent-2)" stroke-width="1.2" stroke-opacity="0.40"/>

      <line x1="780" y1="210" x2="740" y2="380" stroke="var(--accent-2)" stroke-width="1.2" stroke-opacity="0.40"/>
      <line x1="780" y1="210" x2="900" y2="400" stroke="var(--accent-2)" stroke-width="1.2" stroke-opacity="0.40"/>

      <circle cx="500" cy="80"  r="34" fill="var(--accent-1)" fill-opacity="0.10" stroke="var(--accent-1)" stroke-width="0.6" stroke-opacity="0.4"/>
      <circle cx="220" cy="210" r="26" fill="var(--accent-2)" fill-opacity="0.08" stroke="var(--accent-2)" stroke-width="0.5" stroke-opacity="0.4"/>
      <circle cx="500" cy="210" r="26" fill="var(--accent-2)" fill-opacity="0.08" stroke="var(--accent-2)" stroke-width="0.5" stroke-opacity="0.4"/>
      <circle cx="780" cy="210" r="26" fill="var(--accent-2)" fill-opacity="0.08" stroke="var(--accent-2)" stroke-width="0.5" stroke-opacity="0.4"/>
    </svg>

    <div style="position:absolute; left:50%; top:16%; transform:translate(-50%,-50%); width:64px; height:64px; border-radius:50%; background:linear-gradient(135deg, var(--accent-1), var(--accent-2)); display:flex; align-items:center; justify-content:center; box-shadow: 0 6px 24px rgba(0,0,0,0.18), 0 0 0 4px var(--card-bg-from);">
      <div style="text-align:center;">
        <div style="font-size:12px; font-weight:700; color:#fff; letter-spacing:0.05em;">CEO</div>
        <div style="font-size:9px; color:rgba(255,255,255,0.85); letter-spacing:0.08em; margin-top:1px;">Tier 1</div>
      </div>
    </div>

    <div style="position:absolute; left:22%; top:42%; transform:translate(-50%,-50%); width:48px; height:48px; border-radius:50%; background:var(--card-bg-from); border:1.5px solid var(--accent-2); display:flex; align-items:center; justify-content:center;">
      <span style="font-size:11px; font-weight:700; color:var(--text-primary); letter-spacing:0.04em;">CTO</span>
    </div>
    <div style="position:absolute; left:50%; top:42%; transform:translate(-50%,-50%); width:48px; height:48px; border-radius:50%; background:var(--card-bg-from); border:1.5px solid var(--accent-2); display:flex; align-items:center; justify-content:center;">
      <span style="font-size:11px; font-weight:700; color:var(--text-primary); letter-spacing:0.04em;">CFO</span>
    </div>
    <div style="position:absolute; left:78%; top:42%; transform:translate(-50%,-50%); width:48px; height:48px; border-radius:50%; background:var(--card-bg-from); border:1.5px solid var(--accent-2); display:flex; align-items:center; justify-content:center;">
      <span style="font-size:11px; font-weight:700; color:var(--text-primary); letter-spacing:0.04em;">CMO</span>
    </div>

    <div style="position:absolute; left:10%; top:74%; transform:translate(-50%,-50%); display:flex; flex-direction:column; align-items:center; gap:4px;">
      <div style="width:32px; height:32px; border-radius:50%; background:var(--card-bg-to); border:1px solid var(--card-border);"></div>
      <span style="font-size:10px; color:var(--text-secondary); letter-spacing:0.04em;">Platform</span>
    </div>
    <div style="position:absolute; left:28%; top:80%; transform:translate(-50%,-50%); display:flex; flex-direction:column; align-items:center; gap:4px;">
      <div style="width:32px; height:32px; border-radius:50%; background:var(--card-bg-to); border:1px solid var(--card-border);"></div>
      <span style="font-size:10px; color:var(--text-secondary);">AI / ML</span>
    </div>
    <div style="position:absolute; left:46%; top:76%; transform:translate(-50%,-50%); display:flex; flex-direction:column; align-items:center; gap:4px;">
      <div style="width:32px; height:32px; border-radius:50%; background:var(--card-bg-to); border:1px solid var(--card-border);"></div>
      <span style="font-size:10px; color:var(--text-secondary);">FP &amp; A</span>
    </div>
    <div style="position:absolute; left:60%; top:80%; transform:translate(-50%,-50%); display:flex; flex-direction:column; align-items:center; gap:4px;">
      <div style="width:32px; height:32px; border-radius:50%; background:var(--card-bg-to); border:1px solid var(--card-border);"></div>
      <span style="font-size:10px; color:var(--text-secondary);">Ops</span>
    </div>
    <div style="position:absolute; left:74%; top:76%; transform:translate(-50%,-50%); display:flex; flex-direction:column; align-items:center; gap:4px;">
      <div style="width:32px; height:32px; border-radius:50%; background:var(--card-bg-to); border:1px solid var(--card-border);"></div>
      <span style="font-size:10px; color:var(--text-secondary);">Growth</span>
    </div>
    <div style="position:absolute; left:90%; top:80%; transform:translate(-50%,-50%); display:flex; flex-direction:column; align-items:center; gap:4px;">
      <div style="width:32px; height:32px; border-radius:50%; background:var(--card-bg-to); border:1px solid var(--card-border);"></div>
      <span style="font-size:10px; color:var(--text-secondary);">Brand</span>
    </div>

  </div>
</div>
```

**Puntos de implementación**:

- **Las posiciones de los nodos se presupuestan manualmente** - Esta plantilla no tiene JS ejecutando d3-force. Piense en los nodos como "capturas de pantalla convergentes" con x/y codificados directamente en HTML. Reglas: el nivel 1 está centrado y en la parte superior, el nivel 2 está dividido uniformemente horizontalmente en el medio y el nivel 3 está disperso en la parte inferior. Deje al menos un 8 % de espacio horizontal entre cada nodo; de lo contrario, quedará visualmente abarrotado.
- **La conexión es SVG `<línea>`** (no `<ruta>`), porque bezier no es necesario para líneas rectas. El sistema de coordenadas usa un viewBox fijo `1000 × 500`, y el punto central del nodo debe convertirse a la unidad viewBox (HTML usa 50% / SVG usa 500), por lo que SVG usa `preserveAspectRatio="none"` para hacer que las coordenadas se estiren linealmente: los nodos HTML (posicionamiento porcentual) y las conexiones SVG (coordenadas absolutas) se pueden alinear con precisión.
- **Capas visuales de nodos**:
  - Nivel 1 (CEO): círculo degradado de 64 px + anillo exterior de halo de 4 px (use `box-shadow: 0 0 0 4 px`, **sin filtro: desenfoque**)
  - Nivel 2 (C-suite): círculo de borde de 48 px + texto
  - Nivel 3 (Equipo): círculo translúcido de 32 px + etiqueta de texto debajo (para evitar que el texto quede comprimido en el círculo pequeño)
- **La conexión se divide en dos capas**: tier1→tier2 usa `--accent-1` de 1,6 px de grosor, tier2→tier3 usa `--accent-2` de 1,2 px de grosor y reduce la opacidad: lo visual forma naturalmente una jerarquía de "tronco grueso y ramas delgadas".
- **Sin marcas de flecha** (`<marcador>`) - svg2pptx tiene un soporte deficiente para marcadores. Basta que la estructura organizacional implique la dirección del flujo en función de la relación posicional.

**Autocomprobación**:



**Futuras expansiones (v2)**:

- Cuando el número de nodos es > 8, se recomienda utilizar `networkx.spring_layout()` **fuera de línea** de Python para calcular la fuerza dirigida y luego volcar las coordenadas convergentes a JSON o plantilla para su lectura.
- Se agregó "peso del borde" - `<ancho de trazo de línea>` es proporcional al peso del borde
- Utilice SVG `<ruta>` para que los bordes bidireccionales sean ligeramente curvados (los puntos de control están desplazados entre 8 y 12 unidades) para evitar la superposición visual de las flechas bidireccionales.

---

## 17. Diagrama de Sankey (`sankey_flow`)

**Cuándo utilizar**:

- Embudo de conversión de SaaS (Marketing → Prueba → Pagado → Renovado), debe observar el **flujo de múltiples sucursales** de cada paso en lugar de un único embudo
- Asignación presupuestaria (Presupuesto Total → Departamento → Proyecto)
- Fuente del usuario → página de destino → ruta de comportamiento
- Dirección del flujo de energía y composición del flujo.

El diagrama de embudo sólo puede expresar un estrechamiento lineal único; el diagrama de Sankey puede expresar **múltiples entradas, múltiples salidas** y el ancho de cada flujo se asigna con precisión según el valor numérico.

**Formato de datos**:

```json
{
  "title": "SaaS 转化路径 · 2026Q1",
  "unit": "用户数",
  "columns": [
    {"id": "src", "label": "Source", "nodes": [
      {"id": "paid",   "label": "付费广告",  "value": 12000},
      {"id": "organic","label": "自然搜索",  "value":  8000},
      {"id": "referral","label":"推荐",     "value":  4000}
    ]},
    {"id": "trial", "label": "Trial", "nodes": [
      {"id": "trial7",  "label": "7-day Trial",  "value": 14000},
      {"id": "demo",    "label": "Demo Booked",  "value":  6000},
      {"id": "drop1",   "label": "未激活",       "value":  4000}
    ]},
    {"id": "paid_stage", "label": "Paid", "nodes": [
      {"id": "starter", "label": "Starter $29",  "value":  6800},
      {"id": "pro",     "label": "Pro $99",      "value":  3200},
      {"id": "drop2",   "label": "Trial 流失",   "value": 10000}
    ]},
    {"id": "outcome", "label": "12-mo Outcome", "nodes": [
      {"id": "renew",   "label": "续约",         "value":  7600},
      {"id": "churn",   "label": "流失",         "value":  2400}
    ]}
  ],
  "flows": [
    {"from":"paid",     "to":"trial7",  "value": 8000},
    {"from":"paid",     "to":"demo",    "value": 3000},
    {"from":"paid",     "to":"drop1",   "value": 1000},
    {"from":"organic",  "to":"trial7",  "value": 4500},
    {"from":"organic",  "to":"demo",    "value": 2500},
    {"from":"organic",  "to":"drop1",   "value": 1000},
    {"from":"referral", "to":"trial7",  "value": 1500},
    {"from":"referral", "to":"demo",    "value":  500},
    {"from":"referral", "to":"drop1",   "value": 2000},

    {"from":"trial7",   "to":"starter", "value": 4800},
    {"from":"trial7",   "to":"pro",     "value": 2200},
    {"from":"trial7",   "to":"drop2",   "value": 7000},
    {"from":"demo",     "to":"starter", "value": 2000},
    {"from":"demo",     "to":"pro",     "value": 1000},
    {"from":"demo",     "to":"drop2",   "value": 3000},

    {"from":"starter",  "to":"renew",   "value": 5000},
    {"from":"starter",  "to":"churn",   "value": 1800},
    {"from":"pro",      "to":"renew",   "value": 2600},
    {"from":"pro",      "to":"churn",   "value":  600}
  ]
}
```

**Plantilla HTML** (Completamente ejecutable · Versión simplificada de 4 columnas):

```html
<div class="chart-sankey" style="position:relative; width:100%; aspect-ratio: 16/9; padding: 28px 36px;">

  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom: 14px;">
    <div>
      <div style="font-size:11px; letter-spacing:0.18em; text-transform:uppercase; color:var(--accent-1); font-weight:600;">— CONVERSION FLOW</div>
      <div style="font-size:20px; font-weight:600; letter-spacing:-0.01em; color:var(--text-primary); margin-top:6px;">SaaS 用户转化路径 · Q1 2026</div>
    </div>
    <div style="text-align:right;">
      <div style="font-size:28px; font-weight:700; letter-spacing:-0.02em; color:var(--text-primary); font-variant-numeric: tabular-nums;">24 000<span style="font-size:13px; color:var(--text-secondary); font-weight:500; margin-left:6px;">访客 → 7 600 续约</span></div>
      <div style="font-size:11px; color:var(--text-secondary); letter-spacing:0.05em; margin-top:2px;">总转化率 31.7%</div>
    </div>
  </div>

  <div style="position:relative; width:100%; height:80%;">

    <div style="position:absolute; top:-18px; left:0; right:0; display:grid; grid-template-columns: repeat(4, 1fr); font-size:10px; letter-spacing:0.15em; color:var(--text-secondary); text-transform:uppercase; font-weight:600;">
      <div style="text-align:left; padding-left:4px;">— Source</div>
      <div style="text-align:center;">— Trial</div>
      <div style="text-align:center;">— Paid</div>
      <div style="text-align:right; padding-right:4px;">12-mo Outcome —</div>
    </div>

    <svg viewBox="0 0 1000 500" preserveAspectRatio="none" style="position:absolute; inset:0; width:100%; height:100%;">

      <path d="M 80,40 C 280,40 100,150 320,150" stroke="var(--accent-1)" stroke-width="62" stroke-opacity="0.42" fill="none" stroke-linecap="butt"/>
      <path d="M 80,135 C 280,135 100,255 320,255" stroke="var(--accent-1)" stroke-width="22" stroke-opacity="0.42" fill="none"/>
      <path d="M 80,180 C 280,180 100,360 320,360" stroke="var(--accent-2)" stroke-width="8" stroke-opacity="0.30" fill="none"/>

      <path d="M 80,260 C 280,260 100,170 320,170" stroke="var(--accent-1)" stroke-width="35" stroke-opacity="0.42" fill="none"/>
      <path d="M 80,315 C 280,315 100,275 320,275" stroke="var(--accent-1)" stroke-width="20" stroke-opacity="0.42" fill="none"/>
      <path d="M 80,355 C 280,355 100,365 320,365" stroke="var(--accent-2)" stroke-width="8" stroke-opacity="0.30" fill="none"/>

      <path d="M 80,420 C 280,420 100,200 320,200" stroke="var(--accent-1)" stroke-width="12" stroke-opacity="0.42" fill="none"/>
      <path d="M 80,438 C 280,438 100,290 320,290" stroke="var(--accent-1)" stroke-width="4" stroke-opacity="0.42" fill="none"/>
      <path d="M 80,455 C 280,455 100,375 320,375" stroke="var(--accent-2)" stroke-width="16" stroke-opacity="0.30" fill="none"/>

      <path d="M 360,135 C 540,135 380,80  600,80"  stroke="var(--accent-1)" stroke-width="36" stroke-opacity="0.42" fill="none"/>
      <path d="M 360,170 C 540,170 380,180 600,180" stroke="var(--accent-1)" stroke-width="18" stroke-opacity="0.42" fill="none"/>
      <path d="M 360,225 C 540,225 380,335 600,335" stroke="var(--accent-3)" stroke-width="56" stroke-opacity="0.28" fill="none"/>

      <path d="M 360,275 C 540,275 380,128 600,128" stroke="var(--accent-1)" stroke-width="16" stroke-opacity="0.42" fill="none"/>
      <path d="M 360,300 C 540,300 380,210 600,210" stroke="var(--accent-1)" stroke-width="9"  stroke-opacity="0.42" fill="none"/>
      <path d="M 360,330 C 540,330 380,395 600,395" stroke="var(--accent-3)" stroke-width="24" stroke-opacity="0.28" fill="none"/>

      <path d="M 640,80  C 820,80  660,90  880,90"  stroke="var(--accent-1)" stroke-width="40" stroke-opacity="0.45" fill="none"/>
      <path d="M 640,135 C 820,135 660,200 880,200" stroke="var(--accent-3)" stroke-width="16" stroke-opacity="0.32" fill="none"/>
      <path d="M 640,180 C 820,180 660,135 880,135" stroke="var(--accent-1)" stroke-width="22" stroke-opacity="0.45" fill="none"/>
      <path d="M 640,210 C 820,210 660,225 880,225" stroke="var(--accent-3)" stroke-width="6"  stroke-opacity="0.32" fill="none"/>

      <rect x="68" y="14"  width="14" height="56" rx="2" fill="var(--accent-1)" fill-opacity="0.85"/>
      <rect x="68" y="120" width="14" height="42" rx="2" fill="var(--accent-1)" fill-opacity="0.7"/>
      <rect x="68" y="172" width="14" height="22" rx="2" fill="var(--accent-1)" fill-opacity="0.6"/>

      <rect x="318" y="100" width="14" height="100" rx="2" fill="var(--accent-1)" fill-opacity="0.85"/>
      <rect x="318" y="220" width="14" height="48"  rx="2" fill="var(--accent-1)" fill-opacity="0.7"/>
      <rect x="318" y="320" width="14" height="80"  rx="2" fill="var(--accent-3)" fill-opacity="0.55"/>

      <rect x="598" y="40"  width="14" height="80"  rx="2" fill="var(--accent-1)" fill-opacity="0.85"/>
      <rect x="598" y="150" width="14" height="46"  rx="2" fill="var(--accent-1)" fill-opacity="0.7"/>
      <rect x="598" y="280" width="14" height="120" rx="2" fill="var(--accent-3)" fill-opacity="0.55"/>

      <rect x="878" y="50"  width="14" height="100" rx="2" fill="var(--accent-1)" fill-opacity="0.85"/>
      <rect x="878" y="180" width="14" height="68"  rx="2" fill="var(--accent-3)" fill-opacity="0.55"/>
    </svg>

    <div style="position:absolute; left:0; top:6%; font-size:11px;"><div style="font-weight:600; color:var(--text-primary);">付费广告</div><div style="font-size:10px; color:var(--text-secondary); font-variant-numeric:tabular-nums;">12 000</div></div>
    <div style="position:absolute; left:0; top:26%; font-size:11px;"><div style="font-weight:600; color:var(--text-primary);">自然搜索</div><div style="font-size:10px; color:var(--text-secondary); font-variant-numeric:tabular-nums;">8 000</div></div>
    <div style="position:absolute; left:0; top:42%; font-size:11px;"><div style="font-weight:600; color:var(--text-primary);">推荐</div><div style="font-size:10px; color:var(--text-secondary); font-variant-numeric:tabular-nums;">4 000</div></div>

    <div style="position:absolute; left:34%; top:18%; font-size:11px; transform:translateX(-50%); text-align:center;"><div style="font-weight:600; color:var(--text-primary);">7-day Trial</div><div style="font-size:10px; color:var(--text-secondary); font-variant-numeric:tabular-nums;">14 000</div></div>
    <div style="position:absolute; left:34%; top:46%; font-size:11px; transform:translateX(-50%); text-align:center;"><div style="font-weight:600; color:var(--text-primary);">Demo Booked</div><div style="font-size:10px; color:var(--text-secondary); font-variant-numeric:tabular-nums;">6 000</div></div>
    <div style="position:absolute; left:34%; top:70%; font-size:11px; transform:translateX(-50%); text-align:center;"><div style="font-weight:600; color:var(--text-secondary); opacity:0.7;">未激活</div><div style="font-size:10px; color:var(--text-secondary); font-variant-numeric:tabular-nums;">4 000</div></div>

    <div style="position:absolute; left:64%; top:8%;  font-size:11px; transform:translateX(-50%); text-align:center;"><div style="font-weight:600; color:var(--text-primary);">Starter $29</div><div style="font-size:10px; color:var(--text-secondary); font-variant-numeric:tabular-nums;">6 800</div></div>
    <div style="position:absolute; left:64%; top:28%; font-size:11px; transform:translateX(-50%); text-align:center;"><div style="font-weight:600; color:var(--text-primary);">Pro $99</div><div style="font-size:10px; color:var(--text-secondary); font-variant-numeric:tabular-nums;">3 200</div></div>
    <div style="position:absolute; left:64%; top:60%; font-size:11px; transform:translateX(-50%); text-align:center;"><div style="font-weight:600; color:var(--text-secondary); opacity:0.7;">Trial 流失</div><div style="font-size:10px; color:var(--text-secondary); font-variant-numeric:tabular-nums;">10 000</div></div>

    <div style="position:absolute; right:0; top:12%; font-size:12px; text-align:right;"><div style="font-weight:700; color:var(--accent-1);">续约</div><div style="font-size:11px; color:var(--text-primary); font-variant-numeric:tabular-nums; font-weight:600;">7 600</div></div>
    <div style="position:absolute; right:0; top:38%; font-size:12px; text-align:right;"><div style="font-weight:700; color:var(--text-secondary);">流失</div><div style="font-size:11px; color:var(--text-primary); font-variant-numeric:tabular-nums; font-weight:600;">2 400</div></div>

  </div>
</div>
```

**Puntos de implementación**:

- **La barra de flujo usa SVG `<ruta>` en lugar de `<polígono>`** - La firma de Sankey es la curva S suave (Bézier cúbica), escrita como `M startX,startY C cp1X,cp1Y cp2X,cp2Y endX,endY`, los dos puntos de control X están establecidos en 30%/70% de X en ambos extremos, e Y está alineado con los puntos finales.
- **Agilizar ancho = `trazo-ancho`** - Dibujar el trazado como una línea ancha, **no** como un relleno de polígono cerrado. ancho de trazo directamente = valor × escala (en este caso escala ≈ 0.005, 12000 → ~60px). Esta es la forma más elegante de implementar un diagrama de Sankey.
- **Pista dual de color de la barra de transmisión**: use `--accent-1` para transmisiones exitosas (prueba → pago → renovar); use `--accent-3` o baja opacidad para abandonar/abandonar transmisiones (drop1/drop2/churn). Distinga visualmente "ruta saludable" y "abandono" de un vistazo.
- **El nodo utiliza un `<rect>`** estrecho (ancho de 14px × alto del valor del nodo), cerca del punto inicial/final de la barra de flujo. El relleno del nodo tiene el mismo color que la barra de flujo pero tiene una opacidad más alta (0,85 frente a 0,42), lo que forma la apariencia característica de Sankey de "columna sólida + flujo transparente".
- **Altura del nodo = suma(salida) = suma(entrada)** - Esta es la ley de conservación de Sankey. Al calcular el valor a mano, debe equilibrar aguas arriba y aguas abajo, de lo contrario se producirá una desalineación visual. Este ejemplo: prueba7 (14000) = 8000+4500+1500 (entrada) = 4800+2200+7000 (salida).
- **`stroke-linecap="butt"`** (el valor predeterminado es suficiente) - `round` hará que el final de la barra de flujo exceda el rectángulo del nodo, destruyendo la alineación.

**Autocomprobación**:

- [ ] Suma de entradas en cada nodo = suma de salidas (conservación)
- [ ] El ancho de carrera de la barra de flujo es linealmente proporcional al valor
- [] La diferencia de color entre el éxito y el flujo de abandono es obvia (acento-1 vs acento-3)
- [] La altura del rectángulo del nodo es proporcional al valor del nodo
- [] SVG usa `preserveAspectRatio="none"` + viewBox fijo para alinearse con etiquetas HTML
- [ ] SVG interno cero `<texto>`



- Más de 5 columnas: al aumentar el número de columnas, cambie el viewBox a 1400×500 y espacie uniformemente las columnas. Se recomienda proporcionar `scripts/sankey_layout.py`, nodos de entrada/flujos JSON y generar el valor d de cada ruta.
- Resaltado al pasar el cursor sobre la barra de flujo: este canal no admite interacción. Solo puedes seleccionar una ruta principal en capturas de pantalla estáticas en negrita + alta opacidad
- Los valores numéricos están marcados en la barra de flujo: esta tubería no puede seguir la curva y solo puede usar div HTML para superponer números en la sección más ancha (solo las 1 o 2 líneas más grandes)

---

## 18. Calendario térmico (`heatmap_calendar`)

**Cuándo utilizar**:

- 365 días de actividad/número de confirmaciones/historial de DAU (clásico de contribuciones de GitHub)
- Densidad de eventos durante todo el año (actividades operativas, informes de errores, registros de ventas)
- Información estacional (qué meses son densos y qué semanas son frías)

No utilice esta plantilla cuando los puntos de datos sean <100 (una minipolilínea será suficiente). La ventaja de este gráfico es que permite leer 365 puntos de datos en una pantalla al mismo tiempo.

**Formato de datos**:

```json
{
  "year": 2026,
  "metric": "代码提交数",
  "total": 1843,
  "max_per_day": 24,
  "days": [
    {"date": "2026-01-01", "value": 0,  "level": 0},
    {"date": "2026-01-02", "value": 3,  "level": 1},
    {"date": "2026-01-03", "value": 8,  "level": 2}
  ],
  "month_labels": ["1月","2月","3月","4月","5月","6月","7月","8月","9月","10月","11月","12月"]
}
```

`level` ∈ {0, 1, 2, 3, 4, 5} es un depósito de intensidad discreta (GitHub usa 5 depósitos; esta plantilla usa 6 depósitos para coincidir con el rango de datos del proyecto). Sugerencias de mapeo:

| nivel | rango de valores | opacidad |
|-------|----------|---------|
| 0 | 0 | 0,06 |
| 1 | 1-3 | 0,22 |
| 2 | 4-7 | 0,40 |
| 3 | 8-12 | 0,60 |
| 4 | 13-18 | 0,80 |
| 5 | 19+ | 1,00 |

**Plantilla HTML** (completa y ejecutable):

```html
<div class="chart-heatmap-calendar" style="position:relative; width:100%; aspect-ratio: 16/5; padding: 24px 32px 28px 56px;">

  <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom: 18px;">
    <div>
      <div style="font-size:11px; letter-spacing:0.18em; text-transform:uppercase; color:var(--accent-1); font-weight:600;">— 365-DAY ACTIVITY</div>
      <div style="font-size:20px; font-weight:600; letter-spacing:-0.01em; color:var(--text-primary); margin-top:6px;">代码提交日历 · 2026</div>
    </div>
    <div style="text-align:right;">
      <div style="font-size:28px; font-weight:700; letter-spacing:-0.02em; color:var(--text-primary); font-variant-numeric: tabular-nums;">1 843<span style="font-size:13px; color:var(--text-secondary); font-weight:500; margin-left:6px;">次提交 · 全年</span></div>
      <div style="font-size:11px; color:var(--text-secondary); letter-spacing:0.05em; margin-top:2px;">最长连续 47 天 · 平均 5.05 / 日</div>
    </div>
  </div>

  <div style="position:relative; padding-top:16px;">

    <div style="position:absolute; top:0; left:0; right:0; display:grid; grid-template-columns: repeat(53, 1fr); font-size:9px; color:var(--text-secondary); letter-spacing:0.04em; pointer-events:none;">
      <div style="grid-column: 1 / 6;">Jan</div>
      <div style="grid-column: 6 / 10;">Feb</div>
      <div style="grid-column: 10 / 14;">Mar</div>
      <div style="grid-column: 14 / 19;">Apr</div>
      <div style="grid-column: 19 / 23;">May</div>
      <div style="grid-column: 23 / 27;">Jun</div>
      <div style="grid-column: 27 / 32;">Jul</div>
      <div style="grid-column: 32 / 36;">Aug</div>
      <div style="grid-column: 36 / 41;">Sep</div>
      <div style="grid-column: 41 / 45;">Oct</div>
      <div style="grid-column: 45 / 49;">Nov</div>
      <div style="grid-column: 49 / 54;">Dec</div>
    </div>

    <div style="position:absolute; top:18px; left:-44px; display:grid; grid-template-rows: repeat(7, 1fr); height:calc(7 * (100% / 7) - 0px); gap:2px; font-size:9px; color:var(--text-secondary); align-items:center;">
      <div></div>
      <div>Mon</div>
      <div></div>
      <div>Wed</div>
      <div></div>
      <div>Fri</div>
      <div></div>
    </div>

    <div style="display:grid; grid-template-columns: repeat(53, 1fr); grid-template-rows: repeat(7, 1fr); gap:2px; aspect-ratio: 53 / 7;">

      <div style="grid-column:1; grid-row:1; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div>
      <div style="grid-column:1; grid-row:2; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div>
      <div style="grid-column:1; grid-row:3; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>
      <div style="grid-column:1; grid-row:4; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div>
      <div style="grid-column:1; grid-row:5; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>
      <div style="grid-column:1; grid-row:6; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div>
      <div style="grid-column:1; grid-row:7; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div>

      <div style="grid-column:2; grid-row:1; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div>
      <div style="grid-column:2; grid-row:2; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div>
      <div style="grid-column:2; grid-row:3; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div>
      <div style="grid-column:2; grid-row:4; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div>
      <div style="grid-column:2; grid-row:5; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div>
      <div style="grid-column:2; grid-row:6; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>
      <div style="grid-column:2; grid-row:7; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div>

      <div style="grid-column:3; grid-row:1; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>
      <div style="grid-column:3; grid-row:2; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div>
      <div style="grid-column:3; grid-row:3; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div>
      <div style="grid-column:3; grid-row:4; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div>
      <div style="grid-column:3; grid-row:5; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div>
      <div style="grid-column:3; grid-row:6; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div>
      <div style="grid-column:3; grid-row:7; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>

      <div style="grid-column:4; grid-row:1; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div>
      <div style="grid-column:4; grid-row:2; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div>
      <div style="grid-column:4; grid-row:3; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div>
      <div style="grid-column:4; grid-row:4; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div>
      <div style="grid-column:4; grid-row:5; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div>
      <div style="grid-column:4; grid-row:6; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div>
      <div style="grid-column:4; grid-row:7; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>

      <div style="grid-column:5; grid-row:1; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>
      <div style="grid-column:5; grid-row:2; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div>
      <div style="grid-column:5; grid-row:3; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div>
      <div style="grid-column:5; grid-row:4; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div>
      <div style="grid-column:5; grid-row:5; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>
      <div style="grid-column:5; grid-row:6; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div>
      <div style="grid-column:5; grid-row:7; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div>

      <div style="grid-column:6; grid-row:1; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div>
      <div style="grid-column:6; grid-row:2; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>
      <div style="grid-column:6; grid-row:3; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div>
      <div style="grid-column:6; grid-row:4; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div>
      <div style="grid-column:6; grid-row:5; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div>
      <div style="grid-column:6; grid-row:6; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div>
      <div style="grid-column:6; grid-row:7; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>

      <div style="grid-column:7; grid-row:1; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div>
      <div style="grid-column:7; grid-row:2; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div>
      <div style="grid-column:7; grid-row:3; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div>
      <div style="grid-column:7; grid-row:4; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div>
      <div style="grid-column:7; grid-row:5; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div>
      <div style="grid-column:7; grid-row:6; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div>
      <div style="grid-column:7; grid-row:7; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div>

      <div style="grid-column:8; grid-row:1; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>
      <div style="grid-column:8; grid-row:2; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div>
      <div style="grid-column:8; grid-row:3; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div>
      <div style="grid-column:8; grid-row:4; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div>
      <div style="grid-column:8; grid-row:5; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>
      <div style="grid-column:8; grid-row:6; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>
      <div style="grid-column:8; grid-row:7; aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div>

      <div style="grid-column:9 / 13; grid-row:1 / 8; display:grid; grid-template-columns: repeat(4, 1fr); grid-template-rows: repeat(7, 1fr); gap:2px;">
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div>
      </div>

      <div style="grid-column:13 / 27; grid-row:1 / 8; display:grid; grid-template-columns: repeat(14, 1fr); grid-template-rows: repeat(7, 1fr); gap:2px;">
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div>
      </div>

      <div style="grid-column:27 / 41; grid-row:1 / 8; display:grid; grid-template-columns: repeat(14, 1fr); grid-template-rows: repeat(7, 1fr); gap:2px;">
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div>
      </div>

      <div style="grid-column:41 / 54; grid-row:1 / 8; display:grid; grid-template-columns: repeat(13, 1fr); grid-template-rows: repeat(7, 1fr); gap:2px;">
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:1.00;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.80;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.60;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div>
        <div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.40;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.22;"></div><div style="aspect-ratio:1; border-radius:2px; background:var(--accent-1); opacity:0.06;"></div>
      </div>

    </div>
  </div>

  <div style="margin-top:14px; display:flex; align-items:center; justify-content:flex-end; gap:8px;">
    <span style="font-size:10px; letter-spacing:0.12em; color:var(--text-secondary); text-transform:uppercase;">Less</span>
    <span style="display:inline-block; width:11px; height:11px; border-radius:2px; background:var(--accent-1); opacity:0.06;"></span>
    <span style="display:inline-block; width:11px; height:11px; border-radius:2px; background:var(--accent-1); opacity:0.22;"></span>
    <span style="display:inline-block; width:11px; height:11px; border-radius:2px; background:var(--accent-1); opacity:0.40;"></span>
    <span style="display:inline-block; width:11px; height:11px; border-radius:2px; background:var(--accent-1); opacity:0.60;"></span>
    <span style="display:inline-block; width:11px; height:11px; border-radius:2px; background:var(--accent-1); opacity:0.80;"></span>
    <span style="display:inline-block; width:11px; height:11px; border-radius:2px; background:var(--accent-1); opacity:1.00;"></span>
    <span style="font-size:10px; letter-spacing:0.12em; color:var(--text-secondary); text-transform:uppercase;">More</span>
  </div>

</div>
```

**Puntos de implementación**:



**Autocomprobación**:

- [] 53 columnas × 7 filas = 371 celdas (cubre 365-366 días)
- [] Mantenga todas las celdas cuadradas con `relación de aspecto: 1`
- [ ] Un solo color (`--accent-1`), solo cambia la opacidad
- [] 6 cubos de opacidad discretos (0,06 / 0,22 / 0,40 / 0,60 / 0,80 / 1,00)
- [] El intervalo de columnas de la cuadrícula de la etiqueta del mes = el número de semanas correspondientes al mes
- [ ] Leyenda 6 párrafos + Menos / Más texto
- [] números (total/máx.) en números tabulares

**Futuras expansiones (v2)**:



---

## Lista de verificación de implementación común

Antes de generar gráficos complejos, verifique:

- [] **Datos primero**: todos los valores se han asignado a depósitos de `intensidad`/`nivel`/`opacidad`. **No dejes que la plantilla haga los cálculos**: la plantilla solo es responsable de renderizar
- [ ] **Color 100% variable CSS** - no permite codificación física como `#22D3EE`
- [ ] **SVG cero interno `<text>`** - todas las etiquetas son elementos HTML, superposiciones absolutamente posicionadas
- [] **Números abiertos tabular-nums**——especialmente números grandes (`total`, `max`, KPI)
- [] **Utilice `preserveAspectRatio="none"`** (red, sankey) con viewBox para alinear la geometría SVG con etiquetas de porcentaje HTML
- [] **No incluya JS, no use gradiente cónico/imagen-máscara/modo-mezcla-mezcla/filtro:desenfoque()**
- [ ] **Responsivo**: use porcentaje/relación de aspecto para todas las posiciones, no px absolutos; fácil de pegar en tarjetas de cualquier tamaño dentro de 1280×720 PPT

## Ruta de actualización

| Estado actual | Condiciones de activación de actualización | plano v2 |
|------|------------|---------|
| Ruta de 12 países simplificada | Más de 20 países/clientes solicitan mapas reales | GeoJSON sin conexión → topojson-simplify → Ruta en línea |
| Coordenadas manuales de la red presupuestaria | Nodos > 12 / Aristas > 20 | Python `networkx.spring_layout()` Cálculo de coordenadas sin conexión |
| Ruta manual Sankey de 4 columnas | Más de 5 columnas/número de transmisiones > 25 | Python `sankey_layout.py` calcula automáticamente el valor d de la ruta |
| Cuadrícula anidada de 371 celdas | Dinámica de datos / muchos años | Generación de ciclo de plantilla Jinja 371 div |

Cada ruta de actualización no introduce JS** en tiempo de ejecución: cálculo fuera de línea + generación de plantilla = compatibilidad de canalización.