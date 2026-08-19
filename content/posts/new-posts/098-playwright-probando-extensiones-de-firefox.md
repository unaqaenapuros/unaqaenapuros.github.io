---
title: '098 – Playwright: Probando extensiones de Firefox.'
date: '2026-11-30T09:30:00+01:00'
url: /2026/11/30/098-playwright-probando-extensiones-de-firefox/
image: /img/blog-images/new-posts/2026/11/foto87.png
categories:
- automation
- best-practices
- playwright
- qa
tags:
- testing
author: estefafdez
---
<!--
## Resumen para LinkedIn

¿Alguna vez te has preguntado cómo se prueba una extensión de navegador? No es lo mismo que testear una web normal: tiene su propia arquitectura, sus propias limitaciones y sus propias trampas. En esta entrada explico paso a paso cómo probar una extensión de Firefox real con Playwright, desde la configuración hasta los tests de renderizado, dark mode, caché offline y más.

#Playwright #QA #TestAutomation #Firefox #UnaQAEnApuros
-->

¡Hola a todos!

¿Te has preguntado alguna vez cómo se prueba una extensión de navegador? ¿Lo has intentado y no has sabido ni por dónde empezar? Por regla general, las extensiones siempre se prueban a mano. El razonamiento es entendible: no es una aplicación web al uso, así que se asume que las herramientas habituales no sirven y que montar un sistema de tests costaría demasiado tiempo y esfuerzo. Pero eso no es así, y hoy te lo demuestro: con **Playwright** puedes probar una extensión de Firefox exactamente igual que cualquier otra aplicación. Hoy te cuento cómo.

Vamos a usar como ejemplo una extensión real: **[Weather & Clock Dashboard](https://addons.mozilla.org/en-US/firefox/addon/weather-clock-dashboard/)**, una extensión de **nueva pestaña** para Firefox que muestra el tiempo, la hora local y un reloj mundial configurable. Es un caso perfecto porque tiene partes interesantes de testear: llamadas a una API externa, estado persistido en `localStorage`, modo oscuro, y una interfaz que se monta al abrir una nueva pestaña. ¡Empezamos!

---

### ¿Qué es una extensión de navegador?

Antes de entrar en los tests, necesitamos tener claro qué es lo que estamos probando. Una **extensión de navegador** es un pequeño programa que se integra en el navegador y amplía o modifica su comportamiento. Técnicamente, es un conjunto de ficheros web (HTML, CSS, JavaScript) empaquetados con un fichero especial llamado **`manifest.json`** que le dice al navegador qué puede hacer esa extensión y qué permisos necesita.

Las partes más habituales de una extensión son:

- **Popup**: la ventanita que aparece al hacer clic en el icono de la extensión en la barra del navegador.
- **New Tab Override**: sustituye la nueva pestaña por una página HTML propia. Es el caso de nuestra extensión de ejemplo.
- **Content Scripts**: JavaScript que se inyecta en páginas web externas para modificarlas.
- **Background Scripts / Service Worker**: código que corre en segundo plano, sin interfaz visual.
- **Options Page**: una página de configuración de la extensión.

Lo importante es entender que una extensión **no es una aplicación web normal**: vive en un contexto especial del navegador, tiene acceso a APIs privilegiadas (`browser.tabs`, `browser.storage`…) y sus páginas se cargan con protocolos especiales (`moz-extension://` en Firefox, `chrome-extension://` en Chrome).

Esto es precisamente lo que hace que testearlas sea diferente.

---

### ¿Por qué los tests unitarios no son suficientes?

Esta es la pregunta que siempre surge. Y la respuesta es sencilla: los tests unitarios no cubren los modos de fallo más importantes de una extensión. Puedes tener el 100% de cobertura unitaria y aun así no saber si la extensión funciona de verdad.

¿Qué escenarios no cubre un test unitario?

- ¿La extensión se carga correctamente en Firefox?
- ¿La nueva pestaña se activa y muestra la interfaz esperada?
- ¿El dark mode aplica los estilos correctos en el DOM?
- ¿El widget del tiempo muestra datos cuando hay una ciudad configurada?
- ¿La extensión sobrevive a un recargo de página con el estado guardado?
- ¿Qué ocurre cuando la API del tiempo no responde?

Ninguna de estas preguntas la responde un test unitario, porque todas implican un **navegador real** corriendo una **interfaz real** con **interacciones reales**. Aquí es donde entran los tests E2E, y aquí es donde Playwright nos salva.

---

### Preparando el entorno.

Lo primero es instalar Playwright y descargar el binario de Firefox si no lo tienes ya:

```bash
npm install --save-dev @playwright/test
npx playwright install firefox
```

Con esto tenemos todo lo necesario para empezar. Playwright descarga su propio binario de Firefox (no usa el que tengas instalado en el sistema) para garantizar versiones reproducibles y controladas.

---

### Configurando Playwright para Firefox.

Ahora configuramos el proyecto. El fichero `playwright.config.ts` es el punto de entrada para decirle a Playwright cómo lanzar el navegador:

```typescript
// playwright.config.ts
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  testDir: './tests',
  use: {
    browserName: 'firefox',
  },
  projects: [
    {
      name: 'firefox-extension',
      use: {
        ...devices['Desktop Firefox'],
      },
    },
  ],
});
```

Hasta aquí, nada especial. Pero en cuanto necesitamos cargar la extensión real dentro del navegador, la cosa se complica un poco. Y hay algo que debes saber desde el principio.

---

### El problema con Firefox, las extensiones y el modo headless.

Aquí viene el primer punto que te va a ahorrar horas de confusión: **Firefox no permite cargar extensiones en modo headless durante los tests**.

En Chrome, Playwright tiene una API específica que te permite cargar una extensión empaquetada y obtener su ID de forma programática. En Firefox, esa API **no existe de la misma manera**. Firefox requiere que el navegador corra en **modo headful** (con ventana visible) para que las extensiones se activen correctamente en modo desarrollo. El motivo es una limitación de la arquitectura de extensiones de Firefox: en modo headless, algunas partes del ciclo de vida de la extensión no se inicializan.

Para lanzar Firefox con una extensión cargada, necesitaríamos algo así:

```typescript
// launcher.ts — para referencia, no es el enfoque recomendado para new tab extensions
import { firefox } from 'playwright';
import path from 'path';

async function launchFirefoxWithExtension() {
  const extensionPath = path.resolve(__dirname, '..');

  const browser = await firefox.launch({
    headless: false, // Firefox necesita modo headful para extensiones en desarrollo
    firefoxUserPrefs: {
      'extensions.autoDisableScopes': 0, // no deshabilitar extensiones temporales
      'extensions.enabledScopes': 15,    // habilitar todos los scopes
    },
  });

  const context = await browser.newContext();
  return { browser, context };
}
```

El problema con este enfoque es que en un entorno de CI (donde no hay pantalla), necesitas una pantalla virtual (como `xvfb` en Linux), lo que añade complejidad. Para extensiones de tipo **new tab**, hay un enfoque mucho más práctico y mantenible.

---

### El enfoque recomendado: probar el HTML directamente.

Para extensiones de nueva pestaña como la nuestra, **la estrategia más robusta y pragmática es cargar el HTML de la extensión directamente** en el navegador, usando el protocolo `file://`. Esto funciona porque el contenido de la nueva pestaña es, al fin y al cabo, un fichero HTML con JavaScript y CSS. No necesitamos que el navegador lo trate como una extensión para probar la lógica y la interfaz.

Este enfoque tiene varias ventajas importantes:

- **Funciona en modo headless**: no necesitamos pantalla virtual en CI.
- **Es más rápido**: no hay que esperar a que la extensión se registre.
- **Cubre el 90% de los casos**: todos los tests de UI, lógica de estado y comportamiento de la interfaz funcionan igual.
- **Más estable**: no depende de APIs internas de Firefox que pueden cambiar entre versiones.

La única limitación real es que no podemos probar los permisos específicos de la extensión (como el acceso a `browser.tabs` o al historial). Para eso sí necesitaríamos la extensión cargada. Pero para la mayoría de los casos de uso, el enfoque de HTML directo es la solución correcta.

Definimos la URL de la nueva pestaña al principio del fichero de tests:

```typescript
// tests/extension.spec.ts
import { test, expect } from '@playwright/test';
import path from 'path';

// apuntamos directamente al HTML de la nueva pestaña
const NEW_TAB_URL = `file://${path.resolve(__dirname, '../newtab.html')}`;
```

---

### Probando el renderizado del widget del tiempo.

El primer test que queremos escribir es el más básico: ¿muestra la extensión los datos del tiempo cuando hay una ciudad configurada?

Aquí tenemos dos cosas interesantes. Primero, necesitamos simular la respuesta de la API del tiempo para no depender de un servicio externo en los tests (esto es fundamental: los tests deben ser **deterministas** y no fallar por problemas de red o por límites de uso de la API). Para eso usamos `page.route()`, que intercepta las peticiones de red y devuelve la respuesta que queramos.

Segundo, la extensión lee la ciudad desde `localStorage`. Para precargar ese valor antes de que el HTML se ejecute, usamos `page.addInitScript()`.

```typescript
test('renders the weather widget with city data', async ({ page }) => {
  // interceptamos la API del tiempo y devolvemos datos controlados
  await page.route('**/api.openweathermap.org/**', route => {
    route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify({
        name: 'Sevilla',
        sys: { country: 'ES' },
        weather: [{ main: 'Clear', description: 'despejado', icon: '01d' }],
        main: { temp: 22, feels_like: 20, humidity: 40 },
      }),
    });
  });

  // precargamos la ciudad en localStorage antes de que la página cargue
  await page.addInitScript(() => {
    localStorage.setItem('city', 'Sevilla');
  });

  await page.goto(NEW_TAB_URL);
  await page.waitForTimeout(1500); // esperamos a que el widget cargue los datos

  // comprobamos que los datos del tiempo se muestran
  await expect(page.locator('#weather-temp')).toContainText('22');
  await expect(page.locator('#weather-city')).toContainText('Sevilla');
  await expect(page.locator('#weather-description')).toContainText('despejado');
});
```

Un par de notas sobre este test:

- El `waitForTimeout` lo usamos aquí porque la extensión hace la llamada a la API de forma asíncrona al cargar. En tests más sofisticados, lo reemplazaríamos por un `waitFor` sobre el elemento esperado, que es más robusto. Pero para empezar, este enfoque es perfectamente válido.
- El `page.route()` con el patrón glob `**/api.openweathermap.org/**` captura cualquier URL que contenga ese dominio, independientemente de los parámetros que lleve. Así no necesitamos conocer la URL exacta.

---

### Probando el modo oscuro.

El dark mode es un caso interesante porque implica **persistencia de estado**: cuando el usuario activa el modo oscuro, la preferencia se guarda en `localStorage` y debe recuperarse al recargar la página. Esto es exactamente el tipo de comportamiento que un test unitario no puede validar.

```typescript
test('dark mode toggle persists across reload', async ({ page }) => {
  await page.goto(NEW_TAB_URL);

  // comprobamos que empieza en modo claro
  await expect(page.locator('body')).not.toHaveClass(/dark/);

  // activamos el modo oscuro haciendo clic en el botón
  await page.click('#theme-toggle');
  await page.waitForTimeout(300);

  // comprobamos que el tema cambió
  await expect(page.locator('body')).toHaveClass(/dark/);

  // recargamos la página — el tema debe persistir
  await page.reload();
  await page.waitForTimeout(500);

  await expect(page.locator('body')).toHaveClass(/dark/);
});
```

Este test nos da una garantía importante: no solo que el botón funciona, sino que la **persistencia del estado** funciona correctamente. Si alguien rompe la lógica de guardar la preferencia en `localStorage`, este test lo detecta.

---

### Probando el reloj mundial.

La extensión permite configurar relojes de distintas ciudades del mundo. Para testear esto, necesitamos precargar la configuración de los relojes en `localStorage` antes de que la página cargue, igual que hicimos con la ciudad del tiempo:

```typescript
test('world clock displays configured cities', async ({ page }) => {
  // precargamos la configuración del reloj mundial
  await page.addInitScript(() => {
    localStorage.setItem('worldClocks', JSON.stringify([
      { label: 'Tokyo', timezone: 'Asia/Tokyo' },
      { label: 'Londres', timezone: 'Europe/London' },
    ]));
  });

  await page.goto(NEW_TAB_URL);
  await page.waitForTimeout(1000);

  const clocks = await page.locator('.world-clock').all();
  expect(clocks).toHaveLength(2);

  await expect(clocks[0]).toContainText('Tokyo');
  await expect(clocks[1]).toContainText('Londres');

  // comprobamos que el tiempo mostrado tiene formato HH:MM
  const tokyoTime = await clocks[0].locator('.clock-time').textContent();
  expect(tokyoTime).toMatch(/\d{1,2}:\d{2}/);
});
```

Fíjate en el último assert: no comprobamos que la hora sea un valor concreto (eso cambiaría cada vez que ejecutamos el test), sino que tiene el **formato correcto**. Esta es una técnica habitual en QA: cuando el valor exacto no es predecible, valida el formato o el tipo de dato.

---

### Probando el comportamiento offline.

Este es uno de mis tests favoritos de esta extensión, porque cubre un caso de uso real que la mayoría de la gente no testea: ¿qué pasa cuando no hay conexión a internet? Una extensión bien hecha debería mostrar los datos cacheados en lugar de un error.

El truco es usar `page.route()` para abortar las peticiones a la API, simulando que no hay red. Antes, precargamos datos en la caché (`localStorage`) para que la extensión tenga algo que mostrar:

```typescript
test('shows cached weather data when offline', async ({ page }) => {
  // precargamos datos cacheados en localStorage
  await page.addInitScript(() => {
    const cachedData = {
      data: {
        name: 'Sevilla (caché)',
        main: { temp: 18 },
        weather: [{ description: 'nublado' }],
      },
      timestamp: Date.now() - 1000, // cacheado hace 1 segundo
    };
    localStorage.setItem('cache_weather', JSON.stringify(cachedData));
  });

  // simulamos que no hay red abortando las peticiones a la API
  await page.route('**/api.openweathermap.org/**', route => {
    route.abort('failed');
  });

  await page.goto(NEW_TAB_URL);
  await page.waitForTimeout(2000);

  // la extensión debe mostrar los datos cacheados
  await expect(page.locator('#weather-city')).toContainText('Sevilla (caché)');
  await expect(page.locator('#weather-temp')).toContainText('18');

  // y debe indicar que está en modo offline
  const statusText = await page.locator('#weather-status').textContent();
  expect(statusText?.toLowerCase()).toContain('offline');
});
```

Este test verifica una **degradación elegante**: la extensión no rompe cuando no hay conexión, sino que ofrece la mejor experiencia posible con los datos disponibles. Si alguien elimina por error la lógica de caché, este test falla inmediatamente.

---

### Ejecutando los tests.

Para ejecutar los tests tenemos varias opciones útiles según el contexto:

```bash
npm test                          # todos los tests en modo headless
npm run test:headed               # con el navegador visible (útil para depurar)
npm run test:ui                   # modo interactivo con UI de Playwright
npx playwright test --debug       # paso a paso con el depurador
```

El script en `package.json` sería:

```json
{
  "scripts": {
    "test": "playwright test",
    "test:ui": "playwright test --ui",
    "test:headed": "playwright test --headed"
  }
}
```

El modo `--ui` es especialmente útil cuando estás escribiendo tests nuevos o depurando fallos: te da una interfaz visual donde puedes ver la ejecución paso a paso, inspeccionar el DOM en cada momento y ver el vídeo de la ejecución.

---

### Integración en CI con GitHub Actions.

Una de las grandes ventajas del enfoque de HTML directo es que **funciona en CI sin configuración extra**. No necesitamos pantalla virtual, no necesitamos nada especial. La configuración de GitHub Actions es minimalista:

```yaml
# .github/workflows/test.yml
- name: Run extension E2E tests
  run: |
    npx playwright install firefox
    npm test
```

Si hubiéramos optado por cargar la extensión real en Firefox con `headless: false`, necesitaríamos añadir `xvfb` (X Virtual Framebuffer) para crear una pantalla virtual en el servidor de CI. Eso no es imposible, pero añade complejidad y fragilidad. El enfoque de HTML directo elimina ese problema por completo.

---

### Conclusión.

  * Probar extensiones de navegador es diferente a probar una aplicación web normal, pero perfectamente factible con **Playwright** y el enfoque correcto.
  * Los **tests unitarios no son suficientes** para extensiones: no validan que la extensión cargue, que el DOM se monte bien ni que el estado persista entre recargas.
  * En Firefox, la estrategia más robusta para extensiones de nueva pestaña es **cargar el HTML directamente** con `file://`, lo que además elimina la dependencia de pantalla en CI.
  * **`page.route()`** es tu mejor aliado para simular APIs externas y comportamientos offline sin depender de servicios de red.
  * **`page.addInitScript()`** te permite precargar el estado en `localStorage` antes de que la página ejecute su JavaScript, fundamental para testear configuraciones previas.
  * Las pruebas de **persistencia de estado** (como el dark mode) y de **degradación offline** son los casos más valiosos de testear, y los que más se pasan por alto.

* * *

Y hasta aquí nuestra entrada sobre cómo probar extensiones de Firefox con Playwright. Y ahora te dejo con la pregunta del millón: ¿vas a animarte a probar una extensión tuya, de las que usas en tu día a día? Igual te llevas una sorpresa.

¡Nos leemos en la siguiente entrada!
