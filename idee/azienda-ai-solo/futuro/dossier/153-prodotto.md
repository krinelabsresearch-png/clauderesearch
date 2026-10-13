# Dossier 153 (gioco di società AI), parte 2: prodotto, rischi, acquisizione, test e modelli del 2027

> Rapporto di ricerca del 13/10/2026 (agente di ricerca, verificato a campione da Claude). Le voci [NV] non sono verificate con una fonte; "stima" indica un calcolo.

# Rapporto per Lorenzo: idea 153 · Gioco di società AI per serate tra amici

**Data:** 13/10/2026.
**Ricerche web:** 32 su 32, budget esaurito. Non ho usato WebFetch: i dati vengono dagli estratti delle ricerche. I prezzi di Anthropic vengono dal listino dello strumento claude-api, aggiornato al 6/10/2026. Due fonti vengono da ricerche precedenti del repository [33].
**Nessun file scritto nel repository.** I calcoli sono in uno script temporaneo, fuori dal repository.
**Legenda:**
- [n] = fonte numerata nell'elenco in fondo.
- "stima" = un mio calcolo.
- "n.v." = dato non verificato, comprese le mie conoscenze pregresse.
- Cambio 1 € = 1,15 $; IVA al 22% (stima).

---

## Sintesi

- **ChatGPT non ha più le chat di gruppo.**
  - OpenAI le ha ritirate dal 9/7/2026: non si creano nuovi gruppi e quelli esistenti diventano di sola lettura [1].
  - Oggi né ChatGPT né Gemini offrono una vera partita a più persone [1][5].
  - Due concorrenti gratuiti però ci sono già:
    - Meta AI si usa nei gruppi WhatsApp in tutta l'UE [6];
    - Netflix offre giochi di società sulla TV, con il telefono come controller, senza costi in più [7].
- **Rispetto a ChatGPT il prodotto fa chiaramente di più.** Ha segreti e voti anonimi su ogni telefono, regole, tempi e punteggi, la lingua di ciascun giocatore e contenuti presi da ciò che i presenti scrivono in privato.
- **Questo però non basta per un abbonamento.** Il vero concorrente è il gratis (Meta AI, Netflix, il gioco "a dita puntate") e la conversazione stessa.
- **Costo per serata** (12 giocatori, 4 lingue, circa 75 minuti; stima):

  | Versione | Costo |
  |---|---|
  | Essenziale | 0,22 € |
  | Standard | 0,85 € |
  | Premium | 2,63 € |

  Con un pass serata da 1,99 € il margine lordo è dell'84% con la versione essenziale e del 39% con la standard (stima).
- **Acquisizione:**
  - con la pubblicità LTV/CAC è tra 0,04 e 0,29 (stima);
  - si cresce solo con il ciclo virale (ingresso con QR) e con canali gratuiti;
  - serve un fattore K di almeno 0,4–0,5.
- **Gli Erasmus sono un laboratorio, non un mercato.**
  - In UE ci sono circa 40–60 mila "ospiti" possibili l'anno, che rendono al massimo 30–40 k€ (stima).
  - Per 300–500 k€ servono 9–15 mila abbonati medi a 3,99 €/mese (stima).
- **Rischi principali:**
  - presentarlo come gioco alcolico: per Apple è una categoria satura [9], e TikTok non spinge i video con alcol in eccesso [13];
  - umiliazioni e contenuti piccanti;
  - dati personali degli amici;
  - obblighi dell'AI Act in vigore dal 2/8/2026 [16].
- **Test:** 3–4 settimane, 12–20 serate, meno di 1.000 € (stima). Due metriche decidono:
  - gruppi che rigiocano entro 14 giorni: almeno il 40%;
  - giocatori che lanciano una partita da soli entro 21 giorni: almeno il 5%.
- **Voti v2:**
  - somma 25 su 40;
  - con motivazione neutra (3) il punteggio pesato è **3,15**;
  - serve una motivazione 5 per arrivare a 3,55, la soglia della lista.

---

## 4. Cosa fa in più di ChatGPT da 20 $/mese

### Cosa sanno fare oggi gli assistenti e le piattaforme (ottobre 2026)

| Strumento | Cosa fa oggi | Limite in un pre-serata |
|---|---|---|
| **Chat di gruppo di ChatGPT** | Lanciate a novembre 2025: fino a 20 persone via link, con ricerca, caricamento di immagini e file, generazione di immagini e dettatura [2]. **Ritirate dal 9/7/2026:** niente nuovi gruppi, niente ingressi nemmeno con un vecchio link, poi sola lettura. OpenAI dice di "esplorare altre funzioni collaborative" [1] | Oggi non esistono più |
| **ChatGPT Voice** (GPT-Live-1, dall'8/7/2026) | Ascolta e parla insieme, interrompe meno, traduce in tempo reale, passa le richieste difficili a GPT-5.5 [3]. La traduzione non ha un'interfaccia dedicata e non ha un'API al lancio (fonte di un concorrente) [4] | Un solo telefono e un solo utente. Nessuna prova che distingua più voci [3]. Con 12 persone e la musica non sa chi ha risposto |
| **Gemini Live** | Conversazione a voce uno a uno [5]. Da luglio 2026 una chat si può condividere via Drive, solo in lettura [5] | Nessuna modalità di gruppo trovata |
| **Meta AI in WhatsApp** | Si chiama con @MetaAI dentro i gruppi. In UE da marzo 2025, in 6 lingue tra cui l'italiano; non si può disattivare [6] | Genera domande nel gruppo, ma senza regole, tempi, punteggi o segreti |
| **Netflix sulla TV** | Da ottobre 2025, giochi di società con il telefono come controller (QR), senza costi in più: Boggle, Lego Party!, Pictionary, Tetris, Party Crashers [7] | Contenuti fissi, non personalizzati, senza AI |

**Cosa può fare oggi un ospite con ChatGPT a 20 $.**
- Mette il telefono in vivavoce: "facci da presentatore di un quiz su di noi".
- Con 3–5 persone funziona (stima).
- Con 12–20 persone è lento: chi ha risposto, e chi tiene i punti?

### Cosa resta al prodotto

| Elemento | ChatGPT o Gemini oggi | Giochi esistenti | Giudizio |
|---|---|---|---|
| Partita con regole, tempi e punteggi | No | Sì (Jackbox, Netflix, Kahoot) | Netto contro ChatGPT; contro gli altri giochi è il minimo indispensabile |
| Telefono come controller | No | Sì, da anni | Indispensabile, ma non distintivo |
| Segreti e voti anonimi su ogni telefono | No | Sì, nei giochi a ruoli nascosti | **È il motivo vero per cui serve un'app e non una chat.** Undercover, Impostor e "chi è più probabile che…" con voto onesto non si giocano su un solo telefono |
| Ognuno legge nella sua lingua | Traduce per un solo utente [4] | Raro (n.v.) | Distintivo e nativo dell'AI. Esempio: nella stessa partita di Undercover ognuno vede la parola segreta nella propria lingua. Il valore va misurato, perché gli Erasmus spesso usano l'inglese |
| Contenuti sul gruppo | Sì, se qualcuno scrive tutto a mano | No | **Il cuore della novità.** Ognuno inserisce in privato i propri segreti, che diventano domande |
| Memoria del gruppo tra le serate | Solo la memoria del singolo utente (n.v.) | No | Utile solo se i gruppi tornano. È il punto più delicato per il GDPR |
| Design: schermo condiviso, voce, clip | No | Sì (Jackbox, Netflix) | Necessario e copiabile |

### Giudizio critico
1. **Rispetto a ChatGPT il vantaggio è netto e si vede subito.** Una chat, o una voce su un solo telefono, non gestisce segreti, voti anonimi e risposte contemporanee.
2. **L'ospite non fa il confronto con ChatGPT a 20 $, ma con il gratis.** Netflix è incluso nell'abbonamento [7], Meta AI è già nel gruppo WhatsApp [6], e "chi è più probabile che…" si gioca anche puntando il dito.
3. **L'abbonamento mensile ha senso solo per chi ospita almeno 2 volte al mese.** Per gli Erasmus sono più naturali un pass serata o un pass semestre (stima).
4. **Un segnale da leggere.** OpenAI ha chiuso le chat di gruppo dopo circa 8 mesi [1][2]. La mia interpretazione: "l'AI dentro una chat di gruppo" non ha attecchito. Un gioco risponde a un bisogno diverso, ma la domanda va dimostrata.
5. **Il vantaggio ha una scadenza.** OpenAI "esplora funzioni collaborative" [1], e Meta ha già sia i gruppi sia l'AI [6].

---

## 7. Rischi

### Store
- **Apple, linea guida 1.4.3.** Sono vietate le app che incoraggiano il consumo di "quantità eccessive di alcol", e vengono rifiutate quelle che spingono i minori a bere [9].
- **Apple, linea guida 4.3 (spam).** Apple ha inserito i giochi alcolici tra le categorie sature.
  - **Caso reale:** un'app è stata rifiutata perché "è soprattutto un gioco alcolico" e duplica app già presenti [9].
  - Non ho trovato rifiuti di giochi alcolici per la 1.4.3: quelli trovati riguardano il tabacco [9].
- **Classificazione per età su Apple.**
  - Le classi ora sono 4+, 9+, 13+, 16+ e 18+ [10].
  - Il nuovo questionario era obbligatorio entro il 31/1/2026 e considera anche ciò che generano assistenti e chatbot AI [10].
  - Un livello "piccante" o riferimenti all'alcol portano probabilmente a 16+ o 18+ (stima).
  - Le funzioni nascoste sono vietate (linea guida 2.3.1, n.v.): un livello piccante va dichiarato anche se si sblocca dopo.
- **Google Play.**
  - Non ho trovato una regola ufficiale che nomini i giochi alcolici.
  - Una fonte secondaria del 2019 dice che le regole sui contenuti limitati vietano i minori che bevono e il bere eccessivo o "a gara" mostrato in modo positivo [11].
  - La classificazione IARC è obbligatoria [11].
  - Uno studio del 2015 trovava giochi alcolici senza alcun controllo dell'età [11].
- **Cosa fare:**
  - l'app non genera mai ordini come "bevi X sorsi"; se il gruppo beve, decide da sé;
  - va presentata come gioco di società, non come gioco alcolico;
  - questo la separa anche dalla categoria satura.

### Pubblicità degli alcolici
- **Italia, legge 125/2001, art. 13.**
  - Vieta la pubblicità di alcolici nei programmi per minori e nei 15 minuti prima e dopo.
  - Vieta i messaggi che mostrano minori che bevono o presentano il bere in modo positivo.
  - Vieta la pubblicità nei luoghi frequentati soprattutto da minori [12].
  - Il testo è stato modificato alla fine del 2025: va riletto quello in vigore (n.v.) [12].
- **Influencer:** l'AGCOM ha un codice del 2025 per gli influencer "rilevanti" [12]. Non ho verificato regole specifiche sull'alcol.
- **UE:** la direttiva sui servizi di media audiovisivi vieta la pubblicità di alcolici rivolta ai minori o che incoraggia il consumo smodato (n.v.).
- **TikTok.**
  - I video con "consumo di quantità eccessive di alcol" non entrano nel feed "Per te".
  - I contenuti che promuovono alcolici li vedono solo gli adulti [13].
  - Negli USA TikTok accetta pubblicità di marchi di alcolici dal 2024 [13].
- **Sponsorizzazioni.**
  - Le feste Erasmus sono spesso sponsorizzate da marchi di alcolici (n.v.).
  - Un marchio di birra dentro l'app la trasforma in pubblicità di alcolici rivolta a ragazzi di 18–25 anni.
  - **Consiglio:** nessuno sponsor di alcolici nella prima fase.

### Minori
- Gli Erasmus sono maggiorenni, ma attraverso TikTok il gioco arriverà ai liceali.
- In Italia il consenso al trattamento dei dati online vale dai 14 anni (n.v.).
- **Precedente italiano.** Il Garante ha multato Replika per 5 M€ (decisione del 10/4/2025). Mancavano una base giuridica e la verifica dell'età, e i minori entravano senza tutele [15].
- **UE.**
  - Le linee guida del DSA sui minori (luglio 2025) raccomandano di verificare o stimare l'età nei servizi ad alto rischio.
  - L'app UE di verifica dell'età è pronta dal 15/4/2026, con un progetto pilota anche in Italia.
  - Gli Stati devono offrirla entro il 31/12/2026 [14].
- **Cosa fare:**
  - modalità base adatta dai 16 anni (stima);
  - livelli piccanti e riferimenti all'alcol solo per maggiorenni, con verifica dell'età (l'app UE appena sarà disponibile).

### Contenuti
- **Il rischio vero:** "chi è più probabile che…" con nomi veri può diventare bullismo.
- **Temi delicati:** corpo, sesso, orientamento, etnia, religione, salute. Nei gruppi Erasmus pesano anche gli stereotipi nazionali.
- **Consenso individuale e privato.**
  - Ognuno sceglie sul proprio telefono il livello (da 0 a 3) e i temi da evitare.
  - Vale il livello più basso del gruppo, senza rivelare chi l'ha abbassato.
  - L'ospite non può forzare il consenso degli altri.
- **Divieti:** niente contenuti su persone assenti; nelle clip, niente nomi e volti salvo consenso.
- **Controlli:**
  - filtro su ciò che si scrive (nei contenuti entrano solo i nomi dei presenti);
  - classificatore sui contenuti generati;
  - pulsante "salta" anonimo;
  - segnalazioni e registro per 30 giorni (stima).

### GDPR
- Il gruppo inserisce dati personali: nomi, aneddoti, a volte dati sensibili come orientamento o salute.
- L'esenzione per uso personale copre le persone, non l'azienda: per questi dati l'app è titolare del trattamento (n.v.).
- **Dati scritti da altri:** chi inserisce i dati di un amico non ha il suo consenso. **Regola:** ognuno inserisce solo dati su di sé.
- **La memoria del gruppo crea profili che restano nel tempo**, anche di persone che non usano l'app. Servono (stima):
  - un consenso esplicito;
  - la cancellazione automatica, per esempio dopo 24 ore se il gruppo non chiede la memoria;
  - l'esportazione e la cancellazione su richiesta;
  - contratti con i fornitori dei modelli;
  - nessun addestramento su dati personali.
- Probabilmente serve una valutazione d'impatto (DPIA) (n.v.).

### AI Act, art. 50 (in vigore dal 2/8/2026)
- **50(1):** le persone devono sapere che parlano con un'AI. Il presentatore deve dirlo [16].
- **50(2):**
  - chi fornisce un sistema che genera audio, immagini, video o testo deve marcarli in un formato leggibile dalle macchine;
  - il rinvio al 2/12/2026 vale solo per i sistemi già sul mercato prima di agosto 2026 [16];
  - un'app lanciata adesso non ne beneficia.
- **50(4):** i deepfake vanno dichiarati. Caricature o voci che imitano gli amici rientrano qui (stima). Consiglio: non clonare la voce dei giocatori.
- **Multe:** fino a 15 M€ o al 3% del fatturato mondiale [16].
- Il codice di condotta UE sulla trasparenza è volontario, ma aiuta a dimostrare di essere in regola [16].
- **Nelle clip esportate:** etichetta "generato con AI" e metadati.

### Proprietà intellettuale
- **Le meccaniche di gioco non sono protette dal diritto d'autore.**
  - Nel caso Tetris contro Xio (USA, 2012) regole e meccaniche sono "idee"; è protetta l'espressione audiovisiva [17].
  - In Texas un giudice ha escluso la tutela di meccaniche a ruoli nascosti [17].
  - In UE vale un principio simile (Corte di giustizia, SAS Institute, 2012; n.v.).
- **Da evitare:**
  - nomi e marchi altrui: Quiplash, Fibbage e Drawful (Jackbox), Codenames, Spyfall, e "Undercover" come nome di app (tutti n.v.);
  - grafica, testi, interfacce e banche di domande altrui.
- Prima del lancio, controllare i nomi su EUIPO e TMview (n.v.).

### Piattaforme
- **TikTok:** l'algoritmo cambia spesso, e i video con alcol in eccesso restano fuori dal feed "Per te" [13]. Se la crescita dipende da TikTok, basta un cambio di regole per fermarla.
- **Store:** rischio di rifiuto per le linee guida 4.3 e 1.4.3 [9]. All'inizio una web app evita la revisione.
- **Fornitori dei modelli:** prezzi e regole sui contenuti piccanti possono cambiare (n.v.).
- **Grandi piattaforme:** Meta (gruppi WhatsApp), Netflix (TV) e OpenAI (funzioni collaborative) possono offrire una versione gratuita [1][6][7].

### Riepilogo dei rischi

| Rischio | Probabilità | Impatto | Mitigazione principale |
|---|---|---|---|
| Visto come gioco alcolico | Alta, nel contesto pre-serata | Alto: store, TikTok, reputazione | Gioco di società senza alcol nel prodotto e nel marketing |
| Umiliazioni e bullismo | Media | Alto | Consenso privato, livello minimo del gruppo, filtri |
| Minori nei livelli piccanti | Media | Alto (Garante [15]) | Livelli piccanti solo per maggiorenni, con verifica dell'età |
| GDPR (memoria del gruppo) | Media | Medio-alto | Solo dati su di sé, cancellazione automatica |
| AI Act, art. 50 | Certa (obbligo) | Basso, se gestito | Avviso "presentatore AI", marcatura di audio e immagini |
| Proprietà intellettuale | Bassa | Medio | Nomi e grafica propri |
| Piattaforme gratuite | Media-alta entro il 2027 | Alto | Velocità, nicchia, comunità |

---

## 8. Acquirente e CAC

### Chi decide e chi paga
- In casa decide chi ha lo schermo e la cassa, di solito chi ospita.
- Il gioco però lo lancia spesso l'"animatore" del gruppo, per esempio chi ha creato il gruppo WhatsApp (stima, da verificare nel test).
- Paga uno per tutti, come con Jackbox (n.v.). È un bene per la viralità: gli altri giocano gratis.
- Come presentare il prezzo: 1,99 € per 12 persone sono 0,17 € a testa (stima).

### Crescita virale: i dati trovati
- **Kahoot.**
  - Nel 2020 ha avuto più di 250 milioni di partite e circa 1,5 miliardi di giocatori, cioè circa 6 giocatori per partita (stima) [18].
  - Dal 2013 conta più di 9 miliardi di partecipanti; l'azienda parla di "distribuzione virale" [18].
- **Gartic Phone** (uscito nell'ottobre 2020).
  - Picco di 252.500 spettatori su Twitch (giugno 2021).
  - Clip su TikTok da 3,2 e 10,2 milioni di visualizzazioni [19].
  - Agli streamer piace perché si spiega in pochi secondi [19].
  - Non ho trovato dati sui giocatori.
- **Jackbox:** nessun dato ufficiale sul passaparola. Stime di terzi, solo Steam:
  - il Party Pack 2 ha venduto circa 1,1 milioni di copie, per circa 19 M$;
  - i Party Pack 9 e 11 hanno venduto circa 23–24 mila copie ciascuno;
  - chi compra un pacchetto ci gioca 12–14 ore in tutto [20].
  - La mia lettura: un formato con contenuti fissi si consuma.
- **Valori di riferimento del fattore K:**
  - per un prodotto consumer, 0,15–0,25 è buono, 0,4 ottimo e 0,7 eccezionale (attribuito a Rahul Vohra) [21];
  - la media delle app consumer è 0,05–0,2 [21];
  - per i giochi una fonte indica 0,4–1,2, senza dati primari [21].
- **Attenzione: "esposto" non vuol dire "nuovo cliente".** Conta solo chi poi ospita a sua volta. Nei giochi di società ospitano in pochi.

**Fattore K stimato** = persone esposte per serata × serate per ospite (1,5) × quota di esposti che poi ospitano (stima):

| Esposti per serata | 1% ospita | 3% ospita | 5% ospita |
|---|---|---|---|
| 7 | 0,10 | 0,32 | 0,53 |
| 11 | 0,17 | 0,49 | 0,83 |
| 15 | 0,23 | 0,67 | 1,12 |

### Canali

| Canale | Come funziona | Costo (stima) | Rischio |
|---|---|---|---|
| **Ciclo dentro il prodotto (QR)** | Ogni serata porta 7–19 persone nel gioco. Alla fine: "ospita tu la prossima, la prima è gratis" | Costo AI della serata gratuita: 0,06 € senza voce, 0,22 € con voce | Pochi diventano ospiti |
| **TikTok, Reels, Shorts** | Clip automatiche di 15 secondi: rivelazioni, "verdetti" del presentatore, sfide | Il tempo di Lorenzo; le clip le genera l'app | Algoritmo; nomi e volti degli amici; alcol escluso dal feed [13] |
| **ESN e welcome week** | Versione "evento" su grande schermo per 50–300 persone, gratis per le sezioni in cambio di visibilità | 0 € con uno scambio; 200–500 € con una sponsorizzazione (n.v.) | Stagionale: settembre-ottobre e febbraio-marzo |
| **Ambasciatori nelle residenze** | Pass gratis più 2 € per ogni ospite pagante portato | 2,5–4 € per pagante | Tenere motivati gli ambasciatori |
| **Partner per eventi** (bar, organizzatori) | "Quiz AI" nelle serate Erasmus nei locali; può diventare anche un ricavo B2B | Vendita diretta | Spesso hanno sponsor di alcolici |
| **Pubblicità a pagamento** | Solo per testare i messaggi | 25–184 € per ospite pagante | LTV/CAC sotto 0,3 |

### Costo per installazione (CPI) dei giochi casual
- Tra febbraio 2024 e febbraio 2025: **1,41 $ su iOS e 0,14 $ su Android** (Liftoff, via Statista) [22].
- L'Europa occidentale sta tra America Latina e Nord America; il Regno Unito costa il 20–40% meno degli USA [22].
- Nel 2026 il CPI casual su iOS nei mercati occidentali è salito del 38% in un anno; i giochi nei Paesi principali costano 4,22 $ su iOS e 2,97 $ su Android (fonti secondarie, n.v.) [22].
- Una web app non si installa: il costo vero è quello per "prima stanza creata", probabilmente più alto del CPI (stima).

### Rapporto LTV/CAC (stima)
**Valore del cliente (LTV), base 7,05 €.**
- L'abbonamento a 3,99 €/mese rende 2,78 € netti, dopo IVA e commissione dello store del 15% [33].
- Con 2 serate al mese nella versione essenziale restano 2,34 € al mese.
- In 3 mesi pagati l'LTV è 7,05 €; in 2 mesi 4,70 €; in 5 mesi 11,74 €.
- Con il pass serata l'LTV va da 2,34 € a 5,85 €, per 2–5 pass.

| Canale | CAC per ospite pagante | LTV/CAC (LTV 7,05 €) |
|---|---|---|
| Pubblicità, CPI 1,41 $, conversione a pagante 2–5% | 24,5–61,3 € | 0,12–0,29 |
| Pubblicità, CPI 4,22 $ (n.v.), conversione 2–5% | 73–184 € | 0,04–0,10 |
| Ambasciatori | 2,5–4 € | 1,8–2,8 |
| Ciclo nel prodotto: 7–10 serate gratuite per ogni pagante | 0,4–2,2 € | 3–18 |
| ESN a pagamento (200–500 € a evento, n.v.) | oltre 100 € | sotto 0,1 |

**Conclusione: la pubblicità non conviene mai. Il modello sta in piedi solo se il ciclo virale funziona.**

---

## 9. Costruzione e dati

### Architettura consigliata: web app senza installazione, nativa solo dopo

| | Web app (PWA) con QR | App nativa |
|---|---|---|
| Ingresso di 12 persone | **Immediato: QR e browser, senza installare nulla.** Decisivo nel pre-serata | Ognuno deve installare: in un pre-serata nessuno lo fa |
| Revisione degli store | Nessuna all'inizio: niente rischio 4.3 o 1.4.3 | Rischio di rifiuto [9] |
| Pagamenti | Via web, con Apple Pay e Google Pay. La commissione fissa pesa sui micro-pagamenti (Stripe 1,5% + 0,25 €, n.v.) | Commissione dello store del 15% per le piccole imprese [33] |
| Notifiche e ritorno | Limitate su iOS (n.v.) | Migliori: "è venerdì, giochiamo?" |
| Audio, schermo acceso | Restrizioni sull'avvio automatico dell'audio; per tenere lo schermo acceso serve una funzione apposita del browser (n.v.) | Migliori |
| Visibilità | Nessuna ricerca negli store | Ricerca e classifiche |

**Consiglio: schema ibrido, come Jackbox.**
- I giocatori entrano sempre dal browser.
- L'ospite usa la web app sullo schermo condiviso o sul telefono.
- Un'app nativa per l'ospite arriva solo dopo aver dimostrato che i gruppi tornano.

### Tempo reale e latenza
- **Server di gioco:** una stanza per serata, con lo stato della partita tenuto dal server. I telefoni comunicano con WebSocket e si riconnettono da soli quando lo schermo si spegne.
  - Strumenti possibili: Cloudflare Durable Objects, PartyKit, Colyseus (n.v.).
- **La rete non è il collo di bottiglia.** È un gioco a turni, e un ritardo di 100–200 ms non si nota (n.v.).
- **Il collo di bottiglia è l'AI**, che impiega alcuni secondi per rispondere. Per nasconderlo:
  - il turno successivo si genera mentre si gioca quello in corso;
  - il primo gioco parte con contenuti già pronti, mentre i giocatori completano il loro profilo.
- **Voce:**
  - le frasi si sintetizzano in anticipo;
  - ElevenLabs Flash dichiara circa 75 ms di latenza [29];
  - l'audio esce solo dallo schermo condiviso, per evitare l'eco;
  - l'input resta sui telefoni, perché riconoscere più voci in una stanza rumorosa è difficile (n.v.).

### Costi per serata
**Scenario (stima):**
- 12 giocatori, 4 lingue, circa 75 minuti, circa 40 turni.
- Circa 263 mila token in ingresso e 63 mila in uscita, così ripartiti:
  - generazione dei contenuti: 50 mila in ingresso, 10 mila in uscita;
  - battute del presentatore: 120 mila e 6 mila;
  - giudice delle risposte creative: 23 mila e 5 mila;
  - moderazione: 20 mila e 3 mila;
  - traduzione verso 3 lingue in più: 50 mila e 40 mila.
- Il costo è per stanza, non per giocatore. Crescono con il gruppo solo la traduzione (con le lingue) e la moderazione (con i giocatori).

**Costo dei modelli per serata, con tutto sullo stesso modello (stima):**

| Modello | Prezzo per 1 M token (ingresso / uscita) | Costo per serata |
|---|---|---|
| Claude Haiku 5.5 | 0,10 $ / 0,50 $ [28] | 0,05 € |
| GPT-5.4-nano | 0,20 $ / 1,25 $ [26] | 0,11 € |
| Gemini 3.1 Flash-Lite | 0,25 $ / 1,50 $ [27] | 0,14 € |
| Gemini 3 Flash | 0,50 $ / 3 $ [27] | 0,28 € |
| **Sonnet 5.5 per la creatività + Haiku 5.5 per il resto** | — | **0,29 €** |
| GPT-5.4-mini | 0,75 $ / 4,50 $ [26] | 0,42 € |
| Claude Sonnet 5.5 | 2 $ / 10 $ [28] | 1,01 € |
| Claude Opus 5.5 | 4 $ / 20 $ [28] | 2,01 € |
| GPT-5.5 | 5 $ / 30 $ [26] | 2,79 € |

- I prezzi di OpenAI e Google vengono da siti terzi aggiornati a metà 2026 [26][27].
- La memoria temporanea dei prompt (cache) riduce il costo dell'ingresso: le regole e il prompt di sistema si ripetono più di 60 volte a serata. Su Sonnet 5.5 la lettura dalla cache costa 0,20 $ per milione di token [28]. Risparmio stimato sull'ingresso: oltre il 50% (stima).

**Voce del presentatore:** circa 1.800 parole, cioè 10.800 caratteri e 12 minuti, in una sola lingua; i telefoni mostrano i sottotitoli tradotti.
- OpenAI gpt-4o-mini-tts (circa 0,015 $/minuto) [30]: **0,16 €**.
- ElevenLabs Flash v2.5 (0,05 $ ogni 1.000 caratteri) [29]: **0,47 €**.
- ElevenLabs v3 o Multilingual v2 (0,10 $ ogni 1.000 caratteri) [29]: **0,94 €**.
- Non ho trovato i prezzi della voce di Gemini.

**Immagini, solo per i giochi di disegno (20 a serata):**
- GPT Image 1 Mini, bassa qualità (circa 0,005 $ l'una) [31]: **0,09 €**.
- Gemini 2.5 Flash Image (0,039 $) [31]: **0,68 €**.
- Nano Banana 2, a 1K (0,067 $) [31]: **1,17 €**.

**Server in tempo reale:** meno di 0,01 € a serata, a volumi bassi (stima, n.v.).

| Versione | Componenti | Costo per serata |
|---|---|---|
| **Essenziale** | Haiku 5.5, gpt-4o-mini-tts, senza immagini | **0,22 €** |
| **Standard** | Sonnet 5.5 per la creatività + Haiku 5.5, ElevenLabs Flash, 20 immagini Mini | **0,85 €** |
| **Premium** | Sonnet 5.5 ovunque, ElevenLabs v3, 20 immagini Flash Image | **2,63 €** |

**Margini (stima):**
- Un pass da 1,99 € rende 1,39 € netti con lo store, oppure 1,36 € via web con Stripe (n.v.).
- Un abbonamento da 3,99 € rende 2,78 € netti con lo store, oppure 2,97 € via web.

| Versione | Margine lordo |
|---|---|
| Essenziale | 84% |
| Standard | 39% |
| Premium | −90% |

- La versione gratuita deve costare pochissimo: niente voce, modello economico, circa 0,06 € a serata.

### Controllo dei contenuti
1. **In ingresso:**
   - ognuno scrive solo di sé, in privato;
   - dei presenti entrano solo i nomi;
   - ognuno indica i temi che non vuole.
2. **Generazione:**
   - regole vincolanti nel prompt;
   - formato strutturato (JSON) e modelli di domanda già approvati;
   - divieto di contenuti su categorie sensibili e su persone assenti.
3. **In uscita:**
   - un classificatore di moderazione, gratuito con OpenAI (n.v.), più filtri su nomi e temi;
   - prima del lancio, una prova con circa 500 tentativi di abuso (stima).
4. **Livelli "piccante":**

   | Livello | Contenuto |
   |---|---|
   | 0 | Per tutti |
   | 1 | Prese in giro leggere |
   | 2 | Flirt |
   | 3 | Piccante |

   - I livelli 2 e 3 sono solo per maggiorenni, con verifica dell'età e consenso di ogni giocatore.
   - Vale il livello più basso del gruppo, scelto in modo anonimo.
5. **Durante la partita:** pulsante "salta" anonimo, segnalazioni, registro per 30 giorni.

### Dati e apprendimento: quali domande fanno ridere?
- **Segnali raccolti:**
  - un tocco "😂" dopo ogni rivelazione;
  - quante domande vengono saltate;
  - il tempo di risposta;
  - i voti per la risposta migliore;
  - le clip esportate e le partite rigiocate.
- **Quanti dati:** una serata ha circa 40 contenuti votati da 12 persone, cioè circa 480 voti; 1.000 serate danno circa 480 mila voti (stima).
- **Come si usano:**
  1. **Da subito:** un algoritmo di scelta che impara quali modelli di domanda e quali giochi funzionano per ogni tipo di gruppo (dimensione, lingue, livello).
  2. **Dopo circa 100 mila contenuti votati:** un modello che riordina le proposte, oppure l'addestramento sulle preferenze (DPO) di un piccolo modello presentatore (stima).
- **Perché i voti umani contano:**
  - i giudici AI favoriscono le risposte lunghe e dipendono dall'ordine in cui le leggono [32];
  - i modelli di punta concordano poco con i gusti umani e scelgono risposte simili tra loro (fonte secondaria) [32];
  - quindi i voti dei giocatori sono un dato proprio e raro.
- **Privacy:** si addestra solo su modelli di domanda resi anonimi, mai sui segreti dei giocatori.

### Prodotto minimo
- **Per il test**, in 2–3 settimane a tempo pieno con gli strumenti AI del 2026 (stima):
  - stanze con QR;
  - schermo condiviso;
  - 3 giochi: "chi è più probabile che…", parola segreta multilingue, quiz sul gruppo;
  - lingua per giocatore;
  - voce del presentatore;
  - moderazione e livelli;
  - pulsanti di voto, esportazione delle clip;
  - analisi dei dati e link di pagamento.
- **Versione pubblica:** 6–8 settimane (stima).
- **Costi:**
  - test sotto 1.000 €: API, piano ElevenLabs, dominio, hosting (stima);
  - versione pubblica sotto 5.000 €, comprese grafica, informativa privacy e termini (stima).
- La perdita massima di 20 k€ non è mai a rischio nelle prime due fasi.

---

## 12. Cosa la ucciderebbe e test più economico

### Tre motivi di fallimento
1. **Effetto novità.** Si ride una sera, poi si torna a chiacchierare e a mettere musica. Senza partite ripetute niente abbonamento, e i pass rendono troppo poco.
2. **Il pre-serata non è il momento giusto.**
   - La gente arriva a orari diversi, c'è musica, si parla.
   - Un gioco strutturato da 45 minuti compete con la conversazione, e il telefono in mano isola.
   - In più l'ospite non paga, perché il gratis basta: Meta AI, Netflix, giochi a dita puntate.
3. **Nessuno diventa ospite, oppure un incidente.**
   - Se meno dell'1,5% dei giocatori ospita una partita, il fattore K resta sotto 0,25, e la pubblicità non conviene.
   - Oppure un incidente di contenuti: un'umiliazione, un minore nel livello piccante, l'associazione con l'alcol. Le conseguenze possono essere il ritiro dallo store, l'esclusione dal feed di TikTok o un intervento del Garante.

### Protocollo di test: 3–4 settimane, 12–20 serate
- **Il momento è ideale:** il semestre è appena iniziato e i gruppi Erasmus si stanno formando. A metà dicembre molti partono; la seconda occasione è la coorte di febbraio.
- **Settimana 0:** prodotto minimo con i 3 giochi, misure già attive e soglie scritte prima.
- **Settimane 1–3:** 12–20 serate.
  - In un terzo delle serate c'è Lorenzo, che osserva e prende appunti.
  - **In due terzi non c'è:** Lorenzo dà solo il link all'ospite.
  - Gruppi da 6 a 20 persone, con almeno 3 lingue.
  - Fonti dei gruppi: i suoi contatti, 2 sezioni ESN, 1 residenza.
- **Fine di ogni serata:**
  - una domanda NPS a tutti i giocatori;
  - all'ospite, l'offerta reale "prossima serata 1,99 €" oppure "3,99 €/mese", con pagamento vero tramite link.
- **Settimana 4:**
  - misura delle partite ripetute e dei nuovi ospiti nei 21 giorni successivi, tracciati con il link della stanza;
  - interviste a 8 ospiti.
- **Budget:** meno di 1.000 €. Anche con la versione premium, 20 serate costano circa 53 € di AI (stima).

### Metriche e soglie (fissate prima)

| Metrica | Si va avanti se | Ci si ferma se | Riferimenti |
|---|---|---|---|
| Durata della partita attiva (mediana) | ≥ 40 min | < 20 min | Nessun dato trovato sulle sessioni di Jackbox. Chi possiede Jackbox ci gioca 12–14 ore in tutto [20] |
| Giochi per serata | ≥ 3 | ≤ 1 | — |
| **Gruppi che rigiocano entro 14 giorni, senza solleciti** | **≥ 40%** | **< 15%** | GameAnalytics 2026: ritorno dopo 7 giorni sotto il 4% per la metà dei giochi, sopra il 25% per i migliori [24] |
| **Giocatori che lanciano una partita da soli entro 21 giorni** | **≥ 5%** (K ≈ 0,8) | **< 1,5%** (K ≈ 0,25) | Fattore K: 0,4 è ottimo [21]. Kahoot: circa 6 giocatori per partita [18] |
| NPS dei giocatori | ≥ 50 | < 20 | Nessuna media di settore trovata [25]; tra amici il voto è gonfiato di 10–20 punti (stima) |
| Ospiti che pagano davvero (pass da 1,99 € o 3,99 €/mese) | ≥ 20% | < 5% | Le app AI convertono la prova gratuita nell'8,5% dei casi, contro il 5,6% delle altre [33] |
| Video condivisi | ≥ 1 clip pubblicata ogni 4 serate e ≥ 1 clip oltre 10 mila visualizzazioni | 0 clip pubblicate | Gartic Phone: clip da 3,2 e 10,2 milioni di visualizzazioni [19] |
| Incidenti gravi di contenuto | 0 | ≥ 1 non risolvibile con il design | — |

**Regola di decisione:**
- si va avanti se sono rispettate almeno 5 soglie su 8, comprese le due in grassetto;
- ci si ferma se anche una sola delle due in grassetto cade nella zona di stop.

---

## 13. Modelli del 2027 e architettura AI

### a) Cosa diventa più facile
- **Presentatore vocale in tempo reale e multilingue.**
  - ChatGPT ha già una voce che ascolta e parla insieme e traduce in tempo reale (dall'8/7/2026), ma l'API al lancio non c'era [3][4].
  - Nel 2027 sarà probabilmente un componente da collegare, a costi bassi: oggi una voce costa circa 0,015 $ al minuto [30].
  - Resta difficile capire più voci insieme in una stanza rumorosa (n.v.): le risposte passano dai telefoni.
- **Immagini per i giochi di disegno.** Costano già poco: circa 0,005 $ con GPT Image 1 Mini e 0,039 $ con Gemini 2.5 Flash Image [31]. Diventa possibile "l'AI disegna, voi indovinate" quasi in tempo reale.
- **Giudice AI delle risposte creative.**
  - Già oggi le battute generate dall'AI valgono quelle di un umano di livello basso o medio [32].
  - Quando la fonte è nascosta, vengono giudicate come quelle umane [32].
  - Ma come giudici gli LLM sono distorti [32].
  - **Ruolo giusto:** l'AI commenta, il gruppo vota.

### b) Cosa farà da solo il ChatGPT del 2027, e cosa le piattaforme
- **OpenAI** ha chiuso le chat di gruppo ma "esplora funzioni collaborative" [1]. Una "modalità festa" nel 2027 è plausibile (n.v.).
  - Già oggi la voce fa da presentatore di quiz per 3–5 persone su un telefono.
  - Dal 18/12/2025 l'App Directory ospita app di terzi dentro ChatGPT. L'Apps SDK è ancora in anteprima, e nessun gioco compare tra i primi partner [8]. Può diventare un canale di distribuzione, ma non per le partite a più giocatori.
- **Meta** è la minaccia più grande. Ha Meta AI nei gruppi WhatsApp in tutta l'UE [6], cioè dove gli Erasmus si organizzano. Aggiungere giochi di gruppo è un passo naturale (n.v.).
- **Netflix** ha già il formato "TV più telefono via QR" gratis per gli abbonati [7]. Potrebbe aggiungere contenuti personalizzati con l'AI (n.v.).
- **Apple, Google e Discord:** SharePlay e l'app Giochi di Apple, Gemini sulle TV, le Activities di Discord (tutti n.v.). Per gli incontri dal vivo contano meno di Meta e Netflix.

### c) Che vantaggio non replicabile danno

| Leva | Vantaggio | Quanto è replicabile |
|---|---|---|
| **Memoria del gruppo** (ricerca sulla storia del gruppo e sulle battute interne) | Ritorno dei gruppi, contenuti sempre più su misura, "riepilogo del semestre Erasmus" da condividere | Tecnicamente facile. Meta ha già la storia della chat del gruppo; il GDPR limita cosa conservare. Protegge solo se il gruppo "vive" nel gioco. **Medio-basso** |
| **Modello presentatore addestrato sui voti** | Dati rari: preferenze umane sull'umorismo per gruppo, cultura e lingua. I modelli generici concordano poco con i gusti umani [32] | Servono centinaia di migliaia di voti. Chi ha più distribuzione (Netflix, Jackbox, Meta) li raccoglie prima. **Medio** |
| **Game design** | È il prodotto vero: ritmo, rivelazioni, momenti da clip | Le meccaniche non sono protette [17], ma gusto ed esecuzione contano. **Medio** |
| **Comunità e marchio** | "Il gioco degli Erasmus": ogni semestre arrivano nuovi utenti, e chi torna a casa lo porta in oltre 30 Paesi (stima) | Le mode passano. **Medio-basso** |

**Nel complesso la difendibilità è bassa:** voto 2 su 5. L'architettura AI (memoria e preferenze) migliora il prodotto più di quanto lo protegga.

### d) Costo e fattibilità per una persona sola
- **Tempi e costi (stima):**
  - prodotto minimo in 2–3 settimane, versione pubblica in 6–8;
  - test sotto 1 k€, versione pubblica sotto 5 k€.
- **Costi correnti:**
  - 0,22–0,85 € a serata (stima);
  - con 10 mila serate al mese, 2,2–8,5 mila € (stima): crescono con l'uso e vanno coperti dai ricavi.
- **Addestramento:** un ciclo di addestramento sulle preferenze di un piccolo modello aperto costa 100–1.000 € su GPU a noleggio (n.v.). La memoria del gruppo costa poco (n.v.).
- **Ore a regime:** 5–10 a settimana sono plausibili per manutenzione, nuovi giochi e controllo della moderazione, ma solo se la crescita è organica. Nei picchi stagionali (settembre-ottobre, febbraio-marzo) servono più ore.

---

## Voti per la scheda v2

| Voce | Voto | Motivazione |
|---|:--:|---|
| vant | 4 | Ingegnere AI con esperienza di marketing: costruisce il prodotto minimo in 2–3 settimane e sa fare contenuti per TikTok. Ha accesso immediato a gruppi Erasmus per i test. Gli mancano un'esperienza di game design e un pubblico proprio. |
| dolore | 2 | È un piacere, non un problema. Rompere il ghiaccio e divertirsi sono bisogni veri, ma si soddisfano gratis: Meta AI nei gruppi [6], Netflix [7], i giochi a dita puntate. Gli studenti hanno poco budget. |
| mercato | 3 | Il pubblico è enorme: ogni gruppo di amici, e Kahoot ha superato i 9 miliardi di partecipanti [18]. Ma pagano in pochi e i successi sono rari. Gli Erasmus da soli valgono 30–40 k€ l'anno al massimo (stima). |
| margine | 3 | Il margine lordo è dell'84% con la versione essenziale, del 39% con la standard, negativo con la premium (stima). Pesano le serate gratuite, necessarie per la viralità, e la commissione fissa sui micro-pagamenti. |
| valid | 5 | Lorenzo può testare subito, nel momento migliore (semestre appena iniziato), con meno di 1.000 €. In 3–4 settimane ha metriche di comportamento reali e pagamenti veri. |
| solo1M | 2 | Per 300–500 k€ servono 9–15 mila abbonati medi (stima), cioè 0,7–1,2 milioni di nuovi ospiti l'anno. La pubblicità non regge (LTV/CAC tra 0,04 e 0,29). Serve un successo virale in più Paesi. Per arrivare a 1 M€ servirebbe quasi solo un'estensione B2B (bar, eventi, team building), che però richiede vendita. |
| autom | 4 | Contenuti, presentazione, traduzione e moderazione sono automatici. Restano manuali la cura del game design, le novità contro la noia, gli incidenti di contenuto e le campagne stagionali. |
| dif | 2 | Le meccaniche non sono protette [17]. Meta, Netflix e OpenAI possono offrire una versione gratuita [1][6][7]. Memoria e voti aiutano, ma solo dopo milioni di voti. |

**Somma dei voti: 25 su 40** (senza motivazione).

| Motivazione | Punteggio pesato |
|---|---|
| 3 (neutra) | **3,15** |
| 4 | 3,35 |
| 5 | 3,55 (entra in lista, al limite) |

---

## Dati mancanti (budget di ricerche esaurito)
- Prezzi ufficiali della voce di Gemini, della Live API e di gpt-realtime-mini.
- Numeri dell'ESN (sezioni, volontari, partner) e totale UE degli studenti Erasmus nel 2025.
- Valori medi di NPS per i giochi.
- Durata media delle sessioni di Jackbox, Kahoot e dei giochi Netflix.
- Dati ufficiali di Jackbox: giocatori, vendite su console, passaparola.
- Testo ufficiale di:
  - le regole di Google Play sull'alcol;
  - le domande sull'alcol del questionario Apple.
- Testo vigente dell'art. 13 della legge 125/2001 dopo le modifiche del 2025, e regole AGCOM su influencer e alcol.
- Regole pubblicitarie di Meta e TikTok sull'alcol in UE.
- Funzioni di gruppo di Apple, Google TV e Discord nel 2026.
- Conversione da download a pagante per le app di giochi di società.
- Costi per installazione specifici per l'Europa.
- Listini ufficiali di Cloudflare, PartyKit e Stripe.

---

## Fonti
- [1] OpenAI Help Center, ritiro delle chat di gruppo — https://help.openai.com/en/articles/12703475-retiring-group-chats-in-chatgpt
- [2] Lancio delle chat di gruppo (20 persone, funzioni) — https://www.croma.com/unboxed/chatgpt-group-chat-feature-global-rollout ; https://www.iclarified.com/99055/openai-pilots-group-chats-in-chatgpt-letting-you-collaborate-with-friends-and-ai ; https://www.itechguides.com/?p=383300 ; https://www.eesel.ai/en/blog/chatgpt-group-chat-pricing
- [3] GPT-Live (8/7/2026) — https://mer.vin/2026/07/gpt-live-explained-full-duplex-chatgpt-voice-with-gpt-5-5-delegation/ ; https://news.ainauten.com/markdown/openai-soll-gpt-live-1-fuer-natuerlichere-gespraeche-in-chatgpt-ausrollen ; https://observerbd.com/news/586156
- [4] Traduzione di ChatGPT Voice (fonte di un concorrente) — https://www.livelingo.io/guides/gpt-live-translation
- [5] Gemini — https://oneit.charlotte.edu/2026/07/02/ai-helpful-tips-exciting-google-gemini-updates/ ; https://workspaceupdates.googleblog.com/2025/05/gemini-live-in-depth-two-way-conversations.html
- [6] Meta AI in Europa e nei gruppi WhatsApp — https://about.fb.com/news/2025/03/europe-meet-your-newest-assistant-meta-ai/ ; https://www.computing.co.uk/news/2025/ai/meta-ai-launches-in-eu ; https://computing.co.uk/news/2025/ai/meta-rolls-out-ai-on-whatsapp-in-europe-and-users-cannot-disable-it
- [7] Netflix, giochi sulla TV con il telefono — https://techcrunch.com/2025/10/09/netflix-is-letting-users-play-games-on-their-tv-screens ; https://www.tomsguide.com/entertainment/netflix/how-to-set-up-netflix-games-on-tv-all-you-need-is-your-phone ; https://alternativeto.net/news/2025/11/netflix-launches-game-night-for-tv-play-using-phones-as-controllers-no-downloads-required/
- [8] App Directory di ChatGPT — https://www.digitalcitizen.life/chatgpt-gets-an-app-store/ ; https://blog.sista.ai/2026/03/gpt-app-store-guide-how-to-win.html ; https://phiture.com/blog/chat-gpt-app-directory/
- [9] Apple, linee guida 1.4.3 e 4.3, casi di rifiuto — https://developer.apple.com/forums/thread/744164 ; https://developer.apple.com/forums/thread/745135 ; https://developer.apple.com/forums/thread/688592 ; https://cur.at/tol6uU?m=web ; https://developer.apple.com/forums/thread/836116
- [10] Apple, nuove classi d'età — https://9to5mac.com/2025/07/24/apple-notifies-developers-of-new-app-store-age-rating-system/ ; https://www.igeeksblog.com/apple-app-store-age-ratings/ ; https://www.iphoneincanada.ca/2025/07/25/updated-app-store-age-ratings
- [11] Google Play, alcol e IARC — https://www.gummicube.com/blog/google-play-restricts-apps-for-marijuana-alcohol-and-tobacco/ ; https://support.google.com/googleplay/android-developer/answer/9898843 ; https://eucam.info/2015/05/14/alcohol-promotion-through-smartphone-apps-in-breach-of-regulations/
- [12] Legge 125/2001 e AGCOM — https://technical-regulation-information-system.ec.europa.eu/hr/notification/25383/message/107878/IT ; https://legislazionetecnica.it/lt_link/normativa/TDEyNTIwMDE= ; https://www.agcom.it/sites/default/files/media/allegato/2025/197_25_cons_allegato%20B_codice.pdf
- [13] TikTok e alcol — https://www.brewbound.com/news/tiktok-opens-ad-platform-to-beverage-alcohol-brands-in-the-us ; https://www.tspa.org/tiktok.com/ ; https://conductatlas.com/diff/tiktok/tiktok-community-guidelines/4850/5940/
- [14] Verifica dell'età in UE — https://fpf.org/blog/the-eu-commissions-approach-to-age-verification-mobile-apps-dsa-enforcement-and-challenging-national-social-media-bans/ ; https://cadeproject.org/updates/eu-commission-pushes-member-states-to-deploy-eu-age-verification-app-by-year-end/ ; https://www.osborneclarke.com/insights/age-verification-edpb-principles-eu-age-verification-app
- [15] Garante, Replika — https://www.agendadigitale.eu/sicurezza/privacy/replika-sanzionata-dal-garante-ecco-le-falle-nel-sistema-di-verifica-delleta/ ; https://www.cybersecurity360.it/news/garante-privacy-ecco-cosa-contesta-al-chatbot-replika/ ; https://babl.ai/?p=7575
- [16] AI Act, art. 50 — https://www.bakerbotts.com/thought-leadership/publications/2026/september/eu-ai-act-article-50-transparency-obligations-go-live ; https://datamatters.sidley.com/2026/06/24/eu-ai-act-transparency-obligations-preparing-for-compliance-by-2-august-2026/ ; https://www.dastra.eu/en/blog/ai-act-transparency-rules-what-changes-august-2-2026/60164 ; https://www.mccannfitzgerald.com/knowledge/technology-and-innovation/one-month-to-go-eu-ai-act-transparency-compliance ; https://inquisitiveminds.bristows.com/post/102nfaz/the-european-commissions-code-of-practice-on-transparency-of-ai-generated-conten
- [17] Meccaniche di gioco e diritto d'autore — https://coleschotz.com/tetris-defeats-the-clones-in-copyright-infringement-battle ; https://techraptor.net/content/game-mechanics-arent-protected-copyright-according-texas-court-ruling
- [18] Kahoot — https://kahoot.com/blog/2021/02/10/an-update-from-ceo-eilert-hanoa-kahoot-reports-q4-2020-results-delivering-a-year-of-record-high-growth/ ; https://kahoot.com/blog/2021/01/05/kahoot-5-billion-players-year-record-high-growth/ ; https://live.euronext.com/sites/default/files/company_press_releases/attachments_oslo/2023/04/20/588007_2022%20Kahoot%21%20Annual%20Report.pdf
- [19] Gartic Phone — https://streamscharts.com/games/gartic-phone ; https://knowyourmeme.com/editorials/guides/what-is-gartic-phone-and-why-do-streamers-love-it-the-multiplayer-drawing-game-explained
- [20] Jackbox, stime su Steam — https://steampulse.org/game/331670 ; https://steampulse.org/game/397460 ; https://www.steampulse.org/game/1850960 ; https://raijin.gg/app/3364070/The_Jackbox_Party_Pack_11 ; https://playtracker.net/insight/game/95518
- [21] Fattore K — https://inblog.ai/de/glossary/viral-coefficient ; https://www.saxifrage.xyz/post/k-factor-benchmarks ; https://appstorys.com/blog-Viral-Coefficient-Network-Effects-Growth ; https://echai.ventures/startingup/retention-referral/what-s-a-viral-coefficient-and-is-chasing-a-k-factor-above-1-realistic-for-my-kind-of-product
- [22] Costo per installazione — https://www.statista.com/statistics/1241651/global-cpi-casual-gaming-apps-genre-platform ; https://thesocialoutline.com/blog/cpi-benchmarks-mobile-gaming ; https://foxdata.com/en/blogs/2026-mobile-game-user-acquisition-cost-benchmarks-how-much-should-you-spend/ ; https://gamegrowthadvisor.com/blog/2026-03-17-user-acquisition-cpi-benchmarks-2026/
- [23] Erasmus+: nel 2024 quasi 1,5 milioni di mobilità (tutte le categorie); in Italia nel 2025, 36.013 studenti in partenza — https://erasmus-plus.ec.europa.eu/node/5745 ; https://www.orizzontescuola.it/erasmus-2025-oltre-40mila-partenze-dallitalia-12-il-95-degli-universitari-promuove-lesperienza-allestero/ ; https://www.oph.fi/en/news/2026/international-mobility-higher-education-students-continued-increase-2025
- [24] Ritorno dei giocatori, GameAnalytics 2026 — https://investgame.net/wp-content/uploads/2026/01/2026-01-27-2026-mobile-pc-benchmarks_compressed.pdf ; https://gameindustrylibrary.com/documents/gameanalytics-mobile-and-pc-game-benchmarks-in-2026-sponsored-by-pwn-games ; https://appagent.com/?p=61637 ; https://appfollow.io/blog/mobile-game-retention
- [25] NPS: nessuna media di settore trovata — https://customergauge.com/benchmarks/companies/activision-blizzard-inc
- [26] Prezzi OpenAI (siti terzi, metà 2026) — https://morphllm.com/openai-api-pricing ; https://modelcompare.dev/pricing/openai-api-pricing ; https://www.aipricing.guru/blog/openai-api-pricing-guide-2026/
- [27] Prezzi Gemini (siti terzi) — https://www.morphllm.com/gemini-api-pricing ; https://benchlm.ai/google/api-pricing ; https://anotherwrapper.com/llm-pricing/gemini-3.5-flash-lite
- [28] Prezzi Anthropic (listino dello strumento claude-api, 6/10/2026) — https://platform.claude.com/docs/en/about-claude/pricing
- [29] ElevenLabs — https://apiframe.ai/guides/elevenlabs-api-guide ; https://aireiter.com/blog/elevenlabs-eleven-v3-api-guide ; https://www.activepieces.com/blog/elevenlabs-pricing-2026-plans-credits-and-costs
- [30] Voce di OpenAI — https://techsy.io/en/blog/best-tts-apis-developers ; https://www.llmreference.com/model/gpt-4o-mini-tts/openai-api ; https://futureagi.com/llm-cost-calculator/openai/gpt-4o-mini-tts
- [31] Immagini — https://intuitionlabs.ai/articles/ai-image-generation-pricing-google-openai ; https://benchlm.ai/media-pricing/nano-banana ; https://ecorpit.com/ai-image-generation-api-cost-comparison-2026/
- [32] Umorismo e LLM — https://ojs.aaai.org/index.php/AAAI/article/view/40567 ; https://aclanthology.org/2025.chum-1.9.pdf ; https://aclanthology.org/2026.chum-1.7/ ; https://dev.to/autonainews/cards-against-llms-reveals-5-top-models-fail-human-humor-test-52h ; https://www.alphaxiv.org/abs/2604.19786v2
- [33] Da ricerche precedenti nel repository:
  - RevenueCat 2026 — https://techcrunch.com/2026/03/10/ai-powered-apps-struggle-with-long-term-retention-new-report-shows
  - Commissioni degli store in UE dal 1/10/2026 — https://www.macrumors.com/2026/08/18/eu-app-store-fee-change/ ; https://phiture.com/blog/apple-new-app-store-terms-2026/

**Contraddizioni trovate**
- Nome dei nuovi modelli vocali di OpenAI: "GPT-Live-1" in alcune fonti, "GPT-Live-One" in altre [3].
- Prezzo di gpt-4o-mini-tts: 0,60 $ + 12 $ per milione di token secondo una fonte, 2,50 $ + 10 $ secondo un'altra [30].
- Pubblicazione del codice di condotta UE sulla trasparenza: 10/6/2026 oppure 31/7/2026 [16].
- ElevenLabs Multilingual v2: 0,10 $ ogni 1.000 caratteri secondo il listino delle API, 0,17 $ secondo un calcolo basato sui crediti [29].
