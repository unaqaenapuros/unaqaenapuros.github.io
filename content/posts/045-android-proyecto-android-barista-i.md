---
title: '045 - Android: Proyecto Android Barista (I).'
date: '2018-11-07T08:00:07+00:00'
url: /2018/11/07/045-android-proyecto-android-barista-i/
image: /img/blog-images/old-post/2018/11/foto44.jpg
categories:
- android
- mobile-apps
- automation
- barista
- git
- qa
tags:
- android-studio
- mobile-development
- mobile-testing
- testing
author: estefafdez
---
¡Hola a todos!

Antes de seguir avanzando en las pruebas de automatización móvil, debemos tener alguna base (aplicación) para poder probar. ¡Comenzamos!

* * *

### URL Repositorio: https://github.com/estefafdez/AndroidBaristaProject

* * *

## ![11](/img/blog-images/old-post/2018/04/11.png)

## ¿Por qué surgió este proyecto?

Este proyecto surge, en primer lugar, para aprender y mejorar mis conocimientos de Android con Android Studio y después para crear una aplicación básica para poder hacer pruebas tanto con Appium, Espresso o Barista.

## ¿Qué puedo encontrar en este proyecto?

Este proyecto contiene una aplicación muy básica de Android con varios TextView y EditView, además de varios botones y otras funcionalidades simples, como, por ejemplo un Toast.

La lógica que nos vamos a encontrar es muy simple, además encontraremos test de UI desarrollados con [Barista](https://github.com/SchibstedSpain/Barista), que explicaremos en la siguiente entrada.

## ¿Cómo puedo empezar a usar este proyecto y generar una aplicación Android para probar?

Vamos a empezar paso a paso, lo primero que debemos hacer es instalar Android Studio y utilizar una aplicación ya hecha.

### Instalar Android Studio y el SDK de Android.

Para instalar Android Studio tendremos que seguir la guía paso a paso que nos publica Google en la siguiente web:

[https://developer.android.com/studio/install](https://developer.android.com/studio/install)

En esta página podremos encontrar cómo instalar Android Studio tanto en Windows, Mac y Linux. Nosotros haremos esta prueba en **MacOS Mojave (10.14).**

### Descargar el proyecto de Github.

Una vez que tengamos el Android Studio instalado, antes de abrirlo, descargaremos el proyecto de Android Barista para tener nuestro primer proyecto Android que podamos abrir y ejecutar.

Para ello debemos irnos al siguiente repositorio de Github: [https://github.com/estefafdez/AndroidBaristaProject](https://github.com/estefafdez/AndroidBaristaProject)

Hacemos click en clone or download y copiamos la URL que nos aparece:

![1](/img/blog-images/old-post/2018/04/1.png)

Una vez que tengamos esa URL, abrimos un terminal para escribir el comando de git para clonar el repositorio:

```
git clone git@github.com:estefafdez/AndroidBaristaProject.git
```

![2](/img/blog-images/old-post/2018/04/21.png)

Y después de todo esto tendremos el proyecto clonado dentro de nuestro equipo.

### Abrir Android Studio y descargar un emulador.

Una vez que tengamos el Android Studio descargado en nuestro sistema operativo, debemos abrirlo y crear un emulador para poder ejecutar la aplicación que veremos más adelante. Para crear un emulador de forma sencilla utilizaremos el **AVD Manager**.

Cuando abramos Android Studio nos aparecerá la siguiente pantalla:

![Captura de pantalla 2018-11-04 a las 13.48.41](/img/blog-images/old-post/2018/11/captura-de-pantalla-2018-11-04-a-las-13-48-41.png)

Podemos crear un proyecto nuevo de Android (si queremos investigar o ver la estructura de un proyecto básico) o importar un proyecto existente. Como acabamos de descargarnos el proyecto de Android Barista, lo que haremos será hacer click en la segunda opción: _Open an existing Android Studio Project_ y abrir el proyecto que acabamos de descargar.

![Captura_de_pantalla_2018-11-04_a_las_13_50_51](/img/blog-images/old-post/2018/11/captura_de_pantalla_2018-11-04_a_las_13_50_51.png)

Cuando hacemos click en Open, se nos abrirá Android Studio de la siguiente forma:

![Captura de pantalla 2018-11-04 a las 13.53.50](/img/blog-images/old-post/2018/11/captura-de-pantalla-2018-11-04-a-las-13-53-50.png)

Ya que tenemos el proyecto en Android Studio vamos a crear un emulador para ejecutar la app de Android Barista. Para ello tenemos que hacer click en AVD Manager:

![Captura_de_pantalla_2018-11-04_a_las_13_58_53](/img/blog-images/old-post/2018/11/captura_de_pantalla_2018-11-04_a_las_13_58_53.png)

Y nos aparece la siguiente pantalla:

![Captura de pantalla 2018-11-04 a las 14.00.14](/img/blog-images/old-post/2018/11/captura-de-pantalla-2018-11-04-a-las-14-00-14.png)

Podremos crear tanto un emulador de dispositivo móvil, android wear, android TV... etc. Nosotros crearemos un emulador de Android. Hacemos click en **_Create Virtual Device._**.. y nos aparece la siguiente pantalla:

![Captura de pantalla 2018-11-04 a las 14.02.39](/img/blog-images/old-post/2018/11/captura-de-pantalla-2018-11-04-a-las-14-02-39.png)Para nuestro ejemplo vamos a elegir un _**Nexus 5X**_ con Play Store, hacemos click en _**Next**_.

![Captura_de_pantalla_2018-11-04_a_las_14_04_28](/img/blog-images/old-post/2018/11/captura_de_pantalla_2018-11-04_a_las_14_04_28.png)

Para elegir la imagen del sistema, elegiremos las imágenes de _**x86**_ y escogeremos una de las APIs disponibles, en nuestro caso cogeremos la _**API 27 (Android 8.1).**_ Hacemos click en _**Next**_ y nos aparece la siguiente pantalla:

![Captura de pantalla 2018-11-04 a las 14.11.16](/img/blog-images/old-post/2018/11/captura-de-pantalla-2018-11-04-a-las-14-11-16.png)

Elegiremos un nombre para el emulador, en nuestro caso escogeremos _**emulator\_27**_ y haremos click en _**Show Advanced Settings**_ donde podremos ver más opciones disponibles:

![Captura_de_pantalla_2018-11-04_a_las_14_12_03](/img/blog-images/old-post/2018/11/captura_de_pantalla_2018-11-04_a_las_14_12_03.png)

Dentro de estas opciones eliminaremos la de _**Enable Device Frame**_ para evitar que el emulador tenga la skin del móvil seleccionado y nos ocupe menos recursos en nuestro sistema, además para que el emulador se cargue de forma más rápida.

Una vez que tenemos todas estas opciones haremos click en **Finish** y tendremos nuestro emulador creado:

![Captura_de_pantalla_2018-11-04_a_las_14_16_03.png](/img/blog-images/old-post/2018/11/captura_de_pantalla_2018-11-04_a_las_14_16_03.png)

Para poder arrancar el emulador, haremos click en el botón de play y se nos abrirá nuestro emulador ya iniciado:

![Captura de pantalla 2018-11-04 a las 14.21.29.png](/img/blog-images/old-post/2018/11/captura-de-pantalla-2018-11-04-a-las-14-21-29.png)

Una vez que tenemos el emulador creado y arrancado, lo único que tenemos que hacer es arrancar la aplicación de Barista que nos hemos descargado, para ello hacemos click en el botón de play de Android Studio y elegimos el emulador en el que lo vamos a ejecutar:

![Captura_de_pantalla_2018-11-04_a_las_14_22_54](/img/blog-images/old-post/2018/11/captura_de_pantalla_2018-11-04_a_las_14_22_54.png)![Captura de pantalla 2018-11-04 a las 14.23.35](/img/blog-images/old-post/2018/11/captura-de-pantalla-2018-11-04-a-las-14-23-35.png)

Al hacer click en Ok tendremos la app iniciada y funcionando en el emulador:

![Captura de pantalla 2018-11-04 a las 14.24.50](/img/blog-images/old-post/2018/11/captura-de-pantalla-2018-11-04-a-las-14-24-50.png)

Y ya podremos empezar a ver la app y a jugar con ella. En la siguiente entrada, hablaremos de cómo utilizar esta app para hacer test con _**Barista: The guy who serves a great Espresso**_ ([https://github.com/SchibstedSpain/Barista](https://github.com/SchibstedSpain/Barista)) de forma sencilla.

¡Nos leemos en la siguiente entrada!
