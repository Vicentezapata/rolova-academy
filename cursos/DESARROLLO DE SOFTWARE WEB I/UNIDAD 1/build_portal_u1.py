#!/usr/bin/env python3
"""
build_portal_u1.py — Genera portal_unidad1.html
Dashboard interactivo de entrada para la Unidad 1 de Desarrollo de Software Web I.
(Enfoque en Interfaces, Blade, Artisan y FAQs)
"""
import os

DIR = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(DIR, 'portal_unidad1.html')

CSS = """
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
::-webkit-scrollbar{width:8px}
::-webkit-scrollbar-track{background:var(--bg)}
::-webkit-scrollbar-thumb{background:var(--border);border-radius:4px}
::-webkit-scrollbar-thumb:hover{background:var(--text3)}
a{color:var(--p);text-decoration:none;transition:color .3s}
a:hover{color:var(--c2)}

/* ── Typography & Gradients ── */
.gradient-text{background:linear-gradient(135deg,var(--p),var(--c2),var(--c3));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.title-xl{font-size:clamp(2.5rem,6vw,4rem);font-weight:900;line-height:1.05;letter-spacing:-.03em;margin-bottom:1.5rem}
.title-lg{font-size:clamp(2rem,4vw,2.5rem);font-weight:800;line-height:1.15;letter-spacing:-.02em;margin-bottom:1.5rem}
.subtitle{font-size:1.1rem;color:var(--text2);margin-bottom:2rem;max-width:600px}
.mono{font-family:var(--mono)}

/* ── UI Components ── */
.btn{display:inline-flex;align-items:center;gap:.6rem;padding:.75rem 1.5rem;border-radius:50px;font-weight:600;font-size:.95rem;cursor:pointer;transition:all .3s;border:none}
.btn-primary{background:var(--p);color:#fff;box-shadow:0 4px 15px var(--p-glow)}
.btn-primary:hover{background:var(--c2);transform:translateY(-2px);box-shadow:0 6px 20px var(--p-glow)}
.btn-secondary{background:var(--surface);color:var(--text);border:1px solid var(--border)}
.btn-secondary:hover{background:var(--surface-h);transform:translateY(-2px)}

.badge{display:inline-block;padding:.35rem .85rem;border-radius:50px;font-family:var(--mono);font-size:.75rem;font-weight:600;letter-spacing:1px}
.badge.orange{background:rgba(255,69,0,.15);color:var(--p);border:1px solid rgba(255,69,0,.2)}
.badge.gray{background:var(--surface);color:var(--text2);border:1px solid var(--border)}

/* ── Layout & Sections ── */
.container{max-width:1200px;margin:0 auto;padding:0 2rem}
section{padding:5rem 0;position:relative}

/* ── Navbar ── */
.nav{position:fixed;top:0;left:0;right:0;padding:1.25rem 0;z-index:100;transition:all .4s}
.nav.scrolled{background:rgba(10,14,26,.8);backdrop-filter:blur(12px);border-bottom:1px solid var(--border)}
.nav .container{display:flex;align-items:center;justify-content:space-between}
.nav-logo{font-weight:800;font-size:1.1rem;display:flex;align-items:center;gap:.5rem}
.nav-logo .dot{width:8px;height:8px;background:var(--p);border-radius:50%;box-shadow:0 0 10px var(--p-glow)}
.nav-links{display:flex;gap:1.5rem;align-items:center}
.nav-links a{font-size:.9rem;color:var(--text2);font-weight:500}
.nav-links a:hover{color:var(--text)}

/* ── Hero ── */
.hero{min-height:100vh;display:flex;align-items:center;padding-top:4rem}
.hero-grid{display:grid;grid-template-columns:1fr 1fr;gap:4rem;align-items:center}
.hero-content .badge{margin-bottom:1.5rem}

.code-window{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;box-shadow:0 20px 40px rgba(0,0,0,.5);transform:perspective(1000px) rotateY(-5deg) rotateX(2deg);transition:transform .5s ease}
.code-window:hover{transform:perspective(1000px) rotateY(0) rotateX(0)}
.cw-header{display:flex;align-items:center;gap:.4rem;padding:.75rem 1rem;background:rgba(255,255,255,.03);border-bottom:1px solid var(--border)}
.cw-dot{width:10px;height:10px;border-radius:50%}
.cw-dot.r{background:#FF5F57}.cw-dot.y{background:#FFBD2E}.cw-dot.g{background:#28CA41}
.cw-title{margin-left:1rem;font-family:var(--mono);font-size:.7rem;color:var(--text3)}
.cw-body{padding:1.5rem;font-family:var(--mono);font-size:.85rem;line-height:1.6;color:#A9B7C6;overflow-x:auto}
.cw-body .c-p{color:#CC7832} /* keyword */
.cw-body .c-f{color:#FFC66D} /* function */
.cw-body .c-s{color:#6A8759} /* string */
.cw-body .c-c{color:#808080} /* comment */

/* ── Cards Grid (Concepts) ── */
.cards-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:1.5rem;margin-top:3rem}
.card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:2rem;transition:all .4s}
.card:hover{background:var(--surface-h);transform:translateY(-5px);border-color:rgba(255,69,0,.15)}
.card-icon{width:50px;height:50px;border-radius:14px;background:linear-gradient(135deg,rgba(255,69,0,.1),rgba(255,122,51,.05));border:1px solid rgba(255,69,0,.15);display:flex;align-items:center;justify-content:center;margin-bottom:1.25rem}
.card-icon svg{width:24px;height:24px;color:var(--p)}
.card h3{font-size:1.1rem;font-weight:700;margin-bottom:.5rem}
.card p{font-size:.9rem;color:var(--text2);line-height:1.6}

/* ── Artisan Cheatsheet ── */
.artisan-section{background:var(--bg2);border-top:1px solid var(--border);border-bottom:1px solid var(--border);padding:6rem 0}
.artisan-grid{display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-top:3rem}
.a-command{background:var(--bg);border:1px solid var(--border);padding:1.5rem;border-radius:var(--radius-sm);display:flex;flex-direction:column;gap:.5rem}
.a-command code{font-family:var(--mono);color:var(--p);font-size:.9rem;background:rgba(255,69,0,.1);padding:.3rem .6rem;border-radius:4px;display:inline-block;align-self:flex-start}
.a-command h4{font-size:.95rem;font-weight:700}
.a-command p{font-size:.85rem;color:var(--text2)}

/* ── FAQ Accordion ── */
.faq-section{padding:6rem 0}
.faq-container{max-width:800px;margin:3rem auto 0;display:flex;flex-direction:column;gap:1rem}
.faq-item{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-sm);overflow:hidden}
.faq-question{width:100%;text-align:left;background:none;border:none;padding:1.25rem 1.5rem;color:var(--text);font-weight:600;font-size:1rem;display:flex;justify-content:space-between;align-items:center;cursor:pointer;font-family:var(--font)}
.faq-question:hover{background:var(--surface-h)}
.faq-question svg{width:20px;height:20px;color:var(--p);transition:transform .3s}
.faq-item.active .faq-question svg{transform:rotate(180deg)}
.faq-answer{padding:0 1.5rem;max-height:0;overflow:hidden;transition:all .3s ease;color:var(--text2);font-size:.9rem;line-height:1.6}
.faq-item.active .faq-answer{padding:0 1.5rem 1.5rem;max-height:500px}
.faq-answer code{font-family:var(--mono);background:var(--bg);padding:.2rem .4rem;border-radius:4px;color:var(--p)}

/* ── Resources & Eval ── */
.resources-grid{display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-top:3rem}
.res-card{padding:3rem;border-radius:var(--radius);border:1px solid var(--border);position:relative;overflow:hidden;display:flex;flex-direction:column;align-items:flex-start}
.res-card.pres{background:linear-gradient(135deg,rgba(10,14,26,1),rgba(255,69,0,.05))}
.res-card.eval{background:linear-gradient(135deg,rgba(10,14,26,1),rgba(255,179,71,.05))}
.res-icon{width:60px;height:60px;border-radius:16px;background:var(--surface);display:flex;align-items:center;justify-content:center;margin-bottom:1.5rem;border:1px solid var(--border)}
.res-icon svg{width:30px;height:30px;color:var(--p)}
.res-card h3{font-size:1.5rem;font-weight:800;margin-bottom:.75rem}
.res-card p{font-size:.95rem;color:var(--text2);margin-bottom:2rem;line-height:1.6}

/* ── Footer ── */
footer{padding:3rem 0;text-align:center;border-top:1px solid var(--border);color:var(--text3);font-size:.85rem}

/* ── Reveal Animations ── */
.reveal{opacity:0;transform:translateY(30px);transition:all .8s ease}
.reveal.active{opacity:1;transform:translateY(0)}

@media(max-width:900px){
  .hero-grid{grid-template-columns:1fr;text-align:center;gap:2rem}
  .hero-content .subtitle{margin:0 auto 2rem}
  .artisan-grid{grid-template-columns:1fr}
  .resources-grid{grid-template-columns:1fr}
}
@media(max-width:600px){
  .nav-links{display:none}
}
"""

HTML = """<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Unidad 1 - Frameworks y Blade</title>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
<style>
{css}
</style>
</head>
<body>

<nav class="nav" id="nav">
  <div class="container">
    <div class="nav-logo"><div class="dot"></div> DS Web I</div>
    <div class="nav-links">
      <a href="#conceptos">Conceptos</a>
      <a href="#artisan">Artisan CLI</a>
      <a href="#faq">Preguntas Frecuentes</a>
      <a href="#recursos">Recursos</a>
    </div>
  </div>
</nav>

<section class="hero">
  <div class="container hero-grid">
    <div class="hero-content reveal">
      <span class="badge orange">Unidad 1</span>
      <h1 class="title-xl">Diseño de Interfaces con <span class="gradient-text">Blade & Laravel</span></h1>
      <p class="subtitle">Descubre cómo Laravel simplifica el desarrollo web y cómo Blade te permite crear interfaces HTML dinámicas, modulares y seguras.</p>
      <div style="display:flex;gap:1rem;flex-wrap:wrap;justify-content:flex-start">
        <a href="presentacion_U1.html" class="btn btn-primary"><i data-lucide="play-circle"></i> Ver Presentación</a>
        <a href="evaluacion_U1.html" class="btn btn-secondary"><i data-lucide="file-check"></i> Ir a la Evaluación</a>
      </div>
    </div>
    <div class="hero-image reveal">
      <div class="code-window">
        <div class="cw-header">
          <div class="cw-dot r"></div><div class="cw-dot y"></div><div class="cw-dot g"></div>
          <div class="cw-title">resources/views/ejemplo.blade.php</div>
        </div>
        <div class="cw-body">
<span class="c-c">&lt;!-- Directiva para heredar un Layout maestro --&gt;</span>
<span class="c-p">@extends</span>(<span class="c-s">'layouts.app'</span>)

<span class="c-p">@section</span>(<span class="c-s">'content'</span>)
  &lt;h1&gt;Bienvenido, <span class="c-f">{{ $user->name }}</span>&lt;/h1&gt;

  <span class="c-c">&lt;!-- Componente reutilizable --&gt;</span>
  &lt;x-alert type="success"&gt;
    Inicio de sesión exitoso.
  &lt;/x-alert&gt;
<span class="c-p">@endsection</span>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="conceptos" class="container">
  <h2 class="title-lg text-center reveal">Conceptos <span class="gradient-text">Clave</span></h2>
  <div class="cards-grid">
    <div class="card reveal">
      <div class="card-icon"><i data-lucide="layout-template"></i></div>
      <h3>Motor Blade</h3>
      <p>El motor de plantillas de Laravel. Te permite usar HTML puro pero inyectar PHP con doble llave <code>{{ }}</code>, asegurando protección automática contra ataques XSS.</p>
    </div>
    <div class="card reveal">
      <div class="card-icon"><i data-lucide="component"></i></div>
      <h3>Componentes y Layouts</h3>
      <p>Aplica el principio DRY (No te repitas). Usa Layouts para la estructura global de tu página y Componentes para piezas pequeñas como botones y tarjetas.</p>
    </div>
    <div class="card reveal">
      <div class="card-icon"><i data-lucide="folder-open"></i></div>
      <h3>resources/views/</h3>
      <p>La carpeta más importante para el frontend en Laravel. Todas tus interfaces gráficas se almacenan aquí. Deben terminar en <code>.blade.php</code>.</p>
    </div>
    <div class="card reveal">
      <div class="card-icon"><i data-lucide="terminal"></i></div>
      <h3>Artisan CLI</h3>
      <p>Tu asistente por línea de comandos. Artisan te generará archivos pre-configurados para controladores y modelos en un solo comando.</p>
    </div>
  </div>
</section>

<section id="artisan" class="artisan-section">
  <div class="container">
    <div style="text-align:center">
      <span class="badge gray reveal">Consola</span>
      <h2 class="title-lg reveal" style="margin-top:1rem">Cheatsheet de <span class="gradient-text">Artisan</span></h2>
      <p class="subtitle reveal" style="margin:0 auto">Los comandos que más usarás al construir tu aplicación.</p>
    </div>
    
    <div class="artisan-grid">
      <div class="a-command reveal">
        <code>php artisan serve</code>
        <h4>Levantar el Servidor Local</h4>
        <p>Inicia tu aplicación en http://localhost:8000 para que puedas ver y probar tus interfaces web.</p>
      </div>
      <div class="a-command reveal">
        <code>php artisan make:controller NameController</code>
        <h4>Crear un Controlador</h4>
        <p>Genera la estructura base de un controlador en <code>app/Http/Controllers/</code>.</p>
      </div>
      <div class="a-command reveal">
        <code>php artisan route:list</code>
        <h4>Ver tus Rutas</h4>
        <p>Muestra una lista completa de todas las rutas (URLs) disponibles en tu aplicación.</p>
      </div>
      <div class="a-command reveal" style="background:rgba(255,179,71,.05); border-color:rgba(255,179,71,.2)">
        <code>&gt; click derecho -&gt; nuevo archivo</code>
        <h4>¿Cómo crear una Vista?</h4>
        <p>A diferencia de los controladores, Laravel no trae un <code>make:view</code>. Simplemente crea tu archivo <code>nombre.blade.php</code> manualmente en la carpeta <code>resources/views</code>.</p>
      </div>
    </div>
  </div>
</section>

<section id="faq" class="faq-section container">
  <h2 class="title-lg text-center reveal">Preguntas <span class="gradient-text">Frecuentes (FAQ)</span></h2>
  <p class="subtitle text-center reveal" style="margin:0 auto">Problemas típicos de Laravel y cómo resolverlos.</p>

  <div class="faq-container reveal">
    <div class="faq-item">
      <button class="faq-question">
        Cloné un repositorio de Laravel y la página muestra error 500. ¿Qué hago?
        <i data-lucide="chevron-down"></i>
      </button>
      <div class="faq-answer">
        <p>Esto pasa siempre porque las dependencias pesadas y los archivos con contraseñas (el `.env`) NO se suben a Git por seguridad.</p>
        <p style="margin-top:1rem">Soluciónala en tu terminal con 3 simples pasos:</p>
        <ul style="margin-left:1.5rem; margin-top:.5rem">
          <li>1. Descargar librerías: <code>composer install</code></li>
          <li>2. Copiar el archivo de entorno: <code>cp .env.example .env</code></li>
          <li>3. Generar la llave única de tu app: <code>php artisan key:generate</code></li>
        </ul>
      </div>
    </div>
    
    <div class="faq-item">
      <button class="faq-question">
        Si hago cambios en CSS/JS, ¿tengo que reiniciar el `php artisan serve`?
        <i data-lucide="chevron-down"></i>
      </button>
      <div class="faq-answer">
        <p>No. El comando <code>php artisan serve</code> gestiona el servidor PHP. Tus archivos CSS, JS y Vistas Blade son interpretados automáticamente en cada recarga de la página web. Solo debes reiniciar el servidor si modificas archivos de entorno <code>.env</code>.</p>
      </div>
    </div>

    <div class="faq-item">
      <button class="faq-question">
        ¿Puedo usar Bootstrap o Tailwind junto con Blade?
        <i data-lucide="chevron-down"></i>
      </button>
      <div class="faq-answer">
        <p>¡Totalmente! Blade no te restringe en absoluto en qué CSS usar. Puedes escribir tus clases de Tailwind o Bootstrap directamente dentro de los archivos <code>.blade.php</code> tal como lo harías en un HTML normal.</p>
      </div>
    </div>
    
    <div class="faq-item">
      <button class="faq-question">
        ¿Cuándo debo usar @include y cuándo &lt;x-component&gt;?
        <i data-lucide="chevron-down"></i>
      </button>
      <div class="faq-answer">
        <p>Usa <code>@include</code> para bloques de HTML estáticos o muy simples (por ejemplo, insertar el Footer). Usa <code>&lt;x-component&gt;</code> cuando necesitas interfaces dinámicas que reciben parámetros, como un botón de alerta que cambia de color según si recibe `type="error"` o `type="success"`.</p>
      </div>
    </div>
  </div>
</section>

<section id="recursos" class="container">
  <div class="resources-grid">
    <div class="res-card pres reveal">
      <div class="res-icon"><i data-lucide="presentation"></i></div>
      <h3>Mega Presentación (Blade Edition)</h3>
      <p>Material de estudio completo. Incluye el contenido sobre MVC, Blade, Componentes y el guión del profesor interactivo.</p>
      <a href="presentacion_U1.html" class="btn btn-primary">Estudiar ahora</a>
    </div>
    <div class="res-card eval reveal">
      <div class="res-card-glow"></div>
      <div class="res-icon" style="color:var(--c3)"><i data-lucide="file-check-2"></i></div>
      <h3>Evaluación (10%)</h3>
      <p>Caso "Tech Solutions": Crea rutas, controladores y vistas Blade para un gestor de proyectos.</p>
      <a href="evaluacion_U1.html" class="btn btn-secondary">Ver Evaluación</a>
    </div>
  </div>
</section>

<footer>
  <div class="container">
    Desarrollo de Software Web I - Unidad 1 &copy; 2026 IPSS
  </div>
</footer>

<script>
  lucide.createIcons();

  // Scroll handler for navbar
  window.addEventListener('scroll', () => {
    const nav = document.getElementById('nav');
    if(window.scrollY > 50) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');
  });

  // FAQ Accordion
  document.querySelectorAll('.faq-question').forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.parentElement;
      const isActive = item.classList.contains('active');
      
      // Close all others
      document.querySelectorAll('.faq-item').forEach(i => i.classList.remove('active'));
      
      if(!isActive) {
        item.classList.add('active');
      }
    });
  });

  // Intersection Observer for Reveal animations
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if(entry.isIntersecting) {
        entry.target.classList.add('active');
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
</script>
</body>
</html>
"""

def main():
    html_content = HTML.replace('{css}', CSS)
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f'\\u2705 Portal U1 (Blade Edition) generado: {OUT}')

if __name__ == '__main__':
    main()
