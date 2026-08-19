---
title: 020 - Buenas prácticas en el diseño de Test Automáticos con Selenium Webdriver.
date: '2017-07-26T07:00:05+00:00'
url: /2017/07/26/020-buenas-practicas-en-el-diseno-de-test-automaticos-con-selenium-webdriver/
image: /img/blog-images/old-post/2017/07/foto20.jpg
categories:
- qa
- selenium-webdriver
tags:
- best-practices
- selenium
- testing
- webdriver
author: estefafdez
---
¡Hola a todos!

Para seguir con el tema de las buenas prácticas, en esta entrada vamos a hablar de las buenas prácticas en cuanto al diseño de Test Automáticos con Selenium Webdriver...¡Comenzamos!

### Haz siempre tu código legible.

Para ello utiliza métodos claros, devuelve siempre "this", usa métodos "void". Devuelve argumentos genéricos y con nombres auto-descriptivos

```java
@Test
public void openPageWithoutErrors() throws Exception {
MainPage main = openMainPage();
main.hasNumberOfErrors(1);
main.withCampaignName("SELENIUM").save();
main.hasNumberOfErrors(2);
}
```

### Sé robusto y portable a la hora de seleccionar los elementos.

- Evita siempre seleccionar un elemento usando el xpath generado por herramientas como Firepath. Crea siempre tus selectores de la forma más robusta y portable posible.
- Intenta seleccionar siempre un elemento mediante su: id > name > css > xpath.
  - Seleccionar por id y por nombre son, a menudo, la forma más fácil y segura de seleccionar un elemento.
  - Selecciona un elemento por xpath cuando necesites que contenga un texto específico.
  - Usa siempre los selectores css junto al id o el nombre del elemento.
  - Si tenemos problemas seleccionando los links en una aplicación, podemos usar las href parciales.

### Evita usar siempre Thread.sleep, usa Wait o FluentWait.

Sabemos que a veces debemos decirle a Selenium que espere antes de realizar alguna acción. Debemos intentar utilizar siempre métodos como Wait o FluentWait.

```java
public void clickOnContactType() {
driver.findElement(By.id("contacttypelink")).click();
SeleniumUtil.fluentWait(By.name("handle"), getDriver());
}
```

### Usa siempre URLs relativas.

Sabemos que hay veces que necesitamos decirle a Selenium que se vaya a una ruta concreta, pero siempre debemos evitar código como:

```java
driver.get("http://es.wikipedia.org/wiki/Wiki");
```

### Crea tu propio set de datos.

No asumas que los datos siempre van a estar ahí, crea un fichero con los datos necesarios para los test automáticos:

```java
CreatePage createPage = openCreatePage();
createPage.withName("SELENIUM" + new DateTime()).withAgent("tom").withAssignee("tom");
createPage.save().hasNumberOfErrors(0);
createPage.hasInfoMessage();
Long campaignId = createPage.getCampaignId();
ConsultPage consult = openConsultPage(campaignId);
EditPage edit = consult.goToEditPage();
consult = edit.save();
consult.hasInfoMessage();
```

### Mantén el proyecto actualizado.

Ten siempre el proyecto de test automáticos actualizado tanto las librerías que uses como la versión de Selenium (y su compatibilidad con los navegadores).

En las siguientes entradas hablaremos de Selenium y de cómo empezar un proyecto usando Selenium Webdriver.

¡Nos leemos en la siguiente entrada!
