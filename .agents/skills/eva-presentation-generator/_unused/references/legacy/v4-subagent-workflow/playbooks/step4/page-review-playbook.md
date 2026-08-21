# Revisión visual de página y libro de estrategias de reparación: revisión de imágenes de una sola página y reparación de HTML

## Objetivo

Después de tomar la captura de pantalla, cambié a la identidad dual de **arquitecto front-end sénior estricto a nivel de píxel + director de diseño de interfaz de usuario**, verifiqué el PNG área por área de acuerdo con el protocolo de escaneo estructurado e inmediatamente localicé la causa raíz HTML/CSS del problema y lo reparé yo mismo hasta que la página alcanzó los estándares de entrega.

**Principio básico: mire la imagen para hablar, cambie el código para verificar. Sin conjeturas, sin suposiciones, sin dejar ir verbalmente. **

---

## Parte A-0: Protocolo de archivo de capturas de pantalla (obligatorio en cada ronda, no omitir)

> **Por qué necesitas esto**: LLM es propenso a la ilusión de "lo he arreglado". El archivo físico + la comparación del antes y el después son los únicos medios fiables de verificación.

### Reglas de archivo

Cada ronda de capturas de pantalla debe guardarse en dos ubicaciones al mismo tiempo:

1. **最终位置**（供 FINALIZE 使用）：`PNG_OUTPUT`（任务包中的截图输出路径）
2. **轮次存档**（供对比追溯）：`REVIEW_DIR/roundX/slide-N.png`（任务包中的审查存档目录）

截图命令（每轮固定两步，路径取自任务包）：

```bash
# Step A-0-1：截图到最终位置
python3 SKILL_DIR/scripts/html2png.py SLIDE_OUTPUT -o $(dirname PNG_OUTPUT) --scale 0.75

# Step A-0-2：归档到轮次目录（X = 当前轮次编号）
mkdir -p REVIEW_DIR/roundX
cp PNG_OUTPUT REVIEW_DIR/roundX/slide-N.png
```

### Reglas de validación (aplicadas desde la ronda 2 en adelante)

A partir de la Ronda 2, mira solo las capturas de pantalla más recientes de esta ronda:
1. **No lea la primera ronda de imágenes ni la anterior**, solo necesita usar las capacidades de visualización de imágenes disponibles en el host actual para ver `REVIEW_DIR/roundX/slide-N.png`.
2. **Verifique** todos los elementos `[Descubrimiento]` en la ronda anterior de informes elemento por elemento y confirme** si cada elemento está realmente reparado en la **nueva captura de pantalla.
3. Si descubre que efectivamente ha cambiado el HTML, pero la nueva captura de pantalla no tiene cambios, verifique la prioridad de CSS o intente guardar nuevamente.

**Comportamiento prohibido**:
- Está prohibido afirmar que la reparación ha sido superada sin realizar una captura de pantalla.
- Está prohibido inferir cómo debería verse la captura de pantalla basándose en la modificación del código (se deben observar los últimos píxeles de la captura de pantalla)

---

## Parte A: Protocolo de escaneo visual (debe ejecutarse después de cada ronda de capturas de pantalla)

不要泛泛地"看一眼截图"。按以下物理路径系统扫描，每个区域用一句话记录观察：

Antes de comenzar los tres escaneos, realice 4 verificaciones de contrato con `density_contract` en `planning`:
- Si la cantidad de tarjetas y gráficos en la página actual excede el presupuesto
- Si el texto del cuerpo es significativamente más pequeño que `min_body_font_px`
- ¿HTML rompe secretamente `image_policy`?
- Si `decoration_budget` se ve interrumpido por grandes marcas de agua, efectos de iluminación intensos o texturas excesivas.

### Pase 1: Patrulla Fronteriza (de afuera hacia adentro)

| Área de escaneo | Qué mirar | Preguntas típicas |
|--------|--------|---------|
| **Cuatro Esquinas** | ¿Está truncado el contenido? ¿Hay espacios en blanco inesperados o elementos sobrantes en las esquinas? | La tarjeta desborda el lienzo y la colocación de los elementos decorativos se compensa.
| **Cuatro Lados** | ¿El bloque de texto/color encaja perfectamente en el borde de 1280x720 (relleno <30px)? ¿Hay algún contenido en la parte inferior que sea devorado por overflow:hidden? | El acolchado exterior es insuficiente y el contenido se corta por exceso de altura |
| **Área de pie de página (40 píxeles inferiores)** | ¿Existe el número de página? ¿Se superpone con el contenido? | Conflicto de índice z, pie de página cubierto por tarjeta |

### Paso 2: Escaneo profundo del área de contenido (de primario a secundario)

| Área de escaneo | Qué mirar | Preguntas típicas |
|--------|--------|---------|
| **Área de título (40~100px superiores)** | ¿El texto del título es claro y legible? ¿El tamaño de la fuente se destaca del texto? ¿Hay alguna cubierta decorativa? | Contraste insuficiente, conflicto del índice z |
| **Área de enfoque (posición especificada de focus_zone)** | ¿Es el primer punto visual de la página completa? ¿Hay suficientes ventajas de tamaño/color/contraste? | el peso visual de la tarjeta primaria no es suficiente |
| **Área de soporte (tarjetas fuera del foco)** | ¿El contenido es completo y legible? ¿Las tarjetas están espaciadas uniformemente? ¿Existe alguna superposición seria? | El cuerpo del texto está truncado, los espacios son desiguales y el texto está comprimido y bloqueado |
| **Superposición de cascada y composición tipográfica (investigación especial)** | **Superposición causada por posicionamiento absoluto o falla de flexión/cuadrícula, superposición y confusión de imágenes y texto** | Los contenedores no se pueden colocar correctamente, el índice z está desordenado y las restricciones de alto y ancho son demasiado altas |
| **Principios de diseño de imágenes y texto e inspección especial de imágenes** | Según los "Principios de diseño avanzados", ¿las imágenes son elegantes y conformes? ¿La imagen está dañada, agrietada o exprimida y deformada? ¿Hay algún conflicto de capas con las cartas circundantes? | La ruta `src` es incorrecta, `object-fit: cover` no se agrega, entra en conflicto con el color principal o se convierte en un bloque de color de baja calidad |
| **Capa de decoración** | ¿Están SVG/Geometría/Degradados debajo del contenido? ¿Está acaparando la atención? | El índice z es demasiado alto, la opacidad es demasiado grande, el área es demasiado grande |

### Paso 3: Impresión general (da un paso atrás y mira)

| Consultar artículos | Criterios de juicio |
|--------|---------|
| **Prueba de enfoque de un segundo** | Cierra los ojos y mira de nuevo. ¿Lo primero que notas es la información más importante en esta página? |
| **Prueba de la habitación de ladrillos** | ¿Parece una presentación bien diseñada o una página HTML predeterminada? |
| **Consistencia de estilo** | ¿Los colores y las decoraciones coinciden con el ambiente descrito por `design_soul`? |
| **Distinción de páginas adyacentes** | ¿Las proporciones del diseño/bloque de color son significativamente diferentes a las de la página anterior? (Necesita recordar o comparar) |

---

## Parte B: Clasificación de gravedad (determina la prioridad de reparación)

Una vez descubiertos los problemas, se clasifican según su gravedad. **Si falla P0, fallará toda la página. Primero se debe reparar P0 y luego procesar P1/P2. **

### P0 — Defecto fatal (cualquiera existe → no pasa esta ronda)

| identificación | Síntomas | Diagnóstico de causa raíz | Recetas de reparación de CSS |
|----|------|---------|-------------|
| P0-1 | El contenido excede el lienzo y se recorta (las marcas de truncamiento son visibles en la parte inferior/derecha) | El cuerpo no tiene 1280x720 o el área de contenido excede la altura disponible de 580px | Verifique la declaración del "cuerpo"; agregue `altura máxima: 580 px; desbordamiento: oculto` al contenedor de contenido; reducir el tamaño de fuente o eliminar contenido no principal |
| P0-2 | Hay un truco de escalado scale() (la página parece estar reducida) | `transformar: escala(0.x)` existe | Elimine todo `transform: scale` y vuelva a calcular todos los tamaños a 1280x720 |
| P0-3 | Gran área en blanco (más del 40% del área del lienzo sin ningún contenido ni decoración) | El contenido de planificación no está en el terreno y el área de CSS Grid no está llena | Verifique las tarjetas una por una con `planning{n}.json` y complete las tarjetas que faltan; el área vacía de la cuadrícula al menos está llena de decoraciones |
| P0-4 | El texto principal es completamente ilegible (texto blanco sobre fondo blanco, texto negro sobre fondo negro, tamaño de fuente <10px) | Relación de contraste < 2:1 o el tamaño de fuente es demasiado pequeño | Utilice variables CSS opuestas para el color del texto; tamaño mínimo de texto de 14px; agregue una máscara semitransparente si es necesario `fondo: rgba(0,0,0,0.5)` |
| P0-5 | La tarjeta clave en la planificación falta por completo en el HTML | Olvidé escribir o comentar | Compare tarjetas de planificación[] para completar el HTML completo de la tarjeta que falta |
| P0-6 | **Gran superposición y desalineación tipográfica (el texto se aprieta entre sí, las tarjetas se bloquean fuera de orden e interrumpen la lectura)** | Desplazamiento de posicionamiento absoluto (`posición:absoluta`), uso excesivo de `margen` o `traducir`, desbordamiento del área de la cuadrícula | Vuelva a verificar la estructura Flex/Grid, elimine el atributo de desplazamiento no válido; proporcione al contenedor suficiente espacio en blanco interno, repare el contexto en cascada (`z-index`) |
| P0-7 | **La representación a nivel de píxel está rota (la parte inferior/borde del texto está cortada, el contenedor se estira accidentalmente)** | Falta `box-sizing: border-box` o `line-height` es demasiado pequeño | Compensar el modelo de caja globalmente; aumentar la altura de la línea; verifique el atributo de compresión flexible del niño. |
| P0-8 | **Accidente grave en la imagen (la imagen rota muestra una cruz de caja, la proporción está muy apretada/estirada)** | La ruta `src` es incorrecta o el archivo no existe; la imagen carece de la restricción `object-fit: cover` | Verificar y corregir el camino real; agregue estrictamente `ancho: 100%; altura: 100%; ajuste de objeto: cubierta; `para proteger la proporción. |

### P1 — Defecto obligatorio (no afecta la usabilidad básica, pero reduce significativamente la calidad)

| identificación | Síntomas | Diagnóstico de causa raíz | Recetas de reparación de CSS |
|----|------|---------|-------------|
| P1-1 | La parte del texto está truncada (se ve el principio pero desaparece el final) | La tarjeta `max-height` o `overflow:hidden` ha truncado el texto | Reducir el "tamaño de fuente" 1-2 px; o use `-webkit-line-clamp` para controlar el número de líneas; o aumentar la altura de la tarjeta |
| P1-2 | Espacio desigual entre tarjetas (en algún lugar abarrotadas, en algún lugar vacío) | Los valores de "brecha" son inconsistentes o algunas tarjetas tienen un "margen" adicional | Unifique el `espacio: 16px ~ 24px` del contenedor grid/flex; eliminar el "margen" individual de la tarjeta |
| P1-3 | El elemento decorativo bloquea el contenido del texto | Capa decorativa `z-index` >= capa de contenido | Capa decorativa: `índice z: 1; eventos de puntero: ninguno`; Capa de contenido: `índice z: 10` |
| P1-4 | Sin enfoque visual (todas las tarjetas tienen tamaño/color/tamaño de fuente similar) | Las tarjetas de primaria/secundaria no están diferenciadas | Tarjeta principal: tamaño de fuente +4px, agregue "borde izquierdo: 4px solid var(--accent-1)" o use un color de fondo destacado; secundario: reduce la saturación de fondo |
| P1-5 | Valores de color codificados (aparecen valores de color no variables como `#ff0000` y `rgb(...)`) | No se utilizan variables CSS | Reemplace todo con las variables correspondientes como `var(--accent-1)` |
| P1-7 | Los números de datos tienen el mismo tamaño que el texto principal, sin protagonismo visual | Los números clave no tienen estilo mejorado | Números: `font-size` es 8-12 px más grande que el texto, `font-weight: 700`, y está coloreado con `var(--accent-1)` |
| P1-8 | Una altura de línea demasiado pequeña hace que el texto se pegue entre sí | `altura de línea < 1,4` | Texto `altura de línea: 1,6 ~ 1,8`; título `altura de línea: 1,2 ~ 1,3` |
| P1-9 | **Pérdida de independencia del diseño** (el diseño/estructura de esta página parece copiado de la plantilla, en lugar de adaptado al contenido de esta página) | Más de 3 páginas consecutivas utilizan exactamente la misma estructura de cuadrícula, el mismo número y proporción de tarjetas, la misma combinación de estilo de tarjeta, lo que indica que el diseñador está aplicando una plantilla en lugar de diseñar para el contenido | Vuelva a examinar `page_goal` y `page_goal` de esta página `director_command`, vuelva a seleccionar la tecnología de diseño y la asignación de espacio en función de **lo que esta página quiere expresar**, en lugar de continuar con la estructura de la página anterior. El buen diseño se basa en el contenido, no en las plantillas |

### P2 — Elemento de pulido (mejora de la calidad, no bloquea pero fomenta la reparación)

| identificación | Síntoma | Sugerencias de arreglos |
|----|------|---------|
| P2-1 | Esquinas redondeadas inconsistentes (algunas tarjetas de 8 px, otras de 16 px) | Unificado a `var(--card-radius)` |
| P2-2 | Falta el elemento decorativo `signature_move` | Agregar por `decoration_dna.signature_move` |
| P2-3 | Degradar la fuente a la predeterminada del sistema (Nueva canción/tiempos) | Verifique la dirección de Google Fonts `@import` o la cadena de herencia `font-family` |
| P2-4 | La tarjeta tiene una sensación de flotación insuficiente (fuerte sensación de planitud) | Agregue `box-shadow: 0 4px 20px rgba(0,0,0,0.08)` |
| P2-5 | Gradiente insuficiente entre el título y el cuerpo del texto (espacio < 4px) | El título "tamaño de fuente" debe ser al menos 6 píxeles más grande que el texto del cuerpo |
| P2-6 | La "sensación general de la página de inicio" en lugar de la "sensación de presentación" | Aumentar el título `espaciado entre letras: -0.02em`; aumentar el espacio en blanco; aumentar el relleno de la tarjeta; añadir sutiles degradados o sombras a elementos decorativos |

---

## Parte C: Plantilla de informe de revisión estructurada (debe generarse en cada ronda)

Después de cada ronda de revisión de capturas de pantalla, el resultado tendrá estrictamente el siguiente formato (no se puede omitir ningún nivel):

```
## 审查报告 — 第 N 页 / 第 X 轮

### P0 致命缺陷
- [P0-1] [发现/通过] 具体描述 → 修复动作: ...
- [P0-2] [发现/通过]
- [P0-3] [发现/通过]
- [P0-4] [发现/通过]
- [P0-5] [发现/通过]
- [P0-6] [发现/通过] 严重排版重叠
- [P0-7] [发现/通过] 渲染切割破损
- [P0-8] [发现/通过] 图片破裂或扭曲变形

### P1 必修缺陷
- [P1-1] [发现/通过]
- [P1-2] [发现/通过]
- ...（逐条过，不得跳过）

### P2 抛光项
- [P2-1~P2-6] 逐条Breve descripción

### 本轮判定
- P0 全部通过: Sí/No
- 修复动作数: N
- 同类未收敛问题: [如有，列出问题 ID]
- SíNo触发回退 planning: Sí/No
- 进入下一轮: Sí（仍有修复需验证）/ No（达标，准备 FINALIZE）
```

**Ejecute la reparación inmediatamente después de generar el informe**: en lugar de terminar de escribir el informe y otras instrucciones, cambia el código mientras genera el informe.

---

## Parte D: Corregir la especificación de ejecución

### Secuencia de reparación (regla de hierro)

```
P0（致命）→ P1（必修）→ P2（抛光）
```

**Prioridad entre pares**:
1. Falta contenido/está truncado → complete el contenido primero
2. Diseño/desbordamiento → Reconstruir la estructura
3. Contraste/Legibilidad → Luego arregla el color
4. Decoración/textura → pulido final

### Intensidad de reparación: Reparación agresiva, no seas tímido (Reparación agresiva)

Cuando encuentre superposiciones importantes en el diseño, colapso del diseño y elementos que se bloquean entre sí en las capturas de pantalla, **nunca se arriesgue y simplemente modifique tentativamente +/- `5px` de `margin`/`padding` para "ajustar"**. El ajuste fino no tiene sentido en este caso:
- **Defiende la degradación sobre la suerte**: posicionamiento absoluto y cuadrícula compleja. Si el rollover hace que los bloques de texto se superpongan, significa que la representación falla por completo. Las configuraciones de reglas especiales que causan niveles superpuestos deben eliminarse de manera atronadora, y el sólido `display: flex; se debe aplicar flex-direction: column;` defensa, lo que obliga al componente a volver al flujo de documentos estándar. La línea de fondo defensiva no debe ser puesta a prueba.
- **Destruir configuraciones rígidas**: si `altura: 100%` hace que el contenido se desborde, elimine directamente la altura fija, use `min-height` en su lugar y deje que el contenido se expanda de forma adaptativa. Si una proporción fija aplana la tarjeta, agregue directamente una protección de valor extremo obligatoria como `min-width: 400px;`.
- **Elimine las campanas y silbatos y preserve la experiencia de lectura**: si las decoraciones complejas de posicionamiento absoluto y los patrones de fondo enormes interrumpen la lectura del texto y la estructura en capas no se puede aclarar en poco tiempo, utilice decisivamente un truco para borrarlo: `display: none !important;` o reduzca la transparencia a `0.02`.
Recuerde: **¡"Simple y tosco pero claro y legible" siempre superará a "elegante pero blando"! ¡Tu bisturí debe estar afilado! **

### Consejos de diagnóstico de CSS al reparar

Cuando vea un síntoma en un PNG, navegue hasta la fuente HTML:

| 视觉症状 | 优先检查的 CSS 属性与像素级渲染陷阱 |
|---------|-------------------|
| 内容被底部裁切 / 文字底部被削 | 容器 `overflow` 限制导致；`line-height` 太小引发字母下沉被切。 |
| Flex/Grid 布局塌陷挤按 | 缺失 `flex-shrink: 0` 导致被暴力挤压；未设定 `min-width`/`min-height` |
| 元素内边距溢出 / 意外扩容重叠 | 漏加 `* { box-sizing: border-box; }`，padding 撑破原有宽高。 |
| 文字发虚 / 对比度糊块 | 字号小且过度使用低不透明度，或Falta平滑抗锯齿属性。 |
| 绝对定位乱飞 / 死墙角溢展 | `position: absolute` 父级缺 `relative`；长宽百分比引发渲染位移超出画幅。 |
| 图片破裂 / 比例拉伸变形 | `src` 指向了错误路径；宽高被改变且没有加上 `object-fit: cover;` |
| 卡片占比失调重叠 | `grid-template-columns` 比例不对；`flex-grow/basis` 计算未考虑到内外边距 |
| 装饰混淆主图 / 喧宾夺主 | `z-index` 失控；或者滥用极高纯度背景色将主体遮盖。 |

### Reglas de validación fijas

Después de cada modificación HTML:
1. **Debes tomar una nueva captura de pantalla** (No debes juzgar el efecto de reparación según tu imaginación)
2. **Las capturas de pantalla deben archivarse en el directorio de la ronda** (Acuerdo de la Parte A-0)
3. Vuelva a ejecutar el protocolo de escaneo de la Parte A (al menos un paso rápido por la Patrulla Fronteriza)
4. **A partir de la segunda ronda, no leas las capturas de pantalla de las rondas anteriores, solo revisa las capturas de pantalla más recientes para verificarlas**
5. Verifique el elemento `[Descubrimiento]` en el informe anterior para confirmar si cambia a `[Aprobado]`
6. Preste atención a si la solución introduce nuevos problemas (es común que al corregir un error se introduzca otro)
7. Si está seguro de haber cambiado el código pero aún no funciona en la nueva captura de pantalla, verifique nuevamente para ver si se agregó en la posición incorrecta o no se pudo guardar correctamente.

---

## Parte E: Control redondo (sin límite superior hasta que sea perfecto)

> **Regla de hierro: al menos 2 rondas, FINALIZAR está prohibido en la 1.ª ronda y no hay límite superior en el número de veces. ** Incluso si se pasa la ronda 1, se debe realizar la ronda 2. Si todavía se encuentran defectos después de una determinada ronda de reparaciones, debe pasar incondicionalmente a la siguiente ronda** y no se permite ningún compromiso ni entrega por enfermedad.

| Redondo | Enfoque | Objetivo de esta ronda | ¿Puede FINALIZAR |
|------|------|---------|-------------|
| **Ronda 1** | Escaneo completo (Parte A completada 3 veces) + reparación drástica de todos los P0 y P1 | P0, P1 todos reparados | **No** (debe ingresar a la 2da ronda de verificación) |
| **Ronda 2 y posteriores** | Verifique que se haya implementado la reparación (vea la nueva imagen), continúe destruyendo la reconstrucción si no se repara y ejecute visual_qa.py | P0+P1 debe estar absolutamente limpio + visual_qa pasa | Sí (sólo cuando no existe ningún defecto) |

**Por qué la ronda 2 es obligatoria**:
- Es posible que las capturas de pantalla tomadas después de la primera ronda de reparación no hayan surtido efecto (prioridad CSS insuficiente, errores tipográficos, etc.). El efecto de reparación sólo se puede verificar mirando las nuevas imágenes y volviendo a escanearlas en la segunda ronda.
- LLM es extremadamente propenso a autodesestimarse en la ronda 1 - "Cambié el CSS y debería estar bien" - la ronda 2 es la única oportunidad de verificar esta ilusión
- El proceso de reparación puede introducir nuevos errores, que sólo podrán detectarse en la segunda ronda.

**FINALIZE 必要条件**（缺一不可）：
- **P0 全部清零**（任一 P0 残留 → 禁止 FINALIZE）
- **P1 全部清零**（任一 P1 残留 → 禁止 FINALIZE，必须继续修复）
- **visual_qa.py 退出码不为 1**（FAIL 项存在 → 禁止 FINALIZE）
- **至少完成 2 轮审查**（第 1 轮直接 FINALIZE → 无效）

**硬底线：死磕到底**：
- **只要 P0 或 P1 存在任何残留，必须继续截图、继续改码、继续进入下一轮！不存在“X轮后妥协交差”的说法！**
- **坚决不交带 P0 或 P1 的稿件。只要没修好，就一直修下去！**
- **坚决不交第 1 轮就声称全通过但未经后续轮次物理截图验证的稿件。**

### 回退止损规则（新增硬门）

- 如果同一个 P0 / P1 类别在连续 2 轮的新截图里仍然存在，说明问题已经不Sí微调能解决，而Sí planning 骨架或预算本身有问题。
- 此时**停止继续修 HTML**，在报告中明确写出 `SíNo触发回退 planning: Sí`，并说明需要重开的原因：
  - 预算超载
  - 布局承重墙错误
  - 高密页错误使用大图/重装饰
  - `dashboard` 不适合当前内容
- 回退后必须重写 `density_label / density_contract / layout_hint / cards 分配` 中至少一项，禁止只改 5px 边距再回来。

---

## Parte F: Verificación de infracción del contrato de contenido (modos de falla del tiempo de ejecución de contraste)

En el paso 2 del escaneo de la Parte A, se verifican simultáneamente los siguientes contratos:

| Modo de falla | Señales visuales en PNG | Instrucciones de reparación |
|-------------|-----------------|---------|
| **llenado insuficiente** | Hay mucho espacio en blanco en la página + hay muchas más decoraciones que texto | Primero complete la carga útil (regrese a planificación para verificar si falta contenido) |
| **colapso de soporte** | Sólo un número/título grande, sin capa explicativa | Complementar el contenido del cuerpo de la tarjeta de soporte |
| **falta carga útil** | No se encuentra una tarjeta de planificación en la página | Complete el bloque HTML que falta |
| **fuente sobrereclamación** | El texto final es sólido pero no está respaldado por datos/citas | Verificar si existe evidencia en el escrito, en caso contrario debilitar la redacción |
| **ancla sobreexpansión** | Un elemento ocupa >60% de la pantalla y el resto está apretado en la esquina | Reduzca el punto de anclaje al 40-50% para liberar espacio para la capa de soporte |
| **sustitución decorativa** | Muchos degradados/efectos de luz/texturas, pero baja densidad de información | Reducir la opacidad/área decorativa y añadir sustancia |

**Orden de reparación**: primero agrega contenido → luego ajusta la estructura → por último modifica la decoración. No se permiten ajustes cosméticos para cubrir contenido faltante.

---

## Parte G: Afirmaciones visuales automatizadas (aplicación de la ronda final)

Después de que la ronda final de capturas de pantalla pase el escaneo manual, se debe ejecutar un script de afirmación visual automatizado como verificación objetiva:

```bash
python3 SKILL_DIR/scripts/visual_qa.py PNG_OUTPUT --planning PLANNING_OUTPUT --html SLIDE_OUTPUT
```

断言结果解读：

| Código de salida | Significado | Tu acción |
|--------|------|---------|
| 0 | Todo pasó | OK FINALIZAR |
| 1 | FAIL (defecto fatal) | Debes arreglar los elementos correspondientes y volver a capturar la pantalla y reafirmar |
| 2 | WARN (advertencia de calidad) | Enumere los elementos WARN de forma veraz en FINALIZE sin bloquear |

**Si el script de aserción genera FAIL, deshabilite FINALIZAR**. Debe solucionarlo y volver a tomar capturas de pantalla y ejecutar aserciones hasta que el código de salida no sea 1.

---

## Compromiso de circuito cerrado

- Cada ronda: **Captura de pantalla + archivo → Ver la última captura de pantalla → Escanear 3 veces → Informe estructurado → Cambiar código inmediatamente → Verificación de nueva captura de pantalla**
- Cualquier cosa que diga "Creo que debería estar bien" no cuenta y debe verificarse con PNG.
- **No se permiten alucinaciones**: "El CSS ha sido modificado por lo que debería estar bien" no cuenta y debe confirmarse tomando una captura de pantalla.
- **Mire solo imágenes nuevas**: no es necesario buscar imágenes antiguas con frecuencia para compararlas, solo confirme según la experiencia visual y la ronda anterior de informes de texto.
- P0 es la ley de hierro, P1 es el resultado final y P2 es la búsqueda.
- P0, P1 son las líneas de la vida y la muerte. ¡Mientras quede un poquito, hay que modificarlo en un bucle infinito hasta erradicarlo por completo!
- La ronda final debe confirmarse automáticamente a través de `visual_qa.py`