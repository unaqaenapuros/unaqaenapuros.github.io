# Una QA en Apuros — blog

Static site generated with [Hugo](https://gohugo.io/) + the [Stack](https://stack.jimmycai.com/) theme, deployed on GitHub Pages. Migrated from [unaqaenapuros.wordpress.com](https://unaqaenapuros.wordpress.com/).

See the full migration plan in [MIGRATION_PLAN.md](MIGRATION_PLAN.md).

## Local development

```bash
brew install hugo   # one time only
git clone --recurse-submodules <this-repo-url>
cd unaqaenapuros.github.io
hugo server -D       # http://localhost:1313
```

## Create a new post

```bash
hugo new content posts/my-new-post/index.md
```

To **schedule** a future publication, just set a future date in the
front matter's `date:` and commit/push as usual — the GitHub Actions
workflow rebuilds the site every hour (`schedule` cron in
[.github/workflows/deploy.yml](.github/workflows/deploy.yml)) and the
post will show up on its own once its date arrives. No need to touch
anything that day.

Articles are written in Spanish; everything else in the site (menus,
dates, widgets, footer) is in English, driven by
`defaultContentLanguage = "en"` in [hugo.toml](hugo.toml).

## Deployment

Automatic via [.github/workflows/deploy.yml](.github/workflows/deploy.yml)
on every push to `main` (and every hour, for scheduled posts).

## Project layout

- [hugo.toml](hugo.toml) — single-file site config (theme, menu, sidebar, analytics).
- [layouts/_partials/head/custom.html](layouts/_partials/head/custom.html) — small CSS override (bigger avatar, background behind the logo) + the Umami analytics script (production builds only).
- `assets/img/blog_logo.png` — source logo (transparent background).
- `assets/img/avatar-square.png` — square version of the logo used as avatar/favicon.
- `assets/icons/linkedin.svg` — LinkedIn icon (not bundled with the Stack theme).
- `themes/stack` — [Stack theme](https://github.com/CaiJimmy/hugo-theme-stack), tracked as a git submodule.

## Pending manual steps (only you can do these)

- [ ] **Enable GitHub Pages**: in the GitHub repo → *Settings → Pages →
      Source: "GitHub Actions"*.
- [ ] **Export WordPress content**: *Settings → Tools → Export → All
      content* (generates an XML file). Save it and let me know so I
      can convert it to Markdown with `wp2hugo` and migrate the posts.
- [ ] **Auto-publish to LinkedIn**: the site already exposes an RSS feed
      at `/index.xml`. Connect it to [Buffer](https://buffer.com) (free
      plan, RSS → LinkedIn) or [IFTTT](https://ifttt.com) ("New RSS
      item" → "Share a LinkedIn post" applet) once the site is deployed
      and the URL is public.
- [ ] **Custom domain** (optional): if you want to use a custom domain
      instead of `unaqaenapuros.github.io`, let me know and we'll set up
      the `CNAME` and `baseURL`.
