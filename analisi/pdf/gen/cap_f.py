from base import *

def cap11():
    S = N["scenari"]; t = N["tranche"]
    return f"""
<section>
  <h2><span class="num">11</span>I 250.000 euro e le regole di arresto</h2>
  <p class="lead">Ogni fase espone capitale a perdita. Le tappe servono a limitare la spesa prima di affrontare il rischio successivo, e ogni tappa si chiude con una verifica numerica scritta adesso, non dopo aver visto i risultati. Nel caso prudente non attribuiamo alcun valore di realizzo a formula, dossier, marchio e studi.</p>
  <h3>Dove vanno i soldi</h3>
  <table class="tight">
    <thead><tr><th>Tappa</th><th class="n">Mesi</th><th class="n">Euro, netto IVA</th><th>Che cosa compra</th></tr></thead>
    <tbody>
      <tr><td>1 · Verifiche preliminari</td><td class="n">1-3</td><td class="n">12.500</td><td>Società e patti, parere brevettuale sulla formula C, marchio, interviste, mappa verificata, preventivi confrontabili</td></tr>
      <tr><td>2 · Laboratorio e tollerabilità</td><td class="n">4-9</td><td class="n">41.500</td><td>Fattibilità, metodi analitici, micro-prove, candidato completo, prova di colore, patch test e uso ripetuto</td></tr>
      <tr><td>3 · Prodotto pronto</td><td class="n">10-15</td><td class="n">92.300</td><td>Stabilità, protocollo per i claim, sicurezza e notifica, Academy, confezione e sito, test di messaggio, lotto pilota, primo lotto da 3.000 flaconi</td></tr>
      <tr><td>IVA anticipata e costi fissi fino al lancio</td><td class="n">1-15</td><td class="n">37.064</td><td>IVA ai fornitori italiani, recuperata dopo il lancio; commercialista, strumenti, piattaforma</td></tr>
      <tr class="hi"><td>Fino al lancio</td><td class="n">1-15</td><td class="n">{eur(S["Base"]["assorbito"])}</td><td>Coincide con il capitale assorbito al minimo di cassa</td></tr>
      <tr><td>4 · Misura sul mercato</td><td class="n">16-24</td><td class="n">60.000 + lotti</td><td>Pubblicità in tre tranche da 10.000, 20.000 e 30.000 euro; i lotti successivi si pagano in parte con le vendite</td></tr>
      <tr class="hi"><td>Margine al punto più basso</td><td class="n">15</td><td class="n">{eur(S["Base"]["minimo"])}</td><td>Copre un lancio in ritardo di quattro mesi, che assorbe {eur(S["Lancio ritardato"]["assorbito"])} euro</td></tr>
    </tbody>
  </table>
  <h3>Due tranche invece di una</h3>
  <p>Proponiamo che il capitale arrivi in due versamenti: 100.000 euro alla firma e 150.000 al superamento della verifica della tappa 2, al mese 10. Nel modello, con 100.000 euro iniziali la cassa al mese 9 è ancora di {eur(t["min_prima"])} euro. Il capitale che l'investitore rischia prima di sapere se il prodotto si può fabbricare ed è tollerato scende così a circa {eur(round(t["speso_m9"], -3))} euro.</p>
  <h3>Le verifiche</h3>
  <div class="gate"><div class="h">Fine tappa 1, mese 3 · si parte con il laboratorio se</div><ul>
    <li>il parere conclude che la formula C non ricade nelle rivendicazioni individuate, oppure indica un'alternativa percorribile;</li>
    <li>almeno due laboratori quotano le fasi di sviluppo entro 45.000 euro, a parità di capitolato;</li>
    <li>almeno una delle due offerte supera la regola delle interviste: meno di cinque persone su otto chiedono la ricrescita come condizione per ricomprare.</li></ul></div>
  <div class="gate"><div class="h">Fine tappa 2, mese 9 · si libera la seconda tranche se</div><ul>
    <li>il candidato è stabile nelle prove preliminari: adenosina in soluzione (frazione filtrata su totale di almeno 0,95), nessuna separazione;</li>
    <li>patch test e uso ripetuto per quattro settimane restano sotto le soglie di reazione fissate prima con il dermatologo;</li>
    <li>nessun residuo visibile su capello lavato ogni tre giorni. Se una condizione manca, si applica l'ordine di modifiche del dossier: è lo scenario Ritardo, che costa quattro mesi e 12.000 euro.</li></ul></div>
  <div class="gate"><div class="h">Mese 13 · si ordina il primo lotto se</div><ul>
    <li>il protocollo sostiene i claim dei livelli 1, 2 e 3a;</li>
    <li>la stabilità accelerata a tre mesi è conforme;</li>
    <li>il test di messaggio porta iscrizioni qualificate a non più di 12 euro l'una su almeno un'offerta.</li></ul></div>
  <div class="gate"><div class="h">Mese 20 · si libera la terza tranche di pubblicità se</div><ul>
    <li>il CAC complessivo misurato sulle prime due tranche non supera metà del valore a 24 mesi, ricalcolato con il mix, il costo industriale e i rinnovi osservati;</li>
    <li>la coorte media recupera il CAC complessivo entro tre mesi;</li>
    <li>almeno il 55% degli abbonati rinnova dopo il primo invio;</li>
    <li>al controllo del giorno 60 almeno il 70% di chi ha il percorso da sei lo sta usando;</li>
    <li>i reclami per tollerabilità restano sotto il 2% dei clienti;</li>
    <li>dopo la terza tranche la cassa copre i rimborsi attesi non ancora pagati, gli impegni sui lotti e tre mesi di costi fissi.</li></ul>
    <p style="margin:1.5mm 0 0;font-size:9.4pt">Se le prime due condizioni mancano di meno del 20% si rivede l'offerta e si riprova con 10.000 euro. Oltre, o se manca la quinta, si ferma la pubblicità a pagamento.</p></div>
  <div class="gate"><div class="h">Mesi 24-27 · si apre la raccolta successiva se</div><ul>
    <li>sulle coorti che hanno superato il giorno 200 i rimborsi restano sotto il 20% dei percorsi venduti;</li>
    <li>il riacquisto dopo il percorso e la curva di rinnovo confermano un valore a 24 mesi almeno doppio del CAC complessivo.</li></ul></div>
  <p>Il costo di queste regole si vede nel modello: nello scenario avverso la terza tranche non parte, si acquisiscono {eur(S["Avverso con arresto"]["clienti"])} clienti invece di {eur(S["Avverso senza arresto"]["clienti"])}, e al mese 30 restano {eur(S["Avverso con arresto"]["c30"])} euro invece di {eur(S["Avverso senza arresto"]["c30"])}.</p>
  <h3>Che cosa chiediamo ai laboratori per contratto</h3>
  <p>Non serve comprare oggi la redazione dei contratti. Serve sapere che cosa chiedere, perché il valore dell'azienda non resti presso il fornitore: proprietà della formula e dei dati di sviluppo; accesso ai metodi analitici e ai risultati; un pacchetto di trasferimento che permetta di produrre altrove; condizioni di fornitura (minimi d'ordine, tempi, acconti, prezzi, capacità di riassortimento); costi di uscita; responsabilità sui lotti non conformi; riservatezza.</p>
</section>"""

def cap12():
    righe = [
        ("Il cliente compra la speranza di ricrescita", "1 e 4", "Le interviste lo dicono; poi i rimborsi delle prime coorti", "Regola delle interviste; offerta riscritta; oltre il 20% di rimborsi la garanzia si ridisegna o si sospende"),
        ("Il CAC supera il massimo sostenibile", "4", "Prime due tranche di pubblicità", "Verifica del mese 20: si rivede l'offerta o ci si ferma. Si valuta la cessione o la licenza del prodotto invece di insistere"),
        ("Pochi scelgono il percorso da sei", "4", "Mix delle prime coorti", "La cassa regge anche al 15% (capitolo 10); cambia il CAC massimo, che si ricalcola"),
        ("La tollerabilità va male", "2", "Patch test e uso ripetuto", "La formula contiene solventi e sostanze che favoriscono la penetrazione: il dossier ha già l'ordine delle modifiche. Costa un ciclo, è lo scenario Ritardo"),
        ("Parere brevettuale sfavorevole sulla C", "1", "Mese 2", "Architettura B, già calcolata. Costa tempo"),
        ("Il laboratorio quota molto più del previsto", "1-2", "Preventivi", "I metodi analitici possono raddoppiare. Preventivi per fasi e come pacchetto sviluppo più produzione"),
        ("Contestazione dei claim o dell'Academy", "3-4", "Segnalazioni, azioni di concorrenti", "In Italia l'Antitrust, in Germania i concorrenti possono agire direttamente. Parere legale prima del primo contenuto; versione tedesca verificata sul posto"),
        ("Ingiallimento su capelli chiari o grigi", "2", "Prova di colore", "Due estratti colorati in formula. Prova da 500 euro nel mese 7, perché colpirebbe il pubblico con più capacità di spesa"),
        ("Un grande gruppo occupa lo stesso spazio", "tutte", "—", "Ha tutti i mezzi per farlo. La difesa è arrivare prima e costruire una relazione con i clienti, non la formula"),
        ("Il primo lotto resta invenduto", "4", "Vendite dei primi mesi", "La perdita massima è il costo del lotto, circa 25.500 euro più IVA"),
        ("Il tempo dei fondatori", "tutte", "Sempre", "Non ricevono compensi e hanno altre attività. Abbonamenti e garanzia creano obblighi verso i clienti che non si sospendono: processi di assistenza scritti prima del lancio"),
    ]
    body = "".join(f"<tr><td><b>{a}</b></td><td class=\"c\">{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in righe)
    return f"""
<section>
  <h2><span class="num">12</span>I rischi</h2>
  <p class="lead">In ordine di quanto possono fermare il progetto, non di quanto sono probabili.</p>
  <table class="small">
    <thead><tr><th style="width:42mm">Rischio</th><th class="c" style="width:12mm">Tappa</th><th style="width:36mm">Come si vede</th><th>Che cosa facciamo</th></tr></thead>
    <tbody>{body}</tbody>
  </table>
</section>"""

def cap13():
    S = N["scenari"]["Base"]
    post = 250000 / 0.18; pre = post - 250000
    rec = S["c30"] - S["minimo"]
    return f"""
<section>
  <h2><span class="num">13</span>Ritorno e valutazione</h2>
  <p class="lead">Tre cose diverse che spesso si confondono: il pareggio operativo, il recupero del capitale investito, il ritorno per l'azionista.</p>
  <h3>Pareggio operativo</h3>
  <p>Nello scenario base il risultato operativo del mese, cioè contribuzione meno rimborsi, pubblicità e costi fissi, diventa positivo al mese 17 e resta fra 1.300 e 5.200 euro al mese fino al mese 30. È un pareggio facile, e va letto con cautela: i costi fissi sono di circa 700 euro al mese perché i fondatori non sono pagati e l'operatività si regge su strumenti di intelligenza artificiale, due abbonamenti (Fable 5.1 e ASTRA di OpenAI) per 100 euro al mese. Dice poco su un'azienda con personale.</p>
  <h3>Recupero del capitale</h3>
  <p>Dal lancio al mese 30 la cassa dello scenario base sale di {eur(rec)} euro. A quel ritmo, recuperare i {eur(S["assorbito"])} euro assorbiti prima del lancio richiederebbe quasi altri tre anni. Solo la crescita cambia questo numero: più clienti a un costo sostenibile, più riacquisto, un secondo mercato.</p>
  <h3>Ritorno per l'azionista</h3>
  <table class="tight">
    <thead><tr><th>Passaggio</th><th class="n">Valore</th></tr></thead>
    <tbody>
      <tr><td>Investimento</td><td class="n">250.000 €</td></tr>
      <tr><td>Quota ipotizzata, da negoziare</td><td class="n">18%</td></tr>
      <tr><td>Valutazione implicita dopo l'investimento</td><td class="n">{eur(post)} €</td></tr>
      <tr><td>Valutazione implicita prima dell'investimento</td><td class="n">{eur(pre)} €</td></tr>
      <tr><td>Se la raccolta successiva porta la quota al 12%, il nuovo investitore acquista</td><td class="n">un terzo</td></tr>
      <tr><td>con 500.000 € raccolti: valutazione prima del round</td><td class="n">1.000.000 €</td></tr>
      <tr><td>con 1.000.000 € raccolti: valutazione prima del round</td><td class="n">2.000.000 €</td></tr>
      <tr><td>Uscita con 8 milioni distribuibili, al 12%</td><td class="n">960.000 € · 3,84×</td></tr>
      <tr><td>Uscita con 15 milioni distribuibili, al 12%</td><td class="n">1.800.000 € · 7,2×</td></tr>
    </tbody>
    <caption>Aritmetica della proposta, non valutazione di mercato. Con 500.000 euro raccolti la valutazione del secondo round sarebbe inferiore a quella implicita nel primo. Un piano di quote per collaboratori, per esempio del 10%, diluirebbe tutti in proporzione: il 18% diventerebbe 16,2%. Tempi, diluizioni e termini contrattuali cambiano i multipli. <span class="tag">ipotesi</span></caption>
  </table>
  <p>Il fatturato da solo non determina il valore di un marchio. Contano crescita, margini, dipendenza dai fondatori, distribuzione e qualità dei ricavi. Come termine di riferimento, e non come multiplo applicabile: e.l.f. Beauty ha acquistato rhode con 800 milioni di dollari alla chiusura, circa 3,8 volte i 212 milioni di ricavi dei dodici mesi precedenti, più un premio legato alla crescita. È un caso di scala e caratteristiche diverse; serve solo a escludere regole assolute in un senso o nell'altro.</p>
  <p>Un marchio di nicchia profittevole è un buon investimento per un business angel o per chi è specializzato in beni di consumo. Per un fondo che cerca ritorni molto elevati probabilmente non lo è, a meno che le verifiche della tappa 4 non mostrino riacquisto e costo di acquisizione tali da giustificare l'espansione in altri paesi.</p>
</section>"""

def cap14():
    return """
<section>
  <h2><span class="num">14</span>Squadra, proprietà, contratti</h2>
  <p class="lead">Un investitore vuole sapere chi fa che cosa, quanto tempo ci mette, come si sostiene e che cosa appartiene alla società.</p>
  <h3>Chi lavora al progetto</h3>
  <p>I fondatori non ricevono compensi dalla società per tutta la durata del piano: hanno altre entrate, esterne alla società e alla raccolta. Il loro costo aziendale è zero, e questo spiega perché i costi fissi siano così bassi. Il rischio si sposta dal denaro al tempo, ed è nella tabella dei rischi. La scheda della squadra, con ruoli, tempo dedicato, competenze già dimostrate e capacità mancanti, è in un allegato separato in preparazione. Deve coprire sei responsabilità: prodotto e qualità, fornitori e produzione, finanza e modello, acquisizione dei clienti, servizio clienti, regolatorio.</p>
  <h3>Come si lavora</h3>
  <p>La società nasce per lavorare con strumenti di intelligenza artificiale: due abbonamenti, Fable 5.1 e ASTRA di OpenAI, per circa 100 euro al mese. Pareri legali e brevettuali vengono preparati con questi strumenti e confermati da un professionista senior, che firma. Sito, grafica, fotografie e confezione si fanno in casa; restano da pagare i costi fisici. Ogni voce professionale si affida dopo aver chiesto più preventivi sullo stesso perimetro.</p>
  <h3>Che cosa appartiene alla società</h3>
  <p>Marchio, dominio, dossier tecnico, diritti sulla formula, dati degli studi e dati dei clienti sono conferiti alla società alla costituzione, prima dell'ingresso dell'investitore. Nei contratti con i laboratori valgono i requisiti elencati nel capitolo 11.</p>
  <h3>Governo e informazione</h3>
  <p>La quota offerta, i diritti dell'investitore e il governo delle decisioni sono materia di trattativa. Ci impegniamo fin d'ora a una cosa: il modello di cassa allegato viene aggiornato ogni mese con i dati reali e condiviso con l'investitore, insieme all'esito di ogni verifica.</p>
</section>"""

def cap15():
    return """
<section>
  <h2><span class="num">15</span>I primi novanta giorni</h2>
  <p class="lead">La prima tappa costa 12.500 euro e produce le tre risposte che decidono se spendere i 41.500 della seconda.</p>
  <ol>
    <li><b>Società e patti.</b> Costituzione, conferimento di marchio, dominio e dossier, patti parasociali, documenti dell'investimento.</li>
    <li><b>Parere brevettuale sulla formula C.</b> La domanda va posta così: la configurazione C ricade nelle rivendicazioni della famiglia individuata, e se sì quali alternative ne restano fuori? Arrivando con il fascicolo pronto il consulente fattura meno ore.</li>
    <li><b>Capitolato ai laboratori, identico per tutti.</b> Con le voci che servono a evitare sorprese: colore degli estratti su capelli bianchi, grigi e biondi; residuo su capello lungo lavato ogni tre giorni; prove di erogazione su capelli lunghi; dose definita per superficie; massimo d'uso in millilitri al giorno.</li>
    <li><b>Preventivi confrontabili.</b> Tre laboratori, stessa forma, per fasi e come pacchetto sviluppo più produzione. Sulle prove cliniche il preventivo più basso fa quasi sempre meno: venti persone invece di quaranta, nessuna supervisione dermatologica.</li>
    <li><b>Sedici interviste</b>, con il protocollo e la regola del capitolo 03. Il risultato è una pagina con le obiezioni principali e una decisione: quale offerta portare avanti.</li>
    <li><b>Mappa competitiva verificata</b> sulle dieci alternative prioritarie, con codice della confezione, prezzo ordinario e promozionale, dose con fonte e data.</li>
    <li><b>Estrazione Istat</b> della popolazione per età e sesso al 1° gennaio 2026, conservata con data, per chiudere il capitolo 05.</li>
    <li><b>Modello di cassa</b> aggiornato con i preventivi ricevuti.</li>
  </ol>
  <div class="key"><span class="label">Per passare alla tappa 2</span>
    <p>La formula C è percorribile secondo il parere, almeno due laboratori hanno quotato le fasi di sviluppo entro 45.000 euro, e almeno una delle due offerte supera la regola delle interviste. Se manca una delle tre, si rivede il piano prima di spendere.</p>
  </div>
</section>"""
