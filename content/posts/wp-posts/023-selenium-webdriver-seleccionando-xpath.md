---
title: '023 - Selenium Webdriver: seleccionando Xpath.'
date: '2017-08-16T07:00:00+00:00'
url: /2017/08/16/023-selenium-webdriver-seleccionando-xpath/
image: /img/blog-images/wp-posts/2017/07/foto23.jpg
categories:
- automation
- qa
- selenium-webdriver
tags:
- firebug
- firepath
- xpath
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a hablar de cómo seleccionar un Xpath para trabajar con Selenium Webdriver de forma que sea lo más robusto y portable posible. ¡Comenzamos!

Antes de empezar con los consejos debemos comprender qué es un Xpath.

**XPath** (XML Path Language) es un lenguaje que permite recuperar información de un documento XML definiendo una sintaxis para establecer partes en un documento XML, permitiendo navegar a través de sus elementos y atributos, además permite manipular de forma básica booleanos, números y cadenas.

Nosotros usaremos este lenguaje adaptado a Selenium pudiendo así buscar elementos dentro de una web. Para poder hacer esto, necesitamos dos extensiones en nuestro navegador (usaremos Firefox) que son Firebug y Firepath.  Firebug es una extensión que nos permite buscar elementos haciendo simplemente encima del elemento a buscar click con el botón derecho y darle a evaluar con Firebug. Firepath nos permite evaluar expresiones tanto Xpath como CSS para comprobar que la expresión que hemos construido es correcta.

**Firepath**: [https://addons.mozilla.org/es/firefox/addon/firepath/](https://addons.mozilla.org/es/firefox/addon/firepath/) **Firebug**: [https://addons.mozilla.org/es/firefox/addon/firebug/](https://addons.mozilla.org/es/firefox/addon/firebug/) **Firebug** es un complemento muy útil que lamentablemente ya no está soportado en el nuevo Firefox (se ha dejado de desarrollar), pero podemos seguir usándolo de la siguiente forma:

- Instalamos la extensión de firebug en Firefox.
- En la barra de direcciones poner: about:config
- Buscamos los siguientes paquetes:

browser.tabs.remote.autostart -----------> ponlo a falso
browser.tabs.remote.autostart.1 -----------> ponlo a falso
browser.tabs.remote.autostart.2 -----------> ponlo a falso

- Reiniciamos el navegador y listo.

Una vez que tenemos ambos complementos instalados vamos a seleccionar el Xpath de varios elementos de la web de google como ejemplo.

Primero abrimos www.google.com en nuestro navegador, seleccionamos un elemento y hacemos click en el botón derecho y le damos a inspeccionar con Firebug.

![Captura de pantalla 2017-07-15 a las 20.22.14](/img/blog-images/wp-posts/2017/07/captura-de-pantalla-2017-07-15-a-las-20-22-14.png)

Al hacer click en inspeccionar con Firebug nos saldrá la siguiente consola:

![Captura de pantalla 2017-07-15 a las 20.23.14](/img/blog-images/wp-posts/2017/07/captura-de-pantalla-2017-07-15-a-las-20-23-14.png)

Vemos que al pulsar sobre la barra nos aparece una expresión Xpath auto-generada. Este tipo de expresiones es el que vamos a intentar evitar.

Cuando seleccionamos un elemento nos aparece dentro de la estructura DOM de la página, dónde se encuentra:

![Captura de pantalla 2017-07-15 a las 20.23.30](/img/blog-images/wp-posts/2017/07/captura-de-pantalla-2017-07-15-a-las-20-23-30.png)

¿Cómo podemos seleccionar entonces el Xpath de la barra de búsqueda de la mejor forma? Así:

Vemos dentro del DOM que el elemento que queremos seleccionar está incluido en un DIV con un ID, por lo tanto es lo que usaremos para encontrarlo. Un Xpath siempre comienza con // seguido de el elemento que queremos buscar, en este caso el DIV y dentro de ese DIV buscamos un ID (que ya sabemos) indicando el nombre siempre entre comillas simples. La expresión Xpath nos quedaría de la siguiente forma:

```
//div[@id='sb_ifc0']
```

Si le damos click a evaluar vemos que el elemento se encuentra pero que dentro de él hay otro sub-nivel que podríamos usar para tener más precisión, para ello evaluaremos el elemento hijo dentro de ese DIV usando / para identificar que es el hijo dentro de ese DIV. Este hijo DIV también tiene un ID que podremos usar para identificarlo. Siguiendo los pasos previos que hemos comentado, la nueva expresión por tanto quedaría así:

```
//div[@id='sb_ifc0']/div[@id='gs_lc0']
```

Si hacemos click en evaluar, podemos comprobar que el elemento que estábamos buscando se ha seleccionado correctamente:

![Captura de pantalla 2017-07-15 a las 20.35.15](/img/blog-images/wp-posts/2017/07/captura-de-pantalla-2017-07-15-a-las-20-35-15.png)

Este ha sido un elemento fácil de seleccionar, pero, ¿cómo hacemos por ejemplo para seleccionar un elemento que contenta un texto concreto que queramos buscar? Usando contains dentro de nuestra expresión Xpath.

Vamos a buscar el link: Publicidad en el footer de la web de Google usando una expresión Xpath con contains. La expresión Xpath quedaría de la siguiente forma:

```
//a[@class='_Gs' and contains(., "Publicidad")]
```

Hemos visto que el elemento está dentro de un a (si el a no tuviera clase, cogeríamos la clase padre span para buscar ese elemento). Dentro de ese a podemos encontrar el texto "Publicidad" que es el que queremos encontrar. Para indicar el texto que queremos encontrar pondremos que, además de la clase de nuestro elemento a deba contener el texto "Publicidad". Cuando vamos a escribir un texto a buscar, éste siempre va entre comillas dobles.

Una vez que tenemos la expresión, hacemos click en evaluar para comprobar que se selecciona el elemento que estábamos buscando:

![Captura de pantalla 2017-07-15 a las 20.39.17](/img/blog-images/wp-posts/2017/07/captura-de-pantalla-2017-07-15-a-las-20-39-17.png)

Si queremos evaluar otro tipo de expresión (no solo Xpath, también podemos usar CSS), seleccionamos la opción que queramos dentro de Firepath de la siguiente forma:

![Captura de pantalla 2017-07-15 a las 20.44.53.png](/img/blog-images/wp-posts/2017/07/captura-de-pantalla-2017-07-15-a-las-20-44-53.png)

Y hasta aquí nuestra entrada sobre los Xpath y el cómo crear expresiones para seleccionar nuestros elementos. En la siguiente entrada hablaremos de cómo comenzar con Selenium Webdriver en un proyecto Maven con Java para hacer nuestro primer test automático.

¡Nos leemos en la siguiente entrada!
