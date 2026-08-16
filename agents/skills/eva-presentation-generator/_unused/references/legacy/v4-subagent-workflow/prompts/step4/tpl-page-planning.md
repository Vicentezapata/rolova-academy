# Paso 1: Planificación de la página: página {{PAGE_NUM}} de {{TOTAL_PAGES}}

> **Subagente**: `{{SUBAGENT_NAME}}` · **Etapa**: planificación · **Página**: {{PAGE_NUM}}/{{TOTAL_PAGES}}

> **【Instrucciones obligatorias a nivel del sistema / ANULACIÓN CRÍTICA】**
> Este mensaje contiene **todos** los objetivos de la misión y los detalles del Playbook que necesitas para esta etapa.
> **¡Está estrictamente prohibido llamar a herramientas para leer el `SKILL.md` externo o el archivo maestro de reglas globales! **
>
> El único objetivo de esta etapa: generar `{{PLANNING_OUTPUT}}`. Como arquitecto, debes establecer **dibujos de ingeniería duros** insuperables aquí. Ejerza un estricto control estructural en campos como `layout_hint`, `focus_zone` y `must_avoid`. La etapa HTML posterior y el proceso de revisión de imágenes obedecerán absolutamente la disciplina marco que establezca en este momento.
> Si el orquestador externo ha proporcionado un protocolo de avance de etapa, el protocolo externo tiene prioridad sobre la descripción de la señal de finalización en este mensaje.

Esta es su tarea **principal de la primera fase** para la página {{PAGE_NUM}}: planificar el borrador final.
No escriba código HTML todavía, simplemente complete y verifique `{{PLANNING_OUTPUT}}`.

---

## Playbook (detalles de ejecución)

{{LIBRO DE JUEGOS}}

---

## Referencia rápida de principios de diseño

{{PRINCIPLES_CHEATSHEET}}

---

## Paquete de tareas

| proyecto | ruta/valor |
|------|--------|
| Número de página | {{PAGE_NUM}} / {{TOTAL_PAGES}} |
| Requisitos | `{{REQUIREMENTS_PATH}}` |
| Esquema | `{{OUTLINE_PATH}}` |
| Materiales | `{{BRIEF_PATH}}` |
| Estilo | `{{STYLE_PATH}}` |
| Directorio de material de imagen | `{{IMAGES_DIR}}` |
| Instantánea de la lista de imágenes | `{{IMAGE_INVENTORY_PATH}}` |
| Instantánea del menú | `{{RESOURCE_MENU_PATH}}` |
| Ejecutar registro | `{{SUBAGENT_LOG_PATH}}` |
| Directorio de HABILIDADES | `{{SKILL_DIR}}` |
| Directorio de recursos | `{{REFS_DIR}}` |

---

## Ruta del producto

- Borrador de planificación JSON: `{{PLANNING_OUTPUT}}`
- Copia de seguridad en tiempo de ejecución: `{{PLANNING_RUNTIME_COPY_PATH}}`
- Informe del validador: `{{PLANNING_VALIDATOR_REPORT_PATH}}`
- El contenido del archivo debe ser un **objeto JSON puro** (el objeto puede escribirse directamente o incluirse en```json fenced block 中），不要夹杂说明性 prose。

---

## 执行链路（固定顺序，不得跳步）

1. 读取 `{{OUTLINE_PATH}}` 中第 {{PAGE_NUM}} 页的定义（只关注你这一页），特别提取 `密度下限 / 密度目标 / 密度上限 / 节奏动作 / 信息姿态 / 锚点类型`
2. 深度读取 `{{REQUIREMENTS_PATH}}`，将其中的【受众画像】、【目标动作】和【版面心智】作为单页选型和内容设计的最高约束（例如：对底层技术受众放大图表卡片，对合作方主打对比及成果锚点）。
3. 读取 `{{BRIEF_PATH}}` 获取可用素材
4. 读取 `{{STYLE_PATH}}` 提取 `mood_keywords`、`variation_strategy`、`decoration_dna` 做情绪定调
5. 读取主链已生成的**图片清单快照** `{{IMAGE_INVENTORY_PATH}}`。
6. 如需刷新这份图片清单，再执行：
   ```fiesta
   python3 {{SKILL_DIR}}/scripts/subagent_logger.py run --log {{SUBAGENT_LOG_PATH}} --label planificación-actualización-imagenes -- \
     python3 {{SKILL_DIR}}/scripts/resource_loader.py imágenes --images-dir {{IMAGES_DIR}} --output {{IMAGE_INVENTORY_PATH}}```
7. 读取主链已生成的**组件/图表菜单快照** `{{RESOURCE_MENU_PATH}}`（这Sí给 runtime 留档的备份，也作为你本阶段优先使用的菜单视图）。
8. 如需刷新这份菜单快照，再执行：
   ```fiesta
   python3 {{SKILL_DIR}}/scripts/subagent_logger.py run --log {{SUBAGENT_LOG_PATH}} --label planificación-actualización-menu --\
     python3 {{SKILL_DIR}}/scripts/resource_loader.py menú --refs-dir {{REFS_DIR}} --output {{RESOURCE_MENU_PATH}}```
9. **先冻结密度合同，再回答设计提问**。你必须先确定 `density_label`、`density_reason` 和 `density_contract`，再决定 `page_type`、`layout_hint`、`cards[].card_type`、`chart.chart_type`、`resource_ref`、`image.mode`、排版策略等。

### 设计决策驱动提问

在确定布局和资源之前，先回答这 4 个问题（可在心中推演，不需要写入产物）：

1. **观众在这一页应该先看到什么？** → 决定视觉锚点和主次关系
2. **这一页的信息Sí怎么"流动"的？** → 决定空间布局和视觉动线
3. **这一页和上一页的视觉感受应该有什么不同？** → 决定节奏变化
4. **在菜单中的工具里，哪些能最好地服务上面 3 个答案？** → 决定 layout_hint、card_type、chart、resource_ref

> **重要**：菜单里的工具依然Sí你的调色盘。同样的数据可以用完全不同的工具和布局来表达，关键Sí你想让观众产生什么感受。设计原则参考文件与映射表Sí你绝好的灵感索引，你完全可以跨界混搭布局。
> **唯一不可妥协的底线**：你可以自由构思并调配这些高级元素，但你的产物必须Sí精密计算后的产物！任何 `layout_hint` 或组件调用的选择，在下游环节都必须用符合其核心语义的底层结构去精确承接。你的奇思妙想不能以牺牲布局崩塌为代价。
> **密度红线**：`density_label` 只能落在 outline 给你的窗口里。`dashboard` 只允许 `content` 页，且必须同时把 `image_policy` 锁成 `decorate_only`。

**填写 `resources` 字段时必须说明选择理由**（推荐写入 `resources.resource_rationale`），例如回答"为什么用这个布局/组件能最好地让观众产生我想要的感受"。
10. 将完整 planning 写入 `{{PLANNING_OUTPUT}}`，并同步备份到 `{{PLANNING_RUNTIME_COPY_PATH}}`：
   ```fiesta
   python3 {{SKILL_DIR}}/scripts/subagent_logger.py run --log {{SUBAGENT_LOG_PATH}} --label planificación-tiempo de ejecución-copia --\
     cp {{PLANNING_OUTPUT}} {{PLANNING_RUNTIME_COPY_PATH}}```
11. 自审（必须执行，不得跳过）：
   ```fiesta
   python3 {{SKILL_DIR}}/scripts/subagent_logger.py run --log {{SUBAGENT_LOG_PATH}} --label planificación-validador -- \
     python3 {{SKILL_DIR}}/scripts/planning_validator.py $(dirname {{PLANNING_OUTPUT}}) --refs {{REFS_DIR}} --page {{PAGE_NUM}} --report {{PLANNING_VALIDATOR_REPORT_PATH}}
   ```
12. Corrija todos los ERRORES (ADVERTENCIA, correcciones recomendadas).
13. Señal de finalización: salida `--- ETAPA 1 COMPLETA: {{PLANNING_OUTPUT}} ---`, y luego continúe con la siguiente etapa de acuerdo con el protocolo del orquestador externo
14. No confunda la señal de finalización de la etapa actual con el final de la tarea de página completa.

---

## Límite del escenario

- Esta etapa: solo escriba la planificación JSON, no HTML
- Siguiente etapa: el orquestador lo guiará hacia la generación de HTML
- Reglas de consumo: Solo se lee la `>capa de referencia` (menú) del recurso en la etapa de planificación, y la capa de texto solo se lee en la etapa HTML.