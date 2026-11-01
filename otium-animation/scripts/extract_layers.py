"""Step 1 - decompose the flat flyer into separate, animatable layers.

Outputs (layers/):
  text/*.png        every text element / letter as an RGBA sprite at native position
  photo/*.png       photo window, ball-less plate, balls, palms, crowd, depth map
  data.npz          float data used by the renderer (paper field, masks, depth, LUT...)
  manifest.json     sprite positions
"""
import json
import os
import numpy as np
import cv2
import pickle
from common import (LAYERS, W0, H0, PAPER, RED, PLUM, load_rgb, save_rgba,
                    star_polygon, fill_poly_aa, trace_alpha, polys_to_svg_path)

os.makedirs(os.path.join(LAYERS, "text"), exist_ok=True)
os.makedirs(os.path.join(LAYERS, "photo"), exist_ok=True)

src = load_rgb()
H, W = src.shape[:2]
assert (W, H) == (W0, H0)
yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)


def ink_alpha(ink):
    d = PAPER - ink
    v = (PAPER[None, None] - src) @ d / float(d @ d)
    return np.clip(v, 0, 1).astype(np.float32)


A_RED = ink_alpha(RED)
A_PLUM = ink_alpha(PLUM)

# ------------------------------------------------------------------ paper field
diff = np.linalg.norm(src - PAPER, axis=2)
paper_px = (diff < 0.06).astype(np.float32)
paper_px[338:1112] = 0  # never learn paper colour inside the photo band
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


def make_sprite(name, alpha_src, ink, region_mask, pad=3, kind="text", exclude=None):
    """Cut an RGBA sprite out of the flyer from a binary region mask."""
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
    # un-premultiply against the local paper -> keeps the printed ink texture
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


# --- OTIUM -----------------------------------------------------------------
lc = comps(A_RED, (60, 20, 1062, 300))
OT, star_O, I_, UM = lc[0], lc[1], lc[2], lc[3]
# O counter -> O centre; split O|T with a point reflection of the O's left contour
inv = (~OT[20:300, 60:420]).astype(np.uint8)
n, lab, st, cen = cv2.connectedComponentsWithStats(inv, connectivity=4)
cand = [i for i in range(1, n) if st[i, 0] > 0 and st[i, 1] > 0
        and st[i, 0] + st[i, 2] < 360 and st[i, 1] + st[i, 3] < 280]
best = max(cand, key=lambda i: st[i, 4])
ocx, ocy = cen[best][0] + 60, cen[best][1] + 20
left_edge = {}
for y in range(20, 300):
    row = np.where(OT[y, :300])[0]
    if len(row):
        left_edge[y] = row.min()
O_mask = np.zeros((H, W), bool)
for y in range(20, 300):
    yr = int(round(2 * ocy - y))
    if yr not in left_edge:
        continue
    xr = int(2 * ocx - left_edge[yr]) + 3          # point-reflected estimate (merged rows)
    # where the paper gap between O and T exists, use the real right contour of the O
    row = OT[y, int(ocx):int(ocx) + 190]
    xs_ = np.arange(int(ocx), int(ocx) + 190)
    red = np.where(row)[0]
    if len(red) and (~row[:red[0]]).any():          # counter -> O stroke -> gap -> T
        after = row[red[0]:]
        gap = np.where(~after)[0]
        if len(gap) and gap[0] < 120 and after[gap[0]:].any():
            xr = int(xs_[red[0] + gap[0]])
    O_mask[y, :xr] = True
O_only = OT & O_mask
T_only = OT & ~O_mask
prof = UM[40:280, 740:800].sum(0)
cut = 740 + int(np.argmin(prof))
U_only = UM.copy(); U_only[:, cut:] = False
M_only = UM.copy(); M_only[:, :cut] = False
print("O centre", ocx, ocy, "U|M cut", cut)
for name, m, ex in [("logo_O", O_only, T_only), ("logo_star", star_O, None),
                    ("logo_T", T_only, O_only), ("logo_I", I_, None),
                    ("logo_U", U_only, M_only), ("logo_M", M_only, U_only)]:
    make_sprite(name, A_RED, RED, m, exclude=ex)

# --- AT VIVIDO / line / star / FIRENZE ----------------------------------------
atv = comps(A_PLUM, (50, 296, 562, 368))
for i, m in enumerate(atv):
    make_sprite(f"atv_{i}", A_PLUM, PLUM, m)
line_m = np.zeros((H, W), bool); line_m[328:340, 568:790] = True
make_sprite("line", A_PLUM, PLUM, line_m & (A_PLUM > 0.2))
make_sprite("star_small", A_RED, RED, comps(A_RED, (782, 288, 880, 385))[0])
fir = comps(A_PLUM, (878, 310, 1072, 360))
for i, m in enumerate(fir):
    make_sprite(f"fir_{i}", A_PLUM, PLUM, m)

# --- bottom block --------------------------------------------------------------
box = np.zeros((H, W), bool); box[1115:1178, 58:390] = True
make_sprite("domenica", A_PLUM, PLUM, box & (A_PLUM > 0.3))
box = np.zeros((H, W), bool); box[1176:1335, 30:412] = True
make_sprite("date", A_RED, RED, box & (A_RED > 0.3))
make_sprite("star_big", A_RED, RED, comps(A_RED, (415, 1145, 555, 1295))[0])

tc = comps(A_RED, (570, 1115, 1068, 1202))   # 1, 8, ., 00, -, 24, ., 0, 0


def col_split(mask, xa, xb):
    cut = xa + int(np.argmin(mask[1120:1200, xa:xb].sum(0)))
    l_, r_ = mask.copy(), mask.copy()
    l_[:, cut:] = False; r_[:, :cut] = False
    return l_, r_


t0a, t0b = col_split(tc[3], 720, 740)
t2, t4 = col_split(tc[5], 890, 912)
slot_masks = {"t_1": tc[0], "t_8": tc[1], "t_0a": t0a, "t_0b": t0b,
              "t_2": t2, "t_4": t4, "t_0c": tc[7], "t_0d": tc[8]}
sep_masks = {"t_dot1": tc[2], "t_dash": tc[4], "t_dot2": tc[6]}
sib = {"t_0a": t0b, "t_0b": t0a, "t_2": t4, "t_4": t2}
for name, m in {**slot_masks, **sep_masks}.items():
    make_sprite(name, A_RED, RED, m, pad=1, exclude=sib.get(name))
slots, seps = slot_masks, sep_masks

gm = np.zeros((H, W), bool); gm[1203:1238, 572:1082] = True
gm &= A_RED > 0.3
for name, (xa, xb) in {"g_hit": (572, 777), "g_b1": (777, 792), "g_reg": (792, 930),
                       "g_b2": (930, 946), "g_baile": (946, 1082)}.items():
    m = gm.copy(); m[:, :xa] = False; m[:, xb:] = False
    make_sprite(name, A_RED, RED, m, pad=1)

# CTA: red box with knocked-out text (+ a red-text version for the pre-fill state)
bx0, by0, bx1, by1 = 580, 1247, 1072, 1299
box_soft = np.clip(np.minimum.reduce([xx - bx0 + 1.0, bx1 - xx, yy - by0 + 1.0, by1 - yy]), 0, 1)
sl = (slice(by0 - 2, by1 + 2), slice(bx0 - 2, bx1 + 2))
cta_a = box_soft[sl].astype(np.float32)
box_red = np.clip((A_RED[sl] - 0.05) / 0.9, 0, 1) * cta_a          # red box, letters knocked out
save_rgba(os.path.join(LAYERS, "text", "cta_box.png"), src[sl], box_red)
cta_ink = np.median(src[sl][box_red > 0.95], axis=0)
manifest["cta_box"] = {"x": bx0 - 2, "y": by0 - 2, "w": bx1 - bx0 + 4, "h": by1 - by0 + 4,
                       "ink": [float(v) for v in cta_ink]}
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
non_paper[:338] = False
non_paper[1114:] = False
non_paper &= cv2.dilate((text_union > 0.05).astype(np.uint8), np.ones((7, 7), np.uint8)) == 0
m = cv2.morphologyEx(non_paper.astype(np.uint8), cv2.MORPH_CLOSE,
                     cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (17, 17)))
n, lab, st, _ = cv2.connectedComponentsWithStats(m, connectivity=8)
keep = np.isin(lab, [i for i in range(1, n) if st[i, 4] > 400]).astype(np.uint8)
ff = keep.copy()
cv2.floodFill(ff, np.zeros((H + 2, W + 2), np.uint8), (W // 2, 5), 1)
photo_mask = keep.astype(bool) | (ff == 0)
photo_mask[:330] = False
photo_mask[1118:] = False
photo_alpha = cv2.GaussianBlur(photo_mask.astype(np.float32), (0, 0), 0.8)
save_rgba(os.path.join(LAYERS, "photo", "photo_window.png"), src, photo_alpha)

# ------------------------------------------------------------------ disco balls
BALL = dict(cx=546.0, cy=665.0, r=123.0)
BALL2 = dict(cx=544.0, cy=806.0, r=57.0)
ball_m = ((xx - BALL["cx"]) ** 2 + (yy - BALL["cy"]) ** 2) <= (BALL["r"] + 2) ** 2
ball2_m = (((xx - BALL2["cx"]) ** 2 + (yy - BALL2["cy"]) ** 2) <= (BALL2["r"] + 2) ** 2) & ~ball_m
for nm, mk, b in [("disco_ball", ball_m, BALL), ("disco_ball_small", ball2_m, BALL2)]:
    x0, x1 = int(b["cx"] - b["r"] - 8), int(b["cx"] + b["r"] + 9)
    y0, y1 = int(b["cy"] - b["r"] - 8), int(b["cy"] + b["r"] + 9)
    a = cv2.GaussianBlur(mk.astype(np.float32), (0, 0), 1.0)[y0:y1, x0:x1]
    save_rgba(os.path.join(LAYERS, "photo", nm + ".png"), src[y0:y1, x0:x1], a)

src8 = np.clip(src * 255 + 0.5, 0, 255).astype(np.uint8)
inp_mask = (ball_m | ball2_m).astype(np.uint8) * 255   # live balls are drawn r+3, covering it
plate8 = cv2.inpaint(src8, inp_mask, 9, cv2.INPAINT_TELEA)
plate = plate8.astype(np.float32) / 255
cv2.imwrite(os.path.join(LAYERS, "photo", "plate_no_ball.png"), plate8[:, :, ::-1])

lum = src.mean(2)


def env_map(b):
    """Low-pass of the original reflections around a ball (normalised crop)."""
    r = b["r"]
    x0, y0 = int(round(b["cx"] - r * 1.3)), int(round(b["cy"] - r * 1.3))
    sz = int(round(r * 2.6))
    crop = lum[y0:y0 + sz, x0:x0 + sz].copy()
    return cv2.GaussianBlur(crop, (0, 0), max(2.0, r / 20)), x0, y0, sz


env1, e1x, e1y, e1s = env_map(BALL)
env2, e2x, e2y, e2s = env_map(BALL2)

# luminance -> duotone colour LUT learned from the photo itself
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
depth = np.full((H, W), 0.12, np.float32)
depth = np.maximum(depth, np.clip((yy - 905) / 190.0, 0, 1) * 0.85 + (yy > 905) * 0.15)
depth = np.maximum(depth, np.clip((np.abs(xx - 561) - 380) / 180.0, 0, 1) * 0.45)
depth = np.maximum(depth, ((yy > 380) & (yy < 570) & (xx > 280) & (xx < 820)) * 0.28)
pill = (((xx > 88) & (xx < 162)) | ((xx > 935) & (xx < 1005))) & (yy < 950)
depth = np.maximum(depth, pill * 0.42)
palm_pts_L = np.array([(0, 712), (112, 730), (158, 830), (96, 905), (0, 905)], np.int32)
palm_pts_R = np.array([(928, 772), (1122, 752), (1122, 936), (936, 936), (920, 880)], np.int32)
palmL = np.zeros((H, W), np.float32); cv2.fillPoly(palmL, [palm_pts_L], 1.0)
palmR = np.zeros((H, W), np.float32); cv2.fillPoly(palmR, [palm_pts_R], 1.0)
depth = np.maximum(depth, np.maximum(palmL, palmR) * 0.62).astype(np.float32)
depth = cv2.GaussianBlur(depth, (0, 0), 22)
cv2.imwrite(os.path.join(LAYERS, "photo", "depth_map.png"),
            (np.clip(depth, 0, 1) * 255 * photo_alpha).astype(np.uint8))

# palm sway weights: fronds move, trunks stay planted
dL = np.hypot(xx - 40, yy - 905) / 190.0
dR = np.hypot(xx - 1030, yy - 940) / 190.0
sway_L = (cv2.GaussianBlur(palmL, (0, 0), 10) * np.clip(dL, 0, 1) ** 1.3).astype(np.float32)
sway_R = (cv2.GaussianBlur(palmR, (0, 0), 10) * np.clip(dR, 0, 1) ** 1.3).astype(np.float32)
for nm, pm_ in [("palm_left", palmL), ("palm_right", palmR)]:
    a = cv2.GaussianBlur(pm_, (0, 0), 2) * photo_alpha
    ys, xs = np.where(a > 0.01)
    x0, x1, y0, y1 = xs.min(), xs.max() + 1, ys.min(), ys.max() + 1
    save_rgba(os.path.join(LAYERS, "photo", nm + ".png"), src[y0:y1, x0:x1], a[y0:y1, x0:x1])

crowd_w = (np.clip((yy - 930) / 45.0, 0, 1) * photo_alpha).astype(np.float32)
y0 = int(np.where(crowd_w.max(1) > 0.01)[0].min())
save_rgba(os.path.join(LAYERS, "photo", "crowd.png"), src[y0:], crowd_w[y0:])

LIGHTS = [(318, 548), (382, 545), (435, 548), (494, 552), (547, 535), (602, 552), (656, 548),
          (709, 546), (766, 548)]

cv2.imwrite(os.path.join(LAYERS, "00_paper_plate.png"),
            np.clip(paper_low[:, :, ::-1] * 255, 0, 255).astype(np.uint8))

# ------------------------------------------------------------------ vector star fit (logo star)
ys, xs = np.where(star_O)
scx, scy = float(xs.mean()), float(ys.mean())
ix, iy = int(scx), int(scy)
target = star_O[iy - 90:iy + 90, ix - 90:ix + 90]
best = (0, None)
for rl in np.arange(64, 78, 1.5):
    for rs in np.arange(34, 72, 2.5):
        for ri in np.arange(7, 19, 1.5):
            for rot in np.deg2rad(np.arange(-6, 7, 2)):
                pts = star_polygon(90 + scx - ix, 90 + scy - iy, rl, rs, ri, rot)
                m = fill_poly_aa(180, 180, pts, ss=1) > 0.5
                iou = (m & target).sum() / max((m | target).sum(), 1)
                if iou > best[0]:
                    best = (iou, (float(rl), float(rs), float(ri), float(rot)))
print("star fit IoU %.3f" % best[0], best[1])
STAR = dict(cx=scx, cy=scy, r_long=best[1][0], r_short=best[1][1], r_in=best[1][2], rot=best[1][3])

manifest["_meta"] = dict(BALL=BALL, BALL2=BALL2, LIGHTS=LIGHTS, STAR=STAR, slots=list(slots),
                         seps=list(seps), n_atv=len(atv), n_fir=len(fir),
                         O_centre=[float(ocx), float(ocy)], env1=[e1x, e1y, e1s],
                         env2=[e2x, e2y, e2s], paper_hf_std=paper_hf_std)
with open(os.path.join(LAYERS, "manifest.json"), "w") as f:
    json.dump(manifest, f, indent=1)
with open(os.path.join(LAYERS, "vectors.pkl"), "wb") as f:
    pickle.dump(VEC, f)
# vector export: one SVG per element + the whole typography layer
os.makedirs(os.path.join(LAYERS, "vector"), exist_ok=True)


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
