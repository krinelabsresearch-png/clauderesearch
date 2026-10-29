// Barra dei capitoli in stile iOS 26: indicatore che scivola e si allunga,
// icone che si ingrandiscono sotto l'indicatore in movimento, barra che si
// riduce a una capsula quando si "scende" nel microscopico e si riespande dopo.
import React from 'react';
import type {Glass} from '../glass/renderer';
import {COL, FONT, clamp01, lerp, smooth} from '../theme';
import {CO2Icon, DropIcon, HexIcon, O2Icon, SunIcon} from './icons';
import {REGULAR, cue, glide, life, sceneStart} from './kit';

const Y = 1452;
const HALF_W = 392;
const HALF_H = 80;
const MINI = {x: 160, w: 82};
const ITEM_X = (i: number) => 540 + (i - 2) * 152;

const TABS = [
  {label: 'Luce', Icon: SunIcon, color: COL.amber},
  {label: 'Acqua', Icon: DropIcon, color: COL.water},
  {label: 'CO₂', Icon: CO2Icon, color: '#E5E5EA'},
  {label: 'O₂', Icon: O2Icon, color: '#FF8A80'},
  {label: 'Glucosio', Icon: HexIcon, color: COL.orange},
];

let EVENTS: [number, number][] | null = null;
const events = (): [number, number][] =>
  (EVENTS ??= [
    [cue('ingr', 'luce'), 0], [cue('ingr', 'acqua'), 1], [cue('ingr', 'co2'), 2],
    [cue('path', 'up'), 1], [cue('path', 'in'), 2],
    [cue('chloro', 'beam'), 0],
    [cue('light', 'h2o'), 1], [cue('light', 'oxy'), 3],
    [cue('sugar', 'cin'), 2], [cue('sugar', 'glu'), 4],
    [cue('formula', 't1'), 2], [cue('formula', 't2'), 1], [cue('formula', 'arrow'), 0], [cue('formula', 't3'), 4], [cue('formula', 't4'), 3],
    [cue('tree', 'air'), 2],
  ]);

/** Posizione dell'indicatore (indice frazionario) e quanto si sta muovendo. */
const indicator = (t: number) => {
  const ev = events();
  let k = -1;
  while (k + 1 < ev.length && ev[k + 1][0] <= t) k++;
  if (k < 0) return {pos: ev[0][1], active: ev[0][1], moving: 0};
  const prev = k > 0 ? ev[k - 1][1] : ev[k][1];
  const g = glide(t, ev[k][0] - 0.05);
  const pos = lerp(prev, ev[k][1], g);
  return {pos, active: ev[k][1], moving: Math.sin(Math.PI * clamp01(g)) * Math.min(1, Math.abs(ev[k][1] - prev))};
};

const shown = (t: number) => life(t, sceneStart('ingr') + 0.15, sceneStart('cta') + 0.1);
// ridotta durante la discesa nel microscopico, di nuovo estesa per la formula
const minimized = (t: number) => {
  const a = glide(t, sceneStart('chloro') - 0.1);
  const b = glide(t, sceneStart('formula') - 0.2);
  return clamp01(a - b);
};

export const tabbarGlass = (t: number): Glass[] => {
  const m = shown(t);
  if (m <= 0.001) return [];
  const mn = minimized(t);
  const x = lerp(540, MINI.x, mn);
  const w = lerp(HALF_W, MINI.w, mn);
  return [{...REGULAR, x, y: Y, w, h: HALF_H, r: HALF_H, k: 0, mat: m, frost: 0.62, dim: 0.2}];
};

export const TabbarOverlay: React.FC<{t: number}> = ({t}) => {
  const m = shown(t);
  if (m <= 0.02) return null;
  const mn = minimized(t);
  const {pos, active, moving} = indicator(t);
  const ix = lerp(ITEM_X(Math.floor(pos)), ITEM_X(Math.ceil(pos)), pos - Math.floor(pos));
  const stretch = 1 + 0.45 * moving;
  const op = smooth((m - 0.3) / 0.5);
  return (
    <div style={{position: 'absolute', inset: 0, opacity: op}}>
      {mn < 0.98 && (
        <div
          style={{
            position: 'absolute',
            left: ix - 68 * stretch,
            top: Y - 66,
            width: 136 * stretch,
            height: 132,
            borderRadius: 66,
            background: 'linear-gradient(180deg, rgba(255,255,255,0.26), rgba(255,255,255,0.14))',
            boxShadow: 'inset 0 1.5px 0 rgba(255,255,255,0.45), inset 0 -1px 0 rgba(255,255,255,0.12)',
            opacity: 1 - mn,
          }}
        />
      )}
      {TABS.map((tab, i) => {
        const isActive = i === active;
        // posizione: nella barra estesa, oppure al centro della capsula ridotta (solo l'attiva)
        const x = isActive ? lerp(ITEM_X(i), MINI.x, mn) : lerp(ITEM_X(i), MINI.x, mn * 0.6);
        const vis = isActive ? 1 : 1 - smooth(mn * 1.6);
        if (vis <= 0.01) return null;
        const lens = 1 + 0.24 * moving * Math.max(0, 1 - Math.abs(ITEM_X(i) - ix) / 110);
        const col = isActive ? tab.color : '#FFFFFF';
        const showLabel = 1 - smooth(mn * 2);
        return (
          <div
            key={tab.label}
            style={{
              position: 'absolute',
              left: x - 70,
              top: Y - 58 + mn * 18,
              width: 140,
              height: 116,
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              opacity: vis * (isActive ? 1 : 0.82),
              transform: `scale(${lens * (isActive ? 1 + 0.12 * mn : 1)})`,
            }}
          >
            <tab.Icon size={54} color={col} />
            <div
              style={{
                fontFamily: FONT,
                fontSize: 23,
                fontWeight: 600,
                letterSpacing: '-0.01em',
                marginTop: 6,
                color: col,
                opacity: showLabel,
              }}
            >
              {tab.label}
            </div>
          </div>
        );
      })}
    </div>
  );
};
