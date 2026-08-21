# Manual de estrategias de la fase 1 de estilo: definición y resultado del contrato de estilo

## Objetivo

Según las necesidades del usuario, la estructura del esquema y las reglas de estilo de tiempo de ejecución, genere un contrato de estilo global `style.json` que pueda consumirse de manera estable mediante planificación/html en lugar de cualquier código HTML de una sola página.

---

## Proceso de ejecución de etapas

### Fase 1: Refinar las restricciones de estilo

1. Lea `requisitos-entrevista.txt`
2. Extraer señales de alta prioridad: color de marca, áreas restringidas de marca, audiencia, formalidad, lenguaje y estrategia de ilustración. Nunca está permitido seleccionar sin saberlo la audiencia equivocada (como darle a la tecnología una apariencia linda a la audiencia).
3. Lea el esquema `outline.txt`
4. Determine el tipo de ritmo de todo el mazo: avance en estado estable/ondulación/sprint estilo conferencia de prensa/estilo de entrenamiento expansión uniforme para determinar el tono de su estrategia de cambio.

### Fase 2: crear una paleta de estilos central (rechazar las tablas de búsqueda mecánica)

¡No sea un “rellenador de formularios” mecánico! **¡Las necesidades del usuario (estilo, audiencia, escena) tienen absoluta prioridad! **

**Determina tu orientación de estilo principal:**
1. **Refinamiento en profundidad de los requisitos de la entrevista del usuario**: Priorice la lectura del "estilo", la "marca" y la "audiencia" normalizados en "requirements-interview.txt"; Si el archivo conserva el campo canónico, el significado de `visual_style`, `brand_constraints` y `core_audience` también deben estar alineados al mismo tiempo.
2. **Paleta de colores dinámica avanzada**: deshazte de los colores rígidos y anticuados. Utilice su estética avanzada para crear un conjunto de 12 `css_variables` clave (color de fondo principal, degradado de tarjeta, 4 colores de acento) que sean lógicamente autoconsistentes.
3. **Sólo consulte el archivo preestablecido cuando esté extremadamente confundido**.
Si el usuario solicita "este misterioso", "páramo apocalíptico" o "sentido geek comunitario",** puedes personalizar la combinación de colores para ellos. Sin embargo, cualquier combinación de colores original debe cumplir con los principios fundamentales de seguridad visual en la web. El color de fondo debe ser de baja frecuencia o silencioso, y el texto nunca debe perder un fuerte contraste para facilitar la lectura. ¡Está estrictamente prohibido combinar colores que provoquen ceguera para perseguir la "singularidad"! **

Incluso si las necesidades del usuario son raras, como "Mysterious East", "Memphis Geometry", "Doomsday Wasteland" o "Technical Community Sense", ¡su sentido de alto nivel debe encapsularse en una estricta matriz de variables del sistema! **. Nunca utilices el nombre de "creatividad" para combinar la combinación de colores que viola las reglas de la estética. La brújula de demanda `style`/`visual_style` del usuario tiene la primera posición, y su producción debe cumplir con la disciplina Token y las líneas rojas estéticas visuales de los principales fabricantes.

### Fase 3: Generar contrato style.json

Debe generar un documento de contrato JSON que cumpla estrictamente con los siguientes requisitos de campo:

*   `style_id` / `style_name`
*   `mood_keywords`：**（强制：必须提供 3-5 个关键词的数组）**
*   `design_soul`：描述整套 deck 的设计目标，**绝对不可以**写成某一页的成品描述或构图指导。
*   `variation_strategy`：必须同时说明“哪些元素允许变”和“哪些元素锁死不动”。不能写成逐页执行指令。
*   `decoration_dna.signature_move`：必须有，且为非空字符串。
*   `decoration_dna.forbidden`：**（强制：必须提供 2-5 个元素的数组）**
*   `decoration_dna.recommended_combos`：**（强制：必须提供 2-4 个元素的数组）**
*   `font_family`

#### css_variables especificaciones de cantidad y denominación de claves (línea roja obligatoria)

这 12 个变量Sí基石，必须定义并且键名**不能更改一个字母**：

```json
{
  "bg_primary": "#...",
  "bg_secondary": "#...",
  "card_bg_from": "#...",
  "card_bg_to": "#...",
  "card_border": "#...",
  "card_radius": "...px",
  "text_primary": "#...",
  "text_secondary": "#...",
  "accent_1": "#...",
  "accent_2": "#...",
  "accent_3": "#...",
  "accent_4": "#...",
  "css_snippets": {
    "example_class": "font-weight: 700;"
  }
}
```

- key 必须使用下划线（无 `--` 前缀），对应校验合同要求。
- 必须严格保留这 12 个基础变量名，禁止改名。如需自定义增加可以增加，但这 12 个不可少。
- `css_snippets` 必须Sí对象 (Object)，格式为 `"键名": "值"`，**绝对不能Sí数组 (Array)！** 确有必要时可用它固化跨页重复的局部样式结构（如阴影），但绝对不能包含能驱动整页骨架布局的 CSS。
