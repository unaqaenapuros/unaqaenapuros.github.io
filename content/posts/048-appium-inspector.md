---
title: 048 - Appium Inspector
date: '2019-02-27T09:00:33+00:00'
url: /2019/02/27/048-appium-inspector/
image: /img/blog-images/old-post/2019/02/foto47.jpg
categories:
- android
- appium
- automation
- qa
tags:
- appium-inspector
- automatización
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a hablar de Appium Inspector, una herramienta de Appium que nos permite ver los elementos de las pantallas de una aplicación. ¡Empezamos!

## ¿Qué es Appium Inspector?

Appium Inspector es una aplicación que nos permite, de forma rápida, inspeccionar una aplicación que se está mostrando en un emulador/simulador Android o iOS y que nos permite ver:

- Comprobar el DOM de la página de la aplicación que estamos viendo.
- Comprobar los identificadores únicos de cada elemento.
- Realizar acciones sobre los elementos que hemos encontrado con sus identificadores: comprobar si está visible, hacer click, tap...

## ¿Cómo nos lo podemos descargar?

Para poder descargarlo debemos  ir al siguiente enlace: [https://github.com/appium/appium-desktop/releases/](https://github.com/appium/appium-desktop/releases/). Podemos elegir la plataforma para la que queramos utilizarlo (Linux, Windows o Mac). Descargamos el ejecutable, lo abrimos y seguimos los pasos y ya lo tenemos completamente instalado para utilizarlo.

![](/img/blog-images/old-post/2019/02/1.png?w=1000)

## ¿Cómo lo utilizamos?

Una vez que lo tengamos descargado e instalado, debemos hacer click en **Start Server**:

![](/img/blog-images/old-post/2019/02/2.png?w=1000)

Donde nos aparecerá la siguiente pantalla:

![](/img/blog-images/old-post/2019/02/3.png?w=1000)

Hacemos click en el icono de la lupa y nos aparece la siguiente pantalla:

![](/img/blog-images/old-post/2019/02/4.png?w=1000)

Seleccionamos **Automatic Server** y ponemos las capabilities de nuestra aplicación a probar, un ejemplo podría ser _(utilizaremos la aplicación de AndroidBarista de la que hablamos en [entradas anteriores](/2018/11/21/046-android-proyecto-android-barista-ii/) para Android):_![](/img/blog-images/old-post/2019/02/captura-de-pantalla-2019-02-16-a-las-13.49.38.png?w=1000)

Las capabilities mínimas que debemos poner son:

- **deviceName**: nombre del emulador.
- **platformName**: android o ios.
- **platformVersion**: versión del sistema operativo del emulador.
- **app**: ruta de la app. Si ponemos como tipo filepath podremos seleccionarla desde nuestro equipo como un fichero más.

Una vez que tengamos todas las capabilities correctas, hacemos click en **Start Session** y veremos la misma pantalla del emulador en Appium Inspector:

![](/img/blog-images/old-post/2019/02/captura-de-pantalla-2019-02-16-a-las-13.53.29.png?w=1000)

Para poder inspeccionar un elemento, hacemos click en él y veremos las siguientes propiedades:

![](/img/blog-images/old-post/2019/02/2-1.png?w=1000)

Cuando terminemos que ver todos los identificadores de los elementos de la pantalla, quitaremos la sesión haciendo click en:

![](/img/blog-images/old-post/2019/02/3-1.png?w=1000)

## Más funcionalidades.

Ademas de inspeccionar elemento, también podemos realizar funcionalidades como:

- Realizar grabación de pasos: como si utilizáramos Selenium IDE.

![](/img/blog-images/old-post/2019/02/captura-de-pantalla-2019-02-16-a-las-13.57.46.png)

- Buscar un id/xpath: podemos buscar dentro de nuestra pantalla mediante un ID o Xpath un elemento para comprobar que verdaderamente es el correcto.

Hacemos click en search for element:

![](/img/blog-images/old-post/2019/02/captura-de-pantalla-2019-02-16-a-las-13.58.00.png)

Seleccionamos como estratégia a localizar ID e introducimos el nombre del ID a buscar:

![](/img/blog-images/old-post/2019/02/captura-de-pantalla-2019-02-16-a-las-13.58.29.png)

Hacemos click en search para buscar el elemento:

![](/img/blog-images/old-post/2019/02/captura-de-pantalla-2019-02-16-a-las-13.58.37.png)

Y hasta aquí Appium Inspector, en la siguiente entrada hablaremos del UIAutomator como herramienta para localizar elementos en Android.

¡Nos leemos en la siguiente entrada!
