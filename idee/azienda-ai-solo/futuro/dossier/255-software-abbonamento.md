# 255: costruire software con Claude Code su un VPS e venderlo in abbonamento

**Ricerca del 30/10/2026,** circa 15 ricerche web. Le fonti sono numerate in fondo; "stima" indica un mio calcolo, "n.v." un dato che non ho verificato.

## Sintesi in 6 righe

1. **Costruire è diventato quasi gratis.** Claude Max costa 100–200 $ al mese e un VPS 5–40 €. Pieter Levels gestisce Photo AI, circa 1,6 M$ l'anno, con Claude Code su un VPS, e dice di non scrivere codice a mano da circa sei mesi [1][2].
2. **Proprio per questo l'offerta è esplosa.** Nell'App Store le nuove app sono cresciute dell'84% nel primo trimestre 2026, mentre i download crescono del 2–3% [3]. A febbraio e marzo 2026 i titoli del software sono crollati per il timore che gli agenti AI sostituiscano gli abbonamenti (la "SaaSpocalypse") [4].
3. **Anche i clienti costruiscono da soli.** Il 35% delle aziende ha già sostituito almeno un SaaS con software proprio [5]. Il 32% ha rinunciato a un acquisto perché poteva farselo con un agente [6]. Il 20% delle piccole imprese irlandesi scrive software in casa, contro il 10% dell'anno prima [7].
4. **Nella realtà i risultati sono bassi.** Tra i SaaS indipendenti con ricavi pubblici il ricavo mensile mediano è 145–168 $. Solo il 6% supera 10 k$ al mese [8]. Per 300 k€ l'anno servono circa 25 k€ al mese, cioè la fascia del 2–3% migliore (stima).
5. **Claude Code risolve la costruzione e la manutenzione, non la vendita.** I clienti si trovano con la distribuzione, la fiducia e un settore preciso, e la tecnologia non li porta.
6. **Verdetto.** "Fabbrica di software in abbonamento", senza una nicchia scelta, è **scartata con 3,35**. Come **veicolo** è però il modo giusto di costruire le idee che hanno un canale: la 234 SERATA, la 107 e la 116 in lista, la 208 OMBRA. Il punteggio è quello della nicchia, non del veicolo.

---

## 1. Il modello e le sue varianti

"Software funzionante in abbonamento" non è un'idea: è un modo di produrre e di farsi pagare. Le varianti possibili sono sei:

| Variante | Come funziona | Punteggio | Motivazione neutra | Esito |
|---|---|---|---|---|
| **B. Verticale con un canale tuo** | Un software per un settore in cui hai accesso ai clienti (discoteche, laureandi, ricercatori) | **quello della nicchia: 234 SERATA 3,95** | 3,55 | **La strada giusta** |
| A. Fabbrica di piccoli software | Tanti strumenti lanciati in fretta; si tengono quelli che vendono | 3,35 | 3,15 | Scartata (è la 255) |
| C. App nei marketplace | App per Shopify, WordPress, Chrome, Atlassian, HubSpot | 3,25 | 3,25 | Scartata |
| F. Comprare un micro-SaaS e migliorarlo con Claude Code | Si compra un prodotto che ha già clienti | 3,20 | 3,00 | Scartata, ma interessante come palestra |
| D. Licenze e software da installare | Kit di partenza, software self-hosted, plugin | 3,05 | 3,05 | Scartata (in più c'è il CRA, vedi §7) |
| E. Software su misura per PMI con canone | Lo costruisci per un'azienda e incassi la manutenzione | 3,05 | 3,05 | Esclusa: è un servizio |

Voti delle varianti (mot, vant, dolore, mercato, margine, valid, solo1M, autom, dif):

| Variante | mot | vant | dolore | mercato | margine | valid | solo1M | autom | dif |
|---|---|---|---|---|---|---|---|---|---|
| A | 4 | 3 | 2 | 5 | 5 | 4 | 2 | 4 | 1 |
| C | 3 | 3 | 3 | 4 | 4 | 4 | 3 | 4 | 1 |
| F | 4 | 3 | 3 | 3 | 4 | 3 | 2 | 4 | 2 |
| D | 3 | 3 | 2 | 3 | 5 | 4 | 2 | 4 | 1 |
| E | 3 | 4 | 4 | 4 | 3 | 5 | 1 | 2 | 2 |

## 2. Mercato

- **Software e SaaS sono un mercato enorme**, quindi il voto "mercato" è 5. Ma il mercato è grande per tutti, e da quest'anno lo è anche per chi costruisce in un weekend.
- **Quanto guadagnano i SaaS indipendenti** [8]:
  - Su 3.787 prodotti con ricavi pubblici (dati TrustMRR), la media è 4.298 $ al mese e la mediana 145 $.
  - Delle aziende nate nel 2025, la mediana è 168 $ al mese e solo il 23,5% supera 1.000 $.
  - Il 6,1% supera 10 k$ al mese.
  - Il campione è distorto verso l'alto: pubblica i ricavi chi ne ha.
- **Cosa serve per i tuoi obiettivi:** 300–500 k€ l'anno sono 25–42 k€ al mese, la fascia del 2–3% migliore. Con un prezzo di 29 € servono circa 860 clienti; con 99 € circa 250; con 299 € circa 85 (stima).

## 3. Concorrenti e saturazione

- **Chiunque abbia Claude Code o Codex.** Le app nell'App Store mostrano la dinamica [3]:
  - 235.800 app nuove nel primo trimestre 2026 (+84%) e circa 560.000 nel primo semestre, verso il record del 2016;
  - i download però crescono del 2–3%;
  - Apple ha iniziato a bloccare alcune app create con il vibe coding.

  Per i SaaS web non esiste un dato equivalente, ma la direzione è la stessa.
- **I clienti stessi.** Le aziende si costruiscono gli strumenti interni [5][6][7]. Un CRM semplice, un gestionale delle prenotazioni o una dashboard ormai il cliente se li fa con Claude.
- **I grandi.** Dopo il crollo di inizio 2026 hanno messo gli agenti dentro i loro prodotti (Salesforce, HubSpot, Atlassian) [4]. Le funzioni generiche diventano gratuite dentro le piattaforme che il cliente già paga.

## 3-bis. Come fanno oggi i solisti che ci riescono

- **Pieter Levels** [1][2]:
  - Photo AI fa circa 105–138 k$ al mese (dati dichiarati da lui, discordanti).
  - Lo stack è semplicissimo: PHP, SQLite, un VPS; Claude Code gira direttamente sul server.
  - La forza vera è la distribuzione: centinaia di migliaia di follower su X, costruiti in 10 anni.
- **Il caso del simulatore di volo** [9]: fatto in poche ore con l'AI, ha toccato 87 k$ al mese dopo 17 giorni. Secondo un'unica fonte, a metà 2026 la sua bio diceva "$0/m". Un successo virale non è un abbonamento che dura.
- Lo schema comune ai casi riusciti: **un pubblico o un canale già posseduto, poi il prodotto.** Non il contrario.

## 4. Cosa fa in più di ChatGPT o Claude da 20 $ (la domanda decisiva)

Qui la domanda si capovolge: il cliente può chiedere a Claude di **costruirgli lo stesso software**. Un abbonamento regge solo se offre cose che non si ottengono con il vibe coding:
1. **Dati che si accumulano**: lo storico, i confronti tra clienti, i modelli addestrati sui dati del settore.
2. **Integrazioni mantenute**: le API di Meta, delle biglietterie e delle banche cambiano, e qualcuno deve aggiornarle ogni mese.
3. **Responsabilità**: tempo di disponibilità, backup, sicurezza, GDPR con il contratto per il trattamento dei dati, e una persona a cui scrivere quando si rompe.
4. **Conoscenza del settore incorporata**: regole, formati, flussi di lavoro (per esempio le regole di una tesi o di una rivista, o il ritmo di una serata).
5. **Il canale**: il cliente non cerca il software, gli arriva da chi conosce.

Un CRM, un "gestionale semplice", uno strumento per prendere appunti o un link-in-bio generici non passano questo test. SERATA, OMBRA e il biostatistico (116) lo passano.

## 5. Prezzi e disponibilità a pagare

- **Abbonamenti alle piccole imprese:** 29–299 € al mese, a seconda del valore misurabile. Sotto i 20 € al mese servono troppi clienti; sopra i 300 € serve un venditore.
- **Abbandono degli abbonati:** per i SaaS rivolti alle piccole imprese è del 3–5% al mese, cioè il 31–46% l'anno [10]. Con il 4% al mese metà dei clienti se ne va in circa 17 mesi. Per mantenere 250 clienti ne servono circa 10 nuovi al mese solo per restare fermi (stima).

## 6. Conti: quanto costa e quanto rende

| Voce | Costo mensile | Note |
|---|---|---|
| Claude Max | 100–200 $ | Limiti ogni 5 ore e settimanali, cambiati più volte nel 2026 [11] |
| VPS di produzione | 5–40 € | Hetzner CX23: da 3,99 a 5,49 € al mese (IVA esclusa) dal 15/6/2026, dopo due aumenti nel 2026; alcune linee economiche sono esaurite [12] |
| VPS di sviluppo e prova, backup fuori sede | 10–20 € | Stima |
| Dominio, email transazionali, monitoraggio | 0–30 € | Livelli gratuiti fino a un certo volume |
| Merchant of record (Paddle, Lemon Squeezy) | 5% + 0,50 $ a transazione | Incassa, applica l'IVA in oltre 100 Paesi e ti paga; Stripe Managed Payments costa il 3,5% in più dell'elaborazione standard [13] |
| **Totale fisso** | **circa 150–300 € al mese** | Più pubblicità e tempo |

- **Margine lordo:** 85–95%, quindi il voto "margine" è 5. Il problema non è il margine, è il numero di clienti.
- **Fiscale.** I ricavi si sommano al limite di 85 k€ del forfettario, dove hai già circa 60 k€. Se l'attività parte davvero, conviene la SRLS.
  - Il merchant of record semplifica molto l'IVA estera: tu fatturi solo a Paddle o Lemon Squeezy, non a ogni cliente europeo. Da confermare con il commercialista.

## 7. Rischi

1. **Sicurezza.**
   - Secondo il rapporto Veracode 2026, il 44% dei compiti di programmazione svolti dall'AI produce una vulnerabilità della lista OWASP Top 10 [14]. Claude Opus 4.8 supera i test di sicurezza nel 62% dei casi; le falle più comuni sono XSS e log injection.
   - Su 1.400 app create con strumenti di vibe coding, Escape.tech ha trovato 2.038 vulnerabilità gravi e oltre 400 segreti esposti [14].
   - Un'unica falla con dati di clienti significa GDPR, notifiche e fine della fiducia.
2. **Un solo VPS è un solo punto di rottura.** Servono backup fuori sede con un ripristino provato ogni mese e un ambiente di prova separato. Levels fa girare Claude Code sul server di produzione; io non lo farei.
3. **Fornitori che cambiano le condizioni.**
   - Hetzner ha alzato i prezzi due volte nel 2026 [12].
   - Anthropic ha cambiato i limiti di Claude Code più volte [11].
   - Apple blocca alcune app [3].
4. **Abbandono e assistenza.** Con 250 clienti arrivano richieste ogni giorno. Un'assistenza AI basata sulla documentazione ne copre gran parte, non tutte.
5. **Copia in pochi giorni.** Le funzioni di un SaaS generico si replicano con Claude in un weekend: per questo la difendibilità ha voto 1.
6. **Cyber Resilience Act.**
   - Il SaaS puro è in genere **fuori** dal CRA. Restano GDPR e, per aziende più grandi, NIS2 [15].
   - Il software **da installare** (app desktop, self-hosted, plugin) e i server che fanno funzionare un prodotto installato sono **dentro**: obblighi di segnalazione delle vulnerabilità dall'11/9/2026 e conformità piena entro l'11/12/2027 [15].
   - Per evitare la burocrazia conviene vendere servizi web, non software da scaricare.

## 8. Come si trovano i clienti (costo di acquisizione)

- È il collo di bottiglia, e Claude Code non lo tocca. I canali per un solista, dal più adatto alle 5–10 ore a settimana:
  1. **Un canale che hai già**: le discoteche con cui lavori, cioè SERATA.
  2. **Marketplace** come lo Shopify App Store, dove i clienti cercano già. Shopify trattiene lo 0% sul primo milione di dollari e poi il 15%, più il 2,9% sui pagamenti [16]. Però è affollato.
  3. **SEO e pagine generate per ogni ricerca specifica**: lento, 6–12 mesi.
  4. **Partnership** con chi ha già i clienti (biglietterie, software di preventivi, editori).
  5. **Pubblicità e contatti a freddo**: costosi e lunghi da gestire per una persona sola.
- **Esito:** con la variante A (fabbrica) ogni prodotto richiede il suo canale, e con 5–10 ore a settimana se ne regge uno, forse due.

## 9. Come lo costruirei

- **Infrastruttura:**
  - VPS in UE (Hetzner o OVH), con Docker e una piattaforma di deploy open source (per esempio Coolify o Dokploy) oppure Kamal;
  - Postgres con backup giornaliero cifrato fuori sede;
  - Cloudflare davanti, per DNS, TLS e firewall applicativo;
  - un ambiente di prova separato.
- **Claude Code:**
  - lavora su un VPS di sviluppo, non in produzione;
  - in modalità non interattiva (`claude -p`) con una chiave API [17];
  - ciclo: errore in Sentry → l'agente riproduce il bug e scrive la correzione → test → pull request → **la approvi tu** → deploy. Sentry fa già qualcosa di simile con il suo agente basato su Claude (Seer) [17].
- **Sicurezza:**
  - a ogni modifica una revisione di sicurezza automatica e una scansione delle dipendenze;
  - segreti solo nelle variabili d'ambiente;
  - test sulle autorizzazioni (chi vede i dati di chi).
- **Pagamenti:** merchant of record (Paddle o Lemon Squeezy).
- **Testi legali:** termini, privacy, contratto per il trattamento dei dati e cookie.
- **Assistenza:** un'AI sulla documentazione, più email con risposta entro 24 ore.
- **Tempi:** un MVP in 2–4 settimane. A regime 3–5 ore a settimana di manutenzione e assistenza; il resto del tempo va al marketing.

## 10. Perché ora, e quanto dura la finestra

- **A favore:** costruire e mantenere costa una frazione di due anni fa, e una persona sola può gestire un prodotto vero.
- **Contro:** lo stesso vale per tutti. Nel software generico la finestra si sta chiudendo, perché i prezzi scendono e i grandi integrano gli agenti. Resta aperta nei settori in cui i grandi non entrano perché sono piccoli o specifici, e in cui chi conosce il settore ha un canale.
- **Con i modelli del 2027** costruire costerà ancora meno, quindi il vantaggio si sposterà ancora di più su dati, distribuzione e fiducia.

## 11. Voti (variante A, la "fabbrica" senza nicchia)

| Criterio | Peso | Voto | Motivo |
|---|---|---|---|
| Motivazione | 0,20 | 4 | Stima: sei un ingegnere AI e ti attira ciò che si automatizza. Da confermare |
| Vantaggio personale | 0,15 | 3 | Le competenze ci sono, ma senza una nicchia non hai un accesso che gli altri non hanno |
| Dolore | 0,10 | 2 | Senza una nicchia non c'è un dolore preciso |
| Mercato | 0,05 | 5 | Enorme |
| Margine | 0,10 | 5 | 85–95% |
| Validazione | 0,10 | 4 | Si testa con poche centinaia di euro |
| 1 M€ da solo | 0,15 | 2 | Solo il 2–3% arriva a 25 k€ al mese; abbandono del 3–5% al mese; un canale per ogni prodotto |
| Automazione | 0,10 | 4 | Claude Code per la manutenzione, un'AI per l'assistenza |
| Difendibilità | 0,05 | 1 | Si copia in un weekend |
| **Totale** | | **3,35** | **Con motivazione neutra: 3,15** |

## 12. Cosa la ucciderebbe e il test più economico

- **La ucciderebbe:**
  - costruire prima di sapere chi compra;
  - lanciare cinque prodotti in parallelo con 5–10 ore a settimana;
  - una falla di sicurezza con dati di clienti;
  - un abbandono sopra il 6% al mese.
- **Test più economico, valido per qualunque nicchia (300–800 €, 4–6 settimane):**
  1. Scegli la nicchia in cui hai un canale. La prima candidata è la 234 SERATA.
  2. 10 conversazioni con clienti veri, e almeno 3 che pagano in anticipo o firmano una lettera d'intenti prima di scrivere il codice.
  3. MVP con Claude Code in 2–3 settimane, sullo stack del §9.
  4. **GO** se entro 60 giorni dal lancio hai almeno 10 clienti paganti e l'abbandono resta sotto il 5% al mese per i primi 3 mesi. **STOP** se dopo 60 giorni i paganti sono meno di 5.

## Variante F nel dettaglio: comprare invece di costruire

- **I prezzi.** I micro-SaaS piccoli si vendono a circa 2,5–4 volte l'utile annuo del proprietario. Su Acquire.com la mediana è 3,9 volte, e i prezzi pubblicati sono spesso solo richieste [18].
- **Con il tuo limite di perdita (20 k€)** si compra un prodotto da circa 400–600 $ al mese di utile (stima). È piccolo, ma con clienti, dati e canale già presenti.
- **Il lavoro da fare.** Con Claude Code lo migliori e lo porti in UE, in italiano e in altre lingue. Serve una verifica seria: accesso diretto a Stripe, abbandono reale, dipendenza dal venditore.
- **Utilità.** È una buona palestra per imparare acquisizione e abbandono con poco rischio. Da sola non porta a 300 k€.

## Verdetto

- **Come idea a sé ("fabbrica di software in abbonamento"): scartata, 3,35** (motivazione neutra 3,15). Costruire non è più il vantaggio: lo è avere un canale.
- **Come veicolo: sì.** Claude Code su un VPS è il modo giusto, ed economico, per costruire e mantenere da solo:
  - la 234 SERATA, che ha un canale tuo;
  - la 107 e la 116, già in lista;
  - la 208 OMBRA.

  Il criterio di scelta resta la nicchia: un dolore preciso, un canale tuo, dati che si accumulano.

## Fonti

1. https://youmind.com/es-ES/landing/x-viral-articles/claude-code-solo-business-workflow ; https://andrew.ooo/posts/pieter-levels-photo-ai-solo-founder/
2. https://www.youngju.dev/blog/culture/2026-05-14-micro-saas-case-studies-2026-one-person-business-economics-stack-deep-dive-2026 ; https://aiidelist.com/indie-developers/pieter-levels
3. https://9to5mac.com/2026-07-20/report-app-store-added-nearly-as-many-new-apps-in-h1-2026-as-in-all-of-2025/ ; https://thenextweb.com/news/vibe-coding-apple-app-store-surge-crackdown ; https://www.techspot.com/news/113213-apple-app-store-inundated-low-quality-vibecoded-apps.html
4. https://www.deeplearning.ai/the-batch/claude-cowork-plugins-trigger-a-saas-stock-selloff-but-partnerships-lead-to-slight-rebound ; https://www.fool.com/investing/2026/03/27/software-stocks-entered-bear-market-ai-trade/ ; https://www.longangle.com/alts-education/software-ai
5. https://www.businesswire.com/news/home/20260217548274/en/Retools-2026-Build-vs.-Buy-Report-Reveals-35-of-Enterprises-Have-Already-Replaced-SaaS-With-Custom-Software
6. https://byteiota.com/mckinsey-ai-2026-enterprises-are-building-not-buying/
7. https://www.ibec.ie/sfa/news-insights-and-events/news/2026/08/10/small-firms-association-sound-alarm-over-shallow-ai-adoption ; https://thenextweb.com/news/shadow-ai-small-businesses-pax8-survey
8. https://bigideasdb.com/state-of-indie-saas-revenue-2026 ; https://bigideasdb.com/trustmrr-saas-revenue-benchmarks-2026
9. https://dev.to/promptway/he-built-a-flight-simulator-in-three-hours-and-hit-1m-a-year-in-17-days-then-it-went-to-zero-1b1l
10. https://www.shno.co/marketing-statistics/saas-churn-benchmarks-statistics ; https://www.wearefounders.uk/saas-churn-rates-and-customer-acquisition-costs-by-industry-2025-data/
11. https://www.superblocks.com/blog/claude-code-pricing ; https://www.morphllm.com/comparisons/claude-code-vs-codex
12. https://findstack.com/resources/hetzner-price-increase-2026 ; https://privatedevops.com/news/hetzner-june-2026-cloud-price-increase-what-to-do ; https://www.vincentschmalbach.com/hetzner-cheap-cloud-unavailable-price-increases/
13. https://dodopayments.com/blogs/paddle-vs-lemon-squeezy/ ; https://alexcloudstar.com/blog/merchant-of-record-indie-saas-2026/
14. https://sdtimes.com/agentic-security/veracode-finds-ai-generated-code-security-has-barely-improved-since-last-year/ ; https://www.esecurityplanet.com/threats/veracode-finds-ai-generated-code-still-struggles-with-security/ ; https://labs.cloudsecurityalliance.org/research/csa-research-note-ai-generated-code-vulnerability-surge-2026/
15. https://www.dlapiper.com/en/insights/publications/2026/02/cyber-resilience-act-the-fine-line-between-saas-and-digital-products ; https://www.crowell.com/en/insights/client-alerts/eu-cyber-resilience-act-countdown-11-september-2026-incidentvulnerability-reporting-deadline-is-less-than-100-days-away ; https://www.kirkland.com/publications/kirkland-alert/2026/09/the-eu-cyber-resilience-act
16. https://shopify.dev/docs/apps/launch/distribution/revenue-share
17. https://www.virtua.cloud/learn/de/tutorials/claude-code-auf-vps-betreiben ; https://claude.com/es/customers/sentry
18. https://bigideasdb.com/state-of-saas-valuations-2026 ; https://beancount.io/blog/2026/07/11/bootstrapped-saas-valuation-multiples-2026-acquire-com-indie-founders-guide
