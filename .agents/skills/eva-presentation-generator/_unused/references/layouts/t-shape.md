# Diseño en Forma de T (Transversal Superior + Excéntrico Inferior)

> 3 tarjetas.
> Sugerencia de división de espacio: Forma de T (Primera fila 100% visión general transversal + Segunda fila 1fr 1fr dos áreas de inmersión profunda).
> Datos aplicables: Estructura general-específica -- 1 visión general/título/KPI que atraviesa la parte superior + 2 puntos específicos en la parte inferior.
> La parte superior usa accent/elevated para crear una sensación de fuerza transversal, las dos celdas inferiores usan filled+outline para crear particiones.

Aplicable: Primero visión general y luego despliegue, y la información inferior tiene una clara relación principal-secundaria. La diferencia con el diseño heroico es que la parte inferior está dividida de forma desigual.

## Intención Estructural de Gravedad


## Guía de Dinamismo

### Múltiples Personalidades de la Viga Principal Superior
- **Declarativa**: Una fila de 28px de argumento central + 3-4 píldoras de datos de KPI dispuestas horizontalmente, como la barra de titulares de noticias de última hora.
- **Atmosférica**: Sombreado de imagen muy claro + texto translúcido superpuesto, usar `glass` para hacer de la parte superior el "cielo" de la pantalla.
- **Banda de Datos**: Disposición horizontal de barras de progreso/columnas de comparación, usar `transparent` para dejar los datos al descubierto en la parte superior de la pantalla.

### Jerarquía de las Áreas de Inmersión Profunda Inferiores
- La tarjeta grande inferior izquierda es el campo de batalla principal del "despliegue detallado" -- Gráficos + interpretación + argumento, usa `filled` o `elevated` para darle peso.
- Las dos tarjetas pequeñas inferiores derechas son los "susurros laterales" -- datos complementarios compactos, usa `outline` o `transparent` para mantenerlos ligeros.
- Debe haber al menos 2 diferencias de `card_style` entre las tres.


| Atributo | Necesidad | Descripción |
|------|-------|------|
| Barra Transversal Superior `grid-column: 1 / -1` | **Obligatorio** | Si no se escribe, solo ocupará una columna |
| Tarjeta Grande Inf. Izquierda `grid-row: 2 / 4` | **Obligatorio** | Si no se escribe, solo ocupará una fila |
| Cada tarjeta necesita un posicionamiento grid claro | **Obligatorio** | La forma en T no puede depender de la organización automática |
