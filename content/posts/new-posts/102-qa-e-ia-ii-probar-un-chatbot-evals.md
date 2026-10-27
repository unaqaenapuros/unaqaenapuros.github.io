---
title: '102 – QA e IA (II): Cómo probar un chatbot cuando no hay una única respuesta correcta.'
date: '2027-01-11T09:30:00+01:00'
url: /2027/01/11/102-qa-e-ia-ii-probar-un-chatbot-evals/
image: /img/blog-images/new-posts/2027/01/foto91.jpg
categories:
- ai
- automation
- qa
tags:
- evals
- llm
- testing
author: estefafdez
social_text: |
  Un chatbot puede responder bien de veinte formas distintas... o inventarse la respuesta con total soltura. ¿Cómo lo pruebas? En la segunda entrega de la serie QA e IA montamos paso a paso una forma sencilla de comprobarlo: casos concretos, comprobaciones automáticas y cuándo hace falta otra IA como juez.

  https://unaqaenapuros.com/2027/01/11/102-qa-e-ia-ii-probar-un-chatbot-evals/

  #QA #TestAutomation #AI #LLM #UnaQAEnApuros
x_text: |
  ¿Cómo se prueba un chatbot si no hay una única respuesta correcta? Segunda entrega de QA e IA: evals paso a paso.

  https://unaqaenapuros.com/2027/01/11/102-qa-e-ia-ii-probar-un-chatbot-evals/

  #QA #AI #LLM
description: "Cómo probar un chatbot con evals: dataset de casos, criterios deterministas, LLM como juez y ejecución en la CI."
---
Hola de nuevo,

En la entrada anterior usamos la IA para escribir tests y aprendimos a auditarlos. Hoy cruzamos al otro lado: el producto que probamos **lleva IA dentro**. Un chatbot de soporte, una herramienta para resumir documentos, un buscador que responde con lenguaje natural. ¿Cómo escribes un `assert` sobre algo que puede contestar bien de veinte formas distintas? ¡Empezamos!

### El problema: se acabó el "entrada X, salida Y".

En los tests tradicionales solemos partir de una idea base: misma entrada, misma salida. Con un modelo generativo eso ya no vale:

- La respuesta **correcta no es única**: "30 días naturales" y "un mes desde la compra" pueden ser las dos correctas (o una de ellas un error, según la política real).
- El mismo prompt puede dar **respuestas distintas** entre ejecuciones.
- El fallo más peligroso no es una excepción: es una respuesta **fluida, convincente e inventada** (una _alucinación_).

Esto no significa que no se pueda probar. Significa que cambia la unidad de trabajo: en lugar de comparar textos exactos, definimos **criterios de evaluación** y los aplicamos de forma sistemática. A eso se le llama hacer **evals**.

### Qué es una eval.

Una _eval_ es, en esencia, lo mismo que un test: una entrada, una ejecución y una comprobación. Lo que cambia es la comprobación, que admite varias formas:

  1. **Criterios deterministas**: la respuesta debe contener "30 días" y no debe contener "60 días". Baratos, rápidos y repetibles. Ideales para hechos concretos.
  2. **Criterios de formato**: es JSON válido, tiene menos de 500 caracteres, incluye un enlace de ayuda. Perfectamente automatizables.
  3. **Juicio de otro modelo** (_LLM-as-a-judge_): un segundo modelo puntúa la respuesta contra una rúbrica, una guía de criterios concretos para valorarla ("¿responde a la pregunta?" o "¿se inventa datos?"). Escala bien, pero el juez también puede equivocarse, así que hay que revisar sus criterios con muestras manuales.
  4. **Revisión humana**: insustituible para tono, sensibilidad y casos delicados. La reservamos para muestras y para validar que las evals automáticas miden lo que creemos.

La recomendación general, que coincide con la guía de buenas prácticas de evaluación de OpenAI: empieza con criterios simples y deterministas siempre que puedas, y sube de complejidad solo cuando el criterio simple no capta lo que te importa.

### Manos a la obra: una eval mínima.

Vamos a montar una eval pequeña en TypeScript para un chatbot de soporte ficticio. Tres piezas: el sistema bajo prueba, un **dataset de casos** y la función que evalúa.

```typescript
// The "system under test". In a real project you'd call your API/LLM here.
function chatbot(question: string): string {
  if (question.includes('return')) {
    return 'You can return any product within 30 days of purchase.';
  }
  if (question.includes('shipping')) {
    return 'Shipping takes 3 to 5 business days.';
  }
  return "Sorry, I don't have information about that.";
}
```

El dataset es la parte importante y la que más se parece a nuestro diseño de casos de prueba de siempre. Cada caso lleva su pregunta y sus **criterios**:

```typescript
interface TestCase {
  id: string;
  question: string;
  mustContain: string[];
  mustNotContain: string[];
}

const cases: TestCase[] = [
  {
    id: 'return-window',
    question: 'What is the return window?',
    mustContain: ['30 days'],
    mustNotContain: ['60 days', '90 days'], // typical hallucinations
  },
  {
    id: 'shipping-time',
    question: 'How long does shipping take?',
    mustContain: ['3 to 5 business days'],
    mustNotContain: ['24 hours', 'free'],
  },
  {
    id: 'out-of-scope',
    question: "What's the weather like tomorrow?",
    mustContain: ["don't have information"],
    mustNotContain: ['sunny', 'rain'], // it must not invent the weather
  },
];
```

Fíjate en el tercer caso: probar el comportamiento **fuera de alcance** es tan importante como probar el _happy path_. Un chatbot que se inventa la respuesta a lo que no sabe es un defecto, aunque conteste con soltura.

Y la evaluación, que no es más que un bucle con aserciones:

```typescript
function evaluate(chatbot: (question: string) => string, cases: TestCase[]): void {
  let passed = 0;
  for (const testCase of cases) {
    const response = chatbot(testCase.question).toLowerCase();
    const failures: string[] = [];
    for (const fragment of testCase.mustContain) {
      if (!response.includes(fragment.toLowerCase())) {
        failures.push(`missing "${fragment}"`);
      }
    }
    for (const fragment of testCase.mustNotContain) {
      if (response.includes(fragment.toLowerCase())) {
        failures.push(`invents "${fragment}"`);
      }
    }
    const ok = failures.length === 0;
    if (ok) passed++;
    console.log(`${ok ? 'PASS' : 'FAIL'} ${testCase.id}${ok ? '' : ' -> ' + failures.join(', ')}`);
  }
  console.log(`\nScore: ${passed}/${cases.length} cases passed`);
}

evaluate(chatbot, cases);
```

Desde Node 22.18 no hace falta compilar nada: guardamos el fichero como `eval.ts` y lo ejecutamos tal cual con `node eval.ts`. Con este chatbot de prueba obtenemos:

```
PASS return-window
PASS shipping-time
PASS out-of-scope

Score: 3/3 cases passed
```

Es un ejemplo sencillo, pero la estructura es la misma que usan las herramientas serias: **dataset + criterios + ejecución repetible**. Cambia el chatbot de prueba por una llamada a vuestra API y ya tienes una eval real.

### De la eval al pipeline.

Para que esto nos sirva en un proyecto real, os dejo tres buenas prácticas como consejo:

- Os recomiendo guardar estos casos de prueba en el repositorio y revisar los cambios en el pull request, igual que hacemos con el código. Si alguien reporta una respuesta incorrecta, podemos añadirla como un caso más para comprobar que no vuelva a pasar.
- También os recomiendo ejecutar las evals en la CI cada vez que cambie el prompt, el modelo o los datos de contexto (en un [sistema RAG](https://learn.microsoft.com/en-us/azure/developer/ai/advanced-retrieval-augmented-generation), que busca en documentos y responde apoyándose en ellos, la base de documentos). Un cambio de prompt es un cambio de comportamiento, así que merece la misma regresión que cualquier otro.
- Y mejor definir umbrales realistas que perseguir la perfección: la IA puede dar respuestas distintas aunque le hagamos la misma pregunta, así que un 100% estable es raro. Es mejor "al menos el 95% de los casos de hechos críticos y ninguna alucinación en los casos de seguridad" que exigir perfección y acabar ignorando los fallos.

Si el proyecto crece, hay herramientas dedicadas como [**promptfoo**](https://www.promptfoo.dev/), [**DeepEval**](https://deepeval.com/) o [**RAGAS**](https://www.ragas.io/) que estructuran justo esto: datasets, criterios, jueces automáticos e informes. Pero el concepto ya lo tienes con el bucle de arriba.

### Para seguir leyendo.

Si quieres seguir profundizando en las evals, te dejo estos enlaces:

- _Evaluation best practices_, guía de OpenAI: https://developers.openai.com/api/docs/guides/evaluation-best-practices
- _Techniques for Testing Generative AI Applications_, de QA Wolf: https://medium.com/qawolf/techniques-for-testing-generative-ai-applications-344ef53bb13a

* * *

Y hasta aquí la segunda entrega de la serie. En la siguiente veremos qué pasa cuando el usuario no es inocente: prompt injection, el nuevo caso de prueba que todo QA debería conocer. ¡Nos leemos en la siguiente entrada!
