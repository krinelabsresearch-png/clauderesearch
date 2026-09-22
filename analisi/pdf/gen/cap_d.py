from base import *
HI = ' class="hi"'

def cap07():
    return """
<section>
  <h2><span class="num">07</span>Prove e comunicazione</h2>
  <p class="lead">Un pubblico si può aggredire solo con un beneficio che il giorno della campagna sappiamo sostenere con prove. Il capitolo dice quali prove compriamo, che cosa permettono di scrivere, e come si usa l'Academy.</p>
  <h3>La scala delle promesse e il costo delle prove</h3>
  <table>
    <thead><tr><th class="c" style="width:9mm">Liv.</th><th>Che cosa si può dire</th><th style="width:58mm">Prova sul prodotto finito</th><th class="n" style="width:18mm">Costo</th><th class="c" style="width:14mm">Al lancio</th></tr></thead>
    <tbody>
      <tr><td class="c">1</td><td>«Non unge», «asciuga in fretta», «nessun residuo»</td><td>Prove d'uso e strumentali</td><td class="n">4-9 k€</td><td class="c">sì</td></tr>
      <tr><td class="c">2</td><td>Cute più confortevole, meno desquamazione, meno prurito</td><td>Idratazione, barriera, valutazione dermatologica</td><td class="n">9-20 k€</td><td class="c">sì</td></tr>
      <tr><td class="c">3a</td><td>Capelli con più corpo, nel breve periodo</td><td>Foto standardizzate, valutatori, volume alla radice</td><td class="n">6-15 k€</td><td class="c">sì</td></tr>
      <tr><td class="c">3b</td><td>«Capelli dall'aspetto più pieno», nel lungo periodo</td><td>Conteggio fotografico a 24 settimane contro prodotto senza attivi</td><td class="n">70-150 k€</td><td class="c">no</td></tr>
      <tr><td class="c">4</td><td>«Aiuta a ridurre la caduta», con qualificatore</td><td>Studio controllato, popolazione coerente con il messaggio</td><td class="n">80-180 k€</td><td class="c">no</td></tr>
      <tr><td class="c">5</td><td>«Stimola la ricrescita», «tratta la calvizie»</td><td>—</td><td class="n">—</td><td class="c">mai</td></tr>
    </tbody>
    <caption>Costi e tempi stimati, da confermare con preventivi. Livelli 1, 2 e 3a si comprano in un protocollo unico da 22.000 euro. <span class="tag stima">stima</span></caption>
  </table>
  <p>La norma non chiede uno studio clinico nuovo per ogni frase. Chiede prove adeguate, verificabili e pertinenti a ciò che si afferma. Un protocollo ben disegnato sostiene più claim insieme, ed è per questo che i primi tre livelli si comprano in blocco. Il regolamento ammette anche i dati sugli ingredienti, purché si dimostri che la proprietà si trasferisce al prodotto finito. Per il comfort della cute l'argomento è sostenibile. Per i capelli, con dosi e regimi diversi da quelli studiati, non lo è: i dati sugli ingredienti li useremo solo nell'Academy, con i loro limiti, e mai come claim di prodotto.</p>
  <p>Un limite da conoscere: l'autovalutazione dei partecipanti non basta quando il claim implica un risultato biologico misurabile.</p>
  <h3>L'Academy, come esperimento</h3>
  <p>È una sezione del sito che pubblica gli studi sugli ingredienti della categoria, compresi quelli che non usiamo e quelli con esito negativo. Per ciascuno: disegno, numero di persone, durata, finanziatore, limiti. Serve ad aiutare il cliente a valutare le prove in una categoria dove chi compra ha spesso già speso soldi senza risultato. Non serve a fargli dedurre una superiorità che non abbiamo dimostrato: la valutazione legale tiene conto del contesto, e una sezione su un sito che vende resta comunicazione commerciale.</p>
  <p>La trattiamo come un esperimento con un costo noto, 9.000 euro, e un ritorno da misurare. Si parte con poche schede accurate: i sette attivi della tabella del capitolo 04 e il minoxidil come termine di confronto. Si misura quali pagine portano richieste, acquisti, e una migliore comprensione di ciò che il prodotto fa e non fa. Si espande solo se contribuisce. Il modello non le attribuisce nessuna riduzione del costo di acquisizione: i clienti da canali non pagati sono otto al mese in tutto.</p>
  <p>Tre vincoli valgono dal primo contenuto. Niente ripubblicazione dei testi: comprare un articolo non dà il diritto di ospitarlo, si pubblicano sintesi originali e collegamenti. Le prove sfavorevoli hanno lo stesso rilievo delle favorevoli. Nessun numero di efficacia accanto al carrello, e nessuna campagna che porti direttamente a una scheda con un aggancio di efficacia.</p>
  <div class="key"><span class="label">Stato delle prove · sulla pagina prodotto · aggiornato al [data]</span>
    <p>Le percentuali indicate sono quelle reali della formula. Gli studi dell'Academy riguardano i singoli ingredienti, non questo prodotto: non è dimostrato che i loro risultati si trasferiscano alla formula completa, né che si sommino.</p>
    <p><b>Dimostrato su questo prodotto:</b> comfort del cuoio capelluto, riduzione della desquamazione visibile, assenza di residuo. <b>Non ancora dimostrato:</b> aumento della densità, riduzione della caduta.</p>
  </div>
</section>"""

def cap08():
    b = N["scenari"]["Base"]
    esempio = 1200 * 0.25 * 0.55 * 0.22 * per_ordine("p6", 8.5, 0.05)["lordo"]
    return f"""
<section>
  <h2><span class="num">08</span>Offerta, formato, garanzia</h2>
  <p class="lead">Quattro modi di comprare lo stesso flacone da 60 millilitri, e una garanzia definita in ogni dettaglio prima di scriverla su una pagina.</p>
  <h3>Il formato</h3>
  <p>Sessanta millilitri, meno il cinque per cento che resta nel flacone airless, fanno 57 millilitri utilizzabili: a due millilitri al giorno sono 28,5 giorni. Per questo l'abbonamento consegna ogni 28 giorni e non ogni mese. Una consegna mensile lascerebbe il cliente senza prodotto per due giorni ogni mese, e una routine quotidiana non deve dipendere dal calendario. Il residuo del 5% è un'ipotesi, da misurare sul flacone scelto.</p>
  <table>
    <thead><tr><th>Formato</th><th class="n">Giorni d'uso</th><th class="n">Prezzo</th><th class="n">€ ogni 30 gg</th><th>Ruolo</th></tr></thead>
    <tbody>
      <tr><td>Flacone singolo</td><td class="n">28,5</td><td class="n">59 €</td><td class="n">62,11</td><td>Prova, riferimento di prezzo</td></tr>
      <tr><td>Abbonamento, ogni 28 giorni</td><td class="n">28,5 per invio</td><td class="n">49 €</td><td class="n">52,50</td><td>Ingresso con barriera minima</td></tr>
      <tr><td>Percorso da 3</td><td class="n">85,5</td><td class="n">149 €</td><td class="n">52,28</td><td>Impegno intermedio</td></tr>
      <tr class="hi"><td>Percorso da 6, con garanzia</td><td class="n">171</td><td class="n">279 €</td><td class="n">48,95</td><td>Per chi ha deciso</td></tr>
    </tbody>
  </table>
  <p>Sei flaconi danno 342 millilitri utilizzabili, cioè 171 giorni: coprono i 150 della garanzia con tre settimane di margine, senza costringere il cliente a un acquisto in più a metà strada.</p>
  <h3>La garanzia, regola per regola</h3>
  <table>
    <thead><tr><th style="width:36mm">Elemento</th><th>Regola</th></tr></thead>
    <tbody>
      <tr><td><b>Che cosa copre</b></td><td>La soddisfazione del cliente per l'aspetto dei capelli e il comfort della cute dopo 150 giorni d'uso. Usa le stesse parole dei claim: non promette ricrescita e non la lascia intendere.</td></tr>
      <tr><td><b>Su quali acquisti</b></td><td>Solo il percorso da sei, al primo acquisto, una volta per persona. Abbonamento e flacone singolo non hanno garanzia: l'abbonamento si interrompe quando si vuole.</td></tr>
      <tr><td><b>Importo</b></td><td>Quanto pagato, IVA e spedizione comprese. Il rimborso arriva entro 14 giorni dalla richiesta accolta.</td></tr>
      <tr><td><b>Documentazione</b></td><td>Una foto entro sette giorni dalla consegna e una al giorno 150, seguendo una guida su luce e distanza, più un breve questionario. Le foto servono anche a noi: sono il dato che misura il risultato.</td></tr>
      <tr><td><b>Quando si chiede</b></td><td>Fra il giorno 150 e il giorno 200 dalla consegna. Oltre, la richiesta non si accetta: l'esposizione si chiude a circa sette mesi dall'acquisto.</td></tr>
      <tr><td><b>Interruzioni</b></td><td>Se il prodotto non è tollerato si smette subito, e i flaconi non aperti si rimborsano fuori dalla garanzia, senza condizioni. Nessuno deve continuare un uso mal tollerato per restare in garanzia. Una pausa fino a 14 giorni (viaggio, malattia) sposta i termini.</td></tr>
      <tr><td><b>Recesso</b></td><td>Il diritto di recesso di 14 giorni resta ed è indipendente dalla garanzia. L'esclusione per i flaconi aperti, per ragioni igieniche, va confermata dal legale.</td></tr>
      <tr><td><b>Contabilità</b></td><td>Il rimborso riduce il ricavo; dal conto esce l'importo lordo e l'IVA si recupera con nota di variazione. L'accantonamento del 3% per assistenza, resi ordinari e sostituzioni è separato e non si sovrappone.</td></tr>
    </tbody>
  </table>
  <h3>Quanto costa, e quando</h3>
  <p>Nel modello chiede il rimborso il 22% di chi completa il percorso; il completamento è del 55%, quindi i rimborsi valgono il 12,1% dei percorsi venduti. Metà arrivano nel quinto mese dopo l'acquisto e metà nel sesto. Un esempio: 1.200 nuovi clienti, di cui un quarto sceglie il percorso, generano rimborsi attesi per {eur(esempio)} euro lordi, distribuiti su diversi mesi. Il fabbisogno si calcola quindi per coorte: nello scenario base i rimborsi attesi non ancora pagati non superano mai {eur(b["esp"])} euro, e la cassa non scende mai sotto quella cifra più tre mesi di costi fissi.</p>
  <p>Il 12,1% è un'ipotesi da stressare, non un dato di mercato. I tassi di reso del commercio online di cosmetici misurano un evento diverso, il reso entro pochi giorni, e non si possono usare per giustificarlo. Lo misureremo sulle prime coorti, con cento-duecento clienti: abbastanza per vedere problemi e segnali, non per stimare con precisione ogni sottogruppo.</p>
</section>"""

def cap09():
    o = N["ordine"]; o1 = N["ordine_primo"]; V = N["valore"]; CM = N["costo"]
    offs = ["p6", "p3", "abb", "sing"]; nomi = ["Percorso 6", "Percorso 3", "Abbon.", "Singolo"]
    def riga(lbl, key, src, neg=False):
        return f'<tr><td>{lbl}</td>' + "".join(f'<td class="n">{"−" if neg else ""}{e2(src[x][key])}</td>' for x in offs) + "</tr>"
    tab_o = "".join([riga("Prezzo pagato", "lordo", o), riga("Ricavo netto IVA", "netto", o), riga("Prodotto", "prodotto", o, True),
                     riga("Logistica", "logistica", o, True), riga("Commissione di incasso", "incasso", o, True),
                     riga("Assistenza, resi ordinari, sostituzioni", "assist", o, True)])
    contr = '<tr class="hi"><td>Contribuzione</td>' + "".join(f'<td class="n">{e2(o[x]["contrib"])}</td>' for x in offs) + "</tr>"
    contr1 = '<tr><td>Contribuzione del primo ordine, con sconto medio del 5%</td>' + "".join(f'<td class="n">{e2(o1[x]["contrib"])}</td>' for x in offs) + "</tr>"
    rimb = "".join(f'<tr{HI if abs(q-0.121)<1e-9 else ""}><td class="n">{pct(q)}</td><td class="n">{e2(c)}</td><td class="n">{e2(c-50)}</td><td class="n">{e2(c-60)}</td><td class="n">{e2(c-80)}</td></tr>' for q, c in N["rimborsi_p6"])
    par = N["pareggio_p6"]
    val = "".join(f'<tr{HI if h=="24" else ""}><td>entro {h} mesi</td>' + "".join(f'<td class="n">{e2(V[h][x]["valore"])}</td>' for x in offs) + f'<td class="n"><b>{e2(V[h]["medio"])}</b></td></tr>' for h in ("1", "3", "6", "12", "24", "36"))
    cst = "".join(f'<tr{HI if c=="8.5" else ""}><td class="n">{e2(float(c))} €</td><td class="n">{e2(v[0])}</td><td class="n">{e2(v[1])}</td><td class="n">{e2(v[2])}</td></tr>' for c, v in CM.items())
    single_net = o["sing"]["contrib"] / o["sing"]["netto"]; single_gross = o["sing"]["contrib"] / o["sing"]["lordo"]
    return f"""
<section>
  <h2><span class="num">09</span>Economia per ordine e per cliente</h2>
  <p class="lead">Quanto resta di ogni ordine con tutti i costi variabili, quanto vale un cliente nel tempo, e quanto possiamo spendere per acquisirlo.</p>
  <h3>Il costo industriale</h3>
  <table class="tight">
    <thead><tr><th>Voce</th><th class="n">Per flacone da 60 mL</th></tr></thead>
    <tbody>
      <tr><td>Materie prime</td><td class="n">2,50-5,90 €</td></tr>
      <tr><td>Flacone airless con pompa dosatrice</td><td class="n">1,20-2,40 €</td></tr>
      <tr><td>Astuccio, etichetta, foglietto</td><td class="n">0,45-0,90 €</td></tr>
      <tr><td>Riempimento, assemblaggio, controlli</td><td class="n">1,00-2,00 €</td></tr>
      <tr><td>Analisi di rilascio del lotto</td><td class="n">0,20-0,70 €</td></tr>
      <tr class="hi"><td>Totale</td><td class="n">5,35-11,90 € · centrale 8,50 €</td></tr>
    </tbody>
    <caption>Prezzi indicativi di distribuzione europea a volumi di sviluppo; incertezza di un fattore due sulle voci principali. <span class="tag stima">stima</span></caption>
  </table>
  <h3>Che cosa resta di un ordine</h3>
  <table class="tight">
    <thead><tr><th>€ per ordine, costo industriale 8,50 €</th>{"".join(f'<th class="n">{n}</th>' for n in nomi)}</tr></thead>
    <tbody>{tab_o}{contr}{contr1}</tbody>
    <caption>IVA 22%. Logistica: prelievo e imballo 1,20 € più corriere da 4,50 € (un flacone) a 6,50 € (sei). Commissione di incasso 1,9% più 0,25 €: media prudente, perché le carte europee standard costano meno (1,5%) e quelle premium o extraeuropee di più. Assistenza, resi ordinari e sostituzioni: 3% del ricavo netto.</caption>
  </table>
  <p>Sul flacone singolo la contribuzione di {e2(o["sing"]["contrib"])} euro è il {pct(single_net)} del ricavo al netto dell'IVA, oppure il {pct(single_gross)} del prezzo pagato. In entrambi i casi è calcolata prima della pubblicità, che si aggiunge dopo.</p>
  <h3>I rimborsi sul percorso da sei</h3>
  <table class="tight">
    <thead><tr><th class="n">Rimborsi sui percorsi venduti</th><th class="n">Contribuzione per percorso</th><th class="n">dopo CAC 50 €</th><th class="n">dopo CAC 60 €</th><th class="n">dopo CAC 80 €</th></tr></thead>
    <tbody>{rimb}
      <tr><td class="n"><b>Pareggio</b></td><td class="n">—</td><td class="n">{pct(par["50"])}</td><td class="n">{pct(par["60"])}</td><td class="n">{pct(par["80"])}</td></tr>
    </tbody>
    <caption>Primo ordine con sconto medio del 5%: prezzo pagato {e2(o1["p6"]["lordo"])} €, ricavo netto {e2(o1["p6"]["netto"])} €. Il rimborso restituisce quanto pagato; prodotto, spedizione, commissione e assistenza restano spesi. Il 12,1% è l'ipotesi centrale.</caption>
  </table>
  <h3>Il valore di un cliente nel tempo</h3>
  <p>Il valore di un cliente dipende dall'orizzonte su cui lo si misura, e un valore a sei mesi non si confronta con uno sull'intera relazione. Per questo lo diamo per orizzonte, per offerta e per il cliente medio, con il mix ipotizzato: 25% percorso da sei, 10% percorso da tre, 45% abbonamento, 20% flacone singolo.</p>
  <table class="tight">
    <thead><tr><th>Contribuzione cumulata per nuovo cliente, €</th>{"".join(f'<th class="n">{n}</th>' for n in nomi)}<th class="n">Medio</th></tr></thead>
    <tbody>{val}</tbody>
    <caption>Al netto dei rimborsi, prima della pubblicità. Il percorso da sei scende fra il terzo e il sesto mese perché lì cadono i rimborsi. Abbonamento: rinnovo del 65% dopo il primo invio, poi 70%, 72%, 78%, 82% e 85% dal sesto; 3,7 invii nel primo anno. Singolo: 1,6 ordini in media. <span class="tag">ipotesi</span></caption>
  </table>
  <h3>Il costo di acquisizione che possiamo permetterci</h3>
  <p>Il CAC massimo esce dal modello come risultato; la domanda è se quel valore sia raggiungibile. La regola che ci diamo ha due condizioni, e le decisioni si prendono sul CAC complessivo, non su quello pubblicitario.</p>
  <table class="tight">
    <thead><tr><th>Condizione</th><th class="n">Scenario base</th></tr></thead>
    <tbody>
      <tr><td>Il valore del cliente medio a 24 mesi è almeno il doppio del CAC complessivo</td><td class="n">CAC massimo {e2(V["24"]["medio"]/2)} €</td></tr>
      <tr><td>La coorte media recupera il CAC complessivo entro tre mesi</td><td class="n">55 € nel primo mese, 60 € nel secondo</td></tr>
    </tbody>
  </table>
  <p>Nello scenario base la pubblicità costa 50 euro per cliente nelle prime due tranche e 55 nella terza, perché più spesa significa clienti marginali più cari. Aggiungendo creatività e gestione il CAC complessivo delle prime due tranche è 55,00 euro, contro un massimo di {e2(V["24"]["medio"]/2)}. Lo scenario base è al limite della regola, e non la correggiamo per farlo passare. Nello scenario base la cassa regge comunque, con un margine più sottile di quello che ci siamo imposti. Per rientrare nella regola, almeno una delle ipotesi centrali, fra costo di acquisizione, quota del percorso da sei, rinnovi e costo industriale, deve rivelarsi migliore del previsto.</p>
  <table class="tight">
    <thead><tr><th class="n">Costo industriale per flacone</th><th class="n">Valore a 12 mesi</th><th class="n">Valore a 24 mesi</th><th class="n">CAC massimo</th></tr></thead>
    <tbody>{cst}</tbody>
    <caption>Tutte le altre ipotesi dello scenario base invariate.</caption>
  </table>
  <p>Con il costo industriale alto già considerato, anche un CAC di 49 euro supera il limite. «Sotto i 50 euro si scala» non è quindi una regola valida da sola: il limite si ricalcola ogni volta con il costo industriale, il mix di offerte e i rinnovi osservati. Nello scenario avverso, dove tutto peggiora insieme, il valore a 24 mesi scende a {e2(N["valore_avv"]["24"])} euro e il CAC massimo a {e2(N["valore_avv"]["24"]/2)}.</p>
</section>"""
