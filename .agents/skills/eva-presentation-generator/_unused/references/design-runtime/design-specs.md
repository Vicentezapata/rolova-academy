# Especificaciones de diseño (A/B/C/D/E - referencia estable)

> Este documento contiene especificaciones del lienzo, escala de diseño, reglas de la tarjeta, decoración de colores, diseño del tipo de página y especificaciones de salida.
> El contenido es estable y no necesita ocupar un lugar en el contexto LLM cada vez, y el ensamblador lo inyecta mecánicamente.

---

## A. Lienzo y composición tipográfica

### Especificación del lienzo (no se puede modificar)

- Tamaño fijo: ancho=1280px, alto=720px, desbordamiento=oculto
- Área de título: margen superior izquierdo de 40 píxeles, y = 20 ~ 70, altura máxima de 50 píxeles (las páginas de portada/sección/final pueden manejar títulos libremente y no están sujetas a esta restricción)
- Área de contenido: relleno 40 px, y a partir de 80 px, altura disponible 580 px, ancho disponible 1200 px
- Área de pie de página: margen inferior de 40 px, altura de 20 px

### Contrato esqueleto de navegación unificada (obligatorio para todas las páginas)

**Por qué se necesita un esqueleto unificado**: Cada página es generada por un PageAgent independiente. Si la estructura HTML del área de título y pie de página no está unificada, la presentación final ensamblada tendrá problemas con el título/pie de página teniendo diferentes formas y posiciones erráticas. El siguiente esqueleto es un contrato mínimo para mantener la coherencia visual en toda la plataforma.

#### Clasificación de páginas y reglas de aplicación del esqueleto.

| tipo_página | Esqueleto del área de título | Esqueleto del área de pie de página | Descripción |
|-----------|-----------|-----------|------|
| `contenido` | **Forzar el uso** de la estructura unificada a continuación | **Forzar el uso** de la estructura unificada a continuación | La página de texto necesita una experiencia de navegación consistente |
| `toc` | **Obligatorio** | **Obligatorio** | Las páginas de índice también requieren encabezados y pies de página |
| `portada` | **Procesamiento gratuito** (el título es el evento visual principal) | **Opcional** (la información de la marca se puede colocar libremente) | El título de la portada es protagonista del diseño y no está limitado por el esqueleto |
| `sección` | **Tratamiento gratuito** (el título del capítulo es el único protagonista) | **Uso obligatorio** | El título de la sección se puede utilizar libremente, pero el pie de página permanece unificado |
| `fin` | **Procesamiento gratuito** | **Opcional** | Espejo de cierre de página final, alto grado de libertad |

#### Esqueleto HTML del área de título unificado (aplicable a páginas de contenido/común)

```html
<!-- 标题区：position:absolute 钉在画布顶部，所有 content/toc 页共用相同结构 -->
<header class="slide-header">
  <span class="overline">PART 0{{part_number}} &mdash; {{part_title}}</span>
  <h1 class="page-title">{{page_title}}</h1>
</header>
```

```css
.slide-header {
  position: absolute;
  top: 20px; left: 40px; right: 40px;
  height: 50px;
  display: flex;
  align-items: baseline;
  gap: 16px;
  z-index: 10;
}
.overline {
  font-size: 10px; font-weight: 700;
  letter-spacing: 2px; text-transform: uppercase;
  color: var(--accent-1); opacity: 0.8;
  white-space: nowrap;
}
.page-title {
  font-size: 26px; font-weight: 700;
  color: var(--text-primary);
  line-height: 1.2;
  margin: 0;
}
```

> **Espacio libre creativo**: el contenido de la línea superpuesta (número de pieza/etiqueta de marca/espacio en blanco), el tamaño de fuente específico y la línea decorativa del título de la página, y la relación posicional entre el título y la línea superpuesta pueden cambiar según el estilo. Sin embargo, la estructura HTML (`header.slide-header > span.overline + h1.page-title`) y el método de posicionamiento (`position:absolute; top:20px`) deben estar unificados en toda la plataforma. **

#### Esqueleto HTML del área de pie de página unificada (aplicable a las páginas de contenido/toc/sección)

```html
<!-- 页脚区：position:absolute 钉在画布底部，全 deck 统一结构 -->
<footer class="slide-footer">
  <span class="footer-section">{{section_label}}</span>
  <span class="footer-page">{{current_page}} / {{total_pages}}</span>
</footer>
```

```css
.slide-footer {
  position: absolute;
  bottom: 12px; left: 40px; right: 40px;
  height: 20px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 10;
}
.footer-section {
  font-size: 10px; color: var(--text-secondary);
  opacity: 0.5; letter-spacing: 1px;
}
.footer-page {
  font-size: 10px; color: var(--text-secondary);
  opacity: 0.5;
}
```

> **Espacio libre para la creatividad**: el contenido del pie de página se puede reemplazar con un pie de página narrativo (técnica W12) para mostrar el contenido de `.footer-section` (como barra de estado de terminal, insignia de sello, barra de progreso), pero la **estructura HTML (`footer.slide-footer`) y el método de posicionamiento (`position:absolute; bottom:12px`) deben estar unificados en toda la plataforma. ** Si el estilo del pie de página se especifica en `decoration_dna.signature_move` de style.json, se ejecutará primero.

### Escalera de composición tipográfica (desplegando las capas; el contraste del tamaño de fuente es el indicador central del poder del diseño)

| Nivel tipográfico | Tamaño de fuente sugerido | Peso de fuente | Descripción de la aplicación |
|---|---|---|---|
| Titular de la exhibición (H0) | `80px` - `160px` | `900` | Números KPI grandes, citas, cubierta superior, impacto puro |
| Título de la página (H1) | `32px` - `48px` | `800` | El foco del título de cada página (Página H1) |
| Título de la sección (H2) | `24px` - `28px` | `700` | El nombre en clave de cada cuadrante, el título de la tarjeta principal |
| Título de la tarjeta (H3) | `16px` - `20px` | `600` | El título de la información de la tarjeta secundaria |
| Texto principal (P) | `14px` | `400` | La explicación y el texto del párrafo |
| Etiqueta auxiliar (S) | `10px` - `12px` | `700` | Subtítulo, etiqueta superior, nombre de fuente, decoración |

> **Excelente punto de tensión para el contraste del tamaño de fuente**: Se recomienda que la **relación múltiple del tamaño de fuente máximo al tamaño de fuente mínimo por página sea mejor >= 5 veces**.

### El espaciado es una variable de sentimiento (al menos 2 espacios diferentes por página)

| Relación de contenido | Espaciado |
|---------|------|
| Número + anotación (estrecha simbiosis) | espacio: 2-4px |
| Entre cartas del mismo grupo | espacio: 16-20px |
| Diferentes áreas temáticas | espacio: 32-48px |
| Argumento central aislado | relleno: 48-80px |

### Nivel de diseño: disciplina absoluta y libertad ilimitada en la "Sección Yin-Yang"

> "Lo que parece el caos de un loco en la superficie se debe a la estricta disciplina subyacente que lo controla todo"

1. **El esqueleto es una dimensión física poderosa**: `layout_hint` restringe la distribución de la gravedad y el orden espacial de los componentes de la página. Puede elegir una tecnología de implementación excelente (Grid/Absolute), pero la estructura final debe obedecer a este sistema esqueleto.
2. **Esfuércese por crear tensión dentro de los grilletes** -- Aunque el chasis esquelético puede estar centrado y simétrico, en términos de expresión visual, introduzca audazmente sombras pesadas asimétricas en un lado, pasos de tamaño de fuente exagerados de gran tamaño y bloques de colores gráficos de gran tamaño para arrancar con fuerza el contraste primario y secundario en la imagen.
3. **Transgresión radical para eliminar la sensación de caja** -- Al romper el límite visual, no se debe lograr destruyendo el nivel anidado del DOM. ¡Debe utilizar el margen negativo del subelemento (margen superior: -30 px), la penetración y fusión del sombreado y el difuminado de vidrio esmerilado de gran área para deconstruir esta sensación aburrida!
4. **Apriete estructural y liberación visual de diferentes páginas**:
   - **Portada/Capítulo/Página final**: Sistema de coordenadas absolutas extremadamente estricto + **Tamaño de fuente grande extremadamente ilimitado y profundidad de campo sin fondo**.
   - **Página con uso intensivo de datos**: matriz de tarjetas de cuadrícula extremadamente rígida + **número súper KPI flotante extremadamente arrogante y sin restricciones**.
   - **Página narrativa**: basada en la piedra angular de Flex + superposición desinhibida de gráficos y texto lleno de historia.

#### Medios legales para eliminar la sensación de caja (disturbios visuales internos)

> **El resultado final a seguir y el privilegio de dejarlo ir**: El **contenido de texto específico de la tarjeta** no debe desbordarse y causar un desastre (use `overflow:hidden` y `line-clamp` para truncar). Sin embargo, el propio embalaje de la tarjeta (decoración, imagen base, bordes) puede romper la distancia segura de impresión a voluntad, chocar en ángulo o incluso perforarse y empalmarse entre sí. Eres el tirano intransigente del lienzo visual.

**Se anima a utilizar armas de rendimiento que rompan los límites**:

```css
/* 负 margin 叠压 */ .card-overlap { margin-top: -20px; position: relative; z-index: 3; }
/* 出血定位 */ .bleed-element { position: absolute; left: -40px; width: calc(100% + 80px); }
/* 斜切裁剪 */ .card-sliced { clip-path: polygon(0 0, 100% 0, 100% 90%, 0 100%); }
/* 绝对定位 */ .card-free { position: absolute; top: 120px; left: 60px; width: 480px; }
/* 跨区域装饰 */ .deco-cross { position: absolute; z-index: 5; pointer-events: none; }
/* 背景色融合 */ .card-merged { background: transparent; border-right: 1px solid var(--card-border); }
```

**Signos de diseño basado en plantillas (que indican que el diseñador está utilizando plantillas en lugar de diseñar para el contenido)**:
- El esqueleto del diseño de varias páginas consecutivas es exactamente el mismo (el diseño debe depender del contenido, no de los hábitos).
- La estructura visual de todas las páginas de contenido es "título + N tarjetas del mismo tamaño dispuestas". Esto no es un diseño, es un documento de Word.
- Las tarjetas en cada página usan las mismas esquinas redondeadas, relleno y sombras, lo que indica que el diseñador está copiando y pegando en lugar de pensar.
- La posición espacial de cualquier elemento no refleja la relación primaria y secundaria del contenido.

### Arquitectura de profundidad de campo de cinco capas

| capas | índice z | contenido | CSS típico |
|----|---------|------|----------|
| **Capa de fondo L0** | 0 | Color de fondo/gradiente/mapa base de atmósfera | `fondo`, `imagen-de fondo` |
| **Capa de sombreado decorativo L1** | 1 | Marca de agua que rompe límites (T1), penetración de sombreado (T6) | `posición:absoluta`, opacidad 0.03-0.08 |
| **Capa portadora de contenido L2** | 2 | Cuerpo de la tarjeta | Subelemento principal de cuadrícula |
| **L3 enfatiza la capa flotante** | 3 | tarjeta elevada/acento | `box-shadow`, `transform:translateY(-4px)` |
| **Capa de enfoque L4** | 4 | Número de datos muy grande (T2), punto de anclaje del pulso (T9) | `posición: relativa; índice z:4` |

Active al menos 3 capas por página.

### Puntos de anclaje de composición y líneas de movimiento visual.

| Líneas en movimiento | Páginas aplicables | Técnicas básicas de composición |
|------|---------|-------------|
| **Tipo Z** | Página de contenido estándar | Título superior izquierdo -> Datos superior derecho -> Argumento inferior izquierdo -> Conclusión inferior derecha |
| **Tipo F** | Lista/página con uso intensivo de texto | Barrido de título -> Escaneo rápido vertical |
| **Enfoque de radiación** | Página de datos únicos/oración de oro | El foco está centrado o descentrado y la decoración se extiende hacia afuera desde el foco.

**Regla de los anclajes de los tercios**: Los 4 puntos de intersección (aproximadamente 427,240 / 853,240 / 427,480 / 853,480) son puntos visuales fuertes. El centro del lienzo es la posición más aburrida.

### Espacio en blanco y enfoque visual

| Tipo de página | Tasa de llenado de contenido |
|---------|----------|
| Portada | 40-55% |
| Portada del capítulo | 25-40% |
| Contenido estándar | 60-75% |
| Intensivo en datos | 70-80% |
| Página final | 35-50% |

---

## B. Contenido y tarjetas

### 3 Formas de presentar contenido denso (en lugar de copiar y pegar en un documento de Word)

No hagas que las tarjetas parezcan bloques de documentos estándar.

- **texto (bloque de texto)**: Si hay mucho texto, no seas directo. Extraiga la palabra más llamativa y colóquela en negrita, o utilice una letra mayúscula en la primera letra, que es similar al diseño de una revista.
- **datos (bloque de datos)**: evite simplemente "gráfico + leyenda". Utilice la oración final como el tamaño de fuente más grande y el gráfico se presenta silenciosamente a continuación como fondo.
- **lista (bloque de lista)**: abandona los puntos tradicionales de la lista desordenada. Puede utilizar números translúcidos grandes, bloques de color punteados con colores progresivos o incluso hacer que cada elemento de la lista esté ligeramente desalineado en el posicionamiento absoluto.
- **tag_cloud**: no organice las etiquetas en una matriz igualmente espaciada. Haga que las etiquetas importantes sean grandes y que las etiquetas sin importancia aparezcan.

### Variante visual de la tarjeta (card_style)

| Variante | Descripción de características | Escenario aplicable |
|---------|---------|---------|
| `base` | Tarjeta estándar, fondo de color sólido + esquinas redondeadas + sombra débil | General |
| `acento` | Fondo de color acentuado, sombra fuerte, el más llamativo | Solución recomendada o la métrica más importante |
| `vidrio` | Vidrio esmerilado, transparente, resalta la imagen trasera | La imagen es la protagonista de la página |
| `esquema` | Sin color de fondo, solo bordes + sombreado muy claro | Tarjeta de bajo peso, contraste o elemento antiguo |
| `invisible` | Totalmente sin recipiente (los datos puros quedan al descubierto) | El número se agranda y se suspende (T2 + W9a) |

### Arsenal de microdetalles (evitando la homogeneidad)

¿Cómo se consigue que una tarjeta parezca pulida en lugar de toscamente elaborada?

- **Rompe los bordes duros**: utiliza líneas borrosas con degradado para reemplazar el borde sólido rígido. 
- **Elementos embellecidos**: agregue un texto mínimo de 10 píxeles similar a la marca de la esquina de la interfaz de usuario en el borde de la tarjeta para indicar "fuente" o "peso".
- **Resaltado heterogéneo**: no uses negrita solo para palabras importantes, intenta agregar un color de acento con una pastilla de fondo o incluso líneas onduladas.

**La regla del minimalismo**: Los espacios en blanco extremos y la alineación absoluta son en sí mismos una especie de detalle de alto nivel con gran tensión. No acumule a la fuerza efectos especiales sofisticados en una página.

### Reglas para la combinación y disposición de tarjetas

| Modo ritmo | Escenarios aplicables |
|---------|---------|
| **Principal y Auxiliar** | 1 núcleo + 2-3 auxiliares, el núcleo representa 2fr |
| **Decreciente** | De importancia cada vez menor, el primero se extiende por 2 columnas |
| **Escalonado** | Igual de importante pero necesita sentido del ritmo |
| **Isla + Comunidad** | El núcleo ocupa el 40-60% y los grupos auxiliares están estrechamente organizados |

**Evita la igualdad**: No tengas todas las tarjetas alineadas en una fila del mismo ancho y alto.

---

## C. Color y decoración

### 60-30-10 Ritmo de color

| Proporción | Rol | Ámbito de aplicación |
|------|------|---------|
| 60% | Color primario (fondo) | --bg-primario |
| 30% | Color secundario (área de contenido) | --card-bg-desde/hasta |
| 10% | Color de acento (adornado) | --acento-1 ~ --acento-4 |

> 1 o 2 colores de acento en la misma página funcionan mejor. Los requisitos de varios colores (como tag_cloud) pueden usar de manera flexible acento-1 a acento-4.

### Elementos decorativos

2-3 decoraciones por página. Proviene del borrador de planificación tridimensional `decoration_hints`.

### Sistema de navegación (esqueleto unificado + estilo libre)

La **estructura HTML y la ubicación de la información auxiliar inferior (capítulo, número de página, marca) deben utilizar el esqueleto del área de pie de página unificado** ("footer.slide-footer") definido en la Sección A, pero el **estilo visual** dentro del esqueleto se puede diversificar: pie de página narrativo (barra de estado/sello/barra de progreso del terminal W12), microtexto mínimo, énfasis en el color de acento, etc. Los cambios de estilo se logran reemplazando el contenido de `.footer-section` y modificando el fuente/color/opacidad sin cambiar la estructura del esqueleto.

### Pautas de uso de degradado

- Mantenga la dirección del degradado armoniosa en la misma página
- El color del degradado toma valor de la variable CSS

### Color y legibilidad

-El contraste entre el texto y el fondo sigue siendo legible.
- Se prefieren los colores de acento para títulos/etiquetas/datos, no para grandes secciones de texto
- Se hace referencia a los colores primero a través de `var(--xxx)`

### Caracteres especiales

Utilice `°C` para temperatura, `<sub>`/`<sup>` para fórmulas químicas y `μm` para micrómetros.

---

## D. Concepción artística avanzada del tipo de página (implementada mediante código seguro)

La siguiente exhibición de concepción artística de alto nivel no es una divergencia desenfrenada, sino un método de ingeniería frontal pesado que puede utilizar cuando el planificador emite instrucciones de expresión extremadamente fuertes (como: opresión espacial, profundidad de campo infinita, convergencia extrema). El requisito previo para su implementación es estabilizar el modelo de caja subyacente y calcular con precisión las coordenadas, y evitar que la composición colapse debido a la "búsqueda de efectos especiales":

### Tensión de la portada
- Intenta abandonar el centrado. Haga que el título esté cerca de la línea de sangrado izquierda, o incluso use un tamaño de fuente muy grande (160 px) para abarcar directamente dos líneas.
- Pruebe la profundidad de campo "sin fondo": el fondo no es solo un color, también puede ser una enorme marca de agua con el ícono de una marca o un código inminente.

### Índice de contenidos y transiciones (capítulos)
- Pruebe más del 70 % de espacios en blanco extremos para las páginas de los capítulos. El título es extremadamente parcial.
- Intente utilizar números de contorno como patrones: números muy grandes (por ejemplo, 120 píxeles), opacidad muy baja (0,04), que cubran todo el lado.

### Intensivo de datos y panel de control
- No pongas todos tus datos en una casilla. Intente hacer que el KPI principal esté "fuera del marco" (completamente sin el aislamiento del color de fondo y el borde), exponiendo directamente 120 píxeles en la imagen.
- Reduzca mucho los datos secundarios (el tamaño de fuente secundaria de 28 px crea un fuerte contraste con el tamaño de fuente fuera del marco de 120 px).

### Análisis comparativo y selección.
- Romper la simetría o colocarlos uno al lado del otro. La solución recomendada puede "abultarse" como una roca (múltiples sombras, halo fuerte), mientras que la solución abandonada se agazapa en el fondo como una sombra.
- No es necesario trazar una línea vertical en el medio. Puede utilizar cintas degradadas diagonales para dividir el espacio en ambos lados.

### Introducción y narrativa
- Trate la cita como una obra de arte, colóquela en el centro de una pantalla completamente en blanco y coloque una transparencia muy baja a modo de eco.

### Página final
- No escribas simplemente "gracias". Puede ser el reflejo final de la portada: el mismo tono y composición, con elementos que van desde la extrema extravagancia hasta la extrema moderación.

---

## E. Especificación de salida

### Referencia de esqueleto HTML

```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=1280">
<title>Slide {NN} - {TITLE}</title>
<style>
:root { /* 从 style.json 展开完整 CSS 变量 */ }
*, *::before, *::after { margin:0; padding:0; box-sizing:border-box; }
body {
  width:1280px; height:720px; overflow:hidden;
  background: var(--bg-primary);
  font-family: 'PingFang SC', 'Microsoft YaHei', system-ui, sans-serif;
  position:relative; color:var(--text-primary);
}
</style>
</head>
<body>
<!-- 统一标题区（content/toc 页强制；cover/section/end 页按 A 节规则自由处理） -->
<header class="slide-header">
  <span class="overline">PART 01 &mdash; 章节标题</span>
  <h1 class="page-title">页面标题</h1>
</header>

<!-- 内容区从这里开始 -->

<!-- 统一页脚区（content/toc/section 页强制；cover/end 页可选） -->
<footer class="slide-footer">
  <span class="footer-section">章节标签</span>
  <span class="footer-page">3 / 12</span>
</footer>
</body>
</html>
```

### Leyes físicas invisibles (5 líneas rojas técnicas)

| # | Leyes de la Física | Significado del diseño |
|---|--------|------|
| 1 | Lienzo de 1280x720px, `desbordamiento del cuerpo: oculto` | El límite del lienzo es la ventana gráfica |
| 2 | Unidad global de la "familia tipográfica" | piedra angular del orden |
| 3 | Variables CSS globalmente dependientes | Color encerrado en el mismo universo |
| 4 | El texto en el contenedor no se desborda (`overflow:hidden` + `line-clamp`) | La carcasa del contenedor se puede mover y apilar a voluntad |
| 5 | Utilice únicamente elementos visuales estáticos puros (sin `@keyframes`/`animation`/`transition`) | La exportación PPTX no admite animaciones |

### Lanzamiento de capacidad CSS

De uso gratuito: `fondo-clip:text` / `clip-path` / `mask-image` / `conic-gradient` / `backdrop-filter` / `mix-blend-mode` / multicapa `box-shadow` / pseudo-elemento / `writing-mode` / `filter`. No permitir `@keyframes`/`animación`/`transición`.

### Tendencias de diseño

| Tendencia a la mediocridad | Mejores opciones |
|---------|----------|
| Título `text-align:center` | Posicionamiento descentrado + línea decorativa |
| Todas las tarjetas tienen el mismo relleno | El núcleo es más grande y el auxiliar más compacto |
| Página completa `flex; centro; centro` | Regla de los tercios excentricidad + tensión diagonal |
| Todas las tarjetas son del mismo tamaño y altura | Ritmos principales y secundarios / decrecientes / isla + comunidad |
| Utilice solo 1 capa de box-shadow | 3-4 capas de sombra progresiva |