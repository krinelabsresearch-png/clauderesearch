# 208 — OMBRA: tecnologia, precisione, dati, architettura, test

> Rapporto di ricerca del 14/10/2026 (agente di ricerca, verificato a campione da Claude). Le voci [NV] non sono verificate con una fonte; "stima" indica un calcolo.

# OMBRA (idea 208): la "TAC" di un impianto fotovoltaico
## Fattibilità tecnica, accuratezza, accesso ai dati, architettura, piano di sviluppo e test

*Ricerca del 14 ottobre 2026, fatta con 30 ricerche web (WebFetch non funzionava). Le cifre con fonte sono collegate al link. Quelle marcate **[stima]** sono mie elaborazioni, oppure vengono da letteratura nota che in questa sessione non ho potuto verificare. Vanno controllate prima di usarle in pubblico.*

---

## 0. In breve

- **Fisicamente si può fare.** Esistono già i pezzi open source: pvlib per il modello fisico, pvanalytics, RdTools e solar-data-tools/SCSF per pulizia dati, clipping, giorni sereni, degrado e sporcamento. C'è anche letteratura che usa irradianza da satellite al posto del sensore sul posto: lo studio europeo PVSAT-2 del 2007 su 100 impianti fino a 5 kW. L'idea di fondo, cioè raggruppare i dati per posizione del sole e dedurre l'ombra dal deficit di produzione, **è già brevettata negli USA** da Locus Energy (US 10,962,576).
- **Il problema principale non è l'algoritmo ma l'accesso ai dati.** Le API dei produttori sono frammentate e spesso le apre solo l'installatore. Huawei ha limiti di chiamate molto stretti, SolarEdge 300 chiamate al giorno, Fronius e SMA si pagano. Il Data Act UE dà un diritto legale di accesso, ma non impone un'API standard e non ho trovato produttori di inverter che lo abbiano già implementato con un portale dedicato.
- **Secondo limite: l'errore del satellite sul singolo sito.** CAMS in Europa sbaglia l'irradianza globale oraria di circa il 15% (RMSE relativo) e quella diretta di circa il 31%. Di conseguenza le perdite con una **forma riconoscibile** si diagnosticano bene: ombra legata alla posizione del sole, clipping, fermi, stringhe spente, neve, distacchi. Le perdite **uniformi** (sporcamento leggero, degrado nel primo anno, pannelli che rendono meno di targa) restano confuse con l'errore del satellite, a meno di avere un riferimento di flotta o almeno 2 anni di dati.
- **Molti impianti hanno già anni di storico nei portali**, quindi una diagnosi immediata è possibile scaricandolo. Senza storico, una mappa d'ombra completa richiede almeno 6 mesi: il sole percorre tutta la sua fascia di cielo tra un solstizio e l'altro.
- **Test più economico:** versione con caricamento CSV, 200–300 impianti di 3–5 installatori italiani, verifica sul campo di 40–60 impianti. Costo 3–8 k€, durata 8–10 settimane.

---

## 1. Come funziona, passo per passo

### 1.1 L'analogia
Una TAC ricostruisce l'interno del corpo da tante radiografie prese da angoli diversi. OMBRA ricostruisce invece **la porzione di cielo che i pannelli vedono davvero**. Ogni 5–15 minuti il sole è un "raggio" che arriva da un punto diverso del cielo, definito da azimut ed elevazione. Se in quell'istante il cielo è sereno e l'impianto produce meno di quanto la fisica prevede, c'è un ostacolo tra il sole e i pannelli. Ripetendo il confronto su migliaia di istanti e posizioni del sole si ottiene una "maschera d'ombra" (horizon/shading mask): una mappa che dice da quale porzione di cielo l'impianto è ombreggiato e quanto, e quanto costa in euro.

### 1.2 Pipeline

**Passo 1. Dati in ingresso**
- **Dati dell'impianto:** potenza AC ed energia ogni 5–15 minuti, e dove disponibili tensione e corrente per MPPT o stringa, dati per singolo modulo (Enphase, ottimizzatori), codici di allarme, stato della batteria.
- **Metadati:** posizione, kWp, inclinazione e orientamento dichiarati, modello di inverter e moduli. Spesso sono sbagliati, quindi vanno anche *stimati* dai dati.
- **Meteo:** irradianza da satellite (CAMS all-sky più il modello di cielo sereno McClear, LSA SAF, Solcast), temperatura, vento, pioggia e neve (ERA5 o Open-Meteo).

**Passo 2. Pulizia e controllo qualità.** Si individuano buchi nei dati, sfasamenti di orario (ora legale), cambi di potenza installata e clipping, e si selezionano gli intervalli di cielo sereno. Gli strumenti esistono già:
- [pvanalytics](https://pvanalytics.readthedocs.io/en/stable/generated/gallery/index.html) ha moduli per clipping, cielo sereno, orientamento e stima di inclinazione e azimut con il metodo PVWatts. La sua funzione `shading.fixed` rileva ombre fisse (pali, fili) ma lavora su dati di irradianza globale a circa 1 minuto e richiede almeno 60 giorni ([doc](https://pvanalytics.readthedocs.io/en/latest/generated/pvanalytics.features.shading.fixed.html)).
- SCSF / solar-data-tools ([Meyers et al., arXiv 1907.08279](https://arxiv.org/pdf/1907.08279)) stima il profilo di cielo sereno **dalla sola potenza**, senza meteo né metadati.
- Un altro lavoro ([arXiv 1706.06878](https://arxiv.org/pdf/1706.06878)) identifica l'orientamento dell'impianto dopo aver selezionato i periodi sereni, usando McClear come riferimento.

**Passo 3. Modello fisico "diretto" con pvlib.** Si calcola cosa *dovrebbe* produrre l'impianto senza ostacoli:
- separazione dell'irradianza globale in **diretta** (raggio del sole) e **diffusa** (cielo). CAMS fornisce già le due componenti; altrimenti si usano modelli di decomposizione;
- proiezione sul piano dei moduli (modelli Perez o Hay-Davies), perdite per angolo di incidenza, temperatura di cella, curva di efficienza dell'inverter e limite di potenza AC (che produce il clipping).

**Passo 4. Problema inverso.** Si confronta il misurato con l'atteso. In forma semplificata:

`P_misurata(t) ≈ k_sito · [ B(t)·s(az_t, el_t)·cosθ_t·IAM + D(t)·F_cielo + R(t) ] · (1 − sporco(t)) · (1 − d·anni) − eventi(t) + rumore`

Incognite:
- `s(az, el)` ∈ [0,1]: trasparenza della cella di cielo in cui si trova il sole. Con celle da 1–2° le celle effettivamente visitate sono circa 2.000–4.000. Vale 0 se c'è un ostacolo opaco, valori intermedi per un albero;
- `F_cielo`: quota di cielo diffuso visibile, ridotta dagli ostacoli;
- `k_sito`: calibrazione del sito, che assorbe errore del satellite, potenza effettiva dei moduli e perdite uniformi;
- `sporco(t)`: andamento a "dente di sega" che si azzera dopo la pioggia;
- `d`: degrado annuo;
- `eventi(t)`: anomalie sparse come fermi, stringhe spente, distacchi.

Come si risolve:
- **Separare diretta e diffusa** è la chiave dell'identificabilità. Nei giorni sereni la diretta è circa l'80–90% dell'irradianza sul piano dei moduli, quindi il deficit "vede" la maschera `s`. Nei giorni coperti domina la diffusa e il rapporto misurato/atteso rivela `F_cielo`.
- **Selezione dei giorni sereni** con doppio controllo: (a) satellite, cioè rapporto tra CAMS all-sky e McClear vicino a 1 con bassa variabilità; (b) produzione "liscia" secondo SCSF. Usare solo la produzione sarebbe un errore, perché le tacche d'ombra farebbero sembrare nuvoloso un giorno sereno.
- **Ottimizzazione convessa.** Si minimizza una perdita robusta (Huber), perché una nuvola che il satellite non vede assomiglia a un'ombra. Si aggiungono due vincoli tipici del problema:
  - **variazione totale (TV)**, perché gli ostacoli sono "macchie" contigue nel cielo;
  - **monotonia in elevazione**: se a un dato azimut è bloccata un'elevazione, di solito lo sono anche quelle più basse (un profilo d'orizzonte `h(az)`).
  
  Per `s` il problema è lineare, quindi diventa un problema quadratico (QP) che CVXPY/OSQP risolve in pochi secondi per impianto.
- **Separare un orientamento sbagliato da un'ombra.** Un azimut dichiarato male produce un residuo *liscio e globale*; un ostacolo produce un deficit *localizzato e sparso*. È la classica scomposizione "liscio + sparso" (simile alla robust PCA), con penalità L1 sulla maschera.
- **Approccio bayesiano.** Priori Beta o processo gaussiano logistico su `s`, priori di flotta su `k_sito`, sporcamento e degrado come serie temporali latenti, inferenza con NumPyro o PyMC (HMC o inferenza variazionale). Il risultato è una mappa con **probabilità** ("al 90% c'è un ostacolo tra 120° e 140° di azimut e tra 10° e 25° di elevazione") e **intervalli di credibilità in euro** per ciascuna causa.
- **Test di coerenza "solstiziale"** (proposta mia): ogni posizione del sole si ripete due volte l'anno, in date simmetriche rispetto al solstizio. Un ostacolo visto il 20 aprile deve ricomparire verso il 23 agosto; una nuvola no. È una validazione interna gratuita.

**Passo 5. Uscite**
- **Cascata delle perdite** in kWh ed euro: fermi, distacchi, clipping, neve, ombra, sporcamento, guasti di stringa, degrado, residuo non spiegato.
- **Mappa d'ombra** sovrapposta alla vista aerea o alla mappa 3D.
- **Ticket per l'installatore:** causa, evidenza, priorità per euro all'anno, azione suggerita.
- **Report per il proprietario** in linguaggio semplice.

### 1.3 Letteratura e brevetti trovati

| Lavoro | Cosa fa | Rilevanza |
|---|---|---|
| **US 10,962,576 B2**, "Estimation of shading losses for photovoltaic systems from measured and modeled inputs", **Locus Energy** (inventori McBrearty, Herzig, Kerrigan). Domanda US 2018/0188301, concesso il 30 marzo 2021 ([Google Patents](https://patents.google.com/patent/US10962576), [USPTO pdf](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10962576), [Justia](https://patents.justia.com/patent/20180188301), [Golden](https://golden.com/query/list-of-locus-energy-patents-V4X85)) | Stima le perdite da ombra a partire da energia misurata, configurazione e meteo (irradianza, temperature, vento). Calcola l'irradianza diretta sul pannello da DNI e angolo di incidenza, **raggruppa la serie in "bucket" di azimut ed elevazione del sole** (es. elevazione 20–25°, azimut 180–185°) e con un predittore stima la sottoperformance. **Se l'R² della regressione supera una soglia, il bucket è dichiarato ombreggiato.** Google Patents lo indica come "active" | È il cuore dell'idea, brevettato negli USA. Locus Energy è stata poi acquisita da AlsoEnergy, a sua volta acquisita da Stem Inc. **[da verificare negli assignment USPTO]**. Non ho trovato una famiglia EP, quindi in UE è probabilmente libero, ma serve una verifica di libertà di operare (FTO). Una formulazione con maschera continua, TV e inferenza bayesiana è tecnicamente diversa dal "bucket più soglia R²", ma per il mercato USA serve un parere legale |
| Brevetti correlati: [US 9,112,078](https://patents.google.com/patent/US9112078) "Method of recognizing and assessing shadowing events", [US 8,369,999](https://patents.google.com/patent/US8369999) "forecasting shadowing", [US 10,069,460](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10069460) (localizza oggetti fissi dalla posizione del sole durante l'ombra e ne stima la distanza da come l'ombra "migra" sulle celle), [US 8,725,459](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/8725459) (mappa dell'irradianza ricavata da una rete di impianti) | Il campo è presidiato da brevetti | Assegnatari probabili SMA e Locus **[da verificare]** |
| **Energies 2019, 12(9):1722**, Tsafarakis, Sinapis, van Sark ([DOAJ](https://doaj.org/article/f3e07d62023b467ba2d09b522badd42d), [UU](https://research-portal.uu.nl/en/publications/data-analysis-for-effective-monitoring-of-partially-shaded-photov/)) | Algoritmo che rileva automaticamente le perdite da ombra confrontando i dati ad alta risoluzione di un impianto parzialmente ombreggiato con un impianto di riferimento non ombreggiato (con elettronica a livello di modulo). Separa l'ombra dagli altri guasti | Prova la separazione tra ombra e guasti, ma usa un riferimento a terra, non il satellite |
| **EPJ PV 2024**, Kappler & Starosta ([link](https://www.epj-pv.org/articles/epjpv/full_html/2024/01/pv230040/pv230040.html)) | Rileva l'ombra confrontando potenza simulata e misurata, con reti LSTM per le previsioni. Quantifica le perdite da ombra e sporcamento come base per il monitoraggio | Conferma l'approccio "simulato contro misurato" |
| **EPJ PV 2024**, Cooper, Burnham, Braid ([pdf](https://www.epj-pv.org/articles/epjpv/pdf/2024/01/pv230061.pdf)) | Stima le perdite da neve dai normali dati di monitoraggio confrontati col modello. Nota che l'ombra persistente (d'orizzonte o tra file) coincide con istanti in cui la tensione DC scende sotto il range dell'MPPT | La tensione DC è una firma utile per riconoscere l'ombra |
| **EPJ PV 2024**, Özkalay et al. ([link](https://www.epj-pv.org/articles/epjpv/full_html/2024/01/pv230068/pv230068.html)) | Effetto delle ombre parziali ripetute sull'affidabilità dei moduli residenziali (hot spot) | L'ombra causa anche danni, non solo perdite di produzione |
| **NREL/DOE, Progress in PV 2017** ([pdf](https://digitalcommons.unl.edu/cgi/viewcontent.cgi?article=1369&context=usdoepub)) | 46 impianti residenziali ombreggiati (inverter di stringa e di modulo) confrontati con il modello SAM. Conclusione: la modellazione dell'ombra si può fare **da remoto**, senza salire sul tetto | Valida il concetto di diagnosi remota |
| PVSAT-2, Drews et al., Solar Energy 2007 ([ADS](https://ui.adsabs.harvard.edu/abs/2007SoEn...81..548D/abstract)) | Monitoraggio e rilevamento guasti da satellite per impianti fino a 5 kW; 100 impianti in 3 paesi europei per 8 mesi | Precedente diretto, vecchio di quasi 20 anni |
| Diagnosi guasti da satellite con reti ricorrenti, Applied Energy ([link](https://www.sciencedirect.com/science/article/abs/pii/S0306261921011934)) e lavoro con random forest 2024 ([link](https://www.sciencedirect.com/science/article/abs/pii/S0196890424000177)) | Il satellite al posto del sensore riduce la sensibilità della diagnosi | Conferma il limite discusso al §2 |
| Accuratezza dell'orizzonte da immagini fisheye, DTU ([link](https://orbit.dtu.dk/en/publications/accuracy-evaluation-of-horizon-shading-estimation-based-on-fishey/)) | Piccoli errori sulla linea d'orizzonte danno grandi errori sull'irradianza a breve termine, ma si compensano con campionamento di **15 minuti o più** | Indica la risoluzione minima utile |
| SolarAnywhere Far Horizon ([link](https://www.solaranywhere.com/support/data-fields/far-horizon-shading/)) | Vende profili d'orizzonte da satellite e sostiene che gli strumenti convenzionali sovrastimano l'ombra sulla diretta | Possibile concorrente o fonte di dati a priori |
| pvlib, issue #1290 ([GitHub](https://github.com/pvlib/pvlib-python/issues/1290)) | La maggior parte dei dati satellitari non include l'effetto dell'orizzonte, che va applicato a parte | Conferma che serve un modulo "orizzonte" |

**Lacuna:** non ho trovato un paper peer-reviewed che faccia esattamente la ricostruzione bayesiana o convessa della maschera da produzione più satellite su impianti residenziali. È spazio libero per un contributo (e per contenuti di marketing tecnico), ma va considerato che Locus/AlsoEnergy lo fa in modo proprietario negli USA da anni.

---

## 2. Accuratezza e limiti

### 2.1 Risoluzione temporale

| Risoluzione | Spostamento del sole per intervallo | Qualità della maschera |
|---|---|---|
| 60 min | circa 15° di angolo orario | Grossolana: rileva ombre di mezza giornata, non un comignolo **[stima]** |
| 15 min | circa 3,75° | Buona per alberi, edifici e comignoli. Secondo DTU gli errori d'orizzonte si mediano a ≥15 min |
| 5 min | circa 1,25° | Ottima (Huawei ed Enphase la offrono). Il satellite a 5 minuti è più rumoroso, ma nei giorni sereni si usa McClear, che è "liscio" |

### 2.2 Granularità spaziale dei dati
- **Solo AC per inverter:** si vede *quando* manca energia ma non *quale* modulo. Ombre piccole sotto il 3% istantaneo si perdono **[stima]**.
- **Per MPPT o stringa (V e I):** abbastanza comune in Huawei, Sungrow, Fronius e SMA via API o Modbus. Si vedono la caduta di tensione da diodo di bypass, la stringa spenta e l'MPPT bloccato su un massimo locale. Grande salto di qualità.
- **Per modulo** (Enphase, ottimizzatori): localizza *quali pannelli* sono in ombra e, dalla "migrazione" dell'ombra sui moduli, permette di stimarne la distanza (il principio di US 10,069,460).
- **Attenzione al clipping:** in un impianto sovradimensionato a mezzogiorno l'ombra può essere invisibile, perché la potenza resta sopra il limite AC.
- **Attenzione agli impianti est-ovest su un solo MPPT:** due falde miste rendono il problema inverso mal posto.

### 2.3 Quanti dati servono
- **Geometria:** a 42° N (Roma) il sole a mezzogiorno va da circa 24,6° di elevazione (21 dicembre) a circa 71,4° (21 giugno). La fascia completa di posizioni si percorre in **6 mesi**, da solstizio a solstizio. Gli ostacoli bassi a sud si vedono solo tra novembre e febbraio.
- **Statistica [stima]:** con un errore residuo di circa 3–5% per intervallo sereno dopo la calibrazione, servono circa 10 osservazioni serene per cella perché l'errore standard scenda all'1–1,5%. Così si rilevano deficit di luce diretta ≥3–5%.
  - In Italia d'estate, in 3–6 settimane si ottiene una mappa affidabile **della fascia di cielo di quel periodo**.
  - Una mappa completa richiede 6–12 mesi. Nella Pianura Padana d'inverno (nebbia) i giorni utili sono pochi.
- **Lo storico risolve gran parte del problema:** FusionSolar, SolarEdge ed Enphase conservano anni di dati a 5–15 minuti. Con l'**importazione dello storico** la diagnosi arriva al giorno 0. I limiti di chiamata pesano poco: con SolarEdge, un anno a 15 minuti richiede circa 12 chiamate.
- **Degrado:** RdTools usa il metodo year-on-year, che serve almeno 2 anni di dati ([RdTools](https://rdtools.readthedocs.io/en/stable/)). Il suo modulo sporcamento (SRR/CODS) è ancora dichiarato "sperimentale" ([doc](https://rdtools.readthedocs.io/en/latest/generated/rdtools.soiling.soiling_cods.html)).

### 2.4 Errore del satellite sul singolo sito
- **CAMS v4, stazioni europee** ([Meteorol. Z. 2022](https://doaj.org/article/ff03a565d2424f92a066a3ed4036baf9)): bias relativo medio dell'irradianza globale (GHI) tra −1,3% e +3,3%; **RMSE relativo GHI 15,1%, irradianza diretta 30,6%**, da riferirsi alla scala oraria (la scala oraria è quella usata per le validazioni regolari: [EMS2021](https://presentations.copernicus.org/EMS2021/EMS2021-426_presentation.pdf), [ICEM2023](https://www.wemcouncil.org/ICEMs/ICEM2023/ICEM2023_20230628_PETRARCA_1445_SCHROEDTER-HOMSCHEIDT.pdf)).
- **A 15 minuti** l'errore è più alto, circa 20–25% sulla GHI in condizioni nuvolose **[stima]**. **Nei momenti sereni** è molto più basso, circa 3–6% sulla GHI **[stima]**, ed è per questo che l'inversione si fa sui giorni sereni.
- **Scale più lunghe:** NRMSE del satellite 4–8% su base mensile e 2–6% su base annua ([IEA-PVPS](https://iea-pvps.org/key-topics/uncertainties-in-pv-system-yield-predictions-and-assessments/)); Solargis indica ±4–8% (P90) sulla GHI annua ([Solargis](https://kb.solargis.com/docs/uncertainty-estimates)).
- **Conseguenza chiave:** un bias del satellite di ±3–8% sul singolo sito **non si distingue** da perdite uniformi dello stesso ordine (sporcamento leggero, degrado, moduli sotto targa, cablaggio). OMBRA può essere *molto* affidabile sulle perdite con una firma propria e *poco* su quelle uniformi, finché non usa:
  - **impianti vicini della flotta** come "sensori virtuali" (si confrontano i rapporti tra impianti vicini e l'errore del satellite si cancella);
  - la firma temporale dello sporcamento (azzeramento dopo la pioggia);
  - almeno 2 anni di dati per il degrado.

### 2.5 Come separare le cause

| Causa | Firma distintiva |
|---|---|
| Ombra | Deficit legato a (azimut, elevazione), ripetuto nei giorni sereni e nelle date simmetriche; colpisce la diretta; bordi netti; caduta di tensione DC |
| Sporcamento | Quasi uniforme su tutte le posizioni del sole, un po' più forte ad alto angolo d'incidenza; cresce nei periodi secchi e si azzera dopo la pioggia (serve il dato pioggia) |
| Degrado | Lento e monotono, metodo year-on-year su almeno 2 anni |
| Clipping | "Altopiano" piatto al valore nominale AC, solo con alta irradianza |
| Neve | Inverno, dopo nevicate, temperatura bassa, produzione quasi nulla con sole presente, recupero graduale |
| Distacco o limitazione di rete | Calo a zero o ad altopiano in giorni casuali, a mezzogiorno, correlato con tensione di rete alta |
| Stringa o MPPT guasto | Gradino permanente di circa 1/N della potenza (N = numero di stringhe) |
| Orologio od ora legale | Picco di produzione sfasato rispetto al mezzogiorno solare, spesso di 1 ora per metà anno |

### 2.6 Altezza e distanza dell'ostacolo
La maschera dà solo **angoli**. Per sapere *cosa* e *dove* è l'ostacolo servono dati 3D: altezza sopra il pannello = distanza × tan(elevazione).

- **LiDAR in Italia:** il Piano Straordinario di Telerilevamento Ambientale (PST, 2008–2015) ha coperto coste, alvei, aree a rischio idrogeologico e franose, **non tutto il territorio**, con circa 1 punto/m². Il Geoportale Nazionale serviva i dati solo come WMS, senza nuvola di punti ([Antiquity/Cambridge 2018](https://www.cambridge.org/core/product/F61727B70F5EE1DE0FCEDF710AD866CE)). Alcuni prodotti sono aperti: esempio, DSM 1 m Abruzzo in CC BY 4.0 ([INSPIRE](https://inspire-geoportal.ec.europa.eu/srv/api/records/m_amte:299FN3:6786ca71-e5b3-4964-8541-c7063c6df111)). La **Toscana** ha DSM e DTM a 1 m da voli 2019–2021 ([Regione Toscana](https://www502.regione.toscana.it/geonetwork/srv/api/records/r_toscan:f3ff89ee-49fa-4487-89fe-c69ae58ecd0c)); il Veneto ha un proprio geoportale. Per Lombardia, Piemonte ed Emilia-Romagna non ho trovato conferme e la copertura è a macchia di leopardo **[da verificare per regione]**. Limite: i dati 2008–2015 sono **vecchi** per la vegetazione, che cresce.
- **Google Solar API:** l'Italia è coperta (dati "medium quality" estesi a marzo 2024, poi un refresh "high quality") con DSM, mappe di flusso annuo e mensile e **ombra oraria** ([release notes](https://developers.google.cn/maps/documentation/solar/release-notes), [copertura estesa](https://developers.google.com/maps/documentation/solar/expand-coverage?hl=it), [Eurelectric](https://www.eurelectric.org/stories/google-solar-api-application-programming-interface/)). Prezzo a richiesta da verificare. Attenzione ai termini d'uso: limiti su conservazione e prodotti derivati **[da verificare]**.
- **OpenStreetMap:** impronte degli edifici buone, altezze scarse in Italia **[stima]**. **Copernicus DEM a 30 m e PVGIS:** solo orizzonte lontano (montagne).
- **Immagini aeree e visione artificiale** (modelli multimodali 2027): classificare l'ostacolo (albero deciduo, edificio, comignolo) dall'ortofoto. Gli alberi decidui hanno una maschera **stagionale** da modellare.
- **Foto dal proprietario:** foto panoramica dal tetto con bussola, come nel metodo smartphone di [ECMX 2023](https://doaj.org/article/6829eb899c694ec9a76ed9659bb22751). Ottima come verifica sul campo a costo zero.

### 2.7 Quota di impianti con diagnosi affidabile [stima]

| Classe di dati | Esempio | Mappa d'ombra affidabile | Guasti identificabili |
|---|---|---|---|
| A: per modulo, 5 min, ≥12 mesi | Enphase | 80–90% dei casi ombreggiati | Molto alta, anche quali moduli |
| B: V/I per MPPT, 5 min | Huawei, Sungrow, Fronius, SMA | 70–85% | Alta: stringhe, diodi, MPPT |
| C: solo AC per inverter, 15 min | SolarEdge via API | 50–70% | Gradini >5%, fermi, clipping |
| D: dati orari o giornalieri | Molti export | <30% | Solo guasti grossi |

Nell'insieme, su un parco italiano misto con storico disponibile **[stima]**: diagnosi "con confidenza" della mappa d'ombra nel 60–75% degli impianti; attribuzione in euro delle perdite con firma (fermi, clipping, ombra, stringhe, distacchi) entro ±20–30% relativo; perdite uniformi entro ±3–5 punti percentuali solo con il riferimento di flotta.

---

## 3. Guasti e perdite diagnosticabili da produzione + irradianza

| # | Guasto o perdita | Firma nei dati | Dati minimi | Affidabilità | Entità tipica (residenziale e piccolo C&I) |
|---|---|---|---|---|---|
| 1 | **Ombra** per ora e stagione (alberi, edifici, comignoli, file vicine) | Deficit legato alla posizione del sole nei giorni sereni | AC a 15 min; meglio V/I | Alta | 0 a oltre 20% per impianto; sui tetti urbani tipicamente 3–10% quando presente **[stima]**. Nei giorni sereni è più marcata tra le 10 e le 14 negli scenari urbani ([arXiv 2505.19876](https://arxiv.org/pdf/2505.19876)) |
| 2 | **Sporcamento** | Calo uniforme, azzeramento dopo la pioggia | AC più pioggia | Media (bassa sotto il 2%) | Media europea 0,9%/anno se la pioggia pulisce bene, fino al 5,3% se pulisce poco; Grecia 4,3%, Norvegia 0,2%; nel Sud Europa è stagionale ([pv magazine, prima mappa europea](https://www.pv-magazine.com/?p=39317)) |
| 3 | **Neve** | Produzione quasi nulla con sole in inverno, dopo nevicate | AC più neve e temperatura (ERA5) | Alta dove nevica | 0 al Sud e sulle coste; 1–5%/anno in zone alpine e appenniniche **[stima]**. Metodo in [Cooper et al. 2024](https://www.epj-pv.org/articles/epjpv/pdf/2024/01/pv230061.pdf) |
| 4 | **Stringa spenta** (fusibile, connettore MC4, sezionatore) | Gradino permanente di circa 1/N | AC (meglio per MPPT) | Molto alta | Perdita del 33–50% se l'inverter ha 2–3 stringhe. Raro ma di grande valore |
| 5 | **Diodo di bypass guasto o in conduzione** | Perde circa 1/3 di modulo: circa 3% su una stringa da 10 moduli; caduta di Vmp di circa 10–15 V | **V per MPPT** | Media con V, bassa con solo AC | 1–5% della stringa **[stima]** |
| 6 | **PID** (degrado indotto da potenziale) | Calo graduale con perdita di tensione, peggiore in clima caldo e umido | V/I; meglio una curva I-V | Bassa senza I-V (si confonde col degrado) | Da pochi % fino al 10–30% nei casi gravi **[letteratura nota, non verificata qui]** |
| 7 | **Hot spot e microcricche** | Solo indiretti (mismatch) | Serve termografia o elettroluminescenza | **Non diagnosticabile** in modo affidabile | Rischio più che perdita. L'ombra ripetuta aggrava gli hot spot ([Özkalay 2024](https://www.epj-pv.org/articles/epjpv/full_html/2024/01/pv230068/pv230068.html)) |
| 8 | **Degrado** | Trend year-on-year | ≥2 anni | Media | Mediana −0,75%/anno nella flotta NREL; −0,88% nei climi caldi, −0,48% nei freddi; il 90° percentile degrada molto più in fretta ([NREL 2024](https://www.nrel.gov/docs/fy24osti/88769.pdf), [TechXplore](https://techxplore.com/news/2024-01-extreme-weather-aging-affect-photovoltaic.amp), [NREL 2022](https://nrel.gov/docs/fy22osti/83487.pdf)). Dati soprattutto C&I e utility |
| 9 | **Clipping o inverter sottodimensionato** | Altopiano al valore nominale AC | AC a 15 min | Molto alta | Rapporto DC/AC 1,1–1,3: 0–3%/anno **[stima]**. Spesso è una scelta voluta, non un guasto |
| 10 | **Distacchi per sovratensione** (CEI 0-21: soglia 59.S1 a 253 V su media mobile di 10 minuti, distacco veloce sopra circa 264 V) | Calo a zero a mezzogiorno in giorni casuali, con tensione di rete alta | AC; meglio con V di rete | Alta se l'API dà la tensione | Specifico del sito: nei forum ci sono casi con 3–4 distacchi al mese e un distributore che misura "nella norma" ([forum Edilclima](https://forum.edilclima.it/viewtopic.php?p=221927), [forum fibra.click](https://forum.fibra.click/d/42179-tensione-minima-e-massima-enel/129)). Diverse unità % all'anno su linee deboli **[stima]** |
| 11 | **Limitazione di immissione o riduzione di potenza** (impostazione errata, "immissione zero") | Altopiano sotto il nominale, correlato ai consumi | AC più contatore | Alta con il contatore | Da poche unità % fino a quote rilevanti se l'impostazione è sbagliata **[stima]** |
| 12 | **Fermi inverter o comunicazione** | Zero con sole presente; va separato il buco di dati dal fermo vero | AC | Molto alta | Perdite di disponibilità degli inverter circa 2,3% dell'energia annua (dato NREL PV Fleet citato da una [fonte secondaria](https://accelerate-solar.com/blog/solar-system-optimization-complete-guide/)) |
| 13 | **MPPT bloccato su massimo locale** in ombra parziale | V anomala, perdita maggiore del previsto dalla maschera | V/I per MPPT | Media | 1–5% in impianti ombreggiati **[stima]** |
| 14 | **Orientamento o inclinazione dichiarati sbagliati** | Residuo liscio e asimmetrico tra mattina e pomeriggio | AC nei giorni sereni | Alta (stima di tilt e azimut, [pvanalytics](https://pvanalytics.readthedocs.io/en/stable/generated/gallery/index.html), [arXiv 1706.06878](https://arxiv.org/pdf/1706.06878)) | Non è una perdita ma un errore di metadato. Va corretto per non inventare ombre |
| 15 | **Orologio o fuso orario sbagliato** (ora legale) | Picco spostato rispetto al mezzogiorno solare | AC | Molto alta (rilevamento di time shift, approccio SCSF/solar-data-tools) | Non è una perdita, ma se non corretto produce **false ombre** al mattino o alla sera |
| 16 | **Batteria e autoconsumo configurati male** (non carica, carica dalla rete in fascia F1, limiti di stato di carica errati) | Profili di carica e scarica incoerenti | Dati batteria e contatore (API ibride Huawei, Sungrow, FoxESS) | Media | 50–300 €/anno di valore perso **[stima]** |
| 17 | **Mismatch, cavi, moduli sotto targa** | Perdita uniforme | | **Bassa**: si confonde col bias del satellite | 1–3% **[stima]** |

**Quanti impianti residenziali rendono meno del dovuto?** Mancano studi peer-reviewed solidi con la soglia "oltre il 10%". Le cifre disponibili vengono da venditori di monitoraggio australiani, quindi con un interesse in gioco:
- Solar Analytics e SunWiz, su circa 35.000 clienti: **circa il 75%** dei 3,3 milioni di impianti australiani non rende quanto potrebbe, ma il dato include le tariffe sbagliate ([RenewEconomy](https://switchedon.reneweconomy.com.au/content/australias-3-3-million-rooftop-solar-systems-are-likely-to-be-underperforming));
- "1 impianto su 5 rende meno del dovuto" ([Energy Makeovers](https://energymakeovers.com.au/blog/one-in-five-rooftop-solar-systems-are-under-performing/));
- uno studio Ausgrid su 8.000 impianti: oltre la metà non raggiunge la produzione ottimale ([Energy Matters](https://www.energymatters.com.au/renewable-news/is-your-solar-system-underperforming/)).

Il test di OMBRA (§8) potrebbe **produrre lui stesso il primo dato italiano**, che sarebbe anche un ottimo contenuto di marketing.

**Valore per impianto [stima]:** un impianto da 6 kWp nel Centro-Sud produce circa 7.500 kWh/anno. Una perdita del 10% vale **circa 100–180 €/anno** (kWh autoconsumati a circa 0,20–0,30 €/kWh, kWh immessi a circa 0,08–0,12 €/kWh). Il valore diagnostico per singolo impianto è quindi piccolo, e questo vincola il prezzo per impianto, soprattutto se venduto all'installatore.

---

## 4. Accesso ai dati (punto critico)

### 4.1 API cloud dei produttori

| Produttore | Accesso per terzi | Limiti e risoluzione | Costo | Note |
|---|---|---|---|---|
| **Huawei FusionSolar** | Account "Northbound" creato dall'**installatore o proprietario dell'impianto** (Company Management > Northbound Management), con utente diverso dal login principale ([HA FusionSolar](https://github.com/tijsverkoyen/homeassistant-fusionsolar)). Solytic e meteocontrol VCOM lo integrano già ([Solytic](https://kb.solytic.com/en/knowledge/set-up-api-key-huawei-fusionsolar), [VCOM](https://help-center.meteocontrol.com/en/vcom-cloud/latest/huawei-fusionsolar-api-1)) | **Limiti molto stretti**: quota legata al numero di impianti (secondo uno sviluppatore, chiamate al giorno = arrotondamento per eccesso di impianti/100, più 24; errore 407 se si supera); una sola sessione di login; dati a 5 minuti ([Homey](https://community.homey.app/t/app-pro-huawei-solar-smart-energy-for-a-better-life/61745), [guida openAPI](https://docs.rs/crate/huawei_client/latest/source/docs/Communicate%20with%20FusionSolar%20through%20an%20openAPI%20account.pdf)) | Gratis | Probabilmente il primo marchio residenziale in Italia **[da verificare: non ho trovato dati di quota di mercato]**. Rischio politico: si discute di restrizioni UE e nazionali all'accesso remoto per gli inverter cinesi ([greenMe 2026](https://www.greenme.it/?p=1394167)). Sui residenziali offre la diagnosi I-V intelligente a livello di stringa, ma **non con ottimizzatori** ([datasheet](https://solar.huawei.com/-/media/Solar/attachment/pdf/mea/datasheet/IV-Curve.pdf)): è una funzione concorrente |
| **SolarEdge** | API key del sito o dell'account (generata dall'amministratore) | **300 richieste al giorno** per token e per sito, errore 429 oltre ([KNX forum](https://knx-user-forum.de/forum/supportforen/peaknx/2050339-solaredge-bridge-api-access), [ChargeHQ](https://community.chargehq.net/t/lost-connection-to-solaredge-servers/694)); energia e potenza a 15 minuti ([solar-api](https://docs.rs/crate/solar-api/0.1.6)) | Gratis | I dati per modulo (ottimizzatori) **non risultano esposti** nell'API pubblica **[da verificare]** |
| **Fronius Solar.web** | Query API | Dettagli da verificare | **52 €/mese fino a 20 impianti, 195 € fino a 100, 494 € fino a 400** ([eniris](https://docs.eniris.be/Monitoring/Integrations/Battery%20or%20PV%20inverters/Fronius%20integration/FroniusAPI)) | Alternativa gratuita: export FTP locale dall'inverter, Solar API JSON, Modbus/SunSpec |
| **SMA Sunny Portal / ennexOS** | Il **proprietario** aggiunge l'integratore come proprietario e amministratore, poi si apre un ticket con SMA ([eniris/Sunlight](https://docs.sunlight-group.com/en/Monitoring/Integrations/Battery%20or%20PV%20inverters/SMA%20integration/SMA_FTP/SMA_API)) | Dettagli da verificare | A pagamento (listino SMA) | In locale: Modbus/SunSpec, data push gratuito da Home Manager |
| **Enphase Enlighten v4** | App per sviluppatori; piano **Partner** per installatori con almeno 10 impianti Enphase ([Solytic](https://kb.solytic.com/en/knowledge/enphase-enlighten-partner-api)) | Piano Watt gratuito con **1.000 chiamate al mese**; chiamate extra a 0,005 $ con piani Kilowatt o Megawatt; Partner fino a 10.000 chiamate al mese per app ([developer plans](https://developer-v4.enphase.com/developer-plans)). Telemetria **per microinverter**, cioè per modulo | Gratis o a pagamento | Il dato migliore per localizzare le ombre. In locale: gateway IQ (Envoy) con token |
| **Sungrow iSolarCloud** | Open API (developer-api.isolarcloud.com): API key, access key, chiave RSA, utente in sola lettura consigliato ([eniris IT](https://integrations.eniris.be/it/Controller/Devices/Cloud/ISolarCloud)) | Limiti non trovati | Gratis | Documentazione e qualità criticate dagli sviluppatori ([GoSungrow](https://github.com/MickMake/GoSungrow)) |
| **Growatt, GoodWe SEMS, SolisCloud, FoxESS** | Tutti hanno API "open" basate su token o chiave; Solis rilascia la chiave su richiesta al supporto | **Non verificato in questa ricerca** | In genere gratis | Da mappare una per una |
| **Tesla** | Fleet API, a consumo dal 2025 **[non verificato]** | | A consumo | Rilevante soprattutto per le batterie Powerwall |
| **Aggregatori** (Enode) | Consenso dell'utente, 8 marchi di inverter | Solo produzione attuale e cumulata ([Enode](https://enode.com/use-cases/solar-inverters)) | Su preventivo | **Non basta** per OMBRA: niente serie storiche ad alta risoluzione |

**Accesso locale:** Modbus TCP/SunSpec e integrazioni Home Assistant (huawei_solar, SolarEdge Modbus, Fronius, SMA) danno dati al secondo **per MPPT o stringa**: la qualità migliore in assoluto. Però richiede hardware o Home Assistant in casa, quindi è adatto a beta tester ed entusiasti, non alla scala.

**Contatore 2G (Italia):** il canale Chain 2 porta i dati dal contatore direttamente al cliente o a un terzo da lui indicato, tramite un dispositivo che deve superare test di integrazione con e-distribuzione ([ARERA/e-distribuzione](https://arera.it/allegati/eventi/190522_pres_edistribuzione.pdf), [contratto Chain 2](https://www.e-distribuzione.it/content/dam/e-distribuzione/documenti/open-meter/monitoraggiochain2/Contratto%20per%20il%20monitoraggio%20Chain%202_%20V20181018.pdf)); dati quartorari ([bolletta-energia](https://bolletta-energia.it/utenze/guida/contatori/chain-2)). **Misura solo lo scambio netto con la rete**, non la produzione: utile per diagnosticare limitazioni di immissione e configurazione di autoconsumo e batteria, non per l'ombra.

### 4.2 Data Act UE (Reg. 2023/2854, applicabile dal 12 settembre 2025)

Testo: [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2023/2854/oj); sintesi in [Skadden](https://www.skadden.com/insights/publications/2025/06/eu-data-act), [Clifford Chance](https://www.cliffordchance.com/insights/resources/blogs/talking-tech/en/articles/2025/09/eu-data-act--a-new-era-for-data-sharing-has-begun.html), [Wikipedia](https://en.wikipedia.org/wiki/Data_Act_(European_Union)), [Enode](https://enode.com/blog/evolving-energy/the-eu-data-act-what-the-energy-industry-needs-to-know-before-september-12).

- **Art. 4:** l'**utente** del prodotto connesso (il proprietario o locatario dell'impianto) ha diritto ad accedere ai dati "prontamente disponibili" del prodotto e dei servizi correlati, con i metadati necessari, gratuitamente, in formato strutturato e leggibile da macchina, e dove tecnicamente fattibile **in modo continuo e in tempo reale**.
- **Art. 5:** su richiesta dell'utente, il titolare dei dati (il produttore che li tiene in cloud) deve metterli a disposizione di **un terzo scelto dall'utente**, come OMBRA, con la stessa qualità che ha lui e senza costi per l'utente. Un inverter con connettività è un "prodotto connesso", quindi **sì: in linea di principio gli artt. 4–5 danno a OMBRA una via legale**.
- **Art. 6:** il terzo può usare i dati solo per le finalità concordate con l'utente e non può usarli per sviluppare un **prodotto connesso concorrente**. Un software diagnostico non è un inverter, quindi non c'è conflitto **[mia lettura]**.
- **Art. 9:** il titolare può chiedere al terzo un compenso ragionevole e non discriminatorio; per le PMI il compenso è limitato ai costi **[testo da riverificare]**.
- **Art. 3:** i prodotti immessi sul mercato **dopo il 12 settembre 2026** devono essere progettati con accesso diretto ai dati per impostazione predefinita ([lawandtechnology.eu](https://lawandtechnology.eu/en/data-act-access-by-default-connected-products-2026-en/), [McCann FitzGerald](https://www.mccannfitzgerald.com/knowledge/data-privacy-and-cyber-risk/data-act-developments-2026-and-beyond)).

Limiti pratici:
1. Nessuna API standard è imposta: il produttore può consegnare un dump di file. Per la versione CSV di OMBRA un dump storico va benissimo.
2. Il produttore può tutelare i segreti commerciali.
3. L'applicazione da parte delle autorità nazionali è ancora agli inizi.
4. **Non ho trovato produttori di inverter (Fronius, SMA, SolarEdge, Enphase, Huawei) con un portale pubblico per richieste Data Act.**

Il Data Act va quindi usato come leva negoziale e come canale di riserva per il proprietario, mentre la via operativa resta l'API aperta dall'installatore.

**GDPR:** dati di produzione più posizione di un'abitazione sono dati personali. Serve un accordo di trattamento (DPA) con gli installatori, che fanno da titolari, con OMBRA come responsabile.

---

## 5. Fonti di irradianza da satellite

| Fonte | Risoluzione e copertura | Ritardo | Licenza e costo | Note |
|---|---|---|---|---|
| **CAMS Radiation Service** (con McClear per il cielo sereno) | Da 1 minuto a mensile, dal 2004; disco Meteosat (Europa, Africa, Medio Oriente); include componente diretta e diffusa | **Giorno precedente** (da febbraio 2026) | Gratuito e aperto; la licenza Copernicus consente l'uso commerciale con attribuzione **[da verificare il testo]**. **500 richieste al giorno** su ADS ([ECMWF](https://forum.ecmwf.int/t/cams-solar-radiation-timeseries-new-data-availability-and-request-limits-on-ads/14735), [Copernicus](https://hds.hub.copernicus.eu/datasets/hh-dataset-cams-solar-radiation-timeseries), [xweather](https://cams.xweather.com/)) | Con richieste mensili per sito regge circa 10.000 impianti; per aggiornamenti giornalieri serve un'altra fonte |
| **EUMETSAT LSA SAF** (MSG) / **MTG** | 15 minuti (MSG), 10 minuti (MTG) | **Circa 2 ore** | Via Open-Meteo ([doc](https://open-meteo.com/en/docs/satellite-radiation-api)) | Utile per diagnosi quasi in tempo reale |
| **SARAH-3** (CM SAF) | 30 minuti | Climatologico | Gratuito | Buono per lo storico, non per l'operatività |
| **PVGIS** | Orario, basato su SARAH | Anni passati | Gratuito | Orizzonte da modello del terreno, solo ostacoli lontani; non operativo |
| **Solcast** (DNV) | 5–60 minuti (piano Pro), 30–60 minuti (Starter); storico dal 2007 fino a 7 giorni fa | Fino a 7 giorni fa per lo storico (dati in tempo reale con piano a pagamento) | **15 mesi-sito gratuiti**, poi su preventivo ([pricing](https://solcast.com/pricing/historical-time-series), [changelog](https://solcast.com/changelog)) | Endpoint hobbisti deprecato |
| **Open-Meteo** | Aggrega le fonti sopra | 2 ore | Gratuito non commerciale; piani commerciali citati da terzi a 29 $/mese e 99 $/mese, ma precedenti all'API satellitare ([pricing](https://open-meteo.com/en/pricing), [substack](https://openmeteo.substack.com/p/api-subscriptions-for-commercial)) | Da confermare che il piano commerciale copra i dati satellitari |
| **Meteonorm / Solargis** | Premium | | A pagamento, su preventivo | Non necessari per l'MVP |

**Scelta consigliata:** CAMS più McClear per l'inversione (gratis, con componenti diretta e diffusa e cielo sereno), LSA SAF via Open-Meteo per gli allarmi rapidi, Solcast solo come confronto nel test.

---

## 6. Architettura 2027

1. **Ingestione:** connettori per CSV, API dei produttori e add-on Home Assistant, con uno schema comune: timestamp in UTC, potenza AC, V/I per MPPT, energia, stati, batteria, metadati. Storage in Parquet su S3 più Postgres/Timescale.
2. **Meteo:** CAMS, LSA SAF ed ERA5 in cache per cella di griglia (gli impianti vicini condividono i dati).
3. **Qualità dati:** solar-data-tools e pvanalytics (time shift, clipping, giorni sereni, cambi di capacità) e **stima automatica dei metadati** (inclinazione, azimut, kWp effettivi).
4. **Modello fisico:** pvlib (trasposizione, angolo d'incidenza, temperatura, inverter, limite AC).
5. **Motore inverso:**
   - QP convesso per la maschera (CVXPY/OSQP, con TV, L1 e vincolo di monotonia);
   - modello bayesiano gerarchico (NumPyro/JAX) per bias del sito, sporcamento, degrado e maschera stagionale;
   - rilevatori di cambiamenti per fermi e stringhe;
   - cascata delle perdite in € con intervalli di credibilità. Il calcolo richiede pochi secondi per impianto al giorno: 10.000 impianti stanno su una sola VM.
6. **Strato di flotta (il vantaggio difendibile):**
   - priori empirici per regione, marca e orientamento;
   - "sensore virtuale" dagli impianti vicini per cancellare l'errore del satellite (attenzione: concetto coperto da brevetti Locus negli USA);
   - **etichette di verità sul campo** dagli installatori (confermato o smentito), che allenano un classificatore sui residui fisici;
   - monitoraggio della **crescita degli alberi** anno su anno.
7. **Strato LLM:**
   - report in linguaggio semplice e ticket tecnico con grafici di evidenza;
   - domande e risposte per proprietari e installatori **ancorate solo ai numeri calcolati**, tramite chiamate a strumenti sul database, senza numeri inventati;
   - visione artificiale su ortofoto per classificare l'ostacolo;
   - **agente che apre ticket** (email, WhatsApp Business, CRM o helpdesk dell'installatore) e verifica dopo l'intervento ("dopo la pulizia +4,1%");
   - **agente che mantiene i connettori**, rigenerando il codice quando un'API cambia.
   
   La fisica resta il nucleo: le cifre in euro devono essere spiegabili.
8. **Cosa è difendibile:** dati di flotta calibrati, dataset etichettato, integrazione nel flusso di lavoro dell'installatore, brand tecnico. **Non** l'algoritmo in sé, che è replicabile con strumenti open source da team competenti.

---

## 7. Piano di sviluppo (un ingegnere AI)

| Mese | Cosa | Note |
|---|---|---|
| 0–1 | **Versione CSV, offline:** parser degli export dai portali FusionSolar, SolarEdge, Fronius ed Enphase (tutti permettono qualche export a 5–15 minuti **[da verificare marca per marca]**), download CAMS, modello pvlib, selezione dei giorni sereni, **heatmap giorno × ora dei residui**, maschera v0, cascata delle perdite v0 | Sviluppo su dataset pubblici: NREL PVDAQ, PVOutput.org, dataset UK di Open Climate Fix (decine di migliaia di impianti) **[da verificare l'accesso]** |
| 2–3 | Modello bayesiano con incertezze, separazione delle cause, report PDF più testo generato da LLM, primi **2 connettori API** (Huawei e SolarEdge, oppure i marchi prevalenti tra gli installatori partner) | |
| 3–4 | Dashboard per l'installatore con classifica degli impianti per euro persi e generazione dei ticket; connettori Enphase e Fronius | |
| 5–6 | Calibrazione di flotta, ciclo di feedback dalla verifica sul campo, integrazione delle mappe 3D (Google Solar API e LiDAR dove c'è) | |

**Costi vivi dell'MVP [stima]:** cloud 50–200 €/mese per 1.000 impianti; CAMS gratuito; Solcast in prova gratuita; Fronius 52–195 €/mese se serve; Enphase Partner gratuito; LLM circa 1–5 centesimi per report. **Totale sotto i 5 k€ in 6 mesi**, tempo di Lorenzo escluso.

**Da cosa partire:** dalla **versione CSV**. Non dipende dalle API e mostra il valore subito sullo storico. Si testa con gli installatori in poche settimane.

---

## 8. Test più economico (≤ 10 k€, 8–10 settimane)

1. **Dati di sviluppo (settimane 1–3):** algoritmo sui dataset pubblici più 20–30 impianti di "amici" o di utenti Home Assistant italiani, che caricano i CSV.
2. **Reclutamento:** 3–5 installatori od O&M italiani con flotte di 100–1.000 impianti (prevalentemente Huawei e SolarEdge). Offerta gratuita: *"Vi diciamo quali 20 impianti della vostra flotta perdono più euro, e perché"*. Chiediamo un account API in sola lettura o gli export di **200–300 impianti con almeno 12 mesi di storico**. Canale alternativo: proprietari da forum e gruppi (gruppi Facebook dedicati al fotovoltaico, Home Assistant Italia) che caricano CSV.
3. **Analisi alla cieca:** report e classifica, con una confidenza per ogni diagnosi.
4. **Verifica sul campo (settimane 6–9):** campione stratificato di **40–60 impianti**:
   - 20 segnalati per ombra ad alta confidenza;
   - 10–15 per guasti (stringa, distacchi, clipping anomalo, sporcamento);
   - 10–15 "puliti" come controllo.
   
   Strumenti: foto panoramica con bussola dal tetto (gratis, fatta dal proprietario), Google Earth e Solar API, sopralluogo o volo con drone dell'installatore (100–150 € a sito come incentivo), controllo delle stringhe o curva I-V durante la manutenzione ordinaria.
5. **Budget:** incentivi per i sopralluoghi 2–4,5 k€; API e cloud circa 0,5 k€; Solcast, Fronius e Google Solar circa 0,5–1 k€; imprevisti 1–2 k€. **Totale 4–8 k€.**

**Soglie GO / STOP**

| Metrica | GO | STOP |
|---|---|---|
| Precisione dei ticket "azionabili" (confermati sul campo) | ≥75% | <60% |
| Errore sull'azimut dell'ostacolo | ≤10–15° | >25° |
| Perdita da ombra stimata contro la verifica sul campo (foto più ricostruzione 3D) | entro ±30% relativo | oltre ±50% |
| Quota di impianti con almeno un problema **risolvibile** che vale ≥100 €/anno | ≥15–20% | <8% |
| Quota di impianti con diagnosi "con confidenza" | ≥60% | <40% |
| Installatori che chiedono di continuare a pagamento | ≥3 su 5 | ≤1 su 5 |

---

## 9. Cosa potrebbe ucciderlo (tecnicamente)

1. **Accesso ai dati che si chiude o diventa caro:** limiti Huawei, API a pagamento, eventuali restrizioni UE all'accesso remoto per gli inverter cinesi, produttori che riservano i dati alla propria analitica premium.
2. **I produttori fanno la stessa cosa gratis nei loro portali:** Huawei ha già la diagnosi I-V, SMA ha brevetti sul riconoscimento delle ombre, Enphase e SolarEdge mostrano già il dettaglio per pannello.
3. **Rapporto segnale/rumore:** se l'errore del satellite rende inattendibili le perdite uniformi, la promessa "euro per causa" si riduce a ombra, fermi e clipping. Se la precisione sul campo scende sotto il 60%, gli installatori smettono di fidarsi.
4. **Perdite non risolvibili:** il proprietario non può abbattere l'albero o l'edificio del vicino. Se la maggior parte delle perdite trovate è un'ombra non risolvibile, il prodotto diventa un "bello da sapere".
5. **Metadati sporchi e configurazioni complesse:** kWp e orientamento sbagliati nei portali, falde est-ovest su un solo MPPT, ottimizzatori che mascherano le ombre.
6. **Brevetti:** Locus/AlsoEnergy negli USA (bucket per posizione del sole più regressione, mappatura dell'irradianza da una rete di impianti) e probabilmente SMA. Serve una verifica FTO prima di entrare nel mercato USA.
7. **Concorrenza delle piattaforme di monitoraggio esistenti:** Solytic, meteocontrol VCOM, Solar-Log, Solar Analytics, oltre al mondo utility (SmartHelio e simili, [Omdena](https://www.omdena.com/blog/top-startups-ai-solar-industry)). Integrano già le API e l'irradianza satellitare; aggiungere una "maschera d'ombra" per loro è un'aggiunta incrementale.
8. **Valore per impianto basso** (circa 100–180 € di perdita annua per un 10% su un 6 kWp): il prezzo per impianto resta basso, quindi servono flotte grandi. L'aspetto di mercato va approfondito da un'altra analisi.

---

## Scorecard (1–5)

- **vant (vantaggio di Lorenzo): 4.** Problemi inversi, ottimizzazione convessa e inferenza bayesiana sono il suo terreno, e unisce ingegneria AI e marketing. Gli mancano esperienza nel fotovoltaico e una rete di installatori.
- **valid (validità tecnica e prove esistenti): 3.** La fisica e il concetto sono provati (PVSAT-2 2007, NREL 2017, brevetto Locus, Energies 2019), ma l'attribuzione in euro per causa sul singolo sito con il solo satellite non è dimostrata su larga scala. La domanda di mercato non è validata.
- **autom (automatizzabilità): 4.** Una volta stabili i connettori, analisi, report e ticket sono completamente automatici. Restano manuali l'attivazione delle credenziali, le correzioni dei metadati, le contestazioni e la manutenzione dei connettori quando le API cambiano (riducibile con agenti).
- **dif (difendibilità): 3.** L'algoritmo è replicabile con strumenti open source e il concetto è in parte brevettato da altri. Il vantaggio difendibile viene solo da dati di flotta calibrati, verifiche sul campo etichettate e integrazione nel lavoro degli installatori, con forte dipendenza dai produttori per i dati. *(Se "dif" significava difficoltà tecnica: 3/5, media. Il nucleo matematico è alla portata di Lorenzo; la parte difficile sono i dati e la loro validazione.)*

---

### Fonti principali (oltre a quelle citate nel testo)
- Contesto del mercato italiano: 2.092.088 impianti e 43,5 GW a fine 2025; il residenziale è il 27% della potenza (11,6 GW); nuovi impianti sotto 20 kW 198.667 nel 2025 contro 274.537 nel 2024 ([Qualenergia/Italia Solare](https://www.qualenergia.it/articoli/dati-2025-fotovoltaico-italia-solare/), [Italia Solare Q4](https://www.italiasolare.eu/wp-content/uploads/2026/02/20260130_report-q4-fotovoltaico_final-1.pdf), [Renewable Matter](https://www.renewablematter.eu/fotovoltaico-residenziale-italia-calo-2025)).
- Sensibilità dell'ombra agli errori di misura dell'orizzonte: [Penn State](https://pure.psu.edu/en/publications/sensitivity-of-shading-calculations-to-horizon-measurement-accura/).
- Studi EPJ PV 2026 sull'ombra a livello di cella: [link](https://www.epj-pv.org/articles/epjpv/full_html/2026/01/pv20250061/pv20250061.html).
