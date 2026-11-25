---
title: '105 – QA e IA (V): checklist para auditar lo que la IA escribe.'
date: '2027-02-01T09:30:00+01:00'
url: /2027/02/01/105-qa-e-ia-v-checklist-auditoria/
image: /img/blog-images/new-posts/2027/02/foto93.jpg
categories:
- ai
- best-practices
- qa
tags:
- checklist
- llm
- testing
author: estefafdez
social_text: |
  Cerramos la serie QA e IA con lo más práctico: una checklist de auditoría para todo lo que un modelo genere (tests, respuestas, datos). Cuatro bloques revisables, sacados de las entregas anteriores: mutation testing contra la cobertura vacía, evals para salidas no deterministas, prompt injection como caso de prueba y validación de datos sintéticos.

  https://unaqaenapuros.com/2027/02/01/105-qa-e-ia-v-checklist-auditoria/

  #QA #TestAutomation #AI #SoftwareTesting #UnaQAEnApuros
x_text: |
  Cerramos la serie QA e IA con una checklist de auditoría para todo lo que un modelo genere: tests, respuestas y datos sintéticos.

  https://unaqaenapuros.com/2027/02/01/105-qa-e-ia-v-checklist-auditoria/

  #QA #AI #UnaQAEnApuros
description: "Checklist práctica para auditar lo que la IA escribe antes de dejarlo entrar en el pipeline: tests, evals, prompt injection y datos sintéticos."
---
¡Hola a todos!

Llegamos al final de la serie QA e IA. En las cuatro entregas anteriores hemos ido pieza por pieza: primero vimos qué pasa cuando dejamos que un modelo escriba nuestros tests, después cómo evaluar respuestas que no son siempre iguales, luego cómo convertir los ataques contra el modelo en casos de prueba y, por último, cómo validar los datos de prueba que la IA genera. En esta entrada juntamos todo eso en una sola herramienta de trabajo: una **checklist de auditoría** para usar cada vez que un modelo genere algo que vaya a tocar nuestro pipeline.

La idea de fondo es muy sencilla: cuando la IA produce un test, una respuesta o un dataset, no lo tratamos como un resultado terminado sino como **un borrador que hay que auditar** antes de dejarlo entrar. Igual que no mergeamos código de un compañero sin revisarlo, no incorporamos nada generado sin pasarle antes el filtro. Las cuatro secciones que siguen son ese filtro, una por cada entrega de la serie. Revisa una a una las secciones y quédate solo con las que apliquen a tu caso: las que no apliquen son un problema menos que revisar.

¡Empezamos!

### 1. Auditar los tests generados (entrada I).

De [la primera entrega](https://unaqaenapuros.com/2027/01/04/101-qa-e-ia-i-tests-generados-por-ia-mutation-testing/) nos quedamos con una idea incómoda: una suite generada por un modelo puede cubrir el cien por cien de las líneas y, aun así, detectar solo una parte de los errores reales. La cobertura mide qué líneas se ejecutan, no qué se comprueba en ellas, así que el primer punto de la checklist es no fiarnos de ese número.

¿Cómo saber si una suite protege de verdad? La técnica que vimos es el **mutation testing**: herramientas como [Stryker](https://stryker-mutator.io/) introducen errores pequeños a propósito en el código (cambian un `>` por un `>=`, invierten una condición) y nos dicen cuántos de esos errores detecta la suite. Cada error introducido que ningún test detecta es un hueco real de protección, aunque la cobertura diga 100%.

Después toca revisar los asserts a mano, porque un test vale lo que vale su comprobación. Si el test ejecuta la función pero no verifica nada concreto sobre el resultado, ese test no nos protege de ningún fallo real: solo suma líneas ejecutadas al informe de cobertura y tiempo de mantenimiento al equipo. Con los tests generados esto pasa más a menudo de lo que parece, porque el modelo sabe hacer que el código se ejecute, pero no sabe qué es importante comprobar en nuestro proyecto.

Y ahí enlazamos con el último punto de esta sección: el modelo no conoce **nuestras reglas de negocio**. Sabe escribir un test genérico de un formulario, pero no sabe que en nuestra tienda los pedidos de más de 500 euros llevan una verificación extra, ni qué pasa cuando alguien usa la aplicación de formas para las que no fue pensada. Esos casos, los que salen del dominio y de la experiencia con el producto, son los que hay que escribir a mano.

### 2. Evaluar respuestas que no son siempre iguales (entrada II).

Con los tests clásicos la comprobación es de igualdad: la función devuelve 42 o no devuelve 42. Con un modelo de IA eso no funciona, porque a la misma pregunta puede responder de formas distintas y ser correctas todas. De [la segunda entrega](https://unaqaenapuros.com/2027/01/11/102-qa-e-ia-ii-probar-un-chatbot-evals/) nos quedamos con la herramienta para este caso: las **evals**.

Una eval es, básicamente, un conjunto de casos de ejemplo junto con los criterios para valorar cada respuesta. Imagina un chatbot de soporte: el dataset sería una lista de preguntas representativas de los usuarios y, para cada una, anotamos qué debe cumplir una buena respuesta (menciona el plazo de devolución, no inventa precios, mantiene un tono cordial). Al ejecutar la eval, cada respuesta del modelo se compara contra esos criterios y obtenemos un porcentaje de acierto que sí podemos seguir de versión en versión.

El truco está en separar dos tipos de comprobaciones. Las **deterministas** se pueden verificar con código, sin juicio: que la respuesta sea un JSON válido, que incluya los campos obligatorios, que no contenga datos prohibidos como emails o teléfonos. Las demás necesitan criterio, y ahí una opción cada vez más común es usar otro modelo como juez. Si vamos por ese camino, hay que darle al juez las mismas herramientas que le daríamos a una persona: una lista concreta de lo que tiene que mirar y ejemplos de respuestas buenas y malas para que calibre. Un modelo juzgando sin criterios claros da veredictos distintos en cada ejecución, y los da con la misma seguridad que si fueran correctos. Con un juez así no hay porcentaje que valga.

Último punto de esta sección: el dataset de la eval se versiona como el código, porque forma parte de la suite. Si cambian los criterios y no queda registrado, los porcentajes de hoy no se pueden comparar con los de dentro de dos semanas.

### 3. Convertir ataques en casos de prueba (entrada III).

En [la tercera entrega](https://unaqaenapuros.com/2027/01/18/103-qa-e-ia-iii-prompt-injection-caso-de-prueba/) nos pusimos el otro sombrero: todo texto externo que llega al modelo (un mensaje de usuario, un documento, un email, un adjunto) es **entrada potencialmente hostil**. El ejemplo típico es la **prompt injection**: un texto que intenta darle al modelo instrucciones nuevas por encima de las nuestras, como un *«ignore your instructions»* escondido en un documento que le hemos pedido resumir.

La checklist aquí tiene tres puntos. El primero es mantener una batería de inyecciones conocidas como **casos de prueba de regresión que puedas lanzar** con cada cambio del sistema, igual que en su día se hacía con los XSS clásicos: cada ataque conocido tiene que seguir fallando después de cada ajuste del prompt o del modelo. El segundo es la técnica del **canary**: escondemos en las instrucciones del sistema un valor secreto ficticio que el modelo nunca debería revelar, de modo que, si una entrada maliciosa consigue alterar su comportamiento y el canary aparece en una respuesta, lo sabemos a la primera. Y el tercero es no olvidar el happy path: después de blindar el sistema, comprobamos que el usuario legítimo puede seguir trabajando con normalidad, porque una defensa que bloquea el uso normal no es una defensa, es otro problema.

### 4. Validar los datos sintéticos (entrada IV).

De [la cuarta entrega](https://unaqaenapuros.com/2027/01/25/104-qa-e-ia-iv-datos-de-prueba-generados-con-ia/) nos quedamos con la regla de oro: los datos generados por IA son **materia prima, no producto terminado**. Antes de que entren en cualquier test, les ponemos delante una validación mínima con código, como la que montamos en esa entrada.

¿Qué revisa esa validación? Los defectos que casi siempre aparecen: **duplicados** (pides 100 registros y algunos vuelven con variaciones mínimas), distribuciones planas donde el mundo real tiene colas (todas las edades entre 25 y 45, cero valores extremos), formatos casi correctos (un código postal de cuatro dígitos, un email con dominio `test.com`) e incoherencias internas (un pedido entregado antes de pagado). Y, sobre todo, que los datos cubran lo que necesitamos probar: el modelo tiende al caso medio, así que los extremos, los nulos y los valores frontera hay que pedirlos explícitamente o generarlos aparte.

Hay un caso que merece punto aparte: los **entornos compartidos**. Si los datos generados van a un entorno donde ya existen otros (o donde otras personas generan los suyos), hay que comprobar que los identificadores no chocan entre sí ni con lo que ya hay: que no lleguen dos clientes con el mismo email, ni un pedido con un id que ya existe. En un entorno así, un identificador repetido no es solo un dato feo, es un test que falla un martes a las nueve de la mañana sin que nadie sepa por qué.

### El flujo completo.

Si lo juntamos todo, el flujo de trabajo queda en una frase: **genera con la IA, audita con técnica e incorpora solo lo auditado**. La primera vez que recorras la checklist te llevará una tarde. Cuando ya sea costumbre, minutos. Y cada sección tiene su entrega completa detrás, por si quieres profundizar en cómo montar esa parte.

* * *

Y hasta aquí la serie QA e IA. Han sido cinco entregas y, si tengo que quedarme con una idea, es esta: la IA escribe rápido, pero el criterio para saber si lo que escribe nos sirve sigue siendo nuestro. La checklist de hoy es mi forma de no olvidarlo. ¡Nos leemos en la siguiente entrada!
