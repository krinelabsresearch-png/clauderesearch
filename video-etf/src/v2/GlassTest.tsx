import React from 'react';
import {AbsoluteFill, useCurrentFrame} from 'remotion';
import {GlassCanvas} from './glass/GlassCanvas';
import type {Shape, World} from './glass/renderer';

const G: [number, number, number] = [0.2, 0.83, 0.6];
const A: [number, number, number] = [0.98, 0.75, 0.14];

// Banco di prova del motore di vetro: tutte le primitive con un carico simile al video.
export const GlassTest: React.FC<{quality?: number}> = ({quality = 1}) => {
  const f = useCurrentFrame();
  const t = f / 60;
  const shapes: Shape[] = [
    {x: 540, y: 330, w: 420, h: 60, r: 60, k: 0, tint: [1, 1, 1], tintAmt: 0.05, frost: 0.4},
    {x: 300 + Math.sin(t) * 40, y: 620, w: 90, kind: 'circle', k: 60, tint: G, tintAmt: 0.5},
    {x: 420 + Math.sin(t) * 40, y: 640, w: 60, kind: 'circle', k: 60, tint: G, tintAmt: 0.5},
    {x: 760, y: 640, w: 170, h: 110, r: 40, tint: [0.6, 0.7, 1], tintAmt: 0.15, fill: 0.55, wave: 6},
    {x: 540, y: 1000, w: 330, h: 170, r: 50, kind: 'cup', thick: 9},
    {x: 540, y: 1030, w: 316, h: 150, r: 40, kind: 'liquid', fill: 0.6, tint: G, tintAmt: 0.7, wave: 7, refr: 1.4},
    {x: 820, y: 1430, w: 90, kind: 'tri', r: 14, tint: A, tintAmt: 0.6},
    {x: 300, y: 1430, w: 110, kind: 'circle', mag: 0.7, refr: 2},
  ];
  for (let i = 0; i < 14; i++) {
    shapes.push({x: 260 + (i % 7) * 92, y: 1100 - Math.floor(i / 7) * 80, w: 34, kind: 'circle', k: 6, tint: [0.4 + (i % 3) * 0.2, 0.5, 0.95], tintAmt: 0.55});
  }
  const world: World = {
    shapes,
    accA: G,
    accB: G,
    ripple: {x: 540, y: 960, age: (f % 90) / 60, amp: 1},
    beads: {
      cell: 22, r: 7.5, k: 8, x0: 100, y0: 1560, cols: 40, rows: 10, cx: 540, cy: 1660, reveal: 900, shrink: 0,
      tint: G, tintAmt: 0.4, waveAmp: 0.2, waveFreq: 0.03, waveSpeed: 4, redCol: 20, redRow: 5, redAmt: 1, redGone: 0, side: 2,
    },
  };
  return (
    <AbsoluteFill style={{background: '#000'}}>
      <GlassCanvas world={world} quality={quality} />
    </AbsoluteFill>
  );
};
