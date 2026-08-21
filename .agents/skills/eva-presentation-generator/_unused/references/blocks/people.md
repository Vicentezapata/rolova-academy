# people (Bloque de Personas) -- El Poder de los Rostros

> Tipos de datos aplicables: team_profiles / user_testimonials.
> Estructura: persons[]({name, title, avatar_desc, quote?}), de 3 a 6 personas por grupo.
> Puntos clave de diseño: Marcador de posición de avatar circular + nombre + cargo; las citas usan cursiva + letra pequeña. Cuando no haya fotos reales, use bloques de color degradado + iniciales.
> `card_style` recomendado: filled/outline. Disposición recomendada: symmetric / three-column.

## Estructura JSON
```json
{
  "card_type": "people",
  "title": "Equipo Central",
  "members": [
    {"name": "Nombre", "title": "Cargo", "bio": "Biografía (máx. 30 caracteres)", "avatar": true}
  ]
}
```

## Alma del Diseño

### Técnicas Dinámicas para Mostrar Personas
- **No hagas una libreta de direcciones**: 3-4 personas en fila espaciadas equitativamente + avatares del mismo tamaño + nombres y cargos con el mismo formato = la presentación de personas más aburrida.
- **Crea jerarquías**: Si hay una figura clave (ej. CEO / Fundador), haz que su avatar sea notablemente más grande que el de otros miembros (120px vs 80px), posicionado fuera del centro o dominando un lado.
- **Alineación irregular**: Las personas se pueden organizar de forma escalonada (sin equidistancia estricta), algunas tarjetas de personas pueden ser un poco más altas/más grandes, creando una sensación natural de respiración.
- **Historia de fondo**: Detrás de los avatares se pueden superponer gradientes sutiles / halos, sugiriendo el "tono personal" de cada individuo.

### Tratamiento de Avatares
- Recorte circular (border-radius:50% + overflow:hidden).
- Con avatar: borde color `accent` de 3px, creando una sensación de ser "seleccionado".
- Sin avatar: círculo de marcador de posición de iniciales (fondo `accent` + letra grande blanca).

### Jerarquía de Información
- Nombre 16px 700 centrado -- Lo más importante.
- Cargo 13px color `accent` -- Identidad.
- Biografía 12px secondary -- Lo menos importante, puede omitirse cuando falta espacio.

### `card_style` recomendado: `transparent` -- El componente de personas forma su estructura visual basándose en los rostros y la disposición misma.
