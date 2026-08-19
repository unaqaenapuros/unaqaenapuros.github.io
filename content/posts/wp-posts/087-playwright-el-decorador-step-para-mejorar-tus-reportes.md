---
title: '087 – Playwright: El decorador @step() para mejorar tus reportes.'
date: '2026-06-29T07:01:00+00:00'
url: /2026/06/29/087-playwright-el-decorador-step-para-mejorar-tus-reportes/
image: /img/blog-images/wp-posts/2026/05/foto76.png
categories:
- automation
- best-practices
- code-quality
- ai
- playwright
- qa
tags:
- testing
author: estefafdez
---
¡Hola a todos!

Seguimos con la serie de Playwright. En esta entrada vamos a hablar de algo que marca una gran diferencia a la hora de leer los reportes y las trazas de nuestros tests: el **decorador `@step()`**. Si usas **Page Objects** en tus tests, seguro que has visto alguna vez un reporte lleno de acciones de bajo nivel que cuesta seguir. Hoy vemos cómo solucionarlo de forma elegante. ¡Empezamos!

### El problema: reportes difíciles de leer.

Cuando usamos el patrón **Page Object Model** en Playwright, encapsulamos las acciones de la página en clases reutilizables. Esto está genial para mantener el código organizado, pero tiene un efecto secundario no tan bueno en los reportes y trazas: en lugar de ver un paso legible como _"Log in with john.doe"_, vemos una lista interminable de acciones de bajo nivel como _fill_, _click_, _goto_...

Algo así:

```
▶ fill("Username", "john.doe")
▶ fill("Password", "secret123")
▶ click(button "Sign in")

```

Esto es una **pared de acciones** que dificulta entender qué estaba haciendo el test cuando algo falla. Especialmente en entornos de **CI/CD**, donde dependemos del reporte para diagnosticar problemas sin poder ver el navegador en directo.

### La solución: `test.step()`.

Playwright nos ofrece `test.step()` para agrupar acciones bajo un nombre descriptivo. Así, en lugar de ver las acciones individuales, vemos un único paso con un nombre que tiene significado:

```
test('login test', async ({ page }) => {
  await test.step('Log in with john.doe', async () => {
    await page.getByLabel('Username').fill('john.doe');
    await page.getByLabel('Password').fill('secret123');
    await page.getByRole('button', { name: 'Sign in' }).click();
  });
});

```

El resultado en el reporte es mucho más limpio:

```
▶ Log in with john.doe

```

El problema es que si tenemos Page Objects con muchos métodos, tener que envolver cada llamada manualmente en `test.step()` en todos los tests es **tedioso y propenso a errores por olvidarte de ponerlo**.

### La solución elegante: el decorador `@step()`.

Aquí es donde entra el **decorador `@step()`**. Un decorador en TypeScript es una función que se aplica a una clase, método o propiedad para modificar su comportamiento. Con `@step()`, podemos hacer que cualquier método de un Page Object se registre automáticamente como un paso con nombre en los reportes y trazas de Playwright, sin tener que tocar los tests.

#### Implementación del decorador.

La implementación del decorador es sencilla. La podemos poner en un fichero de utilidades compartido, por ejemplo `utils/decorators.ts`:

```
import { test } from '@playwright/test';

export function step(stepName?: string) {
  return function decorator(
    target: Function,
    context: ClassMethodDecoratorContext
  ) {
    return function replacementMethod(this: any, ...args: any[]) {
      // Si hay nombre personalizado, resolvemos los parámetros de la plantilla
      const name = stepName
        ? resolveStepName(stepName, context.name as string, args, target)
        : `${this.constructor.name}.${context.name as string}`;

      return test.step(name, async () => {
        return await target.call(this, ...args);
      });
    };
  };
}

function resolveStepName(
  template: string,
  methodName: string,
  args: any[],
  originalMethod: Function
): string {
  // Extraemos los nombres de los parámetros de la firma del método
  const paramNames = getParamNames(originalMethod);
  return template.replace(/\{\{(\w+)\}\}/g, (_, paramName) => {
    const index = paramNames.indexOf(paramName);
    return index !== -1 ? String(args[index]) : `{{${paramName}}}`;
  });
}

function getParamNames(func: Function): string[] {
  const funcStr = func.toString();
  const result = funcStr
    .slice(funcStr.indexOf('(') + 1, funcStr.indexOf(')'))
    .match(/([^\s,]+)/g);
  return result ?? [];
}

```

#### Cómo usarlo en los Page Objects.

Una vez tenemos el decorador, su uso es muy simple. Lo importamos y lo añadimos encima de cada método que queremos que aparezca como paso en los reportes:

```
import { step } from '../utils/decorators';

class LoginPage {
  @step('Log in with {{username}}')
  async logIn(username: string, password: string) {
    await this.page.getByLabel('Username').fill(username);
    await this.page.getByLabel('Password').fill(password);
    await this.page.getByRole('button', { name: 'Sign in' }).click();
  }

  @step() // Sin nombre: usa "ClassName.methodName" por defecto
  async navigateTo() {
    await this.page.goto('/login');
  }
}

```

Hay dos formas de usar el decorador:

- **Con nombre personalizado**: `@step('Log in with {{username}}')`. El nombre puede incluir **plantillas de parámetros** con la sintaxis `{{nombreParametro}}`, que se resuelven con los valores reales en tiempo de ejecución. En el ejemplo, `{{username}}` se sustituye por el valor concreto que le pasemos al método, como `john.doe`.
- **Sin argumentos**: `@step()`. En este caso, el nombre del paso se genera automáticamente con el formato `NombreClase.nombreMetodo`, por ejemplo `LoginPage.navigateTo`.

#### Resultado en el reporte.

Con el decorador en su sitio, el reporte y el Trace Viewer muestran pasos con nombre legibles, en lugar de la lista de acciones de bajo nivel:

```
▶ LoginPage.navigateTo
▶ Log in with john.doe

```

Esto es especialmente valioso cuando los tests fallan en **CI/CD**: de un vistazo sabemos en qué paso de negocio ocurrió el problema, sin tener que descifrar una secuencia de clicks y fills.

### Un apunte sobre los decoradores en TypeScript.

Para usar decoradores en TypeScript necesitamos tener habilitada la opción `experimentalDecorators` en el `tsconfig.json`. En proyectos con Playwright, esta opción suele estar disponible. La añadimos así:

```
{
  "compilerOptions": {
    "experimentalDecorators": true
  }
}

```

En versiones modernas de TypeScript (5.x), los decoradores siguen un nuevo estándar TC39 Stage 3 que no requiere este flag, pero la sintaxis es ligeramente diferente. La implementación que hemos visto es compatible con esta nueva API de decoradores.

### Conclusión.

- Los **Page Objects** mejoran la organización del código, pero pueden hacer los reportes difíciles de leer.
- `test.step()` permite agrupar acciones bajo un nombre descriptivo, pero aplicarlo manualmente en todos los tests es tedioso.
- El **decorador `@step()`** automatiza este proceso: basta con decorar los métodos del Page Object una sola vez.
- Con la sintaxis `{{paramName}}` en el nombre del paso, el reporte muestra los **valores reales** usados en cada ejecución, no solo un nombre genérico.
- Esto mejora enormemente la legibilidad de los reportes y trazas, especialmente en entornos de **CI/CD**.

* * *

Y hasta aquí nuestra entrada sobre el decorador `@step()` de Playwright. ¡Nos leemos en la siguiente entrada!
