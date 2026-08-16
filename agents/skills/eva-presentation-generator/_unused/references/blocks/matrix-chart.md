# matrix_chart (Bloque de Matriz de Cuadrantes) -- Posicionamiento en Cuadrantes

> Tipos de datos aplicables: matrix_data / swot / competitive_matrix. Posicionamiento en coordenadas de cuadrantes 2x2.
> Estructura: axes(x_label, y_label) + quadrants[4]({label, items[], color}).
> Puntos clave de diseño: Cada cuadrante es un bloque de color independiente, los `items` se marcan con puntos de posicionamiento, ideal para análisis estratégico y evaluación multidimensional.
> Disposición recomendada: single-focus / primary-secondary.

## Estructura JSON
```json
{
  "card_type": "matrix_chart",
  "title": "Análisis de Posicionamiento de Mercado",
  "x_label": "Significado del Eje X (ej. Dificultad de Ejecución)",
  "y_label": "Significado del Eje Y (ej. Valor de Negocio)",
  "quadrants": [
    {"position": "top-right", "title": "Prioridad de Ejecución", "items": ["Proyecto A", "Proyecto B"], "highlight": true},
    {"position": "top-left", "title": "Inversión a Largo Plazo", "items": ["Proyecto C"], "highlight": false},
    {"position": "bottom-right", "title": "Resultados Rápidos", "items": ["Proyecto D"], "highlight": false},
    {"position": "bottom-left", "title": "Baja Prioridad", "items": ["Proyecto E"], "highlight": false}
  ]
}
```

## Alma del Diseño

### La Tensión Visual del Cuadrante
- El **Eje Cruzado** es la columna vertebral de todo el componente -- no lo conviertas en simples dos líneas grises. Puedes usar una línea gruesa (2-3px) con opacidad extremadamente baja del color `accent`, dando "presencia" a los ejes sin opacar el contenido.
- El **Cuadrante Highlight** debe "saltar" visualmente -- color de fondo `accent` con 15% de opacidad + título en negrita y color + etiquetas de los elementos usando píldoras de color `accent`.
- Los **Otros Cuadrantes** deben mantenerse moderados -- 5% de opacidad o totalmente transparentes, las etiquetas de los elementos usan `text-secondary`.

### Técnicas Dinámicas
- No hagas que los cuatro cuadrantes luzcan completamente simétricos -- el cuadrante `highlight` puede tener un área ligeramente mayor / tono ligeramente más intenso, creando un "desplazamiento de gravedad visual".
- Las etiquetas de los ejes en los cuatro extremos usan 12px + letter-spacing:1px, como las marcas de escala de un sistema de coordenadas.
- Las etiquetas de los elementos usan píldoras redondeadas, y pueden esparcirse libremente dentro del cuadrante (no alineación estricta), insinuando el concepto de "posicionamiento".

### `card_style` recomendado: `transparent` + ocupación de gran área cruzando filas y columnas
- Un gráfico de cuadrantes necesita suficiente espacio para presentar claramente una estructura de cuatro cuadrantes.
- Se recomienda ocupar todo el espacio disponible.
