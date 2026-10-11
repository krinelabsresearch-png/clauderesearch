"""Sieri e creme: confronto dei modelli "quasi dropshipping" legali, UE contro USA.

Modelli:
  CAT  formula di catalogo di un laboratorio UE, piccoli lotti, spedisci tu o un 3PL (Italia)
  PODE dropshipping cosmetico su richiesta in UE (es. Selfnamed, Lettonia)
  PODU dropshipping cosmetico su richiesta in USA (es. Blanka)
  DIST rivendita di marchi altrui già notificati (es. grossisti K-beauty in UE)
Tutti i costi dei prodotti sono STIME (vedi valutazione-sieri.md). Esecuzione: python3 modello_sieri.py
"""

from modello import punteggio

IVA_IT = 0.22
ASSISTENZA, RESI = 0.03, 0.02          # i cosmetici aperti non si restituiscono
PAG = {"UE": (0.019, 0.25), "US": (0.029, 0.27)}
LOGISTICA = {"CAT": 5.70, "DIST": 5.70, "PODE": 8.00, "PODU": 6.50}  # € a ordine
# CPC: Italia 0,80 € + 3% di location fee Meta; USA: CPM 16–23 $ con CTR ~1% → ~1,70 €
CPC = {"UE": 0.80 * 1.03, "US": 1.70}

# id, nome, prezzo IT, costo CAT, conversione, riordini/12 mesi, fissi CAT,
# costo PODE (None = non a catalogo), prezzo USA in €, costo PODU (None = non a catalogo)
P = [
    ("062", "Siero viso multi-peptide", 29.90, 4.0, .020, 0.8, 2800, 12.8, 34.0, 13.0),
    ("063", "Siero ai peptidi di rame (GHK-Cu)", 34.90, 4.5, .020, 0.8, 3100, None, 39.0, None),
    ("064", "Siero ciglia e sopracciglia ai peptidi", 39.90, 3.0, .018, 1.0, 3750, None, 45.0, None),
    ("065", "Trattamento labbra ai peptidi", 19.90, 2.5, .028, 1.2, 2300, None, 22.0, 7.0),
    ("066", "Siero cuoio capelluto ai peptidi", 39.90, 5.0, .018, 1.1, 3500, None, 45.0, None),
    ("067", "Siero PDRN (DNA di salmone)", 34.90, 5.0, .020, 0.8, 3200, None, 39.0, None),
    ("068", "Crema contorno occhi ai peptidi", 29.90, 4.0, .020, 0.7, 3300, 12.5, 34.0, 12.0),
    ("069", "Rivendita K-beauty (distributore)", 24.90, 12.0, .022, 0.6, 800, None, None, None),
]

VOTI = {
    "062": dict(mot=3, vant=3, dolore=3, mercato=5, unit=3, valid=3, scal=4, dif=1, tempo=4),
    "063": dict(mot=4, vant=3, dolore=3, mercato=4, unit=3, valid=3, scal=4, dif=1, tempo=4),
    "064": dict(mot=4, vant=4, dolore=4, mercato=3, unit=3, valid=3, scal=4, dif=2, tempo=3),
    "065": dict(mot=2, vant=2, dolore=2, mercato=4, unit=3, valid=4, scal=4, dif=1, tempo=4),
    "066": dict(mot=4, vant=4, dolore=4, mercato=3, unit=3, valid=3, scal=4, dif=1, tempo=4),
    "067": dict(mot=3, vant=2, dolore=2, mercato=3, unit=3, valid=3, scal=4, dif=1, tempo=4),
    "068": dict(mot=2, vant=2, dolore=3, mercato=4, unit=3, valid=3, scal=4, dif=1, tempo=3),
    "069": dict(mot=2, vant=2, dolore=3, mercato=4, unit=1, valid=4, scal=3, dif=1, tempo=5),
}


def contr(prezzo, costo, modello, mercato):
    netto = prezzo / (1 + IVA_IT) if mercato == "UE" else prezzo  # USA: niente IVA sotto le soglie statali
    pct, fisso = PAG[mercato]
    return netto - costo - LOGISTICA[modello] - (prezzo * pct + fisso) - (ASSISTENZA + RESI) * netto


def riga(nome_modello, prezzo, costo, modello, mercato, cvr, riord):
    c = contr(prezzo, costo, modello, mercato)
    cac = CPC[mercato] / cvr
    ltv = c * (1 + riord)
    return f"{nome_modello:5} contr. {c:6.2f} · CAC {cac:6.2f} · LTV12 {ltv:6.2f} · LTV/CAC {ltv / cac:4.2f}", ltv / cac


def main():
    migliori = {}
    for pid, nome, p_it, c_cat, cvr, riord, fissi, c_pode, p_us, c_podu in P:
        print(f"\n{pid} {nome} — fissi CAT ~{fissi} €")
        mod = "DIST" if pid == "069" else "CAT"
        testo, r = riga(mod, p_it, c_cat, mod, "UE", cvr, riord)
        print("  UE  " + testo)
        migliori[pid] = r
        if c_pode:
            testo, _ = riga("PODE", p_it, c_pode, "PODE", "UE", cvr, riord)
            print("  UE  " + testo)
        if c_podu:
            testo, _ = riga("PODU", p_us, c_podu, "PODU", "US", cvr, riord)
            print("  USA " + testo)

    print("\nStesso prodotto generico (costo 8 €, magazzino locale, logistica 5,70 €), UE contro USA:")
    for prezzo_us in (34.90, 44.90):
        for cvr in (0.02, 0.03):
            ue = contr(34.90, 8.0, "CAT", "UE")
            us = contr(prezzo_us, 8.0, "CAT", "US")
            print(f"  conv. {cvr:.0%}: Italia 34,90 € → contr. {ue:5.2f}, CAC {CPC['UE'] / cvr:5.2f} | "
                  f"USA {prezzo_us:.2f} € → contr. {us:5.2f}, CAC {CPC['US'] / cvr:5.2f}")

    print("\nScheda pesata:")
    for pid, nome, *_ in sorted(P, key=lambda x: -punteggio(VOTI[x[0]])):
        print(f"  {pid} {nome:42} {punteggio(VOTI[pid]):.2f}  (LTV/CAC UE {migliori[pid]:.2f})")


if __name__ == "__main__":
    main()
