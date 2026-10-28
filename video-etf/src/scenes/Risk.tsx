import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame} from 'remotion';
import {FPS} from '../script';
import type {Clock} from '../components/SceneWrap';
import {Label, LineChart, noisy} from '../components/Primitives';
import {C, FONT, easeInOut, ramp} from '../theme';

const N = 120;
const PEAK = 60;
const TROUGH = 90;
// Mercato: sale, poi scende. Nessuna promessa di recupero.
const MARKET = noisy(N, 2.2, 1.6, (i) => {
  if (i <= PEAK) return 18 * easeInOut(i / PEAK);
  if (i <= TROUGH) return 18 - 30 * easeInOut((i - PEAK) / (TROUGH - PEAK));
  return -12 + 4 * easeInOut((i - TROUGH) / (N - 1 - TROUGH));
});
const VMIN = -20;
const VMAX = 26;
const CX = 80;
const CY = 820;
const CW = 920;
const CH = 470;
const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;

export const RiskScene: React.FC<{clock: Clock}> = ({clock}) => {
  const f = useCurrentFrame();
  const Wn = clock.cue('warn');
  const Fl = clock.cue('fall');

  const pop = spring({frame: f - Wn, fps: FPS, config: {damping: 10, stiffness: 170}});
  const wiggle = f > Wn ? 9 * Math.exp(-(f - Wn) / 12) * Math.sin((f - Wn) / 2.1) : 0;
  const reveal = interpolate(f, [4, Fl, Fl + 70, clock.total], [0, PEAK, TROUGH + 4, N - 1], clamp);
  const chartOn = ramp(f, 0, 18);

  const i = Math.min(N - 1, Math.floor(reveal));
  const hx = CX + (reveal / (N - 1)) * CW;
  const hy = CY + CH - ((MARKET[i] - VMIN) / (VMAX - VMIN)) * CH;
  const troughX = CX + (TROUGH / (N - 1)) * CW;
  const troughY = CY + CH - ((MARKET[TROUGH] - VMIN) / (VMAX - VMIN)) * CH;
  const note = ramp(f, Fl + 46, Fl + 62);

  return (
    <AbsoluteFill>
      <div
        style={{
          position: 'absolute',
          left: 540 - 85,
          top: 560,
          width: 170,
          height: 170,
          transform: `scale(${pop}) rotate(${wiggle}deg)`,
          opacity: Math.min(1, pop * 2),
        }}
      >
        <svg width={170} height={170} viewBox="0 0 100 100">
          <path d="M50 8 L94 88 Q96 92 91 92 L9 92 Q4 92 6 88 Z" fill={C.amber} stroke={C.amber} strokeWidth={4} strokeLinejoin="round" />
          <rect x={45} y={34} width={10} height={32} rx={5} fill="#1A1203" />
          <circle cx={50} cy={78} r={6} fill="#1A1203" />
        </svg>
      </div>

      <div style={{opacity: chartOn}}>
        <Label style={{position: 'absolute', left: CX, top: CY - 50}}>Mercato</Label>
        <LineChart x={CX} y={CY} w={CW} h={CH} series={MARKET} vmin={VMIN} vmax={VMAX} reveal={reveal} redFrom={PEAK} color={C.green} />
        <div
          style={{
            position: 'absolute',
            left: hx - 44,
            top: hy - 78,
            width: 88,
            padding: '6px 0',
            borderRadius: 12,
            background: reveal > PEAK ? C.red : C.green,
            textAlign: 'center',
            fontFamily: FONT,
            fontWeight: 900,
            fontSize: 26,
            color: C.ink,
          }}
        >
          ETF
        </div>
      </div>

      {note > 0 && (
        <div
          style={{
            position: 'absolute',
            left: troughX - 230,
            top: troughY + 44,
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
    </AbsoluteFill>
  );
};
