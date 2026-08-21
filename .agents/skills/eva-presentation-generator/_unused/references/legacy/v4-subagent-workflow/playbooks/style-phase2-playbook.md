# Manual de estrategias de la fase 2 de estilo: autoevaluación de la calidad del contrato de estilo JSON

## Objetivo

Inmediatamente después de generar `style.json` en la Fase 1, cambie a la perspectiva del inspector de calidad de estilo (QA). Lleve a cabo una estricta legalidad, lógica y conciliación estructural en la extensa configuración JSON que acabamos de describir.

---

## Proceso de acción de autoauditoría

1. **Verifique directamente el archivo original**: verifique `style.json` elemento por elemento. Si se encuentra algún elemento no calificado, use directamente la herramienta para reescribir el valor de retorno JSON en su lugar sin crear un archivo nuevo.
2. **Múltiples rondas de revisión**: una vez completada la modificación, lea nuevamente la lista de 7 elementos, lo que permitirá hasta 2 rondas de ciclos de autorreparación.

---

## Límite de legalidad (la lista de verificación de 7 elementos)

Antes de enviar la señal FINALIZAR final, debes verificar los siguientes 7 criterios uno por uno en tu mente o en tu registro de deducciones:

| # | Puntos clave para la verificación | Límites de tolerancia a fallos y métodos de procesamiento |
|---|--------|------------------|
| 1 | Altura de `design_soul` | No se puede escribir como: un gran cuadrado azul degradado con esquinas redondeadas. Debe ser: un estilo empresarial moderno y plano que encarne la racionalidad de las empresas de tecnología y restrinja el uso del color. Describe el **alma e intención del diseño** de este conjunto de PPT. Si no está en su lugar, reescríbalo. |
| 2 | Dimensiones de `variation_strategy` | no puede ser un conjunto de scripts de ejecución página por página. Debe indicar claramente: "Qué elementos básicos deben integrarse completamente (como el color base de la marca, esquinas redondeadas)" y "Qué partes permiten flexibilidad a nivel de página (como la combinación escalonada de colores de fondo de la tarjeta)". Si falta algún poste, se volverá a la reconstrucción. |
| 3 | Validez de `decoration_dna.forbidden` | Lo que está escrito aquí debe en realidad evitar la deriva de estilo. Por ejemplo: "Está prohibido utilizar colores contrastantes de alta intensidad de rojo y verde", "Está prohibido establecer los parámetros de sombra de la tarjeta demasiado grandes como para causar suciedad". Si es sólo una declaración vacía (los graffitis antiestéticos están prohibidos), debe reescribirse. |
| 4 | La sintaxis de `combos_recomendados` | ¿Es este un conjunto de "sintaxis combinada" o un comando seco? Su contenido debería ser como una receta: "Cuando una página es muy larga, se recomienda utilizar un color de fondo `elevado` con un subtítulo `texto primario`" en lugar de "Debes poner en negrita el subtítulo en la primera página". Si se escribe como una instrucción de una sola página, debe resumirse en reglas generales. |
| 5 | La piedra angular de `css_variables` es estable | Los 12 nombres de variables básicos obligatorios deben verificarse palabra por palabra (use minúsculas y subrayados, sin `--`, como `bg_primary`). Si se pierde alguno, se bloqueará. Si falta algo, escríbalo inmediatamente para compensarlo. |
| 6 | Formato y anclaje `css_snippets` | Primero verifique el formato: debe ser un **Objeto (Objeto/Dict)** y no debe ser una matriz (Array). Si se descubre que es una matriz, se debe reescribir inmediatamente como un par clave-valor. En segundo lugar, verifique el contenido: solo puede contener **estructuras locales** (como el grupo de parámetros de sombra `box-shadow`), en lugar de definir un diseño de ancho y alto de contenedor que pueda cambiar el flujo de toda la página. Esta anulación puede provocar una avería completa del HTML en sentido descendente. Elimine el fragmento directamente una vez encontrado. |
| 7 | Línea roja de longitud de matriz (clave fatal) | Cuente estrictamente las longitudes de tres matrices: `mood_keywords` **debe ser 3-5**; `decoration_dna.forbidden` **debe ser 2-5**; `recommended_combos` **debe ser 2-4**. ¡Uno menos y uno más activará el script para informar un error grave y bloquear directamente el proceso! Si encuentra algún incumplimiento, agréguelo o elimínelo inmediatamente. |

---

## FINALIZAR Contrato de Firma

只有在 7 项检查全部自审并修补通过后，你才可以发出信号终结该流程：

```
FINALIZE: Auto-auditoría completada
- style: [STYLE_OUTPUT 路径]
- Rondas de auditoría: N
- 修复发现: [列举你按照要求修复了什么不规范字段，若无填 无]
```
