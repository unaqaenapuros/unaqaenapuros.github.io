---
title: 016 - SonarQube + Custom Rule.
date: '2017-06-28T07:00:33+00:00'
url: /2017/06/28/016-sonarqube-custom-rule/
image: /img/blog-images/wp-posts/2017/06/foto16.jpg
categories:
- code-quality
- qa
tags:
- custom-rules
- sonarqube
author: estefafdez
---
¡Hola a todos!

Seguimos con SonarQube y en esta ocasión tenemos un post dedicado a las Custom Rules.

Una Custom Rule o Regla Personalizada es una regla creada a través de una Rule Template (ya hablamos de ellas en nuestra anterior entrada).

Las Custom Rules se consideran como cualquier otra regla ya añadida en Sonar a la hora de analizar nuestro código, la única diferencia con las reglas predeterminadas es que las custom rules se pueden editar e incluso eliminar.

Tenemos que tener en cuenta el hecho de que eliminar una regla personalizada no la elimina completamente de sonar, sino que se marca como borrada en la base de datos para que los fallos que haya encontrado esa regla no se pierdan.

¿Qué tenemos que hacer entonces para crear una regla personalizada/Custom Rule?

1. Iniciamos sesión en sonar con un perfil de administrador (por defecto el usuario administrador es _admin/admin_).
1. Hacemos click en reglas.
1. Filtramos por template y hacemos click en show templates only.
1. Cuando tenemos la lista de plantillas, seleccionamos una de ellas del lenguaje en el que queramos crear la regla (por ejemplo Java).
1. En esta plantilla, encontramos el botón para crear una regla personalizada.

![sonar_template_create](/img/blog-images/wp-posts/2017/06/sonar_template_create.png)

Hacemos click y rellenamos el formulario con los campos de la regla:

![create_custom_rule](/img/blog-images/wp-posts/2017/06/create_custom_rule.png)

1. Nombre.
1. Clave (auto sugerida).
1. Descripción (Formato de marcas soportado).
1. Gravedad / Severidad.
1. Estado.
1. Expresión regular.
1. Mensaje.

Una vez que tenemos todos los campos completados, hacemos click en crear y ya tenemos nuestra regla personalizada creada.

Para comprobar que la regla que acabamos de definir se ha creado correctamente, buscamos el template en el que nos hemos basado y en la parte inferior, debe venir una lista con las custom rules creadas a partir de ese template donde debe aparecer la nuestra.

Y hasta aquí el post sobre custom rules. En el siguiente artículo seguiremos con SonarQube en un artículo en el que hablaremos de cómo importar un plugin que incluya reglas.

¡Hasta la siguiente entrada!.
