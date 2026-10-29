// File generato da scripts/make-voice.py (npm run voice): non modificarlo a mano.
// null = nessuna voce, i tempi del video sono stimati in script.ts.

export type VoiceTiming = {
  file: string;
  /** durata del file audio, in secondi */
  dur: number;
  /** inizio e fine di ogni frase del periodo, in secondi dall'inizio del file */
  phrases: {start: number; end: number}[];
};

export const VOICE: VoiceTiming[] | null = [
  {
    "file": "g00.wav",
    "dur": 3.282,
    "phrases": [
      {
        "start": 0.0,
        "end": 3.282
      }
    ]
  },
  {
    "file": "g01.wav",
    "dur": 3.602,
    "phrases": [
      {
        "start": 0.0,
        "end": 3.602
      }
    ]
  },
  {
    "file": "g02.wav",
    "dur": 1.759,
    "phrases": [
      {
        "start": 0.0,
        "end": 1.759
      }
    ]
  },
  {
    "file": "g03.wav",
    "dur": 3.389,
    "phrases": [
      {
        "start": 0.0,
        "end": 3.389
      }
    ]
  },
  {
    "file": "g04.wav",
    "dur": 5.115,
    "phrases": [
      {
        "start": 0.0,
        "end": 2.99
      },
      {
        "start": 3.09,
        "end": 5.115
      }
    ]
  },
  {
    "file": "g05.wav",
    "dur": 4.215,
    "phrases": [
      {
        "start": 0.0,
        "end": 4.215
      }
    ]
  },
  {
    "file": "g06.wav",
    "dur": 1.306,
    "phrases": [
      {
        "start": 0.0,
        "end": 1.306
      }
    ]
  }
];
