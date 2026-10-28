import React from 'react';
import {AbsoluteFill, Easing, spring, useCurrentFrame} from 'remotion';
import {FPS} from '../script';
import type {Clock} from '../components/SceneWrap';
import {Label, TitleCard} from '../components/Primitives';
import {C, FONT, easeIn, easeInOut, fmtInt, hash, lerp, mix, ramp} from '../theme';

const STACK_BASE = 1300;
const CHIP_W = 380;
const CHIP_H = 64;
const STEP = 24;
const MAX_CHIPS = 20;

const Receipt: React.FC<{color: string; text: string; style?: React.CSSProperties}> = ({color, text, style}) => (
  <div
    style={{
      position: 'absolute',
      width: CHIP_W,
      height: CHIP_H,
      borderRadius: 16,
      background: `linear-gradient(180deg, ${color}, ${color}CC)`,
      boxShadow: '0 8px 20px rgba(0,0,0,0.45), inset 0 2px 0 rgba(255,255,255,0.35)',
      display: 'flex',
      alignItems: 'center',
      gap: 16,
      padding: '0 22px',
      boxSizing: 'border-box',
      fontFamily: FONT,
      fontWeight: 800,
      fontSize: 26,
      letterSpacing: '0.06em',
      textTransform: 'uppercase',
      color: '#1A1203',
      ...style,
    }}
  >
    <span
      style={{
        width: 38,
        height: 38,
        borderRadius: '50%',
        background: 'rgba(0,0,0,0.18)',
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center',
        fontSize: 24,
      }}
    >
      €
    </span>
    {text}
  </div>
);

export const CostsScene: React.FC<{clock: Clock}> = ({clock}) => {
  const f = useCurrentFrame();
  const S = clock.cue('stream');
  const Th = clock.cue('thousand');
  const K = clock.cue('collapse');
  const Bc = clock.cue('bar');
  const Tc = clock.cue('ter');
  const Tw = clock.cue('twoeur');

  // Parte A: le commissioni si accumulano accelerando fino a 1.000.
  const grow = ramp(f, S, Th + 8, Easing.in(Easing.quad));
  const n = Math.max(1, Math.round(1000 * grow));
  const collapse = ramp(f, K, K + 24, easeInOut);
  const partA = 1 - ramp(f, Bc - 6, Bc + 12, easeIn);
  const visible = 1 + grow * (MAX_CHIPS - 1);
  const counterPop = spring({frame: f - K - 10, fps: FPS, config: {damping: 11, stiffness: 180}});

  const chips: React.ReactNode[] = [];
  for (let k = 0; k < MAX_CHIPS; k++) {
    const a = Math.min(1, Math.max(0, visible - k));
    if (a <= 0 || f < S) continue;
    const drop = easeIn(1 - a);
    const off = k * STEP * (1 - collapse);
    const jitter = (hash(k * 3) - 0.5) * 26 * (1 - collapse);
    const top = STACK_BASE - CHIP_H - off - drop * 700;
    const fadeOthers = k === 0 ? 1 : 1 - collapse;
    chips.push(
      <Receipt
        key={k}
        color={k === 0 ? mix('#FBBF24', '#34D399', collapse) : '#FBBF24'}
        text={k === 0 && collapse > 0.5 ? '1 ordine' : 'commissione'}
        style={{
          left: 540 - CHIP_W / 2 + jitter,
          top,
          opacity: a * fadeOthers,
          transform: `rotate(${(hash(k * 7) - 0.5) * 7 * (1 - collapse)}deg)`,
          zIndex: k,
        }}
      />,
    );
  }

  // Ricevute che volano verso la pila mentre il contatore sale.
  const flyers: React.ReactNode[] = [];
  if (f >= S && f < Th + 10) {
    for (let j = 0; j < 7; j++) {
      const ph = (((f - S) * (1 + grow * 1.6) + j * 11) % 60) / 60;
      const stackTop = STACK_BASE - CHIP_H - (visible - 1) * STEP;
      flyers.push(
        <Receipt
          key={`f${j}`}
          color="#FBBF24"
          text="commissione"
          style={{
            left: lerp(1150 - (j % 2) * 120, 540 - CHIP_W / 2, easeIn(ph)),
            top: lerp(560 + j * 90, stackTop, ph),
            opacity: (1 - ph) * 0.9 * (1 - ramp(f, Th, Th + 10)),
            transform: `scale(${0.55 + 0.35 * ph}) rotate(${(1 - ph) * 24}deg)`,
          }}
        />,
      );
    }
  }

  // Parte B: 1.000 € e la "fetta" da 2 € del costo annuo.
  const bar = ramp(f, Bc, Bc + 34);
  const sliver = ramp(f, Tc, Tc + 10);
  const lens = spring({frame: f - Tc - 6, fps: FPS, config: {damping: 13, stiffness: 140}});
  const ter = spring({frame: f - Tc, fps: FPS, config: {damping: 14, stiffness: 150}});
  const two = ramp(f, Tw, Tw + 14);

  return (
    <AbsoluteFill>
      <TitleCard num="02" title="COSTI" color={C.amber} outAt={S - 16} />

      {partA > 0 && f >= S - 4 && (
        <div style={{position: 'absolute', inset: 0, opacity: partA, transform: `translateY(${(1 - partA) * -90}px)`}}>
          <div style={{position: 'absolute', top: 600, width: '100%', textAlign: 'center'}}>
            <div
              style={{
                fontFamily: FONT,
                fontWeight: 900,
                fontSize: 128,
                lineHeight: 1,
                fontVariantNumeric: 'tabular-nums',
                color: collapse > 0.5 ? C.green : C.amber,
                transform: `scale(${collapse > 0.5 ? 0.8 + 0.2 * counterPop : 1})`,
              }}
            >
              × {collapse > 0.5 ? '1' : fmtInt(n)}
            </div>
            <Label size={30} color={C.text} style={{marginTop: 14}}>
              {collapse > 0.5 ? 'ordine con l’ETF' : 'commissioni, azione per azione'}
            </Label>
          </div>
          {chips}
          {flyers}
        </div>
      )}

      {f >= Bc - 4 && (
        <>
          <div
            style={{
              position: 'absolute',
              left: 100,
              top: 820,
              width: 880,
              height: 150,
              borderRadius: 75,
              background: 'rgba(255,255,255,0.06)',
              border: '1.5px solid rgba(255,255,255,0.1)',
              overflow: 'hidden',
              opacity: ramp(f, Bc - 4, Bc + 6),
            }}
          >
            <div
              style={{
                width: `${bar * 100}%`,
                height: '100%',
                borderRadius: 75,
                background: `linear-gradient(90deg, #059669, ${C.green})`,
                boxShadow: '0 0 40px rgba(52,211,153,0.35)',
              }}
            />
            <div
              style={{
                position: 'absolute',
                inset: 0,
                display: 'flex',
                alignItems: 'center',
                paddingLeft: 52,
                fontFamily: FONT,
                fontWeight: 900,
                fontSize: 50,
                color: C.ink,
                opacity: ramp(f, Bc + 18, Bc + 30),
              }}
            >
              1.000 € investiti
            </div>
            <div
              style={{
                position: 'absolute',
                right: 64,
                top: 0,
                width: 4,
                height: '100%',
                background: C.amber,
                boxShadow: `0 0 16px ${C.amber}`,
                opacity: sliver,
              }}
            />
          </div>

          {f >= Tc && (
            <svg width={1080} height={1920} style={{position: 'absolute', inset: 0}}>
              <line x1={914} y1={970} x2={830} y2={1046} stroke={C.amber} strokeWidth={3} strokeDasharray="8 8" opacity={lens} />
            </svg>
          )}

          {f >= Tc + 4 && (
            <div
              style={{
                position: 'absolute',
                left: 830 - 125,
                top: 1046,
                width: 250,
                height: 250,
                borderRadius: '50%',
                border: `5px solid ${C.amber}`,
                overflow: 'hidden',
                background: '#0B1220',
                transform: `scale(${lens})`,
                boxShadow: `0 0 50px ${C.amber}40`,
              }}
            >
              <div style={{position: 'absolute', left: 0, top: 70, width: 120, height: 110, background: `linear-gradient(90deg, #059669, ${C.green})`}} />
              <div
                style={{
                  position: 'absolute',
                  left: 120,
                  top: 70,
                  width: 80,
                  height: 110,
                  background: C.amber,
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center',
                  fontFamily: FONT,
                  fontWeight: 900,
                  fontSize: 38,
                  color: '#1A1203',
                }}
              >
                2 €
              </div>
            </div>
          )}

          {f >= Tc - 2 && (
            <div style={{position: 'absolute', left: 100, top: 1070}}>
              <div
                style={{
                  fontFamily: FONT,
                  fontWeight: 900,
                  fontSize: 132,
                  lineHeight: 1,
                  color: C.amber,
                  opacity: Math.min(1, ter * 1.5),
                  transform: `translateY(${(1 - ter) * 40}px)`,
                }}
              >
                0,2%
              </div>
              <Label size={30} color={C.text} style={{marginTop: 10, opacity: ter}}>
                costo all’anno
              </Label>
              <div
                style={{
                  marginTop: 34,
                  fontFamily: FONT,
                  fontWeight: 700,
                  fontSize: 42,
                  color: C.text,
                  opacity: two,
                  transform: `translateY(${(1 - two) * 20}px)`,
                }}
              >
                ≈ 2 € ogni 1.000 €
              </div>
            </div>
          )}

          <div
            style={{
              position: 'absolute',
              top: 1440,
              left: 90,
              right: 90,
              textAlign: 'center',
              fontFamily: FONT,
              fontWeight: 500,
              fontSize: 24,
              lineHeight: 1.4,
              color: C.dim,
              opacity: ramp(f, Tc, Tc + 20),
            }}
          >
            Costo annuo (TER) indicativo: varia da ETF a ETF.
            <br />
            Le commissioni di acquisto dipendono dal broker.
          </div>
        </>
      )}
    </AbsoluteFill>
  );
};
