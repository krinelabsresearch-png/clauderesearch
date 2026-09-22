from base import *

B = N["scenari"]["Base"]; RIT = N["scenari"]["Lancio ritardato"]; AVS = N["scenari"]["Avverso senza arresto"]
AVA = N["scenari"]["Avverso con arresto"]; TUT = N["scenari"]["Tutto insieme"]
V = N["valore"]; CM = N["costo"]
cacmax = V["24"]["medio"] / 2

def cover():
    return f"""
<div class="cover">
  <div>
    <div class="brand">Kriné Labs</div>
    <div class="rule"></div>
    <h1>Piano di progetto<br>e richiesta di finanziamento</h1>
    <div class="sub">Siero leave-on per il cuoio capelluto. Che cosa sappiamo, che cosa ipotizziamo, che cosa compra ogni tranche dei 250.000 euro e in quali condizioni ci fermiamo.</div>
  </div>
  <div>
    <div class="meta">
      <b>Oggetto</b> · Piano di sviluppo e di lancio, modello di cassa a trenta mesi, regole di arresto<br>
      <b>Base documentale</b> · Dossier tecnico di formulazione V9.3 (formula guida C) · modello di cassa (modello-cassa.xlsx) · mappa competitiva (mappa-competitiva.xlsx)<br>
      <b>Data</b> · 22 settembre 2026<br>
      <b>Stato</b> · Versione per la verifica dell'investitore
    </div>
    <div class="conf">Documento riservato · uso esclusivo del destinatario</div>
  </div>
</div>"""

def cap00():
    return """
<section class="cont" style="page-break-before:always">
  <h2><span class="num">00</span>Come leggere questo documento</h2>
  <p class="lead">Il documento serve a decidere se finanziare con 250.000 euro un prodotto cosmetico che non esiste ancora. Separa ciò che è verificabile da ciò che stimiamo e da ciò che scommettiamo, e lega ogni spesa a una decisione. I numeri economici escono da un modello di cassa allegato, che chiunque può aprire e modificare.</p>
  <h3>Tre livelli di affermazione</h3>
  <table>
    <thead><tr><th style="width:26mm">Livello</th><th>Che cos'è</th><th style="width:44mm">Come lo riconoscete</th></tr></thead>
    <tbody>
      <tr><td><b>Dato</b></td><td>Verificabile da un terzo: dossier tecnico, pagina pubblica con indirizzo, norma, articolo scientifico</td><td>fonte accanto, elenco completo nel capitolo 16</td></tr>
      <tr><td><b>Stima</b></td><td>Un calcolo nostro a partire da dati. Valori di partenza dichiarati, aritmetica riproducibile nel modello</td><td>etichetta <span class="tag stima">stima</span></td></tr>
      <tr><td><b>Ipotesi</b></td><td>Una scommessa non ancora verificata. Il piano esiste per trasformarla in dato o scartarla</td><td>etichetta <span class="tag">ipotesi</span></td></tr>
    </tbody>
  </table>
  <h3>Indice</h3>
  <div class="toc">
    <div class="e"><div class="t"><b>01</b>In breve</div><div class="d">la richiesta, la domanda, i numeri</div></div>
    <div class="e"><div class="t"><b>02</b>Che cosa compra il capitale</div><div class="d">noto, ipotizzato, da verificare</div></div>
    <div class="e"><div class="t"><b>03</b>La domanda centrale</div><div class="d">il cliente paga per ciò che possiamo promettere?</div></div>
    <div class="e"><div class="t"><b>04</b>Il prodotto e la formula guida</div><div class="d">attivo per attivo, dose per dose</div></div>
    <div class="e"><div class="t"><b>05</b>Il mercato</div><div class="d">bacino, flusso annuo, imbuto di acquisizione</div></div>
    <div class="e"><div class="t"><b>06</b>Le alternative del cliente</div><div class="d">quanto costano davvero, e che cosa sappiamo</div></div>
    <div class="e"><div class="t"><b>07</b>Prove e comunicazione</div><div class="d">scala dei claim, costi, Academy</div></div>
    <div class="e"><div class="t"><b>08</b>Offerta, formato, garanzia</div><div class="d">regole complete della garanzia</div></div>
    <div class="e"><div class="t"><b>09</b>Economia per ordine e per cliente</div><div class="d">contribuzione, valore, CAC sostenibile</div></div>
    <div class="e"><div class="t"><b>10</b>Coorti e cassa a trenta mesi</div><div class="d">cinque scenari, IVA, scorte</div></div>
    <div class="e"><div class="t"><b>11</b>I 250.000 euro e le regole di arresto</div><div class="d">tappe, verifiche, capitale a rischio</div></div>
    <div class="e"><div class="t"><b>12</b>I rischi</div><div class="d">in ordine di gravità</div></div>
    <div class="e"><div class="t"><b>13</b>Ritorno e valutazione</div><div class="d">pareggio, recupero, ritorno dell'azionista</div></div>
    <div class="e"><div class="t"><b>14</b>Squadra, proprietà, contratti</div><div class="d">chi possiede che cosa</div></div>
    <div class="e"><div class="t"><b>15</b>I primi novanta giorni</div><div class="d">protocollo delle interviste e prima verifica</div></div>
    <div class="e"><div class="t"><b>16</b>Metodo, fonti e limiti</div><div class="d">indirizzi, date, ciò che manca</div></div>
    <div class="e"><div class="t"><b>A</b>Costi voce per voce</div><div class="d">per chiedere preventivi confrontabili</div></div>
    <div class="e"><div class="t"><b>B</b>Le ipotesi del modello</div><div class="d">tutti i parametri, per scenario</div></div>
  </div>
</section>
<section>
  <h3 style="margin-top:0">Gli allegati</h3>
  <table>
    <thead><tr><th style="width:44mm">File</th><th>Che cosa contiene</th></tr></thead>
    <tbody>
      <tr><td><b>modello-cassa.xlsx</b></td><td>Cassa mese per mese dal mese 1 al 30, in cinque scenari. Tutte le celle sono formule; le ipotesi stanno in un solo foglio, una colonna per scenario. Il foglio è stato ricalcolato con un valutatore indipendente e confrontato con un secondo modello scritto da zero: gli scostamenti sono sotto il centesimo.</td></tr>
      <tr><td><b>mappa-competitiva.xlsx</b></td><td>Griglia di rilevazione di prezzi, dosi, garanzie e claim delle alternative. Le statistiche si calcolano solo sulle righe verificate da una persona, con indirizzo e data.</td></tr>
    </tbody>
  </table>
  <h3>Le parole che ricorrono</h3>
  <table>
    <thead><tr><th style="width:40mm">Termine</th><th>Che cosa significa qui</th></tr></thead>
    <tbody>
      <tr><td><b>Siero leave-on</b></td><td>Un liquido che si applica e non si risciacqua. Resta sulla pelle fino al lavaggio successivo.</td></tr>
      <tr><td><b>Attivo</b></td><td>Un ingrediente inserito per un effetto, non per dare consistenza o profumo. La quantità si esprime in percentuale sul peso.</td></tr>
      <tr><td><b>Claim</b></td><td>Ciò che si scrive su confezione, sito e pubblicità. In Europa ogni claim va sostenuto da prove adeguate e verificabili, pertinenti a ciò che si afferma. I dati su un ingrediente possono bastare se si dimostra che la proprietà si trasferisce al prodotto finito (Regolamento UE 655/2013).</td></tr>
      <tr><td><b>Percorso</b></td><td>La confezione da tre o da sei flaconi, pagata in anticipo. Solo quella da sei ha la garanzia di rimborso.</td></tr>
      <tr><td><b>Contribuzione</b></td><td>Quanto resta di un ordine dopo IVA, prodotto, spedizione, commissioni di incasso e assistenza. Prima della pubblicità e dei costi fissi.</td></tr>
      <tr><td><b>Valore del cliente</b></td><td>La contribuzione cumulata che un nuovo cliente porta entro un orizzonte dichiarato (6, 12, 24 mesi), al netto dei rimborsi.</td></tr>
      <tr><td><b>CAC</b></td><td>Costo di acquisizione di un cliente. <i>Pubblicitario</i>: spesa in annunci divisa per i nuovi clienti attribuiti. <i>Complessivo</i>: aggiunge creatività e gestione. <i>Marginale</i>: quanto costano i clienti in più quando si alza il budget.</td></tr>
      <tr><td><b>Coorte</b></td><td>L'insieme dei clienti acquisiti nello stesso mese, seguiti nel tempo.</td></tr>
      <tr><td><b>Regola di arresto</b></td><td>Una condizione numerica, scritta prima di spendere, che decide se la spesa successiva parte o no.</td></tr>
      <tr><td><b>Academy</b></td><td>Una sezione del sito che pubblica gli studi sugli ingredienti della categoria, favorevoli e sfavorevoli, con i loro limiti. Descritta nel capitolo 07.</td></tr>
      <tr><td><b>Airless</b></td><td>Flacone con pompa che eroga senza far entrare aria e dosa una quantità fissa a ogni pressione. Trattiene un piccolo residuo non erogabile.</td></tr>
    </tbody>
  </table>
</section>"""

def cap01():
    return f"""
<section>
  <h2><span class="num">01</span>In breve</h2>
  <p class="lead">Chiediamo 250.000 euro per portare sul mercato un siero per il cuoio capelluto e per misurare, con clienti veri, se il marchio regge economicamente. Proponiamo di versarli in due tranche: 100.000 alla firma e 150.000 quando il prodotto ha superato le prove di laboratorio e di tollerabilità.</p>
  <h3>La domanda a cui risponde il capitale</h3>
  <p>Un cosmetico non può promettere di far ricrescere i capelli. Può promettere una cute più confortevole e capelli dall'aspetto più pieno, se lo dimostra sul prodotto finito. La domanda economica è se chi spende circa cinquanta euro al mese in questa categoria compri quello che possiamo promettere, e resti cliente abbastanza a lungo. Il capitolo 03 la tratta per intero. La nostra risposta, in breve: il mercato che paga questi prezzi per claim cosmetici esiste ed è in crescita, ma compra l'aspetto dei capelli e la fiducia nel marchio, non la sola salute della cute. Il rischio vero sta nel tempo che passa fra l'acquisto e il primo risultato visibile.</p>
  <h3>Che cosa dice il modello di cassa</h3>
  <div class="stat-row">
    <div class="stat"><div class="v">{eur(B["assorbito"])} €</div><div class="k">capitale assorbito fino al lancio, nello scenario base. Il minimo di cassa cade al mese {B["mese_min"]}</div></div>
    <div class="stat"><div class="v">{eur(TUT["minimo"])} €</div><div class="k">cassa minima nel caso peggiore costruito: lancio in ritardo, costi alti, clienti più cari, nessuna regola di arresto</div></div>
    <div class="stat"><div class="v">{e2(cacmax)} €</div><div class="k">CAC massimo sostenibile nello scenario base, con la nostra regola: metà del valore del cliente a 24 mesi</div></div>
  </div>
  <p>La somma richiesta basta in tutti e cinque gli scenari costruiti. Nello scenario base la cassa tocca {eur(B["minimo"])} euro al mese {B["mese_min"]}, subito prima del lancio, e risale a {eur(B["c30"])} euro al mese 30 con le sole vendite. Lo scenario base è però al limite della nostra stessa regola sul costo di acquisizione: il CAC complessivo delle prime due tranche di pubblicità è 55,00 euro contro un massimo di {e2(cacmax)}. La cassa regge comunque; per avere il margine che la regola richiede, almeno una delle ipotesi centrali deve rivelarsi migliore del previsto.</p>
  <h3>Le tre cose che non sappiamo, e quando lo sapremo</h3>
  <table>
    <thead><tr><th>Incognita</th><th style="width:48mm">Come si misura</th><th class="n" style="width:22mm">Quando</th></tr></thead>
    <tbody>
      <tr><td>Se il cliente compra il beneficio che possiamo dimostrare, o pretende la ricrescita</td><td>Interviste con una regola di decisione scritta prima, poi un test di messaggio a pagamento</td><td class="n">mesi 1-3 e 12-15</td></tr>
      <tr><td>Quanto costa acquisire un cliente, e quale offerta sceglie</td><td>Due tranche di pubblicità da 10.000 e 20.000 euro</td><td class="n">mesi 16-20</td></tr>
      <tr><td>Quanti restano: rinnovi, rimborsi della garanzia, riacquisto dopo il percorso</td><td>Coorti seguite fino a oltre il giorno 150</td><td class="n">mesi 21-27</td></tr>
    </tbody>
  </table>
  <div class="key"><span class="label">Il punto di partenza</span>
    <p>Abbiamo una formula documentata attivo per attivo, con alternative già calcolate e un capitolato pronto per i laboratori. Non abbiamo ancora un lotto di prova, uno studio sul prodotto finito, un cliente. Ogni fase del piano espone capitale a perdita; le regole di arresto servono a spenderne il meno possibile prima di sapere se conviene continuare.</p>
  </div>
</section>"""

def cap02():
    return f"""
<section>
  <h2><span class="num">02</span>Che cosa compra il capitale</h2>
  <p class="lead">La tabella divide ciò che sappiamo da ciò che stiamo scommettendo, e indica quale spesa risolve ciascuna scommessa.</p>
  <table>
    <thead><tr><th>Questione</th><th style="width:18mm">Stato</th><th style="width:78mm">Che cosa la risolve, quando, quanto costa</th></tr></thead>
    <tbody>
      <tr><td>Composizione, dosi, razionale, alternative</td><td>noto</td><td>Dossier tecnico completo, attivo per attivo</td></tr>
      <tr><td>Che cosa può dire un cosmetico</td><td>noto</td><td>Norme europee e prassi di mercato (capitolo 03 e 07)</td></tr>
      <tr><td>Prezzi e dosi delle alternative</td><td>parziale</td><td>Mappa competitiva: dieci alternative prioritarie da verificare. Lavoro interno, mesi 1-3</td></tr>
      <tr><td><b>Il cliente compra il beneficio che possiamo dimostrare</b></td><td>ipotesi</td><td>Sedici interviste condotte dai fondatori (1.500 €, mesi 1-3); test di messaggio a pagamento (8.000 €, mesi 12-15)</td></tr>
      <tr><td>La formula C non ricade in brevetti altrui</td><td>ipotesi</td><td>Parere di libertà di attuazione su perimetro definito, 3.500 €, mese 2</td></tr>
      <tr><td><b>La formula si produce entro i vincoli d'uso</b></td><td>ipotesi</td><td>Fattibilità, metodi analitici, micro-prove, candidati: 33.000 €, mesi 4-9</td></tr>
      <tr><td>È tollerata nell'uso ripetuto</td><td>ipotesi</td><td>Patch test e uso ripetuto per quattro settimane: 8.000 €, mesi 8-9</td></tr>
      <tr><td>Possiamo dire qualcosa che valga il prezzo</td><td>ipotesi</td><td>Un protocollo unico su comfort della cute e aspetto del capello: 22.000 €, mesi 11-13</td></tr>
      <tr><td><b>Acquisire un cliente costa meno di {eur(cacmax)} euro</b></td><td>ipotesi</td><td>Solo la vendita lo misura: 30.000 € di pubblicità nelle prime due tranche, mesi 16-20</td></tr>
      <tr><td><b>Chi compra resta</b></td><td>ipotesi</td><td>Rinnovi dell'abbonamento, completamento del percorso, rimborsi, riacquisto: mesi 17-27</td></tr>
      <tr><td>Il vantaggio è difendibile</td><td>ipotesi</td><td>Non dalla formula, che è pubblica per legge. Da dati propri, riacquisto e reputazione, nel tempo</td></tr>
    </tbody>
  </table>
  <p class="note">In grassetto le questioni che possono fermare il progetto.</p>
</section>"""
