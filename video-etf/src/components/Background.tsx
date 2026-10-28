import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {DURATION_FRAMES, FPS, TIMELINE} from '../script';
import {C, accent} from '../theme';

const DOT = 54;

export const Background: React.FC = () => {
  const f = useCurrentFrame();
  const t = f / FPS;
  // Spostamento della griglia multiplo esatto del passo: il video si ripete senza stacchi.
  const shift = (f / DURATION_FRAMES) * DOT * 4;
  return (
    <AbsoluteFill style={{background: C.bg}}>
      {TIMELINE.map((s, i) => {
        const o = interpolate(t, [s.start - 0.3, s.start + 0.3, s.end - 0.3, s.end + 0.3], [0, 1, 1, 0], {
          extrapolateLeft: 'clamp',
          extrapolateRight: 'clamp',
        });
        if (o <= 0) return null;
        const x = 540 + Math.sin(t * 0.5 + i) * 140;
        const y = 1000 + Math.cos(t * 0.37 + i) * 180;
        return (
          <AbsoluteFill
            key={s.id}
            style={{
              opacity: o,
              background: `radial-gradient(1000px 820px at ${x}px ${y}px, ${accent(s.accent)}24, transparent 70%)`,
            }}
          />
        );
      })}
      <AbsoluteFill
        style={{
          backgroundImage: 'radial-gradient(rgba(255,255,255,0.075) 1.6px, transparent 1.9px)',
          backgroundSize: `${DOT}px ${DOT}px`,
          backgroundPosition: `${shift}px ${shift * 1.5}px`,
          WebkitMaskImage: 'radial-gradient(ellipse at 50% 50%, black 25%, transparent 78%)',
          maskImage: 'radial-gradient(ellipse at 50% 50%, black 25%, transparent 78%)',
        }}
      />
      <AbsoluteFill style={{background: 'radial-gradient(ellipse at 50% 45%, transparent 55%, rgba(0,0,0,0.6) 100%)'}} />
    </AbsoluteFill>
  );
};
