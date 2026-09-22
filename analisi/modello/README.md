# Modello di cassa

`modello-cassa.xlsx` segue la cassa della società mese per mese, dalla chiusura
della raccolta al mese 30, in cinque scenari: base, lancio ritardato, avverso,
avverso con regole di arresto, tutto insieme.

- **Parametri**: tutte le ipotesi, una colonna per scenario. Si modificano solo
  le celle in blu su fondo giallo.
- **Progetto**: le voci di spesa prima del lancio, con mese, importo e quota IVA.
- **Confronto**: i risultati dei cinque scenari affiancati.
- **Unitaria**: economia per ordine, valore del cliente, rimborsi, costo industriale.
- **S1…S5**: un foglio di calcolo per scenario. Tutte formule.

Il file non contiene valori precalcolati: Excel e LibreOffice ricalcolano
all'apertura.

## I due modelli

`motore.py` è un secondo modello, scritto da zero in Python con la stessa logica.
`verifica_excel.py` ricalcola il foglio con un valutatore di formule indipendente
(libreria `formulas`) e lo confronta mese per mese con il motore su cassa, incassi,
rimborsi, IVA, scorte, clienti ed esposizione della garanzia. L'ultima verifica ha
dato una differenza massima di 0,00000000001 euro.

```sh
python3 motore.py             # risultati dei cinque scenari
python3 sensibilita.py        # griglie di sensibilità
python3 numeri.py             # scrive numeri.json, usato dal documento
python3 build_modello.py      # rigenera il foglio (serve openpyxl)
python3 verifica_excel.py     # confronto foglio/motore (serve formulas)
```
