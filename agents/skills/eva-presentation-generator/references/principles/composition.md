#Composición y espacio en blanco

> El espacio en blanco no es "espacio desperdiciado", es el elemento de diseño más poderoso. Atrae la atención hacia lo verdaderamente importante y da "aire" a la presentación.
> Campos afectados: `negative_space_target`, `grid-cols`, y espaciado de tarjetas.
> Cuando generes tarjetas, asegúrate de dejar un margen seguro y espacio entre ellas.

## Principios Gestalt

El cerebro humano organiza automáticamente los elementos visuales en conjuntos significativos:

| Principios | Significado | Aplicación PPT |
|------|------|---------|
| **Proximidad** | Los elementos cercanos se consideran un grupo | El espacio entre elementos dentro de una tarjeta es significativamente menor que el espacio entre tarjetas: la relación de espaciado transmite relaciones |
| **Similitud** | Los elementos de apariencia similar se consideran del mismo tipo | Las tarjetas de la misma clase comparten el mismo gen card_style (pero se pueden mezclar de manera flexible entre card_styles) |
| **Continuidad** | La línea de visión fluye a lo largo de la línea/dirección | Los nodos de la línea de tiempo/diagrama de flujo utilizan conexiones para guiar el camino visual |
| **Cierre** | El cerebro humano completa automáticamente formas incompletas | Los bordes de las tarjetas se pueden insinuar en lugar de cortarlos (como un trazo muy ligero en el contorno) |
| **Relación imagen-fondo** | El primer plano (imagen) y el fondo (abajo) deben estar claramente separados | La diferencia de presencia entre diferentes estilos de tarjetas crea naturalmente la separación de la imagen y el fondo.

## La Regla de los Tercios (Rule of Thirds)

Divida el lienzo en tercios horizontal y verticalmente y coloque elementos importantes en las intersecciones o líneas:

```
┌───┬───┬───┐
│   │   │   │  交叉点Sí视觉强点
├───┼───┼───┤  标题放上 1/3 线
│   │   │   │  核心数据放中心或右上交叉点
├───┼───┼───┤
│   │   │   │
└───┴───┴───┘
```

- No centres todo (a menos que sea la portada de un capítulo o una página de oración)
- La esquina superior izquierda es el punto de partida natural para la lectura, y la información importante comienza aquí.
- **Aplicación inteligente**: la regla de los tercios es una línea de referencia, no una vía de ferrocarril; los elementos centrales se pueden desviar deliberadamente de la intersección para crear una tensión visual asimétrica.

## Tres niveles de espacio en blanco

| Nivel | Posición | Función |
|------|------|------|
| **Macros espacios en blanco** | Márgenes de página (área segura) | Enmarque el contenido dentro del área segura del lienzo para evitar verdugones |
| **Espacio en blanco en la vista central** | Espaciado entre tarjetas | Distinguir diferentes grupos de información |
| **Microespacio en blanco** | Distancia entre elementos internos de la tarjeta | Diferenciar los niveles de título/texto/datos/gráficos |

## Jerarquía Visual

- **Tamaño**: Los elementos más grandes atraen primero la vista.
- **Contraste**: Los colores vibrantes sobre fondo neutro resaltan la información crítica.
- **Alineación**: Una alineación estricta a la cuadrícula (Bento Grid) transmite profesionalismo y orden.

## Autoprueba

- ¿La página tiene un "espacio para respirar" claro (no cada centímetro abarrotado)?
- Con todo el texto eliminado, ¿el esqueleto del diseño es claro y ordenado?
- ¿Está aumentando el espacio en blanco en los tres niveles (micro < meso < macro)?