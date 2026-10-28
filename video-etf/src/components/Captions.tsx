import React from 'react';
import {AbsoluteFill, interpolate, useCurrentFrame} from 'remotion';
import {FPS, TIMELINE, type Word} from '../script';
import {C, FONT, accent, easeIn, ramp} from '../theme';

const ALL = TIMELINE.flatMap((s) => s.phrases);

// Fascia alta dello schermo: fuori dalle icone e dalla didascalia di Instagram.
const TOP = 250;

const CapWord: React.FC<{w: Word; f: number; color: string}> = ({w, f, color}) => {
  const s = w.start * FPS;
  const a = ramp(f, s - 2, s + 8);
  const pill = w.hl ? ramp(f, s, s + 11) : 0;
  const pop = interpolate(f, [s, s + 5, s + 18], [0, 1, 0], {extrapolateLeft: 'clamp', extrapolateRight: 'clamp'});
  const scale = 0.9 + 0.1 * a + 0.05 * pop;
  return (
    <span
      style={{
        position: 'relative',
        display: 'inline-block',
        padding: w.hl ? '0 14px' : 0,
        margin: w.hl ? '0 -6px' : 0,
        fontFamily: FONT,
        fontWeight: 800,
        fontSize: 68,
        lineHeight: 1.14,
        letterSpacing: '-0.015em',
        color: w.hl && pill > 0.45 ? C.ink : C.text,
        opacity: a,
        transform: `translateY(${(1 - a) * 20}px) scale(${scale})`,
        filter: a < 0.999 ? `blur(${(1 - a) * 8}px)` : undefined,
        textShadow: w.hl && pill > 0.45 ? 'none' : '0 4px 30px rgba(0,0,0,0.7)',
      }}
    >
      {w.hl && (
        <span
          style={{
            position: 'absolute',
            inset: '7px 0 3px 0',
            background: color,
            borderRadius: 16,
            transform: `scaleX(${pill}) rotate(-1.2deg)`,
            transformOrigin: 'left center',
            zIndex: -1,
            boxShadow: `0 10px 34px ${color}55`,
          }}
        />
      )}
      {w.text}
    </span>
  );
};

export const Captions: React.FC = () => {
  const f = useCurrentFrame();
  return (
    <AbsoluteFill style={{pointerEvents: 'none'}}>
      {ALL.map((p, i) => {
        const next = ALL[i + 1];
        // La frase esce del tutto prima che compaia la prima parola della successiva.
        const visEnd = Math.min(next ? next.start * FPS - 8 : Infinity, (p.end + 0.45) * FPS);
        if (f < p.start * FPS - 3 || f > visEnd + 6) return null;
        const out = ramp(f, visEnd, visEnd + 6, easeIn);
        return (
          <div
            key={i}
            style={{
              position: 'absolute',
              top: TOP,
              left: 70,
              right: 70,
              display: 'flex',
              flexWrap: 'wrap',
              justifyContent: 'center',
              alignContent: 'flex-start',
              columnGap: 18,
              rowGap: 2,
              opacity: 1 - out,
              transform: `translateY(${-26 * out}px)`,
              filter: out > 0 ? `blur(${out * 6}px)` : undefined,
            }}
          >
            {p.words.map((w, j) => (
              <CapWord key={j} w={w} f={f} color={accent(p.color)} />
            ))}
          </div>
        );
      })}
    </AbsoluteFill>
  );
};
