import React from 'react';
import {AbsoluteFill, Sequence, useCurrentFrame} from 'remotion';
import {FPS, cueSeconds, type Scene} from '../script';
import {easeIn, easeOut, ramp} from '../theme';

/** Frame di sovrapposizione tra una scena e la successiva (transizione zoom-blur). */
export const OVER = 8;

export type Clock = {
  scene: Scene;
  /** frame locale in cui inizia la parola marcata con @name */
  cue: (name: string) => number;
  /** frame locale corrispondente a un tempo assoluto in secondi */
  at: (seconds: number) => number;
  /** durata locale totale della sequenza, transizioni incluse */
  total: number;
};

type Props = {
  scene: Scene;
  noEnter?: boolean;
  noExit?: boolean;
  push?: boolean;
  children: (clock: Clock) => React.ReactNode;
};

const Inner: React.FC<Omit<Props, 'scene'> & {clock: Clock}> = ({clock, noEnter, noExit, push = true, children}) => {
  const f = useCurrentFrame();
  const {total} = clock;
  const enter = noEnter ? 1 : ramp(f, 0, OVER * 2, easeOut);
  const exit = noExit ? 0 : ramp(f, total - OVER * 2, total, easeIn);
  // Lenta spinta in avanti della "camera": l'immagine non è mai ferma.
  const drift = push ? 1 + 0.03 * (f / total) : 1;
  const scale = (0.86 + 0.14 * enter) * (1 + 0.22 * exit) * drift;
  const blur = (1 - enter) * 16 + exit * 20;
  const fadeIn = noEnter ? 1 : ramp(f, 0, OVER * 1.4);
  const fadeOut = noExit ? 1 : 1 - ramp(f, total - OVER * 1.6, total);
  return (
    <AbsoluteFill
      style={{
        transform: `scale(${scale})`,
        filter: blur > 0.05 ? `blur(${blur}px)` : undefined,
        opacity: fadeIn * fadeOut,
      }}
    >
      {children(clock)}
    </AbsoluteFill>
  );
};

export const SceneWrap: React.FC<Props> = ({scene, noEnter, noExit, push, children}) => {
  const lead = noEnter ? 0 : OVER;
  const from = Math.round(scene.start * FPS) - lead;
  const total = Math.round((scene.end - scene.start) * FPS) + lead + (noExit ? 0 : OVER);
  const at = (s: number) => (s - scene.start) * FPS + lead;
  const clock: Clock = {scene, total, at, cue: (name) => at(cueSeconds(scene.id, name))};
  return (
    <Sequence from={from} durationInFrames={total} layout="none">
      <Inner clock={clock} noEnter={noEnter} noExit={noExit} push={push}>
        {children}
      </Inner>
    </Sequence>
  );
};
