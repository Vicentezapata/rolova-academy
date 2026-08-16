# timeline (bloque de línea de tiempo) -- El río del tiempo

> Tipos de datos aplicables: timelines / journey_map / gantt_data. Eje horizontal/vertical + nodos.
> Estructura: orientation(horizontal/vertical) + nodes[]({time, title, description, highlight}).
> Puntos clave de diseño: los nodos highlight usan relleno sólido accent + tamaño más grande; los nodos normales usan borde + tamaño pequeño. Se recomiendan de 4 a 8 nodos; si supera los 8, dividir en páginas.
> card_style recomendado: transparent (incluye su propia estructura de eje). Disposición recomendada: l-shape / waterfall.

## Estructura JSON sin cambios (formato de datos en el borrador de planificación)
```json
{
  "card_type": "timeline",
  "orientation": "horizontal | vertical",
  "nodes": [
    {"time": "2020", "title": "Título del evento", "description": "Descripción breve (máx. 30 caracteres)", "highlight": false}
  ]
}
```

## Alma del diseño (no es una plantilla de código)

### Expresión dinámica de la línea de tiempo horizontal
- El eje no tiene por qué ser una línea recta rígida: puede ser un arco ligeramente curvado, puede engrosarse en los nodos highlight o desvanecerse gradualmente en el extremo para sugerir que "el futuro aún se extiende".
- Alternar los nodos arriba y abajo para crear un ritmo visual con sensación de respiración, rompiendo la monotonía de tener todos los nodos en la misma línea horizontal.
- Los nodos Highlight usan relleno sólido accent + tamaño más grande, mientras que los nodos normales usan contorno + tamaño más pequeño, creando una jerarquía visual clara.

### Expresión dinámica de la línea de tiempo vertical
- Las etiquetas de tiempo en el lado izquierdo pueden usar diferentes opacidades/tamaños de fuente, siendo más claras cuanto más recientes sean, creando una "sensación de profundidad temporal".
- La densidad de contenido en el área de descripción derecha no tiene por qué ser uniforme: otorgue más espacio a los eventos importantes y sintetice los secundarios.

### Guía de implementación
- El método de implementación del eje y las líneas conectoras no está limitado (se pueden usar div reales, pseudoelementos `::before`/`::after` o SVG en línea).
- Las flechas pueden ser SVG en línea o triángulos mediante border de CSS.
- Se recomiendan de 4 a 8 nodos; si supera los 8, dividir en varias páginas.
- Se recomienda el card_style `transparent`: la línea de tiempo ya incluye su propia estructura de eje y no necesita un contenedor cuadrado envolvente.