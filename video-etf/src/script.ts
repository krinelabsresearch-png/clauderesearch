// Testo del video e tempi. È l'unica fonte di verità: da qui escono
// sottotitoli, momenti delle animazioni (cue) e il copione in GUION.md.
//
// Sintassi delle frasi:
//   [parole]   evidenziate nel sottotitolo
//   parola@x   "cue" x: istante in cui la parola inizia, usato dalle animazioni
//   parola~N   peso di pronuncia (lettere parlate) quando il testo scritto
//              è più corto di quello detto, es. "0,2%~20" = "zero virgola due per cento"

export const FPS = 60;

export type Accent = 'green' | 'red' | 'amber' | 'blue';

type PhraseSpec = {t: string; c?: Accent};
type SceneSpec = {id: string; accent: Accent; tail?: number; phrases: PhraseSpec[]};

export const SCENES: SceneSpec[] = [
  {
    id: 'hook',
    accent: 'green',
    phrases: [
      {t: 'Con [un solo acquisto]'},
      {t: 'puoi investire@grid in oltre [mille aziende]@mille.'},
      {t: 'Si chiama [ETF]@etf:'},
      {t: 'un fondo che si compra e si vende [in borsa]@borsa,'},
      {t: 'come [un’azione]@azione.'},
    ],
  },
  {
    id: 'basket',
    accent: 'green',
    phrases: [
      {t: 'Dentro@drop ci sono [tante azioni] insieme,'},
      {t: 'scelte seguendo [un indice]@indice:'},
      {t: 'per esempio le grandi@globe aziende [di tutto il mondo].'},
    ],
  },
  {
    id: 'divers',
    accent: 'green',
    phrases: [
      {t: 'Primo vantaggio: la [diversificazione].'},
      {t: 'Se compri@panels [una sola azione]'},
      {t: 'e quell’azienda [crolla]@crash,', c: 'red'},
      {t: 'crolla anche il tuo investimento.', c: 'red'},
      {t: 'Nell’ETF@etfpanel è solo [una su mille]@onered:'},
      {t: 'il colpo [si sente molto meno]@dip.'},
    ],
  },
  {
    id: 'costs',
    accent: 'amber',
    phrases: [
      {t: 'Secondo: i [costi].'},
      {t: 'Comprare@stream mille azioni una per una'},
      {t: 'vuol dire [mille commissioni]@thousand.'},
      {t: 'Con l’ETF è [un solo acquisto]@collapse,', c: 'green'},
      {t: 'con un costo annuo@bar spesso [dello 0,2%~20]@ter o meno:'},
      {t: 'circa@twoeur [2~3 €~4 ogni 1.000~5 €~4].'},
    ],
  },
  {
    id: 'simple',
    accent: 'blue',
    phrases: [
      {t: 'Terzo: la [semplicità].'},
      {t: 'Non devi indovinare@scan tu le aziende vincenti:'},
      {t: '[segui l’intero mercato]@market.', c: 'green'},
    ],
  },
  {
    id: 'risk',
    accent: 'amber',
    phrases: [
      {t: 'Attenzione@warn però:'},
      {t: 'l’ETF [non elimina il rischio].', c: 'red'},
      {t: 'Se scende@fall il mercato,', c: 'red'},
      {t: '[scende anche lui].', c: 'red'},
    ],
  },
  {
    id: 'cta',
    accent: 'green',
    tail: 1.3,
    phrases: [
      {t: '[Salvalo]@save per quando inizierai a investire,'},
      {t: 'e [mandalo]@send a chi vuole iniziare.'},
    ],
  },
];

// Ritmo della voce: ~3 parole al secondo, adatto a un reel informativo.
const WORD_BASE = 0.08;
const PER_CHAR = 0.046;
const PAUSE_COMMA = 0.16;
const PAUSE_COLON = 0.22;
const PAUSE_STOP = 0.34;
const SCENE_GAP = 0.22;
const SCENE_LEAD = 0.1;

export type Word = {text: string; hl: boolean; start: number; end: number};
export type Phrase = {words: Word[]; start: number; end: number; color: Accent; text: string};
export type Scene = {id: string; accent: Accent; start: number; end: number; phrases: Phrase[]};

const spokenWeight = (w: string) => {
  const m = w.match(/~(\d+)/);
  if (m) return Number(m[1]);
  return (w.match(/[\p{L}\p{N}]/gu) ?? []).length;
};

const cues: Record<string, number> = {};

const build = (): Scene[] => {
  let t = 0.12;
  return SCENES.map((sc, si) => {
    const start = si === 0 ? 0 : t;
    if (si > 0) t += SCENE_LEAD;
    const phrases = sc.phrases.map((p) => {
      const tokens = p.t.match(/\[[^\]]*\]\S*|\S+/g) ?? [];
      const pStart = t;
      const words = tokens.map((raw) => {
        let tok = raw;
        const cm = tok.match(/@(\w+)/);
        if (cm) tok = tok.replace(/@\w+/, '');
        const hl = tok.includes('[');
        const plain = tok.replace(/[[\]]/g, '');
        const dur = plain.split(' ').reduce((a, w) => a + WORD_BASE + PER_CHAR * spokenWeight(w), 0);
        const text = plain.replace(/~\d+/g, '');
        if (cm) cues[`${sc.id}.${cm[1]}`] = t;
        const word: Word = {text, hl, start: t, end: t + dur};
        t += dur;
        const last = text.slice(-1);
        if (last === ',' || last === ';') t += PAUSE_COMMA;
        else if (last === ':') t += PAUSE_COLON;
        else if ('.!?'.includes(last)) t += PAUSE_STOP;
        return word;
      });
      return {
        words,
        start: pStart,
        end: t,
        color: p.c ?? sc.accent,
        text: words.map((w) => w.text).join(' '),
      };
    });
    t += sc.tail ?? SCENE_GAP;
    return {id: sc.id, accent: sc.accent, start, end: t, phrases};
  });
};

export const TIMELINE: Scene[] = build();
export const DURATION_FRAMES = Math.ceil(TIMELINE[TIMELINE.length - 1].end * FPS);

export const cueSeconds = (sceneId: string, name: string): number => {
  const v = cues[`${sceneId}.${name}`];
  if (v === undefined) throw new Error(`cue mancante: ${sceneId}.${name}`);
  return v;
};
