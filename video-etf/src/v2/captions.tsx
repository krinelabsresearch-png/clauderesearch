// Sottotitoli della versione liquid glass: parole posizionate con misure reali
// del font, e una capsula di vetro che ne segue la forma frase per frase.
import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {FPS, TIMELINE, type Phrase} from '../script';
import {C, FONT, accent} from '../theme';
import type {Shape} from './glass/renderer';
import {clamp01, lerp, spr} from './kit';

const PHRASES: Phrase[] = TIMELINE.flatMap((s) => s.phrases);
const SIZE = 66;
const GAP = 17;
const LINE = 80;
const MAXW = 880;
const PAD = 26;
export const CAP_TOP = 250;

type WordBox = {x: number; w: number; line: number};
type Layout = {words: WordBox[]; lineW: number[]; width: number; lines: number};

let ctx2d: CanvasRenderingContext2D | null = null;
const measure = (text: string) => {
  if (!ctx2d) {
    ctx2d = document.createElement('canvas').getContext('2d')!;
    ctx2d.font = `800 ${SIZE}px Inter`;
    (ctx2d as unknown as {letterSpacing: string}).letterSpacing = `${-0.015 * SIZE}px`;
  }
  return ctx2d.measureText(text).width;
};

const cache = new Map<number, Layout>();
const layoutOf = (i: number): Layout => {
  const hit = cache.get(i);
  if (hit) return hit;
  const words: WordBox[] = [];
  const lineW: number[] = [0];
  for (const w of PHRASES[i].words) {
    const bw = measure(w.text) + (w.hl ? PAD : 0);
    let line = lineW.length - 1;
    const next = lineW[line] === 0 ? bw : lineW[line] + GAP + bw;
    if (next > MAXW && lineW[line] > 0) {
      lineW.push(0);
      line++;
    }
    const x = lineW[line] === 0 ? 0 : lineW[line] + GAP;
    words.push({x, w: bw, line});
    lineW[line] = x + bw;
  }
  const out = {words, lineW, width: Math.max(...lineW), lines: lineW.length};
  cache.set(i, out);
  return out;
};

/** Fine visibilità di una frase (in frame): poco prima della successiva o 0,45 s dopo la fine. */
const visEnd = (i: number) => {
  const next = PHRASES[i + 1];
  return Math.min(next ? next.start * FPS - 8 : Infinity, (PHRASES[i].end + 0.45) * FPS);
};

type Dims = {w: number; h: number; y: number};
const HIDDEN: Dims = {w: 0, h: 0, y: CAP_TOP + LINE / 2};
const dimsOf = (i: number): Dims => {
  const l = layoutOf(i);
  return {w: l.width / 2 + 40, h: (l.lines * LINE) / 2 + 16, y: CAP_TOP + (l.lines * LINE) / 2 + 4};
};

// Cambi di forma della capsula: si allarga a ogni frase, si ritira in goccia nelle pause lunghe.
type Ev = {f: number; d: Dims};
let EVENTS: Ev[] | null = null;
const events = (): Ev[] => {
  if (EVENTS) return EVENTS;
  const ev: Ev[] = [{f: -1, d: HIDDEN}];
  PHRASES.forEach((p, i) => {
    ev.push({f: p.start * FPS - 4, d: dimsOf(i)});
    const next = PHRASES[i + 1];
    const end = visEnd(i);
    if (!next || next.start * FPS - end > 18) ev.push({f: end, d: {w: 26, h: 26, y: dimsOf(i).y}});
  });
  const last = ev[ev.length - 1];
  ev.push({f: last.f + 20, d: HIDDEN});
  EVENTS = ev;
  return ev;
};

const dimsAt = (f: number): Dims => {
  const ev = events();
  let k = 0;
  while (k + 1 < ev.length && ev[k + 1].f <= f) k++;
  if (k === 0) return ev[0].d;
  // valore di partenza = dove si trovava la capsula al cambio precedente (catena di molle)
  const from = k >= 2 ? blend(ev[k - 2].d, ev[k - 1].d, spr(ev[k].f, ev[k - 1].f, 14, 170)) : ev[k - 1].d;
  return blend(from, ev[k].d, spr(f, ev[k].f, 11, 150), spr(f, ev[k].f + 3, 9, 170));
};

const blend = (a: Dims, b: Dims, t: number, th = t): Dims => ({w: lerp(a.w, b.w, t), h: lerp(a.h, b.h, th), y: lerp(a.y, b.y, t)});

/** La capsula di vetro dietro i sottotitoli, come forma dello shader. */
export const captionShape = (f: number): Shape => {
  const d = dimsAt(f);
  const r = Math.min(d.h, 44);
  return {x: 540, y: d.y, w: Math.max(0, d.w), h: Math.max(0, d.h), r, k: 0, tint: [0.75, 0.85, 1], tintAmt: 0.06, frost: 0.55, refr: 1.1};
};

const Word: React.FC<{p: Phrase; i: number; j: number; f: number}> = ({p, i, j, f}) => {
  const w = p.words[j];
  const box = layoutOf(i).words[j];
  const l = layoutOf(i);
  const s = w.start * FPS;
  const a = clamp01((f - s + 2) / 10);
  const e = 1 - Math.pow(1 - a, 3);
  const pill = w.hl ? clamp01((f - s) / 11) : 0;
  const pop = interpolate(f, [s, s + 5, s + 18], [0, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const col = accent(p.color);
  return (
    <div
      style={{
        position: 'absolute',
        left: 540 - l.lineW[box.line] / 2 + box.x,
        top: CAP_TOP + box.line * LINE,
        width: box.w,
        height: LINE,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontFamily: FONT,
        fontWeight: 800,
        fontSize: SIZE,
        letterSpacing: '-0.015em',
        color: w.hl && pill > 0.45 ? C.ink : C.text,
        opacity: e,
        transform: `translateY(${(1 - e) * 22}px) scale(${0.88 + 0.12 * e + 0.06 * pop})`,
        filter: e < 0.999 ? `blur(${(1 - e) * 9}px)` : undefined,
        textShadow: w.hl && pill > 0.45 ? 'none' : '0 3px 18px rgba(0,0,0,0.55)',
      }}
    >
      {w.hl && (
        <div
          style={{
            position: 'absolute',
            inset: '8px 0 6px 0',
            borderRadius: 18,
            background: `linear-gradient(180deg, ${col}, ${col}D0)`,
            transform: `scaleX(${pill}) rotate(-1.2deg)`,
            transformOrigin: 'left center',
            boxShadow: `0 8px 26px ${col}66, inset 0 2px 0 rgba(255,255,255,0.55), inset 0 -3px 6px rgba(0,0,0,0.18)`,
          }}
        />
      )}
      <span style={{position: 'relative', whiteSpace: 'nowrap'}}>{w.text}</span>
    </div>
  );
};

export const Captions2: React.FC = () => {
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{pointerEvents: 'none'}}>
      {PHRASES.map((p, i) => {
        const end = visEnd(i);
        if (f < p.start * FPS - 3 || f > end + 6) return null;
        const out = clamp01((f - end) / 6);
        return (
          <div
            key={i}
            style={{
              position: 'absolute',
              inset: 0,
              opacity: 1 - out,
              transform: `translateY(${-20 * out}px) scale(${1 - 0.04 * out})`,
              transformOrigin: `540px ${CAP_TOP + 40}px`,
              filter: out > 0 ? `blur(${out * 6}px)` : undefined,
            }}
          >
            {p.words.map((_, j) => (
              <Word key={j} p={p} i={i} j={j} f={f} />
            ))}
          </div>
        );
      })}
    </AbsoluteFill>
  );
};
