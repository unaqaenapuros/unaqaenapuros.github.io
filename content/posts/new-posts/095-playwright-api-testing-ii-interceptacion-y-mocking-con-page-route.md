---
title: '095 – Playwright: API Testing II – Interceptación y mocking con page.route().'
date: '2026-10-19T09:30:00+02:00'
url: /2026/10/19/095-playwright-api-testing-ii-interceptacion-y-mocking-con-page-route/
image: /img/blog-images/new-posts/2026/10/foto84.png
categories:
- automation
- best-practices
- playwright
- qa
tags:
- api
- mocking
- testing
author: estefafdez
social_text: |
  `page.route()` es una de las funcionalidades más potentes de Playwright y una de las más infrautilizadas. En el nuevo artículo vemos qué es la interceptación y el mocking, por qué eliminan los tests inestables y cuatro casos prácticos: respuesta válida, error 500, estado vacío y modificar la respuesta real conservando el resto del backend intacto.

  #Playwright #QA #TestAutomation #APITesting #UnaQAEnApuros
---
¡Hola a todos!

Continuamos con la serie de API testing en Playwright. En la entrada anterior vimos los fundamentos: qué es una API, los métodos HTTP y los códigos de estado. Hoy entramos en uno de los temas más potentes del testing de UI moderno: la **interceptación y el mocking de respuestas** con `page.route()`. Es una de esas técnicas que, una vez que la usas, no puedes imaginarte cómo hacías los tests sin ella. ¡Empezamos!

### ¿Qué es la interceptación y qué es el mocking?

Son dos conceptos relacionados pero distintos:

**Interceptación** es la capacidad de capturar y controlar las peticiones de red que el navegador hace durante un test. Te sitúas entre la UI y el backend:

```
UI → Backend real → Respuesta
```

**Mocking** es ir un paso más allá: en lugar de dejar que la petición llegue al servidor real, la reemplazas con una **respuesta controlada y falsa** que tú defines:

```
UI → Playwright (mock) → Respuesta falsa
```

La clave conceptual es que el frontend no sabe la diferencia. Recibe una respuesta con el formato correcto y actúa en consecuencia, igual que si viniera del servidor real. Esto es lo que convierte al mocking en una herramienta tan potente para aislar la UI del backend.

### Por qué usamos el mocking en tests de UI.

Hay cuatro razones principales por las que los equipos adoptan esta técnica:

  1. **Eliminar tests inestables**: las APIs fallan, las redes tienen latencia, los entornos de CI son impredecibles. El mocking elimina toda esa variabilidad: si tú controlas la respuesta, el test siempre tiene el mismo punto de partida.
  2. **Testear antes de que el backend esté listo**: en equipos ágiles, el frontend suele avanzar antes que el backend. Con mocking, el equipo de front puede escribir y ejecutar tests completos contra una API que todavía no existe o no está desplegada.
  3. **Simular casos extremos con facilidad**: errores 500, respuestas vacías, datos con formatos inesperados... estos escenarios son casi imposibles de reproducir de forma fiable con una API real. Con mocking son triviales.
  4. **Acelerar la ejecución**: los tests con mocking son significativamente más rápidos porque no hacen llamadas de red reales. Son ideales para pipelines de CI/CD.

> _"El mocking no es evitar la realidad, es controlarla."_ Sigues necesitando tests contra la API real, pero no para cada escenario de UI.

### Cuándo mockear y cuándo no.

No todos los tests deberían usar mocking. Una estrategia madura lo aplica según el tipo de test:

| Tipo de test | ¿Usar mocking? |
|---|---|
| Tests funcionales de UI | Sí |
| Tests de componentes | Sí |
| Tests de integración | Parcialmente |
| Tests _end-to-end_ | No |

Los tests E2E deberían ejecutarse contra APIs reales para validar que el sistema completo funciona como una unidad. El mocking es para todo lo que está por debajo de esa capa.

### Cómo funciona `page.route()`.

Playwright nos da `page.route()` para interceptar peticiones. Este método acepta dos parámetros:

1. Un **patrón de URL** (string, glob o expresión regular).
2. Una **función handler** que recibe la ruta capturada.

Desde el handler podemos hacer cuatro cosas:

  * `route.fulfill(...)` — responder con una respuesta mock que definimos nosotros.
  * `route.abort()` — cancelar la petición (como si no hubiera red).
  * `route.continue()` — dejar pasar la petición al servidor real sin modificarla.
  * `route.fetch()` + `route.fulfill(...)` — hacer la petición real, modificar la respuesta y devolverla al navegador.

### Caso 1: simular una respuesta correcta.

**Escenario**: verificar que la página de catálogo muestra correctamente los productos cuando la API devuelve datos válidos.

```typescript
import { test, expect } from '@playwright/test';

test('la página de catálogo muestra los productos correctamente', async ({ page }) => {
  await page.route('**/api/productos', async (route) => {
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify([
        { id: 1, name: 'Camiseta básica', price: 19.99, stock: 50 },
        { id: 2, name: 'Pantalón vaquero', price: 49.99, stock: 15 },
        { id: 3, name: 'Zapatillas deportivas', price: 89.99, stock: 8 }
      ])
    });
  });

  await page.goto('/catalogo');

  await expect(page.locator('text=Camiseta básica')).toBeVisible();
  await expect(page.locator('text=Pantalón vaquero')).toBeVisible();
  await expect(page.locator('text=Zapatillas deportivas')).toBeVisible();
});
```

Fíjate en el orden: **siempre registramos la ruta antes de navegar** con `page.goto()`. Si navegas primero, la petición puede salir antes de que el interceptor esté activo y el mock no se aplicará.

### Caso 2: simular un error del servidor.

**Escenario**: verificar que la UI muestra un mensaje de error cuando el backend devuelve un 500.

```typescript
test('la página de checkout muestra un error cuando la API falla', async ({ page }) => {
  await page.route('**/api/pedidos', async (route) => {
    await route.fulfill({
      status: 500,
      contentType: 'application/json',
      body: JSON.stringify({ message: 'Error interno del servidor' })
    });
  });

  await page.goto('/checkout');
  await page.getByRole('button', { name: 'Confirmar pedido' }).click();

  await expect(page.locator('text=No se pudo procesar el pedido')).toBeVisible();
  await expect(page.locator('text=Inténtalo de nuevo más tarde')).toBeVisible();
});
```

Este es exactamente el tipo de escenario difícil de reproducir con una API real. ¿Cómo provocas de forma controlada un error 500 en producción? Con mocking es inmediato y reproducible.

### Caso 3: simular un estado vacío.

**Escenario**: verificar que la UI gestiona correctamente una respuesta vacía, por ejemplo cuando el carrito de la compra no tiene artículos.

```typescript
test('el carrito muestra el estado vacío cuando no hay artículos', async ({ page }) => {
  await page.route('**/api/carrito', async (route) => {
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify({ items: [], total: 0 })
    });
  });

  await page.goto('/carrito');

  await expect(page.locator('text=Tu carrito está vacío')).toBeVisible();
  await expect(page.locator('text=Seguir comprando')).toBeVisible();
  await expect(page.getByRole('button', { name: 'Finalizar compra' })).not.toBeVisible();
});
```

### Caso 4: modificar la respuesta real.

**Escenario**: hacer la petición real al servidor, pero sobreescribir solo un campo concreto de la respuesta. Útil cuando el backend está disponible pero queremos aislar y testear un estado específico de la UI.

```typescript
test('la UI muestra "Sin stock" cuando el stock del producto es 0', async ({ page }) => {
  await page.route('**/api/productos/1', async (route) => {
    const realResponse = await route.fetch();
    const data = await realResponse.json();

    // Solo modificamos el stock; el resto de la respuesta viene del servidor real
    data.stock = 0;

    await route.fulfill({
      response: realResponse,
      body: JSON.stringify(data)
    });
  });

  await page.goto('/productos/1');

  await expect(page.locator('text=Sin stock')).toBeVisible();
  await expect(page.getByRole('button', { name: 'Añadir al carrito' })).toBeDisabled();
});
```

Este patrón es especialmente útil cuando quieres mantener el comportamiento real del backend para la mayoría de campos pero necesitas forzar un estado concreto en la UI.

### Conclusión.

  * La **interceptación** captura peticiones de red; el **mocking** las reemplaza con respuestas controladas.
  * `page.route()` es la API de Playwright para interceptar: recibe un patrón de URL y un handler desde el que podemos `fulfill`, `abort`, `continue` o `fetch` y modificar la respuesta.
  * **Siempre registra las rutas antes de navegar** con `page.goto()`.
  * El mocking elimina inestabilidad, permite testear estados difíciles de reproducir y acelera la ejecución en CI.
  * No uses mocking en tests E2E: reserva la interceptación para tests funcionales y de componentes donde el aislamiento del backend aporta valor real.

* * *

Y hasta aquí esta segunda entrega sobre API testing con Playwright. En la siguiente y última parte veremos los casos más avanzados: cómo simular respuestas lentas para testear estados de carga, bloquear llamadas externas innecesarias, hacer mocking condicional según los datos de la petición y las buenas prácticas para evitar los errores más comunes. ¡Nos leemos en la siguiente entrada!
