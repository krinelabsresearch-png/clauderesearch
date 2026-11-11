# 258: le 50 attività del centro di Firenze da contattare per un sito (11/11/2026)

Collegato a [258-categorie-siti.md](258-categorie-siti.md). Gli script sono in [../centro_firenze_258/](../centro_firenze_258/).

## In breve
- Nel centro di Firenze ho valutato **tutte le attività trovabili su Google Maps senza un sito proprio: 2.688 candidate**, su 8.818 schede raccolte.
- Ognuna ha due punteggi da 0 a 100:
  - **Beneficio**: quanto un sito la farebbe guadagnare;
  - **Propensione**: quanto è probabile che lo compri.
- La classifica è per **Beneficio × Propensione / 100**.
- Le prime 168 sono state verificate una per una con Codex (modello GPT-6-Luna, con ricerca web). **Il 32% aveva in realtà un sito o faceva parte di una catena o di un hotel**, e l'ho tolto.
- In cima ci sono tre tipi di attività:
  - **attività aperte da poco**, con solo Instagram (un ristorante in San Frediano, un fotografo, una riflessologa);
  - **attività che avevano un sito e l'hanno perso**: siti gratuiti di Google chiusi nel 2024, pagine Google Sites, o un dominio email proprio senza un sito;
  - **botteghe ed enoteche** con clienti quasi solo stranieri.

## Area e raccolta
- **Area:** entro 1,8 km dal Duomo. Comprende il centro storico dentro i viali, l'Oltrarno fino a San Frediano, Porta Romana e San Niccolò, e la prima fascia fuori dai viali (Libertà, Masaccio, Don Minzoni).
- **Raccolta:** Google Places API, ricerca testuale su circa 150 tipi di attività: tutte le categorie della classifica di 258, più negozi, artigiani, professionisti, medici, servizi, ricettività, eventi, onoranze funebri e veterinari. Nessuna categoria esclusa a priori.
  - Quando una ricerca arrivava al tetto di 60 risultati, l'area veniva divisa in 4 riquadri, e se serviva ancora in 16.
  - Le categorie con B da 50 in su sono state coperte tutte con i riquadri. Quelle con B fino a 45 (ristoranti, bar, parrucchieri, barbieri, avvocati, alimentari e alcuni negozi) solo in parte: vedi i limiti.
- **Sito:** "senza sito proprio" vuol dire nessun sito sulla scheda, oppure solo un social o un portale (Facebook, Instagram, Linktree, Booking, MioDottore, Treatwell e simili). Su 8.818 schede: 5.508 con un sito proprio, 2.627 senza nulla, 249 solo social, 434 solo portale.

## Esclusioni (solo i criteri concordati)
| Criterio | Escluse |
|---|---|
| Chiusa (scheda Google o fonti recenti) | 1 |
| Scheda ferma: ultima recensione più vecchia di 18 mesi | 293 |
| Catena o franchising (nome presente in 3 o più sedi, o marchio noto) | 329 |
| Verifica con Codex: ha già un sito proprio non collegato alla scheda | 31 |
| Verifica con Codex: fa parte di una catena, un hotel o un gruppo con un sito | 22 |

- **Non ho escluso le attività con poche recensioni**: chi ha appena aperto è proprio un buon contatto.
- **Chi ha solo un sito gratuito** (Google Sites, il vecchio `business.site` chiuso da Google nel 2024, Wix gratuito, eatbu) **non è escluso**: conta come "ha già provato ad avere un sito".

## Come sono calcolati i punteggi

**Beneficio (0–100)**
| Voce | Punti | Come si misura |
|---|---|---|
| Categoria | fino a 25 | B della classifica 258 × 25/90. Per i nuovi tipi ho dato una B stimata con lo stesso metodo: antiquari e gallerie 60, medici specialisti 60, architetti 65, NCC e transfer 70, artigiani di riparazione 45, negozi 35, servizi vari 25. |
| Domanda persa | 0 / 8 / 15 | Frasi nelle recensioni come "non rispondono", "difficile da trovare", "orari sbagliati", "hard to reach" |
| Concorrenti con un sito | fino a 15 | Quota di attività della stessa categoria entro 500 m che hanno un sito proprio |
| Clienti stranieri | fino a 10 | Quota di recensioni scritte in una lingua diversa dall'italiano |
| Valore del lavoro | 2–10 | Fascia di prezzo di Google; se manca, 8 per i lavori su preventivo e 4 per gli altri |
| Commissioni a piattaforme | 0 / 4 / 10 | 10 se la scheda rimanda a Booking, MioDottore, Treatwell e simili; 4 se la categoria di solito li usa |
| Reputazione | 0 / 5 / 10 | 10 con voto almeno 4,3 e almeno 30 recensioni; 5 con voto almeno 4,0 e almeno 10 recensioni |
| Già pieno | −10 | Recensioni come "sempre pieno" o "prenotare con largo anticipo", oppure più di 1.000 recensioni |

**Propensione (0–100)**
| Voce | Punti | Come si misura |
|---|---|---|
| Scheda curata | fino a 25 | Orari presenti (8), almeno 10 foto (7), foto caricate dal titolare (10) |
| Aperta da poco | 0 / 10 / 20 | 20 se tutte le recensioni lette sono degli ultimi 18 mesi e sono meno di 100 in totale |
| Social o portale come unico sito | 0 / 10 / 20 | 20 se il link sulla scheda è un social, 10 se è un portale |
| Sito rotto o dominio senza sito | 0 / 20 | Sito gratuito o dismesso, oppure email con un dominio proprio ma nessun sito (verifica Codex) |
| Dimensione | fino a 15 | Telefono fisso (7) e almeno 50 recensioni (8). 15 se ha due sedi. |

Rispetto ai criteri proposti mancano **"risponde alle recensioni"** ed **"età del titolare"**: l'API ufficiale di Google non fornisce le risposte del titolare, e l'età non è misurabile. I loro punti non sono stati redistribuiti.

## Le 50 attività

Legenda delle colonne:
- **Beneficio:** Cat. = categoria; Dom. persa = domanda persa; Conc. con sito = concorrenti con un sito; Stran. = clienti stranieri; Valore; Comm. = commissioni; Reput. = reputazione; Già pieno.
- **Propensione:** Scheda curata; Nuova = aperta da poco; Social/portale; Sito rotto/dominio; Dimens. = dimensione.

Il nome rimanda alla scheda Google Maps.

| # | Attività | Categoria (B) | Zona | Presenza online | Voto (recensioni) | Cat. | Dom. persa | Conc. con sito | Stran. | Valore | Comm. | Reput. | Già pieno | **Beneficio** | Scheda curata | Nuova | Social/portale | Sito rotto/dominio | Dimens. | **Propensione** | **B×P/100** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | [Essence Hotel](https://maps.google.com/?cid=9164822320976237353&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Hotel (90) | Piazza della Indipendenza (0,9 km) | nessuno + dominio email proprio | 4,6 (64) | 25 | 0 | 12 | 10 | 4 | 4 | 10 | 0 | **65** | 7 | 20 | 0 | 20 | 15 | **62** | **40,3** |
| 2 | [La Vecchia Maniera](https://maps.google.com/?cid=15093142812836181429&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Ristoranti e trattorie (45) | Borgo S. Frediano (1,0 km) | solo social | 5 (50) | 12,5 | 0 | 11,7 | 10 | 6 | 4 | 10 | 0 | **54,2** | 15 | 20 | 20 | 0 | 15 | **70** | **37,9** |
| 3 | [Settembre Photo Studio](https://maps.google.com/?cid=11977042454209722966&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Fotografi e videomaker (80) | Viale Don Giovanni Minzoni (1,5 km) | solo social | 5 (16) | 22,2 | 0 | 10,7 | 3,8 | 8 | 0 | 5 | 0 | **49,7** | 25 | 20 | 20 | 0 | 7 | **72** | **35,8** |
| 4 | [Prestigio by Leather Point](https://maps.google.com/?cid=818177597863800439&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Botteghe artigiane artistiche (60) | Via de' Pucci (0,2 km) | nessuno + sito gratuito/dismesso | 4,8 (35) | 16,7 | 0 | 10,8 | 8,3 | 8 | 0 | 10 | 0 | **53,8** | 25 | 10 | 0 | 20 | 11 | **66** | **35,5** |
| 5 | [Studio Fotografico Sandro Michahelles](https://maps.google.com/?cid=902770136113101860&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Fotografi e videomaker (80) | Via di S. Niccolò (0,9 km) | solo social + sito gratuito/dismesso | 5 (15) | 22,2 | 0 | 6,4 | 4,4 | 8 | 0 | 5 | 0 | **46** | 25 | 0 | 20 | 20 | 11 | **76** | **35** |
| 6 | [The Hidden Pub](https://maps.google.com/?cid=12884081517978739182&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Bar e caffè (15) | Piazza del Carmine (1,0 km) | solo social + sito gratuito/dismesso | 4,4 (502) | 4,2 | 8 | 5,3 | 10 | 6 | 0 | 10 | 0 | **43,5** | 25 | 0 | 20 | 20 | 15 | **80** | **34,8** |
| 7 | [SoFa il Vino](https://maps.google.com/?cid=5082489545679601288&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Cantine ed enoteche (70) | Via dei Banchi (0,4 km) | solo social | 5 (101) | 19,4 | 0 | 12,9 | 10 | 4 | 0 | 10 | 0 | **56,3** | 25 | 0 | 20 | 0 | 15 | **60** | **33,8** |
| 8 | [Simona Di Trapani - Riflessologia plantare - Firenze -](https://maps.google.com/?cid=18040628358539748191&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Centri estetici e nail (45) | Via Masaccio (1,5 km) | solo social | 5 (31) | 12,5 | 0 | 13 | 2 | 4 | 4 | 10 | 0 | **45,5** | 25 | 20 | 20 | 0 | 7 | **72** | **32,8** |
| 9 | [Trattoria Sostanza](https://maps.google.com/?cid=1434597985181864841&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Ristoranti e trattorie (45) | Via del Porcellana (0,7 km) | solo social | 4,5 (1199) | 12,5 | 8 | 11,5 | 5 | 10 | 4 | 10 | -10 | **51** | 25 | 0 | 20 | 0 | 15 | **60** | **30,6** |
| 10 | [Oreficeria Romano](https://maps.google.com/?cid=12648299608131584099&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Botteghe artigiane artistiche (60) | Via de' Cerretani (0,2 km) | nessuno + dominio email proprio | 4,5 (62) | 16,7 | 0 | 11,2 | 5 | 8 | 0 | 10 | 0 | **50,9** | 25 | 0 | 0 | 20 | 15 | **60** | **30,5** |
| 11 | [Be You Nails & Beauty Firenze](https://maps.google.com/?cid=10288654870438256432&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Centri estetici e nail (45) | Via Santa Caterina D'Alessandria (0,9 km) | solo social | 5 (36) | 12,5 | 0 | 6,4 | 5 | 4 | 4 | 10 | 0 | **41,9** | 25 | 20 | 20 | 0 | 7 | **72** | **30,2** |
| 12 | [Foto Ottica Fani](https://maps.google.com/?cid=6852426741631492873&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Ottici (45) | Via Giuseppe Verdi (0,6 km) | solo social | 4,9 (55) | 12,5 | 0 | 12 | 10 | 4 | 0 | 10 | 0 | **48,5** | 25 | 0 | 20 | 0 | 15 | **60** | **29,1** |
| 13 | [La Bottega d'arte di Emma Draghi](https://maps.google.com/?cid=5424405422585170652&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Botteghe artigiane artistiche (60) | Costa S. Giorgio (0,8 km) | solo social | 4,9 (34) | 16,7 | 0 | 10,2 | 10 | 8 | 0 | 10 | 0 | **54,9** | 15 | 10 | 20 | 0 | 7 | **52** | **28,5** |
| 14 | [Firenze Ink Tattoo Studio](https://maps.google.com/?cid=11114358262694810166&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Tatuatori (40) | Via Ventisette Aprile (0,7 km) | solo social | 4,8 (221) | 11,1 | 0 | 11,2 | 5 | 10 | 0 | 10 | 0 | **47,3** | 25 | 0 | 20 | 0 | 15 | **60** | **28,4** |
| 15 | [Liliana & Alessandro Leather Factory](https://maps.google.com/?cid=5550828651212433802&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Botteghe artigiane artistiche (60) | Via Sant'Antonino (0,4 km) | solo social | 4,4 (47) | 16,7 | 0 | 11,5 | 8,3 | 8 | 0 | 10 | 0 | **54,5** | 25 | 0 | 20 | 0 | 7 | **52** | **28,3** |
| 16 | [Ristorante Tang Anatra Pechinese大唐朝北京烤鸭](https://maps.google.com/?cid=8405889577237262523&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Ristoranti e trattorie (45) | Via Ventisette Aprile (0,6 km) | solo social | 4,3 (431) | 12,5 | 0 | 9,5 | 5 | 6 | 4 | 10 | 0 | **47** | 25 | 0 | 20 | 0 | 15 | **60** | **28,2** |
| 17 | [Ginevra Gemmi Gioielli](https://maps.google.com/?cid=16224909223367812025&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Botteghe artigiane artistiche (60) | Via della Chiesa (1,2 km) | solo social | 5 (102) | 16,7 | 0 | 9,8 | 5 | 8 | 0 | 10 | 0 | **49,5** | 25 | 0 | 20 | 0 | 11 | **56** | **27,7** |
| 18 | [ZionFade Beauty Salon / Barber Shop](https://maps.google.com/?cid=14125758037423687771&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Barbieri (35) | Via Palazzuolo (0,7 km) | nessuno | 4,8 (42) | 9,7 | 0 | 15 | 8,3 | 6 | 4 | 10 | 0 | **53** | 25 | 20 | 0 | 0 | 7 | **52** | **27,6** |
| 19 | [Fermino](https://maps.google.com/?cid=12286249126492310271&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Ristoranti e trattorie (45) | Borgo Santa Croce (0,7 km) | solo social | 4,7 (254) | 12,5 | 0 | 11,7 | 5 | 6 | 4 | 10 | 0 | **49,2** | 25 | 0 | 20 | 0 | 11 | **56** | **27,6** |
| 20 | [Bottega Il Fiorino Artigiana](https://maps.google.com/?cid=16404872059889294079&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Botteghe artigiane artistiche (60) | Lungarno della Zecca Vecchia (0,9 km) | nessuno | 5 (22) | 16,7 | 0 | 10,7 | 8,3 | 8 | 0 | 5 | 0 | **48,7** | 25 | 20 | 0 | 0 | 11 | **56** | **27,3** |
| 21 | [Cherie Cherie Estetica](https://maps.google.com/?cid=14940204554461108740&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Centri estetici e nail (45) | Via Cimabue (1,4 km) | solo portale + sito gratuito/dismesso | 4,7 (42) | 12,5 | 0 | 10,7 | 0 | 4 | 4 | 10 | 0 | **41,2** | 25 | 0 | 10 | 20 | 11 | **66** | **27,2** |
| 22 | [MAYRA Pelletteria](https://maps.google.com/?cid=4284109739490216333&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Botteghe artigiane artistiche (60) | Via dei Leoni (0,5 km) | nessuno | 5 (30) | 16,7 | 0 | 10,4 | 10 | 8 | 0 | 10 | 0 | **55,1** | 22 | 20 | 0 | 0 | 7 | **49** | **27** |
| 23 | [I'Brindellone](https://maps.google.com/?cid=16089370671856876055&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Ristoranti e trattorie (45) | Piazza Piattellina (1,2 km) | solo social | 4,7 (3815) | 12,5 | 0 | 12,4 | 10 | 6 | 4 | 10 | -10 | **44,9** | 25 | 0 | 20 | 0 | 15 | **60** | **26,9** |
| 24 | [Rikiphotos – Wedding Photography & Films 📍 Venice • Lake Como • Milan • Florence • Rome • All Italy](https://maps.google.com/?cid=5781953037977418631&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Fotografi e videomaker (80) | P.za della Signoria (0,3 km) | solo social | 5 (3) | 22,2 | 0 | 10 | 0 | 8 | 0 | 0 | 0 | **40,2** | 24 | 20 | 20 | 0 | 3 | **67** | **26,9** |
| 25 | [Domus Plaza](https://maps.google.com/?cid=3824361473017090448&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | B&B, affittacamere, case vacanza (60) | Via dei Bonizzi (0,1 km) | solo social | 4,7 (99) | 16,7 | 0 | 10,9 | 10 | 4 | 4 | 10 | 0 | **55,6** | 17 | 0 | 20 | 0 | 11 | **48** | **26,7** |
| 26 | [Schiaccia Bistrò San Frediano](https://maps.google.com/?cid=2766405846379806963&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Ristoranti e trattorie (45) | Via Pisana (1,3 km) | solo social | 5 (4) | 12,5 | 0 | 11,9 | 2,5 | 6 | 4 | 0 | 0 | **36,9** | 25 | 20 | 20 | 0 | 7 | **72** | **26,6** |
| 27 | [Parrucchiere The Final Cut](https://maps.google.com/?cid=17968364887056054935&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Parrucchieri (35) | Via dei Macci (0,9 km) | solo social | 4,6 (73) | 9,7 | 0 | 11,2 | 5 | 4 | 4 | 10 | 0 | **43,9** | 25 | 0 | 20 | 0 | 15 | **60** | **26,3** |
| 28 | [Osteria La Dolce Vita Firenze](https://maps.google.com/?cid=17821317301468674019&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Ristoranti e trattorie (45) | Via dei Tavolini (0,2 km) | solo social | 4,8 (1664) | 12,5 | 0 | 11,3 | 10 | 6 | 4 | 10 | -10 | **43,8** | 25 | 0 | 20 | 0 | 15 | **60** | **26,3** |
| 29 | [Pelletteria Valeria](https://maps.google.com/?cid=3255480879473041984&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Botteghe artigiane artistiche (60) | Borgo Ognissanti (1,0 km) | solo social | 4,9 (88) | 16,7 | 0 | 12,8 | 5 | 8 | 0 | 10 | 0 | **52,5** | 15 | 0 | 20 | 0 | 15 | **50** | **26,2** |
| 30 | [Pelletteria Del Corso](https://maps.google.com/?cid=3553098292889311896&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Botteghe artigiane artistiche (60) | Via del Corso (0,2 km) | nessuno | 4,9 (94) | 16,7 | 0 | 10,6 | 5 | 8 | 0 | 10 | 0 | **50,3** | 17 | 20 | 0 | 0 | 15 | **52** | **26,2** |
| 31 | [Essential Mix](https://maps.google.com/?cid=2624112747633481821&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Parrucchieri (35) | Via Santa Caterina D'Alessandria (0,9 km) | solo social | 4,8 (94) | 9,7 | 0 | 10,7 | 5 | 4 | 4 | 10 | 0 | **43,4** | 25 | 0 | 20 | 0 | 15 | **60** | **26** |
| 32 | [Vecchio Lotto](https://maps.google.com/?cid=12180971995087588087&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Botteghe artigiane artistiche (60) | Via dello Studio (0,1 km) | solo social | 5 (8) | 16,7 | 0 | 11 | 10 | 8 | 0 | 0 | 0 | **45,7** | 20 | 10 | 20 | 0 | 7 | **57** | **26** |
| 33 | [L'Osteria Cucina Casalinga](https://maps.google.com/?cid=7328096454827639909&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Ristoranti e trattorie (45) | Via dei Neri (0,6 km) | solo social | 4,6 (1780) | 12,5 | 0 | 11,7 | 5 | 10 | 4 | 10 | -10 | **43,2** | 25 | 0 | 20 | 0 | 15 | **60** | **25,9** |
| 34 | [San Frediano Boutique Hotel](https://maps.google.com/?cid=3670231397039257750&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Hotel (90) | Borgo S. Frediano (1,2 km) | nessuno | 4,5 (27) | 25 | 0 | 10,9 | 10 | 4 | 4 | 5 | 0 | **58,9** | 17 | 20 | 0 | 0 | 7 | **44** | **25,9** |
| 35 | [Trattoria Antichi Cancelli Firenze](https://maps.google.com/?cid=7527511787966869030&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Ristoranti e trattorie (45) | Via Faenza (0,5 km) | solo social | 4,6 (1184) | 12,5 | 0 | 10,7 | 10 | 6 | 4 | 10 | -10 | **43,2** | 25 | 0 | 20 | 0 | 15 | **60** | **25,9** |
| 36 | [Holy Ink Tattoo Atelier](https://maps.google.com/?cid=11938715116561573122&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Tatuatori (40) | V.le Spartaco Lavagnini (1,1 km) | solo social | 5 (648) | 11,1 | 0 | 10 | 5 | 10 | 0 | 10 | 0 | **46,1** | 25 | 0 | 20 | 0 | 11 | **56** | **25,8** |
| 37 | [Trattoria Verdi Firenze](https://maps.google.com/?cid=13153388872106303928&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Ristoranti e trattorie (45) | Via Giuseppe Verdi (0,6 km) | solo social | 4,8 (1629) | 12,5 | 0 | 11,5 | 5 | 10 | 4 | 10 | -10 | **43** | 25 | 0 | 20 | 0 | 15 | **60** | **25,8** |
| 38 | [Wine Window Orcagna - Buchetta del vino](https://maps.google.com/?cid=1043065896529610513&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Bar e caffè (15) | Chiasso dei Baroncelli (0,4 km) | solo social | 4,6 (134) | 4,2 | 8 | 8,6 | 10 | 2 | 0 | 10 | 0 | **42,8** | 25 | 0 | 20 | 0 | 15 | **60** | **25,7** |
| 39 | [Osteria Vecchio Cancello](https://maps.google.com/?cid=2303778393415095841&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Ristoranti e trattorie (45) | Via Guelfa (0,8 km) | solo social | 4,8 (2698) | 12,5 | 0 | 10,7 | 5 | 10 | 4 | 10 | -10 | **42,2** | 25 | 0 | 20 | 0 | 15 | **60** | **25,3** |
| 40 | [Vino Divino](https://maps.google.com/?cid=13879312668234363120&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Cantine ed enoteche (70) | Via Taddea (0,4 km) | solo social | 5 (205) | 19,4 | 0 | 12 | 5 | 4 | 0 | 10 | 0 | **50,4** | 15 | 0 | 20 | 0 | 15 | **50** | **25,2** |
| 41 | [Y beauty lab](https://maps.google.com/?cid=16341638291703954580&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Centri estetici e nail (45) | Via della Vigna Nuova (0,5 km) | nessuno | 4,6 (93) | 12,5 | 0 | 9,1 | 5 | 4 | 4 | 10 | 0 | **44,6** | 25 | 20 | 0 | 0 | 11 | **56** | **25** |
| 42 | [Celeste's House Serviced Apartments](https://maps.google.com/?cid=11233265732255403482&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | B&B, affittacamere, case vacanza (60) | Viale Belfiore (1,5 km) | solo portale | 4,8 (73) | 16,7 | 0 | 9,2 | 10 | 4 | 4 | 10 | 0 | **53,9** | 25 | 0 | 10 | 0 | 11 | **46** | **24,8** |
| 43 | [Nail salon Michelle](https://maps.google.com/?cid=15890882321854649051&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Centri estetici e nail (45) | Via Palazzuolo (0,8 km) | solo social | 4,8 (498) | 12,5 | 0 | 8,4 | 5 | 4 | 4 | 10 | 0 | **43,9** | 25 | 0 | 20 | 0 | 11 | **56** | **24,6** |
| 44 | [Pilates Loto Studio](https://maps.google.com/?cid=8843246562682172703&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Palestre, yoga, pilates (55) | Via dei Pilastri (0,8 km) | nessuno | 5 (35) | 15,3 | 0 | 13 | 5 | 4 | 0 | 10 | 0 | **47,3** | 25 | 20 | 0 | 0 | 7 | **52** | **24,6** |
| 45 | [Vecchio Carlino 1919](https://maps.google.com/?cid=2526103673082403467&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Ristoranti e trattorie (45) | Viale Fratelli Rosselli (1,4 km) | solo social | 4,1 (660) | 12,5 | 0 | 11,8 | 10 | 6 | 4 | 5 | 0 | **49,3** | 15 | 0 | 20 | 0 | 15 | **50** | **24,6** |
| 46 | [Fate Più Balocchi](https://maps.google.com/?cid=11264178374287896413&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Negozi (35) | Via Lorenzo Bartolini (1,2 km) | solo social | 4,7 (50) | 9,7 | 0 | 6,9 | 10 | 4 | 0 | 10 | 0 | **40,6** | 25 | 0 | 20 | 0 | 15 | **60** | **24,4** |
| 47 | [Clés de Florence](https://maps.google.com/?cid=3320104466970352329&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Hotel (90) | Via S. Zanobi (0,7 km) | solo portale | 4 (38) | 25 | 0 | 11,9 | 5 | 4 | 4 | 5 | 0 | **54,9** | 17 | 10 | 10 | 0 | 7 | **44** | **24,2** |
| 48 | [AB Normal Tattoo & Piercing](https://maps.google.com/?cid=1135634585189637932&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Tatuatori (40) | Via dei Servi (0,3 km) | solo social | 4,9 (136) | 11,1 | 0 | 9 | 5 | 10 | 0 | 10 | 0 | **45,1** | 25 | 0 | 20 | 0 | 8 | **53** | **23,9** |
| 49 | [Edith Estetica Avanzata](https://maps.google.com/?cid=18375387762960836468&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Centri estetici e nail (45) | V.le Giovanni Milton (1,5 km) | solo social | 4,4 (53) | 12,5 | 0 | 5,5 | 4,4 | 4 | 4 | 10 | 0 | **40,4** | 23 | 0 | 20 | 0 | 15 | **58** | **23,4** |
| 50 | [Bar Uffizi](https://maps.google.com/?cid=8880399482706088378&g_mp=Cidnb29nbGUubWFwcy5wbGFjZXMudjEuUGxhY2VzLlNlYXJjaFRleHQQAhgEIAA) | Bar e caffè (15) | Via Lambertesca (0,5 km) | solo social | 4,8 (325) | 4,2 | 0 | 8,5 | 10 | 6 | 0 | 10 | 0 | **38,7** | 25 | 0 | 20 | 0 | 15 | **60** | **23,2** |

## Le prime 10 nel dettaglio

### 1. Essence Hotel, Piazza della Indipendenza (Beneficio 65, Propensione 62, punteggio 40,3)
- **Perché il sito gli serve:** è un hotel (B=90) senza alcun sito. Le recensioni lette sono tutte in inglese, dal 2026, voto 4,6 su 64. Ogni prenotazione passa quindi da Booking o Expedia, con commissioni intorno al 15–20%. In un raggio di 500 m l'80% dei 65 alloggi ha un sito proprio.
- **Perché potrebbe accettare:** Codex ha trovato l'email `info@essencehotel.it`, quindi **il dominio ce l'hanno già ma non lo usano**. Le recensioni sono tutte recenti, il che fa pensare a un'apertura o a un cambio di gestione da poco.
- **Cosa proporre:** un sito multilingue sul loro dominio, con prenotazione diretta e un piccolo sconto per chi prenota lì. Il messaggio: "ogni camera prenotata sul sito risparmia la commissione di Booking".
- **Da controllare prima:** Codex ha trovato un marchio "Essence Hotels" senza poter confermare che l'hotel ne faccia parte. La scheda è poco curata: nessuna foto del titolare e self check-in, quindi forse è gestito da una società di affitti.

### 2. La Vecchia Maniera, Borgo San Frediano (54, 70, 37,9)
- **Perché il sito gli serve:** ristorante con 50 recensioni, tutte da 5 stelle e tutte tra settembre e ottobre 2026. È aperto da poche settimane. I clienti sono turisti ("hole in the wall", "owner incredibly friendly"). Fra i 114 ristoranti nel raggio di 500 m, il 78% ha un sito.
- **Perché potrebbe accettare:** è appena aperto e sta costruendo la propria immagine: ha solo Instagram e un telefono fisso. È il momento in cui un titolare decide come farsi trovare.
- **Cosa proporre:** un sito semplice con menù, storia del posto, foto, prenotazione e versione in inglese, collegato alla scheda Google, da consegnare in pochi giorni.
- **Da sapere:** sulla scheda ci sono ancora poche foto caricate dal titolare.

### 3. Settembre Photo Studio, Viale Don Minzoni (50, 72, 35,8)
- **Perché il sito gli serve:** fotografo di matrimoni e battesimi. Per questa categoria il sito conta moltissimo (B=80), perché le coppie vogliono vedere il portfolio e i pacchetti prima di contattare. Ha 16 recensioni da 5 stelle, alcune di coppie straniere che si sposano in Toscana.
- **Perché potrebbe accettare:** ha solo Instagram, ha aperto da poco (recensioni da ottobre 2025), cura la scheda con foto proprie e lavora su preventivi alti.
- **Cosa proporre:** sito portfolio in italiano e inglese, con pacchetti, modulo di preventivo e pagine "matrimonio a Firenze" e "matrimonio nel Chianti" per farsi trovare su Google dagli stranieri.
- **Da sapere:** è un professionista da solo, con un cellulare: il budget potrebbe essere limitato.

### 4. Prestigio by Leather Point, Via de' Pucci, a 160 m dal Duomo (54, 66, 35,5)
- **Perché il sito gli serve:** pelletteria con voto 4,8 su 35. Quasi tutte le recensioni recenti sono di turisti americani ("best experience buying leather goods"). Il 75% delle 52 attività simili intorno ha un sito.
- **Perché potrebbe accettare:** **ha già provato**: esiste una pagina Google Sites fatta da loro, con un'email Gmail. Sa che serve, ma non ha un sito vero.
- **Cosa proporre:** vetrina in inglese con catalogo e spedizioni internazionali. Il cliente straniero, tornato a casa, può ricomprare.

### 5. Studio Fotografico Sandro Michahelles, Via di San Niccolò (46, 76, 35,0)
- **Perché il sito gli serve:** studio di ritratto (B=80) con 15 recensioni da 5 stelle. Fra queste, turisti di passaggio che si sono fatti fare il ritratto di famiglia.
- **Perché potrebbe accettare:** ha la Propensione più alta fra le prime 10. **Aveva un sito `business.site`, il servizio gratuito che Google ha chiuso nel 2024**: il link oggi non funziona. Usa Instagram e cura la scheda.
- **Cosa proporre:** "il suo vecchio sito Google non esiste più, glielo rifaccio": portfolio, ritratti per turisti con prenotazione, versione in inglese.

### 6. The Hidden Pub, Piazza del Carmine (43,5, 80, 34,8)
- **Perché è in alto:** soprattutto per la Propensione, che è la massima della classifica. Ha un mini-sito gratuito su eatbu, Facebook, scheda curata, 502 recensioni e un telefono fisso. Una recensione dice "a little hard to find".
- **Limite:** è un pub (B=15), e per un pub il sito fa vendere poco: il Beneficio è il più basso delle prime 10.
- **Cosa proporre:** solo un'offerta molto economica. Una pagina con birre alla spina, eventi e partite in TV, mappa per trovarlo.

### 7. SoFa il Vino, Via dei Banchi (56, 60, 33,8)
- **Perché il sito gli serve:** enoteca con degustazioni, 101 recensioni da 5 stelle, clienti quasi solo stranieri. Nelle recensioni si nomina sempre il titolare, Fabio, che "spiega i vini del Chianti".
- **Perché potrebbe accettare:** ha solo un Linktree, scheda curata, telefono fisso.
- **Cosa proporre:** due cose che possono rendere: **prenotazione delle degustazioni** sul sito, e **spedizione del vino all'estero** per chi l'ha assaggiato in negozio.

### 8. Simona Di Trapani, riflessologia plantare, Via Masaccio (45,5, 72, 32,8)
- **Perché il sito gli serve:** 31 recensioni da 5 stelle, dal novembre 2025. Il 92% delle attività simili intorno ha un sito.
- **Perché potrebbe accettare:** ha aperto da poco, ha solo Facebook e cura la scheda. Le recensioni parlano di trattamenti per il dolore, cioè di un servizio che va spiegato prima che il cliente prenoti.
- **Cosa proporre:** un sito con la spiegazione dei trattamenti e la prenotazione online.
- **Da sapere:** lavora da sola, con un cellulare: il budget è basso, va fatta un'offerta piccola.

### 9. Trattoria Sostanza, Via del Porcellana (51, 60, 30,6)
- **Perché è in classifica:** per i criteri ci sta. Trattoria storica, fascia di prezzo alta, ha solo Instagram, e l'86% dei ristoranti intorno ha un sito.
- **Ma va contattata per ultima:** è già piena ("make sure to book ahead", "they were full"), e ha già i −10 di "già pieno". La mancanza del sito è probabilmente una scelta.
- **Unico argomento sensato:** meno telefonate, con una pagina per le prenotazioni e le informazioni pratiche.

### 10. Oreficeria Romano, Via de' Cerretani, a 230 m dal Duomo (51, 60, 30,5)
- **Perché il sito gli serve:** gioielleria e orologeria con voto 4,5 su 62. I turisti ci comprano cammei e gioielli, "handmade quality". Il 77% delle 69 attività simili intorno ha un sito.
- **Perché potrebbe accettare:** usa l'email `romano@ilgigliodoro.com`, quindi **ha un dominio proprio senza un sito**. Ha anche telefono fisso, scheda curata e molte recensioni.
- **Cosa proporre:** un sito vetrina sul dominio che hanno già, con una sezione in inglese.
- **Da controllare prima:** "Il Giglio d'Oro" potrebbe essere il nome di un gruppo con altri negozi.

## Limiti
- **Clienti stranieri sottostimati all'inizio:** chiedendo le recensioni in italiano, Google mette davanti quelle in italiano. Per le prime 378 candidate ho letto anche le recensioni in inglese (10 in tutto). Per le altre, 5 recensioni in lingua mista.
- **1.643 candidate valutate senza recensioni:** 813 non ne hanno nessuna. Per le altre ho stimato le voci mancanti con la media della loro categoria, e ho letto le recensioni delle 150 con la stima più alta. Nessuna delle restanti arriva vicino alla cinquantesima posizione.
- **Copertura incompleta per le categorie con B fino a 45:** ristoranti, bar, parrucchieri, barbieri, avvocati, commercialisti, alimentari e alcuni negozi. Per loro ho le prime 60 attività per ricerca, ma senza la divisione in riquadri. Ne mancano alcune, soprattutto ristoranti.
- **Siti rotti trovati solo in parte:** la rete di questa sessione blocca la visita diretta dei siti, quindi li ho trovati solo tramite la ricerca di Codex. Anche l'attività su Instagram, nella maggior parte dei casi, non è stata verificabile.
- **Le B dei nuovi tipi di attività sono mie stime.**
- **Fra le candidate non verificate, oltre la cinquantesima posizione, circa una su tre potrebbe avere un sito.** Nella top 50 sono state verificate tutte.
- **Dati da aggiornare prima di usarli:** le condizioni d'uso di Google Places non consentono di conservare a lungo i dati delle schede. Nel documento ci sono solo nomi, vie e link alla scheda, da riaprire prima di ogni contatto.
- **Per contattarle:** vale quanto già scritto in 258-categorie-siti.md. Le telefonate commerciali sono soggette al Registro pubblico delle opposizioni, quindi meglio di persona (sono tutte in centro) o per email aziendale.

## Costo della ricerca
- **Google Places:** circa 1.240 ricerche testuali e 1.128 letture di dettaglio. Una parte potrebbe aver superato la soglia gratuita mensile: va controllato su Google Cloud.
- **Codex con GPT-6-Luna:** 17 esecuzioni di verifica, fatte con l'account ChatGPT di Lorenzo.
