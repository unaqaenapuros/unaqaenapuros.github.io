---
title: '046 - Android: Proyecto Android Barista (II).'
date: '2018-11-21T08:00:08+00:00'
url: /2018/11/21/046-android-proyecto-android-barista-ii/
image: /img/blog-images/old-post/2018/11/foto45.jpg
categories:
- android
- mobile-apps
- automation
- barista
- git
- qa
tags:
- android-studio
- mobile
- testing
author: estefafdez
---
¡Hola a todos!

Continuamos en esta entrada con el proyecto Android Barista, en esta entrada hablaremos de cómo desarrollar test con Barista en un proyecto de Android. ¡Comenzamos!

* * *

### URL Repositorio: https://github.com/estefafdez/AndroidBaristaProject

* * *

## ![11](/img/blog-images/old-post/2018/04/11.png)

En esta sección hablaremos de cómo hacer pruebas automáticas de UI en Android usando Barista.

### ¿Qué es Barista?

Como comentamos en la entrada anterior, Barista es una herramienta basada en Espresso para realizar test automáticos en Android a más alto nivel que con Espresso.

En Barista, hay una serie de acciones ya definidas como por ejemplo: hacer click en un botón, hacer scroll en una lista, seleccionar un item, pasar de página... que conociendo el id del elemento, podremos usarlas para interactuar con él de forma sencilla.

También tiene acciones de assert para hacer diferentes comprobaciones como si un elemento está visible, tiene un texto concreto, está activado...

Es lo más parecido a Appium que podemos encontrar pero de forma nativa en Android.

Más info sobre Barista: [https://github.com/SchibstedSpain/Barista](https://github.com/SchibstedSpain/Barista)

### ¿Cómo empezar?

#### Requisitos mínimos:

- Tener Android Studio descargado.
- Tener un proyecto de Android, se puede usar el repositorio creado para Barista: [https://github.com/estefafdez/AndroidBaristaProject](https://github.com/estefafdez/AndroidBaristaProject)
- Conocer las acciones que soporta Barista, detalladas en su README.MD: [https://github.com/SchibstedSpain/Barista](https://github.com/SchibstedSpain/Barista)

Para comenzar con Barista debemos comenzar con incluir el repositorio de Google en Maven en el build.gradle ya que es obligatorio para Espresso 3. Nos vamos al build.gradle del proyecto y añadimos:

```groovy
allprojects {
    repositories {
        jcenter()
        maven { url "https://maven.google.com" }
    }
}
```

![Captura de pantalla 2018-11-04 a las 14.37.59](/img/blog-images/old-post/2018/11/captura-de-pantalla-2018-11-04-a-las-14-37-59.png)

A continuación, importamos Barista como una dependencia de testing en el build.gradle de la app:

```groovy
androidTestCompile('com.schibsted.spain:barista:2.7.0') {
    exclude group: 'com.android.support'
}
```

![Captura de pantalla 2018-11-04 a las 14.39.12](/img/blog-images/old-post/2018/11/captura-de-pantalla-2018-11-04-a-las-14-39-12.png)

Si necesitamos otro [paquete de Espresso](https://developer.android.com/topic/libraries/testing-support-library/packages.html#atsl-dependencies) podemos añadirlo al proyecto sin ningún problema.

### Creando nuestro primer test:

Cuando tenemos importadas las dependencias y el repositorio, nos vamos a **app/src/androidTest** y creamos una clase .java para nuestros test, a la que llamaremos BaristaTest.java. En esta clase debemos añadir:

#### La regla de barista:

```java
@Rule
public BaristaRule<MainActivity> baristaRule = BaristaRule.create(MainActivity.class);
```

Esta regla hace varias cosas por defecto:

- Si tenemos definidos fraky tests, realiza 10 intentos de cada uno.
- Por defecto el lanzador de actividades automáticas está a falso.
- El modo de inicio de touch está a true.
- Borra las preferencias
- Borra los datos
- Limpia los ficheros.

#### TestName:

Añadimos también el método TestName de jUnit para usarlo en el log y saber qué test estamos ejecutando.

```java
TestName name = new TestName();
```

#### Método setUp():

Antes de comenzar a crear los test necesitamos un método que se realice siempre antes de todos los test y que lance la Activity principal del proyecto.

Para no tener que repetir esta línea en cada test, usaremos la anotación **@Before** de jUnit:

```java
@Before
public void setUp(){
    Log.i("Info","[START] - Launch Test: " + name.getMethodName());
    baristaRule.launchActivity();
}
```

En este método añadimos en el log el nombre del test que estamos ejecutando y lanzamos la Activity principal del proyecto.

#### Método tearDown():

Además de definir un método al inicio, debemos definir otro método fin para ejecutarse siempre después de cada test.

En este método podemos incluir todas las acciones que se realicen siempre al finalizar los test, por ahora, sólo indicaremos en el log el test que ha terminado.

Usaremos para ello la anotación **@After** de jUnit:

```java
@After
public void tearDown(){
    Log.i("Info", "[FINISH] - Test: " + name.getMethodName());
}
```

#### Creando nuestro primer test:

Cuando tenemos todo esto definido, pasamos a crear nuestro primer test donde comprobaremos si se muestra un botón:

```java
@Test
public void testTextoIsDisplayed(){
    BaristaVisibilityAssertions.assertDisplayed(R.id.texto);
    Log.i("Info", "The element text is displayed.");
}
```

Siempre debemos empezar con la anotación **@Test** antes de escribir el test. Es una buena práctica escribir _**test+NombreTest**_ para nombrar los test que creamos.

En este test, usamos el método _**assertDisplayed**_ dentro de _**BaristaVisibilityAssertions**_ donde en el parámetro indicamos el id del botón que queremos comprobar.

Si esta comprobación es correcta, se escribirá en el log que el botón1 se muestra.

#### Ejecutando nuestro primer test.

Una vez que tenemos el test creado, pasaremos a ejecutarlo, para ello debemos poner el ratón encima del test, hacemos click con el botón derecho y le damos a Run:

![Captura de pantalla 2018-11-04 a las 14.43.57](/img/blog-images/old-post/2018/11/captura-de-pantalla-2018-11-04-a-las-14-43-57.png)

El emulador se abrirá y el test comenzará a ejecutarse. Una vez que termine, podremos ver los resultados:

![Captura de pantalla 2018-11-04 a las 14.44.39](/img/blog-images/old-post/2018/11/captura-de-pantalla-2018-11-04-a-las-14-44-39.png)

Y así podemos hacer test usando Barista de forma sencilla.

En la próxima entrada seguiremos hablando sobre pruebas móviles sobre Android y hablaremos de Appium y cómo hacer pruebas con esta aplicación.

¡Nos leemos en la siguiente entrada!
