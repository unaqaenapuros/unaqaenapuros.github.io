---
title: '101 – QA e IA (I): Tests generados por IA, ¿qué comprueban de verdad?'
date: '2027-01-04T09:30:00+01:00'
url: /2027/01/04/101-qa-e-ia-i-tests-generados-por-ia-mutation-testing/
image: /img/blog-images/new-posts/2027/01/foto90.jpg
categories:
- ai
- best-practices
- qa
tags:
- mutation-testing
- stryker
- testing
author: estefafdez
social_text: |
  Le pedimos tests a una IA, pasan, la cobertura marca 100%... y aun así un tercio de los errores que introducimos a propósito en el código pasan desapercibidos. En la primera entrega de la serie QA e IA hacemos el experimento completo con mutation testing y vemos cómo auditar los tests que escribe un modelo.

  https://unaqaenapuros.com/2027/01/04/101-qa-e-ia-i-tests-generados-por-ia-mutation-testing/

  #QA #TestAutomation #AI #MutationTesting #UnaQAEnApuros
x_text: |
  Tests generados por IA con 100% de cobertura... que dejan pasar un tercio de los errores. Empezamos la serie QA e IA con mutation testing.

  https://unaqaenapuros.com/2027/01/04/101-qa-e-ia-i-tests-generados-por-ia-mutation-testing/

  #QA #AI #MutationTesting
description: "Tests generados por IA con 100% de cobertura que no detectan errores: cómo auditarlos con mutation testing y Stryker."
---
¡Hola a todos!

Empezamos hoy una serie nueva en el blog: **QA e IA**. Llevamos muchas entradas hablando de Playwright y era momento de abrir el foco, porque hay un tema que está cambiando nuestro día a día: los modelos de IA que escriben tests por nosotros. En esta primera entrada vamos a ver qué pasa cuando aceptamos esos tests sin revisarlos, con un experimento real que podéis repetir en vuestro equipo. ¡Empezamos!

### La promesa: tests gratis con un prompt.

La idea es tentadora: le pasas una función al modelo, le pides "escríbeme los tests" y te devuelve una suite que **compila, pasa y cubre el código**. ¿Qué puede fallar?

El problema es que un test que pasa no demuestra nada por sí solo. Un test solo es útil si **falla cuando el código se rompe**. Y ahí es donde los tests generados por IA suelen cojear:

- Aserciones **demasiado débiles** (`el resultado es un número`, `el total es mayor que cero`).
- Aserciones que **repiten la lógica del código** en lugar de comprobar el comportamiento esperado.
- **Happy paths** bien cubiertos y **valores límite olvidados**.
- Tests que prueban lo mismo con distinto nombre, inflando la sensación de cobertura.

¿Cómo medimos esto de forma objetiva? Con **mutation testing**.

### ¿Qué es el mutation testing?

El _mutation testing_ (pruebas de mutación) es una técnica que evalúa la **calidad de tus tests**, no la de tu código. La herramienta introduce pequeños errores deliberados en el código (cada uno es un **mutante**): cambia un `<` por un `<=`, invierte una condición, vacía un bloque... y después ejecuta tu suite contra cada mutante:

- Si algún test **falla**, el mutante está **eliminado** (_killed_): tus tests han detectado el error.
- Si todos los tests **pasan**, el mutante ha **sobrevivido** (_survived_): tienes un agujero en la suite.

El resultado es el **mutation score**: porcentaje de mutantes eliminados. Es una métrica mucho más honesta que la cobertura, porque la cobertura solo te dice qué líneas se ejecutaron, no si comprobaste algo sobre ellas.

Para JavaScript, la herramienta de referencia es **Stryker** (Stryker Mutator, un proyecto open source que también tiene versión para .NET con Stryker.NET. Para Java, la herramienta de referencia es otra: PIT). Stryker hace exactamente lo descrito arriba: instrumenta tu código, genera los mutantes uno a uno, ejecuta tu suite contra cada uno y te dice cuáles sobrevivieron y en qué línea. Se instala como dependencia de desarrollo (`npm install --save-dev @stryker-mutator/core` más el runner de tu framework de tests) y se ejecuta con `npx stryker run`. Y que no dé miedo probarlo: Stryker no toca tus archivos. Copia el proyecto a un directorio temporal (un sandbox) y es ahí donde aplica las mutaciones y ejecuta los tests, así que tus archivos originales quedan intactos.

### El experimento: una función, dos suites.

Vamos a montar un experimento pequeño que puedes repetir en media hora. La función es un carrito de la compra con descuentos y gastos de envío:

```javascript
// Shopping cart: total with discounts and shipping
function calculateTotal(lines, discountCode) {
  let subtotal = 0;
  for (const line of lines) {
    subtotal += line.price * line.quantity;
  }

  let discount = 0;
  if (discountCode === 'SUMMER10') {
    discount = subtotal * 0.10;
  } else if (discountCode === 'VIP20' && subtotal >= 100) {
    discount = subtotal * 0.20;
  }

  let total = subtotal - discount;
  if (total < 50) {
    total += 5; // shipping costs
  }
  return Math.round(total * 100) / 100;
}

module.exports = { calculateTotal };
```

Las suites originales de este experimento no se han recuperado. Para poder repetirlo, las hemos reconstruido a partir de esta función y del ejemplo de test. Las cifras que veis a continuación corresponden a esta nueva ejecución, con Stryker 10.1.1, Mocha 11.8.0, c8 12.0.0 y Node 22.23.4.

Sobre esta función tenemos **dos suites de tests con Mocha**, un framework de tests para JavaScript:

1. Una **suite floja**, imitando lo que suele devolver un LLM cuando le pides tests sin más contexto: recorre todo el código, pero con aserciones débiles. Por ejemplo:

```javascript
it('applies some discount with SUMMER10', () => {
  const total = calculateTotal([{ price: 100, quantity: 1 }], 'SUMMER10');
  assert.ok(total < 100); // passes with any discount, even the wrong one
});
```

2. Una **suite cuidada**, con valores exactos y casos límite: el envío justo por debajo y justo en 50, etc.

Primero medimos la **cobertura** de la suite floja con c8, una herramienta que cuenta qué líneas y ramas ejecutan tus tests:

```
----------|---------|----------|---------|---------|
File      | % Stmts | % Branch | % Funcs | % Lines |
----------|---------|----------|---------|---------|
 cart.js  |     100 |      100 |     100 |     100 |
----------|---------|----------|---------|---------|
```

Cobertura perfecta: 100% en todo. Si nos fiáramos solo de esta métrica, la suite parecería impecable. Ahora pasamos Stryker sobre la misma suite:

```
| % Mutation score | # killed | # survived |
|            64.52 |       20 |         11 |
```

**11 de los 31 mutantes sobrevivieron.** Es decir: podríamos romper un tercio de las condiciones de la función y los tests seguirían en verde. Algunos de los mutantes supervivientes:

- `if (total < 50)` → `if (false)`: nadie comprobaba el importe exacto del envío.
- `total += 5` → `total -= 5`: nadie comprobaba cuánto se sumaba.
- `subtotal >= 100` → `subtotal > 100`: el valor límite del descuento VIP20 no estaba probado.

Y con la **suite cuidada**, mismo código y misma herramienta:

```
| % Mutation score | # killed | # survived |
|            93.55 |       29 |          2 |
```

Los dos mutantes que sobrevivieron también son una lección: los dos vivían en la comparación `subtotal >= 100`. Uno la cambiaba por `subtotal > 100` y el otro la dejaba siempre verdadera. Es decir, el valor límite del VIP20 no estaba probado del todo: faltaban justo el 99 y el 100. Ni siquiera la suite buena lo cubría del todo, y ahí está el valor de la técnica: te enseña los huecos que no ves.

### Qué nos dice esto sobre los tests que escribe una IA.

El experimento confirma lo que varios equipos están reportando: **cobertura alta y capacidad real de detectar fallos son dos cosas distintas**, y los tests generados por IA tienden a maximizar la primera. El modelo optimiza para que el test pase y el código quede recorrido, no para que el test sea exigente.

Esto no significa que no debas usar IA para generar tests. Significa que el trabajo del QA se desplaza: de escribir tests a **auditarlos**. Un flujo razonable:

  1. Genera la suite con el modelo, pero pídele explícitamente **valores límite y casos de error**, no solo el happy path.
  2. Revisa las aserciones: si ves `typeof`, `toBeTruthy()` o `> 0` donde debería haber un valor exacto, ese test no está probando lo que crees.
  3. Ejecuta **Stryker** (o la herramienta de tu stack) sobre el código cubierto por la suite generada y mira qué mutantes sobreviven.
  4. Convierte los supervivientes en tests nuevos: cada mutante que escapa es un caso de prueba que te están regalando.

### Para seguir leyendo.

Si quieres seguir profundizando en el mutation testing y en Stryker, te dejo estos enlaces:

- Documentación de **Stryker Mutator**: https://stryker-mutator.io/docs/stryker-js/getting-started/
- _What is mutation testing?_, introducción al concepto en la documentación oficial de Stryker: https://stryker-mutator.io/docs/

* * *

Por ir resumiendo: un test que pasa solo demuestra que el código se ejecutó, un test útil **falla cuando el código se rompe**. La cobertura mide qué líneas se ejecutan y el mutation score mide si tus aserciones detectan errores de verdad. Ya lo hemos visto en el experimento: la suite floja, con un 100% de cobertura, eliminó solo el 64% de los mutantes, mientras que la suite cuidada llegó al 93%. Así que si usas la IA para generar tests, úsala como punto de partida y audita lo que te devuelve: cada mutante que sobrevive es un caso de prueba que te están regalando.

Y hasta aquí la primera entrega de la serie QA e IA. En la siguiente cambiaremos de lado: en lugar de usar la IA para probar software, veremos cómo probar software que usa IA, con la pregunta incómoda de cómo testear un chatbot cuando no existe una única respuesta correcta. ¡Nos leemos en la siguiente entrada!
