# Categoría Premium Claro (8 Estilos)

> Posicionamiento de la categoría: Fondo claro + Sensación premium + Académico/Profesional/Suave/Médico/Industrial. Estilos tipo Apple / Anthropic / NYT / Mayo Clinic / Suisse.
>
> Compartido: [Reglas de tipografía](../typography.md) · [Modos de fallo](../principles/failure-modes.md) · [Bento Grid](../bento-grid.md)

---

## Índice

| # | style_id | Inspiración | En una frase |
|---|----------|------|-------|
| 1 | `blue_white` | Páginas empresariales de Apple | Blanco minimalista + Gris cedro + Un toque de azul (Versión mejorada) |
| 2 | `fresh_green` | Aesop / Le Labo | Beige suave + Verde hierba ocre + serif italic (Versión mejorada) |
| 3 | `minimal_gray` | NYT Magazine | Fondo de papel de arroz + serif Display + División en tres columnas (Versión mejorada) |
| 4 | `mocha_editorial` | Anthropic / Pantone 2025 | Beige Mocha + Source Serif italic + Línea de énfasis rojo ladrillo |
| 5 | `medical_pulse` | Mayo Clinic | Blanco puro + Azul médico + Onda ECG + Cruz roja |
| 6 | `earth_concrete` | Suisse Int'l | Gris cemento + Cinta naranja cálido + Sensación de orden de cuadrícula |
| 7 | `champagne_gold` | Invitación de boda de alta gama | Degradado beige + Dorado Playfair italic + Decoración de doble línea |
| 8 | `liquid_glass` | iOS 26 / visionOS | Degradado de color + Blob borroso + Múltiples capas de cristal líquido |

---

## 1. blue_white — Azul Blanco Negocios (Versión mejorada)

```json
{
  "style_id": "blue_white",
  "style_name": "Azul Blanco Negocios (Blue White, Apple-grade)",
  "category": "light_premium",
  "inspiration": "Páginas empresariales de Apple / Documentación para desarrolladores de Apple",
  "mood_keywords": ["Blanco minimalista", "Gris cedro", "Confiabilidad Apple", "Líneas de marco interior"],
  "design_soul": "Sobre un papel blanco puro, el azul claro es como un tenue rayo de confianza, todo el texto es cuidadoso y sobrio, como un acuerdo firmado.",
  "variation_strategy": "La portada usa gran espacio en blanco + línea azul fina, la página del capítulo usa bloque azul claro + serif italic, la página de datos usa 4 tarjetas minimalistas + tabular-nums.",
  "decoration_dna": {
    "signature_move": "Blanco minimalista nivel Apple + Línea fina de marco interior + Etiqueta azul de punto de pulso + Mezcla de palabras clave en serif italic + Gran cantidad de espacio en blanco",
    "forbidden": ["Rojo anaranjado saturado", "Fondo oscuro", "Texto degradado", "Efecto neón", "Elementos de dibujos animados", "Diseño abarrotado"],
    "recommended_combos": ["Línea de marco interior + Etiqueta azul + Gran espacio en blanco", "Tarjeta de datos de tres columnas + Separación por línea horizontal + tabular-nums"]
  },
  "background": { "primary": "#ffffff", "gradient_to": "#f6f8fb", "texture": { "type": "none" } },
  "card": { "gradient_from": "#ffffff", "gradient_to": "#f6f8fb", "border": "rgba(10,29,58,0.06)", "border_radius": 12, "backdrop_blur": 0 },
  "text": { "primary": "#0a1d3a", "secondary": "#64748b", "title_size": 78, "body_size": 14, "card_title_size": 18 },
  "accent": { "primary": ["#2563EB", "#1D4ED8"], "secondary": ["#059669", "#047857"] },
  "typography": {
    "display_font": "-apple-system, 'SF Pro Display', 'Inter Tight', 'Inter', BlinkMacSystemFont, sans-serif",
    "body_font": "-apple-system, 'SF Pro Text', 'Inter', sans-serif",
    "serif_italic_font": "'Instrument Serif', 'Fraunces', Georgia, serif",
    "mono_font": "'SF Mono', 'JetBrains Mono', monospace",
    "display_letter_spacing": "-0.042em",
    "headline_letter_spacing": "-0.02em",
    "body_letter_spacing": "-0.005em",
    "label_letter_spacing": "0.22em",
    "feature_settings": "'kern', 'liga', 'calt', 'ss01', 'cv11', 'ccmp'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "dot_pulse", "title_serif_italic": true, "corner_lines": true, "vertical_divider": false, "drop_cap": false, "masthead": false, "inner_frame": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800&family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/blue_white.html`](../../ppt-output/style-gallery/blue_white.html)

---

## 2. fresh_green — Verde Fresco Natural (Rehecho nivel Aesop)

```json
{
  "style_id": "fresh_green",
  "style_name": "Verde Fresco Natural (Fresh Green, Aesop-grade)",
  "category": "light_premium",
  "inspiration": "Aesop / Le Labo / Marcas premium de cuidado de la piel",
  "mood_keywords": ["Beige suave", "Verde hierba ocre", "Hierbas naturales", "serif italic"],
  "design_soul": "En el taller bañado por la luz de la mañana, frascos verde hierba y semillas de color ocre descansan sobre un mantel de lino beige, el título en serif italic es tan suave como si estuviera escrito a mano.",
  "variation_strategy": "La portada usa el título principal serif italic + tarjeta beige + una hoja real SVG, la página de productos usa 3 tarjetas de colores cálidos, la página del capítulo usa gran espacio en blanco + línea horizontal verde hierba.",
  "decoration_dna": {
    "signature_move": "Título Source Serif 4 italic + Fondo cálido beige + Doble acento verde hierba ocre + Hoja real SVG (sin emojis) + Mucho espacio en blanco",
    "forbidden": ["Verde brillante saturado (verde bebé)", "Fondo oscuro", "Efecto neón", "Geometría rígida", "Diseño abarrotado"],
    "recommended_combos": ["Título principal serif italic + Línea horizontal verde hierba + Tarjeta beige", "Imagen de producto circular + Etiqueta de precio ocre + tabular-nums"]
  },
  "background": { "primary": "#f4ede0", "gradient_to": "#e8dec5", "texture": { "type": "none" } },
  "card": { "gradient_from": "#fffaf0", "gradient_to": "#f4ede0", "border": "rgba(133,158,90,0.18)", "border_radius": 14, "backdrop_blur": 0 },
  "text": { "primary": "#2d3a1f", "secondary": "#5a6840", "title_size": 64, "body_size": 14, "card_title_size": 18 },
  "accent": { "primary": ["#859e5a", "#6b8344"], "secondary": ["#a85b3a", "#8b4513"] },
  "typography": {
    "display_font": "'Source Serif 4', 'Fraunces', 'Iowan Old Style', Georgia, serif",
    "body_font": "'Inter', -apple-system, sans-serif",
    "serif_italic_font": "'Source Serif 4', 'Fraunces', Georgia, serif",
    "mono_font": "'JetBrains Mono', monospace",
    "display_letter_spacing": "-0.018em",
    "headline_letter_spacing": "-0.012em",
    "body_letter_spacing": "-0.005em",
    "label_letter_spacing": "0.4em",
    "feature_settings": "'kern', 'liga', 'onum', 'calt', 'ss01'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line", "title_serif_italic": true, "corner_lines": false, "vertical_divider": false, "drop_cap": false, "masthead": false, "leaf_svg": true, "lots_of_whitespace": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;0,8..60,600;1,8..60,400;1,8..60,500&family=Fraunces:ital,wght@0,400;1,400&family=Inter:wght@400;500;600&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/fresh_green.html`](../../ppt-output/style-gallery/fresh_green.html)

---

## 3. minimal_gray — Gris Blanco Minimalista (Rehecho nivel NYT Magazine)

```json
{
  "style_id": "minimal_gray",
  "style_name": "Gris Blanco Minimalista (NYT Magazine-grade)",
  "category": "light_premium",
  "inspiration": "NYT Magazine / The Quarterly Review / Revistas académicas",
  "mood_keywords": ["Revista de papel de arroz", "Serif gigante", "División en tres columnas", "Letra capital"],
  "design_soul": "Una mañana de fin de semana, el papel beige se despliega, el enorme título Playfair domina el diseño, el texto inferior se divide en tres columnas mediante finas líneas.",
  "variation_strategy": "La portada usa el masthead del número de revista + título serif gigante + texto en tres columnas, la página del capítulo usa número de capítulo grande + cita corta, la página de contenido usa gráficos + anotaciones.",
  "decoration_dna": {
    "signature_move": "Título principal Playfair Display 70-90px + masthead número de revista + división en tres columnas (column-rule) + letra capital inicial + rojo ladrillo solo para identificadores clave",
    "forbidden": ["Título principal puramente sans", "Fondo oscuro", "Colores saturados", "Radio de esquina demasiado grande", "Efecto neón"],
    "recommended_combos": ["Masthead + Título grande serif + Texto en tres columnas", "Letra capital + Etiqueta rojo ladrillo + Números antiguos onum"]
  },
  "background": { "primary": "#f7f1e3", "gradient_to": "#f7f1e3", "texture": { "type": "paper", "opacity": 0.02 } },
  "card": { "gradient_from": "transparent", "gradient_to": "transparent", "border": "rgba(0,0,0,0.12)", "border_radius": 0, "backdrop_blur": 0 },
  "text": { "primary": "#1a1a1a", "secondary": "#404040", "title_size": 78, "body_size": 12, "card_title_size": 16 },
  "accent": { "primary": ["#a0392b", "#1a1a1a"], "secondary": ["#666", "#999"] },
  "typography": {
    "display_font": "'Playfair Display', 'Cheltenham', Georgia, serif",
    "body_font": "'Source Serif 4', 'Iowan Old Style', Georgia, serif",
    "serif_italic_font": "'Playfair Display', Georgia, serif",
    "mono_font": "'JetBrains Mono', monospace",
    "display_letter_spacing": "-0.025em",
    "headline_letter_spacing": "-0.02em",
    "body_letter_spacing": "0",
    "label_letter_spacing": "0.22em",
    "feature_settings": "'kern', 'liga', 'onum', 'pnum'",
    "tabular_nums": false
  },
  "decorations": { "label_anchor": "horizontal_line", "title_serif_italic": true, "corner_lines": false, "vertical_divider": true, "drop_cap": true, "masthead": true, "three_column_body": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;1,8..60,400&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/minimal_gray.html`](../../ppt-output/style-gallery/minimal_gray.html)

---

## 4. mocha_editorial — Mocha Editorial (Nuevo - Nivel Anthropic)

```json
{
  "style_id": "mocha_editorial",
  "style_name": "Mocha Editorial (Mocha Editorial, Anthropic-grade)",
  "category": "light_premium",
  "inspiration": "Anthropic.com / claude.ai / Pantone 2025 (Mocha Mousse)",
  "mood_keywords": ["Conocimiento cálido", "Revista de café", "serif italic", "Acento rojo ladrillo"],
  "design_soul": "Abriendo una revista de investigación en un café por la tarde, el título serif italic se desarrolla lentamente en la página beige Mocha, la línea de énfasis rojo ladrillo es tan precisa como un marcador de página.",
  "variation_strategy": "La portada usa cuadrícula asimétrica 1fr/1.5fr + título principal serif italic + letra capital, la página del capítulo usa número grande de PARTE + oración guía, la página de contenido usa dos columnas izquierda y derecha + citas.",
  "decoration_dna": {
    "signature_move": "Source Serif 4 + Palabras clave en Instrument Serif italic + Guion corto rojo ladrillo (24px) en la parte superior + Cuadrícula asimétrica 1fr/1.5fr + Letra capital",
    "forbidden": ["Título principal sans", "Fondo oscuro", "Color saturado (excepto énfasis rojo ladrillo)", "Diseño abarrotado", "Efecto neón"],
    "recommended_combos": ["Título serif italic + Letra capital + Etiqueta rojo ladrillo", "Cuadrícula asimétrica + Gran espacio en blanco + tabular-nums onum"]
  },
  "background": { "primary": "#f3ebde", "gradient_to": "#f3ebde", "texture": { "type": "none" } },
  "card": { "gradient_from": "transparent", "gradient_to": "transparent", "border": "rgba(193,80,46,0.15)", "border_radius": 0, "backdrop_blur": 0 },
  "text": { "primary": "#2a1810", "secondary": "#4a3a30", "title_size": 64, "body_size": 16, "card_title_size": 18 },
  "accent": { "primary": ["#c1502e", "#8b5a3c"], "secondary": ["#a85b3a", "#5a4a3a"] },
  "typography": {
    "display_font": "'Source Serif 4', 'Tiempos Text', 'Iowan Old Style', Georgia, serif",
    "body_font": "'Source Serif 4', Georgia, serif",
    "serif_italic_font": "'Instrument Serif', 'Fraunces', 'Source Serif 4', serif",
    "mono_font": "'JetBrains Mono', monospace",
    "display_letter_spacing": "-0.025em",
    "headline_letter_spacing": "-0.015em",
    "body_letter_spacing": "0",
    "label_letter_spacing": "0.25em",
    "feature_settings": "'kern', 'liga', 'onum', 'ss01'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line_short", "title_serif_italic": true, "corner_lines": false, "vertical_divider": false, "drop_cap": true, "masthead": false, "asymmetric_grid": true, "brick_red_short_line": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;0,8..60,600;1,8..60,400;1,8..60,500&family=Instrument+Serif:ital@0;1&family=Fraunces:ital,wght@0,400;0,500;1,400&family=Inter:wght@500;600&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/mocha_editorial.html`](../../ppt-output/style-gallery/mocha_editorial.html)

---

## 5. medical_pulse — Pulso Médico (Nuevo)

```json
{
  "style_id": "medical_pulse",
  "style_name": "Pulso Médico (Medical Pulse)",
  "category": "light_premium",
  "inspiration": "Mayo Clinic / Stanford Medicine / Páginas de productos médicos IA",
  "mood_keywords": ["Blanco puro profesional", "Azul cian médico", "Onda de electrocardiograma ECG", "Cruz roja"],
  "design_soul": "En la pared blanca pura de la clínica, una onda de electrocardiograma cian late lentamente, cada dato es preciso y suave, como las notas de un médico.",
  "variation_strategy": "La portada usa blanco puro + barra superior de color + SVG de onda ECG, la página de datos usa 4 tarjetas cian menta claro, la página de resultados usa insignia de cruz roja + indicadores clave.",
  "decoration_dna": {
    "signature_move": "Fondo blanco puro + Barra superior degradada de 4px (cian-teal-mint) + SVG onda ECG + Tarjetas verde menta claro + Borde izquierdo verde + Icono de cruz arriba a la derecha",
    "forbidden": ["Fondo oscuro", "Colores neón/cyber", "Sensación de revista serif", "Diseño abarrotado", "Elementos de dibujos animados"],
    "recommended_combos": ["Barra superior degradada + SVG ECG + 4 tarjetas de datos", "Insignia de cruz + Etiqueta azul + Datos clínicos tabular-nums"]
  },
  "background": { "primary": "#ffffff", "gradient_to": "#ffffff", "texture": { "type": "none" } },
  "card": { "gradient_from": "#f0fdfa", "gradient_to": "#f0fdfa", "border": "#4ecdc4", "border_radius": 8, "backdrop_blur": 0 },
  "text": { "primary": "#0a2540", "secondary": "#5a7a96", "title_size": 42, "body_size": 14, "card_title_size": 16 },
  "accent": { "primary": ["#00b4d8", "#4ecdc4"], "secondary": ["#95e1d3", "#dc2626"] },
  "typography": {
    "display_font": "'Inter Tight', 'Inter', -apple-system, sans-serif",
    "body_font": "'Inter', -apple-system, sans-serif",
    "serif_italic_font": "'Instrument Serif', Georgia, serif",
    "mono_font": "'IBM Plex Mono', 'JetBrains Mono', monospace",
    "display_letter_spacing": "-0.035em",
    "headline_letter_spacing": "-0.02em",
    "body_letter_spacing": "-0.005em",
    "label_letter_spacing": "0.22em",
    "feature_settings": "'kern', 'liga', 'ss01', 'cv11', 'calt', 'ccmp'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "dot_pulse", "title_serif_italic": false, "corner_lines": false, "vertical_divider": false, "drop_cap": false, "masthead": false, "ecg_pulse": true, "top_gradient_bar": true, "cross_badge": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/medical_pulse.html`](../../ppt-output/style-gallery/medical_pulse.html)

---

## 6. earth_concrete — Tierra Cemento (Nuevo - Arquitectura/Industrial)

```json
{
  "style_id": "earth_concrete",
  "style_name": "Tierra Cemento (Earth Concrete)",
  "category": "light_premium",
  "inspiration": "Suisse Int'l / Firmas de arquitectura / Blue Bottle Coffee",
  "mood_keywords": ["Gris cemento", "Cinta naranja cálido", "Orden de cuadrícula", "Textura industrial"],
  "design_soul": "Un cálido rayo de sol naranja brilla sobre el muro de cemento, la cuadrícula de 60px proyecta una sombra precisa en la pared, todo el texto es sobrio como un plano arquitectónico.",
  "variation_strategy": "La portada usa nombre del edificio en letra grande + ruido de cemento + cinta naranja cálida, la página del proyecto usa 4-6 mono chips, la página de parámetros usa cuadrícula + datos.",
  "decoration_dna": {
    "signature_move": "Fondo degradado de cemento + Textura de ruido radial + Fondo de cuadrícula de 60px + Cinta paralelogramo clip-path naranja cálida + Chip de metadatos JetBrains Mono",
    "forbidden": ["Colores saturados", "Radio de esquina mayor de 8px", "Fuente serif", "Efecto neón", "Elementos de dibujos animados"],
    "recommended_combos": ["Ruido de cemento + Cuadrícula + Cinta naranja cálida", "Fila de mono chips + Número de proyecto + tabular-nums"]
  },
  "background": { "primary": "#d4cfc4", "gradient_to": "#b5b0a5", "texture": { "type": "cement_noise", "opacity": 0.04 } },
  "card": { "gradient_from": "transparent", "gradient_to": "transparent", "border": "rgba(0,0,0,0.08)", "border_radius": 4, "backdrop_blur": 0 },
  "text": { "primary": "#1a1a1a", "secondary": "#5a5a5a", "title_size": 116, "body_size": 14, "card_title_size": 16 },
  "accent": { "primary": ["#ff6b35", "#1a1a1a"], "secondary": ["#666", "#999"] },
  "typography": {
    "display_font": "'Inter Tight', 'Suisse Intl', 'Inter', sans-serif",
    "body_font": "'Inter', -apple-system, sans-serif",
    "serif_italic_font": "'Instrument Serif', Georgia, serif",
    "mono_font": "'JetBrains Mono', 'DM Mono', monospace",
    "display_letter_spacing": "-0.045em",
    "headline_letter_spacing": "-0.025em",
    "body_letter_spacing": "-0.005em",
    "label_letter_spacing": "0.32em",
    "feature_settings": "'kern', 'liga', 'ss01', 'cv11', 'calt', 'ccmp'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line_short", "title_serif_italic": false, "corner_lines": false, "vertical_divider": false, "drop_cap": false, "masthead": false, "cement_texture": true, "grid_pattern": true, "orange_ribbon": true, "mono_chips": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800;900&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/earth_concrete.html`](../../ppt-output/style-gallery/earth_concrete.html)

---

## 7. champagne_gold — Oro Champán (Nuevo - Bodas/Celebraciones)

```json
{
  "style_id": "champagne_gold",
  "style_name": "Oro Champán (Champagne Gold)",
  "category": "light_premium",
  "inspiration": "Invitación de boda de alta gama / Banquete de hotel de 5 estrellas / Ceremonia de premios",
  "mood_keywords": ["Oro champán", "Rombo doble línea", "Playfair italic", "Celebración central"],
  "design_soul": "Sobre el vestido beige, los dorados caracteres Playfair italic son tan exquisitos como joyas, cada hilo de oro ha sido planchado, esperando el momento solemne.",
  "variation_strategy": "La portada usa palabras gigantes centradas Playfair italic + hilos dorados en ambos lados, la página de capítulo usa sello dorado + cita corta, la página de calendario usa fecha dorada + tarjeta beige.",
  "decoration_dna": {
    "signature_move": "Dorado Playfair italic 100-120px + Decoración de rombo de doble línea (Línea-Rombo-Línea Horizontal) + Sello circular dorado + Simetría central + Etiqueta maison con gran espaciado",
    "forbidden": ["Color saturado (excepto oro)", "Fondo oscuro", "Título principal sans", "Diseño abarrotado", "Efecto neón"],
    "recommended_combos": ["Palabra gigante Playfair italic + Rombo doble línea + Sello dorado", "Etiqueta maison 0.65em + Línea horizontal dorada + Simetría central"]
  },
  "background": { "primary": "#faf6ed", "gradient_to": "#f3ead0", "texture": { "type": "none" } },
  "card": { "gradient_from": "transparent", "gradient_to": "transparent", "border": "rgba(201,163,90,0.3)", "border_radius": 0, "backdrop_blur": 0 },
  "text": { "primary": "#2a2218", "secondary": "rgba(42,34,24,0.6)", "title_size": 108, "body_size": 14, "card_title_size": 18 },
  "accent": { "primary": ["#c9a35a", "#b88d3a"], "secondary": ["#f5e8c8", "#8e6a25"] },
  "typography": {
    "display_font": "'Playfair Display', 'Bodoni Moda', 'Didot', Georgia, serif",
    "body_font": "'Inter', -apple-system, sans-serif",
    "serif_italic_font": "'Playfair Display', 'Didot', serif",
    "mono_font": "'JetBrains Mono', monospace",
    "display_letter_spacing": "-0.005em",
    "headline_letter_spacing": "0",
    "body_letter_spacing": "0",
    "label_letter_spacing": "0.65em",
    "feature_settings": "'kern', 'liga', 'dlig', 'calt', 'onum'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line", "title_serif_italic": true, "corner_lines": true, "vertical_divider": true, "drop_cap": false, "masthead": false, "centered_symmetric": true, "gold_double_line": true, "gold_seal": true, "gold_gradient_text": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Inter:wght@300;400;500;600&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/champagne_gold.html`](../../ppt-output/style-gallery/champagne_gold.html)

---

## 8. liquid_glass — Cristal Líquido (Nuevo - iOS 26 / visionOS)

```json
{
  "style_id": "liquid_glass",
  "style_name": "Cristal Líquido (Liquid Glass)",
  "category": "light_premium",
  "inspiration": "iOS 26 / visionOS / Apple Vision Pro",
  "mood_keywords": ["Cristal líquido", "Blob borroso", "Degradado de color", "Profundidad multicapa"],
  "design_soul": "Los paneles de cristal flotantes en Vision Pro, las tarjetas transparentes multicapa refractan un brillo sutil en el halo de color, cada blob es como una estrella líquida.",
  "variation_strategy": "La portada usa un gran degradado colorido + 5 blobs + 1 tarjeta de cristal grande, la página de la aplicación usa 3 tarjetas de cristal + barra de navegación de cristal superior, la página de resultados usa insignia de cristal + datos centrales.",
  "decoration_dna": {
    "signature_move": "Fondo degradado de color (Azul/Rosa/Naranja) + Múltiples blobs borrosos (rgba radial-gradient + filter blur) + Tarjetas de cristal líquido (rgba semitransparente + backdrop-filter blur) + Profundidad multicapa + SF Pro",
    "forbidden": ["Fondo blanco puro/negro puro", "Geometría rígida", "Fuente serif", "Tono oscuro", "Alto contraste"],
    "recommended_combos": ["Degradado de color + 5 blobs + Tarjeta de cristal", "Insignia en vivo + Navegación de cristal superior + Profundidad multicapa"]
  },
  "background": { "primary": "linear-gradient(135deg, #1a73e8 0%, #34a0ff 40%, #ff6b9d 100%)", "gradient_to": "#ff6b9d", "texture": { "type": "blob_glass" } },
  "card": { "gradient_from": "rgba(255,255,255,0.15)", "gradient_to": "rgba(255,255,255,0.08)", "border": "rgba(255,255,255,0.35)", "border_radius": 20, "backdrop_blur": 30 },
  "text": { "primary": "#FFFFFF", "secondary": "rgba(255,255,255,0.85)", "title_size": 96, "body_size": 14, "card_title_size": 18 },
  "accent": { "primary": ["#ff6b9d", "#ffb74d"], "secondary": ["#34a0ff", "#1a73e8"] },
  "typography": {
    "display_font": "-apple-system, 'SF Pro Display', 'Inter Tight', BlinkMacSystemFont, sans-serif",
    "body_font": "-apple-system, 'SF Pro Text', 'Inter', sans-serif",
    "serif_italic_font": "'Instrument Serif', Georgia, serif",
    "mono_font": "'SF Mono', 'JetBrains Mono', monospace",
    "display_letter_spacing": "-0.045em",
    "headline_letter_spacing": "-0.02em",
    "body_letter_spacing": "-0.005em",
    "label_letter_spacing": "0.22em",
    "feature_settings": "'kern', 'liga', 'ss01', 'cv11', 'calt', 'ccmp'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line", "title_serif_italic": true, "corner_lines": false, "vertical_divider": false, "drop_cap": false, "masthead": false, "blob_decorations": true, "glass_cards": true, "multi_layer_depth": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800&family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/liquid_glass.html`](../../ppt-output/style-gallery/liquid_glass.html)
