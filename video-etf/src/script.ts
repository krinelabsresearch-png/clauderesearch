// Testo del video e tempi. È l'unica fonte di verità: da qui escono
// sottotitoli, momenti delle animazioni (cue) e il copione in GUION.md.
//
// Sintassi delle frasi:
//   [parole]   evidenziate nel sottotitolo
//   parola@x   "cue" x: istante in cui la parola inizia, usato dalle animazioni
//   parola~N   peso di pronuncia (lettere parlate) quando il testo scritto
//              è più corto di quello detto, es. "0,2%~20" = "zero virgola due per cento"
//   say        testo letto dalla voce, se diverso da quello scritto
//
// Senza voce i tempi sono stimati dal ritmo qui sotto. Con la voce generata
// (npm run voice) i tempi reali di ogni frase arrivano da voice-timings.ts.

import {VOICE} from './voice-timings.ts';

export const FPS = 60;

export type Accent = 'green' | 'red' | 'amber' | 'blue';

type PhraseSpec = {t: string; c?: Accent; say?: string};
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
      {
        t: 'con un costo annuo@bar spesso [dello 0,2%~20]@ter o meno:',
        say: 'con un costo annuo spesso dello zero virgola due per cento o meno:',
      },
      {t: 'circa@twoeur [2~3 €~4 ogni 1.000~5 €~4].', say: 'circa due euro ogni mille euro.'},
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

type Token = {text: string; hl: boolean; cue?: string; dur: number};

const tokenize = (spec: string): Token[] =>
  (spec.match(/\[[^\]]*\]\S*|\S+/g) ?? []).map((raw) => {
    const cm = raw.match(/@(\w+)/);
    const tok = cm ? raw.replace(/@\w+/, '') : raw;
    const plain = tok.replace(/[[\]]/g, '');
    return {
      text: plain.replace(/~\d+/g, ''),
      hl: tok.includes('['),
      cue: cm?.[1],
      dur: plain.split(' ').reduce((a, w) => a + WORD_BASE + PER_CHAR * spokenWeight(w), 0),
    };
  });

const pauseAfter = (text: string) => {
  const last = text.slice(-1);
  if (last === ',' || last === ';') return PAUSE_COMMA;
  if (last === ':') return PAUSE_COLON;
  if ('.!?'.includes(last)) return PAUSE_STOP;
  return 0;
};

const plainText = (spec: string) => tokenize(spec).map((w) => w.text).join(' ');

/**
 * Periodi letti dalla voce tutti d'un fiato: frasi consecutive della stessa
 * scena fino a un punto o ai due punti. Ogni periodo è un file audio.
 */
export type VoiceGroup = {scene: string; phrases: number[]; says: string[]; say: string};
export const GROUPS: VoiceGroup[] = [];
{
  SCENES.forEach((sc) => {
    let cur: number[] = [];
    sc.phrases.forEach((p, pi) => {
      cur.push(pi);
      const last = plainText(p.t).slice(-1);
      if (last === '.' || last === ':' || pi === sc.phrases.length - 1) {
        const says = cur.map((i) => sc.phrases[i].say ?? plainText(sc.phrases[i].t));
        GROUPS.push({scene: sc.id, phrases: cur, says, say: says.join(' ')});
        cur = [];
      }
    });
  });
}

/** Per ogni periodo con voce: istante d'inizio nel video e file audio. */
export const VOICE_CLIPS: {file: string; start: number}[] = [];

const cues: Record<string, number> = {};

const build = (): Scene[] => {
  if (VOICE && VOICE.length !== GROUPS.length) {
    throw new Error(`voice-timings.ts ha ${VOICE.length} periodi, il copione ${GROUPS.length}: rigenera la voce`);
  }
  let t = 0.12;
  let g = 0;
  return SCENES.map((sc, si) => {
    const start = si === 0 ? 0 : t;
    if (si > 0) t += SCENE_LEAD;
    const phrases: Phrase[] = [];
    const layout = (spec: PhraseSpec, from: number, to: number | null) => {
      const tokens = tokenize(spec.t);
      // Con la voce le parole si distribuiscono nell'intervallo reale della frase,
      // in proporzione alla loro lunghezza parlata.
      const est = tokens.reduce((a, w, i) => a + w.dur + (i < tokens.length - 1 ? pauseAfter(w.text) : 0), 0);
      const k = to === null ? 1 : (to - from) / est;
      let x = from;
      const words = tokens.map((w, i) => {
        if (w.cue) cues[`${sc.id}.${w.cue}`] = x;
        const word: Word = {text: w.text, hl: w.hl, start: x, end: x + w.dur * k};
        x += w.dur * k + (i < tokens.length - 1 ? pauseAfter(w.text) * k : 0);
        return word;
      });
      phrases.push({words, start: from, end: x, color: spec.c ?? sc.accent, text: words.map((w) => w.text).join(' ')});
      return x;
    };
    while (g < GROUPS.length && GROUPS[g].scene === sc.id) {
      const grp = GROUPS[g];
      const v = VOICE?.[g];
      if (v) {
        VOICE_CLIPS.push({file: v.file, start: t});
        grp.phrases.forEach((pi, k) => layout(sc.phrases[pi], t + v.phrases[k].start, t + v.phrases[k].end));
        t += v.dur + pauseAfter(plainText(sc.phrases[grp.phrases[grp.phrases.length - 1]].t)) * 0.6;
      } else {
        grp.phrases.forEach((pi) => {
          const end = layout(sc.phrases[pi], t, null);
          t = end + pauseAfter(plainText(sc.phrases[pi].t));
        });
      }
      g++;
    }
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
