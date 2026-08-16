#Psicología y aplicación del color

> El color no es decoración, es un lenguaje silencioso. Elegir el color incorrecto puede ser más perjudicial que elegir la fuente incorrecta.
> Campos afectados: `cards[].card_style`, `decoration_hints.page_accent`, `director_command.mood`.
> Las portadas, páginas de capítulos y páginas de transición que requieran calibración emocional deben hacer referencia a este principio; Cubre la regla 60-30-10 y la seguridad del contraste.

## Regla 60-30-10

La ley de hierro en el mundo del diseño controla las proporciones de color:

- **60% Color Dominante**: El color principal de la página, a menudo blanco, gris oscuro o el color de fondo.
- **30% Color Secundario**: El color que apoya al principal, aporta profundidad y divide las secciones.
- **10% Color de Acento**: El color vibrante para destacar lo importante: datos clave, botones, flechas de tendencia.

- Los colores de acento son "condimentos". Si usas demasiado, todo el plato se arruinará.
- Se pueden usar hasta 2 colores de acento en la misma página al mismo tiempo
- Utilice mucho el color de acento = ya no es un color de acento

## Mapeo de emociones en color

| Sistema de colores | Emociones transmitidas | Escenarios aplicables |
|------|----------|---------|
| Azul | Confianza, profesionalismo, tecnología | Informes corporativos, soluciones técnicas, finanzas |
| Departamento Verde | Crecimiento, Naturaleza, Salud | Protección del Medio Ambiente, Atención Médica, Educación |
| Rojo/Naranja | Urgencia, entusiasmo, energía | Marketing, promoción, deportes |
| Púrpura | Innovación, alta gama, misteriosa | Innovación tecnológica, artículos de lujo, creatividad |
| Color gris | Neutro, elegante, minimalista | Informe de consultor, derecho, arquitectura |
| Colores oscuros | Sentido profesional, tranquilo y tecnológico | Desarrolladores, análisis en profundidad, lanzamientos de productos |

**Nota**: Existen diferencias culturales en las emociones de color. El rojo significa celebración en China, pero en el contexto financiero occidental significa pérdida.

## Contraste de seguridad

El texto debe ser legible, ese es el resultado final, no las opciones:

- Fondo oscuro -> Texto claro (blanco/70% blanco)
- Fondo claro -> Texto oscuro (negro/gris oscuro)
- El texto con color de acento solo se usa para títulos/datos/etiquetas, no para los párrafos del cuerpo.
- Relación de contraste mínima: 4,5:1 (estándar WCAG AA)

## Adaptación Automática de Temas

El uso de variables CSS (`--accent-1`, `--card-bg`) garantiza que el diseño sea robusto frente a cambios de tema (dark, light, editorial). No codifiques colores rígidos (hardcode) como `#FF0000`, ya que se romperán al cambiar el contexto.

##Autoprueba

- ¿La proporción de color de la página es cercana a 60-30-10?
- ¿Se utiliza el color de acento sólo donde es necesario llamar la atención?
- En el modo de escala de grises (con todos los colores eliminados), ¿sigue siendo clara la jerarquía de la información?