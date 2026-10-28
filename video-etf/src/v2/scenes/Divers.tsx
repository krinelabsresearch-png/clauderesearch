// Scena 3: il cartello "01" si divide come un liquido in due carte. La singola
// azione crolla e va in frantumi; nell'ETF cade una sola perla su 1.000.
import React from 'react';
import type {Shape} from '../glass/renderer';
import type {SceneDef} from '../world';
import {Label} from '../../components/Primitives';
import {C, FONT, fmtPct} from '../../theme';
import {BLU, G, RED, easeIn, easeInOut, easeOut, hash, lerp, mixRGB, prog, spr, type Ctx} from '../kit';
import {SlabText, slabShape} from './common';

const A = {x: 540, y: 760, w: 460, h: 175};
const B = {x: 540, y: 1235, w: 460, h: 210};
const SLAB = {x: 540, y: 900, w: 380, h: 150};
const BEAD = {cell: 17, cols: 50, rows: 20, x0: 115, y0: 1088};
const RED_BEAD = {col: 31, row: 9};

const cues = (c: Ctx) => {
  const C0 = c.cue('crash');
  return {P: c.cue('panels'), Cr: C0, S: C0 + 42, Ep: c.cue('etfpanel'), O: c.cue('onered'), Dp: c.cue('dip')};
};

const split = (f: number, P: number) => easeInOut(prog(f, P - 34, P - 4));

const redBead = () => ({x: BEAD.x0 + (RED_BEAD.col + 0.5) * BEAD.cell, y: BEAD.y0 + (RED_BEAD.row + 0.5) * BEAD.cell});

// Serie della singola azione e dell'ETF: stesso crollo, peso diverso.
const N = 60;
const noise = (i: number, s: number) => Math.sin(i * 0.9 + s) * 0.8 + Math.sin(i * 0.37 + s * 2) * 0.6;
const single = (i: number) => (i < 34 ? 0 : -60 * easeIn(Math.min(1, (i - 34) / 10))) + noise(i, 1.3);
const basketV = (i: number) => (i < 34 ? 0 : -0.06 * easeIn(Math.min(1, (i - 34) / 10))) + noise(i, 4.1);

const LinePath: React.FC<{x: number; y: number; w: number; h: number; fn: (i: number) => number; reveal: number; color: string; redFrom?: number}> = ({
  x, y, w, h, fn, reveal, color, redFrom = Infinity,
}) => {
  const pts: string[] = [];
  const red: string[] = [];
  const top = 8;
  const bottom = -66;
  const py = (v: number) => y + ((top - v) / (top - bottom)) * h;
  const last = Math.min(N - 1, reveal);
  for (let i = 0; i <= Math.floor(last); i++) {
    const p = `${(x + (i / (N - 1)) * w).toFixed(1)},${py(fn(i)).toFixed(1)}`;
    if (i <= redFrom) pts.push(p);
    if (i >= redFrom) red.push(p);
  }
  const head = Math.floor(last);
  return (
    <svg width={1080} height={1920} style={{position: 'absolute', inset: 0, overflow: 'visible'}}>
      {pts.length > 1 && <polyline points={pts.join(' ')} fill="none" stroke={color} strokeWidth={6} strokeLinejoin="round" strokeLinecap="round" />}
      {red.length > 1 && <polyline points={red.join(' ')} fill="none" stroke={C.red} strokeWidth={6} strokeLinejoin="round" strokeLinecap="round" />}
      {head >= 0 && <circle cx={x + (head / (N - 1)) * w} cy={py(fn(head))} r={9} fill={head >= redFrom ? C.red : color} />}
    </svg>
  );
};

export const divers: SceneDef = {
  ringFrom: [540, 900],
  shapes: (c) => {
    const {f} = c;
    const {P, Cr, S, O} = cues(c);
    const out: Shape[] = [];
    const u = split(f, P);
    if (f < P - 34) {
      out.push(slabShape(f, SLAB, G));
    } else {
      const k = lerp(150, 0, u);
      const hit = prog(f, Cr, Cr + 10);
      const shake = f > Cr && f < S ? Math.sin((f - Cr) * 1.9) * 11 * Math.exp(-(f - Cr) / 14) : 0;
      if (f < S) {
        out.push({
          x: lerp(SLAB.x, A.x, u) + shake, y: lerp(SLAB.y, A.y, u), w: lerp(SLAB.w, A.w, u), h: lerp(SLAB.h, A.h, u), r: 44, k,
          tint: mixRGB(BLU, RED, hit), tintAmt: 0.12 + 0.4 * hit, frost: 0.35,
        });
        const ic = spr(f, P + 6, 12, 160);
        out.push({x: 150 + shake, y: A.y + 30, w: 50 * ic, h: 50 * ic, r: 16 * ic, k: 0, tint: mixRGB(BLU, RED, hit), tintAmt: 0.65});
      } else {
        // la carta va in frantumi: 12 pezzi che cadono, ruotano e si arrotondano in gocce
        const t = f - S;
        for (let j = 0; j < 3; j++) {
          for (let i = 0; i < 4; i++) {
            const id = j * 4 + i;
            const x0 = A.x - A.w + 115 + i * 230;
            const y0 = A.y - A.h + 58.3 + j * 116.7;
            const vx = (i - 1.5) * 2.4 + (hash(id) - 0.5) * 2.5;
            const vy = -3 - hash(id + 9) * 5;
            const sc = 1 - easeIn(prog(t, 18 + hash(id) * 10, 70 + hash(id) * 20));
            if (sc <= 0.01) continue;
            const round = prog(t, 6, 36);
            const hw = lerp(112, 50, round) * sc;
            const hh = lerp(55, 50, round) * sc;
            out.push({
              x: x0 + vx * t, y: y0 + vy * t + 0.38 * t * t, w: hw, h: hh, r: lerp(14, 50, round) * sc,
              rot: (hash(id + 4) - 0.5) * 0.09 * t, k: lerp(2, 26, prog(t, 0, 24)), tint: RED, tintAmt: 0.55,
            });
          }
        }
      }
      // carta ETF: prima solida, poi cornice di vetro piena di perle
      const sh = prog(u, 0.7, 1);
      const solid = 1 - sh;
      if (solid > 0.01) {
        out.push({x: lerp(SLAB.x, B.x, u), y: lerp(SLAB.y, B.y, u), w: lerp(SLAB.w, B.w, u) * (0.3 + 0.7 * solid), h: lerp(SLAB.h, B.h, u) * (0.3 + 0.7 * solid), r: 44, k: Math.max(k, 40), tint: G, tintAmt: 0.2, frost: 0.3});
      }
      if (sh > 0.01) out.push({x: B.x, y: B.y, w: B.w * (0.9 + 0.1 * sh), h: B.h * (0.9 + 0.1 * sh), r: 44, kind: 'shell', thick: 9 * sh, k: 40, tint: G, tintAmt: 0.25});
      // la perla rossa che si stacca e cade
      if (f >= O + 40) {
        const t = f - O - 40;
        const rb = redBead();
        const sc = 1 - easeIn(prog(t, 34, 60));
        if (sc > 0.01) out.push({x: rb.x, y: rb.y + 0.32 * t * t, w: 9 * sc * (1 + Math.min(0.5, t * 0.02)), h: 9 * sc, r: 9 * sc, rot: Math.PI / 2, k: 10, tint: RED, tintAmt: 0.75});
      }
    }
    return out;
  },
  extras: (c) => {
    const {f} = c;
    const {P, Ep, O} = cues(c);
    if (f < P - 10) return {};
    return {
      beads: {
        cell: BEAD.cell, r: 5.8, k: 3, x0: BEAD.x0, y0: BEAD.y0, cols: BEAD.cols, rows: BEAD.rows,
        cx: B.x, cy: B.y, reveal: easeOut(prog(f, P - 8, P + 50)) * 700, shrink: 0,
        tint: G, tintAmt: 0.22 + 0.36 * prog(f, Ep - 6, Ep + 14),
        waveAmp: 0.12, waveFreq: 0.05, waveSpeed: 4,
        redCol: RED_BEAD.col, redRow: RED_BEAD.row, redAmt: prog(f, O, O + 10), redGone: easeIn(prog(f, O + 36, O + 46)), side: 2,
      },
    };
  },
  Overlay: ({c}) => {
    const {f} = c;
    const {P, Cr, S, Ep, O, Dp} = cues(c);
    const u = split(f, P);
    const showA = prog(f, P - 6, P + 10);
    const fallA = easeIn(prog(f, S, S + 26));
    const shake = f > Cr && f < S ? Math.sin((f - Cr) * 1.9) * 11 * Math.exp(-(f - Cr) / 14) : 0;
    const crash = Math.min(1, Math.max(0, (f - Cr) / 40));
    const revA = f < Cr ? lerp(0, 34, prog(f, P + 10, Cr)) : f < Cr + 40 ? lerp(34, 46, prog(f, Cr, Cr + 40)) : lerp(46, 59, prog(f, Cr + 40, S));
    const revB = f < O ? lerp(0, 34, prog(f, Ep, O)) : f < O + 40 ? lerp(34, 46, prog(f, O, O + 40)) : lerp(46, 59, prog(f, O + 40, Dp + 40));
    const crashB = Math.min(1, Math.max(0, (revB - 34) / 10));
    const showB = prog(f, P - 6, P + 10) * (0.5 + 0.5 * prog(f, Ep - 6, Ep + 10));
    const big = easeOut(prog(f, S + 4, S + 30));
    return (
      <>
        <SlabText f={f} num="01" title="DIVERSIFICAZIONE" color={C.green} y={SLAB.y} hideAt={P - 40} />
        {u > 0.6 && (
          <div style={{position: 'absolute', inset: 0, opacity: showA * (1 - fallA), transform: `translate(${shake}px, ${fallA * 160}px) rotate(${fallA * 4}deg)`}}>
            <Label style={{position: 'absolute', left: 116, top: A.y - A.h + 34}}>Una sola azione</Label>
            <LinePath x={280} y={A.y - 90} w={680} h={210} fn={single} reveal={revA} color={C.blue} redFrom={34} />
            <svg width={60} height={60} viewBox="0 0 24 24" style={{position: 'absolute', left: 150 - 30, top: A.y + 30 - 30}}>
              <g fill="#fff">
                <rect x={5} y={13} width={3} height={6} rx={1} />
                <rect x={10.5} y={9} width={3} height={10} rx={1} />
                <rect x={16} y={5} width={3} height={14} rx={1} />
              </g>
            </svg>
          </div>
        )}
        {u > 0.6 && (
          <div
            style={{
              position: 'absolute',
              right: lerp(116, 0, big),
              left: lerp(1080 - 116 - 300, 0, big),
              top: lerp(A.y - A.h + 18, A.y - 70, big),
              textAlign: big > 0.5 ? 'center' : 'right',
              fontFamily: FONT,
              fontWeight: 900,
              fontSize: lerp(60, 132, big),
              color: crash > 0 ? C.red : C.text,
              fontVariantNumeric: 'tabular-nums',
              opacity: showA,
              textShadow: big > 0 ? `0 0 ${40 * big}px rgba(248,113,113,0.5)` : undefined,
            }}
          >
            {fmtPct(-60 * crash, 0)}
          </div>
        )}
        {u > 0.6 && (
          <div style={{position: 'absolute', inset: 0, opacity: showB}}>
            <Label style={{position: 'absolute', left: 116, top: B.y - B.h + 26}}>
              <span style={{color: C.green}}>ETF</span> · 1.000 aziende
            </Label>
            <div style={{position: 'absolute', right: 116, top: B.y - B.h + 10, fontFamily: FONT, fontWeight: 900, fontSize: 56, color: crashB > 0 ? C.amber : C.text, fontVariantNumeric: 'tabular-nums'}}>
              {fmtPct(-0.06 * crashB, 2)}
            </div>
            <LinePath x={130} y={BEAD.y0 + 60} w={820} h={240} fn={basketV} reveal={revB} color={C.green} />
          </div>
        )}
        <div
          style={{
            position: 'absolute',
            top: B.y + B.h + 26,
            width: '100%',
            textAlign: 'center',
            fontFamily: FONT,
            fontWeight: 500,
            fontSize: 24,
            color: C.dim,
            opacity: prog(f, O, O + 20),
          }}
        >
          Esempio semplificato: 1.000 aziende con lo stesso peso.
        </div>
      </>
    );
  },
};
