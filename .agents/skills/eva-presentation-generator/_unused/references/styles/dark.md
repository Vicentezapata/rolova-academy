# Categoría Profesional Oscuro (7 Estilos)

> Posicionamiento de la categoría: Fondo oscuro + Alto contraste + Precisión tecnológica / Sensación de lujo. Adecuado para lanzamientos de productos, plataformas SaaS, documentación técnica, artículos de lujo, esports, Web3, etc.
>
> Compartido: [Reglas de tipografía](../typography.md) · [Modos de fallo](../principles/failure-modes.md) · [Bento Grid](../bento-grid.md)

---

## Índice

| # | style_id | Inspiración | En una frase |
|---|----------|------|-------|
| 1 | `dark_tech` | Linear.app | Luz de escaneo de observatorio, sensación de instrumento de precisión en el espacio profundo y frío |
| 2 | `xiaomi_orange` | Apple Keynote (Hardware) | Producto levitando en la noche oscura, sensación de conferencia de lanzamiento con radiación de luz naranja |
| 3 | `luxury_purple` | Tom Ford | Decoración de rombos negro y oro, lujo y moda nivel YSL |
| 4 | `nocturne_violet` | Linear (Versión violeta) | Halo de cristal púrpura, el nocturno de la herramienta del diseñador |
| 5 | `cyberpunk_neon` | Cyberpunk 2077 | Neón púrpura-cian + líneas de escaneo, escena callejera futura de 2077 |
| 6 | `chrome_y2k` | Y2K / Vaporwave | Sensación de cromo plateado del milenio + perspectiva de cuadrícula |
| 7 | `noir_film` | Cine negro / Blanco y negro | Alto contraste blanco y negro + grano de película, textura documental |

---

## 1. dark_tech — Tecnología Oscura

```json
{
  "style_id": "dark_tech",
  "style_name": "Tecnología Oscura (Dark Tech)",
  "category": "dark_professional",

  "inspiration": "Linear.app",
  "mood_keywords": ["Espacio profundo frío", "Instrumento de precisión", "Pulso tenue", "Flujo de datos", "Sentido futurista"],
  "design_soul": "Interior de la cúpula de un observatorio, una fría luz de escaneo de instrumentos azul verdosa cruza rítmicamente la oscura cortina azul: precisión, frialdad, pero cada escaneo insinúa un pulso. Los datos en la pantalla se alinean con la precisión de un mapa estelar.",
  "variation_strategy": "Las páginas de datos usan matriz de puntos + líneas de esquina decorativas (alta densidad y tensión), las portadas de capítulos usan gran espacio negativo + halo único (liberación), las páginas de productos usan fondo oscuro completo + panel de datos brillante flotando en el centro (enfoque). Las tres variaciones extremas alternan formando el ritmo de 'cambiar paneles de instrumentos en el espacio profundo'.",

  "decoration_dna": {
    "signature_move": "Fondo de matriz de puntos + Resplandor de aurora (radial-gradient de doble capa) + Espaciado de letras ajustado Inter Tight + Mezcla de palabras clave en serif italic",
    "forbidden": [
      "Bloques de color con degradado (excepto transiciones sutiles de fondo)",
      "Decoración de hojas / flores",
      "Líneas de separación onduladas",
      "Colores pastel de macaron",
      "Sensación de revista con serif",
      "Fuentes redondeadas de estilo infantil"
    ],
    "recommended_combos": [
      "Matriz de puntos + Decoración de esquinas + Números grandes de marca de agua",
      "Resplandor de aurora + Etiqueta de puntos de pulso + Marca de agua de números semitransparentes",
      "Línea inferior fina (linear-gradient transparent → cyan → transparent) + Tarjeta de cristal"
    ]
  },

  "background": {
    "primary": "#050b1f",
    "gradient_to": "#0a1f3d",
    "gradient_direction": "radial 100% 80% at 50% -20%",
    "texture": { "type": "grid_dot", "size": 80, "opacity": 0.015 },
    "glow": [
      { "x": "80%", "y": "30%", "color": "#6366f1", "opacity": 0.35, "blur": 60 },
      { "x": "20%", "y": "70%", "color": "#22D3EE", "opacity": 0.25, "blur": 60 }
    ]
  },

  "card": {
    "gradient_from": "rgba(34,211,238,0.08)",
    "gradient_to": "rgba(99,102,241,0.04)",
    "border": "rgba(34,211,238,0.2)",
    "border_radius": 8,
    "backdrop_blur": 10
  },

  "text": {
    "primary": "#FFFFFF",
    "secondary": "rgba(255,255,255,0.65)",
    "title_size": 28,
    "body_size": 14,
    "card_title_size": 20
  },

  "accent": {
    "primary": ["#22D3EE", "#3B82F6"],
    "secondary": ["#6366f1", "#FDE047"]
  },

  "typography": {
    "display_font": "'Inter Tight', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
    "body_font": "'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
    "serif_italic_font": "'Instrument Serif', 'Fraunces', Georgia, serif",
    "mono_font": "'JetBrains Mono', 'DM Mono', 'Courier New', monospace",
    "display_letter_spacing": "-0.045em",
    "headline_letter_spacing": "-0.02em",
    "body_letter_spacing": "-0.005em",
    "label_letter_spacing": "0.18em",
    "feature_settings": "'ss01', 'cv11', 'calt', 'kern', 'liga'",
    "tabular_nums": true
  },

  "decorations": {
    "label_anchor": "dot_pulse",
    "title_serif_italic": true,
    "corner_lines": true,
    "vertical_divider": false,
    "drop_cap": false,
    "masthead": false,
    "bottom_thin_line": true
  },

  "font_imports": [
    "https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800&family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"
  ]
}
```

### Variables CSS

```css
:root {
  --bg-primary: #050b1f;
  --bg-secondary: #0a1f3d;
  --card-bg-from: rgba(34,211,238,0.08);
  --card-bg-to: rgba(99,102,241,0.04);
  --card-border: rgba(34,211,238,0.2);
  --card-radius: 8px;
  --text-primary: #FFFFFF;
  --text-secondary: rgba(255,255,255,0.65);
  --accent-1: #22D3EE;
  --accent-2: #3B82F6;
  --accent-3: #6366f1;
  --accent-4: #FDE047;
  --grid-dot-color: #FFFFFF;
  --grid-dot-opacity: 0.015;
  --grid-size: 80px;
  --display-font: 'Inter Tight', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --body-font: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
  --serif-italic-font: 'Instrument Serif', 'Fraunces', Georgia, serif;
  --mono-font: 'JetBrains Mono', 'DM Mono', 'Courier New', monospace;
}
```

### Mock HTML de Referencia

Ver mock completo de 1280×720 en [`ppt-output/style-gallery/dark_tech.html`](../../ppt-output/style-gallery/dark_tech.html).

---

---

## 2. xiaomi_orange — Naranja Xiaomi (Versión Mejorada)

```json
{
  "style_id": "xiaomi_orange",
  "style_name": "Naranja Xiaomi (Xiaomi Orange)",
  "category": "dark_professional",
  "inspiration": "Apple Keynote (Edición Lanzamiento Hardware)",
  "mood_keywords": ["Escenario de producto", "Levitación nocturna", "Radiación de luz naranja", "Brillo metálico"],
  "design_soul": "Un escenario de producto en la noche oscura, una esfera de luz metálica naranja asciende desde la esquina inferior derecha, tiñendo toda la escena con un cálido color de llamas.",
  "variation_strategy": "La portada usa una esfera de luz de producto suspendida en el centro (mayor impacto), la página de especificaciones usa 3 tarjetas de datos oscuras + radiación naranja inferior derecha, la página de contraste proyecta sombras simétricas del producto a ambos lados.",
  "decoration_dna": {
    "signature_move": "Esfera de luz metálica naranja del producto (radial-gradient multicapa + iluminación interior + sombra) + Radiación de luz naranja inferior + Inter Tight espaciado apretado",
    "forbidden": ["Acentos morados / azules", "Colores pastel de macaron", "Sensación de revista con serif", "Bloques de degradado", "Líneas onduladas"],
    "recommended_combos": ["Esfera de luz + Radiación naranja + Números grandes tabular-nums", "Fondo nocturno + Línea de esquina + Reflejo de bola metálica"]
  },
  "background": {
    "primary": "#0a0a0a",
    "gradient_to": "#1a1a1a",
    "gradient_direction": "radial 70% 100% at 70% 100%",
    "texture": { "type": "vignette", "opacity": 0.3 },
    "glow": [{ "x": "70%", "y": "100%", "color": "#FF6900", "opacity": 0.4, "blur": 80 }]
  },
  "card": { "gradient_from": "#1a1a1a", "gradient_to": "#0a0a0a", "border": "rgba(255,105,0,0.2)", "border_radius": 8, "backdrop_blur": 0 },
  "text": { "primary": "#FFFFFF", "secondary": "rgba(255,255,255,0.65)", "title_size": 28, "body_size": 14, "card_title_size": 20 },
  "accent": { "primary": ["#FF6900", "#ff9d4a"], "secondary": ["#FFFFFF", "#ffd16b"] },
  "typography": {
    "display_font": "'Inter Tight', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
    "body_font": "'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
    "serif_italic_font": "'Instrument Serif', 'Fraunces', Georgia, serif",
    "mono_font": "'JetBrains Mono', 'DM Mono', 'Courier New', monospace",
    "display_letter_spacing": "-0.045em",
    "headline_letter_spacing": "-0.02em",
    "body_letter_spacing": "-0.005em",
    "label_letter_spacing": "0.22em",
    "feature_settings": "'ss01', 'cv11', 'calt', 'kern', 'liga'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "dot_pulse", "title_serif_italic": true, "corner_lines": true, "vertical_divider": false, "drop_cap": false, "masthead": false, "bottom_thin_line": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800&family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/xiaomi_orange.html`](../../ppt-output/style-gallery/xiaomi_orange.html)

---

## 3. luxury_purple — Púrpura y Oro de Lujo (Rehecho Nivel YSL)

```json
{
  "style_id": "luxury_purple",
  "style_name": "Púrpura y Oro de Lujo (Luxury, Tom Ford-grade)",
  "category": "dark_professional",
  "inspiration": "Tom Ford / The Row / YSL Beauty",
  "mood_keywords": ["Negro y oro extremo", "Ceremonia simétrica", "Letras gigantes Didot", "Semana de la Moda"],
  "design_soul": "En el centro de una pantalla de tinta pura negra, letras gigantes doradas en Didot levitan en una postura simétrica, con hilos de oro y decoraciones de rombos como botones en ropa de alta costura.",
  "variation_strategy": "La portada usa letras gigantes Didot centradas + decoración de hilo de oro y rombo, las páginas de capítulos usan líneas L doradas en las 4 esquinas + etiqueta de Maison, las páginas de contenido usan doble columna simétrica + división con hilo de oro.",
  "decoration_dna": {
    "signature_move": "Letras gigantes Playfair/Didot italic + Hilo de oro + Rombo dorado + Diseño simétrico centrado + Etiqueta Maison con espaciado de 0.65em",
    "forbidden": ["Título principal sans serif", "Texto con degradado", "Colores neón", "Decoración vivaz", "Esquinas demasiado redondeadas", "Fondo claro"],
    "recommended_combos": ["Hilo de oro + Rombo dorado + Centrado simétrico", "Letras gigantes Didot + Etiqueta con gran espaciado + Espacio en blanco minimalista"]
  },
  "background": { "primary": "#060606", "gradient_to": "#0a0a0a", "texture": { "type": "none" } },
  "card": { "gradient_from": "rgba(201,169,96,0.04)", "gradient_to": "rgba(201,169,96,0.01)", "border": "rgba(201,169,96,0.2)", "border_radius": 0, "backdrop_blur": 0 },
  "text": { "primary": "#f5e8c8", "secondary": "rgba(245,232,200,0.55)", "title_size": 124, "body_size": 14, "card_title_size": 16 },
  "accent": { "primary": ["#c9a960", "#f5e8c8"], "secondary": ["#1a1a1a", "#fff"] },
  "typography": {
    "display_font": "'Playfair Display', 'Bodoni Moda', 'Didot', Georgia, serif",
    "body_font": "'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
    "serif_italic_font": "'Playfair Display', 'Didot', serif",
    "mono_font": "'JetBrains Mono', 'Courier New', monospace",
    "display_letter_spacing": "-0.005em",
    "headline_letter_spacing": "0",
    "body_letter_spacing": "0",
    "label_letter_spacing": "0.65em",
    "feature_settings": "'kern', 'liga', 'dlig', 'swsh'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line", "title_serif_italic": true, "corner_lines": true, "vertical_divider": true, "drop_cap": false, "masthead": false, "centered_symmetric": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500&family=Inter:wght@300;400;500;600&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/luxury_purple.html`](../../ppt-output/style-gallery/luxury_purple.html)

---

## 4. nocturne_violet — Nocturno Violeta (Nuevo)

```json
{
  "style_id": "nocturne_violet",
  "style_name": "Nocturno Violeta (Nocturne Violet)",
  "category": "dark_professional",
  "inspiration": "Linear.app (Versión púrpura) / Herramientas de diseño",
  "mood_keywords": ["Cristal de nocturno", "Resplandor púrpura", "Herramienta de diseñador", "Tarjetas en estado de cristal"],
  "design_soul": "En la noche oscura de un púrpura profundo, un resplandor púrpura flota como una nebulosa, y las tarjetas de estado de cristal refractan luces y sombras púrpuras sutiles en el halo.",
  "variation_strategy": "La portada usa un gran resplandor púrpura + insignia de cristal, la página de datos usa tarjetas de estado de cristal para mostrar indicadores clave, la página de capítulos usa gran espacio en blanco con luz púrpura.",
  "decoration_dna": {
    "signature_move": "Resplandor radial-gradient púrpura + Tarjeta en estado de cristal (backdrop-filter blur + borde rgba púrpura) + Inter Tight + Palabras clave en Editorial New italic",
    "forbidden": ["Acentos cian / azules (para diferenciar de dark_tech)", "Naranja (para diferenciar de xiaomi_orange)", "Colores neón", "Decoración tradicional"],
    "recommended_combos": ["Resplandor de luz púrpura + Tarjeta de cristal + Fondo de cuadrícula", "Etiqueta de punto de pulso + Insignia de cristal + Anillo de progreso"]
  },
  "background": {
    "primary": "#0a0612",
    "gradient_to": "#1a0d2e",
    "gradient_direction": "radial 100% 80% at 50% -20%",
    "texture": { "type": "grid_dot", "size": 80, "opacity": 0.015 },
    "glow": [
      { "x": "75%", "y": "30%", "color": "#9b64ff", "opacity": 0.4, "blur": 60 },
      { "x": "20%", "y": "70%", "color": "#6d3df0", "opacity": 0.25, "blur": 60 }
    ]
  },
  "card": { "gradient_from": "rgba(155,100,255,0.10)", "gradient_to": "rgba(155,100,255,0.04)", "border": "rgba(155,100,255,0.30)", "border_radius": 12, "backdrop_blur": 18 },
  "text": { "primary": "#FFFFFF", "secondary": "rgba(255,255,255,0.65)", "title_size": 28, "body_size": 14, "card_title_size": 20 },
  "accent": { "primary": ["#9b64ff", "#c4a8ff"], "secondary": ["#6d3df0", "#FDE047"] },
  "typography": {
    "display_font": "'Inter Tight', 'Inter', -apple-system, sans-serif",
    "body_font": "'Inter', -apple-system, sans-serif",
    "serif_italic_font": "'Instrument Serif', 'Fraunces', Georgia, serif",
    "mono_font": "'JetBrains Mono', 'DM Mono', 'Courier New', monospace",
    "display_letter_spacing": "-0.045em",
    "headline_letter_spacing": "-0.02em",
    "body_letter_spacing": "-0.005em",
    "label_letter_spacing": "0.18em",
    "feature_settings": "'ss01', 'cv11', 'calt', 'kern', 'liga', 'ccmp'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "dot_pulse", "title_serif_italic": true, "corner_lines": true, "vertical_divider": false, "drop_cap": false, "masthead": false, "glass_card": true, "bottom_thin_line": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800&family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/nocturne_violet.html`](../../ppt-output/style-gallery/nocturne_violet.html)

---

## 5. cyberpunk_neon — Neón Cyberpunk (Nuevo)

```json
{
  "style_id": "cyberpunk_neon",
  "style_name": "Neón Cyberpunk (Cyberpunk Neon)",
  "category": "dark_professional",
  "inspiration": "Cyberpunk 2077 / Ghost in the Shell / Blade Runner 2049",
  "mood_keywords": ["Neón púrpura-cian", "Líneas de escaneo", "Estética de fallo", "Escena callejera 2077"],
  "design_soul": "Las calles nocturnas de 2077, neones cian y manchas de luz magenta parpadean alternativamente, las líneas de escaneo se desplazan por la pantalla y cada texto tiene un desplazamiento bicolor como un fallo de televisión.",
  "variation_strategy": "La portada usa texto gigante glitch + líneas de escaneo, la página de datos usa cajas de ciencia ficción con esquinas cortadas + borde de neón, la página del capítulo usa decoración de arte de píxeles grande.",
  "decoration_dna": {
    "signature_move": "Línea de escaneo (repeating-linear-gradient) + texto glitch (text-shadow de desplazamiento bicolor) + caja de ciencia ficción con esquina cortada clip-path + resplandor de texto de neón (abundante text-shadow)",
    "forbidden": ["Fuentes serif (usa mono)", "Esquinas redondeadas tradicionales", "Naranja cálido", "Acentos dorados (eso es de luxury)", "Degradados sutiles"],
    "recommended_combos": ["Líneas de escaneo + Título glitch + Caja con esquinas cortadas", "Resplandor de neón + Arte de píxeles + Fuente mono"]
  },
  "background": { "primary": "#0a0014", "gradient_to": "#1a0020", "texture": { "type": "scanlines", "opacity": 0.02 } },
  "card": { "gradient_from": "rgba(255,0,200,0.08)", "gradient_to": "rgba(0,255,255,0.04)", "border": "#ff00c8", "border_radius": 0, "backdrop_blur": 0 },
  "text": { "primary": "#FFFFFF", "secondary": "rgba(255,255,255,0.65)", "title_size": 152, "body_size": 14, "card_title_size": 18 },
  "accent": { "primary": ["#00ffff", "#ff00c8"], "secondary": ["#ffd60a", "#ff3b3b"] },
  "typography": {
    "display_font": "'Orbitron', 'JetBrains Mono', 'DM Mono', 'Courier New', monospace",
    "body_font": "'JetBrains Mono', 'DM Mono', 'Courier New', monospace",
    "serif_italic_font": "'Instrument Serif', Georgia, serif",
    "mono_font": "'JetBrains Mono', 'DM Mono', 'Courier New', monospace",
    "display_letter_spacing": "-0.035em",
    "headline_letter_spacing": "-0.01em",
    "body_letter_spacing": "0",
    "label_letter_spacing": "0.30em",
    "feature_settings": "'kern', 'liga', 'calt', 'ss01', 'cv11', 'ccmp'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line", "title_serif_italic": false, "corner_lines": false, "vertical_divider": false, "drop_cap": false, "masthead": false, "scanlines": true, "glitch_text": true, "clip_path_corners": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700;900&family=JetBrains+Mono:wght@400;500;700&family=Inter:wght@400;500;600&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/cyberpunk_neon.html`](../../ppt-output/style-gallery/cyberpunk_neon.html)

---

## 6. chrome_y2k — Cromo Milenario (Nuevo)

```json
{
  "style_id": "chrome_y2k",
  "style_name": "Cromo Milenario (Chrome Y2K)",
  "category": "dark_professional",
  "inspiration": "Y2K / Vaporwave / Apple iPod (2001) / Daft Punk",
  "mood_keywords": ["Sensación de cromo plateado", "Futuro milenario", "Perspectiva de cuadrícula", "Brillo láser"],
  "design_soul": "El sueño electrónico del nuevo milenio, esferas de cromo plateado flotando en un degradado azul-púrpura, la cuadrícula en el horizonte extendiéndose infinitamente, y el título brillando con luz láser plateada.",
  "variation_strategy": "La portada usa texto láser centrado + esferas de metal en ambos lados + horizonte de cuadrícula en perspectiva, las páginas de especificaciones usan tarjetas plateadas + acentos azules.",
  "decoration_dna": {
    "signature_move": "Texto con degradado plateado láser (linear-gradient clip text) + Esferas de metal plateado (radial-gradient multicapa) + Horizonte de cuadrícula SVG en perspectiva + Brillo Y2K",
    "forbidden": ["Colores sólidos mate", "Colores cálidos (Naranja/Amarillo/Rojo)", "Fuentes serif", "Decoración tradicional"],
    "recommended_combos": ["Texto láser + Esfera metálica + Horizonte de cuadrícula", "Tarjeta plateada + Acentos azules + Metadatos mono"]
  },
  "background": { "primary": "#0a0518", "gradient_to": "#1a0d3a", "gradient_direction": "linear 180deg", "texture": { "type": "starfield", "opacity": 0.05 } },
  "card": { "gradient_from": "rgba(192,208,224,0.08)", "gradient_to": "rgba(160,160,232,0.04)", "border": "rgba(0,212,255,0.3)", "border_radius": 4, "backdrop_blur": 10 },
  "text": { "primary": "#e0e8f0", "secondary": "rgba(224,232,240,0.6)", "title_size": 132, "body_size": 14, "card_title_size": 18 },
  "accent": { "primary": ["#c0d0e0", "#00d4ff"], "secondary": ["#ff6bcd", "#a0a0e8"] },
  "typography": {
    "display_font": "'Inter Tight', 'Orbitron', 'Inter', sans-serif",
    "body_font": "'Inter', -apple-system, sans-serif",
    "serif_italic_font": "'Instrument Serif', Georgia, serif",
    "mono_font": "'JetBrains Mono', 'DM Mono', 'Courier New', monospace",
    "display_letter_spacing": "-0.045em",
    "headline_letter_spacing": "-0.02em",
    "body_letter_spacing": "-0.005em",
    "label_letter_spacing": "0.55em",
    "feature_settings": "'ss01', 'cv11', 'calt', 'kern', 'liga', 'ccmp'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line", "title_serif_italic": false, "corner_lines": false, "vertical_divider": false, "drop_cap": false, "masthead": false, "centered_symmetric": true, "chrome_text": true, "metal_orbs": true, "perspective_grid": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800&family=Orbitron:wght@500;700;900&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/chrome_y2k.html`](../../ppt-output/style-gallery/chrome_y2k.html)

---

## 7. noir_film — Película Negra (Nuevo)

```json
{
  "style_id": "noir_film",
  "style_name": "Película Negra (Noir Film)",
  "category": "dark_professional",
  "inspiration": "Magnum Photos / Henri Cartier-Bresson / Christopher Doyle / Susan Sontag",
  "mood_keywords": ["Contraste blanco y negro", "Grano de película", "Textura documental", "Etiqueta de película de revista"],
  "design_soul": "El papel fotográfico en el cuarto oscuro se revela lentamente, mostrando textos blancos de alto contraste y metadatos de película sobre un fondo negro puro, el grano es delicado y sobrio.",
  "variation_strategy": "La portada usa palabras sans gigantes + clave serif italic + metadatos de película, las páginas de capítulos usan división de línea única minimalista + número de secuencia, las páginas de contenido tienen la sensación de una pared de contactos fotográficos.",
  "decoration_dna": {
    "signature_move": "Grano de película SVG turbulence noise + chip de metadatos de película (fuente mono) + Línea de esquina L + Tono monocromo (sin acentos de color)",
    "forbidden": ["Cualquier acento de color (cian/naranja/oro/púrpura/rojo/verde)", "Fondos degradados", "Bordes redondeados mayores de 4px", "Efectos neón", "Elementos de dibujos animados"],
    "recommended_combos": ["Texto blanco sobre fondo negro + Grano de película + Fila de chips de metadatos", "Esquina L + Pared de contactos + División de línea única"]
  },
  "background": { "primary": "#0a0a0a", "gradient_to": "#0a0a0a", "texture": { "type": "film_grain", "opacity": 0.06 } },
  "card": { "gradient_from": "rgba(250,250,250,0.04)", "gradient_to": "transparent", "border": "rgba(250,250,250,0.08)", "border_radius": 0, "backdrop_blur": 0 },
  "text": { "primary": "#fafafa", "secondary": "rgba(250,250,250,0.5)", "title_size": 96, "body_size": 14, "card_title_size": 18 },
  "accent": { "primary": ["#fafafa", "#5a5a5a"], "secondary": ["#2a2a2a", "#9a9a9a"] },
  "typography": {
    "display_font": "'Inter Tight', 'Helvetica Neue', -apple-system, sans-serif",
    "body_font": "'Inter', -apple-system, sans-serif",
    "serif_italic_font": "'Source Serif 4', 'Fraunces', 'Iowan Old Style', Georgia, serif",
    "mono_font": "'JetBrains Mono', 'DM Mono', 'Courier New', monospace",
    "display_letter_spacing": "-0.045em",
    "headline_letter_spacing": "-0.02em",
    "body_letter_spacing": "-0.005em",
    "label_letter_spacing": "0.30em",
    "feature_settings": "'ss01', 'cv11', 'calt', 'kern', 'liga', 'ccmp'",
    "tabular_nums": true
  },
  "decorations": { "label_anchor": "horizontal_line", "title_serif_italic": true, "corner_lines": true, "vertical_divider": true, "drop_cap": false, "masthead": false, "film_grain": true, "film_metadata_chips": true, "monochrome_only": true },
  "font_imports": ["https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800;900&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;1,8..60,400&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"]
}
```

Mock: [`ppt-output/style-gallery/noir_film.html`](../../ppt-output/style-gallery/noir_film.html)
