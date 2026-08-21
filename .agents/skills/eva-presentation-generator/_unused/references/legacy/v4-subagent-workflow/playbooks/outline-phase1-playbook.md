# Libro de estrategias de la Fase 1 del esquema: ideas de redacción del esquema y generación de estructuras

## Objetivo

Diseñar un esquema narrativo persuasivo basado en materiales estructurados y las necesidades de los usuarios. Usted es el arquitecto del esquema y su responsabilidad es construir el esqueleto narrativo, no completar el código de contenido específico.



## Metodología

### Tres pilares

1. **Principio de la pirámide** - Conclusión primero, unifique lo anterior, categorice y agrupe, y progrese lógicamente
2. **Arco narrativo** -- Trayectoria emocional con altibajos (captador al principio, detallado en el medio y sublime al final)
3. **Ritmo de densidad**: primero toda la plataforma debe tener una sensación general y luego dejar espacios en blanco para cada página.

### Proceso de pensamiento de 5 pasos

1. **Refinando el argumento central general** - Mira la situación completa y escribe 1 oración del alma.
2. **Determinar el número y tema de las Partes** - incluyendo la relación lógica entre las Partes (progresión/giro/causalidad)
3. **Derivación del conjunto completo de tendencias de densidad** - Trate `page_density` en `requirements-interview.txt` como una tendencia a nivel de plataforma, en lugar de una densidad fija por página:
   - `Menos pero mejor -> relajado`
   - `Moderado -> equilibrado`
   - `Capacidad extrema / densidad extremadamente alta -> ultra_dense`
4. **Elija una estrategia argumental para cada parte** -- narrativa_driven (narrativa) / data_driven / case_study / comparación / marco / paso_a_paso / autoridad
5. **Asigne páginas y determine el argumento y la ventana de densidad para cada página** -- **Cada página tiene solo una oración page_goal, que no debe contener la palabra "y"** (Si hay "y", significa que esta página contiene dos objetivos y debe dividirse en dos páginas); al mismo tiempo, proporcione "límite inferior de densidad/objetivo de densidad/límite superior de densidad"
6. **Buscar soporte para historias y contenido** - ¡El contenido debe estar estructurado! El poder de PPT proviene de la combinación de conocimientos en la cima de la pirámide y datos poderosos en la base. Se debe dar prioridad a la extracción de puntos de datos modulares altamente refinados, grupos de comparación y palabras clave del material. Si te encuentras con una narrativa de texto puro, también debes desmontar el esqueleto lógico. Vaya al resumen del material para encontrar armas que realmente puedan soportar la compleja matriz de componentes y rechace los párrafos mediocres y largos con altos decibeles.

---

## Tendencia de densidad y reglas de espacio entre páginas.

### tendencia de densidad a nivel de cubierta

Todo el mazo debe seleccionar primero una "tendencia de densidad":

| Entrada del usuario `page_density` | "Tendencia de densidad" normalizada | Significado |
|---|---|---|
| Menos pero mejor | `relajado` | En general más relajado, pero se permite una pequeña cantidad de "medio/alto" para el clímax |
| Moderado | `equilibrado` | Equilibrio global, que permite fluctuaciones evidentes |
| Capacidad extremadamente alta/densidad extremadamente alta | `ultra_denso` | Toda la ventana sube y la página del búfer no se puede devolver "baja" |

### etiqueta de densidad a nivel de página

Cada página debe utilizar uno de los siguientes 5 archivos:

`bajo` / `medio_bajo` / `medio` / `alto` / `panel`

Son el **tono a nivel de página**, no la única densidad para toda la plataforma. Lo que tienes que hacer es:
- Primero, deja que toda la plataforma tenga una sensación general unificada.
- Luego cree un espacio entre páginas dentro de la ventana permitida.
- No comprimir todas las páginas en el mismo archivo

### Ventana predeterminada para cada tendencia

| `tendencia de densidad` | Distribución predeterminada de la página `contenido` | restricciones especiales |
|---|---|---|
| `relajado` | `bajo ~ medio` | Permita una pequeña cantidad de "euforia" como clímax; deshabilitar el `panel` |
| `equilibrado` | `medio_bajo ~ alto` | `dashboard` solo se puede utilizar como una pequeña cantidad de páginas especiales |
| `ultra_denso` | `medio ~ tablero` | Debe haber una página de búfer relativa, pero la página de búfer solo se puede reducir a "mediana" |

### Reglas estrictas comunes

- No se permite que "portada/sección/fin" sea "panel de control"
- Desactivar 3 páginas consecutivas de "alto/panel"
- Debe haber al menos una página de transición que no sea del panel de control antes y después del "panel de control".
- Todo el mazo debe dar una "curva de densidad", que indique qué páginas son el clímax y cuáles son el buffer.

---

## esquema.txt Forzar formato esqueleto

Su salida debe cumplir estrictamente con los siguientes niveles y campos. El paso 4 posterior analizará su salida línea por línea. No cambie el nombre de la clave a voluntad (por ejemplo, "Destino de página" no se puede cambiar a "Destino de página").

```text
# 大纲
核心论点：{一句话灵魂，贯穿全篇的中心论断}
叙事结构：{问题->方案->效果 / Sí什么->为什么->怎么做 / 全景->聚焦->行动 / 对比论证 / 时间线 / 其他}
密度倾向：{relaxed / balanced / ultra_dense}
密度曲线：{一句话概括整套 deck 的密度节奏，例如：low -> mid_low -> high -> medium -> close}
总页数：{N}

---

## Part 1: {part_title}
Part 目标：{part_goal}
论证策略：{narrative_driven / data_driven / case_study / comparison / framework / step_by_step / authority}
与上一 Part 的关系：{无（首Part）/ 递进 / 转折 / 因果 / 并列}

### 第 1 页：{page_title}
- 页目标：{page_goal，一句话，不含"和"字}
- 叙事角色：{cover / toc / section / evidence / comparison / process / close / cta}
- 页面类型映射：{cover / toc / section / content / end}
- 密度下限：{low / mid_low / medium / high / dashboard}
- 密度目标：{low / mid_low / medium / high / dashboard}
- 密度上限：{low / mid_low / medium / high / dashboard}
- 节奏动作：{铺垫 / 推进 / 爆发 / 缓冲 / 收束}
- 信息姿态：{结论页 / 解释页 / 证据页 / 仪表盘页 / 呼吸页}
- 锚点类型：{标题 / KPI / 图表 / 表格 / 图片 / 引言}
- 论证方式：{proof_type}
- 内容支撑：{这一页需要哪些结构化的金句、数据骨架和逻辑分类来支撑论点。强烈建议在此处对长文进行初步的数据点级切粒。}
- 素材来源：{found_in_brief: true/false，若 false 标注缺口_说明为何缺失却仍需此页}

### 第 2 页：{page_title}
...

---

## Part 2: ...
```

**Restricciones de enumeración de campos**:
- El `rol narrativo` debe seleccionarse estáticamente de `{portada, toc, sección, evidencia, comparación, proceso, cierre, cta}`.
- "Mapeo de tipo de página" debe seleccionarse estáticamente desde "{portada, toc, sección, contenido, fin}", correspondiente al "tipo_página" en el Paso 4 posterior.
- La `tendencia de densidad` debe elegirse estáticamente entre `{relajada, equilibrada, ultra_densa}`.
- El `límite inferior de densidad/objetivo de densidad/límite superior de densidad` debe seleccionarse estáticamente desde `{bajo, medio_bajo, medio, alto, tablero}` y debe satisfacer el `límite inferior <= objetivo <= límite superior`.
- Se debe seleccionar `Acción de ritmo` entre `{Presagio, Avance, Explosión, Amortiguación, Conclusión}`.
- Se debe seleccionar `Postura de información` de `{Página de conclusión, Página de explicación, Página de evidencia, Página de panel, Página de respiración}`.
- Se debe seleccionar `Tipo de anclaje` en `{Título, KPI, Gráfico, Tabla, Imagen, Introducción}`.

### Rol narrativo → reglas de mapeo de tipo de página

| papel narrativo | tipo_página | descripción |
|---------|-----------|------|
| `portada` | `portada` | portada |
| `toc` | `toc` | Página de contenido |
| `sección` | `sección` | Página de transición de capítulo |
| `evidencia` / `comparación` / `proceso` | `contenido` | Página de contenido de texto |
| `cerrar` / `cta` | `fin` | Página final (cerrar=revisión resumida, cta=llamado a la acción)|



## Reglas de aplicación del esqueleto de demostración (no se pueden omitir)



| ubicación | papel narrativo | tipo_página | necesidad | funcionalidad principal |
|------|----------|-----------|--------|----------|
| Página 1 | `portada` | `portada` | **Obligatorio** | Impacto del título + sentido del ritual de la marca |
| Página 2 | `toc` | `toc` | **Obligatorio (cuando el número total de páginas >= 6)** | Hoja de ruta global, que permite a la audiencia comprender la estructura en 3 segundos |
| Página de inicio de cada Parte | `sección` | `sección` | **Obligatorio** | Página de respiración de transición de capítulo, que le dice a la audiencia que ingrese a un nuevo capítulo |
| Última página | `cerrar` o `cta` | `fin` | **Obligatorio** | Conclusión central + llamado a la acción |

**Detección de infracción**:
- Falta cubierta o extremo = **Defecto estructural, se debe reparar**
- Total de páginas >= 6 pero sin toc = **Defecto estructural, debe repararse**
- La primera página de cualquier Parte no es una sección (excepto que la primera página de la Parte 1 es portada/toc) = **Defecto estructural, la Parte debe tener una página de sección**
- Las páginas de la sección solo hacen transiciones de respiración. Está **absolutamente prohibido** insertar gráficos de datos o diseños de varias tarjetas en las páginas de las secciones.

### Reglas de continuación del tema (flexibilidad garantizada)

- El tema de una Parte no se limita a ser tratado en una sola Parte: si un tema es rico en contenido, se puede dividir en varias Partes, cada una de las cuales se centra en diferentes dimensiones del tema.
- La relación entre las Partes puede ser **progresiva/profundizada/expandida** (diferentes niveles del mismo tema), y no tiene que ser un tema independiente completamente nuevo
- Por ejemplo: "Parte 2: Descripción general de la solución técnica → Parte 3: Análisis profundo de la solución técnica" es una estructura completamente legal
- Pero cada parte debe tener su propio "objetivo de la parte" claro, incluso si es una continuación del mismo tema general.

### Reglas de asignación de densidad (obligatorias)

- Las páginas de `portada` utilizan preferentemente `low / mid_low`
- Las páginas `toc` usan preferentemente `mid_low / medium`
- Las páginas de `sección` usan preferentemente `low / mid_low`
- Las páginas de "contenido" se distribuyen según la "tendencia de densidad" de la plataforma.
- La página "final" usa preferentemente "mid_low / medium", y se puede llegar a "high" en el modo "ultra_dense".

**No distribuya uniformemente la densidad mecánicamente**:
- La plataforma "relajada" también permite 1 página de "alta"
- La plataforma "equilibrada" debe tener al menos 2 densidades diferentes
- La plataforma `ultra_dense` no puede escribir todas las páginas de contenido como `tablero`