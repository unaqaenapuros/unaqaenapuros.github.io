---
title: '042 - Pruebas móviles: Pruebas básicas con el dispositivo.'
date: '2018-05-02T07:00:38+00:00'
url: /2018/05/02/042-pruebas-moviles-pruebas-basicas-con-el-dispositivo/
image: /img/blog-images/old-post/2018/04/foto41.jpg
categories:
- mobile-apps
- qa
tags:
- mobile-testing
- pruebas-móviles
- qa-testing
- testing
author: estefafdez
---
¡Hola a todos!

En esta entrada hablaremos de las pruebas básicas que podemos realizar a una aplicación teniendo en cuenta todas las opciones que nos ofrece los dispositivos en los que podemos probarla. ¡Comenzamos!

Cuando vamos a asegurar la calidad de una aplicación, tenemos que ser conscientes de que existen muchos tipos de pruebas que podemos hacerle, y que debemos conocer perfectamente la funcionalidad y los dispositivos en los que necesitamos probarlos.

Las pruebas que se realicen a una aplicación móvil tienen que ser a nivel tanto de software como de hardware ya que muchas de las funcionalidades de esas apps, dependen de los dispositivos en los que se ejecuten, así como la rapidez, el nivel de conectividad, la transmisión de datos...

En esta entrada vamos a centrarnos en la parte de pruebas más hardware y de las posibilidades que tenemos que tener en cuenta a la hora de comprobar las funcionalidades de la aplicación en el dispositivo.

## Pruebas hardware a una aplicación móvil.

A continuación haremos una lista de las pruebas hardware que tenemos que añadir siempre a nuestro plan de pruebas de una app móvil.

### **Instalación de la aplicación.**

![7](/img/blog-images/old-post/2018/04/7.png)

La primera prueba que debemos hacer es la de instalación. Debemos comprobar que la aplicación se instala correctamente en las versiones del sistema operativo que se soporten (iOS 10 y 11, Android 4.4, 5, 6...). Es muy importante que la instalación se realice correctamente y la aplicación se abra sin dar ningún fallo.

Tenemos que tener en cuenta que podemos instalar la aplicación desde el navegador (ser redirigidos a la store correctamente), que hay aplicaciones que necesitan algún tipo de certificado... y son pruebas que tenemos que contemplar siempre en nuestro plan de pruebas.

### **Desinstalación de la aplicación.**

![8](/img/blog-images/old-post/2018/04/8.jpeg)

Al igual que hacemos pruebas de instalación también debemos hacerlas de desinstalación de la app. Tenemos que comprobar que los datos se borran correctamente y no se quedan datos corruptos en el dispositivo, además de comprobar que la desinstalación se realiza correctamente y el proceso termina bien.

### **Tamaño y densidad de pantalla.**

![6](/img/blog-images/old-post/2018/04/6.jpg)

Es de máxima importancia saber y conocer los dispositivos para los que está adaptada nuestra aplicación y en los dispositivos en los que tiene que funcionar bien, no es lo mismo probar en un iPhone 8 Plus ( _5,5 pulgadas, 1.920x1.080 píxeles a 401 ppp_) que en un iPhone SE ( _4 pulgadas, 1,136x640 pixeles a 326ppp)._ Debemos hacer pruebas en ambas densidades (así como en otros dispositivos como tablets si también lo soportamos como parte de los requerimientos). Es importante que comprobemos que la aplicación encaja visualmente en los dispositivos y que no se encuentre ninguna deficiencia visual al utilizarla.

### **Orientación de la pantalla.**

![5](/img/blog-images/old-post/2018/04/5.jpeg)

Al igual que el tamaño y la densidad, es muy importante conocer la orientación de la pantalla en la que se permite en uso de la app. Hay aplicaciones que sólo están diseñadas para portrait pero, por el contrario, hay otras que permiten ambas orientaciones, tanto portrait como landscape. Es necesario que probemos que todas las pantallas de la aplicación se adaptan correctamente a ambas orientaciones y que todos los elementos se ven correctamente.

### **Datos y conectividad.**

![9.png](/img/blog-images/old-post/2018/04/9.png)

Si nuestra aplicación soporta estar sin conexión o no lo soporta, debemos de conocerlo y probar que si la aplicación lo necesita, puede descargar los datos cuando nos conectamos a ella, estemos en una red Wifi o en una red de datos. Es importante que si estamos usando la aplicación con una red de datos y pasamos a una red Wifi, la aplicación reconoce el cambio y el usuario no tiene problemas de conexión, así como el pasar de estar en una red Wifi a una red de datos.

### **Llamadas entrantes.**

![1](/img/blog-images/old-post/2018/04/1.jpeg)

Otra prueba que tenemos que tener en mente es el que nuestra aplicación permita o no las llamadas entrantes y que cuando las tengamos, si estamos usando la aplicación, ésta se mantenga en segundo plano con la sesión abierta y los datos guardados, de esta forma si estamos realizando una compra en nuestra aplicación (por ejemplo) y nos llama alguien, una vez que finalicemos la llamada, podremos seguir realizando la compra en el punto exacto en el que nos encontrábamos.

### **Teclas físicas del dispositivo.**

![2](/img/blog-images/old-post/2018/04/2.jpg)

Además de todo lo anterior, tenemos que tener en cuenta el hecho de los botones físicos en los dispositivos móviles. Puede que tengamos botones físicos para hacer click hacia atrás o para poner la app en segundo plano, y debemos comprobar que estas teclas funcionan sobre la aplicación (por ejemplo el botón físico de atrás) y que esa funcionalidad se realiza correctamente. También debemos comprobar que al ponerla en segundo plano (usando un botón físico), podemos volver a traer de nuevo nuestra aplicación a primer plano y sigue funcionando en el mismo punto en el que la dejamos.

* * *

Y hasta aquí nuestra entrada de hoy. En la siguiente seguiremos hablando de las pruebas básicas que tenemos que tener en cuenta con el dispositivo.

¡Nos leemos en la siguiente entrada!
