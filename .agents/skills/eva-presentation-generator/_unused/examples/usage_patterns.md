# Ejemplos de Uso: EVA Presentation Generator

Esta guía contiene ejemplos de *prompts* (instrucciones) que puedes usar para invocar al Agente y asegurarte de que utilice correctamente el **Pipeline de 5 Fases** de esta skill.

---

## 1. Creación Completa (Pipeline Estándar — Fases 1 a 5)

La forma recomendada de crear una presentación desde cero. El agente ejecutará automáticamente las Fases 0, 1 y 2, y se detendrá en la Fase 3 para pedirte aprobación antes de generar el HTML.

**Prompt de ejemplo:**
> "Quiero crear una presentación para la Unidad 3. Todo el material base está en la carpeta `./cursos/unidad3/material`. Utiliza la herramienta `all2md` para procesar y unificar los documentos de esa carpeta. Quiero usar el tema visual `dark_tech`. La presentación debe ser extensa y muy detallada. Si notas que el material base es escaso, por favor investiga y complementa el contenido con buenas prácticas y tendencias. Empieza entregándome el borrador con el esquema de diapositivas y el plan visual, sin programar nada todavía."

**Lo que ocurrirá:**
1. **Fase 0**: El agente cargará las specs del canvas, tipografía y el tema `dark_tech`.
2. **Fase 1**: Procesará el material con `all2md`, clasificará cada slide por tipo de dato, y generará el `outline.json`.
3. **Fase 2**: Seleccionará layouts, card types, gráficos CSS y decoraciones para cada slide, generando el `visual_plan.json`.
4. **Fase 3 (Validación Automática)**: El agente correrá el script `planning_validator.py` internamente para asegurarse de que el JSON cumple con las reglas de densidad y diseño. Solo si pasa, te presentará el plan.
5. **Aprobación y Fase 4**: Tras tu OK, ensamblará el HTML usando el enrutador de recursos `resource_loader.py`.
6. **Fase 5 (QA Visual)**: Al finalizar, el agente tomará capturas PNG y ejecutará `visual_qa.py` para verificar píxel a píxel que no hay recortes de texto ni problemas de contraste.

---

## 2. Aprobación del Plan Visual (Fase 3 → Fase 4)

Una vez que el agente te entrega el borrador con el plan visual y estás conforme, autoriza la generación del código HTML.

**Prompt de ejemplo:**
> "El plan visual me parece perfecto. Procede con la generación de los archivos HTML. Recuerda crear el `preview.html`, `presenter.html`, el `notas_orador.js` y el `serve.py`."

**Prompt con ajustes antes de aprobar:**
> "Me gusta el plan general, pero quiero estos cambios:
> - Slide 5: Cambia el layout de `symmetric` a `hero-top`, quiero que el concepto principal domine.
> - Slide 9: Añade un gráfico tipo `radar` para visualizar las métricas.
> - Slide 12: Usa una decoración W1 (texto con gradiente) en el título.
> Con esos ajustes, procede a generar."

---

## 3. Solicitar Layouts y Bloques Específicos

Si quieres que una diapositiva en particular use un diseño concreto de la biblioteca de `references/`.

**Prompt de ejemplo (Layouts):**
> "Para la slide 4, donde hablamos de la evolución de HTML, quiero que uses el layout `waterfall` (cascada temporal). Para la slide 7 de ventajas y desventajas, usa el layout `symmetric` con bloques tipo `comparison`. Aplica el layout `hero-top` con un bloque `image-hero` a la portada."

**Prompt de ejemplo (Gráficos CSS):**
> "En la slide 10 tenemos 4 KPIs de rendimiento. Quiero que uses el gráfico tipo `ring` (anillo) de `references/charts/basic.md` para cada uno, dentro de un layout `mixed-grid`."

**Prompt de ejemplo (Decoraciones CSS Weapons):**
> "Quiero que la slide 1 (portada) use la decoración W3 (spotlight con mask-image) y W1 (título con gradiente). La slide 15 debe tener W7 (glassmorphism) en las tarjetas."

---

## 4. Explorar Estilos Disponibles (26 Temas)

Si no sabes qué tema usar, puedes pedirle al agente que consulte la matriz de decisión de estilos.

**Prompt de ejemplo:**
> "No estoy seguro de qué tema usar para una clase de ciberseguridad. ¿Puedes consultar la matriz de decisión en `references/styles/index.md` y recomendarme los 3 temas más adecuados?"

**Prompt para ver el catálogo completo:**
> "Muéstrame una tabla con los 26 temas disponibles y sus escenarios de uso. Consulta `references/styles/index.md`."

---

## 5. Cambio de Tema (Re-estilización)

Si ya generaste una presentación pero quieres cambiar el estilo visual sin perder el contenido.

**Prompt de ejemplo:**
> "Ya tengo generada la presentación de la Unidad 1 con `dark_tech`. Ahora quiero que apliques el tema `cyberpunk_neon`. Consulta la definición en `references/styles/dark.md`, reemplaza las variables CSS y regenera las slides manteniendo el mismo `visual_plan.json`."

---

## 6. Ajustes de Contenido Post-Generación

Si la presentación ya fue generada pero necesitas ajustar la densidad de texto o la distribución del contenido.

**Prompt de ejemplo (Reducir texto):**
> "Revisa la presentación de la Unidad 4. En la slide 5 veo demasiado texto. Mueve el exceso al archivo `notas_orador.js` y deja solo 3 viñetas breves en pantalla. Recuerda la Regla de Respiro Visual."

**Prompt de ejemplo (Mejorar diseño):**
> "La slide 8 se ve muy plana. Consulta `references/design-runtime/css-weapons.md` y aplica 2 decoraciones CSS para darle más impacto visual. Sugiero W5 (bordes gradiente) y W10 (sombras multicapa)."

---

## 7. Exportación a PPTX

Si necesitas una versión PowerPoint nativa de la presentación.

**Prompt de ejemplo:**
> "Necesito exportar la presentación de la Unidad 2 a un archivo PPTX nativo. Escribe y ejecuta un script Python usando Playwright y python-pptx que itere sobre `preview.html`, tome capturas de pantalla de 1280×720 y arme el archivo `.pptx` final."

---

## 8. Generación con Material Escaso (Investigación Autónoma)

Cuando el material de la unidad es insuficiente para llenar 20+ slides.

**Prompt de ejemplo:**
> "Genera la presentación para la Unidad 5 de Testing. El material en la carpeta `material/` es muy escaso (solo 2 PDFs cortos). Necesito que investigues autónomamente sobre las mejores prácticas actuales de testing, frameworks modernos (Jest, Cypress, Playwright), y metodologías TDD/BDD para complementar. La presentación debe tener al menos 25 slides."

---

## 9. Uso del Modo Full-Deck

Si prefieres usar un template completo en lugar de ensamblar con componentes individuales.

**Prompt de ejemplo:**
> "Genera la presentación para la Unidad 4. Usa el full-deck `tech-sharing` (ubicado en `templates/full-decks`). Toma el `index.html` de esa plantilla como base, duplica los moldes para que quepa todo el contenido, inyecta mi material educativo, y genera el archivo final con `serve.py`."

---

## 10. Solicitar Quizzes Interactivos

Para añadir actividades de activación o gamificación a la presentación.

**Prompt de ejemplo:**
> "Quiero que después de cada capítulo (Part) incluyas una slide de quiz interactivo usando el template `knowledge-check.html`. La pregunta debe estar relacionada con los conceptos clave del capítulo anterior. Al hacer clic se debe revelar la respuesta correcta."

---

## 11. Solicitar Ilustraciones con IA

Si el material original carece de imágenes y quieres portadas o diagramas generados con IA.

**Prompt de ejemplo:**
> "Para la portada (slide 0), genera una ilustración usando `generate_image` con el estilo del tema `dark_tech`: un entorno futurista con circuitos y código flotante. Para la slide 12 (arquitectura MVC), genera un diagrama conceptual que muestre la separación de capas."

---

## Consejos Generales

- **Empieza siempre con la Fase 1-3**: Nunca pidas código directamente. El pipeline de fases garantiza que el diseño será creativo y profesional.
- **Confía en las referencias y validadores**: El agente usa scripts en Python (`planning_validator.py`, `visual_qa.py`) para garantizar que la presentación final sea robusta. Permite que ejecute sus autocomprobaciones.
- **Revisa el `visual_plan.json`**: En la Fase 3, el agente te mostrará exactamente qué layout, bloques y decoraciones usará en cada slide. Es tu oportunidad de ajustar antes de generar.
- **Usa el servidor local**: Siempre ejecuta `python serve.py` para visualizar la presentación en `http://localhost:8000`. Abrir los archivos directamente con `file://` causará errores de CORS.
