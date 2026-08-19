---
title: '080 – Playwright (II): Ejecutando los primeros tests.'
date: '2026-04-20T07:00:00+00:00'
url: /2026/04/20/080-playwright-ii-ejecutando-los-primeros-tests/
image: /img/blog-images/wp-posts/2026/04/foto63.png
categories:
- automation
- code-quality
- git
- playwright
- qa
tags:
- api
- ai
- testing
author: estefafdez
---
¡Hola a todos!

En la entrada anterior vimos qué es **Playwright** y cómo instalarlo. Ahora que ya tenemos el proyecto configurado, toca hablar de cómo ejecutar los tests y de las diferentes formas que tenemos de visualizar los resultados. ¡Empezamos!

# Nuestro proyecto de base.

Para poder ver ejemplos, usaremos de base un proyecto creado por mí en mi repositorio:

[https://github.com/estefafdez/playwright-template](https://github.com/estefafdez/playwright-template)

con una estructura básica de Playwright ya precreada para que puedas usarla y te sea más fácil tener una base por la que empezar.

Te aconsejo que te descargues el repo para seguir los siguientes pasos.

# Ejecutando los tests por primera vez.

La forma más básica de ejecutar todos los tests de nuestro proyecto es con el siguiente comando:

```
npx playwright test
```

Por defecto, los tests se ejecutan en modo **headless** (sin ventana de navegador visible) y en **paralelo** en todos los navegadores configurados en el fichero `playwright.config.ts` (en este caso sólo en Chrome). Los resultados se muestran directamente en el terminal como se puede ver en la imagen:

{{< figure src="/img/blog-images/wp-posts/2026/04/screenshot-2026-04-03-at-18.45.34.png?w=1024" alt="" caption="" >}}

Algunos modificadores útiles que podemos añadir a este comando son:

- **`--headed`**: lanza los tests con el navegador visible, para poder ver cómo se ejecutan.
- **`--project=chromium`**: ejecuta los tests solo en un navegador concreto.
- **`npx playwright test tests/web/login.spec.ts`**: ejecuta solo el fichero de tests indicado.
- **`--ui`**: abre el modo UI de Playwright, del que hablaremos más adelante.

### Reporte HTML.

Una vez finalizada la ejecución, Playwright genera automáticamente un **reporte HTML** con los resultados. Este reporte nos permite:

- Filtrar los tests por navegador, tests pasados, fallidos, omitidos ( _skipped_) y tests inestables ( _flaky_).
- Hacer click en cada test para ver los errores, los pasos ejecutados y los adjuntos (capturas de pantalla, vídeos, trazas...).

El reporte se abre automáticamente en el navegador cuando hay tests fallidos. Si queremos abrirlo manualmente, podemos hacerlo con:

```
npx playwright show-report
```

El reporte HTML es especialmente útil cuando ejecutamos los tests en un entorno CI/CD, ya que nos da toda la información necesaria para entender qué ha fallado sin necesidad de volver a ejecutar los tests.

{{< figure src="/img/blog-images/wp-posts/2026/04/screenshot-2026-04-03-at-18.48.02.png?w=1024" alt="" caption="" >}}

### UI Mode.

El **UI Mode** es una de las funcionalidades más potentes de Playwright. Para activarlo, usamos el flag `--ui`:

```
npx playwright test --ui
```

Con el UI Mode tenemos acceso a:

- **Watch mode**: Playwright re-ejecuta los tests automáticamente cuando detecta cambios en los ficheros.
- **Time travel debugging**: podemos ir hacia adelante y hacia atrás en la ejecución del test, viendo el estado del navegador en cada paso.
- **Locator picker**: herramienta para inspeccionar los elementos de la página y obtener sus locators de forma interactiva.
- **Visor de logs, errores y peticiones de red** para cada paso del test.

Si estamos desarrollando o depurando tests, el UI Mode es la opción más recomendable, ya que nos da una visión completa de lo que está pasando en cada momento.

{{< figure src="/img/blog-images/wp-posts/2026/04/screenshot-2026-04-03-at-18.51.03.png?w=1024" alt="" caption="" >}}

### Extensión de VS Code.

Playwright tiene una extensión oficial para **VS Code** que integra todas las capacidades del framework directamente en el editor. Para instalarla:

1. Abrimos la vista de extensiones de VS Code con `Ctrl+Shift+X` y buscamos "Playwright".
1. Instalamos la extensión oficial de **Microsoft**.
1. Abrimos la paleta de comandos con `Ctrl+Shift+P` y ejecutamos el comando `Test: Install Playwright`.
1. Seleccionamos los navegadores que queremos configurar.

{{< figure src="/img/blog-images/wp-posts/2026/04/screenshot-2026-04-03-at-18.52.21.png?w=1024" alt="" caption="" >}}

Una vez instalada, tenemos acceso al **Test Explorer** desde la barra lateral de VS Code. Desde aquí podemos:

- **Ejecutar un test individual**: hacemos click en el icono verde de "play" junto al test.
- **Ejecutar todos los tests** de un fichero o de todo el proyecto.
- **Ejecutar en múltiples navegadores**: marcamos los proyectos (navegadores) que queremos en el panel lateral de Playwright.
- **Show Browser**: activamos esta opción para ver el navegador durante la ejecución. Si la desactivamos, los tests se ejecutan en modo headless.

La extensión de VS Code es la forma más cómoda de trabajar con Playwright en el día a día, ya que nos permite ejecutar y depurar tests sin salir del editor.

{{< figure src="/img/blog-images/wp-posts/2026/04/screenshot-2026-04-03-at-18.54.46.png?w=1024" alt="" caption="" >}}

* * *

Y hasta aquí nuestra entrada sobre cómo ejecutar los primeros tests con Playwright. En la siguiente entrada aprenderemos a escribir nuestros propios tests desde cero: acciones, aserciones y buenas prácticas. ¡Nos leemos en la siguiente entrada!
