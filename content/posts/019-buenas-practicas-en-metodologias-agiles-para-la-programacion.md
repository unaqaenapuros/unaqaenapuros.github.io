---
title: 019 - Buenas prácticas en Metodologías Ágiles para la programación.
date: '2017-07-19T07:00:30+00:00'
url: /2017/07/19/019-buenas-practicas-en-metodologias-agiles-para-la-programacion/
image: /img/blog-images/old-post/2017/06/foto19.jpg
categories:
- code-quality
- qa
tags:
- agilidad
- buenas-prácticas
- metodología-ágil
- scrum
author: estefafdez
---
¡Hola a todos!

Continuando con nuestro anterior post, en esta ocasión hablaremos de buenas prácticas en las metodologías ágiles para la programación. ¡Comenzamos!

Ya que hemos visto algunas de las buenas prácticas recomendadas para las metodologías ágiles, vamos a centrarnos ahora en las buenas prácticas orientadas a la programación en una metodología ágil.

En un principio este tipo de buenas prácticas se catalogan como Extreme Programming (XP), aunque también se han definido con términos como Prácticas de la Ingeniería Ágil, Buenas prácticas de Scrum y Agile Programming.

Podemos definir estas prácticas en los siguientes puntos:

#### Test-first programming (o quizás Test-Driven Development):

- Escribir código si tenemos primero un test que falla.
- Eliminar duplicación (conseguir un código lo más "bonito" posible.

Esto tiene unas implicaciones técnicas:

1. Diseñar el código según escribimos nuestros test: debemos encontrar un balance entre el diseño de UMLs y la realización de test para que nos orienten por dónde tenemos que ir.
1. El entorno de desarrollo tiene que ser capaz de decirnos rápidamente el estado de nuestro código en todo momento (debe ser rápido o sino se deja de hacer pruebas, por lo que hay que diseñarlos para que sean lo más rápidos posibles).
1. Diseñar componentes altamente cohesivos y muy poco acoplados para conseguir probarlos fácilmente.

#### Continuous Integration:

Las prisas hacen que no nos paremos a pensar pero...¿qué pasaría si los cambios los ponemos en producción directamente habiendo hecho simplemente unit test? seguramente falle. Poco o nada dedicamos a la integración continua y debería ser tan necesaria como un buen gestor de repositorios.

#### Simple design:

Sigue siempre la filosofía [KISS](https://es.wikipedia.org/wiki/Principio_KISS): Keep It Simple, Stupid.

#### Pair programming:

Pair programming consiste en juntar a dos personas con distinto nivel o conocimientos y ponerlas a desarrollar software. Para ello se utiliza normalmente la técnica Ping-Pong TDD, en la que una persona codifica y arregla fallos mientras la otra plantea pruebas. El pair programming se recomienda cambiar de pareja. Esto tiene pros y contras:

- La ventaja es que las personas del equipo serán realmente multidisciplinar.
- La desventaja es que las personas acaban medio locas por el cambio de contexto.

Compartir la base de conocimiento con todo el equipo o con la mayoría de los programadores para llegar a tener un equipo multidisciplinar.

#### El perfil del DevOps:

Si tienes el privilegio de tener a una persona sólo de sistemas dentro de tu proyecto (cosa rara), verás que sufre algunos ataques al corazón de vez en cuando en su día a día. Para ayudarle a que no los tenga es recomendable que aprenda a cómo optimizar su trabajo utilizando técnicas de programación.

#### Compartir una misma metodología:

Seguir un estándar para la codificación que sigan todos los programadores del equipo para mantener la coherencia del proyecto y seguir siempre una misma forma de trabajar.

Ser riguroso cuando se escribe el código y tener una refactorización constante del código.

Y hasta aquí los consejos  sobre las metodologías ágiles aplicadas a la programación. En la siguiente entrada hablaremos de buenas prácticas a la hora de diseñar test automáticos con Selenium Webdriver.

¡Hasta la siguiente entrada!
