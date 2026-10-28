import React from 'react';
import {AbsoluteFill, interpolate, spring, useCurrentFrame} from 'remotion';
import {FPS} from '../script';
import type {Clock} from '../components/SceneWrap';
import {Card, CompanyTile, Label, LineChart, TitleCard, noisy} from '../components/Primitives';
import {C, FONT, easeIn, fmtPct, mix, ramp} from '../theme';

const N = 100;
const CRASH_AT = 55;
const CRASH_LEN = 15;
const crashShape = (depth: number) => (i: number) =>
  i < CRASH_AT ? 0 : -depth * easeIn(Math.min(1, (i - CRASH_AT) / CRASH_LEN));
const SINGLE = noisy(N, 1.3, 1.4, crashShape(60));
// Stesso crollo dentro 1.000 aziende di pari peso: -60% × 1/1.000 = -0,06%.
const BASKET = noisy(N, 4.1, 1.4, crashShape(0.06));
const VMIN = -66;
const VMAX = 8;
const clamp = {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'} as const;

const RED_TILE = 612;

export const DiversScene: React.FC<{clock: Clock}> = ({clock}) => {
  const f = useCurrentFrame();
  const P = clock.cue('panels');
  const Cr = clock.cue('crash');
  const Ep = clock.cue('etfpanel');
  const O = clock.cue('onered');
  const Dp = clock.cue('dip');

  const topIn = spring({frame: f - P, fps: FPS, config: {damping: 17, stiffness: 120}});
  const botIn = spring({frame: f - P - 8, fps: FPS, config: {damping: 17, stiffness: 120}});
  const botFocus = ramp(f, Ep - 6, Ep + 10);

  const revTop = interpolate(f, [P, Cr, Cr + 46, Ep], [0, CRASH_AT, CRASH_AT + 22, N - 1], clamp);
  const revBot = interpolate(f, [Ep, O, O + 46, Dp + 40], [0, CRASH_AT, CRASH_AT + 22, N - 1], clamp);
  const crashTop = Math.min(1, Math.max(0, (revTop - CRASH_AT) / CRASH_LEN));
  const crashBot = Math.min(1, Math.max(0, (revBot - CRASH_AT) / CRASH_LEN));

  const hit = ramp(f, Cr, Cr + 8);
  const shake = f > Cr ? Math.sin((f - Cr) * 1.9) * 10 * Math.exp(-(f - Cr) / 12) : 0;
  const crack = ramp(f, Cr + 2, Cr + 14);

  const red = ramp(f, O, O + 10);
  const ring = spring({frame: f - O, fps: FPS, config: {damping: 12, stiffness: 140}});

  return (
    <AbsoluteFill>
      <TitleCard num="01" title="DIVERSIFICAZIONE" color={C.green} outAt={P - 16} />

      <div style={{opacity: topIn, transform: `translateX(${(1 - topIn) * -120}px)`}}>
        <Card x={60} y={590} w={960} h={400}>
          <Label style={{position: 'absolute', left: 40, top: 34}}>Una sola azione</Label>
          <div style={{position: 'absolute', right: 40, top: 22, textAlign: 'right'}}>
            <div style={{fontFamily: FONT, fontWeight: 900, fontSize: 64, color: crashTop > 0 ? C.red : C.text, fontVariantNumeric: 'tabular-nums'}}>
              {fmtPct(-60 * crashTop, 0)}
            </div>
          </div>
          <div style={{position: 'absolute', left: 46 + shake, top: 150}}>
            <CompanyTile size={170} color={mix('#3B82F6', '#EF4444', hit)} kind={4} />
            <svg width={170} height={170} style={{position: 'absolute', left: 0, top: 0}}>
              <path
                d="M92 0 L78 52 L104 78 L70 122 L88 170"
                fill="none"
                stroke="#0B1220"
                strokeWidth={6}
                strokeLinejoin="round"
                pathLength={1}
                strokeDasharray="1"
                strokeDashoffset={1 - crack}
              />
            </svg>
          </div>
          <LineChart x={270} y={120} w={640} h={240} series={SINGLE} vmin={VMIN} vmax={VMAX} reveal={revTop} redFrom={CRASH_AT} color={C.blue} />
        </Card>
      </div>

      <div style={{opacity: botIn * (0.45 + 0.55 * botFocus), transform: `translateX(${(1 - botIn) * 120}px)`}}>
        <Card x={60} y={1024} w={960} h={400} style={{borderColor: botFocus > 0.5 ? `${C.green}55` : undefined}}>
          <Label style={{position: 'absolute', left: 40, top: 34}}>
            <span style={{color: C.green}}>ETF</span> · 1.000 aziende
          </Label>
          <div style={{position: 'absolute', right: 40, top: 22, textAlign: 'right'}}>
            <div style={{fontFamily: FONT, fontWeight: 900, fontSize: 64, color: crashBot > 0 ? C.amber : C.text, fontVariantNumeric: 'tabular-nums'}}>
              {fmtPct(-0.06 * crashBot, 2)}
            </div>
          </div>
          <svg width={200} height={260} style={{position: 'absolute', left: 46, top: 112}}>
            {Array.from({length: 1000}, (_, i) => {
              const c = i % 25;
              const r = Math.floor(i / 25);
              const isRed = i === RED_TILE;
              return (
                <rect
                  key={i}
                  x={c * 7.8}
                  y={r * 6.4}
                  width={6}
                  height={4.8}
                  rx={1.2}
                  fill={isRed ? mix('#1E7A5C', '#EF4444', red) : c % 7 === r % 5 ? '#2A9D74' : '#1E7A5C'}
                />
              );
            })}
            {f >= O && (
              <circle
                cx={(RED_TILE % 25) * 7.8 + 3}
                cy={Math.floor(RED_TILE / 25) * 6.4 + 2.4}
                r={8 + 22 * ring}
                fill="none"
                stroke={C.red}
                strokeWidth={3}
                opacity={Math.max(0, 1.2 - ring * 0.6)}
              />
            )}
          </svg>
          <LineChart x={290} y={120} w={620} h={240} series={BASKET} vmin={VMIN} vmax={VMAX} reveal={revBot} color={C.green} />
        </Card>
      </div>

      <div
        style={{
          position: 'absolute',
          top: 1450,
          width: '100%',
          textAlign: 'center',
          fontFamily: FONT,
          fontWeight: 500,
          fontSize: 24,
          color: C.dim,
          opacity: ramp(f, O, O + 20),
        }}
      >
        Esempio semplificato: 1.000 aziende con lo stesso peso.
      </div>
    </AbsoluteFill>
  );
};
