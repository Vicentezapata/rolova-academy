# Rolova Academy

Portal 3D que centraliza el material docente de `cursos/` y genera presentaciones con IA.

## Puesta en marcha

```bash
npm install
npm run dev
```

Abre [http://localhost:3000](http://localhost:3000).

## Variables de entorno

Se leen de `.env.local` (no versionado).

| Variable | Obligatoria | Descripción |
|---|---|---|
| `GEMINI_API_KEY` | Para generar presentaciones | Clave de la API de Google Gemini. |
| `GEMINI_MODEL` | No | Modelo a usar. Por defecto `gemini-2.5-pro`. |
| `APP_PASSWORD` | Recomendada al desplegar | Activa Basic Auth en toda la app. **Si no se define, el sitio queda abierto.** |
| `PYTHON_BIN` | No | Intérprete de Python. Por defecto `python3`. |

## Estructura

```
app/
  api/
    courses/              listado de cursos con su árbol de materiales
    course-units/         listado de cursos y sus unidades
    file/[...path]/       sirve archivos de cursos/ (restringido a esa raíz)
    generate-presentation/ ingesta material -> Gemini -> ensamblador Python
    export-pptx/          captura un preview.html con Puppeteer -> .pptx
  components/             escena 3D (React Three Fiber) y HUD
  lib/
    safePath.js           resolución de rutas contenidas en cursos/
    courses.js            escaneo del sistema de archivos con caché
    theme.js              paleta por curso
cursos/                   material docente (una carpeta por asignatura)
.agents/skills/           ensamblador de presentaciones (Python + theme packs)
proxy.js                  Basic Auth opcional
```

## Comandos

```bash
npm run dev     # servidor de desarrollo
npm run build   # compilación de producción
npm run lint    # ESLint
```

## Notas

- El generador de presentaciones invoca `.agents/skills/eva-presentation-generator/scripts/generate_presentation_template.py`, que requiere Python 3 y escribe en `cursos/<curso>/<unidad>/presentation/`.
- La exportación a PPTX lanza Chromium mediante Puppeteer, por lo que necesita un entorno con sistema de archivos y memoria suficientes (no funciona tal cual en serverless).

