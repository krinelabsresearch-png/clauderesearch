# Dropshipping gestito da agenti IA (idea 070)

**Data:** 11 ottobre 2026
**Cosa vede Lorenzo nel dropshipping:** non il singolo prodotto, ma la possibilità di farlo gestire da un **sistema di agenti IA**, così da avere un'attività che gira quasi da sola e lasciargli tempo per sviluppare altro.
**Numeri:** `caccia_vincenti.py` (economia della ricerca dei prodotti vincenti) e `modello.py` (contribuzione per prodotto).

---

## 0. Sintesi

**Cambiando prospettiva, il voto cambia: 3,50, al limite della soglia** (contro il massimo di 3,20 dei singoli prodotti). Il motivo: il vero prodotto diventa il **sistema di agenti**, ed è lì che ci sono la tua motivazione (AI) e il tuo vantaggio (AI engineering + dati + Meta Ads).

Tre cose però vanno dette chiaramente:
1. **Gli agenti abbassano il lavoro, non il CAC.** I margini dei due documenti precedenti restano quelli. Gli agenti contano solo se fanno salire la percentuale di prodotti vincenti e scendere il costo di ogni test.
2. **Non sarà passivo.** Stima realistica: 6–10 settimane per costruirlo, poi **5–10 ore a settimana** di supervisione (approvazioni di spesa, problemi con fornitori e pagamenti, blocchi degli account). Meno di un lavoro, più di una rendita.
3. **Il valore che resta è il sistema, non il negozio.** Lo stesso sistema (ricerca, creatività, pubblicità, assistenza, analisi) serve poi **a KRINÉ**. Anche se il dropshipping rende poco, ne esci con l'infrastruttura del tuo marchio già pronta e collaudata con soldi veri.

**Il tuo vantaggio dati è reale, e c'è solo in UE:** grazie al Digital Services Act, la libreria pubblicitaria di Meta mostra tramite API **tutte** le inserzioni commerciali consegnate in UE, con la **copertura** (persone raggiunte) per età, sesso e Paese. Fuori dall'UE si vedono solo le inserzioni politiche. Un agente che misura ogni giorno quali inserzioni stanno crescendo può individuare i prodotti che scalano **prima che diventino saturi**. È esattamente un lavoro da data scientist, e unisce la direzione "scraping e dati" (046) al commercio online.

---

## 1. Cosa cambia rispetto alle valutazioni precedenti

| Punto | Prima (singolo prodotto) | Ora (sistema di agenti) |
|---|---|---|
| Filtro 5: lavoro continuo | Al limite: senza di te le vendite si fermano | **Passa con riserva:** gli agenti fanno il lavoro ripetitivo, tu supervisioni 5–10 h/settimana |
| Motivazione | 2–4 (prodotti senza scienza) | **4**: costruire agenti è una tua passione; manca la scienza del beauty |
| Vantaggio del founder | 2–3 | **4**: AI engineering, data science, esperienza su Meta, dati UE dalla libreria pubblicitaria |
| Unit economics | LTV/CAC 0,2–0,6 | **Invariati**: gli agenti non cambiano dazi, IVA e prezzo della pubblicità |
| Difendibilità | 1 | **2**: il sistema e i dati storici sono tuoi, ma gli strumenti si stanno diffondendo |

---

## 2. Cosa possono fare gli agenti (e cosa no)

| Area | Automatizzabile | Cosa resta a te | Strumenti |
|---|:--:|---|---|
| Ricerca dei prodotti | Alta | Scegliere tra i 3–5 candidati migliori | Libreria pubblicitaria Meta (API, dati UE), TikTok Creative Center, Google Trends, cataloghi CJ e BigBuy |
| Controllo di conformità | Media | Decidere sui casi dubbi (elettronica, claim) | Regole scritte da te + modello linguistico: categorie vietate, GPSR, claim |
| Negozio e schede prodotto | Alta | Revisione rapida | API di Shopify; Sidekick ora può anche modificare il negozio |
| Creatività (immagini, video, testi) | Alta | Approvare ciò che va online | Generazione di immagini e video; varianti automatiche |
| Pubblicità | Media | **Approvare gli aumenti di budget**, gestire i blocchi | API Marketing di Meta con regole di arresto e di crescita |
| Ordini e fornitori | Alta | Fornitore che sparisce, merce difettosa | AutoDS o CJ (da 20–50 $/mese): ordini automatici e cambio di fornitore |
| Assistenza clienti | Media | Rimborsi, casi difficili, contestazioni dei pagamenti | Agente IA: i fornitori dichiarano fino al 60% di richieste risolte, nella pratica di solito meno (20–50%) |
| Conti e analisi | Alta | Le decisioni | Conto economico giornaliero per prodotto, allarmi su CAC e resi |

### Architettura proposta
```
            ┌────────────── Orchestratore + cruscotto + regole di arresto ──────────────┐
            │                                                                            │
 Ricerca ─► Conformità ─► Negozio ─► Creatività ─► Pubblicità ─► Ordini ─► Assistenza ─► Analisi
 (dati UE      (filtri       (Shopify)   (immagini,     (test,        (CJ/AutoDS)  (agente +    (conto economico,
  Meta Ads)     GPSR/claim)              video, testi)   stop, scala)               tu sui casi   allarmi)
                                                                                     difficili)
            └──── Approvazione umana: nuovi prodotti, budget sopra soglia, rimborsi, blocchi ────┘
```

### Costi mensili del sistema (stima)
| Voce | €/mese |
|---|:--:|
| Shopify + app di ordini automatici | 60–100 |
| Modelli linguistici (API) | 50–200 |
| Generazione di immagini e video | 30–100 |
| Assistenza IA (se si usa uno strumento a pagamento) | 0–100 |
| **Totale** | **~150–500** |

---

## 3. L'economia: tutto si gioca sulla percentuale di vincenti

Le fonti di settore (blog di fornitori, quindi da prendere con cautela) indicano: test da **200–400 € di pubblicità per prodotto**, **5–25% di prodotti vincenti**, finestra di vendita di **~8 settimane** prima della saturazione. Un vincente ha un CAC sotto la metà del prezzo.

**Un vincente tipo** (39,90 €, costo 9 € con spedizione, magazzino UE): restano 20,08 € a ordine prima della pubblicità.

| Spesa al giorno | CAC | Profitto in 2 mesi |
|:--:|:--:|:--:|
| 100 € | 14 € | ~2.600 € |
| 300 € | 16 € | ~4.600 € |
| 500 € | 18 € | ~3.500 € (il CAC sale e mangia il margine) |

**Un ciclo di ricerca da 10 prodotti testati** (1–2 mesi):

| Costo per test | Vincenti | Saldo con scala a 100 €/g | Saldo con scala a 300 €/g |
|:--:|:--:|:--:|:--:|
| 200 € | 5% | −700 € | +300 € |
| 200 € | 10% | +600 € | +2.600 € |
| 200 € | 20% | +3.200 € | +7.200 € |
| 400 € | 5% | −2.700 € | −1.700 € |
| 400 € | 10% | −1.400 € | +600 € |
| 400 € | 20% | +1.200 € | +5.200 € |

**Cosa ci dicono i numeri:**
- Le due leve sono **la percentuale di vincenti** (che sale con una ricerca migliore: i dati UE) e **il costo per test** (che scende con creatività generate e regole di arresto rapide, per esempio stop a 100 € se click e aggiunte al carrello sono bassi). Sono proprio le due cose che un sistema di agenti costruito da te può migliorare.
- Con il 10% di vincenti e test da 200 €, il sistema rende **~0,3–1,5 k€ al mese**. Con il 20%, ~2–4 k€. Non è un reddito che cambia la vita, ma può **pagarsi da solo** mentre lavori ad altro.
- Ordine di grandezza: senza un vantaggio nella selezione (5% di vincenti) si perde denaro, come la maggior parte dei dropshipper.

---

## 4. Rischi

| Rischio | Gravità | Come si gestisce |
|---|:--:|---|
| **Blocco dell'account pubblicitario Meta.** Ci sono segnalazioni di blocchi con agenti IA collegati, e i ricorsi riescono di rado. Il rischio non è l'API in sé: sono le azioni automatiche senza ritmo né controllo umano | Alta | Approvazione umana per pubblicazioni e aumenti di budget, ritmo lento, mai ritentativi immediati dopo un errore. Account di riserva e metodi di pagamento puliti |
| **Meta automatizza tutto da sola.** Obiettivo dichiarato: entro fine 2026 basteranno immagine del prodotto e budget, e Meta farà creatività e pubblico | Media | Rende meno preziosi i tuoi agenti di creatività e pubblicità, ma lascia intatto il vantaggio nella **scelta dei prodotti** e nei dati. Conviene concentrarsi su quella |
| Errori degli agenti (claim illegali, risposte sbagliate ai clienti) | Media | Regole rigide, liste di claim vietati, revisione umana dei nuovi testi |
| Responsabilità legale (GPSR: sei importatore e fabbricante) | Media | Solo categorie a basso rischio: niente cosmetici, elettronica o dispositivi medici |
| Blocchi dei pagamenti (riserve di Shopify o Stripe con picchi di vendite e contestazioni) | Media | Crescita graduale, consegne rapide da magazzino UE |
| Concorrenza di strumenti pronti (AutoDS e simili promettono già "negozi automatici") | Bassa | Il tuo vantaggio non è l'automazione in sé, ma la selezione basata sui dati |

**Canali nuovi da tenere d'occhio:** i negozi Shopify vengono mostrati nelle risposte di ChatGPT, e il traffico da strumenti IA verso Shopify è cresciuto di 8 volte in un anno (dato di Shopify, primo trimestre 2026). Il checkout dentro ChatGPT invece è stato ridimensionato a marzo 2026. È un canale di scoperta in crescita, ma oggi non sostituisce la pubblicità.

---

## 5. Piano a fasi, con soglie fissate prima

| Fase | Durata | Budget | Cosa si fa | Soglia per passare alla fase dopo |
|---|---|:--:|---|---|
| **1. Agente di ricerca senza spendere in pubblicità** | 4–6 settimane | ≤ 300 € | Raccolta quotidiana dalla libreria pubblicitaria UE (copertura per inserzione e prodotto), modello che prevede quali prodotti stanno per scalare. **Verifica a posteriori:** le previsioni di 4 settimane fa si sono avverate? | Tra i primi 20 candidati del modello, almeno il 30% ha continuato a crescere nelle 4 settimane successive (contro una media da misurare) |
| **2. Negozio di prova + 10 test** | 6–8 settimane | ≤ 2.500 € di pubblicità + ~500 € di strumenti | Negozio con agenti per creatività, pubblicità con regole automatiche, ordini e assistenza | Costo medio per test ≤ 250 €; almeno 1 vincente su 10 con profitto netto positivo; tue ore ≤ 8 a settimana |
| **3. Scala e riuso** | Continuo | Autofinanziato | Scalare i vincenti; **riusare il sistema per KRINÉ** (creatività, pubblicità, assistenza, analisi) | Il sistema si paga da solo oppure è pronto per il lancio di KRINÉ |

**Regola di arresto:** se dopo 10 test (≤ 3.000 € spesi) non c'è nessun vincente, si chiude il negozio. Il sistema si tiene per KRINÉ. La perdita massima resta molto sotto i 20 k€.

**Perché la fase 1 è la più importante:** si verifica a costo quasi zero l'unica ipotesi che fa la differenza, cioè se i tuoi dati scelgono prodotti migliori della media. Se la risposta è no, si risparmiano i 3.000 € di test.

---

## 6. Scheda pesata (idea 070)

| Criterio | Peso | Voto | Nota |
|---|:--:|:--:|---|
| Motivazione | 20% | 4 | Costruire agenti IA (da confermare) |
| Vantaggio del founder | 15% | 4 | AI engineering, data science, Meta Ads, dati UE |
| Dolore e disponibilità a pagare | 15% | 3 | I prodotti si scelgono dove c'è domanda dimostrata |
| Mercato | 10% | 4 | E-commerce UE grande e in crescita |
| Unit economics | 10% | 2 | Margini sottili, dipendono dalla percentuale di vincenti |
| Costo della validazione | 10% | 4 | Fase 1 ≤ 300 €, fase 2 ≤ 3 k€ |
| Scalabilità | 10% | 4 | Vende in tutta l'UE; il sistema scala senza di te |
| Difendibilità | 5% | 2 | Sistema e dati storici tuoi, ma strumenti in diffusione |
| Tempo al primo euro | 5% | 3 | 6–10 settimane di costruzione |
| **Totale** | | **3,50** | **Passa al limite**: se le unit economics si rivelano 1, scende a 3,40 |

---

## 7. Domande per te
1. **Quanto tempo vuoi che resti a te** una volta a regime? 5–10 ore a settimana ti va bene?
2. **Obiettivo:** il sistema deve **rendere** (autofinanziarsi e generare reddito) o è soprattutto **l'infrastruttura per KRINÉ** collaudata con soldi veri? Cambia quanto spingere la fase 2.
3. **Partiamo dalla fase 1** (agente sui dati UE della libreria pubblicitaria, ≤ 300 €)? Posso preparare l'architettura e il primo prototipo del raccoglitore di dati e del modello di previsione.

---

## 8. Righe per backlog e log
```
| 070 | Dropshipping gestito da agenti IA (il prodotto è il sistema; riusabile per KRINÉ) | 3,50 | 1 → fase 1: agente di ricerca sui dati UE della libreria pubblicitaria (≤ 300 €) |
```
```
| 2026-10-11 | Dropshipping riletto come "sistema di agenti IA" (070): 3,50 | Gli agenti non cambiano i margini ma le due leve decisive (percentuale di vincenti, costo per test); vantaggio dati solo in UE (DSA: copertura di tutte le inserzioni); il sistema si riusa per KRINÉ. Vedi `idee/dropshipping/agenti-ia.md` | Fase 1: verificare a posteriori se il modello sceglie prodotti migliori della media |
```

---

## 9. Fonti
- Meta automatizza la pubblicità: [exchange4media](https://www.exchange4media.com/digital-news/meta-aims-to-fully-automate-advertising-with-ai-by-2026-144037.html) · [Influencer Marketing Hub](https://influencermarketinghub.com/meta-radical-plan-to-reinvent-digital-ads-with-ai/) · [Social Samosa](https://www.socialsamosa.com/news-2/meta-pushes-toward-fully-automated-advertising-future-9330538)
- Libreria pubblicitaria UE (DSA): [AdLibrary, repository DSA](https://adlibrary.com/posts/eu-dsa-ad-repositories-developers) · [AdManage, API](https://admanage.ai/blog/facebook-ads-library-api) · [Who Targets Me](https://whotargets.me/en/?p=533) · [GitHub, client AdsLibrary](https://gitblind.noratr.app/soxoj/AdsLibrary)
- Shopify e agenti: [Coalition Technologies, Winter '26](https://coalitiontechnologies.com/blog/shopify-editions-winter-26) · [ChatterGo, Sidekick](https://www.chattergo.com/blog/shopify-sidekick-deep-dive-from-chatbot-to-agentic-copilot) · [Presta](https://wearepresta.com/shopify-sidekick-features-2026-the-merchants-guide-to-agentic-commerce)
- Commercio tramite agenti: [Modern Retail](https://www.modernretail.co/?p=154880) · [Naturaily](https://naturaily.com/blog/agentic-commerce-shopify-guide) · [Ringly, Instant Checkout](https://www.ringly.io/blog/openai-instant-checkout-agentic-commerce-protocol)
- Assistenza IA: [eesel, Gorgias AI](https://eesel.ai/blog/gorgias-ai-support-agent) · [Macha, prezzi Gorgias](https://www.getmacha.com/blog/gorgias-pricing-explained)
- Strumenti di dropshipping: [PricingSaaS, AutoDS](https://pricingsaas.com/companies/autods) · [Trendtrack, recensione AutoDS](https://www.trendtrack.io/it/blog-post/recensione-autods-2026-e-un-buono-strumento) · [Rework, strumenti IA](https://resources.rework.com/tools/ai-tools/best-ai-tools-for-dropshipping-2026)
- Test e prodotti vincenti: [Funnelish](https://funnelish.com/blog/how-to-test-dropshipping-products) · [Yakkyofy](https://yakkyofy.com/finding-winning-products-for-your-dropshipping-business/) · [Closo](https://closo.co/blogs/dropshipping/best-items-to-dropship) · [Trendtrack](https://www.trendtrack.io/blog-post/how-to-use-ai-for-dropshipping)
- Blocchi degli account: [Porter Metrics](https://portermetrics.com/en/tutorial/meta-ads-mcp-ban/) · [Blend](https://blend-ai.com/mcp/learn/will-mcp-suspend-meta-ads-account) · [Leadsie](https://www.leadsie.com/blog/recover-disabled-facebook-ad-account) · [Vondran Legal](https://www.vondranlegal.com/meta-s-oversight-board-is-raising-questions-about-account-bans-ai-and-the-right-to-a-meaningful-appeal)
