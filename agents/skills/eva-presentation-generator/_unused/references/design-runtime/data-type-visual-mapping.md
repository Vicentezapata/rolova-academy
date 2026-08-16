# Tipo de datos -> Índice de referencia de presentación visual

> Esta tabla asigna estrictamente los tipos de datos principales en resumen (métricas, líneas de tiempo, antes_después, etc., más de 40 tipos) a `card_type`, `layout_hint` y la mejor referencia de implementación de CSS en el proyecto.
> **Disciplina de sangre de hierro**: esta tabla es una biblioteca de componentes de mapeo rígido del motor de arquitectura y de ninguna manera es una "inspiración" para que las personas la descarten a voluntad. Después de que el subagente de Planificación haya establecido la "línea de movimiento y enfoque visual", cuando encuentre un tipo de datos específico, primero debe seleccionar la solución óptima en esta tabla para aceptarla **. El precio de la libertad es el colapso de la calidad y la desorganización estructural. Siga estrictamente las mejores prácticas.
> Cubre 8 categorías principales: visualización de datos, análisis de negocios, argumentación comparativa, estructura de procesos, contenido narrativo, académicos técnicos, estado de progreso, equipo y geografía.

Esta tabla es un puente para **organización de datos ascendente/estructuración breve -> Paso 4 (Planificación) -> Paso 4 (HTML)**.

- En la etapa de compilación de datos ascendentes, consulte la columna "Tipo de datos" para identificar y formatear los datos originales.
- Subagente de planificación del paso 4 **Marque según sea necesario** las columnas "Tipo de tarjeta recomendado" y "Diseño recomendado" para inspirarse, pero la selección final depende de la intención del diseño.
- Para el subagente HTML en el Paso 4, consulte la columna "Referencia de implementación de CSS" y seleccione la técnica de representación.

## Clase de visualización de datos

| Tipo de datos | Tipo de tarjeta recomendada | Diseño recomendado | Referencia de implementación de CSS | Tipos de páginas aplicables |
|----------|---------------|----------|-------------|----------|
| `tablas_datos` | `datos` / `comparación` | simétrico / tres columnas | estándar `<tabla>` + cebra + filas resaltadas | evidencia / comparación |
| `métricas` | `datos_resaltados` | hero-top / primaria-secundaria | `charts/kpi.md` `charts/metric-row.md` | portada / evidencia / cerrar |
| `kv_pairs` | `datos` / `lista` | simétrico / primaria-secundaria | etiqueta + valor diseño de dos columnas, etiqueta translúcida | configuración / evidencia |
| `matriz_datos` | `matrix_chart` | monofocal / primaria-secundaria | `blocks/matrix-chart.md` cuadrícula 2x2 | comparación / marco |
| `datos_embudo` | `datos` | monofocal / primaria-secundaria | `charts/funnel.md` trapezoidal descendente | proceso/evidencia |
| `pie_data` | `datos` | primaria-secundaria | `charts/ring.md` Gráfico de anillos + leyenda | evidencia / comparación |
| `serie_tendencia` | `datos` | primaria-secundaria / hero-top | `charts/sparkline.md` polilínea + etiqueta | evidencia / cerrar |
| `lista_clasificada` | `lista` / `data_highlight` | en forma de L / asimétrica | Número clasificado + barra de gradiente + valor | evidencia / comparación |
| `tarjeta_puntuación` | `datos` | enfoque único | `charts/radar.md` gráfico de radar | evidencia / comparación |
| `datos_distribución` | `datos` | primaria-secundaria | `charts/stacked-bar.md` barra apilada | evidencia |

##Categoría de análisis empresarial

| Tipo de datos | Tipo de tarjeta recomendada | Diseño recomendado | Referencia de implementación de CSS | Tipos de páginas aplicables |
|----------|---------------|----------|-------------|----------|
| `foda` | `matrix_chart` | enfoque único | Cuadrícula de colores 2x2, color separado para cada cuadrante | marco / comparación |
| `planes_precios` | `comparación` | simétrico / tres columnas | alineación de tarjetas + resaltado de recomendaciones + lista de verificación | comparación / cerrar |
| `desglose_costos` | `datos` | primaria-secundaria | `charts/stacked-bar.md` + `charts/ring.md` proporción | evidencia/proceso |
| `matriz_competitiva` | `comparación` / `matrix_chart` | monofoco / simétrico | tabla de comparación de varias columnas + bloque de color de calificación | comparación |
| `cadena_valor` | `proceso` | forma de L / cascada | cadena de flechas + anotación value_add para cada segmento | marco / proceso |

## Clase de argumento comparativo

| Tipo de datos | Tipo de tarjeta recomendada | Diseño recomendado | Referencia de implementación de CSS | Tipos de páginas aplicables |
|----------|---------------|----------|-------------|----------|
| `antes_después` | `comparación` | simétrico | columnas izquierda y derecha + colores contrastantes + flechas | evidencia / comparación |
| `pros_contras` | `comparación` | simétrico | doble columna + icono de marca verde/cruz roja | comparación / marco |
| `comparación_escenario` | `comparación` | simétrico / tres columnas | tarjeta de escena + resaltado de resultados | comparación / cerrar |

## Clase de estructura de proceso

| Tipo de datos | Tipo de tarjeta recomendada | Diseño recomendado | Referencia de implementación de CSS | Tipos de páginas aplicables |
|----------|---------------|----------|-------------|----------|
| `cronologías` | `línea de tiempo` | forma de L / cascada | `bloques/timeline.md` `charts/timeline.md` | proceso/evidencia |
| `flujos_proceso` | `proceso` | forma de L / cascada | número de paso + línea de conexión + resaltado de advertencia | proceso/marco |
| `elementos_paralelos` | `lista` / `datos` | simétrico / tres columnas | Tarjeta paralela + icono + tamaño de fuente unificado | evidencia / configuración |
| `jerarquías` | `diagrama` | foco único / en forma de T | `blocks/diagram.md` sangría anidada / forma de árbol | marco |
| `ciclo_flujo` | `proceso` / `diagrama` | enfoque único | diseño de flecha circular + título central | marco / proceso |
| `árbol_decisión` | `diagrama` | foco único / forma de L | ramal + etiqueta de condición + nodo de resultado | marco / proceso |
| `capas_piramidales` | `diagrama` | enfoque único | trapezoide/triángulo multicapa + progresivo de arriba a abajo | marco |
| `mapa_partes interesadas` | `diagrama` | enfoque único | círculos concéntricos + etiquetas de entidad | marco/configuración |
| `mapa_viaje` | `proceso` / `línea de tiempo` | cascada / en forma de l | Proceso horizontal de varios carriles + curva de emoción | marco / proceso |

## Categoría de contenido narrativo

| Tipo de datos | Tipo de tarjeta recomendada | Diseño recomendado | Referencia de implementación de CSS | Tipos de páginas aplicables |
|----------|---------------|----------|-------------|----------|
| `definiciones` | `texto` | primaria-secundaria | términos en negrita + texto explicativo + línea divisoria | configuración / evidencia |
| `hito_resultados` | `datos_resaltados` | héroe-top / simétrico | `charts/kpi.md` número grande + descripción del logro | cerrar/cta |
| `testimonios_de_usuario` | `cita` / `gente` | asimétrica / primaria-secundaria | `bloques/quote.md` `bloques/personas.md` | evidencia / cerrar |
| `pares_faq` | `lista` / `texto` | en forma de L / simétrica | Q negrita + sangría + contraer expandir | configuración / evidencia |
| `number_highlights` | `datos_resaltados` | héroe superior / enfoque único | `charts/kpi.md` tamaño de fuente súper grande + unidad + contexto | portada / cierre / evidencia |
| `story_arc` | `línea de tiempo` / `texto` | cascada / en forma de l | Flujo lateral en tres actos + anotación de emociones | configuración / evidencia |
| `citas_expertas` | `cita` | primaria-secundaria / asimétrica | `blocks/quote.md` + avatar + organización | evidencia / configuración |
| `lista de verificación` | `lista` | en forma de L / simétrica | Casilla de verificación + color del estado de finalización | proceso / cerrar |
| `pares_analogía` | `texto` / `comparación` | simétrico | Columna izquierda "conocido" + columna derecha "objetivo" + flecha de mapeo | configuración/marco |

##Categoría Académica Técnica

| Tipo de datos | Tipo de tarjeta recomendada | Diseño recomendado | Referencia de implementación de CSS | Tipos de páginas aplicables |
|----------|---------------|----------|-------------|----------|
| `fragmentos_de_código` | `texto` | primaria-secundaria / monofocalidad | `<pre><code>` + resaltado de sintaxis + números de línea | evidencia/marco |
| `resultados_del_experimento` | `datos` / `comparación` | primaria-secundaria | hipótesis-método-resultado tres secciones + tabla de datos | evidencia |
| `diagrama_arquitectura` | `diagrama` | foco único / en forma de T | `blocks/diagram.md` cuadros en capas + líneas de conexión | marco |
| `fórmula_datos` | `texto` | primaria-secundaria | Fórmula en fuente grande y centrada + lista de descripción de variables | evidencia/marco |

## Clase de estado de progreso

| Tipo de datos | Tipo de tarjeta recomendada | Diseño recomendado | Referencia de implementación de CSS | Tipos de páginas aplicables |
|----------|---------------|----------|-------------|----------|
| `progreso_tracker` | `datos` / `lista` | en forma de L / simétrica | `charts/progress-bar.md` barra de progreso + color de estado | proceso / cerrar |
| `gantt_data` | `línea de tiempo` | cascada / monofoco | barra horizontal + escala de tiempo + línea de dependencia | proceso/marco |
| `status_dashboard` | `datos` / `lista` | cuadrícula mixta | Etiqueta de clasificación + bloque de color de estado (verde/amarillo/rojo) | proceso / cerrar |
| `elementos_acción` | `lista` | en forma de L / simétrica | tarea + etiqueta de propietario + fecha de vencimiento | cerrar/cta |
| `elementos_riesgo` | `datos` / `lista` | en forma de L / simétrica | Bloque de color de riesgo (rojo/amarillo/verde) + medidas de mitigación | proceso / cerrar |

## Equipo y Geografía

| Tipo de datos | Tipo de tarjeta recomendada | Diseño recomendado | Referencia de implementación de CSS | Tipos de páginas aplicables |
|----------|---------------|----------|-------------|----------|
| `perfiles_de_equipo` | `gente` | simétrico / tres columnas | `blocks/people.md` avatar + nombre + posición | configurar / cerrar |
| `datos_geográficos` | `datos` | monofocal / primaria-secundaria | lista de regiones + resaltado + escala de color numérica | evidencia |
| `imagen_candidatos` | `image_hero` | héroe-top/forma de l | `bloques/image-hero.md` | portada/sección |

---

## sugerencias de extensión tipo_tarjeta

Enumeración actual de tipo de tarjeta (13 tipos):

```
text | data | list | process | tag_cloud | data_highlight | timeline | diagram | quote | comparison | people | image_hero | matrix_chart
```

Nota: `process` es un `card_type` nativo válido del validador, pero actualmente no existe un `blocks/process.md` independiente. Al usarlo, no espere que `resource_loader resolve` obtenga automáticamente el texto del bloque exclusivo; debe implementarse junto con `layout_refs`, `principle_refs`, `director_command` y los recursos de gráficos necesarios.

Extensiones sugeridas (+9):

```
+funnel        → 漏斗可视化
+pie_ring      → 饼图/环形图
+trend_chart   → 趋势折线图
+ranked        → 排行榜
+score_radar   → 评分雷达图
+cycle         → 循环流程图
+pyramid       → 金字塔/分层图
+journey       → 用户旅程图
+code_block    → 代码片段
```

Después de la expansión, hay 22 tipos de tarjetas, cada uno con su correspondiente referencia de implementación CSS y documentación de bloque.

---

## Lógica combinacional del arquitecto senior (cómo consumir esta tabla)

Esta tabla proporciona un mapeo extremadamente claro de datos a canales físicos visuales.

1. **Reducción y reorganización de la dimensionalidad**: si cree que puede transmitir la intención de manera más perfecta, puede usar "métricas" en un diseño "asimétrico" (asimétrico) o incluso en "cascada".
2. **Llamada transfronteriza**: puede colocar las tablas de datos `data_tables` de Kuicao en el sistema diseñado para `competitive_matrix`.
3. **Declaración importante**: en el borrador de planificación, cuando su combinación de diseño adopta este conjunto de estándares en todos los niveles, es más importante describir claramente la base física de su espacio en `resource_rationale` y `prose` para garantizar que su selección no sea una bofetada aleatoria en la frente sino que tenga una estricta autoconsistencia del contenedor, de modo que la capa HTML se pueda representar de manera segura. .