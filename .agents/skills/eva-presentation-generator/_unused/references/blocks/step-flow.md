# Bloque: Step Flow (Flujo Vertical Numerado)

Un componente elegante y altamente legible para guiar a la audiencia a través de un tutorial, un proceso secuencial o un algoritmo paso a paso.

## Uso
- Procesos de instalación o setup.
- Recetas algorítmicas (Paso 1, Paso 2, Paso 3).
- Ciclos de vida o secuencias ordenadas.

## Código Base (HTML)

```html
<div class="card glass-panel" style="padding: 24px; display: flex; flex-direction: column; grid-column: span 1;">
  
  <!-- Estilos Inyectados Localmente -->
  <style>
    .step-flow { display: flex; flex-direction: column; gap: 12px; margin-top: 8px; }
    .step-item { display: flex; align-items: flex-start; gap: 16px; padding: 16px 20px; background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.06); border-radius: 10px; transition: all 0.3s; }
    .step-item:hover { border-color: rgba(34, 211, 238, 0.3); background: rgba(34, 211, 238, 0.04); transform: translateX(2px); }
    
    .step-num { width: 34px; height: 34px; border-radius: 50%; background: linear-gradient(135deg, var(--accent-1), var(--accent-2)); display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 14px; flex-shrink: 0; color: #000; font-family: var(--display-font); box-shadow: 0 4px 10px rgba(0,0,0,0.3); }
    
    .step-content { flex: 1; display: flex; flex-direction: column; gap: 4px; }
    .step-content strong { font-size: 14px; color: var(--text-primary); }
    .step-content p { font-size: 12.5px; color: var(--text-secondary); line-height: 1.5; }
    .step-content code { background: rgba(255,255,255,0.1); color: var(--accent-3); padding: 2px 6px; border-radius: 4px; font-family: var(--mono-font); font-size: 11px; }
  </style>

  <h3 style="font-size: 16px; font-weight: 700; color: var(--text-primary); margin-bottom: 8px;">Flujo de Migración</h3>
  <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 12px;">Cómo crear y ejecutar una tabla nueva en Laravel.</p>

  <div class="step-flow">
    
    <div class="step-item">
      <div class="step-num">1</div>
      <div class="step-content">
        <strong>Crear el Archivo</strong>
        <p>Ejecuta <code>php artisan make:migration</code> en la terminal.</p>
      </div>
    </div>
    
    <div class="step-item">
      <div class="step-num">2</div>
      <div class="step-content">
        <strong>Definir Columnas</strong>
        <p>Abre el archivo generado y define las columnas usando el esquema Blueprint.</p>
      </div>
    </div>
    
    <div class="step-item">
      <div class="step-num">3</div>
      <div class="step-content">
        <strong>Ejecutar Migración</strong>
        <p>Ejecuta <code>php artisan migrate</code> para materializar los cambios en la BD.</p>
      </div>
    </div>
    
  </div>

</div>
```

## Modificadores / Consejos
1. **Pocos pasos**: Por razones de altura del Grid, mantén un máximo de 3 o 4 pasos por bloque.
2. **Código Inline**: Usa siempre la etiqueta `<code>` dentro del `step-content` si hablas de comandos, URLs o nombres de archivos. El CSS local se encarga de estilizarlo para que resalte.
