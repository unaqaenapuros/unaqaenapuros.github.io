---
title: '090 – Playwright: Fixtures III – Tipado, composición y mergeTests.'
date: '2026-08-10T07:06:00+00:00'
url: /2026/08/10/090-playwright-fixtures-iii-tipado-composicion-y-mergetests/
image: /img/blog-images/wp-posts/2026/05/foto79.png
categories:
- automation
- best-practices
- playwright
- qa
tags:
- fixtures
- testing
author: estefafdez
---
¡Hola a todos!

Llegamos a la tercera y última entrega de nuestra mini-serie sobre fixtures en Playwright. En las dos entradas anteriores vimos los fundamentos de las fixtures, las de **Page Objects**, las de **API**, las de **worker scope** y las de **datos opcionales**. Ahora vamos a ver cómo llevar todo esto al siguiente nivel: **tipado con TypeScript**, **composición de fixtures** en una arquitectura escalable y la función **`mergeTests`** para mantener el código ordenado en proyectos grandes. ¡Empezamos!

### 5\. Tipando las fixtures con TypeScript.

Una de las grandes ventajas de trabajar con Playwright en TypeScript es que podemos definir **tipos explícitos** para todas nuestras fixtures. Esto nos da autocompletado en el editor, comprobación de tipos en tiempo de compilación y, en cierta forma, sirve como documentación viva de lo que cada fixture proporciona.

#### Definiendo interfaces para los distintos tipos de fixtures.

La estrategia recomendada es separar los tipos en interfaces distintas según su responsabilidad. Esto nos permite mantener el código organizado y facilita la composición posterior:

```
// types.ts
import { LoginPage, ProductPage, CheckoutPage } from './pages';
import { UserAPI, ProductAPI, OrderAPI } from './api';
import { DatabaseHelper } from './helpers/database.helper';
import { User, Product, Order } from './models';

// Fixtures de Page Objects
export interface PageFixtures {
  loginPage: LoginPage;
  productPage: ProductPage;
  checkoutPage: CheckoutPage;
}

// Fixtures de clases de API
export interface APIFixtures {
  userAPI: UserAPI;
  productAPI: ProductAPI;
  orderAPI: OrderAPI;
}

// Fixtures de helpers (ámbito worker)
export interface HelperFixtures {
  dbHelper: DatabaseHelper;
}

// Fixtures de datos opcionales
export interface DataFixtures {
  testUser?: User;
  testProduct?: Product;
  testOrder?: Order;
}

// Combinamos todos los tipos de fixtures de test
export interface TestFixtures extends PageFixtures, APIFixtures, DataFixtures {}

// Fixtures de worker
export interface WorkerFixtures extends HelperFixtures {}

```

#### Usando los tipos en base.extend().

Ahora usamos estos tipos en el `base.extend()`. El primer parámetro de tipo son las **fixtures de test** y el segundo son las **fixtures de worker**:

```
// basetest.ts
import { test as base } from '@playwright/test';
import { TestFixtures, WorkerFixtures } from './types';

export const test = base.extend<TestFixtures, WorkerFixtures>({
  // Aquí implementamos cada fixture
});

```

#### Beneficios del tipado.

Una vez tenemos todo tipado correctamente, el editor nos da:

- **Autocompletado** al escribir los argumentos del test: al abrir el destructuring, el editor sugiere todas las fixtures disponibles.
- **Comprobación de tipos**: si intentamos usar una propiedad que no existe en la fixture, TypeScript nos avisa en tiempo de compilación.
- **Refactoring seguro**: si renombramos una clase o una propiedad, TypeScript nos señala todos los lugares donde hay que actualizar el código.
- **Documentación implícita**: los tipos sirven como referencia de qué fixtures están disponibles y qué contienen.

### 6\. Combinando todos los tipos de fixtures.

Ahora que tenemos los tipos definidos, vamos a ver cómo combinar todos los tipos de fixtures en un único fichero que sirva como la base de todos nuestros tests:

```
// fixtures.ts
import { test as base } from '@playwright/test';
import { LoginPage, DashboardPage } from './pages';
import { UserAPI, ProductAPI } from './api';
import { DatabaseHelper } from './helpers/database.helper';
import { User, Product } from './types';

type TestFixtures = {
  loginPage: LoginPage;
  dashboardPage: DashboardPage;
  userAPI: UserAPI;
  productAPI: ProductAPI;
  testUser?: User;
  testProduct?: Product;
};

type WorkerFixtures = {
  dbHelper: DatabaseHelper;
};

export const test = base.extend<TestFixtures, WorkerFixtures>({
  // Fixtures de Page Objects
  loginPage: async ({ page }, use) => {
    await use(new LoginPage(page));
  },
  dashboardPage: async ({ page }, use) => {
    await use(new DashboardPage(page));
  },

  // Fixtures de API
  userAPI: async ({ request }, use) => {
    await use(new UserAPI(request));
  },
  productAPI: async ({ request }, use) => {
    await use(new ProductAPI(request));
  },

  // Fixtures de datos opcionales
  testUser: [async ({}, use) => {
    await use({ id: '1', username: 'testuser', email: 'test@example.com', role: 'user' });
  }, { option: true }],

  testProduct: [async ({}, use) => {
    await use({ id: '1', name: 'Producto de prueba', price: 9.99, stock: 10 });
  }, { option: true }],

  // Fixture de worker: base de datos
  dbHelper: [async ({}, use) => {
    const helper = new DatabaseHelper();
    await helper.connect();
    await helper.resetDatabase(); // Limpiamos la base de datos antes de cada worker
    await use(helper);
    await helper.disconnect();
  }, { scope: 'worker' }],
});

```

#### Un test completo usando todas las fixtures.

Con todo esto en su sitio, podemos escribir tests de extremo a extremo muy expresivos que combinan interacciones de UI, llamadas a API y verificaciones en base de datos, todo con tipado completo:

```
// e2e.spec.ts
import { test } from './fixtures';
import { expect } from '@playwright/test';

test('el usuario puede comprar un producto', async ({
  loginPage,
  dashboardPage,
  userAPI,
  productAPI,
  testUser,
  testProduct,
  dbHelper,
}) => {
  // Creamos el usuario via API
  const user = await userAPI.createUser(testUser);

  // Hacemos login en la UI
  await loginPage.login(user.username, 'contraseña123');

  // Añadimos el producto al carrito y completamos la compra
  await dashboardPage.addToCart(testProduct.id);
  await dashboardPage.completePurchase();

  // Verificamos el pedido en la base de datos
  const dbOrder = await dbHelper.getLatestOrderForUser(user.id);
  expect(dbOrder.productId).toBe(testProduct.id);

  // Verificamos que el stock del producto se ha actualizado
  const updatedProduct = await productAPI.getProduct(testProduct.id);
  expect(updatedProduct.stock).toBe(testProduct.stock - 1);
});

```

Este test es completamente legible y cada línea tiene un propósito claro. Toda la complejidad de preparar los objetos está encapsulada en las fixtures.

### 7\. mergeTests: organizando fixtures en módulos.

En proyectos grandes, tener todas las fixtures en un único fichero `fixtures.ts` puede volverse difícil de mantener. Para esto, Playwright nos ofrece la función `mergeTests`, que nos permite definir las fixtures en módulos separados y combinarlos después.

#### Separando las fixtures en módulos.

Creamos un fichero por cada grupo de fixtures:

```
// fixtures/page-fixtures.ts
import { test as base } from '@playwright/test';
import { LoginPage, DashboardPage } from '../pages';

export const pageTest = base.extend<{
  loginPage: LoginPage;
  dashboardPage: DashboardPage;
}>({
  loginPage: async ({ page }, use) => {
    await use(new LoginPage(page));
  },
  dashboardPage: async ({ page }, use) => {
    await use(new DashboardPage(page));
  },
});

```

```
// fixtures/worker-fixtures.ts
import { test as base } from '@playwright/test';
import { DatabaseHelper } from '../helpers/database.helper';

export const workerTest = base.extend<
  {},
  { dbHelper: DatabaseHelper }
>({
  dbHelper: [async ({}, use) => {
    const helper = new DatabaseHelper();
    await helper.connect();
    await use(helper);
    await helper.disconnect();
  }, { scope: 'worker' }],
});

```

#### Combinando los módulos con mergeTests.

Una vez tenemos los módulos separados, los combinamos con `mergeTests` en el punto de entrada principal:

```
// fixtures/index.ts
import { mergeTests } from '@playwright/test';
import { pageTest } from './page-fixtures';
import { workerTest } from './worker-fixtures';

// Exportamos un único objeto test que combina todos los módulos
export const test = mergeTests(pageTest, workerTest);

```

A partir de aquí, los tests importan solo de `fixtures/index.ts` y tienen acceso a todas las fixtures, independientemente de en qué módulo estén definidas:

```
// checkout.spec.ts
import { test } from './fixtures';
import { expect } from '@playwright/test';

test('el proceso de pago funciona correctamente', async ({
  loginPage,      // viene de page-fixtures.ts
  dashboardPage,  // viene de page-fixtures.ts
  dbHelper,       // viene de worker-fixtures.ts
}) => {
  // ...
});

```

### Buenas prácticas generales.

Antes de cerrar, un resumen de las buenas prácticas más importantes al trabajar con fixtures en proyectos reales:

1. **Modulariza**: separa las fixtures por responsabilidad (páginas, APIs, datos, helpers). No lo pongas todo en un único fichero.
1. **Usa el scope correcto**: ámbito de test para la mayoría de los casos, ámbito de worker solo para operaciones genuinamente costosas.
1. **Tipa todo con TypeScript**: el esfuerzo inicial merece la pena por el autocompletado, la seguridad de tipos y la documentación implícita.
1. **Principio de responsabilidad única**: cada fixture debe tener un único propósito. Si hace demasiadas cosas, divídela.
1. **Usa composición**: `mergeTests` es tu aliado en proyectos grandes para mantener el código organizado sin sacrificar la usabilidad.
1. **No olvides la limpieza**: siempre implementa la fase de teardown (código tras `await use(...)`) para evitar fugas de recursos.
1. **Variables de entorno para credenciales**: nunca hardcodees strings de conexión, contraseñas o tokens en el código de las fixtures.

### Conclusión.

- Tipar las fixtures con **interfaces de TypeScript** ( `TestFixtures`, `WorkerFixtures`) nos da autocompletado, seguridad de tipos y una mejor experiencia de desarrollo.
- Combinar todos los tipos de fixtures en un único `base.extend()` nos permite escribir tests de extremo a extremo muy expresivos.
- **`mergeTests`** nos permite dividir las fixtures en módulos independientes y combinarlos, facilitando el mantenimiento en proyectos grandes.
- Una buena arquitectura de fixtures es la base de una suite de tests robusta, mantenible y escalable.

* * *

Y hasta aquí nuestra mini-serie sobre fixtures en Playwright. Hemos cubierto desde la introducción básica hasta los patrones más avanzados de tipado y composición. ¡Nos leemos en la siguiente entrada!
