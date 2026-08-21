import json

filepath = r'C:\Users\vicen\OneDrive\Escritorio\EVA IPSS\academy-portal\cursos\GH-500\visual_plan.json'
with open(filepath, 'r', encoding='utf-8') as f:
    d = json.load(f)
for i, s in enumerate(d.get('slides', [])):
    print(f"{i}: {s.get('title', '')}")
