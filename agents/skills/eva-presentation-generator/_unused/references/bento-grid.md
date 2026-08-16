# Sistema de Diseño Bento Grid

## Parámetros del lienzo

```
Lienzo fijo: width=1280px, height=720px
Área de título: x=40, y=20, w=1200, h=50
Área de contenido: x=40, y=80, w=1200, h=580
Espaciado de tarjetas: gap=20px
Borde redondeado de tarjetas: border-radius=12px
Relleno de tarjetas: padding=24px
```

## Implementación con CSS Grid

Todos los diseños se implementan con precisión mediante CSS Grid. Definición unificada del contenedor del área de contenido:

```css
.content-area {
  position: absolute;
  left: 40px; top: 80px;
  width: 1200px; height: 580px;
  display: grid;
  gap: 20px;
}
```

## Diseños de tipos de página

### Portada (cover)
- Título principal centrado o alineado a la izquierda, font-size=48-56px, color accent-primary
- Subtítulo font-size=24px
- Ponente/Fecha/Empresa en texto pequeño en la parte inferior, font-size=16px
- Decoración: bloques de color de marca, líneas geométricas, imágenes (técnica de fusión con desvanecimiento)
- **No utiliza Bento Grid**, maquetación libre

### Índice (toc)
- Cuadrícula de 2 a 5 tarjetas de igual tamaño

| Número de tarjetas | grid-template-columns | Tamaño de tarjeta individual |
|-------|----------------------|---------|
| 2 | 1fr 1fr | 590x540 |
| 3 | repeat(3, 1fr) | 387x540 |
| 4 | 1fr 1fr / 1fr 1fr (2x2) | 590x260 |
| 5 | repeat(3, 1fr) / repeat(2, 1fr) (3+2) | Mixto |

### Portada de sección (section)
- "PART 0X" font-size=20px, accent-primary, letter-spacing=2px
- Título font-size=44px, font-weight=700
- Introducción font-size=18px, color=text-secondary
- Abundante espacio en blanco para crear una sensación de amplitud
- **No utiliza Bento Grid**, maquetación centrada

### Página de cierre (end)
- Título font-size=44px centrado
- 3 a 5 puntos clave, font-size=18px
- Información de contacto/CTA en la parte inferior

---

## 7 diseños de página de contenido

Todos basados en el área de contenido (1200x580px, coordenadas de inicio 40,80).

### 1. Enfoque único

Aplicación: 1 argumento clave / visualización de datos masivos a pantalla completa

```css
.content-area { grid-template: 1fr / 1fr; }
/* Tarjeta: 1200x580 */
```

### 2. Simetría 50/50

Aplicación: Comparación, conceptos paralelos

```css
.content-area { grid-template: 1fr / 1fr 1fr; }
/* Izquierda: 590x580 | Derecha: 590x580 */
```

### 3. Dos columnas asimétricas (2/3 + 1/3)

Aplicación: Relación principal-secundaria. **El diseño más utilizado.**

```css
.content-area { grid-template: 1fr / 2fr 1fr; }
/* Principal: 790x580 | Secundario: 390x580 */
```

### 4. Tres columnas de igual ancho

Aplicación: 3 comparaciones paralelas

```css
.content-area { grid-template: 1fr / repeat(3, 1fr); }
/* Tarjeta 1: 387x580 | Tarjeta 2: 387x580 | Tarjeta 3: 386x580 */
```

### 5. Combinación principal-secundaria (Grande + Dos pequeñas)

Aplicación: Relación jerárquica. **Recomendado: Opción prioritaria cuando la jerarquía de información es rica.**

```css
.content-area { grid-template: 1fr 1fr / 2fr 1fr; }
/* Principal: 790x580 (abarca 2 filas) | Secundario 1: 390x280 | Secundario 2: 390x280 */
```

La tarjeta principal debe configurarse con `grid-row: 1 / -1;` para abarcar dos filas.

### 6. Estilo héroe superior

Aplicación: Relación general-detalle. **Recomendado: Opción prioritaria cuando la estructura general-detalle es clara.**

**Versión de 3 subelementos (la más común)**:
```css
.content-area { grid-template: auto 1fr / repeat(3, 1fr); }
/* Héroe: 1200x260 (span 3 cols) | Sub 1-3: 387x300 */
```

**Versión de 4 subelementos**:
```css
.content-area { grid-template: auto 1fr / repeat(4, 1fr); }
/* Héroe: 1200x260 (span 4 cols) | Sub 1-4: 285x300 */
```

**Versión de 2 subelementos**:
```css
.content-area { grid-template: auto 1fr / 1fr 1fr; }
/* Héroe: 1200x280 (span 2 cols) | Sub 1-2: 590x280 */
```

La tarjeta héroe debe configurarse con `grid-column: 1 / -1;` para abarcar todas las columnas.

### 7. Cuadrícula mixta

Aplicación: Alta densidad de información, de 4 a 6 bloques heterogéneos. **Recomendado: Opción prioritaria cuando la densidad de información es máxima.**

**Cuadrícula 2x3**:
```css
.content-area { grid-template: repeat(3, 1fr) / 1fr 1fr; }
/* 6 tarjetas: 590x180 cada una */
```

Se puede usar el span de `grid-row`/`grid-column` para permitir que tarjetas individuales abarquen varias filas/columnas, creando un efecto de mezcla de tamaños.

**Restricción clave**: Ninguna tarjeta debe exceder los límites del área de contenido (x+w<=1240, y+h<=660), espaciado >=20px, prohibido el solapamiento.

---

## Matriz de decisión de diseño

| Características del contenido | Diseño recomendado | Número de tarjetas |
|---------|---------|-------|
| 1 argumento clave / datos | Enfoque único | 1 |
| 2 comparaciones / paralelos | Simetría 50/50 | 2 |
| Concepto principal + suplemento | Dos columnas asimétricas | 2 |
| 3 elementos paralelos | Tres columnas de igual ancho | 3 |
| 1 principal + 2 secundarios | Combinación principal-secundaria | 3 |
| Resumen + 3-4 subelementos | Estilo héroe superior | 4-5 |
| 4-6 bloques heterogéneos | Cuadrícula mixta | 4-6 |

**Prioridad de selección**: Evitar el "Enfoque único" (a menos que realmente solo haya un contenido a pantalla completa). Cuando el contenido sea >= 3 bloques, priorizar la combinación principal-secundaria / estilo héroe / cuadrícula mixta.

---

## 6 tipos de contenido de tarjeta

### text (Tarjeta de texto)
- Título: h3, 18-20px, 700 weight
- Cuerpo: p, 13-14px, line-height 1.8
- Palabras clave destacadas con `<strong>` o `<span class="highlight">`
- **Requisito mínimo**: Título + al menos 2 párrafos de cuerpo (de 30 a 50 palabras cada uno)

### data (Tarjeta de datos)
- Número clave: 36-48px, 800 weight, color accent
- Unidad/Etiqueta: 14-16px, text-secondary
- Interpretación complementaria: 13px
- Se recomienda acompañar con una visualización CSS (barra de progreso / columnas de comparación / gráfico circular)
- **Requisito mínimo**: Número clave + unidad + tendencia + interpretación + visualización

### list (Tarjeta de lista)
- Viñetas: puntos de 6-8px, color accent
- Texto: 13px, line-height 1.6
- Uso alternado de puntos de diferentes colores accent para aumentar la sensación de jerarquía
- **Requisito mínimo**: Al menos 4 elementos de lista, de 15 a 30 palabras cada uno

### tag_cloud (Nube de etiquetas)
- Contenedor: flex-wrap, gap=8px
- Etiquetas: forma de cápsula redondeada, 12px, borde de color accent
- **Requisito mínimo**: Al menos 5 etiquetas

### process (Tarjeta de proceso)
- Nodos: círculo de 32px, color accent, número de paso centrado
- Líneas de conexión: **elementos `<div>` reales** (prohibido ::before/::after)
- Flechas: **SVG `<polygon>` en línea** (prohibido CSS border para triángulos)
- **Requisito mínimo**: Al menos 3 pasos, título de cada paso + una frase descriptiva

### data_highlight (Área destacada de datos masivos)
- Utilizado para la visualización de datos masivos en portadas o páginas clave
- Número: 64-80px, 900 weight, color accent
- Subtítulo + fila de datos complementarios
- **Requisito mínimo**: 1 número gigante + subtítulo + fila de datos complementarios