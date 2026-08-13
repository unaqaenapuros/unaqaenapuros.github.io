---
title: 027 - Jenkins.
date: '2017-09-13T09:00:40+00:00'
url: /2017/09/13/027-jenkins/
image: /img/blog-images/old-post/2017/08/foto28.jpg
categories:
- automation
- jenkins
- qa
tags:
- continuous-integration
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a hablar de lo que es Jenkins y del concepto de integración continua. ¡Comenzamos!

## ¿Qué es Jenkins?

![original](/img/blog-images/old-post/2017/08/original.png?w=300) **Jenkins** es un software de Integración continua, gratuito y Open Source escrito en Java y está basado en el proyecto Hudson, creado por Kohsuke Kawaguchi.  Podemos descargar Jenkins aquí: [https://jenkins.io/index.html](https://jenkins.io/index.html) **Jenkins** proporciona integración continua para el desarrollo de software. Es un sistema que se ejecuta en un servidor que es un contenedor de servlets, como Apache Tomcat. Soporta herramientas de control de versiones como CVS, Subversion, Git, Mercurial, Perforce y Clearcase y puede ejecutar proyectos basados en Apache Ant y Apache Maven, Gradle, así como scripts de shell y programas batch de Windows.

Debemos conocer de qué hablamos al hablar de **integración continua**.

La **integración continua** se puede definir como una práctica de desarrollo software donde los todos los miembros de un equipo de desarrollo integran su código frecuentemente cada vez que terminan un desarrollo. Puede realizarse desde una subida al día hasta varias dependiendo de las tareas a desarrollar.

Cada vez que el equipo de desarrollo hace una subida de su código al repositorio, se realiza una integración que compila el código fuente y verifica que se ha compilado correctamente obteniendo un ejecutable de la aplicación (puede ser un .apk para una aplicación de Android, un .ipa para una aplicación de iOS...). También se puede añadir la opción de integrar plugins como por ejemplo Sonarqube para realizar un análisis del código y detectar errores lo más pronto posible dentro de cada desarrollo. Al hacer estas integraciones de forma periódica, se comprobará que el código funciona correctamente obteniendo así un producto final más fiable y con menos fallos cuando éste llegue a producción.

Esta práctica junto con herramientas como Jenkins que facilita esta integración continua hace que podamos conocer el estado del software que estamos desarrollando al instante y saber de forma continua los posibles errores que tenemos y corregirlos en el mismo momento cuando los detectamos y no ponerlos en producción.

## ¿Cómo usamos Jenkins en la integración continua?

Una vez que tenemos Jenkins configurado e instalado, debemos crear diferentes tareas llamadas **build** que serán las que nos ayuden a hacer esta integración continua.

¿Qué es un build? Un build es una tarea en la que podemos definir todos los pasos a seguir que definamos para la integración continua. Los builds de Jenkins tienen 4 partes definidas que son las más importantes:

- **Build Triggers**: esta sección nos sirve para configurar cómo activaremos ese build, por ejemplo cada vez que un desarrollador haga un push a un repositorio concreto podemos comenzar ese build, también podemos programarlo para que se haga a una hora concreta (todos los días a las 12 am), o podemos dejarlo sin activar y lo ejecutaremos a mano cuando lo necesitemos.
- **Build Environment:** esta sección nos sirve para configurar los diferentes parámetros para el entorno en el que vamos a realizar la integración continua, por ejemplo, borrar el workspace antes de empezar una ejecución, añadir el timestamp al log...
- **Build:** esta sección nos sirve para configurar la ejecución, por ejemplo: ejecutar un comando shell, invocar ant, ejecutar un script de gradle...
- **Post build actions:** esta sección nos sirve para configurar las acciones posteriores a la ejecución del build, por ejemplo, publicar los resultados de los test en jUnit, mandar un e-mail al equipo de devs o de QA con el resultado de la ejecución, publicar los resultados en Slack...

Cuando tengamos todos estos parámetros configurados podremos ver el histórico de ejecuciones, los resultados de éstas, el tiempo que ha tardado, los artefactos generados....

Debemos tener en cuenta que todo el código necesario para el proyecto debe estar subido a un mismo repositorio compartido para todos los desarrolladores y que todos deben hacer subidas periódicas de su código para crear esa integración continua y generar builds que nos ayuden a ver el estado del producto final. Si un build falla, debemos ver el fallo y qué lo ha producido y arreglarlo lo más pronto posible ya que mantener el Jenkins con builds satisfactorias debe ser algo prioritario si queremos mantener la integración continua en el equipo.

Además, Jenkins también sirve para que el equipo de QA sepa qué versión es la última que se ha generado y qué versión se está probando (importante para reportar los defectos), además de ayudar a la parte de automatización de pruebas siendo también una herramienta perfecta para la ejecución de test automáticos dentro del ciclo de integración continua con el proyecto.

Como recomendación y si queréis hacer un curso más detallado sobre Jenkins, podéis hacer este curso de Pluralsight sobre Jenkins e integración continua (bastante bueno y recomendable):

[https://www.pluralsight.com/courses/jenkins-introduction](https://www.pluralsight.com/courses/jenkins-introduction)

En las siguientes entradas seguiremos con Jenkins y viendo todas las posibilidades que nos ofrece (tanto para desarrolladores como para QA). Para empezar desde cero, en la siguiente entrada veremos cómo instalar Jenkins en Docker y crear un entorno de integración continua para empezar a usarlo.

¡Hasta la siguiente entrada!
