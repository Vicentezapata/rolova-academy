/* ============================================================
   RUNTIME COMPARTIDO — idéntico en todas las slides.
   El renderer lo inyecta al final del BODY, igual que _base.css
   se inyecta en SHARED_CSS.

   REGLA: aquí no puede haber literales de color. Los colores se
   leen en tiempo de ejecución desde los tokens del frame.
   ============================================================ */
(function () {
  var LORDICON_ID = /^[a-z0-9]{8}$/;

  function token(el, name) {
    return getComputedStyle(el).getPropertyValue(name).trim();
  }

  /* 1 · ICONOS
     El agente escribe en el slot un emoji, un carácter o un ID de Lordicon.
     Si es un ID de 8 caracteres se sustituye por <lord-icon> coloreado con
     los tokens del pack. Cualquier otra cosa se deja como texto. */
  Array.prototype.forEach.call(document.querySelectorAll('[data-icon]'), function (el) {
    var id = (el.dataset.icon || '').trim();
    if (!LORDICON_ID.test(id)) return;
    var size = el.dataset.iconSize || '34';
    var ico = document.createElement('lord-icon');
    ico.setAttribute('src', 'https://cdn.lordicon.com/' + id + '.json');
    ico.setAttribute('trigger', el.dataset.iconTrigger || 'loop');
    ico.setAttribute('delay', '1600');
    ico.setAttribute('colors', 'primary:' + token(el, '--a1') + ',secondary:' + token(el, '--a2'));
    ico.style.width = size + 'px';
    ico.style.height = size + 'px';
    el.textContent = '';
    el.classList.add('is-lottie');
    el.appendChild(ico);
  });

  /* 2 · GRÁFICOS
     El agente entrega valores crudos, nunca porcentajes. Aquí se normalizan
     a la variable --n (0..1) que cada arquetipo usa como altura, anchura o
     ángulo. data-chart="pct" normaliza contra 100; el resto, contra el máximo
     de la propia serie. */
  Array.prototype.forEach.call(document.querySelectorAll('[data-chart]'), function (chart) {
    var items = Array.prototype.slice.call(chart.querySelectorAll('[data-value]'));
    if (!items.length) return;

    var vals = items.map(function (el) { return parseFloat(el.dataset.value) || 0; });
    var max = chart.dataset.chart === 'pct'
      ? 100
      : Math.max.apply(null, vals.concat([0]));
    if (!(max > 0)) max = 1;

    items.forEach(function (el, i) {
      el.style.setProperty('--n', (vals[i] / max).toFixed(4));
    });

    /* Serie de línea: el trazado se calcula con los mismos valores, así el
       agente nunca escribe coordenadas SVG. */
    var line = chart.querySelector('[data-line]');
    if (!line || vals.length < 2) return;

    var svg = line.ownerSVGElement;
    var box = (svg.getAttribute('viewBox') || '0 0 100 100').split(/\s+/);
    var W = parseFloat(box[2]);
    var H = parseFloat(box[3]);
    var pad = H * 0.1;
    var step = W / (vals.length - 1);

    var pts = vals.map(function (v, i) {
      var y = H - pad - (v / max) * (H - pad * 2);
      return (i * step).toFixed(2) + ',' + y.toFixed(2);
    });

    line.setAttribute('points', pts.join(' '));

    var area = chart.querySelector('[data-area]');
    if (area) area.setAttribute('points', '0,' + H + ' ' + pts.join(' ') + ' ' + W + ',' + H);

    var dots = chart.querySelector('[data-dots]');
    if (dots) {
      pts.forEach(function (p) {
        var xy = p.split(',');
        var c = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
        c.setAttribute('cx', xy[0]);
        c.setAttribute('cy', xy[1]);
        c.setAttribute('r', (H * 0.035).toFixed(2));
        dots.appendChild(c);
      });
    }
  });

  /* 3 · MINI-SERIES
     Para paneles pequeños el agente escribe una sola cadena de texto:
       data-series="Unitarias:120|Integración:45|E2E:12"
     y el tipo de gráfico en data-kind (bars | donut | stack | spark).
     Aquí se parsea y se construye el DOM; el agente nunca escribe HTML. */
  var RAMP = ['--a1', '--a2', '--a3', '--ok', '--warn'];

  function parseSeries(raw) {
    return (raw || '').split('|').filter(Boolean).map(function (part) {
      var cut = part.lastIndexOf(':');
      return {
        label: part.slice(0, cut).trim(),
        value: parseFloat(part.slice(cut + 1)) || 0
      };
    });
  }

  function el(tag, cls, parent) {
    var node = document.createElement(tag);
    if (cls) node.className = cls;
    if (parent) parent.appendChild(node);
    return node;
  }

  Array.prototype.forEach.call(document.querySelectorAll('[data-series]'), function (host) {
    var data = parseSeries(host.dataset.series);
    if (!data.length) return;

    var kind = host.dataset.kind || 'bars';
    var total = data.reduce(function (a, d) { return a + d.value; }, 0) || 1;
    var max = Math.max.apply(null, data.map(function (d) { return d.value; }).concat([0])) || 1;
    host.textContent = '';

    if (kind === 'donut') {
      var stops = [];
      var acc = 0;
      data.forEach(function (d, i) {
        var from = (acc / total) * 100;
        acc += d.value;
        var to = (acc / total) * 100;
        stops.push('var(' + RAMP[i % RAMP.length] + ') ' + from.toFixed(2) + '% ' + to.toFixed(2) + '%');
      });
      var ring = el('div', 'ms-donut', host);
      ring.style.setProperty('--ms-ring', 'conic-gradient(' + stops.join(',') + ')');
      var hole = el('div', 'ms-hole', ring);
      hole.textContent = host.dataset.center || data.length;

    } else if (kind === 'stack') {
      var bar = el('div', 'ms-stack', host);
      data.forEach(function (d, i) {
        var seg = el('span', 'ms-seg', bar);
        seg.style.flexGrow = String(d.value);
        seg.style.background = 'var(' + RAMP[i % RAMP.length] + ')';
        seg.title = d.label + ': ' + d.value;
      });

    } else if (kind === 'spark') {
      var svg = document.createElementNS('http://www.w3.org/2000/svg', 'svg');
      svg.setAttribute('viewBox', '0 0 100 34');
      svg.setAttribute('preserveAspectRatio', 'none');
      svg.setAttribute('class', 'ms-spark');
      var poly = document.createElementNS('http://www.w3.org/2000/svg', 'polyline');
      var stp = 100 / (data.length - 1 || 1);
      poly.setAttribute('points', data.map(function (d, i) {
        return (i * stp).toFixed(1) + ',' + (32 - (d.value / max) * 28).toFixed(1);
      }).join(' '));
      poly.setAttribute('vector-effect', 'non-scaling-stroke');
      svg.appendChild(poly);
      host.appendChild(svg);

    } else {
      var cols = el('div', 'ms-bars', host);
      data.forEach(function (d) {
        var col = el('span', 'ms-col', cols);
        var track = el('span', 'ms-track', col);
        el('i', null, track).style.height = ((d.value / max) * 100).toFixed(1) + '%';
        el('u', null, col).textContent = d.label;
      });
    }

    /* La leyenda solo tiene sentido cuando cada color es una categoría. */
    if (kind !== 'donut' && kind !== 'stack') return;

    var scope = host.closest('[data-legend-scope]') || host.parentNode;
    var legend = scope ? scope.querySelector('[data-legend]') : null;
    if (legend) {
      legend.textContent = '';
      data.forEach(function (d, i) {
        var item = el('span', 'legend-item', legend);
        var key = el('i', 'legend-key', item);
        key.style.background = 'var(' + RAMP[i % RAMP.length] + ')';
        el('span', null, item).textContent = d.label + ' · ' + d.value;
      });
    }
  });
})();
