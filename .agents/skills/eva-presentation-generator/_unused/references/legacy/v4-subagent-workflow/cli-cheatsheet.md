# Hoja de Trucos CLI (CLI Cheatsheet)

> Manual de comandos completo organizado por pasos. Al ejecutar, reemplaza variables como `SKILL_DIR` / `OUTPUT_DIR` con rutas reales.
> El agente principal DEBE leer este archivo para establecer el conocimiento de la interfaz antes de entrar al Step 0. Prohibido ejecutar `--help` en cualquier script.

---

## Paso 0 Entrevista

Generación de Prompt (Elige uno según capacidad):

**A. Modo UI estructurada**

```bash
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/tpl-interview-structured-ui.md \
  --var TOPIC="Tema del usuario" \
  --var USER_CONTEXT="Información de contexto proporcionada por el usuario" \
  --inject-file INTERVIEW_MODE_MODULE=SKILL_DIR/references/prompts/module-structured-interview-ui.md \
  --inject-file INTERVIEW_CORE=SKILL_DIR/references/prompts/tpl-interview.md \
  --output OUTPUT_DIR/runtime/prompt-interview.md
```

**B. Modo de reserva de texto**

```bash
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/tpl-interview-text-fallback.md \
  --var TOPIC="Tema del usuario" \
  --var USER_CONTEXT="Información de contexto proporcionada por el usuario" \
  --inject-file INTERVIEW_MODE_MODULE=SKILL_DIR/references/prompts/module-text-interview-fallback.md \
  --inject-file INTERVIEW_CORE=SKILL_DIR/references/prompts/tpl-interview.md \
  --output OUTPUT_DIR/runtime/prompt-interview.md
```

Reglas de Ejecución:

1. Primero, determina el modo actual según la conclusión de `## Capacidad de UI de la Entrevista`: `structured-ui` o `text-fallback`.
2. El Modo Structured UI usa el comando A; El Modo Text Fallback usa el comando B.
3. Ambos modos deben generar primero `OUTPUT_DIR/runtime/prompt-interview.md`.
4. El Modo Text Fallback también debe generar un formulario de entrevista en Markdown claramente agrupado, no debe degradarse a un solo campo para rellenar o preguntas dispersas.
5. Solo si `prompt_harness.py` experimenta un fallo de interfaz real en el Step 0 y ha determinado `BLOCKED_SCRIPT_INTERFACE`, se permite omitir por completo `prompt-interview.md` y preguntar directamente; la cobertura de las preguntas no debe ser inferior a la de `tpl-interview.md`.

Validación (Gate):

```bash
python3 SKILL_DIR/scripts/contract_validator.py interview OUTPUT_DIR/interview-qa.txt
python3 SKILL_DIR/scripts/contract_validator.py requirements-interview OUTPUT_DIR/requirements-interview.txt
```

---

## Step 1 Confirmación de Rama

El agente principal ejecuta directamente (sin subagente):

1. Identifica si el usuario ha proporcionado materiales listos para usar (archivos/texto/pptx).
2. Confirma con el usuario la selección de la rama:
   - **Rama research (investigación)**: Hacer la presentación después de buscar en internet (→ Step 2A).
   - **Rama no-research**: Hacer la presentación basada en los materiales proporcionados por el usuario (→ Step 2B).
3. Rellena el campo `Rama` en `requirements-interview.txt`:

```bash
# Reemplaza BRANCH_VALUE con el valor real de la rama (research o no-research)
# Encuentra la línea "- Rama: " directamente en el archivo y actualízala
```

Validación (Gate):

```bash
python3 SKILL_DIR/scripts/contract_validator.py requirements-interview OUTPUT_DIR/requirements-interview.txt
```

---

## Step 2A Research (Inyección Progresiva de Contexto)

> **Subagente Obligatorio**: El producto de este paso DEBE ser generado por el subagente ResearchSynth. Se prohíbe al agente principal producirlo en línea.
> El subagente avanza internamente de forma autónoma por fases: Búsqueda -> Formato de Datos + Organización + Autorevisión.

**1. Generar archivos de prompt por fase (Ejecutado por el agente principal):**

```bash
# Fase 1: Búsqueda y recopilación
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/tpl-research-synth-phase1.md \
  --var TOPIC="Tema" \
  --var REQUIREMENTS_PATH=OUTPUT_DIR/requirements-interview.txt \
  --var SEARCH_OUTPUT=OUTPUT_DIR/search.txt \
  --var TOOLS_AVAILABLE="El agente principal inserta dinámicamente las herramientas de búsqueda disponibles y descripciones breves basadas en sus capacidades" \
  --var MAX_SEARCH_ROUNDS="El agente principal estima basado en la complejidad del tema: Fácil 2 / Medio 3 / Alta complejidad 4" \
  --var TARGET_PAGES="Páginas objetivo (De la entrevista)" \
  --inject-file PLAYBOOK=SKILL_DIR/references/playbooks/research-phase1-playbook.md \
  --output OUTPUT_DIR/runtime/prompt-research-phase1.md

# Fase 2: Formato de datos, Organización y Autorevisión
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/tpl-research-synth-phase2.md \
  --var SEARCH_OUTPUT=OUTPUT_DIR/search.txt \
  --var BRIEF_OUTPUT=OUTPUT_DIR/search-brief.txt \
  --var TARGET_PAGES="Páginas objetivo (De la entrevista)" \
  --inject-file PLAYBOOK=SKILL_DIR/references/playbooks/research-phase2-playbook.md \
  --output OUTPUT_DIR/runtime/prompt-research-phase2.md
```

**2. Generar prompt de orquestación (orchestrator):**

```bash
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/tpl-research-synth-orchestrator.md \
  --var PHASE1_PROMPT_PATH=OUTPUT_DIR/runtime/prompt-research-phase1.md \
  --var PHASE2_PROMPT_PATH=OUTPUT_DIR/runtime/prompt-research-phase2.md \
  --var SEARCH_OUTPUT=OUTPUT_DIR/search.txt \
  --var BRIEF_OUTPUT=OUTPUT_DIR/search-brief.txt \
  --output OUTPUT_DIR/runtime/prompt-research-orchestrator.md
```

**3. Crear Subagente y Ejecutar:**

```
{{SUBAGENT_NAME}} = ResearchSynth
{{MODEL}}           = SUBAGENT_MODEL
{{THINKING_EFFORT}} = SUBAGENT_THINKING_EFFORT
{{PROMPT_PATH}}   = OUTPUT_DIR/runtime/prompt-research-orchestrator.md
```

> Internamente, el subagente avanzará de forma autónoma: primero lee phase1 para completar la búsqueda -> luego lee phase2 para completar el formateo + autorevisión -> FINALIZE

**4. Validación (Revisión del agente principal):**

```bash
python3 SKILL_DIR/scripts/contract_validator.py search OUTPUT_DIR/search.txt
python3 SKILL_DIR/scripts/contract_validator.py search-brief OUTPUT_DIR/search-brief.txt
```

> `CURRENT_BRIEF_PATH` (usado en pasos posteriores) = `OUTPUT_DIR/search-brief.txt`

Si la validación (Gate) pasa pero el material aún parece escaso, **regresa al Step 2A.01**: Regenera los prompts phase1/phase2/orchestrator (ampliando `TOOLS_AVAILABLE`, dimensiones de consulta, o `MAX_SEARCH_ROUNDS`), y crea un nuevo subagente ResearchSynth. **No** reanudes la búsqueda en la sesión antigua que ya hizo FINALIZE.

---

## Step 2B Rama No-Research (Inyección Progresiva de Contexto)

> **Subagente Obligatorio**: El producto de este paso DEBE ser generado por el subagente SourceSynth. Se prohíbe al agente principal producirlo en línea.
> El subagente avanza internamente de forma autónoma por fases: Lectura y Refinamiento -> Autorevisión de calidad + verificación de límites.

**1. Generar archivos de prompt por fase (Ejecutado por el agente principal):**

```bash
# Fase 1: Lectura de material y refinamiento estructurado
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/tpl-source-synth-phase1.md \
  --var REQUIREMENTS_PATH=OUTPUT_DIR/requirements-interview.txt \
  --var SOURCE_INPUT=Ruta de los materiales del usuario (directorio o archivo) \
  --var BRIEF_OUTPUT=OUTPUT_DIR/source-brief.txt \
  --inject-file PLAYBOOK=SKILL_DIR/references/playbooks/source-phase1-playbook.md \
  --output OUTPUT_DIR/runtime/prompt-source-phase1.md

# Fase 2: Autorevisión de calidad y verificación de límites
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/tpl-source-synth-phase2.md \
  --var BRIEF_OUTPUT=OUTPUT_DIR/source-brief.txt \
  --var REQUIREMENTS_PATH=OUTPUT_DIR/requirements-interview.txt \
  --inject-file PLAYBOOK=SKILL_DIR/references/playbooks/source-phase2-playbook.md \
  --output OUTPUT_DIR/runtime/prompt-source-phase2.md
```

**2. Generar prompt de orquestación (orchestrator):**

```bash
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/tpl-source-synth-orchestrator.md \
  --var PHASE1_PROMPT_PATH=OUTPUT_DIR/runtime/prompt-source-phase1.md \
  --var PHASE2_PROMPT_PATH=OUTPUT_DIR/runtime/prompt-source-phase2.md \
  --var BRIEF_OUTPUT=OUTPUT_DIR/source-brief.txt \
  --output OUTPUT_DIR/runtime/prompt-source-orchestrator.md
```

**3. Crear Subagente y Ejecutar:**

```
{{SUBAGENT_NAME}} = SourceSynth
{{MODEL}}           = SUBAGENT_MODEL
{{THINKING_EFFORT}} = SUBAGENT_THINKING_EFFORT
{{PROMPT_PATH}}   = OUTPUT_DIR/runtime/prompt-source-orchestrator.md
```

> Internamente, el subagente avanzará de forma autónoma: primero lee phase1 para completar el refinamiento -> luego lee phase2 para completar la autorevisión -> FINALIZE

**4. Validación (Revisión del agente principal):**

```bash
python3 SKILL_DIR/scripts/contract_validator.py source-brief OUTPUT_DIR/source-brief.txt
```

> `CURRENT_BRIEF_PATH` (usado en pasos posteriores) = `OUTPUT_DIR/source-brief.txt`



## Step 3 Esquema (Inyección Progresiva de Contexto)

> **Subagente Obligatorio**: El producto de este paso DEBE ser generado por el subagente Outline. Se prohíbe al agente principal producirlo en línea.
> El subagente avanza internamente de forma autónoma por fases: Escritura de esquema -> Autorevisión estricta + corrección.

**1. Generar archivos de prompt por fase (Ejecutado por el agente principal):**

```bash
# Fase 1: Redacción del esquema
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/tpl-outline-phase1.md \
  --var REQUIREMENTS_PATH=OUTPUT_DIR/requirements-interview.txt \
  --var BRIEF_PATH=CURRENT_BRIEF_PATH \
  --var OUTLINE_OUTPUT=OUTPUT_DIR/outline.txt \
  --inject-file PLAYBOOK=SKILL_DIR/references/playbooks/outline-phase1-playbook.md \
  --output OUTPUT_DIR/runtime/prompt-outline-phase1.md

# Fase 2: Autorevisión estricta y corrección
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/tpl-outline-phase2.md \
  --var OUTLINE_OUTPUT=OUTPUT_DIR/outline.txt \
  --var REQUIREMENTS_PATH=OUTPUT_DIR/requirements-interview.txt \
  --var BRIEF_PATH=CURRENT_BRIEF_PATH \
  --inject-file PLAYBOOK=SKILL_DIR/references/playbooks/outline-phase2-playbook.md \
  --output OUTPUT_DIR/runtime/prompt-outline-phase2.md
```

**2. Generar prompt de orquestación (orchestrator):**

```bash
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/tpl-outline-orchestrator.md \
  --var PHASE1_PROMPT_PATH=OUTPUT_DIR/runtime/prompt-outline-phase1.md \
  --var PHASE2_PROMPT_PATH=OUTPUT_DIR/runtime/prompt-outline-phase2.md \
  --var OUTLINE_OUTPUT=OUTPUT_DIR/outline.txt \
  --output OUTPUT_DIR/runtime/prompt-outline-orchestrator.md
```

**3. Crear Subagente y Ejecutar:**

```
{{SUBAGENT_NAME}} = Outline
{{MODEL}}           = SUBAGENT_MODEL
{{THINKING_EFFORT}} = SUBAGENT_THINKING_EFFORT
{{PROMPT_PATH}}   = OUTPUT_DIR/runtime/prompt-outline-orchestrator.md
```

> Internamente, el subagente avanzará de forma autónoma: primero lee phase1 para escribir el esquema -> luego lee phase2 para la autorevisión y corrección -> FINALIZE

**4. Validación (Revisión del agente principal):**

```bash
python3 SKILL_DIR/scripts/contract_validator.py outline OUTPUT_DIR/outline.txt
```

Si el validador falla, regresa al Step 3.01 para regenerar los prompts y **crear un nuevo subagente Outline**; no reutilices la sesión antigua que hizo FINALIZE.

---

## Step 3.5 Estilo (Inyección Progresiva de Contexto)

> **Subagente Obligatorio**: El producto de este paso DEBE ser generado por el subagente Style. Se prohíbe al agente principal producirlo en línea.
> El subagente avanza internamente de forma autónoma por fases: Extracción de restricciones + Salida de estilo -> Autorevisión de contrato de campos.

**1. Generar archivos de prompt por fase (Ejecutado por el agente principal):**

```bash
# Fase 1: Extracción de restricciones y salida de estilo
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/tpl-style-phase1.md \
  --var REQUIREMENTS_PATH=OUTPUT_DIR/requirements-interview.txt \
  --var OUTLINE_PATH=OUTPUT_DIR/outline.txt \
  --var SKILL_DIR='$SKILL_DIR' \
  --var STYLE_OUTPUT=OUTPUT_DIR/style.json \
  --inject-file STYLE_RUNTIME_RULES=SKILL_DIR/references/styles/runtime-style-rules.md \
  --inject-file STYLE_PRESET_INDEX=SKILL_DIR/references/styles/runtime-style-palette-index.md \
  --inject-file PLAYBOOK=SKILL_DIR/references/playbooks/style-phase1-playbook.md \
  --output OUTPUT_DIR/runtime/prompt-style-phase1.md

# Fase 2: Autorevisión del contrato de campos
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/tpl-style-phase2.md \
  --var STYLE_OUTPUT=OUTPUT_DIR/style.json \
  --inject-file PLAYBOOK=SKILL_DIR/references/playbooks/style-phase2-playbook.md \
  --output OUTPUT_DIR/runtime/prompt-style-phase2.md
```

**2. Generar prompt de orquestación (orchestrator):**

```bash
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/tpl-style-orchestrator.md \
  --var PHASE1_PROMPT_PATH=OUTPUT_DIR/runtime/prompt-style-phase1.md \
  --var PHASE2_PROMPT_PATH=OUTPUT_DIR/runtime/prompt-style-phase2.md \
  --var STYLE_OUTPUT=OUTPUT_DIR/style.json \
  --output OUTPUT_DIR/runtime/prompt-style-orchestrator.md
```

**3. Crear Subagente y Ejecutar:**

```
{{SUBAGENT_NAME}} = Style
{{MODEL}}           = SUBAGENT_MODEL
{{THINKING_EFFORT}} = SUBAGENT_THINKING_EFFORT
{{PROMPT_PATH}}   = OUTPUT_DIR/runtime/prompt-style-orchestrator.md
```

> Internamente, el subagente avanzará de forma autónoma: primero lee phase1 para las decisiones de estilo -> luego lee phase2 para la autorevisión -> FINALIZE

**4. Validación (Revisión del agente principal):**

```bash
python3 SKILL_DIR/scripts/contract_validator.py style OUTPUT_DIR/style.json
```

Si el validador falla, regresa al Step 3.5.01 para regenerar los prompts y **crear un nuevo subagente Style**; no reutilices la sesión antigua que hizo FINALIZE.

---

## Step 4 Producción de Página Individual (Inyección Progresiva de Contexto)

> **Backend de ejecución unificado**: Todos los entornos utilizan orquestación de divulgación progresiva.
> El subagente avanza internamente leyendo de forma autónoma los prompts de fase. El agente principal solo es responsable de generar los prompts + crear el subagente + recopilar y validar.
> Si el usuario habilita el punto de ruptura de auditoría manual, el agente principal sigue generando el mismo conjunto de runtime prompts primero, y luego crea un PageAgent por fase o `PagePatchAgent-N` según sea necesario.

---

### 4.1 Generar instantánea (Snapshot) de Planificación + 3 archivos de prompt de fase

Primero genera la instantánea runtime que usará la etapa de planificación (planning) directamente, y luego ejecuta en orden los tres comandos harness (el orden no puede cambiarse):

**4A.0 Instantánea del Inventario de Imágenes para Planning:**

```bash
python3 SKILL_DIR/scripts/resource_loader.py images \
  --images-dir OUTPUT_DIR/images \
  --output OUTPUT_DIR/runtime/page-images-N.md
```

**4A.1 Instantánea del Menú de Planning:**

```bash
python3 SKILL_DIR/scripts/resource_loader.py menu \
  --refs-dir SKILL_DIR/references \
  --output OUTPUT_DIR/runtime/page-planning-menu-N.md
```

**4A. Aviso de planificación:**

```bash
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/step4/tpl-page-planning.md \
  --var PAGE_NUM=N \
  --var TOTAL_PAGES=TOTAL \
  --var REQUIREMENTS_PATH=OUTPUT_DIR/requirements-interview.txt \
  --var OUTLINE_PATH=OUTPUT_DIR/outline.txt \
  --var BRIEF_PATH=CURRENT_BRIEF_PATH \
  --var STYLE_PATH=OUTPUT_DIR/style.json \
  --var IMAGES_DIR=OUTPUT_DIR/images \
  --var IMAGE_INVENTORY_PATH=OUTPUT_DIR/runtime/page-images-N.md \
  --var RESOURCE_MENU_PATH=OUTPUT_DIR/runtime/page-planning-menu-N.md \
  --var PLANNING_RUNTIME_COPY_PATH=OUTPUT_DIR/runtime/page-planning-output-N.json \
  --var PLANNING_VALIDATOR_REPORT_PATH=OUTPUT_DIR/runtime/page-planning-validator-N.json \
  --var PLANNING_OUTPUT=OUTPUT_DIR/planning/planningN.json \
  --var SUBAGENT_LOG_PATH=OUTPUT_DIR/runtime/page-agent-N.log \
  --var SUBAGENT_NAME=PageAgent-N \
  --var SKILL_DIR='$SKILL_DIR' \
  --var REFS_DIR='$SKILL_DIR/references' \
  --inject-file PRINCIPLES_CHEATSHEET=SKILL_DIR/references/principles/design-principles-cheatsheet.md \
  --inject-file PLAYBOOK=SKILL_DIR/references/playbooks/step4/page-planning-playbook.md \
  --output OUTPUT_DIR/runtime/prompt-page-planning-N.md
```

**4B. HTML rápido:**

```bash
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/step4/tpl-page-html.md \
  --var PAGE_NUM=N \
  --var TOTAL_PAGES=TOTAL \
  --var PLANNING_OUTPUT=OUTPUT_DIR/planning/planningN.json \
  --var SLIDE_OUTPUT=OUTPUT_DIR/slides/slide-N.html \
  --var IMAGES_DIR=OUTPUT_DIR/images \
  --var IMAGE_INVENTORY_PATH=OUTPUT_DIR/runtime/page-images-N.md \
  --var HTML_RESOLVE_PATH=OUTPUT_DIR/runtime/page-html-resolve-N.md \
  --var HTML_RUNTIME_COPY_PATH=OUTPUT_DIR/runtime/page-html-output-N.html \
  --var STYLE_PATH=OUTPUT_DIR/style.json \
  --var SUBAGENT_LOG_PATH=OUTPUT_DIR/runtime/page-agent-N.log \
  --var SUBAGENT_NAME=PageAgent-N \
  --var SKILL_DIR='$SKILL_DIR' \
  --var REFS_DIR='$SKILL_DIR/references' \
  --inject-file PLAYBOOK=SKILL_DIR/references/playbooks/step4/page-html-playbook.md \
  --output OUTPUT_DIR/runtime/prompt-page-html-N.md
```

**4C. Prompt de Revisión (Review):**

```bash
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/step4/tpl-page-review.md \
  --var PAGE_NUM=N \
  --var TOTAL_PAGES=TOTAL \
  --var PLANNING_OUTPUT=OUTPUT_DIR/planning/planningN.json \
  --var SLIDE_OUTPUT=OUTPUT_DIR/slides/slide-N.html \
  --var PNG_OUTPUT=OUTPUT_DIR/png/slide-N.png \
  --var REVIEW_DIR=OUTPUT_DIR/review \
  --var REVIEW_RUNTIME_PNG_PATH=OUTPUT_DIR/runtime/page-review-output-N.png \
  --var VISUAL_QA_REPORT_PATH=OUTPUT_DIR/runtime/page-review-qa-N.txt \
  --var STYLE_PATH=OUTPUT_DIR/style.json \
  --var SUBAGENT_LOG_PATH=OUTPUT_DIR/runtime/page-agent-N.log \
  --var SUBAGENT_NAME=PageAgent-N \
  --var SKILL_DIR='$SKILL_DIR' \
  --inject-file PRINCIPLES_CHEATSHEET=SKILL_DIR/references/principles/design-principles-cheatsheet.md \
  --inject-file PLAYBOOK=SKILL_DIR/references/playbooks/step4/page-review-playbook.md \
  --inject-file FAILURE_MODES=SKILL_DIR/references/principles/runtime-failure-modes.md \
  --output OUTPUT_DIR/runtime/prompt-page-review-N.md
```

---

### 4.2 Generar prompt de orquestación (orchestrator) de la página

```bash
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/step4/tpl-page-orchestrator.md \
  --var PAGE_NUM=N \
  --var TOTAL_PAGES=TOTAL \
  --var PLANNING_PROMPT_PATH=OUTPUT_DIR/runtime/prompt-page-planning-N.md \
  --var HTML_PROMPT_PATH=OUTPUT_DIR/runtime/prompt-page-html-N.md \
  --var REVIEW_PROMPT_PATH=OUTPUT_DIR/runtime/prompt-page-review-N.md \
  --var PLANNING_OUTPUT=OUTPUT_DIR/planning/planningN.json \
  --var SLIDE_OUTPUT=OUTPUT_DIR/slides/slide-N.html \
  --var PNG_OUTPUT=OUTPUT_DIR/png/slide-N.png \
  --var SUBAGENT_LOG_PATH=OUTPUT_DIR/runtime/page-agent-N.log \
  --var SUBAGENT_NAME=PageAgent-N \
  --var SKILL_DIR='$SKILL_DIR' \
  --output OUTPUT_DIR/runtime/prompt-page-orchestrator-N.md
```

---

### 4.3 Crear PageAgent-N y Ejecutar

Consulta el manual operativo del subagente para la plantilla de llamada, reemplaza las variables y **exponlas explícitamente a la conversación** antes de ejecutar:```
{{SUBAGENT_NAME}} = PageAgent-N
{{MODEL}}           = SUBAGENT_MODEL
{{THINKING_EFFORT}} = SUBAGENT_THINKING_EFFORT
{{PROMPT_PATH}}   = OUTPUT_DIR/runtime/prompt-page-orchestrator-N.md
```> El subagente está completamente aislado: Solo puede ver el contenido del prompt orquestador y leerá progresivamente los prompts de las fases basándose en las instrucciones del orquestador de forma interna y autónoma.

> Internamente el subagente avanzará autónomamente según las instrucciones del orquestador:
> 1. Primero lee el prompt de planning -> Completa el diseño de la diapositiva -> Produce `planningN.json`
> 2. Lee de forma autónoma el prompt html -> Completa el boceto de diseño en código -> Produce `slide-N.html`
> 3. Lee de forma autónoma el prompt review -> Revisa con capturas de pantalla y corrige (Mínimo 2 rondas) -> Produce `slide-N.png`
> 4. Cuando los errores P0+P1 lleguen a cero + el `visual_qa` apruebe, hace FINALIZE.

---

### 4.3A Opcional: Punto de ruptura de auditoría manual / Retrabajo externo en el Step 4

Cuando se registre `manual_audit_mode != off` en el Step 0, o cuando el usuario solicite explícitamente "ver una imagen en particular / usar el runtime / reiniciar desde cierto nodo" durante la ejecución, el agente principal debe cambiar a esta rama.

**Casos de uso aplicables:**

- El usuario quiere revisar `planningN.json` antes de decidir si continuar.
- El usuario quiere revisar el estado actual de `slide-N.html` o el `slide-N.png` final.
- El usuario señala una imagen específica `review/roundX/slide-N.png`.
- El usuario provee un prompt adicional solicitando reiniciar la ejecución desde `planning` / `html` / `review`.

**1. Generar prompt orquestador para parches externos:**

```bash
# 1a. Primero generar y validar la solicitud de retrabajo
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/step4/tpl-page-audit-request.md \
  --var PAGE_NUM=N \
  --var START_STAGE=html \
  --var END_STAGE=review \
  --var USER_AUDIT_REQUEST="La solicitud del usuario sobre revisión de imagen o cambio de borrador (comprimida a 1 línea)" \
  --var TARGET_ASSET_PATH=OUTPUT_DIR/review/round2/slide-N.png \
  --var RUNTIME_CONTEXT_PATHS="OUTPUT_DIR/runtime/prompt-page-html-N.md; OUTPUT_DIR/runtime/prompt-page-review-N.md; OUTPUT_DIR/runtime/page-html-resolve-N.md; OUTPUT_DIR/runtime/page-html-output-N.html" \
  --var PLANNING_OUTPUT=OUTPUT_DIR/planning/planningN.json \
  --var SLIDE_OUTPUT=OUTPUT_DIR/slides/slide-N.html \
  --var PNG_OUTPUT=OUTPUT_DIR/png/slide-N.png \
  --output OUTPUT_DIR/runtime/page-audit-request-N.txt

python3 SKILL_DIR/scripts/contract_validator.py page-audit-request OUTPUT_DIR/runtime/page-audit-request-N.txt --base-dir OUTPUT_DIR

# 1b. Luego generar el prompt orquestador de parche externo
python3 SKILL_DIR/scripts/prompt_harness.py \
  --template SKILL_DIR/references/prompts/step4/tpl-page-breakpoint-orchestrator.md \
  --var PAGE_NUM=N \
  --var TOTAL_PAGES=TOTAL \
  --var AUDIT_REQUEST_PATH=OUTPUT_DIR/runtime/page-audit-request-N.txt \
  --var START_STAGE=html \
  --var END_STAGE=review \
  --var PLANNING_PROMPT_PATH=OUTPUT_DIR/runtime/prompt-page-planning-N.md \
  --var HTML_PROMPT_PATH=OUTPUT_DIR/runtime/prompt-page-html-N.md \
  --var REVIEW_PROMPT_PATH=OUTPUT_DIR/runtime/prompt-page-review-N.md \
  --var PLANNING_OUTPUT=OUTPUT_DIR/planning/planningN.json \
  --var SLIDE_OUTPUT=OUTPUT_DIR/slides/slide-N.html \
  --var PNG_OUTPUT=OUTPUT_DIR/png/slide-N.png \
  --var SUBAGENT_LOG_PATH=OUTPUT_DIR/runtime/page-patch-agent-N.log \
  --var SUBAGENT_NAME=PagePatchAgent-N \
  --var SKILL_DIR='$SKILL_DIR' \
  --var TARGET_ASSET_PATH=OUTPUT_DIR/review/round2/slide-N.png \
  --var RUNTIME_CONTEXT_PATHS="OUTPUT_DIR/runtime/prompt-page-html-N.md; OUTPUT_DIR/runtime/prompt-page-review-N.md" \
  --var USER_AUDIT_REQUEST="La solicitud del usuario sobre revisión de imagen o cambio de borrador" \
  --output OUTPUT_DIR/runtime/prompt-page-breakpoint-N.md
```

> Si no hay ninguna imagen nombrada o archivo runtime adicional por el momento, rellena `TARGET_ASSET_PATH` o `RUNTIME_CONTEXT_PATHS` con la palabra `none`.

**2. Crear `PagePatchAgent-N` y Ejecutar:**

```
{{SUBAGENT_NAME}} = PagePatchAgent-N
{{MODEL}}           = SUBAGENT_MODEL
{{THINKING_EFFORT}} = SUBAGENT_THINKING_EFFORT
{{PROMPT_PATH}}   = OUTPUT_DIR/runtime/prompt-page-breakpoint-N.md
```

**3. Reglas de Inicio (Start):**

- `START_STAGE=planning`: Rehacer planificación y continuar de `html -> review`.
- `START_STAGE=html`: Reutilizar el planning existente, rehacer de `html -> review`.
- `START_STAGE=review`: Reutilizar el planning + html existente, ir directamente a corrección visual y tomar otra captura.

**4. Reglas de Fin (End):**

- `END_STAGE=planning`: Solo sacar el `planningN.json` actualizado, para conformación de punto de ruptura intermedio.
- `END_STAGE=html`: Solo sacar el `slide-N.html` actualizado, para conformación de punto de ruptura intermedio.
- `END_STAGE=review`: Sacar el `slide-N.png` actualizado; luego debe seguir yendo a 4.4 inspección final de la página entera.

---

### 4.4 Recopilación FINALIZE — Inspección final de página entera por el agente principal

**Paso 1: Presencia de los productos + Verificación de contrato**

```bash
test -s OUTPUT_DIR/planning/planningN.json
python3 SKILL_DIR/scripts/planning_validator.py OUTPUT_DIR/planning --refs SKILL_DIR/references --page N
test -s OUTPUT_DIR/slides/slide-N.html
test -s OUTPUT_DIR/png/slide-N.png
```

**Paso 2: Aserciones visuales automáticas (Primer filtro)**

```bash
python3 SKILL_DIR/scripts/visual_qa.py OUTPUT_DIR/png/slide-N.png --planning OUTPUT_DIR/planning/planningN.json --html OUTPUT_DIR/slides/slide-N.html
# exit=1 -> Defecto fatal, volver a ejecutar inmediatamente
# exit=2 -> Advertencia de calidad, enfocarse en los elementos WARN durante el Paso 3 al revisar la imagen
```

**Paso 3 (Puerta de calidad principal): El agente principal revisa personalmente la captura de pantalla**

> Ésta es la última línea de defensa en todo el sistema de calidad. `visual_qa.py` solo detecta fallos garrafales; la calidad tipográfica, integridad del contenido, y armonía visual DEBEN ser confirmadas visualmente por el agente principal en persona.

1. Usa la capacidad de inspección de imágenes de tu host para visualizar `OUTPUT_DIR/png/slide-N.png`.
2. Presta especial atención a:
   - ¿Es legible el texto? ¿La tipografía es normal? (Verifica columnas de palabras verticales, truncamiento por desbordamiento de texto, etc.)
   - ¿Está completo el contenido de la tarjeta? (Compara contra la lista de tarjetas en el planning del subagente al hacer FINALIZE).
   - ¿La apariencia general es armoniosa visualmente? (No debe verse como un "borrador", ni como HTML en bruto por defecto).
   - ¿Son correctos los elementos de advertencia (WARN) del archivo `visual_qa.py`?
3. Si notas un problema obvio -> Marca esta página como un fallo, inicia re-ejecución.

**Regla de Juicio**: Si `visual_qa exit=1` o si el agente principal al mirar la imagen descubre problemas visuales obvios, se considera un fallo de la página, y se desencadenará la re-ejecución de toda la página.

---

**Condiciones de Activación (Cualquiera es válida):**
- `planningN.json` no existe, está vacío, o `planning_validator.py` falla.
- `slide-N.html` no existe o está vacío.
- `slide-N.png` no existe o está vacío.
- El código de salida de `visual_qa.py` es 1 (defecto fatal).
- El agente principal revisando en persona ve defectos visuales obvios.

**Independientemente de si es en la misma conversación o a través de diferentes conversaciones, usa dos pasos:**

**Paso Uno: Exploración** -- Lee `outline.txt` para obtener el total de páginas, itera todas para recoger la lista de páginas fallidas:

```bash
# Por cada página de 1..N:
test -s OUTPUT_DIR/planning/planningN.json && \
test -s OUTPUT_DIR/slides/slide-N.html && \
test -s OUTPUT_DIR/png/slide-N.png && \
python3 SKILL_DIR/scripts/planning_validator.py OUTPUT_DIR/planning --refs SKILL_DIR/references --page N && \
python3 SKILL_DIR/scripts/visual_qa.py OUTPUT_DIR/png/slide-N.png --planning OUTPUT_DIR/planning/planningN.json --html OUTPUT_DIR/slides/slide-N.html
# Si exit != 0 en cualquiera de ellos -> añade a la lista de páginas fallidas
```

> Después de que la detección automática apruebe, el agente principal igual debe mirar la imagen; `visual_qa.py` no sustituye a las verificaciones de estética humanas.

**Paso Dos: Re-ejecutar en Paralelo** -- Tras recoger, lanza todas las páginas fallidas en paralelo simultáneamente (no secuencialmente):

```bash
# Para cada página en la lista de fallos [N1, N2, ...], limpia los viejos artefactos y posibles capturas de revisión:
python3 -c "import os, glob; [os.remove(p) for p in ['OUTPUT_DIR/planning/planningN.json','OUTPUT_DIR/slides/slide-N.html','OUTPUT_DIR/png/slide-N.png'] + glob.glob('OUTPUT_DIR/review/round*/slide-N.png') if os.path.exists(p)]"
# Empieza a re-ejecutar desde la etapa de generación de prompt en el Step 4: genera el prompt, luego crea PageAgent-N, y después RUN orchestrator
```

> Todas las sesiones se consideran NO reanudables (muerte de subagente = pérdida de contexto), toda la página debe ser re-ejecutada empezando desde el 4.1.
> Cuando se reanuda a través de conversaciones, las sesiones antiguas son inválidas por completo, usando esta misma lógica.

---

## Step 5 Exportación

Línea de ejecución:

```bash
# 1. Vista previa
python3 SKILL_DIR/scripts/html_packager.py OUTPUT_DIR/slides -o OUTPUT_DIR/preview.html

# 2. Pipeline PNG (Paralelo a SVG)
# --scale 3 → Output de PNGs alta definición a 3840x2160 para PPT (la revisión usa 0.75 para ahorrar tokens, los propósitos son diferentes)
python3 SKILL_DIR/scripts/html2png.py OUTPUT_DIR/slides -o OUTPUT_DIR/png --scale 3
python3 SKILL_DIR/scripts/png2pptx.py OUTPUT_DIR/png -o OUTPUT_DIR/presentation-png.pptx

# 3. Pipeline SVG (Paralelo a PNG)
python3 SKILL_DIR/scripts/html2svg.py OUTPUT_DIR/slides -o OUTPUT_DIR/svg
python3 SKILL_DIR/scripts/svg2pptx.py OUTPUT_DIR/svg -o OUTPUT_DIR/presentation-svg.pptx --html-dir OUTPUT_DIR/slides

# 4. Manifiesto de Entregables
# El agente principal escribe delivery-manifest.json bajo el esquema a continuación
```

**Esquema requerido de delivery-manifest.json**:

```json
{
  "run_id": "RUN_ID (corresponde a OUTPUT_DIR)",
  "generated_at": "Timestamp en formato ISO 8601 (ej. 2026-04-01T14:30:00Z)",
  "summary": {
    "total_pages": Número de páginas (entero positivo)
  },
  "artifacts": {
    "preview_html": "preview.html (relativo a OUTPUT_DIR)",
    "presentation_png_pptx": "presentation-png.pptx",
    "presentation_svg_pptx": "presentation-svg.pptx"
  },
  "pages": [
    { "page": 1, "planning": "planning/planning1.json", "html": "slides/slide-1.html", "png": "png/slide-1.png" }
  ]
}
```

> `run_id`, `generated_at`, `artifacts` (con las tres rutas) son obligatorios para el script del validator; `summary` y `pages` están altamente recomendados.

Validación (Gate):

```bash
python3 SKILL_DIR/scripts/contract_validator.py delivery-manifest OUTPUT_DIR/delivery-manifest.json --base-dir OUTPUT_DIR
```

---

## Enrutamiento de Recursos

Menú (fase de planificación):

```bash
python3 SKILL_DIR/scripts/resource_loader.py menu \
  --refs-dir SKILL_DIR/references \
  --output OUTPUT_DIR/runtime/page-planning-menu-N.md
```

Resolución (fase de html):

```bash
python3 SKILL_DIR/scripts/resource_loader.py resolve --refs-dir SKILL_DIR/references --planning OUTPUT_DIR/planning/planningN.json
```

Inventario de Imágenes (fase de planificación / html):

```bash
python3 SKILL_DIR/scripts/resource_loader.py images --images-dir OUTPUT_DIR/images
```

---

## Hito Final (Verificación de hitos)

```bash
python3 SKILL_DIR/scripts/milestone_check.py <stage> --output-dir OUTPUT_DIR
```

---

## Lista de Contract-Types para el Validador de Contratos

`entrevista` / `requisitos-entrevista` / `búsqueda` / `búsqueda-brief` / `source-brief` / `esquema` / `estilo` / `imágenes` / `revisión-de-página` / `solicitud-de-auditoría-de-página` / `manifiesto-de-entrega`

Formato general:

```bash
python3 SKILL_DIR/scripts/contract_validator.py <contract-type> <target-file> [--base-dir OUTPUT_DIR]
```

---

## Aserción de Calidad Visual

> Este es el primer filtro automatizado post-recolección del Step 4. Detecta problemas flagrantes (baja resolución, blancos excesivos, corrupción de archivos). La verdadera apreciación de estética visual la hace el agente principal viendo las capturas en persona.

Página única:

```bash
python3 SKILL_DIR/scripts/visual_qa.py OUTPUT_DIR/png/slide-N.png --planning OUTPUT_DIR/planning/planningN.json --html OUTPUT_DIR/slides/slide-N.html
```

Procesamiento por Lotes:

```bash
python3 SKILL_DIR/scripts/visual_qa.py OUTPUT_DIR/png --planning-dir OUTPUT_DIR/planning --html-dir OUTPUT_DIR/slides
```

Código de salida: `0` = Aprobado, `1` = FAIL (Defecto fatal, DEBE re-ejecutarse), `2` = WARN (Advertencia de calidad, revisar manualmente las capturas de imagen).

Dependencias: `pip install Pillow`