# Metodología Central

> Fuente: LINUX DO Foro Sandun Compartido (7 años de enseñanza PPT + 3 años de experiencia en productos de IA)

## Argumento Central

> El alma de un PPT es el contenido, no la apariencia.

## Puntos Clave de la Metodología

### 1. Empieza con el problema, no con la plantilla

Pregunta primero: ¿Para quién es? ¿Por qué se hace? ¿Qué quieres que la otra parte recuerde? ¿Cuáles son los hechos que no se pueden equivocar?

Esto no es una pérdida de tiempo -- una definición precisa de los requisitos puede duplicar la calidad de todos los pasos posteriores. Las empresas profesionales de PPT cobran más de 10,000 por página, de los cuales al menos el 30% del valor proviene de la investigación de requisitos.

### 2. Contenido primero, diseño después

Pospón el diseño exquisito hasta que la línea argumental pueda soportar el escrutinio. En la etapa de borrador de planificación, solo verifica la estructura de la información.

Por qué esto es importante: Si descubres que hay problemas con la lógica del contenido después de completar el diseño, el costo de modificación es 5-10 veces mayor que en la etapa de planificación. Primero usa un borrador de texto de bajo costo para verificar la estructura y, una vez confirmado, invierte recursos de diseño.

### 3. Insertar la capa intermedia del borrador de planificación

Las herramientas típicas saltan directamente del esquema al producto terminado. Este método inserta un producto intermedio:
- **El propósito de cada página**: ¿Qué es lo que más quieres que la audiencia recuerde en esta página?
- **Información central**: Título + contenido de la tarjeta principal + puntos destacados de datos
- **Soporte de evidencia**: Datos reales obtenidos de la búsqueda
- **Formato de layout**: Cuántas tarjetas, qué tipos, cómo se organizan
- **Relación jerárquica**: Distinción clara entre principal y secundario, no toda la información es plana

Esta es la mayor mejora práctica de calidad. El borrador de planificación es el "cimiento"; sin un cimiento sólido, un diseño por muy hermoso que sea es solo un castillo en el aire.

### 4. Usa un lenguaje de diseño que el modelo pueda entender

El diseño basado en tarjetas Bento Grid es el lenguaje de diseño más fácil de entender y dominar para la IA:
- Define la página como tarjetas, contenedores, jerarquías y espaciados
- Deja que el contenido impulse la selección del diseño (en lugar de elegir una plantilla y rellenarla con palabras)
- Proporciona reglas claras de tamaño/espaciado/énfasis

Por qué elegir Bento Grid sobre el diseño tradicional de diapositivas: El diseño tradicional de PPT es demasiado libre, y la IA tiende a "dibujar torcido". El diseño de tarjetas viene inherentemente con restricciones de cuadrícula, y el rendimiento de la IA dentro de estas restricciones es en realidad mejor -- así como es más fácil escribir una obra maestra en un soneto que en verso libre.

### 5. Utilizar salidas estructuradas entre fases

Utiliza JSON como formato de transferencia de datos para cada paso, en lugar del lenguaje natural:
- Requisitos -> JSON de descripción de requisitos
- Búsqueda -> JSON de colección de materiales
- Esquema -> JSON de PPT_OUTLINE
- Planificación -> Array JSON de tarjetas de planificación
- Diseño -> Archivo HTML

La ventaja de JSON es **no tener ambigüedad**. El lenguaje natural sufre pérdida de información durante la transmisión, mientras que cada campo en JSON tiene un significado exacto y el siguiente paso puede leerlo con precisión.

### 6. La coherencia se garantiza mediante estilos compartidos

Primero establece el estilo (colores/fuentes/decoraciones), luego généralos en lotes como si "produjeras bloques de Lego".
Cada página comparte el mismo conjunto de definiciones de variables CSS, asegurando que el lenguaje visual de las 15 páginas del PPT esté completamente unificado.

### 7. Relleno de datos reales, eliminación de alucinaciones

La queja más común sobre los PPT de IA es "contenido vacío y con demasiadas tonterías". La causa raíz es que no hay datos reales que lo respalden.

Este método resuelve este problema a través del Paso 2 (Búsqueda de materiales): Buscar primero y luego generar, para que cada punto de datos tenga una fuente. Es mejor poner menos información que inventar un dato.
