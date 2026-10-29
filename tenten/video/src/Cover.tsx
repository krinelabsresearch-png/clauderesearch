// Copertina del reel: la folla vera dell'XO, il buzzer fermo su 10:10 e il vetro
// con il messaggio. Tutto sta tra y 300 e 1640, dentro il ritaglio 3:4 del profilo.
import React from 'react';
import {AbsoluteFill} from 'remotion';
import './assets';
import {GlassCanvas} from './glass/GlassCanvas';
import type {Glass} from './glass/renderer';
import {PhotoRenderer} from './photo/renderer';
import {buzzer, glow, grain, type Ctx} from './content/objects';
import {REGULAR, onGlass} from './ui/kit';
import {BRAND, FONT, WORDMARK, rgb} from './theme';

let photos: PhotoRenderer | null = null;
const paint = (ctx: Ctx) => {
  photos ??= new PhotoRenderer(1080, 1920);
  const cv = photos.render({key: 'folla', cx: 0.56, cy: 0.4, zoom: 1.2, px: 0.02, focus: 0.55, defocus: 1.2, exposure: 0.8}, null, 0, 'fade');
  ctx.drawImage(cv, 0, 0, 1080, 1920);
  const g = ctx.createLinearGradient(0, 900, 0, 1920);
  g.addColorStop(0, 'rgba(10,0,2,0)');
  g.addColorStop(1, 'rgba(10,0,2,0.85)');
  ctx.fillStyle = g;
  ctx.fillRect(0, 0, 1080, 1920);
  glow(ctx, 540, 1150, 700, 'rgba(255,40,50,1)', 0.35);
  buzzer(ctx, 540, 1240, 700, 0.3, 1, '10:10');
  grain(ctx, 0);
};

const CARD = {x: 540, y: 640, w: 430, h: 178, r: 72};
const PILL = {x: 540, y: 1590, w: 360, h: 56, r: 56};

export const Cover: React.FC = () => {
  const glass: Glass[] = [
    {...REGULAR, ...CARD, k: 0, mat: 1, dim: 0.3, frost: 0.66, tint: rgb(BRAND.red), tintAmt: 0.08},
    {...REGULAR, ...PILL, k: 0, mat: 1, dim: 0.28, frost: 0.62, tint: rgb(BRAND.red), tintAmt: 0.1},
  ];
  return (
    <AbsoluteFill style={{background: '#000', fontFamily: FONT}}>
      <GlassCanvas paint={paint} glass={glass} light={[-0.6, -0.8]} />
      <div style={{position: 'absolute', left: 0, right: 0, top: CARD.y - CARD.h + 18, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
        <div style={{fontFamily: WORDMARK, fontSize: 196, lineHeight: '220px', color: BRAND.cream, letterSpacing: '0.01em', textShadow: '0 4px 30px rgba(229,35,44,0.55)'}}>TEN:TEN</div>
        <div style={{...onGlass, fontSize: 56, fontWeight: 800, letterSpacing: '-0.02em', marginTop: 2}}>
          Discoteca a{' '}
          <span style={{background: BRAND.red, padding: '0 16px', borderRadius: 999, boxShadow: '0 6px 20px rgba(229,35,44,0.4), inset 0 1.5px 0 rgba(255,255,255,0.5)'}}>1 €</span>
        </div>
      </div>
      <div style={{...onGlass, position: 'absolute', left: 0, right: 0, top: PILL.y - 30, height: 60, lineHeight: '60px', textAlign: 'center', fontSize: 38, fontWeight: 700}}>Ferma su 10:10, vinci una bottiglia</div>
    </AbsoluteFill>
  );
};
