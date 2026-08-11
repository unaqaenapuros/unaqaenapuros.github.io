# Migration plan: unaqaenapuros.wordpress.com → unaqaenapuros.github.io

## Goal
Migrate the blog from WordPress to a static site hosted on GitHub Pages (this repo), with:
- Simple installation and deployment
- Automatic publishing to LinkedIn when a post goes live
- Scheduled publications (future-dated posts)
- Visit statistics

## Confirmed decisions (2026-08-11)
- SSG/theme: **Hugo + Stack** (tried Blowfish and LoveIt first, settled on Stack)
- LinkedIn: **RSS → Buffer/IFTTT**
- Analytics: **Umami Cloud**
- Site language: interface in **English**, blog articles in **Spanish**
- Blog name ("Una QA en Apuros") kept as-is, not translated

## Implementation status (2026-08-11)
- ✅ Phase 1 (scaffold): Hugo + Stack installed and working in this repo
  (as a git submodule, see [hugo.toml](hugo.toml)).
- ✅ Phase 3 (deployment): GitHub Actions workflow ready in
  `.github/workflows/deploy.yml` (build + deploy to Pages).
- ✅ Phase 5 (scheduling): solved with the `schedule` cron in the same
  workflow — no separate piece needed.
- ✅ Phase 4 (analytics): Umami Cloud wired up via a script tag in
  [layouts/_partials/head/custom.html](layouts/_partials/head/custom.html)
  (loads only on production builds, not in local dev).
- ⚙️ Phase 6 (LinkedIn): RSS already generated (`/index.xml`), still
  need to connect Buffer/IFTTT once the site is published.
- ⏳ Phase 2 (content migration): pending the WordPress XML export —
  see the manual steps checklist in the README.
- ⏳ Phase 0/7: enable GitHub Pages, review real links/images, final QA
  and launch.

Details and actionable checklist in [README.md](README.md).

## Theme trial

Before settling on the final theme, three options were tried locally
(each in an isolated git worktree, so `main` was never at risk):

| Theme | Verdict |
|---|---|
| Blowfish | Discarded |
| LoveIt | Discarded |
| **Stack** | **Chosen** — card-style sidebar layout, clean and readable |

## Recommended stack

| Piece | Choice | Why |
|---|---|---|
| Site generator | **Hugo** | Single binary, no dependencies (no Ruby/Node required), builds in seconds, has native support for "future posts" (the basis for scheduling) |
| Theme | **Stack** | Open source, easy to install as a submodule, card-style sidebar layout |
| Hosting | **GitHub Pages** (we already have the `unaqaenapuros.github.io` repo) | Free, already matches the repo name |
| CI/CD | **GitHub Actions** | Automatic build and deploy on every push, plus a scheduled build (cron) to publish future-dated posts |
| Analytics | **Umami Cloud** (open source) | Lightweight, no cookies, fits the "open source" requirement |
| LinkedIn | **RSS → Buffer / IFTTT** (fast) or **official LinkedIn API** (more control, more red tape) | See the risks section |

## Phases

### Phase 0 — Preparation
- Export the blog from WordPress: `Settings → Tools → Export` (full XML).
- Download all images/media (WordPress exports links, not always the files themselves).
- Confirm the domain: do we keep `unaqaenapuros.github.io` or is there a custom domain to point?

### Phase 1 — Site scaffold
- Install Hugo (`brew install hugo`).
- `hugo new site .` on this repo, add the Stack theme as a submodule.
- Configure `hugo.toml` (title, English interface language, menu, RSS, sitemap).

### Phase 2 — Content migration
- Use **wp2hugo** (`github.com/bep/wp2hugo`) to convert the WordPress XML directly into Markdown + Hugo front matter.
- Manually review: broken images, WordPress shortcodes, internal links.
- Create redirects from the old WordPress URLs to the new ones (`aliases` in front matter) to avoid losing SEO.

### Phase 3 — Deployment
- GitHub Actions workflow that installs Hugo extended and runs
  `actions/deploy-pages`.
- Enable GitHub Pages on the repo, pointing to Actions.
- Verify HTTPS and (if applicable) a custom domain via `CNAME`.

### Phase 4 — Analytics
- Sign up for Umami Cloud (free).
- Add the tracking script to
  [layouts/_partials/head/custom.html](layouts/_partials/head/custom.html)
  (Stack has no built-in analytics provider config, unlike Blowfish).

### Phase 5 — Scheduled publications
- Hugo no longer publishes posts with a future `date` by default.
- A **workflow with a cron schedule** (every hour) rebuilds + redeploys the site → scheduled posts "show up on their own" once their date arrives, with no manual action.

### Phase 6 — Auto-publish to LinkedIn
- Hugo generates RSS automatically (`/index.xml`).
- Connect that RSS to **Buffer** (free plan, RSS→LinkedIn) or **IFTTT** (RSS→LinkedIn applet, free) → every new post publishes itself to LinkedIn.
- A more powerful but more time-costly alternative: the official LinkedIn API (`w_member_social`), which gives full control over the post's text/image but requires:
  - Creating a LinkedIn Developer App.
  - Requesting the "Share on LinkedIn" product (LinkedIn has significantly restricted this access since 2023, it can take a while or be denied for personal use).
  - Refreshing the OAuth token every 60 days.
  - A GitHub Actions step that calls the API after every deploy.

### Phase 7 — QA and launch
- Verify redirects, sitemap.xml, robots.txt, RSS.
- Check old posts, images, comments (if migrated via giscus/utterances).
- Redirect/announce on WordPress pointing to the new blog.

## Estimated timeline
| Phase | Approx. time |
|---|---|
| 0-1 Scaffold | 1 day |
| 2 Content migration | 1-3 days (depending on number of posts) |
| 3 Deployment | half a day |
| 4 Analytics | 1 hour |
| 5 Scheduling | half a day |
| 6 LinkedIn | half a day (RSS) / 2-3 days (official API) |
| 7 QA and launch | 1 day |

## Risks / pending decisions
- **LinkedIn API**: restricted access for personal apps; the RSS→Buffer/IFTTT route is much faster and more reliable in the short term.
- **WordPress comments**: if you want to keep them, need to decide on a system (giscus via GitHub Discussions, utterances, or drop them).
- **Custom domain**: if there is one, DNS (CNAME) needs to be configured before launch.
