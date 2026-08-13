---
title: 007 - Cómo reportar un defecto.
date: '2017-05-30T08:29:04+00:00'
url: /2017/05/30/007-como-reportar-un-defecto/
image: /img/blog-images/old-post/2017/05/foto7.jpg
categories:
- qa
tags:
- attachment
- bug
- current-behaviour
- description
- environment
- error
- expected-behaviour
- issues
- jira
- steps-to-reproduce
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a dar una serie de consejos para reportar de forma correcta un defecto.

Una de las cosas que tenemos que tener claras antes de reportar un defecto es tener una forma de reproducirlo. Tenemos que tener un camino claro y definido de cómo reproducir lo que hemos encontrado para darle el máximo de detalles a los desarrolladores para que sean capaces de investigar y resolver el defecto que nos hemos encontrado. La mejor forma de mostrar evidencias que tenemos es tener unos pasos bien definidos, capturas de pantalla o incluso un video en el que se pueda ver el defecto que acabamos de reportar.

El poder dar todos estos detalles hará que el desarrollador sea capaz de reproducirlo en su entorno de primera mano, ver los pasos necesarios y tener más información de primera mano para investigarlo y resolverlo.

Una vez tenemos claro toda esta información, pasaremos a rellenar los datos necesarios para reportarlo:

1. Crear un issue: Si usamos Jira para reportar los defectos, solo tenemos que irnos a Jira y hacer click en crear issue y nos saldrá la plantilla correspondiente que tenemos que rellenar.
1. Configurar los campos necesarios a rellenar: por ejemplo:
   - **Asignado**: desarrollador, responsable de desarrollo...
   - **Adjuntos**: ¿tenemos adjuntos que añadir? Capturas, videos, logs...
   - **Componentes**: componente o parte a la que afecta el defecto reportado, como, por ejemplo: Front-end, Back-end, UI, UX...
   - **Descripción del defecto**: Una descripción detallada del defecto a reportar (no confundir con el summary).
   - **Summary**: Descripción del defecto en una linea de forma resumida.
   - **Entorno (environment)**: pre/pro/stage/dev/qa...
   - **Fix version**: ¿sabemos que tenemos que tener arreglado este defecto en alguna versión específica del desarrollo?.
   - **Labels** (etiquetas): podemos usar este campo para indicar algún tipo de etiqueta que pueda ayudar a los desarrolladores a identificar este defecto de forma rápida.
   - **Prioridad:** Este es uno de los campos más importantes del que hablaremos a continuación.
1. Una vez que tenemos los campos que necesitamos para reportar el defecto, vamos a reportarlo. Para ello seleccionaremos el proyecto en el que vamos a reportar el issue  y el tipo de issue (en este caso bug) y pasaremos a rellenar todos los datos.

#### Reportando un defecto.

1. **Summary**: como hemos comentado anteriormente, el _summary_ es una descripción corta y precisa del defecto en una línea en el que pondremos de forma concreta cuál es el problema que hemos encontrado.
1. **Componente**: Front-end, Back-end, UX, UI...
1. **Environment (entorno):** Pre-producción, Producción, Stage, QA, CI... o el nombre del entorno/rama en el que se reproduzca el defecto. No tiene por qué ser sólo uno, puede ser más de uno.
1. **Prioridad**: este campo es uno de los más importantes, ya que la prioridad es el nivel que indica la importancia del defecto que estamos reportando. Tenemos que tener claro los tipos de prioridad y lo que representan:

   - **P0-Urgent:** Un defecto con prioridad P0 representa un defecto que bloquea el desarrollo o las pruebas o que hace que el entorno de producción no funcione. La prioridad P0 indica un bug que rompe una función principal de la aplicación y que necesita ser arreglado lo más pronto posible.
   - **P1-Serious Bug:** Un defecto con prioridad P1 representa un bug con una pérdida mayor de funcionalidad, que le ocurre a la mayoría de usuarios aunque el resto del sistema funciona como se espera.
   - **P2-Annoying Bug**:  Un defecto con prioridad P2 incida un bug que ocurre a veces, o en casos aislados a varios usuarios aunque la mayoría de la funcionalidad del sistema funciona como se espera.
   - **P3-Normal Bug**: Un defecto con prioridad P3 indica que es un defecto que ocurre raramente o a usuarios aislados mientras que el resto del sistema funciona como se espera.
   - **P4-Low Bug**:  Un defecto con prioridad P4 representa un bug que ha pasado alguna vez pero que no se puede reproducir fácilmente (bug pequeño del que no tenemos unos pasos concretos para reproducirlo), indica una pérdida menor en la funcionalidad o un problema que tiene un fácil workaround en el que trabajar.
1. **Asignado:** Como ya hemos comentado, el asignado puede ser un desarrollador, responsable de desarrollo...
1. **Descripción**: Este es uno de los puntos más importantes y que debemos hacer lo más preciso posible. En él indicaremos los siguientes campos:

   - **Descripción** detallada del problema que hemos encontrado.
   - **Navegadores**/ **Dispositivos** en el que se reproduce: podemos añadir versiones concretas para aclarar aún más el defecto, por ejemplo, podemos reproducir este defecto en Chrome 58 pero no en Firefox o Safari, o se reproduce en un Nexus 5 pero no en un Galaxy S8.
   - **Pasos a reproducir**: En esta sección expondremos de forma clara y detallada los pasos a seguir para reproducir el problema, por ejemplo:

     1. Ve a la web www.google.com
     1. En el cajón de búsqueda introduce el texto: ...
     1. Haz click en buscar y comprueba el tercer resultado...
   - **Comportamiento actual (current behaviour):** En este campo indicaremos qué es lo que está pasando actualmente.
   - **Comportamiento esperado (expected behaviour):** En este campo indicaremos cuál es el comportamiento que esperamos que pase.
   - **Más información:** Si hay algún detalle que no hayamos añadido previamente, éste es el campo para hacerlo.
   - **Adjuntos:** Añadimos un video, captura de pantalla, log o cualquier fichero que nos ayude a identificar fácilmente el problema.

Una vez que tenemos todos estos campos rellenos, hacemos click en publicar y tendremos nuestro defecto completamente detallado con toda la información para hacer más fácil el trabajo a los desarrolladores para poder identificar el problema y solucionarlo.

En la siguiente entrada hablaremos del ciclo de vida de un defecto y las diferentes fases por las que éste va pasando una vez que lo hemos reportado.

¡Nos leemos en la siguiente entrada!
