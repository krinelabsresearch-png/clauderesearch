// Il reel: foto vere in 2.5D e oggetti generati (Canvas 2D + WebGL), rifratti dallo
// strato di controlli in stile Liquid Glass; testo nitido sopra, voce ed effetti sonori.
import React from 'react';
import {AbsoluteFill, Html5Audio, Sequence, staticFile, useCurrentFrame} from 'remotion';
import './assets';
import {FPS, VOICE_CLIPS} from './script';
import {GlassCanvas} from './glass/GlassCanvas';
import {paintWorld} from './content/world';
import {IslandText, islandGlass} from './ui/island';
import {WidgetsOverlay, lightAt, widgetsGlass} from './ui/widgets';
import {FONT} from './theme';

export const TenTen: React.FC<{quality?: number; sfx?: boolean}> = ({quality = 1, sfx = true}) => {
  const F = useCurrentFrame();
  const t = F / FPS;
  const glass = [islandGlass(F), ...widgetsGlass(t)];
  return (
    <AbsoluteFill style={{background: '#000', fontFamily: FONT}}>
      <GlassCanvas paint={paintWorld} glass={glass} light={lightAt(t)} quality={quality} />
      <WidgetsOverlay t={t} />
      <IslandText />
      {VOICE_CLIPS.map((v) => (
        <Sequence key={v.file} from={Math.round(v.start * FPS)} layout="none">
          <Html5Audio src={staticFile(`voice/${v.file}`)} />
        </Sequence>
      ))}
      {sfx && <Html5Audio src={staticFile('sfx/sfx.wav')} volume={0.6} />}
    </AbsoluteFill>
  );
};
