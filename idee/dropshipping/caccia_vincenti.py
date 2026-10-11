"""Economia della "caccia al prodotto vincente" (dropshipping UE con magazzino UE).

Gli agenti IA abbassano il lavoro e il costo delle creatività, non la spesa pubblicitaria dei test.
Ipotesi (stime da fonti di settore, vedi agenti-ia.md):
  test: 200–400 € di pubblicità a prodotto; percentuale di vincenti 5–25%;
  vincente: prezzo 39,90 €, costo sbarcato 9 € (spedizione inclusa), finestra di vendita ~2 mesi.
Esecuzione: python3 caccia_vincenti.py
"""

IVA, PAG_PCT, PAG_FISSO, ASSIST, RESI = 0.22, 0.019, 0.25, 0.03, 0.05


def contr_pre_ads(prezzo=39.90, costo=9.0):
    netto = prezzo / (1 + IVA)
    return netto - costo - (prezzo * PAG_PCT + PAG_FISSO) - (ASSIST + RESI) * netto


def profitto_vincente(spesa_giorno, cac, mesi=2.0):
    ordini = spesa_giorno / cac * 30 * mesi
    return ordini * (contr_pre_ads() - cac)


def main():
    c = contr_pre_ads()
    print(f"Contribuzione prima della pubblicità per ordine: {c:.2f} €  (pareggio: CAC = {c:.2f} €)")
    print("\nProfitto di un vincente in 2 mesi (il CAC sale con la spesa):")
    scenari = [(100, 14), (300, 16), (500, 18)]
    for spesa, cac in scenari:
        print(f"  {spesa} €/giorno, CAC {cac} € → {profitto_vincente(spesa, cac):7.0f} €")
    print("\nValore atteso di un ciclo di ricerca (10 prodotti testati):")
    for costo_test in (200, 400):
        for hit in (0.05, 0.10, 0.20):
            costo = 10 * costo_test
            vincenti = 10 * hit
            for spesa, cac in scenari[:2]:
                guadagno = vincenti * profitto_vincente(spesa, cac)
                print(f"  test {costo_test} € · vincenti {hit:.0%} · scala {spesa} €/g: "
                      f"costo {costo:5.0f} € · profitto atteso {guadagno:6.0f} € · saldo {guadagno - costo:6.0f} €")


if __name__ == "__main__":
    main()
