---
title: '092 – Playwright: Accesibilidad II – Lo que axe y Lighthouse no pueden detectar.'
date: '2026-09-07T09:30:00+02:00'
url: /2026/09/07/092-playwright-accesibilidad-ii-lo-que-axe-y-lighthouse-no-pueden-detectar/
image: /img/blog-images/new-posts/2026/09/foto81.png
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
¡Hola a todos!

Continuamos con la serie sobre accesibilidad en Playwright. En la entrada anterior vimos por qué las herramientas automatizadas tienen una cobertura limitada: pueden leer el DOM, pero no pueden entender el contexto. Hoy vamos a ver en detalle las categorías concretas de problemas que se les escapan sistemáticamente. Cada una viene con su causa, un ejemplo y cómo deberíamos corregirla. ¡Empezamos!

{{< figure src="/img/blog-images/new-posts/2026/09/gemini%5Fgenerated%5Fimage%5F9ooets9ooets9ooe.png?w=1024" alt="" caption="" >}}

### 1\. Texto de enlace ambiguo.

Textos como _"Ver más"_, _"Saber más"_, _"Haz clic aquí"_ o _"Continuar"_ pasan los checks de axe sin ningún problema. No hay nada estructuralmente incorrecto en ellos: son elementos `<a>` válidos con contenido de texto.

El problema es el contexto. Los usuarios de lectores de pantalla navegan con frecuencia entre los enlaces de una página de forma aislada, sin el párrafo circundante que aporta el significado. Escuchar "Ver más" cuatro veces seguidas no dice nada sobre adónde lleva cada enlace.

Las herramientas automatizadas pueden verificar si el texto del enlace **existe**, pero no si es **significativo**. Una página llena de "Ver más" pasa axe igual de limpiamente que una con textos completamente descriptivos.

**Cómo corregirlo:** Escribe el texto del enlace de forma que tenga sentido fuera de contexto: _"Ver más sobre pruebas de accesibilidad"_ en lugar de _"Ver más"_. Cuando el diseño no permite textos largos visibles, usa `aria-label` para aportar el contexto completo:

```
<a href="/accesibilidad" aria-label="Ver más sobre pruebas de accesibilidad">Ver más</a>

```

### 2\. Ausencia del enlace de saltar al contenido.

Los elementos landmark como `<main>` y `<nav>` satisfacen la comprobación de _bypass block_ de axe (WCAG 2.4.1). La regla se cumple técnicamente porque existe un mecanismo para saltar contenido repetido.

Pero los usuarios que navegan **solo con teclado** y no usan lector de pantalla siguen teniendo que tabular por cada elemento del encabezado antes de llegar al contenido principal. Los landmarks ayudan a los usuarios de lectores de pantalla a saltar entre regiones; no ayudan a un usuario de teclado a saltarse un menú de navegación con 12 elementos en cada carga de página.

Un enlace de saltar al contenido — un ancla oculta visualmente que es el primer elemento enfocable y que lleva hasta `#contenido-principal` — sirve a ambos grupos. Los landmarks solos no.

**Cómo corregirlo:** Añade un enlace de saltar como primer elemento enfocable en todas las páginas:

```
<a href="#contenido-principal" class="sr-only focus:not-sr-only">
  Ir al contenido principal
</a>

```

### 3\. `aria-labelledby` vs `aria-label`: ambos pasan, uno es mejor.

Tanto `aria-labelledby` como `aria-label` satisfacen los checks automatizados por igual. Las herramientas verifican la presencia y la sintaxis válida, pero no evalúan cuál es más apropiado para el contexto específico.

`aria-label` define una cadena que existe solo en el árbol de accesibilidad, invisible visualmente. Esto crea dos problemas:

- Los usuarios con visión que también usan tecnología asistiva pueden recibir información diferente de lo que ven en pantalla y de lo que les anuncia el lector de pantalla.
- Las herramientas de traducción automática suelen ignorar los atributos `aria-label`, dejando a los usuarios en otros idiomas con nombres no traducidos.

Cuando ya existe un texto visible en la página que puede servir de etiqueta, `aria-labelledby` es casi siempre la opción correcta: reutiliza el texto visible, por lo que ambas representaciones se mantienen sincronizadas automáticamente.

```
<!-- Incorrecto: hay un título visible, usar aria-labelledby -->
<section aria-label="Artículos recientes">
  <h2 id="titulo-articulos">Artículos recientes</h2>
  ...
</section>

<!-- Correcto -->
<section aria-labelledby="titulo-articulos">
  <h2 id="titulo-articulos">Artículos recientes</h2>
  ...
</section>

<!-- aria-label sí es correcto cuando no existe texto visible -->
<button aria-label="Cerrar panel lateral">
  <svg aria-hidden="true">...</svg>
</button>

```

**Cómo corregirlo:** Cuando existe un texto visible que puede actuar como etiqueta, usa `aria-labelledby`. Reserva `aria-label` para los casos donde no existe ningún texto visible.

### 4\. Labels ARIA estáticos en controles con estado.

Un toggle de notificaciones con `aria-label="Activar notificaciones"` pasa los checks automatizados independientemente del estado actual del control. La etiqueta está presente y bien formada, pero si las notificaciones ya están activas, la etiqueta es factualmente incorrecta: debería decir _"Desactivar notificaciones"_.

Las herramientas automatizadas comprueban la **presencia** y el **formato**, no la exactitud ni si el valor es correcto a lo largo del tiempo. Una etiqueta estática en un control con estado es completamente invisible para un escáner.

**Cómo corregirlo:** Vincula `aria-label` dinámicamente al estado actual del control:

```
<!-- En Vue -->
<button :aria-label="notificationsActive ? 'Desactivar notificaciones' : 'Activar notificaciones'">
  <svg aria-hidden="true">...</svg>
</button>

```

```
// En React
<button aria-label={isDarkMode ? 'Cambiar a modo claro' : 'Cambiar a modo oscuro'}>
  <svg aria-hidden="true" />
</button>

```

### 5\. Alt text y labels ARIA de baja calidad.

axe-core valida la presencia y el formato. No valida la calidad.

`aria-label="nav"`, `aria-label="sección 1"` y `alt="foto de producto"` pasan los checks. También pasa `role="button"` sobre un `<div>` que no es enfocable por teclado. Un usuario de lector de pantalla que escucha "foto de producto" o "sección 1" no está mejor informado que si no existiera el atributo — en algunos casos está peor, porque la presencia del atributo indica al desarrollador que el problema está resuelto.

Lo mismo aplica al texto alternativo de imágenes. El texto correcto depende del contexto y la función de la imagen, algo que ninguna herramienta puede evaluar:

```
<!-- Logo como imagen independiente — identificar la marca -->
<img src="logo.svg" alt="Empresa XYZ" />

<!-- Logo como enlace — describir el destino, no la imagen -->
<a href="/">
  <img src="logo.svg" alt="Empresa XYZ – Página de inicio" />
</a>

<!-- Imagen de un artículo del blog como enlace -->
<a href="/articulo">
  <img src="thumbnail.jpg" alt="Guía de fixtures en Playwright – leer el artículo" />
</a>

```

Ambos primeros ejemplos pasan axe. Solo uno comunica lo correcto en su contexto.

**Cómo corregirlo:** Antes de añadir cualquier atributo ARIA o `alt`, pregúntate: ¿comunica algo significativo para alguien que no puede ver el contexto visual? Si la respuesta es no, el atributo no es una solución, es ruido.

### 6\. Regresiones que los escáneres no detectan (y a veces provocan).

Este es uno de los más peligrosos. Imagina que un desarrollador aplica la corrección correcta para un problema de accesibilidad, y más tarde otro desarrollador, sin conocer las mejores prácticas, "arregla" lo que interpreta como un error.

Dos casos que ocurren con frecuencia:

- `alt=""` es el atributo correcto para **imágenes decorativas**. Indica explícitamente a los lectores de pantalla que ignoren el elemento. Un linter que marca los `alt` vacíos como error, o un desarrollador que los ve y los cambia a `alt="imagen decorativa"`, introduce una regresión: ahora los lectores de pantalla anuncian "imagen decorativa" en cada elemento decorativo de la página — ruido que antes no existía.
- `aria-hidden="true"` en iconos dentro de botones con etiqueta de texto visible es correcto. Quitarlo y reemplazarlo con `aria-label="icono"` pasa los checks, pero contamina el cálculo del nombre accesible y puede anular la etiqueta real del botón.

En ambos casos, el estado original era más accesible que el estado "corregido". Y los checks automatizados no lo detectan porque el resultado técnico sigue siendo válido.

**Cómo corregirlo:** Documenta las decisiones intencionales en el código para que el equipo no las revierta:

```
<!-- alt="" intencional: separador decorativo, los lectores de pantalla deben ignorarlo -->
<img src="wave-separator.svg" alt="" />

<!-- aria-hidden intencional: el botón tiene etiqueta de texto visible -->
<button>
  <svg aria-hidden="true">...</svg>
  Guardar cambios
</button>

```

### 7\. Limitaciones en la detección de contraste de color.

Lighthouse y axe detectan problemas de contraste en texto estático sobre fondo sólido. Es un avance real, pero quedan brechas importantes:

- **Texto sobre imágenes o gradientes**: axe puede no reportar correctamente los problemas de contraste cuando el fondo no es un color sólido.
- **Fondos semitransparentes**: el color calculado puede no ser preciso.
- **Estados de hover y focus**: el análisis evalúa el elemento tal como existe en el momento de la ejecución. Un contraste insuficiente en el anillo de focus o en los estilos de hover es invisible a menos que ese estado esté activo cuando se ejecuta el análisis.
- **Modo oscuro**: un análisis en modo claro no detecta fallos de contraste en modo oscuro, y viceversa.

Para gradientes, una aproximación manual es comprobar el contraste contra cada extremo del gradiente. Por ejemplo, para este CSS:

```
.card-header {
  background: linear-gradient(to bottom, #1a1a2e, #ffffff);
  color: #6b7280;
}

```

Habría que verificar el ratio de contraste de `#6b7280` sobre `#1a1a2e` y también sobre `#ffffff`. Si pasa en ambos extremos, pasa en todo el gradiente. **Cómo corregirlo:** Para los estados de hover, focus y modo oscuro, necesitamos activar esos estados antes de lanzar el análisis automatizado. Veremos cómo hacerlo con Playwright en la siguiente entrega.

### 8\. Recomendaciones de landmarks que rompen HTML heredado.

Lighthouse marca la ausencia de regiones landmark como violaciones de accesibilidad. En una base de código HTML5 moderna, la recomendación es directa: añade `<main>`, `<nav>`, `<header>`.

En doctypes pre-HTML5 (XHTML strict, HTML 4.01 strict), esos elementos son markup inválido. Seguir la recomendación sin entender la restricción del doctype produce markup que simultáneamente es inválido y aparentemente satisface la regla de accesibilidad.

Las herramientas automatizadas evalúan contra un contexto HTML5 idealizado. No tienen conciencia de las restricciones del doctype ni pueden distinguir entre "landmark ausente" y "rol ARIA landmark correctamente implementado para una base de código heredada".

**Cómo corregirlo:** En contextos pre-HTML5, usa roles ARIA landmark sobre elementos `<div>`:

```
<div role="main">...</div>
<div role="navigation" aria-label="Navegación principal">...</div>
<div role="banner">...</div>

```

En bases de código HTML5, usa los elementos nativos directamente — ya llevan el rol landmark implícito y no necesitan el atributo `role` explícito.

### 9\. Accesibilidad en formularios: etiquetas, instrucciones y mensajes de error.

Las herramientas automatizadas detectan con fiabilidad un `<label>` ausente o un campo sin nombre accesible. Lo que no pueden evaluar es si la etiqueta, la instrucción o el mensaje de error son **realmente útiles**.

Un `<label>Campo 1</label>` asociado a un input pasa todos los checks. También pasa `<label>Dirección de correo electrónico</label>`. La herramienta ve una etiqueta: no la lee.

La misma brecha aparece en todo el formulario:

- **Placeholder como única instrucción**: el texto del placeholder desaparece cuando el usuario empieza a escribir. Las herramientas no detectan este patrón como problema.
- **Mensajes de error vagos**: "Entrada no válida" y "El teléfono debe tener 9 dígitos y empezar por 6 o 7" pasan los checks. Solo uno ayuda al usuario a corregir el error.
- **Proximidad del error**: los errores que aparecen solo al inicio de la página satisfacen los requisitos técnicos de WCAG pero son desorientadores para usuarios de teclado y lector de pantalla en formularios largos.
- **Tiempo de anuncio del error**: si el error se surfacea con `aria-live` o `aria-describedby` de una manera que los lectores de pantalla realmente reciban requiere prueba con tecnología asistiva real, no solo un análisis del DOM.
- **Indicadores de campo obligatorio**: un asterisco rojo es una convención visual. Sin un equivalente de texto o `aria-required="true"`, los usuarios de lector de pantalla no saben que un campo es obligatorio hasta que el envío falla.

**Cómo corregirlo:** Prueba cada formulario manualmente con teclado y un lector de pantalla real. Provoca los estados de error deliberadamente — envía con campos vacíos, introduce formatos incorrectos — y verifica que el mensaje anunciado explica exactamente qué salió mal y cómo corregirlo. Confirma que el placeholder está acompañado siempre de una etiqueta visible persistente.

### 10\. Accesibilidad de teclado: modales y componentes interactivos.

Las herramientas automatizadas pueden verificar que un modal tiene `role="dialog"` y un nombre accesible, o que un acordeón tiene `aria-expanded`. Lo que no pueden hacer es interactuar con esos componentes como lo haría un usuario de teclado, para verificar que se comportan correctamente durante la navegación.

Esta es una limitación estructural del análisis estático del DOM. Un escáner evalúa la página tal como carga: no hace clic en botones, no abre diálogos, no pulsa teclas. Puede confirmar que un modal tiene los atributos ARIA correctos en el markup, pero no puede verificar qué ocurre cuando un usuario lo abre realmente.

Los fallos más comunes en esta área:

- **El foco no se mueve al modal al abrirse**: el diálogo aparece visualmente pero el foco de teclado se queda fuera.
- **El foco no queda atrapado dentro del modal**: Tab debería ciclar dentro del diálogo; si escapa a la página de fondo, el usuario de teclado pierde su posición sin darse cuenta.
- **Escape no cierra el modal**: los usuarios de teclado esperan que Escape cierre un diálogo.
- **El foco no vuelve al elemento disparador al cerrar**: cuando el modal se cierra, el foco debería regresar al elemento que lo abrió.
- **Activación de acordeones con teclado**: un acordeón que solo responde a clics de ratón no es accesible por teclado. Enter y Espacio deberían activar los controles de tipo toggle.
- **Contenido dinámico no anunciado**: el contenido que aparece tras una interacción (resultados de búsqueda, validación inline, notificaciones) necesita regiones `aria-live` o gestión explícita del foco para llegar a los usuarios de lector de pantalla.

**Cómo corregirlo:** Prueba cada componente interactivo solo con teclado — sin ratón. Abre modales con Enter, navega dentro con Tab y Shift+Tab, ciérralos con Escape, y verifica que el foco vuelve al disparador. Activa los controles de expandir/colapsar con Enter y Espacio. Estos flujos de teclado son exactamente los que luego podemos automatizar con Playwright, como veremos en la siguiente entrega.

### Conclusión.

- Las herramientas no pueden evaluar si el **texto de enlace** o el **alt text** son significativos, solo si existen y tienen el formato correcto.
- El **enlace de saltar al contenido** es necesario aunque los landmarks estén presentes, porque ayuda a usuarios de teclado que no usan lector de pantalla.
- Tanto `aria-labelledby` como `aria-label` pasan los checks, pero **`aria-labelledby` es preferible** cuando ya existe texto visible en la página.
- Los **labels ARIA estáticos** en controles con estado siempre serán un punto ciego para los escáneres.
- Los "arreglos" incorrectos pueden introducir **regresiones que pasan los checks** pero empeoran la experiencia real — documentar la intención en el código protege de esto.
- Las limitaciones de **contraste**, **formularios** y **navegación por teclado** requieren comprobaciones más específicas y prueba manual con tecnología asistiva real.

* * *

Y hasta aquí esta segunda entrega sobre accesibilidad con Playwright. En la siguiente y última parte veremos cómo escribir tests de Playwright más inteligentes para cubrir parte de estas brechas, y un checklist de comprobaciones manuales que siempre deberían acompañar a la suite automatizada. ¡Nos leemos en la siguiente entrada!
