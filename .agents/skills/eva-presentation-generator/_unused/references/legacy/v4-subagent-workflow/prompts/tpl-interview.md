#Entrevista Cuestionario Núcleo compartido

> Este archivo es el contrato de contenido de la entrevista compartida del Paso 0 y no se envía directamente al agente principal como mensaje de tiempo de ejecución.
> El tiempo de ejecución debe seleccionar `tpl-interview-structured-ui.md` o `tpl-interview-text-fallback.md` según las capacidades.

## Objetivos principales de la entrevista (guía de ejecución)

Como primer nodo guardián del sistema, debe obtener una entrada con una relación señal-ruido extremadamente alta en la ronda más eficiente. Objetivo principal: bloquear directamente los parámetros dimensionales clave que pueden influir en la estructura del esquema, el estilo visual y las ramas del canal sin chatear con los usuarios.

## 4 conjuntos de dimensiones que deben cubrirse (más 1 conjunto de extensiones de auditoría manual)

Las opciones que ofrezca a los usuarios deben cubrir con precisión los cuatro conjuntos básicos de campos de dimensiones y agregar un conjunto adicional de dimensiones extendidas de auditoría manual.

### A. Escenarios empresariales y objetivos de comunicación

Determine la profundidad del contenido y el tono narrativo.

- `presentación_escenario` (normalizado a `escenario`): Introducción de recién llegados/informe interno/presentación de la comunidad/cooperación en inversiones/exhibición itinerante de financiación/divulgación científica pública, etc.
- `core_audience` (normalizado a `audience`): "¿Quién eres y a quién le vas a contar en el escenario?" Por ejemplo, un comerciante de primera línea solicita recursos a la alta dirección / un número uno de la empresa predica a los clientes / un conferenciante populariza la ciencia entre el público en general y los principiantes.
- `target_action`: generar conciencia / promover la intención / estar dispuesto a unirse / sincronización pura de información

### B. Densidad estructural y cartera de producción.

El número de páginas en los esquemas izquierdo y derecho, la disposición de las imágenes y el texto y la adquisición de fuentes de datos.

- `expected_pages`: 5-10 páginas / 10-20 páginas / 20-30 páginas de ancho / juego libre
- `page_density`: poca pero precisa/moderada/gran capacidad (nota: esta es la tendencia general de toda la plataforma, no requiere que cada página tenga exactamente la misma densidad)
- `material_strategy`: `research` (expansión de toda la red) o `local_only` (solo materiales proporcionados actualmente)
- `must_include` / `must_avoid`: se puede pedir a los usuarios que agreguen la única propuesta central y áreas absolutamente prohibidas

### C. Estética visual y estrategia de activos.

Bloqueo estético para posteriores generadores de Estilo/HTML.

- `visual_style` (normalizado a `style`): negocio minimalista/geek tecnológico/ligero y animado/combinación automática
- `language_mode` (normalizado a `language`): chino/inglés/chino e inglés mixto
- `imagery_strategy` (normalizado a `imagery`): decorar/generar/proporcionar/manual_slot
- `brand_constraints` (normalizado a `brand`): tabúes visuales de la marca, colores principales, preferencias de fuente, límites de uso del logotipo

### D. Entorno de construcción e interfaz de ingeniería

- `success_criteria`: criterios de evaluación del usuario
- `subagent_model_strategy`: hereda el agente principal/especifica un modelo más potente/especifica un modelo más rápido
- `subagent_thinking_effort`: bajo/medio/alto

### E. Auditoría manual y control de puntos de interrupción

- `manual_audit_mode`: `off` (no participar) / `milestone_only` (solo ver nodos clave) / `fine_grained` (puntos de interrupción detallados)
- `manual_audit_scope`: qué nodos desea intervenir, como `outline` / `style` / `page_planning` / `page_html` / `page_review`
- `manual_audit_assets`: `summary_only` (ver solo el resumen del agente principal) / `png_only` (ver imágenes) / `runtime_and_selected_assets` (permitir hacer clic directo en runtime / html / para especificar la imagen de revisión)

## Mapeo de normalización de campo

Durante la fase de entrevista, se da prioridad al nombre de la colección canónica anterior; al escribir, se unifica y normaliza con el nombre del ancla consumido actualmente por el validador y el libro de jugadas descendente.

| 采集字段 | 写入 `entrevista-qa.txt` / `requisitos-entrevista.txt` 的锚点 |
|---|---|
| `escenario_presentación` | `escenario` |
| `core_audience` | `audiencia` |
| `acción_objetivo` | `acción_objetivo` |
| `páginas_esperadas` | `páginas_esperadas` |
| `densidad_página` | `densidad_página` |
| `estilo_visual` | `estilo` |
| `restricciones_de_marca` | `marca` |
| `debe_incluir` | `debe_incluir` |
| `debe_evitar` | `debe_evitar` |
| `modo_idioma` | `lenguaje` |
| `estrategia_imagenes` | `imágenes` |
| `estrategia_material` | `estrategia_material` |
| `subagent_model_strategy` | `subagent_model_strategy` |
| `subagent_thinking_effort` | `subagent_thinking_effort` |
| `modo_auditoría_manual` | `modo_auditoría_manual` |
| `alcance_auditoría_manual` | `alcance_auditoría_manual` |
| `activos_de_auditoría_manual` | `activos_de_auditoría_manual` |

## `interview-qa.txt` Escribir punto de anclaje del disco (obligatorio)

Todos los resultados del cuestionario deben asignarse a los dos productos siguientes como la verdadera fuente de entrada para los subagentes posteriores.

1. `entrevista-qa.txt`
   Mantenga la intención original del usuario. Para pasar una validación sólida a través de `contract_validator.py`, se debe agregar un segmento de anclaje canónico al final. Los 12 puntos de anclaje básicos son indispensables, y los puntos de anclaje de auditoría manual y modelo se agregan de forma predeterminada:
   `escenario`, `audiencia`, `acción_objetivo`, `páginas_esperadas`, `densidad_de_página`, `estilo`, `marca`, `debe_incluir`, `debe_evitar`, `idioma`, `imágenes`, `estrategia_material`, `estrategia_modelo_subagente`, `esfuerzo_pensamiento_subagente`, `modo_auditoría_manual`, `manual_audit_scope`, `manual_audit_assets`

2. `requisitos-entrevista.txt`
   El grupo de parámetros puros deshidratados también debe incluir los 12 puntos de anclaje básicos anteriores, así como puntos de anclaje de auditoría manual/modelo, y aportar valores enriquecidos y claros para el consumo directo del validador, estilo, esquema, PageAgent y nodos de retrabajo manual posteriores.
   Si el agente principal ha completado la normalización, puede agregar adicionalmente `density_bias: relajado/equilibrado/ultra_denso` como un campo derivado interno; si no se agrega, el canal descendente debe derivarlo por sí mismo en función de `page_density` y no se informará ningún error.