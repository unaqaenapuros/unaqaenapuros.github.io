---
title: 012 - Git Básico (II)
date: '2017-06-08T09:00:33+00:00'
url: /2017/06/08/012-git-basico-ii/
image: /img/blog-images/old-post/2017/06/foto12.jpg
categories:
- git
- qa
tags:
- git-workflow
- github
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a continuar hablando de Git y de los comandos más importantes que debemos conocer.

#### Diferencias:

Si hemos tenido cambios en el repositorio y queremos ver qué es lo que ha cambiado, usamos el comando:

> git diff

y se mostrará una lista de los cambios realizados. Si queremos ver cuál es la diferencia entre nuestro commit más reciente, podemos verlo usando el puntero al **HEAD** con el comando:

> git diff HEAD

HEAD es un puntero que contiene tu posición con respecto a todos los commits que se han realizado. Por defecto HEAD te posiciona en tu commit más reciente, de esta forma podrás ver de forma sencilla la referencia a ese commit y los cambios realizados.

#### Diferencias con Staged:

Otro uso del comando diff es el poder ver todos los cambios realizados en ficheros que están en estado staged. Recordamos que staged es el estado de los ficheros que ya hemos dicho a git que están listos para hacer el commit. Para ver estas diferencias usamos el comando:

> git digg --staged

#### Reseteando el Staged:

Podemos quitar ficheros del estado staged usando el comando git reset. Para hacer un reset de un fichero concreto usamos el comando:

> git reset carpeta/fichero.txt

#### Deshacer:

Si después de hacer algún reset nos damos cuenta de que queremos deshacer algún cambio que hemos realizado (dejarlo como estaba antes de nuestro último commit), podemos usar el comando:

> git checkout -- fichero.txt

 **Crear un nuevo branch:**

Para crear un nuevo branch o copia del código usamos el comando:

> git branch <branch>

Para ver todas las ramas (branch) que tenemos en el repositorio usamos:

> git branch

Si queremos **cambiar de un branch** a otro lo hacemos mediante el comando:

> git checkout <branch>

#### Borrar un fichero o una carpeta:

Para borrar un fichero concreto usamos el comando:

> git rm ‘fichero.txt’

Para borrar varios ficheros de un mismo tipo usamos:

> git rm ‘\*.txt’

Para borrar de forma recursiva un directorio con carpetas dentro usamos:

> git rm -r directorio

 **Nota**: Para aplicar los cambios después de borrar algún fichero siempre tenemos que hacer un commit con el comando:

> git commit -m “Comentario del commit”

#### Hacer un merge desde un branch a la rama master:

Para ello nos vamos a la rama master con el comando:

> git checkout master

Hacemos un merge en la rama master indicando con qué branch queremos hacer el merge:

> git merge <branch>

Una vez completado el merge con la rama master, borramos nuestro branch con el comando:

> git branch -d <branch>

y hacemos un push final para guardar todos los cambios:

> git push

#### Trabajar con ramas.

 **Crear una rama y movernos a ella:**

Si tenemos varias ramas en un repositorio y queremos trabajar con ellas, debemos descargarnos las ramas después de realizar el clone del repositorio (como hemos visto anteriormente). Para ello usamos los siguientes comandos:

> git clone **URLRepositorio**
>
> git fetch origin
>
> git checkout -b "nombreDeLaRama"

Al hacer -b creamos la rama en nuestro repositorio local.  El nombre de la rama debe estar entre comillas.

**Movernos a una rama concreta:**

Para movernos a una rama concreta tenemos que hacerlo mediante el siguiente comando:

> git checkout nombreRama

En este caso, el nombre de la rama irá sin comillas.

**Subir los cambios.**

Una vez que hayamos trabajado con la rama que hemos bajado y queramos subir nuestros cambios hacemos los siguientes pasos:

- Comprobamos los ficheros que han cambiado:

> git status

- Añadimos los ficheros que queremos subir.

> git add "nombreFichero"

- También podemos añadir todos los ficheros que se han modificado.

> git add -A

- Hacemos un commit en nuestra rama local.

> git commit -m "mensajeParaElCommit"

- Subimos los cambios al repositorio.

> git push origin nombreRama

 **Actualizar desde una rama:**

Para traernos los cambios desde un repositorio a nuestra rama local debemos actualizarnos mediante el comando pull de la siguiente forma:

> git pull origin nombreRama

* * *

Y con todo esto damos por terminado el tutorial básico de Git.

Si tenéis alguna duda, no dudéis en escribir un comentario en esta entrada o contactar conmigo por cualquiera de mis perfiles.

En la siguiente entrada hablaremos una herramienta de calidad de código como es **Sonarqube**.

¡Nos leemos en la siguiente entrada!
