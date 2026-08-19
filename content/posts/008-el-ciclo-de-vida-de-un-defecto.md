---
title: 008 - El ciclo de vida de un defecto.
date: '2017-05-31T08:21:00+00:00'
url: /2017/05/31/008-el-ciclo-de-vida-de-un-defecto/
image: /img/blog-images/old-post/2017/05/foto8.jpg
categories:
- qa
tags:
- active
- closed
- lifecycle
- defect
- new
- reopened
- rejected
- verified
author: estefafdez
---
¡Hola a todos!

En esta entrada hablaremos de forma detallada del ciclo de vida que tienen los defectos y las diferentes fases por las que pasa desde que lo reportamos hasta que lo cerramos. ¡Comenzamos!

Podríamos definir el ciclo de vida de un defecto como el viaje de éste por los diferentes estados durante su vida útil. Estos estados pueden variar dependiendo de la organización, del proyecto o de las herramientas que utilicemos, aún así, sus diferentes estados podrían definirse con este flujo:

![ciclo-vida-defecto](/img/blog-images/old-post/2017/05/ciclo-vida-defecto.jpg)

- **Nuevo:** Defecto que se acaba de crear y aún no se ha validado.
- **Asignado:** Defecto que es asignado a un equipo de desarrollo  o desarrollador para hacer frente a él. Aún no está resuelto.
- **Activo:** El defecto está siendo controlado por integrante del equipo y la investigación está en curso. En esta etapa hay dos resultados posibles: aplazado o rechazado.
- **Para probar:** El defecto está resuelto por el equipo de desarrollo y listo para probarlo.
- **Verificado:** El defecto se prueba y la prueba ha sido llevada a cabo por el equipo de calidad.
- **Cerrado:** El estado final del defecto puede ser cerrado después de las pruebas por parte del equipo de calidad. También se puede cerrar un defecto está duplicado o considerado como que no es un defecto.
- **Reabierto:** Cuando el equipo de desarrollo arregla el defecto pero el equipo de calidad lo prueba y comprueba que aún no está resuelto. En este caso se vuelve a abrir el mismo defecto pero con un estado de reabierto.
- **Aplazado:** A este estado llegamos cuando un defecto no se puede abordar en este sprint o versión y se pasa al siguiente sprint o versión.
- **Rechazado:** Un defecto puede ser rechazado por 3 razones: está duplicado, no es un defecto o no es posible reproducirlo.

Y con esto terminamos nuestra entrada sobre el ciclo de vida de los defectos. En la siguiente entrada hablaremos de los principios de prueba y de sus objetivos.

¡Hasta la siguiente entrada!
