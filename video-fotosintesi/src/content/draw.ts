// Primitive di disegno dell'illustrazione (Canvas 2D, coordinate di progetto).
import {COL, hash, lerp} from '../theme';

export type Ctx = CanvasRenderingContext2D;

export const linear = (ctx: Ctx, x0: number, y0: number, x1: number, y1: number, stops: [number, string][]) => {
  const g = ctx.createLinearGradient(x0, y0, x1, y1);
  for (const [o, c] of stops) g.addColorStop(o, c);
  return g;
};
export const radial = (ctx: Ctx, x: number, y: number, r0: number, r1: number, stops: [number, string][], x1 = x, y1 = y) => {
  const g = ctx.createRadialGradient(x, y, r0, x1, y1, r1);
  for (const [o, c] of stops) g.addColorStop(o, c);
  return g;
};

/** Alone morbido (per luci, bokeh, bagliori). */
export const glow = (ctx: Ctx, x: number, y: number, r: number, color: string, alpha: number) => {
  if (alpha <= 0.002 || r <= 0) return;
  ctx.save();
  ctx.globalAlpha = Math.min(1, alpha);
  ctx.fillStyle = radial(ctx, x, y, 0, r, [[0, color], [1, 'rgba(0,0,0,0)']]);
  ctx.beginPath();
  ctx.arc(x, y, r, 0, Math.PI * 2);
  ctx.fill();
  ctx.restore();
};

/** Sagoma di foglia con base nell'origine e punta lungo +x. */
export const leafPath = (ctx: Ctx, len: number, wid: number) => {
  ctx.beginPath();
  ctx.moveTo(0, 0);
  ctx.bezierCurveTo(len * 0.22, -wid * 1.08, len * 0.72, -wid * 0.82, len, 0);
  ctx.bezierCurveTo(len * 0.72, wid * 0.82, len * 0.22, wid * 1.08, 0, 0);
  ctx.closePath();
};

export type LeafStyle = {light: string; mid: string; dark: string; vein: string; sheen?: number; veins?: number};
export const LEAF: LeafStyle = {light: '#B8F36B', mid: '#3FB34F', dark: '#14532D', vein: 'rgba(220,255,190,0.55)', sheen: 0.22, veins: 9};

/** Foglia con sfumatura, nervatura centrale, nervature secondarie e lucentezza. */
export const leaf = (ctx: Ctx, x: number, y: number, angle: number, len: number, wid: number, st: LeafStyle = LEAF, glowAmt = 0) => {
  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(angle);
  leafPath(ctx, len, wid);
  ctx.fillStyle = linear(ctx, 0, -wid, 0, wid, [[0, st.dark], [0.42, st.mid], [0.5, st.light], [0.58, st.mid], [1, st.dark]]);
  ctx.fill();
  ctx.save();
  ctx.clip();
  // profondità lungo la foglia: base più scura, punta più chiara
  ctx.fillStyle = linear(ctx, 0, 0, len, 0, [[0, 'rgba(0,30,10,0.35)'], [0.55, 'rgba(0,0,0,0)'], [1, 'rgba(255,255,200,0.12)']]);
  ctx.fillRect(0, -wid * 1.2, len, wid * 2.4);
  if (glowAmt > 0) {
    ctx.fillStyle = `rgba(120,255,140,${0.45 * glowAmt})`;
    ctx.fillRect(0, -wid * 1.2, len, wid * 2.4);
  }
  // nervature secondarie
  const n = st.veins ?? 9;
  ctx.strokeStyle = st.vein;
  ctx.lineCap = 'round';
  for (let i = 1; i <= n; i++) {
    const t = i / (n + 1);
    const bx = len * t * 0.92;
    const reach = wid * Math.sin(Math.PI * Math.min(1, t * 1.15)) * 0.95;
    for (const s of [-1, 1]) {
      ctx.lineWidth = Math.max(1, wid * 0.018 * (1 - t * 0.6));
      ctx.beginPath();
      ctx.moveTo(bx, 0);
      ctx.quadraticCurveTo(bx + len * 0.06, s * reach * 0.55, bx + len * 0.16, s * reach * 0.92);
      ctx.stroke();
    }
  }
  // lucentezza
  if (st.sheen) {
    ctx.globalCompositeOperation = 'screen';
    ctx.fillStyle = radial(ctx, len * 0.42, -wid * 0.35, 0, len * 0.42, [[0, `rgba(255,255,255,${st.sheen})`], [1, 'rgba(255,255,255,0)']]);
    ctx.fillRect(0, -wid * 1.2, len, wid * 2.4);
  }
  ctx.restore();
  // nervatura centrale
  ctx.strokeStyle = st.vein;
  ctx.lineWidth = Math.max(1.5, wid * 0.045);
  ctx.beginPath();
  ctx.moveTo(0, 0);
  ctx.quadraticCurveTo(len * 0.5, -wid * 0.05, len * 0.97, 0);
  ctx.stroke();
  ctx.restore();
};

/** Atomo come sfera illuminata dall'alto a sinistra. */
export const atom = (ctx: Ctx, x: number, y: number, r: number, color: string) => {
  ctx.fillStyle = radial(ctx, x - r * 0.38, y - r * 0.42, r * 0.05, r * 1.15, [
    [0, '#FFFFFF'],
    [0.18, color],
    [0.78, color],
    [1, 'rgba(0,0,0,0.55)'],
  ], x, y);
  ctx.beginPath();
  ctx.arc(x, y, r, 0, Math.PI * 2);
  ctx.fill();
};

const bond = (ctx: Ctx, x0: number, y0: number, x1: number, y1: number, w: number, double = false) => {
  ctx.strokeStyle = '#C9D1DB';
  ctx.lineCap = 'round';
  ctx.lineWidth = w;
  if (!double) {
    ctx.beginPath();
    ctx.moveTo(x0, y0);
    ctx.lineTo(x1, y1);
    ctx.stroke();
    return;
  }
  const a = Math.atan2(y1 - y0, x1 - x0) + Math.PI / 2;
  const o = w * 0.9;
  for (const s of [-1, 1]) {
    ctx.beginPath();
    ctx.moveTo(x0 + Math.cos(a) * o * s, y0 + Math.sin(a) * o * s);
    ctx.lineTo(x1 + Math.cos(a) * o * s, y1 + Math.sin(a) * o * s);
    ctx.stroke();
  }
};

export type MoleculeKind = 'CO2' | 'H2O' | 'O2';

/** Molecole con proporzioni realistiche (CO₂ lineare, H₂O a 104,5°). Scala s = raggio dell'ossigeno. */
export const molecule = (ctx: Ctx, kind: MoleculeKind, x: number, y: number, s: number, rot = 0, alpha = 1) => {
  if (alpha <= 0.01) return;
  ctx.save();
  ctx.globalAlpha = alpha;
  ctx.translate(x, y);
  ctx.rotate(rot);
  if (kind === 'CO2') {
    const d = s * 1.95;
    bond(ctx, -d, 0, d, 0, s * 0.22, true);
    atom(ctx, -d, 0, s, COL.oxygen);
    atom(ctx, d, 0, s, COL.oxygen);
    atom(ctx, 0, 0, s * 0.92, COL.carbon);
  } else if (kind === 'H2O') {
    const a = (104.5 / 2) * (Math.PI / 180);
    const d = s * 1.45;
    const hx = Math.sin(a) * d;
    const hy = Math.cos(a) * d;
    bond(ctx, 0, 0, -hx, hy, s * 0.22);
    bond(ctx, 0, 0, hx, hy, s * 0.22);
    atom(ctx, -hx, hy, s * 0.62, COL.hydrogen);
    atom(ctx, hx, hy, s * 0.62, COL.hydrogen);
    atom(ctx, 0, 0, s, COL.oxygen);
  } else {
    bond(ctx, -s * 0.9, 0, s * 0.9, 0, s * 0.22, true);
    atom(ctx, -s * 0.9, 0, s, COL.oxygen);
    atom(ctx, s * 0.9, 0, s, COL.oxygen);
  }
  ctx.restore();
};

/**
 * Glucosio in forma ciclica (piranosio): anello di 5 carboni e 1 ossigeno,
 * con i gruppi OH e il CH₂OH. `build` 0..1 fa comparire gli atomi uno dopo l'altro.
 */
export const glucose = (ctx: Ctx, x: number, y: number, s: number, build = 1, rot = 0) => {
  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(rot);
  const R = s * 3.1;
  const ring = Array.from({length: 6}, (_, i) => {
    const a = -Math.PI / 2 + (i * Math.PI) / 3 + Math.PI / 6;
    return [Math.cos(a) * R, Math.sin(a) * R * 0.62] as [number, number];
  });
  // vertice 0 = ossigeno dell'anello, 1..5 = carboni C1..C5
  const subs = [1, 2, 3, 4].map((i) => {
    const [px, py] = ring[i];
    const dir = i % 2 === 0 ? 1 : -1;
    return {i, x: px * 1.05, y: py + dir * s * 2.4};
  });
  const ch2 = {x: ring[5][0] * 1.0, y: ring[5][1] - s * 2.6};
  const items = 6 + subs.length + 1;
  const shown = (k: number) => Math.min(1, Math.max(0, build * items - k));
  ring.forEach(([px, py], i) => {
    const [qx, qy] = ring[(i + 1) % 6];
    if (shown(Math.max(i, (i + 1) % 6)) > 0.5) bond(ctx, px, py, qx, qy, s * 0.26);
  });
  subs.forEach((sb, k) => {
    if (shown(6 + k) > 0.3) bond(ctx, ring[sb.i][0], ring[sb.i][1], sb.x, sb.y, s * 0.2);
  });
  if (shown(10) > 0.3) bond(ctx, ring[5][0], ring[5][1], ch2.x, ch2.y, s * 0.2);
  ring.forEach(([px, py], i) => {
    const a = shown(i);
    if (a <= 0) return;
    ctx.save();
    ctx.globalAlpha = a;
    atom(ctx, px, py, (i === 0 ? s * 0.95 : s * 0.9) * (0.6 + 0.4 * a), i === 0 ? COL.oxygen : COL.carbon);
    ctx.restore();
  });
  subs.forEach((sb, k) => {
    const a = shown(6 + k);
    if (a <= 0) return;
    ctx.save();
    ctx.globalAlpha = a;
    atom(ctx, sb.x, sb.y, s * 0.72, COL.oxygen);
    atom(ctx, sb.x + s * 0.95, sb.y + (sb.y > 0 ? s * 0.55 : -s * 0.55), s * 0.42, COL.hydrogen);
    ctx.restore();
  });
  const a = shown(10);
  if (a > 0) {
    ctx.save();
    ctx.globalAlpha = a;
    atom(ctx, ch2.x, ch2.y, s * 0.88, COL.carbon);
    atom(ctx, ch2.x + s * 1.6, ch2.y - s * 0.9, s * 0.72, COL.oxygen);
    ctx.restore();
  }
  ctx.restore();
};

/** Bolla (ossigeno che sale): anello sottile, riflesso e un velo di colore. */
export const bubble = (ctx: Ctx, x: number, y: number, r: number, alpha = 1) => {
  if (alpha <= 0.01 || r <= 0.5) return;
  ctx.save();
  ctx.globalAlpha = alpha;
  ctx.fillStyle = radial(ctx, x, y, r * 0.2, r, [[0, 'rgba(255,255,255,0.02)'], [0.8, 'rgba(210,255,240,0.10)'], [1, 'rgba(230,255,250,0.45)']]);
  ctx.beginPath();
  ctx.arc(x, y, r, 0, Math.PI * 2);
  ctx.fill();
  ctx.strokeStyle = 'rgba(240,255,250,0.55)';
  ctx.lineWidth = Math.max(1, r * 0.08);
  ctx.stroke();
  ctx.fillStyle = 'rgba(255,255,255,0.85)';
  ctx.beginPath();
  ctx.ellipse(x - r * 0.38, y - r * 0.4, r * 0.22, r * 0.13, -0.6, 0, Math.PI * 2);
  ctx.fill();
  ctx.restore();
};

/** Luci sfocate sullo sfondo, deterministiche e in lento movimento. */
export const bokeh = (ctx: Ctx, seed: number, n: number, t: number, color: string, alpha: number, minR = 18, maxR = 70) => {
  for (let i = 0; i < n; i++) {
    const h = hash(seed + i * 7.31);
    const x = (hash(seed + i * 3.7) * 1240 - 80 + Math.sin(t * 0.25 + i) * 30) % 1240;
    const y = ((hash(seed + i * 5.1) * 2100 - 90 - t * (8 + h * 14)) % 2100 + 2100) % 2100 - 90;
    glow(ctx, x, y, lerp(minR, maxR, h), color, alpha * (0.35 + 0.65 * hash(seed + i)) * (0.75 + 0.25 * Math.sin(t * 1.3 + i * 2)));
  }
};

/** Raggi di luce a ventaglio da un punto (sole), in modalità additiva. */
export const rays = (ctx: Ctx, x: number, y: number, len: number, n: number, t: number, alpha: number, color = '255,245,200') => {
  if (alpha <= 0.002) return;
  ctx.save();
  ctx.globalCompositeOperation = 'lighter';
  for (let i = 0; i < n; i++) {
    const a = (i / n) * Math.PI * 2 + t * 0.05 + Math.sin(t * 0.3 + i) * 0.03;
    const w = 0.05 + hash(i * 9.1) * 0.07;
    const l = len * (0.6 + 0.4 * hash(i * 4.3));
    ctx.fillStyle = radial(ctx, x, y, 0, l, [[0, `rgba(${color},${alpha})`], [1, `rgba(${color},0)`]]);
    ctx.beginPath();
    ctx.moveTo(x, y);
    ctx.arc(x, y, l, a - w, a + w);
    ctx.closePath();
    ctx.fill();
  }
  ctx.restore();
};

/** Particella di luce (fotone): punto luminoso con scia. */
export const photon = (ctx: Ctx, x: number, y: number, vx: number, vy: number, color: string, alpha = 1) => {
  if (alpha <= 0.01) return;
  ctx.save();
  ctx.globalCompositeOperation = 'lighter';
  ctx.globalAlpha = alpha;
  const g = ctx.createLinearGradient(x - vx * 6, y - vy * 6, x, y);
  g.addColorStop(0, 'rgba(255,255,255,0)');
  g.addColorStop(1, color);
  ctx.strokeStyle = g;
  ctx.lineWidth = 9;
  ctx.lineCap = 'round';
  ctx.beginPath();
  ctx.moveTo(x - vx * 6, y - vy * 6);
  ctx.lineTo(x, y);
  ctx.stroke();
  ctx.restore();
  glow(ctx, x, y, 40, color, alpha * 0.9);
  glow(ctx, x, y, 10, 'rgba(255,255,255,1)', alpha);
};

/** Foglia semplice e veloce (senza nervature), per le chiome. */
export const smallLeaf = (ctx: Ctx, x: number, y: number, angle: number, len: number, color: string, light: string) => {
  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(angle);
  leafPath(ctx, len, len * 0.34);
  ctx.fillStyle = linear(ctx, 0, -len * 0.34, 0, len * 0.34, [[0, color], [0.5, light], [1, color]]);
  ctx.fill();
  ctx.restore();
};
