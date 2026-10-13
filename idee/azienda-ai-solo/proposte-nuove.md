# Dieci idee nuove (072–081), alcune strampalate

**Data:** 13 ottobre 2026
**Contesto:** B1–B5 non ti convincono; B6 va avanti con il radar (`radar/`). Qui ci sono idee **diverse** da quelle viste finora, tutte con un forte motore AI e un potenziale da oltre 1 M€ senza dipendenti. Punteggi con la scheda v2 (`idee_nuove.py`). **La motivazione è una mia stima**: tra parentesi il punteggio con motivazione neutra (3).

| ID | Idea | In una frase | Scheda v2 |
|---|---|---|:--:|
| **074** | **Tutor AI per il semestre filtro di Medicina** | Esercizi infiniti nel formato esatto dell'esame, spiegati da un matematico | **4,25** (4,05) |
| **075** | **Perizia AI dell'auto usata** | Incolli l'annuncio: prezzo giusto, rischi, domande da fare, copione per trattare | **4,00** (4,00) |
| **072** | **Delitto a cena su misura** *(strampalata)* | Un giallo da giocare a una festa, scritto dall'AI sui tuoi amici | **3,95** (3,75) |
| **080** | **Seconda opinione AI sul preventivo della ristrutturazione** | Carichi il preventivo: confronto con i prezzari regionali e voci gonfiate | **3,95** (3,95) |
| 081 | Detective delle recensioni e degli sconti falsi | Il vuoto lasciato da Fakespot (chiuso a luglio 2025) | 3,70 |
| 077 | Cene tra sconosciuti abbinati dall'AI, per una nicchia | Il modello Timeleft su un pubblico preciso | 3,50 |
| 073 | Canzone-regalo personalizzata con AI | La tua storia diventa una canzone in italiano | 3,40 |
| 076 | Agente che taglia le bollette | Legge la bolletta e ti fa cambiare fornitore ogni anno | 3,40 |
| 078 | Profumo su misura disegnato dall'AI *(strampalata)* | Un questionario, una formula tua, prodotta su richiesta | 3,15 |
| 079 | Libro di viaggio impaginato dall'AI | Foto e tappe del viaggio diventano una rivista stampata | 3,15 |

---

## Le quattro in testa

### 074 · Tutor AI per il semestre filtro di Medicina
- **Il problema:** dal 2025 si entra a Medicina con il "semestre filtro": nel 2025–26 si sono iscritti in **54.313** (64.825 con Veterinaria e Odontoiatria) per circa 20–27 mila posti. Ci sono tre esami nazionali (fisica, chimica, biologia), ciascuno da 31 domande in 45 minuti, con −0,1 per ogni errore. **Fisica è la prova più temuta.** Circa due su tre restano fuori.
- **Il prodotto:** esercizi generati dall'AI **nel formato esatto** dell'esame, adattivi sulle lacune, simulazioni a tempo, spiegazioni passo per passo; probabilità di superamento stimata sui tuoi dati.
- **Perché tu:** un matematico che spiega fisica e chimica è credibile; ed è una delle idee in cui "aiutare molte persone ed essere ringraziato" è più diretto.
- **Economia:** a 149–249 € per semestre, **1 M€ = ~5.000 studenti**, cioè il ~10% degli iscritti. Le estensioni naturali (professioni sanitarie, maturità scientifica, test d'ingresso) allargano il mercato.
- **Rischi:** stagionale (si vende tra luglio e dicembre); la riforma può cambiare ancora; ChatGPT è gratis (la difesa è il formato esatto, i dati sugli errori e la fiducia); concorrenti con corsi in aula (Testbusters, Alpha Test).
- **Test rapido:** una pagina con 3 simulazioni gratuite di fisica prima del prossimo appello; misurare costo per iscritto e conversione al piano a pagamento.

### 075 · Perizia AI dell'auto usata
- **Il problema:** chi compra un'auto usata non sa se il prezzo è giusto né cosa controllare.
- **Prova che si paga:** carVertical, che vende **solo lo storico** del veicolo, ha fatturato **75,8 M€ nel 2025 (+40%)**, anche in Italia.
- **Il prodotto:** incolli il link dell'annuncio. Ricevi prezzo equo stimato su dati di mercato, incongruenze da verificare (chilometri, versioni, foto), domande per il venditore e un copione di trattativa. Si paga a report (9,90–19,90 €), con lo storico come prodotto aggiuntivo.
- **Perché tu:** è puro data science con l'AI che spiega i risultati.
- **Rischi:** **accesso ai dati.** I portali (AutoScout24, Subito) vietano lo scraping nei termini d'uso. Servono dati forniti dall'utente, fonti aperte o accordi. La motivazione è incerta (non c'è un tuo interesse dichiarato per le auto).

### 072 · Delitto a cena su misura *(strampalata)*
- **L'idea:** un "giallo con delitto" da giocare a una festa (compleanno, addio al nubilato, cena tra amici, evento aziendale), **scritto dall'AI sugli invitati veri**: nomi, manie, battute interne. Indizi sul telefono, musica e copione per ogni personaggio.
- **Prove:** il mercato dei giochi con delitto vale 1,4–2 Md$ (stime discordanti). Hunt A Killer ha fatto 27 M$ nel 2019 e ne prevedeva 50 nel 2020 (con 50 dipendenti, perché spediva scatole). Su Etsy i kit stampabili costano 12–35 $.
- **Perché può crescere da solo:** ogni partita la vedono 6–10 persone, e alcune organizzeranno la prossima. **Il passaparola è incorporato nel prodotto.**
- **Perché tu:** feste ed eventi (FIW), dinamiche sociali, creatività; persone felici per una sera.
- **Varianti dello stesso motore:** quiz "chi l'ha detto?" sul gruppo di amici, versione aziendale per il team building (199–499 €).
- **Rischi:** è un "di più", non un bisogno; la qualità narrativa deve essere alta; stagionalità (feste).

### 080 · Seconda opinione AI sul preventivo della ristrutturazione
- **Il problema:** chi ristruttura casa riceve preventivi che non sa leggere e teme di pagare troppo.
- **I dati ci sono e sono pubblici:** i **prezzari regionali** delle opere edili sono pubblicati in formato aperto (ad esempio Toscana e Piemonte).
- **Il prodotto:** carichi il PDF del preventivo. Ottieni le voci confrontate con il prezzario della tua regione, quelle fuori scala, le voci mancanti e le domande da fare all'impresa. Report a 29–79 €.
- **Perché tu (e Alberto):** matematica + AI + **un ingegnere civile** che rende il prodotto credibile. È l'unica idea in cui Alberto porta un vantaggio vero.
- **Rischi:** i prezzari sono pensati per le opere pubbliche, non per i privati (serve una correzione); responsabilità se il consiglio è sbagliato (è un'analisi, non una perizia); acquisto una tantum, quindi serve volume.

---

## Le altre, in breve
- **081 Detective delle recensioni false.** Mozilla ha chiuso Fakespot il 1/7/2025; resta poco (ReviewMeta). Rischi: termini d'uso di Amazon e regole dell'affiliazione per le estensioni del browser.
- **077 Cene tra sconosciuti.** Timeleft è in oltre 150 città (12,99 € a cena). Ti calza (eventi, dinamiche sociali), ma è in parte locale (ristoranti, imprevisti): al limite del filtro 6.
- **073 Canzone-regalo.** Songfinch (canzoni scritte da artisti, ~199 $) fattura 5–11 M$ secondo stime di terzi. Negli USA ci sono già servizi AI a 10–20 $. Si copia facilmente; le licenze dei modelli musicali vanno verificate.
- **076 Taglia-bollette.** Nel 2025 in Italia 7,7 milioni di punti di prelievo hanno cambiato fornitore; Rocket Money negli USA prende il 35–60% del risparmio del primo anno. Ma le regole di ARERA sulla vendita sono burocrazia (filtro 7), e i comparatori sono forti.
- **078 Profumo su misura.** Bello e coerente con beauty e design, ma ogni formula è un cosmetico da valutare: servirebbe una libreria di formule già valutate. È prodotto fisico.
- **079 Libro di viaggio.** Automatizzabile al 100%, ma le app di foto (Apple, Google) fanno già gran parte del lavoro gratis.

---

## Cosa ti chiedo
1. **Voto di motivazione (1–5)** per le 10 idee, anche solo per le prime 4.
2. **B6:** lancia `radar/radar_appstore.py` sul Mac e mandami il CSV, oppure apri la rete dell'ambiente cloud (istruzioni in `radar/ISTRUZIONI.md`).
3. **Meta:** completa la conferma dell'identità e il token (passi in `radar/ISTRUZIONI.md`). Sono passaggi a tuo nome che non posso fare io.

## Fonti
- Semestre filtro: [QuiFinanza](https://quifinanza.it/salute/test-medicina-2025-iscritti-semestre-filtro/922234/) · [Studenti.it](https://www.studenti.it/semestre-filtro-di-medicina-2025-26-giovedi-20-novembre-il-primo-appello-nazionale-fisica-e-la-prova-piu-temuta.html) · [Open](https://www.open.online/2025/11/20/universita-primo-appello-esami-semestre-filtro-dati-iscritti/) · [Studenti.it, idonei esclusi](https://www.studenti.it/semestre-filtro-a-medicina-perche-cosi-tanti-idonei-restano-fuori-e-cosa-possono-fare-adesso.html) · [Testbusters](https://www.testbusters.it/blog/test-medicina/test-medicina-2025-guida-aggiornata-riforma-posti-e-date)
- Auto usate: [carVertical, ricavi 2025](https://www.carvertical.com/en/blog/carvertical-revenue-growth) · [Journal de l'Automobile](https://journalauto.com/services/rapports-dhistorique-carvertical-poursuit-son-ascension/) · [Wikipedia](https://en.wikipedia.org/wiki/CarVertical)
- Giochi con delitto: [Fox Business, Hunt A Killer](https://www.foxbusiness.com/lifestyle/hunt-a-killer-murder-mystery-game-52-55-million-coronavirus) · [Starter Story](https://www.starterstory.com/stories/how-we-increased-revenue-to-50m-year-and-reached-100k-subscribers) · [Research and Markets](https://www.researchandmarkets.com/reports/6242462/murder-mystery-games-market-outlook-market) · [Verified Market Research](https://www.verifiedmarketresearch.com/product/murder-mystery-game-market/) · [Etsy, esempio](https://www.etsy.com/in-en/listing/1471531916/printable-murder-mystery-game-pack-of-4)
- Prezzari regionali: [Regione Toscana](https://www.regione.toscana.it/-/prezzario-lavori-pubblici-2025-aggiornamento-al-costo-del-lavoro-del-personale-dipendente-da-imprese-dell-edilizia) · [Regione Piemonte](https://www.regione.piemonte.it/web/media/57626/download) · [ANCE Cremona](https://cremona.ance.it/2025/06/27/circ-361-25-pubblicata-una-nuova-edizione-del-prezzario-regionale-per-le-opere-pubbliche-2025/?print=pdf)
- Fakespot: [Michael Tsai](https://mjtsai.com/blog/2025/07/02/fakespot-shuts-down) · [The Desk](https://thedesk.net/2025/05/mozilla-shutting-down-pocket-fakespot/) · [Feedbagel](https://feedbagel.com/post/fakespot-shuts-down-impact-on-fake-review-crisis)
- Timeleft: [Brussels Times](https://brusselstimes.com/1160308/table-for-six-strangers-fighting-urban-loneliness-over-dinner) · [Connexion France](https://www.connexionfrance.com/news/how-to-meet-new-people-over-dinner-in-france-we-try-out-new-app/682998) · [Paperjam](https://en.paperjam.lu/article/meet-five-likeminded-strangers)
- Canzoni: [Music Business Worldwide, Songfinch](https://musicbusinessworldwide.com/the-weeknd-backed-personalized-song-creation-firm-songfinch-raises-17m) · [Prospeo](https://prospeo.io/c/songfinch) · [Songive](https://www.accessnewswire.com/newsroom/en/business-and-professional-services/songive-launches-ai-powered-platform-that-turns-personal-stories-1184631) · [GiftSong](https://www.toolmage.com/en/tool/giftsong/)
- Bollette: [ComparaSemplice, dati ARERA 2025](https://www.comparasemplice.it/informazioni/energia/cambio-fornitore-luce-cosa-dicono-i-dati-arera-sul-2025) · [Rocket Money](https://help.rocketmoney.com/en/articles/9744501-how-do-you-lower-my-bill) · [Atlanta News First](https://www.atlantanewsfirst.com/2026/07/10/online-bill-negotiators-promise-savings-require-personal-data-access/)
- Classifiche app AI (per B6): [Marlvel, classifiche USA](https://marlvel.ai/rankings/us/ios/all-grossing/2026-07-17) · [Sensor Tower, previsioni 2026](https://investgame.net/wp-content/uploads/2025/12/2025-12-11-2025_12_10_SensorTower_Digital_Economy_Predictions_2026_26_pgs-1.pdf) · [Statista](https://www.statista.com/statistics/1607386/top-ai-app-segments-by-consumer-spend)
