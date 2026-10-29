// Gli oggetti generati (moneta, buzzer, bottiglia) animati in codice, e la luce
// del locale: foschia, luci sfocate, fasci, scintille. Tutto è funzione del tempo.
import {IMG} from '../assets';
import {hash} from '../theme';

export type Ctx = CanvasRenderingContext2D;
const TAU = Math.PI * 2;

const offscreen = new Map<string, HTMLCanvasElement>();
const layer = (name: string, w: number, h: number) => {
  let c = offscreen.get(name);
  if (!c || c.width !== w || c.height !== h) {
    c = document.createElement('canvas');
    c.width = w;
    c.height = h;
    offscreen.set(name, c);
  }
  const g = c.getContext('2d')!;
  g.setTransform(1, 0, 0, 1, 0, 0);
  g.globalCompositeOperation = 'source-over';
  g.globalAlpha = 1;
  g.clearRect(0, 0, w, h);
  return {c, g};
};

export const glow = (ctx: Ctx, x: number, y: number, r: number, color: string, a: number) => {
  if (a <= 0.001 || r <= 0) return;
  const g = ctx.createRadialGradient(x, y, 0, x, y, r);
  g.addColorStop(0, color);
  g.addColorStop(1, 'rgba(0,0,0,0)');
  ctx.save();
  ctx.globalCompositeOperation = 'lighter';
  ctx.globalAlpha = Math.min(1, a);
  ctx.fillStyle = g;
  ctx.fillRect(x - r, y - r, r * 2, r * 2);
  ctx.restore();
};

// ─── Atmosfera del locale: cremisi, luci sfocate che derivano, fasci dall'alto ──
export const haze = (ctx: Ctx, t: number, amount = 1) => {
  const bg = ctx.createRadialGradient(540, 760, 60, 540, 960, 1300);
  bg.addColorStop(0, '#3A060C');
  bg.addColorStop(0.55, '#160205');
  bg.addColorStop(1, '#050001');
  ctx.fillStyle = bg;
  ctx.fillRect(0, 0, 1080, 1920);
  // nuvole di luce che respirano
  const blobs: [number, number, number, string][] = [
    [260, 520, 620, '#B3121D'],
    [860, 700, 560, '#C2185B'],
    [420, 1400, 700, '#8E0E16'],
    [900, 1500, 520, '#E5232C'],
  ];
  blobs.forEach(([x, y, r, c], i) => {
    const dx = Math.sin(t * 0.37 + i * 1.9) * 90;
    const dy = Math.cos(t * 0.29 + i * 2.7) * 70;
    glow(ctx, x + dx, y + dy, r, c, (0.34 + 0.08 * Math.sin(t * 0.9 + i)) * amount);
  });
  // fasci di luce che oscillano lentamente dal soffitto
  ctx.save();
  ctx.globalCompositeOperation = 'lighter';
  for (let i = 0; i < 5; i++) {
    const a = Math.PI / 2 + Math.sin(t * 0.45 + i * 1.3) * 0.45 + (i - 2) * 0.2;
    const ox = 180 + i * 180;
    const len = 2200;
    const w = 130 + 40 * Math.sin(i * 2.1);
    const ex = ox + Math.cos(a) * len;
    const ey = -40 + Math.sin(a) * len;
    const g = ctx.createLinearGradient(ox, -40, ex, ey);
    g.addColorStop(0, `rgba(255,90,110,${0.12 * amount})`);
    g.addColorStop(1, 'rgba(255,40,60,0)');
    ctx.fillStyle = g;
    const nx = -Math.sin(a) * w;
    const ny = Math.cos(a) * w;
    ctx.beginPath();
    ctx.moveTo(ox - 8, -40);
    ctx.lineTo(ox + 8, -40);
    ctx.lineTo(ex + nx, ey + ny);
    ctx.lineTo(ex - nx, ey - ny);
    ctx.closePath();
    ctx.fill();
  }
  ctx.restore();
  bokeh(ctx, t, amount);
};

/** Luci sfocate in primo piano (come un obiettivo aperto in un locale). */
export const bokeh = (ctx: Ctx, t: number, amount = 1) => {
  for (let i = 0; i < 18; i++) {
    const x = ((((hash(i * 3.1) * 1300 + t * (12 + hash(i) * 26) * (i % 2 ? 1 : -1)) % 1300) + 1300) % 1300) - 110;
    const y = hash(i * 7.3) * 2000 - 40 + Math.sin(t * 0.6 + i) * 30;
    const r = 30 + hash(i * 1.7) * 90;
    const warm = hash(i * 9.1);
    const col = warm > 0.7 ? 'rgba(255,214,190,1)' : warm > 0.35 ? 'rgba(255,60,80,1)' : 'rgba(230,30,110,1)';
    glow(ctx, x, y, r, col, (0.1 + 0.12 * hash(i * 4.4)) * amount * (0.75 + 0.25 * Math.sin(t * 1.3 + i * 2)));
  }
};

// ─── La moneta da 1 € che ruota in 3D ─────────────────────────────────────────
const COIN_R = 492; // raggio della moneta nell'immagine (1024×1024)

/** Moneta con rotazione `theta` attorno all'asse verticale (0 = di fronte). */
export const coin = (ctx: Ctx, x: number, y: number, r: number, theta: number, light = 1) => {
  const c = Math.cos(theta);
  const s = Math.sin(theta);
  const S = Math.ceil(r * 2.3);
  const {c: cv, g} = layer('coin', S, S);
  g.save();
  const cx = S / 2;
  const thick = r * 0.075;
  const sx = Math.max(Math.abs(c), 0.012);
  // bordo: cilindro dorato visto di lato
  const steps = 10;
  for (let k = steps; k >= 0; k--) {
    const off = (k / steps - 0.5) * thick * s;
    const shade = 0.45 + 0.35 * Math.abs(s) * (1 - Math.abs(k / steps - 0.5));
    g.fillStyle = `rgb(${Math.round(196 * shade + 40)},${Math.round(150 * shade + 30)},${Math.round(70 * shade + 10)})`;
    g.beginPath();
    g.ellipse(cx + off, cx, r * sx, r, 0, 0, TAU);
    g.fill();
  }
  // faccia
  g.save();
  g.translate(cx + (thick * s) / 2, cx);
  g.scale(c >= 0 ? sx : -sx, 1);
  g.drawImage(IMG.coin, 512 - COIN_R, 512 - COIN_R, COIN_R * 2, COIN_R * 2, -r, -r, r * 2, r * 2);
  g.restore();
  // luce: la faccia si scurisce di taglio e un riflesso la attraversa mentre gira
  g.globalCompositeOperation = 'source-atop';
  g.fillStyle = `rgba(20,4,0,${(1 - Math.abs(c)) * 0.55})`;
  g.fillRect(0, 0, S, S);
  // i riflessi restano dentro la sagoma della moneta
  g.beginPath();
  g.ellipse(cx, cx, r * sx + (thick * Math.abs(s)) / 2, r, 0, 0, TAU);
  g.clip();
  g.globalCompositeOperation = 'lighter';
  const band = cx + (s * 0.9 - 0.15) * r * sx;
  const lg = g.createLinearGradient(band - r * 0.5, 0, band + r * 0.5, S);
  lg.addColorStop(0, 'rgba(255,255,255,0)');
  lg.addColorStop(0.5, `rgba(255,246,225,${0.38 * light})`);
  lg.addColorStop(1, 'rgba(255,255,255,0)');
  g.fillStyle = lg;
  g.fillRect(0, 0, S, S);
  // riflesso rosso del locale sulla parte bassa
  const rg = g.createLinearGradient(0, cx + r * 0.2, 0, cx + r);
  rg.addColorStop(0, 'rgba(255,30,50,0)');
  rg.addColorStop(1, 'rgba(255,40,60,0.32)');
  g.fillStyle = rg;
  g.fillRect(0, 0, S, S);
  g.restore();
  // ombra morbida sotto
  ctx.save();
  ctx.globalAlpha = 0.5;
  ctx.fillStyle = 'rgba(0,0,0,0.6)';
  ctx.filter = 'blur(28px)';
  ctx.beginPath();
  ctx.ellipse(x, y + r * 1.08, r * 0.8 * Math.max(sx, 0.3), r * 0.1, 0, 0, TAU);
  ctx.fill();
  ctx.restore();
  ctx.drawImage(cv, x - cx, y - cx);
};

/** Stella di luce (riflesso sul metallo, scintilla). */
export const starFlare = (ctx: Ctx, x: number, y: number, r: number, a: number, rot = 0) => {
  if (a <= 0.001) return;
  glow(ctx, x, y, r * 0.5, 'rgba(255,250,235,1)', a);
  ctx.save();
  ctx.globalCompositeOperation = 'lighter';
  ctx.translate(x, y);
  ctx.rotate(rot);
  for (let k = 0; k < 4; k++) {
    ctx.rotate(Math.PI / 4);
    const len = k % 2 ? r * 0.6 : r * 1.5;
    const g = ctx.createLinearGradient(-len, 0, len, 0);
    g.addColorStop(0, 'rgba(255,240,220,0)');
    g.addColorStop(0.5, `rgba(255,248,236,${0.9 * Math.min(1, a)})`);
    g.addColorStop(1, 'rgba(255,240,220,0)');
    ctx.fillStyle = g;
    ctx.fillRect(-len, -2.2, len * 2, 4.4);
  }
  ctx.restore();
};

// ─── Il buzzer, con la cupola che si abbassa e il display a LED ───────────────
/** Display del buzzer nell'immagine: angolo in alto a sinistra e i due assi (pixel dell'immagine). */
const DISPLAY = {o: [76, 522], u: [619, 147], v: [-2, 222]};

/** `w` = larghezza disegnata; `pressed` 0..1; `led` = testo del display o null. */
export const buzzer = (ctx: Ctx, x: number, y: number, w: number, pressed: number, lit: number, led: string | null) => {
  const k = w / 1024;
  ctx.save();
  ctx.translate(x - w / 2, y - w / 2);
  ctx.scale(k, k);
  // ombra sul piano
  ctx.save();
  ctx.filter = 'blur(40px)';
  ctx.fillStyle = 'rgba(0,0,0,0.75)';
  ctx.beginPath();
  ctx.ellipse(470, 965, 480, 70, 0, 0, TAU);
  ctx.fill();
  ctx.restore();
  // base (tutto tranne la cupola)
  ctx.save();
  ctx.beginPath();
  ctx.rect(0, 0, 1024, 1024);
  domePath(ctx);
  ctx.clip('evenodd');
  ctx.drawImage(IMG.buzzer, 0, 0);
  ctx.restore();
  // cupola: scende quando viene premuta
  ctx.save();
  ctx.translate(0, 20 * pressed);
  ctx.beginPath();
  domePath(ctx);
  ctx.clip();
  ctx.drawImage(IMG.buzzer, 0, 0);
  ctx.restore();
  if (lit > 0) glow(ctx, 520, 280 + 20 * pressed, 430, 'rgba(255,40,40,1)', 0.55 * lit);
  if (led) ledOnDisplay(ctx, led, lit);
  ctx.restore();
};

const domePath = (ctx: Ctx) => {
  ctx.moveTo(200, 0);
  ctx.lineTo(845, 0);
  ctx.lineTo(845, 330);
  ctx.ellipse(522, 330, 323, 118, 0, 0, Math.PI);
  ctx.closePath();
};

const ledOnDisplay = (ctx: Ctx, text: string, lit: number) => {
  const {o, u, v} = DISPLAY;
  ctx.save();
  ctx.transform(u[0] / 620, u[1] / 620, v[0] / 222, v[1] / 222, o[0], o[1]);
  ctx.globalCompositeOperation = 'lighter';
  sevenSeg(ctx, text, 70, 42, 480, 138, 'rgba(255,42,42,1)', 0.6 + 0.4 * lit);
  ctx.restore();
};

// Segmenti accesi per ogni cifra: a b c d e f g
const SEG: Record<string, string> = {
  '0': 'abcdef', '1': 'bc', '2': 'abdeg', '3': 'abcdg', '4': 'bcfg', '5': 'acdfg', '6': 'acdefg', '7': 'abc', '8': 'abcdefg', '9': 'abcdfg', '-': 'g', ' ': '',
};

/** Testo in stile display a 7 segmenti (cifre e ':') dentro il riquadro dato. */
export const sevenSeg = (ctx: Ctx, text: string, x: number, y: number, w: number, h: number, color: string, glowAmt = 1) => {
  const chars = text.split('');
  const units = chars.reduce((a, ch) => a + (ch === ':' ? 0.35 : 1), 0);
  const cw = w / units;
  const dw = cw * 0.74;
  const t = dw * 0.17;
  let cx = x;
  const segs: [number, number, number, number][] = [];
  const dots: [number, number][] = [];
  for (const ch of chars) {
    if (ch === ':') {
      dots.push([cx + cw * 0.175, y + h * 0.32], [cx + cw * 0.175 - dw * 0.03, y + h * 0.7]);
      cx += cw * 0.35;
      continue;
    }
    const on = SEG[ch] ?? '';
    const l = cx + (cw - dw) / 2;
    const r = l + dw;
    const m = y + h / 2;
    const sk = dw * 0.12; // leggera inclinazione, come nei display veri
    const S: Record<string, [number, number, number, number]> = {
      a: [l + t * 0.7 + sk, y, r - t * 0.7 + sk, y],
      g: [l + t * 0.7 + sk / 2, m, r - t * 0.7 + sk / 2, m],
      d: [l + t * 0.7, y + h, r - t * 0.7, y + h],
      f: [l + sk, y + t * 0.7, l + sk / 2, m - t * 0.7],
      b: [r + sk, y + t * 0.7, r + sk / 2, m - t * 0.7],
      e: [l + sk / 2, m + t * 0.7, l, y + h - t * 0.7],
      c: [r + sk / 2, m + t * 0.7, r, y + h - t * 0.7],
    };
    for (const k of 'abcdefg') if (on.includes(k)) segs.push(S[k]);
    cx += cw;
  }
  const stroke = () => {
    ctx.beginPath();
    for (const s of segs) {
      ctx.moveTo(s[0], s[1]);
      ctx.lineTo(s[2], s[3]);
    }
    ctx.stroke();
  };
  ctx.save();
  ctx.lineCap = 'round';
  ctx.strokeStyle = color;
  ctx.fillStyle = color;
  // alone
  ctx.globalAlpha = 0.4 * glowAmt;
  ctx.lineWidth = t * 2.8;
  ctx.filter = `blur(${t * 0.9}px)`;
  stroke();
  ctx.filter = 'none';
  ctx.globalAlpha = 1;
  ctx.lineWidth = t;
  stroke();
  // nucleo più chiaro, come un LED acceso
  ctx.strokeStyle = 'rgba(255,215,205,0.55)';
  ctx.lineWidth = t * 0.3;
  stroke();
  for (const [dx, dy] of dots) {
    ctx.beginPath();
    ctx.arc(dx, dy, t * 0.62, 0, TAU);
    ctx.fill();
  }
  ctx.restore();
};

// ─── La bottiglia con la fontana di scintille ─────────────────────────────────
/** Bottiglia con la base in (x, y) e altezza h; `sparks` 0..1 accende la fontana. */
export const bottle = (ctx: Ctx, x: number, y: number, h: number, t: number, sparks: number, tilt = 0) => {
  const k = h / 1438; // altezza della bottiglia nell'immagine (y 50–1488)
  ctx.save();
  ctx.translate(x, y);
  ctx.rotate(tilt);
  ctx.save();
  ctx.filter = 'blur(30px)';
  ctx.fillStyle = 'rgba(0,0,0,0.7)';
  ctx.beginPath();
  ctx.ellipse(0, 6, h * 0.17, h * 0.03, 0, 0, TAU);
  ctx.fill();
  ctx.restore();
  ctx.drawImage(IMG.bottle, -512 * k, -1488 * k, 1024 * k, 1536 * k);
  // la luce delle scintille sul vetro
  if (sparks > 0) glow(ctx, 0, -h * 0.9, h * 0.6, 'rgba(255,170,110,1)', 0.4 * sparks * (0.85 + 0.15 * Math.sin(t * 40)));
  ctx.restore();
  if (sparks > 0) fountain(ctx, x + Math.sin(tilt) * h, y - Math.cos(tilt) * h, h * 0.5, t, sparks, tilt);
};

/** Fontana di scintille: ogni scintilla ha una traiettoria calcolata dal tempo, senza stato. */
export const fountain = (ctx: Ctx, x: number, y: number, size: number, t: number, amount: number, dir = 0) => {
  const N = 240;
  const life = 0.75;
  ctx.save();
  ctx.globalCompositeOperation = 'lighter';
  ctx.lineCap = 'round';
  glow(ctx, x, y, size * 0.4, 'rgba(255,230,180,1)', 0.85 * amount);
  for (let i = 0; i < N; i++) {
    // ogni scintilla rinasce a ogni giro con un ritardo proprio
    const phase = (((t / life + i / N) % 1) + 1) % 1;
    const cycle = Math.floor(t / life + i / N);
    const seed = i * 7.1 + cycle * 13.3;
    if (hash(seed) > amount * 0.95 + 0.05) continue;
    const age = phase * life;
    const a = -Math.PI / 2 + dir + (hash(seed * 2.9) - 0.5) * 0.75;
    const sp = size * (1.5 + hash(seed * 5.1) * 1.7);
    const g = size * 3.4;
    const px = (tt: number) => x + Math.cos(a) * sp * tt;
    const py = (tt: number) => y + Math.sin(a) * sp * tt + 0.5 * g * tt * tt;
    const fade = 1 - phase;
    const t0 = Math.max(0, age - 0.035);
    ctx.strokeStyle = `rgba(255,${200 + Math.round(55 * fade)},${120 + Math.round(120 * fade)},${0.95 * fade * amount})`;
    ctx.lineWidth = 1.5 + 2.3 * fade;
    ctx.beginPath();
    ctx.moveTo(px(t0), py(t0));
    ctx.lineTo(px(age), py(age));
    ctx.stroke();
  }
  ctx.restore();
};

// ─── Grana: rumore fine che unisce foto, oggetti generati e grafica ───────────
let noise: HTMLCanvasElement | null = null;
export const grain = (ctx: Ctx, t: number, amount = 0.07) => {
  if (!noise) {
    noise = document.createElement('canvas');
    noise.width = noise.height = 256;
    const g = noise.getContext('2d')!;
    const d = g.createImageData(256, 256);
    for (let i = 0; i < d.data.length; i += 4) {
      const v = Math.floor(hash(i * 0.37 + 11) * 255);
      d.data[i] = d.data[i + 1] = d.data[i + 2] = v;
      d.data[i + 3] = 255;
    }
    g.putImageData(d, 0, 0);
  }
  const f = Math.floor(t * 60);
  ctx.save();
  ctx.globalCompositeOperation = 'overlay';
  ctx.globalAlpha = amount;
  ctx.translate(-Math.floor(hash(f) * 256), -Math.floor(hash(f + 0.5) * 256));
  ctx.fillStyle = ctx.createPattern(noise, 'repeat')!;
  ctx.fillRect(0, 0, 1080 + 256, 1920 + 256);
  ctx.restore();
};
