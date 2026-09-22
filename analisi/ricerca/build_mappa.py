from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

FONT = "Arial"
wb = Workbook()

ink   = Font(name=FONT, size=10)
bold  = Font(name=FONT, size=10, bold=True)
head  = Font(name=FONT, size=10, bold=True, color="FFFFFF")
blu   = Font(name=FONT, size=10, color="0000FF")          # dato inserito a mano
note  = Font(name=FONT, size=9, italic=True, color="666666")
h1    = Font(name=FONT, size=14, bold=True)
h2    = Font(name=FONT, size=11, bold=True)

fill_head = PatternFill("solid", fgColor="4A4238")
fill_todo = PatternFill("solid", fgColor="FFF6CC")        # da compilare
fill_calc = PatternFill("solid", fgColor="EFEFEF")        # calcolato
fill_noi  = PatternFill("solid", fgColor="E8F0E3")
thin = Side(style="thin", color="CCCCCC")
box  = Border(left=thin, right=thin, top=thin, bottom=thin)

# ---------------------------------------------------------------- ISTRUZIONI
ws = wb.active
ws.title = "Istruzioni"
ws.sheet_view.showGridLines = False
righe = [
 ("Mappa competitiva — come si compila", h1),
 ("", None),
 ("A che serve", h2),
 ("Rispondere con dati verificabili a tre domande che oggi restano opinioni:", ink),
 ("1. Quanto costa davvero un mese di trattamento, per noi e per ciascun concorrente.", ink),
 ("2. Chi dichiara le percentuali degli attivi, quante e quali.", ink),
 ("3. Che cosa promettono i concorrenti e con quali prove.", ink),
 ("", None),
 ("Regola di verifica", h2),
 ("Una riga vale solo se qualcuno ha aperto la pagina e ha scritto URL e data nelle colonne F e G.", ink),
 ("Le celle gialle sono da compilare. Quelle grigie si calcolano da sole: non scriverci dentro.", ink),
 ("Il testo blu segnala un valore inserito a mano; il nero segnala una formula.", ink),
 ("", None),
 ("Ordine di lavoro consigliato", h2),
 ("Primo giro — solo le colonne H, J, L, M su tutte le righe. Servono al costo mensile,", ink),
 ("che è la metrica che manca a tutta la nostra analisi. Bastano due ore.", ink),
 ("Secondo giro — colonne P, Q, R, T: cosa dichiarano e cosa promettono. Serve a capire", ink),
 ("se la trasparenza sulle percentuali è davvero un terreno libero.", ink),
 ("Terzo giro — colonne U, V, W: garanzie, abbonamenti, recensioni. Serve al modello economico.", ink),
 ("", None),
 ("Avvertenze su come si leggono le dosi", h2),
 ("La dose dichiarata è quasi sempre in pipette, contagocce o erogazioni, non in millilitri.", ink),
 ("Dove la marca non dichiara il volume per erogazione, o lo si misura, o si annota la stima", ink),
 ("nella colonna Y scrivendo da dove viene. Non lasciare una stima senza la sua origine.", ink),
 ("La colonna N non toglie il residuo del contenitore: per il nostro airless calcoliamo il 5%,", ink),
 ("per i contagocce altrui non lo sappiamo. È un confronto leggermente a nostro sfavore, e va bene così.", ink),
 ("", None),
 ("Che cosa NON mettere qui", h2),
 ("Giudizi, punteggi, impressioni. Questa tabella contiene solo cose che un terzo può ricontrollare", ink),
 ("aprendo lo stesso indirizzo. Le valutazioni stanno nel documento, non nel foglio.", ink),
]
for i,(t,f) in enumerate(righe, start=2):
    c = ws.cell(row=i, column=2, value=t)
    if f: c.font = f
ws.column_dimensions["A"].width = 2
ws.column_dimensions["B"].width = 110

# ---------------------------------------------------------------- MAPPA
m = wb.create_sheet("Mappa")
cols = [
 ("Marca", 18), ("Prodotto", 32), ("Canale", 16), ("Posizionamento", 20), ("Paese", 8),
 ("URL", 30), ("Data consult.", 12),
 ("Prezzo €", 10), ("Prezzo abbon. €", 13), ("Formato mL", 11),
 ("€/mL", 9), ("Dose dichiarata", 30), ("mL/giorno", 10), ("Giorni/confez.", 12), ("€/mese", 10),
 ("% dichiarate", 13), ("Quali percentuali", 30), ("Claim principale", 34), ("Liv. claim", 9),
 ("Prove citate", 24), ("Garanzia", 20), ("Abbonamento", 14), ("Recensioni", 11),
 ("Stato", 14), ("Note e fonte della stima", 36),
]
for j,(t,w) in enumerate(cols, start=1):
    c = m.cell(row=1, column=j, value=t)
    c.font = head; c.fill = fill_head; c.border = box
    c.alignment = Alignment(vertical="center", wrap_text=True)
    m.column_dimensions[get_column_letter(j)].width = w
m.row_dimensions[1].height = 30
m.freeze_panes = "C2"

# marca, prodotto, canale, posizionamento, paese, prezzo, abbon, mL, dose testo, mL/g, %dich, quali, garanzia, abbon, note
dati = [
 ("The Ordinary","Multi-Peptide Serum for Hair Density","DTC e profumeria","densità e scalp","IT",26.50,None,60,"",None,"","","","","prezzo dalla ricerca preliminare, da riaprire"),
 ("The INKEY List","Caffeine Stimulating Scalp Treatment","DTC e profumeria","scalp e densità","EU",15.50,None,150,"",None,"alcune","1% caffeina · 1% Redensyl · 1% betaina","","","percentuali confermate da ricerca; prezzo da riaprire"),
 ("Vichy","Dercos Aminexil Clinical 5 uomo","farmacia","anticaduta","IT",51.20,None,126,"3 fiale a settimana per 6 settimane, oppure 1 al giorno",None,"nessuna","","","","21 fiale da 6 mL; posologia doppia, va scelta quale confrontare"),
 ("Ducray","Neoptide donna","farmacia","anticaduta","IT",44.94,None,90,"circa 12 spruzzi al giorno per 3 mesi",1.0,"","","","","3 flaconi da 30 mL; mL/giorno dedotto dalla durata dichiarata"),
 ("Kérastase","Genesis Sérum Anti-Chute Fortifiant","salone e profumeria","anticaduta","IT",56.90,None,90,"4 pipette una volta al giorno",2.4,"nessuna","","","","durata dichiarata 5-6 settimane: mL/giorno dedotto da lì"),
 ("Nioxin","Night Density Rescue","salone","densità","IT",60.69,None,70,"2-4 pipette ogni sera",3.0,"","","","","mL/giorno al centro dell'intervallo, da misurare"),
 ("OUAI","Scalp Serum","profumeria","scalp care","IT",61.00,None,60,"2 contagocce pieni, circa 1,5 mL",1.5,"","","","","la marca dichiara circa 40 giorni di durata"),
 ("Living Proof","Scalp Care Density Serum","profumeria","densità e scalp","IT",66.00,None,50,"2-3 contagocce al giorno",1.7,"","","","","la marca dichiara circa 30 giorni di durata"),
 ("Act+Acre","Stem Cell Scalp Serum","DTC","scalp e densità","EU",89.00,None,65,"",None,"","","","","formato e prezzo da riaprire"),
 ("Augustinus Bader","The Scalp Treatment","profumeria","scalp care","IT",89.00,None,30,"",None,"","","","","il più caro al mL della categoria"),
 ("Aveda","Scalp Solutions","salone","scalp care","IT",59.00,None,50,"",None,"","","","",""),
 ("Scandinavian Biolabs","Bio-Pilixin Activation Serum uomo","DTC","densità","EU",55.00,39.00,100,"almeno 2 pipette al giorno",2.0,"","","150 giorni, condizionata","sì, con sconto","il riferimento per la garanzia; verificare le condizioni esatte"),
 ("Plantur","DMG Clinical Serum","farmacia e GDO","anticaduta","DE",19.99,None,125,"",None,"","","","","ancoraggio basso del canale farmacia tedesco"),
 ("Bioscalin (Giuliani)","TricoAge siero concentrato","farmacia","anticaduta e antietà","IT",48.56,None,40,"6 pipette ogni 3 giorni, ciclo di 3 mesi",0.44,"nessuna","","","","mL/giorno dedotto dal ciclo dichiarato di 3 mesi: da verificare"),
 ("Grow Gorgeous","Density Serum Intense","DTC","densità","EU",50.00,None,60,"",None,"","","","",""),
 ("Foreo","Dual-Peptide Scalp Serum","profumeria","scalp e densità","IT",52.90,None,60,"",None,"","","","",""),
 ("René Furterer","Triphasic Progressive","farmacia","anticaduta","IT",None,None,None,"",None,"","","","","da rilevare"),
 ("Crescina (Labo)","Transdermic","farmacia","anticaduta","IT",None,None,None,"",None,"","","","","da rilevare"),
 ("Eucerin","DermoCapillaire","farmacia","scalp care","IT",None,None,None,"",None,"","","","","da rilevare"),
 ("Nutrafol","Scalp Serum","DTC","densità","US",None,None,50,"",None,"","","","","mercato USA: utile per il confronto, non per il prezzo italiano"),
 ("Philip Kingsley","Density Serum","profumeria","densità","EU",None,None,None,"",None,"","","","","da rilevare"),
 ("Alpecin","Caffeine Liquid","GDO","anticaduta","DE",None,None,200,"",None,"","","","","ancoraggio bassissimo, canale diverso dal nostro"),
 ("KRINÉ","Siero leave-on, flacone singolo","DTC","densità e scalp","IT",59.00,49.00,60,"4 erogazioni da 0,5 mL, una volta la sera",2.0,"tutte","tutte le percentuali degli attivi","150 giorni sul percorso","sì","noi, formato singolo"),
 ("KRINÉ","Siero leave-on, percorso da 5","DTC","densità e scalp","IT",239.00,None,300,"4 erogazioni da 0,5 mL, una volta la sera",2.0,"tutte","tutte le percentuali degli attivi","150 giorni, condizionata","—","noi, percorso. Attenzione: 5 flaconi al netto del residuo danno 142,5 giorni, non 150"),
]

for i,d in enumerate(dati, start=2):
    marca,prod,canale,pos,paese,prezzo,abbon,ml,dose,mlg,pdich,quali,gar,sub,nota = d
    vals = {1:marca,2:prod,3:canale,4:pos,5:paese,8:prezzo,9:abbon,10:ml,12:dose,13:mlg,
            16:pdich,17:quali,21:gar,22:sub,25:nota}
    for j in range(1,26):
        c = m.cell(row=i, column=j)
        c.border = box; c.font = ink
        c.alignment = Alignment(vertical="top", wrap_text=(j in (2,12,17,18,20,21,25)))
        if j in vals and vals[j] not in (None,""):
            c.value = vals[j]
            if j in (8,9,10,13): c.font = blu
        elif j in (11,14,15):
            pass
        else:
            c.fill = fill_todo
    m.cell(row=i, column=11, value=f"=IFERROR(H{i}/J{i},\"\")").fill = fill_calc
    m.cell(row=i, column=14, value=f"=IFERROR(J{i}/M{i},\"\")").fill = fill_calc
    m.cell(row=i, column=15, value=f"=IFERROR(H{i}/N{i}*30,\"\")").fill = fill_calc
    for j in (11,14,15):
        m.cell(row=i, column=j).border = box
        m.cell(row=i, column=j).font = ink
    m.cell(row=i, column=24, value="da verificare").font = ink
    if marca == "KRINÉ":
        for j in range(1,26):
            m.cell(row=i, column=j).fill = fill_noi
        m.cell(row=i, column=24, value="nostro dato")

ult = len(dati)+1
m.cell(row=ult+2, column=1, value="Celle gialle: da compilare · Celle grigie: calcolate, non scrivere · Testo blu: valore inserito a mano").font = note
m.cell(row=ult+3, column=1, value="La colonna N non sottrae il residuo del contenitore. Per il nostro airless il residuo stimato è il 5%: a parità di dose la nostra durata reale è leggermente più bassa di quella calcolata qui.").font = note

for col,f in (("H",'#,##0.00 "€"'),("I",'#,##0.00 "€"'),("K",'#,##0.00 "€"'),("O",'#,##0.00 "€"'),
              ("J",'#,##0'),("M",'#,##0.0'),("N",'#,##0')):
    for r in range(2, ult+1):
        m[f"{col}{r}"].number_format = f

dv = DataValidation(type="list", formula1='"nessuna,alcune,tutte,da verificare"', allow_blank=True)
m.add_data_validation(dv); dv.add(f"P2:P{ult}")
dv2 = DataValidation(type="list", formula1='"da verificare,verificato,nostro dato"', allow_blank=True)
m.add_data_validation(dv2); dv2.add(f"X2:X{ult}")

# ---------------------------------------------------------------- SINTESI
s = wb.create_sheet("Sintesi")
s.sheet_view.showGridLines = False
s.column_dimensions["B"].width = 58
s.column_dimensions["C"].width = 16
s.column_dimensions["D"].width = 60
s.cell(row=2, column=2, value="Che cosa dice la mappa").font = h1
s.cell(row=3, column=2, value="Si aggiorna da sola man mano che la tabella viene compilata.").font = note

voci = [
 ("Prodotti in mappa", f"=COUNTA(Mappa!A2:A{ult})", "righe totali"),
 ("Righe verificate da una persona", f'=COUNTIF(Mappa!X2:X{ult},"verificato")', "finché è zero, la mappa non è una fonte"),
 ("Righe con il costo mensile calcolabile", f"=COUNT(Mappa!O2:O{ult})", "servono prezzo, formato e dose"),
 ("", "", ""),
 ("Costo mensile più basso", f"=IFERROR(MIN(Mappa!O2:O{ult}),\"\")", "l'ancoraggio che il cliente confronta"),
 ("Costo mensile più alto", f"=IFERROR(MAX(Mappa!O2:O{ult}),\"\")", ""),
 ("Costo mensile medio", f"=IFERROR(AVERAGE(Mappa!O2:O{ult}),\"\")", ""),
 ("Nostro costo mensile, percorso da 5", f"=IFERROR(O{ult},\"\")", "sotto o sopra la media?"),
 ("", "", ""),
 ("Quanti dichiarano tutte le percentuali", f'=COUNTIF(Mappa!P2:P{ult},"tutte")', "se resta 1, la trasparenza integrale è terreno libero"),
 ("Quanti ne dichiarano alcune", f'=COUNTIF(Mappa!P2:P{ult},"alcune")', "dichiarare qualche percentuale non è una novità"),
 ("Quanti non ne dichiarano nessuna", f'=COUNTIF(Mappa!P2:P{ult},"nessuna")', ""),
 ("", "", ""),
 ("Quanti offrono una garanzia di rimborso", f'=COUNTIF(Mappa!U2:U{ult},"?*")', "se sono pochi, la garanzia è un vantaggio; se sono molti, è un requisito"),
 ("Quanti hanno un abbonamento", f'=COUNTIF(Mappa!V2:V{ult},"?*")', ""),
]
r = 5
for lab, fml, com in voci:
    if lab:
        s.cell(row=r, column=2, value=lab).font = ink
        c = s.cell(row=r, column=3, value=fml); c.font = bold
        if "€" in lab or "Costo" in lab: c.number_format = '#,##0.00 "€"'
        s.cell(row=r, column=4, value=com).font = note
    r += 1

s.cell(row=r+1, column=2, value="Le tre domande a cui questa tabella deve rispondere").font = h2
for k, q in enumerate([
  "1. Il nostro costo mensile è dentro o fuori mercato? Finora lo abbiamo dedotto, mai misurato.",
  "2. La trasparenza sulle percentuali è un terreno libero o è già occupato?",
  "3. La garanzia di rimborso è un vantaggio competitivo o è diventata la norma della categoria?",
], start=1):
    s.cell(row=r+1+k, column=2, value=q).font = ink

wb.save("mappa-competitiva.xlsx")
print("scritto mappa-competitiva.xlsx")
