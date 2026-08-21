import json

filepath = 'C:\\\\Users\\\\vicen\\\\OneDrive\\\\Escritorio\\\\EVA IPSS\\\\academy-portal\\\\cursos\\\\GH-500\\\\visual_plan.json'

with open(filepath, 'r', encoding='utf-8') as f:
    plan = json.load(f)

for slide in plan['slides']:
    if slide.get('archetype') == 'diagram':
        diagram = slide['slots'].get('DIAGRAM', '')
        if slide['title'] == 'Ecosistema GHAS':
            # Convert to Left-to-Right
            diagram = diagram.replace('graph TD', 'graph LR')
            slide['slots']['DIAGRAM'] = diagram
        elif slide['title'] == 'Diagrama de Remediación':
            # Convert to Left-to-Right
            diagram = diagram.replace('flowchart TD', 'flowchart LR')
            slide['slots']['DIAGRAM'] = diagram

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(plan, f, indent=2, ensure_ascii=False)
