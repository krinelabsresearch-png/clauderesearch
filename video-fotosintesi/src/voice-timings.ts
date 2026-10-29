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
    "dur": 2.5,
    "phrases": [
      {
        "start": 0.0,
        "end": 2.5
      }
    ]
  },
  {
    "file": "g01.wav",
    "dur": 3.89,
    "phrases": [
      {
        "start": 0.0,
        "end": 3.89
      }
    ]
  },
  {
    "file": "g02.wav",
    "dur": 4.149,
    "phrases": [
      {
        "start": 0.0,
        "end": 4.149
      }
    ]
  },
  {
    "file": "g03.wav",
    "dur": 6.213,
    "phrases": [
      {
        "start": 0.0,
        "end": 1.46
      },
      {
        "start": 1.65,
        "end": 6.213
      }
    ]
  },
  {
    "file": "g04.wav",
    "dur": 3.53,
    "phrases": [
      {
        "start": 0.0,
        "end": 3.53
      }
    ]
  },
  {
    "file": "g05.wav",
    "dur": 4.31,
    "phrases": [
      {
        "start": 0.0,
        "end": 4.31
      }
    ]
  },
  {
    "file": "g06.wav",
    "dur": 1.704,
    "phrases": [
      {
        "start": 0.0,
        "end": 1.704
      }
    ]
  },
  {
    "file": "g07.wav",
    "dur": 4.079,
    "phrases": [
      {
        "start": 0.0,
        "end": 4.079
      }
    ]
  },
  {
    "file": "g08.wav",
    "dur": 4.431,
    "phrases": [
      {
        "start": 0.0,
        "end": 4.431
      }
    ]
  },
  {
    "file": "g09.wav",
    "dur": 6.087,
    "phrases": [
      {
        "start": 0.0,
        "end": 3.37
      },
      {
        "start": 3.69,
        "end": 6.087
      }
    ]
  },
  {
    "file": "g10.wav",
    "dur": 5.429,
    "phrases": [
      {
        "start": 0.0,
        "end": 1.27
      },
      {
        "start": 1.65,
        "end": 5.429
      }
    ]
  },
  {
    "file": "g11.wav",
    "dur": 4.393,
    "phrases": [
      {
        "start": 0.0,
        "end": 1.62
      },
      {
        "start": 1.85,
        "end": 4.393
      }
    ]
  }
];
