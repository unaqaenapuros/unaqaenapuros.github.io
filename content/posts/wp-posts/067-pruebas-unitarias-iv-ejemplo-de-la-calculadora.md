---
title: '067- Pruebas Unitarias (IV): Ejemplo de la calculadora.'
date: '2020-12-23T08:30:00+00:00'
url: /2020/12/23/067-pruebas-unitarias-iv-ejemplo-de-la-calculadora/
categories:
- mobile-apps
- automation
- best-practices
- code-quality
- git
- qa
tags:
- quality
- unit-test
author: estefafdez
---
  
{{< gallery cols="1" >}}  
{{< figure src="/img/blog-images/wp-posts/2020/11/foto64.png?w=1024" alt="" caption="" >}}  
{{< /gallery >}}  

¡Hola a todos!

En esta nueva entrada vamos a ver un ejemplo real de un proyecto con test unitarios en Java usando Eclipse y JUnit para hacer nuestros test unitarios. ¡Comenzamos!

## ¿Qué necesitas?

- Tener instalado Java en tu ordenador.
- Tener un IDE: yo usaré Eclipse.

## ¿Cómo empezar?

Podemos comenzar de dos formas: creando un proyecto Java desde cero y crear tu las clases o utilizar el proyecto que ya he creado para ti y que puedes descargarte en el siguiente enlace:

https://github.com/estefafdez/unit-test-java-junit

Antes de comenzar recuerda siempre hacer un **fork** del repositorio y clonarlo a tu entorno local para hacerlo más fácil y, si quieres, hacer algún PR a mi repositorio con mejoras.

Una vez que tenemos el **fork** creado y el clone realizado, podemos importar el proyecto en nuestro IDE, en mi caso Eclipse.

## Importar el proyecto:

Para importar un proyecto en Eclipse hacemos click en File -> Import -> Existing Projects into Workspace:

{{< figure src="/img/blog-images/wp-posts/2020/11/75.png?w=417" alt="" caption="" >}}

{{< figure src="/img/blog-images/wp-posts/2020/11/76.png?w=540" alt="" caption="" >}}

Seleccionamos la carpeta donde hemos guardado el proyecto y hacemos click en Finalizar:

{{< figure src="/img/blog-images/wp-posts/2020/11/77.png?w=733" alt="" caption="" >}}

Una vez que lo importamos tendremos la siguiente estructura en el proyecto:

{{< figure src="/img/blog-images/wp-posts/2020/11/screenshot-2020-11-04-at-13.51.28.png?w=532" alt="" caption="" >}}

## Entendiendo las anotaciones de JUnit:

Antes de comenzar con la estructura de paquetes del proyecto tenemos que hablar de las anotaciones en JUnit. Las que hemos usado y las más importantes son las siguientes:

- **@Test:** Anotación que deben llevar todos los test.
- **@Before:** métodos que serán invocados antes de cada test
- **@BeforeClass:** métodos que serán invocados antes de ejecutar los test.
- **@After:** métodos que serán invocados después de cada test
- **@AfterClass:** métodos que serán invocados después de ejecutar los test.
- **@Ignore:** sirve para marcar que un test no debe ser tenido en cuenta a la hora de ejecutar los test unitarios.

## Entendiendo la estructura del proyecto:

Una vez entendido para qué sirven las anotaciones, pasaremos a definir la estructura del proyecto. En este proyecto tenemos dos paquetes:

- El primero, **calculadora**, es el código desarrollado, que en este caso es una Calculadora con varias operaciones: sumar, restar, multiplicar y dividir.
- El segundo, **calculadora.test**, es el paquete en el que crearemos las clases de test. Por ahora tenemos 3 ficheros:
  - **CalculadoraBaseTest:** esta clase es una clase en la que definiremos las funciones genéricas para todos los test, en este caso:
    - _setUpClass:_ Es el método que se ejecuta antes de ejecutar los test. En ella se ve un mensaje para que en el log se muestra que se están empezando a ejecutar los test unitarios.
    - _setUp:_ Es el método que se ejecuta antes de cada test y en el que incluiremos un mensaje con el nombre del test que se está ejecutando.
    - _tearDownClass:_ Es el método que se ejecuta después de ejecutar todos los test. En ella se ve un mensaje para que en el log se muestra que han terminado de ejecutar los test unitarios.
    - _tearDown:_ Es el método que se ejecuta antes de después test y en el que incluiremos un mensaje con el nombre del test que se acaba de ejecutar.
  - **CalculadoraSumaTest:** Clase Test en la que definiremos los test para la operación suma de la calculadora. Extendemos de la clase base (CalculadoraBaseTest) para que se ejecuten los métodos que hemos definido antes y después de la clase y de los test.
  - **CalculadoraRestaTest:** Clase Test en la que definiremos los test para la operación resta de la calculadora. Extendemos de la clase base (CalculadoraBaseTest) para que se ejecuten los métodos que hemos definido antes y después de la clase y de los test.

Si JUnit no está añadido en el proyecto, lo tenemos que añadir de la siguiente forma: Seleccionamos el proyecto -> Build Path -> Configure Build Path.

A continuación hacemos click en Add library -> JUnit.

{{< figure src="/img/blog-images/wp-posts/2020/11/screenshot-2020-11-04-at-13.58.08.png?w=1024" alt="" caption="" >}}

Y ya podemos usarla para ejecutar nuestros test.

## **¿Cómo ejecutar los test?**

Para ejecutar los test con JUnit nos iremos o bien al test (si queremos probar un test concreto) o a la clase, y haremos click en el botón derecho y Run As -> JUnit Test.

{{< figure src="/img/blog-images/wp-posts/2020/11/80.png?w=737" alt="" caption="" >}}

Una vez terminados de ejecutar, podremos comprobar los resultados:

{{< figure src="/img/blog-images/wp-posts/2020/11/81.png?w=1024" alt="" caption="" >}}

Tenéis varios tests en el proyecto sobre la suma y la resta, cualquier PR con nuevas operaciones en la calculadora y nuevos tests son bienvenidos :)

¡Hasta la siguiente entrada!
