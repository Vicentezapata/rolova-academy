# Contrato de Tokens

> Lee esto **solo si vas a crear un theme pack nuevo**. Para generar presentaciones no hace falta.

Los 30 arquetipos de `_shared/` están escritos **sin un solo color literal**: todo sale de las variables que declara el `_frame.html` de cada pack. Por eso **crear un pack son 2 archivos**:

```
theme-packs/<mi_pack>/
  _frame.html    ← tokens + decoraciones de firma + estructura del documento
  pack.json      ← identidad + ritmo de fondos
```

El validador falla si un arquetipo introduce un color literal o si un frame olvida declarar un token que sí se usa. Eso es lo que impide que los packs se desincronicen.

---

## Cómo crear un pack

1. Copia `theme-packs/dark_tech/_frame.html` a `theme-packs/<mi_pack>/_frame.html`.
2. Cambia **solo** el bloque `:root` y las tres reglas `.deco-a/.deco-b/.deco-c`.
3. Copia y edita `pack.json`.
4. `python scripts/validate_packs.py --pack <mi_pack>`

No toques `{{SHARED_CSS}}`, `{{BODY}}`, `{{EXTRA_CSS}}`, `{{SLIDE_NUM}}` ni el `<script>` final: son el contrato con el renderer y el visor.

---

## Tokens obligatorios

### Color base
| Token | Qué es |
|---|---|
| `--bg` / `--bg2` | Fondo del lienzo y variante secundaria |
| `--text` | Texto principal |
| `--text-sec` | Texto de apoyo (párrafos, descripciones) |
| `--text-ter` | Texto terciario (numeración, metadatos) |
| `--strong` | Color de `<b>` y `<strong>` |

### Acentos y semánticos
| Token | Qué es |
|---|---|
| `--a1` | Acento principal. Domina kickers, cifras y énfasis |
| `--a2` | Acento secundario. Tags del header y la regla divisoria |
| `--a3` | Acento terciario. Badges de refuerzo |
| `--ok` / `--warn` / `--err` | Texto semántico (verde / ámbar / rojo del tema) |
| `--a1-t` … `--err-t` | **Tint**: fondo translúcido de píldoras y bloques |
| `--a1-b` … `--err-b` | **Border**: borde del mismo elemento |

> En temas de fondo claro con estética de trazo grueso (como `retro_warm`), los `-b` pueden apuntar todos al color de tinta en vez de a un tono del acento. El contrato solo exige que existan.

### Superficies
| Token | Qué es |
|---|---|
| `--card-bg` | Fondo de tarjeta. Admite color plano o `linear-gradient(...)` |
| `--border` | Color de borde de tarjeta |
| `--bw` | **Ancho de borde**: `1px` en temas sutiles, `2px` en temas de trazo |
| `--rule-h` | Grosor de la regla divisoria bajo el header |
| `--radius` / `--radius-lg` | Radios de esquina de tarjetas y paneles |
| `--radius-sm` | Radio de píldoras, chips, badges y barras de gráfico |
| `--radius-pill` | Radio máximo de las píldoras redondas (`999px` en la mayoría de temas) |
| `--shadow` / `--shadow-sm` | Sombra. `none`, sombra suave o *hard shadow* (`4px 4px 0 ...`) |
| `--inset-bg` / `--inset-border` | Sub-paneles dentro de una tarjeta |
| `--hi-bg` | Fondo de fila o campo resaltado |
| `--hairline` | Separadores de 1px entre filas |
| `--zebra` | Fondo de filas pares en tablas |
| `--thead-bg` | Fondo de la cabecera de tabla |

> **Si tu pack usa `--radius: 0`, declara también `--radius-sm: 0px` y `--radius-pill: 0px`.** Los arquetipos los aplican con fallback (`var(--radius-pill, 999px)`), así que un pack de esquinas rectas que no los declare seguirá pintando píldoras redondas y badges con esquina — una incoherencia que el validador no puede detectar. Lo hacen así `bauhaus_block`, `cyberpunk_neon`, `earth_concrete`, `gov_authority` y `luxury_purple`.

### Mermaid
Seis tokens obligatorios que colorean los diagramas del arquetipo `diagram`:
`--mermaid-primary` (relleno de nodo), `--mermaid-text`, `--mermaid-border`, `--mermaid-line` (aristas), `--mermaid-secondary` y `--mermaid-tertiary`.
Si faltan, el diagrama se dibuja con la paleta por defecto de Mermaid y desentona con el resto del deck.

### Código
`--code-bg`, `--code-fg`, y el resaltado: `--c-kw` (palabra clave), `--c-fn` (función), `--c-str` (cadena), `--c-cm` (comentario), `--c-num` (número).

### Tipografía
| Token | Qué es |
|---|---|
| `--display` | Titulares de tarjeta y header |
| `--display-xl` | Titulares gigantes (portada, separador, cita). Aquí va la fuente con personalidad |
| `--body` | Cuerpo de texto |
| `--mono` | Kickers, tags, código, cifras |
| `--serif` | Fuente de énfasis |
| `--em-family` / `--em-style` / `--em-weight` | Cómo se renderiza `<em>` |
| `--heavy` | Peso de los titulares (`700`, `800` o `900`) |
| `--title-shadow` | `none`, o un desplazamiento sólido en temas de trazo |

### Mermaid
`--mermaid-primary`, `--mermaid-text`, `--mermaid-border`, `--mermaid-line`, `--mermaid-secondary`, `--mermaid-tertiary` — los consume el arquetipo `diagram`.

---

## Decoraciones de firma

El frame expone tres capas que el `<body>` ya coloca por ti. Redefínelas a tu gusto; si tu tema no usa alguna, ponla en `display:none`.

| Clase | Uso típico |
|---|---|
| `.deco-a` | Capa de fondo global (textura de puntos, degradado cálido, regla superior) |
| `.deco-b` | Elemento de energía (orbe difuminado, banda de rayas superior, hairline) |
| `.deco-c` | Contrapunto (banda inferior, hairline de cierre) |

Además puedes añadir cualquier elemento extra dentro del `<main>` del frame — por ejemplo el `<svg>` de grano de `retro_warm`.

## Ritmo de fondos

`pack.json` declara `background_rhythm`: una lista de variantes que el renderer **rota automáticamente por índice de slide**. Cada clave del objeto queda disponible como slot en el frame.

```json
"background_rhythm": [
  { "PAPER": "#faf7f2" },
  { "PAPER": "linear-gradient(180deg,#faf7f2 0%,#f6f2ea 100%)" }
]
```

Así el deck gana variedad visual sin que el agente decida nada.

---

## Packs actuales como referencia

| Pack | Estrategia de tokens |
|---|---|
| `dark_tech` | Oscuro, `--bw:1px`, `--shadow:none`, tints translúcidos sobre acentos, `--card-bg` en gradiente |
| `retro_warm` | Claro cálido, `--bw:2px`, hard shadow, todos los `-b` apuntan a la tinta, `--display-xl` decorativa |
| `editorial_paper` | Papel, `--bw:1px`, `--radius:3px`, sombra mínima, serif en todos los titulares |

Son tres estrategias deliberadamente opuestas: si tu pack encaja en alguna, parte de ese frame.
