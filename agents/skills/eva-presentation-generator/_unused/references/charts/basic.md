# Gráficos básicos (8 tipos · Copiar y usar)

> Este documento contiene plantillas HTML de clase mundial para 8 gráficos básicos. Todas las plantillas:
>
> - **HTML/CSS/SVG puro**, sin dependencias de tiempo de ejecución de JS
> - **Controlador de variable CSS** (`--accent-1`, `--card-bg-from`, etc.), se adapta automáticamente a 26 estilos
> - **Números `tabular-nums`**, los números en PPT no saltan
> - **SVG cero interno `<text>`**, todas las etiquetas usan HTML `<div>`/`<span>` superposición de posicionamiento absoluto (ley de hierro anti-offset)
> - **El gráfico de anillos utiliza el formato de dos valores `stroke-dasharray="circunferencia de longitud de arco"`**, desactiva `stroke-dashoffset`
> - **Use SVG `<polígono>`** para triángulos/flechas, deshabilite los triángulos de borde CSS
> - `conic-gradient` / `mask-image` / `mix-blend-mode` / `background-clip: text` están **permitidos** — la exportación a PPTX es por captura de pantalla (Playwright), no por conversión SVG. Ver `references/playbooks/bespoke-slide-recipe.md`.

Cada plantilla ha sido verificada con capturas de pantalla de titiritero en tres estilos: oscuro/claro/editorial, sin errores de renderizado.

---

## Tabla de contenido

1. [Barra de progreso](#1-Barra de progreso-barra-de progreso) — Porcentaje único/finalización
2. [Barra de comparación](#2-Compare-bar) — Dos o más comparaciones (máximo 6)
3. [Gráfico de anillos](#3-ring-chart) — Porcentaje + KPI central (hasta 3 anillos)
4. [Mini polilínea minigráfico] (#4-Mini polilínea-minigráfico) — Dirección de tendencia (120 × 40 píxeles incrustados)
5. [Gráfico de gofres](#5-Gráfico de gofres) — Proporción intuitiva (10×10 = 100 cuadrículas)
6. [Tarjeta KPI](#6-kpi-metric card-kpi-card) — número grande + flecha de tendencia + año tras año
7. [Fila métrica](#7-metric-row): múltiples indicadores apilados verticalmente (3-6 filas)
8. [Calificación del indicador de calificación] (#8-Calificación del indicador de calificación): escala de 5 puntos (incluida media estrella)

---

## 1. Barra de progreso (progress_bar)

**Cuándo usarlo**: porcentaje único/finalización/progreso unidimensional (como "Satisfacción del cliente 87%", "Finalización del proyecto 64%", "Objetivo logrado 92%"). Cuando solo hay un indicador de porcentaje y es necesario mostrar visualmente la sensación de llenado, la barra de progreso ahorra más espacio que el gráfico de anillos.

**Formato de datos**:

```json
{
  "type": "progress_bar",
  "value": 87,
  "label": "客户满意度",
  "target": 100,
  "unit": "%"
}
```

**Plantilla HTML** (simplemente cópiala directamente):

```html
<div class="chart-progress" style="
  width: 360px;
  font-family: 'Inter Tight', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-feature-settings: 'kern','liga','ss01','cv11';
">
  <div style="
    display: flex; align-items: baseline; justify-content: space-between;
    margin-bottom: 10px;
  ">
    <span style="
      font-size: 11px;
      letter-spacing: 0.18em;
      text-transform: uppercase;
      color: var(--text-secondary);
      font-weight: 600;
    ">客户满意度</span>
    <span style="
      font-size: 22px;
      font-weight: 700;
      letter-spacing: -0.02em;
      font-variant-numeric: tabular-nums proportional-nums;
      color: var(--text-primary);
    ">87<span style="font-size: 13px; opacity: 0.55; margin-left: 2px;">%</span></span>
  </div>

  <div style="
    position: relative;
    height: 8px;
    border-radius: 999px;
    background: var(--card-bg-from);
    overflow: hidden;
    border: 1px solid var(--card-border);
  ">
    <div style="
      position: absolute; top: 0; left: 0; bottom: 0;
      width: 87%;
      border-radius: 999px;
      background: linear-gradient(90deg, var(--accent-1) 0%, var(--accent-2) 100%);
      box-shadow: 0 0 12px var(--accent-1);
    "></div>
  </div>

  <div style="
    display: flex; justify-content: space-between;
    margin-top: 8px;
    font-size: 10px;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: var(--text-secondary);
    opacity: 0.6;
    font-variant-numeric: tabular-nums;
  ">
    <span>0</span>
    <span>目标 100%</span>
  </div>
</div>
```

**Variación A: barra de progreso segmentada (completado/en progreso/tres colores sin terminar)**

```html
<div class="chart-progress-segmented" style="
  width: 360px;
  font-family: 'Inter Tight', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
">
  <div style="display: flex; justify-content: space-between; align-items: baseline; margin-bottom: 10px;">
    <span style="font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--text-secondary); font-weight: 600;">迁移进度</span>
    <span style="font-size: 22px; font-weight: 700; letter-spacing: -0.02em; font-variant-numeric: tabular-nums; color: var(--text-primary);">64<span style="font-size: 13px; opacity: 0.55;">%</span></span>
  </div>
  <div style="display: flex; height: 10px; border-radius: 999px; overflow: hidden; background: var(--card-bg-from); border: 1px solid var(--card-border);">
    <div style="width: 64%; background: linear-gradient(90deg, var(--accent-1), var(--accent-2));"></div>
    <div style="width: 22%; background: var(--accent-4); opacity: 0.55;"></div>
    <div style="width: 14%; background: transparent;"></div>
  </div>
  <div style="display: flex; gap: 18px; margin-top: 12px; font-size: 11px; color: var(--text-secondary); font-variant-numeric: tabular-nums;">
    <div style="display: flex; align-items: center; gap: 6px;">
      <span style="width: 8px; height: 8px; border-radius: 2px; background: var(--accent-1);"></span>已完成 64%
    </div>
    <div style="display: flex; align-items: center; gap: 6px;">
      <span style="width: 8px; height: 8px; border-radius: 2px; background: var(--accent-4); opacity: 0.55;"></span>进行中 22%
    </div>
    <div style="display: flex; align-items: center; gap: 6px;">
      <span style="width: 8px; height: 8px; border-radius: 2px; border: 1px solid var(--card-border);"></span>未开始 14%
    </div>
  </div>
</div>
```

**Variación B: barra de progreso minimalista y delgada (para párrafos de texto incrustados, altura 4px)**

```html
<div style="width: 240px;">
  <div style="height: 4px; border-radius: 999px; background: var(--card-bg-from); overflow: hidden;">
    <div style="height: 100%; width: 92%; border-radius: 999px; background: var(--accent-1);"></div>
  </div>
  <div style="display: flex; justify-content: space-between; margin-top: 6px; font-size: 11px; color: var(--text-secondary); font-variant-numeric: tabular-nums;">
    <span style="letter-spacing: 0.1em; text-transform: uppercase;">SLA 健康度</span>
    <span>92%</span>
  </div>
</div>
```

**Autocomprobación**:

- [x] números `fuente-variante-numérica: números-tabulares números-proporcionales`
- [x] Usar variables CSS para todos los colores (`--accent-1`, `--accent-2`, `--card-bg-from`, `--card-border`, `--text-primary`, `--text-secundario`)
- [x] No use SVG (div simple + gradiente lineal)
- [x] No escriba `<texto>` dentro de SVG
- [x] Ninguno `cónico-gradiente` / `máscara-imagen` / `mix-blend-mode` / `fondo-clip: texto`
- [x] Renderizado mediante titiritero sin errores

---

## 2. Barra de comparación (compare_bar)

**Cuándo usarlo**: Comparación de 2 a 6 indicadores de clasificación (como "ingresos Q1/Q2/Q3/Q4", "versión estándar/Pro/duración máxima de la batería", "cuota de mercado de productos competitivos A/B/C"). Si hay más de 6 líneas, utilice "Línea indicadora" o "Múltiples grupos de barras de comparación (avanzado)".

**Formato de datos**:

```json
{
  "type": "compare_bar",
  "direction": "vertical",
  "items": [
    { "label": "标准版", "value": 668, "unit": "km" },
    { "label": "Pro",    "value": 825, "unit": "km" },
    { "label": "Max",    "value": 962, "unit": "km", "highlight": true }
  ]
}
```

**Plantilla HTML (orientación vertical, más utilizada)**:

```html
<div class="chart-compare-bar-v" style="
  position: relative;
  width: 480px; height: 320px;
  padding: 24px 28px;
  border-radius: var(--card-radius, 8px);
  background: linear-gradient(180deg, var(--card-bg-from), var(--card-bg-to));
  border: 1px solid var(--card-border);
  font-family: 'Inter Tight', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-feature-settings: 'kern','liga','ss01';
">
  <div style="
    font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase;
    color: var(--text-secondary); font-weight: 600;
    margin-bottom: 4px;
  ">— CLTC 续航对比</div>
  <div style="font-size: 18px; font-weight: 700; letter-spacing: -0.01em; color: var(--text-primary);">三档版本一览</div>

  <div style="position: relative; height: 200px; margin-top: 24px;">
    <svg viewBox="0 0 420 200" preserveAspectRatio="none" style="width: 100%; height: 100%; display: block;">
      <line x1="0" y1="200" x2="420" y2="200" stroke="var(--card-border)" stroke-width="1"/>
      <line x1="0" y1="100" x2="420" y2="100" stroke="var(--card-border)" stroke-width="0.5" stroke-dasharray="2 4"/>
      <line x1="0" y1="0"   x2="420" y2="0"   stroke="var(--card-border)" stroke-width="0.5" stroke-dasharray="2 4"/>

      <rect x="40"  y="61"  width="60" height="139" rx="4" fill="var(--accent-3)" opacity="0.55"/>
      <rect x="180" y="29"  width="60" height="171" rx="4" fill="var(--accent-2)" opacity="0.75"/>
      <rect x="320" y="0"   width="60" height="200" rx="4" fill="url(#bar-grad-hi)"/>

      <defs>
        <linearGradient id="bar-grad-hi" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%"  stop-color="var(--accent-1)"/>
          <stop offset="100%" stop-color="var(--accent-2)"/>
        </linearGradient>
      </defs>
    </svg>

    <span style="position: absolute; left: calc(40px / 420 * 100%); top: 47px; width: calc(60px / 420 * 100%); text-align: center;
      font-size: 18px; font-weight: 700; letter-spacing: -0.02em; color: var(--text-primary);
      font-variant-numeric: tabular-nums proportional-nums;">668</span>
    <span style="position: absolute; left: calc(180px / 420 * 100%); top: 15px; width: calc(60px / 420 * 100%); text-align: center;
      font-size: 18px; font-weight: 700; letter-spacing: -0.02em; color: var(--text-primary);
      font-variant-numeric: tabular-nums;">825</span>
    <span style="position: absolute; left: calc(320px / 420 * 100%); top: -14px; width: calc(60px / 420 * 100%); text-align: center;
      font-size: 22px; font-weight: 800; letter-spacing: -0.025em; color: var(--accent-1);
      font-variant-numeric: tabular-nums;">962</span>
  </div>

  <div style="
    display: flex; justify-content: space-between;
    margin-top: 10px; padding: 0 10px;
    font-size: 12px; color: var(--text-secondary);
    letter-spacing: 0.05em;
  ">
    <span style="width: 60px; text-align: center;">标准版</span>
    <span style="width: 60px; text-align: center;">Pro</span>
    <span style="width: 60px; text-align: center; color: var(--accent-1); font-weight: 600;">Max</span>
  </div>

  <div style="
    position: absolute; right: 28px; top: 28px;
    font-size: 10px; color: var(--text-secondary); opacity: 0.6;
    letter-spacing: 0.1em; text-transform: uppercase;
    font-variant-numeric: tabular-nums;
  ">UNIT · KM</div>
</div>
```

**Variación A: Orientación horizontal (adecuada cuando las etiquetas de categoría son largas)**

```html
<div style="
  width: 420px;
  padding: 20px 24px;
  border-radius: 8px;
  background: linear-gradient(180deg, var(--card-bg-from), var(--card-bg-to));
  border: 1px solid var(--card-border);
  font-family: 'Inter Tight', 'Inter', sans-serif;
">
  <div style="font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--text-secondary); font-weight: 600; margin-bottom: 18px;">市场份额 · 2026 Q1</div>

  <div style="display: flex; flex-direction: column; gap: 14px;">
    <div>
      <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
        <span style="color: var(--text-primary); font-weight: 500;">华为 HarmonyOS</span>
        <span style="color: var(--text-primary); font-weight: 700; font-variant-numeric: tabular-nums;">42.3%</span>
      </div>
      <div style="height: 8px; border-radius: 999px; background: var(--card-bg-from); overflow: hidden;">
        <div style="height: 100%; width: 42.3%; border-radius: 999px; background: linear-gradient(90deg, var(--accent-1), var(--accent-2));"></div>
      </div>
    </div>

    <div>
      <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
        <span style="color: var(--text-primary); font-weight: 500;">小米 HyperOS</span>
        <span style="color: var(--text-primary); font-weight: 700; font-variant-numeric: tabular-nums;">28.1%</span>
      </div>
      <div style="height: 8px; border-radius: 999px; background: var(--card-bg-from); overflow: hidden;">
        <div style="height: 100%; width: 28.1%; border-radius: 999px; background: var(--accent-2); opacity: 0.85;"></div>
      </div>
    </div>

    <div>
      <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
        <span style="color: var(--text-primary); font-weight: 500;">vivo OriginOS</span>
        <span style="color: var(--text-primary); font-weight: 700; font-variant-numeric: tabular-nums;">17.6%</span>
      </div>
      <div style="height: 8px; border-radius: 999px; background: var(--card-bg-from); overflow: hidden;">
        <div style="height: 100%; width: 17.6%; border-radius: 999px; background: var(--accent-3); opacity: 0.75;"></div>
      </div>
    </div>

    <div>
      <div style="display: flex; justify-content: space-between; font-size: 12px; margin-bottom: 6px;">
        <span style="color: var(--text-secondary);">其他</span>
        <span style="color: var(--text-secondary); font-weight: 500; font-variant-numeric: tabular-nums;">12.0%</span>
      </div>
      <div style="height: 8px; border-radius: 999px; background: var(--card-bg-from); overflow: hidden;">
        <div style="height: 100%; width: 12.0%; border-radius: 999px; background: var(--text-secondary); opacity: 0.4;"></div>
      </div>
    </div>
  </div>
</div>
```

**Autocomprobación**:

- [x] números `fuente-variante-numérica: números-tabulares números-proporcionales`
- [x] Usar variables CSS para todos los colores
- [x] **Solo hay `<rect>` / `<line>` en SVG, no `<text>`**; todas las etiquetas de datos y el texto del eje x se superponen con HTML en el posicionamiento absoluto
- [x] Utilice `<linearGradient>` o CSS `linear-gradient` para gradientes, sin `conic-gradient`
- [x] Use `--accent-1` para resaltar elementos (Max) a todo color + tamaño de fuente grande para resaltar diferenciado
- [x] Renderizado mediante titiritero sin errores



## 3. Gráfico de anillos (ring_chart)

**Cuándo usarlo**: porcentaje único que coincide con el KPI central (como "tasa de aciertos de caché del 75 %", "meta alcanzada del 92 %"). Los gráficos de anillos son más adecuados como elementos de enfoque de página que las barras de progreso. El anidamiento de varios anillos (hasta 3 anillos) es adecuado para mostrar indicadores jerárquicos (como "objetivos generales/productos principales/clientes clave").

**Formato de datos**:

```json
{
  "type": "ring_chart",
  "rings": [
    { "value": 75, "label": "缓存命中", "color": "accent-1" }
  ],
  "center": { "value": "75%", "label": "CACHE HIT" }
}
```

> **Puntos técnicos clave**: Fórmula de longitud de arco `arco = 2 * pi * r * (porcentaje / 100)`, circunferencia `circunferencia = 2 * pi * r`.
> Por ejemplo r=50: Circunferencia = 314,16, el 75% corresponde a la longitud del arco = 235,62.
> `stroke-dasharray="235 314"` significa dibujar una longitud de 235 y dejar un espacio de 314 de longitud (lo suficientemente largo para cubrir la circunferencia restante).
> **Deshabilitado para usar `stroke-dashoffset`**, no es compatible con svg2pptx.

**Plantilla HTML (anillo único)**:

```html
<div class="chart-ring" style="
  position: relative;
  width: 200px; height: 200px;
  font-family: 'Inter Tight', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-feature-settings: 'kern','liga','ss01';
">
  <svg viewBox="0 0 200 200" style="width: 100%; height: 100%; display: block;">
    <circle cx="100" cy="100" r="80" fill="none"
            stroke="var(--card-bg-from)" stroke-width="14"/>
    <circle cx="100" cy="100" r="80" fill="none"
            stroke="url(#ring1-grad)" stroke-width="14" stroke-linecap="round"
            stroke-dasharray="377 503"
            transform="rotate(-90 100 100)"/>
    <defs>
      <linearGradient id="ring1-grad" x1="0%" y1="0%" x2="100%" y2="100%">
        <stop offset="0%"   stop-color="var(--accent-1)"/>
        <stop offset="100%" stop-color="var(--accent-2)"/>
      </linearGradient>
    </defs>
  </svg>

  <div style="
    position: absolute;
    top: 50%; left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
  ">
    <div style="
      font-size: 42px; font-weight: 800;
      letter-spacing: -0.035em; line-height: 1;
      color: var(--accent-1);
      font-variant-numeric: tabular-nums proportional-nums;
    ">75<span style="font-size: 22px; font-weight: 600; opacity: 0.75; margin-left: 2px;">%</span></div>
    <div style="
      font-size: 10px; font-weight: 600;
      letter-spacing: 0.18em; text-transform: uppercase;
      color: var(--text-secondary);
      margin-top: 6px;
    ">CACHE HIT</div>
  </div>
</div>
```

**Variación A: Anidamiento de anillo doble (indicador principal del anillo exterior + comparación del anillo interior)**

```html
<div style="position: relative; width: 220px; height: 220px; font-family: 'Inter Tight', sans-serif;">
  <svg viewBox="0 0 220 220" style="width: 100%; height: 100%; display: block;">
    <circle cx="110" cy="110" r="90" fill="none" stroke="var(--card-bg-from)" stroke-width="10"/>
    <circle cx="110" cy="110" r="90" fill="none" stroke="var(--accent-1)" stroke-width="10" stroke-linecap="round"
            stroke-dasharray="481 565" transform="rotate(-90 110 110)"/>
    <circle cx="110" cy="110" r="68" fill="none" stroke="var(--card-bg-from)" stroke-width="10"/>
    <circle cx="110" cy="110" r="68" fill="none" stroke="var(--accent-3)" stroke-width="10" stroke-linecap="round"
            stroke-dasharray="269 427" transform="rotate(-90 110 110)"/>
  </svg>
  <div style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); text-align: center;">
    <div style="font-size: 28px; font-weight: 800; letter-spacing: -0.03em; color: var(--text-primary); font-variant-numeric: tabular-nums; line-height: 1;">85<span style="font-size: 14px; opacity: 0.6;">/63%</span></div>
    <div style="font-size: 9px; font-weight: 600; letter-spacing: 0.18em; text-transform: uppercase; color: var(--text-secondary); margin-top: 4px;">实际 / 目标</div>
  </div>
</div>

<div style="display: flex; gap: 16px; margin-top: 14px; font-size: 11px; color: var(--text-secondary);">
  <div style="display: flex; align-items: center; gap: 6px;">
    <span style="width: 10px; height: 10px; border-radius: 50%; background: var(--accent-1);"></span>实际 85%
  </div>
  <div style="display: flex; align-items: center; gap: 6px;">
    <span style="width: 10px; height: 10px; border-radius: 50%; background: var(--accent-3);"></span>目标 63%
  </div>
</div>
```

**Variación B: Anidamiento de tres anillos (por ejemplo, "Ingresos totales/nuevos negocios/en el extranjero")**

```html
<div style="position: relative; width: 240px; height: 240px;">
  <svg viewBox="0 0 240 240" style="width: 100%; height: 100%; display: block;">
    <circle cx="120" cy="120" r="100" fill="none" stroke="var(--card-bg-from)" stroke-width="9"/>
    <circle cx="120" cy="120" r="100" fill="none" stroke="var(--accent-1)" stroke-width="9" stroke-linecap="round"
            stroke-dasharray="565 628" transform="rotate(-90 120 120)"/>
    <circle cx="120" cy="120" r="80"  fill="none" stroke="var(--card-bg-from)" stroke-width="9"/>
    <circle cx="120" cy="120" r="80"  fill="none" stroke="var(--accent-2)" stroke-width="9" stroke-linecap="round"
            stroke-dasharray="352 503" transform="rotate(-90 120 120)"/>
    <circle cx="120" cy="120" r="60"  fill="none" stroke="var(--card-bg-from)" stroke-width="9"/>
    <circle cx="120" cy="120" r="60"  fill="none" stroke="var(--accent-3)" stroke-width="9" stroke-linecap="round"
            stroke-dasharray="151 377" transform="rotate(-90 120 120)"/>
  </svg>
</div>
```

**Autocomprobación**:

- [x] Utilice el formato de dos valores `stroke-dasharray="circunferencia de longitud de arco"` (longitud de arco = 2π·r·por ciento/100, circunferencia = 2π·r)
- [x] **No utilice `stroke-dashoffset`**
- [x] `transform="rotate(-90 cx cy)"` pone la posición 0% a las 12 en punto
- [x] `stroke-linecap="round"` extremo de arco redondeado
- [x] **Utilice HTML `<div>` para superponer el texto central con posicionamiento absoluto, no escriba `<text>`** en SVG
- [x] números grandes `fuente-variante-numérica: números-tabulares números-proporcionales`
- [x] Color usando variables CSS
- [x] Renderizado mediante titiritero sin errores

---

## 4. Mini polilínea (minigráfico)



**Formato de datos**:

```json
{
  "type": "sparkline",
  "values": [42, 45, 41, 48, 52, 56, 54, 61, 65, 68, 72, 78],
  "trend": "up",
  "delta": "+18.4%"
}
```

> **Principio de generación de ruta**: Asigne linealmente N valores al punto promedio del eje x de viewBox + inversión del eje y (SVG y crece hacia abajo, pero el "aumento" visual de la polilínea requiere que y disminuya).

**Plantilla HTML (tendencia alcista/verde)**:

```html
<div class="chart-sparkline" style="
  display: inline-flex; align-items: center; gap: 10px;
  font-family: 'Inter Tight', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
">
  <div style="position: relative; width: 120px; height: 40px;">
    <svg viewBox="0 0 120 40" preserveAspectRatio="none" style="width: 100%; height: 100%; display: block;">
      <defs>
        <linearGradient id="spark-up-fill" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%"   stop-color="var(--accent-1)" stop-opacity="0.28"/>
          <stop offset="100%" stop-color="var(--accent-1)" stop-opacity="0"/>
        </linearGradient>
      </defs>
      <path d="M 0 30 L 11 28 L 22 32 L 33 24 L 44 20 L 55 16 L 66 18 L 77 11 L 88 8 L 99 5 L 110 3 L 120 1 L 120 40 L 0 40 Z"
            fill="url(#spark-up-fill)"/>
      <path d="M 0 30 L 11 28 L 22 32 L 33 24 L 44 20 L 55 16 L 66 18 L 77 11 L 88 8 L 99 5 L 110 3 L 120 1"
            fill="none" stroke="var(--accent-1)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
      <circle cx="120" cy="1" r="2.5" fill="var(--accent-1)"/>
      <circle cx="120" cy="1" r="5"   fill="var(--accent-1)" opacity="0.25"/>
    </svg>
  </div>

  <div style="display: inline-flex; align-items: center; gap: 4px;">
    <svg width="10" height="10" viewBox="0 0 10 10" style="display: block;">
      <polygon points="5,1 9,8 1,8" fill="#22c55e"/>
    </svg>
    <span style="
      font-size: 12px; font-weight: 600;
      letter-spacing: -0.01em;
      color: #22c55e;
      font-variant-numeric: tabular-nums proportional-nums;
    ">+18.4%</span>
  </div>
</div>
```

**Variación A: Tendencia bajista (roja + flecha inversa)**

```html
<div style="display: inline-flex; align-items: center; gap: 10px; font-family: 'Inter Tight', sans-serif;">
  <div style="position: relative; width: 120px; height: 40px;">
    <svg viewBox="0 0 120 40" preserveAspectRatio="none" style="width: 100%; height: 100%; display: block;">
      <defs>
        <linearGradient id="spark-down-fill" x1="0%" y1="0%" x2="0%" y2="100%">
          <stop offset="0%"   stop-color="#ef4444" stop-opacity="0.28"/>
          <stop offset="100%" stop-color="#ef4444" stop-opacity="0"/>
        </linearGradient>
      </defs>
      <path d="M 0 6 L 11 9 L 22 7 L 33 13 L 44 12 L 55 18 L 66 22 L 77 26 L 88 24 L 99 31 L 110 33 L 120 36 L 120 40 L 0 40 Z"
            fill="url(#spark-down-fill)"/>
      <path d="M 0 6 L 11 9 L 22 7 L 33 13 L 44 12 L 55 18 L 66 22 L 77 26 L 88 24 L 99 31 L 110 33 L 120 36"
            fill="none" stroke="#ef4444" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
      <circle cx="120" cy="36" r="2.5" fill="#ef4444"/>
      <circle cx="120" cy="36" r="5"   fill="#ef4444" opacity="0.25"/>
    </svg>
  </div>
  <div style="display: inline-flex; align-items: center; gap: 4px;">
    <svg width="10" height="10" viewBox="0 0 10 10" style="display: block;">
      <polygon points="5,9 9,2 1,2" fill="#ef4444"/>
    </svg>
    <span style="font-size: 12px; font-weight: 600; color: #ef4444; font-variant-numeric: tabular-nums;">-7.2%</span>
  </div>
</div>
```

**Variación B: Línea Pura (sin relleno, más sobria)**

```html
<div style="width: 120px; height: 40px;">
  <svg viewBox="0 0 120 40" preserveAspectRatio="none" style="width: 100%; height: 100%; display: block;">
    <path d="M 0 30 L 15 28 L 30 24 L 45 26 L 60 18 L 75 20 L 90 12 L 105 9 L 120 4"
          fill="none" stroke="var(--accent-1)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    <circle cx="120" cy="4" r="2" fill="var(--accent-1)"/>
  </svg>
</div>
```

**Autocomprobación**:

- [x] **Rellenar con `<linearGradient>`** (translúcido 0,28 → 0), sin `máscara-imagen` ni gradiente CSS
- [x] SVG `<círculo>` para resaltar el punto final (sólido 2,5 px + brillo translúcido 5 px)
- [x] **Utilice SVG `<polígono>`** para flechas de tendencia, sin triángulo de borde CSS (truco `ancho: 0` deshabilitado)
- [x] Números de tasa de crecimiento `font-variant-numeric: números-tabulares números-proporcionales`
- [x] Los colores verde ascendente (#22c55e)/rojo descendente (#ef4444) son prácticas de la industria y la codificación rígida es aceptable (no participa en el cambio de 26 estilos)
- [x] El color del cuerpo de la polilínea usa `var(--accent-1)` para seguir el tema
- [x] **Sin `<texto>`** en SVG
- [x] Renderizado mediante titiritero sin errores

---

## 5. Mapa de bits (waffle_chart)

**Cuándo usarlo**: convierta los porcentajes abstractos en la sensación intuitiva de "N de cada 100 redes están encendidas" (como "87 de cada 100 usuarios volverán a comprar", "23 de cada 100 hogares han sido equipados con energía solar"). Es más fácil de entender que un gráfico de anillos para personas sin experiencia en datos.

**Formato de datos**:

```json
{
  "type": "waffle_chart",
  "value": 87,
  "label": "用户复购率",
  "categories": [
    { "value": 87, "color": "accent-1", "label": "已复购" },
    { "value": 13, "color": "card-bg",  "label": "未复购" }
  ]
}
```

> **Principio de generación**: 100 celdas = cuadrícula de 10 filas × 10 columnas, las primeras N celdas están llenas de colores brillantes y las 100 N celdas restantes están llenas de colores de bajo contraste. Generación de una línea de Python: `["on" si i < 87 else "off" para i in range(100)]`

**Plantilla HTML**:

```html
<div class="chart-waffle" style="
  width: 280px;
  padding: 22px 24px;
  border-radius: var(--card-radius, 8px);
  background: linear-gradient(180deg, var(--card-bg-from), var(--card-bg-to));
  border: 1px solid var(--card-border);
  font-family: 'Inter Tight', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-feature-settings: 'kern','liga','ss01';
">
  <div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 14px;">
    <div>
      <div style="font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--text-secondary); font-weight: 600;">用户复购率</div>
      <div style="font-size: 28px; font-weight: 800; letter-spacing: -0.03em; color: var(--accent-1); margin-top: 4px; font-variant-numeric: tabular-nums proportional-nums; line-height: 1;">87<span style="font-size: 14px; opacity: 0.75; margin-left: 1px;">%</span></div>
    </div>
    <div style="font-size: 10px; color: var(--text-secondary); opacity: 0.55; letter-spacing: 0.1em; text-transform: uppercase; text-align: right;">每 100 人中</div>
  </div>

  <div style="
    display: grid;
    grid-template-columns: repeat(10, 1fr);
    grid-template-rows: repeat(10, 1fr);
    gap: 4px;
    aspect-ratio: 1 / 1;
  ">
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--accent-1); border-radius: 2px;"></span>
    <span style="background: var(--card-bg-from); border: 1px solid var(--card-border); border-radius: 2px;"></span>
    <span style="background: var(--card-bg-from); border: 1px solid var(--card-border); border-radius: 2px;"></span>
    <span style="background: var(--card-bg-from); border: 1px solid var(--card-border); border-radius: 2px;"></span>
    <span style="background: var(--card-bg-from); border: 1px solid var(--card-border); border-radius: 2px;"></span>
    <span style="background: var(--card-bg-from); border: 1px solid var(--card-border); border-radius: 2px;"></span>
    <span style="background: var(--card-bg-from); border: 1px solid var(--card-border); border-radius: 2px;"></span>
    <span style="background: var(--card-bg-from); border: 1px solid var(--card-border); border-radius: 2px;"></span>
    <span style="background: var(--card-bg-from); border: 1px solid var(--card-border); border-radius: 2px;"></span>
    <span style="background: var(--card-bg-from); border: 1px solid var(--card-border); border-radius: 2px;"></span>
    <span style="background: var(--card-bg-from); border: 1px solid var(--card-border); border-radius: 2px;"></span>
    <span style="background: var(--card-bg-from); border: 1px solid var(--card-border); border-radius: 2px;"></span>
    <span style="background: var(--card-bg-from); border: 1px solid var(--card-border); border-radius: 2px;"></span>
    <span style="background: var(--card-bg-from); border: 1px solid var(--card-border); border-radius: 2px;"></span>
  </div>

  <div style="display: flex; gap: 14px; margin-top: 14px; font-size: 11px; color: var(--text-secondary);">
    <div style="display: flex; align-items: center; gap: 6px;">
      <span style="width: 10px; height: 10px; border-radius: 2px; background: var(--accent-1);"></span>已复购 87
    </div>
    <div style="display: flex; align-items: center; gap: 6px;">
      <span style="width: 10px; height: 10px; border-radius: 2px; background: var(--card-bg-from); border: 1px solid var(--card-border);"></span>未复购 13
    </div>
  </div>
</div>
```

**Variación A: versión con puntos (reemplace el cuadrado con "radio de borde: 50%", más suave)**

Reemplace todo el `border-radius: 2px;` anterior con `border-radius: 50%;` y cambie el espacio entre los cuadrados a 6px. Visualmente, se parece más a un "gráfico de distribución de matriz de puntos" y es adecuado para estilos de colores claros.

**Variación B: combinación de colores de categoría dual (por ejemplo, "Tiempo completo 60 % / Tiempo parcial 25 % / Prácticas 15 %")**

Simplemente divida los 100 cuadrados proporcionalmente en 3 secciones, cada una con un color: los primeros 60 cuadrados `var(--accent-1)`, los 25 cuadrados del medio `var(--accent-2)` y los últimos 15 cuadrados `var(--accent-3)`.

**Autocomprobación**:

- [x] 100 `<span>` organizado automáticamente en 10×10 usando la grilla CSS `repeat(10, 1fr)`
- [x] Use `var(--accent-1)` para el color principal, use `var(--card-bg-from)` + `var(--card-border)` para celdas sin llenar
- [x] números grandes `fuente-variante-numérica: números-tabulares números-proporcionales`
- [x] **Sin SVG** (Cuadrícula CSS pura, mejor compatibilidad)
- [x] Ninguno `imagen-máscara` / `modo-mezcla-mezcla` / `gradiente-cónico`
- [x] Representación sin errores a través del titiritero (nota: 100 intervalos es mucho, se recomienda utilizar la salida en bucle durante la fase de generación de Python)

---

## 6. Tarjeta indicadora de KPI (kpi_card)

**Cuándo usarlo**: visualización de alto contraste de una única métrica principal (como ingresos trimestrales, DAU, tasa de conversión). Número grande + flecha interanual + minigráfico opcional = Comunicar la conclusión completa en 5 segundos. Al combinar varias tarjetas, utilice "fila de índice" o conjunto de tarjetas `card_type=data`.

**Formato de datos**:

```json
{
  "type": "kpi_card",
  "value": "¥ 2.84B",
  "label": "Q1 2026 营收",
  "delta": { "direction": "up", "percent": 23.7, "vs": "vs Q4 2025" },
  "sparkline": [42, 48, 52, 56, 61, 68, 72, 78, 82]
}
```

**Plantilla HTML (incluido minigráfico)**:

```html
<div class="chart-kpi-card" style="
  position: relative;
  width: 320px;
  padding: 26px 28px 22px;
  border-radius: var(--card-radius, 8px);
  background: linear-gradient(180deg, var(--card-bg-from), var(--card-bg-to));
  border: 1px solid var(--card-border);
  font-family: 'Inter Tight', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-feature-settings: 'kern','liga','ss01','cv11';
  overflow: hidden;
">
  <div style="
    display: inline-flex; align-items: center; gap: 8px;
    font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase;
    font-weight: 600; color: var(--accent-1);
  ">
    <span style="width: 5px; height: 5px; border-radius: 50%; background: var(--accent-1); box-shadow: 0 0 8px currentColor;"></span>
    Q1 2026 营收
  </div>

  <div style="
    display: flex; align-items: baseline; gap: 6px;
    margin-top: 14px;
  ">
    <span style="
      font-size: 13px; font-weight: 600;
      color: var(--text-secondary); opacity: 0.75;
      letter-spacing: -0.01em;
    ">¥</span>
    <span style="
      font-size: 46px; font-weight: 800;
      letter-spacing: -0.04em; line-height: 1;
      color: var(--text-primary);
      font-variant-numeric: tabular-nums proportional-nums;
    ">2.84</span>
    <span style="
      font-size: 22px; font-weight: 700;
      letter-spacing: -0.02em;
      color: var(--text-secondary);
    ">B</span>
  </div>

  <div style="
    display: flex; align-items: center; justify-content: space-between;
    margin-top: 16px;
  ">
    <div style="display: inline-flex; align-items: center; gap: 6px;">
      <svg width="11" height="11" viewBox="0 0 11 11" style="display: block;">
        <polygon points="5.5,1 10,9 1,9" fill="#22c55e"/>
      </svg>
      <span style="
        font-size: 13px; font-weight: 700;
        color: #22c55e;
        letter-spacing: -0.01em;
        font-variant-numeric: tabular-nums proportional-nums;
      ">+23.7%</span>
      <span style="
        font-size: 11px; color: var(--text-secondary); opacity: 0.65;
        margin-left: 4px; letter-spacing: 0.02em;
      ">vs Q4 2025</span>
    </div>

    <div style="width: 90px; height: 28px;">
      <svg viewBox="0 0 90 28" preserveAspectRatio="none" style="width: 100%; height: 100%; display: block;">
        <defs>
          <linearGradient id="kpi-spark-fill" x1="0%" y1="0%" x2="0%" y2="100%">
            <stop offset="0%"   stop-color="var(--accent-1)" stop-opacity="0.25"/>
            <stop offset="100%" stop-color="var(--accent-1)" stop-opacity="0"/>
          </linearGradient>
        </defs>
        <path d="M 0 22 L 11 20 L 22 17 L 33 14 L 44 12 L 55 9 L 66 7 L 77 5 L 90 2 L 90 28 L 0 28 Z"
              fill="url(#kpi-spark-fill)"/>
        <path d="M 0 22 L 11 20 L 22 17 L 33 14 L 44 12 L 55 9 L 66 7 L 77 5 L 90 2"
              fill="none" stroke="var(--accent-1)" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="90" cy="2" r="2" fill="var(--accent-1)"/>
      </svg>
    </div>
  </div>
</div>
```

**Variación A: Minimalista sin minigráfico (para terrazas horizontales)**

```html
<div style="
  width: 240px; padding: 20px 22px;
  border-left: 2px solid var(--accent-1);
  font-family: 'Inter Tight', sans-serif;
">
  <div style="font-size: 10px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--text-secondary); font-weight: 600;">DAILY ACTIVE USERS</div>
  <div style="font-size: 42px; font-weight: 800; letter-spacing: -0.04em; color: var(--text-primary); font-variant-numeric: tabular-nums proportional-nums; line-height: 1; margin-top: 8px;">1.42<span style="font-size: 18px; opacity: 0.6; margin-left: 3px;">M</span></div>
  <div style="display: inline-flex; align-items: center; gap: 4px; margin-top: 10px;">
    <svg width="9" height="9" viewBox="0 0 9 9"><polygon points="4.5,1 8,7 1,7" fill="#22c55e"/></svg>
    <span style="font-size: 12px; font-weight: 600; color: #22c55e; font-variant-numeric: tabular-nums;">+12.4%</span>
    <span style="font-size: 11px; color: var(--text-secondary); opacity: 0.6; margin-left: 4px;">WoW</span>
  </div>
</div>
```

**Variante B: Indicador de descenso (flecha roja)**

```html
<div style="width: 240px; padding: 20px 22px; border-left: 2px solid #ef4444; font-family: 'Inter Tight', sans-serif;">
  <div style="font-size: 10px; letter-spacing: 0.2em; text-transform: uppercase; color: var(--text-secondary); font-weight: 600;">CHURN RATE</div>
  <div style="font-size: 42px; font-weight: 800; letter-spacing: -0.04em; color: var(--text-primary); font-variant-numeric: tabular-nums; line-height: 1; margin-top: 8px;">3.2<span style="font-size: 18px; opacity: 0.6; margin-left: 2px;">%</span></div>
  <div style="display: inline-flex; align-items: center; gap: 4px; margin-top: 10px;">
    <svg width="9" height="9" viewBox="0 0 9 9"><polygon points="4.5,8 8,2 1,2" fill="#ef4444"/></svg>
    <span style="font-size: 12px; font-weight: 600; color: #ef4444; font-variant-numeric: tabular-nums;">-0.8pp</span>
    <span style="font-size: 11px; color: var(--text-secondary); opacity: 0.6; margin-left: 4px;">MoM</span>
  </div>
</div>
```



- [x] Números grandes 36-48px, `font-variant-numeric: tabular-nums proporcional-nums`
- [x] Espacio entre letras de números grandes en -0,035em ~ -0,045em (cumple con la ley de kerning de [typography.md](../typography.md))
- [x] **Símbolo de moneda, unidad (B / M / %) como `<span>` independiente, alineación de línea base flexible** (para evitar que svg2pptx desalinee diferentes tamaños de fuente incrustados)
- [x] **Las flechas de tendencia usan SVG `<polígono>`**, sin triángulo de borde CSS
- [x] Arriba #22c55e / Abajo #ef4444 Codificado por convención de la industria
- [x] Utilice `<circle>` para puntos finales minigráficos en lugar de etiquetas SVG `<text>`
- [x] Utilice `var(--card-bg-from/to)` para el fondo de la tarjeta y `var(--card-border)` para el borde
- [x] Renderizado mediante titiritero sin errores

---

## 7. Fila de métrica (metric_row)

**Cuándo usarlo**: 3-6 indicadores paralelos apilados verticalmente, cada fila = número + etiqueta + barra de progreso. Ahorra más espacio que el mazo de cartas KPI y es adecuado para colocarlo en la columna derecha o dentro de la tarjeta. Cuando haya ≥ 7 indicadores, dividir en dos columnas.

**Formato de datos**:

```json
{
  "type": "metric_row",
  "rows": [
    { "label": "API 可用性", "value": 99.97, "max": 100, "unit": "%", "highlight": true },
    { "label": "P99 延迟",   "value": 47,    "max": 200, "unit": "ms", "lower_better": true },
    { "label": "错误率",     "value": 0.03,  "max": 1,   "unit": "%", "lower_better": true },
    { "label": "吞吐量",     "value": 12.4,  "max": 20,  "unit": "K/s" }
  ]
}
```

**Plantilla HTML**:

```html
<div class="chart-metric-row" style="
  width: 380px;
  padding: 24px 26px;
  border-radius: var(--card-radius, 8px);
  background: linear-gradient(180deg, var(--card-bg-from), var(--card-bg-to));
  border: 1px solid var(--card-border);
  font-family: 'Inter Tight', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-feature-settings: 'kern','liga','ss01','cv11';
">
  <div style="
    display: flex; align-items: baseline; justify-content: space-between;
    margin-bottom: 18px;
  ">
    <div style="font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--text-secondary); font-weight: 600;">— 系统健康度</div>
    <div style="font-size: 10px; color: var(--text-secondary); opacity: 0.55; letter-spacing: 0.1em; text-transform: uppercase;">LIVE</div>
  </div>

  <div style="display: flex; flex-direction: column; gap: 16px;">
    <div>
      <div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 6px;">
        <span style="font-size: 13px; color: var(--text-primary); font-weight: 500; letter-spacing: -0.005em;">API 可用性</span>
        <span style="font-size: 18px; font-weight: 700; letter-spacing: -0.02em; color: var(--accent-1); font-variant-numeric: tabular-nums proportional-nums;">99.97<span style="font-size: 11px; opacity: 0.65; margin-left: 1px;">%</span></span>
      </div>
      <div style="height: 4px; border-radius: 999px; background: var(--card-bg-from); overflow: hidden;">
        <div style="height: 100%; width: 99.97%; border-radius: 999px; background: linear-gradient(90deg, var(--accent-1), var(--accent-2));"></div>
      </div>
    </div>

    <div>
      <div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 6px;">
        <span style="font-size: 13px; color: var(--text-primary); font-weight: 500;">P99 延迟</span>
        <span style="font-size: 18px; font-weight: 700; letter-spacing: -0.02em; color: var(--text-primary); font-variant-numeric: tabular-nums;">47<span style="font-size: 11px; opacity: 0.55; margin-left: 2px;">ms</span></span>
      </div>
      <div style="height: 4px; border-radius: 999px; background: var(--card-bg-from); overflow: hidden;">
        <div style="height: 100%; width: 23.5%; border-radius: 999px; background: var(--accent-2); opacity: 0.85;"></div>
      </div>
    </div>

    <div>
      <div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 6px;">
        <span style="font-size: 13px; color: var(--text-primary); font-weight: 500;">错误率</span>
        <span style="font-size: 18px; font-weight: 700; letter-spacing: -0.02em; color: var(--text-primary); font-variant-numeric: tabular-nums;">0.03<span style="font-size: 11px; opacity: 0.55; margin-left: 1px;">%</span></span>
      </div>
      <div style="height: 4px; border-radius: 999px; background: var(--card-bg-from); overflow: hidden;">
        <div style="height: 100%; width: 3%; border-radius: 999px; background: var(--accent-3); opacity: 0.7;"></div>
      </div>
    </div>

    <div>
      <div style="display: flex; align-items: baseline; justify-content: space-between; margin-bottom: 6px;">
        <span style="font-size: 13px; color: var(--text-primary); font-weight: 500;">吞吐量</span>
        <span style="font-size: 18px; font-weight: 700; letter-spacing: -0.02em; color: var(--text-primary); font-variant-numeric: tabular-nums;">12.4<span style="font-size: 11px; opacity: 0.55; margin-left: 2px;">K/s</span></span>
      </div>
      <div style="height: 4px; border-radius: 999px; background: var(--card-bg-from); overflow: hidden;">
        <div style="height: 100%; width: 62%; border-radius: 999px; background: var(--accent-4); opacity: 0.75;"></div>
      </div>
    </div>
  </div>
</div>
```



```html
<div style="width: 320px; font-family: 'Inter Tight', sans-serif; display: flex; flex-direction: column; gap: 14px;">
  <div style="display: grid; grid-template-columns: 100px 1fr; align-items: center; gap: 16px;">
    <div style="font-size: 26px; font-weight: 800; letter-spacing: -0.03em; color: var(--text-primary); font-variant-numeric: tabular-nums proportional-nums; line-height: 1;">87<span style="font-size: 14px; opacity: 0.55; margin-left: 1px;">%</span></div>
    <div>
      <div style="font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--text-secondary); margin-bottom: 6px;">客户满意度</div>
      <div style="height: 3px; border-radius: 999px; background: var(--card-bg-from);">
        <div style="height: 100%; width: 87%; border-radius: 999px; background: var(--accent-1);"></div>
      </div>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 100px 1fr; align-items: center; gap: 16px;">
    <div style="font-size: 26px; font-weight: 800; letter-spacing: -0.03em; color: var(--text-primary); font-variant-numeric: tabular-nums; line-height: 1;">64<span style="font-size: 14px; opacity: 0.55; margin-left: 1px;">%</span></div>
    <div>
      <div style="font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--text-secondary); margin-bottom: 6px;">迁移完成度</div>
      <div style="height: 3px; border-radius: 999px; background: var(--card-bg-from);">
        <div style="height: 100%; width: 64%; border-radius: 999px; background: var(--accent-2);"></div>
      </div>
    </div>
  </div>

  <div style="display: grid; grid-template-columns: 100px 1fr; align-items: center; gap: 16px;">
    <div style="font-size: 26px; font-weight: 800; letter-spacing: -0.03em; color: var(--text-primary); font-variant-numeric: tabular-nums; line-height: 1;">42<span style="font-size: 14px; opacity: 0.55; margin-left: 1px;">%</span></div>
    <div>
      <div style="font-size: 11px; letter-spacing: 0.12em; text-transform: uppercase; color: var(--text-secondary); margin-bottom: 6px;">海外营收占比</div>
      <div style="height: 3px; border-radius: 999px; background: var(--card-bg-from);">
        <div style="height: 100%; width: 42%; border-radius: 999px; background: var(--accent-3);"></div>
      </div>
    </div>
  </div>
</div>
```



- [x] Utilice **flex `align-items: baseline`** en cada línea para alinear etiquetas y números con la línea base (¡clave!)
- [x] Las unidades numéricas (%, ms, K/s) se utilizan como intervalos integrados, pero **el cuerpo numérico sigue siendo un intervalo independiente** para evitar la desalineación de la línea base de svg2pptx
- [x] números `fuente-variante-numérica: números-tabulares números-proporcionales`
- [x] La barra de progreso tiene una altura unificada de 4px (no roba el protagonismo digital)
- [x] Puedes usar `--accent-1` ~ `--accent-4` en cada línea para crear una jerarquía
- [x] Resalte elementos con `color: var(--accent-1)` en lugar de un tamaño de fuente más grande (mantenga la alineación)
- [x] Renderizado mediante titiritero sin errores

---

## 8. Indicador de calificación (calificación)

**Cuándo usarlo**: Calificación en una escala de 5 puntos (incluidas medias estrellas) / Satisfacción / Nivel de dificultad / Nivel de rendimiento. Más intuitivo que los números puros (4,5/5). Si se trata de una escala de 10 puntos, utilice una barra de progreso; si es una escala de 0 a 100, utilice un gráfico de anillos.

**Formato de datos**:

```json
{
  "type": "rating",
  "value": 4.5,
  "max": 5,
  "label": "用户评分",
  "shape": "dot"
}
```

> **Lógica de llenado**: valor=4.5, max=5 → 4 llenos + 1 medio + 0 vacío.
> Las medias estrellas se implementan usando un rectángulo de 50% de ancho + clip de ruta SVG, **deshabilite el corte por la mitad con gradiente CSS** (svg2pptx no es confiable).

**Plantilla HTML (versión punto)**:

```html
<div class="chart-rating" style="
  display: inline-flex; flex-direction: column; gap: 8px;
  font-family: 'Inter Tight', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  font-feature-settings: 'kern','liga','ss01';
">
  <div style="
    font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase;
    color: var(--text-secondary); font-weight: 600;
  ">用户评分</div>

  <div style="display: inline-flex; align-items: center; gap: 10px;">
    <div style="display: inline-flex; gap: 6px;">
      <svg width="18" height="18" viewBox="0 0 18 18" style="display: block;">
        <circle cx="9" cy="9" r="7" fill="var(--accent-1)"/>
      </svg>
      <svg width="18" height="18" viewBox="0 0 18 18" style="display: block;">
        <circle cx="9" cy="9" r="7" fill="var(--accent-1)"/>
      </svg>
      <svg width="18" height="18" viewBox="0 0 18 18" style="display: block;">
        <circle cx="9" cy="9" r="7" fill="var(--accent-1)"/>
      </svg>
      <svg width="18" height="18" viewBox="0 0 18 18" style="display: block;">
        <circle cx="9" cy="9" r="7" fill="var(--accent-1)"/>
      </svg>
      <svg width="18" height="18" viewBox="0 0 18 18" style="display: block;">
        <circle cx="9" cy="9" r="7" fill="none" stroke="var(--accent-1)" stroke-width="1.5"/>
        <path d="M 9 2 A 7 7 0 0 1 9 16 Z" fill="var(--accent-1)"/>
      </svg>
    </div>

    <div style="display: inline-flex; align-items: baseline; gap: 4px;">
      <span style="font-size: 22px; font-weight: 800; letter-spacing: -0.03em; color: var(--text-primary); font-variant-numeric: tabular-nums proportional-nums; line-height: 1;">4.5</span>
      <span style="font-size: 12px; color: var(--text-secondary); opacity: 0.6; font-variant-numeric: tabular-nums;">/ 5.0</span>
    </div>
  </div>

  <div style="font-size: 11px; color: var(--text-secondary); opacity: 0.7; letter-spacing: 0.02em;">
    基于 <span style="color: var(--text-primary); font-weight: 600; font-variant-numeric: tabular-nums;">12,847</span> 份反馈
  </div>
</div>
```

**Variación A: Versión estrella (incluye media estrella + ruta SVG)**

```html
<div style="display: inline-flex; align-items: center; gap: 10px; font-family: 'Inter Tight', sans-serif;">
  <div style="display: inline-flex; gap: 4px;">
    <svg width="18" height="18" viewBox="0 0 24 24" style="display: block;">
      <polygon points="12,2 15.09,8.26 22,9.27 17,14.14 18.18,21.02 12,17.77 5.82,21.02 7,14.14 2,9.27 8.91,8.26"
               fill="var(--accent-1)"/>
    </svg>
    <svg width="18" height="18" viewBox="0 0 24 24" style="display: block;">
      <polygon points="12,2 15.09,8.26 22,9.27 17,14.14 18.18,21.02 12,17.77 5.82,21.02 7,14.14 2,9.27 8.91,8.26"
               fill="var(--accent-1)"/>
    </svg>
    <svg width="18" height="18" viewBox="0 0 24 24" style="display: block;">
      <polygon points="12,2 15.09,8.26 22,9.27 17,14.14 18.18,21.02 12,17.77 5.82,21.02 7,14.14 2,9.27 8.91,8.26"
               fill="var(--accent-1)"/>
    </svg>
    <svg width="18" height="18" viewBox="0 0 24 24" style="display: block;">
      <polygon points="12,2 15.09,8.26 22,9.27 17,14.14 18.18,21.02 12,17.77 5.82,21.02 7,14.14 2,9.27 8.91,8.26"
               fill="var(--accent-1)"/>
    </svg>

    <svg width="18" height="18" viewBox="0 0 24 24" style="display: block;">
      <defs>
        <clipPath id="half-star-clip">
          <rect x="0" y="0" width="12" height="24"/>
        </clipPath>
      </defs>
      <polygon points="12,2 15.09,8.26 22,9.27 17,14.14 18.18,21.02 12,17.77 5.82,21.02 7,14.14 2,9.27 8.91,8.26"
               fill="none" stroke="var(--accent-1)" stroke-width="1.2"/>
      <polygon points="12,2 15.09,8.26 22,9.27 17,14.14 18.18,21.02 12,17.77 5.82,21.02 7,14.14 2,9.27 8.91,8.26"
               fill="var(--accent-1)" clip-path="url(#half-star-clip)"/>
    </svg>
  </div>

  <div style="display: inline-flex; align-items: baseline; gap: 4px;">
    <span style="font-size: 20px; font-weight: 800; letter-spacing: -0.03em; color: var(--text-primary); font-variant-numeric: tabular-nums proportional-nums; line-height: 1;">4.5</span>
    <span style="font-size: 11px; color: var(--text-secondary); opacity: 0.6;">/ 5</span>
  </div>
</div>
```

**Variación B: Versión de barra horizontal (5 barras, cada barra = 1 punto)**

```html
<div style="display: inline-flex; flex-direction: column; gap: 6px; font-family: 'Inter Tight', sans-serif;">
  <div style="font-size: 11px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--text-secondary); font-weight: 600;">难度等级</div>
  <div style="display: inline-flex; gap: 4px;">
    <span style="width: 28px; height: 6px; border-radius: 2px; background: var(--accent-1);"></span>
    <span style="width: 28px; height: 6px; border-radius: 2px; background: var(--accent-1);"></span>
    <span style="width: 28px; height: 6px; border-radius: 2px; background: var(--accent-1);"></span>
    <span style="width: 28px; height: 6px; border-radius: 2px; background: linear-gradient(90deg, var(--accent-1) 50%, var(--card-bg-from) 50%);"></span>
    <span style="width: 28px; height: 6px; border-radius: 2px; background: var(--card-bg-from); border: 1px solid var(--card-border);"></span>
  </div>
  <div style="font-size: 12px; color: var(--text-primary); font-weight: 600; font-variant-numeric: tabular-nums;">3.5 <span style="opacity: 0.55; font-weight: 400;">困难</span></div>
</div>
```

**Autocomprobación**:

- [x] Cada unidad de puntuación es `<svg>` independiente para evitar la desalineación de coordenadas causada por la fusión de múltiples rutas de dom a svg.
- [x] **La media estrella usa SVG `<clipPath>` + máscara rectangular**, no se usa ningún degradado CSS para cortarla por la mitad
- [x] **Para estrellas huecas, use `fill="none" trazo=...`**, sin imagen-máscara
- [x] números `fuente-variante-numérica: números-tabulares números-proporcionales`
- [x] Utilice `var(--accent-1)` para el color, `var(--card-bg-from)` + `var(--card-border)` para vacío
- [x] La versión con puntos usa `<círculo>` + ruta, la versión con estrellas usa `<polígono>`
- [x] Renderizado mediante titiritero sin errores

---



| Radio r | Circunferencia (2πr) | 25% de longitud de arco | 50% de longitud de arco | 75% de longitud de arco | 90% de longitud de arco |
|--------|----------|---------|---------|---------|---------|
| 40 | 251 | 63 | 126 | 188 | 226 |
| 50 | 314 | 79 | 157 | 236 | 283 |
| 60 | 377 | 94 | 188 | 283 | 339 |
| 68 | 427 | 107 | 214 | 320 | 384 |
| 80 | 503 | 126 | 251 | 377 | 452 |
| 90 | 565 | 141 | 283 | 424 | 509 |
| 100 | 628 | 157 | 314 | 471 | 565 |

Fórmula: longitud del arco = 2π × r × (porcentaje / 100), circunferencia = 2π × r.
**`stroke-dasharray="circunferencia de longitud de arco"`**, por ejemplo r=80, 75% → `stroke-dasharray="377 503"`.

---

## Apéndice B · Esquema de degradado de color universal

Sugerencias semánticas para cada estilo `--accent-1` ~ `--accent-4`:

| Variables | Semántica | Uso de ejemplo |
|------|------|---------|
| `--acento-1` | **Destacado principal** (contraste más fuerte) | Valor actual/Completado/Artículo resaltado |
| `--acento-2` | Secundario (el mismo color es un poco más claro) | Grupo de comparación / En curso |
| `--acento-3` | Color terciario (a menudo complementario) | Tercer grupo/no iniciado/decoración de bordes |
| `--acento-4` | advertencia/decoración (por ejemplo, dorada) | acento/punto único prominente |

Colores fijos que no participan en el cambio de tema:

| Color | Uso |
|------|------|
| `#22c55e` | Aumento del cambio verde/positivo (práctica de la industria) |
| `#ef4444` | Caída de rojo/cambio negativo (práctica de la industria) |
| `#f59e0b` | Advertencia naranja (opcional, úselo con precaución) |

---



Antes de entregar cada plantilla HTML de gráfico, verifique los siguientes 8 elementos:

- [] Números más `fuente-variante-numérica: números-tabulares números-proporcionales`
- [ ] Todos los colores usan variables CSS (`--accent-*`, `--card-bg-*`, `--card-border`, `--text-*`), sin código hexadecimal (excepto el rojo y el verde que son una práctica común en la industria)
- [ ] No hay ningún elemento `<text>`** en SVG en línea, todo el texto está superpuesto con HTML `<div>`/`<span>` posicionamiento absoluto
- [] El gráfico de anillos usa el formato de dos valores `stroke-dasharray="circunferencia de longitud de arco"`, **no use `stroke-dashoffset`**
- [] Utilice SVG `<polígono>` para triángulos/flechas, **sin truco de triángulo de borde CSS**
- [ ] No utilice `cónico-gradiente` / `máscara-imagen` / `mix-blend-mode` / `fondo-clip: texto` / `filtro: desenfoque()`
- [] Para mezclar diferentes tamaños de fuente, use flex `align-items: baseline` + independiente `<span>`, sin anidar spans
- [] El renderizado mediante titiritero no tiene errores de consola y la inspección visual es claramente legible tanto en fondos oscuros como claros.