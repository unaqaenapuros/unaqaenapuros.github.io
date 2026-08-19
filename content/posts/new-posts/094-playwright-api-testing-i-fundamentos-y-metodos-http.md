---
title: '094 – Playwright: API Testing I – Fundamentos y métodos HTTP.'
date: '2026-10-05T09:30:00+02:00'
url: /2026/10/05/094-playwright-api-testing-i-fundamentos-y-metodos-http/
image: /img/blog-images/new-posts/2026/10/foto83.png
categories:
- automation
- best-practices
- playwright
- qa
tags:
- api
- testing
author: estefafdez
social_text: |
  ¿Sabías que Playwright no es solo para UI? También puedes testear tus APIs directamente con la fixture `request`. En el nuevo artículo del blog repasamos los fundamentos: qué es una API, los 5 métodos HTTP con ejemplos reales y qué significan los códigos de estado. Primera parte de la nueva mini-serie de API testing.

  #Playwright #QA #TestAutomation #APITesting #UnaQAEnApuros
---
¡Hola a todos!

Cerramos la mini-serie de accesibilidad y abrimos una nueva: **API testing con Playwright**. La mayoría conocemos Playwright como herramienta de automatización de navegador, pero tiene capacidades muy potentes para testear APIs directamente, sin necesidad de abrir ningún navegador. En esta primera entrega vamos a ver qué es una API, por qué Playwright es una buena opción para testearlas, cómo funcionan los métodos HTTP y qué significan los códigos de respuesta. ¡Empezamos!

### ¿Qué es una API?

Para entender qué es una **API** (_Application Programming Interface_, o interfaz de programación de aplicaciones), nada mejor que un ejemplo del día a día.

Imagina que tienes instalada en el móvil una aplicación de música en _streaming_. Cuando buscas una canción:

  * La app envía tu búsqueda al servidor.
  * El servidor busca en su base de datos.
  * El servidor devuelve la lista de canciones que coinciden.
  * La app muestra los resultados en pantalla.

Olvídate de lo que ves en pantalla. Fíjate solo en la **comunicación que ocurre entre la app y el servidor**. Ese intercambio de mensajes es exactamente lo que es una API.

Igual que cuando probamos la UI verificamos que lo que el usuario ve y hace es correcto, cuando probamos una API verificamos que ese intercambio de mensajes entre sistemas funciona bien:

  * **Solicitud correcta → respuesta correcta**: buscas "Bohemian Rhapsody" y recibes la canción. El test pasa.
  * **Solicitud correcta → respuesta incorrecta**: buscas "Bohemian Rhapsody" y recibes una lista de jazz. El test falla.
  * **Información incompleta**: envías una búsqueda vacía. El sistema debería devolver un error claro, no romperse sin avisar.
  * **Solicitud no autorizada**: alguien intenta acceder a tu lista de reproducción privada sin autenticarse. El sistema debe rechazar la petición.
  * **Respuesta lenta**: haces una búsqueda y tarda 10 segundos. El sistema debe tener tiempos de respuesta razonables.

### Por qué Playwright es una buena opción para API testing.

Playwright es ampliamente conocido como herramienta de automatización de navegador, pero también ofrece capacidades muy potentes para testear APIs. Sus principales ventajas para los equipos de QA son:

  * Podemos **combinar tests de API y de UI en la misma suite**, con la misma sintaxis y las mismas herramientas. No hace falta aprender un framework separado.
  * Es **rápido**: los tests de API no levantan ningún navegador, por lo que su ejecución es significativamente más rápida que los tests de UI.
  * La **curva de aprendizaje es suave**: si el equipo ya usa Playwright para UI, añadir tests de API es un paso pequeño.
  * Soporta **escenarios de autenticación complejos**: _token-based_, OAuth, cookies de sesión...
  * La fixture predefinida `request` nos da un contexto HTTP completo para hacer llamadas directas a la API desde cualquier test.

### Los métodos HTTP.

En el testing de APIs usamos diferentes **métodos HTTP** según la operación que queramos realizar. Los más habituales son:

  * **GET**: obtener datos. No modifica nada en el servidor.
  * **POST**: crear un nuevo recurso.
  * **PUT**: reemplazar completamente un recurso existente.
  * **PATCH**: actualizar solo una parte de un recurso existente.
  * **DELETE**: eliminar un recurso.

Vamos a ver ejemplos concretos usando la fixture `request` de Playwright. Usaremos una API de gestión de artículos de blog como hilo conductor:

#### GET: obtener datos.

```typescript
import { test, expect } from '@playwright/test';

test('GET – obtener un artículo por su ID', async ({ request }) => {
  const response = await request.get('/api/articulos/5');
  expect(response.status()).toBe(200);

  const body = await response.json();
  expect(body.id).toBe(5);
  expect(body.title).toBeDefined();
});
```

#### POST: crear un recurso.

```typescript
test('POST – publicar un nuevo comentario', async ({ request }) => {
  const response = await request.post('/api/comentarios', {
    data: {
      articleId: 5,
      author: 'Ana García',
      content: 'Muy buen artículo, gracias por explicarlo tan claro.'
    }
  });

  expect(response.status()).toBe(201);
  const body = await response.json();
  expect(body.author).toBe('Ana García');
});
```

#### PUT: reemplazar un recurso completo.

```typescript
test('PUT – actualizar un artículo completo', async ({ request }) => {
  const response = await request.put('/api/articulos/5', {
    data: {
      title: 'Playwright y API Testing: guía completa',
      content: 'Contenido actualizado del artículo...',
      status: 'publicado'
    }
  });

  expect(response.status()).toBe(200);
  const body = await response.json();
  expect(body.title).toBe('Playwright y API Testing: guía completa');
});
```

#### PATCH: actualizar parcialmente un recurso.

```typescript
test('PATCH – cambiar solo el estado de un artículo', async ({ request }) => {
  const response = await request.patch('/api/articulos/5', {
    data: {
      status: 'borrador'
    }
  });

  expect(response.status()).toBe(200);
  const body = await response.json();
  expect(body.status).toBe('borrador');
});
```

#### DELETE: eliminar un recurso.

```typescript
test('DELETE – eliminar un comentario', async ({ request }) => {
  const response = await request.delete('/api/comentarios/12');
  expect(response.status()).toBe(204);
});
```

La diferencia clave entre **PUT** y **PATCH** es el alcance: PUT reemplaza el recurso entero (si no envías un campo, ese campo desaparece o queda en blanco), mientras que PATCH solo modifica los campos que incluyes en la petición.

### Los códigos de estado HTTP.

Un **código de estado** es el número que devuelve el servidor para indicar qué ocurrió con la petición. Es una parte esencial de lo que verificamos en cualquier test de API.

Se agrupan por rangos:

#### Éxito (2xx).

  * `200 OK` → La petición fue correcta y el servidor devuelve datos.
  * `201 Created` → Se creó un nuevo recurso correctamente.
  * `204 No Content` → La petición fue correcta pero no hay datos que devolver (típico de DELETE).

#### Errores del cliente (4xx).

  * `400 Bad Request` → La petición tiene un formato incorrecto o faltan campos obligatorios.
  * `401 Unauthorized` → Se requiere autenticación para acceder al recurso.
  * `403 Forbidden` → El usuario está autenticado pero no tiene permiso para esa operación.
  * `404 Not Found` → El recurso solicitado no existe.

#### Errores del servidor (5xx).

  * `500 Internal Server Error` → Algo falló en el servidor.
  * `502 Bad Gateway` → El servidor recibió una respuesta inválida de otro servicio.
  * `503 Service Unavailable` → El servidor está caído o demasiado ocupado para responder.

Siempre que escribas un test de API, verifica tanto el **código de estado** como el **cuerpo de la respuesta**. Un `200` con datos incorrectos es tan malo como un `500`.

### Conclusión.

  * Una **API** es el mecanismo de comunicación entre sistemas: el cliente envía una petición y el servidor devuelve una respuesta.
  * Playwright permite testear APIs directamente mediante la fixture `request`, sin necesidad de abrir un navegador.
  * Los métodos HTTP definen la operación: **GET** para leer, **POST** para crear, **PUT** para reemplazar, **PATCH** para actualizar parcialmente y **DELETE** para eliminar.
  * Los **códigos de estado** son la primera señal del resultado: 2xx es éxito, 4xx son errores del cliente y 5xx son errores del servidor.
  * Un buen test de API siempre verifica tanto el código de estado como el contenido de la respuesta.

* * *

Y hasta aquí esta primera entrada sobre API testing con Playwright. En la siguiente entrega veremos una de las capacidades más potentes del framework para hacer tests estables y controlados: la **interceptación y el mocking de respuestas** con `page.route()`. ¡Nos leemos en la siguiente entrada!
