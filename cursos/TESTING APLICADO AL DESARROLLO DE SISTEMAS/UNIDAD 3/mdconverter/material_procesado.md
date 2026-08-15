# **Testing Aplicado al Desarrollo de Sistemas** 

 

 

 

 

 

# Código:IF203 

## **Apunte N° 3** **Automatización** 

**Apunte 3 – Automatización** **Testing aplicado al desarrollo de sistemas \_ IF203** 

 

Introducción

 

El presente documento tiene como finalidad presentar En el dinámico panorama actual del desarrollo de 

software, la calidad y la confiabilidad se erigen como piedras angulares para el éxito de cualquier 

proyecto. Si bien las pruebas manuales han sido, y siguen siendo, un componente esencial en el proceso 

de aseguramiento de la calidad, no están exentas de limitaciones. Su carácter tedioso, repetitivo y 

susceptible al error humano, las convierte en un cuello de botella que obstaculiza la eficiencia y la 

precisión. 

Es en este contexto que la automatización de pruebas emerge como una herramienta 

revolucionaria, transformando el panorama de la evaluación de software. Al delegar tareas repetitivas a 

scripts y herramientas automatizadas, los desarrolladores y testers pueden enfocarse en aspectos más 

estratégicos y creativos, optimizando así el tiempo y los recursos disponibles. 

Este documento tiene como objetivo ofrecer una guía sobre la automatización de pruebas, abarcando 

desde su definición y relevancia hasta sus beneficios, herramientas disponibles, proceso de 

funcionamiento y consideraciones prácticas. A través de una descripción detallada y ejemplos 

específicos, 

Junto a lo anterior, verán, a lo largo del documento, algunas preguntas de análisis para corroborar la 

comprensión de los contenidos presentados, las cuales son útiles para el desarrollo de esos 

conocimientos en el ambiente laboral. 

Éxito en el estudio de este apunte, el cual es clave para profundizar aún más en el uso de las tecnologías. 

 

**Apunte 3 – Automatización** **Testing aplicado al desarrollo de sistemas \_ IF203** 

 

Automatización

 

En el dinámico mundo del desarrollo de software, la automatización de pruebas ha surgido como un faro 

de eficiencia y confiabilidad, transformando radicalmente la forma en que se evalúa la calidad del 

software. Esta innovadora metodología introduce un enfoque sistematizado para automatizar tareas 

repetitivas de pruebas, liberando a los equipos de tediosas labores manuales y permitiéndoles enfocarse 

en aspectos más estratégicos del desarrollo. 

A continuación, nos embarcaremos en un viaje profundo para explorar el universo de la automatización 

de pruebas, desentrañando sus conceptos fundamentales, beneficios tangibles, herramientas 

disponibles, su funcionamiento interno, consideraciones prácticas y mucho más. 

La automatización de pruebas, en su esencia, consiste en la aplicación de herramientas y técnicas de 

software para automatizar la ejecución de casos de prueba predefinidos. Estos casos de 

prueba, cuidadosamente diseñados para simular el uso real del software, permiten evaluar la 

funcionalidad, el rendimiento y la seguridad del producto en desarrollo. 

A diferencia de las pruebas manuales, donde un tester ejecuta los casos de prueba de forma individual, la 

automatización de pruebas delega esta tarea a un software especializado. Este software, cual hábil 

marioneta, controla la interfaz del software bajo prueba, ingresa datos, navega por menús y verifica los 

resultados esperados, 

**Definición y Beneficios:** 

La automatización de pruebas se define como el proceso de ejecutar pruebas de software de forma 

automática, utilizando herramientas y scripts predefinidos. Estas herramientas simulan la interacción 

humana con el software, ejecutando casos de prueba, registrando resultados y comparándolos con los 

resultados esperados. 

Los principales beneficios de la automatización de pruebas incluyen: 

* **Eficiencia:** Permite ejecutar pruebas de forma más rápida y repetitiva, liberando tiempo para 

que los testers se enfoquen en pruebas más complejas y exploratorias. 

* **Reducción de costos:** Disminuye los costos asociados a la ejecución manual de pruebas, 

liberando recursos humanos para otras tareas de mayor valor. 

* **Mejora en la cobertura de pruebas:** Permite realizar pruebas más exhaustivas y frecuentes, 

aumentando la probabilidad de detectar errores tempranamente. 

**Apunte 3 – Automatización** **Testing aplicado al desarrollo de sistemas \_ IF203** 

 

* **Mejora en la calidad del software:** Contribuye a la entrega de un software de mayor calidad, 

con menos errores y una mayor confiabilidad. 

* **Integración continua:** Facilita la integración de las pruebas en el proceso de desarrollo, 

permitiendo la detección temprana de errores y una entrega más rápida de software. 

**Herramientas Disponibles y Funciones Principales:** 

Existe una amplia variedad de herramientas de automatización de pruebas disponibles en el mercado, 

cada una con sus propias características y funcionalidades. Algunas de las herramientas más populares 

incluyen: 

* **Selenium:** Un framework de código abierto y multiplataforma para pruebas web, compatible con 

diversos lenguajes de programación como Python, Java y C#. 

* **Appium:** Una herramienta para pruebas móviles multiplataforma, basada en el framework 

Selenium, que permite automatizar pruebas en dispositivos iOS y Android. 

* **Cucumber:** Un framework de pruebas de aceptación basado en el lenguaje Gherkin, que facilita 

la creación de escenarios de prueba fáciles de entender para personas no técnicas. 

* **Robot Framework:** Un framework de pruebas genérico basado en Python, que permite 

automatizar pruebas en una amplia variedad de aplicaciones, incluyendo aplicaciones web, 

móviles, de escritorio y API. 

Las funciones principales de las herramientas de automatización de pruebas incluyen: 

* **Creación y gestión de casos de prueba:** Permiten crear, editar y organizar casos de prueba 

de manera eficiente. 

* **Ejecución de casos de prueba:** Automatizan la ejecución de casos de prueba en diferentes 

entornos y navegadores. 

* **Registro y análisis de resultados:** Registran los resultados de las pruebas y proporcionan 

herramientas para su análisis e interpretación. 

* **Generación de informes:** Generan informes detallados sobre los resultados de las pruebas, 

incluyendo métricas de cobertura, errores encontrados y tendencias a lo largo del tiempo. 

* **Integración con herramientas de desarrollo continuo:** Se integran con herramientas de 

desarrollo continuo (CI/CD) para permitir la ejecución automatizada de pruebas durante el 

proceso de desarrollo. 

**Proceso y Funcionamiento:** 

**a) Lenguajes y Entornos de Desarrollo:** 

**Apunte 3 – Automatización** **Testing aplicado al desarrollo de sistemas \_ IF203** 

 

Las herramientas de automatización de pruebas suelen estar basadas en lenguajes de programación 

populares como Python, Java, C# y JavaScript. Además, muchas herramientas ofrecen soporte para 

múltiples entornos de desarrollo, incluyendo Windows, macOS y Linux. 

**b) Implementación y Gestión:** 

El proceso de implementación y gestión de la automatización de pruebas implica: 

* **Selección de la herramienta adecuada:** Elegir la herramienta adecuada en función de las 

necesidades específicas del proyecto, el lenguaje de programación preferido y el presupuesto 

disponible. 

* **Definición del alcance de las pruebas:** Determinar qué pruebas se automatizarán y qué se 

seguirán ejecutando manualmente. 

* **Desarrollo de scripts de prueba:** Crear scripts de prueba utilizando la herramienta elegida, 

siguiendo las mejores prácticas y metodologías de desarrollo de software. 

* **Integración con el entorno de desarrollo:** Integrar las pruebas automatizadas con el entorno 

de desarrollo para permitir su ejecución automatizada durante el proceso de desarrollo. 

* **Mantenimiento de scripts de prueba:** Mantener los scripts de prueba actualizados a medida 

que el software evoluciona. 

**c) Planificación y Mantenimiento de Pruebas:** 

* **Creación de un plan de pruebas:** Definir un plan de pruebas que detalle la frecuencia de 

ejecución de las pruebas, los criterios de aceptación y los responsables de la ejecución de las 

pruebas. 

* **Monitoreo de resultados:** Monitorear los resultados de las pruebas de forma regular para 

identificar patrones, tendencias y posibles problemas. 

* **Mantenimiento de scripts de prueba:** Mantener los scripts de prueba actualizados a medida 

que el software evoluciona, para asegurar su precisión y efectividad. 

**d) Monitoreo y Análisis de Resultados:** 

El monitoreo y análisis de los resultados de las pruebas automatizadas son esenciales para evaluar su 

eficacia y tomar decisiones informadas: 

* **Recopilación de métricas:** Recopilar métricas clave como la tasa de cobertura de pruebas, la 

cantidad de errores encontrados y el tiempo de ejecución de las pruebas. 

**Apunte 3 – Automatización** **Testing aplicado al desarrollo de sistemas \_ IF203** 

 

* **Análisis de tendencias:** Analizar las tendencias de las métricas recopiladas para identificar 

áreas de mejora y posibles riesgos. 

* **Generación de informes:** Generar informes detallados que resuman los resultados de las 

pruebas, las métricas clave y las tendencias identificadas. 

* **Comunicación de resultados:** Comunicar los resultados de las pruebas a las partes 

interesadas relevantes, incluyendo al equipo de desarrollo, los gerentes de proyecto y los 

clientes. 

1. **Consideraciones Prácticas:** 

**a) Selección Adecuada de Herramientas:** 

La selección de la herramienta de automatización de pruebas adecuada es crucial para el éxito del 

proyecto: 

* **Evaluar las necesidades del proyecto:** Considerar las características y funcionalidades 

requeridas, el presupuesto disponible, la experiencia del equipo y la compatibilidad con el entorno 

de desarrollo. 

* **Probar diferentes herramientas:** Evaluar diferentes herramientas mediante pruebas piloto para 

determinar cuál se adapta mejor a las necesidades del proyecto. 

* **Considerar la escalabilidad:** Elegir una herramienta que pueda escalar para satisfacer las 

necesidades futuras del proyecto. 

**b) Estrategias de Automatización y Evaluación de Eficacia:** 

Implementar una estrategia de automatización efectiva es esencial para aprovechar al máximo las 

pruebas automatizadas: 

* **Definir objetivos claros:** Establecer objetivos claros para la automatización, como la reducción 

del tiempo de ejecución de las pruebas o la mejora de la cobertura de pruebas. 

* **Priorizar casos de prueba:** Priorizar los casos de prueba que se automatizarán en función de 

su importancia, riesgo y valor comercial. 

* **Monitorear y evaluar el progreso:** Monitorear el progreso de la automatización y evaluar su 

eficacia en función de los objetivos establecidos. 

 

 

**Apunte 3 – Automatización** **Testing aplicado al desarrollo de sistemas \_ IF203** 

 

**c) Identificación y Documentación de Defectos:** 

La identificación y documentación de defectos encontrados durante las pruebas automatizadas son 

cruciales para su resolución efectiva: 

* **Registrar defectos de manera detallada:** Incluir una descripción clara del defecto, los pasos 

para reproducirlo, el impacto en el software y la gravedad del error. 

* **Clasificar y priorizar defectos:** Clasificar los defectos según su gravedad, prioridad y tipo. 
* **Asignar defectos al equipo de desarrollo:** Asignar los defectos a los miembros del equipo de 

desarrollo responsables de su resolución. 

**d) Seguimiento y Resolución de Defectos:** 

El seguimiento y la resolución de defectos identificados durante las pruebas automatizadas son 

esenciales para garantizar la calidad del software: 

* **Monitorear el progreso de la resolución:** Monitorear el progreso de la resolución de defectos, 

asegurando que se cumplan los plazos establecidos. 

* **Verificar correcciones:** Verificar que las correcciones realizadas resuelvan efectivamente los 

defectos reportados. 

* **Retesting:** Realizar pruebas de regresión para asegurar que la resolución de un defecto no haya 

introducido nuevos errores. 

La automatización de pruebas se ha convertido en una herramienta indispensable en el desarrollo de 

software moderno, proporcionando eficiencia, confiabilidad y una mejor calidad del software. Al 

seleccionar las herramientas adecuadas, implementar estrategias efectivas y seguir las mejores 

prácticas, las organizaciones pueden aprovechar al máximo las pruebas automatizadas para entregar 

software de alta calidad a sus clientes. 

**COMPRUEBO MI APRENDIZAJE** 

1. Mencione un ejemplo de un error que se puede detectar con 

mayor facilidad mediante pruebas manuales que con pruebas automatizadas. 

2. "La primera etapa del proceso de aplicación de las pruebas 

manuales es la **ejecución** de los casos de prueba." Señale si esta afirmación es verdadera o falsa. Argumente su respuesta. 

 

 

Conclusión

 

 La automatización de pruebas ha transformado el panorama del desarrollo de software, introduciendo un enfoque eficiente, confiable y escalable para evaluar la calidad del software. Al implementar estrategias efectivas de automatización, las organizaciones pueden optimizar sus procesos de pruebas, reducir costos, mejorar la cobertura de pruebas y entregar software de mayor calidad a sus clientes. 

La selección adecuada de herramientas, la definición de objetivos claros, la implementación de metodologías sólidas y el seguimiento continuo del progreso son elementos clave para el éxito de la automatización de pruebas. Al adoptar esta práctica, las empresas pueden garantizar la confiabilidad y el rendimiento de sus productos de software, satisfaciendo las expectativas de sus usuarios y posicionándose en un mercado cada vez más competitivo. 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

**Apunte 3 – Automatización** **Testing aplicado al desarrollo de sistemas \_ IF203** 

 

#### **Información complementaria** 

Link 1: Gherkin Syntax [https://cucumber.io/docs/gherkin/](https://cucumber.io/docs/gherkin/)[ ](https://cucumber.io/docs/gherkin/) 

**Apunte 3 – Automatización** **Testing aplicado al desarrollo de sistemas \_ IF203** 

 

Referencia Bibliografía

 Begado, J. D., & Burlington, C. (2001). **Automatización de pruebas de software: Un enfoque** **práctico**. Madrid: McGraw-Hill Interamericana. Ghermezian, A., & Irani, K. (2017). **Automatización de pruebas de software: Un enfoque** **práctico con Selenium, Java y Cucumber**. Apress. 

**Referencia del presente documento:** Instituto San Sebastián, Innovación académica (2024). *Apunte 3: Automatización*. Testing aplicado al desarrollo de sistemas. Santiago. 

 

---

 

 

 

 

 

# **Testing Aplicado al Desarrollo de Sistemas** 

 

 

 

 

 

# Código: IF203 

## **Apunte N° 3** **Ciclo de vida del defecto** 

**Apunte 3 – Ciclo de vida del defecto** **Testing Aplicado al Desarrollo de Sistemas – IF203** 

Introducción

 

El presente documento tiene como finalidad presentar el ciclo de vida de un defecto en el desarrollo de 

software es un proceso fundamental que define la gestión y resolución de problemas encontrados en el 

sistema. Comienza con la detección inicial del defecto, ya sea por parte de los equipos de pruebas o 

usuarios finales, marcando el inicio de un flujo estructurado que abarca varias etapas clave. Cada fase, 

desde la identificación hasta la corrección y la verificación final, desempeña un papel crucial en garantizar 

la calidad y la fiabilidad del software desarrollado. 

Este proceso no se limita únicamente a los equipos de desarrollo y prueba; implica también una 

meticulosa documentación, seguimiento y comunicación efectiva entre todos los actores involucrados. 

La documentación detallada del defecto permite una comprensión clara de su naturaleza y gravedad, 

facilitando así su gestión adecuada. El seguimiento meticuloso del estado del defecto a lo largo del ciclo 

de vida asegura que se tomen las acciones necesarias en cada fase, desde su reporte inicial hasta su 

resolución final. 

Además, la comunicación efectiva juega un papel crucial en el ciclo de vida del defecto. Es fundamental 

mantener a todas las partes interesadas informadas sobre el estado y el progreso en la resolución del 

defecto, asegurando una colaboración fluida entre desarrolladores, probadores y otros equipos 

involucrados. Esta transparencia ayuda a mitigar riesgos y a garantizar que los defectos sean abordados 

de manera oportuna y eficaz. 

En este documento, exploraremos con detalle los diferentes estados típicos que conforman el ciclo de 

vida de un defecto. A través de este análisis, se proporcionará una comprensión exhaustiva de cómo se 

manejan estos desafíos en el dinámico entorno del desarrollo de software contemporáneo. 

Junto a lo anterior, verán, a lo largo del documento, algunas preguntas de análisis para corroborar la 

comprensión de los contenidos presentados, las cuales son útiles para el desarrollo de esos 

conocimientos en el ambiente laboral. 

Éxito en el estudio de este apunte, el cual es clave para profundizar aún más en el uso de las tecnologías. 

 

**Apunte 3 – Ciclo de vida del defecto** **Testing Aplicado al Desarrollo de Sistemas – IF203** 

Ciclo de vida del defecto

 

El ciclo de vida de un defecto en el desarrollo de software describe las etapas por las que pasa un 

problema identificado en el software, desde su descubrimiento hasta su resolución completa. A 

continuación, te detallo las etapas típicas del ciclo de vida de un defecto: 

1. **Reporte y Registro de Defectos en el Software** 

Reporte: Durante las pruebas del software, un tester identifica un defecto, también conocido como bug o 

error. Este hallazgo es crucial, ya que impacta directamente en la calidad del producto final. 

Registro: Para gestionar eficazmente este defecto, se procede a crear un registro detallado en un sistema 

especializado de seguimiento de errores, comúnmente conocido como bug tracker o sistema de gestión 

de incidencias. Este registro incluye una descripción exhaustiva del comportamiento incorrecto 

observado, los pasos específicos para reproducir el problema, el entorno donde ocurrió el error (como el 

sistema operativo, la configuración de red, etc.), así como cualquier otro detalle relevante que pueda 

ayudar al equipo de desarrollo a entender y corregir el defecto de manera efectiva. 

Este proceso de reporte y registro no solo facilita la comunicación clara y estructurada entre los testers 

y los desarrolladores, sino que también garantiza que todos los problemas identificados sean 

documentados de manera completa y precisa, asegurando así una respuesta y resolución oportuna de 

cada incidencia reportada. 

1. **Análisis y Priorización de Defectos en el Proceso de Desarrollo de Software** 

Análisis: Tras la identificación inicial de un defecto durante las pruebas del software, un responsable 

técnico con experiencia, como un desarrollador senior o un líder de equipo, asume la tarea de realizar 

un análisis detallado. Este análisis tiene como objetivo principal comprender la causa raíz del defecto. El 

responsable técnico investiga minuciosamente las circunstancias que rodean el error para determinar 

exactamente qué aspecto del código o del diseño del software está contribuyendo al comportamiento 

incorrecto observado. 

Durante este proceso, se pueden utilizar herramientas de depuración y técnicas de análisis de código 

para profundizar en los detalles técnicos del problema. El objetivo es identificar no solo el síntoma visible 

del defecto, sino también las condiciones subyacentes que lo están causando, con el fin de proporcionar 

una solución efectiva y duradera. 

**Apunte 3 – Ciclo de vida del defecto** **Testing Aplicado al Desarrollo de Sistemas – IF203** 

* Priorización: Una vez que se ha completado el análisis técnico, el siguiente paso crucial es la 

priorización del defecto. Este paso implica evaluar la gravedad del problema identificado y 

determinar su impacto potencial en el producto final y en los usuarios finales. Para lograr esto de 

manera efectiva, se utilizan categorías de priorización predefinidas, como crítico, alto, medio y 

bajo, que ayudan a clasificar la severidad del defecto. 

Además de la gravedad, otros factores clave se tienen en cuenta para establecer la prioridad del defecto. 

Estos pueden incluir la frecuencia con la que ocurre el error, el número de usuarios afectados, la criticidad 

de las funciones afectadas y cualquier requisito contractual o regulatorio relacionado. El equipo de 

desarrollo también puede considerar el impacto en la experiencia del usuario, la reputación de la empresa 

y los objetivos estratégicos del proyecto al determinar la prioridad. 

Es fundamental que la priorización se realice de manera colaborativa y bien informada, involucrando a 

diversas partes interesadas, como el equipo de desarrollo, el equipo de control de calidad (QA), los 

gestores de producto y, en algunos casos, los clientes o usuarios representativos. Esta estrategia 

garantiza que los recursos se asignen de manera óptima para abordar primero los defectos que tienen 

el mayor impacto en la calidad y la funcionalidad del software, promoviendo así un proceso de desarrollo 

eficiente y centrado en la mejora continua. 

1. **Asignación y Trabajo** 

Asignación: Una vez que un defecto ha sido analizado y priorizado dentro del sistema de gestión de 

incidencias o bug tracker, se procede a asignarlo a un desarrollador específico. Esta asignación no solo 

establece la responsabilidad directa sobre la resolución del problema, sino que también asegura que el 

desarrollador tenga la capacidad técnica y el contexto necesarios para abordar eficazmente el defecto 

identificado. 

La asignación del defecto puede basarse en varios criterios, como la experiencia del desarrollador con 

el área del código afectado, su carga de trabajo actual, la urgencia del problema y la disponibilidad de 

recursos. Es importante que la asignación se realice de manera clara y transparente, comunicando 

adecuadamente al desarrollador todos los detalles relevantes del defecto, incluyendo el análisis previo 

realizado, la prioridad asignada y cualquier otra información crucial para su corrección. 

Trabajo: Una vez asignado, el desarrollador se embarca en el proceso de trabajo para corregir el código 

afectado por el defecto identificado. Este proceso implica una serie de pasos meticulosos que van desde 

la comprensión completa del problema hasta la implementación y prueba de la solución propuesta. 

 

**Apunte 3 – Ciclo de vida del defecto** **Testing Aplicado al Desarrollo de Sistemas – IF203** 

El desarrollador comienza por revisar el código relevante, utilizando la información recopilada durante el 

análisis del defecto para identificar y modificar las secciones específicas que están contribuyendo al 

comportamiento incorrecto del software. Dependiendo de la complejidad del problema, puede ser 

necesario realizar cambios adicionales en otras partes del código para garantizar una solución integral y 

robusta. 

Durante el trabajo de corrección, el desarrollador también debe asegurarse de seguir las prácticas 

recomendadas de desarrollo de software, como la modularidad, la legibilidad del código y la adhesión a 

los estándares de codificación establecidos por el equipo. Esto no solo facilita la comprensión y 

mantenimiento del código en el futuro, sino que también promueve la consistencia y la calidad en todo el 

proceso de desarrollo. 

Una vez completada la corrección, el desarrollador realiza pruebas exhaustivas para verificar que el 

defecto haya sido completamente eliminado y que la funcionalidad afectada funcione correctamente 

según lo esperado. Estas pruebas pueden incluir casos de prueba específicos diseñados para validar la 

solución implementada, así como pruebas de regresión para asegurar que otras partes del sistema no 

se vean afectadas por los cambios realizados. 

En resumen, el proceso de asignación y trabajo en la corrección de defectos no solo es crucial para 

mantener la integridad y calidad del software, sino que también refleja la colaboración efectiva entre los 

equipos de desarrollo y calidad, asegurando así que cada problema identificado sea abordado de manera 

eficiente y profesional. 

1. **Corrección y Pruebas en el Proceso de Desarrollo de Software** 

Corrección: Después de que un desarrollador ha sido asignado para abordar un defecto específico, 

comienza el proceso de corrección. Este paso es crucial para asegurar que el software funcione 

correctamente y cumpla con las expectativas de los usuarios finales. La corrección implica la 

implementación de una solución efectiva al problema identificado dentro del código afectado. 

El desarrollador utiliza la información recopilada durante el análisis del defecto para guiar la modificación 

* reparación del código relevante. Esto puede implicar ajustes directos en el código fuente, 

refactorización de secciones específicas o la introducción de nuevas funciones para corregir el 

comportamiento incorrecto observado. 

Durante este proceso, es fundamental que el desarrollador siga prácticas de desarrollo de software 

robustas y buenas prácticas de codificación. Esto incluye asegurarse de que los cambios sean 

**Apunte 3 – Ciclo de vida del defecto** **Testing Aplicado al Desarrollo de Sistemas – IF203** 

coherentes con la arquitectura existente del software, mantener la legibilidad y modularidad del código, 

y adherirse a los estándares de codificación establecidos por el equipo de desarrollo. 

Pruebas Unitarias: Una vez que la corrección ha sido implementada, es crucial verificar que la solución 

propuesta resuelve efectivamente el defecto sin introducir nuevos problemas en el sistema. Las pruebas 

unitarias desempeñan un papel fundamental en este proceso. 

Las pruebas unitarias son pruebas automatizadas que se centran en verificar el comportamiento 

individual de componentes o módulos específicos del software. Estas pruebas son diseñadas y 

desarrolladas por el mismo desarrollador o por el equipo de desarrollo para evaluar la funcionalidad de 

forma aislada y detallada. 

Durante las pruebas unitarias, se ejecutan casos de prueba específicos que se centran en los cambios 

realizados para corregir el defecto. Esto permite validar que la funcionalidad afectada por la corrección 

se comporta como se espera y que no se han introducido nuevos errores o regresiones en el sistema. 

Además de confirmar la efectividad de la corrección, las pruebas unitarias también contribuyen a mejorar 

la calidad del código y facilitan el mantenimiento futuro del software. Al automatizar estas pruebas, el 

equipo de desarrollo puede identificar y resolver problemas de manera proactiva antes de que afecten al 

usuario final, garantizando así una experiencia de usuario más fluida y confiable. 

En resumen, el proceso de corrección y pruebas unitarias no solo asegura la resolución efectiva de los 

defectos identificados, sino que también fortalece la calidad y la estabilidad del software, promoviendo 

un ciclo de desarrollo más eficiente y centrado en la entrega de productos de alta calidad y confiabilidad. 

1. **Pruebas de Regresión en el Proceso de Desarrollo de Software** 

Las pruebas de regresión desempeñan un papel fundamental en el aseguramiento de la calidad del 

software después de que se ha realizado una corrección o modificación. Estas pruebas están diseñadas 

específicamente para verificar que los cambios introducidos para corregir un defecto no han afectado 

negativamente otras partes del sistema que funcionaban correctamente previamente. 

Importancia de las Pruebas de Regresión: Cuando se implementa una corrección de un defecto, existe 

el riesgo potencial de que los cambios realizados puedan tener impactos no deseados en otras 

funcionalidades del software. Esto se conoce como regresión, donde una modificación destinada a 

resolver un problema específico causa nuevos errores en áreas no relacionadas del sistema. Las pruebas 

de regresión son esenciales para mitigar este riesgo al detectar cualquier regresión o deterioro de la 

calidad del software como resultado de la corrección. 

**Apunte 3 – Ciclo de vida del defecto** **Testing Aplicado al Desarrollo de Sistemas – IF203** 

Estrategia de Pruebas de Regresión: Las pruebas de regresión se planifican y ejecutan meticulosamente 

después de cada ciclo de corrección de defectos o desarrollo de nuevas funcionalidades. Esta estrategia 

asegura que todas las partes del software que podrían verse afectadas por los cambios recientes sean 

evaluadas exhaustivamente para verificar su integridad y funcionalidad. 

Enfoque Automatizado y Manual: Para optimizar el proceso, las pruebas de regresión suelen ser 

automatizadas siempre que sea posible. Las herramientas de automatización permiten ejecutar un 

conjunto predefinido de casos de prueba de manera rápida y repetible, identificando cualquier desviación 

* fallo que pueda haber sido introducido involuntariamente. Esto no solo mejora la eficiencia del equipo 

de desarrollo, sino que también garantiza una cobertura exhaustiva de pruebas en diversas 

configuraciones y escenarios de uso del software. 

Sin embargo, el componente humano sigue siendo crucial en las pruebas de regresión, especialmente 

para casos de prueba complejos o situaciones no estándar que requieren un análisis más profundo y una 

validación manual. Los testers y el equipo de control de calidad desempeñan un papel clave en la 

detección temprana de problemas potenciales, proporcionando feedback y asegurando que el software 

mantenga su calidad y fiabilidad. 

1. **Resultados y Gestión de Defectos** 

Durante las pruebas de regresión, cualquier defecto o anomalía detectada se documenta de manera 

detallada en el sistema de gestión de incidencias o bug tracker. Estos registros incluyen información 

completa sobre la naturaleza del problema, pasos para reproducirlo, su impacto potencial en el usuario 

final y cualquier otra información relevante. Esta gestión eficaz de defectos facilita su priorización y 

resolución oportuna por parte del equipo de desarrollo, garantizando así que el software entregado 

cumpla con los estándares de calidad establecidos. 

En resumen, las pruebas de regresión son esenciales para mantener la estabilidad y la fiabilidad del 

software después de cada cambio. Al adoptar una estrategia integral que combine pruebas 

automatizadas y manuales, las organizaciones pueden mitigar eficazmente los riesgos de regresión y 

asegurar que cada versión del software mantenga su integridad y funcionalidad sin compromisos. Esto 

promueve una experiencia de usuario consistente y satisfactoria, respaldada por un desarrollo de 

software disciplinado y centrado en la calidad. 

Validación y Verificación en el Proceso de Desarrollo de Software: Validación: Una vez que un 

desarrollador ha implementado una corrección para un defecto identificado, el proceso de validación 

juega un papel crucial en asegurar que la solución propuesta efectivamente resuelve el problema 

**Apunte 3 – Ciclo de vida del defecto** **Testing Aplicado al Desarrollo de Sistemas – IF203** 

reportado. Esta fase implica que el tester, utilizando el entorno de prueba adecuado, valide la corrección 

siguiendo los pasos inicialmente reportados para reproducir el defecto. 

El tester se basa en la información detallada proporcionada durante el reporte inicial del defecto, 

incluyendo el comportamiento incorrecto observado y los pasos específicos necesarios para replicar el 

problema. Al reproducir cuidadosamente el escenario original, el objetivo es confirmar que la corrección 

implementada aborda completamente el defecto y restaura la funcionalidad esperada del software. 

Durante la validación, el tester puede también verificar otros aspectos asociados con el defecto, como la 

integridad de los datos afectados o la interacción correcta con otros módulos del sistema. Esta etapa 

garantiza que la solución implementada no solo resuelve el problema superficialmente, sino que también 

considera cualquier impacto más amplio que el defecto pueda haber tenido en el software. 

Verificación: Una vez validada la corrección, se procede con la verificación para asegurar que el defecto 

esté completamente resuelto y que no existan problemas adicionales relacionados con la corrección 

realizada. Esta fase de verificación se centra en revisar exhaustivamente el código modificado y realizar 

pruebas adicionales para confirmar la estabilidad y la integridad del software después de la corrección. 

Durante la verificación, se ejecutan pruebas específicas diseñadas para validar que todas las 

funcionalidades afectadas por el defecto ahora operan correctamente y en consonancia con las 

expectativas del usuario final. Esto incluye la ejecución de pruebas funcionales y de integración, así como 

pruebas de rendimiento si es necesario, para asegurar que la corrección no ha introducido nuevos 

problemas o regresiones en otras áreas del sistema. 

Además, la verificación puede incluir la revisión del código por parte de otros desarrolladores del equipo 

para obtener una perspectiva adicional y asegurar que se han seguido las mejores prácticas de 

desarrollo. Esta revisión colaborativa no solo mejora la calidad del código, sino que también fortalece la 

confianza en la solución implementada antes de su liberación a los usuarios finales. 

Gestión de Resultados y Cierre: Una vez completadas la validación y verificación con éxito, cualquier 

resultado relevante, como la confirmación de la corrección efectiva del defecto o la identificación de 

problemas adicionales, se documenta de manera detallada en el sistema de gestión de incidencias o bug 

tracker. Esto asegura que todos los hallazgos sean registrados adecuadamente para facilitar su 

seguimiento y resolución. Finalmente, el equipo de desarrollo realiza una evaluación final para determinar 

si el defecto está completamente resuelto y si la corrección ha sido validada y verificada de manera 

satisfactoria. Esta evaluación marca el cierre del ciclo de corrección de defectos y prepara el terreno para 

la liberación de nuevas versiones de software que mantengan la calidad y la funcionalidad esperada por 

los usuarios finales. 

**Apunte 3 – Ciclo de vida del defecto** **Testing Aplicado al Desarrollo de Sistemas – IF203** 

En conclusión, el proceso de validación y verificación no solo asegura la efectividad de las correcciones 

de defectos, sino que también promueve la estabilidad y confiabilidad del software a lo largo de su ciclo 

de vida, respaldando así una experiencia de usuario óptima y una gestión eficiente de la calidad del 

producto. 

1. **Cierre y Revisión Post-Implementación en el Proceso de Desarrollo de Software** 

Cierre del Defecto: 

Después de completar exitosamente la validación y verificación de la corrección de un defecto, el 

siguiente paso es marcar el defecto como cerrado en el sistema de seguimiento de errores. Este marcado 

representa un hito significativo en el ciclo de vida del desarrollo de software, indicando que el problema 

identificado ha sido completamente resuelto y que la funcionalidad afectada ahora opera correctamente 

según lo esperado.El proceso de cierre no solo implica la actualización del estado del defecto en el 

sistema de gestión de incidencias o bug tracker, sino también la documentación detallada de los 

resultados de las pruebas de validación y verificación. Esta documentación incluye información sobre las 

acciones tomadas para corregir el defecto, los resultados de las pruebas realizadas y cualquier 

observación relevante que pueda ser útil para futuras referencias o auditorías. 

Revisión Post-Implementación: 

Tras el cierre de un defecto, es altamente recomendable realizar una revisión post-implementación o 

retrospectiva para analizar las lecciones aprendidas del incidente y explorar cómo mejorar los procesos 

para prevenir problemas similares en el futuro. Esta revisión no solo se enfoca en el defecto específico y 

su corrección, sino también en el contexto más amplio del proceso de desarrollo y las prácticas del 

equipo. 

Durante la revisión post-implementación, se pueden abordar varios aspectos clave: 

* Análisis de Causa Raíz: Identificar las causas subyacentes que contribuyeron al surgimiento del 

defecto. Esto puede involucrar factores como errores en el diseño, falta de pruebas adecuadas, 

comunicación insuficiente, entre otros. 

* Efectividad de la Solución: Evaluar la efectividad de la solución implementada y si se abordaron 

completamente todos los aspectos del defecto. También se puede considerar si hubo 

oportunidades para una solución más eficiente o robusta. 

* Proceso de Corrección: Revisar el proceso utilizado para corregir el defecto, incluyendo la 

asignación, trabajo de desarrollo, pruebas y validación. Identificar áreas donde se podría mejorar 

la eficiencia o la calidad del trabajo realizado. 

**Apunte 3 – Ciclo de vida del defecto** **Testing Aplicado al Desarrollo de Sistemas – IF203** 

* Lecciones Aprendidas: Extraer lecciones útiles del incidente, como áreas de mejora en la 

comunicación dentro del equipo, la implementación de mejores prácticas de desarrollo de 

software, la actualización de la documentación de procedimientos, entre otros. 

* Acciones Correctivas y Preventivas: Definir acciones concretas para corregir las deficiencias 

identificadas y prevenir la recurrencia de problemas similares en el futuro. Estas acciones pueden 

incluir la implementación de nuevos controles de calidad, la capacitación adicional del equipo, la 

mejora de herramientas de prueba, entre otras iniciativas. 

La revisión post-implementación no solo tiene como objetivo mejorar la calidad del software, sino también 

fortalecer la capacidad del equipo para aprender y crecer a partir de experiencias pasadas. Fomenta una 

cultura de mejora continua y responsabilidad compartida dentro del equipo de desarrollo, promoviendo 

así un ciclo de desarrollo más eficiente y orientado hacia la excelencia. 

En conclusión, el cierre de un defecto y la revisión post-implementación son componentes críticos en la 

gestión de la calidad del software, proporcionando una oportunidad invaluable para reflexionar, aprender 

y evolucionar hacia prácticas de desarrollo más efectivas y resilientes. 

***Ilustración 1 - Ciclo de Vida** *

 

##### **COMPRUEBO MI APRENDIZAJE** 

* **Compara el ciclo de vida de un defecto en metodologías Agile versus Waterfall. ¿En qué aspectos difieren y cómo influye esto en la gestión de defectos?**  
* **¿Cómo definirías la fase de "Análisis" dentro del ciclo de vida de un defecto? ¿Cuál es su propósito principal en el proceso de desarrollo de software?** 

**Apunte 3 – Ciclo de vida del defecto** **Testing Aplicado al Desarrollo de Sistemas – IF203** 

 

#### **Información complementaria** 

Link 1: **¿Cuál es el ciclo de vida de los defectos?** https://elminimoviable.es/cual-es-el-ciclo-de-vida-de-los-defectos/ 

Conclusión

El ciclo de vida de un defecto en el desarrollo de software representa un proceso meticuloso y 

estructurado destinado a garantizar la identificación, corrección y verificación efectiva de problemas que 

podrían afectar la calidad del producto final. Comienza con la detección inicial del defecto, que puede 

surgir durante las fases de pruebas o incluso ser reportado por usuarios finales, marcando así el inicio 

de un flujo de trabajo organizado y sistemático. 

Una vez detectado, el defecto se registra detalladamente, documentando su naturaleza, contexto y 

cualquier información relevante que facilite su comprensión y gestión. Esta documentación no solo sirve 

para trazar el historial del defecto, sino que también proporciona una base sólida para las acciones 

correctivas que se llevarán a cabo. 

La siguiente fase crucial es la corrección del defecto, donde los desarrolladores trabajan para resolver el 

problema de acuerdo con las especificaciones y requisitos del software. Este proceso implica una 

atención cuidadosa para asegurar que la solución propuesta no introduzca nuevas complicaciones o 

problemas en otras áreas del sistema. 

Una vez implementada la corrección, se procede a las pruebas exhaustivas para verificar que el defecto 

ha sido completamente resuelto y que ninguna funcionalidad relacionada ha sido afectada negativamente 

por la solución. Esta fase es fundamental para garantizar que el software mantenga su integridad y 

funcionalidad original, cumpliendo con las expectativas de calidad y satisfacción del usuario. 

La implementación efectiva de este ciclo de vida no solo se enfoca en resolver problemas específicos de 

manera eficiente, sino que también promueve una cultura de calidad dentro de los equipos de desarrollo 

y prueba. Facilita la colaboración entre diferentes áreas, fomentando un ambiente donde la mejora 

continua y la atención al detalle son prioritarias. 

**Apunte 3 – Ciclo de vida del defecto** **Testing Aplicado al Desarrollo de Sistemas – IF203** 

Al entender y aplicar estos principios, las organizaciones pueden optimizar significativamente sus 

procesos de desarrollo de software. Esto no solo se traduce en la entrega de productos más confiables 

y satisfactorios para los usuarios finales, sino que también fortalece la reputación y la competitividad en 

el mercado, estableciendo estándares elevados de calidad y excelencia en la industria del software. 

 

Referencia Bibliografía

 Atlassian. (s.f.). Jira Software. https://www.atlassian.com/software/jira Bugzilla. (s.f.). Bugzilla. Recuperado el 17 de junio de 2024, de [https://www.bugzilla.org/](https://www.bugzilla.org/)[ ](https://www.bugzilla.org/) Redmine. (s.f.). Redmine. [https://www.redmine.org/](https://www.redmine.org/)[ ](https://www.redmine.org/) Agile Alliance. (s.f.). Understanding Agile Software Development and Testing. https://www.agilealliance.org/agile101/ Lewis, W. E. (2000). *Software Testing and Continuous Quality Improvement* (2da ed.). Auerbach Publications. Black, R. (2002). *Managing the Testing Process: Practical Tools and Techniques for Managing* *Hardware and Software Testing*. Wiley. 

**Referencia del presente documento:** Instituto San Sebastián, Innovación académica (2024). *Apunte 3:Ciclo de vida del defectoH*. Santiago. 

 

---

# **Testing Aplicado al Desarrollo de Sistemas** 

# Código:IF203 

 

 

 

 

 

 

 

 

 

 

 

## **Apunte N° 3** 

## **Defectos** 

**Apunte 3 – Título del apunte** **Testing Aplicado al Desarrollo de Sistemas– IF203** 

Introducción

 

El presente documento tiene como finalidad presentar los defectos en software, conocidos como bugs, 

han sido una preocupación desde los primeros días de la informática. A medida que la tecnología ha 

avanzado, estos errores han evolucionado desde simples anomalías hasta problemas críticos que 

pueden comprometer la seguridad y funcionalidad de sistemas completos. A lo largo de la historia del 

desarrollo de software, desde el primer uso documentado del término "bug" por Grace Hopper en 1947 

hasta la actualidad dominada por metodologías ágiles y DevOps, la gestión de defectos ha sido un 

desafío constante y crucial. 

Inicialmente, los bugs eran a menudo problemas físicos, como la famosa "polilla" que causó un fallo en 

el ordenador Mark II en Harvard. A medida que los sistemas informáticos se volvieron más complejos y 

sofisticados, los defectos se multiplicaron y se diversificaron. En las décadas de 1960 y 1970, con el 

desarrollo de lenguajes de programación más avanzados y sistemas operativos robustos, la detección y 

corrección de bugs se convirtieron en procesos más estructurados. En los años 1980, con la explosión 

de la industria del software, surgió la necesidad de métodos más rigurosos para gestionar y mitigar los 

defectos. 

Desde entonces, la importancia de las pruebas de software y la gestión de calidad ha ido en aumento. 

En los años 1990 y 2000, con la creciente complejidad de las aplicaciones empresariales y la expansión 

de Internet, la gestión de defectos se convirtió en una parte integral del ciclo de vida del desarrollo de 

software. Hoy en día, con metodologías ágiles que enfatizan la entrega rápida y continua, y DevOps que 

promueve la integración estrecha entre desarrollo y operaciones, la detección temprana y la corrección 

ágil de bugs son fundamentales para garantizar la estabilidad y seguridad del software en un entorno 

tecnológico dinámico y globalizado. 

Junto a lo anterior, verán, a lo largo del documento, algunas preguntas de análisis para corroborar la 

comprensión de los contenidos presentados, las cuales son útiles para el desarrollo de esos 

conocimientos en el ambiente laboral. 

Éxito en el estudio de este apunte, el cual es clave para profundizar aún más en el uso de las tecnologías. 

 

**Apunte 3 – Título del apunte** **Testing Aplicado al Desarrollo de Sistemas– IF203** 

Defectos

 

Defectos 

Un Poco de Historia 

Los defectos en software, también conocidos como bugs, han sido una parte inevitable del desarrollo de 

software desde sus inicios. La historia de los defectos en software se remonta a las primeras 

computadoras y los primeros lenguajes de programación. Desde entonces, estos errores han 

evolucionado en complejidad y consecuencias, reflejando los avances tecnológicos y las demandas 

cambiantes del mercado. 

1947: El término "bug" en el contexto informático fue popularizado por Grace Hopper, quien descubrió 

una polilla atrapada en un relé del ordenador Mark II en la Universidad de Harvard, causando un fallo. 

Este incidente marcó un hito en la historia de la informática, estableciendo el término "bug" como una 

referencia común para errores en el software y hardware. 

1960s-1970s: Con el desarrollo de lenguajes de programación más avanzados y sistemas operativos 

complejos, los defectos en software se volvieron más comunes y evidentes. La creciente sofisticación 

del software incrementó la complejidad de su desarrollo y testing, resultando en la identificación más 

frecuente de bugs que afectaban desde pequeñas aplicaciones hasta grandes sistemas empresariales. 

* 1980s: La llegada de las microcomputadoras y la expansión exponencial de la industria del 

software llevaron a un aumento significativo en la cantidad de software producido. Esta 

expansión no solo incrementó las oportunidades de innovación, sino también la presencia de 

defectos en el software debido a la rápida evolución tecnológica y las crecientes expectativas de 

los usuarios. 

* 1990s: Con la explosión de Internet y el surgimiento de aplicaciones web, los defectos en 

software adquirieron una dimensión crítica de seguridad. La exposición a amenazas cibernéticas 

y la capacidad de los bugs para comprometer la integridad y privacidad de los datos llevaron a 

un enfoque renovado en la ciberseguridad y la gestión proactiva de riesgos en el desarrollo de 

software. 

* 2000s-Presente: En la era actual, caracterizada por metodologías ágiles como Scrum y 

metodologías de entrega continua como DevOps, la gestión de defectos se ha convertido en un 

proceso integrado y dinámico dentro del ciclo de vida del desarrollo de software. La 

implementación de herramientas automatizadas, técnicas avanzadas de pruebas y la 

colaboración continua entre equipos de desarrollo y operaciones han mejorado 

**Apunte 3 – Título del apunte** **Testing Aplicado al Desarrollo de Sistemas– IF203** 

significativamente la capacidad de detectar y corregir bugs de manera eficiente. A pesar de estos 

avances, la creciente complejidad del software y las demandas del mercado globalizado 

aseguran que los bugs continúen siendo un desafío persistente para la industria del software. 

Este recorrido histórico subraya cómo los defectos en software han evolucionado junto con la tecnología 

misma, destacando la importancia de estrategias efectivas de gestión de calidad y seguridad para 

garantizar la fiabilidad y el rendimiento de los sistemas informáticos en el mundo moderno. 

 Procesos 

El proceso de gestión de defectos comienza con la identificación y reporte efectivo de los problemas 

encontrados durante el desarrollo y las pruebas de software. Este proceso incluye varios pasos cruciales: 

* Pruebas de Software: Los equipos de testing ejecutan una variedad de pruebas que incluyen 

pruebas unitarias, de integración, de sistema y de aceptación. Cada una de estas pruebas está 

diseñada para detectar diferentes tipos de defectos, desde errores de lógica en el código hasta 

problemas de integración entre módulos o sistemas. 

* Registro de Defectos: Una vez que se identifica un defecto, se registra de manera detallada en 

un sistema de seguimiento de errores o bug tracker como JIRA, Bugzilla o Trello. La información 

registrada suele eincluir el comportamiento anómalo observado, los pasos exactos para 

reproducir el defecto, la severidad (impacto potencial en el software) y el entorno específico 

donde se produjo el problema. Este registro detallado no solo facilita la comunicación entre los 

equipos de desarrollo y testing, sino que también proporciona una referencia histórica crucial 

para futuras revisiones y mejoras del software. 

Análisis y Priorización 

Después de que un defecto ha sido reportado, se procede con su análisis y priorización, lo cual es 

fundamental para una gestión efectiva de defectos: 

* Análisis de Causa Raíz (RCA): Se utiliza el análisis de causa raíz para identificar y comprender 

las razones fundamentales que causaron el defecto. Técnicas como los diagramas de Ishikawa 

(causa y efecto) o los 5 Porqués son comúnmente empleadas para explorar las diferentes capas 

de causalidad y descubrir las verdaderas raíces del problema. Este proceso no solo ayuda a 

abordar el síntoma visible del defecto, sino que también contribuye a prevenir recurrencias 

futuras al atacar las causas subyacentes. 

* Priorización: Una vez identificada la causa raíz, el defecto se prioriza en función de su impacto y 

urgencia. Los criterios de priorización incluyen la gravedad del defecto (crítico, mayor, menor), 

**Apunte 3 – Título del apunte** **Testing Aplicado al Desarrollo de Sistemas– IF203** 

la frecuencia con la que ocurre, y el impacto potencial en los usuarios finales o en otros 

componentes del sistema. Estas categorías de prioridad aseguran que los recursos se asignen 

de manera efectiva, enfocándose primero en los problemas que tienen el mayor impacto en la 

calidad y la funcionalidad del software. 

Corrección y Validación 

Una vez priorizado, el defecto pasa por el proceso de corrección y validación para asegurar que se 

implemente una solución efectiva y que el software mantenga su integridad y funcionalidad: 

* Implementación de Soluciones: Los desarrolladores toman las medidas necesarias para corregir 

el código defectuoso. Esto implica realizar cambios específicos en el código fuente del software 

para abordar las causas subyacentes del defecto identificado. Es crucial que estas correcciones 

se realicen de manera precisa y eficiente para evitar introducir nuevos problemas o afectar 

negativamente otras partes del sistema. 

* Pruebas de Regresión: Después de implementar las correcciones, se ejecutan pruebas de 

regresión. Estas pruebas aseguran que las modificaciones realizadas para corregir el defecto no 

hayan introducido nuevos errores o afectado inadvertidamente a otras áreas del software que 

funcionaban correctamente previamente. La finalidad de las pruebas de regresión es verificar 

que el software modificado continúe operando de manera coherente y cumpla con los requisitos 

y expectativas definidos. 

* Validación: Finalmente, los testers validan la corrección del defecto en un entorno de prueba o 

simulación que refleje fielmente las condiciones donde inicialmente se detectó el problema. 

Siguiendo los pasos detallados en el reporte inicial del defecto, se verifica que la anomalía 

observada haya sido completamente corregida y que el comportamiento del software ahora 

cumpla con las expectativas establecidas. 

Este enfoque estructurado y metodológico en la gestión de defectos asegura que los problemas 

identificados durante el desarrollo de software se aborden de manera efectiva y oportuna, garantizando 

así la calidad, la fiabilidad y la seguridad del producto final entregado a los usuarios. 

 Roles Involucrados 

La gestión efectiva de defectos en software implica la colaboración de diversos roles especializados que 

contribuyen desde distintas perspectivas al proceso de desarrollo y mejora continua del producto: 

* Desarrolladores: Este equipo es responsable de escribir y mantener el código fuente del 

software. Además de desarrollar nuevas funcionalidades, los desarrolladores tienen la tarea 

**Apunte 3 – Título del apunte** **Testing Aplicado al Desarrollo de Sistemas– IF203** 

crucial de corregir los defectos identificados durante las pruebas y el uso del software en 

producción. Su experiencia técnica y capacidad para implementar soluciones eficientes son 

fundamentales para mantener la integridad y funcionalidad del producto. 

* Testers/QA (Quality Assurance): Los testers desempeñan un papel esencial al ejecutar diversas 

pruebas diseñadas para identificar defectos en el software. Esto incluye pruebas unitarias, de 

integración, de sistema y de aceptación, entre otras. Además de detectar errores, los testers 

también verifican que las correcciones realizadas por los desarrolladores funcionen 

correctamente y no introduzcan nuevos problemas en el sistema. Su objetivo es garantizar que 

el software cumpla con los estándares de calidad definidos antes de su liberación. 

* Gerentes de Proyecto: Supervisan el progreso general del proyecto, incluida la gestión de 

defectos. Su responsabilidad incluye la planificación y asignación de recursos, la coordinación 

entre equipos y la evaluación del impacto de los defectos en los objetivos del proyecto. Los 

gerentes de proyecto juegan un papel crucial en la priorización de tareas y la resolución de 

conflictos para asegurar que el proyecto avance de manera eficiente y cumpla con los plazos 

establecidos. 

* Analistas de Negocios: Estos profesionales ayudan a priorizar los defectos según su impacto en 

el negocio y en los usuarios finales. Comprenden los requisitos del cliente y las expectativas del 

usuario final, lo que les permite evaluar la severidad y el riesgo asociado a cada defecto 

reportado. Su aportación es crucial para asegurar que los recursos se asignen de manera 

efectiva y que los esfuerzos de desarrollo se centren en áreas que maximicen el valor para el 

negocio. 

* Usuarios Finales: Aunque no siempre están directamente involucrados en el proceso de gestión 

de defectos, los usuarios finales desempeñan un papel importante al proporcionar 

retroalimentación sobre el software en producción. A veces, los usuarios identifican y reportan 

defectos que no fueron detectados durante las fases de pruebas previas. Esta retroalimentación 

es valiosa para mejorar la experiencia del usuario y abordar problemas que puedan afectar la 

satisfacción del cliente. 

Mejores Prácticas 

Para optimizar la gestión de defectos y mejorar la calidad del software, se recomienda seguir las 

siguientes mejores prácticas: 

* Automatización de Pruebas: Utilizar herramientas de pruebas automatizadas para incrementar 

la eficiencia y cobertura de pruebas. La automatización permite ejecutar pruebas repetitivas de 

manera rápida y precisa, identificando defectos de forma temprana en el ciclo de desarrollo. 

**Apunte 3 – Título del apunte** **Testing Aplicado al Desarrollo de Sistemas– IF203** 

* Integración Continua/Entrega Continua (CI/CD): Implementar pipelines de CI/CD para 

automatizar la integración, prueba y entrega de código. Esto facilita la detección temprana de 

defectos y la entrega rápida de nuevas funcionalidades al usuario final, minimizando el riesgo de 

errores en producción. 

* Revisiones de Código: Realizar revisiones regulares de código entre pares o equipos para 

identificar posibles defectos antes de que se integren al repositorio principal. Las revisiones de 

código fomentan la colaboración y el intercambio de conocimientos, mejorando la calidad y 

consistencia del código desarrollado. 

* Pruebas de Seguridad: Incluir pruebas de seguridad como parte integral del proceso de 

desarrollo para identificar y mitigar vulnerabilidades que podrían ser explotadas por atacantes. 

La seguridad del software es fundamental para proteger la información sensible y mantener la 

confianza de los usuarios. 

 Protocolos Estándar 

Además de seguir las mejores prácticas mencionadas, es fundamental adherirse a protocolos estándar 

que guíen el proceso de gestión de defectos: 

* Ciclo de Vida de Desarrollo de Software (SDLC): Seguir un ciclo de vida estructurado como Agile, 

Waterfall u otros métodos adaptativos que incluyan fases bien definidas de desarrollo, pruebas 

y validación. Esto proporciona un marco claro para gestionar el proceso desde la concepción 

hasta la entrega y mantenimiento del software. 

* Gestión de la Configuración: Mantener un control estricto sobre las versiones del software y sus 

cambios mediante prácticas de gestión de configuración. Esto asegura que todas las 

modificaciones al código fuente y la configuración del sistema se realicen de manera controlada 

y documentada, evitando conflictos y errores no deseados. 

* Documentación: Documentar todos los defectos identificados y las soluciones implementadas 

para futuros análisis y prevención. La documentación detallada facilita la revisión histórica de 

problemas similares, la identificación de patrones recurrentes y la implementación de mejoras 

continuas en el proceso de desarrollo de software. 

Implementar estos métodos de trabajo y protocolos estándar no solo mejora la eficiencia operativa y la 

calidad del software, sino que también fortalece la capacidad del equipo para responder rápidamente a 

los desafíos y exigencias del entorno tecnológico actual. 

 

 

**Apunte 3 – Título del apunte** **Testing Aplicado al Desarrollo de Sistemas– IF203** 

Ventajas 

La gestión efectiva de defectos en software ofrece una serie de beneficios significativos que mejoran la 

calidad, la seguridad y la eficiencia del producto final: 

Eficiencia 

La detección temprana y corrección de defectos durante el ciclo de desarrollo conlleva varias ventajas: 

* Reducción de Costos: Identificar y corregir defectos en etapas tempranas del desarrollo minimiza 

los costos asociados con su reparación posteriormente en el ciclo de vida del software. Corregir 

problemas antes de que se propaguen a otras partes del sistema o lleguen a producción evita 

gastos adicionales y recursos que podrían ser necesarios para abordar problemas más 

complejos y costosos en fases avanzadas del proyecto. 

* Mejora de la Calidad: Un enfoque sistemático en la gestión de defectos contribuye directamente 

a mejorar la calidad general del software. Al abordar y resolver problemas de manera proactiva, 

se asegura que el producto final cumpla con los estándares de funcionalidad y rendimiento 

esperados, lo cual se traduce en una mejor experiencia del usuario y una mayor satisfacción. 

Impacto Positivo 

Además de mejorar la eficiencia y reducir costos, la gestión efectiva de defectos también tiene un impacto 

positivo en otros aspectos clave del desarrollo de software: 

* Seguridad Aumentada: Identificar y corregir defectos ayuda a reducir las vulnerabilidades de 

seguridad del software. Al abordar problemas potenciales antes de que puedan ser explotados 

por actores malintencionados, se fortalece la seguridad del sistema y se protege la integridad de 

los datos y la información confidencial de los usuarios. 

* Confianza del Cliente: Un software con menos defectos inspira confianza en los clientes y 

usuarios finales. La capacidad de entregar productos estables y libres de errores aumenta la 

credibilidad de la organización en el mercado, fortaleciendo las relaciones con los clientes y 

fomentando la lealtad a largo plazo. 

 

 

 

**Apunte 3 – Título del apunte** **Testing Aplicado al Desarrollo de Sistemas– IF203** 

Desventajas 

A pesar de sus numerosas ventajas, la gestión de defectos en software también presenta ciertos desafíos 

y riesgos que deben ser considerados: 

Desafíos y Riesgos 

* Costo Inicial: Implementar procesos y herramientas efectivas de gestión de defectos puede ser 

costoso inicialmente. Esto incluye la adquisición de software especializado, la capacitación del 

personal y la dedicación de recursos para establecer y mantener prácticas robustas de gestión 

de calidad. Para algunas organizaciones, especialmente las pequeñas o emergentes, este costo 

inicial puede representar una barrera significativa para la adopción de prácticas avanzadas de 

gestión de defectos. 

* Requiere Recursos: La gestión de defectos efectiva demanda personal capacitado y tiempo 

dedicado. La identificación, análisis, corrección y validación de defectos requiere la colaboración 

de desarrolladores, testers y otros profesionales involucrados en el ciclo de vida del software. 

Esta necesidad de recursos puede ser un desafío para equipos pequeños o aquellos con 

recursos limitados, quienes podrían enfrentar dificultades para asignar suficientes recursos 

humanos y temporales a la gestión adecuada de defectos. 

* Complejidad Adicional: La implementación de procesos y herramientas de gestión de defectos 

puede agregar complejidad al flujo de trabajo existente. Esto puede resultar en una curva de 

aprendizaje para el personal y una necesidad de gestión cuidadosa para asegurar que los 

procesos no ralenticen el desarrollo o introduzcan nuevos problemas operativos. La complejidad 

adicional puede requerir ajustes continuos y optimización de los procesos para garantizar que 

sigan siendo efectivos y eficientes a medida que evoluciona el proyecto. 

Posibles Riesgos 

* Sobrecarga de Información: Un volumen excesivo de defectos reportados puede sobrecargar al 

equipo de desarrollo y testing, dificultando la priorización efectiva y la atención adecuada a los 

problemas más críticos. Manejar grandes cantidades de información sobre defectos requiere 

sistemas y prácticas claras para filtrar, priorizar y abordar los problemas de manera eficiente. 

* Falsos Positivos: Las pruebas automatizadas, si no se configuran adecuadamente, pueden 

generar falsos positivos. Esto significa que se reportan defectos que en realidad no existen o no 

representan un problema real para el funcionamiento del software. La identificación y gestión de 

falsos positivos puede consumir recursos y tiempo innecesarios, desviando la atención del 

equipo de desarrollo de problemas genuinos que requieren atención inmediata. 

**Apunte 3 – Título del apunte** **Testing Aplicado al Desarrollo de Sistemas– IF203** 

En resumen, mientras que la gestión de defectos en software proporciona numerosas ventajas 

significativas en términos de eficiencia, calidad y seguridad, también conlleva desafíos y riesgos 

inherentes que deben ser gestionados de manera efectiva para maximizar los beneficios y minimizar las 

complicaciones durante el ciclo de vida del desarrollo de software. 

**Problemas que nos afectaron** 

A lo largo de la historia del desarrollo de software, varios incidentes han destacado la importancia crítica 

de la gestión efectiva de defectos. A continuación, se presentan ejemplos específicos que ilustran las 

consecuencias significativas de los errores en el software: 

 Ariane 5 

En 1996, el cohete Ariane 5 de la Agencia Espacial Europea (ESA) sufrió una devastadora explosión 

apenas 40 segundos después de su lanzamiento. Este incidente fue atribuido a un error en el software 

de navegación del cohete. El software estaba diseñado para convertir datos de posición de 64 bits a 16 

bits, pero un valor excedió el rango permitido. Esta situación llevó a una excepción no manejada que 

resultó en la pérdida total del cohete y su carga útil, con un costo estimado de cientos de millones de 

dólares. 

El incidente del Ariane 5 puso de relieve la importancia crítica de pruebas exhaustivas, validación rigurosa 

y gestión efectiva de excepciones en el desarrollo de software para sistemas complejos y de alta 

seguridad como los cohetes espaciales. 

 Therac-25 

Entre 1985 y 1987, varios pacientes recibieron dosis letales de radiación durante tratamientos de 

radioterapia con la máquina Therac-25. Estos accidentes fueron causados por errores en el software de 

control del dispositivo, que permitieron la activación inadvertida de dosis de radiación excesivas. Seis 

pacientes murieron como resultado directo de estas sobredosis. 

El caso Therac-25 resalta las consecuencias graves de los defectos de software en aplicaciones críticas 

para la salud y la seguridad pública. En este caso particular, los problemas de diseño y pruebas 

insuficientes del software llevaron a trágicas consecuencias humanas, subrayando la necesidad 

imperativa de prácticas robustas de desarrollo y pruebas en sectores donde los errores pueden tener 

consecuencias mortales. 

 

**Apunte 3 – Título del apunte** **Testing Aplicado al Desarrollo de Sistemas– IF203** 

**Lecciones Aprendidas** 

Estos ejemplos subrayan la importancia de implementar prácticas sólidas de gestión de defectos y 

aseguramiento de la calidad en todos los aspectos del desarrollo de software. La detección temprana y 

la corrección de defectos, junto con pruebas exhaustivas y validación rigurosa, son fundamentales para 

evitar incidentes catastróficos como los descritos. Además, estos casos destacan la responsabilidad ética 

y profesional de los desarrolladores, testers y otros profesionales de TI en garantizar la integridad y la 

seguridad de los sistemas que diseñan y mantienen. 

 **COMPRUEBO MI APRENDIZAJE** 

1. ¿Cómo podría beneficiar la integración continua (CI) y la 

entrega continua (CD) en la detección y corrección rápida de defectos en un proyecto de desarrollo de software? 

2. ¿Quién fue la persona que popularizó el término "bug" en el 

contexto informático en 1947? 

3. ¿Cuáles son los tipos principales de pruebas de software 

utilizadas para identificar defectos y en qué etapas del desarrollo se aplican? 

#### **Información complementaria** 

Link 1: **Practical Software Testing** https://www.softwaretestinghelp.com/practical-software-testing-new-free-ebook-download/ 

Conclusión

 

En conclusión, la gestión de defectos en software no solo es una práctica técnica esencial, sino que representa un componente fundamental para asegurar la competitividad y la confiabilidad de las soluciones tecnológicas en un entorno empresarial globalizado y dinámico. Desde los primeros registros históricos hasta las metodologías contemporáneas como Agile y DevOps, hemos observado una evolución significativa en la forma en que se abordan y manejan los defectos en el desarrollo de software. 

Históricamente, los defectos en software han sido una preocupación constante desde los albores de la informática. Con el tiempo, han pasado de ser simples errores técnicos a ser problemas críticos que pueden afectar la seguridad, la funcionalidad y la reputación de las organizaciones. La adopción de enfoques estructurados para identificar, reportar, corregir y prevenir defectos ha mejorado radicalmente gracias a avances en metodologías de desarrollo, herramientas de gestión de proyectos y técnicas de aseguramiento de la calidad. 

La implementación de buenas prácticas en la gestión de defectos, como la automatización de pruebas para una cobertura más exhaustiva y eficiente, la integración continua para detectar y corregir problemas de manera temprana, y la gestión rigurosa de cambios para mantener la estabilidad del software, se ha convertido en estándar en la industria del desarrollo de software. Estas prácticas no solo ayudan a reducir los costos asociados con la corrección de errores en etapas avanzadas del ciclo de vida del software, sino que también mejoran la eficiencia operativa y la satisfacción del cliente al ofrecer productos más robustos y confiables. 

Mirando hacia el futuro, el panorama tecnológico continúa evolucionando con la introducción de nuevas plataformas, arquitecturas y demandas de mercado. La capacidad de adaptarse y mejorar constantemente las estrategias de gestión de defectos será crucial para enfrentar los desafíos emergentes y aprovechar las oportunidades en un entorno competitivo. Las organizaciones que mantienen un enfoque proactivo en la calidad del software no solo protegen su reputación y competitividad, sino que también establecen un estándar de excelencia que fortalece su posición en el mercado global. 

En resumen, la gestión efectiva de defectos en software no solo es un requisito técnico, sino un imperativo estratégico para las empresas que buscan mantenerse relevantes y competitivas en un mercado impulsado por la innovación y la calidad. Al invertir en prácticas sólidas de gestión de defectos, las organizaciones pueden no solo mitigar riesgos y optimizar costos, sino también construir una base sólida para el crecimiento sostenible y el éxito a largo plazo en la industria del software. 

 

 

 

 

 

 

 

 

**Apunte 3 – Título del apunte** **Testing Aplicado al Desarrollo de Sistemas– IF203** 

**Apunte 3 – Título del apunte** **Testing Aplicado al Desarrollo de Sistemas– IF203** 

Referencia Bibliografía

 

1. Myers, G. J. (2011). *The Art of Software Testing* (3rd ed.). Wiley. 
2. Martin, R. C. (2008). *Clean Code: A Handbook of Agile Software Craftsmanship*. Prentice Hall. 
3. ISO/IEC 25010:2011. (2011). *Systems and software engineering — Systems and software Quality Requirements and Evaluation (SQuaRE) — System and software quality models*. International Organization for Standardization. 
4. ISO/IEC/IEEE 29119-1:2013. (2013). *Systems and software engineering — Software testing — Part 1: Concepts and definitions*. International Organization for Standardization. 
5. Pressman, R. S., & Maxim, B. R. (2014). *Software Engineering: A Practitioner's Approach* (8th ed.). McGraw-Hill Education. 
6. SoftwareTestingHelp. (s.f.). Defect Management in Software Testing. https://www.softwaretestinghelp.com/defect-management-software-testing/ 

 

**Referencia del presente documento:** Instituto San Sebastián, Innovación académica (2024). *Apunte 3: Defectos*. Testing Aplicado al Desarrollo de Sistemas. Santiago. 

 

---

 

**EVALUACIÓN U3: AUDITORÍA DE CALIDAD Y PRUEBAS PARA UN SOCIO FORMADOR** 

Resultados de Aprendizaje 

Esta evaluación está diseñada para que logres los siguientes resultados de aprendizaje (RA) del 

curso, en concordancia con la rúbrica de la unidad: 

 

1. Aplicar pruebas manuales a un software, documentando la ejecución y gestionando los 

defectos encontrados. 

1. Comprender el funcionamiento de herramientas para la gestión y automatización de pruebas. 

 

* Formular soluciones que integren conceptos de accesibilidad y usabilidad. 
* Aplicar estrategias de optimización y evaluar el rendimiento. 
* Evaluar la seguridad de la aplicación y el consumo de endpoints. 
* Elaborar documentación técnica detallada y comunicar el conocimiento de 

forma efectiva. 

* Gestionar la colaboración en equipo utilizando herramientas digitales. 

 

## 1. **Contexto del Proyecto** 

En el marco de la estrategia de Vinculación con el Medio (VcM), esta evaluación te sumergirá 

en un escenario de consultoría real. Trabajarás como parte de una firma de Aseguramiento 

de la Calidad (QA) para Software de Firma Digital para la empresa Comercial Multi Más. Su 

misión es liderar una auditoría de calidad exhaustiva del sitio web de la comercial, aplicando 

un proceso profesional para diagnosticar su estado actual y entregar un plan de acción 

estratégico que aporte valor a su negocio. 

Actor de Interés: Comercial Multimás 

Plataforma a Evaluar: https://ventasonline.comercialmultimas.cl/ 

 

 

 

 

 

 

 

 

## 2. **Problemática a Resolver** 

 

De cara a la próxima entrada en vigencia de la **Ley N° 21.719 sobre Protección de Datos** 

**Personales en Chile**, programada para el 1 de diciembre de 2026, la empresa *Comercial Multimás* 

se enfrenta a la necesidad crítica de adaptar y blindar su plataforma de comercio electrónico 

(ventasonline.comercialmultimas.cl). Actualmente, el sitio web opera con un flujo constante de datos 

transaccionales, registros de clientes y procesos comerciales presenciales y digitales integrados. Sin 

embargo, la falta de un diagnóstico exhaustivo en etapas tempranas genera una incertidumbre 

técnica y legal, ya que eventuales vulnerabilidades de seguridad, errores funcionales, fallas de 

rendimiento y deficiencias en la usabilidad no solo comprometen los objetivos de negocio y la 

experiencia del usuario, sino que exponen a la organización a severas sanciones por incumplimiento 

normativo. 

 

 

Rol y Desafío del Equipo QA 

 

Ante este escenario, ustedes estudiantes como equipo de Aseguramiento de la Calidad (QA) asume 

el desafío de diseñar y ejecutar una **evaluación integral y multidimensional**. 

 

El problema radica en identificar, clasificar y priorizar de manera oportuna aquellas brechas críticas 

del sitio. El objetivo final es mitigar riesgos mediante la entrega de un informe profesional accionable y 

una presentación ejecutiva que traduzcan los hallazgos técnicos en recomendaciones estratégicas 

para garantizar un sitio web seguro, funcional, óptimo y 100% alineado con la nueva legislación 

chilena. 

 

# **INSTRUCCIONES** 

 

 

3. Organización de Equipos y Asignación de Pruebas 

La clase se dividirá en cuatro equipos de especialistas, cada uno con un rol único para 

garantizar una cobertura integral. 

* Equipo 1: Pruebas Funcionales ("Guardianes de la Lógica del Negocio") 
* Equipo 2: Pruebas de Rendimiento ("Arquitectos de la Estabilidad y Velocidad") 
* Equipo 3: Pruebas de Usabilidad y Accesibilidad ("Defensores de la Experiencia del 

Usuario") 

* Equipo 4: Pruebas de Seguridad y Endpoints ("Guardianes de la Integridad y los 

Datos") 

 

## 4. **Hitos Clave y Comunicación Profesional** 

Un trabajo profesional requiere una gestión de proyecto y comunicación impecables. 

* **Hito 1: Reunión de Kick-Off (Simulada)** 

○ Al inicio del proyecto, cada equipo preparará y participará en una reunión de 

lanzamiento para alinear expectativas, comprender las preocupaciones del 

cliente y definir los objetivos de negocio del sitio web. 

* **Hito 2: Presentación Final de Resultados** 

○ La evaluación culminará con una presentación ejecutiva donde los equipos 

comunicarán sus hallazgos, defenderán sus conclusiones y presentarán su 

plan de acción recomendado al Socio Formador. 

## 5. **Fases del Proyecto e Instrucciones** 

**Fase 1: Planificación Estratégica y Diseño de Pruebas** 

1. Análisis de Criticidad Funcional: Antes de diseñar las pruebas, todos los equipos 

colaborarán para identificar las funcionalidades clave del sitio. Deberán 

clasificarlas en un documento según su importancia para el negocio y el usuario, 

 

 

usando categorías como "Crítica", "Importante" y "Deseable". Esta clasificación será 

la base para priorizar el esfuerzo de testing. 

2. Elaborar Plan de Pruebas: Cada equipo creará un plan detallado que describa el 

alcance, la estrategia (basada en riesgos), los recursos y los criterios de éxito. 

3. Elaborar Matriz de Pruebas: Este es el entregable más importante de la 

planificación. Cada squad creará una matriz (en una hoja de cálculo) para diseñar 

y visualizar la cobertura de su funcionalidad. La matriz debe incluir, como mínimo, 

las siguientes columnas: 

○ ID Caso de Prueba: Identificador único (ej. BUS-001). 

○ Descripción del Caso de Prueba: Qué se va a probar. 

○ Tipo de Prueba: Funcional, Rendimiento, Usabilidad, Seguridad. 

○ Ruta Crítica (Sí/No): ¿Es parte de un flujo esencial que no puede fallar? 

○ Caso de Borde (Sí/No): ¿Prueba un límite del sistema (ej. búsqueda con 

0 resultados, filtros máximos aplicados)? 

○ Candidato a Automatización (Sí/No): ¿Es una prueba repetitiva y estable, 

ideal para automatizar en el futuro? 

○ Prioridad: Crítica, Alta, Media, Baja (definida por la combinación de las 

columnas anteriores). 

4. Diseñar Casos de Prueba: En una plataforma como Kiwi TCMS/TestLink, cada 

equipo diseñará sus casos de prueba, asignando una prioridad (Crítica, Alta, 

Media, Baja) justificada por la Matriz de Riesgos. 

Fase 2: Ejecución, Gestión y Análisis de Causa Raíz 

1. Ejecutar Casos de Prueba según el plan. 

2. Registrar resultados en la plataforma de gestión. 

3. Crear Informes de Defectos (Bug Reports): Para cada fallo, se creará un informe 

detallado que, además de los elementos estándar (pasos, evidencia, 

severidad), deberá incluir un campo de "Posible Causa Raíz", donde el equipo 

hipotetiza sobre el origen técnico del problema. 

 

Fase 3: Análisis, Informe Final y Propuesta de Valor 

1. Análisis de hallazgos: Cada equipo analizará sus resultados y redactará su 

sección del informe. 

2. Consolidación del Informe de Auditoría de Calidad: Se creará un único 

documento profesional que debe incluir: 

○ Resumen Ejecutivo: Síntesis para la gerencia. 

○ Metodología y Criterios de Priorización: Explicación del enfoque basado en la 

criticidad funcional. 

○ Resultados por Área (con Métricas y KPIs): Cada sección debe incluir datos 

cuantitativos. Por ejemplo: 

■ Funcional: % de casos exitosos/fallidos, densidad de defectos. 

■ Rendimiento: Tiempos de respuesta en segundos, tasa de error bajo 

carga. 

■ Usabilidad: Tasa de éxito de tareas, puntuación heurística. 

■ Seguridad: Nº de vulnerabilidades por nivel de riesgo (Crítico, Alto, 

Medio). 

○ Matriz de Defectos Priorizados: Listado de los bugs más importantes. 

○ Propuesta de Estrategia de Automatización: Una sección que identifique los 3-5 

casos de prueba ideales para automatizar, justificando su elección, 

recomendando una herramienta (ej. Selenium, Cypress) y explicando el retorno 

de la inversión (ROI) a largo plazo. 

○ Conclusiones y Plan de Acción Recomendado: Pasos claros y priorizados 

para que el cliente pueda abordar los problemas. 

 

 

 

# **ENTREGABLES** 

 

1. Enlace público al proyecto en Kiwi TCMS (o similar) con planes, matriz de 

riesgos, casos de prueba y resultados. 

2. Informe Final de Auditoría de Calidad en formato PDF. 

3. Diapositivas de la Presentación Final Ejecutiva en formato PDF. 

4. Carga del documento a EVA 

El informe debe ser subido individualmente por cada estudiante en la plataforma EVA. 

6. Evaluación 

El proyecto será evaluado utilizando la Rúbrica de la Unidad 3. Se valorará la rigurosidad 

técnica, la calidad de la documentación, la claridad de la comunicación y la capacidad de 

aportar valor estratégico al Socio Formador, simulando un entorno de consultoría 

profesional. 

 

---

 

# **Ficha VcM Actor Externo** 

## **Asignatura para el desarrollo de Soluciones Tecnológicas** 

Información Actor de Interés Externo 

| Información general de la empresa | Distribuidora Online |
|---|---|
| Nombre de la organización | Multimás |
| Nombre del representante | Francisco Leyán |
| Cargo del representante | CEO |
| Área de la organización que representa |  |
| Email del representante | ventas@comercialmultimas.cl |
| Número de contacto telefónico del
representante |  |
| Breve descripción de la organización | La plataforma ventasonline.comercialmultimas.cl es el
canal de comercio electrónico de Comercial Multimás
Ltda., una empresa distribuidora chilena ubicada en la
comuna de Talagante, Región Metropolitana. Este sitio
web está diseñado para facilitar la compra digital tanto a
clientes particulares como a comercios, ofreciendo un
amplio catálogo de productos de consumo masivo que
abarcan categorías esenciales como despensa, limpieza y
aseo, perfumería, confitería, artículos de cumpleaños,
repostería, librería, alimentos para mascotas y accesorios
para el jardín.
La tienda online destaca por su enfoque en la venta
mayorista y el abastecimiento comercial, permitiendo a
los usuarios registrarse para acceder a atención
personalizada de ejecutivos y un canal de venta
estructurado. Además, cuenta con un sistema de
distribución enfocado principalmente en cubrir diversas
comunas de la Región Metropolitana (como Talagante,
Melipilla, Peñaflor, Buin, entre otras), proporcionando una
alternativa cómoda y eficiente para compras de volumen,
respaldada por herramientas de transparencia de cara al
consumidor como su propio libro de reclamaciones digital. |

 

1 

 

Descripción del desafío 

Describa en detalle el desafío que enfrenta su empresa en el área: 

De cara a la próxima entrada en vigencia de la Ley N° 21.719 sobre Protección de Datos Personales en Chile, programada para el 1 de diciembre de 2026, como empresa nos enfrentamos a la necesidad crítica de adaptar y blindar la plataforma de comercio electrónico 

¿Cuáles son los principales problemas o síntomas que observa como consecuencia de este desafío? 

No contar con la información sobre la nueva ley que se debe evaluación 

 

¿Qué impacto negativo tiene este desafío en las operaciones o la productividad de su empresa? 

No creo que sea un impacto negativo. 

¿Cuánto tiempo lleva enfrentando este desafío? 

Desde que se informo de la nueva ley. 

 

¿Qué resultados o soluciones espera obtener con el desarrollo del proyecto? 

 

 ¿Qué disponibilidad horaria tiene para colaborar con los estudiantes involucrados en el proyecto? 

Miércoles de 10:00 a 12:00 

¿De qué manera se podrá otorgar acceso a los estudiantes a los sistemas o infraestructura de su empresa que sean relevantes para el desafío? 

 Mediante consultas y https://ventasonline.comercialmultimas.cl/ 

¿Existe alguna restricción o protocolo de seguridad que los estudiantes deban considerar al acceder a sus sistemas? 

**No** 

 

**Recursos Adicionales** 

2 

 

¿Dispone de diagramas de red lógicos y/o físicos que puedan ser útiles para los estudiantes en el desarrollo del proyecto? 

https://ventasonline.comercialmultimas.cl/ ¿Existe alguna otra información, documentación o recursos que puedan ser relevantes para que los estudiantes comprendan mejor el desafío? 

https://ventasonline.comercialmultimas.cl/ 

¿Cuenta con accesos y credenciales de administración a los equipos? 

no 

¿Existe algún aspecto o requisito específico que no se haya cubierto en las preguntas anteriores y que considere importante mencionar? 

no 

 

 

3 

---

 

# **Ficha VcM Actor Externo** 

## **Asignatura para el desarrollo de Soluciones Tecnológicas** 

Información Actor de Interés Externo 

| Información general de la empresa | Distribuidora Online |
|---|---|
| Nombre de la organización | Multimás |
| Nombre del representante | Francisco Leyán |
| Cargo del representante | CEO |
| Área de la organización que representa |  |
| Email del representante | ventas@comercialmultimas.cl |
| Número de contacto telefónico del
representante |  |
| Breve descripción de la organización | La plataforma ventasonline.comercialmultimas.cl es el
canal de comercio electrónico de Comercial Multimás
Ltda., una empresa distribuidora chilena ubicada en la
comuna de Talagante, Región Metropolitana. Este sitio
web está diseñado para facilitar la compra digital tanto a
clientes particulares como a comercios, ofreciendo un
amplio catálogo de productos de consumo masivo que
abarcan categorías esenciales como despensa, limpieza y
aseo, perfumería, confitería, artículos de cumpleaños,
repostería, librería, alimentos para mascotas y accesorios
para el jardín.
La tienda online destaca por su enfoque en la venta
mayorista y el abastecimiento comercial, permitiendo a
los usuarios registrarse para acceder a atención
personalizada de ejecutivos y un canal de venta
estructurado. Además, cuenta con un sistema de
distribución enfocado principalmente en cubrir diversas
comunas de la Región Metropolitana (como Talagante,
Melipilla, Peñaflor, Buin, entre otras), proporcionando una
alternativa cómoda y eficiente para compras de volumen,
respaldada por herramientas de transparencia de cara al
consumidor como su propio libro de reclamaciones digital. |

 

1 

 

Descripción del desafío 

Describa en detalle el desafío que enfrenta su empresa en el área: 

De cara a la próxima entrada en vigencia de la Ley N° 21.719 sobre Protección de Datos Personales en Chile, programada para el 1 de diciembre de 2026, como empresa nos enfrentamos a la necesidad crítica de adaptar y blindar la plataforma de comercio electrónico 

¿Cuáles son los principales problemas o síntomas que observa como consecuencia de este desafío? 

No contar con la información sobre la nueva ley que se debe evaluación 

 

¿Qué impacto negativo tiene este desafío en las operaciones o la productividad de su empresa? 

No creo que sea un impacto negativo. 

¿Cuánto tiempo lleva enfrentando este desafío? 

Desde que se informo de la nueva ley. 

 

¿Qué resultados o soluciones espera obtener con el desarrollo del proyecto? 

 

 ¿Qué disponibilidad horaria tiene para colaborar con los estudiantes involucrados en el proyecto? 

Miércoles de 10:00 a 12:00 

¿De qué manera se podrá otorgar acceso a los estudiantes a los sistemas o infraestructura de su empresa que sean relevantes para el desafío? 

 Mediante consultas y https://ventasonline.comercialmultimas.cl/ 

¿Existe alguna restricción o protocolo de seguridad que los estudiantes deban considerar al acceder a sus sistemas? 

**No** 

 

**Recursos Adicionales** 

2 

 

¿Dispone de diagramas de red lógicos y/o físicos que puedan ser útiles para los estudiantes en el desarrollo del proyecto? 

https://ventasonline.comercialmultimas.cl/ ¿Existe alguna otra información, documentación o recursos que puedan ser relevantes para que los estudiantes comprendan mejor el desafío? 

https://ventasonline.comercialmultimas.cl/ 

¿Cuenta con accesos y credenciales de administración a los equipos? 

no 

¿Existe algún aspecto o requisito específico que no se haya cubierto en las preguntas anteriores y que considere importante mencionar? 

no 

 

 

3 

---

## Planificación y Selección de Pruebas en el Desarrollo de Software

* Automatización de Pruebas y CI/CD

---

## ¿Qué veremos hoy en este módulo?

* Introducción a la Automatización de Pruebas
* Fundamentos de la Automatización de Pruebas
* Tipos de Pruebas Automatizadas
* Herramientas para la Automatización de pruebas
* Frameworks de Automatización de Pruebas

---

## Introducción

---

La automatización de pruebas es fundamental en el desarrollo moderno de software, permitiendo validación continua y eficiente. Utiliza herramientas y scripts para ejecutar pruebas automáticamente, mejorando la eficiencia y precisión. Históricamente, se desarrolló para reducir el tiempo y esfuerzo de las pruebas manuales. Las herramientas han avanzado, integrándose con métodos de entrega continua y ágiles. Las principales ventajas son la reducción de tiempo y la consistencia de los resultados, aunque presenta desafíos como el mantenimiento de scripts. En resumen, es esencial para asegurar la calidad del software en un entorno ágil.

---

## Fundamentos de la Automatización de Pruebas

---

## Historia

La automatización de pruebas ha avanzado desde los años 1980, impulsada por la complejidad del software y la necesidad de eficiencia.

**Años 1980:**Aparecen herramientas rudimentarias, específicas para ciertos lenguajes, reduciendo el tiempo y esfuerzo de pruebas manuales.

**Años 1990:**Se producen avances tecnológicos que mejoran las herramientas de automatización, como el desarrollo ágil. Herramientas comerciales como WinRunnerganan popularidad, estableciendo estándares.

**Años 2000:**Se da una expansión significativa con herramientas como Selenium y QTP, mejorando la integración con metodologías de entrega continua (CI/CD) y aumentando la flexibilidad y eficiencia de las pruebas.

---

## Definición

La automatización de pruebas utiliza herramientas y scripts para ejecutar pruebas de software automáticamente, simulando interacciones del usuario y verificando resultados. Abarca diversos tipos de pruebas (funcionales, regresión, carga, rendimiento) y genera informes detallados para identificar y corregir errores. Estas herramientas son flexibles y escalables, integrándose con sistemas de integración continua (CI/CD) para asegurar la estabilidad y funcionalidad del software durante su ciclo de vida.

---

## Propósito

La automatización de pruebas aumenta la eficiencia y efectividad del proceso de pruebas de software al permitir la ejecución rápida y exhaustiva de numerosos casos de prueba, reduciendo costos y tiempos. Libera a los testers de tareas repetitivas, mejorando su productividad y la calidad del software. Además, garantiza una mayor cobertura y consistencia en las pruebas, asegurando que todas las partes del software sean probadas exhaustivamente, incluyendo integraciones y detección de errores. Es crucial en el desarrollo moderno de software, permitiendo validación continua y mejor calidad en menos tiempo.

---

## Proceso

![image]()

---

## Ciclo de Vida

![image]()

---

## Roles

El proceso de automatización de pruebas involucra a diversos roles clave:

- Automatizadoresde Pruebas: Especialistas en la creación y mantenimiento de scripts de automatización. Diseñan, implementan, ejecutan y mantienen los scripts para asegurar su efectividad a lo largo del tiempo.

- Desarrolladores de Software: Colaboran con los automatizadorespara integrar las pruebas automatizadas en el ciclo de desarrollo, proporcionando información sobre nuevas funcionalidades y corrigiendo errores detectados. Ayudan a escribir y mantener scripts, especialmente en entornos ágiles con integración continua.

- Analistas de Calidad (QA): Revisan los resultados de las pruebas automatizadas y realizan pruebas manuales complementarias. Aseguran que los casos de prueba cubran todas las funcionalidades críticas y los resultados sean precisos. Identifican áreas que requieren pruebas manuales detalladas cuando la automatización no es viable.

---

## Mejores Prácticas

Para maximizar la efectividad de la automatización de pruebas, se deben seguir buenas prácticas:

- Selección de Casos de Prueba: Elegir casos repetitivos, críticos y con alta frecuencia de errores humanos para la automatización. Priorizar pruebas de funcionalidades críticas del sistema.

- Modularidad y Reusabilidad: Escribir scripts modulares y reutilizables para facilitar mantenimiento y expansión. Reutilizar componentes en múltiples pruebas ahorra tiempo y esfuerzo, mejorando la claridad y organización del código.

- Mantenimiento Regular: Actualizar y mantener scripts regularmente para adaptarse a cambios en la aplicación, reflejar nuevas funcionalidades, corregir errores y asegurar precisión y efectividad de las pruebas.

---

## Protocolos

La implementación de protocolos estándar es crucial para integrar la automatización de pruebas en el desarrollo de software, asegurando que las pruebas se ejecuten consistentemente y proporcionando validación continua.

* Integración Continua (CI): Integra pruebas automatizadas en el proceso de CI para ejecutar pruebas en cada cambio de código, permitiendo la detección temprana de errores y mejorando la estabilidad y calidad del software. Herramientas como Jenkins, CircleCI y Travis CI son comunes.
* Desarrollo Continuo (CD): Usa la automatización en pipelines de CD para garantizar calidad en el despliegue. Las pruebas automatizadas son obligatorias antes de desplegar en producción, asegurando que solo el software que pasa todas las pruebas se despliega, reduciendo riesgos y mejorando la confiabilidad.

La colaboración entre automatizadoresde pruebas, desarrolladores y analistas de calidad, junto con la aplicación de mejores prácticas y mantenimiento regular, asegura una validación continua y eficiente del software.

---

## Ventajas y Desventajas

![image]()

---

## Tipos de Pruebas Automatizadas

---

## Historia

![image]()

---

## Procesos y Pruebas

![image]()

---

## Roles

---

## Mejores prácticas

![image]()

---

## Protocolos

![image]()

---

## Herramientas para la Automatización de pruebas

---

## Herramientas

![image]()

---

## Frameworks de Automatización de Pruebas

---

## Historia

La automatización de pruebas ha evolucionado significativamente desde la década de 1990, impulsada por frameworks robustos que facilitan la creación, ejecución y mantenimiento de pruebas automatizadas.

Años 1990: Surgieron los primeros frameworks como JUnit, desarrollado por Kent Beck y Erich Gamma, estandarizando las pruebas unitarias automatizadas y permitiendo la verificación de pequeñas unidades de código de manera repetible y automatizada.

Años 2000: La automatización de pruebas se diversificó con herramientas como Selenium en 2004, que permitieron la interacción avanzada con navegadores web y pruebas de regresión, mejorando la flexibilidad y compatibilidad con múltiples lenguajes de programación. También se introdujo el Page ObjectPattern, facilitando la creación y mantenimiento de pruebas automatizadas.

---

## Proceso

![image]()

---

## Mejores prácticas

![image]()

---

---

## Unidad 3

Automatización

* Testing Aplicado al Desarrollo

---

## ÍNDICE

* Introducción
* Beneficios
* Herramientas
* Funciones
* Implementación y Gestión
* Planificación y Mantenimiento
* Seleccipon de Herramientas
* Estrategia
* Identificación y Documentación

---

## Introducción

La automatización de pruebas emerge como una herramienta revolucionaria, transformando el panorama de la evaluación de software. Al delegar tareas repetitivas a scripts y herramientas automatizadas, los desarrolladores y testers pueden enfocarse en aspectos más estratégicos y creativos, optimizando así el tiempo y los recursos disponibles.

---

## Definición

* La automatizaciónde pruebases el proceso de ejecutarpruebasde software automáticamenteutilizandoherramientasy scripts predefinidos, simulandola interacciónhumanacon el software.

![image]()

Esta fotode Autor desconocido está bajo licencia CC BY-SA

---

## Beneficios

**Eficiencia:**

Permite ejecutar pruebas de forma más rápida y repetitiva, liberando tiempo para que los testers se enfoquen en pruebas más complejas y exploratorias.

**Reducción de Costos:**

Disminuye los costos asociados con la ejecución manual de pruebas, liberando recursos humanos para tareas de mayor valor.

**Mejora en la Cobertura de Pruebas:**

Permite realizar pruebas más exhaustivas y frecuentes, aumentando la probabilidad de detectar errores tempranamente.

![image]()

---

## Beneficios

**Mejora en la Calidad del Software:**

Contribuye a la entrega de un software de mayor calidad, con menos errores y mayor confiabilidad.

**Integración Continua:**

Facilita la integración de las pruebas en el proceso de desarrollo, permitiendo la detección temprana de errores y una entrega más rápida de software.

![image]()

---

## Herramientas

**Selenium:**

Framework de código abierto para pruebas web, compatible con varios lenguajes de programación (Python, Java, C#).

**Appium:**

Herramienta para pruebas móviles multiplataforma, basada en Selenium, compatible con iOS y Android.

**Cucumber:**

Framework para pruebas de aceptación basado en Gherkin, facilita la creación de escenarios entendibles por personas no técnicas.

**Robot Framework:**

Framework de pruebas genérico basado en Python, permite automatizar pruebas en aplicaciones web, móviles, de escritorio y API.

![image]()

---

## Funciones

**Creación y Gestión de Casos de Prueba:**

Permiten crear, editar y organizar casos de prueba de manera eficiente.

**Ejecución de Casos de Prueba:**

Automatizan la ejecución de casos de prueba en diferentes entornos y navegadores.

**Registro y Análisis de Resultados:**

Registran resultados de pruebas y proporcionan herramientas para su análisis e interpretación.

**Generación de Informes:**

Generan informes detallados sobre resultados de pruebas, incluyendo métricas de cobertura y errores encontrados.

**Integración con Herramientas de Desarrollo Continuo:**

Se integran con herramientas de CI/CD para permitir la ejecución automatizada de pruebas durante el proceso de desarrollo.

![image]()

---

## Implementación y Gestión

**Selección de Herramienta Adecuada:**

Elegir la herramienta según necesidades específicas del proyecto, lenguaje preferido y presupuesto disponible.

**Definición del Alcance de las Pruebas:**

Determinar qué pruebas se automatizarán y cuáles se ejecutarán manualmente.

**Desarrollo de Scripts de Prueba:**

Crear scripts utilizando la herramienta elegida y siguiendo mejores prácticas de desarrollo de software.

![image]()

---

## Implementación y Gestión

**Integración con el Entorno de Desarrollo:**

Integrar las pruebas automatizadas en el entorno de desarrollo para permitir su ejecución continua.

**Mantenimiento de Scripts de Prueba:**

Mantener scripts actualizados a medida que el software evoluciona.

![image]()

---

## Planificación y Mantenimiento

**Creación de un Plan de Pruebas:**

Definir frecuencia de ejecución, criterios de aceptación y responsables de la ejecución.

**Monitoreo de Resultados:**

Monitorear resultados regularmente para identificar tendencias y posibles problemas.

**Mantenimiento de Scripts de Prueba:**

Mantener scripts actualizados para asegurar su precisión y efectividad.

![image]()

---

## Selección de herramientas

**Evaluar Necesidades del Proyecto:**

Considerar características requeridas, presupuesto, experiencia del equipo y compatibilidad con el entorno de desarrollo.

**Probar Diferentes Herramientas:**

Evaluar herramientas mediante pruebas piloto para determinar la más adecuada.

**Considerar la Escalabilidad:**

Elegir una herramienta que pueda escalar para satisfacer necesidades futuras.

![image]()

---

## Estrategia

**Definir Objetivos Claros:**

Establecer objetivos para la automatización, como reducir el tiempo de ejecución y mejorar la cobertura de pruebas.

**Priorizar Casos de Prueba:**

Priorizar casos de prueba según importancia, riesgo y valor comercial.

**Monitorear y Evaluar el Progreso:**

Supervisar el progreso de la automatización y evaluar su eficacia en función de los objetivos establecidos.

---

## Identificación y Documentación

**Registro Detallado:**

Incluir una descripción clara del defecto, pasos para reproducirlo, y su severidad y gravedad.

**Análisis de Defectos:**

Clasificar los defectos según su origen, frecuencia y tipo para identificar patrones y tendencias.

---

## Ventajas

![image]()

¡Felicitaciones por terminar este recurso!

---

---

## Unidad 2

Gherkin

* Testing Aplicado al Desarrollo

---

## ÍNDICE

* Ciclo de vida
* Identificación
* Registro
* Asignación
* Reproducción
* Análisis
* Corrección
* Cierre
* Pruebas

---

## Introducción

El ciclo de vida de un defecto en el desarrollo de software, destacando la importancia de su detección y resolución. Este ciclo incluye la identificación, corrección y verificación del defecto, asegurando la calidad y fiabilidad del software.

---

## Ciclo de Vida

![image]()

![image]()

---

Reporte:

- Durante las pruebas del software, un testeridentifica un defecto (bug o error), crucial para la calidad del producto final.

Registro:

- Se crea un registro detallado en un sistema especializado (bug tracker) con una descripción exhaustiva del comportamiento incorrecto, pasos para reproducir el problema, entorno donde ocurrió el error, y cualquier otro detalle relevante.

- Este registro facilita la comunicación clara entre testers y desarrolladores, asegurando que los problemas sean documentados de manera completa y precisa para su resolución oportuna.

* Reporte y Registro

---

Análisis:

- Un responsable técnico con experiencia realiza un análisis detallado para comprender la causa raíz del defecto.

- Se utilizan herramientas de depuración y técnicas de análisis de código para identificar no solo el síntoma visible del defecto, sino también las condiciones subyacentes que lo causan, con el fin de proporcionar una solución efectiva y duradera.

* Análisis y Priorización

---

Priorización:

- Tras el análisis técnico, se evalúa la gravedad del defecto y su impacto potencial en el producto final y los usuarios.

- Se utilizan categorías de priorización como crítico, alto, medio y bajo para clasificar la severidad del defecto.

- Otros factores considerados incluyen la frecuencia del error, el número de usuarios afectados, la criticidad de las funciones afectadas y cualquier requisito contractual o regulatorio.

- La priorización debe ser colaborativa e involucrar a diversas partes interesadas, incluyendo equipos de desarrollo, control de calidad y, en algunos casos, clientes o usuarios representativos.

Esta estrategia asegura la asignación óptima de recursos para abordar los defectos que tienen mayor impacto en la calidad y funcionalidad del software, promoviendo un proceso de desarrollo eficiente y centrado en la mejora continua.

* Análisis y Priorización

---

Asignación:

- Una vez analizado y priorizado un defecto, se asigna a un desarrollador específico para su corrección.

- La asignación se basa en criterios como la experiencia del desarrollador, carga de trabajo, urgencia del problema y disponibilidad de recursos.

- Es crucial que la asignación sea clara y transparente, comunicando todos los detalles relevantes del defecto al desarrollador.

* Asignación y Trabajo

---

Trabajo:

- El desarrollador revisa el código relevante para identificar y modificar las secciones específicas que causan el defecto.

- Dependiendo de la complejidad, puede ser necesario realizar cambios adicionales en otras partes del código.

- Durante la corrección, se aseguran prácticas recomendadas de desarrollo de software, como modularidad y legibilidad del código.

- Una vez corregido el defecto, se realizan pruebas exhaustivas para verificar que la corrección sea efectiva y que no se introduzcan nuevos problemas.

- Estas pruebas pueden incluir casos de prueba específicos y pruebas de regresión para validar el funcionamiento del software.

Este proceso garantiza que los defectos se aborden de manera efectiva, manteniendo la calidad y consistencia del software.

* Asignación y Trabajo

---

Corrección:

- Tras la asignación del defecto a un desarrollador, comienza el proceso de corrección para asegurar que el software funcione correctamente y cumpla con las expectativas de los usuarios.

- La corrección implica modificar o reparar el código afectado, guiado por la información del análisis del defecto.

- Se pueden realizar ajustes directos en el código fuente, refactorizaciones o añadir nuevas funciones para corregir el problema.

Prácticas de Desarrollo:

- Es fundamental que el desarrollador siga prácticas robustas de desarrollo y codificación, manteniendo la coherencia con la arquitectura del software, la legibilidad y la modularidaddel código.

* Corrección y Pruebas

---

Pruebas Unitarias:

- Verifican que la solución implementada resuelve el defecto sin introducir nuevos problemas.

- Pueden ser automatizadas y se enfocan en el comportamiento de componentes específicos.

- Las pruebas unitarias validan la funcionalidad aislada y detallada del software.

Casos de Prueba Específicos:

- Evalúanque la funcionalidad afectada por el defecto opere como se espera y que no se introduzcan errores nuevos.

- Estas pruebas aseguran la calidad del software y contribuyen a su mantenimiento futuro, identificando y resolviendo problemas de manera proactiva antes de que afecten a los usuarios.

Este proceso asegura que los defectos se corrijan de manera efectiva y que el software mantenga una alta calidad y fiabilidad.

* Corrección y Pruebas

---

Definición:

- Las pruebas de regresión aseguran la calidad del software después de una corrección o modificación, verificando que los cambios no afecten negativamente otras partes del sistema.

Importancia:

- Son esenciales para detectar cualquier regresión o deterioro en la calidad del software debido a la corrección de un defecto.

- Mitigan el riesgo de que los cambios realizados introduzcan nuevos errores en áreas no relacionadas del sistema.

* Pruebas de regresión

---

Estrategia:

- Se planifican y ejecutan meticulosamente después de cada ciclo de corrección o desarrollo de nuevas funcionalidades.

- Garantizan que todas las partes del software afectadas por los cambios recientes sean evaluadas exhaustivamente.

Enfoque Automatizado y Manual:

- Las pruebas de regresión suelen ser automatizadas para una ejecución rápida y repetible, mejorando la eficiencia y cobertura de pruebas.

- Sin embargo, el componente humano sigue siendo crucial para analizar casos complejos y no estándar, proporcionando feedbacky asegurando que el software mantenga su calidad y fiabilidad.

Este enfoque combinado asegura que el software funcione correctamente y mantenga su integridad después de cualquier cambio.

* Pruebas de regresión

---

Documentación de Defectos:

- Durante las pruebas, cualquier defecto se documenta detalladamente en un sistema de gestión de incidencias.

- La documentación incluye la naturaleza del problema, pasos para reproducirlo, impacto potencial y cualquier información relevante.

Pruebas de Regresión:

- Esenciales para mantener la estabilidad y fiabilidad del software tras cada cambio.

- Una estrategia combinada de pruebas automatizadas y manuales ayuda a mitigar riesgos y asegurar la integridad y funcionalidad del software.

* Resultados y Gestión

---

Validación y Verificación:

- Después de una corrección, se valida que la solución resuelva el problema sin introducir nuevos defectos.

- El testerreproduce el escenario original del defecto para confirmar su eliminación completa y verifica otros aspectos asociados con el defecto.

1. 4. Proceso de Verificación:

- Se asegura que la solución implementada no solo resuelva el problema superficialmente, sino que también considere el impacto más amplio del defecto en el software.

Este enfoque promueve una experiencia de usuario consistente y satisfecha, respaldada por un desarrollo de software disciplinado y centrado en la calidad.

* Resultados y Gestión

---

Cierre del Defecto:

Después de completar exitosamente la validación y verificación de la corrección de un defecto, el siguiente paso es marcar el defecto como cerrado en el sistema de seguimiento de errores. Este marcado representa un hito significativo en el ciclo de vida del desarrollo de software, indicando que el problema identificado ha sido completamente resuelto y que la funcionalidad afectada ahora opera correctamente según lo esperado.El proceso de cierre no solo implica la actualización del estado del defecto en el sistema de gestión de incidencias o bug tracker, sino también la documentación detallada de los resultados de las pruebas de validación y verificación. Esta documentación incluye información sobre las acciones tomadas para corregir el defecto, los resultados de las pruebas realizadas y cualquier observación relevante que pueda ser útil para futuras referencias o auditorías.

Cierre

---

Revisión Post-Implementación:

Tras el cierre de un defecto, es altamente recomendable realizar una revisión post-implementación o retrospectiva para analizar las lecciones aprendidas del incidente y explorar cómo mejorar los procesos para prevenir problemas similares en el futuro. Esta revisión no solo se enfoca en el defecto específico y su corrección, sino también en el contexto más amplio del proceso de desarrollo y las prácticas del equipo.

Durante la revisión post-implementación, se pueden abordar varios aspectos clave:

* Análisis de Causa Raíz: Identificar las causas subyacentes que contribuyeron al surgimiento del defecto. Esto puede involucrar factores como errores en el diseño, falta de pruebas adecuadas, comunicación insuficiente, entre otros.

Cierre

---

* **Efectividad de la Solución: Evaluar la efectividad de la solución implementada y si se abordaron completamente todos los aspectos del defecto.**También se puede considerar si hubo oportunidades para una solución más eficiente o robusta.
* Proceso de Corrección: Revisar el proceso utilizado para corregir el defecto, incluyendo la asignación, trabajo de desarrollo, pruebas y validación. Identificar áreas donde se podría mejorar la eficiencia o la calidad del trabajo realizado.
* Lecciones Aprendidas: Extraer lecciones útiles del incidente, como áreas de mejora en la comunicación dentro del equipo, la implementación de mejores prácticas de desarrollo de software, la actualización de la documentación de procedimientos, entre otros.
* Acciones Correctivas y Preventivas: Definir acciones concretas para corregir las deficiencias identificadas y prevenir la recurrencia de problemas similares en el futuro. Estas acciones pueden incluir la implementación de nuevos controles de calidad, la capacitación adicional del equipo, la mejora de herramientas de prueba, entre otras iniciativas.

Cierre

---

---

## Unidad 3

Defectos

* Testing Aplicado al Desarrollo

---

## ÍNDICE

* Introducción
* Historia
* Procesos
* Roles
* Mejores Prácticas
* Protocolos Estándar
* Ventas y Desvenajas
* Problemas Historicos

---

## Introducción

Los defectos en software, conocidos como bugs, han sido una preocupación desde los primeros días de la informática. La gestión de defectos es crucial para garantizar la seguridad y funcionalidad de los sistemas.

---

## Historia

• 1947: Grace Hopper popularizó el término “bug” tras descubrir una polilla en el ordenador Mark II en Harvard, causando un fallo.

• 1960s-1970s: La complejidad del software aumentó con el desarrollo de lenguajes de programación avanzados y sistemas operativos complejos, incrementando la frecuencia de defectos.

• 1980s: La explosión de la industria del software y la aparición de microcomputadoras llevaron a un aumento significativo en la producción de software, incrementando también la presencia de defectos debido a la rápida evolución tecnológica.

• 1990s: Con el auge de Internet y las aplicaciones web, los defectos adquirieron una dimensión crítica de seguridad, destacando la importancia de la ciberseguridad.

• 2000s-Presente: Las metodologías ágiles y DevOps han integrado la gestión de defectos en el ciclo de vida del desarrollo de software, utilizando herramientas automatizadas y técnicas avanzadas de pruebas para detectar y corregir bugs eficientemente. Sin embargo, la creciente complejidad del software asegura que los bugs sigan siendo un desafío persistente.

---

## Procesos

* Pruebas de Software:
* Se ejecutan diversas pruebas (unitarias, integración, sistema y aceptación) para detectar distintos tipos de defectos.
* Registro de Defectos:
* Los defectos identificados se registran en sistemas de seguimiento como JIRA o Bugzilla, incluyendo detalles sobre el comportamiento anómalo, pasos para reproducirlo, severidad y entorno del problema.
* Análisis y Priorización:
* Análisis de Causa Raíz (RCA): Se identifican y comprenden las razones fundamentales del defecto usando técnicas como diagramas de Ishikawa y los 5 Porqués.
* Priorización: Se priori zanlos defectos según su impacto y urgencia (crítico, mayor, menor), frecuencia y impacto potencial en usuarios finales o componentes del sistema.
* Corrección y Validación:
* Después de la priorización, los defectos se corrigen y validan para asegurar que se han solucionado adecuadamente y que no se introducen nuevos problemas.

---

## Roles

* Desarrolladores:
* Responsables de escribir y mantener el código del software, además de corregir defectos identificados durante pruebas y uso en producción.
* Testers/QA (Quality Assurance):
* Ejecutan pruebas para identificar defectos y verifican que las correcciones no introduzcan nuevos problemas, asegurando el cumplimiento de los estándares de calidad.
* Gerentes de Proyecto:
* Supervisan el progreso del proyecto y la gestión de defectos, planificando recursos y evaluando el impacto de los defectos en los objetivos del proyecto.
* Analistas de Negocios:
* Ayudan a priorizar defectos según su impacto en el negocio y en los usuarios, evaluando la severidad y riesgo de cada defecto.
* Usuarios Finales:
* Proporcionan retroalimentación sobre el software en producción y pueden identificar defectos no detectados durante las pruebas, mejorando la experiencia del usuario y la satisfacción del cliente.

---

## Mejores Prácticas

* Automatización de Pruebas:
* Utilizar herramientas automatizadas para ejecutar pruebas repetitivas de manera rápida y precisa, mejorando la eficiencia y cobertura de pruebas.
* Integración Continua/Entrega Continua (CI/CD):
* Implementar pipelines de CI/CD para automatizar la integración, prueba y entrega de código, facilitando la detección temprana de defectos y la entrega rápida de nuevas funcionalidades.
* Revisiones de Código:
* Realizar revisiones regulares de código entre pares o equipos para identificar posibles defectos antes de integrar cambios al repositorio principal, mejorando la calidad y consistencia del código.
* Pruebas de Seguridad:
* Incluir pruebas de seguridad en el proceso de desarrollo para identificar y mitigar vulnerabilidades, protegiendo la información sensible y manteniendo la confianza de los usuarios.

---

## Protocolos Estándar

* Ciclo de Vida de Desarrollo de Software (SDLC):
* Seguir un ciclo de vida estructurado como Agile o Waterfall, que incluya fases definidas de desarrollo, pruebas y validación para gestionar el proceso desde la concepción hasta la entrega y mantenimiento del software.
* Gestión de la Configuración:
* Mantener un control estricto sobre las versiones del software y sus cambios mediante prácticas de gestión de configuración, asegurando que todas las modificaciones sean controladas y documentadas para evitar conflictos y errores.
* Documentación:
* Documentar detalladamente los defectos y las soluciones implementadas para facilitar el análisis futuro, la identificación de patrones recurrentes y la mejora continua en el proceso de desarrollo.

Implementar estos métodos y protocolos estándar no solo mejora la eficiencia y calidad del software, sino que también fortalece la capacidad del equipo para responder a los desafíos del entorno tecnológico.

---

## Ventajas y Desventajas

Ventajas:

* Reducción de Costos: Identificar y corregir defectos en etapas tempranas del desarrollo minimiza los costos de reparación en fases posteriores y evita gastos adicionales.
* Mejora de la Calidad: Un enfoque sistemático en la gestión de defectos mejora la calidad general del software, asegurando que el producto final cumpla con los estándares esperados y proporcionando una mejor experiencia del usuario.
* Impacto Positivo:
* Seguridad Aumentada: Corregir defectos ayuda a reducir las vulnerabilidades de seguridad del software, protegiendo la integridad de los datos y la información confidencial de los usuarios.
* Confianza del Cliente: Un software con menos defectos inspira confianza en los clientes y usuarios finales, fortaleciendo la credibilidad y las relaciones a largo plazo.

---

## Ventajas y Desventajas

Desventajas:

* Costo Inicial: Implementar procesos y herramientas de gestión de defectos puede ser costoso inicialmente, incluyendo la adquisición de software y capacitación del personal.
* Requiere Recursos: La gestión efectiva de defectos demanda personal capacitado y tiempo dedicado, lo cual puede ser un desafío para equipos pequeños o con recursos limitados.
* Complejidad Adicional: La implementación de procesos de gestión de defectos puede agregar complejidad al flujo de trabajo, requiriendo una gestión cuidadosa para evitar ralentizar el desarrollo.

---

## Problemas Históricos

Ariane 5:

En 1996, el cohete Ariane 5 de la Agencia Espacial Europea explotó 40 segundos después de su lanzamiento debido a un error en el software de navegación. Un valor excedió el rango permitido, causando una excepción no manejada y la pérdida total del cohete y su carga útil, con un costo estimado en cientos de millones de dólares. Este incidente destaca la importancia de pruebas exhaustivas y gestión efectiva de excepciones en sistemas complejos.

Therac-25:

Entre 1985 y 1987, varios pacientes recibieron dosis letales de radiación durante tratamientos de radioterapia debido a errores en el software de la máquina Therac-25, permitiendo la activación inadvertida de dosis excesivas. Seis pacientes murieron como resultado directo. Este caso resalta las graves consecuencias de los defectos de software en aplicaciones críticas para la salud, subrayando la necesidad de prácticas robustas de desarrollo y pruebas.

---

---

 

**Rúbrica de evaluación 3 - Testing Aplicado al Desarrollo de Sistemas** 

| INDICADOR | Niveles de desempeño |  |  |  |
|---|---|---|---|---|
|  | 0%
Bajo | 60%
Medio | 80%
Alto | 100%
Sobresaliente |
| 5.1 Ejecuta casos de prueba
manualmente sobre el
software, verificando que los
resultados obtenidos coincidan
con los esperados según las
especificaciones. | No ejecuta casos de prueba manuales o los
realiza de forma improvisada, sin seguir el
plan, la matriz de pruebas ni los criterios
definidos. No compara resultados
esperados y obtenidos, no deja evidencia
verificable y no permite determinar el estado
real de la plataforma evaluada. | Ejecuta parcialmente casos de prueba
manuales asociados al sitio evaluado.
Registra algunos resultados y compara de
manera básica lo esperado con lo obtenido,
aunque presenta omisiones, inconsistencias
en la evidencia o cobertura limitada de flujos
críticos, casos de borde y prioridades
definidas. | Ejecuta los casos de prueba manuales de
acuerdo con el plan, la matriz de riesgos y la
priorización establecida. Registra resultados
aprobados y fallidos, adjunta evidencia
pertinente y valida con claridad la relación
entre especificación, resultado esperado y
resultado obtenido. | Ejecuta de manera rigurosa, ordenada y
trazable los casos de prueba manuales,
cubriendo rutas críticas, casos de borde y
escenarios de alto impacto para el negocio.
La evidencia es completa, verificable y
permite sustentar decisiones técnicas y
estratégicas para el socio formador. |
| Puntaje por indicador | 0 puntos | 9 puntos | 12 puntos | 15 puntos |

 

**Rúbrica de evaluación 3 - Testing Aplicado al Desarrollo de Sistemas** 

|  | Niveles de desempeño |  |  |  |
|---|---|---|---|---|
| INDICADOR | 0%
Bajo | 60% | 80%
Alto | 100%
Sobresaliente |
|  |  | Medio |  |  |
|  |  | Nota 4.0 |  |  |
| 5.2 Identifica de manera
precisa los errores encontrados
durante las pruebas manuales,
asegurando que estén
registrados de forma clara y
comprensible para su posterior
análisis y corrección. | No identifica errores relevantes o los
registra de forma confusa, incompleta o sin
evidencia. Los defectos no incluyen pasos
de reproducción, severidad, impacto,
resultado esperado, resultado obtenido ni
información suficiente para orientar su
análisis o corrección. | Identifica algunos errores durante las
pruebas manuales y los registra con
información básica. Los reportes incluyen
parte de los elementos solicitados, pero
presentan brechas en claridad, evidencia,
severidad, posible causa raíz o relación con
el impacto funcional, normativo o de
experiencia de usuario. | Identifica y documenta defectos de manera
clara, comprensible y útil para el análisis
posterior. Los bug reports incluyen pasos de
reproducción, evidencia, severidad,
prioridad, resultado esperado, resultado
obtenido y una hipótesis razonable de causa
raíz. | Identifica, clasifica y prioriza defectos con
alto rigor técnico. Los reportes son
accionables, incorporan evidencia sólida,
posible causa raíz, impacto en el negocio,
seguridad, usabilidad o cumplimiento
normativo, y se integran coherentemente en
una matriz de defectos priorizados. |
| Puntaje por indicador | 0 puntos | 12 puntos | 16 puntos | 20 puntos |

 

**Rúbrica de evaluación 3 - Testing Aplicado al Desarrollo de Sistemas** 

|  | Niveles de desempeño |  |  |  |
|---|---|---|---|---|
| INDICADOR | 0%
Bajo | 60% | 80%
Alto | 100%
Sobresaliente |
|  |  | Medio |  |  |
|  |  | Nota 4.0 |  |  |
| 5.3 Aplica técnicas de
exploración del software
eficazmente, descubriendo
posibles fallos que pudieran
haberse pasado por alto en los
casos de pruebas predefinidos. | No aplica técnicas de testing exploratorio o
lo realiza sin propósito, registro ni relación
con los riesgos del sistema. No descubre
fallos adicionales ni complementa los casos
de prueba predefinidos. | Aplica exploración básica en algunas
secciones del sitio, pero sin estrategia clara,
sesiones definidas ni criterios de
observación consistentes. Detecta hallazgos
aislados, con evidencia limitada y escasa
conexión con criticidad funcional, usabilidad,
rendimiento o seguridad. | Aplica técnicas de exploración del software
con foco en riesgos, rutas críticas, entradas
límite, comportamiento del usuario y
escenarios no cubiertos por los casos
predefinidos. Documenta hallazgos y los
relaciona con el plan de pruebas y la
priorización. | Ejecuta testing exploratorio de manera
sistemática y estratégica, usando
heurísticas, sesiones documentadas y
análisis de riesgo. Descubre fallos
relevantes no previstos, justifica su impacto
y propone ajustes concretos para mejorar la
cobertura y efectividad del proceso de QA. |
| Puntaje por indicador | 0 puntos | 9 puntos | 12 puntos | 15 puntos |

 

**Rúbrica de evaluación 3 - Testing Aplicado al Desarrollo de Sistemas** 

|  | Niveles de desempeño |  |  |  |
|---|---|---|---|---|
| INDICADOR | 0%
Bajo | 60% | 80%
Alto | 100%
Sobresaliente |
|  |  | Medio |  |  |
|  |  | Nota 4.0 |  |  |
| 6.1 Utiliza herramientas de
automatización de pruebas
para crear scripts que ejecuten
pruebas repetitivas sobre el
software, demostrando
comprensión del flujo de
trabajo y la sintaxis de la
herramienta. | No utiliza herramientas de automatización o
no logra crear scripts funcionales. No
demuestra comprensión del flujo de trabajo,
sintaxis, selectores, datos de prueba,
ejecución ni validación automática de
resultados. | Utiliza de forma básica una herramienta de
automatización y crea scripts simples o
prototipos con errores menores. La
automatización cubre pocos casos
repetitivos y evidencia comprensión inicial
del flujo, aunque con baja estabilidad,
documentación limitada o validaciones
incompletas. | Crea scripts de automatización funcionales
para pruebas repetitivas seleccionadas
desde la matriz de pruebas. Usa
adecuadamente la herramienta, estructura
los pasos, incorpora aserciones o
verificaciones y registra evidencia de
ejecución comprensible. | Diseña scripts de automatización
mantenibles, claros y reutilizables, alineados
con casos candidatos definidos por riesgo,
repetición y valor. Demuestra dominio del
flujo de trabajo, sintaxis, validaciones,
evidencia de ejecución y justificación técnica
de la herramienta utilizada. |
| Puntaje por indicador | 0 puntos | 9 puntos | 12 puntos | 15 puntos |

 

**Rúbrica de evaluación 3 - Testing Aplicado al Desarrollo de Sistemas** 

| INDICADOR | Niveles de desempeño |  |  |  |
|---|---|---|---|---|
|  | 0%
Bajo | 60%
Medio | 80%
Alto | 100%
Sobresaliente |
| 6.2 Integra eficazmente las
herramientas de
automatización de pruebas en
el proceso de desarrollo de
software, asegurando que los
resultados sean consistentes y
confiables en diferentes
entornos. | No integra herramientas de automatización
al proceso de testing o las usa de manera
aislada sin relación con el plan, los casos de
prueba, la matriz de riesgos ni los
resultados del proyecto. Los resultados no
son confiables ni repetibles. | Integra parcialmente la automatización en el
proceso de QA. La relación con el plan de
pruebas y los casos seleccionados es
básica, los resultados presentan
inconsistencias y no se demuestra con
claridad su confiabilidad en distintos
escenarios o entornos. | Integra herramientas de automatización en
el flujo de trabajo de QA, vinculando scripts,
casos de prueba, matriz de riesgos y
evidencia de resultados. Los resultados son
consistentes, repetibles y útiles para apoyar
la toma de decisiones del equipo. | Integra la automatización de manera
robusta y profesional dentro del ciclo de
aseguramiento de calidad, considerando
gestión de versiones, repetibilidad,
trazabilidad, distintos entornos y criterios de
confiabilidad. La integración fortalece la
eficiencia del proceso y aporta valor
estratégico al proyecto. |
| Puntaje por indicador | 0 puntos | 9 puntos | 12 puntos | 15 puntos |

 

**Rúbrica de evaluación 3 - Testing Aplicado al Desarrollo de Sistemas** 

| INDICADOR | Niveles de desempeño |  |  |  |
|---|---|---|---|---|
|  | 0%
Bajo | 60%
Medio | 80%
Alto | 100%
Sobresaliente |
| 6.3 Analiza los informes
generados por las
herramientas de
automatización de pruebas,
identificando tendencias,
patrones y áreas de mejora en
el software bajo prueba. | No analiza informes de automatización o se
limita a copiarlos sin interpretación. No
identifica tendencias, patrones, fallos
recurrentes, métricas relevantes ni áreas de
mejora del software bajo prueba. | Revisa informes de automatización de
manera básica e identifica algunos datos o
resultados aislados. El análisis es
descriptivo, con poca relación entre
métricas, patrones, defectos, riesgos y
recomendaciones de mejora para el sitio
evaluado. | Analiza informes y resultados de
automatización identificando tendencias,
patrones, fallos recurrentes y áreas de
mejora. Relaciona los hallazgos con
métricas, KPIs, priorización de defectos y
recomendaciones técnicas para mejorar
calidad, rendimiento o confiabilidad. | Interpreta informes de automatización con
enfoque técnico y ejecutivo, transformando
métricas y patrones en conclusiones
accionables. Prioriza mejoras según riesgo
e impacto, propone estrategia de
automatización futura, herramientas
pertinentes y justifica su valor mediante
KPIs o retorno esperado. |
| Puntaje por indicador | 0 puntos | 12 puntos | 16 puntos | 20 puntos |

# **Resumen de distribución de puntajes** 

|  | 0% Bajo |  | 80% Alto | 100% Sobresaliente |
|---|---|---|---|---|
| Indicador de logro |  | 60% Medio |  |  |
|  |  |  |  |  |
| 5.1 Ejecuta casos de prueba manualmente sobre el software,
verificando que los resultados obtenidos coincidan con los esperados
según las especificaciones. | 0 puntos | 9 puntos | 12 puntos | 15 puntos |
| 5.2 Identifica de manera precisa los errores encontrados durante las
pruebas manuales, asegurando que estén registrados de forma clara y
comprensible para su posterior análisis y corrección. | 0 puntos | 12 puntos | 16 puntos | 20 puntos |
| 5.3 Aplica técnicas de exploración del software eficazmente,
descubriendo posibles fallos que pudieran haberse pasado por alto en
los casos de pruebas predefinidos. | 0 puntos | 9 puntos | 12 puntos | 15 puntos |
| 6.1 Utiliza herramientas de automatización de pruebas para crear
scripts que ejecuten pruebas repetitivas sobre el software,
demostrando comprensión del flujo de trabajo y la sintaxis de la
herramienta. | 0 puntos | 9 puntos | 12 puntos | 15 puntos |
| 6.2 Integra eficazmente las herramientas de automatización de
pruebas en el proceso de desarrollo de software, asegurando que los
resultados sean consistentes y confiables en diferentes entornos. | 0 puntos | 9 puntos | 12 puntos | 15 puntos |
| 6.3 Analiza los informes generados por las herramientas de
automatización de pruebas, identificando tendencias, patrones y áreas
de mejora en el software bajo prueba. | 0 puntos | 12 puntos | 16 puntos | 20 puntos |
| Total por nivel de desempeño | 0 puntos |  | 80 puntos | 100 puntos |
|  |  | 60 puntos |  |  |
|  |  |  |  |  |
|  |  |  |  |  |

 

---

## Aplicación y Automatización de Pruebas en el Desarrollo de Software

* Sesión sincrónica

---

## ÍNDICE

* Tema 1:**mapa conceptual**
* Tema 2:**retroalimentaciónpreguntas del apunte**
* Tema 3:**retroalimentación preguntas del foro**
* Tema 4:**Taller**

---

## Resumen unidad

![image]()

---

## Resumen unidad

![image]()

---

## Fase de retroalimentación

---

## Apunte activador de aprendizaje

* ¿Cómo podría beneficiar la integración continua (CI) y la entrega continua (CD) en la detección y corrección rápida de defectos en un proyecto de desarrollo de software?
* ¿Quién fue la persona que popularizó el término "bug" en el contexto informático en 1947?
* ¿Cuáles son los tipos principales de pruebas de software utilizadas para identificar defectos y en qué etapas del desarrollo se aplican?
* Compara el ciclo de vida de un defecto en metodologías Agile versus Waterfall. ¿En qué aspectos difieren y cómo influye esto en la gestión de defectos?
* ¿Cómo definirías la fase de "Análisis" dentro del ciclo de vida de un defecto? ¿Cuál es su propósito principal en el proceso de desarrollo de software?
* Mencione un ejemplo de un error que se puede detectar con mayor facilidad mediante pruebas manuales que con pruebas automatizadas.
* "La primera etapa del proceso de aplicación de las pruebas manuales es la ejecución de los casos de prueba." (Verdadero o Falso)

---

## Foro crítico reflexivo

1. ***1.	En tu experiencia, ¿cuáles son los desafíos más comunes que enfrentas al ejecutar casos de prueba manualmente y cómo los superas?***
2. ***2.	Cuando encuentras un error durante una prueba manual, ¿qué criterios sigues para asegurar que tu registro sea claro y útil para el equipo de desarrollo?***
3. ***3.	Discute una situación en la que aplicar técnicas de exploración del software te permitió descubrir un fallo crítico. ¿Qué pasos seguiste y qué impacto tuvo en el proyecto?***

---

## Foro crítico reflexivo - Respuesta

1. ***1.   En tu experiencia, ¿cuáles son los desafíos más comunes que enfrentas al ejecutar casos de prueba manualmente y cómo los superas?***

***Respuesta:***

***Uno de los desafíos más comunes al ejecutar casos de prueba manualmente es la repetitividad y el tedio que pueden llevar a errores humanos, como la omisión de pasos importantes o la falta de atención a detalles críticos. Otro desafío es la limitación en el alcance de las pruebas debido a la cantidad de tiempo disponible, lo que puede llevar a una cobertura de pruebas insuficiente. Para superar estos desafíos, adopto un enfoque sistemático, utilizando listas de verificación y guías detalladas para asegurarme de que sigo todos los pasos correctamente. Además, divido las sesiones de prueba en bloques más pequeños con descansos intermedios para mantener la concentración. También priorizo los casos de prueba según su criticidad, asegurando que las funcionalidades más importantes sean probadas exhaustivamente.***

---

## Foro crítico reflexivo - Respuesta

1. ***2.   Cuando encuentras un error durante una prueba manual, ¿qué criterios sigues para asegurar que tu registro sea claro y útil para el equipo de desarrollo?***

***Respuesta:***

***Al registrar un error, sigo varios criterios para asegurar que la documentación sea clara y útil. Primero, describo el error de manera detallada, incluyendo el comportamiento esperado y el comportamiento real observado. A continuación, especifico los pasos exactos para reproducir el error, lo que incluye datos de entrada, configuraciones específicas del entorno, y cualquier acción previa que pudiera haber influido en el comportamiento. También indico la gravedad del error y su impacto en el sistema, lo que ayuda al equipo de desarrollo a priorizar su resolución. Finalmente, adjunto capturas de pantalla, logs, o cualquier otra evidencia que pueda facilitar la comprensión del problema.***

---

## Foro crítico reflexivo - Respuesta

1. ***3.   Discute una situación en la que aplicar técnicas de exploración del software te permitió descubrir un fallo crítico. ¿Qué pasos seguiste y qué impacto tuvo en el proyecto?***

***Respuesta:***

***En una ocasión, durante la fase de pruebas de una aplicación de comercio electrónico, apliqué técnicas de exploración para verificar la funcionalidad de pago en un entorno que no estaba cubierto por los casos de prueba predefinidos. Decidí probar diferentes combinaciones de métodos de pago y tipos de productos, y descubrí que al seleccionar una opción de pago específico en combinación con un tipo de descuento, la aplicación permitía que la transacción se completara sin aplicar el descuento correctamente, lo que resultaba en un cobro incorrecto al cliente.***

---

## Taller colaborativo

---

## Desarrollo del mini problema

Un equipo de desarrollo ha lanzado la primera versión de una aplicación de gestión de tareas que permite a los usuarios crear, editar, eliminar y organizar sus tareas diarias. Antes de la implementación final, se requiere una fase de pruebas manuales para garantizar que todas las funcionalidades básicas funcionan correctamente.

---

## Desarrollo del mini problema

Indicadores de Logro:

1. 1. Ejecuta casos de prueba manualmente sobre el software, verificando que los resultados obtenidos coincidan con los esperados según las especificaciones.

Caso de Prueba:

- Escenario: Crear una nueva tarea.

- Acciones: El testeringresa el título "Comprar leche" en el campo de tareas y hace clic en "Guardar".

- Resultado Esperado: La tarea "Comprar leche" aparece en la lista de tareas pendientes.

- Resultado Obtenido: La tarea se guarda correctamente y aparece en la lista, coincidiendo con las especificaciones del caso de prueba.

- Respuesta: El resultado del caso de prueba coincide con las especificaciones, lo que indica que la funcionalidad para crear tareas está funcionando correctamente.

---

## Desarrollo del mini problema

1. 2. Identifica de manera precisa los errores encontrados durante las pruebas manuales, asegurando que estén registrados de forma clara y comprensible para su posterior análisis y corrección.

Detección de Error:

- Escenario: Editar una tarea existente.

- Acciones: El testerselecciona la tarea "Comprar leche", la edita cambiando el título a "Comprar leche y pan", y guarda los cambios.

- Error Detectado: Al guardar, la aplicación genera un error y no actualiza la tarea en la lista.

- Registro del Error: "Error al editar la tarea. Al intentar cambiar el título de 'Comprar leche' a 'Comprar leche y pan', la aplicación genera un mensaje de error 'NullReferenceException' y no guarda los cambios."

- Respuesta: El error fue identificado y registrado claramente, lo que permitirá al equipo de desarrollo comprender el problema y aplicar la corrección necesaria.

---

## Desarrollo del mini problema

1. 3. Aplica técnicas de exploración del software eficazmente, descubriendo posibles fallos que pudieran haberse pasado por alto en los casos de pruebas predefinidos.

Exploración del Software:

- Acción: El tester, al explorar la aplicación, decide probar la funcionalidad de ordenamiento de tareas.

- Descubrimiento del Fallo: Al intentar ordenar las tareas por fecha de creación, el testerdescubre que la aplicación no responde y se cierra inesperadamente.

- Registro del Fallo: "Error crítico en la función de ordenamiento. La aplicación se cierra inesperadamente cuando el usuario intenta ordenar las tareas por fecha de creación."

- Respuesta: La técnica de exploración permitió descubrir un fallo crítico que no estaba cubierto en los casos de prueba predefinidos, demostrando la importancia de explorar el software para encontrar posibles errores ocultos.

Conclusión:

En este mini caso, el testerha demostrado habilidad en la ejecución de pruebas manuales, en la identificación y registro preciso de errores, y en la aplicación efectiva de técnicas de exploración. Estos esfuerzos contribuyen a asegurar la calidad del software antes de su lanzamiento al mercado.

---