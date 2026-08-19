---
title: 035 - Proyecto Selenium - Cucumber (V).
date: '2017-11-08T08:00:00+00:00'
url: /2017/11/08/035-proyecto-selenium-cucumber-v/
image: /img/blog-images/wp-posts/2017/10/foto35.jpg
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

Esta será la última entrada referente al proyecto [Selenium-Cucumber](https://github.com/estefafdez/selenium-cucumber). ¡Comenzamos!

![a.png](/img/blog-images/wp-posts/2017/08/a.png)

* * *

### URL Repositorio: [https://github.com/estefafdez/selenium-cucumber](https://github.com/estefafdez/selenium-cucumber)

* * *

En esta entrada vamos a explicar la sección **Features** del proyecto y los selectores para completar nuestro primer test.

### **Features**.

Esta sección se compone de las diferentes Features (test) del proyecto.

#### **HomePage.feature**

![feature.png](/img/blog-images/wp-posts/2017/10/feature.png)

Pues bien, después de todo lo que hemos hablado sobre la estructura, ahora nos vamos a la parte más sencilla, crear un test automático.

Como ya vimos, en Cucumber, los test se definen mediante .features con diferentes escenarios y una serie de pasos que componen el test (como podemos ver en el ejemplo).

¿Cómo definimos un test?

- Comenzamos escribiendo el nombre de nuestra Feature (Home Page) además de una descripción para definir qué es lo que va a hacer nuestro test.
- Después definimos un escenario con su descripción.
- A continuación vamos realizando los pasos de acuerdo a las acciones (Step Definitions) que hemos definido en nuestras clases.
  - Como podéis ver en el paso de click, le pasamos tanto el type (xpath) como el nombre del elemento (en los selectores) al que queremos hacer click como ya vimos en la definición de ese método.

Como podemos ver, el escribir los pasos usando Cucumber y Gherkin hacen nuestros test mucho más legibles y fáciles de entender a simple vista sin tener necesitad de saber conceptos de programación.

### Selectors.

En esta sección encontraremos los ficheros .properties con los selectores de los elementos que necesitamos.

#### **selector.properties**

![selectors.png](/img/blog-images/wp-posts/2017/10/selectors.png)

Así es como se ve nuestro fichero de properties llamado selector.properties. ¿Qué definimos aquí? pues el xpath, ID, clase, className o forma de seleccionar el elemento que queramos de forma concreta. Podemos añadir todos los selectores que queramos teniendo en cuenta que debemos seguir algún tipo de orden para seguir haciendo mantenible este fichero.

¿Por qué tener los selectores (xpath, id...) en otro fichero si se pueden poner directamente en la lógica de los Page Object? Muy sencillo, para hacer nuestro proyecto más **mantenible**.  Si en algún momento el selector cambia (el xpath del elemento cambia por ejemplo) sólo deberíamos de actualizar ese selector en nuestro fichero de properties y no en cada test que lo usemos, de esta forma, hacer cambios nos será mucho más fácil, sencillo y rápido.

Y hasta aquí toda la información sobre el proyecto de Selenium Cucumber. Espero que después de esta explicación en diferentes entradas podáis entender la necesidad de tener tu propio Core para poder ejecutar test de forma rápida independientemente del proyecto para que el que se vaya a utilizar.

En la siguiente entrada empezaremos a hablar sobre pruebas automáticas para móviles. Y, sin más...

¡Nos leemos en la siguiente entrada!
