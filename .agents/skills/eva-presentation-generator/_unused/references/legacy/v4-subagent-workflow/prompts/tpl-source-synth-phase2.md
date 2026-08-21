# SourceSynth Fase 2: Autoauditoría de calidad y verificación de límites

> **【Instrucciones obligatorias a nivel del sistema / ANULACIÓN CRÍTICA】**
> **Condición previa**: La fase de extracción de datos se ha completado y `{{BRIEF_OUTPUT}}` está listo.
> El único objetivo de esta etapa: realizar un estricto autoexamen del `source-brief.txt` generado y corregir los elementos deficientes.
> Enviar una señal FINALIZAR final cuando se complete.

Ahora pasará al rol de revisor de calidad: realice la aceptación artículo por artículo del `source-brief.txt` que acaba de producir.

---

## Playbook (detalles de ejecución)

{{LIBRO DE JUEGOS}}

---

## Ruta del producto

- Documentos a revisar: `{{BRIEF_OUTPUT}}`
- Archivo de requisitos (referencia): `{{REQUIREMENTS_PATH}}`

---

## Lista de verificación de autoauditoría (confirmar elemento por elemento, no omitir)

| # | Consultar artículos | Estándar | Método de reparación si falla |
|---|--------|------|----------------|
| 1 | Etiqueta fuente | Cada dato tiene una etiqueta de nombre de archivo fuente | Fuente complementaria |
| 2 | Conflictos de datos | Registre los datos contradictorios con sinceridad (no se puede elegir uno para ignorar el otro) | Complemente los datos contradictorios que faltan |
| 3 | Límites materiales | Marque claramente la cobertura de elementos completos, faltantes o contradictorios | Complementar declaraciones de límites |
| 4 | Declaración de modo estricto | Si es modo estricto, debe haber una declaración de modo estricto | Declaración adicional |
| 5 | Paquete de datos PPTX | Contiene fragmentos individuales `## Paquete de datos estructurados PPTX` | Extraído y formateado del contenido existente |
| 6 | Cobertura de tipos de datos | El paquete de datos estructurados cubre al menos 3 tipos | Revisar los datos originales para realizar extracciones adicionales |
| 7 | Números precisos | Nada de expresiones vagas como "ha crecido mucho" | Volver al texto original para complementar los números exactos |
| 8 | Evaluación de cobertura de datos | Hay estadísticas de cobertura + brecha por tipo al final del paquete de datos | Evaluación complementaria |

---

## Proceso de ejecución

1. Lea el texto completo de `{{BRIEF_OUTPUT}}`
2. Consulte la lista de verificación anterior elemento por elemento.
3. **Repare el problema inmediatamente** (cámbielo directamente a `{{BRIEF_OUTPUT}}` sin escribir otra copia)
4. Repase la lista de verificación nuevamente después de la reparación (máximo 2 rondas)
5. Envíe el FINALIZAR final después de que se haya pasado todo:

```
FINALIZE: Auto-auditoría completada
- brief: {{BRIEF_OUTPUT}}
- Tipos de datos cubiertos: [Lista de tipos cubiertos]
- Brechas de cobertura: [Breve descripción]
- Rondas de auditoría: N
```

## Reglas estrictas

- Sin búsqueda complementaria
- No agregar datos que no existen en el perfil (el modo estricto es más estricto)
- Reparar es modificar el archivo original, no reconstruirlo.