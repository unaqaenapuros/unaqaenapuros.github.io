---
title: '089 – Playwright: Fixtures II – Worker Scope y datos opcionales.'
date: '2026-07-27T07:04:00+00:00'
url: /2026/07/27/089-playwright-fixtures-ii-worker-scope-y-datos-opcionales/
image: /img/blog-images/wp-posts/2026/05/foto78.png
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

Continuamos con la mini-serie sobre fixtures en Playwright. En la entrada anterior vimos qué son las fixtures y cómo crear las más básicas: las de **Page Objects** y las de **clases de API**. En esta segunda parte subimos un poco el nivel y veremos dos tipos de fixtures más avanzados: las fixtures con **ámbito de worker** ( _worker scope_), ideales para operaciones costosas que se pueden reutilizar entre tests, y las **fixtures de datos opcionales**, que nos permiten definir datos por defecto sobrescribibles en tests concretos. ¡Empezamos!

### 3\. Fixtures con ámbito de worker.

Hasta ahora, todas las fixtures que hemos visto son de **ámbito de test** ( _test scope_): se crean antes de cada test y se destruyen después. Esto es perfecto para la mayoría de los casos, pero hay operaciones que son muy costosas de repetir para cada test, como abrir una conexión a base de datos o inicializar un generador de datos.

Para estos casos, Playwright nos ofrece las **fixtures con ámbito de worker** ( `scope: 'worker'`). Un _worker_ es el proceso que Playwright usa para ejecutar tests en paralelo. Las fixtures de worker se crean **una sola vez por worker** y se comparten entre todos los tests que se ejecutan en ese worker, en lugar de crearse y destruirse para cada test individual.

Las ventajas de las fixtures de worker son:

- **Eficiencia**: las operaciones costosas (conexiones a base de datos, autenticaciones complejas...) se realizan una sola vez por worker.
- **Reutilización de recursos**: todos los tests del worker comparten la misma instancia.
- **Consistencia**: todos los tests del worker trabajan con el mismo estado inicial.
- **Rendimiento**: al reutilizar conexiones y objetos ya inicializados, la suite de tests corre más rápido.

#### Ejemplo: helper de base de datos.

Imaginemos que necesitamos conectarnos a una base de datos en nuestros tests para verificar que los datos se han guardado correctamente. Abrir y cerrar una conexión para cada test sería muy costoso. Con una fixture de worker, lo hacemos una sola vez:

```
// helpers/database.helper.ts
import { Pool } from 'pg';

export class DatabaseHelper {
  private pool: Pool;

  async connect() {
    this.pool = new Pool({
      user: process.env.DB_USER,
      host: process.env.DB_HOST,
      database: process.env.DB_NAME,
      password: process.env.DB_PASSWORD,
      port: parseInt(process.env.DB_PORT || '5432'),
    });
  }

  async query(sql: string, params: any[] = []) {
    if (!this.pool) {
      throw new Error('Base de datos no conectada. Llama a connect() primero.');
    }
    const client = await this.pool.connect();
    try {
      const result = await client.query(sql, params);
      return result.rows;
    } finally {
      client.release();
    }
  }

  async disconnect() {
    if (this.pool) {
      await this.pool.end();
    }
  }
}

```

#### Ejemplo: generador de datos de prueba.

Otro uso habitual para las fixtures de worker es un generador de datos de prueba. Librerías como **Faker** nos permiten generar datos realistas y aleatorios para nuestros tests:

```
// helpers/test-data-generator.ts
import { faker } from '@faker-js/faker';

export class TestDataGenerator {
  async init() {
    // Lógica de inicialización si fuera necesaria
  }

  generateUser() {
    return {
      name: faker.person.fullName(),
      email: faker.internet.email(),
      password: faker.internet.password(),
    };
  }

  generateProduct() {
    return {
      name: faker.commerce.productName(),
      price: parseFloat(faker.commerce.price()),
      category: faker.commerce.department(),
    };
  }
}

```

#### Registrando las fixtures de worker.

La diferencia clave con las fixtures de test está en la forma de registrarlas: se envuelven en un array y se añade `{ scope: 'worker' }` como segundo elemento. Además, el tipo de la fixture se declara en el segundo parámetro de tipo de `base.extend`, no en el primero:

```
// fixtures.ts
import { test as base } from '@playwright/test';
import { DatabaseHelper } from './helpers/database.helper';
import { TestDataGenerator } from './helpers/test-data-generator';

export const test = base.extend<
  {},                                      // Tipos de fixtures de test
  {                                        // Tipos de fixtures de worker
    dbHelper: DatabaseHelper;
    testDataGen: TestDataGenerator;
  }
>({
  dbHelper: [async ({}, use) => {
    const dbHelper = new DatabaseHelper();
    await dbHelper.connect();      // Se ejecuta UNA VEZ por worker
    await use(dbHelper);
    await dbHelper.disconnect();   // Se ejecuta UNA VEZ por worker, al finalizar
  }, { scope: 'worker' }],

  testDataGen: [async ({}, use) => {
    const testDataGen = new TestDataGenerator();
    await testDataGen.init();
    await use(testDataGen);
  }, { scope: 'worker' }],
});

```

#### Usando las fixtures de worker en los tests.

Desde el punto de vista del test, no hay ninguna diferencia en el uso: se solicitan como cualquier otra fixture:

```
// user.spec.ts
import { test } from './fixtures';
import { expect } from '@playwright/test';

test.describe('Gestión de usuarios', () => {
  test('la lista de usuarios tiene elementos', async ({ page, dbHelper }) => {
    // La base de datos ya está conectada gracias a la fixture de worker
    await page.goto('/users');
    const userCount = await page.locator('.user-item').count();
    expect(userCount).toBeGreaterThan(0);
  });

  test('crear un nuevo usuario lo guarda en la base de datos', async ({ page, dbHelper, testDataGen }) => {
    const newUser = testDataGen.generateUser();

    await page.goto('/users/new');
    await page.fill('#name', newUser.name);
    await page.fill('#email', newUser.email);
    await page.click('#submit');

    // Verificamos que el usuario se ha guardado en la base de datos
    const rows = await dbHelper.query(
      'SELECT * FROM users WHERE email = $1',
      [newUser.email]
    );
    expect(rows.length).toBe(1);
  });
});

```

#### Precauciones con las fixtures de worker.

Las fixtures de worker son muy potentes, pero hay que usarlas con cuidado:

- **Aislamiento**: asegúrate de que los tests no interfieren entre sí modificando el estado compartido. Si un test modifica datos de la base de datos, puede afectar a los tests que se ejecutan después en el mismo worker.
- **Fugas de recursos**: implementa correctamente la fase de limpieza (el código después de `await use(...)`) para evitar que las conexiones y recursos queden abiertos.
- **Variables de entorno**: usa siempre variables de entorno para gestionar cadenas de conexión y credenciales. Nunca las pongas directamente en el código.

### 4\. Fixtures de datos opcionales.

Las **fixtures de datos opcionales** son otro patrón muy útil: nos permiten definir datos de prueba por defecto que se pueden sobrescribir en tests concretos cuando necesitamos una variación.

La idea es que la mayoría de los tests usen unos datos "estándar" (un usuario genérico, un producto básico...), pero si un test concreto necesita datos diferentes (un usuario administrador, un producto sin stock...), puede indicarlo sin necesidad de configurar todo desde cero.

#### Definiendo la fixture con datos por defecto.

Usamos `{ option: true }` para marcar la fixture como un **option** (opción configurable):

```
// types/user.ts
export interface User {
  username: string;
  password: string;
  email: string;
  role: 'admin' | 'user';
}

// fixtures.ts
import { test as base } from '@playwright/test';
import { User } from './types/user';

export const test = base.extend<{
  testUser?: User;
}>({
  testUser: [async ({}, use) => {
    // Datos por defecto
    await use({
      username: 'defaultuser',
      password: 'defaultpass123',
      email: 'default@example.com',
      role: 'user',
    });
  }, { option: true }],
});

```

#### Usando la fixture con los datos por defecto.

La mayoría de tests simplemente solicitan `testUser` y obtienen los datos por defecto:

```
// user.spec.ts
import { test } from './fixtures';
import { expect } from '@playwright/test';

test.describe('Funcionalidad de usuario', () => {
  test('el usuario puede hacer login con las credenciales por defecto', async ({ page, testUser }) => {
    await page.goto('/login');
    await page.fill('#username', testUser.username);
    await page.fill('#password', testUser.password);
    await page.click('#login-button');
    await expect(page).toHaveURL(/\/dashboard/);
  });

```

#### Sobrescribiendo los datos para un test concreto.

Cuando un test concreto necesita datos diferentes, usamos `test.use()` para indicarlo. Playwright fusionará los datos que especifiquemos con los valores por defecto:

```
  test('el usuario admin puede acceder al panel de administración', async ({ page, testUser }) => {
    // Sobrescribimos la fixture solo para este test
    test.use({
      testUser: {
        username: 'adminuser',
        password: 'adminpass123',
        email: 'admin@example.com',
        role: 'admin',
      },
    });

    await page.goto('/login');
    await page.fill('#username', testUser.username);
    await page.fill('#password', testUser.password);
    await page.click('#login-button');

    await page.click('#admin-panel');
    await expect(page).toHaveURL(/\/admin/);
  });
});

```

#### Buenas prácticas con las fixtures de datos opcionales.

- Mantén los **datos por defecto simples y genéricos**. Los casos especiales van en los overrides.
- Crea **múltiples fixtures de datos** para distintas entidades: `testUser`, `testProduct`, `testOrder`...
- Usa interfaces de TypeScript para garantizar que los datos tienen el formato correcto.
- Al sobrescribir, especifica **solo las propiedades que necesitas cambiar**.

### Conclusión.

- Las **fixtures de worker** ( `scope: 'worker'`) se crean una sola vez por proceso de Playwright y se comparten entre todos los tests del worker. Son ideales para conexiones a base de datos, autenticaciones costosas o generadores de datos.
- La limpieza de las fixtures de worker (el código tras `await use(...)`) se ejecuta al terminar todos los tests del worker, no tras cada test individual.
- Las **fixtures de datos opcionales** ( `option: true`) nos permiten definir datos por defecto que se pueden sobrescribir en tests concretos con `test.use()`.
- Ambos patrones ayudan a crear suites de tests más eficientes, organizadas y mantenibles.

* * *

Y hasta aquí esta segunda parte sobre fixtures en Playwright. En la siguiente y última entrega de esta mini-serie veremos cómo **tipar nuestras fixtures con TypeScript**, cómo **combinar todos los tipos de fixtures** en una arquitectura completa y cómo usar `mergeTests` para mantener el código organizado. ¡Nos leemos en la siguiente entrada!
