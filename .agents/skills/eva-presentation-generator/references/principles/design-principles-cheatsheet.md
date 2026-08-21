# Hoja de referencia de principios de diseño - Paso 4 Manual de operación a nivel de campo

> El propósito no es enseñar teoría, sino decirle al planificador de páginas: cuando un determinado campo en JSON está escrito incorrectamente, cuál se debe cambiar.



---

## Principios de acceso a CARP

### Prioridades en conflicto

Cuando CARP parezca entrar en conflicto con un valor predeterminado existente, siga este orden:

1. "requisitos/esquema/planificación" dan prioridad a las fuentes verdaderas
2. `scene_mode` y `density_contract` tienen prioridad
3. A CARP sólo le importa el diseño y el orden, no el estilo y el alma.
4. `variation_strategy` garantiza "el mismo origen pero caras diferentes" para evitar que la repetición degenere en una copia de plantilla

### Cuatro definiciones breves

- **Contraste**: decide quién es visto primero y quién tiene que retroceder
- **Alineación**: determina a qué conjunto de esqueletos comunes pertenecen los elementos, en lugar de flotar aleatoriamente
- **Repetición**: determina si los personajes con la misma semántica hablan el mismo lenguaje visual, en lugar de un sistema de remake de página a página.
- **Proximidad**: determine si la información relacionada está agrupada de forma natural, en lugar de depender del texto para explicar la relación.

### Medidor de velocidad del modo escena

| modo_escena | Contraste | Alineación | Repetición | Proximidad |
|-----------|----------|-----------|------------|-----------|
| `lanzamiento` | Fuerte, puede usarse como diferencia de presión entre héroe y etapa | Medio, permite más gravedad libre | Medio, conserva la sintaxis pero no la apariencia | Medio, evita el cierre excesivo de la página |
| `negocio` | Los juicios de servicio de nivel medio-fuerte se realizan en secuencia | Medio-alto | Medio-alto | Alto, los juicios/bases/acciones deben ser en grupos |
| `informe` | Medio, indicadores de servicio e interpretación de la gestión | Alto | Alto | Alto, el eje de comparación y la descripción deben agregarse |
| `académico` | Medio, cumple con la prioridad de manifestación y no tiene impacto publicitario | Muy alto | Muy alto | Muy alto, las definiciones/evidencias/límites deben estar en grupos |
| `técnico` | Medio, estructura de servicio/mecanismo/escaneo de restricciones | Muy alto | Alto | Muy alto, los módulos/pasos/restricciones deben agruparse |
| `formación` | Medio, pasos de servicio y recordatorios en secuencia | Alto | Alto | Muy alto, los escalones/advertencias/puntos de control deben estar cerca |

### Descripción rápida del mapeo de campos

| CARPA | 优先落在哪些字段 |
|------|------------------|
| Contraste | `visual_weight` / `design_intent.contrast_strategy` / `cards[].role` / `cards[].card_style` |
| Alineación | `layout_hint` / `focus_zone` / `director_command.spatial_strategy` / `layout_variation_note` |
| Repetición | `variation_guardrails.same_gene_as_deck` / `cards[].card_style` / `director_command.techniques` |
| Proximidad | `page_text_strategy` / `cards[].content_focus` / `content_budget` / `compression_priority` |

---

## Principio 1. Jerarquía visual

Pregunta central: ¿Quién es el personaje principal de esta página y quién tiene que dar un paso atrás?

Campos afectados prioritarios:
-`peso_visual`
- `sugerencia_diseño`
- `tarjetas[].rol`
- `tarjetas[].card_style`
- `director_command.anchor_treatment`



Banderas rojas:
- 3 o más cartas están "llenas"
- sin "ancla"
- `director_command.anchor_treatment` es simplemente una tontería de "destacar"
- La escena densa aún comprime todos los puntos clave en tamaños de fuente similares y pesos de fuente similares

---

## Principio 2. Carga cognitiva

Pregunta central: ¿Cuánto necesita digerir la audiencia en esta página?

Campos afectados prioritarios:
-`peso_visual`
- `etiqueta_densidad`
- `tarjetas[].cuerpo`
- `tarjetas[].chart`
- `ritmo_acción`

Método de corrección:
- Si hay demasiadas tarjetas en una página: divídalas en 2 tarjetas o pase a la página siguiente
- Si se debe retener una gran cantidad de información: marque `rhythm_action` como "ráfaga" y organice "búfer" en la página siguiente
- Si hay menos información pero mucho contenido: cambiar a `enfoque único` o `sección libre`
- Si la información no es mucha pero parece desordenada: verifique si "Proximidad" falló primero en lugar de eliminar el contenido primero

Banderas rojas:
- Hay más de 5 cartas en la página de contenido y todas quieren ser las protagonistas.
- Coloque 3 tipos de gráficos en una página al mismo tiempo
- `visual_weight` es bajo, pero el contenido de `cards` es muy denso

---

## Principio 3. Composición y espacios en blanco

Pregunta central: ¿el espacio habla o simplemente contiene contenido?

Campos afectados prioritarios:
- `sugerencia_diseño`
- `nota_variación_diseño`
- `director_command.estrategia_espacial`
- `decoración_sugerencias.fondo`

Método de corrección:
- Si la descripción del diseño vuelve a ser "una pieza a la izquierda y dos a la derecha": reescríbala como una relación de gravedad en lugar de mosaicos de píxeles.
- Si dos páginas consecutivas están estructuradas como clones: escriba al menos 2 dimensiones contrastantes en `variation_guardrails. Different_from_previous`
- Si la frase dorada o la portada del capítulo todavía está abarrotada: baje el `visual_weight` y use `free-section`
- Si los elementos están "casi alineados": reescriba `director_command.spatial_strategy` para especificar línea de base, columna, banda o eje central en lugar de palabras de orientación vagas
- En el escenario "académico/técnico/informe", se requiere una mayor alineación por defecto; No utilices la gravedad libre del lanzamiento para hacer tablas densas.

Banderas rojas:
- Descripciones de estilo web, como "tres columnas divididas equitativamente" y "bloques superior e inferior".
- Sin `nota_variación_diseño`
- `background.feel` está vacío o sólo es "conciso"
- La distancia entre cartas relacionadas y cartas irrelevantes es casi la misma y no se puede ver el esqueleto de agrupación.

---





Campos afectados prioritarios:
- `sugerencias_decoración.*`
- `tarjetas[].card_style`
- `variation_guardrails.same_gene_as_deck`

Método de corrección:
- Si hay muchas decoraciones pero ninguna prioridad: conserva 1 técnica a nivel de página + 1 técnica a nivel de tarjeta
- Si página y página son completamente diferentes del mismo mazo: agregue `same_gene_as_deck`
- Si es demasiado estable y similar a una plantilla: refuerce `background.feel` o `page_accent.feel`, pero especifique `restraint`
- `Repetición` sólo requiere que "caracteres similares hablen la misma gramática" y no requiere que cada página tenga la misma longitud; lo que hay que repetir es la función del título, la función de la etiqueta, la función de anotación y la sintaxis del borde, no el resultado de la composición.

Banderas rojas:
- Los tres niveles de `decoration_hints` están todos escritos como "ligero adorno"
- Las combinaciones de armas en cada página son exactamente iguales.
- Más de 1 tarjeta "acento"

---

## Principio 5. Expresión honesta de los datos

Cuestión central: los datos son evidencia, no pegatinas.

Campos afectados prioritarios:
- `tarjetas[].puntos_datos`
- `tarjetas[].chart`
- `objetivo_página`
- `audiencia_para llevar`

Método de corrección:
- Cuando no haya datos específicos, no pretenda ser una página de datos, cámbiela a `framework` o `quote`
- Cuando haya KPI principales, organice al menos 1 `data_highlight` o `data` con un gráfico
- Si el gráfico existe sólo para decoración, elimine "gráfico"

Banderas rojas:
- Los gráficos son sólo "para parecer profesionales"
- `page_goal` es una sentencia de juicio, pero no hay una tarjeta de evidencia para realizarla
- `data_points.source` muchos espacios en blanco

---

## Principio 6. Ritmo y Variación

Pregunta central: ¿Hay respiración y propulsión al pasar las páginas?







---



- **Error de contraste**: todos los tamaños y pesos de fuente y las áreas de las tarjetas son similares y el público no sabe dónde mirar primero.
- **Error de alineación**: los elementos están "casi alineados" pero no tienen una línea de columna, una línea de borde o un eje central común
- **Repetición no válida**: Es el mismo bloque de título/etiqueta/comentario/indicador, pero la sintaxis cambia en cada página.
- **Proximidad no válida**: el título, la descripción, el indicador y la anotación están dispersos entre sí y la relación solo puede explicarse mediante texto.
- **Mal uso de CARP**: convertir "académico/técnico/informe" en el héroe del lanzamiento; o hacer "lanzamiento" en una página de tabla demasiado rígida

---

## Tabla de corrección de campo

| Problemas encontrados | Qué campo cambiar primero | Qué campo mirar a continuación |
|-----------|------------|------------|
| La página es correcta pero no espectacular | `director_comando` | `sugerencias_de_decoración` |
| Páginas como páginas web | `layout_hint` | `nota_variación_diseño` |
| Las cartas son todas iguales | `tarjetas[].card_style` | `tarjetas[].rol` |
| El ritmo es demasiado plano | `visual_peso` | `acción_ritmo` |
| Desorden de decoración | `decoration_hints.*.restraint` | `variación_guardrails` |
| Argumento fuerte pero evidencia débil | `tarjetas[].puntos_datos` | `gráfico` |

---

## Formulario de examen físico de 8 elementos página por página

- ¿Es el `page_goal` de esta página un argumento completo que se puede juzgar?
- ¿Existe una prioridad clara en `cards[]` en lugar de distribuirla uniformemente?
- ¿Coincide realmente `layout_hint` con la estructura del contenido en lugar de con un diseño personalizado?
- ¿`director_command` da una idea clara de la cámara?
- ¿Las tres capas de `decoration_hints` cumplen con sus funciones?
- ¿Es diferente de la página anterior en al menos 2 dimensiones?
- ¿`must_avoid` alcanza el riesgo de creación de plantillas más peligroso en esta página?
- Después de que la capa de diseño obtenga el JSON de esta página, ¿puede saber qué no se puede cambiar y qué se puede usar libremente?