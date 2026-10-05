# Una QA en Apuros — blog

Blog personal sobre QA, testing y automatización.

🔗 https://unaqaenapuros.com/

Sitio estático generado con [Hugo](https://gohugo.io/) + tema
[Stack](https://stack.jimmycai.com/), publicado en GitHub Pages.

## Desarrollo local

```bash
git submodule update --init --recursive
brew install hugo   # versión extended 0.164.0
hugo server -D      # http://localhost:1313
```

## Nuevo post

```bash
hugo new content posts/mi-post-nuevo.md
```

Para **programar** una publicación futura, basta con poner una fecha
futura en `date:` del front matter y hacer push como siempre — el
disparador externo de cron-job.org llama a GitHub Actions a las 09:30
(hora de Madrid). GitHub Actions no garantiza ejecutar un cron a una hora exacta.

## Despliegue

Automático vía [.github/workflows/deploy.yml](.github/workflows/deploy.yml)
en cada push a `main` y mediante `repository_dispatch` desde cron-job.org para los posts programados.
También admite ejecución manual con `workflow_dispatch`.
