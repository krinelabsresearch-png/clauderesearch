# 208 · OMBRA: la "TAC" di un impianto fotovoltaico

*Scheda del 14/10/2026. Si basa su due ricerche complete:*
- *[dossier/208-tecnologia.md](dossier/208-tecnologia.md), 30 ricerche web;*
- *[dossier/208-clienti.md](dossier/208-clienti.md), 35 ricerche web.*

*Le cifre segnate "stima" sono calcoli, non dati di fonte.*

**Punteggio con la scheda v2:**
- **3,80** con la tua motivazione stimata a 5;
- 3,40 con la motivazione neutra (3).

Entra in lista se la tua motivazione è almeno 4: con 4 il punteggio è 3,60.

---

## 1. In cosa consiste esattamente

**L'analogia.** Una TAC ricostruisce l'interno del corpo da tante radiografie prese da angoli diversi. OMBRA fa lo stesso con il cielo che i pannelli vedono davvero. Ogni 5–15 minuti il sole è un "raggio" che arriva da un punto diverso del cielo. Se in quell'istante il cielo è sereno e l'impianto produce meno di quanto prevede la fisica, tra il sole e i pannelli c'è qualcosa. Ripetendo il confronto su migliaia di istanti si ottiene una **mappa d'ombra**: da quale porzione di cielo l'impianto è oscurato, quanto, e quanti euro costa.

**Come funziona, in cinque passi**
1. **Dati in ingresso.**
   - Produzione dell'inverter ogni 5–15 minuti, presa dal cloud del produttore (Huawei, SolarEdge, Fronius, SMA, Enphase…) o da un file esportato. Quando ci sono, anche tensione e corrente per stringa.
   - Il sole che è arrivato davvero su quel tetto, misurato dai satelliti: CAMS di Copernicus, gratuito, con la luce diretta separata da quella diffusa.
   - Meteo: temperatura, pioggia, neve.
2. **Pulizia dei dati.** Corregge buchi, ora legale sbagliata, potenza installata o orientamento dichiarati male (li stima dai dati stessi) e sceglie i momenti di cielo sereno.
3. **Modello fisico.** Calcola con pvlib, una libreria open source, cosa dovrebbe produrre l'impianto senza ostacoli.
4. **Problema inverso.** Dallo scarto tra produzione attesa e reale ricostruisce le cause:
   - la mappa d'ombra, con un'ottimizzazione convessa che "sa" che gli ostacoli sono macchie contigue nel cielo;
   - una statistica bayesiana che dà a ogni causa una probabilità e un intervallo in euro.

   Un controllo gratuito di coerenza: il sole ripassa nello stesso punto del cielo due volte l'anno, in date simmetriche rispetto al solstizio. Un ostacolo vero ricompare; una nuvola no.
5. **Uscite.**
   - Una "cascata" delle perdite in kWh e in euro, divisa per causa.
   - La mappa d'ombra sovrapposta alla vista aerea.
   - Un ticket per l'installatore con prove e priorità in euro all'anno.
   - Un report in linguaggio semplice per il proprietario, scritto da un LLM ma ancorato solo ai numeri calcolati.

**Cosa riconosce e quanto è affidabile**

| Causa | Affidabilità | Note |
|---|---|---|
| Ombra per ora e stagione (alberi, edifici, comignoli) | alta | Serve la produzione a 15 minuti o meglio |
| Stringa spenta (fusibile, connettore) | molto alta | Perdita del 33–50% se l'inverter ha 2–3 stringhe |
| Inverter fermo o senza comunicazione | molto alta | Circa 2,3% dell'energia annua in media (dato NREL) |
| Distacchi per tensione di rete alta (norma CEI 0-21, soglia 253 V) | alta | Frequenti sulle linee deboli |
| Clipping (inverter sottodimensionato) | molto alta | Spesso è una scelta voluta, non un guasto |
| Neve | alta dove nevica | |
| Ora o orientamento sbagliati nei dati | alta | Non sono perdite, ma vanno corretti per non "inventare" ombre |
| Limitazione d'immissione impostata male | alta | Serve il contatore |
| Batteria configurata male | media | 50–300 €/anno (stima) |
| Diodo di bypass guasto, MPPT bloccato | media | Serve la tensione per stringa |
| Sporcamento | media, bassa sotto il 2% | Media europea 0,9–5,3%/anno |
| Degrado | media | Servono almeno 2 anni di dati |
| PID, mismatch, moduli sotto targa | bassa | Si confondono con l'errore del satellite |
| Hot spot, microcricche | non diagnosticabili | Servono termografia o elettroluminescenza |

**Limite principale.** Sul singolo sito il satellite sbaglia l'irradianza oraria di circa il 15% (la luce diretta di circa il 31%). Per questo:
- le perdite **con una forma riconoscibile** (ombra, fermi, stringhe, clipping, distacchi) si diagnosticano bene;
- quelle **uniformi** (sporco leggero, degrado) richiedono il confronto con gli impianti vicini oppure 2 anni di dati.

**Quanti impianti si diagnosticano bene (stima, su un parco italiano misto con storico disponibile):**
- mappa d'ombra affidabile nel 60–75% degli impianti;
- perdite con una firma riconoscibile stimate in euro con un margine di ±20–30%.

**Quanto storico serve**
- Molti portali conservano anni di dati, quindi importandoli la diagnosi arriva al giorno zero.
- Senza storico la mappa completa richiede 6–12 mesi, perché il sole deve percorrere tutta la sua fascia di cielo.

---

## 2. Tutti i possibili clienti

**Il dato chiave.** In Italia ci sono 2,09 milioni di impianti (43,5 GW, fine 2025). Il 52% della potenza è stato installato tra il 2007 e il 2014, cioè nell'era del **Conto Energia**.
- Alla chiusura gli impianti incentivati erano 531.242, per 18,2 GW.
- Ricevono ancora 0,25–0,45 € di premio per ogni kWh, più il valore dell'energia, fino al 2026–2033.
- **L'1% di produzione persa sull'intero parco Conto Energia vale circa 80 M€ l'anno (stima).**
- Secondo dati GSE riportati da SolareB2B, quel parco produce in media il 75% del previsto e il GSE ha già mandato circa 13.000 lettere di "alerting" agli impianti che rendono poco.

| # | Cliente | Problema | Cosa compra | Quanti | Prezzo realistico | Attrattività per te |
|---|---|---|---|---|---|---|
| 1 | **Impianti Conto Energia da 100 kWp a 1 MWp** (PMI, aziende agricole, piccole società veicolo, family office) | Ogni kWh perso vale 0,35–0,55 €; inverter vecchi; garanzie scadute; grandine; dal 2028 devono decidere se fare revamping o uscire dall'incentivo | TAC una tantum, poi monitoraggio; business case "manutenere, rifare o uscire" | ~20–25 mila impianti, ~10–12 GW | TAC 490–2.500 €; 1,5–3 €/kWp l'anno | **4,5/5** |
| 2 | **Aziende di manutenzione (O&M) e gestori di portafogli** | Margini bassi, troppi allarmi, poco personale | Smistamento automatico dei guasti, ticket, report per i proprietari | Qualche centinaio in Italia | 0,3–1 €/kWp l'anno, con il loro marchio | **4/5** |
| 3 | **Compravendita di impianti incentivati e fondi** | Rischio tecnico nascosto (gli impianti si comprano a circa 3 M€/MW) | Due diligence fatta a distanza, solo dai dati | Centinaia di operazioni l'anno (stima) | 1–3 k€/MW | **3,5/5** |
| 4 | **Installatori** (canale verso residenziale e piccolo C&I) | Il mercato residenziale è sceso del 28% nel 2025; cercano ricavi ricorrenti; ogni uscita tecnica costa 150–250 € | Diagnosi remota, priorità, contatti di vendita per batterie, pulizia, potature, revamping | Migliaia di imprese, ~2 milioni di impianti | 1–1,5 € per impianto al mese, minimo 79 €/mese | **3,5/5** |
| 5 | **Impianti esteri ad alta tariffa** (Germania EEG 2009–12, Francia 2006–11) | Come il Conto Energia, ma più frammentati | Controllo dello stato di salute, monitoraggio | ~1 milione in DE, ~0,3 milioni in FR (stima da verificare) | 30–80 € l'anno residenziale; 1–2 €/kWp l'anno | **3/5** |
| 6 | **Capannoni e aziende con impianti recenti** (dopo il 2014) | Nessuno guarda i dati | Allarmi in euro, report mensile | ~100 mila in Italia | 300–1.200 € l'anno | **3/5** |
| 7 | **Assicurazioni** | Grandine 2023; danni invisibili alle celle; frodi | Verifica oggettiva del danno (produzione rispetto al sole), antifrode, valutazione del rischio | Decine | 50–150 € per sinistro | **2,5/5** |
| 8 | **Utility e venditori di impianti** (Enel X, Edison, Sorgenia, Enpal, Otovo, 1KOMMA5°) | Costo dell'assistenza; nel noleggio (Enpal) il rischio di sottoproduzione è loro | Versione con il loro marchio, API di diagnosi | Pochi grandi; Enpal ha oltre 115 mila famiglie | 0,3–1 € per impianto al mese | **2,5/5 all'inizio, 4/5 in seguito** |
| 9 | **Comunità energetiche (CER)** | Massimizzare l'energia condivisa incentivata | Report ai membri | Da verificare | 100–300 € per impianto l'anno | 2/5 |
| 10 | **Portali immobiliari e periti** | Valutare l'impianto in una compravendita | "Certificato di salute" | Decine di migliaia di compravendite l'anno (stima) | 49–149 € | 2/5 |
| 11 | **Famiglie, direttamente** | "Il mio impianto funziona?" | App o report | ~2 milioni in Italia | 2–5 €/mese | **1/5**: recuperano 40–100 € l'anno e acquisirle costa quanto valgono |
| 12 | Banche, produttori di pannelli e inverter, enti pubblici, agrivoltaico | — | — | — | — | 1/5: non pagano, hanno già i dati o comprano con gare lente |
| 13 | Verifica degli incentivi fiscali | — | — | — | — | **escluso**: il cuore è burocratico |

---

## 3. Tutti i possibili vantaggi, per tipo di cliente

**Proprietari di impianti in Conto Energia** (stime calcolate dalle tariffe)
- **Recupero di produzione**, cioè il 3–5% di perdite evitabili all'anno:

  | Impianto | Recupero annuo |
  |---|---|
  | 200 kWp del IV Conto | 3–5 k€ |
  | 1 MW a terra del II Conto, al Sud | 19–31 k€ |

- **Business case per la scelta 2026–2028.** Il Decreto Bollette 2026 (DL 21/2026, da verificare sul testo) permette dal 2028 l'uscita anticipata dall'incentivo, ma solo rifacendo l'impianto. Servono dati per decidere se manutenere, rifare o uscire.
- **Prove per i reclami in garanzia** (degrado oltre la curva garantita) e per i sinistri da grandine.
- **Valore dell'impianto se lo vendi:** ogni 1% di produzione recuperabile vale circa 30 k€ per MW di prezzo.

**Aziende di manutenzione e gestori di portafogli**
- Meno uscite tecniche inutili.
- Priorità dei guasti in euro invece di centinaia di allarmi uguali.
- Report automatici ai proprietari.
- Contratti meglio difendibili.

**Installatori** (esempio con 1.500 impianti, stima)
- Il triage remoto evita il 25–35% delle uscite tecniche: 6–13 k€ l'anno risparmiati.
- Vendite aggiuntive con un argomento in euro. Per esempio: "quell'albero ti costa 180 € l'anno". L'1% di batterie aggiunte a impianti esistenti vale circa 22 k€ di margine; in Italia circa 1,2 milioni di impianti non hanno ancora una batteria.
- Contratti di manutenzione ricorrenti: circa 11 k€ l'anno.
- **Valore totale: 40–55 k€ l'anno, contro 15–25 k€ di costo di OMBRA.**

**Fondi e acquirenti di impianti**
- Una due diligence che trova un 5% di perdite evitabili vale circa 150 k€/MW di prezzo negoziato.

**Assicurazioni**
- kWh persi misurati in modo oggettivo dopo grandine o tempesta.
- Frodi scoperte: danno dichiarato senza calo di produzione.
- Valutazione del rischio prima di assicurare.

**Utility e venditori a noleggio**
- Meno interventi di assistenza.
- Il rispetto delle garanzie di produzione nei contratti di noleggio.
- Un report mensile "in euro" che fidelizza il cliente.

**Vantaggi indiretti per te**
- Il test produrrebbe **il primo dato italiano** su quanti impianti rendono meno del dovuto: un contenuto forte per stampa di settore e marketing.
- Un'uscita possibile: la vendita a un operatore di monitoraggio. Solytic, che è il concorrente più vicino, è stata comprata da un gruppo del settore.

---

## 4. Concorrenti

**Chi fa monitoraggio**

| Concorrente | Cosa fa | Prezzo |
|---|---|---|
| Solytic | Monitoraggio multi-marca, circa 200 mila impianti, poi acquisita | 5 €/impianto al mese |
| Solar-Log | Monitoraggio, soprattutto in Germania, Austria e Svizzera | — |
| meteocontrol VCOM | Monitoraggio professionale | — |
| Portali dei produttori (Huawei, SolarEdge, Enphase) | Monitoraggio gratuito, ciascuno solo per la propria marca | Gratis |
| GSE | Alerting gratuito agli impianti incentivati: segnala, ma non spiega la causa né i soldi persi | Gratis |

**Chi fa analisi delle perdite, ma per grandi impianti**
- 3E SynaptiQ, Power Factors, SmartHelio.
- Raycatch, specializzata in diagnosi solo da dati, è stata venduta nel 2022 per circa 1,5 M$: per quei grandi impianti la monetizzazione è stata difficile.

**Il vuoto.** Nessuno, per impianti di marche diverse residenziali o piccolo C&I, ricostruisce l'ombra dai soli dati più il satellite e divide le perdite per causa **in euro, con la tariffa reale dell'impianto** (Conto Energia, CER, autoconsumo).

**Cosa ti difende.** Non l'algoritmo: è replicabile con strumenti open source, e negli USA il concetto è brevettato da Locus Energy (US 10,962,576, senza estensione europea trovata). Ti difendono:
- la libreria di tariffe e regole italiane;
- i dati di flotta calibrati e le verifiche sul campo etichettate;
- la distribuzione tramite manutentori e installatori.

---

## 5. Accesso ai dati (il punto critico)

**Condizioni dei principali produttori**

| Produttore | Come si accede | Limiti e costi |
|---|---|---|
| Huawei | L'installatore o il proprietario crea un account in sola lettura | Limiti di chiamate molto stretti |
| SolarEdge | Chiave API | 300 chiamate al giorno; dati a 15 minuti |
| Fronius | API a pagamento | 52–494 € al mese |
| SMA | Serve un ticket | — |
| Enphase | Dati per singolo pannello, i migliori | 1.000 chiamate al mese gratis |

- **Lo storico costa poche chiamate.** Basta per la diagnosi iniziale: un anno a 15 minuti su SolarEdge richiede circa 12 chiamate.
- **Data Act UE** (applicabile dal 12/9/2025):
  - gli articoli 4–5 danno al proprietario il diritto di far consegnare i dati del suo inverter a un terzo scelto da lui, come OMBRA;
  - non impongono però un'API standard;
  - non ho trovato produttori con un portale dedicato.

  Serve come leva e come canale di riserva. La via pratica resta l'account aperto dall'installatore o il file esportato.
- **Impianti vecchi del Conto Energia:** spesso hanno datalogger morti o inverter di marche scomparse. Alternative: dati mensili, letture del contatore, oppure un logger economico tramite un partner.

---

## 6. Conti

**Listino proposto (stima)**
- TAC Conto Energia: 490 € sotto 100 kWp, 990 € tra 100 e 500 kWp, 1.900–2.500 € sopra 500 kWp.
- Monitoraggio: 1,5–3 €/kWp l'anno.
- Due diligence: 1–3 k€/MW.
- Commissione del 2–5% sui lavori di revamping che segnali.

**Scenario Conto Energia (solo Italia)**

| Voce | Calcolo | Ricavo |
|---|---|---|
| Monitoraggio | 500 impianti × 350 kWp × 2 €/kWp (175 MW, circa 1% del parco Conto Energia) | 350 k€ |
| TAC e due diligence | 120 × 1,5 k€ | 180 k€ |
| Commissioni sul revamping | — | 30 k€ |
| **Totale** | | **circa 560 k€ l'anno**, con 150–300 clienti |

Per 1 M€ servono circa 900 impianti più report, oppure si aggiungono installatori, Germania e Francia. Attenzione: il segmento Conto Energia si esaurisce verso il 2031–2033, quindi entro allora va convertito in clienti fuori incentivo.

**Margine:** software puro, 80–90% lordo; i dati satellitari sono gratuiti.

**Costo dell'MVP:** sotto i 5 k€ in 6 mesi, escluso il tuo tempo.

---

## 7. Cosa offre in più di ChatGPT da 20 $ al mese

Davanti a un grafico ChatGPT può dire "forse è un'ombra". Non ha però:
- i dati del tuo inverter ogni 15 minuti per anni;
- il sole reale sopra il tuo tetto misurato dal satellite;
- il modello fisico e il problema inverso risolto con un'incertezza calcolata;
- la tariffa reale del tuo impianto per dare il valore in euro;
- i ticket automatici all'installatore.

E soprattutto non confronta il tuo impianto con mille impianti vicini.

---

## 8. Primo test: sotto i 10 k€, 8–12 settimane

1. **Versione su file esportati (settimane 1–6).** Funziona con i file CSV dei portali, senza API: pvlib più CAMS, mappa d'ombra, cascata delle perdite in euro, report PDF.
2. **Due canali in parallelo.**
   - **Conto Energia:** dalla mappa pubblica del GSE (Atlaimpianti) si scelgono 1.000 impianti da 100 kWp a 1 MWp in 2–3 regioni e se ne contattano 300 aziende con l'offerta "TAC gratuita: quanti euro perdi e perché".
   - **Installatori e manutentori:** 3–5 aziende con flotte da 100–1.000 impianti, a cui si chiedono 200–300 impianti con almeno 12 mesi di storico.
3. **Verifica sul campo** di 40–60 impianti: foto panoramica dal tetto, Google Earth, drone o sopralluogo pagati 100–150 € a sito.

**Soglie per andare avanti (GO) o fermarsi (STOP)**

| Metrica | GO | STOP |
|---|---|---|
| Ticket confermati sul campo | ≥75% | <60% |
| Errore sulla direzione dell'ostacolo | ≤10–15° | >25° |
| Impianti con un problema risolvibile da almeno 100 € l'anno | ≥15–20% | <8% |
| TAC pagate su 300 contatti Conto Energia | ≥10 | <5 |
| Installatori che vogliono continuare pagando | ≥3 su 5 | ≤1 su 5 |

---

## 9. Rischi principali

1. **Accesso ai dati:** API chiuse o costose; possibili restrizioni UE sugli inverter cinesi (la Lituania limita già l'accesso remoto).
2. **I produttori lo integrano gratis nei loro portali.** Funzionerebbe però su una sola marca e senza il valore in euro con la tariffa reale.
3. **Precisione:** se le diagnosi confermate scendono sotto il 60%, installatori e manutentori smettono di fidarsi.
4. **Perdite non risolvibili:** l'albero del vicino non si abbatte. Il valore deve venire da guasti, fermi e decisioni di revamping, non solo dall'ombra.
5. **Il segmento Conto Energia ha una scadenza** (2031–2033): è una finestra di 5–7 anni.
6. **Responsabilità** per diagnosi sbagliate: servono report "consultivi" con probabilità, limiti contrattuali e un'assicurazione.
7. **Brevetti negli USA** (Locus Energy, probabilmente SMA): l'Europa sembra libera, ma va fatta una verifica prima di entrare in America.

---

## 10. Punteggio (scheda v2)

| Voce | Voto | Perché |
|---|---|---|
| Motivazione | 5 (da confermare) | Problema inverso, ottimizzazione e statistica bayesiana: il tuo mestiere |
| Vantaggio | 4 | Matematica e AI sono il cuore; ti mancano esperienza nel fotovoltaico e una rete di installatori |
| Dolore | 3 | Alto (4) per il Conto Energia, dove ogni kWh vale 0,35–0,55 €; basso (2) per famiglie e installatori |
| Mercato | 4 | 2,09 milioni di impianti in Italia, 18 GW in Conto Energia, oltre 15 milioni di tetti nell'UE |
| Margine | 4 | Software puro; dati satellitari gratuiti |
| Validabilità | 4 | Test sotto i 10 k€ in 8–12 settimane con soglie chiare |
| 300–500 k€ da solo | 3 | Plausibili con 150–300 clienti Conto Energia; 1 M€ richiede un canale o un secondo Paese |
| Automazione | 3 | Analisi e report automatici; restano l'attivazione dei dati, gli impianti vecchi e le contestazioni |
| Difendibilità | 3 | Algoritmo replicabile; il vantaggio sta nei dati di flotta, nelle verifiche etichettate e nella distribuzione |
| **Totale** | **3,80** | Motivazione neutra 3,40 |

**Verdetto.** È la prima idea del giro "WOW" che, dopo la ricerca completa, **supera 3,5**. Due condizioni:
- che la tua motivazione sia almeno 4;
- che si parta dal **Conto Energia**, non dalle famiglie.

Il cuore matematico è tuo. Il rischio vero è l'accesso ai dati e la precisione sul campo, e il test sotto i 10 k€ li misura entrambi.
