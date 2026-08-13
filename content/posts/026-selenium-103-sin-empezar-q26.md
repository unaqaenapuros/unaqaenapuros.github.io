---
title: 026 - Selenium 103.
date: '2017-09-06T09:00:59+00:00'
url: /2017/09/06/026-selenium-103-sin-empezar-q26/
image: /img/blog-images/old-post/2017/08/foto26.jpg
categories:
- automation
- qa
- selenium-webdriver
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a continuar con la recopilación de preguntas acerca de Selenium Webdriver a la hora de enfrentarnos a una entrevista de trabajo….¡Comenzamos!

- **¿Qué comandos existen para los diferentes tipos de navegación? Pon un ejemplo.**

Los comandos de navegación disponibles en Selenium son los siguientes:
**navigate().back()** – Este método de navegación lo que hará es volver a la página anterior que estuviéramos visitando. No necesitamos ningún parámetro.  Lo usaremos de la siguiente forma:  _driver.navigate().back();_ **navigate().forward()** – Este método se puede usar cuando hemos vuelto a una página anterior y queremos volver a la página en la que estábamos antes, al contrario del navigate.back, este comando navega a la página siguiente. Tampoco necesita ningún parámetro y lo usaremos:  _driver.navigate().forward();_ **navigate().refresh()** – Este método refresca la página actual del usuario, volviendo a cargar todos los elementos de nuevo. No se necesita ningún parámetro y lo usamos de la forma:  _driver.navigate().refresh();_ **navigate().to()** – Este método sirve para lanzar una nueva página y navegar a una URL específica que debemos pasar como parámetro.  Lo usaremos de la forma: _driver.navigate().to(“https://estefafdez.com”);_

- **¿Cómo podemos hacer click en un hyper link usando linkText?**

Lo haremos usando primero el comando findElement usando el By.linkText y poniendo el texto que queremos buscar. A continuación usamos el comando click para hacer click en ese elemento. Quedaría de la siguiente forma:

> _driver_ _.findElement(By.linkText(_ _“estefafdez”_ _)).click();_

Si tenemos un partial link text también podemos usar esa opción para buscar el elemento que necesitamos:

> _driver_ _.findElement(By.partialLinkText(_ _“est”_ _)).click();_

- **¿Cuándo se usa findElement() y findElements()?**

**findElement():** se usa para encontrar el primer elemento de la página web que tenga el valor específico que queremos encontrar y hemos definido. Eligiendo esta opción, sólo se podrá seleccionar el primer elemento que se encuentre.  Por ejemplo:

> _WebElement element =_ _driver_ _.findElements(By.xpath(_ _“//div\[@class=’custom\_list’\]/ul/li”_ _));_

 **findElements():** se usa para encontrar todos los elementos en la página web actual que tengan el valor específico que queremos encontrar y hemos definido. Cuando usamos este comando, todos los elementos que se encuentren serán guardados en una lista de WebElements. Por ejemplo:

> _List <WebElement> elementList =_ _driver_ _.findElements(By.xpath(_ _“//div\[@class=’custom’\]/ul/li”_ _));_

- **¿Cuál es la diferencia entre los comandos driver.close() y driver.quit()?**

**driver.close()**: Este método de Selenium se usa para cerrar la ventana en la que actualmente se está ejecutando el test con Selenium, simula a cerrar la ventana actual en la que está un usuario. Este comando no tiene ningún parámetro y no devuelve ningún valor.

**driver.quit()**: Este método de Selenium cierra todas las ventanas que el driver ha abierto. Como close(), este método no necesita ningún parámetro y no devuelve ningún valor.

- **¿Cómo comprobamos que el título de una página es correcto mediante un Assert?**

Para poder acceder al título de la página tenemos que usar el comando driver.getTitle(), este comando guardará el texto y lo podremos comparar con el título que queremos comprobar mediante el comando equals, todo esto dentro de un método AssertTrue que nos devolverá si el título es correcto o no. Podemos hacerlo de la siguiente forma:

> _assertTrue(“El título no es correcto.”,driver.getTitle().equals(“Título de mi página”));_

- **¿Cómo podemos simular la acción de mover el ratón encima de un elemento (mouse over) usando Selenium Webdriver?**

Selenium nos ofrece un gran rango de utilidades para crear iteraciones que simulan el comportamiento del usuario, como por ejemplo mover el ratón encima de un elemento o usar acciones de simular la acción de escribir o pulsar teclas del teclado. Para ello tenemos que usar la interfaz Action que es una utilidad de Selenium que es la que nos permite crear este tipo de interacciones del usuario.  Una forma de usar esta utilidad sería la siguiente:

> // Instanciamos la interfaz de Accion y le pasamos el driver:
>
> Actions actions=new Actions(driver);
>
> // Usamos el comando findElement para indicar el elemento al que queremos mover el ratón. Añadimos el comando perform para realizar la acción:
>
> actions.moveToElement(driver.findElement(By.id("id of the dropdown"))).perform();

- **¿Cómo podemos realizar capturas de pantalla usando Selenium?**

Para hacer capturas de pantalla debemos usar las clases File y FileUtils de la siguiente forma:

> // Código para realizar la captura de pantalla.
> File scrFile = ((TakesScreenshot)driver).getScreenshotAs(OutputType.FILE);
>
> //Guardamos en una cadena la fecha y hora para añadirla al nombre de la captura.
> String timestamp = new SimpleDateFormat("yyyy-MM-dd HH-mm-ss").format(new Date());
>
> // Una vez que la tengamos, debemos indicar la carpeta donde queremos guardarla:
> FileUtils.copyFile(scrFile, new File("C://CaptureScreenshot/screenshot\_"+timestamp+".png"));

- **¿Puede un captcha ser automatizado con Selenium Webdriver?**

No, los captcha no pueden ser automatizados usando Selenium.

- **¿Dónde podemos encontrar las diferentes versiones de Selenium y su changelog para saber los cambios y mejoras en cada versión?**

Podemos encontrar el changelog y las diferentes versiones de Selenium en su repositorio en Github: [https://github.com/SeleniumHQ/selenium](https://github.com/SeleniumHQ/selenium), seleccionamos el lenguaje en el que usemos Selenium (en mi caso Java) y hacemos click en changelog:

[https://github.com/SeleniumHQ/selenium/blob/master/java/CHANGELOG](https://github.com/SeleniumHQ/selenium/blob/master/java/CHANGELOG)

Ahí podemos encontrar todas las versiones de Selenium y los cambios de cada una de ellas.

- **¿Cómo podemos borrar las Cookies usando Selenium?**

Usando el método deleteAllCookies() de la forma:

> driver.manage().deleteAllCookies();

- **¿Podemos ejecutar código Javascript en Selenium?, ¿Cómo?**

Podemos ejecutar código javascript usando el comando JavaScriptExecuter. Lo haremos de la siguiente forma:

> ((JavascriptExecutor)driver).executeScript("{JavaScript Code}");

- **¿Qué es TestNG?**

TestNG(NG es de " _Next Generation_") es un framework para testing que se puede usar con Selenium y otras herramientas de automatización para proveer capacidades como: aserciones, reportes, ejecución paralela de test...

- **¿Cuáles son las ventajas de TestNG?**

Algunas de las ventajas de usar TestNG son:

1. TestNG provee diferentes aserciones que nos ayudarán a comprobar los resultados esperados y actuales de los test.
1. Provee ejecución paralela de test.
1. Se puede definir dependencias sobre test.
1. Podemos asignar una prioridad a los test definidos en Selenium para ejecutarlos según prioridad.
1. Nos permite agrupar test cases en grupos de test para crear suites.
1. Nos permite realizar data driven testing usando la anotación @DataProvider.
1. Tenemos la posibilidad de realizar reports cuando termine la ejecución de los test.

- **¿Cuáles son las aserciones que nos provee TestNG?**

Algunas de las aserciones que provee TestNG son las siguientes:

1. assertEquals(String actual, String expected, String message): assert para comparar si dos parámetros son iguales.
1. assertNotEquals(double data1, double data2, String message): assert para comparar si dos parámetros no son iguales.
1. assertFalse(boolean condition, String message): assert para comparar si una condición es falsa.
1. assertTrue(boolean condition, String message): assert para comparar si una condición es verdadera.
1. assertNotNull(Object object): assert para comparar si un objeto no es nulo.

* * *

Y hasta aquí las preguntas sobre Selenium Webdriver. En las próximas entradas comenzaremos a hablar de Jenkins: qué es, para qué sirve, cómo instalarlo, cómo configurar un job...

¡Hasta la próxima entrada!
