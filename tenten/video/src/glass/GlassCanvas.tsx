import React, {useLayoutEffect, useRef} from 'react';
import {useCurrentFrame} from 'remotion';
import {FPS} from '../script';
import {GlassRenderer, type Glass} from './renderer';

export type Painter = (ctx: CanvasRenderingContext2D, F: number) => void;

/**
 * Disegna l'illustrazione (Canvas 2D) e la passa allo shader come texture:
 * il vetro la rifrange davvero. `quality` < 1 calcola meno pixel (bozze).
 */
export const GlassCanvas: React.FC<{paint: Painter; glass: Glass[]; light: [number, number]; quality?: number}> = ({
  paint,
  glass,
  light,
  quality = 1,
}) => {
  const ref = useRef<HTMLCanvasElement>(null);
  const renderer = useRef<GlassRenderer | null>(null);
  const content = useRef<HTMLCanvasElement | null>(null);
  const F = useCurrentFrame();
  useLayoutEffect(() => {
    if (!content.current) {
      content.current = document.createElement('canvas');
      content.current.width = Math.round(1080 * quality);
      content.current.height = Math.round(1920 * quality);
    }
    const ctx = content.current.getContext('2d')!;
    ctx.setTransform(quality, 0, 0, quality, 0, 0);
    ctx.clearRect(0, 0, 1080, 1920);
    paint(ctx, F);
    if (!renderer.current) renderer.current = new GlassRenderer(ref.current!, quality);
    renderer.current.render(content.current, glass, F / FPS, light);
  });
  return (
    <canvas
      ref={ref}
      width={Math.round(1080 * quality)}
      height={Math.round(1920 * quality)}
      style={{position: 'absolute', inset: 0, width: 1080, height: 1920}}
    />
  );
};
