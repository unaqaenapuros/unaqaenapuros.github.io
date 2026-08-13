---
title: 022 - Selenium Webdriver.
date: '2017-08-09T07:00:20+00:00'
url: /2017/08/09/022-selenium-webdriver/
image: /img/blog-images/old-post/2017/07/foto22.jpg
categories:
- automation
- qa
- selenium-webdriver
tags:
- selectors
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a hablar de Selenium Webdriver...¡Comenzamos!

**Selenium WebDriver** es una herramienta que está diseñada para ejecutar las pruebas automáticas en los principales navegadores (IE, Chrome, Firefox y Opera). Utiliza lenguajes como Python, Ruby, Java y C#. La licencia de esta herramienta es Apache 2.0.

Una de las ventajas de usar Selenium WebDriver frente a Selenium IDE son los controladores nativos que incluye, que dan soporte a distintos navegadores (Internet Explorer, Firefox, Chrome y próximamente Opera y Safari).

Debemos tener en cuenta que Selenium es una herramienta que nos permite escribir una prueba que se ejecuta en un navegador y que emula el comportamiento de un usuario: ve a la web xxx.com, busca el botón x, haz click en...

Para comprender mejor cómo trabajar con Selenium, vamos a hacer una lista de los comandos básicos más utilizados y que debemos de conocer:

### Crear una nueva instancia del driver:

```java
WebDriver driver = new FirefoxDriver();
```

también podemos crear instancias de ChromeDriver, InternetExplorerDriver o SafariDriver.

### Navegar a una página.

Una vez que tenemos el driver podemos usarlo para navegar a una página concreta con la siguiente línea:

```java
driver.navigate().to("www.google.com");
```

### Buscar elementos:

Buscar elemento por ID:

```java
driver.findElement(By.id("ID_elemento"));
```

Buscar elemento por clase:

```java
driver.findElement(By.className("className_elemento"));
```

Buscar elemento por tag:

```java
driver.findElement(By.tagName("tag_name"));
```

Buscar elemento por nombre:

```java
driver.findElement(By.name("name_element"));
```

Buscar elemento por CSS selector:

```java
driver.findElement(By.cssSelector("selector"));
```

Buscar elemento por Xpath:

```java
driver.findElement(By.xpath("xpathExpression"));
```

Buscar el texto visible de un HyperLink:

```java
driver.findElement(By.linkText("linkText"));
```

Buscar el texto visible parcial de un HyperLink:

```java
driver.findElement(By.partialLinkText("linkText"));
```

### Hacer click.

Para hacer click en un elemento primero tenemos que buscar el elemento al que queremos hacer click y después mandar la orden de click:

```java
WebElement element = driver.findElement(By.id("ID_elemento1"));

element.click();
```

### Escribir un texto

Para escribir un texto debemos primero hacer click en el cuadro de texto donde queramos escribir este texto y luego mandar la orden de escribir el texto que queramos. Es muy recomendable usar el comando clear(); antes de enviar el texto para limpiar así el cuadro de texto antes de escribirlo.

```java
WebElement element = driver.findElement(By.id("ID_elemento1"));

element.click(); //Hacemos click

element.clear(); //limpiamos el cuadro de texto

element.sendKeys("Mi Texto"); //enviamos el texto
```

Y hasta aquí esta entrada de Selenium. En la siguiente entrada hablaremos de los xpath y cómo seleccionarlos para conseguir xpath robustos y portables.

¡Hasta la siguiente entrada!
