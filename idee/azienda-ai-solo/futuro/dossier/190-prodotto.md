# 190 — Casa editrice senza dipendenti: prodotto, qualità, costi, canali, architettura, test

> Rapporto di ricerca del 14/10/2026 (agente di ricerca, verificato a campione da Claude). Le voci [NV] non sono verificate con una fonte; "stima" indica un calcolo.

# IDEA 190: "Casa editrice senza dipendenti" (saggistica scientifica tradotta con l'AI)
### Report di ricerca: prodotto, qualità, costi, canali, architettura, test

*Data: 14 ottobre 2026. Ho fatto 35 ricerche web; WebFetch non era disponibile, quindi ho letto solo gli snippet dei risultati e non le pagine intere. Le cifre marcate "stima mia" sono calcoli miei, non dati di fonte. Dove non ho potuto verificare qualcosa lo dico.*

---

## 4. Cosa vendiamo che ChatGPT a 20 $/mese non dà

### Cosa può già fare il lettore nel 2026

**Kindle Translate (lato autore, non lato lettore)**
- Amazon l'ha lanciato il 6/11/2025 in beta solo su invito, per gli autori KDP. All'inizio copriva EN↔ES e DE→EN.
  - Fonti: https://techcrunch.com/2025/11/06/amazon-launches-an-ai-powered-kindle-translate-service-for-ebook-authors, https://slator.com/kindle-translate-amazon-create-ai-translated-ebooks-72-hours/
- Amazon dichiara che meno del 5% dei titoli su Amazon esiste in più di una lingua. Fonte: https://ppc.land/amazon-launches-kindle-translate-for-independent-authors/
- Fonti secondarie riportano un'espansione a francese, italiano e portoghese tra maggio e il 30 giugno 2026. Le date sono incoerenti tra le fonti e il servizio sarebbe ancora in beta ad agosto 2026.
  - Fonti: https://www.builtwritten.com/blog/kindle-translate-5-languages-free, https://releasebot.io/updates/amazon/kindle-direct-publishing, https://www.tecmundo.com.br/software/414315-kindle-translate-agora-usa-ia-para-traduzir-livros-para-o-portugues.htm
- I titoli tradotti così sono etichettati come tali per i lettori. Il servizio è gratuito per l'autore. Secondo le help page KDP citate nei risultati, i contenuti di pubblico dominio sono esclusi.
  - Fonte: https://kdp.amazon.com/en_US/help/topic/GV3T7N96QXE8CEMA (citata nei risultati, letta solo come snippet)
- **Cosa significa per noi:** gli autori indie che possiedono i propri diritti tradurranno gratis da soli. Il nostro spazio resta quello dei titoli i cui diritti sono in mano a editori tradizionali, o ai pochi autori che non usano KDP.

**Strumenti del lettore**
- **Immersive Translate** trasforma un EPUB in un'edizione bilingue usando DeepL o ChatGPT. Dichiara 10–20 milioni di utenti; il dato è del vendor e non è verificato.
  - Fonti: https://immersivetranslate.com/en/document/epub-translator, https://www.videosdk.live/ai-apps/immersivetranslate
- **bilingual_book_maker** (open source, basato su ChatGPT) ha circa 9.400 stelle su GitHub. Fonte: https://gittrend.io/repo/yihong0618/bilingual_book_maker
- **App Kindle:** ha un traduttore per brani selezionati in poche lingue e può passare il testo selezionato al menu di condivisione di iOS. **Apple Books:** si seleziona il testo e si sceglie "Traduci". Entrambe sono funzioni passaggio per passaggio, non traduzioni del libro intero.
  - Fonte: https://matetranslate.com/en/help/translate-books-and-articles-on-iphone
- **Google Play Books:** ha avuto una traduzione istantanea delle selezioni dal 2012. Non ho trovato conferme che esista ancora nel 2026.
  - Fonte: https://ebookfriendly.com/instant-translation-is-a-killer-feature-of-google-play-books/

**Quanto è diffuso tradurre libri interi in autonomia?** Non ho trovato dati affidabili. I segnali indiretti (milioni di utenti dell'estensione, migliaia di stelle GitHub) indicano una nicchia tecnica, non il lettore medio.

**DRM.** Per tradurre un libro intero il lettore deve:
1. comprare l'originale;
2. togliere il DRM (illegale nell'UE: art. 6 della direttiva 2001/29/CE; lo dico da conoscenza generale, non l'ho verificato con una ricerca);
3. gestire file e strumenti;
4. accettare una traduzione non rivista, con terminologia incoerente.

### Perché qualcuno dovrebbe pagare la nostra edizione

1. **Nessuna frizione e legalità.** Il lettore compra un ebook o un cartaceo in italiano su Amazon, Kobo o in libreria. Il cartaceo POD e l'audiolibro non si fanno con ChatGPT.
2. **Il lettore target non legge la lingua di partenza.** L'argomento regge davvero solo se la fonte è tedesca, francese, giapponese, russa e così via, oppure per lettori italiani che non leggono comodamente in inglese.
   - Solo il 5% circa dei lettori italiani è digitale (Eurostat, via https://www.orizzontescuola.it/e-book-e-audiolibri-in-europa-nel-2025-gli-acquisti-salgono-al-95-litalia-resta-indietro-con-meno-del-5-di-lettori-digitali/). Chi usa Immersive Translate è una minoranza della minoranza.
3. **Qualità verificata.** Revisione umana, glossario coerente, formule, citazioni e unità di misura controllate. Note del curatore, glossario finale, indice analitico.
4. **Selezione (curatela).** Il valore sta nel trovare il libro giusto, non nel tradurlo.

**Argomento contrario onesto:** per un lettore che già legge l'inglese, un'edizione italiana di un libro inglese vale poco. Il valore massimo si ottiene traducendo verso l'inglese da lingue "minori" (il mercato EN è molto più grande) e verso l'italiano, lo spagnolo e il tedesco da lingue che il lettore non legge.

### Rischio legale chiave: protezione debole della traduzione AI
- Negli USA una traduzione interamente AI non è proteggibile da copyright. Fonte: https://janefriedman.com/amazon-offers-free-ai-translation-service-to-indie-authors-raising-copyright-questions/
- In Italia la L. 132/2025 tutela le opere fatte con l'AI solo se c'è un apporto creativo umano. Fonte: https://www.lavoripubblici.it/news/intelligenza-artificiale-pubblicata-gazzetta-ufficiale-legge-ai-132-2025-36444
- **Conseguenze:**
  - Sui titoli **in licenza** il fossato è il diritto sull'opera originale (in esclusiva), non la traduzione.
  - Sui titoli di **pubblico dominio o CC-BY** tradotti con AI non c'è nessun fossato: chiunque può copiare.

---

## 8. Canali e costo di acquisizione (CAC)

### Mercato Italia (AIE 2025)
- Varia: 1.604,9 M€ in totale (-1,6%).
- Ebook: 87 M€ (+2,4%). Audiolibri in abbonamento: 34 M€ (+13,3%). Il digitale vale circa il 7,5% (calcolo mio).
- Saggistica in calo (in copie): generale -3,3%, specialistica -10,6%.
- Fonti: https://www.orizzontescuola.it/il-mercato-editoriale-italiano-chiude-il-2025-con-tre-milioni-di-copie-in-meno-calano-i-libri-cartacei-crescono-ebook-e-audiolibri/, https://www.italiaoggi.it/marketing-e-media/media/libri-il-2025-segna-un-calo-speranze-sul-2026-d1lvbt3i

**Concorrenza sui diritti.** Nel 2023 gli editori italiani hanno comprato 9.328 diritti di traduzione, di cui 5.778 dall'inglese. Fonte: https://libreriamo.it/libri/diritti-di-traduzione-libri-italiani/
- I titoli inglesi di divulgazione con domanda provata vengono quasi tutti già comprati da editori tradizionali.
- I titoli "mai tradotti" sono quindi, per selezione, quelli a domanda più bassa, oppure in lingue meno presidiate. **È il principale rischio di mercato.**

### Amazon (KDP e Amazon Ads)
- **Benchmark del vendor:** CPC 0,30–0,50 $, ACOS 30–50%, conversione da clic a vendita 5–15%. Non sono dati ufficiali Amazon. Fonte: https://univers.studio/ads-calculator/
- ACOS di pareggio ≈ royalty / prezzo, quindi circa il 70% per un ebook a 4,99 $. Per la saggistica la fascia di prezzo più adatta alla pubblicità è 5,99–9,99 $.
  - Fonti: https://www.vappingo.com/word-blog/acos-amazon-ads-books/, https://www.vappingo.com/word-blog/amazon-ads-nonfiction-books/
- Su Amazon.it, .fr, .es e .nl i CPC sono "spesso molto bassi" (dato qualitativo, senza numeri; si consiglia un test da 1–2 €/giorno). Fonte: https://www.vappingo.com/word-blog/amazon-ads-international-marketplaces/

**CAC per vendita (stima mia)**
- Con CPC 0,30–0,50 € e conversione 5–15%, il costo per vendita va da **2 € a 10 €**.
- Ebook a 9,99 € con IVA al 4% e royalty del 70%: circa 6,7 € lordi. Togliendo circa il 25% del netto al titolare dei diritti, restano circa 5 €.
- **Con la sola pubblicità a pagamento si è in pareggio o in leggera perdita per copia.** Ha senso solo se attiva il ranking organico.

**Kindle Unlimited**
- Pagamento per pagina KENP: circa 0,0042 $ (gennaio e luglio 2026) e circa 0,00517 $ (agosto 2026). Stime di autori e settore, non dati pubblicati da Amazon. Fonte: https://www.inkfluenceai.com/how-to-sell-romance-novels, https://profitable.app/kdp/stats/kenp-rate
- Un libro di circa 400 pagine KENP letto per intero rende circa 1,7–2 $ (stima mia).
- Richiede l'esclusiva KDP Select sull'ebook, quindi niente Kobo, Apple o StreetLib. La saggistica in KU rende meno della narrativa di genere (lettori meno "voraci"): è un'inferenza mia, non verificata.

### Altri canali
- **StreetLib** (aggregatore italiano): nessun costo iniziale, commissione di circa il 20% sul netto. All'autore resta circa il 56–70% secondo il negozio (dato di terzi). Oltre 50 retailer, forte presenza in Italia, Francia e Spagna.
  - Fonte: https://scribecount.com/author-resource/publishing-wide/streetlib-for-indie-authors
- **BookBub** copre solo USA, Regno Unito, Canada e Australia, non l'Italia. Fonte: https://support.bookbub.com/articles/can-i-work-with-bookbub-if-im-based-outside-of-the-us/
  - Non ho trovato equivalenti italiani consolidati.
- **Divulgazione social in Italia:** esiste un ecosistema forte (Geopop, Barbascura X, divulgatori su TikTok), ma non ho dati che colleghino questi canali alle vendite di libri tradotti. La classifica 2025 è dominata da narrativa e self-help. **Non verificato.**
  - Fonti: https://www.focusjunior.it/?p=242244, https://www.italiaoggi.it/marketing-e-media/media/libri-dan-brown-si-conferma-e-suo-il-titolo-piu-venduto-nel-2025-wee19n8i
  - Strategia probabile: affiliazioni o co-branding con divulgatori (prefazione, quota sulle vendite). È un'ipotesi da testare.
- **Newsletter proprietaria:** è l'unico asset di CAC che si accumula nel tempo (Lorenzo ha esperienza di marketing D2C). Non ho benchmark di costo per iscritto in questa nicchia.
- **Audiolibri:** sono disponibili solo i dati di mercato (sopra). I vincoli sulla narrazione AI sono al §9.

**Visibilità della saggistica tradotta di nicchia:** non ho trovato dati quantitativi specifici. L'unico indicatore è il "<5% di titoli multilingua" di Amazon, che suggerisce poca concorrenza a scaffale ma anche poca domanda espressa.

---

## 9. Come costruirlo: pipeline di produzione

### 9.1 Ricerca dei titoli
- **Strumenti:**
  - Publisher Rocket / Kindlepreneur e TCK stimano le vendite giornaliere dal BSR, per formato e marketplace. Nessuna conversione pubblica BSR→vendite: sono stime proprietarie.
    - Fonti: https://kindlepreneur.com/calculator, https://www.tckpublishing.com/amazon-book-sales-calculator/
  - BookBeam e KDSpy sono alternative. Fonte: https://writem.substack.com/p/publisher-rocket-vs-kdspy-pro
- **Criteri proposti (miei):**
  - BSR dell'originale stabilmente sotto 20–30k per più di 2 anni;
  - più di 500 valutazioni su Goodreads con media ≥4,0;
  - nessuna edizione nella lingua di destinazione (controllo su Amazon.it/.de/.es, OPAC SBN, Index Translationum);
  - categoria con domanda per lo stesso tema in lingua di destinazione (volume di ricerca su Amazon.it).
- Tutto questo è automatizzabile con scraping e un LLM che riassume.

### 9.2 Diritti
- Benchmark di anticipi (Germania): **3.000–8.000 €** con royalty dell'8–10% sul prezzo di copertina (fonte non verificabile). Fonte: https://www.artfolio.com/article/negotiating-translation-rights-rates-and-pitfalls-for-freelance-authors
- Royalty per la saggistica: tipicamente 7–8%. Fonte: https://scribecount.com/author-resource/translations/selling-translation-rights
- Per tirature limitate o partner nuovi è comune un compenso fisso invece di un anticipo. Fonte: https://ask.up.hcommons.org/do-translation-deals-include-royalties-or-only-a-fixed-price/
- **Tempi:** il contratto richiede almeno 6 mesi e l'editore ha fino a 2 anni per pubblicare (Springer Nature). Fonte: https://www.springernature.com/de/partners/rights-permissions-third-party-distribution/translations
  - **È il collo di bottiglia per un'attività solo da 5–10 h/settimana.**
- Una fascia di 1–3 k€ per titoli di backlist non venduti, solo ebook più POD, **non l'ho verificata**: è da validare con 10–20 email ad agenti ed editori.
- **Attenzione:** molti contratti vietano esplicitamente la traduzione con AI. Gli editori stanno iniziando a farla in proprio (VBK nei Paesi Bassi, HarperCollins Francia per Harlequin), quindi potrebbero tenersi i diritti.
  - Fonti: https://www.iamexpat.nl/lifestyle/lifestyle-news/largest-dutch-publisher-use-ai-translate-books-english, https://www.webpronews.com/harpercollins-turns-to-ai-for-harlequin-translations-igniting-backlash/

### 9.3 Qualità della traduzione LLM (2025–2026)
- **WMT25:** 30 coppie di lingue, 60 sistemi (24 LLM o servizi online), test set volutamente più difficili (letterario, social, parlato) che hanno fatto emergere più debolezze. Non ho potuto leggere le classifiche.
  - Fonti: https://aclanthology.org/2025.wmt-1.22, https://tech.slator.com/?p=109884
- **Letterario (LitEval, NAACL 2025):** le traduzioni umane pubblicate battono sempre gli LLM, che sono più letterali e meno vari. I valutatori riconoscono la traduzione umana nell'80–100% dei casi. Fonte: https://arxiv.org/html/2410.18697v1
- **Tecnico o informativo:**
  - Studio clinico 2025: GPT-4o equivalente ai traduttori professionisti in MQM (differenza 1,6 punti); i professionisti preferivano l'LLM nel 52% dei casi (campione piccolo, n=20).
  - GPT-4 si comporta come un traduttore junior, peggio dei senior. Errori tipici: letteralità e incoerenza lessicale.
  - Fonte: https://arxiv.org/pdf/2411.13775 e studio UCSF (https://pediatrics.ucsf.edu/node/477426)
- **Terminologia scientifica (EAMT 2026, EN→FR, GPT-4o, GPT-5.2, Claude Sonnet 4.5, DeepSeek):** Claude Sonnet 4.5 è il migliore, ma gli LLM non sostituiscono i corpora specialistici. La confidenza dichiarata dal modello è poco correlata con l'accuratezza. Fonte: https://aclanthology.org/2026.eamt-1.55.pdf
- Errori terminologici restano anche con memorie di traduzione e glossari, quindi servono basi terminologiche per il controllo qualità. Fonte: https://journals.savba.sk/index.php/jc/article/view/6135
- La qualità cala con la densità di termini rari. Fonte: https://arxiv.org/pdf/2602.24119
- **Errori attesi nella divulgazione scientifica:**
  - termini tecnici e falsi amici;
  - incoerenza dello stesso termine tra capitoli;
  - unità e numeri (separatori decimali);
  - citazioni di opere già tradotte (va usata la traduzione italiana esistente, non ritradotta);
  - titoli di libri e articoli;
  - formule (rischio di "correzioni" del modello).

### 9.4 Revisione umana (costo)
- Non ho trovato tariffe italiane 2025 per il post-editing.
- Riferimenti disponibili:
  - traduzione editoriale dall'inglese circa 15–17 €/cartella (Il Post, dato del 2016; https://www.ilpost.it/2016/03/30/linee-guide-contratti-traduttori/);
  - fascia bassa citata in un forum: 0,03–0,04 €/parola (https://www.arredamento.it/forum/viewtopic.php?p=1818220);
  - range internazionale per la traduzione: 0,05–0,50 $/parola (https://translayte.com/it/blog/quanto-costa-un-traduttore-nel-2024).
- Il post-editing è regolato dalla norma ISO 18587 (leggero o completo).
- **Stima mia** per un saggio da 80–100 mila parole (circa 350–400 cartelle):
  - revisione completa bilingue: **2.000–4.000 €**;
  - rilettura monolingue leggera: 800–1.500 €;
  - verifica di un esperto di dominio (per matematica e fisica): +300–600 €.

### 9.5 Impaginazione e formule
- **Kindle:** storicamente converte il MathML in immagini senza testo alternativo (DAISY, ottobre 2024). Amazon dice di aggiornare la conversione. Fonte: https://dl.daisy.org/projects/webinars/2024-10/Reading_Solutions_Transcript.docx
- **Apple Books** visualizza il MathML. Su Kobo non ho trovato conferme. Fonti: https://epubsecrets.com/mathml-support-in-epub-reading-systems.php, https://www.mobileread.com/forums/showthread.php?p=4439438
- **Soluzione:** EPUB3 con MathML più immagini SVG/PNG di riserva con testo alternativo, generate da LaTeX (Pandoc). Per il POD: PDF da LaTeX.
- **Conseguenza:** preferire la divulgazione con poche formule.

### 9.6 Copertine, metadati, ISBN
- Copertina: designer freelance più template, circa 100–400 € (stima mia).
- ISBN in Italia: li gestisce EDISER (AIE) tramite isbn.it. **Non ho trovato il prezzo 2025**, va verificato. Fonte: https://www.babelezon.com/che-cose-il-codice-isbn
- Per gli ebook su KDP l'ASIN basta.

### 9.7 Stampa su richiesta (POD)
- KDP Print UE (it/de/fr/es/nl/ie), bianco e nero, 24–110 pagine: costo fisso 2,05 € (formato regolare). Il costo per pagina oltre le 110 non l'ho potuto confermare. Fonte: https://kdp.amazon.com/en_GB/help/topic/G201834340
- IngramSpark: costi non verificati.
- StreetLib offre anche il POD. Fonte: https://www.businesswire.com/news/home/20231018882291/en/Bowker-partners-with-StreetLib-to-offer-global-ebook-and-audiobook-distribution/

### 9.8 Audiolibri con voce AI
- **ACX/Audible:** narrazione umana obbligatoria salvo le vie interne Amazon (Virtual Voice di KDP, Voice Replica su invito). Non si possono caricare file ElevenLabs.
  - Fonti: https://www.inkfluenceai.com/blog/ai-narration-audible-acx-policy-2026, https://cognitivefuture.ai/elevenlabs-for-audiobooks/
- **Spotify, Google, Apple, Kobo:** accetterebbero la narrazione AI dichiarata (fonti secondarie e in parte contraddittorie).
- **ElevenReader Publishing:** gratuito, royalty del 60% sul netto, senza esclusiva, ma **solo in inglese** (altre 32 lingue "previste").
  - Fonti: https://www.publishersweekly.com/pw/by-topic/industry-news/audio-books/article/98510-elevenreader-launches-sales-for-ai-generated-audiobooks-offers-60-royalty.html, https://kindlepreneur.com/elevenreader-publishing/
- Piani ElevenLabs: 11–330 $/mese. Per un libro, stima mia circa 100–300 $.
- Per gli audiolibri in italiano su Storytel e Audible la strada AI è incerta, quindi **va considerata un'opzione, non una base del modello.**

### 9.9 Obblighi verso Amazon
- KDP considera "AI-generated" anche le **traduzioni** fatte con AI, **anche se rivedute in modo sostanziale**: vanno dichiarate.
- Un blog segnala controlli più severi da aprile 2026.
- Fonti: https://ebookfriendly.com/amazon-requires-to-inform-of-the-use-of-ai-generated-content/, https://writeo.app/news/amazon-kdp-ai-disclosure-enforcement-2026

### 9.10 Costo totale per titolo e lingua (stima mia)

| Voce | Titolo in licenza | Pubblico dominio / CC-BY |
|---|---|---|
| Diritti (anticipo o compenso fisso) | 1.000–5.000 € (non verificato) | 0 € |
| LLM (traduzione multi-passaggio, controllo qualità, back-translation; 1–3 M token) | 30–150 € | 30–150 € |
| Revisione umana completa | 2.000–4.000 € | 800–2.500 € |
| Esperto di dominio (opzionale) | 300–600 € | 0–300 € |
| Copertina, ISBN, varie | 150–500 € | 150–300 € |
| Audiolibro AI (opzionale) | 100–300 € | 100–300 € |
| **Totale** | **≈ 3.500–10.000 €** | **≈ 1.000–3.500 €** |

**Pareggio:** con circa 5 € netti a copia per l'ebook (dopo la royalty al titolare) servono **700–2.000 copie per titolo in licenza** (stima mia). Per la saggistica di nicchia in Italia è un risultato buono, non garantito.

**Tempo per titolo per Lorenzo (stima mia, a pipeline matura):** 8–15 ore. Così ripartite:
- ricerca del titolo: 2 h;
- trattativa sui diritti: 2–4 h, distribuite su mesi;
- supervisione di AI e revisore: 2–4 h;
- metadati, lancio e pubblicità: 2–4 h.

Con 5–10 h a settimana fanno circa 20–40 titoli l'anno al massimo.

---

## 12. Cosa ucciderebbe l'idea e test più economico

### Cosa ucciderebbe l'idea
1. **Domanda per titolo troppo bassa.** I titoli forti sono già tradotti dagli editori italiani (oltre 9.300 diritti l'anno), quindi restano quelli di coda. Un saggio di nicchia che vende 100–300 copie l'anno non ripaga 5.000 €.
2. **Diritti non disponibili o con clausole anti-AI.** Gli editori stanno internalizzando la traduzione AI (VBK, HarperCollins Francia) e i tempi di contratto sono lunghi (6+ mesi).
3. **Reazione negativa sulla qualità.**
   - In Corea l'app di ebook Chaek Doduk ha dovuto scusarsi e rimborsare per traduzioni AI non dichiarate. Fonte: https://www.koreajoongangdaily.com/lifestyle/ebook-app-faces-backlash-apologizes-over-undisclosed-ai-translations/12797276
   - CEATL ed EWC (traduttori e scrittori europei) si oppongono a Kindle Translate. Fonte: https://creativesunite.eu/article/books-cannot-be-translated-in-a-click
   - Clima di sfiducia generale (il caso "Shy Girl" ritirato da Hachette per sospetto uso di AI). Fonte: https://csmonitor.com/Arts-Culture/Books/2026/0812/ai-publishing-commonwealth-prize-shy-girl
4. **Commoditizzazione.** Kindle Translate gratuito e strumenti per il lettore riducono il valore della traduzione in sé.
5. **Nessun fossato** sui titoli di pubblico dominio o CC-BY tradotti con AI (protezione debole, vedi §4).

### Test proposto: 8 settimane, budget circa 3.000 € (con un'estensione a circa 15 k€)

**Fase A (settimane 1–4), pipeline e qualità, circa 1.500 €**
- Scegliere 3 titoli a costo zero di diritti:
  - 2 libri **CC-BY** di divulgazione o didattica scientifica (es. Open Book Publishers, OAPEN). Controllare la licenza titolo per titolo: CC-BY ammette traduzione commerciale con attribuzione, ma va verificato pagina per pagina. Fonti: https://www.openbookpublishers.com/section/14/1/210409cf37c6441f830be098065803ae, https://oabooks-toolkit.org/about-the-toolkit/article/5842566-plan-s
  - 1 classico di **pubblico dominio** senza traduzione italiana moderna, con valore aggiunto: note, introduzione, glossario. KDP accetta il pubblico dominio solo se "differenziato", e la traduzione originale è uno dei criteri ammessi. Fonte: https://kdp.amazon.com/en_US/help/topic/G200743940
- Costo: AI circa 300 € + revisione leggera 3 × circa 400 € (su campioni e parti segnalate) = circa 1.500 €.
- **Soglie di qualità:**
  - densità di correzioni del revisore ≤ 1 errore "grave" (significato, terminologia, numeri) ogni 10 pagine dopo il controllo automatico;
  - tempo del revisore ≤ 25 h per 80 mila parole;
  - test alla cieca con 20–30 lettori (passaggi nostri contro traduzione umana, dove esiste): **preferenza per la nostra o parità ≥ 40%**;
  - formule: rendering corretto su Kindle (fallback) e Apple Books.

**Fase B (settimane 4–8), segnale di mercato, circa 1.500 €**
- Pubblicazione ebook più POD su KDP (Amazon.it) e StreetLib, con dichiarazione AI su KDP. Prezzo ebook 4,99–7,99 €.
- Amazon Ads: circa 10 €/giorno per titolo × 30–40 giorni, cioè circa 1.000–1.200 €. Più una landing page con lista d'attesa per 3–5 titoli "in licenza" ipotetici (senza vendita), per misurare gli iscritti per tema.
- **In parallelo e a costo zero:** 15–20 email a editori ed agenti per quotazioni su diritti di backlist (solo ebook più POD; con traduzione AI dichiarata). Misura: tasso di risposta e prezzo medio.

**Soglie go/stop (dopo 60 giorni)**

| Metrica | VAI | STOP |
|---|---|---|
| Vendite pagate per titolo (ebook + POD), solo Italia | ≥ 50 | < 15 |
| Conversione da clic a vendita delle pubblicità | ≥ 8% | < 4% |
| CTR delle pubblicità | ≥ 0,3% | < 0,15% |
| ACOS ebook | ≤ 70% | > 120% |
| Valutazione media (con almeno 5 recensioni) | ≥ 4,0 | < 3,5 o ≥ 2 recensioni che citano "traduzione automatica/errori" |
| Resi KDP | < 5% | > 10% |
| Editori che rispondono con un'offerta | ≥ 3 su 20, anticipo ≤ 3 k€ | 0–1, o clausole anti-AI generalizzate |

**Bias da tenere presente:** i libri CC-BY e di pubblico dominio hanno domanda strutturalmente più bassa (e l'originale è gratis), quindi un "VAI" è forte e uno "STOP" è debole. Se la pipeline passa ma la domanda è ambigua, il passo successivo è **circa 10–15 k€ per 2–3 titoli in licenza** con domanda provata (BSR dell'originale < 20k), soglia di 300 copie in 90 giorni.

---

## 13. Modelli 2027 e architettura AI

### Architettura consigliata (pipeline agentica)
1. **Acquisizione:** PDF/EPUB → Markdown strutturato con LaTeX per le formule, riferimenti, didascalie. Le formule si bloccano come token non traducibili.
2. **Estrazione terminologica:** glossario per ogni libro e glossario di dominio. Fonti di verifica: IATE (termbase UE), collegamenti interlingua di Wikipedia, traduzioni italiane esistenti delle opere citate. Si consulta via **RAG** durante la traduzione. Motivazione: gli studi EAMT 2026 e Absolon mostrano che il glossario resta necessario.
3. **Traduzione a livello di documento:** guida di stile, riassunti dei capitoli, memoria di traduzione (TM) dei segmenti già approvati. Due modelli diversi, con scelta o fusione dei risultati.
4. **Controllo qualità automatico a più livelli:**
   - controlli deterministici: numeri, unità, formule intatte, rimandi a figure e note, citazioni;
   - **LLM-giudice** di tipo GEMBA-ESA, lo stesso usato in WMT25 (https://arxiv.org/pdf/2508.14909v1);
   - punteggi di stima della qualità (CometKiwi, MetricX) per segnalare i segmenti a rischio;
   - back-translation sui passaggi segnalati.
   - Attenzione: la confidenza auto-dichiarata dai modelli è poco affidabile (EAMT 2026), quindi servono giudici indipendenti.
5. **Revisore umano:** legge tutto il testo, ma lavora su una lista di segmenti segnalati. **Le sue correzioni aggiornano in automatico** la guida di stile, il glossario e la TM (un ciclo di apprendimento che non richiede fine-tuning).
6. **Fine-tuning sullo stile:** priorità bassa. Con modelli migliori, prompt, esempi e TM bastano. Ha senso valutarlo solo oltre 50 titoli.
7. **Generazione dei file:** EPUB3 con MathML e fallback SVG (Kindle), PDF LaTeX per il POD, metadati ONIX, varianti di copertina, testi per le pubblicità.
8. **Livello commerciale:** agente che cerca titoli (BSR, Goodreads, controllo "mai tradotto"), bozze delle email per i diritti, gestione delle campagne pubblicitarie.

### Modelli migliori: rafforzano o indeboliscono il business?
- **Rafforzano il margine:** costi LLM e ore di revisione scendono, e si possono fare più lingue per titolo.
- **Indeboliscono la proposta di valore della traduzione in sé:** Kindle Translate gratuito (con nuove lingue nel 2026), strumenti per il lettore, e soprattutto **i titolari dei diritti che faranno da soli** (VBK, HarperCollins Francia, Nuanxed con oltre 800 traduzioni). Fonte: https://www.publishersweekly.com/pw/by-topic/industrynews/publisher-news/article/96529-sweden-s-nuanxed-promises-fast-accurate-ai-book-translations.html
- **Il fossato resta:** diritti esclusivi, curatela, marchio e collana, recensioni accumulate, newsletter.
- **Saldo netto:** nel medio periodo l'AI migliore **comprime** questo business. Il vantaggio di chi entra presto vale forse 2–4 anni, a patto di bloccare diritti di catalogo con contratti lunghi.

---

## Esempi: piccoli editori ed esperimenti di traduzione AI

- **Iperborea** (Milano, nicchia di letteratura nordica tradotta): ricavi circa 1,63 M€ (2020) → circa 3,04 M€ (2024), utile circa 250 k€ (aggregatore, da verificare sui bilanci). *L'anno della lepre* di Paasilinna vende ancora circa 6.000 copie l'anno. **Ha dipendenti, non è solo.** Mostra che un catalogo di nicchia tradotta può rendere anche dopo decenni.
  - Fonti: https://topaziende.quotidiano.net/?p=203790, https://www.ilpost.it/2015/12/07/iperborea-e-cresciuta/
- **Nuanxed** (Svezia): traduzione AI più post-editing umano, circa 50 traduzioni al mese, oltre 800 nel totale, soprattutto narrativa commerciale (dati aziendali). Fonte: https://www.publishersweekly.com/pw/by-topic/industrynews/publisher-news/article/96529-sweden-s-nuanxed-promises-fast-accurate-ai-book-translations.html
- **VBK / Simon & Schuster:** meno di 10 titoli di narrativa commerciale con diritti inglesi mai venduti, con consenso degli autori e revisione umana. Forti critiche dai traduttori. **Nessun risultato pubblicato trovato.** Fonte: https://multilingual.com/dutch-book-publisher-vbks-ai-translation-trial-sparks-debate/
- **Kindle Translate:** Amazon dichiara valutazioni medie sopra le 4 stelle (dato non verificato). Fonte: https://www.builtwritten.com/blog/kindle-translate-5-languages-free
- **Leanpub** offre traduzioni AI agli autori. Fonte: https://leanpub.com/blog/leanpub-leapfrogs-amazon-kdp-with-ai-powered-book-translations/
- **Non ho trovato** nessun caso documentato di editore individuale reso redditizio da traduzioni AI di saggistica, né dati di vendita di titoli AI tradotti da pubblico dominio su KDP.

**Reazioni dei lettori:** le reazioni negative documentate riguardano soprattutto **l'uso di AI non dichiarato** (Chaek Doduk, con rimborsi), non la qualità in sé. La trasparenza (etichetta "tradotto con AI e rivisto da X") più la revisione umana è la mitigazione principale.

---

## Scorecard v2 (stima)

| Criterio | Voto | Motivazione |
|---|---|---|
| **validabilità (valid)** | **3** | La pipeline e un primo segnale di mercato si testano con circa 3 k€ in 8 settimane su CC-BY e pubblico dominio. Ma la domanda vera (titoli in licenza) richiede contratti che durano mesi e 10–15 k€. |
| **automatizzabilità (autom)** | **3** | Traduzione, controllo qualità, EPUB e metadati sono quasi del tutto automatizzabili. Ricerca dei titoli, trattativa sui diritti, gestione del revisore e lancio restano umani. Con 5–10 h/settimana si fanno circa 20–40 titoli l'anno. |
| **margine** | **3** | Il margine per copia è buono (circa 5 € netti a ebook, circa 50–70% del netto), ma il costo fisso per titolo è 3,5–10 k€, la pubblicità è in pareggio (ACOS 30–70%) e le vendite per titolo di coda sono basse. Rischio di catalogo con molti titoli in perdita. |
| **solo1M** | **2** | 300–500 k€ l'anno richiedono circa 60–100 mila copie l'anno (circa 100–200 titoli × lingue con 500–1.000 copie ciascuno). Plausibile solo puntando al mercato inglese da lingue minori, e con qualche titolo di successo. 1 M€ da soli è improbabile: Iperborea fa circa 3 M€ ma con uno staff. |

**Giudizio sintetico:** è un'idea fattibile e a basso rischio di perdita (il test costa al massimo 3–15 k€). Il collo di bottiglia non è l'AI ma **la domanda per titolo e l'accesso ai diritti**, e l'AI migliore erode il valore della traduzione in sé. Conviene solo se il test mostra titoli di coda che vendono almeno 50 copie in 60 giorni, e se si riescono a bloccare diritti di catalogo pluriennali a meno di 3 k€ a titolo.
