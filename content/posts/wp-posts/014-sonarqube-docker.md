---
title: 014 - SonarQube + Docker.
date: '2017-06-18T11:01:48+00:00'
url: /2017/06/18/014-sonarqube-docker/
image: /img/blog-images/wp-posts/2017/06/foto14.jpg
categories:
- code-quality
- qa
tags:
- docker
- play-with-docker
- sonarqube
author: estefafdez
---
¡Hola a todos!

En esta sección vamos a explicar cómo instalar SonarQube en Docker para poder lanzar fácilmente sonar y ver el estado de la calidad de nuestro código.... ¡Comenzamos!Podemos hacerlo de dos formas, una mediante la aplicación de **Docker** y otra mediante **Play With Docker** (sólo dura 4 horas).

#### Play with Docker.

Play with docker es una web que nos permite crear contenedores virtuales que podemos usar durante un periodo de 4h. Sirven para hacer pruebas con docker de forma fácil y sencilla y para casos puntuales. Si queremos usar Play With Docker para instalar nuestro sonar y hacer un análisis rápido (sin guardar luego los resultados), lo haremos de la siguiente forma:

- Accedemos a la web de Play with Docker: [http://labs.play-with-docker.com/](http://labs.play-with-docker.com/)
- Se nos crea por defecto una nueva sesión que se verá de la siguiente forma:

![instancia_play_with_docker](/img/blog-images/wp-posts/2017/06/instancia_play_with_docker.png)

- Creamos una nueva instancia haciendo click en " **+Add new Instance**":

![instancia_docker.png](/img/blog-images/wp-posts/2017/06/instancia_docker.png)

- Una vez que tenemos la instancia funcionando, podemos comenzar a instalar Sonar. Para ello ponemos los siguientes comandos:

```bash
docker pull sonarqube
docker run -d --name sonarqube -p 9000:9000 sonarqube
```

![sonar.png](/img/blog-images/wp-posts/2017/06/sonar.png)

- El puerto aparece en la web y sólo tenemos que hacer click en él para ver la página de inicio de Sonar.

![sonar_url.png](/img/blog-images/wp-posts/2017/06/sonar_url.png)

- Una vez tenemos esto, debemos añadir esta URL dentro de nuestro proyecto en el pom.xml de la siguiente forma:

Tenemos que añadir las librerías de Sonar dentro de nuestro proyecto en forma de dependencias

```xml
<dependency>
  <groupId>org.codehaus.sonar</groupId>
  <artifactId>sonar-maven-plugin</artifactId>
  <version>${sonar-maven-plugin.version}</version>
</dependency>
```

En la sección de plugins añadimos un perfil para **sonar-maven**:

```xml
<plugin>
  <groupId>org.sonarsource.scanner.maven</groupId>
  <artifactId>sonar-maven-plugin</artifactId>
  <version>3.2</version>
</plugin>
```

Y finalmente creamos un perfil para Sonar:

```xml
<profiles>
  <profile>
    <id>sonar</id>
    <activation>
      <activeByDefault>true</activeByDefault>
    </activation>
    <properties>
      <!-- Optional URL to server. Default value is http://localhost:9000 -->
      <sonar.host.url>URL Sonar Docker</sonar.host.url>
    </properties>
  </profile>
</profiles>
```

Cuando tengamos el POM actualizado con la URL en la que está Sonar, nos vamos a la carpeta del proyecto, abrimos un nuevo terminal y simplemente ejecutamos el siguiente comando:

```bash
mvn clean install sonar:sonar
```

![sonar_ok.png](/img/blog-images/wp-posts/2017/06/sonar_ok.png)Una vez que tengamos el Build Success ya veremos los resultados del análisis del código del proyecto en la página de Sonar:![sonar_resultados.png](/img/blog-images/wp-posts/2017/06/sonar_resultados.png)

#### Usando la aplicación de Docker.

Si lo que queremos es tener los resultados guardados en un Docker propio y que no se pierdan, podemos hacerlo usando la aplicación oficial de Docker que podemos descargar desde su web:

- Versión para Mac: [https://www.docker.com/docker-mac](https://www.docker.com/docker-mac)
- Versión para Windows: [https://www.docker.com/docker-windows](https://www.docker.com/docker-windows)

Una vez descargada, la instalamos e iniciamos, y cuando tengamos el docker iniciado abrimos cualquier terminal y seguimos exactamente los mismos pasos que hemos explicado anteriormente.![Docker_running.png](/img/blog-images/wp-posts/2017/06/docker_running.png) **Nota**: La única diferencia que tenemos que tener en cuenta es que ahora, la URL en la que se encontrará Sonar después de instalarlo en el docker es la URL por defecto: [http://localhost:9000](http://localhost:9000/)

Y esto es todo en cuanto a SonarQube con Docker. En la siguiente entrada seguiremos hablando de Sonar y descubriremos qué son las reglas en Sonar y cómo crear una plantilla.

¡Hasta la siguiente entrada!
