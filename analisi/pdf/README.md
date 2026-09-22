# Documenti impaginati

Due PDF, due sorgenti HTML, due script di rendering.

## `Krine-Labs_Piano-di-progetto.pdf` (33 pagine)

Il documento principale. Piano di progetto costruito per reggere l'esame di
un investitore: mercato ricostruito dal basso, mappa competitiva con il costo
mensile reale dei concorrenti, economia unitaria completa, coorti e cassa,
uso dei 250.000 euro, rischi, primi novanta giorni. Formula guida: candidata C.

Sorgente: `report-piano.html`. Rendering: `node render-piano.mjs`.

## `Krine-Labs_Analisi-di-mercato.pdf` (36 pagine)

L'analisi di mercato precedente, tenuta come riferimento. Si legge da sola.

Sorgente: `report.html`. Rendering: `node render.mjs`.

## Come rigenerare

```sh
node render-piano.mjs    # oppure render.mjs
```

Ogni script produce `cover.pdf` e `body.pdf` con Chromium, poi li unisce nel
PDF finale. La copertina viene generata a parte perché non porta il numero di
pagina. I due file intermedi si possono cancellare dopo il merge.
