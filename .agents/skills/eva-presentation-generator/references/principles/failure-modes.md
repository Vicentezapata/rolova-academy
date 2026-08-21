# Modos de falla en tiempo de ejecución

> Este documento precipita el modo de falla del enlace de producción de una sola página del Paso 4-5. **Define el incumplimiento del contrato y la secuencia de reparación, no define un estilo estético determinado y no suprime la innovación**.
>
> Fuente de inspiración: [runtime-failure-modes of sunbigfly/ppt-agent-skills](https://github.com/sunbigfly/ppt-agent-skills/blob/main/references/principles/runtime-failure-modes.md)

---

## 1. Contenido sin terminar (4 tipos)

### 1.1 subllenado (la densidad de información es demasiado baja)

- **Condición de activación**: la visión de la página está establecida, pero la carga útil es obviamente insuficiente.
- **Signos de fallo**: La densidad de información en una sola página es demasiado baja, con mucha más decoración que información efectiva; la tarjeta tiene demasiado espacio en blanco pero ningún contenido explicativo.
- **Zona de innovación permitida**: puedes cambiar la composición, pero no puedes usar espacios en blanco para reemplazar el contrato de contenido.
- **Reparación**: complemente datos/casos/interpretaciones de los materiales originales para completar la densidad de la tarjeta principal de 40 a 100 palabras requerida en el borrador de planificación.

### 1.2 support_collapse (colapso de tarjeta de soporte)

- **Desencadenante**: Las tarjetas de apoyo no contienen explicación, comparación, evidencia o contexto.
- **Signos de fallo**: La página sólo tiene el título principal y uno o dos números grandes, y carece de una capa de soporte.
- **Zona de Innovación Permitida**: El formulario de soporte (lista/datos/proceso/cotización) se puede cambiar, pero las tareas de soporte deben completarse.
- **FIX**: ≥ 3 tarjetas + ≥ 2 tipos de tarjetas + ≥ 1 tarjeta de datos por página de contenido.

### 1.3 payload_missing (falta información clave)

- **Condición desencadenante**: la planificación o HTML no implementa completamente la información que esta página debería ofrecer.
- **Señal de fracaso**: El reclamo clave no tiene evidencia, pasos, condiciones o fuentes para realizar.
- **Zona de innovación permitida**: el contenido se puede reorganizar, pero los campos necesarios no se pueden omitir.
- **Solución**: compare el campo `cards[]` del borrador de planificación JSON y complete los campos uno por uno.

### 1.4 source_overclaim (la afirmación excede el soporte de datos)

- **Condición de activación**: la conclusión de la página es más sólida que el soporte de datos.
- **Signos de error**: la afirmación parece completa, pero el paquete de búsqueda del Paso 2 no tiene pruebas suficientes.
- **Zona de innovación permitida**: Se puede fortalecer el ritmo de expresión, pero no se pueden exagerar los límites de los hechos.
- **Corrección**: Debilitar la redacción de la conclusión o completar la búsqueda (por ejemplo, "Se espera que se convierta en una" reforma "en la industria X").

---

## 2. Tipo de distorsión visual (4 tipos)

### 2.1 launch_drift (derivación del estilo de apertura)

- **Condición de activación**: la portada o la página del capítulo hace que toda la presentación adquiera un tono de conferencia que no coincide con el contenido.
- **Signos de fracaso**: Es difícil aceptar páginas de información posteriores y el sesgo de estilo continúa ampliándose.
- **Zona de Innovación Permitida**: Puedes fortalecer la apertura, pero debe obedecer al modo de escena (presencial/autolectura/entrenamiento) y audiencia.
- **Solución**: verifique la escena de demostración en el Paso 1; si se trata de un "documento de lectura automática", la portada debe ser discreta y no escénica.

### 2.2 Anchor_overexpansion (sobreexpansión del punto de anclaje)



### 2.3 deck_rhythm_clone (clon de ritmo)

- **Condiciones de activación**: varias páginas utilizan diseño isomórfico, decoración isomórfica y relaciones de puntos de anclaje isomórficos.
- **Signos de fracaso**: El mazo tiene unidad pero no progresión rítmica.
- **Zona de innovación permitida**: los sistemas se pueden replicar, pero los resultados no se pueden replicar.
- **Solución**: consulte el principio de "alternancia de densidad" de SKILL.md: una página de alta densidad (cuadrícula híbrida) seguida de una página de baja densidad (portada de capítulo), formando un ritmo relajado.



- **Condiciones desencadenantes**: utilice materiales, efectos de luz y divisores para reemplazar la organización de la información real.
- **Signos de falla**: La página parece complicada, pero la capacidad real de carga de información se reduce.
- **Zona de innovación permitida**: los materiales se pueden reforzar, pero no pueden asumir tareas estructurales.
- **Solución**: Eliminar el elemento "decoración por decoración"; Pregúntese: "Si elimina esta decoración, ¿se perderá la información de la página?", si no, elimínela.

---

## 3. Reparar la ley de hierro de la secuencia.

Las correcciones se realizan en el siguiente orden, **no se deben omitir los dos primeros pasos**:

1. **Completa la carga útil primero** (el contenido es la base)
2. **Añadir soporte y contexto** (la tarjeta es el soporte)
3. **Recorrija la proporción y posición del ancla** (Lo visual es narrativo)
4. **Ajuste final de materiales, decoración y expresión local** (la decoración es el toque final)

Los ajustes cosméticos no se pueden utilizar para cubrir contratos de contenido faltantes.

---



- Se permite que la innovación ocurra en: composición, ritmo, combinación decorativa, expresión de puntos de anclaje y jerarquía de materiales.
- El modo de error solo restringe los valores predeterminados, no los experimentos de estilo.
- Siempre que el contrato de contenidos esté completo, la ruta de lectura sea clara y el sistema de estilos sea estable, se permite una exploración muy diferenciada de la página.

---

## 5. Detectar sugerencias automáticamente

`scripts/smoke_test.py` detecta automáticamente modos de falla parcial a través de la siguiente heurística:

| Modos de falla | Heurísticas de detección |
|---------|----------|
| subllenado | Número total de palabras en una sola página < 80 (excluyendo portada/portada de capítulo) |
| soporte_collapse | Cantidad de tarjetas de página de contenido < 3 o tipo de tipo de tarjeta < 2 |
| anclaje_sobreexpansión | Una sola tarjeta ocupa un área > 65% |
| sustitución_decorativa | Número de divs decorativos > Número de divs de texto × 1,5 |
| deck_rhythm_clone | Utilice el mismo layout_hint para más de 3 páginas consecutivas |

Otros modos de falla (payload_missing, source_overclaim, launch_drift) requieren una intervención de control de calidad manual o visual.