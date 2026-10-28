# Guion — “Cos’è un ETF” (reel Instagram)

Formato: verticale 1080×1920, 60 fps, durata 58.9 s (3533 fotogrammi). Voce narrante generata con Gemini (`npm run voice`): sottotitoli e animazioni seguono i tempi reali della voce, riportati qui sotto. Questo file è generato da `src/script.ts` con `npm run guion`: se cambi un testo lì, video e copione restano allineati.

## Perché è costruito così (ottimizzazione per Instagram)

Nessuno può garantire che un reel diventi virale: dipende anche dall’account, dall’orario e da fattori che non controlliamo. Il video però è costruito sui segnali che contano di più:

- **Gancio nel primo secondo.** Il primo fotogramma è già in movimento e la prima frase promette un numero sorprendente (“un solo acquisto → oltre mille aziende”). Niente intro né logo.
- **Un cambio visivo ogni 1-3 secondi.** Ogni frase fa succedere qualcosa sullo schermo, così l’occhio non ha tempo di annoiarsi e la percentuale di visione resta alta.
- **Sottotitoli parola per parola, con la parola chiave evidenziata.** Il video si capisce anche senza audio, come lo guarda gran parte del pubblico.
- **Struttura a capitoli (01, 02, 03).** Chi guarda sa quanto manca e resta fino al terzo vantaggio.
- **Numeri concreti e verificabili:** −60% contro −0,06%, × 1.000 commissioni contro × 1, 0,2% = 2 € ogni 1.000 €.
- **Avvertenza sul rischio.** Aumenta la credibilità e protegge da segnalazioni per contenuti finanziari fuorvianti.
- **Invito finale a salvare e inviare.** Salvataggi e condivisioni in DM sono tra i segnali più forti per la distribuzione.
- **Loop perfetto.** L’ultimo fotogramma coincide con il primo: chi non scorre subito lo rivede, e il tempo di visione sale.

## Stile visivo

- Fondo quasi nero (#05070C) con griglia di puntini in lento movimento e un alone del colore del capitolo.
- Colori con significato fisso: **verde** #34D399 = ETF/positivo, **rosso** #F87171 = perdita/rischio, **ambra** #FBBF24 = costi/attenzione, **blu** #60A5FA = singola azione/scelta.
- Font Inter (ExtraBold per i sottotitoli, Black per i numeri). Sottotitoli in alto (da y≈250), fuori dalle zone coperte dall’interfaccia di Instagram.
- Animazioni: 60 fotogrammi distinti al secondo, curve di accelerazione morbide, rimbalzi fisici. Tra una scena e l’altra c’è una transizione di 16 fotogrammi con zoom e sfocatura.

## Copione fotogramma per fotogramma

Tempi in minuti:secondi; tra parentesi i fotogrammi a 60 fps. Ogni riga è una frase dei sottotitoli: chi registra la voce deve far partire la frase al tempo indicato. Le parole in **grassetto** sono quelle evidenziate.

### Scena 1 — Gancio + cos’è un ETF · 00:00.00 → 00:08.59 (fotogrammi 0–514)

**Obiettivo:** Fermare lo scroll nel primo secondo con un numero sorprendente (1 acquisto → 1.000 aziende) e dare subito la definizione.

**Transizione:** Nessuna in entrata: il primo fotogramma è già in movimento (il quadrato verde sta crescendo). Uscita con zoom in avanti + sfocatura.

| Tempo (fotogrammi) | Sottotitolo / voce | Cosa appare sullo schermo |
|---|---|---|
| 00:00.12 → 00:01.14 (7–67) | Con **un solo acquisto** | Fondo blu notte con griglia di puntini che scorre. Al centro un quadrato verde luminoso cresce con un piccolo rimbalzo; due anelli verdi si espandono come un “tap”. Sotto: etichetta “1 ACQUISTO”. |
| 00:01.14 → 00:02.94 (68–176) | puoi investire in oltre **mille aziende.** | Su “investire” il quadrato si rimpicciolisce e diventa la tessera centrale di una griglia 32×32 (1.024 tessere) che si accende a onda dal centro e si inclina in prospettiva 3D. In basso il contatore sale da 1 a “1.000+ AZIENDE”. Su “mille aziende” un’onda verde colora tutte le tessere. |
| 00:03.15 → 00:04.55 (189–272) | Si chiama **ETF:** | Su “ETF” la griglia torna piatta: le tessere che formano le lettere E-T-F diventano verde brillante con alone, tutte le altre cadono e si spengono. Il contatore sparisce. |
| 00:04.68 → 00:06.98 (281–418) | un fondo che si compra e si vende **in borsa,** | Sotto le lettere si scrive “EXCHANGE TRADED FUND” (iniziali in verde). Su “in borsa” appare con un rimbalzo la pillola “= fondo quotato in borsa”. |
| 00:07.24 → 00:08.17 (435–489) | come **un’azione.** | Su “un’azione” sotto la pillola crescono, una dopo l’altra, 18 candele di un grafico di borsa (verdi e rosse). |

### Scena 2 — Dentro l’ETF: il paniere · 00:08.59 → 00:15.54 (fotogrammi 515–931)

**Obiettivo:** Far capire con un’immagine fisica che l’ETF è un contenitore di tante azioni scelte da un indice.

**Transizione:** Entrata: la scena arriva da leggermente più piccola e sfocata. Uscita: zoom in avanti + sfocatura.

| Tempo (fotogrammi) | Sottotitolo / voce | Cosa appare sullo schermo |
|---|---|---|
| 00:08.69 → 00:10.33 (521–619) | Dentro ci sono **tante azioni** insieme, | Dal basso sale un contenitore trasparente con la targa “ETF · 1 SOLO ACQUISTO”. Su “Dentro” 24 aziende astratte (quadrati colorati con simboli geometrici, nessun logo reale) cadono dall’alto ruotando e rimbalzano, impilandosi su 4 file. |
| 00:10.54 → 00:12.04 (632–721) | scelte seguendo **un indice:** | Su “un indice” un cartellino bianco “INDICE” si aggancia al bordo destro del contenitore e oscilla come un pendolo fino a fermarsi. |
| 00:12.17 → 00:15.12 (730–906) | per esempio le grandi aziende **di tutto il mondo.** | Su “grandi” sopra il contenitore emerge un globo fatto di puntini che ruota; su “di tutto il mondo” circa il 20% dei puntini si accende di verde (le aziende nel mondo). |

### Scena 3 — Vantaggio 1: diversificazione · 00:15.54 → 00:27.55 (fotogrammi 932–1652)

**Obiettivo:** Mostrare il rischio di una singola azione contro l’effetto diluito dentro un ETF, con un confronto onesto e un esempio dichiarato come semplificato.

**Transizione:** Entrata e uscita zoom + sfocatura.

| Tempo (fotogrammi) | Sottotitolo / voce | Cosa appare sullo schermo |
|---|---|---|
| 00:15.64 → 00:17.96 (938–1076) | Primo vantaggio: la **diversificazione.** | Cartello di sezione: grande “01” a contorno verde che sale dal basso e la scritta “DIVERSIFICAZIONE” lettera per lettera. |
| 00:18.16 → 00:19.62 (1090–1176) | Se compri **una sola azione** | Il cartello si dissolve e resta in alto la pillola “01 DIVERSIFICAZIONE”. Entrano due schede: sopra “UNA SOLA AZIONE” (quadrato blu + grafico a linea), sotto “ETF · 1.000 AZIENDE” (griglia di 1.000 micro-tessere + grafico), la seconda ancora attenuata. Le linee iniziano a disegnarsi. |
| 00:19.75 → 00:20.83 (1185–1249) | e quell’azienda **crolla,** | Su “crolla” la linea della scheda sopra precipita in rosso, l’area sotto si colora di rosso, il quadrato diventa rosso, trema e si crepa. In alto a destra il valore scende fino a “−60%”. |
| 00:21.07 → 00:22.55 (1264–1352) | crolla anche il tuo investimento. | La scheda resta su “−60%”: il calo è tutto sul tuo investimento. |
| 00:22.75 → 00:25.15 (1365–1508) | Nell’ETF è solo **una su mille:** | Su “Nell’ETF” la scheda sotto si accende con bordo verde. Su “una su mille” una sola micro-tessera tra le 1.000 diventa rossa, evidenziata da un anello rosso che si allarga. |
| 00:25.28 → 00:27.13 (1517–1627) | il colpo **si sente molto meno.** | La linea verde della scheda sotto prosegue quasi piatta: lo stesso crollo vale “−0,06%” (valore in ambra). In basso la nota: “Esempio semplificato: 1.000 aziende con lo stesso peso.” |

### Scena 4 — Vantaggio 2: costi · 00:27.55 → 00:41.49 (fotogrammi 1653–2488)

**Obiettivo:** Rendere tangibile il costo di comprare tante azioni una per una e tradurre lo 0,2% in euro.

**Transizione:** Entrata e uscita zoom + sfocatura. Fondo con alone ambra.

| Tempo (fotogrammi) | Sottotitolo / voce | Cosa appare sullo schermo |
|---|---|---|
| 00:27.65 → 00:28.95 (1659–1736) | Secondo: i **costi.** | Cartello di sezione “02 · COSTI” in ambra, stessa animazione del capitolo 01. |
| 00:29.16 → 00:31.16 (1749–1868) | Comprare mille azioni una per una | Resta la pillola “02 COSTI”. Al centro il contatore “× 1” che inizia a salire con sotto “COMMISSIONI, AZIONE PER AZIONE”. Ricevute gialle “€ COMMISSIONE” volano da destra e si impilano in una torre che cresce, sempre più veloce. |
| 00:31.55 → 00:33.15 (1893–1988) | vuol dire **mille commissioni.** | Su “mille commissioni” il contatore arriva a “× 1.000” e la torre è al massimo. |
| 00:33.36 → 00:35.26 (2001–2114) | Con l’ETF è **un solo acquisto,** | Su “un solo acquisto” la torre si comprime in un’unica ricevuta che diventa verde con scritto “1 ORDINE”; il contatore scatta a “× 1” verde, “ORDINE CON L’ETF”. |
| 00:35.65 → 00:38.76 (2139–2324) | con un costo annuo spesso **dello 0,2%** o meno: | Su “costo annuo” tutto sale e svanisce; appare una barra a capsula che si riempie di verde: “1.000 € INVESTITI”. Su “dello 0,2%” una sottile fetta ambra si accende all’estremità della barra, una linea tratteggiata porta a una lente che la ingrandisce: “2 €”. A sinistra grande “0,2%” e “COSTO ALL’ANNO”. |
| 00:38.89 → 00:41.06 (2333–2463) | circa **2 € ogni 1.000 €.** | Su “circa” sotto lo 0,2% compare “≈ 2 € ogni 1.000 €”. In basso le note: “Costo annuo (TER) indicativo: varia da ETF a ETF. Le commissioni di acquisto dipendono dal broker.” |

### Scena 5 — Vantaggio 3: semplicità · 00:41.49 → 00:47.80 (fotogrammi 2489–2867)

**Obiettivo:** Contrapporre lo stock picking (indovinare il vincitore) al comprare l’intero indice.

**Transizione:** Entrata e uscita zoom + sfocatura. Fondo con alone blu.

| Tempo (fotogrammi) | Sottotitolo / voce | Cosa appare sullo schermo |
|---|---|---|
| 00:41.59 → 00:43.20 (2495–2591) | Terzo: la **semplicità.** | Cartello di sezione “03 · SEMPLICITÀ” in blu. |
| 00:43.40 → 00:45.77 (2604–2745) | Non devi indovinare tu le aziende vincenti: | Resta la pillola “03 SEMPLICITÀ”. Compare una griglia 8×6 di aziende spente, ognuna con un “?”. Su “indovinare” una lente blu salta da un’azienda all’altra: quella sotto la lente si ingrandisce e il suo “?” diventa blu. |
| 00:45.90 → 00:47.38 (2754–2842) | **segui l’intero mercato.** | Su “segui l’intero mercato” la lente si allarga fino a diventare una cornice verde attorno a tutta la griglia; le aziende si accendono a onda in diagonale, ognuna col suo colore e simbolo. Sotto: “INDICE = L’INTERO MERCATO”. |

### Scena 6 — Avvertenza: il rischio resta · 00:47.80 → 00:53.82 (fotogrammi 2868–3228)

**Obiettivo:** Correttezza e credibilità: l’ETF diversifica il rischio della singola azienda, non quello del mercato.

**Transizione:** Entrata e uscita zoom + sfocatura. Fondo con alone ambra.

| Tempo (fotogrammi) | Sottotitolo / voce | Cosa appare sullo schermo |
|---|---|---|
| 00:47.90 → 00:48.88 (2874–2932) | Attenzione però: | Su “Attenzione” un triangolo di pericolo ambra compare con un rimbalzo e oscilla. Sotto, il grafico “MERCATO” inizia a disegnarsi in verde, con l’etichetta “ETF” che segue la punta della linea. |
| 00:49.01 → 00:51.18 (2941–3070) | l’ETF **non elimina il rischio.** | La linea continua a salire mentre il sottotitolo in rosso dice “non elimina il rischio”. |
| 00:51.38 → 00:52.41 (3083–3144) | Se scende il mercato, | Su “scende” la linea gira verso il basso e diventa rossa, con l’area sotto rossa; l’etichetta “ETF” diventa rossa e scende con la linea. |
| 00:52.57 → 00:53.40 (3154–3203) | **scende anche lui.** | Vicino al punto più basso appare in rosso “il valore può scendere”. Nessun recupero promesso. |

### Scena 7 — Chiusura: salva e condividi (loop) · 00:53.82 → 00:58.87 (fotogrammi 3229–3531)

**Obiettivo:** Chiedere i due segnali che Instagram premia di più (salvataggi e invii in DM) e chiudere in loop.

**Transizione:** Entrata zoom + sfocatura. Nessuna uscita: l’ultimo fotogramma coincide con il primo, così il reel riparte senza stacco.

| Tempo (fotogrammi) | Sottotitolo / voce | Cosa appare sullo schermo |
|---|---|---|
| 00:53.92 → 00:55.79 (3235–3346) | **Salvalo** per quando inizierai a investire, | Due icone in riquadri di vetro: segnalibro “SALVA” e aeroplanino “CONDIVIDI”. Su “Salvalo” il segnalibro si riempie di verde dal basso con un rimbalzo e il riquadro si illumina. In basso: “Contenuto informativo, non è consulenza finanziaria. Investire comporta rischi, anche di perdita del capitale.” |
| 00:55.96 → 00:57.36 (3358–3441) | e **mandalo** a chi vuole iniziare. | Su “mandalo” l’aeroplanino vola via in alto a destra e torna con un rimbalzo; il riquadro si illumina di blu. Nell’ultimo secondo tutto si stringe verso il centro e svanisce, e nasce il quadrato verde del primo fotogramma: il video ricomincia in loop. |

## Testo completo per la voce

Da leggere con tono sicuro e amichevole, ritmo sostenuto (circa 3 parole al secondo) e una breve pausa a ogni virgola e a ogni punto. Si legge così come è scritto, tranne: “0,2%” = “zero virgola due per cento”, “2 € ogni 1.000 €” = “due euro ogni mille euro”.

> Con un solo acquisto puoi investire in oltre mille aziende. Si chiama ETF: un fondo che si compra e si vende in borsa, come un’azione.
>
> Dentro ci sono tante azioni insieme, scelte seguendo un indice: per esempio le grandi aziende di tutto il mondo.
>
> Primo vantaggio: la diversificazione. Se compri una sola azione e quell’azienda crolla, crolla anche il tuo investimento. Nell’ETF è solo una su mille: il colpo si sente molto meno.
>
> Secondo: i costi. Comprare mille azioni una per una vuol dire mille commissioni. Con l’ETF è un solo acquisto, con un costo annuo spesso dello 0,2% o meno: circa 2 € ogni 1.000 €.
>
> Terzo: la semplicità. Non devi indovinare tu le aziende vincenti: segui l’intero mercato.
>
> Attenzione però: l’ETF non elimina il rischio. Se scende il mercato, scende anche lui.
>
> Salvalo per quando inizierai a investire, e mandalo a chi vuole iniziare.

**Voce inclusa:** `out/etf-voce.mp4` ha già la voce generata (voce Gemini “Charon”, accelerata del 10%); `out/etf-sottotitoli.mp4` è la stessa versione muta. Per cambiare voce: `VOICE_NAME=Kore npm run voice`, poi `npm run render`.

**Per usare una voce tua:** registra o genera la voce seguendo i tempi della tabella. Se il ritmo della tua voce è diverso, posso ritagliare i sottotitoli sui tempi reali: mi basta il file audio. In alternativa, nell’editor di Instagram o in CapCut appoggia la traccia voce sopra il video e regola il volume della musica intorno al 15-20%.

## Pubblicazione

- **Copertina:** `out/cover.png` (“Cos’è un ETF? 3 vantaggi rispetto alle azioni”).
- **Musica:** una base strumentale di tendenza dalla libreria di Instagram, a volume basso sotto la voce. La musica aggiunta da Instagram è già concessa in licenza per i reel.
- **Didascalia proposta:**

> Con un solo acquisto puoi investire in oltre 1.000 aziende 🌍
> ETF vs singola azione, in 3 punti:
> 1️⃣ Diversificazione: se un’azienda crolla, nell’ETF pesa poco
> 2️⃣ Costi: un solo ordine e un costo annuo spesso intorno allo 0,2% o meno
> 3️⃣ Semplicità: non devi indovinare le aziende vincenti
> ⚠️ L’ETF non elimina il rischio di mercato.
> 📌 Salvalo per quando inizierai a investire.
>
> Contenuto informativo, non è consulenza finanziaria.
>
> #etf #investire #educazionefinanziaria #finanzapersonale #borsa #risparmio #investimenti #soldi

- **Primo commento (da fissare in alto):** una domanda che invita a rispondere, per esempio “Tu hai già un ETF o compri azioni singole?”.
- **Controlli prima di pubblicare:** il TER dello 0,2% è un valore indicativo per gli ETF azionari più diffusi; se nel video citi un prodotto specifico, verifica i suoi dati sul documento ufficiale (KID).
