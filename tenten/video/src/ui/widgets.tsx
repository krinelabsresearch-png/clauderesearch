// I controlli di vetro di ogni scena. Vivono su un unico piano fluttuante e,
// come nei controlli di iOS, si trasformano l'uno nell'altro invece di sparire:
// prezzo → TEN:TEN (+ capsula XO che si stacca come una goccia) → 1 drink = 1 giocata
// → timer → area VIP; alla fine la scheda con le informazioni e il pulsante Prenota.
import React, {useLayoutEffect, useRef} from 'react';
import type {Glass} from '../glass/renderer';
import {IMG} from '../assets';
import {sevenSeg} from '../content/objects';
import {T, W, flash, timerBlink, timerText, timerValue} from '../timing';
import {BRAND, WORDMARK, clamp01, easeInOut, lerp, prog, rgb, smooth} from '../theme';
import {REGULAR, Touch, cue, glide, life, matIn, matOut, onGlass, popScale, press, textWidth} from './kit';

type G = {x: number; y: number; w: number; h: number; r: number};
const mixG = (a: G, b: G, u: number): G => ({x: lerp(a.x, b.x, u), y: lerp(a.y, b.y, u), w: lerp(a.w, b.w, u), h: lerp(a.h, b.h, u), r: lerp(a.r, b.r, u)});
const fade = (m: number) => smooth((m - 0.35) / 0.5);
/** Il testo compare solo quando il vetro ha (quasi) la sua misura finale. */
const settle = (u: number) => smooth((u - 0.72) / 0.28);
const CREAM = BRAND.cream;

// ─── Numero che scorre come .numericText(): due colonne di cifre ───────────────
const priceAt = (t: number, t0: number) => lerp(20, 1, easeInOut(prog(t, t0, t0 + 0.65)));
const digitW = (size: number) => textWidth('0', size, 800) * 1.02;
const digitsWidth = (v: number, size: number) => digitW(size) * (1 + clamp01(v - 9));

const Digits: React.FC<{v: number; size: number}> = ({v, size}) => {
  const H = size * 1.12;
  const dw = digitW(size);
  // la colonna delle decine scorre solo nell'ultimo tratto, poi si richiude (da 10 a 9)
  const tens = Math.floor(v / 10) + Math.max(0, (v % 10) - 9);
  const col = (pos: number, w: number, op = 1) => (
    <span style={{display: 'inline-block', width: w, height: H, overflow: 'hidden', verticalAlign: 'bottom', opacity: op}}>
      <span style={{display: 'block', transform: `translateY(${-(((pos % 10) + 10) % 10) * H}px)`}}>
        {[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0].map((d, i) => (
          <span key={i} style={{display: 'block', height: H, lineHeight: `${H}px`, textAlign: 'center'}}>
            {d}
          </span>
        ))}
      </span>
    </span>
  );
  return (
    <span style={{display: 'inline-flex', fontSize: size, fontWeight: 800, fontVariantNumeric: 'tabular-nums', letterSpacing: '-0.03em', whiteSpace: 'nowrap'}}>
      {col(tens, dw * clamp01(v - 9), clamp01(v - 9))}
      {col(v, dw)}
    </span>
  );
};

// ─── Geometrie ────────────────────────────────────────────────────────────────
const PRICE_Y = 1290;
const priceGeom = (t: number): G => {
  const v = priceAt(t, W().roll);
  const w = (textWidth('Ingresso', 34, 600) + 22 + digitsWidth(v, 80) + 8 + textWidth('€', 64, 700)) / 2 + 46;
  return {x: 540, y: PRICE_Y, w, h: 64, r: 64};
};
const TITLE: G = {x: 540, y: 860, w: 396, h: 150, r: 74};
const locGeom = (): G => ({x: 540, y: 1092, w: (100 + 18 + textWidth('Via Verdi 59R', 38, 700)) / 2 + 40, h: 52, r: 52});
const CHIP_TEXT = '1 drink = 1 giocata';
const CHIP_Y = 1310;
const chipGeom = (): G => ({x: 540, y: CHIP_Y, w: (58 + 16 + textWidth(CHIP_TEXT, 44, 700)) / 2 + 42, h: 56, r: 56});
const TIMER: G = {x: 540, y: 610, w: 300, h: 104, r: 104};
const VIP_TEXT = 'Bottiglia in area VIP';
const VIP_Y = 1560;
const vipGeom = (): G => ({x: 540, y: VIP_Y, w: (44 + 14 + textWidth(VIP_TEXT, 40, 700)) / 2 + 40, h: 50, r: 50});
const CARD = {y: 990, w: 424, h: 318};
const BTN: G = {x: 540, y: 1400, w: 150, h: 54, r: 54};

/** Il vetro principale che cambia forma: prezzo → titolo → chip → timer → VIP. */
const mainGlass = (t: number) => {
  const w = W();
  const m = Math.min(matIn(t, w.price), matOut(t, w.vipOut, 0.35));
  const a = glide(t, w.title);
  const b = glide(t, w.chip);
  const c = glide(t, w.timer);
  const d = glide(t, w.vip);
  let g = priceGeom(t);
  g = mixG(g, TITLE, a);
  g = mixG(g, chipGeom(), b);
  g = mixG(g, TIMER, c);
  g = mixG(g, vipGeom(), d);
  return {g, m, a, b, c, d};
};

/** La capsula XO: nasce dal titolo, si stacca come una goccia, poi rientra nel chip. */
const locGlass = (t: number) => {
  const w = W();
  const e = glide(t, w.loc);
  const b = glide(t, w.chip);
  const from: G = {x: 540, y: TITLE.y + 90, w: 40, h: 40, r: 40};
  const g = mixG(mixG(from, locGeom(), e), chipGeom(), b);
  return {g, m: t < w.loc ? 0 : Math.min(1, e * 1.6) * (1 - smooth(prog(b, 0.85, 1))), e, b};
};

const glassTimeline = (t: number): Glass[] => {
  const out: Glass[] = [];
  const w = W();
  const M = mainGlass(t);
  if (M.m > 0.001) {
    const pr = press(t, T().stop);
    const pPrice = press(t, cue('hook', 'euro') + 0.35);
    const timerOn = M.c * (1 - M.d);
    const s = popScale(t, w.price) * (timerOn > 0.5 ? pr.scale : M.a < 0.5 ? pPrice.scale : 1);
    out.push({
      ...REGULAR,
      ...M.g,
      w: M.g.w * s,
      h: M.g.h * s,
      r: M.g.r * s,
      k: 90,
      mat: M.m,
      dim: lerp(0.2, 0.62, timerOn),
      frost: lerp(0.6, 0.7, timerOn),
      tint: rgb(BRAND.red),
      tintAmt: 0.08 + 0.25 * flash(t) * timerOn + 0.1 * pPrice.glow * (1 - M.a),
      glow: Math.max(pr.glow * timerOn, pPrice.glow * (1 - M.a)),
      gx: M.g.x - 60,
      gy: M.g.y - 30,
    });
  }
  const L = locGlass(t);
  if (L.m > 0.001) out.push({...REGULAR, ...L.g, k: lerp(110, 12, smooth(prog(L.e, 0.35, 0.95))) + 90 * L.b, mat: Math.min(L.m, M.m), dim: 0.22, frost: 0.6});
  // scheda finale + pulsante Prenota (uniti come una goccia quando il pulsante nasce)
  const mc = life(t, w.card, w.end);
  if (mc > 0.001) {
    const s = popScale(t, w.card) * (1 + 0.02 * Math.exp(-Math.pow((t - w.see - 0.2) / 0.2, 2)));
    out.push({...REGULAR, x: 540, y: CARD.y, w: CARD.w * s, h: CARD.h * s, r: 64 * s, k: 70, mat: mc, dim: 0.34, frost: 0.68, tint: rgb(BRAND.red), tintAmt: 0.06});
    const mb = life(t, w.btn, w.end);
    if (mb > 0.001) {
      const e = glide(t, w.btn);
      const pr = press(t, w.tap);
      const g = mixG({x: 540, y: CARD.y + CARD.h - 40, w: 60, h: 30, r: 30}, BTN, e);
      const tapped = smooth(prog(t, w.tap, w.tap + 0.3));
      out.push({...REGULAR, ...g, w: g.w * pr.scale, h: g.h * pr.scale, r: g.r * pr.scale, k: lerp(80, 14, e), mat: Math.min(mb, mc), dim: 0.2, tint: rgb(BRAND.red), tintAmt: 0.12 + 0.45 * tapped, glow: pr.glow, gx: BTN.x - 20, gy: BTN.y - 10});
    }
  }
  return out;
};

// ─── Testo e simboli sopra il vetro ───────────────────────────────────────────
const XoLogo: React.FC<{h: number}> = ({h}) => <img src={IMG.xo.src} style={{height: h, width: (h * IMG.xo.naturalWidth) / IMG.xo.naturalHeight, display: 'block'}} />;

const Cocktail: React.FC<{size: number}> = ({size}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke="#fff" strokeWidth={2} strokeLinecap="round" strokeLinejoin="round">
    <path d="M4 4h16l-8 9z" fill="rgba(229,35,44,0.85)" />
    <path d="M12 13v7M8 20h8M15.5 4l2.5-2.5" />
  </svg>
);
const Sparkle: React.FC<{size: number}> = ({size}) => (
  <svg width={size} height={size} viewBox="0 0 24 24">
    <path d="M12 1.5c.7 4.8 2.7 7.7 9.5 10.5-6.8 2.8-8.8 5.7-9.5 10.5-.7-4.8-2.7-7.7-9.5-10.5 6.8-2.8 8.8-5.7 9.5-10.5z" fill={CREAM} />
  </svg>
);

/** Display a LED disegnato in un canvas: nitido sopra il vetro. */
const Led: React.FC<{text: string; x: number; y: number; w: number; h: number; alpha: number}> = ({text, x, y, w, h, alpha}) => {
  const ref = useRef<HTMLCanvasElement>(null);
  useLayoutEffect(() => {
    const c = ref.current!;
    const g = c.getContext('2d')!;
    g.clearRect(0, 0, c.width, c.height);
    sevenSeg(g, text, 26, 20, c.width - 52, c.height - 40, BRAND.led, 1);
  });
  return <canvas ref={ref} width={Math.round(w)} height={Math.round(h)} style={{position: 'absolute', left: x - w / 2, top: y - h / 2, width: w, height: h, opacity: alpha}} />;
};

const Row: React.FC<{y: number; h?: number; gap: number; opacity: number; scale?: number; children: React.ReactNode}> = ({y, h = 80, gap, opacity, scale = 1, children}) => (
  <div style={{position: 'absolute', left: 0, right: 0, top: y - h / 2, height: h, display: 'flex', alignItems: 'center', justifyContent: 'center', gap, opacity, transform: `scale(${scale})`}}>{children}</div>
);

const MainUI: React.FC<{t: number}> = ({t}) => {
  const w = W();
  const M = mainGlass(t);
  if (M.m <= 0.02) return null;
  const op = fade(M.m);
  const price = op * (1 - smooth(M.a / 0.3));
  const title = op * settle(M.a) * (1 - smooth(M.b / 0.3));
  const chip = op * settle(M.b) * (1 - smooth(M.c / 0.3));
  const timer = op * settle(M.c) * (1 - smooth(M.d / 0.3));
  const vip = op * settle(M.d);
  const pr = press(t, T().stop);
  return (
    <>
      {price > 0.01 && (
        <Row y={PRICE_Y} h={100} gap={22} opacity={price} scale={popScale(t, w.price) * press(t, cue('hook', 'euro') + 0.35).scale}>
          <span style={{...onGlass, fontSize: 34, fontWeight: 600, color: 'rgba(255,255,255,0.78)'}}>Ingresso</span>
          <span style={{...onGlass, display: 'flex', alignItems: 'baseline', gap: 8}}>
            <Digits v={priceAt(t, w.roll)} size={80} />
            <span style={{fontSize: 64, fontWeight: 700}}>€</span>
          </span>
        </Row>
      )}
      {title > 0.01 && (
        <div style={{position: 'absolute', left: 0, right: 0, top: TITLE.y - 120, height: 240, lineHeight: '240px', textAlign: 'center', fontFamily: WORDMARK, fontSize: 212, color: CREAM, letterSpacing: '0.01em', opacity: title, transform: `translateY(${(1 - title) * 14}px)`, textShadow: '0 4px 30px rgba(229,35,44,0.55)'}}>
          TEN:TEN
        </div>
      )}
      {chip > 0.01 && (
        <Row y={CHIP_Y} gap={16} opacity={chip}>
          <Cocktail size={58} />
          <span style={{...onGlass, fontSize: 44, fontWeight: 700, letterSpacing: '-0.01em'}}>{CHIP_TEXT}</span>
        </Row>
      )}
      {timer > 0.01 && <Led text={timerText(timerValue(t))} x={TIMER.x} y={TIMER.y} w={(TIMER.w * 2 - 40) * pr.scale} h={(TIMER.h * 2 - 30) * pr.scale} alpha={timer * timerBlink(t)} />}
      {vip > 0.01 && (
        <Row y={VIP_Y} gap={14} opacity={vip}>
          <Sparkle size={44} />
          <span style={{...onGlass, fontSize: 40, fontWeight: 700}}>{VIP_TEXT}</span>
        </Row>
      )}
    </>
  );
};

const LocUI: React.FC<{t: number}> = ({t}) => {
  const L = locGlass(t);
  const a = Math.min(fade(L.m), settle(L.e)) * (1 - smooth(L.b / 0.3));
  if (a <= 0.01) return null;
  return (
    <Row y={locGeom().y} gap={18} opacity={a}>
      <XoLogo h={50} />
      <span style={{...onGlass, fontSize: 38, fontWeight: 700}}>Via Verdi 59R</span>
    </Row>
  );
};

const CardUI: React.FC<{t: number}> = ({t}) => {
  const w = W();
  const mc = life(t, w.card, w.end);
  if (mc <= 0.02) return null;
  const s = popScale(t, w.card);
  const a = fade(mc) * smooth(prog(t, w.card + 0.15, w.card + 0.45));
  const mb = life(t, w.btn, w.end);
  return (
    <>
      <div style={{position: 'absolute', left: 540 - CARD.w, top: CARD.y - CARD.h, width: CARD.w * 2, height: CARD.h * 2, opacity: a, transform: `scale(${s})`, display: 'flex', flexDirection: 'column', alignItems: 'center'}}>
        <div style={{fontFamily: WORDMARK, fontSize: 150, lineHeight: '170px', marginTop: 34, color: CREAM, letterSpacing: '0.01em', textShadow: '0 4px 26px rgba(229,35,44,0.5)'}}>TEN:TEN</div>
        <div style={{...onGlass, fontSize: 30, fontWeight: 700, letterSpacing: '0.08em', textTransform: 'uppercase', color: 'rgba(255,255,255,0.86)', marginTop: 4}}>Ogni venerdì · 23.30–5.00</div>
        <div style={{display: 'flex', alignItems: 'center', gap: 24, marginTop: 26}}>
          <span style={{...onGlass, display: 'flex', alignItems: 'baseline', gap: 8}}>
            <Digits v={1} size={104} />
            <span style={{fontSize: 80, fontWeight: 700}}>€</span>
          </span>
          <span style={{...onGlass, fontSize: 30, fontWeight: 600, lineHeight: '38px', color: 'rgba(255,255,255,0.86)', textAlign: 'left'}}>
            con prenotazione
            <br />
            entro le 00.30
          </span>
        </div>
        <div style={{width: CARD.w * 2 - 120, height: 2, background: 'rgba(255,255,255,0.18)', marginTop: 28}} />
        <div style={{display: 'flex', alignItems: 'center', gap: 16, marginTop: 26}}>
          <XoLogo h={44} />
          <span style={{...onGlass, fontSize: 32, fontWeight: 700}}>Via Verdi 59R, Firenze</span>
        </div>
      </div>
      {mb > 0.02 && (
        <Row y={BTN.y} h={60} gap={10} opacity={fade(mb) * settle(glide(t, w.btn))} scale={press(t, w.tap).scale}>
          <span style={{...onGlass, fontSize: 36, fontWeight: 700}}>Prenota</span>
        </Row>
      )}
      <Touch t={t} T={w.tap} x={BTN.x + 30} y={BTN.y + 12} />
    </>
  );
};

/** Il dito che preme il buzzer: avvio e stop del timer. */
const BuzzerTouches: React.FC<{t: number}> = ({t}) => {
  const S = T();
  return (
    <>
      <Touch t={t} T={S.press} x={560} y={930} />
      <Touch t={t} T={S.stop} x={560} y={930} />
    </>
  );
};

export const widgetsGlass = (t: number): Glass[] => glassTimeline(t);

export const WidgetsOverlay: React.FC<{t: number}> = ({t}) => (
  <>
    <MainUI t={t} />
    <LocUI t={t} />
    <CardUI t={t} />
    <BuzzerTouches t={t} />
  </>
);

export const lightAt = (t: number): [number, number] => {
  // inclinazione simulata del telefono: i riflessi scorrono lentamente sui bordi
  const a = -2.2 + 0.42 * Math.sin(t * 0.55) + 0.12 * Math.sin(t * 1.7);
  return [Math.cos(a), Math.sin(a)];
};
