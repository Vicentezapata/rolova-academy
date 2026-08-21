import json

plan = {
    "pack": "noir_film",
    "title": "GH-500 — GitHub Advanced Security",
    "slides": [
        {
            "archetype": "cover",
            "title": "GH-500: GitHub Advanced Security",
            "notes": "Bienvenidos a la guía integral de estudio para la certificación GH-500. Esta presentación abarca los seis dominios del examen, cubriendo la prevención, detección y remediación de vulnerabilidades en el ecosistema GitHub.",
            "slots": {
                "EYEBROW": "Examen GH-500 (Actualizado)",
                "TITLE": "GitHub Advanced Security",
                "SUBTITLE": "Guía Integral de Estudio y Operaciones de Seguridad",
                "CHIPS": [
                    {"label": "Code Security", "accent": "var(--a1)"},
                    {"label": "Secret Protection", "accent": "var(--a2)"},
                    {"label": "Supply Chain", "accent": "var(--ok)"}
                ]
            }
        },
        {
            "archetype": "toc",
            "title": "Mapa de Sesiones",
            "notes": "La agenda cubre los 6 dominios del examen con especial atención en las características, administración y mejores prácticas de seguridad.",
            "slots": {
                "TAG_LEFT": "Índice",
                "TITLE": "Mapa de la Sesión",
                "TAG_RIGHT": "01",
                "ROWS": "2",
                "COLS": "3",
                "ITEMS": [
                    {"num": "1", "icon": "1", "title": "Ecosistema GHAS", "desc": "Suites y características", "chips": ""},
                    {"num": "2", "icon": "2", "title": "Secret Protection", "desc": "Escaneo e interceptación", "chips": ""},
                    {"num": "3", "icon": "3", "title": "Supply Chain", "desc": "Dependabot & Reviews", "chips": ""},
                    {"num": "4", "icon": "4", "title": "Code Security", "desc": "CodeQL y SARIF", "chips": ""},
                    {"num": "5", "icon": "5", "title": "Operaciones", "desc": "Priorización y campañas", "chips": ""},
                    {"num": "6", "icon": "6", "title": "Administración", "desc": "Policies & Enforcement", "chips": ""}
                ]
            }
        },
        {
            "archetype": "section",
            "title": "Dominio 1",
            "notes": "Comenzamos con el Dominio 1, que representa el 15-20% del examen. Aquí entenderemos las suites de seguridad, el ciclo de vida seguro y la diferencia vital entre Code Security y Secret Protection.",
            "slots": {
                "PART_LABEL": "DOMINIO 1",
                "TITLE": "Suites de Seguridad y Ecosistema",
                "SUBTITLE": "Comprendiendo el mapa completo (15-20%)",
                "AGENDA": [
                    {"label": "1.1", "text": "Los tres pilares de GHAS"},
                    {"label": "1.2", "text": "Disponibilidad y Licencias"},
                    {"label": "1.3", "text": "Security Overview y SSDLC"}
                ]
            }
        },
        {
            "archetype": "bento",
            "title": "Los tres pilares",
            "notes": "Para aprobar el examen, es crucial entender que GHAS ya no es un solo producto, sino un paraguas para Code Security y Secret Protection, sumado a las características de Supply Chain incluidas en todos los planes.",
            "slots": {
                "TAG_LEFT": "DOMINIO 1",
                "TITLE": "Los tres pilares de seguridad",
                "TAG_RIGHT": "PILARES",
                "TILES": [
                    {
                        "variant": "card-dark",
                        "col": "1 / 4",
                        "row": "1 / 3",
                        "icon": "🛡️",
                        "tag": "LICENCIA",
                        "stat": "Code",
                        "unit": "Security",
                        "title": "¿Mi propio código tiene vulnerabilidades?",
                        "body": "Incluye CodeQL, SARIF, Copilot Autofix, Dependency Review.",
                        "foot": "Enfocado en vulnerabilidades lógicas"
                    },
                    {
                        "variant": "card-accent",
                        "col": "4 / 7",
                        "row": "1 / 3",
                        "icon": "🔑",
                        "tag": "LICENCIA",
                        "stat": "Secret",
                        "unit": "Protection",
                        "title": "¿He filtrado credenciales?",
                        "body": "Secret scanning, Push protection, validity checks, custom patterns.",
                        "foot": "Enfocado en datos sensibles"
                    },
                    {
                        "variant": "card-light",
                        "col": "1 / 7",
                        "row": "3 / 5",
                        "icon": "📦",
                        "tag": "GRATUITO",
                        "stat": "Supply",
                        "unit": "Chain",
                        "title": "¿Mis dependencias son seguras?",
                        "body": "Dependency graph, Dependabot alerts/updates, GH Advisory Database.",
                        "foot": "Enfocado en el código ajeno"
                    }
                ]
            }
        },
        {
            "archetype": "feature-matrix",
            "title": "Disponibilidad",
            "notes": "Entender esta matriz es clave. Lo más importante: Dependency graph NO se puede desactivar en repos públicos. Secret scanning y Code scanning son gratis en repos públicos. Security overview y Push protection para repos siempre requieren licencia (excepto public monitoring).",
            "slots": {
                "TAG_LEFT": "DOMINIO 1",
                "TITLE": "Disponibilidad por Tipo de Repo",
                "TAG_RIGHT": "MATRIZ",
                "LEAD": "Qué características requieren licencia y cuáles son gratuitas.",
                "HEADERS": "<th>Característica</th><th>Público (Gratis)</th><th>Privado (Gratis)</th><th>Code Sec.</th><th>Secret Prot.</th>",
                "NOTE_LABEL": "Trampa clásica",
                "NOTE": "Dependabot alerts NO está activo por defecto en públicos, aunque el dependency graph sí lo esté.",
                "ROWS": [
                    {"cells": "<td>Dependency graph</td><td><span class=\"mk yes\">Siempre</span></td><td><span class=\"mk no\">No (por def.)</span></td><td><span class=\"mk yes\">Sí</span></td><td><span class=\"mk no\">—</span></td>"},
                    {"cells": "<td>Code Scanning (CodeQL)</td><td><span class=\"mk yes\">Sí</span></td><td><span class=\"mk no\">No</span></td><td><span class=\"mk yes\">Sí</span></td><td><span class=\"mk no\">—</span></td>"},
                    {"cells": "<td>Secret Scanning</td><td><span class=\"mk yes\">Sí</span></td><td><span class=\"mk no\">No</span></td><td><span class=\"mk no\">—</span></td><td><span class=\"mk yes\">Sí</span></td>"},
                    {"cells": "<td>Security Overview</td><td><span class=\"mk no\">No</span></td><td><span class=\"mk no\">No</span></td><td><span class=\"mk yes\">Sí</span></td><td><span class=\"mk yes\">Sí</span></td>"}
                ]
            }
        },
        {
            "archetype": "concept-cards",
            "title": "Estrategias de Seguridad",
            "notes": "En GHAS operamos con estrategias de seguridad defensiva. Push protection es el mejor ejemplo de prevention-first porque el secreto nunca llega al historial de Git.",
            "slots": {
                "TAG_LEFT": "DOMINIO 1",
                "TITLE": "Estrategias en el SSDLC",
                "TAG_RIGHT": "ESTRATEGIA",
                "COLS": "3",
                "CARDS": [
                    {
                        "badge": "Shift-left",
                        "title": "Prevention-first",
                        "body": "Impedir que el problema entre. Ej: Push protection, Copilot Autofix en IDE.",
                        "note_label": "Ventaja",
                        "note": "Coste de corrección mínimo."
                    },
                    {
                        "badge": "Control",
                        "title": "Gate-based (Puertas)",
                        "body": "Detectar y bloquear en un punto de control. Ej: Dependency review con fail-on-severity.",
                        "note_label": "Riesgo",
                        "note": "Puede bloquear entregas."
                    },
                    {
                        "badge": "Reactiva",
                        "title": "Detect & Remediate",
                        "body": "Encontrar lo ya introducido. Ej: Escaneos programados, Security Campaigns.",
                        "note_label": "Cuidado",
                        "note": "Existe ventana de exposición."
                    }
                ]
            }
        },
        {
            "archetype": "quiz",
            "title": "Quiz - Dominio 1",
            "notes": "Validación rápida. Recuerda que la respuesta correcta muestra por qué el Dashboard no es válido para compliance: porque los datos mutan (ej. si borras un repo o cambia un CVE).",
            "slots": {
                "TAG_LEFT": "REPASO",
                "TITLE": "Knowledge Check: Dominio 1",
                "TAG_RIGHT": "Q1",
                "BADGE": "Pregunta de Examen",
                "QUESTION": "¿Por qué el dashboard de Security Overview NO sirve como evidencia de auditoría estricta?",
                "COLS": "2",
                "EXPLANATION_LABEL": "Respuesta correcta",
                "EXPLANATION": "Para evidencias inmutables de cumplimiento normativo SIEMPRE debes usar el Audit Log.",
                "OPTIONS": [
                    {"key": "A", "text": "Porque solo Enterprise Owners pueden verlo.", "correct": "false"},
                    {"key": "B", "text": "Porque no incluye datos de Secret Protection.", "correct": "false"},
                    {"key": "C", "text": "Porque las métricas históricas pueden cambiar si se borran repos o cambian los Advisories.", "correct": "true"},
                    {"key": "D", "text": "Porque tiene un retraso de 24 horas en la sincronización.", "correct": "false"}
                ]
            }
        },
        {
            "archetype": "section",
            "title": "Dominio 2",
            "notes": "Continuamos con Secret Protection. Este es un dominio clave donde se producen la mayoría de los fallos por no entender el flujo de remediación y el Partner Program.",
            "slots": {
                "PART_LABEL": "DOMINIO 2",
                "TITLE": "Secret Protection",
                "SUBTITLE": "Escaneo, Push Protection y Remediación (15-20%)",
                "AGENDA": [
                    {"label": "2.1", "text": "Push Protection y Bypass"},
                    {"label": "2.2", "text": "Validity Checks"},
                    {"label": "2.3", "text": "Ciclo de Remediación"}
                ]
            }
        },
        {
            "archetype": "matrix",
            "title": "Motivos de Bypass",
            "notes": "Cuando un desarrollador se salta el Push Protection, la alerta se genera inmediatamente pero su estado de cierre depende del motivo seleccionado.",
            "slots": {
                "TAG_LEFT": "DOMINIO 2",
                "TITLE": "Bypass de Push Protection",
                "TAG_RIGHT": "BYPASS",
                "AXIS_X": "Estado de la alerta",
                "AXIS_Y": "Riesgo Asumido",
                "SIDE_TITLE": "Motivos",
                "Q1_TAG": "ABIERTA",
                "Q1_TITLE": "I'll fix it later",
                "Q1_DESC": "La alerta se genera y queda abierta. Es deuda técnica de seguridad inminente.",
                "Q2_TAG": "CERRADA",
                "Q2_TITLE": "Used in tests",
                "Q2_DESC": "GitHub crea la alerta y la cierra como 'used in tests'.",
                "Q3_TAG": "CERRADA",
                "Q3_TITLE": "False positive",
                "Q3_DESC": "GitHub crea la alerta y la cierra como 'false positive'.",
                "Q4_TAG": "ACCIÓN",
                "Q4_TITLE": "Delegated Bypass",
                "Q4_DESC": "Proceso de aprobación. Las solicitudes expiran en 7 días si nadie aprueba.",
                "RULES": [
                    {"label": "Audit", "text": "Todo bypass genera un evento en el audit log."},
                    {"label": "Email", "text": "Envía email a los administradores del repo y security managers."},
                    {"label": "Alerta", "text": "Aún si es falso positivo, la alerta se CREA y luego se Cierra."}
                ]
            }
        },
        {
            "archetype": "timeline",
            "title": "Remediación",
            "notes": "Nunca elijas 'reescribir el historial' como la primera opción en el examen. Un secreto ya pudo haber sido clonado. La primera acción siempre es rotar/revocar.",
            "slots": {
                "TAG_LEFT": "DOMINIO 2",
                "TITLE": "El Orden Correcto de Remediación",
                "TAG_RIGHT": "FLUJO",
                "LEAD": "Qué hacer cuando detectas un secreto filtrado en el historial.",
                "COLS": "4",
                "STEPS": [
                    {"n": "1", "phase": "Crítico", "title": "Rotar / Revocar", "desc": "La credencial expuesta en el proveedor. ¡Siempre lo primero!", "output": "Secreto inútil"},
                    {"n": "2", "phase": "Código", "title": "Sustituir", "desc": "Por una referencia segura (Actions secrets, Key Vault).", "output": "Código seguro"},
                    {"n": "3", "phase": "Git", "title": "Eliminar", "desc": "Eliminar el secreto del código actual y hacer commit.", "output": "Commit limpio"},
                    {"n": "4", "phase": "GHAS", "title": "Cerrar Alerta", "desc": "Cerrar la alerta con la resolución adecuada.", "output": "Alerta cerrada"}
                ]
            }
        },
        {
            "archetype": "concept-cards",
            "title": "Características Avanzadas",
            "notes": "Los validity checks cambian por completo la prioridad de un triage. Si la credencial dice que sigue activa, el riesgo es extremo. El partner program funciona solo en repos públicos.",
            "slots": {
                "TAG_LEFT": "DOMINIO 2",
                "TITLE": "Validación y Patrones",
                "TAG_RIGHT": "ADVANCED",
                "COLS": "3",
                "CARDS": [
                    {
                        "badge": "Verificación",
                        "title": "Validity Checks",
                        "body": "Contacta al emisor para saber si la credencial sigue activa. Requiere Code Security para metadatos extendidos.",
                        "note_label": "Prioridad",
                        "note": "Acelera el triage."
                    },
                    {
                        "badge": "Custom",
                        "title": "Custom Patterns",
                        "body": "Expresiones regulares (org o repo) para credenciales internas. Soporta push protection.",
                        "note_label": "Nivel",
                        "note": "Requiere licencia SP."
                    },
                    {
                        "badge": "Públicos",
                        "title": "Partner Program",
                        "body": "En repos públicos, notifica al proveedor directo, NO crea alerta en tu repo.",
                        "note_label": "Matiz",
                        "note": "Revocación proactiva."
                    }
                ]
            }
        },
        {
            "archetype": "quiz",
            "title": "Quiz - Dominio 2",
            "notes": "Para evitar los dismissals directos usamos Delegated alert dismissal.",
            "slots": {
                "TAG_LEFT": "REPASO",
                "TITLE": "Knowledge Check: Dominio 2",
                "TAG_RIGHT": "Q2",
                "BADGE": "Pregunta de Examen",
                "QUESTION": "Si un desarrollador intenta hacer un push con un secreto y selecciona 'I'll fix it later' en la CLI. ¿Qué sucede con la alerta en GHAS?",
                "COLS": "2",
                "EXPLANATION_LABEL": "Respuesta correcta",
                "EXPLANATION": "Seleccionar 'I'll fix it later' es el único motivo que deja la alerta formalmente abierta en el dashboard de GHAS.",
                "OPTIONS": [
                    {"key": "A", "text": "La alerta se crea y se cierra como 'used in tests'.", "correct": "false"},
                    {"key": "B", "text": "La alerta se crea y permanece abierta.", "correct": "true"},
                    {"key": "C", "text": "El push se rechaza completamente y no se crea alerta.", "correct": "false"},
                    {"key": "D", "text": "La alerta se elimina automáticamente.", "correct": "false"}
                ]
            }
        },
        {
            "archetype": "section",
            "title": "Dominio 3",
            "notes": "Pasamos a Supply Chain Security. Hay que tener muy clara la diferencia entre Version Updates (que requiere YAML y usa SemVer) y Security Updates (que usa el Grafo de Dependencias).",
            "slots": {
                "PART_LABEL": "DOMINIO 3",
                "TITLE": "Supply Chain Security",
                "SUBTITLE": "Dependabot & Dependency Review (15-20%)",
                "AGENDA": [
                    {"label": "3.1", "text": "Dependency Graph"},
                    {"label": "3.2", "text": "Los 4 Sabores de Dependabot"},
                    {"label": "3.3", "text": "Dependabot.yml config"},
                    {"label": "3.4", "text": "SBOM y Attestations"}
                ]
            }
        },
        {
            "archetype": "feature-matrix",
            "title": "Sabores de Dependabot",
            "notes": "Las actualizaciones de versión necesitan el dependabot.yml. Las actualizaciones de seguridad no. El dependency graph alimenta todo excepto las Version Updates.",
            "slots": {
                "TAG_LEFT": "DOMINIO 3",
                "TITLE": "Los Cuatro Sabores de Dependabot",
                "TAG_RIGHT": "DEPENDABOT",
                "LEAD": "Diferencias cruciales para el examen sobre cómo opera cada uno.",
                "HEADERS": "<th>Característica</th><th>Requiere dependabot.yml</th><th>Usa Dependency Graph</th><th>Objetivo</th>",
                "NOTE_LABEL": "¡Ojo!",
                "NOTE": "Las Version Updates ignoran el Dependency Graph porque se basan exclusivamente en Versionado Semántico (SemVer).",
                "ROWS": [
                    {"cells": "<td>Dependabot Alerts</td><td><span class=\"mk no\">No</span></td><td><span class=\"mk yes\">Sí</span></td><td><span class=\"mk null\">Generar alertas</span></td>"},
                    {"cells": "<td>Malware Alerts</td><td><span class=\"mk no\">No</span></td><td><span class=\"mk yes\">Sí</span></td><td><span class=\"mk null\">Alertas de paquetes maliciosos</span></td>"},
                    {"cells": "<td>Security Updates</td><td><span class=\"mk no\">No (opcional)</span></td><td><span class=\"mk yes\">Sí</span></td><td><span class=\"mk yes\">Versión mínima segura</span></td>"},
                    {"cells": "<td>Version Updates</td><td><span class=\"mk yes\">Obligatorio</span></td><td><span class=\"mk no\">No (SemVer)</span></td><td><span class=\"mk yes\">Última versión disponible</span></td>"}
                ]
            }
        },
        {
            "archetype": "dodont",
            "title": "Dependency Review",
            "notes": "Dependency review action te permite bloquear Pull Requests basándose en licencias prohibidas o severidad de vulnerabilidades.",
            "slots": {
                "TAG_LEFT": "DOMINIO 3",
                "TITLE": "Dependency Review Action",
                "TAG_RIGHT": "CI/CD",
                "BAD_TITLE": "Configuración Inválida",
                "BAD_SNIPPET": "with:\n  fail-on-severity: high\n  allow-licenses: MIT, BSD\n  deny-licenses: GPL",
                "GOOD_TITLE": "Configuración Válida",
                "GOOD_SNIPPET": "with:\n  fail-on-severity: critical\n  allow-licenses: MIT, BSD, Apache-2.0\n  fail-on-scopes: development",
                "WHY_LABEL": "Por qué",
                "WHY": "allow-licenses y deny-licenses son mutuamente excluyentes. No puedes usar ambas en el mismo workflow.",
                "BAD_POINTS": [
                    {"text": "Uso de licencias permitidas y denegadas juntas"}
                ],
                "GOOD_POINTS": [
                    {"text": "Uso de 'fail-on-severity' para establecer umbral"}
                ]
            }
        },
        {
            "archetype": "concept-cards",
            "title": "Procedencia y SBOM",
            "notes": "El SBOM que exporta GHAS siempre es SPDX. Las Artifact Attestations son muy importantes en GHEC para asegurar la procedencia y combatir ataques de inyección de código.",
            "slots": {
                "TAG_LEFT": "DOMINIO 3",
                "TITLE": "Integridad de la Cadena de Suministro",
                "TAG_RIGHT": "SBOM",
                "COLS": "3",
                "CARDS": [
                    {
                        "badge": "Inventario",
                        "title": "SBOM",
                        "body": "Se exporta el Dependency graph en formato compatible SPDX (Software Bill of Materials).",
                        "note_label": "API",
                        "note": "Requiere acceso Read."
                    },
                    {
                        "badge": "Integridad",
                        "title": "Artifact Attestations",
                        "body": "Declaraciones firmadas criptográficamente sobre la procedencia de un artefacto construido en Actions.",
                        "note_label": "Licencia",
                        "note": "GHEC para privados."
                    },
                    {
                        "badge": "Ruido",
                        "title": "Auto-triage rules",
                        "body": "Descartan o posponen alertas ANTES de notificar. Ideal para dependencias scoped a development.",
                        "note_label": "Ventaja",
                        "note": "Menos fatiga de alerta."
                    }
                ]
            }
        },
        {
            "archetype": "quiz",
            "title": "Quiz - Dominio 3",
            "notes": "Las actualizaciones de seguridad siempre van a la versión mínima que soluciona el problema, para evitar romper cambios (breaking changes).",
            "slots": {
                "TAG_LEFT": "REPASO",
                "TITLE": "Knowledge Check: Dominio 3",
                "TAG_RIGHT": "Q3",
                "BADGE": "Pregunta de Examen",
                "QUESTION": "¿Hacia qué versión de una dependencia actualiza un PR de Dependabot Security Update?",
                "COLS": "2",
                "EXPLANATION_LABEL": "Respuesta correcta",
                "EXPLANATION": "Para reducir el riesgo de incompatibilidades, Dependabot actualiza a la versión mínima necesaria para tapar el hueco.",
                "OPTIONS": [
                    {"key": "A", "text": "A la última versión menor disponible.", "correct": "false"},
                    {"key": "B", "text": "A la versión mínima necesaria que parchea la vulnerabilidad.", "correct": "true"},
                    {"key": "C", "text": "A la última versión compatible según SemVer.", "correct": "false"},
                    {"key": "D", "text": "A la última versión mayor publicada.", "correct": "false"}
                ]
            }
        },
        {
            "archetype": "section",
            "title": "Dominio 4",
            "notes": "Code Security, especialmente CodeQL. Dominio altamente técnico. Importante diferenciar Default Setup de Advanced Setup.",
            "slots": {
                "PART_LABEL": "DOMINIO 4",
                "TITLE": "Code Security con CodeQL",
                "SUBTITLE": "Análisis Estático (SAST) y Dataflow (10-15%)",
                "AGENDA": [
                    {"label": "4.1", "text": "Default vs Advanced Setup"},
                    {"label": "4.2", "text": "Workflows y Build modes"},
                    {"label": "4.3", "text": "Query suites"},
                    {"label": "4.4", "text": "SARIF e interoperabilidad"}
                ]
            }
        },
        {
            "archetype": "comparison",
            "title": "Setup de CodeQL",
            "notes": "La query suite 'security-and-quality' no existe en Default Setup, requiere obligatoriamente Advanced Setup.",
            "slots": {
                "TAG_LEFT": "DOMINIO 4",
                "TITLE": "Configuración de CodeQL",
                "TAG_RIGHT": "SETUP",
                "VS_LABEL": "VS",
                "LEFT_LABEL": "Gestión automática",
                "LEFT_TITLE": "Default Setup",
                "LEFT_BODY": "Ideal para habilitación a escala en cientos de repos. Sin archivos YAML visibles. Detecta lenguajes automáticamente.",
                "LEFT_EXAMPLE": "Suites: default, security-extended",
                "RIGHT_LABEL": "Control total",
                "RIGHT_TITLE": "Advanced Setup",
                "RIGHT_BODY": "Fichero `.github/workflows/codeql.yml`. Controlas matrices, builds complejos manuales y filtros de queries.",
                "RIGHT_EXAMPLE": "Suite: security-and-quality",
                "LEFT_POINTS": [
                    {"text": "No permite builds manuales"},
                    {"text": "Fácil despliegue"}
                ],
                "RIGHT_POINTS": [
                    {"text": "Permite builds manuales"},
                    {"text": "Permite exclude paths con exactitud"}
                ],
                "RIGHT_TAGS": [
                    {"text": "Requerido para security-and-quality"}
                ]
            }
        },
        {
            "archetype": "code-criteria",
            "title": "Workflow de CodeQL",
            "notes": "El permiso security-events: write es OBLIGATORIO para subir los resultados.",
            "slots": {
                "TAG_LEFT": "DOMINIO 4",
                "TITLE": "Anatomía del Workflow",
                "TAG_RIGHT": "YAML",
                "KICKER": "codeql.yml",
                "CODE_TITLE": "Componentes clave",
                "CODE": "jobs:\n  analyze:\n    permissions:\n      security-events: write\n    steps:\n    - uses: github/codeql-action/init@v4\n      with:\n        languages: ${{ matrix.language }}\n    - run: make clean && make  # manual build\n    - uses: github/codeql-action/analyze@v4\n      with:\n        category: \"/language:${{ matrix.language }}\"",
                "PANEL_TITLE": "Requisitos del Examen",
                "WHY_TITLE": "Permisos y Parámetros",
                "WHY": "El analizador necesita write access a security-events para insertar alertas en la UI.",
                "CRITERIA": [
                    {"letter": "1", "name": "Permisos", "meta": "security-events: write es obligatorio", "highlight": "hi"},
                    {"letter": "2", "name": "Init", "meta": "La acción init debe declarar los lenguajes", "highlight": ""},
                    {"letter": "3", "name": "Build", "meta": "Build-mode: manual requiere comandos explícitos", "highlight": ""},
                    {"letter": "4", "name": "Category", "meta": "Permite múltiples análisis del mismo commit", "highlight": "hi"}
                ]
            }
        },
        {
            "archetype": "anatomy",
            "title": "Alertas y SARIF",
            "notes": "GitHub etiqueta las alertas fuera de código de aplicación (Generated, Test, Library, Documentation).",
            "slots": {
                "TAG_LEFT": "DOMINIO 4",
                "TITLE": "Alertas y Formato SARIF",
                "TAG_RIGHT": "ALERTS",
                "SPEC_TITLE": "Interoperabilidad"
            },
            "slots_repeats": {
                "FIELDS": [
                    {"key": "SARIF", "value": "Static Analysis Results Interchange Format (v2.1.0 JSON)", "highlight": "hi"},
                    {"key": "CodeQL CLI", "value": "Permite correr el análisis offline/on-premise y subir el SARIF a la API", "highlight": ""},
                    {"key": "Terceros", "value": "Herramientas como Snyk o Checkmarx suben su SARIF", "highlight": ""},
                    {"key": "Etiquetas automáticas", "value": "Generated, Test, Library, Documentation", "highlight": ""}
                ],
                "NOTES": [
                    {"n": "1", "title": "Dataflow", "text": "CodeQL rastrea desde un Source (origen) hasta un Sink (sumidero)."},
                    {"n": "2", "title": "Agrupación", "text": "Diferentes rutas al mismo sink generan UNA SOLA alerta agrupada."}
                ]
            }
        },
        {
            "archetype": "quiz",
            "title": "Quiz - Dominio 4",
            "notes": "Una pregunta muy común del examen.",
            "slots": {
                "TAG_LEFT": "REPASO",
                "TITLE": "Knowledge Check: Dominio 4",
                "TAG_RIGHT": "Q4",
                "BADGE": "Pregunta de Examen",
                "QUESTION": "Si configuras un workflow de CodeQL con `on: pull_request: paths-ignore: ['**/*.md']`, ¿qué significa esto?",
                "COLS": "2",
                "EXPLANATION_LABEL": "Respuesta correcta",
                "EXPLANATION": "El trigger on decide si el WORKFLOW se ejecuta, no los archivos que analiza.",
                "OPTIONS": [
                    {"key": "A", "text": "CodeQL excluirá todos los archivos markdown de su análisis.", "correct": "false"},
                    {"key": "B", "text": "El workflow no se disparará si el PR solo modifica archivos markdown.", "correct": "true"},
                    {"key": "C", "text": "Ocurrirá un error de sintaxis en el archivo YAML.", "correct": "false"},
                    {"key": "D", "text": "Se analizarán los markdown solo si hay cambios en otros archivos.", "correct": "false"}
                ]
            }
        },
        {
            "archetype": "section",
            "title": "Dominio 5",
            "notes": "Operaciones de seguridad: cómo lidiar con 5,000 alertas. Hablamos de campañas, CVSS vs EPSS y Security Manager.",
            "slots": {
                "PART_LABEL": "DOMINIO 5",
                "TITLE": "Operaciones de Seguridad",
                "SUBTITLE": "Priorización, Campañas y Roles (15-20%)",
                "AGENDA": [
                    {"label": "5.1", "text": "CVE, CWE y EPSS"},
                    {"label": "5.2", "text": "Security Campaigns"},
                    {"label": "5.3", "text": "Roles de Seguridad"}
                ]
            }
        },
        {
            "archetype": "heatmap",
            "title": "Priorización de Vulnerabilidades",
            "notes": "EPSS indica probabilidad de explotación en 30 días, mientras CVSS es el impacto si es explotada. Juntas priorizan el riesgo.",
            "slots": {
                "TAG_LEFT": "DOMINIO 5",
                "TITLE": "La matriz CVSS vs EPSS",
                "TAG_RIGHT": "TRIAGE",
                "AXIS_X": "CVSS (Impacto Severidad)",
                "AXIS_Y": "EPSS (Probabilidad de Explotación)",
                "EXPL_TITLE": "Triage Inteligente",
                "EXPL_BODY": "Prioriza siempre el cuadrante superior derecho: Alto impacto y alta probabilidad de explotación a corto plazo.",
                "COLS": "3",
                "CELLS": [
                    {"label": "Priorizar luego", "level": "1"},
                    {"label": "Monitorear", "level": "2"},
                    {"label": "Mitigar", "level": "3"},
                    {"label": "Monitorear", "level": "2"},
                    {"label": "Mitigar", "level": "3"},
                    {"label": "ALERTA", "level": "4"},
                    {"label": "Aceptar Riesgo", "level": "1"},
                    {"label": "Parcheo Menor", "level": "1"},
                    {"label": "Crítico Rápido", "level": "4"}
                ],
                "ZONES": [
                    {"badge": "Top Priority", "condition": "Alta EPSS + Alta CVSS", "title": "Remediación Inmediata", "desc": "Campañas urgentes o hotfixes.", "color": "var(--err)", "bg": "var(--err-bg)"},
                    {"badge": "Low Priority", "condition": "Baja EPSS + Baja CVSS", "title": "Deuda Técnica", "desc": "Se auto-descarta o se mete a campañas largas.", "color": "var(--card-border)", "bg": "transparent"}
                ]
            }
        },
        {
            "archetype": "roadmap",
            "title": "Security Campaigns",
            "notes": "Las campañas centralizan los esfuerzos. En código, Autofix genera las correcciones; en secretos, no hay autofix, hay que rotar.",
            "slots": {
                "TAG_LEFT": "DOMINIO 5",
                "TITLE": "Ciclo de Vida de una Campaña",
                "TAG_RIGHT": "CAMPAIGNS",
                "LEAD": "Coordinación y reducción de deuda técnica a gran escala.",
                "COLS": "4",
                "LANES": [
                    {
                        "phase": "1. Identificar",
                        "when": "Manager",
                        "color": "var(--a1)",
                        "items": "<div class=\"rd-item st-done\">Agrupar por CWE</div><div class=\"rd-item st-done\">Seleccionar repos afectados</div>"
                    },
                    {
                        "phase": "2. Crear",
                        "when": "Setup",
                        "color": "var(--a2)",
                        "items": "<div class=\"rd-item st-now\">Due date definido</div><div class=\"rd-item st-now\">Manager asignado</div>"
                    },
                    {
                        "phase": "3. Notificar",
                        "when": "Equipos",
                        "color": "var(--warn)",
                        "items": "<div class=\"rd-item st-next\">Notificación a dueños (Write)</div>"
                    },
                    {
                        "phase": "4. Remediar",
                        "when": "Desarrolladores",
                        "color": "var(--ok)",
                        "items": "<div class=\"rd-item st-later\">Copilot Autofix (código)</div><div class=\"rd-item st-later\">Rotación manual (secretos)</div>"
                    }
                ]
            }
        },
        {
            "archetype": "quiz",
            "title": "Quiz - Dominio 5",
            "notes": "Es vital saber que Security Manager es un rol a nivel de EQUIPO.",
            "slots": {
                "TAG_LEFT": "REPASO",
                "TITLE": "Knowledge Check: Dominio 5",
                "TAG_RIGHT": "Q5",
                "BADGE": "Pregunta de Examen",
                "QUESTION": "Quieres que tres personas puedan leer todas las alertas de seguridad y gestionar configuraciones sin darles acceso de escritura al código de la organización. ¿Qué haces?",
                "COLS": "2",
                "EXPLANATION_LABEL": "Respuesta correcta",
                "EXPLANATION": "El rol de Security Manager se asigna siempre a un equipo, nunca a usuarios individuales, y provee acceso de lectura a los repos.",
                "OPTIONS": [
                    {"key": "A", "text": "Los agregas individualmente con el rol Security Manager.", "correct": "false"},
                    {"key": "B", "text": "Creas un equipo y les asignas el rol Security Manager al equipo.", "correct": "true"},
                    {"key": "C", "text": "Les das el rol de Organization Owner.", "correct": "false"},
                    {"key": "D", "text": "Los añades a cada repo como Administradores.", "correct": "false"}
                ]
            }
        },
        {
            "archetype": "section",
            "title": "Dominio 6",
            "notes": "Dominio 6: Administración, Security Configurations y Enforcement. Es crucial entender cómo se heredan las políticas.",
            "slots": {
                "PART_LABEL": "DOMINIO 6",
                "TITLE": "Administración de Suites",
                "SUBTITLE": "Governance y Security Configurations (10-15%)",
                "AGENDA": [
                    {"label": "6.1", "text": "Niveles de Habilitación"},
                    {"label": "6.2", "text": "Security Configurations (Enforce)"},
                    {"label": "6.3", "text": "APIs y Automatización"}
                ]
            }
        },
        {
            "archetype": "diagram",
            "title": "Jerarquía de Habilitación",
            "notes": "Todo lo que la empresa o la organización marca como ENFORCE, el repositorio no lo puede cambiar. Si NO tiene enforce, el repositorio lo puede sobreescribir.",
            "slots": {
                "TAG_LEFT": "DOMINIO 6",
                "TITLE": "Herencia y Enforcement",
                "TAG_RIGHT": "POLICIES",
                "SPLIT": "1fr 1fr",
                "DIAGRAM": "flowchart TD\nE[Empresa] -->|Políticas globales| O[Organización]\nO -->|Security Config + Enforce| R[Repositorio]\nR -.->|Si NO hay enforce| O\nstyle E fill:var(--a1),stroke:#fff\nstyle O fill:var(--a2),stroke:#fff\nstyle R fill:var(--bg),stroke:var(--a2)",
                "SIDE_TITLE": "Regla de Oro",
                "LEAD": "La política superior manda si tiene Enforce activo.",
                "NOTE_LABEL": "Security Configurations",
                "NOTE": "Las configuraciones predeterminadas solo se aplican automáticamente a repositorios NUEVOS. Si transfieres un repo, debes asignarla manual."
            },
            "slots_repeats": {
                "STEPS": [
                    {"n": "1", "name": "Empresa", "text": "Decide si GHAS está habilitado a nivel global."},
                    {"n": "2", "name": "Organización", "text": "Crea y aplica Security Configurations con defaults."},
                    {"n": "3", "name": "Repositorio", "text": "Puede ajustar configuración granular si el nivel superior lo permite."}
                ]
            }
        },
        {
            "archetype": "metrics",
            "title": "Límites y Licencias",
            "notes": "Facturación por comitter activo es una métrica clave del examen.",
            "slots": {
                "TAG_LEFT": "DOMINIO 6",
                "TITLE": "Reglas de Licenciamiento",
                "TAG_RIGHT": "LICENSES",
                "LEAD": "Licencias por Committer Activo Único.",
                "COLS": "3",
                "SOURCE": "Fuente: GitHub Docs (GHAS Billing)",
                "METRICS": [
                    {"label": "Ventana", "value": "90", "unit": "días", "desc": "Periodo de actividad para considerar a un committer activo.", "pct": "100%"},
                    {"label": "Límite SARIF", "value": "10", "unit": "MB", "desc": "Tamaño máximo de un archivo SARIF comprimido.", "pct": "100%"},
                    {"label": "Límite PRs (Version Updates)", "value": "5", "unit": "PRs", "desc": "Open PR limit por defecto (No aplica a security updates).", "pct": "100%"}
                ]
            }
        },
        {
            "archetype": "quiz",
            "title": "Quiz - Dominio 6",
            "notes": "Habilitación masiva y segura.",
            "slots": {
                "TAG_LEFT": "REPASO",
                "TITLE": "Knowledge Check: Dominio 6",
                "TAG_RIGHT": "Q6",
                "BADGE": "Pregunta de Examen",
                "QUESTION": "Tienes 200 repos con flujos avanzados de CodeQL mediante ficheros YAML personalizados y quieres habilitar CodeQL en 300 repositorios más usando una Security Configuration a nivel Organización. ¿Qué política seleccionas para evitar romper los repos antiguos?",
                "COLS": "2",
                "EXPLANATION_LABEL": "Respuesta correcta",
                "EXPLANATION": "Esta opción despliega el default setup SOLO donde no detecte un análisis de CodeQL configurado de antemano.",
                "OPTIONS": [
                    {"key": "A", "text": "Default Setup: Enabled con Enforce marcado.", "correct": "false"},
                    {"key": "B", "text": "Advanced Setup Only.", "correct": "false"},
                    {"key": "C", "text": "Default Setup: Enabled with advanced setup allowed.", "correct": "true"},
                    {"key": "D", "text": "Deshabilitar todos los flujos YAML primero.", "correct": "false"}
                ]
            }
        },
        {
            "archetype": "resources",
            "title": "Recursos",
            "notes": "Lecturas recomendadas para el examen y link al simulador.",
            "slots": {
                "TAG_LEFT": "MATERIAL",
                "TITLE": "Recursos Adicionales",
                "TAG_RIGHT": "LINKS",
                "LIST_TITLE": "Lecturas Oficiales",
                "QR_LABEL": "Escanea para",
                "QR_DATA": "https://docs.github.com/es/code-security",
                "QR_ALT": "GitHub Docs",
                "QR_CAPTION": "GitHub Docs: Code Security",
                "NEXT_LABEL": "Preparación",
                "NEXT": "Completa el simulacro de 80 preguntas incluido en la guía de estudio original."
            },
            "slots_repeats": {
                "RESOURCES": [
                    {"icon": "📚", "title": "GitHub Advisory Database", "desc": "Repositorio central de CVE y GHSA.", "url": "https://github.com/advisories"},
                    {"icon": "💻", "title": "CodeQL Action", "desc": "Documentación oficial del action.", "url": "https://github.com/github/codeql-action"},
                    {"icon": "🧪", "title": "Sandbox del Examen", "desc": "Entorno demo de Pearson VUE.", "url": "https://GHCertDemo.starttest.com"}
                ]
            }
        },
        {
            "archetype": "closing",
            "title": "Cierre",
            "notes": "Muchas gracias y éxito en el examen GH-500.",
            "slots": {
                "TAG_LEFT": "FIN",
                "TITLE": "Éxito en tu examen",
                "TAG_RIGHT": "GH-500",
                "ICON": "🏁",
                "HERO_TITLE": "Aprobar GH-500 requiere pensamiento sistemático.",
                "HERO_TEXT": "Recuerda: la seguridad shift-left ahorra dinero, el audit log es la única fuente de verdad para compliance, y siempre se rota un secreto antes de cualquier otra cosa.",
                "LEFT_PANEL_TITLE": "Takeaways Clave",
                "RIGHT_PANEL_TITLE": "Siguientes Pasos",
                "NEXT_LABEL": "Práctica",
                "NEXT": "Realiza los laboratorios de configuración sugeridos antes del examen."
            },
            "slots_repeats": {
                "TAKEAWAYS": [
                    {"n": "1", "text": "Code Security = vulnerabilidades lógicas. Secret Protection = credenciales expuestas."},
                    {"n": "2", "text": "Push protection = prevention first. Dependency Review = gate-based."},
                    {"n": "3", "text": "Rotar credenciales > eliminar historial Git."}
                ],
                "NEXT_STEPS": [
                    {"n": "1", "text": "Crea tu org de prueba."},
                    {"n": "2", "text": "Configura un dependabot.yml."},
                    {"n": "3", "text": "Activa CodeQL Default Setup."}
                ]
            }
        }
    ]
}

# Fix some nested array assignments for fields defined as repeats
def format_slots_repeats():
    for slide in plan['slides']:
        if 'slots_repeats' in slide:
            if 'slots' not in slide:
                slide['slots'] = {}
            for k, v in slide['slots_repeats'].items():
                slide['slots'][k] = v
            del slide['slots_repeats']

format_slots_repeats()

with open('C:\\\\Users\\\\vicen\\\\OneDrive\\\\Escritorio\\\\EVA IPSS\\\\academy-portal\\\\cursos\\\\GH-500\\\\visual_plan.json', 'w', encoding='utf-8') as f:
    json.dump(plan, f, indent=2, ensure_ascii=False)
