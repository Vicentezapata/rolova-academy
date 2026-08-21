import json
import os

unit_path = r"C:\Users\vicen\OneDrive\Escritorio\EVA IPSS\academy-portal\cursos\PROGRAMACIÓN PARA LA CIENCIA DE DATOS\UNIDAD 3"
os.makedirs(unit_path, exist_ok=True)
plan_path = os.path.join(unit_path, "visual_plan.json")

data = {
  "pack": "fresh_green",
  "title": "Unidad 3 — Depuración y Optimización",
  "slides": [
    {
      "archetype": "cover",
      "title": "Unidad 3",
      "notes": "Bienvenidos a la Unidad 3. Aprenderemos a hacer que nuestros pipelines no solo funcionen, sino que sean rápidos, seguros y mantenibles.",
      "slots": {
        "EYEBROW": "UNIDAD 3",
        "TITLE": "Depuración y<br>Optimización",
        "SUBTITLE": "Programación para la Ciencia de Datos",
        "BG_IMAGE": "",
        "CHIPS": [
          { "label": "Eficiencia", "accent": "var(--a1)" },
          { "label": "Robustez", "accent": "var(--a2)" }
        ]
      }
    },
    {
      "archetype": "toc",
      "title": "Mapa de la Sesión",
      "notes": "Nuestra hoja de ruta para dominar el rendimiento en Python.",
      "slots": {
        "TAG_LEFT": "Unidad 3",
        "TITLE": "Mapa de la Sesión",
        "TAG_RIGHT": "Sincrónica",
        "ROWS": "2",
        "COLS": "3",
        "ITEMS": [
          { "num": "01", "icon": "qhsqomla", "title": "Diagnóstico", "desc": "Medir antes de actuar.", "chips": "" },
          { "num": "02", "icon": "yyecauzv", "title": "Robustez", "desc": "Manejo de excepciones.", "chips": "" },
          { "num": "03", "icon": "wzpjhhhq", "title": "Optimización", "desc": "Vectorización y Memoria.", "chips": "" },
          { "num": "04", "icon": "qgcohzrn", "title": "Pruebas", "desc": "Regresión y Unitarias.", "chips": "" },
          { "num": "05", "icon": "gqdyesfu", "title": "Refactor", "desc": "DRY y mantenibilidad.", "chips": "" },
          { "num": "06", "icon": "dxjqoygy", "title": "Caso E-commerce", "desc": "Mercado Austral.", "chips": "" }
        ]
      }
    },
    {
      "archetype": "section",
      "title": "Bloque 1: Diagnóstico y Perfilado",
      "notes": "No podemos optimizar lo que no medimos.",
      "slots": {
        "PART_LABEL": "Bloque 1",
        "TITLE": "Diagnóstico y Perfilado",
        "SUBTITLE": "Encontrando los cuellos de botella.",
        "AGENDA": [
          { "label": "1.1", "text": "La trampa de la intuición" },
          { "label": "1.2", "text": "Herramientas de Profiling" }
        ]
      }
    },
    {
      "archetype": "quote",
      "title": "Medir antes de optimizar",
      "notes": "Una regla fundamental de la ingeniería de software.",
      "slots": {
        "QUOTE": "La optimización prematura es la raíz de todos los males. Antes de reescribir tu código, debes medir exactamente dónde se está perdiendo el tiempo.",
        "AUTHOR": "Donald Knuth",
        "ROLE": "Científico de la Computación",
        "CONTEXT_LABEL": "PRINCIPIO",
        "CONTEXT": "El 80% del tiempo de ejecución suele concentrarse en el 20% del código."
      }
    },
    {
      "archetype": "concept-cards",
      "title": "Herramientas de Perfilado",
      "notes": "Cómo auditar la velocidad de nuestro script.",
      "slots": {
        "TAG_LEFT": "Profiling",
        "TITLE": "Auditando el Rendimiento",
        "TAG_RIGHT": "U3",
        "COLS": "3",
        "CARDS": [
          { "badge": "%timeit", "title": "Micro-benchmarks", "body": "Comando mágico de Jupyter para medir milisegundos en líneas de código específicas.", "note_label": "USO", "note": "Comparar dos funciones" },
          { "badge": "cProfile", "title": "Perfilado Completo", "body": "Módulo nativo que rastrea cada función llamada, cuántas veces y cuánto tardó.", "note_label": "USO", "note": "Auditar un pipeline entero" },
          { "badge": "Logging", "title": "Trazabilidad", "body": "Escribir timestamps en consola o archivo para entender cuánto tarda cada etapa en producción.", "note_label": "USO", "note": "Monitoreo en vivo" }
        ]
      }
    },
    {
      "archetype": "section",
      "title": "Bloque 2: Robustez y Excepciones",
      "notes": "Un pipeline no debe colapsar abruptamente por un dato faltante.",
      "slots": {
        "PART_LABEL": "Bloque 2",
        "TITLE": "Robustez y Excepciones",
        "SUBTITLE": "Preparando el código para el mundo real.",
        "AGENDA": [
          { "label": "2.1", "text": "Manejo Defensivo" },
          { "label": "2.2", "text": "Bloques Try/Except" }
        ]
      }
    },
    {
      "archetype": "callouts",
      "title": "Causas de Colapso",
      "notes": "Lo que puede salir mal, saldrá mal.",
      "slots": {
        "TAG_LEFT": "Fragilidad",
        "TITLE": "¿Por qué fallan los pipelines diarios?",
        "TAG_RIGHT": "U3",
        "LEAD": "Si el código asume perfección, un solo error de negocio detendrá todo el sistema.",
        "CALLOUTS": [
          { "kind": "danger", "icon": "msoeawqm", "title": "Archivos Inexistentes", "text": "El sistema origen no generó el CSV de hoy. Falla común: FileNotFoundError." },
          { "kind": "warn", "icon": "pithnlch", "title": "Archivos Vacíos", "text": "El CSV existe pero pesa 0 bytes. Falla común: EmptyDataError en Pandas." },
          { "kind": "info", "icon": "lhjllvga", "title": "Tipos Inesperados", "text": "Una columna numérica trae de pronto el string 'N/A', rompiendo sumatorias." }
        ]
      }
    },
    {
      "archetype": "code-criteria",
      "title": "Manejo de Excepciones",
      "notes": "Cómo atajar errores sin matar el proceso.",
      "slots": {
        "TAG_LEFT": "Excepciones",
        "TITLE": "Atrapando Errores Específicos",
        "TAG_RIGHT": "U3",
        "KICKER": "ROBUSTEZ",
        "CODE_TITLE": "Lectura Segura de Archivos",
        "CODE": "<span class=\"c-kw\">try</span>:\n    df = pd.<span class=\"c-fn\">read_csv</span>(<span class=\"c-str\">'diario.csv'</span>)\n    <span class=\"c-fn\">procesar</span>(df)\n<span class=\"c-kw\">except</span> <span class=\"c-kw\">FileNotFoundError</span>:\n    logger.<span class=\"c-fn\">error</span>(<span class=\"c-str\">\"Archivo diario.csv no encontrado. Saltando día.\"</span>)\n<span class=\"c-kw\">except</span> pd.errors.<span class=\"c-kw\">EmptyDataError</span>:\n    logger.<span class=\"c-fn\">warning</span>(<span class=\"c-str\">\"Archivo vacío. Día sin operaciones.\"</span>)\n<span class=\"c-kw\">except</span> <span class=\"c-kw\">Exception</span> <span class=\"c-kw\">as</span> e:\n    logger.<span class=\"c-fn\">critical</span>(<span class=\"c-str\">f\"Error crítico inesperado: {e}\"</span>)",
        "PANEL_TITLE": "Buenas Prácticas",
        "WHY_TITLE": "Continuidad",
        "WHY": "Un pipeline mensual no debería abortarse completamente solo porque el día 15 no hubo ventas. Registra el incidente y continúa.",
        "CRITERIA": [
          { "letter": "E", "name": "Especificidad", "meta": "Atrapa errores exactos primero.", "highlight": "hi" },
          { "letter": "L", "name": "Logging", "meta": "Deja un rastro escrito (no solo print).", "highlight": "" },
          { "letter": "F", "name": "Fallback", "meta": "Define un plan B (ignorar, usar ceros).", "highlight": "" }
        ]
      }
    },
    {
      "archetype": "section",
      "title": "Bloque 3: Optimización Vectorial",
      "notes": "El núcleo de la aceleración matemática en Python.",
      "slots": {
        "PART_LABEL": "Bloque 3",
        "TITLE": "Optimización de Ejecución",
        "SUBTITLE": "Acelerando el procesamiento masivo.",
        "AGENDA": [
          { "label": "3.1", "text": "Vectorización vs Bucles" },
          { "label": "3.2", "text": "Gestión de Memoria (dtypes)" }
        ]
      }
    },
    {
      "archetype": "dodont",
      "title": "Vectorización vs Bucles",
      "notes": "La diferencia entre minutos y milisegundos.",
      "slots": {
        "TAG_LEFT": "Performance",
        "TITLE": "El Pecado del Bucle 'For'",
        "TAG_RIGHT": "U3",
        "BAD_TITLE": "Iteración Fila a Fila (Anti-patrón)",
        "BAD_SNIPPET": "<span class=\"c-kw\">for</span> i, row <span class=\"c-kw\">in</span> df.<span class=\"c-fn\">iterrows</span>():\n    df.loc[i, <span class=\"c-str\">'total'</span>] = row[<span class=\"c-str\">'cant'</span>] * row[<span class=\"c-str\">'precio'</span>]",
        "GOOD_TITLE": "Vectorización Nativa",
        "GOOD_SNIPPET": "<span class=\"c-cm\"># Pandas opera todo el bloque en C</span>\ndf[<span class=\"c-str\">'total'</span>] = df[<span class=\"c-str\">'cant'</span>] * df[<span class=\"c-str\">'precio'</span>]",
        "WHY_LABEL": "MAGNITUD",
        "WHY": "Iterar fila a fila con `.iterrows()` o `.apply()` en millones de registros obliga a Python a interpretar cada celda individualmente, destruyendo el rendimiento.",
        "BAD_POINTS": [
          { "text": "Desperdicia el motor en C de pandas." },
          { "text": "Tarda minutos en 5M de filas." }
        ],
        "GOOD_POINTS": [
          { "text": "Usa registros contiguos de memoria." },
          { "text": "Tarda milisegundos." }
        ]
      }
    },
    {
      "archetype": "feature-matrix",
      "title": "Estrategias de Optimización",
      "notes": "Resumen de técnicas para acelerar.",
      "slots": {
        "TAG_LEFT": "Técnicas",
        "TITLE": "Haciendo Más con Menos",
        "TAG_RIGHT": "U3",
        "LEAD": "Aplica estos ajustes antes de pedir un servidor más potente.",
        "HEADERS": "<th>Técnica</th><th>Impacto Principal</th><th>Ejemplo Práctico</th>",
        "NOTE_LABEL": "CONSEJO",
        "NOTE": "El Lazy Loading (no cargar columnas que no usarás) es el paso 1.",
        "ROWS": [
          { "cells": "<td><b>Vectorización</b></td><td><span class=\"mk yes\">Velocidad CPU</span></td><td>Operar columnas completas de una vez.</td>" },
          { "cells": "<td><b>Uso de .isin()</b></td><td><span class=\"mk yes\">Velocidad CPU</span></td><td>Filtrar sin múltiples condiciones OR anidadas.</td>" },
          { "cells": "<td><b>Categorical Dtypes</b></td><td><span class=\"mk yes\">Memoria RAM</span></td><td><code>df['comuna'] = df['comuna'].astype('category')</code></td>" },
          { "cells": "<td><b>Downcasting Int</b></td><td><span class=\"mk part\">Memoria RAM</span></td><td>Usar int8 (0-255) en vez del default int64.</td>" }
        ]
      }
    },
    {
      "archetype": "section",
      "title": "Bloque 4: Calidad, Pruebas y Refactor",
      "notes": "Asegurando que la optimización no rompió las matemáticas.",
      "slots": {
        "PART_LABEL": "Bloque 4",
        "TITLE": "Pruebas y Mantenibilidad",
        "SUBTITLE": "Confianza absoluta en tu código.",
        "AGENDA": [
          { "label": "4.1", "text": "Pruebas de Exactitud (Unit/Regression)" },
          { "label": "4.2", "text": "Refactorización y DRY" }
        ]
      }
    },
    {
      "archetype": "anatomy",
      "title": "Test de Regresión",
      "notes": "El concepto de regresión en pruebas.",
      "slots": {
        "TAG_LEFT": "Pruebas",
        "TITLE": "Asegurando la Exactitud Matemática",
        "TAG_RIGHT": "U3",
        "SPEC_TITLE": "Prueba de Regresión: ¿Rompí algo al optimizar?",
        "FIELDS": [
          { "key": "Paso 1: Baseline", "value": "Ejecutar la métrica en el script lento original (Ej: Ventas totales = $5M)", "highlight": "" },
          { "key": "Paso 2: Snapshot", "value": "Guardar un dataset sintético o una muestra con esos resultados validados", "highlight": "" },
          { "key": "Paso 3: Optimizar", "value": "Reemplazar los bucles por vectorización ultrarrápida", "highlight": "hi" },
          { "key": "Paso 4: Verificar", "value": "Asegurar que el nuevo script arroja EXACTAMENTE $5M en la misma muestra", "highlight": "hi" }
        ],
        "NOTES": [
          { "n": "1", "title": "Peligro de Joins", "text": "Un merge() mal diseñado duplica filas, arruinando métricas financieras silenciosamente." },
          { "n": "2", "title": "Tolerancia", "text": "En flotantes complejos usa np.isclose()." }
        ]
      }
    },
    {
      "archetype": "callouts",
      "title": "El Arte de Refactorizar",
      "notes": "Pasar de un notebook sucio a código profesional.",
      "slots": {
        "TAG_LEFT": "Mantenibilidad",
        "TITLE": "Limpiando la Casa",
        "TAG_RIGHT": "U3",
        "LEAD": "El código se lee diez veces más de lo que se escribe.",
        "CALLOUTS": [
          { "kind": "tip", "icon": "lhjllvga", "title": "Principio DRY (Don't Repeat Yourself)", "text": "Si copiaste y pegaste un bloque 3 veces, conviértelo en una función." },
          { "kind": "info", "icon": "hwwxhzgs", "title": "Responsabilidad Única", "text": "Separa tu pipeline en funciones lógicas: cargar(), transformar(), calcular(), reportar()." },
          { "kind": "note", "icon": "pithnlch", "title": "Docstrings y Tipado", "text": "Usa type hints (df: pd.DataFrame) y triple comilla para que tus colegas entiendan qué entra y qué sale." }
        ]
      }
    },
    {
      "archetype": "section",
      "title": "Bloque 5: Caso Práctico",
      "notes": "Entrando al eCommerce Mercado Austral.",
      "slots": {
        "PART_LABEL": "Bloque 5",
        "TITLE": "Caso: Mercado Austral",
        "SUBTITLE": "Depuración de un pipeline de E-commerce.",
        "AGENDA": [
          { "label": "5.1", "text": "Contexto y Datasets" },
          { "label": "5.2", "text": "Los Errores del Script" },
          { "label": "5.3", "text": "Entregables del Proyecto" }
        ]
      }
    },
    {
      "archetype": "anatomy",
      "title": "El Escenario",
      "notes": "De qué trata la evaluación final.",
      "slots": {
        "TAG_LEFT": "El Caso",
        "TITLE": "Mercado Austral (E-commerce)",
        "TAG_RIGHT": "U3",
        "SPEC_TITLE": "Rescatando un Pipeline Frágil",
        "FIELDS": [
          { "key": "Empresa", "value": "Mercado Austral (procesa millones de registros al mes)", "highlight": "" },
          { "key": "El Problema", "value": "El script de métricas es lento, se cae seguido y tiene errores de cálculo", "highlight": "hi" },
          { "key": "Métricas Clave", "value": "GMV (Ventas Brutal), Tasa de Devoluciones, Tiempo de Entrega", "highlight": "" },
          { "key": "Tu Misión", "value": "Perfilado -> Corrección -> Aceleración -> Pruebas", "highlight": "hi" }
        ],
        "NOTES": [
          { "n": "1", "title": "El Dato", "text": "Cuidado con los JOINS que inflan el GMV." }
        ]
      }
    },
    {
      "archetype": "table",
      "title": "Los Insumos del Sistema",
      "notes": "Muestra de los CSVs entregados.",
      "slots": {
        "TAG_LEFT": "Insumos",
        "TITLE": "La Telaraña Relacional",
        "TAG_RIGHT": "U3",
        "LEAD": "Recibirás 5 datasets. Cuidado al cruzarlos (Cardinalidad 1 a Muchos).",
        "HEADERS": "<th>Archivo</th><th>Contenido Principal</th><th>Cuidado con...</th>",
        "NOTE_LABEL": "RIESGO",
        "NOTE": "Unir 'orders' (1 fila por pedido) con 'order_items' (N filas por pedido) duplica la cabecera del pedido.",
        "ROWS": [
          { "cells": "<td><b>orders.csv</b></td><td>order_id, date, status</td><td>Las fechas vienen mixtas.</td>" },
          { "cells": "<td><b>order_items.csv</b></td><td>product_id, quantity, price</td><td>Base para calcular el GMV exacto.</td>" },
          { "cells": "<td><b>returns.csv</b></td><td>order_id, return_date</td><td>Solo pedidos devueltos.</td>" },
          { "cells": "<td><b>shipments.csv</b></td><td>shipped_date, delivered_date</td><td>Base para tiempos de entrega.</td>" }
        ]
      }
    },
    {
      "archetype": "activity",
      "title": "Diagnóstico del Pipeline Actual",
      "notes": "Análisis de las fallas requeridas por la pauta.",
      "slots": {
        "TAG_LEFT": "Diagnóstico",
        "TITLE": "Los Pecados del Script Original",
        "TAG_RIGHT": "U3",
        "ICON": "msoeawqm",
        "ACTIVITY_NAME": "Auditoría de Código",
        "INSTRUCTIONS": "El código entregado tiene 4 fallas estructurales que debes corregir de inmediato para tu evaluación.",
        "COLS": "2",
        "META": [
          { "label": "Exactitud" },
          { "label": "Performance" }
        ],
        "CASES": [
          { "num": "1", "title": "Join Peligroso", "desc": "Calcula devoluciones cruzando con ítems, inflando la métrica.", "challenge_label": "SOLUCIÓN", "challenge": "Asegurar tasa por orden, no por ítem." },
          { "num": "2", "title": "Bucle Mortal", "desc": "Calcula métricas fila a fila con for/apply.", "challenge_label": "SOLUCIÓN", "challenge": "Implementar Vectorización." },
          { "num": "3", "title": "Fechas Rotas", "desc": "Strings mezclados sin normalizar.", "challenge_label": "SOLUCIÓN", "challenge": "Parseo y ordenamiento." },
          { "num": "4", "title": "Cero Excepciones", "desc": "Se cae si falta el archivo diario.", "challenge_label": "SOLUCIÓN", "challenge": "Try/Except y Logging." }
        ]
      }
    },
    {
      "archetype": "roadmap",
      "title": "Plan de Entrega",
      "notes": "Cómo estructurar el repositorio.",
      "slots": {
        "TAG_LEFT": "Entregables",
        "TITLE": "Estructura del Proyecto Final",
        "TAG_RIGHT": "U3",
        "LEAD": "El trabajo requiere código fuente depurado, un informe técnico y tests.",
        "COLS": "4",
        "LANES": [
          { "phase": "Código", "when": "Script", "color": "var(--st-done-bg)", "items": [ { "title": "Funciones modulares" }, { "title": "Docstrings y Try/Except" } ] },
          { "phase": "Pruebas", "when": "Tests", "color": "var(--st-now-bg)", "items": [ { "title": "Unitarias (GMV)" }, { "title": "Regresión (Exactitud)" } ] },
          { "phase": "Informe", "when": "PDF", "color": "var(--st-next-bg)", "items": [ { "title": "Antes vs Después" }, { "title": "Decisiones de Diseño" } ] },
          { "phase": "Data", "when": "Output", "color": "var(--st-later-bg)", "items": [ { "title": "Dataset final limpio" } ] }
        ]
      }
    },
    {
      "archetype": "quote",
      "title": "Conclusión",
      "notes": "Cierre inspiracional sobre ingeniería de datos.",
      "slots": {
        "QUOTE": "Cualquiera puede escribir código que un ordenador entienda. Los buenos programadores escriben código que los humanos pueden mantener y en el que el negocio puede confiar a ciegas.",
        "AUTHOR": "Martin Fowler",
        "ROLE": "Refactoring",
        "CONTEXT_LABEL": "VERDAD",
        "CONTEXT": "El rendimiento importa, pero la exactitud y la mantenibilidad son innegociables."
      }
    },
    {
      "archetype": "resources",
      "title": "Recursos Adicionales",
      "notes": "Cierre con QR",
      "slots": {
        "TAG_LEFT": "Recursos",
        "TITLE": "Material Complementario",
        "TAG_RIGHT": "U3",
        "LIST_TITLE": "Enlaces Útiles",
        "QR_LABEL": "ESCANEAR",
        "QR_DATA": "https%3A%2F%2Fpandas.pydata.org%2Fdocs%2Fuser_guide%2Fenhancingperf.html",
        "QR_ALT": "Pandas Performance",
        "QR_CAPTION": "Pandas Enhancing Perf",
        "NEXT_LABEL": "Siguiente paso",
        "NEXT": "Comenzar el perfilado inicial.",
        "RESOURCES": [
          { "icon": "hwwxhzgs", "title": "Cuaderno Ejercitación", "desc": "Casos prácticos de vectorización.", "url": "EVA IPSS" },
          { "icon": "yyecauzv", "title": "Documentación cProfile", "desc": "Módulo estándar de Python.", "url": "docs.python.org" },
          { "icon": "qgcohzrn", "title": "Pytest Docs", "desc": "Creación de pruebas unitarias.", "url": "pytest.org" }
        ]
      }
    },
    {
      "archetype": "closing",
      "title": "Cierre Final",
      "notes": "Fin de Unidad.",
      "slots": {
        "TAG_LEFT": "Cierre",
        "TITLE": "Fin de la Unidad 3",
        "TAG_RIGHT": "Sincrónica",
        "ICON": "wzpjhhhq",
        "HERO_TITLE": "A Optimizar Motores",
        "HERO_TEXT": "Están listos para tomar código frágil y convertirlo en pipelines de nivel de producción.",
        "LEFT_PANEL_TITLE": "Síntesis",
        "RIGHT_PANEL_TITLE": "Próximos Pasos",
        "NEXT_LABEL": "ACCIÓN",
        "NEXT": "Ejecutar cProfile en el script base.",
        "TAKEAWAYS": [
          { "n": "1", "text": "Mide antes de actuar (Profiling)." },
          { "n": "2", "text": "Abandona el iterrows(); abraza los vectores." },
          { "n": "3", "text": "Asegura la exactitud matemática con asserts." }
        ],
        "NEXT_STEPS": [
          { "n": "1", "text": "Revisar los 5 datasets de eCommerce." },
          { "n": "2", "text": "Identificar el error de JOIN en el GMV." },
          { "n": "3", "text": "Crear el repositorio de proyecto." }
        ]
      }
    }
  ]
}

# Recursively inject repeats into slots
for s in data['slides']:
    if 'repeats' in s:
        s.setdefault('slots', {}).update(s.pop('repeats'))

with open(plan_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
