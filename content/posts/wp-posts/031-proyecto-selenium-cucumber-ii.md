---
title: 032 - Proyecto Selenium - Cucumber (II).
date: '2017-10-18T07:00:25+00:00'
url: /2017/10/18/031-proyecto-selenium-cucumber-ii/
image: /img/blog-images/wp-posts/2017/10/foto32.jpg
categories:
- automation
- cucumber
- qa
- selenium-webdriver
tags:
- selenium
author: estefafdez
---
¡Hola a todos!

En esta entrada seguiremos hablando del proyecto [Selenium-Cucumber](https://github.com/estefafdez/selenium-cucumber) que comenzamos en la anterior entrada. ¡Comenzamos!

![a.png](/img/blog-images/wp-posts/2017/08/a.png)

* * *

### URL Repositorio: [https://github.com/estefafdez/selenium-cucumber](https://github.com/estefafdez/selenium-cucumber)

* * *

En esta entrada vamos a explicar la sección **Configure Environment** del proyecto centrándonos en la clase **createDriver**.

### Configure Environment.

Esta sección se compone de las siguientes clases:

- CreateDriver.java
- WebDriverFactory.java
- PropertiesHandler.java

_\*Nota: Las clases HandlerRepo.java y Main.java las comentaremos una vez que estén terminadas ya que siguen siendo un WIP._

#### CreateDriver.java

Esta clase es una de las más importantes ya que nos sirve para poder configurar y crear el WebDriver que vamos a usar en el proyecto al lanzar los test.

Para empezar en esta clase tenemos un Singleton pattern para devolver una única instancia de la clase así como un constructor privado:

![constructor](/img/blog-images/wp-posts/2017/10/constructor.png)

Esto nos permitirá inicializar la configuración del driver cuando se cree una nueva instancia de la clase.

Después de estas funciones principales necesitamos inicializar la configuración del driver con los parámetros que se han seleccionado en el POM (como explicamos en la anterior entrada, la funcionalidad principal de este proyecto es tener un core en el que mediante el POM podamos seleccionar tanto el sistema operativo como el navegador que queremos usar para lanzar los test automáticos).

¿Cómo hacemos esta lectura de propiedades del POM y las usamos para configurar la instancia del Driver? Mediante la función **initConfig():**![initconfig.png](/img/blog-images/wp-posts/2017/10/initconfig.png)

¿Qué podemos ver en esta función? que tenemos una función load para cargar las diferentes properties que necesitamos, en nuestro caso esas properties son: **browser, os, logLevel.**¿Cómo las definimos en el POM? Escribiendo en los siguientes campos el valor que queramos de los disponibles:

![pom.png](/img/blog-images/wp-posts/2017/10/pom.png)

- Browser: podemos seleccionar como navegador Firefox, Chrome, Internet Explorer (Remote sería para lanzar los test automáticos en SauceLabs que es un WIP por ahora).
- OS: Podemos seleccionar el sistema operativo con el que trabajemos, ya sea Linux, Mac o Windows.
- LOG: Podemos seleccionar el tipo de log que queremos ver: todos los logs, debug, info...

Una vez que tenemos cargador y leídos los parámetros y guardados en nuestras variables, llamamos a nuestra clase WebDriverFactory que no es más que una factoría de Drivers y en la que llamaremos al método createNewWebDriver pasándo por parámetros el navegador y el sistema operativo que hemos guardado previamente.

Este método nos devolverá el driver que usaremos. Además hemos añadido en la configuración que antes de inicializar el driver se borren las cookies y que se maximice el  navegador.

Y hasta aquí la clase createDriver. En la siguiente entrada seguiremos con la clase WebDriverFactory donde veremos cómo crear una factoría con los diferentes Drivers disponibles y cómo inicializarlos.

¡Hasta la siguiente entrada!
