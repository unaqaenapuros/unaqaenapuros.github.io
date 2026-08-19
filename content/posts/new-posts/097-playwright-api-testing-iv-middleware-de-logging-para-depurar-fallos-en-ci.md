---
title: '097 – Playwright: API Testing IV – Middleware de logging para depurar fallos en CI.'
date: '2026-11-16T09:30:00+01:00'
url: /2026/11/16/097-playwright-api-testing-iv-middleware-de-logging-para-depurar-fallos-en-ci/
image: /img/blog-images/new-posts/2026/11/foto86.png
categories:
- automation
- best-practices
- ci
- playwright
- qa
tags:
- api
- debugging
- testing
author: estefafdez
---
<!--
## Resumen para LinkedIn

Tu test falla en CI con `expected 201, received 400` y no tienes ni petición ni respuesta. ¿La solución? No más `console.log` en los tests: instrumenta el cliente con un middleware que captura todo el ciclo y lo adjunta directamente al informe HTML de Playwright con `test.info().attach()`. Configúralo una vez en el API factory y todo se registra solo, en todos los tests, para siempre.

👉 Enlace en comentarios.

#Playwright #QA #TestAutomation #APITesting #UnaQAEnApuros
-->

¡Hola a todos!

Seguimos con la serie de API testing en Playwright. En las tres entregas anteriores vimos los fundamentos, el mocking con `page.route()` y los casos avanzados. Hoy abordamos un problema que tarde o temprano nos encuentra a todos: el test falla en CI, el error dice `expected 200, received 400`, y no tienes ni idea de qué envió realmente la petición ni qué respondió el servidor. Hoy vemos cómo resolverlo con un **middleware de logging** que captura toda esa evidencia automáticamente y la adjunta al informe HTML de Playwright. ¡Empezamos!

### El problema: arqueología en CI.

Playwright es una herramienta fantástica, hasta que la ejecución de CI falla y no tienes contexto. El mensaje que recibes es algo así:

```
expected 201, received 400
```

Sin petición. Sin respuesta. Sin contexto.

Empieza lo que podríamos llamar _arqueología de CI_: relanzas el test en local, añades `console.log` temporales, intentas reproducir el fallo antes de que el entorno de CI cambie de nuevo. A veces tienes suerte. La mayoría de las veces, no.

El problema de fondo es simple: **Playwright no ofrece una forma nativa de persistir el ciclo completo de petición y respuesta** a través de la suite de tests. Y en sistemas modernos, eso no es opcional: es crítico.

Por defecto, cada llamada a la API en tus tests es una _petición invisible_. Se ejecuta. Afecta al resultado del test. Y luego desaparece. Esto se convierte en un problema real cuando trabajas con ejecuciones paralelas en CI, datos de test dinámicos, múltiples servicios o clientes de API generados automáticamente.

### Por qué `console.log` no es la solución.

El reflejo habitual es añadir `console.log` dentro de los tests. Funciona, al menos temporalmente, pero en ejecuciones paralelas de CI los logs se mezclan entre tests y el ruido hace desaparecer la señal. Acabas exactamente donde empezaste.

El problema no es que falten logs. El problema es **dónde estás registrando**.

En lugar de instrumentar tests individuales, la solución correcta es **instrumentar la frontera de red**. Un único punto de interceptación, fiable y automático, que captura todo lo que pasa por el cable sin que tengas que tocar ningún test.

### El punto de interceptación: el middleware.

Si usas un generador de clientes OpenAPI como `typescript-fetch`, ya tienes exactamente lo que necesitas: una **capa de middleware** por la que pasan todas las llamadas a la API, con hooks que se ejecutan antes de que salga la petición y después de que llegue la respuesta.

Este es el cambio conceptual clave:

> No instrumentas los tests — instrumentas el cliente.

Una vez que lo haces, el logging se vuelve automático, consistente e imposible de olvidar. No depende de la disciplina de cada desarrollador al escribir tests.

### Construyendo el middleware de logging.

No queremos logs ruidosos en la consola. Queremos **datos estructurados adjuntos directamente al informe HTML de Playwright**: el mismo lugar al que van los ingenieros cuando algo falla.

Playwright nos da `test.info().attach()` exactamente para esto: podemos adjuntar cualquier dato estructurado a un test y aparecerá como _attachment_ en el informe HTML.

Aquí está el middleware completo que captura el ciclo petición/respuesta y lo inyecta en el informe:

```typescript
// middleware/playwright-logging.middleware.ts
import test from '@playwright/test';
import { Middleware, RequestContext, ResponseContext } from './api-client';

export const playwrightLoggingMiddleware: Middleware = {
  pre: async (context: RequestContext) => {
    const method = context.init.method || 'GET';
    const url = context.url;
    const path = new URL(url).pathname;
    const headers = context.init.headers as Record<string, string> | undefined;

    let body;
    if (context.init.body) {
      try {
        body = typeof context.init.body === 'string'
          ? JSON.parse(context.init.body)
          : context.init.body;
      } catch {
        body = '[non-JSON body omitted]';
      }
    }

    await test.info().attach(`REQ: ${method} ${path}`, {
      body: JSON.stringify({ url, method, headers, body }, null, 2),
      contentType: 'application/json',
    });
  },

  post: async (context: ResponseContext) => {
    const method = context.init.method || 'GET';
    const path = new URL(context.url).pathname;
    const headers = context.response.headers;

    let body;
    if (headers.get('content-type')?.includes('application/json')) {
      /**
       * IMPORTANT: always use .clone().
       * Fetch streams can only be read once. Without cloning,
       * the test code will receive an empty body.
       */
      body = await context.response.clone().json();
    }

    await test.info().attach(`RES: ${context.response.status} ${path}`, {
      body: JSON.stringify({
        status: context.response.status,
        headers: Object.fromEntries(headers.entries()),
        body,
      }, null, 2),
      contentType: 'application/json',
    });
  },
};
```

Tres detalles importantes de esta implementación:

  * **`test.info().attach()`** adjunta datos estructurados directamente al informe HTML, en el apartado de _attachments_ de cada test.
  * **`response.clone()`** es crítico: los _streams_ de Fetch solo se pueden leer una vez. Si lees la respuesta en el middleware sin clonar primero, el código del test recibirá un cuerpo vacío y el test fallará de forma misteriosa.
  * **El formateo JSON** con `null, 2` mantiene los datos legibles en el informe.

Esto deja de ser _debugging_ para convertirse en **recolección de evidencia**.

### Conectar una vez, usar en todas partes.

Aquí es donde el enfoque se vuelve realmente potente. No tocas ningún test. Conectas el middleware **una sola vez**, a nivel del cliente de API:

```typescript
// api/api-factory.ts
import { Configuration, ArticlesApi, CommentsApi } from './generated-api';
import { playwrightLoggingMiddleware } from '../middleware/playwright-logging.middleware';

const config = new Configuration({
  basePath: process.env.API_BASE_URL,
  middleware: [playwrightLoggingMiddleware],
});

export const articlesApi = new ArticlesApi(config);
export const commentsApi = new CommentsApi(config);
```

A partir de ese momento, **toda llamada a la API se registra sola**. Sin decoradores. Sin configuración repetida en cada test. Sin que nadie tenga que acordarse de añadir nada.

### La experiencia después de implementarlo.

La próxima vez que un test falle con `expected 201, received 400`, no tendrás que adivinar nada. Abres el informe HTML de Playwright y en los _attachments_ del test fallido encuentras exactamente lo que ocurrió:

```json
// REQ: POST /api/comentarios
{
  "url": "https://api.ejemplo.com/api/comentarios",
  "method": "POST",
  "body": {
    "author": "Ana García",
    "content": "Muy buen artículo."
  }
}
```

```json
// RES: 400 /api/comentarios
{
  "status": 400,
  "body": {
    "code": "CAMPO_REQUERIDO",
    "message": "El campo articleId es obligatorio."
  }
}
```

En segundos ves que la petición se envió sin el campo `articleId`. No hubo que reproducir nada. La evidencia estaba en el informe desde el primer momento.

### Más allá del logging: middleware composable.

El middleware es **componible**. El logging es solo el principio. Una vez que tienes esta capa, puedes extenderla de forma natural sin tocar ningún test:

  * **Monitorización de rendimiento**: mide la latencia de cada petición y detecta _endpoints_ lentos.
  * **Reintentos automáticos**: gestiona respuestas `429` (demasiadas peticiones) o `503` (servicio no disponible) sin contaminar la lógica de los tests.
  * **Seguridad**: redacta cabeceras sensibles (tokens, cookies, API keys) antes de adjuntarlas al informe.
  * **Gestión de autenticación**: refresca tokens expirados de forma transparente entre petición y respuesta.

Todo esto ocurre en un único lugar, sin modificar ningún test. Cuando capturas lo que realmente ocurre en la red, tu suite de tests deja de ser una simple señal de verde/rojo y se convierte en una **fuente de verdad**.

### Conclusión.

  * Por defecto, las peticiones de API en tus tests son **peticiones invisibles**: se ejecutan, afectan al resultado y desaparecen sin dejar evidencia.
  * Añadir `console.log` en los tests es una solución temporal que se rompe en **ejecuciones paralelas**: los logs se mezclan y pierden su utilidad.
  * La solución correcta es **instrumentar el cliente**, no los tests: un middleware que intercepta cada petición antes de que salga y cada respuesta cuando llega.
  * **`test.info().attach()`** adjunta los datos estructurados directamente al informe HTML de Playwright, donde los ingenieros ya van a buscar información cuando algo falla.
  * **`response.clone()`** es imprescindible: leer el _stream_ de respuesta en el middleware sin clonar primero dejará el cuerpo vacío en el test.
  * El middleware es **componible**: una vez que existe esa capa, añadir monitorización de rendimiento, reintentos, redacción de datos sensibles o gestión de tokens es un paso natural.

* * *

Y hasta aquí esta cuarta entrega sobre API testing con Playwright. Hemos recorrido toda la serie: fundamentos, mocking básico, mocking avanzado y ahora observabilidad con middleware de logging. ¡Nos leemos en la siguiente entrada!
