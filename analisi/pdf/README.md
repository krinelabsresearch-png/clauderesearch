# Report impaginato

`Krine-Labs_Analisi-di-mercato.pdf` è il documento. Si legge da solo: non
presuppone conoscenza del settore né di conversazioni precedenti, e ogni
termine tecnico è spiegato la prima volta che compare.

`report.html` è la sorgente. Per rigenerare il PDF:

```sh
node render.mjs     # produce cover.pdf e body.pdf con Chromium
```

Poi si uniscono i due file: la copertina è generata a parte perché non
porta il numero di pagina.
