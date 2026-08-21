# Layout 11: Hero & Cards (1 Arriba + 3 Abajo)

Un layout muy estructurado para presentar un concepto principal (Hero) seguido de 3 puntos de apoyo, categorías o conclusiones. Ideal para explicar un tema central y desglosarlo inmediatamente en tres partes.

## Características
- Bloque Hero superior que abarca todo el ancho.
- 3 Tarjetas en la parte inferior, idénticas en tamaño.
- Elementos flotantes como la nota del profesor (`teacher-note`).

## Estructura Base (HTML a generar en `html_content`)

```html
<div style="display: grid; grid-template: auto 1fr / repeat(3, 1fr); gap: 18px; height: 100%; width: 100%;">
  
  <!-- Estilo del Teacher Note (Para inyectar localmente si se usa) -->
  <style>
    .teacher-note { position: absolute; bottom: 20px; left: 48px; background: rgba(245,158,11,0.15); border: 1px solid rgba(245,158,11,0.4); border-radius: 8px; padding: 12px 16px; display: flex; align-items: flex-start; gap: 12px; max-width: 800px; z-index: 20; }
    .teacher-note h4 { color: var(--warn, #f59e0b); font-size: 12px; text-transform: uppercase; letter-spacing: 0.1em; margin-bottom: 4px; font-family: var(--mono-font); }
    .teacher-note p { color: var(--text-secondary); font-size: 12px; line-height: 1.5; }
  </style>

  <!-- Bloque Hero (Top) -->
  <div class="hero glass-panel" style="grid-column: 1 / -1; padding: 22px 28px; display: flex; align-items: center; gap: 32px; border-radius: 8px;">
    <!-- Aquí puedes poner texto, una Risk Matrix, u otro bloque -->
    <div class="hero-text">
      <h3 style="font-family: var(--display-font); font-size: 17px; font-weight: 700; color: var(--text-primary); margin-bottom: 8px;">Título Principal del Hero</h3>
      <p style="font-size: 13px; color: var(--text-secondary); line-height: 1.65; max-width: 700px;">
        Explicación detallada del concepto central que abarca la parte superior de la slide.
      </p>
    </div>
  </div>

  <!-- Tarjetas Inferiores (Bottom 3) -->
  <div class="card glass-panel" style="padding: 20px 22px; display: flex; flex-direction: column; gap: 8px; border-radius: 8px;">
    <div class="card-tag" style="font-family: var(--mono-font); font-size: 10px; color: var(--accent-1); text-transform: uppercase;">Tag 1</div>
    <h4 style="font-size: 14px; font-weight: 700; color: var(--text-primary);">Concepto 1</h4>
    <p style="font-size: 12px; color: var(--text-secondary); line-height: 1.65;">Descripción del primer punto de apoyo derivado del hero principal.</p>
  </div>
  
  <div class="card glass-panel" style="padding: 20px 22px; display: flex; flex-direction: column; gap: 8px; border-radius: 8px;">
    <div class="card-tag" style="font-family: var(--mono-font); font-size: 10px; color: var(--accent-2); text-transform: uppercase;">Tag 2</div>
    <h4 style="font-size: 14px; font-weight: 700; color: var(--text-primary);">Concepto 2</h4>
    <p style="font-size: 12px; color: var(--text-secondary); line-height: 1.65;">Descripción del segundo punto de apoyo.</p>
  </div>
  
  <div class="card glass-panel" style="padding: 20px 22px; display: flex; flex-direction: column; gap: 8px; border-radius: 8px;">
    <div class="card-tag" style="font-family: var(--mono-font); font-size: 10px; color: var(--accent-3); text-transform: uppercase;">Tag 3</div>
    <h4 style="font-size: 14px; font-weight: 700; color: var(--text-primary);">Concepto 3</h4>
    <p style="font-size: 12px; color: var(--text-secondary); line-height: 1.65;">Descripción del tercer punto de apoyo.</p>
  </div>

  <!-- Opcional: Teacher Note Absoluto -->
  <!-- <div class="teacher-note"><div class="teacher-text"><h4>Nota del Profesor</h4><p>Explicación oral recomendada para esta diapositiva.</p></div></div> -->

</div>
```

## Reglas de Implementación
1. **Grid Asimétrico Vertical**: El `grid-template: auto 1fr / repeat(3, 1fr)` hace que la fila de arriba (Hero) ocupe su propio tamaño (`auto`), y las tarjetas de abajo se expandan al espacio restante (`1fr`), distribuidas en 3 columnas iguales.
2. **Teacher Note**: Es un elemento posicionado absolutamente (`bottom: 20px; left: 48px;`) ideal para añadir tips de enseñanza sobre el lienzo de la slide, sin romper la cuadrícula.
3. **Badges**: Puedes inyectar las clases `badge` (W12) dentro de las tarjetas inferiores para jerarquizarlas.
