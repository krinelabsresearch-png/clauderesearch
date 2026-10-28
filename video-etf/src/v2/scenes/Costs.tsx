// Scena 4: monete di vetro si impilano (1.000 commissioni), poi si fondono in un
// solo ordine che diventa il liquido di un tubo; dal liquido si stacca la goccia da 2 €.
import React from 'react';
import type {Shape} from '../glass/renderer';
import type {SceneDef} from '../world';
import {Label} from '../../components/Primitives';
import {C, FONT, fmtInt} from '../../theme';
import {AMB, G, droplet, easeIn, easeInOut, easeOut, hash, lerp, mixRGB, prog, spr, type Ctx} from '../kit';
import {SlabText, slabShape} from './common';

const SLAB = {x: 540, y: 900, w: 300, h: 140};
const BASE = 1300;
const STEP = 34;
const MAXC = 18;
const TUBE = {x: 540, y: 900, w: 440, h: 76};
const LIQ_L = TUBE.x - TUBE.w + 16;
const LIQ_R = TUBE.x + TUBE.w - 16;

const cues = (c: Ctx) => ({S: c.cue('stream'), Th: c.cue('thousand'), K: c.cue('collapse'), Bc: c.cue('bar'), Tc: c.cue('ter'), Tw: c.cue('twoeur')});

// La moneta k atterra quando il contatore (che accelera) la raggiunge.
const growEnd = (S: number, Th: number) => Th + 8;
const fallWindow = (k: number, S: number, Th: number): [number, number] => {
  const span = growEnd(S, Th) - S;
  return [S + span * Math.cbrt((k - 1) / (MAXC - 1)), S + span * Math.cbrt(k / (MAXC - 1))];
};

const coin = (k: number, f: number, cu: ReturnType<typeof cues>): Shape | null => {
  const {S, Th, K} = cu;
  const yT = BASE - k * STEP;
  const jit = (hash(k * 5) - 0.5) * 18;
  const col = easeInOut(prog(f, K, K + 26));
  let y = yT;
  if (k > 0) {
    const [a, b] = fallWindow(k, S, Th);
    if (f < a) return null;
    if (f < b) y = lerp(yT - 560, yT, easeIn((f - a) / Math.max(1, b - a)));
    else y = yT - 14 * Math.exp(-(f - b) / 6) * Math.abs(Math.sin((f - b) / 3));
  }
  y = lerp(y, BASE, col);
  const big = k === 0 ? 1 : 1 - 0.5 * col;
  return {
    x: 540 + jit * (1 - col), y, w: lerp(150, k === 0 ? 190 : 150, col) * big, h: lerp(24, k === 0 ? 42 : 24, col) * big, r: 40,
    rot: (hash(k * 7) - 0.5) * 0.06 * (1 - col), k: lerp(5, 70, col), tint: mixRGB(AMB, G, col), tintAmt: 0.6,
  };
};

const orderPos = (f: number, Bc: number): [number, number] => {
  const u = easeInOut(prog(f, Bc - 10, Bc + 14));
  return [lerp(540, LIQ_L + 50, u), lerp(BASE, TUBE.y, u) - Math.sin(u * Math.PI) * 160];
};

const twoPos = (f: number, Tc: number): [number, number] => {
  const u = easeInOut(prog(f, Tc, Tc + 30));
  return [lerp(LIQ_R - 30, 842, u), lerp(TUBE.y, 1180, u)];
};

export const costs: SceneDef = {
  ringFrom: [540, 1300],
  shapes: (c) => {
    const {f} = c;
    const cu = cues(c);
    const {S, Th, K, Bc, Tc} = cu;
    const out: Shape[] = [];
    if (f < S + 6) {
      const s = slabShape(f, SLAB, AMB);
      const u = easeInOut(prog(f, S - 16, S + 6));
      out.push({...s, x: 540, y: lerp(s.y, BASE, u), w: lerp(s.w, 150, u), h: lerp(s.h ?? s.w, 24, u), r: lerp(s.r ?? 0, 24, u)});
    }
    if (f >= S + 6 && f < Bc - 10) {
      const n = f < K + 26 ? MAXC : 1;
      for (let k = 0; k < n; k++) {
        const cs = coin(k, f, cu);
        if (cs) out.push(cs);
      }
      if (f < Th + 10) {
        for (let j = 0; j < 4; j++) {
          const pos = (ff: number): [number, number] => {
            const ph = (((ff - S) * 1.3 + j * 15) % 60) / 60;
            const top = BASE - (MAXC - 1) * STEP * easeIn(prog(ff, S, Th + 8));
            return [lerp(1180, 560, easeIn(ph)), lerp(560 + j * 100, top - 40, ph) - Math.sin(ph * Math.PI) * 120];
          };
          const fade = 1 - prog(f, Th, Th + 10);
          out.push(droplet(pos, f, 30 * fade, {h: 14 * fade, tint: AMB, tintAmt: 0.6, k: 0}, 0.02));
        }
      }
    }
    if (f >= Bc - 10) {
      const tube = spr(f, Bc - 14, 13, 140);
      out.push({x: TUBE.x, y: TUBE.y, w: TUBE.w * tube, h: TUBE.h * tube, r: TUBE.h * tube, kind: 'shell', thick: 8, k: 20, tint: [0.8, 0.9, 1], tintAmt: 0.06});
      if (f < Bc + 18) out.push(droplet((ff) => orderPos(ff, Bc), f, lerp(80, 58, prog(f, Bc - 10, Bc + 14)), {tint: G, tintAmt: 0.6, k: 40}, 0.015));
      const grow = easeOut(prog(f, Bc + 6, Bc + 44));
      if (f >= Bc + 6) {
        const right = lerp(LIQ_L + 110, LIQ_R, grow);
        out.push({x: (LIQ_L + right) / 2, y: TUBE.y + Math.sin(f * 0.08) * 1.5, w: (right - LIQ_L) / 2, h: 60, r: 60, k: 30, tint: G, tintAmt: 0.66, refr: 1.5});
      }
      if (f >= Tc - 2) {
        const r = lerp(18, 78, spr(f, Tc + 4, 11, 110));
        out.push(droplet((ff) => twoPos(ff, Tc), f, r, {tint: AMB, tintAmt: 0.68, k: 44, refr: 1.4}, 0.018));
      }
    }
    return out;
  },
  Overlay: ({c}) => {
    const {f} = c;
    const {S, Th, K, Bc, Tc, Tw} = cues(c);
    const n = Math.max(1, Math.round(1000 * easeIn(prog(f, S, Th + 8))));
    const col = prog(f, K, K + 26);
    const partA = 1 - prog(f, Bc - 14, Bc);
    const pop = spr(f, K + 12, 10, 190);
    const [tx, ty] = twoPos(f, Tc);
    const ter = spr(f, Tc, 14, 150);
    return (
      <>
        <SlabText f={f} num="02" title="COSTI" color={C.amber} y={SLAB.y} hideAt={S - 22} />
        {f >= S && partA > 0 && (
          <div style={{position: 'absolute', inset: 0, opacity: partA}}>
            <div style={{position: 'absolute', top: 560, width: '100%', textAlign: 'center'}}>
              <div
                style={{
                  fontFamily: FONT,
                  fontWeight: 900,
                  fontSize: 124,
                  lineHeight: 1,
                  color: col > 0.5 ? C.green : C.amber,
                  fontVariantNumeric: 'tabular-nums',
                  transform: `scale(${col > 0.5 ? 0.8 + 0.2 * pop : 1})`,
                  textShadow: `0 0 40px ${col > 0.5 ? 'rgba(52,211,153,0.45)' : 'rgba(251,191,36,0.4)'}`,
                }}
              >
                × {col > 0.5 ? '1' : fmtInt(n)}
              </div>
              <Label size={28} color={C.text} style={{marginTop: 14}}>
                {col > 0.5 ? 'ordine con l’ETF' : 'commissioni, azione per azione'}
              </Label>
            </div>
            {col > 0.7 && (
              <Label size={24} color={C.ink} style={{position: 'absolute', top: BASE - 15, width: '100%', textAlign: 'center', opacity: prog(f, K + 20, K + 30)}}>
                1 ordine
              </Label>
            )}
          </div>
        )}
        {f >= Bc + 24 && (
          <div
            style={{
              position: 'absolute',
              left: LIQ_L + 40,
              top: TUBE.y - 30,
              fontFamily: FONT,
              fontWeight: 900,
              fontSize: 46,
              lineHeight: '60px',
              color: C.ink,
              opacity: prog(f, Bc + 24, Bc + 36),
            }}
          >
            1.000 € investiti
          </div>
        )}
        {f >= Tc + 10 && (
          <div
            style={{
              position: 'absolute',
              left: tx - 80,
              top: ty - 30,
              width: 160,
              textAlign: 'center',
              fontFamily: FONT,
              fontWeight: 900,
              fontSize: 46,
              lineHeight: '60px',
              color: '#1A1203',
              opacity: prog(f, Tc + 16, Tc + 28),
            }}
          >
            2 €
          </div>
        )}
        {f >= Tc - 2 && (
          <div style={{position: 'absolute', left: 100, top: 1078, opacity: Math.min(1, ter * 1.4), transform: `translateY(${(1 - ter) * 40}px)`}}>
            <div style={{fontFamily: FONT, fontWeight: 900, fontSize: 132, lineHeight: 1, color: C.amber, textShadow: '0 0 40px rgba(251,191,36,0.35)'}}>0,2%</div>
            <Label size={28} color={C.text} style={{marginTop: 10}}>
              costo all’anno
            </Label>
            <div style={{marginTop: 30, fontFamily: FONT, fontWeight: 700, fontSize: 40, color: C.text, opacity: prog(f, Tw, Tw + 14)}}>≈ 2 € ogni 1.000 €</div>
          </div>
        )}
        <div
          style={{
            position: 'absolute',
            top: 1430,
            left: 90,
            right: 90,
            textAlign: 'center',
            fontFamily: FONT,
            fontWeight: 500,
            fontSize: 24,
            lineHeight: 1.4,
            color: C.dim,
            opacity: prog(f, Tc, Tc + 20),
          }}
        >
          Costo annuo (TER) indicativo: varia da ETF a ETF.
          <br />
          Le commissioni di acquisto dipendono dal broker.
        </div>
      </>
    );
  },
};
