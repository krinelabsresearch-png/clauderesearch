// Scena 2: un vaso di vetro si riempie di liquido; le aziende (biglie di vetro)
// ci cadono dentro sollevando onde, poi dal liquido emerge una bolla-globo.
import React from 'react';
import type {Shape} from '../glass/renderer';
import type {SceneDef} from '../world';
import {C, FONT} from '../../theme';
import {G, SECTOR, WHITE, easeIn, easeOut, hash, lerp, prog, spr, type Ctx} from '../kit';

const CUP = {x: 540, y: 1185, w: 340, h: 215};
const LIQ = {x: 540, y: 1193, w: 326, h: 200};
const N = 11;
const MR = 40;

const cues = (c: Ctx) => ({D: c.cue('drop'), I: c.cue('indice'), Gb: c.cue('globe')});

const landing = (k: number, D: number) => D - 4 + k * 6 + 24;

const fillAt = (f: number, D: number) => {
  let fill = 0.24;
  for (let k = 0; k < N; k++) fill += 0.035 * easeOut(prog(f, landing(k, D), landing(k, D) + 24));
  return fill;
};
const surfaceY = (fill: number) => LIQ.y - LIQ.h + 2 * LIQ.h * (1 - fill);

const marble = (k: number, f: number, D: number, surf: number) => {
  const row = k < 6 ? 0 : 1;
  const col = row === 0 ? k : k - 6;
  const xT = row === 0 ? 540 + (col - 2.5) * 98 : 540 + (col - 2) * 98;
  const yT = row === 0 ? surf + 36 : surf - 38;
  const t0 = D - 4 + k * 6;
  const tl = landing(k, D);
  if (f < t0) return null;
  if (f < tl) {
    const u = (f - t0) / (tl - t0);
    return {x: lerp(xT + (hash(k + 3) - 0.5) * 260, xT, easeOut(u)), y: lerp(-140, yT, u * u)};
  }
  const dt = f - tl;
  return {x: xT, y: yT + 30 * Math.exp(-dt / 9) * Math.sin(dt / 3.6) + Math.sin(f * 0.07 + k) * 2.5};
};

const swing = (f: number, I: number) => {
  const dt = Math.max(0, f - I);
  return 0.6 * Math.exp(-dt / 18) * Math.cos(dt / 5.4);
};
const ANCHOR = {x: 872, y: CUP.y - CUP.h + 6};

const globePos = (f: number, Gb: number, surf: number) => {
  const u = easeOut(prog(f, Gb - 2, Gb + 34));
  return {x: 540, y: lerp(surf, 668, u), r: lerp(26, 205, spr(f, Gb, 13, 90))};
};

export const basket: SceneDef = {
  ringFrom: [540, 1180],
  shapes: (c) => {
    const {f} = c;
    const {D, I, Gb} = cues(c);
    const rise = (1 - spr(f, 0, 15, 110)) * 360;
    const fill = fillAt(f, D);
    const surf = surfaceY(fill);
    let wave = 4;
    for (let k = 0; k < N; k++) {
      const dt = f - landing(k, D);
      if (dt > 0) wave += 13 * Math.exp(-dt / 16);
    }
    const out: Shape[] = [
      {x: CUP.x, y: CUP.y + rise, w: CUP.w, h: CUP.h, r: 70, kind: 'cup', thick: 10, tint: WHITE, tintAmt: 0.05, refr: 1.1},
      {x: LIQ.x, y: LIQ.y + rise, w: LIQ.w, h: LIQ.h, r: 62, kind: 'liquid', fill, wave: Math.min(wave, 24), k: 0, tint: G, tintAmt: 0.62, refr: 1.5},
    ];
    for (let k = 0; k < N; k++) {
      const m = marble(k, f, D, surf);
      if (m) out.push({x: m.x, y: m.y, w: MR, kind: 'circle', k: 12, tint: SECTOR[k % SECTOR.length], tintAmt: 0.58, refr: 1.2});
    }
    if (f >= I - 4) {
      const a = swing(f, I);
      const app = spr(f, I - 4, 12, 170);
      out.push({x: ANCHOR.x - Math.sin(a) * 104, y: ANCHOR.y + Math.cos(a) * 104, w: 98 * app, h: 40 * app, r: 20 * app, rot: a, tint: WHITE, tintAmt: 0.12, frost: 0.4});
    }
    if (f >= Gb - 2) {
      const gp = globePos(f, Gb, surf);
      out.push({x: gp.x, y: gp.y, w: gp.r, kind: 'circle', k: 46, tint: [0.6, 0.85, 1], tintAmt: 0.1, refr: 1.7, mag: 0.28});
    }
    return out;
  },
  extras: (c) => {
    const {f} = c;
    const {D} = cues(c);
    let last = -1;
    for (let k = 0; k < N; k++) if (f >= landing(k, D)) last = k;
    if (last < 0) return {};
    const surf = surfaceY(fillAt(f, D));
    const m = marble(last, landing(last, D), D, surf)!;
    return {ripple: {x: m.x, y: surf, age: (f - landing(last, D)) / 60, amp: 0.6}};
  },
  Overlay: ({c}) => {
    const {f} = c;
    const {D, I, Gb} = cues(c);
    const surf = surfaceY(fillAt(f, D));
    const a = swing(f, I);
    const app = spr(f, I - 4, 12, 170);
    const gp = globePos(f, Gb, surf);
    const dots = prog(f, Gb + 18, Gb + 40);
    const ang = f * 0.014;
    return (
      <>
        {f >= I - 4 && (
          <div
            style={{
              position: 'absolute',
              left: ANCHOR.x,
              top: ANCHOR.y,
              width: 0,
              height: 0,
              transform: `rotate(${a}rad)`,
              opacity: Math.min(1, app),
            }}
          >
            <div style={{position: 'absolute', left: -1.5, top: 0, width: 3, height: 64, background: 'rgba(255,255,255,0.7)', borderRadius: 2}} />
            <div style={{position: 'absolute', left: -7, top: -7, width: 14, height: 14, borderRadius: 7, background: C.text}} />
            <div
              style={{
                position: 'absolute',
                left: -98,
                top: 104 - 40,
                width: 196,
                height: 80,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                fontFamily: FONT,
                fontWeight: 900,
                fontSize: 34,
                letterSpacing: '0.14em',
                color: C.text,
                transform: `scale(${app})`,
                textShadow: '0 2px 10px rgba(0,0,0,0.5)',
              }}
            >
              INDICE
            </div>
          </div>
        )}
        {dots > 0 && (
          <svg width={1080} height={1920} style={{position: 'absolute', inset: 0, opacity: dots}}>
            {Array.from({length: 420}, (_, i) => {
              const yy = 1 - (i / 419) * 2;
              const rr = Math.sqrt(1 - yy * yy);
              const th = i * 2.39996 + ang;
              const z = Math.sin(th) * rr;
              if (z < 0) return null;
              const lit = hash(i * 7.7) < 0.22;
              const R = gp.r * 0.82;
              const cx = gp.x + Math.cos(th) * rr * R;
              const cy = gp.y + (yy * Math.cos(0.38) - z * Math.sin(0.38)) * R;
              const lp = lit ? easeIn(prog(f, Gb + 22 + hash(i) * 30, Gb + 34 + hash(i) * 30)) : 0;
              return lit && lp > 0 ? (
                <g key={i}>
                  <circle cx={cx} cy={cy} r={8 * lp} fill={C.green} opacity={0.3 * lp} />
                  <circle cx={cx} cy={cy} r={2.5 + 2 * lp} fill={C.green} />
                </g>
              ) : (
                <circle key={i} cx={cx} cy={cy} r={2.2} fill="#CFE3F5" opacity={0.25 + 0.5 * z} />
              );
            })}
          </svg>
        )}
      </>
    );
  },
};
