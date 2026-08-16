# Tipo de datos -> Índice de referencia de inspiración de decoración

> Este documento mapea los distintos tipos de datos (data types) con las técnicas de diseño (T) y armas CSS (W) más adecuadas.
> Utilízalo como una tabla de búsqueda (lookup table) para asignar el peso decorativo correcto.

## Clasificación de densidad decorativa

| Nivel de densidad | Significado | T Número de técnicas | W Número de armas | Escenarios aplicables |
|---------|------|---------|---------|---------|
| `mínimo` | Casi sin decoración, domina la carga útil del contenido | 0-1 | 0-1 | Página puramente académica intensiva / panel de datos puros |
| `bajo` | Restringir la decoración y solo brindar asistencia estructural | 1-2 | 1-2 | escena densa (informe/técnico/formación) |
| `medio` | Equilibrando decoración y contenido | 2-3 | 2-3 | Página de contenido estándar |
| `generoso` | Rica decoración, impulsada por la atmósfera | 2-3 | 2-4 | Portada / Portada del capítulo / Página de frases / Página final |

---

## Clase de visualización de datos

| Tipo de datos | Técnica T recomendada | Arma W recomendada | Densidad de decoración | Principio de combinación |
|---------|------------|------------|---------|---------|
| `tablas_datos` | T3 (superposición del eje Z) T9 (punto de anclaje de pulso) | W7 (sombra multicapa) W8 (marca de fila de pseudoelemento) | `bajo` | La mesa en sí tiene un fuerte sentido de estructura, y la decoración solo resalta las filas y realza las capas.
| `métricas` | T2 (simbiosis extrema del tamaño de fuente) T10 (fondo de datos) | W1 (texto degradado) W4 (progreso circular) | `medio` | Los números son anclajes visuales naturales y requieren el máximo contraste entre el tamaño de fuente y los gráficos de fondo para aumentar la sensación de densidad.
| `kv_pairs` | T9 (punto de anclaje de pulsos) T4 (panel isla flotante) | W8 (pseudo elemento divisor) W7 (sombra multicapa) | `bajo` | Los pares clave-valor requieren mucha información, la decoración solo agrupa puntos de anclaje y una separación exquisita |
| `matriz_datos` | T3 (superposición del eje Z) T6 (penetración de sombreado) | W2 (recorte geométrico) W7 (sombra multicapa) | `medio` | La matriz de cuatro cuadrantes requiere un color independiente para cada cuadrante + profundidad de fabricación de superposición |
| `datos_embudo` | T5 (cinta biselada) T3 (superposición del eje Z) | W2 (recorte geométrico) W1 (texto degradado) | `medio` | El ritmo decreciente del embudo es naturalmente adecuado para el sentido de dirección biselada + la cinta degradada guía la línea de visión |
| `pie_data` | T10 (antecedentes de datos) T2 (simbiosis de tamaño de fuente) | W4 (gradiente cónico) W1 (texto degradado) | `medio` | El propio gráfico de anillos es el protagonista visual y el fondo permite que los datos ocupen la pantalla |
| `serie_tendencia` | T10 (base de datos) T5 (cinta biselada) | W1 (texto degradado) W9c (cinta sangrante) | `medio` | Las líneas de tendencia necesitan un sentido de dirección, y la polilínea base + cinta biselada implica el flujo del tiempo |
| `lista_clasificada` | T2 (simbiosis de tamaño de fuente) T9 (punto de anclaje de pulso) | W1 (texto degradado) W8 (número de serie del pseudoelemento) | `medio` | El número de clasificación requiere contraste en el tamaño de fuente y el punto de anclaje marca la posición clave de clasificación |
| `tarjeta_puntuación` | T10 (base de datos) T2 (simbiosis de tamaño de fuente) | W4 (gradiente cónico) W7 (sombra multicapa) | `medio` | Los gráficos/puntuaciones de radar requieren un dibujo de gradiente cónico + números flotantes en el gráfico |
| `datos_distribución` | T10 (base de datos) T3 (superposición del eje Z) | W1 (texto degradado) W2 (recorte geométrico) | `medio` | Los histogramas apilados deben recortarse para crear una sensación de volumen + base para llenar la pantalla |

##Categoría de análisis empresarial

| Tipo de datos | Técnica T recomendada | Arma W recomendada | Densidad de decoración | Principio de combinación |
|---------|------------|------------|---------|---------|
| `foda` | T3 (superposición del eje Z) T6 (penetración de sombreado) | W2 (recorte geométrico) W7 (sombra multicapa) | `medio` | Los cuatro cuadrantes requieren colores independientes en cada área + penetración de sombreado para crear distinción de profundidad |
| `planes_precios` | T4 (panel de isla flotante) T3 (superposición del eje Z) | W7 (sombra multicapa) W8 (pseudo marca de esquina del elemento) | `medio` | La solución recomendada requiere una protuberancia de isla flotante para crear el foco principal + recomendación de marca de esquina |
| `desglose_costos` | T10 (base de datos) T2 (simbiosis de tamaño de fuente) | W4 (progreso circular) W1 (texto degradado) | `medio` | La relación de costos es adecuada para gráficos de anillos + grandes números totales como anclajes visuales |
| `matriz_competitiva` | T3 (superposición del eje Z) T8 (gravedad asimétrica) | W7 (sombra multicapa) W8 (pseudo marca de esquina del elemento) | `medio` | La comparación de productos competitivos requiere la selección del elemento recomendado + guía de gravedad asimétrica |
| `cadena_valor` | T5 (cinta de inglete) T9 (punto de anclaje de pulso) | W2 (corte geométrico) W9c (cinta sangrante) | `medio` | La dirección del flujo de flecha de la cadena de valor requiere guía biselada + punto de anclaje para marcar el segmento de valor agregado |

## Clase de argumento comparativo

| Tipo de datos | Técnica T recomendada | Arma W recomendada | Densidad de decoración | Principio de combinación |
|---------|------------|------------|---------|---------|
| `antes_después` | T8 (gravedad asimétrica) T6 (penetración de sombreado) | W2 (recorte geométrico) W7 (sombra multicapa) | `medio` | El contraste del antes y el después requiere naturalmente la tensión espacial de uno pesado y otro ligero |
| `pros_contras` | T8 (gravedad asimétrica) T9 (punto de anclaje de pulso) | W8 (icono de pseudoelemento) W7 (sombra multicapa) | `medio` | La comparación de ventajas y desventajas requiere un icono de verificación + fortalecimiento asimétrico de la tendencia de selección |
| `comparación_escenario` | T4 (panel de isla flotante) T3 (superposición del eje Z) | W7 (sombra multicapa) W2 (recorte geométrico) | `medio` | Recomendación para escenas múltiples que requieren islas flotantes sobresalientes + espacio en soluciones de fabricación de superposiciones |

## Clase de estructura de proceso

| Tipo de datos | Técnica T recomendada | Arma W recomendada | Densidad de decoración | Principio de combinación |
|---------|------------|------------|---------|---------|
| `cronologías` | T9 (punto de anclaje de pulso) T5 (cinta biselada) | W8 (línea de conexión de pseudoelemento) W1 (texto degradado) | `medio` | Los nodos de la línea de tiempo son naturalmente adecuados para puntos de anclaje de pulso + los cortes biselados implican la dirección del tiempo |
| `flujos_proceso` | T9 (punto de anclaje de pulso) T5 (cinta de inglete) | W8 (marca de paso de pseudoelemento) W2 (corte geométrico) | `medio` | Los pasos del proceso requieren puntos de anclaje para marcar nodos clave + un sentido de dirección entre los pasos de corte y fabricación |
| `elementos_paralelos` | T4 (panel de isla flotante) T3 (superposición del eje Z) | W7 (sombra multicapa) W8 (pseudo marca de esquina del elemento) | `bajo` | Se ha regularizado la estructura de elementos paralelos, y la decoración es únicamente estampado de tarjetas y marcas de números de serie.
| `jerarquías` | T6 (penetración de sombreado) T3 (superposición del eje Z) | W8 (línea de conexión de pseudoelementos) W9e (resta decorativa) | `medio` | Las relaciones jerárquicas deben expresarse conectando líneas + el sombreado distingue la profundidad jerárquica |
| `ciclo_flujo` | T6 (penetración de sombreado) T9 (punto de anclaje de pulso) | W4 (gradiente cónico) W8 (arco de pseudoelemento) | `medio` | La estructura de anillo del flujo del ciclo es adecuada para gradientes cónicos + puntos de anclaje para marcar nodos clave |
| `árbol_decisión` | T6 (penetración de sombreado) T9 (punto de anclaje de pulso) | W8 (pseudoelemento ramal) W2 (recorte geométrico) | `medio` | El árbol de decisión requiere expresión de línea de rama + ruta condicional de distinción de sombreado |
| `capas_piramidales` | T3 (superposición del eje Z) T5 (cinta de inglete) | W2 (corte geométrico) W1 (texto degradado) | `medio` | La progresión trapezoidal de la pirámide es naturalmente adecuada para el corte en bisel + capas de fabricación superpuestas |
| `mapa_partes interesadas` | T6 (penetración de sombreado) T9 (punto de anclaje de impulso) | W9e (resta decorativa) W8 (etiqueta de pseudoelemento) | `bajo` | La estructura de círculo concéntrico solo necesita una forma geométrica grande + punto de anclaje para marcar el papel clave |
| `mapa_viaje` | T9 (punto de anclaje de pulso) T5 (cinta biselada) | W8 (línea de carril de pseudoelemento) W1 (texto degradado) | `medio` | Los carriles múltiples del mapa de viaje requieren líneas de carril claras + contactos de marca de anclaje |

## Categoría de contenido narrativo

| Tipo de datos | Técnica T recomendada | Arma W recomendada | Densidad de decoración | Principio de combinación |
|---------|------------|------------|---------|---------|
| `definiciones` | T7 (compresión de espacios en blanco) T4 (panel de isla flotante) | W8 (pseudo elemento divisor) W1 (texto degradado) | `bajo` | El contenido de la definición requiere terminología clara: capas de explicación y espacios en blanco para resaltar los términos |
| `hito_resultados` | T2 (simbiosis de tamaño de fuente) T1 (marca de agua límite) | W1 (texto degradado) W7 (sombra multicapa) | `generoso` | Los resultados de los hitos son puntos emocionales altos y requieren números extremadamente grandes + marcas de agua para crear una sensación de ceremonia |
| `testimonios_de_usuario` | T7 (opresión de espacios en blanco) T8 (gravedad asimétrica) | W5 (vidrio esmerilado) W8 (comillas de pseudoelemento) | `medio` | Los testimonios deben estar decorados con comillas grandes + espacios en blanco para darle un respiro a la cita |
| `pares_faq` | T4 (Panel de isla flotante) T9 (Punto de anclaje de pulso) | W8 (Marcador Q/A de pseudoelemento) W7 (Múltiples capas de sombra) | `bajo` | Las preguntas frecuentes contienen mucha información, la decoración solo hace distinción visual de preguntas y respuestas y agrupación de islas flotantes |
| `number_highlights` | T2 (simbiosis de tamaño de fuente) T1 (marca de agua que rompe fronteras) | W1 (texto degradado) W9a (dígitos fuera del marco) | `generoso` | Los números centrales requieren el tamaño de fuente máximo + fuera de marco para crear impacto en el espacio |
| `story_arc` | T5 (cinta biselada) T9 (punto de anclaje de pulso) | W8 (anotación de pseudoelemento en tres actos) W1 (texto degradado) | `medio` | El flujo horizontal en tres actos requiere un sentido de dirección + los puntos de anclaje marcan los puntos de inflexión |
| `citas_expertas` | T7 (espacio en blanco para la opresión) T8 (gravedad asimétrica) | W8 (pseudoelemento comillas grandes) W5 (vidrio esmerilado) | `medio` | Las citas de expertos requieren una sensación de espacio en blanco autorizado + comillas grandes como firma visual |
| `lista de verificación` | T9 (punto de anclaje de pulsos) T4 (panel isla flotante) | W8 (casilla de verificación de pseudoelemento) W7 (sombra multicapa) | `bajo` | La lista es contenido de tipo ejecución y la decoración solo visualiza el estado marcado |
| `pares_analogía` | T8 (gravedad asimétrica) T5 (cinta de corte oblicuo) | W2 (recorte geométrico) W8 (línea de mapeo de pseudoelementos) | `medio` | La analogía requiere un sentido de mapeo de la dirección de "conocido → objetivo" + la asimetría distingue a ambos lados |

##Categoría Académica Técnica

| Tipo de datos | Técnica T recomendada | Arma W recomendada | Densidad de decoración | Principio de combinación |
|---------|------------|------------|---------|---------|
| `fragmentos_de_código` | T4 (panel de isla flotante) T6 (penetración de sombreado) | W10b (línea de escaneo) W7 (sombra multicapa) | `bajo` | El bloque de código requiere una línea de escaneo de detección de terminal + protuberancia de isla flotante y distinción de fondo |
| `resultados_del_experimento` | T3 (superposición del eje Z) T10 (pavimentación de datos) | W7 (sombra multicapa) W8 (marca de pseudoelemento) | `bajo` | Los datos experimentales son pruebas contundentes, la decoración debe ser extremadamente moderada, solo capas de estructura de datos |
| `diagrama_arquitectura` | T6 (penetración de sombreado) T3 (superposición del eje Z) | W9e (resta de decoración) W8 (línea de conexión de pseudoelementos) | `medio` | El diagrama de arquitectura requiere cajas en capas + use un sombreado geométrico grande en lugar de decoración de fragmentos |
| `fórmula_datos` | T7 (compresión de espacios en blanco) T4 (panel de isla flotante) | W1 (texto degradado) W8 (anotación de pseudoelemento) | `bajo` | La fórmula debe estar centrada con caracteres grandes + descripciones variables dispuestas en silencio, y la decoración solo proporciona una ayuda mínima.

## Clase de estado de progreso

| Tipo de datos | Técnica T recomendada | Arma W recomendada | Densidad de decoración | Principio de combinación |
|---------|------------|------------|---------|---------|
| `progreso_tracker` | T9 (punto de anclaje de impulsos) T10 (pavimentación de datos) | W4 (gradiente cónico) W8 (color de estado del pseudoelemento) | `medio` | La barra de progreso es adecuada para dibujar un degradado cónico + el punto de anclaje marca la posición actual |
| `gantt_data` | T5 (cinta biselada) T9 (punto de anclaje de pulso) | W2 (recorte geométrico) W8 (escala de tiempo de pseudoelementos) | `bajo` | El diagrama de Gantt requiere mucha información y la decoración solo incluye escalas de tiempo y marcadores de líneas de dependencia |
| `status_dashboard` | T10 (base de datos) T3 (superposición del eje Z) | W11 (esquina HUD) W4 (gradiente cónico) | `medio` | El tablero es adecuado para enmarcar HUD para crear una sensación de consola + base de gráficos múltiples |
| `elementos_acción` | T9 (punto de anclaje de pulsos) T4 (panel isla flotante) | W8 (etiqueta de persona responsable del pseudoelemento) W7 (sombra multicapa) | `bajo` | Los elementos de acción son contenido ejecutivo y la decoración solo incluye el estado de la tarea y la marca de la persona responsable |
| `elementos_riesgo` | T9 (punto de anclaje de pulso) T3 (superposición del eje Z) | W8 (color de estado del pseudoelemento) W7 (sombra multicapa) | `bajo` | Los elementos de riesgo requieren visualización del color de estado rojo/amarillo/verde + puntos de anclaje para marcar elementos de alto riesgo |

## Equipo y Geografía

| Tipo de datos | Técnica T recomendada | Arma W recomendada | Densidad de decoración | Principio de combinación |
|---------|------------|------------|---------|---------|
| `perfiles_de_equipo` | T4 (panel de isla flotante) T6 (penetración de sombreado) | W7 (sombra multicapa) W5 (vidrio esmerilado) | `medio` | La tarjeta de personaje necesita una protuberancia de isla flotante + sombreado para crear una sensación de atmósfera |
| `datos_geográficos` | T6 (penetración de sombreado) T1 (marca de agua que rompe fronteras) | W9e (resta decorativa) W1 (texto degradado) | `medio` | Los datos geográficos son adecuados para formas de sombreado grandes para sugerencias regionales + marcas de agua para identificación geográfica |
| `imagen_candidatos` | T1 (marca de agua que rompe fronteras) T7 (compresión de espacios en blanco) | W5 (vidrio esmerilado) W3 (máscara perforada) | `generoso` | Las imágenes grandes requieren vidrio esmerilado para cubrir la capa de texto + enfoque de máscara perforada + firma de marca de agua |

---

## Mapeo por Tipo de Página (Page Type)

Cuando la página no consume ningún tipo de datos explícito, utilice `page_type`:

| tipo_página | Densidad de decoración predeterminada | Técnicas T recomendadas | Armas W recomendadas |
|-----------|------------|------------|------------|
| `portada` | `generoso` | T1 (marca de agua que rompe fronteras) T7 (compresión de espacios en blanco) T2 (simbiosis de tamaño de fuente) | W1 (texto degradado) W5 (vidrio esmerilado) W3 (máscara perforada) |
| `toc` | `bajo` | T5 (cinta biselada) T9 (punto de anclaje de pulso) | W8 (pseudoelemento) W1 (texto degradado) |
| `sección` | `generoso` | T1 (marca de agua que rompe fronteras) T7 (compresión en blanco) | W1 (texto degradado) W6 (modo mixto) |
| `fin` | `generoso` | T1 (marca de agua que rompe fronteras) T7 (compresión en blanco) T8 (gravedad asimétrica) | W1 (texto degradado) W5 (vidrio esmerilado) |
| `contenido` (predeterminado) | `medio` | (determinado por tipo de datos) | (determinado por tipo de datos) |

---

## Reglas de combinación de múltiples tipos de datos

Al consumir varios tipos de datos en una página:

1. **Unión, eliminar duplicados**: recopile todos los números T/W recomendados y elimine duplicados
2. **Límite superior total**: No más de 3 tarjetas T, no más de 3 tarjetas W
3. **Prioridad**: la recomendación de los tipos de datos consumidos por la tarjeta ancla tiene prioridad sobre la tarjeta de soporte.
4. **Tome la densidad más baja**: si un tipo de datos recomienda "baja" y otro tipo recomienda "media", toda la página se basará en "baja" (principio de prioridad de contenido).
5. **Conflicto duplicado**: dos tipos de datos recomiendan técnicas contradictorias (como la compresión en blanco T7 frente a la base de datos T10). Se da prioridad a retener aquellos que coincidan con el tipo de datos ancla.

## Lógica de decisión de ejecución de la arquitectura (fase de planificación)

1. **Mira la intención**: ¿Qué sensación de opresión u orden necesita esta página para brindarle a la gente?
2. **Contrato estricto**: Extraiga estrictamente las técnicas T y las opciones de configuración de armas W de los tipos de datos especificados en la tabla, y está prohibido crearlas de la nada.
3. **Prioridades claras**: Elige entre 1 y 2 de las armas más expresivas (nunca más de 3 para evitar que la complejidad del código se salga de control) y elimina con decisión otras decoraciones triviales.
4. ** Liberación forzada **: registre claramente "el eje y la lógica espacial de la configuración del arma" en `resource_rationale`, lo que equivale a publicar un dibujo de construcción completo en el escenario HTML.