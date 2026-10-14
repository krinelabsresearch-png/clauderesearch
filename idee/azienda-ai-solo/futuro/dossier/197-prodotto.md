# 197 — Libri low content con AI su Amazon: prodotto, canali, produzione, architettura, test

> Rapporto di ricerca del 14/10/2026 (agente di ricerca, verificato a campione da Claude). Le voci [NV] non sono verificate con una fonte; "stima" indica un calcolo.

# IDEA 197: libri low/medium-content generati con AI e venduti su Amazon KDP

Ricerca chiusa il 14/10/2026 con 35 WebSearch, cioè tutto il budget. Molte fonti del settore KDP sono blog di venditori di tool o di corsi: le segnalo come **[vendor/guru]**. Dove scrivo **[stima mia]** il numero è un mio calcolo e non viene da una fonte.

---

## 0. Economia unitaria (serve per tutte le sezioni)

- **Royalty KDP sul cartaceo (cambiata il 10/06/2025).** Sotto una soglia di prezzo per marketplace la royalty è scesa dal 60% al 50%. Su Amazon.com la soglia è $9,99: a $9,98 o meno si prende il 50%, da $9,99 in su il 60%. Anche il prezzo minimo di listino è salito. Fonte: https://kdp.amazon.com/en_US/help/topic/GXFPA52P6ZJD2U3N. Una guida di settembre 2026 dice che questa struttura è ancora in vigore (https://www.vappingo.com/word-blog/kdp-print-royalties/). È un primo esempio concreto di **rischio piattaforma**: Amazon può cambiare le condizioni da sola.
- **Costo di stampa in bianco e nero (US, formato regolare, 110 pagine o più).** La formula indicata da fonti terze è circa $1,00 + $0,012 a pagina. Corrisponde all'esempio KDP (300 pagine = $4,60), ma non l'ho trovata sulla pagina ufficiale (https://bestwriting.com/kdp-royalties). Il formato grande 8,5×11", tipico di coloring e puzzle book, costa di più. **Da verificare sul calcolatore KDP.**
- **[stima mia] Netto per copia:** un libro 8,5×11" da circa 100–120 pagine venduto a **$9,99** rende circa **$2,9–3,2 di royalty**. A $7,99 (quindi royalty al 50%) scende a **circa $1,1–1,5**. Il prezzo di $9,99 o più è quindi praticamente obbligatorio.
- **Per arrivare a 300–500 k€ di fatturato** (che per Lorenzo coincide con le royalty, perché il venditore è Amazon) servono circa 110–180 mila copie l'anno, cioè **300–500 copie al giorno** sull'intero catalogo [stima mia].
- **Conversione BSR → vendite** (stime, non è una formula Amazon). BSR 10.000 ≈ 10–20 copie al giorno; BSR 100.000 ≈ 1–1,5 copie al giorno (https://www.vappingo.com/word-blog/kdp-bsr-sales-estimator/, https://sellerbowl.com/amazon-bsr-chart). Per 400 copie al giorno servono quindi circa 25–40 titoli stabilmente sotto BSR 10k, oppure 300 o più titoli intorno a BSR 100k.
- **Cosa rendono davvero i cataloghi** (annunci di vendita su Empire Flippers, profitti dichiarati dai venditori):

  | Catalogo | Profitto medio/mese | Valutazione |
  |---|---|---|
  | 11 coloring book | ~$1.367 | ~$38k (28× il mensile) |
  | **oltre 1.900 libri di coloring per adulti** | **~$3.217** | ~$90k |
  | 147 libri low-content | ~$1.618 | ~$58k (36×) |
  | catalogo misto (journal, activity, coloring) | ~$1.180 | ~$39k (33×) |

  Link: https://empireflippers.com/listing/90291/, https://empireflippers.com/listing/78031/, https://empireflippers.com/listing/53884/, https://empireflippers.com/listing/83742/. **Sono dati di mercato reali, non di guru, e indicano un tetto tipico di qualche migliaio di dollari al mese.**

---

## 4. Cosa vendiamo che ChatGPT da $20 al mese non dà

**Obiezione.** Sì, chi compra può farsi da solo una pagina da colorare o un sudoku con ChatGPT, Ideogram (che ha un tier gratuito giornaliero) o uno dei tanti generatori gratuiti, e stamparlo a casa (https://toolchase.com/blog/best-ai-coloring-page-generators-2026/). **Il contenuto in sé non vale nulla**: l'AI non è un vantaggio per noi, anzi abbassa il valore percepito.

**Perché la gente compra lo stesso il libro fisico:**

1. **Costo e comodità.** Stampare in casa costa circa 3–20 centesimi a pagina in bianco e nero con inkjet, 2–8 con laser. Le stime si basano su una copertura del 5%; una pagina da colorare piena di linee costa 2–3 volte tanto (https://new.risingsunartscentre.org/news/printing-cost-per-page-black-and-white-2026.html, fonte di bassa autorevolezza). Cento pagine costano quindi già **$3–20 di inchiostro**, più carta, tempo e fogli sciolti. Un libro rilegato a $9,99 regge il confronto.
2. **Regalo.** Un PDF fatto con ChatGPT non si regala. Si dice che circa il 40% delle vendite di puzzle book per anziani siano regali dei figli adulti: è un dato **[vendor]** non verificato (https://www.kdpeasy.com/blog/large-print-word-search-seniors). La gran parte del posizionamento in vetrina punta su "gift for seniors" (https://www.asinsight.com/report/US/word-search-large-print).
3. **Anziani e utenti poco digitali.** Chi compra i word search a caratteri grandi non scrive prompt. Il best-seller di luglio 2026 è un pacchetto da 6 libri a $16,99 con rating 4,6 (asinsight, link sopra).
4. **Screen-free per bambini e adulti.** Secondo Circana, nel Q1 2026 crescono le categorie senza schermo: puzzle book, coloring, logica/brain teaser, guided journal. Il mercato bambini torna a crescere grazie agli activity book (https://www.circana.com/post/turning-the-page-on-2026-book-trends, https://www.publishersweekly.com/pw/by-topic/industry-news/bookselling/article/99800-wi2026-passion-purchases-analog-living-trend-up.html). Nel primo semestre 2025 gli activity book sono stati un motore della saggistica per ragazzi (https://www.infodocket.com/2025/07/17/new-data-from-circana-bookscan-u-s-book-market-holds-steady-in-the-first-half-of-2025-results-and-highlights/). Paradosso: proprio lo stesso trend "analog" porta l'acquirente a premiare l'opera umana e a diffidare dell'AI (vedi più sotto).
5. **Stile curato e firmato.** I veri successi sono **brand con uno stile riconoscibile**, non "pagine qualsiasi":
   - Bobbie Goods: 2,5 milioni di copie dichiarate in 7 mesi in Brasile, dato senza fonte primaria (https://en.wikipedia.org/wiki/Bobbie_Goods).
   - Coco Wyo: collettivo vietnamita, oltre 25 libri auto-pubblicati, 555k follower su Instagram e 332k su TikTok, poi un contratto a sei cifre con Penguin Random House (https://bookriot.com/bold-and-cozy-coloring-coco-wyo-controversies/, https://thebookseller.com/rights/vietnamese-artists-collective-coco-wyo-signs-with-penguin-random-house-childrens-in-six-figure-deal).
   - Jade Summer (Fritzen Publishing): ha licenziato edizioni in Francia (Dessain et Tolra) e Portogallo (Quiuí) (https://export.side.fr/en/9782295017307-comfy-cosy-jade-summer, https://www.continente.pt/produto/profissoes-fofas-livro-de-colorir-de-jade-summer-jade-summer-8778994.html).
6. **Garanzia di qualità sui puzzle.** Soluzione unica, difficoltà progressiva, soluzioni incluse, caratteri grandi. ChatGPT genera sudoku a volte non validi o a soluzione multipla. È un'osservazione nota ma **non l'ho verificata con una fonte in questa ricerca**.

**Conclusione.** Vendiamo **formato fisico + curatela + fiducia + comodità del regalo**, non contenuto. È un vantaggio reale ma **non è legato all'AI**, ed è replicabile da migliaia di concorrenti.

---

## 8. Canali e costo di acquisizione cliente (CAC)

**Amazon SEO**
- Si lavora su keyword, categorie e BSR, e la nicchia stretta vince. Esempio: "Gratitude Journal" ha più di 10.000 concorrenti, "Gratitude Journal for Recovering Perfectionists" ne ha 40 (https://www.vappingo.com/word-blog/why-your-low-content-kdp-book-is-not-selling/).
- Il boom del low-content del 2019–2021 è finito. Notebook e planner generici sono saturi. Puzzle book, soprattutto large print per anziani, vendono con continuità e con riacquisto (https://naomijane.substack.com/p/low-and-medium-content-books-on-amazon, Substack, fonte media).

**Amazon Ads: non ho trovato dati primari 2025–26 specifici per puzzle o coloring**
- CPC sui libri: circa £0,15–0,60 (https://www.vappingo.com/word-blog/amazon-sponsored-products-kdp/); $0,30–0,50 nella media secondo un altro calcolatore (https://univers.studio/ads-calculator/); $0,30–0,80 secondo i report di piccoli editori (https://the-write-moves.beehiiv.com/p/amazon-ads-for-low-content-worth-the-spend-or-a-money-pit).
- Conversione: 5–15%, circa 10% (stesse fonti).
- ACOS sul low-content: 50–150% secondo un'analisi del 2023 citata di seconda mano e non verificata.
- Su un journal da £7,99 il CPC massimo di pareggio è circa £0,21, mentre le offerte suggerite sono £0,35–0,60, quindi in perdita (https://www.vappingo.com/word-blog/amazon-ads-low-content-books/).
- **[stima mia]** Con netto $3, CPC $0,40 e conversione 10%, il **CAC è circa $4 a vendita, superiore al netto per copia**. L'ACOS di pareggio a $9,99 è circa 30%. Le Ads servono a far partire il ranking, non sono un canale profittevole da solo.
- Le Ads funzionano anche su Amazon.it (CPC, moderazione) (https://kdp.amazon.com/it_IT/help/topic/G202081960). Non ho trovato CPC medi per IT o DE.

**Traffico esterno**
- Il coloring "bold & easy" è di tendenza su TikTok (https://www.penguinrandomhouseretail.com/tag/art-photography/).
- Il caso documentato di TikTok è di un workbook, non di un coloring: lo Shadow Work Journal ha venduto oltre 40.000 copie via TikTok Shop, con un creator affiliato che ha incassato più di $150k di commissioni (https://www.boston.com/news/books/2024/05/31/how-a-self-published-book-broke-all-the-rules-and-became-a-bestseller/).
- **Ostilità verso l'AI:** r/AdultColoring vieta l'autopromozione ai "content generator" che usano l'AI, e un'autrice racconta di essere stata attaccata per le illustrazioni AI (https://failurefriday.substack.com/p/failure-friday-30-reddit-found-my).
- Gruppi Facebook per anziani o coloring: nessun dato trovato.

**Etsy (printable)**
- Gli standard di creatività di giugno 2025 hanno tolto la possibilità di usare template o pattern di terzi. È richiesta la disclosure quando l'AI incide in modo sostanziale, ma l'AI non è vietata. Il mercato è saturo: le pagine generiche "cute cat" non vendono più (https://blog.marmalead.com/etsy-print-on-demand/, https://www.techbloat.com/?p=1549010, https://www.promptspace.in/blog/ai-coloring-page-prompts-etsy-sellers-printable-2026).
- Il caso da $18k in una shop è **[guru, senza fonte]**. Le fee Etsy non le ho verificate.

**Altre piattaforme print-on-demand e retail**
- **IngramSpark:** può non accettare libri con più del 10% di pagine bianche o journal, e rifiuta le opere create *solo* con AI generativa (https://www.ingramspark.com/content-guidelines, https://www.ingramspark.com/blog/important-ingramspark-content-guidelines-for-your-titles-success). Un coloring generato con AI quindi è a rischio.
- **Expanded Distribution di KDP:** esclude journal, notebook e planner. I low-content non hanno ISBN gratuito (https://kdp.amazon.com/help/topic/GQTT4W3T5AYK7L45, https://www.vappingo.com/word-blog/kdp-isbn-guide/).
- Lulu: non verificato.
- Il retail e il wholesale passano di fatto per la **licenza a un editore**, come hanno fatto Coco Wyo e Jade Summer. È un canale reale, ma solo per chi ha già un brand affermato.

**[stima mia] Sintesi.** Il modello regge solo se la quota organica supera circa il 60–70% delle vendite. Il CAC a pagamento (circa $3–8) è dello stesso ordine del netto per copia ($1–3).

---

## 9. Come costruirlo

**Ricerca di nicchia**
- Book Bolt: da $9,99 al mese; annuale $89,99 (Newbie) o $199,99 (Pro, che include il generatore di puzzle). Publisher Rocket: una tantum, $97 o $199 a seconda della fonte (https://revenuegeeks.com/book-bolt-pricing/, https://nichepursuits.com/bookbolt-vs-publisherrocket). Sono siti affiliati.
- Conversione BSR → vendite: vedi sezione 0.

**Algoritmi per i puzzle (open source)**
- **Sudoku:** dokusan (Python, GPLv3, solver con tecniche umane come X-Wing o unique rectangle, difficoltà regolabile ma solo approssimata) (https://pypi.org/project/dokusan). sudokutools ha `is_unique()` e `rate()` su una scala 0–10 basata sulla tecnica più difficile richiesta (https://sudokutools.readthedocs.io/en/latest/_modules/sudokutools/analyze.html). Attenzione alla GPL se si distribuisce codice; per stampare i puzzle non dovrebbe essere un problema, ma va verificato.
- **Nonogram:** NonoSharp ha un generatore con unicità verificata dal suo solver (https://www.nuget.org/packages/NonoSharp/); nonogram_dart è MIT e verifica senza backtracking (https://pub.dev/packages/nonogram_dart).
- **Kakuro:** sen-ltd/kakuro, unicità provata via backtracking; licenza non verificata (https://dev.to/sendotltd/solving-kakuro-cross-sums-with-constraint-propagation-sum-combination-domains-fewest-candidate-4mje).
- **Zebra/Einstein:** si genera prima la soluzione e poi gli indizi, togliendo quelli ridondanti (https://codemia.io/knowledge-hub/path/algorithmically_generate_a_zebraeinstein_puzzle). Non ho trovato una libreria matura.
- **Simon Tatham's Portable Puzzle Collection:** licenza MIT, circa 40 tipi (molti di origine Nikoli), riuso commerciale permesso dalla MIT (https://www.chiark.greenend.org.uk/~sgtatham/puzzles/). Dal manuale so che ha generatori a soluzione unica con livelli di difficoltà, ma **in questa ricerca non l'ho verificato**.

**Il vantaggio del matematico**
1. Graduare la difficoltà in base alle tecniche richieste, non al numero di caselle vuote. Il metodo è citato da un engine commerciale (https://www.summerengine.com/ai-logic-puzzle-maker).
2. Unicità garantita tramite SAT o Dancing Links.
3. Tipi di puzzle meno inflazionati (Slitherlink, Hashi, Nurikabe, Kakuro), dato che il sudoku su Amazon.de è "highly contested" (https://www.kdpeasy.com/de/features/sudoku-generator, **[vendor]**).
4. Nonogram a tema che rivelano un'immagine: si passa dall'immagine AI al pixel art e si controlla l'unicità.
5. Libri "medium-content" con un tutorial per ogni tecnica.

**Limite onesto:** chi compra vede la calibrazione solo indirettamente, attraverso le recensioni. È un vantaggio di qualità, non di distribuzione.

**Immagini AI per le pagine da colorare**
- Modelli: GPT Image 1.5 indicato come il migliore per line art (https://fluxnote.io/guides/best-ai-image-generator-for-coloring-pages); Ideogram con contorni più puliti; Recraft che esporta SVG vettoriale nativo (https://toolchase.com/blog/best-ai-coloring-page-generators-2026/).
- Difetti tipici: regioni non chiuse, retini grigi che stampano "fangosi", pagine quasi duplicate, deriva di stile e personaggio da una pagina all'altra (https://www.inkfluenceai.com/blog/sell-ai-coloring-books-on-kdp-2026, https://www.inkfluenceai.com/blog/how-to-make-a-coloring-book-with-ai-2026).
- **[stima mia]** A 300 dpi una pagina 8,5×11" richiede 2550×3300 px. Conviene vettorializzare (potrace o Recraft) e controllare in automatico la chiusura delle regioni con un flood-fill.
- **Licenze Midjourney:** uso commerciale consentito sui piani a pagamento; le aziende sopra $1M di ricavi devono avere il piano Pro o Mega; nessuna manleva, quindi il rischio di proprietà intellettuale resta a noi (https://terms.law/2026/01/15/midjourney-commercial-use-rights-complete-2026-guide/). Le immagini interamente AI sono probabilmente non proteggibili da copyright, quindi chiunque può copiarle (stessa fonte, guida legale).

**Copertine, impaginazione, traduzione**
- Impaginazione: PDF generati via Python, completamente automatizzabile.
- Copertine: generatore di immagini più testo inserito a mano. Ideogram è forte sul testo (fluxnote).
- Traduzione:
  - Sudoku, nonogram, kakuro e coloring sono **indipendenti dalla lingua**: si traducono solo titolo, descrizione e istruzioni, quindi il costo è quasi zero.
  - Word search e cruciverba richiedono liste di parole native (in tedesco ä/ö/ü/ß) e una revisione da madrelingua.
  - Giappone: non ho verificato la disponibilità della stampa KDP su amazon.co.jp.

**[stime mie] Tempi e costi per titolo, a pipeline costruita**

| Tipo di libro | Tempo | Costo | Note |
|---|---|---|---|
| Puzzle book | ~1–2 h (QA, copertina, scheda prodotto) | < $5 | il calcolo costa quasi zero |
| Coloring book da 50 pagine | ~4–8 h, soprattutto QA manuale | ~$10–40 di generazione immagini | si scarta da 2 a 4 volte |

Costruire la pipeline richiede 40–80 h una tantum.

**Disclosure obbligatoria** dell'uso di AI per testo, immagini e traduzioni, titolo per titolo (https://scribecount.com/author-resource/protecting-books/kdp-ai-content-policy-the-compliance-guide).

---

## 12. Cosa lo ucciderebbe, e il test più economico

**Fattori killer**
1. **Account KDP come unico punto di rottura.** Le chiusure sono decise da sistemi automatici con un punteggio di rischio. Fanno scattare la chiusura: cataloghi ripetitivi a template, molti titoli AI caricati in poco tempo, trademark nei titoli (c'è un caso del 2023 di un brand di coloring chiuso per marchi registrati), risposte sbagliate al questionario sull'AI (https://selfpublishing.com/amazon-kdp-account-was-closed/, https://lowcontentprofits.com/warning-kdp-account-terminated/, https://www.goodreads.com/author_blog_posts/24443366-kdp-amazon-terminated-my-account-i-am-more-powerful-than-amazon). **Non ho trovato un'ondata documentata di chiusure di account AI coloring nel 2025.** Secondo un blog, nel 2025 le categorie ricche di immagini (coloring, activity) avrebbero ricevuto controlli mirati (https://univers.studio/blog/kdp-ai-content-policy-2026/, non verificato).
2. **Limite di 3 nuovi titoli al giorno per account.** Riportato da fonti secondarie, con date discordanti (2023 o fine 2024). I low-content rientrano nel limite, con esenzioni possibili caso per caso (https://selfpublishingadvice.org/self-publishing-news-kdp-ai-new-limits-on-titles/).
3. **Inondazione di contenuti AI.** Nel caso dei libri per bambini, ricercatori hanno trovato 517 titoli AI e Amazon ne ha rimossi 198 dopo la segnalazione (https://aiweekly.co/alerts/amazons-ai-generated-childrens-books-flood-gift-piles). È un precedente di rimozioni in massa.
4. **Stigma anti-AI nella community del coloring** (r/AdultColoring, vedi sezione 8). Lamentele dirette di acquirenti trovate: poche. Solo una recensione Etsy a 3 stelle che dice "Cute art but lots of ai" (https://www.etsy.com/jp/shop/PagesAndPatterns). **Non ho trovato recensioni Amazon verificabili che parlino di "dita in più".**
5. **Amazon Ads strutturalmente in pareggio o in perdita**, più il precedente del taglio royalty di giugno 2025.
6. **Tetto basso per catalogo**: vedi i dati Empire Flippers nella sezione 0.

**Test proposto: circa €1.500–2.000, 8 settimane**

- **Settimane 1–2.** Costruire la pipeline: generatori di puzzle, PDF automatici, QA automatico.
- **Settimane 2–4.** Pubblicare **24 titoli** rispettando il limite di 3 al giorno. Tre sotto-nicchie con 8 titoli ciascuna:
  - **A.** Puzzle large print a tema per anziani, su IT (parole intrecciate, sudoku a caratteri grandi) e DE (Rätsel Großdruck). Motivo: cultura enigmistica forte in Italia (Settimana Enigmistica circa 400k copie a settimana, margine del 25%, https://www.italiaoggi.it/marketing-e-media/media/la-settimana-enigmistica-e-la-regola-degli-utili-sono-il-25-dei-ricavi-xf17ub6z). Il mercato libri italiano però è in calo (-2,7% copie nel 2025, https://libreriamo.it/libri/libri-piu-venduti-primi-9-mesi-2025/).
  - **B.** Logic puzzle calibrati e meno inflazionati (Kakuro, Slitherlink, nonogram a tema) su US, UK e DE.
  - **C.** Coloring "bold & easy" su US e DE: è il test del rischio AI.
- **Prezzi:** $9,99 / €9,99 o più.
- **Budget:**

  | Voce | Costo |
  |---|---|
  | Tool (Book Bolt, generazione immagini) | ~€200 |
  | Copie autore | ~€150 |
  | Ads ($15–20/giorno per 6 settimane, offerte $0,25–0,45) | ~€1.000–1.300 |

**Soglie a 60 giorni dalla pubblicazione** [soglie mie, derivate dall'economia unitaria]

| Esito | Condizioni |
|---|---|
| **GO** | almeno 8 titoli su 24 con BSR medio sotto 100k, cioè circa 1 copia al giorno o più; catalogo a 15 o più copie al giorno; ACOS al massimo 35%; quota organica almeno 60%; rating medio almeno 4,3; zero avvisi KDP. |
| **STOP** | meno di 3 copie al giorno su tutto il catalogo alla settimana 8; oppure ACOS sopra 70% dopo l'ottimizzazione; oppure rating sotto 4,0; oppure qualunque avviso di qualità o AI. |

**Anche con un GO, il fatturato resta lontano dall'obiettivo.** 15 copie al giorno × $3 fanno circa 16k$ l'anno. Per arrivare a 300 k€ serve un fattore 20, che non si ottiene semplicemente moltiplicando i titoli: i rendimenti calano titolo dopo titolo e c'è il limite di 3 titoli al giorno.

---

## 13. Modelli 2027 e architettura AI

**Pipeline ad agenti**
1. **Ricerca di nicchia:** export da Book Bolt o Helium più un LLM che fa da ranker. Lo scraping diretto di Amazon pone un problema di termini di servizio, non verificato.
2. **Generazione:** motori di puzzle deterministici più modelli di immagine.
3. **QA:** controlli deterministici, cioè un solver indipendente per l'unicità e un flood-fill per le regioni aperte. In più un modello di visione che controlla anatomia e duplicati.
4. **Scheda prodotto:** **KDP non ha un'API pubblica di upload.** Esistono estensioni Chrome che compilano i campi in automatico (https://chrome.google.com/webstore/detail/kdp-uploader/hfnmagmigjbbmjlanikaihcokkmidlfb), ma la compatibilità con i termini KDP non è verificata e c'è rischio per l'account. Meglio un caricamento semi-manuale, circa 15 minuti a titolo.
5. **Ottimizzazione Ads:** regole di offerta automatiche.

**Effetto dei modelli più forti nel 2027.** Indeboliscono il segmento generico, perché il costo di produzione tende a zero per tutti: più inondazione, più controlli Amazon, più stigma. Rafforzano relativamente solo quattro cose:
- (a) i brand e le serie con un seguito social (il modello Coco Wyo);
- (b) recensioni e riacquisti, cioè l'anzianità del catalogo;
- (c) la qualità algoritmica verificabile dei puzzle;
- (d) la licenza verso editori.

**Rischio di cannibalizzazione:** app e chatbot che generano puzzle personalizzati stampabili su richiesta (inferenza mia).

---

## Esempi reali e casi negativi

- **Brand reali (non guru):**
  - Coco Wyo: oltre 25 libri auto-pubblicati, poi contratto a sei cifre con Penguin Random House; nessun fatturato verificato. I "$6M l'anno" sono un claim **[guru, Whop]** (https://whop.com/joined/publishandprosper-ai-llc/products/ai-coloring-book-profits-db/).
  - Jade Summer / Fritzen Publishing: licenze in Francia e Portogallo; fatturato non trovato.
  - Bobbie Goods: artista umana, successo partito da TikTok.
  - Cataloghi Empire Flippers: $1,2–3,2k al mese (sezione 0).
  - **Nessuno di questi brand di successo è dichiaratamente fatto con AI.**
- **Account chiusi o titoli rimossi:** casi aneddotici e chiusure automatiche (sezione 12); 198 libri per bambini AI rimossi. Nessuna ondata 2025 specifica sui coloring documentata.
- **Recensioni negative sui coloring AI:** prove scarse. Solo la recensione Etsy, i difetti tecnici elencati dai vendor e l'ostilità su Reddit. Va controllato a mano con le recensioni a 1–2 stelle dei best-seller.

---

## Voti scorecard v2

| Criterio | Voto | Motivazione |
|---|---|---|
| **valid** | **3** | Domanda reale e in crescita: Circana registra crescita delle categorie screen-free, ci sono riacquisti e regali. Ma è satura, e il nostro "plus" AI non dà vantaggio, anzi può essere uno stigma. |
| **autom** | **4** | Generazione, QA, impaginazione e ottimizzazione Ads sono automatizzabili. Restano manuali upload (niente API, limite 3 al giorno), copertine e QA visivo; 5–10 h a settimana sono realistiche. |
| **margine** | **2** | Netto di circa $3 su $9,99 e CAC a pagamento circa pari al netto. Il margine c'è solo sull'organico, e la piattaforma può tagliarlo da sola (taglio royalty di giugno 2025). |
| **solo1M** | **1** | Cataloghi reali da 147 a 1.900 titoli rendono $1,2–3,2k al mese. Il milione richiede un brand virale di tipo artistico, che è l'opposto di un catalogo AI. |

**Verdetto sintetico.** È un buon esperimento da meno di €2k, utile come asset rivendibile a circa 30× il profitto mensile. **Non è un veicolo credibile per 300–500 k€.** L'unica variante con un tetto più alto è un brand di puzzle o logica "da matematico" con un seguito proprio e licenze a editori, ma a quel punto non è più un business AI-native da 5 ore a settimana.
