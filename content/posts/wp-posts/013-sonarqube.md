---
title: 013 - SonarQube
date: '2017-06-10T09:00:15+00:00'
url: /2017/06/10/013-sonarqube/
image: /img/blog-images/wp-posts/2017/06/foto13.jpg
categories:
- automation
- code-quality
- qa
tags:
- sonarqube
- testing
author: estefafdez
---
¡Hola a todos!

Como comentábamos ya en las pasadas entradas, vamos a dejar atrás las entradas teóricas y vamos a centrarnos en las más técnicas. Comenzamos con git y los comandos básicos para saber usarlos y en esta entrada continuaremos con SonarQube.

¿Qué es SonarQube?  **SonarQube** (conocido anteriormente como **Sonar** ) es una plataforma para evaluar código fuente. Es software libre y usa diversas herramientas de análisis estático de código fuente como Checkstyle, PMD o FindBugs para obtener métricas que pueden ayudar a mejorar la calidad del código de nuestra aplicación.

Debemos tener en cuenta que SonarQube es una herramienta para gestionar la calidad del código, la herramienta controla la calidad en 7 ejes:

![image0031](/img/blog-images/wp-posts/2017/06/image0031.png)

La plataforma soporta actualmente más de 20 lenguajes incluyendo Java, Javascript, Cobol, PL, C#… nosotros nos centraremos en Java.

¿Cómo empezar? En este tutorial comenzaremos instalando SonarQube en Eclipse.

El objetivo que deseamos obtener con la integración de SonarQube con Eclipse es mejorar el código generado a lo largo de la fase de desarrollo, de forma que podemos ver en esta fase las posibles malas prácticas utilizadas y evitarlas con la información que nos proporciona SonarQube.

#### Instalación de SonarQube en Eclipse.

1. Help
1. Install New Software
1. Añadir la siguiente url [http://downloads.sonarsource.com/eclipse/eclipse/](http://downloads.sonarsource.com/eclipse/eclipse/)
1. Install

![instalarSonar1.png](/img/blog-images/wp-posts/2017/06/instalarsonar1.png)

#### Configuración de servidor

1. Preferences
1. SonarQube
1. Servers
1. Add..
1. SonarQube Server ID: El id que queramos dar al servidor añadido (en nuestro caso default)
1. SonarQube Server URL: URL donde se localiza la instalación de sonar (por defecto **http://localhost:9000**)
1. Username y Password: Usuario y Password para conectarnos a SonarQUBE

![instalarSonar2.png](/img/blog-images/wp-posts/2017/06/instalarsonar2.png)

#### Añadir y seleccionar proyecto Sonar.

1. Hacemos click derecho en el proyecto de Eclipse que queramos analizar.
1. Configure
1. Associate with SonarQube
1. Escribimos el nombre del proyecto de SonarQube
1. Finish

#### ![instalarSonar4](/img/blog-images/wp-posts/2017/06/instalarsonar4.png)

#### Analizar el proyecto con Sonar.

1. Hacemos de nuevo click derecho en el proyecto de Eclipse que queremos analizar.
1. Hacemos click en SonarQube
1. Analyze.

![instalarSonar3.png](/img/blog-images/wp-posts/2017/06/instalarsonar3.png)

#### Revisión de errores

Una vez analizado el proyecto podremos ver los errores señalados con un ícono de sonar y una descripción. Además de una ventana que nos muestra todos los errores del proyecto , de manera que nos facilita el acceso a estos errores para poder arreglarlos.

* * *

Y esto es todo por esta entrada. En la siguiente veremos como instalar SonarQube por consola o incluso en un Docker de forma rápida y cómo analizar el proyecto desde el terminal.

¡Nos leemos en la siguiente entrada!
