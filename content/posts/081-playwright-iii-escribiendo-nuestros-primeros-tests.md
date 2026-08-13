---
title: '081 – Playwright (III): Escribiendo nuestros primeros tests.'
date: '2026-04-13T07:00:00+00:00'
url: /2026/04/13/081-playwright-iii-escribiendo-nuestros-primeros-tests/
image: /img/blog-images/old-post/2026/04/foto64.png
categories:
- automation
- best-practices
- code-quality
- playwright
- qa
tags:
- estructura
- locators
- selectors
- testing
author: estefafdez
---
¡Hola a todos!

Ya sabemos instalar Playwright y ejecutar los tests de ejemplo de nuestro repo base. Ahora toca la parte más importante: aprender a escribir nuestros propios tests. En esta entrada veremos la estructura de un test, las acciones más importantes, cómo hacer aserciones y cómo organizar los tests con hooks. ¡Empezamos!

### Estructura de un test.

Los tests de Playwright son sencillos en su estructura: realizan acciones sobre la página y comprueban el estado de la misma contra unas expectativas. Veamos el test de ejemplo que genera Playwright al instalarse:

```
import { test, expect } from '@playwright/test';

test('has title', async ({ page }) => {
  await page.goto('https://playwright.dev/');
  // Comprobamos que el título contiene la cadena "Playwright"
  await expect(page).toHaveTitle(/Playwright/);
});

test('get started link', async ({ page }) => {
  await page.goto('https://playwright.dev/');
  // Hacemos click en el enlace "Get started"
  await page.getByRole('link', { name: 'Get started' }).click();
  // Comprobamos que el heading "Installation" es visible
  await expect(page.getByRole('heading', { name: 'Installation' })).toBeVisible();
});

```

Como vemos, la estructura básica de un test es:

1. **Importamos** `test` y `expect` de `@playwright/test`.
1. Definimos el test con `test('nombre del test', async ({ page }) => { ... })`.
1. Dentro del test, usamos `page` para navegar, interactuar con elementos y hacer aserciones.

Una de las grandes ventajas de Playwright es que **espera automáticamente** a que los elementos sean accionables antes de interactuar con ellos. No necesitamos añadir `sleep()` ni esperas manuales.

### Navegación.

La mayoría de los tests comienzan navegando a una URL. Para ello usamos `page.goto()`:

```
await page.goto('https://playwright.dev/');

```

Playwright espera a que la página llegue al estado `load` antes de continuar con el siguiente paso.

### Locators y acciones básicas.

Para interactuar con los elementos de la página, Playwright usa la **API de Locators**. Un locator representa una forma de encontrar un elemento (o varios) en la página en cualquier momento. Playwright recomienda usar **locators semánticos** siempre que sea posible, ya que son más _robustos_ y _resistentes_ a cambios en el DOM.

> **Nota**: aquí yo no estoy muy de acuerdo, preferiría ser yo la persona que pusiera IDs únicos en el DOM y los usara y así no depender de un atributo o texto que puede cambiar, pero siendo _mijitas_, nos vamos a quedar con la teoría oficial que nos dicen nuestros amigos de Microsoft.

Los locators más utilizados son:

- **`page.getByRole()`**: localiza elementos por su rol ARIA (link, button, heading, textbox...). Es el más recomendado.
- **`page.getByText()`**: localiza elementos por su contenido de texto.
- **`page.getByLabel()`**: localiza campos de formulario por su etiqueta.
- **`page.getByPlaceholder()`**: localiza inputs por su placeholder.
- **`page.getByTestId()`**: localiza elementos por su atributo `data-testid`.

Una vez tenemos el locator, podemos encadenar las acciones más comunes:

- **`.click()`**: hace click en el elemento.
- **`.fill('texto')`**: rellena un campo de texto.
- **`.press('Enter')`**: simula la pulsación de una tecla.
- **`.check()` / `.uncheck()`**: marca o desmarca un checkbox.
- **`.selectOption('valor')`**: selecciona una opción de un `<select>`.
- **`.hover()`**: pasa el ratón por encima del elemento.

```
// Localizar y hacer click
await page.getByRole('link', { name: 'Get started' }).click();

// Rellenar un input
await page.getByLabel('Email').fill('usuario@example.com');

// Pulsar una tecla
await page.getByRole('textbox').press('Enter');

```

### Aserciones.

Las aserciones en Playwright se hacen con la función **`expect()`**. Lo que hace especiales las aserciones de Playwright es que son **asíncronas**: en lugar de comprobar el estado en el momento exacto en que se llaman, esperan a que la condición se cumpla dentro de un timeout configurable. Esto elimina los problemas de flakiness por condiciones de carrera.

Las aserciones más utilizadas son:

- **`await expect(page).toHaveTitle(/Playwright/)`**: comprueba el título de la página.
- **`await expect(page).toHaveURL('https://...')`**: comprueba la URL actual.
- **`await expect(locator).toBeVisible()`**: comprueba que el elemento es visible.
- **`await expect(locator).toHaveText('texto')`**: comprueba el texto del elemento.
- **`await expect(locator).toBeEnabled()`**: comprueba que el elemento está habilitado.
- **`await expect(locator).toBeChecked()`**: comprueba que un checkbox está marcado.
- **`await expect(locator).toHaveValue('valor')`**: comprueba el valor de un input.

Además de las aserciones asíncronas, Playwright también incluye **aserciones síncronas** genéricas como `toEqual`, `toContain` o `toBeTruthy`, que se usan para comprobar valores ya disponibles sin necesidad de espera:

```
expect(success).toBeTruthy();
expect(items).toContain('elemento');

```

### Aislamiento de tests.

En Playwright, cada test se ejecuta en un **BrowserContext** independiente, equivalente a un **perfil de navegador completamente nuevo.** Esto garantiza que los tests no comparten estado entre sí (cookies, localStorage, sesiones...), aunque se ejecuten en el mismo proceso del navegador.

```
test('primer test', async ({ page }) => {
  // "page" pertenece a un BrowserContext aislado, creado para este test.
});

test('segundo test', async ({ page }) => {
  // "page" en este test está completamente aislada del primero.
});

```

Esto es una de las grandes ventajas de Playwright frente a otros frameworks: el aislamiento es automático y no requiere configuración adicional.

### Organización con hooks.

Para organizar nuestros tests y evitar repetir código, Playwright nos ofrece los siguientes **hooks**:

- **`test.describe()`**: agrupa tests relacionados bajo un nombre común.
- **`test.beforeEach()`**: se ejecuta antes de cada test del grupo.
- **`test.afterEach()`**: se ejecuta después de cada test del grupo.
- **`test.beforeAll()`**: se ejecuta una vez antes de todos los tests del grupo (a nivel de worker).
- **`test.afterAll()`**: se ejecuta una vez después de todos los tests del grupo.

```
import { test, expect } from '@playwright/test';

test.describe('Navegación principal', () => {
  test.beforeEach(async ({ page }) => {
    // Navegamos a la URL inicial antes de cada test
    await page.goto('https://playwright.dev/');
  });

  test('el título es correcto', async ({ page }) => {
    await expect(page).toHaveTitle(/Playwright/);
  });

  test('la URL es correcta', async ({ page }) => {
    await expect(page).toHaveURL('https://playwright.dev/');
  });
});

```

Usar `test.describe` y `beforeEach` nos permite mantener los tests organizados, legibles y con menos código duplicado.

* * *

Y hasta aquí nuestra entrada sobre cómo escribir tests con Playwright. En la siguiente entrada veremos cómo depurar los tests cuando algo falla y cómo usar el **Trace Viewer** para analizar los resultados. ¡Nos leemos en la siguiente entrada!
