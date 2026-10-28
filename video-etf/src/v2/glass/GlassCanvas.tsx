import React, {useLayoutEffect, useRef} from 'react';
import {useCurrentFrame} from 'remotion';
import {FPS} from '../../script';
import {GlassRenderer, type World} from './renderer';

/**
 * Tela WebGL a tutto schermo che disegna sfondo e forme di vetro.
 * `quality` < 1 calcola meno pixel (bozze veloci); il risultato viene scalato.
 */
export const GlassCanvas: React.FC<{world: World; quality?: number}> = ({world, quality = 1}) => {
  const ref = useRef<HTMLCanvasElement>(null);
  const renderer = useRef<GlassRenderer | null>(null);
  const frame = useCurrentFrame();
  useLayoutEffect(() => {
    if (!renderer.current) renderer.current = new GlassRenderer(ref.current!, quality);
    renderer.current.render(world, frame / FPS);
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
