// Genera GUION.md dagli stessi dati che usa il video (src/script.ts),
// così tempi del copione e sottotitoli coincidono al fotogramma.
// Uso: npm run guion
import {writeFileSync} from 'node:fs';
import {DURATION_FRAMES, FPS, TIMELINE} from '../src/script.ts';
import {VOICE} from '../src/voice-timings.ts';

type SceneNotes = {title: string; goal: string; transition: string; beats: string[]};

// Una descrizione visiva per ogni frase, nello stesso ordine di src/script.ts.
const NOTES: Record<string, SceneNotes> = {
  hook: {
    title: 'Gancio + cos’è un ETF',
    goal: 'Fermare lo scroll nel primo secondo con un numero sorprendente (1 acquisto → 1.000 aziende) e dare subito la definizione.',
    transition: 'Nessuna in entrata: il primo fotogramma è già in movimento (il quadrato verde sta crescendo). Uscita con zoom in avanti + sfocatura.',
    beats: [
      'Fondo blu notte con griglia di puntini che scorre. Al centro un quadrato verde luminoso cresce con un piccolo rimbalzo; due anelli verdi si espandono come un “tap”. Sotto: etichetta “1 ACQUISTO”.',
      'Su “investire” il quadrato si rimpicciolisce e diventa la tessera centrale di una griglia 32×32 (1.024 tessere) che si accende a onda dal centro e si inclina in prospettiva 3D. In basso il contatore sale da 1 a “1.000+ AZIENDE”. Su “mille aziende” un’onda verde colora tutte le tessere.',
      'Su “ETF” la griglia torna piatta: le tessere che formano le lettere E-T-F diventano verde brillante con alone, tutte le altre cadono e si spengono. Il contatore sparisce.',
      'Sotto le lettere si scrive “EXCHANGE TRADED FUND” (iniziali in verde). Su “in borsa” appare con un rimbalzo la pillola “= fondo quotato in borsa”.',
      'Su “un’azione” sotto la pillola crescono, una dopo l’altra, 18 candele di un grafico di borsa (verdi e rosse).',
    ],
  },
  basket: {
    title: 'Dentro l’ETF: il paniere',
    goal: 'Far capire con un’immagine fisica che l’ETF è un contenitore di tante azioni scelte da un indice.',
    transition: 'Entrata: la scena arriva da leggermente più piccola e sfocata. Uscita: zoom in avanti + sfocatura.',
    beats: [
      'Dal basso sale un contenitore trasparente con la targa “ETF · 1 SOLO ACQUISTO”. Su “Dentro” 24 aziende astratte (quadrati colorati con simboli geometrici, nessun logo reale) cadono dall’alto ruotando e rimbalzano, impilandosi su 4 file.',
      'Su “un indice” un cartellino bianco “INDICE” si aggancia al bordo destro del contenitore e oscilla come un pendolo fino a fermarsi.',
      'Su “grandi” sopra il contenitore emerge un globo fatto di puntini che ruota; su “di tutto il mondo” circa il 20% dei puntini si accende di verde (le aziende nel mondo).',
    ],
  },
  divers: {
    title: 'Vantaggio 1: diversificazione',
    goal: 'Mostrare il rischio di una singola azione contro l’effetto diluito dentro un ETF, con un confronto onesto e un esempio dichiarato come semplificato.',
    transition: 'Entrata e uscita zoom + sfocatura.',
    beats: [
      'Cartello di sezione: grande “01” a contorno verde che sale dal basso e la scritta “DIVERSIFICAZIONE” lettera per lettera.',
      'Il cartello si dissolve e resta in alto la pillola “01 DIVERSIFICAZIONE”. Entrano due schede: sopra “UNA SOLA AZIONE” (quadrato blu + grafico a linea), sotto “ETF · 1.000 AZIENDE” (griglia di 1.000 micro-tessere + grafico), la seconda ancora attenuata. Le linee iniziano a disegnarsi.',
      'Su “crolla” la linea della scheda sopra precipita in rosso, l’area sotto si colora di rosso, il quadrato diventa rosso, trema e si crepa. In alto a destra il valore scende fino a “−60%”.',
      'La scheda resta su “−60%”: il calo è tutto sul tuo investimento.',
      'Su “Nell’ETF” la scheda sotto si accende con bordo verde. Su “una su mille” una sola micro-tessera tra le 1.000 diventa rossa, evidenziata da un anello rosso che si allarga.',
      'La linea verde della scheda sotto prosegue quasi piatta: lo stesso crollo vale “−0,06%” (valore in ambra). In basso la nota: “Esempio semplificato: 1.000 aziende con lo stesso peso.”',
    ],
  },
  costs: {
    title: 'Vantaggio 2: costi',
    goal: 'Rendere tangibile il costo di comprare tante azioni una per una e tradurre lo 0,2% in euro.',
    transition: 'Entrata e uscita zoom + sfocatura. Fondo con alone ambra.',
    beats: [
      'Cartello di sezione “02 · COSTI” in ambra, stessa animazione del capitolo 01.',
      'Resta la pillola “02 COSTI”. Al centro il contatore “× 1” che inizia a salire con sotto “COMMISSIONI, AZIONE PER AZIONE”. Ricevute gialle “€ COMMISSIONE” volano da destra e si impilano in una torre che cresce, sempre più veloce.',
      'Su “mille commissioni” il contatore arriva a “× 1.000” e la torre è al massimo.',
      'Su “un solo acquisto” la torre si comprime in un’unica ricevuta che diventa verde con scritto “1 ORDINE”; il contatore scatta a “× 1” verde, “ORDINE CON L’ETF”.',
      'Su “costo annuo” tutto sale e svanisce; appare una barra a capsula che si riempie di verde: “1.000 € INVESTITI”. Su “dello 0,2%” una sottile fetta ambra si accende all’estremità della barra, una linea tratteggiata porta a una lente che la ingrandisce: “2 €”. A sinistra grande “0,2%” e “COSTO ALL’ANNO”.',
      'Su “circa” sotto lo 0,2% compare “≈ 2 € ogni 1.000 €”. In basso le note: “Costo annuo (TER) indicativo: varia da ETF a ETF. Le commissioni di acquisto dipendono dal broker.”',
    ],
  },
  simple: {
    title: 'Vantaggio 3: semplicità',
    goal: 'Contrapporre lo stock picking (indovinare il vincitore) al comprare l’intero indice.',
    transition: 'Entrata e uscita zoom + sfocatura. Fondo con alone blu.',
    beats: [
      'Cartello di sezione “03 · SEMPLICITÀ” in blu.',
      'Resta la pillola “03 SEMPLICITÀ”. Compare una griglia 8×6 di aziende spente, ognuna con un “?”. Su “indovinare” una lente blu salta da un’azienda all’altra: quella sotto la lente si ingrandisce e il suo “?” diventa blu.',
      'Su “segui l’intero mercato” la lente si allarga fino a diventare una cornice verde attorno a tutta la griglia; le aziende si accendono a onda in diagonale, ognuna col suo colore e simbolo. Sotto: “INDICE = L’INTERO MERCATO”.',
    ],
  },
  risk: {
    title: 'Avvertenza: il rischio resta',
    goal: 'Correttezza e credibilità: l’ETF diversifica il rischio della singola azienda, non quello del mercato.',
    transition: 'Entrata e uscita zoom + sfocatura. Fondo con alone ambra.',
    beats: [
      'Su “Attenzione” un triangolo di pericolo ambra compare con un rimbalzo e oscilla. Sotto, il grafico “MERCATO” inizia a disegnarsi in verde, con l’etichetta “ETF” che segue la punta della linea.',
      'La linea continua a salire mentre il sottotitolo in rosso dice “non elimina il rischio”.',
      'Su “scende” la linea gira verso il basso e diventa rossa, con l’area sotto rossa; l’etichetta “ETF” diventa rossa e scende con la linea.',
      'Vicino al punto più basso appare in rosso “il valore può scendere”. Nessun recupero promesso.',
    ],
  },
  cta: {
    title: 'Chiusura: salva e condividi (loop)',
    goal: 'Chiedere i due segnali che Instagram premia di più (salvataggi e invii in DM) e chiudere in loop.',
    transition: 'Entrata zoom + sfocatura. Nessuna uscita: l’ultimo fotogramma coincide con il primo, così il reel riparte senza stacco.',
    beats: [
      'Due icone in riquadri di vetro: segnalibro “SALVA” e aeroplanino “CONDIVIDI”. Su “Salvalo” il segnalibro si riempie di verde dal basso con un rimbalzo e il riquadro si illumina. In basso: “Contenuto informativo, non è consulenza finanziaria. Investire comporta rischi, anche di perdita del capitale.”',
      'Su “mandalo” l’aeroplanino vola via in alto a destra e torna con un rimbalzo; il riquadro si illumina di blu. Nell’ultimo secondo tutto si stringe verso il centro e svanisce, e nasce il quadrato verde del primo fotogramma: il video ricomincia in loop.',
    ],
  },
};

const ts = (s: number) => {
  const m = Math.floor(s / 60);
  const sec = s - m * 60;
  return `${String(m).padStart(2, '0')}:${sec.toFixed(2).padStart(5, '0')}`;
};
const fr = (s: number) => Math.round(s * FPS);

const lines: string[] = [];
const total = DURATION_FRAMES / FPS;

lines.push('# Guion — “Cos’è un ETF” (reel Instagram)');
lines.push('');
lines.push(
  `Formato: verticale 1080×1920, ${FPS} fps, durata ${total.toFixed(1)} s (${DURATION_FRAMES} fotogrammi). ` +
    (VOICE
      ? 'Voce narrante generata con Gemini (`npm run voice`): sottotitoli e animazioni seguono i tempi reali della voce, riportati qui sotto. '
      : 'Video senza voce: i sottotitoli sono già nel video, sincronizzati sui tempi qui sotto. ') +
    'Questo file è generato da `src/script.ts` con `npm run guion`: se cambi un testo lì, video e copione restano allineati.',
);
lines.push('');
lines.push('## Perché è costruito così (ottimizzazione per Instagram)');
lines.push('');
lines.push('Nessuno può garantire che un reel diventi virale: dipende anche dall’account, dall’orario e da fattori che non controlliamo. Il video però è costruito sui segnali che contano di più:');
lines.push('');
lines.push('- **Gancio nel primo secondo.** Il primo fotogramma è già in movimento e la prima frase promette un numero sorprendente (“un solo acquisto → oltre mille aziende”). Niente intro né logo.');
lines.push('- **Un cambio visivo ogni 1-3 secondi.** Ogni frase fa succedere qualcosa sullo schermo, così l’occhio non ha tempo di annoiarsi e la percentuale di visione resta alta.');
lines.push('- **Sottotitoli parola per parola, con la parola chiave evidenziata.** Il video si capisce anche senza audio, come lo guarda gran parte del pubblico.');
lines.push('- **Struttura a capitoli (01, 02, 03).** Chi guarda sa quanto manca e resta fino al terzo vantaggio.');
lines.push('- **Numeri concreti e verificabili:** −60% contro −0,06%, × 1.000 commissioni contro × 1, 0,2% = 2 € ogni 1.000 €.');
lines.push('- **Avvertenza sul rischio.** Aumenta la credibilità e protegge da segnalazioni per contenuti finanziari fuorvianti.');
lines.push('- **Invito finale a salvare e inviare.** Salvataggi e condivisioni in DM sono tra i segnali più forti per la distribuzione.');
lines.push('- **Loop perfetto.** L’ultimo fotogramma coincide con il primo: chi non scorre subito lo rivede, e il tempo di visione sale.');
lines.push('');
lines.push('## Stile visivo');
lines.push('');
lines.push('- Fondo quasi nero (#05070C) con griglia di puntini in lento movimento e un alone del colore del capitolo.');
lines.push('- Colori con significato fisso: **verde** #34D399 = ETF/positivo, **rosso** #F87171 = perdita/rischio, **ambra** #FBBF24 = costi/attenzione, **blu** #60A5FA = singola azione/scelta.');
lines.push('- Font Inter (ExtraBold per i sottotitoli, Black per i numeri). Sottotitoli in alto (da y≈250), fuori dalle zone coperte dall’interfaccia di Instagram.');
lines.push('- Animazioni: 60 fotogrammi distinti al secondo, curve di accelerazione morbide, rimbalzi fisici. Tra una scena e l’altra c’è una transizione di 16 fotogrammi con zoom e sfocatura.');
lines.push('');
lines.push('## Copione fotogramma per fotogramma');
lines.push('');
lines.push('Tempi in minuti:secondi; tra parentesi i fotogrammi a 60 fps. Ogni riga è una frase dei sottotitoli: chi registra la voce deve far partire la frase al tempo indicato. Le parole in **grassetto** sono quelle evidenziate.');

TIMELINE.forEach((s, si) => {
  const n = NOTES[s.id];
  if (!n || n.beats.length !== s.phrases.length) throw new Error(`note mancanti o disallineate per la scena ${s.id}`);
  lines.push('');
  lines.push(`### Scena ${si + 1} — ${n.title} · ${ts(s.start)} → ${ts(s.end)} (fotogrammi ${fr(s.start)}–${fr(s.end) - 1})`);
  lines.push('');
  lines.push(`**Obiettivo:** ${n.goal}`);
  lines.push('');
  lines.push(`**Transizione:** ${n.transition}`);
  lines.push('');
  lines.push('| Tempo (fotogrammi) | Sottotitolo / voce | Cosa appare sullo schermo |');
  lines.push('|---|---|---|');
  s.phrases.forEach((p, pi) => {
    const text = p.words.map((w) => (w.hl ? `**${w.text}**` : w.text)).join(' ');
    lines.push(`| ${ts(p.start)} → ${ts(p.end)} (${fr(p.start)}–${fr(p.end) - 1}) | ${text} | ${n.beats[pi]} |`);
  });
});

lines.push('');
lines.push('## Testo completo per la voce');
lines.push('');
lines.push('Da leggere con tono sicuro e amichevole, ritmo sostenuto (circa 3 parole al secondo) e una breve pausa a ogni virgola e a ogni punto. Si legge così come è scritto, tranne: “0,2%” = “zero virgola due per cento”, “2 € ogni 1.000 €” = “due euro ogni mille euro”.');
lines.push('');
for (const s of TIMELINE) lines.push(`> ${s.phrases.map((p) => p.text).join(' ')}`, '>');
lines.pop();
lines.push('');
lines.push('**Voce inclusa:** `out/etf-voce.mp4` ha già la voce generata (voce Gemini “Charon”, accelerata del 10%); `out/etf-sottotitoli.mp4` è la stessa versione muta. Per cambiare voce: `VOICE_NAME=Kore npm run voice`, poi `npm run render`.');
lines.push('');
lines.push('**Per usare una voce tua:** registra o genera la voce seguendo i tempi della tabella. Se il ritmo della tua voce è diverso, posso ritagliare i sottotitoli sui tempi reali: mi basta il file audio. In alternativa, nell’editor di Instagram o in CapCut appoggia la traccia voce sopra il video e regola il volume della musica intorno al 15-20%.');
lines.push('');
lines.push('## Pubblicazione');
lines.push('');
lines.push('- **Copertina:** `out/cover.png` (“Cos’è un ETF? 3 vantaggi rispetto alle azioni”).');
lines.push('- **Musica:** una base strumentale di tendenza dalla libreria di Instagram, a volume basso sotto la voce. La musica aggiunta da Instagram è già concessa in licenza per i reel.');
lines.push('- **Didascalia proposta:**');
lines.push('');
lines.push('> Con un solo acquisto puoi investire in oltre 1.000 aziende 🌍');
lines.push('> ETF vs singola azione, in 3 punti:');
lines.push('> 1️⃣ Diversificazione: se un’azienda crolla, nell’ETF pesa poco');
lines.push('> 2️⃣ Costi: un solo ordine e un costo annuo spesso intorno allo 0,2% o meno');
lines.push('> 3️⃣ Semplicità: non devi indovinare le aziende vincenti');
lines.push('> ⚠️ L’ETF non elimina il rischio di mercato.');
lines.push('> 📌 Salvalo per quando inizierai a investire.');
lines.push('>');
lines.push('> Contenuto informativo, non è consulenza finanziaria.');
lines.push('>');
lines.push('> #etf #investire #educazionefinanziaria #finanzapersonale #borsa #risparmio #investimenti #soldi');
lines.push('');
lines.push('- **Primo commento (da fissare in alto):** una domanda che invita a rispondere, per esempio “Tu hai già un ETF o compri azioni singole?”.');
lines.push('- **Controlli prima di pubblicare:** il TER dello 0,2% è un valore indicativo per gli ETF azionari più diffusi; se nel video citi un prodotto specifico, verifica i suoi dati sul documento ufficiale (KID).');
lines.push('');

writeFileSync(new URL('../GUION.md', import.meta.url), lines.join('\n'));
console.log(`GUION.md scritto: ${TIMELINE.length} scene, ${total.toFixed(1)} s`);
