// Scena 1: una goccia di vetro si scioglie in 1.024 perle, che poi si ritirano
// mentre il liquido "scrive" le lettere E-T-F.
import React from 'react';
import type {Shape} from '../glass/renderer';
import type {SceneDef} from '../world';
import {Label} from '../../components/Primitives';
import {C, FONT, fmtInt} from '../../theme';
import {G, RED, easeIn, easeInOut, easeOut, hash, lerp, prog, spr, type Ctx} from '../kit';

export const DROP = {x: 540, y: 980, r: 86};

/** La goccia a riposo che respira: è anche l'ultimo fotogramma del video (loop). */
export const dropletRest = (f: number): Shape => {
  const sq = 0.07 * Math.sin(f * 0.11);
  return {
    x: DROP.x,
    y: DROP.y,
    w: DROP.r * (1 + sq),
    h: DROP.r * (1 - sq),
    r: DROP.r * (1 - Math.abs(sq)),
    k: 40,
    tint: G,
    tintAmt: 0.45,
    refr: 1.25,
  };
};

const T = 27;
// Tratti delle lettere: ogni tratto cresce come liquido dal suo punto d'inizio.
const STROKES = [
  {x0: 217, y0: 756, x1: 217, y1: 1044, d: 0},
  {x0: 217, y0: 783, x1: 392, y1: 783, d: 6},
  {x0: 217, y0: 900, x1: 362, y1: 900, d: 9},
  {x0: 217, y0: 1017, x1: 392, y1: 1017, d: 12},
  {x0: 440, y0: 783, x1: 640, y1: 783, d: 10},
  {x0: 540, y0: 783, x1: 540, y1: 1044, d: 15},
  {x0: 717, y0: 756, x1: 717, y1: 1044, d: 18},
  {x0: 717, y0: 783, x1: 892, y1: 783, d: 22},
  {x0: 717, y0: 900, x1: 862, y1: 900, d: 25},
];

const CANDLES = (() => {
  let v = 0;
  return Array.from({length: 9}, (_, i) => {
    const o = v;
    v += (hash(i * 3.7) - 0.36) * 60;
    return {x: 540 + (i - 4) * 76, top: Math.min(o, v), bot: Math.max(o, v), up: v >= o};
  });
})();

const cues = (c: Ctx) => ({G: c.cue('grid'), M: c.cue('mille'), E: c.cue('etf'), B: c.cue('borsa'), A: c.cue('azione')});

const pillPos = (f: number, B: number): [number, number] => {
  const u = easeInOut(prog(f, B - 4, B + 22));
  return [lerp(717, 540, u), lerp(1044, 1206, u)];
};

export const hook: SceneDef = {
  ringFrom: [540, 980],
  shapes: (c) => {
    const {f} = c;
    const {G: g, E, B, A} = cues(c);
    const out: Shape[] = [];
    if (f < g + 24) {
      const melt = easeIn(prog(f, g - 8, g + 24));
      const d = dropletRest(f);
      const k = 1 - melt * (1 - 9 / DROP.r);
      out.push({...d, w: d.w * k, h: (d.h ?? d.w) * k, r: (d.r ?? 0) * k});
    }
    // capsula di vetro dietro il contatore
    const cnt = spr(c.f, g + 4, 14, 150) * (1 - easeIn(prog(f, E - 6, E + 10)));
    if (cnt > 0.01) out.push({x: 540, y: 1478, w: 200 * cnt, h: 50 * cnt, r: 50 * cnt, tint: G, tintAmt: 0.18, frost: 0.4});
    if (f >= E - 2) {
      STROKES.forEach((s, i) => {
        const p = spr(f, E + s.d, 14, 120);
        const bob = Math.sin((f - E) * 0.06 + i * 0.7) * 2.5 * prog(f, E + 40, E + 80);
        const x1 = lerp(s.x0, s.x1, p);
        const y1 = lerp(s.y0, s.y1, p);
        const cx = (s.x0 + x1) / 2;
        const cy = (s.y0 + y1) / 2 + bob;
        const half = Math.hypot(x1 - s.x0, y1 - s.y0) / 2 + T;
        const vertical = s.x0 === s.x1;
        out.push({x: cx, y: cy, w: vertical ? T : half, h: vertical ? half : T, r: T, k: 22, tint: G, tintAmt: 0.5, refr: 1.35});
      });
    }
    if (f >= B - 4) {
      const [x, y] = pillPos(f, B);
      const g2 = spr(f, B + 8, 12, 130);
      out.push({x, y, w: lerp(T, 300, g2), h: lerp(T, 44, g2), r: lerp(T, 44, g2), k: 34, tint: G, tintAmt: 0.22, frost: 0.35});
    }
    if (f >= A - 2) {
      CANDLES.forEach((k, i) => {
        const s = spr(f, A + i * 3, 12, 160);
        const hh = Math.max(12, (k.bot - k.top) / 2 + 12) * s;
        out.push({x: k.x, y: 1338 + (k.top + k.bot) / 2 - 10, w: 15 * Math.min(1, s * 1.4), h: hh, r: 15, tint: k.up ? G : RED, tintAmt: 0.6});
      });
    }
    return out;
  },
  extras: (c) => {
    const {f} = c;
    const {G: g, M, E} = cues(c);
    const ripple =
      f < g ? {x: 540, y: 980, age: f / 60, amp: 0.9}
      : f < M ? {x: 540, y: 980, age: (f - g) / 60, amp: 1}
      : f < E ? {x: 540, y: 980, age: (f - M) / 60, amp: 0.6}
      : {x: 540, y: 900, age: (f - E) / 60, amp: 0.8};
    if (f < g - 6 || f > E + 30) return {ripple};
    const bump = Math.exp(-Math.pow((f - M - 10) / 18, 2));
    return {
      ripple,
      beads: {
        cell: 26, r: 8.6, k: 14, x0: 124, y0: 564, cols: 32, rows: 32,
        cx: 540, cy: 980, reveal: easeOut(prog(f, g - 6, g + 60)) * 1150, shrink: easeIn(prog(f, E - 4, E + 26)),
        tint: G, tintAmt: 0.15 + 0.45 * easeInOut(prog(f, M, M + 40)),
        waveAmp: 0.14 + 0.28 * bump, waveFreq: 0.035, waveSpeed: 5,
        redCol: -9, redRow: -9, redAmt: 0, redGone: 0, side: 2,
      },
    };
  },
  Overlay: ({c}) => {
    const {f} = c;
    const {G: g, M, E, B} = cues(c);
    const n = Math.round(lerp(1, 1000, easeInOut(prog(f, g + 6, M + 46))));
    const cnt = spr(f, g + 4, 14, 150) * (1 - easeIn(prog(f, E - 6, E + 10)));
    const lab = prog(f, E + 34, E + 62);
    return (
      <>
        <Label
          size={30}
          color={C.text}
          style={{
            position: 'absolute',
            top: DROP.y + 110,
            width: '100%',
            textAlign: 'center',
            opacity: prog(f, 8, 22) * (1 - prog(f, g - 8, g + 4)),
            transform: `translateY(${(1 - easeOut(prog(f, 8, 22))) * 16}px)`,
          }}
        >
          1 acquisto
        </Label>
        {cnt > 0.05 && (
          <div
            style={{
              position: 'absolute',
              top: 1478 - 38,
              width: '100%',
              display: 'flex',
              alignItems: 'baseline',
              justifyContent: 'center',
              gap: 14,
              opacity: Math.min(1, cnt * 1.3),
              transform: `scale(${0.8 + 0.2 * Math.min(1, cnt)})`,
            }}
          >
            <span style={{fontFamily: FONT, fontWeight: 900, fontSize: 64, lineHeight: 1, color: C.text, fontVariantNumeric: 'tabular-nums'}}>
              {fmtInt(n)}
              {n >= 1000 ? '+' : ''}
            </span>
            <Label size={26} color={C.text}>
              aziende
            </Label>
          </div>
        )}
        {lab > 0 && (
          <Label
            size={32}
            color={C.dim}
            style={{
              position: 'absolute',
              top: 1100,
              width: '100%',
              textAlign: 'center',
              letterSpacing: '0.34em',
              clipPath: `inset(0 ${(1 - easeInOut(lab)) * 100}% 0 0)`,
            }}
          >
            <span style={{color: C.green}}>E</span>xchange <span style={{color: C.green}}>T</span>raded{' '}
            <span style={{color: C.green}}>F</span>und
          </Label>
        )}
        {f >= B + 14 && (
          <div
            style={{
              position: 'absolute',
              top: 1206 - 24,
              width: '100%',
              textAlign: 'center',
              fontFamily: FONT,
              fontWeight: 700,
              fontSize: 36,
              lineHeight: '48px',
              color: C.text,
              opacity: prog(f, B + 14, B + 26),
              textShadow: '0 2px 12px rgba(0,0,0,0.5)',
            }}
          >
            = fondo quotato in borsa
          </div>
        )}
      </>
    );
  },
};
