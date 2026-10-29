import React from 'react';
import {AbsoluteFill, Composition, Still, useCurrentFrame} from 'remotion';
import {DURATION_FRAMES, FPS} from './script';
import {GlassCanvas} from './glass/GlassCanvas';
import {paintWorld} from './content/world';
import {Fotosintesi} from './Fotosintesi';
import {Cover} from './Cover';

// Solo il contenuto illustrato, senza vetro: per verificare le illustrazioni.
const ContentOnly: React.FC<{quality?: number}> = ({quality = 1}) => {
  useCurrentFrame();
  return (
    <AbsoluteFill style={{background: '#000'}}>
      <GlassCanvas paint={paintWorld} glass={[]} light={[-0.6, -0.8]} quality={quality} />
    </AbsoluteFill>
  );
};

export const RemotionRoot: React.FC = () => (
  <>
    <Composition id="Fotosintesi" component={Fotosintesi} durationInFrames={DURATION_FRAMES} fps={FPS} width={1080} height={1920} defaultProps={{quality: 1}} />
    <Still id="Cover" component={Cover} width={1080} height={1920} />
    <Composition id="Content" component={ContentOnly} durationInFrames={DURATION_FRAMES} fps={FPS} width={1080} height={1920} defaultProps={{quality: 1}} />
  </>
);
