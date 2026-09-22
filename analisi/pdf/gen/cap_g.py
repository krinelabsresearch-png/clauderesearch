from base import *

FONTI = [
 ("Criteri per i claim cosmetici", "Regolamento (UE) 655/2013, allegato", "https://eur-lex.europa.eu/eli/reg/2013/655/oj", "norma"),
 ("Confine fra cosmetico e medicinale", "Commissione europea, manuale del gruppo di lavoro sui prodotti di confine, versione corrente", "da allegare in copia", "norma"),
 ("Sanzione AGCM a L'Oréal Italia, Dercos", "Quotidiano Sanità", "https://www.quotidianosanita.it/cronache/articolo.php?articolo_id=8448", "ricerca"),
 ("Posologia e tempi del minoxidil", "Foglio illustrativo Minoximen soluzione cutanea", "https://www.viafarmaciaonline.it/media/upload/file/MINOXIMEN%C2%AE%20Soluzione%20Cutanea.pdf", "ricerca"),
 ("Prezzo del minoxidil 5%", "Redcare; Farmacia Fatigato", "https://www.redcare.it/medicinali/IT042311011/minoxidil-biorga-5-soluzione-cutanea.htm", "ricerca"),
 ("Abbandono del minoxidil", "Senthilnathan A. et al., J Drugs Dermatol 2023;22(3):252-255", "https://doi.org/10.36849/JDD.6639", "letta (PubMed)"),
 ("Crescita dei sieri per capelli in Europa", "Circana, ripreso da Cosmetics Business", "https://cosmeticsbusiness.com/cosmetics-business-reveals-the-top-5-hair-care-1", "ricerca"),
 ("Crescita della cura del cuoio capelluto, Stati Uniti", "Circana, ripreso da Beauty Packaging", "https://www.beautypackaging.com/breaking-news/circana-reports-2025-u-s-prestige-and-mass-beauty-retail-gains/", "ricerca"),
 ("Mercato italiano dei prodotti per capelli", "Pambianco Beauty, dicembre 2025", "https://beauty.pambianconews.com/2025/12/haircare-evolution/75890", "ricerca"),
 ("Kérastase Genesis: claim, dose, prezzo", "Pagina ufficiale Kérastase Italia", "https://www.kerastase.it/genesis/trattamento-serum-anti-chute-fortifiant/3474636858002.html", "ricerca"),
 ("Vichy Dercos Aminexil: prezzo e regime", "idealo.it; notino.it", "https://www.idealo.it/confronta-prezzi/200464034/vichy-dercos-aminexil-clinical-5-trattamento-uomo-anticaduta.html", "ricerca"),
 ("OUAI Scalp Serum: dose e durata", "Pagina ufficiale OUAI", "https://theouai.com/products/scalp-serum", "ricerca"),
 ("Living Proof: claim e studio", "Pagina ufficiale Living Proof", "https://www.livingproof.com/products/scalp-care-density-serum", "ricerca"),
 ("Garanzia di Scandinavian Biolabs", "Condizioni pubblicate", "https://scandinavianbiolabs.com/pages/money-back-guarantee", "ricerca"),
 ("Commissioni di incasso", "Listino Stripe Italia", "https://stripe.com/it/pricing", "ricerca"),
 ("Compensazione del credito IVA", "Fiscomania", "https://fiscomania.com/compensazione-del-credito-iva/", "ricerca"),
 ("IVA sulla pubblicità online", "Fiscomania", "https://fiscomania.com/facebook-ads-fattura-iva-account/", "ricerca"),
 ("Costi di costituzione della società", "Notaionline", "https://notaionline.it/guida/costo-costituzione-srl-notaio/", "ricerca"),
 ("Acquisizione di rhode", "e.l.f. Beauty, comunicato del 28 maggio 2025", "https://investor.elfbeauty.com/stock-and-financial/press-releases/landing-news/2025/05-28-2025-210536607", "ricerca"),
 ("Popolazione per età e sesso", "Istat, demo.istat.it, popolazione al 1° gennaio 2026", "https://demo.istat.it/app/?i=POS", "da estrarre"),
 ("Composizione, dosi, studi, brevetti", "Dossier tecnico di formulazione V9.3", "documento interno", "dato"),
]

def cap16():
    rows = "".join(f'<tr><td>{a}</td><td>{b}<div class="src">{c}</div></td><td>{d}</td></tr>' for a, b, c, d in FONTI)
    return f"""
<section>
  <h2><span class="num">16</span>Metodo, fonti e limiti</h2>
  <h3>Come è stato costruito</h3>
  <p>Il piano incrocia il dossier tecnico, letto per intero, con fonti pubbliche e con un modello di cassa costruito per questo scopo. Il modello esiste in due versioni indipendenti: il foglio di calcolo allegato, tutto a formule, e un programma scritto separatamente. Le due versioni sono state confrontate mese per mese in tutti gli scenari, su cassa, incassi, rimborsi, IVA, scorte, clienti ed esposizione della garanzia: coincidono al centesimo. I numeri del documento sono generati direttamente dal modello, non ricopiati.</p>
  <h3>Fonti</h3>
  <table class="small long">
    <thead><tr><th style="width:44mm">Tema</th><th>Fonte e indirizzo</th><th style="width:22mm">Stato</th></tr></thead>
    <tbody>{rows}</tbody>
    <caption>Rilevazione del 22 settembre 2026. «Ricerca»: contenuto visto tramite motore di ricerca; la pagina va aperta, salvata e archiviata con data prima della consegna a terzi. «Letta»: metadati e sintesi dell'articolo consultati direttamente.</caption>
  </table>
  <h3>Limiti dichiarati</h3>
  <ul>
    <li><b>La mappa competitiva non è verificata.</b> Due confronti di costo su dieci reggono; gli altri dipendono da dosi da ricostruire.</li>
    <li><b>Le percentuali del bacino non sono misurate</b>, e la popolazione va riallineata a un'unica estrazione Istat.</li>
    <li><b>Le ipotesi di comportamento</b> (mix di offerte, completamento, rimborsi, rinnovi, riacquisti) sono le più fragili e quelle che muovono di più il risultato. Sono tutte nell'appendice B e nel foglio Parametri del modello.</li>
    <li><b>Nessuno studio esiste sul prodotto finito.</b> Ogni affermazione su che cosa il prodotto farà è un'ipotesi.</li>
    <li><b>Il documento non contiene pareri legali.</b> Brevetti, claim, Academy, garanzia e recesso sono valutati come rischi commerciali; ciascuno richiede la firma di un professionista.</li>
    <li><b>Imposte sul reddito e IRAP non sono modellate.</b> La compensazione orizzontale dell'IVA non è usata.</li>
  </ul>
</section>"""

def appA():
    rows = ""
    for voce, m, leg, imp, q, t in [(v, m, l, i, q, t) for (m, v, i, q, t) in [(x[0], x[1], x[2], x[3], x[4]) for x in costi_progetto(BASE)] for l in [""]]:
        rows += f'<tr><td>{voce}</td><td class="c">{t}</td><td class="c">{m}</td><td class="n">{eur(imp)}</td><td class="n">{pct(q, 0)}</td></tr>'
    tot = sum(x[2] for x in costi_progetto(BASE))
    return f"""
<section>
  <h2><span class="num">A</span>Costi voce per voce</h2>
  <p class="lead">Le voci del modello, nello scenario base, nella forma in cui servono per chiedere preventivi. Importi centrali al netto dell'IVA; la colonna IVA indica la quota soggetta a IVA italiana.</p>
  <table class="small tight long">
    <thead><tr><th>Voce</th><th class="c" style="width:12mm">Tappa</th><th class="c" style="width:12mm">Mese</th><th class="n" style="width:18mm">Euro</th><th class="n" style="width:14mm">IVA</th></tr></thead>
    <tbody>{rows}<tr class="hi"><td>Totale costi di progetto</td><td></td><td></td><td class="n">{eur(tot)}</td><td></td></tr></tbody>
    <caption>Il primo lotto di produzione (3.000 flaconi a 8,50 euro, 25.500 euro più IVA) è nel foglio delle scorte del modello, non qui. Intervalli di stima delle voci principali: laboratorio 17.500-50.000; tollerabilità 4.300-11.000; protocollo per i claim 15.000-35.000; lotto pilota 3.500-12.000. <span class="tag stima">stima</span></caption>
  </table>
</section>"""

def appB():
    s = BASE; a = scenario("Avverso senza arresto")
    righe = [
        ("Mese del lancio", "16", "16 (20 nei casi con ritardo)"),
        ("Costo industriale per flacone", "8,50 €", "11,90 €"),
        ("Mix: percorso 6 · percorso 3 · abbonamento · singolo", "25% · 10% · 45% · 20%", "uguale"),
        ("Completamento del percorso da sei", "55%", "55%"),
        ("Chi completa e chiede il rimborso", "22% (12,1% dei percorsi)", "36% (19,8%)"),
        ("Riacquisto dopo il percorso, di chi completa senza rimborso", "45%, poi 60%", "35%, poi 60%"),
        ("Riacquisto del percorso da tre", "35%, poi 55%", "25%, poi 55%"),
        ("Rinnovo dell'abbonamento dopo gli invii 1-6", "65 · 70 · 72 · 78 · 82 · 85%", "57 · 62 · 64 · 70 · 74 · 77%"),
        ("Nuovo acquisto del flacone singolo", "37,5% (1,6 ordini)", "30%"),
        ("Sconto medio sul primo ordine", "5%", "10%"),
        ("Pubblicità: tranche 1 · 2 · 3", "10.000 · 20.000 · 30.000 €", "uguale (terza a zero con arresto)"),
        ("CAC pubblicitario: tranche 1-2 · tranche 3 e dopo", "50 € · 55 €", "70 € · 77 €"),
        ("Pubblicità dopo le tranche", "5.000 € al mese", "5.000 € (zero con arresto)"),
        ("Creatività e gestione campagne", "600 € al mese", "uguale"),
        ("Clienti da canali non pagati", "8 al mese", "4 al mese"),
        ("Residuo nel flacone", "5%", "uguale"),
        ("Lotto · acconto · tempo di fornitura · scorta di sicurezza", "3.000 · 40% · 3 mesi · 1 mese", "uguale"),
        ("Commissione di incasso · assistenza e resi", "1,9% + 0,25 € · 3%", "uguale"),
        ("Rimborsi di garanzia: quando", "metà al 5° mese, metà al 6°", "uguale"),
    ]
    body = "".join(f"<tr><td>{x}</td><td>{y}</td><td>{z}</td></tr>" for x, y, z in righe)
    return f"""
<section>
  <h2><span class="num">B</span>Le ipotesi del modello</h2>
  <p class="lead">Tutti i parametri in un posto. Sono modificabili nel foglio Parametri di modello-cassa.xlsx, una colonna per scenario.</p>
  <table class="small">
    <thead><tr><th>Parametro</th><th style="width:48mm">Base</th><th style="width:48mm">Avverso</th></tr></thead>
    <tbody>{body}</tbody>
    <caption><span class="tag">ipotesi</span> Tutti i valori di comportamento dei clienti sono ipotesi da misurare nella tappa 4.</caption>
  </table>
</section>"""
