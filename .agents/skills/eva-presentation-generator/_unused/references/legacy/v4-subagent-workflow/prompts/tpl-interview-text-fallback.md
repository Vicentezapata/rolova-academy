# Cuestionario de entrevista (texto alternativo)

Tema: {{TEMA}}
Antecedentes del usuario: {{USER_CONTEXT}}

---

## Modo de ejecución actual

El entorno actual no admite la interfaz de usuario de entrevista estructurada nativa. Debe recurrir a una **hoja de entrevista de texto estructurado** en lugar de una línea de preguntas para completar en blanco o divagaciones.

{{INTERVIEW_MODE_MODULE}}

---

## Compartir el núcleo de la entrevista

{{INTERVIEW_CORE}}

---

## Requisitos finales

- Brinde directamente a los usuarios una hoja de entrevista de Markdown claramente agrupada.
- No degeneres en el formato de una sola línea `escenario=;audiencia=;acción objetivo=...`
- Permitir a los usuarios escribir "predeterminado", pero la cobertura del campo no puede ser menor
- Si el usuario solo responde a "todo predeterminado, usar investigación", aún debe completar campos clave como `material_strategy: investigación` de acuerdo con el punto de ubicación predeterminado del núcleo compartido.
- Una vez completada la recopilación, el agente principal escribe `interview-qa.txt` y `requirements-interview.txt`.
- Al escribir `interview-qa.txt`, debe agregar la sección de anclaje canónica y escribir explícitamente campos clave como `target_action`, `must_avoid`, `material_strategy`, `subagent_model_strategy`, `subagent_thinking_effort`, `manual_audit_mode`, `manual_audit_scope`, `manual_audit_assets` y otros campos clave para evitar validador perdido debido a la respuesta corta del usuario