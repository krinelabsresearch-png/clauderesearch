# Dropshipping: UE, USA, Canada o America Latina?

**Data:** 11 ottobre 2026 (riscritto dopo la precisazione di Lorenzo: la domanda riguarda **solo il dropshipping**)
**Domanda:** per il dropshipping, vendere in UE è la scelta più conveniente? E se vendessi negli USA, in Canada o in America Latina?
**Risposta breve:** nessun mercato è una scorciatoia. **USA e Italia si equivalgono**: negli USA si incassa di più per ordine, ma la pubblicità costa il doppio. Gli USA convengono solo con prodotti che reggono un prezzo più alto del ~30%. Per imparare e testare, **l'Italia (e l'UE) costa la metà**. L'America Latina ha un modello che funziona (pagamento alla consegna), ma richiede presenza e un socio sul posto. Il Canada è piccolo: è un'aggiunta agli USA.

---

## 1. Il confronto

| | **Italia / UE** | **USA** | **Canada** | **America Latina** (Messico, Colombia, Brasile) |
|---|---|---|---|---|
| **Dalla Cina diretto** | +3 € di dazio UE (dal 1/7/2026) + 2 € di contributo italiano (dal 1/12/2026, da verificare) | Esenzione da 800 $ sospesa dal 29/8/2025, a tempo indeterminato da giugno 2026, abolita per legge dal 1/7/2027. Dazi sulla Cina ~20% complessivi (tregua fino al 10/11/2026, scenario instabile) + importazione formale per ogni pacco | Soglie d'esenzione basse (da verificare) | **Messico:** 33,5% sui pacchi da Paesi senza accordi (dal 15/8/2025). **Brasile:** 20–60% più l'imposta statale ICMS (dati non ufficiali) |
| **L'alternativa che funziona** | Magazzini UE (CJ in Germania e Polonia, BigBuy in Spagna): consegna in 2–5 giorni | Fornitori con magazzino negli USA (CJ USA, Spocket; Blanka per i cosmetici) | Spedizione da magazzini USA o canadesi | **Pagamento alla consegna con fornitori locali** (Dropi: ~2.200 negozi). Verso il Messico, dagli USA i pacchi fino a 50 $ sono esenti (T-MEC) |
| **Imposte sul prezzo** | IVA 22% compresa nel prezzo | **Niente IVA.** La sales tax scatta solo oltre le soglie di ogni stato (in molti 100.000 $ di vendite l'anno) | GST/HST con registrazione oltre una soglia di vendite | Regimi locali complessi |
| **Pubblicità (CPM Meta)** | Italia ~7–8 € + 3% di location fee dal 1/7/2026 | **16–23 $** | Dato non trovato | **3–12 $** (40–60% meno dei mercati anglofoni) |
| **Pagamenti e resi** | Carte; recesso di 14 giorni | Carte; contestazioni dei pagamenti (chargeback) frequenti; i clienti si aspettano resi a 30 giorni e consegne veloci | Come gli USA | **Contrassegno:** il 15–35% delle consegne non va a buon fine (stime di fonti non indipendenti) |
| **Concorrenza** | Media | **Massima**: è il mercato più battuto dai dropshipper di tutto il mondo | Media | In crescita |
| **Cosa serve a te, dall'Italia** | Niente di nuovo | Una società non è obbligatoria; Stripe e Shopify funzionano. Assistenza in inglese e su un altro fuso orario | Etichette e assistenza anche in francese | **Colombia:** il codice fiscale (RUT) per gli stranieri richiede documenti apostillati e tradotti; il conto bancario richiede un visto oltre i 90 giorni e la presenza in filiale. **In pratica serve un socio locale** |
| **Cosmetici (sieri)** | Selfnamed: legale, ma ~2–9 € a ordine | Blanka: legale e semplice (piccole imprese esenti dalla registrazione FDA, **tranne la zona occhi**), ma CAC doppio | Blanka + notifica a Health Canada + etichetta bilingue | Registrazione locale obbligatoria (ANVISA in Brasile, COFEPRIS in Messico): no |

---

## 2. I numeri: stesso prodotto, Italia contro USA

Prodotto generico con costo di 8 € da magazzino locale, logistica 5,70 €, stesso tasso di conversione nei due mercati (`dropshipping/modello_sieri.py`):

| Mercato e prezzo | Contribuzione per ordine | CAC con conversione 2% | CAC con conversione 3% | Contribuzione ÷ CAC (conv. 2%) |
|---|:--:|:--:|:--:|:--:|
| Italia, 34,90 € | 12,56 € | 41,20 € | 27,47 € | 0,30 |
| USA, 34,90 € (~40 $) | 18,17 € | 85,00 € | 56,67 € | 0,21 |
| USA, 44,90 € (~52 $) | 27,38 € | 85,00 € | 56,67 € | 0,32 |

**Come leggerli:**
- Negli USA **l'assenza di IVA** fa incassare il 45% in più a parità di prezzo, ma **la pubblicità costa il doppio**. Allo stesso prezzo l'Italia rende di più; gli USA tornano in pari solo con un prezzo più alto del ~30%, che lì il cliente accetta più spesso.
- **Il vantaggio vero degli USA è la scala**, non il margine: un prodotto che funziona può vendere 5–10 volte di più. Ma ogni test costa il doppio.
- Per **imparare e testare**, ogni euro di pubblicità in Italia compra il doppio dei dati.

---

## 3. Raccomandazione per il dropshipping

| Mercato | Quando ha senso | Verdetto |
|---|---|---|
| **Italia / UE** | Per i test e per imparare: dati a metà prezzo. Con magazzino UE, non dalla Cina | **Primo mercato** |
| **USA** | Solo dopo aver trovato un prodotto che regge un prezzo premium, con un fornitore che ha già il magazzino negli USA. Pubblicità e test costano il doppio | **Secondo passo**, non punto di partenza |
| **Canada** | Come estensione degli USA, con gli stessi fornitori | Aggiunta |
| **America Latina** | Il modello con pagamento alla consegna funziona, ma è lavoro operativo quotidiano (conferme degli ordini, consegne fallite) e richiede presenza o un socio locale. È contro i tuoi filtri 5 e 6 | **No**, salvo un socio sul posto (es. Alberto o un contatto locale) |

**In sintesi:** cambiare mercato non risolve i problemi di fondo del dropshipping (margini sottili, nessuna difendibilità), visti nelle due valutazioni. Sposta solo l'equilibrio tra prezzo e costo della pubblicità.

---

## 4. Nota sul marchio KRINÉ (dalla versione precedente)
Se un giorno la domanda riguardasse KRINÉ e non il dropshipping, valgono due punti già emersi:
- negli USA il piroctone non è ammesso come antiforfora (lì un antiforfora è un farmaco da banco, monografia 21 CFR 358, da verificare);
- negli USA le prostaglandine per ciglia restano legali, quindi la finestra di mercato di KRINÉ Lash esiste solo in UE e in Canada.

---

## 5. Fonti
- USA: [AP via Coeur d'Alene Press](https://cdapress.com/news/2025/aug/29/duty-free-no-more-parcels-worth-under-800-no-longer-qualify-for-a-us-tariff-exemption/) · [Thompson Hine, regole CBP 2026](https://www.thompsonhinesmartrade.com/2026/06/cbp-issues-interim-final-rules-indefinitely-suspending-the-de-minimis-exemption-for-imports/) · [China Briefing, dazi USA–Cina](https://china-briefing.com/news/us-china-tariff-rates-2025) · [EY, tregua di novembre 2025](https://taxnews.ey.com/news/2025-2247-white-house-issues-executive-order-formalizing-trade-truce-with-china) · [GoComet](https://www.gocomet.com/blog/understanding-us-china-tariff-rates/)
- UE e Italia: vedi le fonti di `dropshipping/valutazione-10-prodotti.md`
- Messico: [Bloomberg Tax](https://news.bloombergtax.com/daily-tax-report/mexico-raises-import-taxes-on-online-purchases-from-shein-temu) · [The Logistics World](https://thelogisticsworld.com/actualidad-logistica/mexico-lleva-al-33-5-el-impuesto-a-importaciones-por-paqueteria/) · [Bringgoship, soglie T-MEC](https://bringgoship.com/en/blog/shein-temu-tax-mexico) · [FreightWaves](https://www.freightwaves.com/?p=566652)
- Brasile: [Goods Across Borders](https://goodsacrossborders.com/posting/send/cosmetics-commercial/to/brazil) · [Freyr, ANVISA](https://cosmetics.freyrsolutions.com/cosmetics-regulatory-services-brazil)
- Colombia e Dropi: [Portafolio](https://www.portafolio.co/innovacion/dropshipping-una-alternativa-a-la-alta-demanda-del-e-commerce-560125) · [Andrey Business, Dropi](https://www.andreybusiness.com/blog/dropi-latam-dropshipping-colombia-mexico-ecuador-peru) · [Accounter, RUT](https://accounter.co/noticias/actualidad/titulares/el-parto-de-obtener-un-registro-unico-tributario) · [Expat.com, banche in Colombia](https://www.expat.com/es/guia/america-del-sur/colombia/13930-bancos-en-colombia.html) · [CIJUF](https://cijuf.org.co/sites/cijuf.org.co/files/documentos_interes/FLASH%20412.pdf)
- Canada: [Registrar Corp](https://www.registrarcorp.com/blog/cosmetics/cosmetic-regulations/import-sell-us-cosmetic-products-in-canada/) · [BorderBuddy](https://borderbuddy.com/canada-imports/cosmetics)
- Pubblicità: [Adligator, CPM per Paese](https://adligator.com/blog/meta-ads-cpm-by-country-benchmarks) · [Adamigo](https://www.adamigo.ai/blog/meta-ads-cpm-cpc-benchmarks-by-country-2026) · [MediaPost, location fee Meta](https://www.mediapost.com/publications/article/413378/meta-passes-eu-digital-services-tax-to-advertisers.html)
- Cosmetici USA: [Registrar Corp, esenzioni MoCRA](https://www.registrarcorp.com/blog/cosmetics/mocra/mocra-exemptions/) · [Blanka, FAQ](https://faq.blankabrand.com/en/articles/4879945-what-is-blanka)
