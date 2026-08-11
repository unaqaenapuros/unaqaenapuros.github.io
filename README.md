# Una QA en apuros — blog

Sitio estático generado con [Hugo](https://gohugo.io/) + tema [Blowfish](https://blowfish.page/), desplegado en GitHub Pages. Migrado desde [unaqaenapuros.wordpress.com](https://unaqaenapuros.wordpress.com/).

Ver el plan de migración completo en [MIGRATION_PLAN.md](MIGRATION_PLAN.md).

## Desarrollo local

```bash
brew install hugo   # una sola vez
git clone --recurse-submodules <url-de-este-repo>
cd unaqaenapuros.github.io
hugo server -D       # http://localhost:1313
```

## Crear un post nuevo

```bash
hugo new content posts/mi-post-nuevo/index.md
```

Para **programar** una publicación futura, basta con poner una fecha
futura en `date:` del front matter y hacer commit/push como siempre — el
workflow de GitHub Actions rebuilda el sitio cada hora (`schedule` cron
en [.github/workflows/deploy.yml](.github/workflows/deploy.yml)) y el
post aparecerá solo en cuanto llegue su fecha. No hace falta volver a
tocar nada ese día.

## Despliegue

Automático vía [.github/workflows/deploy.yml](.github/workflows/deploy.yml)
en cada push a `main` (y cada hora, para las publicaciones programadas).

## Pasos manuales pendientes (solo tú puedes hacerlos)

- [ ] **Activar GitHub Pages**: en el repo de GitHub → *Settings → Pages →
      Source: "GitHub Actions"*.
- [ ] **Exportar el contenido de WordPress**: *Ajustes → Herramientas →
      Exportar → Todo el contenido* (genera un XML). Guárdalo y avísame
      para convertirlo a Markdown con `wp2hugo` y migrar los posts.
- [ ] **Estadísticas (Umami)**: crear cuenta gratis en
      [cloud.umami.is](https://cloud.umami.is), añadir el sitio, copiar el
      `website id` y pegarlo en `[umamiAnalytics] websiteid = "..."`
      dentro de [config/_default/params.toml](config/_default/params.toml).
- [ ] **Auto-publicación en LinkedIn**: el sitio ya expone RSS en
      `/index.xml`. Conectarlo en [Buffer](https://buffer.com) (gratis,
      RSS → LinkedIn) o [IFTTT](https://ifttt.com) (applet "New RSS item"
      → "Share a LinkedIn post") una vez el sitio esté desplegado y la
      URL sea pública.
- [ ] **Enlaces reales**: sustituir los placeholders de LinkedIn/GitHub en
      [config/_default/languages.es.toml](config/_default/languages.es.toml)
      y [config/_default/menus.es.toml](config/_default/menus.es.toml) por
      tus URLs reales.
- [ ] **Logo/avatar**: sustituir los SVG de marcador de posición en
      `assets/img/logo.svg` y `assets/img/author.svg` por tus imágenes
      reales.
- [ ] **Dominio propio** (opcional): si quieres usar un dominio propio en
      vez de `unaqaenapuros.github.io`, dímelo y configuramos el `CNAME`
      y el `baseURL`.
