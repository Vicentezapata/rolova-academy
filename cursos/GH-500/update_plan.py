import json

diagram_1 = """graph TD
    A[GitHub Advanced Security] --> B[GitHub Code Security]
    A --> C[GitHub Secret Protection]
    A --> D[Funciones incluidas en todos los planes]

    B --> B1[Code scanning / CodeQL]
    B --> B2[CodeQL CLI]
    B --> B3[Copilot Autofix]
    B --> B4[AI-powered security detections]
    B --> B5[Dependency review]
    B --> B6[Custom auto-triage rules Dependabot]
    B --> B7[Security campaigns - código]
    B --> B8[Security overview]

    C --> C1[Secret scanning]
    C --> C2[Push protection]
    C --> C3[AI-detected secrets]
    C --> C4[Custom patterns]
    C --> C5[Delegated bypass + Delegated alert dismissal]
    C --> C6[Security campaigns - secretos]
    C --> C7[Security overview]

    D --> D1[Dependency graph]
    D --> D2[Dependabot alerts]
    D --> D3[Dependabot security & version updates]
    D --> D4[GitHub Advisory Database]
    D --> D5[Private vulnerability reporting]
    D --> D6[Artifact attestations / Immutable releases]
"""

diagram_2 = """flowchart LR
    subgraph P["🛡️ PREVENCIÓN (shift-left)"]
        direction LR
        A["<b>1. PLAN</b><br/>Políticas<br/>Rulesets<br/>SECURITY.md"]
        B["<b>2. CODE</b><br/>Push protection<br/>Copilot Autofix<br/>IDE + CodeQL"]
        C["<b>3. BUILD / CI</b><br/>CodeQL en CI<br/>Secret scanning<br/>SBOM / dep. submit"]
    end
    subgraph G["🚦 PUERTAS (gates)"]
        D["<b>4. REVIEW / PR</b><br/>Dependency review<br/>Code scanning en PR<br/>Merge protection<br/>Autofix en PR"]
    end
    subgraph R["🔏 PROCEDENCIA"]
        E["<b>5. DEPLOY</b><br/>Artifact attestations<br/>Immutable releases"]
    end
    subgraph O["📊 DETECCIÓN Y RESPUESTA"]
        F["<b>6. OPERATE</b><br/>Security overview<br/>Campañas<br/>Auditoría<br/>Webhooks / API"]
    end

    A --> B --> C --> D --> E --> F
    F -. "retroalimenta políticas y campañas" .-> A
"""

diagram_3 = """flowchart LR
    A([Detección]) --> B["<b>OPEN</b><br/>alerta abierta"]
    B --> T{Triage}
    T -->|Se corrige el código| F["<b>Fixed / Resolved</b><br/>cierre 'bueno'"]
    T -->|Descarte manual con motivo| D["<b>Dismissed</b><br/>riesgo aceptado"]
    T -->|Regla automática| X["<b>Auto-dismissed</b><br/>auto-triage rules"]
    X -. "si deja de cumplir la regla" .-> B
"""

diagram_4 = """flowchart TD
    A([Detección del secreto]) --> B["<b>ALERTA ABIERTA</b>"]
    B --> C["1️⃣ <b>ROTAR / REVOCAR</b> la credencial<br/><i>SIEMPRE lo primero</i>"]
    C --> D["2️⃣ Sustituir por referencia segura<br/>Actions secrets · Key Vault · OIDC"]
    D --> E["3️⃣ Eliminar el secreto del código"]
    E --> F["4️⃣ Cerrar la alerta con resolución"]
    F --> G["5️⃣ <i>Opcional</i>: purgar el historial de Git"]
    G --> H["6️⃣ Investigar uso indebido<br/>durante la exposición"]

    F --> R1[Revoked]
    F --> R2[False positive]
    F --> R3[Used in tests]
    F --> R4["Won't fix"]
    F --> R5["Pattern edited / deleted<br/><i>cierre automático</i>"]
"""

with open('C:\\\\Users\\\\vicen\\\\OneDrive\\\\Escritorio\\\\EVA IPSS\\\\academy-portal\\\\cursos\\\\GH-500\\\\visual_plan.json', 'r', encoding='utf-8') as f:
    plan = json.load(f)

slides = plan['slides']

# Insert diagram_1 and diagram_2 after the slide with title "Dominio 1"
idx_dominio_1 = next(i for i, s in enumerate(slides) if s.get('title') == 'Dominio 1')

new_slide_1 = {
    "archetype": "diagram",
    "title": "Ecosistema GHAS",
    "notes": "Este mapa mental muestra la estructura general de GitHub Advanced Security, dividido en sus tres pilares.",
    "slots": {
        "TAG_LEFT": "DOMINIO 1",
        "TITLE": "Mapa mental del ecosistema GHAS",
        "TAG_RIGHT": "MAPA",
        "SPLIT": "1fr",
        "DIAGRAM": diagram_1,
        "SIDE_TITLE": "3 Pilares",
        "LEAD": "GitHub Advanced Security se compone de tres grandes bloques de características.",
        "NOTE_LABEL": "Nota",
        "NOTE": "El ecosistema abarca desde código hasta dependencias y secretos."
    },
    "slots_repeats": {
        "STEPS": [
            {"n": "1", "name": "Code Security", "text": "Análisis de vulnerabilidades lógicas en código propio."},
            {"n": "2", "name": "Secret Protection", "text": "Prevención y detección de credenciales."},
            {"n": "3", "name": "Supply Chain", "text": "Seguridad en las dependencias de terceros."}
        ]
    }
}

new_slide_2 = {
    "archetype": "diagram",
    "title": "Ciclo de Vida Seguro",
    "notes": "El ciclo SSDLC muestra dónde actúa cada característica de GHAS.",
    "slots": {
        "TAG_LEFT": "DOMINIO 1",
        "TITLE": "Ciclo de vida seguro (SSDLC)",
        "TAG_RIGHT": "FLUJO",
        "SPLIT": "1fr",
        "DIAGRAM": diagram_2,
        "SIDE_TITLE": "SSDLC",
        "LEAD": "Estrategias de seguridad integradas en el ciclo de vida.",
        "NOTE_LABEL": "Shift-left",
        "NOTE": "Cuanto más a la izquierda detectas el problema, más barato es corregirlo."
    },
    "slots_repeats": {
        "STEPS": [
            {"n": "1", "name": "Prevención", "text": "Evitar que entre el problema."},
            {"n": "2", "name": "Puertas", "text": "Bloquear en puntos de control."},
            {"n": "3", "name": "Operación", "text": "Detectar y responder a problemas."}
        ]
    }
}

slides.insert(idx_dominio_1 + 1, new_slide_2)
slides.insert(idx_dominio_1 + 1, new_slide_1)


# Insert diagram_3 before the "Dominio 2" section or somewhere in D1 (it's part of 1.5 Detección, gestión y respuesta a alertas)
# Let's find "Estrategias de Seguridad" slide and put it after that.
idx_estrategias = next(i for i, s in enumerate(slides) if s.get('title') == 'Estrategias de Seguridad')
new_slide_3 = {
    "archetype": "diagram",
    "title": "Ciclo de Alerta",
    "notes": "Toda alerta tiene un estado (abierto o cerrado) y una razón de resolución.",
    "slots": {
        "TAG_LEFT": "DOMINIO 1",
        "TITLE": "Ciclo de vida de una alerta",
        "TAG_RIGHT": "ALERTA",
        "SPLIT": "1fr",
        "DIAGRAM": diagram_3,
        "SIDE_TITLE": "Estados",
        "LEAD": "Cómo transitan las alertas desde su detección hasta su cierre.",
        "NOTE_LABEL": "Cuidado",
        "NOTE": "Descartar una alerta no elimina el riesgo técnico."
    },
    "slots_repeats": {
        "STEPS": [
            {"n": "1", "name": "Detección", "text": "Se crea la alerta."},
            {"n": "2", "name": "Triage", "text": "Se decide qué hacer."},
            {"n": "3", "name": "Cierre", "text": "Resolución o descarte."}
        ]
    }
}
slides.insert(idx_estrategias + 1, new_slide_3)

# Insert diagram_4 after "Remediación" timeline in D2
idx_remediacion = next(i for i, s in enumerate(slides) if s.get('title') == 'Remediación')
new_slide_4 = {
    "archetype": "diagram",
    "title": "Diagrama de Remediación",
    "notes": "Diagrama del flujo completo de respuesta a credenciales comprometidas.",
    "slots": {
        "TAG_LEFT": "DOMINIO 2",
        "TITLE": "Remediación de alertas de secretos",
        "TAG_RIGHT": "FLUJO",
        "SPLIT": "1fr",
        "DIAGRAM": diagram_4,
        "SIDE_TITLE": "Acción Clave",
        "LEAD": "El orden importa y rotar el secreto siempre va primero.",
        "NOTE_LABEL": "Reescritura",
        "NOTE": "Reescribir el historial de Git rara vez es útil frente a credenciales ya expuestas."
    },
    "slots_repeats": {
        "STEPS": [
            {"n": "1", "name": "Rotar", "text": "Revocar en el origen."},
            {"n": "2", "name": "Limpiar", "text": "Eliminar de código y Git."},
            {"n": "3", "name": "Investigar", "text": "Asegurar que no hubo uso indebido."}
        ]
    }
}
slides.insert(idx_remediacion + 1, new_slide_4)

def format_slots_repeats(slide):
    if 'slots_repeats' in slide:
        if 'slots' not in slide:
            slide['slots'] = {}
        for k, v in slide['slots_repeats'].items():
            slide['slots'][k] = v
        del slide['slots_repeats']

for slide in slides:
    format_slots_repeats(slide)

with open('C:\\\\Users\\\\vicen\\\\OneDrive\\\\Escritorio\\\\EVA IPSS\\\\academy-portal\\\\cursos\\\\GH-500\\\\visual_plan.json', 'w', encoding='utf-8') as f:
    json.dump(plan, f, indent=2, ensure_ascii=False)

