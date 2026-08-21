import json
import os

unit_path = r"C:\Users\vicen\OneDrive\Escritorio\EVA IPSS\academy-portal\cursos\PROGRAMACIÓN PARA LA CIENCIA DE DATOS\UNIDAD 2"
os.makedirs(unit_path, exist_ok=True)
plan_path = os.path.join(unit_path, "visual_plan.json")

data = {
  "pack": "fresh_green",
  "title": "Unidad 2 — Procesamiento y Transformación de Datos",
  "slides": [
    {
      "archetype": "cover",
      "title": "Unidad 2",
      "notes": "Bienvenidos a la Unidad 2. Pasaremos de los fundamentos básicos a la construcción de pipelines reales de limpieza y transformación.",
      "slots": {
        "EYEBROW": "UNIDAD 2",
        "TITLE": "Procesamiento y<br>Transformación",
        "SUBTITLE": "Programación para la Ciencia de Datos",
        "BG_IMAGE": "",
        "CHIPS": [
          { "label": "22 Horas", "accent": "var(--a1)" },
          { "label": "20% Ponderación", "accent": "var(--a2)" }
        ]
      }
    },
    {
      "archetype": "toc",
      "title": "Mapa de la Sesión",
      "notes": "Nuestra hoja de ruta incluye desde el diseño algorítmico hasta el cruce de bases de datos heterogéneas.",
      "slots": {
        "TAG_LEFT": "Unidad 2",
        "TITLE": "Mapa de la Sesión",
        "TAG_RIGHT": "Sincrónica",
        "ROWS": "2",
        "COLS": "3",
        "ITEMS": [
          { "num": "01", "icon": "qhsqomla", "title": "Repaso U1", "desc": "De scripts a pipelines.", "chips": "" },
          { "num": "02", "icon": "yyecauzv", "title": "Diseño", "desc": "Algoritmos y lógica.", "chips": "" },
          { "num": "03", "icon": "wzpjhhhq", "title": "Limpieza", "desc": "Faltantes y Outliers.", "chips": "" },
          { "num": "04", "icon": "qgcohzrn", "title": "Transformación", "desc": "Normalización y Fechas.", "chips": "" },
          { "num": "05", "icon": "gqdyesfu", "title": "Integración", "desc": "Merge y GroupBy.", "chips": "" },
          { "num": "06", "icon": "dxjqoygy", "title": "Caso Práctico", "desc": "Educación en Chile.", "chips": "" }
        ]
      }
    },
    {
      "archetype": "section",
      "title": "Bloque 1: Conectando con la Unidad 1",
      "notes": "En la U1 vimos las piezas del lego. Ahora construiremos la nave espacial completa.",
      "slots": {
        "PART_LABEL": "Bloque 1",
        "TITLE": "De Scripts a Pipelines",
        "SUBTITLE": "Evolución de nuestras habilidades.",
        "AGENDA": [
          { "label": "1.1", "text": "Competencia Global" },
          { "label": "1.2", "text": "El Salto de Complejidad" }
        ]
      }
    },
    {
      "archetype": "quote",
      "title": "Competencia de Unidad 2",
      "notes": "El objetivo es claro: crear pipelines automatizados.",
      "slots": {
        "QUOTE": "Programar algoritmos robustos para el procesamiento y transformación de datos, desde la limpieza profunda hasta la consolidación final.",
        "AUTHOR": "Competencia U2",
        "ROLE": "Nivel de Dominio: Avanzado",
        "CONTEXT_LABEL": "OBJETIVO",
        "CONTEXT": "Generar datos listos para modelos predictivos o analítica avanzada."
      }
    },
    {
      "archetype": "comparison",
      "title": "El Salto Cualitativo",
      "notes": "Diferencia entre un script de U1 y un pipeline de U2.",
      "slots": {
        "TAG_LEFT": "Evolución",
        "TITLE": "Unidad 1 vs Unidad 2",
        "TAG_RIGHT": "U2",
        "VS_LABEL": "Evolución",
        "LEFT_LABEL": "Unidad 1",
        "LEFT_TITLE": "Scripts Básicos",
        "LEFT_BODY": "Operaciones lineales sobre un único archivo limpio.",
        "LEFT_EXAMPLE": "df = pd.read_csv('datos.csv')",
        "RIGHT_LABEL": "Unidad 2",
        "RIGHT_TITLE": "Pipelines Robustos",
        "RIGHT_BODY": "Arquitectura modular, validación y cruce de múltiples fuentes sucias.",
        "RIGHT_EXAMPLE": "def ejecutar_pipeline(rutas):",
        "LEFT_POINTS": [
          { "text": "Datos aislados (1 CSV)." },
          { "text": "Limpieza manual." }
        ],
        "RIGHT_POINTS": [
          { "text": "Múltiples formatos (JSON, CSV)." },
          { "text": "Funciones automatizadas." }
        ],
        "RIGHT_TAGS": [
          { "text": "Escalable" },
          { "text": "Modular" }
        ]
      }
    },
    {
      "archetype": "section",
      "title": "Bloque 2: Diseño de Algoritmos",
      "notes": "Antes de picar código, hay que pensar.",
      "slots": {
        "PART_LABEL": "Bloque 2",
        "TITLE": "Diseño de Algoritmos",
        "SUBTITLE": "Estructurando la lógica antes de programar.",
        "AGENDA": [
          { "label": "2.1", "text": "Pseudocódigo" },
          { "label": "2.2", "text": "Flujo de Datos" }
        ]
      }
    },
    {
      "archetype": "diagram",
      "title": "Arquitectura de un Pipeline",
      "notes": "El ciclo típico de un proceso ETL básico.",
      "slots": {
        "TAG_LEFT": "Arquitectura",
        "TITLE": "Flujo de Trabajo Estándar",
        "TAG_RIGHT": "U2",
        "SPLIT": "1fr 1fr",
        "DIAGRAM": "flowchart TD\n    A[Datos Brutos] --> B[Preprocesamiento]\n    B --> C[Transformación]\n    C --> D[Integración]\n    D --> E[Dataset Consolidado]",
        "SIDE_TITLE": "Etapas del Proceso",
        "LEAD": "Divide y vencerás. Cada etapa es una función independiente.",
        "NOTE_LABEL": "REGLA DE ORO",
        "NOTE": "Nunca sobreescribir los datos originales. El pipeline debe ser reproducible.",
        "STEPS": [
          { "n": "1", "name": "Lectura", "text": "Carga de CSV/JSON tolerando fallos." },
          { "n": "2", "name": "Limpieza", "text": "Nulos, duplicados y outliers." },
          { "n": "3", "name": "Transformación", "text": "Casteo, normalización, encoding." },
          { "n": "4", "name": "Consolidación", "text": "Joins y agregaciones finales." }
        ]
      }
    },
    {
      "archetype": "section",
      "title": "Bloque 3: Preprocesamiento de Datos",
      "notes": "Entrando a la limpieza profunda.",
      "slots": {
        "PART_LABEL": "Bloque 3",
        "TITLE": "Preprocesamiento (Limpieza)",
        "SUBTITLE": "Domando el caos del mundo real.",
        "AGENDA": [
          { "label": "3.1", "text": "Valores Faltantes" },
          { "label": "3.2", "text": "Valores Atípicos (Outliers)" },
          { "label": "3.3", "text": "Duplicados" }
        ]
      }
    },
    {
      "archetype": "concept-cards",
      "title": "Anomalías Comunes",
      "notes": "Los tres jinetes de los datos sucios.",
      "slots": {
        "TAG_LEFT": "Calidad",
        "TITLE": "Enemigos de la Calidad de Datos",
        "TAG_RIGHT": "U2",
        "COLS": "3",
        "CARDS": [
          { "badge": "NaN", "title": "Faltantes", "body": "Campos vacíos por fallos de sistema o humanos. Requieren imputación o eliminación.", "note_label": "ACCIÓN", "note": "fillna() / dropna()" },
          { "badge": "Atípicos", "title": "Outliers", "body": "Valores extremos (ej. edad=999). Distorsionan promedios y modelos predictivos.", "note_label": "ACCIÓN", "note": "Filtros IQR / Z-Score" },
          { "badge": "Clones", "title": "Duplicados", "body": "Registros ingresados dos veces. Generan sobre-representación estadística.", "note_label": "ACCIÓN", "note": "drop_duplicates()" }
        ]
      }
    },
    {
      "archetype": "dodont",
      "title": "Manejo de Valores Faltantes",
      "notes": "No siempre es buena idea borrar todo.",
      "slots": {
        "TAG_LEFT": "Estrategias",
        "TITLE": "Eliminación vs Imputación",
        "TAG_RIGHT": "U2",
        "BAD_TITLE": "Eliminación Ciega",
        "BAD_SNIPPET": "<span class=\"c-cm\"># Borra la fila si falta ALGO</span>\n<span class=\"c-kw\">df_limpio</span> = df.<span class=\"c-fn\">dropna</span>()",
        "GOOD_TITLE": "Imputación Inteligente",
        "GOOD_SNIPPET": "<span class=\"c-kw\">mediana</span> = df[<span class=\"c-str\">'ingreso'</span>].<span class=\"c-fn\">median</span>()\ndf[<span class=\"c-str\">'ingreso'</span>].<span class=\"c-fn\">fillna</span>(mediana)",
        "WHY_LABEL": "IMPACTO",
        "WHY": "Eliminar reduce drásticamente tu muestra. Si falta el 5-15% de los datos, imputar con media/mediana suele preservar el valor estadístico del resto de la fila.",
        "BAD_POINTS": [
          { "text": "Pérdida masiva de datos." },
          { "text": "Sesga la muestra si el fallo no es aleatorio." }
        ],
        "GOOD_POINTS": [
          { "text": "Preserva registros valiosos." },
          { "text": "Mantiene la representatividad." }
        ]
      }
    },
    {
      "archetype": "code-criteria",
      "title": "Detección de Outliers",
      "notes": "Cómo encontrar valores atípicos de forma programática.",
      "slots": {
        "TAG_LEFT": "Outliers",
        "TITLE": "Encontrando lo Atípico",
        "TAG_RIGHT": "U2",
        "KICKER": "ESTADÍSTICA",
        "CODE_TITLE": "Filtro por Rango Intercuartílico (IQR)",
        "CODE": "<span class=\"c-kw\">def</span> <span class=\"c-fn\">limpiar_outliers</span>(df, col):\n    Q1 = df[col].<span class=\"c-fn\">quantile</span>(<span class=\"c-num\">0.25</span>)\n    Q3 = df[col].<span class=\"c-fn\">quantile</span>(<span class=\"c-num\">0.75</span>)\n    IQR = Q3 - Q1\n    <span class=\"c-kw\">lim_inf</span> = Q1 - <span class=\"c-num\">1.5</span> * IQR\n    <span class=\"c-kw\">lim_sup</span> = Q3 + <span class=\"c-num\">1.5</span> * IQR\n    <span class=\"c-kw\">return</span> df[(df[col] >= lim_inf) & (df[col] <= lim_sup)]",
        "PANEL_TITLE": "Mecánica del IQR",
        "WHY_TITLE": "Robustez",
        "WHY": "A diferencia de la media, los cuartiles no se dejan arrastrar por valores extremos extremos, haciendo al IQR muy confiable.",
        "CRITERIA": [
          { "letter": "Q", "name": "Cuartiles", "meta": "Cortes al 25% y 75%.", "highlight": "" },
          { "letter": "I", "name": "Rango", "meta": "La distancia entre ambos (Caja).", "highlight": "" },
          { "letter": "B", "name": "Bigotes", "meta": "Tolerancia de 1.5 veces el rango.", "highlight": "hi" }
        ]
      }
    },
    {
      "archetype": "section",
      "title": "Bloque 4: Transformación y Enriquecimiento",
      "notes": "Cambiando la forma y el significado de los datos.",
      "slots": {
        "PART_LABEL": "Bloque 4",
        "TITLE": "Transformación (Enriquecimiento)",
        "SUBTITLE": "Fechas, Normalización y Encoding.",
        "AGENDA": [
          { "label": "4.1", "text": "Formatos y Fechas" },
          { "label": "4.2", "text": "Normalización Numérica" },
          { "label": "4.3", "text": "Variables Derivadas" }
        ]
      }
    },
    {
      "archetype": "feature-matrix",
      "title": "Técnicas de Transformación",
      "notes": "Un resumen de por qué transformamos la data.",
      "slots": {
        "TAG_LEFT": "Transformación",
        "TITLE": "Adecuando los Datos",
        "TAG_RIGHT": "U2",
        "LEAD": "El formato original casi nunca es el óptimo para análisis o ML.",
        "HEADERS": "<th>Técnica</th><th>Propósito</th><th>Ejemplo Pandas</th>",
        "NOTE_LABEL": "REGLA",
        "NOTE": "Las transformaciones deben documentarse rigurosamente para asegurar reproducibilidad.",
        "ROWS": [
          { "cells": "<td><b>Normalización Min-Max</b></td><td>Nivelar escalas dispares (ej. edad vs presupuesto)</td><td><span class=\"c-fn\">MinMaxScaler()</span></td>" },
          { "cells": "<td><b>Parseo de Fechas</b></td><td>Habilitar series temporales matemáticas</td><td><span class=\"c-fn\">pd.to_datetime()</span></td>" },
          { "cells": "<td><b>Categorical Encoding</b></td><td>Convertir texto a número para modelos</td><td><span class=\"c-fn\">pd.get_dummies()</span></td>" },
          { "cells": "<td><b>Variable Derivada</b></td><td>Crear KPIs lógicos (Población / Superficie)</td><td><span class=\"c-kw\">df['densidad'] = ...</span></td>" }
        ]
      }
    },
    {
      "archetype": "code",
      "title": "Parseo de Fechas",
      "notes": "Las fechas como texto son inútiles.",
      "slots": {
        "TAG_LEFT": "Fechas",
        "TITLE": "Estandarización Temporal",
        "TAG_RIGHT": "U2",
        "SPLIT": "1fr 1fr",
        "LEAD": "Las fechas vienen en cientos de formatos (DD-MM-YYYY, YYYY/MM/DD). Pandas las unifica.",
        "CALLOUT_LABEL": "VENTAJA",
        "CALLOUT": "Una vez parseadas, puedes extraer fácilmente el mes, el año o el día de la semana (.dt.month).",
        "FILENAME": "fechas.py",
        "CODE": "<span class=\"c-cm\"># Convertir string mixto a Datetime</span>\n<span class=\"c-kw\">def</span> <span class=\"c-fn\">parsear_fechas</span>(df, col):\n    df[col] = pd.<span class=\"c-fn\">to_datetime</span>(\n        df[col],\n        <span class=\"c-kw\">format</span>=<span class=\"c-str\">'mixed'</span>, \n        <span class=\"c-kw\">dayfirst</span>=<span class=\"c-num\">True</span>\n    )\n    <span class=\"c-kw\">return</span> df",
        "STEPS": [
          { "n": "1", "text": "format='mixed' infiere automáticamente múltiples estructuras." },
          { "n": "2", "text": "dayfirst=True avisa que 02/01 es Enero 2, no Febrero 1." }
        ]
      }
    },
    {
      "archetype": "quiz",
      "title": "Verificación: Normalización",
      "notes": "¿Por qué es importante escalar?",
      "slots": {
        "TAG_LEFT": "Verificación",
        "TITLE": "¿Por qué Normalizamos?",
        "TAG_RIGHT": "U2",
        "BADGE": "Pregunta",
        "QUESTION": "Si tienes 'Edad' (0-100) y 'Presupuesto' (0-1B), ¿Por qué debes normalizarlas antes de un análisis conjunto?",
        "COLS": "1",
        "EXPLANATION_LABEL": "Respuesta",
        "EXPLANATION": "Si no se escala, la magnitud masiva del Presupuesto eclipsará matemáticamente el impacto de la Edad.",
        "OPTIONS": [
          { "key": "A", "text": "Para evitar que variables con valores altos dominen el peso estadístico.", "correct": "ok" },
          { "key": "B", "text": "Para reducir el uso de memoria RAM del DataFrame.", "correct": "" },
          { "key": "C", "text": "Para eliminar los valores nulos (NaN) automáticamente.", "correct": "" }
        ]
      }
    },
    {
      "archetype": "section",
      "title": "Bloque 5: Agregación y Combinación",
      "notes": "Uniendo las piezas dispersas.",
      "slots": {
        "PART_LABEL": "Bloque 5",
        "TITLE": "Agregación y Consolidación",
        "SUBTITLE": "GroupBy y Merge.",
        "AGENDA": [
          { "label": "5.1", "text": "Agregaciones (GroupBy)" },
          { "label": "5.2", "text": "Uniones (Merge/Join)" },
          { "label": "5.3", "text": "Validación" }
        ]
      }
    },
    {
      "archetype": "anatomy",
      "title": "El patrón Split-Apply-Combine",
      "notes": "La filosofía detrás de groupby.",
      "slots": {
        "TAG_LEFT": "Agregación",
        "TITLE": "Mecánica de GroupBy",
        "TAG_RIGHT": "U2",
        "SPEC_TITLE": "df.groupby('region')['matricula'].sum()",
        "FIELDS": [
          { "key": "df", "value": "Dataset original", "highlight": "" },
          { "key": "groupby('region')", "value": "SPLIT: Separa la tabla en trozos por cada región única", "highlight": "hi" },
          { "key": "['matricula']", "value": "Filtra la columna que nos interesa operar", "highlight": "" },
          { "key": ".sum()", "value": "APPLY: Ejecuta la suma en cada trozo. COMBINE: Une los resultados en un resumen", "highlight": "hi" }
        ],
        "NOTES": [
          { "n": "1", "title": "Versatilidad", "text": "Soporta mean(), count(), max(), etc." },
          { "n": "2", "title": ".agg()", "text": "Permite aplicar múltiples funciones a la vez." }
        ]
      }
    },
    {
      "archetype": "bento",
      "title": "Combinación de Datasets",
      "notes": "Cómo actúan los joins.",
      "slots": {
        "TAG_LEFT": "Relacional",
        "TITLE": "Estrategias de Unión (Merge)",
        "TAG_RIGHT": "U2",
        "TILES": [
          { "variant": "solid", "col": "1 / 4", "row": "1 / 4", "icon": "qhsqomla", "tag": "INTERSECCIÓN", "stat": "", "unit": "", "title": "Inner Join", "body": "Solo retiene filas donde la clave existe en AMBOS datasets. Evita nulos, pero pierde datos.", "foot": "" },
          { "variant": "outline", "col": "4 / 7", "row": "1 / 7", "icon": "yyecauzv", "tag": "CÓDIGO", "stat": "", "unit": "", "title": "pd.merge()", "body": "pd.merge(df1, df2, on='codigo_region', how='left')", "foot": "Las claves deben llamarse igual o usar left_on y right_on." },
          { "variant": "card", "col": "1 / 4", "row": "4 / 7", "icon": "wzpjhhhq", "tag": "PRIORIDAD", "stat": "", "unit": "", "title": "Left Join", "body": "Conserva TODO el dataset izquierdo. Si no hay match en el derecho, rellena con NaN.", "foot": "" }
        ]
      }
    },
    {
      "archetype": "section",
      "title": "Bloque 6: Caso Práctico",
      "notes": "El caso central: Mineduc e INE.",
      "slots": {
        "PART_LABEL": "Bloque 6",
        "TITLE": "Caso Práctico",
        "SUBTITLE": "Sistema Educacional y Factores Socioeconómicos.",
        "AGENDA": [
          { "label": "6.1", "text": "Los Tres Datasets" },
          { "label": "6.2", "text": "Arquitectura del Pipeline" },
          { "label": "6.3", "text": "Validaciones" }
        ]
      }
    },
    {
      "archetype": "anatomy",
      "title": "El Problema Educacional",
      "notes": "Contexto de la evaluación de U2.",
      "slots": {
        "TAG_LEFT": "El Caso",
        "TITLE": "Mineduc + INE",
        "TAG_RIGHT": "U2",
        "SPEC_TITLE": "Misión del Futuro Científico de Datos",
        "FIELDS": [
          { "key": "Organismos", "value": "Ministerio de Educación e Instituto Nacional de Estadísticas", "highlight": "" },
          { "key": "Problema", "value": "Archivos fragmentados, formatos sucios e incompatibles", "highlight": "hi" },
          { "key": "Insumos", "value": "Rendimiento (CSV), Indicadores (JSON), Infraestructura (CSV)", "highlight": "" },
          { "key": "Objetivo", "value": "Diseñar un pipeline que consolide un único Dataset Maestro", "highlight": "hi" }
        ],
        "NOTES": [
          { "n": "1", "title": "Requisito", "text": "Código modular, basado en funciones." },
          { "n": "2", "title": "Entrega", "text": "Script Python (.py / .ipynb), CSV limpio e Informe de Proceso." }
        ]
      }
    },
    {
      "archetype": "table",
      "title": "Los Tres Datasets Originales",
      "notes": "Qué incluye cada archivo fuente.",
      "slots": {
        "TAG_LEFT": "Fuentes",
        "TITLE": "Fragmentación de la Información",
        "TAG_RIGHT": "U2",
        "LEAD": "Para consolidar, debes unir usando el 'codigo_region'.",
        "HEADERS": "<th>Fuente</th><th>Formato</th><th>Contenido Clave</th><th>Desafíos</th>",
        "NOTE_LABEL": "DATO",
        "NOTE": "El uso de JSON requiere métodos específicos de pandas (read_json).",
        "ROWS": [
          { "cells": "<td><b>rendimiento_escolar</b></td><td>CSV</td><td>SIMCE, matrícula, fecha</td><td>Fechas mixtas, outliers en SIMCE, mayúsculas locas.</td>" },
          { "cells": "<td><b>indicadores_regionales</b></td><td>JSON</td><td>Ingreso, población, vulnerabilidad</td><td>Nulos en ingreso, disparidad en nombres de región.</td>" },
          { "cells": "<td><b>infraestructura</b></td><td>CSV</td><td>Presupuesto, n° colegios</td><td>Presupuestos en escalas irreales (miles vs millones).</td>" }
        ]
      }
    },
    {
      "archetype": "roadmap",
      "title": "Hoja de Ruta del Estudiante",
      "notes": "Pasos recomendados para la evaluación.",
      "slots": {
        "TAG_LEFT": "Metodología",
        "TITLE": "Cómo Atacar el Proyecto",
        "TAG_RIGHT": "U2",
        "LEAD": "Sigue este orden estructurado para no perderte en el código.",
        "COLS": "4",
        "LANES": [
          { "phase": "Diseño", "when": "Paso 1", "color": "var(--st-now-bg)", "items": [ { "title": "Diagramar flujo" }, { "title": "Identificar nulos" } ] },
          { "phase": "Modularizar", "when": "Paso 2", "color": "var(--st-next-bg)", "items": [ { "title": "Crear func. limpiar" }, { "title": "Crear func. transformar" } ] },
          { "phase": "Unir (Merge)", "when": "Paso 3", "color": "var(--st-later-bg)", "items": [ { "title": "Homologar llaves" }, { "title": "pd.merge() x2" } ] },
          { "phase": "Validar", "when": "Paso 4", "color": "var(--st-done-bg)", "items": [ { "title": "Comprobar asserts" }, { "title": "Generar CSV final" } ] }
        ]
      }
    },
    {
      "archetype": "code-criteria",
      "title": "Validación Rigurosa",
      "notes": "Cómo asegurar que el pipeline funcionó.",
      "slots": {
        "TAG_LEFT": "Validación",
        "TITLE": "Pruebas de Consistencia",
        "TAG_RIGHT": "U2",
        "KICKER": "CALIDAD",
        "CODE_TITLE": "Verificando el Merge",
        "CODE": "<span class=\"c-cm\"># ¿Se perdieron filas al unir?</span>\n<span class=\"c-kw\">def</span> <span class=\"c-fn\">validar_totales</span>(df_inicial, df_final):\n    <span class=\"c-kw\">try</span>:\n        <span class=\"c-kw\">assert</span> <span class=\"c-fn\">len</span>(df_inicial) == <span class=\"c-fn\">len</span>(df_final)\n        <span class=\"c-fn\">print</span>(<span class=\"c-str\">\"Validación OK: Filas intactas.\"</span>)\n    <span class=\"c-kw\">except</span> <span class=\"c-kw\">AssertionError</span>:\n        <span class=\"c-fn\">print</span>(<span class=\"c-str\">\"Error: Pérdida de registros durante el Merge.\"</span>)",
        "PANEL_TITLE": "Manejo de Errores",
        "WHY_TITLE": "Confianza",
        "WHY": "Un pipeline ciego es peligroso. Los asserts garantizan que la automatización no destruya silenciosamente tus datos vitales.",
        "CRITERIA": [
          { "letter": "A", "name": "Assert", "meta": "Falla ruidosamente si es False.", "highlight": "hi" },
          { "letter": "T", "name": "Try/Except", "meta": "Atrapa caídas críticas del sistema.", "highlight": "" },
          { "letter": "L", "name": "Logs", "meta": "Prints para auditar el proceso.", "highlight": "" }
        ]
      }
    },
    {
      "archetype": "quote",
      "title": "Resultado y Toma de Decisiones",
      "notes": "La importancia del dataset consolidado.",
      "slots": {
        "QUOTE": "Un pipeline bien diseñado convierte tres archivos incompatibles e inservibles en una única fuente de verdad para dictar política pública.",
        "AUTHOR": "El Valor de los Datos",
        "ROLE": "Visión Estratégica",
        "CONTEXT_LABEL": "CONCLUSIÓN",
        "CONTEXT": "La calidad del análisis depende íntegramente de la calidad del preprocesamiento."
      }
    },
    {
      "archetype": "resources",
      "title": "Recursos U2",
      "notes": "Cierre con lecturas y material anexo de la plataforma.",
      "slots": {
        "TAG_LEFT": "Bibliografía",
        "TITLE": "Material Complementario",
        "TAG_RIGHT": "U2",
        "LIST_TITLE": "Lecturas y Enlaces",
        "QR_LABEL": "ESCANEAR",
        "QR_DATA": "https%3A%2F%2Fpandas.pydata.org%2Fdocs%2Freference%2Fapi%2Fpandas.DataFrame.merge.html",
        "QR_ALT": "QR Merge Pandas",
        "QR_CAPTION": "Doc. pd.merge()",
        "NEXT_LABEL": "Siguiente paso",
        "NEXT": "Desarrollar la Evaluación U2.",
        "RESOURCES": [
          { "icon": "hwwxhzgs", "title": "Cuaderno de Ejercitación", "desc": "Prácticas de imputación y merge.", "url": "EVA IPSS" },
          { "icon": "yyecauzv", "title": "Documentación Merge", "desc": "Cruces de datos en Pandas.", "url": "pandas.pydata.org" },
          { "icon": "qgcohzrn", "title": "Detección de Outliers", "desc": "Técnicas estadísticas.", "url": "haciaelcódigo.com" }
        ]
      }
    },
    {
      "archetype": "closing",
      "title": "Cierre",
      "notes": "Despedida.",
      "slots": {
        "TAG_LEFT": "Cierre",
        "TITLE": "Fin de la Unidad 2",
        "TAG_RIGHT": "Sincrónica",
        "ICON": "wzpjhhhq",
        "HERO_TITLE": "¡A Construir el Pipeline!",
        "HERO_TEXT": "Ya tienen la teoría y la estructura. Es hora de crear funciones robustas.",
        "LEFT_PANEL_TITLE": "Síntesis",
        "RIGHT_PANEL_TITLE": "Próximos Pasos",
        "NEXT_LABEL": "ACCIÓN",
        "NEXT": "Comenzar el diseño del algoritmo.",
        "TAKEAWAYS": [
          { "n": "1", "text": "El preprocesamiento es el 80% del trabajo." },
          { "n": "2", "text": "Modularizar la lógica evita dolores de cabeza." },
          { "n": "3", "text": "Siempre auditar (asserts) tras cada cruce." }
        ],
        "NEXT_STEPS": [
          { "n": "1", "text": "Crear diagrama de flujo del pipeline." },
          { "n": "2", "text": "Escribir funciones base de limpieza." },
          { "n": "3", "text": "Generar informe y ZIP final." }
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
