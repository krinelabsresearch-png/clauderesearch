"""Step 2 - render the OTIUM 12 s loop (100 BPM, 5 bars) frame by frame.

Two-stage compositing for maximum sharpness:
  stage A (native 1122-px flyer grid): paper + photo window (2.5D push-in, live disco balls,
          beams, light spots, sparkles) -> area-resampled once to the output size
  stage B (output grid): every piece of type is re-rasterised from its traced vector outline
          (4x4 supersampled, flat ink) directly at output resolution -> crisp edges, no
          resampling, no grain on the letters.

    python3 render.py --fmt 4x5                       # -> out/OTIUM_4x5_60fps.mp4 + _30fps.mp4
    python3 render.py --fmt 9x16
    python3 render.py --fmt 4x5 --preview 0.3,1.3,3.0  # PNG stills for review
"""
import argparse
import json
import math
import os
import pickle
import subprocess
import time
from multiprocessing import get_context

import numpy as np
import cv2

from common import (LAYERS, OUT, W0, H0, FPS, DURATION, BEAT, BAR, PAPER, RED, PLUM, GLINT,
                    DARK_BG, smoothstep, ease_out_cubic, ease_in_cubic, ease_in_quad,
                    ease_in_out_cubic, ease_out_back, ease_in_out_sine, halftone_screen)

MAN = json.load(open(os.path.join(LAYERS, "manifest.json")))
META = MAN["_meta"]
VEC = pickle.load(open(os.path.join(LAYERS, "vectors.pkl"), "rb"))
B = BEAT
FORMATS = {"4x5": dict(H=H0, out=(1080, 1350)), "9x16": dict(H=1995, out=(1080, 1920))}

# =============================================================== timeline (s) - 100 BPM grid, 5 bars
N_BEATS = int(round(DURATION / B))                       # 20
KICKS = [B * k for k in range(N_BEATS)]
SNARES = sorted(B * (bar * 4 + s) for bar in range(N_BEATS // 4) for s in (0.75, 1.5, 2.75, 3.5))
# opening: star 0 -> 1.5 beats (25% shorter than before), then OTIUM stamps on the dembow hits
T_FLY0, T_FLY1 = B * 1.0, B * 1.5
T_IRIS0, T_IRIS1 = B * 0.95, B * 1.85
LOGO_HITS = [("logo_O", B * 1.5), ("logo_T", B * 2), ("logo_I", B * 2.75), ("logo_U", B * 3),
             ("logo_M", B * 3.5)]
T_LOGO_DONE = LOGO_HITS[-1][1] + 0.25      # after this NOTHING shakes / jitters any more
# bar 2: camera tilts down, photo prints, location
T_PAN0, T_PAN1 = B * 4, B * 4 + 1.15
T_REVEAL = B * 4
T_ATV, ATV_STAG = B * 4.5, B / 8
T_LINE0, T_LINE1 = B * 5.5, B * 6
T_SSTAR = B * 6
T_FIR, FIR_STAG = B * 6.15, B / 14
T_BEAMS = B * 6
# bar 3: date
T_DOM = B * 8
T_DATE = B * 9
T_BSTAR = B * 9.5
T_ROLL0, T_STOP0 = B * 10, B * 10.75
T_SEPS = B * 10.75
# bar 4: genres + CTA
GENRES = [("g_hit", B * 12), ("g_b1", B * 12.5), ("g_reg", B * 13), ("g_b2", B * 13.5),
          ("g_baile", B * 14)]
T_TYPE0, T_TYPE1 = B * 14.5, B * 14.9
T_FILL0, T_FILL1 = B * 15, B * 16
# bar 5: drop + hold + loop close
T_FLASH = B * 16
T_SPIN = B * 18
T_CLOSE0, T_CLOSE1 = DURATION - 0.55, DURATION - 0.12
T_STAR_BACK = DURATION - 0.5

PAD = 560
CAM0 = 540.0
STAR_ROT_SPEED = 0.75
S0 = 2.15
BEAM_COL = np.array([0.96, 0.74, 0.72], np.float32)

# beat-synced jitter only while OTIUM is being stamped in
JOLTS = [(t, 1.0) for _, t in LOGO_HITS]
SHAKES = [(LOGO_HITS[0][1], 1.6), (LOGO_HITS[-1][1], 1.8)]
rng0 = np.random.RandomState(7)
JOLT_DIRS = [(math.cos(a), math.sin(a)) for a in rng0.uniform(0, 2 * np.pi, len(JOLTS))]
SHAKE_PH = rng0.uniform(0, 2 * np.pi, (len(SHAKES), 2))


def cam_y(t):
    if t < T_PAN0:
        return CAM0
    return CAM0 * (1 - ease_in_out_cubic((t - T_PAN0) / (T_PAN1 - T_PAN0)))


def env_kick(t, decay=0.12, times=KICKS):
    v = 0.0
    for k in times:
        if 0 <= t - k < 6 * decay:
            v += math.exp(-(t - k) / decay)
    return v


# =============================================================== vector type
def fill_polys_aa(h, w, polys, ss=4):
    """even-odd fill of several polygons, ss x ss supersampled, 1/16 sub-sample precision."""
    m = np.zeros((h * ss, w * ss), np.uint8)
    pts = [np.round(((p + 0.5) * ss - 0.5) * 16).astype(np.int32) for p in polys]
    cv2.fillPoly(m, pts, 255, lineType=cv2.LINE_8, shift=4)
    return cv2.resize(m, (w, h), interpolation=cv2.INTER_AREA).astype(np.float32) / 255


class VSprite:
    def __init__(self, name):
        m = MAN[name]
        self.name = name
        self.x, self.y, self.w, self.h = m["x"], m["y"], m["w"], m["h"]
        self.polys = [p.astype(np.float32) for p in VEC[name]]
        self.color = np.array(RED if name == "cta_text_red" else m["ink"], np.float32)

    @property
    def cx(self):
        return self.x + self.w / 2

    @property
    def cy(self):
        return self.y + self.h / 2


def _span_cov(n0, n, lo, hi):
    """per-pixel coverage of the interval [lo,hi] (pixel centres at integers)."""
    c = np.arange(n0, n0 + n, dtype=np.float32)
    return np.clip(np.minimum(c + 0.5, hi) - np.maximum(c - 0.5, lo), 0, 1)


class CovBatch:
    """Accumulates the coverage of abutting pieces of one ink (e.g. the letters of the OTIUM
    ligature) and composites them once -> no hairline seams where AA edges meet."""

    def __init__(self, shape, color):
        self.cov = np.zeros(shape[:2], np.float32)
        self.color = np.asarray(color, np.float32)
        self.used = False

    def flush(self, img):
        if self.used:
            a = np.clip(self.cov, 0, 1)[..., None]
            img *= 1 - a
            img += a * self.color


def vdraw(img, spr, oyB, dx=0.0, dy=0.0, scale=1.0, rot=0.0, alpha=1.0, anchor=None, clip=None,
          origin=(0.0, 0.0), color=None, batch=None):
    """Rasterise a vector sprite straight onto the output-resolution image.
    All geometry params are in flyer (native) units; clip = native (x0,y0,x1,y1)."""
    if alpha <= 0.003 or scale <= 0.01:
        return
    C = CTX
    SX, SY = C.SX, C.SY
    rest = scale == 1.0 and rot == 0.0
    key = None
    hit = None
    if rest and clip is None and C.cache_ok:
        key = (spr.name, round(dx * 64), round((dy + oyB) * 64), origin)
        hit = C.vcache.get(key)
    if hit is None:
        ax, ay = anchor if anchor is not None else (spr.cx, spr.cy)
        c, s = math.cos(rot) * scale, math.sin(rot) * scale
        polys = []
        for P in spr.polys:
            if rest:
                X, Y = P[:, 0] + dx, P[:, 1] + dy
            else:
                X = ax + c * (P[:, 0] - ax) - s * (P[:, 1] - ay) + dx
                Y = ay + s * (P[:, 0] - ax) + c * (P[:, 1] - ay) + dy
            polys.append(np.stack([X * SX - origin[0], (Y + oyB) * SY - origin[1]], 1))
        allp = np.concatenate(polys)
        x0, x1 = int(math.floor(allp[:, 0].min())) - 1, int(math.ceil(allp[:, 0].max())) + 2
        y0, y1 = int(math.floor(allp[:, 1].min())) - 1, int(math.ceil(allp[:, 1].max())) + 2
        if clip is not None:
            cx0, cx1 = clip[0] * SX - origin[0], clip[2] * SX - origin[0]
            cy0, cy1 = (clip[1] + oyB) * SY - origin[1], (clip[3] + oyB) * SY - origin[1]
            x0, x1 = max(x0, int(math.floor(cx0))), min(x1, int(math.ceil(cx1)) + 1)
            y0, y1 = max(y0, int(math.floor(cy0))), min(y1, int(math.ceil(cy1)) + 1)
        x0, y0 = max(x0, 0), max(y0, 0)
        x1, y1 = min(x1, img.shape[1]), min(y1, img.shape[0])
        if x1 <= x0 or y1 <= y0:
            return
        off = np.array([x0, y0], np.float32)
        cov = fill_polys_aa(y1 - y0, x1 - x0, [p - off for p in polys])
        if clip is not None:      # anti-aliased (sub-pixel) mask edges
            cov *= _span_cov(y0, y1 - y0, cy0, cy1)[:, None] * _span_cov(x0, x1 - x0, cx0, cx1)[None, :]
        if key is not None:
            C.vcache[key] = (cov, x0, y0)
    else:
        cov, x0, y0 = hit
    h, w = cov.shape
    if batch is not None:
        batch.cov[y0:y0 + h, x0:x0 + w] += cov * alpha
        batch.used = True
        return
    a = (cov * alpha)[..., None]
    col = spr.color if color is None else np.asarray(color, np.float32)
    roi = img[y0:y0 + h, x0:x0 + w]
    if img.shape[2] == 4:
        roi[..., :3] = roi[..., :3] * (1 - a) + col * a
        roi[..., 3:] = roi[..., 3:] * (1 - a) + a
    else:
        roi *= 1 - a
        roi += a * col


_star = VEC["logo_star"]
_sp = max(_star, key=lambda p: abs(cv2.contourArea(p)))
_mo = cv2.moments(_sp)
STAR_HOME = (float(_mo["m10"] / _mo["m00"]), float(_mo["m01"] / _mo["m00"]))
STAR_PTS = (_sp - np.array(STAR_HOME, np.float32)).astype(np.float32)


def draw_star(img, cx, cy, scale, rot, color, alpha=1.0, blur_samples=None):
    """vector star in the pixel coords of `img`; blur_samples = [(cx,cy,scale,rot), ...]."""
    samples = blur_samples or [(cx, cy, scale, rot)]
    Hc, Wc = img.shape[:2]
    rmax = max(s[2] for s in samples) * 80 + 4
    xs_ = [s[0] for s in samples]
    ys_ = [s[1] for s in samples]
    x0, x1 = int(max(0, min(xs_) - rmax)), int(min(Wc, max(xs_) + rmax))
    y0, y1 = int(max(0, min(ys_) - rmax)), int(min(Hc, max(ys_) + rmax))
    if x1 <= x0 or y1 <= y0 or alpha <= 0.003:
        return
    cov = np.zeros((y1 - y0, x1 - x0), np.float32)
    for (sx, sy, sc, sr) in samples:
        c, s = math.cos(sr) * sc, math.sin(sr) * sc
        P = np.stack([STAR_PTS[:, 0] * c - STAR_PTS[:, 1] * s + sx - x0,
                      STAR_PTS[:, 0] * s + STAR_PTS[:, 1] * c + sy - y0], 1)
        cov += fill_polys_aa(y1 - y0, x1 - x0, [P], ss=4)
    cov = (cov / len(samples) * alpha)[..., None]
    roi = img[y0:y1, x0:x1]
    roi *= 1 - cov
    roi += cov * np.asarray(color, np.float32)


# =============================================================== mirror ball
def render_ball(img, cx, cy, R, theta, env, R0, t, seed, tilt=-0.5, n_lat=30, glint=0.0, ss=2):
    """Mirror ball with a rotating tile grid; each facet re-samples the (fixed) reflection
    map taken from the original flyer -> same look, but the ball really turns."""
    H, W = img.shape[:2]
    x0, x1 = int(max(0, cx - R - 2)), int(min(W, cx + R + 3))
    y0, y1 = int(max(0, cy - R - 2)), int(min(H, cy + R + 3))
    if x1 <= x0 or y1 <= y0:
        return
    hh, ww = (y1 - y0) * ss, (x1 - x0) * ss
    yy, xx = np.mgrid[0:hh, 0:ww].astype(np.float32)
    u = ((xx + 0.5) / ss + x0 - cx) / R
    v = ((yy + 0.5) / ss + y0 - cy) / R
    r2 = u * u + v * v
    z = np.sqrt(np.clip(1 - r2, 0, 1))
    ca, sa = math.cos(tilt), math.sin(tilt)
    ct, st = math.cos(theta), math.sin(theta)
    y1_ = v * ca - z * sa
    z1 = v * sa + z * ca
    xo = u * ct + z1 * st
    zo = -u * st + z1 * ct
    lat = np.arcsin(np.clip(y1_, -1, 1))
    lon = np.arctan2(xo, zo)
    dl = np.pi / n_lat
    bi = np.clip(np.floor((lat + np.pi / 2) / dl), 0, n_lat - 1)
    latc = -np.pi / 2 + (bi + 0.5) * dl
    nl = np.maximum(4, np.round(2 * n_lat * np.cos(latc) / 4) * 4)
    fj = (lon + np.pi) / (2 * np.pi) * nl
    j = np.floor(fj)
    flon = fj - j
    flat = (lat + np.pi / 2) / dl - bi
    lonc = -np.pi + (j + 0.5) / nl * 2 * np.pi
    xoc = np.cos(latc) * np.sin(lonc)
    yoc = np.sin(latc)
    zoc = np.cos(latc) * np.cos(lonc)
    x1c = xoc * ct - zoc * st
    z1c = xoc * st + zoc * ct
    uc = x1c
    vc = yoc * ca + z1c * sa
    h1 = np.abs(np.modf(np.sin(bi * 12.9898 + j * 78.233 + seed) * 43758.5453)[0])
    h2 = np.abs(np.modf(np.sin(bi * 39.346 + j * 11.135 + seed * 1.7) * 24634.6345)[0])
    h3 = np.abs(np.modf(np.sin(bi * 73.156 + j * 52.235 + seed * 2.3) * 12543.4567)[0])
    su = uc + (h1 - 0.5) * 0.20
    sv = vc + (h2 - 0.5) * 0.20
    rr = np.sqrt(su * su + sv * sv)
    kk = np.where(rr > 0.97, 0.97 / np.maximum(rr, 1e-6), 1.0)
    su, sv = su * kk, sv * kk
    es = env.shape[0]
    mx = (su * R0 + es / 2).astype(np.float32)
    my = (sv * R0 + es / 2).astype(np.float32)
    val = cv2.remap(env, mx, my, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
    val = (val - 0.5) * 1.18 + 0.5
    val = val * (0.82 + 0.36 * h3)
    g = np.minimum(np.minimum(flon, 1 - flon), np.minimum(flat, 1 - flat))
    val = val * (0.42 + 0.58 * smoothstep(0.02, 0.14, g))
    tw = np.sin(t * 7.0 + h1 * 40.0 + j * 0.9) * 0.5 + 0.5
    hot = (h2 > 0.93) * smoothstep(0.55, 0.85, val) * tw * (0.6 + glint)
    val = np.clip(val + hot * 0.6, 0, 1.2)
    gx_ = (xx + 0.5) / ss + x0
    gy_ = (yy + 0.5) / ss + y0
    uu = (gx_ + gy_) * 0.7071 / 4.6
    vv = (gy_ - gx_) * 0.7071 / 4.6
    sd = ((uu % 1.0 - 0.5) ** 2 + (vv % 1.0 - 0.5) ** 2) * 2.0
    ink = 1 - np.clip(val, 0, 1)
    dots = smoothstep(sd - 0.1, sd + 0.1, ink)
    val = val - 0.16 * (dots - ink)
    idx = np.clip(val * 255, 0, 255).astype(np.int32)
    col = CTX.lut[idx]
    over = smoothstep(0.85, 1.15, val)[..., None]
    col = col * (1 - over) + GLINT * over
    a = np.clip((1 - np.sqrt(r2)) * R + 0.5, 0, 1)
    rgba = np.dstack([col * a[..., None], a]).astype(np.float32)
    if ss > 1:
        rgba = cv2.resize(rgba, (x1 - x0, y1 - y0), interpolation=cv2.INTER_AREA)
    roi = img[y0:y1, x0:x1]
    roi *= 1 - rgba[..., 3:4]
    roi += rgba[..., :3]


# =============================================================== per-format context
class Ctx:
    pass


CTX = Ctx()


def smooth_noise(shape, sigma, seed):
    r = np.random.RandomState(seed)
    n = cv2.GaussianBlur(r.randn(*shape).astype(np.float32), (0, 0), sigma)
    return n / (n.std() + 1e-6)


def init_ctx(fmt):
    D = np.load(os.path.join(LAYERS, "data.npz"))
    C = CTX
    C.fmt = fmt
    C.H = FORMATS[fmt]["H"]
    C.out = FORMATS[fmt]["out"]
    C.oy = (C.H - H0) // 2
    C.SX = C.out[0] / W0
    C.SY = C.out[1] / C.H
    C.PAD = PAD
    C.vcache = {}
    C.cache_ok = False
    oy, Hc = C.oy, C.H
    Wo, Ho = C.out
    # ---- stage A paper (padded above for the opening camera position), static fibre texture
    pl = D["paper_low"]
    top_n = oy + PAD
    top = np.repeat(pl[:30].mean(0, keepdims=True), top_n, 0)
    bot = np.repeat(pl[-30:].mean(0, keepdims=True), Hc - H0 - oy, 0)
    full = np.concatenate([top, pl, bot], 0)
    full = cv2.GaussianBlur(full, (0, 0), 12)
    full[top_n + 60:top_n + H0 - 60] = pl[60:-60]
    Hp = PAD + Hc
    fib = 0.6 * smooth_noise((Hp, W0), 0.7, 1) + 0.4 * smooth_noise((Hp, W0), 2.5, 2)
    C.paper = (full * (1 + 0.010 * fib[..., None])).astype(np.float32)
    C.paper_ref_out = cv2.resize(C.paper[PAD:PAD + Hc], C.out, interpolation=cv2.INTER_AREA)
    # ---- photo window data (native)
    pa = D["photo_alpha"]
    rows = np.where(pa.max(1) > 0.001)[0]
    C.py0, C.py1 = int(rows.min()), int(rows.max()) + 1
    sl = slice(C.py0, C.py1)
    C.photo_alpha = pa[sl]
    C.plate = D["plate"]
    C.depth = D["depth"][sl]
    C.sway_L = D["sway_L"][sl]
    C.sway_R = D["sway_R"][sl]
    C.lum = D["src"][sl].mean(2)
    C.env1, C.env2, C.lut = D["env1"], D["env2"], D["lut"]
    ph = C.py1 - C.py0
    C.pX, C.pY = np.meshgrid(np.arange(W0, dtype=np.float32),
                             np.arange(C.py0, C.py1, dtype=np.float32))
    C.scr_reveal = halftone_screen(ph, W0, cell=9.0, angle_deg=45, oy=C.py0)
    C.scr_beam = halftone_screen(ph, W0, cell=5.0, angle_deg=15, oy=C.py0)
    C.bX, C.bY = np.meshgrid(np.arange(0, W0, 2, dtype=np.float32),
                             np.arange(C.py0, C.py1, 2, dtype=np.float32))
    # ---- stage B (output-res) helpers for the opening / closing
    C.ogx, C.ogy = np.meshgrid(np.arange(Wo, dtype=np.float32), np.arange(Ho, dtype=np.float32))
    C.scr_dark = halftone_screen(Ho, Wo, cell=12.0 * C.SX, angle_deg=45)
    C.scr_iris = halftone_screen(Ho, Wo, cell=16.0 * C.SX, angle_deg=30)
    C.dgrain = [(0.65 * smooth_noise((Ho, Wo), 0.6, 10 + i) + 0.35 * smooth_noise((Ho, Wo), 1.8, 20 + i))
                .astype(np.float32) for i in range(4)]
    C.spr = {k: VSprite(k) for k in MAN if not k.startswith("_")}
    # ---- deterministic random events
    r = np.random.RandomState(11)
    C.spots = []
    while len(C.spots) < 90:
        x, y = r.uniform(0, W0), r.uniform(C.py0 + 20, 930)
        if math.hypot(x - 546, y - 665) < 140 or C.lum[int(y) - C.py0, int(x)] > 0.75:
            continue
        C.spots.append((x, y, r.uniform(16, 34), r.uniform(1.3, 3.0), r.uniform(0.9, 2.2), r.uniform(0, 3)))
    C.sparkles = []
    for q in range(int((T_REVEAL + 1.5) / (B / 4)), int((T_CLOSE0 - 0.1) / (B / 4))):
        tq = B * q / 4
        n = 2 if q % 4 == 0 else (1 if r.rand() < 0.45 else 0)
        for _ in range(n):
            a_, rr = r.uniform(0, 2 * np.pi), math.sqrt(r.uniform(0.02, 0.8))
            C.sparkles.append(("ball", tq + r.uniform(0, 0.05), math.cos(a_) * rr, math.sin(a_) * rr,
                               r.uniform(0.11, 0.24), r.uniform(0, np.pi)))
        if r.rand() < 0.22:
            lx, ly = META["LIGHTS"][r.randint(len(META["LIGHTS"]))]
            C.sparkles.append(("abs", tq, lx, ly + 4, r.uniform(0.12, 0.2), r.uniform(0, np.pi)))
    glyph_pool = ["t_1", "t_8", "t_0d", "t_2", "t_4"]
    C.reels = []
    for k, name in enumerate(META["slots"]):
        seq = []
        for i in range(7 + k):
            g = glyph_pool[r.randint(len(glyph_pool))]
            while seq and g == seq[-1]:
                g = glyph_pool[r.randint(len(glyph_pool))]
            seq.append(g)
        C.reels.append((name, seq))


# =============================================================== stage A: photo
ZC = (546.0, 540.0)


def cam_k(t):
    return ease_in_out_sine((t - T_REVEAL) / (T_CLOSE1 - T_REVEAL)) if t > T_REVEAL else 0.0


def to_view(x, y, d, k):
    s = 1 + k * (0.026 + 0.04 * d)
    return ZC[0] + (x - ZC[0]) * s - 9.0 * k * d, ZC[1] + (y - ZC[1]) * s + 3.0 * k * d, s


def light_intensity(i, t):
    if t < T_BEAMS:
        return 0.0
    base = 0.48 * ease_out_cubic((t - T_BEAMS) / 0.7)
    hits = KICKS if i % 2 == 0 else SNARES
    pulse = 0.75 * env_kick(t, 0.18, hits)
    flash = 1.2 * math.exp(-(t - T_FLASH) / 0.2) if t >= T_FLASH else 0.0
    fade = 1 - smoothstep(T_CLOSE0, T_CLOSE1, t)
    return (base + pulse + flash) * fade


def render_photo(t):
    C = CTX
    k = cam_k(t)
    d = C.depth
    s = 1 + k * (0.026 + 0.04 * d)
    mx = ZC[0] + (C.pX - ZC[0] + 9.0 * k * d) / s
    my = ZC[1] + (C.pY - ZC[1] - 3.0 * k * d) / s
    swL = 3.2 * math.sin(2 * math.pi * 0.42 * t + 0.4) + 1.2 * math.sin(2 * math.pi * 1.1 * t)
    swR = 3.6 * math.sin(2 * math.pi * 0.36 * t + 2.1) + 1.0 * math.sin(2 * math.pi * 0.9 * t + 1)
    sw = C.sway_L * swL + C.sway_R * swR
    mx -= sw
    my -= sw * 0.25
    img = cv2.remap(C.plate, mx.astype(np.float32), my.astype(np.float32), cv2.INTER_CUBIC,
                    borderMode=cv2.BORDER_REFLECT)
    img = np.clip(img, 0, 1)
    py0 = C.py0

    # mirror-ball light spots drifting over the walls
    if t > T_REVEAL + 0.6:
        ov = np.zeros(img.shape[:2], np.float32)
        fade = smoothstep(T_REVEAL + 0.6, T_REVEAL + 1.6, t) * (1 - smoothstep(T_CLOSE0, T_CLOSE1, t))
        for (x, y, v, rad, life, ph) in C.spots:
            xx = (x + v * t) % W0
            a = math.sin(math.pi * (((t + ph) / life) % 1.0)) ** 2 * fade
            if a < 0.02:
                continue
            vx, vy, _ = to_view(xx, y, 0.15, k)
            cv2.ellipse(ov, (int(vx * 8), int((vy - py0) * 8)), (int(rad * 8 * 1.4), int(rad * 8)), 0, 0,
                        360, a, -1, cv2.LINE_AA, 3)
        ov = cv2.GaussianBlur(ov, (0, 0), 0.9)
        img = 1 - (1 - img) * (1 - ov[..., None] * GLINT * 0.85)

    # moving-head beams (half-res field, printed through a halftone screen)
    if t > T_BEAMS:
        A = np.zeros(C.bX.shape, np.float32)
        for i, (lx, ly) in enumerate(META["LIGHTS"]):
            I = light_intensity(i, t)
            if I < 0.01:
                continue
            ox, oyv, _ = to_view(lx, ly, 0.28, k)
            sgn = 1 if i % 2 == 0 else -1
            phi = sgn * (0.12 + 0.42 * (0.5 + 0.5 * math.sin(2 * math.pi * (t - T_BEAMS) / BAR + i * 0.5)))
            phi += 0.10 * math.sin(2 * math.pi * t / (2 * BAR) + i)
            ddx, ddy = C.bX - ox, C.bY - oyv
            ang = np.arctan2(ddx, ddy)
            dist = np.sqrt(ddx * ddx + ddy * ddy)
            spread = 0.05 + 0.00012 * dist
            core = smoothstep(spread, spread * 0.3, np.abs(ang - phi))
            fall = np.exp(-dist / 600) * smoothstep(8, 50, dist) * (ddy > 0)
            A += I * core * fall
        A = cv2.resize(A, (W0, img.shape[0]), interpolation=cv2.INTER_LINEAR)
        A = np.clip(A, 0, 1.4)
        ht = smoothstep(C.scr_beam - 0.12, C.scr_beam + 0.12, A * 1.15)
        Af = np.clip(0.42 * A + 0.62 * ht, 0, 1)
        img = 1 - (1 - img) * (1 - Af[..., None] * BEAM_COL)
        gl = np.zeros(img.shape[:2], np.float32)
        for i, (lx, ly) in enumerate(META["LIGHTS"]):
            I = light_intensity(i, t)
            if I > 0.01:
                ox, oyv, _ = to_view(lx, ly, 0.28, k)
                cv2.circle(gl, (int(ox * 8), int((oyv - py0) * 8)), int(13 * 8), min(1.0, I), -1,
                           cv2.LINE_AA, 3)
        gl = cv2.GaussianBlur(gl, (0, 0), 6)
        img = 1 - (1 - img) * (1 - np.clip(gl * 1.3, 0, 1)[..., None] * GLINT * 0.9)

    # disco balls (small one first, the big one hangs in front)
    theta = 0.22 * t
    glint = 1.0 * math.exp(-(t - T_FLASH) / 0.3) if t >= T_FLASH else 0.0
    for b, env, seed in [(META["BALL2"], C.env2, 3.0), (META["BALL"], C.env1, 1.0)]:
        bx, by, sc = to_view(b["cx"], b["cy"], 0.32, k)
        render_ball(img, bx, by - py0, (b["r"] + 3) * sc, theta, env, b["r"], t, seed, glint=glint)

    # sparkles (vector stars) on the ball and lamps
    bx, by, sc = to_view(META["BALL"]["cx"], META["BALL"]["cy"], 0.32, k)
    R = META["BALL"]["r"] * sc
    for kind, ts, a1, a2, size, rot in C.sparkles:
        u = (t - ts) / 0.34
        if not (0 <= u <= 1):
            continue
        e = math.sin(math.pi * u) ** 0.8
        if kind == "ball":
            x, y = bx + a1 * R, by + a2 * R
        else:
            x, y, _ = to_view(a1, a2, 0.28, k)
        draw_star(img, x, y - py0, size * e, rot + u * 0.9, GLINT, alpha=0.95)
    if T_FLASH <= t < T_FLASH + 0.45:
        u = (t - T_FLASH) / 0.45
        draw_star(img, bx - 0.35 * R, by - 0.38 * R - py0, 0.55 * math.sin(math.pi * u) ** 0.6, 0.3 + u, GLINT)
    return img


def reveal_mask(t):
    C = CTX
    if t <= T_REVEAL:
        return None
    yrel = (C.pY - 340) / 770
    prog = np.clip((t - T_REVEAL - 0.45 * yrel) / 1.25, 0, 1)
    prog = prog * prog * (3 - 2 * prog)
    if prog.min() >= 1:
        return 1.0
    ink = 1 - C.lum
    cov = prog * 1.3 - 0.3 * (1 - ink) * (1 - prog)
    return smoothstep(C.scr_reveal - 0.06, C.scr_reveal + 0.06, cov)


def stage_a(t, camy):
    """paper + photo on the native grid -> area-resampled to the output frame."""
    C = CTX
    top = C.PAD - camy                       # first visible padded-canvas row
    r0 = int(math.floor(top))
    frac = top - r0
    nrows = C.H + (2 if frac > 1e-6 else 0)
    view = C.paper[r0:r0 + nrows].copy()
    rm = reveal_mask(t)
    if rm is not None:
        ph = render_photo(t)
        a = (C.photo_alpha * rm)[..., None] if not isinstance(rm, float) else C.photo_alpha[..., None]
        ya = C.py0 + C.oy + C.PAD - r0       # photo rows inside the view
        yb = ya + ph.shape[0]
        sa, sb = max(0, -ya), ph.shape[0] - max(0, yb - nrows)
        if sb > sa:
            roi = view[ya + sa:ya + sb]
            roi *= 1 - a[sa:sb]
            roi += ph[sa:sb] * a[sa:sb]
    Wo, Ho = C.out
    if frac <= 1e-6:
        return cv2.resize(view, (Wo, Ho), interpolation=cv2.INTER_AREA)
    ho2 = int(round(nrows * C.SY))
    small = cv2.resize(view, (Wo, ho2), interpolation=cv2.INTER_AREA)
    M = np.array([[1, 0, 0], [0, 1, -frac * C.SY]], np.float32)
    return cv2.warpAffine(small, M, (Wo, Ho), flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)


# =============================================================== text animation helpers
def stamp(t, th, pre=0.09, big=1.22, settle=0.17):
    """scale/alpha of a letterpress stamp landing exactly on time th."""
    if t < th - pre:
        return None
    if t < th:
        u = (t - (th - pre)) / pre
        return big - (big - 1) * ease_in_quad(u), min(1.0, u * 2.2)
    v = (t - th) / settle
    if v >= 1:
        return 1.0, 1.0
    return 1 - 0.035 * math.sin(math.pi * v) * (1 - v), 1.0


def rise(t, t0, dur=0.26, dist=55, s=1.25):
    if t < t0:
        return None
    u = (t - t0) / dur
    return dist * (1 - ease_out_back(u, s)) if u < 1 else 0.0


def pop(t, t0, dur=0.32, s=2.2):
    if t < t0:
        return None
    u = (t - t0) / dur
    if u >= 1:
        return 1.0, 0.0
    return ease_out_back(u, s), 1 - ease_out_cubic(u)


def hero_star_state(t):
    """position/scale/rotation/colour-mix of the opening star (native coords)."""
    cxc, cyc = W0 / 2, H0 / 2 - CAM0
    pulse = 1 + 0.10 * env_kick(t, 0.11, [0.0, B]) + 0.05 * env_kick(t, 0.09, [0.75 * B])
    if t < T_FLY0:
        return cxc, cyc, S0 * pulse, STAR_ROT_SPEED * t, 0.0
    if t < T_FLY1:
        u = (t - T_FLY0) / (T_FLY1 - T_FLY0)
        e = ease_in_out_cubic(u)
        hx, hy = STAR_HOME
        x = cxc + (hx - cxc) * e
        y = cyc + (hy - cyc) * e - 120 * math.sin(math.pi * e)
        r0 = STAR_ROT_SPEED * T_FLY0
        r1 = math.ceil((r0 + math.pi) / (math.pi / 2)) * (math.pi / 2)
        return x, y, S0 * pulse + (1 - S0 * pulse) * e, r0 + (r1 - r0) * e, e
    return None


def hero_star_close(t):
    if t < T_STAR_BACK:
        return None
    u = (t - T_STAR_BACK) / (DURATION - T_STAR_BACK)
    return W0 / 2, H0 / 2, S0 * ease_out_cubic(u), -STAR_ROT_SPEED * (DURATION - t)


def to_out(x, y, oyB):
    return x * CTX.SX, (y + oyB) * CTX.SY


def dark_layer(img, t, iris_c_out, iris_r, closing, centre_out):
    """deep bordeaux backdrop printed with a red halftone glow; paper iris with dotted edge.
    Everything in output pixels."""
    C = CTX
    k = C.SX
    dist = np.sqrt((C.ogx - iris_c_out[0]) ** 2 + (C.ogy - iris_c_out[1]) ** 2)
    cov = np.clip((dist - iris_r * k) / (120.0 * k) + 0.5, 0, 1)
    D = smoothstep(C.scr_iris - 0.05, C.scr_iris + 0.05, cov)
    if D.max() <= 0.001:
        return
    rr = np.sqrt((C.ogx - centre_out[0]) ** 2 + (C.ogy - centre_out[1]) ** 2) / k
    pulse = env_kick(t, 0.14, [0.0, B])
    glow_amt = 0.42 + 0.25 * pulse
    if closing:
        glow_amt = 0.42 * smoothstep(T_CLOSE0, DURATION, t)
    glow = glow_amt * np.exp(-(rr / 330) ** 2)
    dots = smoothstep(C.scr_dark - 0.07, C.scr_dark + 0.07, glow)
    bg = DARK_BG + (RED * 0.85 - DARK_BG) * dots[..., None]
    if not closing:
        u = t / 0.5
        if 0 <= u <= 1:
            R = 190 + 520 * ease_out_cubic(u)
            ring = np.exp(-((rr - R) / 26) ** 2) * (1 - u) * 0.9
            rd = smoothstep(C.scr_dark - 0.08, C.scr_dark + 0.08, ring)
            bg = bg + (PAPER - bg) * rd[..., None]
    # printed texture lives only in the dark backdrop (12 fps)
    bg = bg * (1 + 0.035 * C.dgrain[int(math.floor(t * 12)) % 4][..., None])
    img *= 1 - D[..., None]
    img += bg * D[..., None]


TR = -np.log(np.clip(RED / PAPER, 1e-3, None))
TP = -np.log(np.clip(PLUM / PAPER, 1e-3, None))
MIX = np.stack([TR, TP], 1).astype(np.float32)
PINV = np.linalg.pinv(MIX).astype(np.float32)


def misregister(img, jx, jy):
    """Decompose into red + plum ink densities (log domain), shift the red plate, recompose."""
    P = np.clip(CTX.paper_ref_out, 1e-3, None)
    T = -np.log(np.clip(img, 1e-3, None) / P)
    ab = T @ PINV.T
    resid = T - ab @ MIX.T
    M = np.array([[1, 0, jx], [0, 1, jy]], np.float32)
    a2 = cv2.warpAffine(np.ascontiguousarray(ab[..., 0]), M, (T.shape[1], T.shape[0]),
                        flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    T2 = a2[..., None] * TR + ab[..., 1:2] * TP + resid
    return P * np.exp(-T2)


# =============================================================== frame
def render_frame(fi):
    C = CTX
    t = fi / FPS
    camy = cam_y(t)
    C.cache_ok = camy == 0.0
    img = stage_a(t, camy)                     # output-res float image
    oyB = C.oy + camy                          # native y -> output y = (y + oyB) * SY
    S = C.spr

    # ---- OTIUM letterpress stamps (resting letters share one coverage batch -> seamless ligature)
    logo_batch = CovBatch(img.shape, S["logo_O"].color)
    moving = []
    for name, th in LOGO_HITS:
        st = stamp(t, th)
        if st:
            if st == (1.0, 1.0):
                vdraw(img, S[name], oyB, batch=logo_batch)
            else:
                moving.append((name, st))
    logo_batch.flush(img)
    for name, st in moving:
        spr = S[name]
        vdraw(img, spr, oyB, scale=st[0], alpha=st[1], anchor=(spr.cx, spr.y + spr.h * 0.62))
    if t >= T_FLY1:
        v = min(1.0, (t - T_FLY1) / 0.2)
        sc = 1 + 0.07 * math.sin(math.pi * v) * (1 - v)
        vdraw(img, S["logo_star"], oyB, scale=sc, anchor=STAR_HOME)

    # ---- AT VIVIDO, line, star, FIRENZE
    for i in range(META["n_atv"]):
        spr = S[f"atv_{i}"]
        off = rise(t, T_ATV + i * ATV_STAG)
        if off is not None:
            clip = None if off == 0.0 else (spr.x - 6, spr.y - 60, spr.x + spr.w + 6, spr.y + spr.h)
            vdraw(img, spr, oyB, dy=off, clip=clip)
    if t >= T_LINE0:
        spr = S["line"]
        e = ease_out_cubic((t - T_LINE0) / (T_LINE1 - T_LINE0))
        vdraw(img, spr, oyB, clip=None if e >= 1 else (spr.x - 1, spr.y - 2, spr.x + spr.w * e, spr.y + spr.h + 2))
    p = pop(t, T_SSTAR)
    if p:
        vdraw(img, S["star_small"], oyB, scale=p[0], rot=-math.pi * p[1])
    for i in range(META["n_fir"]):
        spr = S[f"fir_{i}"]
        off = rise(t, T_FIR + i * FIR_STAG, dur=0.22, dist=38)
        if off is not None:
            clip = None if off == 0.0 else (spr.x - 6, spr.y - 50, spr.x + spr.w + 6, spr.y + spr.h)
            vdraw(img, spr, oyB, dy=off, clip=clip)

    # ---- DOMENICA slides down into its slot, 15/11 stamps
    if t >= T_DOM:
        spr = S["domenica"]
        u = (t - T_DOM) / 0.34
        off = -(spr.h + 6) * (1 - ease_out_back(u, 1.1)) if u < 1 else 0.0
        clip = None if off == 0.0 else (spr.x - 4, spr.y, spr.x + spr.w + 4, spr.y + spr.h + 2)
        vdraw(img, spr, oyB, dy=off, clip=clip)
    st = stamp(t, T_DATE, pre=0.1, big=1.38, settle=0.2)
    if st:
        spr = S["date"]
        vdraw(img, spr, oyB, scale=st[0], alpha=st[1], anchor=(spr.cx, spr.y + spr.h * 0.7))

    # ---- big star
    p = pop(t, T_BSTAR, dur=0.38, s=2.4)
    if p:
        rot = -1.25 * math.pi * p[1]
        if T_SPIN <= t < T_SPIN + 0.4:
            rot += (math.pi / 2) * ease_in_out_cubic((t - T_SPIN) / 0.4)
        vdraw(img, S["star_big"], oyB, scale=p[0], rot=rot)

    # ---- 18.00 - 24.00 slot-machine roll (motion blur = average of sub-frame layers)
    if t >= T_ROLL0:
        last_stop = T_STOP0 + (len(C.reels) - 1) * (B / 16) + 0.17
        if t < last_stop:
            ys0 = int(math.floor((1114 + oyB) * C.SY))
            ys1 = int(math.ceil((1202 + oyB) * C.SY))
            NS = 6
            acc = np.zeros((ys1 - ys0, img.shape[1], 4), np.float32)
            pitch = 88.0
            for q in range(NS):
                tq = t - (q / NS) * (0.5 / FPS)
                strip = np.zeros_like(acc)
                for kk, (name, seq) in enumerate(C.reels):
                    final = S[name]
                    start = T_ROLL0 + kk * 0.018
                    stop = T_STOP0 + kk * (B / 16)
                    if tq < start:
                        continue
                    if tq < stop:
                        n = len(seq) * (1 - ease_out_cubic((tq - start) / (stop - start)))
                    else:
                        v = min(1.0, (tq - stop) / 0.16)
                        n = -0.09 * math.sin(math.pi * v) * (1 - v)
                    fade = min(1.0, (tq - start) / 0.06)
                    clip = (final.x - 3, 1119, final.x + final.w + 3, 1198)
                    base_bottom = final.y + final.h
                    for gi in range(len(seq) + 1):
                        yoff = (n - gi) * pitch
                        if abs(yoff) > pitch * 1.05:
                            continue
                        if gi == 0:
                            vdraw(strip, final, oyB, dy=yoff, alpha=fade, clip=clip, origin=(0.0, ys0))
                        else:
                            g = S[seq[-gi]]
                            vdraw(strip, g, oyB, dx=final.cx - g.cx, dy=base_bottom - (g.y + g.h) + yoff,
                                  alpha=fade, clip=clip, origin=(0.0, ys0))
                acc += strip
            acc /= NS
            roi = img[ys0:ys1]
            roi *= 1 - acc[..., 3:4]
            roi += acc[..., :3]
        p = pop(t, T_SEPS, dur=0.25, s=2.5)
        time_batch = CovBatch(img.shape, S["t_1"].color)
        if t >= last_stop:
            for name, _ in C.reels:
                vdraw(img, S[name], oyB, batch=time_batch)
        if p:
            for name in META["seps"]:
                if p[0] == 1.0:
                    vdraw(img, S[name], oyB, batch=time_batch)
                else:
                    vdraw(img, S[name], oyB, scale=p[0])
        time_batch.flush(img)

    # ---- genres
    for name, tg in GENRES:
        spr = S[name]
        if name.startswith("g_b"):
            p = pop(t, tg, dur=0.22, s=3.0)
            if p:
                vdraw(img, spr, oyB, scale=p[0])
        else:
            off = rise(t, tg, dur=0.22, dist=32)
            if off is not None:
                clip = None if off == 0.0 else (spr.x - 4, spr.y - 40, spr.x + spr.w + 4, spr.y + spr.h)
                vdraw(img, spr, oyB, dy=off, clip=clip)

    # ---- CTA: typed in red, then the red box fills left->right and knocks the text out
    if t >= T_TYPE0:
        box, txt = S["cta_box"], S["cta_text_red"]
        steps = 18
        u = min(1.0, (t - T_TYPE0) / (T_TYPE1 - T_TYPE0))
        xtype = box.x + 8 + (box.w - 14) * (math.floor(u * steps) / steps if u < 1 else 1.0)
        fill_x = box.x
        if t >= T_FILL0:
            fill_x = box.x + box.w * ease_in_out_cubic((t - T_FILL0) / (T_FILL1 - T_FILL0))
        if fill_x < box.x + box.w:
            vdraw(img, txt, oyB, clip=(fill_x, box.y - 2, xtype, box.y + box.h + 2))
        if fill_x >= box.x + box.w:
            vdraw(img, box, oyB)
        elif fill_x > box.x:
            vdraw(img, box, oyB, clip=(box.x - 2, box.y - 2, fill_x, box.y + box.h + 2))

    # ---- opening: dark backdrop + paper iris + hero star; closing mirrors it for the loop
    centre_out = (C.out[0] / 2, (H0 / 2 + C.oy) * C.SY)
    if t < T_IRIS1 + 0.05:
        hs = hero_star_state(t)
        cx_, cy_ = (hs[0], hs[1]) if hs else STAR_HOME
        r_iris = -200.0 if t < T_IRIS0 else -60 + 2000 * ease_in_cubic((t - T_IRIS0) / (T_IRIS1 - T_IRIS0))
        dark_layer(img, t, to_out(cx_, cy_, oyB), r_iris, False, centre_out)
    if t > T_CLOSE0:
        u = (t - T_CLOSE0) / (T_CLOSE1 - T_CLOSE0)
        r_iris = 1900 * (1 - ease_in_out_cubic(u)) if u < 1 else -400
        dark_layer(img, t, centre_out, r_iris, True, centre_out)

    hs = hero_star_state(t)
    if hs:
        x, y, sc, rot, e = hs
        col = GLINT + (RED - GLINT) * smoothstep(0.15, 0.85, e)
        samples = None
        if T_FLY0 <= t < T_FLY1:
            samples = []
            for q in range(5):
                s_ = hero_star_state(t - q * (0.5 / FPS) / 4)
                if s_:
                    xo, yo = to_out(s_[0], s_[1], oyB)
                    samples.append((xo, yo, s_[2] * C.SX, s_[3]))
        xo, yo = to_out(x, y, oyB)
        draw_star(img, xo, yo, sc * C.SX, rot, col, blur_samples=samples)
    hc = hero_star_close(t)
    if hc:
        xo, yo = to_out(hc[0], hc[1], oyB)
        draw_star(img, xo, yo, hc[2] * C.SX, hc[3], GLINT)

    # ---- strobe flash on the CTA drop (light only - nothing moves)
    if T_FLASH <= t < T_FLASH + 0.6:
        f = 0.75 * math.exp(-(t - T_FLASH) / 0.08)
        img += (GLINT - img) * f

    # ---- beat jitter ONLY while OTIUM is stamped in: risograph misregistration + small shake
    if t < T_LOGO_DONE:
        jx = jy = 0.0
        for (tj, sj), (ux, uy) in zip(JOLTS, JOLT_DIRS):
            if 0 <= t - tj < 0.4:
                e = sj * 3.0 * C.SX * math.exp(-(t - tj) / 0.07)
                jx += ux * e
                jy += uy * e
        if abs(jx) + abs(jy) > 0.15:
            img = misregister(img, jx, jy)
        sx = sy = 0.0
        for (ts, amp), (p1, p2) in zip(SHAKES, SHAKE_PH):
            if 0 <= t - ts < 0.35:
                e = amp * C.SX * math.exp(-(t - ts) / 0.08)
                sx += e * math.sin(2 * math.pi * 19 * (t - ts) + p1)
                sy += e * math.cos(2 * math.pi * 23 * (t - ts) + p2)
        if abs(sx) + abs(sy) > 0.05:
            M = np.array([[1, 0, -sx], [0, 1, -sy]], np.float32)
            img = cv2.warpAffine(img, M, C.out, flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    return (np.clip(img, 0, 1) * 255 + 0.5).astype(np.uint8)


# =============================================================== driver
def _init(fmt):
    cv2.setNumThreads(1)
    init_ctx(fmt)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fmt", default="4x5", choices=list(FORMATS))
    ap.add_argument("--preview", default="")
    ap.add_argument("--outdir", default="")
    ap.add_argument("--workers", type=int, default=4)
    args = ap.parse_args()
    os.makedirs(OUT, exist_ok=True)
    if args.preview:
        init_ctx(args.fmt)
        outdir = args.outdir or OUT
        os.makedirs(outdir, exist_ok=True)
        for ts in args.preview.split(","):
            t0 = time.time()
            fr = render_frame(int(round(float(ts) * FPS)))
            cv2.imwrite(os.path.join(outdir, f"prev_{args.fmt}_{float(ts):05.2f}.png"), fr[:, :, ::-1])
            print("t=%s  %.2fs" % (ts, time.time() - t0))
        return
    n = int(round(DURATION * FPS))
    w, h = FORMATS[args.fmt]["out"]
    # quality first: both deliverables are encoded straight from the raw frames (no second
    # generation): x264 CRF 10, preset slower, tune grain (keeps the halftone photo intact)
    audio = os.path.join(OUT, "otium_audio.wav")
    path = os.path.join(OUT, f"OTIUM_{args.fmt}_60fps.mp4")
    path30 = os.path.join(OUT, f"OTIUM_{args.fmt}_30fps.mp4")
    venc = ["-c:v", "libx264", "-preset", "slower", "-crf", "10", "-tune", "grain", "-pix_fmt", "yuv420p",
            "-profile:v", "high", "-c:a", "aac", "-b:a", "320k", "-shortest", "-movflags", "+faststart"]
    cmd = ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{w}x{h}",
           "-r", str(FPS), "-i", "-", "-i", audio,
           "-map", "0:v", "-map", "1:a", *venc, path,
           "-map", "0:v", "-map", "1:a", "-vf", "fps=30", *venc, path30]
    enc = subprocess.Popen(cmd, stdin=subprocess.PIPE)
    t0 = time.time()
    ctx = get_context("spawn")      # fork + OpenCV's thread pool can deadlock
    with ctx.Pool(args.workers, initializer=_init, initargs=(args.fmt,)) as pool:
        for i, fr in enumerate(pool.imap(render_frame, range(n), chunksize=2)):
            enc.stdin.write(fr.tobytes())
            if i % 60 == 0:
                print(f"frame {i}/{n}  {time.time() - t0:.1f}s", flush=True)
    enc.stdin.close()
    enc.wait()
    print("done", path, "%.1fs" % (time.time() - t0))


if __name__ == "__main__":
    main()
