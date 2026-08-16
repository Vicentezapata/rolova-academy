# SourceSynth Phase 1 Playbook: lectura de datos y extracción estructurada

## Objetivo

Extraiga los materiales existentes (documentos, textos, tablas de datos, PPT, etc.) proporcionados por los usuarios en resúmenes de materiales estructurados `source-brief.txt`, para que puedan consumirse de manera estable en las etapas de esquema y planificación.

---

## Identificación de estrategia (basada en requisitos)

Identifique sus patrones de lectura y extractos del campo "Política de uso de materiales" en "requirements-interview.txt":



---



Cuando se encuentran archivos de referencia en diferentes formatos, se extraen según las siguientes prioridades:

| Formato | Procesamiento | Extracción de claves |
|------|---------|---------|
| PDF | Analizar con lector de pdf o markitdown | Datos del gráfico, párrafo de conclusión, citas a pie de página |
| Palabra (.docx) | Convertir con markitdown y leer | Estructura del capítulo, argumentos centrales, tablas integradas |
| Excel (.xlsx) | Utilice Markitdown para convertir y leer | Tabla de datos->convertir directamente al formato de paquete de datos estructurados |
| PowerPoint (.pptx) | Utilice Markitdown para extraer texto y estructura | Título de cada página + viñetas, notas del orador, gráficos de datos |
| Texto sin formato/Rebajas | Lectura directa | Extracción por fragmentos semánticos |
| Archivos de código | Lectura directa | Descripción de la arquitectura, comentarios, descripciones en README |
| Fotos | Utilice el reconocimiento de imágenes para describir el contenido | Datos de gráficos, contenido de capturas de pantalla, elementos de marca |

---

## Armas narrativas y búsqueda de inspiración (misión principal: el contenido es el rey y la granularidad)

PPT es una herramienta para contar historias. No recomendamos extraer datos secos por el bien del "contenido de diseño", ¡pero esto no significa que pueda ser perezoso y solo dar una conclusión macro! **
Después de leer detenidamente la información, está absolutamente prohibido utilizar conclusiones vacías como "la situación es buena" o "hay muchos puntos débiles" para comentarios superficiales. Debes profundizar en la línea de negocios y descubrir armas de contenido con una granularidad extremadamente alta como un detective.



### 1. Armas narrativas de alta granularidad (extraídas primero, deben implementarse de manera concreta)
- **Excelente metáfora/analogía**: Una oración que puede hacer que conceptos complejos se entiendan en un segundo (debe traer el contexto específico del escenario original).
- **Puntos débiles y trampa de empatía**: debe ser específico de los detalles comerciales negativos, reales y de carne y hueso, de "qué vínculo y por qué razón llevó a la pérdida de incluso una hora más".
- **Frases de oro para la reducción de dimensionalidad**: conclusiones centrales con una penetración extremadamente fuerte (adjunte lógica deductiva, no se limite a gritar eslóganes).
- **La resistencia detrás del proceso**: no solo extrae el paso 123, sino también "por qué este paso es extremadamente difícil" y descubre obstáculos específicos.

### 2. La piedra angular de los datos estructurados (si la hay, hay que aprovecharla para enriquecer la carne y la sangre)
¡Todavía es necesario permanecer sensible a la evidencia! Siempre que haya datos nativos en los datos, se deben capturar en el siguiente formato y no se deben perder:
- `métricas`: características numéricas básicas `10% (aumento)`
- `before_after`: comparación antes y después extremadamente contrastante
- `líneas de tiempo`: momentos clave
- `expert_quotes`: nombres específicos y citas originales

En resumen: **¡Rechace las macroconclusiones falsas y vacías! ¡Sea específico! ¡Trae detalles! **

---



Complete toda la información y envíela a la ruta de destino de acuerdo con la siguiente estructura. No revise ni repare en esta etapa:

```text
# 资料摘要

## 基本信息
- 来源类型：用户现有资料（非联网搜索）
- 资料文件数：N
- 覆盖主题：...

## 核心论点与数据
（按主题分组，每条数据标注来源文件名）

### [主题1]
- [论点/数据] — 来源：[文件名]
- ...

## 关键数据清单
（所有可被直接引用的数据、统计、案例）
- [数据] — 来源：[文件名]

## 优质叙事武器库（金句/痛点/类比/洞察）
- [极具张力的洞察]
- [有画面感的比喻]

## PPTX 结构化数据包
（仅当资料库内确实有这些结构化信息时提取）
- [数据点/对比/图表化骨架]

## 素材边界
- 覆盖完整的内容：...
- 资料中缺失的内容（PPT 可能需要但资料未覆盖）：...
- 数据矛盾项（如果有多个文件数据打架）：...

## 资料使用建议
- 强论据（直接引用）：...
- 辅助背景（间接参考）：...
```
