---
title: 015 - SonarQube + Rule Template.
date: '2017-06-21T07:00:24+00:00'
url: /2017/06/21/015-sonarqube-rule-template/
image: /img/blog-images/wp-posts/2017/06/foto15.jpg
categories:
- qa
tags:
- code-quality
- rule-template
- sonar
- sonarqube
author: estefafdez
---
¡Hola a todos!

Continuamos con los artículos relacionados con SonarQube dedicando este último a una parte muy importante, las reglas.

Como ya hemos hablado anteriormente y para refrescar la memoria, sabemos que **SonarQube** es una herramienta que nos permite monitorizar y analizar el código de una aplicación y ver los errores, code smells y buenas prácticas del código analizado. El uso de esta herramienta cada vez está más extendido ya que el impacto que tiene su implementación es relativamente bajo comparado con la calidad con la que se genera en el código.

En este post se pretende dejar claro qué son, para qué sirven y cómo se crean/editan las reglas que utiliza SonarQube para validar la calidad del código que desarrollamos.

Debemos tener en cuenta que en este momento no es posible crear reglas personalizadas desde la interfaz de usuario de Sonar, esto debe hacerse mediante plugins instalables que ofrece Sonar o plugins desarrollados manualmente.

#### Rule Template.

Vamos a comenzar definiendo qué es una **Rule Template**.

Una _Rule Template_ es aquella regla creada a través de un plugin para permitir a los usuarios definir sus propias reglas dentro de SonarQube.

Esta es la clasificación actual (a partir de SonarQube 4.4) de tipos de reglas y para que se utilizan:

- **Plantilla de reglas**: Son aquellas que sólo se utilizan para crear reglas personalizadas. Estas plantillas no pueden ser activadas ya que son plantillas vacías con parámetros vacíos.
- **Reglas personalizadas**: Son aquellas consideradas como cualquier otra regla. Pueden ser editadas o eliminadas en cualquier momento.

Si queremos ver las plantillas de reglas incluidas en SonarQube tenemos que seguir los siguientes pasos:

1. Abrimos Sonar y hacemos click en la pestaña de reglas.
1. En el menú de la izquierda, seleccionamos Plantillas y hacemos click sobre: Mostrar solo plantillas.
1. Podemos seleccionar una de las plantillas y ver su contenido.

![sonar_templates_rules](/img/blog-images/wp-posts/2017/06/sonar_templates_rules.png)

Una vez estamos aquí podemos ver qué incluye cada plantilla de reglas, sus expresiones, los mensajes que aparecen...

Y hasta aquí esta entrada dedicada a las template rules. En la siguiente entrada seguiremos con Sonar y hablaremos de las Custom Rules.

¡Nos leemos en la siguiente entrada!.
