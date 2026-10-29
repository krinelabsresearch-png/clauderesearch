// I controlli di vetro di ogni scena. Vivono su un unico piano fluttuante e,
// come nei controlli di iOS, si trasformano l'uno nell'altro invece di sparire.
import React from 'react';
import type {Glass} from '../glass/renderer';
import {PRISM, STOMA, SUN} from '../content/shots';
import {COL, DISPLAY, clamp01, lerp, prog, rgb, smooth} from '../theme';
import {BookmarkIcon, CheckIcon, CO2Icon, DropIcon, MolSVG, ShareIcon, SunIcon} from './icons';
import {CLEAR, Pill, REGULAR, Touch, bounce, cue, glide, life, matIn, matOut, onGlass, pillGlass, popScale, press, sceneEnd, sceneStart, textWidth} from './kit';

type G = Required<Pick<Glass, 'x' | 'y' | 'w' | 'h' | 'r'>>;
const mixG = (a: G, b: G, u: number): G => ({x: lerp(a.x, b.x, u), y: lerp(a.y, b.y, u), w: lerp(a.w, b.w, u), h: lerp(a.h, b.h, u), r: lerp(a.r, b.r, u)});
const circle = (x: number, y: number, r: number): G => ({x, y, w: r, h: r, r});
const box = (x: number, y: number, w: number, h: number, r: number): G => ({x, y, w, h, r});
const fade = (m: number) => smooth((m - 0.35) / 0.5);

// ─── 1. Badge O₂ → titolo ─────────────────────────────────────────────────────
const BADGE = circle(790, 700, 100);
const TITLE = box(540, 1040, 430, 168, 64);
const hookT = () => ({avanzo: cue('hook', 'avanzo'), name: cue('hook', 'name') - 0.05, out: cue('hook', 'leaf') - 0.05});

const hookGlass = (t: number): Glass[] => {
  const T = hookT();
  const m = Math.min(matIn(t, 0.3), matOut(t, T.out, 0.35));
  if (m <= 0.001) return [];
  const u = glide(t, T.name);
  const g = mixG({...BADGE, y: BADGE.y + Math.sin(t * 1.6) * 6}, TITLE, u);
  const pr = press(t, T.avanzo);
  const s = popScale(t, 0.3) * pr.scale;
  return [{...REGULAR, ...g, w: g.w * s, h: g.h * s, r: g.r * s, mat: m, tint: rgb(COL.leaf), tintAmt: 0.1 * (1 - u), glow: pr.glow, gx: g.x - 30, gy: g.y - 40}];
};

const HookUI: React.FC<{t: number}> = ({t}) => {
  const T = hookT();
  const m = Math.min(matIn(t, 0.3), matOut(t, T.out, 0.35));
  if (m <= 0.02) return null;
  const u = glide(t, T.name);
  const g = mixG(BADGE, TITLE, u);
  const o2 = fade(m) * (1 - smooth(u / 0.35));
  const title = fade(m) * smooth((u - 0.72) / 0.28);
  const pr = press(t, T.avanzo);
  return (
    <>
      {o2 > 0.01 && (
        <div style={{...onGlass, position: 'absolute', left: g.x - 150, top: g.y + Math.sin(t * 1.6) * 6 - 60, width: 300, height: 120, lineHeight: '120px', textAlign: 'center', fontSize: 92, fontWeight: 800, letterSpacing: '-0.03em', opacity: o2, transform: `scale(${popScale(t, 0.3) * pr.scale})`}}>
          O₂
        </div>
      )}
      {title > 0.01 && (
        <div style={{position: 'absolute', left: TITLE.x - 430, top: TITLE.y - 103, width: 860, textAlign: 'center', opacity: title, transform: `translateY(${(1 - title) * 16}px)`, filter: title < 0.99 ? `blur(${(1 - title) * 6}px)` : undefined}}>
          <div style={{...onGlass, fontFamily: DISPLAY, fontSize: 104, lineHeight: '124px', fontWeight: 800, letterSpacing: '-0.035em'}}>Fotosintesi</div>
          <div style={{...onGlass, fontSize: 56, lineHeight: '70px', fontWeight: 600, letterSpacing: '-0.02em', color: 'rgba(255,255,255,0.8)'}}>clorofilliana</div>
        </div>
      )}
    </>
  );
};

// ─── 2. Tre ingredienti: una capsula che si divide in tre pulsanti ────────────
const BTN_R = 88;
const BUTTONS = [
  {x: SUN.x, y: SUN.y, Icon: SunIcon, label: 'Luce', cueName: 'luce', color: COL.amber},
  {x: 300, y: 1218, Icon: DropIcon, label: 'Acqua', cueName: 'acqua', color: COL.water},
  {x: 280, y: 760, Icon: CO2Icon, label: 'CO₂', cueName: 'co2', color: '#E5E5EA'},
];
const ingrT = () => {
  const i0 = cue('ingr', 'ingr');
  return {i0, split: i0 + 0.75, taps: BUTTONS.map((b) => cue('ingr', b.cueName) + 0.05), pathStart: sceneStart('path'), up: cue('path', 'up'), inn: cue('path', 'in')};
};
const CAPSULE_TEXT = '3 ingredienti';
const capsule = () => box(540, 1000, textWidth(CAPSULE_TEXT, 46, 700) / 2 + 54, 70, 70);
const RADICI = (b: (typeof BUTTONS)[number]) => pillGlass(b.x, b.y, 'Radici', 1);

/** Stato di ogni pulsante al tempo t. */
const buttonState = (t: number, i: number) => {
  const T = ingrT();
  const b = BUTTONS[i];
  const u = glide(t, T.split + i * 0.05);
  const pr = press(t, T.taps[i]);
  // luce che si irradia ai pulsanti vicini quando se ne tocca uno
  let near = 0;
  T.taps.forEach((tp, j) => {
    if (j !== i && t >= tp) near = Math.max(near, 0.35 * Math.exp(-(t - tp) / 0.42));
  });
  const out =
    i === 0 ? matOut(t, T.pathStart, 0.35) : i === 2 ? matOut(t, T.inn + 0.4, 0.35) : matOut(t, T.inn + 0.6, 0.35);
  const toPill = i === 1 ? glide(t, T.up - 0.1) : 0;
  return {u, pr, near, out, toPill, b, tinted: smooth(prog(t, T.taps[i], T.taps[i] + 0.4))};
};

const ingrGlass = (t: number): Glass[] => {
  const T = ingrT();
  const out: Glass[] = [];
  const mc = Math.min(matIn(t, T.i0 - 0.05), 1);
  if (t < T.i0 - 0.05 || t > T.inn + 1.2) return out;
  const cap = capsule();
  const split = glide(t, T.split);
  if (split < 0.98) {
    const sc = 1 - split;
    out.push({...REGULAR, ...cap, w: cap.w * sc, h: cap.h * (0.6 + 0.4 * sc), r: cap.r * (0.6 + 0.4 * sc), k: 70, mat: mc * popScale(t, T.i0 - 0.05)});
  }
  BUTTONS.forEach((_, i) => {
    const s = buttonState(t, i);
    if (s.u <= 0.001 || s.out <= 0.001) return;
    const from = circle(cap.x, cap.y, 30);
    let g = mixG(from, circle(s.b.x, s.b.y, BTN_R), s.u);
    if (s.toPill > 0) {
      const p = RADICI(s.b);
      g = mixG(g, {x: p.x, y: p.y, w: p.w, h: p.h!, r: p.r!}, s.toPill);
    }
    const sc = s.pr.scale;
    out.push({
      ...REGULAR,
      ...g,
      w: g.w * sc,
      h: g.h * sc,
      r: g.r * sc,
      k: 70 * (1 - s.u) + 8,
      mat: Math.min(mc, s.out),
      frost: i === 0 ? 0.12 : 0.5,
      tint: rgb(s.b.color),
      tintAmt: 0.22 * s.tinted * (1 - s.toPill),
      glow: Math.max(s.pr.glow, s.near),
      gx: s.pr.glow >= s.near ? g.x - 22 : g.x,
      gy: s.pr.glow >= s.near ? g.y - 26 : g.y - 200,
    });
  });
  return out;
};

const IngrUI: React.FC<{t: number}> = ({t}) => {
  const T = ingrT();
  if (t < T.i0 - 0.05 || t > T.inn + 1.2) return null;
  const split = glide(t, T.split);
  const cap = capsule();
  const mc = matIn(t, T.i0 - 0.05);
  return (
    <>
      {split < 0.5 && (
        <div style={{...onGlass, position: 'absolute', left: cap.x - 300, top: cap.y - 35, width: 600, height: 70, lineHeight: '70px', textAlign: 'center', fontSize: 46, fontWeight: 700, letterSpacing: '-0.015em', opacity: fade(mc) * (1 - smooth(split / 0.4))}}>
          {CAPSULE_TEXT}
        </div>
      )}
      {BUTTONS.map((_, i) => {
        const s = buttonState(t, i);
        const vis = Math.min(fade(Math.min(1, s.u * 1.2)), s.out) * (1 - smooth(s.toPill / 0.5));
        const x = lerp(cap.x, s.b.x, s.u);
        const y = lerp(cap.y, s.b.y, s.u);
        return (
          <React.Fragment key={i}>
            {vis > 0.01 && (
              <>
                <div style={{position: 'absolute', left: x - 40, top: y - 40, width: 80, height: 80, opacity: vis, transform: `scale(${s.pr.scale * (0.6 + 0.4 * s.u)})`, filter: 'drop-shadow(0 2px 8px rgba(0,0,0,0.3))'}}>
                  <s.b.Icon size={80} color={s.tinted > 0.5 ? s.b.color : '#FFFFFF'} />
                </div>
                <div style={{...onGlass, position: 'absolute', left: x - 150, top: y + BTN_R + 10, width: 300, textAlign: 'center', fontSize: 32, fontWeight: 700, opacity: vis * smooth(s.u * 1.4 - 0.4)}}>
                  {s.b.label}
                </div>
              </>
            )}
            <Touch t={t} T={T.taps[i]} x={s.b.x + 10} y={s.b.y + 14} />
          </React.Fragment>
        );
      })}
      {(() => {
        const s = buttonState(t, 1);
        return <Pill x={s.b.x} y={s.b.y} text="Radici" m={smooth((s.toPill - 0.4) / 0.6) * s.out} />;
      })()}
    </>
  );
};

// ─── 3. La lente sugli stomi ──────────────────────────────────────────────────
const stomaT = () => ({in: cue('path', 'stomi') - 0.75, label: cue('path', 'stomi') - 0.05, out: sceneStart('chloro') + 0.05});

const stomaGlass = (t: number): Glass[] => {
  const T = stomaT();
  const m = life(t, T.in, T.out);
  if (m <= 0.001) return [];
  const s = popScale(t, T.in);
  const lens: Glass = {...CLEAR, x: STOMA.x, y: STOMA.y + Math.sin(t * 1.4) * 5, w: 180 * s, h: 180 * s, r: 180 * s, mag: 0.85, refr: 1.4, disp: 0.05, mat: m, k: 0};
  const ml = life(t, T.label, T.out);
  return ml > 0.001 ? [lens, pillGlass(STOMA.x, STOMA.y + 250, 'Stoma', ml, popScale(t, T.label))] : [lens];
};

const StomaUI: React.FC<{t: number}> = ({t}) => {
  const T = stomaT();
  const ml = life(t, T.label, T.out);
  return <Pill x={STOMA.x} y={STOMA.y + 250} text="Stoma" m={ml} s={popScale(t, T.label)} />;
};

// ─── 4. Cellule → Cloroplasto → grafico della clorofilla; il prisma ───────────
const CARD = box(540, 1200, 432, 166, 50);
const PILL_POS = {x: 540, y: 1330};
const chloroT = () => ({
  in: sceneStart('chloro') + 0.4,
  rename: cue('chloro', 'chloro'),
  prism: cue('chloro', 'beam') - 0.35,
  card: cue('chloro', 'absorb') - 0.3,
  green: cue('chloro', 'green'),
  out: sceneStart('light') - 0.25,
});

const pillLabel = (t: number) => (t < chloroT().rename + 0.08 ? 'Cellule' : 'Cloroplasto');
const pillDims = (t: number): G => {
  const T = chloroT();
  const a = pillGlass(PILL_POS.x, PILL_POS.y, 'Cellule', 1);
  const b = pillGlass(PILL_POS.x, PILL_POS.y, 'Cloroplasto', 1);
  const u = bounce(t, T.rename);
  return {x: PILL_POS.x, y: PILL_POS.y, w: lerp(a.w, b.w, u), h: a.h!, r: a.r!};
};

const chloroGlass = (t: number): Glass[] => {
  const T = chloroT();
  const out: Glass[] = [];
  const m = life(t, T.in, T.out);
  if (m > 0.001) {
    const u = glide(t, T.card);
    const g = mixG(pillDims(t), CARD, u);
    out.push({...REGULAR, ...g, mat: m, dim: lerp(0.3, 0.34, u), frost: lerp(0.55, 0.7, u), k: 0});
  }
  const mp = life(t, T.prism, T.out);
  if (mp > 0.001) {
    const s = popScale(t, T.prism);
    out.push({...CLEAR, x: PRISM.x, y: PRISM.y, w: PRISM.r * s, kind: 'tri', r: 18, rot: -0.35 * (1 - bounce(t, T.prism)), refr: 1.9, disp: 0.26, mat: mp, k: 0, tint: [1, 1, 1], tintAmt: 0.04});
  }
  return out;
};

// Assorbimento della clorofilla (a + b) tra 400 e 700 nm: picchi nel blu e nel rosso, minimo nel verde.
// Picco a 430 nm (clorofilla a) con la spalla a 455 nm (clorofilla b); nel rosso 642 e 663 nm.
const absorb = (nm: number) => {
  const g = (c: number, s: number) => Math.exp(-Math.pow((nm - c) / s, 2));
  return 0.05 + 0.9 * g(430, 20) + 0.55 * g(455, 12) + 0.35 * g(642, 10) + 0.75 * g(663, 11);
};

// la curva parte 58 px sotto il titolo: lo spazio per le etichette dei picchi
const SVG_TOP = 58;

const SpectrumChart: React.FC<{t: number; show: number}> = ({t, show}) => {
  const T = chloroT();
  const W = 740;
  const Hc = 150;
  const x = (nm: number) => ((nm - 400) / 300) * W;
  const reveal = smooth(prog(t, T.card + 0.35, T.card + 1.1));
  const pts: string[] = [];
  for (let nm = 400; nm <= 400 + 300 * reveal; nm += 2) pts.push(`${x(nm).toFixed(1)},${(Hc - absorb(nm) * (Hc - 12)).toFixed(1)}`);
  const area = pts.length > 1 ? `M0,${Hc} L${pts.join(' L')} L${pts[pts.length - 1].split(',')[0]},${Hc} Z` : '';
  const green = smooth(prog(t, T.green, T.green + 0.5));
  const peaks = smooth(prog(t, T.card + 0.9, T.card + 1.3));
  return (
    <div style={{position: 'absolute', left: CARD.x - W / 2, top: CARD.y - 128, width: W, opacity: show}}>
      <div style={{...onGlass, fontSize: 28, lineHeight: '34px', height: 34, fontWeight: 700, letterSpacing: '-0.01em', marginBottom: SVG_TOP - 34}}>
        Luce assorbita dalla clorofilla
      </div>
      <svg width={W} height={Hc + 46} style={{overflow: 'visible'}}>
        <defs>
          <linearGradient id="spec" x1="0" x2="1">
            <stop offset="0" stopColor="#8B5CF6" />
            <stop offset="0.17" stopColor="#3B82F6" />
            <stop offset="0.3" stopColor="#22D3EE" />
            <stop offset="0.43" stopColor="#22C55E" />
            <stop offset="0.57" stopColor="#FACC15" />
            <stop offset="0.7" stopColor="#FB923C" />
            <stop offset="0.85" stopColor="#EF4444" />
            <stop offset="1" stopColor="#B91C1C" />
          </linearGradient>
          <linearGradient id="area" x1="0" x2="0" y1="0" y2="1">
            <stop offset="0" stopColor="#fff" stopOpacity="0.45" />
            <stop offset="1" stopColor="#fff" stopOpacity="0.04" />
          </linearGradient>
        </defs>
        {area && <path d={area} fill="url(#area)" />}
        {pts.length > 1 && <polyline points={pts.join(' ')} fill="none" stroke="#fff" strokeWidth={4} strokeLinejoin="round" />}
        <rect x={0} y={Hc + 6} width={W} height={14} rx={7} fill="url(#spec)" />
        <rect x={x(500)} y={Hc + 2} width={x(580) - x(500)} height={22} rx={11} fill="none" stroke="#fff" strokeWidth={3} opacity={green} />
        {[430, 662].map((nm) => (
          <circle key={nm} cx={x(nm)} cy={Hc - absorb(nm) * (Hc - 12)} r={9 * peaks} fill={nm < 500 ? '#3B82F6' : '#EF4444'} stroke="#fff" strokeWidth={3} />
        ))}
        {[['400 nm', 400, 'start'], ['550', 550, 'middle'], ['700 nm', 700, 'end']].map(([l, nm, a]) => (
          <text key={l as string} x={x(nm as number)} y={Hc + 44} fill="rgba(255,255,255,0.75)" fontFamily="Inter" fontSize={20} fontWeight={600} textAnchor={a as 'start'}>
            {l}
          </text>
        ))}
      </svg>
      {/* etichette di fianco ai picchi, mai sopra la curva */}
      <div style={{position: 'absolute', left: x(430) + 22, top: SVG_TOP + (Hc - absorb(430) * (Hc - 12)) - 27, ...onGlass, fontSize: 22, lineHeight: '26px', fontWeight: 700, opacity: peaks, color: '#9CC2FF'}}>assorbe il blu</div>
      <div style={{position: 'absolute', right: W - x(663) + 22, top: SVG_TOP + (Hc - absorb(663) * (Hc - 12)) - 27, textAlign: 'right', ...onGlass, fontSize: 22, lineHeight: '26px', fontWeight: 700, opacity: peaks, color: '#FFA3A3'}}>assorbe il rosso</div>
      <div style={{position: 'absolute', left: x(540) - 70, top: SVG_TOP + 76, width: 140, textAlign: 'center', ...onGlass, fontSize: 24, fontWeight: 800, color: '#7CFF9B', opacity: green}}>riflette</div>
    </div>
  );
};

const ChloroUI: React.FC<{t: number}> = ({t}) => {
  const T = chloroT();
  const m = life(t, T.in, T.out);
  if (m <= 0.02) return null;
  const u = glide(t, T.card);
  const label = pillLabel(t);
  const swap = Math.abs(t - T.rename - 0.08) < 0.12 ? 1 - Math.abs(t - T.rename - 0.08) / 0.12 : 0;
  return (
    <>
      {u < 0.5 && (
        <div style={{...onGlass, position: 'absolute', left: PILL_POS.x - 300, top: PILL_POS.y - 30, width: 600, height: 60, lineHeight: '60px', textAlign: 'center', fontSize: 34, fontWeight: 700, opacity: fade(m) * (1 - smooth(u / 0.35)) * (1 - 0.8 * swap), filter: swap > 0 ? `blur(${swap * 6}px)` : undefined}}>
          {label}
        </div>
      )}
      <SpectrumChart t={t} show={fade(m) * smooth((u - 0.8) / 0.2)} />
    </>
  );
};

// ─── 5. Contatore di O₂ → scheda del glucosio → pannello della formula ────────
const COUNTER = box(790, 610, 168, 56, 56);
const GLU_CARD = box(540, 1270, 290, 74, 74);
const SHEET = box(540, 960, 472, 332, 64);
const widgetT = () => ({
  in: cue('light', 'split'),
  count0: cue('light', 'split') + 0.45,
  glu: cue('sugar', 'glu') - 0.25,
  sheet: cue('formula', 'f') - 0.15,
  out: sceneStart('tree') + 0.55,
  terms: [cue('formula', 't1'), cue('formula', 't2'), cue('formula', 'arrow'), cue('formula', 't3'), cue('formula', 't4')],
});

const widgetDims = (t: number) => {
  const T = widgetT();
  const a = glide(t, T.glu);
  const b = glide(t, T.sheet);
  return {g: mixG(mixG(COUNTER, GLU_CARD, a), SHEET, b), a, b};
};

const widgetGlass = (t: number): Glass[] => {
  const T = widgetT();
  const m = life(t, T.in, T.out);
  if (m <= 0.001) return [];
  const {g, a, b} = widgetDims(t);
  const s = popScale(t, T.in);
  return [{...REGULAR, ...g, w: g.w * s, h: g.h * s, r: g.r * s, mat: m, dim: 0.16 + 0.24 * b, frost: 0.55 + 0.2 * b, tint: rgb(COL.orange), tintAmt: 0.12 * a * (1 - b), k: 0}];
};

/** Cifre che scorrono come in .numericText(). */
const Rolling: React.FC<{value: number; size: number}> = ({value, size}) => (
  <span style={{display: 'inline-block', height: size * 1.15, overflow: 'hidden', verticalAlign: 'bottom'}}>
    <span style={{display: 'block', transform: `translateY(${-(value % 10) * size * 1.15}px)`}}>
      {Array.from({length: 10}, (_, d) => (
        <span key={d} style={{display: 'block', height: size * 1.15, lineHeight: `${size * 1.15}px`}}>
          {d}
        </span>
      ))}
    </span>
  </span>
);

const Term: React.FC<{t: number; T: number; x: number; y: number; coef?: number; mol: 'CO2' | 'H2O' | 'O2' | 'GLU'; label: React.ReactNode}> = ({t, T, x, y, coef, mol, label}) => {
  const k = bounce(t, T - 0.05);
  const a = smooth(prog(t, T - 0.05, T + 0.25));
  const roll = coef ? Math.round(lerp(0, coef, smooth(prog(t, T, T + 0.45)))) : 0;
  return (
    <div style={{position: 'absolute', left: x - 170, top: y - 92, width: 340, display: 'flex', flexDirection: 'column', alignItems: 'center', opacity: a, transform: `scale(${0.7 + 0.3 * k})`, filter: a < 0.99 ? `blur(${(1 - a) * 8}px)` : undefined}}>
      <MolSVG kind={mol} height={mol === 'GLU' ? 74 : 62} />
      <div style={{...onGlass, fontSize: 60, fontWeight: 800, letterSpacing: '-0.02em', marginTop: 10, whiteSpace: 'nowrap', fontVariantNumeric: 'tabular-nums'}}>
        {coef ? (
          <>
            <Rolling value={roll} size={60} />{' '}
          </>
        ) : null}
        {label}
      </div>
    </div>
  );
};

const WidgetUI: React.FC<{t: number}> = ({t}) => {
  const T = widgetT();
  const m = life(t, T.in, T.out);
  if (m <= 0.02) return null;
  const {g, a, b} = widgetDims(t);
  const n = Math.max(1, Math.min(6, Math.floor((t - T.count0) / 0.5) + 1));
  const stage1 = fade(m) * (1 - smooth(a / 0.35));
  // il testo compare solo quando il vetro ha (quasi) la misura finale: mai fuori dal pannello
  const stage2 = fade(m) * smooth((a - 0.78) / 0.22) * (1 - smooth(b / 0.3));
  const stage3 = fade(m) * smooth((b - 0.82) / 0.18);
  const [t1, t2, arrow, t3, t4] = T.terms;
  const arr = smooth(prog(t, arrow - 0.05, arrow + 0.45));
  return (
    <>
      {stage1 > 0.01 && (
        <div style={{position: 'absolute', left: g.x - 168, top: g.y - 40, width: 336, height: 80, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 14, opacity: stage1}}>
          <MolSVG kind="O2" height={44} />
          <span style={{...onGlass, fontSize: 48, fontWeight: 800, fontVariantNumeric: 'tabular-nums'}}>
            × {t < T.count0 ? 0 : <Rolling value={n} size={48} />}
          </span>
        </div>
      )}
      {stage2 > 0.01 && (
        <div style={{position: 'absolute', left: g.x - 300, top: g.y - 40, width: 600, height: 80, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 18, opacity: stage2}}>
          <MolSVG kind="GLU" height={48} />
          <span style={{...onGlass, fontSize: 46, fontWeight: 800, letterSpacing: '-0.015em'}}>Glucosio</span>
          <span style={{...onGlass, fontSize: 40, fontWeight: 600, color: 'rgba(255,255,255,0.78)'}}>C₆H₁₂O₆</span>
        </div>
      )}
      {stage3 > 0.01 && (
        <div style={{position: 'absolute', inset: 0, opacity: stage3}}>
          <div style={{...onGlass, position: 'absolute', left: 0, right: 0, top: SHEET.y - 272, textAlign: 'center', fontSize: 26, fontWeight: 700, letterSpacing: '0.14em', textTransform: 'uppercase', color: 'rgba(255,255,255,0.72)'}}>
            La fotosintesi in formula
          </div>
          <Term t={t} T={t1} x={330} y={SHEET.y - 126} coef={6} mol="CO2" label="CO₂" />
          <div style={{...onGlass, position: 'absolute', left: 510, top: SHEET.y - 144, width: 60, textAlign: 'center', fontSize: 60, fontWeight: 700, opacity: smooth(prog(t, t2 - 0.1, t2 + 0.2))}}>+</div>
          <Term t={t} T={t2} x={750} y={SHEET.y - 126} coef={6} mol="H2O" label="H₂O" />
          <svg width={720} height={80} style={{position: 'absolute', left: 190, top: SHEET.y + 16, overflow: 'visible', opacity: arr}}>
            <line x1={0} y1={40} x2={700 * arr} y2={40} stroke="#fff" strokeWidth={5} strokeLinecap="round" />
            <path d={`M${700 * arr - 22},24 L${700 * arr},40 L${700 * arr - 22},56`} fill="none" stroke="#fff" strokeWidth={5} strokeLinecap="round" strokeLinejoin="round" />
          </svg>
          <div style={{position: 'absolute', left: 540 - 110, top: SHEET.y - 26, width: 220, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 10, opacity: arr}}>
            <SunIcon size={38} color={COL.amber} />
            <span style={{...onGlass, fontSize: 30, fontWeight: 700, color: COL.amber}}>luce</span>
          </div>
          <Term t={t} T={t3} x={330} y={SHEET.y + 202} mol="GLU" label="C₆H₁₂O₆" />
          <div style={{...onGlass, position: 'absolute', left: 510, top: SHEET.y + 184, width: 60, textAlign: 'center', fontSize: 60, fontWeight: 700, opacity: smooth(prog(t, t4 - 0.1, t4 + 0.2))}}>+</div>
          <Term t={t} T={t4} x={750} y={SHEET.y + 202} coef={6} mol="O2" label="O₂" />
        </div>
      )}
    </>
  );
};

// ─── 6. L'albero: "Legno" e il selettore Terreno | Aria ───────────────────────
const SEG = box(540, 1250, 312, 66, 66);
const SEG_X = [540 - 156, 540 + 156];
const LEGNO = {x: 800, y: 1090};
const treeT = () => ({wood: cue('tree', 'wood') - 0.1, seg: cue('tree', 'soil') - 0.35, soil: cue('tree', 'soil'), air: cue('tree', 'air'), out: sceneStart('cta') + 0.05});

const treeGlass = (t: number): Glass[] => {
  const T = treeT();
  const out: Glass[] = [];
  const ml = life(t, T.wood, T.out);
  if (ml > 0.001) out.push(pillGlass(LEGNO.x, LEGNO.y, 'Legno', ml, popScale(t, T.wood)));
  const ms = life(t, T.seg, T.out);
  if (ms > 0.001) {
    const s = popScale(t, T.seg);
    const pr = press(t, T.air);
    out.push({...REGULAR, ...SEG, w: SEG.w * s, h: SEG.h * s, r: SEG.r * s, mat: ms, dim: 0.2, k: 0, glow: pr.glow * 0.8, gx: SEG_X[1], gy: SEG.y});
  }
  return out;
};

const TreeUI: React.FC<{t: number}> = ({t}) => {
  const T = treeT();
  const ml = life(t, T.wood, T.out);
  const ms = life(t, T.seg, T.out);
  const slide = glide(t, T.air - 0.05);
  const thumbX = lerp(SEG_X[0], SEG_X[1], slide);
  const stretch = 1 + 0.35 * Math.sin(Math.PI * clamp01(slide));
  const thumbCol = slide > 0.5 ? 'rgba(48,209,88,0.55)' : 'rgba(255,69,58,0.42)';
  return (
    <>
      {ml > 0.02 && (
        <svg width={1080} height={1920} style={{position: 'absolute', inset: 0, opacity: fade(ml)}}>
          <line x1={LEGNO.x - textWidth('Legno', 34) / 2 - 34} y1={LEGNO.y} x2={566} y2={LEGNO.y + 20} stroke="rgba(255,255,255,0.85)" strokeWidth={3} strokeLinecap="round" />
          <circle cx={566} cy={LEGNO.y + 20} r={8} fill="#fff" />
        </svg>
      )}
      <Pill x={LEGNO.x} y={LEGNO.y} text="Legno" m={ml} s={popScale(t, T.wood)} />
      {ms > 0.02 && (
        <div style={{position: 'absolute', inset: 0, opacity: fade(ms)}}>
          <div style={{position: 'absolute', left: thumbX - 140 * stretch, top: SEG.y - 52, width: 280 * stretch, height: 104, borderRadius: 52, background: thumbCol, boxShadow: 'inset 0 1.5px 0 rgba(255,255,255,0.5)', opacity: smooth(prog(t, T.soil - 0.1, T.soil + 0.2))}} />
          {['Terreno', 'Aria'].map((l, i) => (
            <div key={l} style={{...onGlass, position: 'absolute', left: SEG_X[i] - 140, top: SEG.y - 30, width: 280, height: 60, display: 'flex', alignItems: 'center', justifyContent: 'center', gap: 10, fontSize: 38, fontWeight: 700}}>
              {i === 1 && slide > 0.6 && <CheckIcon size={34} />}
              {l}
            </div>
          ))}
        </div>
      )}
      <Touch t={t} T={T.air} x={SEG_X[1] + 20} y={SEG.y + 10} />
    </>
  );
};

// ─── 7. Salva e condividi; poi tutto torna alla foglia (loop) ─────────────────
const SAVE = circle(400, 1010, 96);
const SHARE = circle(680, 1010, 96);
const ctaT = () => ({in: cue('cta', 'save') - 0.15, save: cue('cta', 'save') + 0.25, send: cue('cta', 'send') + 0.2});
// negli ultimi 1,35 s tutto il vetro si dissolve e resta la foglia del primo fotogramma
const END = () => sceneEnd('cta') - 1.35;

const ctaGlass = (t: number): Glass[] => {
  const T = ctaT();
  const out: Glass[] = [];
  [SAVE, SHARE].forEach((g, i) => {
    const m = life(t, T.in + i * 0.08, END());
    if (m <= 0.001) return;
    const s = popScale(t, T.in + i * 0.08);
    const prS = press(t, T.save);
    const prH = press(t, T.send);
    const pr = i === 0 ? prS : prH;
    // la luce del tocco si irradia anche al pulsante vicino
    const near = i === 0 ? prH.glow * 0.4 : prS.glow * 0.4;
    const tinted = i === 0 ? smooth(prog(t, T.save, T.save + 0.4)) : smooth(prog(t, T.send, T.send + 0.4));
    out.push({
      ...REGULAR, ...g, w: g.w * s * pr.scale, h: g.h * s * pr.scale, r: g.r * s * pr.scale, mat: m, k: 0,
      tint: rgb(i === 0 ? COL.leaf : COL.blue), tintAmt: 0.3 * tinted,
      glow: Math.max(pr.glow, near), gx: pr.glow >= near ? g.x - 20 : (i === 0 ? SHARE.x : SAVE.x), gy: g.y - 20,
    });
  });
  return out;
};

const CtaUI: React.FC<{t: number}> = ({t}) => {
  const T = ctaT();
  return (
    <>
      {[SAVE, SHARE].map((g, i) => {
        const m = life(t, T.in + i * 0.08, END());
        if (m <= 0.02) return null;
        const pr = press(t, i === 0 ? T.save : T.send);
        const fill = smooth(prog(t, T.save, T.save + 0.35));
        const sent = smooth(prog(t, T.send + 0.05, T.send + 0.3));
        return (
          <React.Fragment key={i}>
            <div style={{position: 'absolute', left: g.x - 44, top: g.y - 44, width: 88, height: 88, opacity: fade(m), transform: `scale(${popScale(t, T.in + i * 0.08) * pr.scale})`}}>
              {i === 0 ? (
                <BookmarkIcon size={88} fill={fill} />
              ) : (
                <div style={{position: 'relative', width: 88, height: 88}}>
                  <div style={{position: 'absolute', inset: 0, opacity: 1 - sent, transform: `scale(${1 - 0.3 * sent})`}}>
                    <ShareIcon size={88} />
                  </div>
                  <div style={{position: 'absolute', inset: 0, opacity: sent, transform: `scale(${0.6 + 0.4 * sent})`}}>
                    <CheckIcon size={88} />
                  </div>
                </div>
              )}
            </div>
            <div style={{...onGlass, position: 'absolute', left: g.x - 150, top: g.y + g.r + 22, width: 300, textAlign: 'center', fontSize: 32, fontWeight: 700, opacity: fade(m)}}>
              {i === 0 ? 'Salva' : 'Condividi'}
            </div>
          </React.Fragment>
        );
      })}
      <Touch t={t} T={T.save} x={SAVE.x + 10} y={SAVE.y + 14} />
      <Touch t={t} T={T.send} x={SHARE.x + 10} y={SHARE.y + 14} />
    </>
  );
};

// ─── Raccolta ─────────────────────────────────────────────────────────────────
export const widgetsGlass = (t: number): Glass[] => [
  ...hookGlass(t),
  ...ingrGlass(t),
  ...stomaGlass(t),
  ...chloroGlass(t),
  ...widgetGlass(t),
  ...treeGlass(t),
  ...ctaGlass(t),
];

export const WidgetsOverlay: React.FC<{t: number}> = ({t}) => (
  <>
    <HookUI t={t} />
    <IngrUI t={t} />
    <StomaUI t={t} />
    <ChloroUI t={t} />
    <WidgetUI t={t} />
    <TreeUI t={t} />
    <CtaUI t={t} />
  </>
);

export const lightAt = (t: number): [number, number] => {
  // inclinazione simulata del telefono: i riflessi scorrono lentamente sui bordi
  const a = -2.2 + 0.42 * Math.sin(t * 0.55) + 0.12 * Math.sin(t * 1.7);
  return [Math.cos(a), Math.sin(a)];
};
