---
title: 021- Selenium 101.
date: '2017-08-02T07:00:17+00:00'
url: /2017/08/02/021-selenium-101/
image: /img/blog-images/old-post/2017/07/foto21.jpg
categories:
- automation
- qa
- selenium-webdriver
tags:
- selenium
- testing
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a hablar de Selenium, primero haciendo una pequeña definición de qué es, y hablando de Selenium IDE. ¡Comenzamos!

**Selenium** es un entorno de pruebas de software para aplicaciones web. Existen dos herramientas principales: _Selenium IDE_, que es una herramienta para grabar/reproducir pruebas sólo grabando acciones y en la que se puede generar el código de esas pruebas, y _Selenium Webdriver_ (el más conocido) en el que se pueden escribir en forma de código pruebas software usando lenguajes como Java, C#, Ruby, Groovy, Perl, Php o Python. Las pruebas pueden ejecutarse en cualquier navegador (Firefox, Chrome, IE, Safari..) así como en cualquier sistema operativo (Windows, Linux, MacOSX).

Selenium fue desarrollado por _Jason Huggins_ en 2004. Es un software de código abierto bajo la licencia apache 2.0. Uno de los datos más curiosos es su nombre.  El nombre de Selenium  proviene de una broma hecha por Huggins burlándose de un competidor llamado Mercury (mercurio) diciendo que el envenenamiento por mercurio puede ser curado tomando complementos de Selenio (de ahí su nombre).

### Selenium IDE.

 _Selenium IDE_ es una herramienta que ayuda a ejecutar test sobre una página o aplicación web. Estos test pueden ser de distintos tipos dependiendo de las preferencias o las necesidades de cada usuario. Esta herramienta permite desarrollar nuestros propios test, ofreciendo la posibilidad de guardarlos para su posterior uso. Para ello, proporciona una gran variedad de comandos o funciones, con una serie de parámetros que conjuntamente formarán un test completo.

En Selenium IDE incluye una herramienta de depuración que permite encontrar y solucionar errores cometidos por los usuarios en la definición de las pruebas que realicen. Al igual que pueden definirse test particulares, también existe la posibilidad de crear una suite de test, es decir, un conjunto de test agrupados para un fin concreto. Además de todas estas funciones, la herramienta dispone de la verificación de la existencia de elementos en la página que necesitamos probar.

Selenium IDE pone a disposición del usuario una serie de comandos inmediatos, los cuales se efectuarán uno tras otro sin tiempo de espera, pero además ofrece versiones de algunos de estos comandos a los que añade una opción de espera (Wait), para cuando la página tiene que cargar debido al acceso a otra página distinta o si la actual debe recargarse. Para cuando la carga de nuevos elementos se realiza mediante AJAX y no mediante un método tradicional, existen otros tipos de comandos que esperan a la carga de un elemento en concreto (waitFor).

La aplicación también dispone de diálogos con ventanas emergentes con la posibilidad de interactuar con ellas, almacenar los test en distintos lenguajes de programación (por ejemplo Java o Ruby), y visualizar los resultados en distintos formatos.

La herramienta dispone de una interfaz sencilla, con un diseño básico. Como herramienta de ejecución de casos de prueba y a su vez entorno de desarrollo, dispone de los siguientes elementos:

![ide_-_labelled_parts](/img/blog-images/old-post/2017/07/ide_-_labelled_parts.png)

- **URL de la página**: dirección de la página principal sobre la que se está ejecutando el test.
- **Barra de acceso rápido**: conjunto de botones a través de los cuales se pueden manejar las herramientas de forma rápida y sencilla (ejecutar un test, pausar la ejecución...).
- **Menú de test creados**: donde se recogen los test creados por el usuario y los cargados en la herramienta, lo que nos permite un acceso rápido a los mismos.
- **Cuadro para la definición de test**: Listado de comandos de Selenium IDE que componen un test definido por el usuario o cargado en la aplicación. Se puede acceder al código del test.
- **Muestra de resultados**: Se dispone de un cuadro, como en el incluido en todo el entorno de desarrollo, que da feedback al usuario que ejecuta el test. Este cuadro muestra los logs de resultados, errores a la hora de ejecutar el test y el resto de los resultados obtenidos.

Para poder usar esta herramienta, simplemente debemos tener instalado Mozilla Firefox, tener instalado el complemento de Selenium IDE.

En la próxima entrada hablaremos de Selenium Webdriver. ¡Nos leemos!
