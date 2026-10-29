import {CULL_COLS, CULL_ROWS, CULL_SLOTS, CULL_TILE, FRAG, MAX_SHAPES, SHAPE_TEXELS, VERT} from './shader';

export type Kind = 'box' | 'circle' | 'shell' | 'tri';
const KIND: Record<Kind, number> = {box: 0, circle: 1, shell: 2, tri: 3};

/** Un elemento di vetro. Coordinate e misure in pixel di progetto (1080×1920). */
export type Glass = {
  x: number;
  y: number;
  /** semi-larghezza (per 'circle' e 'tri': raggio) */
  w: number;
  h?: number;
  kind?: Kind;
  /** raggio degli angoli */
  r?: number;
  /** distanza entro cui si fonde con il vetro vicino (come GlassEffectContainer) */
  k?: number;
  rot?: number;
  tint?: [number, number, number];
  tintAmt?: number;
  /** smerigliatura 0..1 (0 ≈ variante "clear") */
  frost?: number;
  /** larghezza del bordo che fa da lente */
  refr?: number;
  /** comparsa 0..1: modula curvatura della luce, riflessi e ombra */
  mat?: number;
  /** ingrandimento (lente) */
  mag?: number;
  /** oscuramento del contenuto sotto il vetro, per la leggibilità */
  dim?: number;
  /** illuminazione al tocco e suo punto */
  glow?: number;
  gx?: number;
  gy?: number;
  /** dispersione cromatica aggiuntiva */
  disp?: number;
  /** spessore per le cornici */
  thick?: number;
};

const compile = (gl: WebGL2RenderingContext, type: number, src: string) => {
  const s = gl.createShader(type)!;
  gl.shaderSource(s, src);
  gl.compileShader(s);
  if (!gl.getShaderParameter(s, gl.COMPILE_STATUS)) throw new Error(`Shader non compilato: ${gl.getShaderInfoLog(s)}`);
  return s;
};

export class GlassRenderer {
  private gl: WebGL2RenderingContext;
  private shapesTex: WebGLTexture;
  private cullTex: WebGLTexture;
  private contentTex: WebGLTexture;
  private data = new Float32Array(MAX_SHAPES * SHAPE_TEXELS * 4);
  private cull = new Float32Array(CULL_SLOTS * CULL_COLS * CULL_ROWS);
  private loc: Record<string, WebGLUniformLocation | null> = {};

  constructor(private canvas: HTMLCanvasElement, private scale: number) {
    const gl = canvas.getContext('webgl2', {preserveDrawingBuffer: true, antialias: false, premultipliedAlpha: false});
    if (!gl) throw new Error('WebGL2 non disponibile');
    this.gl = gl;
    const prog = gl.createProgram()!;
    gl.attachShader(prog, compile(gl, gl.VERTEX_SHADER, VERT));
    gl.attachShader(prog, compile(gl, gl.FRAGMENT_SHADER, FRAG));
    gl.linkProgram(prog);
    if (!gl.getProgramParameter(prog, gl.LINK_STATUS)) throw new Error(`Link fallito: ${gl.getProgramInfoLog(prog)}`);
    gl.useProgram(prog);
    const buf = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, buf);
    gl.bufferData(gl.ARRAY_BUFFER, new Float32Array([-1, -1, 3, -1, -1, 3]), gl.STATIC_DRAW);
    const aPos = gl.getAttribLocation(prog, 'aPos');
    gl.enableVertexAttribArray(aPos);
    gl.vertexAttribPointer(aPos, 2, gl.FLOAT, false, 0, 0);

    const make = (unit: number, minFilter: number) => {
      const t = gl.createTexture()!;
      gl.activeTexture(gl.TEXTURE0 + unit);
      gl.bindTexture(gl.TEXTURE_2D, t);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, minFilter);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, minFilter === gl.NEAREST ? gl.NEAREST : gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
      return t;
    };
    this.contentTex = make(0, gl.LINEAR_MIPMAP_LINEAR);
    this.shapesTex = make(1, gl.NEAREST);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA32F, SHAPE_TEXELS, MAX_SHAPES, 0, gl.RGBA, gl.FLOAT, this.data);
    this.cullTex = make(2, gl.NEAREST);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.R32F, CULL_SLOTS, CULL_COLS * CULL_ROWS, 0, gl.RED, gl.FLOAT, this.cull);
    for (const n of ['uRes', 'uScale', 'uTime', 'uLight', 'uContent', 'uShapes', 'uCull']) this.loc[n] = gl.getUniformLocation(prog, n);
  }

  render(content: HTMLCanvasElement, glass: Glass[], time: number, light: [number, number]) {
    const {gl, loc} = this;
    gl.viewport(0, 0, this.canvas.width, this.canvas.height);

    gl.activeTexture(gl.TEXTURE0);
    gl.bindTexture(gl.TEXTURE_2D, this.contentTex);
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, content);
    gl.generateMipmap(gl.TEXTURE_2D);

    const shapes = glass.filter((s) => (s.mat ?? 1) > 0.001 && s.w > 0.05).slice(0, MAX_SHAPES);
    this.data.fill(0);
    shapes.forEach((s, i) => {
      const t = s.tint ?? [1, 1, 1];
      this.data.set(
        [
          s.x, s.y, s.w, s.h ?? s.w,
          s.r ?? 0, KIND[s.kind ?? 'box'], s.k ?? 0, s.rot ?? 0,
          t[0], t[1], t[2], s.tintAmt ?? 0,
          s.frost ?? 0.5, s.refr ?? 1, s.mat ?? 1, s.mag ?? 0,
          s.dim ?? 0, s.glow ?? 0, s.gx ?? s.x, s.gy ?? s.y,
          s.disp ?? 0, s.thick ?? 0, 0, 0,
        ],
        i * SHAPE_TEXELS * 4,
      );
    });
    gl.activeTexture(gl.TEXTURE1);
    gl.bindTexture(gl.TEXTURE_2D, this.shapesTex);
    gl.texSubImage2D(gl.TEXTURE_2D, 0, 0, 0, SHAPE_TEXELS, MAX_SHAPES, gl.RGBA, gl.FLOAT, this.data);

    this.buildCull(shapes);
    gl.activeTexture(gl.TEXTURE2);
    gl.bindTexture(gl.TEXTURE_2D, this.cullTex);
    gl.texSubImage2D(gl.TEXTURE_2D, 0, 0, 0, CULL_SLOTS, CULL_COLS * CULL_ROWS, gl.RED, gl.FLOAT, this.cull);

    gl.uniform2f(loc.uRes, this.canvas.width, this.canvas.height);
    gl.uniform1f(loc.uScale, this.scale);
    gl.uniform1f(loc.uTime, time);
    gl.uniform2f(loc.uLight, light[0], light[1]);
    gl.uniform1i(loc.uContent, 0);
    gl.uniform1i(loc.uShapes, 1);
    gl.uniform1i(loc.uCull, 2);
    gl.drawArrays(gl.TRIANGLES, 0, 3);
    gl.finish();
  }

  /** Per ogni tassello, gli elementi il cui ingombro (più fusione, bordo e ombra) lo tocca. */
  private buildCull(shapes: Glass[]) {
    this.cull.fill(0);
    shapes.forEach((s, i) => {
      const w = s.w;
      const h = s.h ?? s.w;
      const kind = s.kind ?? 'box';
      const reach = kind === 'circle' ? w : kind === 'tri' ? w * 1.2 + (s.r ?? 0) : Math.hypot(w, h) + (s.thick ?? 0);
      const m = reach + (s.k ?? 0) + 140;
      const c0 = Math.max(0, Math.floor((s.x - m) / CULL_TILE));
      const c1 = Math.min(CULL_COLS - 1, Math.floor((s.x + m) / CULL_TILE));
      const r0 = Math.max(0, Math.floor((s.y - m) / CULL_TILE));
      const r1 = Math.min(CULL_ROWS - 1, Math.floor((s.y + m) / CULL_TILE));
      for (let r = r0; r <= r1; r++) {
        for (let c = c0; c <= c1; c++) {
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
