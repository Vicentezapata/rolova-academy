# Bloque: Directory Structure (Árbol de Explorador)

Este bloque sirve para explicar la arquitectura de carpetas de un proyecto, framework (Laravel, React, Node) o la ubicación física de ciertos archivos. Es altamente visual gracias al uso de Iconos (Lordicon o Lucide).

## Uso
- Explicar MVC (Models, Views, Controllers) basándose en las carpetas.
- Mostrar dónde guardar configuraciones, assets públicos o rutas.
- Enseñar la estructura de un repositorio nuevo.

## Código Base (HTML)

```html
<div class="card glass-panel" style="padding: 24px; display: flex; flex-direction: column; grid-column: span 1;">
  
  <!-- Estilos Inyectados Localmente -->
  <style>
    .dir-structure { display: flex; flex-direction: column; gap: 8px; font-family: var(--mono-font); font-size: 13px; }
    .dir-item { display: flex; align-items: center; gap: 16px; padding: 12px 16px; background: rgba(255,255,255,0.02); border: 1px solid rgba(255,255,255,0.05); border-radius: 8px; transition: all 0.2s; }
    .dir-item:hover { background: rgba(255,255,255,0.05); }
    .dir-item span { display: flex; align-items: center; gap: 8px; font-weight: 700; min-width: 140px; }
    
    .dir-item.folder span { color: var(--accent-3, #d4a82a); } /* Color Carpeta */
    .dir-item.file span { color: var(--text-primary); } /* Color Archivo */
    
    /* Highlight = Resaltar carpeta importante */
    .dir-item.highlight { border-color: var(--accent-1); background: rgba(34, 211, 238, 0.05); }
    .dir-item.highlight span { color: var(--accent-1); }
    
    .dir-desc { color: var(--text-secondary); font-family: var(--body-font); font-size: 12.5px; line-height: 1.5; }
    
    .icon-wrapper { display: flex; align-items: center; justify-content: center; width: 20px; height: 20px; color: currentColor; }
    .icon-wrapper svg { width: 100%; height: 100%; }
  </style>

  <h3 style="font-size: 15px; font-weight: 700; color: var(--text-primary); margin-bottom: 16px;">Estructura Backend</h3>

  <div class="dir-structure">
    <!-- Carpeta Principal Resaltada -->
    <div class="dir-item folder highlight">
      <span>
        <div class="icon-wrapper"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg></div>
        app/
      </span>
      <div class="dir-desc">Lógica de Negocio (Modelos, Controladores).</div>
    </div>
    
    <!-- Carpeta Normal Indentada -->
    <div class="dir-item folder" style="margin-left: 20px;">
      <span>
        <div class="icon-wrapper"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg></div>
        Models/
      </span>
      <div class="dir-desc">Define la estructura de BD.</div>
    </div>
    
    <!-- Carpeta Normal -->
    <div class="dir-item folder">
      <span>
        <div class="icon-wrapper"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 19a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h5l2 3h9a2 2 0 0 1 2 2z"></path></svg></div>
        config/
      </span>
      <div class="dir-desc">Configuraciones globales.</div>
    </div>
    
    <!-- Archivo Resaltado -->
    <div class="dir-item file highlight">
      <span>
        <div class="icon-wrapper"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline><line x1="16" y1="13" x2="8" y2="13"></line><line x1="16" y1="17" x2="8" y2="17"></line><polyline points="10 9 9 9 8 9"></polyline></svg></div>
        .env
      </span>
      <div class="dir-desc">Variables de Entorno secretas.</div>
    </div>
  </div>

</div>
```

## Modificadores / Consejos
1. **SVG Integrados**: Debido a que Lucide puede no inyectarse correctamente vía JavaScript en todos los motores de render, preferimos usar **SVGs crudos incrustados** para los iconos dentro del `.icon-wrapper`. El código base incluye iconos genéricos para "Folder" (carpeta) y "File" (documento con texto).
2. **Indentación**: Para simular jerarquía (carpetas dentro de carpetas), añade `style="margin-left: 20px;"` o `margin-left: 40px;` al elemento `.dir-item`.
3. **Resaltado**: Añade la clase `highlight` a cualquier elemento que sea el punto central de la enseñanza en esa diapositiva.
