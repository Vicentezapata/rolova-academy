# Etapa 2: Producción de página HTML: página {{PAGE_NUM}} de {{TOTAL_PAGES}}

> **Subagente**: `{{SUBAGENT_NAME}}` · **Paso**: html · **Página**: {{PAGE_NUM}}/{{TOTAL_PAGES}}

> **【Instrucciones obligatorias a nivel del sistema / ANULACIÓN CRÍTICA】**
> Este mensaje contiene **todos** los objetivos de la misión y los detalles del Playbook que necesitas para esta etapa.
> **¡Está estrictamente prohibido llamar a herramientas para leer el `SKILL.md` externo o el archivo maestro de reglas globales! **
>
> **Condición previa**: La fase de planificación se ha completado y `{{PLANNING_OUTPUT}}` está listo.
> El único objetivo de esta etapa: generar `{{SLIDE_OUTPUT}}` basado en la planificación JSON. Envíe la señal FINALIZAR cuando haya terminado.
> Si el orquestador externo ha proporcionado un protocolo de avance de etapa, el protocolo externo tiene prioridad sobre la descripción de la señal de finalización en este mensaje.

Esta es su tarea **principal de la segunda fase** para la página {{PAGE_NUM}}: generación de diseño HTML.
Su borrador de planificación (`{{PLANNING_OUTPUT}}`) es el insumo principal de esta etapa, y su esqueleto debe restaurarse estricta y fielmente.

---

## Playbook (detalles de ejecución)

{{LIBRO DE JUEGOS}}

---

## Paquete de tareas

| proyecto | ruta/valor |
|------|--------|
| Número de página | {{PAGE_NUM}} / {{TOTAL_PAGES}} |
| Borrador de planificación | `{{PLANNING_OUTPUT}}` |
| Pautas de estilo | `{{STYLE_PATH}}` |
| HTML de salida | `{{SLIDE_OUTPUT}}` |
| Instantánea de la lista de imágenes | `{{IMAGE_INVENTORY_PATH}}` |
| Instantánea del cuerpo del recurso | `{{HTML_RESOLVE_PATH}}` |
| Copia de seguridad HTML en tiempo de ejecución | `{{HTML_RUNTIME_COPY_PATH}}` |
| Ejecutar registro | `{{SUBAGENT_LOG_PATH}}` |
| Directorio de HABILIDADES | `{{SKILL_DIR}}` |
| Directorio de recursos | `{{REFS_DIR}}` |
| Directorio de material de imagen | `{{IMAGES_DIR}}` |

---

## Enlace de ejecución (orden fijo, sin omitir)

1. lea `{{PLANNING_OUTPUT}}`, extraiga el esqueleto completo (`page_type`, `layout_hint`, `density_label`, `density_contract`, `focus_zone`, `negative_space_target`, `cards[].card_id/role/card_type/card_style/headline/body/data_points/chart/image/resource_ref`, `director_command`, `decoration_hints`, `source_guidance`, `resources`, `must_avoid`)
2. Lea `{{STYLE_PATH}}` y extraiga `css_variables`, `font_family`, `design_soul`, `variation_strategy`, `decoration_dna`
3. **Debe ejecutarse**: obtenga los **detalles de implementación de la capa del cuerpo** de los recursos a los que se hace referencia en la planificación (no se pueden omitir, hay parámetros CSS a nivel de componente y sugerencias de esqueleto) y haga una copia de seguridad de los resultados en el tiempo de ejecución:```bash
   python3 {{SKILL_DIR}}/scripts/subagent_logger.py run --log {{SUBAGENT_LOG_PATH}} --label html-resolve-resources -- \
     python3 {{SKILL_DIR}}/scripts/resource_loader.py resolve --refs-dir {{REFS_DIR}} --planning {{PLANNING_OUTPUT}} --output {{HTML_RESOLVE_PATH}}
   ```Luego lea `{{HTML_RESOLVE_PATH}}`. La salida del cuerpo del componente mediante resolución es el punto de partida que debe respetarse estrictamente. Usted es el ejecutivo de diseño más estricto: bajo la premisa de garantizar la línea roja física del lienzo de 1280x720, combinada con `page_goal` y `director_command`, utilice código de alta precisión para restaurar el borrador del diseño en el árbol DOM sin compromiso. La revisión de imágenes sólo detectará sus defectos y no tolerará la reconstrucción del esqueleto.
4. Verifique los materiales de imágenes y actualice la instantánea de la lista de imágenes si es necesario:```bash
   python3 {{SKILL_DIR}}/scripts/subagent_logger.py run --log {{SUBAGENT_LOG_PATH}} --label html-refresh-images -- \
     python3 {{SKILL_DIR}}/scripts/resource_loader.py images --images-dir {{IMAGES_DIR}} --output {{IMAGE_INVENTORY_PATH}}
   ```Luego lea `{{IMAGE_INVENTORY_PATH}}` para confirmar que se puede acceder a la ruta `image.source_hint`.
5. **Resumen ejecutivo (debe escribirse primero antes de comenzar)**: resuma la estrategia central de esta página en 3 oraciones, envíela a una conversación y luego comience a escribir HTML:
   - Oración 1: ¿Cuál es el argumento central y el enfoque visual de esta página?
   - Oración 2: Qué estructura de diseño y componentes principales usar
   - Oración 3: Ancla de estilo (cómo se refleja design_soul en esta página)
6. Genere HTML autónomo de acuerdo con las siguientes **líneas rojas físicas del lienzo** (no se pueden violar):
   - `cuerpo {ancho: 1280px; altura: 720 px; desbordamiento: oculto; }` - No escriba 100% ni otros tamaños
   - Deshabilitar el truco de escalado `transform: scale()`
   - Todo el CSS está en línea en la etiqueta `<style>`, no se permiten referencias a archivos CSS externos
   - La fuente toma el valor de `font_family` en `style.json` y se introduce a través de Google Fonts o la pila de fuentes del sistema.
7. Procese la imagen de acuerdo con `image.mode` (**el modo está bloqueado en la etapa de planificación y no se puede cambiar temporalmente aquí**):
   - `generate` / `provided` (`image.needed=true`): vincula la ruta `source_hint` a `<img src>` o `background-image`, la imagen debe estar realmente renderizada
   - `manual_slot` (`image.needed=false`): genera un espacio de imagen claramente reemplazable (con borde/texto emergente), y el espacio no debe eliminarse en secreto
   - `decorar` (`image.needed=false`): no utilice imágenes externas, utilice SVG en línea, bloques de color, degradados y decoraciones de fuentes para complementar la atmósfera visual, y no deje grandes espacios en blanco.
8. **Primero determine el modo de ejecución y luego realice la autoprueba "Yin-Yang Secante"**:
   - `low/mid_low`: alto grado de libertad
   - `medium`: grado de libertad medio
   - `alto/tablero`: bajo grado de libertad, dando prioridad a la cuadrícula/flexión estable, prohibiendo tarjetas con imágenes grandes para la imagen principal, prohibiendo marcas de agua de área grande, prohibiendo la yuxtaposición de múltiples puntos de anclaje principales
9. **Autoprueba de diseño "Yin-Yang Secante" (debe responder y ejecutarse en mente antes de escribir HTML)**:
   - **Cátodo (Leyes irresistibles de la física)**: ¿Los muros de carga subyacentes de esta página cumplen con los requisitos estructurales impuestos por `page_goal` y `director_command`? ¿Ha modificado el punto de anclaje absoluto de la barra de título superior o ha cambiado el flujo de la cuadrícula de forma privada? (Si es así, ¡anule y vuelva a escribir!)
   - **Ánodo (privilegio visual extremadamente explosivo)**: ¿El nivel de tu imagen es lo suficientemente profundo? ¿Es posible eliminar la sensación rígida de la caja de documentos mediante el uso de impactantes marcas de agua oscuras de gran tamaño, superposición y colisión de márgenes negativos y tecnología de tipografía extrema con un tamaño de fuente de más de 5 veces sin tocar la pared de carga?
   - ¡Demuestra que no sólo eres un codificador riguroso, sino también un ávido maestro de la tipografía de vanguardia!
10. **Cada tarjeta de planificación debe tener un nodo raíz de representación correspondiente en HTML** y agregar `data-card-id="<planning.card_id>"` al nodo raíz para facilitar la revisión y la conciliación; si una tarjeta contiene `chart.chart_type`, el resultado de la representación debe coincidir con este tipo.
11. **Todos los nodos puramente decorativos deben estar marcados explícitamente**: use `data-decoration-layer="background|floating|page-accent"` y agregue `aria-hidden="true"`. `visual_qa.py` contará estos nodos de acuerdo con `density_contract.decoration_budget`. Si el presupuesto excede el presupuesto, fracasará directamente.
12. Escriba el HTML completo en `{{SLIDE_OUTPUT}}` y sincronice la copia de seguridad con `{{HTML_RUNTIME_COPY_PATH}}`
    > **🔴 Advertencia absoluta de línea roja 🔴**
    > `{{SLIDE_OUTPUT}}` debe ser 100% código HTML puro.
    > ¡Está absolutamente prohibido escribir el "Resumen ejecutivo" (Paso 5), el "Proceso de autocomprobación" (Paso 8), la "Declaración de intención de planificación" o cualquier instrucción/proceso de pensamiento rápido que no esté relacionado con la representación real de la página en el documento HTML (incluidos `<body>`, `<div>`, `<!--Comments-->`)!
    > Solo puedes generar estas reflexiones en una interfaz conversacional o como un registro separado. El HTML escrito en el archivo debe estar absolutamente limpio y contener sólo elementos de diseño que se ajusten al esqueleto de planificación.```bash
    python3 {{SKILL_DIR}}/scripts/subagent_logger.py run --log {{SUBAGENT_LOG_PATH}} --label html-runtime-copy -- \
      cp {{SLIDE_OUTPUT}} {{HTML_RUNTIME_COPY_PATH}}
    ```13. Señal de finalización: salida `--- ETAPA 2 COMPLETA: {{SLIDE_OUTPUT}} ---`, y luego continúe con la siguiente etapa de acuerdo con el protocolo del orquestador externo

---

## Límite del escenario

- Esta etapa: solo escriba HTML, sin capturas de pantalla, sin control de calidad
- Siguiente etapa: el orquestador lo guiará a la revisión.
- Reglas de consumo de recursos: en esta etapa, se lee la **capa de texto** del recurso (paso 3), en lugar de la capa de resumen del menú utilizada en la etapa de planificación.