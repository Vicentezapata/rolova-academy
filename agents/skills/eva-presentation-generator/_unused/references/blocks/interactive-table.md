# Bloque: Tabla Interactiva (RTM / Matrices de Datos)

Las tablas estándar pueden ser aburridas. Este bloque te enseña a construir una tabla avanzada con hover, etiquetas de datos (`<code>`), insignias de estado (Badges) y elementos clickeables que abren modales descriptivos, ideal para matrices de trazabilidad (RTM) o glosarios técnicos.

## Uso
- Matriz de Trazabilidad (RTM).
- Listados de APIs, Casos de Prueba, o Roles.
- Comparaciones complejas que requieren ampliación de información.

## Código Base (HTML)

```html
<div class="card glass-panel" style="padding: 22px 26px; display: flex; flex-direction: column; gap: 14px; grid-column: 1 / -1; min-height: 300px;">
  
  <div class="card-tag" style="color: var(--accent-1); font-family: var(--mono-font); font-size: 10px; letter-spacing: 0.18em; text-transform: uppercase;">
    Matriz de Trazabilidad de Requerimientos
  </div>
  
  <h3 style="font-size: 16px; font-weight: 700; color: var(--text-primary); letter-spacing: -0.015em; margin-bottom: 4px;">
    Cada requerimiento mapeado a sus Test Cases
  </h3>
  
  <p style="font-size: 12.5px; color: var(--text-secondary); line-height: 1.7;">
    Haz clic en los Requerimientos o Casos de Prueba para ver los detalles completos.
  </p>
  
  <!-- Estilos de Tabla en línea (el contenedor aísla los estilos) -->
  <style>
    .rtm-table { width: 100%; border-collapse: collapse; flex: 1; }
    .rtm-table th { text-align: left; padding: 10px 12px; background: rgba(255,255,255,0.03); color: var(--accent-3); font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.12em; border-bottom: 1px solid rgba(255,255,255,0.1); }
    .rtm-table td { padding: 9px 12px; color: var(--text-secondary); border-bottom: 1px solid rgba(255,255,255,0.05); font-size: 12px; vertical-align: middle; }
    .rtm-table tr:hover td { background: rgba(255,255,255,0.03); }
    .rtm-table code { background: rgba(255,255,255,0.06); color: var(--accent-1); padding: 2px 6px; border-radius: 3px; font-size: 11px; font-family: var(--mono-font); }
    
    .clickable { cursor: pointer; border-bottom: 1px dotted rgba(255,255,255,0.4); padding-bottom: 2px; transition: all 0.2s; }
    .clickable:hover { color: var(--accent-1); border-bottom-color: var(--accent-1); }
    .rtm-table code.clickable { border-bottom: none; cursor: pointer; transition: all 0.2s; }
    .rtm-table code.clickable:hover { background: var(--accent-1); color: #000; }
  </style>

  <table class="rtm-table">
    <thead>
      <tr><th>Req ID</th><th>Descripción</th><th>Test Case(s)</th><th>Status</th></tr>
    </thead>
    <tbody>
      <tr>
        <td><code>REQ-01</code></td>
        <td><span class="clickable" onclick="showDetail('REQ-01')">Login con credenciales válidas</span></td>
        <td><code class="clickable" onclick="showDetail('TC-001')">TC-001</code></td>
        <td><span class="badge badge-pass">PASS</span></td>
      </tr>
      <tr>
        <td><code>REQ-02</code></td>
        <td><span class="clickable" onclick="showDetail('REQ-02')">Suscripción Newsletter</span></td>
        <td><code class="clickable" onclick="showDetail('TC-002')">TC-002</code></td>
        <td><span class="badge badge-pend">PENDIENTE</span></td>
      </tr>
    </tbody>
  </table>
  
  <!-- Modal Interactivo e Inyección JS (Solo incluir si hay interactividad clickeable) -->
  <div id="detailModal" style="display:none; position:absolute; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.8); backdrop-filter:blur(5px); z-index:100; align-items:center; justify-content:center;">
    <div style="background:var(--bg-secondary); border:1px solid var(--accent-3); border-radius:12px; padding:24px; width:550px; color:#fff; position:relative; box-shadow:0 20px 40px rgba(0,0,0,0.6);">
      <button onclick="document.getElementById('detailModal').style.display='none'" style="position:absolute; top:16px; right:16px; background:transparent; border:none; color:var(--text-secondary); font-size:18px; cursor:pointer;">&times;</button>
      <h3 id="modalTitle" style="color:var(--accent-3); margin-bottom:12px; font-family:var(--display-font); font-size:18px;"></h3>
      <pre id="modalContent" style="white-space:pre-wrap; font-family:var(--mono-font); font-size:13px; color:var(--text-primary); background:var(--bg-primary); padding:16px; border-radius:6px; border:1px solid rgba(255,255,255,0.1); line-height:1.6;"></pre>
    </div>
  </div>

  <script>
    const details = {
      'REQ-01': { title: 'Requerimiento: REQ-01', content: 'COMO usuario registrado\nQUIERO iniciar sesión con mis credenciales\nPARA acceder a mi panel personal.' },
      'TC-001': { title: 'Test Case: TC-001', content: 'Feature: Login\n\n  Scenario: Login exitoso\n    Given estoy en la página de login\n    When ingreso "admin" y "1234"\n    Then veo mi panel personal' },
      'REQ-02': { title: 'Requerimiento: REQ-02', content: 'COMO visitante\nQUIERO suscribirme al boletín\nPARA recibir noticias.' },
      'TC-002': { title: 'Test Case: TC-002', content: 'Feature: Suscripción\n\n  Scenario: Correo válido\n    Given ingreso "test@correo.com"\n    Then veo mensaje de éxito' }
    };
    function showDetail(id) {
      if(details[id]) {
        document.getElementById('modalTitle').innerText = details[id].title;
        document.getElementById('modalContent').innerText = details[id].content;
        document.getElementById('detailModal').style.display = 'flex';
      }
    }
  </script>

</div>
```

## Modificadores / Consejos
1. **Badges**: Este bloque asume que has utilizado la decoración `W12` en `decoration_hints` para que los estilos `.badge` funcionen.
2. **Escala**: Mantén la tabla con pocas columnas (máx 4-5) y pocas filas (máx 5) para no romper el layout.
3. **Diccionario JS**: El script en línea y el modal DEBEN generarse íntegramente dentro del `html_content` de esa diapositiva en particular.
