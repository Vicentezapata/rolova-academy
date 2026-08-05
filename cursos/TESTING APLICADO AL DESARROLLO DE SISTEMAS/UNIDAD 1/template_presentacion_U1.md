# 🎨 Template de Presentación — Unidad 1
## Testing Aplicado al Desarrollo de Sistemas | IF203IINF
> **Instrucciones de uso:** Este template define la estructura y contenido de cada slide para las 4 sesiones de la Unidad 1. Cada sección corresponde a una presentación PowerPoint o similar. Adapta los ejemplos visuales según el contexto de tu clase.

---

# 🖥️ PRESENTACIÓN S1 — Introducción al Testing y Principios Fundamentales

---

## SLIDE 1 — Portada

```
╔══════════════════════════════════════════════════════╗
║                                                      ║
║   🔍 TESTING APLICADO AL DESARROLLO DE SISTEMAS     ║
║              IF203IINF · IPSS · 2026                ║
║                                                      ║
║         UNIDAD 1 — SESIÓN 1                          ║
║   Introducción al Testing y Principios Fundamentales ║
║                                                      ║
║   Docente: [Nombre del Docente]                      ║
║   Semana 1 · Modalidad Asíncrona                     ║
╚══════════════════════════════════════════════════════╝
```

**Elementos visuales:** Logo IPSS · Imagen fondo (código/testing) · Paleta de colores institucional

---

## SLIDE 2 — Índice / Agenda

### 📋 ¿Qué veremos hoy?

1. ¿Qué es el Testing de Software?
2. Error, Defecto y Falla — ¿Son lo mismo?
3. Principios Fundamentales del Testing
4. Objetivos del Testing
5. Tipos de Errores en el Software
6. Actividades y cierre

> ⏱️ **Duración estimada:** 4 horas (autoaprendizaje)

---

## SLIDE 3 — ¿Por qué importa el Testing?

### 💰 El Costo de NO Probar

**Dato clave:**
> El costo de corregir un error en **producción** puede ser hasta **100 veces** mayor que corregirlo en la fase de requerimientos.

**Caso real — Therac-25 (1985-1987):**
- Máquina de radioterapia controlada por software.
- Un error de condición de carrera → 6 pacientes recibieron sobredosis de radiación.
- 3 murieron directamente a causa del error.

**Lección:** El testing no es opcional; es una inversión.

---

## SLIDE 4 — ¿Qué es el Testing de Software?

### 🔍 Definición

> **Testing de Software:** Proceso de evaluación y verificación de que un software cumple sus requisitos y funciona correctamente bajo las condiciones esperadas.

### Objetivos principales:
- ✅ **Detectar defectos** antes de que lleguen al usuario
- ✅ **Validar** que el producto cumple las necesidades del cliente
- ✅ **Verificar** que el producto fue construido correctamente
- ✅ **Asegurar la calidad** del producto de software

### 📊 Diagrama:
```
Requerimientos → Diseño → Desarrollo → [TESTING] → Producción
                                             ↑
                              Detecta errores ANTES del usuario
```

---

## SLIDE 5 — Error, Defecto y Falla: ¿Son lo mismo?

### ⚠️ Tres conceptos clave

| Concepto | Definición | Quién lo causa | Ejemplo |
|----------|------------|----------------|---------|
| **Error (Mistake)** | Acción humana que produce un resultado incorrecto | Desarrollador | Escribir `if (x = 5)` en lugar de `if (x == 5)` |
| **Defecto (Bug/Fault)** | Imperfección introducida en el código | — | El código con `=` en lugar de `==` queda en el sistema |
| **Falla (Failure)** | Desviación del comportamiento esperado cuando el software se ejecuta | — | El sistema permite acceso cuando no debería |

### 🔗 Relación:
```
Error del programador → Introduce un Defecto → Que al ejecutarse produce una Falla
```

---

## SLIDE 6 — Principios Fundamentales del Testing (1/2)

### 📌 Los 7 Principios del Testing (ISTQB)

**Principio 1: El testing muestra la presencia de defectos**
> Las pruebas pueden probar que existen defectos, pero **no** que no existen.

**Principio 2: El testing exhaustivo es imposible**
> Es imposible probar todas las combinaciones de entradas y estados. Se prioriza por riesgo.

**Principio 3: El testing temprano ahorra tiempo y dinero**
> Las actividades de testing deben comenzar lo antes posible en el ciclo de vida.

**Principio 4: Agrupación de defectos (Pareto)**
> Un pequeño número de módulos contiene la mayoría de los defectos (regla 80/20).

---

## SLIDE 7 — Principios Fundamentales del Testing (2/2)

**Principio 5: La paradoja del pesticida**
> Si los mismos tests se repiten, eventualmente dejan de encontrar nuevos defectos. Revisar y actualizar regularmente.

**Principio 6: El testing depende del contexto**
> El testing de un banco difiere del testing de una app de juegos.

**Principio 7: La ilusión de la ausencia de defectos**
> Encontrar y corregir defectos no sirve si el sistema no cumple las necesidades del usuario.

---

## SLIDE 8 — Objetivos del Testing

### 🎯 ¿Para qué hacemos testing?

```
┌─────────────────────────────────────────────────┐
│  OBJETIVOS DEL TESTING                          │
│                                                 │
│  🔎 Detección temprana de defectos              │
│     Antes de que lleguen al usuario             │
│                                                 │
│  ✅ Validación                                  │
│     ¿Construimos el producto CORRECTO?          │
│     (necesidades del cliente)                   │
│                                                 │
│  ✔️ Verificación                                │
│     ¿Construimos el producto CORRECTAMENTE?     │
│     (especificaciones técnicas)                 │
│                                                 │
│  📈 Mejora continua                             │
│     Retroalimentación al equipo de desarrollo   │
└─────────────────────────────────────────────────┘
```

---

## SLIDE 9 — Tipos de Errores

### 🐛 Clasificación de Errores

**Por naturaleza:**
- **Funcionales:** El sistema no realiza la función esperada.  
  *Ej: El botón "Comprar" no agrega al carrito.*
- **No funcionales:** El sistema funciona, pero de forma inadecuada.  
  *Ej: La página tarda 30 segundos en cargar.*

**Por impacto:**
| Nivel | Descripción | Ejemplo |
|-------|-------------|---------|
| 🔴 Crítico | Paraliza el sistema | Login no funciona |
| 🟠 Alto | Funcionalidad importante no disponible | No se puede pagar |
| 🟡 Medio | Funcionalidad secundaria afectada | El filtro de búsqueda no ordena |
| 🟢 Bajo | Problema menor, no bloquea | Un botón mal alineado |

---

## SLIDE 10 — Actividad de la Sesión

### 💻 Tu turno — Análisis de caso real

**Instrucción:**
Investiga uno de los siguientes errores históricos de software:
- 🚀 Ariane 5 (1996) — Misil se destruye a sí mismo
- 🏥 Therac-25 (1985-1987) — Muertes por dosis de radiación
- 💻 Bug del año 2000 (Y2K)
- 💸 Flash Crash de Wall Street (2010)

**Responde:**
1. ¿Qué tipo de error fue (funcional/no funcional)?
2. ¿En qué fase del desarrollo fue introducido?
3. ¿Qué tipo de testing lo hubiera detectado?
4. ¿Cuál fue el impacto económico/social?

---

## SLIDE 11 — Cierre y Resumen S1

### ✅ ¿Qué aprendimos hoy?

- El testing es un **proceso esencial** del desarrollo de software.
- Error ≠ Defecto ≠ Falla (son conceptos distintos).
- Los **7 principios del testing** guían la práctica profesional.
- El testing tiene múltiples objetivos: detectar, validar, verificar, mejorar.
- Los errores se clasifican por naturaleza (funcional/no funcional) e impacto.

### 📌 Para la próxima sesión:
Leer el **Apunte N°1 — Niveles de Prueba**, secciones: Unitarias e Integración.

---
---

# 🖥️ PRESENTACIÓN S2 — Niveles de Prueba: Unitaria e Integración

---

## SLIDE 1 — Portada

```
╔══════════════════════════════════════════════════════╗
║                                                      ║
║   🔍 TESTING APLICADO AL DESARROLLO DE SISTEMAS     ║
║              IF203IINF · IPSS · 2026                ║
║                                                      ║
║         UNIDAD 1 — SESIÓN 2                          ║
║   Niveles de Prueba: Unitarias e Integración        ║
║                                                      ║
║   Semana 2 · Modalidad Asíncrona                     ║
╚══════════════════════════════════════════════════════╝
```

---

## SLIDE 2 — Índice

1. Los 4 Niveles de Prueba — Visión general
2. Pruebas Unitarias — Definición y características
3. Herramientas de pruebas unitarias
4. Pruebas de Integración — Definición y estrategias
5. ¿Cuándo usar cada nivel?
6. Ejemplo práctico integrador
7. Actividad práctica

---

## SLIDE 3 — Los 4 Niveles de Prueba

### 🏗️ Pirámide de Testing

```
              ┌─────────────┐
              │  ACEPTACIÓN │  ← Usuario/Cliente
              ├─────────────┤
              │   SISTEMA   │  ← Sistema completo
              ├─────────────┤
              │ INTEGRACIÓN │  ← Módulos combinados
              ├─────────────┤
              │   UNITARIA  │  ← Componente individual
              └─────────────┘
```

> ⬇️ **Abajo:** Más barato, más rápido, más frecuente  
> ⬆️ **Arriba:** Más costoso, más lento, menos frecuente  
> 💡 **Regla:** Más pruebas en la base = software más robusto

---

## SLIDE 4 — Pruebas Unitarias: ¿Qué son?

### 🔬 Definición

> Pruebas que evalúan el comportamiento de **unidades individuales de código** (funciones, métodos, clases) de forma **completamente aislada** del resto del sistema.

**¿Qué es una "unidad"?**
- Una función: `calcularDescuento(precio, porcentaje)`
- Un método de clase: `Usuario.autenticar(email, password)`
- Un componente UI: Botón de navegación

**¿Quién las hace?**
- 👨‍💻 **Los propios desarrolladores** (no el equipo de QA)

**¿Cuándo?**
- Durante la fase de **codificación**, no al final

---

## SLIDE 5 — Pruebas Unitarias: ¿Qué se prueba?

### 🧪 Escenarios de Prueba

```python
# Función a probar
def calcular_precio_final(precio_base, impuesto, descuento):
    return precio_base + (precio_base * impuesto) - descuento

# Casos de prueba
✅ Entrada válida:      calcular_precio_final(100, 0.19, 10) = 99
✅ Descuento cero:      calcular_precio_final(100, 0.19, 0) = 119
⚠️  Precio negativo:    calcular_precio_final(-100, 0.19, 0) → lanzar excepción
⚠️  Descuento mayor:   calcular_precio_final(100, 0.19, 200) → comportamiento esperado
⚠️  Valores nulos:     calcular_precio_final(None, 0.19, 0) → lanzar excepción
```

---

## SLIDE 6 — Herramientas de Pruebas Unitarias

### 🛠️ Frameworks por Lenguaje

| Lenguaje | Framework | Ejemplo de uso |
|----------|-----------|----------------|
| ☕ Java | JUnit 5 | `@Test void testCalcularPrecio()` |
| 🐍 Python | pytest | `def test_calcular_precio():` |
| 🟦 C# / .NET | NUnit / MSTest | `[Test] public void TestCalcular()` |
| 🌐 JavaScript | Jest | `test("calcula precio", () => { })` |
| 🐘 PHP | PHPUnit | `public function testCalcular()` |

**¿Por qué usar frameworks?**
- Ejecutar pruebas automáticamente.
- Reportes de resultados claros.
- Integración con CI/CD (pipelines).

---

## SLIDE 7 — Pruebas de Integración: ¿Qué son?

### 🔗 Definición

> Pruebas que evalúan la **interacción y comunicación** entre distintas unidades o componentes del software cuando trabajan **en conjunto**.

**¿Qué se verifica?**
- ✅ Datos transferidos correctamente entre módulos.
- ✅ APIs se comportan según lo esperado.
- ✅ No hay problemas de compatibilidad.
- ✅ La sincronización entre componentes es correcta.

**¿Quién las hace?**
- 👩‍💻 Desarrolladores + Equipo de QA

---

## SLIDE 8 — Estrategias de Integración

### 📐 4 Estrategias Principales

```
┌─────────────────────────────────────────────────────┐
│  BIG BANG                                           │
│  Módulo A + B + C + D → Probar todo junto          │
│  ✅ Rápido  ❌ Difícil aislar errores               │
├─────────────────────────────────────────────────────┤
│  BOTTOM-UP                                          │
│  Módulo D → D+C → D+C+B → D+C+B+A                 │
│  ✅ Errores de base detectados primero              │
├─────────────────────────────────────────────────────┤
│  TOP-DOWN                                           │
│  Módulo A → A+B → A+B+C → A+B+C+D                 │
│  ✅ Arquitectura validada temprano                  │
├─────────────────────────────────────────────────────┤
│  SANDWICH (MIXTA)                                   │
│  Combina Top-Down y Bottom-Up simultáneamente       │
│  ✅ Mayor cobertura  ❌ Mayor complejidad            │
└─────────────────────────────────────────────────────┘
```

---

## SLIDE 9 — Ejemplo Práctico: Sistema de Reservas de Vuelos

### ✈️ Caso de Estudio

**Sistema:** Plataforma de reserva de vuelos en línea.

| Nivel | ¿Qué se prueba? | Ejemplo concreto |
|-------|-----------------|------------------|
| **Unitaria** | Función individual | `calcularPrecioFinal(base, impuesto, descuento)` devuelve el valor correcto |
| **Integración** | Módulos combinados | El módulo de búsqueda de vuelos consulta correctamente al módulo de disponibilidad de asientos |

**Diagrama de integración:**
```
[Módulo Búsqueda] --solicitud--> [Módulo Disponibilidad]
                  <--respuesta--
                  
Prueba: ¿Los datos llegan completos? ¿El formato es correcto? ¿El tiempo de respuesta es aceptable?
```

---

## SLIDE 10 — Actividad S2

### 💻 Ejercicio: Sistema de E-commerce

**Dado el siguiente sistema:**
```
┌─────────────────────────────────────────────────┐
│  Sistema de Compra en Línea                     │
│                                                 │
│  [Módulo Login] → [Módulo Catálogo]             │
│       ↓                   ↓                    │
│  [Módulo Carrito] → [Módulo Pago]               │
│                           ↓                    │
│               [Módulo Confirmación]             │
└─────────────────────────────────────────────────┘
```

**Identifica y describe:**
1. **3 pruebas unitarias** (una por módulo a elección).
2. **2 pruebas de integración** entre módulos.
3. ¿Qué estrategia de integración usarías y por qué?

---

## SLIDE 11 — Cierre y Resumen S2

### ✅ ¿Qué aprendimos hoy?

- Las **pruebas unitarias** evalúan componentes individuales; las hacen los desarrolladores.
- Las **pruebas de integración** evalúan la interacción entre módulos.
- Existen 4 estrategias de integración: Big Bang, Bottom-Up, Top-Down, Sandwich.
- Los frameworks (JUnit, pytest, Jest) automatizan las pruebas unitarias.

### 📌 Para la próxima sesión:
Leer **Apunte N°1** secciones: Sistema y Aceptación. Revisar Requerimientos_Funcionales_Software.pdf.

---
---

# 🖥️ PRESENTACIÓN S3 — Niveles de Prueba: Sistema y Aceptación

---

## SLIDE 1 — Portada

```
╔══════════════════════════════════════════════════════╗
║   🔍 TESTING APLICADO AL DESARROLLO DE SISTEMAS     ║
║              IF203IINF · IPSS · 2026                ║
║                                                      ║
║         UNIDAD 1 — SESIÓN 3                          ║
║   Niveles de Prueba: Sistema y Aceptación           ║
║   Semana 3 · Modalidad Asíncrona                     ║
╚══════════════════════════════════════════════════════╝
```

---

## SLIDE 2 — Pruebas de Sistema: ¿Qué son?

### 🖥️ Definición

> Pruebas que evalúan el software en su **totalidad**, como sistema completo e integrado, bajo **condiciones realistas** de operación.

**Objetivo:** Verificar que el sistema cumpla con **todos** sus requisitos funcionales y no funcionales.

**¿Quién las ejecuta?**
- 🧪 Equipo de QA / Testers especializados (no los desarrolladores)

**¿Cuándo?**
- Después de las pruebas de integración, antes de la aceptación.

---

## SLIDE 3 — ¿Qué se evalúa en Pruebas de Sistema?

### 📋 Checklist de Pruebas de Sistema

| ✅ | Aspecto | Ejemplo |
|----|---------|---------|
| ✅ | Flujos de trabajo completos | Proceso completo de compra (desde búsqueda hasta pago) |
| ✅ | Interfaces de usuario | Navegación, formularios, mensajes de error |
| ✅ | APIs y servicios externos | Integración con pasarela de pago |
| ✅ | Rendimiento | 1000 usuarios simultáneos sin degradación |
| ✅ | Seguridad | No se puede acceder sin autenticación |
| ✅ | Usabilidad | El flujo es intuitivo para el usuario |
| ✅ | Compatibilidad | Funciona en Chrome, Firefox, Safari, Edge |
| ✅ | Recuperación ante fallos | Ante caída del servidor, muestra error amigable |

---

## SLIDE 4 — Tipos de Pruebas dentro del Nivel Sistema

### 📊 Clasificación

| Tipo | ¿Qué evalúa? | Herramientas |
|------|-------------|--------------|
| **Rendimiento** | Velocidad, estabilidad bajo carga | JMeter, k6, Gatling |
| **Seguridad** | Vulnerabilidades, accesos no autorizados | OWASP ZAP, Burp Suite |
| **Usabilidad** | Facilidad de uso, experiencia del usuario | Pruebas con usuarios reales |
| **Compatibilidad** | Funcionamiento en distintos entornos | BrowserStack, Selenium Grid |
| **Recuperación** | Comportamiento ante fallos | Pruebas de caos (Chaos Engineering) |

---

## SLIDE 5 — Pruebas de Aceptación: ¿Qué son?

### 🤝 Definición

> **Última etapa de QA** antes de que el software vaya a producción. Verifica que el producto cumpla las expectativas de los **usuarios finales y el cliente**.

**La gran pregunta de las pruebas de aceptación:**
> *¿El software hace lo que el cliente necesita, de la forma en que lo necesita?*

**No se trata de encontrar bugs** — se trata de **validar** que el producto es el correcto.

---

## SLIDE 6 — Actores en las Pruebas de Aceptación

### 👥 ¿Quién realiza las pruebas UAT?

| Actor | Rol | Ventaja |
|-------|-----|---------|
| 🧑‍💼 **Usuarios Finales** | Prueban desde su experiencia diaria | Perspectiva real del usuario |
| 👔 **Representantes del Cliente** | Intermediarios con conocimiento del negocio | Conocen los requisitos en profundidad |
| 🔬 **Equipos de QA Independientes** | Evaluación objetiva y externa | Sin sesgo del equipo de desarrollo |

---

## SLIDE 7 — Tipos de Pruebas de Aceptación

### 📋 4 Tipos Principales

| Tipo | Sigla | Descripción | ¿Quién? |
|------|-------|-------------|---------|
| **User Acceptance Testing** | UAT | Usabilidad y satisfacción del usuario final | Usuarios |
| **Business Acceptance Testing** | BAT | Cumplimiento de objetivos del negocio | Stakeholders |
| **Aceptación de Integración** | — | Integración con sistemas externos existentes | QA + Clientes |
| **Aceptación del Sistema** | SAT | Sistema completo en su entorno operativo final | QA |

---

## SLIDE 8 — Criterios de Aceptación

### 📝 ¿Qué son los Criterios de Aceptación?

> Condiciones claras y medibles que determinan si un software **cumple o no cumple** los requisitos del usuario.

**Ejemplo — Funcionalidad: Login de Usuario**

| # | Criterio de Aceptación | Resultado Esperado |
|---|------------------------|--------------------|
| 1 | El usuario ingresa credenciales correctas | Redirige al dashboard en < 2 segundos |
| 2 | El usuario ingresa contraseña incorrecta | Muestra mensaje "Contraseña incorrecta. Intento 1/3" |
| 3 | El usuario falla 3 veces | La cuenta se bloquea por 15 minutos |
| 4 | El usuario olvida su contraseña | Botón "¿Olvidaste tu contraseña?" disponible |
| 5 | La sesión expira sin actividad | El sistema cierra sesión automáticamente tras 30 minutos |

---

## SLIDE 9 — Relación entre los 4 Niveles

### 🔄 El Flujo de Niveles de Prueba

```
FASE DE DESARROLLO          QUIÉN PRUEBA          OBJETIVO
─────────────────────────────────────────────────────────────
📝 Codificación         → Desarrollador      → Pruebas UNITARIAS
                                                (¿Funciona la unidad?)

🔗 Integración          → Dev + QA           → Pruebas INTEGRACIÓN
                                                (¿Funcionan juntos?)

🖥️ Sistema completo     → Equipo QA          → Pruebas SISTEMA
                                                (¿Funciona el sistema?)

✅ Pre-producción       → Usuario / Cliente  → Pruebas ACEPTACIÓN
                                                (¿Es lo que necesitamos?)
                                                          ↓
🚀 PRODUCCIÓN
```

> 💡 En metodologías **ágiles**, estos niveles se superponen en cada sprint.

---

## SLIDE 10 — Actividad S3

### 💻 Ejercicio: Sistema de Biblioteca Digital

**Funcionalidad:** Un usuario puede buscar libros, reservarlos y recibirlos por correo electrónico.

**Tarea 1 — Prueba de Sistema:**  
Diseña 3 pruebas de sistema para esta funcionalidad. Incluye: tipo de prueba, qué se prueba, resultado esperado.

**Tarea 2 — Criterios de Aceptación UAT:**  
Escribe 5 criterios de aceptación para la funcionalidad "Buscar libro por ISBN".

**Formato de entrega:**
```
Prueba de Sistema N°1:
- Tipo: [Rendimiento / Seguridad / Funcional / etc.]
- ¿Qué se prueba?: [Descripción]
- Resultado esperado: [Descripción]
```

---

## SLIDE 11 — Cierre y Resumen S3

### ✅ ¿Qué aprendimos hoy?

- Las **pruebas de sistema** evalúan el software completo bajo condiciones realistas.
- Las **pruebas de aceptación** validan que el producto cumple las necesidades reales del usuario.
- Los criterios de aceptación deben ser **claros, medibles y acordados** con el cliente.
- Los 4 niveles forman un proceso progresivo desde lo más básico hasta lo más completo.

### 📌 Para la próxima sesión (SINCRÓNICA):
Revisar el **Apunte N°2 (Tipos de Pruebas)** completo. La sesión S4 es en Teams — ¡asistencia obligatoria!

---
---

# 🖥️ PRESENTACIÓN S4 (SINCRÓNICA) — Tipos de Pruebas

---

## SLIDE 1 — Portada

```
╔══════════════════════════════════════════════════════╗
║   🔍 TESTING APLICADO AL DESARROLLO DE SISTEMAS     ║
║              IF203IINF · IPSS · 2026                ║
║                                                      ║
║         UNIDAD 1 — SESIÓN 4 (SINCRÓNICA)             ║
║   Tipos de Pruebas: Caja Blanca, Caja Negra,        ║
║   Funcionales, No Funcionales y Regresión           ║
║                                                      ║
║   Semana 4 · Microsoft Teams                         ║
╚══════════════════════════════════════════════════════╝
```

---

## SLIDE 2 — Agenda de la Sesión Sincrónica

| Tiempo | Actividad |
|--------|-----------|
| 0:00 - 1:00 | Presentación docente: Caja Blanca y Caja Negra |
| 1:00 - 1:30 | Actividad en vivo: Clasificación de casos de prueba |
| 1:30 - 2:15 | Presentación docente: Funcionales y No Funcionales |
| 2:15 - 3:00 | Trabajo en grupos: Diseño de casos de prueba |
| 3:00 - 3:30 | Plenaria y cierre de unidad |
| 3:30 - 3:45 | Instrucciones de Evaluación U1 |

---

## SLIDE 3 — ¿Qué hemos visto hasta ahora?

### 🗺️ Mapa de la Unidad 1

```
SESIÓN 1: Principios y Objetivos del Testing
          ↓
SESIÓN 2: Niveles → Unitaria + Integración
          ↓
SESIÓN 3: Niveles → Sistema + Aceptación
          ↓
SESIÓN 4: Tipos → Caja Blanca / Caja Negra / Funcional / No Funcional
          ↓
SESIÓN 5: EVALUACIÓN SUMATIVA
```

---

## SLIDE 4 — Caja Blanca vs. Caja Negra

### ⬜⬛ La Gran Diferencia

```
┌─────────────────────┐        ┌─────────────────────┐
│   CAJA BLANCA       │        │   CAJA NEGRA        │
│  (White Box)        │        │  (Black Box)        │
│                     │        │                     │
│  El tester VE       │        │  El tester NO VE    │
│  el código fuente   │        │  el código fuente   │
│                     │        │                     │
│  Evalúa la          │        │  Evalúa el          │
│  ESTRUCTURA interna │        │  COMPORTAMIENTO     │
│  del software       │        │  externo            │
│                     │        │                     │
│  🔍 Enfocado en     │        │  👤 Enfocado en     │
│  la implementación  │        │  el usuario         │
└─────────────────────┘        └─────────────────────┘
```

---

## SLIDE 5 — Pruebas de Caja Blanca

### ⬜ White Box Testing — En Profundidad

**Metodologías principales:**

| Método | ¿Qué hace? | Ejemplo |
|--------|------------|---------|
| **Cobertura de Código** | Mide % de código ejecutado | "El 85% del código fue ejecutado por las pruebas" |
| **Basadas en Caminos** | Identifica todos los flujos posibles | Probar cada rama del IF-ELSE |
| **Basadas en Condiciones** | Evalúa cada condición lógica | True y False para cada condición |

**Cobertura de código — ejemplo visual:**
```python
def categorizar_edad(edad):
    if edad < 18:           # ← ¿Se probó con edad < 18?
        return "Menor"
    elif edad < 65:         # ← ¿Se probó con 18 <= edad < 65?
        return "Adulto"
    else:                   # ← ¿Se probó con edad >= 65?
        return "Adulto mayor"
```
> 3 caminos → se necesitan mínimo 3 casos de prueba para cobertura de 100%.

---

## SLIDE 6 — Pruebas de Caja Negra

### ⬛ Black Box Testing — En Profundidad

**El tester actúa como usuario final:**
- Envía **entradas** al sistema.
- Observa las **salidas**.
- No importa **cómo** está implementado internamente.

**Tipos dentro de Caja Negra:**
- **Funcionales:** ¿El login funciona? ¿El carrito suma correctamente?
- **Usabilidad:** ¿Es intuitivo? ¿Los mensajes de error son claros?
- **Compatibilidad:** ¿Funciona en Chrome y Firefox igualmente?

**Técnicas de diseño de casos:**
- **Partición de equivalencias:** Agrupar entradas equivalentes.
- **Valores límite:** Probar en los bordes (0, 1, máximo, máximo-1).
- **Tablas de decisión:** Para lógica compleja con múltiples condiciones.

---

## SLIDE 7 — Funcionales vs. No Funcionales

### 📊 Comparativa Completa

| | Pruebas Funcionales | Pruebas No Funcionales |
|-|---------------------|------------------------|
| **Pregunta central** | ¿El sistema hace lo correcto? | ¿El sistema funciona BIEN? |
| **Basadas en** | Requisitos funcionales / Casos de uso | Atributos de calidad |
| **Ejemplo simple** | El botón "Comprar" agrega al carrito | La página carga en menos de 2 segundos |
| **Ejemplo complejo** | El cálculo de impuestos es correcto | El sistema soporta 10.000 usuarios simultáneos |
| **Herramientas** | Selenium, Cypress, Postman | JMeter, k6, OWASP ZAP |

---

## SLIDE 8 — Atributos de Calidad No Funcionales

### 🏆 Los Grandes Atributos

```
RENDIMIENTO   → ¿Qué tan rápido? ¿Bajo qué carga?
SEGURIDAD     → ¿Está protegido contra ataques?
USABILIDAD    → ¿Es fácil e intuitivo de usar?
FIABILIDAD    → ¿Opera sin fallos durante períodos largos?
ESCALABILIDAD → ¿Puede crecer con la demanda?
COMPATIBILIDAD → ¿Funciona en distintos entornos?
MANTENIBILIDAD → ¿Es fácil de actualizar y modificar?
```

**Ejemplo de prueba no funcional — Rendimiento:**
> "El sistema debe procesar 500 transacciones por segundo con un tiempo de respuesta menor a 200ms para el 95% de las peticiones."

---

## SLIDE 9 — Pruebas de Regresión

### 🔄 ¿Qué es una Prueba de Regresión?

> Verificar que los **cambios realizados** al código (corrección de bugs, nuevas funcionalidades, refactoring) **no hayan roto** lo que ya funcionaba correctamente.

**¿Cuándo se ejecutan?**
- ✅ Después de corregir un defecto.
- ✅ Después de agregar una nueva funcionalidad.
- ✅ Antes de cada release o despliegue.
- ✅ En cada commit (con CI/CD automatizado).

**Proceso:**
```
Cambio en el código
       ↓
Identificar áreas afectadas
       ↓
Ejecutar suite de regresión
       ↓
¿Nuevos errores? → Reportar y corregir
       ↓
✅ Todo OK → Continuar con el release
```

---

## SLIDE 10 — Síntesis Final: Mapa de Tipos de Prueba

### 🗺️ Todo el Universo del Testing

```
╔══════════════════════════════════════════════════╗
║  PRUEBAS DE SOFTWARE                             ║
║                                                  ║
║  Por NIVEL          Por TÉCNICA                  ║
║  ─────────          ────────────                 ║
║  • Unitarias        • Caja Blanca (ve código)    ║
║  • Integración      • Caja Negra (no ve código)  ║
║  • Sistema                                       ║
║  • Aceptación       Por NATURALEZA               ║
║                     ─────────────                ║
║  Por PROPÓSITO      • Funcionales                ║
║  ───────────────    • No Funcionales             ║
║  • Regresión                                     ║
║  • Componentes                                   ║
║  • UAT / BAT                                     ║
╚══════════════════════════════════════════════════╝
```

---

## SLIDE 11 — Actividad Grupal en Teams

### 👥 Ejercicio: Sistema de Biblioteca Digital

**Grupos de 3 personas — 45 minutos**

**Sistema:** App para buscar, reservar y recibir libros digitales.

**Parte 1 — Caja Negra (2 casos):**
```
Caso N°1:
- Funcionalidad: [Ej: "Buscar libro por ISBN"]
- Entradas: [Ej: "ISBN = 978-3-16-148410-0"]
- Resultado esperado: [Ej: "Muestra ficha del libro en < 1 segundo"]
- Tipo: [Funcional / No funcional]
```

**Parte 2 — No Funcionales (2 casos):**
Diseña pruebas de rendimiento y seguridad para el sistema.

**Presentación:** Cada grupo expone sus 4 casos al curso.

---

## SLIDE 12 — Evaluación U1 — Instrucciones

### 📋 ¿Qué evalúa la U1?

**Tipo:** Situación problemática (caso de sistema real)  
**Plazo:** Indicado en EVA  
**Ponderación:** 10% de la nota final  
**Instrumento:** Rúbrica disponible en EVA

**Lo que debes hacer:**
1. ✅ Identificar niveles y tipos de prueba pertinentes al caso.
2. ✅ Justificar la selección con argumentos técnicos.
3. ✅ Diseñar al menos 3 casos de prueba concretos.
4. ✅ Analizar qué errores detectaría cada prueba.

**Criterios de Rúbrica:**
- Identificación de niveles (25%)
- Selección de tipos de prueba (25%)
- Diseño de casos (30%)
- Análisis y justificación (20%)

---

## SLIDE 13 — Cierre de la Unidad 1

### 🏁 ¿Qué logramos en la Unidad 1?

✅ Comprender los principios y objetivos del testing de software.  
✅ Distinguir los 4 niveles de prueba: Unitaria, Integración, Sistema, Aceptación.  
✅ Identificar y aplicar distintos tipos de prueba: Caja Blanca, Caja Negra, Funcional, No Funcional, Regresión.  
✅ Analizar escenarios reales para seleccionar el tipo y nivel de prueba adecuado.  
✅ Diseñar casos de prueba básicos con criterios de aceptación.

### 🚀 Próxima unidad:
**Unidad 2 — Planificación y Construcción de Planes de Prueba**  
(Gherkin, Historias de Usuario, Matrices de Prueba)

---
*IF203IINF — Testing Aplicado al Desarrollo de Sistemas · IPSS · 2026*
