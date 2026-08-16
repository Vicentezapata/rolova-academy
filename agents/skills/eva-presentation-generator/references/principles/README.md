#Principios de diseño PPT

> Estos son los principios subyacentes reconocidos en el mundo del diseño de presentaciones. Comprender el "por qué" le permite tomar decisiones correctas cuando no hay reglas específicas que lo cubran.

## Índice de principios

| Documentación | Principios Básicos | Fuentes/Teorías | Directrices de una frase para la planificación |
|------|---------|----------|------------------|
| `visual-jerarquía.md` | Jerarquía visual y CRAP | "Libro de diseño para todos" de Robin Williams | Solo puede haber un punto de anclaje visual en una página, y lo primero que ves cuando cierras los ojos y luego los abres debe ser la información más importante |
| `carga-cognitiva.md` | Carga cognitiva y densidad de información | Ley de Miller / Teoría del aprendizaje multimedia de Mayer | Cada página puede resumir la información central en una oración. Si se necesitan dos oraciones, la página debe dividirse |
| `composición.md` | Composición y espacios en blanco | Regla de los tercios / Psicología Gestalt | El espacio en blanco no es un desperdicio de espacio, el microespaciado <mesoespaciado <macroespaciado puede establecer un sentido de jerarquía |
| `color-psicología.md` | Psicología y Aplicación del Color | 60-30-10 Regla / Color Mapeo Emocional | Los colores de acento son condimentos, no el plato principal, máximo 2 acentos en la misma página, uso en área grande = ya no énfasis |
| `visualización-datos.md` | Principios de visualización de datos | Edward Tufte / Stephen Few | El objetivo de la visualización es permitir que la audiencia comprenda la conclusión en 3 segundos, no mostrar datos.
| `narrativa-arc.md` | Estructura narrativa y ritmo | Principio piramidal / SCQA / Arco narrativo | No 3 páginas consecutivas de alta densidad o 3 páginas consecutivas de baja densidad, ritmo ondulado para mantener la atención |

## Manual de operación (la base de la etapa de planificación)

| Documentación | Posicionamiento | Papel en la planificación |
|------|------|-------------|
| **`principios-de-diseño-cheatsheet.md`** | **6 principios principales -> planificación de guía de operación JSON a nivel de campo + hoja de examen físico de 8 elementos página por página** | **Paso 4 El elemento de lectura obligada número 0 en la subetapa de planificación en el enlace de producción de una sola página. Un mensaje de una sola página inyecta el contexto de ejecución antes de planificar la ejecución. No le dice a LLM "qué es un buen diseño", sino "cómo completar cada campo JSON es un buen diseño", "qué campo se debe cambiar cuando es incorrecto y a qué valor se debe cambiar". ** |

> El manual de instrucciones no sustituye a los 6 documentos principales. Manual de operación = "Cómo operar campos JSON", documento de política = "Por qué necesitamos operar de esta manera". Cuando encuentre casos extremos que no estén cubiertos por el manual de operación, regrese al documento principal correspondiente para comprender la lógica subyacente antes de emitir un juicio.

## Cuando leer

- **Paso 4 Enlace de una sola página antes de ingresar a la planificación**:
  1. **Lea primero** `design-principles-cheatsheet.md` (Debe leerse el elemento número 0, la base de la planificación)
  2. Luego lea `references/principles/README.md` (este documento) para establecer el conocimiento de los principios.
- **Paso 4 Etapa de reparación de revisión de imagen/HTML de la misma página**: cuando tenga dudas en la toma de decisiones de diseño, lea el archivo principal correspondiente a pedido
- No es necesario leer los 6 archivos de políticas cada vez; el manual de operación ya cubre orientación específica a nivel de campo JSON

## Relación con reglas específicas

```
原则层（principles/*.md）                    = "为什么这样做"             -> 理解动机
  └─ 操作手册（cheatsheet）                 = "planning JSON 字段怎么定"  -> 逐页执行 + 逐页体检
运行规则层（page-agent prompt / playbook）  = "planning 与 HTML 怎么落地" -> 执行约束
组件层（blocks/charts/layouts）             = "用什么组件/图表/布局"      -> 工具选择
```

Los principios guían el manual de operación, el manual de operación guía cómo completar la planificación JSON y la planificación JSON luego impulsa la generación de HTML. El manual de operaciones es el puente entre los principios y la ejecución, y traduce la teoría del diseño abstracto en instrucciones de operación de campo que LLM puede ejecutar con precisión.