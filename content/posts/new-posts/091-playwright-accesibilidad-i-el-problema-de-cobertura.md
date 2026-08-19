---
title: '091 – Playwright: Accesibilidad I – El problema de cobertura.'
date: '2026-08-24T09:30:00+02:00'
url: /2026/08/24/091-playwright-accesibilidad-i-el-problema-de-cobertura/
image: /img/blog-images/new-posts/2026/08/foto80.png
categories:
- automation
- best-practices
- playwright
- qa
tags:
- accesibility
- testing
author: estefafdez
social_text: |
  ¿Sabías que axe y Lighthouse no detectan entre el 43 y el 70% de los errores reales de accesibilidad? Empezamos una nueva mini-serie sobre accesibilidad con Playwright: qué detectan bien las herramientas automatizadas, por qué siguen siendo imprescindibles para prevenir regresiones, y cuáles son sus límites estructurales que ninguna herramienta puede superar. Primera parte de tres.

  #Playwright #QA #TestAutomation #Accesibilidad #UnaQAEnApuros
---
¡Hola a todos!

Después de la mini-serie sobre fixtures, hoy empezamos una nueva: **accesibilidad web con Playwright**. Es un tema fundamental que, en mi experiencia, se trata de forma muy superficial en muchos proyectos. La mayoría de los equipos ejecutan un análisis con axe o miran el informe de Lighthouse, ven todo en verde y dan por hecha la accesibilidad. Pero hay un problema serio con ese enfoque: las herramientas automatizadas solo detectan entre el **30 y el 57% de los errores reales de WCAG**. En esta primera entrega vamos a entender por qué ocurre esto, si detectan bien estas herramientas y cuáles son sus límites estructurales. ¡Empezamos!

{{< figure src="/img/blog-images/new-posts/2026/08/gemini%5Fgenerated%5Fimage%5Fwx54fewx54fewx54.png?w=1024" alt="" caption="" >}}

### El gap de cobertura: lo que dice la investigación.

Esto no es una crítica a Axe, Lighthouse o cualquier herramienta que use su motor. Los propios fabricantes y la investigación independiente coinciden: existen **límites estructurales** en lo que cualquier motor de análisis automatizado puede evaluar.

Las cifras varían según la fuente, pero la conclusión es siempre la misma:

FuenteResultadoWebAIM~30% de los fallos reales de WCAG son detectables por automatizaciónW3C / WAI~20-30% de los criterios de éxito de WCAG son completamente automatizablesU.S. GSA – Sección 508Aproximadamente 1 de cada 3 problemas es detectado por tests automatizadosDeque (axe)57,38% de las violaciones conocidas detectadas al analizar páginas auditadas realesAccessible.org13% completamente automatizable, 45% parcialmente, 42% no automatizable (WCAG 2.2 AA)

La cifra de Deque es la más optimista y se obtiene de un enfoque pragmático: en lugar de calcular cuántos criterios son teóricamente automatizables, midieron cuántos defectos reales documentados habrían detectado al pasar axe-core por un conjunto amplio de páginas auditadas. Es una buena noticia relativa — en la práctica, las herramientas encuentran más de lo que la teoría sugiere. Pero incluso así, dejan una **brecha del 43%**. Podemos tener un informe completamente verde y publicar una experiencia inutilizable para muchas personas.

### Qué detectan bien las herramientas automatizadas:

Antes de hablar de limitaciones, es importante reconocer dónde son realmente útiles. Las herramientas automatizadas detectan con fiabilidad las **violaciones de reglas mecánicas**:

- Atributo `alt` ausente en imágenes.
- Campos de formulario sin etiqueta ( `<label>`).
- Ratios de contraste de color insuficientes en texto estático sobre fondo sólido.
- Ausencia del atributo `lang` en el elemento `<html>`.
- Ausencia del título del documento ( `<title>`).
- Roles ARIA inválidos o con atributos mal formados.

Son comprobaciones **estructurales**: cosas que se pueden evaluar leyendo el DOM sin necesidad de entender la intención o el contexto. Y precisamente por eso son exactamente el tipo de cosas que es fácil romper accidentalmente en una refactorización.

#### Prevención de regresiones.

La **prevención de regresiones** es donde los checks automatizados ganan su sitio en el pipeline de CI. Los defectos de accesibilidad no se anuncian solos como los bugs funcionales. Un cambio en la UI que elimina un `aria-label`, rompe el orden del foco o suprime una región landmark no lanzará ningún error ni provocará un fallo visual sin una comprobación explícita. Un análisis de Playwright captura estas regresiones introducidas silenciosamente antes de que lleguen a producción — algo que una revisión manual periódica inevitablemente pasaría por alto entre ciclos.

#### Superficie a escala.

La otra gran ventaja es la **escala**: una suite de Playwright analiza cada página en cada ejecución de CI. Una revisión manual completa lleva horas y, en la práctica, ocurre con poca frecuencia. Los checks automatizados no reemplazan la revisión manual, pero cubren terreno a una velocidad que ninguna auditoría manual puede igualar.

El objetivo no es enfrentar la automatización contra la revisión manual. Cada una aporta algo que la otra no puede. Los tests automatizados son el suelo siempre activo; la revisión manual es el pase más profundo y periódico que captura lo que la automatización no puede evaluar estructuralmente.

### Lo que las herramientas no pueden evaluar.

Aquí es donde el análisis automatizado tiene sus límites estructurales. No es un fallo de implementación: es una consecuencia de lo que significa "leer el DOM sin entender el contexto".

En las siguientes entregas de esta serie veremos en detalle cada una de estas categorías:

- **Texto de enlace ambiguo**: _"Ver más"_ pasa axe sin problemas aunque sea inútil fuera de contexto.
- **Ausencia de enlace de saltar al contenido**: los landmarks satisfacen la regla técnica, pero no ayudan a usuarios que navegan solo con teclado.
- **`aria-labelledby` vs `aria-label`**: ambos pasan los checks, pero uno puede ser la elección incorrecta para tu contexto.
- **Labels ARIA estáticos en controles con estado**: un toggle de notificaciones con `aria-label="Activar notificaciones"` pasa los checks aunque las notificaciones ya estén activas.
- **Alt text de baja calidad**: `alt="foto de producto"` pasa axe, aunque no comunique nada útil.
- **Regresiones introducidas por arreglos incorrectos**: `alt=""` es correcto para imágenes decorativas; cambiarlo a `alt="imagen decorativa"` es una regresión que ningún escáner detecta.
- **Limitaciones en contraste de color**: gradientes, fondos semitransparentes, estados de hover y focus, modo oscuro.
- **Accesibilidad de formularios**: etiquetas genéricas, instrucciones insuficientes, mensajes de error vagos.
- **Accesibilidad de teclado en componentes interactivos**: modales, acordeones y dropdowns que pasan los atributos ARIA pero fallan en la navegación real.

### Conclusión.

- Las herramientas automatizadas como axe y Lighthouse detectan entre el **30 y el 57%** de los problemas reales de accesibilidad, según la fuente consultada.
- Son muy útiles para detectar **violaciones de reglas estructurales** y para **prevenir regresiones** en CI a una escala que la revisión manual no puede alcanzar.
- Su limitación fundamental es que pueden leer el DOM pero **no pueden entender el contexto** ni evaluar si un atributo o texto es semánticamente correcto.
- El objetivo es **combinar tests automatizados con revisión manual**, no elegir entre ellos.
- En las próximas entregas veremos qué categorías de problemas se escapan a la automatización y cómo escribir tests de Playwright más inteligentes para cubrir parte de esa brecha.

* * *

Y hasta aquí esta primera entrada sobre accesibilidad con Playwright. En la siguiente entrega veremos en detalle las categorías de problemas que axe y Lighthouse no pueden detectar, con ejemplos concretos y cómo corregirlos. ¡Nos leemos en la siguiente entrada!
