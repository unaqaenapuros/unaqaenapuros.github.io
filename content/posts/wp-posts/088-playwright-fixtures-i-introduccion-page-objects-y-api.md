---
title: '088 – Playwright: Fixtures I – Introducción, Page Objects y API.'
date: '2026-07-13T07:02:00+00:00'
url: /2026/07/13/088-playwright-fixtures-i-introduccion-page-objects-y-api/
image: /img/blog-images/wp-posts/2026/05/foto77.png
categories:
- automation
- best-practices
- ai
- playwright
- qa
tags:
- fixtures
- testing
author: estefafdez
---
¡Hola a todos!

Seguimos con Playwright. Hoy empezamos una mini-serie dentro de la serie: vamos a hablar de las **fixtures**. Es uno de los temas más importantes de Playwright y, al mismo tiempo, uno de los que más dudas genera cuando empiezas a usarlo en proyectos reales. Lo vamos a ver en tres entregas, y en esta primera cubriremos qué son las fixtures, para qué sirven, y cómo crear las dos más habituales: las de **Page Objects** y las de **clases de API**. ¡Empezamos!

### ¿Qué son las fixtures en Playwright?

Las **fixtures** son una funcionalidad de Playwright que nos permite compartir objetos o datos entre tests, preparar precondiciones y gestionar los recursos de los tests de forma eficiente. En resumen, son la herramienta que Playwright nos da para organizar y reutilizar el código de preparación de los tests.

Sin fixtures, cada test tiene que encargarse de crear y configurar todos los objetos que necesita. Esto lleva rápidamente a mucho código duplicado y tests difíciles de mantener. Con fixtures, definimos esos objetos una sola vez y Playwright se encarga de inyectarlos en cada test que los necesite.

Las fixtures nos ayudan a:

- **Compartir objetos** entre tests (Page Objects, clientes de API, helpers...).
- **Configurar precondiciones** de forma centralizada.
- **Gestionar el ciclo de vida** de los recursos: se crean antes del test y se destruyen después.
- **Reducir la duplicación** de código.
- **Mejorar la organización** y legibilidad de los tests.

Playwright ya incluye fixtures predefinidas como `page`, `browser`, `context` o `request`. Lo que vamos a ver en esta serie es cómo crear las nuestras propias extendiendo las que ya existen.

### ¿Cómo funciona una fixture?

La base de todo es `base.extend()`. Con este método extendemos el objeto `test` de Playwright para añadir nuestras propias fixtures. El patrón es siempre el mismo:

```
import { test as base } from '@playwright/test';

export const test = base.extend<{
  miFixture: TipoDeFixture;
}>({
  miFixture: async ({ page }, use) => {
    // 1. Preparación: creamos el objeto
    const objeto = new MiClase(page);

    // 2. Uso: lo inyectamos en el test
    await use(objeto);

    // 3. Limpieza (opcional): lo destruimos después del test
  },
});

```

La clave está en la función `use`: todo lo que va antes es la **preparación** (equivalente al `beforeEach`), y todo lo que va después de `await use(...)` es la **limpieza** (equivalente al `afterEach`). Playwright gestiona esto automáticamente.

### 1\. Fixtures de Page Objects.

El patrón **Page Object Model (POM)** es uno de los más usados en automatización: creamos clases que encapsulan las interacciones con cada página de nuestra aplicación. Las fixtures son la forma perfecta de hacer que esas clases estén disponibles en todos nuestros tests sin tener que instanciarlas manualmente en cada uno.

#### Creando los Page Objects.

Primero definimos nuestras clases de Page Object:

```
// pages/login.page.ts
import { Page } from '@playwright/test';

export class LoginPage {
  constructor(private page: Page) {}

  async login(username: string, password: string) {
    await this.page.fill('#username', username);
    await this.page.fill('#password', password);
    await this.page.click('#login-button');
  }
}

```

```
// pages/dashboard.page.ts
import { Page } from '@playwright/test';

export class DashboardPage {
  constructor(private page: Page) {}

  async getUserName() {
    return this.page.textContent('.user-name');
  }
}

```

#### Creando las fixtures.

Ahora creamos un fichero `fixtures.ts` donde extendemos `test` para incluir nuestros Page Objects como fixtures:

```
// fixtures.ts
import { test as base } from '@playwright/test';
import { LoginPage } from './pages/login.page';
import { DashboardPage } from './pages/dashboard.page';

export const test = base.extend<{
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

#### Usando las fixtures en los tests.

A partir de aquí, en nuestros tests importamos el `test` de nuestro fichero de fixtures en lugar del de `@playwright/test`. Los Page Objects estarán disponibles directamente como argumentos del test:

```
// login.spec.ts
import { test } from './fixtures';
import { expect } from '@playwright/test';

test('el usuario puede hacer login', async ({ loginPage, dashboardPage }) => {
  await loginPage.login('usuario', 'contraseña123');
  const userName = await dashboardPage.getUserName();
  expect(userName).toBe('usuario');
});

```

Fíjate en la diferencia: ya no necesitamos crear `new LoginPage(page)` ni `new DashboardPage(page)` en el test. Playwright nos los inyecta automáticamente, y si necesitamos la fixture `page` directamente también la podemos pedir.

### 2\. Fixtures de clases de API.

Además de interactuar con la interfaz de usuario, muchos tests necesitan comunicarse directamente con el backend: crear datos de prueba, verificar el estado de la base de datos, limpiar datos después del test... Para esto usamos **clases de API** combinadas con fixtures.

La fixture predefinida `request` de Playwright nos da un contexto HTTP para hacer llamadas a la API. La usamos para instanciar nuestras clases de API:

#### Creando las clases de API.

```
// api/user.api.ts
import { APIRequestContext } from '@playwright/test';

export class UserAPI {
  constructor(private request: APIRequestContext) {}

  async createUser(userData: any) {
    return this.request.post('/api/users', { data: userData });
  }

  async deleteUser(userId: string) {
    return this.request.delete(`/api/users/${userId}`);
  }
}

```

```
// api/product.api.ts
import { APIRequestContext } from '@playwright/test';

export class ProductAPI {
  constructor(private request: APIRequestContext) {}

  async getProducts() {
    return this.request.get('/api/products');
  }

  async getProduct(id: string) {
    return this.request.get(`/api/products/${id}`);
  }
}

```

#### Añadiendo las fixtures de API.

Añadimos las nuevas fixtures al fichero `fixtures.ts`. Observa que aquí usamos `request` en lugar de `page`:

```
// fixtures.ts
import { test as base } from '@playwright/test';
import { UserAPI } from './api/user.api';
import { ProductAPI } from './api/product.api';

export const test = base.extend<{
  userAPI: UserAPI;
  productAPI: ProductAPI;
}>({
  userAPI: async ({ request }, use) => {
    await use(new UserAPI(request));
  },
  productAPI: async ({ request }, use) => {
    await use(new ProductAPI(request));
  },
});

```

#### Usando las fixtures de API en los tests.

```
// products.spec.ts
import { test } from './fixtures';
import { expect } from '@playwright/test';

test('la lista de productos no está vacía', async ({ page, productAPI }) => {
  // Comprobamos primero via API que hay productos
  const response = await productAPI.getProducts();
  const products = await response.json();
  expect(products.length).toBeGreaterThan(0);

  // Luego verificamos que se muestran en la UI
  await page.goto('/products');
  await expect(page.locator('.product-item')).not.toHaveCount(0);
});

```

Combinar fixtures de UI con fixtures de API en el mismo test es una de las mayores ventajas de este patrón: podemos verificar tanto lo que ve el usuario como el estado real del backend.

### Conclusión.

- Las **fixtures** son la forma que tiene Playwright de compartir objetos y gestionar recursos entre tests.
- Se crean extendiendo `base.extend()` y se inyectan automáticamente en cada test que las solicita.
- Las **fixtures de Page Objects** nos permiten usar nuestras clases de POM directamente en los tests sin instanciarlas manualmente.
- Las **fixtures de API** nos permiten interactuar con el backend desde los tests usando `request` como base.
- Combinar fixtures de UI y de API en el mismo test nos da una visión completa del estado de la aplicación.

* * *

Y hasta aquí esta primera parte sobre fixtures en Playwright. En la siguiente entrada veremos cómo crear fixtures con **ámbito de worker** para operaciones costosas como conexiones a base de datos, y cómo definir **datos opcionales por defecto** para nuestros tests. ¡Nos leemos en la siguiente entrada!
