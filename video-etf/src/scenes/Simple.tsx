import React from 'react';
import {AbsoluteFill, useCurrentFrame} from 'remotion';
import type {Clock} from '../components/SceneWrap';
import {Glyph, Label, SECTOR, TitleCard} from '../components/Primitives';
import {C, FONT, easeInOut, lerp, mix, ramp} from '../theme';

const COLS = 8;
const ROWS = 6;
const T = 96;
const GAP = 18;
const GW = COLS * T + (COLS - 1) * GAP;
const GH = ROWS * T + (ROWS - 1) * GAP;
const GX = (1080 - GW) / 2;
const GY = 640;
const TARGETS = [9, 30, 20, 43, 13];
const HOP = 26;

const centerOf = (i: number) => ({
  x: GX + (i % COLS) * (T + GAP) + T / 2,
  y: GY + Math.floor(i / COLS) * (T + GAP) + T / 2,
});

export const SimpleScene: React.FC<{clock: Clock}> = ({clock}) => {
  const f = useCurrentFrame();
  const Sc = clock.cue('scan');
  const M = clock.cue('market');

  // La lente salta da un'azienda all'altra: "quale sarà la vincente?"
  const k = Math.max(0, (f - Sc) / HOP);
  const idx = Math.min(TARGETS.length - 1, Math.floor(k));
  const nextIdx = Math.min(TARGETS.length - 1, idx + 1);
  const hopT = easeInOut(Math.min(1, Math.max(0, (k - idx) * 1.6 - 0.6)));
  const a = centerOf(TARGETS[idx]);
  const b = centerOf(TARGETS[nextIdx]);
  const lx = lerp(a.x, b.x, hopT);
  const ly = lerp(a.y, b.y, hopT);
  const focus = hopT < 0.5 ? TARGETS[idx] : TARGETS[nextIdx];

  const morph = ramp(f, M, M + 26, easeInOut);
  const lensOn = ramp(f, Sc - 8, Sc + 4);
  const fw = lerp(170, GW + 44, morph);
  const fh = lerp(170, GH + 44, morph);
  const fx = lerp(lx, 540, morph);
  const fy = lerp(ly, GY + GH / 2, morph);
  const radius = lerp(85, 36, morph);
  const ring = mix('#60A5FA', '#34D399', morph);

  return (
    <AbsoluteFill>
      <TitleCard num="03" title="SEMPLICITÀ" color={C.blue} outAt={Sc - 18} />

      <div style={{opacity: ramp(f, Sc - 14, Sc + 6)}}>
        {Array.from({length: COLS * ROWS}, (_, i) => {
          const c = i % COLS;
          const r = Math.floor(i / COLS);
          const lit = ramp(f, M + 8 + (c + r) * 2, M + 20 + (c + r) * 2);
          const isFocus = morph < 0.2 && f >= Sc && i === focus;
          const color = SECTOR[(i * 3) % SECTOR.length];
          return (
            <div
              key={i}
              style={{
                position: 'absolute',
                left: GX + c * (T + GAP),
                top: GY + r * (T + GAP),
                width: T,
                height: T,
                borderRadius: 24,
                background: lit > 0 ? mix('#1B2433', color, lit) : '#1B2433',
                border: '1.5px solid rgba(255,255,255,0.07)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                transform: `scale(${isFocus ? 1.12 : 1})`,
                boxShadow: lit > 0 ? `0 10px 30px ${color}${Math.round(lit * 60).toString(16).padStart(2, '0')}` : undefined,
              }}
            >
              {lit > 0.5 ? (
                <Glyph kind={i} size={58} opacity={lit} />
              ) : (
                <span
                  style={{
                    fontFamily: FONT,
                    fontWeight: 900,
                    fontSize: isFocus ? 58 : 40,
                    color: isFocus ? C.blue : 'rgba(255,255,255,0.22)',
                    opacity: 1 - lit,
                  }}
                >
                  ?
                </span>
              )}
            </div>
          );
        })}
      </div>

      {lensOn > 0 && (
        <div
          style={{
            position: 'absolute',
            left: fx - fw / 2,
            top: fy - fh / 2,
            width: fw,
            height: fh,
            borderRadius: radius,
            border: `6px solid ${ring}`,
            boxShadow: `0 0 40px ${ring}66, inset 0 0 30px ${ring}33`,
            opacity: lensOn,
          }}
        />
      )}
      {lensOn > 0 && morph < 1 && (
        <div
          style={{
            position: 'absolute',
            left: fx + 52,
            top: fy + 52,
            width: 22,
            height: 90,
            borderRadius: 11,
            background: ring,
            transform: 'rotate(-45deg)',
            transformOrigin: '11px 0px',
            opacity: lensOn * (1 - morph),
          }}
        />
      )}

      <Label
        size={34}
        color={C.green}
        style={{
          position: 'absolute',
          top: GY + GH + 60,
          width: '100%',
          textAlign: 'center',
          letterSpacing: '0.12em',
          opacity: ramp(f, M + 26, M + 42),
          transform: `translateY(${(1 - ramp(f, M + 26, M + 42)) * 18}px)`,
        }}
      >
        Indice = l’intero mercato
      </Label>
    </AbsoluteFill>
  );
};
