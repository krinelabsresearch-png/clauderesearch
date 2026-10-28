// Il "regista": a ogni frame raccoglie le forme di vetro delle scene attive,
// la capsula dei sottotitoli e l'onda di transizione, e prepara il World dello shader.
import type React from 'react';
import {DURATION_FRAMES, FPS, TIMELINE, type Accent} from '../script';
import type {Shape, World} from './glass/renderer';
import {captionShape} from './captions';
import {AMB, BLU, G, LEAD, RED, TAIL, clamp01, easeInOut, makeCtx, scaled, type Ctx, type RGB} from './kit';

export type Extras = Partial<Pick<World, 'beads' | 'tiles' | 'chart' | 'ripple'>>;
export type SceneDef = {
  shapes: (c: Ctx) => Shape[];
  extras?: (c: Ctx) => Extras;
  Overlay: React.FC<{c: Ctx}>;
  /** punto da cui parte l'onda di vetro che apre la scena */
  ringFrom: [number, number];
};

const ACC: Record<Accent, RGB> = {green: G, red: RED, amber: AMB, blue: BLU};

export const WINDOWS = TIMELINE.map((s, i) => {
  const from = Math.round(s.start * FPS) - (i > 0 ? LEAD : 0);
  const end = i < TIMELINE.length - 1 ? Math.round(s.end * FPS) + TAIL : DURATION_FRAMES;
  return {from, total: end - from};
});

export type Transition = {i: number; x: number; y: number; R: number; thick: number; u: number};

export const transitionAt = (F: number, defs: Record<string, SceneDef>): Transition | null => {
  for (let i = 1; i < TIMELINE.length; i++) {
    const b = Math.round(TIMELINE[i].start * FPS);
    if (F >= b - LEAD && F < b + TAIL) {
      const u = (F - (b - LEAD)) / (LEAD + TAIL);
      const [x, y] = defs[TIMELINE[i].id].ringFrom;
      const R = easeInOut(u) * 2300;
      // finché l'onda è piccola resta sottile: un anello spesso e stretto sembrerebbe una ciambella
      return {i, x, y, R, thick: Math.min(14 + 92 * Math.sin(Math.PI * u), R * 0.5), u};
    }
  }
  return null;
};

const smooth = (x: number) => {
  const s = clamp01(x);
  return s * s * (3 - 2 * s);
};

/** Quanto è visibile una forma mentre passa l'onda: chi esce si scioglie, chi entra nasce dietro l'onda. */
const passFactor = (role: 'in' | 'out', x: number, y: number, tr: Transition) => {
  const d = Math.hypot(x - tr.x, y - tr.y);
  return role === 'out' ? smooth((d - tr.R + 40) / 220) : smooth((tr.R - d + 40) / 220);
};

export const activeScenes = (F: number) =>
  TIMELINE.map((s, i) => ({s, i, w: WINDOWS[i]})).filter(({w}) => F >= w.from && F < w.from + w.total);

export const computeWorld = (F: number, defs: Record<string, SceneDef>): World => {
  const tr = transitionAt(F, defs);
  const shapes: Shape[] = [captionShape(F)];
  const world: World = {shapes, accA: G, accB: G};
  for (const {s, i, w} of activeScenes(F)) {
    const def = defs[s.id];
    const c = makeCtx(s, w.from, w.total, F - w.from);
    const role = tr ? (i === tr.i ? 'in' : i === tr.i - 1 ? 'out' : null) : null;
    for (const sh of def.shapes(c)) {
      const k = role ? passFactor(role, sh.x, sh.y, tr!) : 1;
      if (k > 0.01) shapes.push(k < 1 ? scaled(sh, k) : sh);
    }
    const ex = def.extras?.(c);
    if (ex) {
      const side = role === 'out' ? 0 : role === 'in' ? 1 : 2;
      if (ex.beads) world.beads = {...ex.beads, side};
      if (ex.tiles) world.tiles = {...ex.tiles, side};
      if (ex.chart) world.chart = {...ex.chart, side};
      if (ex.ripple) world.ripple = ex.ripple;
    }
    if (!tr) world.accA = world.accB = ACC[s.accent];
  }
  if (tr) {
    world.accA = ACC[TIMELINE[tr.i - 1].accent];
    world.accB = ACC[TIMELINE[tr.i].accent];
    world.ring = {x: tr.x, y: tr.y, r: tr.R, thick: tr.thick};
  }
  return world;
};
