# Bloque: Matriz de Riesgo / Matriz de Calor (3x3)

Un componente puramente visual en CSS para mostrar relaciones de dos ejes (ej: Impacto vs Probabilidad, Urgencia vs Importancia). Se diseña para ser colocado al lado de un bloque de texto explicativo.

## Uso
- Matrices de Riesgo (Risk Matrix).
- Cuadrantes de Priorización (Eisenhower).
- Mapas de Calor conceptuales.

## Código Base (HTML)

```html
<div class="card glass-panel" style="padding: 22px 28px; display: flex; align-items: center; gap: 32px; grid-column: 1 / -1;">
  
  <!-- CSS del Componente (Inyectado localmente) -->
  <style>
    .matrix-visual { display: flex; flex-direction: column; gap: 4px; flex-shrink: 0; margin-right: 24px; }
    .matrix-row { display: flex; gap: 4px; }
    .matrix-cell { width: 70px; height: 45px; border-radius: 4px; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 700; letter-spacing: 0.05em; text-transform: uppercase; }
    
    .m-low { background: rgba(16,185,129,0.25); color: #6ee7b7; border: 1px solid rgba(16,185,129,0.3); }
    .m-med { background: rgba(245,158,11,0.25); color: #fcd34d; border: 1px solid rgba(245,158,11,0.3); }
    .m-high { background: rgba(239,68,68,0.25); color: #fca5a5; border: 1px solid rgba(239,68,68,0.3); }
    .m-crit { background: rgba(239,68,68,0.45); color: #fff; border: 1px solid rgba(239,68,68,0.6); }
    
    .axis-label { font-size: 11px; font-weight: 700; color: var(--text-secondary); text-align: center; letter-spacing: 0.08em; }
  </style>

  <!-- Matriz Visual (Lado Izquierdo) -->
  <div class="matrix-visual">
    <div class="axis-label">↑ IMPACTO</div>
    <div class="matrix-row">
      <div class="matrix-cell m-med">Med</div>
      <div class="matrix-cell m-high">Alto</div>
      <div class="matrix-cell m-crit">Crítico</div>
    </div>
    <div class="matrix-row">
      <div class="matrix-cell m-low">Bajo</div>
      <div class="matrix-cell m-med">Med</div>
      <div class="matrix-cell m-high">Alto</div>
    </div>
    <div class="matrix-row">
      <div class="matrix-cell m-low">Bajo</div>
      <div class="matrix-cell m-low">Bajo</div>
      <div class="matrix-cell m-med">Med</div>
    </div>
    <div class="axis-label">PROBABILIDAD →</div>
  </div>
  
  <!-- Texto Descriptivo (Lado Derecho) -->
  <div class="hero-text">
    <h3 style="font-family: var(--display-font); font-size: 17px; font-weight: 700; color: var(--text-primary); margin-bottom: 8px; letter-spacing: -0.015em;">
      Priorización basada en Riesgo
    </h3>
    <p style="font-size: 13px; color: var(--text-secondary); line-height: 1.65; max-width: 700px;">
      La Matriz de Riesgo es la herramienta central para decidir <strong>dónde invertir el esfuerzo de prueba</strong>. Clasifica cada funcionalidad según su <strong>Probabilidad de Fallo × Impacto del Fallo</strong>. El cuadrante Crítico recibe cobertura máxima.
    </p>
  </div>
  
</div>
```

## Modificadores / Consejos
1. **Colores Semánticos**: La matriz usa colores hardcoded en RGB específicos (`rgba(239,68,68)`) para mantener los colores de alerta rojo/amarillo/verde independientes del tema global. NO cambies estos colores por `var(--accent-1)`, ya que el semáforo es universal.
2. **Ejes**: Puedes cambiar las flechas y textos de `.axis-label` según el concepto (ej: `↑ URGENCIA` y `IMPORTANCIA →`).
