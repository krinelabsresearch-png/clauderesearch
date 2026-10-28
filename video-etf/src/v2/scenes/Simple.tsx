// Scena 5: una lente d'ingrandimento di vetro (ingrandimento vero dello sfondo)
// salta tra le aziende, poi si trasforma nella cornice di tutto il mercato.
import React from 'react';
import type {Shape} from '../glass/renderer';
import type {SceneDef} from '../world';
import {Label} from '../../components/Primitives';
import {C, FONT} from '../../theme';
import {BLU, G, droplet, easeInOut, lerp, mixRGB, prog, spr, type Ctx} from '../kit';
import {SlabText, slabShape} from './common';

const SLAB = {x: 540, y: 900, w: 330, h: 140};
const COLS = 8;
const ROWS = 6;
const CELL = 114;
const SIZE = 96;
const X0 = (1080 - COLS * CELL) / 2;
const Y0 = 620;
const GW = COLS * CELL;
const GH = ROWS * CELL;
const TARGETS = [9, 30, 20, 43, 13];
const HOP = 24;
const LENS = 84;

const cues = (c: Ctx) => ({Sc: c.cue('scan'), M: c.cue('market')});
const center = (i: number): [number, number] => [X0 + (i % COLS) * CELL + CELL / 2, Y0 + Math.floor(i / COLS) * CELL + CELL / 2];

const lensPos = (f: number, Sc: number): [number, number] => {
  const k = Math.max(0, (f - Sc) / HOP);
  const idx = Math.min(TARGETS.length - 1, Math.floor(k));
  const nxt = Math.min(TARGETS.length - 1, idx + 1);
  const t = easeInOut(Math.min(1, Math.max(0, (k - idx) * 1.6 - 0.6)));
  const a = center(TARGETS[idx]);
  const b = center(TARGETS[nxt]);
  return [lerp(a[0], b[0], t), lerp(a[1], b[1], t) - Math.sin(t * Math.PI) * 40];
};

const focusTile = (f: number, Sc: number) => {
  const k = Math.max(0, (f - Sc) / HOP);
  const idx = Math.min(TARGETS.length - 1, Math.floor(k));
  const t = (k - idx) * 1.6 - 0.6;
  return t > 0.5 ? TARGETS[Math.min(TARGETS.length - 1, idx + 1)] : TARGETS[idx];
};

export const simple: SceneDef = {
  ringFrom: [540, 960],
  shapes: (c) => {
    const {f} = c;
    const {Sc, M} = cues(c);
    const out: Shape[] = [];
    const morph = easeInOut(prog(f, M, M + 28));
    if (f < Sc) {
      const s = slabShape(f, SLAB, BLU);
      const u = easeInOut(prog(f, Sc - 20, Sc));
      const [lx, ly] = center(TARGETS[0]);
      out.push({...s, x: lerp(s.x, lx, u), y: lerp(s.y, ly, u), w: lerp(s.w, LENS, u), h: lerp(s.h ?? s.w, LENS, u), r: lerp(s.r ?? 0, LENS, u), mag: 0.55 * u, refr: lerp(1.3, 1.8, u)});
    } else if (morph < 1) {
      const d = droplet((ff) => lensPos(ff, Sc), f, LENS * (1 - morph), {tint: BLU, tintAmt: 0.1, mag: 0.55 * (1 - morph), refr: 1.8, k: 60}, 0.005);
      out.push(d);
    }
    if (morph > 0) {
      const s = 0.6 + 0.4 * spr(f, M, 12, 120);
      out.push({x: 540, y: Y0 + GH / 2, w: (GW / 2 + 22) * s, h: (GH / 2 + 22) * s, r: 44, kind: 'shell', thick: 10 * morph, k: 60, tint: mixRGB(BLU, G, morph), tintAmt: 0.3});
    }
    return out;
  },
  extras: (c) => {
    const {f} = c;
    const {Sc, M} = cues(c);
    if (f < Sc - 30) return {};
    return {tiles: {x0: X0, y0: Y0, cell: CELL, size: SIZE * spr(f, Sc - 30, 14, 140), cols: COLS, rows: ROWS, lit: prog(f, M + 6, M + 46), side: 2}};
  },
  Overlay: ({c}) => {
    const {f} = c;
    const {Sc, M} = cues(c);
    const lit = prog(f, M + 6, M + 46);
    const focus = f >= Sc && f < M ? focusTile(f, Sc) : -1;
    const show = prog(f, Sc - 20, Sc);
    return (
      <>
        <SlabText f={f} num="03" title="SEMPLICITÀ" color={C.blue} y={SLAB.y} hideAt={Sc - 26} />
        {show > 0 &&
          Array.from({length: COLS * ROWS}, (_, i) => {
            const [x, y] = center(i);
            const col = i % COLS;
            const row = Math.floor(i / COLS);
            const w = Math.min(1, Math.max(0, lit * 1.7 - (col + row) / (COLS + ROWS)));
            if (w >= 1) return null;
            const isF = i === focus;
            return (
              <div
                key={i}
                style={{
                  position: 'absolute',
                  left: x - 50,
                  top: y - 40,
                  width: 100,
                  height: 80,
                  textAlign: 'center',
                  fontFamily: FONT,
                  fontWeight: 900,
                  fontSize: isF ? 66 : 38,
                  lineHeight: '80px',
                  color: isF ? C.blue : 'rgba(255,255,255,0.28)',
                  opacity: show * (1 - w),
                  textShadow: isF ? '0 0 24px rgba(96,165,250,0.8)' : undefined,
                }}
              >
                ?
              </div>
            );
          })}
        <Label
          size={34}
          color={C.green}
          style={{
            position: 'absolute',
            top: Y0 + GH + 64,
            width: '100%',
            textAlign: 'center',
            letterSpacing: '0.12em',
            opacity: prog(f, M + 26, M + 42),
            transform: `translateY(${(1 - prog(f, M + 26, M + 42)) * 18}px)`,
          }}
        >
          Indice = l’intero mercato
        </Label>
      </>
    );
  },
};
