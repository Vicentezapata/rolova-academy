# comparison (Bloque de Comparación) -- La Arena de Choque

> Tipos de datos aplicables: before_after / pros_cons / scenario_comparison / competitive_matrix.
> Estructura: Comparación cara a cara de doble panel, left+right contienen cada uno label, points[], configuración de color accent, y un verdict opcional en la parte inferior.
> Puntos clave de diseño: El plan recomendado de la derecha usa un color accent más fuerte + tamaño de fuente más grande + contenido más denso, el lado izquierdo usa colores neutros + tipografía sobria -- guiando visualmente a una conclusión.
> `card_style` recomendado: outline (separando suavemente los dos paneles). Disposición recomendada: symmetric.

## Estructura JSON
```json
{
  "card_type": "comparison",
  "title": "Método Tradicional vs Nueva Solución",
  "left": {"label": "Solución A / Situación Actual", "points": ["Dimensión 1", "Dimensión 2", "Dimensión 3"], "accent": "neutral"},
  "right": {"label": "Solución B / Objetivo", "points": ["Dimensión 1", "Dimensión 2", "Dimensión 3"], "accent": "primary"},
  "verdict": "Oración de conclusión inferior (opcional)"
}
```

## Alma del Diseño

### La Dramaticidad del Contraste
- Los dos paneles izquierdo y derecho no deben verse exactamente iguales solo con contenido diferente -- ese es el pensamiento de frontend web más rígido.
- Contraste con postura: Si el lado derecho es la "solución recomendada", haz que el panel derecho use un color `accent` más fuerte, tipografía más grande y contenido más denso, y el panel izquierdo use colores neutros + diseño moderado. Visualmente ya estás "guiando la conclusión".
- Contraste sin postura: Ambos paneles usan diferentes colores `accent` (accent-1 vs accent-2), pero la estructura es completamente simétrica.

### Técnicas Dinámicas
- El separador VS puede ser un bloque de color `accent` circular que cruza el eje central + el texto "VS", rompiendo la división física entre izquierda y derecha.
- Alinea las dimensiones de comparación verticalmente, permitiendo que la audiencia escanee horizontalmente para comparar, creando una sensación de tensión de "duelo punto por punto".
- El `verdict` (oración de conclusión) se centra cruzando ambos paneles, siendo el toque final donde "el árbitro anuncia el resultado".

### 3-5 Dimensiones de Comparación por Panel
- Muy pocas dimensiones (< 3) hacen una comparación insuficiente, demasiadas dimensiones (> 5) hacen que la pantalla esté saturada.
- `card_style` recomendado: `outline` -- un borde suave separa los dos paneles sin ocupar peso visual.
