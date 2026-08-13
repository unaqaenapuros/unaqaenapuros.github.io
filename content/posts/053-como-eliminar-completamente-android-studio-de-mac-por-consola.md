---
title: 053 - Cómo eliminar completamente Android Studio de Mac por consola.
date: '2019-05-08T09:00:57+00:00'
url: /2019/05/08/053-como-eliminar-completamente-android-studio-de-mac-por-consola/
image: /img/blog-images/old-post/2019/02/foto52.png
categories:
- android
- mobile-apps
- automation
- qa
tags:
- android-studio
- command-line
- emuladores
author: estefafdez
---
¡Hola a todos!

Para seguir con los post relacionados con Android y la consola, vamos a ver los comandos que debemos seguir para eliminarlo completamente. ¡Comenzamos!

## Preparando la consola.

Primero tenemos que cerrar Android Studio completamente y abrir una consola. Estos comandos los podemos hacer uno a uno desde consola o hacernos un script de bash como hicimos en [esta entrada](/2019/03/06/050-script-ejecutar-emuladores-en-android/) para abrir el emulador.

Los comandos que tenemos que seguir son los siguientes:

```
rm -Rf ~/Library/Preferences/AndroidStudio*
rm ~/Library/Preferences/com.google.android.studio.plist
rm -Rf ~/Library/Application\ Support/AndroidStudio*
rm -Rf ~/Library/Logs/AndroidStudio*
rm -Rf ~/Library/Caches/AndroidStudio*

// Si quieres eliminar todos los proyectos creados con Android Studio:
rm -Rf ~/AndroidStudioProjects

//Borrar todos los ficheros relacionados con gradle (caches y wrapper) utilizaremos:
rm -Rf ~/.gradle

//Borrar todos los dispositivos (AVSs) creados:
rm -Rf ~/.android

// Borrar todas las SDK Tools
rm -Rf ~/Library/Android*

// Borrar todos los logs de Android Studio.
rm -Rf /Applications/Android\ Studio.app
```

Y una vez que ejecutemos todos estos comandos tenemos limpio el sistema de todos los ficheros creados con Android Studio.

Hasta aquí esta entrada, en la siguiente, ya que tenemos Android Studio completamente desinstalado, enseñaremos cómo instalar el SDK de Android desde consola sin necesidad del Android Studio.

¡Nos leemos en la siguiente entrada!
