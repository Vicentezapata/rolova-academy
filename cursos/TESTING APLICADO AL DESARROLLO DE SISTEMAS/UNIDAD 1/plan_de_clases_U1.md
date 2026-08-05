# 📘 Plan de Clases — Unidad 1
## Testing Aplicado al Desarrollo de Sistemas | IF203IINF
### Carrera: Ingeniería en Informática · 5° Trimestre · IPSS

---

## 🎯 Descripción General de la Unidad

**Nombre de la Unidad:** Competencia en Testing de Software  
**Código:** UA 1 — Unidad de Competencia I  
**Horas totales:** 20 horas (teoría + práctica)  
**Evaluación:** Situación problemática (Rúbrica) — Ponderación: 10%

### Resultado de Aprendizaje Central
> *"Aplica los principios, objetivos del testing, niveles y tipos de pruebas, además de su importancia en el ciclo de vida del desarrollo de software."*

### Resultados de Aprendizaje Específicos

| N° | Resultado de Aprendizaje | Indicadores de Logro |
|----|--------------------------|----------------------|
| 1 | Aplica los principios y objetivos del testing en el desarrollo de software | 1.1 Identifica errores efectivamente · 1.2 Aplica métodos apropiados · 1.3 Usa herramientas de análisis |
| 2 | Analiza los distintos tipos de pruebas y sus objetivos | 2.1 Distingue pruebas unitarias/integración/sistema/aceptación · 2.2 Determina idoneidad · 2.3 Analiza resultados |

---

## 📅 Distribución de Sesiones — Unidad 1

| Sesión | Nombre | Modalidad | Horas | Semana |
|--------|--------|-----------|-------|--------|
| S1 | Introducción al Testing y Principios Fundamentales | Asíncrona | 4h | 1 |
| S2 | Niveles de Prueba: Unitaria e Integración | Asíncrona | 4h | 2 |
| S3 | Niveles de Prueba: Sistema y Aceptación | Asíncrona | 4h | 3 |
| S4 | Tipos de Pruebas: Caja Blanca, Negra, Funcionales | Sincrónica (Teams) | 4h | 4 |
| S5 | Evaluación Sumativa U1 — Situación Problemática | Evaluación | 4h | 5 |

---

## 📖 SESIÓN 1 — Introducción al Testing y Principios Fundamentales

### 📌 Datos Generales
- **Modalidad:** Asíncrona (EVA)  
- **Duración:** 4 horas · **Semana:** 1

### 🎯 Objetivos de la Clase
1. Explicar qué es el testing de software y su relevancia.
2. Identificar los principios fundamentales del testing.
3. Distinguir entre error, defecto y falla.
4. Comprender los objetivos del testing: detección temprana, aseguramiento de calidad, validación y verificación.

### 📚 Contenidos

#### 1. ¿Qué es el Testing de Software? (60 min)
- **Definición:** Proceso de evaluación de software para verificar que cumple los requisitos y funciona correctamente.
- **Evolución histórica:** Desde pruebas informales hasta disciplinas sistemáticas.
- **Conceptos clave:**
  - **Error (mistake):** Acción humana que produce resultado incorrecto.
  - **Defecto (bug/fault):** Imperfección en el componente.
  - **Falla (failure):** Desviación del resultado esperado.

#### 2. Principios Fundamentales del Testing (60 min)
- **Exhaustividad vs. completitud:** No es posible probar todo; se prioriza según riesgo.
- **Agrupación de defectos:** Los errores tienden a concentrarse en módulos específicos (Pareto).
- **Ilusión de ausencia de errores:** Pasar todas las pruebas no garantiza software perfecto.
- **Detección temprana:** Corregir errores en etapas tempranas cuesta menos.
- **Testing depende del contexto:** No existe un enfoque único válido.

#### 3. Objetivos del Testing (45 min)
- **Detección temprana de defectos** antes de que lleguen al usuario.
- **Validación:** ¿Construimos el producto correcto? (satisface necesidades del usuario).
- **Verificación:** ¿Construimos el producto correctamente? (cumple especificaciones técnicas).
- **Mejora continua:** El testing retroalimenta el proceso de desarrollo.

#### 4. Tipos de Errores en el Software (45 min)
- **Funcionales:** El sistema no hace lo que debería.
- **No funcionales:** El sistema hace lo correcto, pero mal (lento, inseguro, etc.).
- **Clasificación por impacto:** Crítico / Alto / Medio / Bajo.

### 🔧 Actividades

| Actividad | Tipo | Duración | Descripción |
|-----------|------|----------|-------------|
| Lectura guiada | Individual | 30 min | Leer introducción del Apunte N°1 (Niveles de Prueba) |
| Caso de análisis | Individual | 30 min | Analizar un error famoso (Ej: Bug del año 2000, Therac-25) — ¿qué falló, en qué fase, cuál fue el impacto? |
| Foro de reflexión | Grupal | 20 min | ¿Por qué el testing es más que "buscar errores"? |
| Quiz formativo | Individual | 10 min | 5 preguntas en EVA (solo feedback, sin nota) |

### ❓ Preguntas de Activación
1. ¿En qué medida la detección temprana de errores reduce los costos de desarrollo?
2. ¿Cuál es la diferencia entre validar y verificar un software?
3. ¿Podría un software pasar todas las pruebas y aún fallar en producción?

### 📎 Recursos
- Apunte activador N°1: Niveles de Prueba
- Video complementario de introducción al Testing
- [Niveles de prueba - Platzi](https://platzi.com/clases/1421-pruebas-software/15099-niveles-de-pruebas/)

---

## 📖 SESIÓN 2 — Niveles de Prueba: Pruebas Unitarias y de Integración

### 📌 Datos Generales
- **Modalidad:** Asíncrona (EVA) · **Duración:** 4 horas · **Semana:** 2

### 🎯 Objetivos de la Clase
1. Definir y caracterizar las pruebas unitarias.
2. Explicar las pruebas de integración y sus estrategias.
3. Distinguir cuándo aplicar cada nivel.
4. Identificar herramientas de testing unitario (JUnit, pytest, NUnit).

### 📚 Contenidos

#### 1. Pruebas Unitarias — Unit Testing (90 min)

> Pruebas que evalúan el comportamiento individual de pequeñas unidades de código (funciones, métodos, componentes) de forma independiente.

**Características clave:**
- Realizadas por **los desarrolladores** durante la fase de codificación.
- Permiten detección **temprana y eficiente** de errores.
- Fomentan **código modular y bien estructurado**.

**¿Qué se prueba?**
- Entradas válidas → resultado correcto.
- Entradas inválidas → manejo adecuado (excepciones, errores).
- Casos límite (valores frontera, null, vacío).

**Herramientas principales:**

| Lenguaje | Framework |
|----------|-----------|
| Java | JUnit |
| Python | pytest, unittest |
| .NET / C# | NUnit, MSTest |
| JavaScript | Jest, Mocha |

**Ventajas:** Código más confiable · Facilita mantenimiento · Acelera el ciclo.  
**Desventajas:** Tiempo adicional · Difícil probar con dependencias externas.

#### 2. Pruebas de Integración — Integration Testing (90 min)

> Pruebas que evalúan la interacción y comunicación entre distintas unidades o componentes cuando se combinan.

**¿Qué se verifica?**
- Transferencia correcta de datos entre módulos.
- Comportamiento de interfaces (APIs).
- Ausencia de problemas de compatibilidad.

**Estrategias:**

| Estrategia | Descripción | Ventaja | Desventaja |
|------------|-------------|---------|------------|
| Big Bang | Todos los componentes integrados de una vez | Rápido (proyectos pequeños) | Difícil localizar errores |
| Bottom-Up | Primero los componentes más básicos | Errores en base detectados antes | Módulos superiores al final |
| Top-Down | Primero los módulos de nivel superior | Arquitectura validada temprano | Requiere stubs |
| Sandwich | Combina Top-Down y Bottom-Up | Mayor cobertura | Mayor complejidad |

### 🔧 Actividades

| Actividad | Tipo | Duración | Descripción |
|-----------|------|----------|-------------|
| Lectura apunte | Individual | 40 min | Sección Unitaria e Integración del Apunte N°1 |
| Ejercicio de identificación | Individual | 30 min | Sistema de comercio electrónico: ¿qué se probaría en cada nivel? |
| Cuaderno de ejercitación | Individual | 40 min | Resolver ejercicios del Cuaderno U1 |
| Compruebo mi aprendizaje | Individual | 10 min | Responder preguntas 1-4 del apunte |

### ❓ Preguntas de Activación
1. ¿Por qué las pruebas unitarias son responsabilidad del desarrollador y no del tester?
2. Si 5 módulos funcionan bien individualmente, ¿el sistema completo funcionará bien? ¿Por qué?
3. ¿Cuándo usarías Big Bang vs. Bottom-Up?

### 📝 Ejemplo Práctico
**Sistema de reserva de vuelos:**
- **Unitaria:** Probar la función `calcularPrecioFinal(precioBase, impuesto, descuento)`.
- **Integración:** Probar que el módulo de búsqueda de vuelos se comunica con el módulo de disponibilidad de asientos.

---

## 📖 SESIÓN 3 — Niveles de Prueba: Pruebas de Sistema y Aceptación

### 📌 Datos Generales
- **Modalidad:** Asíncrona (EVA) · **Duración:** 4 horas · **Semana:** 3

### 🎯 Objetivos de la Clase
1. Definir y caracterizar las pruebas de sistema.
2. Explicar las pruebas de aceptación y sus actores.
3. Comprender la relación entre niveles y el ciclo de vida del software.
4. Analizar escenarios prácticos para determinar el nivel adecuado.

### 📚 Contenidos

#### 1. Pruebas de Sistema — System Testing (90 min)

> Evalúan el software en su totalidad como sistema completo e integrado, bajo condiciones realistas.

**¿Qué se evalúa?**

| Aspecto | Descripción |
|---------|-------------|
| Flujos de trabajo completos | Simular escenarios reales de uso |
| Interfaces | Verificar UI, APIs y conexiones externas |
| Comunicación entre componentes | Sincronización, integridad de datos |
| Requisitos funcionales | Que el sistema haga lo que debe hacer |
| Requisitos no funcionales | Rendimiento, seguridad, usabilidad, compatibilidad |

**Tipos de pruebas de sistema:**

| Tipo | Descripción |
|------|-------------|
| Rendimiento | Comportamiento bajo carga |
| Seguridad | Vulnerabilidades, accesos no autorizados |
| Usabilidad | Facilidad de uso, interfaz intuitiva |
| Recuperación | Capacidad de recuperarse ante fallos |
| Compatibilidad | Funcionamiento en distintos SO/navegadores |

#### 2. Pruebas de Aceptación — Acceptance Testing (90 min)

> Última etapa de QA. Verifica que el software cumpla con los requisitos y expectativas de los usuarios finales o clientes.

**Actores:**

| Actor | Rol |
|-------|-----|
| Usuarios Finales | Validan desde su experiencia práctica |
| Representantes del Cliente | Intermediarios con conocimiento del negocio |
| Equipos de QA Independientes | Perspectiva objetiva |

**Tipos de Pruebas de Aceptación:**

| Tipo | Sigla | Descripción |
|------|-------|-------------|
| Pruebas de Aceptación del Usuario | UAT | Usabilidad y satisfacción del usuario final |
| Pruebas de Aceptación del Negocio | BAT | Cumplimiento de objetivos comerciales |
| Pruebas de Aceptación de Integración | — | Integración con sistemas externos |

**Flujo general de niveles:**
```
Unitarias → Integración → Sistema → Aceptación
Desarrollador   Dev+QA       QA      Usuario/Cliente
```
> En metodologías ágiles los niveles se superponen y ejecutan en paralelo.

### 🔧 Actividades

| Actividad | Tipo | Duración | Descripción |
|-----------|------|----------|-------------|
| Análisis de requerimientos | Individual | 30 min | Leer Requerimientos_Funcionales_Software.pdf e identificar qué prueba de sistema aplicarías |
| Mapa de niveles | Parejas | 40 min | Sistema bancario: mapear qué se prueba en cada nivel con ejemplos |
| Diseño de criterios UAT | Individual | 40 min | Para "Iniciar sesión", redactar 5 criterios de aceptación medibles |
| Preguntas de activación | Individual | 10 min | Responder preguntas 11-14 del Apunte N°2 |

### ❓ Preguntas de Activación
1. ¿Qué diferencia hay entre prueba de sistema y prueba de aceptación?
2. ¿Por qué es importante que los usuarios finales participen en las pruebas UAT?
3. ¿Qué sucede si el sistema pasa las pruebas de sistema pero falla en las de aceptación?

---

## 📖 SESIÓN 4 (SINCRÓNICA) — Tipos de Pruebas: Caja Blanca, Caja Negra, Funcionales y No Funcionales

### 📌 Datos Generales
- **Modalidad:** Sincrónica (Microsoft Teams) · **Duración:** 4 horas · **Semana:** 4

### 🎯 Objetivos de la Clase
1. Distinguir entre pruebas de caja blanca y caja negra.
2. Identificar pruebas funcionales y no funcionales con ejemplos reales.
3. Reconocer pruebas de regresión y su importancia.
4. Aplicar criterios de selección de tipo de prueba según contexto.

### 📚 Contenidos

#### 1. Pruebas de Caja Blanca — White Box Testing (60 min)

> Análisis del código fuente para identificar errores. El tester **conoce la implementación interna**.

**Metodologías:**

| Método | Descripción |
|--------|-------------|
| Cobertura de Código | Medir % de código ejecutado |
| Basadas en Caminos | Identificar todos los caminos posibles |
| Basadas en Condiciones | Evaluar cada condición lógica |

**Ventajas:** Mayor profundidad · Enfoque en causa raíz · Prevención temprana.  
**Desventajas:** Requiere código fuente · Mayor dificultad · Mayor tiempo.

#### 2. Pruebas de Caja Negra — Black Box Testing (60 min)

> Se evalúa el software desde la **perspectiva del usuario**, sin acceso al código. Solo entradas → salidas.

**Proceso:** Especificación de requisitos → Diseño de casos → Ejecución → Comparación → Reporte.

**Ventajas:** Imparcialidad · Enfoque en usuario · No requiere programación.  
**Desventajas:** No garantiza cobertura del código · Difícil identificar causa raíz.

#### 3. Funcionales vs. No Funcionales (45 min)

| Aspecto | Pruebas Funcionales | Pruebas No Funcionales |
|---------|---------------------|------------------------|
| ¿Qué evalúa? | "¿El sistema HACE lo correcto?" | "¿El sistema funciona BIEN?" |
| Basadas en | Requisitos funcionales | Atributos de calidad |
| Ejemplos | Login funciona, carrito agrega productos | Tiempo de respuesta < 2s |
| Atributos | Funcionalidad, corrección | Rendimiento, seguridad, usabilidad, escalabilidad |

#### 4. Pruebas de Regresión (30 min)

> Verificar que los cambios en el código **no hayan introducido nuevos errores** ni afectado funcionalidades validadas.

**¿Cuándo se ejecutan?** Después de corregir un bug · Después de añadir funcionalidades · Antes de cada release.

### 🔧 Actividades Sincrónicas (Teams)

| Actividad | Tipo | Duración | Descripción |
|-----------|------|----------|-------------|
| Presentación docente | Exposición | 60 min | Explicación con PPT y ejemplos en vivo |
| Clasificación de casos | Grupal | 30 min | Clasificar 10 casos de prueba: Caja Blanca / Negra / Funcional / No Funcional |
| Caso práctico | Grupos de 3 | 45 min | Sistema de biblioteca digital: 2 casos de caja negra + 2 no funcionales |
| Cierre y preguntas | Plenaria | 20 min | Resolución de dudas, síntesis de unidad |
| Instrucciones de evaluación | Individual | 15 min | Explicación Evaluación U1 |

### 🧩 Síntesis — Mapa de Tipos de Prueba

```
PRUEBAS DE SOFTWARE
├── Por NIVEL
│   ├── Unitarias · Integración · Sistema · Aceptación
├── Por TÉCNICA
│   ├── Caja Blanca (con código) · Caja Negra (sin código)
├── Por NATURALEZA
│   ├── Funcionales · No Funcionales
└── Por PROPÓSITO
    └── Regresión · Componentes · UAT / BAT
```

---

## 📋 SESIÓN 5 — Evaluación Sumativa Unidad 1

- **Modalidad:** EVA · **Ponderación:** 10% · **Instrumento:** Rúbrica
- **Tipo:** Situación problemática — El estudiante analiza un caso de sistema real y debe:
  1. Identificar niveles y tipos de prueba pertinentes.
  2. Justificar la selección.
  3. Describir al menos 3 casos de prueba concretos.
  4. Analizar qué errores detectaría cada prueba.

### Criterios de Evaluación

| Criterio | Logrado (100%) | Medianamente Logrado (60%) | No Logrado (0%) |
|----------|----------------|---------------------------|-----------------|
| Identificación de niveles | Correcto con justificación sólida | La mayoría con justificación parcial | Incorrecto |
| Selección de tipos de prueba | Adecuado al contexto con argumento técnico | Justificación básica | Selección incorrecta |
| Diseño de casos de prueba | Casos claros con entrada/proceso/salida | Casos incompletos | Sin casos válidos |
| Análisis | Propone mejoras con profundidad | Análisis superficial | Sin análisis |
| Presentación y claridad | Redacción clara con terminología técnica | Aceptable con errores | Confusa o graves errores |

---

## 📚 Referencias Bibliográficas

**Obligatorias:**
- Heusser, M. (2023). *Software Testing Strategies*. Packt Publishing. ISBN: 9781837637850.
- IPSS (2024). *Niveles de Prueba. Apunte N°1*. Santiago.
- IPSS (2024). *Tipos de Pruebas. Apunte N°2*. Santiago.

**Complementarias:**
- ISTQB: https://www.istqb.org/certifications/certified-tester-foundation-level
- Myers, E. W. et al. (2012). *The art of software testing: 3rd edition*. Addison-Wesley.
- Sánchez Peño, J. M. (2015). *Pruebas de Software. Fundamentos y Técnicas*. https://oa.upm.es/40012/1/PFC_JOSE_MANUEL_SANCHEZ_PENO_3.pdf

---
*IF203IINF — Testing Aplicado al Desarrollo de Sistemas · IPSS · 2026*
