---
title: 065- Pruebas Unitarias (II)
date: '2020-11-25T08:30:00+00:00'
url: /2020/11/25/065-pruebas-unitarias-ii/
image: /img/blog-images/old-post/2020/10/foto62.png
categories:
- appmóviles
- automation
- buenas-prácticas
- code-quality
- git
- qa
tags:
- quality
- unit-test
author: estefafdez
---
¡Hola a todos!

Seguimos con las entradas de pruebas unitarias. En esta entrada hablaremos de las ventajas y limitaciones de este tipo de pruebas y algunas consideraciones sobre ellas. ¡Comenzamos!

## Ventajas

El **objetivo** de las pruebas unitarias es aislar cada parte del programa y mostrar que las partes individuales son correctas. Proporcionan un contrato escrito que el trozo de código debe satisfacer. Estas pruebas aisladas proporcionan cinco ventajas básicas:

### Fomentan el cambio

Las pruebas unitarias facilitan que el programador cambie el código para mejorar su estructura (refactorización), puesto que permiten hacer pruebas sobre los cambios y así asegurarse de que los nuevos cambios no han introducido errores.

### Simplifica la integración

Se reducen drásticamente los problemas y tiempos dedicados a la integración. En las pruebas se simulan las dependencias lo que nos permite que podamos probar nuestro código sin disponer del resto de módulos. Por experiencia puede decir que los procesos de integración son más de una vez traumáticos, dejándolos habitualmente para el final del proyecto. La frase “sólo queda integrar” haciendo referencia a que el proyecto está cerca de terminar suele ser engañosa, ya que el periodo de integración suele estar lleno de curvas.

### Documenta el código

Las pruebas nos ayudan a entender mejor el código, ya que sirven de documentación. A través de las pruebas podemos comprender mejor qué hace un módulo y que se espera de él. Separación de la interfaz y la implementación Dado que la única interacción entre los casos de prueba y las unidades bajo prueba son las interfaces de estas últimas, se puede cambiar cualquiera de los dos sin afectar al otro, a veces usando objetos mock (mock object) para simular el comportamiento de objetos complejos.

### Los errores están más acotados y son más fáciles de localizar

Nos permite poder probar o depurar un módulo sin necesidad de disponer del sistema completo. Aunque seamos los propietarios de toda la aplicación, en algunas situaciones montar un entorno para poder probar una incidencia es más costoso que corregir la incidencia propiamente dicha. Si partimos de la prueba unitaria podemos centrarnos en corregir el error de una forma más rápida y lógicamente, asegurándonos posteriormente que todo funciona según lo esperado.

## Limitaciones

- Es importante darse cuenta de que las pruebas unitarias no descubrirán todos los errores del código.
- Algunos enfoques se basan en la generación aleatoria de objetos para amplificar el alcance de las pruebas de unidad.
- Esta técnica se conoce como testing aleatorio (RT, por random testing).
- Por definición, sólo prueban las unidades por sí solas.
- Por lo tanto, no descubrirán errores de integración, problemas de rendimiento y otros problemas que afectan a todo el sistema en su conjunto.
- Además, puede no ser trivial anticipar todos los casos especiales de entradas que puede recibir en realidad la unidad de programa bajo estudio.
- Las pruebas unitarias sólo son efectivas si se usan en conjunto con otras pruebas de software.

## Consideraciones

Como en la adopción de cualquier otra disciplina, la incorporación de pruebas unitarias no está exenta de problemas o limitaciones, a continuación se enumeran algunas consideraciones a tener en cuenta:

- Por estar orientada a la prueba de fragmentos de código aislados, la pruebas unitarias no descubrirán errores de integración, problemas de rendimiento y otros problemas que afectan a todo el sistema en su conjunto.
- En alguno casos será complicado anticipar inicialmente cuales son los valores de entradas adecuados para las pruebas, en esos casos las pruebas deberán evolucionar e ir incorporando valores de entrada representativos.
- Si la utilización de pruebas unitarias no se incorpora como parte de la metodología de trabajo, probablemente, el código quedará fuera de sincronismo con los casos de prueba.
- Otro desafío es el desarrollo de casos de prueba realistas y útiles. Es necesario crear condiciones iniciales para que la porción de aplicación que está siendo probada funcione como parte completa del sistema al que pertenece.
- Escribir código para un caso de pruebas unitario tiene tantas probabilidades de estar libre de errores como el mismo código que se está probando.

Y hasta aquí nuestra entrada de hoy. En la próxima entrada hablaremos de herramientas para las pruebas unitarias y haremos un ejemplo en Java para aprender a realizarlas.

¡Hasta la siguiente entrada!
