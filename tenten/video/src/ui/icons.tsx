// Icone a tratto (originali) e molecole in SVG con le stesse sfere dell'illustrazione.
import React from 'react';
import {COL} from '../theme';

type P = {size: number; color?: string; fill?: number};

export const SunIcon: React.FC<P> = ({size, color = '#fff'}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth={1.9} strokeLinecap="round">
    <circle cx={12} cy={12} r={4.3} fill={color} />
    {Array.from({length: 8}, (_, i) => {
      const a = (i * Math.PI) / 4;
      return <line key={i} x1={12 + Math.cos(a) * 7} y1={12 + Math.sin(a) * 7} x2={12 + Math.cos(a) * 9.6} y2={12 + Math.sin(a) * 9.6} />;
    })}
  </svg>
);

export const DropIcon: React.FC<P> = ({size, color = '#fff'}) => (
  <svg width={size} height={size} viewBox="0 0 24 24">
    <path d="M12 2.8C12 2.8 5.6 10.2 5.6 14.6a6.4 6.4 0 0 0 12.8 0C18.4 10.2 12 2.8 12 2.8Z" fill={color} />
    <path d="M9 15.2a3 3 0 0 0 2.6 2.9" stroke="rgba(0,0,0,0.25)" strokeWidth={1.6} fill="none" strokeLinecap="round" />
  </svg>
);

export const CO2Icon: React.FC<P> = ({size, color = '#fff'}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth={1.8}>
    <line x1={6.5} y1={10.9} x2={17.5} y2={10.9} />
    <line x1={6.5} y1={13.1} x2={17.5} y2={13.1} />
    <circle cx={4.6} cy={12} r={3.2} fill={color} stroke="none" />
    <circle cx={19.4} cy={12} r={3.2} fill={color} stroke="none" />
    <circle cx={12} cy={12} r={2.7} fill="#1d1d1f" stroke={color} />
  </svg>
);

export const O2Icon: React.FC<P> = ({size, color = '#fff'}) => (
  <svg width={size} height={size} viewBox="0 0 24 24">
    <circle cx={8.6} cy={12} r={5} fill={color} />
    <circle cx={15.4} cy={12} r={5} fill={color} stroke="#1d1d1f" strokeWidth={1.4} />
  </svg>
);

export const HexIcon: React.FC<P> = ({size, color = '#fff'}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth={2} strokeLinejoin="round">
    <path d="M12 3.2 19.6 7.6v8.8L12 20.8 4.4 16.4V7.6Z" />
    <circle cx={12} cy={3.2} r={1.8} fill={color} />
  </svg>
);

export const BookmarkIcon: React.FC<P> = ({size, color = '#fff', fill = 0}) => (
  <svg width={size} height={size} viewBox="0 0 24 24">
    <defs>
      <clipPath id="bmk">
        <path d="M6 3h12v18l-6-4.6L6 21Z" />
      </clipPath>
    </defs>
    <rect x={0} y={24 - 24 * fill} width={24} height={24} fill={color} clipPath="url(#bmk)" />
    <path d="M6 3h12v18l-6-4.6L6 21Z" fill="none" stroke={color} strokeWidth={1.9} strokeLinejoin="round" />
  </svg>
);

export const ShareIcon: React.FC<P> = ({size, color = '#fff'}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth={1.9} strokeLinecap="round" strokeLinejoin="round">
    <path d="M8 9H6.5A1.5 1.5 0 0 0 5 10.5v9A1.5 1.5 0 0 0 6.5 21h11a1.5 1.5 0 0 0 1.5-1.5v-9A1.5 1.5 0 0 0 17.5 9H16" />
    <path d="M12 14V2.8M8.4 6.2 12 2.8l3.6 3.4" />
  </svg>
);

export const CheckIcon: React.FC<P> = ({size, color = '#fff'}) => (
  <svg width={size} height={size} viewBox="0 0 24 24" fill="none" stroke={color} strokeWidth={2.4} strokeLinecap="round" strokeLinejoin="round">
    <path d="M5 12.5 10 17.5 19.5 7" />
  </svg>
);

// ─── Molecole in SVG ──────────────────────────────────────────────────────────
let uid = 0;
const Atom: React.FC<{x: number; y: number; r: number; c: string}> = ({x, y, r, c}) => {
  const id = `a${uid++}`;
  return (
    <>
      <defs>
        <radialGradient id={id} cx="0.32" cy="0.3" r="0.75">
          <stop offset="0" stopColor="#ffffff" />
          <stop offset="0.2" stopColor={c} />
          <stop offset="0.8" stopColor={c} />
          <stop offset="1" stopColor="#000000" stopOpacity="0.55" />
        </radialGradient>
      </defs>
      <circle cx={x} cy={y} r={r} fill={`url(#${id})`} />
    </>
  );
};
const Bond: React.FC<{x0: number; y0: number; x1: number; y1: number; double?: boolean}> = ({x0, y0, x1, y1, double}) =>
  double ? (
    <g stroke="#C9D1DB" strokeWidth={2.4} strokeLinecap="round">
      <line x1={x0} y1={y0 - 2.6} x2={x1} y2={y1 - 2.6} />
      <line x1={x0} y1={y0 + 2.6} x2={x1} y2={y1 + 2.6} />
    </g>
  ) : (
    <line x1={x0} y1={y0} x2={x1} y2={y1} stroke="#C9D1DB" strokeWidth={2.8} strokeLinecap="round" />
  );

export const MolSVG: React.FC<{kind: 'CO2' | 'H2O' | 'O2' | 'GLU'; height: number}> = ({kind, height}) => {
  if (kind === 'CO2')
    return (
      <svg height={height} viewBox="0 0 120 50">
        <Bond x0={22} y0={25} x1={98} y1={25} double />
        <Atom x={22} y={25} r={17} c={COL.oxygen} />
        <Atom x={98} y={25} r={17} c={COL.oxygen} />
        <Atom x={60} y={25} r={15.5} c={COL.carbon} />
      </svg>
    );
  if (kind === 'H2O') {
    const a = (104.5 / 2) * (Math.PI / 180);
    const hx = Math.sin(a) * 26;
    const hy = Math.cos(a) * 26;
    return (
      <svg height={height} viewBox="0 0 90 60">
        <Bond x0={45} y0={20} x1={45 - hx} y1={20 + hy} />
        <Bond x0={45} y0={20} x1={45 + hx} y1={20 + hy} />
        <Atom x={45 - hx} y={20 + hy} r={11} c={COL.hydrogen} />
        <Atom x={45 + hx} y={20 + hy} r={11} c={COL.hydrogen} />
        <Atom x={45} y={20} r={17} c={COL.oxygen} />
      </svg>
    );
  }
  if (kind === 'O2')
    return (
      <svg height={height} viewBox="0 0 90 50">
        <Bond x0={29} y0={25} x1={61} y1={25} double />
        <Atom x={29} y={25} r={17} c={COL.oxygen} />
        <Atom x={61} y={25} r={17} c={COL.oxygen} />
      </svg>
    );
  const pts = Array.from({length: 6}, (_, i) => {
    const ang = -Math.PI / 2 + (i * Math.PI) / 3 + Math.PI / 6;
    return [60 + Math.cos(ang) * 34, 32 + Math.sin(ang) * 21] as [number, number];
  });
  return (
    <svg height={height} viewBox="0 0 120 64">
      {pts.map((p, i) => (
        <Bond key={`b${i}`} x0={p[0]} y0={p[1]} x1={pts[(i + 1) % 6][0]} y1={pts[(i + 1) % 6][1]} />
      ))}
      {pts.map((p, i) => (
        <Atom key={`a${i}`} x={p[0]} y={p[1]} r={i === 0 ? 10 : 9.5} c={i === 0 ? COL.oxygen : COL.carbon} />
      ))}
    </svg>
  );
};
