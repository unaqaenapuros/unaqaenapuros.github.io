---
title: 006 - Diferencias entre validación y verificación.
date: '2017-05-29T07:42:05+00:00'
url: /2017/05/29/006-diferencias-entre-validacion-y-verificacion/
image: /img/blog-images/wp-posts/2017/05/foto6.jpg
categories:
- qa
tags:
- validation
- verification
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a hablar de dos conceptos que a menudo se confunden y que hay que tener claros a la hora de revisar un defecto. ¡Comenzamos!

La _validación y verificación (V&V)_ es el nombre que se da a los procesos de comprobación y análisis que aseguran que el software que se ha desarrollado es acorde a sus especificaciones y cumple con las necesidades del cliente. También debemos de tener en cuenta que ambas sirven para los siguientes propósitos en común:

- Primero, ambas nos sirven para facilitar la detección temprana y la corrección de posibles errores que se hayan cometido en el proceso de desarrollo.
- Segundo, ambas favorecen y fomentan la intervención de las partes implicadas en todas las fases del proceso (Devs, QA, PO...)
- Tercero, ambas proporcionan medidas de apoyo en el proceso de mejorar el cumplimiento de los requisitos que se han establecido.

Para definirlas de forma más concreta, vamos a usar una de las definiciones más conocidas, la de Boehm (1979):

#### Validación:

 _**¿Estamos construyendo el producto concreto?**_
La validación es un proceso mas general. Se debe asegurar que el software
cumple las expectativas del cliente. Va mas allá de comprobar si el
sistema está acorde con su especificación, para probar que el software
hace lo que el usuario espera a diferencia de lo que se ha especificado.

#### Verificación:

 **_¿Estamos construyendo el producto correctamente?_**
El papel de la verificación comprende comprobar que el software está de
acuerdo con su especificación. Se comprueba que el sistema cumple los
requerimientos funcionales y no funcionales que se le han especificado.

Es importante llevar a cabo la **validación** de los requerimientos del sistema en el inicio del proyecto ya que es fácil cometer errores durante la fase de análisis de requerimientos del sistema y, si estos errores se producen en estos casos, el software desarrollado no cumplirá con las necesidades del cliente. No obstante debemos de tener en cuenta que la validación de los requerimientos no puede descubrir todos los
problemas que pueda presentar la aplicación. Algunos defectos en los requerimientos solo pueden descubrirse cuando el sistema esté implementado de forma completa.

Espero que después de esta entrada haya quedado claro la diferencia entre ambos conceptos y tengamos en mente la pregunta que debemos hacernos en cada caso.

¡Nos leemos en la siguiente entrada!
