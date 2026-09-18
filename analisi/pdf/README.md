# Report impaginato

`report.html` è la sorgente. Per rigenerare il PDF:

```sh
node render.mjs            # produce cover.pdf e body.pdf con Chromium
# poi unire i due file (la copertina non porta il numero di pagina)
```

`Krine-Labs_Analisi-di-mercato_v2.pdf` è la versione corrente e supera la v1.

Differenze della v2: flacone da 60 mL con percorsi da tre e cinque al posto
del formato da 120 mL; garanzia a 150 giorni condizionata al percorso
completo come meccanismo centrale; capitolo sui claim riscritto con i quattro
livelli di ciò che è utilizzabile e con l'Academy; classifica dei pubblici
ricalcolata tenendo conto del canale organico e della garanzia; soglie di
pareggio rifatte in funzione del costo di acquisizione.
