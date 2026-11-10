---
title: '104 – QA e IA (IV): Datos de prueba generados con IA (realismo, riesgos y validación).'
date: '2027-01-25T09:30:00+01:00'
url: /2027/01/25/104-qa-e-ia-iv-datos-de-prueba-generados-con-ia/
image: /img/blog-images/new-posts/2027/01/foto89.jpg
categories:
- ai
- best-practices
- qa
tags:
- test-data
- llm
- testing
author: estefafdez
social_text: |
 *"Genérame 100 usuarios de prueba"* es fácil de pedir y peligroso de aceptar. En la cuarta entrega de la serie QA e IA vemos los defectos típicos de los datos sintéticos (duplicados, distribuciones planas, formatos colados) y montamos una validación mínima con código antes de dejarlos entrar en nuestros tests.

 https://unaqaenapuros.com/2027/01/25/104-qa-e-ia-iv-datos-de-prueba-generados-con-ia/

 #QA #TestAutomation #AI #TestData #UnaQAEnApuros
x_text: |
 "Genérame 100 usuarios de prueba" es fácil de pedir y peligroso de aceptar. Cuarta entrega de QA e IA: datos sintéticos y cómo validarlos.

 https://unaqaenapuros.com/2027/01/25/104-qa-e-ia-iv-datos-de-prueba-generados-con-ia/

 #QA #AI #TestData
description: "Datos de prueba generados con IA: cuándo compensan, sus defectos típicos y cómo validarlos con código antes de usarlos."
---
Hola de nuevo,

Cuarta entrega de la serie QA e IA. Después de auditar tests generados, evaluar chatbots y convertir ataques en casos de prueba, hoy volvemos a una tarea cotidiana que a todos nos ha robado horas: conseguir **datos de prueba** decentes. Pedirle a un modelo "genérame 100 clientes de prueba" es tentadoramente fácil. La pregunta es qué nos está dando realmente. ¡Empezamos!

### Por qué los datos de prueba son un dolor conocido.

Quien haya montado un entorno de pruebas conoce las opciones clásicas y sus problemas:

- **Copia de producción anonimizada**: realista, pero la anonimización bien hecha es cara y la mal hecha es un riesgo legal (todos conocemos a nuestro amigo RGPD...).
- **Datos a mano**: cinco usuarios llamados "Test Test1", que no cubren ni la variedad ni el volumen que necesitamos.
- **Generadores tipo faker**: bien para volumen, pero sin relaciones entre datos (edades que no casan con fechas de alta, importes que no cuadran con los impuestos).

Los modelos de IA añaden una opción nueva: datos sintéticos con **variedad y coherencia aparente** a partir de una descripción en lenguaje natural. "Genera 100 clientes españoles, el 10% con pedidos devueltos, importes coherentes con IVA". Y lo que devuelve, a primera vista, pinta muy bien.

### Cuándo compensa (y cuándo no).

Usar IA para generar datos compensa cuando:

- Necesitas **volumen y variedad** para pruebas de rendimiento o de visualización.
- Quieres **prototipar rápido** sin montar un generador propio.
- Los datos necesitan **narrativa**: textos de opiniones, descripciones de producto, mensajes de soporte con tono realista.

No compensa, o exige mucho más cuidado, cuando:

- El dominio tiene **reglas estrictas** (finanzas, salud): el modelo no conoce las condiciones de tu negocio y puede generar datos que no las cumplan.
- Necesitas **casos límite específicos**: el modelo tiende a lo típico, y justo lo raro que buscas es lo que menos probabilidad tiene de generar.
- Hay riesgo de **privacidad**: un modelo puede reproducir datos reales que haya memorizado, y un dato sintético que coincide con una persona real sigue siendo un problema.

### Los defectos típicos de los datos generados.

Si generas un dataset con un modelo y lo miras de cerca, encontrarás casi siempre los mismos defectos:

  1. **Duplicados encubiertos**: pide 100 registros y algunos vuelven con pequeñas variaciones.
  2. **Distribución poco realista**: todas las edades entre 25 y 45, todos los nombres igual de frecuentes, cero valores extremos.
  3. **Formatos que se cuelan**: un email con dominio `test.com`, un código postal de 4 dígitos, un teléfono inventado que podría ser de alguien real.
  4. **Incoherencias internas**: fecha de nacimiento y edad que no casan, pedido entregado antes de pagado.
  5. **Pocos casos límite**: el modelo genera lo típico, no lo raro. Los casos que se encuentran en los extremos hay que pedirlos explícitamente o generarlos aparte.

La conclusión práctica: los datos generados por IA son **materia prima**, no producto terminado. Necesitan una validación antes de entrar en tu entorno de pruebas.

### Manos a la obra: validar antes de usar.

Vamos a escribir una validación mínima en TypeScript. Este es el dataset de clientes que nos habría devuelto el modelo (fíjate en que parece razonable a simple vista):

```typescript
interface Person {
  name: string
  email: string
  age: number
  postalCode: string
}

const generatedData: Person[] = [
  { name: 'Ana García', email: 'ana.garcia@example.com', age: 34, postalCode: '41001' },
  { name: 'Luis Pérez', email: 'luis.perez@example.com', age: 28, postalCode: '28013' },
  { name: 'Ana García', email: 'ana.garcia@example.com', age: 34, postalCode: '41001' }, // duplicate
  { name: 'María Test', email: 'maria@test.com', age: 25, postalCode: '08001' },         // test domain
  { name: 'Joven Demasiado', email: 'joven@example.com', age: 15, postalCode: '46001' }, // underage
  { name: 'Sin Codigo', email: 'sincp@example.com', age: 41, postalCode: '123' },        // invalid postal code
]
```

Y las reglas que debe cumplir cualquier dataset antes de entrar en nuestros tests:

```typescript
interface Rule {
  name: string
  check: (data: Person[]) => boolean
}

const rules: Rule[] = [
  { name: 'no duplicate records',
    check: (ds) => new Set(ds.map((d) => d.email)).size === ds.length },
  { name: 'no test email domains (test.com, example.org...)',
    check: (ds) => ds.every((d) => !d.email.endsWith('@test.com')) },
  { name: 'age between 18 and 99',
    check: (ds) => ds.every((d) => d.age >= 18 && d.age <= 99) },
  { name: '5-digit postal code',
    check: (ds) => ds.every((d) => /^\d{5}$/.test(d.postalCode)) },
]

let failures = 0
for (const rule of rules) {
  const ok = rule.check(generatedData)
  if (!ok) failures++
  console.log(`${ok ? 'PASS' : 'FAIL'} ${rule.name}`)
}
console.log(`\n${failures} rule(s) failed: the dataset is NOT ready to use`)
```

Al ejecutarlo (`node validar.ts`, con Node 22.18 o superior, que ya entiende TypeScript directamente), el dataset que en teoría era bueno y generado correctamente empieza a dar fallos:

```
FAIL no duplicate records
FAIL no test email domains (test.com, example.org...)
FAIL age between 18 and 99
FAIL 5-digit postal code

4 rule(s) failed: the dataset is NOT ready to use
```

![Las cuatro reglas fallan sobre el dataset generado por IA](/img/blog-images/new-posts/2027/01/104-validacion-dataset-fail.png)

*Salida real de `node validar.ts` sobre el dataset del ejemplo.*

El patrón es el de siempre en QA: **definir los criterios de aceptación antes de generar**. Si sabes qué debe cumplir el dato, validarlo es fácil con un código no muy complejo. Si no lo sabes, no hay generadores que te ayuden a saber si esos datos son o no correctos.

### Buenas prácticas para generar datos con IA.

Antes de terminar este artículo, me gustaría dejaros algunas cosas que yo considero buenas prácticas como consejo a vuestros yos del futuro (o a mi yo del futuro):

- Os recomiendo pedir por partes: primero el esquema y las reglas, revisarlas, y luego los datos. Es más fácil corregir un esquema que 500 registros.
- También os recomiendo pedir los casos límite ("incluye edades de 0, 17 y 99, un CP con letras, un email sin @"): si no se los pides explícitamente, probablemente no te los va a incluir, la IA no es tan inteligente aún (¿o sí? 🤔).
- Valida siempre con código, no a ojo: esquema, duplicados, rangos, formatos y coherencia interna. Y si necesitas una distribución concreta (un 10% de devoluciones, por ejemplo), cuéntala y no asumas que el modelo ha cumplido el porcentaje.
- Y nunca mezcles datos generados con datos reales sin revisar: un teléfono o DNI generado puede pertenecer a alguien. Usa rangos reservados para pruebas siempre que existan.

* * *

Y hasta aquí la cuarta entrega. En la siguiente cerramos la serie con lo más práctico de todo: una checklist para auditar lo que la IA escribe antes de dejarlo entrar en nuestro pipeline. ¡Nos leemos en la siguiente entrada!
