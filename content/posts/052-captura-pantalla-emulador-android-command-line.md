---
title: 052 - Captura de pantalla de un Emulador Android por consola.
date: '2019-04-24T11:46:16+00:00'
url: /2019/04/24/052-captura-pantalla-emulador-android-command-line/
image: /img/blog-images/old-post/2019/04/foto51.png
categories:
- android
- appium
- appmóviles
- automation
- qa
tags:
- adb
- command-line
- emulador
author: estefafdez
---
¡Hola a todos!

En esta entrada hablaremos de cómo hacer capturas de pantalla de un emulador Android desde consola. ¡Comenzamos!

## Requisitos.

Para seguir estos pasos debemos tener creado previamente un emulador y conocer los comandos para ello. Todo eso puedes volver a leerlo en la entrada [anterior](/2019/03/13/051-como-crear-e…roid-por-consola/).

## ¿Cómo hacemos una captura de pantalla?

Para empezar debemos de entender que vamos a hacer dos pasos para tener la captura:

1. Hacer la captura y guardarla dentro de la memoria (sdcard) del emulador.
1. Pasarla de la memoria del emulador a nuestro equipo.

Para esto utilizaremos el comando **adb** y **screencap.**

Empezamos abriendo un emulador (por consola o Android Studio) y abrimos una aplicación (la que queramos, podemos utilizar la de [AndroidBarista](/2018/11/07/045-android-proyecto-android-barista-i/) que vimos en artículos anteriores).

![](/img/blog-images/old-post/2019/02/install_apk.gif)

## Screencap.

El comando _**screencap**_ tiene las siguientes opciones:

```
usage: screencap [-hp] [-d display-id] [FILENAME]
-h: this message
-p: save the file as a png.
-d: specify the display id to capture, default 0.
If FILENAME ends with .png it will be saved as a png.
If FILENAME is not given, the results will be printed to stdout.
```

Como hemos visto podemos ponerle un nombre y una extensión para guardar la foto.

## Paso 1: Hacer la captura y guardarla en el emulador.

Para utilizarlo, tenemos que irnos primero a la carpeta donde está el **adb**:

```
$ cd /Users/estefafdez/Library/Android/sdk/platform-tools
```

Con el emulador abierto y la pantalla que queremos capturar, ponemos el siguiente comando en la consola:

```
$ ./adb shell screencap -p /sdcard/nameOfScreenshot.png
```

Esto tendrá la siguiente salida por consola y cuando termine sabremos que la captura se ha hecho:

![](/img/blog-images/old-post/2019/04/captura-de-pantalla-2019-02-18-a-las-13.22.50.png)

Con este comando habremos conseguido el primer punto que comentábamos antes, hacer la captura y guardarla dentro de la memoria (sdcard) del emulador.

## Paso 2: Copiar la captura del emulador a nuestro equipo.

Ahora queremos hacer la segunda parte, pasarla de la memoria del emulador a nuestro equipo. Para ello utilizaremos el siguiente comando:

```
$ ./adb pull /sdcard/nameOfScreenshot.png
```

![](/img/blog-images/old-post/2019/04/captura-de-pantalla-2019-02-18-a-las-13.42.46.png)

Con este comando nos traeremos al directorio donde nos encontramos (ahora mismo donde está el adb: ../sdk/platform-tools) una copia del archivo que acabamos de almacenar en el emulador:

![](/img/blog-images/old-post/2019/04/captura_de_pantalla_2019-02-18_a_las_13_27_50.png)

Además podremos abrirla y comprobar que es correcta:

![](/img/blog-images/old-post/2019/04/captura_de_pantalla_2019-02-18_a_las_13_43_16.png)

## Paso 3: Borrar la captura del emulador.

Cuando ya tenemos la captura en nuestro equipo, la eliminaremos del emulador para no dejar nada guardado dentro. Para ello utilizaremos el siguiente comando:

```
$ ./adb shell rm /sdcard/nameOfScreenshot.png
```

Cuando termine este comando se habrá eliminado la captura de nuestro emulador.

## Paso 4: Eliminar la captura del sistema.

Para eliminar por consola la captura que acabamos de hacer, estando en el mismo directorio en el que estábamos, hacemos el siguiente comando:

```
$ rm nameOfScreenshot.png
```

De esa forma tendremos limpio tanto el emulador como el sistema.

Y hasta aquí esta entrada, en la siguiente entrada hablaremos de cómo eliminar completamente Android Studio en Mac todo desde consola.

¡Hasta la siguiente entrada!
