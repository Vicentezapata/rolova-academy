const T = [
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">¡Bienvenidos a la gran recta final! <br><br>Ustedes ya saben cómo crear un sistema web, conectarlo a una base de datos y subirlo a la nube. En teoría, podrían construir cualquier cosa. Pero... <b>(Pausa dramática)</b><br><br>¿Qué pasa cuando tu aplicación empieza a recibir 100,000 visitas al día? ¿Qué pasa cuando tienes que conectarte con 5 pasarelas de pago distintas? El código básico de controladores gigantes (que aprendimos en la Unidad 2) colapsa, se vuelve imposible de mantener.<br><br>En esta unidad no aprenderán a 'hacer' cosas nuevas, aprenderán a hacerlas como lo exigen las empresas que pagan los sueldos más altos. Construiremos una arquitectura <i>Enterprise</i>.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 2 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">Miren esto. Si un Junior hace CRUDs, un Senior diseña Arquitecturas. <br><br>Vamos a recorrer estos 7 módulos que separan a los programadores básicos de los verdaderos Ingenieros de Software. <i>(Señalar los íconos)</i>. Hoy no escribiremos tanto código nuevo, reestructuraremos el que ya existe para hacerlo a prueba de balas.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 2 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">Iniciamos el Módulo 1. Aquí entenderemos por qué poner todo el código (SQL, validación, correos) en un Controlador de 500 líneas es un error masivo que les costará noches de desvelo en el futuro.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 1 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;"><b>(Anécdota)</b><br> ¿Qué pasa si su jefe llega mañana y dice 'Oye, ya no usaremos Stripe, nos cobra mucha comisión. Ahora pasaremos todo a PayPal'? <br><br>Si programaron a lo Junior, buscando clases específicas con el 'new StripePaymentGateway', tendrán que buscar y reemplazar ese código en 50 archivos distintos. Si programan a lo Senior, su controlador jamás supo si era Stripe o Paypal. Solo pidió 'Algo que pague' (Interface). Cambian una sola línea en Laravel y la magia ocurre.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 3 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">Para que la inyección de la diapositiva anterior funcione, usamos los Service Providers. <br>El Provider es literalmente el lugar donde 'unimos los cables' de nuestra aplicación. Le decimos al cerebro de Laravel: 'Oye, cuando un controlador te pida esta interfaz, entrégale esta clase'. Así de potente.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 2 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">Este patrón fue el Rey de Laravel hace unos años. Su objetivo es simple: Desacoplar la base de datos de tu lógica. Si mañana tu empresa migra de MySQL a MongoDB, o si deciden guardar los usuarios en la Caché de Redis en vez de la BD... El controlador ni se entera. Solo sigue llamando a 'getActiveUsers()'.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 2.5 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;"><b>(Ojo aquí)</b><br> Las Actions Classes son la Arquitectura Moderna de Laravel. En vez de Repositories, hoy la gente crea clases especializadas con un solo método público ('execute()' o 'handle()'). <br><br>¿Por qué? Porque puedes reutilizar esa clase 'CreateInvoiceAction' desde la web, desde una API móvil, e incluso desde la consola de comandos Artisan. Reusabilidad pura.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 2.5 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">Terminada la arquitectura de clases, hablemos del corazón de Laravel: Eloquent. Ya saben hacer un CRUD básico, pero Eloquent es una bestia cuando se trata de optimizar el rendimiento.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 1 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">El polimorfismo es hermoso. Si no lo usas, terminarías con una tabla de 'Comentarios' que tiene un post_id, un video_id, un photo_id, y 20 columnas vacías. Al usar polimorfismo, solo tienes dos columnas: el ID del objeto (commentable_id) y QUÉ tipo de objeto es (commentable_type). Eloquent sabe exactamente qué buscar.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 3 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;"><b>(Tip sobre los Casters)</b><br> MySQL no sabe qué es un Array en PHP, y PHP no sabe qué hacer con un String de JSON. Los Casters traducen automáticamente. Guardas un array, y Laravel lo convierte a texto en BD. Lo lees, y Laravel te lo devuelve como array. Todo sin que tú muevas un dedo. <br><br>Y sobre los Scopes: dejen de escribir 'where('role', 'admin')' en 10 partes distintas. Si mañana el admin pasa a llamarse 'superadmin', rompen todo.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 2.5 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">El principal problema de PHP es que es síncrono. Bloqueante. Si un proceso demora, el usuario se queda viendo una pantalla blanca que carga infinitamente. Y eso arruina la experiencia. Entramos al mundo de las Colas (Queues).</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 1 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">Todo proyecto moderno usa Colas. Miren este diagrama: el usuario pide el reporte. Laravel no se queda esperando los 10 minutos. Agarra una 'orden de trabajo' (Job), la tira a Redis, y de inmediato le responde al usuario '¡Listo! Te avisaremos por correo'. <br><br>Mientras tanto, detrás de escena, un proceso invisible llamado Worker toma esa orden y se demora lo que tenga que demorar. Esa es la verdadera asincronía.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 3 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">El método dispatch 'empuja' el Job a la cola. Pero ojo, si ustedes hacen dispatch y no tienen levantado el servidor de Redis y el Worker... la tarea simplemente se quedará ahí dormida eternamente. Hay que prender al trabajador.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 2 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;"><b>(Anécdota)</b><br> En mi primer trabajo, pusimos la cola en la base de datos de MySQL. Cada 2 segundos MySQL hacía consultas para ver si había tareas nuevas. Arruinamos la base de datos. Por eso la industria usa Redis: es pura RAM, es veloz, no le duele revisar millones de veces. Y con Horizon, tienen un dashboard visual hermoso para ver gráficos de rendimiento de esos Workers.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 3 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">La Autenticación responde a '¿Quién eres?' (Con tu email y contraseña o token).<br><br>Pero la Autorización responde a '¿Tienes derecho a borrar este archivo?'. Son dos conceptos absolutamente diferentes.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 1 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">Las policies centralizan los permisos. Así, en vez de poner 'if ($user->id == $post->user_id)' en cada lugar de la app (controlador, vista, api), simplemente llaman a 'authorize()'. Si el usuario no tiene permisos, el framework detiene la ejecución al instante y arroja un error 403 Forbidden.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 2.5 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">No inventen la rueda. Si necesitan roles y permisos jerárquicos estructurados (SuperAdmin > Manager > Usuario), todos en Laravel instalan el paquete de Spatie. Es fácil, elegante, y usa caché automáticamente para no destruir la base de datos en cada consulta.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 2 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">¿Cómo sabemos que los cambios de código de hoy no rompieron algo que hicimos hace un mes? Testing automático. Escribimos código que prueba nuestro código.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 1 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">Al ejecutar 'php artisan test', Laravel levanta todo el sistema, inyecta la base de datos falsa temporal, simula el clic de POST y verifica si la respuesta es la correcta. Todo en 0.2 segundos. <br><br>Así es como duermen tranquilos las noches previas a un pase a producción.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 2.5 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">Esto es vital para servicios pagados (Tarjetas en Stripe, Twilio para SMS, Sendgrid). Usamos Fakes y Mocks para 'simular' el comportamiento externo sin tocar internet y sin gastar saldo.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 2 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">Históricamente, PHP devolvía HTML estático y tenías que hacer malabares con jQuery. Hoy, el ecosistema de Laravel es el rey de la reactividad.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 1 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">Si aman Javascript, usan Inertia.js. Si odian Javascript, usan Livewire. <br><br>Ambos ecosistemas están oficialmente soportados. Laravel Breeze o Jetstream te permiten iniciar un proyecto con cualquiera de los dos con un solo comando.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 2 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">La antigua técnica del Long-Polling, donde el navegador preguntaba '¿Hay mensajes nuevos?' cada 2 segundos, murió. Con WebSockets y Reverb, el servidor mantiene un túnel abierto. Cuando el usuario A comenta, el servidor 'empuja' (push) ese comentario al navegador del usuario B instantáneamente.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 2 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">Por último. Han programado una joya arquitectónica. ¿Cómo la subimos, monitoreamos y escalamos sin un equipo de ingenieros de redes? Con DevOps SaaS.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 1 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">El modelo de negocio de los creadores de Laravel radica en venderles Forge y Vapor. Han simplificado la administración de servidores a tal punto que ustedes mismos pueden ser los desarrolladores Backend Y los DevOps de sus empresas, aumentando su valor de mercado.</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 3 min</div>
    `,
    `
    <h4>Guión del Profesor</h4>
    <div style="font-size:1.1rem; line-height:1.7;">Ha sido un viaje increíble a lo largo de este curso. Dominar estos 7 módulos los posicionará en el tope del ecosistema web.<br><br><b>(Pausa final)</b><br><br>Ya tienen las herramientas y el conocimiento arquitectónico. Ahora el límite lo ponen ustedes. ¡Mucho éxito en el mercado laboral!</div>
    <div class="t-time" style="margin-top:15px; font-weight:bold; color:var(--p);">Tiempo: 1.5 min</div>
    `,
];
window.speakerNotes = {};
for(let i=0; i<T.length; i++) window.speakerNotes[i] = T[i];
