# Gráficos de Visualización de Datos -- Munición Visual para Presentaciones PPTX

> Material no predeterminado. Manual de gráficos solo para humanos (human-only chart workbook).
>
> Este archivo no se inyecta como material de gráficos en la cadena principal de runtime por defecto, y no entra en la cadena de inyección del prompt predeterminado ni en la cadena de carga automática de recursos. Conserva los esqueletos, demos y contenido explicativo, y se consulta a demanda solo para depuración manual o referencia dirigida.

> Los datos son el arma más persuasiva en un discurso. Pero un número grande y aislado es solo "información para recordar", mientras que un número + visualización es "un insight comprensible en un segundo".
>
> **Regla de oro**: Cada tarjeta de datos (`data`) debe ir acompañada de al menos un elemento visual. No coloques simplemente un número gigante.

## Guía de Selección (Características del dato -> Munición visual)

| Características del Dato | Gráfico Recomendado | Alma Visual | Archivo |
|---------|---------|---------|------|
| Porcentaje/Progreso | Barra de progreso | Claridad instantánea de "hasta dónde hemos llegado" | `progress-bar.md` |
| Porcentaje/Progreso | Gráfico de anillo | La plenitud del arco transmite intuitivamente la "proporción" | `ring.md` |
| Comparación binaria | Barras de comparación | Percepción inmediata de diferencias de altura | `comparison-bar.md` |
| Tendencia temporal | Minigráfico de líneas (sparkline) | Una sola línea cuenta toda la historia | `sparkline.md` |
| Proporción intuitiva | Gráfico de waffle (matriz de puntos) | "¿Cuántos de los 100 cuadrados están iluminados?" | `waffle.md` |
| KPI central | Tarjeta de métricas KPI | Número grande + Flecha de tendencia = La combinación más impactante | `kpi.md` |
| Múltiples indicadores alineados | Fila de métricas | Flujo de información horizontal, ideal para escaneo rápido | `metric-row.md` |
| Calificación/Puntuación | Indicador de puntuación | Intuición de estrellas/puntajes | `rating.md` |
| Comparación multidimensional | Gráfico de radar | La "plenitud" del polígono transmite fuerza general | `radar.md` |
| Proporción multicategoría | Gráfico de barras apiladas | "Análisis de componentes" dentro de una sola barra | `stacked-bar.md` |
| Proporción jerárquica | Treemap (Mapa de árbol) | Tamaño del área = Importancia | `treemap.md` |
| Historia/Hitos | Línea de tiempo (Timeline) | La trayectoria del flujo de eventos | `timeline.md` |
| Flujo de conversión | Gráfico de embudo | "Visualización de la pérdida" estrechándose capa por capa | `funnel.md` |

## Reglas Dinámicas

### Los gráficos no son islas
- El gráfico debe formar una **fuerte combinación narrativa** con la interpretación de texto arriba o al lado de él. El número grande es "qué", el gráfico es "cómo" y la interpretación es "qué significa".
- Los colores de los gráficos deben usar variables CSS (`var(--accent-1)`, etc.), nunca codifiques colores absolutos (para mantener el estilo uniforme).

### El peso visual del gráfico debe subordinarse a la estructura general
- En las tarjetas con `card_style` tipo `accent`, usa tonos claros/blancos para el gráfico (porque el fondo es oscuro).
- En las tarjetas con `card_style` tipo `transparent`, puedes usar colores de acento más fuertes (porque el fondo está vacío).
- Los contenedores de gráficos deben tener un `height` claro (para evitar el desbordamiento), pero este valor de altura debe ajustarse de manera flexible según el espacio de la tarjeta donde se encuentre, en lugar de ser siempre de 80px.

### Qué proporcionan los archivos de gráficos
- **Modelos de esqueleto estructural** (ring/kpi/sparkline/comparison-bar/waffle/metric-row/rating/progress-bar): Proporcionan código de referencia estructural HTML/SVG (porque las fórmulas matemáticas SVG deben ser precisas), pero las dimensiones, datos y colores en ellos son **ejemplos de marcadores de posición (placeholders)**. Deben ser readaptados de acuerdo a los datos reales.
- **Modelos de principios de diseño** (funnel/stacked-bar/timeline/treemap/radar): Solo describen los principios estructurales y directrices dinámicas, no proporcionan código. El LLM los construye de manera autónoma basándose en los principios.
- Todos los gráficos vienen con **descripción del alma visual** y **directrices dinámicas**, guiando al LLM a comprender el papel narrativo de cada tipo de gráfico.
- Absolutamente nunca copies y pegues los datos de demostración tal cual.
