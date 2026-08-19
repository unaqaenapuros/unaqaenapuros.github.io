---
title: 051 - Como crear, ejecutar y eliminar emuladores de Android por consola.
date: '2019-04-10T09:00:53+00:00'
url: /2019/04/10/051-como-crear-ejecutar-y-eliminar-emuladores-de-android-por-consola/
image: /img/blog-images/wp-posts/2019/02/foto50.jpg
categories:
- android
- appium
- automation
- ci
- jenkins
- qa
tags:
- android-studio
- command-line
- emulators
- emulator
author: estefafdez
---
¡Hola a todos!

En esta entrada hablaremos de cómo crear, ejecutar y eliminar emuladores de Android de forma sencilla. ¡Comenzamos!

## ¿Por qué necesitamos conocer estos comandos?

Aunque podemos hacerlo con Android Studio (como ya vimos en [entradas anteriores](/2018/11/07/045-android-proyecto-android-barista-i/)), para mí es mucho más cómodo hacerlo por comandos en lugar de por Android Studio, además, de esta forma podremos utilizar los comandos para crear un entorno de CI (por ejemplo Jenkins) para lanzar nuestros test automáticos con Appium.

## ¿Para qué Sistema Operativo nos sirve?.

Los comandos valen tanto como para Linux, Mac o Windows. Lo que tendremos que adaptar en Windows serán las extensiones (.exe, .bat...).

## Conocer dónde está el SDK.

Lo primero que tenemos que hacer es saber dónde tenemos el SDK instalado. Para ello hemos tenido que definir la variable de entorno **ANDROID\_HOME** en nuestro sistema.

Para mí, **ANDROID\_HOME** es:

```
ANDROID_HOME= /Users/estefafdez/Library/Android/sdk/
```

Lo que iré haciendo a partir de ahora es dar las rutas a las que tenemos que acceder para cada comando partiendo de ANDROID\_HOME que será diferente para cada uno. La ruta que veis de mi sistema es la de por defecto en Mac.

## Crear un Emulador Android por consola.

Para crear un emulador necesitamos varias cosas previas:

1. Un nombre para el emulador, en el comando que os dé lo pondremos como el parámetro **EMULATOR\_NAME**.
1. Un tipo de arquitectura para el emulador. Nosotros usaremos **x86** ya que las últimas versiones de Android es la que se recomienda utilizar.
1. La API de Android que queremos utilizar, puede ser **23, 24, 25, 26, 27**... Para nosotros será el parámetro **ANDROID\_DEVICE\_API.**
1. Tipo de dispositivo: aunque Android Studio nos ofrece varios skins (móviles concretos) para crear, nosotros utilizaremos por defecto un **Nexus 5X** para tener una resolución buena. Si no indicamos este parámetro el emulador aparecerá demasiado pequeño.

Una vez que tenemos todo esto claro, para crear un emulador debemos de:

Ir a la carpeta tools/bin dentro del SDK:

```
cd ${ANDROID_HOME}"+"/tools/bin/"
```

Ahora utilizaremos el **avdmanager** para crear el emulador con los parámetros que hemos comentado anteriormente:

```
echo no | ./avdmanager create avd --force --name ${EMULATOR_NAME} --abi google_apis/x86 --package 'system-images;android-${ANDROID_DEVICE_API};google_apis;x86' --device "Nexus 5X"
Ejemplo parametrizado.
```

```
echo no | ./avdmanager create avd --force --name emulator_API_27 --abi google_apis/x86 --package 'system-images;android-27;google_apis;x86' --device "Nexus 5X"
Ejemplo con valores.
```

Cuando ejecutemos este comando ya tendremos nuestro emulador creado con los parámetros que hemos indicado.

## Ejecutar un Emulador Android por consola.

Una vez que hemos creado el emulador, vamos a ejecutar ese mismo desde la consola. Para ello vamos a darle varias propiedades para mejorar el rendimiento del emulador. Estas propiedades son:

- **engine-auto**: mejora rendimiento del emulador.

- **no-windows**: Esta opción sólo la usaremos para CI ya que hará que no se vea la pantalla del emulador. Esto mejorará los recursos del sistema en el que lancemos el simulador, en este caso no lo usaremos.

- **no-audio:** A no ser que tengamos que hacer pruebas de audio concretas, utilizaremos este parámetro para que no se escuche audio en el emulador.

- **wipe-data**: borra los datos anteriores del emulador si los hay.

- **no-cache**: Con este parámetro, el emulador no guardará datos cacheados.

- **memory**: Definimos la memoria máxima del emulador.

- **no-snapshot**: no guarda una imagen del emulador cuando éste se cierre después de usarlo.

- **no-boot-anim**: Con este parámetro no aparece el logo de Google al iniciar el emulador. Esto hace que vaya más rápido el arranque.

- **no-snapstorage**: Con este parámetro no se guardarán datos en la memoria del emulador.

Tenemos muchas más opciones para especificar, para mí esas son las más interesantes. Si queréis leer todas las disponibles podéis hacerlo [aquí](https://developer.android.com/studio/run/emulator-commandline).

Una vez que tenemos todo esto claro, para ejecutar un emulador debemos seguir los siguientes pasos:

Ir a la carpeta emulator dentro del SDK:

```
cd ${ANDROID_HOME}"+"/emulator/"
```

Ahora utilizaremos el comando **emulator** para ejecutar el emulador con los parámetros que hemos comentado anteriormente:

```
./emulator -avd ${EMULATOR_NAME} -engine auto -no-audio -wipe-data -no-cache -memory 3072 -no-snapshot -no-boot-anim -no-snapstorageCuando ejecutemos este comando ya tendremos nuestro emulador creado con los parámetros que hemos indicado.
```

Una vez que ejecutemos ese comando por consola tendremos el emulador abierto.

## Ver los Emuladores que tenemos creados en el sistema.

Para ver una lista de los emuladores que tenemos en el sistema debemos de seguir los siguientes pasos.

Ir a la carpeta emulator dentro del SDK:

```
cd ${ANDROID_HOME}"+"/emulator/"
```

Ahora utilizaremos el comando **emulator** para ejecutar la siguiente orden:

```
./emulator -list-avds
```

Con este comando tendremos una lista de todos los emuladores que tenemos creados en el sistema.

## Eliminar un Emulador Android por consola.

Para eliminar emuladores podemos hacerlo de varias formas, una borrando todos los emuladores creados y otra borrar un emulador concreto.

Las imágenes de los emuladores que se guardan al crear uno ( _ficheros .avd y .ini por cada emulador_) se crean en una carpeta en la siguiente ruta por defecto:

```
cd /Users/estefafdez/.android/avd
```

Para eliminar todos los emuladores que tengamos utilizaremos el comando:

```
rm -rf emulator_API*.*
NOTA: He utilizado emulator_API delante porque es la forma en la que nombro siempre los emuladores.
```

Para eliminar un emulador concreto, utilizaremos el siguiente comando:

```
rm -rf emulator_API_27.*
```

De esta forma se eliminarán del emulador que hemos creado antes tanto el fichero .avd como el .ini y ese emulador se eliminará completamente.

Y hasta aquí esta entrada. En la siguiente entrada hablaremos de cómo hacer capturas de pantalla de un emulador Android desde consola.

¡Nos leemos en la siguiente entrada!
