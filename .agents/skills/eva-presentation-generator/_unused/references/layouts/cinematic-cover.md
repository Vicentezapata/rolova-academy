# Layout 10: Cinematic Cover (Portada Cinemática)

Este layout está diseñado específicamente para lograr un impacto visual espectacular (estilo Unidad 2). Rompe con la grilla convencional inyectando fondos completos y orbes luminosos absolutos, manteniendo el contenido textual perfectamente alineado.

## Características
- Imagen de fondo full-bleed con modo de fusión y gradiente de oscurecimiento.
- Orbes de luz (glows) para dar profundidad atmosférica.
- Tipografía editorial avanzada (Eyebrow y cursivas Instrument Serif).
- Rompe el padding por defecto del `.slide` mediante `position: absolute`.

## Estructura Base (HTML a generar en `html_content`)

```html
<!-- CAPAS DE FONDO ABSOLUTAS -->
<div class="bg-img" style="position: absolute; inset: 0; background-size: cover; background-position: center right; opacity: 0.25; z-index: 0; background-image: url('../images/cover.png');"></div>
<div class="bg-overlay" style="position: absolute; inset: 0; background: linear-gradient(90deg, var(--bg-primary) 40%, transparent 100%); z-index: 1;"></div>
<div class="grid-texture" style="position: absolute; inset: 0; z-index: 1; background-image: radial-gradient(var(--accent-3) 1px, transparent 1px); background-size: 40px 40px; opacity: 0.08;"></div>
<div class="glow1" style="position: absolute; width: 400px; height: 400px; border-radius: 50%; background: var(--accent-3); filter: blur(60px); top: -80px; right: 320px; z-index: 1; opacity: 0.2;"></div>
<div class="glow2" style="position: absolute; width: 400px; height: 400px; border-radius: 50%; background: var(--accent-3); filter: blur(60px); bottom: -60px; left: 80px; z-index: 1; opacity: 0.2;"></div>

<!-- CAPA DE CONTENIDO FRONTAL -->
<div class="content-front" style="position: relative; z-index: 10; display: flex; flex-direction: column; justify-content: center; height: 100%; max-width: 800px;">
  
  <div class="eyebrow">
    <div class="dot"></div> IF203IINF &nbsp;·&nbsp; IPSS &nbsp;·&nbsp; 2026
  </div>
  
  <h1 class="page-title gradient-text" style="font-size: 56px; font-weight: 800; line-height: 1.1; letter-spacing: -0.045em; margin-bottom: 20px;">
    Unidad 2<br>
    <em style="font-family: var(--serif-italic-font); font-style: italic; color: var(--accent-1);">Planificación</em><br>
    de Pruebas
  </h1>
  
  <p class="subtitle" style="font-size: 17px; color: var(--text-secondary); line-height: 1.7; max-width: 580px; margin-bottom: 44px;">
    Estrategia, diseño y documentación de pruebas de software. Desde la selección contextual de tipos de prueba hasta el Plan Maestro IEEE 829.
  </p>
  
  <div class="meta-row" style="display: flex; align-items: center; gap: 20px;">
    <div class="meta-chip accent">4 Sesiones</div>
    <div class="meta-chip accent">21 Slides</div>
    <div class="meta-chip">Gherkin · RTM · Test Plan · INVEST</div>
  </div>
</div>
```

## Reglas de Implementación
1. **Fondo e Imágenes**: Reemplaza `url('../images/cover.png')` por la ruta correcta si hay una imagen asignada en el planning. Si no hay imagen, deja la URL vacía o usa un degradado dramático.
2. **Colores Variables**: Usa EXCLUSIVAMENTE las variables CSS (`var(--accent-1)`, `var(--bg-primary)`, etc.).
3. **El elemento `<em>`**: Úsalo dentro del `<h1>` para aplicar la fuente `Instrument Serif` en cursiva a la palabra más importante del título.
4. **Z-Index**: Mantén el `z-index` de las capas de fondo en `0` o `1`, y el del `content-front` en `10` para garantizar que el texto sea seleccionable.
