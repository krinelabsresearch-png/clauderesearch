import React from 'react';
import {spring, useCurrentFrame} from 'remotion';
import {FPS} from '../script';
import {C, FONT, easeInOut, lerp, ramp} from '../theme';

/** Colori "settore" per le aziende astratte (nessun logo reale). */
export const SECTOR = ['#3B82F6', '#8B5CF6', '#10B981', '#F59E0B', '#14B8A6', '#EC4899', '#6366F1', '#22C55E'];

export const Glyph: React.FC<{kind: number; size: number; color?: string; opacity?: number}> = ({
  kind,
  size,
  color = '#FFFFFF',
  opacity = 0.92,
}) => {
  const k = ((kind % 6) + 6) % 6;
  return (
    <svg width={size} height={size} viewBox="0 0 100 100" style={{opacity, display: 'block'}}>
      {k === 0 && <circle cx="50" cy="50" r="25" fill={color} />}
      {k === 1 && <path d="M50 22 L78 74 L22 74 Z" fill={color} />}
      {k === 2 && <rect x="27" y="27" width="46" height="46" rx="9" fill={color} />}
      {k === 3 && <circle cx="50" cy="50" r="23" fill="none" stroke={color} strokeWidth="11" />}
      {k === 4 && (
        <g fill={color}>
          <rect x="24" y="52" width="13" height="24" rx="3" />
          <rect x="44" y="38" width="13" height="38" rx="3" />
          <rect x="64" y="24" width="13" height="52" rx="3" />
        </g>
      )}
      {k === 5 && <path d="M50 20 L80 50 L50 80 L20 50 Z" fill={color} />}
    </svg>
  );
};

/** Una "azienda": quadrato colorato con un simbolo astratto. */
export const CompanyTile: React.FC<{size: number; color: string; kind: number; style?: React.CSSProperties}> = ({
  size,
  color,
  kind,
  style,
}) => (
  <div
    style={{
      width: size,
      height: size,
      borderRadius: size * 0.24,
      background: `linear-gradient(145deg, ${color}, ${color}B0)`,
      boxShadow: `inset 0 2px 0 rgba(255,255,255,0.25), 0 ${size * 0.12}px ${size * 0.3}px rgba(0,0,0,0.45)`,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      ...style,
    }}
  >
    <Glyph kind={kind} size={size * 0.62} />
  </div>
);

export const Label: React.FC<{children: React.ReactNode; color?: string; size?: number; style?: React.CSSProperties}> = ({
  children,
  color = C.dim,
  size = 26,
  style,
}) => (
  <div
    style={{
      fontFamily: FONT,
      fontWeight: 700,
      fontSize: size,
      letterSpacing: '0.16em',
      textTransform: 'uppercase',
      color,
      ...style,
    }}
  >
    {children}
  </div>
);

/**
 * Cartello di sezione ("01 DIVERSIFICAZIONE"): entra grande al centro,
 * poi si dissolve lasciando una piccola etichetta fissa in alto.
 */
export const TitleCard: React.FC<{num: string; title: string; color: string; outAt: number}> = ({
  num,
  title,
  color,
  outAt,
}) => {
  const f = useCurrentFrame();
  const inP = spring({frame: f - 4, fps: FPS, config: {damping: 15, stiffness: 150}});
  const out = ramp(f, outAt, outAt + 18, easeInOut);
  const chip = ramp(f, outAt + 6, outAt + 24);
  return (
    <>
      {out < 1 && (
        <div
          style={{
            position: 'absolute',
            left: 0,
            right: 0,
            top: 700,
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            opacity: 1 - out,
            transform: `translateY(${-50 * out}px) scale(${1 - 0.1 * out})`,
            filter: out > 0 ? `blur(${out * 10}px)` : undefined,
          }}
        >
          <div style={{overflow: 'hidden', height: 270}}>
            <div
              style={{
                fontFamily: FONT,
                fontWeight: 900,
                fontSize: 260,
                lineHeight: 1,
                color: 'transparent',
                WebkitTextStroke: `4px ${color}`,
                transform: `translateY(${(1 - inP) * 270}px)`,
                textShadow: `0 0 60px ${color}40`,
              }}
            >
              {num}
            </div>
          </div>
          <div style={{display: 'flex', marginTop: 18}}>
            {[...title].map((ch, i) => {
              const p = ramp(f, 10 + i * 1.6, 24 + i * 1.6);
              return (
                <span
                  key={i}
                  style={{
                    fontFamily: FONT,
                    fontWeight: 800,
                    fontSize: 62,
                    letterSpacing: '0.12em',
                    color: C.text,
                    opacity: p,
                    display: 'inline-block',
                    transform: `translateY(${(1 - p) * 30}px)`,
                  }}
                >
                  {ch}
                </span>
              );
            })}
          </div>
        </div>
      )}
      {chip > 0 && (
        <div style={{position: 'absolute', top: 492, left: 0, right: 0, display: 'flex', justifyContent: 'center'}}>
          <div
            style={{
              display: 'flex',
              alignItems: 'center',
              gap: 14,
              padding: '10px 24px',
              borderRadius: 999,
              border: `2px solid ${color}66`,
              background: `${color}14`,
              opacity: chip,
              transform: `translateY(${(1 - chip) * -16}px)`,
            }}
          >
            <span style={{fontFamily: FONT, fontWeight: 900, fontSize: 28, color}}>{num}</span>
            <Label size={24} color={C.text} style={{letterSpacing: '0.14em'}}>
              {title}
            </Label>
          </div>
        </div>
      )}
    </>
  );
};

type ChartProps = {
  x: number;
  y: number;
  w: number;
  h: number;
  series: number[];
  vmin: number;
  vmax: number;
  /** quanti punti sono già disegnati (anche frazionario) */
  reveal: number;
  /** indice da cui la linea diventa rossa (calo) */
  redFrom?: number;
  color?: string;
  baseline?: number;
};

/** Grafico a linea che si disegna nel tempo, con tratto rosso nel calo e punto luminoso in testa. */
export const LineChart: React.FC<ChartProps> = ({
  x,
  y,
  w,
  h,
  series,
  vmin,
  vmax,
  reveal,
  redFrom = Infinity,
  color = C.green,
  baseline = 0,
}) => {
  const n = series.length;
  const px = (i: number) => (i / (n - 1)) * w;
  const py = (v: number) => h - ((v - vmin) / (vmax - vmin)) * h;
  const r = Math.max(0, Math.min(n - 1, reveal));
  const last = Math.floor(r);
  const frac = r - last;
  const pts: [number, number][] = [];
  for (let i = 0; i <= last; i++) pts.push([px(i), py(series[i])]);
  if (last < n - 1 && frac > 0) {
    pts.push([lerp(px(last), px(last + 1), frac), py(lerp(series[last], series[last + 1], frac))]);
  }
  const toD = (p: [number, number][]) => p.map(([a, b], i) => `${i ? 'L' : 'M'}${a.toFixed(1)} ${b.toFixed(1)}`).join(' ');
  const split = Math.min(pts.length, Math.max(0, Math.floor(redFrom) + 1));
  const normal = pts.slice(0, split);
  const red = split < pts.length ? pts.slice(Math.max(0, split - 1)) : [];
  const head = pts[pts.length - 1];
  const headColor = red.length ? C.red : color;
  const id = `g${Math.round(x)}${Math.round(y)}`;
  return (
    <svg width={w + 40} height={h + 40} style={{position: 'absolute', left: x - 20, top: y - 20, overflow: 'visible'}}>
      <defs>
        <linearGradient id={`${id}r`} x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stopColor={C.red} stopOpacity="0.35" />
          <stop offset="1" stopColor={C.red} stopOpacity="0" />
        </linearGradient>
        <linearGradient id={`${id}n`} x1="0" y1="0" x2="0" y2="1">
          <stop offset="0" stopColor={color} stopOpacity="0.22" />
          <stop offset="1" stopColor={color} stopOpacity="0" />
        </linearGradient>
      </defs>
      <g transform="translate(20 20)">
        {[0.25, 0.5, 0.75].map((k) => (
          <line key={k} x1={0} x2={w} y1={h * k} y2={h * k} stroke="rgba(255,255,255,0.06)" strokeWidth={1.5} />
        ))}
        <line x1={0} x2={w} y1={py(baseline)} y2={py(baseline)} stroke="rgba(255,255,255,0.22)" strokeWidth={2} strokeDasharray="6 10" />
        {normal.length > 1 && (
          <path d={`${toD(normal)} L${normal[normal.length - 1][0]} ${h} L0 ${h} Z`} fill={`url(#${id}n)`} />
        )}
        {red.length > 1 && (
          <path d={`${toD(red)} L${red[red.length - 1][0]} ${h} L${red[0][0]} ${h} Z`} fill={`url(#${id}r)`} />
        )}
        {normal.length > 1 && <path d={toD(normal)} fill="none" stroke={color} strokeWidth={6} strokeLinejoin="round" strokeLinecap="round" />}
        {red.length > 1 && <path d={toD(red)} fill="none" stroke={C.red} strokeWidth={6} strokeLinejoin="round" strokeLinecap="round" />}
        {head && (
          <>
            <circle cx={head[0]} cy={head[1]} r={22} fill={headColor} opacity={0.18} />
            <circle cx={head[0]} cy={head[1]} r={10} fill={headColor} />
            <circle cx={head[0]} cy={head[1]} r={4} fill="#fff" />
          </>
        )}
      </g>
    </svg>
  );
};

/** Serie con un rumore leggero e deterministico. */
export const noisy = (n: number, seed: number, amp: number, shape: (i: number) => number) =>
  Array.from({length: n}, (_, i) => {
    const a = Math.sin(i * 0.9 + seed) * 0.5 + Math.sin(i * 0.37 + seed * 2) * 0.35 + (Math.sin(i * 2.3 + seed * 3) * 0.15);
    return shape(i) + a * amp;
  });

export const Card: React.FC<{x: number; y: number; w: number; h: number; style?: React.CSSProperties; children?: React.ReactNode}> = ({
  x,
  y,
  w,
  h,
  style,
  children,
}) => (
  <div
    style={{
      position: 'absolute',
      left: x,
      top: y,
      width: w,
      height: h,
      borderRadius: 34,
      background: 'linear-gradient(180deg, rgba(255,255,255,0.05), rgba(255,255,255,0.02))',
      border: '1.5px solid rgba(255,255,255,0.09)',
      boxShadow: '0 30px 80px rgba(0,0,0,0.45), inset 0 1px 0 rgba(255,255,255,0.06)',
      ...style,
    }}
  >
    {children}
  </div>
);
