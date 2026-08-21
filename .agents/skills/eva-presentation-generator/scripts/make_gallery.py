"""Genera el muestrario visual de la skill.

Produce `gallery/index.html` con dos secciones:
  1. Los 25 arquetipos renderizados en un pack, para ver las diagramaciones.
  2. Los 28 packs renderizados con las mismas 3 slides, para comparar estética.

Uso:  python3 scripts/make_gallery.py [pack_para_arquetipos]
"""
import json
import os
import shutil
import sys

SKILL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(SKILL, "scripts"))
from pack_renderer import ThemePack, render_slide  # noqa: E402

OUT = os.path.join(SKILL, "gallery")
PACKS_DIR = os.path.join(SKILL, "theme-packs")

# --- Contenido de demostración: un slot por cada campo del contrato ---------

DEMO = [
    ("cover", {
        "EYEBROW": "UNIDAD 3 · MUESTRARIO",
        "TITLE": "Diseño de Pruebas",
        "SUBTITLE": "Cómo se ve cada arquetipo con contenido real",
        "BG_IMAGE": "",
        "CHIPS": [
            {"label": "30 arquetipos", "accent": "a1"},
            {"label": "28 packs", "accent": "a2"},
            {"label": "1280 × 720", "accent": "a3"},
        ],
    }),
    ("toc", {
        "TAG_LEFT": "MAPA", "TITLE": "Qué veremos", "TAG_RIGHT": "02",
        "ROWS": "2", "COLS": "3",
        "ITEMS": [
            {"num": "01", "icon": "◆", "title": "Fundamentos", "desc": "Qué es una prueba y qué no lo es.", "chips": "Base"},
            {"num": "02", "icon": "◆", "title": "Diseño de casos", "desc": "Partición, valores límite y tablas.", "chips": "Técnica"},
            {"num": "03", "icon": "◆", "title": "Automatización", "desc": "Cuándo compensa y cuándo no.", "chips": "Práctica"},
            {"num": "04", "icon": "◆", "title": "Cobertura", "desc": "Medirla sin dejar que te mida a ti.", "chips": "Métrica"},
            {"num": "05", "icon": "◆", "title": "Reporte", "desc": "Escribir un defecto que se pueda arreglar.", "chips": "Oficio"},
            {"num": "06", "icon": "◆", "title": "Cierre", "desc": "Criterios de salida y deuda aceptada.", "chips": "Gestión"},
        ],
    }),
    ("section", {
        "PART_LABEL": "PARTE 01", "TITLE": "Fundamentos",
        "SUBTITLE": "Antes de automatizar nada, entender qué se está verificando",
        "AGENDA": [
            {"label": "01", "text": "Qué prueba una prueba"},
            {"label": "02", "text": "El coste de encontrar tarde"},
            {"label": "03", "text": "Oráculo y expectativa"},
        ],
    }),
    ("concept-cards", {
        "TAG_LEFT": "CONCEPTOS", "TITLE": "Tres niveles de prueba", "TAG_RIGHT": "04", "COLS": "3",
        "CARDS": [
            {"badge": "01", "title": "Unitaria", "body": "Verifica una unidad aislada. Rápida, barata y la primera en avisar.",
             "note_label": "Coste", "note": "Milisegundos por caso."},
            {"badge": "02", "title": "Integración", "body": "Verifica que dos piezas hablan bien entre sí. Aquí viven los contratos.",
             "note_label": "Coste", "note": "Segundos, requiere entorno."},
            {"badge": "03", "title": "Extremo a extremo", "body": "Recorre el flujo completo como lo haría una persona.",
             "note_label": "Coste", "note": "Minutos y mucha fragilidad."},
        ],
    }),
    ("comparison", {
        "TAG_LEFT": "CONTRASTE", "TITLE": "Verificar contra validar", "TAG_RIGHT": "05", "VS_LABEL": "VS",
        "LEFT_LABEL": "VERIFICAR", "LEFT_TITLE": "¿Lo construimos bien?",
        "LEFT_BODY": "Comprueba que el producto cumple la especificación escrita.",
        "LEFT_EXAMPLE": "El campo acepta 8 caracteres, como pedía el requisito.",
        "RIGHT_LABEL": "VALIDAR", "RIGHT_TITLE": "¿Construimos lo correcto?",
        "RIGHT_BODY": "Comprueba que la especificación resolvía el problema real.",
        "RIGHT_EXAMPLE": "Nadie usa ese campo porque el flujo no tenía sentido.",
        "LEFT_POINTS": [{"text": "Contra el documento"}, {"text": "Objetiva y automatizable"}, {"text": "La hace el equipo"}],
        "RIGHT_POINTS": [{"text": "Contra la necesidad"}, {"text": "Requiere criterio"}, {"text": "La hace el usuario"}],
        "RIGHT_TAGS": [{"text": "UAT"}, {"text": "Piloto"}],
    }),
    ("activity", {
        "TAG_LEFT": "TALLER", "TITLE": "Diseña los casos", "TAG_RIGHT": "06", "ICON": "gqdnbnwt",
        "ACTIVITY_NAME": "Partición de equivalencia en 20 minutos",
        "INSTRUCTIONS": "En parejas, tomad el formulario de alta y proponed el conjunto mínimo de casos que cubre todas las clases.",
        "COLS": "2",
        "META": [{"label": "20 min"}, {"label": "Parejas"}, {"label": "Entregable en el aula"}],
        "CASES": [
            {"num": "01", "title": "Campo edad", "desc": "Acepta enteros de 18 a 99.",
             "challenge_label": "Reto", "challenge": "¿Cuántos casos bastan de verdad?"},
            {"num": "02", "title": "Campo correo", "desc": "Formato libre con validación en cliente.",
             "challenge_label": "Reto", "challenge": "Encuentra la clase que nadie prueba."},
        ],
    }),
    ("code", {
        "TAG_LEFT": "CÓDIGO", "TITLE": "Una prueba legible", "TAG_RIGHT": "07", "SPLIT": "1.1fr 1fr",
        "LEAD": "El nombre del test es documentación. Si hay que leer el cuerpo para saber qué falla, está mal escrito.",
        "CALLOUT_LABEL": "Regla", "CALLOUT": "Un assert por comportamiento, no por línea.",
        "FILENAME": "test_alta_usuario.py",
        "CODE": "<span class='c-cm'># Arrange</span>\nusuario = Usuario(edad=<span class='c-num'>17</span>)\n\n<span class='c-cm'># Act</span>\nresultado = registrar(usuario)\n\n<span class='c-cm'># Assert</span>\n<span class='c-kw'>assert</span> resultado.error == <span class='c-str'>\"MENOR_DE_EDAD\"</span>",
        "STEPS": [
            {"n": "1", "text": "Prepara el estado mínimo que necesita el caso."},
            {"n": "2", "text": "Ejecuta una sola acción."},
            {"n": "3", "text": "Comprueba un solo comportamiento observable."},
        ],
    }),
    ("table", {
        "TAG_LEFT": "DATOS", "TITLE": "Casos de la partición", "TAG_RIGHT": "08",
        "LEAD": "El conjunto mínimo que cubre todas las clases de equivalencia del campo edad.",
        "HEADERS": "<th>Caso</th><th>Entrada</th><th>Clase</th><th>Esperado</th>",
        "NOTE_LABEL": "Nota", "NOTE": "Los límites 17/18 y 99/100 se prueban aparte con valores límite.",
        "ROWS": [
            {"cells": "<td>CP-01</td><td>-5</td><td>Inválida baja</td><td>Rechazo</td>"},
            {"cells": "<td>CP-02</td><td>17</td><td>Menor</td><td>Rechazo</td>"},
            {"cells": "<td>CP-03</td><td>42</td><td>Válida</td><td>Alta correcta</td>"},
            {"cells": "<td>CP-04</td><td>120</td><td>Inválida alta</td><td>Rechazo</td>"},
        ],
    }),
    ("metrics", {
        "TAG_LEFT": "CIFRAS", "TITLE": "El coste de encontrar tarde", "TAG_RIGHT": "09",
        "LEAD": "Datos del último trimestre en tres equipos de producto.", "COLS": "4",
        "SOURCE": "Fuente: informe interno de calidad, Q2.",
        "METRICS": [
            {"label": "En diseño", "value": "1", "unit": "×", "desc": "Coste base de corregir.", "pct": "10%"},
            {"label": "En desarrollo", "value": "6", "unit": "×", "desc": "Ya hay código escrito.", "pct": "30%"},
            {"label": "En pruebas", "value": "15", "unit": "×", "desc": "Hay que rehacer y reprobar.", "pct": "60%"},
            {"label": "En producción", "value": "100", "unit": "×", "desc": "Incidente, parche y confianza.", "pct": "100%"},
        ],
    }),
    ("timeline", {
        "TAG_LEFT": "PROCESO", "TITLE": "El ciclo de una prueba", "TAG_RIGHT": "10",
        "LEAD": "De la lectura del requisito al cierre del defecto.", "COLS": "4",
        "STEPS": [
            {"n": "1", "phase": "Analizar", "title": "Leer el requisito", "desc": "Detectar ambigüedades antes de escribir nada.", "output": "Dudas resueltas"},
            {"n": "2", "phase": "Diseñar", "title": "Derivar casos", "desc": "Partición, límites y tabla de decisión.", "output": "Casos priorizados"},
            {"n": "3", "phase": "Ejecutar", "title": "Correr y observar", "desc": "Registrar evidencia de lo que ocurre.", "output": "Resultados"},
            {"n": "4", "phase": "Reportar", "title": "Escribir el defecto", "desc": "Pasos, esperado, obtenido y entorno.", "output": "Ticket accionable"},
        ],
    }),
    ("matrix", {
        "TAG_LEFT": "DECISIÓN", "TITLE": "¿Qué automatizo?", "TAG_RIGHT": "11",
        "AXIS_X": "Frecuencia de ejecución →", "AXIS_Y": "↑ Estabilidad del caso",
        "SIDE_TITLE": "Cómo leer el cuadrante",
        "Q1_TAG": "AUTOMATIZA YA", "Q1_TITLE": "Estable y frecuente", "Q1_DESC": "Regresión del núcleo. Se paga sola en dos sprints.",
        "Q2_TAG": "EVALÚA", "Q2_TITLE": "Estable y esporádico", "Q2_DESC": "Automatiza solo si el caso es caro de ejecutar a mano.",
        "Q3_TAG": "MANUAL", "Q3_TITLE": "Inestable y esporádico", "Q3_DESC": "Exploratorio. Automatizarlo es tirar el tiempo.",
        "Q4_TAG": "ESTABILIZA ANTES", "Q4_TITLE": "Inestable y frecuente", "Q4_DESC": "Arregla el flakiness antes de invertir.",
        "RULES": [
            {"label": "Regla 1", "text": "Si el caso cambia cada sprint, no lo automatices todavía."},
            {"label": "Regla 2", "text": "Si tarda más en mantenerse que en ejecutarse, bórralo."},
        ],
    }),
    ("quote", {
        "QUOTE": "Las pruebas no demuestran la ausencia de defectos, solo su presencia.",
        "AUTHOR": "Edsger W. Dijkstra", "ROLE": "Informático",
        "CONTEXT_LABEL": "Por qué importa",
        "CONTEXT": "Ninguna suite prueba que el sistema es correcto. Prueba que no ha fallado todavía en lo que miraste.",
    }),
    ("quiz", {
        "TAG_LEFT": "COMPRUEBA", "TITLE": "Knowledge check", "TAG_RIGHT": "13", "BADGE": "PREGUNTA 1",
        "QUESTION": "¿Qué mide realmente la cobertura de código?",
        "COLS": "2",
        "EXPLANATION_LABEL": "Por qué",
        "EXPLANATION": "La cobertura dice qué líneas se ejecutaron, no si se comprobó algo sobre ellas. Un test sin assert da cobertura.",
        "OPTIONS": [
            {"key": "A", "text": "Qué porcentaje del código se ejecutó al correr la suite", "correct": "true"},
            {"key": "B", "text": "Qué porcentaje de los requisitos está verificado", "correct": ""},
            {"key": "C", "text": "La probabilidad de que no haya defectos", "correct": ""},
            {"key": "D", "text": "La calidad de los asserts escritos", "correct": ""},
        ],
    }),
    ("dodont", {
        "TAG_LEFT": "PRÁCTICA", "TITLE": "Cómo nombrar un test", "TAG_RIGHT": "14",
        "BAD_TITLE": "Así no", "BAD_SNIPPET": "def test_1():\n    ...\n\ndef test_usuario():\n    ...",
        "GOOD_TITLE": "Así sí", "GOOD_SNIPPET": "def test_rechaza_alta_si_menor_de_edad():\n    ...",
        "WHY_LABEL": "Por qué", "WHY": "Cuando falla en el pipeline, el nombre es lo único que ves. Si no dice qué se rompió, alguien tiene que abrir el archivo.",
        "BAD_POINTS": [{"text": "No dice qué comprueba"}, {"text": "Obliga a leer el cuerpo"}, {"text": "Se duplica sin que nadie lo note"}],
        "GOOD_POINTS": [{"text": "Describe el comportamiento"}, {"text": "Se lee en el log de CI"}, {"text": "Delata si el test hace dos cosas"}],
    }),
    ("anatomy", {
        "TAG_LEFT": "ANATOMÍA", "TITLE": "Partes de un reporte de defecto", "TAG_RIGHT": "15",
        "SPEC_TITLE": "DEF-2481 · Alta rechaza mayores de edad",
        "FIELDS": [
            {"key": "Severidad", "value": "Alta", "highlight": "true"},
            {"key": "Entorno", "value": "Staging · Chrome 121 · macOS", "highlight": ""},
            {"key": "Pasos", "value": "1. Abrir alta 2. Edad 42 3. Enviar", "highlight": ""},
            {"key": "Esperado", "value": "Usuario creado", "highlight": ""},
            {"key": "Obtenido", "value": "Error MENOR_DE_EDAD", "highlight": "true"},
        ],
        "NOTES": [
            {"n": "1", "title": "Reproducible", "text": "Si no puedes repetirlo, todavía no es un defecto: es una anécdota."},
            {"n": "2", "title": "Aislado", "text": "Un ticket, un problema. Dos defectos juntos no se cierran nunca."},
        ],
    }),
    ("principle", {
        "TAG_LEFT": "PRINCIPIO", "TITLE": "La regla del 80/20 en pruebas", "TAG_RIGHT": "16",
        "GHOST": "80/20", "KICKER": "Pareto aplicado",
        "PRINCIPLE": "El 20% de los módulos concentra el 80% de los defectos.",
        "PRINCIPLE_BODY": "No repartas el esfuerzo por igual. Mide dónde aparecen los fallos y concentra ahí la profundidad de prueba.",
        "LIST_TITLE": "Cómo encontrar ese 20%",
        "FACTORS": [
            {"name": "Historial", "text": "Módulos con más defectos cerrados el último año.", "color": "var(--a1)"},
            {"name": "Cambio", "text": "Archivos con más commits en el trimestre.", "color": "var(--a2)"},
            {"name": "Acoplamiento", "text": "Piezas de las que dependen muchas otras.", "color": "var(--a3)"},
        ],
        "EXAMPLES": [
            {"tag": "Antes", "value": "42", "label": "defectos en producción", "desc": "Esfuerzo repartido por igual.", "color": "var(--err)"},
            {"tag": "Después", "value": "11", "label": "defectos en producción", "desc": "Profundidad concentrada.", "color": "var(--ok)"},
        ],
    }),
    ("heatmap", {
        "TAG_LEFT": "RIESGO", "TITLE": "Mapa de calor por módulo", "TAG_RIGHT": "17",
        "AXIS_X": "Impacto →", "AXIS_Y": "↑ Probabilidad", "COLS": "3",
        "EXPL_TITLE": "Cómo se lee", "EXPL_BODY": "Cada celda cruza probabilidad de fallo con impacto en el usuario. Empieza por la esquina caliente.",
        "CELLS": [
            {"label": "Pagos", "level": "3"}, {"label": "Sesión", "level": "3"}, {"label": "Alta", "level": "2"},
            {"label": "Buscador", "level": "2"}, {"label": "Perfil", "level": "1"}, {"label": "Ayuda", "level": "1"},
            {"label": "Export", "level": "2"}, {"label": "Tema", "level": "0"}, {"label": "Idioma", "level": "0"},
        ],
        "ZONES": [
            {"badge": "ALTA", "condition": "Nivel 3", "title": "Prueba profunda", "desc": "Casos límite y automatización de regresión.", "color": "var(--err)", "bg": "var(--err-t)"},
            {"badge": "MEDIA", "condition": "Nivel 2", "title": "Prueba dirigida", "desc": "Camino feliz más dos casos de error.", "color": "var(--warn)", "bg": "var(--warn-t)"},
            {"badge": "BAJA", "condition": "Nivel 0-1", "title": "Prueba de humo", "desc": "Que abra y no rompa nada.", "color": "var(--ok)", "bg": "var(--ok-t)"},
        ],
    }),
    ("code-criteria", {
        "TAG_LEFT": "REVISIÓN", "TITLE": "Criterios de aceptación de un test", "TAG_RIGHT": "18",
        "KICKER": "Checklist de revisión",
        "CODE_TITLE": "test_carrito.py",
        "CODE": "<span class='c-kw'>def</span> <span class='c-fn'>test_total_aplica_descuento</span>():\n    carrito = Carrito()\n    carrito.añadir(precio=<span class='c-num'>100</span>)\n    carrito.cupon(<span class='c-str'>\"DIEZ\"</span>)\n    <span class='c-kw'>assert</span> carrito.total() == <span class='c-num'>90</span>",
        "PANEL_TITLE": "Criterios",
        "WHY_TITLE": "Por qué este pasa",
        "WHY": "Nombre descriptivo, un solo comportamiento, sin dependencias externas y con un valor esperado explícito.",
        "CRITERIA": [
            {"letter": "A", "name": "Nombre describe el comportamiento", "meta": "Obligatorio", "highlight": "true"},
            {"letter": "B", "name": "Un solo assert conceptual", "meta": "Obligatorio", "highlight": ""},
            {"letter": "C", "name": "Sin red ni base de datos", "meta": "Unitaria", "highlight": ""},
            {"letter": "D", "name": "Determinista entre ejecuciones", "meta": "Obligatorio", "highlight": "true"},
        ],
    }),
    ("bento", {
        "TAG_LEFT": "PANORAMA", "TITLE": "La estrategia de un vistazo", "TAG_RIGHT": "19",
        "TILES": [
            {"variant": "stat", "col": "span 2", "row": "span 2", "icon": "◆", "tag": "COBERTURA", "stat": "72", "unit": "%",
             "title": "Líneas ejecutadas", "body": "Sube despacio y por módulos de riesgo, no por el total.", "foot": "Meta trimestral: 80%"},
            {"variant": "", "col": "span 2", "row": "span 1", "icon": "▲", "tag": "SUITE", "stat": "", "unit": "",
             "title": "1.240 pruebas", "body": "Ejecución completa en 6 minutos.", "foot": ""},
            {"variant": "accent", "col": "span 2", "row": "span 1", "icon": "●", "tag": "FLAKY", "stat": "3", "unit": "",
             "title": "Pruebas inestables", "body": "En cuarentena hasta arreglarlas.", "foot": ""},
            {"variant": "", "col": "span 3", "row": "span 1", "icon": "■", "tag": "PIPELINE", "stat": "", "unit": "",
             "title": "Bloqueo en rojo", "body": "Ningún merge con la suite en fallo.", "foot": "Sin excepciones"},
            {"variant": "", "col": "span 3", "row": "span 1", "icon": "▮", "tag": "ENTORNO", "stat": "", "unit": "",
             "title": "Datos sembrados", "body": "Cada prueba crea y destruye lo suyo.", "foot": ""},
        ],
    }),
    ("callouts", {
        "TAG_LEFT": "AVISOS", "TITLE": "Lo que conviene recordar", "TAG_RIGHT": "20",
        "LEAD": "Cinco advertencias que se repiten en todas las revisiones de código.",
        "CALLOUTS": [
            {"kind": "info", "icon": "qhgmphtg", "title": "Contexto", "text": "Una prueba sin assert sigue dando cobertura. La cobertura no es una medida de calidad."},
            {"kind": "tip", "icon": "xtzvywzp", "title": "Consejo", "text": "Escribe primero el nombre del test. Si no sabes nombrarlo, todavía no sabes qué vas a probar."},
            {"kind": "warn", "icon": "inrunzby", "title": "Cuidado", "text": "Los sleep fijos son la primera causa de pruebas inestables. Espera por condición, no por tiempo."},
            {"kind": "danger", "icon": "lupuorrc", "title": "Nunca", "text": "No pruebes contra producción. Nunca. Ni «solo esta vez para salir del paso»."},
            {"kind": "note", "icon": "msoeawqm", "title": "Nota", "text": "Una prueba que nadie ha visto fallar no ha demostrado que sirve. Rómpela a propósito una vez."},
        ],
    }),
    ("feature-matrix", {
        "TAG_LEFT": "COMPARATIVA", "TITLE": "Herramientas de automatización", "TAG_RIGHT": "21",
        "LEAD": "Criterios que importan al elegir, no los del folleto comercial.",
        "HEADERS": "<th>Criterio</th><th>Playwright</th><th>Cypress</th><th>Selenium</th>",
        "NOTE_LABEL": "Criterio de decisión",
        "NOTE": "Elige por el navegador que debes soportar y por quién va a mantener la suite dentro de un año.",
        "ROWS": [
            {"cells": "<td>Multi-navegador</td><td>Sí</td><td>Parcial</td><td>Sí</td>"},
            {"cells": "<td>Espera automática</td><td>Sí</td><td>Sí</td><td>No</td>"},
            {"cells": "<td>Depuración por traza</td><td>Sí</td><td>Sí</td><td>Limitada</td>"},
            {"cells": "<td>Curva de entrada</td><td>Media</td><td>Baja</td><td>Alta</td>"},
        ],
    }),
    ("diagram", {
        "TAG_LEFT": "FLUJO", "TITLE": "El pipeline de calidad", "TAG_RIGHT": "22", "SPLIT": "1.2fr 1fr",
        "DIAGRAM": "flowchart LR\n  A[Commit] --> B[Unitarias]\n  B --> C{¿Verde?}\n  C -->|Sí| D[Integración]\n  C -->|No| E[Bloqueo]\n  D --> F[Despliegue]",
        "SIDE_TITLE": "Las cuatro puertas",
        "LEAD": "Cada puerta filtra un tipo de fallo distinto. Saltarse una traslada el coste a la siguiente.",
        "NOTE_LABEL": "Regla", "NOTE": "Ninguna puerta se salta «por urgencia». La urgencia es justo cuando más fallan las cosas.",
        "STEPS": [
            {"n": "1", "name": "Commit", "text": "Formato y linter en local, antes de subir."},
            {"n": "2", "name": "Unitarias", "text": "Segundos. Bloquean el merge si fallan."},
            {"n": "3", "name": "Integración", "text": "Minutos. Verifican contratos entre servicios."},
            {"n": "4", "name": "Despliegue", "text": "Humo en el entorno real tras publicar."},
        ],
    }),
    ("roadmap", {
        "TAG_LEFT": "PLAN", "TITLE": "Adopción en tres trimestres", "TAG_RIGHT": "23",
        "LEAD": "Qué se hace en cada fase y qué se deja explícitamente para después.", "COLS": "3",
        "LANES": [
            {"phase": "Q1 · Base", "when": "Ene – Mar", "color": "var(--a1)",
             "items": "Suite unitaria en el núcleo|Pipeline que bloquea en rojo|Convención de nombres"},
            {"phase": "Q2 · Extensión", "when": "Abr – Jun", "color": "var(--a2)",
             "items": "Integración en los tres servicios críticos|Datos de prueba sembrados|Cuarentena de inestables"},
            {"phase": "Q3 · Profundidad", "when": "Jul – Sep", "color": "var(--a3)",
             "items": "Extremo a extremo en dos flujos|Pruebas de carga del checkout|Informe mensual de calidad"},
        ],
    }),
    ("closing", {
        "TAG_LEFT": "CIERRE", "TITLE": "Lo que te llevas", "TAG_RIGHT": "24", "ICON": "wzwygmng",
        "HERO_TITLE": "Probar es diseñar",
        "HERO_TEXT": "Cuando escribes una prueba antes que el código, estás decidiendo cómo se va a usar. Esa es la mitad del valor.",
        "LEFT_PANEL_TITLE": "Ideas clave", "RIGHT_PANEL_TITLE": "Siguientes pasos",
        "NEXT_LABEL": "Próxima sesión", "NEXT": "Unidad 4 — Automatización y pipeline de integración continua.",
        "TAKEAWAYS": [
            {"n": "1", "text": "La cobertura mide ejecución, no verificación."},
            {"n": "2", "text": "El 20% de los módulos concentra el 80% de los defectos."},
            {"n": "3", "text": "El nombre del test es lo único que se lee cuando falla."},
        ],
        "NEXT_STEPS": [
            {"n": "1", "text": "Escribe cinco casos con partición para tu módulo."},
            {"n": "2", "text": "Nombra tres pruebas existentes que no dicen qué comprueban."},
            {"n": "3", "text": "Trae un defecto real para reescribir su reporte."},
        ],
    }),
    ("resources", {
        "TAG_LEFT": "MATERIAL", "TITLE": "Para seguir", "TAG_RIGHT": "25",
        "LIST_TITLE": "Lecturas y herramientas",
        "QR_LABEL": "AULA VIRTUAL", "QR_DATA": "https://eva.ipss.cl", "QR_ALT": "Código QR del aula virtual",
        "QR_CAPTION": "Material completo de la unidad",
        "NEXT_LABEL": "Entrega", "NEXT": "Casos de prueba del módulo asignado, antes de la próxima sesión.",
        "RESOURCES": [
            {"icon": "▤", "title": "ISTQB Foundation", "desc": "El vocabulario común del oficio.", "url": "istqb.org"},
            {"icon": "▤", "title": "Playwright Docs", "desc": "Guía de espera por condición.", "url": "playwright.dev"},
            {"icon": "▤", "title": "Working Effectively with Legacy Code", "desc": "Cómo probar lo que no se diseñó para probarse.", "url": "Feathers, 2004"},
        ],
    }),
    ("chart-bars", {
        "TAG_LEFT": "GRÁFICO", "TITLE": "Defectos por módulo", "TAG_RIGHT": "26",
        "LEAD": "Defectos abiertos en el último trimestre. Confirma la regla del 80/20: dos módulos concentran la mitad.",
        "COLS": "6",
        "SCALE_TOP": "48", "SCALE_MID": "24", "SCALE_BASE": "0",
        "READ_LABEL": "Cómo se lee",
        "READ": "Pagos y Sesión suman el 54% de los defectos con el 18% del código. Ahí va la prueba profunda.",
        "SOURCE": "Fuente: backlog de calidad, Q2 · n=112",
        "BARS": [
            {"label": "Pagos", "sub": "crítico", "value": "42", "unit": "", "tone": "warn"},
            {"label": "Sesión", "sub": "crítico", "value": "31", "unit": "", "tone": "warn"},
            {"label": "Alta", "sub": "medio", "value": "18", "unit": "", "tone": ""},
            {"label": "Buscador", "sub": "medio", "value": "12", "unit": "", "tone": ""},
            {"label": "Perfil", "sub": "bajo", "value": "6", "unit": "", "tone": "alt"},
            {"label": "Ayuda", "sub": "bajo", "value": "3", "unit": "", "tone": "mute"},
        ],
    }),
    ("chart-split", {
        "TAG_LEFT": "GRÁFICO Y DATOS", "TITLE": "Tiempo de ejecución de la suite", "TAG_RIGHT": "27",
        "SPLIT": "1.15fr 1fr",
        "LEAD": "Duración media por tipo de prueba. La forma se ve a la izquierda; la cifra exacta, a la derecha.",
        "TABLE_TITLE": "Detalle por tipo",
        "HEADERS": "<th>Tipo</th><th>Casos</th><th>Media</th><th>Total</th>",
        "INSIGHT_TITLE": "Qué hacer con esto",
        "INSIGHT": "El extremo a extremo cuesta 40 veces más por caso que una unitaria. No es que sea malo: es que no puede ser la mayoría de la suite.",
        "SOURCE": "Media de 30 ejecuciones en CI",
        "BARS": [
            {"label": "Unitarias", "value": "0.9", "unit": "s", "tone": "ok"},
            {"label": "Integración", "value": "6.4", "unit": "s", "tone": ""},
            {"label": "Contrato", "value": "11.2", "unit": "s", "tone": "alt"},
            {"label": "Extremo a extremo", "value": "38.5", "unit": "s", "tone": "warn"},
        ],
        "ROWS": [
            {"cells": "<td>Unitarias</td><td>982</td><td>0,9 s</td><td>2 min</td>"},
            {"cells": "<td>Integración</td><td>184</td><td>6,4 s</td><td>4 min</td>"},
            {"cells": "<td>Contrato</td><td>52</td><td>11,2 s</td><td>3 min</td>"},
            {"cells": "<td>Extremo a extremo</td><td>22</td><td>38,5 s</td><td>7 min</td>"},
        ],
    }),
    ("chart-grid", {
        "TAG_LEFT": "PANORAMA", "TITLE": "Salud de la suite", "TAG_RIGHT": "28",
        "LEAD": "Cuatro lecturas distintas del mismo trimestre. Ninguna basta sola.",
        "COLS": "2",
        "SOURCE": "Panel de calidad · cierre de Q2",
        "PANELS": [
            {"title": "Reparto de la pirámide", "tag": "COMPOSICIÓN", "kind": "donut",
             "series": "Unitarias:982|Integración:184|Contrato:52|E2E:22", "center": "1240",
             "note": "La base sostiene el 79% de la suite. Es la proporción que se busca."},
            {"title": "Defectos por sprint", "tag": "TENDENCIA", "kind": "bars",
             "series": "S1:18|S2:22|S3:14|S4:9|S5:11|S6:6", "center": "",
             "note": "Caída sostenida desde que el pipeline bloquea en rojo."},
            {"title": "Dónde se encuentran", "tag": "FASE", "kind": "stack",
             "series": "Local:44|CI:38|Staging:12|Producción:6", "center": "",
             "note": "Solo el 6% llega a producción. Hace un año era el 24%."},
            {"title": "Duración del pipeline", "tag": "MINUTOS", "kind": "spark",
             "series": "Ene:22|Feb:19|Mar:21|Abr:15|May:13|Jun:12", "center": "",
             "note": "De 22 a 12 minutos tras paralelizar la integración."},
        ],
    }),
    ("gauges", {
        "TAG_LEFT": "INDICADORES", "TITLE": "Objetivos del trimestre", "TAG_RIGHT": "29",
        "LEAD": "Cuatro compromisos medibles. El anillo muestra el avance real contra la meta acordada.",
        "COLS": "4",
        "READ_LABEL": "Lectura",
        "READ": "Tres de cuatro en verde. La cobertura de integración es la única que no llega, y es la que más defectos evitaría.",
        "SOURCE": "Corte al 30 de junio",
        "GAUGES": [
            {"label": "Cobertura", "value": "72", "goal": "meta 80", "desc": "Líneas ejecutadas por la suite completa.", "tone": ""},
            {"label": "Integración", "value": "41", "goal": "meta 70", "desc": "Servicios críticos con contrato verificado.", "tone": "warn"},
            {"label": "Pipeline verde", "value": "94", "goal": "meta 90", "desc": "Ejecuciones sin fallo en la rama principal.", "tone": "ok"},
            {"label": "Sin inestables", "value": "88", "goal": "meta 85", "desc": "Pruebas fuera de cuarentena.", "tone": "alt"},
        ],
    }),
    ("trend", {
        "TAG_LEFT": "EVOLUCIÓN", "TITLE": "Defectos que llegan a producción", "TAG_RIGHT": "30",
        "SPLIT": "1.25fr 1fr",
        "LEAD": "Doce meses de incidentes en producción. El trazado lo calcula el sistema a partir de las cifras.",
        "SIDE_TITLE": "Qué pasó en el camino",
        "DELTA_LABEL": "Variación anual", "DELTA": "−74%",
        "DELTA_NOTE": "De 42 incidentes en julio a 11 en junio, sin añadir una sola persona al equipo.",
        "SOURCE": "Registro de incidentes · 12 meses",
        "SERIES": [
            {"when": "Jul", "value": "42"}, {"when": "Ago", "value": "38"},
            {"when": "Sep", "value": "40"}, {"when": "Oct", "value": "29"},
            {"when": "Nov", "value": "24"}, {"when": "Dic", "value": "26"},
            {"when": "Ene", "value": "19"}, {"when": "Feb", "value": "17"},
            {"when": "Mar", "value": "20"}, {"when": "Abr", "value": "14"},
            {"when": "May", "value": "12"}, {"when": "Jun", "value": "11"},
        ],
        "MILESTONES": [
            {"when": "Oct", "title": "Pipeline bloquea en rojo", "text": "Ningún merge con la suite en fallo. La caída más brusca del año."},
            {"when": "Ene", "title": "Cuarentena de inestables", "text": "Las pruebas poco fiables dejan de esconder fallos reales."},
            {"when": "Abr", "title": "Contratos entre servicios", "text": "Desaparece la familia de incidentes por cambios de API."},
        ],
    }),
]

# Las 3 slides que se usan para comparar packs entre sí.
PACK_SAMPLE = ["cover", "principle", "concept-cards"]


def render(pack_id, entries, outdir):
    pack = ThemePack(PACKS_DIR, pack_id)
    os.makedirs(outdir, exist_ok=True)
    made = []
    for i, (arch, slots) in enumerate(entries):
        html, _ = render_slide(pack, {"archetype": arch, "slots": slots}, i, len(entries))
        name = f"{i:02d}-{arch}.html"
        open(os.path.join(outdir, name), "w", encoding="utf-8").write(html)
        made.append((name, arch))
    return made


def thumbs(items, base, scale=0.26):
    w, h = 1280, 720
    cells = "".join(
        f'<a class="cell" href="{base}/{name}" target="_blank">'
        f'<iframe src="{base}/{name}" scrolling="no"></iframe>'
        f'<span>{label}</span></a>'
        for name, label in items
    )
    return cells, int(w * scale), int(h * scale)


def build_icons():
    """Muestrario de iconos Lordicon, a partir del catálogo verificado."""
    path = os.path.join(PACKS_DIR, "_shared", "icons.json")
    if not os.path.isfile(path):
        return 0
    data = json.load(open(path, encoding="utf-8"))
    icons = data.get("icons", [])
    roto = ", ".join(data.get("_rotos", {}).get("ids", []))

    cards = "".join(
        f'<figure class="ic"><div class="ic-box">'
        f'<lord-icon src="https://cdn.lordicon.com/{i["id"]}.json" trigger="loop" delay="1400" '
        f'colors="primary:#3ddbf0,secondary:#7b6cff" style="width:56px;height:56px"></lord-icon>'
        f'</div><figcaption><code>{i["id"]}</code>'
        f'<span><b>{i.get("name") or "&nbsp;"}</b></span>'
        f'<span>{i.get("tags") or "&nbsp;"}</span></figcaption></figure>'
        for i in icons
    )

    html = f"""<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">
<title>Iconos animados · EVA</title>
<script src="https://cdn.lordicon.com/lordicon.js"></script>
<style>
:root{{--bg:#0e0e10;--fg:#e8e8ea;--mut:#8f8f99;--card:#17171c;--line:#2c2c33}}
[data-theme="light"]{{--bg:#f6f5f2;--fg:#1a1a1e;--mut:#6a6a72;--card:#fff;--line:#e0ded8}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--bg);color:var(--fg);font:14px/1.5 system-ui,-apple-system,sans-serif;
  transition:background .25s,color .25s}}
header{{padding:30px 40px 18px;border-bottom:1px solid var(--line);display:flex;
  justify-content:space-between;align-items:flex-start;gap:24px;flex-wrap:wrap}}
h1{{margin:0 0 6px;font-size:21px;letter-spacing:-.02em}}
header p{{margin:0;color:var(--mut);max-width:660px}}
.toggle{{display:flex;gap:2px;background:var(--card);border:1px solid var(--line);border-radius:22px;padding:3px}}
.toggle button{{padding:6px 13px;border:0;border-radius:18px;background:transparent;color:var(--mut);
  font:inherit;font-size:13px;cursor:pointer}}
.toggle button[aria-pressed="true"]{{background:#3ddbf0;color:#08080a}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(132px,1fr));gap:12px;padding:24px 40px 60px}}
.ic{{margin:0;background:var(--card);border:1px solid var(--line);border-radius:10px;overflow:hidden}}
.ic-box{{height:96px;display:flex;align-items:center;justify-content:center}}
figcaption{{border-top:1px solid var(--line);padding:8px 10px;display:flex;flex-direction:column;gap:2px}}
figcaption code{{font-family:ui-monospace,SFMono-Regular,Menlo,monospace;font-size:11.5px;
  color:var(--fg);user-select:all}}
figcaption span{{font-size:11px;color:var(--mut)}}
.warn{{margin:0 40px;padding:12px 16px;border-left:3px solid #e0563f;background:var(--card);
  border-radius:0 8px 8px 0;color:var(--mut);font-size:13px}}
.warn code{{color:var(--fg)}}
</style></head><body>
<header>
  <div>
    <h1>Iconos animados · Lordicon</h1>
    <p>{len(icons)} iconos verificados contra el CDN. Haz clic sobre el ID para seleccionarlo y pégalo
    en cualquier slot <code>ICON</code> o <code>icon</code>: el runtime lo convierte en icono animado
    y lo colorea con los tokens del pack.</p>
  </div>
  <div class="toggle" role="group" aria-label="Tema">
    <button data-t="light" aria-pressed="false">Claro</button>
    <button data-t="dark" aria-pressed="true">Oscuro</button>
  </div>
</header>
<p class="warn"><b>Descartados:</b> <code>{roto}</code> devuelven 404 en el CDN.
Aparecen en presentaciones de <code>cursos/</code> y ahí no se ven.</p>
<div class="grid">{cards}</div>
<script>
document.querySelectorAll('.toggle button').forEach(function (b) {{
  b.addEventListener('click', function () {{
    document.documentElement.setAttribute('data-theme', b.dataset.t);
    document.querySelectorAll('.toggle button').forEach(function (o) {{
      o.setAttribute('aria-pressed', String(o === b));
    }});
  }});
}});
</script>
</body></html>"""

    open(os.path.join(OUT, "icons.html"), "w", encoding="utf-8").write(html)
    return len(icons)


def main():
    showcase = sys.argv[1] if len(sys.argv) > 1 else "dark_tech"
    for sub in ("archetypes", "packs"):
        if os.path.isdir(os.path.join(OUT, sub)):
            shutil.rmtree(os.path.join(OUT, sub))
    os.makedirs(OUT, exist_ok=True)
    thumbs_dir = os.path.join(OUT, "thumbs")

    by_id = {a: s for a, s in DEMO}

    arch_items = render(showcase, DEMO, os.path.join(OUT, "archetypes"))

    packs = sorted(
        d for d in os.listdir(PACKS_DIR)
        if os.path.isdir(os.path.join(PACKS_DIR, d)) and not d.startswith("_")
    )
    pack_items = []
    for p in packs:
        entries = [(a, by_id[a]) for a in PACK_SAMPLE]
        made = render(p, entries, os.path.join(OUT, "packs", p))
        meta = json.load(open(os.path.join(PACKS_DIR, p, "pack.json"), encoding="utf-8"))
        pack_items.append((p, meta.get("name", p), meta.get("best_for", []), made))

    a_cells, tw, th = thumbs(arch_items, "archetypes")

    p_blocks = ""
    for pid, name, best, made in pack_items:
        cells = ""
        for n, _lbl in made:
            png = os.path.join(thumbs_dir, f"{pid}__{n[:-5]}.png")
            inner = (f'<img src="thumbs/{pid}__{n[:-5]}.png">' if os.path.isfile(png)
                     else f'<iframe src="packs/{pid}/{n}" scrolling="no" loading="lazy"></iframe>')
            cells += f'<a class="cell" href="packs/{pid}/{n}" target="_blank">{inner}</a>'
        tags = " · ".join(best[:3]) if best else ""
        p_blocks += (
            f'<section class="pack"><h3>{name} <code>{pid}</code></h3>'
            f'<p class="best">{tags}</p><div class="row">{cells}</div></section>'
        )

    html = f"""<!DOCTYPE html><html lang="es"><head><meta charset="UTF-8">
<title>Muestrario · EVA Presentation Generator</title>
<style>
*{{box-sizing:border-box}}
body{{margin:0;background:#0e0e10;color:#e8e8ea;font:14px/1.5 system-ui,-apple-system,sans-serif}}
header{{padding:32px 40px 20px;border-bottom:1px solid #26262b}}
h1{{margin:0 0 6px;font-size:22px;letter-spacing:-.02em}}
header p{{margin:0;color:#9a9aa4}}
h2{{margin:36px 40px 4px;font-size:15px;letter-spacing:.14em;text-transform:uppercase;color:#8f8f99}}
.hint{{margin:0 40px 18px;color:#6f6f79;font-size:12.5px}}
.grid{{display:flex;flex-wrap:wrap;gap:12px;padding:0 40px 24px}}
.cell{{position:relative;width:{tw}px;height:{th}px;overflow:hidden;border:1px solid #2c2c33;
  border-radius:6px;text-decoration:none;display:block;background:#000}}
.cell:hover{{border-color:#6b6bff}}
.cell iframe{{width:1280px;height:720px;border:0;transform:scale({tw/1280});transform-origin:0 0;pointer-events:none}}
.cell img{{width:100%;height:100%;display:block}}
.cell span{{position:absolute;left:0;bottom:0;right:0;background:rgba(0,0,0,.78);color:#fff;
  font-size:10.5px;padding:3px 6px;letter-spacing:.06em}}
.pack{{padding:0 40px 6px}}
.pack h3{{margin:20px 0 2px;font-size:15px;font-weight:600}}
.pack h3 code{{color:#7a7a86;font-weight:400;font-size:12px;margin-left:6px}}
.best{{margin:0 0 8px;color:#6f6f79;font-size:12px}}
.row{{display:flex;gap:10px}}
.row .cell{{width:{tw}px;height:{th}px}}
footer{{padding:28px 40px 60px;color:#6f6f79;font-size:12.5px;border-top:1px solid #26262b;margin-top:28px}}
</style></head><body>
<header>
  <h1>Muestrario · EVA Presentation Generator</h1>
  <p>{len(arch_items)} arquetipos · {len(pack_items)} packs · lienzo 1280×720. Clic en cualquier miniatura para abrirla a tamaño real.
  &nbsp;—&nbsp; <a href="icons.html" style="color:#6b6bff">Muestrario de iconos animados →</a></p>
</header>

<h2>Arquetipos — las diagramaciones</h2>
<p class="hint">Los {len(arch_items)} arquetipos con contenido real, renderizados en <strong>{showcase}</strong>. Esto es lo que define dónde va cada cosa.</p>
<div class="grid">{a_cells}</div>

<h2>Packs — la estética</h2>
<p class="hint">Las mismas tres slides (portada, principio, tarjetas) en los {len(pack_items)} packs. Mismo contenido, misma diagramación: lo único que cambia es el pack.</p>
{p_blocks}

<footer>Generado por <code>scripts/make_gallery.py</code>. Regenerar tras tocar cualquier frame o arquetipo.</footer>
</body></html>"""

    path = os.path.join(OUT, "index.html")
    open(path, "w", encoding="utf-8").write(html)
    n_icons = build_icons()
    print(path)
    print(f"{len(arch_items)} arquetipos · {len(pack_items)} packs · {n_icons} iconos")


if __name__ == "__main__":
    main()
