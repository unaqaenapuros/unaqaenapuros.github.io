# Plan de migración: unaqaenapuros.wordpress.com → unaqaenapuros.github.io

## Objetivo
Migrar el blog de WordPress a un sitio estático alojado en GitHub Pages (este repo), con:
- Instalación y despliegue simples
- Publicación automática en LinkedIn al publicar un post
- Programación de publicaciones (posts con fecha futura)
- Estadísticas de visitas

## Decisiones confirmadas (2026-08-11)
- SSG/tema: **Hugo + Blowfish**
- LinkedIn: **RSS → Buffer/IFTTT**
- Estadísticas: **Umami Cloud**

## Estado de implementación (2026-08-11)
- ✅ Fase 1 (scaffold): Hugo + Blowfish instalados y funcionando en este repo.
- ✅ Fase 3 (despliegue): workflow de GitHub Actions listo en
  `.github/workflows/deploy.yml` (build + deploy a Pages).
- ✅ Fase 5 (programación): resuelta con el `schedule` cron del mismo
  workflow — no requiere pieza aparte.
- ⚙️ Fase 4 (estadísticas): config de Umami ya presente en
  `config/_default/params.toml`, falta solo pegar el `websiteid` real.
- ⚙️ Fase 6 (LinkedIn): RSS ya generado (`/index.xml`), falta conectar
  Buffer/IFTTT una vez el sitio esté publicado.
- ⏳ Fase 2 (migración de contenido): pendiente del export XML de
  WordPress — ver checklist de pasos manuales en el README.
- ⏳ Fase 0/7: activar GitHub Pages, revisar enlaces/imágenes reales,
  QA final y lanzamiento.

Detalle y checklist accionable en [README.md](README.md).

## Stack recomendado

| Pieza | Elección | Por qué |
|---|---|---|
| Generador de sitio | **Hugo** | Binario único, sin dependencias (no Ruby/Node obligatorio), build en segundos, tiene soporte nativo de "posts futuros" (base de la programación) |
| Tema | **Blowfish** (alt. más simple: **PaperMod**) | Open source, fácil de instalar como módulo/submódulo, integra analítica, SEO, RSS y comentarios sin curro extra |
| Hosting | **GitHub Pages** (ya tenemos el repo `unaqaenapuros.github.io`) | Gratis, ya encaja con el nombre del repo |
| CI/CD | **GitHub Actions** | Build y deploy automático en cada push, y build programado (cron) para publicar posts con fecha futura |
| Estadísticas | **Umami Cloud** (open source) o **GoatCounter** (100% gratis/OSS) | Ligero, sin cookies, cumple con "open source" |
| LinkedIn | **RSS → Buffer / IFTTT** (rápido) o **API oficial de LinkedIn** (más control, más burocracia) | Ver sección de riesgos |

## Fases

### Fase 0 — Preparación
- Exportar el blog desde WordPress: `Ajustes → Herramientas → Exportar` (XML completo).
- Descargar todas las imágenes/medios (WordPress exporta enlaces, no siempre los ficheros).
- Confirmar dominio: ¿nos quedamos con `unaqaenapuros.github.io` o hay dominio propio a apuntar?

### Fase 1 — Scaffold del sitio
- Instalar Hugo (`brew install hugo`).
- `hugo new site .` sobre este repo, añadir tema Blowfish como submódulo.
- Configurar `hugo.toml` (título, idioma es-ES, menú, RSS, sitemap).

### Fase 2 — Migración de contenido
- Usar **wp2hugo** (`github.com/bep/wp2hugo`) para convertir el XML de WordPress directamente a Markdown + front matter de Hugo.
- Revisar manualmente: imágenes rotas, shortcodes de WordPress, enlaces internos.
- Crear redirecciones desde las URLs antiguas de WordPress a las nuevas (`aliases` en front matter) para no perder SEO.

### Fase 3 — Despliegue
- Workflow de GitHub Actions oficial `actions/deploy-pages` + `peaceiris/actions-hugo`.
- Activar GitHub Pages en el repo apuntando a Actions.
- Verificar HTTPS y (si aplica) dominio custom vía `CNAME`.

### Fase 4 — Estadísticas
- Alta en Umami Cloud (gratis) o GoatCounter (gratis, sin cuenta compleja).
- Insertar script de tracking en el tema (Blowfish lo soporta por configuración, sin tocar HTML).

### Fase 5 — Programación de publicaciones
- Hugo ya no publica posts con `date` futura por defecto.
- Añadir un **workflow con cron** (ej. cada hora) que haga rebuild + deploy del sitio → los posts programados "aparecen solos" al llegar su fecha, sin ninguna acción manual.

### Fase 6 — Auto-publicación en LinkedIn
- Hugo genera RSS automáticamente (`/index.xml`).
- Conectar ese RSS a **Buffer** (plan gratis, RSS→LinkedIn) o **IFTTT** (applet RSS→LinkedIn, gratis) → cada post nuevo se publica solo en LinkedIn.
- Alternativa más potente pero más costosa en tiempo: API oficial de LinkedIn (`w_member_social`), que da control total del texto/imagen del post pero requiere:
  - Crear una LinkedIn Developer App.
  - Solicitar el producto "Share on LinkedIn" (LinkedIn ha restringido bastante este acceso desde 2023, puede tardar/denegarse para uso personal).
  - Refrescar el token OAuth cada 60 días.
  - Un step de GitHub Actions que llame a la API tras cada deploy.

### Fase 7 — QA y lanzamiento
- Verificar redirecciones, sitemap.xml, robots.txt, RSS.
- Comprobar posts antiguos, imágenes, comentarios (si se migran vía giscus/utterances).
- Redirigir/avisar en WordPress apuntando al nuevo blog.

## Cronograma estimado
| Fase | Tiempo aprox. |
|---|---|
| 0-1 Scaffold | 1 día |
| 2 Migración contenido | 1-3 días (según nº de posts) |
| 3 Despliegue | medio día |
| 4 Estadísticas | 1 hora |
| 5 Programación | medio día |
| 6 LinkedIn | medio día (RSS) / 2-3 días (API oficial) |
| 7 QA y lanzamiento | 1 día |

## Riesgos / decisiones pendientes
- **LinkedIn API**: acceso restringido para apps personales; la ruta RSS→Buffer/IFTTT es mucho más rápida y fiable a corto plazo.
- **Comentarios de WordPress**: si se quieren conservar, hay que decidir sistema (giscus vía GitHub Discussions, utterances, o prescindir).
- **Dominio propio**: si existe, hay que configurar DNS (CNAME) antes del lanzamiento.
