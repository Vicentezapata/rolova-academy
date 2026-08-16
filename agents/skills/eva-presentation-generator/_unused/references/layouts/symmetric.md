# Diseño Simétrico de Dos Columnas (50/50)

> 2 tarjetas.
> Sugerencia de división de espacio: Columnas 1fr 1fr. Confrontación igual de izquierda y derecha 50/50.
> Datos aplicables: before_after / pros_cons / Plan A vs Plan B.
> Ambos lados deben usar diferentes `card_style` (ej. filled+outline), está prohibido usar `filled` en ambos.

Aplicable: Contrastar, conceptos en paralelo (A vs B, Ventajas vs Desventajas, Plan A vs Plan B)

## Intención Estructural de Gravedad


## Guía de Dinamismo

### "Simétrico" no significa "exactamente igual"
- El **esqueleto de información** de las dos tarjetas puede ser simétrico (mismas dimensiones, misma jerarquía), pero la **expresión visual debe tener contraste**.
- Técnica clásica de dinamismo: Un lado usa `accent` (representa recomendación/nuevo plan/ganador), el otro lado usa `filled` u `outline` (representa estado actual/plan antiguo/perdedor).
- Incluso para una comparación igualitaria, debe haber diferencia en los colores accent (izquierda usa accent-1, derecha usa accent-2/accent-3).

### Expresiones avanzadas más allá de la simetría estereotipada
- **Inclinación de Gravedad**: Aunque el espacio sea 50/50, hacer que el peso visual del contenido de un lado sea mucho mayor que el otro (ej. lado izquierdo usa datos grandes + accent, derecho usa outline + texto pequeño), creando una tensión de "simetría de forma pero gravedad excéntrica".
- **Cruzar la Brecha**: Usar CSS avanzado para compensación de tensión (como una marca VS grande absolutamente centrada, o una banda diagonal degradada), para fortalecer el sentido de colisión entre los dos mundos sin destruir la matriz subyacente dividida en partes iguales.
- **Respiración Alta y Baja**: El contenido de la tarjeta izquierda se organiza comenzando desde la parte superior, mientras que el contenido de la derecha comienza deliberadamente desde el centro, formando una caída visual.

### Flujo de Distribución Igualitaria (Puede lograr tensión de igualdad confiando solo en Flex básico)
Las dos tarjetas se organizan automáticamente, no es necesario escribir `grid-row` / `grid-column`.
