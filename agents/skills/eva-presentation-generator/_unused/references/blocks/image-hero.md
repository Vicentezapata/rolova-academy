# image_hero (Imagen Grande + Bloque de Texto Superpuesto) -- Inmersión Visual

> Tipo de datos aplicable: image_candidates. Imagen a sangría completa + texto superpuesto, creando impacto emocional.
> Estructura: Debe especificar image.usage(hero-background/inline-illustration) + image.placement(full-bleed/left-half) + image.content_description.
> `card_style` recomendado: transparent/glass (la imagen grande no necesita un límite de borde, o usar vidrio esmerilado para que el texto flote sobre la imagen).
> Tipo de página aplicable: páginas de atmósfera como cover / section. Máximo 1 image_hero por página.

## Estructura JSON
```json
{
  "card_type": "image_hero",
  "title": "Título Principal (28-44px)",
  "subtitle": "Descripción Complementaria (hasta 80 caracteres, opcional)",
  "image_prompt": "Descripción de la imagen (usada para generar la imagen)",
  "data_highlights": [{"value": "87%", "label": "Penetración de Mercado"}]
}
```

## Alma del Diseño

### La imagen es el protagonista, el texto es flotante
- La imagen usa `object-fit:cover` para cubrir toda el área -- la imagen es el marco mismo, no una decoración "colocada" en alguna posición.
- La capa de máscara usa un `<div>` real con un gradiente semitransparente (prohibido usar mask-image) -- el propósito de la máscara es hacer que el texto sea legible sobre la imagen, no ocultar la imagen.
- La capa de texto flota sobre la imagen. El título usa una fuente grande para garantizar el impacto, y el subtítulo y los datos destacados usan fuentes pequeñas para mantener la moderación.

## Técnicas Dinámicas
- **Fusión de Desvanecimiento**: La imagen se desvanece gradualmente de un lado (ej. lado derecho) al otro, y el texto reside en el área desvanecida. La imagen y el texto no son dos capas separadas, sino que se integran en una sola imagen.
- **Surgiendo desde Abajo**: La imagen cubre el 70% superior, y el texto surge de una zona oscura con gradiente en el 30% inferior. Como la tipografía del título de un póster de película.
- **Susurro en la Esquina**: La imagen cubre todo el área, y el texto se acurruca muy pequeño en una esquina, permitiendo que el poder narrativo de la imagen monopolice el escenario.

## Guía de Implementación
- La imagen puede usar la etiqueta `<img>` o `background-image` de CSS, eligiendo el mejor método según el escenario.
- El método de máscara de gradiente no está limitado: un div real, `::before`/`::after`, o `mask-image` son todos aceptables, elige el mejor efecto visual.
- `card_style` recomendado: `transparent` -- la imagen grande no necesita estar restringida por el borde de la tarjeta.
