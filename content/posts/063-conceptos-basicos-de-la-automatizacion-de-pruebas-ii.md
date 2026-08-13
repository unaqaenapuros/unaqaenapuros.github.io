---
title: 063 - Conceptos Básicos de la Automatización de pruebas (II).
date: '2020-10-21T07:30:00+00:00'
url: /2020/10/21/063-conceptos-basicos-de-la-automatizacion-de-pruebas-ii/
image: /img/blog-images/old-post/2020/10/foto60.png
categories:
- automation
- best-practices
- code-quality
- qa
tags:
- testing
author: estefafdez
---
¡Hola a todos!

En esta entrada seguiremos hablando sobre los conceptos básicos a tener en cuentra sobre la automatización de pruebas. ¡Comenzamos!

### ¿Qué es un Test automático?

Antes de comenzar a explicar los tipos de test que tenemos, debemos comenzar explicando qué es un test para nosotros. Un test es:

**DEFINICIÓN DE TEST: Conjunto de acciones que se llevarán a cabo de manera atómica en la aplicación para comprobar que toda su funcionalidad cumple el resultado definido previamente.**

Un test está compuesto por:

- **Acciones únicas:** Acción unitaria que se realizará sobre la aplicación (Ej.: Hacer un click)
- **Flujo atómico:** Las acciones unitarias no se verán afectadas por otros test.
- **Precondición:** Condiciones que se deben cumplir para realizar la prueba.
- **Resultado esperado:** Resultado definido para cada acción.

Debemos tener en cuenta que cada vez que se ejecute un test automático, la aplicación comenzará desde cero, como si el usuario **la instala por primera vez o se visitara una web por primera vez (borrando las cookies).**

### Tipos de test automáticos.

Existen diversas tipologías de tests automáticos y cada uno de ellos aportan un valor diferenciado:

Tipo de TestDefiniciónTests unitarios.Los test unitarios comprueban que cada función desarrollada es correcta y que no se han cometido errores en el desarrollo. Con la ayuda de la integración contínua, se ejecutarán siempre antes de cada commit.Tests de User Interface y funcionales.Los test de UI y funcionales simulan acciones de usuario para los diferentes Use Cases y por tanto se anticipa que la experiencia de usuario y las funcionalidades sean las esperadas y funcionen correctamente.Monkey TestingLos tests aleatorios permiten detectar casos de error no controlados y ayuda a depurar la aplicación y prepararla para un despliegue en todo tipo de dispositivos. Además, estas herramientas no requieren de esfuerzo adicional para preparar los diferentes casos de uso.Cloud TestingSi se programan los tests de User Interface, es posible contratar servicios que ejecuten estos tests en multitud de Dispositivos (reales y virtuales), sin necesidad de que el Servicio disponga de ellos.Tipos de tests y su definición.

### Valoración de esfuerzo.

Aunque los tests automáticos y manuales tengan coste inicial el ponerlos en funcionamiento, es esencial ya que los esfuerzos de depuración del software aumentan exponencialmente dependiendo del momento en el que una incidencia es detectada.

La siguiente gráfica muestra esa relación:

{{< figure src="/img/blog-images/old-post/2020/10/chart.jpg?w=1024" alt="" caption="" >}}

### Limitaciones de las pruebas automáticas.

Debemos tener en cuenta que la automatización y los frameworks de desarrollo de pruebas automáticas también tienen limitaciones y que hay cosas que necesariamente van a seguir teniendo que ser probadas a mano.

Centrándonos en las aplicaciones de audio y video, las mayores limitaciones que hemos encontrado son las siguientes:

- **Audio:** no podemos comprobar automáticamente que se está escuchando un audio que se está reproduciendo al oído humano usando herramientas de pruebas. La solución que hemos encontrado es comprobar los botones de play/pause para comprobar que al salir (o no) el sonido se está reproduciendo, pero no tenemos ninguna forma nativa para comprobar que el audio esté sonando correctamente y no haya silencios en la emisión.
- **Video:** Como el audio, no podemos comprobar de forma automática que se está reproduciendo correctamente un video y se esté viendo correctamente. La solución que hemos encontrado es:
  - Comenzamos a reproducir un vídeo concreto haciendo click en el botón de play.
  - Comprobamos la barra de reproducción y los valores de tiempo inicial y final que aparecen.
  - Dejamos reproducir el video unos segundos.
  - Volvemos a comprobar la barra de reproducción y comprobamos que el tiempo inicial ha crecido y es mayor que el tiempo inicial anterior (eso quiere decir que el video ha comenzado a reproducirse).
  - Si esto se cumple, podemos concluir de forma automática que un video se está reproduciendo pero en ningún momento asegurar que se vea y escuche correctamente a la vista y oído humano.
- **Problemas de carga de datos y datos dinámicos:** Si no tenemos un entorno de pruebas estático que poder modificar es muy difícil comprobar de forma automática una aplicación de noticias que cambia constantemente. Para ello lo principal es tener un entorno de pruebas o un mockeo de servicios como ya hemos comentado anteriormente. Si este caso no ocurre, se deberá invertir más tiempo en procesar todos los datos y almacenarlos para poder comprobarlos luego que en el propio desarrollo de test automáticos. Lo mismo pasa con la publicidad y los objetos que aparecen a veces sí y a veces no. Para la automatización tenemos que tener muy claro qué prueba vamos a hacer, cuál es el resultado esperado y el obtenido y esperar exactamente lo que sabemos que va aparecer. El detectar errores de casos repetitivos es en lo que nos ayuda la automatización.

y hasta aquí nuestros conceptos básicos sobre automatización. Espero que os haya valido para asentar conceptos y aprender el por qué es tan importante automatizar. En las próximas entras hablaremos de las pruebas unitarías. ¡Hasta la siguiente entrada!
