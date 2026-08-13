---
title: 074 - Pruebas de rendimiento (I)
date: '2021-06-09T07:00:00+00:00'
url: /2021/06/09/074-pruebas-de-rendimiento-i/
image: /img/blog-images/old-post/2021/04/foto71.png
categories:
- mobile-apps
- automation
- best-practices
- ci
- code-quality
- qa
- test-types
tags:
- performance
- pruebas
- rendimiento
- testing
author: estefafdez
---
¡Hola a todos!

En esta nueva serie de post comenzamos con las pruebas de rendimiento y toda la información sobre ellas.

¡Comenzamos!

## ¿Qué son las pruebas de rendimiento?

Las pruebas de rendimiento son las pruebas que se realizan, desde una perspectiva, para determinar lo rápido que realiza una tarea un sistema en condiciones particulares de trabajo. También puede servir para validar y verificar otros atributos de la calidad del sistema, tales como la escalabilidad, fiabilidad y uso de los recursos.

Las pruebas de rendimiento son un subconjunto de la ingeniería de pruebas, una práctica informática que se esfuerza por mejorar el rendimiento, englobando en el diseño y la arquitectura de un sistema, antes incluso del esfuerzo inicial de la codificación.

{{< figure src="/img/blog-images/old-post/2021/04/96.png?w=480" alt="" caption="" >}}

Pueden servir para diferentes propósitos. Pueden demostrar que el sistema cumple los criterios de rendimiento. Pueden comparar dos sistemas para encontrar cual de ellos funciona mejor. O pueden medir qué partes del sistema o de carga de trabajo provocan que el conjunto rinda mal. Para su diagnóstico, se utilizan herramientas como pueden ser monitorizaciones que midan qué partes de un dispositivo o software contribuyen más al mal rendimiento o para establecer niveles (y umbrales) del mismo que mantenga un tiempo de respuesta aceptable.

Es fundamental para alcanzar un buen nivel de rendimiento de un nuevo sistema, que los esfuerzos en estas pruebas comienzan en el inicio del proyecto de desarrollo y se amplíe durante su construcción. Cuanto más se tarde en detectar un defecto de rendimiento, mayor es el coste de la solución. Esto es cierto en el caso de las pruebas funcionales, pero mucho más en las pruebas de rendimiento, debido a que su ámbito de aplicación es de principio a fin.

El entorno de pruebas de rendimiento no debe cruzarse con pruebas de aceptación de usuarios ni con el entorno de desarrollo. Esto es tan peligroso que si las pruebas de aceptación de usuarios, o las pruebas de integración o cualquier otra prueba se ejecutan en el mismo entorno, entonces los resultados no son fiables. Como buena práctica, siempre es aconsejable disponer de un entorno de pruebas de rendimiento lo más parecido como se pueda al entorno de producción.

Y hasta aquí esta entrada. En las siguientes seguiremos profundizando más en este tipo de pruebas.

¡Hasta la siguiente entrada!
