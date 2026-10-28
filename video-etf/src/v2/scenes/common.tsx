// Elementi condivisi dalle scene "capitolo": il cartello di vetro con numero e titolo.
import React from 'react';
import type {Shape} from '../glass/renderer';
import {C, FONT} from '../../theme';
import {clamp01, lerp, prog, spr, type RGB} from '../kit';

type Box = {x: number; y: number; w: number; h: number};

/** Cartello di vetro che nasce da una goccia e si allarga con una molla. */
export const slabShape = (f: number, b: Box, tint: RGB): Shape => {
  const s = spr(f, 4, 12, 120);
  const sy = spr(f, 8, 10, 120);
  return {
    x: b.x,
    y: b.y + Math.sin(f * 0.05) * 3,
    w: lerp(30, b.w, s),
    h: lerp(30, b.h, sy),
    r: lerp(30, 60, Math.min(1, s)),
    k: 60,
    tint,
    tintAmt: 0.2,
    frost: 0.35,
    refr: 1.3,
  };
};

export const SlabText: React.FC<{f: number; num: string; title: string; color: string; y: number; hideAt: number}> = ({
  f,
  num,
  title,
  color,
  y,
  hideAt,
}) => {
  const out = clamp01((f - hideAt) / 12);
  if (out >= 1) return null;
  const n = spr(f, 10, 14, 150);
  return (
    <div
      style={{
        position: 'absolute',
        left: 0,
        right: 0,
        top: y - 118,
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        opacity: (1 - out) * prog(f, 8, 16),
        filter: out > 0 ? `blur(${out * 10}px)` : undefined,
        transform: `scale(${1 - 0.08 * out})`,
      }}
    >
      <div style={{height: 150, overflow: 'hidden'}}>
        <div
          style={{
            fontFamily: FONT,
            fontWeight: 900,
            fontSize: 150,
            lineHeight: 1,
            color: 'transparent',
            WebkitTextStroke: `3px ${color}`,
            transform: `translateY(${(1 - n) * 150}px)`,
            textShadow: `0 0 40px ${color}55`,
          }}
        >
          {num}
        </div>
      </div>
      <div style={{display: 'flex', marginTop: 10}}>
        {[...title].map((ch, i) => {
          const p = prog(f, 16 + i * 1.5, 28 + i * 1.5);
          return (
            <span
              key={i}
              style={{
                fontFamily: FONT,
                fontWeight: 800,
                fontSize: 48,
                letterSpacing: '0.12em',
                color: C.text,
                opacity: p,
                display: 'inline-block',
                transform: `translateY(${(1 - p) * 24}px)`,
                textShadow: '0 2px 14px rgba(0,0,0,0.5)',
              }}
            >
              {ch}
            </span>
          );
        })}
      </div>
    </div>
  );
};
