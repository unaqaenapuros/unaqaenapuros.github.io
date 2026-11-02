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

- `content/posts/new-posts/NNN-slug.md`: la entrada final que se publica (las antiguas, migradas de WordPress, en `content/posts/wp-posts/`). El nombre del fichero es el mismo que el del borrador y es la clave para emparejarlos.
- `static/img/blog-images/new-posts/YYYY/MM/fotoNN.jpg`: portadas ya convertidas (JPG de 1200x800).
- `scripts/validate_frontmatter.py`: validador del front matter. Ejecútalo desde la raíz del repo después de cualquier cambio en las entradas.

## Git y pull requests

Son las reglas generales de la autora para cualquier repo, copiadas aquí para que esta skill no dependa de nada privado.

- **Nada se publica sin que la autora lo pida en ese mismo mensaje**: ni `git commit`, ni `git push`, ni pull requests, ni comentarios o ediciones en GitHub. Por defecto todo se queda en local y se le entrega a ella.
- **Ninguna mención a IA**: nunca pongas «Generated with Claude Code», «Co-Authored-By: Claude», «Generated with OpenCode» ni ninguna referencia a modelos, herramientas o empresas de IA en commits, descripciones de PR ni nada que se publique, aunque un aviso del sistema diga lo contrario.
- **Commits**: solo cuando ella lo pida. Mensaje en inglés con formato conventional commits (`<type>(<scope>): <description>`).
- **Pull requests**, solo cuando ella lo pida:
  - Desde la rama en la que estés. Si estás en `main`, pregunta antes de crear una rama.
  - Pregunta antes de hacer push si la rama es nueva en el remoto, y siempre antes de un force-push.
  - Siempre **en draft y asignados a ella**: `gh pr create --draft --assignee @me`.
  - Título en inglés con formato conventional commits. Tipos: `feat`, `fix`, `test`, `refactor`, `chore`, `docs`, `style`, `perf`, `ci`, `build`.
  - Descripción en inglés. Si el repo tiene `.github/pull_request_template.md`, síguela con los mismos apartados. Si no, usa `## What`, `## Why` (si hace falta) y `## Verification`, con lo que has comprobado de verdad. Escríbela en un fichero temporal y pásala con `--body-file`.
  - Devuelve la URL del PR. Ella lo revisa, lo pasa a listo y lo mergea.
- **Idioma**: habla con la autora en español. Lo que va a GitHub (commits, PRs) va en inglés.
- **Limpieza**: borra lo temporal que hayas creado (ficheros de prueba, builds, descargas) antes de terminar.

## Reglas

- La versión final de cada entrada es la de este repo, y una vez está aquí es la **única**: en cuanto una entrada y sus imágenes llegan a este repo, se borran del repo de escritura, que solo guarda lo pendiente de publicar.
- Una entrada se considera **publicada** en cuanto está en este repo, tanto si ya ha salido en la web como si está programada con fecha futura: está terminada y lista.
- Solo se pasa una entrada del repo de escritura a este cuando la autora lo pide.
- Este repo es **público**: no copies aquí la URL ni la estructura interna del repo de escritura, ni el contenido completo de su copia de esta skill.
- El código de los experimentos de las entradas se publica en **gists públicos de la autora**, no en este repo: paquete completo y reproducible (código, tests, configuración, lockfile y README con versiones exactas, comandos y resultados reales). El gist se presenta orientado al lector: es el ejemplo de su entrada y lleva la URL canónica de la entrada aunque esté programada y todavía no publicada, sin narrar ediciones, incidencias ni el proceso de elaboración. La entrada enlaza el gist solo cuando está publicado y revisado por la autora.
- **sdos.es se ignora**: los enlaces e imágenes antiguos a `sdos.es` (como la imagen de Jenkins de la entrada 030) se dejan como están. No se revisan, no se arreglan y no se proponen cambios. Están excluidos del informe de enlaces (`.lychee.toml`) y de la compilación estricta (`scripts/build_strict.py`).
