---
title: 064- Pruebas Unitarias (I)
date: '2020-11-04T08:30:00+00:00'
url: /2020/11/04/064-pruebas-unitarias/
image: /img/blog-images/wp-posts/2020/10/foto61.png
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
¡Hola a todos!

En esta entrada y siguientes vamos a hablar de las pruebas unitarias. ¡Empezamos!

{{< figure src="/img/blog-images/wp-posts/2020/10/74.png?w=1024" alt="" caption="" >}}

Una **prueba unitaria** es una forma de comprobar el correcto funcionamiento de una unidad de código. Por ejemplo en diseño estructurado o en diseño funcional una función o un procedimiento, en diseño orientado a objetos una clase.

Esto sirve para asegurar que cada unidad funcione correctamente y eficientemente por separado. Además de verificar que el código hace lo que tiene que hacer, verificamos que sea correcto el nombre, los nombres y tipos de los parámetros, el tipo de lo que se devuelve, que si el estado inicial es válido entonces el estado final es válido

La idea es escribir casos de prueba para cada función no trivial o método en el módulo, de forma que cada caso sea independiente del resto. Luego, con las Pruebas de Integración se podrá asegurar el correcto funcionamiento del sistema o subsistema en cuestión.

## Características de las pruebas unitarias

Para que una prueba unitaria tenga la calidad suficiente se deben cumplir los siguientes requisitos:

### Objetivo

Es importante conocer claramente cuál es el objetivo del test. Cualquier desarrollador debería poder conocer claramente cuál es el objetivo de la prueba y su funcionamiento. Esto sólo se consigue si se trata el código de pruebas como el código de la aplicación. Aunque estos requisitos no tienen que ser cumplidos al pie de la letra, se recomienda seguirlos o de lo contrario las pruebas pierden parte de su función.

### Automatizable

Las pruebas unitarias se tienen que poder ejecutar sin necesidad de intervención manual. Esta característica posibilita que podamos automatizar su ejecución.

### Repetibles o Reutilizables

Las pruebas unitarias tienen que poder repetirse tantas veces como uno quiera. Por este motivo, la rapidez de las pruebas tiene un factor clave. Si pasar las pruebas es un proceso lento no se pasarán de forma habitual, por lo que se perderán los beneficios que éstas nos ofrecen.

### Independientes

Las pruebas unitarias tienen que poder ejecutarse independientemente del estado del entorno. Las pruebas tienen que pasar en cualquier ordenador del equipo de desarrollo. La ejecución de una prueba no puede afectar la ejecución de otra. Después de la ejecución de una prueba el entorno debería quedar igual que estaba antes de realizar la prueba Las diferentes relaciones que puedan existir entre módulos deben ser simulada para evitar dependencias entre módulos.

### Cobertura

Las pruebas unitarias deben poder cubrir casi la totalidad del código de nuestra aplicación. Una prueba unitaria será tan buena como su cobertura de código. La cobertura de código marca la cantidad de código de la aplicación que está sometido a una prueba. Por tanto, si la cobertura es baja, significa que gran parte de nuestro código está sin probar.

Y hasta aquí esta entrada, en la siguiente nos centraremos en las ventajas y limitaciones y algunas herramientas para realizarlas.

¡Nos leemos en la siguiente entrada!
