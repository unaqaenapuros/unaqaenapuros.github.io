---
title: 049 - UIAutomatorViewer
date: '2019-03-13T09:00:41+00:00'
url: /2019/03/13/049-uiautomatorviewer/
image: /img/blog-images/wp-posts/2019/02/foto48.jpg
categories:
- android
- appium
- automation
- qa
tags:
- tutorial
- uiautomatorviewer
author: estefafdez
---
¡Hola a todos!

En esta entrada hablaremos de otra herramienta para inspeccionar los elementos de las aplicaciones, exclusiva para Android. ¡Comenzamos!

## ¿Qué es UIAutomatorViewer?

Como alternativa a Appium Inspector, podemos utilizar (sólo para Android) la herramienta _UIAutomatorViewer_ que viene por defecto dentro del SDK de Android.

_UIautomatorviewer_ es una aplicación de GUI que analiza los componentes de interfaz de usuario de una aplicación de Android. Para automatizar cualquier aplicación de Android utilizando Appium, necesitamos identificar los objetos AUT (Application under test / objetos de la aplicación a probar). Con _UIAutomatorViewer_ podemos inspeccionar la UI de una aplicación de Android y descubrir el árbol DOM de la aplicación, además de ver las propiedades de las diferentes vistas (id, text...) de un elemento.

![](/img/blog-images/wp-posts/2019/02/1-1.png?w=1000)

## ¿Cómo descargar e instalar UIAutomator?

Uiautomatorviewer está incluido dentro del SDK de Android y está incluido en el SDK manager. Podemos descargar el Android SDK [aquí](https://developer.android.com/studio/).

Una vez que tengamos el SDK instalado, nos iremos a la carpeta donde tenemos el SDK instalado:

Para usuarios de Windows:

```
C:\users\<username>\AppData\Local\Android\sdk\tools\bin
```

Para usuarios de Mac:

```
/Users/<username>/Library/Android/sdk/tools/bin
```

Una vez que estemos en la carpeta, ejecutaremos el fichero (doble click en): _UIAutomatorViewer_ y se abrirá la aplicación:

![](/img/blog-images/wp-posts/2019/02/3-2.png)

## ¿Cómo utilizar UIAutomatorViewer?

En primer lugar, debemos tener el emulador de Android ejecutándose y después debemos instalar el apk que queremos inspeccionar. Esto es tan sencillo como arrastrar un apk dentro del emulador:

![](/img/blog-images/wp-posts/2019/02/install_apk.gif)

Una vez que tengamos la aplicación abierta y el _UIAutomatorViewer_ abierto, hacemos click en el botón de Device screenshot del _UIAutomatorViewer_:

![](/img/blog-images/wp-posts/2019/02/4-1.png)

Al refrescar la pantalla aparecerá la pantalla del emulador con la aplicación y seremos capaces de ver todos los elementos:

![](/img/blog-images/wp-posts/2019/02/5.png?w=1000)

Como podemos ver en la imagen, tenemos dos paneles:

1. En la primera parte del panel (arriba a la derecha) aparece el DOM de la página así como todos los contenedores y elementos que aparecen.
1. Al hacer click en un botón, además de aparecer la parte del árbol donde está, en la segunda parte del panel (abajo a la derecha) aparecen las propiedades de los elementos, como, por ejemplo: text, resource-id...

![](/img/blog-images/wp-posts/2019/02/6.png?w=1000)

## Posibles errores en UIAutomator.

Aunque _UIAutomatorViewer_ funciona bastante bien (a veces incluso mejor que Appium Inspector), hay veces que podemos encontrarnos errores como este:

![](/img/blog-images/wp-posts/2019/02/captura-de-pantalla-2019-02-16-a-las-18.49.45.png)

Este tipo de errores se solucionan:

- Si tienes un emulador, reinicia el emulador y vuelve a utilizar _UIAutomatorViewer_.
- Si estás usando un dispositivo físico, asegurate de que está bien conectado con las developer options activas.

Y hasta aqui nuestro tutorial de _UIAutomatorViewer._ En el próximo artículo hablaremos de cómo crear un script para ejecutar emuladores en Android.

¡Nos leemos en la siguiente entrada!
