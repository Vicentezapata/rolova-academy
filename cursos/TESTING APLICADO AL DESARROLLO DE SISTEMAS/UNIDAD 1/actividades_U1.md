# 🎮 Actividades Didácticas — Unidad 1
## Testing Aplicado al Desarrollo de Sistemas | IF203IINF
### Metodología: Aprendizaje Basado en Problemas (ABP) · "Aprender Haciendo"

---

> **Principio pedagógico:** Cada actividad está diseñada para que el estudiante **aplique** conocimientos en situaciones reales, no solo los memorice. Se utiliza la metodología activa de **Aprendizaje Basado en Problemas (ABP)**, centrada en el estudiante.

---

## 📋 Resumen de Actividades por Sesión

| Sesión | Actividad Principal | Tipo | Modalidad | Tiempo |
|--------|---------------------|------|-----------|--------|
| S1 | 🔍 El Gran Detective de Bugs | Individual | Asíncrona | 60 min |
| S1 | 🗣️ Foro: El costo del error | Grupal | Asíncrona | 20 min |
| S2 | 🧪 Laboratorio de Pruebas Unitarias | Individual | Asíncrona | 70 min |
| S2 | 🧩 Arquitecto de Integración | Parejas | Asíncrona | 45 min |
| S3 | 🏦 Sistema Bancario: Mapeando Niveles | Parejas | Asíncrona | 50 min |
| S3 | ✅ El Contrato del Cliente (UAT) | Individual | Asíncrona | 40 min |
| S4 | ⬜⬛ La Caja Misteriosa | Grupal | Sincrónica | 40 min |
| S4 | 🔨 Taller de Diseño de Casos | Grupos 3 | Sincrónica | 50 min |
| S5 | 🏆 Evaluación: Caso Real Integrador | Individual | EVA | 4h |

---

---

# 🔵 SESIÓN 1 — Introducción al Testing y Principios Fundamentales

---

## 🎯 Actividad 1.1 — "El Gran Detective de Bugs"
### Tipo: Individual | Asíncrona | ⏱️ 60 min | Entrega: Foro EVA

### 📖 Contexto
En 1996, el cohete Ariane 5 de la Agencia Espacial Europea explotó 37 segundos después del despegue. La causa: un error de software. El costo: 370 millones de dólares. En 1999, la sonda Mars Climate Orbiter se perdió porque un equipo usó unidades métricas y otro imperiales. En los años 80-90, la máquina de radioterapia Therac-25 mató a 6 pacientes por un error de condición de carrera en el código.

### 🔍 Tu Misión
Eres un **Detective de Bugs** recién contratado. Debes investigar UN caso real de error de software, analizarlo y presentar tu informe forense.

### 📁 Casos disponibles (elige 1)
- **Caso A:** Ariane 5 — El cohete que se destruyó a sí mismo (1996)
- **Caso B:** Therac-25 — La máquina que mató pacientes (1985-1987)
- **Caso C:** Mars Climate Orbiter — La sonda perdida por métricas (1999)
- **Caso D:** Flash Crash de Wall Street — El mercado que cayó por un algoritmo (2010)
- **Caso E:** Bug del año 2000 (Y2K) — El error que aterrorizó al mundo

### 📝 Entregable: Informe Forense de Bug (formato libre — máx. 1 página)

```
╔══════════════════════════════════════════════════════════╗
║  INFORME FORENSE DE BUG                                  ║
║  Detective: [Tu nombre]                                  ║
║  Caso: [Nombre del caso elegido]                         ║
╠══════════════════════════════════════════════════════════╣
║                                                          ║
║  1. DESCRIPCIÓN DEL SISTEMA                              ║
║     ¿Para qué servía el software? ¿Quién lo usaba?       ║
║                                                          ║
║  2. TIPO DE ERROR IDENTIFICADO                           ║
║     ☐ Error funcional    ☐ Error no funcional            ║
║     Clasifica el impacto: ☐ Crítico ☐ Alto ☐ Medio ☐ Bajo ║
║                                                          ║
║  3. CAUSA RAÍZ                                           ║
║     ¿Qué falla exactamente ocurrió en el código/proceso? ║
║                                                          ║
║  4. FASE DE INTRODUCCIÓN DEL ERROR                       ║
║     ¿En qué etapa del desarrollo se introdujo el defecto?║
║     ☐ Diseño ☐ Codificación ☐ Integración ☐ Requisitos  ║
║                                                          ║
║  5. VEREDICTO: ¿QUÉ TIPO DE TESTING LO HABRÍA EVITADO? ║
║     ¿Pruebas unitarias? ¿De sistema? ¿Aceptación?        ║
║     Justifica tu respuesta.                              ║
║                                                          ║
║  6. IMPACTO                                              ║
║     Económico: $___________  Humano: ___________         ║
║     Reputacional: ___________                            ║
║                                                          ║
║  7. LECCIÓN APRENDIDA                                    ║
║     ¿Qué principio del testing aplica aquí?              ║
╚══════════════════════════════════════════════════════════╝
```

### 🎯 Criterios de Éxito
- ✅ Identificó correctamente el tipo de error (funcional/no funcional)
- ✅ Determinó la fase donde se introdujo el defecto
- ✅ Propuso el tipo de testing que lo habría detectado **con justificación**
- ✅ Conectó con al menos 1 principio del testing ISTQB

### 💡 Recursos para investigar
- Google Scholar / Wikipedia
- [Casos de fallas de software - IEEE](https://ieeexplore.ieee.org)
- El Apunte N°1 te ayudará a identificar el tipo y principio correspondiente

---

## 🎯 Actividad 1.2 — Foro: "¿Por qué NO probar sale más caro?"
### Tipo: Grupal | Asíncrona | ⏱️ 20 min | Foro EVA

### 📢 Situación
Una startup de fintech te contrató. El CEO dice: "No tenemos tiempo para testing, lanzamos en 2 semanas y lo corregimos después con updates". El CTO está en desacuerdo.

### 🗣️ Tu Tarea
1. **Publica** tu posición (¿apoyas al CEO o al CTO?) en máx. 5 líneas, con al menos **1 argumento técnico** basado en los principios del testing.
2. **Responde** a 1 compañero/a con quien estés en desacuerdo, refutando su argumento con otro argumento del apunte.

### ⚠️ Reglas del Foro
- No se aceptan respuestas sin argumento técnico
- Usa terminología del apunte: error, defecto, falla, detección temprana, etc.
- El debate debe ser respetuoso y profesional

---

---

# 🟢 SESIÓN 2 — Niveles de Prueba: Pruebas Unitarias e Integración

---

## 🎯 Actividad 2.1 — "Laboratorio de Pruebas Unitarias"
### Tipo: Individual | Asíncrona | ⏱️ 70 min | Entrega: Documento Word/PDF

### 📖 Contexto
Eres QA Engineer en **TiendaChile.cl**, un e-commerce que vende tecnología. El desarrollador te entregó las siguientes funciones y necesita que diseñes los casos de prueba unitaria para validarlas ANTES de integrarlas al sistema.

### 🖥️ Función 1: Calculadora de Precio Final
```
FUNCIÓN: calcularPrecioFinal(precioBase, porcentajeIVA, descuento)
- precioBase: número positivo en pesos chilenos
- porcentajeIVA: porcentaje (ej: 19 para 19% IVA)
- descuento: monto fijo a descontar (puede ser 0)
- RETORNA: precio final con IVA y sin descuento
- EJEMPLO: calcularPrecioFinal(10000, 19, 500) = 11.400
```

### 🖥️ Función 2: Validador de RUT chileno
```
FUNCIÓN: validarRUT(rut)
- rut: string en formato "12345678-9" o "12.345.678-9"
- RETORNA: true si el RUT es válido, false si no
- REGLA: debe verificar el dígito verificador
```

### 📝 Tu Entregable: Tabla de Casos de Prueba

Completa la siguiente tabla para CADA función (mínimo 5 casos por función):

```
FUNCIÓN: calcularPrecioFinal
┌────┬──────────────────────┬─────────────┬────────┬─────────────┬─────────┬────────────┐
│ #  │ Descripción del caso │ precioBase  │  IVA%  │  descuento  │ Resultado│  Resultado │
│    │                      │             │        │             │ Esperado │  Real (*)  │
├────┼──────────────────────┼─────────────┼────────┼─────────────┼──────────┼────────────┤
│ 1  │ Caso válido estándar │   10.000    │   19   │     500     │  11.400  │            │
│ 2  │ Descuento cero       │             │        │             │          │            │
│ 3  │ Precio negativo      │   -5.000    │   19   │      0      │ ERROR/EX │            │
│ 4  │ IVA = 0%             │             │        │             │          │            │
│ 5  │ Descuento > precio   │    1.000    │   19   │   2.000     │          │            │
│ 6  │ Valores decimales    │             │        │             │          │            │
│ 7  │ [Tu caso adicional]  │             │        │             │          │            │
└────┴──────────────────────┴─────────────┴────────┴─────────────┴──────────┴────────────┘
(*) Esta columna la completan en clases avanzadas con código real
```

### 🔍 Además responde:
1. ¿Qué tipo de prueba es esta (caja blanca o caja negra)? Justifica.
2. ¿Cuáles son los casos límite más críticos? ¿Por qué?
3. ¿Qué framework de testing usarías si TiendaChile.cl usa Python? ¿Y si usa Java?

### 🎯 Criterios de Éxito
- ✅ Mínimo 5 casos bien definidos por función
- ✅ Incluye: casos válidos, casos inválidos y casos límite
- ✅ Resultado esperado es específico y medible
- ✅ Responde las 3 preguntas adicionales

---

## 🎯 Actividad 2.2 — "Arquitecto de Integración"
### Tipo: Parejas | Asíncrona | ⏱️ 45 min | Entrega: Diagrama + Justificación

### 📖 Contexto
El sistema de TiendaChile.cl tiene los siguientes módulos:

```
┌─────────────────────────────────────────────────────┐
│  SISTEMA TIENDACHILE.CL                             │
│                                                     │
│  [M1] Autenticación    [M2] Catálogo de Productos   │
│        ↓                         ↓                  │
│  [M3] Carrito de Compras ←→ [M4] Stock/Inventario  │
│        ↓                                            │
│  [M5] Pago y Facturación   [M6] Envío y Despacho   │
│        ↓                         ↓                  │
│  [M7] Confirmación y Notificaciones al usuario       │
└─────────────────────────────────────────────────────┘
```

### 🧩 Tu Misión (en pareja)

**Parte A — Diseñen 4 pruebas de integración** (2 por persona):
Para cada prueba especifiquen:
- **¿Qué módulos integra?** (ej: M3 ↔ M4)
- **¿Qué se está verificando?** (qué dato o flujo se prueba)
- **¿Qué resultado esperan?** (comportamiento correcto)
- **¿Qué error podría ocurrir?** (qué falla de integración detectaría)

**Parte B — Elijan UNA estrategia de integración:**
De las 4 estrategias (Big Bang / Bottom-Up / Top-Down / Sandwich):
- ¿Cuál usarían para este sistema? ¿Por qué?
- ¿Qué módulo probarían primero con su estrategia?
- ¿Qué riesgos tiene la estrategia que eligieron?

### 📋 Formato de entrega (tabla + párrafo)

```
PRUEBA DE INTEGRACIÓN N°1
- Módulos involucrados: M___ ↔ M___
- ¿Qué se verifica?: ___________________________________
- Datos de entrada: ____________________________________
- Resultado esperado: __________________________________
- Error posible que detectaría: ________________________
```

---

---

# 🟡 SESIÓN 3 — Niveles de Prueba: Sistema y Aceptación

---

## 🎯 Actividad 3.1 — "El Sistema Bancario Bajo la Lupa"
### Tipo: Parejas | Asíncrona | ⏱️ 50 min | Entrega: Tabla completa

### 📖 Contexto
Trabajas en el equipo de QA del **BancoDigital**, un banco 100% online que acaba de terminar el desarrollo de su aplicación móvil. Tu jefe te pide que diseñes el plan de pruebas de sistema antes del lanzamiento.

### 🖥️ Funcionalidades del sistema bancario
1. Login con huella dactilar / contraseña
2. Ver saldo y movimientos
3. Transferencia entre cuentas
4. Pago de servicios (luz, agua, internet)
5. Solicitar crédito de consumo
6. Bloqueo de tarjeta ante 3 intentos fallidos

### 🧪 Tu Misión: Diseñar 6 pruebas de sistema (1 por funcionalidad)

Para cada una especifica el **tipo de prueba de sistema** más adecuado:

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│ PLAN DE PRUEBAS DE SISTEMA — BANCODIGITAL                                           │
├────┬─────────────────────────┬──────────────┬─────────────────────┬─────────────────┤
│ #  │ Funcionalidad           │ Tipo de      │ ¿Qué se prueba      │ Resultado       │
│    │                         │ prueba*      │ específicamente?    │ esperado        │
├────┼─────────────────────────┼──────────────┼─────────────────────┼─────────────────┤
│ 1  │ Login con huella        │              │                     │                 │
│ 2  │ Ver saldo y movimientos │              │                     │                 │
│ 3  │ Transferencia           │              │                     │                 │
│ 4  │ Pago de servicios       │              │                     │                 │
│ 5  │ Solicitar crédito       │              │                     │                 │
│ 6  │ Bloqueo de tarjeta      │              │                     │                 │
└────┴─────────────────────────┴──────────────┴─────────────────────┴─────────────────┘
```
*Tipo de prueba: Rendimiento / Seguridad / Usabilidad / Funcional / Compatibilidad / Recuperación

### 🔍 Además responde (reflexión en pareja):
1. ¿Qué prueba de sistema es la más CRÍTICA para un banco? ¿Por qué?
2. ¿Qué pasaría si lanzaran sin pruebas de seguridad?
3. ¿En qué orden ejecutarían estas 6 pruebas? Justifica.

---

## 🎯 Actividad 3.2 — "El Contrato del Cliente: Criterios UAT"
### Tipo: Individual | Asíncrona | ⏱️ 40 min | Entrega: Lista de criterios

### 📖 Contexto
El cliente del BancoDigital te mandó este mensaje:

> *"Necesito que el sistema de transferencias funcione bien. El usuario debe poder transferir dinero a cualquier cuenta, de cualquier banco, las 24 horas. Si hay algún error, que el sistema lo diga claramente. Y que sea rápido."*

### 🤔 El Problema
Este mensaje es **vago e impreciso**. Un criterio como "que sea rápido" no sirve para hacer una prueba de aceptación. Los criterios UAT deben ser **específicos, medibles y verificables**.

### ✍️ Tu Misión
Transforma el mensaje del cliente en **8 criterios de aceptación** formales para la funcionalidad de **Transferencias Bancarias**.

**Usa este formato:**

```
CRITERIO DE ACEPTACIÓN #N
Funcionalidad: Transferencias Bancarias

DADO [contexto/precondición]
CUANDO [acción del usuario]
ENTONCES [resultado esperado MEDIBLE]

Ejemplo CORRECTO:
  DADO que el usuario tiene saldo disponible de $50.000
  CUANDO ingresa un monto de $30.000 y selecciona cuenta destino válida
  ENTONCES el sistema debería completar la transferencia en menos de 5 segundos
  Y mostrar un mensaje de confirmación con número de operación
  Y descontar el monto del saldo en tiempo real

Ejemplo INCORRECTO:
  El usuario puede transferir dinero fácilmente y rápido ← VAGO
```

### 💡 Pistas para tus 8 criterios
Piensa en cubrir: monto mínimo/máximo, cuentas de otros bancos, horarios, mensajes de error, confirmaciones, saldo insuficiente, conexión caída...

### 🎯 Criterios de Éxito
- ✅ Cada criterio usa formato DADO/CUANDO/ENTONCES
- ✅ El resultado esperado es **medible** (números, tiempos, porcentajes)
- ✅ Cubre escenarios exitosos Y escenarios de error
- ✅ No queda ningún criterio ambiguo

---

---

# 🟣 SESIÓN 4 — Tipos de Pruebas (SINCRÓNICA — Teams)

---

## 🎯 Actividad 4.1 — "La Caja Misteriosa" *(Actividad en vivo — 40 min)*
### Tipo: Grupal en vivo | Sincrónica | ⏱️ 40 min

### 🎮 Mecánica del Juego
El docente presenta **10 tarjetas de casos de prueba** proyectadas en pantalla. Los equipos (grupos de 3-4) deben clasificar CADA tarjeta en la categoría correcta en **30 segundos** por tarjeta.

**Categorías:**
- ⬜ Caja Blanca
- ⬛ Caja Negra
- ✅ Funcional
- 📊 No Funcional
- 🔄 Regresión

**Tarjetas de casos** (el docente las proyecta una a una):

```
TARJETA 1
"El tester analiza el código fuente para asegurarse
de que todas las ramas del if-else sean ejecutadas
al menos una vez durante las pruebas."
CATEGORÍA: ___________

TARJETA 2
"Se verifica que el sistema de login acepte
un usuario y contraseña correctos y redirija
al dashboard sin ver el código."
CATEGORÍA: ___________

TARJETA 3
"Se prueba que la página de inicio cargue
en menos de 2 segundos con 500 usuarios
concurrentes."
CATEGORÍA: ___________

TARJETA 4
"Después de actualizar el módulo de pagos,
se vuelven a ejecutar TODOS los casos de prueba
que antes pasaban para verificar que siguen funcionando."
CATEGORÍA: ___________

TARJETA 5
"El tester ingresa datos al formulario de registro
sin saber cómo está implementado el backend."
CATEGORÍA: ___________

TARJETA 6
"Se traza cada línea de código para verificar
que no haya código muerto (nunca ejecutado)."
CATEGORÍA: ___________

TARJETA 7
"Se prueba que el sistema funcione correctamente
en Chrome, Firefox, Safari y Edge."
CATEGORÍA: ___________

TARJETA 8
"Se intenta inyectar SQL en el campo
de búsqueda para ver si el sistema lo bloquea."
CATEGORÍA: ___________

TARJETA 9
"Se verifica que el botón 'Agregar al carrito'
efectivamente agregue el producto al carrito."
CATEGORÍA: ___________

TARJETA 10
"Se corrigió un bug en el módulo de descuentos.
Ahora se ejecutan las pruebas de los módulos
de carrito y pago para asegurar que nada se rompió."
CATEGORÍA: ___________
```

### 🏆 Sistema de Puntos
- Respuesta correcta en < 10 segundos: 3 puntos
- Respuesta correcta en 10-30 segundos: 1 punto
- Respuesta incorrecta: 0 puntos
- El equipo con más puntos gana reconocimiento en el foro

**Respuestas correctas:** 1=⬜, 2=⬛✅, 3=📊, 4=🔄, 5=⬛, 6=⬜, 7=📊, 8=📊🔒, 9=✅⬛, 10=🔄

---

## 🎯 Actividad 4.2 — "Taller: Somos el Equipo QA de StreamChile"
### Tipo: Grupos de 3 | Sincrónica | ⏱️ 50 min | Presentación al curso

### 📖 Contexto
**StreamChile** es una plataforma de streaming (como Netflix) chilena recién lanzada. Tienen estos problemas reportados por usuarios beta:

> ⚠️ **Reporte 1:** "A veces cuando busco una película, el resultado no carga y queda en pantalla en blanco."
> ⚠️ **Reporte 2:** "El video se congela cuando muchas personas ven el mismo contenido popular."
> ⚠️ **Reporte 3:** "En mi iPhone el botón de 'favoritos' no aparece, pero en Android sí."
> ⚠️ **Reporte 4:** "Pago el plan, pero a veces me pide iniciar sesión de nuevo y pierdo mi progreso."

### 🛠️ Su Misión como Equipo QA (grupos de 3)

**Paso 1 — Diagnóstico (15 min):**
Para CADA reporte de usuario, completen:
```
Reporte #N:
- Tipo de prueba que detectaría esto: [Caja Blanca / Negra / Funcional / No Funcional]
- Nivel de prueba donde se detectaría: [Unitaria / Integración / Sistema / Aceptación]
- Criticidad: [Crítica / Alta / Media / Baja]
- Justificación: _______________
```

**Paso 2 — Diseño de casos de prueba (25 min):**
Diseñen **2 casos de prueba formales** para los reportes que consideran MÁS CRÍTICOS:

```
CASO DE PRUEBA #1
Nombre: ______________________________
Funcionalidad: ________________________
Precondición: _________________________
Pasos a ejecutar:
  1. ___________________________________
  2. ___________________________________
  3. ___________________________________
Datos de prueba: ______________________
Resultado esperado: ___________________
Tipo de prueba: _______________________
Técnica: [Caja Blanca / Caja Negra / Funcional / No Funcional]
```

**Paso 3 — Presentación (10 min):**
Cada grupo presenta sus 2 casos al curso. Los demás grupos pueden hacer 1 pregunta.

---

## 🎯 Actividad 4.3 — "El Bug que Volvió: Regresión en Acción"
### Tipo: Individual | Post-sesión (tarea) | ⏱️ 30 min

### 📖 Situación
StreamChile corrigió el bug del botón de "favoritos" en iPhone (Reporte #3). El desarrollador cambió el CSS del botón. Ahora el tester debe verificar que:
1. El botón aparece en iPhone ✅
2. El botón también sigue funcionando en Android ✅
3. El botón no rompió ninguna otra funcionalidad ✅

### 📝 Tu Tarea
Diseña un **mini plan de regresión** con 5 casos de prueba que ejecutarías después de este fix:

```
PLAN DE REGRESIÓN — Fix botón "Favoritos"
Fecha del fix: ___________  Responsable: ___________

Área afectada por el cambio: CSS del componente Botón Favoritos

Casos de Regresión:
┌───┬──────────────────────────────┬────────────┬────────────────┐
│ # │ Caso a re-probar             │ Plataforma │ ¿Por qué?      │
├───┼──────────────────────────────┼────────────┼────────────────┤
│ 1 │ Botón favoritos visible      │ iPhone     │ Caso reparado  │
│ 2 │ Botón favoritos visible      │ Android    │ No debe romper │
│ 3 │                              │            │                │
│ 4 │                              │            │                │
│ 5 │                              │            │                │
└───┴──────────────────────────────┴────────────┴────────────────┘

Criterio de cierre: ¿Cuándo considerarías que la regresión pasó?
```

---

---

# 🏆 SESIÓN 5 — Evaluación Sumativa: Situación Problemática

---

## 🎯 EVALUACIÓN FINAL U1 — "Proyecto QA: AppSalud"
### Tipo: Individual | Plataforma EVA | ⏱️ 4 horas | Ponderación: 10%

### 📖 Contexto del Caso
El **MINSAL** (Ministerio de Salud) contrató a la empresa **AppSalud SpA** para desarrollar una aplicación web y móvil de telemedicina. La app permite:

1. **Registro de pacientes** — Con RUT, nombre, fecha de nacimiento, datos de contacto.
2. **Solicitar consulta médica** — Elegir especialidad, fecha y hora disponible.
3. **Videollamada con médico** — Consulta en tiempo real (duración máx. 30 min).
4. **Prescripción electrónica** — El médico emite receta digital al finalizar.
5. **Historial de consultas** — El paciente puede ver todas sus consultas pasadas.
6. **Sistema de pagos** — Pago con tarjeta, débito o Fonasa (gratuito para algunos beneficiarios).

AppSalud terminó el desarrollo y te contrató como **QA Engineer** para evaluar el sistema ANTES de lanzarlo al público. El lanzamiento está programado en 2 semanas.

---

### 📋 PARTE 1 — Análisis de Niveles de Prueba *(30 pts)*

**Para las 6 funcionalidades del sistema, indica qué nivel de prueba es el más apropiado y por qué:**

```
┌────┬───────────────────────────┬──────────────────┬──────────────────────────────────┐
│ #  │ Funcionalidad             │ Nivel de prueba  │ Justificación técnica            │
│    │                           │ principal        │                                  │
├────┼───────────────────────────┼──────────────────┼──────────────────────────────────┤
│ 1  │ Registro de pacientes     │                  │                                  │
│ 2  │ Solicitar consulta        │                  │                                  │
│ 3  │ Videollamada con médico   │                  │                                  │
│ 4  │ Prescripción electrónica  │                  │                                  │
│ 5  │ Historial de consultas    │                  │                                  │
│ 6  │ Sistema de pagos          │                  │                                  │
└────┴───────────────────────────┴──────────────────┴──────────────────────────────────┘
```
*Niveles: Unitaria / Integración / Sistema / Aceptación (puede haber más de uno)*

---

### 📋 PARTE 2 — Diseño de Casos de Prueba *(40 pts)*

Diseña **4 casos de prueba formales** (usando el formato completo). Elige funcionalidades diferentes para cada caso:

**IMPORTANTE:** Al menos uno debe ser un caso de prueba de un **escenario de ERROR** (no solo el camino feliz).

```
╔═══════════════════════════════════════════════════════════════╗
║  CASO DE PRUEBA #___                                          ║
╠═══════════════════════════════════════════════════════════════╣
║  ID: CP-U1-001                                                ║
║  Nombre: ___________________________________________________  ║
║  Funcionalidad: ____________________________________________  ║
╠═══════════════════════════════════════════════════════════════╣
║  TÉCNICA DE PRUEBA:                                           ║
║  ☐ Caja Negra    ☐ Caja Blanca                               ║
║  TIPO: ☐ Funcional    ☐ No Funcional (especifica: _________)  ║
║  NIVEL: ☐ Unitaria ☐ Integración ☐ Sistema ☐ Aceptación      ║
╠═══════════════════════════════════════════════════════════════╣
║  PRECONDICIÓN:                                                ║
║  (Estado del sistema ANTES de ejecutar el caso)              ║
║  _____________________________________________________________║
╠═══════════════════════════════════════════════════════════════╣
║  DATOS DE PRUEBA:                                             ║
║  _____________________________________________________________║
╠═══════════════════════════════════════════════════════════════╣
║  PASOS A EJECUTAR:                                            ║
║  1. _________________________________________________________ ║
║  2. _________________________________________________________ ║
║  3. _________________________________________________________ ║
║  4. _________________________________________________________ ║
╠═══════════════════════════════════════════════════════════════╣
║  RESULTADO ESPERADO:                                          ║
║  (Debe ser ESPECÍFICO Y MEDIBLE)                             ║
║  _____________________________________________________________║
╠═══════════════════════════════════════════════════════════════╣
║  TIPO DE ERROR QUE DETECTARÍA:                               ║
║  _____________________________________________________________║
╚═══════════════════════════════════════════════════════════════╝
```

---

### 📋 PARTE 3 — Criterios de Aceptación UAT *(20 pts)*

El médico (usuario final) del sistema te dijo:

> *"La videollamada tiene que funcionar bien. Si el paciente no puede conectarse, que le avise. Y quiero poder prescribir medicamentos durante la consulta, no después."*

Transforma esto en **5 criterios de aceptación** formales en formato DADO/CUANDO/ENTONCES.

---

### 📋 PARTE 4 — Análisis y Priorización *(10 pts)*

Responde en un párrafo (máx. 150 palabras):

> AppSalud tiene solo **2 semanas** antes del lanzamiento y recursos limitados para hacer todas las pruebas. Como QA Engineer, ¿qué tipo y nivel de prueba priorizarías? ¿Por qué? Considera que es una aplicación de salud pública con potencial impacto en vidas humanas.

---

### 📊 Rúbrica de Evaluación

| Criterio | Logrado (100%) | Med. Logrado (60%) | No Logrado (0%) |
|----------|----------------|-------------------|-----------------|
| **P1 — Niveles (30pts)** | Todos los niveles correctos con justificación técnica sólida | Mayoría correctos, justificación básica | Niveles incorrectos o sin justificación |
| **P2 — Casos (40pts)** | 4 casos completos, medibles, incluye escenario de error | 4 casos pero incompletos o sin escenario de error | Menos de 4 casos o sin formato correcto |
| **P3 — UAT (20pts)** | 5 criterios en formato DADO/CUANDO/ENTONCES, específicos y medibles | Criterios en formato correcto pero ambiguos | Sin formato correcto o criterios vagos |
| **P4 — Análisis (10pts)** | Argumenta con criterio técnico y consideración del contexto crítico (salud) | Argumenta superficialmente | No argumenta o no considera el contexto |

---

---

## 📌 ACTIVIDADES COMPLEMENTARIAS TRANSVERSALES

*(Disponibles en cualquier momento de la Unidad 1)*

---

### 🎯 Actividad Bonus — "Inspecciona tu App Favorita"
### Tipo: Individual | Opcional | ⏱️ 45 min

**Misión:**
Elige una app móvil que uses regularmente (Instagram, Mercado Libre, Uber, WhatsApp, etc.).
Durante 30 minutos, úsala como un **tester profesional** y encuentra al menos:
- 2 pruebas funcionales que pasarían
- 1 prueba funcional que podrían mejorar
- 2 pruebas no funcionales que podrían hacerse
- 1 posible escenario de error que intentarías provocar

Documenta usando la plantilla de caso de prueba de la Evaluación U1.

---

### 🎯 Actividad Bonus — "El Test del Compañero"
### Tipo: Parejas | Opcional | ⏱️ 30 min

Intercambia con un/a compañero/a los casos de prueba que diseñaste en Actividad 2.1.
1. **Revisa** sus casos: ¿están completos? ¿son medibles? ¿falta algún escenario crítico?
2. **Agrega** al menos 2 casos que él/ella no haya considerado.
3. **Devuelve** con comentarios constructivos usando el formato: "Está bien porque... / Mejoraría... / Agregaría..."

---

### 🎯 Actividad Bonus — Glosario Colaborativo
### Tipo: Grupal | Ongoing | Foro EVA

Durante toda la unidad, el curso construye un **Glosario Colaborativo de Testing** en el foro EVA.

**Reglas:**
- Cada estudiante agrega mínimo 2 términos
- Cada término debe incluir: definición con palabras propias + ejemplo concreto + diferencia con un término similar
- No se pueden repetir términos
- Términos iniciales sugeridos: Error, Defecto, Falla, Prueba Unitaria, Prueba de Integración, Prueba de Sistema, Prueba de Aceptación, UAT, Caja Blanca, Caja Negra, Cobertura de Código, Regresión, Criterio de Aceptación

---

## 📎 Resumen Visual — Mapa de Actividades U1

```
SEMANA 1          SEMANA 2          SEMANA 3          SEMANA 4          SEMANA 5
─────────         ─────────         ─────────         ─────────         ─────────
                  
S1 ASÍNCRONA      S2 ASÍNCRONA      S3 ASÍNCRONA      S4 SINCRÓNICA     EVALUACIÓN
   ↓                  ↓                 ↓                 ↓                 ↓
🔍 Detective      🧪 Lab Pruebas    🏦 Banca UAT      ⬜⬛ Caja          🏆 AppSalud
   de Bugs           Unitarias         (Diseño de        Misteriosa        (Caso real
                                       criterios)        (Juego en         integrador)
🗣️ Foro:          🧩 Arquitecto                         vivo)
   ¿Probar o no?     de Integración                  🔨 StreamChile
                                                         QA Taller
                                                     ✅ Regresión
                                                         (Tarea)
```

---

## 📚 Recursos de Apoyo para las Actividades

| Recurso | Uso recomendado |
|---------|-----------------|
| Apunte N°1 — Niveles de Prueba | S1, S2, S3 — Base conceptual |
| Apunte N°2 — Tipos de Pruebas | S3, S4, S5 — Tipos y técnicas |
| Cuaderno de Ejercitación U1 | S2, S3 — Ejercicios adicionales |
| Requerimientos_Funcionales_Software.pdf | S3, S4, S5 — Para análisis práctico |
| Rúbrica U1 | S5 — Criterios de evaluación |
| [ISTQB Foundation](https://www.istqb.org) | Referencia profesional |
| [Platzi — Pruebas de Software](https://platzi.com/clases/1421-pruebas-software) | Videos complementarios |

---

*IF203IINF — Testing Aplicado al Desarrollo de Sistemas · IPSS · 2026*
*Elaborado con metodología Aprendizaje Basado en Problemas (ABP) — Barrows, 1986*
