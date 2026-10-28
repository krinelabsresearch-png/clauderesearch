import React from 'react';
import {AbsoluteFill, spring, useCurrentFrame} from 'remotion';
import {FPS} from '../script';
import type {Clock} from '../components/SceneWrap';
import {Label} from '../components/Primitives';
import {C, FONT, easeIn, easeInOut, fmtInt, hash, lerp, mix, ramp} from '../theme';

const COLS = 32;
const CELL = 26;
const TILE = 20;
const GW = COLS * CELL;
const OX = (1080 - GW) / 2;
const OY = 990 - GW / 2;
export const CENTER_Y = 990;
export const HERO = 150;

/** Scala del quadrato iniziale: usata anche dall'ultima scena per chiudere il loop. */
export const heroScale = (f: number) => spring({frame: f + 8, fps: FPS, config: {damping: 12, stiffness: 110}});

// Lettere "pixel" (1 pixel = 2×2 tessere della griglia).
const BITMAPS: string[][] = [
  ['####', '#...', '#...', '###.', '#...', '#...', '####'],
  ['#####', '..#..', '..#..', '..#..', '..#..', '..#..', '..#..'],
  ['####', '#...', '#...', '###.', '#...', '#...', '#...'],
];
const MASK = new Set<number>();
{
  let c0 = 1;
  for (const bm of BITMAPS) {
    bm.forEach((row, y) =>
      [...row].forEach((ch, x) => {
        if (ch !== '#') return;
        for (const dx of [0, 1]) for (const dy of [0, 1]) MASK.add((9 + 2 * y + dy) * COLS + c0 + 2 * x + dx);
      }),
    );
    c0 += bm[0].length * 2 + 2;
  }
}

const BASE = ['#22324A', '#263B57', '#21403F', '#2E2F4A', '#2A3647', '#1F3A4F'];
const OWN = '#1E7A5C';

const CANDLES = (() => {
  let p = 50;
  return Array.from({length: 18}, (_, i) => {
    const o = p;
    p += (hash(i * 3.1) - 0.38) * 14;
    const c = p;
    return {o, c, hi: Math.max(o, c) + hash(i * 5.7) * 6, lo: Math.min(o, c) - hash(i * 7.3) * 6};
  });
})();

export const HookScene: React.FC<{clock: Clock}> = ({clock}) => {
  const f = useCurrentFrame();
  const G = clock.cue('grid');
  const M = clock.cue('mille');
  const E = clock.cue('etf');
  const B = clock.cue('borsa');
  const A = clock.cue('azione');

  const hs = heroScale(f);
  const shrink = ramp(f, G - 4, G + 14, easeInOut);
  const heroSize = lerp(HERO * hs, TILE, shrink);
  const heroOpacity = 1 - ramp(f, G + 12, G + 20);

  const tilt = ramp(f, G, G + 90, easeInOut) * (1 - ramp(f, E, E + 36, easeInOut));
  const zoom = 1 + 0.05 * ramp(f, G, E, easeInOut);

  const count = ramp(f, G + 6, M + 46, easeInOut);
  const counterOn = ramp(f, G + 8, G + 20) * (1 - ramp(f, E, E + 12));
  const n = Math.round(lerp(1, 1000, count));

  const tiles: React.ReactNode[] = [];
  if (f >= G) {
    for (let i = 0; i < COLS * COLS; i++) {
      const c = i % COLS;
      const r = Math.floor(i / COLS);
      const d = Math.hypot(c - 15.5, r - 15.5);
      const h = hash(i);
      const appear = ramp(f, G + 4 + d * 1.25 + h * 5, G + 20 + d * 1.25 + h * 5);
      if (appear <= 0) continue;
      const own = ramp(f, M + d * 1.1, M + 12 + d * 1.1);
      const inMask = MASK.has(i);
      const etf = inMask ? ramp(f, E + c * 0.7, E + 16 + c * 0.7) : 0;
      const fade = inMask ? 0 : ramp(f, E + h * 16, E + 14 + h * 16, easeIn);
      let color = mix(BASE[Math.floor(h * BASE.length)], OWN, own * (0.55 + 0.45 * hash(i * 9.1)));
      if (etf > 0) color = mix(OWN, C.green, etf);
      tiles.push(
        <div
          key={i}
          style={{
            position: 'absolute',
            left: c * CELL,
            top: r * CELL,
            width: TILE,
            height: TILE,
            borderRadius: 5,
            background: color,
            opacity: appear * (1 - fade * 0.94),
            transform: `translateY(${fade * 36}px) scale(${(0.3 + 0.7 * appear) * (1 + 0.12 * etf)})`,
            boxShadow: etf > 0 ? `0 0 ${18 * etf}px rgba(52,211,153,${0.6 * etf})` : undefined,
          }}
        />,
      );
    }
  }

  const rings = f < G ? [0, 26] : [];
  const etfLabel = ramp(f, E + 34, E + 62, easeInOut);
  const chip = spring({frame: f - B, fps: FPS, config: {damping: 14, stiffness: 160}});
  const candlesOn = f >= A - 4;

  return (
    <AbsoluteFill>
      <div
        style={{
          position: 'absolute',
          left: OX,
          top: OY,
          width: GW,
          height: GW,
          transform: `perspective(1800px) rotateX(${28 * tilt}deg) rotateZ(${-8 * tilt}deg) scale(${zoom})`,
        }}
      >
        {tiles}
      </div>

      {rings.map((k) => {
        const p = (((f - k) % 66) + 66) % 66 / 66;
        if (f < k + 4) return null;
        const rad = 80 + 280 * p;
        return (
          <div
            key={k}
            style={{
              position: 'absolute',
              left: 540 - rad,
              top: CENTER_Y - rad,
              width: rad * 2,
              height: rad * 2,
              borderRadius: '50%',
              border: `3px solid ${C.green}`,
              opacity: (1 - p) * 0.4 * (1 - shrink),
            }}
          />
        );
      })}

      {heroOpacity > 0 && (
        <div
          style={{
            position: 'absolute',
            left: 540 - heroSize / 2,
            top: CENTER_Y - heroSize / 2,
            width: heroSize,
            height: heroSize,
            borderRadius: heroSize * 0.24,
            background: `linear-gradient(145deg, #6EE7B7, ${C.green} 45%, #059669)`,
            boxShadow: `0 0 ${80 * (1 - shrink)}px rgba(52,211,153,0.55), inset 0 3px 0 rgba(255,255,255,0.4)`,
            opacity: heroOpacity,
          }}
        />
      )}

      <Label
        size={30}
        color={C.text}
        style={{
          position: 'absolute',
          top: CENTER_Y + 120,
          width: '100%',
          textAlign: 'center',
          opacity: ramp(f, 8, 22) * (1 - ramp(f, G - 6, G + 6)),
          transform: `translateY(${(1 - ramp(f, 8, 22)) * 16}px)`,
        }}
      >
        1 acquisto
      </Label>

      {counterOn > 0 && (
        <div
          style={{
            position: 'absolute',
            top: 1428,
            width: '100%',
            display: 'flex',
            alignItems: 'baseline',
            justifyContent: 'center',
            gap: 18,
            opacity: counterOn,
          }}
        >
          <span style={{fontFamily: FONT, fontWeight: 900, fontSize: 76, color: C.green, fontVariantNumeric: 'tabular-nums'}}>
            {fmtInt(n)}
            {n >= 1000 ? '+' : ''}
          </span>
          <Label size={30} color={C.text}>
            aziende
          </Label>
        </div>
      )}

      {etfLabel > 0 && (
        <Label
          size={34}
          color={C.dim}
          style={{
            position: 'absolute',
            top: 1196,
            width: '100%',
            textAlign: 'center',
            letterSpacing: '0.32em',
            clipPath: `inset(0 ${(1 - etfLabel) * 100}% 0 0)`,
          }}
        >
          <span style={{color: C.green}}>E</span>xchange <span style={{color: C.green}}>T</span>raded{' '}
          <span style={{color: C.green}}>F</span>und
        </Label>
      )}

      {f >= B - 2 && (
        <div style={{position: 'absolute', top: 1262, width: '100%', display: 'flex', justifyContent: 'center'}}>
          <div
            style={{
              padding: '14px 30px',
              borderRadius: 999,
              border: `2px solid ${C.green}88`,
              background: `${C.green}18`,
              fontFamily: FONT,
              fontWeight: 700,
              fontSize: 38,
              color: C.text,
              opacity: Math.min(1, chip * 1.4),
              transform: `scale(${0.7 + 0.3 * chip})`,
            }}
          >
            = fondo quotato in borsa
          </div>
        </div>
      )}

      {candlesOn && (
        <svg width={560} height={120} style={{position: 'absolute', left: 260, top: 1352}}>
          {CANDLES.map((k, i) => {
            const p = ramp(f, A + i * 2.2, A + 12 + i * 2.2);
            const y = (v: number) => 110 - (v - 20) * 1.25;
            const up = k.c >= k.o;
            const col = up ? C.green : C.red;
            const top = y(Math.max(k.o, k.c));
            const bot = y(Math.min(k.o, k.c));
            const mid = (top + bot) / 2;
            const cx = 14 + i * 31;
            return (
              <g key={i} opacity={p} transform={`translate(0 ${mid}) scale(1 ${p}) translate(0 ${-mid})`}>
                <line x1={cx} x2={cx} y1={y(k.hi)} y2={y(k.lo)} stroke={col} strokeWidth={2.5} />
                <rect x={cx - 8} y={top} width={16} height={Math.max(4, bot - top)} rx={3} fill={col} />
              </g>
            );
          })}
        </svg>
      )}
    </AbsoluteFill>
  );
};
