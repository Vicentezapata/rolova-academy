# Biblioteca de Componentes de Área -- Lenguaje de Diseño de Presentaciones PPTX

> Los componentes compuestos no son "Componentes de UI web", sino **vehículos visuales de la narrativa de información**. Cada componente es una forma única de organizar la información, que conlleva un ritmo de presentación específico y la emoción de la audiencia.

## Tabla General de Componentes

| card_type | Rol Narrativo | Archivo |
|----------|---------|------|
| `timeline` | **El Río del Tiempo** -- Da sensación de fluidez a la historia/progreso | `timeline.md` |
| `diagram` | **El Mapa Estelar Estructural** -- Hace tangibles las relaciones abstractas | `diagram.md` |
| `quote` | **El Ancla del Alma** -- Corona el argumento con una voz autorizada | `quote.md` |
| `comparison` | **La Arena de Choque** -- Crea tensión dramática entre opuestos | `comparison.md` |
| `people` | **El Poder de los Rostros** -- Acerca a la audiencia a través de las personas | `people.md` |
| `image_hero` | **Inmersión Visual** -- Crea una onda de choque emocional con imágenes | `image-hero.md` |
| `matrix_chart` | **Posicionamiento de Cuadrantes** -- Revela la posición estratégica usando coordenadas 2D | `matrix-chart.md` |

## Guía de Selección

| Características del Contenido | Componente Recomendado | Por qué |
|---------|---------|-------|
| Eventos cronológicos (4-8) | **timeline** | La línea de tiempo hace que la audiencia sienta el "impulso del progreso" |
| Arquitectura/Flujo/Relaciones Multi-nivel | **diagram** | Los diagramas hacen que la audiencia pase de "escuchar una descripción" a "ver el panorama general" |
| Citas Autorizadas/Puntos de Vista Disruptivos | **quote** | Las citas doradas son el arma para "silenciar la sala por un segundo" en una presentación |
| A vs B Toma de Decisiones Comparativa | **comparison** | La comparación lado a lado permite que la audiencia "saque sus propias conclusiones" en lugar de aceptar pasivamente |
| Exhibición de Equipo/Personas | **people** | Los rostros son el canal más rápido para generar confianza |
| Impacto Emocional/Creación de Escenarios | **image_hero** | Una buena imagen vale más que mil palabras |
| Análisis de Posicionamiento Estratégico 2x2 | **matrix_chart** | Un gráfico de cuadrantes es la herramienta más intuitiva para decisiones de negocio |

## Principios de Combinación Dinámica

- Los componentes compuestos vienen con su propio esqueleto visual, se recomienda el estilo `transparent` en `card_style` -- envolverlos en cajas es redundante
- Cuando los componentes compuestos y las tarjetas básicas coexisten en una página, deja que el componente compuesto ocupe varias columnas para ser el protagonista de la imagen, relegando las tarjetas básicas a un papel secundario
- No debe haber más de 1 componente compuesto que cruce columnas y filas en la misma página, de lo contrario, dos "protagonistas" se robarán el espectáculo
- Cuando el componente compuesto está expuesto en la imagen con `transparent`, su tensión visual proviene de la estructura del propio componente (ejes, nodos, paneles), y no necesita bordes de tarjeta adicionales para "enmarcarlo"
