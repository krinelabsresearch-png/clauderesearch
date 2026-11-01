"""Shared constants and helpers for the OTIUM animation pipeline."""
import os
import numpy as np
import cv2

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "source", "flyer.png")
LAYERS = os.path.join(ROOT, "layers")
OUT = os.path.join(ROOT, "out")

W0, H0 = 1122, 1402          # source flyer size (all layout coords live here)
FPS = 60
DURATION = 12.0
BPM = 100.0
BEAT = 60.0 / BPM            # 0.6 s -> 5 bars = 12 s exactly
BAR = 4 * BEAT

# measured inks (sRGB 0..1)
PAPER = np.array([246, 200, 197], np.float32) / 255
RED = np.array([183, 12, 27], np.float32) / 255
PLUM = np.array([81, 21, 55], np.float32) / 255
DARK_BG = np.array([58, 12, 34], np.float32) / 255     # opening backdrop (deep bordeaux)
GLINT = np.array([255, 236, 230], np.float32) / 255    # brightest "light" tone, stays in palette


def load_rgb(path=SRC):
    return cv2.imread(path, cv2.IMREAD_COLOR)[:, :, ::-1].astype(np.float32) / 255


def save_rgba(path, rgb, a):
    img = np.dstack([rgb, a[..., None]])
    img = np.clip(img * 255 + 0.5, 0, 255).astype(np.uint8)
    cv2.imwrite(path, cv2.cvtColor(img, cv2.COLOR_RGBA2BGRA))


def load_rgba(path):
    img = cv2.imread(path, cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(img, cv2.COLOR_BGRA2RGBA).astype(np.float32) / 255
    return img[..., :3].copy(), img[..., 3].copy()


def smoothstep(e0, e1, x):
    t = np.clip((x - e0) / (e1 - e0), 0.0, 1.0)
    return t * t * (3 - 2 * t)


def clamp01(x):
    return np.clip(x, 0.0, 1.0)


# ---------------------------------------------------------------- easing (scalar)
def _c(t):
    return float(min(1.0, max(0.0, t)))


def ease_out_cubic(t):
    t = _c(t)
    return 1 - (1 - t) ** 3


def ease_in_cubic(t):
    return _c(t) ** 3


def ease_in_quad(t):
    return _c(t) ** 2


def ease_in_out_cubic(t):
    t = _c(t)
    return 4 * t ** 3 if t < 0.5 else 1 - (-2 * t + 2) ** 3 / 2


def ease_out_back(t, s=1.70158):
    t = _c(t)
    return 1 + (s + 1) * (t - 1) ** 3 + s * (t - 1) ** 2


def ease_in_out_sine(t):
    t = _c(t)
    return -(np.cos(np.pi * t) - 1) / 2


def ease_out_expo(t):
    t = _c(t)
    return 1.0 if t >= 1 else 1 - 2 ** (-10 * t)


def beat_t(b):
    """time (s) of beat index b (fractional allowed, 0.25 = one 16th)."""
    return b * BEAT


def halftone_screen(h, w, cell=8.0, angle_deg=45.0, ox=0.0, oy=0.0):
    """AM dot screen. s in [0,1]: 0 at dot centre, 1 at cell corner.
    A pixel is inked when coverage > s, so dots grow from their centres."""
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    a = np.deg2rad(angle_deg)
    u = (xx + ox) * np.cos(a) + (yy + oy) * np.sin(a)
    v = -(xx + ox) * np.sin(a) + (yy + oy) * np.cos(a)
    fu = (u / cell) % 1.0 - 0.5
    fv = (v / cell) % 1.0 - 0.5
    d = np.sqrt(fu * fu + fv * fv) / 0.7071
    return np.clip(d, 0, 1) ** 2


def star_polygon(cx, cy, r_long, r_short, r_in, rot=0.0):
    """8-point star like the OTIUM logo: 4 long cardinal arms, 4 short diagonals."""
    pts = []
    for k in range(16):
        ang = rot + k * np.pi / 8 - np.pi / 2
        if k % 2 == 1:
            r = r_in
        elif k % 4 == 0:
            r = r_long
        else:
            r = r_short
        pts.append((cx + r * np.cos(ang), cy + r * np.sin(ang)))
    return np.array(pts, np.float32)


def fill_poly_aa(h, w, pts, ss=4):
    """Anti-aliased polygon coverage via supersampling."""
    m = np.zeros((h * ss, w * ss), np.uint8)
    p = np.round(pts * ss).astype(np.int32)
    cv2.fillPoly(m, [p], 255, lineType=cv2.LINE_8)
    m = cv2.resize(m, (w, h), interpolation=cv2.INTER_AREA)
    return m.astype(np.float32) / 255


def trace_alpha(a, up=8, thr=0.5, min_area=0.4):
    """Sub-pixel vector outline of an anti-aliased alpha mask.
    Returns a list of closed polygons (N,2) in pixel-centre coords of `a`
    (outer contours and holes; fill them with the even-odd rule)."""
    h, w = a.shape
    pad = 2
    ap = np.pad(a.astype(np.float32), pad)
    big = cv2.resize(ap, ((w + 2 * pad) * up, (h + 2 * pad) * up), interpolation=cv2.INTER_CUBIC)
    m = (big > thr).astype(np.uint8)
    cnts, _ = cv2.findContours(m, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
    k = np.exp(-0.5 * (np.arange(-4, 5) / 1.4) ** 2)
    k /= k.sum()
    out = []
    for c in cnts:
        p = c[:, 0, :].astype(np.float32)
        if len(p) < 6:
            continue
        # light smoothing along the closed contour removes the 1/8 px staircase
        pw = np.concatenate([p[-4:], p, p[:4]])
        p = np.stack([np.convolve(pw[:, 0], k, "valid"), np.convolve(pw[:, 1], k, "valid")], 1)
        p = ((p + 0.5) / up - 0.5 - pad).astype(np.float32)
        if abs(cv2.contourArea(p)) < min_area:
            continue
        p = cv2.approxPolyDP(p.reshape(-1, 1, 2), 0.04, True)[:, 0, :]
        out.append(p.astype(np.float32))
    return out


def polys_to_svg_path(polys, ox=0.0, oy=0.0):
    d = []
    for p in polys:
        d.append("M" + " L".join("%.2f %.2f" % (x - ox, y - oy) for x, y in p) + " Z")
    return " ".join(d)
