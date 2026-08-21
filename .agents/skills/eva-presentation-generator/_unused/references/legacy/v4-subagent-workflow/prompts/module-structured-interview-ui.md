# Modo de interfaz de usuario estructurado: entrevista estructurada nativa CLI

## Requisitos de refinamiento y enriquecimiento (disciplina de ejecución)

1. **Interacción extremadamente silenciosa**: genera directamente componentes estructurales y está estrictamente prohibido intercalar "preguntas de motivos/instrucciones de pasos/saludos hablados".
2. **Rechace la sequedad y ofrezca alternativas de alta densidad**: no se limite a utilizar palabras secas como “negocios” y “geek”. Se debe extraer una imagen estética/lógica específica de la "etiqueta" o "descripción" de cada opción.
   -*Contraejemplo*: `{etiqueta: "Estilo empresarial"}`
   -*Ejemplo*: `{etiqueta: "Negocio minimalista", descripción: "Estilo Apple, gran espacio en blanco, refinado sin gráficos, adecuado para informes avanzados"}`
3. **Inducción de circuito cerrado**: No se permite completar los espacios en blanco de todos los campos principales. Todas las categorías se convierten en opciones altamente profesionales e inspiradoras (con "otras" aperturas), lo que induce a los usuarios a proporcionar parámetros completos que puedan satisfacer a los usuarios intermedios.
4. **Alineación explícita de nombres de capacidades**: primero llame a `AskUserQuestion`; si el nombre de la capacidad correspondiente al entorno de host es `request_user_input`, también se considera una implementación sinónima y se ejecuta de acuerdo con el mismo contrato de entrevista estructurado.

## Esqueleto de formato de componente

Utilice los mejores componentes admitidos por el sistema (como `pregunta/encabezado/id/opciones`) y asegúrese de que la estructura sea la siguiente:

```text
questions: [
  {
    header: "...",
    id: "...",
    question: "...",
    options: [
      { label: "...", description: "..." }
    ]
  }
]
```

## Restricciones de campo y problema

- Cubra al menos `presentation_scenario`, `core_audience`, `target_action`, `expected_pages`, `page_density`, `visual_style`, `language_mode`, `imagery_strategy`, `material_strategy`, `manual_audit_mode`
- `presentation_scenario`, `core_audience`, `visual_style`, `language_mode`, `imagery_strategy`, `material_strategy`, `manual_audit_mode` deben convertirse primero en preguntas de opción múltiple
- `manual_audit_scope`, `manual_audit_assets`, `must_include`, `must_avoid`, `brand_constraints`, `success_criteria`, `subagent_model_strategy` se pueden recopilar a través de la segunda ronda de preguntas estructuradas u "otra" recopilación complementaria