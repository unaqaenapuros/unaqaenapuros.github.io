---
title: '078 – Pruebas de rendimiento (V): Apache Jmeter.'
date: '2024-09-16T07:00:00+00:00'
url: /2024/09/16/078-pruebas-de-rendimiento-v-apache-jmeter/
image: /img/blog-images/wp-posts/2024/09/foto60.png
categories:
- automation
- best-practices
- qa
tags:
- apache
- jmeter
- performance
- testing
author: estefafdez
---
¡Hola a todos!

Volvemos a la carga para hablar de Apache Jmeter, una de las herramientas de automatización de pruebas de rendimiento más conocidas… ¿Empezamos?

## ¿Qué es Jmeter?

{{< figure src="/img/blog-images/wp-posts/2024/09/imagen.png?w=600" alt="" caption="" >}}

JMeter es un proyecto de Apache que puede ser utilizado como una herramienta de prueba de carga para analizar y medir el desempeño de una variedad de servicios, con énfasis en aplicaciones web. Con esta aplicación podemos realizar también pruebas funcionales.

{{< figure src="/img/blog-images/wp-posts/2024/09/imagen-1.png?w=1024" alt="" caption="" >}}

JMeter puede ser usado como una herramienta de pruebas unitarias para conexiones de bases de datos con JDBC, FTP, LDAP, Servicios web, JMS, HTTP y conexiones TCP genéricas. Puede también ser configurado como un monitor de peticiones HTTP (lo realmente importante para nuestro propósito), aunque es comúnmente considerado una solución ad-hoc respecto de soluciones avanzadas de monitoreo.

A veces se clasifica JMeter como herramienta de "generación de carga", pero esto no es una descripción completa de la herramienta. JMeter soporta aserciones para asegurar que los datos recibidos son correctos, por lo que es una herramienta de realización de pruebas automáticas.

Los datos generados por la herramienta para cada petición se pueden canalizar a través de un tipo de componente que proporciona la interfaz GUI llamados listeners y existe la posibilidad de crear scripts en diferentes lenguajes de programación. Podemos destacar las siguientes ventajas para el uso de esta herramienta:

- Su uso es bastante sencillo y asequible.
- Es una aplicación “Open Source” y completamente gratuita.
- Tiene gran cantidad de documentación y tutoriales disponibles.
- Posee numerosos plugins externos que complementan las funcionalidades de la herramienta.

También existen algunos inconvenientes:

- JMeter NO se comporta como un navegador (no guarda ni envía cookies, no interpreta código JavaScript...).
- La interfaz GUI y el reporte de resultados no es muy agradable.
- Es poco práctico a la hora de realizar acciones como copiar componentes.

* * *

Y hasta aquí nuestra entrada qué es Jmeter. En la siguiente entrada seguiremos con la serie de rendimiento y haremos un ejemplo utilizando Jmeter para hacer pruebas de rendimiento simples.

¡Nos leemos en la siguiente entrada!
