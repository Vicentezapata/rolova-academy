# Índice del Sistema de Estilos (26 Estilos / 5 Categorías)

> Cada archivo `<quadrant>.md` en este directorio contiene todas las definiciones de estilo de una categoría.
>
> **Añadir nuevos estilos**: Añade el JSON Schema + CSS Variables + Mock HTML en el `.md` de la categoría correspondiente.
>
> **Compartido entre estilos**: [Reglas de tipografía](../typography.md) · [Modos de fallo](../principles/failure-modes.md) · [Recipe de slide autocontenida](../playbooks/bespoke-slide-recipe.md)

---

## 1. Tabla General de 26 Estilos

| # | style_id | Categoría | Inspiración | Casos de uso | Archivo de categoría |
|---|----------|------|------|---------|---------|
| 1 | `dark_tech` | Profesional Oscuro | Linear.app | IA / SaaS / Herramientas de desarrollo | [dark.md](dark.md) |
| 2 | `xiaomi_orange` | Profesional Oscuro | Apple Keynote (Hardware) | Hardware / IoT / Lanzamiento de autos | [dark.md](dark.md) |
| 3 | `luxury_purple` | Profesional Oscuro | Tom Ford | Lujo / Marcas premium | [dark.md](dark.md) |
| 4 | `nocturne_violet` | Profesional Oscuro | Linear (Versión Violeta) | Diseño SaaS / Lanzamiento de producto | [dark.md](dark.md) |
| 5 | `cyberpunk_neon` | Profesional Oscuro | Cyberpunk 2077 | Esports / Gaming / Web3 | [dark.md](dark.md) |
| 6 | `chrome_y2k` | Profesional Oscuro | Y2K / Vaporwave | Web3 / Retro milenario | [dark.md](dark.md) |
| 7 | `noir_film` | Profesional Oscuro | Película en blanco y negro | Documentales / Videoarte | [dark.md](dark.md) |
| 8 | `blue_white` | Premium Claro | Páginas empresariales de Apple | SaaS empresarial / Capacitación | [light.md](light.md) |
| 9 | `fresh_green` | Premium Claro | Aesop | Cuidado de la piel / Bienestar / Alimentos | [light.md](light.md) |
| 10 | `minimal_gray` | Premium Claro | NYT Magazine | Académico / Legal / Consultoría | [light.md](light.md) |
| 11 | `mocha_editorial` | Premium Claro | Anthropic / Pantone 2025 | Investigación ética en IA / Publicación | [light.md](light.md) |
| 12 | `medical_pulse` | Premium Claro | Blanco azul médico + ECG | Medicina / Farmacia / Seguros | [light.md](light.md) |
| 13 | `earth_concrete` | Premium Claro | Suisse Int'l | Arquitectura / Industria / Café | [light.md](light.md) |
| 14 | `champagne_gold` | Premium Claro | Oro champán | Bodas / Banquetes / Celebraciones | [light.md](light.md) |
| 15 | `liquid_glass` | Premium Claro | iOS 26 / visionOS | XR / AR / Ecosistema Apple | [light.md](light.md) |
| 16 | `vibrant_rainbow` | Vibrante | Stripe Sessions | Marketing / Creadores | [vibrant.md](vibrant.md) |
| 17 | `kindergarten_pop` | Vibrante | Quicksand Infantil | Educación infantil / Preescolar | [vibrant.md](vibrant.md) |
| 18 | `bauhaus_block` | Vibrante | Bauhaus / Suizo | Educación / Marcas creativas | [vibrant.md](vibrant.md) |
| 19 | `candy_pastel` | Vibrante | Macaron | Postres / Panadería / Snacks | [vibrant.md](vibrant.md) |
| 20 | `royal_red` | Cultura Oriental | Ceremonia de apertura Juegos Olímpicos de Invierno Beijing | Estilo chino / Gobierno / Cultura | [cultural.md](cultural.md) |
| 21 | `sakura_wabi` | Cultura Oriental | Wabi-sabi Japonés | Estilo japonés / Ceremonia del té / Hoteles | [cultural.md](cultural.md) |
| 22 | `ink_jade` | Cultura Oriental | Tinta + Beige Claro + Bermellón | Tendencia nacional / Té / Estilo antiguo | [cultural.md](cultural.md) |
| 23 | `botanic_forest` | Natural/Retro | Bosque profundo | Aire libre / Sostenible / Forestal | [natural.md](natural.md) |
| 24 | `safari_savanna` | Natural/Retro | Naranja cálido de sabana | Viajes / Exploración / Documentales | [natural.md](natural.md) |
| 25 | `retro_70s` | Natural/Retro | Retro años 70 | Café independiente / Discos / Vintage | [natural.md](natural.md) |
| 26 | `gov_authority` | Natural/Retro | Emblema nacional / Banquete estatal | Partido y Gobierno / Reuniones importantes / Formal | [natural.md](natural.md) |

---

## 2. Matriz de Decisión de Categorías

Combinar rápidamente con la categoría según las palabras clave del tema:

| Palabras clave del tema | Categoría Recomendada | Estilo por Defecto |
|-----------|---------|---------|
| IA / SaaS / Desarrollador / Modelos grandes / Datos | Profesional Oscuro | `dark_tech` |
| Hardware / Móvil / IoT / Autos / Hogar inteligente | Profesional Oscuro | `xiaomi_orange` |
| Lujo / Moda / Marcas premium | Profesional Oscuro | `luxury_purple` o `noir_film` |
| Juegos / Esports / Web3 | Profesional Oscuro | `cyberpunk_neon` o `chrome_y2k` |
| Corporativo / Capacitación / Negocios / Finanzas | Premium Claro | `blue_white` |
| Académico / Investigación / Whitepapers / Legal | Premium Claro | `minimal_gray` o `mocha_editorial` |
| Medicina / Farmacia / Salud | Premium Claro | `medical_pulse` |
| Arquitectura / Industrial / Manufactura | Premium Claro | `earth_concrete` |
| Bodas / Celebraciones / Premiaciones | Premium Claro | `champagne_gold` |
| Ecosistema Apple / XR / AR / VR | Premium Claro | `liquid_glass` |
| Ambiental / Naturaleza / Cuidado de la piel / Bienestar | Premium Claro | `fresh_green` |
| Marketing / Promoción / Creadores / Social | Vibrante | `vibrant_rainbow` |
| Infantil / Educación / Preescolar / Familia | Vibrante | `kindergarten_pop` |
| Marcas Creativas / Diseño Independiente | Vibrante | `bauhaus_block` |
| Postres / Panadería / Pastelería | Vibrante | `candy_pastel` |
| Estilo chino / Asuntos gubernamentales / Construcción del Partido / Cultura | Cultura Oriental | `royal_red` |
| Estilo japonés / Ceremonia del té / Bed & Breakfast / Wabi-sabi | Cultura Oriental | `sakura_wabi` |
| Tendencia nacional / Té / Cultura creativa antigua | Cultura Oriental | `ink_jade` |
| Exterior / Forestal / Camping | Natural/Retro | `botanic_forest` |
| Viajes / Exploración / Road trip | Natural/Retro | `safari_savanna` |
| Vintage / Vinilos / Café independiente | Natural/Retro | `retro_70s` |
| Partido y Gobierno / Reuniones importantes / Eventos de nivel nacional | Natural/Retro | `gov_authority` |
| **Temas generales sin coincidencia** | — | `blue_white` (Más versátil) |

---

## 3. JSON Schema de Estilos

Cada estilo se define en el archivo de su categoría según el siguiente JSON Schema:

```json
{
  "style_id": "dark_tech",
  "style_name": "Tecnología Oscura (Dark Tech)",
  "category": "dark_professional",

  "inspiration": "Linear.app",
  "mood_keywords": ["Espacio profundo frío", "Instrumento de precisión", "Pulso tenue", "Flujo de datos", "Sentido futurista"],
  "design_soul": "Interior de la cúpula de un observatorio, una fría luz de escaneo de instrumentos azul verdosa cruza rítmicamente la oscura cortina azul: precisión, frialdad, pero cada escaneo insinúa un pulso.",
  "variation_strategy": "Las páginas de datos usan matriz de puntos + líneas de esquina decorativas (alta densidad y tensión), las portadas de capítulos usan gran espacio negativo + halo único (liberación), las páginas de productos usan fondo oscuro completo + panel de datos brillante flotando en el centro (enfoque).",

  "decoration_dna": {
    "signature_move": "Fondo de matriz de puntos + Línea de esquina en forma de L + Halo de aurora",
    "forbidden": ["Bloques de degradado", "Decoración de hojas", "Líneas de separación onduladas", "Colores pastel de macaron", "Sensación de revista con serif"],
    "recommended_combos": [
      "Matriz de puntos + Esquina + Números de marca de agua grandes",
      "Efecto de halo + Puntos de pulso + Marca de agua de números semitransparentes"
    ]
  },

  "background": {
    "primary": "#050b1f",
    "gradient_to": "#0a1f3d",
    "texture": { "type": "grid_dot", "size": 80, "opacity": 0.015 },
    "glow": [
      { "x": "80%", "y": "30%", "color": "#6366f1", "opacity": 0.35, "blur": 60 },
      { "x": "20%", "y": "70%", "color": "#22D3EE", "opacity": 0.25, "blur": 60 }
    ]
  },

  "card": {
    "gradient_from": "#1E293B",
    "gradient_to": "#0F172A",
    "border": "rgba(255,255,255,0.05)",
    "border_radius": 12,
    "backdrop_blur": 10
  },

  "text": {
    "primary": "#FFFFFF",
    "secondary": "rgba(255,255,255,0.7)",
    "title_size": 28,
    "body_size": 14,
    "card_title_size": 20
  },

  "accent": {
    "primary": ["#22D3EE", "#3B82F6"],
    "secondary": ["#FDE047", "#F59E0B"]
  },

  "typography": {
    "display_font": "'Inter Tight', 'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
    "body_font": "'Inter', -apple-system, BlinkMacSystemFont, sans-serif",
    "serif_italic_font": "'Instrument Serif', 'Fraunces', Georgia, serif",
    "mono_font": "'JetBrains Mono', 'DM Mono', 'Courier New', monospace",
    "display_letter_spacing": "-0.045em",
    "headline_letter_spacing": "-0.015em",
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
    "masthead": false
  },

  "font_imports": [
    "https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800&family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"
  ]
}
```

### Definición de Campos

| Campo | Requerido | Descripción |
|------|------|------|
| `style_id` | ✓ | ID único en inglés (snake_case) |
| `style_name` | ✓ | Nombre legible (Español + Inglés entre paréntesis) |
| `category` | ✓ | Una de 5 categorías: `dark_professional` / `light_premium` / `vibrant` / `cultural_oriental` / `natural_retro` |
| `inspiration` | ✓ | Fuente de inspiración (Marca/Sitio web) |
| `mood_keywords` | ✓ | 3-5 etiquetas de estado de ánimo |
| `design_soul` | ✓ | Alma del diseño en una frase (descripción poética) |
| `variation_strategy` | ✓ | Estrategia de ritmo entre páginas |
| `decoration_dna.signature_move` | ✓ | Movimiento distintivo (una frase) |
| `decoration_dna.forbidden` | ✓ | Elementos prohibidos de forma explícita |
| `decoration_dna.recommended_combos` | ✓ | Combinaciones recomendadas |
| `background` | ✓ | Definición de fondo (incluye texture / glow) |
| `card` | ✓ | Definición de tarjetas |
| `text` | ✓ | Definición de texto |
| `accent` | ✓ | Colores de acento (primary 2 colores + secondary 2 colores) |
| `typography` | ✓ | Pila de fuentes + espaciado de letras + características OpenType |
| `decorations` | ✓ | Lista de técnicas distintivas (interruptores booleanos) |
| `font_imports` | ✓ | Arreglo de URLs de Google Fonts |

---

## 4. Compatibilidad

- 8 `style_id` originales (`dark_tech` / `xiaomi_orange` / `blue_white` / `royal_red` / `fresh_green` / `luxury_purple` / `minimal_gray` / `vibrant_rainbow`) se mantienen sin cambios, pero los aspectos visuales se han rehecho de acuerdo con estándares mundiales.
- 18 estilos nuevos utilizan nuevos nombres poéticos.
- El antiguo `references/style-system.md` se ha cambiado a un archivo de guía, redirigiendo a este directorio.
- Todos los campos originales en el Prompt #4 siguen siendo compatibles; los nuevos campos (`mood_keywords` / `design_soul` / `decoration_dna` / `typography` / `decorations`) son de inyección opcional.

---

## 5. Auto-verificación de Calidad

Después de que se complete cada definición de estilo, verifica con estos 7 elementos:

- [ ] Los 7 campos principales completos (style_id / style_name / category / inspiration / mood_keywords / design_soul / decoration_dna)
- [ ] Variables CSS completas (bg/card/text/accent presentes)
- [ ] Pila de fuentes con degradación en 3 niveles (Comercial/Google/Sistema)
- [ ] `decoration_dna.forbidden` enumera claramente al menos 3 elementos prohibidos
- [ ] `font_imports` URL de Google Fonts correcta
- [ ] El mock HTML que lo acompaña se renderiza correctamente en un canvas de 1280×720 (sin errores en la consola)
- [ ] Pasa la validación `scripts/smoke_test.py --style <id>`
