---
title: 028 - Instalar Jenkins en Docker.
date: '2017-09-20T09:00:43+00:00'
url: /2017/09/20/028-instalar-jenkins-en-docker/
image: /img/blog-images/wp-posts/2017/08/foto27.jpg
categories:
- automation
- jenkins
- qa
tags:
- continuous-integration
- docker
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a hablar de cómo instalar Jenkins en Docker. ¡Comenzamos!

![jenkins_docker](/img/blog-images/wp-posts/2017/08/jenkins_docker.png)**Herramientas utilizadas en este tutorial:**

- MacbookPro con MacOSX Sierra.
- Docker for Mac: [https://www.docker.com/docker-mac](https://www.docker.com/docker-mac)
- Imagen de Jenkins para Docker: [https://hub.docker.com/r/jenkins/jenkins/](https://hub.docker.com/r/jenkins/jenkins/)

Comenzamos descargando Docker para Mac e instalándolo:

![installdocker](/img/blog-images/wp-posts/2017/08/installdocker.png)

Una vez que lo tengamos lo ejecutaremos y lo veremos de la siguiente forma:

![Docker_running](/img/blog-images/wp-posts/2017/06/docker_running.png)

Cuando veamos que Docker está corriendo, abrimos un terminal y escribimos los siguientes comandos para instalar la imagen de Jenkins en Docker:

Bajamos la última versión de Jenkins (lts significa latest):

```bash
docker pull jenkins/jenkins:lts
```

Una vez que termine de descargar todos los archivos, hacemos un pull con las últimas actualizaciones:

```bash
docker pull jenkins/jenkins
```

Una vez descargado por completo, lo ejecutamos en segundo plano para poder seguir usando la consola usando el símbolo & detrás del comando:

```bash
docker run --name jenkins -p 9090:8080 jenkins/jenkins:latest &
```

Cuando lo ejecutamos debemos estar pendiente del log ya que la primera vez que usamos Jenkins nos pedirá una contraseña inicial de Administrador, esta contraseña la podemos encontrar en el log que se genera al lanzar el comando:

![passjenkins.png](/img/blog-images/wp-posts/2017/08/passjenkins.png)

Copiamos la contraseña y abrimos nuestro localhost con el puerto 9090 ([http://localhost:9090/](http://localhost:9090/)) ya que ha sido en el que hemos ejecutado Jenkins y veremos la siguiente pantalla:

![jenkinsUnlock](/img/blog-images/wp-posts/2017/08/jenkinsunlock.png)

Escribimos la contraseña que hemos copiado anteriormente del log y hacemos click en continue y nos aparece la pantalla de bienvenida:

![welcomejenkins.png](/img/blog-images/wp-posts/2017/08/welcomejenkins.png)

Por defecto aparece seleccionada la opción de instalar los plugins sugeridos por la comunidad, que es la que usaremos, una vez que tengamos Jenkins configurado podemos instalar mas plugins si los necesitamos.

Los plugins empiezan a instalarse y podemos ver el proceso de instalación:

![installplugins](/img/blog-images/wp-posts/2017/08/installplugins.png)

Una vez que terminan de instalarse todos los plugins nos aparece una pantalla para crear a nuestro primer usuario administrador. Rellenamos los datos y hacemos click en guardar y finalizar:

![createadminuser](/img/blog-images/wp-posts/2017/08/createadminuser.png)

Y ya tenemos Jenkins listo para usar:

![jenkins ready](/img/blog-images/wp-posts/2017/08/jenkins-ready.png)

Hacemos click en start using Jenkins y accederemos por fin a la pantalla de inicio de Jenkins con el usuario que hemos creado:

![jenkins.png](/img/blog-images/wp-posts/2017/08/jenkins.png)

Y ya tenemos Jenkins instalado y corriendo en nuestro Docker.

En las siguientes entradas hablaremos de cómo configurar un Job, los campos que necesitamos rellenar, que son las acciones pre-build, build y post-build y cómo configurarla con un proyecto real, instalación de plugins...

¡Hasta la siguiente entrada!
