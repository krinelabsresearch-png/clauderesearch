// Foto vere in 2.5D: ogni foto ha la sua mappa di profondità, quindi la camera
// può muoversi davvero (parallasse), mettere a fuoco su un piano e passare da una
// foto all'altra facendo comparire prima ciò che è vicino e poi lo sfondo.
import {IMG} from '../assets';

export type Shot = {
  /** nome della foto in public/img (senza estensione) */
  key: string;
  /** punto della foto al centro dell'inquadratura (0..1) */
  cx: number;
  cy: number;
  /** 1 = la foto riempie l'altezza del video */
  zoom: number;
  rot?: number;
  /** spostamento della camera: i piani vicini si muovono più di quelli lontani */
  px?: number;
  py?: number;
  /** profondità che resta ferma (0 = sfondo, 1 = primo piano) */
  focus?: number;
  /** scia di movimento, in pixel del video */
  bx?: number;
  by?: number;
  /** sfocatura (livello di mipmap) */
  defocus?: number;
  exposure?: number;
};

export type Mode = 'depth' | 'flare' | 'fade';
const MODE: Record<Mode, number> = {depth: 0, flare: 1, fade: 2};

const VERT = `#version 300 es
in vec2 aPos;
out vec2 vUv;
void main() {
  vUv = aPos * 0.5 + 0.5;
  vUv.y = 1.0 - vUv.y;
  gl_Position = vec4(aPos, 0.0, 1.0);
}`;

const FRAG = `#version 300 es
precision highp float;
in vec2 vUv;
out vec4 o;
uniform sampler2D uA, uDA, uB, uDB;
uniform vec4 uCamA, uParA, uFxA, uCamB, uParB, uFxB;
uniform float uMix, uFrame, uHasB;
uniform int uMode;
uniform vec3 uFlare;

// inquadratura -> coordinate della foto, con il parallasse dato dalla profondità
vec2 photoUv(vec2 p, vec4 cam, vec4 par, sampler2D dep, out float depth) {
  vec2 d = p - 0.5;
  d.x *= uFrame / par.w;
  float c = cos(cam.w), s = sin(cam.w);
  d = mat2(c, -s, s, c) * d;
  vec2 q = d / cam.z + cam.xy;
  vec2 qi = q;
  depth = 0.5;
  for (int i = 0; i < 5; i++) {
    depth = textureLod(dep, clamp(qi, 0.001, 0.999), 1.5).r;
    qi = q + (depth - par.z) * par.xy / cam.z;
  }
  return clamp(qi, 0.001, 0.999);
}

vec3 shade(sampler2D img, sampler2D dep, vec4 cam, vec4 par, vec4 fx, out float depth) {
  vec2 q = photoUv(vUv, cam, par, dep, depth);
  vec2 blur = fx.xy;
  vec3 col;
  if (dot(blur, blur) > 1e-7) {
    // scia lungo il movimento: 9 campioni in coordinate della foto
    vec2 bq = blur * vec2(uFrame / par.w, 1.0) / cam.z;
    col = vec3(0.0);
    for (int k = 0; k < 9; k++) {
      float t = float(k) / 8.0 - 0.5;
      col += textureLod(img, clamp(q + bq * t, 0.001, 0.999), fx.z).rgb;
    }
    col /= 9.0;
  } else {
    col = textureLod(img, q, fx.z).rgb;
  }
  return col * fx.w;
}

void main() {
  float dA, dB = 0.0;
  vec3 a = shade(uA, uDA, uCamA, uParA, uFxA, dA);
  vec3 col = a;
  if (uHasB > 0.5) {
    vec3 b = shade(uB, uDB, uCamB, uParB, uFxB, dB);
    if (uMode == 0) {
      // prima compare il primo piano della foto nuova, poi lo sfondo; sul fronte una riga di luce
      float e = dB + 1.3 * uMix - 1.0;
      float m = smoothstep(0.0, 0.14, e);
      col = mix(a, b, m);
      col += uFlare * exp(-pow(e / 0.05, 2.0)) * 0.9 * (1.0 - uMix * uMix);
    } else if (uMode == 1) {
      float m = smoothstep(0.3, 0.7, uMix);
      col = mix(a, b, m);
      col += uFlare * pow(sin(3.14159 * uMix), 2.0) * 1.4;
    } else {
      col = mix(a, b, uMix);
    }
  }
  // look uniforme: nero profondo, rossi pieni, vignettatura morbida
  col = max(col, 0.0);
  col = col / (1.0 + col * 0.18);
  float l = dot(col, vec3(0.299, 0.587, 0.114));
  col = mix(vec3(l), col, 1.08);
  col = pow(col, vec3(1.06));
  vec2 v = vUv - 0.5;
  col *= 1.0 - 0.55 * smoothstep(0.35, 0.95, length(v * vec2(1.25, 0.95)));
  o = vec4(col, 1.0);
}`;

const compile = (gl: WebGL2RenderingContext, type: number, src: string) => {
  const s = gl.createShader(type)!;
  gl.shaderSource(s, src);
  gl.compileShader(s);
  if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(`Shader foto non compilato: ${gl.getShaderInfoLog(s)}`);
  return s;
};

export class PhotoRenderer {
  readonly canvas: HTMLCanvasElement;
  private gl: WebGL2RenderingContext;
  private tex = new Map<string, WebGLTexture>();
  private loc: Record<string, WebGLUniformLocation | null> = {};

  constructor(w: number, h: number) {
    this.canvas = document.createElement('canvas');
    this.canvas.width = w;
    this.canvas.height = h;
    const gl = this.canvas.getContext('webgl2', {preserveDrawingBuffer: true, antialias: false});
    if (!gl) throw new Error('WebGL2 non disponibile');
    this.gl = gl;
    const prog = gl.createProgram()!;
    gl.attachShader(prog, compile(gl, gl.VERTEX_SHADER, VERT));
    gl.attachShader(prog, compile(gl, gl.FRAGMENT_SHADER, FRAG));
    gl.linkProgram(prog);
    if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) throw new Error(`Link foto fallito: ${gl.getProgramInfoLog(prog)}`);
    gl.useProgram(prog);
    const buf = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
    const aPos = gl.getAttribLocation(prog, 'aPos');
    gl.enableVertexAttribArray(aPos);
    gl.vertexAttribPointer(aPos, 2, gl.FLOAT, false, 0, 0);
    for (const n of ['uA', 'uDA', 'uB', 'uDB', 'uCamA', 'uParA', 'uFxA', 'uCamB', 'uParB', 'uFxB', 'uMix', 'uFrame', 'uHasB', 'uMode', 'uFlare']) {
      this.loc[n] = gl.getUniformLocation(prog, n);
    }
    gl.uniform1i(this.loc.uA, 0);
    gl.uniform1i(this.loc.uDA, 1);
    gl.uniform1i(this.loc.uB, 2);
    gl.uniform1i(this.loc.uDB, 3);
    gl.viewport(0, 0, w, h);
  }

  private texture(name: string) {
    const hit = this.tex.get(name);
    if (hit) return hit;
    const gl = this.gl;
    const t = gl.createTexture()!;
    gl.bindTexture(gl.TEXTURE_2D, t);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, IMG[name]);
    gl.generateMipmap(gl.TEXTURE_2D);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR_MIPMAP_LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
    this.tex.set(name, t);
    return t;
  }

  private bind(s: Shot, unit: number, cam: string, par: string, fx: string) {
    const gl = this.gl;
    const img = IMG[s.key];
    gl.activeTexture(gl.TEXTURE0 + unit);
    gl.bindTexture(gl.TEXTURE_2D, this.texture(s.key));
    gl.activeTexture(gl.TEXTURE0 + unit + 1);
    gl.bindTexture(gl.TEXTURE_2D, this.texture(`${s.key}_depth`));
    gl.uniform4f(this.loc[cam], s.cx, s.cy, s.zoom, s.rot ?? 0);
    gl.uniform4f(this.loc[par], s.px ?? 0, s.py ?? 0, s.focus ?? 0.5, img.naturalWidth / img.naturalHeight);
    gl.uniform4f(this.loc[fx], (s.bx ?? 0) / 1080, (s.by ?? 0) / 1920, s.defocus ?? 0, s.exposure ?? 1);
  }

  /** Disegna `a`, oppure il passaggio da `a` a `b` (mix 0..1). */
  render(a: Shot, b: Shot | null, mix: number, mode: Mode, flare: [number, number, number] = [1, 0.35, 0.3]) {
    const gl = this.gl;
    this.bind(a, 0, 'uCamA', 'uParA', 'uFxA');
    if (b) this.bind(b, 2, 'uCamB', 'uParB', 'uFxB');
    gl.uniform1f(this.loc.uHasB, b ? 1 : 0);
    gl.uniform1f(this.loc.uMix, mix);
    gl.uniform1i(this.loc.uMode, MODE[mode]);
    gl.uniform1f(this.loc.uFrame, 1080 / 1920);
    gl.uniform3f(this.loc.uFlare, ...flare);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
    return this.canvas;
  }
}
