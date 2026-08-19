---
title: '086 – Playwright: Por qué tu locator getByRole no funciona.'
date: '2026-06-15T07:03:00+00:00'
url: /2026/06/15/086-playwright-por-que-tu-locator-getbyrole-no-funciona/
image: /img/blog-images/wp-posts/2026/05/foto75.png
categories:
- automation
- best-practices
- code-quality
- ai
- playwright
- qa
tags:
- flaky
- getbyrole
- selectors
author: estefafdez
---
¡Hola a todos!

Seguimos con la serie de Playwright. En esta entrada vamos a hablar de uno de los problemas más comunes que nos encontramos cuando empezamos a automatizar con Playwright: el locator **`getByRole`** no encuentra el elemento aunque está ahí delante de nuestras narices. El test se queda esperando y acaba fallando por timeout. ¿Por qué pasa esto? La respuesta tiene que ver con **ARIA** y los **nombres accesibles**. ¡Empezamos!

### El problema clásico.

Imagina que tienes que automatizar una caja de búsqueda. Inspeccionas el HTML y ves esto:

```
<input
  class="DocSearch-Input"
  aria-labelledby="docsearch-label"
  placeholder="Search docs"
  type="search"
/>

```

Lo lógico es escribir el locator usando el texto del placeholder:

```
page.getByRole('searchbox', { name: 'Search docs' })

```

Pero el test falla. Así que pruebas:

```
page.getByRole('searchbox', { name: 'Search' })

```

Y funciona perfectamente. Pero... ¿cómo? El placeholder pone claramente "Search docs". ¿Dónde se ha ido el "docs"?

### El nombre accesible y su cadena de resolución.

Cuando usamos `getByRole` con la opción `name`, Playwright **no busca el texto del placeholder** ni el `id` del elemento ni ningún atributo arbitrario. Lo que busca es el **nombre accesible computado** del elemento: el mismo nombre que un lector de pantalla anunciaría a una persona con discapacidad visual.

Este nombre accesible se resuelve siguiendo una cadena de prioridad estricta, de mayor a menor:

1. **`aria-labelledby`**: referencia el contenido de texto de otro elemento del DOM. **Máxima prioridad.**
1. **`aria-label`**: proporciona directamente el texto del label como cadena.
1. **Elemento `<label>`** con atributo `for` que apunte al input.
1. **`placeholder` / `title`**: fallback de último recurso. **Mínima prioridad.**

En el ejemplo anterior, el input tenía `aria-labelledby="docsearch-label"`. Ese atributo apuntaba a un elemento `<label>` en el DOM con el texto **"Search"**, no "Search docs". Como `aria-labelledby` tiene la máxima prioridad, el `placeholder="Search docs"` quedaba completamente ignorado.

El placeholder estaba ahí a la vista, pero era irrelevante para cómo Playwright resolvía el nombre.

### `input` no es un rol ARIA.

Antes de llegar al problema del nombre, hay otra confusión habitual. Al ver un `<input>`, el instinto es escribir:

```
page.getByRole('input', { name: 'Search docs' })

```

Esto no funciona. **`input` es un tag HTML, no un rol ARIA.** El método `getByRole` trabaja con roles ARIA, que son descripciones semánticas de lo que hace un elemento, no del tag que usa.

El navegador asigna automáticamente un **rol ARIA implícito** a cada elemento HTML. Los más comunes son:

Elemento HTMLRol ARIA implícito`<input type="text">``textbox``<input type="search">``searchbox``<input type="checkbox">``checkbox``<input type="radio">``radio``<button>``button``<a href="...">``link``<h1>` a `<h6>``heading``<select>``combobox``<ul>``list`

Cuando los desarrolladores crean componentes personalizados con `<div>` y `<span>`, los roles implícitos no existen y es donde ARIA cobra toda su importancia.

### Cómo depurar: la pestaña Accessibility de DevTools.

Aquí viene el truco que nos ahorra mucho tiempo. Chrome DevTools tiene una forma de ver exactamente lo mismo que ve Playwright:

1. Click derecho sobre el elemento → **Inspeccionar**.
1. En DevTools, busca la pestaña **Accessibility** (puede estar oculta, haz click en `>>` para encontrarla).
1. Mira **Computed Properties → Name**.

Para nuestro input de búsqueda, la pestaña mostraría algo así:

```
Name: "Search"
  ▸ aria-labelledby:
      label#docsearch-label.DocSearch-MagnifierLabel...
    aria-label: Not specified
    From label (for= attribute): ...
    title: Not specified
    placeholder: "Search docs"  ← tachado, sobreescrito

```

La pestaña nos muestra toda la cadena de resolución: qué ha ganado y qué ha quedado sobreescrito (aparece tachado). **Esta es tu fuente de verdad** cada vez que `getByRole` no te encuentre el elemento que esperas.

### Matching parcial vs. exacto.

Otro punto importante que suele pasar desapercibido: `getByRole` hace **substring matching** por defecto para la opción `name`. Esto significa que cualquiera de estos locators coincide con un elemento cuyo nombre accesible sea "Search docs":

```
// Los tres coinciden con el nombre accesible "Search docs"
page.getByRole('searchbox', { name: 'Search' })       // substring ✅
page.getByRole('searchbox', { name: 'Search docs' })  // coincidencia exacta ✅
page.getByRole('searchbox', { name: 'docs' })         // substring ✅

```

Si queremos una coincidencia exacta, usamos la opción `exact`:

```
page.getByRole('searchbox', { name: 'Search', exact: true })       // ✅ coincide
page.getByRole('searchbox', { name: 'docs', exact: true })         // ❌ no coincide

```

Usar `exact: true` es recomendable para mayor robustez, especialmente cuando la página tiene varios elementos con nombres similares. El **Pick Locator** de Playwright sugiere `{ name: 'Search' }` porque busca el match más corto que sea único en la página.

### ¿Qué es ARIA?

Si llevas un tiempo escribiendo tests de Playwright sin pensar demasiado en ARIA, aquí va un repaso rápido.

**ARIA** son las siglas de _Accessible Rich Internet Applications_. Es un conjunto de atributos HTML que describe los elementos de la interfaz para tecnologías asistivas como los lectores de pantalla. Un usuario con visión puede ver que un `<div>` estilado actúa como botón, pero un lector de pantalla no puede saberlo a menos que se lo digamos:

```
<!-- El lector de pantalla no sabe que esto es un botón -->
<div onclick="submit()">Submit</div>

<!-- Ahora sí lo sabe -->
<div role="button" aria-label="Submit" onclick="submit()">Submit</div>

```

ARIA proporciona tres categorías de atributos:

- **Roles**: qué es el elemento. `role="button"`, `role="searchbox"`, `role="dialog"`, `role="navigation"`.
- **Properties**: lo describen. `aria-label="Search"`, `aria-labelledby="label-id"`, `aria-placeholder="Escribe aquí"`.
- **States**: condición actual. `aria-expanded="true"`, `aria-checked="false"`, `aria-disabled="true"`.

Los elementos HTML nativos tienen roles implícitos incorporados, por lo que normalmente no necesitamos añadir ARIA manualmente. Pero cuando los desarrolladores construyen componentes con `<div>` y `<span>`, ARIA se vuelve esencial tanto para la accesibilidad como para que nuestros tests funcionen.

### Aplicándolo a un Page Object Model.

Veamos cómo encaja todo esto en un **POM** real en TypeScript:

```
import { Locator, Page } from '@playwright/test';

export class HomePage {
  private readonly searchButton: Locator;
  private readonly searchBox: Locator;
  private readonly heading: Locator;

  constructor(private readonly page: Page) {
    this.searchButton = page.getByRole('button', { name: 'Search' });
    this.searchBox = page.getByRole('searchbox', { name: 'Search' });
    this.heading = page.getByRole('heading', { level: 1 });
  }

  // Devuelve un Locator — síncrono, no necesita async
  getHeading(): Locator {
    return this.heading;
  }

  // Realiza una acción — necesita async
  async clickSearch() {
    await this.searchButton.click();
  }

  // Realiza una acción — necesita async
  async searchFor(term: string) {
    await this.searchButton.click();
    await this.searchBox.fill(term);
  }
}

```

Y en el test:

```
// Aserción sobre un Locator — le pasamos el locator directamente a expect
await expect(homePage.getHeading()).toHaveText(/Playwright enables reliable/);

// Acción y luego aserción
await homePage.clickSearch();
await expect(page.getByRole('searchbox', { name: 'Search' })).toBeVisible();

```

Un detalle importante: `getHeading()` devuelve un `Locator` de forma **síncrona**, no necesita `async/await`. El `await` va en `expect().toHaveText()`, que es donde Playwright hace el polling del DOM y reintenta hasta que la condición se cumple o se agota el timeout.

### Checklist de depuración.

La próxima vez que `getByRole` no encuentre el elemento, repasa esta lista:

1. **¿Estoy usando el rol correcto?** Comprueba el rol ARIA, no el tag HTML. `<input type="search">` es `searchbox`, no `input`.
1. **¿Estoy usando el nombre correcto?** Abre DevTools → pestaña Accessibility → revisa el **Name computado**. No asumas que coincide con el placeholder o el texto visible.
1. **¿Hay un `aria-labelledby` sobreescribiendo el nombre?** Este es el gotcha más frecuente. `aria-labelledby` siempre gana sobre `aria-label`, `<label>` y `placeholder`.
1. **¿El elemento es visible?** Algunos elementos solo aparecen tras una interacción, como hacer click en un botón para abrir un modal o un desplegable.
1. **¿Necesito `exact: true`?** Si el substring matching está pillando el elemento equivocado, usa `exact: true` para forzar la coincidencia exacta.

### Conclusión.

- **`getByRole` no busca por placeholder ni por texto visible**: busca por el **nombre accesible computado**, que sigue una cadena de prioridad estricta.
- **`aria-labelledby` tiene la máxima prioridad** y sobreescribe todo lo demás, incluido el `placeholder`.
- **`input` no es un rol ARIA**: usa los roles implícitos como `textbox`, `searchbox`, `checkbox`, etc.
- La **pestaña Accessibility de Chrome DevTools** te muestra exactamente lo que ve Playwright: el nombre resuelto y qué atributos han ganado o sido descartados.
- **`getByRole` hace substring matching por defecto**: usa `exact: true` para coincidencias precisas.

* * *

Y hasta aquí nuestra entrada sobre los problemas más comunes con `getByRole` y los nombres accesibles en Playwright. Una vez que entiendes cómo funciona la cadena de resolución de ARIA, estos problemas dejan de ser un misterio. ¡Nos leemos en la siguiente entrada!
