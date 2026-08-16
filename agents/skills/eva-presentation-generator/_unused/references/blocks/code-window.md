# Bloque: Code Window (Mac-style Terminal / Editor)

Este bloque genera un contenedor altamente estilizado que simula una ventana de terminal o un editor de código (estilo macOS) con sus 3 botones característicos (Rojo, Amarillo, Verde). Es excelente para mostrar fragmentos de código, comandos de terminal o estructuras de archivos en presentaciones técnicas.

## Uso
- Mostrar código (PHP, JS, SQL, Python, etc.)
- Mostrar salida de consola o comandos (ej: `npm run dev`)
- Enseñar archivos de configuración completos.

## Código Base (HTML)

```html
<div class="card glass-panel" style="padding: 0; display: flex; flex-direction: column; grid-column: span 1; overflow: hidden; border-radius: 12px;">
  
  <!-- Estilos del Componente Inyectados Localmente -->
  <style>
    .code-window { width: 100%; height: 100%; display: flex; flex-direction: column; background: var(--bg-secondary); }
    .cw-header { display: flex; align-items: center; gap: 6px; padding: 12px 16px; background: rgba(0, 0, 0, 0.2); border-bottom: 1px solid rgba(255, 255, 255, 0.08); }
    .cw-dot { width: 12px; height: 12px; border-radius: 50%; border: 1px solid rgba(0,0,0,0.1); }
    .cw-dot.r { background: #FF5F57; }
    .cw-dot.y { background: #FFBD2E; }
    .cw-dot.g { background: #28CA41; }
    .cw-title { margin-left: 12px; font-family: var(--mono-font); font-size: 11px; color: var(--text-secondary); letter-spacing: 0.05em; font-weight: 600; }
    
    .cw-body { padding: 16px; font-family: var(--mono-font); font-size: 12.5px; line-height: 1.6; color: var(--text-primary); white-space: pre-wrap; overflow-x: auto; flex: 1; }
    
    /* Syntax Highlighting Colors */
    .c-c { color: #5C7080; font-style: italic; } /* Comentarios */
    .c-p { color: #BD93F9; } /* Puntuación/Variables */
    .c-s { color: #50FA7B; } /* Strings */
    .c-f { color: #FFB86C; } /* Funciones/Métodos */
    .c-k { color: #FF79C6; } /* Keywords (if, return, public) */
    .c-n { color: #8BE9FD; } /* Nombres/Clases/Propiedades */
  </style>

  <div class="code-window">
    <div class="cw-header">
      <div class="cw-dot r"></div><div class="cw-dot y"></div><div class="cw-dot g"></div>
      <div class="cw-title">UserController.php</div>
    </div>
    
    <div class="cw-body"><span class="c-c">// Recupera el usuario activo</span>
<span class="c-k">public function</span> <span class="c-f">show</span>(<span class="c-p">$</span><span class="c-n">id</span>) {
    <span class="c-p">$</span><span class="c-n">user</span> = <span class="c-n">User</span>::<span class="c-f">findOrFail</span>(<span class="c-p">$</span><span class="c-n">id</span>);
    
    <span class="c-k">return</span> <span class="c-f">view</span>(<span class="c-s">'users.profile'</span>, [
        <span class="c-s">'user'</span> => <span class="c-p">$</span><span class="c-n">user</span>
    ]);
}</div>
  </div>

</div>
```

## Modificadores / Consejos
1. **Resaltado de Sintaxis Manual**: Debes usar las clases `<span class="c-...">` para darle color al código, de lo contrario todo será texto blanco. Esto le da un aspecto ultra-profesional.
   - `c-c`: Comments (Gris cursiva)
   - `c-k`: Keywords como `public`, `function`, `class`, `if`, `return` (Rosa)
   - `c-f`: Funciones y métodos invocados (Naranja)
   - `c-n`: Nombres de clases, atributos, parámetros (Cyan)
   - `c-s`: Cadenas de texto o strings (Verde)
   - `c-p`: Variables principales o signos como `$` (Morado)
2. **Uso de Grid**: Puedes colocar la ventana al lado de un texto explicativo (ej: `grid-column: span 1`) en un layout de 2 columnas, o abarcar toda la fila (`span 2`).
