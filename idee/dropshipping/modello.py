"""Confronto economico di 10 prodotti in dropshipping (Italia, ottobre 2026).

Tutti i costi dei prodotti sono STIME da verificare con preventivi reali
(CJdropshipping, AliExpress, BigBuy). Le ipotesi comuni sono in cima al file.
Esecuzione: python3 modello.py
"""

IVA = 0.22
PAGAMENTO_PCT, PAGAMENTO_FISSO = 0.019, 0.25   # come nel modello KRINÉ
ASSISTENZA_PCT = 0.03
# Dalla Cina diretto: dazio UE fisso 3 € (dal 1/7/2026) + contributo italiano 2 €
# (rinviato al 1/12/2026, data da verificare in Gazzetta Ufficiale).
DOGANA_CINA = 3.0 + 2.0

# Costo per clic su Meta in Italia: CPM ~7–8 € e CTR ~1% → CPC ~0,80 €.
CPC = {"ottimista": 0.60, "base": 0.80, "pessimista": 1.00}
# Scenario "ottimizzato": creatività vincenti e bundle, come fanno i dropshipper che reggono.
OTT_CPC, OTT_CVR, OTT_AOV = 0.60, 1.5, 1.25   # CPC, moltiplicatore conversione, carrello

PESI = {"mot": .20, "vant": .15, "dolore": .15, "mercato": .10, "unit": .10,
        "valid": .10, "scal": .10, "dif": .05, "tempo": .05}

# id, nome, prezzo IVA incl., costo Cina (prodotto+spedizione), costo magazzino UE,
# resi/rimborsi (% del netto), conversione della landing, riordini attesi in 12 mesi,
# prezzo del riordino, costo del riordino (canale UE), costi fissi una tantum di conformità
P = [
    ("051", "Spazzola massaggiante per cuoio capelluto", 16.90, 4.4, 6.4, .04, .028, 0.0, 0, 0, 300),
    ("052", "Filtro doccia + cartucce di ricambio", 39.90, 11.5, 13.5, .08, .018, 1.6, 14.90, 6.5, 500),
    ("053", "Federa in seta di gelso 22 momme", 44.90, 14.5, 17.5, .10, .016, 0.2, 44.90, 17.5, 400),
    ("054", "Piegaciglia riscaldato ricaricabile", 29.90, 7.5, 10.0, .08, .020, 0.05, 29.90, 10.0, 1200),
    ("055", "Maschera LED viso", 149.00, 54.0, 58.0, .15, .008, 0.0, 0, 0, 6000),
    ("056", "Strisce sbiancanti PAP (marchio proprio, stock UE)", 29.90, None, 8.5, .06, .020, 0.8, 29.90, 8.5, 3500),
    ("057", "Pressurizzatore per palline da padel", 34.90, 12.5, 14.0, .06, .020, 0.1, 34.90, 14.0, 400),
    ("058", "Registratore vocale AI (tipo Plaud)", 109.00, 38.0, 43.0, .12, .010, 0.0, 0, 0, 2500),
    ("059", "Cubi a compressione da viaggio (set)", 29.90, 10.5, 12.5, .06, .020, 0.05, 29.90, 12.5, 300),
    ("060", "Nastro per la bocca per il sonno (30 notti)", 14.90, 3.7, 5.8, .03, .028, 1.5, 14.90, 5.8, 400),
]

# Voti della scheda (1–5). La motivazione è una stima di Claude: la conferma Lorenzo.
VOTI = {
    "051": dict(mot=3, vant=3, dolore=2, mercato=2, unit=1, valid=5, scal=4, dif=1, tempo=5),
    "052": dict(mot=3, vant=3, dolore=3, mercato=3, unit=3, valid=4, scal=4, dif=2, tempo=4),
    "053": dict(mot=3, vant=2, dolore=2, mercato=3, unit=2, valid=4, scal=4, dif=2, tempo=4),
    "054": dict(mot=3, vant=3, dolore=2, mercato=2, unit=2, valid=4, scal=4, dif=1, tempo=4),
    "055": dict(mot=4, vant=3, dolore=3, mercato=4, unit=2, valid=2, scal=4, dif=2, tempo=3),
    "056": dict(mot=3, vant=3, dolore=3, mercato=3, unit=3, valid=3, scal=4, dif=2, tempo=3),
    "057": dict(mot=4, vant=3, dolore=2, mercato=2, unit=2, valid=5, scal=4, dif=1, tempo=5),
    "058": dict(mot=3, vant=3, dolore=3, mercato=4, unit=2, valid=3, scal=5, dif=1, tempo=4),
    "059": dict(mot=2, vant=2, dolore=2, mercato=3, unit=1, valid=5, scal=4, dif=1, tempo=5),
    "060": dict(mot=2, vant=3, dolore=2, mercato=2, unit=2, valid=5, scal=4, dif=1, tempo=5),
}


def contribuzione(prezzo, costo, resi, dogana=0.0):
    netto = prezzo / (1 + IVA)
    pagamento = prezzo * PAGAMENTO_PCT + PAGAMENTO_FISSO
    return netto - costo - dogana - pagamento - ASSISTENZA_PCT * netto - resi * netto


def punteggio(v):
    return sum(PESI[k] * v[k] for k in PESI)


def main():
    print(f"{'ID':4} {'Prodotto':52} {'Prezzo':>7} {'Contr.CN':>8} {'Contr.UE':>8} "
          f"{'CAC base':>8} {'LTV12':>6} {'LTV/CAC':>7} {'Pareggio CAC':>12} {'Scheda':>6}")
    righe = []
    for (pid, nome, prezzo, c_cn, c_eu, resi, cvr, riord, p_r, c_r, fissi) in P:
        contr_cn = contribuzione(prezzo, c_cn, resi, DOGANA_CINA) if c_cn else None
        contr_eu = contribuzione(prezzo, c_eu, resi)
        migliore = max(x for x in (contr_cn, contr_eu) if x is not None)
        contr_r = contribuzione(p_r, c_r, resi) if riord else 0
        ltv = migliore + riord * contr_r
        cac = {k: cpc / cvr for k, cpc in CPC.items()}
        # Conversione minima perché il primo ordine ripaghi il CAC (CPC base)
        cvr_pareggio = CPC["base"] / migliore if migliore > 0 else float("inf")
        s = punteggio(VOTI[pid])
        righe.append((pid, nome, prezzo, contr_cn, contr_eu, cac, ltv, cvr_pareggio, s, fissi))
        cn = f"{contr_cn:8.2f}" if contr_cn is not None else "    n.d."
        print(f"{pid:4} {nome:52} {prezzo:7.2f} {cn} {contr_eu:8.2f} {cac['base']:8.2f} "
              f"{ltv:6.2f} {ltv / cac['base']:7.2f} {cvr_pareggio:11.1%} {s:6.2f}")

    print("\nLTV/CAC per scenario di CPC (ottimista 0,60 · base 0,80 · pessimista 1,00):")
    for r in righe:
        cac, ltv = r[5], r[6]
        print(f"{r[0]} {r[1]:52} " + "  ".join(f"{k[:4]} {ltv / cac[k]:4.2f}" for k in CPC))

    print("\nConversione minima per ripagare il CAC entro 12 mesi (CPC base) e scenario ottimizzato:")
    for (pid, nome, prezzo, c_cn, c_eu, resi, cvr, riord, p_r, c_r, fissi), r in zip(P, righe):
        cvr_ltv = CPC["base"] / r[6]
        # ottimizzato: carrello +25% (bundle con costo +25%), conversione x1,5, CPC 0,60
        costo = min(x for x in (c_cn and c_cn + DOGANA_CINA, c_eu) if x)
        contr_o = contribuzione(prezzo * OTT_AOV, costo * OTT_AOV, resi)
        ltv_o = contr_o + riord * (contribuzione(p_r, c_r, resi) if riord else 0)
        cac_o = OTT_CPC / (cvr * OTT_CVR)
        print(f"{pid} {nome:52} conv. ipotizzata {cvr:4.1%} · minima {cvr_ltv:5.1%} · "
              f"ottimizzato: CAC {cac_o:5.2f} LTV {ltv_o:5.2f} LTV/CAC {ltv_o / cac_o:4.2f} · fissi {fissi} €")

    print("\nClassifica per punteggio della scheda:")
    for r in sorted(righe, key=lambda x: -x[8]):
        print(f"{r[0]} {r[1]:52} {r[8]:.2f}")


if __name__ == "__main__":
    main()
