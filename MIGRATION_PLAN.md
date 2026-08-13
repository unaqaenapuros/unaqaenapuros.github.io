# Migración WordPress → GitHub Pages: pendiente

La migración a Hugo + Stack ya está en producción en
https://unaqaenapuros.github.io/ (contenido migrado, analíticas,
publicación programada y auto-publicación en LinkedIn vía Make, todo
funcionando). WordPress ya no publica nada nuevo. Este fichero se
borrará en cuanto quede lo de abajo resuelto.

## Pendiente

- [ ] **Dominio propio** (opcional): si en algún momento quieres usar
      un dominio distinto a `unaqaenapuros.github.io`, hay que
      configurar `CNAME` y `baseURL` en [hugo.toml](hugo.toml).
- [ ] **QA final**: revisar que no queden imágenes rotas ni enlaces
      internos rotos en los posts migrados, y comprobar
      `sitemap.xml`/`robots.txt`. (pendiente para mañana)

## Decidido

- Comentarios de WordPress: **no se migran**, se quedan fuera.
