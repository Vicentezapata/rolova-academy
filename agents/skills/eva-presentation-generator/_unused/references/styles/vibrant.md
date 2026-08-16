# Categoría Dinámico y Vibrante (4 Estilos)

> Posicionamiento de la categoría: Alta saturación + Brillante + Amigable/Creativo/Marketing/Sensación Infantil. Stripe / Libro ilustrado infantil / Bauhaus / Tienda de dulces.

---

## Índice

| # | style_id | Inspiración | En una frase |
|---|----------|------|-------|
| 1 | `vibrant_rainbow` | Stripe Sessions | Degradado multicapa + Reflejo de bola de cristal (Mejorado) |
| 2 | `kindergarten_pop` | Fuente redondeada Quicksand | Fondo amarillo crema + Blob amigable + emoji |
| 3 | `bauhaus_block` | Bauhaus / Swiss | Collage geométrico de tres colores primarios + Helvetica |
| 4 | `candy_pastel` | Tienda de dulces Ladurée | Puntos de macaron + Playfair italic |

---

## 1. vibrant_rainbow (Mejorado - Nivel Stripe)

```json
{
  "style_id": "vibrant_rainbow",
  "style_name": "Arcoíris Vibrante (Stripe-grade Gradient)",
  "category": "vibrant",
  "inspiration": "Stripe Sessions / Stripe.com",
  "mood_keywords": ["Degradado multicapa", "Reflejo de bola de cristal", "Alta saturación premium", "Escenario de conferencia"],
  "design_soul": "En el escenario de la conferencia Stripe Sessions, el degradado de color de múltiples capas fluye como una aurora, las bolas de cristal reflejan las luces del escenario y cada dato domina orgullosamente el campo de visión.",
  "variation_strategy": "La portada usa gran degradado + múltiples bolas de cristal, la página de productos usa un solo color de alta saturación + 1 tarjeta de cristal, la página de datos usa fondo blanco de alto contraste + color de acento.",
  "decoration_dna": {
    "signature_move": "Fondo degradado linear-gradient multicapa (rosa/púrpura/azul/cian) + Bola de cristal (radial-gradient multicapa + sombra interior + halo borroso) + Botón de píldora redondeado + Palabras clave en serif italic",
    "forbidden": ["Fondo de color sólido", "Tono oscuro", "Sensación de revista serif", "Colores pastel de macaron (para diferenciar de candy_pastel)"],
    "recommended_combos": ["Degradado multicapa + Gran bola de cristal + Botón redondeado", "CTA píldora blanca + Botón fantasma (ghost) + Datos tabular-nums"]
  },
  "background": { "primary": "linear-gradient(135deg, #ff5b9d 0%, #b266ff 30%, #4a8cff 60%, #00d8d4 100%)", "gradient_to": "#00d8d4", "texture": { "type": "glass_orbs" } },
  "card": { "gradient_from": "rgba(255,255,255,0.18)", "gradient_to": "rgba(255,255,255,0.08)", "border": "rgba(255,255,255,0.4)", "border_radius": 100, "backdrop_blur": 20 },
  "text": { "primary": "#FFFFFF", "secondary": "rgba(255,255,255,0.85)", "title_size": 116, "body_size": 14, "card_title_size": 18 },
  "accent": { "primary": ["#ffd16b", "#ffffff"], "secondary": ["#ff5b9d", "#00d8d4"] },
  "typography": {
    "display_font": "'Inter Tight', 'Inter', -apple-system, sans-serif",
    "body_font": "'Inter', -apple-system, sans-serif",
    "serif_italic_font": "'Instrument Serif', 'Fraunces', Georgia, serif",
    "mono_font": "'JetBrains Mono', monospace",
    "display_letter_spacing": "-0.045em",
    "headline_letter_spacing": "-0.025em",
    "body_letter_spacing": "-0.005em",
    "label_letter_spacing": "0.22em",
    "feature_settings": "'ss01', 'cv11', 'calt', 'kern', 'liga', 'ccmp'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line", "title_serif_italic": true, "corner_lines": false, "vertical_divider": false, "drop_cap": false, "masthead": false, "glass_orbs": true, "pill_buttons": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800&family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/vibrant_rainbow.html`](../../ppt-output/style-gallery/vibrant_rainbow.html)

---

## 2. kindergarten_pop (Nuevo - Educación Infantil)

```json
{
  "style_id": "kindergarten_pop",
  "style_name": "Ilustración Infantil (Kindergarten Pop)",
  "category": "vibrant",
  "inspiration": "Libros ilustrados infantiles de alta calidad / Sensación amigable de Notion / Apple Kids",
  "mood_keywords": ["Luz de sol suave", "Quicksand redondeado", "Blob de color", "Emoji amigable"],
  "design_soul": "En la habitación de los niños iluminada por la luz de la mañana, la luz del sol color crema cubre la mesa, las letras redondeadas se alinean suavemente y varios globos de colores flotan en la esquina.",
  "variation_strategy": "La portada usa tarjeta con esquinas muy redondeadas + decoración emoji + título amigable, la página de actividad usa 3 tarjetas de colores con esquinas muy redondeadas, la página de resultados usa la insignia de celebración ✓⭐.",
  "decoration_dna": {
    "signature_move": "Fondo degradado amarillo crema + Blob de color circular (rosa/azul/verde/amarillo) + Fuente redondeada Quicksand + Esquinas muy redondeadas (≥ 16px) + Adornos emoji ✓⭐❤️",
    "forbidden": ["Fondo oscuro", "Geometría rígida", "Efecto neón", "Fuente serif", "Diseño abarrotado"],
    "recommended_combos": ["Fondo amarillo crema + blob de 4 colores + Tarjeta de esquina redondeada", "emoji + Quicksand redondeado + Números tabular-nums"]
  },
  "background": { "primary": "#fff8e7", "gradient_to": "#ffeed4", "texture": { "type": "none" } },
  "card": { "gradient_from": "#ffffff", "gradient_to": "#fff8e7", "border": "rgba(255,127,193,0.2)", "border_radius": 28, "backdrop_blur": 0 },
  "text": { "primary": "#2a2a3a", "secondary": "#5a5a6a", "title_size": 36, "body_size": 14, "card_title_size": 18 },
  "accent": { "primary": ["#ff7eb9", "#ffd166"], "secondary": ["#06d6a0", "#87ceeb"] },
  "typography": {
    "display_font": "'Quicksand', 'Nunito', -apple-system, sans-serif",
    "body_font": "'Quicksand', 'Nunito', -apple-system, sans-serif",
    "serif_italic_font": "'Instrument Serif', Georgia, serif",
    "mono_font": "'JetBrains Mono', monospace",
    "display_letter_spacing": "-0.015em",
    "headline_letter_spacing": "-0.01em",
    "body_letter_spacing": "0",
    "label_letter_spacing": "0.18em",
    "feature_settings": "'kern', 'liga', 'calt', 'ss01'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line", "title_serif_italic": false, "corner_lines": false, "vertical_divider": false, "drop_cap": false, "masthead": false, "color_blobs": true, "rounded_corners": true, "emoji_decorations": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Quicksand:wght@400;500;600;700&family=Nunito:wght@400;500;600;700&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/kindergarten_pop.html`](../../ppt-output/style-gallery/kindergarten_pop.html)

---

## 3. bauhaus_block (Nuevo - Collage Geométrico)

```json
{
  "style_id": "bauhaus_block",
  "style_name": "Bloque Bauhaus (Bauhaus Block)",
  "category": "vibrant",
  "inspiration": "Bauhaus / Swiss Design / Massimo Vignelli / IBM Eames",
  "mood_keywords": ["Tres colores primarios", "Collage geométrico", "Helvetica 800", "Contención extrema"],
  "design_soul": "En el edificio Bauhaus en Dessau en la década de 1920, las formas geométricas de los tres colores primarios estaban dispuestas en un orden de cuadrícula estricto, y cada círculo y cuadrado era tan preciso como un teorema matemático.",
  "variation_strategy": "La portada usa fuente grande Helvetica + geometría de tres colores primarios, la página de principios usa 3 tarjetas cuadradas, la página de trabajos usa patrón de cuadrícula para visualización.",
  "decoration_dna": {
    "signature_move": "Formas geométricas (círculo/cuadrado/triángulo) de los tres colores primarios (rojo #d62828 / azul #003049 / amarillo #ffd60a) + Grosor de fuente Helvetica Now 800 + Cuadrícula estricta + Espacio en blanco minimalista",
    "forbidden": ["Fondo oscuro", "Texto degradado", "Efecto neón", "Radio de esquina superior a 4px", "Decoración de curvas"],
    "recommended_combos": ["Fondo crema + Círculo rojo + Cuadrado azul + Triángulo amarillo", "Letra gigante Helvetica + Cuadrícula estricta + Tres colores primarios"]
  },
  "background": { "primary": "#f4f0e8", "gradient_to": "#f4f0e8", "texture": { "type": "none" } },
  "card": { "gradient_from": "#ffffff", "gradient_to": "#f4f0e8", "border": "#1a1a1a", "border_radius": 0, "backdrop_blur": 0 },
  "text": { "primary": "#1a1a1a", "secondary": "#666", "title_size": 92, "body_size": 14, "card_title_size": 18 },
  "accent": { "primary": ["#d62828", "#003049"], "secondary": ["#ffd60a", "#1a1a1a"] },
  "typography": {
    "display_font": "'Helvetica Neue', 'Inter Tight', 'Inter', sans-serif",
    "body_font": "'Inter', -apple-system, sans-serif",
    "serif_italic_font": "'Instrument Serif', Georgia, serif",
    "mono_font": "'JetBrains Mono', monospace",
    "display_letter_spacing": "-0.035em",
    "headline_letter_spacing": "-0.025em",
    "body_letter_spacing": "-0.005em",
    "label_letter_spacing": "0.32em",
    "feature_settings": "'kern', 'liga', 'calt', 'ss01', 'cv11'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line", "title_serif_italic": false, "corner_lines": false, "vertical_divider": true, "drop_cap": false, "masthead": false, "geometric_shapes": true, "primary_colors_only": true, "strict_grid": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;700;800;900&family=Inter:wght@400;500;600;700&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/bauhaus_block.html`](../../ppt-output/style-gallery/bauhaus_block.html)

---

## 4. candy_pastel (Nuevo - Postres/Repostería)

```json
{
  "style_id": "candy_pastel",
  "style_name": "Caramelo Macaron (Candy Pastel)",
  "category": "vibrant",
  "inspiration": "Ladurée / Pierre Hermé / Glossier",
  "mood_keywords": ["Puntos de macaron", "Rosa pastel y suave", "Playfair italic", "Tienda de postres"],
  "design_soul": "En el escaparate de Ladurée en París, los macarons rosas pastel están cuidadosamente colocados, y cada uno es tan exquisito y elegante como las letras de Playfair.",
  "variation_strategy": "La portada usa el título principal Playfair italic + puntos de macaron de 5 colores, la página del producto usa tarjetas de productos con esquinas muy redondeadas + precios tabulares, y la página de resultados usa insignias rosas + sensación de empaque.",
  "decoration_dna": {
    "signature_move": "Fondo degradado rosa pastel y beige + Puntos color macaron (rosa/verde/amarillo/azul/púrpura) + Título principal Playfair italic + Esquinas muy redondeadas (≥ 24px) + Posición de imagen de producto circular",
    "forbidden": ["Fondo oscuro", "Efecto neón", "Geometría rígida", "Alta saturación", "Diseño abarrotado"],
    "recommended_combos": ["Degradado beige + Puntos macaron de 5 colores + Playfair italic", "Producto circular + Precio ¥XX tabular + Tarjeta de esquina muy redondeada"]
  },
  "background": { "primary": "#fff5f0", "gradient_to": "#fff0e8", "texture": { "type": "none" } },
  "card": { "gradient_from": "#ffffff", "gradient_to": "#fff5f0", "border": "rgba(248,187,208,0.3)", "border_radius": 24, "backdrop_blur": 0 },
  "text": { "primary": "#4a2c2a", "secondary": "#7a4c4a", "title_size": 78, "body_size": 14, "card_title_size": 18 },
  "accent": { "primary": ["#f8bbd0", "#c8e6c9"], "secondary": ["#fff59d", "#b3e5fc"] },
  "typography": {
    "display_font": "'Playfair Display', 'Fraunces', Georgia, serif",
    "body_font": "'Inter', -apple-system, sans-serif",
    "serif_italic_font": "'Playfair Display', 'Fraunces', Georgia, serif",
    "mono_font": "'JetBrains Mono', monospace",
    "display_letter_spacing": "-0.025em",
    "headline_letter_spacing": "-0.015em",
    "body_letter_spacing": "-0.005em",
    "label_letter_spacing": "0.4em",
    "feature_settings": "'kern', 'liga', 'ss01', 'cv11', 'calt', 'dlig'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line", "title_serif_italic": true, "corner_lines": false, "vertical_divider": false, "drop_cap": false, "masthead": false, "macaron_dots": true, "rounded_24": true, "circular_product": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Fraunces:ital,wght@0,400;1,400&family=Inter:wght@400;500;600&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/candy_pastel.html`](../../ppt-output/style-gallery/candy_pastel.html)
