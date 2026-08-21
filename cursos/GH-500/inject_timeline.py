import json

filepath = 'C:\\\\Users\\\\vicen\\\\OneDrive\\\\Escritorio\\\\EVA IPSS\\\\academy-portal\\\\cursos\\\\GH-500\\\\visual_plan.json'

with open(filepath, 'r', encoding='utf-8') as f:
    plan = json.load(f)

for slide in plan['slides']:
    if slide.get('archetype') == 'timeline' and slide.get('title') == 'Flujo de Remediación':
        slide['slots']['STEPS'] = [
            { "n": "1", "phase": "INMEDIATO", "title": "Rotar", "desc": "Revocar la credencial en el sistema de origen.", "output": "Acceso bloqueado" },
            { "n": "2", "phase": "REEMPLAZO", "title": "Sustituir", "desc": "Usar Actions secrets, Key Vault o Azure OIDC.", "output": "Referencia segura" },
            { "n": "3", "phase": "LIMPIEZA", "title": "Eliminar", "desc": "Quitar el secreto del código en tu rama actual.", "output": "Código limpio" },
            { "n": "4", "phase": "GHAS", "title": "Cerrar", "desc": "Marcar como 'Revoked' o 'False positive' en GitHub.", "output": "Alerta resuelta" },
            { "n": "5", "phase": "OPCIONAL", "title": "Purgar", "desc": "Reescribir el historial Git (rara vez útil si ya se rotó).", "output": "Historial purgado" },
            { "n": "6", "phase": "AUDITORÍA", "title": "Investigar", "desc": "Revisar logs para ver si hubo uso indebido.", "output": "Auditoría final" }
        ]
        if 'repeats' in slide:
            del slide['repeats']
        break

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(plan, f, indent=2, ensure_ascii=False)
