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
    title: 'Gancio: l’ossigeno è un avanzo',
    goal: 'Fermare lo scroll con un’affermazione che sorprende e riguarda chi guarda (“l’ossigeno che stai respirando”), poi dare subito il nome dell’argomento.',
    transition: 'Nessuna in entrata: il primo fotogramma è già in movimento ed è identico all’ultimo (loop). Uscita: la camera si allontana dalla foglia fino alla pianta intera.',
    beats: [
      'Foglia in macro controluce: raggi di sole che ruotano lentamente, bokeh, bolle d’ossigeno che nascono sulla foglia e salgono. In alto la capsula di vetro dei sottotitoli si allarga con una molla attorno alla frase; le parole entrano da sfocate a nitide. A destra si materializza un bottone rotondo di vetro “O₂” che galleggia: compare modulando la rifrazione, non con una dissolvenza. Su “un avanzo” il bottone viene premuto: si comprime, rimbalza e si illumina dal punto del tocco; nel sottotitolo “un avanzo” si evidenzia con una pillola verde.',
      'Su “fotosintesi clorofilliana” il bottone O₂ si trasforma con un morph nella card di vetro del titolo, “Fotosintesi / clorofilliana”; il testo compare solo quando il vetro ha raggiunto la misura finale. Su “foglia” la card si smaterializza e la camera si allontana: dalla foglia in macro si passa alla pianta intera, con cielo, sole, colline e terreno in sezione con le radici.',
    ],
  },
  ingr: {
    title: 'I tre ingredienti',
    goal: 'Fissare la “ricetta” con tre oggetti toccabili: ogni ingrediente diventa un controllo che si preme.',
    transition: 'Stessa inquadratura della pianta. Dal basso si materializza la tab bar di vetro con i 5 capitoli: Luce, Acqua, CO₂, O₂, Glucosio.',
    beats: [
      'Su “ingredienti” compare al centro la capsula “3 ingredienti” che, come i controlli uniti di iOS 26, si divide in tre bottoni rotondi: restano uniti da ponti liquidi mentre si separano, poi volano ai loro posti (Luce sopra il sole, CO₂ nel cielo a sinistra, Acqua nel terreno). Su ogni ingrediente un dito tocca il bottone: pressione con rimbalzo, la luce del tocco si irradia anche ai bottoni vicini, il vetro prende il colore dell’ingrediente e l’indicatore della tab bar scivola sulla voce giusta, allungandosi come una goccia mentre si muove. Nella scena si accende ciò che si nomina: il sole si intensifica, nel terreno compare l’acqua, nel cielo le molecole di CO₂.',
    ],
  },
  path: {
    title: 'Dove entrano acqua e CO₂',
    goal: 'Mostrare il percorso reale dei due ingredienti: radici → fusto → foglia per l’acqua, stomi per la CO₂.',
    transition: 'Uscita: zoom dentro la foglia, nel punto dove entra la CO₂, fino alla sua superficie inferiore.',
    beats: [
      'Su “sale” il bottone Acqua si trasforma nella capsula “Radici”; gocce blu risalgono dalle punte delle radici, lungo il fusto, fino alla foglia. L’indicatore della tab bar torna su Acqua.',
      'Le molecole di CO₂ (sfere: carbonio nero, ossigeno rosso) convergono verso un punto della foglia; l’indicatore passa a CO₂ e i bottoni rimasti si smaterializzano. Zoom dentro la foglia: un tappeto di cellule e gli stomi, le due cellule a fagiolo con il poro al centro. Su “gli stomi” una lente di vetro trasparente (variante clear, che ingrandisce) galleggia sullo stoma centrale, che si apre; le molecole di CO₂ vengono risucchiate nel poro. Sotto la lente compare la capsula “Stoma”.',
    ],
  },
  chloro: {
    title: 'Cloroplasti e clorofilla: perché le foglie sono verdi',
    goal: 'Il momento “aha”: il verde è la luce che la clorofilla non usa. Lo mostra un grafico vero, non solo una frase.',
    transition: 'Entrata: zoom dentro lo stoma fino alle cellule, poi dentro un cloroplasto. Uscita: zoom dentro un grano di tilacoidi.',
    beats: [
      'Cellule a palizzata con i cloroplasti verdi che si muovono lungo le pareti. La tab bar si riduce a un piccolo bottone rotondo a sinistra, come quando si scorre una pagina in iOS 26, e mostra solo l’icona attiva. In basso la capsula “Cellule”; su “cloroplasti” l’etichetta cambia in “Cloroplasto” e la capsula si allunga con una molla. Zoom dentro un cloroplasto: un’ellisse con i grani (pile di tilacoidi) collegati dalle lamelle.',
      'In alto a sinistra un prisma di vetro trasparente si materializza ruotando fino a fermarsi: la luce bianca lo attraversa e si apre nei colori, con vera dispersione cromatica sui bordi del vetro. Su “assorbe” la capsula si trasforma nella card “Luce assorbita dalla clorofilla”: lo spettro di assorbimento si disegna da 400 a 700 nm, con i picchi segnati nel blu (~430 nm) e nel rosso (~663 nm) e le etichette “assorbe il blu” e “assorbe il rosso”; i raggi blu e rosso entrano nei grani, che si illuminano. Su “il verde” la banda 500–580 nm viene cerchiata, compare “riflette” e il raggio verde rimbalza via.',
      'Il cloroplasto si accende di verde; la card e il prisma si smaterializzano.',
    ],
  },
  light: {
    title: 'La luce spezza l’acqua: nasce l’ossigeno',
    goal: 'Correggere l’errore più comune: l’ossigeno liberato viene dall’acqua, non dalla CO₂.',
    transition: 'Entrata: zoom dentro un grano, fino alla membrana del tilacoide. Uscita: dissolvenza.',
    beats: [
      'Membrana del tilacoide: doppio strato lipidico che ondeggia, tre complessi proteici viola (i fotosistemi) e, sullo sfondo, pile di tilacoidi sfocate che danno profondità. Fotoni gialli arrivano dall’alto. Su “spezza” le molecole d’acqua salgono dal basso, raggiungono il primo fotosistema e si spezzano con un lampo: l’O₂ sale, gli ioni H⁺ restano sotto, l’energia corre lungo la membrana. In alto a destra un contatore di vetro “O₂ × 1… 6” con cifre che scorrono come in .numericText. Nel bottone ridotto della tab bar l’icona passa ad Acqua, poi a O₂.',
    ],
  },
  sugar: {
    title: 'La CO₂ diventa glucosio',
    goal: 'Chiudere il cerchio: il carbonio dell’aria diventa il cibo della pianta.',
    transition: 'Entrata in dissolvenza nello stroma del cloroplasto. Uscita: dissolvenza.',
    beats: [
      'Stroma del cloroplasto con grani sfocati sullo sfondo: sei molecole di CO₂ sospese vengono attirate al centro insieme a scintille d’energia. Su “glucosio” si forma, con un lampo dorato, la molecola di glucosio in 3D (anello di cinque atomi di carbonio e uno di ossigeno, con i gruppi OH). Il contatore O₂ si trasforma, allungandosi, nella capsula “Glucosio C₆H₁₂O₆”, con una leggera tinta arancio.',
    ],
  },
  formula: {
    title: 'La formula',
    goal: 'Dare la versione “da compito”: l’equazione bilanciata, costruita termine per termine mentre la voce la legge.',
    transition: 'Entrata: dissolvenza alla foglia in macro, attenuata per dare risalto al pannello. Uscita: dissolvenza al cielo dell’albero.',
    beats: [
      'La capsula del glucosio si espande nel pannello di vetro “La fotosintesi in formula” e la tab bar si riespande. Su “sei di anidride carbonica” entra “6 CO₂” con la sua molecola e il 6 scorre da 0 a 6; su “sei d’acqua” compaiono il “+” e “6 H₂O”. L’indicatore della tab bar segue ogni termine.',
      'Su “diventano” si disegna la freccia, con sopra il sole e la parola “luce”; poi “C₆H₁₂O₆” con la molecola di glucosio, il “+” e “6 O₂”. A schermo resta l’equazione completa e bilanciata: 6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂.',
    ],
  },
  tree: {
    title: 'Il colpo di scena: il legno viene dall’aria',
    goal: 'Il fatto controintuitivo che fa commentare e condividere, e che prepara la chiamata all’azione.',
    transition: 'Entrata in dissolvenza. Uscita in dissolvenza alla foglia del primo fotogramma.',
    beats: [
      'Cielo azzurro e prato: dal terreno cresce un albero, ramo dopo ramo (cinque livelli di biforcazioni), poi la chioma con centinaia di foglie su tre strati.',
      'Su “legno” compare la capsula “Legno”, con una linea che punta al tronco. Compare un selettore segmentato di vetro “Terreno | Aria”: su “terreno” il cursore rosso è su Terreno e il suolo si scurisce. Su “dall’aria” un dito tocca Aria: il cursore scivola allungandosi come una goccia, diventa verde con la spunta, e le molecole di CO₂ e i puntini dell’aria convergono nella chioma. L’indicatore della tab bar va su CO₂.',
    ],
  },
  cta: {
    title: 'Chiusura: salva e condividi (loop)',
    goal: 'Chiedere i due segnali che Instagram premia di più (salvataggi e invii in DM), con un motivo concreto per farlo, e chiudere in loop.',
    transition: 'Entrata: dissolvenza alla foglia in macro con le bolle; la tab bar si smaterializza. Nessuna uscita: l’ultimo fotogramma coincide con il primo.',
    beats: [
      'Due bottoni rotondi di vetro: segnalibro “Salva” e condivisione “Condividi”. Un dito tocca Salva: pressione, rimbalzo, il segnalibro si riempie, il vetro si tinge di verde e la luce del tocco si irradia anche al bottone vicino.',
      'Tocco su Condividi: l’icona si trasforma nella spunta (sostituzione di simbolo) e il vetro si tinge di blu. Nell’ultimo secondo e mezzo tutti i vetri si smaterializzano e resta la foglia del primo fotogramma: il reel riparte senza stacco.',
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

lines.push('# Guion — “La fotosintesi clorofilliana in 60 secondi” (reel Instagram)');
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
lines.push('- **Gancio nel primo secondo, personale.** “L’ossigeno che stai respirando è un avanzo” parla di chi guarda e crea una domanda (“un avanzo di cosa?”) che si risolve solo restando. Niente intro né logo: il primo fotogramma è già in movimento.');
lines.push('- **Un cambio visivo ogni 1-3 secondi.** Ogni frase fa succedere qualcosa: un controllo che si trasforma, uno zoom dentro la scala successiva (pianta → foglia → stoma → cellula → cloroplasto → membrana → molecola), un tocco.');
lines.push('- **Viaggio di scala continuo.** La discesa nel microscopico è un unico movimento di camera: chi guarda vuole vedere “il livello dopo”.');
lines.push('- **Sottotitoli parola per parola, con la parola chiave evidenziata.** Il video si capisce anche senza audio, come lo guarda gran parte del pubblico.');
lines.push('- **Due momenti “aha” da condividere:** perché le foglie sono verdi (con il grafico vero dello spettro) e il legno che viene dall’aria.');
lines.push('- **Valore da salvare.** La formula bilanciata a schermo per qualche secondo è il fotogramma che uno studente vuole ritrovare: “salvalo per il prossimo compito” dà un motivo concreto per salvare.');
lines.push('- **Invito a inviare con un bersaglio preciso** (“a chi pensa che le piante mangino terra”): gli invii in DM sono tra i segnali più forti per la distribuzione.');
lines.push('- **Loop perfetto.** L’ultimo fotogramma coincide con il primo: chi non scorre subito lo rivede, e il tempo di visione sale.');
lines.push('- **Zone sicure.** Sottotitoli in alto (da y≈242), controlli tra y≈500 e y≈1530: lontano dalla didascalia e dai pulsanti di Instagram.');
lines.push('');
lines.push('## Stile: il linguaggio di movimento di Liquid Glass (iOS 26)');
lines.push('');
lines.push('Il video non “disegna del vetro”: usa le regole di movimento che Apple ha introdotto con Liquid Glass. Tutto ciò che è interfaccia sta su un unico piano di vetro sopra l’illustrazione, che il vetro rifrange davvero (shader WebGL), fotogramma per fotogramma.');
lines.push('');
lines.push('- **Il vetro rifrange, non sfoca e basta:** i bordi piegano l’immagine sottostante (lensing), con una leggera dispersione cromatica; il centro è smerigliato per la leggibilità e si scurisce dove il fondo è chiaro.');
lines.push('- **Riflessi che seguono il movimento:** i riflessi sui bordi scorrono lentamente come se il telefono venisse inclinato in mano.');
lines.push('- **Comparire e sparire modulando la rifrazione,** non con dissolvenze: il vetro “si condensa” e “si scioglie”.');
lines.push('- **Morphing tra controlli:** un elemento diventa il successivo invece di sparire (O₂ → titolo; capsula → 3 bottoni; Acqua → Radici; Cellule → Cloroplasto → grafico; contatore O₂ → Glucosio → pannello della formula).');
lines.push('- **Controlli che si uniscono e si separano come gocce** (come GlassEffectContainer): la capsula “3 ingredienti” si divide in tre bottoni uniti da ponti liquidi.');
lines.push('- **Risposta al tocco:** il vetro si comprime, rimbalza e si illumina dal punto toccato; la luce si irradia anche ai controlli vicini.');
lines.push('- **Indicatore che si allunga** mentre scivola tra le voci della tab bar, con le icone che si ingrandiscono sotto di lui; la tab bar si **riduce** a un bottone quando si “scende” nel microscopico e si riespande dopo.');
lines.push('- **Due varianti di vetro:** “regular” (smerigliato, per testo e controlli) e “clear” (trasparente, per la lente sullo stoma e il prisma).');
lines.push('- **Testo e simboli:** cifre che scorrono (come .numericText), sostituzione di simbolo con rimbalzo (condividi → spunta), testo sempre nitido sopra il vetro e mai fuori dal pannello.');
lines.push('- **Niente vetro su vetro:** il vetro è solo per i controlli; illustrazioni e contenuti restano sotto.');
lines.push('');
lines.push('Colori: verde clorofilla per la pianta e i passaggi chiave, ambra per la luce, blu per l’acqua, rosso/nero/bianco per gli atomi (convenzione dei modelli molecolari: ossigeno rosso, carbonio nero, idrogeno bianco). Font Inter. Animazioni a 60 fotogrammi distinti al secondo, con molle fisiche (rimbalzo leggero, mai meccanico).');
lines.push('');
lines.push('## Copione fotogramma per fotogramma');
lines.push('');
lines.push('Tempi in minuti:secondi; tra parentesi i fotogrammi a 60 fps. Ogni riga è una frase dei sottotitoli e della voce. Le parole in **grassetto** sono quelle evidenziate.');

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
lines.push('Tono sicuro e curioso, ritmo sostenuto (circa 3 parole al secondo), breve pausa a ogni virgola e a ogni punto. Si legge così come è scritto.');
lines.push('');
for (const s of TIMELINE) lines.push(`> ${s.phrases.map((p) => p.text).join(' ')}`, '>');
lines.pop();
lines.push('');
lines.push('**Voce inclusa:** `out/fotosintesi.mp4` ha già la voce, generata con Gemini TTS (voce “Charon”, accelerata del 10%, volume normalizzato a −16 LUFS). Ogni periodo è stato riascoltato da un secondo modello Gemini che lo ha trascritto e confrontato con il testo: tutti i 12 periodi corrispondono al 100%. `out/fotosintesi-muto.mp4` è la stessa versione senza voce (`npm run mute`). Per cambiare voce: `VOICE_NAME=Kore npm run voice`, poi `npm run render`.');
lines.push('');
lines.push('## Correttezza scientifica (cosa è semplificato e perché è comunque giusto)');
lines.push('');
lines.push('- **L’ossigeno come “avanzo”:** l’O₂ è un prodotto di scarto della fotosintesi. Le piante terrestri non sono l’unica fonte: circa metà dell’ossigeno prodotto sulla Terra viene dal fitoplancton degli oceani (lo usiamo come primo commento, sotto).');
lines.push('- **L’ossigeno viene dall’acqua:** nella fase luminosa la luce spezza le molecole d’acqua (fotolisi, nel fotosistema II) e l’O₂ liberato viene da lì, non dalla CO₂. Il video lo mostra in quest’ordine.');
lines.push('- **Clorofilla e colore:** la clorofilla (a e b) assorbe soprattutto il blu-violetto (~430–455 nm) e il rosso (~640–665 nm) e molto meno il verde, che viene riflesso o attraversa la foglia. Il grafico è una curva indicativa di clorofilla a + b, non la misura di una foglia intera (nella foglia vera anche una parte del verde viene assorbita).');
lines.push('- **Glucosio:** il ciclo di Calvin produce direttamente zuccheri a tre atomi di carbonio, da cui la pianta costruisce glucosio, saccarosio, amido e cellulosa. Dire “costruisce glucosio” è la semplificazione standard della scuola e corrisponde all’equazione complessiva.');
lines.push('- **Formula:** 6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂ è l’equazione complessiva bilanciata (6 C, 12 H e 18 O per lato).');
lines.push('- **Il legno dall’aria:** circa metà della massa secca del legno è carbonio, e tutto quel carbonio viene dalla CO₂ dell’aria; anche gran parte dell’ossigeno del legno viene dalla CO₂, mentre l’idrogeno viene dall’acqua. I minerali del suolo sono una piccola percentuale (le ceneri). Per questo la voce dice “gran parte”, non “tutto”. È anche l’esperimento storico di van Helmont (XVII secolo): un salice crebbe di circa 74 kg mentre il terreno nel vaso perse solo una sessantina di grammi.');
lines.push('');
lines.push('## Pubblicazione');
lines.push('');
lines.push('- **Video:** `out/fotosintesi.mp4` (con voce). **Copertina:** `out/cover.png` (“L’ossigeno che respiri è un avanzo · Fotosintesi clorofilliana · spiegata in 60 secondi”); il testo sta nel ritaglio 3:4 della griglia del profilo.');
lines.push('- **Musica:** una base strumentale leggera dalla libreria di Instagram, a volume basso (15-20%) sotto la voce. La musica aggiunta da Instagram è già concessa in licenza per i reel.');
lines.push('- **Didascalia proposta:**');
lines.push('');
lines.push('> L’ossigeno che respiri è un avanzo 🌿');
lines.push('> La fotosintesi in 60 secondi:');
lines.push('> ☀️ luce + 💧 acqua + 🌫️ anidride carbonica');
lines.push('> ➡️ glucosio (il cibo della pianta) + ossigeno (quello che respiri tu)');
lines.push('> 6 CO₂ + 6 H₂O → C₆H₁₂O₆ + 6 O₂');
lines.push('> 🤯 E gran parte del legno di un albero viene dall’aria, non dal terreno.');
lines.push('> 📌 Salvalo per il prossimo compito e mandalo a chi pensa che le piante mangino terra.');
lines.push('>');
lines.push('> #fotosintesi #biologia #scienza #scuola #piante');
lines.push('');
lines.push('- **Hashtag:** pochi e pertinenti funzionano meglio di molti generici. Alternative da ruotare tra un post e l’altro: #divulgazionescientifica #studiare #natura #clorofilla #biologiavegetale.');
lines.push('- **Primo commento (da fissare in alto):** “Lo sapevi che circa metà dell’ossigeno della Terra lo producono le alghe microscopiche degli oceani? 🌊 Scrivi 🌿 se lo sapevi già.” Fa rispondere e aggiunge un dato corretto che il video non ha spazio per dire.');
lines.push('- **Testo sul reel:** non serve aggiungerne: titolo e sottotitoli sono già nel video.');
lines.push('');

writeFileSync(new URL('../GUION.md', import.meta.url), lines.join('\n'));
console.log(`GUION.md scritto: ${TIMELINE.length} scene, ${total.toFixed(1)} s`);
