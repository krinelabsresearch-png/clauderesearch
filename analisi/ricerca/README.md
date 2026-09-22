# Ricerca sul campo

## `mappa-competitiva.xlsx`

La griglia dove si raccolgono prezzi, dosi, garanzie e claim delle alternative.

- **Istruzioni**: a che cosa serve, la regola di verifica, l'ordine di lavoro,
  come si legge una dose.
- **Mappa**: 23 alternative (dieci prioritarie, tredici di riferimento) e le
  quattro offerte KRINÉ. Giallo = da compilare, grigio = calcolato.
  La tabella si estende fino alla riga 200 senza toccare le formule.
- **Sintesi**: conteggi e statistiche. Le righe KRINÉ sono escluse; minimi,
  massimi e medie usano solo righe verificate con dose verificata.

Regola: una riga conta solo se qualcuno ha aperto le pagine e ha compilato URL e
data di prezzo e dose. Una dose ricavata dalla durata di un ciclo di trattamento
non vale.

## `build_mappa.py`

Rigenera il file da zero, sovrascrivendo la compilazione manuale.
