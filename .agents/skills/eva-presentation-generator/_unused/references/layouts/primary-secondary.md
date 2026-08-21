# Diseño Principal-Secundario (Grande + Dos Pequeñas)

> 3 tarjetas.
> Sugerencia de división de espacio: Tarjeta grande izquierda 2/3 de altura + 2 tarjetas pequeñas apiladas a la derecha.
> Datos aplicables: 1 exhibición central + 2 datos auxiliares. Común en páginas con big_number + métricas de apoyo.
> La tarjeta grande usa elevated/accent, las dos pequeñas usan outline/transparent.

Aplicable: Contenido con una clara relación principal-subordinada. Un argumento central monopoliza 2/3 de la pantalla, y dos datos auxiliares asienten suavemente en el flanco.

## Intención Estructural de Gravedad


## Guía de Dinamismo

### Variación de Atmósfera de la Zona Principal (Debe ser diferente cada vez que se usa)
- **Universo de Datos**: La zona principal está llena de gráficos centrales + datos grandes + interpretaciones detalladas, es el agujero negro de información de la página entera. La zona de apoyo usa `outline` para dibujar a la ligera algunos KPIs complementarios.
- **Propuesta Minimalista**: La zona principal tiene 80% de espacio en blanco, solo contiene un argumento central de 36px + una pequeña evidencia de datos. La zona auxiliar, en cambio, usa `accent` y `elevated` para albergar datos específicos, formando un contraste de "Zona principal silenciosa, Flanco ruidoso".
- **Narrativa Gráfico-Texto**: La mitad superior de la zona principal tiene una imagen (en tiempo de ejecución el `usage` suele ser `inline-illustration`, puede adoptar la técnica `card-inset`), la mitad inferior tiene texto explicativo. La zona de apoyo usa tarjetas de datos compactas.

### La Presencia de la Zona de Apoyo
- El espacio de la zona auxiliar es compacto (aprox. 1/3 del ancho x media altura), el contenido debe ser extremadamente refinado.
- Entre las dos tarjetas auxiliares se deben usar diferentes `card_style` -- una `filled` y una `outline`, o una `elevated` y una `transparent`.
- Las tarjetas auxiliares son ideales para: Números de KPI, gráficos circulares, barras de progreso, listas breves.


| Atributo | Necesidad | Descripción |
|------|-------|------|
| Zona Principal `grid-row: 1 / -1` | **Obligatorio** | Si no se escribe, la zona principal ocupa una fila y las tarjetas de apoyo son empujadas abajo |
| Zona Auxiliar `grid-row` | **Omitir** | Se organizan automáticamente arriba y abajo a la derecha |

### Inversión Dinámica
- Intenta cambiar la proporción de la columna a `1fr 2fr`, dejando la zona principal a la derecha -- rompiendo la inercia de "el protagonista siempre está a la izquierda".
- Intenta que la zona principal use `transparent` mientras la auxiliar usa `accent` -- lo inusual es dinámico.
