---
title: '093 – Playwright: Accesibilidad III – Tests inteligentes y checklist manual.'
date: '2026-09-21T09:30:00+02:00'
url: /2026/09/21/093-playwright-accesibilidad-iii-tests-inteligentes-y-checklist-manual/
image: /img/blog-images/new-posts/2026/09/foto82.png
categories:
- automation
- best-practices
- playwright
- qa
tags:
- accesibility
- testing
author: estefafdez
---
<!--
## Resumen para LinkedIn

Cerrar la mini-serie de accesibilidad con lo más práctico: tests de Playwright que van más allá del análisis genérico de axe. Contraste en hover, focus y modo oscuro, verificación del skip link, detección de texto de enlace ambiguo, aria-labels dinámicos en toggles y el ciclo completo de teclado en modales. Más un checklist de comprobaciones manuales que la automatización nunca podrá hacer sola.

👉 Enlace en comentarios.

#Playwright #QA #TestAutomation #Accesibilidad #UnaQAEnApuros
-->

¡Hola a todos!

Llegamos a la tercera y última entrega de la mini-serie sobre accesibilidad con Playwright. En las dos anteriores vimos por qué las herramientas automatizadas tienen una cobertura limitada y cuáles son las categorías concretas de problemas que se les escapan. Ahora viene la parte práctica: cómo escribir tests de Playwright que vayan más allá de un análisis genérico de axe, y un checklist de comprobaciones manuales que siempre deberían acompañar a la suite automatizada. ¡Empezamos!

### Tests de Playwright que van más allá del informe de Lighthouse.

La respuesta a las limitaciones que vimos en la entrega anterior no es abandonar los tests automatizados: es escribir tests que vayan más lejos que un `AxeBuilder` por defecto. Un análisis estándar de axe es el suelo mínimo, no el techo. Los patrones que veremos a continuación cubren exactamente los defectos que ese análisis no detecta.

### El análisis base de axe.

Antes de nada, el análisis básico. Este es el punto de partida del que depende todo lo demás:

```typescript
// a11y.spec.ts
import { test, expect } from '@playwright/test';
import AxeBuilder from '@axe-core/playwright';

test('la página principal no tiene violaciones de accesibilidad', async ({ page }) => {
  await page.goto('/');
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});
```

### Contraste en estado hover.

Un análisis estándar no detecta problemas de contraste que solo aparecen al hacer hover. La solución es activar el estado primero y luego analizar:

```typescript
test('los botones de acción no tienen problemas de contraste al hacer hover', async ({ page }) => {
  await page.goto('/');
  // Activamos el estado hover sobre el botón principal de llamada a la acción
  await page.getByRole('button', { name: 'Suscribirse' }).hover();
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});
```

### Contraste en estado focus.

El mismo principio: activamos el foco antes del análisis para que axe evalúe los estilos del anillo de focus:

```typescript
test('los campos de formulario no tienen problemas de contraste al recibir el foco', async ({ page }) => {
  await page.goto('/contacto');
  // Colocamos el foco en el campo de email
  await page.getByRole('textbox', { name: 'Correo electrónico' }).focus();
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});
```

### Contraste en modo oscuro y modo claro.

Un análisis en modo claro no detecta fallos de contraste que solo ocurren en modo oscuro. Necesitamos ejecutar ambas comprobaciones por separado:

```typescript
test('no hay problemas de contraste en modo oscuro', async ({ page }) => {
  await page.emulateMedia({ colorScheme: 'dark' });
  await page.goto('/');
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});

test('no hay problemas de contraste en modo claro', async ({ page }) => {
  await page.emulateMedia({ colorScheme: 'light' });
  await page.goto('/');
  const results = await new AxeBuilder({ page }).analyze();
  expect(results.violations).toEqual([]);
});
```

### El enlace de saltar al contenido.

Verificamos tres cosas: que existe, que es el primer elemento alcanzable por teclado y que realmente lleva al contenido principal cuando se activa:

```typescript
test('el primer elemento enfocable es el enlace de saltar al contenido', async ({ page }) => {
  await page.goto('/');
  await page.keyboard.press('Tab');

  const focusedElement = page.locator(':focus');
  await expect(focusedElement).toHaveAttribute('href', '#contenido-principal');
  await expect(focusedElement).toHaveText('Ir al contenido principal');

  // Al activarlo, la URL debe incluir el ancla del contenido principal
  await page.keyboard.press('Enter');
  await expect(page).toHaveURL(/#contenido-principal$/);
});
```

### Labels únicos en landmarks de navegación.

Verificamos que no hay landmarks de navegación duplicados ni sin etiquetar. Dos `<nav>` sin `aria-label` son indistinguibles para los usuarios de lector de pantalla:

```typescript
test('todos los elementos de navegación tienen aria-label único', async ({ page }) => {
  await page.goto('/');
  const navElements = await page.getByRole('navigation').all();

  const labels = await Promise.all(
    navElements.map((nav) => nav.getAttribute('aria-label'))
  );

  // Cada nav debe tener label
  labels.forEach((label, index) => {
    expect(label, `El elemento de navegación ${index + 1} no tiene aria-label`).not.toBeNull();
  });

  // Todos los labels deben ser únicos
  const uniqueLabels = new Set(labels);
  expect(uniqueLabels.size).toBe(labels.length);
});
```

### Texto de enlace ambiguo.

Detectamos los textos de enlace que pasan axe pero son inútiles cuando se leen fuera de contexto:

```typescript
test('ningún enlace tiene texto ambiguo', async ({ page }) => {
  await page.goto('/');
  const ambiguousTexts = ['ver más', 'saber más', 'haz clic aquí', 'aquí', 'continuar', 'más info', 'leer más'];
  const links = await page.getByRole('link').all();

  for (const link of links) {
    const text = (await link.innerText()).toLowerCase().trim();
    expect(
      ambiguousTexts,
      `Texto de enlace ambiguo encontrado: "${text}"`
    ).not.toContain(text);
  }
});
```

### `aria-label` dinámico en controles con estado.

Verificamos que el `aria-label` de un control de tipo toggle refleja correctamente el estado actual antes y después de la interacción. Una etiqueta que no cambia es un bug de accesibilidad invisible para los escáneres:

```typescript
// modo-oscuro-toggle.spec.ts
test('el toggle de tema actualiza su aria-label al cambiar el estado', async ({ page }) => {
  // Empezamos en modo claro — el botón debe ofrecer cambiar a modo oscuro
  await page.emulateMedia({ colorScheme: 'light' });
  await page.goto('/');

  const toggle = page.getByRole('button', { name: /modo/i });
  await expect(toggle).toHaveAttribute('aria-label', 'Cambiar a modo oscuro');

  // Tras hacer clic, el label debe reflejar el nuevo estado
  await toggle.click();
  await expect(toggle).toHaveAttribute('aria-label', 'Cambiar a modo claro');
});
```

### Alt text genérico en imágenes.

Detectamos alt text que se añadió para silenciar un linter pero no comunica nada útil a los usuarios de lector de pantalla:

```typescript
test('ninguna imagen tiene alt text genérico', async ({ page }) => {
  await page.goto('/');
  const genericAlts = ['imagen', 'foto', 'fotografía', 'icono', 'banner', 'picture', 'img', 'thumbnail', 'photo'];
  const images = await page.locator('img[alt]').all();

  for (const image of images) {
    const alt = (await image.getAttribute('alt') ?? '').toLowerCase().trim();
    // alt="" es correcto e intencional para imágenes decorativas — no lo marcamos
    if (alt === '') continue;
    expect(
      genericAlts,
      `Alt text genérico encontrado: "${alt}"`
    ).not.toContain(alt);
  }
});
```

### Accesibilidad de teclado en modales.

Verificamos el ciclo completo: apertura, trampa de foco durante la navegación interna, cierre con Escape y retorno del foco al elemento disparador:

```typescript
// confirmacion-borrado.spec.ts
test('el diálogo de confirmación atrapa el foco y se cierra con Escape', async ({ page }) => {
  await page.goto('/mis-documentos');

  const deleteButton = page.getByRole('button', { name: 'Eliminar documento' });
  await deleteButton.click();

  const dialog = page.getByRole('dialog');
  await expect(dialog).toBeVisible();

  // Tabulamos varias veces — el foco debe permanecer dentro del diálogo
  for (let i = 0; i < 8; i++) {
    await page.keyboard.press('Tab');
    const insideDialog = await page.evaluate(() =>
      document.activeElement?.closest('[role="dialog"]') !== null
    );
    expect(insideDialog).toBe(true);
  }

  // Escape debe cerrar el diálogo
  await page.keyboard.press('Escape');
  await expect(dialog).not.toBeVisible();
});

test('el foco vuelve al botón disparador al cerrar el diálogo', async ({ page }) => {
  await page.goto('/mis-documentos');
  const deleteButton = page.getByRole('button', { name: 'Eliminar documento' });
  await deleteButton.click();

  await page.keyboard.press('Escape');
  await expect(deleteButton).toBeFocused();
});
```

### Activación de acordeón por teclado.

Verificamos que tanto Enter como Espacio activan correctamente los controles de tipo toggle, que es lo que los usuarios de teclado esperan:

```typescript
test('el acordeón de preguntas frecuentes responde a Enter y Espacio', async ({ page }) => {
  await page.goto('/ayuda');
  const toggleButton = page.getByRole('button', { name: '¿Cómo puedo cancelar mi suscripción?' });
  const content = page.getByRole('region', { name: '¿Cómo puedo cancelar mi suscripción?' });

  await expect(toggleButton).toHaveAttribute('aria-expanded', 'false');
  await expect(content).not.toBeVisible();

  // Enter debe expandir el acordeón
  await toggleButton.press('Enter');
  await expect(toggleButton).toHaveAttribute('aria-expanded', 'true');
  await expect(content).toBeVisible();

  // Espacio debe colapsar el acordeón
  await toggleButton.press('Space');
  await expect(toggleButton).toHaveAttribute('aria-expanded', 'false');
  await expect(content).not.toBeVisible();
});
```

### Comprobaciones manuales que la automatización no puede hacer.

Algunos defectos de accesibilidad no se pueden detectar solo con automatización. Si un label es _significativo_ o meramente presente, si el orden del foco tiene sentido lógico para un usuario real, si un lector de pantalla anuncia el contenido de una manera comprensible... todo esto requiere un juicio humano.

Usa este checklist como parte de tu auditoría de accesibilidad periódica:

  * [ ] Navega por la página completa solo con el teclado — ¿tiene sentido el orden del foco?
  * [ ] ¿El enlace de saltar al contenido es el primer elemento enfocable?
  * [ ] ¿Todas las regiones landmark están etiquetadas y son distintas entre sí?
  * [ ] ¿Todos los enlaces tienen sentido al leerlos en voz alta fuera de contexto?
  * [ ] ¿Los controles dinámicos actualizan su nombre accesible cuando cambia el estado?
  * [ ] ¿Las referencias de `aria-labelledby` apuntan a texto visible y preciso?
  * [ ] Prueba con un lector de pantalla real: **NVDA** (gratuito, Windows), **JAWS** o **VoiceOver** (integrado en macOS e iOS).
  * [ ] Navega usando landmarks, encabezados y enlaces — no solo de forma lineal con Tab.
  * [ ] Rellena y envía cada formulario provocando errores: ¿los mensajes son suficientemente descriptivos para corregirlos?
  * [ ] Comprueba el contraste en modo oscuro y claro, y en los estados de hover y focus.

### Conclusión.

  * Un análisis básico de **`AxeBuilder`** es el punto de partida, no el destino de la estrategia de accesibilidad.
  * Activar los **estados de hover, focus y modo oscuro** antes del análisis captura fallos de contraste que un análisis estático por defecto no detecta.
  * Playwright puede verificar que el **enlace de saltar al contenido** existe, es el primero en ser enfocado y funciona correctamente.
  * Podemos detectar **texto de enlace ambiguo** y **alt text genérico** con comprobaciones programáticas sobre el contenido de los elementos.
  * Los flujos completos de **teclado en modales y acordeones** son exactamente el tipo de test que Playwright ejecuta mejor y que los escáneres estáticos no pueden simular.
  * La automatización y la **revisión manual con tecnología asistiva real** son complementarias: ninguna sustituye a la otra.

* * *

Y hasta aquí nuestra mini-serie sobre accesibilidad con Playwright. Hemos cubierto la brecha de cobertura de las herramientas automatizadas, las categorías de problemas que se les escapan y cómo escribir tests más inteligentes para cubrir parte de esa brecha. La accesibilidad no es un informe verde: es una experiencia que funciona para todas las personas. ¡Nos leemos en la siguiente entrada!
