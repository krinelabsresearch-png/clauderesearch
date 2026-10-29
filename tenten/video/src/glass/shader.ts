// Shader in stile Liquid Glass: il vetro legge l'illustrazione sottostante come
// texture e la piega ai bordi (lensing), con smerigliatura vera, vivacità,
// riflessi speculari che seguono un'inclinazione simulata, ombre morbide,
// comparsa per modulazione della rifrazione e illuminazione al tocco.
// Coordinate in pixel di progetto (1080×1920), y verso il basso.

export const MAX_SHAPES = 48;
export const SHAPE_TEXELS = 6;
export const CULL_TILE = 64;
export const CULL_COLS = Math.ceil(1080 / CULL_TILE);
export const CULL_ROWS = Math.ceil(1920 / CULL_TILE);
export const CULL_SLOTS = 24;

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
uniform vec2 uLight;
uniform sampler2D uContent;
uniform sampler2D uShapes;
uniform sampler2D uCull;

int gTile;
int gCnt;
const float MAXD = 1e5;
const vec2 SIZE = vec2(1080.0, 1920.0);

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

vec4 S(int i, int j) { return texelFetch(uShapes, ivec2(j, i), 0); }
int shapeAt(int j) { return int(texelFetch(uCull, ivec2(j + 1, gTile), 0).r + 0.5); }

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
  if (kind == 2) return abs(box) - S(i, 5).y;
  return box;
}

float sceneD(vec2 p) {
  float d = MAXD;
  for (int j = 0; j < ${CULL_SLOTS} - 1; j++) {
    if (j >= gCnt) break;
    int i = shapeAt(j);
    vec4 b = S(i, 1);
    d = smin(d, shapeD(i, p, S(i, 0), b), b.z);
  }
  return d;
}

// Distanza "di ombra": le forme che stanno comparendo fanno meno ombra.
float shadowD(vec2 p) {
  float d = MAXD;
  for (int j = 0; j < ${CULL_SLOTS} - 1; j++) {
    if (j >= gCnt) break;
    int i = shapeAt(j);
    vec4 b = S(i, 1);
    float m = S(i, 3).z;
    d = smin(d, shapeD(i, p, S(i, 0), b) + (1.0 - m) * 90.0, b.z);
  }
  return d;
}

struct Hit { float d; vec4 tint; vec4 fx; vec4 fx2; vec4 fx3; int idx; float raw; };

Hit scene(vec2 p) {
  Hit h;
  h.d = MAXD; h.tint = vec4(0.0); h.fx = vec4(0.0, 1.0, 0.0, 0.0); h.fx2 = vec4(0.0); h.fx3 = vec4(0.0);
  h.idx = -1; h.raw = MAXD;
  for (int j = 0; j < ${CULL_SLOTS} - 1; j++) {
    if (j >= gCnt) break;
    int i = shapeAt(j);
    vec4 b = S(i, 1);
    float di = shapeD(i, p, S(i, 0), b);
    float k = b.z;
    float w = k < 0.01 ? (di < h.d ? 0.0 : 1.0) : clamp(0.5 + 0.5 * (di - h.d) / k, 0.0, 1.0);
    h.tint = mix(S(i, 2), h.tint, w);
    h.fx = mix(S(i, 3), h.fx, w);
    h.fx2 = mix(S(i, 4), h.fx2, w);
    h.fx3 = mix(S(i, 5), h.fx3, w);
    if (di < h.raw) { h.raw = di; h.idx = i; }
    h.d = smin(h.d, di, k);
  }
  return h;
}

vec3 tex(vec2 p, float lod) { return textureLod(uContent, p / SIZE, lod).rgb; }

// Smerigliatura: 5 campioni su un livello di mipmap, per una sfocatura morbida e senza blocchi.
vec3 frosted(vec2 p, float lod) {
  if (lod < 0.25) return tex(p, 0.0);
  float r = exp2(lod) * 0.85;
  vec3 c = tex(p, lod) * 0.28;
  c += tex(p + vec2(r, r * 0.3), lod) * 0.18;
  c += tex(p - vec2(r, r * 0.3), lod) * 0.18;
  c += tex(p + vec2(-r * 0.3, r), lod) * 0.18;
  c += tex(p - vec2(-r * 0.3, r), lod) * 0.18;
  return c;
}

void main() {
  vec2 p = vec2(gl_FragCoord.x, uRes.y - gl_FragCoord.y) / uScale;
  ivec2 tc = clamp(ivec2(p / ${CULL_TILE}.0), ivec2(0), ivec2(${CULL_COLS} - 1, ${CULL_ROWS} - 1));
  gTile = tc.y * ${CULL_COLS} + tc.x;
  gCnt = int(texelFetch(uCull, ivec2(0, gTile), 0).r + 0.5);

  Hit h = scene(p);
  vec3 col = tex(p, 0.0);
  if (gCnt > 0 && h.d > -1.0) {
    float ds = shadowD(p - vec2(0.0, 20.0));
    col *= 1.0 - exp(-max(ds, 0.0) / 34.0) * 0.26 * smoothstep(-1.0, 2.0, h.d);
  }

  if (h.d < 2.0) {
    float mat = h.fx.z;
    float e = 1.25;
    vec2 n = vec2(sceneD(p + vec2(e, 0.0)) - h.d, sceneD(p + vec2(0.0, e)) - h.d);
    float nl = length(n);
    n = nl > 1e-5 ? n / nl : vec2(0.0, -1.0);
    float band = clamp(44.0 * h.fx.y, 8.0, 130.0);
    float depth = clamp(-h.d / band, 0.0, 1.0);
    float edge = 1.0 - depth;
    float prof = edge * edge;
    vec2 off = -n * prof * band * 1.35 * mat;

    vec2 sp = p;
    if (h.fx.w > 0.01 && h.idx >= 0) {
      vec2 c = S(h.idx, 0).xy;
      sp = c + (p - c) / (1.0 + h.fx.w * mat);
    }
    float lod = h.fx.x * 4.6 * mat;
    float disp = (0.035 + h.fx3.x) * mat;
    vec3 g;
    g.r = frosted(sp + off * (1.0 + disp), lod).r;
    g.g = frosted(sp + off, lod).g;
    g.b = frosted(sp + off * (1.0 - disp), lod).b;

    float lum = dot(g, vec3(0.299, 0.587, 0.114));
    g = mix(vec3(lum), g, 1.0 + 0.22 * mat);
    g = g * (1.0 + 0.07 * mat) + 0.03 * mat;
    g = mix(g, g * 0.55 + h.tint.rgb * (0.22 + 0.95 * lum), h.tint.a * mat);
    g *= 1.0 - h.fx2.x * mat;

    vec2 L = normalize(uLight);
    float rimA = pow(max(dot(n, L), 0.0), 2.4) * pow(edge, 9.0);
    float rimB = pow(max(dot(n, -L), 0.0), 2.4) * pow(edge, 11.0) * 0.42;
    g += vec3(1.0) * (rimA * 0.95 + rimB) * mat;
    g += vec3(1.0) * pow(edge, 26.0) * 0.2 * mat;
    g *= 1.0 - 0.09 * mat * pow(edge, 3.0) * max(n.y, 0.0);

    if (h.fx2.y > 0.001) {
      float dd = length(p - h.fx2.zw);
      g += vec3(1.0) * h.fx2.y * (exp(-dd / 140.0) * 0.32 + exp(-dd / 320.0) * pow(edge, 6.0) * 0.7);
    }
    float a = 1.0 - smoothstep(-0.9, 0.9, h.d);
    col = mix(col, g, a);
  }
  col += (hash12(p * 1.37 + fract(uTime * 7.0) * 113.0) - 0.5) * (1.4 / 255.0);
  fragColor = vec4(col, 1.0);
}
`;
