"""Genera mappa-competitiva.xlsx: griglia di rilevazione dei concorrenti.

Rigenerare il file sovrascrive la compilazione manuale: usarlo solo per ricostruire la griglia.
"""
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter as L
from openpyxl.worksheet.datavalidation import DataValidation

F = "Arial"
fb, fn, fi, fnote = Font(name=F, size=10, bold=True), Font(name=F, size=10), Font(name=F, size=10, color="0000FF"), Font(name=F, size=9, italic=True, color="555555")
ft = Font(name=F, size=14, bold=True)
y, g, h = PatternFill("solid", fgColor="FFF2CC"), PatternFill("solid", fgColor="EDEDED"), PatternFill("solid", fgColor="D9E1F2")
EUR2 = '#,##0.00;(#,##0.00);"-"'
ULT = 200   # righe utili: la tabella si estende fino a qui senza toccare le formule

COL = [  # intestazione, larghezza, tipo (i = da compilare, c = calcolata)
 ("Marca", 20, "i"), ("Prodotto", 30, "i"), ("Tipo", 12, "i"), ("Gruppo", 12, "i"), ("Canale", 14, "i"), ("Mercato", 8, "i"),
 ("Codice confezione (EAN/minsan)", 16, "i"), ("URL prezzo", 22, "i"), ("Data prezzo", 11, "i"), ("URL dose", 22, "i"), ("Data dose", 11, "i"),
 ("Prezzo ordinario €", 11, "i"), ("Prezzo promo €", 10, "i"), ("Spedizione €", 10, "i"), ("Formato mL", 9, "i"),
 ("Dose dichiarata (testo esatto)", 30, "i"), ("mL al giorno", 9, "i"), ("Stato della dose", 14, "i"), ("Fase", 12, "i"),
 ("€/mL", 8, "c"), ("Durata nominale gg", 10, "c"), ("Residuo nel contenitore %", 10, "i"), ("Durata utilizzabile gg", 10, "c"),
 ("Costo 30 gg nominale €", 11, "c"), ("Costo 30 gg utilizzabile €", 11, "c"),
 ("Esborso minimo per provare €", 11, "i"), ("Esborso fino al primo risultato promesso €", 12, "i"), ("Giorni al primo risultato promesso", 10, "i"),
 ("Impegno e possibilità di interrompere", 24, "i"), ("Beneficio promesso", 14, "i"), ("Claim principale (testo esatto)", 34, "i"),
 ("Percentuali dichiarate", 12, "i"), ("Garanzia di rimborso", 11, "i"), ("Condizioni del rimborso", 28, "i"), ("Abbonamento", 11, "i"),
 ("Frizioni d'uso", 22, "i"), ("Stato della riga", 12, "i"), ("Note e fonti", 44, "i"),
]
IDX = {n: i + 1 for i, (n, _, _) in enumerate(COL)}
c = lambda name: L(IDX[name])

wb = Workbook()
# ------------------------------------------------------------------ Istruzioni
ist = wb.active; ist.title = "Istruzioni"
testo = [
 ("Mappa competitiva · istruzioni", ft),
 ("", None),
 ("A che cosa serve", fb),
 ("Confrontare quanto spende davvero il cliente con ciascuna alternativa: per provare, per arrivare al primo risultato promesso, e ogni 30 giorni.", fn),
 ("Il prezzo del flacone da solo non basta, perché le dosi giornaliere vanno da meno di mezzo millilitro a diversi millilitri.", fn),
 ("", None),
 ("La regola", fb),
 ("Una riga vale come fonte solo se una persona ha aperto le pagine e ha compilato URL e data sia del prezzo sia della dose, poi ha messo 'verificato'.", fn),
 ("Senza questi campi il dato non va usato in nessun documento. Il foglio Sintesi calcola minimi, massimi e medie solo sulle righe verificate.", fn),
 ("", None),
 ("Ordine di lavoro", fb),
 ("1. Le dieci righe del gruppo 'prioritario': sono le alternative che il nostro cliente considera davvero. Si completano per prime, per intero.", fn),
 ("2. Per ciascuna: codice della confezione, prezzo ordinario e promozionale, spedizione, dose con la sua fonte, fase del trattamento.", fn),
 ("3. Poi le colonne che servono alla decisione d'acquisto: esborso minimo, esborso fino al primo risultato promesso, impegno, garanzia.", fn),
 ("4. Il gruppo 'riferimento' si compila solo dopo, e solo se serve.", fn),
 ("", None),
 ("Come si legge la dose", fb),
 ("Si copia la frase esatta della confezione o della pagina nella colonna 'Dose dichiarata'. I millilitri al giorno si scrivono solo se la marca li dichiara", fn),
 ("o se si possono misurare (una pipetta si pesa). 'Stato della dose': verificata = dichiarata o misurata; intervallo = la marca dà un intervallo;", fn),
 ("dedotta = ricavata da una durata o da un ciclo di trattamento, e quindi NON utilizzabile per il costo; non disponibile = manca un dato.", fn),
 ("Una durata commerciale ('un mese di trattamento') non è una dose: un ciclo di tre mesi può richiedere più confezioni.", fn),
 ("", None),
 ("Residuo nel contenitore", fb),
 ("Si scrive solo se misurato. Se non è noto la cella resta vuota: non si inventa uno zero. Per KRINÉ il 5% è la nostra ipotesi, da misurare sul flacone scelto.", fn),
 ("", None),
 ("Colori", fb),
 ("Giallo: da compilare · Grigio: calcolato, non scrivere · Testo blu: valore inserito a mano", fn),
 ("Le righe KRINÉ sono escluse da tutti i conteggi e da tutte le statistiche della Sintesi.", fn),
]
for i, (t, f) in enumerate(testo, 1):
    ist.cell(i, 1, t)
    if f: ist.cell(i, 1).font = f
ist.column_dimensions["A"].width = 150

# ------------------------------------------------------------------ Mappa
m = wb.create_sheet("Mappa")
for j, (nome, w, tipo) in enumerate(COL, 1):
    cc = m.cell(1, j, nome); cc.font = fb; cc.fill = h; cc.alignment = Alignment(wrap_text=True, vertical="center")
    m.column_dimensions[L(j)].width = w
m.row_dimensions[1].height = 45
m.freeze_panes = "C2"

P, R = "prioritario", "riferimento"
S = "https://"
dati = [
 # marca, prodotto, tipo, gruppo, canale, mercato, codice, url prezzo, data prezzo, url dose, data dose, prezzo, promo, sped, mL,
 # dose testo, mL/g, stato dose, fase, residuo, esborso min, esborso primo ris., giorni primo ris., impegno, beneficio, claim,
 # % dich., garanzia, condizioni, abbon., frizioni, stato riga, note
 ("Minoxidil 5% (Biorga)", "Soluzione cutanea 60 mL", "farmaco", P, "farmacia", "IT", "", S + "www.redcare.it/medicinali/IT042311011/minoxidil-biorga-5-soluzione-cutanea.htm", "", "", "",
  31.89, None, None, 60, "1 mL due volte al giorno; massimo 2 mL al giorno", 2.0, "verificata", "unica", None, 31.89, None, 120,
  "Uso continuativo; sospendendo l'effetto si perde", "ricrescita (farmaco)", "Trattamento dell'alopecia androgenetica",
  "tutte", "no", "", "no", "Unge; può irritare; caduta iniziale possibile", "da verificare",
  "Farmaco senza obbligo di ricetta. Dose e tempi dal foglio illustrativo: almeno 4 mesi per vedere la ricrescita. Prezzi online visti fra 31,57 e 37,50 € (ricerca del 22/09/2026): da riaprire e datare"),
 ("Bioscalin (Giuliani)", "TricoAge siero concentrato", "concorrente", P, "farmacia", "IT", "", "", "", "", "",
  48.56, None, None, 40, "6 pipette ogni 3 giorni, ciclo di 3 mesi (da ricontrollare)", None, "dedotta", "iniziale", None, None, None, None,
  "", "caduta", "", "nessuna", "non verificato", "", "non verificato", "", "da verificare",
  "mL/giorno ricavati in passato dalla durata del ciclo: non valgono. Identificare versione e confezione, poi ricostruire la dose"),
 ("Vichy", "Dercos Aminexil Clinical 5", "concorrente", P, "farmacia", "IT", "", S + "www.idealo.it/confronta-prezzi/200464034/vichy-dercos-aminexil-clinical-5-trattamento-uomo-anticaduta.html", "", "", "",
  51.20, None, None, 126, "21 fiale da 6 mL. Due regimi riportati: 1 fiala al giorno oppure 3 a settimana", None, "non disponibile", "iniziale", None, 51.20, None, 42,
  "Cicli di trattamento", "caduta", "Riduce la caduta dei capelli temporanea (formulazione da verificare sulla confezione)",
  "nessuna", "non verificato", "", "non verificato", "Fiala monodose", "da verificare",
  "Con i prezzi provvisori: 1 fiala al giorno = 21 giorni e 73,14 €/30 gg; 3 a settimana = 49 giorni e 31,35 €/30 gg. Scegliere la fase da confrontare"),
 ("Ducray", "Neoptide (linea anticaduta, denominazione da aggiornare)", "concorrente", P, "farmacia", "IT", "", "", "", "", "",
  44.94, None, None, 90, "Spruzzi giornalieri per un ciclo di 3 mesi (da ricontrollare)", None, "dedotta", "iniziale", None, None, None, None,
  "", "caduta", "", "nessuna", "non verificato", "", "non verificato", "", "da verificare",
  "La gamma attuale ha denominazioni aggiornate: registrare il codice. mL/giorno ricavati dal ciclo: non valgono"),
 ("Crescina (Labo)", "Linea anticaduta", "concorrente", P, "farmacia", "IT", "", "", "", "", "",
  None, None, None, None, "", None, "non disponibile", "", None, None, None, None,
  "", "caduta", "", "", "non verificato", "", "non verificato", "", "da verificare", "da rilevare per intero"),
 ("Kérastase", "Genesis Sérum Anti-Chute Fortifiant", "concorrente", P, "salone e profumeria", "IT", "3474636858002",
  S + "www.kerastase.it/genesis/trattamento-serum-anti-chute-fortifiant/3474636858002.html", "", S + "www.kerastase.it/genesis/trattamento-serum-anti-chute-fortifiant/3474636858002.html", "",
  56.90, None, None, 90, "4 dosi al giorno, ogni dose = pipetta fino al segno; trattamento di 6 settimane", None, "non disponibile", "iniziale", None, 56.90, None, None,
  "", "rottura della fibra", "Riduce fino al 97% la caduta dovuta alla rottura da spazzolamento (da verificare)",
  "nessuna", "non verificato", "", "non verificato", "Pipetta", "da verificare",
  "Volume della pipetta non dichiarato: i 2,4 mL/giorno usati in passato venivano dalla durata, non valgono. Prezzi visti fra 34,90 e 56,90 €: forte sconto abituale"),
 ("The Ordinary", "Multi-Peptide Serum for Hair Density", "concorrente", P, "DTC e profumeria", "EU", "", "", "", "", "",
  26.50, None, None, 60, "", None, "non disponibile", "", None, 26.50, None, None,
  "", "aspetto", "", "alcune", "non verificato", "", "non verificato", "", "da verificare", "Prezzo dalla ricerca preliminare, da riaprire"),
 ("OUAI", "Scalp Serum", "concorrente", P, "profumeria", "IT", "", "", "", S + "theouai.com/products/scalp-serum", "",
  61.00, None, None, 60, "Due contagocce pieni, circa 1,5 mL; fino a 40 giorni per 60 mL", 1.5, "verificata", "unica", None, 61.00, None, None,
  "", "cute", "", "", "non verificato", "", "non verificato", "", "da verificare",
  "Dose e durata confermate dalla pagina ufficiale (risposta del marchio). Prezzo italiano di 61 € non ancora confermato"),
 ("Living Proof", "Scalp Care Density Serum", "concorrente", P, "profumeria", "IT", "", "", "", S + "www.livingproof.co.uk/products/scalp-care-density-serum", "",
  66.00, None, None, 50, "2-3 contagocce al giorno", None, "intervallo", "unica", None, 66.00, None, 90,
  "", "aspetto", "Capelli dall'aspetto più spesso e pieno; studio di 90 giorni su 30 persone (claim da leggere sulla pagina UE)",
  "", "non verificato", "", "non verificato", "Contagocce", "da verificare",
  "Volume del contagocce non dichiarato. Sul sito USA: in 90 giorni il 35% ha registrato più densità e il 70% meno caduta visibile"),
 ("Scandinavian Biolabs", "Bio-Pilixin Serum", "concorrente", P, "DTC", "EU", "", "", "", "", "",
  55.00, 39.00, None, 100, "Istruzioni e offerta da riconciliare: il flacone è presentato anche come fornitura mensile", None, "non disponibile", "unica", None, 55.00, 195.00, 150,
  "Garanzia legata a 150 giorni d'uso consecutivo", "aspetto", "", "", "sì",
  "150 giorni d'uso, foto mensili, 5 flaconi; richieste fuori dal periodo non ammesse. Leggere le condizioni integrali", "sì", "", "da verificare",
  S + "scandinavianbiolabs.com/pages/money-back-guarantee · i 50 giorni ricavati da 2 mL/giorno sono in conflitto con la 'fornitura mensile'"),
 ("The INKEY List", "Caffeine Stimulating Scalp Treatment", "concorrente", R, "DTC e profumeria", "EU", "", "", "", "", "",
  15.50, None, None, 150, "", None, "non disponibile", "", None, None, None, None, "", "cute", "", "alcune", "non verificato", "", "non verificato", "", "da verificare",
  "Dichiara 1% caffeina, 1% Redensyl, 1% betaina: la trasparenza parziale sulle percentuali esiste già"),
 ("Nioxin", "Night Density Rescue", "concorrente", R, "salone", "IT", "", "", "", "", "",
  60.69, None, None, 70, "2-4 pipette ogni sera", None, "intervallo", "", None, None, None, None, "", "aspetto", "", "", "non verificato", "", "non verificato", "", "da verificare", "Volume della pipetta da misurare"),
 ("Act+Acre", "Stem Cell Scalp Serum", "concorrente", R, "DTC", "EU", "", "", "", "", "", 89.00, None, None, 65, "", None, "non disponibile", "", None, None, None, None, "", "cute", "", "", "non verificato", "", "non verificato", "", "da verificare", ""),
 ("Augustinus Bader", "The Scalp Treatment", "concorrente", R, "profumeria", "IT", "", "", "", "", "", 89.00, None, None, 30, "", None, "non disponibile", "", None, None, None, None, "", "cute", "", "", "non verificato", "", "non verificato", "", "da verificare", ""),
 ("Aveda", "Scalp Solutions", "concorrente", R, "salone", "IT", "", "", "", "", "", 59.00, None, None, 50, "", None, "non disponibile", "", None, None, None, None, "", "cute", "", "", "non verificato", "", "non verificato", "", "da verificare", ""),
 ("Plantur", "DMG Clinical Serum", "concorrente", R, "farmacia e GDO", "DE", "", "", "", "", "", 19.99, None, None, 125, "", None, "non disponibile", "", None, None, None, None, "", "caduta", "", "", "non verificato", "", "non verificato", "", "da verificare", "Mercato tedesco"),
 ("Grow Gorgeous", "Density Serum Intense", "concorrente", R, "DTC", "EU", "", "", "", "", "", 50.00, None, None, 60, "", None, "non disponibile", "", None, None, None, None, "", "aspetto", "", "", "non verificato", "", "non verificato", "", "da verificare", ""),
 ("Foreo", "Dual-Peptide Scalp Serum", "concorrente", R, "profumeria", "IT", "", "", "", "", "", 52.90, None, None, 60, "", None, "non disponibile", "", None, None, None, None, "", "aspetto", "", "", "non verificato", "", "non verificato", "", "da verificare", ""),
 ("René Furterer", "Triphasic", "concorrente", R, "farmacia", "IT", "", "", "", "", "", None, None, None, None, "", None, "non disponibile", "", None, None, None, None, "", "caduta", "", "", "non verificato", "", "non verificato", "", "da verificare", "da rilevare"),
 ("Eucerin", "DermoCapillaire", "concorrente", R, "farmacia", "IT", "", "", "", "", "", None, None, None, None, "", None, "non disponibile", "", None, None, None, None, "", "caduta", "", "", "non verificato", "", "non verificato", "", "da verificare", "da rilevare"),
 ("Philip Kingsley", "Density Serum", "concorrente", R, "profumeria", "EU", "", "", "", "", "", None, None, None, None, "", None, "non disponibile", "", None, None, None, None, "", "aspetto", "", "", "non verificato", "", "non verificato", "", "da verificare", "da rilevare"),
 ("Alpecin", "Caffeine Liquid", "concorrente", R, "GDO", "DE", "", "", "", "", "", None, None, None, 200, "", None, "non disponibile", "", None, None, None, None, "", "caduta", "", "", "non verificato", "", "non verificato", "", "da verificare", "Canale diverso dal nostro"),
 ("Nutrafol", "Scalp Serum", "concorrente", R, "DTC", "US", "", "", "", "", "", None, None, None, 50, "", None, "non disponibile", "", None, None, None, None, "", "aspetto", "", "", "non verificato", "", "non verificato", "", "da verificare", "Mercato USA: utile per confronto, non per il prezzo italiano"),
 # KRINÉ
 ("KRINÉ", "Flacone singolo", "KRINÉ", "-", "DTC", "IT", "", "", "", "", "", 59.00, None, None, 60, "4 erogazioni da 0,5 mL, la sera", 2.0, "verificata", "unica", 0.05, 59.00, None, None,
  "Nessun impegno", "cute", "", "tutte", "no", "", "no", "", "nostro dato", "Residuo del 5%: ipotesi da misurare"),
 ("KRINÉ", "Abbonamento, invio ogni 28 giorni", "KRINÉ", "-", "DTC", "IT", "", "", "", "", "", 49.00, None, None, 60, "4 erogazioni da 0,5 mL, la sera", 2.0, "verificata", "unica", 0.05, 49.00, None, None,
  "Si interrompe in qualunque momento", "cute", "", "tutte", "no", "", "sì", "", "nostro dato", "Consegna ogni 28 giorni perché 57 mL utili durano 28,5 giorni: il prezzo in colonna L è per 28 giorni"),
 ("KRINÉ", "Percorso da 3 flaconi", "KRINÉ", "-", "DTC", "IT", "", "", "", "", "", 149.00, None, None, 180, "4 erogazioni da 0,5 mL, la sera", 2.0, "verificata", "unica", 0.05, 149.00, None, None,
  "Pagamento anticipato di 85 giorni", "cute", "", "tutte", "no", "", "no", "", "nostro dato", ""),
 ("KRINÉ", "Percorso da 6 flaconi", "KRINÉ", "-", "DTC", "IT", "", "", "", "", "", 279.00, None, None, 360, "4 erogazioni da 0,5 mL, la sera", 2.0, "verificata", "unica", 0.05, 279.00, 279.00, 150,
  "Pagamento anticipato di 171 giorni", "aspetto", "", "tutte", "sì", "Vedi capitolo 07 del piano", "no", "", "nostro dato",
  "342 mL utili = 171 giorni: coprono i 150 della garanzia"),
]
for i, d in enumerate(dati, start=2):
    (marca, prod, tipo, gruppo, canale, merc, cod, up, dp, ud, dd, prezzo, promo, sped, ml, dose, mlg, sdose, fase, resid,
     emin, eris, gris, imp, ben, claim, pdich, gar, cond, abb, friz, stato, note) = d
    vals = {"Marca": marca, "Prodotto": prod, "Tipo": tipo, "Gruppo": gruppo, "Canale": canale, "Mercato": merc,
            "Codice confezione (EAN/minsan)": cod, "URL prezzo": up, "Data prezzo": dp, "URL dose": ud, "Data dose": dd,
            "Prezzo ordinario €": prezzo, "Prezzo promo €": promo, "Spedizione €": sped, "Formato mL": ml,
            "Dose dichiarata (testo esatto)": dose, "mL al giorno": mlg, "Stato della dose": sdose, "Fase": fase,
            "Residuo nel contenitore %": resid, "Esborso minimo per provare €": emin,
            "Esborso fino al primo risultato promesso €": eris, "Giorni al primo risultato promesso": gris,
            "Impegno e possibilità di interrompere": imp, "Beneficio promesso": ben, "Claim principale (testo esatto)": claim,
            "Percentuali dichiarate": pdich, "Garanzia di rimborso": gar, "Condizioni del rimborso": cond, "Abbonamento": abb,
            "Frizioni d'uso": friz, "Stato della riga": stato, "Note e fonti": note}
    for k, v in vals.items():
        if v not in (None, ""):
            cc = m.cell(i, IDX[k], v); cc.font = fi
last = 1 + len(dati)
# formule e colori su tutte le righe utili
for r in range(2, ULT + 1):
    Lp, Lml, Lmg, Lres = f"{c('Prezzo ordinario €')}{r}", f"{c('Formato mL')}{r}", f"{c('mL al giorno')}{r}", f"{c('Residuo nel contenitore %')}{r}"
    Ldur, Lduu, Lsd = f"{c('Durata nominale gg')}{r}", f"{c('Durata utilizzabile gg')}{r}", f"{c('Stato della dose')}{r}"
    ok = lambda x: f"ISNUMBER({x}),{x}>0"
    m[f"{c('€/mL')}{r}"] = f'=IF(AND({ok(Lp)},{ok(Lml)}),{Lp}/{Lml},"")'
    m[f"{c('Durata nominale gg')}{r}"] = f'=IF(AND({ok(Lml)},{ok(Lmg)},OR({Lsd}="verificata",{Lsd}="intervallo")),{Lml}/{Lmg},"")'
    m[f"{c('Durata utilizzabile gg')}{r}"] = f'=IF(AND(ISNUMBER({Ldur}),ISNUMBER({Lres})),{Ldur}*(1-{Lres}),"")'
    m[f"{c('Costo 30 gg nominale €')}{r}"] = f'=IF(AND({ok(Lp)},ISNUMBER({Ldur})),{Lp}/{Ldur}*30,"")'
    m[f"{c('Costo 30 gg utilizzabile €')}{r}"] = f'=IF(AND({ok(Lp)},ISNUMBER({Lduu})),{Lp}/{Lduu}*30,"")'
    for j, (nome, w, tipo) in enumerate(COL, 1):
        cc = m.cell(r, j)
        if tipo == "c":
            cc.fill = g; cc.font = fn
            cc.number_format = EUR2 if "€" in nome else "0.0"
        elif r <= last:
            cc.fill = y
        if nome in ("Prezzo ordinario €", "Prezzo promo €", "Spedizione €", "Esborso minimo per provare €", "Esborso fino al primo risultato promesso €"):
            cc.number_format = EUR2
        if nome == "Residuo nel contenitore %": cc.number_format = "0%"
        cc.alignment = Alignment(vertical="top", wrap_text=nome in ("Note e fonti", "Dose dichiarata (testo esatto)", "Claim principale (testo esatto)", "Condizioni del rimborso"))
# menu a tendina
liste = {"Tipo": "concorrente,farmaco,KRINÉ", "Gruppo": "prioritario,riferimento,-",
         "Stato della dose": "verificata,intervallo,dedotta,non disponibile", "Fase": "iniziale,mantenimento,unica",
         "Beneficio promesso": "cute,rottura della fibra,aspetto,caduta,ricrescita (farmaco)",
         "Percentuali dichiarate": "nessuna,alcune,tutte,non verificato", "Garanzia di rimborso": "sì,no,non verificato",
         "Abbonamento": "sì,no,non verificato", "Stato della riga": "da verificare,verificato,nostro dato"}
for k, v in liste.items():
    dv = DataValidation(type="list", formula1=f'"{v}"', allow_blank=True); m.add_data_validation(dv)
    dv.add(f"{c(k)}2:{c(k)}{ULT}")

# ------------------------------------------------------------------ Sintesi
s = wb.create_sheet("Sintesi")
s["B2"] = "Che cosa dice la mappa"; s["B2"].font = ft
s["B3"] = "Solo righe di concorrenti e farmaci, escluse le righe KRINÉ. Le statistiche di costo usano solo righe verificate con dose verificata."; s["B3"].font = fnote
rg = lambda name: f"Mappa!${c(name)}$2:${c(name)}${ULT}"
NK = f'{rg("Tipo")},"<>KRINÉ"'   # sempre combinato con un altro criterio, che esclude le righe vuote
VER = f'{rg("Stato della riga")},"verificato"'
DV = f'{rg("Stato della dose")},"verificata"'
righe = [
 ("Righe di concorrenti e farmaci (una per marca)", f'=COUNTIF({rg("Tipo")},"concorrente")+COUNTIF({rg("Tipo")},"farmaco")', "0", "Le quattro righe KRINÉ sono offerte nostre e non entrano nei conteggi"),
 ("di cui del gruppo prioritario", f'=COUNTIFS({NK},{rg("Gruppo")},"prioritario")', "0", "Le alternative che il cliente considera davvero"),
 ("Righe verificate", f"=COUNTIFS({NK},{VER})", "0", "Finché è zero, la mappa non è una fonte"),
 ("Prioritarie verificate", f'=COUNTIFS({NK},{VER},{rg("Gruppo")},"prioritario")', "0", "Obiettivo: dieci su dieci"),
 ("Righe con dose verificata", f"=COUNTIFS({NK},{DV})", "0", "Le sole su cui si può calcolare un costo per 30 giorni"),
 ("", None, None, None),
 ("Costo per 30 giorni, minimo", f'=IF(COUNTIFS({NK},{VER},{DV})=0,"",_xlfn.MINIFS({rg("Costo 30 gg nominale €")},{NK},{VER},{DV}))', EUR2, "Solo righe verificate con dose verificata"),
 ("Costo per 30 giorni, massimo", f'=IF(COUNTIFS({NK},{VER},{DV})=0,"",_xlfn.MAXIFS({rg("Costo 30 gg nominale €")},{NK},{VER},{DV}))', EUR2, ""),
 ("Costo per 30 giorni, media", f'=IF(COUNTIFS({NK},{VER},{DV})=0,"",AVERAGEIFS({rg("Costo 30 gg nominale €")},{NK},{VER},{DV}))', EUR2, "Una media fra prodotti diversi non stabilisce il nostro prezzo"),
 ("KRINÉ percorso da 6: costo per 30 giorni utilizzabili",
  f'=IFERROR(IF(ISNUMBER(INDEX({rg("Costo 30 gg utilizzabile €")},MATCH("Percorso da 6 flaconi",{rg("Prodotto")},0))),INDEX({rg("Costo 30 gg utilizzabile €")},MATCH("Percorso da 6 flaconi",{rg("Prodotto")},0)),""),"")', EUR2, "Con il residuo del 5%"),
 ("KRINÉ flacone singolo: costo per 30 giorni utilizzabili",
  f'=IFERROR(IF(ISNUMBER(INDEX({rg("Costo 30 gg utilizzabile €")},MATCH("Flacone singolo",{rg("Prodotto")},0))),INDEX({rg("Costo 30 gg utilizzabile €")},MATCH("Flacone singolo",{rg("Prodotto")},0)),""),"")', EUR2, ""),
 ("", None, None, None),
 ("Dichiarano tutte le percentuali", f'=COUNTIFS({NK},{rg("Percentuali dichiarate")},"tutte")', "0", "Il farmaco le dichiara per legge"),
 ("Ne dichiarano alcune", f'=COUNTIFS({NK},{rg("Percentuali dichiarate")},"alcune")', "0", "La trasparenza parziale esiste già"),
 ("Non ne dichiarano nessuna", f'=COUNTIFS({NK},{rg("Percentuali dichiarate")},"nessuna")', "0", ""),
 ("Offrono una garanzia di rimborso", f'=COUNTIFS({NK},{rg("Garanzia di rimborso")},"sì")', "0", "Conta solo i 'sì'"),
 ("Garanzia non ancora verificata", f'=COUNTIFS({NK},{rg("Garanzia di rimborso")},"non verificato")', "0", ""),
 ("Hanno un abbonamento", f'=COUNTIFS({NK},{rg("Abbonamento")},"sì")', "0", "Conta solo i 'sì'"),
]
for i, (lab, f, fmt, nota) in enumerate(righe, 5):
    s.cell(i, 2, lab).font = fn
    if f:
        cc = s.cell(i, 3, f); cc.font = fb; cc.number_format = fmt
        s.cell(i, 4, nota).font = fnote
s["B25"] = "Le tre domande a cui questa tabella deve rispondere"; s["B25"].font = fb
for i, t in enumerate(["1. Quanto spende al mese chi usa l'alternativa più vicina a noi? Oggi lo sappiamo per due prodotti su dieci.",
                       "2. La trasparenza completa sulle percentuali è un terreno libero o è già occupato?",
                       "3. La garanzia di rimborso è un vantaggio o è già la norma per chi vende online?"], 26):
    s.cell(i, 2, t).font = fn
s.column_dimensions["B"].width = 56; s.column_dimensions["C"].width = 14; s.column_dimensions["D"].width = 70
from openpyxl.workbook.properties import CalcProperties
wb.calculation = CalcProperties(fullCalcOnLoad=True)
wb.save("mappa-competitiva.xlsx")
print("ok", last - 1, "righe")
