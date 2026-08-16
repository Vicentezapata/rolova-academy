# diagram (Bloque de Diagrama) -- El Mapa Estelar de la Estructura

> Tipos de datos aplicables: hierarchies (jerarquías) / architecture_diagram (diagramas de arquitectura) / cycle_flow (flujos cíclicos) / decision_tree (árboles de decisión) / pyramid_layers (capas piramidales) / stakeholder_map (mapas de stakeholders).
> Estructura: nodes[] (nodos) + edges[] (líneas de conexión), soporta cuatro modos de diseño: layered (en capas) / radial / tree (árbol) / flowchart (diagrama de flujo).
> Implementación ilimitada: Cajas anidadas con CSS Grid, nodos y líneas de conexión con SVG en línea, o líneas de conexión con Flexbox + pseudoelementos.
> `card_style` recomendado: transparent (tiene su propio esqueleto visual, los cuadros alrededor solo interferirán). Diseño recomendado: single-focus / t-shape.

## Estructura JSON
```json
{
  "card_type": "diagram",
  "diagram_type": "pyramid | flowchart | hub-spoke | layers | cycle",
  "nodes": [
    {"id": "1", "label": "Nombre del Nodo", "description": "Descripción (hasta 20 caracteres)", "level": 1, "connects_to": ["2","3"]}
  ]
}
```

## Pensamiento de Diseño Dinámico por Subtipo

| diagram_type | Alma Visual | Técnica Dinámica |
|-------------|---------|---------|
| pyramid | Orden jerárquico firme | Los bloques de las capas inferiores son opacos, las capas superiores cambian gradualmente a translúcidas o a contornos, atrayendo la mirada hacia la cima. |
| flowchart | Conexión lógica fluida | Nodos de estado (filled) vs. Nodos de decisión (outline). Las líneas de conexión usan animaciones sutiles tipo "hormigas marchando" o colores de acento para guiar el flujo. |
| hub-spoke | Gravedad central (Modelo Hub-Spoke) | El nodo central usa `accent` (núcleo ardiente) o `elevated` (tamaño grande), los nodos circundantes usan `transparent` o texto pequeño, unidos por líneas radiales extremadamente finas. |
| layers | Acumulación arquitectónica (Capas) | Perspectiva isométrica o superposición en el eje Y. Usa sombras superpuestas o texturas `glass` para enfatizar la relación "arriba/abajo". |
| cycle | Ciclo sin fin | Diseño circular, flechas superpuestas. Solo un nodo clave usa un color brillante, el resto se desvanece, rompiendo el aburrimiento de una rueda de colores uniforme. |

## Interacción Avanzada y Arquitectura de CSS
- **SVG en Línea (Recomendado)**: Se recomienda generar un `<svg>` en línea y ubicar los nodos usando SVG `<foreignObject>` para un control absoluto sobre las curvas de conexión y flechas.
- **Micro-interacciones**:
  - Al pasar el ratón sobre un nodo (Hover), resaltar las conexiones adyacentes (`edges`) y oscurecer el resto del diagrama (enfoque en la ruta).
  - Animación de entrada: Los nodos aparecen en un efecto de onda (ripple) en orden de nivel (`level`), no todos a la vez.
