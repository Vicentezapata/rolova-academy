window.speakerNotes = {
  0: `
<strong>¡Bienvenidos a la Unidad 2!</strong><br><br>
En esta segunda unidad de Testing Aplicado al Desarrollo de Sistemas, daremos un paso más allá de los fundamentos teóricos. Vamos a sumergirnos en cómo se diseñan formalmente las pruebas en un entorno profesional. Hoy dejamos de "adivinar" errores y empezamos a construir una red de seguridad metódica y estructurada para el software.
`,
  1: `
<strong>Ruta de Aprendizaje:</strong><br><br>
Nuestra hoja de ruta para esta unidad se divide en 4 bloques críticos:<br>
1. <strong>Estrategia de Prueba:</strong> Aprenderemos a decidir qué probar basándonos en el riesgo.<br>
2. <strong>Análisis de Requerimientos:</strong> Desde documentos SRS hasta historias de usuario ágiles.<br>
3. <strong>Diseño de Casos:</strong> Cómo estructurar un Test Case profesional y trazarlo con una RTM.<br>
4. <strong>Test Plan:</strong> La coronación del proceso, estructurando el plan maestro según estándares de la industria.
`,
  2: `
<strong>Comenzamos con la Sesión 1: Estrategia de Prueba.</strong><br><br>
Antes de escribir una sola línea de código o de casos de prueba, un equipo de QA debe tener una estrategia clara. No podemos probar el infinito, así que ¿cómo decidimos dónde enfocar nuestros esfuerzos y presupuesto?
`,
  3: `
<strong>El Principio del Contexto.</strong><br><br>
El Testing NO es una talla única. El séptimo principio del testing nos dice que "Las pruebas dependen del contexto".<br>
<em>Ejemplo al curso:</em> "Si ustedes están desarrollando una aplicación para pedir pizza y falla, alguien se queda con hambre. Si están desarrollando el software que controla un marcapasos o los frenos de un auto y falla, alguien muere. Por ende, la rigurosidad, los tipos de prueba y la documentación requerida para ambos proyectos será diametralmente opuesta."
`,
  4: `
<div class="teacher-note">
  <div class="teacher-text">
    <h4>Nota para el Profesor: Dinámica Shark Tank</h4>
    <p>Divide la clase en "Gerentes" (quieren lanzar ya) y "QAs" (quieren probar todo). Dales el caso de la app de Delivery. Tienen 5 minutos para debatir qué módulo se prueba a fondo y cuál se deja fuera. QA debe usar Riesgo/Impacto para convencer al gerente.</p>
  </div>
</div>
<br>
<strong>La Matriz de Riesgos:</strong><br>
La herramienta fundamental del QA Lead. Evaluamos dos variables: <em>Probabilidad de que ocurra un fallo</em> vs <em>Impacto que tendría en el negocio</em>.<br>
Lo que caiga en la zona roja (Alta probabilidad + Alto impacto) se prueba exhaustivamente. Lo que caiga en verde, recibe pruebas mínimas o se asume el riesgo.
`,
  5: `
<strong>Actividad Práctica: El Estratega.</strong><br><br>
Ahora los pondré a prueba. Asuman el rol de Test Managers. Tienen 3 casos ficticios. Discutan en grupos y decidan 3 tipos de prueba exactos para cada caso justificando sus decisiones. Tienen 30 minutos.
`,
  6: `
<strong>Pasamos a la Sesión 2: Análisis de Requerimientos y BDD.</strong><br><br>
Una vez que sabemos nuestra estrategia, necesitamos saber QUÉ vamos a probar exactamente. El software no se prueba contra ideas al aire, se prueba contra requerimientos específicos.
`,
  7: `
<strong>SRS vs Historias de Usuario.</strong><br><br>
Tradicionalmente (Cascada), usábamos Documentos de Requerimientos de Software (SRS), que son tomos enormes y técnicos.<br>
Hoy en día (Agile), usamos Historias de Usuario: "Como [rol], quiero [acción] para [beneficio]". <br>
<em>Punto clave:</em> El QA debe participar activamente en la definición de estas historias para asegurar que sean "testeables" desde el día 1.
`,
  8: `
<strong>INVEST y Gherkin.</strong><br><br>
¿Cómo sabemos si una historia de usuario es buena? Usamos el acrónimo <strong>INVEST</strong> (Independiente, Negociable, Valiosa, Estimable, Pequeña y Testeable).<br>
Para que sea testeable, usamos <strong>BDD</strong> (Desarrollo Guiado por Comportamiento) y la sintaxis <strong>Gherkin</strong>:<br>
<em>Given</em> (Dado un contexto)<br>
<em>When</em> (Cuando ocurre una acción)<br>
<em>Then</em> (Entonces espero este resultado).
`,
  9: `
<strong>Actividad Práctica: El Traductor Ágil.</strong><br><br>
Vamos a ensuciarnos las manos. Tomaremos requerimientos tradicionales ambiguos y, en grupos, deberán reescribirlos usando Historias de Usuario e inventarles 2 Criterios de Aceptación utilizando la sintaxis Gherkin (Dado/Cuando/Entonces). ¡Tienen 30 minutos!
`,
  10: `
<strong>Sesión 3: Casos de Prueba y Trazabilidad.</strong><br><br>
Ya tenemos los requerimientos ágiles y los criterios de aceptación. Ahora, ¿cómo estructuramos las pruebas paso a paso para que cualquier tester del equipo (o un script automatizado) pueda ejecutarlas?
`,
  11: `
<strong>Anatomía del Test Case.</strong><br><br>
Un Test Case profesional no es una simple nota en un cuaderno. Es un artefacto formal.<br>
Debe tener: Un ID único, un Título descriptivo, Precondiciones (qué debe estar listo antes de empezar), Pasos (1, 2, 3... precisos) y el <strong>Resultado Esperado</strong> (la piedra angular del testing).<br>
<em>Recordatorio:</em> Si no defines el resultado esperado antes de probar, podrías engañarte a ti mismo aceptando un comportamiento erróneo como correcto.
`,
  12: `
<strong>Matriz de Trazabilidad (RTM).</strong><br><br>
¿Cómo demostramos que probamos TODO el sistema? Con la RTM.<br>
Es una tabla que cruza los Requerimientos (columnas/filas) con los Casos de Prueba (ID). <br>
<strong>Regla de oro:</strong> Todo Requerimiento debe tener al menos 1 Test Case positivo y 1 negativo. Si un requerimiento no tiene Test Cases, es un "agujero de cobertura". Si un Test Case no apunta a ningún requerimiento, es "esfuerzo desperdiciado".
`,
  13: `
<strong>Actividad Práctica: Anatomía del Caso de Prueba.</strong><br><br>
En esta actividad, usaremos Trello. Cada grupo creará una "tarjeta" que representará un Bug o un Test Case. Aprenderemos a redactarlos de manera profesional utilizando las estructuras que acabamos de ver.
`,
  14: `
<strong>Llegamos a la Sesión 4: El Test Plan.</strong><br><br>
Ya sabemos priorizar riesgos, leer requerimientos, escribir casos y trazar cobertura. Ahora toca unificar todo en el documento maestro que guiará a todo el equipo de QA a lo largo del ciclo de vida del software.
`,
  15: `
<strong>Estándar IEEE 829 (Test Plan).</strong><br><br>
Aunque Agile ha simplificado la documentación, la estructura del IEEE 829 sigue siendo el pilar.<br>
Un buen Plan de Pruebas define: <br>
- <strong>Alcance:</strong> Qué probaremos (In Scope) y qué NO probaremos (Out of Scope).<br>
- <strong>Recursos:</strong> Quiénes probarán y con qué herramientas.<br>
- <strong>Cronograma:</strong> Cuándo iniciaremos y terminaremos.<br>
- <strong>Criterios de Entrada/Salida:</strong> ¿Cuándo estamos listos para empezar a probar? ¿Y cuándo consideramos que terminamos?
`,
  16: `
<div class="teacher-note">
  <div class="teacher-text">
    <h4>Nota para el Profesor: Roleplay de Test Plan</h4>
    <p>Asume el rol de Gerente implacable: "¿Por qué no probaron este módulo? ¡La app sale mañana y puede caerse!". Obliga al grupo a defender que la exclusión del alcance (Out of Scope) fue pactada y documentada en la matriz de riesgos.</p>
  </div>
</div>
<br>
<strong>Gestión de Expectativas:</strong><br>
El Test Plan no es solo técnico, es un documento político y contractual. Si algo falla en producción y estaba "Out of Scope" (Fuera de alcance), el Test Plan es su escudo como equipo de QA.
`,
  17: `
<strong>Cierre de la Unidad 2.</strong><br><br>
Hemos completado el ciclo de diseño. Ya tienen las herramientas de un QA Analyst y un QA Lead. Saben desde cómo levantar requerimientos hasta cómo planificar un ciclo completo de calidad. ¡Felicidades!
`,
  18: `
<div class="teacher-note">
  <div class="teacher-text">
    <h4>Nota para el Profesor: Contexto Evaluativo</h4>
    <p>Aquí se unifica la asignatura. En la U1 conocieron el repositorio CS50 y propusieron 4 casos. Ahora deben <strong>orquestar el plan completo</strong> para ese mismo código. Los "Requerimientos" a trazar son los enunciados formales de los problemas de LeetCode/CS50.</p>
  </div>
</div>
<br>
<strong>Preparación para la Evaluación Sumativa 2.</strong><br>
Vamos a unificar lo aprendido. En la Unidad 1 usaron el repositorio CS50. Para esta evaluación, deberán tomar ese mismo código y crear toda la orquestación formal que acabamos de aprender.
`,
  19: `
<div class="teacher-note">
  <div class="teacher-text">
    <h4>Nota para el Profesor: Pautas Entregables</h4>
    <p>RTM en Excel es obligatoria para demostrar la trazabilidad (1 requerimiento de algoritmo -> múltiples casos de prueba). Gherkin debe usar lenguaje claro de negocio, sin tecnicismos.</p>
  </div>
</div>
<br>
<strong>¿Qué deben entregar?</strong><br>
1. La Matriz de Trazabilidad (RTM) en Excel, mapeando cada requerimiento a sus Casos de Prueba (positivos y negativos).<br>
2. Escenarios en sintaxis Gherkin redactados con lenguaje de negocio (sin tecnicismos de código).<br>
3. El Test Plan estructurado donde definan los riesgos y los criterios de entrada/salida para el repositorio CS50.
`,
  20: `
<strong>Rúbrica de Evaluación.</strong><br><br>
Revisemos juntos los criterios de evaluación. Presten especial atención al rigor en la redacción de sus casos de prueba y en la justificación de sus decisiones de alcance en el Test Plan. ¡Tienen el control total de la calidad de su proyecto!
teeeeeees
`,
};
