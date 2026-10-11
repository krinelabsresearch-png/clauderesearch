# Dropshipping: valutazione di 10 prodotti (051–060)

**Data:** 11 ottobre 2026
**Metodo:** stessi filtri eliminatori e stessa scheda pesata di `02-criteri-valutazione.md`; modello economico comune in `modello.py` (stesse commissioni del modello KRINÉ).
**Attenzione:** i costi dei prodotti dai fornitori sono **stime** (fasce tipiche di AliExpress, CJdropshipping e BigBuy), da confermare con preventivi prima di qualsiasi test. Prezzi dei concorrenti, regole e dati di mercato hanno la fonte in fondo.

---

## 0. Sintesi

| ID | Prodotto | Contribuzione 1° ordine | CAC stimato | LTV/CAC base | Scheda | Esito |
|---|---|:--:|:--:|:--:|:--:|---|
| 052 | Filtro doccia + cartucce | 14,60 € | 44 € | 0,47 | **3,20** | In attesa: solo come parte del "kit cuoio capelluto" |
| 057 | Pressurizzatore palline da padel | 11,12 € | 40 € | 0,31 | 3,15 | In attesa: piace, ma il problema è piccolo |
| 058 | Registratore vocale AI (tipo Plaud) | 30,62 € | 80 € | 0,38 | 3,15 | Scartato come dropshipping; nasce l'idea 061 |
| 055 | Maschera LED viso | 39,07 € | 100 € | 0,39 | 3,15 | **Scartata (filtro 3: dispositivi medici)** |
| 056 | Strisce sbiancanti PAP (marchio proprio) | 12,98 € | 40 € | 0,58 | 3,05 | In attesa: è il test di WHITECORE 2.0, non dropshipping |
| 051 | Spazzola massaggiante per cuoio capelluto | 5,91 € | 29 € | 0,21 | 2,85 | Scartata da sola; utile come accessorio |
| 053 | Federa in seta di gelso | 13,42 € | 50 € | 0,32 | 2,80 | Scartata |
| 054 | Piegaciglia riscaldato | 10,99 € | 40 € | 0,29 | 2,80 | Scartato |
| 060 | Nastro per la bocca (sonno) | 5,15 € | 29 € | 0,45 | 2,75 | **Scartato (prove deboli, rischi segnalati)** |
| 059 | Cubi a compressione da viaggio | 8,98 € | 40 € | 0,24 | 2,60 | Scartati |

**In una frase:** nessuno dei 10 prodotti passa la soglia di 3,5. Con la pubblicità a pagamento nessuno ripaga il costo di acquisizione nello scenario base (LTV/CAC tra 0,21 e 0,58, contro l'1,77 di KRINÉ Scalp).

**Le tre lezioni:**
1. **Nel 2026 il dropshipping dalla Cina verso l'Italia costa di più.** Dal 1° luglio 2026 c'è il dazio UE fisso di 3 € a pacco, e dal 1° dicembre 2026 (data da confermare) si aggiunge il contributo italiano di 2 €. Su un prodotto da 15–30 € questi 5 € si mangiano un terzo del margine. Conviene il magazzino UE, ma questo vuol dire comprare scorte, quindi non è più dropshipping puro.
2. **Reggono solo i prodotti che si ricomprano** (filtri, strisce): è la stessa lezione di KRINÉ. I prodotti che si comprano una volta sola, con un CAC di 30–100 €, non stanno in piedi senza traffico gratuito.
3. **Manca ciò che ti motiva.** Il dropshipping vende prodotti di altri, senza scienza dietro e con difendibilità vicina a zero (voto 1 o 2 su tutti e 10). Non soddisfa "la scienza dietro il prodotto", la prima cosa che ti accendeva in KRINÉ.

**Dove il dropshipping può servire:** non come business principale, ma come **strumento al servizio di KRINÉ**: un "kit cuoio capelluto" (filtro doccia + spazzola) venduto allo stesso pubblico di KRINÉ Scalp, per misurare il CAC con acquisti veri e costruire una lista di clienti prima del lancio di marzo 2027. Dettagli al capitolo 6.

---

## 1. Cosa cambia nel 2026 per chi fa dropshipping in Italia

| Regola | Cosa dice | Effetto sul dropshipping |
|---|---|---|
| **Dazio UE sui piccoli pacchi** | Dal 1/7/2026 sparisce l'esenzione sotto i 150 €. Nuovo dazio fisso di **3 € per voce doganale** nel pacco (3 magliette = 3 €; magliette + orologio = 6 €), temporaneo fino al regime definitivo (indicato al 2028). L'IVA si calcola anche sul dazio | +3 € a ordine dalla Cina, di più con i bundle di prodotti diversi |
| **Contributo italiano di 2 €** | Legge di bilancio 2026: 2 € per ogni spedizione extra UE fino a 150 €, B2C compreso, con o senza IOSS. Più volte rinviato; l'ultima fonte trovata (DL 162/2026) lo fissa al **1/12/2026**. **Da verificare** in Gazzetta Ufficiale o con l'Agenzia delle Dogane | +2 € a ordine. Nel modello è incluso (ipotesi prudente) |
| **Diritti di gestione UE** | Il nuovo codice doganale UE introduce anche un diritto di gestione per i piccoli pacchi extra UE. **Importo e data non verificati** | Ulteriore costo da monitorare |
| **GPSR (Reg. UE 2023/988)** | Ogni prodotto venduto nell'UE deve avere un operatore economico stabilito nell'UE. Se vendi col tuo marchio un prodotto importato dalla Cina, **sei tu l'importatore e anche il "fabbricante"**. Ogni scheda prodotto deve indicare fabbricante, responsabile UE e avvertenze; va aggiornata a ogni cambio di fornitore | Responsabilità legale tua; serve un'assicurazione RC prodotto; cambiare fornitore spesso diventa costoso |
| **Elettronica (RAEE e pile)** | Chi vende a distanza apparecchi elettrici a consumatori italiani deve iscriversi come produttore (Registro AEE) e aderire a un consorzio. Per le batterie vale il Regolamento UE 2023/1542 | Costi fissi e burocrazia per 054, 055 e 058 |
| **Cosmetici** | Servono una persona responsabile nell'UE, un PIF con valutazione della sicurezza e la notifica CPNP **prima** della vendita | **Non si possono fare in dropshipping dalla Cina.** Le strisce PAP (056) richiedono un marchio proprio con scorte nell'UE |
| **Dispositivi senza scopo medico (MDR, Allegato XVI)** | Il Reg. 2022/2347 classifica in **classe IIb** le apparecchiature che emettono radiazioni elettromagnetiche ad alta intensità per trattare la pelle; serve un organismo notificato. I periodi transitori valgono solo per i prodotti già sul mercato prima del 22/6/2023 | Rischio forte per le maschere LED (055). Se una maschera LED a bassa potenza rientri o no nell'"alta intensità" resta da chiarire |
| **Recesso di 14 giorni** | Il consumatore può restituire il prodotto senza motivo | Con la spedizione dalla Cina un reso costa più del prodotto: di solito si rimborsa e basta (nel modello: voce "resi") |

**Il quadro di mercato.** Le fonti, quasi tutte blog di fornitori, concordano su un ordine di grandezza: solo il **10–20% dei negozi** arriva a un utile stabile, e il margine netto di chi regge è del **15–20%**. La causa principale dei fallimenti è la cassa, non l'assenza di vendite. Sui siti nuovi la conversione è spesso **sotto lo 0,5%**.

---

## 2. Ipotesi comuni del modello (`modello.py`)

| Voce | Valore | Nota |
|---|---|---|
| IVA | 22% | Prezzi al pubblico IVA inclusa |
| Pagamento | 1,9% + 0,25 € | Come nel modello KRINÉ |
| Assistenza clienti | 3% del netto | Come nel modello KRINÉ |
| Dogana dalla Cina | 3 € (dazio UE) + 2 € (contributo IT) | Da magazzino UE: 0 € a ordine (il dazio si paga sulle scorte, già incluso nel costo) |
| Resi e rimborsi | 3–15% del netto, secondo il prodotto | Più alti per elettronica e tessile |
| CPC su Meta in Italia | 0,60 / **0,80** / 1,00 € | CPM ~7–8 € con CTR ~1% (benchmark 2026 non verificato alla fonte primaria) |
| Conversione della pagina | 0,8% (sopra i 100 €) – 2,8% (sotto i 20 €) | Ipotesi da principiante con pagina curata |
| CAC | CPC ÷ conversione | |
| LTV a 12 mesi | contribuzione del 1° ordine + riordini attesi × contribuzione del riordino | Riordini solo sui consumabili |
| Scenario "ottimizzato" | CPC 0,60 €, conversione ×1,5, carrello +25% con bundle | Ciò che riesce a chi ha creatività vincenti |

---

## 3. I 10 prodotti

Ho scelto i 10 prodotti in modo da coprire i tuoi territori: **beauty senza cosmetici** (051, 052, 053, 054, 055), **beauty con cosmetici** (056), **le tue passioni** (padel 057, AI 058, viaggi 059) e **un trend del benessere** (060).

### 051 · Spazzola massaggiante per cuoio capelluto
- **Perché in lista:** stesso pubblico di KRINÉ Scalp; non è un cosmetico, quindi niente PIF né CPNP.
- **Mercato:** prodotto da 5–10 € su Amazon (stima); nessuna differenza tecnica possibile.
- **Economia:** 16,90 € di prezzo, 5,91 € di contribuzione da magazzino UE. Per ripagare il CAC servirebbe una conversione del 13,5%: impossibile.
- **Rischi:** quasi nessuno sul piano normativo; il problema è solo economico.
- **Verdetto:** **scartata da sola, utile come accessorio** (regalo o bundle con il filtro doccia e, più avanti, con KRINÉ Scalp).

### 052 · Filtro doccia + cartucce di ricambio
- **Perché in lista:** acqua dura e cloro sono un fastidio vero per capelli e cuoio capelluto; le cartucce si ricomprano ogni 2–3 mesi.
- **Mercato:** in Italia 883 comuni hanno acqua molto calcarea (Roma e Bologna tra le grandi città). Il modello USA è Jolie: abbonamento da 148 $ l'anno, oltre 3.500 abbonati. Le stime del mercato dei filtri premium non concordano (195 M$ nel 2025 secondo una fonte, molto di più secondo altre).
- **Il punto scientifico, decisivo per un marchio trasparente:** **i filtri doccia non tolgono il calcare.** In un test di laboratorio la durezza dell'acqua non è calata, e uno dei produttori ammette che "nessun filtro doccia rimuove calcio e magnesio". Tolgono il cloro (vitamina C, KDF) e alcuni metalli. Le prove che l'acqua dura rovini i capelli sono deboli. Quasi tutto il mercato promette "acqua addolcita": un marchio onesto può dire solo **"toglie il cloro, non il calcare"**. È un messaggio più debole, ma coerente con il tuo stile "#HideNothing".
- **Economia:** kit a 39,90 €, contribuzione 14,60 €; cartuccia a 14,90 € con ~1,6 riordini l'anno. LTV/CAC 0,47 nello scenario base, **1,10 in quello ottimizzato**: il migliore dopo le strisce PAP.
- **Rischi:** materiali a contatto con l'acqua; claim da tenere strettamente sul cloro; resi per raccordi non compatibili.
- **Verdetto:** **in attesa (3,20).** Da solo non basta, ma è il miglior candidato per un "kit cuoio capelluto" collegato a KRINÉ.

### 053 · Federa in seta di gelso (22 momme)
- **Perché in lista:** beauty senza formule; meno attrito per capelli e pelle; scontrino medio alto.
- **Mercato:** ~1,8 Md$ nel mondo (due stime simili, di fonti commerciali). Slip la vende a 115–120 $ e incassa ~8,9 M$ in 6 mesi (stima Particl). Su Amazon le federe economiche costano 20–30 € (stima).
- **Economia:** 44,90 €, contribuzione 13,42 €, LTV/CAC 0,32 (0,78 nello scenario ottimizzato).
- **Rischi:** fornitori che spacciano raso di poliestere per seta (servono controlli sul campione); etichetta di composizione obbligatoria (Reg. UE 1007/2011); resi alti sul tessile.
- **Verdetto:** **scartata (2,80).** Funziona solo con un marchio di lusso già affermato, cioè l'opposto del dropshipping.

### 054 · Piegaciglia riscaldato ricaricabile
- **Perché in lista:** collegato alla futura linea KRINÉ Lash, senza cosmetici.
- **Mercato:** in Italia costa 10–40 € (MediaWorld 29,99–39,99 €, Unieuro 29,99 €, offerte Amazon sotto i 10 €).
- **Economia:** 29,90 €, contribuzione 10,99 €, LTV/CAC 0,29.
- **Rischi:** elettronica con batteria (RAEE, pile, marcatura CE); scotta vicino all'occhio; difetti e resi.
- **Verdetto:** **scartato (2,80).** Prezzo di riferimento troppo basso per i costi fissi dell'elettronica.

### 055 · Maschera LED viso
- **Perché in lista:** è il "beauty tech" che va di moda; scontrino alto; tecnologia (ti motiva).
- **Mercato:** 270–320 M$ nel mondo (stime che non concordano). Prezzi: Nanoleaf 149,99 €, CurrentBody fino a 469 $.
- **Economia:** 149 €, contribuzione 39,07 €, ma CAC stimato a 100 € (pochi comprano a freddo un oggetto da 149 €). LTV/CAC 0,39 (0,98 nello scenario ottimizzato).
- **Rischi:** **Allegato XVI del Regolamento sui dispositivi medici** (possibile classe IIb con organismo notificato); sicurezza fotobiologica per gli occhi; resi alti. Una maschera cinese generica difficilmente ha la documentazione per reggere un controllo, e con il GPSR **la responsabilità sarebbe tua**.
- **Verdetto:** **scartata (filtro 3).** Il voto di 3,15 conta poco: il rischio normativo da solo basta a escluderla.

### 056 · Strisce sbiancanti PAP (marchio proprio, scorte nell'UE)
- **Perché in lista:** è la versione più economica di WHITECORE 2.0: si vende davvero e si misurano CAC e riacquisto.
- **Mercato:** Hismile vende le strisce PAP anche da Kruidvat; un fornitore cinese offre strisce PAP a 2,50–3,00 $ la scatola franco fabbrica, dichiarando CPSR e GMP (**da verificare**: non basta per vendere nell'UE).
- **Non è dropshipping:** è un cosmetico. Servono persona responsabile UE, valutazione della sicurezza, PIF e notifica CPNP, quindi ~3,5 k€ di costi fissi (stima) e scorte in un magazzino UE.
- **Economia:** 29,90 €, contribuzione 12,98 €, ~0,8 riordini l'anno. LTV/CAC 0,58 nello scenario base e **1,33 in quello ottimizzato: il migliore dei 10**.
- **Rischi:** il tetto di efficacia del PAP resta (critica strutturale di WHITECORE); Amazon è pieno di strisce PAP a basso prezzo.
- **Verdetto:** **in attesa (3,05).** Ha senso solo se decidi di tenere viva WHITECORE 2.0 (domanda aperta n. 5 del dossier).

### 057 · Pressurizzatore per palline da padel
- **Perché in lista:** il padel è una tua passione e lo conosci da giocatore. In Italia ci sono 10.352 campi (giugno 2026) e 1,5–2 milioni di giocatori (stime diverse).
- **Mercato:** prezzi da 20 a 90 € (Tubo Plus 20–40 €, Bounce Padel X4 89,90 €, Pascal Box di Bullpadel ~60 €); professionali per club da 700 a 1.500 €. Lo vende anche Decathlon.
- **Economia:** 34,90 €, contribuzione 11,12 € (è ingombrante: la spedizione pesa), LTV/CAC 0,31.
- **Rischi:** **Pascal Box ha brevetti**: alcune copie cinesi potrebbero violarli. Inoltre il dolore è piccolo: un tubo di palline nuove costa pochi euro.
- **Verdetto:** **in attesa (3,15), ma debole.** Motivazione alta, problema da "nice to have". Potrebbe tornare utile dentro un progetto padel più ampio (territorio T3).

### 058 · Registratore vocale AI (tipo Plaud)
- **Perché in lista:** AI (la tua passione); mercato dimostrato: Plaud stima ~250 M$ di ricavi annualizzati a settembre 2025 (metà hardware e metà abbonamenti), oltre 1 milione di pezzi venduti. NotePin a 169,90 € nell'UE.
- **Economia del clone:** 109 €, contribuzione 30,62 €, CAC 80 €, LTV/CAC 0,38.
- **Il problema vero:** in dropshipping **vendi l'AI di qualcun altro**. App, trascrizione e cloud sono del fornitore, spesso con server fuori dall'UE: è un problema di GDPR e di fiducia proprio per i clienti a cui serve (professionisti, riunioni). E il ricavo ricorrente (l'abbonamento) va al fornitore, non a te.
- **Verdetto:** **scartato come dropshipping (3,15).** La versione interessante è un'altra idea: **061, hardware generico + software tuo** (trascrizione in italiano, dati nell'UE, verticale per una professione). È hardware più SaaS, non dropshipping: va valutata a parte.

### 059 · Cubi a compressione da viaggio
- **Perché in lista:** viaggi (tua passione); prodotto semplice, nessuna norma particolare.
- **Mercato:** saturo su Amazon, prezzi bassi, nessuna differenza possibile.
- **Economia:** 29,90 €, contribuzione 8,98 € (voluminoso), LTV/CAC 0,24.
- **Verdetto:** **scartati (2,60).** Il voto più basso: niente scienza, niente marchio, niente riacquisto.

### 060 · Nastro per la bocca per il sonno
- **Perché in lista:** trend del biohacking del sonno; consumabile mensile; costo bassissimo.
- **Prove:** una revisione sistematica del 2025 (PLOS One, 10 studi, 213 pazienti) trova benefici solo in 2 studi su 10, nell'apnea lieve, mentre 4 studi su 10 segnalano un rischio di asfissia. L'interesse di ricerca negli USA ha toccato il massimo a fine dicembre 2024 e poi è calato.
- **Rischi:** se si promette "riduce il russamento" diventa un dispositivo medico; un marchio "scientifico e trasparente" non può venderlo onestamente.
- **Verdetto:** **scartato (2,75).** In contrasto con l'identità del marchio.

---

## 4. Tabella economica completa

Contribuzione per ordine dopo IVA, prodotto, spedizione, dogana, pagamento, assistenza e resi.

| ID | Prezzo | Contr. dalla Cina | Contr. da magazzino UE | CAC base | LTV 12 mesi | LTV/CAC (ottim. · base · pess.) | Conversione minima per ripagare il CAC in 12 mesi | LTV/CAC scenario ottimizzato | Costi fissi stimati |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 051 | 16,90 € | 2,91 € | 5,91 € | 28,57 € | 5,91 € | 0,28 · 0,21 · 0,17 | 13,5% | 0,52 | 300 € |
| 052 | 39,90 € | 11,60 € | 14,60 € | 44,44 € | 20,74 € | 0,62 · 0,47 · 0,37 | 3,9% | **1,10** | 500 € |
| 053 | 44,90 € | 11,42 € | 13,42 € | 50,00 € | 16,10 € | 0,43 · 0,32 · 0,26 | 5,0% | 0,78 | 400 € |
| 054 | 29,90 € | 8,49 € | 10,99 € | 40,00 € | 11,54 € | 0,38 · 0,29 · 0,23 | 6,9% | 0,72 | 1.200 € |
| 055 | 149,00 € | 38,07 € | 39,07 € | 100,00 € | 39,07 € | 0,52 · 0,39 · 0,31 | 2,0% | 0,98 | 6.000 € |
| 056 | 29,90 € | non ammesso | 12,98 € | 40,00 € | 23,37 € | 0,78 · 0,58 · 0,47 | 3,4% | **1,33** | 3.500 € |
| 057 | 34,90 € | 7,62 € | 11,12 € | 40,00 € | 12,23 € | 0,41 · 0,31 · 0,24 | 6,5% | 0,75 | 400 € |
| 058 | 109,00 € | 30,62 € | 30,62 € | 80,00 € | 30,62 € | 0,51 · 0,38 · 0,31 | 2,6% | 0,96 | 2.500 € |
| 059 | 29,90 € | 5,98 € | 8,98 € | 40,00 € | 9,43 € | 0,31 · 0,24 · 0,19 | 8,5% | 0,59 | 300 € |
| 060 | 14,90 € | 2,25 € | 5,15 € | 28,57 € | 12,87 € | 0,60 · 0,45 · 0,36 | 6,2% | 1,00 | 400 € |
| *Rif. KRINÉ Scalp* | *39,90 €* | — | *~20,7 €* | *32 €* | *45 €* | *base 1,77* | — | — | *~18 k€* |

**Come leggerla:**
- Il **magazzino UE batte quasi sempre la Cina diretta**, perché i 5 € di dogana superano il risparmio sul prodotto. Ma vuol dire anticipare scorte (per lo stock in Europa di CJ una fonte terza indica ~100 pezzi minimi), quindi c'è un rischio di magazzino.
- La colonna "conversione minima" è la più utile: dice quale conversione serve per non perdere soldi. Per 051, 059 e 054 servono conversioni irrealistiche (7–13%); per 052, 056 e 055 servono il 2–4%, livelli raggiunti solo da chi ha creatività vincenti.
- Anche nello scenario ottimizzato solo i **consumabili** (052, 056, 060) arrivano a LTV/CAC ≥ 1, cioè al pareggio, non al guadagno. Per vivere servirebbe traffico organico (TikTok, creator), e oggi non hai un pubblico.

---

## 5. Scheda pesata

**Motivazione:** il voto è una **mia stima**, da confermare. Ho dato 4 solo dove c'è una tua passione diretta (padel, tecnologia beauty), 2 dove non c'è niente di tuo.

| Criterio (peso) | 051 | 052 | 053 | 054 | 055 | 056 | 057 | 058 | 059 | 060 |
|---|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| Motivazione (20%) | 3 | 3 | 3 | 3 | 4 | 3 | 4 | 3 | 2 | 2 |
| Vantaggio del founder (15%) | 3 | 3 | 2 | 3 | 3 | 3 | 3 | 3 | 2 | 3 |
| Dolore e disponibilità a pagare (15%) | 2 | 3 | 2 | 2 | 3 | 3 | 2 | 3 | 2 | 2 |
| Mercato (10%) | 2 | 3 | 3 | 2 | 4 | 3 | 2 | 4 | 3 | 2 |
| Unit economics (10%) | 1 | 3 | 2 | 2 | 2 | 3 | 2 | 2 | 1 | 2 |
| Costo della validazione (10%) | 5 | 4 | 4 | 4 | 2 | 3 | 5 | 3 | 5 | 5 |
| Scalabilità (10%) | 4 | 4 | 4 | 4 | 4 | 4 | 4 | 5 | 4 | 4 |
| Difendibilità (5%) | 1 | 2 | 2 | 1 | 2 | 2 | 1 | 1 | 1 | 1 |
| Tempo al primo euro (5%) | 5 | 4 | 4 | 4 | 3 | 3 | 5 | 4 | 5 | 5 |
| **Totale** | **2,85** | **3,20** | **2,80** | **2,80** | **3,15** | **3,05** | **3,15** | **3,15** | **2,60** | **2,75** |

**Filtri eliminatori:**
| Filtro | Esito |
|---|---|
| 1. Capitale > 20 k€ | Tutti superati (il dropshipping si testa con 0,5–6 k€) |
| 3. Norme proibitive | **055 bocciata** (Allegato XVI MDR); 056 solo con marchio proprio e PIF; 060 a rischio se si promette qualcosa sul russamento |
| 4. Nessun interesse | 059 e 060 al limite |
| 5. Servizio continuativo | **Al limite per tutti:** è un prodotto, ma il dropshipping regge solo con un lavoro continuo su pubblicità, nuove creatività e assistenza. Senza di te le vendite si fermano in poche settimane |
| 7. Burocrazia al centro | Al limite per l'elettronica (054, 055, 058: RAEE, pile, CE) e per i cambi di fornitore sotto GPSR |

---

## 6. Lettura e raccomandazione

### Perché il dropshipping non è la strada principale
- **Rispetto a KRINÉ Scalp perde su quasi tutti i criteri** che pesano di più: motivazione (manca la scienza), vantaggio del founder (chiunque compra gli stessi prodotti dallo stesso fornitore), unit economics (LTV/CAC 0,2–0,6 contro 1,77) e difendibilità. Vince solo su costo della validazione e tempo al primo euro.
- **Il tuo vantaggio si sfrutta poco.** La tua forza (matematica + dati + AI) nel dropshipping diventa "trovare prodotti vincenti con i dati": è un vantaggio reale ma breve, perché un prodotto vincente viene copiato in poche settimane.
- **Il 2026 ha alzato i costi:** 3–5 € in più a pacco dalla Cina, GPSR, RAEE. Il dropshipping "alla vecchia" (AliExpress, 15 giorni di consegna, nessuna responsabilità) in Italia non esiste più.

### Dove ha senso: il dropshipping al servizio di KRINÉ
L'incognita principale di KRINÉ Scalp è il **CAC**, e oggi non hai **né clienti né pubblico**. Un piccolo negozio con prodotti già pronti, venduti **allo stesso pubblico** di KRINÉ Scalp, può dare entrambe le cose prima del lancio di marzo 2027.

**Proposta: test "Kit cuoio capelluto" (052 + 051)**
- **Cosa:** filtro doccia "toglie il cloro, non il calcare" (con i dati del test sul cloro) + spazzola massaggiante in regalo, sotto il marchio KRINÉ Labs. Comunicazione trasparente sul limite del calcare: è già il tono del marchio.
- **Perché:** misura il CAC **con acquisti veri** sul pubblico "cuoio capelluto che prude e si squama"; costruisce una lista di acquirenti a cui lanciare KRINÉ Scalp; ti fa allenare su Shopify, Meta e creatività a basso rischio.
- **Si integra con il test già previsto:** le 3 landing di KRINÉ Scalp (prude e brucia · squame che tornano · sebo e capelli) possono raccogliere iscrizioni e, sulla stessa pagina, vendere il kit.
- **Budget:** ≤ 2.000 € (≈ 300 € di campioni e piccolo stock in un magazzino UE, 1.500 € di pubblicità in 4 settimane, ~200 € tra Shopify e app).
- **Soglie da fissare prima (proposta):**

  | Metrica | Soglia per proseguire |
  |---|---|
  | CAC sul primo acquisto del kit | ≤ 30 € |
  | Conversione della pagina | ≥ 2% |
  | Costo per iscrizione alla lista KRINÉ Scalp | ≤ 12 € (come già fissato) |
  | Ordini in 4 settimane | ≥ 40 |
  | Riordino cartucce a 90 giorni | ≥ 25% (si misura dopo) |

- **Regola di arresto:** se dopo 2 settimane e 750 € di spesa il CAC supera i 50 €, si ferma la pubblicità e si tiene solo la raccolta di iscrizioni.

**Alternativa, solo se WHITECORE 2.0 ti motiva ancora:** strisce PAP con marchio proprio (056), ~5–6 k€ in tutto (3,5 k€ di conformità, ~2 k€ di stock, 1 k€ di pubblicità). Soglie: CAC ≤ 20 €, riordino ≥ 25% a 90 giorni.

**Da tenere nel backlog:** l'idea **061** (registratore AI con software tuo) merita una scheda a parte: è il primo caso in cui la tua competenza principale, l'AI engineering, diventa il prodotto.

---

## 7. Domande per te
1. **Motivazione:** i voti che ho stimato ti tornano? In particolare padel (057) e registratore AI (058): ti accendono davvero o solo come passatempo?
2. **Obiettivo del dropshipping:** lo cerchi come business a sé o come primo passo veloce per imparare a vendere online? La risposta cambia tutto: nel primo caso consiglio di non farlo, nel secondo il "kit cuoio capelluto" ha senso.
3. **Kit cuoio capelluto:** lo uniamo al test di domanda di KRINÉ Scalp (budget complessivo ~2–3,5 k€)?
4. **061 (registratore AI con software proprio):** vuoi che lo valuti con la scheda?
5. **WHITECORE 2.0:** tenerlo vivo (e allora 056 diventa il suo test) o archiviarlo?

---

## 8. Righe da aggiungere a backlog e log

**`03-backlog-idee.md`, nuova sezione:**

```
## Dropshipping (2026-10-11) · `idee/dropshipping/valutazione-10-prodotti.md`
| ID | Prodotto | Punteggio | Fase |
|---|---|:--:|:--:|
| 052 | Filtro doccia + cartucce (solo nel "kit cuoio capelluto" per KRINÉ) | 3,20 | 1 |
| 057 | Pressurizzatore palline da padel | 3,15 | cassetto |
| 058 | Registratore vocale AI in dropshipping | 3,15 | X → genera la 061 |
| 055 | Maschera LED viso | 3,15 | X (filtro 3) |
| 056 | Strisce PAP con marchio proprio (test di WHITECORE 2.0) | 3,05 | cassetto |
| 051 | Spazzola massaggiante cuoio capelluto (accessorio del kit) | 2,85 | X da sola |
| 053 | Federa in seta di gelso | 2,80 | X |
| 054 | Piegaciglia riscaldato | 2,80 | X |
| 060 | Nastro per la bocca | 2,75 | X |
| 059 | Cubi a compressione da viaggio | 2,60 | X |
| 061 | Registratore AI con software proprio (hardware + SaaS) | da valutare | 0 |
```

**`04-log-decisioni.md`, nuova riga:**

```
| 2026-10-11 | Valutati 10 prodotti di dropshipping: nessuno passa (massimo 3,20); LTV/CAC base 0,21–0,58 | Dazio UE di 3 € dal 1/7/2026 + contributo IT di 2 € (dal 1/12/2026, da verificare); GPSR rende il venditore importatore; solo i consumabili si avvicinano al pareggio; manca la scienza (motivazione). Vedi `idee/dropshipping/valutazione-10-prodotti.md` | Decidere se usare un "kit cuoio capelluto" (052 + 051) come test di CAC e lista per KRINÉ Scalp (≤ 2 k€) |
```

---

## 9. Fonti

**Regole 2026**
- Dazio UE di 3 €: [Easyship](https://www.easyship.com/blog/eu-150-de-minimis-ends-for-ecommerce-sellers) · [ShipperHQ](https://shipperhq.com/blog/de-minimis-is-ending-in-the-eu-what-ecommerce-brands-need-to-know) · [UKP Worldwide](https://www.ukpworldwide.com/2025/12/16/eu-customs-update-removal-of-duty-de-minimis-from-july-2026/) · [Logistics Plus](https://www.logisticsplus.com/?p=57642) · [fulfilment.com](https://fulfilment.com/blog/eu-de-minimis-changes)
- Contributo italiano di 2 €: [Diritto.it](https://www.diritto.it/legge-bilancio-2026-contributo-importazioni-150-e/) · [Fiscomania](https://fiscomania.com/prelievo-2-euro-pacchi-extra-ue/) · [QuotidianoPiù, rinvio al 1/12/2026](https://www.quotidianopiu.it/dettaglio/16444854/rinviata-al-1-dicembre-2026-la-tassa-nazionale-sui-mini-pacchi) · [FiscoeTasse, proroga](https://www.fiscoetasse.com/new-rassegna-stampa/3310-contributo-di-2-euro-sui-pacchi-extra-ue-confermata-la-proroga.html)
- GPSR: [ecommerceGermany](https://ecommercegermany.com/blog/gpsr-general-product-safety-regulation/) · [Flex Fulfillment](https://www.flexfulfillment.eu/gpsr-and-eu-product-safety-what-non-eu-brands-must-know-in-2026/) · [Landmark Global](https://landmarkglobal.com/eu/en/news-insights/what-is-gpsr) · [Katana](https://katanapim.com/post/from-gpsd-to-gpsr-what-eu-sellers-must-do-to-stay-compliant-in-2025) · [EVZ, dropshipping nell'UE](https://www.evz.de/en/shopping-internet/online-shopping/dropshipping/)
- MDR Allegato XVI: [NAMSA](https://namsa.com/resources/blog/mdr-implementing-regulation-annex-xvi-published/) · [BSI, white paper](https://bsigroup.com/siteassets/pdf/en/insights-and-media/insights/white-papers/bsi-md-mdr-annex-xvi-whitepaper-en-gb.pdf) · [BSI, domande e risposte](https://v1.bsigroup.com/siteassets/pdf/en/insights-and-media/insights/brochures/bsi-md-mdr-annex-xvi-qa-en-gb.pdf)

**Mercato del dropshipping e pubblicità**
- Tassi di successo e margini: [TrueProfit](https://trueprofit.io/blog/dropshipping-success-rate) · [Carro](https://getcarro.com/blog/dropshipping-statistics) · [DropCommerce](https://blog.dropcommerce.com/posts/dropshipping-success-rate) · [Gropulse](https://gropulse.com/shopify-dropshipping-failure-rate/)
- Costi Meta: [Adamigo, CPM per Paese 2026](https://www.adamigo.ai/blog/meta-ads-cpm-cpc-benchmarks-by-country-2026) · [ContentStudio](https://contentstudio.io/blog/meta-ads-benchmarks) · [eightx, CAC in Europa](https://eightx.co/blog/eu-ecommerce-cac-benchmark)
- Magazzini UE: [CJ, magazzini globali](https://cjdropshipping.com/blogs/cj-news/CJ-s-Global-Warehouses) · [Eurofiscalis, CJ EU](https://www.eurofiscalis.com/cs/glosar/cj-dropshipping-eu/) · [Trendtrack, BigBuy](https://www.trendtrack.io/it/blog-post/recensione-bigbuy-e-un-opzione-affidabile-per-il-tuo-sito-dropshipping)

**Prodotti**
- Filtro doccia: [Smartrr, Jolie](https://smartrr.com/case-studies/step-0-jolie-skin-co) · [Beauty Independent, Jolie](https://www.beautyindependent.com/greats-founder-ryan-babenzien-new-showerhead-filter-brand-jolie/) · [Fortune Business Insights](https://www.fortunebusinessinsights.com/zh/premium-shower-filters-market-115975) · [Techprincess, 883 comuni](https://techprincess.it/comuni-con-acqua-piena-di-calcare-in-italia-sono-883/) · [Water Filter Guru, test di laboratorio](https://waterfilterguru.com/hello-klean-shower-filter-review/)
- Federa in seta: [Market Intelo](https://marketintelo.com/report/silk-pillowcase-market) · [Dataintelo](https://dataintelo.com/report/silk-pillowcase-market) · [Particl, Slip](https://www.particl.com/company/Slip)
- Piegaciglia: [MediaWorld, Dam](https://www.mediaworld.it/it/product/_piegaciglia-dam-electronics-dmar0242c50-batteria-ricaricabile-3-livelli-di-temperatura-142647390.html) · [MediaWorld, Idermia](https://www.mediaworld.it/it/product/_piegaciglia-idermia-dmak0668c50-batteria-ricaricabile-3-livelli-temperatura-140567542.html) · [Unieuro](https://www.unieuro.it/online/Altri/Piegaciglia-WOW-LASH-PRO-Heated-Eyelash-Curler-pidRBEELCP) · [DiLei](https://dilei.it/bellezza/smiling-shark-piegaciglia-elettronico-offerta-amazon/1780659/)
- Maschera LED: [IMARC](https://www.imarcgroup.com/led-light-face-mask-market) · [Verified Market Research](https://www.verifiedmarketresearch.com/product/led-face-masks-market/) · [Notebookcheck, Nanoleaf](https://www.notebookcheck.net/Nanoleaf-s-new-LED-Light-Therapy-Face-Mask-now-available-to-pre-order-in-Europe.964718.0.html)
- Strisce PAP: [Kruidvat, Hismile](https://www.kruidvat.nl/hismile-teeth-whitening-pap-strips/p/6289848) · [Beautetrade, fornitore](https://beautetrade.com/products/ce-approved-glorysmile-professional-white-tooth-strips-advanced-pap-teeth-whitening-strips-private-label/42080) · [Alibaba, guida al private label](https://seller.alibaba.com/blogs/2026/southeast-asia/personal-care/teeth-whitening-strips-private-label-guide-alibaba-b2b)
- Padel: [Padel Market](https://padelmarket.com/en-eu/collections/accessories-pressurizers) · [Tennis Pro](https://www.tennispro.eu/bounce-padel-x4-ball-pressurizer-840175.html) · [Padelspeak](https://padelspeak.com/en/padel-ball-pressuriser/) · [ABG IP, brevetti Pascal Box](https://abg-ip.com/intellectual-property-padel-patents/) · [Dire, campi in Italia](https://www.dire.it/13-07-2026/1255235-litalia-e-il-secondo-paese-al-mondo-per-campi-di-padel/) · [Geopop](https://www.geopop.it/boom-di-padel-litalia-e-il-secondo-paese-al-mondo-per-numero-di-campi-e-praticanti/)
- Registratore AI: [Plaud EU, NotePin](https://eu.plaud.ai/collections/plaud-notepin) · [Sacra, ricavi Plaud](https://sacra.com/research/250m-year-granola-for-plumbers) · [36Kr](https://eu.36kr.com/en/p/3961453579746437) · [KrASIA](https://amp.kr-asia.com/tencents-rumored-plaud-deal-points-to-looming-ai-hardware-contest)
- Nastro per la bocca: [HealthDay, revisione PLOS One 2025](https://www.healthday.com/health-news/sleep-disorder/mouth-taping-for-better-sleep-little-benefit-lots-of-risk-review-says) · [CU Anschutz](https://news.cuanschutz.edu/news-stories/mouth-tape-for-better-sleep-myth-or-miracle) · [Scimex](https://www.scimex.org/newsfeed/social-media-fad-of-nighttime-mouth-taping-may-pose-serious-risks) · [Fawcett, trend delle ricerche](https://fawcettmattress.com/blogs/news/mouth-taping)
