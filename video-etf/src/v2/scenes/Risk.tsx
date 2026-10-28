// Scena 6: un triangolo di vetro avverte; una goccia "ETF" scivola lungo il
// grafico del mercato e, nel calo, lascia una scia liquida rossa.
import React from 'react';
import type {Shape} from '../glass/renderer';
import type {SceneDef} from '../world';
import {Label} from '../../components/Primitives';
import {C, FONT} from '../../theme';
import {AMB, G, RED, droplet, easeInOut, lerp, mixRGB, prog, spr, type Ctx} from '../kit';

const N = 48;
const X0 = 90;
const X1 = 990;
const PEAK = 24;
const TROUGH = 37;
const noise = (i: number) => Math.sin(i * 1.1) * 0.9 + Math.sin(i * 0.43 + 1) * 0.7;
// Il mercato sale e poi scende. Nessun recupero promesso.
const value = (i: number) => {
  if (i <= PEAK) return 18 * easeInOut(i / PEAK) + noise(i);
  if (i <= TROUGH) return 18 - 30 * easeInOut((i - PEAK) / (TROUGH - PEAK)) + noise(i) * 0.6;
  return -12 + 4 * easeInOut((i - TROUGH) / (N - 1 - TROUGH)) + noise(i) * 0.5;
};
const YS = Array.from({length: N}, (_, i) => 1090 - value(i) * 12);
const TRI = {x: 540, y: 640, r: 96};

const cues = (c: Ctx) => ({W: c.cue('warn'), Fl: c.cue('fall')});

const reveal = (f: number, Fl: number, total: number) => {
  if (f < Fl) return lerp(0, PEAK, prog(f, 8, Fl));
  if (f < Fl + 70) return lerp(PEAK, TROUGH + 1, easeInOut(prog(f, Fl, Fl + 70)));
  return lerp(TROUGH + 1, N - 1, prog(f, Fl + 70, total));
};

const curve = (u: number): [number, number] => {
  const i0 = Math.max(0, Math.min(N - 2, Math.floor(u)));
  const t = Math.min(1, Math.max(0, u - i0));
  return [X0 + (u / (N - 1)) * (X1 - X0), lerp(YS[i0], YS[i0 + 1], t)];
};

const beadPos = (f: number, Fl: number, total: number): [number, number] => {
  const [x, y] = curve(reveal(f, Fl, total));
  return [x, y - 34];
};

export const risk: SceneDef = {
  ringFrom: [540, 640],
  shapes: (c) => {
    const {f, total} = c;
    const {W, Fl} = cues(c);
    const out: Shape[] = [];
    const pop = spr(f, W - 2, 9, 170);
    const wig = f > W ? 0.18 * Math.exp(-(f - W) / 12) * Math.sin((f - W) / 2.2) : 0;
    if (pop > 0.01) out.push({x: TRI.x, y: TRI.y, w: TRI.r * pop, kind: 'tri', r: 18 * pop, rot: wig, tint: AMB, tintAmt: 0.62, refr: 1.3});
    const app = spr(f, 6, 13, 150);
    const falling = reveal(f, Fl, total) > PEAK;
    const tint = mixRGB(G, RED, prog(reveal(f, Fl, total), PEAK, PEAK + 2));
    out.push(droplet((ff) => beadPos(ff, Fl, total), f, 34 * app, {tint, tintAmt: 0.6, refr: 1.8, k: 26}, 0.05));
    if (falling) {
      for (let j = 1; j <= 4; j++) {
        const sc = (0.72 - j * 0.13) * prog(f, Fl + j * 2, Fl + j * 2 + 8) * (1 - prog(f, Fl + 80, Fl + 110));
        if (sc > 0.02) out.push(droplet((ff) => beadPos(ff - j * 4, Fl, total), f, 34 * sc, {tint: RED, tintAmt: 0.6, k: 26}, 0.05));
      }
    }
    return out;
  },
  extras: (c) => {
    const {f, total} = c;
    const {Fl} = cues(c);
    return {chart: {x0: X0, x1: X1, ys: YS, reveal: reveal(f, Fl, total) + 0.3, redFrom: PEAK, baseY: 1330, side: 2, alpha: prog(f, 0, 16)}};
  },
  Overlay: ({c}) => {
    const {f, total} = c;
    const {W, Fl} = cues(c);
    const pop = spr(f, W - 2, 9, 170);
    const wig = f > W ? 0.18 * Math.exp(-(f - W) / 12) * Math.sin((f - W) / 2.2) : 0;
    const [bx, by] = beadPos(f, Fl, total);
    const [tx, ty] = curve(TROUGH);
    const note = prog(f, Fl + 46, Fl + 62);
    return (
      <>
        <div
          style={{
            position: 'absolute',
            left: TRI.x - 60,
            top: TRI.y - 34,
            width: 120,
            textAlign: 'center',
            fontFamily: FONT,
            fontWeight: 900,
            fontSize: 92,
            lineHeight: '100px',
            color: '#1A1203',
            transform: `scale(${pop}) rotate(${wig}rad)`,
            transformOrigin: '60px 34px',
          }}
        >
          !
        </div>
        <Label style={{position: 'absolute', left: X0, top: 760, opacity: prog(f, 0, 16)}}>Mercato</Label>
        <div
          style={{
            position: 'absolute',
            left: bx - 40,
            top: by - 16,
            width: 80,
            textAlign: 'center',
            fontFamily: FONT,
            fontWeight: 900,
            fontSize: 24,
            lineHeight: '32px',
            color: C.text,
            opacity: prog(f, 10, 22),
            textShadow: '0 2px 8px rgba(0,0,0,0.6)',
          }}
        >
          ETF
        </div>
        {note > 0 && (
          <div
            style={{
              position: 'absolute',
              left: tx - 230,
              top: ty + 50,
              width: 460,
              textAlign: 'center',
              fontFamily: FONT,
              fontWeight: 800,
              fontSize: 36,
              color: C.red,
              opacity: note,
              transform: `translateY(${(1 - note) * 16}px)`,
            }}
          >
            il valore può scendere
          </div>
        )}
      </>
    );
  },
};
