# Categoría Cultura Oriental (3 Estilos)

> Posicionamiento de la categoría: Estética oriental + Fuente Serif/Kaiti + Rojo Bermellón/Color Tinta/Oro + Contención en espacios en blanco. Palacio chino / Wabi-sabi japonés / Nueva tendencia nacional china.

---

## Índice

| # | style_id | Inspiración | En una frase |
|---|----------|------|-------|
| 1 | `royal_red` | Ceremonia de apertura de los Juegos Olímpicos de Invierno de Beijing | Muro de palacio rojo bermellón + Decoración de esquina dorada + Sello (Mejorado) |
| 2 | `sakura_wabi` | Wabi-sabi japonés | Beige de papel Washi + Texto vertical + Un punto de rosa flor de cerezo |
| 3 | `ink_jade` | Nueva tendencia nacional china | Beige claro de papel Washi + Texto vertical en tinta + Un trazo rojo bermellón |

---

## 1. royal_red (Mejorado - Nivel Juegos Olímpicos de Invierno de Beijing)

```json
{
  "style_id": "royal_red",
  "style_name": "Muro de Palacio Rojo Bermellón (Royal Red, Beijing 2022-grade)",
  "category": "cultural_oriental",
  "inspiration": "Ceremonia de apertura de Beijing 2022 / Productos culturales de la Ciudad Prohibida / Museo Nacional",
  "mood_keywords": ["Muro rojo bermellón", "Decoración de esquina dorada", "Serif centrado", "Etiqueta de sello"],
  "design_soul": "El muro de palacio lacado en rojo de la Ciudad Prohibida brilla con luz dorada al atardecer, 4 hilos dorados en forma de L son tan precisos como celosías de ventanas, y los caracteres grandes de la fuente Songti en el centro son como un sello cuadrado presionado en el centro del pergamino.",
  "variation_strategy": "La portada usa serif centrado + hilo dorado de 4 esquinas + sello rojo, la portada del capítulo usa gran espacio en blanco + hilo dorado que se desvanece, la página de contenido usa columnas dobles simétricas a izquierda y derecha + división de hilo dorado.",
  "decoration_dna": {
    "signature_move": "Fondo radial rojo bermellón oscuro + 4 decoraciones de esquina en forma de L con hilo dorado + Noto Serif SC centrado (espaciado de letra de 0.18em) + Sello rojo + Hilo dorado que se desvanece (60px vertical)",
    "forbidden": ["Título principal sans", "Texto con degradado", "Efecto neón", "Esquinas demasiado redondeadas", "Fondo claro", "Colores pastel de macaron"],
    "recommended_combos": ["Hilo dorado en las 4 esquinas + Serif centrado + Sello rojo", "Hilo dorado que se desvanece + Etiqueta maison con gran espaciado + Simetría central"]
  },
  "background": { "primary": "#6b0a0a", "gradient_to": "#2d0303", "gradient_direction": "radial 80% 60% at 50% 30%", "texture": { "type": "subtle_grain", "opacity": 0.02 } },
  "card": { "gradient_from": "rgba(201,169,96,0.05)", "gradient_to": "transparent", "border": "rgba(201,169,96,0.3)", "border_radius": 0, "backdrop_blur": 0 },
  "text": { "primary": "#fff8e7", "secondary": "rgba(255,248,231,0.7)", "title_size": 96, "body_size": 14, "card_title_size": 16 },
  "accent": { "primary": ["#c9a960", "#FFD700"], "secondary": ["#c0392b", "#fff8e7"] },
  "typography": {
    "display_font": "'Noto Serif SC', 'Source Han Serif SC', 'STSong', SimSun, serif",
    "body_font": "'Inter', -apple-system, sans-serif",
    "serif_italic_font": "'Noto Serif SC', 'STSong', serif",
    "mono_font": "'JetBrains Mono', monospace",
    "display_letter_spacing": "0.18em",
    "headline_letter_spacing": "0.12em",
    "body_letter_spacing": "0.05em",
    "label_letter_spacing": "0.8em",
    "feature_settings": "'kern', 'liga', 'palt', 'ss01', 'calt'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line", "title_serif_italic": false, "corner_lines": true, "vertical_divider": false, "drop_cap": false, "masthead": false, "centered_symmetric": true, "gold_l_corners": true, "vertical_gold_gradient_line": true, "vermilion_seal": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/royal_red.html`](../../ppt-output/style-gallery/royal_red.html)

---

## 2. sakura_wabi (Nuevo - Wabi-sabi Japonés)

```json
{
  "style_id": "sakura_wabi",
  "style_name": "Cerezo Wabi-sabi (Sakura Wabi)",
  "category": "cultural_oriental",
  "inspiration": "Wabi-sabi japonés / Museo de la Cultura de Kioto / Jun'ichiro Tanizaki 'El elogio de la sombra'",
  "mood_keywords": ["Beige papel Washi", "Tinta vertical", "Un punto rosa cerezo", "Espacio en blanco extremo"],
  "design_soul": "En el salón de té de Kioto, la puerta corrediza de papel washi está medio abierta, un rayo de luz matutina ilumina los caracteres de tinta escritos verticalmente, el único toque de rosa flor de cerezo se detiene en silencio en una esquina de la imagen.",
  "variation_strategy": "La portada usa título vertical + decoración de un punto rosa + 70% de espacio en blanco, la página de contenido usa subtítulo horizontal + oraciones cortas, la página de resultados usa sello + cita.",
  "decoration_dna": {
    "signature_move": "Fondo beige de papel Washi + Título vertical en japonés/chino (writing-mode: vertical-rl) + Punto rosa flor de cerezo único (radial-gradient) + Línea única minimalista + Más del 70% de espacio en blanco",
    "forbidden": ["Colores saturados", "Fondo oscuro", "Diseño abarrotado", "Geometría rígida", "Efectos neón", "Título principal sans"],
    "recommended_combos": ["Serif vertical + Un punto rosa + Gran espacio en blanco", "Subtítulo horizontal + Línea única minimalista + Marco de sello rojo"]
  },
  "background": { "primary": "#f5f0e8", "gradient_to": "#f5f0e8", "texture": { "type": "washi_grain", "opacity": 0.04 } },
  "card": { "gradient_from": "transparent", "gradient_to": "transparent", "border": "rgba(201,184,150,0.3)", "border_radius": 0, "backdrop_blur": 0 },
  "text": { "primary": "#2c2826", "secondary": "#5a4f44", "title_size": 64, "body_size": 13, "card_title_size": 16 },
  "accent": { "primary": ["#ffb7c5", "#d97a87"], "secondary": ["#c9b896", "#8b7d6b"] },
  "typography": {
    "display_font": "'Source Han Serif SC', 'Noto Serif JP', 'Hiragino Mincho ProN', 'Songti SC', serif",
    "body_font": "'Source Han Serif SC', 'Noto Serif JP', serif",
    "serif_italic_font": "'Source Han Serif SC', serif",
    "mono_font": "'JetBrains Mono', monospace",
    "display_letter_spacing": "0.32em",
    "headline_letter_spacing": "0.18em",
    "body_letter_spacing": "0.05em",
    "label_letter_spacing": "0.55em",
    "feature_settings": "'kern', 'liga', 'palt'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line", "title_serif_italic": false, "corner_lines": false, "vertical_divider": true, "drop_cap": false, "masthead": false, "vertical_writing": true, "single_pink_dot": true, "extreme_whitespace": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Noto+Serif+JP:wght@400;500;600&family=Noto+Serif+SC:wght@400;500;600&family=Inter:wght@400;500&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/sakura_wabi.html`](../../ppt-output/style-gallery/sakura_wabi.html)

---

## 3. ink_jade (Nuevo - Nueva tendencia nacional china)

```json
{
  "style_id": "ink_jade",
  "style_name": "Rima de Tinta Nuevo Estilo Chino (Ink Jade)",
  "category": "cultural_oriental",
  "inspiration": "Sexy Tea / Heytea PRO / Línea joven de productos culturales de la Ciudad Prohibida / Tienda de vida sencilla",
  "mood_keywords": ["Papel Washi beige claro", "Tinta vertical", "Un trazo bermellón", "Nueva tendencia nacional"],
  "design_soul": "En el menú de la nueva tienda de té, sobre el fondo de papel de arroz beige claro, hay una marca de tinta bermellón al lado del título vertical de tinta, joven y elegante.",
  "variation_strategy": "La portada usa título vertical de tinta + un trazo bermellón + sello, la página del menú usa cita horizontal + precio, la página de la historia usa oraciones cortas + espacio en blanco.",
  "decoration_dna": {
    "signature_move": "Fondo beige claro papel Washi + Título vertical de tinta + Manchado de tinta de pincel bermellón (div + linear-gradient + desenfoque de punto) + Sello rojo + Gran cantidad de espacio en blanco",
    "forbidden": ["Colores saturados (excepto el rojo bermellón)", "Fondo oscuro", "Efecto neón", "Esquinas redondeadas grandes", "Geometría rígida"],
    "recommended_combos": ["Fondo beige claro + Tinta vertical + Sello rojo + Un trazo bermellón", "Subtítulo horizontal + Etiqueta oro claro + Espacio en blanco"]
  },
  "background": { "primary": "#f5f1e8", "gradient_to": "#f5f1e8", "texture": { "type": "rice_paper_grain", "opacity": 0.04 } },
  "card": { "gradient_from": "transparent", "gradient_to": "transparent", "border": "rgba(192,57,43,0.2)", "border_radius": 2, "backdrop_blur": 0 },
  "text": { "primary": "#1a1a1a", "secondary": "#5a4f44", "title_size": 84, "body_size": 14, "card_title_size": 18 },
  "accent": { "primary": ["#c0392b", "#1a1a1a"], "secondary": ["#c9b896", "#8b7d6b"] },
  "typography": {
    "display_font": "'Source Han Serif SC', 'Noto Serif SC', 'STKaiti', 'STSong', serif",
    "body_font": "'Source Han Serif SC', 'Noto Serif SC', serif",
    "serif_italic_font": "'Source Han Serif SC', serif",
    "mono_font": "'JetBrains Mono', monospace",
    "display_letter_spacing": "0.32em",
    "headline_letter_spacing": "0.18em",
    "body_letter_spacing": "0.05em",
    "label_letter_spacing": "0.4em",
    "feature_settings": "'kern', 'liga', 'palt', 'ss01', 'calt', 'ccmp'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line_short", "title_serif_italic": false, "corner_lines": false, "vertical_divider": false, "drop_cap": false, "masthead": false, "vertical_writing": true, "vermilion_brush_stroke": true, "vermilion_seal": true, "ink_bleed_subtle": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;600;700&family=Inter:wght@400;500&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/ink_jade.html`](../../ppt-output/style-gallery/ink_jade.html)
