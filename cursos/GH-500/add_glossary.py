import json

filepath = r'C:\Users\vicen\OneDrive\Escritorio\EVA IPSS\academy-portal\cursos\GH-500\visual_plan.json'

with open(filepath, 'r', encoding='utf-8') as f:
    plan = json.load(f)

glossary_data = [
    [
        ("GHAS", "Término paraguas para Code Security + Secret Protection."),
        ("Code Security", "SKU con code scanning/CodeQL, Autofix, dependency review, campañas, security overview, auto-triage."),
        ("Secret Protection", "SKU con secret scanning, push protection, custom patterns, delegated bypass, campañas de secretos."),
        ("Alerta", "Hallazgo generado por una característica de seguridad, con estado (open/closed) y motivo de cierre."),
        ("Security configuration", "Colección reutilizable de ajustes de habilitación aplicable a repos de una organización.")
    ],
    [
        ("Ruleset", "Regla de gobierno (rama/etiqueta/push) que puede exigir protección de merge por code scanning."),
        ("Delegated bypass", "Flujo de aprobación para saltarse push protection."),
        ("Delegated alert dismissal", "Flujo de aprobación para descartar alertas ('Prevent direct alert dismissals')."),
        ("SARIF", "<i>Static Analysis Results Interchange Format</i>, estándar OASIS JSON para resultados de análisis estático."),
        ("CodeQL", "Motor de análisis semántico de GitHub: trata el código como datos y ejecuta consultas (QL) sobre una base de datos.")
    ],
    [
        ("Query suite", "Conjunto de consultas para CodeQL: <code>default</code>, <code>security-extended</code>, <code>security-and-quality</code>."),
        ("Build mode", "Cómo CodeQL crea la BD en lenguajes compilados: <code>none</code>, <code>autobuild</code>, <code>manual</code>."),
        ("Dependency graph", "Grafo de dependencias directas y transitivas construido desde manifiestos/lockfiles."),
        ("GitHub Advisory Database", "Base de avisos: <code>GHSA-xxxx-xxxx-xxxx</code>; incluye <i>GitHub-reviewed</i>, <i>unreviewed</i> y malware."),
        ("CVE", "Identificador público de vulnerabilidad (<code>CVE-AAAA-NNNN</code>).")
    ],
    [
        ("CWE", "Taxonomía de <i>tipos</i> de debilidad (<code>CWE-89</code> = SQL injection)."),
        ("CVSS", "Sistema de puntuación de severidad (0.0–10.0) → Low/Medium/High/Critical."),
        ("EPSS", "<i>Exploit Prediction Scoring System</i>: probabilidad (%) de explotación en los próximos 30 días."),
        ("SBOM", "<i>Software Bill of Materials</i>; GitHub exporta en formato estandarizado <b>SPDX</b>."),
        ("Security campaign", "Agrupación de alertas para remediación coordinada con desarrolladores, con responsable y plazo.")
    ],
    [
        ("Validity check", "Comprobación con el proveedor externo de si un secreto detectado sigue <b>activo</b> en sus sistemas."),
        ("Push protection", "Bloqueo del push cuando el servidor detecta que contiene un patrón de secreto conocido."),
        ("Auto-triage rules", "Reglas organizacionales que descartan/posponen automáticamente alertas de Dependabot de bajo riesgo."),
        ("PVR", "<i>Private vulnerability reporting</i>. Canal privado para que investigadores reporten vulnerabilidades al mantenedor."),
        ("Artifact attestation", "Declaración firmada criptográficamente sobre la procedencia y origen de un artefacto construido con Actions.")
    ]
]

new_slides = []
for i, page in enumerate(glossary_data):
    rows = []
    for term, definition in page:
        rows.append({"cells": f"<td><strong>{term}</strong></td><td>{definition}</td>"})
        
    slide = {
        "archetype": "table",
        "title": f"Glosario Maestro (Parte {i+1})",
        "notes": f"Revisión de términos clave del glosario maestro, parte {i+1} de {len(glossary_data)}.",
        "slots": {
            "TAG_LEFT": "ANEXO",
            "TITLE": "Glosario Maestro de Términos",
            "TAG_RIGHT": f"{i+1}/{len(glossary_data)}",
            "LEAD": "Términos, acrónimos y definiciones operativas clave para aprobar la certificación GH-500.",
            "HEADERS": "<th style='width: 30%'>Término</th><th>Definición Operativa</th>",
            "NOTE_LABEL": "Tip de examen:",
            "NOTE": "Diferenciar entre <b>Code Security</b> y <b>Secret Protection</b> es vital para preguntas de licenciamiento.",
            "ROWS": rows
        }
    }
    new_slides.append(slide)

plan['slides'] = [s for s in plan['slides'] if not s.get('title', '').startswith('Glosario Maestro')]

last_slide = plan['slides'].pop()
plan['slides'].extend(new_slides)
plan['slides'].append(last_slide)

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(plan, f, indent=2, ensure_ascii=False)
