---
title: 060- Testing exploratorio.
date: '2019-11-06T09:00:13+00:00'
url: /2019/11/06/060-testing-exploratorio/
categories:
- qa
tags:
- exploratory-testing
author: estefafdez
---
¡Hola a todos!

En esta entrada hablaremos de una parte del testing muy utilizada en cualquier equipo y que tenemos que conocer bien las bases para saber hacerla correctamente, hablamos del testing exploratorio. ¡Comenzamos!

![1](/img/blog-images/wp-posts/2019/08/1.png)

Por defecto, cuando pensamos en **testing exploratorio**, lo que se nos viene a la cabeza es un tipo de testing ad-hoc, sin planificación, sin límite de tiempo, sin documentación... pero el testing exploratorio bien realizado es mucho más que todo eso.

### ¿Qué es el testing exploratorio?

El testing exploratorio es un **enfoque de pruebas** en el que simultáneamente se aprende sobre la aplicación, se diseñan casos de prueba y se ejecutan esos casos de prueba.

Para que lo entendamos mejor: cuando una persona hace testing exploratorio, **diseña y ejecuta pruebas con un objetivo en concreto**. Con las conclusiones que obtiene va aprendiendo sobre la aplicación, y utiliza esa información para diseñar y ejecutar nuevas pruebas. Cuando hacemos testing exploratorio no probamos por probar, sino que antes de empezar tenemos que definir varias cosas:

- **Un objetivo** que queremos conseguir con la sesión de testing exploratorio (por ejemplo establecer flujos que podrían seguir los usuarios de la aplicación y probarlos, ver cómo se integra la aplicación con software externo, vulnerabilidades de seguridad en el login etc.), que puede ponerlo el propio tester, el equipo de testing, o el test manager
- **Limitar de alguna manera el tiempo** que vamos a dedicarle a esa actividad de testing (sesiones de 1 hora, 25 min etc.).

La principal ventaja del testing exploratorio es que **limita qué se quiere conseguir y en cuánto tiempo**, pero el objetivo es bastante general, no se indica qué pasos debe ir verificando el tester. El tester es el responsable del camino que debe seguir para conseguir ese objetivo, que puede ir cambiando a medida que va aprendiendo sobre la aplicación durante el tiempo establecido.

Para hacer buenas pruebas exploratorias, es necesario que los testers tengan una **mente abierta, pensamiento crítico, sean observadores, creativos, y curiosos para detectar bugs más complejos y evaluar riesgos**. El testing exploratorio bien planteado puede dar muy buenos resultados, pero todo depende de las habilidades del tester, de que sea capaz de analizar en qué puntos podría fallar la aplicación (de acuerdo al objetivo establecido), qué riesgos puede tener eso etc.; todo ello basándose en el conocimiento que tiene de la aplicación. Esto requiere mayor actividad intelectual y experiencia que verificar funcionalidades, pero por experiencia, suele motivar más a los testers experimentados, ya que pone a prueba sus habilidades, es un reto. Una vez que se termine la sesión de testing exploratorio, se reportarán los bugs que se han encontrado durante el tiempo de la sesión.

En cuanto a la documentación, en las sesiones de testing exploratorio **podemos (y debemos como buena práctica) documentar**: podemos documentar el objetivo de la sesión de testing exploratorio, bocetos de los casos de prueba que vayamos realizado, diagramas etc. Podemos ayudarnos de documentar en Word, Excel, capturas de pantalla etc. No hay ninguna restricción sobre cómo documentar en testing exploratorio, pero si es recomendable documentar, aunque no realizar una documentación exhaustiva (al menos, en lo que dura la sesión, ya que solamente diseñar casos de prueba no es el objetivo). Lo que si es imprescindible (como en cualquier actividad de testing) es ser capaces de reproducir los bugs que encontremos para que el proceso de pruebas sea **fiable** y los desarrolladores puedan **reproducir los fallos** para solucionarlos.

Otra de las bases principales del testing exploratorio es que, a medida que avanza la sesión de testing exploratorio, **aumenta la calidad de las pruebas que se realizan** (en relación al objetivo que quieres cumplir), ya que el tester aprende sobre la aplicación y va alimentando el diseño y ejecución de las pruebas con lo que va aprendiendo.

### ¿Para qué sirve el testing exploratorio?

Es recomendable que no sólo realicemos testing exploratorio, sino que este tipo de pruebas sea una actividad complementaria a las pruebas funcionales, historias de usuario, pruebas de rendimiento, automáticas... en definitiva, algo complementario a todas nuestras actividades de pruebas que se realicen.

Las **ventajas** que nos aporta frente a otro tipo de pruebas son:

- Podemos profundizar y obtener feedback rápido y sobre algo concreto.
- Podemos aprender sobre la aplicación.
- Es muy útil si ya se tiene parte de automatización, pruebas de regresión puntuales (al final del sprint) y pruebas de validación y verificación. Si además de todo esto hacemos testing exploratorio, estaremos encontrando bugs más complejos que puede que no hayamos encontrados en cualquiera de los otros casos.
- Podemos mejorar la documentación de la aplicación, los casos de prueba automáticos, los casos de prueba manuales definidos con lo que aprendamos mediante este tipo de pruebas.

Como **desventaja** podemos decir que es algo que no tiene mucho retorno de inversión en aplicaciones críticas y sí en aquellas en entornos estables donde se tiene muchísimo conocimiento de la aplicación.

### Fases principales del testing exploratorio:

Las fases principales de las pruebas exploratorias son:

- **Exploración del producto:** para conocer a fondo cómo cumplir con los requisitos hay que registrar los objetivos, las funciones, los tipos de datos que se procesan y las zonas de inestabilidad del producto. Para llevar a cabo esta exploración, hay que contar con la compresión general de la tecnología, la información sobre el producto y la cantidad de tiempo en el que se va a realizar el trabajo.
- **Diseño de pruebas:** crear diferentes estrategias para observar y evaluar por completo el producto. Ejecución de pruebas: explorar el producto para poder formular una hipótesis de cómo funciona y cuáles pueden ser sus puntos débiles.
- **Heurística:** reglas generales que ayudarán a cómo probar correctamente el producto.
- **Resultados revisables:** cuando se finalicen las pruebas exploratorias, el tester debe ser capaz de explicar cualquier aspecto del programa y mostrar cómo se cumplen los requisitos indicados en el procedimiento. De manera que, todos los requisitos hayan sido probados al menos una vez durante todo el proceso de trabajo.

Para conocer más el producto y facilitar el trabajo se determinarán distintas funciones a realizar durante las pruebas exploratorias:

- **Funciones primarias:** se asocian con la funcionalidad del producto y son esenciales para un objetivo en concreto. Un conjunto de funciones pueden constituir una función primaria, por ejemplo, las distintas funciones de una barra de herramientas no se consideran primarias, pero toda la barra de herramientas si puede considerarse una función primaria.
- **Funciones contributivas:** colaboran con la funcionalidad del producto, pero no se consideran primarias.

Con el fin de asegurar la **funcionalidad y la estabilidad** del producto, tenemos que comprobar que su función es coherente con su finalidad, independientemente de la exactitud de su producción, y comprobando que ningún comportamiento perjudique su uso normal, provocando un crash o una pérdida de datos. Para conseguirlo, debemos tener una noción similar a la de un usuario normal, que puede ser una persona con conocimientos básicos de la aplicación o con experiencia previa en su función.

Además, debemos asegurarnos que se cubre el 100% de las funciones del producto, para ello se dedicará aproximadamente el 80% del tiempo en probar las funciones primarias de la aplicación, el 10% en las funciones contributivas y el resto en las posibles áreas de inestabilidad que podrían provocarse.

Para realizar las pruebas exploratorias, normalmente la fuente principal es la propia intuición, aunque algunas veces tendremos acceso a documentación del producto, que nos ayudará a guiarnos en nuestro trabajo,y otras veces podremos ayudarnos de nuestra propia experiencia en productos relacionados. También nos ayudarán los oráculos, que nos permitirán determinar si un comportamiento observado es o no correcto, estos elementos son importantes ya que controlan los tipos de problema que pueden observarse e informan de ellos. De manera general, un oráculo se forma a partir de unas reglas de consistencia:

- **Consistencia con propósito**
- **Consistencia dentro del producto**
- **Consistencia de la historia**
- **Consistencias con los productos comparables**

De esta forma, podremos determinar si la función se ajusta de manera aparente a su propósito, si es consistente con el resto de funciones comparables del producto, si es coherente con el comportamiento pasado y, por último, si es comparable con las funciones similares en productos similares.

Esta es la manera más completa para realizar las pruebas exploratorias pero, en la mayoría de las ocasiones, nuestra propia intuición será la mejor compañera para llevarlas a cabo.

_Exploratory software testing is a style of software testing that emphasizes the personal freedom and responsibility of the individual tester to continually optimize the value of her work._

(Las pruebas de software exploratorio son un estilo de pruebas de software que enfatizan la libertad personal y la responsabilidad del tester individual para optimizar continuamente el valor de su trabajo.)

### Conclusión.

- El testing exploratorio requiere su planificación, limitación de tiempo y objetivo, no está reñido con documentar y hacerlo bien es más complicado.
- Para poder mejorar en este tipo de testing debemos tener experiencia y conocimiento de la aplicación y, sobre todo, mucha práctica.
- Es una práctica complementaria perfecta para aprender más de la aplicación y encontrar defectos complejos.

* * *

Y hasta aquí nuestra entrada sobre el testing exploratorio. ¡Nos leemos en la siguiente entrada!
