# quote (Bloque de Citas) -- El Ancla del Alma

> Tipos de datos aplicables: expert_quotes / user_testimonials. Cita en comillas grandes suspendida de forma independiente.
> Estructura: quote_text + attribution(name, title, organization).
> Puntos clave de diseño: Comillas decorativas gigantes (font-size:120px, opacity:0.1), texto de la cita font-size:28-36px, atribución font-size:14px.
> `card_style` recomendado: transparent (el texto sostiene la imagen por su propia gravedad), máximo 1 tarjeta de cita por página.

## Estructura JSON
```json
{
  "card_type": "quote",
  "content": "Contenido de la cita (50-150 caracteres)",
  "attribution": {"name": "Nombre de la Persona", "title": "Cargo / Organización"},
  "avatar": true
}
```

## Alma del Diseño

### El Peso Visual de la Cita
- El texto de la cita usa 24-28px, font-weight:500, line-height:1.6 -- haciendo que cada palabra tenga peso.
- La decoración de comillas usa un `div` enorme (carácter `"` de 80-120px), color `accent` con muy baja opacidad (10-15%), como una marca de agua gigante que realza el texto desde atrás.
- Necesita una gran cantidad de espacio en blanco alrededor de la cita -- el espacio en blanco es la invitación silenciosa a "por favor, escuche con atención".

### Variaciones de Expresión Dinámica
- **Estilo de línea vertical izquierda**: Una línea vertical `accent` de 3px a lo largo del lado izquierdo del texto, con la información de origen debajo. Solemne, con autoridad.
- **Estilo de suspensión central**: El texto de la cita está centrado con mucho espacio en blanco alrededor, comillas gigantes desplazadas en el fondo. Poético, emocional.
- **Estilo de tensión excéntrica**: El texto de la cita se apoya hacia un lado de la pantalla, con un gran espacio en blanco + información de la fuente en el otro lado. Dinamismo asimétrico.

### Información de la Fuente
- Avatar (recorte circular de 48px) + Nombre (16px 700) + Cargo (13px secondary).
- La información de la fuente debe ser visiblemente más débil que el texto de la cita -- la audiencia lee la cita primero y luego mira quién lo dijo.

### `card_style` recomendado: `transparent` -- La cita expuesta en el vacío, sosteniendo la pantalla solo con la gravedad de sus palabras.
