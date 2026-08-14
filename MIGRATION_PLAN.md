# Migración WordPress → GitHub Pages: pendiente

La migración a Hugo + Stack ya está en producción en
https://unaqaenapuros.github.io/ (contenido migrado, analíticas,
publicación programada y auto-publicación en LinkedIn vía Make, todo
funcionando). WordPress ya no publica nada nuevo. Este fichero se
borrará en cuanto quede lo de abajo resuelto.

## Pendiente para mañana

- [ ] **Crear los secrets de email en GitHub** (Settings → Secrets and
      variables → Actions → New repository secret):
      - `GMAIL_ADDRESS` → `estefafdez@gmail.com`
      - `GMAIL_APP_PASSWORD` → contraseña de aplicación generada en
        https://myaccount.google.com/apppasswords (requiere
        verificación en 2 pasos activada en la cuenta de Google).
- [ ] **Comprobar que llega el email**: tras crear los secrets y
      mergear [.github/workflows/deploy.yml](.github/workflows/deploy.yml),
      lanzar el workflow manualmente (pestaña Actions → "Build and
      deploy to GitHub Pages" → "Run workflow") y confirmar que llega
      el correo de `notify` a la bandeja de entrada.
- [ ] **QA final**: revisar que no queden imágenes rotas ni enlaces
      internos rotos en los posts migrados, y comprobar
      `sitemap.xml`/`robots.txt`.

## Pendiente sin fecha

- [ ] **Dominio propio** (opcional): si en algún momento quieres usar
      un dominio distinto a `unaqaenapuros.github.io`, hay que
      configurar `CNAME` y `baseURL` en [hugo.toml](hugo.toml).

## Decidido

- Comentarios de WordPress: **no se migran**, se quedan fuera.
