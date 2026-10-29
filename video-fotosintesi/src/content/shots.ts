// Le illustrazioni del contenuto (sotto il vetro). Ogni inquadratura riempie
// tutto lo schermo e accetta un tempo locale `t` (secondi) e i suoi parametri.
import {clamp01, hash, lerp, smooth} from '../theme';
import {LEAF, bokeh, bubble, glow, glucose, leaf, linear, molecule, photon, radial, rays, smallLeaf, type Ctx, type LeafStyle} from './draw';

const W = 1080;
const H = 1920;
const fillAll = (ctx: Ctx, style: string | CanvasGradient) => {
  ctx.fillStyle = style;
  ctx.fillRect(-W, -H, W * 3, H * 3);
};
const DARK_LEAF: LeafStyle = {light: '#4E9A3A', mid: '#22663A', dark: '#0B3018', vein: 'rgba(150,220,130,0.25)', sheen: 0.06, veins: 7};
const modp = (x: number, m: number) => ((x % m) + m) % m;

// ─── A. Foglia in macro con bolle di ossigeno ────────────────────────────────
export const HERO_LEAF = {x: -90, y: 1640, a: -0.78, len: 1650, wid: 380};

export const leafMacro = (ctx: Ctx, t: number, dim = 0) => {
  fillAll(ctx, radial(ctx, 790, 400, 0, 1750, [[0, '#F2FFC9'], [0.1, '#A7E86A'], [0.34, '#228E40'], [0.72, '#08421D'], [1, '#021509']]));
  bokeh(ctx, 11, 20, t, 'rgba(235,255,190,1)', 0.2, 34, 120);
  glow(ctx, 800, 360, 560, 'rgba(255,250,215,1)', 0.5);
  rays(ctx, 800, 360, 1500, 10, t, 0.045);
  const z = 1 + 0.045 * smooth(t / 7);
  ctx.save();
  ctx.translate(540, 960);
  ctx.scale(z, z);
  ctx.translate(-540, -960);
  leaf(ctx, 1190, 1880, -2.55, 920, 240, DARK_LEAF);
  leaf(ctx, -160, 330, 0.32, 760, 190, DARK_LEAF);
  const L = HERO_LEAF;
  const a = L.a + Math.sin(t * 0.7) * 0.012;
  leaf(ctx, L.x, L.y, a, L.len, L.wid, LEAF);
  // bolle che nascono sulla foglia e salgono, in ciclo
  const ca = Math.cos(a);
  const sa = Math.sin(a);
  for (let i = 0; i < 28; i++) {
    const u = 0.14 + hash(i * 3.1) * 0.74;
    const v = (hash(i * 7.7) - 0.5) * 0.9 * L.wid * Math.sin(Math.PI * u);
    const bx = L.x + ca * u * L.len - sa * v;
    const by = L.y + sa * u * L.len + ca * v;
    const period = 3.6 + hash(i) * 3.2;
    const ph = modp(t / period + hash(i * 5.3), 1);
    const rise = ph * (520 + hash(i * 2.2) * 420);
    const r = (5 + hash(i * 9.9) * 17) * smooth(ph / 0.12);
    bubble(ctx, bx + Math.sin(ph * 9 + i) * 10 * ph, by - rise, r, 1 - smooth((ph - 0.75) / 0.25));
  }
  ctx.restore();
  fillAll(ctx, radial(ctx, 540, 960, 600, 1400, [[0, 'rgba(0,0,0,0)'], [1, 'rgba(0,10,4,0.55)']]));
  if (dim > 0) fillAll(ctx, `rgba(2,14,8,${dim})`);
};

// ─── B. La pianta intera: cielo, sole, terreno in sezione, radici ─────────────
export const SUN = {x: 800, y: 520};
export const GROUND = 1160;
export const TARGET_LEAF = {x: 552, y: 905, a: -0.42, len: 290, wid: 86};
const STEM_TOP = 690;

type PlantParams = {sun: number; water: number; flow: number; co2: number; enter: number};

const ROOTS: {x0: number; y0: number; x1: number; y1: number; w: number}[] = [];
{
  const grow = (x: number, y: number, ang: number, len: number, w: number, depth: number, seed: number) => {
    const x1 = x + Math.cos(ang) * len;
    const y1 = y + Math.sin(ang) * len;
    ROOTS.push({x0: x, y0: y, x1, y1, w});
    if (depth === 0) return;
    for (const s of [-1, 1]) grow(x1, y1, ang + s * (0.35 + hash(seed + s) * 0.35), len * (0.62 + hash(seed * 2 + s) * 0.18), w * 0.62, depth - 1, seed * 3 + s + 7);
  };
  grow(540, GROUND, Math.PI / 2, 150, 16, 4, 1);
}
const ROOT_TIP = ROOTS[ROOTS.length - 1];

const PLANT_LEAVES = [
  {y: 1085, s: -1, len: 230, wid: 68, a: -2.55},
  {y: 1010, s: 1, len: 250, wid: 74, a: -0.55},
  {y: 935, s: -1, len: 270, wid: 80, a: -2.7},
  {y: 905, s: 1, len: TARGET_LEAF.len, wid: TARGET_LEAF.wid, a: TARGET_LEAF.a},
  {y: 830, s: -1, len: 240, wid: 72, a: -2.45},
  {y: 770, s: 1, len: 200, wid: 60, a: -0.85},
  {y: 720, s: -1, len: 170, wid: 50, a: -2.2},
];

// Percorso dell'acqua: punta della radice → base del fusto → su per il fusto → nella foglia.
const WATER_PATH: [number, number][] = [
  [ROOT_TIP.x1, ROOT_TIP.y1], [ROOT_TIP.x0, ROOT_TIP.y0], [540, GROUND + 120], [540, GROUND], [540, 1000], [544, TARGET_LEAF.y],
  [TARGET_LEAF.x + Math.cos(TARGET_LEAF.a) * 130, TARGET_LEAF.y + Math.sin(TARGET_LEAF.a) * 130],
  [TARGET_LEAF.x + Math.cos(TARGET_LEAF.a) * 250, TARGET_LEAF.y + Math.sin(TARGET_LEAF.a) * 250],
];
const pathAt = (u: number): [number, number] => {
  const segs = WATER_PATH.slice(1).map((p, i) => Math.hypot(p[0] - WATER_PATH[i][0], p[1] - WATER_PATH[i][1]));
  const total = segs.reduce((a, b) => a + b, 0);
  let d = clamp01(u) * total;
  for (let i = 0; i < segs.length; i++) {
    if (d <= segs[i]) {
      const k = d / segs[i];
      return [lerp(WATER_PATH[i][0], WATER_PATH[i + 1][0], k), lerp(WATER_PATH[i][1], WATER_PATH[i + 1][1], k)];
    }
    d -= segs[i];
  }
  return WATER_PATH[WATER_PATH.length - 1];
};

/** Punto sulla foglia bersaglio dove entra l'anidride carbonica (stomi). */
export const STOMA_POINT: [number, number] = [TARGET_LEAF.x + Math.cos(TARGET_LEAF.a) * 170, TARGET_LEAF.y + Math.sin(TARGET_LEAF.a) * 170 + 10];

export const plantScene = (ctx: Ctx, t: number, p: PlantParams) => {
  fillAll(ctx, linear(ctx, 0, 0, 0, GROUND, [[0, '#0D3F7E'], [0.45, '#3D8FDB'], [0.86, '#A9D8F2'], [1, '#FFE6A6']]));
  glow(ctx, SUN.x, SUN.y, 640, 'rgba(255,236,170,1)', 0.38 + 0.3 * p.sun);
  rays(ctx, SUN.x, SUN.y, 1300, 12, t, 0.035 + 0.07 * p.sun);
  glow(ctx, SUN.x, SUN.y, 150 + 40 * p.sun, 'rgba(255,255,235,1)', 0.95);
  ctx.fillStyle = '#FFFBEA';
  ctx.beginPath();
  ctx.arc(SUN.x, SUN.y, 62, 0, Math.PI * 2);
  ctx.fill();
  // colline lontane, con foschia
  const hill = (base: number, amp: number, freq: number, ph: number, col: string) => {
    ctx.fillStyle = col;
    ctx.beginPath();
    ctx.moveTo(-W, GROUND + 4);
    for (let x = -W; x <= 2 * W; x += 30) ctx.lineTo(x, base - amp * (0.5 + 0.5 * Math.sin(x * freq + ph)));
    ctx.lineTo(2 * W, GROUND + 4);
    ctx.closePath();
    ctx.fill();
  };
  hill(GROUND - 60, 70, 0.006, 1.2, '#8CC7A0');
  hill(GROUND - 20, 50, 0.009, 3.1, '#4E9E5E');
  // terreno in sezione
  ctx.fillStyle = linear(ctx, 0, GROUND, 0, H, [[0, '#7A4E28'], [0.25, '#5B3A1E'], [1, '#26160A']]);
  ctx.fillRect(-W, GROUND, W * 3, H * 2);
  for (let i = 0; i < 70; i++) {
    const x = hash(i * 1.7) * W;
    const y = GROUND + 30 + hash(i * 2.9) * 720;
    const r = 4 + hash(i * 4.4) * 11;
    ctx.fillStyle = `rgba(${150 + hash(i) * 60},${110 + hash(i) * 40},${70 + hash(i) * 30},0.35)`;
    ctx.beginPath();
    ctx.ellipse(x, y, r * 1.3, r, hash(i * 6) * 3, 0, Math.PI * 2);
    ctx.fill();
  }
  ctx.fillStyle = linear(ctx, 0, GROUND - 26, 0, GROUND + 10, [[0, '#57B85F'], [1, '#2E7D3A']]);
  ctx.fillRect(-W, GROUND - 14, W * 3, 26);
  // acqua nel terreno
  if (p.water > 0) {
    for (let i = 0; i < 26; i++) {
      const x = 260 + hash(i * 3.3) * 560;
      const y = GROUND + 120 + hash(i * 8.1) * 560;
      const r = (6 + hash(i * 2.6) * 9) * smooth(p.water * 1.4 - hash(i) * 0.4);
      if (r <= 0.5) continue;
      glow(ctx, x, y, r * 4, 'rgba(100,210,255,1)', 0.25 * p.water);
      ctx.fillStyle = radial(ctx, x - r * 0.3, y - r * 0.3, 0, r, [[0, '#E8FAFF'], [0.35, '#64D2FF'], [1, '#0A84FF']]);
      ctx.beginPath();
      ctx.arc(x, y, r, 0, Math.PI * 2);
      ctx.fill();
    }
  }
  // radici
  ctx.lineCap = 'round';
  for (const r of ROOTS) {
    ctx.strokeStyle = '#E3C59A';
    ctx.lineWidth = r.w;
    ctx.beginPath();
    ctx.moveTo(r.x0, r.y0);
    ctx.lineTo(r.x1, r.y1);
    ctx.stroke();
  }
  // fusto e foglie
  ctx.strokeStyle = linear(ctx, 0, STEM_TOP, 0, GROUND, [[0, '#7BD86B'], [1, '#2F8F3D']]);
  ctx.lineWidth = 18;
  ctx.beginPath();
  ctx.moveTo(540, GROUND);
  ctx.quadraticCurveTo(528, 940, 540, STEM_TOP);
  ctx.stroke();
  for (const l of PLANT_LEAVES) {
    const sway = Math.sin(t * 0.9 + l.y) * 0.03;
    leaf(ctx, 540 + l.s * 8, l.y, l.a + sway, l.len, l.wid, {...LEAF, veins: 6, sheen: 0.18}, l.y === TARGET_LEAF.y ? 0.25 * p.enter : 0);
  }
  // acqua che sale: perline luminose lungo il percorso
  if (p.flow > 0) {
    for (let k = 0; k < 14; k++) {
      const u = modp(t * 0.22 + k / 14, 1);
      if (u > p.flow * 1.05) continue;
      const [x, y] = pathAt(u);
      glow(ctx, x, y, 26, 'rgba(100,210,255,1)', 0.75);
      ctx.fillStyle = '#E8FAFF';
      ctx.beginPath();
      ctx.arc(x, y, 6, 0, Math.PI * 2);
      ctx.fill();
    }
  }
  // anidride carbonica nell'aria, che poi entra nella foglia
  if (p.co2 > 0) {
    for (let i = 0; i < 12; i++) {
      const hx = 140 + hash(i * 4.7) * 800;
      const hy = 560 + hash(i * 6.1) * 470;
      const fx = hx + Math.sin(t * 0.6 + i) * 26;
      const fy = hy + Math.cos(t * 0.5 + i * 1.3) * 20;
      const e = smooth(p.enter * 1.5 - (i / 12) * 0.5);
      const x = lerp(fx, STOMA_POINT[0], e);
      const y = lerp(fy, STOMA_POINT[1], e);
      const a = smooth(p.co2 * 1.6 - hash(i) * 0.6) * (1 - smooth((e - 0.8) / 0.2));
      molecule(ctx, 'CO2', x, y, 15 * (1 - 0.5 * e), t * 0.6 + i, a);
    }
  }
};

// ─── C. Superficie inferiore della foglia: stomi ──────────────────────────────
export const STOMA = {x: 540, y: 900};

const cellBlob = (ctx: Ctx, cx: number, cy: number, r: number, seed: number) => {
  const n = 7;
  const pts = Array.from({length: n}, (_, i) => {
    const a = (i / n) * Math.PI * 2 + hash(seed) * 0.6;
    const rr = r * (0.82 + hash(seed + i * 1.3) * 0.3);
    return [cx + Math.cos(a) * rr, cy + Math.sin(a) * rr * 0.86];
  });
  ctx.beginPath();
  pts.forEach((p, i) => {
    const q = pts[(i + 1) % n];
    const m = [(p[0] + q[0]) / 2, (p[1] + q[1]) / 2];
    if (i === 0) ctx.moveTo((pts[n - 1][0] + p[0]) / 2, (pts[n - 1][1] + p[1]) / 2);
    ctx.quadraticCurveTo(p[0], p[1], m[0], m[1]);
  });
  ctx.closePath();
};

const stoma = (ctx: Ctx, x: number, y: number, s: number, open: number, rot: number) => {
  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(rot);
  ctx.scale(s, s);
  ctx.fillStyle = 'rgba(10,50,22,0.55)';
  ctx.beginPath();
  ctx.ellipse(0, 0, 92, 62, 0, 0, Math.PI * 2);
  ctx.fill();
  for (const side of [-1, 1]) {
    ctx.save();
    ctx.scale(1, side);
    ctx.beginPath();
    ctx.ellipse(0, 22 + open * 6, 80, 34, 0, 0, Math.PI * 2);
    ctx.fillStyle = radial(ctx, -20, 10, 4, 90, [[0, '#B9F2A8'], [0.6, '#5FC46B'], [1, '#2C8A3E']]);
    ctx.fill();
    for (let k = 0; k < 6; k++) {
      ctx.fillStyle = 'rgba(25,110,45,0.85)';
      ctx.beginPath();
      ctx.ellipse(-52 + k * 21, 26 + open * 6 + Math.sin(k * 2) * 6, 7, 5, 0.4, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.restore();
  }
  // poro: si apre
  ctx.fillStyle = radial(ctx, 0, 0, 0, 60, [[0, '#020D05'], [1, '#0B2E16']]);
  ctx.beginPath();
  ctx.ellipse(0, 0, 62, 4 + 16 * open, 0, 0, Math.PI * 2);
  ctx.fill();
  ctx.restore();
};

export const stomata = (ctx: Ctx, t: number, p: {open: number; co2: number}) => {
  fillAll(ctx, linear(ctx, 0, 0, 0, H, [[0, '#1E6B33'], [0.5, '#2E8C46'], [1, '#164F27']]));
  for (let j = -1; j < 14; j++) {
    for (let i = -1; i < 9; i++) {
      const cx = i * 150 + (j % 2) * 75 + (hash(i * 13 + j) - 0.5) * 30;
      const cy = j * 140 + (hash(j * 7 + i) - 0.5) * 30;
      cellBlob(ctx, cx, cy, 82, i * 31 + j * 17);
      ctx.fillStyle = `rgba(${110 + hash(i + j * 9) * 40},${200 + hash(i * 2 + j) * 40},${120 + hash(j + i * 5) * 30},0.55)`;
      ctx.fill();
      ctx.strokeStyle = 'rgba(20,80,35,0.9)';
      ctx.lineWidth = 6;
      ctx.stroke();
    }
  }
  const others: [number, number, number, number][] = [[200, 560, 0.85, 0.5], [880, 640, 0.8, -0.3], [250, 1320, 0.9, 0.2], [860, 1250, 0.85, 0.9]];
  for (const [x, y, s, r] of others) stoma(ctx, x, y, s, 0.5 + 0.2 * Math.sin(t + x), r);
  stoma(ctx, STOMA.x, STOMA.y, 1.7, p.open, -0.08);
  for (let i = 0; i < 7; i++) {
    const ph = modp(t * 0.33 + i / 7, 1);
    const ang = hash(i * 3.3) * Math.PI * 2;
    const r0 = 560 + hash(i) * 200;
    const x = STOMA.x + Math.cos(ang) * r0 * (1 - ph);
    const y = STOMA.y + Math.sin(ang) * r0 * 0.7 * (1 - ph);
    molecule(ctx, 'CO2', x, y, 20 * (1 - 0.6 * smooth((ph - 0.6) / 0.4)), ang + t, p.co2 * (1 - smooth((ph - 0.85) / 0.15)));
  }
  fillAll(ctx, radial(ctx, 540, 900, 500, 1300, [[0, 'rgba(0,0,0,0)'], [1, 'rgba(0,20,8,0.5)']]));
};

// ─── D. Cellule a palizzata con i cloroplasti in movimento ────────────────────
export const TARGET_CHLORO: [number, number] = [608, 985];

export const cells = (ctx: Ctx, t: number) => {
  fillAll(ctx, linear(ctx, 0, 0, 0, H, [[0, '#0A2F17'], [1, '#05170B']]));
  ctx.fillStyle = linear(ctx, 0, 380, 0, 500, [[0, '#9FE3A0'], [1, '#5DBB6A']]);
  ctx.fillRect(-W, 380, W * 3, 110);
  const cw = 150;
  for (let row = 0; row < 2; row++) {
    for (let i = -1; i < 8; i++) {
      const x = 40 + i * (cw + 14);
      const y = 520 + row * 560;
      const h = 520;
      ctx.beginPath();
      ctx.roundRect(x, y, cw, h, 54);
      ctx.fillStyle = linear(ctx, x, y, x + cw, y, [[0, '#BFE9B5'], [0.5, '#E2F7DC'], [1, '#BFE9B5']]);
      ctx.fill();
      ctx.lineWidth = 7;
      ctx.strokeStyle = '#7CCB7A';
      ctx.stroke();
      // cloroplasti lungo la parete (ciclosi)
      const per = 2 * (cw + h) - 120;
      for (let k = 0; k < 16; k++) {
        const s = modp(k / 16 + t * 0.035 * (row ? -1 : 1) + i * 0.13, 1) * per;
        let px: number;
        let py: number;
        let ang: number;
        const inset = 26;
        if (s < h - 60) [px, py, ang] = [x + inset, y + 30 + s, Math.PI / 2];
        else if (s < h - 60 + cw - 60) [px, py, ang] = [x + 30 + (s - (h - 60)), y + h - inset, 0];
        else if (s < 2 * (h - 60) + cw - 60) [px, py, ang] = [x + cw - inset, y + h - 30 - (s - (h - 60 + cw - 60)), Math.PI / 2];
        else [px, py, ang] = [x + cw - 30 - (s - (2 * (h - 60) + cw - 60)), y + inset, 0];
        ctx.save();
        ctx.translate(px, py);
        ctx.rotate(ang);
        ctx.fillStyle = radial(ctx, -5, -3, 1, 22, [[0, '#7EE07F'], [0.6, '#1E9A3E'], [1, '#0F6427']]);
        ctx.beginPath();
        ctx.ellipse(0, 0, 21, 12, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      }
    }
  }
  // il cloroplasto su cui si entra
  ctx.save();
  ctx.translate(TARGET_CHLORO[0], TARGET_CHLORO[1]);
  ctx.rotate(-0.12);
  glow(ctx, 0, 0, 90, 'rgba(140,255,150,1)', 0.35 + 0.15 * Math.sin(t * 3));
  ctx.fillStyle = radial(ctx, -8, -5, 2, 34, [[0, '#9CF09A'], [0.6, '#24A846'], [1, '#0F6427']]);
  ctx.beginPath();
  ctx.ellipse(0, 0, 34, 20, 0, 0, Math.PI * 2);
  ctx.fill();
  ctx.restore();
};

// ─── E. Il cloroplasto, la luce e lo spettro ──────────────────────────────────
export const CHLORO = {x: 600, y: 1000, rx: 390, ry: 236, rot: -0.12};
export const PRISM = {x: 290, y: 640, r: 120};
const BANDS = [
  {c: '#8B5CF6', fate: 'abs'}, {c: '#3B82F6', fate: 'abs'}, {c: '#22D3EE', fate: 'part'}, {c: '#22C55E', fate: 'refl'},
  {c: '#FACC15', fate: 'part'}, {c: '#FB923C', fate: 'part'}, {c: '#EF4444', fate: 'abs'},
] as const;

const GRANA: [number, number][] = [[-250, -20], [-120, -90], [-120, 80], [20, -10], [160, -95], [170, 85], [290, -10]];

export const chloroplast = (ctx: Ctx, t: number, p: {beam: number; absorb: number; green: number; verdi: number}) => {
  fillAll(ctx, radial(ctx, 600, 980, 100, 1300, [[0, '#0E4A22'], [1, '#020E06']]));
  bokeh(ctx, 41, 14, t, 'rgba(120,230,140,1)', 0.12, 30, 90);
  const {x, y, rx, ry, rot} = CHLORO;
  glow(ctx, x, y, 620, 'rgba(90,230,120,1)', 0.18 + 0.4 * p.verdi + 0.2 * p.absorb);
  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(rot);
  ctx.beginPath();
  ctx.ellipse(0, 0, rx, ry, 0, 0, Math.PI * 2);
  ctx.fillStyle = radial(ctx, -80, -60, 20, rx * 1.1, [[0, '#7FDC86'], [0.55, '#3DAE52'], [1, '#1D7A33']]);
  ctx.fill();
  ctx.lineWidth = 7;
  ctx.strokeStyle = '#B8F3B0';
  ctx.stroke();
  ctx.beginPath();
  ctx.ellipse(0, 0, rx - 16, ry - 16, 0, 0, Math.PI * 2);
  ctx.lineWidth = 4;
  ctx.strokeStyle = 'rgba(200,250,190,0.7)';
  ctx.stroke();
  // lamelle che collegano i grani
  ctx.strokeStyle = 'rgba(25,110,45,0.8)';
  ctx.lineWidth = 6;
  for (let i = 0; i < GRANA.length - 1; i++) {
    ctx.beginPath();
    ctx.moveTo(GRANA[i][0], GRANA[i][1]);
    ctx.quadraticCurveTo((GRANA[i][0] + GRANA[i + 1][0]) / 2, (GRANA[i][1] + GRANA[i + 1][1]) / 2 + 30, GRANA[i + 1][0], GRANA[i + 1][1]);
    ctx.stroke();
  }
  // grani: pile di tilacoidi
  const lit = p.absorb;
  GRANA.forEach(([gx, gy], gi) => {
    for (let k = 0; k < 7; k++) {
      const yy = gy - 56 + k * 17;
      ctx.beginPath();
      ctx.roundRect(gx - 44, yy, 88, 13, 6.5);
      ctx.fillStyle = linear(ctx, 0, yy, 0, yy + 13, [[0, '#2FA34B'], [1, '#0E5A24']]);
      ctx.fill();
      ctx.fillStyle = `rgba(190,255,170,${0.25 + 0.5 * lit * (0.6 + 0.4 * Math.sin(t * 6 + gi + k))})`;
      ctx.fillRect(gx - 38, yy + 2, 76, 2);
    }
  });
  for (let i = 0; i < 40; i++) {
    const a = hash(i * 2.3) * Math.PI * 2;
    const r = Math.sqrt(hash(i * 5.7)) * 0.85;
    ctx.fillStyle = 'rgba(230,255,220,0.5)';
    ctx.beginPath();
    ctx.arc(Math.cos(a) * rx * r, Math.sin(a) * ry * r, 3, 0, Math.PI * 2);
    ctx.fill();
  }
  ctx.restore();

  // fascio di luce bianca verso il prisma
  if (p.beam > 0) {
    const sx = -60;
    const sy = 250;
    const ex = lerp(sx, PRISM.x - 40, clamp01(p.beam * 2));
    const ey = lerp(sy, PRISM.y - 6, clamp01(p.beam * 2));
    ctx.save();
    ctx.globalCompositeOperation = 'lighter';
    ctx.strokeStyle = 'rgba(255,255,245,0.85)';
    ctx.lineWidth = 26;
    ctx.lineCap = 'round';
    ctx.beginPath();
    ctx.moveTo(sx, sy);
    ctx.lineTo(ex, ey);
    ctx.stroke();
    ctx.strokeStyle = 'rgba(255,255,230,0.25)';
    ctx.lineWidth = 70;
    ctx.stroke();
    ctx.restore();
    // ventaglio dei colori in uscita dal prisma
    const fan = clamp01(p.beam * 2 - 1);
    if (fan > 0) {
      const ox = PRISM.x + 46;
      const oy = PRISM.y + 18;
      BANDS.forEach((b, i) => {
        const tx = lerp(420, 790, i / 6);
        const ty = lerp(1150, 900, i / 6);
        const reach = smooth(fan * 1.4 - i * 0.06);
        let end = reach;
        if (b.fate === 'part') end = reach * (1 - 0.45 * p.absorb);
        const ex2 = lerp(ox, tx, end);
        const ey2 = lerp(oy, ty, end);
        ctx.save();
        ctx.globalCompositeOperation = 'lighter';
        ctx.strokeStyle = b.c;
        ctx.globalAlpha = 0.85 * (b.fate === 'part' ? 1 - 0.5 * p.absorb : 1);
        ctx.lineWidth = 20;
        ctx.lineCap = 'round';
        ctx.beginPath();
        ctx.moveTo(ox, oy + (i - 3) * 4);
        ctx.lineTo(ex2, ey2);
        ctx.stroke();
        ctx.restore();
        if (b.fate === 'abs' && p.absorb > 0) {
          glow(ctx, tx, ty, 90 + 40 * Math.sin(t * 8 + i), b.c, 0.7 * p.absorb);
          glow(ctx, tx, ty, 260, 'rgba(120,255,140,1)', 0.25 * p.absorb);
        }
        if (b.fate === 'refl' && p.green > 0) {
          const rx2 = lerp(tx, 1000, smooth(p.green));
          const ry2 = lerp(ty, 380, smooth(p.green));
          ctx.save();
          ctx.globalCompositeOperation = 'lighter';
          ctx.strokeStyle = b.c;
          ctx.lineWidth = 26;
          ctx.lineCap = 'round';
          ctx.beginPath();
          ctx.moveTo(tx, ty);
          ctx.lineTo(rx2, ry2);
          ctx.stroke();
          ctx.restore();
          glow(ctx, rx2, ry2, 80, 'rgba(60,240,120,1)', 0.9 * p.green);
        }
      });
    }
  }
  fillAll(ctx, radial(ctx, 540, 960, 600, 1350, [[0, 'rgba(0,0,0,0)'], [1, 'rgba(0,12,5,0.55)']]));
};

// ─── F. La membrana del tilacoide: l'acqua viene spezzata ─────────────────────
export const MEMBRANE_Y = 980;
export const SPLIT_X = 330;

/** Pile di tilacoidi sfocate sullo sfondo: danno profondità alle scene dentro il cloroplasto. */
const backGrana = (ctx: Ctx, t: number, seed: number, alpha: number) => {
  for (let g = 0; g < 7; g++) {
    const gx = hash(seed + g * 3.3) * W;
    const gy = 200 + hash(seed + g * 5.1) * 1500;
    const s = 0.8 + hash(seed + g) * 0.9;
    ctx.save();
    ctx.globalAlpha = alpha * (0.5 + 0.5 * hash(seed + g * 9));
    ctx.translate(gx + Math.sin(t * 0.3 + g) * 12, gy);
    ctx.scale(s, s);
    for (let k = 0; k < 6; k++) {
      ctx.beginPath();
      ctx.roundRect(-70, -54 + k * 20, 140, 15, 7.5);
      ctx.fillStyle = linear(ctx, 0, -54 + k * 20, 0, -39 + k * 20, [[0, 'rgba(70,160,80,1)'], [1, 'rgba(20,95,40,1)']]);
      ctx.fill();
    }
    ctx.restore();
  }
};

export const thylakoid = (ctx: Ctx, t: number, p: {split: number; oxy: number}) => {
  fillAll(ctx, linear(ctx, 0, 0, 0, H, [[0, '#44A85A'], [0.48, '#2C8442'], [0.52, '#0F4D25'], [1, '#062B14']]));
  backGrana(ctx, t, 21, 0.22);
  bokeh(ctx, 77, 12, t, 'rgba(200,255,200,1)', 0.14, 30, 90);
  glow(ctx, SPLIT_X, MEMBRANE_Y - 40, 420, 'rgba(255,236,140,1)', 0.25 * p.split);
  // doppio strato lipidico ondulato
  // doppio strato lipidico ondulato, con le "code" tra le due file di teste
  ctx.fillStyle = 'rgba(190,240,170,0.28)';
  ctx.beginPath();
  for (let x = -20; x <= W + 20; x += 10) ctx.lineTo(x, MEMBRANE_Y - 40 + Math.sin(x * 0.012 + t * 0.8) * 14);
  for (let x = W + 20; x >= -20; x -= 10) ctx.lineTo(x, MEMBRANE_Y + 40 + Math.sin(x * 0.012 + t * 0.8) * 14);
  ctx.closePath();
  ctx.fill();
  for (const off of [-40, 40]) {
    for (let x = -20; x <= W + 20; x += 26) {
      const y = MEMBRANE_Y + off + Math.sin(x * 0.012 + t * 0.8) * 14;
      ctx.fillStyle = radial(ctx, x - 4, y - 4, 1, 14, [[0, '#F7FFF0'], [1, '#8FD28E']]);
      ctx.beginPath();
      ctx.arc(x, y, 13, 0, Math.PI * 2);
      ctx.fill();
    }
  }
  // complessi proteici (fotosistemi) nella membrana, con un nucleo che si accende
  for (const [cx, w] of [[SPLIT_X, 150], [660, 105], [900, 120]] as const) {
    const y = MEMBRANE_Y + Math.sin(cx * 0.012 + t * 0.8) * 14;
    ctx.fillStyle = radial(ctx, cx - 26, y - 40, 10, w * 1.3, [[0, '#DCD0FF'], [0.55, '#7C5CE0'], [1, '#3D2596']]);
    ctx.beginPath();
    ctx.ellipse(cx, y, w * 0.64, w, 0, 0, Math.PI * 2);
    ctx.fill();
    glow(ctx, cx, y - 10, w * 0.7, 'rgba(255,236,140,1)', (cx === SPLIT_X ? 0.65 : 0.3) * p.split * (0.7 + 0.3 * Math.sin(t * 7 + cx)));
  }
  // fotoni che arrivano dall'alto
  for (let k = 0; k < 4; k++) {
    const ph = modp(t * 0.7 + k / 4, 1);
    const x = SPLIT_X - 140 + k * 26 + ph * 120;
    const y = lerp(380, MEMBRANE_Y - 60, ph);
    photon(ctx, x, y, 4, 9, 'rgba(255,230,90,1)', p.split * (1 - smooth((ph - 0.85) / 0.15)));
  }
  // acqua dal basso che si spezza: H₂O → O₂ (sale) + H⁺ (resta) + energia (corre a destra)
  const N = 6;
  for (let i = 0; i < N; i++) {
    const ph = modp(t * 0.32 + i / N, 1) * p.split;
    if (p.split <= 0) continue;
    const startX = SPLIT_X + (hash(i * 3.1) - 0.5) * 300;
    const startY = 1480 + hash(i * 2.2) * 200;
    if (ph < 0.5) {
      const u = smooth(ph / 0.5);
      molecule(ctx, 'H2O', lerp(startX, SPLIT_X + (i - 2.5) * 16, u), lerp(startY, MEMBRANE_Y + 110, u), 34, t + i, 1);
    } else {
      const u = (ph - 0.5) / 0.5;
      glow(ctx, SPLIT_X, MEMBRANE_Y, 200 * (1 - u), 'rgba(255,240,150,1)', 0.7 * (1 - u));
      molecule(ctx, 'O2', SPLIT_X + (i - 2.5) * 30 + Math.sin(u * 6 + i) * 18, lerp(MEMBRANE_Y - 60, 420, smooth(u)), 34, u * 3 + i, (1 - smooth((u - 0.8) / 0.2)) * p.oxy + (1 - p.oxy) * (u < 0.15 ? 1 : 0));
      for (let h = 0; h < 2; h++) {
        const hx = SPLIT_X + (h ? 80 : -80) + (i - 2.5) * 22;
        const hy = MEMBRANE_Y + 130 + u * 240;
        glow(ctx, hx, hy, 36, 'rgba(255,255,255,1)', 0.6 * (1 - u));
        ctx.fillStyle = `rgba(255,255,255,${0.9 * (1 - u)})`;
        ctx.beginPath();
        ctx.arc(hx, hy, 10, 0, Math.PI * 2);
        ctx.fill();
      }
      photon(ctx, lerp(SPLIT_X, 900, smooth(u)), MEMBRANE_Y + Math.sin(u * 10) * 10, 9, 0, 'rgba(255,214,10,1)', 1 - smooth((u - 0.85) / 0.15));
    }
  }
};

// ─── G. Il ciclo che costruisce lo zucchero ───────────────────────────────────
export const GLU_CENTER: [number, number] = [540, 880];

export const calvin = (ctx: Ctx, t: number, p: {cin: number; glu: number}) => {
  fillAll(ctx, radial(ctx, 540, 900, 80, 1350, [[0, '#4DB063'], [0.6, '#22773A'], [1, '#0A3619']]));
  backGrana(ctx, t, 57, 0.26);
  bokeh(ctx, 91, 18, t, 'rgba(255,240,170,1)', 0.14, 30, 100);
  const [gx, gy] = GLU_CENTER;
  // anidride carbonica: già sospesa nello stroma, poi attirata al centro
  for (let i = 0; i < 6; i++) {
    const a = (i / 6) * Math.PI * 2 + 0.3;
    const r = 430 + hash(i) * 120;
    const e = smooth(p.cin * 1.3 - i * 0.06);
    const x = gx + Math.cos(a) * r * (1 - e) + Math.sin(t * 0.8 + i) * 16 * (1 - e);
    const y = gy + Math.sin(a) * r * 0.95 * (1 - e) + Math.cos(t * 0.7 + i) * 14 * (1 - e);
    molecule(ctx, 'CO2', x, y, 40, a + t * 0.5, 1 - smooth((e - 0.82) / 0.18));
  }
  // energia raccolta dalla luce che arriva al centro
  for (let k = 0; k < 10; k++) {
    const ph = modp(t * 0.5 + k / 10, 1);
    const a = hash(k * 4.1) * Math.PI * 2;
    photon(ctx, gx + Math.cos(a) * 640 * (1 - ph), gy + Math.sin(a) * 640 * (1 - ph), -Math.cos(a) * 6, -Math.sin(a) * 6, 'rgba(255,214,10,1)', (0.35 + 0.65 * clamp01(p.cin * 3)) * (1 - p.glu) * 0.8);
  }
  if (p.glu > 0) {
    glow(ctx, gx, gy, 560, 'rgba(255,214,120,1)', 0.5 * p.glu);
    glow(ctx, gx, gy, 200, 'rgba(255,250,220,1)', 0.35 * Math.max(0, 1 - Math.abs(p.glu - 0.9) * 6));
    glucose(ctx, gx, gy, 62, p.glu, Math.sin(t * 0.6) * 0.05);
  }
};

// ─── H. L'albero fatto (soprattutto) d'aria ───────────────────────────────────
type Branch = {x0: number; y0: number; x1: number; y1: number; w: number; lvl: number};
const TREE: Branch[] = [];
const CANOPY: [number, number, number][] = [];
{
  const grow = (x: number, y: number, ang: number, len: number, w: number, lvl: number, seed: number) => {
    const x1 = x + Math.cos(ang) * len;
    const y1 = y + Math.sin(ang) * len;
    TREE.push({x0: x, y0: y, x1, y1, w, lvl});
    if (lvl === 5) {
      CANOPY.push([x1, y1, 70 + hash(seed) * 40]);
      return;
    }
    const spread = 0.42 + hash(seed) * 0.15;
    grow(x1, y1, ang - spread, len * 0.74, w * 0.66, lvl + 1, seed * 2 + 1);
    grow(x1, y1, ang + spread, len * 0.74, w * 0.66, lvl + 1, seed * 2 + 2);
  };
  grow(540, 1330, -Math.PI / 2, 300, 58, 0, 1);
}
export const TREE_BASE: [number, number] = [540, 1330];

export const treeScene = (ctx: Ctx, t: number, p: {grow: number; air: number; soil: number}) => {
  fillAll(ctx, linear(ctx, 0, 0, 0, 1330, [[0, '#1C6FD1'], [0.6, '#79C2F3'], [1, '#E3F6FF']]));
  glow(ctx, 220, 420, 520, 'rgba(255,246,210,1)', 0.55);
  ctx.fillStyle = linear(ctx, 0, 1330, 0, H, [[0, '#4FAE58'], [0.04, '#2F7F3B'], [0.06, '#7A5230'], [1, '#2E1B0C']]);
  ctx.fillRect(-W, 1330, W * 3, H);
  // il terreno si scurisce quando la voce dice che il legno "non viene dal terreno"
  if (p.soil > 0) {
    ctx.fillStyle = `rgba(20,8,2,${0.35 * p.soil})`;
    ctx.fillRect(-W, 1345, W * 3, H);
  }
  // CO₂ dell'aria che converge nell'albero
  for (let i = 0; i < 90; i++) {
    const hx = hash(i * 1.37) * W;
    const hy = 280 + hash(i * 2.71) * 900;
    const tgt = CANOPY[i % CANOPY.length];
    const e = smooth(p.air * 1.6 - hash(i * 3.3) * 0.6);
    const x = lerp(hx + Math.sin(t * 0.7 + i) * 20, tgt[0], e);
    const y = lerp(hy + Math.cos(t * 0.6 + i) * 16, tgt[1], e);
    const a = (1 - smooth((e - 0.85) / 0.15)) * 0.9;
    if (i % 6 === 0) molecule(ctx, 'CO2', x, y, 11, t + i, a);
    else {
      glow(ctx, x, y, 14, 'rgba(255,255,255,1)', 0.5 * a);
      ctx.fillStyle = `rgba(255,255,255,${0.85 * a})`;
      ctx.beginPath();
      ctx.arc(x, y, 3.5, 0, Math.PI * 2);
      ctx.fill();
    }
  }
  // tronco e rami che crescono livello dopo livello
  ctx.lineCap = 'round';
  for (const b of TREE) {
    const k = clamp01(p.grow * 6.2 - b.lvl);
    if (k <= 0) continue;
    ctx.strokeStyle = linear(ctx, b.x0, b.y0, b.x1, b.y1, [[0, '#6B4527'], [1, '#8A5D36']]);
    ctx.lineWidth = b.w;
    ctx.beginPath();
    ctx.moveTo(b.x0, b.y0);
    ctx.lineTo(lerp(b.x0, b.x1, k), lerp(b.y0, b.y1, k));
    ctx.stroke();
  }
  // chioma: una massa d'ombra morbida, poi centinaia di foglie su più strati
  const ck = smooth(p.grow * 6.2 - 4.4);
  if (ck > 0) {
    glow(ctx, 540, 760, 520 * ck, 'rgba(30,110,45,1)', 0.75);
    glow(ctx, 470, 700, 360 * ck, 'rgba(60,150,60,1)', 0.5);
  }
  for (let layer = 0; layer < 3; layer++) {
    const dark = ['#1F6B2E', '#2F8F3D', '#4FB04F'][layer];
    const light = ['#3E9A44', '#6BCB5A', '#A6E77A'][layer];
    CANOPY.forEach(([x, y, r], i) => {
      const k = smooth(p.grow * 6.2 - 4.6 - hash(i + layer) * 0.7 - layer * 0.15);
      if (k <= 0) return;
      for (let j = 0; j < 7; j++) {
        const a = hash(i * 7 + j + layer * 31) * Math.PI * 2;
        const d = Math.sqrt(hash(i * 5 + j + layer * 17)) * r * 1.25 * k;
        smallLeaf(ctx, x + Math.cos(a) * d, y + Math.sin(a) * d * 0.8 - layer * 10, a + Math.sin(t * 1.4 + i + j) * 0.08, (34 + hash(i + j * 3) * 20) * k, dark, light);
      }
    });
  }
};
