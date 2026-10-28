import {Easing, interpolate} from 'remotion';
import type {Accent} from './script';

export const W = 1080;
export const H = 1920;

export const C = {
  bg: '#05070C',
  text: '#F4F6FA',
  dim: '#8B95A7',
  faint: 'rgba(255,255,255,0.08)',
  card: 'rgba(255,255,255,0.035)',
  green: '#34D399',
  red: '#F87171',
  amber: '#FBBF24',
  blue: '#60A5FA',
  ink: '#04110B',
} as const;

export const accent = (a: Accent): string => C[a];

export const FONT = 'Inter, "Inter Display", system-ui, sans-serif';

export const easeOut = Easing.bezier(0.16, 1, 0.3, 1);
export const easeInOut = Easing.bezier(0.65, 0, 0.35, 1);
export const easeIn = Easing.bezier(0.5, 0, 0.75, 0);

const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;

/** 0→1 tra i frame a e b, con easing. */
export const ramp = (f: number, a: number, b: number, e: (t: number) => number = easeOut) =>
  interpolate(f, [a, b], [0, 1], {...clamp, easing: e});

export const lerp = (a: number, b: number, t: number) => a + (b - a) * t;

/** Pseudo-casuale deterministico in [0,1): ogni render dà lo stesso risultato. */
export const hash = (n: number) => {
  const x = Math.sin(n * 127.1 + 311.7) * 43758.5453;
  return x - Math.floor(x);
};

export const mix = (a: string, b: string, t: number) => {
  const k = Math.min(1, Math.max(0, t));
  const pa = parseInt(a.slice(1), 16);
  const pb = parseInt(b.slice(1), 16);
  const ch = (s: number) =>
    Math.round(lerp((pa >> s) & 255, (pb >> s) & 255, k))
      .toString(16)
      .padStart(2, '0');
  // Esadecimale, così si può aggiungere l'alpha in coda (es. `${mix(...)}CC`).
  return `#${ch(16)}${ch(8)}${ch(0)}`;
};

/** 1000 -> "1.000" (separatore italiano, senza dipendere da Intl). */
export const fmtInt = (n: number) => String(Math.round(n)).replace(/\B(?=(\d{3})+(?!\d))/g, '.');

export const fmtPct = (v: number, dec: number) => {
  const sign = v < -1e-9 ? '−' : v > 1e-9 ? '+' : '';
  return `${sign}${Math.abs(v).toFixed(dec).replace('.', ',')}%`;
};
