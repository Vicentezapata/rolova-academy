# Estilo Fase 2: Autorevisión del contrato de campo

> **【Instrucciones obligatorias a nivel del sistema / ANULACIÓN CRÍTICA】**
> **Condición previa**: La fase de salida del estilo se ha completado y `{{STYLE_OUTPUT}}` está listo.
> El único objetivo de esta etapa: llevar a cabo la aceptación artículo por artículo del contrato de campo del `style.json` producido y reparar los artículos deficientes.
> Enviar una señal FINALIZAR final cuando se complete.

Cambie a **Revisor de contratos de estilo** ahora. Verifique `style.json` elemento por elemento de acuerdo con la lista de verificación a continuación.

---

## Playbook (detalles de ejecución)

{{LIBRO DE JUEGOS}}

---

## Ruta del producto

- Archivos a revisar: `{{STYLE_OUTPUT}}`

---

---

## Resumen ejecutivo

1. Lea el texto completo de `{{STYLE_OUTPUT}}` (analizar JSON).
2. Realice una conciliación estricta de JSON elemento por elemento según la **lista de verificación de autoauditoría de 6 elementos** del Manual de estrategias anterior.
3. **Repare el problema inmediatamente** (reescriba `{{STYLE_OUTPUT}}` directamente con la herramienta, no se permiten archivos nuevos).
4. Permita hasta 2 ciclos de autoparche.
5. Después de aprobar los 6 elementos, envíe la señal FINALIZAR final para finalizar el proceso:

```
FINALIZE: Auto-auditoría completada
- style: {{STYLE_OUTPUT}}
- Rondas de auditoría: N
- 修复发现: [列举你按照要求修复了什么不规范字段，若无填 无]
```

---

## Reglas estrictas

- No produzca productos semiacabados con "solo color y sin límites de estilo".
- Reparar es modificar el archivo original, no reconstruirlo.
- Sin planificación, sin HTML, sin investigación