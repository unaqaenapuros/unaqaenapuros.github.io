---
title: '044 - Automatización de Pruebas móviles: Barista-Test Recorder.'
date: '2018-05-30T07:00:58+00:00'
url: /2018/05/30/044-automatizacion-de-pruebas-moviles-barista-test-recorder/
image: /img/blog-images/wp-posts/2018/04/foto43.jpg
categories:
- appium
- mobile-apps
- automation
- code-quality
- qa
tags:
- barista-test-recorder
- mobile-testing
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a hablar de **Barista-Test Recorder**, una aplicación bastante curiosa y que nos puede ayudar a empezar a automatizar pruebas funcionales en dispositivos móviles. ¡Comenzamos!

### ¿Qué es Barista-Test Recorder?

Barista es una aplicación Android disponible en el Google Play Store que nos permite, mediante el uso de los servicios de accesibilidad de Android, capturar acciones realizadas por el usuario dentro de una app a probar. El mismo usuario puede realizar comprobaciones en un elemento, hacer acciones, enviar datos... y poder exportar estas acciones como un test automático para Appium, Espresso o UIAutomator.

### ¿Dónde podemos encontrar Barista?

Puedes descargarla desde el siguiente enlace:

[https://play.google.com/store/apps/details?id=com.moquality.barista](https://play.google.com/store/apps/details?id=com.moquality.baristahttps://play.google.com/store/apps/details?id=com.moquality.barista)

\* **Nota**: Sólo está disponible para dispositivos Android.

### ¿Qué acciones podemos realizar con Barista?

![b1](/img/blog-images/wp-posts/2018/04/b1.png)Podemos grabar acciones sobre cualquier aplicación y exportar el resultado de esas acciones como un test automático en Appium, Expresso o UIAutomator.Podemos limpiar los datos de la aplicación de forma sencilla realizando el gesto de slide hacia la izquierda. De esta forma comenzaremos nuestro test de la aplicación sin datos previos para crear una prueba "limpia" como si el usuario abriera la aplicación por primera vez.![b2](/img/blog-images/wp-posts/2018/04/b2.png)![b3](/img/blog-images/wp-posts/2018/04/b3.png)En cada aplicación que queramos grabar acciones, nos encontraremos un asistente flotante (la taza del icono de Barista en este caso) donde podemos hacer click cuando queramos y de forma sencilla para ver las acciones que podemos realizar.Al hacer click en el asistente, nos despliega una serie de opciones, estas son:

- Añadir un check (assert) en un elemento, por ejemplo para comprobar si un elemento está presente o visible.
- Añadir un comentario en el código: por si necesitamos dejar una notación a la hora de exportar el código.
- Hacer una captura de pantalla, en el caso de que lo necesitemos como paso.
- Terminar y enviar el test creado una vez finalizada la prueba.
- Terminar la sesión.

![b4](/img/blog-images/wp-posts/2018/04/b4.png)![b5](/img/blog-images/wp-posts/2018/04/b5.png)Cada vez que queramos comprobar un elemento (por ejemplo checkear que está presente), seleccionamos ese elemento a checkear y la acción que queremos hacer. Además de eso en la parte baja de la pantalla, nos aparecerá la información en tiempo de ejecución de las propiedades de ese elemento: el ID, la posición...Las acciones que podemos realizar sobre un elemento son:

- **Displayed**: podemos comprobar si el elemento se está mostrando o no.
- **Completely displayed**: comprobar si el elemento se ha mostrado completamente.
- **Enabled**: Comprobamos si el elemento está habilitado para realizar cualquier acción.
- **Matches text**: Comprobamos si el elemento contiene un texto concreto.
- **Matches text part**: Comprobamos si el elemento contiene parte de un texto.
- **Store text in var**: guardamos el texto de un elemento en una variable.
- **Clickable**: comprobamos si un elemento es clickable.
- **Check Everything**: comprobamos todas las propiedades del elemento.
- **Cancel check**: cancelamos la comprobación.

![b6.png](/img/blog-images/wp-posts/2018/04/b6.png)![b7](/img/blog-images/wp-posts/2018/04/b7.png)Por último, antes de enviar el test por correo, podemos comprobar los pasos y acciones que hemos hecho  y podemos dar un nombre y una descripción al test que hemos completado. Después de esto, al hacer click en enviar, la aplicación enviará el código generado a la cuenta de google que está sincronizada en el sistema.

### Ejemplo de código generado por Barista.

Para terminar este ejemplo vamos a hacer un ejemplo de test básico y lo vamos a exportar usando la aplicación para ver el código auto-generado que nos envía por correo. Para ello vamos a realizar las siguientes acciones en una aplicación calculadora que puedes descargar [aquí:](https://www.dropbox.com/s/c95x6nktn0oyff2/calculadoraQA.apk?dl=0)

1. Abrimos la aplicación de calculadora.
1. Comprobamos si está presente el botón del número 1.
1. Hacemos click en el botón del número 1.
1. Comprobamos si está presente el botón de +.
1. Hacemos click en el botón +.
1. Comprobamos si está presente el botón del número 2.
1. Hacemos click en el botón 2.
1. Comprobamos si está presente el botón =.
1. Hacemos click en el botón =.
1. Comprobamos que en el elemento resultado aparece el texto 1+2=3 (la operación que acabamos de hacer).

Os dejo un video para que podáis ver lo sencillo que es. Lo he hecho utilizando el emulador de Android con la aplicación de Barista y la calculadora instalada:

\https://www.youtube.com/watch?v=DOWvtUljvM8&w=560&h=315\

Después de hacer estas acciones la aplicación nos envía el siguiente correo:

![mail](/img/blog-images/wp-posts/2018/04/mail.png)

Hacemos click en _**here**_ para ver el test y nos lleva a la siguiente página.

![exp](/img/blog-images/wp-posts/2018/04/exp.png)

Nos aparecen las 3 opciones, nosotros elegiremos **Appium** para ver el código.

Al hacer click en descargar (download) nos descarga el siguiente código:

```
package com.sample.foo.samplecalculator;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.TouchAction;
import org.junit.After;
import org.junit.Assert.*;
import org.junit.Before;
import org.junit.Test;
import org.openqa.selenium.By;
import org.openqa.selenium.remote.DesiredCapabilities;
import java.io.File;
import java.net.URL;
import static org.hamcrest.CoreMatchers.*;
import static org.junit.Assert.*;

public class SampleCalculatorTest {

privateAndroidDriverdriver;

@Before
publicvoidsetUp() throwsException {
// set up appium
FileclasspathRoot=newFile(System.getProperty("user.dir"));

//TODO: Set correct ClassPath
//File appDir = new File(classpathRoot, "\SampleCalculator\app\build\outputs\apk");
Fileapp=newFile(appDir, "app-debug.apk");

DesiredCapabilitiescapabilities=newDesiredCapabilities();
 capabilities.setCapability("deviceName","Android");
 capabilities.setCapability("platformVersion", "6.0");
 capabilities.setCapability("app", app.getAbsolutePath());
 capabilities.setCapability("appPackage", "com.sample.foo.samplecalculator");
 capabilities.setCapability("appActivity", "com.sample.foo.samplecalculator.MainActivity");
 driver = new AndroidDriver(new URL("http://127.0.0.1:4723/wd/hub"), capabilities);
}

@After
publicvoidtearDown() throwsException {
 driver.quit();
}

/**
* Test for SampleCalculator
* @author - estefafdez@gmail.com
* Generated using Barista - http://moquality.com/barista
*/

@Test
publicvoidtest_SampleCalculatorTest(){

 assertThat(driver.findElement(By.id("buttonOne")).isDisplayed(), is(true));
 driver.findElement(By.id("buttonOne")).click();
 assertThat(driver.findElement(By.id("buttonAdd")).isDisplayed(), is(true));
 driver.findElement(By.id("buttonAdd")).click();
 assertThat(driver.findElement(By.id("buttonTwo")).isDisplayed(), is(true));
 driver.findElement(By.id("buttonTwo")).click();
 assertThat(driver.findElement(By.id("buttonEqual")).isDisplayed(), is(true));
 driver.findElement(By.id("buttonEqual")).click();
 assertEquals(driver.findElement(By.id("infoTextView")).getText().toString(),"1+2 = 3");
}
}

```

* * *

Con esto termina nuestro tutorial sobre Barista-Test Recorder, una forma sencilla y fácil de generar test automáticos con **Appium**.

En la siguiente entrada hablaremos de Barista (framework basado en _Espresso_) para crear test automáticos en Android usando código.

¡Nos leemos en la siguiente entrada!
