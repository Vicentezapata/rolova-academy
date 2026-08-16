

# ===== Presentación - Automatización pt2.pptx =====


## Slide 1
- Planificación y Selección de Pruebas en el Desarrollo de Software
- Automatización de Pruebas y CI/CD

## Slide 2
- ¿Qué veremos hoy en este módulo?
- Introducción a la Automatización de Pruebas
- Fundamentos de la Automatización de Pruebas
- Tipos de Pruebas Automatizadas
- Herramientas para la Automatización de pruebas
- Frameworks de Automatización de Pruebas

## Slide 3
- Introducción

## Slide 4
- La automatización de pruebas es fundamental en el desarrollo moderno de software, permitiendo validación continua y eficiente. Utiliza herramientas y scripts para ejecutar pruebas automáticamente, mejorando la eficiencia y precisión. Históricamente, se desarrolló para reducir el tiempo y esfuerzo de las pruebas manuales. Las herramientas han avanzado, integrándose con métodos de entrega continua y ágiles. Las principales ventajas son la reducción de tiempo y la consistencia de los resultados, aunque presenta desafíos como el mantenimiento de scripts. En resumen, es esencial para asegurar la calidad del software en un entorno ágil.

## Slide 5
- Fundamentos de la Automatización de Pruebas

## Slide 6
- La automatización de pruebas ha avanzado desde los años 1980, impulsada por la complejidad del software y la necesidad de eficiencia.
- Años 1980: Aparecen herramientas rudimentarias, específicas para ciertos lenguajes, reduciendo el tiempo y esfuerzo de pruebas manuales.
- Años 1990: Se producen avances tecnológicos que mejoran las herramientas de automatización, como el desarrollo ágil. Herramientas comerciales como WinRunner ganan popularidad, estableciendo estándares.
- Años 2000: Se da una expansión significativa con herramientas como Selenium y QTP, mejorando la integración con metodologías de entrega continua (CI/CD) y aumentando la flexibilidad y eficiencia de las pruebas.
- Historia

## Slide 7
- Definición
- La automatización de pruebas utiliza herramientas y scripts para ejecutar pruebas de software automáticamente, simulando interacciones del usuario y verificando resultados. Abarca diversos tipos de pruebas (funcionales, regresión, carga, rendimiento) y genera informes detallados para identificar y corregir errores. Estas herramientas son flexibles y escalables, integrándose con sistemas de integración continua (CI/CD) para asegurar la estabilidad y funcionalidad del software durante su ciclo de vida.

## Slide 8
- Propósito
- La automatización de pruebas aumenta la eficiencia y efectividad del proceso de pruebas de software al permitir la ejecución rápida y exhaustiva de numerosos casos de prueba, reduciendo costos y tiempos. Libera a los testers de tareas repetitivas, mejorando su productividad y la calidad del software. Además, garantiza una mayor cobertura y consistencia en las pruebas, asegurando que todas las partes del software sean probadas exhaustivamente, incluyendo integraciones y detección de errores. Es crucial en el desarrollo moderno de software, permitiendo validación continua y mejor calidad en menos tiempo.

## Slide 9
- Proceso

## Slide 10
- Ciclo de Vida

## Slide 11
- Roles
- El proceso de automatización de pruebas involucra a diversos roles clave:
- - Automatizadores de Pruebas: Especialistas en la creación y mantenimiento de scripts de automatización. Diseñan, implementan, ejecutan y mantienen los scripts para asegurar su efectividad a lo largo del tiempo.
- - Desarrolladores de Software: Colaboran con los automatizadores para integrar las pruebas automatizadas en el ciclo de desarrollo, proporcionando información sobre nuevas funcionalidades y corrigiendo errores detectados. Ayudan a escribir y mantener scripts, especialmente en entornos ágiles con integración continua.
- - Analistas de Calidad (QA): Revisan los resultados de las pruebas automatizadas y realizan pruebas manuales complementarias. Aseguran que los casos de prueba cubran todas las funcionalidades críticas y los resultados sean precisos. Identifican áreas que requieren pruebas manuales detalladas cuando la automatización no es viable.

## Slide 12
- Mejores Prácticas
- Para maximizar la efectividad de la automatización de pruebas, se deben seguir buenas prácticas:
- - Selección de Casos de Prueba: Elegir casos repetitivos, críticos y con alta frecuencia de errores humanos para la automatización. Priorizar pruebas de funcionalidades críticas del sistema.
- - Modularidad y Reusabilidad: Escribir scripts modulares y reutilizables para facilitar mantenimiento y expansión. Reutilizar componentes en múltiples pruebas ahorra tiempo y esfuerzo, mejorando la claridad y organización del código.
- - Mantenimiento Regular: Actualizar y mantener scripts regularmente para adaptarse a cambios en la aplicación, reflejar nuevas funcionalidades, corregir errores y asegurar precisión y efectividad de las pruebas.

## Slide 13
- Protocolos
- La implementación de protocolos estándar es crucial para integrar la automatización de pruebas en el desarrollo de software, asegurando que las pruebas se ejecuten consistentemente y proporcionando validación continua.
- Integración Continua (CI): Integra pruebas automatizadas en el proceso de CI para ejecutar pruebas en cada cambio de código, permitiendo la detección temprana de errores y mejorando la estabilidad y calidad del software. Herramientas como Jenkins, CircleCI y Travis CI son comunes.
- Desarrollo Continuo (CD): Usa la automatización en pipelines de CD para garantizar calidad en el despliegue. Las pruebas automatizadas son obligatorias antes de desplegar en producción, asegurando que solo el software que pasa todas las pruebas se despliega, reduciendo riesgos y mejorando la confiabilidad.
- La colaboración entre automatizadores de pruebas, desarrolladores y analistas de calidad, junto con la aplicación de mejores prácticas y mantenimiento regular, asegura una validación continua y eficiente del software.

## Slide 14
- Ventajas y Desventajas

## Slide 15
- Tipos de Pruebas Automatizadas

## Slide 16
- Historia

## Slide 17
- Procesos y Pruebas

## Slide 18
- Roles

## Slide 19
- Mejores prácticas

## Slide 20
- Protocolos

## Slide 21
- Herramientas para la Automatización de pruebas

## Slide 22
- Herramientas

## Slide 23
- Frameworks de Automatización de Pruebas

## Slide 24
- La automatización de pruebas ha evolucionado significativamente desde la década de 1990, impulsada por frameworks robustos que facilitan la creación, ejecución y mantenimiento de pruebas automatizadas.
- Años 1990: Surgieron los primeros frameworks como JUnit, desarrollado por Kent Beck y Erich Gamma, estandarizando las pruebas unitarias automatizadas y permitiendo la verificación de pequeñas unidades de código de manera repetible y automatizada.
- Años 2000: La automatización de pruebas se diversificó con herramientas como Selenium en 2004, que permitieron la interacción avanzada con navegadores web y pruebas de regresión, mejorando la flexibilidad y compatibilidad con múltiples lenguajes de programación. También se introdujo el Page Object Pattern, facilitando la creación y mantenimiento de pruebas automatizadas.
- Historia

## Slide 25
- Proceso

## Slide 26
- Mejores prácticas


# ===== Presentación Automatizacion.pptx =====


## Slide 1
- Unidad 3
- Automatización
- Testing Aplicado al Desarrollo

## Slide 2
- ÍNDICE
- Introducción
- Beneficios
- Herramientas
- Funciones
- Implementación y Gestión
- Planificación y Mantenimiento
- Seleccipon de Herramientas
- Estrategia
- Identificación y Documentación

## Slide 3
- Introducción
- La automatización de pruebas emerge como una herramienta revolucionaria, transformando el panorama de la evaluación de software. Al delegar tareas repetitivas a scripts y herramientas automatizadas, los desarrolladores y testers pueden enfocarse en aspectos más estratégicos y creativos, optimizando así el tiempo y los recursos disponibles.

## Slide 4
- Definición
- La automatización de pruebas es el proceso de ejecutar pruebas de software automáticamente utilizando herramientas y scripts predefinidos, simulando la interacción humana con el software.
- Esta foto de Autor desconocido está bajo licencia CC BY-SA

## Slide 5
- Eficiencia:
- Permite ejecutar pruebas de forma más rápida y repetitiva, liberando tiempo para que los testers se enfoquen en pruebas más complejas y exploratorias.
- Reducción de Costos:
- Disminuye los costos asociados con la ejecución manual de pruebas, liberando recursos humanos para tareas de mayor valor.
- Mejora en la Cobertura de Pruebas:
- Permite realizar pruebas más exhaustivas y frecuentes, aumentando la probabilidad de detectar errores tempranamente.
- Beneficios

## Slide 6
- Mejora en la Calidad del Software:
- Contribuye a la entrega de un software de mayor calidad, con menos errores y mayor confiabilidad.
- Integración Continua:
- Facilita la integración de las pruebas en el proceso de desarrollo, permitiendo la detección temprana de errores y una entrega más rápida de software.
- Beneficios

## Slide 7
- Selenium:
- Framework de código abierto para pruebas web, compatible con varios lenguajes de programación (Python, Java, C#).
- Appium:
- Herramienta para pruebas móviles multiplataforma, basada en Selenium, compatible con iOS y Android.
- Cucumber:
- Framework para pruebas de aceptación basado en Gherkin, facilita la creación de escenarios entendibles por personas no técnicas.
- Robot Framework:
- Framework de pruebas genérico basado en Python, permite automatizar pruebas en aplicaciones web, móviles, de escritorio y API.
- Herramientas

## Slide 8
- Creación y Gestión de Casos de Prueba:
- Permiten crear, editar y organizar casos de prueba de manera eficiente.
- Ejecución de Casos de Prueba:
- Automatizan la ejecución de casos de prueba en diferentes entornos y navegadores.
- Registro y Análisis de Resultados:
- Registran resultados de pruebas y proporcionan herramientas para su análisis e interpretación.
- Generación de Informes:
- Generan informes detallados sobre resultados de pruebas, incluyendo métricas de cobertura y errores encontrados.
- Integración con Herramientas de Desarrollo Continuo:
- Se integran con herramientas de CI/CD para permitir la ejecución automatizada de pruebas durante el proceso de desarrollo.
- Funciones

## Slide 9
- Selección de Herramienta Adecuada:
- Elegir la herramienta según necesidades específicas del proyecto, lenguaje preferido y presupuesto disponible.
- Definición del Alcance de las Pruebas:
- Determinar qué pruebas se automatizarán y cuáles se ejecutarán manualmente.
- Desarrollo de Scripts de Prueba:
- Crear scripts utilizando la herramienta elegida y siguiendo mejores prácticas de desarrollo de software.
- Implementación y Gestión

## Slide 10
- Integración con el Entorno de Desarrollo:
- Integrar las pruebas automatizadas en el entorno de desarrollo para permitir su ejecución continua.
- Mantenimiento de Scripts de Prueba:
- Mantener scripts actualizados a medida que el software evoluciona.
- Implementación y Gestión

## Slide 11
- Creación de un Plan de Pruebas:
- Definir frecuencia de ejecución, criterios de aceptación y responsables de la ejecución.
- Monitoreo de Resultados:
- Monitorear resultados regularmente para identificar tendencias y posibles problemas.
- Mantenimiento de Scripts de Prueba:
- Mantener scripts actualizados para asegurar su precisión y efectividad.
- Planificación y Mantenimiento

## Slide 12
- Evaluar Necesidades del Proyecto:
- Considerar características requeridas, presupuesto, experiencia del equipo y compatibilidad con el entorno de desarrollo.
- Probar Diferentes Herramientas:
- Evaluar herramientas mediante pruebas piloto para determinar la más adecuada.
- Considerar la Escalabilidad:
- Elegir una herramienta que pueda escalar para satisfacer necesidades futuras.
- Selección de herramientas

## Slide 13
- Definir Objetivos Claros:
- Establecer objetivos para la automatización, como reducir el tiempo de ejecución y mejorar la cobertura de pruebas.
- Priorizar Casos de Prueba:
- Priorizar casos de prueba según importancia, riesgo y valor comercial.
- Monitorear y Evaluar el Progreso:
- Supervisar el progreso de la automatización y evaluar su eficacia en función de los objetivos establecidos.
- Estrategia

## Slide 14
- Registro Detallado:
- Incluir una descripción clara del defecto, pasos para reproducirlo, y su severidad y gravedad.
- Identificación y Documentación
- Análisis de Defectos:
- Clasificar los defectos según su origen, frecuencia y tipo para identificar patrones y tendencias.

## Slide 15
- Ventajas
- ¡Felicitaciones por terminar este recurso!


# ===== Presentación Ciclo de Vida.pptx =====


## Slide 1
- Unidad 2
- Gherkin
- Testing Aplicado al Desarrollo

## Slide 2
- ÍNDICE
- Ciclo de vida
- Identificación
- Registro
- Asignación
- Reproducción
- Análisis
- Corrección
- Cierre
- Pruebas

## Slide 3
- Introducción
- El ciclo de vida de un defecto en el desarrollo de software, destacando la importancia de su detección y resolución. Este ciclo incluye la identificación, corrección y verificación del defecto, asegurando la calidad y fiabilidad del software.

## Slide 4
- Ciclo de Vida

## Slide 5
- Reporte:
- - Durante las pruebas del software, un tester identifica un defecto (bug o error), crucial para la calidad del producto final.
- Registro:
- - Se crea un registro detallado en un sistema especializado (bug tracker) con una descripción exhaustiva del comportamiento incorrecto, pasos para reproducir el problema, entorno donde ocurrió el error, y cualquier otro detalle relevante.
- - Este registro facilita la comunicación clara entre testers y desarrolladores, asegurando que los problemas sean documentados de manera completa y precisa para su resolución oportuna.
- Reporte y Registro

## Slide 6
- Análisis:
- - Un responsable técnico con experiencia realiza un análisis detallado para comprender la causa raíz del defecto.
- - Se utilizan herramientas de depuración y técnicas de análisis de código para identificar no solo el síntoma visible del defecto, sino también las condiciones subyacentes que lo causan, con el fin de proporcionar una solución efectiva y duradera.
- Análisis y Priorización

## Slide 7
- Priorización:
- - Tras el análisis técnico, se evalúa la gravedad del defecto y su impacto potencial en el producto final y los usuarios.
- - Se utilizan categorías de priorización como crítico, alto, medio y bajo para clasificar la severidad del defecto.
- - Otros factores considerados incluyen la frecuencia del error, el número de usuarios afectados, la criticidad de las funciones afectadas y cualquier requisito contractual o regulatorio.
- - La priorización debe ser colaborativa e involucrar a diversas partes interesadas, incluyendo equipos de desarrollo, control de calidad y, en algunos casos, clientes o usuarios representativos.
- Esta estrategia asegura la asignación óptima de recursos para abordar los defectos que tienen mayor impacto en la calidad y funcionalidad del software, promoviendo un proceso de desarrollo eficiente y centrado en la mejora continua.
- Análisis y Priorización

## Slide 8
- Asignación:
- - Una vez analizado y priorizado un defecto, se asigna a un desarrollador específico para su corrección.
- - La asignación se basa en criterios como la experiencia del desarrollador, carga de trabajo, urgencia del problema y disponibilidad de recursos.
- - Es crucial que la asignación sea clara y transparente, comunicando todos los detalles relevantes del defecto al desarrollador.
- Asignación y Trabajo

## Slide 9
- Trabajo:
- - El desarrollador revisa el código relevante para identificar y modificar las secciones específicas que causan el defecto.
- - Dependiendo de la complejidad, puede ser necesario realizar cambios adicionales en otras partes del código.
- - Durante la corrección, se aseguran prácticas recomendadas de desarrollo de software, como modularidad y legibilidad del código.
- - Una vez corregido el defecto, se realizan pruebas exhaustivas para verificar que la corrección sea efectiva y que no se introduzcan nuevos problemas.
- - Estas pruebas pueden incluir casos de prueba específicos y pruebas de regresión para validar el funcionamiento del software.
- Este proceso garantiza que los defectos se aborden de manera efectiva, manteniendo la calidad y consistencia del software.
- Asignación y Trabajo

## Slide 10
- Corrección:
- - Tras la asignación del defecto a un desarrollador, comienza el proceso de corrección para asegurar que el software funcione correctamente y cumpla con las expectativas de los usuarios.
- - La corrección implica modificar o reparar el código afectado, guiado por la información del análisis del defecto.
- - Se pueden realizar ajustes directos en el código fuente, refactorizaciones o añadir nuevas funciones para corregir el problema.
- Prácticas de Desarrollo:
- - Es fundamental que el desarrollador siga prácticas robustas de desarrollo y codificación, manteniendo la coherencia con la arquitectura del software, la legibilidad y la modularidad del código.
- Corrección y Pruebas

## Slide 11
- Pruebas Unitarias:
- - Verifican que la solución implementada resuelve el defecto sin introducir nuevos problemas.
- - Pueden ser automatizadas y se enfocan en el comportamiento de componentes específicos.
- - Las pruebas unitarias validan la funcionalidad aislada y detallada del software.
- Casos de Prueba Específicos:
- - Evalúan que la funcionalidad afectada por el defecto opere como se espera y que no se introduzcan errores nuevos.
- - Estas pruebas aseguran la calidad del software y contribuyen a su mantenimiento futuro, identificando y resolviendo problemas de manera proactiva antes de que afecten a los usuarios.
- Este proceso asegura que los defectos se corrijan de manera efectiva y que el software mantenga una alta calidad y fiabilidad.
- Corrección y Pruebas

## Slide 12
- Definición:
- - Las pruebas de regresión aseguran la calidad del software después de una corrección o modificación, verificando que los cambios no afecten negativamente otras partes del sistema.
- Importancia:
- - Son esenciales para detectar cualquier regresión o deterioro en la calidad del software debido a la corrección de un defecto.
- - Mitigan el riesgo de que los cambios realizados introduzcan nuevos errores en áreas no relacionadas del sistema.
- Pruebas de regresión

## Slide 13
- Estrategia:
- - Se planifican y ejecutan meticulosamente después de cada ciclo de corrección o desarrollo de nuevas funcionalidades.
- - Garantizan que todas las partes del software afectadas por los cambios recientes sean evaluadas exhaustivamente.
- Enfoque Automatizado y Manual:
- - Las pruebas de regresión suelen ser automatizadas para una ejecución rápida y repetible, mejorando la eficiencia y cobertura de pruebas.
- - Sin embargo, el componente humano sigue siendo crucial para analizar casos complejos y no estándar, proporcionando feedback y asegurando que el software mantenga su calidad y fiabilidad.
- Este enfoque combinado asegura que el software funcione correctamente y mantenga su integridad después de cualquier cambio.
- Pruebas de regresión

## Slide 14
- Documentación de Defectos:
- - Durante las pruebas, cualquier defecto se documenta detalladamente en un sistema de gestión de incidencias.
- - La documentación incluye la naturaleza del problema, pasos para reproducirlo, impacto potencial y cualquier información relevante.
- Pruebas de Regresión:
- - Esenciales para mantener la estabilidad y fiabilidad del software tras cada cambio.
- - Una estrategia combinada de pruebas automatizadas y manuales ayuda a mitigar riesgos y asegurar la integridad y funcionalidad del software.
- Resultados y Gestión

## Slide 15
- Validación y Verificación:
- - Después de una corrección, se valida que la solución resuelva el problema sin introducir nuevos defectos.
- - El tester reproduce el escenario original del defecto para confirmar su eliminación completa y verifica otros aspectos asociados con el defecto.
- 4. Proceso de Verificación:
- - Se asegura que la solución implementada no solo resuelva el problema superficialmente, sino que también considere el impacto más amplio del defecto en el software.
- Este enfoque promueve una experiencia de usuario consistente y satisfecha, respaldada por un desarrollo de software disciplinado y centrado en la calidad.
- Resultados y Gestión

## Slide 16
- Cierre del Defecto:
- Después de completar exitosamente la validación y verificación de la corrección de un defecto, el siguiente paso es marcar el defecto como cerrado en el sistema de seguimiento de errores. Este marcado representa un hito significativo en el ciclo de vida del desarrollo de software, indicando que el problema identificado ha sido completamente resuelto y que la funcionalidad afectada ahora opera correctamente según lo esperado. El proceso de cierre no solo implica la actualización del estado del defecto en el sistema de gestión de incidencias o bug tracker, sino también la documentación detallada de los resultados de las pruebas de validación y verificación. Esta documentación incluye información sobre las acciones tomadas para corregir el defecto, los resultados de las pruebas realizadas y cualquier observación relevante que pueda ser útil para futuras referencias o auditorías.
- Cierre

## Slide 17
- Revisión Post-Implementación:
- Tras el cierre de un defecto, es altamente recomendable realizar una revisión post-implementación o retrospectiva para analizar las lecciones aprendidas del incidente y explorar cómo mejorar los procesos para prevenir problemas similares en el futuro. Esta revisión no solo se enfoca en el defecto específico y su corrección, sino también en el contexto más amplio del proceso de desarrollo y las prácticas del equipo.
- Durante la revisión post-implementación, se pueden abordar varios aspectos clave:
- Análisis de Causa Raíz: Identificar las causas subyacentes que contribuyeron al surgimiento del defecto. Esto puede involucrar factores como errores en el diseño, falta de pruebas adecuadas, comunicación insuficiente, entre otros.
- Cierre

## Slide 18
- Efectividad de la Solución: Evaluar la efectividad de la solución implementada y si se abordaron completamente todos los aspectos del defecto. También se puede considerar si hubo oportunidades para una solución más eficiente o robusta.
- Proceso de Corrección: Revisar el proceso utilizado para corregir el defecto, incluyendo la asignación, trabajo de desarrollo, pruebas y validación. Identificar áreas donde se podría mejorar la eficiencia o la calidad del trabajo realizado.
- Lecciones Aprendidas: Extraer lecciones útiles del incidente, como áreas de mejora en la comunicación dentro del equipo, la implementación de mejores prácticas de desarrollo de software, la actualización de la documentación de procedimientos, entre otros.
- Acciones Correctivas y Preventivas: Definir acciones concretas para corregir las deficiencias identificadas y prevenir la recurrencia de problemas similares en el futuro. Estas acciones pueden incluir la implementación de nuevos controles de calidad, la capacitación adicional del equipo, la mejora de herramientas de prueba, entre otras iniciativas.
- Cierre


# ===== Presentación Defectos.pptx =====


## Slide 1
- Unidad 3
- Defectos
- Testing Aplicado al Desarrollo

## Slide 2
- ÍNDICE
- Introducción
- Historia
- Procesos
- Roles
- Mejores Prácticas
- Protocolos Estándar
- Ventas y Desvenajas
- Problemas Historicos

## Slide 3
- Introducción
- Los defectos en software, conocidos como bugs, han sido una preocupación desde los primeros días de la informática. La gestión de defectos es crucial para garantizar la seguridad y funcionalidad de los sistemas.

## Slide 4
- Historia
- • 1947: Grace Hopper popularizó el término “bug” tras descubrir una polilla en el ordenador Mark II en Harvard, causando un fallo.
- • 1960s-1970s: La complejidad del software aumentó con el desarrollo de lenguajes de programación avanzados y sistemas operativos complejos, incrementando la frecuencia de defectos.
- • 1980s: La explosión de la industria del software y la aparición de microcomputadoras llevaron a un aumento significativo en la producción de software, incrementando también la presencia de defectos debido a la rápida evolución tecnológica.
- • 1990s: Con el auge de Internet y las aplicaciones web, los defectos adquirieron una dimensión crítica de seguridad, destacando la importancia de la ciberseguridad.
- • 2000s-Presente: Las metodologías ágiles y DevOps han integrado la gestión de defectos en el ciclo de vida del desarrollo de software, utilizando herramientas automatizadas y técnicas avanzadas de pruebas para detectar y corregir bugs eficientemente. Sin embargo, la creciente complejidad del software asegura que los bugs sigan siendo un desafío persistente.

## Slide 5
- Pruebas de Software:
- Se ejecutan diversas pruebas (unitarias, integración, sistema y aceptación) para detectar distintos tipos de defectos.
- Registro de Defectos:
- Los defectos identificados se registran en sistemas de seguimiento como JIRA o Bugzilla, incluyendo detalles sobre el comportamiento anómalo, pasos para reproducirlo, severidad y entorno del problema.
- Análisis y Priorización:
- Análisis de Causa Raíz (RCA): Se identifican y comprenden las razones fundamentales del defecto usando técnicas como diagramas de Ishikawa y los 5 Porqués.
- Priorización: Se priori	zan los defectos según su impacto y urgencia (crítico, mayor, menor), frecuencia y impacto potencial en usuarios finales o componentes del sistema.
- Corrección y Validación:
- Después de la priorización, los defectos se corrigen y validan para asegurar que se han solucionado adecuadamente y que no se introducen nuevos problemas.
- Procesos

## Slide 6
- Desarrolladores:
- Responsables de escribir y mantener el código del software, además de corregir defectos identificados durante pruebas y uso en producción.
- Testers/QA (Quality Assurance):
- Ejecutan pruebas para identificar defectos y verifican que las correcciones no introduzcan nuevos problemas, asegurando el cumplimiento de los estándares de calidad.
- Gerentes de Proyecto:
- Supervisan el progreso del proyecto y la gestión de defectos, planificando recursos y evaluando el impacto de los defectos en los objetivos del proyecto.
- Analistas de Negocios:
- Ayudan a priorizar defectos según su impacto en el negocio y en los usuarios, evaluando la severidad y riesgo de cada defecto.
- Usuarios Finales:
- Proporcionan retroalimentación sobre el software en producción y pueden identificar defectos no detectados durante las pruebas, mejorando la experiencia del usuario y la satisfacción del cliente.
- Roles

## Slide 7
- Automatización de Pruebas:
- Utilizar herramientas automatizadas para ejecutar pruebas repetitivas de manera rápida y precisa, mejorando la eficiencia y cobertura de pruebas.
- Integración Continua/Entrega Continua (CI/CD):
- Implementar pipelines de CI/CD para automatizar la integración, prueba y entrega de código, facilitando la detección temprana de defectos y la entrega rápida de nuevas funcionalidades.
- Revisiones de Código:
- Realizar revisiones regulares de código entre pares o equipos para identificar posibles defectos antes de integrar cambios al repositorio principal, mejorando la calidad y consistencia del código.
- Pruebas de Seguridad:
- Incluir pruebas de seguridad en el proceso de desarrollo para identificar y mitigar vulnerabilidades, protegiendo la información sensible y manteniendo la confianza de los usuarios.
- Mejores Prácticas

## Slide 8
- Ciclo de Vida de Desarrollo de Software (SDLC):
- Seguir un ciclo de vida estructurado como Agile o Waterfall, que incluya fases definidas de desarrollo, pruebas y validación para gestionar el proceso desde la concepción hasta la entrega y mantenimiento del software.
- Gestión de la Configuración:
- Mantener un control estricto sobre las versiones del software y sus cambios mediante prácticas de gestión de configuración, asegurando que todas las modificaciones sean controladas y documentadas para evitar conflictos y errores.
- Documentación:
- Documentar detalladamente los defectos y las soluciones implementadas para facilitar el análisis futuro, la identificación de patrones recurrentes y la mejora continua en el proceso de desarrollo.
- Implementar estos métodos y protocolos estándar no solo mejora la eficiencia y calidad del software, sino que también fortalece la capacidad del equipo para responder a los desafíos del entorno tecnológico.
- Protocolos Estándar

## Slide 9
- Ventajas:
- Reducción de Costos: Identificar y corregir defectos en etapas tempranas del desarrollo minimiza los costos de reparación en fases posteriores y evita gastos adicionales.
- Mejora de la Calidad: Un enfoque sistemático en la gestión de defectos mejora la calidad general del software, asegurando que el producto final cumpla con los estándares esperados y proporcionando una mejor experiencia del usuario.
- Impacto Positivo:
- Seguridad Aumentada: Corregir defectos ayuda a reducir las vulnerabilidades de seguridad del software, protegiendo la integridad de los datos y la información confidencial de los usuarios.
- Confianza del Cliente: Un software con menos defectos inspira confianza en los clientes y usuarios finales, fortaleciendo la credibilidad y las relaciones a largo plazo.
- Ventajas y Desventajas

## Slide 10
- Desventajas:
- Costo Inicial: Implementar procesos y herramientas de gestión de defectos puede ser costoso inicialmente, incluyendo la adquisición de software y capacitación del personal.
- Requiere Recursos: La gestión efectiva de defectos demanda personal capacitado y tiempo dedicado, lo cual puede ser un desafío para equipos pequeños o con recursos limitados.
- Complejidad Adicional: La implementación de procesos de gestión de defectos puede agregar complejidad al flujo de trabajo, requiriendo una gestión cuidadosa para evitar ralentizar el desarrollo.
- Ventajas y Desventajas

## Slide 11
- Ariane 5:
- En 1996, el cohete Ariane 5 de la Agencia Espacial Europea explotó 40 segundos después de su lanzamiento debido a un error en el software de navegación. Un valor excedió el rango permitido, causando una excepción no manejada y la pérdida total del cohete y su carga útil, con un costo estimado en cientos de millones de dólares. Este incidente destaca la importancia de pruebas exhaustivas y gestión efectiva de excepciones en sistemas complejos.
- Therac-25:
- Entre 1985 y 1987, varios pacientes recibieron dosis letales de radiación durante tratamientos de radioterapia debido a errores en el software de la máquina Therac-25, permitiendo la activación inadvertida de dosis excesivas. Seis pacientes murieron como resultado directo. Este caso resalta las graves consecuencias de los defectos de software en aplicaciones críticas para la salud, subrayando la necesidad de prácticas robustas de desarrollo y pruebas.
- Problemas Históricos


# ===== Sesión Sincrónica S9.pptx =====


## Slide 1
- Aplicación y Automatización de Pruebas en el Desarrollo de Software
- Sesión sincrónica

## Slide 2
- ÍNDICE
- Tema 1: mapa conceptual
- Tema 2: retroalimentación preguntas del apunte
- Tema 3: retroalimentación preguntas del foro
- Tema 4: Taller

## Slide 3
- Resumen unidad

## Slide 4
- Resumen unidad

## Slide 5
- Fase de retroalimentación

## Slide 6
- Apunte activador de aprendizaje
- ¿Cómo podría beneficiar la integración continua (CI) y la entrega continua (CD) en la detección y corrección rápida de defectos en un proyecto de desarrollo de software?
- ¿Quién fue la persona que popularizó el término "bug" en el contexto informático en 1947?
- ¿Cuáles son los tipos principales de pruebas de software utilizadas para identificar defectos y en qué etapas del desarrollo se aplican?
- Compara el ciclo de vida de un defecto en metodologías Agile versus Waterfall. ¿En qué aspectos difieren y cómo influye esto en la gestión de defectos?
- ¿Cómo definirías la fase de "Análisis" dentro del ciclo de vida de un defecto? ¿Cuál es su propósito principal en el proceso de desarrollo de software?
- Mencione un ejemplo de un error que se puede detectar con mayor facilidad mediante pruebas manuales que con pruebas automatizadas.
- "La primera etapa del proceso de aplicación de las pruebas manuales es la ejecución de los casos de prueba." (Verdadero o Falso)

## Slide 7
- Foro crítico reflexivo
- 1.	En tu experiencia, ¿cuáles son los desafíos más comunes que enfrentas al ejecutar casos de prueba manualmente y cómo los superas?
- 2.	Cuando encuentras un error durante una prueba manual, ¿qué criterios sigues para asegurar que tu registro sea claro y útil para el equipo de desarrollo?
- 3.	Discute una situación en la que aplicar técnicas de exploración del software te permitió descubrir un fallo crítico. ¿Qué pasos seguiste y qué impacto tuvo en el proyecto?

## Slide 8
- Foro crítico reflexivo - Respuesta
- 1.   En tu experiencia, ¿cuáles son los desafíos más comunes que enfrentas al ejecutar casos de prueba manualmente y cómo los superas?
- Respuesta:
- Uno de los desafíos más comunes al ejecutar casos de prueba manualmente es la repetitividad y el tedio que pueden llevar a errores humanos, como la omisión de pasos importantes o la falta de atención a detalles críticos. Otro desafío es la limitación en el alcance de las pruebas debido a la cantidad de tiempo disponible, lo que puede llevar a una cobertura de pruebas insuficiente. Para superar estos desafíos, adopto un enfoque sistemático, utilizando listas de verificación y guías detalladas para asegurarme de que sigo todos los pasos correctamente. Además, divido las sesiones de prueba en bloques más pequeños con descansos intermedios para mantener la concentración. También priorizo los casos de prueba según su criticidad, asegurando que las funcionalidades más importantes sean probadas exhaustivamente.

## Slide 9
- Foro crítico reflexivo - Respuesta
- 2.   Cuando encuentras un error durante una prueba manual, ¿qué criterios sigues para asegurar que tu registro sea claro y útil para el equipo de desarrollo?
- Respuesta:
- Al registrar un error, sigo varios criterios para asegurar que la documentación sea clara y útil. Primero, describo el error de manera detallada, incluyendo el comportamiento esperado y el comportamiento real observado. A continuación, especifico los pasos exactos para reproducir el error, lo que incluye datos de entrada, configuraciones específicas del entorno, y cualquier acción previa que pudiera haber influido en el comportamiento. También indico la gravedad del error y su impacto en el sistema, lo que ayuda al equipo de desarrollo a priorizar su resolución. Finalmente, adjunto capturas de pantalla, logs, o cualquier otra evidencia que pueda facilitar la comprensión del problema.

## Slide 10
- Foro crítico reflexivo - Respuesta
- 3.   Discute una situación en la que aplicar técnicas de exploración del software te permitió descubrir un fallo crítico. ¿Qué pasos seguiste y qué impacto tuvo en el proyecto?
- Respuesta:
- En una ocasión, durante la fase de pruebas de una aplicación de comercio electrónico, apliqué técnicas de exploración para verificar la funcionalidad de pago en un entorno que no estaba cubierto por los casos de prueba predefinidos. Decidí probar diferentes combinaciones de métodos de pago y tipos de productos, y descubrí que al seleccionar una opción de pago específico en combinación con un tipo de descuento, la aplicación permitía que la transacción se completara sin aplicar el descuento correctamente, lo que resultaba en un cobro incorrecto al cliente.

## Slide 11
- Taller colaborativo

## Slide 12
- Desarrollo del mini problema
- Un equipo de desarrollo ha lanzado la primera versión de una aplicación de gestión de tareas que permite a los usuarios crear, editar, eliminar y organizar sus tareas diarias. Antes de la implementación final, se requiere una fase de pruebas manuales para garantizar que todas las funcionalidades básicas funcionan correctamente.

## Slide 13
- Desarrollo del mini problema
- Indicadores de Logro:
- 1. Ejecuta casos de prueba manualmente sobre el software, verificando que los resultados obtenidos coincidan con los esperados según las especificaciones.
- Caso de Prueba:
- - Escenario: Crear una nueva tarea.
- - Acciones: El tester ingresa el título "Comprar leche" en el campo de tareas y hace clic en "Guardar".
- - Resultado Esperado: La tarea "Comprar leche" aparece en la lista de tareas pendientes.
- - Resultado Obtenido: La tarea se guarda correctamente y aparece en la lista, coincidiendo con las especificaciones del caso de prueba.
- - Respuesta: El resultado del caso de prueba coincide con las especificaciones, lo que indica que la funcionalidad para crear tareas está funcionando correctamente.

## Slide 14
- Desarrollo del mini problema
- 2. Identifica de manera precisa los errores encontrados durante las pruebas manuales, asegurando que estén registrados de forma clara y comprensible para su posterior análisis y corrección.
- Detección de Error:
- - Escenario: Editar una tarea existente.
- - Acciones: El tester selecciona la tarea "Comprar leche", la edita cambiando el título a "Comprar leche y pan", y guarda los cambios.
- - Error Detectado: Al guardar, la aplicación genera un error y no actualiza la tarea en la lista.
- - Registro del Error: "Error al editar la tarea. Al intentar cambiar el título de 'Comprar leche' a 'Comprar leche y pan', la aplicación genera un mensaje de error 'NullReferenceException' y no guarda los cambios."
- - Respuesta: El error fue identificado y registrado claramente, lo que permitirá al equipo de desarrollo comprender el problema y aplicar la corrección necesaria.

## Slide 15
- Desarrollo del mini problema
- 3. Aplica técnicas de exploración del software eficazmente, descubriendo posibles fallos que pudieran haberse pasado por alto en los casos de pruebas predefinidos.
- Exploración del Software:
- - Acción: El tester, al explorar la aplicación, decide probar la funcionalidad de ordenamiento de tareas.
- - Descubrimiento del Fallo: Al intentar ordenar las tareas por fecha de creación, el tester descubre que la aplicación no responde y se cierra inesperadamente.
- - Registro del Fallo: "Error crítico en la función de ordenamiento. La aplicación se cierra inesperadamente cuando el usuario intenta ordenar las tareas por fecha de creación."
- - Respuesta: La técnica de exploración permitió descubrir un fallo crítico que no estaba cubierto en los casos de prueba predefinidos, demostrando la importancia de explorar el software para encontrar posibles errores ocultos.
- Conclusión:
- En este mini caso, el tester ha demostrado habilidad en la ejecución de pruebas manuales, en la identificación y registro preciso de errores, y en la aplicación efectiva de técnicas de exploración. Estos esfuerzos contribuyen a asegurar la calidad del software antes de su lanzamiento al mercado.