import json

filepath = r'C:\Users\vicen\OneDrive\Escritorio\EVA IPSS\academy-portal\cursos\GH-500\visual_plan.json'

with open(filepath, 'r', encoding='utf-8') as f:
    plan = json.load(f)

slides = plan['slides']

def find_quiz_index(domain_num):
    for i, s in enumerate(slides):
        if s.get('title', '') == f"Quiz - Dominio {domain_num}":
            return i
    return -1

# Domain 1
idx_d1 = find_quiz_index(1)
if idx_d1 != -1:
    d1_slides = [
        {
            "archetype": "table",
            "title": "Roles y Responsabilidades",
            "notes": "Una regla de oro del examen es saber quién puede hacer qué. El Security Manager no da acceso al código, solo a las alertas.",
            "slots": {
                "TAG_LEFT": "DOMINIO 1",
                "TITLE": "Matriz de Permisos (GHAS)",
                "TAG_RIGHT": "ROLES",
                "LEAD": "Identificar qué rol se requiere para cada acción de seguridad es crítico en el examen GH-500.",
                "HEADERS": "<th>Rol</th><th>Responsabilidad / Permisos</th>",
                "NOTE_LABEL": "Security Manager:",
                "NOTE": "Es un rol a nivel de <b>equipo</b>. Da permisos de lectura en todos los repositorios y acceso completo a ver y gestionar alertas de seguridad.",
                "ROWS": [
                    {"cells": "<td><strong>Enterprise Owner</strong></td><td>Políticas globales, licencias, habilitar GHAS globalmente.</td>"},
                    {"cells": "<td><strong>Org Owner</strong></td><td>Security configurations (crear/enforce), designar security managers.</td>"},
                    {"cells": "<td><strong>Security Manager</strong></td><td>Lectura global. Ver todas las alertas. NO da permisos write.</td>"},
                    {"cells": "<td><strong>Repo Admin</strong></td><td>Habilitar características, rulesets, acceso a alertas.</td>"},
                    {"cells": "<td><strong>Write / Maintain</strong></td><td>Ver y gestionar alertas, bypass (si no hay delegated), asignar alertas.</td>"},
                    {"cells": "<td><strong>Read</strong></td><td>Ver código y exportar SBOM. NO ve alertas de seguridad.</td>"}
                ]
            }
        },
        {
            "archetype": "concept-cards",
            "title": "Vistas de Security Overview",
            "notes": "Recuerda que para cumplimiento siempre se usa el Audit Log, ya que las vistas del dashboard pueden variar retrospectivamente.",
            "slots": {
                "TAG_LEFT": "DOMINIO 1",
                "TITLE": "Vistas de Security Overview",
                "TAG_RIGHT": "DASHBOARD",
                "COLS": "2",
                "CARDS": [
                    {"badge": "Riesgo", "title": "Risk & Coverage", "body": "<b>Risk</b>: Muestra el riesgo actual por vulnerabilidades y dependencias.<br><br><b>Coverage</b>: Adopción de GHAS por repositorio (quién lo tiene activado)."},
                    {"badge": "Acción", "title": "Campaigns", "body": "Crear y seguir agrupaciones de alertas (campañas) para remediación coordinada con desarrolladores. Disparan Copilot Autofix automático."},
                    {"badge": "Equipos", "title": "Enablement", "body": "Permite medir la velocidad de adopción de GHAS desglosado por equipos de desarrollo."},
                    {"badge": "⚠️ Audit Log vs Dashboard", "title": "Métricas de Cumplimiento", "body": "<b>Las métricas históricas del dashboard pueden cambiar retrospectivamente</b>.<br><br>Para evidencias formales de auditoría, <b>siempre</b> debes utilizar el <code>Audit log</code> (eventos inmutables)."}
                ]
            }
        }
    ]
    slides[idx_d1:idx_d1] = d1_slides


# Domain 2
# Remove old duplicate first if exists, so script is idempotent:
slides = [s for s in slides if s.get('title') not in [
    "Roles y Responsabilidades", "Vistas de Security Overview", 
    "Delegated Bypass", "Trampas de dependabot.yml", "Modelos de Riesgo: GHSA, CVSS y EPSS",
    "CodeQL Query Suites", "Troubleshooting CodeQL", "Gobernanza y PVR", 
    "GHEC vs GHES", "REST API y Despliegue Masivo"
]]

idx_d2 = find_quiz_index(2)
if idx_d2 != -1:
    for s in slides:
        if s.get('title') == "Características Avanzadas" and s.get('archetype') == "concept-cards":
            if "Secret scanning busca" not in s.get('notes', ''):
                s['notes'] += " Secret scanning busca en issues (abiertos y cerrados), PRs y wikis, no solo en el historial del código."
    
    d2_slides = [
        {
            "archetype": "concept-cards",
            "title": "Delegated Bypass",
            "notes": "Delegated bypass previene que los desarrolladores usen 'I'll fix it later' sin aprobación. Las solicitudes expiran a los 7 días.",
            "slots": {
                "TAG_LEFT": "DOMINIO 2",
                "TITLE": "Flujo de Delegated Bypass",
                "TAG_RIGHT": "BYPASS",
                "COLS": "3",
                "CARDS": [
                    {"badge": "Proceso", "title": "Aprobación Previa", "body": "Impide que los desarrolladores hagan bypass libremente en <b>push protection</b>. Requieren solicitar bypass y que un aprobador lo autorice."},
                    {"badge": "Límites", "title": "Expiración (7 días)", "body": "Toda solicitud de bypass de un desarrollador caduca automáticamente en <b>7 días</b> si no es aprobada por un administrador/manager."},
                    {"badge": "Configuración", "title": "Listas y Exenciones", "body": "<b>1. Bypass privileges:</b> Quién puede saltarse el bloqueo y aprobar a otros.<br><b>2. Exemptions:</b> Actores exentos totalmente (bots)."}
                ]
            }
        }
    ]
    slides[idx_d2:idx_d2] = d2_slides


# Domain 3
idx_d3 = find_quiz_index(3)
if idx_d3 != -1:
    d3_slides = [
        {
            "archetype": "concept-cards",
            "title": "Trampas de dependabot.yml",
            "notes": "Los updates de version y los de security tienen reglas distintas. Las security updates no se limitan por open-pull-requests-limit.",
            "slots": {
                "TAG_LEFT": "DOMINIO 3",
                "TITLE": "Matices en dependabot.yml",
                "TAG_RIGHT": "YML",
                "COLS": "3",
                "CARDS": [
                    {"badge": "Límites", "title": "open-pull-requests-limit", "body": "Límite por defecto: <b>5</b>.<br>Trampa: Los PRs de <i>security updates</i> <b>NO</b> cuentan ni están limitados por esta clave. Solo aplica a version updates.", "note_label": "Tip", "note": "Poner 0 desactiva version updates."},
                    {"badge": "Reglas", "title": "allow vs ignore", "body": "Se evalúa primero `allow`, luego `ignore`. Si una dependencia coincide en ambas listas, <b>se ignora</b> (el ignore tiene precedencia final).", "note_label": "Regla", "note": "Ignore siempre gana."},
                    {"badge": "Tiempos", "title": "cooldown", "body": "Aplica <b>solo</b> a version updates. Retrasa la actualización (default de GitHub: 3 días aunque no lo declares). <b>Nunca aplica a security updates</b>.", "note_label": "Uso", "note": "Evita paquetes maliciosos recientes."}
                ]
            }
        },
        {
            "archetype": "table",
            "title": "Modelos de Riesgo: GHSA, CVSS y EPSS",
            "notes": "CVSS mide el daño técnico. EPSS mide la probabilidad. Combinar ambos permite priorizar correctamente.",
            "slots": {
                "TAG_LEFT": "DOMINIO 3",
                "TITLE": "Estructuras y Modelos de Riesgo",
                "TAG_RIGHT": "EPSS",
                "LEAD": "Identificadores clave y cómo priorizar vulnerabilidades en base a CVSS y EPSS.",
                "HEADERS": "<th>Identificador</th><th>Descripción y Uso</th>",
                "NOTE_LABEL": "Fórmula moderna:",
                "NOTE": "Priorización = Daño técnico (<b>CVSS</b>) × Probabilidad (<b>EPSS</b>) × Contexto.",
                "ROWS": [
                    {"cells": "<td><strong>GHSA</strong></td><td>Identificador único de la GitHub Advisory Database (ej. <code>GHSA-jfh8-c2jp...</code>). Mapea a uno o varios CVE.</td>"},
                    {"cells": "<td><strong>CWE</strong></td><td>Clase o <i>tipo</i> de debilidad técnica (ej. <code>CWE-89</code> para inyección SQL). No es una vulnerabilidad específica.</td>"},
                    {"cells": "<td><strong>CVSS</strong></td><td>Sistema de puntuación de <b>severidad técnica</b> (0.0 - 10.0). No tiene en cuenta la probabilidad de ataque.</td>"},
                    {"cells": "<td><strong>EPSS</strong></td><td><b>Probabilidad de explotación en los próximos 30 días</b> (0% - 100%). Fundamental para priorizar parches frente a CVSS altos pero no explotados.</td>"}
                ]
            }
        }
    ]
    slides[idx_d3:idx_d3] = d3_slides


# Domain 4
idx_d4 = find_quiz_index(4)
if idx_d4 != -1:
    d4_slides = [
        {
            "archetype": "concept-cards",
            "title": "CodeQL Query Suites",
            "notes": "Recuerda que security-and-quality REQUIERE advanced setup. Default setup solo da hasta security-extended.",
            "slots": {
                "TAG_LEFT": "DOMINIO 4",
                "TITLE": "Suites y Archivos de CodeQL",
                "TAG_RIGHT": "SUITES",
                "COLS": "3",
                "CARDS": [
                    {"badge": "Base", "title": "Suite: default", "body": "Consultas de seguridad de <b>alta precisión</b>. Muy pocos falsos positivos. Ideal para despliegues iniciales silenciosos.", "note_label": "Setup", "note": "Default & Advanced"},
                    {"badge": "Ampliación", "title": "Suite: extended", "body": "<code>security-extended</code>. Suma consultas de precisión menor. Encuentra más fallos, pero incrementa los falsos positivos.", "note_label": "Setup", "note": "Default & Advanced"},
                    {"badge": "Máximo", "title": "Suite: quality", "body": "<code>security-and-quality</code>. Suma análisis de mantenibilidad y fiabilidad (deuda técnica). <b>Exige configuración avanzada</b>.", "note_label": "Setup", "note": "SOLO Advanced"}
                ]
            }
        },
        {
            "archetype": "table",
            "title": "Troubleshooting CodeQL",
            "notes": "Para los problemas de 'No source code', la solución suele ser cambiar el build-mode a manual o none.",
            "slots": {
                "TAG_LEFT": "DOMINIO 4",
                "TITLE": "Resolución de Problemas (CodeQL)",
                "TAG_RIGHT": "TROUBLESHOOTING",
                "LEAD": "Escenarios clásicos de examen sobre fallos durante el análisis de código.",
                "HEADERS": "<th>Síntoma / Error</th><th>Causa raíz y Solución</th>",
                "NOTE_LABEL": "Workflow vs Config:",
                "NOTE": "<code>paths-ignore</code> en <b>workflow</b> (determina si corre). <code>paths-ignore</code> en <b>CodeQL config</b> (determina qué ficheros analiza).",
                "ROWS": [
                    {"cells": "<td><strong>\"No source code was seen during the build\"</strong></td><td>El <code>autobuild</code> falló. <b>Solución:</b> Usa <code>build-mode: manual</code> (para definir los pasos) o <code>none</code> si aplica.</td>"},
                    {"cells": "<td><strong>Timeout / Análisis muy lento</strong></td><td>Código enorme. <b>Solución:</b> Paralelizar por lenguajes con matriz, reducir alcance con <code>paths</code>, o usar <code>none</code>.</td>"},
                    {"cells": "<td><strong>OOM (Out Of Memory)</strong></td><td>Falta de memoria en el runner al compilar o rastrear. <b>Solución:</b> Runner más grande y con más RAM.</td>"},
                    {"cells": "<td><strong>Alertas obsoletas no se cierran</strong></td><td>Configuraciones estancadas (stale). <b>Solución:</b> Re-ejecutar el workflow o eliminar las alertas asociadas a esa config.</td>"},
                    {"cells": "<td><strong>SARIF Rechazado</strong></td><td>Fichero excede los límites documentados (~10 MB gzip, ~5000 resultados).</td>"}
                ]
            }
        }
    ]
    slides[idx_d4:idx_d4] = d4_slides


# Domain 5
idx_d5 = find_quiz_index(5)
if idx_d5 != -1:
    d5_slides = [
        {
            "archetype": "concept-cards",
            "title": "Gobernanza y PVR",
            "notes": "PVR permite un flujo seguro y sin ruido público cuando alguien encuentra una vulnerabilidad en tu código. Y rulesets pueden forzar compliance.",
            "slots": {
                "TAG_LEFT": "DOMINIO 5",
                "TITLE": "Políticas y Flujos de Reporte",
                "TAG_RIGHT": "PVR",
                "COLS": "3",
                "CARDS": [
                    {"badge": "Rulesets", "title": "Merge Protection", "body": "Los <b>Rulesets</b> pueden bloquear el merge de un PR (Code Scanning) si una alerta de severidad alta es encontrada, o si el análisis sigue en curso."},
                    {"badge": "Documento", "title": "SECURITY.md", "body": "Política pública obligatoria en proyectos serios que indica explícitamente cómo y a quién reportar vulnerabilidades."},
                    {"badge": "Reporte Privado", "title": "PVR", "body": "Ofrece un canal cifrado y <b>privado</b> para que investigadores externos reporten bugs de seguridad sin crear issues públicos.<br><br>Genera un <b>draft advisory</b> y un <b>fork temporal</b>."}
                ]
            }
        }
    ]
    slides[idx_d5:idx_d5] = d5_slides


# Domain 6
idx_d6 = find_quiz_index(6)
if idx_d6 != -1:
    d6_slides = [
        {
            "archetype": "table",
            "title": "GHEC vs GHES",
            "notes": "GHES carece de las features 100% cloud como Public Monitoring, y requiere GitHub Connect para descargar advisories.",
            "slots": {
                "TAG_LEFT": "DOMINIO 6",
                "TITLE": "GitHub Enterprise: Cloud vs Server",
                "TAG_RIGHT": "GHEC/GHES",
                "LEAD": "Diferencias arquitectónicas en la disponibilidad de características de GHAS.",
                "HEADERS": "<th>Característica</th><th>GHEC (Cloud)</th><th>GHES (On-Prem Server)</th>",
                "NOTE_LABEL": "Public Monitoring:",
                "NOTE": "Monitorear miembros en repos públicos externos es <b>exclusivo de Cloud</b>.",
                "ROWS": [
                    {"cells": "<td><strong>Características de IA (Autofix)</strong></td><td>✅ Siempre disponibles (GA)</td><td>⚠️ Limitadas, dependen de la versión y conectividad con GitHub.com</td>"},
                    {"cells": "<td><strong>Public Monitoring (Secretos)</strong></td><td>✅ Habilitable</td><td>❌ No disponible</td>"},
                    {"cells": "<td><strong>Advisory Database y CodeQL Packs</strong></td><td>Descarga directa (Nube)</td><td>Requiere configurar <b>GitHub Connect</b> o usar una herramienta de sincronización offline.</td>"},
                    {"cells": "<td><strong>Actualizaciones de CodeQL</strong></td><td>Automáticas y transparentes</td><td>Empaquetadas con la release del Server (o vía bundle manual).</td>"}
                ]
            }
        },
        {
            "archetype": "concept-cards",
            "title": "REST API y Despliegue Masivo",
            "notes": "La API REST es fundamental para aplicar security configurations a miles de repos en masa.",
            "slots": {
                "TAG_LEFT": "DOMINIO 6",
                "TITLE": "Gestión a Escala (APIs)",
                "TAG_RIGHT": "REST",
                "COLS": "3",
                "CARDS": [
                    {"badge": "SARIF", "title": "Subida de SARIF", "body": "Se utiliza el endpoint <code>POST /repos/{owner}/{repo}/code-scanning/sarifs</code> para inyectar escaneos de herramientas SAST de terceros."},
                    {"badge": "SBOM", "title": "Exportación", "body": "Se pueden exportar manifiestos SPDX a través de <code>GET /dependency-graph/sbom</code> con solo permisos de lectura."},
                    {"badge": "Despliegue", "title": "Security Configurations", "body": "Habilitar GHAS en masa se logra usando la API:<br><br>1. <code>POST /code-security/configurations</code> (Crear)<br>2. <code>POST /.../attach</code> (Adjuntarla a repos existentes)<br>3. <code>PUT /.../defaults</code> (Forzar para repos futuros)."}
                ]
            }
        }
    ]
    slides[idx_d6:idx_d6] = d6_slides


plan['slides'] = slides

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(plan, f, indent=2, ensure_ascii=False)
