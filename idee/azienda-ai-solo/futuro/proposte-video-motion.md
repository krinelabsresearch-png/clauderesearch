# Proposte 234–254: business basati su video in motion design fatti con Claude Code (30/10/2026)

**In breve.**
- Ho valutato 21 idee con la scheda v2: le 5 migliori sono descritte sotto, le altre 16 sono elencate in fondo, ciascuna con il motivo per cui resta indietro.
- Solo due superano 3,5. **234 SERATA** (3,95) è contenuti animati ogni settimana per discoteche e promoter, ed è l'unica che resta sopra la soglia anche con motivazione neutra (3,55). **235 PREVENTIVO** (3,60) è un video personalizzato per ogni preventivo di un installatore.
- È una verifica rapida, con circa 25 ricerche web in tutto, non il dossier con le 12 domande. Sopra 3,5 vuol dire "merita la ricerca completa".
- Le motivazioni sono mie stime e vanno confermate da te. I voti sono in [video_motion.py](video_motion.py).

## La premessa: fare bei video con Claude non è più un vantaggio

Nel 2026 il motion design scritto come codice è diventato alla portata di tutti:
- **Remotion** ha rilasciato a inizio gennaio 2026 le sue "Agent Skills", con cui Claude Code scrive e renderizza video in React [1][2].
  - La licenza è gratuita per persone singole e aziende fino a 3 persone.
  - Oltre servono la Company License, da 25 $ per sviluppatore al mese, o la formula "Automators", da 0,01 $ a render con un minimo di 100 $ al mese [3].
- **HyperFrames** di HeyGen è open source con licenza Apache 2.0, quindi senza costi per render né soglie per l'uso commerciale [4][5].
  - Trasforma HTML, CSS e animazioni in MP4.
  - Ha 21 skill pronte per gli agenti.
- **Claude Motion** di Anthropic è in beta dall'8 ottobre 2026 sui piani Team ed Enterprise [6][7].
  - In chat crea spiegazioni animate, grafici animati e presentazioni di prodotto, ed esporta in MP4.
  - Non usa modelli che generano video: anima testi, grafici, forme e immagini con il codice.
- Il generico "scrivi un prompt e ottieni un video animato" è già occupato da molti prodotti:
  - Hera, "il tuo motion designer AI", startup YC S25 [8];
  - per i video di lancio a partire dal sito: UX Pilot, Clickcast e URLmotion [9];
  - per gli annunci dal catalogo: almeno cinque app Shopify lanciate tra aprile e maggio 2026 [10].

Per questo la domanda solita, "cosa fa in più di ChatGPT da 20 $", qui diventa **"cosa fa in più di Claude Motion, o di Claude Code con le skill di Remotion che sono gratis"**. Ho trovato quattro risposte che reggono:
1. **Il video si fa da solo, senza che qualcuno lo chieda.** Parte da un dato che arriva: una serata, un preventivo, una release, un articolo pubblicato.
2. **Migliaia di video tutti diversi**, uno per cliente, per lingua o per prodotto. In chat se ne fa uno alla volta.
3. **Numeri esatti presi dai dati del cliente**, non inventati. Qui il video fatto con il codice batte i generatori di video, che sbagliano testi e cifre.
4. **Clienti che non apriranno mai Claude**: discoteche, installatori, ricercatori. Per loro il prodotto è il flusso di lavoro, non lo strumento.

Le idee che non hanno almeno una di queste risposte sono finite in fondo alla classifica.

## Classifica

| # | Idea | Chi paga | Punteggio | Motivazione neutra |
|---|---|---|---|---|
| **234** | **SERATA:** contenuti animati ogni settimana per discoteche e promoter | Discoteche, promoter, festival | **3,95** | **3,55** |
| **235** | **PREVENTIVO:** un video personalizzato per ogni preventivo | Installatori di fotovoltaico e pompe di calore | **3,60** | 3,40 |
| **236** | **ABSTRACT:** il video abstract degli articoli scientifici | Ricercatori, università, editori | 3,50 | 3,30 |
| **237** | **RILASCIO:** un video per ogni release, da GitHub | Aziende di software e di strumenti per sviluppatori | 3,50 | 3,30 |
| **238** | **GUIDA VIVA:** video tutorial che si rifanno da soli quando cambia l'interfaccia | Aziende di software B2B | 3,40 | 3,40 |
| 239 | TEOREMA: animazioni di matematica corrette | Editori scolastici, piattaforme didattiche | 3,35 | 2,95 |
| 240 | SPOT: dal catalogo e-commerce agli annunci animati | Negozi online | 3,35 | 3,15 |
| 241 | WRAPPED: il video personale di fine anno | App e negozi online | 3,30 | 3,10 |
| 242 | ITINERARIO: il viaggio proposto, in video con la mappa | Agenzie di viaggio, tour operator | 3,30 | 3,30 |
| 243 | LEDWALL: visual a tempo di musica col marchio della serata | Club, festival, DJ | 3,30 | 2,90 |
| 244 | IMMOBILI: un video per ogni annuncio | Agenzie immobiliari | 3,25 | 3,25 |
| 245 | LOCALIZZA: anteprime per App Store in 40 lingue | Sviluppatori di app | 3,20 | 3,20 |
| 246 | INVITI: video inviti personalizzati su Etsy | Privati (matrimoni, feste) | 3,20 | 3,20 |
| 247 | MERCATI: video settimanale dei mercati | Consulenti finanziari | 3,15 | 3,15 |
| 248 | MARCHIO: il motion design del marchio per i team marketing | Aziende medie | 3,15 | 3,15 |
| 249 | PADEL: grafiche animate per tornei e circoli | Circoli, circuiti, federazioni | 3,10 | 2,70 |
| 250 | LANCIO: dall'indirizzo del sito al video di lancio | Startup | 3,10 | 3,10 |
| 251 | CANALE: canale YouTube di dati animati | Pubblicità e sponsor | 3,00 | 2,80 |
| 252 | KIT: template e skill a pagamento | Creator e sviluppatori | 2,90 | 2,90 |
| 253 | BOLLETTA: video personalizzati per utility e assicurazioni | Grandi aziende | 2,80 | 3,00 |
| 254 | STUDIO: studio di motion design con l'AI | Aziende (servizio, escluso) | 2,75 | 2,75 |

---

## 234. SERATA: tutti i contenuti animati della serata, ogni settimana, senza grafico

- **Cosa fa.** Il locale, o il promoter, carica una volta il suo kit di marca: logo, caratteri, colori e stile. Poi ogni settimana compila la scheda della serata (nome, data, artisti, foto, orari, prezzi, link ai biglietti). SERATA genera da sola il pacchetto completo, già nei formati giusti e in italiano, inglese e spagnolo:
  - annuncio e svelamento della lineup;
  - conto alla rovescia a 3, 2 e 1 giorno;
  - storia "stasera" con il QR dei biglietti;
  - reel verticale e post;
  - versione per il ledwall;
  - il lunedì, il riepilogo della serata.

  Collegata alla biglietteria, quando restano pochi posti produce da sola il video "ultimi 50 biglietti". Può anche programmare la pubblicazione su Instagram.
- **Momento WOW.** Il gestore scrive "sabato: Marco Rossi, apertura 23:30, ingresso 20 €". Dieci minuti dopo ha 12 contenuti animati nello stile del locale, che prima costavano una settimana di messaggi con il grafico.
- **Perché tu.** È il mondo in cui lavori: conosci il ritmo settimanale dei locali, chi decide e quanto si spende oggi. Hai già i primi clienti di prova, e alla parte tecnica aggiungi l'esperienza di marketing. È l'unica idea del round in cui il tuo vantaggio è reale e non replicabile da chiunque abbia Claude.
- **Chi paga e quanto.**
  - Discoteche e club: 79–149 €/mese. Promoter e collettivi: 29–49 €/mese. Festival: pacchetti stagionali da 500–2.000 € (stime da verificare).
  - L'alternativa oggi è il grafico freelance pagato a flyer, oppure Canva fatto in casa.
  - 300–480 k€ l'anno corrispondono a 250–400 locali a circa 100 €/mese. In Italia i locali da ballo sono qualche migliaio (stima, n.v.), quindi servono anche Spagna, Francia e Germania.
  - La strada verso 1 M€ è un accordo con una biglietteria per serate ed eventi, che offra SERATA come funzione integrata con ricavi condivisi (Xceed, Dice, Shotgun e simili; da verificare).
- **Più di Claude Motion.**
  - Claude Motion fa un video alla volta in chat ed è riservato ai piani Team ed Enterprise.
  - Il social media manager di un club non scrive prompt ogni settimana. SERATA produce 10–15 formati coerenti a ogni serata, dai dati della serata e della biglietteria, nello stile del locale, e li pubblica.
  - È un flusso di lavoro, non un video.
- **Concorrenti.** Non ho trovato nessun prodotto verticale per la vita notturna; è una verifica rapida.
  - Ci sono strumenti generici: Invideo propone video per la lineup dei DJ e HeyGen ha un modello per la lineup dei festival [11].
  - Canva ha modelli animati.
  - Il concorrente vero è il grafico amico del locale.
- **Come si costruisce.**
  - Motore: HyperFrames (Apache 2.0, nessun vincolo) oppure Remotion, gratuito finché siete al massimo in 3.
  - 30–50 modelli con parametri, scritti con Claude Code e rifiniti a mano: il gusto dei modelli è il prodotto.
  - Render su server, web app con la scheda della serata, pubblicazione tramite le API di Meta e un LLM per i testi.
  - MVP in 6–8 settimane. A regime 4–6 ore a settimana, soprattutto nuovi modelli a ogni stagione.
- **Primo test (0–1.000 €, 6 settimane).**
  - Per 4 settimane prepari a mano, con Claude Code, il pacchetto per 3–5 locali con cui lavori già, e misuri quanti formati usano davvero e la portata rispetto alle settimane prima. È un test, non un servizio da tenere.
  - In parallelo una landing page con 500–1.000 € di pubblicità rivolta a promoter e locali fuori dalla tua rete.
  - **GO** se almeno 3 locali su 5 pagano almeno 79 €/mese dal secondo mese e almeno 15 locali o promoter estranei si iscrivono alla lista d'attesa.
  - **STOP** se usano meno di 3 formati a settimana o se non sono disposti a pagare più di quanto pagano il grafico.
- **Rischi.**
  - Clienti attenti al prezzo e stagionali: i club invernali chiudono d'estate e viceversa, quindi gli abbonamenti si disdicono.
  - Canva o le biglietterie potrebbero aggiungere la stessa funzione.
  - Dipendenza dalle API di Meta per pubblicare.
  - Modelli con l'aspetto "fatto con l'AI" se manca il gusto.
  - Fiscale: i ricavi del software si sommano al limite di 85 k€ del forfettario, dove hai già circa 60 k€. Conviene quindi farli passare dalla SRLS di cui abbiamo parlato.
- **Si collega con:** 243 LEDWALL, come modulo a pagamento in più.

## 235. PREVENTIVO: il cliente riceve il video della sua casa con l'impianto, non un PDF

- **Cosa fa.** Si collega al software con cui l'installatore prepara i preventivi (OpenSolar, Aurora, Solargraf, Reonic) oppure legge il PDF. Per ogni preventivo genera un video di 60–90 secondi con:
  - la casa del cliente vista dal satellite e i pannelli che compaiono sul tetto;
  - il sole che attraversa la giornata;
  - la bolletta prima e dopo, gli incentivi e il rientro dell'investimento anno per anno;
  - il nome del cliente e quello del tecnico.

  Il link è tracciato: l'installatore sa quando il cliente lo guarda e lo richiama in quel momento.
- **Momento WOW.** La sera il cliente gira il video al coniuge: "guarda, questa è casa nostra". Un PDF di 14 pagine non lo inoltra nessuno.
- **Chi paga e quanto.**
  - Installatori di fotovoltaico e pompe di calore: 99–249 €/mese, oppure 3–5 € a video.
  - Poi altri acquisti costosi per la casa: infissi, cucine, piscine, domotica.
  - 300 k€ corrispondono a circa 250 installatori a 100–120 €/mese. Per 1 M€ serve un accordo con un software di preventivi, che lo offra con il proprio marchio, oppure più settori.
- **Più di Claude.** Un video per ogni preventivo, in automatico, con i numeri esatti del preventivo. Decine al giorno senza che il venditore scriva una riga, più il tracciamento delle visualizzazioni.
- **Concorrenti.** Non ho trovato video animati generati dal singolo preventivo.
  - Le piattaforme di proposta (Solargraf, Aurora, OpenSolar, Surge PV) mostrano grafici di risparmio e permettono di inserire un video registrato.
  - VidProposals e Smarterlaunch usano video registrati con Loom.
  - HeyGen ha solo modelli promozionali generici per installatori [12].
- **Perché tu.**
  - Matematica dei risparmi e dell'irraggiamento: hai già studiato il settore con 208 OMBRA, e l'ombra animata può diventare una scena del video.
  - Marketing.
  - Non hai però una rete di installatori.
- **Primo test (1–2 k€, 6–8 settimane).**
  - 5 installatori; per metà dei loro preventivi c'è anche il video.
  - **GO** se, su almeno 100 preventivi, quelli con il video vengono firmati almeno il 20% più spesso (in termini relativi), oppure se 3 installatori su 5 pagano. Il campione è piccolo, quindi il dato è solo indicativo.
  - **STOP** se il cliente apre il video meno di una volta su due.
- **Rischi.**
  - In alcuni Paesi il mercato del fotovoltaico residenziale è in rallentamento (da verificare).
  - Le piattaforme di preventivi possono aggiungere la stessa funzione in poco tempo.
  - Responsabilità sui numeri: usare solo quelli del preventivo e aggiungere una nota legale.
  - Dati personali dei clienti (GDPR), gestibili.

## 236. ABSTRACT: il video abstract di un articolo scientifico in un'ora, fedele al testo

- **Cosa fa.** Si carica il PDF dell'articolo. ABSTRACT:
  - estrae figure, tabelle e risultati;
  - scrive un copione di 60–120 secondi in cui ogni frase rimanda alla pagina dell'articolo da cui viene;
  - anima i grafici con i dati veri;
  - aggiunge voce sintetica e sottotitoli in più lingue;
  - esporta nei formati chiesti dalle riviste (di solito 1–3 minuti [13]) e in quelli per LinkedIn e X.
- **Chi paga e quanto.**
  - Ricercatori e laboratori: 99–199 € a video. Uffici comunicazione delle università: pacchetti. Editori: con il loro marchio, a video.
  - Oggi i video sono fatti da persone e costano molto [14]:
    - Research Square: 1.500 $ il video abstract e 300 $ il "Video Byte" da un minuto (FAQ di Wiley, forse datata);
    - Springer Nature: 499 $;
    - ACS: 350 $.
  - 300 k€ corrispondono a 2.000–3.000 video l'anno, oppure a 1–2 editori.
- **Più di Claude.** Fedeltà verificata all'articolo, grafici ricostruiti dai dati, formati delle riviste. Claude Motion richiede un piano Team e lavoro a mano.
- **Concorrenti.**
  - I servizi degli editori, fatti da persone.
  - Invideo e AITuber, generici.
  - Due sistemi di ricerca: Preacher (ICCV 2025, codice annunciato) e Manimator [15].
- **Perché tu.** Il tuo profilo scientifico, ed è vicina alle idee già in lista 107 e 116.
- **Primo test.** 30 video gratuiti per autori di articoli open access appena usciti, in 2–3 discipline, con l'offerta successiva a 99 €. **GO** se compra almeno il 10% degli autori contattati, oppure se un editore accetta un pilota.
- **Rischi.**
  - I ricercatori pagano poco, e spesso con i fondi del progetto.
  - Gli editori possono farlo da soli.
  - Ci sono le regole delle riviste sull'uso dell'AI e i diritti sulle figure (liberi negli articoli CC-BY).

## 237. RILASCIO: a ogni release il video è già pronto da pubblicare

- **Cosa fa.**
  - È un'app per GitHub, che si può collegare anche agli strumenti per il registro delle modifiche (changelog).
  - A ogni release legge le note e le modifiche al codice, cattura le schermate cambiate su un ambiente di prova e genera un video di 20–40 secondi nello stile dell'azienda, per X, LinkedIn, changelog ed email.
  - Ogni mese prepara anche il riepilogo "cosa è cambiato".
  - Si approva con un clic su Slack.
- **Chi paga e quanto.** Aziende di software e di strumenti per sviluppatori, da 5 a 200 persone: 49–199 $/mese. 300 k€ corrispondono a 250–500 clienti nel mondo, in inglese.
- **Più di Claude.** Uno sviluppatore con Claude Code e Remotion fa il video una volta. RILASCIO lo fa a ogni release, da solo, sempre coerente e con le schermate vere.
- **Concorrenti.** Non ho trovato strumenti che facciano video dalle note di release di GitHub [16]. Sono vicini i generatori di video di lancio dal sito (UX Pilot, Clickcast, URLmotion) e Hera.
- **Il problema.** I clienti sono proprio le persone più capaci di farselo da sole. Il dolore è basso: nessuno perde clienti per non avere il video della release. Per questo la difendibilità ha voto 1.
- **Primo test.**
  - Fai il video della release di 50 startup e lo mandi in privato: "è vostro se vi piace".
  - **GO** se almeno 10 chiedono la versione automatica e almeno 5 pagano 49 $.

## 238. GUIDA VIVA: tutorial video che si rifanno da soli a ogni rilascio, in 20 lingue

- **Cosa fa.**
  - I tutorial del centro assistenza nascono da copioni ed esecuzioni automatiche del prodotto (Playwright).
  - Hanno zoom, frecce ed evidenziazioni animate e una voce.
  - Quando l'interfaccia cambia, i video vengono rigenerati in tutte le lingue.
- **Chi paga e quanto.** Aziende di software B2B, cioè i team di assistenza clienti e di documentazione: 99–499 $/mese.
- **Più di Claude.** La rigenerazione automatica a ogni rilascio e la gestione delle lingue.
- **Concorrenti.** Il settore è affollato, per questo la difendibilità ha voto 1:
  - Videate dichiara già l'aggiornamento automatico quando cambia l'interfaccia [17];
  - poi ci sono Trainn, Guidde, Trupeer, Clueso, Supademo, Arcade e Scribe.
- **Perché resta in classifica.** Il dolore è reale: i video vecchi generano richieste di assistenza. Il mercato è grande, e la tua parte tecnica conta.

---

## Le altre 16, in breve

- **239 TEOREMA (3,35)**: animazioni di matematica corrette, verificate con il calcolo simbolico, per editori e piattaforme didattiche.
  - La motivazione è alta, ma docenti ed editori pagano poco e lentamente.
  - Ci sono già molti progetti con Manim e un LLM [18].
  - **Meglio come funzione della 096**, il tutor di Analisi 1 già in lista: "il tuo errore spiegato con un'animazione".
- **240 SPOT (3,35)**: dal catalogo agli annunci animati.
  - Il mercato è enorme ma saturo: MerchMotion, AdCrex, Movioo, Catalog Motion e Adstellar sono nati tutti nel 2026 [10], oltre agli strumenti di Meta.
  - È utile come strumento interno per il tuo dropshipping, per esempio per la 228 GPX.
- **241 WRAPPED (3,30)**: il video personale di fine anno per gli utenti di app e negozi.
  - È forte come effetto, ma si vende a dicembre e con trattative B2B.
  - Algo, di Torino, fa già video da dati per Bloomberg; c'è anche Jev Wrapped [19][20].
- **242 ITINERARIO (3,30)**: il viaggio proposto dall'agenzia, in video con il percorso sulla mappa.
  - Non ho trovato prodotti per tour operator [21].
  - Le agenzie però pagano poco: è una variante della 235 da tenere in riserva.
- **243 LEDWALL (3,30)**: visual a tempo di musica con il nome della serata e gli sponsor. Il mercato da solo è piccolo: è un modulo della 234.
- **244 IMMOBILI (3,25)**: un video per ogni annuncio, preso dal gestionale. È un bisogno ricorrente, ma il settore è affollato e tu non hai un vantaggio.
- **245 LOCALIZZA (3,20)**: anteprime per App Store in 40 lingue.
  - Apple permette fino a 3 video per lingua [22], ma esistono già molti strumenti.
  - Esiste perfino una skill gratuita per Claude che fa anteprime per l'App Store.
- **246 INVITI (3,20)**: video inviti personalizzati su Etsy. Si valida in fretta, ma è pieno di venditori con modelli Canva: non arriva a 300 k€.
- **247 MERCATI (3,15)**: video settimanale dei mercati con il marchio del consulente.
  - Ci sono già InvestSuite StoryTeller (belga), Croesus Vidia, Storyline e SundaySky [23][24].
  - Le regole MiFID sulle comunicazioni di marketing la avvicinano alla burocrazia.
- **248 MARCHIO (3,15)**: il motion design del marchio come codice, per i team marketing. È lo stesso spazio di Claude Motion, Canva e Hera.
- **249 PADEL (3,10)**: grafiche animate automatiche per tornei e circoli.
  - Non ho trovato strumenti per il padel: esistono solo per il calcio (Terrace, Sportgraphics) [25].
  - Il mercato però è piccolo e i circoli pagano poco.
- **250 LANCIO (3,10)**: dal sito al video di lancio. È già fatto da UX Pilot, Clickcast, URLmotion e HeyGen [9].
- **251 CANALE (3,00)**: canale YouTube di dati animati senza volto. Approfondita il 31/10/2026 come [256](dossier/256-youtube-video-claude.md): scartata con 3,05.
  - Dipende da pochi video di successo.
  - Dal 2025 YouTube toglie la monetizzazione ai contenuti "prodotti in serie" [26].
- **252 KIT (2,90)**: template e skill a pagamento. Remotion e HyperFrames ne regalano già decine.
- **253 BOLLETTA (2,80)**: video personalizzati della bolletta per utility e telco. Si vende a grandi aziende, con gare e tempi lunghi, e lo fanno già SundaySky e Idomoo [27].
- **254 STUDIO (2,75)**: studio di motion design a pacchetto. Il mercato paga 1.500–8.000 $ al minuto [28], ma è un servizio, quindi è escluso.

## Cosa farei

1. **Confermami la motivazione per 234 SERATA.** Ho stimato 5 perché è il tuo lavoro attuale. Se è 4, il punteggio scende a 3,75 e la 234 resta comunque prima.
2. **Ricerca completa sulla 234 con le 12 domande**, in particolare su:
   - quante discoteche e quanti promoter ci sono in Italia, Spagna e Germania;
   - quanto spendono oggi in grafica;
   - quali biglietterie hanno API e programmi per partner.
3. **Il test della 234 può partire subito** con i locali con cui lavori, a costo quasi zero. In parallelo la 235 può avere la sua ricerca completa: è la seconda e non dipende dalla tua rete.

## Fonti

1. https://www.tella.com/blog/how-to-use-remotion-agent-skills-with-claude-code
2. https://aividpipeline.com/fr/blog/remotion-agent-skills-guide-2026
3. https://www.remotion.dev/docs/license/pricing ; https://remotion.dev/pricing
4. https://github.com/heygen-com/hyperframes
5. https://themenonlab.blog/blog/heygen-hyperframes-video-as-code
6. https://support.claude.com/en/articles/17454997
7. https://www.layer3labs.io/guides/claude-motion ; https://mezha.ua/en/news/claude-dashboards-315990/amp/
8. https://www.ycombinator.com/launches/Nwh-hera-your-ai-motion-designer
9. https://uxpilot.ai/product-launch-video-maker ; https://bigideasdb.com/launchdb/launches/clickcast ; https://peerpush.com/p/urlmotion ; https://www.heygen.com/en-gb/tool/url-to-video
10. https://apps.shopify.com/merchmotion?locale=it ; https://apps.shopify.com/movioo ; https://pickyourapp.com/collections/store-design-images-and-media/products/catalog-motion-ai
11. https://info.invideo.io/blog/ai-tool-video-nightclub-dj-lineup ; https://www.heygen.com/video/festival-lineup-video-maker
12. https://www.solargraf.com/solar-proposal ; https://www.opensolar.com/?p=516 ; https://surgepv.com/solar-proposals ; https://www.salesforge.ai/directory/sales-tools/vidproposals ; https://www.heygen.com/video/ai-solar-installer-promo-video-maker
13. https://blog-sc.hku.hk/creating-video-abstracts-with-ai-tools/
14. https://authorservices.wiley.com/asset/photos/promote.html/VA%20FAQ%20Postcard.pdf ; https://solutions.springernature.com/products/video-byte ; https://authoringservices.acs.org/promotional-services
15. https://openaccess.thecvf.com/content/ICCV2025/html/Liu_Preacher_Paper-to-Video_Agentic_System_ICCV_2025_paper.html ; https://icml.cc/virtual/2025/50491
16. https://awesome.ecosyste.ms/projects/github.com%2Fhideoo%2Fchangelogithub-action
17. https://www.capterra.ie/software/1037930/videate ; https://trainn.co/blog/keep-training-videos-updated-when-product-ui-changes/
18. https://peerlist.io/itshp/project/manimai ; https://arxiv.org/abs/2604.05266
19. https://algo.tv/ideas/year-in-review-campaign ; https://forcreativegirls.com/algo-tv-data-visualization-studio-ilenia-notarangelo
20. https://aiindigo.com/tool/jev-wrapped
21. https://info.invideo.io/blog/best-software-animate-luxury-travel-itineraries ; https://www.saashub.com/mapanim
22. https://appdrift.co/guides/app-store-connect/app-preview-videos ; https://tessl.io/registry/skills/github/Eronred/aso-skills/app-preview-video
23. https://finance.yahoo.com/sectors/technology/articles/investsuite-launches-storyteller-u-market-100424378.html ; https://www.investmentexecutive.com/brand-knowledge_/croesus-vidia-brings-investment-information-to-life
24. https://www.thewealthmosaic.com/vendors/storyline/storyline-wealth-management ; https://sundaysky.com/solutions/wealth-management/
25. https://trustmrr.com/startup/myterrace-net ; https://www.producthunt.com/products/sportgraphics
26. https://air.io/en/monetization/youtube-monetization-policy-changes-2026-a-complete-dated-timeline
27. https://sundaysky.com/blog/sundaysky-vs-idomoo/ ; https://ecosystem.hubspot.com/marketplace/listing/idomoo
28. https://pixune.com/blog/animated-explainer-video-cost/ ; https://creamyanimation.com/explainer-video-cost/
