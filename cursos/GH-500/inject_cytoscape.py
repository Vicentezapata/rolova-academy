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
    Haz <b>clic en un nodo</b> para expandir o colapsar la rama. Usa los botones superiores para controlar la vista completa.
  </p>

  <div id="cy-container" style="flex:1; position:relative; border-radius:var(--radius); border:var(--bw) solid var(--border); background:var(--inset-bg); overflow:hidden; box-shadow:var(--shadow);">
    <div id="cy" style="width:100%; height:100%; position:absolute; inset:0;"></div>
  </div>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.23.0/cytoscape.min.js"></script>
<script src="https://unpkg.com/dagre@0.8.5/dist/dagre.min.js"></script>
<script src="https://unpkg.com/cytoscape-dagre@2.4.0/cytoscape-dagre.js"></script>

<script type="module">
  function initCyDiagram() {
    var container = document.getElementById('cy');
    if (!container) return;

    const t = k => getComputedStyle(document.documentElement).getPropertyValue(k).trim();
    const cBg = t('--card-bg') || '#1a1a1a';
    const cText = t('--text') || '#ffffff';
    const cBorder = t('--border') || '#333333';
    const cA1 = t('--a1') || '#ff5555';
    const cA2 = t('--a2') || '#55ff55';
    const cA3 = t('--a3') || '#5555ff';

    var rawData = [
      { id: 'root', text: 'GitHub Advanced Security', parent: null, type: 'root' },
      
      { id: 'code_sec', text: 'Code Security', parent: 'root', type: 'branch', color: cA1 },
      { id: 'cs1', text: 'Code scanning / CodeQL', parent: 'code_sec', type: 'leaf', color: cA1 },
      { id: 'cs2', text: 'CodeQL CLI', parent: 'code_sec', type: 'leaf', color: cA1 },
      { id: 'cs3', text: 'Copilot Autofix', parent: 'code_sec', type: 'leaf', color: cA1 },
      { id: 'cs4', text: 'AI-powered security detections', parent: 'code_sec', type: 'leaf', color: cA1 },
      { id: 'cs5', text: 'Dependency review', parent: 'code_sec', type: 'leaf', color: cA1 },
      { id: 'cs6', text: 'Custom auto-triage rules', parent: 'code_sec', type: 'leaf', color: cA1 },
      { id: 'cs7', text: 'Security campaigns - código', parent: 'code_sec', type: 'leaf', color: cA1 },
      { id: 'cs8', text: 'Security overview', parent: 'code_sec', type: 'leaf', color: cA1 },

      { id: 'secret_sec', text: 'Secret Protection', parent: 'root', type: 'branch', color: cA2 },
      { id: 'sp1', text: 'Secret scanning', parent: 'secret_sec', type: 'leaf', color: cA2 },
      { id: 'sp2', text: 'Push protection', parent: 'secret_sec', type: 'leaf', color: cA2 },
      { id: 'sp3', text: 'AI-detected secrets', parent: 'secret_sec', type: 'leaf', color: cA2 },
      { id: 'sp4', text: 'Custom patterns', parent: 'secret_sec', type: 'leaf', color: cA2 },
      { id: 'sp5', text: 'Delegated bypass', parent: 'secret_sec', type: 'leaf', color: cA2 },
      { id: 'sp6', text: 'Security campaigns - secretos', parent: 'secret_sec', type: 'leaf', color: cA2 },
      { id: 'sp7', text: 'Security overview (secretos)', parent: 'secret_sec', type: 'leaf', color: cA2 },

      { id: 'free_sec', text: 'Planes Gratuitos', parent: 'root', type: 'branch', color: cA3 },
      { id: 'fs1', text: 'Dependency graph', parent: 'free_sec', type: 'leaf', color: cA3 },
      { id: 'fs2', text: 'Dependabot alerts', parent: 'free_sec', type: 'leaf', color: cA3 },
      { id: 'fs3', text: 'Dependabot security updates', parent: 'free_sec', type: 'leaf', color: cA3 },
      { id: 'fs4', text: 'GitHub Advisory Database', parent: 'free_sec', type: 'leaf', color: cA3 },
      { id: 'fs5', text: 'Private vulnerability reporting', parent: 'free_sec', type: 'leaf', color: cA3 },
      { id: 'fs6', text: 'Artifact attestations', parent: 'free_sec', type: 'leaf', color: cA3 }
    ];

    var elements = [];
    rawData.forEach(function(item) {
      elements.push({ group: 'nodes', data: { id: item.id, label: item.text, type: item.type, bgColor: item.color || cBg } });
      if (item.parent) {
        elements.push({ group: 'edges', data: { source: item.parent, target: item.id } });
      }
    });

    var cy = cytoscape({
      container: container,
      elements: elements,
      style: [
        { selector: 'node', style: {
          'background-color': cBg,
          'color': cText,
          'border-width': '1px',
          'border-color': cBorder,
          'label': 'data(label)',
          'text-valign': 'center',
          'text-halign': 'center',
          'font-family': 'Inter, sans-serif',
          'font-size': '12px',
          'shape': 'round-rectangle',
          'width': 'label',
          'height': 'label',
          'padding': '10px'
        }},
        { selector: 'node[type="root"]', style: {
          'font-size': '15px',
          'font-weight': 'bold',
          'border-width': '2px',
          'border-color': cText,
          'padding': '14px'
        }},
        { selector: 'node[type="branch"]', style: {
          'font-size': '14px',
          'font-weight': '600',
          'border-color': 'data(bgColor)',
          'border-width': '2px'
        }},
        { selector: 'node[type="leaf"]', style: {
          'font-size': '11px',
          'background-color': 'data(bgColor)',
          'color': '#000000',
          'border-width': '0px'
        }},
        { selector: 'edge', style: {
          'width': 1.5,
          'line-color': cBorder,
          'target-arrow-color': cBorder,
          'target-arrow-shape': 'triangle',
          'curve-style': 'bezier'
        }},
        { selector: ':selected', style: {
          'border-color': cText,
          'border-width': '3px'
        }}
      ],
      layout: { name: 'dagre', padding: 30, rankDir: 'LR', spacingFactor: 1.1, rankSep: 60, nodeSep: 20 },
      minZoom: 0.2, maxZoom: 2.5, boxSelectionEnabled: false
    });

    var childrenMap = {};
    rawData.forEach(function(item) {
      if (item.parent) {
        if (!childrenMap[item.parent]) childrenMap[item.parent] = [];
        childrenMap[item.parent].push(item.id);
      }
    });

    var collapsed = {};
    rawData.forEach(function(item) {
      if (childrenMap[item.id] && item.type !== 'root') {
        collapsed[item.id] = true;
      }
    });

    function applyVisibility() {
      var visible = { 'root': true, 'code_sec': true, 'secret_sec': true, 'free_sec': true };
      
      function walkVisible(nodeId) {
        var kids = childrenMap[nodeId] || [];
        kids.forEach(function(kidId) {
          if (!collapsed[nodeId]) {
            visible[kidId] = true;
            walkVisible(kidId);
          }
        });
      }
      walkVisible('root');

      cy.batch(function() {
        cy.nodes().forEach(function(n) {
          n.style('display', visible[n.id()] ? 'element' : 'none');
        });
        cy.edges().forEach(function(e) {
          var src = e.source().id();
          var tgt = e.target().id();
          e.style('display', (visible[src] && visible[tgt]) ? 'element' : 'none');
        });
        
        cy.nodes().forEach(function(n) {
          var nodeId = n.id();
          var item = rawData.find(d => d.id === nodeId);
          if (item && childrenMap[nodeId]) {
            var base = item.text;
            n.data('label', collapsed[nodeId] ? base + ' [+]' : base + ' [−]');
          }
        });
      });
    }

    applyVisibility();

    function reLayout() {
      cy.layout({
        name: 'dagre', padding: 30, rankDir: 'LR',
        spacingFactor: 1.1, rankSep: 60, nodeSep: 20,
        animate: true, animationDuration: 350, animationEasing: 'ease-out'
      }).run();
    }

    reLayout();

    function getDescendants(nodeId) {
      var desc = [];
      var kids = childrenMap[nodeId] || [];
      kids.forEach(function(kid) {
        desc.push(kid);
        desc = desc.concat(getDescendants(kid));
      });
      return desc;
    }

    cy.on('tap', 'node', function(evt) {
      var nodeId = evt.target.id();
      if (childrenMap[nodeId]) {
        if (collapsed[nodeId]) {
          collapsed[nodeId] = false;
        } else {
          collapsed[nodeId] = true;
          getDescendants(nodeId).forEach(function(descId) {
            if (childrenMap[descId]) collapsed[descId] = true;
          });
        }
        applyVisibility();
        reLayout();
      }
    });

    var btnContainer = document.createElement('div');
    btnContainer.style.cssText = 'position:absolute;top:15px;right:15px;z-index:10;display:flex;gap:10px;';
    btnContainer.innerHTML = `
      <button id="cy-expand" style="background:var(--card-bg);border:1px solid var(--border);color:var(--text);padding:8px 16px;border-radius:var(--radius-sm, 6px);cursor:pointer;font-family:var(--body);font-size:12px;font-weight:600;box-shadow:var(--shadow);">Expandir Todo</button>
      <button id="cy-collapse" style="background:var(--card-bg);border:1px solid var(--border);color:var(--text);padding:8px 16px;border-radius:var(--radius-sm, 6px);cursor:pointer;font-family:var(--body);font-size:12px;font-weight:600;box-shadow:var(--shadow);">Colapsar Todo</button>
    `;
    document.getElementById('cy-container').appendChild(btnContainer);

    document.getElementById('cy-expand').addEventListener('click', function(e) {
      e.stopPropagation();
      Object.keys(collapsed).forEach(k => collapsed[k] = false);
      applyVisibility();
      reLayout();
      cy.fit();
    });
    document.getElementById('cy-collapse').addEventListener('click', function(e) {
      e.stopPropagation();
      rawData.forEach(item => { if (childrenMap[item.id] && item.type !== 'root') collapsed[item.id] = true; });
      applyVisibility();
      reLayout();
      cy.fit();
    });
  }

  // Use setTimeout to ensure DOM is ready and CSS variables are computed
  setTimeout(initCyDiagram, 100);
</script>
"""

for slide in plan['slides']:
    if slide.get('title') == 'Ecosistema GHAS':
        slide['html_content'] = html_slide

with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(plan, f, indent=2, ensure_ascii=False)
