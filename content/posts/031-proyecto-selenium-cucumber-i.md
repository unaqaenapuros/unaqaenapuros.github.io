---
title: 031 - Proyecto Selenium - Cucumber (I).
date: '2017-10-11T07:00:33+00:00'
url: /2017/10/11/031-proyecto-selenium-cucumber-i/
image: /img/blog-images/old-post/2017/09/foto31.jpg
categories:
- appium
- automation
- code-quality
- cucumber
- git
- qa
- selenium-webdriver
tags:
- bdd
- gherking
- selenium-3
author: estefafdez
---
¡Hola a todos!

En esta entrada hablaremos del proyecto [Selenium-Cucumber](https://github.com/estefafdez/selenium-cucumber). ¡Comenzamos!

![a.png](/img/blog-images/old-post/2017/08/a.png)

Este proyecto propio fue llevado a cabo con [Francisco Fernández González](https://www.linkedin.com/in/francisco-fern%C3%A1ndez-gonz%C3%A1lez-71b178115/), gran compañero y amigo.

* * *

### URL Repositorio: [https://github.com/estefafdez/selenium-cucumber](https://github.com/estefafdez/selenium-cucumber)

* * *

### ¿Por qué hacer este proyecto?

Este proyecto surge, primero, de poder tener un "core" propio donde poder ejecutar pruebas usando Selenium Webdriver 3 en cualquier sistema operativo y cualquier navegador simplemente cambiando las configuraciones necesarias en el fichero pom.xml y segundo, para poder aprender Cucumber y cómo trabajar con él en el desarrollo de test automáticos con Selenium.

Comenzaremos con una definición de los _conceptos necesarios_ que debemos comprender antes de pasar a hablar del proyecto.

### ¿Qué es Cucumber?

 [**Cucumber**](https://cucumber.io/) es una herramienta creada en 2008 por Aslak Hellesoy para implementar metodologías como el _Behaviour Driven Development (BDD)_, que permite ejecutar descripciones funcionales en texto plano como pruebas de software automatizadas.

Estas descripciones funcionales de casos de prueba, se escriben en un lenguaje específico de dominio, legible por el área de negocio, denominado “ **Gherkin**”, el cual sirve simultáneamente como documentación de apoyo al desarrollo y de las pruebas automatizadas.

### Behaviour Driven Development (BDD).

Behavior-Driven Development ​​o BDD es un proceso de desarrollo software que busca unir la parte técnica y la de negocio mediante un lenguaje común (Gherkin), en el cual se escriben las pruebas de aceptación que se basan en las historias de usuario que necesitemos automatizar. ¿Cómo lo hacemos? mediante escenarios.

¿Cómo definimos un escenario?

> **Given** \[contexto inicial del escenario\], **when** \[evento\], **then** \[resultado\]

Un ejemplo de escenario (contenido en este proyecto) podría ser:

![escenario.png](/img/blog-images/old-post/2017/08/escenario.png)

Como vemos, un lenguaje sencillo de entender tanto para la parte técnica como para la de negocio.

### Gherkin, ¿Cómo lo uso?.

Gherkin es un lenguaje creado para ser comprensible y fácil de leer, tanto para la parte técnica como a la de negocio y con el que vamos a describir las funcionalidades, dependiendo del comportamiento del software, sin entrar en su implementación.

¿Cuáles son las **sentencias** que debemos usar en Gherkin?:

- **Feature**: Indica el nombre de la funcionalidad que vamos a probar de una forma clara y expícita. A partir de esta funcionalidad, comenzaremos a construir nuestros escenarios de prueba.
- **Scenario**: Describe cada escenario que vamos a probar.
- **Given**: Esta sentencia provee el contexto en el cual el escenario se va a ejecutar dentro del test. También podemos describir los pre-requisitos en él y toda la información necesaria para comenzar el test.
- **When**: Especifica el conjunto de acciones que lanzan el test dentro de un escenario, definiendo así la interacción del usuario que acciona la funcionalidad que deseamos probar.
- **Then**: Especifica el resultado esperado en el test.

Para probar de forma correcta una funcionalidad, crearemos distintos escenarios con las diferentes pruebas de aceptación que necesitamos cumplir hasta pasar una historia de usuario completa.

* * *

### Selenium-Cucumber.

Una vez que tenemos en la cabeza los conceptos en los que nos basamos, vamos a comentar el proyecto y toda la lógica interesante de éste.

#### Descargamos el proyecto:

Creamos un fork del repositorio del proyecto (indicado más arriba) y clonamos el repositorio:

> git clone https://github.com/XXXX/selenium-cucumber

Una vez que tenemos el proyecto descargado, lo importamos en nuestro IDE favorito, en mi caso lo haré en Eclipse, y vemos la estructura del proyecto:

![estructura.png](/img/blog-images/old-post/2017/08/estructura.png)

1. **Configure Environment**: en este paquete se encuentran las clases de configuración en las que definiremos una factoría de Drivers (para los diferentes navegadores), un manejador de properties y una clase de inicialización del Driver.
1. **SauceLabs**: un WIP para la integración de SauceLabs en el proyecto para lanzar los test en remoto.
1. **Step Definitions**: en este paquete encontremos las clases con una serie de pasos previamente definidos simplemente para ser usados.
1. **Features**: en este paquete encontraremos las diferentes features del proyecto.
1. **Files/Software**: En este directorio tenemos una serie de sub-directorios divididos por sistemas operativos en el que encontraremos los drivers necesarios por sistema operativo para cada navegador.
1. **Selectors**: en este directorio encontraremos los ficheros .properties con los selectores de los elementos que necesitamos.
1. **log4j.properties y test.properties**: son dos ficheros de configuración para definir el nivel de log y las propiedades de los test.

El **pom.xml** también está incluido dentro de la estructura del proyecto.

Y esto es todo por esta entrada, en la siguiente comenzaremos a explicar cada una de los clases en las diferentes secciones y el pom.xml para entender cómo ejecutar los test en cualquier sistema operativo con cualquier navegador.

¡Hasta la siguiente entrada!
