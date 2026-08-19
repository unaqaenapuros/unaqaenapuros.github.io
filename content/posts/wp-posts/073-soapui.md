---
title: 073 - SoapUI
date: '2021-05-12T07:00:00+00:00'
url: /2021/05/12/073-soapui/
image: /img/blog-images/wp-posts/2021/04/foto70.png
categories:
- mobile-apps
- automation
- best-practices
- ci
- code-quality
- qa
- test-types
tags:
- integration-testing
- soapui
- testing
author: estefafdez
---
¡Hola a todos!

Antes de nada muchas gracias a todos por leerme y por seguir este blog desde el principio apoyando y compartiendo su contenido por las redes sociales. La verdad es que es un honor para mi ser capaz de ayudaros a todos y espero que toda la documentación que tengo por aquí os ayude a crecer y a mejorar como QAs.

Ahora si... ¡Comenzamos!

{{< figure src="/img/blog-images/wp-posts/2021/04/83.jpg?w=1024" alt="" caption="" >}}

## ¿Qué es SoapUI?

SoapUI es una herramienta de gran alcance diseñada para ayudar en la prueba y el desarrollo de aplicaciones. Permite efectuar el testeo de la web, con docenas de características, incluyendo una interfaz simple, fácil e intuitiva. Permite la utilización de métodos de captura y repetición, siendo una herramienta de gran ayuda en la realización de pruebas de carga de gran alcance, informes detallados, gráficos, etc…

{{< figure src="/img/blog-images/wp-posts/2021/04/84.png?w=1024" alt="" caption="" >}}

## Ventajas de usar SoapUI.

Entre las numerosas ventajas que posee la aplicación (muchas de las funcionalidades descritas anteriormente también se pueden considerar como ventajas) citamos:

- Existe una versión libre que cubre las necesidades de test básicas.
- Nos permite generar con facilidad el esqueleto de una petición.
- Permite estructurar las pruebas de servicios en proyectos, permitiendo agruparlos de una manera lógica. Además cada proyecto se guarda como un fichero XML, facilitando la incorporación y seguimiento a través de nuestro sistema de control de versiones (subversion, CVS…).
- Fácil de usar.
- Permite generar proxies de los servicios con distintos frameworks existentes (Jaxrpc, Axis…).
- Permite la importación de colecciones de Postman

## Inconvenientes de usar SoapUI.

Si tenemos que destacar algún inconveniente de esta aplicación sería las numerosas funcionalidades innecesarias para nuestro propósito.

## ¿Cuáles son sus principales funcionalidades?

Esta herramienta es bastante completa para pruebas funcionales y de carga. Posee numerosas funcionalidades:

- Incorpora un monitor SOAP para capturar y analizar el tráfico.
- Inspecciona Web Services WSDL y REST (tanto WADL como WADLess) y los visualiza jerárquicamente.
- Genera automáticamente los tests y las peticiones SOAP de las operaciones definidas en el descriptor WSDL o WADL.
- Permite verificar la conformidad de un WSDL según los estándares WS-I\*.
- Opcionalmente, puede utilizarse el scripting de Groovy para que el comportamiento de los tests sea dinámico.
- Soporta varios métodos de autentificación: Basic, Digest, WS-Security y NTLM Web Service.
- Soporta diferentes tecnologías de ficheros adjuntos: MTOM, SOAP con Attachments, ficheros Inline para WSDL y MIME Attachments para REST.
- Verificación del contenido de mensajes con Xpath y Xquery.
- Versatilidad en la configuración del test de carga, pudiendo indicar el límite (en tiempo o peticiones), el número de threads de ataque, el método HTTP de la petición (POST, GET ...).
- Permite exponer Web Services de simulación (o mocking) con el contenido de respuesta personalizable.

Y vosotros...¿utilizáis SoapUI en vuestro día a día?

¡Nos leemos en la siguiente entrada!
