---
title: 017 - SonarQube + Plugins con Reglas.
date: '2017-07-05T07:00:43+00:00'
url: /2017/07/05/017-sonarqube-plugins-con-reglas/
image: /img/blog-images/wp-posts/2017/06/foto17.jpg
categories:
- code-quality
- qa
tags:
- plugins-sonar
- sonarqube
author: estefafdez
---
¡Hola a todos!

En las últimas entradas hemos estado hablando de SonarQube: su instalación en Eclipse, en Docker y por último hemos estado hablando de las Reglas y las plantillas. En esta última entrada dedicada a Sonar, hablaremos de cómo importar plugins con reglas ya añadidas... ¡Comenzamos!

Este es un paso bastante importante ya que, en función del lenguaje que se quiera analizar, ofrecerá una batería de métricas ya definidas listas para atacar el código analizado. A partir de esta batería de reglas se podrán coger las plantillas que tenga y crear reglas más personalizadas para cualquier caso en concreto.

Un plugin con reglas provee un muy buen punto de partida a la hora de implementar el análisis de código de la mano de Sonar. El único inconveniente que tiene es que, al ser algo predefinido, deberemos ir regla a regla viendo cuáles de ellas se adaptan a nuestras necesidades y cuáles no para no sobrecargar el análisis del código con datos falsos ni aumentar la deuda técnica de un proyecto.

Para incluir un plugin en Sonar debemos seguir los siguientes pasos:

1. Iniciamos sesión con un perfil que tenga permisos para instalar plugins (por defecto el administrador es _admin/admin_).
1. Hacemos click en Administración en el menú de Sonar.
1. Seleccionamos Sistema y hacemos click en Update Center.
1. Dentro de la sección de actualizar, hacemos click en Available.
1. Buscamos un lenguaje de programación del que queramos instalar plugins, por ejemplo Java.
1. De los plugins disponibles, hacemos click en Instalar.
1. Nos aparece el mensaje de que un plugin necesita instalarse y Sonar se va a reiniciar.
1. Le damos a restart y esperamos a que Sonar se restaure.
1. Una vez que termina de restaurarse, ya tenemos ese plugin disponible e instalado en nuestro Sonar para usarlo.

![sonar_install_plugin](/img/blog-images/wp-posts/2017/06/sonar_install_plugin.png)

Y hasta aquí la entrada de plugins en Sonar.

En la siguiente entrada hablaremos de las buenas prácticas . ¡Nos leemos en la siguiente entrada!
