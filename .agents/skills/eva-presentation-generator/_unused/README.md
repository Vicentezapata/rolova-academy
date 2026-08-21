# EVA Presentation Generator - Estructura de Directorios

Esta Skill se encarga de generar presentaciones web interactivas (HTML/CSS/JS) a partir de material educativo en formato Markdown. A continuación se detalla la arquitectura de carpetas para comprender cómo se ensamblan las piezas.

## 🗂 Mapa de la Skill

```text
eva-presentation-generator/
│
├── SKILL.md                   # (OBLIGATORIO) Reglas de comportamiento e instrucciones core del Agente AI.
├── README.md                  # Este documento explicativo de la arquitectura.
│
├── assets/                    # 📦 Core de la UI y Runtime (Obligatorio copiar al destino)
│   ├── base.css               # Sistema de tipografía, variables y grid.
│   ├── runtime.js             # Lógica de navegación de las diapositivas y atajos de teclado.
│   ├── fonts.css              # Importación de Google Fonts.
│   ├── animations/            # CSS con micro-animaciones (@keyframes).
│   └── themes/                # (Opcional) Variables de colores predeterminados si no se usa la Style Gallery.
│
├── style-gallery/             # 🎨 Los "Skins" (Temas Visuales)
│   ├── dark_tech.html         # Muestrarios visuales individuales. El Agente abre estos archivos
│   ├── liquid_glass.html      # para extraer la etiqueta `<style>` y variables CSS (`:root`) y 
│   └── ...                    # luego inyectarlas como "ropa" a los esqueletos de `single-page`.
│
├── templates/                 # 🏗 Estructuras HTML
│   ├── single-page/           # -> Los "Esqueletos" para el ensamblaje dinámico.
│   │   ├── cover.html         # Archivos vacíos que el Agente utiliza como moldes.
│   │   ├── kpi-grid.html      # Inyecta texto aquí y luego lo viste con la Style Gallery.
│   │   └── ... 
│   │
│   ├── full-decks/            # -> Presentaciones Standalone (Modo Especial)
│   │   ├── tech-sharing/      # Plantillas completas (múltiples diapositivas ya unidas).
│   │   ├── product-launch/    # Poseen sus propios estilos (style.css) y un index.html unificado.
│   │   └── ...                # El Agente debe copiar toda la carpeta y sobreescribir el contenido.
│   │
│   └── core/                  # -> Vistas de entorno
│       ├── preview.html       # Interfaz pública del estudiante (con iFrames hacia los slides).
│       └── presenter.html     # Interfaz privada del profesor (notas + reloj + preview dual).
│
├── examples/                  # 💡 Referencias de Uso
│   ├── usage_patterns.md      # Ejemplos de prompts de cómo pedirle cosas al Agente.
│   └── output/                # Ejemplo de una presentación ya generada correctamente.
│
└── references/                # 📚 Documentación Externa (Para el modelo fundacional)
    └── ...                    # Guías de diseño, principios de Bento Grid, y cheat-sheets.
```

## 🧠 Lógica de Ensamblaje (Por qué están separados)

El diseño está pensado de forma modular (Lego) para evitar que la Inteligencia Artificial alucine o rompa el código HTML tratando de inyectar contenido en estructuras muy complejas.

### Flujo Estándar (Componentes Sueltos)
1. **Paso 1 (Estructura):** Se toma un esqueleto vacío de `templates/single-page/` (ej. `kpi-grid.html`).
2. **Paso 2 (Contenido):** Se inyecta el material educativo parseado (H1, P, listas).
3. **Paso 3 (Estilo):** Se extrae el estilo de `style-gallery/dark_tech.html` y se pega en el `<head>`.
4. **Paso 4 (Runtime):** Se añade una referencia a `assets/runtime.js`.
5. **Resultado:** Se guarda como `slide_01.html`. Este proceso se repite `N` veces y luego se agrupa en `preview.html`.

### Flujo Full-Deck (Plantilla Completa)
A veces, se desea una estética ultra-específica que ya viene armada de principio a fin.
1. Se copia **toda la carpeta** (ej. `templates/full-decks/tech-sharing/`) al proyecto destino.
2. Se abre el `index.html` de esa carpeta.
3. Se usan sus bloques `<section class="slide">` existentes como moldes.
4. Se inyecta el contenido y se guardan los cambios en el mismo `index.html`.
