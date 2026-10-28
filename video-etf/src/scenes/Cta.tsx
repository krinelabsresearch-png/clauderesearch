import React from 'react';
import {AbsoluteFill, spring, useCurrentFrame} from 'remotion';
import {FPS} from '../script';
import type {Clock} from '../components/SceneWrap';
import {Label} from '../components/Primitives';
import {C, FONT, easeIn, easeInOut, easeOut, lerp, ramp} from '../theme';
import {CENTER_Y, HERO, heroScale} from './Hook';

const BOX = 240;

const IconBox: React.FC<{x: number; color: string; children: React.ReactNode; scale: number; glow: number}> = ({
  x,
  color,
  children,
  scale,
  glow,
}) => (
  <div
    style={{
      position: 'absolute',
      left: x - BOX / 2,
      top: 880 - BOX / 2,
      width: BOX,
      height: BOX,
      borderRadius: 64,
      background: 'linear-gradient(160deg, rgba(255,255,255,0.08), rgba(255,255,255,0.02))',
      border: `2px solid ${glow > 0 ? color : 'rgba(255,255,255,0.12)'}`,
      boxShadow: `0 0 ${60 * glow}px ${color}55, 0 30px 70px rgba(0,0,0,0.5)`,
      transform: `scale(${scale})`,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
    }}
  >
    {children}
  </div>
);

export const CtaScene: React.FC<{clock: Clock}> = ({clock}) => {
  const f = useCurrentFrame();
  const Sv = clock.cue('save');
  const Sd = clock.cue('send');
  const end = clock.total - 1;

  const inP = spring({frame: f - 2, fps: FPS, config: {damping: 15, stiffness: 140}});
  const save = ramp(f, Sv + 4, Sv + 22, easeInOut);
  const savePop = spring({frame: f - Sv - 4, fps: FPS, config: {damping: 9, stiffness: 200}});
  const sendT = ramp(f, Sd + 2, Sd + 34, easeIn);
  const planeBack = spring({frame: f - Sd - 40, fps: FPS, config: {damping: 13, stiffness: 160}});
  const sendGlow = ramp(f, Sd, Sd + 10) * (1 - ramp(f, Sd + 50, Sd + 70));

  // Chiusura in loop: tutto collassa nel quadrato verde con cui il video inizia.
  const collapse = ramp(f, end - 62, end - 30, easeInOut);
  const hero = ramp(f, end - 40, end, easeOut);
  const heroSize = HERO * heroScale(0) * hero;

  const iconScale = (0.6 + 0.4 * inP) * (1 - collapse);
  const iconShift = (x: number) => lerp(x, 540, collapse) - x;

  return (
    <AbsoluteFill>
      <div style={{position: 'absolute', inset: 0, opacity: 1 - collapse}}>
        <div style={{position: 'absolute', inset: 0, transform: `translateX(${iconShift(320)}px)`}}>
          <IconBox x={320} color={C.green} scale={iconScale * (1 + 0.08 * savePop * (1 - save * 0.6))} glow={save}>
            <svg width={120} height={140} viewBox="0 0 24 28">
              <defs>
                <clipPath id="bm">
                  <path d="M3 2 H21 V26 L12 19.5 L3 26 Z" />
                </clipPath>
              </defs>
              <rect x={0} y={28 - 28 * save} width={24} height={28} fill={C.green} clipPath="url(#bm)" />
              <path d="M3 2 H21 V26 L12 19.5 L3 26 Z" fill="none" stroke={save > 0.5 ? C.green : C.text} strokeWidth={1.8} strokeLinejoin="round" />
            </svg>
          </IconBox>
          <Label size={30} color={save > 0.5 ? C.green : C.text} style={{position: 'absolute', top: 1030, left: 320 - 150, width: 300, textAlign: 'center', opacity: inP}}>
            Salva
          </Label>
        </div>

        <div style={{position: 'absolute', inset: 0, transform: `translateX(${iconShift(760)}px)`}}>
          <IconBox x={760} color={C.blue} scale={iconScale} glow={sendGlow}>
            <svg
              width={130}
              height={130}
              viewBox="0 0 24 24"
              style={{
                transform:
                  f < Sd + 40
                    ? `translate(${sendT * 380}px, ${-sendT * 420}px) rotate(${-sendT * 18}deg) scale(${1 - sendT * 0.4})`
                    : `scale(${planeBack})`,
                opacity: f < Sd + 40 ? 1 - sendT * 0.9 : 1,
              }}
            >
              <path d="M22 2 L11 13" stroke={C.text} strokeWidth={1.8} strokeLinecap="round" />
              <path d="M22 2 L15 22 L11 13 L2 9 Z" fill={sendGlow > 0.2 ? C.blue : 'none'} stroke={C.text} strokeWidth={1.8} strokeLinejoin="round" />
            </svg>
          </IconBox>
          <Label size={30} color={sendGlow > 0.2 ? C.blue : C.text} style={{position: 'absolute', top: 1030, left: 760 - 150, width: 300, textAlign: 'center', opacity: inP}}>
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
            opacity: ramp(f, 10, 30),
          }}
        >
          Contenuto informativo, non è consulenza finanziaria.
          <br />
          Investire comporta rischi, anche di perdita del capitale.
        </div>
      </div>

      {hero > 0 && (
        <div
          style={{
            position: 'absolute',
            left: 540 - heroSize / 2,
            top: CENTER_Y - heroSize / 2,
            width: heroSize,
            height: heroSize,
            borderRadius: heroSize * 0.24,
            background: `linear-gradient(145deg, #6EE7B7, ${C.green} 45%, #059669)`,
            boxShadow: `0 0 80px rgba(52,211,153,0.55), inset 0 3px 0 rgba(255,255,255,0.4)`,
          }}
        />
      )}
    </AbsoluteFill>
  );
};
