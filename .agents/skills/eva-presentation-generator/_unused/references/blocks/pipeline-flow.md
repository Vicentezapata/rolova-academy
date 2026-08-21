# Bloque: Pipeline Flow (Flujo Horizontal)

Un componente para mostrar conexiones horizontales entre conceptos. Ideal para explicar arquitecturas cliente-servidor, flujos de CI/CD, o transformaciones de datos a través del tiempo.

## Uso
- Ciclo Petición-Respuesta (Browser → Servidor → BD).
- Flujo de Build (Código → Compilación → Despliegue).
- Arquitecturas simples y secuenciales.

## Código Base (HTML)

```html
<div class="card glass-panel" style="padding: 24px; display: flex; flex-direction: column; grid-column: 1 / -1; align-items: center; justify-content: center; min-height: 200px;">
  
  <!-- Estilos Inyectados Localmente -->
  <style>
    .pipeline { display: flex; align-items: center; justify-content: center; gap: 4px; width: 100%; flex-wrap: wrap; margin-top: 12px; }
    
    .pipeline-box { background: rgba(255,255,255,0.03); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 16px 20px; text-align: center; min-width: 140px; transition: all 0.3s; display: flex; flex-direction: column; align-items: center; gap: 6px; }
    
    .pipeline-box:hover { border-color: var(--accent-1); background: rgba(34, 211, 238, 0.05); transform: translateY(-3px); }
    
    .pipeline-box svg { width: 28px; height: 28px; color: var(--accent-1); }
    .pipeline-box strong { display: block; font-size: 13.5px; font-weight: 700; color: var(--text-primary); }
    .pipeline-box small { font-size: 11px; color: var(--text-secondary); line-height: 1.4; }
    
    .pipeline-arrow { color: var(--accent-3, #d4a82a); font-size: 24px; font-weight: 900; display: flex; align-items: center; margin: 0 8px; }
  </style>

  <h3 style="font-size: 16px; font-weight: 700; color: var(--text-primary); margin-bottom: 8px;">Flujo MVC Tradicional</h3>
  <p style="font-size: 13px; color: var(--text-secondary); margin-bottom: 24px;">Ciclo de vida de una petición en Laravel.</p>

  <div class="pipeline">
    
    <!-- Caja 1 -->
    <div class="pipeline-box">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>
      <strong>Router</strong>
      <small>Recibe la URL y<br>elige Controlador</small>
    </div>
    
    <!-- Flecha -->
    <div class="pipeline-arrow">→</div>
    
    <!-- Caja 2 -->
    <div class="pipeline-box">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"></path></svg>
      <strong>Controller</strong>
      <small>Pide datos y<br>prepara lógica</small>
    </div>
    
    <!-- Flecha -->
    <div class="pipeline-arrow">→</div>
    
    <!-- Caja 3 -->
    <div class="pipeline-box">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect><rect x="7" y="7" width="3" height="9"></rect><rect x="14" y="7" width="3" height="5"></rect></svg>
      <strong>View</strong>
      <small>Blade renderiza<br>HTML al cliente</small>
    </div>
    
  </div>

</div>
```

## Modificadores / Consejos
1. **Grid Completo**: Este bloque luce mucho mejor cuando ocupa toda la fila (`grid-column: 1 / -1`) para que el flujo horizontal respire adecuadamente.
2. **Menos es más**: Usa máximo de 4 `.pipeline-box` para que el ancho no genere un overflow o forcé saltos de línea antiestéticos.
3. **SVG Crudo**: Al igual que en `dir-structure`, incrusta los iconos SVG directamente (tomados de lucide.dev) para evitar fallos de renderizado de JS externo.
