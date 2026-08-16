# Diseño Asimétrico de Dos Columnas (2/3 + 1/3)

> 2-3 tarjetas.
> Sugerencia de división de espacio: Columnas 2fr 1fr. Jerarquía clara -- el ancla (anchor) ocupa la zona grande de 2/3, el soporte (support) está en el flanco de 1/3.
> Datos aplicables: Páginas con 1 argumento central + 1 evidencia de apoyo.
> La zona principal usa `card_style` elevated/accent, la zona de apoyo usa outline/transparent -- prohibido usar `filled` en ambos lados.

Aplicable: Dos bloques de contenido con una clara relación principal-secundaria. El argumento central ocupa 2/3 del territorio visual, y los datos auxiliares hacen eco en el flanco.

## Intención Estructural de Gravedad


## Guía de Dinamismo

### El contraste es el alma
- Zona principal + `elevated` / `accent` = núcleo de gravedad ineludible.
- Zona de apoyo + `outline` / `transparent` = respiración ligera en el flanco.
- Absolutamente prohibido usar `filled` en ambos lados -- eso equivale a no tener jerarquía principal-secundaria.

### Posibilidad de Inversión de Gravedad
- Cambia la proporción de la columna a `1fr 2fr`, dejando la zona principal a la derecha -- rompe la inercia visual de que "el protagonista siempre está a la izquierda".
- La zona principal usa `transparent` solo con un número central de 80px, mientras que la zona auxiliar usa `filled` y se llena de detalles -- usar lo pequeño para combatir lo grande.

### Creación de Profundidad
- La zona auxiliar puede estar visualmente "más atrás" (usando menor contraste, tamaño de fuente más pequeño), haciendo que la zona principal se perciba "más cerca".
- La diferencia entre principal y auxiliar no es solo de ancho, sino también de "profundidad de campo".

### Desvío asimétrico (Requiere distribución precisa o usar proporción Flex en línea)
Las dos tarjetas se organizan automáticamente, no es necesario escribir `grid-row` / `grid-column`.
