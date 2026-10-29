// Il montaggio del contenuto: quale illustrazione in ogni istante e come si passa
// da una all'altra (zoom dentro un punto, allontanamento, dissolvenza).
import {DURATION_FRAMES, FPS, TIMELINE, cueSeconds} from '../script';
import {easeInOut, prog, smooth} from '../theme';
import type {Ctx} from './draw';
import {CHLORO, STOMA, STOMA_POINT, TARGET_CHLORO, TARGET_LEAF, calvin, cells, chloroplast, leafMacro, plantScene, stomata, thylakoid, treeScene} from './shots';

const cue = (s: string, n: string) => cueSeconds(s, n);
const start = (s: string) => TIMELINE.find((x) => x.id === s)!.start;
const LAST = (DURATION_FRAMES - 1) / FPS;

type Shot = {id: string; until: number; paint: (ctx: Ctx, t: number) => void};
// Come entra l'inquadratura successiva: 'in' = zoom dentro il punto `at`, 'out' = allontanamento, 'fade'.
type Cut = {kind: 'in' | 'out' | 'fade'; at: [number, number]};

const SHOTS: Shot[] = [
  {id: 'macro', until: cue('hook', 'leaf') + 0.1, paint: (ctx, t) => leafMacro(ctx, t)},
  {
    id: 'plant',
    until: cue('path', 'stomi') - 1.1,
    paint: (ctx, t) =>
      plantScene(ctx, t, {
        sun: smooth(prog(t, cue('ingr', 'luce') - 0.1, cue('ingr', 'luce') + 0.5)),
        water: prog(t, cue('ingr', 'acqua') - 0.1, cue('ingr', 'acqua') + 0.8),
        flow: prog(t, cue('path', 'up') - 0.2, cue('path', 'up') + 1.6),
        co2: prog(t, cue('ingr', 'co2') - 0.1, cue('ingr', 'co2') + 0.8),
        enter: prog(t, cue('path', 'in'), cue('path', 'in') + 2.2),
      }),
  },
  {id: 'stomata', until: start('chloro') + 0.25, paint: (ctx, t) => stomata(ctx, t, {open: 0.3 + 0.7 * smooth(prog(t, cue('path', 'stomi') - 1, cue('path', 'stomi') + 0.4)), co2: 1})},
  {id: 'cells', until: cue('chloro', 'chloro') + 0.45, paint: (ctx, t) => cells(ctx, t)},
  {
    id: 'chloroplast',
    until: start('light'),
    paint: (ctx, t) =>
      chloroplast(ctx, t, {
        beam: prog(t, cue('chloro', 'beam') - 0.2, cue('chloro', 'beam') + 1.1),
        absorb: prog(t, cue('chloro', 'absorb'), cue('chloro', 'absorb') + 0.6),
        green: prog(t, cue('chloro', 'green'), cue('chloro', 'green') + 0.8),
        verdi: prog(t, cue('chloro', 'verdi') - 0.1, cue('chloro', 'verdi') + 0.7),
      }),
  },
  {
    id: 'thylakoid',
    until: start('sugar'),
    paint: (ctx, t) => thylakoid(ctx, t, {split: smooth(prog(t, cue('light', 'split') - 0.7, cue('light', 'split') + 0.1)), oxy: prog(t, cue('light', 'oxy') - 0.4, cue('light', 'oxy') + 0.2)}),
  },
  {id: 'calvin', until: start('formula'), paint: (ctx, t) => calvin(ctx, t, {cin: prog(t, cue('sugar', 'cin') - 0.4, cue('sugar', 'cin') + 1.6), glu: prog(t, cue('sugar', 'glu') - 0.2, cue('sugar', 'glu') + 1.4)})},
  {id: 'formula', until: start('tree') + 0.3, paint: (ctx, t) => leafMacro(ctx, t, 0.4)},
  {
    id: 'tree',
    until: start('cta'),
    paint: (ctx, t) =>
      treeScene(ctx, t, {
        grow: prog(t, start('tree') + 0.2, cue('tree', 'wood') + 0.6),
        air: prog(t, cue('tree', 'air') - 0.6, cue('tree', 'air') + 1.2),
        soil: prog(t, cue('tree', 'soil'), cue('tree', 'soil') + 0.4) * (1 - prog(t, cue('tree', 'air'), cue('tree', 'air') + 0.5)),
      }),
  },
  // ritorno alla foglia: il tempo locale arriva a 0 sull'ultimo fotogramma, identico al primo (loop)
  {id: 'loop', until: Infinity, paint: (ctx, t) => leafMacro(ctx, t - LAST)},
];

const CUTS: Cut[] = [
  {kind: 'out', at: [TARGET_LEAF.x + 130, TARGET_LEAF.y - 60]},
  {kind: 'in', at: STOMA_POINT},
  {kind: 'in', at: [STOMA.x, STOMA.y]},
  {kind: 'in', at: TARGET_CHLORO},
  {kind: 'in', at: [CHLORO.x - 120, CHLORO.y - 20]},
  {kind: 'fade', at: [540, 960]},
  {kind: 'fade', at: [540, 960]},
  {kind: 'fade', at: [540, 960]},
  {kind: 'fade', at: [540, 960]},
];

const HALF = 0.32;

let layer: HTMLCanvasElement | null = null;
const layerFor = (ctx: Ctx) => {
  if (!layer || layer.width !== ctx.canvas.width) {
    layer = document.createElement('canvas');
    layer.width = ctx.canvas.width;
    layer.height = ctx.canvas.height;
  }
  return layer;
};

const withCamera = (ctx: Ctx, at: [number, number], scale: number, draw: () => void) => {
  ctx.save();
  ctx.translate(at[0], at[1]);
  ctx.scale(scale, scale);
  ctx.translate(-at[0], -at[1]);
  draw();
  ctx.restore();
};

export const paintWorld = (ctx: Ctx, F: number) => {
  const t = F / FPS;
  let i = SHOTS.findIndex((s) => t < s.until);
  if (i < 0) i = SHOTS.length - 1;
  // siamo dentro una transizione? (attorno al confine con l'inquadratura precedente o successiva)
  let k = -1;
  if (i > 0 && t < SHOTS[i - 1].until + HALF) k = i - 1;
  else if (t > SHOTS[i].until - HALF && i < SHOTS.length - 1) k = i;
  if (k < 0) {
    SHOTS[i].paint(ctx, t);
    return;
  }
  const b = SHOTS[k].until;
  const u = easeInOut(prog(t, b - HALF, b + HALF));
  const cut = CUTS[k];
  const out = SHOTS[k];
  const inn = SHOTS[k + 1];
  const sOut = cut.kind === 'in' ? 1 + 1.6 * u : cut.kind === 'out' ? 1 - 0.55 * u : 1 + 0.06 * u;
  const sIn = cut.kind === 'in' ? 0.42 + 0.58 * u : cut.kind === 'out' ? 2.2 - 1.2 * u : 1.06 - 0.06 * u;
  withCamera(ctx, cut.at, sOut, () => out.paint(ctx, t));
  const lay = layerFor(ctx);
  const lc = lay.getContext('2d')!;
  lc.setTransform(ctx.getTransform());
  lc.clearRect(0, 0, 1080, 1920);
  withCamera(lc, cut.at, sIn, () => inn.paint(lc, t));
  ctx.save();
  ctx.globalAlpha = smooth(u);
  ctx.drawImage(lay, 0, 0, 1080, 1920);
  ctx.restore();
};
