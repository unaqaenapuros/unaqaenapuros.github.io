---
title: '106 – QA con modelos locales: Ollama para analizar fallos de tests.'
date: '2027-02-08T09:30:00+01:00'
url: /2027/02/08/106-qa-con-modelos-locales-ollama/
image: /img/blog-images/new-posts/2027/02/foto94.jpg
categories:
- ai
- qa
tags:
- ollama
- llm
- testing
author: estefafdez
social_text: |
  ¿Y si no puedes mandar tus logs y tu código a una API externa? Los modelos abiertos en local con Ollama son la respuesta: analizan fallos de tests, resumen logs de CI y proponen casos candidatos sin que nada salga de tu máquina. En esta entrada vemos qué tareas encajan bien, la diferencia entre open weights y open source (con licencias concretas) y cómo integrarlo en tus scripts con una llamada HTTP local.

  https://unaqaenapuros.com/2027/02/08/106-qa-con-modelos-locales-ollama/

  #QA #TestAutomation #AI #Ollama #UnaQAEnApuros
x_text: |
  Modelos abiertos en local con Ollama para QA: analiza fallos de tests y resume logs de CI sin que nada salga de tu máquina.

  https://unaqaenapuros.com/2027/02/08/106-qa-con-modelos-locales-ollama/

  #QA #AI #UnaQAEnApuros
description: "Cómo usar modelos de lenguaje abiertos en local con Ollama para tareas de QA: analizar fallos, resumir logs de CI y generar casos candidatos sin mandar datos fuera."
---
¡Hola a todos!

Después de la serie QA e IA (entradas 101 a 105), queda pendiente una variante muy práctica: ¿y si no puedes (o no quieres) mandar tus logs y tu código a una API externa? En esta entrada hablamos de usar **modelos abiertos en local** para tareas de QA con **Ollama**: analizar fallos de tests, resumir logs de CI y generar casos candidatos sin que nada salga de tu máquina. ¡Empezamos!

¿Qué es Ollama? Una herramienta gratuita y open source que descarga y ejecuta modelos de lenguaje en tu propia máquina, sin depender de un proveedor externo ([ollama.com](https://ollama.com)). Se instala como cualquier programa y, a partir de ahí, los modelos se descargan y se usan con un comando.

### Por qué un modelo local.

Para mí hay 3 razones muy importantes para que lo consideres:

- **Datos sensibles**: los logs de tests contienen URLs internas, datos de prueba y a veces datos que no deberían estar ahí. Mandarlos a una API externa puede no ser una opción.
- **Coste y control**: sin tokens que pagar ni límites de uso impuestos por un proveedor: el límite lo pone tu propia máquina. El modelo se ejecuta en tu ordenador, con tus restricciones, o en un servidor si tu empresa lo tiene montado para uso interno. A veces, esto puede ser incluso mejor que pagar licencias de Claude, ChatGPT, Copilot o similares.
- **La versión la eliges tú**: fijas el modelo y la versión exacta que quieres usar, y no cambia de un día para otro como un endpoint gestionado.

Eso sí: local **reduce la exposición, no la elimina**. Si luego copias la salida en una herramienta en la nube, o tus herramientas hacen telemetría, los datos vuelven a salir. "Local" no es sinónimo de privacidad absoluta.

### Open source, open weights: no es lo mismo.

Antes de elegir modelo, un matiz que importa legalmente: la mayoría de los "modelos abiertos" populares son **open weights** (pesos descargables con licencia propia), no open source en sentido estricto. Ejemplos concretos:

- **Mistral 7B**: Apache 2.0. Uso comercial permitido con pocas restricciones.
- **Qwen2.5-7B**: Apache 2.0 (ojo: no toda la familia Qwen usa la misma licencia, conviene comprobar la del modelo exacto que descargues).
- **Llama 3.x**: licencia propia de Meta (Llama Community License), con condiciones adicionales sobre uso y redistribución.

Conclusión práctica: antes de usar un modelo en el trabajo, abre su página oficial y lee la licencia **de ese modelo y de tu versión concreta**, no la de la familia. Ten esto muy en cuenta.

### Qué tareas de QA encajan bien.

Los modelos locales pequeños (7-8B) no compiten con los grandes modelos comerciales en razonamiento complejo, pero hay tareas de QA en las que pueden ayudarnos mucho:

  1. **Analizar un fallo de test.** Cuando tenemos un fallo en un test, lo primero es entender qué ha pasado, y el modelo sirve como primer filtro: le pegas el stack trace (la traza de llamadas que deja el error, con el archivo y la línea de cada salto) junto al mensaje del assert y le pides hipótesis ordenadas por probabilidad. No acierta siempre, pero te da por dónde empezar a mirar.
  2. **Resumir logs de CI.** Un pipeline roto puede dejar miles de líneas de log y el fallo real suele esconderse entre ellas. El modelo las resume en lo que importa: qué rompió, dónde y qué tests se llevaron por delante. Tú sigues verificando el resumen contra el log, pero empezar por ahí es mucho más llevadero que empezar por la primera línea.
  3. **Generar casos candidatos.** A partir de una historia de usuario o de una función, el modelo propone una primera lista de casos de prueba que luego revisamos nosotros. Recuerda la regla de [la entrada 101](https://unaqaenapuros.com/2027/01/04/101-qa-e-ia-i-tests-generados-por-ia-mutation-testing/): lo generado se audita, no se acepta tal cual.
  4. **Clasificar tests inestables.** Cuando una suite acumula fallos aleatorios, antes de investigarlos uno a uno conviene agruparlos. El modelo lee el histórico de fallos y sugiere patrones (mismo componente, mismo mensaje de error, misma franja horaria) que tú confirmas o descartas. No significa que todos compartan causa, pero investigar por grupos ordena mucho el trabajo.

### Manos a la obra: del log al análisis.

Con Ollama instalado, empezar es cuestión de dos comandos:

```bash
# Download the model (only needed once)
ollama pull mistral:7b

# Ask the model from the command line
ollama run mistral:7b "Summarize this test failure in two sentences: $(cat failure.txt)"
```

Y si no quieres vivir en la terminal, hay otra forma: deja Ollama ejecutándose en segundo plano y usa sus modelos desde herramientas que ya tengas. VS Code, por ejemplo, tiene una extensión oficial de Ollama que añade tus modelos locales al selector de modelos del chat del editor. Los pasos ([la documentación oficial los detalla](https://docs.ollama.com/integrations/vscode)):

  1. Comprueba que tu VS Code es la versión 1.127 o superior e instala la extensión **Ollama** desde el marketplace: búscala en la vista de extensiones, la publica el propio equipo de Ollama.
  2. Asegúrate de que Ollama está arrancado y tiene al menos un modelo descargado, el `ollama pull` de antes.
  3. Abre el chat de VS Code y despliega el selector de modelos: ahí aparecen tus modelos locales, listos para elegir.

![Selector de modelos del chat de VS Code con los modelos locales de Ollama y qwen3.5:4b elegido](/img/blog-images/new-posts/2027/02/106-ollama-vscode.jpg)

A partir de ahí le hablas al modelo desde el editor como en cualquier otro chat, y las respuestas las genera el modelo local en tu máquina. Así es como lo uso yo: con Ollama ejecutándose y el modelo seleccionado en VS Code.

Y si quieres integrarlo en un script o en la CI, Ollama expone una API HTTP en tu propia máquina. Vamos por partes, que aquí hay varios conceptos que conviene tener claros.

Una API HTTP es una forma de hablar con un programa mediante peticiones web, igual que el navegador pide una página a un servidor, pero entre programas. Ollama abre esa ventanilla en tu equipo, en la dirección `http://localhost:11434`: `localhost` significa "esta misma máquina" y `11434` es el puerto donde escucha. Cada operación tiene su endpoint, la ruta concreta dentro de esa dirección. Para generar texto, el endpoint es `/api/generate` y se llama con el método POST, es decir, enviándole datos en lugar de solo pedirlos.

Esos datos viajan en formato JSON, una manera de escribir pares clave-valor entre llaves que entienden casi todos los lenguajes: `{"model": "mistral:7b", "prompt": "..."}`. Con `model` dices qué modelo quieres usar y con `prompt` le pasas el texto. Hay un tercer campo que conviene conocer: por defecto la respuesta llega en modo _stream_, trozo a trozo según se genera, como en los chats. Para un script nos interesa recibirla entera, y eso se consigue con `stream: false`.

En resumen: `POST http://localhost:11434/api/generate` con un cuerpo JSON que lleva `model`, `prompt` y `stream: false`.

Para probarlo hace falta tener Ollama arrancado con el modelo descargado (lo que acabamos de ver) y dos herramientas de terminal: `curl`, que lanza la petición, y [jq](https://jqlang.github.io/jq/), que monta el JSON. Y un detalle importante: no construyas ese JSON concatenando texto a mano, porque un log real trae comillas y saltos de línea que rompen el cuerpo de la petición. jq se encarga del escapado por ti:

```bash
jq -n --arg prompt "Analyze this test failure and give me the 3 most likely causes:
$(cat failure.txt)" \
  '{model: "mistral:7b", prompt: $prompt, stream: false}' \
  | curl -s http://localhost:11434/api/generate -d @-
```

La respuesta JSON trae el texto generado en el campo `response`, junto a métricas de la generación.

![Llamada real a la API local de Ollama con el análisis de un fallo de test real](/img/blog-images/new-posts/2027/02/106-ollama-analisis-fallo.png)

*Ejecución real del flujo de arriba en una máquina con poca RAM, por eso con un modelo pequeño (`qwen2.5:0.5b`) en lugar del 7B del ejemplo (la salida se muestra con `jq -r .response` y `fold` para que quepa en pantalla). El log analizado es un fallo de test real. Fíjate en la respuesta: detecta que algo va con mayúsculas y minúsculas, pero enreda la dirección del fallo («ana» frente a «ANA») y se inventa una causa sobre la versión de TAP. Es justo el nivel de fiabilidad que esta entrada advierte: útil como primer filtro, nunca como veredicto.*

A partir de ahí, el patrón es el de siempre: un script que recoge los fallos del pipeline, los manda al modelo local y deja el resumen como comentario o artefacto del build.

### Requisitos y expectativas realistas.

- **Hardware**: como regla general, un modelo de 7-8B cuantizado necesita en torno a 8 GB de RAM libres para ir cómodo. Con GPU dedicada va mucho más rápido, pero no es imprescindible.
- **Calidad**: el tamaño del modelo no garantiza nada por sí solo. Antes de fiarte de uno para una tarea, pruébalo con casos reales de esa tarea y revisa el resultado con lupa: ¿conserva los datos relevantes?, ¿omite detalles que importan?, ¿propone conclusiones que el texto no apoya? Esa prueba con tus propios casos te dice más que cualquier cifra de parámetros.
- **Verificación**: que el modelo se ejecute en tu ordenador no lo hace más fiable. Puede generar tests con aserciones débiles o inventar información, así que la regla de [la entrada 101](https://unaqaenapuros.com/2027/01/04/101-qa-e-ia-i-tests-generados-por-ia-mutation-testing/) se aplica aquí también: lo que propone el modelo se revisa antes de usarlo, siempre.

### Para seguir leyendo.

- _Analyzing Cypress Automated Test Results with Local AI Using Ollama + Open Source LLM_, de Niar: https://medium.com/@niarsdet/analyzing-cypress-automated-test-results-with-local-ai-using-ollama-open-source-llm-ccecba0e8245
- _How I Use Ollama to Make Sense of Automated Test Failure_, de Niar: https://medium.com/@niarsdet/how-i-use-ollama-to-make-sense-of-automated-test-failure-d99a893bc0e9
- Documentación de la API de Ollama: https://docs.ollama.com/api/introduction

Y hasta aquí nuestra entrada sobre modelos locales para QA. ¡Nos leemos en la siguiente entrada!
