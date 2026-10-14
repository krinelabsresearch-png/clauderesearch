# Lista: idee per i bisogni dei prossimi 1–5 anni (candidati sopra 3,5)

**Stato al 13/10/2026, ore 16:50 UTC: 8 candidati in lista su 33 studiati, più la 153 (gioco di società AI) in valutazione.**
- La ricerca continua su altri 8 candidati (vedi in fondo).
- La lista è completa quando arriva ad almeno 10 candidati, oppure, come mi hai chiesto, quando i crediti arrivano al 90%.

## Come è stata fatta
- **Criteri** (tue decisioni del 13/10/2026):
  - obiettivo 300–500 k€ l'anno senza dipendenti, con una strada verso 1 M€;
  - mercato UE e mondo, con l'Italia come possibile punto di partenza;
  - B2B ammesso;
  - motivazione 5, data da te, per 092, 093, 096 e 109;
  - per gli ultimi candidati, anche l'ottica dei modelli del 2027 e di un'architettura AI vera e propria.
- **Ricerca.** Per ogni candidato un agente ha risposto alle 12 domande:
  1. mercato;
  2. concorrenti;
  3. come fanno oggi;
  4. cosa fa in più di ChatGPT;
  5. disponibilità a pagare;
  6. monetizzazione;
  7. rischi;
  8. acquirente e CAC;
  9. costruzione e dati;
  10. perché adesso;
  11. voti;
  12. cosa la ucciderebbe e test più economico.

  I dossier completi, con le fonti, sono in [dossier/](dossier/).
- **Punteggio.** Scheda v2: pesi in [../scheda_v2.py](../scheda_v2.py), voti in [punteggi.py](punteggi.py). In lista solo con punteggio sopra 3,5.
- **Limiti.** WebFetch non funzionava, quindi i dati vengono dagli estratti delle ricerche web. Nei dossier i dati non verificati sono segnati "n.v." e le stime "stima".

## Tre cose da sapere prima di leggere
1. **Solo 107 (tesi con dati) e 116 (biostatistico) superano 3,5 anche con motivazione neutra.** Gli altri sei entrano grazie alla motivazione:
   - la tua per 096, 109, 093 e 092;
   - la mia stima (4) per 127 e 113.
2. **Nessuno arriva a 1 M€ con la sola Italia.** Per 300–500 k€ serve quasi sempre un secondo mercato: l'UE in altre lingue, o il mondo in inglese.
3. **"Cosa fa in più di ChatGPT da 20 $/mese".**
   - La risposta è forte quando il prodotto fa ciò che una chat non può fare:
     - calcoli verificati da codice (107, 116, 096, 127);
     - azioni sui dati del cliente (113);
     - un servizio chiuso e sicuro per i minori (093).
   - È debole quando vende soprattutto un percorso (109, 092). Con i modelli del 2027 questa distanza aumenta.

## La lista in breve

| # | Idea | Punteggio (neutro) | Chi paga | Cosa fa in più di ChatGPT da 20 $/mese | Prezzo | Strada verso 300–500 k€ | Test |
|---|---|---|---|---|---|---|---|
| 1 | **107 Assistente AI per la tesi con dati** | 3,85 (3,65) | Laureandi di psicologia, economia, area sanitaria | Numeri calcolati da codice con verifiche obbligatorie; sintassi SPSS e jamovi; dati sanitari in UE; registro dell'uso dell'AI; allenamento alla discussione | Pacchetto 99–149 € | Italia 50–290 k€; poi Spagna e Francia, o i dottorandi | ≤1,5 k€, 4–6 settimane |
| 2 | **096 Tutor AI per Analisi 1, Geometria e Fisica 1** | 3,85 (3,45) | Universitari del primo anno | Correttezza verificata dal calcolo simbolico; primo errore trovato sullo scritto a mano; esercizi nello stile dell'esame; piano fino all'appello | Pass 29–39 € a sessione | Italia 50–100 k€; serve la nicchia del semestre filtro o altri Paesi UE | ≤3 k€, appello di gennaio 2027 |
| 3 | **116 Biostatistico AI per medici e ricercatori** | 3,75 (3,55) | Specializzandi, ricercatori, laboratori (mondo) | Protocollo fisso (ChatGPT va dal 32,5% al 92,5% di accuratezza a seconda del prompt); risultati riproducibili; materiale pronto per la rivista; dati nel browser; risposte ai revisori | 49 €/mese; 249 € ad articolo | 400 k€ ≈ 1.000 abbonati | ≤4 k€, 6 settimane |
| 4 | **093 Tutor di matematica AI a voce, 6–13 anni** | 3,70 (3,30) | Genitori | ChatGPT è vietato sotto i 13 anni: servizio chiuso e sicuro, a voce, sul programma italiano, con diagnosi degli errori e report ai genitori | 9,99 €/mese | 3–5 mila famiglie, almeno metà arrivate senza pubblicità | 2–3 k€, 4–6 settimane |
| 5 | **109 Matematica per lavorare con l'AI** | 3,65 (3,25) | Adulti di 25–40 anni | Lingua; tutor AI vincolato al calcolo; visualizzazioni; progetti e portfolio. Math Academy fa già il percorso adattivo | 99–129 €/anno | Solo italiano 100–300 k€; in inglese contro Math Academy e Brilliant | circa 2 k€, 4 settimane |
| 6 | **092 Allenatore AI dell'esame orale** | 3,65 (3,25) | Maturandi (o i genitori) e universitari | Formato reale dell'esame; voto su griglia calibrata; copertura del programma; misure sull'esposizione | Pass 29–39 € | Italia 150–400 k€; per 1 M€ servono Francia, Germania e Spagna | 1,5 k€, sessione di gennaio 2027 |
| 7 | **127 Preparazione AI agli esami attuariali (P e FM)** | 3,60 (3,40) | Aspiranti attuari (mondo, in inglese) | Banca di domande calibrata sull'esame; soluzioni ricalcolate due volte; probabilità di superamento calibrata sugli esiti reali | 129 $ a esame | 300 k€ possibile ma non probabile (circa 3.100 pacchetti l'anno) | ≤6 k€, 8 settimane |
| 8 | **113 Revenue manager AI per club di padel** | 3,55 (3,35) | Club di padel (B2B) | Legge le prenotazioni ogni giorno, prevede la domanda, manda le offerte e misura con un gruppo di controllo: ChatGPT non può farlo | €49–149/mese | 240–400 club in 3–4 Paesi | ≤€1.500, 5–6 settimane |

**Sinergie.**
- 107 e 116 usano lo stesso motore statistico per due mercati.
- 107 e 092 diventano "analisi della tesi più allenamento alla discussione".
- 096, 093, 127 e 109 condividono il motore di esercizi verificati.

## Schede complete
Ogni scheda risponde a tutte le domande. Il dettaglio e le fonti sono nel dossier collegato.

### 107 · Assistente AI per la tesi con dati (statistica e metodo)
**Punteggio 3,85** (con motivazione neutra: 3,65, l'unica sopra soglia anche senza la tua motivazione) · B2C, studenti · [dossier](dossier/092-107.md)

**Cos'è.** Guida il laureando di psicologia, economia, scienze sociali o area medica nell'analisi statistica della tesi:
- sceglie il test giusto e controlla le assunzioni;
- calcola tutto con il codice;
- produce le tabelle APA e la sintassi per SPSS e jamovi;
- lo allena a difendere l'analisi alla discussione.

Non scrive la tesi.

- **Mercato.**
  - Italia: 334.601 laureati AlmaLaurea nel 2025 (in tutto 360–400 mila). Le tesi con analisi quantitative sono stimate in 65–90 mila l'anno, e 40–60 mila studenti hanno davvero bisogno di aiuto.
  - UE: circa 4,5 milioni di laureati l'anno, da cui 0,9–1,1 milioni di tesi quantitative (stima).
  - Si paga già: un tutor di statistica costa 50 €/h (pacchetti da 250–500 €); Julius AI ha oltre 2 milioni di utenti a 20–45 $/mese.
- **Concorrenti.**
  - Julius AI (USA): oltre 2 milioni di utenti, 10 M$ raccolti, 20–45 $/mese con il 50% di sconto per gli studenti. Non è pensato per la tesi.
  - Intellectus Statistics (USA): da 59,99 $, formato APA, solo in inglese.
  - Tesify (Italia): beta gratuita, dichiara 9.000 studenti. Aiuta a scrivere; un modulo di statistica non è verificato.
  - iWeaver Thesis Writer: scrive la tesi al posto dello studente, con rischio penale.
  - jamovi e JASP: gratuiti, ma non dicono quale test scegliere.
  - Tutor privati e servizi di "elaborazione dati" (area grigia).
  - ChatGPT con l'analisi dei dati e Gemini, gratis per gli studenti.
- **Come fanno oggi.** Si appoggiano a relatore, dottorandi, ChatGPT, YouTube e SPSS o jamovi. Quando si bloccano pagano un tutor. Gli errori tipici:
  - test sbagliato;
  - assunzioni saltate;
  - alla discussione non sanno spiegare cosa hanno fatto.
- **Cosa fa in più di ChatGPT da 20 $/mese.**
  1. I numeri li calcola sempre codice verificato (R e Python), mai l'LLM. Le verifiche delle assunzioni sono obbligatorie e la scelta del test segue un albero di decisione. ChatGPT a volte sceglie il test sbagliato, e lo studente non se ne accorge.
  2. Tabelle APA in italiano, più la sintassi equivalente per SPSS e jamovi: lo studente rifà tutto con i programmi dell'ateneo e lo mostra al relatore.
  3. Dati sanitari (psicologia, medicina) su server in UE, con accordo sul trattamento e senza addestramento. Caricare dati di pazienti su ChatGPT è un problema di GDPR (art. 9).
  4. Un registro dell'uso dell'AI, da allegare alla dichiarazione che gli atenei ora chiedono.
  5. Allenamento alla discussione: le 20 domande probabili della commissione, e la verifica che lo studente abbia capito.

  **Giudizio.** I punti 1 e 2 li ottiene anche un esperto con un buon prompt; i punti 3–5 sono il vero motivo per pagare. Si vende la certezza di non sbagliare e di capire. È un pacchetto per la durata della tesi, non un abbonamento a vita.
- **Quanto pagherebbero.** 29 €/mese (minimo 2 mesi), oppure un "Pacchetto Tesi" da 99–149 € per 3–4 mesi. Costa meno di due ore di tutor.
- **Fatturato.**
  - Italia, con l'1–3% delle tesi: 700–2.700 clienti, cioè 50–290 k€ l'anno.
  - **300–500 k€:** Italia più Spagna e Francia, oppure i dottorandi.
  - **1 M€:** l'1–1,5% delle tesi UE, in 4–5 lingue.
  - Margine lordo oltre il 90% (1–5 € di costo a tesi). Il cliente se ne va dopo la laurea, ma può tornare per la magistrale.
- **Rischi.**
  - Legge 475/1925: è reato presentare come proprio un lavoro altrui, ed è punito anche chi lo esegue. Il prodotto spiega e guida; non scrive capitoli e non dice "facciamo noi l'analisi".
  - Linee guida degli atenei sull'AI.
  - GDPR art. 9: valutazione d'impatto e server in UE.
  - Un errore statistico scoperto alla discussione.
  - Julius o ChatGPT potrebbero specializzarsi sulle tesi.
- **Acquirente e CAC.** Laureandi di 22–27 anni, 2–6 mesi prima della sessione. Canali:
  - Google su ricerche ad alta intenzione ("t test o Mann-Whitney", "come scrivere i risultati SPSS");
  - YouTube in italiano;
  - gruppi dei corsi;
  - creator di psicologia.

  CAC di 10–60 € con la pubblicità, sotto i 10 € con contenuti SEO e YouTube. Valore di un cliente 71–106 €, quindi **LTV/CAC 1,5–7: il migliore del gruppo.**
- **Come si costruisce.**
  - Web app che accetta file CSV, XLSX e SPSS.
  - Ambiente di calcolo isolato in UE, con R e Python.
  - Un agente che:
    1. ricostruisce la domanda di ricerca e il disegno dello studio;
    2. costruisce il piano di analisi con un albero di decisione (tipo di variabili, campioni appaiati o indipendenti, normalità, potenza, confronti multipli);
    3. esegue il codice;
    4. produce tabelle, grafici e sintassi;
    5. interroga lo studente.
  - Qualità controllata su 200 casi presi dai manuali, con risultati confrontati con jamovi e R.
  - Dati: solo quelli dell'utente; dataset pubblici o sintetici per le demo.
  - Prodotto minimo: 6–8 settimane, 3–6 k€.
- **Perché adesso.**
  - Gli atenei chiedono di dichiarare l'AI e vietano il testo generato: serve un aiuto lecito.
  - Gli LLM ora eseguono codice in modo affidabile.
  - Iscritti al massimo storico, e le telematiche sono al 15%.
  - Finestra di 12–24 mesi.
- **Cosa la ucciderebbe.** ChatGPT, Gemini e il relatore bastano; il mercato italiano è piccolo; un caso sui giornali la bolla come "tesi fatta dall'AI".
- **Test più economico** (4–6 settimane, al massimo 1.500 €):
  - una landing page, 5 articoli SEO e 3 video;
  - 600 € di Google Ads;
  - prevendita di un "Pacchetto Analisi Tesi" a 79 €.

  **Avanti se:** almeno 20 prevendite con CAC ≤40 €, e almeno il 70% dei clienti pilota dà 8/10 a "ho capito la mia analisi". **Stop** con meno di 8 vendite o CAC oltre 80 €.

### 096 · Tutor AI per Analisi 1, Geometria e Fisica 1
**Punteggio 3,85** (con motivazione neutra: 3,45) · B2C, universitari · [dossier](dossier/095-096.md)

**Cos'è.** Prepara lo studente a un esame preciso, come Analisi 1 di un certo ateneo o la Fisica del semestre filtro di Medicina. Offre:
- esercizi nello stile del docente;
- correzione riga per riga, verificata da un motore di calcolo simbolico;
- un piano di studio fino all'appello.

- **Mercato.**
  - Italia: 150–200 mila studenti l'anno, tra circa 97 mila immatricolati STEM, circa 53 mila iscritti al semestre filtro e una parte di Economia.
  - Bocciature alte:
    - Geometria alla Sapienza: ammessi all'orale tra il 38% e il 61% al primo appello;
    - Fisica del semestre filtro: circa il 90% bocciato al primo appello.
  - Si paga già: ripetizioni a 19 €/h di media (25–40 €/h a Roma), Docsity a 15,99 €/mese.
- **Concorrenti.**
  - ChatGPT, modalità Studio (gratis).
  - Gemini, Guided Learning, più 12 mesi di Google AI Plus gratis per gli studenti di 18–24 anni (attivazione entro il 31/12/2026).
  - Photomath, Symbolab, Wolfram Alpha.
  - Thetawise (USA): dichiara 140 mila universitari, circa 20 $/mese, solo in inglese.
  - MathGPT.ai: vende agli atenei, oltre 50 istituzioni.
  - Docsity e Studocu (60 milioni di utenti al mese).
  - Il canale YouTube di Elia Bombardelli (581 mila iscritti, gratis).

  Nessuna app italiana ha trazione all'università.
- **Come fanno oggi.** Temi passati del docente, gruppi WhatsApp, YouTube, Docsity, ripetizioni e, sempre più spesso, ChatGPT o Gemini gratis.
- **Cosa fa in più di ChatGPT da 20 $/mese.** Va detto chiaramente: il 75–85% del valore è già gratis. Resta:
  1. **correttezza garantita:** ogni passaggio è verificato con un motore di calcolo simbolico (SymPy) più un controllo numerico. ChatGPT a volte sbaglia e lo studente non se ne accorge;
  2. **il primo errore nella soluzione scritta a mano:** lo studente fotografa il foglio e il tutor indica il primo passaggio sbagliato;
  3. **esercizi nello stile del proprio esame,** già organizzati, senza dover caricare 10 PDF;
  4. **simulazioni a tempo** con voto stimato e un piano giorno per giorno fino all'appello;
  5. **memoria del percorso:** mappa delle lacune e ripasso a intervalli crescenti.

  **Limite.** Vale per il calcolo, non per dimostrazioni e teoria. Pagano soprattutto i ripetenti a ridosso dell'appello: conviene un pass per sessione, non un abbonamento continuo.
- **Quanto pagherebbero.** 9,99 €/mese è plausibile; 14,99 € è difficile. Meglio un pass per sessione da 29–39 €.
- **Fatturato.**
  - Italia: realisticamente 50–100 k€ l'anno.
  - **300–500 k€:** solo con la nicchia del semestre filtro (esame nazionale, programma uguale per tutti, prezzo più alto), oppure portando il prodotto in Spagna, Francia e Germania, dove ogni Paese ha esami diversi.
- **Rischi.**
  - Diritto d'autore sui temi d'esame: usarli solo per lo stile.
  - Una correzione sbagliata diventa uno screenshot virale.
  - Uso durante gli esami online.
  - Google che regala Gemini agli studenti.
- **Acquirente e CAC.** Lo studente stesso. Canali: gruppi dei corsi, TikTok con "tema d'esame risolto", SEO su "temi esame analisi 1 [ateneo]". CAC di 60–100 € con la pubblicità contro un valore di 30–60 € per cliente: **funziona solo se almeno il 70% degli utenti arriva in modo organico.**
- **Come si costruisce.**
  - Generatore di esercizi parametrici.
  - Soluzioni di riferimento con SymPy e controllo numerico.
  - Foto della soluzione scritta a mano convertita in LaTeX con un modello di visione.
  - Verifica di equivalenza passo per passo.
  - Spiegazione dell'LLM vincolata al risultato del calcolo.
  - Livello dello studente stimato per argomento (BKT/IRT), più ripasso a intervalli crescenti.
  - Dati: temi pubblicati dagli atenei (solo per lo stile) e PDF caricati dall'utente.
  - Prodotto minimo: 6–8 settimane, meno di 3 k€.
- **Perché adesso.** Il semestre filtro ha creato un esame nazionale uniforme con bocciature di massa. Contro: ChatGPT e Gemini gratis. Finestra di 1–2 anni per una nicchia legata a un esame.
- **Cosa la ucciderebbe.**
  - "Gemini basta": meno del 2% paga.
  - Abbandono stagionale.
  - Costo di adattare i contenuti a ogni ateneo.
- **Test più economico** (al massimo 3 k€): prodotto minimo "Fisica semestre filtro" o "Analisi 1" per 3 atenei, lanciato a novembre 2026 per l'appello di gennaio 2027.
  - **Avanti se:** conversione ≥5%, almeno 100 paganti, CAC ≤20 €, almeno il 40% dice "meglio di ChatGPT", zero errori su 500 passaggi.
  - **Stop se:** conversione sotto il 2% o CAC oltre 40 €.

### 116 · Biostatistico AI per medici, specializzandi e ricercatori clinici
**Punteggio 3,75** (con motivazione neutra: 3,55; sopra soglia anche senza la tua motivazione) · professionisti e laboratori, mondo · [dossier](dossier/116-121.md)

**Cos'è.** Accompagna il ricercatore clinico dal piano di analisi fino alla risposta ai revisori.
- Sceglie i test e ne verifica le assunzioni.
- Calcola tutto in R: i numeri non li scrive mai l'LLM.
- Produce il materiale per la rivista: Table 1, curve di Kaplan-Meier, forest plot, checklist STROBE o CONSORT, sezione metodi e codice riproducibile.
- I dati restano nel browser, oppure in un ambiente in UE cancellato a fine sessione.

- **Mercato.**
  - Circa 1,5 milioni di articoli l'anno su PubMed.
  - 1,98 milioni di medici in UE, di cui 315.720 in Italia; 162.644 specializzandi negli USA.
  - In Italia circa 12.700 nuovi specializzandi l'anno.
  - Si paga già:
    - biostatistici universitari 70–345 $/h;
    - revisione statistica di Editage 200 $ a progetto;
    - Julius ha raccolto 10 M$.
- **Concorrenti.**
  - ChatGPT Plus: secondo uno studio JMIR del 2025, l'accuratezza dell'inferenza va dal 32,5% al 92,5% a seconda del prompt. I server in UE sono offerti solo ai piani Enterprise, Edu e API.
  - Julius AI: 20–60 $/mese, 10,5 M$ raccolti.
  - Intellectus Statistics: da 59,99 $.
  - EasyMedStat (Francia): prezzo su richiesta.
  - JASP e jamovi: gratuiti.
  - GraphPad Prism: 142–250 $/anno.
  - SPSS e Stata.
  - Elicit e Consensus: lavorano sulla letteratura, sono complementari.
  - Editage.
  - Biostatistici d'ateneo.
  - Strumenti per l'industria farmaceutica (Veristat InStat).
- **Come fanno oggi.**
  - Servizio di biostatistica dell'ateneo, con attese.
  - Statistici freelance.
  - SPSS o Prism da soli.
  - Sempre più spesso ChatGPT.
  - Coautorialità offerta allo statistico.
- **Cosa fa in più di ChatGPT da 20 $/mese.**
  1. **Un protocollo fisso invece del prompt.** Verifiche e analisi di sensibilità vengono fatte sempre. Con ChatGPT la qualità dipende da quanto è esperto chi scrive la domanda (32,5% contro 92,5%).
  2. **Riproducibilità.** Ogni numero dell'articolo è collegato al codice che lo ha prodotto, e il revisore può rieseguirlo.
  3. **Materiale pronto per la rivista.** Tabelle e figure standard, checklist compilate, sezione metodi con le versioni dei pacchetti, dichiarazione d'uso dell'AI secondo le regole ICMJE 2026.
  4. **Una privacy che regge davanti al responsabile della protezione dei dati.** R gira nel browser e al modello arrivano solo i nomi delle variabili e le statistiche aggregate.
  5. **Risposte ai revisori.** Dal commento si passa alla nuova analisi, al confronto con la precedente e alla bozza di risposta.

  **Critica.** Un esperto ottiene circa l'80% di questo con buoni prompt, e i generalisti possono colmare il distacco in 12–24 mesi.
- **Quanto pagherebbero.**
  - 49 €/mese o 390 €/anno.
  - "Pacchetto articolo" a 249 €.
  - Laboratorio a 199 €/mese per 5 utenti.

  Costa meno di un'ora di consulenza.
- **Fatturato.**
  - Ricavo netto di circa 33,5 € al mese per abbonato.
  - **400 k€:** circa 1.000 abbonati, oppure 1.900 pacchetti l'anno.
  - **1 M€:** circa 2.500 abbonati, lo 0,12% del bacino; probabilmente servono licenze per interi dipartimenti.
  - Margine lordo di circa l'83%.
  - Abbandono dell'8–12% al mese, perché il bisogno è legato a tesi, articoli e revisioni.
- **Rischi.**
  - GDPR, art. 9: i dati sono sanitari, e quelli pseudonimizzati restano dati personali. Serve un accordo sul trattamento.
  - EHDS: in futuro potrebbe servire una versione installabile negli ambienti sicuri.
  - Errori statistici: limite di responsabilità nel contratto, traccia di ogni operazione, test automatici, assicurazione.
  - Nessuna funzione deve orientare decisioni sul singolo paziente, per non diventare un dispositivo medico.
  - Da evitare: conservare i dataset, lasciar scrivere numeri all'LLM, promettere la pubblicazione.
- **Acquirente e CAC.**
  - Chi compra: specializzandi e dottorandi (pagano di tasca propria), ricercatori con fondi, responsabili di laboratorio.
  - Canali:
    - SEO tecnica ("Cox regression in R");
    - strumenti gratuiti, come un calcolatore della numerosità;
    - YouTube, LinkedIn, Reddit;
    - scuole di specializzazione.
  - CAC organico 30–80 €, a pagamento 150–400 €. Valore di un cliente circa 280 €, quindi **LTV/CAC 1,9–3,5.**
- **Come si costruisce.**
  - Dati nel browser (webR, Pyodide) oppure in un ambiente UE cancellato a fine sessione.
  - L'LLM vede solo il dizionario delle variabili e propone un piano di analisi, scelto da una libreria di metodi già validati.
  - R esegue i calcoli. I risultati chiave sono ricalcolati con Python, controllati per coerenza e testati su dataset con risultati noti.
  - Esportazione in Word o LaTeX, con lo script.
  - Metodi coperti: modelli lineari generalizzati, Cox, modelli misti, meta-analisi, potenza statistica.
  - Prodotto minimo: 8–12 settimane, 5–10 k€.
- **Perché adesso.**
  - Le raccomandazioni ICMJE 2026 chiedono di dichiarare l'uso dell'AI.
  - Gli LLM scrivono codice corretto se guidati bene.
  - La sovranità dei dati conta sempre di più, e c'è lo spazio europeo dei dati sanitari (EHDS).
  - Finestra di 12–24 mesi.
- **Cosa la ucciderebbe.**
  - Basta un'alternativa gratuita "abbastanza buona": conversione sotto il 2%.
  - I responsabili della protezione dei dati vietano il caricamento.
  - Abbandono oltre il 15% al mese con un CAC oltre 150 €.
- **Test più economico** (6 settimane, al massimo 4 k€):
  - pagina in italiano e inglese con tre offerte: 49 €/mese, pacchetto articolo a 249 €, risposta ai revisori a 149 €;
  - 10–20 clienti serviti a mano.

  **Avanti se:**
  - almeno 10 pagamenti da 99 € in su;
  - CAC ≤150 €;
  - al massimo 2 ore di lavoro per progetto;
  - almeno 4 clienti su 10 pronti ad abbonarsi.
- **Sinergia.** Usa lo stesso motore statistico della 107: un prodotto, due mercati (laureandi e medici).

### 093 · Tutor di matematica AI a voce per bambini di 6–13 anni
**Punteggio 3,70** (con motivazione neutra: 3,30) · B2C, genitori · [dossier](dossier/093-094.md)

**Cos'è.** Un tutor "solo matematica", sicuro per i minori:
- funziona a voce per i bambini di 6–8 anni;
- segue il programma italiano classe per classe;
- riconosce gli errori tipici;
- manda un report ai genitori.

- **Mercato.**
  - INVALSI 2026: circa 4 bambini su 10 della primaria sono sotto il livello base in matematica, e i risultati sono in calo.
  - Italia: circa 3,7 milioni di bambini di 6–13 anni, in calo del 3% l'anno. UE: circa 34 milioni.
  - Le famiglie pagano già le ripetizioni: 1 studente su 4, circa 400 € l'anno.
  - All'estero si pagano già app di matematica: Synthesis a 119 $/anno.
- **Concorrenti.**
  - Synthesis Tutor (USA): solo in inglese.
  - Khanmigo: in abbonamento solo negli USA.
  - Smartick (Spagna): 25–39 €/mese, adattivo, senza voce AI.
  - DragonBox / Kahoot! Kids: in italiano, ma non segue il programma italiano.
  - Redooc (Italia): medie e superiori, senza voce.
  - Photomath e Gauth: per ragazzi più grandi, danno la soluzione.
  - Skye di Third Space Learning (Regno Unito): **è già un tutor AI a voce per la primaria,** ma lo vende solo alle scuole, a 3.500 £ l'anno.
  - Sull'App Store italiano solo eserciziari.
- **Come fanno oggi.** Compiti con i genitori, ripetizioni (soprattutto dalle medie), eserciziari e app gratuite.
- **Cosa fa in più di ChatGPT da 20 $/mese.**
  1. **Un bambino di 7 anni non può usare ChatGPT da solo.** ChatGPT è vietato sotto i 13 anni, e in Italia sotto i 14 serve il consenso dei genitori (L. 132/2025). Questo è un servizio chiuso, solo matematica, senza chat libera e senza "amico AI", in linea con il KIDS Act.
  2. Voce pensata per chi non scrive ancora bene, con riconoscimento limitato a numeri e parole chiave.
  3. Percorso adattivo sul programma italiano.
  4. Diagnosi degli errori tipici (valore posizionale, prestito, frazioni), con le risposte verificate da un motore di calcolo e non dall'LLM.
  5. Report settimanale per il genitore: errori ricorrenti, tempo d'uso, un'attività da fare insieme senza schermo.

  Si paga per il progresso visibile e per la fiducia del genitore. Un grande lo può copiare in pochi mesi.
- **Quanto pagherebbero.** 9,99 €/mese o 69–89 €/anno per famiglia: "costa meno di un'ora di ripetizioni al mese".
- **Fatturato.**
  - **300–500 k€:** 3–5 mila famiglie paganti.
  - **1 M€:** circa 9.500 famiglie, lo 0,35% di quelle italiane con figli di 6–13 anni.
  - Il problema è economico, non operativo: con un CAC di 60–100 € il marketing costerebbe 0,5–0,9 M€ l'anno. Servono almeno metà di clienti organici e piani annuali, poi Spagna, Francia e Germania con il programma locale.
- **Rischi.**
  - Privacy dei minori: consenso sotto i 14 anni, nessuna impronta vocale, audio cancellato, valutazione d'impatto.
  - AI Act: niente vendita alle scuole all'inizio, niente riconoscimento delle emozioni.
  - Regole degli store per le app dei bambini.
  - Fughe di registrazioni.
- **Acquirente e CAC.** I genitori. Canali:
  - SEO con schede gratuite per classe;
  - maestre e mamme influencer;
  - Meta.

  CAC di 50–120 € contro un valore di 80–100 € per famiglia: il CAC deve restare sotto i 35–40 €.
- **Come si costruisce.**
  - Web app per tablet.
  - Riconoscimento vocale limitato a numeri e parole chiave, con alternativa touch.
  - Spiegazioni registrate in anticipo.
  - Motore di calcolo deterministico. L'LLM scrive solo suggerimenti e report, entro limiti fissati.
  - Grafo delle competenze, livello del bambino con BKT/IRT, catalogo degli errori tipici con distrattori diagnostici.
  - Contenuti: Indicazioni nazionali del Ministero e stile INVALSI.
  - Prodotto minimo (III–V primaria): 8–10 settimane, 5–15 k€, più 2–4 k€ per la privacy.
- **Perché adesso.**
  - INVALSI in calo.
  - KIDS Act e L. 132/2025.
  - La voce costa sempre meno.
  - Finestra di 12–24 mesi: Khanmigo è solo negli USA, Synthesis solo in inglese, Skye solo per le scuole britanniche.
- **Cosa la ucciderebbe.**
  - Le famiglie della primaria non pagano.
  - CAC oltre 80 € e abbandono oltre il 12% al mese.
  - Il riconoscimento vocale non capisce i bambini di 6–8 anni.
  - Google o Khan Academy lanciano in italiano.
- **Test più economico** (2–3 k€, 4–6 settimane):
  - **A:** landing page più 1,5 k€ su Meta, con pre-ordine "socio fondatore" a 49 €/anno. Costo per pre-ordine al massimo 40 €.
  - **B:** prototipo con 20 bambini per 3 settimane. Almeno il 50% lo usa 3 volte a settimana e almeno il 30% dei genitori paga.

### 109 · Matematica per lavorare con l'AI (adulti)
**Punteggio 3,65** (con motivazione neutra: 3,25) · B2C, adulti · [dossier](dossier/108-109.md)

Il punteggio era 3,80. È sceso dopo la verifica dei concorrenti, perché Math Academy fa già il percorso adattivo a 49 $/mese.

**Cos'è.** Un percorso strutturato sulla matematica del machine learning (algebra lineare, probabilità, ottimizzazione) per adulti che vogliono lavorare con l'AI. Offre:
- esercizi verificati da un motore di calcolo;
- progetti su dati reali;
- un portfolio e un attestato.

- **Mercato.**
  - Italia: 5–20 mila acquirenti l'anno (stima).
  - In inglese il mercato è mondiale, ma si compete con Brilliant, Coursera e DataCamp.
  - A favore: l'obiettivo UE di 20 milioni di specialisti ICT entro il 2030 e l'obbligo di alfabetizzazione AI dell'art. 4 dell'AI Act, che però spinge soprattutto la vendita alle aziende.
  - **Cautela:** i lavori che crescono sono applicativi (agenti, automazione), dove l'algebra lineare serve poco.
- **Concorrenti.**
  - **Math Academy** (USA, in inglese): è il concorrente più diretto.
    - Ha un corso "Mathematics for Machine Learning", adattivo, con padronanza e ripasso a intervalli.
    - Prezzo di lancio 49 $/mese; prezzo pieno annunciato 79–99 $/mese.
  - Brilliant: tra 150 e 240 $/anno, in inglese.
  - Coursera, "Mathematics for Machine Learning" dell'Imperial College: 234–276 mila iscritti. Esiste anche il corso di DeepLearning.AI. Coursera Plus costa circa 59 $/mese.
  - DataCamp.
  - Khan Academy (gratis).
  - 3Blue1Brown (gratis).
  - Udemy (10–20 €).
  - Bootcamp italiani (start2impact, EPICODE, Develhope, Boolean, Talent Garden): migliaia di euro, focus sullo sviluppo software.
  - Corsi gratuiti di Federica e POK.
  - ChatGPT, Gemini e Claude come tutor.
- **Come fanno oggi.** Usano 3Blue1Brown, i corsi Coursera in inglese, il libro gratuito "Mathematics for Machine Learning" e ChatGPT. Spesso saltano la matematica e passano agli strumenti.
- **Cosa fa in più di ChatGPT da 20 $/mese.** **È la risposta più debole della lista.** ChatGPT e Gemini fanno già da tutor socratico, verificano i calcoli con SymPy e generano esercizi. Il percorso strutturato con verifica della padronanza lo vende già Math Academy. Restano:
  - **la lingua:** italiano e altre lingue UE, contro concorrenti solo in inglese;
  - **un tutor AI con cui parlare,** vincolato al calcolo simbolico (Math Academy non ce l'ha);
  - **visualizzazioni interattive di qualità,** animazioni in stile 3Blue1Brown che una chat non produce;
  - **progetti su dati reali** corretti in automatico, con portfolio e attestato;
  - **un piano** che tiene costante lo studio.

  Si vende disciplina e design, non una capacità nuova. Un abbonamento si giustifica solo legandolo a un traguardo concreto, come l'ammissione a un master o un colloquio tecnico.
- **Quanto pagherebbero.** 9,99–14,99 €/mese o 99–129 €/anno; 149–249 € se il percorso è legato a un traguardo.
- **Fatturato.**
  - Solo in italiano: 100–300 k€.
  - **300–500 k€:** in inglese, contro Brilliant e Coursera, oppure vendendo alle aziende per l'alfabetizzazione AI.
  - 1 M€: circa 5.100 abbonati attivi a 19,99 €.
- **Rischi.** Legali bassi: trasparenza (art. 50) e nessuna promessa di lavoro, per non rischiare con l'Antitrust. Il vero rischio è che l'AI gratuita renda il prodotto una commodity.
- **Acquirente e CAC.** Persone di 25–40 anni con lauree non informatiche. Canali: LinkedIn, YouTube, TikTok, newsletter. CAC di 40–150 €, LTV/CAC 1–3. **L'unica leva credibile sei tu come creator:** un matematico e ingegnere AI che pubblica contenuti.
- **Come si costruisce.**
  - Grafo delle competenze.
  - Esercizi parametrici verificati con SymPy e NumPy.
  - Tutor LLM obbligato a controllare ogni passaggio con il calcolo simbolico.
  - Animazioni con Manim e grafici con D3.
  - Python nel browser (Pyodide).
  - Livello dello studente con BKT, ripasso con FSRS.
  - Dati aperti: Istat, Eurostat, OpenML.
  - 6–8 progetti, per esempio una PCA su dati Istat o una rete neurale da zero.
  - Prodotto minimo: un modulo "Algebra lineare per il ML" in 6–10 settimane, con 2–5 k€.
- **Perché adesso.** Paura dell'AI, corsa alla riconversione, art. 4 dell'AI Act. Finestra di 6–12 mesi, solo per una nicchia legata a un traguardo.
- **Cosa la ucciderebbe.**
  - Il tutor gratuito basta.
  - Il mercato del lavoro non premia la matematica.
  - CAC troppo alto.
- **Test più economico** (4 settimane, circa 2 k€):
  - 20 interviste;
  - una landing page con 3 lezioni gratis e un'offerta "socio fondatore" a 99 €/anno;
  - una pagina di controllo "Costruisci agenti AI".

  **Avanti se:** almeno 25 paganti (≥3%) e almeno il 30% degli intervistati indica la matematica come ostacolo. **Se la pagina sugli agenti converte il doppio, conviene cambiare direzione.**
- **Nota sulla ricerca.** La prima ricerca non aveva potuto fare verifiche web. I concorrenti principali (Math Academy, Brilliant, Coursera) sono stati verificati dopo: vedi la sezione aggiunta in fondo al dossier.

### 092 · Allenatore AI dell'esame orale
**Punteggio 3,65** (con motivazione neutra: 3,25) · B2C, maturandi e universitari · [dossier](dossier/092-107.md)

**Cos'è.** Un simulatore dell'esame orale, a voce. Parte dalla maturità, con le 4 materie note da gennaio, poi gli orali universitari e il Grand Oral francese. Offre:
- voto su griglia;
- copertura del programma;
- misure sull'esposizione;
- un piano fino all'esame.

- **Mercato.**
  - Italia: 527.747 maturandi nel 2026 e 2,05 milioni di universitari. Il 54% dei maturandi indica il colloquio come la prova più temuta.
  - UE: 19 milioni di universitari; il Grand Oral francese riguarda circa 533 mila candidati.
  - Le prove che i consumatori pagano sono deboli: StudierAI ha circa 214 abbonamenti. Le ripetizioni per la maturità arrivano a 540 €.
- **Concorrenti.**
  - Italia:
    - StudierAI: interrogazione a voce con voto, circa 214 abbonamenti;
    - Kiwi AI: 9,99 €/mese, l'orale a voce non è confermato;
    - MaturAI: sperimentale.
  - Estero:
    - JuryAI: Grand Oral, una sola persona;
    - StudyVoice: circa 570 download;
    - Trainexus, ExamSim e Voralio: strumenti per atenei.
  - Grandi:
    - ChatGPT con modalità Studio e voce, gratis;
    - Gemini, gratis per gli studenti;
    - Knowunity (20 milioni di utenti, 45 M€ raccolti), che può aggiungere l'orale in pochi mesi;
    - Studocu, Quizlet, Yoodli (quest'ultimo vende alle aziende).
- **Come fanno oggi.** Ripetono ad alta voce con genitori e compagni. 3 maturandi su 4 usano l'AI, il 47% ogni giorno, e il 61% di chi la usa abitualmente prepara così interrogazioni e verifiche.
- **Cosa fa in più di ChatGPT da 20 $/mese.** Di difendibile, poco: "interrogami su questo PDF" con la voce di ChatGPT funziona già. Si aggiunge:
  1. il formato reale dell'esame: 4 materie, 4 commissari, i tempi, esaminatore gentile o severo;
  2. un voto su griglia, calibrato su risposte già valutate da docenti e coerente tra una sessione e l'altra;
  3. la copertura del programma misurata nel tempo;
  4. misure sull'esposizione (velocità, intercalari, pause). Con la riforma chi resta in silenzio all'orale viene bocciato;
  5. un piano giorno per giorno e lo storico dei progressi.

  Un buon prompt ne copre metà. Si vende comodità e specificità nelle 2–4 settimane prima dell'esame: **pass, non abbonamento.**
- **Quanto pagherebbero.**
  - "Pass Maturità" a 29–39 € una tantum, spesso pagato dai genitori.
  - "Pass Sessione" per gli universitari a 12,99–14,99 € per 30 giorni.
- **Fatturato.**
  - Circa 30 € netti per pagante l'anno.
  - Italia: tetto di 150–400 k€.
  - **300–500 k€:** 10–17 mila paganti.
  - **1 M€:** circa 33 mila paganti, servono Francia, Germania e Spagna.
  - La voce costa 0,02–0,05 $/min; margine lordo del 55–80%.
- **Rischi.**
  - AI Act: vietato riconoscere le emozioni negli istituti di istruzione; niente vendita alle scuole prima di essere conformi; l'audio sintetico va marcato.
  - Consenso dei genitori sotto i 14 anni.
  - Pacchetti senza rinnovo automatico.
- **Acquirente e CAC.**
  - Maturandi (per i minorenni pagano i genitori) e universitari prima dell'orale.
  - Canali: TikTok con video "l'AI mi interroga", ScuolaZoo e Skuola.net, SEO su "domande orale [materia] 2027".
  - CAC di 25–100 € con la pubblicità: non funziona. Con canali organici 5–10 €, LTV/CAC 2–5.
- **Come si costruisce.**
  - Appunti, PDF e slide letti con OCR e trasformati in una mappa di argomenti, con una banca di domande e griglie di valutazione.
  - Voce in tempo reale con un modello "mini", oppure la catena trascrizione → LLM → sintesi vocale.
  - Un LLM valuta con la griglia, calibrato su 100–200 risposte valutate da docenti (obiettivo di accordo con i docenti: kappa ≥0,7).
  - Livello per argomento con un modello bayesiano o IRT.
  - Misure ricavate dalla trascrizione.
  - Prodotto minimo: 4–6 settimane, 2–5 k€.
- **Perché adesso.**
  - Riforma della maturità (L. 164/2025).
  - Ritorno degli orali contro i compiti fatti con l'AI: Danimarca, Praga, Cornell, Penn, NYU.
  - La voce costa ormai pochissimo.
  - Finestra di 12–24 mesi.
- **Cosa la ucciderebbe.**
  - Basta ChatGPT con la voce.
  - Un acquisto da circa 30 € con un CAC più alto.
  - Il costo della voce.
- **Test più economico** (sessione di gennaio–febbraio 2027, 1.500 € di creator e pubblicità):
  - web app su 3 esami orali molto frequentati, con un pass a 14,99 €;
  - **Avanti se:** almeno il 4% compra (almeno 40 clienti), CAC ≤12 €, costo della voce ≤2 € per cliente.
  - **Stop se:** compra meno del 2% o il CAC supera 25 €.
- **Sinergia.** Con la 107: "analisi della tesi più allenamento alla discussione" in un unico prodotto.

### 127 · Preparazione AI agli esami attuariali (solo P e FM)
**Punteggio 3,60** (con motivazione neutra: 3,40) · B2C professionale, mondo in inglese · [dossier](dossier/122-127.md)

**Cos'è.** Prepara gli aspiranti attuari agli esami P (probabilità) e FM (matematica finanziaria) della SOA e del CAS. Offre:
- domande illimitate, generate e verificate da un motore di calcolo;
- simulazioni d'esame a tempo;
- una stima della probabilità di superare l'esame;
- un piano di studio fino all'esame.

**Il filtro "morte".** Gli esami "vita" (FAM, ALTAM, CM1 dell'IFoA) trattano tavole di mortalità, quindi li escludo. Restano P, FM e gli esami finanziari, che sono anche quelli con più candidati.

- **Mercato.**
  - Circa 24.000 prove l'anno tra P e FM. Tra SOA, CAS e IFoA si arriva a 70–90 mila prove, cioè 40–60 mila candidati.
  - Supera circa il 45% al primo colpo.
  - Si spendono 200–500 $ per esame, spesso rimborsati dal datore di lavoro.
  - Il mercato vale 15–45 M$ l'anno e cresce del 2–4%.
  - Negli USA il salario mediano di un attuario è di 125.770 $, e l'occupazione è prevista in crescita del 22% in 10 anni.
- **Concorrenti.**
  - Coaching Actuaries: il leader.
    - Il suo motore adattivo stima il punteggio ("Earned Level") e ha anni di dati.
    - Circa 200 $ a esame, 300–500 $ con le lezioni.
  - The Infinite Actuary: video gratuiti per P e FM.
  - FreeFellow: 39.000 domande gratis, piano a pagamento da 39 $/mese.
  - ACTEX, ASM, Mahler, ActEd (per l'IFoA), AnalystPrep.
  - Domande d'esempio ufficiali e Reddit.
  - ChatGPT.
- **Come fanno oggi.** Circa 300 ore di studio per esame. Comprano Coaching Actuaries o un manuale, spesso rimborsati dal datore di lavoro, e usano le domande ufficiali e i gruppi di studio.
- **Cosa fa in più di ChatGPT da 20 $/mese.** ChatGPT spiega e risolve gran parte degli esercizi di P e FM. Non dà:
  - una banca di domande calibrata sull'esame vero (difficoltà, formato, pesi del programma);
  - soluzioni garantite, ricalcolate con un secondo metodo indipendente;
  - **una probabilità di superamento calibrata sugli esiti reali** (es. "62% ± 8"), che è la cosa per cui si paga;
  - la simulazione d'esame al computer;
  - una fattura che il datore di lavoro rimborsa.

  **Critica.** Coaching Actuaries offre già quasi tutto questo, e TIA e FreeFellow coprono P e FM gratis. Lo spazio vero è stretto:
  - prezzo più basso;
  - domande infinite e verificate;
  - un tutor AI con cui parlare, che il leader non ha.
- **Modelli del 2027 e architettura AI** (la tua nuova indicazione).
  - Con i modelli del 2027 generare e verificare domande costerà quasi zero, e ChatGPT risolverà P e FM quasi senza errori. Resta difendibile solo la **calibrazione sugli esiti reali**: un modello IRT bayesiano aggiornato con i risultati dichiarati da migliaia di candidati. È un ciclo di dati che migliora con l'uso e che un chatbot generalista non ha.
  - Né RAG né fine-tuning servono davvero. La vera architettura sono il motore di verifica e i dati di calibrazione.
  - Il leader ha questi dati da anni: il vantaggio si costruisce solo nel tempo.
- **Quanto pagherebbero.** 129 $ a esame, in alternativa 29–39 $/mese. Per i datori di lavoro 100–150 $ a posto.
- **Fatturato.**
  - Circa 97 € netti per pacchetto, venduto dal sito con un Merchant of Record.
  - Servono:

    | Obiettivo | Pacchetti l'anno | Quota delle prove di P e FM |
    |---|---|---|
    | 300 k€ | circa 3.100 | 13% |
    | 1 M€ | circa 10.300 | 43% |

  - Scenario: 29–58 k€ il primo anno, 240–340 k€ il terzo, aggiungendo esami e clienti aziendali.
  - **Verdetto dell'analista: 300 k€ possibile ma non probabile; 1 M€ improbabile da solo.**
  - Margine lordo 85–95%.
- **Rischi.**
  - Diritto d'autore sulle domande ufficiali: niente copie né domande "ricordate".
  - Marchi SOA e CAS: indicare sempre "non affiliato".
  - AI Act: rischio solo se si vende a università o a programmi aziendali.
  - Comunità piccola e molto attiva su Reddit: un lancio con errori brucia il marchio.
  - I programmi d'esame cambiano.
- **Acquirente e CAC.**
  - Chi compra: universitari di 19–24 anni e giovani analisti. Spesso paga il datore di lavoro.
  - Canali: Reddit r/actuary, Discord, club attuariali universitari, YouTube, SEO.
  - CAC di 20–40 € con canali organici, 50–120 € con la pubblicità. LTV di circa 175 €, quindi **LTV/CAC 1,5–8,7.**
- **Come si costruisce.**
  - Domande descritte in JSON, con i parametri e il programma di soluzione.
  - L'LLM scrive il testo e le risposte sbagliate plausibili.
  - SymPy, SciPy e NumPy calcolano la risposta; un secondo metodo (formula alternativa o Monte Carlo) la verifica.
  - Un revisore attuario controlla a campione il 5–10%.
  - Abilità dello studente stimata con IRT bayesiano; ripasso con FSRS.
  - Prodotto minimo (solo Exam P): 800–1.000 domande verificate e 3 simulazioni, in 6–10 settimane, con 5–10 k€ (compreso un revisore ASA/FSA).
- **Perché adesso.**
  - Generare e verificare esercizi costa poco.
  - Il CAS ha aumentato le sessioni d'esame.
  - I candidati all'Exam P crescono del 3,3%.
  - Finestra di 12–24 mesi, finché Coaching Actuaries non lancia un tutor AI.
- **Cosa la ucciderebbe.**
  - Il gratuito basta.
  - Il leader è rimborsato dal datore di lavoro, quindi il prezzo più basso non conta.
  - Errori nelle domande.
- **Test più economico** (8 settimane, al massimo 6.000 €): diagnostica gratuita dell'Exam P più un pacchetto in pre-ordine a 79 $, lanciati prima della sessione di gennaio 2027.

  **Avanti se:**
  - almeno 400 diagnostiche completate;
  - almeno il 5% (almeno 20 persone) paga;
  - CAC ≤40 $;
  - errori nelle domande ≤1%.

### 113 · Revenue manager AI per club di padel
**Punteggio 3,55** (con motivazione neutra: 3,35) · B2B, club · [dossier](dossier/113-115.md)

**Cos'è.** Un software che lavora ogni giorno sui dati del club.
- Legge le prenotazioni, tramite le API di Playtomic o i file esportati.
- Prevede la domanda per fascia oraria.
- Suggerisce prezzi e sconti per le fasce vuote.
- Manda offerte su WhatsApp ai giocatori che hanno dato il consenso.
- Misura, con un gruppo di controllo, quanto ha recuperato.

- **Mercato.**
  - Mondo, a fine 2025: oltre 20.900 club, 58.300 campi e 19,4 milioni di giocatori. L'Europa ha circa il 66% dei campi.
  - Italia: 3.716 club e circa 10.200 campi. Spagna: 4.500 club.
  - Svezia: crollo, con 90 fallimenti nel 2023.
  - Un campo costa €38–40 l'ora in Italia. Un punto di occupazione in più vale circa €5.800 l'anno per un club italiano medio (stima).
  - Si paga già: CourtReserve da $150/mese, 1club da $63/mese, Boosterpadel solo a risultato.
- **Concorrenti.**
  - Playtomic:
    - circa 6.000 club, 1,5 milioni di giocatori attivi al mese, €65 M raccolti;
    - i prezzi si impostano a regole manuali;
    - API in sola lettura, solo nei piani più cari.
  - MATCHi: oltre 3.000 club, Nord Europa.
  - Boosterpadel.ai: è la stessa idea, pagata solo a risultato.
  - Anolla: prezzi dinamici con il meteo, ma è un gestionale completo; esiste anche in italiano.
  - 1club.ai: prezzi dinamici nelle ore morte.
  - Anybuddy (Francia), CourtReserve, Wakesys, anny.
  - ChatGPT su un file esportato.
- **Come fanno oggi.** Prezzi fissati a mano per giorno e ora, sconti manuali, messaggi nei gruppi WhatsApp. Nessuno prevede la domanda né misura i ricavi persi.
- **Cosa fa in più di ChatGPT da 20 $/mese.** **È la risposta più solida della lista.** ChatGPT non può:
  - leggere ogni giorno le prenotazioni;
  - conoscere come si riempiono le fasce in base all'anticipo;
  - mandare offerte ai giocatori;
  - misurare con un gruppo di controllo quanto ha recuperato.

  Il rivale vero non è ChatGPT ma Playtomic, che ha i dati e la distribuzione. Esistono già collegamenti non ufficiali tra ChatGPT e Playtomic: il vantaggio si riduce in 2–3 anni.
- **Quanto pagherebbero.** €49–149/mese, oppure il 10–20% dei ricavi recuperati e misurati. Con 2–3 punti di occupazione in più (€12–17k l'anno) il ritorno è circa 10 volte il costo.
- **Fatturato.**
  - Ricavo medio di €104/mese per club.
  - **300 k€:** 240 club.
  - **500 k€:** circa 400 club. In Italia sarebbero l'11%: servono 3–4 Paesi.
  - **1 M€:** circa 800 club.
  - Vincolo: l'API di Playtomic è solo nei piani più cari.
  - Abbandono circa 3% al mese; margine 80–90%.
- **Rischi.**
  - GDPR: si scrive solo a chi ha dato il consenso.
  - I prezzi personalizzati vanno dichiarati (direttiva Omnibus).
  - Playtomic può copiare la funzione o negare la partnership.
  - I rincari nelle ore di punta possono sembrare speculazione: meglio partire solo con sconti.
  - Da evitare: scraping e API non ufficiali.
- **Acquirente e CAC.**
  - Chi compra: titolari di club indipendenti con 2–8 campi e piccole catene.
  - Canali:
    - visite ai club con un audit gratuito dei ricavi persi;
    - Playtomic Connect, il programma partner;
    - integrazione nei gestionali che non hanno prezzi dinamici.
  - CAC €300–800, quasi tutto tempo. LTV circa €2.950, quindi **LTV/CAC 4–10.**
  - Il collo di bottiglia sono le tue ore di vendita e di avvio.
- **Come si costruisce.**
  - Connettori verso Playtomic e verso i file esportati.
  - Previsione per fascia oraria: modello bayesiano gerarchico o gradient boosting, con la curva di riempimento.
  - Elasticità al prezzo stimata con esperimenti controllati (Thompson sampling), con variazioni entro ±15–20%.
  - Abbinamento dei giocatori per livello.
  - Report settimanale con 3–5 azioni concrete.
  - Prodotto minimo: 6–8 settimane, €2–6k.
- **Perché adesso.**
  - In Spagna, Italia e Svezia si passa dal costruire club all'ottimizzarli.
  - Nel mondo si aggiungono 8.000 campi l'anno.
  - Playtomic ha aperto API e un programma partner.
  - Nei campi coperti l'energia pesa.
  - Finestra di 12–24 mesi.
- **Cosa la ucciderebbe.**
  - Playtomic integra i prezzi dinamici o rifiuta la partnership.
  - Nessun aumento misurabile.
  - Vendere e avviare i club richiede più di 10 ore a settimana.
- **Test più economico** (5–6 settimane, al massimo €1.500):
  - candidatura a Playtomic Connect;
  - audit gratuito per 15 club, 10 in Italia e 5 in Spagna;
  - pilota manuale di 4 settimane, con metà delle fasce come gruppo di controllo.

  **Avanti se:**
  - almeno 4 punti di occupazione in più, oppure almeno €400/mese per club;
  - almeno 3 club firmano a €99/mese;
  - al massimo 1,5 ore per club a settimana.

## Scartati
24 candidati restano sotto soglia: l'elenco con i motivi è in [scartate.md](scartate.md). Quello che insegnano gli scarti:
- **"Lo fa già ChatGPT"** è il motivo più frequente.
- **Coaching per i consumatori:** abbandono troppo alto.
- **B2B con obblighi morbidi:** le PMI rimandano.
- **Prodotti in cui chi usa non è chi paga:** serve convincere due persone.

## Nuovo in lista: 208 · OMBRA, la "TAC" degli impianti fotovoltaici (14/10/2026)

**Punteggio dopo la ricerca completa:** 3,80; con motivazione neutra 3,40.

**Cosa fa.** Dai dati dell'inverter e dal sole misurato dai satelliti ricostruisce, come una TAC, dove sta l'ostacolo che fa ombra. Poi divide le perdite per causa e le esprime in euro con la tariffa reale dell'impianto.

**Primo cliente:** gli impianti in Conto Energia da 100 kWp a 1 MWp (circa 20–25 mila impianti in Italia, ~10–12 GW). Per loro ogni kWh perso vale 0,35–0,55 €.

**Test:** sotto i 10 k€.

**Scheda completa:** [208-ombra.md](208-ombra.md). Dossier: [208-tecnologia](dossier/208-tecnologia.md), [208-clienti](dossier/208-clienti.md).

## In valutazione: 153 · Gioco di società AI per serate tra amici
**Punteggio 3,35 con motivazione 4 (mia stima); 3,55 con motivazione 5, cioè entra in lista al limite.** Con motivazione neutra vale 3,15.
- **Clienti:** consumatori; paga solo chi ospita.
- **Primo pubblico:** i pre-serata Erasmus.
- **Dossier:**
  - [mercato e concorrenti](dossier/153-mercato.md);
  - [prodotto, rischi e test](dossier/153-prodotto.md).

**Cos'è.** Una web app senza installazione: chi ospita mostra un QR e tutti entrano dal telefono. L'AI crea giochi su misura per i presenti e fa da presentatore:
- indovinelli costruiti su ciò che ognuno scrive in privato;
- impostore multilingue;
- "chi è più probabile che…";
- battuta migliore.

Ognuno legge nella sua lingua.

- **Mercato.**
  - Erasmus+ nel 2024: circa 1,44–1,5 milioni di partecipanti (tutti i settori), di cui circa 350–450 mila universitari (stima). L'ESN ha 512 sezioni in 44 Paesi e segue circa 350 mila studenti.
  - In UE ci sono 1,76 milioni di studenti stranieri e 18,8 milioni di universitari.
  - La Gen Z vuole vedersi dal vivo, fa feste in casa e beve meno.
  - Ma nel 2025 la spesa nei party game su mobile è scesa del 16,2% (AppMagic).
  - **Gli Erasmus da soli valgono al massimo 20–80 k€ l'anno: sono il laboratorio, non il mercato.**
- **Concorrenti.**
  - **App affermate:**
    - Picolo: 7,7 milioni di download, circa 50 $/anno;
    - Undercover: 6,1 milioni di installazioni su iOS;
    - Heads Up!: 70 milioni di download;
    - Jackbox: il formato schermo, telefoni e codice stanza;
    - Kahoot, Gartic Phone, Among Us.
  - **Grandi piattaforme:**
    - Netflix offre giochi sulla TV con il telefono come controller, gratis per gli abbonati;
    - Meta AI è già dentro i gruppi WhatsApp.
  - **Nuove app con AI (2025–2026), almeno 5:**
    - Inside Joke Battle Arena fa già "chi è più probabile che…" sui presenti, con codice stanza;
    - Whisper Games ha un presentatore AI a voce;
    - Little Umbrella ("Death by AI") ha avuto 20 milioni di giocatori in 3 mesi, ma online.
  - Nessuna mette insieme tutto: gruppi da 8–20, più lingue, presentatore, domande sui presenti, ingresso con QR. Ogni pezzo però è copiabile in poche settimane.
- **Come fanno oggi.**
  - Giochi fisici con l'alcol: beer pong, King's Cup, "Non ho mai".
  - App su un telefono che passa di mano: Picolo, Undercover.
  - L'"impostore" di TikTok, giocato senza app.
  - Musica.

  I problemi: lingue diverse, persone che non si conoscono, chi non beve resta escluso, contenuti ripetitivi.
- **Cosa fa in più di ChatGPT da 20 $/mese.**
  - ChatGPT ha ritirato le chat di gruppo il 9/7/2026, e la sua voce serve un utente alla volta.
  - Il gioco ha ciò che una chat non può avere:
    - segreti e voti anonimi su ogni telefono;
    - risposte contemporanee, regole, tempi e punteggi;
    - la lingua di ciascuno;
    - contenuti presi da ciò che ognuno scrive in privato.
  - **Però chi ospita non lo confronta con ChatGPT a 20 $, ma con il gratis:** Netflix, Meta AI, i giochi a dita puntate.
  - Un abbonamento mensile ha senso solo per chi ospita almeno 2 volte al mese. Per gli Erasmus sono meglio un pass serata o un pass semestre.
- **Quanto pagherebbero.**
  - Riferimenti:
    - Picolo: circa 50 $/anno;
    - Drinktivity: 2,99 $/settimana;
    - Drink and Tell: 5,99 $/mese;
    - Jackbox: 25–30 $ una tantum;
    - Kahoot per i bar: 19–59 $/mese.
  - Plausibile: pass serata a 1,99 €, pass semestre a 9,99 €, abbonamento a 3,99 €/mese. Paga solo chi ospita: in un gruppo di 12 sono 0,17 € a testa.
- **Fatturato.**
  - Costo dell'AI per serata: 0,22 € nella versione essenziale, 0,85 € nella standard.
  - Paganti necessari:

    | Obiettivo | Modello | Ospiti paganti l'anno |
    |---|---|---|
    | 300 k€ | Abbonamento settimanale da 4,99 €, tenuto 3 settimane | circa 29.000 |
    | 300 k€ | Annuale da 29,99 € sul web | circa 12.600 |
    | 1 M€ | Abbonamento settimanale | circa 96.000 |
    | 1 M€ | Locali a 99 €/mese | circa 860 locali |

  - La pubblicità non rientra (LTV/CAC 0,04–0,29). **Serve un fattore virale K di almeno 0,4–0,5.**
  - Probabilità stimata dall'analista: 300–500 k€ al 5–10%, 1 M€ all'1–3%.
  - **Strada B2B:** un presentatore AI di quiz per locali, ostelli e scambi linguistici. I bar pagano già 25–250 $/mese per un software, oppure 300–400 $ a serata per un presentatore umano.
- **Rischi e cosa fare.**
  - **Essere visto come gioco alcolico.** Per Apple è una categoria satura (linee guida 4.3 e 1.4.3), e TikTok non spinge i video con alcol. Va presentato come gioco di società, non alcolico.
  - **Umiliazioni e bullismo.** Ognuno scrive solo di sé. Il livello "piccante" si sceglie in privato, e vale il più basso del gruppo.
  - **Minori.** Contenuti piccanti solo per maggiorenni verificati: c'è il precedente del Garante contro Replika (5 M€).
  - **GDPR.** Dati degli amici e memoria del gruppo: cancellazione automatica salvo consenso.
  - **AI Act, art. 50 (dal 2/8/2026).** Dichiarare che il presentatore è un'AI e marcare audio e immagini.
  - **Marchi.** Niente nomi come Quiplash, Codenames o "Undercover".
- **Acquirente e CAC.**
  - Decide chi ospita, o l'"animatore" del gruppo.
  - Canali:
    - il QR dentro il gioco ("ospita tu la prossima, la prima è gratis");
    - clip automatiche per TikTok e Reels;
    - ESN e welcome week, come canale e non come cliente;
    - ambasciatori nelle residenze.
  - CAC per pagante: 0,4–2,2 € con il ciclo dentro il gioco, 25–184 € con la pubblicità.
- **Come si costruisce.**
  - Web app con QR, senza store all'inizio.
  - Server di stanza in tempo reale (WebSocket).
  - Contenuti generati in anticipo, per non far aspettare i giocatori.
  - Voce solo dallo schermo condiviso; le risposte arrivano dai telefoni.
  - Modelli economici per il gioco gratuito: circa 0,06 € a serata.
  - Moderazione su tre livelli.
  - I voti "😂" dei giocatori insegnano cosa fa ridere: un ciclo di dati proprio.
  - Prodotto minimo per il test: 2–3 settimane, meno di 1.000 €. Versione pubblica: 6–8 settimane, meno di 5.000 €.
- **Perché adesso.**
  - LLM e voce costano centesimi.
  - La traduzione in tempo reale è ormai normale.
  - La Gen Z vuole vedersi dal vivo.
  - Per Erasmus+ 2028–2034 è proposto il 56% di budget in più.
  - Finestra di 12–24 mesi.
- **Modelli del 2027 e architettura AI.**
  - **Più facile:** presentatore vocale multilingue, immagini per i giochi di disegno, commenti dell'AI alle risposte.
  - **Minacce:**
    - Meta, con l'AI già nei gruppi WhatsApp;
    - Netflix, con il formato TV più telefono gratis;
    - OpenAI, che sta valutando "funzioni collaborative".
  - **Vantaggi possibili:**
    - la memoria del gruppo, ma limitata dal GDPR;
    - un presentatore addestrato sui voti dei giocatori, ma servono centinaia di migliaia di voti;
    - game design e comunità.
  - **Difendibilità 2 su 5:** l'architettura AI migliora il prodotto più di quanto lo protegga.
- **Cosa la ucciderebbe.**
  - L'effetto novità: si gioca una sera e basta.
  - Il pre-serata non è il momento giusto: si arriva a orari diversi, c'è musica, si parla.
  - Nessuno diventa a sua volta ospite, oppure un incidente di contenuti.

**Modello di prezzo proposto da Lorenzo (14/10/2026).** Gratis, con un abbonamento a 1,99 €/mese che sblocca:
- più di 6 giocatori;
- le traduzioni nelle altre lingue;
- la versione "extra hot";
- altre funzioni da definire.

La scommessa: l'abbonamento costa poco, quindi non si disdice.

| | Calcolo (stima) | Netto al mese |
|---|---|---|
| 1,99 € con IVA al 22% | 1,63 € | — |
| Store al 15% | — | 1,39 € |
| Store Apple al 10% (piccoli sviluppatori UE dal 1/10/2026) | — | 1,47 € |
| Web con Stripe (1,5% + 0,25 €) | — | 1,35 € |

**Abbonati attivi in media, con un netto di 1,39 € al mese:**

| Obiettivo | Abbonati attivi |
|---|---|
| 300 k€ | circa 18.000 |
| 500 k€ | circa 30.000 |
| 1 M€ | circa 60.000 |

**Nuovi abbonati necessari ogni anno per tenerne 18.000:**

| Abbandono mensile | Valore di un cliente | Nuovi abbonati l'anno |
|---|---|---|
| 5% | circa 28 € | circa 10.800 |
| 10% | circa 14 € | circa 21.600 |

**Vincolo.** Il costo AI per abbonato deve restare sotto 0,40 €/mese: modelli economici e un tetto di uso.

**Test con i tuoi gruppi Erasmus** (3–4 settimane, 12–20 serate, meno di 1.000 €)
- Il momento è ideale: il semestre è appena iniziato.
- In un terzo delle serate ci sei tu a osservare; negli altri due terzi dai solo il link a chi ospita.
- Soglie fissate prima:

| Metrica | Avanti se | Stop se |
|---|---|---|
| Durata della partita (mediana) | ≥ 40 min | < 20 min |
| Giochi per serata | ≥ 3 | ≤ 1 |
| **Gruppi che rigiocano entro 14 giorni, senza solleciti** | **≥ 40%** | **< 15%** |
| **Giocatori che lanciano una partita da soli entro 21 giorni** | **≥ 5%** | **< 1,5%** |
| NPS dei giocatori | ≥ 50 | < 20 |
| Ospiti che pagano davvero (pass da 1,99 € o 3,99 €/mese) | ≥ 20% | < 5% |
| Clip pubblicate | ≥ 1 ogni 4 serate | 0 |
| Incidenti gravi di contenuto | 0 | ≥ 1 non risolvibile |

**Regola.** Si va avanti con almeno 5 soglie su 8, comprese le due in grassetto. Ci si ferma se anche una sola delle due in grassetto è in zona stop.

## Ricerche interrotte
I candidati 123, 124, 126, 136, 138, 140, 146 e 148 non ti interessavano. Le ricerche sono state fermate e non sono in lista.
