---
title: 058- Prueba técnica de QA.
date: '2019-10-09T07:00:21+00:00'
url: /2019/10/09/058-prueba-tecnica-de-qa/
image: /img/blog-images/wp-posts/2019/09/foto55.png
categories:
- automation
- profiles
- qa
tags:
- test-case
- technical-test
- profiles
- selenium
- testing
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a hablar de una posible prueba técnica para seleccionar a los candidatos que entran al departamento de QA. ¡Comenzamos!

## ¿Por qué hacer una prueba técnica?

Cuando estamos en un proceso de selección para incorporar a alguien en el equipo, necesitamos conocer a esa persona, no sólo en una entrevista personal, sino también necesitamos tener referencias de nuestros candidatos y de la forma en la que trabajan.

Para ello, os presento las dos pruebas que suelo hacer a los candidatos, una para la parte más funcional y otra para la de automatización (que tendrá que hacer ambas pruebas).

Lo que se pretende es conseguir es cuanta más información posible de la forma en la que trabajan, se organizan, se definen los casos de prueba... para tener una visión del candidato y de si es el correcto para el equipo o no.

### Prueba técnica perfil funcional.

Visita la web de _**--TU-EMPRESA--**_ y crea los 5 casos de prueba de aceptación más importantes que harías en la web para asegurarte de que la subida a producción de la nueva versión ha sido correcta.

Utiliza el siguiente formato:

- Título del test.
- Tipo de prueba: en este caso aceptación.
- Prioridad.
- Tecnología: Android, iOS, Web...
- Pre-condiciones: si necesito cumplir alguna.
- Descripción.
- Pasos a reproducir con resultado esperado (detállalos lo máximo posible). Por ejemplo:

PasoResultadoIr a la web de _**--TU-EMPRESA--**_La web se muestra correctamente en el navegador.

### Prueba técnica automático.

Después de haber definido los casos de prueba de aceptación mínimos que necesitas, crea un proyecto Maven con las siguientes características:

- Proyecto **Maven** con **Java**
- Añade **Selenium** y las dependencias necesarias para ejecutar el proyecto.
- Añade como navegador **Firefox** para lanzar las pruebas.
- Utiliza el **Modelo Base Page Object** para organizar la estructura de tu proyecto.
- Desarrolla los **5 test de aceptación** que has definido anteriormente de forma automática, no te olvides de:

  - Si haces una comprobación **(check)** utilizar **Assert** con un mensaje explicativo.
  - Utiliza el **Javadoc** en cada uno de los métodos.
  - Cierra el navegador cuando termine cada caso de prueba.
- Crea una suite en **TestNG o JUnit** para lanzar todas las pruebas.
- Analiza tu código con **Sonar** y corrige los defectos encontrados. Manda captura de los resultados del análisis.
- Cuando termines el proyecto, súbelo a **Gitlab/Github/** y comparte el repositorio.
- Crear un fichero **README.MD** en el repositorio explicando cómo lanzar los test y la estructura del proyecto.

* * *

Y hasta aquí la entrada con la prueba técnica, he de decir que me ha ayudado mucho a la hora de elegir a los candidatos y ver la forma de trabajo de las diferentes personas así como la forma en la que definen las pruebas. Espero que os ayude a encontrar a los mejores candidatos para vuestro equipo.

¡Nos leemos en la siguiente entrada!
