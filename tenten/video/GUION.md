# Guion — “TEN:TEN all’XO Club” (reel Instagram)

Formato: verticale 1080×1920, 60 fps, durata 22.5 s (1350 fotogrammi). Tempi stimati: la voce non è ancora stata generata. Questo file è generato da `src/script.ts` con `npm run guion`: se cambi un testo lì, video e copione restano allineati.

Fonte unica dei contenuti: la pagina del venerdì di Florence International Week (informazioni, foto e loghi). Le persone e il locale sono solo quelli delle foto vere; le immagini generate (con Codex) sono solo oggetti: la moneta, il buzzer e la bottiglia.

## Perché è costruito così (concorso e Instagram)

- **Gancio nel primo secondo:** un oggetto che gira già al primo fotogramma, il suono della moneta e una promessa concreta (“entri in discoteca con un euro”).
- **Un evento visivo ogni 1-2 secondi:** moneta che si ferma, prezzo che scorre, lampo, marchio, capsula che si stacca, buzzer premuto, timer che si ferma, bottiglia, montaggio.
- **Il gioco si vede, non si spiega:** il timer si ferma davvero su 10:10 davanti a chi guarda, con lampo, vibrazione della camera e jingle.
- **Foto vere che si muovono in 3D:** ogni foto della serata ha una mappa di profondità (generata con Codex a partire dalla foto vera), quindi la camera non fa un semplice zoom ma si muove nello spazio. Le transizioni fanno comparire prima ciò che è vicino e poi lo sfondo.
- **Immagini generate integrate senza stacchi:** stessa luce rossa, stessa grana e stessa sfocatura per foto vere e oggetti generati; ogni oggetto fa da ponte tra un piano e il successivo (moneta → luce del locale, foto sfocata → buzzer, buzzer → bottiglia → brindisi).
- **Sottotitoli parola per parola** con le parole chiave evidenziate in rosso: si capisce anche senza audio.
- **Una schermata da salvare:** la scheda finale ha tutte le informazioni (giorno, orari, prezzo e condizione, indirizzo).
- **Loop perfetto:** l’ultimo fotogramma coincide con il primo, anche nel suono della moneta.

## Stile: il linguaggio di movimento di Liquid Glass (iOS 26)

- **Un solo piano di vetro** sopra le foto, che le rifrange davvero (shader WebGL): lensing sui bordi, leggera dispersione cromatica, centro smerigliato e scurito per la leggibilità.
- **Comparire e sparire modulando la rifrazione,** non con dissolvenze.
- **Un controllo diventa il successivo:** prezzo → TEN:TEN → 1 drink = 1 giocata → timer → area VIP.
- **Controlli che si staccano e si uniscono come gocce:** la capsula XO esce dalla card TEN:TEN e ci rientra; il pulsante Prenota esce dalla scheda finale.
- **Risposta al tocco:** il vetro si comprime, rimbalza e si illumina dal punto toccato.
- **Cifre che scorrono** come .numericText (20 € → 1 €) e riflessi che seguono l’inclinazione simulata del telefono.

Colori del marchio: rosso del buzzer #E5232C, cremisi, crema #F4E7D1 per il marchio TEN:TEN (font Anton), testo bianco in Inter. 60 fotogrammi distinti al secondo, molle fisiche.

## Copione fotogramma per fotogramma

Tempi in minuti:secondi; tra parentesi i fotogrammi a 60 fps. Ogni riga è una frase dei sottotitoli e della voce. Le parole in **grassetto** sono quelle evidenziate.

### Scena 1 — Gancio: la moneta da 1 € · 00:00.00 → 00:03.73 (fotogrammi 0–223)

**Obiettivo:** Fermare lo scroll nel primo secondo con un oggetto in movimento e una promessa concreta: entrare in discoteca con un euro.

**Transizione:** Nessuna in entrata: il primo fotogramma è già in movimento ed è identico all’ultimo (loop). Uscita: la moneta corre verso la camera e il suo bagliore diventa la luce del locale.

| Tempo (fotogrammi) | Sottotitolo / voce | Cosa appare sullo schermo |
|---|---|---|
| 00:00.12 → 00:03.17 (7–189) | A Firenze, il venerdì, entri in discoteca con **un euro.** | Fondo cremisi con fasci di luce che oscillano dal soffitto e luci sfocate che derivano. Al centro una moneta da 1 € (immagine generata) gira in 3D su sé stessa, con il bordo dorato visibile di taglio e un riflesso che la attraversa; rallenta e si ferma di fronte sulla parola “un euro”, con una stella di luce sul metallo e un tintinnio. Sotto si materializza la capsula di vetro “Ingresso 20 €”: le cifre scorrono come in .numericText fino a “1 €”, la colonna delle decine si richiude e la capsula si stringe con una molla; quando si ferma, il vetro viene “premuto” e si illumina. |

### Scena 2 — TEN:TEN all’XO Club · 00:03.73 → 00:06.66 (fotogrammi 224–399)

**Obiettivo:** Dare il nome della serata e del locale, con le persone vere della serata.

**Transizione:** Entrata dal lampo della moneta: la foto della folla nasce sovraesposta e la camera si allontana. Uscita: transizione “di profondità” verso la pista, in cui compare prima chi è vicino e poi lo sfondo, con una riga di luce sul fronte.

| Tempo (fotogrammi) | Sottotitolo / voce | Cosa appare sullo schermo |
|---|---|---|
| 00:03.83 → 00:06.10 (230–365) | Si chiama **TEN:TEN,** all’XO Club di via Verdi. | Foto vera della folla sotto il palco (dal sito), in 2.5D: grazie alla mappa di profondità la camera scivola di lato e le mani in primo piano si muovono più dello sfondo. La capsula del prezzo si trasforma nella card di vetro con il marchio “TEN:TEN” (crema su vetro rosso). Su “XO” dal fondo della card si stacca, come una goccia, una capsula con il logo XO e “Via Verdi 59R”. Su “via Verdi” la folla lascia il posto alla pista. |

### Scena 3 — Il gioco: ferma il timer su 10:10 · 00:06.66 → 00:11.42 (fotogrammi 400–684)

**Obiettivo:** Spiegare il meccanismo in pochi secondi e farlo vivere: il buzzer viene premuto davvero e il timer si ferma esattamente su 10:10.

**Transizione:** Entrata: transizione di profondità verso la foto della ragazza con il buzzer. Poi la camera scivola verso il buzzer che ha in mano, la foto va fuori fuoco e diventa lo sfondo luminoso del buzzer generato.

| Tempo (fotogrammi) | Sottotitolo / voce | Cosa appare sullo schermo |
|---|---|---|
| 00:06.76 → 00:08.08 (406–484) | Ogni drink è una giocata: | Foto vera della ragazza che tiene il buzzer, con la scritta al neon alle spalle. Card e capsula XO si fondono in un’unica capsula “🍸 1 drink = 1 giocata”. |
| 00:08.30 → 00:10.86 (498–651) | premi il **buzzer** e ferma il timer su **10:10.** | La foto va fuori fuoco e dal basso sale, con una molla, il buzzer rosso (immagine generata, uguale a quello della locandina). La capsula diventa il timer di vetro con le cifre a LED. Un dito preme la cupola, che si abbassa davvero, e il timer parte: le cifre corrono, sul display del buzzer e nel vetro, con un bip a ogni secondo. Su “10:10” secondo tocco: il timer si ferma esattamente su 10:10, lampo rosso, la camera trema, il display lampeggia tre volte e suona il jingle della vincita. |

### Scena 4 — La bottiglia in area VIP · 00:11.42 → 00:16.46 (fotogrammi 685–986)

**Obiettivo:** Mostrare il premio e legarlo all’idea di festeggiare insieme.

**Transizione:** Il buzzer scende fuori campo mentre dietro la foto sfocata diventa il brindisi. Uscita: la bottiglia vola in alto e la camera scende sui calici che si toccano.

| Tempo (fotogrammi) | Sottotitolo / voce | Cosa appare sullo schermo |
|---|---|---|
| 00:11.52 → 00:14.06 (691–843) | Se ci riesci, vinci **una bottiglia** in area VIP, | Dal basso sale una bottiglia (immagine generata) con una fontana di scintille calcolata in codice che illumina il vetro e il fondo. Il timer si trasforma nella capsula “✦ Bottiglia in area VIP”. |
| 00:14.22 → 00:15.90 (853–953) | da festeggiare con **i tuoi amici.** | La bottiglia vola via verso l’alto lasciando la scia delle scintille; la foto del brindisi va a fuoco. Poi un montaggio veloce di foto vere della serata (ragazze che ballano, DJ, MC), legate da colpi di camera laterali con scia di movimento e dalle transizioni di profondità. |

### Scena 5 — Chiusura: prenota (loop) · 00:16.46 → 00:22.49 (fotogrammi 987–1348)

**Obiettivo:** Dare la condizione esatta per l’ingresso a 1 € e tutte le informazioni in una sola schermata da salvare.

**Transizione:** Entrata: transizione di profondità verso la pista, che poi va fuori fuoco. Nessuna uscita: la scheda si smaterializza, il locale si spegne e torna la moneta che gira, identica al primo fotogramma.

| Tempo (fotogrammi) | Sottotitolo / voce | Cosa appare sullo schermo |
|---|---|---|
| 00:16.56 → 00:19.53 (993–1171) | Prenota: entro le **00.30** entri a un euro. | Si materializza la scheda di vetro: “TEN:TEN”, “Ogni venerdì · 23.30–5.00”, “1 € con prenotazione entro le 00.30”, logo XO e “Via Verdi 59R, Firenze”. Dalla scheda si stacca come una goccia il pulsante di vetro “Prenota”, che viene toccato: si comprime, rimbalza e si accende di rosso. |
| 00:19.87 → 00:20.85 (1192–1250) | **Ci vediamo venerdì.** | La scheda pulsa leggermente. Nell’ultimo secondo e mezzo tutto il vetro si smaterializza, la pista si spegne nella foschia cremisi e la moneta torna girando al centro: il reel riparte senza stacco. |

## Testo della voce

Voce femminile dolce, ritmo sereno ma sostenuto. Si legge così come è scritto, tranne: “TEN:TEN” = “ten ten”, “XO” = “ics o”, “10:10” = “dieci e dieci”, “00.30” = “mezzanotte e mezza”.

> A Firenze, il venerdì, entri in discoteca con un euro.
>
> Si chiama TEN:TEN, all’XO Club di via Verdi.
>
> Ogni drink è una giocata: premi il buzzer e ferma il timer su 10:10.
>
> Se ci riesci, vinci una bottiglia in area VIP, da festeggiare con i tuoi amici.
>
> Prenota: entro le 00.30 entri a un euro. Ci vediamo venerdì.

## Effetti sonori

Tutti sintetizzati in codice (`npm run sfx`), agganciati agli stessi istanti delle animazioni: fruscio metallico della moneta che segue la velocità di rotazione e tintinnio quando si ferma; salita e colpo basso sul lampo; “tink” leggero a ogni vetro che si forma; whoosh sui passaggi di foto; clic del buzzer, bip a ogni secondo del timer e jingle della vincita su 10:10; crepitio della fontana di scintille; tocco sul pulsante Prenota. In coda torna il fruscio della moneta, uguale all’inizio, per il loop. La musica la aggiungi su Instagram, a volume basso sotto la voce.

## Pubblicazione

- **Video:** `out/tenten.mp4`. **Copertina:** `out/cover.png` (“TEN:TEN · Discoteca a 1 € · Ferma su 10:10, vinci una bottiglia”).
- **Didascalia proposta:**

> A Firenze il venerdì entri in discoteca con 1 € 🪙
> TEN:TEN all’XO Club, Via Verdi 59R
> 🍸 Ogni drink è una giocata: ferma il timer su 10:10 e vinci una bottiglia in area VIP 🍾
> 🕦 23.30–5.00 · 1 € con prenotazione entro le 00.30
> 📲 Prenota dal link in bio o su WhatsApp
> 👯 Tagga chi viene con te venerdì
>
> #firenze #discotecafirenze #venerdisera #nightlifefirenze #tenten

- **Primo commento (da fissare):** “Chi riesce a fermarlo su 10:10 al primo colpo? 👀”
- **Controllo prima di pubblicare:** prezzi, orari e date sono quelli della pagina di Florence International Week al momento del montaggio; se cambiano, aggiorna `src/ui/widgets.tsx` e rigenera.
