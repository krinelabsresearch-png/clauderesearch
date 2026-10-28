// Scena 7: "Salva" si riempie di liquido, "Condividi" lancia un aeroplanino con
// una scia di gocce. Alla fine tutto si fonde nella goccia del primo fotogramma.
import React from 'react';
import type {Shape} from '../glass/renderer';
import type {SceneDef} from '../world';
import {Label} from '../../components/Primitives';
import {C, FONT} from '../../theme';
import {BLU, G, WHITE, droplet, easeIn, easeInOut, lerp, mixRGB, prog, spr, type Ctx} from '../kit';
import {DROP, dropletRest} from './Hook';

const L = {x: 320, y: 880};
const R = {x: 760, y: 880};
const HALF = 118;

const cues = (c: Ctx) => ({Sv: c.cue('save'), Sd: c.cue('send'), end: c.total - 1});

const planePos = (f: number, Sd: number): [number, number] => {
  const u = easeIn(prog(f, Sd + 2, Sd + 36));
  return [R.x + u * 420, R.y - u * 460 + Math.sin(u * Math.PI) * 60];
};

/** Interpola una forma verso la goccia finale (identica al primo fotogramma del video). */
const toDrop = (s: Shape, c: number): Shape => {
  const d = dropletRest(0);
  return {
    ...s,
    x: lerp(s.x, d.x, c),
    y: lerp(s.y, d.y, c),
    w: lerp(s.w, d.w, c),
    h: lerp(s.h ?? s.w, d.h ?? d.w, c),
    r: lerp(s.r ?? 0, d.r ?? 0, c),
    // fusione forte a metà strada, nulla alla fine: due cerchi identici con k > 0
    // risulterebbero più grandi della goccia singola e il loop "scatterebbe"
    k: lerp(s.k ?? 0, 120, Math.sin(Math.PI * c)) * (1 - c),
    tint: mixRGB(s.tint ?? WHITE, d.tint!, c),
    tintAmt: lerp(s.tintAmt ?? 0, d.tintAmt ?? 0, c),
    fill: lerp(s.fill ?? 0, 0, c),
    refr: lerp(s.refr ?? 1, d.refr ?? 1, c),
    frost: lerp(s.frost ?? 0, 0, c),
  };
};

export const cta: SceneDef = {
  ringFrom: [540, 880],
  shapes: (c) => {
    const {f} = c;
    const {Sv, Sd, end} = cues(c);
    const app = spr(f, 2, 13, 140);
    const col = easeInOut(prog(f, end - 64, end - 6));
    const fill = easeInOut(prog(f, Sv + 4, Sv + 44));
    const glow = prog(f, Sd, Sd + 10) * (1 - prog(f, Sd + 50, Sd + 70));
    const left: Shape = {x: L.x, y: L.y, w: HALF * app, h: HALF * app, r: 62 * app, k: 20, tint: mixRGB(WHITE, G, fill), tintAmt: 0.08 + 0.42 * fill, fill, wave: 7, frost: 0.2, refr: 1.2};
    const right: Shape = {x: R.x, y: R.y, w: HALF * app, h: HALF * app, r: 62 * app, k: 20, tint: mixRGB(WHITE, BLU, glow), tintAmt: 0.08 + 0.4 * glow, frost: 0.2, refr: 1.2};
    if (col >= 1) return [dropletRest(0)];
    const out: Shape[] = [toDrop(left, col), toDrop(right, col)];
    if (f >= Sd && f < Sd + 46) {
      for (let j = 1; j <= 6; j++) {
        const sc = 1 - prog(f, Sd + j * 3, Sd + 40);
        if (sc > 0.02) out.push(droplet((ff) => planePos(ff - j * 3, Sd), f, (18 - j * 2) * sc, {tint: BLU, tintAmt: 0.5, k: 16}, 0.03));
      }
    }
    return out;
  },
  Overlay: ({c}) => {
    const {f} = c;
    const {Sv, Sd, end} = cues(c);
    const app = spr(f, 2, 13, 140);
    const col = easeInOut(prog(f, end - 64, end - 6));
    const fill = easeInOut(prog(f, Sv + 4, Sv + 44));
    const pop = spr(f, Sv + 4, 9, 200);
    const [px, py] = planePos(f, Sd);
    const back = spr(f, Sd + 40, 12, 160);
    const glow = prog(f, Sd, Sd + 10) * (1 - prog(f, Sd + 50, Sd + 70));
    const fade = 1 - prog(f, end - 70, end - 40);
    const move = (x: number) => lerp(x, DROP.x, col) - x;
    return (
      <div style={{position: 'absolute', inset: 0, opacity: fade}}>
        <div style={{position: 'absolute', inset: 0, transform: `translateX(${move(L.x)}px)`}}>
          <svg
            width={110}
            height={130}
            viewBox="0 0 24 28"
            style={{position: 'absolute', left: L.x - 55, top: L.y - 65, transform: `scale(${app * (1 + 0.1 * pop * (1 - fill * 0.5))})`}}
          >
            <path d="M3 2 H21 V26 L12 19.5 L3 26 Z" fill={fill > 0.5 ? '#fff' : 'none'} stroke="#fff" strokeWidth={1.8} strokeLinejoin="round" />
          </svg>
          <Label size={28} color={fill > 0.5 ? C.green : C.text} style={{position: 'absolute', top: L.y + 140, left: L.x - 150, width: 300, textAlign: 'center', opacity: app}}>
            Salva
          </Label>
        </div>
        <div style={{position: 'absolute', inset: 0, transform: `translateX(${move(R.x)}px)`}}>
          <svg
            width={120}
            height={120}
            viewBox="0 0 24 24"
            style={{
              position: 'absolute',
              left: (f < Sd + 40 ? px : R.x) - 60,
              top: (f < Sd + 40 ? py : R.y) - 60,
              transform: `scale(${f < Sd + 40 ? app * (1 - prog(f, Sd + 2, Sd + 36) * 0.5) : back}) rotate(${f < Sd + 40 ? -prog(f, Sd + 2, Sd + 36) * 20 : 0}deg)`,
              opacity: f < Sd + 40 ? 1 - prog(f, Sd + 26, Sd + 38) : 1,
            }}
          >
            <path d="M22 2 L11 13" stroke="#fff" strokeWidth={1.8} strokeLinecap="round" />
            <path d="M22 2 L15 22 L11 13 L2 9 Z" fill={glow > 0.2 ? '#fff' : 'none'} stroke="#fff" strokeWidth={1.8} strokeLinejoin="round" />
          </svg>
          <Label size={28} color={glow > 0.2 ? C.blue : C.text} style={{position: 'absolute', top: R.y + 140, left: R.x - 150, width: 300, textAlign: 'center', opacity: app}}>
            Condividi
          </Label>
        </div>
        <div
          style={{
            position: 'absolute',
            top: 1330,
            left: 110,
            right: 110,
            textAlign: 'center',
            fontFamily: FONT,
            fontWeight: 500,
            fontSize: 26,
            lineHeight: 1.45,
            color: C.dim,
            opacity: prog(f, 10, 30),
          }}
        >
          Contenuto informativo, non è consulenza finanziaria.
          <br />
          Investire comporta rischi, anche di perdita del capitale.
        </div>
      </div>
    );
  },
};
