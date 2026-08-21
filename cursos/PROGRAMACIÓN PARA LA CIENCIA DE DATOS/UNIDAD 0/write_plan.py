import json
import os

unit_path = r"C:\Users\vicen\OneDrive\Escritorio\EVA IPSS\academy-portal\cursos\PROGRAMACIÓN PARA LA CIENCIA DE DATOS\UNIDAD 0"
plan_path = os.path.join(unit_path, "visual_plan.json")

data = {
  "pack": "fresh_green",
  "title": "Unidad 0 — Programación para la Ciencia de Datos",
  "slides": [
    {
      "archetype": "cover",
      "title": "Bienvenida e Introducción",
      "notes": "Bienvenidos a la asignatura Programación para la Ciencia de Datos. Esta es la unidad cero, donde presentaremos el curso, la metodología y las bases fundamentales.",
      "slots": {
        "EYEBROW": "UNIDAD 0",
        "TITLE": "Bienvenida y<br>Fundamentos",
        "SUBTITLE": "Programación para la Ciencia de Datos",
        "BG_IMAGE": "",
        "CHIPS": [
          { "label": "72 Horas", "accent": "var(--a1)" },
          { "label": "Trimestre 3", "accent": "var(--a2)" }
        ]
      }
    },
    {
      "archetype": "toc",
      "title": "Mapa de la Sesión",
      "notes": "Hoy revisaremos 5 puntos principales: la presentación del curso, el programa de la asignatura, la metodología, las bases de programación y un caso práctico inicial.",
      "slots": {
        "TAG_LEFT": "Unidad 0",
        "TITLE": "Mapa de la Sesión",
        "TAG_RIGHT": "S1",
        "ROWS": "2",
        "COLS": "3",
        "ITEMS": [
          { "num": "01", "icon": "qhsqomla", "title": "Bienvenida", "desc": "Propósito y presentación." },
          { "num": "02", "icon": "yyecauzv", "title": "El Programa", "desc": "Unidades de aprendizaje." },
          { "num": "03", "icon": "wzpjhhhq", "title": "Metodología", "desc": "Evaluaciones y ABP." },
          { "num": "04", "icon": "qgcohzrn", "title": "Bases Técnicas", "desc": "Python y librerías." },
          { "num": "05", "icon": "gqdyesfu", "title": "Caso Práctico", "desc": "Atención sanitaria." },
          { "num": "06", "icon": "dxjqoygy", "title": "Cierre", "desc": "Próximos pasos." }
        ]
      }
    },
    {
      "archetype": "section",
      "title": "Bloque 1: Bienvenida al Curso",
      "notes": "Comenzamos con la introducción general y la presentación del docente.",
      "slots": {
        "PART_LABEL": "Bloque 1",
        "TITLE": "Bienvenida al Curso",
        "SUBTITLE": "Introducción al propósito y objetivos de la asignatura.",
        "AGENDA": [
          { "label": "1.1", "text": "Bienvenida" },
          { "label": "1.2", "text": "Presentación del Docente" }
        ]
      }
    },
    {
      "archetype": "quote",
      "title": "El rol de la programación",
      "notes": "La programación es la herramienta esencial que nos permite transformar datos brutos en conocimiento accionable.",
      "slots": {
        "QUOTE": "La programación es la herramienta esencial en la ciencia de datos, permitiendo preparar y depurar información para proyectos reales.",
        "AUTHOR": "Descripción del Curso",
        "ROLE": "Programa de Asignatura",
        "CONTEXT_LABEL": "PROPÓSITO",
        "CONTEXT": "Transformar datos en conocimiento."
      }
    },
    {
      "archetype": "anatomy",
      "title": "Perfil del Docente",
      "notes": "Me presento brevemente. Soy especialista en ciencias de la computación con años de experiencia aplicada.",
      "slots": {
        "TAG_LEFT": "Docente",
        "TITLE": "Experiencia y Perfil",
        "TAG_RIGHT": "S1",
        "SPEC_TITLE": "Resumen Profesional",
        "FIELDS": [
          { "key": "Área", "value": "Informática / Ciencias de la Computación", "highlight": "" },
          { "key": "Experiencia Laboral", "value": "+3 a 5 años en ciencia de datos", "highlight": "hi" },
          { "key": "Experiencia Docente", "value": "2+ años en Educación Superior", "highlight": "" },
          { "key": "Especialidad", "value": "Técnicas de datos en entornos industriales", "highlight": "" },
          { "key": "Rol", "value": "Guía en Aprendizaje Basado en Problemas", "highlight": "" }
        ],
        "NOTES": [
          { "n": "1", "title": "Experiencia", "text": "Aplicación práctica en proyectos relevantes." },
          { "n": "2", "title": "Guía", "text": "Acompañamiento en el desarrollo de competencias." }
        ]
      }
    },
    {
      "archetype": "section",
      "title": "Bloque 2: El Programa",
      "notes": "Revisemos ahora la estructura del programa de asignatura, las horas y la competencia principal que desarrollaremos.",
      "slots": {
        "PART_LABEL": "Bloque 2",
        "TITLE": "El Programa de Asignatura",
        "SUBTITLE": "Competencias y unidades de aprendizaje.",
        "AGENDA": [
          { "label": "2.1", "text": "Datos Generales" },
          { "label": "2.2", "text": "Competencia Global" },
          { "label": "2.3", "text": "Ruta de Aprendizaje" }
        ]
      }
    },
    {
      "archetype": "metrics",
      "title": "Datos clave de la asignatura",
      "notes": "La asignatura cuenta con 72 horas en total, fuertemente enfocadas en la teoría aplicada y el taller.",
      "slots": {
        "TAG_LEFT": "El Programa",
        "TITLE": "Estructura Horaria",
        "TAG_RIGHT": "S1",
        "LEAD": "Distribución de las 72 horas totales del curso.",
        "COLS": "3",
        "SOURCE": "Programa de Asignatura 2025",
        "METRICS": [
          { "label": "Horas Teóricas", "value": "40", "unit": "h", "desc": "Conceptos y fundamentos.", "pct": "55%" },
          { "label": "Horas Taller", "value": "32", "unit": "h", "desc": "Aplicación práctica en Python.", "pct": "45%" },
          { "label": "Horas Prácticas/Lab", "value": "0", "unit": "h", "desc": "El taller suple esta necesidad.", "pct": "0%" }
        ]
      }
    },
    {
      "archetype": "quote",
      "title": "Competencia de la asignatura",
      "notes": "El nivel de dominio esperado es 5. Deberán codificar algoritmos completos, desde la entrada hasta la salida.",
      "slots": {
        "QUOTE": "Codificar secuencias lógicas de algoritmos para el tratamiento de datos, abordando entradas, operaciones y salidas.",
        "AUTHOR": "Competencia Global",
        "ROLE": "Nivel de Dominio: 5",
        "CONTEXT_LABEL": "OBJETIVO",
        "CONTEXT": "Responder a los requerimientos del usuario/cliente."
      }
    },
    {
      "archetype": "timeline",
      "title": "Ruta de Aprendizaje",
      "notes": "El curso se divide en 3 unidades principales, culminando con la evaluación final integradora.",
      "slots": {
        "TAG_LEFT": "El Programa",
        "TITLE": "Unidades de Aprendizaje",
        "TAG_RIGHT": "S1",
        "LEAD": "La progresión que seguiremos durante el trimestre.",
        "COLS": "4",
        "STEPS": [
          { "n": "01", "phase": "UNIDAD 1", "title": "Fundamentos", "desc": "Programación y manipulación.", "output": "10% ponderación" },
          { "n": "02", "phase": "UNIDAD 2", "title": "Procesamiento", "desc": "Transformación de datos.", "output": "20% ponderación" },
          { "n": "03", "phase": "UNIDAD 3", "title": "Optimización", "desc": "Depuración y análisis.", "output": "30% ponderación" },
          { "n": "04", "phase": "FINAL", "title": "Integración", "desc": "Evaluación final de la asignatura.", "output": "40% ponderación" }
        ]
      }
    },
    {
      "archetype": "section",
      "title": "Bloque 3: Las Unidades en Detalle",
      "notes": "Veamos qué contiene exactamente cada una de las 3 unidades de competencia.",
      "slots": {
        "PART_LABEL": "Bloque 3",
        "TITLE": "Las Unidades en Detalle",
        "SUBTITLE": "Desglose de los resultados de aprendizaje esperados.",
        "AGENDA": [
          { "label": "3.1", "text": "Unidad 1" },
          { "label": "3.2", "text": "Unidad 2" },
          { "label": "3.3", "text": "Unidad 3" }
        ]
      }
    },
    {
      "archetype": "concept-cards",
      "title": "Unidad 1: Fundamentos",
      "notes": "En la unidad 1, aprenderemos la base del lenguaje Python y cómo manipular estructuras fundamentales.",
      "slots": {
        "TAG_LEFT": "Unidad 1",
        "TITLE": "Fundamentos y Manipulación",
        "TAG_RIGHT": "22 Horas",
        "COLS": "3",
        "CARDS": [
          { "badge": "Conceptos", "title": "Sintaxis Python", "body": "Tipos de datos nativos, diccionarios, listas y tuplas.", "note_label": "OBJETIVO", "note": "Aplicar conceptos" },
          { "badge": "Control", "title": "Estructuras de Flujo", "body": "Condicionales (if/else) y bucles (for, while) para iterar.", "note_label": "OBJETIVO", "note": "Automatizar" },
          { "badge": "Herramientas", "title": "Librerías", "body": "Introducción a pandas y NumPy para operaciones.", "note_label": "OBJETIVO", "note": "Manejo eficiente" }
        ]
      }
    },
    {
      "archetype": "concept-cards",
      "title": "Unidad 2: Procesamiento",
      "notes": "La unidad 2 nos llevará a diseñar e implementar algoritmos para limpiar, transformar y validar conjuntos de datos.",
      "slots": {
        "TAG_LEFT": "Unidad 2",
        "TITLE": "Procesamiento y Transformación",
        "TAG_RIGHT": "22 Horas",
        "COLS": "3",
        "CARDS": [
          { "badge": "Diseño", "title": "Algoritmos", "body": "Construcción de pseudocódigo y estructuración lógica.", "note_label": "ENFOQUE", "note": "Pensamiento estructurado" },
          { "badge": "Limpieza", "title": "Preprocesamiento", "body": "Tratamiento de outliers, nulos y estandarización.", "note_label": "ENFOQUE", "note": "Calidad del dato" },
          { "badge": "Transformación", "title": "Enriquecimiento", "body": "Normalización, parseo de fechas y agrupaciones (groupby).", "note_label": "ENFOQUE", "note": "Datos listos para análisis" }
        ]
      }
    },
    {
      "archetype": "concept-cards",
      "title": "Unidad 3: Optimización",
      "notes": "Finalmente, en la unidad 3, nos enfocaremos en hacer que nuestro código sea robusto, libre de errores y rápido.",
      "slots": {
        "TAG_LEFT": "Unidad 3",
        "TITLE": "Depuración y Optimización",
        "TAG_RIGHT": "22 Horas",
        "COLS": "3",
        "CARDS": [
          { "badge": "Debugging", "title": "Depuración", "body": "Identificación de errores, manejo de excepciones (try/except).", "note_label": "META", "note": "Código robusto" },
          { "badge": "Validación", "title": "Pruebas", "body": "Diseño de casos de prueba simples y assertions.", "note_label": "META", "note": "Verificación de resultados" },
          { "badge": "Rendimiento", "title": "Optimización", "body": "Refactorización, vectorización con NumPy y profiling básico.", "note_label": "META", "note": "Eficiencia" }
        ]
      }
    },
    {
      "archetype": "quiz",
      "title": "Compruebo mi aprendizaje - Unidades",
      "notes": "Veamos si recordamos las horas y ponderaciones.",
      "slots": {
        "TAG_LEFT": "Revisión",
        "TITLE": "¿Cuánto vale la evaluación final de la asignatura?",
        "TAG_RIGHT": "S1",
        "BADGE": "Pregunta",
        "QUESTION": "Selecciona la ponderación correcta para la evaluación final:",
        "COLS": "2",
        "EXPLANATION_LABEL": "Respuesta",
        "EXPLANATION": "La evaluación final integradora tiene una ponderación del 40% del total de la asignatura.",
        "OPTIONS": [
          { "key": "A", "text": "10%", "correct": "" },
          { "key": "B", "text": "20%", "correct": "" },
          { "key": "C", "text": "30%", "correct": "" },
          { "key": "D", "text": "40%", "correct": "ok" }
        ]
      }
    },
    {
      "archetype": "section",
      "title": "Bloque 4: Metodología y Evaluación",
      "notes": "Ahora pasaremos a entender cómo vamos a aprender y cómo seremos evaluados.",
      "slots": {
        "PART_LABEL": "Bloque 4",
        "TITLE": "Metodología y Evaluación",
        "SUBTITLE": "Cómo aprenderemos a lo largo del trimestre.",
        "AGENDA": [
          { "label": "4.1", "text": "Aprendizaje Basado en Problemas" },
          { "label": "4.2", "text": "Instrumentos de Evaluación" }
        ]
      }
    },
    {
      "archetype": "principle",
      "title": "Metodología ABP",
      "notes": "El Aprendizaje Basado en Problemas es el corazón de nuestra metodología. No solo escucharemos teoría, sino que la aplicaremos en escenarios reales.",
      "slots": {
        "TAG_LEFT": "Metodología",
        "TITLE": "Aprendizaje Basado en Problemas (ABP)",
        "TAG_RIGHT": "S1",
        "GHOST": "ABP",
        "KICKER": "ENFOQUE ACTIVO",
        "PRINCIPLE": "Se privilegia la resolución de problemas relacionados a la manipulación y análisis de datos.",
        "PRINCIPLE_BODY": "Esta estrategia activa asegura que la comprensión teórica se refuerce mediante la experiencia práctica.",
        "LIST_TITLE": "Componentes de la Metodología:",
        "FACTORS": [
          { "name": "Práctica", "text": "Ejecución directa en Python.", "color": "var(--a1)" },
          { "name": "Contexto", "text": "Escenarios laborales reales.", "color": "var(--a2)" },
          { "name": "Feedback", "text": "Retroalimentación continua.", "color": "var(--a1)" }
        ],
        "EXAMPLES": [
          { "tag": "FORMATIVA", "value": "1", "label": "Evaluaciones orientadoras", "desc": "Entregas parciales sin nota directa.", "color": "var(--a1)" },
          { "tag": "SUMATIVA", "value": "4", "label": "Evaluaciones con calificación", "desc": "Miden el logro del aprendizaje.", "color": "var(--a2)" }
        ]
      }
    },
    {
      "archetype": "table",
      "title": "Ponderaciones de Evaluación",
      "notes": "Aquí está el desglose de nuestras 4 notas importantes. Las unidades progresan de 10% a 30%, terminando con el 40% final.",
      "slots": {
        "TAG_LEFT": "Evaluaciones",
        "TITLE": "Esquema de Calificaciones",
        "TAG_RIGHT": "S1",
        "LEAD": "Todas las evaluaciones son prácticas (rúbrica).",
        "HEADERS": "<th>Unidad</th><th>Situación</th><th>Instrumento</th><th>Ponderación</th>",
        "NOTE_LABEL": "IMPORTANTE",
        "NOTE": "El examen final incluye ejercicios de codificación en tiempo limitado.",
        "ROWS": [
          { "cells": "<td>U1. Fundamentos</td><td>Ejecución Práctica</td><td><span class=\"st-pill st-now\">Rúbrica</span></td><td><b>10%</b></td>" },
          { "cells": "<td>U2. Algoritmos</td><td>Ejecución Práctica</td><td><span class=\"st-pill st-now\">Rúbrica</span></td><td><b>20%</b></td>" },
          { "cells": "<td>U3. Depuración</td><td>Ejecución Práctica</td><td><span class=\"st-pill st-now\">Rúbrica</span></td><td><b>30%</b></td>" },
          { "cells": "<td>Evaluación Final</td><td>Ejecución Práctica</td><td><span class=\"st-pill st-next\">Rúbrica (6 hrs)</span></td><td><b>40%</b></td>" }
        ]
      }
    },
    {
      "archetype": "callouts",
      "title": "Reglas para el Taller",
      "notes": "Algunos recordatorios para el desarrollo fluido de las clases prácticas.",
      "slots": {
        "TAG_LEFT": "El Taller",
        "TITLE": "Recomendaciones Clave",
        "TAG_RIGHT": "S1",
        "LEAD": "Para tener éxito en este curso altamente práctico:",
        "CALLOUTS": [
          { "kind": "info", "icon": "hwwxhzgs", "title": "Participación Activa", "text": "Los talleres requieren tu involucramiento directo escribiendo código." },
          { "kind": "tip", "icon": "lhjllvga", "title": "Prueba y Error", "text": "No temas equivocarte. La depuración es el 50% de la programación." },
          { "kind": "warn", "icon": "msoeawqm", "title": "Asistencia", "text": "Dado que el conocimiento es acumulativo, faltar te retrasará rápidamente." },
          { "kind": "note", "icon": "pithnlch", "title": "Herramientas", "text": "Contaremos con laboratorios y plataformas virtuales (EVA)." }
        ]
      }
    },
    {
      "archetype": "section",
      "title": "Bloque 5: Bases de Programación",
      "notes": "Entramos de lleno a repasar los conceptos fundamentales de Python que usaremos.",
      "slots": {
        "PART_LABEL": "Bloque 5",
        "TITLE": "Bases de Programación",
        "SUBTITLE": "Conceptos introductorios a la Unidad 1.",
        "AGENDA": [
          { "label": "5.1", "text": "El Ecosistema Python" },
          { "label": "5.2", "text": "Sintaxis y Estructuras" },
          { "label": "5.3", "text": "Pandas y Visualización" }
        ]
      }
    },
    {
      "archetype": "concept-cards",
      "title": "El Ecosistema Python",
      "notes": "Python no trabaja solo. Para la ciencia de datos, nos apoyamos en librerías altamente optimizadas.",
      "slots": {
        "TAG_LEFT": "Bases",
        "TITLE": "Las Herramientas",
        "TAG_RIGHT": "S1",
        "COLS": "3",
        "CARDS": [
          { "badge": "Lenguaje", "title": "Python", "body": "Lenguaje base de sintaxis clara. Soporta estructuras nativas y control de flujo.", "note_label": "ROL", "note": "El pegamento de todo" },
          { "badge": "Librería", "title": "NumPy", "body": "Computación numérica eficiente. Operaciones vectorizadas en arrays N-dimensionales.", "note_label": "ROL", "note": "Motor matemático" },
          { "badge": "Librería", "title": "Pandas", "body": "Manipulación de datos tabulares a través de DataFrames y Series.", "note_label": "ROL", "note": "Hoja de cálculo en código" }
        ]
      }
    },
    {
      "archetype": "code",
      "title": "Sintaxis Básica",
      "notes": "La indentación es clave en Python. Observemos un ejemplo simple de if/else.",
      "slots": {
        "TAG_LEFT": "Sintaxis",
        "TITLE": "La legibilidad de Python",
        "TAG_RIGHT": "S1",
        "SPLIT": "1fr 1.2fr",
        "LEAD": "Python utiliza indentación (espacios) en lugar de llaves { } para definir bloques.",
        "CALLOUT_LABEL": "CLAVE",
        "CALLOUT": "Sin la indentación correcta, el programa arrojará error.",
        "FILENAME": "ejemplo.py",
        "CODE": "<span class=\"c-cm\"># Variables y tipos</span>\n<span class=\"c-kw\">ciudad</span> = <span class=\"c-str\">\"Valdivia\"</span>\n<span class=\"c-kw\">temperatura</span> = <span class=\"c-num\">20</span>\n\n<span class=\"c-kw\">if</span> temperatura > <span class=\"c-num\">25</span>:\n    <span class=\"c-fn\">print</span>(<span class=\"c-str\">\"Hace calor en\"</span>, ciudad)\n<span class=\"c-kw\">else</span>:\n    <span class=\"c-fn\">print</span>(<span class=\"c-str\">\"Clima templado en\"</span>, ciudad)",
        "STEPS": [
          { "n": "1", "text": "Variables de tipado dinámico (no se declara tipo)." },
          { "n": "2", "text": "Dos puntos (:) abren un nuevo bloque lógico." },
          { "n": "3", "text": "El código anidado lleva 4 espacios de indentación." },
          { "n": "4", "text": "Uso de comentarios con el símbolo #." }
        ]
      }
    },
    {
      "archetype": "feature-matrix",
      "title": "Estructuras de Datos Nativas",
      "notes": "Listas, tuplas y diccionarios sirven para distintos propósitos en la agrupación de información.",
      "slots": {
        "TAG_LEFT": "Estructuras",
        "TITLE": "Agrupando Valores",
        "TAG_RIGHT": "S1",
        "LEAD": "Comparativa de las colecciones nativas más usadas en Python.",
        "HEADERS": "<th>Estructura</th><th>Mutable</th><th class=\"best\">Ordenada</th><th>Caso de Uso</th>",
        "NOTE_LABEL": "NOTA",
        "NOTE": "Mutable significa que puede modificarse después de crearse.",
        "ROWS": [
          { "cells": "<td><b>Listas [ ]</b></td><td><span class=\"mk yes\">✓</span></td><td class=\"best\"><span class=\"mk yes\">✓</span></td><td>Colecciones variables de datos (ej. temperaturas)</td>" },
          { "cells": "<td><b>Tuplas ( )</b></td><td><span class=\"mk no\">✗</span></td><td class=\"best\"><span class=\"mk yes\">✓</span></td><td>Datos fijos o posicionales (ej. coordenadas lat/lon)</td>" },
          { "cells": "<td><b>Diccionarios { }</b></td><td><span class=\"mk yes\">✓</span></td><td class=\"best\"><span class=\"mk part\">~</span></td><td>Pares clave-valor (ej. región -> capital)</td>" },
          { "cells": "<td><b>Cadenas \" \"</b></td><td><span class=\"mk no\">✗</span></td><td class=\"best\"><span class=\"mk yes\">✓</span></td><td>Secuencia de caracteres (texto)</td>" }
        ]
      }
    },
    {
      "archetype": "dodont",
      "title": "Control de Flujo: For vs While",
      "notes": "Usaremos for la gran mayoría de las veces para recorrer datasets.",
      "slots": {
        "TAG_LEFT": "Control",
        "TITLE": "¿Cuándo usar For o While?",
        "TAG_RIGHT": "S1",
        "BAD_TITLE": "Bucle While",
        "BAD_SNIPPET": "<span class=\"c-kw\">while</span> fondos < <span class=\"c-num\">2000000</span>:\n    fondos *= <span class=\"c-num\">1.05</span>\n    anos += <span class=\"c-num\">1</span>",
        "GOOD_TITLE": "Bucle For",
        "GOOD_SNIPPET": "<span class=\"c-kw\">for</span> valor <span class=\"c-kw\">in</span> ica_diario:\n    <span class=\"c-kw\">if</span> valor > <span class=\"c-num\">150</span>:\n        <span class=\"c-fn\">print</span>(<span class=\"c-str\">\"Alerta\"</span>)",
        "WHY_LABEL": "REGLA GENERAL",
        "WHY": "En ciencia de datos, rara vez iteramos sin saber el tamaño del dataset. Preferimos <b>for</b> para colecciones conocidas.",
        "BAD_POINTS": [
          { "text": "Repeticiones basadas en condición lógica." },
          { "text": "Riesgo de bucles infinitos." },
          { "text": "Menos usado en iteración de datasets." },
          { "text": "Útil para leer streams hasta agotarlos." }
        ],
        "GOOD_POINTS": [
          { "text": "Iteración sobre elementos de secuencia." },
          { "text": "Ideal para recorrer listas o arrays." },
          { "text": "Seguro: termina al agotar secuencia." },
          { "text": "Permite uso de funciones como enumerate." }
        ]
      }
    },
    {
      "archetype": "concept-cards",
      "title": "El poder de pandas",
      "notes": "Pandas es el estándar para el análisis tabular en Python.",
      "slots": {
        "TAG_LEFT": "Pandas",
        "TITLE": "Operaciones Fundamentales",
        "TAG_RIGHT": "S1",
        "COLS": "3",
        "CARDS": [
          { "badge": "Paso 1", "title": "Carga e Inspección", "body": "Uso de pd.read_csv() para cargar DataFrames y df.head() o df.info() para revisión inicial.", "note_label": "OPERACIÓN", "note": "Ingesta" },
          { "badge": "Paso 2", "title": "Filtrado y Selección", "body": "Aplicación de máscaras booleanas para filtrar filas que cumplen con ciertas condiciones lógicas.", "note_label": "OPERACIÓN", "note": "Subconjuntos" },
          { "badge": "Paso 3", "title": "Agregación", "body": "Cálculo de estadísticas resumen como sum(), mean(), max() o creación de columnas derivadas.", "note_label": "OPERACIÓN", "note": "Métricas" }
        ]
      }
    },
    {
      "archetype": "chart-bars",
      "title": "Visualización con Matplotlib",
      "notes": "Matplotlib nos permite ver rápidamente disparidades, como la población concentrada en la capital.",
      "slots": {
        "TAG_LEFT": "Visualización",
        "TITLE": "Población por Región (Ejemplo)",
        "TAG_RIGHT": "S1",
        "LEAD": "La creación de gráficos complementa las tablas para hacer evidentes los hallazgos.",
        "COLS": "6",
        "SCALE_TOP": "7.1M",
        "SCALE_MID": "3.5M",
        "SCALE_BASE": "0",
        "READ_LABEL": "HALLAZGO",
        "READ": "La Región Metropolitana concentra abrumadoramente la población comparada con las demás.",
        "SOURCE": "Datos de ejemplo del apunte U1",
        "BARS": [
          { "label": "RM", "sub": "Centro", "value": "7100000", "unit": "", "tone": "" },
          { "label": "Valp.", "sub": "Centro", "value": "1800000", "unit": "", "tone": "alt" },
          { "label": "Biobío", "sub": "Sur", "value": "1550000", "unit": "", "tone": "alt" },
          { "label": "Arauc.", "sub": "Sur", "value": "1000000", "unit": "", "tone": "mute" },
          { "label": "Atacama", "sub": "Norte", "value": "300000", "unit": "", "tone": "mute" },
          { "label": "Aysén", "sub": "Sur", "value": "110000", "unit": "", "tone": "warn" }
        ]
      }
    },
    {
      "archetype": "section",
      "title": "Bloque 6: Caso Práctico",
      "notes": "Para cerrar la sesión, veamos un caso práctico real que ilustra el flujo de trabajo.",
      "slots": {
        "PART_LABEL": "Bloque 6",
        "TITLE": "Caso: Capacidad Sanitaria",
        "SUBTITLE": "Aplicando lo aprendido en un escenario logístico/salud.",
        "AGENDA": [
          { "label": "6.1", "text": "Contexto del Caso" },
          { "label": "6.2", "text": "Diccionario de Datos" },
          { "label": "6.3", "text": "Flujo de Resolución" }
        ]
      }
    },
    {
      "archetype": "anatomy",
      "title": "Contexto del Caso",
      "notes": "Debemos entregar un informe ejecutivo basado en el cruce de datos demográficos y sanitarios.",
      "slots": {
        "TAG_LEFT": "El Caso",
        "TITLE": "Atención Sanitaria Regional 2025",
        "TAG_RIGHT": "S1",
        "SPEC_TITLE": "Misión del Analista",
        "FIELDS": [
          { "key": "Organismo", "value": "Subdirección de Planificación de Salud", "highlight": "" },
          { "key": "Objetivo", "value": "Priorizar refuerzos de personal en regiones", "highlight": "hi" },
          { "key": "Fuente de Datos", "value": "Archivo CSV agregado a nivel regional 2025", "highlight": "" },
          { "key": "Entregable", "value": "Breve resumen ejecutivo con evidencias", "highlight": "" },
          { "key": "Tareas", "value": "Cargar, explorar, limpiar, transformar y visualizar", "highlight": "" }
        ],
        "NOTES": [
          { "n": "1", "title": "Urgencia", "text": "Se requiere un informe express." },
          { "n": "2", "title": "Impacto", "text": "Toma de decisiones en asignación de recursos." }
        ]
      }
    },
    {
      "archetype": "table",
      "title": "Diccionario de Datos",
      "notes": "Entender los datos es el primer paso antes de programar cualquier algoritmo.",
      "slots": {
        "TAG_LEFT": "El Caso",
        "TITLE": "Antecedentes del CSV",
        "TAG_RIGHT": "S1",
        "LEAD": "Estructura de las columnas en nuestro dataset.",
        "HEADERS": "<th>Columna</th><th>Tipo</th><th>Descripción</th>",
        "NOTE_LABEL": "VERIFICACIÓN",
        "NOTE": "Revisar posibles nulos y confirmar que los tipos de datos en pandas (int64) coincidan con el diccionario.",
        "ROWS": [
          { "cells": "<td><b>region</b></td><td>str (object)</td><td>Nombre de la región</td>" },
          { "cells": "<td><b>poblacion</b></td><td>int</td><td>Habitantes estimados 2025</td>" },
          { "cells": "<td><b>superficie_km2</b></td><td>int/float</td><td>Superficie en km²</td>" },
          { "cells": "<td><b>medicos</b></td><td>int</td><td>Nº de médicos/as en red pública</td>" },
          { "cells": "<td><b>consultorios</b></td><td>int</td><td>Cantidad de establecimientos APS</td>" },
          { "cells": "<td><b>atenciones_2025</b></td><td>int</td><td>Total de atenciones (ene-jun)</td>" }
        ]
      }
    },
    {
      "archetype": "timeline",
      "title": "Flujo de Resolución",
      "notes": "El caso se resuelve en 4 pasos progresivos, desde la carga hasta el reporte.",
      "slots": {
        "TAG_LEFT": "El Caso",
        "TITLE": "Pasos del Script",
        "TAG_RIGHT": "S1",
        "LEAD": "La secuencia de operaciones en pandas y python.",
        "COLS": "4",
        "STEPS": [
          { "n": "01", "phase": "Exploración", "title": "Carga inicial", "desc": "pd.read_csv() y df.info()", "output": "Conocer la estructura" },
          { "n": "02", "phase": "Limpieza", "title": "Consistencia", "desc": "Verificar >= 0 y corregir con abs()", "output": "Datos válidos" },
          { "n": "03", "phase": "Transformación", "title": "Derivadas", "desc": "Cálculo de densidad y ratios", "output": "Nuevas métricas" },
          { "n": "04", "phase": "Reporte", "title": "Priorización", "desc": "Filtrar (densidad > 100) y graficar", "output": "Regiones críticas" }
        ]
      }
    },
    {
      "archetype": "quiz",
      "title": "Compruebo mi aprendizaje - Datos",
      "notes": "Una pregunta rápida de reflexión.",
      "slots": {
        "TAG_LEFT": "Reflexión",
        "TITLE": "Consistencia de Datos",
        "TAG_RIGHT": "S1",
        "BADGE": "Pregunta",
        "QUESTION": "¿Por qué es vital validar que la población no sea negativa antes de calcular la densidad?",
        "COLS": "1",
        "EXPLANATION_LABEL": "Respuesta",
        "EXPLANATION": "Porque un valor negativo propagará el error a todas las métricas derivadas (como densidad o atenciones per cápita), arruinando el informe ejecutivo.",
        "OPTIONS": [
          { "key": "A", "text": "Porque Python arroja error sintáctico ante números negativos.", "correct": "" },
          { "key": "B", "text": "Porque invalida los cálculos posteriores llevando a decisiones erróneas.", "correct": "ok" },
          { "key": "C", "text": "Para evitar que el archivo CSV aumente su tamaño en disco.", "correct": "" }
        ]
      }
    },
    {
      "archetype": "resources",
      "title": "Recursos",
      "notes": "Toda esta documentación complementará el aprendizaje.",
      "slots": {
        "TAG_LEFT": "Bibliografía",
        "TITLE": "Material Complementario",
        "TAG_RIGHT": "S1",
        "LIST_TITLE": "Lecturas y Enlaces",
        "QR_LABEL": "ESCANEAR",
        "QR_DATA": "https%3A%2F%2Fpandas.pydata.org%2Fdocs%2Fuser_guide%2F10min.html",
        "QR_ALT": "QR Pandas",
        "QR_CAPTION": "10 Minutos con Pandas",
        "NEXT_LABEL": "Siguiente paso",
        "NEXT": "Instalar Python y repasar el apunte U1.",
        "RESOURCES": [
          { "icon": "hwwxhzgs", "title": "Documentación Python", "desc": "Tipos integrados y estructuras.", "url": "docs.python.org" },
          { "icon": "yyecauzv", "title": "Tutorial Pandas", "desc": "10 minutos para pandas.", "url": "pandas.pydata.org" },
          { "icon": "qgcohzrn", "title": "Matplotlib", "desc": "Guía de gráficos de barras.", "url": "matplotlib.org" },
          { "icon": "dxjqoygy", "title": "Introducción a Python", "desc": "López & Rojas (2021).", "url": "Biblioteca Digital" }
        ]
      }
    },
    {
      "archetype": "closing",
      "title": "Cierre",
      "notes": "Muchas gracias por su atención. Estamos listos para arrancar.",
      "slots": {
        "TAG_LEFT": "Cierre",
        "TITLE": "Fin de la Sesión",
        "TAG_RIGHT": "S1",
        "ICON": "wzpjhhhq",
        "HERO_TITLE": "¡Bienvenidos al Curso!",
        "HERO_TEXT": "La ciencia de datos empieza con una buena base de programación.",
        "LEFT_PANEL_TITLE": "Síntesis",
        "RIGHT_PANEL_TITLE": "Próximos Pasos",
        "NEXT_LABEL": "PRÓXIMA CLASE",
        "NEXT": "Traer el entorno configurado.",
        "TAKEAWAYS": [
          { "n": "1", "text": "Metodología 100% práctica (ABP)." },
          { "n": "2", "text": "Python es nuestra herramienta principal." },
          { "n": "3", "text": "Limpieza y manipulación aseguran el éxito." }
        ],
        "NEXT_STEPS": [
          { "n": "1", "text": "Leer Apunte de la Unidad 1." },
          { "n": "2", "text": "Revisar los casos prácticos." },
          { "n": "3", "text": "Comenzar a codificar." }
        ]
      }
    }
  ]
}

with open(plan_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
