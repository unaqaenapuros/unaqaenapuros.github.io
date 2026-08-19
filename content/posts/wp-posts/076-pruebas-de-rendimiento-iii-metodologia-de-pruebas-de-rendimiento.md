---
title: '076 – Pruebas de rendimiento (III): Metodología de pruebas de rendimiento.'
date: '2021-11-03T08:00:00+00:00'
url: /2021/11/03/076-pruebas-de-rendimiento-iii-metodologia-de-pruebas-de-rendimiento/
image: /img/blog-images/wp-posts/2021/10/foto73.png
categories:
- automation
- best-practices
- performance
- qa
author: estefafdez
---
¡Hola a todos!

Antes de nada, bienvenidos de nuevo y perdonad el retraso en las entradas, últimamente no he tenido tiempo de sentarme y preparar nuevo material pero volvemos a la carga con más fuerza que nunca y más entradas de rendimiento... ¿Empezamos?

## Aprendiendo sobre metodologías de pruebas de rendimiento.

Según Microsoft Developer Network, la Metodología de las Pruebas de Rendimiento consiste en las siguientes actividades:

### Identificar el entorno de pruebas.

{{< figure src="/img/blog-images/wp-posts/2021/10/imagen.jpg?w=640" alt="" caption="" >}}

Identificar el entorno físico de pruebas y el entorno de producción, así como las herramientas y recursos de que dispone el equipo de prueba. El entorno físico incluye hardware, software y configuraciones de red. Tener un profundo conocimiento de todo el entorno de prueba desde el principio permite diseños más eficientes de pruebas y la planificación y ayuda a identificar problemas en las pruebas en fases tempranas del proyecto. En algunas situaciones, este proceso debe ser revisado periódicamente durante todo el ciclo de vida del proyecto.

### Identificar los criterios de aceptación de rendimiento.

{{< figure src="/img/blog-images/wp-posts/2021/10/1%5Fsclbpq23jrosw8fd4jqfua.png?w=800" alt="" caption="" >}}

Determinar el tiempo de respuesta, el rendimiento, la utilización de los recursos y los objetivos y limitaciones. En general, el tiempo de respuesta concierne al usuario, el rendimiento al negocio, y la utilización de los recursos al sistema. Además, identificar criterios de éxito del proyecto que no hayan sido recogidos por los objetivos y limitaciones, por ejemplo, mediante pruebas de rendimiento para evaluar qué combinación de la configuración da lugar a un funcionamiento óptimo.

### Planificar y diseñar las pruebas.

{{< figure src="/img/blog-images/wp-posts/2021/10/software-testing-without-requirements-survival-guide-12-638.webp?w=638" alt="" caption="" >}}

Identificar los principales escenarios, determinar la variabilidad de los usuarios y la forma de simular esa variabilidad, definir los datos de las pruebas, y establecer las métricas a recoger. Consolidar esta información en uno o más modelos de uso del sistema a implantar, ejecutarlo y analizarlo.

### Configurar el entorno de prueba.

{{< figure src="/img/blog-images/wp-posts/2021/10/test-dev-and-production-environment.jpg?w=485" alt="" caption="" >}}

Preparar el entorno de prueba, herramientas y recursos necesarios para ejecutar cada una de las estrategias, así como las características y componentes disponibles para la prueba. Asegurarse de que el entorno de prueba se ha preparado para la monitorización de los recursos según sea necesario.

### Aplicar el diseño de la prueba.

Desarrollar las pruebas de rendimiento de acuerdo con el diseño del plan.

### Ejecutar la prueba.

{{< figure src="/img/blog-images/wp-posts/2021/10/load-testing2.png?w=627" alt="" caption="" >}}

Ejecutar y monitorizar las pruebas. Validar las pruebas, los datos de las pruebas, y recoger los resultados. Ejecutar pruebas válidas para analizar, mientras se monitoriza la prueba y su entorno.

### Analizar los resultados, realizar un informe y repetirlo.

{{< figure src="/img/blog-images/wp-posts/2021/10/performancesummary1.webp?w=1024" alt="" caption="" >}}

Consolidar y compartir los resultados de la prueba. Analizar los datos, tanto individualmente, como con un equipo multidisciplinario. Volver a priorizar el resto de las pruebas y volver a ejecutarlas de ser necesario. Cuando todas las métricas estén dentro de los límites aceptados, ninguno de los umbrales establecidos han sido rebasados, y toda la información deseada se ha reunido, las pruebas han acabado para el escenario definido por la configuración.

* * *

Y hasta aquí nuestra entrada sobre metodologías de pruebas de rendimiento. En la siguiente entrada seguiremos con la serie de rendimiento y hablaremos sobre las herramientas que tenemos disponibles para este tipo de pruebas.

¡Nos leemos en la siguiente entrada!
