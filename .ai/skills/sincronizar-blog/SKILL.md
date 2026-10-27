---
name: sincronizar-blog
description: Relación entre este repo de publicación del blog UnaQAEnApuros y el repo de escritura de la autora (UnaQAEnApuros). Úsala siempre que la autora pida pasar una entrada de un repo al otro, llevar cambios de uno a otro, revisar si una entrada está igual en los dos, o preparar entradas e imágenes para publicar.
---

# Sincronizar los dos repos del blog

El blog **UnaQAEnApuros** vive en dos repos:

- **Este repo (publicación)**: sitio Hugo con el contenido final que se publica.
- **El repo de escritura, `UnaQAEnApuros`**: privado. Ahí están los borradores, las imágenes por usar y las skills de redacción.

Los dos clones están siempre en la misma carpeta, uno al lado del otro, así que el repo de escritura está en `../UnaQAEnApuros`.

## Cómo trabajar

Las instrucciones completas están en la copia de esta skill del repo de escritura: `../UnaQAEnApuros/.ai/skills/sincronizar-blog/SKILL.md`. **Léela antes de hacer nada** y síguela. Si no encuentras el repo de escritura en `../`, pregunta a la autora antes de seguir.

Lo que hay en este repo:

- `content/posts/new-posts/NNN-slug.md`: la entrada final que se publica. El nombre del fichero es el mismo en los dos repos y es la clave para emparejar las entradas.
- `static/img/blog-images/new-posts/YYYY/MM/fotoNN.jpg`: portadas ya convertidas (JPG de 1200x800).
- `scripts/validate_frontmatter.py`: validador del front matter. Ejecútalo desde la raíz del repo después de cualquier cambio en las entradas.

## Reglas

- La versión final de cada entrada es la de este repo.
- **Los commits, los push y los pull requests los hace la autora.** No hagas commit en ninguno de los dos repos salvo que te lo pida.
- Este repo es **público**: no copies aquí la URL ni la estructura interna del repo de escritura, ni el contenido completo de su copia de esta skill.
