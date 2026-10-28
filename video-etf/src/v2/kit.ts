// Strumenti comuni alle scene liquid glass.
import {spring} from 'remotion';
import {FPS, cueSeconds, type Scene} from '../script';
import type {Shape} from './glass/renderer';

export type RGB = [number, number, number];
export const G: RGB = [0.2, 0.83, 0.6];
export const RED: RGB = [0.97, 0.36, 0.36];
export const AMB: RGB = [0.98, 0.74, 0.14];
export const BLU: RGB = [0.38, 0.62, 0.98];
export const WHITE: RGB = [1, 1, 1];
export const SECTOR: RGB[] = [
  [0.23, 0.51, 0.96], [0.55, 0.36, 0.96], [0.06, 0.73, 0.51], [0.96, 0.62, 0.04],
  [0.08, 0.72, 0.65], [0.93, 0.28, 0.6], [0.39, 0.4, 0.95], [0.13, 0.77, 0.37],
];

/** Frame di sovrapposizione prima (LEAD) e dopo (TAIL) ogni cambio scena. */
export const LEAD = 18;
export const TAIL = 18;

export type Ctx = {
  scene: Scene;
  /** frame locale della scena */
  f: number;
  /** durata locale totale (transizioni incluse) */
  total: number;
  /** frame locale in cui inizia la parola marcata @name */
  cue: (name: string) => number;
  /** frame locale di un istante assoluto (secondi) */
  at: (seconds: number) => number;
};

export const makeCtx = (scene: Scene, from: number, total: number, f: number): Ctx => {
  const at = (s: number) => s * FPS - from;
  return {scene, f, total, at, cue: (n) => at(cueSeconds(scene.id, n))};
};

export const clamp01 = (x: number) => Math.min(1, Math.max(0, x));
export const lerp = (a: number, b: number, t: number) => a + (b - a) * t;
export const easeOut = (t: number) => 1 - Math.pow(1 - clamp01(t), 3);
export const easeIn = (t: number) => Math.pow(clamp01(t), 3);
export const easeInOut = (t: number) => {
  const x = clamp01(t);
  return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
};
export const prog = (f: number, a: number, b: number) => clamp01((f - a) / (b - a));

/** Molla con rimbalzo (0→1, può superare 1): il movimento "elastico" del liquido. */
export const spr = (f: number, start: number, damping = 13, stiffness = 140, mass = 1) =>
  f < start ? 0 : spring({frame: f - start, fps: FPS, config: {damping, stiffness, mass}});

export const hash = (n: number) => {
  const x = Math.sin(n * 127.1 + 311.7) * 43758.5453;
  return x - Math.floor(x);
};

export const mixRGB = (a: RGB, b: RGB, t: number): RGB => [lerp(a[0], b[0], t), lerp(a[1], b[1], t), lerp(a[2], b[2], t)];

/**
 * Goccia che si allunga nella direzione del moto e si schiaccia di lato
 * (squash & stretch), calcolata dalla posizione al frame precedente.
 */
export const droplet = (
  pos: (f: number) => [number, number],
  f: number,
  r: number,
  extra: Partial<Shape> = {},
  stretch = 0.012,
): Shape => {
  const [x, y] = pos(f);
  const [px, py] = pos(f - 1);
  const v = Math.hypot(x - px, y - py);
  const s = Math.min(0.75, v * stretch);
  return {
    x,
    y,
    w: r * (1 + s),
    h: r / (1 + s * 0.6),
    r: r,
    rot: v > 0.01 ? Math.atan2(y - py, x - px) : 0,
    ...extra,
  };
};

/** Scala una forma (per comparire/sparire) mantenendo il centro. */
export const scaled = (s: Shape, k: number): Shape => ({
  ...s,
  w: s.w * k,
  h: (s.h ?? s.w) * k,
  r: s.r !== undefined ? s.r * k : undefined,
  thick: s.thick !== undefined ? s.thick * k : undefined,
});
