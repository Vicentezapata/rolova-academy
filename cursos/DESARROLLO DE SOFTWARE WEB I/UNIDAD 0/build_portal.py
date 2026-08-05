#!/usr/bin/env python3
"""
build_portal.py — Genera portal_unidad0.html
Desarrollo de Software Web I | Unidad 0: Bienvenida
Instituto Profesional San Sebastián | 2° Trimestre 2026
"""
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT = os.path.join(SCRIPT_DIR, 'portal_unidad0.html')

HTML = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Desarrollo de Software Web I — Portal de Bienvenida</title>
<meta name="description" content="Portal interactivo de la asignatura Desarrollo de Software Web I - Laravel, MVC, CRUD - IPSS 2026">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
<style>
/* ============================================
   RESET & DESIGN TOKENS
   ============================================ */
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{
  --p:#FF4500;--p-glow:rgba(255,69,0,.35);
  --c2:#FF7A33;--c3:#FFB347;--c4:#FFCF70;
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
::-webkit-scrollbar{width:7px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--border);border-radius:4px}
::-webkit-scrollbar-thumb:hover{background:var(--p)}
img{max-width:100%;display:block}
a{color:inherit;text-decoration:none}

/* ============================================
   LAYOUT
   ============================================ */
.container{max-width:1200px;margin:0 auto;padding:0 2rem}
.section{padding:5.5rem 0;position:relative}
.section-label{
  font-family:var(--mono);font-size:.72rem;font-weight:600;
  text-transform:uppercase;letter-spacing:3px;color:var(--p);
  margin-bottom:.75rem;display:flex;align-items:center;gap:.5rem;
}
.section-label::before{content:'';width:24px;height:2px;background:var(--p);border-radius:1px}
.section-title{font-size:clamp(1.75rem,3vw,2.5rem);font-weight:800;line-height:1.2;margin-bottom:.75rem;letter-spacing:-.02em}
.section-sub{font-size:1.05rem;color:var(--text2);max-width:600px;margin-bottom:3rem}
.gradient-text{background:linear-gradient(135deg,var(--p),var(--c2),var(--c3));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}

/* ============================================
   GLASS CARD
   ============================================ */
.glass{
  background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
  padding:1.75rem;transition:all .35s ease;position:relative;overflow:hidden;
}
.glass::before{
  content:'';position:absolute;top:0;left:0;right:0;height:1px;
  background:linear-gradient(90deg,transparent,var(--p),transparent);opacity:0;transition:opacity .35s;
}
.glass:hover{background:var(--surface-h);border-color:var(--border-h);transform:translateY(-3px)}
.glass:hover::before{opacity:1}

/* ============================================
   NAVBAR
   ============================================ */
.navbar{
  position:fixed;top:0;left:0;right:0;z-index:1000;
  padding:1rem 2rem;display:flex;align-items:center;justify-content:space-between;transition:all .3s ease;
}
.navbar.scrolled{background:rgba(10,14,26,.88);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);padding:.7rem 2rem}
.nav-brand{display:flex;align-items:center;gap:.75rem;font-weight:700;font-size:1.1rem}
.nav-icon{
  width:36px;height:36px;background:linear-gradient(135deg,var(--p),var(--c2));border-radius:10px;
  display:flex;align-items:center;justify-content:center;
}
.nav-icon svg{width:18px;height:18px;color:#fff}
.nav-links{display:flex;gap:1.25rem;align-items:center}
.nav-links a{color:var(--text2);font-size:.84rem;font-weight:500;transition:color .3s;padding:.5rem 0}
.nav-links a:hover{color:var(--p)}

/* ============================================
   HERO
   ============================================ */
.hero{min-height:100vh;display:flex;align-items:center;position:relative;overflow:hidden;padding:6rem 0 4rem}
.hero-bg{position:absolute;inset:0;z-index:0;pointer-events:none}
.orb{position:absolute;border-radius:50%;filter:blur(90px);animation:float 10s ease-in-out infinite}
.orb-1{width:520px;height:520px;background:var(--p);top:-12%;right:-6%;opacity:.12}
.orb-2{width:420px;height:420px;background:var(--c3);bottom:-12%;left:-6%;opacity:.1;animation-delay:-4s}
.orb-3{width:280px;height:280px;background:var(--c2);top:45%;left:28%;opacity:.06;animation-delay:-7s}

.hero-inner{position:relative;z-index:1;display:grid;grid-template-columns:1.2fr 1fr;gap:4rem;align-items:center;width:100%;max-width:1200px;margin:0 auto;padding:0 2rem}
.hero-badge{
  display:inline-flex;align-items:center;gap:.5rem;
  background:var(--surface);border:1px solid var(--border);border-radius:50px;
  padding:.45rem 1rem;font-family:var(--mono);font-size:.72rem;color:var(--c3);margin-bottom:1.5rem;
}
.badge-dot{width:6px;height:6px;border-radius:50%;background:var(--p);animation:pulse 2s ease-in-out infinite}
.hero-title{font-size:clamp(2.5rem,5vw,4rem);font-weight:900;line-height:1.08;letter-spacing:-.03em;margin-bottom:1.25rem}
.hero-desc{font-size:1.12rem;color:var(--text2);line-height:1.7;margin-bottom:2rem;max-width:520px}
.hero-desc strong{color:var(--c2);font-weight:600}
.hero-stats{display:flex;gap:2.5rem;margin-bottom:2.5rem}
.h-stat-val{display:block;font-size:1.8rem;font-weight:800;color:var(--p);font-family:var(--mono)}
.h-stat-lbl{font-size:.75rem;color:var(--text3);text-transform:uppercase;letter-spacing:1.5px}
.hero-cta{
  display:inline-flex;align-items:center;gap:.75rem;
  background:linear-gradient(135deg,var(--p),var(--c2));color:#fff;
  padding:1rem 2rem;border-radius:12px;font-weight:600;font-size:.95rem;
  transition:all .3s ease;box-shadow:0 4px 20px var(--p-glow);
}
.hero-cta:hover{transform:translateY(-2px);box-shadow:0 8px 30px var(--p-glow)}
.hero-cta svg{width:18px;height:18px}

/* Hero code block */
.code-window{
  background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;
  box-shadow:0 25px 60px rgba(0,0,0,.5);
  transform:perspective(1200px) rotateY(-5deg) rotateX(2deg);transition:transform .6s ease;
}
.code-window:hover{transform:perspective(1200px) rotateY(0) rotateX(0)}
.code-header{display:flex;align-items:center;gap:.5rem;padding:.7rem 1rem;background:rgba(255,255,255,.025);border-bottom:1px solid var(--border)}
.dot{width:10px;height:10px;border-radius:50%}
.dot-r{background:#FF5F57}.dot-y{background:#FFBD2E}.dot-g{background:#28CA41}
.code-title{margin-left:.5rem;font-family:var(--mono);font-size:.68rem;color:var(--text3)}
.code-body{padding:1.2rem 1.4rem;font-family:var(--mono);font-size:.78rem;line-height:2;color:var(--text2)}
.code-body .kw{color:#C792EA}.code-body .fn{color:#82AAFF}.code-body .str{color:#C3E88D}
.code-body .cls{color:var(--c2)}.code-body .op{color:#89DDFF}.code-body .cmt{color:var(--text3);font-style:italic}
.code-body .ln{display:block;min-height:1.6em}

/* ============================================
   COMPETENCIA / OVERVIEW
   ============================================ */
.overview-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(240px,1fr));gap:1.25rem}
.ov-card{text-align:center;padding:2rem 1.5rem}
.ov-icon{
  width:52px;height:52px;border-radius:14px;margin:0 auto 1rem;
  display:flex;align-items:center;justify-content:center;
  background:linear-gradient(135deg,rgba(255,69,0,.15),rgba(255,122,51,.08));
  border:1px solid rgba(255,69,0,.15);
}
.ov-icon svg{width:24px;height:24px;color:var(--p)}
.ov-card h3{font-size:1rem;font-weight:700;margin-bottom:.5rem}
.ov-card p{font-size:.88rem;color:var(--text2);line-height:1.6}

/* ============================================
   ROADMAP
   ============================================ */
.roadmap{display:flex;gap:0;position:relative;padding:2rem 0}
.roadmap::before{
  content:'';position:absolute;top:38px;left:0;right:0;height:2px;
  background:linear-gradient(90deg,var(--p),var(--c2),var(--c3),var(--c4));border-radius:1px;
}
.rm-node{flex:1;text-align:center;position:relative;padding-top:3.5rem}
.rm-dot{
  position:absolute;top:26px;left:50%;transform:translateX(-50%);
  width:24px;height:24px;border-radius:50%;background:var(--bg);
  border:3px solid var(--p);z-index:2;transition:all .3s;
}
.rm-node:nth-child(2) .rm-dot{border-color:var(--c2)}
.rm-node:nth-child(3) .rm-dot{border-color:var(--c3)}
.rm-node:nth-child(4) .rm-dot{border-color:var(--c4)}
.rm-node:hover .rm-dot{background:var(--p);box-shadow:0 0 20px var(--p-glow)}
.rm-label{font-family:var(--mono);font-size:.65rem;color:var(--text3);text-transform:uppercase;letter-spacing:2px;margin-bottom:.35rem}
.rm-title{font-size:.95rem;font-weight:700;margin-bottom:.35rem}
.rm-desc{font-size:.8rem;color:var(--text2);line-height:1.5;max-width:180px;margin:0 auto}
.rm-weight{
  display:inline-block;margin-top:.5rem;font-family:var(--mono);font-size:.7rem;font-weight:700;
  color:var(--p);background:rgba(255,69,0,.1);padding:.2rem .6rem;border-radius:20px;
}

/* ============================================
   LARAVEL SECTION
   ============================================ */
.laravel-grid{display:grid;grid-template-columns:1fr 1fr;gap:1.5rem}
.lv-feature{display:flex;gap:1rem;align-items:flex-start;padding:1.5rem}
.lv-feature .ov-icon{margin:0;flex-shrink:0}
.lv-feature h3{font-size:.95rem;font-weight:700;margin-bottom:.3rem}
.lv-feature p{font-size:.84rem;color:var(--text2);line-height:1.55}
.lv-highlight{
  grid-column:1/-1;text-align:center;padding:2.5rem;
  background:linear-gradient(135deg,rgba(255,69,0,.06),rgba(255,179,71,.04));
  border:1px solid rgba(255,69,0,.12);
}
.lv-highlight .big-num{font-size:3rem;font-weight:900;font-family:var(--mono)}
.lv-highlight p{color:var(--text2);margin-top:.5rem;font-size:.9rem}

/* ============================================
   EVALUACIÓN
   ============================================ */
.eval-list{display:flex;flex-direction:column;gap:1.25rem;max-width:700px}
.eval-item{display:flex;align-items:center;gap:1.5rem;padding:1.25rem 1.5rem}
.eval-pct{font-family:var(--mono);font-size:1.5rem;font-weight:800;color:var(--p);min-width:60px;text-align:right}
.eval-info{flex:1}
.eval-info h4{font-size:.95rem;font-weight:700;margin-bottom:.35rem}
.eval-info p{font-size:.82rem;color:var(--text2)}
.eval-bar{height:6px;background:var(--surface);border-radius:3px;margin-top:.5rem;overflow:hidden}
.eval-bar-fill{height:100%;border-radius:3px;background:linear-gradient(90deg,var(--p),var(--c2));width:0;transition:width 1.2s ease}
.eval-note{
  margin-top:1.5rem;padding:1rem 1.5rem;border-radius:var(--radius-sm);
  background:rgba(255,179,71,.06);border:1px solid rgba(255,179,71,.12);
  font-size:.85rem;color:var(--c3);display:flex;align-items:center;gap:.75rem;
}
.eval-note svg{flex-shrink:0;width:18px;height:18px}

/* ============================================
   HERRAMIENTAS
   ============================================ */
.tools-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1.25rem}
.tool-card{text-align:center;padding:2rem 1.25rem}
.tool-card .ov-icon{width:56px;height:56px;border-radius:16px}
.tool-name{font-size:1rem;font-weight:700;margin-bottom:.25rem}
.tool-ver{font-family:var(--mono);font-size:.72rem;color:var(--c3);margin-bottom:.5rem}
.tool-desc{font-size:.82rem;color:var(--text2);line-height:1.5}

/* ============================================
   CALENDARIO
   ============================================ */
.cal-wrap{overflow-x:auto;border-radius:var(--radius);border:1px solid var(--border)}
.cal-table{width:100%;border-collapse:collapse;font-size:.84rem}
.cal-table thead{background:var(--bg3)}
.cal-table th{padding:.85rem 1rem;text-align:left;font-weight:600;font-size:.75rem;text-transform:uppercase;letter-spacing:1.5px;color:var(--text2);white-space:nowrap}
.cal-table td{padding:.8rem 1rem;border-top:1px solid var(--border);white-space:nowrap}
.cal-table tbody tr{transition:background .2s}
.cal-table tbody tr:hover{background:var(--surface-h)}
.cal-table .eval-row{background:rgba(255,69,0,.05)}
.cal-table .eval-row td{color:var(--c2);font-weight:600}
.cal-table .final-row{background:rgba(255,179,71,.06)}
.cal-table .final-row td{color:var(--c3);font-weight:700}
.badge-sync{
  display:inline-block;padding:.15rem .5rem;border-radius:20px;font-size:.7rem;font-weight:600;
  background:rgba(255,69,0,.12);color:var(--p);
}
.badge-async{
  display:inline-block;padding:.15rem .5rem;border-radius:20px;font-size:.7rem;font-weight:600;
  background:rgba(100,116,139,.15);color:var(--text3);
}

/* ============================================
   CTA
   ============================================ */
.cta-box{
  text-align:center;padding:4rem 2rem;border-radius:var(--radius);
  background:linear-gradient(135deg,rgba(255,69,0,.08),rgba(255,179,71,.04));
  border:1px solid rgba(255,69,0,.12);position:relative;overflow:hidden;
}
.cta-box::before{
  content:'';position:absolute;top:-50%;left:-50%;width:200%;height:200%;
  background:radial-gradient(circle,rgba(255,69,0,.05) 0%,transparent 70%);pointer-events:none;
}
.cta-box h2{font-size:clamp(1.5rem,3vw,2.2rem);font-weight:800;margin-bottom:.75rem}
.cta-box p{color:var(--text2);margin-bottom:2rem;font-size:1rem}

/* ============================================
   FOOTER
   ============================================ */
.footer{padding:2.5rem 0;border-top:1px solid var(--border);text-align:center}
.footer p{font-size:.8rem;color:var(--text3)}
.footer span{color:var(--p)}

/* ============================================
   ANIMATIONS
   ============================================ */
@keyframes float{0%,100%{transform:translateY(0)}50%{transform:translateY(-25px)}}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}
@keyframes fadeInUp{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}

.reveal{opacity:0;transform:translateY(28px);transition:opacity .65s ease,transform .65s ease}
.reveal.visible{opacity:1;transform:translateY(0)}
.reveal-d1{transition-delay:.1s}.reveal-d2{transition-delay:.2s}.reveal-d3{transition-delay:.3s}.reveal-d4{transition-delay:.35s}

/* ============================================
   RESPONSIVE
   ============================================ */
@media(max-width:900px){
  .hero-inner{grid-template-columns:1fr;text-align:center}
  .hero-desc{margin:0 auto 2rem}
  .hero-stats{justify-content:center}
  .hero-visual{display:none}
  .nav-links{display:none}
  .laravel-grid{grid-template-columns:1fr}
  .roadmap{flex-direction:column;gap:1.5rem}
  .roadmap::before{display:none}
  .rm-node{padding-top:0;text-align:left;padding-left:2.5rem}
  .rm-dot{top:4px;left:0}
}
</style>
</head>
<body>

<!-- ========== NAVBAR ========== -->
<nav class="navbar" id="navbar">
  <div class="nav-brand">
    <div class="nav-icon"><i data-lucide="code-2"></i></div>
    <span>DSW I</span>
  </div>
  <div class="nav-links">
    <a href="#competencia">Competencia</a>
    <a href="#roadmap">Roadmap</a>
    <a href="#laravel">Laravel</a>
    <a href="#evaluacion">Evaluación</a>
    <a href="#herramientas">Herramientas</a>
    <a href="#calendario">Calendario</a>
  </div>
</nav>

<!-- ========== HERO ========== -->
<section class="hero" id="inicio">
  <div class="hero-bg">
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
  </div>
  <div class="hero-inner">
    <div class="hero-text">
      <div class="hero-badge"><span class="badge-dot"></span>IF204IINF &middot; 5&deg; Trimestre &middot; 2026</div>
      <h1 class="hero-title">Desarrollo de<br><span class="gradient-text">Software Web I</span></h1>
      <p class="hero-desc">Construye aplicaciones web completas y modernas utilizando <strong>Laravel</strong>, el framework PHP más popular del mundo.</p>
      <div class="hero-stats">
        <div><span class="h-stat-val">72</span><span class="h-stat-lbl">Horas</span></div>
        <div><span class="h-stat-val">3</span><span class="h-stat-lbl">Unidades</span></div>
        <div><span class="h-stat-val">MVC</span><span class="h-stat-lbl">Patrón</span></div>
      </div>
      <a href="presentacion_U0.html" class="hero-cta"><i data-lucide="play"></i> Iniciar Presentación</a>
    </div>
    <div class="hero-visual">
      <div class="code-window">
        <div class="code-header">
          <span class="dot dot-r"></span><span class="dot dot-y"></span><span class="dot dot-g"></span>
          <span class="code-title">routes/web.php</span>
        </div>
        <div class="code-body">
          <span class="ln"><span class="cmt">// Define las rutas de tu aplicación</span></span>
          <span class="ln"><span class="kw">use</span> App\\Http\\Controllers\\<span class="cls">ProjectController</span>;</span>
          <span class="ln"></span>
          <span class="ln"><span class="cls">Route</span><span class="op">::</span><span class="fn">get</span>(<span class="str">'/projects'</span>, [</span>
          <span class="ln">&nbsp;&nbsp;&nbsp;&nbsp;<span class="cls">ProjectController</span><span class="op">::</span><span class="kw">class</span>,</span>
          <span class="ln">&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">'index'</span></span>
          <span class="ln">]);</span>
          <span class="ln"></span>
          <span class="ln"><span class="cls">Route</span><span class="op">::</span><span class="fn">get</span>(<span class="str">'/projects/{id}'</span>, [</span>
          <span class="ln">&nbsp;&nbsp;&nbsp;&nbsp;<span class="cls">ProjectController</span><span class="op">::</span><span class="kw">class</span>,</span>
          <span class="ln">&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">'show'</span></span>
          <span class="ln">]);</span>
          <span class="ln"></span>
          <span class="ln"><span class="cls">Route</span><span class="op">::</span><span class="fn">post</span>(<span class="str">'/projects'</span>, [</span>
          <span class="ln">&nbsp;&nbsp;&nbsp;&nbsp;<span class="cls">ProjectController</span><span class="op">::</span><span class="kw">class</span>,</span>
          <span class="ln">&nbsp;&nbsp;&nbsp;&nbsp;<span class="str">'store'</span></span>
          <span class="ln">]);</span>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ========== COMPETENCIA ========== -->
<section class="section" id="competencia">
  <div class="container">
    <div class="section-label reveal">Competencia</div>
    <h2 class="section-title reveal">¿Qué serás capaz de <span class="gradient-text">construir</span>?</h2>
    <p class="section-sub reveal">Al finalizar, construirás a nivel intermedio una aplicación de software web integrando diseño de interfaz, programación, arquitectura y calidad.</p>
    <div class="overview-grid">
      <div class="glass ov-card reveal reveal-d1">
        <div class="ov-icon"><i data-lucide="layout-template"></i></div>
        <h3>Arquitectura MVC</h3>
        <p>Domina el patrón Modelo-Vista-Controlador que estructura las aplicaciones web profesionales.</p>
      </div>
      <div class="glass ov-card reveal reveal-d2">
        <div class="ov-icon"><i data-lucide="component"></i></div>
        <h3>Componentes Reutilizables</h3>
        <p>Construye piezas de software modulares, mantenibles y escalables con Laravel.</p>
      </div>
      <div class="glass ov-card reveal reveal-d3">
        <div class="ov-icon"><i data-lucide="database"></i></div>
        <h3>ORM &amp; Base de Datos</h3>
        <p>Gestiona datos con Eloquent ORM: modelos, migraciones y relaciones entre tablas.</p>
      </div>
      <div class="glass ov-card reveal reveal-d4">
        <div class="ov-icon"><i data-lucide="shield-check"></i></div>
        <h3>Seguridad &amp; CRUD</h3>
        <p>Implementa autenticación, autorización, cifrado y operaciones CRUD completas.</p>
      </div>
    </div>
  </div>
</section>

<!-- ========== ROADMAP ========== -->
<section class="section" id="roadmap">
  <div class="container">
    <div class="section-label reveal">Ruta de aprendizaje</div>
    <h2 class="section-title reveal">Tu roadmap de <span class="gradient-text">12 semanas</span></h2>
    <p class="section-sub reveal">Un viaje progresivo: de los fundamentos del framework hasta una aplicación web completa con CRUD y seguridad.</p>
    <div class="roadmap reveal">
      <div class="rm-node">
        <div class="rm-dot"></div>
        <div class="rm-label">Semanas 2-4</div>
        <div class="rm-title">Unidad 1</div>
        <div class="rm-desc">Introducción a Frameworks Modernos y patrón MVC</div>
        <span class="rm-weight">10%</span>
      </div>
      <div class="rm-node">
        <div class="rm-dot"></div>
        <div class="rm-label">Semanas 5-7</div>
        <div class="rm-title">Unidad 2</div>
        <div class="rm-desc">Base de Datos, ORM y Seguridad de la Información</div>
        <span class="rm-weight">20%</span>
      </div>
      <div class="rm-node">
        <div class="rm-dot"></div>
        <div class="rm-label">Semanas 8-10</div>
        <div class="rm-title">Unidad 3</div>
        <div class="rm-desc">Operaciones CRUD: Crear, Leer, Actualizar, Eliminar</div>
        <span class="rm-weight">30%</span>
      </div>
      <div class="rm-node">
        <div class="rm-dot"></div>
        <div class="rm-label">Semana 12</div>
        <div class="rm-title">Examen Final</div>
        <div class="rm-desc">Caso práctico integrador con todos los contenidos</div>
        <span class="rm-weight">40%</span>
      </div>
    </div>
  </div>
</section>

<!-- ========== LARAVEL ========== -->
<section class="section" id="laravel">
  <div class="container">
    <div class="section-label reveal">Nuestro Framework</div>
    <h2 class="section-title reveal">¿Por qué <span class="gradient-text">Laravel</span>?</h2>
    <p class="section-sub reveal">El framework PHP más popular del mundo, utilizado por empresas de todos los tamaños para construir aplicaciones web robustas y escalables.</p>
    <div class="laravel-grid">
      <div class="glass lv-feature reveal reveal-d1">
        <div class="ov-icon"><i data-lucide="route"></i></div>
        <div>
          <h3>Routing Expresivo</h3>
          <p>Define rutas limpias y RESTful con una sintaxis clara que conecta URLs con controladores.</p>
        </div>
      </div>
      <div class="glass lv-feature reveal reveal-d2">
        <div class="ov-icon"><i data-lucide="settings-2"></i></div>
        <div>
          <h3>Controllers &amp; Middleware</h3>
          <p>Organiza la lógica en controladores y aplica filtros con middleware para seguridad y validación.</p>
        </div>
      </div>
      <div class="glass lv-feature reveal reveal-d3">
        <div class="ov-icon"><i data-lucide="database"></i></div>
        <div>
          <h3>Eloquent ORM</h3>
          <p>Interactúa con bases de datos usando objetos PHP elegantes en lugar de SQL crudo.</p>
        </div>
      </div>
      <div class="glass lv-feature reveal reveal-d4">
        <div class="ov-icon"><i data-lucide="file-code-2"></i></div>
        <div>
          <h3>Blade Templates</h3>
          <p>Motor de plantillas poderoso con herencia de layouts y componentes reutilizables.</p>
        </div>
      </div>
      <div class="glass lv-highlight reveal">
        <div class="big-num gradient-text">v13</div>
        <p>Laravel 13 (marzo 2026) — Con AI SDK integrado, PHP 8.3+, Passkeys y Octane para alto rendimiento.</p>
      </div>
    </div>
  </div>
</section>

<!-- ========== EVALUACIÓN ========== -->
<section class="section" id="evaluacion">
  <div class="container">
    <div class="section-label reveal">Sistema de evaluación</div>
    <h2 class="section-title reveal">¿Cómo se <span class="gradient-text">evalúa</span>?</h2>
    <p class="section-sub reveal">Todas las evaluaciones son desarrollo de casos aplicados con rúbrica detallada. La nota 4.0 se obtiene con un 60% de exigencia.</p>
    <div class="eval-list">
      <div class="glass eval-item reveal reveal-d1">
        <span class="eval-pct">10%</span>
        <div class="eval-info">
          <h4>Evaluación 1 — Frameworks Modernos</h4>
          <p>Caso: "Software de Gestión de Proyectos" — Definir rutas, controladores y vistas</p>
          <div class="eval-bar"><div class="eval-bar-fill" data-width="10"></div></div>
        </div>
      </div>
      <div class="glass eval-item reveal reveal-d2">
        <span class="eval-pct">20%</span>
        <div class="eval-info">
          <h4>Evaluación 2 — Base de Datos y Seguridad</h4>
          <p>ORM, autenticación, autorización y cifrado de datos en reposo</p>
          <div class="eval-bar"><div class="eval-bar-fill" data-width="20"></div></div>
        </div>
      </div>
      <div class="glass eval-item reveal reveal-d3">
        <span class="eval-pct">30%</span>
        <div class="eval-info">
          <h4>Evaluación 3 — Operaciones CRUD</h4>
          <p>Crear, Leer, Actualizar y Eliminar registros de forma segura y eficiente</p>
          <div class="eval-bar"><div class="eval-bar-fill" data-width="30"></div></div>
        </div>
      </div>
      <div class="glass eval-item reveal reveal-d4">
        <span class="eval-pct">40%</span>
        <div class="eval-info">
          <h4>Examen Transversal Final</h4>
          <p>Caso práctico integrador que abarca todas las unidades del curso</p>
          <div class="eval-bar"><div class="eval-bar-fill" data-width="40"></div></div>
        </div>
      </div>
      <div class="eval-note reveal">
        <i data-lucide="info"></i>
        <span>Todas las evaluaciones serán revisadas con rúbrica detallada que se entrega <strong>antes</strong> de cada evaluación.</span>
      </div>
    </div>
  </div>
</section>

<!-- ========== HERRAMIENTAS ========== -->
<section class="section" id="herramientas">
  <div class="container">
    <div class="section-label reveal">Stack tecnológico</div>
    <h2 class="section-title reveal">Tus <span class="gradient-text">herramientas</span></h2>
    <p class="section-sub reveal">Asegúrate de tener estas herramientas instaladas antes de la semana 2. Son tu kit esencial de desarrollo.</p>
    <div class="tools-grid">
      <div class="glass tool-card reveal reveal-d1">
        <div class="ov-icon"><i data-lucide="braces"></i></div>
        <div class="tool-name">PHP</div>
        <div class="tool-ver">v8.3+</div>
        <p class="tool-desc">Lenguaje de programación base para el desarrollo backend con Laravel.</p>
      </div>
      <div class="glass tool-card reveal reveal-d2">
        <div class="ov-icon"><i data-lucide="package"></i></div>
        <div class="tool-name">Composer</div>
        <div class="tool-ver">v2.x</div>
        <p class="tool-desc">Gestor de dependencias de PHP. Instala y gestiona las librerías del proyecto.</p>
      </div>
      <div class="glass tool-card reveal reveal-d3">
        <div class="ov-icon"><i data-lucide="rocket"></i></div>
        <div class="tool-name">Laravel</div>
        <div class="tool-ver">v13</div>
        <p class="tool-desc">Framework MVC para construir aplicaciones web robustas, elegantes y escalables.</p>
      </div>
      <div class="glass tool-card reveal reveal-d4">
        <div class="ov-icon"><i data-lucide="monitor"></i></div>
        <div class="tool-name">VS Code</div>
        <div class="tool-ver">latest</div>
        <p class="tool-desc">IDE recomendado con extensiones para PHP, Laravel y autocompletado inteligente.</p>
      </div>
    </div>
  </div>
</section>

<!-- ========== CALENDARIO ========== -->
<section class="section" id="calendario">
  <div class="container">
    <div class="section-label reveal">Planificación</div>
    <h2 class="section-title reveal">Calendario del <span class="gradient-text">trimestre</span></h2>
    <p class="section-sub reveal">2° Trimestre 2026 — Modalidad Online. Cada semana tiene actividades sincrónicas o asincrónicas.</p>
    <div class="cal-wrap reveal">
      <table class="cal-table">
        <thead>
          <tr><th>Sem.</th><th>Hito</th><th>Inicio</th><th>Término</th><th>Recurso Didáctico</th><th>Modalidad</th></tr>
        </thead>
        <tbody>
          <tr><td>1</td><td>Inicio</td><td>30-jun</td><td>05-jul</td><td>Bienvenida a la Asignatura — Inicio Unidad 1</td><td><span class="badge-sync">Sincrónica</span></td></tr>
          <tr><td>2</td><td>EA 1</td><td>06-jul</td><td>12-jul</td><td>Revisión RDD Unidad 1 — Foro</td><td><span class="badge-async">Asincrónica</span></td></tr>
          <tr><td>3</td><td>EA 1</td><td>13-jul</td><td>19-jul</td><td>Retroalimentación RDD 1 — Cuestionario</td><td><span class="badge-sync">Sincrónica</span></td></tr>
          <tr class="eval-row"><td>4</td><td>Eval 1</td><td>17-jul</td><td>26-jul</td><td>EVALUACIÓN 1</td><td><span class="badge-async">Asincrónica</span></td></tr>
          <tr><td>5</td><td>EA 2</td><td>27-jul</td><td>02-ago</td><td>Retroalimentación Eval 1 — Inicio U2 — Foro</td><td><span class="badge-sync">Sincrónica</span></td></tr>
          <tr><td>6</td><td>EA 2</td><td>03-ago</td><td>09-ago</td><td>Retroalimentación RDD 2 — Cuestionario</td><td><span class="badge-sync">Sincrónica</span></td></tr>
          <tr class="eval-row"><td>7</td><td>Eval 2</td><td>07-ago</td><td>16-ago</td><td>EVALUACIÓN 2</td><td><span class="badge-async">Asincrónica</span></td></tr>
          <tr><td>8</td><td>EA 3</td><td>17-ago</td><td>23-ago</td><td>Retroalimentación Eval 2 — Inicio U3 — Foro</td><td><span class="badge-sync">Sincrónica</span></td></tr>
          <tr><td>9</td><td>EA 3</td><td>24-ago</td><td>30-ago</td><td>Retroalimentación RDD 3 — Cuestionario</td><td><span class="badge-sync">Sincrónica</span></td></tr>
          <tr class="eval-row"><td>10</td><td>Eval 3</td><td>28-ago</td><td>06-sep</td><td>EVALUACIÓN 3</td><td><span class="badge-async">Asincrónica</span></td></tr>
          <tr><td>11</td><td>Cierre</td><td>07-sep</td><td>13-sep</td><td>Retroalimentación Eval 3 — Rev. Examen Final</td><td><span class="badge-sync">Sincrónica</span></td></tr>
          <tr class="final-row"><td>12</td><td>Final</td><td>11-sep</td><td>17-sep</td><td>EXAMEN TRANSVERSAL FINAL</td><td><span class="badge-async">Asincrónica</span></td></tr>
        </tbody>
      </table>
    </div>
  </div>
</section>

<!-- ========== CTA ========== -->
<section class="section" id="cta">
  <div class="container">
    <div class="cta-box reveal">
      <h2>¿Listo para empezar? <span class="gradient-text">¡Vamos!</span></h2>
      <p>Accede a la presentación completa de bienvenida y conoce todo sobre esta asignatura.</p>
      <a href="presentacion_U0.html" class="hero-cta"><i data-lucide="presentation"></i> Ver Presentación de Bienvenida</a>
    </div>
  </div>
</section>

<!-- ========== FOOTER ========== -->
<footer class="footer">
  <div class="container">
    <p>Desarrollo de Software Web I &middot; IF204IINF &middot; <span>Instituto Profesional San Sebastián</span> &middot; 2° Trimestre 2026</p>
  </div>
</footer>

<!-- ========== SCRIPTS ========== -->
<script>
/* Lucide Icons */
lucide.createIcons();

/* Navbar scroll */
const nav=document.getElementById('navbar');
window.addEventListener('scroll',()=>{nav.classList.toggle('scrolled',window.scrollY>40)});

/* Scroll reveal */
const obs=new IntersectionObserver((entries)=>{
  entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');obs.unobserve(e.target)}})
},{threshold:.12});
document.querySelectorAll('.reveal').forEach(el=>obs.observe(el));

/* Progress bars */
const barObs=new IntersectionObserver((entries)=>{
  entries.forEach(e=>{
    if(e.isIntersecting){
      const fill=e.target.querySelector('.eval-bar-fill');
      if(fill){fill.style.width=fill.dataset.width+'%'}
      barObs.unobserve(e.target);
    }
  })
},{threshold:.5});
document.querySelectorAll('.eval-item').forEach(el=>barObs.observe(el));

/* Smooth nav links */
document.querySelectorAll('.nav-links a').forEach(a=>{
  a.addEventListener('click',e=>{
    e.preventDefault();
    const t=document.querySelector(a.getAttribute('href'));
    if(t)t.scrollIntoView({behavior:'smooth',block:'start'});
  });
});
</script>
</body>
</html>"""

def main():
    with open(OUTPUT, 'w', encoding='utf-8') as f:
        f.write(HTML)
    size = os.path.getsize(OUTPUT)
    print(f'\\u2705 Portal generado: {OUTPUT}')
    print(f'   Tamano: {size:,} bytes ({size/1024:.1f} KB)')

if __name__ == '__main__':
    main()
