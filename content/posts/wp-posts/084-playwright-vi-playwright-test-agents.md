---
title: '084 – Playwright (VI): Playwright Test Agents'
date: '2026-05-18T07:00:00+00:00'
url: /2026/05/18/084-playwright-vi-playwright-test-agents/
image: /img/blog-images/wp-posts/2026/04/foto67.png
categories:
- automation
- best-practices
- ci
- code-quality
- profiles
- performance
- playwright
- qa
tags:
- generator
- healer
- ai
- planner
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a hablar de una de las funcionalidades más novedosas de Playwright: los **Playwright Test Agents**. Se trata de agentes basados en inteligencia artificial (nuestra nueva mejor amiga, la IA), que nos ayudan a generar y mantener tests de forma automática. ¿Suena bien, verdad? ¡Empezamos!

### ¿Qué son los Playwright Test Agents?

Playwright incorpora de forma nativa tres agentes de IA para la generación automática de tests:

- **🎭 Planner**: explora la aplicación y genera un plan de tests en formato Markdown.
- **🎭 Generator**: transforma el plan de tests en ficheros de tests de Playwright ejecutables.
- **🎭 Healer**: ejecuta los tests y repara automáticamente los que fallen.

Estos tres agentes pueden usarse de forma independiente, de forma secuencial, o encadenados en un **bucle agéntico** completo. Usados de forma secuencial, nos permiten generar y mejorar la cobertura de tests para nuestra aplicación con muy poco esfuerzo manual.

### Primeros pasos: inicializando los agentes.

Para añadir los Playwright Test Agents a nuestro proyecto, ejecutamos el siguiente comando en la carpeta raíz del proyecto:

```
npx playwright init-agents --loop=vscode

```

Este comando genera las definiciones de los agentes en nuestro proyecto. Una vez generadas, podemos usar nuestra herramienta de IA favorita (VS Code Copilot, Cursor, Claude Code...) para invocar a los agentes y empezar a generar tests.

### 🎭 El agente Planner.

El **Planner** es el punto de partida del proceso. Su función es explorar la aplicación y generar un **plan de tests** en formato Markdown: un documento legible por humanos que describe los escenarios y flujos de usuario que hay que probar.

#### ¿Qué necesita el Planner?

- Una **petición clara** de lo que queremos planificar (por ejemplo: "Genera un plan de tests para el flujo de checkout como usuario invitado").
- Un **seed test**: un test mínimo que configura el entorno necesario para interactuar con la aplicación (global setup, fixtures, hooks...). El Planner ejecuta este seed test para inicializar correctamente el entorno antes de explorar.
- Opcionalmente, un **documento de requisitos** (PRD) para dar más contexto al agente.

El seed test actúa como punto de entrada y como ejemplo del estilo en el que se generarán los tests. Un seed test típico tiene este aspecto:

```
import { test, expect } from './fixtures';

test('seed', async ({ page }) => {
  // Este test usa fixtures personalizados desde ./fixtures
  // que configuran el entorno necesario (login, datos de prueba...)
});

```

#### ¿Qué genera el Planner?

El Planner genera un fichero Markdown bajo la carpeta `specs/` con el plan de tests. Este plan es legible, preciso y suficientemente detallado para que el Generator pueda transformarlo en tests ejecutables. Un ejemplo de plan generado podría ser:

```
# TodoMVC - Plan de tests de operaciones básicas

## Escenario 1: Añadir una tarea nueva
### 1.1 Añadir una tarea válida
**Pasos:**
1. Hacer click en el campo "What needs to be done?"
1. Escribir "Comprar pan"
1. Pulsar Enter

**Resultados esperados:**
- La tarea aparece en la lista con el checkbox desmarcado
- El contador muestra "1 item left"
- El campo de entrada se vacía

```

### 🎭 El agente Generator.

El **Generator** toma el plan de tests generado por el Planner (o escrito manualmente) y lo convierte en **tests de Playwright ejecutables**. Durante el proceso, verifica los locators y las aserciones en tiempo real interactuando con la aplicación.

#### ¿Qué necesita el Generator?

- El plan de tests en Markdown generado por el Planner (bajo `specs/`).

Al invocar al Generator, le indicamos el plan que queremos transformar. El Generator lee el plan, interactúa con la aplicación para verificar que los locators son correctos y genera los ficheros de tests bajo la carpeta `tests/`.

Los tests generados pueden contener pequeños errores iniciales que el Healer se encargará de corregir automáticamente.

### 🎭 El agente Healer.

El **Healer** es el agente encargado de mantener los tests en buen estado. Cuando un test falla, el Healer:

1. **Reproduce** los pasos fallidos.
1. **Inspecciona** la interfaz de usuario actual para localizar elementos equivalentes o flujos alternativos.
1. **Propone un parche**: por ejemplo, actualizar un locator que haya cambiado, añadir una espera o corregir un dato de prueba.
1. **Re-ejecuta** el test hasta que pasa o hasta que los "guardarraíles" ( _guardrails_) detienen el bucle.

Si el Healer determina que la funcionalidad está rota (no es un problema del test, sino de la aplicación), marca el test como _skipped_ en lugar de intentar arreglarlo indefinidamente.

### La estructura de ficheros resultante.

Los agentes siguen una estructura de ficheros simple y facil de leer:

```
repo/
  .github/              # Definiciones de los agentes
  specs/                # Planes de tests en Markdown (legibles por humanos)
    basic-operations.md
  tests/                # Tests de Playwright generados
    seed.spec.ts        # Seed test para inicializar el entorno
    create/
      add-valid-todo.spec.ts
  playwright.config.ts

```

Esta estructura separa claramente los **planes** (legibles y revisables por el equipo) de los **tests ejecutables** (generados automáticamente), lo que facilita las revisiones de código y mantiene el repositorio fácil de leer y mantener.

### ¿Cuándo usar los Playwright Test Agents?

Los Test Agents son especialmente útiles en estos escenarios:

- **Proyectos nuevos**: cuando necesitamos cobertura de tests rápida para una aplicación nueva.
- **Aplicaciones sin tests**: para dar el primer paso en la automatización sin necesidad de un gran esfuerzo inicial.
- **Mantenimiento de tests**: cuando los cambios en la UI rompen muchos tests, el Healer puede repararlos automáticamente (no os penséis que es magia, es repetición).

Es importante tener en cuenta que los tests generados deben **revisarse siempre** antes de considerarlos definitivos. Los agentes son una herramienta de ayuda, no un sustituto del criterio del tester.

* * *

Y hasta aquí nuestra entrada sobre los Playwright Test Agents. En la siguiente y última entrada de la serie hablaremos del **Playwright MCP** y el **Playwright CLI**, dos herramientas que permiten integrar Playwright con agentes de IA de forma muy potente. ¡Nos leemos en la siguiente entrada!
