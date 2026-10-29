import React from 'react';
import {Composition, Still} from 'remotion';
import {DURATION_FRAMES, FPS} from './script';
import {TenTen} from './TenTen';
import {Cover} from './Cover';

export const RemotionRoot: React.FC = () => (
  <>
    <Composition id="TenTen" component={TenTen} durationInFrames={DURATION_FRAMES} fps={FPS} width={1080} height={1920} defaultProps={{quality: 1, sfx: true}} />
    <Still id="Cover" component={Cover} width={1080} height={1920} />
  </>
);
