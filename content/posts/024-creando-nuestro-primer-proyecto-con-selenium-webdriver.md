---
title: 024 - Creando nuestro primer proyecto con Selenium Webdriver.
date: '2017-08-23T07:00:34+00:00'
url: /2017/08/23/024-creando-nuestro-primer-proyecto-con-selenium-webdriver/
image: /img/blog-images/old-post/2017/07/foto24.jpg
categories:
- automation
- qa
- selenium-webdriver
tags:
- geckodriver
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a aprender a hacer nuestro primer proyecto de pruebas automáticas usando Selenium Webdriver.... ¡Comenzamos!

**Herramientas utilizadas en este tutorial:**

- MacbookPro con MacOSX Sierra.
- InteliJ Idea 2017.
- Geckodriver for MacOSX: [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)

Vamos a comenzar creando un nuevo proyecto Maven de la siguiente forma:

Create new project -> Maven.

![Captura de pantalla 2017-07-15 a las 21.26.15.png](/img/blog-images/old-post/2017/07/captura-de-pantalla-2017-07-15-a-las-21-26-15.png)

Escribimos un GroupId y un ArtifactId y hacemos click en next.

![Captura de pantalla 2017-07-15 a las 21.27.44.png](/img/blog-images/old-post/2017/07/captura-de-pantalla-2017-07-15-a-las-21-27-44.png)

Elegimos la localización donde guardar el proyecto y hacemos click en finalizar. Tendremos un proyecto con la siguiente estructura:

![Captura de pantalla 2017-07-15 a las 21.30.24.png](/img/blog-images/old-post/2017/07/captura-de-pantalla-2017-07-15-a-las-21-30-24.png)

Comenzaremos con el fichero pom.xml. En él añadiremos las librerías que vamos a necesitar para nuestro proyecto como son Selenium 3 y JUnit. Lo añadimos como dependencias en nuestro pom.xml de la siguiente forma:

![Captura de pantalla 2017-07-15 a las 21.36.51](/img/blog-images/old-post/2017/07/captura-de-pantalla-2017-07-15-a-las-21-36-51.png)

Ahora vamos a realizar nuestro primer test, para ello vamos a crear una nueva clase y vamos a escribir nuestro primer test (vamos a usar los Xpath que vimos en la anterior entrada y la web de Google para ello):

![Captura de pantalla 2017-07-16 a las 19.20.14.png](/img/blog-images/old-post/2017/07/captura-de-pantalla-2017-07-16-a-las-19-20-14.png)

Después de ver el código tenemos que comentar varias cosas:

- Desde que Selenium 3 salió oficialmente, el driver de Firefox no está soportado por defecto, es por eso que debemos bajarnos Geckodriver para poder ejecutar test con Firefox. Es importante colocar el fichero dentro del proyecto en la carpeta resources y darle permisos de ejecución ( _chmod +x geckodriver_) sino, éste no funcionará.
- Indicaremos la localización de Geckodriver y definiremos una propiedad del sistema de la forma:

```java
System.setProperty("webdriver.gecko.driver", resourceFolder+"/geckodriver");
```

- Usaremos las anotaciones de JUnit para indicar:
  - @Before: métodos que serán invocados antes de cada test. Crearemos un método para inicializar una instancia del driver.
  - @After: métodos que serán invocados después de cada test. Crearemos un método para cerrar la instancia del driver y el navegador.
  - @Test: Anotación que deben llevar todos los test. En este apartado crearemos un método que será nuestro test.

Lo único que nos queda es ejecutar este test y comprobar el resultado, para ello nos ponemos encima del test, hacemos click con el botón derecho y hacemos click en Run test().

![Captura de pantalla 2017-07-16 a las 19.29.57.png](/img/blog-images/old-post/2017/07/captura-de-pantalla-2017-07-16-a-las-19-29-57.png)

El navegador se abrirá, se ejecutará el test y obtendremos el resultado:

![Captura de pantalla 2017-07-16 a las 19.30.57.png](/img/blog-images/old-post/2017/07/captura-de-pantalla-2017-07-16-a-las-19-30-57.png)

Y ya tenemos nuestro primer test realizado con Selenium 3 y JUnit. En el siguiente artículo haremos una recopilación de preguntas acerca de Selenium que todos deberíamos conocer.

¡Hasta la siguiente entrada!
