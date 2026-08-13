---
title: '085 – Playwright (VII): Playwright MCP y CLI.'
date: '2026-06-01T07:00:00+00:00'
url: /2026/06/01/085-playwright-vii-playwright-mcp-y-cli/
image: /img/blog-images/old-post/2026/04/foto74.png
categories:
- automation
- buenas-prácticas
- ci
- code-quality
- playwright
- qa
tags:
- agents
- ia
- mcp
author: estefafdez
---
¡Hola a todos!

Llegamos a la última entrada de nuestra serie sobre Playwright intensivo. En esta ocasión vamos a hablar de dos herramientas muy interesantes que permiten integrar Playwright con agentes de IA: el **Playwright MCP** y el **Playwright CLI**. ¡Empezamos!

### ¿Qué es el Playwright MCP?

El **Playwright MCP** ( _Model Context Protocol_) es un servidor MCP desarrollado por Microsoft que proporciona capacidades de automatización de navegadores usando Playwright. Está disponible en [https://github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp).

Lo que hace especial a este servidor MCP es que **no usa capturas de pantalla** para que el modelo de IA interactúe con la página. En lugar de eso, usa el **árbol de accesibilidad** del navegador, que es una representación estructurada de los elementos de la página. Esto tiene varias ventajas importantes:

- **Rápido y ligero**: al trabajar con datos estructurados en lugar de imágenes, consume muchos menos recursos.
- **Compatible con cualquier LLM**: no necesita modelos con capacidades de visión, ya que opera sobre texto estructurado.
- **Determinista**: al evitar la ambigüedad de interpretar imágenes, las acciones son más predecibles.

#### Requisitos.

- Node.js 18 o superior.
- Un cliente MCP compatible: VS Code, Cursor, Windsurf, Claude Desktop, Goose u otro.

#### Configuración.

La configuración estándar del servidor MCP funciona en la mayoría de herramientas:

```
{
  "mcpServers": {
    "playwright": {
      "command": "npx",
      "args": [
        "@playwright/mcp@latest"
      ]
    }
  }
}

```

Para instalarlo en **Claude Code**, simplemente ejecutamos:

```
claude mcp add playwright npx @playwright/mcp@latest

```

Para instalarlo en **Copilot**, usamos el comando `/mcp add` o editamos manualmente el fichero de configuración `~/.copilot/mcp-config.json`.

Para **Cursor**, lo añadimos desde Cursor Settings → MCP → Add new MCP Server.

### ¿Qué es el Playwright CLI?

El **Playwright CLI** es una interfaz de línea de comandos para Playwright pensada específicamente para **agentes de codificación** ( _coding agents_). Está disponible en [https://github.com/microsoft/playwright-cli](https://github.com/microsoft/playwright-cli).

A diferencia del MCP, el CLI expone las capacidades de Playwright a través de comandos de terminal, lo que lo hace más eficiente desde el punto de vista de los tokens consumidos por el modelo de IA.

#### Instalación.

```
npm install -g @playwright/cli@latest
playwright-cli --help

```

#### Instalando las skills.

Una vez instalado el CLI, podemos instalar las **skills** (habilidades) que usará el agente de IA. Las skills son guías de referencia detalladas sobre cómo hacer tareas concretas con Playwright. Para instalarlas en nuestro proyecto, ejecutamos:

```
playwright-cli install --skills

```

Esto instala las skills en el directorio del proyecto, donde el agente las leerá automáticamente. Las skills cubren tareas como:

- Interceptar y mockear peticiones de red.
- Ejecutar código Playwright arbitrario.
- Gestionar múltiples sesiones de navegador.
- Persistir y restaurar el estado del navegador (cookies, localStorage).
- Generar tests desde interacciones.
- Grabar y analizar trazas.
- Capturar vídeo de las sesiones.

### Playwright MCP vs Playwright CLI: ¿cuándo usar cada uno?

Esta es la pregunta clave, y la respuesta depende del caso de uso:

**Usaremos el CLI cuando:**

- Trabajemos con agentes de codificación que trabajan con bases de código grandes.
- Necesitamos **eficiencia de tokens**: el CLI no carga esquemas de herramientas ni árboles de accesibilidad completos en el contexto del modelo.
- El agente necesita combinar la automatización del navegador con lectura de código, ejecución de tests y razonamiento sobre el proyecto.

**Usaremos el MCP cuando:**

- Necesitamos **estado persistente**: el servidor MCP mantiene el contexto del navegador entre llamadas.
- Hagamos exploración interactiva o automatización autónoma de larga duración.
- Trabajemos con **bucles agénticos** que se beneficien de la introspección profunda de la página.
- Implementemos **self-healing tests** o flujos de automatización donde mantener el contexto del navegador sea más importante que el coste en tokens.

En resumen: el **CLI es mejor para agentes de codificación** que trabajan con proyectos grandes, y el **MCP es mejor para bucles agénticos** especializados en automatización de navegador.

### Conclusión de la serie de Playwright.

A lo largo de esta serie hemos visto:

- **Qué es Playwright** y cómo instalarlo.
- Cómo **ejecutar los tests** y las diferentes formas de visualizar los resultados.
- Cómo **escribir tests** desde cero: locators, acciones, aserciones y hooks.
- Cómo **depurar tests** con el UI Mode, el Inspector y el Trace Viewer.
- Cómo integrar Playwright en **CI/CD con GitHub Actions**.
- Los **Playwright Test Agents**: Planner, Generator y Healer para generar tests con IA.
- El **Playwright MCP y CLI** para integrar Playwright con agentes de IA.

Playwright es una herramienta muy potente y en constante evolución. Si aún no la has probado, te animamos a que te pongas manos a la obra y empieces por la instalación. Seguro que no te decepciona.

* * *

Y hasta aquí nuestra serie sobre Playwright. ¡Esperamos que os haya resultado útil y que os anime a adoptar esta herramienta en vuestros proyectos! ¡Nos leemos en la siguiente entrada!
