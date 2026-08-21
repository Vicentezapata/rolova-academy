# Diseño en Forma de L (Principal + Flanco + Inferior)

> 3 tarjetas.
> Sugerencia de división de espacio: Forma de L (Principal 60% + Flanco 40% en primera fila, Inferior 100% en segunda fila).
> Datos aplicables: Página de tres partes: argumento central + evidencia lateral + conclusión inferior.
> Trayectoria visual: Sumersión desde el principal -> deslizamiento hacia el flanco -> anclaje en el fondo. La tarjeta inferior se usa a menudo para summary/source_guidance.

Aplicable: Exhibición central + datos auxiliares + resumen inferior/barra de etiquetas. El diseño dorado cuando la información tiene tres niveles.

## Intención Estructural de Gravedad


## Guía de Dinamismo

### El Cambio Drástico Emocional de Tres Niveles
- **El Primer Nivel (Zona Principal)** es el núcleo de gravedad de la pantalla -- puede ser una tormenta de datos con colores intensos, o un argumento único y minimalista flotando en un gran espacio en blanco.
- **El Segundo Nivel (Doble Satélite Derecho)** es el grito del flanco -- compacto pero preciso, dos tarjetas usan diferente `card_style` (ej. `elevated` vs `outline`) creando desniveles.
- **El Tercer Nivel (Barra Inferior)** es el anclaje inferior -- puede ser una nube de etiquetas cruzando todo el ancho, una fila de métricas, o una conclusión poderosa. Usa `transparent` para hacerlo ligero, o `accent` para darle un gran cierre final.

### Posibles Variaciones
- Zona principal usa `transparent` + dato gigante de 120px, lado derecho usa `filled` para los detalles -- "Izquierda impactante, Derecha analítica".
- Dos tarjetas derechas: una `accent` y una `transparent` -- "Una arde, una respira".
- La barra inferior usa `glass` cubriendo una decoración de fondo con degradado muy sutil -- creando una sensación de anclaje en la niebla.


| Atributo | Necesidad | Descripción |
|------|-------|------|
| Tarjeta Principal `grid-row: 1 / 3` | **Obligatorio** | Si no se escribe, la zona principal solo ocupa una fila |
| Barra Inferior `grid-column: 1 / -1` | **Obligatorio** | Si no se escribe, la parte inferior solo ocupa una columna |
| Cada tarjeta necesita un posicionamiento grid claro | **Obligatorio** | La forma en L no puede depender de la organización automática |
