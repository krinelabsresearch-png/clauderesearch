// File generato da scripts/make-voice.py (npm run voice): non modificarlo a mano.
// null = nessuna voce, i tempi del video sono stimati in script.ts.

export type VoiceTiming = {
  file: string;
  /** durata del file audio, in secondi */
  dur: number;
  /** inizio e fine di ogni frase del periodo, in secondi dall'inizio del file */
  phrases: {start: number; end: number}[];
};

export const VOICE: VoiceTiming[] | null = null;
