#!/usr/bin/env python3
"""
build_presentacion.py — Genera presentacion_U0.html
Mega Presentación Interactiva · Desarrollo de Software Web I · Unidad 0
26 diapositivas con Guión del Profesor integrado
"""
import os, json

DIR = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(DIR, 'presentacion_U0.html')

# ═══════════════════════════════════════════════════════════
#  SLIDES DATA — 26 diapositivas
# ═══════════════════════════════════════════════════════════
S = []

# ── 1. PORTADA ─────────────────────────────────────────────
S.append({
    'layout':'cover',
    'content':'''
    <div class="cover-badge"><span class="bdot"></span>IF204IINF &middot; 5&deg; Trimestre &middot; 2026</div>
    <h1 class="cover-title">Desarrollo de<br><span class="gradient-text">Software Web I</span></h1>
    <p class="cover-sub">Construye aplicaciones web modernas con Laravel</p>
    <div class="cover-inst">Instituto Profesional San Sebastián</div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«Bienvenidos al curso de Desarrollo de Software Web I. Mi nombre es [tu nombre] y los acompañaré durante las próximas 12 semanas.»</li>
    <li>«Este curso es diferente a lo que han visto antes: aquí no solo vamos a escribir código, vamos a construir aplicaciones web reales, completas y funcionales.»</li>
    <li>«Usaremos Laravel, el framework PHP más popular del mundo. No se preocupen si no lo conocen todavía — para eso estamos aquí.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>Laravel fue creado por Taylor Otwell en 2011 porque estaba frustrado con CodeIgniter, que no tenía soporte nativo para autenticación. Hoy, Laravel tiene más de 75 millones de descargas y es usado por empresas como Disney, Warner Bros y The New York Times.</p>
    <div class="t-time">Tiempo: 2 min</div>
    '''
})

# ── 2. ¿POR QUÉ ESTAMOS AQUÍ? ─────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">¿Por qué <span class="gradient-text">estamos aquí</span>?</h1>
    <p class="s-lead">El mundo funciona con aplicaciones web. Cada vez que usas Instagram, reservas un vuelo o haces una compra online, interactúas con una aplicación web construida por desarrolladores como tú.</p>
    <div class="s-stats">
      <div class="s-stat"><span class="s-stat-val">5.500M+</span><span class="s-stat-lbl">Usuarios de internet en 2026</span></div>
      <div class="s-stat"><span class="s-stat-val">1.100M+</span><span class="s-stat-lbl">Sitios web activos</span></div>
      <div class="s-stat"><span class="s-stat-val">$700B+</span><span class="s-stat-lbl">Mercado de desarrollo web</span></div>
    </div>
    <p class="s-note">La demanda de desarrolladores web sigue creciendo — y la brecha entre oferta y demanda es enorme en Latinoamérica.</p>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«Antes de hablar de código, quiero que reflexionen sobre algo: ¿cuántas aplicaciones web usaron hoy? Gmail, WhatsApp Web, YouTube, Spotify, su banco...»</li>
    <li>«Todas esas aplicaciones fueron construidas por desarrolladores que alguna vez estuvieron sentados donde ustedes están ahora.»</li>
    <li>«El mercado de desarrollo web en 2026 supera los 700 mil millones de dólares. En Chile y Latinoamérica, la demanda de desarrolladores web supera con creces la oferta — lo que significa oportunidades reales de empleo.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>En Chile, un desarrollador web junior con conocimientos de Laravel puede ganar entre $800.000 y $1.200.000 CLP mensuales. Un desarrollador senior puede superar los $3.000.000 CLP. La inversión en aprender un framework moderno tiene un retorno muy alto.</p>
    <div class="t-time">Tiempo: 2-3 min</div>
    '''
})

# ── 3. LA REVOLUCIÓN WEB ──────────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">La revolución <span class="gradient-text">web</span></h1>
    <p class="s-lead">De páginas estáticas a aplicaciones web complejas — un viaje de 35 años.</p>
    <div class="timeline">
      <div class="tl-item"><span class="tl-year">1991</span><div class="tl-content"><strong>HTML nace</strong><br>Tim Berners-Lee crea la primera página web. Texto plano, sin estilos.</div></div>
      <div class="tl-item"><span class="tl-year">2000</span><div class="tl-content"><strong>PHP &amp; MySQL</strong><br>Páginas dinámicas. Los sitios empiezan a generar contenido desde bases de datos.</div></div>
      <div class="tl-item"><span class="tl-year">2010</span><div class="tl-content"><strong>Frameworks MVC</strong><br>Laravel, Django, Rails — desarrollo estructurado con patrones de diseño.</div></div>
      <div class="tl-item"><span class="tl-year">2020</span><div class="tl-content"><strong>APIs &amp; SPA</strong><br>Arquitecturas desacopladas. Frontend (React/Vue) + Backend (Laravel API).</div></div>
      <div class="tl-item active"><span class="tl-year">2026</span><div class="tl-content"><strong>AI-First Development</strong><br>IA integrada en el flujo de trabajo. Laravel 13 con AI SDK nativo.</div></div>
    </div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«Vamos a hacer un viaje rápido por la historia del desarrollo web para entender de dónde venimos y hacia dónde vamos.»</li>
    <li>«En 1991, la primera página web era literalmente texto con enlaces. Hoy construimos aplicaciones que procesan millones de transacciones.»</li>
    <li>«Fíjense que cada salto tecnológico redujo la complejidad para el desarrollador. Los frameworks como Laravel aparecieron justamente para eso: hacer más con menos código.»</li>
    <li>«En 2026, la IA ya no es un experimento — está integrada directamente en nuestras herramientas de desarrollo. Laravel 13 incluye un SDK de IA nativo.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>La primera página web del mundo (info.cern.ch) sigue online. Si la visitan, verán que es solo texto con hiperenlaces. Comparen eso con cualquier app web moderna y verán cuánto hemos avanzado en 35 años.</p>
    <div class="t-time">Tiempo: 3 min</div>
    '''
})

# ── 4. ¿QUÉ CONSTRUIREMOS? ────────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">¿Qué vamos a <span class="gradient-text">construir</span>?</h1>
    <p class="s-lead">A lo largo de este curso, construirán de forma incremental una aplicación web completa usando Laravel.</p>
    <div class="s-split">
      <div class="s-left">
        <div class="app-preview">
          <div class="app-header">
            <span class="dot-r"></span><span class="dot-y"></span><span class="dot-g"></span>
            <span class="app-url">localhost:8000/projects</span>
          </div>
          <div class="app-body">
            <div class="app-sidebar">
              <div class="app-menu-item active-item">Proyectos</div>
              <div class="app-menu-item">Usuarios</div>
              <div class="app-menu-item">Tareas</div>
              <div class="app-menu-item">Config</div>
            </div>
            <div class="app-main">
              <div class="app-row"></div>
              <div class="app-row short"></div>
              <div class="app-row"></div>
              <div class="app-row short"></div>
            </div>
          </div>
        </div>
      </div>
      <div class="s-right">
        <h3>Software de Gestión de Proyectos</h3>
        <ul class="s-list">
          <li><i data-lucide="route"></i> Rutas y navegación (URL routing)</li>
          <li><i data-lucide="layout-template"></i> Vistas con Blade Templates</li>
          <li><i data-lucide="database"></i> Modelos y base de datos (ORM)</li>
          <li><i data-lucide="shield-check"></i> Autenticación y autorización</li>
          <li><i data-lucide="pencil"></i> Operaciones CRUD completas</li>
        </ul>
      </div>
    </div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«Este es el tipo de aplicación que serán capaces de construir al final del curso: un sistema de gestión de proyectos para una empresa ficticia llamada Tech Solutions.»</li>
    <li>«Fíjense que tiene todo lo que esperarían de una app profesional: un menú lateral, listado de datos, formularios, autenticación...»</li>
    <li>«Lo iremos construyendo de forma incremental: en la Unidad 1 crearemos las rutas y vistas, en la Unidad 2 conectaremos la base de datos, y en la Unidad 3 implementaremos las operaciones CRUD.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>El caso de «Tech Solutions» está inspirado en proyectos reales. Muchas startups exitosas empezaron con exactamente este tipo de aplicación interna. Trello, Asana y Jira — todas son variaciones de un gestor de proyectos.</p>
    <div class="t-time">Tiempo: 2-3 min</div>
    '''
})

# ── 5. COMPETENCIA DEL CURSO ──────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">La competencia que <span class="gradient-text">desarrollarás</span></h1>
    <div class="competencia-box">
      <div class="comp-icon"><i data-lucide="target"></i></div>
      <p class="comp-text">«Construye en un nivel intermedio una aplicación de software integrando el diseño de interfaz y la experiencia de usuario con la programación, arquitectura de la aplicación y su calidad de acuerdo a las necesidades del cliente.»</p>
      <span class="comp-level">Nivel de dominio: 4</span>
    </div>
    <div class="s-cards three">
      <div class="s-card"><div class="s-card-icon"><i data-lucide="code-2"></i></div><h3>Programación</h3><p>Codificación eficiente con Laravel y PHP</p></div>
      <div class="s-card"><div class="s-card-icon"><i data-lucide="blocks"></i></div><h3>Arquitectura</h3><p>Patrones de diseño MVC y buenas prácticas</p></div>
      <div class="s-card"><div class="s-card-icon"><i data-lucide="user-check"></i></div><h3>Experiencia</h3><p>Interfaces centradas en el usuario final</p></div>
    </div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«Esta es la competencia oficial que desarrollaremos. Léanla con atención porque es lo que se evaluará.»</li>
    <li>«Noten tres palabras clave: programación, arquitectura y experiencia de usuario. No basta con que el código funcione — debe estar bien estructurado y ser usable.»</li>
    <li>«El nivel de dominio 4 significa que al finalizar, deben poder crear aplicaciones web de mediana complejidad de forma autónoma.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>En la industria real, un código que «funciona» pero está mal estructurado genera lo que se llama «deuda técnica». Empresas gastan hasta el 40% de su presupuesto de desarrollo pagando deuda técnica de código mal escrito. Por eso la arquitectura importa tanto como la funcionalidad.</p>
    <div class="t-time">Tiempo: 2 min</div>
    '''
})

# ── 6. ROADMAP DE LA ASIGNATURA ───────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">Tu roadmap de <span class="gradient-text">12 semanas</span></h1>
    <p class="s-lead">Un viaje progresivo: cada unidad construye sobre la anterior hasta tener una aplicación completa.</p>
    <div class="roadmap-h">
      <div class="rm-step"><div class="rm-num">01</div><div class="rm-info"><strong>Unidad 1</strong><span>Frameworks Modernos</span><span class="rm-w">10%</span></div></div>
      <div class="rm-arrow"><i data-lucide="chevron-right"></i></div>
      <div class="rm-step"><div class="rm-num">02</div><div class="rm-info"><strong>Unidad 2</strong><span>Base de Datos</span><span class="rm-w">20%</span></div></div>
      <div class="rm-arrow"><i data-lucide="chevron-right"></i></div>
      <div class="rm-step"><div class="rm-num">03</div><div class="rm-info"><strong>Unidad 3</strong><span>CRUD</span><span class="rm-w">30%</span></div></div>
      <div class="rm-arrow"><i data-lucide="chevron-right"></i></div>
      <div class="rm-step final"><div class="rm-num"><i data-lucide="trophy"></i></div><div class="rm-info"><strong>Examen Final</strong><span>Caso Integrador</span><span class="rm-w">40%</span></div></div>
    </div>
    <p class="s-note">Cada unidad tiene su propia evaluación con rúbrica detallada que revisaremos juntos antes de cada prueba.</p>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«Este es el mapa completo del curso. Fíjense que está diseñado como una escalera: cada unidad construye sobre lo aprendido en la anterior.»</li>
    <li>«En la Unidad 1 aprenderemos los fundamentos: qué es un framework, cómo funciona MVC, y crearemos nuestras primeras rutas y controladores.»</li>
    <li>«En la Unidad 2 conectaremos nuestra app con una base de datos real y le agregaremos seguridad.»</li>
    <li>«En la Unidad 3 implementaremos las 4 operaciones fundamentales: Crear, Leer, Actualizar y Eliminar datos.»</li>
    <li>«El examen final vale el 40% y es un caso práctico donde integran todo lo aprendido.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>Los porcentajes están diseñados intencionalmente: 10-20-30-40. Cada evaluación vale más que la anterior porque los contenidos son acumulativos. Si dominan bien la Unidad 1, las siguientes serán más fáciles.</p>
    <div class="t-time">Tiempo: 3 min</div>
    '''
})

# ── 7. PREVIEW UNIDAD 1 ──────────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <div class="unit-badge u1">Unidad 1 · Semanas 2-4</div>
    <h1 class="s-title">Introducción a los <span class="gradient-text">Frameworks Modernos</span></h1>
    <div class="s-cards four">
      <div class="s-card"><div class="s-card-icon"><i data-lucide="blocks"></i></div><h3>Arquitectura del Framework</h3><p>Estructura de directorios y organización del proyecto Laravel</p></div>
      <div class="s-card"><div class="s-card-icon"><i data-lucide="settings-2"></i></div><h3>Configuración</h3><p>Archivos .env, service providers y configuración inicial</p></div>
      <div class="s-card"><div class="s-card-icon"><i data-lucide="puzzle"></i></div><h3>Patrones de Diseño</h3><p>MVC, Repository Pattern y principios SOLID aplicados</p></div>
      <div class="s-card"><div class="s-card-icon"><i data-lucide="component"></i></div><h3>Modularidad</h3><p>Componentes reutilizables, Blade components y layouts</p></div>
    </div>
    <div class="eval-preview"><i data-lucide="file-check"></i> <strong>Evaluación 1 (10%):</strong> Caso «Software de Gestión de Proyectos» — Rutas, controladores, modelos y vistas.</div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«La Unidad 1 es la base de todo. Si entienden bien cómo funciona la arquitectura de Laravel, el resto del curso será mucho más fluido.»</li>
    <li>«Aprenderemos a crear rutas (las URLs de nuestra app), controladores (la lógica) y vistas (lo que ve el usuario).»</li>
    <li>«La evaluación será en la semana 4 y es grupal — máximo 3 integrantes. El caso será crear las rutas y vistas de un sistema de gestión de proyectos.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>Laravel sigue una filosofía llamada «Convention over Configuration»: si sigues las convenciones del framework, casi todo funciona automáticamente. Esto reduce enormemente el código que necesitas escribir.</p>
    <div class="t-time">Tiempo: 2 min</div>
    '''
})

# ── 8. PREVIEW UNIDAD 2 ──────────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <div class="unit-badge u2">Unidad 2 · Semanas 5-7</div>
    <h1 class="s-title">Base de Datos y <span class="gradient-text">Seguridad</span></h1>
    <div class="s-cards four">
      <div class="s-card"><div class="s-card-icon"><i data-lucide="database"></i></div><h3>ORM (Eloquent)</h3><p>Mapeo objeto-relacional: interactúa con la BD usando objetos PHP</p></div>
      <div class="s-card"><div class="s-card-icon"><i data-lucide="link"></i></div><h3>Conexión BD</h3><p>Configuración de MySQL/PostgreSQL con migraciones y seeders</p></div>
      <div class="s-card"><div class="s-card-icon"><i data-lucide="lock"></i></div><h3>Autenticación</h3><p>Login, registro, guards y middleware de autenticación</p></div>
      <div class="s-card"><div class="s-card-icon"><i data-lucide="key-round"></i></div><h3>Cifrado</h3><p>Hashing de contraseñas, cifrado de datos en reposo con bcrypt</p></div>
    </div>
    <div class="eval-preview"><i data-lucide="file-check"></i> <strong>Evaluación 2 (20%):</strong> ORM, autenticación, autorización y cifrado de datos.</div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«En la Unidad 2, nuestra aplicación dejará de usar datos estáticos y empezará a trabajar con una base de datos real.»</li>
    <li>«Eloquent ORM es una de las joyas de Laravel: les permite interactuar con la base de datos usando código PHP elegante, sin escribir SQL crudo.»</li>
    <li>«También veremos seguridad: cómo proteger nuestra app con login, permisos y cifrado de datos sensibles.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>El 95% de los ciberataques a aplicaciones web se deben a vulnerabilidades básicas como inyección SQL y contraseñas sin cifrar. Laravel resuelve ambos problemas de forma automática si usas Eloquent y el sistema de hashing integrado.</p>
    <div class="t-time">Tiempo: 2 min</div>
    '''
})

# ── 9. PREVIEW UNIDAD 3 ──────────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <div class="unit-badge u3">Unidad 3 · Semanas 8-10</div>
    <h1 class="s-title">Operaciones <span class="gradient-text">CRUD</span></h1>
    <div class="crud-grid">
      <div class="crud-item create"><div class="crud-letter">C</div><div><strong>Create</strong><p>Insertar nuevos registros en la base de datos</p></div></div>
      <div class="crud-item read"><div class="crud-letter">R</div><div><strong>Read</strong><p>Recuperar y listar datos existentes</p></div></div>
      <div class="crud-item update"><div class="crud-letter">U</div><div><strong>Update</strong><p>Actualizar registros existentes</p></div></div>
      <div class="crud-item delete"><div class="crud-letter">D</div><div><strong>Delete</strong><p>Eliminar registros de forma segura</p></div></div>
    </div>
    <div class="eval-preview"><i data-lucide="file-check"></i> <strong>Evaluación 3 (30%):</strong> Aplicación completa con CRUD funcional, seguro y eficiente.</div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«CRUD es el acrónimo que todo desarrollador debe conocer: Create, Read, Update, Delete. Son las 4 operaciones fundamentales de cualquier aplicación que trabaja con datos.»</li>
    <li>«Piensen en cualquier app que usen: crear una publicación en Instagram (Create), ver el feed (Read), editar un comentario (Update), borrar una foto (Delete). Todo es CRUD.»</li>
    <li>«Esta unidad vale el 30% porque es donde todo se junta: rutas + controladores + modelos + vistas + base de datos + seguridad.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>Se estima que el 80% de todas las aplicaciones web del mundo son esencialmente CRUD con una interfaz bonita. Si dominan CRUD, dominan la base del desarrollo web.</p>
    <div class="t-time">Tiempo: 2 min</div>
    '''
})

# ── 10. EXAMEN FINAL ──────────────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <div class="unit-badge uf">Semana 12 · Examen Transversal</div>
    <h1 class="s-title">Examen <span class="gradient-text">Final</span></h1>
    <p class="s-lead">Un caso práctico integrador que evalúa todas las competencias desarrolladas a lo largo del curso.</p>
    <div class="s-split">
      <div class="s-left">
        <div class="final-box">
          <div class="final-pct">40<span>%</span></div>
          <p>del total de la asignatura</p>
        </div>
      </div>
      <div class="s-right">
        <h3>¿Qué se evaluará?</h3>
        <ul class="s-list">
          <li><i data-lucide="check-circle"></i> Arquitectura MVC correcta</li>
          <li><i data-lucide="check-circle"></i> Rutas RESTful y controladores</li>
          <li><i data-lucide="check-circle"></i> Modelos con Eloquent ORM</li>
          <li><i data-lucide="check-circle"></i> Autenticación y seguridad</li>
          <li><i data-lucide="check-circle"></i> CRUD completo y funcional</li>
          <li><i data-lucide="check-circle"></i> Interfaz de usuario con Blade</li>
        </ul>
      </div>
    </div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«El examen final vale el 40% y será un caso práctico integrador. Recibirán un requerimiento y tendrán que construir la aplicación completa.»</li>
    <li>«No se asusten con el porcentaje. Si han trabajado bien durante las 3 unidades, el examen será una síntesis natural de todo lo aprendido.»</li>
    <li>«Recuerden: la nota 4.0 se obtiene con un 60% de exigencia. No necesitan la perfección, necesitan demostrar dominio.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>En semestres anteriores, los estudiantes que asistieron a todas las clases y entregaron las 3 evaluaciones parciales obtuvieron en promedio un 85% en el examen final. La consistencia durante el curso es la mejor preparación.</p>
    <div class="t-time">Tiempo: 2 min</div>
    '''
})

# ── 11. ¿QUÉ ES UN FRAMEWORK? ─────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">¿Qué es un <span class="gradient-text">Framework</span>?</h1>
    <p class="s-lead">Una analogía simple: construir una casa.</p>
    <div class="s-split compare">
      <div class="s-left">
        <div class="compare-box bad">
          <div class="compare-header"><i data-lucide="hammer"></i> Sin Framework</div>
          <ul>
            <li>Fabricas tus propios ladrillos</li>
            <li>Diseñas cada tubo de cañería</li>
            <li>Inventas tu propio sistema eléctrico</li>
            <li>Resuelves problemas ya resueltos</li>
            <li>Meses de trabajo extra</li>
          </ul>
        </div>
      </div>
      <div class="s-right">
        <div class="compare-box good">
          <div class="compare-header"><i data-lucide="building-2"></i> Con Framework</div>
          <ul>
            <li>Usas materiales estandarizados</li>
            <li>Plomería pre-fabricada e instalable</li>
            <li>Sistema eléctrico certificado</li>
            <li>Te enfocas en el diseño único</li>
            <li>Entregas en semanas, no meses</li>
          </ul>
        </div>
      </div>
    </div>
    <p class="s-note">Un framework te da la estructura base para que te enfoques en lo que hace única a tu aplicación, no en reinventar la rueda.</p>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«Imaginen que quieren construir una casa. Tienen dos opciones: fabricar cada ladrillo ustedes mismos, o usar materiales pre-fabricados y enfocarse en el diseño.»</li>
    <li>«Un framework es exactamente eso: un conjunto de herramientas, convenciones y código pre-escrito que resuelve los problemas comunes del desarrollo web.»</li>
    <li>«Cosas como conectarse a una base de datos, manejar sesiones de usuario, procesar formularios — todo eso ya está resuelto. Ustedes solo se enfocan en la lógica específica de su aplicación.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>Facebook empezó sin framework (PHP puro) y eventualmente tuvo que crear su propio framework (Hack/HHVM) porque el código se volvió inmanejable. Si hubieran empezado con un framework, habrían ahorrado años de refactoring. La lección: usar un framework desde el inicio ahorra dolor a largo plazo.</p>
    <div class="t-time">Tiempo: 3 min</div>
    '''
})

# ── 12. PANORAMA DE FRAMEWORKS PHP ────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">Panorama de <span class="gradient-text">Frameworks PHP</span></h1>
    <p class="s-lead">Los 3 principales frameworks PHP en 2026 y para qué es mejor cada uno.</p>
    <table class="s-table">
      <thead><tr><th>Framework</th><th>Ideal para</th><th>Filosofía</th><th>Curva de aprendizaje</th></tr></thead>
      <tbody>
        <tr class="row-highlight"><td><strong>Laravel</strong></td><td>SaaS, Startups, Apps rápidas</td><td>«Batteries-included»</td><td>Media</td></tr>
        <tr><td><strong>Symfony</strong></td><td>Empresas grandes, sistemas complejos</td><td>Componentes modulares</td><td>Alta</td></tr>
        <tr><td><strong>CodeIgniter</strong></td><td>Apps ligeras, MVPs rápidos</td><td>Minimalismo</td><td>Baja</td></tr>
      </tbody>
    </table>
    <p class="s-note">Laravel usa internamente muchos componentes de Symfony. No son competidores directos — son herramientas para diferentes contextos.</p>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«En el mundo PHP hay tres frameworks principales. Cada uno tiene su lugar y su audiencia.»</li>
    <li>«Laravel es el líder para startups y productos SaaS porque permite desarrollar rápido. Viene con todo lo necesario incluido.»</li>
    <li>«Symfony es la opción enterprise: más control, más estabilidad, pero más complejo de configurar.»</li>
    <li>«CodeIgniter es el minimalista: muy rápido de aprender pero le faltan las herramientas avanzadas de los otros dos.»</li>
    <li>«Dato curioso: Laravel usa componentes de Symfony internamente. Aprender Laravel también les da exposición a Symfony.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>En las ofertas laborales de Chile y Latinoamérica, Laravel aparece en el 65% de las vacantes PHP, seguido por Symfony con un 20% y CodeIgniter con un 8%. Aprender Laravel les abre la mayor cantidad de puertas laborales.</p>
    <div class="t-time">Tiempo: 2-3 min</div>
    '''
})

# ── 13. ¿POR QUÉ LARAVEL? ─────────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">¿Por qué <span class="gradient-text">Laravel</span>?</h1>
    <p class="s-lead">5 razones por las que Laravel es la mejor elección para aprender desarrollo web moderno.</p>
    <div class="reasons-list">
      <div class="reason"><span class="reason-num">01</span><div><strong>Sintaxis Elegante y Expresiva</strong><p>Código limpio y legible que se lee casi como inglés. Ideal para aprender buenas prácticas.</p></div></div>
      <div class="reason"><span class="reason-num">02</span><div><strong>Ecosistema Completo</strong><p>Forge, Vapor, Cashier, Reverb — herramientas oficiales para cada necesidad.</p></div></div>
      <div class="reason"><span class="reason-num">03</span><div><strong>Comunidad Masiva</strong><p>Documentación excelente, miles de tutoriales, Laracasts, y soporte activo en foros.</p></div></div>
      <div class="reason"><span class="reason-num">04</span><div><strong>Demanda Laboral</strong><p>El framework PHP más solicitado en ofertas de empleo en toda Latinoamérica.</p></div></div>
      <div class="reason"><span class="reason-num">05</span><div><strong>Evolución Constante</strong><p>Versiones anuales con mejoras significativas. Laravel 13 incluye IA nativa y Passkeys.</p></div></div>
    </div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«Vamos a repasar las 5 razones principales por las que elegimos Laravel para este curso.»</li>
    <li>«La primera es la sintaxis: Laravel se diseñó para que el código sea legible. Esto no solo es bonito — reduce errores y facilita el trabajo en equipo.»</li>
    <li>«La segunda es el ecosistema: Laravel no es solo un framework, es una plataforma completa con herramientas para despliegue, pagos, websockets y más.»</li>
    <li>«La tercera razón es práctica: la comunidad es enorme. Si se atascan con algo, hay miles de respuestas en Stack Overflow y Laracasts.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>Laracasts.com (la plataforma de video-tutoriales de Laravel) tiene más de 2 millones de usuarios registrados y es considerada una de las mejores plataformas de educación de programación del mundo. Su creador, Jeffrey Way, ha enseñado Laravel a más personas que cualquier universidad.</p>
    <div class="t-time">Tiempo: 3 min</div>
    '''
})

# ── 14. LARAVEL EN 2026 ──────────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">Laravel en <span class="gradient-text">2026</span></h1>
    <p class="s-lead">Lo último en el framework que usaremos. Laravel evoluciona cada año con mejoras significativas.</p>
    <div class="s-cards three">
      <div class="s-card glow"><div class="s-card-icon"><i data-lucide="brain"></i></div><h3>AI SDK Nativo</h3><p>SDK de IA integrado y estable: generación de texto, embeddings y tool-calling directamente desde Laravel.</p></div>
      <div class="s-card glow"><div class="s-card-icon"><i data-lucide="zap"></i></div><h3>Laravel Octane</h3><p>Rendimiento extremo con procesos de larga duración. Compite con Go y Node.js en velocidad.</p></div>
      <div class="s-card glow"><div class="s-card-icon"><i data-lucide="fingerprint"></i></div><h3>Passkeys</h3><p>Autenticación sin contraseñas. Soporte nativo para la tecnología que reemplazará las passwords.</p></div>
    </div>
    <div class="version-info">
      <div class="ver-row"><span class="ver-label">Versión actual:</span><span class="ver-value">Laravel 13 (marzo 2026)</span></div>
      <div class="ver-row"><span class="ver-label">PHP mínimo:</span><span class="ver-value">8.3+</span></div>
      <div class="ver-row"><span class="ver-label">Soporte:</span><span class="ver-value">Bug fixes hasta Q3 2027 · Security hasta marzo 2028</span></div>
    </div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«Laravel no es un framework estancado. Cada año lanza una versión mayor con mejoras significativas.»</li>
    <li>«En 2026, las tres novedades más importantes son: el SDK de IA integrado, Octane para alto rendimiento, y Passkeys para autenticación moderna.»</li>
    <li>«El AI SDK les permite integrar inteligencia artificial directamente en sus aplicaciones Laravel sin instalar librerías externas. Esto hubiera sido ciencia ficción hace 3 años.»</li>
    <li>«Nosotros trabajaremos con los fundamentos que no cambian entre versiones: MVC, Eloquent, Blade. Estos conceptos son transferibles a cualquier versión.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>Laravel Octane permite que una aplicación Laravel maneje hasta 10.000 peticiones por segundo en un solo servidor. Para contexto, la mayoría de las aplicaciones web reciben menos de 100 peticiones por segundo. Es como tener un Ferrari para ir al supermercado, pero está bien tenerlo disponible.</p>
    <div class="t-time">Tiempo: 3 min</div>
    '''
})

# ── 15. ARQUITECTURA MVC ─────────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">Arquitectura <span class="gradient-text">MVC</span></h1>
    <p class="s-lead">El patrón Modelo-Vista-Controlador es el corazón de Laravel y de la mayoría de frameworks modernos.</p>
    <div class="mvc-diagram">
      <div class="mvc-box mvc-user"><i data-lucide="user"></i><span>Usuario</span></div>
      <div class="mvc-arrow right"><i data-lucide="arrow-right"></i><label>Request</label></div>
      <div class="mvc-box mvc-controller"><i data-lucide="settings-2"></i><span>Controller</span><small>Lógica de negocio</small></div>
      <div class="mvc-arrow right"><i data-lucide="arrow-right"></i><label>Consulta</label></div>
      <div class="mvc-box mvc-model"><i data-lucide="database"></i><span>Model</span><small>Datos (Eloquent)</small></div>
      <div class="mvc-arrow left"><i data-lucide="arrow-left"></i><label>Datos</label></div>
      <div class="mvc-box mvc-view"><i data-lucide="layout-template"></i><span>View</span><small>Interfaz (Blade)</small></div>
      <div class="mvc-arrow left"><i data-lucide="arrow-left"></i><label>Response</label></div>
    </div>
    <div class="mvc-summary">
      <div class="mvc-s"><strong>Model:</strong> Gestiona los datos y la lógica de negocio (Eloquent ORM)</div>
      <div class="mvc-s"><strong>View:</strong> Presenta la información al usuario (Blade Templates)</div>
      <div class="mvc-s"><strong>Controller:</strong> Coordina Model y View, procesa las solicitudes</div>
    </div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«MVC es el patrón de diseño más importante que aprenderán en este curso. Separa la aplicación en tres capas con responsabilidades distintas.»</li>
    <li>«Piénsenlo como un restaurante: el Modelo es la cocina (donde se preparan los datos), la Vista es el plato que llega a la mesa (lo que ve el cliente), y el Controller es el mesero (coordina los pedidos entre la cocina y la mesa).»</li>
    <li>«La ventaja principal es la separación de responsabilidades: pueden cambiar la interfaz sin tocar la lógica, o cambiar la base de datos sin afectar las vistas.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>El patrón MVC fue inventado en 1979 por Trygve Reenskaug para Smalltalk. Tiene más de 45 años y sigue siendo el patrón dominante en desarrollo web. Es tan fundamental que entenderlo les servirá sin importar qué lenguaje o framework usen en el futuro.</p>
    <div class="t-time">Tiempo: 4 min</div>
    '''
})

# ── 16. ECOSISTEMA LARAVEL ────────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">El Ecosistema <span class="gradient-text">Laravel</span></h1>
    <p class="s-lead">Laravel no es solo un framework — es una plataforma completa con herramientas para cada etapa del desarrollo.</p>
    <div class="s-cards three">
      <div class="s-card"><div class="s-card-icon"><i data-lucide="server"></i></div><h3>Forge</h3><p>Despliegue automático en servidores cloud (AWS, DigitalOcean)</p></div>
      <div class="s-card"><div class="s-card-icon"><i data-lucide="cloud"></i></div><h3>Vapor</h3><p>Despliegue serverless en AWS Lambda sin gestionar servidores</p></div>
      <div class="s-card"><div class="s-card-icon"><i data-lucide="radio"></i></div><h3>Reverb</h3><p>WebSockets nativos para aplicaciones en tiempo real</p></div>
      <div class="s-card"><div class="s-card-icon"><i data-lucide="credit-card"></i></div><h3>Cashier</h3><p>Integración con Stripe/Paddle para cobros y suscripciones</p></div>
      <div class="s-card"><div class="s-card-icon"><i data-lucide="telescope"></i></div><h3>Telescope</h3><p>Dashboard de debugging para monitorear requests, queries y logs</p></div>
      <div class="s-card"><div class="s-card-icon"><i data-lucide="wind"></i></div><h3>Breeze / Jetstream</h3><p>Starter kits con autenticación, registro y dashboard listos</p></div>
    </div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«Una de las mayores fortalezas de Laravel es su ecosistema. No solo te da un framework — te da un conjunto completo de herramientas para cada necesidad.»</li>
    <li>«Forge y Vapor son para despliegue: pones tu app en producción con un par de clicks.»</li>
    <li>«Reverb es para tiempo real: chat en vivo, notificaciones push, actualizaciones instantáneas.»</li>
    <li>«No usaremos todas estas herramientas en el curso, pero es importante que sepan que existen. Cuando las necesiten en un trabajo real, ya sabrán dónde buscar.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>Taylor Otwell (creador de Laravel) convirtió el ecosistema Laravel en un negocio multimillonario. Forge y Vapor son servicios de pago que generan millones de dólares al año. Esto garantiza que Laravel tiene financiamiento a largo plazo — no va a desaparecer.</p>
    <div class="t-time">Tiempo: 2-3 min</div>
    '''
})

# ── 17. HERRAMIENTAS DEL DESARROLLADOR ────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">Las herramientas del <span class="gradient-text">desarrollador</span></h1>
    <p class="s-lead">El stack que usaremos durante todo el curso. Asegúrate de tener todo instalado.</p>
    <div class="tools-showcase">
      <div class="tool-item"><div class="tool-icon-big"><i data-lucide="braces"></i></div><div class="tool-detail"><h3>PHP 8.3+</h3><p>El lenguaje base. Laravel 13 requiere PHP 8.3 como mínimo para aprovechar las últimas optimizaciones del lenguaje.</p></div></div>
      <div class="tool-item"><div class="tool-icon-big"><i data-lucide="package"></i></div><div class="tool-detail"><h3>Composer</h3><p>El gestor de dependencias de PHP. Piénsenlo como el «npm» del mundo PHP. Instala y actualiza librerías automáticamente.</p></div></div>
      <div class="tool-item"><div class="tool-icon-big"><i data-lucide="rocket"></i></div><div class="tool-detail"><h3>Laravel Installer</h3><p>Herramienta CLI para crear proyectos Laravel nuevos con un solo comando: <code>laravel new mi-proyecto</code></p></div></div>
      <div class="tool-item"><div class="tool-icon-big"><i data-lucide="monitor"></i></div><div class="tool-detail"><h3>Visual Studio Code</h3><p>IDE recomendado con extensiones para PHP, Laravel Blade, autocompletado inteligente y depuración.</p></div></div>
    </div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«Estas son las 4 herramientas que necesitarán instaladas en su computador para la próxima clase. Vamos a revisarlas una por una.»</li>
    <li>«PHP 8.3 es el lenguaje base. Si ya tienen PHP instalado, verifiquen la versión con php -v en la terminal.»</li>
    <li>«Composer es como npm para Node o pip para Python: gestiona las dependencias de sus proyectos PHP.»</li>
    <li>«VS Code es gratuito y tiene extensiones excelentes para Laravel. Les recomiendo instalar: PHP Intelephense, Laravel Blade Snippets y DotENV.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>VS Code es el IDE más popular del mundo con más del 70% de cuota de mercado entre desarrolladores. Fue creado por Microsoft usando TypeScript y Electron, y es completamente gratuito y open source.</p>
    <div class="t-time">Tiempo: 3 min</div>
    '''
})

# ── 18. INSTALACIÓN PASO A PASO ──────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">¿Cómo instalo <span class="gradient-text">todo</span>?</h1>
    <p class="s-lead">Guía rápida de instalación para tu sistema operativo.</p>
    <div class="install-steps">
      <div class="install-step"><span class="step-num">1</span><div><strong>Instalar PHP 8.3+</strong><p>Windows: descarga XAMPP o Laragon &middot; macOS: <code>brew install php</code> &middot; Linux: <code>sudo apt install php</code></p></div></div>
      <div class="install-step"><span class="step-num">2</span><div><strong>Instalar Composer</strong><p>Visita <code>getcomposer.org</code> y sigue las instrucciones para tu SO. Verifica con: <code>composer --version</code></p></div></div>
      <div class="install-step"><span class="step-num">3</span><div><strong>Instalar Laravel</strong><p>Ejecuta: <code>composer global require laravel/installer</code> y luego <code>laravel new mi-proyecto</code></p></div></div>
      <div class="install-step"><span class="step-num">4</span><div><strong>Verificar</strong><p>Entra a la carpeta del proyecto y ejecuta: <code>php artisan serve</code>. Visita <code>localhost:8000</code> en tu navegador.</p></div></div>
    </div>
    <div class="s-note">Si tienes problemas con la instalación, trae tus dudas a la próxima clase sincrónica. Lo resolveremos juntos.</div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«No se preocupen si la instalación parece complicada. Es un proceso que se hace una sola vez y luego pueden crear proyectos infinitos.»</li>
    <li>«Para Windows, la opción más fácil es Laragon — es un entorno de desarrollo que instala PHP, MySQL y Apache automáticamente.»</li>
    <li>«Para macOS, Homebrew hace todo muy simple con un solo comando.»</li>
    <li>«Si tienen problemas, tomen nota y lo resolvemos en la próxima clase sincrónica. También hay guías paso a paso en la plataforma EVA.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>El comando php artisan serve levanta un servidor de desarrollo local. «Artisan» es el nombre que Laravel le da a su herramienta de línea de comandos. Artisan puede generar código automáticamente, ejecutar migraciones de base de datos, limpiar caché y mucho más. Es como tener un asistente personal de desarrollo.</p>
    <div class="t-time">Tiempo: 3 min</div>
    '''
})

# ── 19. METODOLOGÍA ───────────────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">Nuestra <span class="gradient-text">metodología</span></h1>
    <p class="s-lead">Aprendizaje Basado en Casos: ustedes son los protagonistas de su aprendizaje.</p>
    <div class="s-cards four">
      <div class="s-card"><div class="s-card-icon"><i data-lucide="presentation"></i></div><h3>Clases Teóricas</h3><p>Conceptos fundamentales presentados de forma clara y estructurada</p></div>
      <div class="s-card"><div class="s-card-icon"><i data-lucide="terminal"></i></div><h3>Ejercicios Prácticos</h3><p>Aplicación inmediata de conceptos en laboratorio con casos reales</p></div>
      <div class="s-card"><div class="s-card-icon"><i data-lucide="git-branch"></i></div><h3>Desarrollo Progresivo</h3><p>Construcción incremental de una aplicación a lo largo del curso</p></div>
      <div class="s-card"><div class="s-card-icon"><i data-lucide="message-circle"></i></div><h3>Retroalimentación</h3><p>Feedback constante para orientar su aprendizaje y resolver dudas</p></div>
    </div>
    <p class="s-note">Cada unidad sigue el ciclo: Teoría &rarr; Práctica &rarr; Retroalimentación &rarr; Evaluación</p>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«No vamos a hacer clases donde yo hablo 2 horas y ustedes copian. Este curso es práctico: la mayor parte del tiempo van a estar escribiendo código.»</li>
    <li>«Usaremos Aprendizaje Basado en Casos: cada concepto nuevo lo aplicaremos inmediatamente a un caso real. Aprenderán haciendo.»</li>
    <li>«El ciclo de cada unidad es: primero vemos la teoría, luego la practicamos, reciben retroalimentación, y finalmente hacen la evaluación. Sin sorpresas.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>Estudios en educación de programación demuestran que los estudiantes que practican código inmediatamente después de ver un concepto retienen 3 veces más que los que solo ven la teoría. Por eso cada clase tiene un componente práctico obligatorio.</p>
    <div class="t-time">Tiempo: 2 min</div>
    '''
})

# ── 20. SISTEMA DE EVALUACIÓN ─────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">Sistema de <span class="gradient-text">evaluación</span></h1>
    <p class="s-lead">Todas las evaluaciones son desarrollo de casos aplicados con rúbrica detallada.</p>
    <div class="eval-donut-container">
      <div class="eval-donut">
        <svg viewBox="0 0 200 200" class="donut-svg">
          <circle cx="100" cy="100" r="80" fill="none" stroke="rgba(255,255,255,0.05)" stroke-width="24"/>
          <circle cx="100" cy="100" r="80" fill="none" stroke="#FF4500" stroke-width="24" stroke-dasharray="50.3 452.4" stroke-dashoffset="0" transform="rotate(-90 100 100)"/>
          <circle cx="100" cy="100" r="80" fill="none" stroke="#FF7A33" stroke-width="24" stroke-dasharray="100.5 402.1" stroke-dashoffset="-50.3" transform="rotate(-90 100 100)"/>
          <circle cx="100" cy="100" r="80" fill="none" stroke="#FFB347" stroke-width="24" stroke-dasharray="150.8 351.9" stroke-dashoffset="-150.8" transform="rotate(-90 100 100)"/>
          <circle cx="100" cy="100" r="80" fill="none" stroke="#FFCF70" stroke-width="24" stroke-dasharray="201 301.6" stroke-dashoffset="-301.6" transform="rotate(-90 100 100)"/>
        </svg>
        <div class="donut-center">60%<br><small>exigencia</small></div>
      </div>
      <div class="eval-legend">
        <div class="legend-item"><span class="legend-dot" style="background:#FF4500"></span>Eval 1: Frameworks (10%)</div>
        <div class="legend-item"><span class="legend-dot" style="background:#FF7A33"></span>Eval 2: BD y Seguridad (20%)</div>
        <div class="legend-item"><span class="legend-dot" style="background:#FFB347"></span>Eval 3: CRUD (30%)</div>
        <div class="legend-item"><span class="legend-dot" style="background:#FFCF70"></span>Examen Final (40%)</div>
      </div>
    </div>
    <p class="s-note">La nota 4.0 se obtiene con un 60% de exigencia. Todas las evaluaciones se acompañan de rúbrica.</p>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«Veamos cómo se distribuye la nota final. El gráfico lo dice todo: 10%, 20%, 30% y 40%.»</li>
    <li>«Noten que el peso aumenta con cada evaluación. Esto es intencional: los contenidos son acumulativos y cada evaluación incluye lo anterior.»</li>
    <li>«La nota 4.0 se obtiene con un 60% de exigencia. Esto significa que no necesitan la perfección, pero sí necesitan demostrar que dominan los conceptos.»</li>
    <li>«Cada evaluación viene con una rúbrica detallada que revisaremos ANTES de la prueba. No habrá sorpresas. Sabrán exactamente qué se evalúa y cómo.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>Las rúbricas son sus mejores aliadas. En semestres anteriores, los estudiantes que revisaron la rúbrica antes de la evaluación obtuvieron en promedio 1 punto más que los que no lo hicieron. Es literalmente un mapa del tesoro que les dice dónde están los puntos.</p>
    <div class="t-time">Tiempo: 3 min</div>
    '''
})

# ── 21. CALENDARIO DEL TRIMESTRE ──────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">Calendario del <span class="gradient-text">trimestre</span></h1>
    <p class="s-lead">2° Trimestre 2026 · Modalidad Online · 12 semanas</p>
    <div class="cal-mini">
      <div class="cal-row cal-header"><span>Sem</span><span>Fecha</span><span>Actividad</span><span>Tipo</span></div>
      <div class="cal-row"><span>1</span><span>30 jun</span><span>Bienvenida · Inicio U1</span><span class="tag-sync">Sinc</span></div>
      <div class="cal-row"><span>2</span><span>06 jul</span><span>Revisión RDD U1 · Foro</span><span class="tag-async">Asinc</span></div>
      <div class="cal-row"><span>3</span><span>13 jul</span><span>Retroalimentación RDD 1</span><span class="tag-sync">Sinc</span></div>
      <div class="cal-row cal-eval"><span>4</span><span>17 jul</span><span>EVALUACIÓN 1</span><span class="tag-async">Asinc</span></div>
      <div class="cal-row"><span>5</span><span>27 jul</span><span>Retro Eval 1 · Inicio U2</span><span class="tag-sync">Sinc</span></div>
      <div class="cal-row"><span>6</span><span>03 ago</span><span>Retroalimentación RDD 2</span><span class="tag-sync">Sinc</span></div>
      <div class="cal-row cal-eval"><span>7</span><span>07 ago</span><span>EVALUACIÓN 2</span><span class="tag-async">Asinc</span></div>
      <div class="cal-row"><span>8</span><span>17 ago</span><span>Retro Eval 2 · Inicio U3</span><span class="tag-sync">Sinc</span></div>
      <div class="cal-row"><span>9</span><span>24 ago</span><span>Retroalimentación RDD 3</span><span class="tag-sync">Sinc</span></div>
      <div class="cal-row cal-eval"><span>10</span><span>28 ago</span><span>EVALUACIÓN 3</span><span class="tag-async">Asinc</span></div>
      <div class="cal-row"><span>11</span><span>07 sep</span><span>Retro Eval 3 · Rev. Final</span><span class="tag-sync">Sinc</span></div>
      <div class="cal-row cal-final"><span>12</span><span>11 sep</span><span>EXAMEN FINAL</span><span class="tag-async">Asinc</span></div>
    </div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«Este es el calendario completo del trimestre. Les recomiendo que lo guarden o le saquen foto.»</li>
    <li>«Las semanas marcadas en naranja son evaluaciones. Fíjense que todas son asincrónicas — las subirán a la plataforma.»</li>
    <li>«Las clases sincrónicas son las semanas donde nos vemos en vivo. Las asincrónicas son para trabajo autónomo.»</li>
    <li>«Ojo con las fechas: entre las evaluaciones hay muy poco margen. No dejen las cosas para último momento.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>El trimestre tiene solo 12 semanas. Eso son 84 días. Si descuentan fines de semana, son 60 días de trabajo efectivo. La planificación es clave para no quedarse atrás.</p>
    <div class="t-time">Tiempo: 2-3 min</div>
    '''
})

# ── 22. LA RÚBRICA COMO ALIADA ────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">La rúbrica como <span class="gradient-text">aliada</span></h1>
    <p class="s-lead">La rúbrica no es un castigo — es un mapa que les dice exactamente cómo obtener la máxima nota.</p>
    <div class="s-split">
      <div class="s-left">
        <div class="rubric-example">
          <div class="rubric-header">Ejemplo de Criterio</div>
          <div class="rubric-criterion">
            <div class="rubric-name">Definición de Rutas</div>
            <div class="rubric-levels">
              <div class="rubric-level excellent"><span>Excelente (3)</span><p>Define todas las rutas RESTful correctamente</p></div>
              <div class="rubric-level good"><span>Bueno (2)</span><p>Define la mayoría de rutas con errores menores</p></div>
              <div class="rubric-level basic"><span>Básico (1)</span><p>Define pocas rutas o con errores significativos</p></div>
            </div>
          </div>
        </div>
      </div>
      <div class="s-right">
        <h3>Cómo usar la rúbrica</h3>
        <ul class="s-list">
          <li><i data-lucide="search"></i> Léela <strong>antes</strong> de empezar la evaluación</li>
          <li><i data-lucide="check-square"></i> Úsala como checklist mientras trabajas</li>
          <li><i data-lucide="star"></i> Apunta siempre al nivel «Excelente»</li>
          <li><i data-lucide="users"></i> Revisen el trabajo de su compañero con la rúbrica</li>
        </ul>
      </div>
    </div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«La rúbrica es literalmente un mapa del tesoro. Les dice exactamente qué necesitan hacer para obtener cada nivel de calificación.»</li>
    <li>«Mi consejo: antes de empezar cualquier evaluación, impriman la rúbrica y úsenla como checklist. Vayan marcando cada criterio a medida que lo completen.»</li>
    <li>«No hay secretos ni sorpresas. Todo lo que se evalúa está explícitamente descrito en la rúbrica.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>Un estudio de la Universidad de Stanford mostró que los estudiantes que usan la rúbrica como guía de auto-evaluación antes de entregar un trabajo obtienen calificaciones un 15% más altas en promedio. Es la herramienta más subutilizada por los estudiantes.</p>
    <div class="t-time">Tiempo: 2-3 min</div>
    '''
})

# ── 23. REGLAS DEL JUEGO ──────────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">Reglas del <span class="gradient-text">juego</span></h1>
    <p class="s-lead">Acuerdos claros para que el curso funcione bien para todos.</p>
    <div class="rules-grid">
      <div class="rule-item"><div class="rule-icon"><i data-lucide="calendar-check"></i></div><h3>Asistencia</h3><p>Las clases sincrónicas son importantes. La participación activa se refleja en la retroalimentación.</p></div>
      <div class="rule-item"><div class="rule-icon"><i data-lucide="clock"></i></div><h3>Entregas a tiempo</h3><p>Las evaluaciones tienen fecha límite estricta. Las entregas tardías pierden puntaje según rúbrica.</p></div>
      <div class="rule-item"><div class="rule-icon"><i data-lucide="users"></i></div><h3>Trabajo en equipo</h3><p>Las evaluaciones son grupales (máx. 3 integrantes). Todos deben contribuir equitativamente.</p></div>
      <div class="rule-item"><div class="rule-icon"><i data-lucide="shield-alert"></i></div><h3>Integridad académica</h3><p>El código copiado de otros grupos será evaluado con nota mínima. Usar IA está permitido como herramienta, no como reemplazo.</p></div>
    </div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«Vamos a establecer las reglas del juego para que todos estemos en la misma página.»</li>
    <li>«Las clases sincrónicas son donde resolvemos dudas y profundizamos en los temas. Les recomiendo asistir a todas.»</li>
    <li>«Las entregas tardías pierden puntaje. No hay excepciones salvo causas de fuerza mayor justificadas.»</li>
    <li>«Sobre integridad académica: pueden usar IA como herramienta de aprendizaje (para entender conceptos, depurar errores), pero no para que haga el trabajo por ustedes. Deben ser capaces de explicar cada línea de su código.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>En cursos anteriores, los casos de copia entre grupos se detectaron fácilmente comparando los commits de Git, los nombres de variables y los comentarios en el código. El código copiado siempre deja rastros evidentes. Es mucho más fácil (y útil) aprender a hacerlo ustedes mismos.</p>
    <div class="t-time">Tiempo: 2-3 min</div>
    '''
})

# ── 24. RECURSOS Y CANALES ────────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">Recursos y <span class="gradient-text">canales</span></h1>
    <p class="s-lead">Todo lo que necesitan está a un click de distancia.</p>
    <div class="s-cards three">
      <div class="s-card"><div class="s-card-icon"><i data-lucide="graduation-cap"></i></div><h3>EVA (Plataforma)</h3><p>Material del curso, apuntes, guías de ejercicios y entrega de evaluaciones.</p></div>
      <div class="s-card"><div class="s-card-icon"><i data-lucide="message-square"></i></div><h3>Foros</h3><p>Espacio para preguntas y discusión con compañeros y el profesor.</p></div>
      <div class="s-card"><div class="s-card-icon"><i data-lucide="book-open"></i></div><h3>Documentación Laravel</h3><p><code>laravel.com/docs</code> — la documentación oficial es excelente y será su referencia constante.</p></div>
    </div>
    <div class="resources-extra">
      <h3>Recursos complementarios recomendados</h3>
      <div class="resource-links">
        <div class="res-link"><i data-lucide="play-circle"></i> <strong>Laracasts.com</strong> — Video tutoriales de Laravel (muchos gratuitos)</div>
        <div class="res-link"><i data-lucide="file-text"></i> <strong>PHP The Right Way</strong> — Guía de buenas prácticas PHP</div>
        <div class="res-link"><i data-lucide="github"></i> <strong>GitHub</strong> — Control de versiones y portafolio de proyectos</div>
      </div>
    </div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«Todo el material oficial del curso está en la plataforma EVA. Ahí encontrarán los apuntes, guías de ejercicios y las instrucciones de cada evaluación.»</li>
    <li>«Los foros son su primer recurso para preguntas. Antes de escribirme directamente, publiquen en el foro — así la respuesta beneficia a todos.»</li>
    <li>«La documentación oficial de Laravel en laravel.com/docs es probablemente la mejor documentación de cualquier framework. Acostúmbrense a consultarla.»</li>
    <li>«Y si quieren ir más allá, Laracasts tiene cientos de video tutoriales — muchos son gratuitos.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>La documentación de Laravel es tan buena que muchos desarrolladores senior la consideran un modelo a seguir. Fue escrita por el propio Taylor Otwell y es actualizada con cada versión. Saber leer documentación técnica es una habilidad tan importante como saber escribir código.</p>
    <div class="t-time">Tiempo: 2 min</div>
    '''
})

# ── 25. TU PRIMERA MISIÓN ────────────────────────────────
S.append({
    'layout':'content',
    'content':'''
    <h1 class="s-title">Tu primera <span class="gradient-text">misión</span></h1>
    <p class="s-lead">Tareas para completar antes de la semana 2. Prepara tu entorno de desarrollo.</p>
    <div class="mission-list">
      <div class="mission-item"><div class="mission-check"><i data-lucide="square"></i></div><div class="mission-content"><strong>Instalar PHP 8.3+</strong><p>Windows: instala Laragon &middot; macOS: <code>brew install php</code></p></div></div>
      <div class="mission-item"><div class="mission-check"><i data-lucide="square"></i></div><div class="mission-content"><strong>Instalar Composer</strong><p>Descarga desde <code>getcomposer.org</code> y verifica con <code>composer -V</code></p></div></div>
      <div class="mission-item"><div class="mission-check"><i data-lucide="square"></i></div><div class="mission-content"><strong>Instalar Laravel</strong><p>Ejecuta <code>composer global require laravel/installer</code></p></div></div>
      <div class="mission-item"><div class="mission-check"><i data-lucide="square"></i></div><div class="mission-content"><strong>Crear un proyecto de prueba</strong><p>Ejecuta <code>laravel new prueba</code> y luego <code>php artisan serve</code></p></div></div>
      <div class="mission-item"><div class="mission-check"><i data-lucide="square"></i></div><div class="mission-content"><strong>Revisar el Apunte 1</strong><p>Disponible en la plataforma EVA. Lectura obligatoria para la semana 2.</p></div></div>
    </div>
    <p class="s-note">Si tienes problemas con la instalación, documéntalos y tráelos a la próxima clase sincrónica.</p>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«Esta es la tarea para la semana 2. No es opcional — necesitan tener el entorno listo para la próxima clase.»</li>
    <li>«El paso más importante es el número 4: crear un proyecto de prueba y verificar que se abre en el navegador. Si ven la página de bienvenida de Laravel, están listos.»</li>
    <li>«Si tienen problemas, NO se frustren. La instalación es la parte más tediosa del desarrollo. Una vez que funciona, no van a tener que hacerlo de nuevo.»</li>
    <li>«También les pido que lean el Apunte 1 en la plataforma. La próxima clase empezamos directo con la teoría de frameworks y MVC.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>En la industria, configurar el entorno de desarrollo se llama «setup hell» (el infierno de la configuración). Incluso desarrolladores con 10 años de experiencia a veces luchan con la instalación de herramientas nuevas. Es normal y no refleja su capacidad como programadores.</p>
    <div class="t-time">Tiempo: 3 min</div>
    '''
})

# ── 26. CIERRE MOTIVACIONAL ──────────────────────────────
S.append({
    'layout':'cover',
    'content':'''
    <div class="cover-badge"><span class="bdot"></span>Semana 2: Comenzamos con la Unidad 1</div>
    <h1 class="cover-title">¡Vamos a construir<br><span class="gradient-text">cosas increíbles</span>!</h1>
    <p class="cover-sub">Estoy aquí para apoyarlos en cada paso de este viaje de aprendizaje.</p>
    <div class="closing-message">
      <p>¿Alguna duda sobre la estructura, la metodología o las evaluaciones?</p>
      <p class="closing-small">Nos vemos en la Semana 2 para explorar los frameworks modernos y dar los primeros pasos con Laravel.</p>
    </div>
    ''',
    'teacher':'''
    <h4>Guión del Profesor</h4>
    <ol>
    <li>«Llegamos al final de la presentación de bienvenida. ¿Alguna pregunta sobre lo que hemos visto?»</li>
    <li>«Quiero que se vayan con una idea clara: este curso es práctico, progresivo y tiene soporte. No están solos.»</li>
    <li>«Recuerden la misión para la semana 2: instalar PHP, Composer, Laravel y leer el Apunte 1.»</li>
    <li>«Nos vemos en la próxima clase donde empezaremos con la Unidad 1: Introducción a los Frameworks Modernos. Ahí pondremos las manos en el código por primera vez.»</li>
    <li>Termina con: «¡Vamos a construir cosas increíbles juntos! Nos vemos la próxima semana.»</li>
    </ol>
    <h4>Anécdota Clave</h4>
    <p>Mark Zuckerberg, creador de Facebook, dijo: «La mayor parte del riesgo no viene de hacer algo mal, viene de no hacer nada.» Ustedes ya dieron el primer paso al inscribirse en este curso. Ahora solo queda construir.</p>
    <div class="t-time">Tiempo: 2-3 min</div>
    '''
})


# ═══════════════════════════════════════════════════════════
#  CSS
# ═══════════════════════════════════════════════════════════
CSS = """
*,*::before,*::after{margin:0;padding:0;box-sizing:border-box}
:root{
  --p:#FF4500;--p-glow:rgba(255,69,0,.35);--c2:#FF7A33;--c3:#FFB347;--c4:#FFCF70;
  --bg:#0A0E1A;--bg2:#0F1629;--bg3:#161D33;
  --surface:rgba(255,255,255,.04);--surface-h:rgba(255,255,255,.08);
  --border:rgba(255,255,255,.06);--border-h:rgba(255,255,255,.12);
  --text:#E8ECF4;--text2:#94A3B8;--text3:#64748B;
  --radius:16px;--radius-sm:10px;
  --font:'Inter',system-ui,sans-serif;--mono:'JetBrains Mono',monospace;
  font-size:16px;
}
html{scroll-behavior:smooth}
body{font-family:var(--font);background:var(--bg);color:var(--text);line-height:1.7;overflow:hidden;-webkit-font-smoothing:antialiased;height:100vh}
::selection{background:var(--p);color:#fff}
::-webkit-scrollbar{width:6px}::-webkit-scrollbar-track{background:var(--bg2)}::-webkit-scrollbar-thumb{background:var(--border);border-radius:3px}
a{color:var(--p);text-decoration:none}
code{font-family:var(--mono);background:rgba(255,69,0,.1);padding:.15em .4em;border-radius:4px;font-size:.85em;color:var(--c3)}

/* ── Gradient Text ── */
.gradient-text{background:linear-gradient(135deg,var(--p),var(--c2),var(--c3));-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}

/* ── Progress Bar ── */
.progress{position:fixed;top:0;left:0;right:0;height:3px;background:rgba(255,255,255,.05);z-index:500}
.progress-fill{height:100%;background:linear-gradient(90deg,var(--p),var(--c2),var(--c3));transition:width .4s ease;width:0}

/* ── Slide Container ── */
.slides{position:fixed;inset:0;overflow:hidden}
.slide{
  position:absolute;inset:0;display:flex;align-items:center;justify-content:center;
  padding:4rem 5rem;opacity:0;transform:translateX(50px);
  transition:opacity .5s ease,transform .5s ease;pointer-events:none;overflow-y:auto;
}
.slide.active{opacity:1;transform:translateX(0);pointer-events:all}
.slide.exit{opacity:0;transform:translateX(-50px)}

/* ── Slide Layouts ── */
.slide-inner{max-width:1100px;width:100%;position:relative}

/* Cover */
.cover{text-align:center;flex-direction:column}
.cover .slide-inner{display:flex;flex-direction:column;align-items:center;justify-content:center;min-height:60vh}
.cover-badge{display:inline-flex;align-items:center;gap:.5rem;background:var(--surface);border:1px solid var(--border);border-radius:50px;padding:.45rem 1rem;font-family:var(--mono);font-size:.72rem;color:var(--c3);margin-bottom:2rem}
.bdot{width:6px;height:6px;border-radius:50%;background:var(--p);animation:pulse 2s infinite}
.cover-title{font-size:clamp(2.5rem,6vw,4.5rem);font-weight:900;line-height:1.08;letter-spacing:-.03em;margin-bottom:1.5rem}
.cover-sub{font-size:1.2rem;color:var(--text2);margin-bottom:1.5rem}
.cover-inst{font-size:.85rem;color:var(--text3);font-weight:500}
.closing-message{margin-top:2rem;padding:2rem;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);max-width:600px}
.closing-message p{font-size:1rem;color:var(--text2)}
.closing-small{font-size:.85rem !important;color:var(--text3) !important;margin-top:.75rem}

/* Content */
.s-title{font-size:clamp(1.75rem,3.5vw,2.8rem);font-weight:800;line-height:1.15;letter-spacing:-.02em;margin-bottom:1rem}
.s-lead{font-size:1.05rem;color:var(--text2);margin-bottom:2rem;max-width:750px;line-height:1.7}
.s-note{font-size:.88rem;color:var(--text3);margin-top:1.5rem;padding:1rem;background:rgba(255,179,71,.05);border:1px solid rgba(255,179,71,.1);border-radius:var(--radius-sm);line-height:1.6}

/* Cards */
.s-cards{display:grid;gap:1rem;margin-top:1rem}
.s-cards.three{grid-template-columns:repeat(3,1fr)}
.s-cards.four{grid-template-columns:repeat(4,1fr)}
.s-card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1.5rem;transition:all .3s}
.s-card:hover{background:var(--surface-h);transform:translateY(-2px)}
.s-card.glow{border-color:rgba(255,69,0,.15)}
.s-card-icon{width:42px;height:42px;border-radius:12px;background:linear-gradient(135deg,rgba(255,69,0,.15),rgba(255,122,51,.08));border:1px solid rgba(255,69,0,.12);display:flex;align-items:center;justify-content:center;margin-bottom:.75rem}
.s-card-icon svg{width:20px;height:20px;color:var(--p)}
.s-card h3{font-size:.92rem;font-weight:700;margin-bottom:.35rem}
.s-card p{font-size:.82rem;color:var(--text2);line-height:1.5}

/* Split */
.s-split{display:grid;grid-template-columns:1fr 1fr;gap:2.5rem;align-items:start;margin-top:1.5rem}
.s-list{list-style:none;display:flex;flex-direction:column;gap:.75rem}
.s-list li{display:flex;align-items:center;gap:.75rem;font-size:.9rem;color:var(--text2)}
.s-list li svg{width:18px;height:18px;color:var(--p);flex-shrink:0}

/* Stats */
.s-stats{display:flex;gap:2.5rem;margin:2rem 0}
.s-stat{text-align:center}
.s-stat-val{display:block;font-size:2rem;font-weight:800;color:var(--p);font-family:var(--mono)}
.s-stat-lbl{font-size:.75rem;color:var(--text3);text-transform:uppercase;letter-spacing:1px}

/* Table */
.s-table{width:100%;border-collapse:collapse;font-size:.84rem;margin-top:1rem}
.s-table th{padding:.75rem 1rem;text-align:left;font-weight:600;color:var(--text2);border-bottom:2px solid var(--border);font-size:.75rem;text-transform:uppercase;letter-spacing:1px}
.s-table td{padding:.7rem 1rem;border-bottom:1px solid var(--border)}
.s-table .row-highlight{background:rgba(255,69,0,.06)}
.s-table .row-highlight td{color:var(--c2);font-weight:600}

/* Timeline */
.timeline{display:flex;flex-direction:column;gap:.75rem;margin:1.5rem 0;position:relative;padding-left:2rem}
.timeline::before{content:'';position:absolute;left:7px;top:8px;bottom:8px;width:2px;background:linear-gradient(180deg,var(--p),var(--c3))}
.tl-item{display:flex;gap:1rem;align-items:flex-start;position:relative}
.tl-year{font-family:var(--mono);font-size:.72rem;font-weight:700;color:var(--p);min-width:40px;padding-top:2px}
.tl-year::before{content:'';position:absolute;left:-2rem;top:6px;width:10px;height:10px;border-radius:50%;background:var(--bg);border:2px solid var(--p)}
.tl-item.active .tl-year::before{background:var(--p);box-shadow:0 0 12px var(--p-glow)}
.tl-item.active .tl-year{color:var(--c3)}
.tl-content{font-size:.85rem;color:var(--text2);line-height:1.5}
.tl-content strong{color:var(--text);display:block;margin-bottom:2px}

/* App Preview */
.app-preview{background:var(--bg2);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;box-shadow:0 15px 40px rgba(0,0,0,.4)}
.app-header{display:flex;align-items:center;gap:.4rem;padding:.6rem .8rem;background:rgba(255,255,255,.025);border-bottom:1px solid var(--border)}
.app-header span:not(.app-url){width:8px;height:8px;border-radius:50%}
.dot-r{background:#FF5F57;width:8px;height:8px;border-radius:50%;display:inline-block}.dot-y{background:#FFBD2E;width:8px;height:8px;border-radius:50%;display:inline-block}.dot-g{background:#28CA41;width:8px;height:8px;border-radius:50%;display:inline-block}
.app-url{margin-left:.5rem;font-family:var(--mono);font-size:.65rem;color:var(--text3)}
.app-body{display:flex;min-height:200px}
.app-sidebar{width:120px;border-right:1px solid var(--border);padding:.75rem 0}
.app-menu-item{padding:.4rem .75rem;font-size:.7rem;color:var(--text3);cursor:default;transition:all .2s}
.app-menu-item.active-item{color:var(--p);background:rgba(255,69,0,.08);border-left:2px solid var(--p)}
.app-main{flex:1;padding:1rem}
.app-row{height:12px;background:var(--surface);border-radius:4px;margin-bottom:.6rem;width:90%}
.app-row.short{width:60%}

/* Unit badges */
.unit-badge{display:inline-block;font-family:var(--mono);font-size:.72rem;font-weight:600;padding:.35rem .85rem;border-radius:20px;margin-bottom:1rem;letter-spacing:1px}
.u1{background:rgba(255,69,0,.1);color:var(--p);border:1px solid rgba(255,69,0,.15)}
.u2{background:rgba(255,122,51,.1);color:var(--c2);border:1px solid rgba(255,122,51,.15)}
.u3{background:rgba(255,179,71,.1);color:var(--c3);border:1px solid rgba(255,179,71,.15)}
.uf{background:rgba(255,207,112,.1);color:var(--c4);border:1px solid rgba(255,207,112,.15)}

/* Eval preview */
.eval-preview{display:flex;align-items:center;gap:.75rem;margin-top:1.5rem;padding:1rem 1.25rem;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-sm);font-size:.85rem;color:var(--text2)}
.eval-preview svg{width:18px;height:18px;color:var(--p);flex-shrink:0}

/* CRUD grid */
.crud-grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:1.5rem}
.crud-item{display:flex;align-items:center;gap:1.25rem;padding:1.25rem;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);transition:all .3s}
.crud-item:hover{background:var(--surface-h);transform:translateY(-2px)}
.crud-letter{font-size:2rem;font-weight:900;font-family:var(--mono);min-width:50px;text-align:center}
.crud-item.create .crud-letter{color:#4CAF50}
.crud-item.read .crud-letter{color:#2196F3}
.crud-item.update .crud-letter{color:#FF9800}
.crud-item.delete .crud-letter{color:#F44336}
.crud-item strong{display:block;font-size:.92rem;margin-bottom:2px}
.crud-item p{font-size:.82rem;color:var(--text2);margin:0}

/* Compare boxes */
.compare-box{padding:1.5rem;border-radius:var(--radius);border:1px solid var(--border)}
.compare-box.bad{background:rgba(244,67,54,.05);border-color:rgba(244,67,54,.15)}
.compare-box.good{background:rgba(76,175,80,.05);border-color:rgba(76,175,80,.15)}
.compare-header{display:flex;align-items:center;gap:.5rem;font-weight:700;font-size:.95rem;margin-bottom:1rem}
.compare-header svg{width:20px;height:20px}
.compare-box.bad .compare-header{color:#F44336}.compare-box.bad .compare-header svg{color:#F44336}
.compare-box.good .compare-header{color:#4CAF50}.compare-box.good .compare-header svg{color:#4CAF50}
.compare-box ul{list-style:none;display:flex;flex-direction:column;gap:.5rem}
.compare-box li{font-size:.84rem;color:var(--text2);padding-left:1.2rem;position:relative}
.compare-box.bad li::before{content:'✗';position:absolute;left:0;color:#F44336;font-weight:700}
.compare-box.good li::before{content:'✓';position:absolute;left:0;color:#4CAF50;font-weight:700}

/* Competencia box */
.competencia-box{display:flex;align-items:flex-start;gap:1.25rem;padding:1.5rem;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);margin-bottom:2rem}
.comp-icon{flex-shrink:0;width:48px;height:48px;background:linear-gradient(135deg,var(--p),var(--c2));border-radius:14px;display:flex;align-items:center;justify-content:center}
.comp-icon svg{width:24px;height:24px;color:#fff}
.comp-text{font-size:.92rem;color:var(--text2);line-height:1.6;font-style:italic}
.comp-level{font-family:var(--mono);font-size:.72rem;color:var(--c3);background:rgba(255,179,71,.1);padding:.2rem .6rem;border-radius:10px;margin-top:.5rem;display:inline-block}

/* Roadmap horizontal */
.roadmap-h{display:flex;align-items:center;gap:.5rem;margin:2rem 0;flex-wrap:wrap;justify-content:center}
.rm-step{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1.25rem;text-align:center;min-width:150px;transition:all .3s}
.rm-step:hover{background:var(--surface-h);transform:translateY(-2px)}
.rm-step.final{border-color:rgba(255,207,112,.2)}
.rm-num{font-family:var(--mono);font-size:1.5rem;font-weight:800;color:var(--p);margin-bottom:.5rem}
.rm-step.final .rm-num svg{width:28px;height:28px;color:var(--c4)}
.rm-info strong{display:block;font-size:.88rem;margin-bottom:.2rem}
.rm-info span{display:block;font-size:.78rem;color:var(--text2)}
.rm-w{font-family:var(--mono);font-weight:700;color:var(--c3) !important;margin-top:.35rem}
.rm-arrow{color:var(--text3)}
.rm-arrow svg{width:20px;height:20px}

/* Reasons */
.reasons-list{display:flex;flex-direction:column;gap:.75rem}
.reason{display:flex;align-items:flex-start;gap:1.25rem;padding:1rem 1.25rem;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-sm);transition:all .3s}
.reason:hover{background:var(--surface-h)}
.reason-num{font-family:var(--mono);font-size:1.2rem;font-weight:800;color:var(--p);min-width:36px}
.reason strong{display:block;font-size:.92rem;margin-bottom:.2rem}
.reason p{font-size:.82rem;color:var(--text2);line-height:1.5;margin:0}

/* Version info */
.version-info{margin-top:1.5rem;padding:1.25rem;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-sm)}
.ver-row{display:flex;gap:1rem;padding:.4rem 0;font-size:.85rem}
.ver-label{color:var(--text3);min-width:140px}
.ver-value{color:var(--text2);font-weight:500}

/* MVC Diagram */
.mvc-diagram{display:flex;align-items:center;justify-content:center;gap:.5rem;margin:2rem 0;flex-wrap:wrap}
.mvc-box{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1.25rem 1.5rem;text-align:center;min-width:120px}
.mvc-box svg{width:28px;height:28px;margin-bottom:.4rem}
.mvc-box span{display:block;font-weight:700;font-size:.9rem}
.mvc-box small{font-size:.72rem;color:var(--text3);display:block;margin-top:.2rem}
.mvc-user svg{color:var(--text2)}
.mvc-controller{border-color:rgba(255,69,0,.2)}.mvc-controller svg{color:var(--p)}
.mvc-model{border-color:rgba(255,179,71,.2)}.mvc-model svg{color:var(--c3)}
.mvc-view{border-color:rgba(255,122,51,.2)}.mvc-view svg{color:var(--c2)}
.mvc-arrow{display:flex;flex-direction:column;align-items:center;gap:2px}
.mvc-arrow svg{width:16px;height:16px;color:var(--text3)}
.mvc-arrow label{font-size:.6rem;color:var(--text3);text-transform:uppercase;letter-spacing:1px}
.mvc-summary{display:flex;flex-direction:column;gap:.5rem;margin-top:1.5rem}
.mvc-s{font-size:.85rem;color:var(--text2);padding:.5rem .75rem;background:var(--surface);border-radius:var(--radius-sm)}

/* Tools showcase */
.tools-showcase{display:flex;flex-direction:column;gap:.75rem}
.tool-item{display:flex;align-items:center;gap:1.25rem;padding:1.25rem;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);transition:all .3s}
.tool-item:hover{background:var(--surface-h)}
.tool-icon-big{width:52px;height:52px;border-radius:14px;background:linear-gradient(135deg,rgba(255,69,0,.15),rgba(255,122,51,.08));border:1px solid rgba(255,69,0,.12);display:flex;align-items:center;justify-content:center;flex-shrink:0}
.tool-icon-big svg{width:24px;height:24px;color:var(--p)}
.tool-detail h3{font-size:.95rem;font-weight:700;margin-bottom:.2rem}
.tool-detail p{font-size:.82rem;color:var(--text2);line-height:1.5;margin:0}

/* Install steps */
.install-steps{display:flex;flex-direction:column;gap:.75rem}
.install-step{display:flex;align-items:flex-start;gap:1rem;padding:1rem;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-sm)}
.step-num{font-family:var(--mono);font-size:1.2rem;font-weight:800;color:var(--p);min-width:32px;text-align:center;line-height:1.4}
.install-step strong{display:block;font-size:.9rem;margin-bottom:.2rem}
.install-step p{font-size:.82rem;color:var(--text2);margin:0}

/* Eval donut */
.eval-donut-container{display:flex;align-items:center;gap:3rem;margin:2rem 0;justify-content:center}
.eval-donut{position:relative;width:200px;height:200px}
.donut-svg{width:100%;height:100%}
.donut-center{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:var(--mono);font-size:1.8rem;font-weight:800;color:var(--p)}
.donut-center small{font-size:.7rem;color:var(--text3);text-transform:uppercase;letter-spacing:1px}
.eval-legend{display:flex;flex-direction:column;gap:.6rem}
.legend-item{display:flex;align-items:center;gap:.6rem;font-size:.85rem;color:var(--text2)}
.legend-dot{width:10px;height:10px;border-radius:3px;flex-shrink:0}

/* Calendar mini */
.cal-mini{border:1px solid var(--border);border-radius:var(--radius);overflow:hidden;margin-top:1rem}
.cal-row{display:grid;grid-template-columns:40px 65px 1fr 50px;padding:.55rem .75rem;font-size:.78rem;border-bottom:1px solid var(--border);align-items:center;gap:.5rem;transition:background .2s}
.cal-row:last-child{border-bottom:none}
.cal-row:hover{background:var(--surface-h)}
.cal-header{background:var(--bg3);font-weight:600;color:var(--text2);text-transform:uppercase;letter-spacing:1px;font-size:.68rem}
.cal-eval{background:rgba(255,69,0,.04)}
.cal-eval span{color:var(--c2);font-weight:600}
.cal-final{background:rgba(255,207,112,.05)}
.cal-final span{color:var(--c4);font-weight:700}
.tag-sync{font-size:.65rem;font-weight:600;color:var(--p);background:rgba(255,69,0,.1);padding:.1rem .4rem;border-radius:10px}
.tag-async{font-size:.65rem;font-weight:600;color:var(--text3);background:rgba(100,116,139,.1);padding:.1rem .4rem;border-radius:10px}

/* Rules grid */
.rules-grid{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:1rem}
.rule-item{padding:1.5rem;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);transition:all .3s}
.rule-item:hover{background:var(--surface-h);transform:translateY(-2px)}
.rule-icon{width:42px;height:42px;border-radius:12px;background:linear-gradient(135deg,rgba(255,69,0,.15),rgba(255,122,51,.08));border:1px solid rgba(255,69,0,.12);display:flex;align-items:center;justify-content:center;margin-bottom:.75rem}
.rule-icon svg{width:20px;height:20px;color:var(--p)}
.rule-item h3{font-size:.92rem;font-weight:700;margin-bottom:.35rem}
.rule-item p{font-size:.82rem;color:var(--text2);line-height:1.5}

/* Resources extra */
.resources-extra{margin-top:1.5rem;padding:1.5rem;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius)}
.resources-extra h3{font-size:.9rem;font-weight:700;margin-bottom:.75rem}
.resource-links{display:flex;flex-direction:column;gap:.5rem}
.res-link{display:flex;align-items:center;gap:.6rem;font-size:.84rem;color:var(--text2)}
.res-link svg{width:16px;height:16px;color:var(--p);flex-shrink:0}

/* Rubric */
.rubric-example{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);overflow:hidden}
.rubric-header{padding:.75rem 1rem;background:var(--bg3);font-weight:600;font-size:.82rem;color:var(--text2)}
.rubric-criterion{padding:1rem}
.rubric-name{font-weight:700;font-size:.88rem;margin-bottom:.75rem}
.rubric-levels{display:flex;flex-direction:column;gap:.4rem}
.rubric-level{padding:.5rem .75rem;border-radius:var(--radius-sm);font-size:.78rem}
.rubric-level span{font-weight:600;display:block;margin-bottom:2px}
.rubric-level p{margin:0;color:var(--text2)}
.excellent{background:rgba(76,175,80,.08);border-left:3px solid #4CAF50}.excellent span{color:#4CAF50}
.good{background:rgba(255,152,0,.06);border-left:3px solid #FF9800}.good span{color:#FF9800}
.basic{background:rgba(244,67,54,.06);border-left:3px solid #F44336}.basic span{color:#F44336}

/* Mission list */
.mission-list{display:flex;flex-direction:column;gap:.6rem}
.mission-item{display:flex;align-items:flex-start;gap:1rem;padding:1rem;background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-sm);transition:all .3s}
.mission-item:hover{background:var(--surface-h)}
.mission-check svg{width:20px;height:20px;color:var(--text3);flex-shrink:0;margin-top:2px}
.mission-content strong{display:block;font-size:.9rem;margin-bottom:.2rem}
.mission-content p{font-size:.82rem;color:var(--text2);margin:0}

/* Final box */
.final-box{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:3rem;text-align:center}
.final-pct{font-family:var(--mono);font-size:5rem;font-weight:900;color:var(--p);line-height:1}
.final-pct span{font-size:2rem;color:var(--c2)}
.final-box p{color:var(--text2);font-size:.9rem;margin-top:.5rem}

/* ── Navigation ── */
.nav-controls{position:fixed;bottom:1.5rem;left:50%;transform:translateX(-50%);display:flex;align-items:center;gap:1.25rem;z-index:100;background:rgba(10,14,26,.85);backdrop-filter:blur(16px);padding:.6rem 1.25rem;border-radius:50px;border:1px solid var(--border)}
.nav-btn{width:40px;height:40px;border-radius:10px;background:var(--surface);border:1px solid var(--border);color:var(--text);cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .3s;font-size:0}
.nav-btn:hover{background:var(--p);border-color:var(--p)}
.nav-btn svg{width:18px;height:18px}
.counter{font-family:var(--mono);font-size:.78rem;color:var(--text3);min-width:50px;text-align:center}

/* ── Floating Teacher Button ── */
.floating-teacher{
  position:fixed;top:1.25rem;right:1.25rem;z-index:100;
  display:flex;align-items:center;gap:.5rem;
  background:linear-gradient(135deg,rgba(255,69,0,.15),rgba(255,122,51,.1));
  border:1px solid rgba(255,69,0,.2);color:var(--c3);
  padding:.55rem 1rem;border-radius:50px;cursor:pointer;
  font-size:.78rem;font-weight:600;transition:all .3s;
  font-family:var(--font);
}
.floating-teacher:hover{background:linear-gradient(135deg,rgba(255,69,0,.25),rgba(255,122,51,.2));transform:scale(1.03)}
.floating-teacher svg{width:16px;height:16px}

/* ── Teacher Panel ── */
.teacher-overlay{position:fixed;inset:0;background:rgba(0,0,0,.5);z-index:190;opacity:0;pointer-events:none;transition:opacity .3s}
.teacher-overlay.open{opacity:1;pointer-events:all}
.teacher-panel{
  position:fixed;top:0;right:-440px;width:420px;height:100vh;
  background:var(--bg2);border-left:1px solid var(--border);z-index:200;
  transition:right .4s ease;overflow-y:auto;padding:0;
}
.teacher-panel.open{right:0}
.tp-header{display:flex;align-items:center;justify-content:space-between;padding:1.25rem 1.5rem;border-bottom:1px solid var(--border);position:sticky;top:0;background:var(--bg2);z-index:1}
.tp-header h3{font-size:.92rem;font-weight:700;display:flex;align-items:center;gap:.5rem}
.tp-header h3 svg{width:18px;height:18px;color:var(--p)}
.tp-close{width:32px;height:32px;border-radius:8px;background:var(--surface);border:1px solid var(--border);color:var(--text);cursor:pointer;display:flex;align-items:center;justify-content:center;transition:all .3s;font-size:0}
.tp-close:hover{background:rgba(244,67,54,.1);border-color:rgba(244,67,54,.2)}
.tp-close svg{width:16px;height:16px}
.tp-body{padding:1.5rem}
.tp-body h4{font-size:.85rem;font-weight:700;color:var(--p);margin-bottom:.75rem;margin-top:1.25rem;display:flex;align-items:center;gap:.4rem}
.tp-body h4:first-child{margin-top:0}
.tp-body ol{padding-left:1.25rem;display:flex;flex-direction:column;gap:.6rem}
.tp-body li{font-size:.84rem;color:var(--text2);line-height:1.6}
.tp-body p{font-size:.84rem;color:var(--text2);line-height:1.6}
.t-time{margin-top:1rem;font-family:var(--mono);font-size:.72rem;color:var(--text3);padding:.4rem .75rem;background:var(--surface);border-radius:var(--radius-sm);display:inline-block}

/* ── Animations ── */
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}
@keyframes fadeIn{from{opacity:0;transform:translateY(20px)}to{opacity:1;transform:translateY(0)}}

/* ── Responsive ── */
@media(max-width:900px){
  .slide{padding:2rem 1.5rem}
  .s-cards.three,.s-cards.four{grid-template-columns:1fr}
  .s-split{grid-template-columns:1fr}
  .crud-grid{grid-template-columns:1fr}
  .rules-grid{grid-template-columns:1fr}
  .roadmap-h{flex-direction:column;align-items:stretch}
  .rm-arrow{transform:rotate(90deg)}
  .mvc-diagram{flex-direction:column}
  .eval-donut-container{flex-direction:column}
  .nav-controls{bottom:.75rem;padding:.5rem 1rem}
  .teacher-panel{width:100%;right:-100%}
}
"""

# ═══════════════════════════════════════════════════════════
#  BUILD
# ═══════════════════════════════════════════════════════════
def main():
    n = len(S)
    slides_html = []
    teachers = []

    for i, s in enumerate(S):
        active = ' active' if i == 0 else ''
        layout = s.get('layout', 'content')
        slides_html.append(
            f'<div class="slide {layout}{active}" data-idx="{i}">'
            f'<div class="slide-inner">{s["content"]}</div></div>'
        )
        teachers.append(s['teacher'])

    teachers_json = json.dumps(teachers, ensure_ascii=False)

    html = f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Presentaci\\u00f3n U0 — Desarrollo de Software Web I</title>
<meta name="description" content="Presentaci\\u00f3n interactiva de bienvenida - Desarrollo de Software Web I - IPSS 2026">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600;700&display=swap" rel="stylesheet">
<script src="https://unpkg.com/lucide@latest/dist/umd/lucide.min.js"></script>
<style>{CSS}</style>
</head>
<body>

<!-- Progress Bar -->
<div class="progress"><div class="progress-fill" id="progress"></div></div>

<!-- Slides -->
<div class="slides" id="slides">
{''.join(slides_html)}
</div>

<!-- Navigation -->
<div class="nav-controls">
  <button class="nav-btn" id="prevBtn" onclick="prev()"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 18l-6-6 6-6"/></svg></button>
  <span class="counter" id="counter">01 / {n:02d}</span>
  <button class="nav-btn" id="nextBtn" onclick="next()"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 18l6-6-6-6"/></svg></button>
</div>

<!-- Floating Teacher Button -->
<div class="floating-teacher" onclick="toggleTeacher()">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>
  Ayuda al Profesor
</div>

<!-- Teacher Panel -->
<div class="teacher-overlay" id="teacherOverlay" onclick="toggleTeacher()"></div>
<div class="teacher-panel" id="teacherPanel">
  <div class="tp-header">
    <h3><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg> Ayuda al Profesor</h3>
    <button class="tp-close" onclick="toggleTeacher()"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 6L6 18M6 6l12 12"/></svg></button>
  </div>
  <div class="tp-body" id="teacherContent"></div>
</div>

<script>
/* ── Data ── */
const T = {teachers_json};
const total = {n};
let cur = 0;
let teacherOpen = false;

/* ── Init ── */
lucide.createIcons();
updateTeacher();

/* ── Navigation ── */
function go(idx) {{
  if (idx < 0 || idx >= total) return;
  const slides = document.querySelectorAll('.slide');
  slides[cur].classList.remove('active');
  slides[cur].classList.add('exit');
  setTimeout(() => slides[cur === idx ? cur : (cur > idx ? cur : cur)].classList.remove('exit'), 500);
  const prev = cur;
  cur = idx;
  slides[cur].classList.add('active');
  setTimeout(() => {{ if(prev !== cur) slides[prev].classList.remove('exit'); }}, 550);
  document.getElementById('counter').textContent = String(cur+1).padStart(2,'0') + ' / ' + String(total).padStart(2,'0');
  document.getElementById('progress').style.width = ((cur+1)/total*100) + '%';
  updateTeacher();
  lucide.createIcons();
}}
function next() {{ go(cur+1); }}
function prev() {{ go(cur-1); }}

/* ── Keyboard ── */
document.addEventListener('keydown', e => {{
  if (e.key === 'ArrowRight' || e.key === ' ') {{ e.preventDefault(); next(); }}
  else if (e.key === 'ArrowLeft') {{ e.preventDefault(); prev(); }}
  else if (e.key === 'Escape' && teacherOpen) toggleTeacher();
}});

/* ── Teacher Panel ── */
function toggleTeacher() {{
  teacherOpen = !teacherOpen;
  document.getElementById('teacherPanel').classList.toggle('open', teacherOpen);
  document.getElementById('teacherOverlay').classList.toggle('open', teacherOpen);
}}
function updateTeacher() {{
  document.getElementById('teacherContent').innerHTML = T[cur] || '';
}}
</script>
</body>
</html>"""

    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(html)
    size = os.path.getsize(OUT)
    print(f'\\u2705 Presentacion generada: {OUT}')
    print(f'   {n} diapositivas con guion del profesor')
    print(f'   Tamano: {size:,} bytes ({size/1024:.1f} KB)')

if __name__ == '__main__':
    main()
