# Diseño de Tres Columnas (three-column)

> 3 tarjetas.
> Sugerencia de división de espacio: Columnas 1fr 1fr 1fr. Tres columnas del mismo ancho en paralelo.
> Datos aplicables: parallel_items / pricing_plans / team_profiles (3 elementos paralelos del mismo peso).
> Cada columna debe usar al menos 2 `card_style` (ej. filled+accent+outline), prohibido usar 3 `filled` completos.

Aplicable: 3 comparaciones paralelas (tres ventajas principales, tres fases, tres líneas de productos).

## Intención Estructural de Gravedad


## Guía de Dinamismo

### "Tres columnas" es el diseño que más fácilmente cae en la trampa de la monotonía
Tres tarjetas del mismo ancho + mismo `card_style` + misma estructura de información = un manual mediocre sin tensión de diseño. Debes construir una coreografía avanzada con una base unificada y elementos complementarios:

1. **Distribución no uniforme de `card_style`**: Haz que la tarjeta del medio use `accent` o `elevated` (porque el medio es el punto de aterrizaje visual natural), y los lados usen `filled` + `outline` o `transparent`.
2. **Diferenciación de la forma del contenido**: Incluso si las tres tarjetas muestran información del mismo nivel, deben usar diferentes formas de organizar el contenido -- por ejemplo, la primera usa visualización de datos, la segunda usa una lista, la tercera usa una cita brillante.
3. **Olas de peso visual**: La densidad de contenido de las tres tarjetas no debe ser exactamente igual. Haz que una tarjeta tenga contenido escaso (mucho espacio en blanco + un número central), y otra tarjeta tenga un contenido denso (lista + datos + interpretación).

### Superando la limitación del mismo ancho
- Puedes superponer un contenedor cruzado `transparent` arriba o abajo de las tres tarjetas (como una nube de etiquetas o una conclusión en una línea), extrayendo puntos clave bajo la estructura de carcasa rígida de tarjetas paralelas.

### Desvío estricto en tres tercios (Controlado estrictamente por Flex fuerte o Grid de 3 columnas)
Las tres tarjetas se organizan automáticamente, no es necesario escribir `grid-row` / `grid-column`.
