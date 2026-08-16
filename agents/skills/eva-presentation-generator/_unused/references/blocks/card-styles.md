# Variantes Visuales de Tarjeta (card_style) -- Lenguaje de Diseño PPTX

> Tabla de decisión de card_style: 6 tipos de presencia visual -- filled (base sólida) / transparent (flotación sin bordes) / outline (borde etéreo) / accent (núcleo ardiente) / glass (fantasma en la niebla) / elevated (roca flotante).
> Regla: Usar >= 2 tipos por página para romper la monotonía; accent y elevated máximo 1 cada uno por página.
> Resonancia interna entre card_type y card_style: data_highlight usa transparent/accent, quote usa transparent, timeline/diagram usa transparent (tienen esqueleto propio, no necesitan caja), comparison usa outline, data/text/list usan filled/outline.
> Combinaciones de máximo contraste: accent+transparent+filled (Fuego vs Vacío vs Tierra), elevated+outline+transparent (Roca Flotante vs Burbuja vs Fantasma).

## Filosofía de Diseño: Cada variante es una "Presencia Espacial"

No entiendas `card_style` simplemente como "cambiar el color de fondo de un div". En el auténtico lenguaje de diseño PPTX, cada variante representa la **forma en que la información existe y respira** en la pantalla. Define si el contenido se asienta en el fondo, flota en el medio, o salta a la superficie.

## Definición del Alma de las 6 Variantes

### filled -- La Tierra Firme
- **Presencia espacial**: Una capa base sólida, la superficie de soporte de información más confiable en la pantalla.
- **Esencia**: Un área física con límites perceptibles, rellena con el color principal.
- **Pensamiento de diseño**: Imagina un bloque de mármol pulido. No necesita adornarse; su propósito es hacer que el contenido sobre él se vea estable y creíble.
- **Absolutamente prohibido**: Que todas las tarjetas usen `filled` -- "Todo es una mesa de mármol" equivale a "No hay protagonista".

### transparent -- El Espíritu Sin Límites
- **Presencia espacial**: Una presencia fantasmal, el contenido respira directamente expuesto al vacío.
- **Esencia**: Sin fondo, sin bordes, sin rastros. El contenido flota independientemente sostenido por su propia gravedad visual.
- **Pensamiento de diseño**: Una cita impactante, un dato central de 120px -- no necesitan estar contenidas en una caja, son el ancla visual de la pantalla en sí mismas. Déjalas "crecer" directamente en el espacio de la página.
- **Combinación dorada**: data_highlight / quote / timeline / diagram -- estos componentes ya tienen un esqueleto visual; envolverlos en una caja es un desastre visual.

### outline -- El Borde Etéreo
- **Presencia espacial**: Una película de burbuja apenas visible, sugiere un límite pero no crea una barrera.
- **Esencia**: Usa un borde muy sutil (color `accent` al 20% de opacidad) para delinear suavemente la superficie de existencia.
- **Pensamiento de diseño**: Información auxiliar, datos secundarios, notas explicativas -- necesitan un sentido de límite pero no deben robar peso visual. Como un narrador que asiente en voz baja.

### accent -- El Núcleo Ardiente
- **Presencia espacial**: El único núcleo ardiente en la pantalla, saltando intensamente desde el fondo.
- **Esencia**: Relleno de gradiente del color de énfasis del tema + texto invertido, creando una explosión visual innegable.
- **Pensamiento de diseño**: Esta es la parte de la página que más quieres que la audiencia recuerde. Es como el protagonista solo bajo un foco de luz. **Máximo 1 por página** -- dos focos equivalen a ningún foco.
- **Tensión visual**: Cuando se coloca junto a una tarjeta `transparent`, crea el máximo contraste -- uno ardiendo, el otro respirando en el vacío.

### glass -- El Fantasma en la Niebla
- **Presencia espacial**: Una capa de hielo flotante translúcida, creando una profundidad de campo brumosa sobre el fondo o gradiente.
- **Esencia**: Textura de vidrio esmerilado (frosted glass), permitiendo que la información visual de fondo se filtre sutilmente.
- **Pensamiento de diseño**: Cuando la página tiene imágenes o un fondo degradado intenso, `glass` hace que las tarjetas de información parezcan vallas publicitarias flotando en la niebla -- legibles sin destruir la atmósfera del fondo.
- **Nota**: El `backdrop-filter` en `glass` puede no ser compatible al exportar a PPTX, pero es el recurso de profundidad más sorprendente en la vista previa HTML.

### elevated -- La Roca Flotante
- **Presencia espacial**: Una isla flotante que "empuja" hacia afuera de la pantalla, usando sombras para crear un relieve físico en el eje Z.
- **Esencia**: Fondo sólido + sombra de proyección clara + sutil desplazamiento hacia arriba, creando la ilusión de "este contenido está físicamente más cerca".
- **Pensamiento de diseño**: La tarjeta más importante de la página. No solo su contenido es importante, sino que debe estar "más cerca" espacialmente. **Máximo 1 por página**.
- **Combinación extrema**: Al encuadrar con `transparent` y `outline`, `elevated` se ve como un pico solitario elevándose desde la llanura.

## Reglas de Uso (La esencia de la fluidez radica en el contraste y la mezcla)

1. **Al menos 2 `card_style` por página** -- este es el requisito mínimo para crear profundidad y una respiración dinámica.
2. **Máximo 1 `accent` y 1 `elevated` por página** -- demasiado énfasis = ningún énfasis.
3. **No hay valor por defecto** -- el `card_style` de cada tarjeta debe ser elegido activamente basándose en su rol en la pantalla.
4. **Combinaciones dinámicas recomendadas** (de mayor a menor tensión):
   - `accent` + `transparent` + `filled` -- Contraste extremo: Fuego vs Vacío vs Tierra.
   - `elevated` + `outline` + `transparent` -- Profundidad en capas: Roca Flotante vs Burbuja vs Fantasma.
   - `glass` + `transparent` + `accent` -- Atmósfera inmersiva: Niebla vs Vacío vs Llama.
   - `filled` + `outline` -- Ritmo suave: Entidad vs Borde Etéreo (profundidad mínima).

## Resonancia Interna con card_type

| card_type | Presencia más adecuada | Por qué |
|----------|-------------|-------|
| data_highlight | `transparent` / `accent` | Un número de 120px es un ancla por sí mismo, no necesita una caja; o usa fuego para convertirlo en un núcleo explosivo innegable. |
| quote | `transparent` | Una cita brillante expuesta en el vacío, sosteniendo la pantalla solo con la gravedad de sus palabras, ese es el verdadero poder. |
| image_hero | `transparent` / `glass` | Una imagen grande no necesita restricciones de bordes; o usa un fantasma en la niebla para hacer que el texto flote sobre la imagen. |
| timeline | `transparent` / `outline` | Una línea de tiempo tiene su propio esqueleto de eje, un cuadro alrededor es ruido innecesario. |
| diagram | `transparent` | Un diagrama/arquitectura tiene su propia estructura visual de nodos y líneas de conexión, un cuadro solo interferirá. |
| comparison | `outline` | El borde separa suavemente dos paneles, sin ocupar peso visual. |
| data | `filled` / `accent` (métrica central) | Las tarjetas de datos usan una entidad sólida como portador, o una llama para resaltar la más crítica. |
| text | `filled` / `outline` | El texto necesita un límite de lectura claro. |
| list | `filled` / `outline` | Las listas necesitan estar contenidas dentro de un área reconocible. |
