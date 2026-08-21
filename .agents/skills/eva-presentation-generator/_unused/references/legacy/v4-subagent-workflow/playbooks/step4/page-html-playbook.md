# Page HTML Playbook -- 单页 HTML 设计稿

## Objetivo

Restaure fielmente el esqueleto y el espíritu de planificación JSON y utilice las capacidades de análisis de `resource_loader.py resolve` para ensamblar componentes abstractos en **HTML autónomo de una sola página** con un fuerte sentido de diseño avanzado.

---

## Fase 1: Comprensión del esqueleto (no se puede omitir)

Lea los siguientes campos de `planning{n}.json` como restricciones estrictas para esta etapa:

| Campos | Significado de la etapa HTML |
|------|--------------|
| `tipo_página` / `sugerencia_diseño` | Determinar el esqueleto general y la libertad de la página |
| `densidad_etiqueta` / `densidad_contrato` | Determinar si esta página es un modo de ejecución de alto o bajo grado de libertad |
| `zona_enfoque` | Determina qué tarjeta/zona debe tener el mayor peso visual |
| `objetivo_espacio_negativo` | Determine la proporción de espacios en blanco (alto=suelto/medio=moderado/bajo=denso)|
| `tarjetas[].role` / `tarjetas[].card_style` | Determinar el orden de prioridad y presencia de la tarjeta |
| `tarjetas[].card_id` | Se implementarán uno por uno en HTML y se asignarán a `data-card-id` |
| `tarjetas[].content_budget` | Limite la capacidad de carga de cada tarjeta para evitar el desbordamiento |
| `director_command` / `decoration_hints` | Determinar la sensación de la cámara, el nivel de decoración y los límites de implementación |
| `source_guidance` / `must_avoid` | Determinar cómo se presentan las pruebas y acciones prohibidas |
| `imagen.modo` | Siga estrictamente la cláusula 3 a continuación |

---

## Fase 2: Consumo del cuerpo de recursos (obligatorio, no se puede omitir)

```bash
python3 SKILL_DIR/scripts/resource_loader.py resolve --refs-dir REFS_DIR --planning PLANNING_OUTPUT
```

El script devuelve la implementación de cuerpo completo de cada recurso al que se hace referencia en la planificación, que contiene:
- Esqueleto estructural HTML del componente (incluidos ejemplos de nombres de clases)
- Parámetros CSS recomendados (espaciado, tamaño de fuente, uso de variables de color)
- Requisitos de formato de datos (como formato de datos de gráficos)

**Debes tratar esto como un esqueleto subyacente insuperable. Basado en este esqueleto, puede mejorarlo con técnicas expresivas avanzadas (como el procesamiento espacial CSS), pero está absolutamente prohibido desviarse o destruir la disposición lógica de la estructura original. La revisión de imágenes solo interceptará errores y no reconstruirá el esqueleto caótico por usted. **

Atención especial:
- Aunque resolve proporciona la estructura básica, debes alinear estrictamente la lógica espacial dada por el `layout_hint` original. Puede mejorarlo con CSS más moderno y sofisticado, pero nunca se admite "destruir-reconstruir".
- Se permite optimizar la visión bajo la premisa de alinear y restaurar perfectamente el esqueleto de diseño, pero no intentar desafiar la prioridad de datos originalmente planificada en este momento.
- `proceso`, un tipo_tarjeta que no tiene un archivo de bloque independiente, debe utilizar una estructura DOM nativa sólida combinada con técnicas de diseño rigurosas para heredarla, y está prohibido destruir arbitrariamente el flujo de lectura establecido.

### Modo de ejecución de densidad (debe obedecer)

- `low / mid_low`：高自由度，可使用更强的留白、图片和材质变化
- `medium`：中自由度，允许有设计表达，但不能破坏阅读秩序
- `high / dashboard`：低自由度，只能做稳态 grid / flex 骨架，优先表格、矩阵、微图表，禁止依赖复杂绝对定位硬塞内容

**Línea Roja Especial**:
- `high/dashboard` desactiva la tarjeta visual principal con imagen grande
- El "panel de control" prohíbe las marcas de agua y las decoraciones de gran superficie que puedan dominar la ruta de lectura.
- `density_contract` es el contrato de construcción más alto, HTML no puede aumentar ni disminuir la densidad de esta página por sí solo

---

## Fase 3: el modo de imagen se aplica estrictamente

| modo.imagen | HTML para hacer | Absolutamente prohibido |
|-----------|-------------|----------|
| `generar` / `proporcionado` | Utilice la ruta `source_hint` para representar `<img src>` o `imagen de fondo: url()` | No utilice bloques de colores de marcador de posición para reemplazar la imagen real |
| `ranura_manual` | Representar un cuadro de marcador de posición de imagen con un tamaño claro (con borde punteado + descripción de texto "[Ranura de reemplazo de imagen]") | No debe eliminarse ni convertirse en un espacio en blanco invisible |
| `decorar` | Utilice SVG en línea, degradados CSS, bloques de colores geométricos, marcas de agua de caracteres grandes, decoraciones circulares y otros lenguajes visuales internos para complementar la atmósfera. No hay grandes agujeros en blanco ni `<div>` vacío |

Al mismo tiempo, cumpla estrictamente con `density_contract.image_policy`:
- `flexible`: puedes seleccionar imágenes libremente, pero aun así debes publicar page_goal
- `support_only`: Las imágenes solo se pueden utilizar como soporte y no como imágenes de fondo de página completa.
- `decorate_only`: no se deben renderizar imágenes externas, solo `decorar`

---

## Fase 4: Conciliación de tarjetas (obligatoria)

- Cada tarjeta en `planning.cards[]` debe tener un nodo raíz HTML correspondiente.
- Cada nodo raíz debe tener `data-card-id="<card_id>"` para facilitar la conciliación entre la etapa de Revisión y la planificación.
- La tarjeta con `rol = ancla` debe convertirse en el primer punto de aterrizaje visual de toda la página; El `apoyo/contexto` retrocede pero no puede desaparecer.
- Cualquier **nodo de decoración pura** debe tener `data-decoration-layer="background|floating|page-accent"` y escribir `aria-hidden="true"` al mismo tiempo; `visual_qa.py` contabilizará directamente el presupuesto de decoración según esta marca.
- Si la tarjeta tiene `chart.chart_type`, el tipo de gráfico final debe ser coherente con la planificación; no reemplace `comparison_bar` con una lista normal.
- Si `source_guidance` requiere que se conserve la fuente, al menos proporcione una pista de la fuente en el pie de página/título/espacio de comentarios de la tarjeta.
- El número de tarjetas, gráficos y filas por tarjeta no debe exceder el límite de presupuesto de "density_contract".
- **【Limpieza antifugas】**: Cuando completas el `cuerpo` y el `título` en JSON en las etiquetas HTML, si lees **"narración", "acciones de composición tipográfica"** obvias (por ejemplo: "Esta página primero prepara el escenario y finalmente concluye con la conclusión" y otras tonterías), ¡honestamente no tienes permitido renderizarlo en la pantalla grande! ** Esta es la instrucción del director que el agente de planificación previa omitió. ¡Debes actuar activamente como el último firewall para eliminarlo directamente o reescribirlo tú mismo en una copia seca!

---

## Fase 5: Línea roja física del lienzo (no se puede violar)

```css
* {
  box-sizing: border-box; /* 像素级排版防崩核心 */
}

body {
  width: 1280px;
  height: 720px;
  overflow: hidden;
  margin: 0;
  padding: 0;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; /* 保障文字渲染精度 */
}
```

**像素级渲染安全防线（涉及无头浏览器最终出图质量，极度重要）：**
- **流体坍缩预防**：在高度自由发挥时，`flex` / `grid` 极易出现子项挤压坍缩。凡Sí重要卡片或必须撑开的区域，务必使用 `min-width`, `min-height` 或 `flex-shrink: 0`。
- **行高裁剪预防**：文字的 `line-height` 若低于 `1.3`，部分英文小写字母下端极其容易被隐形裁剪，正文需保持合理行高。
- **边框与阴影溢出**：所有的边框宽度、`box-shadow` 都可能溢出原有容器。借助于 `box-sizing: border-box`，确保 padding 和 border 在规划宽度内。
- **密度合同预防**：正文最小字号不得低于 `density_contract.min_body_font_px`；如果放不下，先减装饰，再收紧预算，再回退 planning，不得偷缩到不可读。

- **禁止** `width: 100%; height: 100%` 然后依赖父容器
- **禁止** `transform: scale()` 缩放 hack
- **禁止** 引用外部 CSS 文件（如 `common.css`、`deck.css`）

### Esqueleto de navegación unificado (obligatorio, para garantizar la coherencia visual en toda la plataforma)

每个页面由独立的 PageAgent 生成，**必须**使用统一的标题区和页脚区 HTML 骨架，避免拼装后各页标题/页脚形态各异。骨架规范详见 `design-specs.md` A 节「统一导航骨架合同」，核心规则如下：

| tipo_página | área de título | área de pie de página |
|-----------|--------|--------|
| `contenido` / `toc` | **Obligatorio** `header.slide-header > span.overline + h1.page-title`, `posición:absoluta; arriba: 20px` | **Obligatorio** `pie de página.pie de página`, `posición:absoluta; abajo: 12px` |
| `sección` | **Gratis** (el título de la sección es el diseño protagonista) | **Obligatorio** Igual que el anterior |
| `portada` / `fin` | **Gratis** | **Opcional** |

**视觉创意不受影响**：overline 内容、page-title 字号、装饰线、页脚风格（W12 终端/印章/进度条）都可按风格变化。统一的只Sí **HTML 结构和定位方式**。

---

## Fase 6: las variables de estilo están estrictamente vinculadas

Extraiga todas las variables de `css_variables` de `style.json` y escríbalas en `:root` de HTML:

```css
:root {
  --bg-primary: [从 style.json 取];
  --bg-secondary: [从 style.json 取];
  --card-bg-from: [从 style.json 取];
  --card-bg-to: [从 style.json 取];
  --card-border: [从 style.json 取];
  --card-radius: [从 style.json 取];
  --text-primary: [从 style.json 取];
  --text-secondary: [从 style.json 取];
  --accent-1: [从 style.json 取];
  --accent-2: [从 style.json 取];
  --accent-3: [从 style.json 取];
  --accent-4: [从 style.json 取];
  --font-primary: [从 style.json font_family 取];
}
```

- `design_soul`: se utiliza para calibrar emociones y no se puede copiar directamente en la copia de la página.
- `variation_strategy`: controla el rango de variación de esta página para evitar la copia isomórfica con páginas adyacentes
- `decoration_dna.forbidden`: límite estricto, la violación significa falla automática
- `decoration_dna.recommended_combos`: preferido
- `decoration_dna.signature_move`: punto de anclaje de identificación entre páginas, debe aparecer
- `density_contract.decoration_budget`: Restringe el número de capas de decoración al mismo tiempo. Las recomendaciones de límite superior predeterminadas son: `generoso <= 6`, `medio <= 4`, `bajo <= 2`, `mínimo <= 1`

---

## Fase 7: Eres el arquitecto con mejor desempeño

> **Concepto principal**: el JSON de planificación es su dibujo de ingeniería principal y el texto componente de la resolución de recursos es su molde. Su trabajo consiste en combinar CSS de alta precisión (sombras, filtros, recortes) para crear una representación final sorprendente respetando estrictamente el tamaño del dibujo y la configuración de espacio.

**Sus resultados arquitectónicos y privilegios de renderizado:**
- **Respete estrictamente el esqueleto**: nunca está permitido destruir el sistema estructural `layout_hint` y documentar el campo de gravedad definido por Planificación en una escala macro.
- **Libere el poder del renderizado**: los privilegios de implementación de CSS se le delegan por completo, al mismo tiempo que se garantiza una estructura sólida. Puede utilizar audazmente posicionamiento absoluto, filtros avanzados, degradados complejos y rutas de clip para esculpir tarjetas, y utilizar CSS para liberar la tensión expresiva ligada a los datos originales.
- **La densidad obedece a la prioridad**: la página "alta/panel" primero debe ser clara, estable y escaneable, y luego hablar sobre el rendimiento dramático. No se debe sacrificar la estructura en aras de la "frialdad".

**设计独立性自检（追问：我的执行SíNo精准且克制？）**：
- 本页的底层承重墙（DOM结构）与 `page_goal` 和 `director_command` 的原意做到了一比一还原吗？
- 视觉锚点的位置SíNo彻底捍卫了原设计稿中定义的信息主次？
- 严禁套模板的心理：不可直接拿通用结构的冗余代码应付了事，任何多余的包裹标签都Sí负面的。

**Restricciones de garantía básica**: Usted es el único responsable de este proceso de representación. El proceso de revisión es sólo la última línea de defensa para la inspección de calidad antes de salir de fábrica. No limpiará el desorden de una estructura caótica por ti. Todos los errores deben ser reparados por usted mismo.

---

## Fase 8: Condiciones de finalización

写入目标 HTML 文件后：
- 文件非空
- 格式绝对纯净：HTML 中不得以可见文本形式包含大模型思考过程（如阴阳自检、摘要阐述、策略说明等与实际幻灯片不相关的文字）
- 无语法错误（HTML 标签闭合完整）
- 没有明显乱码或缺失的 CSS 变量引用
- `planning.cards[]` 全部能在 HTML 中找到对应的 `data-card-id`

发送 FINALIZE 信号，然后等待 Review 阶段指令。
