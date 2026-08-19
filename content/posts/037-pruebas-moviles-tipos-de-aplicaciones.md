---
title: '037 - Pruebas móviles: tipos de aplicaciones.'
date: '2017-11-29T08:00:17+00:00'
url: /2017/11/29/037-pruebas-moviles-tipos-de-aplicaciones/
image: /img/blog-images/old-post/2017/11/foto37.jpg
categories:
- mobile-apps
- qa
tags:
- híbridas
- nativas
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a continuar con los conceptos básicos que debemos saber antes de aprender a realizar pruebas móviles de forma automática. En esta entrada vamos a hablar de los tipos de aplicaciones que se pueden desarrollar para los dispositivos móviles... ¡Comenzamos!

### Tipos de aplicaciones.

![blog-apps-nativas-vs-apps-html-designplus](/img/blog-images/old-post/2017/11/blog-apps-nativas-vs-apps-html-designplus.jpg)

Como comentamos en la anterior entrada, hay diferentes formas y lenguajes de programación utilizados para crear una aplicación móvil ( _Java, C#, Swift, Kotlin.._.) pero no sólo podemos hacerlos en esos también podemos desarrollar aplicaciones mediante frameworks como _Ionic_, _Phonegap_, _Xamarin_... esto da lugar a tener dos tipos claramente diferenciados de aplicaciones móviles, estas son conocidas como aplicaciones **nativas e híbridas.**

### Aplicaciones nativas.

![nativas.png](/img/blog-images/old-post/2017/11/nativas.png)Las aplicaciones nativas son aquellas que están creadas, diseñadas  y optimizadas para un sistema operativo concreto y sólo pueden ejecutarse en ese sistema operativo y en todos los dispositivos móviles que tengan ese sistema operativo. Estas aplicaciones utilizan mejor los recursos del sistema y los elementos disponibles en los SDKs para lograr la mayor funcionalidad posible entre la app y el teléfono.  Estas aplicaciones se escriben y desarrollan en función de un sistema operativo concreto, por lo que es necesario tener permisos de desarrollador en ese sistema para poder subir la aplicación a las tiendas de cada uno de los sistemas.

En el mercado de las aplicaciones nativas, cada una de ellas está desarrollada en un sistema operativo diferente y con lenguajes de programación distintos, siendo los más usados los siguientes:

- **iOS**: Para desarrollar una app nativa en iOS necesitas tener **permisos de desarrollador de Apple (99$/año)**, un ordenador con MacOSX, XCode y el SDK de Apple para poder empezar. Además debes saber **C# o Swift** para poder desarrollar una aplicación.
- **Android**: Para desarrollar una app nativa en Android necesitas tener **permisos de desarrollador de Android (25$ para siempre),** cualquier ordenador que soporte Android Studio y el SDK de Android. Además debes saber **Java o Kotlin** (el nuevo lenguaje de moda en el desarrollo Android) para desarrollar una aplicación.

#### Ventajas de las aplicaciones nativas:

- Acceso completo al dispositivo, en software y hardware.
- Un mejor aprovechamiento de los recursos del dispositivo.
- Mejor experiencia de usuario.
- Visualización desde las tiendas de apps e integración con wereables.
- Envío de notificaciones nativas cada vez que hay una actualización nueva con los cambios desarrollados.

#### Desventajas de las aplicaciones nativas:

- Diferentes lenguajes de programación y habilidades según el sistema operativo.
- Coste de la licencia de desarrollador.
- Permisos para probar tu aplicación en dispositivos físicos (sobre todo por las restricciones de Apple).
- Si necesitas hacer la misma aplicación en ambos sistemas operativos (Android e iOS), el coste de desarrollar esa app es el doble ya que debe hacerse en dos lenguajes diferentes para dos tecnologías distintas aunque sean la misma aplicación.

### Aplicaciones híbridas.

![hibridas.png](/img/blog-images/old-post/2017/11/hibridas.png)Las aplicaciones híbridas son aquellas que se desarrollan utilizando tecnologías webs como **HTML, JavaScript y CSS** y que normalmente se ejecutan mediante el navegador nativo del sistema en el que se ejecuten (valen tanto para Android como para iOS). Estas aplicaciones aparentemente ofrecen las mismas ventajas que una nativa, teniendo en cuenta que al no ser nativo del sistema, y dependiendo del framework que utilicemos para desarrollarlas, no podremos tener acceso a tantas funcionalidades del hardware del dispositivo en el que la queramos ejecutar (no como una nativa), ni podremos tener acceso a las librerías del sistema. Por regla general ofrecen un peor diseño (aunque no es 100% cierto con la llegada de los nuevos frameworks de desarrollo como **Ionic, Phonegap o  Xamarin**) y tienen un rendimiento algo más bajo que una aplicación nativa ya que al no estar desarrollada explícitamente para un sistema operativo, no aprovecha todos los recursos del sistema como si lo hace una nativa específicamente diseñada para un sistema operativo.

#### Ventajas de las aplicaciones híbridas:

- Podemos reutilizar el mismo código para tener una aplicación tanto en iOS como en Android.
- Frameworks como Ionic, Phonegap o Xamarin están en alza.
- Desarrollo más sencillo y menor coste si necesitamos una aplicación para dos plataformas (la desarrollamos una vez y no dos).
- Tiene mucha portabilidad y podemos ejecutarla en cualquier sistema operativo.
- No necesita instalación.
- El usuario siempre contará con la última versión de la aplicación.

#### Desventajas de las aplicaciones híbridas:

- Dependen de un navegador con conexión a internet.
- No tenemos acceso a a tantas funcionalidades del hardware del dispositivo como con una nativa.
- No tenemos acceso a las librerías del sistema.
- Tienen por norma general un peor rendimiento que una nativa.
- No aprovechamos todos los recursos del sistema
- Puede que el lenguaje en el que desarrollemos la app, no sea compatible con alguno de los navegadores incluidos en los sistemas operativos.
- Al no necesitar instalación pierde visibilidad en las tiendas.

* * *

Y hasta aquí nuestra entrada con las diferencias de ambas aplicaciones. En la siguiente entrada seguiremos con los conceptos básicos y hablaremos de las clasificaciones que tienen las diferentes aplicaciones móviles.

¡Hasta la siguiente entrada!
