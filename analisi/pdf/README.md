# Documenti impaginati

## `Krine-Labs_Piano-di-progetto.pdf`

Il piano di progetto e la richiesta di finanziamento, pronto per la verifica di un
investitore. I numeri economici non sono scritti a mano: il generatore li legge
dal modello di cassa (`../modello/numeri.json`).

Per rigenerarlo:

```sh
PY=/percorso/python-con-pymupdf ./build-piano.sh
```

Lo script ricalcola i numeri dal modello, scrive `report-piano.html` con
`gen/genera.py` (un file per gruppo di capitoli in `gen/`), lo stampa con
Chromium (`render-piano.mjs`) e unisce copertina e corpo.

## `Krine-Labs_Analisi-di-mercato.pdf`

L'analisi di mercato precedente, tenuta come riferimento. Sorgente `report.html`,
rendering con `node render.mjs`.
