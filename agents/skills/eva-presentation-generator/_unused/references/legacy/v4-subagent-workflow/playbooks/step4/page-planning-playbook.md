# Manual de estrategias de planificación de páginas: borrador de planificación de una sola página

## Objetivo

Desarrolle un plano detallado del formato físico de 1280x720 desde el diseño, las fuentes, la estrategia de imagen hasta la organización de la tarjeta. **En esta etapa solo se escribe JSON, no HTML. **

---

## Fase 1: comprender el posicionamiento actual de la página

Busque la definición en la página N de `outline.txt` y déjela clara:
- `page_goal`: el argumento central de esta página (una oración, sin la palabra "y")
- `narrative_role`: Rol narrativo (portada/toc/sección/evidencia/comparación/proceso/cerrar/cta)
- `proof_type`: método de argumento (basado en datos/caso/comparación/marco/paso)
- `límite inferior de densidad/objetivo de densidad/límite superior de densidad`
- `Acción de ritmo/Gesto de información/Tipo de anclaje`
- "Tendencia de densidad" a nivel de plataforma y el conjunto completo de "Curvas de densidad"

> **硬边界**：本阶段不Sí重新发明这一页的密度，而Sí把 outline 定下的窗口冻结成单页可执行的 `density_contract`。

---

## Fase 2: Descubrimiento de recursos y decisiones de diseño

Después de ejecutar `resource_loader.py menu` para obtener el menú de componentes disponibles, **Eres un arquitecto riguroso, no un pintor casual**. Es necesario comprender profundamente los tipos de datos físicos y conectar la pila de componentes sin problemas:

1. **观众在这一页应该先看到什么？** → 决定你的视觉锚点和主次关系
2. **这一页的信息Sí怎么“流动”的？** → 决定空间布局和视觉动线
3. **这一页和上一页的视觉感受应该有什么不同？** → 决定节奏变化
4. **在菜单中的工具里，哪些能最好地服务上面 3 个答案？** → 决定 layout_hint、card_type、chart、resource_ref

> **Importante**: Las herramientas del menú son su biblioteca de moldes industriales, no pinceles para graffiti casual. Aunque se pueden utilizar moldes de alto orden de forma transfronteriza para diferentes datos, la lógica debe ser coherente para evitar que el esqueleto colapse.

**Al completar el campo `recursos` debes explicar por qué seleccionaste este componente** (campo `resource_rationale`).

### 命名合同（必须区分 schema 枚举 与 资源文件 stem）

- `layout_hint` / `page_type`: Escribe el valor reconocido por el validador. `layout_hint` recomienda utilizar raíces de archivos reales, como `hero-top`, `mixed-grid`, `l-shape`.
- Las páginas que no son de `contenido` consumen preferentemente desde `page-templates/` hasta `page_type` (como `cover` / `toc` / `section` / `end`). Normalmente no es necesario escribir `layout_hint`; Solo complete `resources.page_template` adicionalmente cuando desee fijar explícitamente el cuerpo de la plantilla.
- `card_type`: escribe enumeraciones reconocidas por el validador, como `data_highlight`, `image_hero`, `matrix_chart`.
- `chart.chart_type`: escribe una enumeración reconocida por el validador, **nombre con guiones bajos**, como `metric_row`, `comparison_bar`, `stacked_bar`, `progress_bar`.
- `resources.*_refs` y `card.resource_ref.*`: se recomienda escribir raíces de archivos reales en `references/`, como `metric-row`, `comparison-bar`, `visual-hierarchy`; `resource_loader.py` automáticamente realizará la normalización de guiones bajos/guiones.
- `process` es el esquema nativo `card_type`, pero actualmente no hay `blocks/process.md`. Si lo usa, debe proporcionar los `layout_refs`, `principle_refs`, `director_command` y los `chart_refs`/`resource_ref` más fuertes, y no asumir que habrá un cuerpo de bloque dedicado para cargar.

### guía de principio_refs (importante: los archivos de principios de diseño se seleccionan según los escenarios)

El campo `resources.principle_refs[]` determina si la etapa HTML puede recibir el texto del principio de diseño. Complete de acuerdo con las siguientes reglas:

| Características de esta página | Debe citarse |
|---------|--------|
| Página principal del gráfico de datos | `visualización de datos` |
| El diseño de varias tarjetas requiere un sentido de jerarquía | `jerarquía-visual` |
| Portada/página de capítulo, necesita calibración del estado de ánimo | `psicología del color` |
| Información ultradensa, preocupada por la carga cognitiva | `carga cognitiva` |
| Narrativa pasando página (del problema a la solución) | `arco-narrativo` |
| Optimización del diseño y composición de cualquier página | `composición` |
| No estoy seguro de cuál elegir | `design-principles-cheatsheet` (verificación rápida completa) |

Ejemplo de escritura en planificación JSON:```json
"resources": {
  "principle_refs": ["visual-hierarchy", "composition"],
  "layout_refs": ["hero-top"],
  "block_refs": [],
  "chart_refs": ["kpi"]
}
```

Una vez completado, `resource_loader.py resolve` inyectará automáticamente el texto completo del archivo de política correspondiente en el contexto de la etapa HTML.

---

## Fase 3: Congelación del contrato de densidad (obligatorio)

### Cinco niveles de presupuesto básico

| `etiqueta_densidad` | `max_cards` | `max_charts` | `min_body_font_px` | `max_lines_per_card` | `política_imagen` | `presupuesto_decoración` | `estrategia_desbordamiento` |
|---|---:|---:|---:|---:|---|---|---|
| `bajo` | 2 | 1 | 24 | 3 | `flexibles` | `generoso` | `rebalance_layout` |
| `medio_bajo` | 3 | 1 | 20 | 4 | `flexibles` | `medio` | `rebalance_layout` |
| `medio` | 4 | 2 | 18 | 5 | `sólo_soporte` | `medio` | `apretar_presupuesto` |
| `alto` | 6 | 2 | 16 | 4 | `sólo_soporte` | `bajo` | `tabla_o_micrográfico` |
| `tablero` | 8 | 4 | 14 | 3 | `decorar_solo` | `mínimo` | `rollback_planning` |

### Reglas de congelación

- `density_label` debe estar entre el `límite inferior de densidad/límite superior de densidad` del contorno.
- `density_reason` debe explicar por qué esta página terminó en este archivo, en lugar de simplemente escribir "más contenido".
- `density_contract` debe escribirse explícitamente `deck_bias`, `page_lower_bound`, `page_upper_bound`, `max_cards`, `max_charts`, `min_body_font_px`, `max_lines_per_card`, `image_policy`, `decoration_budget`, `overflow_strategy`.
- El `panel` solo está permitido para páginas de `contenido` y tiene prioridad sobre `cuadrícula mixta`/`forma de T`.
- `high/dashboard` desactiva la tarjeta principal `image_hero`, desactiva la imagen grande `hero-background`.

## Fase 4: contrato de estructura `planningN.json` (obligatorio)

Su salida debe ser JSON que pueda validarse directamente mediante `planning_validator.py`. Aquí está el esqueleto del esquema (**solo muestra la estructura, no las decisiones de diseño**; el diseño, el tipo de tarjeta y el estilo visual dependen de usted):

```json
{
  "page": {
    "slide_number": "<页码>",
    "page_type": "<cover/toc/section/content/end>",
    "narrative_role": "<叙事角色>",
    "title": "<页标题>",
    "page_goal": "<一句话核心论点>",
    "audience_takeaway": "<观众带走什么>",
    "visual_weight": "<1-10 信息密度>",
    "density_label": "<low/mid_low/medium/high/dashboard>",
    "density_reason": "<为什么这一页最终落在这个密度档>",
    "density_contract": {
      "deck_bias": "<relaxed/balanced/ultra_dense>",
      "page_lower_bound": "<来自 outline 的密度下限>",
      "page_upper_bound": "<来自 outline 的密度上限>",
      "max_cards": "<整数>",
      "max_charts": "<整数>",
      "min_body_font_px": "<整数>",
      "max_lines_per_card": "<整数>",
      "image_policy": "<flexible/support_only/decorate_only>",
      "decoration_budget": "<generous/medium/low/minimal>",
      "overflow_strategy": "<rebalance_layout/tighten_budget/table_or_microchart/rollback_planning>"
    },
    "layout_hint": "<你的布局选择>",
    "layout_variation_note": "<与上一页的结构对比（如果有微调），要求详尽>",
    "focus_zone": "<视觉焦点区域描述>",
    "negative_space_target": "<high/medium/low>",
    "page_text_strategy": "<文字策略>",
    "rhythm_action": "<推进/爆发/缓冲/收束>",
    "must_avoid": ["<你认为这页最危险的平庸设计陷阱>"],
    "variation_guardrails": {
      "same_gene_as_deck": "<哪些元素跨页保持统一>",
      "different_from_previous": ["<与上一页的具体变化维度>"]
    },
    "director_command": {
      "mood": "<你为这页设定的情绪基调>",
      "spatial_strategy": "<你的空间编排策略>",
      "anchor_treatment": "<你怎么处理视觉锚点>",
      "techniques": ["<你选用的技法编号>"],
      "prose": "<用电影镜头语言描述这页的视觉感受>"
    },
    "decoration_hints": {
      "background": {"feel": "<>", "restraint": "<>", "techniques": ["<>"]},
      "floating": {"feel": "<>", "restraint": "<>", "techniques": ["<>"]},
      "page_accent": {"feel": "<>", "restraint": "<>", "techniques": ["<>"]}
    },
    "source_guidance": {
      "brief_sections": ["<素材引用路径>"],
      "citation_expectation": "<引用策略>",
      "strictness": "<证据边界>"
    },
    "resources": {
      "page_template": "<null 或页面模板 ref>",
      "layout_refs": ["<你的 layout ref>"],
      "block_refs": [],
      "chart_refs": ["<你选用的 chart ref>"],
      "principle_refs": ["<你需要的设计原则>"],
      "resource_rationale": "<为什么选这些资源，必须说明理由>"
    },
    "cards": [
      {
        "card_id": "<s页码-role-序号>",
        "role": "<anchor/support/context>",
        "card_type": "<你的卡片类型选择>",
        "card_style": "<你的视觉变体选择>",
        "argument_role": "<claim/evidence/context>",
        "headline": "<精炼标题>",
        "body": ["<正文字符串数组>"],
        "data_points": [{"label": "<>", "value": "<>", "unit": "<>", "source": "<>"}],
        "chart": {"chart_type": "<你的图表类型>"},
        "content_budget": {"headline_max_chars": 12, "body_max_bullets": 3, "body_max_lines": 5},
        "image": {
          "mode": "<generate/provided/manual_slot/decorate>",
          "needed": "<true/false>",
          "usage": "<null 或图片用途>",
          "placement": "<null 或放置位置>",
          "content_description": "<null 或描述>",
          "source_hint": "<null 或路径>",
          "decorate_brief": "<装饰说明>"
        },
        "resource_ref": {"chart": "<>", "principle": "<>"}
      }
    ],
    "workflow_metadata": {
      "stage": "planning",
      "workflow_version": "2026.04.09-v4.1",
      "planning_schema_version": "4.1",
      "planning_packet_version": "4.1",
      "planning_continuity_version": "4.1"
    }
  }
}
```

> **Recordatorio importante**: Cada uno de los marcadores de posición `<>` anteriores eventualmente aterrizará en un código sólido como una roca. Como ingeniero riguroso, debe producir dibujos de diseño y ensamblaje precisos basados ​​en el contenido, la audiencia y los límites físicos de esta página.

### Campos obligatorios y resultado final de la enumeración

- Los campos de página de nivel superior deben tener al menos: `slide_number`, `page_type`, `title`, `page_goal`, `cards`, `visual_weight`, `density_label`, `density_reason`, `density_contract`, `director_command`, `decoration_hints`, `resources`, `workflow_metadata`.
- `tipo_página`: `portada` / `toc` / `sección` / `contenido` / `fin`
- `narrative_role`: Alinearse con el rol narrativo del esquema, usar `cover` / `toc` / `section` / `evidence` / `comparison` / `process` / `close` / `cta`
- `density_label`: `baja` / `media_baja` / `media` / `alta` / `panel`
- `density_contract.image_policy`: `flexible` / `support_only` / `decorate_only`
- `density_contract.decoration_budget`: `generoso` / `medio` / `bajo` / `mínimo`
- `density_contract.overflow_strategy`: `rebalance_layout` / `tighten_budget` / `table_or_microchart` / `rollback_planning`
- La página de contenido debe tener "layout_hint" y seleccionarse del conjunto reconocido por el validador, como "enfoque único", "simétrico", "asimétrico", "tres columnas", "primario-secundario", "hero-top", "cuadrícula mixta", "forma de L", "forma de T", "cascada".
- `tarjetas[].role`: `ancla` / `soporte` / `contexto`
- `cards[].card_style`: `acento` / `elevado` / `relleno` / `contorno` / `vidrio` / `transparente`
- `cards[].body` debe ser una **matriz de cadenas**, no la escriba como una sola cadena
- `cards[].data_points` debe ser una matriz de objetos; intenta traer "fuente" cuando haya números
- `cards[].content_budget` debe ser un objeto; Incluso el objeto más pequeño debe escribirse explícitamente. También debe obedecer el `density_contract` a nivel de página.
- Cuando `cards[].image.needed = true`, se debe completar `usage` / `placement` / `content_description` / `source_hint`; de lo contrario, estos campos deberían ser "nulos".

### Conclusión especial de densidad

- El número total de `tarjetas` no debe exceder `density_contract.max_cards`
- El número de tarjetas con `chart.chart_type` no debe exceder `density_contract.max_charts`
- `content_budget.body_max_lines` por tarjeta no debe exceder `density_contract.max_lines_per_card`
- La tarjeta `image_hero` no se puede usar en la página `dashboard` y la imagen grande no se puede usar como ancla principal.
- `image_policy` de la página `dashboard` debe ser `decorate_only`

---

## Phase 5：图片策略决策（必须明确，不得含糊）

| Modo | Escenarios aplicables | Campos obligatorios |
|------|---------|---------|
| `generar` | Portadas, páginas de capítulos, páginas centrales que requieren un fuerte impacto visual | `image.needed=true`, `usage`, `placement`, `content_description`, `source_hint` (ruta de ubicación de destino), `image.prompt` (palabra de indicación de imagen en inglés) |
| `proporcionado` | El usuario ha proporcionado imágenes/galerías de marcas/capturas de pantalla | `image.needed=true`, `source_hint` (ruta local real) |
| `ranura_manual` | El usuario completará la imagen él mismo más tarde y ocupará el espacio primero | `image.needed=false`, `image.slot_note` explica la posición de la ranura, la proporción y las sugerencias de reemplazo |
| `decorar` | Página de datos, página lógica, página de composición tipográfica pura | `image.needed=false`, `image.decorate_brief` describe el lenguaje visual interno (SVG/degradado/bloque de color/marca de agua/decoración de fuente) |

**Está prohibido salir del modo ambiguo. Una vez seleccionado, no se debe cambiar temporalmente durante la etapa HTML. **

**Restricciones de densidad adicionales**:
- `low/mid_low`: permite estrategias de imagen más liberales
- `medium`: Las imágenes sólo se pueden utilizar como soporte para evitar tragar el texto.
- `high`: no use `hero-background`, las imágenes solo se pueden usar como apoyo o ilustración parcial
- `panel`: el valor predeterminado es `decorar`, la imagen grande no se puede utilizar como ancla principal

---

## Fase 6: Eres arquitecto, tanto la disciplina como la creatividad son importantes

> **Concepto central**: El menú de la Fase 2 anterior, el contrato de densidad de la Fase 3 y el esquema de la Fase 4 no son borradores con los que usted puede jugar, sino **dibujos de ingeniería** establecidos por usted como diseñador arquitectónico. La verdadera creatividad florece dentro de limitaciones extremadamente severas.

**La Disciplina de Ejecución:**
- `layout_hint` **es el muro de carga dorado de la interfaz**. En la etapa de renderizado posterior, se asignará a la estructura de cuadrícula DOM real con una precisión sin concesiones, y la configuración del centro de gravedad del diseño original no se puede romper a voluntad.
- `card_type` y `chart_type` implican la imposición de ciertas especificaciones de diseño. Una vez que seleccione un tipo específico, debe seguir sus mejores prácticas; de lo contrario, el proceso de revisión de imágenes posterior enviará directamente la página de regreso y la rehará.
- `director_command` es su anotación de dibujo; esta es una descripción de dimensiones superiores de la utilización del espacio, que guía a los usuarios posteriores a centrarse en qué CSS implementar con cuidado sin destruir el esqueleto. El revisor de imágenes no se hará cargo de las consecuencias para usted y las instrucciones deben ser estrictas.
- `must_avoid` es una línea roja fatal: escribe al menos 1 zona prohibida verdaderamente significativa en cada página para recordarte que debes hacer lo mejor que puedas dentro de los límites y rechazar activamente compromisos mediocres.

**Advertencia de revisión gráfica**: Todas las decisiones estructurales que tomes en esta etapa deben ser totalmente responsables del código final. No crea que puede desviarse del marco a voluntad debido a la "revisión de imagen a nivel de píxeles". La revisión de imágenes es para pulir y ajustar, no para limpiarse el trasero y reconstruir el esqueleto.

---

## Fase 7: especificaciones de llenado del campo de tarjetas

Cada tarjeta debe contener:
- `card_id`: estable y único, se recomienda utilizar `s{número de página}-{anchor|support|context}-{número de serie}`
- `rol`: `ancla` / `apoyo` / `contexto`
- `card_type`: valor de enumeración del validador, como `text` / `data` / `list` / `process` / `data_highlight` / `timeline` / `diagram` / `quote` / `comparison` / `people` / `image_hero` / `matrix_chart`
- `card_style`: una de las 6 variantes visuales legales
- `headline`: título (conciso, no más de 12 palabras)
- `body`: matriz de cadenas del cuerpo, no puede estar vacía
- **[Ley de hierro antifugas]**: ¡`título` y `cuerpo` solo pueden y deben completarse con la copia del contenido que finalmente se muestra a la audiencia! Está absolutamente prohibido completar las "instrucciones de narración", "acciones de trabajo" e "ideas de diseño" en el esquema (por ejemplo: *"Esta página primero comprime todo el contenido en un mapa y luego lo desmantela"* Esto es obviamente un comentario detrás de escena) como un guión. Incluya todas las instrucciones detrás de escena orientadas al diseño en `director_command`. ¡Exponer instrucciones de trabajo en el cuerpo de la tarjeta se considerará un accidente de diseño grave!
- `data_points`: Si hay un valor, complete la matriz de objetos
- `content_budget`: objeto de presupuesto de contenido y debe obedecer al `density_contract` a nivel de página
- `image`: objeto de contrato de imagen completo, con `mode`
- `resource_ref`: escriba aquí cuando necesite vincular un bloque/gráfico/principio de manera específica
- `image.slot_note` / `image.decorate_brief` / `image.prompt`: Suplemento bajo demanda según modo de imagen

Opcional pero recomendado:
- `argumento_rol`
- `gráfico`

**No se permiten tarjetas con `cuerpo` vacío. **

---

## Fase 8: Campos de entrega de intención de diseño

Mejore la calidad de la presentación mientras se adhiere al esqueleto. Defina y utilice estrictamente los siguientes campos para enviar sus instrucciones de ingeniería precisas y planes de microtallado a la etapa HTML. Constituyen un contrato obligatorio para su posterior implementación visual:

- `focus_zone`: propuesta propuesta y área de enfoque visual
- `must_avoid`: no caiga en un diseño de plantilla mediocre durante la etapa de aprovisionamiento de HTML
- `director_command`: proporciona estructura creativa, puntos de anclaje y dirección técnica avanzada
- `decoration_hints`: describe la intensidad y jerarquía visual de la decoración.
- `source_guidance`: restringe los límites de la evidencia y las expectativas de citación
- `resources` / `resource_ref`: recursos de componentes recomendados para el consumo

---

## Phase 9：自审（强制）

Ejecute `planning_validator.py` hasta cero ERROR:

```bash
python3 SKILL_DIR/scripts/planning_validator.py $(dirname PLANNING_OUTPUT) --refs REFS_DIR --page PAGE_NUM
```

- El ERROR debe repararse antes de FINALIZAR
- ADVERTENCIA reparación recomendada, no obligatoria
- Envíe FINALIZE inmediatamente después de aprobar el autoexamen y luego espere las instrucciones de la etapa HTML