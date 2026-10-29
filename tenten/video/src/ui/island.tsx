// Sottotitoli in una capsula di vetro che si adatta a ogni frase con una molla,
// come una Live Activity: si allarga, si restringe e nelle pause si ritira.
import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {FPS, TIMELINE, type Phrase} from '../script';
import type {Glass} from '../glass/renderer';
import {BRAND, COL, FONT, bouncy, clamp01, lerp} from '../theme';
import {REGULAR} from './kit';

const PHRASES: Phrase[] = TIMELINE.flatMap((s) => s.phrases);
const SIZE = 60;
const GAP = 15;
const LINE = 74;
const MAXW = 860;
const PAD = 24;
export const ISLAND_TOP = 242;

const ACCENT: Record<string, string> = {green: COL.leaf, amber: COL.amber, blue: COL.water, red: BRAND.red};

type Box = {x: number; w: number; line: number};
type Layout = {words: Box[]; lineW: number[]; width: number; lines: number};

let ctx2d: CanvasRenderingContext2D | null = null;
const measure = (text: string) => {
  if (!ctx2d) {
    ctx2d = document.createElement('canvas').getContext('2d')!;
    ctx2d.font = `700 ${SIZE}px Inter`;
    (ctx2d as unknown as {letterSpacing: string}).letterSpacing = `${-0.02 * SIZE}px`;
  }
  return ctx2d.measureText(text).width;
};

const cache = new Map<number, Layout>();
const layoutOf = (i: number): Layout => {
  const hit = cache.get(i);
  if (hit) return hit;
  const words: Box[] = [];
  const lineW: number[] = [0];
  for (const w of PHRASES[i].words) {
    const bw = measure(w.text) + (w.hl ? PAD : 0);
    let line = lineW.length - 1;
    if (lineW[line] > 0 && lineW[line] + GAP + bw > MAXW) {
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

const visEnd = (i: number) => {
  const next = PHRASES[i + 1];
  return Math.min(next ? next.start * FPS - 7 : Infinity, (PHRASES[i].end + 0.45) * FPS);
};

type Dims = {w: number; h: number; y: number};
const HIDDEN: Dims = {w: 0, h: 0, y: ISLAND_TOP + LINE / 2};
const dimsOf = (i: number): Dims => {
  const l = layoutOf(i);
  return {w: l.width / 2 + 40, h: (l.lines * LINE) / 2 + 18, y: ISLAND_TOP + (l.lines * LINE) / 2};
};

type Ev = {f: number; d: Dims};
let EVENTS: Ev[] | null = null;
const events = (): Ev[] => {
  if (EVENTS) return EVENTS;
  const ev: Ev[] = [{f: -1, d: HIDDEN}];
  PHRASES.forEach((p, i) => {
    ev.push({f: p.start * FPS - 5, d: dimsOf(i)});
    const next = PHRASES[i + 1];
    const end = visEnd(i);
    if (!next || next.start * FPS - end > 20) ev.push({f: end, d: {w: 30, h: 30, y: ISLAND_TOP + 30}});
  });
  ev.push({f: ev[ev.length - 1].f + 22, d: HIDDEN});
  EVENTS = ev;
  return ev;
};

const blend = (a: Dims, b: Dims, t: number, th = t): Dims => ({w: lerp(a.w, b.w, t), h: lerp(a.h, b.h, th), y: lerp(a.y, b.y, t)});
const dimsAt = (f: number): Dims => {
  const ev = events();
  let k = 0;
  while (k + 1 < ev.length && ev[k + 1].f <= f) k++;
  if (k === 0) return ev[0].d;
  const from = k >= 2 ? blend(ev[k - 2].d, ev[k - 1].d, bouncy(ev[k].f, ev[k - 1].f)) : ev[k - 1].d;
  // larghezza e altezza con molle leggermente sfasate: il vetro "si assesta" come un gel
  return blend(from, ev[k].d, bouncy(f, ev[k].f), bouncy(f, ev[k].f + 3));
};

export const islandGlass = (f: number): Glass => {
  const d = dimsAt(f);
  return {...REGULAR, x: 540, y: d.y, w: Math.max(0, d.w), h: Math.max(0, d.h), r: Math.min(d.h, 46), k: 0, dim: 0.24, frost: 0.62, mat: clamp01(d.w / 40)};
};

const Word: React.FC<{p: Phrase; i: number; j: number; f: number}> = ({p, i, j, f}) => {
  const w = p.words[j];
  const l = layoutOf(i);
  const box = l.words[j];
  const s = w.start * FPS;
  const a = clamp01((f - s + 2) / 9);
  const e = 1 - Math.pow(1 - a, 3);
  const pill = w.hl ? clamp01((f - s) / 10) : 0;
  const pop = interpolate(f, [s, s + 5, s + 18], [0, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const col = ACCENT[p.color] ?? COL.leaf;
  return (
    <div
      style={{
        position: 'absolute',
        left: 540 - l.lineW[box.line] / 2 + box.x,
        top: ISLAND_TOP + box.line * LINE,
        width: box.w,
        height: LINE,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontFamily: FONT,
        fontWeight: 700,
        fontSize: SIZE,
        letterSpacing: '-0.02em',
        color: '#FFFFFF',
        opacity: e,
        transform: `translateY(${(1 - e) * 18}px) scale(${0.9 + 0.1 * e + 0.05 * pop})`,
        filter: e < 0.999 ? `blur(${(1 - e) * 8}px)` : undefined,
        textShadow: '0 1px 2px rgba(0,0,0,0.3)',
      }}
    >
      {w.hl && (
        <div
          style={{
            position: 'absolute',
            inset: '9px 0 7px 0',
            borderRadius: 999,
            background: col,
            transform: `scaleX(${pill})`,
            transformOrigin: 'left center',
            boxShadow: `0 6px 20px ${col}55, inset 0 1.5px 0 rgba(255,255,255,0.6)`,
          }}
        />
      )}
      <span style={{position: 'relative', whiteSpace: 'nowrap'}}>{w.text}</span>
    </div>
  );
};

export const IslandText: React.FC = () => {
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{pointerEvents: 'none'}}>
      {PHRASES.map((p, i) => {
        const end = visEnd(i);
        if (f < p.start * FPS - 3 || f > end + 6) return null;
        const out = clamp01((f - end) / 6);
        return (
          <div key={i} style={{position: 'absolute', inset: 0, opacity: 1 - out, filter: out > 0 ? `blur(${out * 6}px)` : undefined}}>
            {p.words.map((_, j) => (
              <Word key={j} p={p} i={i} j={j} f={f} />
            ))}
          </div>
        );
      })}
    </AbsoluteFill>
  );
};
