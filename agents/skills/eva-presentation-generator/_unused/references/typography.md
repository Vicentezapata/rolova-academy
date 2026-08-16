# Reglas de Hierro de Tipografía de Clase Mundial (Typography Bible)

> Este archivo resume todas las reglas de tipografía compartidas por los 26 estilos. **Lectura obligatoria antes de generar cada borrador de diseño HTML**.
>
> Fuentes de inspiración: Prácticas tipográficas reales de marcas como Linear / Anthropic / Stripe / Apple / Vercel / NYT Magazine / Tom Ford / Pitch / Mercury / Arc / Notion.

---

## 1. Regla de Hierro del Espaciado de Letras (Letter-Spacing)

El espaciado de letras se clasifica por el tamaño de la fuente, **no se puede aplicar un enfoque único para todos**:

| Nivel | Tamaño de Fuente | letter-spacing | Uso |
|------|------|----------------|------|
| **Display** | ≥ 48px | `-0.025em ~ -0.045em` | Título principal de portada / Grandes datos |
| **Headline** | 28-44px | `-0.015em` | Título principal de la página |
| **Title** | 20-24px | `-0.01em` | Títulos de tarjetas |
| **Body** | 13-16px | `-0.005em` ligeramente contraído | Párrafos de texto |
| **Caption** | 11-12px | `+0.05em` | Anotaciones auxiliares / Notas al pie |
| **Overline** | 10-12px | `+0.15em ~ +0.3em` | Identificador PART / Subtítulos pequeños |
| **Maison label** | 10-11px | `+0.4em ~ +0.65em` | Firma de marca de lujo |

> Regla de oro: Cuanto más grande sea la fuente, más ajustado debe ser el espaciado; cuanto más pequeña sea, más suelto. Esta es una regla de hierro compartida por Apple / Linear / Tom Ford.

---

## 2. Los Números Deben Ser Tabular-Nums

**Todos los datos numéricos deben** estar alineados con un ancho fijo (monoespaciado); de lo contrario, los números saltarán al cambiar en la presentación y se verán de baja calidad:

```css
.data-number {
  font-variant-numeric: tabular-nums proportional-nums;
}
```

Alcance aplicable: Todas las tarjetas `card_type=data`, indicadores de KPIs, datos comparativos, años/fechas, precios, porcentajes, IDs y cualquier número.

---

## 3. Características OpenType Obligatorias

La llamada de fuente para cada estilo debe habilitar las características avanzadas de tipografía:

```css
.world-class {
  font-feature-settings: "kern", "liga", "ss01", "cv11", "calt", "ccmp";
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
```

| Característica | Función |
|------|------|
| `kern` | Pares de interletraje (Kerning) |
| `liga` | Ligaduras estándar (fi, fl, ffi)|
| `ss01` ~ `ss20` | Conjuntos estilísticos (Stylistic Sets, difieren según la fuente) |
| `cv01` ~ `cv99` | Variantes de caracteres (ej. Inter cv11 tiene una 'g' más moderna) |
| `calt` | Alternativas contextuales (ej. ligaduras de flechas -> →) |
| `ccmp` | Composición y descomposición de glifos |

---

## 4. Combinación de Sans + Serif Italic (Técnica de Firma)

**La técnica oculta utilizada por Linear / Stripe / Apple**: Reemplazar palabras clave en el título con tipografía *serif cursiva*, eleva instantáneamente la calidad.

```html
<h1 class="headline">
  Built for <em>the future.</em>
</h1>
```

```css
.headline { font-family: 'Inter Tight', sans-serif; font-weight: 600; }
.headline em {
  font-family: 'Instrument Serif', 'Fraunces', serif;
  font-style: italic;
  font-weight: 400;
  letter-spacing: -0.02em;
}
```

Aplicabilidad: Todos los estilos profesionales oscuros + estilos avanzados claros.

---

## 5. Capitular (Drop Cap)

Tipografía insignia que aporta sensación de revista y editorial. Aplicable a `mocha_editorial` / `paper_archive` / `noir_film` y escenarios de textos largos:

```css
.body-text::first-letter {
  float: left;
  font-size: 60px;
  line-height: 0.85;
  padding: 6px 10px 0 0;
  font-weight: 600;
  font-family: 'Fraunces', 'Source Serif 4', serif;
  color: var(--text-primary);
}
```

---

## 6. Cuadrícula Asimétrica

**Evita diseños que sean siempre 50/50 o centrados**. Comúnmente usado en sitios web de clase mundial:

| Proporción | Aplicación |
|------|------|
| `1fr / 1.5fr` | Título a la izquierda, texto a la derecha (Sensación editorial) |
| `2fr / 3fr` | Imagen principal a la derecha, texto a la izquierda |
| `1fr / 2fr / 1fr` | Tres columnas, la central lleva la información principal |
| `auto / 1fr` | Número grande + interpretación, ancho adaptativo |

El espacio en blanco debe dar lugar de manera proactiva a la información principal; no debe distribuirse por igual.

---

## 7. Ancla de Etiqueta (Label Anchor)

Agregar un guion corto o un punto `::before` delante de una etiqueta para establecer un ancla visual. **Esta es la técnica distintiva de Linear / Stripe**:

```html
<div class="label">— Research · 2026</div>
```

```css
.label {
  font-size: 11px;
  letter-spacing: 0.18em;
  color: var(--accent-1);
  font-weight: 600;
  text-transform: uppercase;
  display: inline-flex;
  align-items: center;
  gap: 8px;
}
.label::before {
  content: '';
  width: 24px;
  height: 1px;
  background: currentColor;
}
```

O un punto con brillo (`dot_pulse`):

```css
.label::before {
  width: 6px; height: 6px; border-radius: 50%;
  background: var(--accent-1);
  box-shadow: 0 0 8px currentColor;
}
```

---

## 8. Degradación de la Pila de Fuentes en Tres Niveles

Cada llamada de fuente en cada estilo sigue un respaldo (fallback) de tres niveles:

```
[Fuente Comercial (Si el usuario tiene licencia)]
  → [Equivalente en Google Fonts]
  → [Respaldo de Fuente del Sistema]
```

**Ejemplos prácticos**:

| Rol | Comercial | Google Fonts | Respaldo del Sistema |
|------|------|--------------|---------|
| Sans Moderna | Söhne / GT America / ABC Diatype | Inter / Inter Tight | -apple-system, BlinkMacSystemFont, sans-serif |
| Serif Editorial | Tiempos Text / SangBleu OG | Source Serif 4 / Fraunces | Iowan Old Style, Georgia, serif |
| Serif Display Cursiva | Editorial New | Instrument Serif | Georgia italic |
| Serif de Moda | Didot | Playfair Display | Bodoni Moda, serif |
| Monospace | Söhne Mono / Geist Mono | JetBrains Mono / DM Mono | Courier New, monospace |
| Serif Chino | 思源宋体 (Source Han Serif) | Noto Serif SC | STSong, SimSun, serif |
| Sans Chino | PingFang / Microsoft YaHei (Fuentes del sistema) | — | PingFang SC, Microsoft YaHei, sans-serif |

Uso:

```css
font-family:
  'Söhne',                                     /* Comercial */
  'Inter Tight', 'Inter',                      /* Google */
  -apple-system, BlinkMacSystemFont,           /* Sistema */
  'Segoe UI', sans-serif;                      /* Fallback */
```

---

## 9. Texturas Sutiles (No colores puros sin textura)

| Tipo de Estilo | Textura |
|---------|------|
| Oscuro | Cuadrícula de puntos (40-80px) + Brillo tipo aurora (múltiples capas radial-gradient) |
| Claro Avanzado | Micro ruido (SVG turbulence o matriz de puntos con baja opacidad) |
| Revista | Fondo color papel beige + bordes internos |
| Retro | Sensación de grano + bloques de color semitransparentes |

Implementación:

```css
/* Cuadrícula de puntos oscuros */
.dark-bg {
  background-image:
    radial-gradient(circle, rgba(255,255,255,0.03) 1px, transparent 1px);
  background-size: 80px 80px;
}

/* Brillo tipo aurora */
.aurora-glow::before {
  content: '';
  position: absolute; inset: 0;
  background:
    radial-gradient(circle at 80% 30%, rgba(99, 102, 241, 0.35) 0%, transparent 40%),
    radial-gradient(circle at 20% 70%, rgba(34, 211, 238, 0.25) 0%, transparent 35%);
  filter: blur(60px);
  pointer-events: none;
}
```

---

## 10. Sistema Unificado de Pie de Página (Footer)

Cada página (excepto la portada y las portadas de capítulos) debe tener un pie de página unificado. **Tamaño de fuente 11px, opacidad 0.5, espaciado de letras 1px**, extremadamente discreto, para no desviar la atención del contenido:

```html
<div class="footer">
  <span class="part-label">PART 01 — Nombre del Capítulo</span>
  <span class="page-info">07 / 15  |  Nombre de la Marca</span>
</div>
```

```css
.footer {
  position: absolute; bottom: 20px; left: 40px; right: 40px;
  display: flex; justify-content: space-between; align-items: center;
  font-size: 11px;
  color: var(--text-secondary);
  opacity: 0.5;
  letter-spacing: 0.1em;
  font-family: 'Inter', sans-serif;
}
```

---

## 11. Importación de Fuentes (Font Imports)

Cada estilo solo hace `@import` de las fuentes que realmente utiliza, evitando cargar todas las Google Fonts en cada página. En el `<head>` del HTML:

```html
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter+Tight:wght@500;600;700;800&family=Instrument+Serif:ital@0;1&display=swap');
</style>
```

---

## 12. Reglas de Mezcla Chino/Inglés

- **Agregar automáticamente un espacio de media anchura (espacio simple)** entre el chino y el inglés/números (por ejemplo: "Tasa de crecimiento alcanza el 47.3%").
- Se recomienda usar `font-variant-numeric: tabular-nums` para que los números estén alineados con el mismo ancho.
- Para números grandes (36px+), se sugiere usar `font-family: 'Inter Tight', 'DIN', var(--font-family)` para darles más impacto.
- La puntuación china usa ancho completo (。，；：).
- La puntuación inglesa usa ancho medio + espacio posterior.

---

## 13. Reglas de Seguridad de Contraste

El color del texto debe formar suficiente contraste con su fondo directo:

| Tipo de Fondo | Requisito de Color del Texto |
|---------|------------|
| Oscuro (Brillo < 40%) | Título usa blanco, el cuerpo usa 70% blanco |
| Claro (Brillo > 60%) | Título usa oscuro, el cuerpo usa gris al 60-70% |
| Interior de la Tarjeta | Sigue la claridad/oscuridad del fondo de la tarjeta |
| Texto de color accent | Solo se usa para Títulos/Etiquetas/Datos Numéricos |

**Prohibido**:
- Fondo Oscuro + Texto Oscuro
- Fondo Claro + Texto Blanco
- Valores de color codificados (hardcoded) (se deben usar variables CSS)

---

## 14. Checklist de Auto-revisión Tipográfica

Después de generar cada página HTML, compara con estas 7 reglas para auto-revisión:

- [ ] Letras grandes (≥48px) el letter-spacing está en -0.025em ~ -0.045em
- [ ] Subtítulos pequeños el letter-spacing es ≥ 0.15em
- [ ] Todos los números tienen activado `font-variant-numeric: tabular-nums`
- [ ] Características OpenType (kern, liga) están habilitadas al menos
- [ ] Las tres capas de degradación (fallback) de la pila de fuentes están completas (Comercial/Google/Sistema)
- [ ] Las palabras clave en los títulos utilizan *serif italic* para mezcla (si aplica)
- [ ] El pie de página es uniforme (excepto en portadas / portadas de capítulos)

