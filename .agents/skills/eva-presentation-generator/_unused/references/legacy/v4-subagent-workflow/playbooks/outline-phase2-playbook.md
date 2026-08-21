

## Objetivo

Una vez escrito el esquema, cambie inmediatamente a la perspectiva del revisor (QA/Quality Gatekeeper). Conciliar el `outline.txt` generado en la etapa anterior y su racionalidad lógica elemento por elemento.

---

## Revise estrictamente las reglas y actitudes (¡niéguese a ser moralista y superficial!)

- **Nunca lo dejes pasar fácilmente**: Está prohibido leerlo una vez y luego escribir "después de la inspección, la lógica es clara y pasó sin problemas", ¡este tipo de tonterías pretenciosas! ¡Eres un control de calidad exigente y cruel! No te mientas a ti mismo.
- **Debes encontrar los puntos débiles**: Después de leerlo por primera vez, si piensas "todo está bien", significa que no lo estás revisando en absoluto. ¿Ir a ver qué páginas tienen objetivos que parecen clichés? ¿Qué materiales simplemente no pueden respaldar la ambición? Sería negligente en su revisión sin sacar al menos una o dos espinas y hacer revisiones reales.
- **Modificar directamente sobre el archivo original**: No escribir una copia nueva. Si descubre que una determinada página no cumple con los estándares, modifique directamente la línea del `outline.txt` original.
- **Hasta 2 rondas de ciclos de corrección**: Descubra problemas -> Haga correcciones -> Vuelva a examinar la situación general.

---

## Lista de verificación de autoauditoría (9 elementos para control de acceso)

Debes realizar estas 9 comprobaciones en tu mente (o en tu registro de deducciones). Si suspendes alguno de ellos, no podrás entregar el trabajo:

| # | Artículos de inspección | Estándares estrictos | Métodos de tratamiento del fracaso |
|---|--------|------|-------------|
| 1 | **Alineación de páginas** | El número total de páginas incluidas en el esquema (sin contar las páginas virtuales, como los títulos de las partes, contando la "Página X"), debe ser estrictamente igual al número objetivo de páginas requeridas en los requisitos. | Eliminar páginas de agua/ampliar páginas secas |
| 2 | **Tamaño de pieza** | Cada Parte (excepto la primera y última portada/cta) debe estar respaldada por >= 2 páginas. | Si solo hay una página, significa que no es una parte independiente y debe fusionarse en otro lugar o expandirse. |
| 3 | **Parte Lógica** | Existen vínculos lógicos claros entre las partes (como progresión, causa y efecto) y no deben yuxtaponerse con temas del mismo nivel como una cuenta corriente. | Ajuste el orden de redacción de la parte o reescriba el objetivo de la parte. |
| 4 | **Honestidad de los datos** | "Fuente del material" Si está marcado como "verdadero", ¿realmente puede encontrarlo en resumen? | Si no lo encuentra, debe marcar "falso" e indicar dónde está el espacio. |
| 5 | **Enfoque único de una sola página (control de acceso fatal)** | El "destino de página" de cada página debe ser una oración. **¡Absolutamente no puede contener conjunciones como "y" y "y"! ** Intentar decir dos cosas en una página arruinará el diseño. | Dividido en dos páginas. |
| 6 | **Integridad del contrato de densidad** | El encabezado del esquema debe indicar "tendencia de densidad" y "curva de densidad"; cada página debe tener "límite inferior de densidad/objetivo de densidad/límite superior de densidad/acción rítmica/postura de información/tipo de anclaje". | Complete los campos que faltan y prohíba dejar el juicio de densidad a la improvisación en etapas posteriores. |
| 7 | **Legalidad de la ventana de densidad** | Cada página debe cumplir con el `límite inferior <= objetivo <= límite superior`; `portada/sección/fin` no debe ser `panel`; en el modo "ultra_dense", la página del búfer de contenido no puede volver a "bajo". | Reescribe el intervalo de densidad de la página correspondiente. |
| 8 | **Arco narrativo** | No todas las páginas son solo datos secos. ¿Existe algo "cercano" a la cognición precipitada? ¿Existe una "sección" para hacer la respiración? ¿Existe un flujo y reflujo rítmico en la combinación de roles narrativos (evidencia/comparación/proceso/cierre/cta)? | Ajuste la distribución de densidad de la combinación "Rol narrativo" en la página. |
| 9 | **Argumento del alma** | Todo el conjunto de PPT debe tener una tesis central final, no una oración sin sentido correcta. | Purifica el argumento. |

### Ley especial de densidad del hierro

- Desactivar 3 páginas consecutivas de "alto/panel"
- Debe haber al menos una página de transición que no sea del panel de control antes y después del "panel de control".
- El modo "relajado" desactiva el "panel de control"
- El modo "equilibrado" permite el "panel de control", pero sólo en pequeñas cantidades

---

## FINALIZAR Contrato de Firma

Sólo después de haber superado los siete autoexámenes se puede añadir una firma al final del documento y la tarea se declara completada.
El formato de firma es el siguiente (se adjunta al final del archivo):

```text
---
SELF_REVIEW_PASS
Rondas de auditoría：{你实际修改审查的次数}
自审时间：{YYYY-MM-DD HH:MM}
```
