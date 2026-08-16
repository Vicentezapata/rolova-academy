# Reglas de Compatibilidad de la Pipeline HTML -> SVG -> PPTX

Este documento resume todas las lecciones de compatibilidad de la pipeline. **Deben cumplirse al generar borradores de diseño HTML para evitar problemas de desplazamiento desde el origen.**

Principio fundamental: **html2svg + svg2pptx no es un navegador**, muchas propiedades CSS y atributos SVG se perderán o se desplazarán durante el proceso de conversión. El código HTML debe tener en cuenta los límites de capacidad de los convertidores subsiguientes.

---

## 1. Lista de Prohibiciones CSS

| Característica Prohibida | Fenómeno tras la Conversión | Alternativa Correcta |
|---------|---------|-----------|
| `background-clip: text` | Bloque de color degradado + texto blanco | `color: var(--accent-1)` colorear directamente |
| `-webkit-text-fill-color` | El color del texto se pierde | Propiedad `color` estándar |
| `mask-image` / `-webkit-mask-image` | La imagen desaparece por completo | Capa de máscara `<div>` (fondo linear-gradient) |
| `::before` / `::after` (Para decoración visual) | El contenido desaparece | Elementos reales `<div>` / `<span>` |
| `conic-gradient` | No se renderiza | SVG en línea `<circle>` + stroke-dasharray |
| Triángulos de borde CSS (truco width:0) | La forma se pierde | SVG en línea `<polygon>` |
| `mix-blend-mode` | No soportado | Superposición con `opacity` |
| `filter: blur()` | Rasterizado a mapa de bits | `opacity` o `box-shadow` |
| `content: 'Texto'` | El texto desaparece | Elemento real `<span>` |
| CSS `background-image: url(...)` | Ignorado por dom-to-svg | Etiqueta `<img>` |

Respaldo de html2svg.py: Cubre las 3 primeras + pseudoelementos + conic-gradient + triángulos de borde (6 en total), pero el efecto de respaldo es mucho peor que el enfoque correcto.

---

## 2. Técnicas Antidesplazamiento (Sección Clave)

El posicionamiento de texto de svg2pptx se basa en las coordenadas del elemento SVG text, pero el sistema de coordenadas del textbox de PPTX es diferente al de SVG (SVG text y = baseline, PPTX y = parte superior del textbox). Las siguientes prácticas pueden evitar el desplazamiento desde el origen HTML:

### 2.1 Anotaciones de Texto en SVG en Línea -- Usar superposición HTML en lugar de SVG text

**Problema**: Los elementos `<text>` en los SVG en línea, después de la conversión dom-to-svg, están en el sistema de coordenadas viewBox, y svg2pptx tiene una pérdida de precisión (alrededor de +/- 3-5px) al procesar el desplazamiento del baseline y el text-anchor middle, causando el desplazamiento de la posición de la anotación.

**Solución HTML antidesplazamiento**: Mover la anotación de texto fuera de la etiqueta SVG `<text>` y usar posicionamiento absoluto HTML `<div>` superpuesto encima del SVG. El div HTML es posicionado con precisión por dom-to-svg, no sufre conversión de coordenadas viewBox y el riesgo de desplazamiento es cero.

```html
<!-- Correcto: div HTML superpone anotaciones, cero desplazamiento -->
<div class="chart-container" style="position: relative;">
  <svg viewBox="0 0 660 340" style="width:100%; height:100%;">
    <!-- Solo dibuja elementos gráficos como pilares, líneas, no escribas <text> -->
    <rect x="80" y="100" width="60" height="200" fill="#FF6900"/>
  </svg>
  <!-- Las anotaciones se superponen usando posicionamiento absoluto HTML -->
  <span style="position:absolute; left:12.5%; top:25%; font-size:14px; color:#fff;">720</span>
  <span style="position:absolute; left:12.5%; bottom:5%; font-size:12px; color:rgba(255,255,255,0.6);">Versión Estándar</span>
</div>
```

```html
<!-- Prohibido: El SVG text se desplazará en PPTX -->
<svg viewBox="0 0 660 340">
  <rect x="80" y="100" width="60" height="200" fill="#FF6900"/>
  <text x="110" y="90" text-anchor="middle" fill="#fff">720</text>
</svg>
```

### 2.2 Mezcla de Diferentes Tamaños de Fuente -- Debe usarse elementos flex independientes

**Problema**: El anidamiento de fuentes grandes y pequeñas (`<div class="big">3.08<span class="small">s</span></div>`) se convierte en tspan independientes a través de dom-to-svg. Luego svg2pptx da a cada tspan un desplazamiento de línea base (baseline) basado en sus respectivos tamaños de fuente, causando que la fuente pequeña se desplace hacia arriba.

```html
<!-- Correcto: Alineación baseline con flex -->
<div style="display:flex; align-items:baseline; gap:4px;">
  <span style="font-size:48px;">3.08</span>
  <span style="font-size:18px;">s</span>
</div>
```

```html
<!-- Prohibido: Anidamiento de span con diferentes tamaños de fuente -->
<div class="big">3.08<span class="small">s</span></div>
```

### 2.3 Gráfico de Anillo (Barra de progreso circular) -- Dibujar arco SVG + Superponer texto HTML

```html
<!-- Correcto: Mejor práctica para gráfico de anillo -->
<div class="ring-container" style="position: relative; width:120px; height:120px;">
  <!-- SVG solo dibuja el arco del anillo -->
  <svg viewBox="0 0 120 120" style="width:100%; height:100%;">
    <!-- Círculo base -->
    <circle cx="60" cy="60" r="50" fill="none" stroke="rgba(255,255,255,0.1)" stroke-width="8"/>
    <!-- Arco: Usar formato de dos valores en dasharray, prohibido dashoffset -->
    <circle cx="60" cy="60" r="50" fill="none" stroke="#FF6900" stroke-width="8"
            stroke-dasharray="235 314" stroke-linecap="round"
            transform="rotate(-90 60 60)"/>
  </svg>
  <!-- El texto central usa superposición HTML, no uses SVG text -->
  <div style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%); text-align:center;">
    <div style="font-size:22px; font-weight:700; color:#fff;">15</div>
    <div style="font-size:10px; color:rgba(255,255,255,0.6);">minutos</div>
  </div>
</div>
```

### 2.4 Etiquetas de Leyenda -- Usar diseño HTML flex

```html
<!-- Correcto: Leyenda HTML flex, no uses SVG text -->
<div style="display:flex; gap:16px; font-size:12px;">
  <div style="display:flex; align-items:center; gap:4px;">
    <span style="display:inline-block; width:12px; height:12px; background:#999; border-radius:2px;"></span>
    <span style="color:rgba(255,255,255,0.6);">SU7 Original</span>
  </div>
  <div style="display:flex; align-items:center; gap:4px;">
    <span style="display:inline-block; width:12px; height:12px; background:#FF6900; border-radius:2px;"></span>
    <span style="color:rgba(255,255,255,0.6);">Nueva Generación SU7</span>
  </div>
</div>
```

### 2.5 Etiquetas del eje x (Estándar/Pro/Max) -- Usar contenedor HTML

```html
<!-- Correcto: Etiquetas del eje x usan HTML -->
<div style="display:flex; justify-content:space-around; padding:0 10%;">
  <span style="font-size:13px; color:rgba(255,255,255,0.6);">Estándar</span>
  <span style="font-size:13px; color:rgba(255,255,255,0.6);">Pro</span>
  <span style="font-size:13px; color:rgba(255,255,255,0.6);">Max</span>
</div>
```

---

## 3. Rutas de Imágenes

| Escenario | Uso Incorrecto | Uso Correcto |
|------|---------|---------|
| Referencia de `img src` | Depender de la resolución del navegador | html2svg resuelve rutas relativas basadas en el directorio donde se encuentra el archivo HTML |
| CSS `background-image` | Será ignorado por dom-to-svg | Usar etiqueta `<img>` |

---

## 4. Atributos del Gráfico de Anillo SVG `circle`

| Atributo | Soporte de svg2pptx | Descripción |
|------|-------------|------|
| `stroke-dasharray="arco hueco"` | Soportado | Usar dos valores: longitud del arco + longitud del espacio |
| `stroke-dashoffset` | **No soportado** | Prohibido su uso, cambiar a formato de dos valores de dasharray |
| `stroke-linecap="round"` | Soportado | Extremos del arco redondeados |
| `transform="rotate(-90 cx cy)"` | Soportado | Empezar desde la dirección de las 12 en punto |

Forma correcta de escribir el arco: `stroke-dasharray="235 314"` (Longitud del arco=235, Circunferencia=2*pi*50=314)

---

## 5. Imagen de Atmósfera de Fondo

| Ítem | Regla |
|------|------|
| opacity | 0.05 - 0.10 (dentro de tarjeta) / 0.25 - 0.40 (página de portada) |
| Tamaño | Limitado al 40-60% del contenedor, no cubrir completamente |
| z-index | Debe ser 0 o -1 |
| Método de implementación | Opacity muy bajo: Directamente `<img>` + opacity |
| | Desvanecimiento de nivel de portada: Contenedor `<div>` con img + div de máscara |
| **Prohibido** | Cuando la superposición de div de máscara en PPTX no sea confiable, recurrir a puro opacity |

---

## 6. Nivel de Seguridad de la Pipeline en Técnicas de Ilustración

| Técnica | Seguridad de Pipeline | Razón |
|------|---------|------|
| Fusión con desvanecimiento (div de máscara) | Segura | Div real + linear-gradient |
| Máscara de tono | Segura | Div real + fondo semitransparente |
| Imagen de atmósfera de fondo | Más Segura | Puro opacity |
| Recorte de ventana | Segura | overflow:hidden + div gradiente |
| Recorte circular | Segura | border-radius |
| ~~CSS mask-image~~ | **Prohibido** | dom-to-svg no lo soporta |

---

## 7. Conclusión: Checklist Antidesplazamiento de Diseño HTML

Al generar el HTML de cada página, verifica esta lista:

- [ ] Ninguna de las características de la Lista de Prohibiciones CSS ha sido usada
- [ ] Todas las imágenes usan etiqueta `<img>`, no se usa CSS background-image
- [ ] Los SVG en línea **no contienen elementos `<text>`**, todas las anotaciones de texto usan superposición HTML div
- [ ] La mezcla de diferentes tamaños de fuente usa flex + span independiente, no span anidados
- [ ] Los gráficos de anillo usan formato de dos valores stroke-dasharray, no dashoffset
- [ ] Leyendas, etiquetas de eje x y anotaciones de datos utilizan elementos HTML en su totalidad, no SVG text
- [ ] Las imágenes de fondo usan un `<img>` de bajo opacity o div de máscara
- [ ] La decoración de pseudoelementos `::before`/`::after` ha sido reemplazada por elementos reales
