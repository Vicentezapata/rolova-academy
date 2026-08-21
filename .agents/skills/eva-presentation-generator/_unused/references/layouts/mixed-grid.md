# Diseño de Cuadrícula Mixta (mixed-grid)

> 4-6 tarjetas.
> Sugerencia de división de espacio: Cuadrículas de tamaño desigual en múltiples filas y columnas. Estilo panel de control con mucha información.
> Datos aplicables: status_dashboard / páginas de alta densidad con visualización paralela de múltiples métricas.
> Atención: Cuando hay muchas tarjetas, el contenido de cada una debe ser conciso (control estricto de `content_budget`), de lo contrario habrá sobrecarga cognitiva.

Aplicable: Alta densidad de información, 4-6 bloques heterogéneos. La mejor opción cuando hay muchas dimensiones de contenido y cada dimensión necesita mostrarse de forma independiente.

## Variantes de Intención Estructural

El mayor tabú en el diseño de alta densidad es "tamaños iguales", se debe crear una jerarquía artificial.

### Desplazamiento del foco (Centro de gravedad irregular)
Al agrandar una o dos tarjetas, se rompe la mediocridad de la cuadrícula. Por ejemplo, la tarjeta izquierda de la primera fila ocupa 2/3 del ancho, y el resto de las tarjetas llenan el espacio restante.

### Atravesar y Extender (Cinturón horizontal o viga vertical)
Entre muchas tarjetas pequeñas, inserta una tarjeta estrecha que atraviese toda la pantalla (cinturón horizontal) o una tarjeta alta que cruce de arriba a abajo (columna vertical), como línea divisoria visual de información.

### Sándwich (Panel de control en capas)
Hay una barra de descripción general que atraviesa todo el ancho en la parte superior e inferior, con varias tarjetas de métricas paralelas de tamaño pequeño intercaladas en el medio.

## Guía de Dinamismo

### El alma de la densidad es la "Desigualdad"
- Incluso si hay 6 tarjetas, absolutamente no pueden verse como una tabla de Excel. Debes cambiar su peso visual mediante una combinación de `background`, `border`, `opacity` y `box-shadow`.
- Haz que 1-2 tarjetas "salten" de la matriz.
- Cierta tarjeta puede ser extremadamente minimalista (fondo completamente transparente + un único número gigante de 64px), formando un contraste con las tarjetas densas de información adyacentes.

### Evita el laberinto de bordes
- Cuando el número de tarjetas supera las 4, no dibujes bordes sólidos para cada tarjeta. Usa mucho espacio en blanco, sutiles diferencias de color de bloque o sombras inferiores borrosas para insinuar los límites, evitando que la página parezca una jaula de hierro.

### Reglas de hierro de ejecución y límites artesanales
- **Irregular no significa desordenado**.
### Lógica subyacente de la implementación
- Abandona el enfoque ingenuo de división rígida y equitativa, usa restricciones precisas y complejas de `Grid`.
- Dependiendo de la longitud, anchura y estrechez del contenido, usa contenedores restringidos con precisión desigual de `grid` o bloqueados por `flex` del elemento padre. Tu sentido de la respiración debe construirse dentro de una estricta matriz de cajas, en lugar de flotar aleatoriamente fuera de la gravedad.
- **Prohibición estricta de colapso y desorden libre**: Cada bloque heterogéneo debe tener configuraciones precisas bloqueadas en el espacio (como `min-width`, `flex-shrink: 0`), requiriendo adaptarse al contenido como engranajes encajando, y nunca se permite depender del flujo de escape `float` o del uso aleatorio de posicionamiento absoluto no calculado causando superposiciones e imágenes rotas.
