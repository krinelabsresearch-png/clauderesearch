# Idee "perché adesso" (082–090): bisogni nati da poco o in arrivo

**Data:** 13 ottobre 2026
**Contesto:** dopo l'approfondimento la 075 (auto usata) non ti convince. Qui cerco bisogni creati da **un cambiamento con una data precisa** (un farmaco, una legge, una piattaforma), che i grandi non hanno ancora coperto in Italia o in Europa. Punteggi con la scheda v2 (`perche_adesso.py`). **La motivazione è una mia stima**: tra parentesi il punteggio con motivazione neutra (3).

## I cinque controlli (la lezione della 075)
La 075 è caduta su controlli arrivati alla fine. Ora li faccio subito, per ogni idea:
1. **Lo fa già ChatGPT?** Serve qualcosa che un chatbot da solo non dà: un'abitudine quotidiana, dati che si accumulano, un risultato concreto.
2. **C'è già gratis?** Come le etichette di prezzo di AutoScout24 per la 075.
3. **I dati si hanno in modo lecito?** Dati dell'utente, fonti pubbliche, API ufficiali. Niente scraping vietato.
4. **Si trova il cliente a basso costo?** Serve un momento preciso (l'inizio di una terapia, un cambio di lavoro) e un posto dove queste persone si riuniscono.
5. **Perché adesso, e per quanto?** Una data che crea il bisogno, e il tempo che resta prima che arrivino i grandi.

---

## Classifica
| ID | Idea | Cosa è cambiato, e quando | Scheda v2 |
|---|---|---|:--:|
| **082** | **Compagno per chi prende i farmaci GLP-1** | Pillola di Wegovy approvata in UE (luglio 2026); in Italia, per l'obesità, questi farmaci si pagano di tasca propria (Mounjaro: 300–500 € al mese) | **3,95** (3,75) |
| **090** | **Scanner delle dichiarazioni "green" vietate** *(B2B)* | Dal 27/9/2026 sono vietate in UE le dichiarazioni ambientali generiche ("eco", "green", "a impatto zero" grazie alle compensazioni) | **3,50** (3,50) |
| 083 | Busta paga giusta | Dal 7/6/2026 (D.Lgs. 96/2026) gli annunci devono indicare lo stipendio, non si può chiedere quello attuale, e i lavoratori hanno diritto a informazioni sulle retribuzioni | 3,45 (3,45) |
| 085 | Coach di padel per gli occhiali AI | Oltre 7 milioni di occhiali Meta venduti nel 2025; app di terzi in anteprima, pubblicazione aperta prevista nel 2026 | 3,45 (3,05) |
| 087 | Scudo contro foto rubate e deepfake | Nuovo reato di deepfake (dal 10/10/2025); casi "Mia moglie" e Phica (agosto 2025) | 3,35 (3,35) |
| 086 | Analisi delle pubblicità dei concorrenti (dati UE) | Le pubblicità mostrate in UE sono consultabili, con la copertura per Paese, età e genere | 3,30 (3,50) |
| 089 | Guardiano digitale per le famiglie | Il Parlamento europeo chiede 16 anni come età minima per i social (novembre 2025) | 3,25 (3,25) |
| 084 | Analisi del sangue spiegate | Fascicolo sanitario 2.0 interoperabile da giugno 2026 | 3,15 (3,15) |
| 088 | Certificato della batteria dell'auto elettrica usata | Data Act (12/9/2025 e 12/9/2026), passaporto della batteria (18/2/2027) | 2,60 (3,00) |

**In sintesi:** una sola idea supera bene la soglia (082). La 090 è sulla soglia, ma è B2B. Le altre restano tra 3,0 e 3,5 (da tenere ferme) o sotto.

---

## Le due in testa

### 082 · Compagno per chi prende i farmaci GLP-1 (Mounjaro, Wegovy e le nuove pillole)
**Cosa è cambiato:**
- **Luglio 2026:** la Commissione europea approva la **pillola di Wegovy**, il primo GLP-1 per bocca contro l'obesità. La Germania la lancia per prima (settembre); gli altri Paesi UE seguono dalla seconda metà del 2026. Ad agosto il Regno Unito ha autorizzato anche l'orforglipron di Lilly; in UE la decisione è attesa.
- **In Italia**, per l'obesità, Mounjaro e Wegovy sono in classe C: li paga il paziente (Mounjaro costa **300–500 € al mese**). La Lombardia prepara prezzi calmierati.
- **In Francia**, che a maggio 2026 ha deciso di rimborsarli, a fine gennaio erano già **oltre 70.000** (stima) i pazienti in cura con Mounjaro.

**Il bisogno nuovo.** Chi spende 300–500 € al mese vuole il massimo risultato e teme gli effetti collaterali:
- **Muscoli:** si mangia molto meno; senza abbastanza proteine si perde anche massa magra.
- **Capelli:** uno studio pubblicato sul BMJ, su pazienti con diabete di tipo 2, trova un rischio di alopecia più alto del 37% rispetto a chi prende gli SGLT-2 e del 68% rispetto ai DPP-4. In valori assoluti sono 6,9 casi ogni 1.000 anni-persona, contro 5,0 e 3,9.
- **Nausea e stitichezza:** cosa mangiare e quando.
- **La pillola ha regole nuove:** si prende al mattino a digiuno, con al massimo ~120 ml d'acqua (niente caffè), almeno 30 minuti prima di mangiare o di prendere altri farmaci. In uno studio su volontari sani, presa dopo un pasto, in 14 persone su 25 non risultava affatto nel sangue.
- **Dopo:** come non riprendere il peso quando si riduce o si sospende il farmaco.

**Il prodotto.** Un'app (iPhone, Android, web), prima in italiano e poi in spagnolo, tedesco e francese:
- diario di dosi, peso e sintomi;
- foto dei pasti con la stima delle proteine fatta dall'AI;
- menù adatti al poco appetito e brevi allenamenti di forza per difendere i muscoli;
- promemoria della routine della pillola;
- piano di mantenimento;
- un **riassunto in PDF da portare al medico** a ogni visita.

| Controllo | Esito |
|---|---|
| Lo fa ChatGPT? | **No.** Risponde alle domande, ma non tiene il diario, non ricorda la routine e non prepara il riassunto per il medico. Il valore sta nell'abitudine quotidiana e nei dati che si accumulano |
| C'è già gratis? | **In italiano non sembra.** Non ho trovato app dedicate (va verificato sull'App Store). Negli USA ce ne sono molte: Shotsy ha quasi 1 milione di download; terzi stimano ~300.000 $ di ricavi al mese, dato non verificato. Ha già aggiunto le pillole e una modalità di mantenimento |
| Dati? | **Sì.** Li inserisce l'utente; i valori nutrizionali vengono da tabelle pubbliche |
| Cliente? | **Raggiungibile, con un limite.** C'è un momento preciso (l'inizio della terapia), ci sono comunità attive (gruppi Facebook, TikTok) e ricerche su effetti collaterali, capelli e proteine. **Però** il targeting sanitario e le pubblicità che citano farmaci da prescrizione sono limitati: il canale principale deve essere organico (contenuti, ricerca, comunità) |
| Finestra? | **12–24 mesi**, mentre le pillole arrivano nei Paesi UE e prima che le grandi app di dieta coprano bene l'italiano |

- **Economia:** 9,99 € al mese o 59,99 € all'anno. **1 M€ di fatturato (IVA esclusa) ≈ 20.000 abbonati annuali.** È una piccola parte del mercato: solo in Francia c'erano 70.000 pazienti con un solo farmaco.
- **Perché tu:** scienza, aiutare le persone e un legame diretto con KRINÉ (capelli e pelle), se un giorno la lanci.
- **Rischi:**
  - **Dispositivo medico:** l'app non deve calcolare o consigliare le dosi né fare diagnosi. Diario, educazione e nutrizione sono ammessi.
  - **Dati sanitari (GDPR):** servono consenso esplicito, una valutazione d'impatto e server in UE.
  - **Concorrenza:** le app di dieta già tradotte (Yazio, MyFitnessPal, Lose It!) possono aggiungere una modalità GLP-1, e Shotsy può tradursi. A quel punto il vantaggio si riduce a lingua, cucina italiana e marketing locale.
  - **Abbandono:** le app AI perdono abbonati più in fretta (RevenueCat: dopo il primo anno rinnova il 21% degli abbonati annuali, contro il 31% delle altre app).
- **Test rapido (≤ 1.000 €, 3 settimane):**
  - una pagina "Mounjaro e Wegovy senza perdere muscoli e capelli", con guida gratuita e lista d'attesa;
  - contenuti su TikTok e Instagram, più 500 € di pubblicità con creatività neutre (senza citare farmaci);
  - preordine "fondatori" a 29,99 € il primo anno.

  **Soglie fissate prima:** costo per iscritto ≤ 2 € e almeno il 5% degli iscritti che preordina.

### 090 · Scanner delle dichiarazioni "green" vietate dal 27 settembre 2026 *(B2B)*
**Cosa è cambiato.** Dal **27 settembre 2026** si applica in tutta l'UE la direttiva 2024/825 ("consumatori per la transizione verde"). Diventano sempre vietati:
- le dichiarazioni ambientali **generiche** ("eco", "green", "sostenibile", "amico dell'ambiente"), se l'azienda non dimostra prestazioni ambientali eccellenti e riconosciute;
- le dichiarazioni di impatto neutro o ridotto basate sulla **compensazione** delle emissioni;
- i **marchi di sostenibilità** che non si basano su un sistema di certificazione e non sono istituiti da autorità pubbliche;
- le dichiarazioni sull'intero prodotto quando il merito riguarda solo una parte;
- presentare come un merito ciò che la legge impone a tutti.

In Italia lo schema di decreto è l'Atto del Governo n. 345 (dicembre 2025); la pubblicazione definitiva è da verificare. Le sanzioni sono quelle delle pratiche commerciali scorrette: multe dell'AGCM fino a 10 M€.

**Il bisogno nuovo.** Migliaia di marchi (cosmetica, moda, alimentare, casa) hanno siti, schede prodotto e pubblicità pieni di queste parole, scritte prima del divieto.

**Il prodotto:**
1. Il marchio inserisce l'indirizzo del sito (e, se vuole, le foto delle confezioni).
2. L'AI legge ogni pagina e scheda e trova le dichiarazioni a rischio.
3. Per ciascuna indica la regola violata e propone una riscrittura conforme, in un report.
4. Ogni mese ricontrolla le pagine nuove e le pubblicità.

| Controllo | Esito |
|---|---|
| Lo fa ChatGPT? | **Solo in parte.** Controlla un testo alla volta; non legge tutto il sito, le pubblicità e i contenuti nuovi ogni mese |
| C'è già gratis? | **No.** Ci sono studi legali e consulenti, costosi e una tantum. Gli strumenti AI dedicati sono da verificare |
| Dati? | **Sì.** È il sito del cliente stesso |
| Cliente? | **Il punto forte.** La libreria pubblicitaria di Meta mostra chi usa queste parole nelle pubblicità in UE: si trovano i marchi a rischio e si manda a ciascuno un mini-report gratuito ("3 delle tue pubblicità usano dichiarazioni vietate dal 27/9"). La ricerca si fa anche a mano dal sito della libreria, senza token. Con il token riusa `radar_meta.py` |
| Finestra? | **6–18 mesi** di massima attenzione; poi diventa un controllo di routine |

- **Economia:** audit a 149 €, monitoraggio a 49–99 € al mese, piano per agenzie a 299 € (prezzi + IVA). **1 M€ ≈ 850 abbonamenti a 99 € al mese.**
- **Perché tu:** marketing, regole sui claim cosmetici imparate con KRINÉ e AI. Servirebbe anche a KRINÉ.
- **Rischi:**
  - è **B2B**, mentre tu preferisci il B2C;
  - molti clienti fanno l'audit una volta e poi disdicono;
  - è un'analisi, non una consulenza legale;
  - se in Italia i controlli sono blandi, il dolore resta basso.
- **Test rapido (≤ 300 €, 2 settimane):** trovare 50 marchi italiani nella libreria pubblicitaria, mandare a ciascuno il mini-report gratuito e offrire l'audit completo. **Soglie:** almeno 10 risposte e almeno 3 audit pagati.

---

## Le altre, in breve
- **083 Busta paga giusta (3,45).**
  - **Cosa è cambiato:** dal 7/6/2026 gli annunci devono indicare lo stipendio iniziale o la fascia, non si può chiedere quanto si guadagna oggi, e i lavoratori hanno diritto a informazioni sulle retribuzioni.
  - **Il prodotto:** quanto dovresti guadagnare (dalle fasce degli annunci, ora pubbliche, e dai minimi dei contratti collettivi), la lettera per chiedere le informazioni all'azienda, il copione e una simulazione vocale della trattativa.
  - **Pro:** il "perché adesso" è forte ed è utile.
  - **Contro:** si paga una volta sola (29–39 €), quindi 1 M€ richiede ~35.000 acquisti l'anno. I dati sono un problema: LinkedIn e Indeed vietano lo scraping, quindi servono le pagine "lavora con noi" delle aziende e i dati degli utenti. Per crescere servono altri Paesi UE (la direttiva vale per tutti).
- **085 Coach di padel per gli occhiali AI (3,45; 3,05 con motivazione neutra).** È l'unica idea che tocca davvero il padel.
  - **Cosa è cambiato:** Meta ha venduto oltre 7 milioni di occhiali nel 2025, più del triplo dei due anni precedenti insieme. Il suo kit per sviluppatori dà accesso a fotocamera e microfono; l'app gira sul telefono.
  - **Contro:** la pubblicazione aperta non c'è ancora (a maggio 2026: al massimo 100 tester), il modello con display non è arrivato in Europa, e le app di analisi del padel dal telefono esistono già (Padel AI, Padel Coach, Padelize, PadelShot AI).
  - **Quando rivederla:** quando Meta apre lo store in Europa.
- **087 Scudo contro foto rubate e deepfake (3,35).**
  - **Cosa è cambiato:** dal 10/10/2025 diffondere un deepfake che danneggia una persona è reato (art. 612-quater, da 1 a 5 anni). Il gruppo "Mia moglie" aveva ~32.000 iscritti; Phica tra 720.000 e 800.000.
  - **Il prodotto:** cerca online le tue foto, anche modificate, con strumenti ufficiali di ricerca per immagini; prepara le richieste di rimozione alle piattaforme e il fascicolo di prove per la denuncia.
  - **Pro:** aiuta davvero.
  - **Contro:** niente riconoscimento facciale (è un dato biometrico); StopNCII e alcune associazioni aiutano gratis; è un tema pesante da gestire ogni giorno.
- **086 Analisi delle pubblicità dei concorrenti (3,30).** Grazie al DSA, le pubblicità mostrate in UE sono consultabili, con la copertura per Paese, età e genere, e il codice c'è già (`radar_meta.py`). Però è B2B e affollato: Foreplay, Minea, Atria, AdSpy e Brandsearch costano 49–459 $ al mese. **Meglio usarla come motore per trovare i clienti della 090.**
- **089 Guardiano digitale per le famiglie (3,25).** Il Parlamento europeo chiede 16 anni come età minima per i social, la Danimarca va verso il divieto sotto i 15 e in Italia il disegno di legge è fermo. Il bisogno è reale, ma Qustodio (europeo) e i controlli gratuiti di Apple e Google coprono già molto, e su iPhone il monitoraggio è limitato.
- **084 Analisi del sangue spiegate (3,15).** Il fascicolo sanitario 2.0 doveva diventare interoperabile in tutta Italia da giugno 2026. Negli USA Function Health ha oltre 500.000 iscritti a 365 $ l'anno. **Contro:** un software che interpreta i valori di un singolo paziente è probabilmente un **dispositivo medico** (filtro 7), e ChatGPT legge già un referto.
- **088 Certificato della batteria dell'auto elettrica usata (2,60).** Data Act e passaporto della batteria creano il bisogno, ma è di nuovo un'idea sulle auto: dopo la 075 la escludo.

## Scartate subito
- **Visibilità delle PMI nelle risposte dell'AI ("GEO"):** affollato. Peec AI ha superato 10 M$ di ricavi ricorrenti in 16 mesi, ma i fornitori sono già oltre 50.
- **Anti-truffa per anziani:** banche e piattaforme lo stanno integrando, mancano i dati, e chi paga (i figli) è difficile da raggiungere.
- **Strumenti AI per insegnanti con la Carta del docente:** 383 € l'anno, e software e hardware si possono comprare solo ogni 4 anni. Canale debole.

---

## Cosa ti chiedo
1. **Voto di motivazione (1–5)** per 082–090, almeno per 082, 090, 083 e 085.
2. **Quali approfondire** (una o due). Rifaccio il lavoro della 075, ma con i cinque controlli **prima** di tutto il resto.
3. **Verifica da 5 minuti sul tuo iPhone:** cerca "Mounjaro", "GLP-1" e "Wegovy" sull'App Store italiano. Dimmi se compaiono app in italiano e quante recensioni hanno. È il controllo "c'è già gratis?" della 082.

## Righe per backlog e log
```
| 082 | Compagno per chi prende i farmaci GLP-1 (iniezioni e pillole) | 3,95 (scheda v2) | 1 |
| 090 | Scanner delle dichiarazioni green vietate dal 27/9/2026 (B2B) | 3,50 (scheda v2) | 2 |
| 083 | Busta paga giusta: coach della trasparenza salariale | 3,45 (scheda v2) | 3 |
| 085 | Coach di padel per gli occhiali AI | 3,45 (scheda v2) | in attesa dello store Meta in UE |
| 087 | Scudo contro foto rubate e deepfake | 3,35 (scheda v2) | cassetto |
| 086 | Analisi delle pubblicità dei concorrenti (dati UE del DSA) | 3,30 (scheda v2) | motore per la 090 |
| 089 | Guardiano digitale per le famiglie | 3,25 (scheda v2) | cassetto |
| 084 | Analisi del sangue spiegate | 3,15 (scheda v2) | no (dispositivo medico) |
| 088 | Certificato della batteria dell'auto elettrica usata | 2,60 (scheda v2) | no |
| 075 | Analisi AI dell'auto usata | 3,75 (scheda v2) | no (bocciata da Lorenzo dopo l'approfondimento) |
```
```
| 2026-10-13 | 075 bocciata dopo l'approfondimento. Nuove idee "perché adesso" 082–090, con cinque controlli fatti all'inizio (ChatGPT, gratis, dati, cliente, finestra). In testa la 082 (compagno GLP-1, 3,95), poi la 090 (dichiarazioni green, 3,50, B2B) | Bisogni creati da date precise: pillola di Wegovy in UE (7/2026), direttiva 2024/825 (27/9/2026), D.Lgs. 96/2026 (7/6/2026). Vedi `idee/azienda-ai-solo/perche-adesso.md` | Voti di motivazione; scelta di 1–2 idee da approfondire; verifica sull'App Store per la 082 |
```

---

## Fonti
- **082 · Farmaci GLP-1**
  - Pillola di Wegovy in UE: [Nordic Life Science](https://nordiclifescience.org/novo-nordisk-receives-european-commission-approval-of-wegovy-pill-as-first-oral-glp-1-for-weight-management/) · [FoodNavigator, lancio in Germania](https://www.foodnavigator.com/Article/2026/08/06/germany-first-to-launch-wegovy-pill/)
  - Orforglipron: [Greek Reporter](https://greekreporter.com/2026/08/24/uk-first-country-europe-approve-glp-weight-loss-pill/) · [BHF](https://www.bhf.org.uk/informationsupport/heart-matters-magazine/news/behind-the-headlines/weight-loss-pills-orforglipron)
  - Italia e Francia: [AIFA, comunicato 21/2026](https://www.aifa.gov.it/documents/20142/3346516/Comunicato_AIFA_21-2026.pdf) · [Il Sole 24 Ore](https://en.ilsole24ore.com/art/france-reimburses-new-treatments-for-severely-obese-patients-italia-opens-debate-AIhbHQZD) · [Il Post, Lombardia](https://www.ilpost.it/2026/01/18/regione-lombardia-farmaci-dimagranti-ozempic-prezzi-calmierati/) · [Euronews, Francia](https://it.euronews.com/health/2026/05/28/francia-prima-in-europa-a-rimborsare-i-farmaci-dimagranti)
  - Capelli: [Epocrates](https://www.epocrates.com/online/article/glp-1-drugs-linked-to-higher-rates-of-hair-loss-real-world-data-suggest) · [Eastern Eye](https://www.easterneye.biz/glp-1-drugs-hair-loss-risk-new-study/)
  - Come si prende la pillola: [GoodRx](https://www.goodrx.com/wegovy/wegovy-pill-form) · [Medino, assunzione](https://www.medino.com/article/how-to-take-the-wegovy-pill-correctly) · [Medino, a digiuno o con il cibo](https://www.medino.com/article/should-you-take-the-wegovy-pill-with-food-or-on-an-empty-stomach)
  - Shotsy: [VC Backed](https://www.vcbacked.co/company/shotsy) · [Dealroom](https://app.dealroom.co/companies/shotsyapp_com) · [Rutland Herald, pillole e mantenimento](https://www.rutlandherald.com/features/health/shotsy-now-supports-oral-glp-1-tracking-first-of-its-kind-maintenance-mode-and-multi/article_b641db90-e971-5ec6-ad56-16a4197f845e.html)
  - Rinnovi delle app AI: [TechCrunch, RevenueCat 2026](https://techcrunch.com/2026/03/10/ai-powered-apps-struggle-with-long-term-retention-new-report-shows)
- **090 · Dichiarazioni green:** [Direttiva (UE) 2024/825](https://eur-lex.europa.eu/eli/dir/2024/825/oj) · [Camera, dossier sull'Atto del Governo 345](https://documenti.camera.it/Leg19/Dossier/Pdf/VQAG345.Pdf) · [Senato](https://www.senato.it/service/PDF/PDFServer/BGT/1485497.pdf) · [Legge 91/2025 (delega)](https://www.studiolegaleambiente.it/wp-content/uploads/2025/07/L.-91.2025-.pdf)
- **083 · Trasparenza salariale:** [Informazione Fiscale](https://www.informazionefiscale.it/stipendi-decreto-trasparenza-retribuzioni-novita-7-giugno-2026) · [Arletti Partners](https://arlettipartners.com/it/decreto-legislativo-sulla-trasparenza-salariale-n-96-del-2026-in-vigore-dal-7-giugno-2026/) · [A&O Shearman](https://www.aoshearman.com/it-it/insights/pay-transparency-italy-among-the-first-countries-to-comply-with-eu-obligations) · [Lente Pubblica](https://lentepubblica.it/personale-e-previdenza/guida-completa-decreto-trasparenza-salariale-2026/) · [Leyton](https://leyton.com/it/insights/articles/trasparenza-retributiva-dlgs-96-2026/)
- **085 · Occhiali e padel**
  - Occhiali: [Il Sole 24 Ore, produzione](https://en.ilsole24ore.com/art/essilux-paris-meta-aims-to-double-smart-glasses-production-AIbNOjr) · [Basic Tutorials, vendite](https://basic-tutorials.com/news/smart-glasses-are-booming-sales-of-meta-glasses-have-nearly-doubled/) · [Road to VR, kit per sviluppatori](https://roadtovr.com/meta-ray-ban-smart-glasses-third-party-app-sdk-device-access-toolkit/) · [PPC Land, modello con display](https://ppc.land/meta-opens-display-glasses-to-developers-with-two-sdk-paths/)
  - App di padel: [Padel AI](https://apps.apple.com/sr/app/padel-ai/id6760341511) · [Padel Coach](https://apps.apple.com/ee/app/id6757166892) · [Padelize](https://www.hunted.space/product/padelize) · [PadelShot AI](https://appshunter.io/ios/app/padelshot-ai-padel-coach/id6758633701)
- **087 · Deepfake**
  - Il reato: [Studio Cataldi](https://www.studiocataldi.it/articoli/48017-il-nuovo-reato-il-deepfake.asp) · [Diritto.it](https://www.diritto.it/deepfake-e-offesa-reale-la-nuova-fattispecie-penale/) · [Cybersecurity360](https://www.cybersecurity360.it/legal/il-nuovo-reato-di-deepfake-quando-il-diritto-penale-diventa-lultima-difesa-dellincertezza/)
  - I casi: [Il Post, Phica](https://www.ilpost.it/2025/08/29/phica-eu-testimonianze-donne-foto/) · [LaPresse, "Mia moglie"](https://www.lapresse.it/cronaca/2025/08/27/da-mia-moglie-ai-gruppi-porno-non-consensuali-le-denunce-di-alessandra-moretti-e-valeria-campagna/) · [Open](https://www.open.online/2025/08/29/facebook-causa-gruppo-mia-moglie-phica-avvocata-bernardini-de-pace/)
  - [StopNCII](https://stopncii.org/partners/join/)
- **086 · Pubblicità:** [AdLibrary, archivi del DSA](https://adlibrary.com/posts/eu-dsa-ad-repositories-developers) · [Foreplay](https://foreplay.co/post/adspy-vs-bigspy-vs-foreplay) · [Brandsearch](https://brandsearch.co/discovery) · [Gethookd, prezzi](https://www.gethookd.ai/learn/top-4-ai-ad-library-tools-in-2026-with-pricing/)
- **089 · Minori:** [Parlamento europeo](https://www.europarl.europa.eu/news/en/press-room/20251120IPR31496/) · [ABC7, Danimarca](https://abc7ny.com/post/denmarks-government-aims-ban-access-social-media-children-15/18127417/) · [Agenda Digitale](https://agendadigitale.eu/sicurezza/privacy/tutela-dei-minori-sui-social-dove-vanno-le-norme-in-ue-italia-mondo)
- **084 · Analisi del sangue:** [Agenda Digitale, FSE 2.0](https://www.agendadigitale.eu/sanita/fascicolo-sanitario-elettronico-2-0-si-cambia-davvero-tutto-quello-che-ce-da-sapere/) · [Regione Lazio](https://regione.lazio.it/notizie/urp/Urp-Nur-informazioni-utilizzo-nuovo-Fascicolo-Sanitario-Elettronico) · [TechCrunch, Function Health](https://techcrunch.com/2025/11/19/function-health-closes-298m-series-b-at-a-2-5b-valuation-launches-medical-intelligence) · [Sacra](https://sacra.com/c/function-health/)
- **088 · Batterie:** [CMS, Data Act e veicoli](https://cms.law/en/ita/publication/vehicle-data-in-the-era-of-the-data-act.-the-eu-commission-s-guidelines) · [Automotive IQ, passaporto della batteria](https://www.automotive-iq.com/electrics-electronics/articles/eu-battery-passport-explained-requirements-timeline-and-compliance-steps-to-2027)
- **Scartate:** [Peec AI, 10 M$](https://www.onenewspage.com/n/Press+Releases/1ztfis6jxj/Peec-AI-hits-10M-ARR-16-months-after.htm) · [Omnius, mercato GEO](https://omnius.so/blog/ai-search-geo-report-and-trends-2026) · [Orizzonte Scuola, Carta del docente](https://www.orizzontescuola.it/carta-del-docente-piattaforma-temporaneamente-chiusa-dopo-il-31-agosto-per-laggiornamento-al-2026-27/) · [Docenti.it](https://www.docenti.it/blog/come-usare-la-carta-del-docente)
