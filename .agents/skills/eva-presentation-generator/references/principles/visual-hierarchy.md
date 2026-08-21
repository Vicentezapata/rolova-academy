# Jerarquía visual y principios CRAP

> El ojo humano no lee palabra por palabra, sino que salta y escanea según el peso visual. La tarea principal del diseño es utilizar medios visuales para controlar el orden de lectura.
> Campos afectados: `visual_weight`, `cards[].role`, `cards[].card_style`, `director_command.anchor_treatment`.
> El diseño de varias tarjetas y las páginas que requieren un sentido de jerarquía deben hacer referencia a este principio; cubriendo los cuatro principios de CRAP, contraste, alineación, repetición e intimidad.

## Los cuatro principios del CRAP (Robin Williams)

### Contraste
- **Principio**: Cuanto mayor sea la diferencia, más clara será la jerarquía. Los elementos similares se consideran hermanos.
- **Aplicación PPT**: Hay al menos una diferencia de tamaño de fuente de 2 niveles entre el título y el texto; enfatice los datos con color de acento en lugar de negrita; use diferente card_style para tarjetas en diferentes niveles (diferente "sensación de presencia espacial")
- **Errores comunes**: Hay una ligera diferencia de tamaño entre el título y el texto principal (no se puede ver la jerarquía); todo el texto está en negrita (equivale a no estar en negrita); todas las tarjetas usan el mismo card_style

### Repetición
- **Principio**: Reutilizar los mismos elementos visuales para crear una sensación de unidad y previsibilidad.
- **Aplicación PPT**: todas las páginas utilizan el mismo conjunto de variables CSS (los genes de color son consistentes); un sistema que mantiene técnicas de decoración de títulos consistentes en todas las páginas; el "ADN" del estilo recorre todo el artículo
- **Errores comunes**: use diferentes estilos decorativos en cada página (parece un mosaico); el estilo carece de un gen unificado
- **Smart Balance**: La repetición es "unidad genética", no "todas las páginas tienen la misma longitud". Bajo la premisa de que los genes son consistentes, el diseño, la combinación de estilo de tarjeta y los detalles decorativos de cada página deben cambiar de manera flexible.

### Alineación
- **Principio**: Ningún elemento de la página se coloca al azar, cada elemento debe tener una conexión visual con otros elementos.
- **Aplicación PPT**: use CSS Grid para una alineación estricta (en lugar de posicionamiento absoluto para adivinar coordenadas); espaciado uniforme entre tarjetas; alineación uniforme (la alineación a la izquierda es la opción más segura)
- **Smart Balance**: la alineación es la regla, pero romper deliberadamente la alineación también puede ser un método de diseño inteligente. La clave es "alineación consciente" o "desalineación consciente"; ambas son mejores que la "desalineación inconsciente".

### Proximidad
- **Principio**: La información relevante está cerca y la información irrelevante está lejos. El espaciado transmite relaciones
- **aplicación PPT**: los elementos dentro de la misma tarjeta están muy juntos (el espacio entre el título y el texto es menor que el espacio entre las tarjetas); hay un claro gradiente en el espacio entre los diferentes niveles
- **Smart Balance**: el espaciado no tiene por qué ser constante para siempre. Puede utilizar una gran cantidad de espacio en blanco para "aislar" un elemento central y crear una sensación dramática de respiración; esta es la "aplicación inversa" del principio de intimidad para crear un ancla visual.



Peso visual de mayor a menor (referencia aproximada, valor no fijo):

```
超大数据(64px+) > 页面标题(28px+) > 配图 > 卡片标题(16-20px) > 数据数字(36px+) > 正文 > 标注/注释
```

**Solo un ancla visual en una página**: el elemento que primero llama la atención. Si dos elementos compiten por el anclaje (como dos números de gran tamaño uno al lado del otro), el público no sabrá cuál mirar primero.

##Autoprueba

- Cierra los ojos y luego ábrelos nuevamente. ¿El primer elemento que ves es la información más importante de la página?
- ¿Puedes identificar la estructura jerárquica de una página en 3 segundos?
- ¿El sistema visual es consistente al pasar las páginas (no un estilo por página)?
- ¿Hay algún cambio inteligente deliberado para que cada página sea visualmente nueva?