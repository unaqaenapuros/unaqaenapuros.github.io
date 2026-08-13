---
title: 025 - Selenium 102.
date: '2017-08-30T07:00:34+00:00'
url: /2017/08/30/025-selenium-102/
image: /img/blog-images/old-post/2017/07/foto25.jpg
categories:
- automation
- qa
- selenium-webdriver
tags:
- interview
- questions
- work
author: estefafdez
---
¡Hola a todos!

En esta entrada haremos una recopilación de preguntas acerca de Selenium Webdriver a la hora de enfrentarnos a una entrevista de trabajo....¡Comenzamos!

- **¿Qué es Selenium?**

Selenium es una herramienta de automatización de pruebas funcionales basada en el navegador. Es básicamente una biblioteca que puede utilizar en su programa para probar una aplicación web.

- **¿Qué versiones existen de Selenium?**

1. _Selenium WebDriver_ \- Se usa para la automatización de pruebas en aplicaciones web usando métodos en un navegador nativo.
1. _Selenium IDE_ \- Plugin de Firefox para grabar y ejecutar pruebas.
1. _Selenium Grid_ \-  Permite ejecutar test de selenium en paralelo a través de múltiples máquinas.

- **¿Qué lenguajes de programación soporta Selenium Webdriver?**

Los lenguajes soportados son: Java, C#, php, Ruby, Python.

- **¿Qué tipo de pruebas podemos realizar con Selenium Webdriver?**

Siempre haremos pruebas en aplicaciones web y pueden ser de dos tipos: pruebas funcionales y de regresión.

- **¿Cuáles son las limitaciones de Selenium?**

Las limitaciones principales de selenium son:

\- Sólo se pueden realizar pruebas en aplicaciones web, no para escritorio o móvil.

\- Los captcha y la lectura de códigos de barra no pueden ser automatizados con Selenium.

\- El usuario que vaya a realizar pruebas automáticas con Selenium debe tener conocimientos previos de programación en uno de los lenguajes soportados por Selenium.

- **¿Cuáles son los diferentes tipos de selectores que podemos usar para buscar un elemento con Selenium?**

Los selectores que podemos usar con Selenium son: ID, ClassName, Name, TagName, LinkText, PartialLinkText, Xpath, CSS Selector.

- **¿Qué es un XPath?**

Xpath (XML Path Language) es un lenguaje que permite recuperar información de un documento XML definiendo una sintaxis para establecer partes en un documento XML, permitiendo navegar a través de sus elementos y atributos, además permite manipular de forma básica booleanos, números y cadenas.

- **¿Qué diferencia hay entre / y // en una expresión Xpath?**

Usaremos / para empezar la selección desde un nodo en el documento. Nos permite crear expresiones Xpath absolutas.

Usaremos // para empezar la selección desde cualquier sitio del documento. Nos permite crear expresiones Xpath relativas.

- **¿Sabrías decirme qué es Selenese?**

Selenese es el lenguaje usado para escribir los test script en Selenium IDE.

- **¿Cómo se lanza una nueva instancia del navegador usando Selenium Webdriver?**

Siguiendo la siguiente sintaxis y dependiendo del navegador del que queramos crear una instancia, puede ser:

> _WebDriver driver =_ **_new_** _FirefoxDriver(); -> para Firefox_ _WebDriver driver =_ **_new_** _ChromeDriver(); -> para Chrome_ _WebDriver driver =_ **_new_** _InternetExplorerDriver(); -> Para IE._

- **¿Cuáles son los diferentes tipos de drivers soportados actualmente por Selenium Webdriver?**

Los diferentes drivers soportados son: Geckodriver (nuevo desde Selenium 3 para crear una instancia deFirefoxDriver), ChromeDriver, InternetExplorerDriver, SafariDriver, OperaDriver, AndroidDriver, IPhoneDriver, HtmlUnitDriver.

- **¿Cómo podemos escribir en un cuadro de texto usando Selenium Webdriver?**

Para poder escribir en un cuadro de texto primero tenemos que encontrar el elemento y luego usar el comando sendKeys de la siguiente forma:

> _WebElement element = driver_ _.findElement(By.class(_ _“textbox1”_ _));_ _element.sendKeys(_ _“This is a test”_ _);_

- **¿Cómo podemos comprobar que un elemento se muestra en la pantalla usando Selenium Webdriver?**

Webdriver nos facilita varios métodos que podemos utilizar para comprobar la visibilidad de un elemento web en la pantalla. Podemos comprobar la visibilidad de elementos como botones, cajas de texto, checkbox, radio button, etiquetas... Para ello usamos los comandos:

> **Comando isDisplayed():** **_boolean_** _buttonDisplayed = driver.findElement(By.id(_ _“button1”_ _)).isDisplayed();_ **Comando isSelected():** **_boolean_** _buttonSelected = driver.findElement(By.class(_ _“button2”_ _)).isSelected();_ **Comando isEnabled():** **_boolean_** _buttonEnabled = driver.findElement(By.id(_ _“button3”_ _)).isEnabled();_

- **¿Cómo podemos guardar el texto de un WebElement?**

Para poder guardar el texto de un elemento web primero tenemos que seleccionar el elemento que quedamos recoger el texto y usar el comando getText():

> _String errorText = driver.findElement(By.class(“error\_label”)).getText();_

Este comando sólo puede ser usado para elementos webs que contentan texto como por ejemplo: etiquetas, mensajes de verificación, botones, mensajes de error...

- **¿Cómo podemos seleccionar una opción de un dropdown usando Selenium Webdriver?**

Para poder seleccionar el valor de un dropdown usando Selenium Webdriver tenemos que usar la clase Select de Webdriver. Mediante esta clase podremos seleccionar un valor de un dropdown por: su valor, su texto visible o su número de index (posición).

Lo podemos ver más claro en el siguiente ejemplo de cada uno de ellos:

> **selectByValue:** _Select selectByValue =_ **_new_** _Select(_ _driver_ _.findElement(By.id(_ _“ID1”_ _)));_ _selectByValue.selectByValue(_ _“value1”_ _);_ **selectByVisibleText:** _Select selectByVisibleText =_ **_new_** _Select (_ _driver_ _.findElement(By.id(_ _“ID2”_ _)));_ _selectByVisibleText.selectByVisibleText(_ _“Text1”_ _);_ **selectByIndex:** _Select selectByIndex =_ **_new_** _Select(_ _driver_ _.findElement(By.id(_ _“ID3”_ _)));_ _selectByIndex.selectByIndex(2);_

Y hasta aquí esta entrada. En la siguiente seguiremos con nuestra recopilación de Selenium Webdriver y posibles preguntas que se pueden hacer en una entrevista de trabajo.

¡Hasta la siguiente entrada!
