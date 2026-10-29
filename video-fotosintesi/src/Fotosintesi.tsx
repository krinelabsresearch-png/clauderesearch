// Il reel: illustrazione (Canvas 2D) rifratta dallo strato di controlli in
// stile Liquid Glass (WebGL), testo nitido sopra, voce sincronizzata.
import React from 'react';
import {AbsoluteFill, Html5Audio, Sequence, staticFile, useCurrentFrame} from 'remotion';
import {FPS, VOICE_CLIPS} from './script';
import {GlassCanvas} from './glass/GlassCanvas';
import {paintWorld} from './content/world';
import {IslandText, islandGlass} from './ui/island';
import {TabbarOverlay, tabbarGlass} from './ui/tabbar';
import {WidgetsOverlay, lightAt, widgetsGlass} from './ui/widgets';
import {FONT} from './theme';

export const Fotosintesi: React.FC<{quality?: number}> = ({quality = 1}) => {
  const F = useCurrentFrame();
  const t = F / FPS;
  const glass = [islandGlass(F), ...tabbarGlass(t), ...widgetsGlass(t)];
  return (
    <AbsoluteFill style={{background: '#000', fontFamily: FONT}}>
      <GlassCanvas paint={paintWorld} glass={glass} light={lightAt(t)} quality={quality} />
      <WidgetsOverlay t={t} />
      <TabbarOverlay t={t} />
      <IslandText />
      {VOICE_CLIPS.map((v) => (
        <Sequence key={v.file} from={Math.round(v.start * FPS)} layout="none">
          <Html5Audio src={staticFile(`voice/${v.file}`)} />
        </Sequence>
      ))}
    </AbsoluteFill>
  );
};
