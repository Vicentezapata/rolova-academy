#!/usr/bin/env python3
"""
build_evaluacion_u2.py — Genera evaluacion_U2.html
Evaluación Interactiva para la Unidad 2 de Desarrollo de Software Web I
Caso de estudio: Tech Solutions - Autenticación, JWT y Persistencia
"""
import os

DIR = r"c:\Users\vicen\OneDrive\Escritorio\EVA IPSS\DESARROLLO DE SOFTWARE WEB I\UNIDAD 2"
OUT = os.path.join(DIR, 'evaluacion_U2.html')

CSS = """
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{
  --p:#6C3BFF;--p-glow:rgba(108,59,255,.35);
  --c2:#9D6BFF;--c3:#C4A7FF;
  --bg:#080B18;--bg2:#0D1128;--bg3:#131830;
  --surface:rgba(255,255,255,.04);--surface-h:rgba(255,255,255,.08);
  --border:rgba(255,255,255,.07);--border-h:rgba(255,255,255,.14);
  --text:#E8ECF4;--text2:#94A3B8;--text3:#64748B;
  --radius:16px;--radius-sm:10px;
  --font:'Inter',system-ui,sans-serif;
  --mono:'JetBrains Mono',monospace;
  font-size:16px;
}
html{scroll-behavior:smooth}
body{font-family:var(--font);background:var(--bg);color:var(--text);line-height:1.7;overflow-x:hidden;-webkit-font-smoothing:antialiased}
::selection{background:var(--p);color:#fff}
::-webkit-scrollbar{width:8px}::-webkit-scrollbar-track{background:var(--bg)}::-webkit-scrollbar-thumb{background:var(--border);border-radius:4px}
a{color:var(--c2);text-decoration:none}
.gradient-text{background:linear-gradient(135deg,var(--p),var(--c2),var(--c3));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.container{max-width:1200px;margin:0 auto;padding:0 2rem}
.badge{display:inline-block;padding:.35rem .85rem;border-radius:50px;font-family:var(--mono);font-size:.75rem;font-weight:600;background:rgba(196,167,255,.1);color:var(--c3);border:1px solid rgba(196,167,255,.2)}

/* Nav */
.nav{padding:1.5rem 0;border-bottom:1px solid var(--border);background:var(--bg2)}
.nav .container{display:flex;align-items:center;justify-content:space-between}
.nav-logo{font-weight:800;font-size:1.1rem;display:flex;align-items:center;gap:.5rem}
.nav-logo .dot{width:8px;height:8px;background:var(--c3);border-radius:50%;box-shadow:0 0 10px rgba(196,167,255,.5)}
.btn-back{font-size:.9rem;color:var(--text2);display:flex;align-items:center;gap:.4rem;padding:.5rem 1rem;background:var(--surface);border-radius:50px;border:1px solid var(--border);transition:all .3s}
.btn-back:hover{background:var(--surface-h);color:var(--text)}

/* Hero */
.hero{padding:4rem 0;text-align:center;border-bottom:1px solid var(--border)}
.hero h1{font-size:clamp(2rem,5vw,3.5rem);font-weight:900;line-height:1.1;margin:1rem 0;letter-spacing:-.02em}
.hero p{font-size:1.1rem;color:var(--text2);max-width:700px;margin:0 auto}

/* Layout */
.layout{display:grid;grid-template-columns:1fr 420px;gap:2rem;margin:3rem 0}
.card{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:2rem}
.card-title{font-size:1.25rem;font-weight:800;display:flex;align-items:center;gap:.5rem;margin-bottom:1.5rem;padding-bottom:1rem;border-bottom:1px solid var(--border)}
.card-title svg{width:22px;height:22px;color:var(--p)}

/* Requirements List */
.req-group{margin-bottom:2.5rem}
.req-group h4{font-size:1rem;font-weight:700;color:var(--c3);margin-bottom:1rem;display:flex;align-items:center;gap:.5rem}
.req-list{list-style:none;display:flex;flex-direction:column;gap:.75rem}
.req-item{display:flex;align-items:flex-start;gap:.75rem;padding:1rem;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-sm);cursor:pointer;transition:all .2s;user-select:none}
.req-item:hover{background:var(--surface-h)}
.req-item.done{border-color:rgba(80,250,123,.3);background:rgba(80,250,123,.03)}
.req-item.done .req-checkbox{background:#50FA7B;border-color:#50FA7B}
.req-item.done .req-checkbox svg{opacity:1;stroke-dashoffset:0}
.req-item.done .req-text{text-decoration:line-through;opacity:.6}
.req-checkbox{width:22px;height:22px;border:2px solid var(--text3);border-radius:6px;display:flex;align-items:center;justify-content:center;transition:all .3s;flex-shrink:0;margin-top:2px}
.req-checkbox svg{width:14px;height:14px;color:#080B18;opacity:0;transition:all .3s;stroke-dasharray:16;stroke-dashoffset:16}
.req-text{font-size:.9rem;color:var(--text2)}
.req-text strong{color:var(--text);display:block;margin-bottom:2px}

/* Code Snippet */
.snippet{background:#05070f;padding:1rem;border-radius:var(--radius-sm);font-family:var(--mono);font-size:.8rem;color:#B0C4D8;margin-top:1rem;border:1px solid rgba(108,59,255,.15)}

/* Rubric Simulator */
.rubric-card{position:sticky;top:6.5rem}
.rubric-score{text-align:center;margin-bottom:2rem}
.score-circle{width:130px;height:130px;border-radius:50%;background:var(--surface);border:4px solid var(--border);margin:0 auto 1rem;display:flex;flex-direction:column;align-items:center;justify-content:center;transition:all .3s}
.score-circle.pass{border-color:#50FA7B;box-shadow:0 0 20px rgba(80,250,123,.2)}
.score-circle.fail{border-color:#FF5555;box-shadow:0 0 20px rgba(255,85,85,.1)}
.score-val{font-size:2.8rem;font-weight:900;font-family:var(--mono);line-height:1}
.score-max{font-size:.8rem;color:var(--text3);margin-top:0.25rem}
.score-msg{font-size:.9rem;font-weight:600;min-height:1.5rem}

.r-crit{margin-bottom:1.75rem}
.r-crit-title{font-size:.85rem;font-weight:700;margin-bottom:.5rem;display:flex;justify-content:space-between;align-items:center}
.r-crit-title span{color:var(--c2)}
.r-options{display:grid;grid-template-columns:repeat(4, 1fr);gap:.4rem}
.r-opt{padding:.5rem;background:var(--surface);border:1px solid var(--border);border-radius:6px;text-align:center;font-size:.72rem;cursor:pointer;transition:all .2s;color:var(--text2);font-weight:500}
.r-opt:hover{background:var(--surface-h)}
.r-opt.selected{background:rgba(108,59,255,.15);border-color:var(--p);color:var(--c3);font-weight:700}

/* Info Box */
.info-box{padding:1.25rem;background:rgba(108,59,255,.04);border:1px solid rgba(108,59,255,.15);border-radius:var(--radius-sm);margin-top:2rem;font-size:.85rem;color:var(--text2)}
.info-box strong{color:var(--c3);display:block;margin-bottom:.5rem}

@media(max-width:960px){
  .layout{grid-template-columns:1fr}
  .rubric-card{position:static}
}
"""

HTML = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Evaluación Unidad 2 - Tech Solutions Fase 2</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
<style>{CSS}</style>
</head>
<body>

<nav class="nav">
  <div class="container">
    <div class="nav-logo"><div class="dot"></div> DS Web I</div>
    <a href="portal_unidad2.html" class="btn-back"><i data-lucide="arrow-left"></i> Volver al Portal de Unidad 2</a>
  </div>
</nav>

<section class="hero">
  <div class="container">
    <span class="badge">Evaluación Sumativa Unidad 2</span>
    <h1>Proyecto: <span class="gradient-text">Tech Solutions (Fase II)</span></h1>
    <p>Conectaremos la aplicación a base de datos utilizando Eloquent ORM. Implementarás autenticación de usuarios, encriptación de claves, generación de JWT y un Middleware de seguridad para proteger las rutas.</p>
  </div>
</section>

<div class="container layout">
  
  <!-- LEFT: Requirements -->
  <div class="main-content">
    <div class="card">
      <h2 class="card-title"><i data-lucide="list-checks"></i> Requerimientos del Proyecto</h2>
      
      <!-- 1. Configuración de Base de Datos y Modelos -->
      <div class="req-group">
        <h4><i data-lucide="database"></i> 1. Configuración de Base de Datos y Modelos</h4>
        <div class="req-list">
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text">
              <strong>Variables de Entorno (.env)</strong>
              Configurar la conexión a MySQL usando:
              <div class="snippet">DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=desarrollo_software_1
DB_USERNAME=root
DB_PASSWORD=desarrollo_software_1</div>
            </div>
          </div>
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text">
              <strong>Modelo Usuario (User)</strong>
              Implementar el modelo con los atributos: id, nombre, correo (identificador único) y clave. Debe usar asignación masiva de forma segura.
            </div>
          </div>
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text">
              <strong>Modelo Proyecto (Actualizado)</strong>
              Actualizar el modelo Proyecto para incluir el campo de clave foránea <code>created_by</code> apuntando al ID del Usuario que creó el proyecto.
            </div>
          </div>
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text">
              <strong>Migraciones</strong>
              Crear las migraciones de base de datos respectivas con las restricciones de clave foránea adecuadas (e.g. <code>$table->foreignId('created_by')->constrained('usuarios')</code>).
            </div>
          </div>
        </div>
      </div>
      
      <!-- 2. Rutas y Controladores de Autenticación -->
      <div class="req-group">
        <h4><i data-lucide="key-round"></i> 2. Rutas y Controladores de Autenticación</h4>
        <div class="req-list">
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text">
              <strong>Rutas de API de Autenticación</strong>
              Definir las rutas para: Registro de Usuario (POST <code>/api/register</code>) e Inicio de Sesión (POST <code>/api/login</code>).
            </div>
          </div>
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text">
              <strong>Registro de Usuario (Cifrado de Clave)</strong>
              La función del AuthController para registrar usuarios debe encriptar/cifrar la clave del usuario (usando <code>bcrypt()</code> o <code>Hash::make()</code>) antes de guardarla en la base de datos.
            </div>
          </div>
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text">
              <strong>Inicio de Sesión (Retorno de JWT)</strong>
              La función de login del AuthController debe validar las credenciales del usuario y retornar un Token JWT válido (puedes simular la firma del JWT o integrar una librería como firebase/php-jwt o tymon/jwt-auth).
            </div>
          </div>
        </div>
      </div>

      <!-- 3. Middleware de Seguridad -->
      <div class="req-group">
        <h4><i data-lucide="shield-check"></i> 3. Middleware de Seguridad</h4>
        <div class="req-list">
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text">
              <strong>Crear JWT Middleware</strong>
              Generar un middleware que valide el JWT en las solicitudes entrantes (leyendo el header Authorization <code>Bearer token</code>). Si es inválido, rechazar con código de estado HTTP 401.
            </div>
          </div>
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text">
              <strong>Proteger Rutas de Proyectos</strong>
              Asociar el Middleware creado a las rutas del CRUD de Proyectos para que solo usuarios con token válido puedan ver o manipular proyectos.
            </div>
          </div>
        </div>
      </div>

      <!-- 4. Vistas Blade -->
      <div class="req-group">
        <h4><i data-lucide="layout"></i> 4. Vistas Blade (Interfaz)</h4>
        <div class="req-list">
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text">
              <strong>Vista de Inicio de Sesión</strong>
              Formulario Blade con campos Correo y Clave. Debe enviar datos vía POST e incluir la directiva <code>@csrf</code>.
            </div>
          </div>
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text">
              <strong>Vista de Registro</strong>
              Formulario Blade con campos Nombre, Correo y Clave. Con directiva <code>@csrf</code> y renderización de errores de validación mediante <code>@error</code>.
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
  
  <!-- RIGHT: Rubric Simulator -->
  <div class="sidebar">
    <div class="card rubric-card">
      <div class="rubric-score">
        <div class="score-circle fail" id="scoreCircle">
          <span class="score-val" id="scoreVal">0</span>
          <span class="score-max">/ 100 pts</span>
        </div>
        <div class="score-msg" id="scoreMsg">Reprobado (Menos del 60%)</div>
      </div>
      
      <!-- Criterio 1: Conexión BD y Modelos -->
      <div class="r-crit">
        <div class="r-crit-title">Conexión BD y Modelos <span id="crit1-score">0 pts</span></div>
        <div class="r-options">
          <div class="r-opt selected" onclick="selectCrit(1, 0, 'Bajo')">B (0)</div>
          <div class="r-opt" onclick="selectCrit(1, 22, 'Medio')">M (22)</div>
          <div class="r-opt" onclick="selectCrit(1, 27, 'Alto')">A (27)</div>
          <div class="r-opt" onclick="selectCrit(1, 33, 'Sobresaliente')">S (33)</div>
        </div>
      </div>

      <!-- Criterio 2: Autenticación y JWT Middleware -->
      <div class="r-crit">
        <div class="r-crit-title">Autenticación y Middleware <span id="crit2-score">0 pts</span></div>
        <div class="r-options">
          <div class="r-opt selected" onclick="selectCrit(2, 0, 'Bajo')">B (0)</div>
          <div class="r-opt" onclick="selectCrit(2, 23, 'Medio')">M (23)</div>
          <div class="r-opt" onclick="selectCrit(2, 28, 'Alto')">A (28)</div>
          <div class="r-opt" onclick="selectCrit(2, 34, 'Sobresaliente')">S (34)</div>
        </div>
      </div>

      <!-- Criterio 3: Registro y Cifrado -->
      <div class="r-crit">
        <div class="r-crit-title">Registro y Cifrado <span id="crit3-score">0 pts</span></div>
        <div class="r-options">
          <div class="r-opt selected" onclick="selectCrit(3, 0, 'Bajo')">B (0)</div>
          <div class="r-opt" onclick="selectCrit(3, 22, 'Medio')">M (22)</div>
          <div class="r-opt" onclick="selectCrit(3, 27, 'Alto')">A (27)</div>
          <div class="r-opt" onclick="selectCrit(3, 33, 'Sobresaliente')">S (33)</div>
        </div>
      </div>
      
      <div class="info-box">
        <strong>Nota Importante</strong>
        La escala exige un 60% de logro para la aprobación (nota 4.0), equivalente a <strong>60 puntos</strong> en el simulador.
      </div>
    </div>
  </div>

</div>

<footer>
  <div class="container">
    &copy; 2026 Instituto Profesional San Sebastián. Tecnología Educativa.
  </div>
</footer>

<script>
let scores = [0, 0, 0];

function selectCrit(critIdx, value, level) {{
  // Update score array
  scores[critIdx - 1] = value;
  
  // Update visual selection
  const group = document.querySelectorAll('.r-crit')[critIdx - 1];
  const options = group.querySelectorAll('.r-opt');
  options.forEach(opt => opt.classList.remove('selected'));
  
  // Find which option matches value
  let index = 0;
  if (critIdx === 1) {{
    if (value === 22) index = 1;
    if (value === 27) index = 2;
    if (value === 33) index = 3;
  }} else if (critIdx === 2) {{
    if (value === 23) index = 1;
    if (value === 28) index = 2;
    if (value === 34) index = 3;
  }} else if (critIdx === 3) {{
    if (value === 22) index = 1;
    if (value === 27) index = 2;
    if (value === 33) index = 3;
  }}
  options[index].classList.add('selected');
  
  // Update label
  document.getElementById('crit' + critIdx + '-score').textContent = value + ' pts';
  
  calculateTotal();
}}

function calculateTotal() {{
  const total = scores[0] + scores[1] + scores[2];
  document.getElementById('scoreVal').textContent = total;
  
  const circle = document.getElementById('scoreCircle');
  const msg = document.getElementById('scoreMsg');
  
  if (total >= 60) {{
    circle.className = 'score-circle pass';
    msg.textContent = 'Aprobado (' + getNota(total) + ')';
    msg.style.color = '#50FA7B';
  }} else {{
    circle.className = 'score-circle fail';
    msg.textContent = 'Reprobado (' + getNota(total) + ')';
    msg.style.color = '#FF5555';
  }}
}}

function getNota(pts) {{
  if (pts < 60) {{
    return (1.0 + (pts * 0.05)).toFixed(1);
  }} else {{
    return (4.0 + ((pts - 60) * 0.075)).toFixed(1);
  }}
}}

function toggleReq(el) {{
  el.classList.toggle('done');
}}

lucide.createIcons();
</script>
</body>
</html>
"""

with open(OUT, 'w', encoding='utf-8') as f:
    f.write(HTML)

print(f"[OK] Generado: {OUT}")
