# Diseño de Héroe Superior (hero-top)

> 2-4 tarjetas.
> Sugerencia de división de espacio: Fila 1fr + fila auto. Gran banner superior ocupa 50-60% de altura + tarjetas pequeñas inferiores en fila.
> Datos aplicables: 1 dato de titular/imagen grande + múltiples métricas auxiliares. Común en páginas de resumen de métricas.
> El ancla superior (anchor) usa elevated/accent, los soportes inferiores (supports) usan outline/transparent en fila.

Aplicable: Estructura general-específica. Un área de resumen que domina todo abarca la parte superior, con 2-4 subelementos debajo detallando los puntos.

## Intención Estructural de Gravedad

- **Zona de Héroe (Resumen)**: Ocupa el dominio horizontal absoluto de la página. La implementación debe ser una viga Grid fuerte que cruce todo el ancho, o un contenedor Flex estricto, asegurando que presione firmemente el centro de gravedad de la página. Dado que la zona de héroe establece el tono de toda la página, los subelementos deben mantener la convergencia y un sentido de orden.

## Variantes (La cantidad de subelementos determina el ritmo inferior)

| N° de Subelementos | Diseño Inferior | Temperamento del Diseño |
|-------|---------|---------|
| 2 | Dos plataformas de exhibición amplias | Sensación de diálogo relajado |
| 3 | Tres pulsos de información equilibrados (más común) | Ritmo claro |
| 4 | Cuatro cristales de datos compactos | Sensación de alta densidad de información |

## Guía de Dinamismo

### Múltiples Expresiones del Alma de la Zona de Héroe
- **Opresiva**: La zona de héroe usa un color de fondo de alto contraste, dentro contiene un argumento central de 48px+ + datos clave, ocupando el 40%+ del peso visual de la pantalla, dejando que los subelementos inferiores respiren bajo su sombra.
- **Etérea**: La zona de héroe es completamente transparente, con solo una línea de texto de resumen de 28px + un gran espacio en blanco, dejando el escenario para los subelementos inferiores.
- **Pictórica**: La zona de héroe tiene una imagen, con texto superpuesto, creando una sensación de pantalla ancha de cine.

### Contraste Dinámico de los Subelementos Inferiores
- **Asignar estilos según la importancia del contenido** entre los subelementos. Si el contenido de cierto subelemento es el más importante, haz que se destaque de sus similares.
- No trates esta página como un "formulario con 4 casillas", usa cambios flexibles en espaciado y tamaño para reflejar el ritmo real del contenido.

### Lógica Subyacente de Implementación
- Sigue estrictamente la conversión de proporción de `grid-template-rows` y un eje principal Flex sólido.
- Debe satisfacer la intención estructural ortogonal de "grande arriba, pequeño abajo; general arriba, específico abajo", evitando el uso de posicionamiento absoluto tipo póster que se sale del flujo del documento al azar, asegurando que el peso del flujo del documento de la zona de héroe y la lógica de apilamiento del subconjunto inferior sean firmes.
