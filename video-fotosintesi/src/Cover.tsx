// Copertina del reel: la foglia del primo capitolo con il titolo di vetro del
// video, più una domanda-gancio. Gli elementi stanno tra y 480 e 1340, dentro il
// ritaglio 3:4 della griglia del profilo Instagram (y 240–1680).
import React from 'react';
import {AbsoluteFill, Freeze} from 'remotion';
import {FPS, cueSeconds} from './script';
import {GlassCanvas} from './glass/GlassCanvas';
import type {Glass} from './glass/renderer';
import {paintWorld} from './content/world';
import {WidgetsOverlay, lightAt, widgetsGlass} from './ui/widgets';
import {Pill, REGULAR, onGlass, pillGlass} from './ui/kit';
import {COL, FONT} from './theme';

// il titolo di vetro è completo poco più di un secondo dopo "fotosintesi clorofilliana"
const T = cueSeconds('hook', 'name') + 1.3;
const HEAD = {x: 540, y: 620, w: 452, h: 128, r: 64};
const PILL_Y = 1296;
const PILL_TEXT = 'spiegata in 60 secondi';

export const Cover: React.FC = () => {
  const glass: Glass[] = [
    {...REGULAR, ...HEAD, k: 0, mat: 1, dim: 0.26, frost: 0.62},
    ...widgetsGlass(T),
    pillGlass(540, PILL_Y, PILL_TEXT, 1, 1, 38),
  ];
  return (
    <AbsoluteFill style={{background: '#000', fontFamily: FONT}}>
      <Freeze frame={Math.round(T * FPS)}>
        <GlassCanvas paint={paintWorld} glass={glass} light={lightAt(T)} />
        <WidgetsOverlay t={T} />
      </Freeze>
      <div style={{...onGlass, position: 'absolute', left: HEAD.x - 420, top: HEAD.y - 104, width: 840, textAlign: 'center', fontSize: 80, lineHeight: '104px', fontWeight: 800, letterSpacing: '-0.03em'}}>
        L’ossigeno che respiri
        <br />è{' '}
        <span style={{background: COL.leaf, color: '#0B1A0F', padding: '0 20px', borderRadius: 999, textShadow: 'none', boxShadow: `0 6px 20px ${COL.leaf}55, inset 0 1.5px 0 rgba(255,255,255,0.6)`}}>un avanzo</span>
      </div>
      <Pill x={540} y={PILL_Y} text={PILL_TEXT} m={1} size={38} />
    </AbsoluteFill>
  );
};
