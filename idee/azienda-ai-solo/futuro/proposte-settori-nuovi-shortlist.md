# Proposte 208–217, settori nuovi: le 16 idee scelte dal curatore (14/10/2026)

Le 16 idee sono state scelte tra le 48 proposte da 6 generatori, prima della verifica sul web. Le 10 finali saranno in `proposte-settori-nuovi.md`.

## 1. OMBRA: la TAC del fotovoltaico che trova e disegna in 3D chi ti ruba il sole — fotovoltaico residenziale e piccole imprese (mixed)

- **Cosa fa:** Usa solo la curva di produzione dell'inverter e l'irraggiamento misurato dai satelliti. Con questi dati ricostruisce come una TAC gli ostacoli che fanno ombra ai pannelli (l'albero del vicino, un comignolo, un palazzo nuovo) e trova i guasti nascosti. Per ognuno dice quanto costa in euro all'anno. Gli installatori lo usano come motore white label per vendere manutenzione; i proprietari lo comprano come check-up.
- **Momento WOW:** Il proprietario collega l'account dell'inverter. In 30 secondi sul modello 3D del suo tetto compare una sagoma a sud-ovest: 'Ostacolo alto circa 11 m, a 17 m di distanza: probabilmente il pioppo del vicino. Ti costa 186 € l'anno, il 9% in più ogni anno perché cresce.' Più sotto: 'La stringa 2 rende il 38% in meno dal 14 marzo. Finora hai perso 290 €: chiama l'installatore.' Un'animazione mostra l'ombra che scorre sul tetto alle 16:00 di dicembre.
- **Perché era impossibile prima:** Il problema inverso funziona come una tomografia: ogni calo di produzione a una certa posizione del sole è un 'raggio' che attraversa l'ostacolo. Con mesi di dati si ricostruisce l'orizzonte. Gli ingredienti necessari sono disponibili tutti insieme solo da poco:
- irraggiamento satellitare gratuito e quasi in tempo reale per ogni tetto (CAMS, SARAH-3);
- dati degli inverter tramite API cloud;
- modelli 3D di edifici e altezza della vegetazione, da LiDAR nazionali e da satellite;
- ottimizzazione differenziabile che costa centesimi per impianto.
In più dopo il 2022 il numero di impianti è esploso: circa 1,9 milioni in Italia e oltre 4 milioni in Germania (stime da verificare), quasi tutti senza diagnosi. Prima un'analisi delle ombre richiedeva un sopralluogo con uno strumento dedicato.
- **Chi paga e quanto:** - Installatori e manutentori (canale principale): 1,5 €/impianto/mese, minimo 99 €/mese. Lo usano per vendere manutenzione, pulizie, potature, ottimizzatori e batterie.
- Proprietari: check-up a 29 €, oppure 3 €/mese.
- In seguito: una 'garanzia di resa' venduta da installatori o assicuratori.
Per 300 k€ servono circa 15.000 impianti in abbonamento B2B più qualche migliaio di check-up. Per 1 M€: Germania e Olanda, oppure un accordo con un grande installatore o con una utility.
- **Più di ChatGPT:** Davanti a un grafico ChatGPT può dire 'forse è un'ombra'. Non incrocia tre anni di dati quartorari con l'irraggiamento reale sopra il tuo tetto, giorno per giorno. Non risolve un problema geometrico inverso per dire dove sta l'ostacolo e quanto è alto, e non traduce la perdita in euro. Qui si paga una diagnosi fisica con un numero, più un flusso automatico che ogni mese avvisa l'installatore.
- **Primo test:** Budget 10 k€, 10 settimane: analisi retroattive gratuite su 300 impianti, reclutati tramite 10 installatori e gruppi di proprietari.
- GO se valgono tutte e tre:
  1. almeno il 25% degli impianti ha una perdita spiegata del 5% o più;
  2. l'ostacolo indicato è confermato sul posto in almeno 7 casi su 10;
  3. entro 60 giorni almeno 3 installatori firmano a 99 €/mese o più.
- STOP se le perdite rilevanti riguardano meno del 10% degli impianti, o se firmano meno di 2 installatori.
- **Rischi:** - API: Huawei, forse la marca più diffusa nel residenziale italiano (da verificare), dà i dati solo tramite account installatore. I produttori possono limitare o chiudere l'accesso.
- Con dati solo orari la tomografia è meno precisa.
- Concorrenti nel monitoraggio: Solytic, Solar-Log, le app degli inverter che aggiungono AI, gli ottimizzatori per pannello di SolarEdge ed Enphase, Raycatch per i grandi impianti.
- Se l'impianto va bene il valore percepito è basso: va venduto come assicurazione sulla resa.
- Se l'ostacolo è l'albero del vicino, il cliente può sentirsi frustrato invece che aiutato.
- **Nota del curatore:** PERCHÉ: tra le idee del lens energia è quella con il WOW più 'impensabile': una TAC fatta con la curva dell'inverter. Il nucleo è un problema geometrico inverso, cioè lavoro da matematico. Ricavi ricorrenti tramite gli installatori e poco lavoro operativo.
AFFINAMENTO: venderlo agli installatori come motore di upsell e 'garanzia di resa', non come l'ennesima app di monitoraggio. Condividere connettori e clienti con CURVA, perché spesso è lo stesso proprietario ad avere fotovoltaico e pompa di calore.
DA VERIFICARE:
- politiche API di Huawei FusionSolar, SolarEdge e Fronius;
- se SolarEdge, Enphase, Solytic, 1KOMMA5° o altri offrono già una diagnosi delle ombre con ricostruzione dell'orizzonte;
- numero reale di impianti residenziali in Italia e Germania.

## 2. CURVA: il pilota automatico che fa rendere la pompa di calore come in laboratorio — energia domestica (pompe di calore) (consumer)

- **Cosa fa:** Un agente si collega al cloud della pompa di calore e in una settimana impara la fisica della casa. Poi ogni ora riscrive curva climatica, temperatura di mandata e orari, in base a meteo, prezzi dinamici dell'energia e produzione del fotovoltaico. Alza l'efficienza stagionale del 15–30% senza toccare l'impianto, e si paga con il risparmio misurato.
- **Momento WOW:** Il proprietario entra con il suo account Daikin, Viessmann o Panasonic. Dopo 30 secondi vede la 'radiografia' dell'inverno scorso, ora per ora: 'Il 14 gennaio la macchina mandava acqua a 47 °C quando ne bastava 35, e si è accesa e spenta 61 volte. Con la curva giusta avresti speso 380 € in meno.' Preme 'guida tu' e la mattina dopo il grafico del COP passa da 2,6 a 3,5, con la stessa temperatura in salotto.
- **Perché era impossibile prima:** Quattro cambiamenti recenti:
1. Tra il 2021 e il 2025 in UE sono state installate milioni di pompe di calore aria-acqua (Superbonus in Italia, legge GEG in Germania), quasi sempre lasciate con la curva di fabbrica.
2. Solo da poco i produttori espongono API cloud utilizzabili da terzi, come Daikin Onecta e Viessmann ViCare (da verificare marca per marca).
3. Dal 2025 in Germania ogni fornitore di energia deve offrire una tariffa dinamica.
4. Calibrare un modello termico per ogni casa e far girare ogni ora un controllo predittivo richiedeva un termotecnico. Oggi costa pochi centesimi di calcolo, e un LLM spiega le scelte e fa assistenza senza persone.
- **Chi paga e quanto:** Pagano i proprietari di pompe di calore aria-acqua: 59 €/anno, oppure il 25% del risparmio misurato. Canale B2B: white label per utility e installatori a 1–2 €/impianto/mese.
- 300 k€: circa 5.000 abbonati, oppure 2 partner con 10–15.000 impianti.
- 1 M€: Germania, Italia e Francia insieme.
In UE le pompe di calore installate sono oltre 20 milioni (dato EHPA da verificare).
- **Più di ChatGPT:** ChatGPT spiega cos'è una curva climatica e consiglia di abbassarla di 2 gradi, ma:
- non si collega alla tua macchina;
- non legge 8.760 ore di dati;
- non stima quanto disperde la tua casa;
- non comanda la pompa ogni ora in base a meteo e prezzi;
- non dimostra il risparmio contro un controfattuale.
Qui si paga un agente che agisce sul dispositivo con un modello fisico calibrato, e si paga solo se si risparmia.
- **Primo test:** Budget 12 k€, 60 giorni, da partire subito: oggi, a metà ottobre, inizia la stagione di riscaldamento.
- Analizzatore gratuito in sola lettura per Daikin e Viessmann: 'radiografia' dell'inverno e risparmio stimato.
- Lancio in Germania e in Italia su forum e gruppi di proprietari, con 6 k€ di ads.
- Il pilota automatico si vende in prevendita a 59 €/anno.
GO con almeno 300 account collegati e almeno il 12% di prevendite (36 o più paganti). STOP con meno di 120 account o con conversione sotto il 5%.
- **Rischi:** - Accesso alle API: un produttore può limitarle o vietarle (per Onecta risultano limiti di chiamate giornaliere, da verificare). Meglio puntare a partnership ufficiali.
- Concorrenza diretta: Havenwise (UK) fa esattamente questo; tado, 1KOMMA5° Heartbeat, Octopus e le app dei produttori stanno aggiungendo l'AI.
- Responsabilità su comfort e garanzia.
- Stagionalità: si vende in inverno.
- Il risparmio reale varia molto da casa a casa.
- **Nota del curatore:** PERCHÉ: ha la logica commerciale più solida della lista. Si paga con un risparmio misurato, il parco installato è enorme e mal regolato, e Havenwise dimostra che la domanda esiste. Il WOW è meno 'impensabile' di OMBRA, ma la radiografia dell'inverno colpisce, e la stagione di riscaldamento appena iniziata permette un test immediato.
AFFINAMENTO:
- partire dalla Germania (tariffe dinamiche obbligatorie, grande parco GEG);
- cercare subito un accordo white label con una utility o un installatore, per avere un accesso ufficiale alle API;
- condividere connettori e clienti con OMBRA.
DA VERIFICARE:
- limiti delle API Daikin Onecta e Viessmann ViCare;
- se Havenwise si espande in UE;
- funzioni di ottimizzazione già offerte da tado, Octopus, 1KOMMA5° e dagli stessi produttori.

## 3. RIVERBERO: ascolti la tua stanza con i pannelli acustici prima di comprarli — acustica architettonica e d'interni (retail)

- **Cosa fa:** Inquadri la stanza col telefono e batti le mani. L'app ricostruisce l'acustica reale e ti fa sentire in cuffia come suonerà con 12 pannelli fonoassorbenti, un tappeto o un controsoffitto. Poi riempie il carrello. Si vende come widget a marchi ed e-commerce di prodotti acustici.
- **Momento WOW:** Il titolare di un ristorante rumoroso scansiona la sala per 40 secondi e batte le mani. In cuffia sente la sala piena di un sabato sera com'è oggi, con chiacchiericcio e piatti. Con un tocco la riascolta con il kit da 18 pannelli, e la voce di chi gli siede di fronte diventa chiara. A schermo il riverbero scende da 1,9 a 0,6 secondi, i pannelli compaiono già posizionati in realtà aumentata e c'è un carrello da 2.340 € pronto.
- **Perché era impossibile prima:** - La scansione 3D della stanza è nativa sui telefoni solo dal 2022 (Apple RoomPlan, API di profondità Android).
- La simulazione acustica a onde su GPU oggi richiede secondi; prima servivano ore e un software specialistico da migliaia di euro.
- I modelli di visione riconoscono i materiali delle superfici.
- L'audio generativo crea scene sonore realistiche, e il rendering binaurale funziona sulle cuffie che milioni di persone hanno già.
- Dopo il 2020 la vendita online di pannelli acustici è esplosa, spinta da home office, podcast e locali.
- **Chi paga e quanto:** - Marchi ed e-commerce di pannelli e arredi acustici: 1.500–4.000 €/mese più l'1% del venduto generato. Per esempio Caimi Snowsound, Fantoni, Vicoustic, Artnovion, BAUX, Abstracta e i marchi diretti di pannelli in legno (nomi da verificare).
- Progettisti d'interni e architetti: 49 €/mese.

Per 300 k€ servono 8 brand più 150 professionisti. Per 1 M€ bisogna allargarsi a tende, tappeti, controsoffitti e vetri fonoisolanti.
- **Più di ChatGPT:** ChatGPT applica la formula di Sabine alle misure che gli detti e risponde 'servono circa 10 m² di pannelli'. Non misura la tua stanza, non simula le onde e non calibra il modello sul tuo battito di mani. Soprattutto non ti fa sentire il prima e il dopo, che è proprio ciò che fa comprare.
- **Primo test:** Budget 15 k€: prototipo iOS solo per telefoni con LiDAR, limitato ai pannelli a parete.
1. Validazione dell'accuratezza su 20 stanze: il riverbero previsto deve stare entro ±15% di quello misurato con un fonometro.
2. Test A/B sul sito di 1–2 brand, oppure su un piccolo e-commerce in affiliazione.

GO se chi usa l'ascolto converte almeno il doppio del gruppo di controllo e se entro 4 mesi almeno 2 brand firmano un pilota da 1.000 €/mese o più. STOP se la conversione cresce meno del 30% o se nessun brand paga.
- **Rischi:** - Precisione: i microfoni dei telefoni sono deboli sui bassi e molti Android non hanno il LiDAR.
- I brand grandi potrebbero farselo in casa o restare con i calcolatori semplici.
- Strumenti professionali come Treble Technologies, Odeon, CATT ed EASE: servono agli specialisti, non a vendere.
- Il WOW deve tradursi in vendite misurabili.
- Le aspettative vanno gestite: dopo l'installazione la stanza deve suonare come in cuffia.
- **Nota del curatore:** PERCHÉ: è l'unica idea davvero 'retail', con un WOW sensoriale (ascolti la tua stanza prima di comprare) e un modello a percentuale sul venduto. Usa lo stesso motore di ONDE (scansione della stanza più simulazione d'onda), che è stata scartata: se questa idea passa, il motore potrà servire anche altri mercati.
AFFINAMENTO: attaccare due verticali dove il problema fa male e il carrello è alto, cioè ristoranti e home studio/podcaster. Ai brand si vende canone più percentuale.
DA VERIFICARE:
- precisione del tempo di riverbero (RT60) stimato da telefono, in letteratura e nelle app esistenti;
- se Treble o altri offrono già l'auralizzazione per e-commerce;
- quali brand hanno configuratori online, e con quali volumi.

## 4. STABILE: la storia di un edificio misurata al millimetro dai satelliti — immobili e rischio fisico degli edifici (mixed)

- **Cosa fa:** Inserisci un indirizzo o il link di un annuncio e in 30 secondi vedi quattro cose:
- se l'edificio si è abbassato o spostato dal 2016 a oggi, in millimetri misurati dal radar satellitare;
- se la strada si è allagata;
- quanto sole prende ogni facciata;
- quanto caldo farà dentro nel 2035.
È un 'carVertical delle case', con API per periti, banche, assicurazioni e fondi.
- **Momento WOW:** La mappa vola sul palazzo, che si colora di rosso, e parte un grafico: '−2,3 cm dal 2016, 3 volte più dei palazzi vicini, in accelerazione dal 2021'. Sopra compare l'immagine satellitare dell'alluvione del maggio 2023. Oppure arriva il sollievo: 'stabile: ±1 mm l'anno, mai allagato'. Un fondo carica 3.000 indirizzi e in 5 minuti riceve i 40 edifici che si muovono.
- **Perché era impossibile prima:** - Dal 2022 l'European Ground Motion Service di Copernicus (EGMS) pubblica gratis, per tutta Europa e con aggiornamenti annuali, miliardi di misure di spostamento al millimetro ottenute con l'interferometria radar (InSAR). Prima uno studio InSAR costava migliaia di euro ed era riservato a enti e grandi aziende: per un singolo acquirente era impensabile.
- Sentinel-1C, lanciato a fine 2024, ha ripristinato i passaggi frequenti.
- I modelli fondazionali geospaziali e gli LLM permettono di associare i punti radar a ogni edificio e di spiegare il risultato a chi compra casa.
- **Chi paga e quanto:** - B2B, canale principale: periti e società di valutazione, banche per i mutui, assicurazioni casa, amministratori e fondi immobiliari. API da 0,50 a 3 € a indirizzo, oppure abbonamento da 1 a 5 k€/mese.
- Acquirenti di casa: 29–49 € a report, con un semaforo gratuito che porta traffico.

300 k€ = 5–6 clienti API più 5.000 report. 1 M€ = aggiungere Spagna, Olanda (case su pali di fondazione) e Germania.
- **Più di ChatGPT:** ChatGPT può dire in generale che 'la zona è soggetta a subsidenza'. Non ha le misure radar del tuo civico, non sa elaborarle e non distingue un cedimento reale dalla dilatazione termica estiva. Qui si vende un dato fisico misurato su quell'edificio: un grafico che nessun venditore può smontare a parole.
- **Primo test:** Budget 9 k€, 60 giorni.
- Contatto diretto con 30 periti, 5 assicurazioni e 3 fondi, con pilota API a pagamento.
- In parallelo, landing in Italia con semaforo gratuito per indirizzo e report a 29 €.
- 5 k€ di ads e SEO su chi cerca casa nelle zone note per subsidenza o bradisismo (ravennate, Veneto, area flegrea).
GO se almeno 1 cliente B2B paga un pilota da 2 k€ o più e se, su almeno 2.000 ricerche, almeno il 3% compra il report (60 o più). STOP con conversione B2C sotto l'1% e nessun pilota B2B.
- **Rischi:** - Copertura: i punti radar mancano su edifici piccoli, rurali o coperti dalla vegetazione. Serve una soglia onesta di 'dato insufficiente'.
- Rischio legale: un venditore può contestare un report che svaluta la sua casa. Linguaggio sempre probabilistico, e mai presentarlo come perizia.
- I dati sono gratuiti anche per i concorrenti: TRE Altamira, Detektia, SkyGeo (mappe gratuite in Olanda), Planetek Rheticus, Terrafirma nel Regno Unito.
- La disponibilità a pagare dell'acquirente italiano non è dimostrata.
- EGMS esce una volta l'anno, con 1–2 anni di ritardo.
- **Nota del curatore:** PERCHÉ: il WOW è forte ('il tuo palazzo si è abbassato di 2,3 cm, misurato dallo spazio') e il lavoro operativo è quasi nullo: dati pubblici gratuiti e report automatici. È anche l'unico prodotto immobiliare della lista, quindi aggiunge un settore.
AFFINAMENTO: invertire l'ordine dei canali rispetto alla bozza. Prima il B2B (periti, banche, assicurazioni, fondi via API), poi il consumatore, con il semaforo gratuito come fonte di traffico. Concentrarsi sulle zone dove il problema è noto.
DA VERIFICARE:
- copertura e calendario degli aggiornamenti EGMS;
- licenza commerciale dei dati Copernicus;
- proptech che vendono già report per indirizzo in Italia e in UE;
- prezzi reali di TRE Altamira e Detektia.

## 5. GLIFO: scrivi cinque lettere su un tovagliolo, ricevi una famiglia di font completa — tipografia e design grafico (mixed)

- **Cosa fa:** Partendo da 5–8 lettere disegnate a mano o da un logotipo, l'AI ricostruisce l'intero carattere: maiuscole, minuscole, numeri, gli accenti di tutte le lingue UE, greco e cirillico, più pesi e corsivo. Il risultato è un font variabile da installare, già spaziato e crenato. I soldi veri arrivano dal carattere aziendale costruito sul logo.
- **Momento WOW:** Scrivi 'Lorenzo' a penna su un foglio e lo fotografi. Novanta secondi dopo apri Word e scrivi una mail in quel carattere, anche in grassetto e in corsivo. Le lettere che non hai disegnato (Q, ß, ž, perfino Ω e Ж) sono coerenti con le tue. Un'azienda fa lo stesso partendo dal logo e ottiene un carattere tutto suo, senza licenze annuali.
- **Perché era impossibile prima:** La generazione vettoriale di font da pochi esempi è maturata tra il 2023 e il 2025, con DeepVecFont-v2, DualVector, VecFusion, FontDiffuser e gli LLM che scrivono SVG come StarVector e OmniSVG. Tre anni fa c'erano solo due strade: un modello da riempire glifo per glifo (Calligraphr) o settimane di lavoro di un type designer. Nessun sistema ricavava le lettere mancanti mantenendo contrasto, terminali e proporzioni, né garantiva che i pesi si potessero interpolare.
- **Chi paga e quanto:** - Consumatori e creator: 19 € per un peso, uso personale. È il canale virale.
- Professionisti, studi e startup: 290 € per la famiglia completa, con licenza commerciale e proprietà del file.
- Aziende: piano 'Corporate' a 2.900 €, con più alfabeti, più assi e revisioni illimitate. Un carattere su misura da fonderia o una licenza aziendale annuale costano 20–150 k€ (stima da verificare).
- Studi di design: 99 €/mese.
Esempio: 1.200 famiglie commerciali e 40 piani Corporate fanno circa 465 k€ l'anno.
- **Più di ChatGPT:** ChatGPT può disegnare qualche lettera come immagine o un SVG isolato. Non produce un OpenType variabile pronto da installare, con oltre 600 glifi coerenti, metriche, spaziatura, crenatura, hinting e pesi interpolabili. Non verifica nemmeno che il risultato non copi un font esistente. Qui si paga il file pronto per la produzione, non il disegno.
- **Primo test:** Budget 5–9 k€.
- MVP latino a un peso: maiuscole, minuscole, numeri e accenti UE.
- Landing, video corti su TikTok, Instagram e Behance, lancio su Product Hunt, 3 k€ di pubblicità.
- Prezzi veri: 29 € per uso personale, 290 € per uso commerciale.
GO se in 60 giorni si vendono almeno 500 font, o si incassano almeno 15 k€, con rimborsi sotto il 10% e almeno 5 richieste 'Corporate'. STOP sotto i 150 font venduti o con rimborsi oltre il 25%.
- **Rischi:** - Adobe, Canva, Figma o Monotype possono lanciare una funzione simile; forse esistono già generatori AI che producono un OTF completo (da verificare).
- I type designer possono criticarlo in pubblico.
- Diritto: in UE il disegno dei caratteri si può tutelare come design e il software dei font è protetto da copyright. Servono un controllo anti-copia e un parere legale sull'addestramento con font OFL.
- Il consumatore compra una volta sola: i ricavi ricorrenti vengono da studi e aziende.
- **Nota del curatore:** PERCHÉ: è puro software self-serve e globale. Il WOW si capisce subito e si condivide da solo: scrivi il nome a penna e 90 secondi dopo lo usi in Word. È il più 'matematico' dei creativi: scheletri compatibili, interpolazione dei pesi, crenatura come ottimizzazione. In più è affine alla sensibilità di design di Lorenzo.
AFFINAMENTO: il consumatore porta traffico, i ricavi stanno nel piano Corporate (carattere aziendale dal logo, con cirillico e greco) e negli studi.
DA VERIFICARE:
- se a fine 2026 qualcuno genera già font variabili completi da pochi glifi (startup di font AI, funzioni di Adobe, Canva o Figma);
- termini della licenza OFL per l'addestramento;
- tutela UE dei caratteri tipografici.

## 6. PLAYFORGE: dal video di gameplay a 10 annunci giocabili in un'ora — videogiochi mobile (pubblicità e acquisizione utenti) (pmi)

- **Cosa fa:** Lo studio incolla il video del proprio gioco mobile. Un agente ricostruisce la meccanica in HTML5 e genera varianti di annunci giocabili (playable ad) già conformi alle reti pubblicitarie. Poi le pubblica, legge come convertono e fa evolvere le migliori.
- **Momento WOW:** La responsabile dell'acquisizione utenti incolla il link YouTube di 40 secondi del suo puzzle game. Pochi minuti dopo inquadra un QR e sul telefono gioca 5 mini-versioni del suo gioco, con la sua grafica, il suo logo e il bottone 'Installa'. Sono annunci pronti, sotto i 5 MB. Un'agenzia li avrebbe consegnati in 2–3 settimane, a 3–8 mila $ l'uno.
- **Perché era impossibile prima:** Dal 2025 sono disponibili tre capacità:
- gli agenti di programmazione (Claude Code, Codex) scrivono e correggono da soli giochi HTML5 completi, verificandoli in un browser headless;
- i modelli video (Gemini 2.5/3) capiscono la meccanica guardando un gameplay;
- SAM 2/3 e i modelli di editing d'immagine estraggono sprite puliti da un video.
Nel 2023 GPT-4 faceva un Pong traballante. Un playable fedele al gioco, testato su 30 dispositivi e conforme a MRAID, richiedeva settimane di lavoro umano.
- **Chi paga e quanto:** Pagano gli studi di giochi mobile medi, che spendono da 50 k€ a qualche M€ al mese in acquisizione utenti, e i publisher.
- Starter: 990 €/mese, 10 playable.
- Pro: 2.490 €/mese, 40 playable, motore di varianti e caricamento automatico.
- Enterprise: da 5 k€/mese.
15 clienti Pro fanno circa 450 k€ l'anno, 35 circa 1 M€. Riferimento: agenzie e freelance chiedono 2–10 k$ a playable (stima da verificare).
- **Più di ChatGPT:** ChatGPT scrive un mini-gioco generico da un prompt. Non fa invece nessuna di queste cose:
- estrarre la meccanica e la grafica vere del TUO gioco da un video;
- rispettare le specifiche di sei reti (peso, MRAID, CTA, orientamento);
- testare su decine di dispositivi;
- pubblicare le campagne;
- leggere l'IPM reale di ogni variante per generare le successive.
Si paga il ciclo creativo automatico, non il codice.
- **Primo test:** Budget 8–14 k€: calcolo, una fiera tipo Pocket Gamer Connects, dispositivi di test.
- MVP su 2 generi: puzzle e merge.
- Offerta a 60 studi via LinkedIn: '3 playable gratis in 48 ore dal vostro video'.
- Gli studi li mettono in campagna accanto ai loro migliori.
- GO se in 90 giorni almeno 3 studi su 10 ottengono un IPM pari ad almeno l'80% del loro miglior playable fatto da persone, e se almeno 3 firmano un piano da 990 €/mese o più.
- STOP con meno di 2 paganti o con IPM sotto il 60% del riferimento.
- **Rischi:** - Rischio principale: AppLovin, Unity (Luna) e Mintegral possono integrare la generazione AI di playable nelle loro console. Da verificare cosa offrono a fine 2026.
- Probabili startup AI già attive in questo spazio.
- Le reti vietano gli annunci ingannevoli: il playable deve rappresentare il gioco vero.
- Gli studi grandi hanno sviluppatori interni, quelli piccoli spendono poco.
- La tentazione del lavoro su misura può trasformarlo in servizio.
- **Nota del curatore:** PERCHÉ: i clienti spendono già decine di migliaia di euro al mese in creatività e il ROI si misura in IPM, quindi un playable migliore si paga da solo. Per chi compra il WOW è enorme: dal link YouTube al gioco sul telefono in pochi minuti. È anche il caso d'uso più naturale per un ingegnere AI che padroneggia gli agenti di codice.
AFFINAMENTO: restare su 2–3 generi 'a scheletro' e self-serve. Il fossato vero è il ciclo bayesiano sulle metriche reali, non la generazione in sé.
DA VERIFICARE:
- funzioni AI per i playable di AppLovin, Unity Luna, Mintegral e Google;
- startup già sul mercato con prodotti simili;
- prezzi attuali di agenzie e freelance per un playable.

## 7. GEMELLO: il magazzino in 3D da un video, con il riordino che taglia i chilometri — logistica di magazzino (layout e posizionamento degli articoli) (pmi)

- **Cosa fa:** Il responsabile cammina 15 minuti tra gli scaffali con un iPhone e carica l'export degli ordini. Il giorno dopo riceve tre cose:
- un gemello 3D navigabile del magazzino, con tutte le ubicazioni lette in automatico;
- i prelievi degli ultimi 90 giorni riprodotti nel 3D;
- un piano di spostamento degli articoli che riduce i metri percorsi dai magazzinieri.
- **Momento WOW:** Sul portatile compare il proprio magazzino in 3D fotorealistico. Si preme 'riproduci martedì scorso' e 1.900 righe d'ordine diventano puntini che corrono tra le corsie, con le zone più battute in rosso. Poi si preme 'ottimizza': i 300 articoli più venduti si spostano vicino alla baia di spedizione e il contatore segna '-24% di metri percorsi, circa 1,5 persone per turno'. Accanto c'è la lista ordinata dei 412 spostamenti da fare sabato mattina.
- **Perché era impossibile prima:** Tre anni fa servivano un rilievo con laser scanner (decine di migliaia di euro), un disegnatore CAD e settimane di consulenza in intralogistica. I software di posizionamento degli articoli esistevano solo nei WMS dei grandi. Tra il 2023 e il 2025 sono arrivati tre strumenti:
- Gaussian splatting e modelli di ricostruzione 3D (DUSt3R/MASt3R, VGGT), che ricavano in pochi minuti una scena in scala reale da un video di telefono;
- modelli visione-linguaggio, che leggono le etichette delle ubicazioni nei fotogrammi e le collegano alle coordinate;
- LLM che riportano su uno schema standard gli export disordinati dei gestionali.
- **Chi paga e quanto:** Paga il direttore operations o il titolare di un magazzino da 2.000 a 30.000 m²: e-commerce, distributori, 3PL.
- Primo gemello con analisi: 2.900 €.
- Abbonamento: 390–790 €/mese, con riposizionamento mensile e simulazioni 'cosa succede se' (nuove scaffalature, picchi stagionali).
- In seguito: un modulo di prelievo guidato con occhiali AI (vedi OCCHIO, assorbita qui) sugli stessi clienti.
35 abbonati a circa 590 €/mese e circa 20 nuovi gemelli l'anno fanno circa 300 k€. Per 1 M€ servono circa 120 abbonati in UE, oppure la rivendita tramite produttori di scaffalature e integratori di WMS.
- **Più di ChatGPT:** ChatGPT può spiegare la classificazione ABC. Non vede il magazzino e non conosce la distanza vera tra l'ubicazione A-12-3 e la baia 4. Non ha 90 giorni di righe d'ordine e non sa risolvere un'assegnazione su 8.000 articoli e 12.000 ubicazioni. Qui il cliente paga un risparmio misurato sul proprio layout e una lista di spostamenti pronta da eseguire.
- **Primo test:** Budget 9 k€, 8 settimane. Prodotto minimo in formato fisso, per non diventare consulenza.
- Il cliente carica l'export di ordini e ubicazioni e un video del magazzino.
- La pianta si ricostruisce in modo semiautomatico e l'ottimizzatore restituisce un report standard con la lista degli spostamenti.
- Prezzo 1.500 €, rimborsabile se il risparmio simulato è sotto il 10%.
- In parallelo, demo del gemello 3D su 2 magazzini amici.
- Contatto di 150 responsabili di magazzino in Italia e Spagna.
GO se pagano almeno 5 clienti, se in almeno 3 casi su 5 il risparmio simulato è del 15% o più e se almeno 2 clienti accettano l'abbonamento a 390 €/mese. STOP se pagano meno di 3 clienti o se il risparmio medio è sotto il 10%.
- **Rischi:** - Deriva verso la consulenza: formato fisso e pochi clienti nella fase iniziale.
- Magazzini ripetitivi che mettono in crisi la ricostruzione 3D.
- Export dei WMS con ubicazioni sbagliate o mancanti.
- Spostare la merce costa lavoro: il cliente può applicare il piano solo in parte e disdire dopo il primo riordino.
- Concorrenti: robot e droni di inventario (Dexory, Gather AI, Corvus), moduli di posizionamento nei WMS (Manhattan, Blue Yonder), SaaS dedicati. Pare che nessuno parta da un video di telefono (da verificare).
- **Nota del curatore:** PERCHÉ: il WOW visivo è forte (le righe d'ordine di martedì scorso che corrono tra le corsie) e il ROI si misura in persone per turno. Si regge su ottimizzazione combinatoria e ricostruzione 3D, entrambe competenze di Lorenzo.
AFFINAMENTO:
- primo test in formato prodotto fisso con rimborso, per evitare la consulenza;
- OCCHIO (occhiali per il prelievo) assorbita come modulo futuro sugli stessi clienti;
- per arrivare a 1 M€, rivendita tramite produttori di scaffalature e integratori WMS.
DA VERIFICARE:
- se VGGT e MASt3R reggono corsie ripetitive;
- SaaS di posizionamento degli articoli per PMI già sul mercato;
- se qualcuno costruisce già il gemello da un video di telefono.

## 8. PIANO B: tre piani di recupero in 40 secondi quando un jet resta a terra — aviazione d'affari e charter (operazioni di volo) (pmi)

- **Cosa fa:** Un aereo resta a terra per un guasto, o un pilota si ammala. L'agente legge dal software operativo la situazione reale di aerei ed equipaggi e in meno di un minuto propone tre piani di recupero completi: scambi di aereo, riassegnazioni di equipaggio, voli di trasferimento, sub-charter. Ogni piano è già verificato in modo formale sui limiti di tempo di volo e di servizio, con costo e impatto sui clienti.
- **Momento WOW:** Alle 05:52 il responsabile operativo scrive 'OK-ABC fermo a Olbia, perdita idraulica'. Dopo 40 secondi arrivano tre piani:
- A: 'Scambio con OK-XYZ da Linate; equipaggio Rossi/Bianchi in regola per altre 9h10; ritardo di 1h35 per 2 clienti; +6.400 €'.
- B: un'alternativa con un altro aereo e un altro equipaggio.
- C: 'Sub-charter, 3 offerte trovate'.
Con un clic il programma voli si aggiorna, e i messaggi per equipaggi e clienti sono già scritti.
- **Perché era impossibile prima:** Nelle grandi compagnie aeree la riprogrammazione ottimizzata dopo un imprevisto esiste da anni, con sistemi Sabre, Jeppesen o Lufthansa Systems da centinaia di migliaia di euro e team dedicati. Negli operatori con 5–40 aerei non è mai arrivata: si fa a mano, al telefono. Dal 2024–26 tre cose lo rendono possibile:
- gli LLM traducono i limiti di tempo di volo e il manuale operativo in vincoli formali verificabili;
- i risolutori CP-SAT trovano i piani in pochi secondi su cloud economico;
- i software operativi cloud dell'aviazione d'affari hanno API che un agente può leggere e aggiornare (da verificare per ciascuno).
- **Chi paga e quanto:** Pagano gli operatori di aviazione d'affari e charter con 5–40 aerei, gli operatori di elicotteri e le piccole compagnie che noleggiano aerei con equipaggio (ACMI). Prezzo: 150–250 €/aereo/mese, cioè 1.500–4.000 €/mese per operatore. 300 k€/anno = 12–18 operatori; in Europa ce ne sono alcune centinaia (da verificare). Ogni imprevisto gestito meglio vale migliaia di euro e soprattutto evita di perdere clienti VIP.
- **Più di ChatGPT:** ChatGPT non vede il programma voli, la storia dei turni dei piloti né la posizione degli aerei. Non garantisce che un piano rispetti i limiti di tempo di volo e non esplora milioni di combinazioni. Qui c'è un ottimizzatore collegato ai dati in tempo reale, con un controllo di legalità deterministico: alle 6 del mattino si paga un piano migliore e sicuro, in un minuto.
- **Primo test:** Circa 12 k€, 3 mesi, nessuna integrazione. Si chiedono a 2–3 operatori 6 mesi di storico (programmi, turni, imprevisti) e si rigiocano 30 casi reali in modalità ombra, confrontando i piani proposti con le decisioni prese davvero.
- GO se valgono tutte e tre:
  1. in almeno il 60% dei casi i responsabili operativi giudicano il piano proposto uguale o migliore per costo o ritardo;
  2. sui casi controllati non c'è nessun errore di legalità;
  3. almeno 2 operatori firmano un pilota a pagamento da almeno 1.500 €/mese.
- STOP se restano errori di legalità non correggibili, o se dopo 15 dimostrazioni nessuno paga.
- **Rischi:** - FL3XX, Leon e simili possono costruire la stessa funzione, e l'accesso alle API non è garantito.
- Un piano sbagliato crea responsabilità: serve sempre la conferma umana.
- Le operazioni vanno avanti 24 ore su 24 e i clienti si aspettano assistenza immediata, contro le 5–10 ore settimanali di Lorenzo.
- Il mercato è piccolo e conservatore.
- Lorenzo non ha esperienza di aviazione: serve un advisor del settore pagato a equity o a compenso, non un dipendente.
- **Nota del curatore:** PERCHÉ: porta in un settore nuovo la competenza più rara di Lorenzo, la verifica formale (il motore di legalità deve essere sempre corretto), insieme all'ottimizzazione CP-SAT. Per un responsabile operativo alle 6 del mattino il WOW è enorme, e ogni evento gestito vale migliaia di euro. La tecnologia è parente di PianoFabbrica, ma mercato, cliente e problema sono diversi.
AFFINAMENTO:
- prima la modalità ombra, senza integrazioni;
- poi un solo software operativo, possibilmente tramite il suo marketplace;
- un ex responsabile operativo come advisor.
DA VERIFICARE:
- API e marketplace di FL3XX e Leon, e se offrono già funzioni di recovery;
- numero di operatori in Europa;
- carico reale di assistenza richiesto.

## 9. FORMULA INVERSA: la ricetta di qualsiasi prodotto dalla foto dell'etichetta — alimentare confezionato e private label (R&D di formulazione) (pmi)

- **Cosa fa:** Dalla foto del retro di una confezione ricostruisce la ricetta in percentuali, con un intervallo di confidenza per ogni ingrediente. Poi propone 3 riformulazioni con ingredienti e prezzi reali dei fornitori: più economiche, con Nutri-Score migliore o con meno zucchero.
- **Momento WOW:** La responsabile R&D di un terzista che produce biscotti per la GDO fotografa il pacco del leader di mercato. In 20 secondi legge: 'farina di frumento 58,4% (±1,9), zucchero 19,2% (±1,1), olio di girasole 13,1% (±0,8)... aromi 0,2%', con accanto il grafico delle ricette compatibili. Un clic dopo arriva la 'versione B': stessa tabella nutrizionale entro le tolleranze, materie prime -11%, Nutri-Score B invece di C. In laboratorio la fanno il giorno stesso.
- **Perché era impossibile prima:** La matematica dell'inversione (vincoli d'ordine, QUID, bilanci nutrizionali) esiste da tempo. Mancava il pezzo che richiedeva un team di tecnologi alimentari: leggere etichette fotografate in 24 lingue e collegare ogni nome commerciale ('farina tipo 00', 'grassi vegetali', 'aromi') alla voce giusta delle banche dati di composizione (CREA, CIQUAL, USDA). Dal 2024–25 lo fanno i modelli visione-linguaggio, insieme alle stime delle perdite di processo (acqua persa in cottura, olio assorbito in frittura). Così un lavoro da consulenza diventa un prodotto self-serve, e si possono decodificare in blocco i circa 3 milioni di prodotti di Open Food Facts.
- **Chi paga e quanto:** Pagano:
- R&D e qualità dei terzisti di private label, migliaia in UE (la marca del distributore vale circa il 35–40% del largo consumo, dato da verificare);
- startup food;
- application lab dei fornitori di ingredienti.

Prezzi:
- Pro: 290 €/mese, con 30 decodifiche e 10 riformulazioni;
- Team: 790 €/mese;
- Enterprise: 18–36 k€/anno, con API e listini integrati.

40 Pro, 10 Team e 3 Enterprise fanno circa 310 k€. Verso 1 M€: la 'mappa del mercato' per i fornitori di ingredienti ('quali prodotti in UE potrebbero usare la mia fibra al posto dello zucchero'), a 25–50 k€/anno.
- **Più di ChatGPT:** ChatGPT dà percentuali verosimili che spesso non tornano: la somma non fa 100, l'ordine in etichetta non è rispettato e la tabella nutrizionale non quadra. FORMULA INVERSA invece:
- rispetta per costruzione tutti i vincoli;
- dà l'incertezza ingrediente per ingrediente;
- usa banche dati di composizione e prezzi reali;
- ha un'accuratezza misurata su ricette note;
- lavora in blocco su un'intera categoria.
- **Primo test:** Budget 8–12 k€.
1. MVP per frollini e sughi pronti.
2. Validazione su 30 prodotti a ricetta nota: 3 terzisti partner sotto NDA, più 15 ricette preparate apposta e fatte analizzare da un laboratorio accreditato (circa 3 k€).
3. Primo GO: errore assoluto mediano di 2 punti percentuali o meno sui primi 5 ingredienti.
4. 40 demo a responsabili R&D, su LinkedIn e alla fiera Marca di Bologna (gennaio 2027).
Secondo GO: entro 60 giorni almeno 5 abbonamenti da 250 €/mese o più, oppure 2 contratti annuali. STOP se l'errore supera 4 punti o se pagano meno di 2 clienti.
- **Rischi:** - Nei prodotti complessi molti ingredienti hanno composizione simile (zucchero e destrosio, oli diversi) e non si distinguono: la forchetta si allarga e il valore percepito cala.
- Può sembrare uno 'strumento per copiare', anche se usa solo informazioni pubbliche.
- La licenza ODbL di Open Food Facts obbliga a condividere le banche dati derivate, se pubblicate (da verificare).
- I software di etichettatura nutrizionale potrebbero offrire funzioni simili.
- Le PMI hanno budget R&D piccoli.
- **Nota del curatore:** PERCHÉ: unisce un WOW netto (la ricetta del leader di mercato in 20 secondi, con intervalli di confidenza) a un nucleo matematico vero: inversione bayesiana vincolata, campionamento sul politopo, MIP per riformulare. È self-serve e ha una strada credibile verso 1 M€ con la mappa del mercato per i fornitori di ingredienti.
AFFINAMENTO: pubblicare il benchmark di accuratezza come arma di vendita. Posizionare il prodotto su riformulazione e costo, non sulla copia.
DA VERIFICARE:
- concorrenti come Spoonshot, Journey Foods, NotCo e le suite di etichettatura nutrizionale;
- vincoli della licenza ODbL;
- disponibilità a pagare dei terzisti private label in IT/DE/ES.

## 10. MISCELA: la stessa miscela di caffè, con i lotti di questa settimana e meno costi — caffè (torrefazioni) (pmi)

- **Cosa fa:** Quando il caffè verde rincara o un lotto finisce, ricostruisce la miscela firma della torrefazione con i lotti davvero disponibili dagli importatori, al costo minimo. Stima la probabilità che un panel di assaggio si accorga della differenza e indica il profilo di tostatura. Impara a ogni cupping successivo.
- **Momento WOW:** Il torrefattore carica i listini PDF dei suoi tre importatori e la ricetta della 'Miscela Bar Oro'. In 30 secondi legge: '35% Brasile Cerrado lotto 4471, 25% India Cherry AB, 20% Uganda Robusta scr.18, 20% Honduras SHG. Costo -0,58 €/kg (-87 k€ l'anno sui tuoi volumi). Probabilità che un panel la distingua in un test triangolare: 31% (il caso puro è 33%)'. Il cupping alla cieca del giorno dopo gli dà ragione.
- **Perché era impossibile prima:** Tre fattori recenti:
- la crisi dei prezzi: nel 2024–25 arabica e robusta hanno toccato livelli record, con l'arabica oltre 4 $/lb a febbraio 2025;
- gli LLM che leggono offerte e schede di cupping eterogenee (PDF, email, Excel in più lingue) e raccolgono a voce le note di assaggio: tre anni fa servivano settimane di inserimento manuale;
- i modelli sensoriali gerarchici, che imparano da molte torrefazioni insieme.
Prima l'ottimizzazione della miscela era teoria: mancavano dati strutturati e un modo di prevedere il gusto.
- **Chi paga e quanto:** Pagano le torrefazioni medie, da 300 a 20.000 t/anno. In Italia sono circa 800–1.000, quasi tutte con miscele per il bar (dato da verificare); in Europa diverse migliaia.
- Prezzo: 500–1.500 €/mese in base ai volumi.
- Valore per il cliente: l'1% del costo del verde su 1.000 t a 8 €/kg vale 80 k€/anno.
- 300 k€: circa 35 torrefazioni a 700 €/mese.
- Verso 1 M€: Germania, Francia, Spagna e USA, più licenze agli importatori, che offrirebbero il 'blend matching' ai propri clienti.
- **Più di ChatGPT:** ChatGPT suggerisce sostituzioni generiche ('usa un Brasile al posto del Colombia'). Non conosce l'impronta sensoriale misurata della tua miscela né i lotti e i prezzi reali di questa settimana. Non calcola la probabilità che il panel noti la differenza, non ottimizza il costo sotto vincoli e non impara dai tuoi cupping successivi.
- **Primo test:** Budget 6–10 k€.
1. Tre torrefazioni partner forniscono lo storico delle miscele e dei cupping.
2. Si riformulano 3 miscele; verde e tostature sul tostino di prova costano 1–2 k€.
3. Test triangolari alla cieca con lo staff e con 30 consumatori per miscela.
4. Primo GO: almeno 2 riformulazioni su 3 non distinte (p > 0,05 con n ≥ 30) e risparmio di almeno 0,30 €/kg.
5. 30 demo.
Secondo GO: entro 90 giorni almeno 5 torrefazioni pagano 400 €/mese o più. STOP se il panel distingue la maggioranza delle riformulazioni o se pagano meno di 3 clienti.
- **Rischi:** - La cultura del 'palato del mastro torrefattore' resiste agli algoritmi.
- Se i prezzi del verde scendono, cala l'urgenza. Resta però il bisogno di continuità, perché i lotti finiscono ogni stagione.
- Cropster ha già magazzino del verde e cupping e potrebbe aggiungere questa funzione.
- Gli importatori danno consigli gratis.
- Esistono approcci simili in campi vicini (Tastry nel vino).
- Le piccole torrefazioni pagano poco.
- **Nota del curatore:** PERCHÉ: il ROI è immediato (una torrefazione media risparmia decine di migliaia di euro l'anno) e il WOW si verifica al cupping del giorno dopo. Unisce statistica sensoriale (modelli thurstoniani) e ottimizzazione robusta: matematica applicata al gusto. Il settore è nuovo e ha un forte legame con l'Italia, che può essere il mercato di partenza.
AFFINAMENTO: posizionarla come R&D sensoriale e continuità della miscela, non come strumento di acquisto (settore già esplorato). Per arrivare a 1 M€, licenza agli importatori.
DA VERIFICARE:
- prezzi del verde a fine 2026, da cui dipende l'urgenza;
- funzioni di Cropster e Artisan;
- startup di ottimizzazione delle miscele;
- numero reale di torrefazioni in IT e UE.

## 11. MORFO: la sequenza di movimenti calcolata per il tuo corpo, da 15 secondi di video — arrampicata sportiva (palestre e board) (mixed)

- **Cosa fa:** Inquadri un blocco o una board di allenamento e l'app ricostruisce la geometria e riconosce le prese. Poi mostra un avatar con la tua altezza, apertura delle braccia e peso che sale con la sequenza più adatta a te, e stima il grado per la tua corporatura. Alle palestre dà, per ogni nuovo blocco, il grado per corpi diversi e quanto dipende dall'altezza.
- **Momento WOW:** Una climber di 1,58 m è bloccata sul passo chiave che i ragazzi alti risolvono con un lancio. Filma il blocco per 15 secondi. Circa 30 secondi dopo vede il suo avatar, con le sue proporzioni, che invece del lancio fa un tallonaggio sulla presa 9 e un incrocio sulla 11, mentre le due prese si illuminano in AR sulla parete vera. Sotto compare: 'Per te 6B+; per un 1,85 m 6A'. Al tentativo successivo lo chiude.
- **Perché era impossibile prima:** Servono tre capacità arrivate tra il 2024 e il 2025:
- ricostruzione 3D metrica da un video di telefono in pochi secondi (DUSt3R/MASt3R 2024, VGGT 2025, LiDAR degli iPhone Pro), invece di ore di fotogrammetria;
- segmentazione zero-shot delle prese (SAM 2);
- simulatori fisici su GPU (MuJoCo MJX, Warp) che provano migliaia di sequenze in pochi secondi.
Nel 2017 sintetizzare i movimenti di arrampicata era un articolo SIGGRAPH, con ore di calcolo su pareti modellate a mano. Nessuno l'avrebbe immaginato come app da 5 € al mese.
- **Chi paga e quanto:** - Climber: 3 blocchi al mese gratis, poi 6,99 €/mese o 49 €/anno.
- Palestre: 149–299 €/mese per sede. Ogni nuovo blocco riceve in automatico il grado per diverse corporature, un 'indice di dipendenza dall'altezza' per i tracciatori e un video della sequenza via QR.
- Produttori di board standard (Kilter, Tension, Moon): licenza.
4.000 abbonati (circa 200 k€) e 150 palestre (circa 360 k€) fanno circa 0,55 M€. USA e Regno Unito portano verso 1 M€.
- **Più di ChatGPT:** Da una foto ChatGPT dà consigli generici ('usa i piedi'). Non sa fare nessuna di queste cose:
- misurare in centimetri le distanze tra le prese;
- sapere se il TUO braccio ci arriva;
- verificare l'equilibrio di una posizione;
- generare il video di un corpo con le tue proporzioni che sale quel blocco;
- dare alla palestra statistiche sui blocchi tracciati.
Il valore sta nella geometria misurata unita alla simulazione fisica personalizzata.
- **Primo test:** Costo circa 12 k€, in 8 settimane:
- 5 palestre partner (Italia, Germania, Francia) forniscono 60 blocchi più problemi su board standard;
- sequenze generate per 3 tipi di corporatura;
- 4 k€ di ads Instagram/TikTok su climber in 4 paesi;
- prevendita founding a 29 €/anno.
GO se valgono tutte e tre:
1. su 100 climber, chi vede la sequenza AI chiude il blocco entro 3 tentativi almeno 15 punti percentuali più spesso del gruppo di controllo;
2. almeno 300 prevendite, con costo di acquisizione entro 15 €;
3. almeno 3 palestre su 5 firmano una lettera d'intenti a 149 €/mese o più.
STOP con meno di 100 prevendite, o se meno del 50% dei tester giudica la sequenza utile.
- **Rischi:** - Fedeltà della simulazione: una sequenza sbagliata brucia la fiducia.
- Molti climber non vogliono la soluzione già pronta ('no beta spray'): servono suggerimenti a livelli, da 'guarda la presa 9' al video completo.
- Le app di palestra già diffuse (TopLogger, Vertical-Life, Griptonite, Kaya, Stokt) potrebbero aggiungere funzioni simili.
- I dati delle board (Aurora/Kilter) sono proprietari.
- Da verificare il numero di palestre e la disponibilità a pagare dei tracciatori.
- **Nota del curatore:** PERCHÉ: uno dei WOW più forti e personali della lista: un avatar con le tue proporzioni che risolve il blocco su cui sei fermo. Il cuore è ottimizzazione vincolata e geometria computazionale. Ha due fonti di ricavo, climber e palestre, ed è uno sport nuovo rispetto al padel.
AFFINAMENTO:
- partire dalle board standard, dove la disposizione delle prese è nota e il pubblico è già abituato a un'app: si accorcia molto il percorso tecnico;
- suggerimenti a livelli per rispettare la cultura 'no beta spray'.
DA VERIFICARE:
- se Kilter/Aurora, Stokt, Crimpd o altre startup simulano già sequenze personalizzate per corporatura;
- licenze dei dati delle board;
- numero di palestre in UE e USA.

## 12. VERSO: la tua canzone cantata da te in spagnolo, inglese e giapponese, con le rime che tornano — musica e localizzazione linguistica (mixed)

- **Cosa fa:** Un artista carica il master. Il sistema separa la voce e scrive una traduzione cantabile, vincolata a melodia, accenti e rime. La fa cantare con la voce dell'artista e una pronuncia da madrelingua, poi restituisce il mix pronto per la distribuzione e, se serve, il video con il labiale sincronizzato.
- **Momento WOW:** Un cantautore italiano carica 'Notte a Milano' e sceglie lo spagnolo. Otto minuti dopo ascolta il ritornello cantato da lui, con la stessa grana di voce e gli stessi respiri. Al posto di 'sera/vera' c'è 'noche/coche', e ogni sillaba cade sulla stessa nota. Lo fa sentire a un amico messicano, che non si accorge che è una traduzione.
- **Perché era impossibile prima:** Nel 2023 HYBE e Supertone fecero cantare un artista K-pop in sei lingue (progetto MIDNATT), con lavoro manuale e madrelingua veri. Dal 2024–26 ogni pezzo della catena si può automatizzare:
- separazione della voce con qualità da studio (BS-RoFormer, Demucs);
- conversione e sintesi della voce cantata zero-shot, con controllo dei fonemi;
- LLM che rispettano vincoli prosodici quando un verificatore li controlla;
- lipsync video (LatentSync, MuseTalk).
Tre anni fa un brano così era una produzione da decine di migliaia di euro; oggi costa pochi euro di calcolo.
- **Chi paga e quanto:** - Artisti indipendenti: 49 € per brano e per lingua, 149 € per 4 lingue, video con labiale +39 €.
- Etichette ed editori: abbonamento per il catalogo, 1.500–5.000 €/mese.
- Canale: upsell dentro i distributori digitali (DistroKid, TuneCore, Believe, Amuse) in revenue share, da verificare.
6.000 versioni l'anno (circa 300 k€) e 10 etichette a 24 k€ (240 k€) fanno circa 0,54 M€.
- **Più di ChatGPT:** ChatGPT traduce il testo, ma:
- non lo fa stare sulle note;
- non lo canta con la tua voce e la pronuncia giusta;
- non restituisce un master pubblicabile né il video sincronizzato.
Per rendere un testo cantabile serve un ciclo di audio, misura e correzione su ogni sillaba, che un chatbot non esegue.
- **Primo test:** Costo circa 9 k€, in 6 settimane:
- pipeline dall'italiano verso spagnolo e inglese;
- 2 k€ per raggiungere 300 artisti indipendenti (Instagram, SubmitHub, Groover), con un ritornello di 30 secondi gratis;
- brano completo a 49 €;
- panel cieco di 30 madrelingua su Prolific (1 k€).
GO se almeno il 25% dei campioni gratuiti diventa un brano pagato, con almeno 40 brani pagati, e se il panel giudica la naturalezza almeno 3,8 su 5 in media. STOP con conversione sotto il 10% o naturalezza sotto 3 su 5.
- **Rischi:** - Diritti: una traduzione è un'opera derivata e serve il consenso di autore ed editore. Si parte dai cantautori autoprodotti; per i cataloghi va negoziato.
- Regole sull'AI: piattaforme e distributori chiedono trasparenza e vietano le imitazioni non autorizzate; l'art. 50 dell'AI Act impone la marcatura dei contenuti sintetici.
- Rischio di piattaforma alto: Suno, Udio, ElevenLabs o i distributori potrebbero aggiungere 'traduci la tua canzone'.
- Effetto innaturale e accoglienza dei fan.
- **Nota del curatore:** PERCHÉ: il WOW è emotivo e globale: la tua canzone cantata da te in spagnolo, con le rime che tornano. Il pezzo difficile, il traduttore vincolato a melodia, accenti e rime, è un problema di ottimizzazione combinatoria adatto a un matematico. Il settore è nuovo.
AFFINAMENTO:
- canale B2B2C dentro distributori digitali ed etichette, invece di acquisire artisti uno a uno;
- consenso esplicito dell'artista e watermark sempre.
DA VERIFICARE:
- chi offre già la traduzione cantata con la voce dell'artista (Supertone/HYBE, ElevenLabs, Suno, startup);
- regole di Spotify e dei distributori sulle voci AI;
- qualità attuale della sintesi cantata in altre lingue.

## 13. RAFFICA: vedere il vento sull'acqua 30 secondi prima che arrivi — vela, kitesurf e wingfoil (consumer)

- **Cosa fa:** Uno smartphone o un'action cam, in testa d'albero, sul gommone dell'allenatore o su un treppiede rialzato a riva, legge la texture dell'acqua sopravento. In realtà aumentata disegna le raffiche e i salti di vento in arrivo, con intensità, direzione e secondi all'arrivo. In allenamento una voce avvisa: 'raffica +4 nodi tra 20 secondi, ti ruota di 8 gradi a destra'.
- **Momento WOW:** Inquadri il campo di regata con il telefono. Le chiazze scure sull'acqua, che solo i tattici esperti sanno leggere, diventano frecce colorate con scritto '+5 kn, 25 s, buono'. Venticinque secondi dopo la raffica arriva come annunciato, e l'anemometro di bordo lo conferma in diretta sullo stesso schermo.
- **Perché era impossibile prima:** Servono tre cose diventate accessibili solo ora:
- le NPU dei telefoni 2024–26, che fanno girare in tempo reale reti video spazio-temporali;
- l'addestramento auto-supervisionato: il vento misurato dagli strumenti di bordo nei 10–60 secondi successivi etichetta in automatico ogni fotogramma, e così si ottengono milioni di esempi senza annotatori;
- i modelli meteo AI (ECMWF AIFS, operativo dal 2025) come contesto a costo zero.
Prima la lettura delle raffiche era solo esperienza umana, e i sensori remoti del vento (LiDAR Doppler) costano decine di migliaia di euro e non stanno su una deriva.
- **Chi paga e quanto:** - Kiter, winger e velisti: 12,99 €/mese o 99 €/anno.
- Team e scuole vela, per l'allenamento: 49 €/mese, con più barche e analisi dopo l'uscita.
- Produttori di strumenti di bordo (B&G, Garmin, Vakaros): licenza come funzione, interesse da verificare.
4.000 abbonati a 99 € fanno circa 400 k€. Che i velisti paghino abbonamenti meteo lo dimostra PredictWind (prezzi e numeri da verificare).
- **Più di ChatGPT:** ChatGPT non vede il tuo campo di regata in questo momento, non lavora a 10 fotogrammi al secondo, non è calibrato sulla fisica dell'acqua increspata e non è collegato al tuo anemometro. Anche le migliori previsioni meteo lavorano su griglie di chilometri e intervalli di ore. Qui si parla di 300 metri e 30 secondi.
- **Primo test:** Budget circa 15 k€, in due fasi con un cancello tecnico.
Fase 1, tecnica (circa 7 k€, 8–10 settimane):
- action cam in testa d'albero su 2 gommoni di allenatori e 2 camere rialzate a riva;
- spot con vento affidabile anche in inverno (Tarifa, Canarie, Lo Stagnone), oppure il Garda da aprile;
- 60 ore di video sincronizzate con gli anemometri e modello addestrato in cloud.
GO tecnico se, su dati mai visti, il modello rileva almeno il 70% delle raffiche da +3 nodi con almeno 15 s di anticipo e al massimo il 30% di falsi allarmi. STOP sotto il 50%.
Fase 2, mercato (circa 6 k€, solo se la fase 1 passa):
- video demo e landing in 4 lingue;
- prevendita founding a 59 €/anno a kiter, winger e velisti.
GO con almeno 250 prevendite. STOP sotto 80.
- **Rischi:** - Fattibilità ottica (riflessi, controluce, mare mosso, vento debole che non lascia texture): è il rischio numero uno e va misurato per primo.
- In regata la RRS 41 e molte regole di classe limitano i dispositivi elettronici tattici. Il mercato iniziale è quindi allenamento, kite, wing, crociera e le classi d'altura dove sono ammessi.
- Stagionalità e hardware esposto all'ambiente marino.
- Non è chiaro se esistano già startup di 'wind vision' da camera: da verificare.
- Va posizionato come strumento di prestazione, non di sicurezza.
- **Nota del curatore:** PERCHÉ: è la scommessa ad alto WOW della lista: rende visibile ciò che oggi solo i tattici esperti sanno leggere. L'auto-etichettatura con l'anemometro di bordo è elegante e permette di scalare senza annotatori. Tocca i valori di Lorenzo (sport, mare, scienza) senza ricadere in padel o viaggi.
AFFINAMENTO:
- test diviso in due fasi: prima la fattibilità ottica su dati registrati, poi la prevendita;
- partire da kite e wing, dove non ci sono regolamenti di regata, e dalle camere rialzate a riva;
- siamo a metà ottobre, quindi conviene usare spot invernali.
DA VERIFICARE:
- letteratura sulla stima del vento dalla rugosità dell'acqua ripresa da camera;
- startup o funzioni esistenti;
- RRS 41 classe per classe;
- numero di kiter e winger in UE.

## 14. CONTROPROVA: prima di finanziare una scoperta, un'AI rifà i conti dei paper su cui si basa — integrità della ricerca e due diligence scientifica (enterprise)

- **Cosa fa:** Un fondo o un'azienda carica i paper e i brevetti dietro uno spinout o una licenza. Agenti AI:
- scaricano dati supplementari e codice;
- ricalcolano le statistiche;
- cercano immagini duplicate nella letteratura;
- rieseguono le analisi in sandbox;
- controllano ritrattazioni e repliche indipendenti.
In mezz'ora si ha un punteggio di solidità per ogni risultato chiave, con le prove e le domande da fare ai fondatori.
- **Momento WOW:** Il partner di un fondo deep tech carica i 14 paper dietro un seed da 3 M€. Dopo 25 minuti legge:
- 'Il risultato chiave 2 (efficienza del catalizzatore 94%) si regge sulla figura 3, e il pannello 3c è un duplicato ruotato di 90° di un pannello dello stesso gruppo del 2020 (sovrapposizione allegata).'
- 'Tabella 2: 4 medie su 9 sono impossibili con n=12.'
- 'Il codice condiviso riproduce la figura 4, ma cambiando il seme casuale l'effetto si dimezza.'
- 'Nessuna replica indipendente nei 37 paper che lo citano.'
- **Perché era impossibile prima:** Fino al 2023 questo lavoro lo facevano a mano pochi investigatori, come Elisabeth Bik o il gruppo di Data Colada, un paper alla volta. Dal 2024–26:
- gli agenti LLM leggono paper e tabelle supplementari, scrivono ed eseguono codice e riproducono una parte crescente dei risultati pubblicati (PaperBench, CORE-Bench);
- il database di Retraction Watch è aperto dal 2023 grazie a Crossref;
- progetti come Black Spatula hanno mostrato che gli LLM trovano errori reali nei paper.
- **Chi paga e quanto:** Pagano:
- fondi di venture capital deep tech e biotech, e corporate venture;
- team di licensing di aziende chimiche, dei materiali e farmaceutiche;
- uffici di trasferimento tecnologico.
Prezzi: report per singola operazione 2,5 k€ (self-serve), abbonamento illimitato 30 k€/anno per fondo. 10 fondi e 60 report fanno 450 k€. Verso 1 M€ con i team di licensing delle grandi aziende.
- **Più di ChatGPT:** ChatGPT riassume il paper e gli crede. Non può:
- ricalcolare in modo deterministico ogni statistica;
- confrontare le immagini con migliaia di altri paper;
- rieseguire il codice in sandbox;
- consultare in modo sistematico ritrattazioni e repliche.
CONTROPROVA consegna un fascicolo di prove verificabili, non un riassunto.
- **Primo test:** Budget 8–12 k€.
1. Benchmark su 100 paper ritrattati per problemi di dati (dal database di Retraction Watch) e su 100 paper di controllo, in materiali, chimica e AI. GO tecnico con AUC di almeno 0,8 e allarmi rossi su non più del 10% dei controlli.
2. Audit gratuito di un'operazione passata, offerto a 25 fondi deep tech europei.
GO se entro 3 mesi almeno 3 fondi comprano un report da 2 k€ o più, oppure 1 firma una lettera d'intenti per l'abbonamento annuale. STOP se nessuno paga.
- **Rischi:** - Diffamazione e reputazione: i report devono parlare di 'incoerenze da chiarire', mai di frode, e restare riservati.
- Falsi positivi.
- I PDF a pagamento li carica il cliente.
- Nicchia: qualche migliaio di fondi e team di licensing nel mondo.
- Concorrenza: chi oggi vende agli editori (Proofig, Imagetwin, Clear Skies, STM Integrity Hub) potrebbe spostarsi sugli investitori; YesNoError e Black Spatula sono gratuiti.
- Restare lontani dalla ricerca clinica, per il filtro sui claim clinici.
- **Nota del curatore:** PERCHÉ: è il prodotto più 'scienza e matematica' della lista (GRIM, GRIMMER, SPRITE, p-curve, rilevamento delle duplicazioni). Per un investitore il WOW è immediato: 'il pannello 3c è un duplicato ruotato'. È self-serve, richiede poche ore di supporto e i clienti pagano bene. Il settore è del tutto nuovo.
AFFINAMENTO:
- partire da materiali, chimica e AI, lontano da qualsiasi claim clinico;
- linguaggio sempre di 'incoerenze da chiarire', report riservati;
- seconda fase per i team di licensing corporate.
DA VERIFICARE:
- chi vende già agli investitori (Proofig, Imagetwin, Clear Skies, YesNoError, Black Spatula);
- disponibilità a pagare dei fondi deep tech europei;
- aspetti legali dell'elaborazione di PDF protetti.

## 15. CARTELLO: il foglio A4 che dirotta il robot. Red teaming fisico automatico per robot guidati da modelli visione-linguaggio — sicurezza della robotica e dell'AI incarnata (enterprise)

- **Cosa fa:** Per chi costruisce robot, droni e telecamere intelligenti che 'leggono' il mondo con modelli visione-linguaggio. In simulazione, su una replica 3D del sito del cliente, la piattaforma cerca gli attacchi fisici realizzabili: scritte, adesivi, cartelli, oggetti disposti ad arte che fanno fare al robot la cosa sbagliata. Ne misura la probabilità di successo e consegna il kit stampabile per verificarli sul robot vero, insieme alle difese.
- **Momento WOW:** Nel video di demo un braccio robotico riceve l'ordine 'metti i bicchieri rossi nel cestino'. Sul tavolo c'è un foglio A4 stampato da CARTELLO, con un disegno innocuo e una scritta minuscola, e il robot butta nel cestino il portatile. Sotto compare: 'Successo nel 74% di 200 condizioni simulate di luce e angolazione; verificato dal vero 7 volte su 10'. Il CTO di un'azienda di robotica chiede di provarlo sul suo modello.
- **Perché era impossibile prima:** Fino al 2023 i robot non interpretavano la scena con un modello linguistico, quindi una scritta su un foglio non poteva dar loro ordini. Dal 2023–25 i modelli visione-linguaggio-azione (VLA) leggono il testo nella scena e lo seguono: RT-2, OpenVLA, π0 con pesi aperti, Gemini Robotics, GR00T N1, SmolVLA. È una superficie d'attacco nuova. In più i gemelli digitali da Gaussian splatting e i simulatori su GPU permettono a una sola persona di fare migliaia di prove al giorno.
- **Chi paga e quanto:** Pagano le aziende di robot umanoidi e di magazzino, di droni, di veicoli autonomi che usano VLM e di telecamere intelligenti; in seguito enti di prova e assicuratori.
- Valutazione self-serve: 6 k€.
- Abbonamento continuo: 40 k€/anno.
9 abbonamenti e 15 valutazioni fanno 450 k€. Verso 1 M€ con l'ondata di robot umanoidi in produzione nel 2027–28 e con licenze ai laboratori di prova.
- **Più di ChatGPT:** ChatGPT può elencare gli attacchi noti, ma non può:
- ottimizzare una patch fisicamente robusta contro il tuo modello;
- provarla 10.000 volte in una replica del tuo magazzino;
- stimare il tasso di successo con un intervallo di confidenza;
- consegnarti il foglio da stampare per la verifica sul robot vero e il dataset per difenderti.
- **Primo test:** Budget 10–15 k€: GPU, un braccio robotico economico (SO-101 di LeRobot oppure uno da 3–5 k€), stampe.
1. Attacchi contro 3 VLA open (OpenVLA, π0, SmolVLA) e 2 agenti basati su VLM.
2. Rapporto tecnico e video, con divulgazione responsabile, per attirare contatti.
3. Assaggio gratuito di 10 attacchi offerto a 30 aziende di robotica.
GO se entro 4 mesi almeno 3 aziende comprano una valutazione da 5 k€ o più, oppure 2 firmano una lettera d'intenti per l'abbonamento. STOP se dopo 20 conversazioni qualificate nessuno paga.
- **Rischi:** - Doppio uso: divulgazione responsabile e clienti verificati.
- I clienti oggi sono pochi e potrebbero fare il red teaming in casa.
- Il red teaming AI generalista è affollato (Mindgard, HiddenLayer, Haize Labs, Lakera passata a Check Point); da verificare se esistono già attori specifici per i robot.
- I modelli proprietari sono difficili da raggiungere.
- Il divario tra simulazione e realtà può ridurre la credibilità.
- Cyber Resilience Act e Regolamento Macchine (dal 2027) spingono la domanda, ma il prodotto non deve diventare carte di conformità.
- **Nota del curatore:** PERCHÉ: è il WOW più cinematografico della lista (un foglio A4 che fa buttare il portatile nel cestino) e arriva al momento giusto: i robot guidati da VLA entrano in produzione nel 2027–28 e la superficie d'attacco è nuova. Lorenzo, ingegnere AI, può costruirlo da solo con modelli open e un braccio economico.
AFFINAMENTO:
- il primo rapporto pubblico, con divulgazione responsabile, fa insieme da ricerca e da marketing;
- vendere valutazioni self-serve in container, senza progetti su misura.
DA VERIFICARE:
- numero reale di aziende con robot basati su VLA in UE e USA;
- red teamer già specializzati in robotica;
- interesse di laboratori di prova (TÜV, DEKRA) e assicuratori;
- requisiti del Regolamento Macchine.

## 16. SMALTO: fotografi un colore, l'AI inventa lo smalto ceramico e ti mostra il pezzo cotto prima di accendere il forno — ceramica e chimica degli smalti (mixed)

- **Cosa fa:** Per ceramisti e studi di ceramica, e poi per i produttori di smalti. Dalla foto di un colore o di una superficie, l'AI progetta la ricetta dello smalto con i materiali che hai sullo scaffale. Ne verifica la chimica (dilatazione termica, assenza di piombo) e ti mostra in modo fotorealistico come uscirà sul tuo pezzo. Poi impara dalle foto delle tue piastrelle di prova come si comporta il tuo forno.
- **Momento WOW:** Una ceramista carica la foto del mare di Capri a mezzogiorno. In 20 secondi sullo schermo ruotano tre ciotole in quel turchese esatto, che sui bordi vira al marrone. Ognuna ha una ricetta fatta con i 9 materiali del suo scaffale: 'probabilità di ottenerlo alla prima cottura 62%; dopo le 6 piastrelle di prova suggerite 91%'. Dopo la cottura fotografa la piastrella e l'app risponde: 'il tuo forno riduce sul ripiano alto: aggiungi il 2% di silice'.
- **Perché era impossibile prima:** I calcolatori di smalti (Insight di Digitalfire, Glazy) calcolano la formula chimica. Nessuno però sa dire che aspetto avrà lo smalto, né risalire dall'aspetto alla ricetta. Oggi ci sono quattro elementi nuovi:
- database aperti di decine di migliaia di ricette con foto delle cotture (Glazy; numero e licenza da verificare);
- modelli visione-linguaggio che descrivono la superficie cotta;
- generatori d'immagine controllabili che rendono uno smalto plausibile su una forma vera fotografata col telefono;
- ottimizzazione bayesiana che impara da poche prove reali.
- **Chi paga e quanto:** - Ceramisti amatori e professionisti: 7,90 €/mese o 69 €/anno.
- Studi e scuole di ceramica con più forni: 29 €/mese.
- Produttori di smalti (Amaco, Mayco, Botz), poi l'industria di smalti e fritte per piastrelle (Castellón, Sassuolo): API di 'cottura virtuale' a 15–40 k€/anno.
3.000 abbonati annuali, 150 studi e 4 licenze B2B fanno circa 380 k€. La strada verso 1 M€ passa dall'industria delle piastrelle.
- **Più di ChatGPT:** ChatGPT ti dà una ricetta di 'turchese' presa da internet, ma:
- non sa come uscirà con i tuoi materiali e il tuo forno;
- non te la mostra sul tuo pezzo;
- non garantisce la compatibilità con l'argilla né l'assenza di piombo;
- non impara dalle tue cotture.
Il fossato è il dataset delle cotture reali, che cresce a ogni utente.
- **Primo test:** Budget 8–12 k€.
1. Prototipo web 'foto → ricetta → anteprima', costruito sui dati aperti.
2. 30 ceramisti beta cuociono le ricette suggerite.
3. 4–5 k€ di collaborazioni con creator di ceramica su TikTok e Instagram (USA, Regno Unito, Germania, Italia), con prevendita del piano annuale a 49 €.
GO se, in un test alla cieca su 40 cotture, almeno il 60% è giudicato 'vicino' o 'molto vicino' all'anteprima, e se in 8 settimane arrivano almeno 300 prevendite (oppure 1 lettera d'intenti di un produttore di smalti). STOP sotto il 40% di somiglianza o sotto le 100 prevendite.
- **Rischi:** - Forno, argilla e spessore possono deludere: il prodotto deve vendere probabilità e prove guidate, non magia.
- Licenza dei dati: Glazy potrebbe essere non commerciale, quindi serve una partnership.
- La disponibilità a pagare degli hobbisti è da verificare.
- Materiali tossici (bario, manganese, litio): solo avvertenze, mai dichiarazioni di idoneità al contatto con gli alimenti.
- Glazy o Digitalfire potrebbero aggiungere l'AI.
- **Nota del curatore:** PERCHÉ: unisce scienza (chimica UMF, dilatazione termica), design e un WOW immediato (fotografi il mare di Capri, vedi la ciotola cotta) in un settore mai esplorato. Il fossato di dati cresce a ogni cottura. È un prodotto consumer globale con una strada B2B verso l'industria degli smalti e delle fritte, dove l'Italia (Sassuolo) è un polo mondiale.
AFFINAMENTO:
- vendere probabilità e piastrelle di prova guidate, mai promesse;
- nessuna dichiarazione sul contatto alimentare, per non scivolare nella burocrazia;
- partnership sui dati invece di scraping.
DA VERIFICARE:
- licenza dei dati Glazy;
- funzioni AI in Glazy e Digitalfire;
- dimensione e disponibilità a pagare della comunità ceramica in USA, Regno Unito e Germania;
- interesse di un produttore di fritte del distretto di Sassuolo o di Castellón.

## Scartate dal curatore

| Idea | Motivo |
|---|---|
| NODO: la mappa che prevede dove la rete elettrica europea ha ancora posto | Solido ma affollato da attori finanziati (Paces, LandTech, Continuum, Aurora, Modo). Le vendite enterprise portano il tempo richiesto al limite delle 10 h/settimana, e il WOW è professionale più che inimmaginabile. Resta come riserva. |
| RAGGI X: vedere tubi e cavi dentro i muri, anni dopo, con il telefono | Il valore arriva anni dopo la cattura e richiede che gli installatori adottino un'abitudine nuova. Il riallineamento AR dopo anni non è dimostrato e la crescita virale è lenta. |
| AGORÀ: 300 persone simulate vivono il tuo ufficio prima che esista | Il realismo degli agenti LLM non è validato. Ogni progetto rischia di diventare consulenza, le vendite enterprise sono lente e la calibrazione richiede dati badge sotto GDPR. |
| MESCOLA: lo stesso calcestruzzo con il 15% di cemento in meno | Ci sono concorrenti diretti ben finanziati (Alcemy, Concrete.ai, Converge, Giatec). Il settore è conservatore, con responsabilità EN 206, e l'avvio di ogni impianto scivola verso la consulenza. Il WOW è solo economico. |
| ALIBI: il gioco investigativo infinito con sospettati che mentono | È troppo vicino ai settori di gioco già esplorati (giochi matematici e party game). Il mercato indie vive di pochi successi e i ricavi sono imprevedibili. Servono 9–12 mesi più una direzione artistica. |
| LUMEN: il light designer AI che ascolta la band e programma lo show | Il supporto a hardware DMX eterogeneo supera le 5–10 h/settimana. SoundSwitch e rekordbox Lighting coprono già i DJ e le band hanno budget bassi con disdette frequenti. È anche vicino al settore eventi già esplorato. |
| MONTA: dal file CAD al manuale di montaggio stile IKEA con AR | BILT e Cadasio esistono già e molte PMI non hanno un CAD pulito. I cicli B2B nel mobile sono lunghi, c'è il rischio di diventare un servizio di illustrazione e il WOW resta B2B. |
| MOTIVO: il DNA sonoro del marchio che compone ogni colonna sonora | La concorrenza diretta è forte: Adobe Firefly Soundtrack, ElevenLabs Music e i modelli personalizzati per i brand di Stable Audio. La domanda è debole, perché pochi marchi hanno un logo sonoro, e ci sono rischi sui diritti. |
| PUNTO: da un logo al file di ricamo perfetto in 20 secondi | Il WOW è basso, come ammette la scheda stessa. Gli incumbent (Wilcom, Hatch, Brother Artspira) stanno aggiungendo la digitalizzazione automatica con AI e i digitalizzatori all'estero costano poco. |
| TIMBRO: senti il clic del prodotto prima che esista | Richiede 9–15 mesi di lavoro di livello ricerca, in una nicchia enterprise con cicli lunghi incompatibile con 5–10 h/settimana. Il canale delle confezioni di lusso è vicino alla cosmetica, già esplorata. |
| TROVAPACCO: il furgone che sa dov'è ogni pacco | Amazon ha già il suo sistema e i corrieri impongono palmari bloccati. I subappaltatori hanno margini bassissimi, e le telecamere sul lavoro toccano l'art. 4 dello Statuto dei lavoratori. |
| RITORNO PIENO: il dispatcher AI che telefona ai broker | Il meccanismo di trattativa ripete TailBuyer e il settore negoziazione già esplorato. Le borse carichi possono vietare l'automazione nei termini d'uso, e gli imprevisti in tempo reale sono incompatibili con 5–10 h/settimana. |
| VANGENIUS: il camper progettato sul tuo furgone, in AR e tagliato a CNC | È vicino al settore viaggi già esplorato (vanlife). Ci sono omologazioni da verificare paese per paese, logistica e responsabilità di kit fisici ingombranti, e concorrenza di piani economici su Etsy. |
| OCCHIO: occhiali AI che guidano e controllano il prelievo | Accorpata a GEMELLO come modulo futuro sugli stessi clienti. L'accesso commerciale alla fotocamera degli occhiali, la batteria e il diritto del lavoro (art. 4, Betriebsrat) rendono fragile un primo test autonomo. |
| BINARIO VIVO: ogni tram diventa un treno diagnostico | Acquisti pubblici con cicli di 6–18 mesi e approvazioni di sicurezza per i dispositivi in cabina. Pochi clienti grandi: incompatibile con un fondatore solo a 5–10 h/settimana. |
| SECCA: sapere sei settimane prima quanto il Reno potrà portare | Stesso modello di Mediterra Signal (previsioni vendute a grandi aziende, vicino al forecasting di commodity già esplorato). Oltre 2–3 settimane la prevedibilità è limitata, e la validazione richiede una stagione di acque basse. |
| FORMA: nuovi formati di pasta progettati dalla fisica | Ottima trovata di comunicazione ma business debole: licenze a gradini verso pochi pastifici conservatori, nessun ricavo ripetibile verso 300 k€, e la prototipazione fisica consuma ore. |
| CROCCANTE: il telefono diventa un texturometro da laboratorio | L'accuratezza rispetto agli strumenti certificati è incerta e il mercato è frammentato con budget bassi. Si sovrappone ai clienti R&D di FORMULA INVERSA, di cui potrebbe diventare un modulo. |
| RICETTA VIVA: lo chef cucina una volta, la ricetta si scrive da sola | Telecamere sui lavoratori in cucina (art. 4), bassa adozione tecnologica e alto abbandono nella ristorazione. Il carico di supporto è alto e il settore è vicino al business locale. |
| ZERO: il vino dealcolato che sa ancora di vino | Le regole sulle aggiunte ammesse sono incerte e in evoluzione (rischio compliance). Il lavoro di laboratorio per ogni cantina rischia di diventare consulenza e il mercato NoLo italiano è ancora piccolo. |
| LEGGERO: imballaggi alimentari con il 20% di plastica in meno | È vicino ai test di packaging già esplorati, spinto dalla conformità al regolamento imballaggi PPWR. Ha concorrenti forti e finanziati (Altair, Ansys, PhysicsX, Monolith) e i clienti chiederanno supporto ingegneristico. |
| DIAL-IN: l'espresso giusto in tre tazze | È il WOW più debole, come dichiara la scheda stessa. Breville/Sage e Meticulous integrano già la guida, la nicchia paga poco e il caffè è già coperto da MISCELA. |
| PONTE: videochiamata tradotta dialetto-lingua della diaspora con la tua voce | I modelli vocali generalisti migliorano in fretta sui dialetti, quindi il fossato può sparire. Il pubblico è vicino alla cura degli anziani già esplusa, la disponibilità a pagare non è provata e i dati costano per ogni dialetto. |
| TOCCA: quadri e foto da toccare che ti dicono cosa c'è sotto il dito | Ricavi soprattutto da progetti museali una tantum, con acquisti pubblici lenti e la finestra PNRR che si chiude nel 2026. C'è il rischio di progettazione su misura e il B2C non è provato. Molto affine ai valori di Lorenzo: resta come riserva. |
| ORECCHIO: il direttore sente chi cala, sezione per sezione | La separazione delle quattro sezioni nelle chiese riverberanti non è dimostrata. I cori hanno budget minimi e decidono in assemblea, e il prodotto è vicino all'istruzione musicale. |
| LINEA FANTASMA: il rider più veloce che scende davanti a te nella tua GoPro | Si sovrappone a MORFO (sport più ricostruzione 3D da telefono) con un WOW minore. Rischio Strava/GoPro, responsabilità perché spinge a scendere più veloci, GPS debole sotto bosco. |
| PROVA-CARROZZINA: vedi la tua carrozzina entrare in quella camera prima di prenotare | Problema dell'uovo e della gallina dal lato offerta (gli hotel devono scansionare). È vicino a ospitalità e viaggi già esplorati e alla conformità sull'accessibilità, e Wheel the World è già finanziata. |
| PERIZIA: il crash test attuariale degli agenti AI | Il mercato della valutazione degli LLM è affollato (Giskard, Patronus, Galileo, Braintrust, Vals, Collinear) e AIUC unisce già certificazione e assicurazione. La differenziazione è sottile e le vendite enterprise sono lente. |
| DIECIMILA: 10.000 anni di meteo sintetico per coperture parametriche | Molti concorrenti esperti (Descartes, Arbol, CelsiusPro, Reask, Speedwell). Le vendite assicurative sono lente e servono track record e code validate. È vicino al modello Mediterra e ai dati meteo già proposti. |
| ONDE: il Wi-Fi visto come nebbia colorata in AR prima di montare gli access point | Usa lo stesso motore di RIVERBERO (scansione della stanza più simulazione d'onda): si tiene RIVERBERO per il WOW maggiore e il canale retail. La pianificazione Wi-Fi è presidiata (Ekahau, Hamina), la nicchia professionale è piccola e iOS limita l'accesso all'RSSI. |
| BOTTEGA: il tecnico che va in pensione lascia un gemello che risponde ai giovani | Servono accordi sindacali (art. 4, Betriebsrat), le sessioni di cattura rischiano di diventare un servizio, ed è vicino alla formazione e al manifatturiero già esplorati. |
| PROBABILE: ogni notizia sul futuro con la sua probabilità calibrata | Gli editori pagano poco e lentamente, gli errori su temi sensibili creano rischio reputazionale, e i bot di previsione si stanno banalizzando (FutureSearch, bot di Metaculus, possibili modalità dei grandi LLM). Il WOW è moderato. |
