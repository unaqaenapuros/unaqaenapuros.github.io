# Una QA en Apuros — blog

Blog personal sobre QA, testing y automatización.

🔗 https://unaqaenapuros.github.io/

Sitio estático generado con [Hugo](https://gohugo.io/) + tema
[Stack](https://stack.jimmycai.com/), publicado en GitHub Pages.

## Desarrollo local

```bash
brew install hugo   # solo la primera vez
hugo server -D      # http://localhost:1313
```

## Nuevo post

```bash
hugo new content posts/mi-post-nuevo.md
```

Para **programar** una publicación futura, basta con poner una fecha
futura en `date:` del front matter y hacer push como siempre — el
workflow de GitHub Actions reconstruye el sitio cada hora y el post
aparece solo en cuanto llega su fecha.

## Despliegue

Automático vía [.github/workflows/deploy.yml](.github/workflows/deploy.yml)
en cada push a `main` (y cada hora, para los posts programados).
