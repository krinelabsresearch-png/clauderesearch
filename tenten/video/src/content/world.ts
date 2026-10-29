// La regia del contenuto sotto il vetro: quale foto, come si muove la camera,
// quando entrano moneta, buzzer e bottiglia e come si passa da un piano all'altro.
import {DURATION_FRAMES, FPS} from '../script';
import {glide} from '../ui/kit';
import {T, flash, timerText, timerValue} from '../timing';
import {clamp01, easeIn, easeInOut, lerp, prog, smooth} from '../theme';
import {PhotoRenderer, type Mode, type Shot} from '../photo/renderer';
import {bottle, buzzer, coin, glow, grain, haze, starFlare, type Ctx} from './objects';

const LAST = (DURATION_FRAMES - 1) / FPS;

/** Abbassamento della cupola del buzzer intorno all'istante T0. */
const pressCurve = (t: number, T0: number) => Math.exp(-Math.pow((t - T0) / 0.09, 2));

// ─── Le foto in sequenza: ogni tratto ha una camera che non si ferma mai ───────
type Seg = {from: number; shot: (t: number) => Shot; mode?: Mode; dur?: number};

const segments = (): Seg[] => {
  const S = T();
  return [
    {
      from: S.place - 0.05,
      shot: (t) => {
        // nasce dal lampo della moneta: la camera si allontana dalla folla
        const u = glide(t, S.place - 0.1);
        return {key: 'folla', cx: 0.56, cy: 0.38, zoom: lerp(1.75, 1.18, u) - 0.03 * Math.max(0, t - S.place), px: lerp(0.05, -0.03, prog(t, S.place, S.game)), py: 0.012, focus: 0.55, exposure: lerp(2.2, 1, smooth(prog(t, S.place - 0.1, S.place + 0.5)))};
      },
    },
    {
      from: S.pista,
      dur: 0.75,
      shot: (t) => ({key: 'pista', cx: 0.5, cy: 0.42, zoom: 1.16 + 0.04 * prog(t, S.pista, S.game + 0.6), px: lerp(-0.04, 0.03, prog(t, S.pista, S.game + 0.6)), py: 0.01, focus: 0.6}),
    },
    {
      from: S.game - 0.05,
      dur: 0.75,
      shot: (t) => {
        // la camera scivola verso il buzzer che lei tiene in mano, poi la foto va fuori fuoco
        const u = easeInOut(prog(t, S.game, S.rise + 0.3));
        const d = smooth(prog(t, S.rise, S.rise + 0.55));
        return {key: 'gioco', cx: lerp(0.52, 0.74, u), cy: lerp(0.5, 0.74, u), zoom: lerp(1.12, 1.75, u) + 0.25 * d, px: lerp(0.035, -0.02, u), py: 0.015, focus: 0.7, defocus: 4.8 * d, exposure: lerp(1, 0.42, d)};
      },
    },
    {
      from: S.bottle,
      mode: 'fade',
      dur: 0.5,
      shot: (t) => {
        // dietro la bottiglia il brindisi è sfocato; con "da festeggiare" va a fuoco e la camera scende sui calici
        const f = smooth(prog(t, S.party, S.party + 0.55));
        return {key: 'brindisi', cx: 0.5, cy: lerp(0.34, 0.46, f), zoom: lerp(1.3, 1.16, f), px: lerp(0.02, -0.02, prog(t, S.bottle, S.party + 0.7)), py: lerp(-0.02, 0.02, f), focus: 0.7, defocus: lerp(4.5, 0, f), exposure: lerp(0.45, 1, f), by: -260 * Math.sin(Math.PI * f) * (1 - f)};
      },
    },
    ...montage(S.party + 0.62, S.cta),
    {
      from: S.cta,
      dur: 0.7,
      shot: (t) => {
        const d = smooth(prog(t, S.cta + 0.2, S.cta + 1.4));
        return {key: 'pista', cx: 0.5, cy: 0.44, zoom: 1.22 - 0.05 * prog(t, S.cta, S.end), px: lerp(0.03, -0.03, prog(t, S.cta, S.end)), py: 0.01, focus: 0.6, defocus: 2.8 * d, exposure: lerp(1, 0.5, d)};
      },
    },
  ];
};

/** "Con i tuoi amici": tre foto legate da colpi di camera con scia di movimento. */
const montage = (a: number, b: number): Seg[] => {
  const keys: [string, number, number, number][] = [
    ['ragazze', 0.52, 0.42, 1],
    ['dj', 0.55, 0.4, -1],
    ['mc', 0.46, 0.4, 1],
  ];
  const step = (b - a) / keys.length;
  return keys.map(([key, cx, cy, dir], i) => {
    const t0 = a + i * step;
    return {
      from: t0,
      mode: i === 1 ? ('flare' as Mode) : ('depth' as Mode),
      dur: 0.32,
      shot: (t: number) => {
        const u = prog(t, t0, t0 + step + 0.4);
        // entra con una frustata laterale e poi rallenta
        const whip = Math.exp(-Math.max(0, t - t0) / 0.12);
        return {key, cx: cx + dir * (0.05 - 0.07 * u) + dir * 0.06 * whip, cy, zoom: 1.2 + 0.08 * u, px: dir * lerp(0.04, -0.03, u), py: 0.012, focus: 0.65, bx: dir * 120 * whip};
      },
    };
  });
};

let SEGS: Seg[] | null = null;
let photos: PhotoRenderer | null = null;

/** La foto del momento t (con l'eventuale passaggio alla successiva), o null. */
const photoAt = (t: number): {a: Shot; b: Shot | null; mix: number; mode: Mode} | null => {
  const segs = (SEGS ??= segments());
  let i = -1;
  while (i + 1 < segs.length && segs[i + 1].from <= t) i++;
  if (i < 0) return null;
  const cur = segs[i];
  const prev = segs[i - 1];
  const mix = clamp01((t - cur.from) / (cur.dur ?? 0.6));
  if (prev && mix < 1) return {a: prev.shot(t), b: cur.shot(t), mix: easeInOut(mix), mode: cur.mode ?? 'depth'};
  return {a: cur.shot(t), b: null, mix: 0, mode: 'fade'};
};

// ─── La moneta: arriva girando, si ferma di fronte sulla parola "un euro" ──────
const paintCoin = (ctx: Ctx, t: number, scale = 1, alpha = 1) => {
  const {land} = T();
  const theta = t < land ? 3.3 * Math.pow(land - t, 2) : 0.11 * Math.exp(-(t - land) / 0.32) * Math.sin((t - land) * 19);
  const y = 880 + 14 * Math.sin(t * 1.6);
  ctx.save();
  ctx.globalAlpha = alpha;
  coin(ctx, 540, y, 270 * scale, theta);
  ctx.restore();
  const g = t - land;
  if (g > -0.05 && scale < 1.4) starFlare(ctx, 540 - 150 * scale, y - 175 * scale, 130 * scale, Math.max(0, 1 - Math.abs(g - 0.1) / 0.45) * alpha, g * 0.6);
};

// ─── Pittura di un fotogramma ─────────────────────────────────────────────────
export const paintWorld = (ctx: Ctx, F: number) => {
  const t = F / FPS;
  const S = T();
  ctx.save();
  // scossa della camera quando il timer si ferma su 10:10
  const k = t - S.stop;
  if (k > 0 && k < 0.6) ctx.translate(Math.sin(k * 70) * 9 * Math.exp(-k / 0.13), Math.cos(k * 53) * 7 * Math.exp(-k / 0.13));

  haze(ctx, t);
  const ph = t > S.place - 0.1 ? photoAt(t) : null;
  if (ph) {
    photos ??= new PhotoRenderer(1080, 1920);
    const cv = photos.render(ph.a, ph.b, ph.mix, ph.mode);
    // in coda il locale si spegne e torna la foschia della moneta (loop)
    const a = 1 - smooth(prog(t, S.end, S.end + 0.6));
    if (a > 0.001) {
      ctx.save();
      ctx.globalAlpha = a;
      ctx.drawImage(cv, -12, -20, 1104, 1960);
      ctx.restore();
    }
  }

  // moneta: in apertura, poi corre verso la camera e diventa la luce del locale
  if (t < S.place + 0.35) {
    const r = easeIn(prog(t, S.rush, S.place + 0.3));
    if (r < 0.999) {
      for (let j = 3; j >= 0; j--) paintCoin(ctx, t - j * 0.006 * r, 1 + 4.2 * r * (1 - j * 0.05), (1 - r) * (j ? 0.25 : 1));
    }
    glow(ctx, 540, 880, 900 * r + 200, 'rgba(255,225,215,1)', Math.sin(Math.PI * r) * 1.2);
  }
  if (t > S.end) paintCoin(ctx, t - LAST, smooth(prog(t, S.end, LAST)), 1);

  // buzzer: sale dal basso sopra la foto sfocata, si preme, poi scende sotto la bottiglia
  if (t > S.rise - 0.1 && t < S.bottle + 0.9) {
    const up = glide(t, S.rise);
    const down = easeIn(prog(t, S.bottle, S.bottle + 0.6));
    const y = lerp(2350, 1170, up) + 1300 * down;
    const pr = Math.max(pressCurve(t, S.press), pressCurve(t, S.stop));
    const lit = Math.max(pr, t > S.press && t < S.stop ? 0.35 : 0, flash(t));
    buzzer(ctx, 540, y, 760, pr, lit, t < S.press - 0.1 ? null : timerText(timerValue(t)));
  }
  if (t > S.stop - 0.05) glow(ctx, 540, 720, 1100, 'rgba(255,60,60,1)', flash(t) * 0.9);

  // bottiglia con le scintille: sale, brilla, poi vola via in alto mentre la camera scende sul brindisi
  if (t > S.bottle && t < S.party + 0.7) {
    const up = glide(t, S.bottle + 0.1);
    const away = easeIn(prog(t, S.party, S.party + 0.6));
    const y = lerp(2500, 1440, up) - 1900 * away;
    const sp = smooth(prog(t, S.bottle + 0.35, S.bottle + 0.8));
    bottle(ctx, 540, y, 760, t, sp, Math.sin(t * 1.4) * 0.025);
  }
  ctx.restore();
  grain(ctx, t);
};
