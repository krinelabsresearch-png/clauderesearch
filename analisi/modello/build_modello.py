"""Genera modello-cassa.xlsx: modello mensile a 30 mesi, cinque scenari, tutto a formule.

Ogni scenario ha un foglio proprio che legge la sua colonna in 'Parametri'. Cambiando un
valore in 'Parametri' si aggiornano tutti i fogli. Le celle da modificare sono solo quelle
in blu su fondo giallo del foglio 'Parametri' e le voci del foglio 'Progetto'.
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter as L
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.comments import Comment

F = "Arial"
f_title = Font(name=F, size=14, bold=True)
f_bold = Font(name=F, size=10, bold=True)
f_norm = Font(name=F, size=10)
f_input = Font(name=F, size=10, color="0000FF")
f_link = Font(name=F, size=10, color="008000")
f_note = Font(name=F, size=9, italic=True, color="555555")
fill_in = PatternFill("solid", fgColor="FFF2CC")
fill_head = PatternFill("solid", fgColor="D9E1F2")
fill_key = PatternFill("solid", fgColor="E2EFDA")
thin = Side(style="thin", color="BBBBBB")
EUR = '#,##0;(#,##0);"-"'
EUR2 = '#,##0.00;(#,##0.00);"-"'
PCT = '0.0%;(0.0%);"-"'
NUM1 = '#,##0.0;(#,##0.0);"-"'
NUM3 = '0.000;(0.000);"-"'

SCEN = ["Base", "Lancio ritardato", "Avverso senza arresto", "Avverso con arresto", "Tutto insieme"]
SHEETS = ["S1 Base", "S2 Ritardo", "S3 Avverso", "S4 Avverso+arresto", "S5 Tutto insieme"]
MESI, ETA, KMAX = 30, 36, 45

A6 = [.65, .70, .72, .78, .82, .85]; B6 = [round(x - .08, 2) for x in A6]
PAR = [  # chiave, etichetta, unità, [5 valori], nota
    ("lancio", "Mese del lancio", "mese", [16, 20, 16, 16, 20], "Primo mese di vendita dopo la chiusura della raccolta"),
    ("costo", "Costo industriale per flacone", "€", [8.5, 8.5, 11.9, 11.9, 11.9], "Stima centrale 8,50; alta 11,90 (capitolo 08)"),
    ("mix_p6", "Quota nuovi clienti: percorso da 6", "%", [.25] * 5, "IPOTESI. La più delicata per la cassa"),
    ("mix_p3", "Quota nuovi clienti: percorso da 3", "%", [.10] * 5, "IPOTESI"),
    ("mix_abb", "Quota nuovi clienti: abbonamento", "%", [.45] * 5, "IPOTESI"),
    ("mix_sing", "Quota nuovi clienti: flacone singolo", "%", [.20] * 5, "IPOTESI. Le quattro quote devono sommare a 100%"),
    ("compl", "Percorso da 6: quota che lo completa", "%", [.55] * 5, "IPOTESI. Solo chi completa può chiedere la garanzia"),
    ("gar", "Percorso da 6: chi completa e chiede il rimborso", "%", [.22, .22, .36, .36, .36], "IPOTESI. Rimborsi sul totale = completamento × questa quota"),
    ("rp6", "Percorso da 6: riacquisto di chi completa senza rimborso", "%", [.45, .45, .35, .35, .35], "IPOTESI. Nuovo percorso da 6, senza garanzia"),
    ("rp6s", "Percorso da 6: riacquisti successivi", "%", [.60] * 5, "IPOTESI"),
    ("rp3", "Percorso da 3: riacquisto a 3 mesi", "%", [.35, .35, .25, .25, .25], "IPOTESI"),
    ("rp3s", "Percorso da 3: riacquisti successivi", "%", [.55] * 5, "IPOTESI"),
    ("r1", "Abbonamento: rinnovo dopo il 1° invio", "%", [A6[0], A6[0], B6[0], B6[0], B6[0]], "IPOTESI. Curva di rinnovo, non media"),
    ("r2", "Abbonamento: rinnovo dopo il 2° invio", "%", [A6[1], A6[1], B6[1], B6[1], B6[1]], "IPOTESI"),
    ("r3", "Abbonamento: rinnovo dopo il 3° invio", "%", [A6[2], A6[2], B6[2], B6[2], B6[2]], "IPOTESI"),
    ("r4", "Abbonamento: rinnovo dopo il 4° invio", "%", [A6[3], A6[3], B6[3], B6[3], B6[3]], "IPOTESI"),
    ("r5", "Abbonamento: rinnovo dopo il 5° invio", "%", [A6[4], A6[4], B6[4], B6[4], B6[4]], "IPOTESI"),
    ("r6", "Abbonamento: rinnovo dal 6° invio in poi", "%", [A6[5], A6[5], B6[5], B6[5], B6[5]], "IPOTESI"),
    ("rs", "Flacone singolo: probabilità di un nuovo acquisto", "%", [.375, .375, .30, .30, .30], "IPOTESI. 0,375 = 1,6 ordini medi"),
    ("sconto", "Sconto medio sul primo ordine", "%", [.05, .05, .10, .10, .10], "Codici, promozioni di lancio"),
    ("org", "Clienti da canali non pagati, al mese", "clienti", [8, 8, 4, 4, 4], "IPOTESI. Rete dei fondatori, Academy, passaparola"),
    ("s1", "Pubblicità tranche 1 (totale)", "€", [10000] * 5, "Prima coorte"),
    ("d1", "Tranche 1: durata", "mesi", [2] * 5, ""),
    ("c1", "CAC pubblicitario tranche 1", "€", [50, 50, 70, 70, 70], "IPOTESI. Avverso = base × 1,4"),
    ("s2", "Pubblicità tranche 2 (totale)", "€", [20000] * 5, "Replica"),
    ("d2", "Tranche 2: durata", "mesi", [3] * 5, ""),
    ("c2", "CAC pubblicitario tranche 2", "€", [50, 50, 70, 70, 70], "IPOTESI"),
    ("s3", "Pubblicità tranche 3 (totale)", "€", [30000, 30000, 30000, 0, 30000], "Liberata solo se passa la verifica. 0 = regola di arresto applicata"),
    ("d3", "Tranche 3: durata", "mesi", [4] * 5, ""),
    ("c3", "CAC pubblicitario tranche 3 (marginale)", "€", [55, 55, 77, 77, 77], "IPOTESI. Più spesa, clienti più cari"),
    ("pd", "Pubblicità mensile dopo le tranche", "€/mese", [5000, 5000, 5000, 0, 5000], "Finanziata dalla cassa"),
    ("cd", "CAC dopo le tranche", "€", [55, 55, 77, 77, 77], "IPOTESI"),
    ("cre", "Creatività e gestione campagne", "€/mese", [600] * 5, "Nei mesi con pubblicità. Differenza fra CAC pubblicitario e complessivo"),
    ("x10", "Ciclo di laboratorio aggiuntivo, mese 10", "€", [0, 6000, 0, 0, 6000], "Solo negli scenari con ritardo"),
    ("x11", "Ciclo di laboratorio aggiuntivo, mese 11", "€", [0, 6000, 0, 0, 6000], ""),
    ("k1", "Capitale versato al mese 1", "€", [250000] * 5, "Per simulare due tranche: 100.000 qui e 150.000 sotto"),
    ("k2m", "Mese della seconda tranche di capitale", "mese", [10] * 5, ""),
    ("k2", "Seconda tranche di capitale", "€", [0] * 5, ""),
]
COST = [
    ("iva", "Aliquota IVA", "%", .22, ""),
    ("pz_p6", "Prezzo percorso da 6 flaconi", "€ IVA incl.", 279, ""),
    ("pz_p3", "Prezzo percorso da 3 flaconi", "€ IVA incl.", 149, ""),
    ("pz_abb", "Prezzo abbonamento, ogni 28 giorni", "€ IVA incl.", 49, "Consegna ogni 28 giorni: 57 mL utili a 2 mL/giorno"),
    ("pz_sing", "Prezzo flacone singolo", "€ IVA incl.", 59, ""),
    ("fl_p6", "Flaconi: percorso da 6", "n", 6, ""), ("fl_p3", "Flaconi: percorso da 3", "n", 3, ""),
    ("fl_abb", "Flaconi: abbonamento", "n", 1, ""), ("fl_sing", "Flaconi: singolo", "n", 1, ""),
    ("co_p6", "Corriere: 6 flaconi", "€", 6.5, "IVA 22%"), ("co_p3", "Corriere: 3 flaconi", "€", 5.5, ""),
    ("co_abb", "Corriere: 1 flacone (abbonamento)", "€", 4.5, ""), ("co_sing", "Corriere: 1 flacone (singolo)", "€", 4.5, ""),
    ("pick", "Prelievo e imballo per ordine", "€", 1.2, "IVA 22%"),
    ("feep", "Commissione di incasso, percentuale", "%", .019, "Media prudente: carte UE standard 1,5%, premium 1,9%, extra UE di più"),
    ("feef", "Commissione di incasso, fissa", "€", .25, ""),
    ("ass", "Assistenza, resi ordinari, sostituzioni", "% ricavo netto", .03, "Distinto dalla garanzia: nessuna sovrapposizione"),
    ("lotto", "Lotto di produzione", "flaconi", 3000, "Minimo d'ordine ipotizzato"),
    ("ant", "Acconto all'ordine del lotto", "%", .40, "Saldo alla consegna"),
    ("tempo", "Tempo di fornitura", "mesi", 3, "Dall'ordine alla disponibilità, estremi inclusi"),
    ("sic", "Scorta di sicurezza", "mesi di consumo", 1, ""),
    ("scarto", "Scarto di produzione", "%", .01, ""),
    ("tratt", "Flaconi trattenuti per lotto (analisi e campioni di riserva)", "flaconi", 30, ""),
    ("camp_l", "Campioni al lancio", "flaconi", 150, ""),
    ("camp_m", "Campioni al mese dopo il lancio", "flaconi", 20, ""),
    ("sost", "Sostituzioni fisiche", "% flaconi spediti", .01, ""),
    ("int_abb", "Intervallo abbonamento", "giorni", 28, ""),
    ("int_sing", "Durata di un flacone", "giorni", 28.5, "57 mL utili a 2 mL/giorno"),
    ("gm", "Giorni per mese", "giorni", 30.4375, ""),
]
PROG = [  # voce, mese base, legato al lancio, importo, quota IVA, tappa
    ("Costituzione della società", 1, "no", 3500, .6, 1),
    ("Patti parasociali e documenti dell'investimento", 1, "no", 2500, 1, 1),
    ("Parere brevettuale sulla formula C", 2, "no", 3500, 1, 1),
    ("Deposito del marchio UE", 2, "no", 1500, .3, 1),
    ("Interviste: incentivi e reclutamento", 2, "no", 750, 0, 1),
    ("Interviste: incentivi e reclutamento", 3, "no", 750, 0, 1),
    ("Laboratorio: fattibilità", 4, "no", 3000, 1, 2),
    ("Laboratorio: metodi analitici, acconto", 5, "no", 5000, 1, 2),
    ("Laboratorio: metodi analitici, saldo", 7, "no", 5000, 1, 2),
    ("Laboratorio: micro-prove e solubilità", 5, "no", 4000, 1, 2),
    ("Laboratorio: micro-prove e solubilità", 6, "no", 4000, 1, 2),
    ("Laboratorio: micro-prove e solubilità", 7, "no", 4000, 1, 2),
    ("Prova di colore su capelli bianchi e chiari", 7, "no", 500, 1, 2),
    ("Laboratorio: candidati e sensorialità", 8, "no", 4000, 1, 2),
    ("Laboratorio: candidati e sensorialità", 9, "no", 4000, 1, 2),
    ("Tollerabilità: patch test e uso ripetuto, acconto", 8, "no", 4000, 1, 2),
    ("Tollerabilità: patch test e uso ripetuto, saldo", 9, "no", 4000, 1, 2),
    ("Stabilità, challenge test, compatibilità, acconto", 10, "sì", 3500, 1, 3),
    ("Stabilità, challenge test, compatibilità, saldo", 13, "sì", 3500, 1, 3),
    ("Protocollo per i claim, acconto", 11, "sì", 11000, 1, 3),
    ("Protocollo per i claim, saldo", 13, "sì", 11000, 1, 3),
    ("Valutazione di sicurezza, PIF, notifica", 13, "sì", 2000, 1, 3),
    ("Valutazione di sicurezza, PIF, notifica", 14, "sì", 2000, 1, 3),
] + [("Academy: parere, testi, revisione, traduzioni", m, "sì", 1800, .8, 3) for m in range(11, 16)] \
  + [x for m in range(12, 16) for x in (("Confezione, grafica, foto, sito", m, "sì", 2000, 1, 3),
                                         ("Test di messaggio a pagamento", m, "sì", 2000, 0, 3))] \
  + [("Codici a barre GS1", 12, "sì", 300, 1, 3), ("Lotto pilota e trasferimento di scala", 12, "sì", 8500, 1, 3)]

wb = Workbook()

# ------------------------------------------------------------------ Leggimi
ws = wb.active; ws.title = "Leggimi"
righe = [
    ("Kriné Labs · Modello di cassa mensile a 30 mesi", f_title),
    ("", None),
    ("A che cosa serve", f_bold),
    ("Calcola mese per mese la cassa della società dalla chiusura della raccolta al mese 30: spese di sviluppo, scorte,", f_norm),
    ("pubblicità, incassi, IVA, rimborsi della garanzia. Cassa minima e fabbisogno sono risultati, non ipotesi.", f_norm),
    ("", None),
    ("Come si usa", f_bold),
    ("1. Si modificano solo le celle in blu su fondo giallo del foglio Parametri e gli importi del foglio Progetto.", f_norm),
    ("2. Ogni colonna di Parametri è uno scenario. Ogni scenario ha il suo foglio di calcolo (S1…S5).", f_norm),
    ("3. Il foglio Confronto mette i risultati uno accanto all'altro. Il foglio Unitaria mostra l'economia per ordine e per cliente.", f_norm),
    ("", None),
    ("Colori", f_bold),
    ("Testo blu su fondo giallo: valore inserito a mano, da discutere · Testo nero: formula · Testo verde: collegamento a un altro foglio", f_norm),
    ("", None),
    ("Convenzioni", f_bold),
    ("Mese 1 = primo mese dopo la chiusura della raccolta. Importi in euro. Le spese di progetto sono al netto dell'IVA; l'IVA pagata", f_norm),
    ("ai fornitori italiani è calcolata a parte e recuperata compensandola con l'IVA sulle vendite. Pubblicità, piattaforme e", f_norm),
    ("abbonamenti di fornitori UE extra-Italia sono in inversione contabile e non assorbono cassa. Liquidazione IVA mensile, prudente.", f_norm),
    ("I fondatori non ricevono compenso dalla società: hanno altre entrate. Imposte sul reddito e IRAP non sono modellate.", f_norm),
    ("", None),
    ("Verifica", f_bold),
    ("Il foglio è stato ricalcolato con un valutatore di formule indipendente e confrontato, scenario per scenario e mese per mese,", f_norm),
    ("con un secondo modello scritto in Python (motore.py, nella stessa cartella). Le differenze sono sotto un centesimo.", f_norm),
]
for i, (t, fnt) in enumerate(righe, 1):
    c = ws.cell(i, 1, t)
    if fnt: c.font = fnt
ws.column_dimensions["A"].width = 130

# ------------------------------------------------------------------ Parametri
P = wb.create_sheet("Parametri")
P["A1"] = "Parametri del modello"; P["A1"].font = f_title
P["A2"] = "Blu su giallo: da discutere e modificare. Una colonna per scenario."; P["A2"].font = f_note
hdr = ["Parametro", "Unità", "Nota"] + SCEN
for j, h in enumerate(hdr, 1):
    c = P.cell(4, j, h); c.font = f_bold; c.fill = fill_head; c.alignment = Alignment(wrap_text=True, vertical="center")
PROW = {}
r = 5
for key, lab, un, vals, nota in PAR:
    P.cell(r, 1, lab).font = f_norm; P.cell(r, 2, un).font = f_norm; P.cell(r, 3, nota).font = f_note
    for j, v in enumerate(vals):
        c = P.cell(r, 4 + j, v); c.font = f_input; c.fill = fill_in
        c.number_format = PCT if un == "%" else (EUR if un.startswith("€") else "General")
    PROW[key] = r; r += 1
r += 1
P.cell(r, 1, "Costanti, uguali per tutti gli scenari").font = f_bold; P.cell(r, 1).fill = fill_head; r += 1
CROW = {}
for key, lab, un, val, nota in COST:
    P.cell(r, 1, lab).font = f_norm; P.cell(r, 2, un).font = f_norm; P.cell(r, 3, nota).font = f_note
    c = P.cell(r, 4, val); c.font = f_input; c.fill = fill_in
    c.number_format = PCT if un.startswith("%") else ("0.00" if isinstance(val, float) else "General")
    CROW[key] = r; r += 1
r += 1
P.cell(r, 1, "Controllo: somma delle quote di offerta").font = f_bold
for j in range(5):
    col = L(4 + j)
    c = P.cell(r, 4 + j, f"=SUM({col}{PROW['mix_p6']}:{col}{PROW['mix_sing']})"); c.number_format = PCT; c.font = f_norm
P.column_dimensions["A"].width = 52; P.column_dimensions["B"].width = 14; P.column_dimensions["C"].width = 62
for j in range(5): P.column_dimensions[L(4 + j)].width = 15
P.freeze_panes = "D5"

# ------------------------------------------------------------------ Progetto
G = wb.create_sheet("Progetto")
G["A1"] = "Costi di progetto prima del lancio"; G["A1"].font = f_title
G["A2"] = ("Importi al netto dell'IVA. 'Legato al lancio' = sì: la voce si sposta se il lancio slitta (mese effettivo = mese base + lancio − 16). "
           "Quota IVA = parte dell'importo su cui si paga IVA italiana."); G["A2"].font = f_note
for j, h in enumerate(["Voce", "Mese base", "Legato al lancio", "Importo €", "Quota IVA", "Tappa"], 1):
    c = G.cell(4, j, h); c.font = f_bold; c.fill = fill_head
GR0 = 5
for i, (voce, m, leg, imp, q, t) in enumerate(PROG):
    rr = GR0 + i
    G.cell(rr, 1, voce).font = f_norm
    for j, v in ((2, m), (3, leg), (4, imp), (5, q), (6, t)):
        c = G.cell(rr, j, v); c.font = f_input; c.fill = fill_in
    G.cell(rr, 4).number_format = EUR; G.cell(rr, 5).number_format = PCT
GR1 = GR0 + len(PROG) - 1
G.cell(GR1 + 1, 1, "Totale").font = f_bold
G.cell(GR1 + 1, 4, f"=SUM(D{GR0}:D{GR1})").number_format = EUR
for t in (1, 2, 3):
    G.cell(GR1 + 2 + t, 1, f"Tappa {t}").font = f_norm
    G.cell(GR1 + 2 + t, 4, f"=SUMIF(F{GR0}:F{GR1},{t},D{GR0}:D{GR1})").number_format = EUR
G.cell(GR1 + 6, 1, "Il ciclo di laboratorio aggiuntivo degli scenari con ritardo è in Parametri, non qui.").font = f_note
G.column_dimensions["A"].width = 52
for c in "BCDEF": G.column_dimensions[c].width = 14
dv = DataValidation(type="list", formula1='"sì,no"', allow_blank=False); G.add_data_validation(dv); dv.add(f"C{GR0}:C{GR1}")

# ------------------------------------------------------------------ fogli scenario
def build_scenario(idx, name):
    S = wb.create_sheet(name)
    S["A1"] = f"Scenario {idx}: {SCEN[idx-1]}"; S["A1"].font = f_title
    S["A2"] = "Indice dello scenario (colonna di Parametri)"; S["A2"].font = f_note
    S["C2"] = idx; S["C2"].font = f_bold
    R = {}; row = [4]
    def title(t):
        row[0] += 1; c = S.cell(row[0], 1, t); c.font = f_bold; c.fill = fill_head; row[0] += 1
    def put(key, label, unit=None):
        R[key] = row[0]; S.cell(row[0], 1, label).font = f_norm
        if unit: S.cell(row[0], 2, unit).font = f_note
        row[0] += 1; return R[key]
    pc = lambda k: f"$C${R['p_'+k]}"
    # --- parametri locali
    title("Parametri dello scenario (da Parametri)")
    for key, lab, un, vals, nota in PAR:
        rr = put("p_" + key, lab, un)
        c = S.cell(rr, 3, f"=INDEX(Parametri!$D${PROW[key]}:$H${PROW[key]},1,$C$2)"); c.font = f_link
        c.number_format = PCT if un == "%" else (EUR2 if un.startswith("€") else "General")
    for key, lab, un, val, nota in COST:
        rr = put("p_" + key, lab, un)
        c = S.cell(rr, 3, f"=Parametri!$D${CROW[key]}"); c.font = f_link
        c.number_format = PCT if un.startswith("%") else "General"
    # --- economia per ordine
    title("Economia per ordine (colonne C-F ordini successivi, H-K primo ordine con sconto)")
    offs = ["p6", "p3", "abb", "sing"]; labs = ["Percorso 6", "Percorso 3", "Abbonamento", "Singolo"]
    hr = row[0]
    for j, lab in enumerate(labs):
        S.cell(hr, 3 + j, lab).font = f_bold; S.cell(hr, 8 + j, lab + ", 1° ord.").font = f_bold
    row[0] += 1
    items = ["lordo", "netto", "prodotto", "logistica", "incasso", "assist", "contrib"]
    ilab = ["Prezzo pagato (IVA incl.)", "Ricavo netto IVA", "Costo del prodotto", "Logistica", "Commissione di incasso",
            "Assistenza e resi ordinari", "Contribuzione per ordine"]
    for it, lab in zip(items, ilab):
        put("e_" + it, lab, "€")
    for j, o in enumerate(offs):
        for base, sc in ((3, "0"), (8, pc("sconto"))):
            col = L(base + j)
            S[f"{col}{R['e_lordo']}"] = f"={pc('pz_'+o)}*(1-{sc})"
            S[f"{col}{R['e_netto']}"] = f"={col}{R['e_lordo']}/(1+{pc('iva')})"
            S[f"{col}{R['e_prodotto']}"] = f"={pc('costo')}*{pc('fl_'+o)}"
            S[f"{col}{R['e_logistica']}"] = f"={pc('pick')}+{pc('co_'+o)}"
            S[f"{col}{R['e_incasso']}"] = f"={col}{R['e_lordo']}*{pc('feep')}+{pc('feef')}"
            S[f"{col}{R['e_assist']}"] = f"={col}{R['e_netto']}*{pc('ass')}"
            S[f"{col}{R['e_contrib']}"] = (f"={col}{R['e_netto']}-{col}{R['e_prodotto']}-{col}{R['e_logistica']}"
                                           f"-{col}{R['e_incasso']}-{col}{R['e_assist']}")
            for it in items: S[f"{col}{R['e_'+it]}"].number_format = EUR2
    E = lambda it, o, first=False: f"${L((8 if first else 3) + offs.index(o))}${R['e_'+it]}"
    # --- sequenze di ordini per abbonamento e singolo
    title("Sequenza degli invii: abbonamento e flacone singolo (colonna = invio k)")
    rk = put("k", "Invio k"); ra = put("abb_eta", "Abbonamento: mese di età dell'invio"); rs = put("abb_sopr", "Abbonamento: clienti ancora attivi")
    rsa = put("sing_eta", "Singolo: mese di età dell'acquisto"); rss = put("sing_sopr", "Singolo: probabilità dell'acquisto")
    for k in range(1, KMAX + 1):
        col = L(2 + k)
        S[f"{col}{rk}"] = k
        S[f"{col}{ra}"] = f"=INT({pc('int_abb')}*({col}{rk}-1)/{pc('gm')}+0.5)"
        S[f"{col}{rsa}"] = f"=INT({pc('int_sing')}*({col}{rk}-1)/{pc('gm')}+0.5)"
        if k == 1:
            S[f"{col}{rs}"] = 1; S[f"{col}{rss}"] = 1
        else:
            prev = L(1 + k); rr_ = f"r{min(k-1, 6)}"
            S[f"{col}{rs}"] = f"={prev}{rs}*{pc(rr_)}"
            S[f"{col}{rss}"] = f"={prev}{rss}*{pc('rs')}"
        S[f"{col}{rs}"].number_format = NUM3; S[f"{col}{rss}"].number_format = NUM3
    kr = f"$C${ra}:${L(2+KMAX)}${ra}"; ks = f"$C${rs}:${L(2+KMAX)}${rs}"
    kra = f"$C${rsa}:${L(2+KMAX)}${rsa}"; kss = f"$C${rss}:${L(2+KMAX)}${rss}"
    # --- vettori per età
    title("Ordini e rimborsi per cliente iniziale, per mese di età (0 = mese dell'acquisto)")
    rage = put("eta", "Età (mesi)")
    v_p6 = put("v_p6", "Percorso 6: ordini"); v_r6 = put("v_r6", "Percorso 6: rimborsi di garanzia")
    v_p3 = put("v_p3", "Percorso 3: ordini"); v_ab = put("v_abb", "Abbonamento: ordini"); v_si = put("v_sing", "Singolo: ordini")
    cum = {o: put("cum_" + o, f"{lab}: contribuzione cumulata", "€") for o, lab in zip(offs, labs)}
    cmed = put("cum_med", "Cliente medio (mix): contribuzione cumulata", "€")
    for a in range(ETA):
        col = L(3 + a); e = f"{col}{rage}"
        S[f"{col}{rage}"] = a
        S[f"{col}{v_p6}"] = (f"=IF({e}=0,1,IF(MOD({e},6)=0,{pc('compl')}*(1-{pc('gar')})*{pc('rp6')}*{pc('rp6s')}^({e}/6-1),0))")
        S[f"{col}{v_r6}"] = f"=IF(OR({e}=5,{e}=6),{pc('compl')}*{pc('gar')}/2,0)"
        S[f"{col}{v_p3}"] = f"=IF({e}=0,1,IF(MOD({e},3)=0,{pc('rp3')}*{pc('rp3s')}^({e}/3-1),0))"
        S[f"{col}{v_ab}"] = f"=SUMIF({kr},{e},{ks})"
        S[f"{col}{v_si}"] = f"=SUMIF({kra},{e},{kss})"
        for rr_ in (v_p6, v_r6, v_p3, v_ab, v_si): S[f"{col}{rr_}"].number_format = NUM3
        for o, vr in (("p6", v_p6), ("p3", v_p3), ("abb", v_ab), ("sing", v_si)):
            if a == 0:
                f = f"={E('contrib', o, True)}+({col}{vr}-1)*{E('contrib', o)}"
            else:
                f = f"={L(2+a)}{cum[o]}+{col}{vr}*{E('contrib', o)}"
            if o == "p6":
                f += f"-{col}{v_r6}*{E('netto', 'p6', True)}"
            S[f"{col}{cum[o]}"] = f; S[f"{col}{cum[o]}"].number_format = EUR2
        S[f"{col}{cmed}"] = "=" + "+".join(f"{pc('mix_'+o)}*{col}{cum[o]}" for o in offs)
        S[f"{col}{cmed}"].number_format = EUR2
    # --- clienti per mese
    title("Clienti nuovi per mese")
    rm = put("mese", "Mese"); rrel = put("rel", "Mesi dal lancio")
    rpub = put("pubbl", "Pubblicità", "€"); rcac = put("cac", "CAC pubblicitario", "€")
    rnp = put("n_pag", "Nuovi clienti da pubblicità"); rno = put("n_org", "Nuovi clienti da canali non pagati")
    rn = put("n_tot", "Nuovi clienti totali")
    rno_ = {o: put("n_" + o, f"Nuovi clienti: {lab}") for o, lab in zip(offs, labs)}
    rcre = put("creativi", "Creatività e gestione campagne", "€")
    d1, d2, d3 = pc("d1"), pc("d2"), pc("d3")
    for m in range(1, MESI + 1):
        col = L(2 + m); rel = f"{col}{rrel}"
        S[f"{col}{rm}"] = m; S[f"{col}{rrel}"] = f"={col}{rm}-{pc('lancio')}"
        S[f"{col}{rpub}"] = (f"=IF({rel}<0,0,IF({rel}<{d1},{pc('s1')}/{d1},IF({rel}<{d1}+{d2},{pc('s2')}/{d2},"
                             f"IF({rel}<{d1}+{d2}+{d3},{pc('s3')}/{d3},{pc('pd')}))))")
        S[f"{col}{rcac}"] = (f"=IF({rel}<0,0,IF({rel}<{d1},{pc('c1')},IF({rel}<{d1}+{d2},{pc('c2')},"
                             f"IF({rel}<{d1}+{d2}+{d3},{pc('c3')},{pc('cd')}))))")
        S[f"{col}{rnp}"] = f"=IF({col}{rpub}>0,{col}{rpub}/{col}{rcac},0)"
        S[f"{col}{rno}"] = f"=IF({rel}>=0,{pc('org')},0)"
        S[f"{col}{rn}"] = f"={col}{rnp}+{col}{rno}"
        for o in offs: S[f"{col}{rno_[o]}"] = f"={col}{rn}*{pc('mix_'+o)}"
        S[f"{col}{rcre}"] = f"=IF({col}{rpub}>0,{pc('cre')},0)"
        for rr_ in (rpub, rcac, rcre): S[f"{col}{rr_}"].number_format = EUR
        for rr_ in [rnp, rno, rn] + list(rno_.values()): S[f"{col}{rr_}"].number_format = NUM1
    # --- matrici coorte x mese
    mats = {}
    for key, lab, vr, src in (("p6", "Percorso 6: ordini", v_p6, "p6"), ("r6", "Percorso 6: rimborsi", v_r6, "p6"),
                              ("p3", "Percorso 3: ordini", v_p3, "p3"), ("abb", "Abbonamento: ordini", v_ab, "abb"),
                              ("sing", "Singolo: ordini", v_si, "sing")):
        title(f"{lab} per coorte (righe = mese di acquisizione, colonne = mese di calendario)")
        top = row[0]
        for a in range(1, MESI + 1):
            S.cell(top + a - 1, 1, f"Coorte del mese {a}").font = f_note
            for m in range(1, MESI + 1):
                col = L(2 + m)
                if m < a:
                    S[f"{col}{top+a-1}"] = 0
                else:
                    S[f"{col}{top+a-1}"] = (f"=${L(2+a)}${rno_[src]}*INDEX(${L(3)}${vr}:${L(2+ETA)}${vr},1,{m-a+1})")
                S[f"{col}{top+a-1}"].number_format = NUM1
        row[0] = top + MESI
        tot = put("t_" + key, f"Totale {lab.lower()}")
        for m in range(1, MESI + 1):
            col = L(2 + m); S[f"{col}{tot}"] = f"=SUM({col}{top}:{col}{top+MESI-1})"; S[f"{col}{tot}"].number_format = NUM1
            S[f"{col}{tot}"].font = f_bold
        mats[key] = tot
    # --- flussi mensili
    title("Vendite e costi variabili per mese")
    rinc = put("incassi", "Incassi lordi (IVA incl.)", "€"); rric = put("ricavi", "Ricavi netti IVA", "€")
    rivv = put("iva_v", "IVA sulle vendite", "€"); rrl = put("rimb", "Rimborsi di garanzia pagati (lordi)", "€")
    rivr = put("iva_r", "IVA recuperata sui rimborsi", "€"); rlog = put("log", "Logistica (netto IVA)", "€")
    rcom = put("comm", "Commissioni di incasso", "€"); rass = put("assist", "Assistenza e resi ordinari", "€")
    rcogs = put("cogs", "Costo del prodotto venduto (competenza)", "€")
    rfl = put("flaconi", "Flaconi spediti con gli ordini"); rcmp = put("campioni", "Campioni"); rsos = put("sost", "Sostituzioni")
    def summ(col, it):
        parts = []
        for o in offs:
            first = f"{col}{rno_[o]}"; allo = f"{col}{mats[o]}"
            parts.append(f"{first}*{E(it, o, True)}+({allo}-{first})*{E(it, o)}")
        return "=" + "+".join(parts)
    for m in range(1, MESI + 1):
        col = L(2 + m)
        S[f"{col}{rinc}"] = summ(col, "lordo"); S[f"{col}{rric}"] = summ(col, "netto")
        S[f"{col}{rivv}"] = f"={col}{rinc}-{col}{rric}"
        S[f"{col}{rrl}"] = f"={col}{mats['r6']}*{E('lordo', 'p6', True)}"
        S[f"{col}{rivr}"] = f"={col}{mats['r6']}*({E('lordo', 'p6', True)}-{E('netto', 'p6', True)})"
        S[f"{col}{rlog}"] = summ(col, "logistica"); S[f"{col}{rcom}"] = summ(col, "incasso")
        S[f"{col}{rass}"] = summ(col, "assist"); S[f"{col}{rcogs}"] = summ(col, "prodotto")
        S[f"{col}{rfl}"] = "=" + "+".join(f"{col}{mats[o]}*{pc('fl_'+o)}" for o in offs)
        S[f"{col}{rcmp}"] = f"=IF({col}{rrel}=0,{pc('camp_l')},IF({col}{rrel}>0,{pc('camp_m')},0))"
        S[f"{col}{rsos}"] = f"={col}{rfl}*{pc('sost')}"
        for rr_ in (rinc, rric, rivv, rrl, rivr, rlog, rcom, rass, rcogs): S[f"{col}{rr_}"].number_format = EUR
        for rr_ in (rfl, rcmp, rsos): S[f"{col}{rr_}"].number_format = NUM1
    # --- costi di progetto nello scenario
    title("Costi di progetto nello scenario (mese effettivo)")
    top = row[0]; n = len(PROG)
    S.cell(top - 1, 3, "Mese").font = f_bold; S.cell(top - 1, 4, "Importo").font = f_bold; S.cell(top - 1, 5, "IVA").font = f_bold
    for i in range(n):
        rr_ = top + i; g = GR0 + i
        S.cell(rr_, 1, f"=Progetto!A{g}").font = f_link
        S[f"C{rr_}"] = f"=Progetto!B{g}+IF(Progetto!C{g}=\"sì\",{pc('lancio')}-16,0)"
        S[f"D{rr_}"] = f"=Progetto!D{g}"; S[f"E{rr_}"] = f"=Progetto!D{g}*Progetto!E{g}*{pc('iva')}"
        for c_ in "CDE": S[f"{c_}{rr_}"].font = f_link
    for i, (k_, mm) in enumerate((("x10", 10), ("x11", 11))):
        rr_ = top + n + i
        S.cell(rr_, 1, "Ciclo di laboratorio aggiuntivo").font = f_norm
        S[f"C{rr_}"] = mm; S[f"D{rr_}"] = f"={pc(k_)}"; S[f"E{rr_}"] = f"=D{rr_}*{pc('iva')}"
    bot = top + n + 1; row[0] = bot + 1
    for rr_ in range(top, bot + 1):
        S[f"D{rr_}"].number_format = EUR; S[f"E{rr_}"].number_format = EUR
    pm = f"$C${top}:$C${bot}"; pd_ = f"$D${top}:$D${bot}"; pv = f"$E${top}:$E${bot}"
    # --- scorte
    title("Scorte e lotti di produzione")
    rcons = put("consumo", "Consumo di flaconi (ordini, campioni, sostituzioni)")
    rarr = put("arrivi", "Flaconi in arrivo dal lotto"); rstk = put("stock", "Flaconi in magazzino a fine mese")
    rmed = put("media", "Consumo medio degli ultimi due mesi"); rpr = put("punto", "Punto di riordino")
    rord = put("ordine", "Lotto ordinato nel mese"); racq = put("acquisti", "Pagamenti ai produttori (netto IVA)", "€")
    for m in range(1, MESI + 1):
        col = L(2 + m); prv = L(1 + m)
        S[f"{col}{rcons}"] = f"={col}{rfl}+{col}{rcmp}+{col}{rsos}"
        S[f"{col}{rarr}"] = f"={L(m)}{rord}" if m >= 3 else 0
        prev_stock = f"{prv}{rstk}" if m > 1 else "0"
        S[f"{col}{rstk}"] = (f"={prev_stock}+{col}{rarr}*(1-{pc('scarto')})-IF({col}{rarr}>0,{pc('tratt')},0)-{col}{rcons}")
        S[f"{col}{rmed}"] = f"=AVERAGE({prv}{rcons}:{col}{rcons})" if m > 1 else f"={col}{rcons}"
        S[f"{col}{rpr}"] = f"={col}{rmed}*({pc('tempo')}+{pc('sic')})"
        pipe = f"{prv}{rord}" if m > 1 else "0"
        S[f"{col}{rord}"] = (f"=IF({col}{rrel}=-3,{pc('lotto')},IF(AND({col}{rrel}>=0,{col}{rstk}+{pipe}<={col}{rpr}),{pc('lotto')},0))")
        S[f"{col}{racq}"] = f"={col}{rord}*{pc('costo')}*{pc('ant')}+{col}{rarr}*{pc('costo')}*(1-{pc('ant')})"
        for rr_ in (rcons, rarr, rstk, rmed, rpr, rord): S[f"{col}{rr_}"].number_format = NUM1
        S[f"{col}{racq}"].number_format = EUR
    # --- costi fissi
    title("Costi fissi")
    rfx = put("fissi", "Costi fissi (netto IVA)", "€"); rfxi = put("fissi_iva", "IVA sui costi fissi", "€")
    for m in range(1, MESI + 1):
        col = L(2 + m); mm = f"{col}{rm}"; Lc = pc("lancio")
        S[f"{col}{rfx}"] = (f"=100+250+40+IF({mm}>=10,IF({mm}<{Lc},30,80),0)+IF({mm}>={Lc}-1,100,0)"
                            f"+IF(OR({mm}=3,{mm}=15,{mm}=27),430,0)+IF(OR({mm}={Lc},{mm}={Lc}+12),1200,0)")
        S[f"{col}{rfxi}"] = f"=(250+40*0.5+IF({mm}>={Lc}-1,100,0))*{pc('iva')}"
        S[f"{col}{rfx}"].number_format = EUR; S[f"{col}{rfxi}"].number_format = EUR
    S.cell(row[0], 1, "Abbonamenti IA 100 (Fable 5.1 e ASTRA di OpenAI) · commercialista 250 · banca, PEC, dominio 40 · piattaforma e-commerce 30, poi 80 dal lancio · "
                     "magazzino 100 dal mese prima del lancio · diritto camerale e libri sociali 430 nei mesi 3, 15, 27 · assicurazione RC prodotto 1.200 all'anno").font = f_note
    row[0] += 1
    # --- IVA
    title("IVA: posizione mensile, compensazione, versamenti")
    rpro = put("progetto", "Costi di progetto (netto IVA)", "€"); rproi = put("progetto_iva", "IVA sui costi di progetto", "€")
    riva_a = put("iva_acq", "IVA pagata ai fornitori nel mese", "€"); rnet = put("iva_net", "IVA del mese: vendite meno rimborsi meno acquisti", "€")
    rtmp = put("iva_tmp", "Posizione prima del versamento", "€"); rdue = put("iva_due", "IVA da versare il mese successivo", "€")
    rpos = put("iva_pos", "Posizione dopo il versamento (negativo = credito)", "€")
    rver = put("iva_ver", "IVA versata nel mese", "€"); rcred = put("credito", "Credito IVA a fine mese", "€")
    for m in range(1, MESI + 1):
        col = L(2 + m); prv = L(1 + m)
        S[f"{col}{rpro}"] = f"=SUMIF({pm},{col}{rm},{pd_})"; S[f"{col}{rproi}"] = f"=SUMIF({pm},{col}{rm},{pv})"
        S[f"{col}{riva_a}"] = f"={col}{rproi}+{col}{rfxi}+{col}{racq}*{pc('iva')}+{col}{rlog}*{pc('iva')}"
        S[f"{col}{rnet}"] = f"={col}{rivv}-{col}{rivr}-{col}{riva_a}"
        S[f"{col}{rtmp}"] = (f"={prv}{rpos}+{col}{rnet}" if m > 1 else f"={col}{rnet}")
        S[f"{col}{rdue}"] = f"=MAX(0,{col}{rtmp})"; S[f"{col}{rpos}"] = f"=MIN(0,{col}{rtmp})"
        S[f"{col}{rver}"] = f"={prv}{rdue}" if m > 1 else 0
        S[f"{col}{rcred}"] = f"=-{col}{rpos}"
        for rr_ in (rpro, rproi, riva_a, rnet, rtmp, rdue, rpos, rver, rcred): S[f"{col}{rr_}"].number_format = EUR
    # --- cassa
    title("Cassa")
    rcap = put("capitale", "Capitale versato", "€"); rent = put("entrate", "Entrate: capitale e incassi", "€")
    rusc = put("uscite", "Uscite totali", "€"); rcas = put("cassa", "Cassa a fine mese", "€")
    rexp = put("esposizione", "Garanzia: rimborsi attesi non ancora pagati (lordi)", "€")
    rop = put("operativo", "Risultato operativo del mese (competenza semplificata)", "€")
    for m in range(1, MESI + 1):
        col = L(2 + m); prv = L(1 + m)
        S[f"{col}{rcap}"] = f"=IF({col}{rm}=1,{pc('k1')},0)+IF({col}{rm}={pc('k2m')},{pc('k2')},0)"
        S[f"{col}{rent}"] = f"={col}{rcap}+{col}{rinc}"
        S[f"{col}{rusc}"] = (f"={col}{rrl}+{col}{rlog}*(1+{pc('iva')})+{col}{rcom}+{col}{rass}+{col}{rpub}+{col}{rcre}"
                             f"+{col}{rpro}+{col}{rproi}+{col}{rfx}+{col}{rfxi}+{col}{racq}*(1+{pc('iva')})+{col}{rver}")
        S[f"{col}{rcas}"] = (f"={prv}{rcas}+{col}{rent}-{col}{rusc}" if m > 1 else f"={col}{rent}-{col}{rusc}")
        S[f"{col}{rexp}"] = (f"=SUM($C${rno_['p6']}:{col}{rno_['p6']})*{pc('compl')}*{pc('gar')}*{E('lordo', 'p6', True)}"
                             f"-SUM($C${rrl}:{col}{rrl})")
        S[f"{col}{rop}"] = (f"={col}{rric}-{col}{rcogs}-{col}{rlog}-{col}{rcom}-{col}{rass}-({col}{rrl}-{col}{rivr})"
                            f"-{col}{rpub}-{col}{rcre}-{col}{rfx}")
        for rr_ in (rcap, rent, rusc, rcas, rexp, rop): S[f"{col}{rr_}"].number_format = EUR
        S[f"{col}{rcas}"].font = f_bold; S[f"{col}{rcas}"].fill = fill_key
    # --- sintesi
    title("Sintesi dello scenario")
    rng = lambda rr_: f"$C${rr_}:${L(2+MESI)}${rr_}"
    out = {}
    def res(key, label, formula, fmt=EUR):
        rr_ = put("o_" + key, label); S[f"C{rr_}"] = formula; S[f"C{rr_}"].number_format = fmt; S[f"C{rr_}"].font = f_bold
        out[key] = f"'{name}'!$C${rr_}"
    res("min", "Cassa minima", f"=MIN({rng(rcas)})")
    res("mese_min", "Mese della cassa minima", f"=INDEX({rng(rm)},1,MATCH(MIN({rng(rcas)}),{rng(rcas)},0))", "0")
    res("fabb", "Capitale assorbito fino al minimo (versato meno cassa minima)", f"=SUM({rng(rcap)})-MIN({rng(rcas)})")
    res("c24", "Cassa al mese 24", f"=${L(2+24)}${rcas}")
    res("c30", "Cassa al mese 30", f"=${L(2+30)}${rcas}")
    res("clienti", "Nuovi clienti fino al mese 30", f"=SUM({rng(rn)})", "#,##0")
    res("pagati", "di cui da pubblicità", f"=SUM({rng(rnp)})", "#,##0")
    res("pubbl", "Pubblicità fino al mese 30", f"=SUM({rng(rpub)})")
    res("ricavi", "Ricavi netti fino al mese 30", f"=SUM({rng(rric)})")
    res("rimb", "Rimborsi di garanzia pagati fino al mese 30", f"=SUM({rng(rrl)})")
    res("lotti", "Lotti ordinati", f"=SUM({rng(rord)})/{pc('lotto')}", "0")
    res("cred", "Credito IVA massimo", f"=MAX({rng(rcred)})")
    res("esp", "Esposizione di garanzia massima", f"=MAX({rng(rexp)})")
    res("v6", "Valore del cliente medio a 6 mesi", f"=${L(3+5)}${cmed}", EUR2)
    res("v12", "Valore del cliente medio a 12 mesi", f"=${L(3+11)}${cmed}", EUR2)
    res("v24", "Valore del cliente medio a 24 mesi", f"=${L(3+23)}${cmed}", EUR2)
    res("cacmax", "CAC massimo con la regola 2:1 sul valore a 24 mesi", f"=${L(3+23)}${cmed}/2", EUR2)
    res("primo", "Contribuzione media del primo ordine", f"=$C${cmed}", EUR2)
    S.column_dimensions["A"].width = 58; S.column_dimensions["B"].width = 9
    for j in range(3, 3 + KMAX): S.column_dimensions[L(j)].width = 11
    S.freeze_panes = "C4"
    return R, out, cum, cmed

OUT = {}; ROWS = {}
for i, nm in enumerate(SHEETS, 1):
    R, out, cum, cmed = build_scenario(i, nm); OUT[nm] = out; ROWS[nm] = (R, cum, cmed)

# ------------------------------------------------------------------ Confronto
C = wb.create_sheet("Confronto", 1)
C["A1"] = "Confronto fra scenari"; C["A1"].font = f_title
C["A2"] = "Tutti i valori sono collegamenti ai fogli di scenario: cambiano quando cambiano i Parametri."; C["A2"].font = f_note
for j, h in enumerate(["Risultato"] + SCEN, 1):
    c = C.cell(4, j, h); c.font = f_bold; c.fill = fill_head; c.alignment = Alignment(wrap_text=True)
voci = [("min", "Cassa minima", EUR), ("mese_min", "Mese della cassa minima", "0"),
        ("fabb", "Capitale assorbito fino al minimo", EUR), ("c24", "Cassa al mese 24", EUR), ("c30", "Cassa al mese 30", EUR),
        ("clienti", "Nuovi clienti fino al mese 30", "#,##0"), ("pagati", "di cui da pubblicità", "#,##0"),
        ("pubbl", "Pubblicità fino al mese 30", EUR), ("ricavi", "Ricavi netti fino al mese 30", EUR),
        ("rimb", "Rimborsi di garanzia pagati", EUR), ("esp", "Esposizione di garanzia massima", EUR),
        ("cred", "Credito IVA massimo", EUR), ("lotti", "Lotti di produzione ordinati", "0"),
        ("primo", "Contribuzione media del primo ordine", EUR2), ("v12", "Valore del cliente medio a 12 mesi", EUR2),
        ("v24", "Valore del cliente medio a 24 mesi", EUR2), ("cacmax", "CAC massimo (regola 2:1 sul valore a 24 mesi)", EUR2)]
for i, (k, lab, fmt) in enumerate(voci):
    C.cell(5 + i, 1, lab).font = f_norm
    for j, nm in enumerate(SHEETS):
        c = C.cell(5 + i, 2 + j, "=" + OUT[nm][k]); c.number_format = fmt; c.font = f_link
C.column_dimensions["A"].width = 50
for j in range(5): C.column_dimensions[L(2 + j)].width = 16

# ------------------------------------------------------------------ Unitaria
U = wb.create_sheet("Unitaria", 2)
U["A1"] = "Economia per ordine e per cliente (scenario base)"; U["A1"].font = f_title
U["A2"] = "Collegata al foglio S1 Base. Per altri valori si cambiano i Parametri."; U["A2"].font = f_note
R1, cum1, cmed1 = ROWS["S1 Base"]; s1 = "'S1 Base'"
labs = ["Percorso 6", "Percorso 3", "Abbonamento", "Singolo"]
for j, h in enumerate(["Per ordine (successivo)"] + labs, 1):
    c = U.cell(4, j, h); c.font = f_bold; c.fill = fill_head
items = [("lordo", "Prezzo pagato"), ("netto", "Ricavo netto IVA"), ("prodotto", "Costo del prodotto"), ("logistica", "Logistica"),
         ("incasso", "Commissione di incasso"), ("assist", "Assistenza e resi ordinari"), ("contrib", "Contribuzione")]
for i, (it, lab) in enumerate(items):
    U.cell(5 + i, 1, lab).font = f_norm
    for j in range(4):
        c = U.cell(5 + i, 2 + j, f"={s1}!{L(3+j)}{R1['e_'+it]}"); c.number_format = EUR2; c.font = f_link
U.cell(12, 1, "Contribuzione in % del ricavo netto").font = f_norm
U.cell(13, 1, "Contribuzione in % del prezzo pagato").font = f_norm
for j in range(4):
    col = L(2 + j)
    U[f"{col}12"] = f"={col}11/{col}6"; U[f"{col}12"].number_format = PCT
    U[f"{col}13"] = f"={col}11/{col}5"; U[f"{col}13"].number_format = PCT
for j, h in enumerate(["Valore per cliente (contribuzione cumulata)"] + labs + ["Cliente medio"], 1):
    c = U.cell(15, j, h); c.font = f_bold; c.fill = fill_head
for i, h in enumerate((1, 3, 6, 12, 24, 36)):
    U.cell(16 + i, 1, f"entro {h} mesi").font = f_norm
    for j, o in enumerate(["p6", "p3", "abb", "sing"]):
        c = U.cell(16 + i, 2 + j, f"={s1}!{L(2+h)}{cum1[o]}"); c.number_format = EUR2; c.font = f_link
    c = U.cell(16 + i, 6, f"={s1}!{L(2+h)}{cmed1}"); c.number_format = EUR2; c.font = f_link
# rimborsi sul percorso da sei
U.cell(23, 1, "Percorso da 6: contribuzione del primo ordine al variare dei rimborsi").font = f_bold; U.cell(23, 1).fill = fill_head
for j, h in enumerate(["Rimborsi sul totale", "Contribuzione", "Dopo CAC 50", "Dopo CAC 60", "Dopo CAC 80"], 1):
    U.cell(24, j, h).font = f_bold
c6 = f"{s1}!$H${R1['e_contrib']}"; n6 = f"{s1}!$H${R1['e_netto']}"
for i, q in enumerate((0.05, 0.121, 0.20, 0.30)):
    rr = 25 + i
    c = U.cell(rr, 1, q); c.number_format = PCT; c.font = f_input; c.fill = fill_in
    U[f"B{rr}"] = f"={c6}-A{rr}*{n6}"
    for j, cac in enumerate((50, 60, 80)):
        U[f"{L(3+j)}{rr}"] = f"=B{rr}-{cac}"
    for col in "BCDE": U[f"{col}{rr}"].number_format = EUR2
U.cell(29, 1, "Pareggio sul primo ordine").font = f_norm
for j, cac in enumerate((50, 60, 80)):
    U[f"{L(3+j)}29"] = f"=({c6}-{cac})/{n6}"; U[f"{L(3+j)}29"].number_format = PCT
# costo industriale
U.cell(31, 1, "Sensibilità al costo industriale (tutte le altre ipotesi del base)").font = f_bold; U.cell(31, 1).fill = fill_head
for j, h in enumerate(["Costo per flacone", "Valore a 24 mesi", "CAC massimo 2:1"], 1):
    U.cell(32, j, h).font = f_bold
fl = {"p6": 6, "p3": 3, "abb": 1, "sing": 1}
# valore a 24 mesi = valore base + (costo base - costo) * flaconi attesi entro 24 mesi, pesati per il mix
for i, cst in enumerate((5.35, 8.50, 11.90)):
    rr = 33 + i
    c = U.cell(rr, 1, cst); c.number_format = EUR2; c.font = f_input; c.fill = fill_in
    parts = []
    for o in ["p6", "p3", "abb", "sing"]:
        vrow = {"p6": R1["v_p6"], "p3": R1["v_p3"], "abb": R1["v_abb"], "sing": R1["v_sing"]}[o]
        parts.append(f"{s1}!$C${R1['p_mix_'+o]}*SUM({s1}!$C${vrow}:${L(2+24)}${vrow})*{fl[o]}")
    U[f"B{rr}"] = f"={s1}!${L(2+24)}${cmed1}+({s1}!$C${R1['p_costo']}-A{rr})*(" + "+".join(parts) + ")"
    U[f"C{rr}"] = f"=B{rr}/2"
    U[f"B{rr}"].number_format = EUR2; U[f"C{rr}"].number_format = EUR2
U.column_dimensions["A"].width = 52
for c in "BCDEF": U.column_dimensions[c].width = 15

from openpyxl.workbook.properties import CalcProperties
wb.calculation = CalcProperties(fullCalcOnLoad=True)
wb.save("/home/user/clauderesearch/analisi/modello/modello-cassa.xlsx")
print("ok")
