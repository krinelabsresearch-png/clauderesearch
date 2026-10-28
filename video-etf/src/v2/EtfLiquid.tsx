// Versione "liquid glass" del reel: sfondo e vetro nello shader WebGL,
// testi e numeri in DOM sopra, voce e tempi dalla versione 1.
import React from 'react';
import {AbsoluteFill, Html5Audio, Sequence, staticFile, useCurrentFrame} from 'remotion';
import {FPS, TIMELINE, VOICE_CLIPS} from '../script';
import {FONT} from '../theme';
import {Captions2} from './captions';
import {GlassCanvas} from './glass/GlassCanvas';
import {makeCtx} from './kit';
import {SCENE_DEFS} from './scenes';
import {WINDOWS, computeWorld, transitionAt} from './world';

export const EtfLiquid: React.FC<{quality?: number}> = ({quality = 1}) => {
  const F = useCurrentFrame();
  const world = computeWorld(F, SCENE_DEFS);
  const tr = transitionAt(F, SCENE_DEFS);
  return (
    <AbsoluteFill style={{background: '#000', fontFamily: FONT}}>
      <GlassCanvas world={world} quality={quality} />
      {TIMELINE.map((s, i) => {
        const w = WINDOWS[i];
        if (F < w.from || F >= w.from + w.total) return null;
        const c = makeCtx(s, w.from, w.total, F - w.from);
        const {Overlay} = SCENE_DEFS[s.id];
        // Il testo segue l'onda di vetro: chi entra appare dentro il cerchio, chi esce fuori.
        let mask: string | undefined;
        if (tr && i === tr.i) mask = `radial-gradient(circle at ${tr.x}px ${tr.y}px, black ${Math.max(0, tr.R - 40)}px, transparent ${tr.R + 40}px)`;
        if (tr && i === tr.i - 1) mask = `radial-gradient(circle at ${tr.x}px ${tr.y}px, transparent ${Math.max(0, tr.R - 40)}px, black ${tr.R + 40}px)`;
        return (
          <AbsoluteFill key={s.id} style={{WebkitMaskImage: mask, maskImage: mask}}>
            <Overlay c={c} />
          </AbsoluteFill>
        );
      })}
      <Captions2 />
      {VOICE_CLIPS.map((v) => (
        <Sequence key={v.file} from={Math.round(v.start * FPS)} layout="none">
          <Html5Audio src={staticFile(`voice/${v.file}`)} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
