"""075 Analisi AI dell'auto usata: economia per cliente, CAC sostenibile, strada verso 1 M€.
Tutte le ipotesi sono STIME da misurare con i test (vedi approfondimento.md). Esecuzione: python3 economia.py
"""

IVA = 0.22
PAG_PCT, PAG_FISSO = 0.015, 0.25        # Stripe UE carte europee (ordine di grandezza)
COSTO_AI_REPORT = 0.25                    # estrazione + analisi + testo (modello linguistico), stima
REPORT_PER_ACQUISTO = {"singolo": 1, "pass30": 4}

OFFERTE = {"singolo": 9.90, "pass30": 19.90}   # prezzi IVA inclusa
MIX = {"singolo": 0.6, "pass30": 0.4}
AFFILIAZIONI = 3.0                        # € medi per pagante: storico veicolo, assicurazione, finanziamento (stima)


def contribuzione():
    tot = 0.0
    for k, p in OFFERTE.items():
        netto = p / (1 + IVA)
        c = netto - (p * PAG_PCT + PAG_FISSO) - COSTO_AI_REPORT * REPORT_PER_ACQUISTO[k]
        tot += MIX[k] * c
    return tot + AFFILIAZIONI


def main():
    c = contribuzione()
    ricavo = sum(MIX[k] * OFFERTE[k] / (1 + IVA) for k in OFFERTE) + AFFILIAZIONI
    print(f"Ricavo netto medio per pagante: {ricavo:.2f} € · contribuzione: {c:.2f} €  → CAC massimo per il pareggio")

    print("\nCAC con pubblicità sulla ricerca Google (CPC × visite per un pagante):")
    for cpc in (0.30, 0.60, 1.00):
        for conv in (0.02, 0.04, 0.06):
            cac = cpc / conv
            print(f"  CPC {cpc:.2f} € · conversione visita→pagante {conv:.0%} → CAC {cac:6.2f} € · margine {c - cac:+6.2f} €")

    print("\nStrada verso 1 M€ di ricavi (Italia, 3,22 M di passaggi di proprietà nel 2025):")
    for quota in (0.005, 0.01, 0.02, 0.03):
        paganti = 3_221_145 * quota
        print(f"  {quota:.1%} dei passaggi → {paganti:,.0f} paganti → ricavi {paganti * ricavo / 1e6:4.2f} M€ (netti IVA, affiliazioni incluse)")

    print("\nCon Spagna (2,16 M di transazioni) e Germania (~6,5 M stimate) la stessa quota vale ~3,7 volte l'Italia.")


if __name__ == "__main__":
    main()
