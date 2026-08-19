---
title: 071 - Pruebas de Integración (II)
date: '2021-03-31T07:00:00+00:00'
url: /2021/03/31/071-pruebas-de-integracion-ii/
image: /img/blog-images/wp-posts/2021/02/foto68.png
categories:
- mobile-apps
- automation
- best-practices
- code-quality
- qa
- test-types
tags:
- integration
- integration-testing
author: estefafdez
---
¡Hola a todos!

En esta entrada vamos a seguir con las pruebas de integración como empezamos en la entrada anterior. Esta vez vamos a aprender qué tipos de pruebas de integración existen así como sus ventajas e inconvenientes. ¡Empezamos!

{{< figure src="/img/blog-images/wp-posts/2021/02/image-2.png?w=900" alt="" caption="" >}}

## Tipos de pruebas de integración.

Existen principalmente dos tipos de pruebas de integración:

- **No incrementales:** combinar todos los módulos y probar todo el programa en su conjunto. El resultado puede ser un poco caótico con un gran conjunto de fallos y la consiguiente dificultad para identificar el módulo (o módulos) que los provocó.
- **Incrementales:** el programa se prueba en pequeñas porciones en las que los fallos son más fáciles de detectar. Existen dos tipos de integración incremental, ascendente y descendente.
  - **Incrementales ascendente:** empieza la construcción y la prueba con los módulos atómicos, es decir, módulos de los niveles más bajos de la estructura del programa. Dado que los módulos son integrados de abajo hacia arriba, el procesamiento requerido de los módulos subordinados siempre está disponible y se elimina la necesidad de resguardo. Los pasos a dar:
    1. Se combinan los módulos de bajo nivel en grupos que realicen una subfunción específica del software.
    1. Se escribe un controlador (un programa de control de la prueba) para coordinar la entrada y salida de los casos de prueba.
    1. Se prueba el grupo.
    1. Se eliminan los controladores y se combinan los grupos moviéndose hacia arriba por la estructura del programa.
  - **Incrementales descendente:** inicia del módulo de control principal (de mayor nivel) para luego ir incorporando los módulos subordinados progresivamente. Los pasos a seguir:
    1. Se usa el módulo de control principal como controlador de la prueba, creando resguardos (módulos que simulan el funcionamiento de los módulos que utiliza el que está probando) para todos los módulos directamente subordinados al módulo de control principal.
    1. Dependiendo del enfoque e integración elegido (es decir, primero-en-profundidad, o primero-en-anchura) se van sustituyendo uno a uno los resguardos subordinados por los módulos reales.
    1. Se llevan a cabo pruebas cada vez que se integra un nuevo módulo.
    1. Tras terminar cada conjunto de pruebas, se reemplaza otro resguardo con el módulo real.

## Ventajas e inconvenientes.

Ya que hemos comentado los tipos de pruebas de integración que tenemos, nombraremos las ventajas e inconvenientes de cada una:

### Pruebas de integración incremental ascendente

**Ventajas:**

- Las entradas para las pruebas son más fáciles de crear ya que los módulos inferiores suelen tener funciones más específicas.
- Es más fácil la observación de los resultados de las pruebas puesto que es en los módulos inferiores donde se elaboran.
- Resuelve primero los errores de los módulos inferiores que son los que acostumbran tener el procesamiento más complejo, para luego nutrir de datos al resto del sistema.

**Inconvenientes:**

- Se requieren módulos impulsores, que deben escribirse especialmente y que no son necesariamente sencillos de codificar.
- El sistema como entidad no existe hasta que se agrega el último módulo.

### Pruebas de integración incremental descendente

**Ventajas:**

- Las fallas que pudieran existir en los módulos superiores se detectan en una etapa temprana.
- Permite ver la estructura del sistema desde un principio, facilitando la elaboración de demostraciones de su funcionamiento.
- Concuerda con la necesidad de definir primero las interfaces de los distintos subsistemas para después seguir con las funciones específicas de cada uno por separado.

**Inconvenientes:**

- Requiere mucho trabajo de desarrollo adicional ya que se deben escribir un gran número de módulos ficticios subordinados que no siempre son fáciles de realizar. Suelen ser más complicados de lo que aparentan.
- Antes de incorporar los módulos de entrada y salida resulta difícil introducir los casos de prueba y obtener los resultados.
- Induce a diferir la terminación de la prueba de ciertos módulos.

Y hasta aquí esta entrada sobre las pruebas de integración. En la siguiente entrada hablaremos de las herramientas que podemos utilizar para realizar este tipo de pruebas.

¡Hasta la siguiente entrada!
