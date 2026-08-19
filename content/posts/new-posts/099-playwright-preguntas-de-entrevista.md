---
title: '099 – Playwright: 20 preguntas básicas para una entrevista técnica.'
date: '2026-12-14T09:30:00+01:00'
url: /2026/12/14/099-playwright-preguntas-de-entrevista/
image: /img/blog-images/new-posts/2026/12/foto88.png
categories:
- automation
- playwright
- qa
tags:
- interview
- questions
- testing
author: estefafdez
---
<!--
## Resumen para LinkedIn

Llevamos varios meses hablando de Playwright en el blog: instalación, fixtures, debugging, API testing, accesibilidad… Pero ¿qué pasa cuando te sientas en una entrevista técnica y te preguntan por lo más básico? En esta entrada repasamos 20 preguntas habituales sobre Playwright con respuestas completas para que llegues preparado.

#Playwright #QA #TestAutomation #Entrevista #UnaQAEnApuros
-->

¡Hola a todos!

Llevamos ya un buen puñado de entradas hablando de **Playwright**: desde la instalación hasta fixtures avanzadas, pasando por debugging, API testing, accesibilidad y hasta cómo probar extensiones de Firefox. Hemos cubierto mucho terreno. Pero hay algo que me parece importante hacer de vez en cuando: parar, mirar hacia atrás y asegurarnos de que los fundamentos están bien asentados.

¿Por qué? Porque una cosa es saber usar una herramienta en el día a día, y otra muy distinta es saber explicarla cuando alguien te pregunta en una entrevista técnica. A veces los conceptos más básicos son los que peor se verbalizan, precisamente porque los tenemos tan interiorizados que no nos hemos parado a articularlos. Y en una entrevista, si no puedes explicarlo con claridad, da igual que lo uses todos los días.

Así que vamos a repasar las **20 preguntas más habituales sobre Playwright** que puedes encontrarte en una entrevista. Para cada una, te doy la respuesta completa con el contexto que necesitas para que no te quedes en un "sí, lo uso, pero…".

---

### 1. ¿Qué es Playwright?

**Playwright** es un framework de automatización _open source_ desarrollado por **Microsoft** para realizar pruebas _end-to-end_ de aplicaciones web. Permite controlar navegadores de forma programática usando una única API, independientemente del navegador que estés usando.

Lo que lo distingue de otras herramientas es que fue diseñado desde cero pensando en las aplicaciones web modernas: SPAs, iframes, múltiples pestañas, peticiones de red, autenticación… todo está contemplado de serie.

Actualmente soporta TypeScript, JavaScript, Python, Java y .NET, aunque su uso más extendido es con **TypeScript**.

---

### 2. ¿Cuáles son las características principales de Playwright?

Las más importantes que debes conocer:

- **Soporte multi-navegador**: Chromium, Firefox y WebKit con la misma API.
- **Auto-waiting**: espera automáticamente a que los elementos estén listos antes de interactuar con ellos.
- **Ejecución headless y headed**: puedes correr los tests sin interfaz gráfica (ideal para CI) o con navegador visible (ideal para depurar).
- **Intercepción de red**: puedes interceptar, modificar y mockear peticiones HTTP desde los tests.
- **Ejecución en paralelo**: los tests corren en paralelo por defecto, lo que reduce significativamente el tiempo total de ejecución.
- **Test runner propio**: `@playwright/test` incluye todo lo necesario sin depender de frameworks externos como Jest o Mocha.
- **Trace Viewer**: una herramienta de depuración que graba toda la ejecución del test y te permite revisarla paso a paso.
- **Generador de código** (`codegen`): genera código de Playwright automáticamente mientras interactúas con el navegador.

---

### 3. ¿Qué navegadores soporta Playwright?

Playwright soporta tres motores de navegador:

- **Chromium**: el motor que usa Chrome y Edge.
- **Firefox**: el motor de Mozilla Firefox.
- **WebKit**: el motor de Safari (Apple).

Un punto importante que vale la pena mencionar en una entrevista: Playwright **no usa los navegadores que tengas instalados** en tu máquina. Descarga sus propios binarios controlados para garantizar versiones reproducibles y evitar que los tests fallen por actualizaciones del sistema. Esto se hace con `npx playwright install`.

---

### 4. ¿Qué es el auto-waiting?

El **auto-waiting** es uno de los mecanismos más importantes de Playwright y uno de los que más diferencian su comportamiento del de Selenium clásico.

Antes de ejecutar cualquier acción sobre un elemento (hacer clic, escribir, etc.), Playwright comprueba automáticamente que el elemento cumple una serie de condiciones:

- Que existe en el DOM.
- Que es **visible** (no está oculto con `display: none` o `visibility: hidden`).
- Que es **estable** (no está animándose ni moviéndose).
- Que está **habilitado** (no está `disabled`).
- Que es **interactuable** (no está tapado por otro elemento).

Si el elemento no cumple las condiciones, Playwright reintenta durante un tiempo configurable (por defecto 30 segundos) antes de fallar. Esto elimina la necesidad de poner `sleep()` o `waitForTimeout()` artificiales en el código, que son una de las principales causas de tests frágiles (_flaky tests_).

---

### 5. ¿En qué se diferencia Playwright de Selenium?

Esta es una de las preguntas clásicas. Hay varias diferencias relevantes:

| | Playwright | Selenium |
|---|---|---|
| **Protocolo** | CDP / WebSocket nativo | WebDriver (HTTP) |
| **Auto-waiting** | Incorporado | Manual (requiere explicit waits) |
| **Velocidad** | Más rápido | Más lento por la capa HTTP |
| **Navegadores** | Binarios propios controlados | Drivers externos (geckodriver, chromedriver…) |
| **Test runner** | Propio (`@playwright/test`) | Externo (JUnit, TestNG, pytest…) |
| **Contextos aislados** | `BrowserContext` nativo | Más complejo de implementar |
| **Madurez** | Más reciente (2020) | Más antiguo, más extendido en empresa |

La respuesta honesta es que **Playwright es más moderno y más potente para aplicaciones web actuales**, pero Selenium sigue siendo más prevalente en entornos enterprise con años de inversión en infraestructura. En una entrevista, no desprecies Selenium: muestra que conoces ambos y sabes cuándo usar cada uno.

---

### 6. ¿Cómo se instala Playwright?

```bash
npm init playwright@latest
```

Este comando crea un proyecto nuevo con Playwright configurado: instala las dependencias, descarga los binarios de los navegadores, genera un fichero `playwright.config.ts` y crea tests de ejemplo. Es el punto de partida recomendado.

Si quieres añadir Playwright a un proyecto existente:

```bash
npm install --save-dev @playwright/test
npx playwright install
```

---

### 7. ¿Qué es un BrowserContext?

Un **`BrowserContext`** es un entorno de navegación completamente aislado dentro de un mismo proceso de navegador. Es el equivalente a abrir una **ventana de incógnito**: tiene sus propias cookies, su propio `localStorage`, su propia caché y su propio historial, completamente separados de otros contextos.

En Playwright Test, **cada test tiene su propio `BrowserContext` por defecto**, lo que garantiza el aislamiento entre tests sin necesidad de lanzar un navegador nuevo para cada uno. Esto es mucho más eficiente.

Un uso típico avanzado es crear contextos con estados de autenticación precargados:

```typescript
// guardamos el estado de autenticación una sola vez
await page.context().storageState({ path: 'auth.json' });

// y lo reutilizamos en todos los tests que lo necesiten
const context = await browser.newContext({ storageState: 'auth.json' });
```

---

### 8. ¿Cómo se lanza un navegador en Playwright?

Usando la API de bajo nivel directamente:

```typescript
import { chromium } from '@playwright/test';

// lanzamos el navegador manualmente
const browser = await chromium.launch({ headless: true });
const context = await browser.newContext();
const page = await context.newPage();

await page.goto('https://example.com');

// siempre hay que cerrar el navegador al terminar
await browser.close();
```

En la práctica, cuando usas `@playwright/test` **nunca necesitas hacer esto manualmente**: el test runner gestiona el ciclo de vida del navegador, el contexto y la página a través de las fixtures `browser`, `context` y `page`. El código anterior es útil para scripts puntuales, pero no para una suite de tests organizada.

---

### 9. ¿Qué es el Playwright Test Runner?

**`@playwright/test`** es el test runner oficial de Playwright. A diferencia de Selenium, que necesita integrarse con herramientas externas (JUnit, pytest, Jest…), Playwright incluye todo de serie:

- Ejecución en paralelo con workers.
- Sistema de **fixtures** para compartir estado entre tests.
- **Retries** automáticos en tests fallidos.
- **Reporters** variados: HTML, JSON, JUnit, línea de comandos.
- **Sharding** para distribuir la ejecución entre máquinas.
- **Trace Viewer** integrado para depuración.

Toda la configuración vive en `playwright.config.ts`.

---

### 10. ¿Cómo se localizan elementos en Playwright?

Playwright ofrece varios mecanismos de localización. Los recomendados, de más a menos preferidos:

- **`getByRole`**: localiza por rol ARIA. Es el más robusto y el que mejor refleja cómo los usuarios interactúan con la interfaz.
- **`getByLabel`**: localiza campos de formulario por su etiqueta.
- **`getByPlaceholder`**: localiza inputs por su placeholder.
- **`getByText`**: localiza por contenido de texto.
- **`getByTestId`**: localiza por el atributo `data-testid`. Requiere instrumentar el código.
- **Selectores CSS**: `page.locator('button.submit')`. Funcionan, pero son más frágiles ante cambios de estilos.
- **XPath**: disponible, pero no recomendado salvo casos muy concretos.

La recomendación de la documentación oficial es **priorizar los locators semánticos** (`getByRole`, `getByLabel`) porque reflejan la accesibilidad real de la interfaz y son más resistentes a cambios de implementación.

---

### 11. ¿Qué son los locators?

Los **locators** son el mecanismo central de Playwright para encontrar e interactuar con elementos del DOM. Se crean con `page.locator()` o con los métodos `getBy*`, pero no ejecutan ninguna búsqueda en el momento de crearse: son **lazy**, es decir, buscan el elemento en el momento en que se realiza la acción.

Esto tiene una ventaja importante: si el elemento no existe todavía cuando creas el locator pero aparece un momento después, Playwright lo encontrará igualmente gracias al auto-waiting.

```typescript
// esto no busca el elemento todavía
const submitButton = page.getByRole('button', { name: 'Enviar' });

// aquí es cuando Playwright busca y espera a que el elemento esté listo
await submitButton.click();
```

A diferencia de los selectores de Selenium (que devuelven el elemento en el momento de la búsqueda y pueden quedar obsoletos), los locators de Playwright son siempre frescos.

---

### 12. ¿Cómo se manejan los iframes en Playwright?

Con **`frameLocator`**, que crea un locator que apunta al interior del iframe:

```typescript
// apuntamos al iframe por su selector
const iframeContent = page.frameLocator('#payment-iframe');

// a partir de aquí, interactuamos como si fuera la página principal
await iframeContent.getByLabel('Card number').fill('4111111111111111');
await iframeContent.getByRole('button', { name: 'Pay' }).click();
```

Los iframes son habituales en pasarelas de pago, widgets de terceros (chat, mapas, anuncios) y editores embebidos. Playwright los trata como una capa de localización más, lo que simplifica mucho el código respecto a cómo se manejaban en Selenium.

---

### 13. ¿Cómo se hacen screenshots en Playwright?

```typescript
// screenshot de la página completa
await page.screenshot({ path: 'screenshot.png', fullPage: true });

// screenshot de un elemento concreto
await page.locator('#dashboard-chart').screenshot({ path: 'chart.png' });
```

Los screenshots son útiles tanto para depuración como para **tests de regresión visual**. Playwright tiene soporte nativo para comparar screenshots con una imagen de referencia:

```typescript
// compara el aspecto del componente con la imagen de referencia guardada
await expect(page.locator('.hero-section')).toMatchSnapshot('hero.png');
```

Si la imagen ha cambiado más del umbral permitido, el test falla. Ideal para detectar regresiones visuales involuntarias.

---

### 14. ¿Cómo se manejan las subidas de ficheros?

```typescript
// subida de un único fichero
await page.getByLabel('Adjuntar documento').setInputFiles('contrato.pdf');

// subida de múltiples ficheros
await page.getByLabel('Adjuntar documentos').setInputFiles([
  'contrato.pdf',
  'anexo.pdf',
]);

// limpiar la selección
await page.getByLabel('Adjuntar documento').setInputFiles([]);
```

`setInputFiles` funciona directamente sobre el input de tipo `file`, sin necesidad de simular el diálogo del sistema operativo. Si la subida se activa desde un botón que abre el explorador de archivos del OS, hay que usar `page.waitForFileChooser()` en combinación con el clic.

---

### 15. ¿Qué es el modo headless?

El **modo headless** significa que el navegador se ejecuta **sin interfaz gráfica**: no abre ninguna ventana visible. Todo ocurre en memoria.

Las ventajas son claras: es más rápido, consume menos recursos y funciona en servidores sin entorno gráfico (como los runners de CI). Por eso es el modo por defecto en Playwright.

El **modo headed** (`headless: false`) abre el navegador con ventana visible y es útil cuando estás desarrollando o depurando tests.

Un punto que vale la pena mencionar: como vimos en la entrada anterior (la de extensiones de Firefox), **Firefox no puede cargar extensiones en modo headless**. Esta es una de las pocas limitaciones del modo sin interfaz gráfica.

---

### 16. ¿Cómo se ejecutan los tests en paralelo?

Playwright Test ejecuta los tests en paralelo **por defecto**, usando workers. Cada worker es un proceso independiente con su propio navegador y contexto.

La configuración se hace en `playwright.config.ts`:

```typescript
import { defineConfig } from '@playwright/test';

export default defineConfig({
  workers: 4, // número de workers en paralelo (por defecto: la mitad de las CPUs)
  fullyParallel: true, // todos los tests dentro de un fichero también corren en paralelo
});
```

Para proyectos grandes, también existe el **sharding**: dividir la suite entre varias máquinas de CI:

```bash
# máquina 1: ejecuta el primer tercio de los tests
npx playwright test --shard=1/3

# máquina 2: ejecuta el segundo tercio
npx playwright test --shard=2/3

# máquina 3: ejecuta el tercer tercio
npx playwright test --shard=3/3
```

---

### 17. ¿Cómo se hacen tests de API con Playwright?

A través de **`APIRequestContext`**, disponible como fixture `request` en los tests:

```typescript
import { test, expect } from '@playwright/test';

test('the API returns the list of users', async ({ request }) => {
  // hacemos una petición GET
  const response = await request.get('/api/users');

  expect(response.status()).toBe(200);

  const body = await response.json();
  expect(body).toHaveLength(10);
});

test('creates a new user', async ({ request }) => {
  // hacemos una petición POST con cuerpo JSON
  const response = await request.post('/api/users', {
    data: { name: 'Ana García', email: 'ana@example.com' },
  });

  expect(response.status()).toBe(201);
});
```

Lo interesante de hacer API testing con Playwright es que puedes **combinar llamadas de API con tests de UI** en el mismo test: por ejemplo, crear un usuario vía API y luego verificar que aparece en la interfaz, sin pasar por el formulario.

---

### 18. ¿Qué es la intercepción de red?

La **intercepción de red** permite monitorizar, modificar o bloquear las peticiones HTTP que hace la página durante el test. Se hace con `page.route()`:

```typescript
// dejamos pasar la petición sin cambios
await page.route('**/api/**', route => route.continue());

// devolvemos una respuesta mockeada
await page.route('**/api/users', route => {
  route.fulfill({
    status: 200,
    contentType: 'application/json',
    body: JSON.stringify([{ id: 1, name: 'Ana' }]),
  });
});

// bloqueamos la petición (simula error de red / modo offline)
await page.route('**/api/weather', route => route.abort('failed'));
```

Es una de las funcionalidades más potentes de Playwright para tests E2E: permite aislar el frontend de servicios externos, simular respuestas de error, probar estados de carga o comportamiento offline, todo sin necesidad de un servidor de mocks separado.

---

### 19. ¿Cómo se depuran los tests en Playwright?

Playwright ofrece varias herramientas de depuración, de menos a más potentes:

- **Modo headed** (`--headed`): ver el navegador en acción es el primer paso para entender qué está pasando.
- **`page.pause()`**: detiene la ejecución y abre el **Playwright Inspector**, una herramienta visual donde puedes ejecutar el test paso a paso, inspeccionar locators y ver el estado del DOM.
- **`PWDEBUG=1`**: variable de entorno que activa el Inspector automáticamente al inicio del test.
- **Trace Viewer**: la herramienta más completa. Graba toda la ejecución (acciones, capturas de pantalla, peticiones de red, consola) y te permite reproducirla después de un fallo en CI:

```bash
npx playwright show-trace trace.zip
```

En mi experiencia, el **Trace Viewer** es la herramienta que más tiempo ahorra cuando tienes un test que falla en CI pero no consigues reproducirlo en local. Es el equivalente a tener una grabación completa de lo que pasó.

---

### 20. ¿Qué son las fixtures en Playwright?

Las **fixtures** son el mecanismo de Playwright para encapsular y compartir el _setup_ y _teardown_ entre tests. Son funciones que preparan un estado (abrir una página, autenticar un usuario, conectar a una base de datos…) y lo ponen a disposición del test a través de la inyección de dependencias.

```typescript
import { test as base } from '@playwright/test';
import { LoginPage } from './pages/login.page';

// extendemos el test base con nuestra fixture personalizada
const test = base.extend<{ loginPage: LoginPage }>({
  loginPage: async ({ page }, use) => {
    const loginPage = new LoginPage(page);
    await loginPage.navigate(); // setup: navegamos a la página de login
    await use(loginPage);       // ejecutamos el test
    // teardown: lo que pongamos aquí se ejecuta al terminar el test
  },
});

test('the user can log in', async ({ loginPage }) => {
  await loginPage.login('usuario@example.com', 'contraseña');
  // ...
});
```

Hemos dedicado tres entradas completas a las fixtures en el blog (entradas 088, 089 y 090), que cubren desde los fundamentos hasta patrones avanzados de tipado y composición. Si quieres profundizar, son una lectura obligatoria.

---

### Conclusión.

  * Playwright es un framework de automatización moderno, desarrollado por Microsoft, que soporta Chromium, Firefox y WebKit con una única API.
  * El **auto-waiting** y los **locators** son dos de sus pilares fundamentales: eliminan la fragilidad (_flakiness_) que caracterizaba a los tests de Selenium.
  * El **`BrowserContext`** garantiza el aislamiento entre tests sin necesidad de lanzar un navegador nuevo para cada uno.
  * La **intercepción de red** (`page.route()`) y las **fixtures** son las herramientas más potentes para construir una suite de tests robusta y mantenible.
  * El **Trace Viewer** es el recurso de depuración más valioso, especialmente para fallos en CI.
  * Conocer los conceptos no basta: practica explicarlos en voz alta antes de una entrevista. La diferencia entre quien usa una herramienta y quien la entiende se nota en cómo la explica.

* * *

Y hasta aquí nuestro repaso de las 20 preguntas más habituales sobre Playwright en entrevistas técnicas. Ahora que las tienes frescas, ¿te animarías a responderlas todas de memoria sin mirar? Es un buen ejercicio para saber dónde tienes los huecos.

¡Nos leemos en la siguiente entrada!
