import {CULL_COLS, CULL_ROWS, CULL_SLOTS, CULL_TILE, FRAG, MAX_SHAPES, SHAPE_TEXELS, VERT} from './shader';

export type Kind = 'box' | 'circle' | 'shell' | 'tri' | 'ring' | 'cup' | 'liquid';
const KIND: Record<Kind, number> = {box: 0, circle: 1, shell: 2, tri: 3, ring: 4, cup: 5, liquid: 6};

/** Una forma di vetro. Coordinate e misure in pixel di progetto (1080×1920). */
export type Shape = {
  x: number;
  y: number;
  /** semi-larghezza (per 'circle', 'ring', 'tri': raggio) */
  w: number;
  /** semi-altezza */
  h?: number;
  kind?: Kind;
  /** raggio degli angoli */
  r?: number;
  /** quanto si fonde con le forme vicine (px): 0 = bordi netti */
  k?: number;
  rot?: number;
  tint?: [number, number, number];
  tintAmt?: number;
  /** livello del liquido interno 0..1 (per 'liquid': altezza del liquido) */
  fill?: number;
  /** spessore per cornici, anelli e vasi */
  thick?: number;
  /** intensità della rifrazione (larghezza del bordo curvo) */
  refr?: number;
  /** smerigliatura 0..1 */
  frost?: number;
  /** ingrandimento della lente (0 = nessuno) */
  mag?: number;
  /** ampiezza dell'onda sulla superficie del liquido */
  wave?: number;
};

export type Beads = {
  cell: number;
  r: number;
  k: number;
  x0: number;
  y0: number;
  cols: number;
  rows: number;
  /** centro e raggio dell'onda che fa comparire le perle */
  cx: number;
  cy: number;
  reveal: number;
  shrink: number;
  tint: [number, number, number];
  tintAmt: number;
  waveAmp: number;
  waveFreq: number;
  waveSpeed: number;
  redCol: number;
  redRow: number;
  redAmt: number;
  redGone: number;
  side: number;
};

export type Tiles = {x0: number; y0: number; cell: number; size: number; cols: number; rows: number; lit: number; side: number};
export type Chart = {x0: number; x1: number; ys: number[]; reveal: number; redFrom: number; baseY: number; side: number; alpha: number};

export type World = {
  shapes: Shape[];
  accA: [number, number, number];
  accB: [number, number, number];
  ring?: {x: number; y: number; r: number; thick: number};
  ripple?: {x: number; y: number; age: number; amp: number};
  beads?: Beads;
  tiles?: Tiles;
  chart?: Chart;
};

const compile = (gl: WebGL2RenderingContext, type: number, src: string) => {
  const s = gl.createShader(type)!;
  gl.shaderSource(s, src);
  gl.compileShader(s);
  if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) {
    throw new Error(`Shader non compilato: ${gl.getShaderInfoLog(s)}`);
  }
  return s;
};

export class GlassRenderer {
  private gl: WebGL2RenderingContext;
  private prog: WebGLProgram;
  private tex: WebGLTexture;
  private cullTex: WebGLTexture;
  private data = new Float32Array(MAX_SHAPES * SHAPE_TEXELS * 4);
  private cull = new Float32Array(CULL_SLOTS * CULL_COLS * CULL_ROWS);
  private loc: Record<string, WebGLUniformLocation | null> = {};

  constructor(private canvas: HTMLCanvasElement, private scale: number) {
    const gl = canvas.getContext('webgl2', {preserveDrawingBuffer: true, antialias: false, premultipliedAlpha: false});
    if (!gl) throw new Error('WebGL2 non disponibile in questo browser');
    this.gl = gl;
    const prog = gl.createProgram()!;
    gl.attachShader(prog, compile(gl, gl.VERTEX_SHADER, VERT));
    gl.attachShader(prog, compile(gl, gl.FRAGMENT_SHADER, FRAG));
    gl.linkProgram(prog);
    if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) throw new Error(`Link fallito: ${gl.getProgramInfoLog(prog)}`);
    this.prog = prog;
    gl.useProgram(prog);

    const buf = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
    const aPos = gl.getAttribLocation(prog, 'aPos');
    gl.enableVertexAttribArray(aPos);
    gl.vertexAttribPointer(aPos, 2, gl.FLOAT, false, 0, 0);

    this.tex = gl.createTexture()!;
    gl.activeTexture(gl.TEXTURE0);
    gl.bindTexture(gl.TEXTURE_2D, this.tex);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA32F, SHAPE_TEXELS, MAX_SHAPES, 0, gl.RGBA, gl.FLOAT, this.data);

    this.cullTex = gl.createTexture()!;
    gl.activeTexture(gl.TEXTURE1);
    gl.bindTexture(gl.TEXTURE_2D, this.cullTex);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.NEAREST);
    gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.NEAREST);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.R32F, CULL_SLOTS, CULL_COLS * CULL_ROWS, 0, gl.RED, gl.FLOAT, this.cull);

    for (const n of ['uRes', 'uScale', 'uTime', 'uShapes', 'uCull', 'uAccA', 'uAccB', 'uRing', 'uRipple',
      'uBeadA', 'uBeadB', 'uBeadC', 'uBeadD', 'uBeadE', 'uBeadF', 'uTilesA', 'uTilesB', 'uChartA', 'uChartB', 'uY']) {
      this.loc[n] = gl.getUniformLocation(prog, n);
    }
  }

  render(world: World, time: number) {
    const {gl, loc} = this;
    gl.viewport(0, 0, this.canvas.width, this.canvas.height);
    const shapes = world.shapes.slice(0, MAX_SHAPES);
    this.data.fill(0);
    shapes.forEach((s, i) => {
      const o = i * SHAPE_TEXELS * 4;
      const t = s.tint ?? [1, 1, 1];
      this.data.set(
        [
          s.x, s.y, Math.max(0, s.w), Math.max(0, s.h ?? s.w),
          s.r ?? 0, KIND[s.kind ?? 'box'], s.k ?? 0, s.rot ?? 0,
          t[0], t[1], t[2], s.tintAmt ?? 0,
          s.fill ?? 0, s.thick ?? 0, s.refr ?? 1, s.frost ?? 0,
          s.mag ?? 0, s.wave ?? 0, 0, 0,
        ],
        o,
      );
    });
    gl.activeTexture(gl.TEXTURE0);
    gl.bindTexture(gl.TEXTURE_2D, this.tex);
    gl.texSubImage2D(gl.TEXTURE_2D, 0, 0, 0, SHAPE_TEXELS, MAX_SHAPES, gl.RGBA, gl.FLOAT, this.data);

    this.buildCull(shapes);
    gl.activeTexture(gl.TEXTURE1);
    gl.bindTexture(gl.TEXTURE_2D, this.cullTex);
    gl.texSubImage2D(gl.TEXTURE_2D, 0, 0, 0, CULL_SLOTS, CULL_COLS * CULL_ROWS, gl.RED, gl.FLOAT, this.cull);

    gl.uniform2f(loc.uRes, this.canvas.width, this.canvas.height);
    gl.uniform1f(loc.uScale, this.scale);
    gl.uniform1f(loc.uTime, time);
    gl.uniform1i(loc.uShapes, 0);
    gl.uniform1i(loc.uCull, 1);
    gl.uniform3f(loc.uAccA, ...world.accA);
    gl.uniform3f(loc.uAccB, ...world.accB);
    const ring = world.ring;
    gl.uniform4f(loc.uRing, ring?.x ?? 0, ring?.y ?? 0, ring?.r ?? 0, ring ? ring.thick : 0);
    const rp = world.ripple;
    gl.uniform4f(loc.uRipple, rp?.x ?? 0, rp?.y ?? 0, rp?.age ?? 0, rp ? rp.amp : 0);

    const b = world.beads;
    gl.uniform4f(loc.uBeadA, b?.cell ?? 1, b?.r ?? 0, b ? 1 : 0, b?.k ?? 0);
    gl.uniform4f(loc.uBeadB, b?.cx ?? 0, b?.cy ?? 0, b?.reveal ?? 0, b?.shrink ?? 0);
    gl.uniform4f(loc.uBeadC, b?.x0 ?? 0, b?.y0 ?? 0, b?.cols ?? 0, b?.rows ?? 0);
    gl.uniform4f(loc.uBeadD, b?.redCol ?? -9, b?.redRow ?? -9, b?.redAmt ?? 0, b?.side ?? 2);
    gl.uniform4f(loc.uBeadE, ...(b?.tint ?? [1, 1, 1]), b?.tintAmt ?? 0);
    gl.uniform4f(loc.uBeadF, b?.waveAmp ?? 0, b?.waveFreq ?? 0, b?.waveSpeed ?? 0, b?.redGone ?? 0);

    const tl = world.tiles;
    gl.uniform4f(loc.uTilesA, tl?.x0 ?? 0, tl?.y0 ?? 0, tl?.cell ?? 1, tl ? tl.size : 0);
    gl.uniform4f(loc.uTilesB, tl?.cols ?? 0, tl?.rows ?? 0, tl?.lit ?? 0, tl?.side ?? 2);

    const c = world.chart;
    const ys = new Float32Array(48);
    if (c) ys.set(c.ys.slice(0, 48));
    gl.uniform4f(loc.uChartA, c?.x0 ?? 0, c?.x1 ?? 1, c ? Math.min(48, c.ys.length) : 2, c?.reveal ?? 0);
    gl.uniform4f(loc.uChartB, c?.redFrom ?? 999, c?.baseY ?? 0, c?.side ?? 2, c ? c.alpha : 0);
    gl.uniform4fv(loc.uY, ys);

    gl.drawArrays(gl.TRIANGLES, 0, 3);
    gl.finish();
  }

  /** Per ogni tassello, le forme il cui ingombro (più fusione, ombra e bordo) lo tocca. */
  private buildCull(shapes: Shape[]) {
    this.cull.fill(0);
    shapes.forEach((s, i) => {
      const w = Math.max(0, s.w);
      const h = Math.max(0, s.h ?? s.w);
      if (w < 0.05 && h < 0.05) return;
      const kind = s.kind ?? 'box';
      const reach =
        kind === 'circle' ? w : kind === 'ring' ? w + (s.thick ?? 0) : kind === 'tri' ? w * 1.2 + (s.r ?? 0) : Math.hypot(w, h) + (s.thick ?? 0) + (s.wave ?? 0);
      const m = reach + (s.k ?? 0) + 170;
      const c0 = Math.max(0, Math.floor((s.x - m) / CULL_TILE));
      const c1 = Math.min(CULL_COLS - 1, Math.floor((s.x + m) / CULL_TILE));
      const r0 = Math.max(0, Math.floor((s.y - m) / CULL_TILE));
      const r1 = Math.min(CULL_ROWS - 1, Math.floor((s.y + m) / CULL_TILE));
      for (let r = r0; r <= r1; r++) {
        for (let c = c0; c <= c1; c++) {
          // distanza dal tassello al centro della forma
          const dx = Math.max(c * CULL_TILE - s.x, 0, s.x - (c + 1) * CULL_TILE);
          const dy = Math.max(r * CULL_TILE - s.y, 0, s.y - (r + 1) * CULL_TILE);
          if (Math.hypot(dx, dy) > m) continue;
          const o = (r * CULL_COLS + c) * CULL_SLOTS;
          const n = this.cull[o];
          if (n < CULL_SLOTS - 1) {
            this.cull[o + 1 + n] = i;
            this.cull[o] = n + 1;
          }
        }
      }
    });
  }
}
