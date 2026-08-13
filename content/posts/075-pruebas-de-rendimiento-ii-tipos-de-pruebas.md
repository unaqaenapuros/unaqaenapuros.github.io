---
title: '075 - Pruebas de rendimiento (II): Tipos de pruebas.'
date: '2021-06-30T07:00:00+00:00'
url: /2021/06/30/075-pruebas-de-rendimiento-ii-tipos-de-pruebas/
image: /img/blog-images/old-post/2021/04/foto72.png
categories:
- appmóviles
- automation
- buenas-prácticas
- code-quality
- qa
tags:
- load-testing
- performance
- rendimiento
- scalability-testing
- soak-testing
- stress-testing
- testing
- tipos-de-pruebas
- volume-testing
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a hablar de los tipos de pruebas de rendimiento. ¡Comenzamos!

## Tipos de pruebas de rendimiento.

{{< figure src="/img/blog-images/old-post/2021/04/performancetesting-07.png?w=503" alt="" caption="" >}}

Algunas de las pruebas que pueden realizarse son:

### Prueba de carga.

Este es el tipo más sencillo de pruebas de rendimiento. Una prueba de carga se realiza generalmente para observar el comportamiento de una aplicación bajo una cantidad de peticiones esperada. Esta carga puede ser el número esperado de usuarios concurrentes utilizando la aplicación y que realizan un número específico de transacciones durante el tiempo que dura la carga. Esta prueba puede mostrar los tiempos de respuesta de todas las transacciones importantes de la aplicación. Si la base de datos, el servidor de aplicaciones, etc... también se monitorizan, entonces esta prueba puede mostrar el cuello de botella en la aplicación.

### Prueba de estrés.

Esta prueba se utiliza normalmente para romper la aplicación. Se va doblando el número de usuarios que se agregan a la aplicación y se ejecuta una prueba de carga hasta que se rompe. Este tipo de prueba se realiza para determinar la solidez de la aplicación en los momentos de carga extrema y ayuda a los administradores para determinar si la aplicación rendirá lo suficiente en caso de que la carga real supere a la carga esperada.

### Prueba de estabilidad (soak testing).

Esta prueba normalmente se hace para determinar si la aplicación puede aguantar una carga esperada continuada. Generalmente esta prueba se realiza para determinar si hay alguna fuga de memoria en la aplicación.

### Prueba de pico (spike testing).

La prueba de picos, como el nombre sugiere, trata de observar el comportamiento del sistema variando el número de usuarios, tanto cuando bajan, como cuando tiene cambios drásticos en su carga. Esta prueba se recomienda que sea realizada con un software automatizado que permita realizar cambios en el número de usuarios mientras que los administradores llevan un registro de los valores a ser monitorizados.

Y hasta aquí esta entrada, ¡nos leemos en las siguientes!
