# Ricerca sul campo

## `mappa-competitiva.xlsx`

La griglia dove si raccolgono i dati sui prodotti concorrenti. Tre fogli:

- **Istruzioni** — a cosa serve, la regola di verifica, l'ordine di lavoro
- **Mappa** — 24 prodotti, 25 colonne. Giallo = da compilare a mano,
  grigio = calcolato da formula, azzurro = valore nostro già inserito
- **Sintesi** — conteggi, minimi, massimi e medie calcolati sulla Mappa

Regola: una riga conta solo se qualcuno ha aperto la pagina del prodotto e ha
compilato URL e data di consultazione. Senza quei due campi il dato non è
verificato e non va usato in nessun documento.

Le formule sono scritte ma non hanno valori in cache: si calcolano alla prima
apertura in Excel o LibreOffice.

## `build_mappa.py`

Lo script che genera il file. Rigenerarlo sovrascrive tutto il lavoro di
compilazione manuale: usarlo solo per ricostruire la griglia da zero.

```sh
python3 build_mappa.py
```
