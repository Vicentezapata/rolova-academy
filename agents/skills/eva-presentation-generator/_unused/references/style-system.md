# Sistema de Estilos (Archivo Guía)

> ⚠️ Este archivo ha sido reemplazado por la nueva estructura. A partir de la versión 2.0, el sistema de estilos se ha expandido de 8 a **26 estilos**, gestionados en directorios a través de 5 categorías.

## Nueva Ubicación

Por favor, lea los siguientes archivos en su lugar:

| Propósito | Nueva Ubicación |
|------|-------|
| **26 Índices de Estilos + Matriz de Decisión + JSON Schema** | [`references/styles/index.md`](styles/index.md) |
| **Profesional Oscuro (7 estilos)** | [`references/styles/dark.md`](styles/dark.md) |
| **Avanzado Claro (8 estilos)** | [`references/styles/light.md`](styles/light.md) |
| **Vibrante (4 estilos)** | [`references/styles/vibrant.md`](styles/vibrant.md) |
| **Cultura Oriental (3 estilos)** | [`references/styles/cultural.md`](styles/cultural.md) |
| **Natural/Retro (4 estilos)** | [`references/styles/natural.md`](styles/natural.md) |
| **Reglas de Tipografía (Compartidas)** | [`references/typography.md`](typography.md) |
| **Directorio de Modos de Fallo** | [`references/principles/failure-modes.md`](principles/failure-modes.md) |
| **Galería de Previsualización de Estilos** | Ejecutar `python3 scripts/gallery.py` → `ppt-output/style-gallery/index.html` |

## Compatibilidad

Los 8 `style_id` originales (`dark_tech` / `xiaomi_orange` / `blue_white` / `royal_red` / `fresh_green` / `luxury_purple` / `minimal_gray` / `vibrant_rainbow`) **se mantienen por completo y se han actualizado** a estándares de clase mundial. Los IDs se mantienen sin cambios para garantizar la compatibilidad. El código de los usuarios existentes no requiere modificaciones.

## Puntos Clave de la Actualización

Mejoras clave del nuevo sistema de estilos en comparación con los 8 estilos originales:

1. **Cantidad**: 8 → 26 (Cubre más escenarios)
2. **Nuevos campos para cada estilo**:
   - `mood_keywords` Etiquetas de estado de ánimo
   - `design_soul` Alma del diseño en una frase
   - `variation_strategy` Estrategia de ritmo entre páginas
   - `decoration_dna.signature_move` Movimiento/Toque distintivo
   - `decoration_dna.forbidden` Prohibiciones explícitas
   - `decoration_dna.recommended_combos` Combinaciones recomendadas
   - `typography.*` Pila de fuentes completa + Reglas de espaciado + Características OpenType
3. **Cada estilo incluye un mockup de referencia de 1280×720**: `ppt-output/style-gallery/<style_id>.html`
4. **Referencia de Calidad**: Prácticas tipográficas reales de marcas como Linear / Anthropic / Stripe / Apple / NYT / Tom Ford / Pitch / Mercury
