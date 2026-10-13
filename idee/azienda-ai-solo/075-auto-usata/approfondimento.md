# 075 · Analisi AI dell'auto usata: approfondimento

**Data:** 13 ottobre 2026
**Numeri:** `economia.py` (economia per cliente, CAC sostenibile, strada verso 1 M€).
**Nota sul nome:** "perizia" è un termine professionale; il prodotto va chiamato "analisi" o "verifica" dell'annuncio.

---

## 0. Sintesi

| Domanda | Risposta breve |
|---|---|
| **C'è mercato?** | Sì: **3,22 M di passaggi di proprietà** nel 2025 in Italia (record), prezzo medio dell'usato **21.270 €**, chi compra spende in media 20.000 €. Si paga già: carVertical ~24 € a report (75,8 M€ di ricavi nel 2025), visura PRA ~6 €, quotazione Quattroruote 3,99 € |
| **Cosa c'è già (gratis)?** | **Molto.** AutoScout24 mette etichette "Super / Ottimo / Buon prezzo" sui suoi annunci. alVolante con Subito Motori (giugno 2026) pubblica quotazioni per 2.000 modelli con i km medi. Il Portale dell'Automobilista mostra gratis i km all'ultima revisione |
| **Allora cosa vendiamo?** | Non il "prezzo giusto" (è ormai gratis) ma **la decisione completa su un annuncio preciso**, su qualsiasi sito: prezzo, rischi, costi veri, domande, quanto offrire. È la sintesi che oggi richiede 5 siti e un amico esperto |
| **Il rischio più grande** | **I dati.** Chi li ha (AutoScout24, Subito) è anche il concorrente, e lo scraping dei portali è vietato. Senza dati propri il prezzo è più debole di quello dei portali |
| **Economia** | Contribuzione ~13 € per pagante. Con la sola pubblicità su Google si va in pari solo se il clic costa ≤ 0,30–0,60 € e almeno il 4–6% dei visitatori paga. **Serve traffico organico** (contenuti, SEO, passaparola) |
| **1 M€?** | Servirebbe il **2–3% dei passaggi di proprietà italiani** (65–95.000 paganti l'anno): ambizioso. Con Spagna e Germania lo stesso 1% vale ~3,7 volte l'Italia |
| **Scheda v2** | Scende da 4,20 a **3,75**: passa ancora, ma la concorrenza gratuita e il problema dei dati pesano |

**Raccomandazione:** non partire dal codice. Fai un **test concierge di 2–3 settimane (≤ 300 €)**: 20–30 analisi vere, fatte con strumenti semi-manuali, vendute a 9,90 € a chi sta comprando un'auto. Misura se pagano, se il report cambia la trattativa e quanto costa trovarli.

---

## 1. Il mercato

| Dato | Valore | Fonte |
|---|---|---|
| Passaggi di proprietà di auto usate, Italia 2025 (al netto delle minivolture) | **3.221.145** (+2,1%, record) | ACI tramite AutoScout24 |
| Rapporto usato/nuovo | 208 usate ogni 100 nuove | ACI |
| Prezzo medio delle usate su AutoScout24 | **21.270 €** (−3,4% sul 2024; +39,8% sul pre-pandemia) | AutoScout24, Europa Report 2025 |
| Budget medio per l'acquisto | 20.000 € (+11%) | Osservatorio AutoScout24 |
| Annunci su Subito Motori | ~500.000 al giorno | alVolante |
| Auto con km scalati in Italia | 3–11% secondo le fonti (in media ~70.000 km cancellati) | carVertical (fonte interessata) |
| Spagna 2025 | 2,16 M di transazioni (+4,4%) | Autovista24 su dati GANVAM |
| Germania, primo semestre 2025 | 3,27 M di transazioni (~6,5 M l'anno, stima) | Autovista24 su dati KBA |

**Perché le persone pagherebbero:** una decisione da ~20.000 € presa di rado (ogni 5–8 anni), con poca competenza e paura della fregatura. Spendere 10–20 € per decidere meglio è nulla rispetto a uno sconto di qualche centinaio di euro o a una truffa evitata.

**Quota dei privati:** non ho trovato un dato affidabile sulla ripartizione tra vendite tra privati e vendite da concessionario. Conta, perché le analisi servono di più nelle vendite tra privati (niente garanzia).

---

## 2. Concorrenti e strumenti già esistenti

| Cosa | Chi | Prezzo | Cosa non fa |
|---|---|---|---|
| Etichetta "Super / Ottimo / Buon prezzo" | AutoScout24 (su marca, modello, anno, alimentazione, potenza, km, cambio, optional) | Gratis | Solo sui suoi annunci; niente rischi, costi o trattativa |
| Quotazioni per modello e anno, con km medi | alVolante + Subito Motori (dal 10/6/2026) | Gratis online | Valori medi, non l'annuncio specifico |
| Quotazione professionale | Quattroruote (3,99 €), Eurotax / Autovista (B2B, API in Italia) | Pochi € | Solo prezzo |
| Storico del veicolo (km, incidenti, furti, valore) | carVertical | ~24 € | Non dice se conviene né come trattare |
| Km all'ultima revisione | Portale dell'Automobilista (MIT), app iPatente, KM VERI, KMSICURO | Gratis | Solo l'ultima revisione (dal 6/2018); niente sotto i 4 anni |
| Fermi amministrativi e ipoteche | Visura PRA (ACI) | ~6 € | Solo lo stato giuridico |
| Prezzo stimato dall'annuncio con AI | Carvago (UE, ±2% dichiarato), PriceGuru (app italiana) | — | Solo prezzo |
| Assistente AI che analizza un annuncio | Avturo (USA, inglese) | — | Non in Italia |

**Il nostro spazio:** l'unico prodotto che, **partendo da un annuncio qualsiasi** (AutoScout24, Subito, Facebook Marketplace, concessionario), dà una risposta completa e personale. In più, ha dentro i **calcoli italiani** che ChatGPT non fa in modo affidabile: bollo regionale, superbollo, IPT provinciale, costi del passaggio, limiti di circolazione per classe Euro.

---

## 3. Che informazioni dà il report

1. **Verdetto in 3 righe:** prezzo (equo / alto / sospettosamente basso), rischio dell'annuncio (basso / medio / alto), cosa fare.
2. **Prezzo:** fascia di valore (dal 10° al 90° percentile), prezzo atteso di chiusura, 5 annunci comparabili, e cosa sposta il prezzo (es. "+800 € per il cambio automatico, −1.200 € per 30.000 km sopra la media").
3. **Rischi dell'annuncio:**
   - km incoerenti con età e uso;
   - prezzo troppo basso (possibile truffa);
   - frasi tipiche delle truffe ("sono all'estero", "caparra", "spedizione");
   - foto riutilizzate (ricerca inversa delle immagini);
   - auto importata;
   - richiami del modello.
4. **Verifiche guidate da fare in 2 minuti:**
   - km all'ultima revisione sul Portale dell'Automobilista (lo fa l'utente: il servizio ha un codice di sicurezza);
   - visura PRA (~6 €);
   - storico carVertical (con link di affiliazione).
5. **Costi veri:**
   - passaggio di proprietà (IPT provinciale: 150,81 € fino a 53 kW + 3,51 €/kW oltre, con maggiorazioni provinciali fino al 30%, più diritti ed emolumenti);
   - bollo regionale e superbollo (20 €/kW oltre 185 kW, ridotto con l'età);
   - consumi, assicurazione stimata e svalutazione a 3 anni.
6. **Il modello:** difetti tipici di quella motorizzazione e anno, cosa controllare durante la visita, quando conviene un meccanico.
7. **Trattativa:** prezzo da offrire, prezzo massimo oltre il quale rinunciare, argomenti basati sui dati, testo pronto da mandare al venditore.
8. **Regole locali:** limiti di circolazione per classe Euro nella tua zona (es. Area B a Milano, bacino padano), da tenere aggiornati con fonti ufficiali.

---

## 4. Come si costruisce l'app

### Architettura
```
Annuncio (link, testo o screenshot) ──► Estrazione dei dati (modello linguistico con visione)
                                              │  marca, modello, versione, anno, km, kW, cambio,
                                              │  prezzo, venditore, zona, optional, descrizione
                                              ▼
                       Normalizzazione sulla versione esatta (catalogo versioni)
                                              ▼
   ┌──────────────── Motore prezzo ────────────────┐   ┌──── Motore rischi ────┐   ┌── Calcolatori ──┐
   │ quotazione di base + correzione con il modello │   │ regole + AI sul testo │   │ IPT, bollo,     │
   │ (fascia, prezzo di chiusura, comparabili)      │   │ + foto + coerenza km  │   │ costi, regole   │
   └────────────────────────────────────────────────┘   └───────────────────────┘   └─────────────────┘
                                              ▼
                        Report (web + PDF) · trattativa · link di verifica e affiliazione
```
- **Tecnologia:** web app (non app nativa: nessuna commissione degli store e nessun tempo di approvazione). Frontend Next.js, backend Python (FastAPI), Postgres, LightGBM per il prezzo, API di un modello linguistico per estrazione e testi, Stripe per i pagamenti, server in UE.
- **Agenti di contorno:**
  - pagine SEO per modello e anno ("Quanto vale una Fiat Panda 2019?");
  - assistenza clienti;
  - creatività per la pubblicità;
  - controllo della qualità dei report (campioni verificati a mano ogni settimana).
- **Fase 2: estensione per il browser.** Mostra il nostro verdetto direttamente sulla pagina dell'annuncio che l'utente sta guardando. È il canale di distribuzione più forte (stile Keepa per le auto), ma va verificato legalmente.

### Tempi di costruzione (stima, con te a tempo pieno)
| Blocco | Settimane |
|---|:--:|
| Estrazione dall'annuncio + report base (senza modello di prezzo proprio) | 2 |
| Calcolatori italiani (IPT, bollo, superbollo, passaggio) | 1 |
| Motore rischi (regole + testo + foto) | 1–2 |
| Modello di prezzo (dipende dai dati, vedi sotto) | 2–4 |
| Pagamenti, PDF, pagine SEO | 1–2 |
| **Totale fino a un prodotto vendibile** | **~7–11** |

---

## 5. Come ottenere i dati (il punto critico)

| Fonte | Cosa dà | Legale | Costo | Giudizio |
|---|---|:--:|---|---|
| **Scraping di AutoScout24, Subito, ecc.** | Prezzi di tutti gli annunci | ✗ Vietato dai termini d'uso; diritto sulle banche dati in UE | — | **Escluso** (regole del dossier, capitolo 15) |
| **L'annuncio incollato dall'utente** | I dati di quell'annuncio | ✓ (testo o screenshot fornito dall'utente) | 0 | **Base del prodotto** |
| **Quotazioni con licenza** (Autovista / Eurotax tramite API; alVolante; Quattroruote) | Valore di riferimento per versione e anno | ✓ con contratto | Da chiedere (Quattroruote vende singole quotazioni a 3,99 €) | **Prima scelta per il prezzo di base** |
| **Accordo con un portale più piccolo** (Automobile.it, AutoSuperMarket, Motori.it) | Annunci e storico prezzi | ✓ con accordo | Scambio: loro ricevono il nostro strumento o traffico | Da esplorare |
| **Dati raccolti dagli utenti** (ogni annuncio analizzato, con consenso; esito della trattativa) | Il nostro storico: prezzi chiesti, prezzi di chiusura | ✓ con consenso GDPR | 0 | **Il fossato nel tempo**: nessuno ha i prezzi di chiusura tra privati |
| Dati pubblici (km all'ultima revisione, richiami, regole di circolazione, IPT e bollo) | Rischi e costi | ✓ (il Portale si consulta con l'utente, senza aggirare il codice di sicurezza) | 0 | Utili, già pronti |
| Storico veicolo (carVertical) | Km, incidenti, furti | ✓ tramite programma di affiliazione | Ci pagano loro | **Ricavo aggiuntivo** |

**Il fossato vero non è il prezzo chiesto** (quello lo vedono tutti) ma **il prezzo a cui le auto si vendono davvero**. Chiedere a ogni utente, dopo l'acquisto, "a quanto l'hai presa?" in cambio di un rimborso o di un'analisi gratuita costruisce in un anno una banca dati che nessun portale ha.

---

## 6. Come calcola il prezzo l'algoritmo

1. **Prezzo di base:** la quotazione con licenza per versione e anno (oppure, all'inizio, una stima dai comparabili disponibili).
2. **Correzione con un modello statistico** (gradient boosting sul logaritmo del prezzo) che impara le differenze rispetto alla base da:
   - km rispetto ai km attesi per età (alVolante pubblica i km medi per modello e anno);
   - potenza, cambio, alimentazione, optional estratti dal testo;
   - regione, tipo di venditore (privato o concessionario, con o senza garanzia);
   - stagione e andamento del mercato (le elettriche −8,3% nel 2025).
3. **Fascia, non numero:** regressione quantilica (10°, 50° e 90° percentile), con calibrazione conformale perché la fascia sia onesta (l'80% delle auto vere deve cadere dentro).
4. **Dal prezzo chiesto al prezzo di chiusura:** sconto atteso stimato da giorni in vendita, ribassi già fatti, tipo di venditore e, col tempo, dai prezzi di chiusura comunicati dagli utenti.
5. **Spiegazione:** i 3–5 fattori che spostano di più il prezzo (valori SHAP), più i comparabili.
6. **Controllo continuo:** errore misurato ogni mese sui prezzi di chiusura raccolti; se peggiora, il modello si riallena.

**Precisione attesa:** Carvago dichiara un errore medio di circa il 2% sul prezzo di vendita. All'inizio è realistico un errore del 5–10%, quindi il report deve mostrare la fascia e non un numero preciso.

---

## 7. Come trovare clienti e quanto costano

**Il momento giusto è stretto:** si compra un'auto ogni 5–8 anni, e la ricerca dura qualche settimana. Quindi niente abbonamento classico: **pagamento a report o "pass" per il periodo di ricerca**.

| Prezzo (proposta) | Cosa include |
|---|---|
| Gratis | Verdetto sintetico sul prezzo (per farsi trovare e conquistare fiducia) |
| **9,90 €** | Report completo su un annuncio |
| **19,90 €** | "Pass 30 giorni": report illimitati più avvisi |
| Affiliazioni | Storico carVertical, preventivi assicurativi, finanziamento, ispezione del meccanico |

**Economia per cliente (stima, `economia.py`):** ricavo netto ~14,4 €, contribuzione **~13,4 €**. È il CAC massimo per andare in pari al primo acquisto, e c'è poco riacquisto.

| CPC su Google | Visitatori che pagano | CAC | Margine |
|:--:|:--:|:--:|:--:|
| 0,30 € | 4% | 7,50 € | +5,90 € |
| 0,60 € | 4% | 15,00 € | −1,60 € |
| 0,60 € | 6% | 10,00 € | +3,40 € |
| 1,00 € | 4% | 25,00 € | −11,60 € |

Non ho trovato il CPC reale italiano per parole come "valutazione auto usata" (i riferimenti globali per il settore auto vanno da 0,9 a 3,9 $): **va misurato** con il Keyword Planner e il test.

**Canali, in ordine di importanza:**
1. **Contenuti brevi automatizzati:** "Affare o fregatura? Analizzo annunci veri" su TikTok, Instagram e YouTube. È un formato già popolare tra i creator di auto, e gli agenti possono produrlo partendo dai report (con il tuo volto o senza).
2. **SEO a pagine generate dai dati:** una pagina per modello e anno ("Quanto vale davvero una Golf 2019 diesel?"), più guide sulle truffe e sui km. I concorrenti SEO sono forti (AutoScout24, alVolante, Quattroruote): conviene puntare sulle domande lunghe e specifiche.
3. **Pubblicità sulla ricerca Google**, solo sulle parole con intenzione forte, e solo se il test conferma un CAC sotto i 10 €.
4. **Condivisione incorporata:** il report si manda al venditore ("ecco perché offro X") o al partner. Ogni condivisione è una pubblicità.
5. **Partner:** meccanici e servizi di ispezione, comparatori assicurativi, finanziarie. Si guadagna in entrambe le direzioni.

---

## 8. Quanto può crescere

| Quota dei passaggi italiani | Paganti l'anno | Ricavi |
|:--:|:--:|:--:|
| 0,5% | ~16.000 | ~0,23 M€ |
| 1% | ~32.000 | ~0,46 M€ |
| 2% | ~64.000 | ~0,93 M€ |
| 3% | ~97.000 | ~1,39 M€ |

**Lettura:** 1 M€ in sola Italia vuol dire diventare il riferimento per chi compra un'usata (2–3% di tutti gli acquisti). Con un modello che funziona in Italia, Spagna e Germania si moltiplica il bacino per ~3,7. Una seconda via è vendere ai piccoli concessionari (prezzo delle permute, 49–99 €/mese), ma è B2B con vendita e assistenza.

---

## 9. Rischi

| Rischio | Gravità | Risposta |
|---|:--:|---|
| Dati: i portali non vogliono condividerli | Alta | Base con licenza + dati degli utenti; niente scraping |
| I portali aggiungono le stesse funzioni (AutoScout24 ha già le etichette) | Alta | Funzionare **su tutti i siti** e con i privati; dati sui prezzi di chiusura; trattativa e costi |
| CAC troppo alto con la sola pubblicità | Media | Contenuti e SEO prima; pubblicità solo se il test la giustifica |
| Errori del prezzo o dei rischi → reclami | Media | Fasce e non numeri, avvertenze chiare, "analisi" e non "perizia" |
| Dati personali (targa, proprietario) | Bassa–media | Non conservare la targa senza necessità; consultazioni fatte dall'utente; server in UE |

---

## 10. Scheda v2 aggiornata

| Criterio | Peso | Voto | Nota |
|---|:--:|:--:|---|
| Motivazione | 20% | 4 | "Può essere interessante" (da confermare) |
| Vantaggio del founder | 15% | 4 | Data science + AI + marketing; ma niente dati propri all'inizio |
| Dolore e disponibilità a pagare | 10% | 3 | Si paga (carVertical), ma il prezzo giusto è ormai gratis |
| Mercato | 5% | 4 | 3,2 M di acquisti l'anno in Italia, ~12 M con Spagna e Germania |
| Margine | 10% | 4 | Digitale, costo per report < 0,5 € |
| Costo della validazione | 10% | 4 | Test concierge ≤ 300 € |
| Potenziale 1 M€ da solo | 15% | 3 | Possibile con l'estero o con un ruolo dominante in Italia |
| Automazione | 10% | 5 | Tutto il servizio è software |
| Difendibilità | 5% | 2 | Cresce solo se si costruisce la banca dati dei prezzi di chiusura |
| **Totale** | | **3,75** | Passa (era 4,20) |

---

## 11. Piano di validazione, con soglie fissate prima

| Test | Durata e costo | Cosa misura | Soglia per proseguire |
|---|---|---|---|
| **T1. Concierge** | 2–3 settimane, ≤ 300 € | 20–30 report fatti con strumenti semi-manuali, venduti a 9,90 € a chi sta comprando davvero (gruppi Facebook, Reddit, forum, conoscenti, un po' di pubblicità) | ≥ 20 report pagati; ≥ 70% li giudica utili; almeno 1 su 3 dice che ha cambiato la trattativa o la scelta |
| **T2. Pagina + Google Ads** | 2 settimane, ≤ 500 € | CPC reale, conversione visita → pagamento | CAC ≤ 12 € oppure conversione ≥ 4% con CPC ≤ 0,50 € |
| **T3. Dati** | In parallelo, 0 € | Preventivi di Autovista/Eurotax, alVolante, Quattroruote; disponibilità dei portali più piccoli | Prezzo di base a ≤ 0,50 € per analisi, o un accordo |
| **T4. Contenuti** | 4 settimane, 0–200 € | 10 video "affare o fregatura?" | ≥ 1 video sopra 50.000 visualizzazioni, o ≥ 200 iscritti alla lista |

**Regola di arresto:** se T1 non arriva a 20 report pagati, o se T2 e T3 danno CAC > 20 € e dati di base > 2 € ad analisi, si archivia.

---

## Fonti
- Mercato: [Teleborsa, dati ACI 2025](https://www.teleborsa.it/News/2026/02/05/mercato-auto-usate-nel-2025-2-1percent-diesel-ancora-dominante-elettrico-fermo-al-2percent-97.html) · [AutoScout24, Europa Report 2025](https://www.autoscout24.it/azienda/comunicati-stampa/europa-report-autoscout24-nel-2025-prezzi-usato-in-calo-in-italia-3-4-elettriche-giu-dell-8-3/) · [Osservatorio AutoScout24](https://www.autoscout24.it/azienda/comunicati-stampa/osservatorio-autoscout24-mercato-auto-usate-in-crescita-2-1-aumenta-il-budget-di-spesa-11-e-c-e-apertura-ai-brand-cinesi/) · [Auto.it](https://www.auto.it/news/attualita/2026/02/11-8627601/mercato-auto-usate-2025-previsioni-2026) · [Motorionline](https://www.motorionline.com/auto-usate-boom-in-italia-36-milioni-di-passaggi-nel-2025/) · [Autoblog](https://www.autoblog.it/post/auto-usate-italia-2025-modelli-prezzi) · [Autovista24, mercati europei 2025](https://autovista24.autovistagroup.com/news/how-did-europes-major-used-car-markets-perform-in-2025/)
- Concorrenti: [AutoScout24, valutazione del prezzo](https://www.autoscout24.it/b2b-info/valutazione-del-prezzo/) · [Quotidiano.net, etichette AutoScout24](https://motori.quotidiano.net/news/autoscout24-auto-usate-nuove.htm) · [alVolante e Subito Motori](https://www.alvolante.it/news/auto-usate-alvolante-quotazioni-collaborazione-subito-motori-414611) · [Automobilista.it](https://www.automobilista.it/dove-trovare-il-listino-usato-di-al-volante/) · [Autovista API](https://jdpower.com/business/autovista-api/) · [FleetMagazine, Eurotax](https://www.fleetmagazine.com/eurotax-cose-e-come-funziona-il-listino-per-la-valutazione-auto-usata/) · [HDmotori, carVertical](https://www.hdmotori.it/acquisto-auto-usata-carvertical-aiuta-a-evitare-le-fregature-la-nuova-offerta/) · [carVertical, programma di affiliazione](https://www.carvertical.com/it/affiliate-program) · [PriceGuru](https://apps.apple.com/us/app/id848960792) · [Silicon, Carvago](https://silicon.eu/used-car-trade-vehicle-inspections-with-ai-9086.html) · [Avturo](https://alternativeto.net/software/avturo/about/) · [AutoSuperMarket AI](https://autosupermarket.it/ai)
- Verifiche pubbliche: [SicurAuto, verifica revisione](https://www.sicurauto.it/news/verifica-revisione-auto-come-controllare-la-scadenza/) · [Telefonino.net, km reali](https://www.telefonino.net/notizie/auto-usate-e-km-scalati-come-verificare-gratis-online-i-chilometri-reali/) · [Tom's Hardware, controllo targa](https://www.tomshw.it/automotive/controllo-targa-gratis-vs-a-pagamento-pro-contro-e-quale-scegliere) · [Motor1, visura PRA](https://it.motor1.com/features/697439/visura-targa-auto-come-costi-guida/) · [SmartWorld, visura targa](https://www.smartworld.it/mobilita/come-fare-visura-targa-auto.html)
- Km scalati: [HDmotori](https://www.hdmotori.it/truffa-chilometri-scalati-auto-usate/) · [SicurAuto](https://www.sicurauto.it/news/attualita-e-curiosita/auto-usate-il-12-e-con-chilometri-contraffatti/)
- Pubblicità: [Pixis, benchmark Google Ads 2025](https://pixis.ai/blog/2025-google-advertising-benchmarks-for-every-industry/) · [Demandlocal, automotive](https://www.demandlocal.com/blog/google-vehicle-ads-performance-statistics/) · [Code Design, costi Google Ads in Europa](https://codedesign.org/google-ads-cost-europe-your-complete-guide/)
- Modelli di prezzo: [SciTePress, XGBoost](https://scitepress.org/Papers/2023/125107/125107.pdf) · [arXiv](https://arxiv.org/abs/2307.15982v1)
