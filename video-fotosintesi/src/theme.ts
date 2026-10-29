import {spring} from 'remotion';
import {FPS} from './script';

export const FONT = 'Inter, "Inter Display", system-ui, sans-serif';
export const DISPLAY = '"Inter Display", Inter, system-ui, sans-serif';

export const COL = {
  text: '#FFFFFF',
  soft: 'rgba(255,255,255,0.72)',
  green: '#34C759',
  leaf: '#30D158',
  blue: '#0A84FF',
  water: '#64D2FF',
  amber: '#FFD60A',
  orange: '#FF9F0A',
  red: '#FF453A',
  carbon: '#3A3F47',
  oxygen: '#E8433F',
  hydrogen: '#F2F4F7',
};

export type RGB = [number, number, number];
export const rgb = (hex: string): RGB => {
  const n = parseInt(hex.slice(1), 16);
  return [((n >> 16) & 255) / 255, ((n >> 8) & 255) / 255, (n & 255) / 255];
};

export const clamp01 = (x: number) => Math.min(1, Math.max(0, x));
export const lerp = (a: number, b: number, t: number) => a + (b - a) * t;
export const prog = (f: number, a: number, b: number) => clamp01((f - a) / (b - a));
export const easeOut = (t: number) => 1 - Math.pow(1 - clamp01(t), 3);
export const easeIn = (t: number) => Math.pow(clamp01(t), 3);
export const easeInOut = (t: number) => {
  const x = clamp01(t);
  return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
};
export const smooth = (t: number) => {
  const x = clamp01(t);
  return x * x * (3 - 2 * x);
};
export const hash = (n: number) => {
  const x = Math.sin(n * 127.1 + 311.7) * 43758.5453;
  return x - Math.floor(x);
};

/** Molle in stile iOS: "bouncy" per i controlli, "smooth" per gli spostamenti ampi. */
export const bouncy = (f: number, start: number) =>
  f < start ? 0 : spring({frame: f - start, fps: FPS, config: {damping: 12, stiffness: 170, mass: 1}});
export const smoothSpring = (f: number, start: number) =>
  f < start ? 0 : spring({frame: f - start, fps: FPS, config: {damping: 20, stiffness: 120, mass: 1}});
