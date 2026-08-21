# Reglas de tiempo de ejecución del comando Director

> Este archivo es el documento de reglas `director_command` dedicado a la cadena principal del tiempo de ejecución del Paso 4.
>
> Solo define responsabilidades de campo, límites de escritura, reglas de selección y modos de falla. No proporciona una biblioteca de muestra ni guiones de lentes terminados.

---

## 1. Posicionamiento de funciones

- Ayudar a la planificación a traducir los roles de la página en instrucciones de diseño ejecutables.
- Deje que `director_command` proporcione dirección en lugar de escribir la página para la capa HTML.
- Garantizar una división estable del trabajo entre campos y evitar que la prosa devore la estrategia espacial.

---

## 2. Responsabilidades de campo

### `estado de ánimo`

- Describir el estado de lectura y la atmósfera crítica que debe establecer esta página.
- Describa únicamente la intensidad semántica y la dirección de la atmósfera, no escriba eslóganes de marketing ni detalles de imágenes.

### `estrategia_espacial`

- Describir el esqueleto de la página, áreas primarias y secundarias y distribución del centro de gravedad.
- Debe responder dónde están los puntos de anclaje, dónde está el contenido de soporte, cómo participa el espacio en blanco en la estructura.
- No escriba HTML, DOM, coordenadas específicas o nombres de clases específicos.

### `tratamiento_ancla`

- Describir cómo se enfatiza, restringe y sostiene el ancla principal.
- Solo se escriben los principios de procesamiento del punto de anclaje y no se escribe el guión completo del truco decorativo.

### `técnicas`

- Selecciona sólo los números de técnica que realmente necesitas.
- El número debería ser limitado; es necesario explicar cómo estas técnicas sirven a la misión de esta página, en lugar de llenarse de números.

### `prosa`

- Responsable de complementar la intención del diseño que no se expresa plenamente en los campos anteriores.
- Sólo puedes explicar "por qué está organizado así", no puedes escribir directamente la página como una descripción del producto terminado.



## 3. Reglas de escritura

- "mood" debe ser breve, preciso, estable y puede ser utilizado por HTML posterior como dirección de diseño.
- `spatial_strategy` debería girar en torno a relaciones estructurales, no a un lenguaje performativo.
- `anchor_treatment` debe enfatizar la relación entre el ancla principal y el soporte, no expresiones exageradas.
- Se debe priorizar que las "técnicas" sean pocas y efectivas, y evitar reemplazar el criterio de diseño por el número de técnicas.
- La "prosa" debe obedecer el contrato de la página y no puede anular el diseño, la función de la tarjeta ni el presupuesto de contenido.





### prosa escribiendo un guión de crecimiento

- Condición desencadenante: "prosa" describe directamente la apariencia específica del producto terminado.
- Señales de fallo: La capa HTML simplemente se copia, sin margen para la discreción del diseño.
- Secuencia de reparación: reciclar la descripción del producto terminado en objetivos estructurales, rutas de lectura e intenciones rítmicas.

### `spatial_strategy` está escrito como HTML

- Condición de activación: DOM, nombre de clase, CSS concreto o implementación elemento por elemento aparece en el campo.
- Síntomas de fracaso: la planificación se excede en su autoridad y escribe la implementación para el diseño.
- Orden de reparación: eliminar detalles de implementación, conservar solo la estructura y la descripción del enfoque.

### El "estado de ánimo" se convierte en un eslogan de marketing



### Las `técnicas` están acumuladas pero no tienen prioridad.



