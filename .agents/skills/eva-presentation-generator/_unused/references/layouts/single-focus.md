# Diseño de Enfoque Único (single-focus)

> 1-2 tarjetas.
> Sugerencia de división de espacio: Celda única centrada, con gran cantidad de espacio en blanco alrededor.
> Datos aplicables: Páginas donde un gráfico / diagrama / cita necesita un enfoque absoluto. Se recomienda `visual_weight` <= 5.
> El espacio en blanco en sí es el lenguaje de diseño -- usar compresión de espacio en blanco para contenidos escasos, creando un sentido de ritual.

Aplicable: Un argumento central que domina todo, un gráfico a pantalla completa, un dato clave que cambia la percepción. Rara vez usado -- elíjalo solo cuando el contenido realmente necesite un enfoque extremo.

## Intención Estructural de Gravedad


## Guía de Dinamismo

### El enfoque único es el diseño que más prueba las habilidades de diseño
No hay combinación de múltiples tarjetas de las que depender, toda la tensión visual recae completamente sobre el único foco y el espacio en blanco que lo rodea.

### Tres Almas del Foco
- **Ojo de la Tormenta de Datos**: En el centro exacto de la pantalla hay un dato clave de 120px+, rodeado por un espacio en blanco enorme + una marca de agua decorativa grande como sombra. Usa `transparent` style para dejar que el dato se exponga en el vacío.
- **Estela del Argumento**: Un argumento central de 36px+ se ubica en la proporción áurea de la pantalla, emparejado con una sutil decoración de fondo de halo en degradado; el texto en sí es el único ancla visual.
- **Ilustración Panorámica**: Una visualización de datos grande en SVG (gráfico de radar / gráfico de cuadrantes / diagrama de arquitectura) cubre toda el área, con etiquetas de texto esparcidas alrededor del gráfico.

### El espacio en blanco es parte del diseño
En un diseño de enfoque único, el contenido solo debe ocupar el 30-50% del área de la pantalla. El "vacío" del espacio restante es en sí mismo un lenguaje de diseño -- transmite que "vale la pena contener la respiración para contemplar esta información".

### Flujo de Documento de Enfoque Único (Sin necesidad de coordenadas Grid complejas)
Solo hay una tarjeta, se extiende automáticamente.
