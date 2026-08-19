---
title: 050 - Script Ejecutar Emuladores en Android.
date: '2019-03-27T09:00:32+00:00'
url: /2019/03/27/050-script-ejecutar-emuladores-en-android/
image: /img/blog-images/wp-posts/2019/02/foto49.jpg
categories:
- android
- appium
- automation
- qa
tags:
- android-sdk
- bash
- emulators
- script
author: estefafdez
---
¡Hola a todos!

En esta entrada hablaremos de cómo crear un script para ejecutar emuladores de Android de forma sencilla. ¡Comenzamos!

## ¿Por qué creamos este Script?

Cuando trabajamos con emuladores Android y los necesitamos cada día para trabajar en crear pruebas automáticas, terminaremos cansados de escribir cada día los mismos comandos o estar abriendo y cerrando el Android Studio (como ya vimos en [entradas anteriores](/2018/11/07/045-android-proyecto-android-barista-i/)). Para ello hemos diseñado este script fácil de hacer en bash para abrir los emuladores que tenemos ya creados en el sistema de forma fácil.

## ¿Qué hace este Script?

Los pasos que realiza este script son:

- Va a la carpeta donde están los emuladores dentro del SDK (cada uno debe poner su directorio)
- Lista los emuladores disponibles creados.
- Introduce el número de la lista para seleccionar el emulador a abrir.
- Lanza el emulador seleccionado.

## ¿Para qué sistema operativo nos sirve?.

Como es un script en bash, sirve tanto para Windows, Linux o Mac.

## El código:

En este script hay una cosas que necesitas cambiar para utilizarlo: la ruta del SDK. En el ejemplo aparece la mía pero es algo que debes editar antes de poder ejecutarlo. Yo lo he llamado **emulator.sh.**

```
#!/bin/bash
echo "Going to the sdk folder"
cd /Users/estefania.fernandez/Library/Android/sdk/emulator {CHANGE THIS}

echo "Emulator List:"
OUTPUT="$(./emulator -list-avds)"
echo $OUTPUT
COUNTER=1
arr[0]="Nothing"
echo "Select Device:"

for l in $OUTPUT
do
arr[$COUNTER]=$l
echo $COUNTER.$l
let COUNTER=COUNTER+1
done

read IND

echo "Launching: ${arr[$IND]}"

echo "@${arr[$IND]}"

./emulator "@${arr[$IND]}"
```

También puedes encontrar el script en el siguiente repositorio de Github: [https://github.com/estefafdez/script-open-android-emulator](https://github.com/estefafdez/script-open-android-emulator)

## ¿Cómo ejecutarlo?

Copia el siguiente script y guárdalo en un fichero de nombre **emulator.sh.** Cada vez que lo necesites, ejecútalo y podrás abrir el emulador que necesites de forma rápida.

![](/img/blog-images/wp-posts/2019/02/1-2.png)

Y hasta aquí el tutorial para crear este script. En la siguiente entrada hablaremos de cómo crear, abrir y eliminar emuladores de Android por consola.

¡Nos leemos en la siguiente entrada!
