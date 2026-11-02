"""Step 1 - decompose the flat flyer into separate, animatable layers.

    OTIUM_VARIANT=feed python3 extract_layers.py   # 4:5 flyer  -> layers/
    OTIUM_VARIANT=reel python3 extract_layers.py   # 9:16 flyer -> layers_reel/

Outputs (in the variant's layers dir):
  text/*.png        every text element / letter as an RGBA sprite at native position
  vector/*.svg      the same elements as traced vector outlines (+ _all_typography.svg)
  photo/*.png       photo window, ball-less plate, balls, palms, crowd, depth map
  data.npz          float data used by the renderer (paper field, masks, depth, LUT...)
  vectors.pkl       traced outlines used by the renderer
  manifest.json     sprite positions + layout metadata
"""
import json
import os
import pickle
import numpy as np
import cv2
from common import (LAYERS, LAYOUT, W0, H0, PAPER, RED, PLUM, load_rgb, save_rgba,
                    star_polygon, fill_poly_aa, trace_alpha, polys_to_svg_path)

L = LAYOUT
BX = L["boxes"]
os.makedirs(os.path.join(LAYERS, "text"), exist_ok=True)
os.makedirs(os.path.join(LAYERS, "photo"), exist_ok=True)
os.makedirs(os.path.join(LAYERS, "vector"), exist_ok=True)

src = load_rgb()
H, W = src.shape[:2]
assert (W, H) == (W0, H0), (W, H)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
PR0, PR1 = L["photo_rows"]


def ink_alpha(ink):
    d = PAPER - ink
    v = (PAPER[None, None] - src) @ d / float(d @ d)
    return np.clip(v, 0, 1).astype(np.float32)


A_RED = ink_alpha(RED)
A_PLUM = ink_alpha(PLUM)

# ------------------------------------------------------------------ paper field
diff = np.linalg.norm(src - PAPER, axis=2)
paper_px = (diff < 0.06).astype(np.float32)
paper_px[PR0:PR1 - 2] = 0  # never learn paper colour inside the photo band
num = cv2.GaussianBlur(src * paper_px[..., None], (0, 0), 30)
den = cv2.GaussianBlur(paper_px, (0, 0), 30)[..., None]
num2 = cv2.GaussianBlur(src * paper_px[..., None], (0, 0), 120)
den2 = cv2.GaussianBlur(paper_px, (0, 0), 120)[..., None]
wide = num2 / np.maximum(den2, 1e-6)
paper_low = np.where(den > 0.05, num / np.maximum(den, 1e-6), wide).astype(np.float32)
paper_hf_std = float(np.std((src - paper_low)[paper_px > 0]))
print("paper texture std", paper_hf_std)

# ------------------------------------------------------------------ text sprites
manifest = {}
VEC = {}            # traced vector outlines of every text sprite (absolute flyer coords)
text_union = np.zeros((H, W), np.float32)


def comps(alpha, box, min_area=12):
    x0, y0, x1, y1 = box
    m = (alpha[y0:y1, x0:x1] > 0.45).astype(np.uint8)
    n, lab, st, _ = cv2.connectedComponentsWithStats(m, connectivity=8)
    out = []
    for i in range(1, n):
        if st[i, 4] >= min_area:
            full = np.zeros((H, W), bool)
            full[y0:y1, x0:x1] = (lab == i)
            out.append((int(st[i, 0] + x0), full))
    out.sort(key=lambda c: c[0])
    return [c[1] for c in out]


def bbox(m):
    ys, xs = np.where(m)
    return xs.min(), ys.min(), xs.max() + 1, ys.max() + 1


def make_sprite(name, alpha_src, ink, region_mask, pad=3, kind="text", exclude=None):
    """Cut an RGBA sprite out of the flyer from a binary region mask (+ trace its outline)."""
    reg = cv2.dilate(region_mask.astype(np.uint8), np.ones((5, 5), np.uint8)).astype(bool)
    if exclude is not None:          # split letters: never bleed into the sibling piece
        reg &= ~exclude
    a = np.clip((alpha_src - 0.05) / 0.9, 0, 1) * reg
    ys, xs = np.where(a > 0.004)
    x0, x1 = max(xs.min() - pad, 0), min(xs.max() + pad + 1, W)
    y0, y1 = max(ys.min() - pad, 0), min(ys.max() + pad + 1, H)
    a_c = a[y0:y1, x0:x1]
    s_c = src[y0:y1, x0:x1]
    p_c = paper_low[y0:y1, x0:x1]
    rgb = p_c + (s_c - p_c) / np.maximum(a_c[..., None], 1e-3)
    solid = a_c > 0.6
    ink_med = np.median(s_c[solid], axis=0) if solid.sum() > 20 else ink
    rgb = np.where(solid[..., None], rgb, ink_med)
    rgb = np.clip(rgb, 0, 1)
    save_rgba(os.path.join(LAYERS, kind, name + ".png"), rgb, a_c)
    manifest[name] = {"x": int(x0), "y": int(y0), "w": int(x1 - x0), "h": int(y1 - y0),
                      "ink": [float(v) for v in ink_med]}
    VEC[name] = [p + np.array([x0, y0], np.float32) for p in trace_alpha(a_c)]
    text_union[y0:y1, x0:x1] = np.maximum(text_union[y0:y1, x0:x1], a_c)


def col_split(mask, frac_lo=0.35, frac_hi=0.65):
    """split a merged pair of glyphs at the lightest column of its middle third."""
    x0, y0, x1, y1 = bbox(mask)
    a, b = x0 + int((x1 - x0) * frac_lo), x0 + int((x1 - x0) * frac_hi)
    cut = a + int(np.argmin(mask[y0:y1, a:b].sum(0)))
    l_, r_ = mask.copy(), mask.copy()
    l_[:, cut:] = False
    r_[:, :cut] = False
    return l_, r_


# --- OTIUM -----------------------------------------------------------------
lb = BX["logo"]
lc = comps(A_RED, lb)
OT, star_O, I_, UM = lc[0], lc[1], lc[2], lc[3]
ox0, oy0, ox1, oy1 = bbox(OT)
sub = (~OT[lb[1]:lb[3], lb[0]:lb[0] + (ox1 - lb[0]) // 2 + 60]).astype(np.uint8)
n, lab, st, cen = cv2.connectedComponentsWithStats(sub, connectivity=4)
cand = [i for i in range(1, n) if st[i, 0] > 0 and st[i, 1] > 0
        and st[i, 0] + st[i, 2] < sub.shape[1] and st[i, 1] + st[i, 3] < sub.shape[0]]
best = max(cand, key=lambda i: st[i, 4])
ocx, ocy = cen[best][0] + lb[0], cen[best][1] + lb[1]
left_edge = {}
for y in range(lb[1], lb[3]):
    row = np.where(OT[y, :int(ocx)])[0]
    if len(row):
        left_edge[y] = row.min()
span = int((ocx - min(left_edge.values())) * 1.35)
O_mask = np.zeros((H, W), bool)
for y in range(lb[1], lb[3]):
    yr = int(round(2 * ocy - y))
    if yr not in left_edge:
        continue
    xr = int(2 * ocx - left_edge[yr]) + 3          # point-reflected estimate (merged rows)
    row = OT[y, int(ocx):int(ocx) + span]
    xs_ = np.arange(int(ocx), int(ocx) + span)
    red = np.where(row)[0]
    if len(red) and (~row[:red[0]]).any():          # counter -> O stroke -> gap -> T
        after = row[red[0]:]
        gap = np.where(~after)[0]
        if len(gap) and gap[0] < span * 0.65 and after[gap[0]:].any():
            xr = int(xs_[red[0] + gap[0]])
    O_mask[y, :xr] = True
O_only = OT & O_mask
T_only = OT & ~O_mask
# U|M: cut along the natural paper gap between U's right stroke and M's left stem
# (row by row); where the two letters merge (top band, bottom serif) the cut continues
# the gap line, so each piece keeps its true outline and no straight "chop" shows.
ca, cb = L["um_cut"]
ux0, uy0, ux1, uy1 = bbox(UM)
path = np.full(H, np.nan, np.float32)
for y in range(uy0, uy1):
    paper_ = A_RED[y, ca:cb] < 0.5
    if not paper_.any():
        continue
    best_len, best_c, run_s = 0, None, None
    for i, v in enumerate(np.append(paper_, False)):
        if v and run_s is None:
            run_s = i
        elif not v and run_s is not None:
            if i - run_s > best_len:
                best_len, best_c = i - run_s, ca + (run_s + i - 1) / 2.0
            run_s = None
    if best_len >= 2:
        path[y] = best_c
rows = np.arange(uy0, uy1)
vals = path[uy0:uy1]
ok = ~np.isnan(vals)
vals = np.interp(rows, rows[ok], vals[ok]).astype(np.float32)
vals = np.convolve(np.pad(vals, 3, mode="edge"), np.ones(7) / 7, "valid")
path[:] = np.median(vals)
path[uy0:uy1] = vals
U_only = UM & (xx < path[:, None])
M_only = UM & (xx >= path[:, None])


def give_islands(a, b, frac=0.05):
    """move small pieces of `a` that are detached from its main body over to `b`
    (avoids stray crumbs showing while a letter is on screen alone)."""
    n_, lab_, st_, _ = cv2.connectedComponentsWithStats(a.astype(np.uint8), connectivity=8)
    if n_ <= 2:
        return a, b
    main = 1 + int(np.argmax(st_[1:, 4]))
    small = (lab_ > 0) & (lab_ != main)
    small &= np.isin(lab_, [i for i in range(1, n_) if st_[i, 4] < frac * st_[main, 4]])
    return a & ~small, b | small


U_only, M_only = give_islands(U_only, M_only)
M_only, U_only = give_islands(M_only, U_only)
print("O centre", ocx, ocy, "U|M gap path x %.1f..%.1f" % (vals.min(), vals.max()))
for name, m, ex in [("logo_O", O_only, T_only), ("logo_star", star_O, None),
                    ("logo_T", T_only, O_only), ("logo_I", I_, None),
                    ("logo_U", U_only, M_only), ("logo_M", M_only, U_only)]:
    make_sprite(name, A_RED, RED, m, exclude=ex)

# --- AT VIVIDO / line / star / FIRENZE ----------------------------------------
atv = comps(A_PLUM, BX["atv"])
for i, m in enumerate(atv):
    make_sprite(f"atv_{i}", A_PLUM, PLUM, m)
x0, y0, x1, y1 = BX["line"]
line_m = np.zeros((H, W), bool); line_m[y0:y1, x0:x1] = True
make_sprite("line", A_PLUM, PLUM, line_m & (A_PLUM > 0.2))
make_sprite("star_small", A_RED, RED, max(comps(A_RED, BX["sstar"]), key=lambda m: m.sum()))
fir = comps(A_PLUM, BX["fir"])
for i, m in enumerate(fir):
    make_sprite(f"fir_{i}", A_PLUM, PLUM, m)

# --- bottom block --------------------------------------------------------------
x0, y0, x1, y1 = BX["dom"]
box = np.zeros((H, W), bool); box[y0:y1, x0:x1] = True
make_sprite("domenica", A_PLUM, PLUM, box & (A_PLUM > 0.3))
x0, y0, x1, y1 = BX["date"]
box = np.zeros((H, W), bool); box[y0:y1, x0:x1] = True
make_sprite("date", A_RED, RED, box & (A_RED > 0.3))
make_sprite("star_big", A_RED, RED, max(comps(A_RED, BX["bstar"]), key=lambda m: m.sum()))

# time "18.00 - 24.00": digits (split merged pairs) and separators
tc = comps(A_RED, BX["time"])
hmax = max(bbox(m)[3] - bbox(m)[1] for m in tc)
digits, seps = [], []
for m in tc:
    x0, y0, x1, y1 = bbox(m)
    if (y1 - y0) < 0.5 * hmax:
        seps.append(m)
    elif (x1 - x0) > 1.05 * (y1 - y0):
        l_, r_ = col_split(m)
        digits += [(l_, r_), (r_, l_)]
    else:
        digits.append((m, None))
slots = []
for i, (m, sib) in enumerate(digits):
    make_sprite(f"t_d{i}", A_RED, RED, m, pad=1, exclude=sib)
    slots.append(f"t_d{i}")
sep_names = []
for i, m in enumerate(seps):
    make_sprite(f"t_s{i}", A_RED, RED, m, pad=1)
    sep_names.append(f"t_s{i}")
print("time:", len(slots), "digits,", len(sep_names), "separators")

# genres: words split at the bullets
gx0, gy0, gx1, gy1 = BX["genres"]
gm = np.zeros((H, W), bool); gm[gy0:gy1, gx0:gx1] = True
gm &= A_RED > 0.3
gcomps = comps(A_RED, BX["genres"])
bullets = []
for m in gcomps:
    x0, y0, x1, y1 = bbox(m)
    if (x1 - x0) <= 11 and (y1 - y0) <= 11:
        bullets.append((x0, x1))
bullets.sort()
edges = [gx0] + [v for b in bullets for v in b] + [gx1]
genre_names = []
for i in range(len(bullets) + 1):
    xa, xb = edges[2 * i], edges[2 * i + 1]
    m = gm.copy(); m[:, :xa] = False; m[:, xb:] = False
    make_sprite(f"g_w{i}", A_RED, RED, m, pad=1)
    genre_names.append(f"g_w{i}")
    if i < len(bullets):
        bx_a, bx_b = bullets[i]
        m = gm.copy(); m[:, :bx_a - 1] = False; m[:, bx_b + 1:] = False
        make_sprite(f"g_b{i + 1}", A_RED, RED, m, pad=1)
        genre_names.append(f"g_b{i + 1}")
print("genres:", genre_names)

# CTA: red box with knocked-out text (+ a red-text version for the pre-fill state)
cta_c = comps(A_RED, BX["cta"])
bx0, by0, bx1, by1 = bbox(max(cta_c, key=lambda m: m.sum()))
box_soft = np.clip(np.minimum.reduce([xx - bx0 + 1.0, bx1 - xx, yy - by0 + 1.0, by1 - yy]), 0, 1)
sl = (slice(by0 - 2, by1 + 2), slice(bx0 - 2, bx1 + 2))
cta_a = box_soft[sl].astype(np.float32)
box_red = np.clip((A_RED[sl] - 0.05) / 0.9, 0, 1) * cta_a
save_rgba(os.path.join(LAYERS, "text", "cta_box.png"), src[sl], box_red)
cta_ink = np.median(src[sl][box_red > 0.95], axis=0)
manifest["cta_box"] = {"x": int(bx0 - 2), "y": int(by0 - 2), "w": int(bx1 - bx0 + 4),
                       "h": int(by1 - by0 + 4), "ink": [float(v) for v in cta_ink]}
VEC["cta_box"] = [p + np.array([bx0 - 2, by0 - 2], np.float32) for p in trace_alpha(box_red)]
txt_a = np.clip((1 - A_RED[sl] - 0.08) / 0.84, 0, 1) * cta_a
txt_a[:6] = 0; txt_a[-6:] = 0; txt_a[:, :7] = 0; txt_a[:, -7:] = 0
save_rgba(os.path.join(LAYERS, "text", "cta_text_red.png"),
          np.broadcast_to(RED, txt_a.shape + (3,)).copy(), txt_a)
manifest["cta_text_red"] = dict(manifest["cta_box"])
VEC["cta_text_red"] = [p + np.array([bx0 - 2, by0 - 2], np.float32) for p in trace_alpha(txt_a)]
text_union[sl] = np.maximum(text_union[sl], cta_a)

# ------------------------------------------------------------------ photo window
non_paper = diff > 0.10
non_paper[:PR0] = False
non_paper[PR1:] = False
non_paper &= cv2.dilate((text_union > 0.05).astype(np.uint8), np.ones((7, 7), np.uint8)) == 0
m = cv2.morphologyEx(non_paper.astype(np.uint8), cv2.MORPH_CLOSE,
                     cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17, 17)))
n, lab, st, _ = cv2.connectedComponentsWithStats(m, connectivity=8)
keep = np.isin(lab, [i for i in range(1, n) if st[i, 4] > 400]).astype(np.uint8)
ff = keep.copy()
cv2.floodFill(ff, np.zeros((H + 2, W + 2), np.uint8), (W // 2, 5), 1)
photo_mask = keep.astype(bool) | (ff == 0)
photo_mask[:PR0 - 8] = False
photo_mask[PR1 + 4:] = False
photo_alpha = cv2.GaussianBlur(photo_mask.astype(np.float32), (0, 0), 0.8)
save_rgba(os.path.join(LAYERS, "photo", "photo_window.png"), src, photo_alpha)

# ------------------------------------------------------------------ disco balls (elliptical ok)
BALL, BALL2 = dict(L["ball"]), dict(L["ball2"])


def ell(b, grow):
    return (((xx - b["cx"]) / (b["rx"] + grow)) ** 2 + ((yy - b["cy"]) / (b["ry"] + grow)) ** 2) <= 1


ball_m = ell(BALL, 2)
ball2_m = ell(BALL2, 2) & ~ball_m
for nm, mk, b in [("disco_ball", ball_m, BALL), ("disco_ball_small", ball2_m, BALL2)]:
    x0, x1 = int(b["cx"] - b["rx"] - 8), int(b["cx"] + b["rx"] + 9)
    y0, y1 = int(b["cy"] - b["ry"] - 8), int(b["cy"] + b["ry"] + 9)
    a = cv2.GaussianBlur(mk.astype(np.float32), (0, 0), 1.0)[y0:y1, x0:x1]
    save_rgba(os.path.join(LAYERS, "photo", nm + ".png"), src[y0:y1, x0:x1], a)

src8 = np.clip(src * 255 + 0.5, 0, 255).astype(np.uint8)
inp_mask = (ball_m | ball2_m).astype(np.uint8) * 255   # live balls are drawn r+3, covering it
plate8 = cv2.inpaint(src8, inp_mask, 9, cv2.INPAINT_TELEA)
plate = plate8.astype(np.float32) / 255
cv2.imwrite(os.path.join(LAYERS, "photo", "plate_no_ball.png"), plate8[:, :, ::-1])

lum = src.mean(2)


def env_map(b):
    """Low-pass of the original reflections around a ball, resampled to a square map in
    ball-normalised coordinates (centre at es/2, radius es/2.6)."""
    rx, ry = b["rx"], b["ry"]
    es = int(round(rx * 2.6))
    x0, y0 = b["cx"] - rx * 1.3, b["cy"] - ry * 1.3
    mxs = (x0 + (np.arange(es) + 0.5) * (2.6 * rx / es)).astype(np.float32)
    mys = (y0 + (np.arange(es) + 0.5) * (2.6 * ry / es)).astype(np.float32)
    MX, MY = np.meshgrid(mxs, mys)
    crop = cv2.remap(lum.astype(np.float32), MX, MY, cv2.INTER_LINEAR, borderMode=cv2.BORDER_REFLECT)
    return cv2.GaussianBlur(crop, (0, 0), max(2.0, rx / 20))


env1 = env_map(BALL)
env2 = env_map(BALL2)

pm = photo_mask & ~ball_m
Lp = (lum[pm] * 255).astype(np.int32).clip(0, 255)
cols = src[pm]
cnt = np.bincount(Lp, minlength=256).astype(np.float32)
lut = np.stack([np.bincount(Lp, weights=cols[:, c], minlength=256) for c in range(3)], 1)
valid = cnt > 30
lut[valid] /= cnt[valid, None]
idx = np.arange(256)
lut = np.stack([np.interp(idx, idx[valid], lut[valid, c]) for c in range(3)], 1)
k = np.ones(9) / 9
lut = np.stack([np.convolve(np.pad(lut[:, c], 4, mode="edge"), k, "valid") for c in range(3)],
               1).astype(np.float32)

# ------------------------------------------------------------------ depth map (0 far .. 1 near)
DP = L["depth"]
c0, c1 = DP["crowd"]
depth = np.full((H, W), 0.12, np.float32)
depth = np.maximum(depth, np.clip((yy - c0) / float(c1 - c0), 0, 1) * 0.85 + (yy > c0) * 0.15)
depth = np.maximum(depth, np.clip((np.abs(xx - DP["side_c"]) - DP["side"][0]) / DP["side"][1], 0, 1) * 0.45)
tx0, ty0, tx1, ty1 = DP["truss"]
depth = np.maximum(depth, ((yy > ty0) & (yy < ty1) & (xx > tx0) & (xx < tx1)) * 0.28)
pill = np.zeros((H, W), bool)
for (pa_, pb_) in DP["pillars"]:
    pill |= (xx > pa_) & (xx < pb_)
pill &= yy < DP["pill_ymax"]
depth = np.maximum(depth, pill * 0.42)
palmL = np.zeros((H, W), np.float32); cv2.fillPoly(palmL, [np.array(L["palmL"], np.int32)], 1.0)
palmR = np.zeros((H, W), np.float32); cv2.fillPoly(palmR, [np.array(L["palmR"], np.int32)], 1.0)
depth = np.maximum(depth, np.maximum(palmL, palmR) * 0.62).astype(np.float32)
depth = cv2.GaussianBlur(depth, (0, 0), 22)
cv2.imwrite(os.path.join(LAYERS, "photo", "depth_map.png"),
            (np.clip(depth, 0, 1) * 255 * photo_alpha).astype(np.uint8))

dL = np.hypot(xx - L["trunkL"][0], yy - L["trunkL"][1]) / L["sway_r"]
dR = np.hypot(xx - L["trunkR"][0], yy - L["trunkR"][1]) / L["sway_r"]
sway_L = (cv2.GaussianBlur(palmL, (0, 0), 10) * np.clip(dL, 0, 1) ** 1.3).astype(np.float32)
sway_R = (cv2.GaussianBlur(palmR, (0, 0), 10) * np.clip(dR, 0, 1) ** 1.3).astype(np.float32)
for nm, pm_ in [("palm_left", palmL), ("palm_right", palmR)]:
    a = cv2.GaussianBlur(pm_, (0, 0), 2) * photo_alpha
    ys, xs = np.where(a > 0.01)
    x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    save_rgba(os.path.join(LAYERS, "photo", nm + ".png"), src[y0:y1, x0:x1], a[y0:y1, x0:x1])

crowd_w = (np.clip((yy - L["crowd_y"]) / 45.0, 0, 1) * photo_alpha).astype(np.float32)
y0 = int(np.where(crowd_w.max(1) > 0.01)[0].min())
save_rgba(os.path.join(LAYERS, "photo", "crowd.png"), src[y0:], crowd_w[y0:])

cv2.imwrite(os.path.join(LAYERS, "00_paper_plate.png"),
            np.clip(paper_low[:, :, ::-1] * 255, 0, 255).astype(np.uint8))

# ------------------------------------------------------------------ vector star fit (logo star)
ys, xs = np.where(star_O)
scx, scy = float(xs.mean()), float(ys.mean())
ix, iy = int(scx), int(scy)
target = star_O[iy - 90:iy + 90, ix - 90:ix + 90]
best = (0, None)
for rl in np.arange(56, 78, 2.0):
    for rs in np.arange(34, 72, 3.0):
        for ri in np.arange(7, 19, 2.0):
            pts = star_polygon(90 + scx - ix, 90 + scy - iy, rl, rs, ri, 0.0)
            m = fill_poly_aa(180, 180, pts, ss=1) > 0.5
            iou = (m & target).sum() / max((m | target).sum(), 1)
            if iou > best[0]:
                best = (iou, (float(rl), float(rs), float(ri), 0.0))
STAR = dict(cx=scx, cy=scy, r_long=best[1][0], r_short=best[1][1], r_in=best[1][2], rot=best[1][3])

manifest["_meta"] = dict(BALL=BALL, BALL2=BALL2, LIGHTS=[list(p) for p in L["lights"]], STAR=STAR,
                         slots=slots, seps=sep_names, genres=genre_names, n_atv=len(atv), n_fir=len(fir),
                         O_centre=[float(ocx), float(ocy)], paper_hf_std=paper_hf_std)
with open(os.path.join(LAYERS, "manifest.json"), "w") as f:
    json.dump(manifest, f, indent=1)
with open(os.path.join(LAYERS, "vectors.pkl"), "wb") as f:
    pickle.dump(VEC, f)


def hexcol(c):
    return "#%02x%02x%02x" % tuple(int(round(v * 255)) for v in c)


paths = []
for name, polys in VEC.items():
    m_ = manifest[name]
    col = hexcol(RED if name == "cta_text_red" else m_["ink"])
    d = polys_to_svg_path(polys, m_["x"], m_["y"])
    with open(os.path.join(LAYERS, "vector", name + ".svg"), "w") as f:
        f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">'
                '<path fill="%s" fill-rule="evenodd" d="%s"/></svg>\n' % (m_["w"], m_["h"], m_["w"], m_["h"], col, d))
    if name != "cta_text_red":
        paths.append('<path id="%s" fill="%s" fill-rule="evenodd" d="%s"/>' % (name, col, polys_to_svg_path(polys)))
with open(os.path.join(LAYERS, "vector", "_all_typography.svg"), "w") as f:
    f.write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 %d %d" width="%d" height="%d">'
            '<rect width="100%%" height="100%%" fill="%s"/>%s</svg>\n' % (W, H, W, H, hexcol(PAPER), "".join(paths)))
np.savez_compressed(os.path.join(LAYERS, "data.npz"), paper_low=paper_low, photo_alpha=photo_alpha,
                    plate=plate, depth=depth, sway_L=sway_L, sway_R=sway_R, crowd_w=crowd_w,
                    env1=env1, env2=env2, lut=lut, src=src)
print("ok: %d sprites" % (len(manifest) - 1))
