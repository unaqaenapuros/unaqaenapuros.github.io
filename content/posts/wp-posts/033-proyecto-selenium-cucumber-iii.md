---
title: 033 - Proyecto Selenium - Cucumber (III).
date: '2017-10-25T07:00:42+00:00'
url: /2017/10/25/033-proyecto-selenium-cucumber-iii/
image: /img/blog-images/wp-posts/2017/10/foto33.jpg
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

En esta entrada seguiremos hablando del proyecto [Selenium-Cucumber](https://github.com/estefafdez/selenium-cucumber). ¡Comenzamos!

![a.png](/img/blog-images/wp-posts/2017/08/a.png)

* * *

### URL Repositorio: [https://github.com/estefafdez/selenium-cucumber](https://github.com/estefafdez/selenium-cucumber)

* * *

En esta entrada vamos a explicar la sección **Configure Environment** del proyecto centrándonos en la clase **WebDriverFactory** y **PropertiesHandler**.

### Configure Environment.

Esta sección se compone de las siguientes clases:

- CreateDriver.java
- WebDriverFactory.java
- PropertiesHandler.java

_\*Nota: Las clases HandlerRepo.java y Main.java las comentaremos una vez que estén terminadas ya que siguen siendo un WIP._

#### **WebDriverFactory**.java

En esta clase tenemos una factoría de Drivers que nos permitirá seleccionar y configurar el Driver de acuerdo a la selección de sistema operativo y navegador seleccionado en el POM.

Empezamos declarando la carpeta en la que se encuentran los ficheros que nos permitirán lanzar los diferentes drivers (Gekodriver para Firefox, Chromedriver...)

![resources](/img/blog-images/wp-posts/2017/10/resources.png)

De nuevo creamos un constructor privado y un Singleton pattern para crear una instancia única de la clase:

![constructor.png](/img/blog-images/wp-posts/2017/10/constructor1.png)

Y ahora vamos al método más importante de esta clase: createNewWebDriver().

![createnewwebdriver.png](/img/blog-images/wp-posts/2017/10/createnewwebdriver.png)

En este método tenemos 3 grandes bloques diferenciados: si el driver seleccionado es Firefox, Chrome o IE.

Para cada uno de ellos comprobamos el valor del parámetro browser que le hemos pasado para ver cuál ha sido el elegido, además del sistema operativo seleccionado. Debemos hacer la distinción de si el sistema operativo es Windows o no, ¿por qué? por que en Linux y Mac, los drivers no tienen extensión (.exe) como sí que tienen en Windows.

Si el driver seleccionado es Firefox, vemos el sistema operativo y devolvemos una nueva instancia del driver seleccionado así como la ruta para el fichero que se debe inicializar al ejecutar el test.

¿Qué se incluye en la carpeta files/software? Pues en esta carpeta encontramos diferentes carpetas por sistema operativo con los drivers disponibles para cada uno de ellos:

![drivers](/img/blog-images/wp-posts/2017/10/drivers.png)

y después de cada nueva instancia del driver la guardamos en la variable driver y la devolvemos y ya tenemos nuestra instancia del driver creada y configurada con los valores del POM leídos mediante properties.

* * *

#### PropertiesHandler.java

Esta es una clase customizada para gestionar la lectura de properties de un fichero.

Esta clase tiene dos funciones importantes:

_**getSelectorFromProperties():**_![getselector](/img/blog-images/wp-posts/2017/10/getselector.png)

¿Qué hace este método? Nos selecciona un fichero .properties donde esté la key que le pasamos y nos de vuelve el selector que necesitamos de ese fichero .properties. ¿Para qué nos sirve esta función? Pues para el siguiente método que contiene la clase.

**_getCompleteElement()_**![get.png](/img/blog-images/wp-posts/2017/10/get.png)

¿Qué hace este método? nos devuelve el WebElement a partir de un type y una key.

¿Qué entendemos por type? Si el elemento lo queremos seleccionar por _className, cssSelector, id, linkText, xPath._..  ¿y la Key? la key es el valor del elemento a seleccionar que puede ser el nombre de una clase, el nombre del selector css, el ID del elemento... juntos nos devuelve el elemento que usaremos para los métodos ya creados en el proyecto (de los que hablaremos más adelante) y que nos permitirán de forma fácil seleccionar elementos sin tener que poner el xPath directamente en la definición de los tests.

Y hasta aquí las clases de la sección **Configure Environment,** en las siguientes entradas hablaremos de los Steps definitions para ver cómo se han definido y cómo los podemos usar en los test.

¡Hasta la siguiente entrada!
