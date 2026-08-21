# Arsenal avanzado de CSS (W1-W12)

> El agente lee este archivo bajo demanda según las `decoration_hints` de cada página en el `visual_plan.json` (incluido el número W).
> En cada página solo se inyecta el código del arma al que se hace referencia, no la cantidad total. Las combinaciones de armas deberían ser diferentes en las páginas adyacentes.
> En la etapa de planificación, use el número W para hacer referencia al arma en `decoration_hints`: como `W1 texto degradado | use acento-1 → acento-2 135deg` para el título.

---

## W1. Relleno de texto degradado (para títulos/números principales)

```css
.gradient-text {
  background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
}
```**Aplicable**: título de la página, números de KPI principales, título principal de la portada. El impacto visual es mucho mayor que el del texto en color sólido.
**ADAPTAR**: ángulo de degradado 90-180 grados / combinación de colores acento-1 → acento-2 o acento-1 → acento-3 / usado para texto o datos_resaltado

---

## W1.5 Tipografía Editorial (Clases Auxiliares)

```css
/* Eyebrow: Etiqueta superior pre-título */
.eyebrow {
  display: inline-flex; align-items: center; gap: 8px;
  background: rgba(34,211,238,0.12); border: 1px solid rgba(34,211,238,0.35);
  color: var(--accent-1); padding: 8px 18px; border-radius: 999px;
  font-size: 11px; font-weight: 700; letter-spacing: 0.18em; text-transform: uppercase;
  margin-bottom: 28px; width: fit-content;
}
.eyebrow .dot {
  width: 6px; height: 6px; border-radius: 50%;
  background: var(--accent-1); animation: pulse 2s ease-in-out infinite;
}

/* Meta-chips: Etiquetas de metadatos o tags */
.meta-chip {
  background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12);
  padding: 7px 16px; border-radius: 6px; font-size: 12px;
  color: var(--text-secondary); letter-spacing: 0.05em;
  font-family: var(--mono-font);
}
.meta-chip.accent {
  background: rgba(99,102,241,0.2); border-color: rgba(99,102,241,0.4); color: var(--accent-2);
}
```
**Aplicable**: Subtítulos de sección, tags de metadata, indicadores de estado, números de slide. Reemplaza el texto plano por micro-componentes altamente estilizados.

## W2. corte geométrico con ruta de clip (para tarjetas/bloques de colores)

```css
/* 底部斜切 -- 制造"撕裂"动感 */
.card-sliced { clip-path: polygon(0 0, 100% 0, 100% 88%, 0 100%); }
/* 左侧斜入 -- 制造"侵入"感 */
.card-invade { clip-path: polygon(5% 0, 100% 0, 100% 100%, 0 100%); }
/* 菱形裁切 -- 装饰元素用 */
.diamond { clip-path: polygon(50% 0, 100% 50%, 50% 100%, 0 50%); }
```**Aplicable**: tarjetas de soluciones recomendadas en la página de comparación, bloques de colores decorativos en las portadas de los capítulos y cintas decorativas.
**ADAPTAR**: Ángulo de bisel/dirección de corte (abajo/izquierda/derecha/diagonal)/relación de corte 80%-95%

---

## W3. máscara-imagen máscara de perforación (para capa de atmósfera)

```css
.mask-spotlight {
  background: var(--bg-primary);
  mask-image: radial-gradient(ellipse 300px 250px at 65% 40%, transparent 100%, black 101%);
  -webkit-mask-image: radial-gradient(ellipse 300px 250px at 65% 40%, transparent 100%, black 101%);
}
```**Aplicable**: efecto de foco para portada/página final, perforación de enfoque para página de datos.
**ADAPTAR**: Tamaño de elipse 200-500 px/posición de enfoque/dirección (ablación radial/lineal)

---

## W4. gradiente cónico-gradiente gradiente de cono (para gráfico de anillos/progreso)

```css
.ring-progress {
  width: 80px; height: 80px; border-radius: 50%;
  background: conic-gradient(var(--accent-1) 0% 20%, rgba(255,255,255,0.08) 20% 100%);
  mask: radial-gradient(circle 28px, transparent 100%, black 101%);
  -webkit-mask: radial-gradient(circle 28px, transparent 100%, black 101%);
}
```**Aplicable**: Visualización de porcentaje, indicador de calificación en tarjeta de datos.
**ADAPTAR**: Ancho del anillo (radio del círculo de la máscara) / porcentaje de relleno / color

---

## W5. filtro de fondo de vidrio esmerilado (para vidrio estilo tarjeta)

```css
.card-glass {
  background: rgba(255,255,255,0.03);
  backdrop-filter: blur(16px) saturate(180%);
  -webkit-backdrop-filter: blur(16px) saturate(180%);
  border: 1px solid rgba(255,255,255,0.06);
}
```**Aplicable**: superposiciones de texto en páginas de imágenes, tarjetas de información en portadas/finales.
**ADAPTAR**: desenfoque 8-24px / saturar 120-200% / transparencia de fondo 0,02-0,08

---

## W6. mix-blend-mode Modo de Fusión (Para Marcas de Agua/Superposiciones)

```css
.watermark-blend {
  mix-blend-mode: overlay; /* 或 soft-light / screen */
  color: var(--accent-1);
  opacity: 0.06;
}
```
**Aplicable**: Texto grande decorativo, imágenes de fondo superpuestas. Crea un efecto integrado y moderno en lugar de simplemente bajar la opacidad.
**ADAPTAR**: Modo de fusión (`overlay` / `multiply` / `screen` / `soft-light`), opacidad 0.05-0.15.

---

## W7. sombra multicapa box-shadow (para tarjetas elevadas)

```css
.card-elevated {
  box-shadow:
    0 1px 2px rgba(0,0,0,0.1),
    0 4px 8px rgba(0,0,0,0.08),
    0 12px 24px rgba(0,0,0,0.12),
    0 24px 48px rgba(0,0,0,0.06);
  transform: translateY(-4px);
}
/* accent 卡片的发光阴影 */
.card-accent-glow {
  box-shadow:
    0 4px 12px rgba(245,197,24,0.15),
    0 12px 32px rgba(245,197,24,0.1),
    inset 0 1px 0 rgba(255,255,255,0.15);
}
```**Aplica**: tarjetas elevadas/acento por página. 4 capas de sombra proporcionan 5 veces más textura que 1 capa de sombra.
**ADAPTAR**: Número de capas de sombra 2-4 / dirección de desplazamiento / color luminoso acentuado siguiendo el fortalecimiento o debilitamiento del fondo variable / oscuro

---

## W8. Uso avanzado de pseudoelementos (decoración/marcado/superposición)

```css
/* 卡片左上角的分类角标 */
.card::before {
  content: attr(data-label);
  position: absolute; top: -1px; left: 16px;
  font-size: 10px; font-weight: 700; letter-spacing: 1px;
  background: var(--accent-1); color: var(--bg-primary);
  padding: 2px 10px; border-radius: 0 0 6px 6px;
}
/* 引用标记的大引号 */
.quote-card::before {
  content: '\201C';
  position: absolute; top: -12px; left: 16px;
  font-size: 80px; line-height: 1; color: var(--accent-1);
  opacity: 0.15; font-family: Georgia, serif;
}
/* 卡片底部的渐隐分隔线 */
.card::after {
  content: '';
  position: absolute; bottom: 0; left: 10%; right: 10%;
  height: 1px;
  background: linear-gradient(90deg, transparent, var(--accent-1), transparent);
  opacity: 0.2;
}
```**Aplicable**: marcadores de esquina, decoraciones con citas, divisores delicados, formas geométricas decorativas.
**ADAPTAR**: Uso de pseudoelementos (subíndice/comillas/separador/forma)/posición/color/transparencia

---

## W9. Técnicas de estructura espacial (dejar que el propio espacio narre)

> Actúa sobre la forma y posición de la tarjeta/elemento, no sobre detalles decorativos. Romper fundamentalmente la estructura mediocre de "cajas rectangulares dispuestas en una cuadrícula".

```css
/* 9a. 数字脱框——核心数据裸露在空间中，不在任何卡片容器内 */
.hero-number-naked {
  position: absolute;
  top: 100px; left: 60px;
  font-size: 120px; font-weight: 900;
  color: var(--accent-1);
  line-height: 0.85;
  text-shadow: 0 0 80px rgba(245,197,24,0.12);
  z-index: 4;
  /* 没有 background、没有 padding、没有 border-radius -- 数字裸露 */
}

/* 9b. 卡片斜切——clip-path 制造非矩形边缘 */
.card-slash-bottom { clip-path: polygon(0 0, 100% 0, 100% 88%, 0 100%); }
.card-slash-left { clip-path: polygon(6% 0, 100% 0, 100% 100%, 0 100%); }

/* 9c. 出血色带——冲出画布两侧边缘 */
.bleed-band {
  position: absolute;
  left: -40px; right: -40px;
  height: 64px;
  background: linear-gradient(135deg, var(--accent-1), var(--accent-2));
  clip-path: polygon(2% 0, 100% 20%, 98% 100%, 0 80%);
}

/* 9d. 消融边缘——卡片一侧渐隐消失而非硬切 */
.card-fade-right {
  mask-image: linear-gradient(90deg, black 60%, transparent 100%);
  -webkit-mask-image: linear-gradient(90deg, black 60%, transparent 100%);
}

/* 9e. 装饰做减法——一个大几何形状取代 N 个小点缀 */
.deco-mega-circle {
  position: absolute;
  top: -100px; right: -80px;
  width: 500px; height: 500px;
  border-radius: 50%;
  background: radial-gradient(circle, var(--accent-1), transparent 70%);
  opacity: 0.05; z-index: 1;
}
```**Aplicable**:
- **9a Número fuera del marco**: página con KPI principales
- **9b-9d Bisel/Sangrado/Ablación**: al menos 1 elemento no rectangular cada 3-4 páginas
- **9e Resta de decoración**: más de 5 decoraciones pequeñas → cambiar a 1 forma geométrica grande
**ADAPTAR**: Combinación gratuita de subtécnicas / Tamaño de fuente del número fuera del marco 80-160 px / Ángulo de bisel / Volumen de sangrado -20 ~ -60 px / Dirección de ablación

---

## W10. Material de la superficie (haga que la imagen sea táctil)

> Añade textura táctil a los elementos planos (ruido SVG, líneas de escaneo, neumorfismo), aumentando dramáticamente la sofisticación del diseño.

```css
/* 10a. SVG 噪声纹理——宣纸/磨砂/胶片颗粒感 */
.texture-grain {
  background-image: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" width="200" height="200"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency="0.8" numOctaves="4" stitchTiles="stitch"/></filter><rect width="200" height="200" filter="url(%23n)" opacity="0.08"/></svg>');
  /* baseFrequency: 0.3=粗砂岩 / 0.8=细宣纸 / 1.5=胶片颗粒 */
  /* opacity: 0.04-0.12 */
}

/* 10b. 扫描线——CRT 显示器 / 仪表盘 */
.texture-scanlines::after {
  content: '';
  position: absolute; inset: 0;
  background: repeating-linear-gradient(0deg, transparent 0, rgba(0,0,0,0.15) 1px, transparent 2px);
  background-size: 100% 3px;
  opacity: 0.3; pointer-events: none; z-index: 1;
}

/* 10c. 拟态凹凸——从平面中压出/凸起形状 */
.neumorphic-raised {
  background: var(--bg-secondary); border-radius: 16px;
  box-shadow: 6px 6px 12px rgba(0,0,0,0.12), -6px -6px 12px rgba(255,255,255,0.08);
}
.neumorphic-inset {
  background: var(--bg-secondary); border-radius: 16px;
  box-shadow: inset 4px 4px 8px rgba(0,0,0,0.1), inset -4px -4px 8px rgba(255,255,255,0.06);
}
```**Aplicable**: 10a cultura/académico/marcas de alta gama/10b tecnología/datos/monitoreo/10c diseño minimalista añade un sutil eje Z
**ADAPTAR**: Selección del tipo de material/espesor de control de frecuencia base/densidad de la línea de escaneo/dirección e intensidad cóncava y convexa

---

## W11. Marcos HUD / Esquinas de Interfaz (Para Estilo Tecnológico/Cyber)

```css
.hud-frame::before,
.hud-frame::after {
  content: '';
  position: absolute;
  width: 28px; height: 28px;
  border-color: var(--accent-1);
  border-style: solid;
  opacity: 0.4; z-index: 2;
}
.hud-frame::before {
  top: 20px; left: 20px;
  border-width: 2px 0 0 2px; /* 左上角 */
}
.hud-frame::after {
  bottom: 20px; right: 20px;
  border-width: 0 2px 2px 0; /* 右下角 */
}
```**Aplicable**: portada, página del panel de datos, página de conclusión. El grosor/color/virtual y sólido de las líneas de las esquinas siguen el ADN del estilo.
**ADAPTAR**: Tamaño de esquina 20-40 px / Ancho de línea 1-3 px / Línea discontinua versus línea sólida / El color sigue el acento / 2 esquinas versus 4 esquinas / Agregar arco de radio de borde

---

## W12. Pie de página narrativo (dejar que los elementos funcionales participen en la historia)

> Un número de página no es sólo un número, puede ser parte de la narrativa.

```css
/* 12a. 终端状态栏 -- 科技/数据主题 */
.footer-terminal {
  position: absolute; bottom: 20px; left: 24px;
  font-size: 11px; font-family: 'Courier New', monospace;
  color: var(--accent-1); opacity: 0.6; letter-spacing: 1px;
  /* 内容：STATUS: ACTIVE | SECTION: 02 | PAGE: 03/12 */
}

/* 12b. 印章/徽记 -- 国风/文化/正式场合 */
.footer-seal {
  position: absolute; bottom: 24px; right: 32px;
  width: 56px; height: 24px;
  background: var(--accent-1); color: var(--bg-primary);
  font-size: 12px; font-weight: 700;
  display: flex; align-items: center; justify-content: center;
  border: 1px solid var(--accent-2); border-radius: 2px; opacity: 0.8;
}

/* 12c. 刻度尺/进度条 -- 流程/时间线主题 */
.footer-progress {
  position: absolute; bottom: 0; left: 0; right: 0; height: 3px;
  background: var(--bg-secondary);
}
.footer-progress::after {
  content: '';
  position: absolute; left: 0; top: 0; height: 100%;
  width: calc(var(--progress, 25) * 1%);
  background: linear-gradient(90deg, var(--accent-1), var(--accent-2));
}
```**Aplica**: seleccione libremente la personalidad del pie de página según `design_soul`. Transforme los números de página de "esquinas destacadas" a "toques finales de diseño".
**ADAPTAR**: Tipo de pie de página (terminal/sello/barra de progreso)/posición/formato de contenido/color sigue el acento