---
title: '096 – Playwright: API Testing III – Mocking avanzado y buenas prácticas.'
date: '2026-11-02T09:30:00+01:00'
url: /2026/11/02/096-playwright-api-testing-iii-mocking-avanzado-y-buenas-practicas/
image: /img/blog-images/new-posts/2026/11/foto85.png
categories:
- automation
- best-practices
- code-quality
- playwright
- qa
tags:
- api
- mocking
- testing
author: estefafdez
---
<!--
## Resumen para LinkedIn

Cerramos la mini-serie de API testing con los casos más avanzados de mocking en Playwright: simular respuestas lentas para testear spinners de carga, bloquear llamadas de analítica en CI, mocking condicional para flujos de login por roles, y las buenas prácticas para no caer en los errores típicos. El mocking no es evitar la realidad: es controlarla.

👉 Enlace en comentarios.

#Playwright #QA #TestAutomation #APITesting #UnaQAEnApuros
-->

¡Hola a todos!

Llegamos a la última entrega de la mini-serie de API testing con Playwright. En la anterior vimos los cuatro casos base de `page.route()`: respuesta válida, error de servidor, estado vacío y modificación de la respuesta real. Hoy subimos el nivel: respuestas lentas para testear estados de carga, bloqueo de llamadas externas, mocking condicional según los datos de la petición, y cerramos con las buenas prácticas y los errores más comunes. ¡Empezamos!

### Caso 5: simular una respuesta lenta.

**Escenario**: verificar que la UI muestra un indicador de carga mientras espera la respuesta de la API. Este es exactamente el tipo de estado que en tests manuales se ve _de refilón_ y en tests automatizados normalmente se ignora porque la API real responde demasiado rápido en un entorno local.

```typescript
import { test, expect } from '@playwright/test';

test('la búsqueda muestra el spinner mientras espera la respuesta', async ({ page }) => {
  await page.route('**/api/busqueda', async (route) => {
    // Simulamos un retraso de 2 segundos antes de responder
    await new Promise((res) => setTimeout(res, 2000));

    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify([
        { id: 10, name: 'Resultado 1 – Zapatillas running' },
        { id: 11, name: 'Resultado 2 – Zapatillas trail' }
      ])
    });
  });

  await page.goto('/busqueda?q=zapatillas');

  // Durante el retraso, el indicador de carga debe estar visible
  await expect(page.locator('.spinner-busqueda')).toBeVisible();

  // Cuando llega la respuesta, el spinner desaparece y se muestran los resultados
  await expect(page.locator('text=Resultado 1 – Zapatillas running')).toBeVisible();
  await expect(page.locator('.spinner-busqueda')).not.toBeVisible();
});
```

Este patrón es especialmente valioso en equipos donde el frontend y el backend se desarrollan en paralelo: podemos verificar los estados de carga sin depender de la velocidad real de la red ni necesitar un backend desplegado.

### Caso 6: bloquear llamadas externas innecesarias.

**Escenario**: durante los tests, nuestra aplicación puede lanzar peticiones a servicios de terceros — herramientas de analítica, _trackers_, chatbots de soporte, píxeles publicitarios. Estas llamadas ralentizan los tests, generan datos de prueba en sistemas externos y pueden causar inestabilidad si esos servicios tienen latencia o fallos intermitentes.

La solución es bloquearlas con `route.abort()`:

```typescript
test('la página principal carga sin ejecutar llamadas de analítica', async ({ page }) => {
  // Bloqueamos cualquier petición a servicios de analítica y tracking
  await page.route('**/analytics/**', (route) => route.abort());
  await page.route('**/tracking/**', (route) => route.abort());
  await page.route('**/*.hotjar.io/**', (route) => route.abort());
  await page.route('**/api/chat-widget/**', (route) => route.abort());

  await page.goto('/');

  // Verificamos que la página cargó correctamente a pesar de los bloqueos
  await expect(page.locator('h1')).toBeVisible();
  await expect(page).toHaveURL(/.*\//);
});
```

Bloquear las llamadas externas tiene dos beneficios directos: los tests son más rápidos y no generamos datos de prueba en herramientas de analítica reales con cada ejecución del pipeline.

### Caso 7: mocking condicional según los datos de la petición.

**Escenario**: simular que la API devuelve respuestas distintas según los datos que recibe en la petición. El caso más típico es el formulario de login: las credenciales correctas devuelven un token de sesión, las incorrectas devuelven un error de autenticación.

```typescript
test('el login responde de forma diferente según las credenciales', async ({ page }) => {
  await page.route('**/api/auth/login', async (route, req) => {
    const body = req.postDataJSON();

    if (body.email === 'admin@ejemplo.com') {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({ token: 'jwt-valido-abc123', role: 'admin' })
      });
    } else {
      await route.fulfill({
        status: 401,
        contentType: 'application/json',
        body: JSON.stringify({ error: 'Credenciales incorrectas' })
      });
    }
  });

  await page.goto('/login');

  // Flujo de éxito: credenciales correctas → redirige al dashboard
  await page.fill('#email', 'admin@ejemplo.com');
  await page.fill('#password', 'contraseña-segura');
  await page.click('button[type="submit"]');
  await expect(page).toHaveURL(/\/dashboard/);
});
```

El mocking condicional nos permite probar múltiples flujos del mismo formulario o componente sin necesitar usuarios con distintos roles configurados en el entorno de test. Podemos simular un administrador, un usuario sin permisos o una cuenta bloqueada con la misma facilidad.

### Buenas prácticas.

Después de ver los siete casos, estas son las reglas que hacen que el mocking sea una estrategia sólida:

  * **Registra siempre las rutas antes de navegar**: `page.route()` debe ejecutarse antes que `page.goto()`. Si navegas primero, la petición puede salir antes de que el interceptor esté activo.

  * **Mantén los mocks realistas**: usa el mismo esquema de respuesta que devuelve la API real. Si el mock tiene una estructura diferente, el test puede pasar aunque la UI se rompería con datos reales.

  * **No abuses del mocking**: demasiado mocking da una falsa sensación de seguridad. Si lo mockeas todo, tus tests pueden pasar mientras el sistema real falla. Reserva el mocking para tests funcionales y de componentes; los tests E2E deben ir contra el backend real.

  * **Abstrae los mocks repetidos**: si el mismo mock se usa en varios tests, extráelo a una función _helper_ o a una **fixture** de Playwright. Evita copiar el mismo bloque `page.route()` en diez ficheros diferentes.

  * **Combina con fixtures**: `page.route()` se puede registrar dentro de una fixture para que esté disponible en todos los tests que la necesiten, manteniendo los tests limpios y con una sola responsabilidad.

```typescript
// fixtures/api-mocks.ts
import { test as base } from '@playwright/test';

export const test = base.extend({
  mockEmptyCart: async ({ page }, use) => {
    await page.route('**/api/carrito', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({ items: [], total: 0 })
      });
    });
    await use(page);
  },
});
```

### Errores comunes que debes evitar.

  * **Interceptar demasiado ampliamente**: usar `'**/*'` como patrón captura todas las peticiones, incluyendo las que no querías mockear. Sé específico con los patrones de URL.
  * **Olvidar el `await` en el handler**: las funciones de handler son asíncronas. Olvidar el `await` antes de `route.fulfill()` puede hacer que el mock no se aplique a tiempo y la petición pase al servidor real.
  * **Ignorar el contrato real de la API**: el mock debe reflejar el esquema real que devuelve el backend. Si el backend cambia y no actualizas los mocks, los tests seguirán pasando pero el sistema fallará en producción.
  * **Mezclar tests con mocking con tests E2E**: los tests que verifican la integración completa del sistema no deberían usar mocking. Mezclarlos genera confusión sobre qué está realmente validando cada test.

### El mocking como estrategia, no solo como técnica.

La conclusión más importante de toda esta mini-serie es que el mocking no es un atajo: es una **estrategia de testing**. Una suite de automatización madura lo aplica de forma consciente:

  * **Usa mocking para velocidad y fiabilidad**: en tests funcionales y de componentes, donde necesitas ejecución rápida y resultados deterministas.
  * **Usa APIs reales para confianza y validación de integración**: en tests E2E, donde el objetivo es verificar que el sistema completo funciona como una unidad.

El equilibrio entre ambos enfoques es lo que define una suite de tests robusta y mantenible a largo plazo.

### Conclusión.

  * Simular **respuestas lentas** con `setTimeout` dentro del handler permite testear estados de carga que de otra forma serían difíciles o imposibles de reproducir de forma fiable.
  * **Bloquear llamadas externas** con `ruta.abort()` hace los tests más rápidos y evita generar datos de prueba en servicios de analítica o tracking reales.
  * El **mocking condicional** basado en los datos de la petición permite simular flujos completos — login, roles, permisos — sin necesitar usuarios reales configurados en el entorno.
  * Las reglas clave: registrar rutas **antes de navegar**, mantener los mocks **realistas**, **no abusar** del mocking y abstraer los handlers repetidos en **helpers o fixtures**.
  * El mocking es una estrategia de testing: úsalo donde aporta velocidad y control, y evítalo donde la validación de integración real es necesaria.

* * *

Y hasta aquí nuestra mini-serie de API testing con Playwright. Hemos recorrido desde los fundamentos de las APIs y los métodos HTTP hasta el mocking avanzado con `page.route()`. ¡Nos leemos en la siguiente entrada!
