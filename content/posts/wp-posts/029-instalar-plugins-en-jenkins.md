---
title: 029 - Instalar Plugins en Jenkins.
date: '2017-09-27T09:00:47+00:00'
url: /2017/09/27/029-instalar-plugins-en-jenkins/
image: /img/blog-images/wp-posts/2017/08/foto29.jpg
categories:
- automation
- jenkins
- qa
tags:
- continuous-integration
- docker
- plugins
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a hablar de cómo instalar plugins en Jenkins y cómo encontrarlos. ¡Comenzamos!

![jenkinsplugins.png](/img/blog-images/wp-posts/2017/08/jenkinsplugins.png)

Primero tenemos que ver cómo recuperar el contenedor donde instalamos Jenkins en Docker. ¿Qué debemos hacer? Arrancamos Docker y abrimos un terminal.

Una vez que tengamos Docker corriendo y el terminal abierto, escribimos el siguiente comando que nos dará un listado de los contenedores que tenemos en nuestro Docker:

```bash
docker ps -a
```

![contenedor.png](/img/blog-images/wp-posts/2017/08/contenedor.png)

Ahí podemos ver que tenemos un contenedor con un ID, la imagen que tenemos montada en él y el nombre que le dimos, ¿qué hacemos para arrancar ese contenedor? Escribimos el siguiente comando:

```bash
docker start <nombreContenedor>
```

en mi caso tendría que poner **docker start jenkins** y al abrir de nuevo [http://localhost:9090/](http://localhost:9090/) tendríamos Jenkins como lo dejamos.

Una vez que accedemos con nuestro usuario **administrador**, seleccionamos en el menú la opción **Manage Jenkins** y a continuación hacemos click en **Manage Plugins**:

![jenkinsplugins2.png](/img/blog-images/wp-posts/2017/08/jenkinsplugins2.png)

Cuando estamos en la sección de Manage plugins nos aparecen cuatro secciones a tener en cuenta:

![manage.png](/img/blog-images/wp-posts/2017/08/manage.png)

- **Updates**: en esta sección aparecerán las nuevas versiones de los plugins que tenemos instalados en Jenkins cuando haya una actualización de ellos.
- **Available**: en esta sección se muestra el listado de todos los plugins disponibles en Jenkins.
- **Installed**: en esta sección aparecen los plugins que ya tenemos instalados en nuestro Jenkins.
- **Advanced**: en esta sección encontraremos los campos para realizar una conexión HTTP con un proxy por si lo necesitamos para descargar los plugins, así como la posibilidad de instalar un plugin mediante un fichero .hpi.

Una vez que tenemos claras las secciones que tenemos, hacemos click en Available y vemos la lista de todos los plugins disponibles para Jenkins que podemos encontrar:

![listaplugins.png](/img/blog-images/wp-posts/2017/08/listaplugins.png)

Como veremos en la imagen, la lista de plugins está ordenada por la tecnología en la que se usan, lo cual hace muy fácil buscar aquel que necesitamos en la sección correspondiente.

Y ahora.... ¿cómo instalamos un plugin?

Imaginad que tenemos un repositorio en gitlab donde tenemos nuestro código y necesitamos un plugin de este tipo de repositorio para Jenkins, ¿qué hacemos? primero, buscamos en la web: [https://plugins.jenkins.io/](https://plugins.jenkins.io/) el plugin que necesitemos, en este caso el que queremos es Gitlab Plugins: [https://plugins.jenkins.io/gitlab-plugin](https://plugins.jenkins.io/gitlab-plugin).

¿Qué hacemos ahora que sabemos cuál es el plugin que necesitamos? lo buscamos en la lista y lo seleccionamos:

![gitlabseleccionado.png](/img/blog-images/wp-posts/2017/08/gitlabseleccionado.png)

Como vemos podemos: instalarlo sin reiniciar el Jenkins y descargarlo ahora e instalarlo después de reiniciar. Nosotros haremos click en Install without restart (instalar sin reiniciar jenkins).

![installing.png](/img/blog-images/wp-posts/2017/08/installing.png)

Cuando esté instalado, nos aparecerá este mensaje:

![exito.png](/img/blog-images/wp-posts/2017/08/exito.png)

Y ya podemos volver a nuestro Jenkins y usar nuestro plugin en un job, ¡así de fácil!

En la siguiente entrada os hablaré de mi proyecto [Selenium-Cucumber](http://github.com/estefafdez/selenium-cucumber), proyecto que usaremos para crear nuestro primer Job para ejecutar los test en Jenkins dentro de Docker.

**PD:** No os olvidéis de parar vuestro contenedor en Docker utilizando el comando:

```bash
docker stop <nombreContenedor>
```

¡Hasta la siguiente entrada!
