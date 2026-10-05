# Una QA en Apuros - blog

A personal blog about QA, testing and automation.

🔗 https://unaqaenapuros.com/

A static site built with [Hugo](https://gohugo.io/) and the
[Stack](https://stack.jimmycai.com/) theme, hosted on GitHub Pages.

## Local development

```bash
git submodule update --init --recursive
brew install hugo   # extended version 0.164.0
hugo server -D      # http://localhost:1313
```

## New post

```bash
hugo new content posts/mi-post-nuevo.md
```

To **schedule** a future post, set a future date in the front matter's
`date:` field and push as usual. The external cron-job.org trigger calls
GitHub Actions at 09:30 (Madrid time). GitHub Actions does not guarantee
that scheduled workflows run at an exact time.

## Deployment

Automatic deployment through [.github/workflows/deploy.yml](.github/workflows/deploy.yml)
on every push to `main` and through `repository_dispatch` from cron-job.org
for scheduled posts. Manual runs through `workflow_dispatch` are also supported.
