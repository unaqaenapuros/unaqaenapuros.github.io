---
title: '082 – Playwright (IV): Depuración y Trace Viewer.'
date: '2026-04-28T07:00:00+00:00'
url: /2026/04/28/082-playwright-iv-depuracion-y-trace-viewer/
image: /img/blog-images/wp-posts/2026/04/foto65.png
categories:
- automation
- best-practices
- playwright
- qa
tags:
- testing
author: estefafdez
---
¡Hola a todos!

En las entradas anteriores aprendimos a instalar Playwright, a ejecutar los tests y a escribirlos, pero cuando los tests fallan, necesitamos herramientas para entender qué ha pasado. En esta entrada veremos las diferentes formas de depurar tests con Playwright y cómo usar el **Trace Viewer** para analizar en detalle lo que ocurrió durante la ejecución. ¡Empezamos!

### Opciones de ejecución para depurar.

Antes de entrar en las herramientas de depuración, conviene recordar que Playwright ofrece varios **flags** de ejecución que nos pueden ayudar a entender qué está pasando:

- **`--headed`**: Ejecuta los tests con el navegador visible para poder ver cómo interactúa con la página.
- **`--project=chromium`**: Ejecuta los tests solo en el navegador indicado, reduciendo el ruido.
- **`--last-failed`**: Re-ejecuta únicamente los tests que fallaron en la última ejecución, muy útil para iterar rápido cuando estamos arreglando un fallo.

Un ejemplo de usar todo esto sería:

```
# Solo tests fallidos, con navegador visible, solo en Chromium
npx playwright test --last-failed --headed --project=chromium

```

### Depurando con UI Mode.

La forma más cómoda de depurar tests es usando el **UI Mode**, que ya mencionamos en la entrada anterior. Lo activamos con:

```
npx playwright test --ui

```

El **UI-Mode** nos permite:

- **Inspeccionar cada paso** del test con detalle, viendo el estado del navegador antes y después de cada acción.
- **Time travel debugging**: podemos retroceder y avanzar por los pasos del test para ver exactamente en qué momento empezó a fallar algo.
- Ver los **logs**, **errores**, **peticiones de red** y la **consola del navegador** en cada paso.
- Usar el **locator picker** para inspeccionar elementos de la página y obtener sus locators de forma interactiva, lo que es muy útil cuando estamos escribiendo tests nuevos.

El UI Mode es la herramienta recomendada para el desarrollo y depuración local de tests.

{{< figure src="/img/blog-images/wp-posts/2026/04/screenshot-2026-04-10-at-18.38.23.png?w=1024" alt="" caption="" >}}

### Playwright Inspector.

Para una depuración más clásica, al estilo "paso a paso", Playwright incluye el **Playwright Inspector**. Para activarlo, añadimos el flag `--debug`:

```
npx playwright test --debug

```

Con el Inspector podemos:

- **Ejecutar los tests paso a paso**, deteniéndonos en cada acción de Playwright.
- Ver los **logs de depuración** de cada llamada a la API de Playwright.
- **Explorar locators** en la propia ventana del navegador.
- **Modificar el test en caliente** y ver el efecto inmediato.

{{< figure src="/img/blog-images/wp-posts/2026/04/screenshot-2026-04-10-at-18.40.25.png?w=1024" alt="" caption="" >}}

Si solo queremos depurar un test concreto, podemos combinarlo con el nombre del test:

```
npx playwright test -g "nombre del test" --debug

```

También podemos usar **`page.pause()`** directamente en el código del test para detener la ejecución en un punto concreto y abrir el Inspector:

```
test('mi test', async ({ page }) => {
  await page.goto('https://ejemplo.com');
  await page.pause(); // La ejecución se pausa aquí y se abre el Inspector
  await page.getByRole('button', { name: 'Login' }).click();
});

```

{{< figure src="/img/blog-images/wp-posts/2026/04/screenshot-2026-04-10-at-18.42.38.png?w=1024" alt="" caption="" >}}

### Trace Viewer.

El **Trace Viewer** es una herramienta GUI de Playwright que nos permite explorar las trazas ( _traces_) grabadas durante la ejecución de los tests. Una traza es un registro completo de todo lo que ocurrió durante el test: cada acción, cada estado del DOM, cada petición de red, cada screenshot...

#### ¿Cuándo se graban las trazas?

Por defecto, la configuración generada por Playwright establece que las trazas se graben **en el primer reintento de un test fallido** ( _on-first-retry_). Así está configurado en el `playwright.config.ts`:

```
import { defineConfig } from '@playwright/test';

export default defineConfig({
  retries: process.env.CI ? 2 : 0, // 2 reintentos en CI, 0 en local
  use: {
    trace: 'on-first-retry', // graba la traza en el primer reintento
  },
});

```

Si queremos forzar la grabación de trazas en todos los tests (por ejemplo, para depurar localmente), podemos usar el flag `--trace on`:

```
npx playwright test --trace on

```

#### Abriendo el Trace Viewer.

Las trazas se pueden abrir de varias formas:

- Desde el **reporte HTML**: hacemos click en el icono de traza junto al nombre del test fallido.
- O directamente desde la vista detallada del test, en la pestaña "Traces".

{{< figure src="/img/blog-images/wp-posts/2026/04/monosnap-playwright-test-report-2026-04-10-18-45-30.png?w=1024" alt="" caption="" >}}

#### ¿Qué podemos ver en el Trace Viewer?

El Trace Viewer nos da una visión completa de la ejecución del test:

- **Timeline**: una línea de tiempo con todas las acciones del test. Podemos hacer click en cualquier acción para ver el estado del navegador en ese momento exacto.
- **Snapshot del DOM**: una captura del estado del DOM en cada paso, con la que podemos interactuar y abrir las DevTools del navegador para inspeccionar el HTML y CSS.
- **Logs**: los logs de Playwright para cada paso.
- **Errores**: los mensajes de error con el stack trace completo.
- **Peticiones de red**: todas las peticiones HTTP realizadas durante el test.
- **Consola del navegador**: los mensajes de consola.

El Trace Viewer es especialmente útil en entornos **CI/CD**, donde no podemos ver el navegador en tiempo real. Gracias a las trazas podemos analizar los fallos a posteriori con el mismo nivel de detalle que si hubiéramos estado viendo la ejecución en directo.

{{< figure src="/img/blog-images/wp-posts/2026/04/screenshot-2026-04-10-at-18.46.30.png?w=1024" alt="" caption="" >}}

### Conclusión.

- Para depurar tests en local, el **UI Mode** es la opción más completa y recomendada.
- Para una depuración paso a paso más clásica, usamos el **Playwright Inspector** con el flag `--debug`.
- Para analizar fallos en CI/CD, el **Trace Viewer** nos da toda la información necesaria sin necesidad de re-ejecutar los tests.
- Podemos combinar estos recursos con `--last-failed` para iterar rápido cuando arreglamos fallos.

* * *

Y hasta aquí nuestra entrada sobre depuración y Trace Viewer. En la siguiente entrada veremos cómo configurar Playwright para que se ejecute en un entorno de integración continua con **GitHub Actions**. ¡Nos leemos en la siguiente entrada!
