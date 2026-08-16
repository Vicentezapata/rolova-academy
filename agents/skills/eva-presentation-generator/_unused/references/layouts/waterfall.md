# Diseño de Cascada (3 Columnas de Altura Desigual)

> 3-5 tarjetas.
> Sugerencia de división de espacio: Múltiples columnas de altura desigual. La diferencia de altura irregular crea ritmo.
> Datos aplicables: process_flows / timelines / journey_map (Contenido secuencial que requiere ritmo visual).
> Alternar altos y bajos crea un sentido de caída de cascada. Columnas altas usan filled/elevated, columnas bajas usan outline/transparent.

Aplicable: Múltiples bloques de información de altura desigual (Preguntas frecuentes, listas de funciones, análisis multidimensional). 4-6 bloques de contenido dispuestos de forma natural.

## Intención Estructural de Gravedad


## Guía de Dinamismo

### La ventaja natural del flujo en cascada: Lo irregular es dinámico
- Diferentes tarjetas varían en altura debido a diferentes cantidades de contenido; esta irregularidad natural en sí misma crea un ritmo visual.
- **Absolutamente prohibido** hacer que todas las tarjetas tengan más o menos la misma cantidad de contenido -- eso se convertiría en un diseño de tres columnas de ancho igual, perdiendo el sentido de la cascada.

### Crear deliberadamente diferencias de altura
- Haz que una tarjeta solo contenga un dato central (baja), la tarjeta adyacente contenga una lista + interpretación de datos (alta).
- Haz que una tarjeta use `transparent` + gran espacio en blanco (visualmente baja), y la de al lado use `filled` llena de contenido (visualmente alta).

### El ritmo del `card_style`
- Para 6 tarjetas usa al menos 3 diferentes `card_style`, formando un compás visual (ej. filled-outline-accent-filled-transparent-outline).
- Haz que una tarjeta clave salte de los escalones irregulares usando `accent` o `elevated`.

### Prevención de Desbordamiento
- El contenedor exterior `overflow:hidden` evita que la altura total supere los 580px.
- El espacio de la tarjeta es compacto (aprox. 1/3 de ancho), el contenido es refinado.
