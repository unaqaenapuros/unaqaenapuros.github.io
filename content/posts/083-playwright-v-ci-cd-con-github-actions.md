---
title: '083- Playwright (V): CI/CD con GitHub Actions.'
date: '2026-05-04T07:00:00+00:00'
url: /2026/05/04/083-playwright-v-ci-cd-con-github-actions/
image: /img/blog-images/old-post/2026/04/foto66.png
categories:
- automation
- buenas-prácticas
- ci
- docker
- playwright
- qa
tags:
- github-actions
- ia
author: estefafdez
---
¡Hola a todos!

En las entradas anteriores hemos aprendido a instalar Playwright, ejecutar tests, escribirlos y depurarlos. Pero para que una suite de pruebas aporte valor real al equipo, necesitamos que se ejecute automáticamente en cada cambio de código. En esta entrada veremos cómo integrar Playwright en un pipeline de **CI/CD con GitHub Actions**. ¡Empezamos!

### ¿Por qué integrar Playwright en CI/CD?

Tener los tests corriendo en local está muy bien, pero el verdadero valor de los tests automatizados se obtiene cuando se ejecutan automáticamente en cada pull request o cada push a la rama principal. Esto nos permite:

- Detectar **regresiones** de forma temprana, antes de que lleguen a producción.
- Dar **confianza** al equipo para mergear cambios con seguridad.
- Tener un **historial de ejecuciones** con los reportes de resultados.

### Configurando GitHub Actions.

Cuando instalamos Playwright con _`npm init playwright@latest`_, el asistente nos ofrece la opción de generar automáticamente un workflow de GitHub Actions. Si lo aceptamos, se crea el fichero `.github/workflows/playwright.yml` con la configuración lista para usar.

Este es el aspecto del workflow que nos genera por defecto:

```
name: Playwright Tests
on:
  push:
    branches: [ main, master ]
  pull_request:
    branches: [ main, master ]
jobs:
  test:
    timeout-minutes: 60
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v5
    - uses: actions/setup-node@v5
      with:
        node-version: lts/*
    - name: Install dependencies
      run: npm ci
    - name: Install Playwright Browsers
      run: npx playwright install --with-deps
    - name: Run Playwright tests
      run: npx playwright test
    - uses: actions/upload-artifact@v4
      if: ${{ !cancelled() }}
      with:
        name: playwright-report
        path: playwright-report/
        retention-days: 30

```

### ¿Qué hace este workflow paso a paso?

1. **`actions/checkout@v5`**: descarga el código del repositorio en el agente de CI.
1. **`actions/setup-node@v5`**: instala la versión LTS de Node.js.
1. **`npm ci`**: instala las dependencias del proyecto de forma limpia y reproducible.
1. **`npx playwright install --with-deps`**: descarga los binarios de los navegadores de Playwright junto con sus dependencias del sistema operativo. Este paso es imprescindible en entornos CI donde los navegadores no están preinstalados.
1. **`npx playwright test`**: ejecuta todos los tests.
1. **`actions/upload-artifact@v4`**: sube el reporte HTML generado como un artefacto del workflow, disponible para descarga desde la interfaz de GitHub. Se configura para que se suba incluso si los tests fallan (gracias al `if: ${{ !cancelled() }}`).

### Configuración de workers en CI.

En entornos de CI recomendamos configurar el número de **workers** (procesos que se ejecutan en paralelo) a `1`. Aunque esto hace que los tests tarden más, garantiza mayor estabilidad y reproducibilidad, ya que cada test tiene acceso a todos los recursos del sistema sin competir con otros.

```
import { defineConfig, devices } from '@playwright/test';

export default defineConfig({
  // Desactivamos la paralelización en CI
  workers: process.env.CI ? 1 : undefined,
});

```

Si tenemos un sistema de CI propio con mucha capacidad, podemos aumentar este valor. Para suites muy grandes, también podemos usar el **sharding**: distribuir los tests entre varios jobs de CI para reducir el tiempo total de ejecución.

### Visualizando los resultados en GitHub.

Una vez que el workflow se ejecuta, podemos ver los resultados directamente en la interfaz de GitHub:

1. Accedemos a la pestaña **Actions** del repositorio para ver la lista de ejecuciones.
1. Hacemos click en la ejecución que nos interesa para ver el detalle de todos los pasos.
1. Hacemos click en el step **Run Playwright tests** para ver los logs, incluyendo los errores, los mensajes de lo que se esperaba y lo que se recibió, y el _call log_ de las acciones.

#### Descargando el reporte HTML.

En la sección **Artifacts** de la ejecución encontraremos el archivo **`playwright-report`** listo para descargar. Es importante tener en cuenta que el reporte HTML necesita un servidor web para funcionar correctamente. Para abrirlo localmente:

1. Descargamos y extraemos el zip del reporte.
1. Desde la carpeta donde está el proyecto (con Playwright instalado), ejecutamos:

```
npx playwright show-report nombre-de-la-carpeta-extraida

```

Esto lanza un servidor local y podemos ver el reporte en el navegador con todas sus funcionalidades: filtros, detalle de cada test, trazas, capturas...

### Docker.

Playwright también ofrece una **imagen Docker oficial** con todos los navegadores y sus dependencias preinstaladas. Es una alternativa muy práctica para entornos CI que ya usan Docker, ya que evita tener que instalar los navegadores en cada ejecución.

Podemos usarla directamente en nuestro workflow de GitHub Actions:

```
jobs:
  test:
    runs-on: ubuntu-latest
    container:
      image: mcr.microsoft.com/playwright:v1.49.0-jammy
    steps:
      - uses: actions/checkout@v5
      - name: Install dependencies
        run: npm ci
      - name: Run tests
        run: npx playwright test

```

La imagen oficial de Playwright se puede consultar en la documentación oficial: [https://playwright.dev/docs/docker](https://playwright.dev/docs/docker)

* * *

Y hasta aquí nuestra entrada sobre cómo integrar Playwright con GitHub Actions. En la siguiente entrada hablaremos de algo muy interesante: los **Playwright Test Agents**, una funcionalidad que nos permite usar inteligencia artificial para generar y reparar tests de forma automática. ¡Nos leemos en la siguiente entrada!
