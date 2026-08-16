# Índice del Sistema de Gráficos (18 tipos / 3 niveles)

> Todos los gráficos se implementan puramente con HTML/CSS/SVG, **evita introducir runtimes como ECharts** (peso y dependencias innecesarias para una slide estática). Evita escribir `<text>` dentro de SVG — las etiquetas como divs HTML superpuestos renderizan más consistente entre navegadores. Efectos como `conic-gradient`/`mask-image`/`filter:blur()` están permitidos (la exportación a PPTX es por captura de pantalla, no por conversión SVG — ver `references/playbooks/bespoke-slide-recipe.md`).

---

## 1. Panorama de los 18 Tipos de Gráficos

| # | Gráfico | Nivel | Archivo | Cuándo usar |
|---|------|------|------|-------|
| 1 | Barra de Progreso (Progress Bar) | Básico | [basic.md](basic.md) | Porcentaje único / Grado de finalización |
| 2 | Barra de Comparación (Compare Bar) | Básico | [basic.md](basic.md) | Comparación de dos elementos |
| 3 | Gráfico de Anillo (Ring Chart) | Básico | [basic.md](basic.md) | Porcentaje + KPI central |
| 4 | Minigráfico de Línea (Sparkline) | Básico | [basic.md](basic.md) | Dirección de tendencia |
| 5 | Gráfico de Waffle (Waffle Chart) | Básico | [basic.md](basic.md) | Proporción intuitiva (10×10) |
| 6 | Tarjeta de Indicador KPI | Básico | [basic.md](basic.md) | Número grande + flecha de tendencia |
| 7 | Fila de Métricas (Metric Row) | Básico | [basic.md](basic.md) | Apilamiento vertical de múltiples indicadores |
| 8 | Indicador de Puntuación (Rating) | Básico | [basic.md](basic.md) | Sistema de 5 puntos / Medias estrellas |
| 9 | Gráfico de Radar (Radar) | Avanzado | [advanced.md](advanced.md) | Comparación multidimensional (5-8 dimensiones) |
| 10 | Línea de Tiempo (Timeline) | Avanzado | [advanced.md](advanced.md) | Historia / Hoja de ruta / Flujo |
| 11 | Gráfico de Embudo (Funnel) | Avanzado | [advanced.md](advanced.md) | Tasa de conversión / Análisis de pérdida |
| 12 | Indicador de Tablero (Gauge) | Avanzado | [advanced.md](advanced.md) | Calificación de KPI / Salud |
| 13 | Barras Agrupadas (Grouped Bar) | Avanzado | [advanced.md](advanced.md) | Múltiples categorías × múltiples grupos de comparación |
| 14 | Mapa Geográfico Simple (Simple Map) | Avanzado | [advanced.md](advanced.md) | Puntos de ciudad / Distribución regional |
| 15 | Mapa Mundial de Coropletas (Choropleth) | Complejo | [complex.md](complex.md) | Visualización de datos globales |
| 16 | Red de Relaciones (Network) | Complejo | [complex.md](complex.md) | Nodos + conexiones (dirigidas por fuerza estática) |
| 17 | Diagrama de Sankey (Sankey) | Complejo | [complex.md](complex.md) | Tráfico / Rutas de conversión |
| 18 | Calendario de Mapa de Calor (Heatmap Calendar) | Complejo | [complex.md](complex.md) | Densidad de datos de 365 días |

---

## 2. Matriz de Decisión

Selección rápida de gráficos por características de datos:

| Tipo de Dato | Gráfico Recomendado | Alternativa |
|---------|---------|------|
| Porcentaje único | Barra de progreso / Gráfico de anillo | Tarjeta KPI |
| Comparación binaria | Barra de comparación | Barras agrupadas |
| 3-8 indicadores paralelos | Grupo de tarjetas KPI / Fila de métricas | Gráfico de radar |
| Evaluación multidimensional | Gráfico de radar | Indicador de puntuación |
| Tendencia temporal | Minigráfico de línea | Línea de tiempo |
| Proporción intuitiva | Gráfico de waffle | Gráfico de anillo |
| Embudo de conversión | Gráfico de embudo | Diagrama de Sankey |
| Calificación KPI (ej. salud) | Indicador de tablero | Indicador de puntuación |
| Comparación multicategoría (ej. interanual) | Barras agrupadas | — |
| Distribución geográfica (China/Mundo) | Mapa simple / Mapa mundial | — |
| Red de relaciones (ej. organigrama) | Red de relaciones | — |
| Análisis de tráfico complejo | Diagrama de Sankey | Gráfico de embudo |
| Datos continuos de fechas | Calendario de mapa de calor | Minigráfico de línea |

---

## 3. Especificaciones Generales de Gráficos

### 3.1 Formato de Datos

Todas las plantillas HTML de gráficos aceptan datos en línea simples, sin dependencias de tiempo de ejecución. Por ejemplo:

```html
<!-- Barra de Progreso -->
<div class="chart-progress" data-value="87" data-label="Completado">
  <div class="bar"><div class="fill" style="width:87%"></div></div>
  <span class="value">87%</span>
</div>
```

### 3.2 Mapeo de Colores

Todos los gráficos deben usar variables CSS (`--accent-1`, `--accent-2`, etc.), no codifiques colores fijos. De esta manera, los 26 estilos se adaptan automáticamente.

### 3.3 Formato de Números

Todos los números de datos deben tener `font-variant-numeric: tabular-nums proportional-nums`.

### 3.4 Prohibición de `<text>` en SVG

Todas las anotaciones de texto (etiquetas de datos, eje x, leyendas, números centrales) se superponen utilizando un posicionamiento absoluto con HTML `<div>` / `<span>` sobre el SVG.

### 3.5 Compatibilidad sin ECharts

Estrategia de implementación para gráficos complejos (Mapa mundial, Red, Sankey, Mapa de calor):
- **No introduzcas el tiempo de ejecución de ECharts**
- Usa datos puros de ruta SVG (`path`) + cálculo estático
- Proporciona scripts auxiliares en Python cuando sea necesario (como `scripts/world_map_paths.py`) para generar rutas SVG desde GeoJSON.

### 3.6 Adaptación de Estilo

Cada gráfico debe adaptarse automáticamente a cada estilo:
- Estilo oscuro: usa `--accent-1` para el color de resalte principal, `--card-border` para líneas
- Estilo claro: usa `--accent-1` para el contorno, `--card-bg-from` para el relleno
- Estilo cultural (royal_red, etc.): tono dual con `--accent-1` (dorado) + `--accent-3` (rojo bermellón)

### 3.7 Lista de Verificación (Checklist)

Autocontrol para cada plantilla HTML de gráfico:

- [ ] Usa variables CSS, sin colores fijos codificados (hardcoded)
- [ ] Números usando `tabular-nums`
- [ ] Sin etiqueta `<text>` dentro de los SVG
- [ ] Sin uso de `conic-gradient` (el gráfico de anillo debe usar `circle` SVG + `dasharray`)
- [ ] Sin uso de `mask-image` / `mix-blend-mode`
- [ ] Al menos un dato de ejemplo presente
