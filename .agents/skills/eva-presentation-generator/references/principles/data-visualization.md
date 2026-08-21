# Principios de visualización de datos

> El objetivo de la visualización de datos no es "mostrar datos", sino "dejar que los datos cuenten historias". Un buen diagrama permite que la audiencia comprenda la conclusión en 3 segundos.
> Campos afectados: `cards[].chart.chart_type`, `cards[].data_points`, `resources.chart_refs`.
> La página principal de los gráficos de datos debe hacer referencia a este principio; que cubre la proporción de tinta de datos de Tufte, la selección del tipo de gráfico y la integridad de los datos.

## Proporción de tinta de datos de Tufte

> Proporción de tinta de datos = tinta utilizada para mostrar datos / volumen total de tinta

- **MAXIMIZADO** Tinta de datos: cada elemento visual comunica datos
- **MINIMIZADO** Tinta sin datos: elimina líneas de cuadrícula decorativas, efectos 3D y rellenos degradados
- Líneas oscuras en PPT: el fondo del gráfico es transparente, el eje es extremadamente delgado (1 px, 20 % de transparencia) y las etiquetas están simplificadas

## Reglas de oro para la selección de gráficos

| ¿Qué quieres expresar? Qué usar | Qué no usar |
|----------------|--------|---------|
| Proporción/cuota | Gráfico de anillos/barras apiladas/gráfico de árbol | Gráfico de líneas |
| Tendencia/Cambio | Gráfico de líneas/Gráfico de áreas | Gráfico circular |
| Comparación/clasificación | Gráfico de columnas/barra de comparación | Gráfico radial (cuando hay más de 5 elementos) |
| KPI único | Tarjeta KPI / número grande | Gráfico complejo |
| Capacidades multidimensionales | Gráfico radar (3-5 dimensiones) | Mesa |
| Transformación de Procesos | Gráfico de embudo | Gráfico circular |
| Nodos de tiempo | Línea de tiempo | Mesa |

**Error más común**: Mostrar más de 5 categorías en un gráfico circular (el ojo humano no puede comparar pequeñas diferencias entre sectores).

## Principios del panel de control de Stephen Few

- **Completar en una pantalla**: todos los indicadores clave en una sola vista, no es necesario desplazarse
- **Marcar anomalías**: utilice colores neutros para los datos normales y resalte los datos anormales con colores acentuados.
- **Proporcione contexto**: Los números por sí solos no tienen sentido, "37%" no es tan bueno como "37% (promedio de la industria 22%)"
- **Tendencia > Instantánea**: un número de tendencia es 10 veces más informativo que un número estático

## Integridad de datos

- **Proporcionalidad**: El tamaño del elemento gráfico (área, longitud) debe ser estrictamente proporcional al valor que representa.
- **Línea base cero**: Los gráficos de barras y columnas deben comenzar en 0. Si se trunca el eje, debe indicarse claramente para no exagerar las diferencias.
- **Sin efectos 3D**: La perspectiva 3D distorsiona los datos y hace que las áreas traseras parezcan más pequeñas.

##Autoprueba

- ¿Tiene cada visualización de datos una "conclusión" clara (en lugar de permitir que los espectadores encuentren sus propias conclusiones)?
- Si quitas el gráfico y te fijas sólo en los números, ¿el mensaje sigue siendo claro? (Si es así, el diagrama puede ser redundante)
- Mirando números en lugar de gráficos, ¿está claro el mensaje? (Si es así, la anotación puede ser insuficiente)