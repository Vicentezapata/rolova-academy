# Cuestionario de entrevista (UI estructurada)

Tema: {{TEMA}}
Antecedentes del usuario: {{USER_CONTEXT}}

---

## Modo de ejecución actual

El entorno actual ha confirmado la compatibilidad con la interfaz de usuario de entrevista estructurada nativa. Debe priorizar el uso de las capacidades de preguntas estructuradas integradas de la CLI en lugar de generar directamente párrafos largos de preguntas de texto ordinarias.

{{INTERVIEW_MODE_MODULE}}

---

## Compartir el núcleo de la entrevista

{{INTERVIEW_CORE}}

---

## Requisitos finales

- Priorizar la recopilación de dimensiones de alta señal al mismo tiempo; si el número de preguntas es limitado, se puede dividir en 2 rondas
- **Debe crear** `presentation_scenario`, `core_audience`, `target_action`, `page_density`, `visual_style`, `language_mode`, `imagery_strategy`, `material_strategy`, `manual_audit_mode` en una selección estructurada con ricas alternativas
- Antes de escribir en el disco, normalice según el mapeo de campos del núcleo compartido: `presentación_escenario -> escenario`, `core_audience -> audiencia`, `visual_style -> estilo`, `brand_constraints -> marca`, `language_mode -> idioma`, `imagery_strategy -> imagery`
- Permitir a los usuarios agregar libremente elementos abiertos o seleccionar "Otros"
- Una vez completada la recopilación, el agente principal escribe `interview-qa.txt` y `requirements-interview.txt`.
- Al escribir `interview-qa.txt`, debe agregar la sección de anclaje canónica y escribir explícitamente campos clave como `target_action`, `must_avoid`, `material_strategy`, `subagent_model_strategy`, `subagent_thinking_effort`, `manual_audit_mode`, `manual_audit_scope`, `manual_audit_assets` y otros campos clave para evitar validador perdido debido a la respuesta corta del usuario