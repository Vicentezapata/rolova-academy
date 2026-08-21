import json

filepath = 'C:\\\\Users\\\\vicen\\\\OneDrive\\\\Escritorio\\\\EVA IPSS\\\\academy-portal\\\\cursos\\\\GH-500\\\\visual_plan.json'

with open(filepath, 'r', encoding='utf-8') as f:
    plan = json.load(f)

cyto_data = [
    { 'id': 'root', 'text': 'GitHub Advanced Security', 'parent': None, 'type': 'root' },
    { 'id': 'code_sec', 'text': 'Code Security', 'parent': 'root', 'type': 'branch', 'color': 'var(--a1)' },
    { 'id': 'cs1', 'text': 'Code scanning / CodeQL', 'parent': 'code_sec', 'type': 'leaf', 'color': 'var(--a1)' },
    { 'id': 'cs2', 'text': 'CodeQL CLI', 'parent': 'code_sec', 'type': 'leaf', 'color': 'var(--a1)' },
    { 'id': 'cs3', 'text': 'Copilot Autofix', 'parent': 'code_sec', 'type': 'leaf', 'color': 'var(--a1)' },
    { 'id': 'cs4', 'text': 'AI-powered security detections', 'parent': 'code_sec', 'type': 'leaf', 'color': 'var(--a1)' },
    { 'id': 'cs5', 'text': 'Dependency review', 'parent': 'code_sec', 'type': 'leaf', 'color': 'var(--a1)' },
    { 'id': 'cs6', 'text': 'Custom auto-triage rules', 'parent': 'code_sec', 'type': 'leaf', 'color': 'var(--a1)' },
    { 'id': 'cs7', 'text': 'Security campaigns - código', 'parent': 'code_sec', 'type': 'leaf', 'color': 'var(--a1)' },
    { 'id': 'cs8', 'text': 'Security overview', 'parent': 'code_sec', 'type': 'leaf', 'color': 'var(--a1)' },
    { 'id': 'secret_sec', 'text': 'Secret Protection', 'parent': 'root', 'type': 'branch', 'color': 'var(--a2)' },
    { 'id': 'sp1', 'text': 'Secret scanning', 'parent': 'secret_sec', 'type': 'leaf', 'color': 'var(--a2)' },
    { 'id': 'sp2', 'text': 'Push protection', 'parent': 'secret_sec', 'type': 'leaf', 'color': 'var(--a2)' },
    { 'id': 'sp3', 'text': 'AI-detected secrets', 'parent': 'secret_sec', 'type': 'leaf', 'color': 'var(--a2)' },
    { 'id': 'sp4', 'text': 'Custom patterns', 'parent': 'secret_sec', 'type': 'leaf', 'color': 'var(--a2)' },
    { 'id': 'sp5', 'text': 'Delegated bypass', 'parent': 'secret_sec', 'type': 'leaf', 'color': 'var(--a2)' },
    { 'id': 'sp6', 'text': 'Security campaigns - secretos', 'parent': 'secret_sec', 'type': 'leaf', 'color': 'var(--a2)' },
    { 'id': 'sp7', 'text': 'Security overview (secretos)', 'parent': 'secret_sec', 'type': 'leaf', 'color': 'var(--a2)' },
    { 'id': 'free_sec', 'text': 'Planes Gratuitos', 'parent': 'root', 'type': 'branch', 'color': 'var(--a3)' },
    { 'id': 'fs1', 'text': 'Dependency graph', 'parent': 'free_sec', 'type': 'leaf', 'color': 'var(--a3)' },
    { 'id': 'fs2', 'text': 'Dependabot alerts', 'parent': 'free_sec', 'type': 'leaf', 'color': 'var(--a3)' },
    { 'id': 'fs3', 'text': 'Dependabot security updates', 'parent': 'free_sec', 'type': 'leaf', 'color': 'var(--a3)' },
    { 'id': 'fs4', 'text': 'GitHub Advisory Database', 'parent': 'free_sec', 'type': 'leaf', 'color': 'var(--a3)' },
    { 'id': 'fs5', 'text': 'Private vulnerability reporting', 'parent': 'free_sec', 'type': 'leaf', 'color': 'var(--a3)' },
    { 'id': 'fs6', 'text': 'Artifact attestations', 'parent': 'free_sec', 'type': 'leaf', 'color': 'var(--a3)' }
]

for slide in plan['slides']:
    if slide.get('title') == 'Ecosistema GHAS' or 'html_content' in slide:
        if 'html_content' in slide:
            del slide['html_content']
        slide['archetype'] = 'cytoscape'
        slide['slots'] = {
            'TAG_LEFT': 'DOMINIO 1',
            'TITLE': 'Mapa mental del ecosistema GHAS',
            'TAG_RIGHT': 'INTERACTIVO',
            'LEAD': 'Haz clic en un nodo para expandir o colapsar la rama. Usa los botones para controlar la vista completa.',
            'CYTO_DATA': json.dumps(cyto_data, ensure_ascii=False)
        }
        # Keep notes as they were

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(plan, f, indent=2, ensure_ascii=False)
