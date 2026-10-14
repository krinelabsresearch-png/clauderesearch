# 208 — OMBRA: clienti, mercato, concorrenti, valore, prezzi, rischi

> Rapporto di ricerca del 14/10/2026 (agente di ricerca, verificato a campione da Claude). Le voci [NV] non sono verificate con una fonte; "stima" indica un calcolo.

# OMBRA (Idea 208): clienti, mercato, concorrenti, prezzi e rischi

*Ricerca al 14/10/2026. Ho fatto 35 ricerche web. Dove un dato non viene da una fonte lo segno **[stima]**. Dove viene da mie conoscenze precedenti e non l'ho verificato in questa ricerca lo segno **[da verificare]**.*

---

## SINTESI ESECUTIVA

- **Italia a fine 2025:** 2.092.088 impianti per 43,5 GW.
  - Residenziale: 11,6 GW (27%).
  - C&I 20 kW–1 MW: 18,9 GW (43%).
  - Utility: 13,0 GW (30%).
- **Parco giovane per numero, vecchio per potenza.** Il 52% della potenza cumulata è stato installato tra il 2007 e il 2014, cioè nell'era Conto Energia.
- **Il segmento con più valore è il vecchio Conto Energia.**
  - Alla chiusura c'erano 531.242 impianti per 18.217 MW.
  - Costava circa 6,5 mld€ l'anno di incentivi, cioè circa 0,29–0,31 €/kWh in media [stima mia: 6,5 mld€ diviso circa 21–22 TWh].
  - **L'1% di produzione persa sull'intero parco vale circa 80 M€ l'anno.** Per un impianto da 1 MW del II Conto l'1% vale circa 6.000 € l'anno.
  - Secondo il GSE, circa 20 GW dell'era Conto Energia hanno una produzione reale del 75% e un degrado reale del 2,2% l'anno.
  - Il GSE ha già mandato circa 13.000 lettere di "alerting" a impianti poco performanti.
- **Finestra temporale.** Gli incentivi scadono tra il 2026 e il 2033. Il Decreto Bollette 2026 (DL 21/2026) apre l'uscita anticipata dal 2028, ma solo con rifacimento integrale dell'impianto. Quindi nel 2026–2028 molti proprietari devono decidere se fare manutenzione, revamping o uscire, e hanno bisogno di dati.
- **Concorrenza.** È affollata sul monitoraggio (Solytic, Solar-Log, meteocontrol, SolarEdge, Enphase, Huawei, Solarman, GSE stesso). Non ho trovato nessuno che, per impianti multi-marca residenziali o piccolo C&I, ricostruisca gli ombreggiamenti e scomponga le perdite per causa in euro. Esistono solo componenti accademici e brevetti USA. Il vuoto di mercato è reale ma sottile, quindi copiabile.
- **Disponibilità a pagare (DAP) delle famiglie: bassa.**
  - Solar Analytics in Australia chiede 60–95 AUD l'anno.
  - Enphase premium costa circa 9,99 $ al mese (prezzo riportato da un sito terzo).
  - In Europa il valore recuperato da un impianto residenziale è di 40–100 € l'anno.
- **Verdetto: partire dal Conto Energia, non dalle famiglie.**
  - Target: impianti in Conto Energia da 100 kWp a 1 MWp e i loro gestori di manutenzione (O&M) o di asset.
  - Offerta: una "TAC" una tantum, poi monitoraggio in €/kWp l'anno, più commissioni di segnalazione sul revamping.
  - Poi gli installatori come canale, e infine i parchi ad alta tariffa in Germania (EEG 2009–2012) e Francia (2006–2011).

---

## A. DIMENSIONE DEL MERCATO

### A1. Italia (GSE, Terna/Gaudì via Italia Solare)

| Indicatore | 2022 | 2023 | 2024 | 2025 | 2026E |
|---|---|---|---|---|---|
| Impianti cumulati | ~1,23 M [da verificare] | ~1,60 M | **1.875.870** | **2.092.088** | ~2,27 M [stima] |
| Potenza cumulata | ~25,1 GW [da verificare] | **30,3 GW** | **37,0 GW** | **43,5 GW** | ~49–50 GW [stima] |
| Nuovi impianti nell'anno | — | **~371.500** | **283.914** | **213.200** | ~180–200k [stima] |
| Nuova potenza nell'anno | ~2,5 GW | **5,2 GW** | **6,7 GW** | **6,44 GW** | ~6 GW [stima] |

Fonti: [GSE Rapporto 2024](https://www.gse.it/documenti_site/Documenti%20GSE/Rapporti%20statistici/Solare%20Fotovoltaico%20-%20Rapporto%20Statistico%202024.pdf), [QualEnergia su GSE 2024](https://www.qualenergia.it/pro/documenti/rapporto-statistico-2024-solare-fotovoltaico/), [Italia Solare Q4 2025](https://www.italiasolare.eu/wp-content/uploads/2026/02/20260130_report-q4-fotovoltaico_final-1.pdf), [QualEnergia dati 2025](https://www.qualenergia.it/articoli/dati-2025-fotovoltaico-italia-solare/), [pv magazine](https://www.pv-magazine.com/2026/02/06/italy-installs-6-4-gw-of-solar-in-2025/).

**Segmenti a fine 2025.** Potenza da Italia Solare; numero di impianti per fascia **[stima]**, ricostruita da potenze medie e dalla distribuzione storica del GSE.

| Segmento | Potenza | N. impianti (stima) | Trend 2025 |
|---|---|---|---|
| Residenziale <20 kW | 11.627 MW | ~1,85–1,9 M (media ~6 kW) | impianti da 274.537 a 198.667 (−28%) |
| Piccolo commerciale 20–200 kW | ~7–8 GW [stima] | ~90–120k | C&I totale 1.744 MW (−21%) |
| C&I 200 kW–1 MW | ~10–11 GW [stima] | ~18–25k | (incluso sopra) |
| Utility >1 MW | 13.036 MW | ~2,5–3,5k | +15% (3.412 MW) |

**Età del parco.** Il 52% della potenza cumulata (dato di dicembre 2024) è del 2007–2014 ([SolareB2B revamping 24](https://www.solareb2b.it/newsletter/revamping_24.pdf)). Per numero, invece, circa il 70% degli impianti è successivo al 2014, soprattutto 2020–2025 con Superbonus e scambio sul posto [stima].
- Età mediana per numero: circa 4–5 anni.
- Età mediana per potenza: circa 11–13 anni.

**Batterie in Italia.** A fine 2025 c'erano 884.387 sistemi di accumulo per circa 18 GWh. Nel 2025 sono entrati in esercizio 145.927 sistemi, di cui 145.908 abbinati a fotovoltaico ([Italia Solare accumuli Q4 2025](https://www.italiasolare.eu/wp-content/uploads/2026/02/20260223_report-q4-sistemi-di-accumulo_final.pdf), [Infobuildenergia](https://www.infobuildenergia.it/accumuli-elettrochimici-18-gwh-nel-2025/)).
- Quota sul parco: circa 42% degli impianti ha una batteria [stima: 884k su 2,09 M].
- Quota sui nuovi residenziali 2025: circa 70–75% [stima: 146k su 199k].
- Restano circa 1,2 M impianti senza batteria, cioè un mercato di "upsell" per gli installatori.

### A2. Il segmento Conto Energia (Italia)

- **Dimensione.** Alla chiusura del 6/7/2013 c'erano 531.242 impianti per 18.217 MW. A dicembre 2012 erano 463.746 impianti per 16.104 MW, con un costo di 6,50 mld€ l'anno ([lavoripubblici](https://www.lavoripubblici.it/news/stampa/11706), [contatore GSE](https://www.lavoripubblici.it/news/stampa/10561)).
- **Distribuzione per taglia [stima, da verificare su Atlaimpianti]:**

  | Fascia | N. impianti | Potenza | Peso |
  |---|---|---|---|
  | ≤20 kW | ~85–88% | ~2,5–3 GW | — |
  | 20–200 kW | ~45–55k | ~3,5–4,5 GW | — |
  | 200 kW–1 MW | ~12–15k | ~6–7 GW | — |
  | >1 MW | ~1,5–2k | ~5 GW | — |
  | **Totale >100 kW** | ~20–25k | ~10–12 GW | ~60% della potenza in meno del 5% degli impianti |

- **Tariffe [da verificare].**
  - I e II Conto: 0,36–0,49 €/kWh di premio, più la vendita o l'autoconsumo dell'energia.
  - III e IV Conto: circa 0,13–0,40 €/kWh.
  - V Conto: tariffa omnicomprensiva di circa 0,11–0,21 €/kWh.
- **Scadenze (durata 20 anni).**
  - I Conto: 2026–2028.
  - II Conto (con la coda "salva-Alcoa"): 2027–2031.
  - III e IV Conto: 2031–2032.
  - V Conto: 2032–2033.
  - Gli impianti oltre 200 kW che hanno scelto lo "spalma-incentivi" del 2014 arrivano fino a circa 2034–2037 [da verificare].
- **Prestazioni.** Secondo il GSE, circa 20 GW dell'era Conto Energia hanno una produzione reale del 75% e un degrado reale del 2,2% l'anno. Il GSE ha inviato circa 13.000 comunicazioni di "alerting" a impianti sotto 800 kWp poco performanti ([SolareB2B revamping 23](https://solareb2b.it/newsletter/revamping_23.pdf), [revamping 22](https://www.solareb2b.it/newsletter/revamping_22.pdf)).
- **Inverter.** Gli inverter dell'epoca avevano spesso garanzie di 5 anni e una sostituzione tipica intorno ai 10 anni. I guasti più frequenti: MPPT, fusibili, cavi, sovratensioni di stringa con il freddo ([QualEnergia](https://www.qualenergia.it/articoli/fotovoltaico-e-inverter-residenziale-per-tanti-impianti-pensare-revamping/)).
- **Decreto Bollette 2026 (DL 21/2026).**
  - Gli impianti oltre 20 kW con scadenza dal 2029 potevano scegliere, entro il 31/5/2026, un taglio del premio del 15% o 30% nel 2026–27 in cambio di 3 o 6 mesi di proroga.
  - Dal 2028 è possibile l'uscita anticipata con un corrispettivo, solo a condizione di rifare integralmente l'impianto. Secondo la guida Enpal il corrispettivo è pari al 90% del valore attuale netto (VAN) degli incentivi residui, pagato in 10 rate.
  - Fonti: [Fiscoetasse](https://www.fiscoetasse.com/new-rassegna-stampa/3575-conto-energia-fotovoltaico-aiuti-nel-decreto-bollette.html), [Andersen](https://it.andersen.com/wp-content/uploads/2026/03/NL_Andersen_Energy-in-Action_n.2-2026.pdf), [ARERA 53/2026](https://www.arera.it/fileadmin/allegati/docs/26/53-2026-I-com.pdf), [Enpal guida](https://www.enpal.com/it/fotovoltaico/conto-energia), [PMI.it](https://www.pmi.it/economia/green-economy/500806/uscita-conto-energia-fotovoltaico-corrispettivo-gse.html).
- **Mercato secondario.**
  - Acea ha acquistato circa 25 MWp incentivati per un valore d'impresa di circa 75 M€, cioè circa 3 M€/MW ([QualEnergia](https://www.qualenergia.it/pro/articoli-pro/mercato-secondario-fotovoltaico-acea-acquisisce-impianti-per-25-mw/)).
  - Esistono acquirenti specializzati che comprano impianti di circa 1 MW per poi fare revamping, per esempio LCF Alliance ([QualEnergia](https://www.qualenergia.it/articoli/fotovoltaico-mercato-secondario-perche-vendere-proprio-impianto-incentivato-risultare-conveniente/)).

### A3. Altri Paesi e UE

| Paese | Parco | Note utili per OMBRA |
|---|---|---|
| **Germania** | 117 GW a fine 2025 ([BNetzA](https://www.bundesnetzagentur.de/SharedDocs/Pressemitteilungen/EN/2026/20260108_EEG.html)). 4,80 M impianti a fine 2024 secondo BSW ([factsheet](https://www.solarwirtschaft.de/datawall/uploads/2020/08/bsw_factsheet_solar_pv_eng.pdf)), più circa 1,03 M impianti da balcone a giugno 2025 ([heise](https://heise.de/-10439636)) e circa 430k nuovi balconi nel 2025 | Circa metà della crescita 2025 è sugli edifici. Abbinamento batteria nel residenziale circa 80% ([GTAI](https://www.gtai.de/en/invest/industries/energy/photovoltaic-65800)); accumulo totale 24 GWh ([pv magazine](https://www.pv-magazine.com/2026/01/12/germany-adds-6-57-gwh-of-battery-storage-in-2025-total-hits-24-gwh/)). **Parco EEG 2009–2012** ad alta tariffa (circa 0,19–0,43 €/kWh, ~1 M impianti, ~30 GW, scadenze 2029–2032) **[da verificare]**: è l'analogo tedesco del Conto Energia. Il Solarspitzengesetz (2025) introduce il tetto al 60% e nessuna remunerazione nei quarti d'ora a prezzo negativo; perdite stimate 1,1–9% ([RatedPower](https://ratedpower.com/blog/how-solarspitzengesetz-affects-solar/)). Il curtailment è raddoppiato nel 2024 e di nuovo nel 2025 ([CLEW](https://www.cleanenergywire.org/news/solar-power-curtailment-rise-germany-grid-expansion-lags-behind)) |
| **Paesi Bassi** | Più di 3 M abitazioni con FV (37% del parco abitativo) a fine 2025 ([Zonneplan su CBS](https://www.zonneplan.nl/blog/zonnepanelen-per-gemeente-2026)); circa 28,6 GWp; la maggior parte dei pannelli è su edifici aziendali ([ioplus](https://ioplus.nl/en/posts/most-solar-panels-are-located-at-businesses)) | Lo scambio sul posto (saldering) finisce l'1/1/2027, quindi il kWh esportato vale circa zero. Interessa l'ottimizzazione dell'autoconsumo più che il recupero delle perdite. Segmento debole per OMBRA |
| **Spagna** | Autoconsumo 9,3 GW a fine 2025; +1.139 MW nel 2025; 36.330 nuove case nel 2025 (−17%) ([UNEF via Energías Renovables](https://www.energias-renovables.com/autoconsumo/el-autoconsumo-solar-alcanza-los-9-3-20260129)) | C&I in ripresa; residenziale in calo. Molta polvere: lo sporcamento (soiling) conta |
| **Francia** | 1.347.232 installazioni a fine 2025, 33,0 GW al 31/3/2026 (SDES); il 86% delle nuove installazioni nei primi 9 mesi del 2025 era sotto 9 kW ([Hellowatt](https://www.hellowatt.fr/blog/chiffres-t4-2025-photovoltaique/), [TaiyangNews](https://taiyangnews.info/markets/france-installed-45-gw-solar-pv-capacity-in-9m-2025)) | Contratti di acquisto obbligatorio 2006–2011 con tariffe fino a circa 0,55–0,60 €/kWh per il FV integrato, in scadenza 2026–2031 **[da verificare]**: secondo segmento "tipo Conto Energia" |
| **UE** | 65,1 GW installati nel 2025 (−0,7%); utility per la prima volta oltre il 50%; residenziale circa 14–15% del nuovo; tetti circa 61% della potenza cumulata ([pv magazine](https://www.pv-magazine.com/2025/12/11/eu-installs-65-1-gw-of-solar-in-2025/), [Mercom](https://mercomindia.com/eu-solar-installations-fall-to-65-gw-in-2025-ending-a-decade-of-yearly-growth), [GreentechLead](https://greentechlead.com/solar/eu-solar-market-faces-slowdown-in-2025-2026-2027-solar-power-europe-51622)) | Cumulato circa 400 GW, di cui circa 245 GW su tetto [stima]. Circa 15–18 M impianti su tetto e balcone nella UE [stima]. Calo atteso nel 2026–27 |

---

## B. TUTTI I SEGMENTI DI CLIENTI

Prezzo realistico e numerosità sono **[stima]** dove non c'è fonte.

| # | Segmento | Chi | Problema principale | Cosa pagherebbe | Quanti | Prezzo realistico | Come raggiungerli | Prove di DAP |
|---|---|---|---|---|---|---|---|---|
| 1 | **Impianti Conto Energia 100 kW–1 MW (IT)** | PMI, aziende agricole, società veicolo (SPV) piccole, family office, condomini industriali | Ogni kWh perso vale 0,3–0,45 €; inverter vecchi; garanzie scadute; grandine 2023; scelte del DL 21/2026 (manutenere, fare revamping o uscire dal 2028) | TAC iniziale con perdite in € e cause; monitoraggio continuo; business case del revamping; prove per assicurazioni e garanzie | ~20–25k impianti, ~10–12 GW | TAC 490–2.500 €; 1,5–3 €/kWp l'anno; oppure 10–20% dell'energia recuperata | Atlaimpianti GSE (potenza, località, data) + registro imprese; O&M; ditte di revamping; Italia Solare; Coldiretti e Confagricoltura | Le lettere GSE di alerting dimostrano il problema; contratti O&M già pagati; mercato secondario a ~3 M€/MW; acquirenti che fanno revamping |
| 2 | **Gestori O&M e asset manager di portafogli Conto Energia/C&I** | O&M medi, gestori di SPV, fondi | Margini bassi (utility ~6,7 €/kWp l'anno [mio calcolo da contratto ESPE](https://www.soldionline.it/?p=6843)); troppi allarmi; poche persone | Triage automatico, ticket, report per il proprietario | Qualche centinaio in IT | 0,3–1 €/kWp l'anno; marchio proprio (white-label) | Fiere, LinkedIn, Italia Solare, ANIE | Usano già 3E, meteocontrol, VCOM: il budget esiste |
| 3 | **Installatori** (residenziale e piccolo C&I) | Migliaia di imprese in IT (ICE: >21.000 imprese rinnovabili, dato generico, [ICE](https://www.ice.it/en/my-home/it/settori/energie-rinnovabili/il-settore-delle-energie-rinnovabili)) | Mercato residenziale −28%; servono ricavi ricorrenti; uscite tecniche costose; parco multi-marca | Triage remoto, priorità dei ticket, lead di upsell (batterie, pulizia, ottimizzatori, revamping inverter) | ~2 M impianti residenziali in IT | 0,8–2 € per impianto al mese; minimo 49–99 € al mese | Distributori (VP Solar ecc.), Key Energy, Intersolar, webinar con QualEnergia e SolareB2B | Solytic: ~200k impianti nel 2022, 5 €/sito/mese; servizio Otovo con 3.000 clienti al lancio ([Reuters/TradingView](https://de.tradingview.com/news/reuters.com%2C2025-09-24%3Anewsml_Obihkt57a%3A0-otovo-debuts-service-product-with-3-000-first-customers-signed-up)); Omnidian vende tramite installatori a 300 $ il primo anno |
| 4 | **Proprietari C&I nuovi (post-2014)**: fabbriche, magazzini, supermercati, aziende agricole | Responsabile manutenzione, energy manager, titolare | Nessuno guarda i dati; valore in autoconsumo 0,15–0,22 €/kWh | Allarmi in € e report mensile | ~100k in IT | 300–1.200 € per impianto l'anno | Tramite installatori ed EPC; energy manager; Confindustria e Confagricoltura | Indiretta: domanda di monitoraggio in crescita per gli impianti medio-grandi ([SolareB2B O&M 24](https://www.solareb2b.it/newsletter/O&M_24.pdf)) |
| 5 | **Parchi esteri ad alta tariffa** (DE EEG 2009–12, FR 2006–11) | Privati e aziende agricole (DE), privati (FR) | Come il Conto Energia ma frammentati | Controllo dello stato di salute, monitoraggio | ~1 M (DE) + ~0,3 M (FR) [stima] | 30–80 € l'anno residenziale; 1–2 €/kWp l'anno agricolo | Partner locali, Solarteure, Data Act | Da validare |
| 6 | **Utility, retailer, installatori verticali** (Enel X, Edison, Sorgenia, Octopus, E.ON, Engie, 1KOMMA5°, Enpal, Zolar, Otovo) | Responsabile service/prodotto | Costo del servizio per cliente; fidelizzazione; nel modello a noleggio (Enpal) il rischio di sottoproduzione resta in capo all'azienda | White-label, API di diagnosi | Enpal: >115k famiglie DE+IT, >1 mld€ di ricavi nel 2025 ([pv magazine DE](https://www.pv-magazine.de/2026/01/29/enpal-meldet-erstmals-mehr-als-eine-milliarde-jahresumsatz/)); Otovo >30k clienti | 0,3–1 € per impianto al mese | Vendita enterprise, POC, Intersolar | 1KOMMA5° ha una piattaforma interna (Heartbeat): rischio che scelgano di costruire in casa |
| 7 | **Leasing, PPA, ESCo, fondi con portafogli distribuiti** | Asset manager | Garanzie di prestazione; scostamenti rispetto al business plan | Analisi del portafoglio; due diligence; garanzia di produzione | Decine in UE | 1–3 €/kWp l'anno; due diligence 1–3 k€/MW | Diretto, M&A advisor | Omnidian (USA): ~75.000 impianti, 15 M$ raccolti, garanzia del 100% della produzione di riferimento ([Solar Builder](https://solarbuildermag.com/news/omnidian-raises-new-capital-to-grow-its-residential-solar-pv-performance-guarantee-program/), [Seattle Business](https://www.seattlebusinessmag.com/green/seattle-solar-services-startup-omnidian-raises-15m-fuel-growth)) |
| 8 | **Acquirenti e venditori sul mercato secondario Conto Energia** | Investitori, advisor | Rischio tecnico nascosto | Due diligence desktop automatica | Centinaia di operazioni l'anno [stima] | 1–5 k€ per impianto | Advisor, Milk the Sun, broker | Prezzi a ~3 M€/MW: 1% di gap ≈ 30 k€/MW di valore |
| 9 | **Assicurazioni** (FV, perdita di produzione, grandine) | Liquidatori, prodotto | Grandine 2023 (Lombardia, Veneto, Friuli): compagnie che sospendono le polizze, franchigie in aumento ([SolareB2B grandine 24](https://www.solareb2b.it/newsletter/grandine_24.pdf)); danni invisibili alle celle | Verifica del danno (produzione rispetto all'irraggiamento), antifrode, sottoscrizione del rischio | Decine | 50–200 € per sinistro; 2–5 € per polizza l'anno | Partnership, broker | Prodotti esistenti: Enpal/AIG grandine fino a 20 k€ ([Enpal](https://www.enpal.com/it/garanzie-aig-fotovoltaico-plus)); Arca: grandine al 50% del capitale ([Arca](https://bancafucino.it/sites/default/files/2025-04/Allegato2-Set%20informativoArcaEnergiaFuturo_cod619.pdf)) |
| 10 | **Comunità energetiche (CER)** | Referenti, ESCo, piattaforme | Incentivo sull'energia condivisa: tariffa premio 60–120 €/MWh, +4/+10 €/MWh per Centro e Nord, più ~8–10,6 €/MWh ARERA, per 20 anni; tetto di 5 GW entro fine 2027 ([MASE](https://www.mase.gov.it/sites/default/files/Decalogo-CER.pdf), [Studio Madera](https://studiomadera.it/news/690-comunita-energetiche-2)) | Report per i membri, perdite | Numero di CER non verificato | 100–300 € per impianto l'anno | Piattaforme CER, ESCo | Debole: valore al kWh basso, mercato già servito da piattaforme CER |
| 11 | **Banche e finanziatori green** | Rischio e ESG | Qualità delle garanzie, reportistica ESG | Dati aggregati | Decine | Contratti dati | Partnership | Bassa |
| 12 | **Produttori di moduli e inverter** | Qualità e garanzie | Analisi del parco | Hanno già i loro dati | Pochi | — | — | Molto bassa; anzi, OMBRA aiuta i clienti nei reclami *contro* di loro |
| 13 | **Real estate, condomini, enti pubblici, scuole** | Amministratori, uffici tecnici | Impianti non monitorati | Report | Molti | 100–500 € l'anno | Gare MePA, amministratori | Ciclo lento, burocratico |
| 14 | **Agrivoltaico (PNRR)** | Sviluppatori | Obbligo di monitoraggio | SCADA già previsto | Pochi grandi | — | — | Non adatto (scala utility) |
| 15 | **Portali immobiliari e ispezioni casa** | Portali, periti | Valutare il FV in una compravendita | "Certificato di salute" del FV | ~decine di migliaia di compravendite l'anno con FV [stima] | 49–149 € una tantum | Partnership portali e agenti | Non provata |
| 16 | **Verifica incentivi fiscali** (Transizione 5.0, ecc.) | EGE, certificatori | Certificazione ex-post | Dati di produzione | — | — | — | **Escluso**: il cuore è burocratico |
| 17 | **Famiglie (diretto)** | Proprietari | "Il mio impianto funziona?" | App o report | ~2 M in IT, >10 M in UE | 2–5 € al mese | Pubblicità, SEO | Solar Analytics 60–95 AUD l'anno ([pricing](https://www.solaranalytics.com.au/pricing)); Enphase 9,99 $ al mese ([ConsumerAffairs](https://www.consumeraffairs.com/solar-energy/best-solar-monitoring-systems.html)); Vesta 19,99 $ al mese ([Vesta](https://monitoring.vestahomeenergy.com/)). Ma il valore recuperato è di 40–100 € l'anno e il costo di acquisizione (CAC) è alto |

**Classifica per un fondatore solo** (attrattività da 1 a 5):
1. **Conto Energia 100 kW–1 MW e i loro gestori O&M/asset: 4,5.** € per kWh altissimo, decisori pochi e identificabili, urgenza 2026–2028, ciclo di vendita breve.
2. **Gestori O&M e asset di portafogli: 4.** Pagano già per l'analisi; servono come canale verso il segmento 1.
3. **Due diligence per il mercato secondario e i fondi: 3,5.** Ticket alto e poco supporto, ma volumi bassi.
4. **Installatori (come canale B2B2C): 3,5.** Volume e ricavi ricorrenti, ma prezzo per impianto basso e onboarding pesante.
5. **Parchi ad alta tariffa in Germania e Francia: 3.** Espansione naturale; serve un partner locale.
6. **C&I post-2014: 3.**
7. **Assicurazioni: 2,5.** Buon modulo aggiuntivo, ciclo di vendita lungo.
8. **Utility e verticali in white-label: 2,5 all'inizio, 4 come seconda fase.**
9. **CER: 2.**
10. **Portali immobiliari: 2.**
11. **Famiglie dirette, banche, produttori, enti pubblici, agrivoltaico, verifica fiscale: 1–1,5.**

---

## C. CONCORRENTI

| Player | Target | Cosa fa | Ricostruisce l'ombra o scompone le perdite in €? | Prezzo | Trazione e funding |
|---|---|---|---|---|---|
| **Solytic** (Berlino, ora S.E.E./PV SECURE) | Installatori, piccolo C&I, multi-marca (>40 produttori) | Monitoraggio senza hardware, allarmi, white-label | Parziale (allarmi di prestazione); niente ombre o € per causa | ≤200 kWp: 5 €/sito/mese + 60 € di setup; >200 kWp: 0,02 €/kWp/mese + 0,50 €/kWp; white-label 500 €/mese ([pricing](https://www.solytic.com/pricing/)) | ~200k impianti, 2 M€ raccolti nel 2022 (EWE) ([tech.eu](https://tech.eu/2022/03/16/solytic-heats-up-solar-energy-market-with-eur2-million-for-monitoring-pv-installations)); acquisita ([blog](https://solytic.com/blog/s-e-e-acquires-solytic/)). **È il concorrente più vicino come canale; il suo acquisto da parte di un player O&M/assicurativo indica una via d'uscita possibile per OMBRA** |
| **Solar-Log** (WEB Enerest) | Installatori, C&I | Datalogger hardware + portale | No | Dati 2018: ~70 € l'anno (5 kWp), 250 € (100 kWp), 800 € (500 kWp), 4.000 € (5 MWp) ([confronto](https://www.solytic.com/solar-log-web-enerest-vs-solytic/), [brochure IT](https://www.vpsolar.com/download/catalog/Monitoraggio/Solar-Log/Solar-Log-WEB-Enerest/SolarLog_Brochure_Solar-Log_WEB_Enerest_Monitoring_IT.pdf)) | Base installata ampia nel DACH |
| **meteocontrol VCOM** | C&I e utility | Monitoraggio professionale, controllo impianto | Analisi delle perdite per grandi impianti | Su preventivo, non pubblico | Leader storico in DE |
| **3E SynaptiQ** (BE) | Utility e C&I; FV, eolico, accumulo | Analisi di prestazione, raccomandazioni sul ritorno economico | Sì per grandi impianti, con modello di resa attesa | Su preventivo | >20 GW connessi; partnership con BayWa r.e. su 10 GW ([fonte](https://rejobs.org/en/renewable-energy-jobs/121217-junior-saas-engineer-3e)) |
| **Power Factors (Drive), Clir** | Utility | Gestione asset ad alta prestazione | Sì, scala utility | Enterprise | Grandi **[da verificare]** |
| **Raycatch DeepSolar** (IL) | Utility | Diagnosi IA dai soli dati, perdite per causa | Sì, utility | — | 4,5 M$ (DSM, BayWa); **asset venduti a BladeRanger nel 2022 per circa 1,5 M$** ([Shibolet](https://www.shibolet.com/en/representation-of-blade-ranger-in-purchasing-the-assets-and-activities-of-raycatch/), [CB Insights](https://www.cbinsights.com/company/raycatch)). Segnale: la "diagnosi solo da dati" per utility ha faticato a monetizzare |
| **SmartHelio** (CH) | C&I e utility, mercati emergenti | IA: ombreggiamento, connettori, corrosione | Parziale | — | ~8 M$ totali, 30 progetti pilota ([Venture Kick](https://www.venturekick.ch/SmartHelio-wins-CHF-150000-to-optimize-solar-plant-performance-through-AIdriven-analytics), [TechCrunch](https://techcrunch.com/2022/12/14/smarthelio-predictive-maintenance/)) |
| **SunSniffer** (DE) | C&I | Sensori a livello di modulo (hardware) | Per modulo, ma con hardware | ~1 c€/Wp ([sito](https://www.sunsniffer.de/en/why-module-precise/improve-roi)) | Di nicchia |
| **SolarEdge, Enphase** | Residenziale | Dati per modulo, allarmi integrati | Vedono il modulo ombreggiato ma solo sul proprio hardware; niente € per causa **[da verificare]** | Enphase premium ~9,99 $ al mese | Quota grande ma mono-marca |
| **Huawei FusionSolar** | Tutti | Arco elettrico con IA, curva I-V intelligente (utility, accuratezza >95%) ([pv-tech](https://www.pv-tech.org/products/huaweis-next-gen-fusionsolar-residential-smart-pv-solution-aims-for-100-self-consumption), [CleanTechnica](https://cleantechnica.com/2020/08/12/huawei-showcases-ai-powered-smart-pv-solution-at-snec-2020/)) | Diagnostica forte ma mono-marca; rischio regolatorio | Incluso | Primo per quota inverter in UE |
| **Solarman, SolisCloud, eSolar (Sinapsi)** | Installatori | Portali multi-marca o del datalogger | No | Spesso gratis o incluso ([Solarman](https://www.solarmanpv.com/pv-monitoring-companies-classification-and-comparison), [eSolar](https://www.qualenergia.it/news-dalle-aziende/20161124-monitoraggio-fotovoltaico-online-il-sito-di-esolar-di-sinapsi/)) | Abituano al "monitoraggio gratis" |
| **GSE (alerting + Performance Platform)** | Impianti incentivati: alerting sotto 800 kWp, piattaforma da 800 kWp in su | Segnala sottoproduzione | No (né causa né €) | Gratis | ~13.000 lettere. **Concorrente gratuito ma anche validazione del problema** |
| **Solar Analytics** (AU), **Omnidian** (USA) | Famiglie, proprietari di asset | Monitoraggio consumer; garanzia di prestazione | Omnidian: produzione di riferimento con rimborso | 60–95 AUD l'anno; 300 $ il primo anno | Modelli di riferimento per DAP |
| **Solarwatt, Kiwigrid, Enode** | Ecosistemi e API | Gestione energia, piattaforma IoT, aggregatore di API | No; Enode è un possibile partner per le integrazioni | — | — |
| **Italiani** (Comal, Alectris, Elettrostudio, O&M degli installatori) | Utility e C&I (O&M) | Servizi O&M con piattaforme proprie (es. ACTIS di Alectris) **[da verificare]** | Non risultano offerte multi-marca con scomposizione in € per il residenziale | — | Possibili **partner o clienti**, non concorrenti diretti |
| **Open source e ricerca** | — | pvlib, RdTools (NREL), PVPRO (LBNL), profilazione dell'orizzonte da serie storiche (Sandia), ricostruzione dell'irraggiamento da dati FV ([Sandia](https://www.sandia.gov/research/publications/details/horizon-profiling-methods-for-photovoltaic-arrays-2023-01-01/), [arXiv](https://web3.arxiv.org/pdf/1706.06878v1)) | I metodi esistono | Gratis | Barriera tecnica bassa: il vantaggio difensivo non è l'algoritmo |
| **Brevetti USA** (es. US 10,962,576 "Estimation of shading losses… from measured and modeled inputs", [USPTO](https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/10962576)) | — | Stima delle perdite da ombra confrontando produzione misurata e modellata | — | — | Rischio solo per gli USA; titolare probabilmente nell'area Locus Energy/AlsoEnergy **[da verificare]** |

Sugli altri nomi richiesti: "Wattsight" (Montel) fa previsioni di prezzo e meteo, non monitoraggio FV, quindi non è un concorrente. Per "Bluesolar" non ho trovato un prodotto di analisi con questo nome (forse è BlueSol, software di progettazione). Above Surveying è un servizio di ispezione con droni per grandi impianti **[da verificare]**.

**Il vuoto di mercato.** Non ho trovato nessuno che offra **per impianti multi-marca residenziali e piccolo C&I**:
- ricostruzione dell'orizzonte e degli ostacoli dai soli dati di produzione più satellite;
- scomposizione per causa (ombra, sporcamento, stringhe, degrado, clipping, curtailment, fermi) **in euro con la tariffa reale dell'impianto** (Conto Energia, tariffa CER, autoconsumo);
- ticket automatici.

Il vantaggio difensivo non è l'algoritmo. Sta in tre cose:
1. la libreria di tariffe e regole italiane (Conto Energia, scambio sul posto, ritiro dedicato, CER);
2. la distribuzione;
3. il dataset proprietario di casi etichettati.

---

## D. VALORE PER OGNI CLIENTE (QUANTIFICATO)

### D1. Quanta energia si perde (studi)

| Studio | Risultato |
|---|---|
| COST PEARL PV: >8.400 impianti, soprattutto residenziali in UE (BE) | Performance ratio medio 76,7%; perdita di prestazione −0,74/−0,86% l'anno ([UTwente](https://research.utwente.nl/en/publications/performance-analysis-and-degradation-of-a-large-fleet-of-pv-syste/)) |
| GSE sul parco Conto Energia (~20 GW) | Produzione reale 75%; degrado reale 2,2% l'anno ([SolareB2B](https://solareb2b.it/newsletter/revamping_23.pdf)) |
| UK domestico (Firth, 2010) | Perdite per guasti tra 3,6% e 18,9% ([Loughborough](https://dspace.lboro.ac.uk/2134/6153)) |
| NREL, 250 impianti | Indisponibilità degli inverter: −2,3% in media, ~8% nei primi 6 mesi ([NREL](https://research-hub.nrel.gov/en/publications/pv-fleet-performance-data-initiative-performance-index-based-anal/)) |
| Sporcamento in Europa | 0,9% con pulizia perfetta da pioggia, fino a 5,3% con pioggia poco efficace; costo dell'energia (LCOE) +4/+15% ([Renewable Energy](https://ideas.repec.org/a/eee/renene/v178y2021icp420-428.html)) |
| Germania, Solarspitzengesetz | Perdite da tetto al 60%: 1,1% (est-ovest) fino a 9% (sud senza batteria) ([RatedPower](https://ratedpower.com/blog/how-solarspitzengesetz-affects-solar/)) |
| UNSW, 1.089 impianti australiani | Classificazione automatica della sottoproduzione con accuratezza 88–92% ([pv magazine AU](https://www.pv-magazine-australia.com/?p=9349)) |

**Ipotesi di lavoro [stima]:** la perdita *evitabile e recuperabile* grazie a una diagnosi tempestiva è del 2–5% della resa l'anno, fino al 10–20% negli impianti con guasti non rilevati (stringhe spente, inverter fermi per settimane).

### D2. Valore di un kWh per segmento [stima, salvo dove indicato]

| Segmento | €/kWh perso |
|---|---|
| Residenziale IT nuovo (40% autoconsumo a ~0,27 €, resto ritirato a ~0,10 €) | ~0,17 |
| C&I IT (70% autoconsumo a ~0,20 €) | ~0,17 |
| CER: tariffa premio + ARERA sulla quota condivisa, più l'energia | ~0,12 incentivo + energia |
| **Conto Energia II–IV** (premio 0,25–0,45 € + energia ~0,10 €) | **0,35–0,55** |
| Conto Energia V (omnicomprensiva) | 0,11–0,21 |
| Germania nuovo (35% autoconsumo a 0,38 €, immissione a ~0,08 €) | ~0,18 |
| Germania EEG 2010 | ~0,39 |
| Francia contratti 2006–2010 integrati | ~0,55–0,60 |
| Paesi Bassi dopo il 2027 (esportazione) | ~0–0,05 |

### D3. Euro recuperati per impianto all'anno [stima]

| Impianto tipo | Produzione | Valore annuo | 1% vale | Recupero 3–5% |
|---|---|---|---|---|
| Residenziale IT 6 kW nuovo | 7.800 kWh | ~1.330 € | 13 € | **40–65 €** |
| Residenziale Conto Energia 3 kW (2009–10) | 3.600 kWh | ~1.900 € | 19 € | **60–100 €** |
| C&I IT 200 kW nuovo | 260 MWh | ~44 k€ | 440 € | **1,3–2,2 k€** |
| **Conto Energia 200 kW IV Conto (2011)** | 260 MWh | ~104 k€ | 1.040 € | **3,1–5,2 k€** |
| **Conto Energia 1 MW a terra II Conto (2010, Sud)** | 1.400 MWh | ~630 k€ | 6.300 € | **19–31 k€** |
| Germania EEG 2010, 10 kW | 9.000 kWh | ~3,5 k€ | 35 € | 105–175 € |
| **Intero parco Conto Energia (~18 GW, ~21–22 TWh)** | — | ~6,5 mld€ incentivo + energia | **~80 M€/anno** | 240–400 M€/anno |

### D4. Altri vantaggi per tipo di cliente

- **Installatori** [stima], esempio con 1.500 impianti:
  - Circa 150 chiamate l'anno al 10%; ogni uscita tecnica costa 150–250 €.
  - Il triage remoto ne evita il 25–35%, cioè 6–13 k€ l'anno.
  - Upsell: 1% di batterie in retrofit = 15 vendite × ~1,5 k€ di margine = 22 k€. Ci sono circa 1,2 M impianti in Italia senza accumulo.
  - Contratti O&M: 5% × 150 € l'anno = ~11 k€ di ricavi ricorrenti.
  - Altro: pulizia, potatura alberi (OMBRA identifica l'ostacolo e il suo costo in € l'anno, un argomento di vendita fortissimo), ottimizzatori, revamping degli inverter a fine vita.
  - **Valore totale ~40–55 k€ l'anno, contro un costo di OMBRA di 15–25 k€ l'anno.**
- **Proprietari Conto Energia:**
  - Recupero di produzione (vedi D3).
  - Prove per i reclami in garanzia (degrado oltre la curva garantita).
  - Prove per i sinistri da grandine e i danni invisibili alle celle ([3S memorandum](https://www.3s-solar.swiss/hubfs/25212269/MB_D_Memorandum-Danni_invisibili-da-grandine_IT_2023-01.pdf?hsLang=it)).
  - **Business case "revamping o uscita anticipata 2028"** per il DL 21/2026.
  - Nel revamping, il passaggio a tracker vale fino a +16% di produzione al Sud ([SolareB2B](https://solareb2b.it/newsletter/revamping_23.pdf)).
- **Fondi, acquirenti, venditori:** a circa 3 M€/MW, ogni 1% di produzione recuperabile vale circa 30 k€/MW di valore. Una due diligence che trova un 5% evitabile vale circa 150 k€/MW di prezzo negoziato.
- **Assicurazioni:**
  - Quantificazione oggettiva dei kWh persi dopo grandine o tempesta, confrontando produzione e irraggiamento satellitare.
  - Antifrode (danno dichiarato senza perdita di produzione).
  - Punteggio di rischio per la sottoscrizione.
- **Utility e verticali:**
  - Meno uscite tecniche.
  - Rispetto degli obblighi di prestazione nei modelli a noleggio o abbonamento (Enpal, Otovo).
  - Fidelizzazione: un report mensile "in €" per il cliente.
- **CER:** massimizzazione dell'energia condivisa incentivata e report ai membri. Valore basso.

---

## E. PREZZI E MODELLO DI RICAVO

**Cosa pagano oggi i clienti:**

| Riferimento | Prezzo |
|---|---|
| Solytic, impianti ≤200 kWp | 5 €/sito/mese (60 € l'anno) |
| Solytic, impianti >200 kWp | 0,24 €/kWp l'anno |
| Solar-Log (dati 2018) | ~14 €/kWp l'anno a 5 kWp; 2,5 € a 100 kWp; 1,6 € a 500 kWp; 0,8 € a 5 MWp |
| O&M completo utility | ~6,7 €/kWp l'anno [mio calcolo da contratto ESPE] |
| O&M piccolo C&I | 10–20 €/kWp l'anno [stima] |
| Consumer | Solar Analytics 60–95 AUD l'anno; Enphase ~120 $ l'anno; Omnidian 300 $ il primo anno |
| Hardware per modulo | SunSniffer ~10 €/kWp |

**Listino proposto per OMBRA [stima]:**

| Prodotto | Prezzo |
|---|---|
| **TAC Conto Energia** (una tantum: 12–24 mesi di dati, perdite per causa in €, piano d'azione) | 490 € (<100 kWp) · 990 € (100–500 kWp) · 1.900–2.500 € (>500 kWp) |
| **Monitoraggio Conto Energia/C&I** | 1,5–3 €/kWp l'anno (minimo 300 € l'anno), oppure 10–20% del valore recuperato certificato |
| **Installatori** | 1,0–1,5 € per impianto residenziale al mese, 0,5–1 €/kWp l'anno per il C&I; minimo 79 € al mese |
| **Due diligence per il secondario** | 1–3 k€/MW |
| **White-label enterprise** | 0,3–0,8 € per impianto al mese con minimo garantito |
| **Commissione sul revamping** (verso EPC e O&M partner) | 2–5% del contratto (es. 50–150 k€ → 1–7 k€) |
| **Modulo assicurativo** | 50–150 € per verifica di sinistro |

**Scenari:**

| Scenario | Composizione | Ricavi |
|---|---|---|
| **S1 – Conto Energia prima di tutto (solo IT)**, obiettivo 300–500 k€ | 500 impianti × 350 kWp × 2 €/kWp = 350 k€ di ricavo ricorrente (175 MW, circa 1% del Conto Energia) + 120 TAC o due diligence × 1,5 k€ = 180 k€ + 10 commissioni × 3 k€ = 30 k€ | **~560 k€**, con 150–300 account (molti clienti hanno più impianti) |
| S1 portato a 1 M€ | 900 impianti (~315 MW) = 630 k€ + 200 report = 300 k€ + commissioni 100 k€ | **~1,03 M€**. È un tetto naturale: il segmento si esaurisce verso il 2031–33 |
| **S2 – Canale installatori (IT + DE)** | 40 installatori × 700 impianti × 1,2 €/mese = 403 k€; per arrivare a 1 M€ servono ~100 installatori (70k impianti) | 0,4–1 M€, ma il supporto è pesante e incompatibile con 5–10 ore a settimana senza molta automazione |
| **S3 – Mix (consigliato come traiettoria)** | 250 impianti Conto Energia (150 k€) + 30 installatori × 500 impianti (216 k€) + report (100 k€) + 1 white-label da 40k impianti × 0,8 € (384 k€) | **~850 k€**; oltre 1 M€ con Germania (EEG 2009–12) e Francia |

**Mercato aggredibile (SAM) [stima]:**
- Conto Energia >100 kW: ~10–12 GW × 2 €/kWp = **20–24 M€ l'anno**. Una quota del 2–5% vale 0,4–1,2 M€.
- Installatori in IT: ~2 M impianti × 12–18 € l'anno = 24–36 M€.

---

## F. COME ARRIVARE AL MERCATO (FONDATORE SOLO)

1. **Liste mirate da Atlaimpianti (GSE).** La mappa pubblica mostra potenza, località e data di esercizio [livello di dettaglio da verificare]. Si incrociano con registro imprese, LinkedIn e PEC. Va contattato solo chi è un'azienda, per il GDPR.
   - Esca: "**TAC gratuita** sul tuo impianto: quanti € perdi e perché".
   - Dati necessari: export dell'inverter (Sunny Portal, Aurora Vision/FIMER, Fronius, Huawei, SolarEdge) oppure curve del contatore.
2. **Partner O&M e revamping.** OMBRA porta lead qualificati (impianti che perdono X € l'anno) e incassa una commissione. Il partner esegue l'intervento sul campo, quindi resta zero servizio a carico di Lorenzo.
3. **Associazioni:** Italia Solare, ANIE Rinnovabili, Elettricità Futura; per l'agricolo Coldiretti, Confagricoltura e CIA (molti tetti di stalle del 2010–11).
4. **Fiere:** Key Energy Rimini (novembre), Intersolar/The smarter E Monaco (giugno). Meglio da visitatore con demo su tablet: costo di 1–3 k€ invece di uno stand da 15–30 k€.
5. **Media di settore:** webinar o studio "Quanto perde il Conto Energia: analisi di N impianti" su QualEnergia e SolareB2B. È anche un contenuto forte di PR.
6. **Integrazioni dati:**
   - API dei principali marchi (Huawei, SMA, Fronius, SolarEdge, Sungrow, GoodWe, Solis, FIMER/ABB) oppure un aggregatore (Enode).
   - Flussi di consenso basati sul **Data Act**: il proprietario autorizza la condivisione verso OMBRA.
   - Dati meteo e irraggiamento gratuiti: CAMS, PVGIS, Open-Meteo.
7. **Installatori come seconda fase:** tramite i distributori (VP Solar, ecc.) con un piano "fleet triage" a prezzo per impianto.

**CAC stimato [stima]:**

| Canale | CAC | Valore cliente (LTV) | Rapporto LTV/CAC |
|---|---|---|---|
| Proprietario Conto Energia (outbound + TAC gratis) | 400–900 € per account pagante | ~3,5–6 k€ (5 anni, più report) | ~5x |
| Gestore O&M o asset | 1–3 k€ | 10–50 k€ | Buono |
| Installatore | 800–2.000 € | 15–40 k€ se resta | Buono ma lento: l'adozione dentro il parco è graduale |
| Famiglia B2C | 60–150 € | 60–150 € | ~1x, **da evitare** |
| Enterprise / white-label | 10–30 k€ (POC, 6–12 mesi) | Alto | Seconda fase |

**Primo segnale di mercato con ≤20 k€ (circa 12 settimane):**
- **Settimane 1–6:** prodotto minimo (MVP) con pvlib + CAMS/PVGIS, caricamento CSV e 2–3 API, ricostruzione dell'orizzonte dai residui rispetto al cielo sereno, report PDF in €.
- **Settimane 4–12:** 1.000 impianti Conto Energia da 100 kW a 1 MW in 2–3 regioni (es. Puglia, Emilia-Romagna, Veneto), contattarne 300.
- **Obiettivi:** 30 TAC gratuite, 10 TAC pagate (490–990 €), 3 abbonamenti, 2 accordi di commissione con O&M.
- **Budget:** circa 8–12 k€ (dati e strumenti 1–2 k€, legale per contratti di trattamento dati e condizioni 2 k€, outbound e telemarketing freelance 3–5 k€, fiera 1–2 k€, riserva).
- **Criterio di stop:** meno di 5 TAC pagate su 300 contatti.

---

## G. RISCHI

| Rischio | Prob. | Impatto | Mitigazione |
|---|---|---|---|
| **Produttori che restringono le API** (limiti di chiamate, API a pagamento, accesso solo per installatore) | Media | Alto | Più fonti dati (CSV, contatore, aggregatori come Enode); Data Act: dal 12/9/2025 l'utente ha diritto di accesso e condivisione; dal 12/9/2026 obbligo di accesso by design per i nuovi prodotti; sanzioni fino a 20 M€ o 4% del fatturato ([Enode](https://enode.com/blog/the-eu-data-act-what-the-energy-industry-needs-to-know-before-september-12), [Innobu](https://www.innobu.com/en/articles/data-act-2025-energy-utilities-iot-manufacturers.html), [Bird&Bird](https://twobirds.com/en/insights/2024/global/how-the-eu-data-act-is-accelerating-the-digital-transformation-of-the-energy-sector)). Il compenso chiesto dai produttori a una PMI destinataria dei dati è limitato ai costi **[da verificare]** |
| **Restrizioni sugli inverter cinesi** (Lituania: niente accesso remoto dei fornitori "ad alto rischio" sopra 100 kW, dal 2025–26; proposta UE di "Inverter Security Toolbox") ([pv-tech](https://pv-tech.org/lithuania-to-block-chinese-inverters-with-cybersecurity-legislation), [PV Europe](https://www.pveurope.eu/inverter/lithuania-takes-lead-cybersecurity-solar), [Mercom](https://mercomindia.com/eu-lawmakers-want-chinese-solar-inverters-restricted-on-security-concerns)) | Media | Medio | Anche un'**opportunità**: monitoraggio indipendente UE e lettura locale via Modbus o contatore |
| **IA integrata dei produttori di inverter** (Huawei, SolarEdge, Enphase) | Alta | Medio | Funziona su una sola marca; i parchi degli installatori e del Conto Energia sono multi-marca e con hardware legacy; il calcolo in € con la tariffa reale non è nel loro interesse |
| **Bassa DAP delle famiglie** | Alta | Alto se le famiglie fossero il target | Non vendere al consumatore; passare per gli installatori |
| **Dati legacy del Conto Energia** (datalogger morti, inverter FIMER/ex-ABB, Santerno) | Alta | Alto | TAC su dati mensili e del contatore; logger economico tramite partner; curve di misura dal portale del distributore o lettura del contatore (Chain2) **[da verificare]** |
| **Finestra limitata** (incentivi in scadenza 2026–33; DL 21/2026) | Certa | Medio | Le decisioni di revamping e uscita 2027–28 sono un picco di domanda; poi convertire in clienti C&I post-incentivo; espansione in Germania e Francia |
| **Responsabilità per una diagnosi errata** (uscita tecnica inutile) | Media | Medio | Report "advisory" con probabilità e confidenza, limiti contrattuali, assicurazione RC professionale, nessuna garanzia di produzione (o solo con un partner assicurativo) |
| **Privacy e GDPR** (le curve di produzione e consumo sono dati personali per le famiglie) | Media | Medio | Hosting UE, contratto di trattamento dati con l'installatore come titolare, minimizzazione dei dati, outbound solo a persone giuridiche |
| **Copiabilità** (Solytic, Solar-Log, 3E possono aggiungere la funzione) | Media | Medio | Velocità, nicchia italiana (tariffe, regole GSE), dataset etichettato, rete di partner per il revamping; una possibile uscita è la vendita a uno di loro |
| **GSE alerting gratuito** | Certa | Basso | Il GSE segnala, OMBRA spiega causa, € e azione |
| **Mercato in calo** (residenziale IT −28%, UE in calo nel 2026–27) | Alta | Medio | OMBRA vende sul parco installato, non sulle nuove installazioni; il calo spinge gli installatori a cercare ricavi da servizio |
| **Brevetti USA sulla stima delle perdite da ombra** | Bassa in UE | Basso | Restare in UE, verificare la libertà d'uso prima di andare negli USA |

---

## SCORECARD

| Criterio | Voto | Motivazione |
|---|---|---|
| **Dolore** | **3/5** | Alto (4) per Conto Energia e proprietari di asset: ogni kWh vale 0,35–0,55 € e il GSE stesso segnala sottoproduzione. Basso (2) per famiglie e installatori, che percepiscono poche decine di € per impianto. |
| **Mercato** | **4/5** | 2,09 M impianti e 43,5 GW in IT; ~18 GW Conto Energia con ~6,5 mld€ l'anno di incentivi; oltre 15 M impianti su tetto in UE. Ma il SAM monetizzabile realistico è di circa 50–100 M€ l'anno. |
| **Margine** | **4/5** | Software puro con margine lordo dell'80–90%; dati di irraggiamento gratuiti (CAMS, PVGIS). I costi veri sono le integrazioni e il supporto dati legacy. |
| **Solo 1M** | **3/5** | 300–500 k€ plausibili con 150–300 account B2B Conto Energia più commissioni. 1 M€ richiede un canale (installatori o white-label) o un secondo Paese e un'automazione spinta dell'onboarding; le 5–10 ore a settimana sono a rischio. |

---

## VERDETTO: IL MIGLIOR CUNEO DI INGRESSO

**"OMBRA Conto Energia": impianti italiani incentivati da 100 kWp a 1 MWp (circa 20–25k impianti, circa 10–12 GW) e i loro gestori O&M o asset.**

1. **Perché.** Il valore per kWh è 2–3 volte quello di qualunque altro segmento. I decisori sono pochi, sono aziende (quindi niente problemi GDPR) e sono identificabili da dati pubblici GSE. Il dolore è certificato dal GSE stesso (75% di produzione reale, 13.000 lettere). C'è un evento che obbliga a decidere: il DL 21/2026 con l'uscita dal 2028 condizionata al rifacimento, più garanzie scadute e grandine.
2. **Offerta.**
   - TAC una tantum (490–2.500 €) con perdite per causa in € e business case "manutenere, fare revamping o uscire".
   - Poi monitoraggio a 1,5–3 €/kWp l'anno.
   - Commissioni dai partner di revamping e O&M: zero servizio sul campo per Lorenzo.
3. **Espansione.**
   - (a) Due diligence per il mercato secondario e i fondi.
   - (b) Installatori come canale multi-marca per residenziale e piccolo C&I.
   - (c) Parchi ad alta tariffa in Germania (EEG 2009–12) e Francia (2006–11).
   - (d) White-label per utility e verticali (Sorgenia, Edison, Otovo, Enpal).
4. **Da evitare all'inizio:** famiglie dirette, CER, banche, produttori, verifica degli incentivi fiscali (burocrazia).

---

### Fonti principali (oltre a quelle citate nel testo)
[GSE Rapporto 2024](https://www.gse.it/documenti_site/Documenti%20GSE/Rapporti%20statistici/Solare%20Fotovoltaico%20-%20Rapporto%20Statistico%202024.pdf) · [GSE Rapporto 2023](https://gse.it/documenti_site/Documenti%20GSE/Rapporti%20statistici/Solare%20Fotovoltaico%20-%20Rapporto%20Statistico%202023.pdf) · [Italia Solare Q4 2025](https://www.italiasolare.eu/wp-content/uploads/2026/02/20260130_report-q4-fotovoltaico_final-1.pdf) · [QualEnergia dati 2025](https://www.qualenergia.it/articoli/dati-2025-fotovoltaico-italia-solare/) · [Italia Solare accumuli](https://www.italiasolare.eu/wp-content/uploads/2026/02/20260223_report-q4-sistemi-di-accumulo_final.pdf) · [Conto Energia, chiusura 2013](https://www.lavoripubblici.it/news/stampa/11706) · [SolareB2B revamping 2023](https://solareb2b.it/newsletter/revamping_23.pdf) · [SolareB2B revamping 2024](https://www.solareb2b.it/newsletter/revamping_24.pdf) · [SolareB2B revamping 2025](https://www.solareb2b.it/newsletter/revamping_25.pdf) · [Fiscoetasse DL Bollette](https://www.fiscoetasse.com/new-rassegna-stampa/3575-conto-energia-fotovoltaico-aiuti-nel-decreto-bollette.html) · [BNetzA 2025](https://www.bundesnetzagentur.de/SharedDocs/Pressemitteilungen/EN/2026/20260108_EEG.html) · [pv magazine UE 2025](https://www.pv-magazine.com/2025/12/11/eu-installs-65-1-gw-of-solar-in-2025/) · [Hellowatt FR](https://www.hellowatt.fr/blog/chiffres-t4-2025-photovoltaique/) · [UNEF/Energías Renovables](https://www.energias-renovables.com/autoconsumo/el-autoconsumo-solar-alcanza-los-9-3-20260129) · [Zonneplan/CBS](https://www.zonneplan.nl/blog/zonnepanelen-per-gemeente-2026) · [Solytic pricing](https://www.solytic.com/pricing/) · [Solar Analytics](https://www.solaranalytics.com.au/pricing) · [Omnidian](https://solarbuildermag.com/news/omnidian-raises-new-capital-to-grow-its-residential-solar-pv-performance-guarantee-program/) · [Raycatch/BladeRanger](https://www.shibolet.com/en/representation-of-blade-ranger-in-purchasing-the-assets-and-activities-of-raycatch/) · [Enode Data Act](https://enode.com/blog/the-eu-data-act-what-the-energy-industry-needs-to-know-before-september-12) · [pv-tech Lituania](https://pv-tech.org/lithuania-to-block-chinese-inverters-with-cybersecurity-legislation) · [SolareB2B grandine](https://www.solareb2b.it/newsletter/grandine_24.pdf) · [MASE CER](https://www.mase.gov.it/sites/default/files/Decalogo-CER.pdf) · [Sandia orizzonte](https://www.sandia.gov/research/publications/details/horizon-profiling-methods-for-photovoltaic-arrays-2023-01-01/) · [Sandia, valore economico della mitigazione delle perdite](https://sandia.gov/research/publications/details/the-economic-value-of-photovoltaic-performance-loss-mitigation-in-electrici-2022-09-03) · [Enpal ricavi 2025](https://www.pv-magazine.de/2026/01/29/enpal-meldet-erstmals-mehr-als-eine-milliarde-jahresumsatz/) · [Enpal leader UE 2024](https://www.solarserver.de/2025/08/28/europaeischer-photovoltaik-markt-2024-enpal-bleibt-marktfuehrer/)

**Dati da verificare per primi, nelle fonti primarie:**
- distribuzione per taglia del Conto Energia (Atlaimpianti / open data GSE);
- tariffe e scadenze per singolo Conto;
- dimensione del parco EEG 2009–12 in Germania e dei contratti 2006–11 in Francia;
- numero di CER attive;
- disponibilità delle curve di produzione al quarto d'ora per i produttori in bassa tensione.
