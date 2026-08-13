---
title: '068 - Pruebas Unitarias (V): Ejemplo de la calculadora en JavaScript + Jasmine'
date: '2021-02-17T08:30:00+00:00'
url: /2021/02/17/068-pruebas-unitarias-v-ejemplo-de-la-calculadora-en-javascript-jasmine/
image: /img/blog-images/old-post/2021/02/foto65.png
categories:
- automation
- best-practices
- code-quality
- qa
tags:
- calculator
- jasmine
- javascript
- testing
author: estefafdez
---
¡Hola a todos!

Bienvenidos a una nueva entrega de pruebas unitarias, en este artículo haremos la misma prueba de la calculadora que en el anterior artículo pero esta vez utilizando Javascript y Jasmine. ¡Comenzamos!

## Aclaración importante antes de seguir:

No soy una experta en JavaScript, de hecho mi stack habitual siempre ha sido Java aunque poco a poco (con Cypress) me estoy migrando cada vez más a JS, así que si ves algún error en esta entrada, por favor, añade un comentario para mejorarlo y corregirlo para todos. ¡Gracias!

## ¿Qué necesitas?

- Tener instalado Node y NPM en tu ordenador.
- Tener un IDE: yo usaré VSCode.

## ¿Cómo empezar?

Podemos comenzar de dos formas: creando un proyecto NPM desde cero y crear tu la estructura o utilizar el proyecto que ya he creado para ti y que puedes descargarte en el siguiente enlace:

[https://github.com/estefafdez/unit-test-javascript](https://github.com/estefafdez/unit-test-javascript)

## Entendiendo Jasmine y sus anotaciones.

Antes empezar de lleno y, teniendo el proyecto delante, vamos a hablar de varios conceptos antes de empezar a meternos de lleno en el proyecto.

### **¿Qué es Jasmine?**

Jasmine es un framework de testing pensado para el BDD (Behavior Driven Development) de JavaScript. Una de las cosas buenas que tiene es que no necesita un navegador o DOM para ejecutarse o ningún framework de JavaScript integrado, además puede usarse en cualquier proyecto que esté escrito en JavaScript o Nodejs. La sintaxis y los tests son bastante fáciles de leer y entender, lo que lo hace un framework bastante simple para empezar a hacer test unitarios.

Si queréis más info sobre Jasmine y su historia podéis entrar su repositorio oficial en Github: https://github.com/jasmine/jasmine.

### **Anotaciones a tener en cuenta en Jasmine:**

**describe()**

Este comando agrupa los test. Necesita dos argumentos, el primero es el nombre del grupo de test y el segundo es la función de callback que vamos a ejecutar.

**it()**

Utilizamos esta etiqueta para designar a un test individual. También necesita dos argumentos: el primero es el nombre del test como tal y el segundo es la función callback que contiene el test actual.

## Entendiendo la estructura del proyecto.

**¿Cómo hemos creado este proyecto?**

- Primero he creado un proyecto nuevo de npm mediante el comando _[npm init.](https://docs.npmjs.com/cli/v6/commands/npm-init)_
- Después de seguir todas las instrucciones hasta terminar de crear el repositorio, he instalado Jasmine con el siguiente comando:

```
npm i jasmine
```

- Una vez que tenemos Jasmine listo para usarse, comprobaremos que Jasmine nos ha creado varios ficheros:
  - **spec**: este directorio se crea por defecto para crear el código de test.
  - **support**: este directorio contiene un fichero _jasmine.json_ donde se pondrán las especificaciones de Jasmine.
- A continuación crearemos la clase de la calculadora con el código con las diferentes operaciones. El código lo crearemos en la raíz del proyecto en la clase _Calculator.js._ Esta clase incluirá las operaciones: suma, resta, multiplicación y división.
- En el fichero de spec, crearemos una clase _test.spec.js_ donde crearemos los tests.
- Crearemos un fichero _index.html_ en la raíz para ejecutar los tests y ver los resultados. Este fichero incluirá lo siguiente:
  - En el _head_ del fichero añadiremos las dependencias de jasmine.
  - En el _body_ del fichero añadiremos dónde están localizados tanto el código como los tests.

**La clase de los tests:**

En esta clase tendremos varias cosas a tener en cuenta:

- Crearemos dos variables con dos números para generar dos números aleatorios cada vez que se ejecuten los tests.
- Usaremos estas variables en los enunciados de los tests para saber los números que estamos utilizando para las diferentes operaciones.
- Haremos una aserción con **expect** para comprobar que el resultado de cada operación es el correcto.

## ¿Cómo ejecutar los test?

Para ejecutar los tests simplemente abre el fichero _index.html_ y actualiza el fichero. Al tener números aleatorios generados en cada iteración, veréis las operaciones y los resultados de los tests.

{{< figure src="/img/blog-images/old-post/2021/02/image.png?w=948" alt="" caption="" >}}

Y hasta aquí esta entrada sobre testing unitario con JavaScript y Jasmine.

¡Nos leemos en la siguiente entrada!
