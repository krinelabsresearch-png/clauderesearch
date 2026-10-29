// Gli effetti sonori del reel, agganciati agli stessi istanti delle animazioni.
// scripts/make-sfx.py li legge e scrive un'unica traccia, public/sfx/sfx.wav.
import {DURATION_FRAMES, FPS, TIMELINE, cueSeconds} from './script.ts';
import {T, W, timerValue} from './timing.ts';

export type Sfx = {t: number; kind: string; gain: number; dur?: number};

export const sfxEvents = (): Sfx[] => {
  const S = T();
  const w = W();
  const last = (DURATION_FRAMES - 1) / FPS;
  const ev: Sfx[] = [
    // la moneta gira (il fruscio segue la velocità di rotazione) e si ferma con un tintinnio
    {t: 0, kind: 'spin', gain: 0.55, dur: S.land},
    {t: S.land, kind: 'clink', gain: 0.8},
    // corsa verso la camera e lampo che apre il locale
    {t: S.rush - 0.25, kind: 'riser', gain: 0.5, dur: 0.6},
    {t: S.place, kind: 'boom', gain: 0.9},
    {t: cueSeconds('place', 'name'), kind: 'thump', gain: 0.7},
    {t: S.pista, kind: 'whoosh', gain: 0.35},
    {t: S.game, kind: 'whoosh', gain: 0.35},
    {t: S.rise, kind: 'whoosh', gain: 0.5},
    {t: S.press, kind: 'click', gain: 0.9},
    {t: S.stop, kind: 'click', gain: 0.9},
    {t: S.stop + 0.02, kind: 'win', gain: 0.75},
    {t: S.stop + 0.02, kind: 'boom', gain: 0.6},
    {t: S.bottle, kind: 'whoosh', gain: 0.45},
    {t: S.bottle + 0.35, kind: 'sparkler', gain: 0.4, dur: S.party + 0.6 - (S.bottle + 0.35)},
    {t: S.party, kind: 'whoosh', gain: 0.45},
    {t: S.cta, kind: 'whoosh', gain: 0.35},
    {t: w.tap, kind: 'tap', gain: 0.6},
    // in coda la moneta torna girando: il suono riparte uguale all'inizio (loop)
    {t: S.end, kind: 'spinIn', gain: 0.55, dur: last - S.end + 1 / FPS},
  ];
  // ogni vetro che si forma fa un "tink" leggero
  for (const t of [w.price, w.title, w.loc, w.chip, w.timer, w.vip, w.card, w.btn]) ev.push({t, kind: 'tink', gain: 0.22});
  // il timer: un bip a ogni secondo che scatta
  for (let s = 1; s <= 10; s++) {
    let a = S.press;
    let b = S.stop;
    for (let k = 0; k < 40; k++) {
      const m = (a + b) / 2;
      if (timerValue(m) < s) a = m;
      else b = m;
    }
    ev.push({t: b, kind: 'tick', gain: 0.35});
  }
  // tagli del montaggio "con i tuoi amici"
  const a = S.party + 0.62;
  const step = (S.cta - a) / 3;
  for (let i = 0; i < 3; i++) ev.push({t: a + i * step, kind: 'whoosh', gain: 0.32});
  return ev.sort((x, y) => x.t - y.t);
};

export const SFX_META = {duration: DURATION_FRAMES / FPS, land: T().land, scenes: TIMELINE.map((s) => s.id)};
