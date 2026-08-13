---
title: '043 - Pruebas móviles: Pruebas básicas con el dispositivo (II parte).'
date: '2018-05-16T07:00:08+00:00'
url: /2018/05/16/043-pruebas-moviles-pruebas-basicas-con-el-dispositivo-ii-parte/
image: /img/blog-images/old-post/2018/04/foto42.jpg
categories:
- appmóviles
- qa
tags:
- mobile-testing
- ux
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a seguir hablando de las pruebas básicas que siempre debemos hacer con un dispositivo físico sobre nuestra aplicación. ¡Comenzamos!

### Memoria del dispositivo.

![3](/img/blog-images/old-post/2018/04/3.jpg)

Una de las pruebas más importantes que debemos hacer es la de la memoria del dispositivo. Debemos tener en cuenta el tamaño de nuestra aplicación primero a la hora de instalarla (si no tenemos memoria suficiente, no podremos hacerlo) y también a la hora de ejecutarla. Si nuestra aplicación guarda demasiados recursos en el dispositivo, debemos comprobar que si el dispositivo tiene la memoria casi llena, nuestra aplicación sigue funcionando correctamente o nos aparece algún mensaje diciendo que debemos borrar memoria para seguir utilizándola (este flujo daría lugar a un gran espectro de pruebas que podríamos realizar). ¿Qué pasaría si tenemos el dispositivo casi lleno y estamos ejecutando la aplicación? ¿Tenemos pérdida de memoria de datos de la app?, ¿si eliminamos datos de la memoria, podremos recuperar aquellos que no se han podido guardar antes por no tener espacio suficiente?.

También debemos comprobar la memoria que gasta en el caso de que tengamos el dispositivo limpio, es decir, ¿cuántos datos se guardan en nuestro dispositivo?, ¿es una cantidad alta?, ¿qué peso tiene la aplicación al instalarla?. Esas son algunas de las preguntas que debemos hacernos y que debemos plasmar en nuestro plan de pruebas a la app con un dispositivo físico.

### Batería.

![4](/img/blog-images/old-post/2018/04/4.jpg)

La batería es uno de los problemas fundamentales de los smartphones y por tanto una de las pruebas más importantes que debemos hacer cuando probamos una aplicación móvil. ¿Qué reacción tiene nuestra aplicación cuando la batería del dispositivo donde la estamos ejecutando está a punto de agotarse?, ¿qué ocurre si la batería no tiene una carga óptima y se nos apaga el terminal?, ¿perdemos los datos de la aplicación? (por ejemplo estamos en mitad de una compra y se nos apaga el móvil, ¿podremos continuar en ese punto al encenderlo?).

En el mismo apartado de la batería debemos tener en cuenta la función que juega el cable de carga. ¿La aplicación sigue funcionando bien cuando conectamos el cable de carga?, ¿y al quitarlo?.

Este tipo de casos es algo que debemos añadir a nuestro plan de pruebas de aplicaciones sobre dispositivos físicos.

### Reproducción de sonidos.

![6](/img/blog-images/old-post/2018/04/61.jpg)

Imaginaos que tenemos música sonando en nuestro móvil (a través de cualquier tipo de aplicación) y estamos probando una aplicación de radio, ¿la música que estamos reproduciendo se para?, ¿se mezclan los sonidos?, ¿podemos pararla?, ¿afecta al uso de nuestra aplicación el hacer un gesto tan simple como cambiar de canción?. Este tipo de casos debemos tenerlos en cuenta al redactar el plan de pruebas de nuestra aplicación. Puede que este tipo de cosas no nos afecten, pero debemos pensar en el tipo de aplicación que estamos probando (si es alguna de reproducción de audio o video) y si este tipo de casos nos puede afectar.

### Experiencia de usuario (UX).

![5](/img/blog-images/old-post/2018/04/5.png)

Este es uno de los puntos más importantes y a los que me gustaría dedicar una entrada completa del blog. Para resumir, diremos que el UX y las pruebas asociadas a la experiencia de usuario son unas de las pruebas más importantes y problemáticas de hacer. Lo que siempre debemos tener en cuenta es que a la hora de comprobar una aplicación como  usuario siempre debe ganar la sencillez y la facilidad de utilizar la app.

* * *

Y hasta aquí nuestra actualización dedicada a las pruebas básicas con dispositivos físicos. En la siguiente entrada vamos a ir avanzando en la automatización de pruebas móviles, explicando diferentes herramientas para comenzar a realizarlas así como sus ventajas e inconvenientes e incluso post sobre cómo empezar a usarlas.

¡Nos leemos en la siguiente entrada!
