"""Motore di calcolo del modello di cassa Kriné Labs.

Implementazione indipendente dal foglio Excel: serve a produrre i numeri del
piano e a verificare che le formule del foglio diano gli stessi risultati.
Tutti gli importi in euro. Mese 1 = primo mese dopo la chiusura della raccolta.
"""
import math, copy, json

MESI = 30          # orizzonte del modello di cassa
ETA = 36           # orizzonte per il valore del cliente (mesi di vita della coorte)
IVA = 0.22
GG_MESE = 30.4375

OFFERTE = ["p6", "p3", "abb", "sing"]
PREZZO = {"p6": 279.0, "p3": 149.0, "abb": 49.0, "sing": 59.0}
FLACONI = {"p6": 6, "p3": 3, "abb": 1, "sing": 1}
CORRIERE = {"p6": 6.50, "p3": 5.50, "abb": 4.50, "sing": 4.50}
PRELIEVO = 1.20
COMM_PCT, COMM_FISSA = 0.019, 0.25
ASSIST = 0.03

BASE = dict(
    nome="Base",
    lancio=16,
    costo_flacone=8.50,
    mix={"p6": 0.25, "p3": 0.10, "abb": 0.45, "sing": 0.20},
    # percorso da sei
    completamento=0.55, richiesta_garanzia=0.22, riacquisto_p6=0.45, riacquisto_p6_succ=0.60,
    # percorso da tre
    riacquisto_p3=0.35, riacquisto_p3_succ=0.55,
    # abbonamento: probabilità di rinnovo dopo l'ordine k (k=1..6, poi costante)
    rinnovo=[0.65, 0.70, 0.72, 0.78, 0.82, 0.85],
    intervallo_abb=28,
    # singolo
    riacquisto_sing=0.375,
    # acquisizione: spesa pubblicitaria per mese relativo al lancio
    tranche=[(0, 2, 10000.0, 50.0), (2, 3, 20000.0, 50.0), (5, 4, 30000.0, 55.0)],
    pubbl_dopo=5000.0, cac_dopo=55.0,
    creativi=600.0,
    organici=8,
    sconto_primo=0.05,       # codici sconto e promozioni sul primo ordine
    capitale=[(1, 250000.0)],
    # ritardo: costi extra di laboratorio (mese, importo)
    extra=[],
)

def scenario(nome):
    s = copy.deepcopy(BASE)
    s["nome"] = nome
    if nome in ("Lancio ritardato", "Tutto insieme"):
        s["lancio"] = 20
        s["extra"] = [(10, 6000.0, 1.0), (11, 6000.0, 1.0)]
    if nome.startswith("Avverso") or nome == "Tutto insieme":
        s["costo_flacone"] = 11.90
        s["richiesta_garanzia"] = 0.36
        s["rinnovo"] = [r - 0.08 for r in s["rinnovo"]]
        s["riacquisto_sing"] = 0.30
        s["riacquisto_p3"] = 0.25
        s["riacquisto_p6"] = 0.35
        s["tranche"] = [(a, n, imp, cac * 1.4) for a, n, imp, cac in s["tranche"]]
        s["cac_dopo"] = s["cac_dopo"] * 1.4
        s["organici"] = 4
        s["sconto_primo"] = 0.10
        if nome == "Avverso con arresto":
            s["tranche"] = s["tranche"][:2]        # la terza tranche non viene liberata
            s["pubbl_dopo"] = 0.0
    return s

SCENARI = ["Base", "Lancio ritardato", "Avverso senza arresto", "Avverso con arresto", "Tutto insieme"]

# ---------------------------------------------------------------- economia per ordine
def per_ordine(off, costo, sconto=0.0):
    lordo = PREZZO[off] * (1 - sconto)
    netto = lordo / (1 + IVA)
    prodotto = costo * FLACONI[off]
    logistica = PRELIEVO + CORRIERE[off]
    incasso = lordo * COMM_PCT + COMM_FISSA
    assist = netto * ASSIST
    return dict(lordo=lordo, netto=netto, prodotto=prodotto, logistica=logistica,
                incasso=incasso, assist=assist,
                contrib=netto - prodotto - logistica - incasso - assist)

# ---------------------------------------------------------------- vettori per età
def vettori(s):
    """Per ogni offerta: ordini, flaconi e rimborsi per cliente iniziale, per età 0..ETA-1."""
    v = {o: dict(ordini=[0.0] * ETA, rimborsi=[0.0] * ETA) for o in OFFERTE}
    # percorso da sei
    o = v["p6"]["ordini"]; o[0] += 1
    c, g = s["completamento"], s["richiesta_garanzia"]
    v["p6"]["rimborsi"][5] += c * g / 2
    v["p6"]["rimborsi"][6] += c * g / 2
    q = c * (1 - g) * s["riacquisto_p6"]
    eta = 6
    while eta < ETA:
        o[eta] += q
        q *= s["riacquisto_p6_succ"]; eta += 6
    # percorso da tre
    o = v["p3"]["ordini"]; o[0] += 1
    q = s["riacquisto_p3"]; eta = 3
    while eta < ETA:
        o[eta] += q
        q *= s["riacquisto_p3_succ"]; eta += 3
    # abbonamento
    o = v["abb"]["ordini"]; sopr = 1.0; k = 1
    while True:
        eta = math.floor(s["intervallo_abb"] * (k - 1) / GG_MESE + 0.5)
        if eta >= ETA: break
        o[eta] += sopr
        r = s["rinnovo"][min(k, len(s["rinnovo"])) - 1]
        sopr *= r; k += 1
    # singolo
    o = v["sing"]["ordini"]; sopr = 1.0; k = 1
    while True:
        eta = math.floor(28.5 * (k - 1) / GG_MESE + 0.5)
        if eta >= ETA: break
        o[eta] += sopr
        sopr *= s["riacquisto_sing"]; k += 1
    return v

def valore_cliente(s, orizzonte):
    """Contribuzione cumulata per cliente iniziale entro 'orizzonte' mesi (età 0..orizzonte-1)."""
    v = vettori(s); out = {}
    for off in OFFERTE:
        e = per_ordine(off, s["costo_flacone"])
        e1 = per_ordine(off, s["costo_flacone"], s["sconto_primo"])
        ordini = sum(v[off]["ordini"][:orizzonte])
        rimb = sum(v[off]["rimborsi"][:orizzonte])
        out[off] = dict(ordini=ordini, rimborsi=rimb,
                        valore=e1["contrib"] + (ordini - 1) * e["contrib"] - rimb * e1["netto"])
    out["medio"] = sum(s["mix"][o] * out[o]["valore"] for o in OFFERTE)
    return out

def curva_cumulata(s, off):
    v = vettori(s); e = per_ordine(off, s["costo_flacone"])
    e1 = per_ordine(off, s["costo_flacone"], s["sconto_primo"]); acc = 0; res = []
    for a in range(ETA):
        q = v[off]["ordini"][a]
        acc += (e1["contrib"] + (q - 1) * e["contrib"] if a == 0 else q * e["contrib"]) - v[off]["rimborsi"][a] * e1["netto"]
        res.append(acc)
    return res

# ---------------------------------------------------------------- costi di progetto
def costi_progetto(s):
    """Lista di (mese, voce, importo imponibile, quota soggetta a IVA italiana, tappa)."""
    L = s["lancio"]; d = L - 16   # spostamento delle attività legate al lancio
    c = []
    add = lambda m, voce, imp, iva, tappa: c.append((m, voce, imp, iva, tappa))
    add(1, "Costituzione della società", 3500, 0.6, 1)
    add(1, "Patti parasociali e documenti dell'investimento", 2500, 1.0, 1)
    add(2, "Parere brevettuale sulla formula C", 3500, 1.0, 1)
    add(2, "Deposito del marchio UE", 1500, 0.3, 1)
    add(2, "Interviste: incentivi e reclutamento", 750, 0.0, 1)
    add(3, "Interviste: incentivi e reclutamento", 750, 0.0, 1)
    add(4, "Laboratorio: fattibilità", 3000, 1.0, 2)
    add(5, "Laboratorio: metodi analitici (acconto)", 5000, 1.0, 2)
    add(7, "Laboratorio: metodi analitici (saldo)", 5000, 1.0, 2)
    for m in (5, 6, 7):
        add(m, "Laboratorio: micro-prove e solubilità", 4000, 1.0, 2)
    add(7, "Prova di colore su capelli bianchi e chiari", 500, 1.0, 2)
    add(8, "Laboratorio: candidati e sensorialità", 4000, 1.0, 2)
    add(9, "Laboratorio: candidati e sensorialità", 4000, 1.0, 2)
    add(8, "Tollerabilità: patch test e uso ripetuto (acconto)", 4000, 1.0, 2)
    add(9, "Tollerabilità: patch test e uso ripetuto (saldo)", 4000, 1.0, 2)
    for m, imp, q in s["extra"]:
        add(m, "Ciclo di laboratorio aggiuntivo", imp, q, 2)
    add(10 + d, "Stabilità, challenge test, compatibilità (acconto)", 3500, 1.0, 3)
    add(13 + d, "Stabilità, challenge test, compatibilità (saldo)", 3500, 1.0, 3)
    add(11 + d, "Protocollo per i claim (acconto)", 11000, 1.0, 3)
    add(13 + d, "Protocollo per i claim (saldo)", 11000, 1.0, 3)
    add(13 + d, "Valutazione di sicurezza, PIF, notifica", 2000, 1.0, 3)
    add(14 + d, "Valutazione di sicurezza, PIF, notifica", 2000, 1.0, 3)
    for m in range(11, 16):
        add(m + d, "Academy: parere, testi, revisione, traduzioni", 1800, 0.8, 3)
    for m in range(12, 16):
        add(m + d, "Confezione, grafica, foto, sito", 2000, 1.0, 3)
        add(m + d, "Test di messaggio a pagamento", 2000, 0.0, 3)
    add(12 + d, "Codici a barre GS1", 300, 1.0, 3)
    add(12 + d, "Lotto pilota e trasferimento di scala", 8500, 1.0, 3)
    return c

# ---------------------------------------------------------------- costi fissi
def costi_fissi(s, m):
    """(importo, quota IVA italiana) del mese m."""
    L = s["lancio"]; voci = []
    voci.append((100.0, 0.0))                 # due abbonamenti IA (Fable 5.1, ASTRA di OpenAI): reverse charge
    voci.append((250.0, 1.0))                 # commercialista
    voci.append((40.0, 0.5))                  # banca, PEC, dominio, posta
    if m >= 10: voci.append((30.0 if m < L else 80.0, 0.0))   # piattaforma e-commerce (reverse charge)
    if m >= L - 1: voci.append((100.0, 1.0))  # magazzino in conto terzi
    if m in (3, 15, 27): voci.append((430.0, 0.0))            # diritto camerale e tassa libri sociali
    if m == L or m == L + 12: voci.append((1200.0, 0.0))     # assicurazione RC prodotto (esente)
    return voci

# ---------------------------------------------------------------- simulazione
def simula(s):
    L = s["lancio"]; v = vettori(s)
    econ = {o: per_ordine(o, s["costo_flacone"]) for o in OFFERTE}
    econ1 = {o: per_ordine(o, s["costo_flacone"], s["sconto_primo"]) for o in OFFERTE}
    M = MESI
    rng = range(1, M + 1)
    z = lambda: {m: 0.0 for m in rng}
    pubbl, cac, nuovi_pag, nuovi_org, nuovi = z(), z(), z(), z(), z()
    for (inizio, durata, importo, c) in s["tranche"]:
        for k in range(durata):
            m = L + inizio + k
            if m <= M:
                pubbl[m] += importo / durata; cac[m] = c
    fine_tranche = L + max(i + n for i, n, _, _ in s["tranche"]) - 1
    for m in rng:
        if m > fine_tranche and m >= L:
            pubbl[m] += s["pubbl_dopo"]; cac[m] = s["cac_dopo"]
        if m >= L:
            nuovi_pag[m] = pubbl[m] / cac[m] if pubbl[m] > 0 else 0.0
            nuovi_org[m] = s["organici"]
            nuovi[m] = nuovi_pag[m] + nuovi_org[m]
    creativi = {m: (s["creativi"] if pubbl[m] > 0 else 0.0) for m in rng}
    # ordini per offerta e mese (convoluzione)
    ordini = {o: z() for o in OFFERTE}; primi = {o: z() for o in OFFERTE}; rimborsi = z()
    for a in rng:
        for o in OFFERTE:
            n = nuovi[a] * s["mix"][o]
            primi[o][a] += n
            for m in range(a, M + 1):
                ordini[o][m] += n * v[o]["ordini"][m - a]
                if o == "p6": rimborsi[m] += n * v[o]["rimborsi"][m - a]
    # flussi per mese
    R = {k: z() for k in ["incassi", "ricavi_netti", "iva_vendite", "rimborsi_lordi", "iva_rimborsi",
                          "logistica", "commissioni", "assistenza", "cogs", "contrib_ordini",
                          "flaconi", "campioni", "sostituzioni"]}
    for m in rng:
        for o in OFFERTE:
            for q, e in ((primi[o][m], econ1[o]), (ordini[o][m] - primi[o][m], econ[o])):
                R["incassi"][m] += q * e["lordo"]
                R["ricavi_netti"][m] += q * e["netto"]
                R["iva_vendite"][m] += q * (e["lordo"] - e["netto"])
                R["logistica"][m] += q * e["logistica"]
                R["commissioni"][m] += q * e["incasso"]
                R["assistenza"][m] += q * e["assist"]
                R["cogs"][m] += q * e["prodotto"]
            R["flaconi"][m] += ordini[o][m] * FLACONI[o]
        R["rimborsi_lordi"][m] = rimborsi[m] * econ1["p6"]["lordo"]
        R["iva_rimborsi"][m] = rimborsi[m] * (econ1["p6"]["lordo"] - econ1["p6"]["netto"])
        R["campioni"][m] = 150.0 if m == L else (20.0 if m > L else 0.0)
        R["sostituzioni"][m] = 0.01 * R["flaconi"][m]
    # progetto e fissi
    progetto = z(); progetto_iva = z(); tappe = {1: 0.0, 2: 0.0, 3: 0.0}
    for (m, voce, imp, q, t) in costi_progetto(s):
        if m <= M:
            progetto[m] += imp; progetto_iva[m] += imp * q * IVA; tappe[t] += imp
    fissi = z(); fissi_iva = z()
    for m in rng:
        for imp, q in costi_fissi(s, m):
            fissi[m] += imp; fissi_iva[m] += imp * q * IVA
    # scorte: primo lotto ordinato a L-3 (acconto 40%), consegnato a L-1 (saldo 60%)
    Q, ANTICIPO, TEMPO, SICUREZZA, RESIDUO_LOTTO = 3000, 0.40, 3, 1, 30
    costo = s["costo_flacone"]
    scorta = z(); ordinati = z(); consegne = z(); acquisti = z(); acquisti_iva = z()
    ordinati[L - 3] = Q
    stock = 0.0; in_arrivo = {}
    in_arrivo[L - 3 + TEMPO - 1] = Q   # il primo lotto arriva a L-1
    consumo_storico = []
    for m in rng:
        # pagamenti dei lotti ordinati
        for mo, q in list(ordinati.items()):
            if q and mo == m:
                acquisti[m] += q * costo * ANTICIPO
        if m in in_arrivo:
            q = in_arrivo.pop(m); consegne[m] = q
            stock += q * 0.99 - RESIDUO_LOTTO   # 1% di scarto, 30 pezzi per analisi e campioni di riserva
            acquisti[m] += q * costo * (1 - ANTICIPO)
        consumo = R["flaconi"][m] + R["campioni"][m] + R["sostituzioni"][m]
        stock -= consumo
        scorta[m] = stock
        consumo_storico.append(consumo)
        # punto di riordino: domanda nel tempo di fornitura + scorta di sicurezza, sulla media degli ultimi due mesi
        if m >= L:
            media = sum(consumo_storico[-2:]) / min(2, len(consumo_storico))
            punto = media * (TEMPO + SICUREZZA)
            gia = sum(in_arrivo.values())
            if stock + gia <= punto and m + TEMPO - 1 <= M + 12:
                ordinati[m] = Q; in_arrivo[m + TEMPO - 1] = Q
                acquisti[m] += Q * costo * ANTICIPO
        acquisti_iva[m] = acquisti[m] * IVA
    # ordini del primo lotto: acconto già contato sopra per m=L-3 tramite ordinati
    # IVA: posizione mensile, pagamento il mese successivo
    iva_da_versare = z(); credito = z(); pos = 0.0
    for m in rng:
        iva_acquisti = progetto_iva[m] + fissi_iva[m] + acquisti_iva[m] \
            + R["logistica"][m] * IVA + R["assistenza"][m] * 0.0
        netto = R["iva_vendite"][m] - R["iva_rimborsi"][m] - iva_acquisti
        pos = pos + netto
        if pos > 0:
            if m + 1 <= M: iva_da_versare[m + 1] += pos
            pos = 0.0
        credito[m] = -pos
    # cassa
    cassa = z(); c = 0.0; uscite_tot = z()
    versamenti = z()
    for mm, imp in s["capitale"]: versamenti[mm] += imp
    righe = {}
    for m in rng:
        entrate = R["incassi"][m]
        uscite = (R["rimborsi_lordi"][m] + R["logistica"][m] * (1 + IVA) + R["commissioni"][m]
                  + R["assistenza"][m] + pubbl[m] + creativi[m]
                  + progetto[m] + progetto_iva[m] + fissi[m] + fissi_iva[m]
                  + acquisti[m] + acquisti_iva[m] + iva_da_versare[m])
        c = c + versamenti[m] + entrate - uscite
        cassa[m] = c; uscite_tot[m] = uscite
    # esposizione di garanzia aperta: rimborsi attesi non ancora pagati
    esposizione = z()
    for m in rng:
        tot = 0.0
        for a in rng:
            if a <= m:
                n = nuovi[a] * s["mix"]["p6"]
                futuri = sum(v["p6"]["rimborsi"][k] for k in range(m - a + 1, ETA))
                tot += n * futuri * econ1["p6"]["lordo"]
        esposizione[m] = tot
    minimo = min(cassa.values()); mese_min = min(cassa, key=cassa.get)
    # risultato operativo mensile (competenza semplificata): contribuzione ordini - rimborsi netti - pubblicità - fissi
    operativo = {m: (R["ricavi_netti"][m] - R["cogs"][m] - R["logistica"][m] - R["commissioni"][m]
                     - R["assistenza"][m] - (R["rimborsi_lordi"][m] - R["iva_rimborsi"][m])
                     - pubbl[m] - creativi[m] - fissi[m]) for m in rng}
    return dict(s=s, pubbl=pubbl, cac=cac, nuovi_pag=nuovi_pag, nuovi_org=nuovi_org, nuovi=nuovi,
                ordini=ordini, primi=primi, rimborsi=rimborsi, versamenti=versamenti, R=R, progetto=progetto, progetto_iva=progetto_iva,
                tappe=tappe, fissi=fissi, fissi_iva=fissi_iva, scorta=scorta, ordinati=ordinati,
                consegne=consegne, acquisti=acquisti, acquisti_iva=acquisti_iva, iva_da_versare=iva_da_versare,
                credito=credito, cassa=cassa, uscite=uscite_tot, creativi=creativi, esposizione=esposizione,
                minimo=minimo, mese_min=mese_min, operativo=operativo)

if __name__ == "__main__":
    for nome in SCENARI:
        s = scenario(nome); r = simula(s)
        print(f"\n=== {nome} ===  cassa minima {r['minimo']:,.0f} al mese {r['mese_min']}, cassa al mese 30 {r['cassa'][30]:,.0f}")
        print("nuovi clienti totali", round(sum(r['nuovi'].values())), " di cui pagati", round(sum(r['nuovi_pag'].values())))
        print("pubblicità totale", round(sum(r['pubbl'].values())), " rimborsi lordi", round(sum(r['R']['rimborsi_lordi'].values())))
        print("incassi lordi", round(sum(r['R']['incassi'].values())), " ricavi netti", round(sum(r['R']['ricavi_netti'].values())))
        print("lotti ordinati", {m: q for m, q in r['ordinati'].items() if q})
        print("credito IVA max", round(max(r['credito'].values())), " IVA versata", round(sum(r['iva_da_versare'].values())))
        print("tappe", {k: round(x) for k, x in r['tappe'].items()})
        print("cassa:", " ".join(f"{m}:{r['cassa'][m]/1000:.0f}" for m in range(1, 31)))
        print("oper:", " ".join(f"{m}:{r['operativo'][m]/1000:.1f}" for m in range(14, 31)))
        for h in (6, 12, 24, 36):
            vc = valore_cliente(s, h)
            print(f"valore {h}m:", {o: round(vc[o]['valore'], 2) for o in OFFERTE}, "medio", round(vc['medio'], 2))
