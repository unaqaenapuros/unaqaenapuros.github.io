---
title: 011 - Git Básico.
date: '2017-06-06T09:00:06+00:00'
url: /2017/06/06/011-git-basico/
image: /img/blog-images/old-post/2017/06/foto11.jpg
categories:
- git
- qa
tags:
- git-workflow
- github
- getting-started
author: estefafdez
---
¡Hola a todos!

En esta entrad hablaremos de Git y de los comandos básicos que tenemos que saber para poder usarlo con nuestro proyecto de automatización de pruebas.

Para comenzar, os dejo el enlace de un curso básico gratuito de Git (bastante completo además) de Code School llamado [Try Git](https://www.codeschool.com/courses/try-git).

Una vez que tengamos claro todos los conceptos, vamos a detallar los más importantes:

#### Configurar una cuenta de Github.

Para poder configurar una cuenta, tenemos que realizar una configuración previa para poder realizar cualquier acción en git.

```bash
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

 _Nota_: Si sólo queremos identificarnos en un repositorio concreto, podemos omitir el comando --global.

#### Iniciar un repositorio:

Para iniciar un repositorio de git usamos el comando:

```bash
git init
```

#### Clonar un repositorio en nuestra máquina local.

Para poder descargarnos por primera vez un repositorio a nuestro ordenador desde git hub tenemos que realizar un clonado de éste. Para ello usamos el siguiente comando:

```bash
git clone <URLRepositorio>
```

Por ejemplo:

```bash
git clone http://github.com/estefafdez/selenium-cucumber
```

#### Añadir un fichero:

Para añadir un fichero a git debemos usar el comando:

```bash
git add example.txt
```

Tenemos varias categorías cuando vamos a añadirlo que debemos tener en cuenta:

- **Staged**: ficheros listos para hacer el commit.
- **Unstaged**: ficheros con cambios que no están preparados para hacer el commit.
- **Untracked**: Ficheros que no están en Git, normalmente son ficheros nuevos o recién creados.
- **Deleted**: Ficheros que han sido borrados del proyecto pero aún no lo han sido de Git.

Podemos añadir todos los cambios con el siguiente comando:

```bash
git add -A
```

#### Borrar ficheros de stagin area:

```bash
git reset <filename>
```

Con ese comando borramos todos los ficheros o el fichero específico que pasemos de la staging area.

#### Hacer un commit en Git.

- Lo primero que debemos hacer es un **git status** para que Git reconozca los cambios que hemos hecho y de los que vamos a hacer commit.
- A continuación veremos los ficheros que están en la Stating Área pero aún no están en nuestro repositorio (master), podemos añadir o borrar los ficheros del staging area antes de almacenarlos en el repositorio.
- Cuando tenemos preparados todos los ficheros de los que vamos a hacer commit, escribimos:

```bash
git commit -m "Comentario del commit"
```

El comando -m nos permite añadir un comentario a nuestro commit.

#### Añadir varios ficheros del mismo tipo.

Si tenemos varios ficheros del mismo tipo (varios txt o .java que necesitemos añadir) podemos hacerlo mediante el comando siguiente con el \*:

```bash
git add '*.txt'
```

Una vez que tenemos todos los ficheros añadidos en la staging area, tenemos que hacer un git commit para subir los cambios al repositorio (master):

```bash
git commit -m "Comentario del commit"
```

#### Ver el histórico de Commits.

Para ver el **histórico de los commits** que hemos hecho en el repositorio podemos usar el comando:

```bash
git log
```

y se nos mostrarán todos los cambios que hemos hecho en nuestro repositorio master. También podemos usar el comando:

```bash
git log --summary
```

para ver más información de cada commit.

#### Crear un repositorio remoto:

Cuando queramos crear un repositorio remoto donde almacenar nuestro proyecto (por ejemplo en GitHub) y queramos actualizarlo con nuestro repositorio en local, necesitamos usar el comando:

```bash
git remote add origin https://github.com/myrepo.git
```

Esto añade nuestro repositorio local a la dirección que le indiquemos, en este caso, nuestro repositorio de GitHub cuyo nombre será origin (es el estándar que se suele dar).

#### Hacer un push a un repositorio remoto:

El comando push le dice a git dónde poner los commits cuando estén listos, en este caso vamos a hacer un push con todos los cambios que tenemos en local a nuestro repositorio origin en GitHub. El nombre de nuestro repositorio remoto es origin y nuestro branch local es master. El comando -u le dice a git que recuerde los parámetros necesarios para hacer el push, de esta forma la siguiente vez que queramos hacerlo sólo necesitemos hacer un git push. El comando para hacer nuestro primer push es:

```bash
git push -u origin master
```

#### Hacer un pull a un repositorio remoto:

Cuando tenemos a varias personas colaborando el mismo proyecto, debemos descargarnos sus cambios antes de hacer un push de nuestro código, para ello debemos comprobar los cambios en el repositorio con el comando:

```bash
git pull origin master
```

Es importante tener en cuenta que hay veces que cuando hacemos un pull de todos los cambios disponibles, hay cambios que nos aparecen y de los que no queremos hacer commit aún. Una opción para seleccionar los cambios que aún no queremos subir (hacer commit) es hacer un _stash_ a los cambios. Usando el comando:

```bash
git stash
```

podemos descartar los cambios realizados, y con el comando:

```bash
git stash apply
```

podemos volver a aplicar los cambios después del pull.

* * *

Y con esto daremos por finalizado la primera parte del tutorial de git. En el siguiente artículo seguiremos hablando de git y de los comandos más importantes.

¡Nos leemos en la siguiente entrada!
