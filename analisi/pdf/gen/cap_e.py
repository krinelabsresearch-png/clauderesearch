from base import *
HI = ' class="hi"'

def grafico_payback():
    cm = N["curva_media"][:13]; ca = N["curva_abb"][:13]; cv = N["curva_media_avv"][:13]
    xs = list(range(1, 14))
    svg = svg_linee([("Cliente medio, base", COL[0], cm), ("Abbonato, base", COL[1], ca), ("Cliente medio, avverso", COL[2], cv)],
                    xs, 120, 20, lambda y: f"{int(y)} €", [1, 3, 6, 9, 12, 13], h=220, dash=[None, None, "6 4"],
                    hlines=[(50, "CAC 50 €"), (60, "CAC 60 €"), (80, "CAC 80 €")], x_label="mese dall'acquisizione")
    leg = legenda([("Cliente medio, base", COL[0], False), ("Abbonato, base", COL[1], False), ("Cliente medio, avverso", COL[2], True)])
    return f'<div class="fig"><div class="ttl">Contribuzione cumulata per nuovo cliente, al netto dei rimborsi</div>{leg}{svg}<div class="cap">Il cliente medio include il percorso da sei, pagato in anticipo: per questo parte da 60 euro. La flessione fra il quinto e il sesto mese sono i rimborsi della garanzia. Il cliente in abbonamento da solo recupera un CAC di 60 euro al quinto mese e uno di 80 al decimo.</div></div>'

def grafico_cassa():
    xs = list(range(1, 31))
    nomi = [("Base", "Base"), ("Lancio ritardato", "Ritardo"), ("Avverso con arresto", "Avverso, con arresto"),
            ("Avverso senza arresto", "Avverso, senza arresto"), ("Tutto insieme", "Tutto insieme")]
    serie = [(lab, COL[i], N["scenari"][n]["cassa"]) for i, (n, lab) in enumerate(nomi)]
    svg = svg_linee(serie, xs, 250000, 50000, lambda y: f"{int(y/1000)} k", [1, 6, 12, 16, 20, 24, 30], h=250,
                    dash=[None, None, None, "6 4", "2 3"], vlines=[(16, "lancio base"), (20, "lancio in ritardo")], label_min_gap=11)
    leg = legenda([(lab, COL[i], i >= 3) for i, (_, lab) in enumerate(nomi)])
    return f'<div class="fig"><div class="ttl">Cassa a fine mese, cinque scenari, euro</div>{leg}{svg}<div class="cap">Dal modello di cassa allegato. Fino al lancio gli scenari con lo stesso calendario coincidono e le linee si sovrappongono. Nessuna seconda raccolta è ipotizzata. I valori sono nella tabella sotto il grafico.</div></div>'

def cap10():
    S = N["scenari"]; fi = N["fonti_impieghi"]
    ordine = ["Base", "Lancio ritardato", "Avverso senza arresto", "Avverso con arresto", "Tutto insieme"]
    corti = ["Base", "Ritardo", "Avverso", "Avverso con arresto", "Tutto insieme"]
    def r(lbl, key, f=eur, hi=False):
        return f'<tr{HI if hi else ""}><td>{lbl}</td>' + "".join(f'<td class="n">{f(S[n][key])}</td>' for n in ordine) + "</tr>"
    tab = "".join([r("Cassa minima, €", "minimo", hi=True), r("Mese della cassa minima", "mese_min", lambda x: str(x)),
                   r("Capitale assorbito fino al minimo, €", "assorbito"), r("Cassa al mese 24, €", "c24"), r("Cassa al mese 30, €", "c30"),
                   r("Nuovi clienti fino al mese 30", "clienti"), r("di cui da pubblicità", "pagati"), r("Pubblicità, €", "pubbl"),
                   r("Ricavi netti, €", "ricavi"), r("Rimborsi di garanzia pagati, €", "rimborsi"), r("Credito IVA massimo, €", "cred"),
                   r("Lotti da 3.000 flaconi ordinati", "lotti", lambda x: str(x))])
    imp = [("Sviluppo, prove, regolatorio, marchio, Academy, sito", fi["progetto"]), ("IVA pagata ai fornitori italiani sul progetto", fi["progetto_iva"]),
           ("Produzione: primo lotto e riordini", fi["produzione"]), ("IVA sulla produzione", fi["produzione_iva"]),
           ("Pubblicità", fi["pubbl"]), ("Creatività e gestione campagne", fi["creativi"]),
           ("Logistica, IVA inclusa", fi["logistica"]), ("Commissioni di incasso", fi["commissioni"]), ("Assistenza e resi ordinari", fi["assistenza"]),
           ("Rimborsi di garanzia", fi["rimborsi"]), ("Costi fissi, IVA inclusa", fi["fissi"] + fi["fissi_iva"])]
    tot_imp = sum(x for _, x in imp)
    imp_html = "".join(f'<tr><td>{a}</td><td class="n">{eur(b)}</td></tr>' for a, b in imp)
    g = N["griglia"]
    grid = "".join(f'<tr><td class="n">{c} €</td>' + "".join(f'<td class="n">{eur(g[f"{c}|{q}"][1])}</td>' for q in ("0.15", "0.25", "0.35")) + "</tr>" for c in (40, 50, 60, 70, 85, 100))
    return f"""
<section>
  <h2><span class="num">10</span>Coorti e cassa a trenta mesi</h2>
  <p class="lead">Il modello allegato segue la cassa mese per mese dalla chiusura della raccolta al mese 30: sviluppo, scorte, pubblicità, incassi, IVA, rimborsi. Cassa minima e fabbisogno ne sono il risultato, non un'ipotesi di partenza.</p>
  <h3>Quando rientra la spesa di acquisizione</h3>
  {grafico_payback()}
  <table class="tight">
    <thead><tr><th>CAC complessivo</th><th class="n">50 €</th><th class="n">55 €</th><th class="n">60 €</th><th class="n">70 €</th><th class="n">80 €</th></tr></thead>
    <tbody>
      <tr><td>Mese in cui la coorte media lo recupera</td>{"".join(f'<td class="n">{N["payback"][str(c)][0]}°</td>' for c in (50, 55, 60, 70, 80))}</tr>
      <tr><td>Mese in cui lo recupera un abbonato</td>{"".join(f'<td class="n">{N["payback"][str(c)][1]}°</td>' for c in (50, 55, 60, 70, 80))}</tr>
    </tbody>
    <caption>Scenario base, con la curva di rinnovo e non con una media. Una durata media di 4,1 invii non basta a stabilire i tempi di cassa: chi abbandona presto pesa sulla coorte.</caption>
  </table>
  <h3>Cinque scenari</h3>
  <p>Oltre allo scenario base il modello ne calcola quattro. <b>Ritardo</b>: il lancio slitta di quattro mesi per un ciclo di laboratorio in più, che costa 12.000 euro. <b>Avverso</b>: costo industriale alto (11,90 euro), CAC più alto del 40%, rimborsi al 19,8%, rinnovi più bassi di otto punti, meno riacquisti, sconti più forti, metà dei clienti da canali non pagati. <b>Avverso con arresto</b>: lo stesso, ma con le regole del capitolo 11 applicate, per cui la terza tranche di pubblicità non parte. <b>Tutto insieme</b>: ritardo e avverso combinati, senza regole di arresto.</p>
  {grafico_cassa()}
  <table class="small tight">
    <thead><tr><th></th>{"".join(f'<th class="n">{c}</th>' for c in corti)}</tr></thead>
    <tbody>{tab}</tbody>
  </table>
  <p>La somma richiesta basta in tutti e cinque gli scenari. Il minimo di cassa dello scenario base cade al mese {S["Base"]["mese_min"]}, a ridosso del lancio, quando sviluppo e primo lotto sono pagati e le vendite non sono iniziate. Le regole di arresto valgono circa {eur(S["Avverso con arresto"]["c30"] - S["Avverso senza arresto"]["c30"])} euro di cassa al mese 30 nello scenario avverso, e la differenza cresce dopo. Nel caso peggiore la cassa risale dopo il mese 27 solo perché si vende il magazzino già pagato: il risultato operativo resta negativo di 1.400-3.000 euro al mese, ed è la situazione che le regole di arresto esistono per evitare.</p>
  <h3>Fonti e impieghi fino al mese 24, scenario base</h3>
  <table class="tight">
    <thead><tr><th>Voce</th><th class="n">Euro</th></tr></thead>
    <tbody>
      <tr class="hi"><td>Capitale versato</td><td class="n">{eur(fi["capitale"])}</td></tr>
      <tr class="hi"><td>Incassi dalle vendite, IVA inclusa</td><td class="n">{eur(fi["incassi"])}</td></tr>
      {imp_html}
      <tr class="hi"><td>Totale impieghi</td><td class="n">{eur(tot_imp)}</td></tr>
      <tr class="hi"><td>Cassa al mese 24</td><td class="n">{eur(fi["cassa_m24"])}</td></tr>
    </tbody>
    <caption>Al mese 24 restano inoltre {eur(fi["credito_m24"])} euro di credito IVA da recuperare. I fondatori non ricevono compensi dalla società: hanno altre entrate, e il loro tempo non compare come costo. Imposte sul reddito e IRAP non sono modellate: nel periodo la società resta in perdita cumulata.</caption>
  </table>
  <h3>L'IVA</h3>
  <p>Prima del lancio la società paga IVA ai fornitori italiani (laboratorio, studi, produzione, professionisti) e non ne incassa. Il credito arriva a {eur(S["Base"]["cred"])} euro al mese 15 e si recupera compensandolo con l'IVA sulle vendite; nello scenario base si esaurisce al mese 28 e il primo versamento cade al mese 29. Pubblicità, piattaforme e abbonamenti acquistati da società di altri paesi europei sono in inversione contabile e non assorbono cassa. La compensazione con altri tributi è ammessa fino a 5.000 euro l'anno senza visto di conformità, e il modello non la usa: è un'ipotesi prudente. La liquidazione è mensile, anch'essa per prudenza.</p>
  <h3>Le scorte</h3>
  <p>I lotti sono da 3.000 flaconi, con acconto del 40% all'ordine e saldo alla consegna, tre mesi dopo. Il riordino non ha una data fissa: si ordina quando le scorte più il lotto in arrivo scendono sotto il consumo previsto nel tempo di fornitura più un mese di sicurezza, calcolato sulla media degli ultimi due mesi. Il consumo comprende ordini, campioni (150 al lancio, poi 20 al mese) e sostituzioni (1% dei flaconi spediti); ogni lotto perde l'1% di scarto e 30 flaconi per analisi e campioni di riserva. Nello scenario base i lotti partono ai mesi {", ".join(str(m) for m in S["Base"]["mesi_lotti"])}. Fornitori e laboratori dovranno confermare tempi, minimi d'ordine, acconti e capacità di riassortimento: sono parte dell'economia del prodotto.</p>
  <h3>La quota del percorso da sei</h3>
  <p>Dopo il costo di acquisizione è l'ipotesi che muove di più la cassa, perché il percorso incassa 171 giorni in anticipo.</p>
  <table class="tight">
    <thead><tr><th>CAC pubblicitario</th><th class="n">15% sceglie il percorso</th><th class="n">25% (base)</th><th class="n">35%</th></tr></thead>
    <tbody>{grid}</tbody>
    <caption>Cassa al mese 30, euro. Tutte le altre ipotesi dello scenario base invariate; le altre offerte si ridistribuiscono in proporzione.</caption>
  </table>
  <h3>Il calendario delle coorti</h3>
  <p>I primi clienti arrivano al mese 16. Chi compra il percorso quel mese raggiunge il giorno 150 al mese 21 e può chiedere il rimborso fino al mese 22; il primo riacquisto dopo 171 giorni cade anch'esso al mese 22. Le coorti delle prime due tranche di pubblicità, mesi 16-20, avranno superato la finestra della garanzia al mese 27. Una seconda raccolta fra i mesi 24 e 30 potrà quindi mostrare tre-cinque coorti mature, non di più. Il modello non la ipotizza: nello scenario base la società arriva al mese 30 con {eur(S["Base"]["c30"])} euro in cassa e un risultato operativo positivo. Nello scenario base il capitale successivo serve alla crescita; la sopravvivenza non ne dipende.</p>
</section>"""
