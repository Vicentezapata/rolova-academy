import json

filepath = 'C:\\\\Users\\\\vicen\\\\OneDrive\\\\Escritorio\\\\EVA IPSS\\\\academy-portal\\\\cursos\\\\GH-500\\\\visual_plan.json'

with open(filepath, 'r', encoding='utf-8') as f:
    plan = json.load(f)

html_slide = """
<div class="header">
  <span class="tag">DOMINIO 1</span>
  <span class="h2">Mapa mental del ecosistema GHAS</span>
  <span class="tag">INTERACTIVO</span>
</div>
<div class="divider"></div>
<div style="position:absolute;left:48px;top:88px;right:48px;bottom:44px;display:flex;flex-direction:column;gap:20px;z-index:10;">
  
  <p style="font-size:14px;color:var(--text-sec);line-height:1.7;">
    Este diagrama es interactivo. <b>Usa el ratón para arrastrar (pan) y haz scroll para hacer zoom</b> sobre los nodos.
  </p>

  <div id="diagram-container" style="background:var(--inset-bg);border:var(--bw) solid var(--border);border-radius:var(--radius);box-shadow:var(--shadow);flex:1;overflow:hidden;position:relative;cursor:grab;">
    <div id="zoom-wrapper" style="width:100%;height:100%;display:flex;align-items:center;justify-content:center;transform-origin:center center;transition:transform 0.1s ease-out;">
      <pre class="mermaid" style="background:transparent;">
graph LR
    A[GitHub Advanced Security] --> B[GitHub Code Security]
    A --> C[GitHub Secret Protection]
    A --> D[Funciones en todos los planes]

    B --> B1[Code scanning / CodeQL]
    B --> B2[CodeQL CLI]
    B --> B3[Copilot Autofix]
    B --> B4[AI-powered security detections]
    B --> B5[Dependency review]
    B --> B6[Custom auto-triage rules]
    B --> B7[Security campaigns - código]
    B --> B8[Security overview]

    C --> C1[Secret scanning]
    C --> C2[Push protection]
    C --> C3[AI-detected secrets]
    C --> C4[Custom patterns]
    C --> C5[Delegated bypass]
    C --> C6[Security campaigns - secretos]
    C --> C7[Security overview]

    D --> D1[Dependency graph]
    D --> D2[Dependabot alerts]
    D --> D3[Dependabot security updates]
    D --> D4[GitHub Advisory Database]
    D --> D5[Private vulnerability reporting]
    D --> D6[Artifact attestations]
      </pre>
    </div>
  </div>
</div>

<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  const t = k => getComputedStyle(document.documentElement).getPropertyValue(k).trim();
  mermaid.initialize({
    startOnLoad: true,
    theme: 'base',
    themeVariables: {
      primaryColor: t('--mermaid-primary'),
      primaryTextColor: t('--mermaid-text'),
      primaryBorderColor: t('--mermaid-border'),
      lineColor: t('--mermaid-line'),
      secondaryColor: t('--mermaid-secondary'),
      tertiaryColor: t('--mermaid-tertiary'),
      fontFamily: t('--body'),
      fontSize: '16px'
    }
  });

  // Vanilla JS Pan & Zoom
  const container = document.getElementById('diagram-container');
  const wrapper = document.getElementById('zoom-wrapper');
  
  let scale = 1;
  let isDragging = false;
  let startX, startY, translateX = 0, translateY = 0;

  container.addEventListener('wheel', (e) => {
    e.preventDefault();
    const zoomFactor = 0.1;
    if (e.deltaY < 0) scale += zoomFactor;
    else scale -= zoomFactor;
    scale = Math.min(Math.max(0.5, scale), 4); // clamp between 0.5x and 4x
    updateTransform();
  });

  container.addEventListener('mousedown', (e) => {
    isDragging = true;
    container.style.cursor = 'grabbing';
    startX = e.clientX - translateX;
    startY = e.clientY - translateY;
  });

  container.addEventListener('mousemove', (e) => {
    if (!isDragging) return;
    translateX = e.clientX - startX;
    translateY = e.clientY - startY;
    updateTransform();
  });

  window.addEventListener('mouseup', () => {
    isDragging = false;
    container.style.cursor = 'grab';
  });

  function updateTransform() {
    wrapper.style.transform = `translate(${translateX}px, ${translateY}px) scale(${scale})`;
  }
</script>
"""

# Replace the specific slide with html_content
for slide in plan['slides']:
    if slide.get('title') == 'Ecosistema GHAS':
        # Remove archetype and slots
        slide.pop('archetype', None)
        slide.pop('slots', None)
        slide['html_content'] = html_slide

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(plan, f, indent=2, ensure_ascii=False)
