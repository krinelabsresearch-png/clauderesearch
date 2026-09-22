from base import *

def cap04():
    return """
<section>
  <h2><span class="num">04</span>Il prodotto e la formula guida</h2>
  <p class="lead">Un siero da applicare la sera sul cuoio capelluto e non risciacquare, pensato per un uso continuativo di sei-dodici mesi. Lavora su due fronti: il comfort della cute e l'aspetto del capello.</p>
  <h3>Uso e dose</h3>
  <p>La dose si definisce per superficie: un'erogazione da mezzo millilitro ogni trenta centimetri quadrati circa. Il regime di riferimento è di quattro erogazioni la sera, due millilitri al giorno, la mediana dei regimi usati negli studi sugli attivi. Una sola applicazione serale è più comoda di due, ma non è dimostrato che dia lo stesso effetto di un millilitro mattina e sera: lo teniamo distinto. Il massimo d'uso giornaliero verrà fissato in millilitri con il valutatore della sicurezza; fino ad allora nel materiale commerciale compare solo il regime di riferimento.</p>
  <h3>Le tre architetture</h3>
  <p>Il dossier tecnico descrive tre configurazioni complete. Si sviluppa la <b>C</b>: trentacinque ingredienti, senza diaminopirimidina ossido. La <b>A</b>, che contiene anche quella molecola, resta un'opzione da riprendere solo dopo un parere legale favorevole sul brevetto che la riguarda. La <b>B</b> entra in gioco se il piroctone olamina dà problemi di stabilità o di fornitura. Avere alternative già calcolate significa che un ostacolo di fornitura o di brevetto costa tempo, non il progetto.</p>
  <h3>Attivo per attivo: dose, studio, differenza</h3>
  <p>La regola del dossier è che un attivo entra alla dose dello studio che lo giustifica, oppure la differenza viene dichiarata. Solo due attivi sono alla concentrazione studiata. Per gli altri la dose è diversa o la ragione della presenza è un'altra, e la tabella lo dice.</p>
  <table class="small">
    <thead><tr><th style="width:24mm">Attivo</th><th class="n" style="width:14mm">Nostra dose</th><th>Studi di riferimento</th><th style="width:26mm">Dose e regime studiati</th><th style="width:52mm">Differenza da dichiarare</th></tr></thead>
    <tbody>
      <tr><td><b>Adenosina</b></td><td class="n">0,75%</td><td>Oura 2008, 30 donne, 12 mesi, contro placebo · Iwabuchi 2016, 38 uomini, 6 mesi, contro placebo · Kim 2024, 46 persone, 4 mesi, contro minoxidil, senza veicolo</td><td>0,75%, quasi sempre due volte al giorno; in Kim 2024 1 mL una volta al giorno, insieme a pantenolo 1% e niacinamide 2%</td><td>Stessa concentrazione, regime diverso. Una meta-analisi del 2025 su sette studi non trova una stima aggregata significativa: meno certezza, non prova di inefficacia</td></tr>
      <tr><td><b>Procianidine di mela</b></td><td class="n">0,70%</td><td>Takahashi 2005, 43 uomini, 6 mesi, contro placebo</td><td>0,7%</td><td>Stessa concentrazione, grado commerciale diverso da quello studiato. Il valore p dichiarato non torna con i dati riassuntivi (circa 0,04 invece di meno di 0,001)</td></tr>
      <tr><td><b>Niacinamide</b></td><td class="n">4%</td><td>Kim 2024, nel complesso con adenosina</td><td>2%</td><td>Il doppio. Scelta per barriera e tollerabilità, non per i capelli. Riduzione al 2% prevista se la tollerabilità lo richiede</td></tr>
      <tr><td><b>Ectoina</b></td><td class="n">0,5%</td><td>Evidenza soprattutto sulla pelle, non sul cuoio capelluto</td><td>—</td><td>Presente per barriera e protezione osmotica. Nessuna equivalenza con uno studio sul cuoio capelluto</td></tr>
      <tr><td><b>Pantenolo</b></td><td class="n">2%</td><td>Kim 2024</td><td>1%</td><td>Il doppio; da confrontare con 1-1,5% se appiccica</td></tr>
      <tr><td><b>Piroctone olamina</b></td><td class="n">0,30%</td><td>Studio 2021, 43 donne, prodotto da non risciacquare</td><td>0,45%</td><td>Dose inferiore: quel risultato non vale per lo 0,30%</td></tr>
      <tr><td><b>Melatonina</b></td><td class="n">0,0033%</td><td>Fischer 2004, 40 donne, contro placebo</td><td>0,1%</td><td>Trenta volte inferiore: il risultato non si trasferisce</td></tr>
    </tbody>
    <caption>Dalla matrice degli studi del dossier tecnico V9.3. Redensyl, Serenoa e Burgeon-Up sono ingredienti condizionati: restano solo se fornitura, brevetto e sicurezza lo consentono.</caption>
  </table>
  <p>La frase che useremo in comunicazione è quindi questa: <i>adenosina e procianidine sono alla concentrazione degli studi che le giustificano; per gli altri attivi indichiamo, uno per uno, perché ci sono e in che cosa la nostra dose differisce da quella studiata.</i> Nessuno studio sui singoli ingredienti dimostra che cosa farà la formula completa, né che gli effetti si sommino.</p>
  <h3>A che punto siamo</h3>
  <p>La formula è definita e pronta per un laboratorio esterno. Non esistono prove di stabilità, lotto di prova, studi sul prodotto finito. Nel calendario del piano il prodotto è in vendita al mese 16 dalla chiusura della raccolta, al mese 20 se un ciclo di laboratorio va ripetuto.</p>
</section>"""

def cap05():
    b = N["scenari"]["Base"]
    return f"""
<section>
  <h2><span class="num">05</span>Il mercato: bacino, flusso, imbuto</h2>
  <p class="lead">Tre numeri diversi che vanno tenuti separati: quante persone potrebbero comprare a questo prezzo (il bacino), quante ne possiamo acquisire ogni anno (il flusso), e con quale spesa (l'imbuto).</p>
  <h3>Il bacino, ricostruito dal basso</h3>
  <table class="tight">
    <thead><tr><th>Fascia</th><th class="n">Popolazione</th><th class="n">Prevalenza</th><th class="n">Con diradamento</th></tr></thead>
    <tbody>
      <tr><td>Uomini 25-34</td><td class="n">3,2 M</td><td class="n">25%</td><td class="n">800.000</td></tr>
      <tr><td>Uomini 35-44</td><td class="n">3,5 M</td><td class="n">40%</td><td class="n">1.400.000</td></tr>
      <tr><td>Uomini 45-54</td><td class="n">4,4 M</td><td class="n">50%</td><td class="n">2.200.000</td></tr>
      <tr><td>Donne 25-34</td><td class="n">3,1 M</td><td class="n">12%</td><td class="n">372.000</td></tr>
      <tr><td>Donne 35-44</td><td class="n">3,5 M</td><td class="n">20%</td><td class="n">700.000</td></tr>
      <tr><td>Donne 45-54</td><td class="n">4,5 M</td><td class="n">25%</td><td class="n">1.125.000</td></tr>
      <tr class="hi"><td>Totale 25-54</td><td class="n">22,2 M</td><td class="n">30%</td><td class="n">6,6 milioni</td></tr>
    </tbody>
    <caption>Popolazione arrotondata, da sostituire con un'unica estrazione Istat per età e sesso al 1° gennaio 2026 (demo.istat.it), conservata con data. Prevalenza dell'alopecia androgenetica da studi su popolazioni caucasiche. <span class="tag stima">stima</span></caption>
  </table>
  <table class="tight">
    <thead><tr><th>Passaggio</th><th class="n">Quota</th><th class="n">Persone</th><th style="width:66mm">Su che cosa si regge</th></tr></thead>
    <tbody>
      <tr><td>Con diradamento, 25-54 anni</td><td class="n">—</td><td class="n">6.600.000</td><td>Tabella sopra</td></tr>
      <tr><td>Lo percepisce e vuole intervenire</td><td class="n">20%</td><td class="n">1.320.000</td><td>Molti hanno il fenomeno senza considerarlo un problema</td></tr>
      <tr><td>Compra almeno un prodotto topico all'anno</td><td class="n">25%</td><td class="n">330.000</td><td>Gli altri usano integratori, shampoo, farmaci o niente</td></tr>
      <tr><td>Accetta 45 € al mese o più</td><td class="n">15%</td><td class="n">49.500</td><td>Il filtro più incerto</td></tr>
      <tr class="hi"><td>Raggiungibile dai nostri canali</td><td class="n">70%</td><td class="n">34.650</td><td>Compra online, non dipende dal consiglio del banco</td></tr>
    </tbody>
    <caption>Le quattro percentuali sono ipotesi e sono il punto più contestabile. Se la disponibilità a spendere fosse del 5% invece del 15%, il bacino scenderebbe a 11.550 persone. <span class="tag">ipotesi</span></caption>
  </table>
  <p>Le 34.650 persone sono un bacino, cioè chi oggi potrebbe plausibilmente comprare a questo prezzo. Non sono 34.650 acquirenti nuovi ogni anno: chi diventa cliente non si conta di nuovo l'anno dopo, e il bacino si rinnova solo con chi entra nella condizione, cambia prodotto o supera la soglia di spesa. Il ritmo di questo rinnovo non è misurato. Le quote del 2, 4 e 7% vanno lette come penetrazione del bacino in scenari diversi, non come vendite annue.</p>
  <h3>Il flusso: l'imbuto che spiega i primi clienti</h3>
  <p>Il numero di clienti che il piano può acquisire dipende dalla spesa, più che dal bacino. L'imbuto è semplice e ogni anello è un'ipotesi da misurare nella prima tranche di pubblicità.</p>
  <table class="tight">
    <thead><tr><th>Anello</th><th class="n">Ipotesi</th><th style="width:70mm">Esempio sulla prima tranche da 10.000 €</th></tr></thead>
    <tbody>
      <tr><td>Costo per visita qualificata</td><td class="n">0,70 €</td><td>14.286 visite alla pagina prodotto</td></tr>
      <tr><td>Visite che diventano un primo ordine</td><td class="n">1,4%</td><td>200 nuovi clienti</td></tr>
      <tr class="hi"><td>CAC pubblicitario</td><td class="n">50 €</td><td>10.000 € diviso 200</td></tr>
      <tr><td>Creatività e gestione delle campagne</td><td class="n">600 €/mese</td><td>CAC complessivo 56 €</td></tr>
      <tr><td>Clienti da canali non pagati</td><td class="n">8 al mese</td><td>Rete dei fondatori, Academy, passaparola. Non sono gratuiti: costano contenuti e tempo</td></tr>
    </tbody>
    <caption><span class="tag">ipotesi</span> Costo per visita e conversione sono i due numeri che la prima tranche misura per primi.</caption>
  </table>
  <p>Con questo imbuto, i 60.000 euro di pubblicità previsti nelle tre tranche portano {eur(N["tranche_clienti"]["t1"])} + {eur(N["tranche_clienti"]["t2"])} + {eur(N["tranche_clienti"]["t3"])} = 1.145 clienti a pagamento in nove mesi, più 72 da canali non pagati. Nello scenario base, fino al mese 30, i nuovi clienti sono {eur(b["clienti"])}, di cui {eur(b["pagati"])} da pubblicità: circa il 5% del bacino italiano in quindici mesi di vendita.</p>
  <h3>Che cosa implica per la scala</h3>
  <p>A regime, nello scenario base, i ricavi al netto dell'IVA stanno intorno ai 19.000 euro al mese, circa 230.000 l'anno. A quel livello l'attività si sostiene, ma restituisce il capitale lentamente. Per diventare un investimento con un ritorno importante servono tre cose che questo piano non dimostra: più riacquisto di quanto ipotizzato, più clienti a un costo sostenibile, un secondo mercato. Germania e Spagna, con le stesse proporzioni, porterebbero il bacino fra 150.000 e 230.000 persone, con due avvertenze: in Germania la farmacia pesa di più, in Spagna la capacità di spesa è diversa.</p>
</section>"""

def pill(stato):
    cls = {"verificata": "ok", "intervallo": "mid", "dedotta": "no", "non disponibile": "no", "farmaco": "ok"}[stato]
    return f'<span class="pill {cls}">{stato}</span>'

def cap06():
    righe = [
        ("Minoxidil 5% (farmaco)", "farmacia", "31,57-37,50 € / 60 mL", "1 mL due volte al giorno", "verificata", "≈ 32-38", "31,57"),
        ("OUAI Scalp Serum", "profumeria", "61,00 € / 60 mL *", "circa 1,5 mL, fino a 40 giorni", "verificata", "≈ 45,75", "61,00"),
        ("Kérastase Genesis", "salone, profumeria", "56,90 € / 90 mL", "4 pipette al giorno, volume non dichiarato", "non disponibile", "—", "34,90-56,90"),
        ("Vichy Dercos Aminexil", "farmacia", "51,20 € / 21 fiale", "due regimi riportati: 31-73 € a seconda del regime", "non disponibile", "—", "51,20"),
        ("Living Proof Density", "profumeria", "66,00 € / 50 mL *", "2-3 contagocce, volume non dichiarato", "intervallo", "—", "66,00"),
        ("Scandinavian Biolabs", "online", "55,00 € / 100 mL", "istruzioni e offerta da riconciliare", "non disponibile", "—", "39,00-55,00"),
        ("The Ordinary Multi-Peptide", "online, profumeria", "26,50 € / 60 mL *", "da rilevare", "non disponibile", "—", "26,50"),
        ("Bioscalin TricoAge", "farmacia", "48,56 € / 40 mL", "ricavata dal ciclo", "dedotta", "—", "48,56"),
        ("Ducray (linea anticaduta)", "farmacia", "44,94 € / 90 mL", "ricavata dal ciclo", "dedotta", "—", "44,94"),
        ("Crescina", "farmacia", "da rilevare", "da rilevare", "non disponibile", "—", "—"),
    ]
    body = "".join(f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td><td>{d}</td><td>{pill(e)}</td><td class="n">{f}</td><td class="n">{g}</td></tr>' for a, b, c, d, e, f, g in righe)
    return f"""
<section>
  <h2><span class="num">06</span>Le alternative del cliente</h2>
  <p class="lead">Il confronto di prezzo che si fa di solito, flacone contro flacone, dice poco: le dosi giornaliere della categoria vanno da meno di mezzo millilitro a diversi millilitri. Quello che conta per chi compra è quanto spende per provare, quanto spende per arrivare al primo risultato promesso, e quanto spende ogni mese.</p>
  <h3>Le dieci alternative prioritarie</h3>
  <table class="small">
    <thead><tr><th>Alternativa</th><th style="width:22mm">Canale</th><th style="width:28mm">Prezzo e formato</th><th style="width:36mm">Dose</th><th style="width:22mm">Stato della dose</th><th class="n" style="width:15mm">€ ogni 30 gg</th><th class="n" style="width:17mm">€ per provare</th></tr></thead>
    <tbody>{body}
      <tr class="hi"><td><b>Kriné</b>, percorso da 6</td><td>online</td><td>279 € / 6 × 60 mL</td><td>2 mL la sera</td><td>{pill("verificata")}</td><td class="n">48,95</td><td class="n">49-59</td></tr>
    </tbody>
    <caption>Prezzi da rivenditori online e pagine di marca rilevati con ricerca il 22/09/2026, da riaprire e archiviare. * prezzo italiano da confermare. Costo per 30 giorni calcolato solo con dose verificata; per Kriné su 57 mL utilizzabili per flacone. Stato completo nella mappa competitiva allegata.</caption>
  </table>
  <p>Oggi il confronto regge per due prodotti su dieci. Per il minoxidil la dose viene dal foglio illustrativo; per OUAI dalla pagina ufficiale della marca, mentre il prezzo italiano va ancora confermato. Per gli altri otto la dose manca, è un intervallo di pipette di volume ignoto, oppure è stata ricavata dalla durata di un ciclo di trattamento. Quest'ultimo metodo non vale: un ciclo di tre mesi può richiedere più confezioni, e un «mese di trattamento» dichiarato da una marca è una durata commerciale, non una dose.</p>
  <p>Ne segue che non sappiamo ancora di quanto la farmacia sia più economica di noi. Probabilmente lo è, e il farmaco certamente. Il completamento della mappa, con codice della confezione, prezzo ordinario e promozionale, dose con la sua fonte e data, è uno dei risultati della prima tappa.</p>
  <h3>Le tre spese che il cliente confronta</h3>
  <table class="tight">
    <thead><tr><th>Offerta Kriné</th><th class="n">Per provare</th><th class="n">Fino al giorno 150</th><th class="n">Ogni 30 giorni d'uso</th><th>Impegno</th></tr></thead>
    <tbody>
      <tr><td>Flacone singolo</td><td class="n">59 €</td><td class="n">354 €</td><td class="n">62,11 €</td><td>nessuno</td></tr>
      <tr><td>Abbonamento, invio ogni 28 giorni</td><td class="n">49 €</td><td class="n">294 €</td><td class="n">52,50 €</td><td>si interrompe quando si vuole</td></tr>
      <tr><td>Percorso da 3</td><td class="n">149 €</td><td class="n">≈ 298 €</td><td class="n">52,28 €</td><td>85 giorni pagati in anticipo</td></tr>
      <tr class="hi"><td>Percorso da 6, con garanzia</td><td class="n">279 €</td><td class="n">279 €</td><td class="n">48,95 €</td><td>171 giorni pagati in anticipo</td></tr>
    </tbody>
    <caption>Prezzi di listino, senza lo sconto medio del 5% sul primo ordine usato nel modello. Il giorno 150 è quello in cui si valuta la garanzia.</caption>
  </table>
  <p>Pagare 279 euro in anticipo e pagare 49 euro ogni quattro settimane sono decisioni diverse, anche se al giorno 150 costano quasi uguale. Il percorso da sei serve a chi ha già deciso e vuole la garanzia; per entrare ci sono il flacone singolo e l'abbonamento. Il modello ipotizza che la scelga un nuovo cliente su quattro. È l'ipotesi a cui la cassa è più sensibile dopo il costo di acquisizione, e nel capitolo 10 si vede quanto.</p>
  <h3>Trasparenza e garanzia: quanto è libero il terreno</h3>
  <p>Dichiarare alcune percentuali degli attivi non è una novità: The INKEY List pubblica l'1% di caffeina, di Redensyl e di betaina. Nessuna delle alternative rilevate le dichiara tutte, con la differenza rispetto agli studi; la verifica però non è completa. Una garanzia di rimborso lunga esiste presso Scandinavian Biolabs: 150 giorni d'uso consecutivo, foto mensili, cinque flaconi. Prova che il meccanismo esiste; non prova che sia redditizio, né per loro né per noi.</p>
</section>"""
