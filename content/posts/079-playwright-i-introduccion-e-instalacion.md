---
title: '079 – Playwright (I): Introducción e instalación.'
date: '2026-04-06T07:00:00+00:00'
url: /2026/04/06/079-playwright-i-introduccion-e-instalacion/
image: /img/blog-images/old-post/2026/03/foto62.png
categories:
- automation
- playwright
- qa
tags:
- azure
- ai
- microsoft
- testing
author: estefafdez
---
¡Hola a todos!

Aquí Estefanía a los mandos ( **_¡y no su IA!_**), una frase que estoy leyendo mucho últimamente y que tiene totalmente la razón en la época en la que vivimos. Antes de nada, disculpad por la laaaarga pausa en este blog, pero hay veces que la vida te consume y no te quedan ni fuerzas, ni energías, ni tiempo para poder dedicar un ratito a escribir, pero hemos vuelto, espero que con muchas cositas de aquí en adelante :)

Empezamos, ahora sí, con una nueva serie en el blog, y esta vez vamos a hablar de **Playwright**, uno de los frameworks de automatización de pruebas end-to-end más potentes y populares que existen actualmente (sí, me he migrado desde Cypress al lado oscuro de Microsoft!). En esta primera entrada haremos una introducción y veremos cómo instalarlo y configurarlo. ¡Comenzamos!

## **¿Qué es Playwright?**

{{< figure src="/img/blog-images/old-post/2026/03/pw.png?w=960" alt="" caption="" >}}

**Playwright** es un framework de código abierto desarrollado por **Microsoft** que permite realizar pruebas end-to-end (E2E) de aplicaciones web. Fue lanzado oficialmente el **31 de enero de 2020** _(¡menudo año y fecha eh!)_ y, curiosamente, su equipo principal tiene raíces de **Puppeteer**: los desarrolladores que trabajaron en esa herramienta en Google se unieron a Microsoft y canalizaron toda esa experiencia para crear algo mejor, superando las limitaciones de frameworks anteriores ( _si no puedes con el enemigo, únete_).

Su principal fortaleza es que permite automatizar navegadores de forma robusta y consistente, sin los problemas de flakiness (inestabilidad) que solemos encontrar en otros frameworks de automatización. A diferencia de **Selenium**, Playwright se conecta directamente a los navegadores a través de protocolos modernos como el **Chrome DevTools Protocol**, lo que lo hace más rápido y eficiente.

Algunas de sus características más destacadas son:

- **Multi-navegador**: soporta **Chromium** (Chrome, Edge), **Firefox** y **WebKit** (Safari) de forma nativa, permitiendo pruebas cross-browser reales.
- **Multi-lenguaje**: podemos escribir nuestros tests en TypeScript, JavaScript, Python, Java y .NET. En esta serie nos centraremos en **TypeScript**.
- **Autoespera inteligente**: Playwright espera automáticamente a que los elementos sean accionables antes de interactuar con ellos, lo que elimina la necesidad de añadir waits manuales.
- **Aislamiento de tests**: cada test se ejecuta en un contexto de navegador independiente (similar a una ventana de incógnito), creado en milisegundos, lo que garantiza que los tests no se interfieran entre sí y es mucho más rápido que levantar un navegador completo cada vez.
- **Paralelismo**: los tests se ejecutan en paralelo por defecto, lo que reduce considerablemente el tiempo de ejecución de nuestra suite.
- **Codegen**: una de las funcionalidades más curiosas es su generador de código, que graba las acciones del usuario en el navegador y genera automáticamente el código del test.
- **Emulación de dispositivos**: permite emular dispositivos móviles, geolocalización y permisos de usuario con gran facilidad.
- **Playwright Testing en Azure**: Microsoft ofrece integración con Azure para ejecutar pruebas a gran escala en la nube en múltiples navegadores simultáneamente (¡aviso, esto no es gratis!).

Si quieres saber más, tienes toda la documentación oficial en la web de Playwright: [https://playwright.dev/](https://playwright.dev/)

Y el repositorio oficial en GitHub: [https://github.com/microsoft/playwright](https://github.com/microsoft/playwright)

## **Requisitos del sistema.**

Antes de instalar Playwright, necesitamos asegurarnos de que nuestro entorno cumple con los siguientes requisitos:

- **Node.js**: versión 20.x, 22.x o 24.x (se recomienda usar la última versión LTS).
- **Sistema operativo**:
  - Windows 11 o superior, Windows Server 2019 o superior o Windows Subsystem for Linux (WSL).
  - macOS 14 (Ventura) o superior.
  - Debian 12/13 o Ubuntu 22.04/24.04 (arquitecturas x86-64 o arm64).

## **Instalando Playwright.**

La forma más sencilla de comenzar con Playwright es usando **npm**. El siguiente comando nos permite tanto inicializar un proyecto nuevo como añadir Playwright a un proyecto ya existente:

```
npm init playwright@latest
```

Al ejecutar este comando, el asistente de instalación nos irá haciendo preguntas: dónde queremos guardar los tests, si queremos añadir un workflow de GitHub Actions y qué navegadores queremos instalar. Una vez finalizado, Playwright descargará los binarios de los navegadores necesarios y creará los ficheros necesarios para empezar a escribir nuestros tests.

## **¿Qué se instala?**

Después de la instalación, nuestro proyecto tendrá la siguiente estructura:

```
playwright.config.ts   # Configuración de los tests
package.json
package-lock.json      # O yarn.lock / pnpm-lock.yaml
tests/
  example.spec.ts      # Un test de ejemplo mínimo
```

Veamos qué es cada cosa:

- **playwright.config.ts**: este fichero centraliza toda la configuración de Playwright: los navegadores en los que queremos ejecutar los tests ( _projects_), los timeouts, los reintentos en caso de fallo, los reportes y mucho más. Es el corazón de la configuración de nuestra suite.
- **tests/**: carpeta donde guardaremos nuestros tests. Playwright añade un test de ejemplo mínimo para que podamos ver cómo es la estructura de un test.

### **El fichero playwright.config.ts.**

El fichero de configuración es uno de los más importantes del proyecto. Aunque lo veremos con más detalle en próximas entradas, es importante saber que desde aquí podemos configurar:

- Los **navegadores** ( _projects_) en los que se ejecutarán los tests: Chromium, Firefox, WebKit.
- El **timeout** global de los tests.
- Los **reintentos** en caso de fallo, especialmente útiles en entornos CI.
- Los **reportes** que se generarán tras la ejecución.
- La **URL base** de la aplicación que vamos a probar.

En la siguiente entrada empezaremos a ejecutar nuestros primeros tests y veremos las diferentes formas que tenemos de lanzarlos y visualizar los resultados.

¡Nos leemos en la siguiente entrada!
