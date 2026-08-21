# Índice de Referencias

Este directorio contiene la **única fuente de la verdad** para todos los recursos del flujo de trabajo de presentaciones. El agente principal usa `view_file` para leer las referencias necesarias en cada fase; los subagentes reciben el contenido relevante inyectado en sus prompts mediante las plantillas `tpl-*.md`.

## Estructura de Directorios

```
references/
  playbooks/          -- Detalles de ejecución de subagentes (5 + 3 bajo step4/)
  prompts/            -- Plantillas de prompts (múltiples tpl-*.md + 2 module-*.md + 4 bajo step4/)
  layouts/            -- Recursos de layouts (10 tipos)
  blocks/             -- Componentes de visualización de área (8 tipos + card-styles)
  charts/             -- Componentes de gráficos (13 tipos + runtime-chart-rules)
  styles/             -- Temas de estilo (8 tipos + runtime-style-rules + runtime-style-palette-index)
  principles/         -- Principios de diseño (7 tipos + runtime-failure-modes)
  page-templates/     -- Plantillas de estructura de página (cover/toc/section/end)
  design-runtime/     -- Mapeo de tipos de datos + Especificaciones de diseño + Arsenal CSS
```

## Entradas Centrales

Lee estos primero, luego revisa los elementos detallados de la biblioteca de recursos:

1. `SKILL.md` -- Contrato de la consola principal: Máquina de estados, esqueleto de programación unificada, Puertas (Gates), reglas de recuperación.
2. `playbooks/research-phase{1,2}-playbook.md` -- Detalles de ejecución y revisión de la recopilación y organización (Step 2A)
3. `playbooks/source-phase{1,2}-playbook.md` -- Detalles de ejecución y revisión de la integración de materiales (Step 2B)
4. `playbooks/outline-phase{1,2}-playbook.md` -- Detalles de ejecución de la redacción y autorrevisión del esquema (Step 3)
5. `playbooks/style-phase{1,2}-playbook.md` -- Contrato de estilo global y autorrevisión de campos (Step 3.5)
7. `playbooks/step4/page-planning-playbook.md` -- Detalles de ejecución de la planificación de páginas (Step 4A)
8. `playbooks/step4/page-html-playbook.md` -- Detalles de ejecución de la implementación HTML (Step 4B)
9. `playbooks/step4/page-review-playbook.md` -- Detalles de ejecución de la revisión y reparación de imágenes (Step 4C)
10. `styles/runtime-style-rules.md` -- Contrato de campos de estilo runtime (Step 3.5)
11. `styles/runtime-style-palette-index.md` -- Entrada base a los estilos preestablecidos (Step 3.5)
12. **`playbooks/bespoke-slide-recipe.md` -- LECTURA OBLIGATORIA en Fase 4: cómo escribir cada slide como documento HTML autocontenido (sin CSS compartido).**

## Plantillas de Prompt

Los archivos `tpl-*.md` contienen las plantillas de prompt para cada subagente. Las variables `{{VAR}}` son reemplazadas por el agente principal antes de enviar el prompt al subagente.

En particular, el Paso 0 ahora utiliza "Plantilla Doble / Recorte por Capacidad":

- `tpl-interview-structured-ui.md`: Modo de Entrevista Estructurada UI
- `tpl-interview-text-fallback.md`: Modo de Respaldo de Texto
- `tpl-interview.md`: Núcleo de entrevista compartido, no se ejecuta directamente como plantilla runtime.
- `module-structured-interview-ui.md` / `module-text-interview-fallback.md`: Módulos de modo, inyectados en la plantilla runtime a través de `--inject-file`.

P2A/P2B/P3/P3.5/P4 utilizan inyección de contexto progresiva: cada nodo tiene orchestrator + phase1 + phase2 (el Paso 4 tiene phase1/2/3), y los subagentes leen de forma autónoma por etapas internamente.

| Plantilla | Etapa | Descripción |
|------|------|------|
| `tpl-interview.md` | Núcleo Step 0 | Contrato de preguntas de entrevista compartida, no se ejecuta directamente |
| `tpl-interview-structured-ui.md` | Entrevista Step 0 | Modo Structured UI |
| `tpl-interview-text-fallback.md` | Entrevista Step 0 | Modo Text Fallback |
| `module-structured-interview-ui.md` | Módulo Step 0 | Protocolo de modo Structured UI |
| `module-text-interview-fallback.md` | Módulo Step 0 | Protocolo de modo Text Fallback |
| `tpl-research-synth-orchestrator.md` | Programación Step 2A | Orchestrator ligero |
| `tpl-research-synth-phase1.md` | Búsqueda Step 2A | Búsqueda y recopilación |
| `tpl-research-synth-phase2.md` | Organización Step 2A | Formateo de datos + autorrevisión |
| `tpl-source-synth-orchestrator.md` | Programación Step 2B | Orchestrator ligero |
| `tpl-source-synth-phase1.md` | Extracción Step 2B | Lectura y extracción de materiales |
| `tpl-source-synth-phase2.md` | Autorrevisión Step 2B | Autorrevisión de calidad + verificación de límites |
| `tpl-outline-orchestrator.md` | Programación Step 3 | Orchestrator ligero |
| `tpl-outline-phase1.md` | Redacción Step 3 | Redacción de esquema |
| `tpl-outline-phase2.md` | Autorrevisión Step 3 | Autorrevisión estricta + reparación |
| `tpl-style-orchestrator.md` | Programación Step 3.5 | Orchestrator ligero |
| `tpl-style-phase1.md` | Decisión Step 3.5 | Extracción de restricciones + salida de estilo |
| `tpl-style-phase2.md` | Autorrevisión Step 3.5 | Autorrevisión del contrato de campos |
| `step4/tpl-page-orchestrator.md` | Programación Step 4 | Orchestrator progresivo (backend de ejecución unificado) |
| `step4/tpl-page-planning.md` | Planificación Step 4A | Planificación de página |
| `step4/tpl-page-html.md` | HTML Step 4B | Generación del borrador de diseño |
| `step4/tpl-page-review.md` | Revisión Step 4C | Revisión y reparación de imágenes |

## Biblioteca de Recursos

El agente resuelve los recursos usando `view_file` para leer el archivo correcto según los campos del `visual_plan.json`:

| Campo del plan | Directorio de recursos | Ejemplo |
|---|---|---|
| `layout_hint` | `layouts/` | `layout_hint: "primary-secondary"` → leer `layouts/primary-secondary.md` |
| `card_type` | `blocks/` | `card_type: "timeline"` → leer `blocks/timeline.md` |
| `chart_type` | `charts/` | `chart_type: "radar"` → leer `charts/advanced.md` |
| `page_type` | `page-templates/` | `page_type: "cover"` → leer `page-templates/cover.md` |

Para páginas de tipo `cover`, `toc`, `section`, `end`, la referencia principal es `page-templates/`.
Para páginas de tipo `content`, los recursos se seleccionan por `layout_hint` + `card_type`.

## Design Runtime

El archivo puente de los datos a lo visual:

| Archivo | Propósito |
|------|------|
| `data-type-visual-mapping.md` | Tipo de datos -> card_type + layout + Referencia de implementación CSS |
| `data-type-decoration-mapping.md` | Tipo de datos -> Técnica de decoración (T) + Arma (W) + Densidad |
| `design-specs.md` | Especificaciones de lienzo, jerarquía tipográfica, reglas de tarjetas |
| `css-weapons.md` | Arsenal CSS avanzado W1-W12 |

## Style Runtime

El directorio de estilos contiene:

- **`eva-style-guide.md`**: Guía maestra con los 26 temas (usados como inspiración del "theme recipe", no como archivo CSS a enlazar) y la matriz de decisión para EVA IPSS. **Lectura obligatoria en Fase 0.**
- **`index.md`**: Índice de todos los estilos con previews.
- **Archivos por categoría**: `dark.md`, `light.md`, `natural.md`, `vibrant.md`, `cultural.md` — Se leen bajo demanda cuando se necesita inspeccionar un tema candidato en detalle.
- **`README.md`**: Documentación del sistema de estilos y campos de configuración.

## Scripts de Orquestación y Validación

El pipeline se apoya en scripts de Python ubicados en `scripts/` para garantizar consistencia:
- `planning_validator.py`: Valida estrictamente el `visual_plan.json` contra el esquema y el `density_contract`.
- `visual_qa.py`: Realiza análisis de píxeles sobre las capturas PNG para detectar errores de diseño (overflow, contraste).
- `resource_loader.py`: Enruta dinámicamente los recursos basados en el `visual_plan.json`.
- `generate_presentation_template.py`: Ensambla la carpeta `presentation/` final a partir del `visual_plan.json`.

> Los scripts bajo `scripts/legacy/` (`prompt_harness.py`, `contract_validator.py`, `build_themes.py`) pertenecen a la arquitectura anterior de subagentes y NO se usan en el pipeline actual.

## Fuente Única de la Verdad

La skill mantiene una arquitectura markdown-first. La última palabra sobre cada aspecto la tiene:

- **Validación del Plan JSON**: `scripts/planning_validator.py`
- **Variables CSS y temas**: `references/styles/eva-style-guide.md` (paleta de inspiración por tema; cada slide define su propio `:root`)
- **Recursos disponibles**: Los archivos reales en `references/layouts/`, `blocks/`, `charts/`, `page-templates/`
- **Pipeline de 5 fases**: `SKILL.md`
- **Cómo escribir el HTML de cada slide**: `references/playbooks/bespoke-slide-recipe.md` (reemplaza las restricciones antiguas de `legacy/pipeline-compat.md`, que ya no aplican al ensamblaje HTML/PPTX por captura de pantalla)

## Reglas de Mantenimiento

- Coloque los nuevos archivos de recursos en el directorio correspondiente.
- Cada archivo de recurso debe tener `# Título` + `> Cita multilinea` (Tipo de datos, Escenarios aplicables, Restricciones).
- No coloque archivos en el directorio raíz, no cree nuevos subdirectorios.
