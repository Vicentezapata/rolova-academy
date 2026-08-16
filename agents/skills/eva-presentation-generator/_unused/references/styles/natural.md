# Categoría Natural/Retro (4 Estilos)

> Posicionamiento de la categoría: Elementos naturales + Sentimiento retro + Serio/Oficial. Patagonia / National Geographic / Años 70 / Órganos de gobierno y partidos.

---

## Índice

| # | style_id | Inspiración | En una frase |
|---|----------|------|-------|
| 1 | `botanic_forest` | Patagonia / Nat Geo | Bosque verde oscuro + Atardecer naranja cálido + serif italic |
| 2 | `safari_savanna` | National Geographic | Naranja cálido del desierto + Sello de pasaporte de aventura + Latitud y longitud |
| 3 | `retro_70s` | Wes Anderson / Vinilo | Tricolor marrón naranja amarillo + Fuente redondeada de los 70s + Textura granulada |
| 4 | `gov_authority` | Diario del Pueblo / Consejo de Estado | Solemne rojo oscuro y azul + Estrella de cinco puntas + Sello |

---

## 1. botanic_forest (Nuevo - Exterior/Sostenible)

```json
{
  "style_id": "botanic_forest",
  "style_name": "Bosque Profundo (Botanic Forest)",
  "category": "natural_retro",
  "inspiration": "Patagonia / The North Face / National Geographic",
  "mood_keywords": ["Verde bosque profundo", "Atardecer naranja cálido", "Textura de exteriores", "serif italic"],
  "design_soul": "En lo profundo del bosque antes del anochecer, el último rayo cálido de sol naranja atraviesa las ramas de los pinos, y la silueta de las montañas permanece en silencio a lo lejos.",
  "variation_strategy": "La portada usa título serif italic + SVG de montañas + decoración de hojas, la página de historia usa texto grande + mapa simple, la página de resultados usa 3 tarjetas de datos + kilometraje en tabular-nums.",
  "decoration_dna": {
    "signature_move": "Fondo radial verde oscuro + Acento naranja cálido + Título grande en Source Serif italic + Silueta de montaña SVG + Decoración de hojas SVG",
    "forbidden": ["Verde brillante saturado (verde bebé)", "Fondo blanco puro", "Efecto neón", "Elementos de dibujos animados", "Diseño abarrotado"],
    "recommended_combos": ["Fondo verde oscuro + Halo de sol naranja cálido + serif italic", "Montañas SVG + Hojas SVG + Coordenadas de latitud/longitud mono"]
  },
  "background": { "primary": "#1a2e1f", "gradient_to": "#0d1a14", "gradient_direction": "radial 100% 80% at 70% 30%", "texture": { "type": "subtle_grain", "opacity": 0.03 } },
  "card": { "gradient_from": "rgba(255,140,66,0.08)", "gradient_to": "rgba(255,140,66,0.02)", "border": "rgba(255,140,66,0.25)", "border_radius": 6, "backdrop_blur": 0 },
  "text": { "primary": "#e8efe2", "secondary": "rgba(232,239,226,0.7)", "title_size": 96, "body_size": 14, "card_title_size": 16 },
  "accent": { "primary": ["#ff8c42", "#e8b86d"], "secondary": ["#5a8c3a", "#3a5e28"] },
  "typography": {
    "display_font": "'Source Serif 4', 'Fraunces', Georgia, serif",
    "body_font": "'Inter', -apple-system, sans-serif",
    "serif_italic_font": "'Source Serif 4', 'Fraunces', Georgia, serif",
    "mono_font": "'JetBrains Mono', monospace",
    "display_letter_spacing": "-0.025em",
    "headline_letter_spacing": "-0.015em",
    "body_letter_spacing": "-0.005em",
    "label_letter_spacing": "0.22em",
    "feature_settings": "'kern', 'liga', 'onum', 'calt', 'ss01', 'cv11'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line", "title_serif_italic": true, "corner_lines": false, "vertical_divider": false, "drop_cap": false, "masthead": false, "mountain_silhouette_svg": true, "leaf_svg": true, "warm_sunset_glow": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,500;0,8..60,600;1,8..60,400;1,8..60,500&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/botanic_forest.html`](../../ppt-output/style-gallery/botanic_forest.html)

---

## 2. safari_savanna (Nuevo - Viajes/Aventura)

```json
{
  "style_id": "safari_savanna",
  "style_name": "Aventura en la Sabana (Safari Savanna)",
  "category": "natural_retro",
  "inspiration": "National Geographic / Lonely Planet / Atardecer en la sabana",
  "mood_keywords": ["Naranja cálido del desierto", "Pasaporte de aventura", "Metadatos de lat/long", "Publicación de viajes"],
  "design_soul": "Un diario de viaje de papel kraft abierto, sellado con un matasellos de aventura inclinado, junto a un mapa dibujado a mano y coordenadas de latitud y longitud.",
  "variation_strategy": "La portada usa título en Playfair italic + matasellos de aventura + lat/long, la página de itinerario usa mapa + línea de tiempo, la página de historia usa letra grande + cita.",
  "decoration_dna": {
    "signature_move": "Fondo beige desierto cálido + Borde marrón + Sello de pasaporte de aventura (inclinado -12 grados) + Mapa SVG simple + Metadatos mono de lat/long",
    "forbidden": ["Fondo blanco puro", "Tonos oscuros", "Efecto neón", "Geometría rígida", "Diseño abarrotado"],
    "recommended_combos": ["Fondo beige desierto + Sello inclinado + Mapa simple", "Lat/long mono + Acento naranja atardecer + serif italic"]
  },
  "background": { "primary": "#f3e6cc", "gradient_to": "#e8d4a8", "gradient_direction": "linear 135deg", "texture": { "type": "paper_grain", "opacity": 0.04 } },
  "card": { "gradient_from": "transparent", "gradient_to": "transparent", "border": "rgba(196,77,42,0.4)", "border_radius": 0, "backdrop_blur": 0 },
  "text": { "primary": "#2a1f0f", "secondary": "#5a4a30", "title_size": 78, "body_size": 14, "card_title_size": 16 },
  "accent": { "primary": ["#c44d2a", "#8b3a1f"], "secondary": ["#e8b86d", "#5a4a30"] },
  "typography": {
    "display_font": "'Playfair Display', 'Fraunces', Georgia, serif",
    "body_font": "'Source Serif 4', Georgia, serif",
    "serif_italic_font": "'Playfair Display', 'Fraunces', Georgia, serif",
    "mono_font": "'JetBrains Mono', 'DM Mono', monospace",
    "display_letter_spacing": "-0.025em",
    "headline_letter_spacing": "-0.015em",
    "body_letter_spacing": "0",
    "label_letter_spacing": "0.42em",
    "feature_settings": "'kern', 'liga', 'onum', 'calt', 'ss01'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line", "title_serif_italic": true, "corner_lines": true, "vertical_divider": false, "drop_cap": false, "masthead": false, "expedition_stamp": true, "tilted_passport": true, "simple_map_svg": true, "geo_metadata_mono": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;1,8..60,400&family=JetBrains+Mono:wght@400;500;700&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/safari_savanna.html`](../../ppt-output/style-gallery/safari_savanna.html)

---

## 3. retro_70s (Nuevo - Retro años 70)

```json
{
  "style_id": "retro_70s",
  "style_name": "Retro 70s (Retro 70s)",
  "category": "natural_retro",
  "inspiration": "Wes Anderson / Discos de vinilo / Saul Bass / Carteles de 1970s",
  "mood_keywords": ["Collage marrón naranja amarillo", "Redondeado y grueso", "Grano retro", "Simetría de Wes Anderson"],
  "design_soul": "En un café independiente de Brooklyn en 1972, un póster de Saul Bass cuelga en la pared, y los tres colores marrón, naranja y amarillo son tan armoniosos como la portada de un disco.",
  "variation_strategy": "La portada usa letras gigantes de Bagel Fat One + collage marrón, naranja y amarillo, la página de menú usa decoración circular + tarjeta con esquinas redondeadas, la página de historia usa grano retro + cuerpo serif.",
  "decoration_dna": {
    "signature_move": "Fondo crema + Collage de tres colores marrón, naranja y amarillo + Fuente gruesa y redondeada Bagel Fat One + Grano retro (SVG turbulence) + Elementos decorativos circulares + Simetría de Wes Anderson",
    "forbidden": ["Fondo oscuro", "Efecto neón", "Colores de neón (púrpura, rosa, cian)", "Geometría rígida", "Diseño abarrotado"],
    "recommended_combos": ["Fondo crema + Marrón/naranja circular + Letras gigantes Bagel Fat One", "Textura de grano + Tarjeta de esquina redondeada + Elementos de vinilo"]
  },
  "background": { "primary": "#f4e9d0", "gradient_to": "#f4e9d0", "texture": { "type": "retro_grain", "opacity": 0.10 } },
  "card": { "gradient_from": "#ffffff", "gradient_to": "#f4e9d0", "border": "#6b4423", "border_radius": 8, "backdrop_blur": 0 },
  "text": { "primary": "#2a1810", "secondary": "#5a3823", "title_size": 116, "body_size": 14, "card_title_size": 18 },
  "accent": { "primary": ["#e07a3e", "#d4a82a"], "secondary": ["#6b4423", "#c14d3f"] },
  "typography": {
    "display_font": "'Bagel Fat One', 'Bowlby One', 'Inter Tight', sans-serif",
    "body_font": "'Inter', -apple-system, sans-serif",
    "serif_italic_font": "'Fraunces', Georgia, serif",
    "mono_font": "'JetBrains Mono', 'DM Mono', monospace",
    "display_letter_spacing": "-0.035em",
    "headline_letter_spacing": "-0.02em",
    "body_letter_spacing": "-0.005em",
    "label_letter_spacing": "0.4em",
    "feature_settings": "'kern', 'liga', 'ss01', 'cv11', 'calt'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line", "title_serif_italic": false, "corner_lines": false, "vertical_divider": false, "drop_cap": false, "masthead": false, "circular_decorations": true, "retro_grain": true, "vinyl_record": true, "warm_palette_collage": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Bagel+Fat+One&family=Bowlby+One&family=Inter+Tight:wght@500;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/retro_70s.html`](../../ppt-output/style-gallery/retro_70s.html)

---

## 4. gov_authority (Nuevo - Oficial Serio)

```json
{
  "style_id": "gov_authority",
  "style_name": "Autoridad Oficial (Government Authority)",
  "category": "natural_retro",
  "inspiration": "Portada del Diario del Pueblo / Agencia de Noticias Xinhua / Oficina de Información del Consejo de Estado / Banquete Estatal",
  "mood_keywords": ["Rojo y azul oscuros solemnes", "Songti centrado", "Sello de estrella de cinco puntas", "Contención extrema"],
  "design_soul": "Frente al salón de banquetes del estado en la alfombra roja, el emblema nacional cuelga solemnemente en el centro, y los grandes caracteres Songti están centrados debajo del hilo dorado, cada detalle es tratado con sumo respeto.",
  "variation_strategy": "La portada usa barra horizontal bicolor rojo y azul + título principal centrado en Songti + estrella de cinco puntas, la página del capítulo usa número de capítulo grande + cita, la página de contenido usa datos de cuatro columnas + tabular-nums.",
  "decoration_dna": {
    "signature_move": "Rojo oscuro + Azul oscuro barra superior bicolor + Source Han Serif Songti centrado + SVG de estrella de cinco puntas + Cuadro estilo sello + División de doble línea + Simetría central",
    "forbidden": ["Naranja/amarillo/verde saturados", "Efecto neón", "Elementos de dibujos animados", "Esquinas demasiado redondeadas", "Diseño abarrotado", "Colores pastel de macaron"],
    "recommended_combos": ["Barra bicolor rojo y azul + Songti centrado + Estrella de cinco puntas", "Cuadro de sello + Simetría central + Datos tabular-nums"]
  },
  "background": { "primary": "#fffaf3", "gradient_to": "#fffaf3", "texture": { "type": "subtle_grain", "opacity": 0.02 } },
  "card": { "gradient_from": "#ffffff", "gradient_to": "#fffaf3", "border": "rgba(196,30,58,0.3)", "border_radius": 0, "backdrop_blur": 0 },
  "text": { "primary": "#1a1a1a", "secondary": "#404040", "title_size": 64, "body_size": 14, "card_title_size": 16 },
  "accent": { "primary": ["#c41e3a", "#1a3a6e"], "secondary": ["#8b1721", "#0d2a5e"] },
  "typography": {
    "display_font": "'Source Han Serif SC', 'Noto Serif SC', 'STSong', SimSun, serif",
    "body_font": "'Source Han Sans SC', 'Noto Sans SC', 'Microsoft YaHei', sans-serif",
    "serif_italic_font": "'Source Han Serif SC', serif",
    "mono_font": "'JetBrains Mono', monospace",
    "display_letter_spacing": "0.22em",
    "headline_letter_spacing": "0.15em",
    "body_letter_spacing": "0.05em",
    "label_letter_spacing": "0.45em",
    "feature_settings": "'kern', 'liga', 'palt', 'calt'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line", "title_serif_italic": false, "corner_lines": true, "vertical_divider": true, "drop_cap": false, "masthead": false, "centered_symmetric": true, "red_blue_top_bar": true, "five_star_svg": true, "seal_box": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Noto+Serif+SC:wght@400;500;600;700&family=Noto+Sans+SC:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/gov_authority.html`](../../ppt-output/style-gallery/gov_authority.html)
