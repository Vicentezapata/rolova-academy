#!/usr/bin/env python3
"""
build_evaluacion_u1.py — Genera evaluacion_U1.html
Evaluación Interactiva para la Unidad 1 de Desarrollo de Software Web I
Caso de estudio: Tech Solutions
"""
import os

DIR = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(DIR, 'evaluacion_U1.html')

CSS = """
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{
  --p:#FF4500;--p-glow:rgba(255,69,0,.35);
  --c2:#FF7A33;--c3:#FFB347;
  --bg:#0A0E1A;--bg2:#0F1629;--bg3:#161D33;
  --surface:rgba(255,255,255,.04);--surface-h:rgba(255,255,255,.08);
  --border:rgba(255,255,255,.06);--border-h:rgba(255,255,255,.12);
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
a{color:var(--p);text-decoration:none}
.gradient-text{background:linear-gradient(135deg,var(--p),var(--c2),var(--c3));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.container{max-width:1200px;margin:0 auto;padding:0 2rem}
.badge{display:inline-block;padding:.35rem .85rem;border-radius:50px;font-family:var(--mono);font-size:.75rem;font-weight:600;background:rgba(255,179,71,.1);color:var(--c3);border:1px solid rgba(255,179,71,.2)}

/* Nav */
.nav{padding:1.5rem 0;border-bottom:1px solid var(--border);background:var(--bg2)}
.nav .container{display:flex;align-items:center;justify-content:space-between}
.nav-logo{font-weight:800;font-size:1.1rem;display:flex;align-items:center;gap:.5rem}
.nav-logo .dot{width:8px;height:8px;background:var(--c3);border-radius:50%;box-shadow:0 0 10px rgba(255,179,71,.5)}
.btn-back{font-size:.9rem;color:var(--text2);display:flex;align-items:center;gap:.4rem;padding:.5rem 1rem;background:var(--surface);border-radius:50px;border:1px solid var(--border);transition:all .3s}
.btn-back:hover{background:var(--surface-h);color:var(--text)}

/* Hero */
.hero{padding:4rem 0;text-align:center;border-bottom:1px solid var(--border)}
.hero h1{font-size:clamp(2rem,5vw,3.5rem);font-weight:900;line-height:1.1;margin:1rem 0;letter-spacing:-.02em}
.hero p{font-size:1.1rem;color:var(--text2);max-width:700px;margin:0 auto}

/* Layout */
.layout{display:grid;grid-template-columns:1fr 400px;gap:2rem;margin:3rem 0}
.card{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);padding:2rem}
.card-title{font-size:1.25rem;font-weight:800;display:flex;align-items:center;gap:.5rem;margin-bottom:1.5rem;padding-bottom:1rem;border-bottom:1px solid var(--border)}
.card-title svg{width:22px;height:22px;color:var(--p)}

/* Requirements List */
.req-group{margin-bottom:2rem}
.req-group h4{font-size:1rem;font-weight:700;color:var(--c3);margin-bottom:1rem;display:flex;align-items:center;gap:.5rem}
.req-list{list-style:none;display:flex;flex-direction:column;gap:.75rem}
.req-item{display:flex;align-items:flex-start;gap:.75rem;padding:1rem;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-sm);cursor:pointer;transition:all .2s;user-select:none}
.req-item:hover{background:var(--surface-h)}
.req-item.done{border-color:rgba(76,175,80,.4);background:rgba(76,175,80,.05)}
.req-item.done .req-checkbox{background:#4CAF50;border-color:#4CAF50}
.req-item.done .req-checkbox svg{opacity:1;stroke-dashoffset:0}
.req-item.done .req-text{text-decoration:line-through;opacity:.6}
.req-checkbox{width:22px;height:22px;border:2px solid var(--text3);border-radius:6px;display:flex;align-items:center;justify-content:center;transition:all .3s;flex-shrink:0;margin-top:2px}
.req-checkbox svg{width:14px;height:14px;color:#fff;opacity:0;transition:all .3s;stroke-dasharray:16;stroke-dashoffset:16}
.req-text{font-size:.9rem;color:var(--text2)}
.req-text strong{color:var(--text);display:block;margin-bottom:2px}

/* Code Snippet */
.snippet{background:#111;padding:1rem;border-radius:var(--radius-sm);font-family:var(--mono);font-size:.8rem;color:#A9B7C6;margin-top:1rem;border:1px solid #333}

/* Rubric Simulator */
.rubric-card{position:sticky;top:2rem}
.rubric-score{text-align:center;margin-bottom:2rem}
.score-circle{width:120px;height:120px;border-radius:50%;background:var(--surface);border:4px solid var(--border);margin:0 auto 1rem;display:flex;flex-direction:column;align-items:center;justify-content:center;transition:border-color .3s}
.score-circle.pass{border-color:#4CAF50;box-shadow:0 0 20px rgba(76,175,80,.2)}
.score-circle.fail{border-color:#FF5252}
.score-val{font-size:2.5rem;font-weight:900;font-family:var(--mono);line-height:1}
.score-max{font-size:.8rem;color:var(--text3)}
.score-msg{font-size:.9rem;font-weight:600;min-height:1.5rem}

.r-crit{margin-bottom:1.5rem}
.r-crit-title{font-size:.9rem;font-weight:700;margin-bottom:.5rem;display:flex;justify-content:space-between}
.r-crit-title span{color:var(--c2)}
.r-options{display:grid;grid-template-columns:repeat(4, 1fr);gap:.4rem}
.r-opt{padding:.5rem;background:var(--surface);border:1px solid var(--border);border-radius:6px;text-align:center;font-size:.75rem;cursor:pointer;transition:all .2s;color:var(--text2)}
.r-opt:hover{background:var(--surface-h)}
.r-opt.selected{background:rgba(255,69,0,.15);border-color:var(--p);color:var(--p);font-weight:700}

/* Info Box */
.info-box{padding:1.25rem;background:rgba(255,179,71,.05);border:1px solid rgba(255,179,71,.2);border-radius:var(--radius-sm);margin-top:2rem;font-size:.85rem;color:var(--text2)}
.info-box strong{color:var(--c3);display:block;margin-bottom:.5rem}

@media(max-width:900px){
  .layout{grid-template-columns:1fr}
  .rubric-card{position:static}
}
"""

HTML = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Evaluación Unidad 1 - Tech Solutions</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;700&display=swap" rel="stylesheet">
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
<style>{css}</style>
</head>
<body>

<nav class="nav">
  <div class="container">
    <div class="nav-logo"><div class="dot"></div> DS Web I</div>
    <a href="portal_unidad1.html" class="btn-back"><i data-lucide="arrow-left"></i> Volver al Portal</a>
  </div>
</nav>

<section class="hero">
  <div class="container">
    <span class="badge">Evaluación 1 (10%)</span>
    <h1>Proyecto: <span class="gradient-text">Tech Solutions</span></h1>
    <p>La empresa Tech Solutions necesita modernizar su sistema de gestión de proyectos utilizando Laravel. Deberás construir la estructura base (Rutas, Controladores, Vistas y Modelo) requerida por el equipo de desarrollo.</p>
  </div>
</section>

<div class="container layout">
  
  <!-- LEFT: Requirements -->
  <div class="main-content">
    <div class="card">
      <h2 class="card-title"><i data-lucide="list-checks"></i> Requerimientos de la Entrega</h2>
      
      <!-- 1. Rutas -->
      <div class="req-group">
        <h4><i data-lucide="route"></i> 1. Definición de Rutas</h4>
        <div class="req-list">
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text"><strong>Ruta: Listar Proyectos</strong>GET /proyectos</div>
          </div>
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text"><strong>Ruta: Agregar Proyecto</strong>POST /proyectos</div>
          </div>
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text"><strong>Ruta: Actualizar Proyecto</strong>PUT /proyectos/{id}</div>
          </div>
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text"><strong>Ruta: Eliminar Proyecto</strong>DELETE /proyectos/{id}</div>
          </div>
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text"><strong>Ruta: Obtener Proyecto por ID</strong>GET /proyectos/{id}</div>
          </div>
        </div>
      </div>
      
      <!-- 2. Controladores -->
      <div class="req-group">
        <h4><i data-lucide="cpu"></i> 2. Controladores (ProjectController)</h4>
        <div class="req-list">
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text"><strong>5 Métodos implementados</strong>index(), store(), show(), update(), destroy() conectados a sus rutas respectivas.</div>
          </div>
        </div>
      </div>

      <!-- 3. Modelo -->
      <div class="req-group">
        <h4><i data-lucide="database"></i> 3. Modelo Estático</h4>
        <div class="req-list">
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text"><strong>Modelo Proyecto</strong>Debe manejar estructura simulada con: Id, Nombre, Fecha de Inicio, Estado, Responsable y Monto.</div>
          </div>
        </div>
      </div>

      <!-- 4. Vistas -->
      <div class="req-group">
        <h4><i data-lucide="layout"></i> 4. Vistas Blade</h4>
        <div class="req-list">
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text"><strong>5 Vistas creadas</strong>Estilos básicos para mostrar la información retornada por los controladores correspondientes.</div>
          </div>
        </div>
      </div>

      <!-- 5. Componente API -->
      <div class="req-group">
        <h4><i data-lucide="plug"></i> 5. Consumo de API (Componente)</h4>
        <div class="req-list">
          <div class="req-item" onclick="toggleReq(this)">
            <div class="req-checkbox"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3"><path d="M20 6L9 17l-5-5"/></svg></div>
            <div class="req-text"><strong>Servicio Externo UF</strong>Componente reutilizable que extrae el valor de la UF del día (usar mindicador.cl u otro similar).</div>
          </div>
        </div>
        
        <div class="snippet">
// Tip del Profesor: Puedes usar Http facade
use Illuminate\\Support\\Facades\\Http;

$response = Http::get('https://mindicador.cl/api/uf');
$uf = $response->json()['serie'][0]['valor'];
        </div>
      </div>

    </div>
  </div>

  <!-- RIGHT: Rubric -->
  <div>
    <div class="card rubric-card">
      <h2 class="card-title"><i data-lucide="calculator"></i> Simulador de Rúbrica</h2>
      
      <div class="rubric-score">
        <div class="score-circle" id="scoreCircle">
          <span class="score-val" id="scoreVal">0</span>
          <span class="score-max">/ 100</span>
        </div>
        <div class="score-msg" id="scoreMsg">Selecciona tus logros</div>
      </div>

      <!-- Criteria -->
      <div id="criteria"></div>

      <div class="info-box">
        <strong><i data-lucide="info"></i> Formato de Entrega</strong>
        Documento Word o PDF (máx 4 pág, Arial 12) + Archivo comprimido con el proyecto. Nombrar como: EVU1_APELLIDO_NOMBRE.
      </div>
    </div>
  </div>

</div>

<script>
lucide.createIcons();

function toggleReq(el) {
  el.classList.toggle('done');
}

// Rubric Logic
const rubrics = [
  { id: 'c1', title: '1. Rutas (18pts)', options: [{l:'Bajo',v:0}, {l:'Medio',v:10}, {l:'Alto',v:14}, {l:'Sobresaliente',v:18}] },
  { id: 'c2', title: '2. Arquitectura (18pts)', options: [{l:'Bajo',v:0}, {l:'Medio',v:8}, {l:'Alto',v:10}, {l:'Sobresaliente',v:18}] },
  { id: 'c3', title: '3. Patrones & Conexión (14pts)', options: [{l:'Bajo',v:0}, {l:'Medio',v:10}, {l:'Alto',v:12}, {l:'Sobresaliente',v:14}] },
  { id: 'c4', title: '4. Componente UF (14pts)', options: [{l:'Bajo',v:0}, {l:'Medio',v:10}, {l:'Alto',v:12}, {l:'Sobresaliente',v:14}] },
  { id: 'c5', title: '5. Vistas UI (18pts)', options: [{l:'Bajo',v:0}, {l:'Medio',v:12}, {l:'Alto',v:16}, {l:'Sobresaliente',v:18}] },
  { id: 'c6', title: '6. Servicios (18pts)', options: [{l:'Bajo',v:0}, {l:'Medio',v:12}, {l:'Alto',v:16}, {l:'Sobresaliente',v:18}] }
];

let selections = {c1:0, c2:0, c3:0, c4:0, c5:0, c6:0};

const critContainer = document.getElementById('criteria');

rubrics.forEach(r => {
  let html = `<div class="r-crit"><div class="r-crit-title">${r.title} <span id="v_${r.id}">0</span></div><div class="r-options">`;
  r.options.forEach((o, i) => {
    html += `<div class="r-opt" onclick="setScore('${r.id}', ${o.v}, this)">${o.l}</div>`;
  });
  html += `</div></div>`;
  critContainer.innerHTML += html;
});

function setScore(id, val, el) {
  // Update UI selection
  const siblings = el.parentElement.children;
  for(let i=0; i<siblings.length; i++) siblings[i].classList.remove('selected');
  el.classList.add('selected');
  
  // Update Score
  selections[id] = val;
  document.getElementById('v_' + id).innerText = val;
  
  calculateTotal();
}

function calculateTotal() {
  let total = Object.values(selections).reduce((a,b) => a+b, 0);
  const circ = document.getElementById('scoreCircle');
  const msg = document.getElementById('scoreMsg');
  
  document.getElementById('scoreVal').innerText = total;
  
  circ.classList.remove('pass', 'fail');
  if(total === 0) {
    msg.innerText = "Selecciona tus logros";
    msg.style.color = "var(--text)";
  } else if(total >= 60) {
    circ.classList.add('pass');
    msg.innerText = "¡Aprobado! (Nota >= 4.0)";
    msg.style.color = "#4CAF50";
  } else {
    circ.classList.add('fail');
    msg.innerText = "Reprobado (Nota < 4.0)";
    msg.style.color = "#FF5252";
  }
}
</script>
</body>
</html>
"""
def main():
    html_content = HTML.replace('{css}', CSS)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f'\\u2705 Evaluacion U1 generada: {OUT}')

if __name__ == '__main__':
    main()
