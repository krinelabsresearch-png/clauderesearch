"""Conti e scheda dei 16 prodotti della ricerca del 28/10/2026 (ID 218–233).

Stesse ipotesi e stessa scheda di ../modello.py (IVA, pagamenti, assistenza, CPC Meta Italia,
dazio Cina 3 € + contributo IT 2 €). Parametri dai rapporti verifica-*.md: sono STIME.
Esecuzione: python3 modello_ricerca.py
"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from modello import contribuzione, CPC, OTT_CPC, OTT_CVR, OTT_AOV, PESI, DOGANA_CINA  # noqa: E402

# id, nome, prezzo IVA incl., costo Cina (prodotto+spedizione, senza dogana) o None,
# costo da stock UE, resi (% netto), conversione landing, riordini 12 mesi,
# prezzo riordino, costo riordino (UE), costi fissi una tantum, dazio extra (più voci doganali)
P = [
    ("218", "Kit espresso puck prep + filtri carta", 34.90, 13.0, 16.0, .06, .015, 1.0, 14.90, 7.0, 1200, 3.0),
    ("219", "Calze antiscivolo pilates/padel (4 paia)", 34.90, 11.0, 14.0, .05, .018, 0.6, 34.90, 14.0, 1500, 0),
    ("220", "Overgrip padel in abbonamento (box 12)", 24.90, 9.0, 13.0, .03, .013, 3.0, 24.90, 13.0, 2000, 0),
    ("221", "Kit craft per adulti + video corso IT", 29.90, 9.0, 11.0, .05, .018, 1.0, 24.90, 10.0, 2500, 0),
    ("222", "Kit sigillo in ceralacca", 34.90, 9.5, 12.0, .03, .020, 0.4, 12.90, 5.5, 1200, 0),
    ("223", "Kit book nook (diorama per libreria)", 44.90, 22.0, 21.0, .08, .014, 0.3, 44.90, 21.0, 2500, 0),
    ("224", "Lampada scalda-candela", 49.90, 24.0, 26.0, .10, .015, 0.8, 19.90, 8.0, 4500, 3.0),
    ("225", "Monitor CO2 NDIR + umidità", 59.90, 24.0, 28.0, .07, .015, 0.1, 54.90, 28.0, 2500, 0),
    ("226", "Focus Tag NFC anti-scroll + metodo 30 giorni", 39.00, 8.5, 11.0, .08, .015, 0.12, 19.90, 6.5, 2000, 0),
    ("227", "Carte di conversazione in italiano", 27.90, None, 10.0, .04, .020, 0.30, 15.90, 8.0, 3500, 0),
    ("228", "Poster del percorso GPX (Gelato Italia)", 49.00, None, 18.0, .03, .018, 0.20, 49.00, 18.0, 1500, 0),
    ("229", "Penna in titanio incisa", 54.90, 20.0, 21.0, .04, .015, 0.12, 49.90, 21.0, 1800, 0),
    ("230", "Zaino 40x30x20 per voli low-cost", 39.90, 19.0, 17.0, .10, .022, 0.1, 24.90, 8.0, 2000, 0),
    ("231", "Ventola booster per termosifone", 39.90, 15.0, 19.0, .10, .018, 0.2, 34.90, 19.0, 2000, 0),
    ("232", "Mini stampante termica + rotoli", 29.90, 14.0, 17.0, .08, .015, 0.8, 12.90, 6.0, 2500, 3.0),
    ("233", "Gioielli acciaio 316L PVD", 39.00, 7.0, 10.0, .07, .020, 0.4, 35.00, 7.5, 3000, 0),
]

# Voti 1–5. dolore, mercato, valid, scal, dif, tempo: dai verificatori.
# mot e vant: stima di Claude sul profilo di Lorenzo (da confermare). unit: calcolato da LTV/CAC.
VOTI = {
    "218": dict(mot=4, vant=3, dolore=2, mercato=3, valid=4, scal=2, dif=2, tempo=4),
    "219": dict(mot=3, vant=3, dolore=3, mercato=4, valid=5, scal=2, dif=2, tempo=5),
    "220": dict(mot=4, vant=3, dolore=3, mercato=4, valid=3, scal=3, dif=3, tempo=4),
    "221": dict(mot=2, vant=2, dolore=3, mercato=4, valid=3, scal=3, dif=4, tempo=3),
    "222": dict(mot=3, vant=2, dolore=2, mercato=3, valid=5, scal=2, dif=2, tempo=5),
    "223": dict(mot=3, vant=2, dolore=2, mercato=3, valid=2, scal=3, dif=2, tempo=2),
    "224": dict(mot=3, vant=3, dolore=3, mercato=4, valid=2, scal=3, dif=3, tempo=2),
    "225": dict(mot=4, vant=4, dolore=3, mercato=3, valid=3, scal=3, dif=2, tempo=3),
    "226": dict(mot=4, vant=4, dolore=4, mercato=3, valid=4, scal=3, dif=2, tempo=4),
    "227": dict(mot=4, vant=4, dolore=2, mercato=3, valid=3, scal=3, dif=3, tempo=3),
    "228": dict(mot=4, vant=5, dolore=1, mercato=3, valid=4, scal=3, dif=3, tempo=3),
    "229": dict(mot=3, vant=2, dolore=1, mercato=2, valid=4, scal=2, dif=3, tempo=4),
    "230": dict(mot=3, vant=2, dolore=4, mercato=5, valid=4, scal=3, dif=1, tempo=4),
    "231": dict(mot=2, vant=2, dolore=3, mercato=3, valid=3, scal=2, dif=1, tempo=3),
    "232": dict(mot=2, vant=2, dolore=1, mercato=4, valid=3, scal=3, dif=1, tempo=3),
    "233": dict(mot=3, vant=3, dolore=2, mercato=5, valid=4, scal=3, dif=2, tempo=4),
}


def voto_unit(ltv_cac):
    for soglia, v in ((0.3, 1), (0.5, 2), (0.8, 3), (1.2, 4)):
        if ltv_cac < soglia:
            return v
    return 5


def calcola(p):
    pid, nome, prezzo, c_cn, c_eu, resi, cvr, riord, p_r, c_r, fissi, extra = p
    contr_cn = contribuzione(prezzo, c_cn, resi, DOGANA_CINA + extra) if c_cn else None
    contr_eu = contribuzione(prezzo, c_eu, resi)
    primo = max(x for x in (contr_cn, contr_eu) if x is not None)
    contr_r = contribuzione(p_r, c_r, resi) if riord else 0
    ltv = primo + riord * contr_r
    cac = CPC["base"] / cvr
    costo = min(x for x in ((c_cn + DOGANA_CINA + extra) if c_cn else None, c_eu) if x)
    ltv_o = contribuzione(prezzo * OTT_AOV, costo * OTT_AOV, resi) + riord * contr_r
    cac_o = OTT_CPC / (cvr * OTT_CVR)
    v = dict(VOTI[pid], unit=voto_unit(ltv / cac))
    s = sum(PESI[k] * v[k] for k in PESI)
    s_neutro = s - PESI["mot"] * (v["mot"] - 3)
    return dict(pid=pid, nome=nome, prezzo=prezzo, contr_cn=contr_cn, contr_eu=contr_eu, primo=primo,
                ltv=ltv, cac=cac, rapp=ltv / cac, cvr_pareggio=CPC["base"] / ltv, rapp_o=ltv_o / cac_o,
                fissi=fissi, voti=v, scheda=s, neutro=s_neutro)


def main():
    righe = sorted((calcola(p) for p in P), key=lambda r: -r["scheda"])
    print(f"{'ID':4} {'Prodotto':45} {'Prezzo':>6} {'1°ord':>6} {'LTV12':>6} {'CAC':>6} "
          f"{'LTV/CAC':>7} {'ottim.':>6} {'conv.pareggio':>13} {'fissi':>6} {'unit':>4} {'Scheda':>6} {'neutra':>6}")
    for r in righe:
        print(f"{r['pid']:4} {r['nome']:45} {r['prezzo']:6.2f} {r['primo']:6.2f} {r['ltv']:6.2f} {r['cac']:6.2f} "
              f"{r['rapp']:7.2f} {r['rapp_o']:6.2f} {r['cvr_pareggio']:12.1%} {r['fissi']:6d} {r['voti']['unit']:4d} "
              f"{r['scheda']:6.2f} {r['neutro']:6.2f}")


if __name__ == "__main__":
    main()
