// Strumenti dello strato di controlli in stile Liquid Glass.
import React from 'react';
import {FPS, TIMELINE, cueSeconds} from '../script';
import type {Glass} from '../glass/renderer';
import {FONT, bouncy, clamp01, lerp, prog, smooth, smoothSpring} from '../theme';

export const cue = (s: string, n: string) => cueSeconds(s, n);
export const sceneStart = (id: string) => TIMELINE.find((x) => x.id === id)!.start;
export const sceneEnd = (id: string) => TIMELINE.find((x) => x.id === id)!.end;

/** Comparsa: la curvatura della luce cresce (non una dissolvenza). 0→1 in ~0,5 s. */
export const matIn = (t: number, t0: number) => clamp01(smoothSpring(t * FPS, t0 * FPS));
/** Scomparsa: la curvatura della luce torna a zero. */
export const matOut = (t: number, t1: number, dur = 0.3) => 1 - smooth(prog(t, t1, t1 + dur));
export const life = (t: number, t0: number, t1: number) => Math.min(matIn(t, t0), matOut(t, t1));
/** Scala "bouncy" di iOS alla comparsa (supera leggermente 1 e torna). */
export const popScale = (t: number, t0: number) => 0.9 + 0.1 * bouncy(t * FPS, t0 * FPS);
/** Molla 0→1 con rimbalzo, in secondi. */
export const bounce = (t: number, t0: number) => bouncy(t * FPS, t0 * FPS);
export const glide = (t: number, t0: number) => smoothSpring(t * FPS, t0 * FPS);

/** Materiale "regular": smerigliato, leggermente scurito per la leggibilità del testo. */
export const REGULAR: Partial<Glass> = {frost: 0.55, refr: 1.0, tint: [1, 1, 1], tintAmt: 0.05, dim: 0.14};
/** Materiale "clear": quasi trasparente, solo lente sui bordi. */
export const CLEAR: Partial<Glass> = {frost: 0.04, refr: 1.2, tintAmt: 0, dim: 0};

/** Reazione al tocco: schiacciamento, rimbalzo e luce che si accende nel punto toccato. */
export const press = (t: number, T: number) => {
  if (t < T - 0.05) return {scale: 1, glow: 0};
  const down = Math.exp(-Math.pow((t - T) / 0.07, 2));
  const after = t > T + 0.08 ? Math.sin((t - T - 0.08) * 22) * Math.exp(-(t - T - 0.08) * 7) : 0;
  return {scale: 1 - 0.085 * down + 0.06 * after, glow: t >= T ? Math.exp(-(t - T) / 0.42) : 0};
};

let ctx2d: CanvasRenderingContext2D | null = null;
/** Larghezza reale del testo con il font del video: i pannelli prendono la misura esatta. */
export const textWidth = (text: string, size: number, weight = 700, tracking = -0.01) => {
  if (!ctx2d) ctx2d = document.createElement('canvas').getContext('2d')!;
  ctx2d.font = `${weight} ${size}px Inter`;
  (ctx2d as unknown as {letterSpacing: string}).letterSpacing = `${tracking * size}px`;
  return ctx2d.measureText(text).width;
};

/** Testo sul vetro: bianco, con un'ombra leggera per staccarlo dal contenuto. */
export const onGlass: React.CSSProperties = {
  fontFamily: FONT,
  color: '#FFFFFF',
  textShadow: '0 1px 2px rgba(0,0,0,0.25), 0 2px 14px rgba(0,0,0,0.25)',
};

/** Dito simulato che tocca un controllo all'istante T. */
export const Touch: React.FC<{t: number; T: number; x: number; y: number}> = ({t, T, x, y}) => {
  if (t < T - 0.35 || t > T + 0.5) return null;
  const arrive = smooth(prog(t, T - 0.35, T - 0.05));
  const down = Math.exp(-Math.pow((t - T) / 0.08, 2));
  const a = arrive * (1 - smooth(prog(t, T + 0.18, T + 0.5)));
  const px = lerp(x + 70, x, arrive);
  const py = lerp(y + 110, y, arrive);
  const r = 40 * (1 - 0.18 * down);
  return (
    <div
      style={{
        position: 'absolute',
        left: px - r,
        top: py - r,
        width: r * 2,
        height: r * 2,
        borderRadius: '50%',
        background: 'radial-gradient(circle, rgba(255,255,255,0.55), rgba(255,255,255,0.22) 70%)',
        border: '2px solid rgba(255,255,255,0.65)',
        boxShadow: '0 8px 24px rgba(0,0,0,0.25)',
        opacity: a,
      }}
    />
  );
};

/** Capsula di vetro con un'etichetta, larga esattamente quanto il testo. */
export const pillGlass = (x: number, y: number, text: string, m: number, s = 1, size = 34): Glass => {
  const w = textWidth(text, size, 700) / 2 + 30;
  return {...REGULAR, x, y, w: w * s, h: 34 * s, r: 34 * s, k: 40, mat: m};
};

export const Pill: React.FC<{x: number; y: number; text: string; m: number; s?: number; size?: number; color?: string}> = ({
  x,
  y,
  text,
  m,
  s = 1,
  size = 34,
  color = '#FFFFFF',
}) =>
  m > 0.02 ? (
    <div
      style={{
        ...onGlass,
        position: 'absolute',
        left: x - 300,
        top: y - 30,
        width: 600,
        height: 60,
        lineHeight: '60px',
        textAlign: 'center',
        fontSize: size,
        fontWeight: 700,
        letterSpacing: '-0.01em',
        color,
        opacity: smooth((m - 0.35) / 0.5),
        transform: `scale(${s})`,
      }}
    >
      {text}
    </div>
  ) : null;
