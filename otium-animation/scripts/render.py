"""Step 2 - render the OTIUM 10 s loop frame by frame from the extracted layers.

    python3 render.py --fmt 4x5             # full render -> out/otium_4x5_video.mp4 (no audio)
    python3 render.py --fmt 9x16
    python3 render.py --fmt 4x5 --preview 0.3,1.3,3.0   # PNG stills for review
"""
import argparse
import json
import math
import os
import subprocess
import time
from multiprocessing import get_context

import numpy as np
import cv2

from common import (LAYERS, OUT, W0, H0, FPS, DURATION, BEAT, BAR, PAPER, RED, PLUM, GLINT,
                    DARK_BG, load_rgba, smoothstep, ease_out_cubic, ease_in_cubic, ease_in_quad,
                    ease_in_out_cubic, ease_out_back, ease_in_out_sine, halftone_screen,
                    fill_poly_aa)

MAN = json.load(open(os.path.join(LAYERS, "manifest.json")))
META = MAN["_meta"]
B = BEAT
FORMATS = {"4x5": dict(H=H0, out=(1080, 1350)), "9x16": dict(H=1995, out=(1080, 1920))}

# =============================================================== timeline (s) - 96 BPM grid
KICKS = [B * k for k in range(16)]
SNARES = sorted(B * (bar * 4 + s) for bar in range(4) for s in (0.75, 1.5, 2.75, 3.5))
LOGO_HITS = [("logo_O", B * 2), ("logo_T", B * 2.75), ("logo_I", B * 3), ("logo_U", B * 3.5),
             ("logo_M", B * 4)]
T_FLY0, T_FLY1 = B * 1.5, B * 2          # star flies into the O
T_IRIS0, T_IRIS1 = B * 1.45, B * 2.35    # paper floods in
T_REVEAL = B * 4                          # photo prints in (halftone)
T_ATV, ATV_STAG = B * 4.5, B / 8
T_LINE0, T_LINE1 = B * 5.5, B * 6
T_SSTAR = B * 6
T_FIR, FIR_STAG = B * 6.15, B / 14
T_BEAMS = B * 6
T_DOM = B * 8
T_DATE = B * 9
T_BSTAR = B * 9.5
T_ROLL0, T_STOP0 = B * 9.45, B * 10
T_SEPS = B * 10
GENRES = [("g_hit", B * 10.5), ("g_b1", B * 10.75), ("g_reg", B * 11), ("g_b2", B * 11.25),
          ("g_baile", B * 11.5)]
T_TYPE0, T_TYPE1 = B * 12, B * 12.4
T_FILL0, T_FILL1 = B * 12.5, B * 13
T_FLASH = B * 13
T_SPIN = B * 14
T_CLOSE0, T_CLOSE1 = 9.56, 9.93
T_STAR_BACK = 9.60

# camera: during bar 1 the logo sits centred in frame; on the bar-2 downbeat the camera
# tilts down to the full layout while the photo prints in
PAD = 560
CAM0 = 540.0
T_PAN0, T_PAN1 = B * 4, B * 4 + 1.15


def cam_y(t):
    if t < T_PAN0:
        return CAM0
    return CAM0 * (1 - ease_in_out_cubic((t - T_PAN0) / (T_PAN1 - T_PAN0)))


BEAM_COL = np.array([0.96, 0.74, 0.72], np.float32)   # warm haze, stays in the pink palette
STAR_ROT_SPEED = 0.75          # rad/s of the opening/closing hero star
S0 = 2.15                      # hero star scale vs. the logo star

# misregistration jolts (time, strength) and shakes (time, px)
JOLTS = [(t, 1.0) for _, t in LOGO_HITS] + [(T_SSTAR, 0.6), (T_DATE, 1.7), (T_BSTAR, 0.6),
                                            (T_SEPS, 0.5), (T_FLASH, 1.5), (T_SPIN, 0.5)]
JOLTS += [(k, 0.3) for k in KICKS if k >= B * 4.5 and all(abs(k - j[0]) > 0.05 for j in JOLTS)]
SHAKES = [(B * 2, 2.0), (B * 4, 2.2), (T_DATE, 6.5), (T_FLASH, 3.5), (T_SSTAR, 1.0)]

rng0 = np.random.RandomState(7)
JOLT_DIRS = [(math.cos(a), math.sin(a)) for a in rng0.uniform(0, 2 * np.pi, len(JOLTS))]
SHAKE_PH = rng0.uniform(0, 2 * np.pi, (len(SHAKES), 2))


def env_kick(t, decay=0.12, times=KICKS):
    """sum of exponential envelopes of past hits."""
    v = 0.0
    for k in times:
        if 0 <= t - k < 6 * decay:
            v += math.exp(-(t - k) / decay)
    return v


# =============================================================== sprites
class Sprite:
    def __init__(self, name):
        rgb, a = load_rgba(os.path.join(LAYERS, "text", name + ".png"))
        m = MAN[name]
        self.name = name
        self.x, self.y = m["x"], m["y"]
        self.h, self.w = a.shape
        self.pm = np.dstack([rgb * a[..., None], a]).astype(np.float32)

    @property
    def cx(self):
        return self.x + self.w / 2

    @property
    def cy(self):
        return self.y + self.h / 2


def blit(cv, spr, oy, dx=0.0, dy=0.0, scale=1.0, rot=0.0, alpha=1.0, anchor=None, clip=None):
    """Composite a premultiplied sprite with an affine transform. clip = native (x0,y0,x1,y1)."""
    if alpha <= 0.003 or scale <= 0.01:
        return
    Hc, Wc = cv.shape[:2]
    ax, ay = anchor if anchor is not None else (spr.cx, spr.cy)
    c, s = math.cos(rot) * scale, math.sin(rot) * scale
    bx = ax + c * (spr.x - ax) - s * (spr.y - ay) + dx
    by = ay + oy + s * (spr.x - ax) + c * (spr.y - ay) + dy
    corners = np.array([[0, 0], [spr.w, 0], [0, spr.h], [spr.w, spr.h]], np.float32)
    px = bx + c * corners[:, 0] - s * corners[:, 1]
    py = by + s * corners[:, 0] + c * corners[:, 1]
    x0, x1 = int(math.floor(px.min())) - 1, int(math.ceil(px.max())) + 1
    y0, y1 = int(math.floor(py.min())) - 1, int(math.ceil(py.max())) + 1
    if clip is not None:
        x0, x1 = max(x0, int(math.floor(clip[0]))), min(x1, int(math.ceil(clip[2])))
        y0, y1 = max(y0, int(math.floor(clip[1] + oy))), min(y1, int(math.ceil(clip[3] + oy)))
    x0, y0, x1, y1 = max(x0, 0), max(y0, 0), min(x1, Wc), min(y1, Hc)
    if x1 <= x0 or y1 <= y0:
        return
    fast = scale == 1.0 and rot == 0.0 and float(bx).is_integer() and float(by).is_integer()
    if fast:
        sx0, sy0 = x0 - int(bx), y0 - int(by)
        w = np.zeros((y1 - y0, x1 - x0, 4), np.float32)
        ya, xa = max(0, -sy0), max(0, -sx0)
        part = spr.pm[max(sy0, 0):sy0 + (y1 - y0), max(sx0, 0):sx0 + (x1 - x0)]
        w[ya:ya + part.shape[0], xa:xa + part.shape[1]] = part
    else:
        M = np.array([[c, -s, bx - x0], [s, c, by - y0]], np.float32)
        w = cv2.warpAffine(spr.pm, M, (x1 - x0, y1 - y0), flags=cv2.INTER_LINEAR,
                           borderMode=cv2.BORDER_CONSTANT, borderValue=(0, 0, 0, 0))
    if alpha < 1.0:
        w = w * alpha
    roi = cv[y0:y1, x0:x1]
    roi *= 1.0 - w[..., 3:4]
    roi += w if cv.shape[2] == 4 else w[..., :3]


# =============================================================== vector star (traced logo star)
def trace_star():
    rgb, a = load_rgba(os.path.join(LAYERS, "text", "logo_star.png"))
    up = cv2.resize(a, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
    up = cv2.GaussianBlur(up, (0, 0), 1.2)
    m = (up > 0.5).astype(np.uint8)
    cnts, _ = cv2.findContours(m, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt = max(cnts, key=cv2.contourArea)[:, 0, :].astype(np.float32) / 4.0
    mm = MAN["logo_star"]
    ys, xs = np.where(a > 0.5)
    cx, cy = xs.mean(), ys.mean()
    pts = cnt - np.array([cx, cy], np.float32)
    return pts, (mm["x"] + cx, mm["y"] + cy)


STAR_PTS, STAR_HOME = trace_star()


def draw_star(cv, oy, cx, cy, scale, rot, color, alpha=1.0, blur_samples=None):
    """Anti-aliased vector star; blur_samples = list of (cx,cy,scale,rot) for motion blur."""
    samples = blur_samples or [(cx, cy, scale, rot)]
    Hc, Wc = cv.shape[:2]
    rmax = max(s[2] for s in samples) * 80 + 4
    xs_ = [s[0] for s in samples]
    ys_ = [s[1] + oy for s in samples]
    x0, x1 = int(max(0, min(xs_) - rmax)), int(min(Wc, max(xs_) + rmax))
    y0, y1 = int(max(0, min(ys_) - rmax)), int(min(Hc, max(ys_) + rmax))
    if x1 <= x0 or y1 <= y0 or alpha <= 0.003:
        return
    cov = np.zeros((y1 - y0, x1 - x0), np.float32)
    for (sx, sy, sc, sr) in samples:
        c, s = math.cos(sr) * sc, math.sin(sr) * sc
        P = np.stack([STAR_PTS[:, 0] * c - STAR_PTS[:, 1] * s + sx - x0,
                      STAR_PTS[:, 0] * s + STAR_PTS[:, 1] * c + sy + oy - y0], 1)
        cov += fill_poly_aa(y1 - y0, x1 - x0, P, ss=3)
    cov = (cov / len(samples) * alpha)[..., None]
    roi = cv[y0:y1, x0:x1]
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
    oy, Hc = C.oy, C.H
    C.PAD = PAD
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
    C.paper_vis = C.paper[PAD:].copy()
    C.grain = [(0.65 * smooth_noise((Hc, W0), 0.6, 10 + i) + 0.35 * smooth_noise((Hc, W0), 1.8, 20 + i))
               .astype(np.float32) for i in range(4)]
    C.boil = [(smooth_noise((Hc, W0), 5, 30 + i) * 0.42, smooth_noise((Hc, W0), 5, 40 + i) * 0.42)
              for i in range(4)]
    C.gx, C.gy = np.meshgrid(np.arange(W0, dtype=np.float32), np.arange(Hp, dtype=np.float32))
    C.ogx, C.ogy = np.meshgrid(np.arange(W0, dtype=np.float32), np.arange(Hc, dtype=np.float32))
    pa = D["photo_alpha"]
    rows = np.where(pa.max(1) > 0.001)[0]
    C.py0, C.py1 = int(rows.min()), int(rows.max()) + 1
    sl = slice(C.py0, C.py1)
    C.photo_alpha = pa[sl]
    C.plate = D["plate"]
    C.depth = D["depth"][sl]
    C.sway_L = D["sway_L"][sl]
    C.sway_R = D["sway_R"][sl]
    C.crowd_w = D["crowd_w"][sl]
    C.lum = D["src"][sl].mean(2)
    C.env1, C.env2, C.lut = D["env1"], D["env2"], D["lut"]
    ph = C.py1 - C.py0
    C.pX, C.pY = np.meshgrid(np.arange(W0, dtype=np.float32),
                             np.arange(C.py0, C.py1, dtype=np.float32))
    C.scr_reveal = halftone_screen(ph, W0, cell=9.0, angle_deg=45, oy=C.py0)
    C.scr_beam = halftone_screen(ph, W0, cell=5.0, angle_deg=15, oy=C.py0)
    C.scr_dark = halftone_screen(Hp, W0, cell=12.0, angle_deg=45)
    C.scr_iris = halftone_screen(Hp, W0, cell=16.0, angle_deg=30)
    r = np.random.RandomState(5)
    ph_x = cv2.GaussianBlur(r.rand(1, W0).astype(np.float32), (0, 0), 18)[0]
    ph_x = (ph_x - ph_x.min()) / (ph_x.max() - ph_x.min() + 1e-6)
    C.crowd_phase = (ph_x * 0.11).astype(np.float32)
    am = cv2.GaussianBlur(r.rand(1, W0).astype(np.float32), (0, 0), 14)[0]
    C.crowd_amp = (0.55 + 0.9 * (am - am.min()) / (am.max() - am.min() + 1e-6)).astype(np.float32)
    C.spr = {k: Sprite(k) for k in MAN if not k.startswith("_")}
    C.bX, C.bY = np.meshgrid(np.arange(0, W0, 2, dtype=np.float32),
                             np.arange(C.py0, C.py1, 2, dtype=np.float32))
    r = np.random.RandomState(11)
    C.spots = []
    while len(C.spots) < 90:
        x, y = r.uniform(0, W0), r.uniform(C.py0 + 20, 930)
        if math.hypot(x - 546, y - 665) < 140 or C.lum[int(y) - C.py0, int(x)] > 0.75:
            continue
        C.spots.append((x, y, r.uniform(16, 34), r.uniform(1.3, 3.0), r.uniform(0.9, 2.2), r.uniform(0, 3)))
    C.sparkles = []
    for q in range(int(4.0 / (B / 4)), int(9.55 / (B / 4))):
        tq = B * q / 4
        on_kick = q % 4 == 0
        n = 2 if on_kick else (1 if r.rand() < 0.45 else 0)
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


# =============================================================== photo
def cam_k(t):
    return ease_in_out_sine((t - T_REVEAL) / (9.9 - T_REVEAL)) if t > T_REVEAL else 0.0


ZC = (546.0, 540.0)


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
    if t > T_REVEAL:
        tq = math.floor(t * 12) / 12
        bounce = np.zeros(W0, np.float32)
        for kt in KICKS:
            tau = tq - kt - C.crowd_phase
            m = (tau >= 0) & (tau < 0.5)
            tc = np.clip(tau, 0, 0.5)
            bounce += np.where(m, (tc / 0.07) * np.exp(1 - tc / 0.07), 0).astype(np.float32)
        my += C.crowd_w * (bounce * C.crowd_amp * 3.6)[None, :]
    img = cv2.remap(C.plate, mx.astype(np.float32), my.astype(np.float32), cv2.INTER_LINEAR,
                    borderMode=cv2.BORDER_REFLECT)
    py0 = C.py0

    # mirror-ball light spots sweeping the walls
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
        draw_star(img, -py0, x, y, size * e, rot + u * 0.9, GLINT, alpha=0.95)
    if T_FLASH <= t < T_FLASH + 0.45:
        u = (t - T_FLASH) / 0.45
        draw_star(img, -py0, bx - 0.35 * R, by - 0.38 * R, 0.55 * math.sin(math.pi * u) ** 0.6,
                  0.3 + u, GLINT)
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
        return x, y, S0 + (1 - S0) * e, r0 + (r1 - r0) * e, e
    return None


def hero_star_close(t):
    if t < T_STAR_BACK:
        return None
    u = (t - T_STAR_BACK) / (10.0 - T_STAR_BACK)
    return W0 / 2, H0 / 2, S0 * ease_out_cubic(u), -STAR_ROT_SPEED * (10.0 - t)


def dark_layer(cv, t, iris_c, iris_r, closing, camy):
    """deep bordeaux backdrop printed with a red halftone glow; paper iris with a dotted edge."""
    C = CTX
    oy = C.oy + C.PAD
    dist = np.sqrt((C.gx - iris_c[0]) ** 2 + (C.gy - (iris_c[1] + oy)) ** 2)
    cov = np.clip((dist - iris_r) / 120.0 + 0.5, 0, 1)
    D = smoothstep(C.scr_iris - 0.05, C.scr_iris + 0.05, cov)
    if D.max() <= 0.001:
        return
    rr = np.sqrt((C.gx - W0 / 2) ** 2 + (C.gy - (H0 / 2 - camy + oy)) ** 2)
    pulse = env_kick(t, 0.14, [0.0, B])
    glow_amt = 0.42 + 0.25 * pulse
    if closing:
        glow_amt = 0.42 * smoothstep(T_CLOSE0, 10.0, t)
    glow = glow_amt * np.exp(-(rr / 330) ** 2)
    dots = smoothstep(C.scr_dark - 0.07, C.scr_dark + 0.07, glow)
    bg = DARK_BG + (RED * 0.85 - DARK_BG) * dots[..., None]
    if not closing:
        for kt in (0.0, B):
            u = (t - kt) / 0.5
            if 0 <= u <= 1:
                R = 190 + 520 * ease_out_cubic(u)
                ring = np.exp(-((rr - R) / 26) ** 2) * (1 - u) * 0.9
                rd = smoothstep(C.scr_dark - 0.08, C.scr_dark + 0.08, ring)
                bg = bg + (PAPER - bg) * rd[..., None]
    cv *= 1 - D[..., None]
    cv += bg * D[..., None]


# =============================================================== frame
def render_frame(fi):
    C = CTX
    t = fi / FPS
    oy = C.oy + C.PAD
    camy = cam_y(t)
    cv = C.paper.copy()
    S = C.spr

    # ---- photo window (prints in through a halftone screen)
    rm = reveal_mask(t)
    if rm is not None:
        ph = render_photo(t)
        a = C.photo_alpha * rm
        roi = cv[C.py0 + oy:C.py1 + oy]
        roi *= 1 - a[..., None]
        roi += ph * a[..., None]

    # ---- OTIUM letterpress stamps
    for name, th in LOGO_HITS:
        st = stamp(t, th)
        if st:
            spr = S[name]
            blit(cv, spr, oy, scale=st[0], alpha=st[1], anchor=(spr.cx, spr.y + spr.h * 0.62))
    if t >= T_FLY1:
        v = min(1.0, (t - T_FLY1) / 0.2)
        sc = 1 + 0.07 * math.sin(math.pi * v) * (1 - v)
        blit(cv, S["logo_star"], oy, scale=sc, anchor=STAR_HOME)

    # ---- AT VIVIDO, line, star, FIRENZE
    for i in range(META["n_atv"]):
        spr = S[f"atv_{i}"]
        off = rise(t, T_ATV + i * ATV_STAG)
        if off is not None:
            blit(cv, spr, oy, dy=off, clip=(spr.x - 6, spr.y - 60, spr.x + spr.w + 6, spr.y + spr.h))
    if t >= T_LINE0:
        spr = S["line"]
        e = ease_out_cubic((t - T_LINE0) / (T_LINE1 - T_LINE0))
        blit(cv, spr, oy, clip=(spr.x, spr.y, spr.x + spr.w * e, spr.y + spr.h))
    p = pop(t, T_SSTAR)
    if p:
        blit(cv, S["star_small"], oy, scale=p[0], rot=-math.pi * p[1])
    for i in range(META["n_fir"]):
        spr = S[f"fir_{i}"]
        off = rise(t, T_FIR + i * FIR_STAG, dur=0.22, dist=38)
        if off is not None:
            blit(cv, spr, oy, dy=off, clip=(spr.x - 6, spr.y - 50, spr.x + spr.w + 6, spr.y + spr.h))

    # ---- DOMENICA slides down into its slot, 15/11 stamps
    if t >= T_DOM:
        spr = S["domenica"]
        u = (t - T_DOM) / 0.34
        off = -(spr.h + 6) * (1 - ease_out_back(u, 1.1)) if u < 1 else 0.0
        blit(cv, spr, oy, dy=off, clip=(spr.x - 4, spr.y, spr.x + spr.w + 4, spr.y + spr.h + 2))
    st = stamp(t, T_DATE, pre=0.1, big=1.38, settle=0.2)
    if st:
        spr = S["date"]
        blit(cv, spr, oy, scale=st[0], alpha=st[1], anchor=(spr.cx, spr.y + spr.h * 0.7))

    # ---- big star
    p = pop(t, T_BSTAR, dur=0.38, s=2.4)
    if p:
        rot = -1.25 * math.pi * p[1]
        if t >= T_SPIN:
            rot += (math.pi / 2) * ease_in_out_cubic((t - T_SPIN) / 0.4)
        blit(cv, S["star_big"], oy, scale=p[0], rot=rot)

    # ---- 18.00 - 24.00 slot-machine roll (motion blur = average of sub-frame layers)
    if t >= T_ROLL0:
        sy0, sy1 = 1114, 1202
        last_stop = T_STOP0 + (len(C.reels) - 1) * (B / 16) + 0.17
        NS = 6 if t < last_stop else 1
        acc = np.zeros((sy1 - sy0, W0, 4), np.float32)
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
                        blit(strip, final, -sy0, dy=yoff, alpha=fade, clip=clip)
                    else:
                        g = S[seq[-gi]]
                        blit(strip, g, -sy0, dx=final.cx - g.cx, dy=base_bottom - (g.y + g.h) + yoff,
                             alpha=fade, clip=clip)
            acc += strip
        acc /= NS
        roi = cv[sy0 + oy:sy1 + oy]
        roi *= 1 - acc[..., 3:4]
        roi += acc[..., :3]
        p = pop(t, T_SEPS, dur=0.25, s=2.5)
        if p:
            for name in META["seps"]:
                blit(cv, S[name], oy, scale=p[0])

    # ---- genres
    for name, tg in GENRES:
        spr = S[name]
        if name.startswith("g_b"):
            p = pop(t, tg, dur=0.22, s=3.0)
            if p:
                blit(cv, spr, oy, scale=p[0])
        else:
            off = rise(t, tg, dur=0.22, dist=32)
            if off is not None:
                blit(cv, spr, oy, dy=off, clip=(spr.x - 4, spr.y - 40, spr.x + spr.w + 4, spr.y + spr.h))

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
            blit(cv, txt, oy, clip=(fill_x, box.y, xtype, box.y + box.h))
        if fill_x > box.x:
            blit(cv, box, oy, clip=(box.x, box.y, fill_x, box.y + box.h))

    # ---- opening: dark backdrop + paper iris + hero star; closing mirrors it for the loop
    if t < T_IRIS1 + 0.05:
        hs = hero_star_state(t)
        cx_, cy_ = (hs[0], hs[1]) if hs else STAR_HOME
        r_iris = -200.0 if t < T_IRIS0 else -60 + 2000 * ease_in_cubic((t - T_IRIS0) / (T_IRIS1 - T_IRIS0))
        dark_layer(cv, t, (cx_, cy_), r_iris, closing=False, camy=camy)
    if t > T_CLOSE0:
        u = (t - T_CLOSE0) / (T_CLOSE1 - T_CLOSE0)
        r_iris = 1900 * (1 - ease_in_out_cubic(u)) if u < 1 else -400
        dark_layer(cv, t, (W0 / 2, H0 / 2 - camy), r_iris, closing=True, camy=camy)

    hs = hero_star_state(t)
    if hs:
        x, y, sc, rot, e = hs
        col = GLINT + (RED - GLINT) * smoothstep(0.15, 0.85, e)
        samples = None
        if T_FLY0 <= t < T_FLY1:
            samples = [s_[:4] for s_ in (hero_star_state(t - q * (0.5 / FPS) / 4) for q in range(5)) if s_]
        draw_star(cv, oy, x, y, sc, rot, col, blur_samples=samples)
    hc = hero_star_close(t)
    if hc:
        draw_star(cv, oy, hc[0], hc[1], hc[2], hc[3], GLINT)

    # ---- strobe flash on the CTA landing
    if T_FLASH <= t < T_FLASH + 0.6:
        f = 0.82 * math.exp(-(t - T_FLASH) / 0.075)
        cv += (GLINT - cv) * f

    # ---- camera + shake + boil in a single remap
    sx = sy = 0.0
    for (ts, amp), (p1, p2) in zip(SHAKES, SHAKE_PH):
        if 0 <= t - ts < 0.6:
            e = amp * math.exp(-(t - ts) / 0.11)
            sx += e * math.sin(2 * math.pi * 19 * (t - ts) + p1)
            sy += e * math.cos(2 * math.pi * 23 * (t - ts) + p2)
    bi = int(math.floor(t * 12)) % 4
    bdx, bdy = C.boil[bi]
    cv = cv2.remap(cv, C.ogx + bdx + sx, C.ogy + (C.PAD - camy) + bdy + sy, cv2.INTER_LINEAR,
                   borderMode=cv2.BORDER_REFLECT)

    # ---- risograph misregistration: shift the red ink plate
    jx = jy = 0.0
    for (tj, sj), (ux, uy) in zip(JOLTS, JOLT_DIRS):
        if 0 <= t - tj < 0.5:
            e = sj * 3.2 * math.exp(-(t - tj) / 0.085)
            jx += ux * e
            jy += uy * e
    if abs(jx) + abs(jy) > 0.15:
        cv = misregister(cv, jx, jy)

    # ---- animated grain at 12 fps
    cv *= 1 + 0.022 * C.grain[bi][..., None]
    out = cv2.resize(np.clip(cv, 0, 1), C.out, interpolation=cv2.INTER_AREA)
    return (out * 255 + 0.5).astype(np.uint8)


TR = -np.log(np.clip(RED / PAPER, 1e-3, None))
TP = -np.log(np.clip(PLUM / PAPER, 1e-3, None))
MIX = np.stack([TR, TP], 1).astype(np.float32)          # 3x2
PINV = np.linalg.pinv(MIX).astype(np.float32)          # 2x3


def misregister(cv, jx, jy):
    """Decompose into red + plum ink densities (log domain), shift the red plate, recompose."""
    T = -np.log(np.clip(cv, 1e-3, None) / np.clip(CTX.paper_vis, 1e-3, None))
    ab = T @ PINV.T
    resid = T - ab @ MIX.T
    M = np.array([[1, 0, jx], [0, 1, jy]], np.float32)
    a2 = cv2.warpAffine(np.ascontiguousarray(ab[..., 0]), M, (T.shape[1], T.shape[0]),
                        flags=cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    T2 = a2[..., None] * TR + ab[..., 1:2] * TP + resid
    return CTX.paper_vis * np.exp(-T2)


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
    # generation), x264 CRF 12 / preset slower / tune grain (keeps halftone + paper grain intact)
    audio = os.path.join(OUT, "otium_audio.wav")
    path = os.path.join(OUT, f"OTIUM_{args.fmt}_60fps.mp4")
    path30 = os.path.join(OUT, f"OTIUM_{args.fmt}_30fps.mp4")
    venc = ["-c:v", "libx264", "-preset", "slower", "-crf", "12", "-tune", "grain", "-pix_fmt", "yuv420p",
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
