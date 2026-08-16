# Sistema de Estilos

> Material no predeterminado. Libro de trabajo creativo solo para humanos (human-only creative workbook).
>
> Este documento no se inyecta como material de la cadena principal de tiempo de ejecución predeterminado, y no entra en la cadena de inyección de prompt predeterminada ni en la cadena de carga automática de recursos. Si todo este documento se inyecta directamente a gran escala en los subagentes de planificación (planning) o HTML, aumentará significativamente el riesgo de creación de plantillas e imitación.

## Concepto Central

> **Los 8 estilos preestablecidos son paletas de referencia, no uniformes fijos.** Proporcionan combinaciones de colores e ideas decorativas comprobadas, pero puedes:
> - Ajustar los valores de color basándote en los estilos preestablecidos.
> - Combinar las características de dos estilos.
> - Crear combinaciones de colores completamente nuevas basadas en el tema (solo necesitas seguir los principios de color a continuación).
>
> **La única regla inquebrantable**: Todos los colores deben referenciarse a través de variables CSS para garantizar la coherencia global.
>
> **Regla de la agilidad**: Bajo el mismo conjunto de variables de estilo, la combinación decorativa de cada página debe ser diferente. La caja de herramientas de decoración proporciona técnicas que se pueden combinar libremente, no paquetes fijos. Elige una combinación de 2-3 técnicas para cada página, y las combinaciones de páginas adyacentes no deben ser idénticas.

## Modelo de Datos style.json

style.json no es solo un contenedor para variables CSS, sino también la **definición del genotipo del alma visual** de toda la presentación. Debe llevar tres capas de información: genes de valores de color, descripción del alma y estrategia de variación.

### Estructura Completa (Obligatorio tanto al crear un estilo propio como al elegir uno)

```json
{
  "style_id": "ID personalizado o ID preestablecido",
  "style_name": "Nombre del estilo",
  "mood_keywords": ["3-5 palabras clave de emoción, como 'instrumento de precisión', 'frío del espacio profundo', 'pulso de luz tenue'"],
  "design_soul": "Declaración del alma en una oración -- Usa un lenguaje emocional para describir la experiencia emocional central que este estilo quiere transmitir. Esta oración servirá como un ancla emocional cuando se genere cada página HTML. Ejemplo: 'Un hilo dorado cruza la pared roja de la Ciudad Prohibida al atardecer, revelando una luz cálida en la solemnidad'",
  "variation_strategy": "Estrategia de variación entre páginas -- Describe cómo crear cambios dinámicos entre páginas bajo este gen de estilo. Ejemplo: 'La página de fondo oscuro usa una matriz de cuadrícula + línea decorativa de esquina para crear una sensación de instrumento de precisión, la página de transición clara usa una respiración de halo de área grande + espacio en blanco minimalista, las dos alternancias extremas forman un latido visual'",
  "decoration_dna": {
    "signature_move": "La técnica decorativa más emblemática de este estilo (1 tipo), debe aparecer al menos una vez cada 3-4 páginas",
    "forbidden": ["Técnicas decorativas explícitamente prohibidas (elementos que destruirían la consistencia del estilo), como 'matriz de cuadrícula', 'efecto de halo'"],
    "recommended_combos": [
      "Combinación de técnica decorativa recomendada A (ej. 'subrayado de título + burbuja de número + línea divisoria que se desvanece')",
      "Combinación de técnica decorativa recomendada B (ej. 'decoración de esquina + marca de agua grande + bloque de color de marca')"
    ]
  },
  "css_variables": {
    "bg_primary": "#Fondo principal",
    "bg_secondary": "#Color de transición degradado",
    "card_bg_from": "#Inicio de degradado de tarjeta",
    "card_bg_to": "#Fin de degradado de tarjeta",
    "card_border": "rgba(Color de borde)",
    "card_radius": "12px",
    "text_primary": "#Título/Cuerpo",
    "text_secondary": "rgba(Texto auxiliar)",
    "accent_1": "#Énfasis principal",
    "accent_2": "#Énfasis secundario",
    "accent_3": "#Tercer énfasis",
    "accent_4": "#Cuarto énfasis"
  },
  "font_family": "PingFang SC, Microsoft YaHei, system-ui, sans-serif",
  "css_snippets": {
    "title_style": "font-size: 28px; font-weight: 700; letter-spacing: -0.5px; border-bottom: 3px solid var(--accent-1); padding-bottom: 8px; display: inline-block;",
    "list_marker": "content:''; width: 6px; height: 6px; border-radius: 2px; background: var(--accent-1); margin-right: 12px; flex-shrink: 0;",
    "body_text": "font-size: 14px; line-height: 1.8; color: var(--text-primary);",
    "page_number": "font-size: 11px; color: var(--text-secondary); opacity: 0.5; position: absolute; bottom: 24px;",
    "card_padding": "padding: 28px 32px;",
    "section_gap": "gap: 20px;"
  }
}
```

### Descripción de Campos

| Campo | Función | Qué afecta |
|------|------|---------|
| `mood_keywords` | 3-5 palabras clave emocionales para guiar la elección de la atmósfera decorativa para cada página | Selección de `decoration_hints` por el planificador + implementación decorativa por el diseñador |
| `design_soul` | Declaración del alma en una oración -- lenguaje emocional para describir la experiencia emocional central del estilo | Inyectado en el prompt de cada página, sirve como ancla emocional del diseñador |
| `variation_strategy` | Estrategia de variación entre páginas -- describe el ritmo y los métodos de cambio entre páginas | Guía a los diseñadores para crear saltos dinámicos bajo un gen unificado |
| `decoration_dna` | ADN de decoración (técnicas emblemáticas/prohibidas/combinaciones recomendadas) | Asegura que la elección de decoración sea ágil pero no fuera de lugar |
| `css_variables` | Variables de valor de color puro -- garantía estricta de consistencia global | Mapeado directamente a variables CSS :root |
| `css_snippets` | Fragmentos CSS consolidados -- Anclajes duros de consistencia entre páginas para dimensiones **no de color** como estilo de título/marcador de lista/tamaño de texto del cuerpo/espaciado | Inyectado en el contexto de cada página, el LLM debe usar estrictamente estos estilos fijos |

> **Distinción clave**: `design_soul` y `variation_strategy` proporcionan "contexto de intención de diseño" al LLM, en lugar de código CSS específico. Resuelven la pregunta del alma de "por qué se eligen estos colores y cómo cambian entre las páginas", en lugar del problema de implementación de "qué CSS se debe usar para este elemento".

## Principios de Color (Líneas de fondo estrictas al crear colores propios)

| Principio | Requisito | Propósito |
|------|------|------|
| Contraste Seguro | El contraste entre el texto y el fondo >= 4.5:1 | Garantizar la legibilidad |
| Regla 60-30-10 | Color de fondo 60%, tarjeta/color secundario 30%, color de énfasis (accent) 10% | Evitar ser "llamativo" |
| Moderación de acento | No más de 2 colores de énfasis (accent) en la misma página (puede variar en diferentes páginas) | Enfoque visual claro |
| Consistencia de profundidad | Fondo oscuro con texto claro, fondo claro con texto oscuro | Legibilidad básica |
| Distinción entre tarjeta y fondo | Hay una diferencia de color perceptible entre el fondo de la tarjeta y el fondo de la página (al menos un 5% de diferencia de brillo) | Límite de tarjeta claro |

## 8 Paletas de Colores de Referencia

> Estos son esquemas de color probados que se pueden usar directamente, ajustarse para encajar o usarse como inspiración para colores creados a medida.

| Paleta | Archivo | Tono | Emoción adecuada |
|--------|------|------|----------|
| Azul Blanco Negocios | `blue-white.md` | Fondo claro + acento azul | Profesional, confiable, institucional |
| Gris Blanco Minimalista | `minimal-gray.md` | Fondo claro + gris/negro + punto rojo | Tranquilo, académico, diseño suizo |
| Tierra Cálida | `warm-earth.md` | Fondo crema + camel/verde oliva | Cálido, de alta calidad, estilo de vida |
| Verde Fresco | `fresh-green.md` | Fondo claro + acento verde | Natural, saludable, orgánico |
| Muro de Palacio Rojo | `royal-red.md` | Fondo oscuro + acento rojo/oro | Solemne, estilo nacional, sentido de ceremonia |
| Tecnología Oscura | `dark-tech.md` | Fondo oscuro + acento cian/azul | Geek, conferencia de prensa, espacio profundo |
| Púrpura/Oro Lujo | `luxury-purple.md` | Fondo oscuro + acento púrpura/oro | Alta gama, lujo, alta costura |
| Arcoíris Vibrante | `vibrant-rainbow.md` | Fondo claro + acento multicolor | Joven, vivo, Instagram |

---

## Proceso de Decisión de Estilo

### Prioridad de Decisión

| Prioridad | Señal | Acción |
|--------|------|------|
| 1 | El usuario **especificó claramente** un estilo o color de marca | Usarlo directamente / crear basado en el color de la marca |
| 2 | El tema tiene una fuerte tendencia emocional | Elegir una paleta de colores que coincida con la emoción, que se puede afinar |
| 3 | La audiencia tiene preferencias claras | Consultar el mapeo de audiencia a continuación |
| 4 | Ninguna preferencia obvia | `blue_white` como predeterminado seguro |

### Audiencia -> Emoción -> Paleta de Colores

| Audiencia | Emoción esperada | Paleta de Referencia |
|------|----------|----------|
| Gestión corporativa / inversores | Profesional y confiable | `blue_white` / `minimal_gray` / Serie de colores fríos propios |
| Gobierno / Instituciones públicas | Estable y formal | `blue_white` / `royal_red` / Serie de colores solemnes propios |
| Académicos / Investigadores | Tranquilo y sobrio | `minimal_gray` / Serie de colores de baja saturación propios |
| Desarrolladores / Equipos técnicos | Sensación de futuro geek | `dark_tech` / Serie de tecnología oscura propia |
| Bienes de consumo / Marcas de estilo de vida | Cálido y de alta calidad | `warm_earth` / Serie de colores cálidos propios |
| Consumidores jóvenes | Vivo y creativo | `vibrant_rainbow` / Serie de colores brillantes propios |
| Clientes de alta gama | Textura de lujo | `luxury_purple` / Serie premium de color oscuro propia |
| Temas de salud / Naturaleza | Orgánico y fresco | `fresh_green` / `warm_earth` / Serie verde propia |

### Metodología de Creación Ágil -- Pensando como un Director de Arte

> No simplemente "elijas una paleta y saques variables CSS". Estás **mezclando un alma visual única** para este proyecto en particular.

**Paso 1: Extraer Palabras Clave Emocionales**

Extrae 3-5 **palabras emocionales o sensoriales** del tema, la audiencia y la estructura narrativa, no palabras descriptivas de color como "azul" o "oscuro", sino **palabras de experiencia sinestésica** como "sensación de instrumento de precisión", "frío del espacio profundo", "cálido fuego del hogar".

| Tipo de Tema | Ejemplos de palabras clave emocionales |
|---------|-------------|
| IA / Productos Tecnológicos | Instrumento de precisión, Frío del espacio profundo, Pulso de luz tenue, Torrente de datos |
| Negocios Corporativos | Sólido como una roca, Plan claro, Ancla de confianza, Respiración profesional |
| Cultura / Historia | Atardecer en el muro del palacio, Patrón oscuro de hilo de oro, Precipitación pesada, Ceremonia solemne |
| Salud / Naturaleza | Luz de la mañana a través de las hojas, Corriente fina de manantial claro, Respiración orgánica, Crecimiento suave |
| Creativo / Joven | Bloque de color rebotando, Refracción de prisma, Néctar de fiesta, Risa sin límites |

**Paso 2: Derivar Colores de las Emociones**

No es "elegir azul porque es tecnología", sino "elegir una combinación de azul de aguas profundas + pulso de luz cian para transmitir la sensación de un 'instrumento de precisión respirando rítmicamente en el espacio profundo'".

| Ruta de Derivación | Ejemplo |
|---------|------|
| Emoción -> Analogía Natural -> Color | "Instrumento de precisión" -> Interior de la cúpula del observatorio -> Fondo negro azul oscuro + Luz de escaneo cian fría |
| Emoción -> Asociación de Escena -> Color | "Atardecer en el muro del palacio" -> El sol poniente golpea el muro rojo -> Rojo bermellón oscuro + Luz lateral dorada oscura |
| Emoción -> Sinestesia Táctil -> Color | "Crecimiento suave" -> Dedos tocando hojas nuevas -> Menta muy clara + Verde dorado de sol cálido |

**Paso 3: Escribir la Declaración del Alma**

Usa una oración para describir la **sensación de imagen** que este conjunto de colores quiere transmitir. Esta oración se inyectará en el prompt de generación de HTML de cada página y se convertirá en el ancla emocional del diseñador.

Buenas declaraciones de alma:
- "En el interior de la cúpula del observatorio, una fría luz de escaneo cian de un instrumento cruza la cortina negra azul oscura rítmicamente -- preciso, frío, pero cada escaneo contiene un pulso"
- "Un hilo dorado cruza la pared roja de la Ciudad Prohibida al atardecer, revelando una luz cálida en la solemnidad -- cada textura tiene el peso de mil años"
- "La luz de la mañana se filtra a través de los poros de las hojas jóvenes, proyectando una respiración color menta en el papel blanco -- suave, orgánico, sin prisas"

Malas declaraciones de alma:
- "Estilo de tecnología azul, negocios profesionales" -- sin sentido de imagen, el LLM solo producirá cuadrados azules uniformes
- "Fondo oscuro + acento de color brillante" -- Esta es una descripción del valor del color, no del alma

**Paso 4: Diseñar la Estrategia de Variación**

Bajo un gen unificado, cómo crear variaciones ágiles entre páginas. La estrategia de variación no es "usar decoraciones diferentes en cada página" (todos lo saben), sino describir **el ritmo del cambio**.

Buenas estrategias de variación:
- "La página de fondo oscuro usa una matriz de cuadrícula + línea decorativa de esquina para crear una sensación de instrumento de precisión (tensión), la página de transición clara usa una respiración de halo de área grande + espacio en blanco minimalista (liberación), las dos alternancias extremas forman un latido visual"
- "Las páginas impares son más cálidas y pesadas (decoración dorada pintada de forma gruesa), las páginas pares son más frías y ligeras (solo líneas finas + marcas de agua), creando la alternancia de luz y oscuridad del paso de página de un pergamino de palacio"

Malas estrategias de variación:
- "Usar decoraciones diferentes en cada página" -- Obvio
- "Alternar usando diferentes diseños (layouts)" -- Esto es un problema de diseño (layout), no una variación de estilo

### Guía de Creación de Colores Propios

Cuando las paletas preestablecidas no coinciden perfectamente, crea la tuya:

1. Completa el "método de cuatro pasos de creación ágil" anterior
2. Elige la paleta de colores preestablecida más cercana como **punto de partida**
3. Ajusta según las siguientes estrategias:
   - Cambiar color de acento -> Mantener el fondo y el texto, solo ajustar el color de énfasis
   - Cambiar temperatura de color -> Cambiar colores fríos a cálidos (azul -> naranja) o viceversa
   - Cambiar brillo -> Cambiar fondo claro a fondo oscuro (voltear simultáneamente el color del texto y el color de la tarjeta)
4. Generar el style.json completo (**debe incluir mood_keywords / design_soul / variation_strategy / decoration_dna**, no solo css_variables)

---

## Caja de Herramientas de Técnicas Decorativas

> **La decoración no es una lista fija, son técnicas que se pueden combinar libremente.** Cada técnica tiene su alma visual y escenario aplicable. Al menos 2-3 técnicas combinadas por página.

### Técnicas de Capa de Fondo

| Técnica | Alma Visual | Emoción Adecuada |
|------|---------|----------|
| Matriz de cuadrícula | Sensación de instrumento de precisión, como sombreado de papel de coordenadas | Tecnología, ingeniería, impulsado por datos |
| Bloque de color degradado | Sensación de iluminación suave, como un halo junto a una fogata | Cálido, natural, amigable |
| Efecto de halo | Bola de luz futurista, como un foco de atención en la oscuridad | Lanzamiento, ciencia ficción, geek |
| Líneas geométricas | Sentido esquelético de un edificio, como líneas auxiliares en un plano | Ingeniería, estructura, rigor |
| Mapa base de textura | Materialidad, como el toque del papel/satén/tinta | Cultura, textura, tradición |
| Partículas de ruido | Textura fractal generada por SVG feTurbulence, como papel de arroz / esmerilado / grano de película | Sensación hecha a mano, académico, marca de alta gama, cultura |
| Líneas de escaneo | Líneas finas horizontales creadas por repeating-linear-gradient, como un monitor CRT | Panel de tecnología, vista de monitoreo, páginas ricas en datos |

### Técnicas de Capa de Tarjeta

| Técnica | Alma Visual | Efecto |
|------|---------|------|
| Línea de énfasis izquierda | Barra vertical de una valla, una entrada para guiar la línea de visión del lector | Ancla visual |
| Burbuja de número | Placa de número circular, como una marca de navegación | Sensación de número de secuencia |
| Banda de color superior | El "sombrero" de la tarjeta, una línea horizontal de color para identificar la categoría | Etiqueta de clasificación |
| Sensación de tarjeta flotante | Bulto en el eje Z creado por múltiples capas de sombras | Sensación de jerarquía (solo para estilos de color claro) |

### Técnicas de Capa de Página

| Técnica | Alma Visual | Efecto |
|------|---------|------|
| Decoración de esquina | Delicado adorno de borde, como la esquina de un marco de fotos | Sensación de refinamiento |
| Línea divisoria desvanecida | Una línea fina que se desvanece en ambos extremos, como el horizonte en la niebla | Suave división del área |
| Marca de agua grande | Números/texto extragrandes con opacidad extremadamente baja, como un iceberg que se asoma en el océano | Reconocimiento de página |
| Subrayado de título | Banda horizontal corta de color de acento, como la "base" del título | Énfasis de título |
| Bloque de color de marca | Rectángulo redondeado grande de baja opacidad, como una burbuja en un trampolín | Marca de estilo |
| Encuadre de esquina HUD | Líneas cortas en forma de L en las cuatro esquinas del lienzo, como un visor / marcas de posicionamiento de un dibujo técnico | Sensación de tensión y precisión de estar siendo "observado" |
| Pie de página narrativo | Los números de página se convierten en parte de la historia (barra de estado de terminal/insignia de sello/escala de progreso) | Deja que los rincones funcionales también participen en la creación de la atmósfera |


---

## Optimización Tipográfica Multilingüe

### Escenario en Inglés

| Nivel | Predeterminado (Chino) | Ajuste (Inglés) | Razón |
|------|---------|---------|------|
| H0 Título de Portada | 48-56px | 44-52px | Las letras inglesas parecen visualmente más pequeñas que los caracteres chinos |
| H1 Título de Página | 28px | 26px | Igual que arriba |
| Body Texto Principal | 13-14px | 13px | 13px en inglés ya es bastante legible |
| Altura de línea | 1.8 | 1.6 | El inglés no necesita una altura de línea tan grande |
| Espaciado de letras | Predeterminado | `letter-spacing: 0.01em` | Ajuste fino para mejorar la legibilidad |

Pila de fuentes recomendadas para inglés:
```css
font-family: 'Inter', 'SF Pro Display', 'Segoe UI', system-ui, -apple-system, sans-serif;
```

### Idiomas Japonés y Coreano

| Idioma | Recomendación de Fuente |
|------|---------|
| Japonés | `'Hiragino Kaku Gothic ProN', 'Yu Gothic', 'Meiryo', system-ui, sans-serif` |
| Coreano | `'Apple SD Gothic Neo', 'Malgun Gothic', 'Nanum Gothic', system-ui, sans-serif` |

Las reglas tipográficas son las mismas que en chino (los caracteres CJK comparten características tipográficas similares).
