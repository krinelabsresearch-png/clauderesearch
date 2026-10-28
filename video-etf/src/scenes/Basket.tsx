import React from 'react';
import {AbsoluteFill, spring, useCurrentFrame} from 'remotion';
import {FPS} from '../script';
import type {Clock} from '../components/SceneWrap';
import {CompanyTile, Label, SECTOR} from '../components/Primitives';
import {C, FONT, easeOut, hash, lerp, ramp} from '../theme';

const BX = 540;
const BW = 700;
const BH = 520;
const BTOP = 930;
const PLATE = 118;
const T = 86;
const PITCH = 100;

// Punti del globo distribuiti uniformemente (spirale di Fibonacci).
const GLOBE = Array.from({length: 560}, (_, i) => {
  const y = 1 - (i / 559) * 2;
  const r = Math.sqrt(1 - y * y);
  const th = i * 2.39996;
  return {x: Math.cos(th) * r, y, z: Math.sin(th) * r, lit: hash(i * 7.7) < 0.2, d: hash(i * 3.3)};
});

export const BasketScene: React.FC<{clock: Clock}> = ({clock}) => {
  const f = useCurrentFrame();
  const D = clock.cue('drop');
  const I = clock.cue('indice');
  const Gb = clock.cue('globe');

  const box = spring({frame: f - 2, fps: FPS, config: {damping: 16, stiffness: 120}});

  const tiles = Array.from({length: 24}, (_, k) => {
    const row = Math.floor(k / 6); // 0 = fila in basso
    const col = (k * 4 + row) % 6;
    const h = hash(k + 40);
    const xl = BX - (6 * PITCH - (PITCH - T)) / 2 + col * PITCH + (h - 0.5) * 8;
    // Le file si impilano sopra la targa frontale, così restano tutte visibili.
    const yl = BTOP + BH - PLATE - 10 - T - row * (T + 8);
    const t0 = D - 6 + k * 3.6;
    const tl = t0 + 20;
    if (f < t0) return null;
    let y: number;
    let x: number;
    let rot: number;
    if (f < tl) {
      const u = (f - t0) / 20;
      y = lerp(-160 - h * 220, yl, u * u);
      x = lerp(xl + (hash(k + 90) - 0.5) * 220, xl, easeOut(u));
      rot = lerp((h - 0.5) * 80, (h - 0.5) * 6, easeOut(u));
    } else {
      const dt = f - tl;
      // Rimbalzo smorzato all'atterraggio.
      y = yl - 34 * Math.exp(-dt / 6) * Math.abs(Math.sin(dt / 3.4));
      x = xl;
      rot = (h - 0.5) * 6;
    }
    return (
      <CompanyTile
        key={k}
        size={T}
        color={SECTOR[k % SECTOR.length]}
        kind={k}
        style={{position: 'absolute', left: x, top: y, transform: `rotate(${rot}deg)`}}
      />
    );
  });

  // Cartellino "INDICE" che oscilla come un pendolo.
  const tagOn = f >= I - 2;
  const dt = Math.max(0, f - I);
  const swing = 38 * Math.exp(-dt / 16) * Math.cos(dt / 5.2);
  const tagP = ramp(f, I - 2, I + 6);

  const globeP = spring({frame: f - Gb, fps: FPS, config: {damping: 18, stiffness: 90}});
  const ang = f * 0.012;
  const tiltX = 0.38;
  const R = 230;
  const gx = 540;
  const gy = 690;
  const pts = f >= Gb - 2
    ? GLOBE.map((p, i) => {
        const x1 = p.x * Math.cos(ang) + p.z * Math.sin(ang);
        const z1 = -p.x * Math.sin(ang) + p.z * Math.cos(ang);
        const y2 = p.y * Math.cos(tiltX) - z1 * Math.sin(tiltX);
        const z2 = p.y * Math.sin(tiltX) + z1 * Math.cos(tiltX);
        const front = z2 > 0;
        const lit = p.lit ? ramp(f, Gb + 8 + p.d * 40, Gb + 20 + p.d * 40) : 0;
        return {i, sx: gx + R * x1, sy: gy + R * y2, z: z2, front, lit};
      }).sort((a, b) => a.z - b.z)
    : [];

  return (
    <AbsoluteFill>
      {pts.length > 0 && (
        <svg width={1080} height={1920} style={{position: 'absolute', inset: 0, opacity: globeP, transform: `scale(${0.7 + 0.3 * globeP})`, transformOrigin: `${gx}px ${gy}px`}}>
          <defs>
            <radialGradient id="atm">
              <stop offset="0.7" stopColor={C.green} stopOpacity="0" />
              <stop offset="0.92" stopColor={C.green} stopOpacity="0.16" />
              <stop offset="1" stopColor={C.green} stopOpacity="0" />
            </radialGradient>
          </defs>
          <circle cx={gx} cy={gy} r={R * 1.12} fill="url(#atm)" />
          <circle cx={gx} cy={gy} r={R} fill="rgba(10,18,30,0.65)" stroke="rgba(255,255,255,0.08)" strokeWidth={2} />
          {pts.map((p) => {
            const depth = (p.z + 1) / 2;
            if (p.lit > 0 && p.front) {
              return (
                <g key={p.i}>
                  <circle cx={p.sx} cy={p.sy} r={9 * p.lit} fill={C.green} opacity={0.25 * p.lit} />
                  <circle cx={p.sx} cy={p.sy} r={3.2 + 1.8 * p.lit} fill={C.green} />
                </g>
              );
            }
            return <circle key={p.i} cx={p.sx} cy={p.sy} r={p.front ? 2.8 : 1.8} fill="#9FB3C8" opacity={p.front ? 0.25 + 0.45 * depth : 0.1} />;
          })}
        </svg>
      )}

      <div style={{position: 'absolute', inset: 0, opacity: box, transform: `translateY(${(1 - box) * 140}px)`}}>
        <div
          style={{
            position: 'absolute',
            left: BX - BW / 2,
            top: BTOP,
            width: BW,
            height: BH,
            borderRadius: '0 0 44px 44px',
            background: 'linear-gradient(180deg, rgba(255,255,255,0.02), rgba(52,211,153,0.07))',
          }}
        />
        {tiles}
        <svg width={BW + 20} height={BH + 20} style={{position: 'absolute', left: BX - BW / 2 - 10, top: BTOP - 10}}>
          <path
            d={`M10 10 L10 ${BH - 34} Q10 ${BH + 10} 54 ${BH + 10} L${BW - 34} ${BH + 10} Q${BW + 10} ${BH + 10} ${BW + 10} ${BH - 34} L${BW + 10} 10`}
            fill="none"
            stroke="rgba(255,255,255,0.4)"
            strokeWidth={5}
            strokeLinecap="round"
          />
        </svg>
        <div
          style={{
            position: 'absolute',
            left: BX - BW / 2 + 2,
            top: BTOP + BH - PLATE,
            width: BW - 4,
            height: PLATE + 2,
            borderRadius: '0 0 42px 42px',
            background: 'linear-gradient(180deg, rgba(8,14,22,0.55), rgba(8,14,22,0.92))',
            borderTop: '1.5px solid rgba(255,255,255,0.14)',
            backdropFilter: 'blur(6px)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: 22,
          }}
        >
          <span style={{fontFamily: FONT, fontWeight: 900, fontSize: 64, letterSpacing: '0.18em', color: C.green}}>ETF</span>
          <Label size={24}>1 solo acquisto</Label>
        </div>
      </div>

      {tagOn && (
        <div
          style={{
            position: 'absolute',
            left: 858,
            top: BTOP - 14,
            transformOrigin: '0px 0px',
            transform: `rotate(${swing}deg)`,
            opacity: tagP,
          }}
        >
          <svg width={30} height={80} style={{position: 'absolute', left: -15, top: 0}}>
            <circle cx={15} cy={6} r={6} fill={C.text} />
            <line x1={15} x2={15} y1={6} y2={80} stroke={C.text} strokeWidth={2.5} />
          </svg>
          <div
            style={{
              position: 'absolute',
              left: -92,
              top: 76,
              width: 184,
              padding: '18px 18px 16px',
              borderRadius: 18,
              background: C.text,
              boxShadow: '0 20px 40px rgba(0,0,0,0.5)',
            }}
          >
            <div style={{fontFamily: FONT, fontWeight: 900, fontSize: 32, letterSpacing: '0.1em', color: '#0B1220'}}>INDICE</div>
            {[0.9, 0.7, 0.8].map((w, i) => (
              <div key={i} style={{height: 8, width: `${w * 100}%`, borderRadius: 4, background: '#0B122033', marginTop: 10}} />
            ))}
          </div>
        </div>
      )}
    </AbsoluteFill>
  );
};
