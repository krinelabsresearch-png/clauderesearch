// I tempi della regia, ricavati dalle parole della voce (src/script.ts).
// Li usano immagine, vetro ed effetti sonori: tutto resta sincronizzato.
import {TIMELINE, cueSeconds} from './script.ts';
import {clamp01} from './math.ts';

const cue = (s: string, n: string) => cueSeconds(s, n);
const sceneStart = (id: string) => TIMELINE.find((x) => x.id === id)!.start;
const sceneEnd = (id: string) => TIMELINE.find((x) => x.id === id)!.end;

// ─── Tempi della regia (dalle parole della voce) ──────────────────────────────
const times = () => {
  const place = sceneStart('place');
  const game = sceneStart('game');
  const press = cue('game', 'press') + 0.12;
  return {
    land: cue('hook', 'euro') + 0.05,
    rush: place - 0.3,
    place,
    pista: cue('place', 'verdi') - 0.05,
    game,
    rise: press - 0.6,
    press,
    stop: cue('game', 'ten') + 0.12,
    bottle: cue('win', 'bottle') - 0.35,
    party: cue('win', 'party') - 0.1,
    cta: sceneStart('cta') - 0.12,
    end: sceneEnd('cta') - 1.25,
  };
};
let TT: ReturnType<typeof times> | null = null;
export const T = () => (TT ??= times());

// ─── Il timer del gioco: corre veloce e si ferma esattamente su 10:10 ─────────
export const timerValue = (t: number) => {
  const {press, stop} = T();
  if (t < press) return 0;
  const u = clamp01((t - press) / (stop - press));
  return 10.1 * (1 - Math.pow(1 - u, 1.7));
};
export const timerText = (v: number) => {
  const s = Math.floor(v + 1e-6);
  const c = Math.floor((v - s) * 100 + 1e-6);
  return `${String(s).padStart(2, '0')}:${String(c).padStart(2, '0')}`;
};
/** Il display lampeggia tre volte quando il timer si ferma. */
export const timerBlink = (t: number) => {
  const d = t - T().stop;
  if (d < 0 || d > 0.66) return 1;
  return Math.floor(d / 0.11) % 2 ? 0.25 : 1;
};
/** Lampo quando il timer si ferma. */
export const flash = (t: number) => {
  const d = t - T().stop;
  return d < 0 ? 0 : Math.exp(-d / 0.28);
};
// ─── Tempi dei controlli di vetro ─────────────────────────────────────────────
const wtimes = () => {
  const S = T();
  return {
    price: cue('hook', 'disco') - 0.25,
    roll: cue('hook', 'euro') - 0.3,
    title: cue('place', 'name') - 0.15,
    loc: cue('place', 'xo') - 0.05,
    chip: sceneStart('game') + 0.05,
    timer: S.rise,
    vip: S.bottle + 0.25,
    vipOut: S.party + 0.25,
    card: sceneStart('cta') - 0.05,
    // il pulsante si stacca dalla scheda appena formata e viene toccato mentre la voce dice "Prenota"
    btn: sceneStart('cta') + 0.3,
    tap: Math.max(sceneStart('cta') + 0.85, cue('cta', 'book') + 0.3),
    see: cue('cta', 'see'),
    end: sceneEnd('cta') - 1.3,
  };
};
let WT: ReturnType<typeof wtimes> | null = null;
export const W = () => (WT ??= wtimes());

