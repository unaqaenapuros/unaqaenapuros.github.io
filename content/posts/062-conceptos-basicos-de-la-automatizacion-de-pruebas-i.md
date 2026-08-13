---
title: 062 - Conceptos Básicos de la Automatización de pruebas I
date: '2020-10-07T07:30:00+00:00'
url: /2020/10/07/062-conceptos-basicos-de-la-automatizacion-de-pruebas-i/
image: /img/blog-images/old-post/2020/10/foto59.png
categories:
- automation
- best-practices
- code-quality
- qa
tags:
- basic
- testing
author: estefafdez
---
¡Hola a todos!

después de un breve parón y pocas atualizaciones por aquí, vamos a volver a la carga retomando el tema de QA. En esta entrada vamos a hablar de conceptos básicos de la automatización de pruebas. ¡Vamos!

* * *

La automatización de pruebas involucra el uso de frameworks para desarrollar test que ejecutan pruebas automatizadas en software. Las pruebas automáticas se diferencian de las manuales ya que estas últimas requieren que una persona ejecute las pruebas, mientras que las automáticas se basan en una aplicación que ejecuta y supervisa las pruebas por sí misma.

Las pruebas automáticas se usan frecuentemente para tareas de **test de regresión**, buscando errores y defectos en aplicaciones. El test de regresión es habitualmente agotador y requiere de mucho tiempo, por lo que en este caso las pruebas automáticas facilitan la labor del equipo de QA. Las pruebas automáticas son capaces de replicar funciones del usuario como entradas de teclado, clics del mouse, scroll, buscar en una lista… **haciendo que estas acciones se hagan una y otra vez** en la aplicación para comprobar que todo es correcto.

### ¿Por qué automatizar?

Las principales razones para realizar la automatización de pruebas son:

- **Tiempo:** Ganamos tiempo ejecutando pruebas automáticas en lugar de hacerlas a mano. Evitamos volver a hacer a mano pruebas repetitivas.
- **Feedback diario:** Las pruebas automáticas se ejecutan cada noche y nos dan un informe diario del estado de la aplicación en la que hemos estado trabajando cada día.
- **Pruebas eficientes:** Los resultados de las pruebas automáticas son muy eficientes. Un equipo de QA puede hacer una estrategia para realizar los casos más repetitivos y complejos gracias a la automatización y dejar los demás casos para ejecutarse a mano. De esta forma los dos ámbitos se cumplen y se hace en menor tiempo gracias a la ayuda de la automatización. Además, este método te permite ahorrar tiempo, dinero y recursos humanos, además de generar un alto retorno de inversión.
- **Actualización y reutilización:** Una de las mayores ventajas de los test automáticos es que estos son reutilizables y podemos utilizar lógica de la misma pantalla para realizar varias acciones (o aprovechar esas mismas acciones para realizar varios test distintos que tengan que pasar por secciones comunes). A pesar de que hay que invertir mucho tiempo en hacer un framework sobre el cual desarrollar los test, es mucho mejor tener una buena base sobre la que construir ya que miraremos a la larga que tendremos una solución duradera, sólida y reutilizable para todos los proyectos en los que lo utilicemos, además de seguir un estándar de trabajo.
- **Consistencia:** Las pruebas automáticas ofrecen consistencia en los requerimientos necesarios para las pruebas. Normalmente los test que se deciden automatizar son aquellos que resultan tareas agotadoras de realizar a mano una y otra vez. La automatización disminuye la tasa de error humano al hacer tareas de esta índole, haciendo que las pruebas de regresión puedan pasarse cada noche y sea capaz de detectar cualquier cambio que a una persona puede pasarse al hacer la misma prueba varias veces.

En el siguiente gráfico podremos comprobar el retorno de inversión cuando realizamos automatización de pruebas con respecto a ejecutar pruebas manuales a lo largo de los diferentes sprint:

{{< figure src="/img/blog-images/old-post/2020/10/roi-automation-testing.png?w=1024" alt="" caption="" >}}

### Necesidades para la automatización

#### Entorno de pruebas.

Se requiere de un entorno estático donde poder manipular el contenido en función de las necesidades generadas por la prueba.

El tener un **entorno estático de pruebas** es un punto **definitivo** para empezar con la automatización. Sin un entorno con datos que podamos añadir no seríamos capaces de crear **escenarios para los test** en los que nos aseguremos que falla por la aplicación y no por los datos. El tener esos datos estáticos y poder modificarlos para crear pruebas concretas es algo indispensable para poder empezar a automatizar.

#### Documentación.

- **Análisis funcional:** sin el análisis no seremos capaces de entender qué es lo que necesita el cliente funcionalmente hablando.
- **Caso de uso:** Que se va a probar y qué resultado se espera: Es algo esencial conocer esto antes de empezar las pruebas. Tenemos que tener un objetivo claro, conocer las entradas y saber de antemano las salidas de las pruebas que vamos a hacer. Sin este punto no es posible empezar con la automatización.
- **Historias de usuario bien definidas:** sin unas historias de usuario bien redactadas, detalladas y concretas no seremos capaces de entender la funcionalidad que necesitamos probar.
- **Diagramas de flujo de la aplicación:** nos ayudaría mucho a tener una visión global de la aplicación antes de comenzar a describir el plan de pruebas o de automatizar ninguna prueba.
- **Zeplin/Marvel:** Necesitamos comprobar que el diseño es el correcto y esto nos valdrá tanto para la parte manual como la de automatización.

#### Identificadores en cada elemento.

Para poder trabajar con herramientas de automatización como **Appium, Selenium o Cypress**, necesitamos definir un identificador _(id, accesibilityId, data-test-id, cy-test...)_ a cada elemento que vayamos a comprobar para poder, en primera instancia encontrarlo y luego realizar acciones sobre ese elemento.

El poner identificadores a los elementos es algo que facilita mucho el trabajo de la automatización, además de ser una buena práctica.

Para este tipo de casos y para investigar alguno de los problemas que podamos tener al inspeccionar la aplicación y desarrollar los test (por ejemplo, elementos que no se ven porque un otro elemento se ha quedado encima, elementos que aunque tengan ID tienen la propiedad de visibilidad a falso…) necesitamos **tiempo dedicado de los desarrolladores y apoyo al equipo de QA**

Al principio este tiempo será algo más alto ya que, habrá que añadir todos los identificadores necesarios para probar la aplicación, pero en el futuro, cuando este tipo de acciones se incorporen dentro de los desarrollos (una tarea no estará terminada sin que los identificadores están añadidos), el tiempo del equipo de desarrollo con el equipo de QA irá decreciendo a medida que aumente el desarrollo de los test automáticos.

Y hasta aquí esta entrada, seguiremos hablando de los conceptos básicos de automatización en la siguiente entrada. ¡Nos leemos!
