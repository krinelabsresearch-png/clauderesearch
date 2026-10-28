// Shader "liquid glass": sfondo procedurale + forme di vetro definite da SDF
// (signed distance field), fuse tra loro con smooth-min (metaball).
// Coordinate in pixel di progetto (1080×1920), y verso il basso.

export const MAX_SHAPES = 64;
// Ogni forma occupa 5 texel RGBA32F nella texture dei parametri.
export const SHAPE_TEXELS = 5;
// Culling a tasselli: per ogni quadrato di schermo, l'elenco delle forme che lo influenzano.
export const CULL_TILE = 64;
export const CULL_COLS = Math.ceil(1080 / CULL_TILE);
export const CULL_ROWS = Math.ceil(1920 / CULL_TILE);
export const CULL_SLOTS = 32;

export const VERT = `#version 300 es
in vec2 aPos;
void main() { gl_Position = vec4(aPos, 0.0, 1.0); }
`;

export const FRAG = `#version 300 es
precision highp float;
precision highp int;
precision highp sampler2D;
out vec4 fragColor;

uniform vec2 uRes;
uniform float uScale;
uniform float uTime;
uniform sampler2D uShapes;
uniform sampler2D uCull;

int gTile;
int gCnt;
uniform vec3 uAccA;
uniform vec3 uAccB;
uniform vec4 uRing;
uniform vec4 uRipple;
uniform vec4 uBeadA;
uniform vec4 uBeadB;
uniform vec4 uBeadC;
uniform vec4 uBeadD;
uniform vec4 uBeadE;
uniform vec4 uBeadF;
uniform vec4 uTilesA;
uniform vec4 uTilesB;
uniform vec4 uChartA;
uniform vec4 uChartB;
uniform vec4 uY[12];

const float MAXD = 1e5;

float hash12(vec2 p) {
  vec3 p3 = fract(vec3(p.xyx) * 0.1031);
  p3 += dot(p3, p3.yzx + 33.33);
  return fract((p3.x + p3.y) * p3.z);
}

float smin(float a, float b, float k) {
  if (k < 0.01) return min(a, b);
  float h = max(k - abs(a - b), 0.0) / k;
  return min(a, b) - h * h * k * 0.25;
}

float sdBox(vec2 p, vec2 b, float r) {
  r = min(r, min(b.x, b.y));
  vec2 q = abs(p) - b + r;
  return length(max(q, 0.0)) + min(max(q.x, q.y), 0.0) - r;
}

float sdTri(vec2 p, float r) {
  const float k = 1.7320508;
  p.x = abs(p.x) - r;
  p.y = p.y + r / k;
  if (p.x + k * p.y > 0.0) p = vec2(p.x - k * p.y, -k * p.x - p.y) / 2.0;
  p.x -= clamp(p.x, -2.0 * r, 0.0);
  return -length(p) * sign(p.y);
}

bool insideRing(vec2 p) { return uRing.w > 0.0 && length(p - uRing.xy) < uRing.z; }

// side: 0 = solo fuori dall'onda di transizione, 1 = solo dentro, 2 = sempre
bool visibleSide(float side, bool inside) {
  return side > 1.5 || (side < 0.5 && !inside) || (side > 0.5 && side < 1.5 && inside);
}

vec4 S(int i, int j) { return texelFetch(uShapes, ivec2(j, i), 0); }

float waveAt(float x, float amp) {
  return amp * (sin(x * 0.021 + uTime * 3.1) * 0.6 + sin(x * 0.047 - uTime * 2.3) * 0.4);
}

float shapeD(int i, vec2 p, vec4 a, vec4 b) {
  vec2 lp = p - a.xy;
  if (b.w != 0.0) {
    float c = cos(b.w), s = sin(b.w);
    lp = vec2(c * lp.x + s * lp.y, -s * lp.x + c * lp.y);
  }
  int kind = int(b.y + 0.5);
  if (kind == 1) return length(lp) - a.z;
  if (kind == 3) return sdTri(vec2(lp.x, -lp.y), a.z) - b.x;
  float box = sdBox(lp, a.zw, b.x);
  if (kind == 0) return box;
  vec4 c = S(i, 3);
  if (kind == 2) return abs(box) - c.y;
  if (kind == 4) return abs(length(lp) - a.z) - c.y;
  if (kind == 5) return max(abs(box) - c.y, -a.w * 0.78 - lp.y);
  float level = -a.w + 2.0 * a.w * (1.0 - c.x);
  return max(box, (level + waveAt(p.x, S(i, 4).y)) - lp.y);
}

int shapeAt(int j) { return int(texelFetch(uCull, ivec2(j + 1, gTile), 0).r + 0.5); }

float beadsD(vec2 p, bool inside, out float red) {
  red = 0.0;
  if (uBeadA.z < 0.5 || !visibleSide(uBeadD.w, inside)) return MAXD;
  float cell = uBeadA.x;
  vec2 lo = uBeadC.xy - cell;
  vec2 hi = uBeadC.xy + uBeadC.zw * cell + cell;
  if (p.x < lo.x || p.y < lo.y || p.x > hi.x || p.y > hi.y) return MAXD;
  vec2 g = (p - uBeadC.xy) / cell;
  vec2 base = floor(g - 0.5);
  float best = MAXD;
  for (int j = 0; j < 4; j++) {
    vec2 cid = base + vec2(float(j & 1), float(j >> 1));
    if (cid.x < 0.0 || cid.y < 0.0 || cid.x > uBeadC.z - 1.0 || cid.y > uBeadC.w - 1.0) continue;
    vec2 c = uBeadC.xy + (cid + 0.5) * cell;
    float dist = length(c - uBeadB.xy);
    float grow = 1.0 - smoothstep(uBeadB.z - 150.0, uBeadB.z, dist);
    float wv = 1.0 + uBeadF.x * sin(dist * uBeadF.y - uTime * uBeadF.z);
    float r = uBeadA.y * grow * (1.0 - uBeadB.w) * wv;
    bool isRed = abs(cid.x - uBeadD.x) < 0.5 && abs(cid.y - uBeadD.y) < 0.5;
    if (isRed) r *= (1.0 + 0.4 * uBeadD.z) * (1.0 - uBeadF.w);
    if (r < 0.3) continue;
    float d = length(p - c) - r;
    if (isRed && d < 2.0) red = uBeadD.z;
    best = smin(best, d, uBeadA.w);
  }
  return best;
}

// withBeads = false per l'ombra: centinaia di perle vicine sommerebbero le ombre in un rettangolo scuro.
float sceneD(vec2 p, bool inside, bool withBeads) {
  float d = MAXD;
  for (int j = 0; j < ${CULL_SLOTS} - 1; j++) {
    if (j >= gCnt) break;
    int i = shapeAt(j);
    vec4 a = S(i, 0);
    vec4 b = S(i, 1);
    d = smin(d, shapeD(i, p, a, b), b.z);
  }
  if (withBeads) {
    float rh;
    d = smin(d, beadsD(p, inside, rh), uBeadA.w);
  }
  if (uRing.w > 0.0) d = smin(d, abs(length(p - uRing.xy) - uRing.z) - uRing.w, 70.0);
  return d;
}

struct Hit { float d; vec4 tint; vec4 fx; vec4 mg; int idx; float raw; };

void blendIn(inout Hit h, float di, float k, vec4 tint, vec4 fx, vec4 mg, int idx) {
  float w = k < 0.01 ? (di < h.d ? 0.0 : 1.0) : clamp(0.5 + 0.5 * (di - h.d) / k, 0.0, 1.0);
  h.tint = mix(tint, h.tint, w);
  h.fx = mix(fx, h.fx, w);
  h.mg = mix(mg, h.mg, w);
  if (di < h.raw) { h.raw = di; h.idx = idx; }
  h.d = smin(h.d, di, k);
}

Hit scene(vec2 p, bool inside) {
  Hit h;
  h.d = MAXD; h.tint = vec4(0.0); h.fx = vec4(0.0, 0.0, 1.0, 0.0); h.mg = vec4(0.0); h.idx = -1; h.raw = MAXD;
  for (int j = 0; j < ${CULL_SLOTS} - 1; j++) {
    if (j >= gCnt) break;
    int i = shapeAt(j);
    vec4 a = S(i, 0);
    vec4 b = S(i, 1);
    blendIn(h, shapeD(i, p, a, b), b.z, S(i, 2), S(i, 3), S(i, 4), i);
  }
  float red;
  float db = beadsD(p, inside, red);
  if (db < MAXD * 0.5) {
    vec4 bt = vec4(mix(uBeadE.rgb, vec3(1.0, 0.32, 0.32), red), max(uBeadE.a, red));
    blendIn(h, db, uBeadA.w, bt, vec4(0.0, 0.0, 0.8, 0.0), vec4(0.0), -2);
  }
  if (uRing.w > 0.0) {
    float dr = abs(length(p - uRing.xy) - uRing.z) - uRing.w;
    blendIn(h, dr, 70.0, vec4(0.0), vec4(0.0, 0.0, 2.2, 0.0), vec4(0.0), -3);
  }
  return h;
}

const vec3 PAL[8] = vec3[8](
  vec3(0.23, 0.51, 0.96), vec3(0.55, 0.36, 0.96), vec3(0.06, 0.73, 0.51), vec3(0.96, 0.62, 0.04),
  vec3(0.08, 0.72, 0.65), vec3(0.93, 0.28, 0.60), vec3(0.39, 0.40, 0.95), vec3(0.13, 0.77, 0.37)
);

float chartY(int i) {
  vec4 v = uY[i / 4];
  int k = i - (i / 4) * 4;
  return k == 0 ? v.x : (k == 1 ? v.y : (k == 2 ? v.z : v.w));
}

vec3 background(vec2 p, float blur, bool inside) {
  if (uRipple.w > 0.0) {
    vec2 v = p - uRipple.xy;
    float r = length(v);
    float ph = r - uRipple.z * 760.0;
    float env = exp(-ph * ph / (120.0 * 120.0)) * uRipple.w * exp(-uRipple.z * 0.8);
    p += v / max(r, 1.0) * sin(ph * 0.05) * env * 24.0;
  }
  vec3 acc = inside ? uAccB : uAccA;
  float t = uTime;
  vec3 col = mix(vec3(0.010, 0.014, 0.028), vec3(0.022, 0.032, 0.062), clamp(p.y / 1920.0, 0.0, 1.0));
  vec2 b1 = vec2(540.0 + sin(t * 0.31) * 330.0, 760.0 + cos(t * 0.23) * 380.0);
  vec2 b2 = vec2(540.0 + cos(t * 0.27 + 1.7) * 360.0, 1260.0 + sin(t * 0.19 + 0.6) * 360.0);
  vec2 b3 = vec2(540.0 + sin(t * 0.21 + 3.1) * 420.0, 430.0 + cos(t * 0.33 + 2.2) * 260.0);
  vec2 b4 = vec2(540.0 + cos(t * 0.17 + 4.4) * 300.0, 1600.0 + sin(t * 0.29 + 1.1) * 200.0);
  col += acc * 0.60 * exp(-dot(p - b1, p - b1) / (2.0 * 380.0 * 380.0));
  col += vec3(0.05, 0.50, 0.78) * 0.30 * exp(-dot(p - b2, p - b2) / (2.0 * 400.0 * 400.0));
  col += vec3(0.48, 0.25, 0.95) * 0.28 * exp(-dot(p - b3, p - b3) / (2.0 * 330.0 * 330.0));
  col += acc * 0.24 * exp(-dot(p - b4, p - b4) / (2.0 * 300.0 * 300.0));

  vec2 q = abs(fract(p / 60.0) - 0.5) * 60.0;
  float line = min(30.0 - q.x, 30.0 - q.y);
  col += vec3(0.55, 0.65, 0.95) * (1.0 - smoothstep(0.6, 1.6 + blur * 5.0, line)) * (0.05 - blur * 0.02);
  float cross = length(vec2(30.0) - q);
  col += vec3(0.7, 0.8, 1.0) * (1.0 - smoothstep(1.4, 3.0 + blur * 4.0, cross)) * 0.11;

  vec2 cp = p / 170.0 + vec2(0.0, -t * 0.06);
  vec2 ci = floor(cp);
  float hp = hash12(ci);
  if (hp > 0.55) {
    vec2 pp = vec2(hash12(ci + 3.1), hash12(ci + 7.7)) * 0.8 + 0.1;
    float dd = length(fract(cp) - pp) * 170.0;
    float sz = 1.5 + (hp - 0.55) * 9.0 + blur * 5.0;
    col += mix(vec3(1.0), acc, 0.4) * (1.0 - smoothstep(sz * 0.3, sz, dd)) * 0.32 * (0.6 + 0.4 * sin(t * 2.0 + hp * 20.0));
  }

  if (uTilesA.w > 0.0 && visibleSide(uTilesB.w, inside)) {
    vec2 g = (p - uTilesA.xy) / uTilesA.z;
    vec2 id = floor(g);
    if (id.x >= 0.0 && id.y >= 0.0 && id.x < uTilesB.x && id.y < uTilesB.y) {
      vec2 lp = (fract(g) - 0.5) * uTilesA.z;
      float d = sdBox(lp, vec2(uTilesA.w * 0.5), 22.0);
      float wave = clamp(uTilesB.z * 1.7 - (id.x + id.y) / (uTilesB.x + uTilesB.y), 0.0, 1.0);
      wave = wave * wave * (3.0 - 2.0 * wave);
      vec3 tc = mix(vec3(0.085, 0.11, 0.17), PAL[int(hash12(id + 11.0) * 7.99)], wave);
      float a = 1.0 - smoothstep(-1.0, 1.0 + blur * 3.0, d);
      col = mix(col, tc, a * 0.95);
      col += vec3(1.0, 1.0, 1.0) * a * 0.08 * (1.0 - smoothstep(0.0, 6.0, abs(d + 3.0)));
      float gd = length(lp) - 15.0;
      col = mix(col, vec3(1.0), (1.0 - smoothstep(-1.0, 1.0, gd)) * a * (0.12 + 0.75 * wave));
    }
  }

  if (uChartB.w > 0.0 && visibleSide(uChartB.z, inside) && p.x > uChartA.x - 30.0 && p.x < uChartA.y + 30.0) {
    float n = uChartA.z;
    float u = clamp((p.x - uChartA.x) / (uChartA.y - uChartA.x), 0.0, 1.0) * (n - 1.0);
    int i0 = int(floor(u));
    int i1 = min(i0 + 1, int(n) - 1);
    float y0 = chartY(i0), y1 = chartY(i1);
    float yc = mix(y0, y1, u - float(i0));
    float slope = (y1 - y0) / ((uChartA.y - uChartA.x) / (n - 1.0));
    float dl = abs(p.y - yc) / sqrt(1.0 + slope * slope);
    float shown = 1.0 - smoothstep(uChartA.w - 0.3, uChartA.w, u);
    vec3 lc = u >= uChartB.x ? vec3(0.97, 0.44, 0.44) : vec3(0.20, 0.83, 0.60);
    float al = shown * uChartB.w;
    col += lc * (1.0 - smoothstep(2.5, 4.5 + blur * 4.0, dl)) * al;
    col += lc * exp(-dl * dl / (2.0 * 16.0 * 16.0)) * 0.35 * al;
    if (p.y > yc && p.y < uChartB.y) col += lc * 0.20 * (1.0 - (p.y - yc) / (uChartB.y - yc + 1.0)) * al;
  }

  vec2 vq = (p - vec2(540.0, 900.0)) / vec2(900.0, 1300.0);
  col *= 1.0 - 0.45 * smoothstep(0.35, 1.0, dot(vq, vq));
  return col;
}

void main() {
  vec2 p = vec2(gl_FragCoord.x, uRes.y - gl_FragCoord.y) / uScale;
  ivec2 tc = clamp(ivec2(p / ${CULL_TILE}.0), ivec2(0), ivec2(${CULL_COLS} - 1, ${CULL_ROWS} - 1));
  gTile = tc.y * ${CULL_COLS} + tc.x;
  gCnt = int(texelFetch(uCull, ivec2(0, gTile), 0).r + 0.5);
  bool inside = insideRing(p);
  vec3 acc = inside ? uAccB : uAccA;
  Hit h = scene(p, inside);

  vec3 col = vec3(0.0);
  if (h.d > -1.0) {
    float dsh = sceneD(p - vec2(0.0, 28.0), inside, false);
    col = background(p, 0.0, inside);
    col *= 1.0 - exp(-max(dsh, 0.0) / 40.0) * 0.45 * smoothstep(-1.0, 2.0, h.d);
  }

  if (h.d < 2.0) {
    float e = 1.25;
    vec2 n = vec2(sceneD(p + vec2(e, 0.0), inside, true) - h.d, sceneD(p + vec2(0.0, e), inside, true) - h.d);
    float nl = length(n);
    n = nl > 1e-5 ? n / nl : vec2(0.0, -1.0);
    float band = clamp(40.0 * h.fx.z, 6.0, 110.0);
    float depth = clamp(-h.d / band, 0.0, 1.0);
    float edge = 1.0 - depth;
    float prof = edge * edge;
    vec2 off = -n * prof * band * 1.3;
    vec2 sp = p;
    if (h.mg.x > 0.01 && h.idx >= 0) {
      vec2 c = S(h.idx, 0).xy;
      sp = c + (p - c) / (1.0 + h.mg.x);
    }
    float frost = h.fx.w;
    vec3 refr;
    refr.r = background(sp + off * 1.09, frost, inside).r;
    refr.g = background(sp + off, frost, inside).g;
    refr.b = background(sp + off * 0.91, frost, inside).b;

    vec3 tint = h.tint.rgb;
    float ta = h.tint.a;
    float lum = dot(refr, vec3(0.3, 0.5, 0.2));
    vec3 glass = refr * 1.06;
    glass = mix(glass, glass * 0.5 + tint * (0.3 + 1.1 * lum), ta * 0.6);
    glass += tint * ta * 0.05 + 0.022;

    if (h.idx >= 0 && h.fx.x > 0.001 && S(h.idx, 1).y < 5.5) {
      vec4 a = S(h.idx, 0);
      float lv = a.y - a.w + 2.0 * a.w * (1.0 - h.fx.x) + waveAt(p.x, S(h.idx, 4).y + 3.0);
      if (p.y > lv) {
        float dd = p.y - lv;
        vec3 lq = tint * (0.45 + 1.3 * lum) + tint * 0.35 * exp(-dd / 14.0);
        glass = mix(glass, lq, 0.8);
      }
      glass += vec3(1.0) * exp(-abs(p.y - lv) / 1.4) * 0.55;
    }

    vec3 N = normalize(vec3(n * prof * 1.8, 1.0));
    vec3 L = normalize(vec3(-0.5, -0.85, 0.75));
    vec3 H = normalize(L + vec3(0.0, 0.0, 1.0));
    float spec = pow(max(dot(N, H), 0.0), 70.0) * 1.1;
    float lit = max(dot(n, normalize(vec2(-0.5, -0.85))), 0.0);
    glass += vec3(1.0) * (spec + pow(lit, 2.0) * pow(edge, 7.0) * 1.05);
    glass += mix(acc, tint, ta) * pow(max(dot(n, normalize(vec2(0.45, 0.9))), 0.0), 2.0) * pow(edge, 5.0) * 0.5;
    glass += vec3(0.85, 0.92, 1.0) * pow(edge, 16.0) * 0.4;
    glass += (tint * ta + acc * 0.45) * pow(max(n.y, 0.0), 3.0) * smoothstep(0.0, 0.5, depth) * (1.0 - depth) * 0.3;

    float a = 1.0 - smoothstep(-0.9, 0.9, h.d);
    col = mix(col, glass, a);
  }
  col += (hash12(p * 1.37 + fract(uTime * 7.0) * 113.0) - 0.5) * (1.6 / 255.0);
  fragColor = vec4(col, 1.0);
}
`;
