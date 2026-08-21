# Sistema de Layouts -- El Lenguaje de Diseño del Espacio de Presentación PPTX

## El Lienzo: Tus Restricciones Físicas del Escenario

```
Lienzo Fijo: width=1280px, height=720px (Proporción de proyección 16:9)
Zona de Título: Desde arriba izquierda 40px, altura 50px (las páginas cover/section/end pueden manejarse libremente, no están sujetas a esta restricción)
Zona de Contenido: Espacio disponible 1200x580px
```

> Éstas son fronteras físicas, no de diseño. Un diseño verdadero de PPTX debe hacer que el contenido **dialogue con los bordes** -- a veces abrazándolos, a veces provocándolos, a veces dejando deliberadamente que los elementos los rocen de manera ambigua.

## Filosofía Central: El layout es un campo de gravedad, no una prisión

Cada archivo de layout define una **tendencia de distribución de la gravedad visual**, no una valla de hierro a nivel de píxeles.

Cuando leas "Principal-Secundario (2fr : 1fr)", la información obtenida debe ser:
- "La zona izquierda tiene un campo de atracción visual más fuerte, la derecha es más ligera"
- "El sujeto central de la información debe ser atraído por el campo gravitatorio izquierdo"

Y **absolutamente no debe ser**:
- "Pon un cuadrado de 790px a la izquierda, y dos cuadrados en 390px a la derecha"

### Qué proporcionan los archivos de layout

Cada archivo de layout describe:

1. **Filosofía del campo de gravedad** -- Cómo se distribuye la gravedad visual de este layout y cómo fluye la información.
2. **Expresiones del alma** -- Múltiples variantes completamente diferentes (el mismo layout puede presentar aspectos visuales totalmente distintos).
3. **Guías de composición dinámica** -- Cómo crear sorpresas visuales mientras se mantiene el núcleo del layout.

Los archivos de layout **no proporcionan** código de esqueleto HTML Grid. El LLM debe construir la estructura Grid de forma autónoma basándose en la filosofía del campo gravitatorio.

### `card_style` hace que las tarjetas "cobren vida"

El esqueleto solo gestiona la distribución espacial, `card_style` determina la presencia de cada tarjeta (ver detalles en `blocks/card-styles.md`). **Al menos 2 `card_style` por página** -- este es el umbral mínimo de dinamismo.

## Grados de Libertad de Páginas no-content

| Tipo de Página | Rigor Arquitectónico | Requisitos Centrales |
|----------|------------|----------|
| Portada (cover) | Máxima tensión -- Prohibida la dispersión, lanzar impacto visual sobre un marco Flex absolutamente sólido | Gran impacto de título + ilustración/atmósfera + huella de marca |
| Índice (toc) | Extremadamente alto -- Grid de división forzada o alineación Flex estricta | Títulos de capítulos claramente distinguibles, progresión en niveles |
| Cierre (end) | Máxima tensión -- Organizar elementos clave sobre un fuerte eje principal | Repaso central + CTA + Eco visual con la portada |

## Matriz de Decisión de Layout (Características del Contenido -> Tendencia de Distribución de Gravedad)

| Características del Contenido | Layout Recomendado | Descripción del Campo de Gravedad |
|---------|---------|-----------|
| 1 argumento central / dato monopoliza la escena | Enfoque Único `single-focus.md` | Toda la gravedad converge en el centro de la pantalla o en la proporción áurea, completamente rodeado de espacio en blanco |
| 2 conceptos paralelos colisionan | Simétrico `symmetric.md` | Enfrentamiento de cantidades iguales de gravedad izquierda-derecha, como los dos extremos de una balanza |
| Concepto principal + nota complementaria | Asimétrico `asymmetric.md` | Gravedad claramente sesgada a un lado (6:4), el otro lado asiente suavemente |
| 3 elementos paralelos mostrados por igual | Tres Columnas `three-column.md` | Tres centros de gravedad equilibrados dispuestos horizontalmente |
| 1 principal + 2 evidencias de apoyo | Principal-Secundario `primary-secondary.md` | Un abismo gravitatorio que atraviesa + dos satélites ligeros suspendidos |
| Resumen general + 3-4 desarrollos específicos | Héroe Superior `hero-top.md` | Una presa gravitacional transversal superior + flujos ligeros dispersos inferiores |
| 4-6 informaciones heterogéneas dispuestas densamente | Cuadrícula Mixta `mixed-grid.md` | Múltiples puntos de gravedad de diferentes densidades distribuidos entrecruzados |
| Argumento principal + evidencia lateral + conclusión inferior | Forma en L `l-shape.md` | Trayectoria gravitacional en forma de L: resbala desde el cuerpo principal hacia un lado y se asienta en el fondo |
| Visión general + desarrollo + datos laterales | Forma en T `t-shape.md` | Voladizo en forma de T: Visión general transversal superior + inmersión profunda inferior excéntrica |
| Múltiples cascadas de información de altura desigual | Cascada `waterfall.md` | Escalones de gravedad irregulares, creando un ritmo visual natural |

**Principios de Uso**:
- **Selección de layout impulsado por el contenido** -- Primero pregunta "¿Cuál es el modo de flujo de información de esta página?", luego encuentra el campo gravitatorio más adecuado en la matriz, en lugar de elegir un layout diferente solo para "ser distinto a la página anterior".
- **Cuidado con la inercia del layout** -- Si has elegido el mismo layout por 3+ páginas consecutivas, haz una pausa y pregúntate: ¿Es porque el contenido realmente lo necesita, o por costumbre?
- **Los 10 layouts son un sistema de matriz de alta precisión** -- En una presentación se deben invocar con precisión de 4 a 6 layouts diferentes para apoyar distintos objetivos expresivos, pero sin importar cuál se elija, no se deben transgredir las reglas de física límite de la arquitectura de dicho layout.

## Ley del Dinamismo: Cómo hacer que el mismo layout parezca completamente diferente

Incluso si dos páginas utilizan el layout "Principal-Secundario", deberían parecer completamente diferentes. Métodos:

1. **Inversión de gravedad**: La primera página tiene la zona principal a la izquierda, la segunda página puede cambiar el `grid-template-columns` a `1fr 2fr` para poner la zona principal a la derecha.
2. **Variaciones de presencia**: La primera página usa `accent` para la tarjeta principal + `transparent` para la auxiliar, la segunda página usa `elevated` para la tarjeta principal + `outline` para la auxiliar.
3. **Saltos de densidad**: La zona principal de la primera página está llena de datos en gráficos, la zona principal de la segunda página solo tiene un enorme eslogan + 80% de espacio vacío.
4. **Provocación de fronteras**: En la primera página todos los elementos permanecen de forma ordenada en sus celdas, en la segunda página se permite que algún elemento decorativo (gran marca de agua/sombra de datos) se desborde intencionalmente de la cuadrícula.

> Dinamismo no es caos. Dinamismo significa, bajo la restricción de los mismos genes de diseño (variables de color + sistema de tipografías), hacer que la coreografía visual de cada página sea inesperada y deje sin aliento.
