---
title: 034 - Proyecto Selenium - Cucumber (IV).
date: '2017-11-01T08:00:08+00:00'
url: /2017/11/01/034-proyecto-selenium-cucumber-iv/
image: /img/blog-images/old-post/2017/10/foto34.jpg
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

![a.png](/img/blog-images/old-post/2017/08/a.png)

* * *

### URL Repositorio: [https://github.com/estefafdez/selenium-cucumber](https://github.com/estefafdez/selenium-cucumber)

* * *

En esta entrada vamos a explicar la sección **Step Definitions** del proyecto centrándonos en la clase Hooks y en una clase con pasos ya definidos como es ClickSteps().

### Step Definitions.

Esta sección se compone de las siguientes clases:

- ConfigurationSteps.java
- Hooks.java
- ClickSteps.java
- AssertionSteps.java
- ConfigurationSteps.java
- InputSteps.javaJavascript
- HandlingSteps.java
- KeyboardSteps.java
- NavigationSteps.java
- ProgressSteps.java
- ScreenshotSteps.java

_\\* Cada una de estas clases representa un conjunto de acciones agrupadas en cada clase._

#### Hooks.java

Esta es la clase base de inicialización de los test. ¿Qué tiene esta clase que la hace tan importante? Vamos a ver los métodos que la componen:

![before.png](/img/blog-images/old-post/2017/10/before.png)

Estos métodos @Before son de los más importantes a la hora de lanzar los test. Como hemos hablado en otras entradas, estamos usando métodos de jUnit, en este caso el método @Before (y después el @After). Recordemos que estos métodos son los que se ejecutan antes y después de lanzar la clase de test.

¿Qué hacen nuestros métodos @Before?

- El primero nos guarda el escenario en el que estamos, para poder utilizarlo en el segundo método.
- El segundo @Before con el método **initDriver**() inicializa el driver mediante la llamada al método **CreateDriver.initConfig**() que ya hemos visto en anteriores entradas. Además, nos pie en el Log el escenario en el que estamos para poder verlo de forma más visual.

Ahora pasaremos a ver el método que se ejecuta en el @After.

![after.png](/img/blog-images/old-post/2017/10/after.png)

¿Qué necesitamos hacer después de ejecutar cada test? Pues lo que hacemos es que si el escenario ha fallado (el test falla) hacemos una captura de pantalla y la guardamos y una vez que haya terminado, quitamos el driver.

#### ClickSteps.java

Esta es una clase con pasos (acciones) ya definidas. Hemos catalogado las acciones en diferentes clases para organizar, de una forma definida, las funciones implementadas para hacer más fácil el desarrollo de los test. ¿Qué nos encontraremos en esta clase? Pues todas las acciones posibles que necesiten un click en un elemento.

Vamos a ver cómo es la inicialización de esta clase y uno de sus métodos para hacernos una idea de cómo hemos organizado las demás clases:

![click.png](/img/blog-images/old-post/2017/10/click.png)

Lo primero que tenemos que hacer al inicializar la clase es llamar a la clase Hooks (que acabamos de comentar) para traernos el driver (recordemos que esta clase es la que llama a nuestro método para inicializar el driver y traernos la instancia).

Una vez que tenemos el driver, podremos usarlo en nuestra función.

¿Cómo hacemos una función click?

Primero ponemos el paso en Gherkin al que corresponde:

![when.png](/img/blog-images/old-post/2017/10/when.png)

¿Qué necesitamos para hacer click? como ya vimos, el type para seleccionar el elemento ( _xpath, css, id...)_ y la key del elemento al que queremos hacer click. Con estos datos llamamos a la función **getCompleteElement** (de la que ya hablamos en previas entradas) y nos devuelve el elemento completo (By) al que queremos hacer click. Una vez que tenemos esto, podemos utilizar nuestra función de Selenium **findElement(y el elemento)** y la función **click()** para hacer click en él.

Una vez que hemos hecho click, mostraremos por consola que se ha realizado el click y al elemento al que le hemos hecho click. De esta forma podremos ver en el Log los elementos por los que vamos pasando y las acciones realizadas a cada elemento.

Y de esta forma hemos creado funciones propias en cada clase por acciones para que cualquier persona que use nuestro core pueda hacer test automáticos sin tener que pensar en cómo hacer toda la lógica (¡nosotros se la damos ya hecha!).

Y hasta aquí esta entrada. En la siguiente entraremos al detalle del bloque Features para que veamos cómo crear un test automático usando las Features de Cucumber así como la carpeta Selectors y ver cómo podemos definir los elementos necesarios para los test.

¡Hasta la siguiente entrada!
