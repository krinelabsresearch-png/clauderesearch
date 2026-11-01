"""Contact sheet of the extracted layers + reconstruction check (all layers at rest == flyer)."""
import glob
import json
import os
import numpy as np
import cv2
from common import LAYERS, load_rgba, load_rgb

man = json.load(open(os.path.join(LAYERS, "manifest.json")))
D = np.load(os.path.join(LAYERS, "data.npz"))
src = D["src"]

# ---- reconstruction: paper + photo window + every sprite at its native position
rec = D["paper_low"].copy()
pa = D["photo_alpha"][..., None]
rec = rec * (1 - pa) + src * pa
for name, m in man.items():
    if name.startswith("_") or name == "cta_text_red":
        continue
    rgb, a = load_rgba(os.path.join(LAYERS, "text", name + ".png"))
    y, x = m["y"], m["x"]
    h, w = a.shape
    reg = rec[y:y + h, x:x + w]
    rec[y:y + h, x:x + w] = reg * (1 - a[..., None]) + rgb * a[..., None]
mse = float(np.mean((rec - src) ** 2))
print("reconstruction PSNR %.1f dB" % (10 * np.log10(1 / mse)))
cv2.imwrite(os.path.join(LAYERS, "_reconstruction.png"),
            np.clip(rec[:, :, ::-1] * 255, 0, 255).astype(np.uint8))

# ---- contact sheet
tiles = []
files = sorted(glob.glob(os.path.join(LAYERS, "text", "*.png"))) + \
    sorted(glob.glob(os.path.join(LAYERS, "photo", "*.png")))
TW, TH = 260, 200
for f in files:
    img = cv2.imread(f, cv2.IMREAD_UNCHANGED)
    if img.ndim == 2:
        img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGRA)
    if img.shape[2] == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2BGRA)
    h, w = img.shape[:2]
    s = min((TW - 16) / w, (TH - 34) / h)
    img = cv2.resize(img, (max(1, int(w * s)), max(1, int(h * s))), interpolation=cv2.INTER_AREA)
    h, w = img.shape[:2]
    tile = np.full((TH, TW, 3), 255, np.uint8)
    ck = ((np.indices((TH, TW)).sum(0) // 10) % 2).astype(np.uint8)
    tile[:] = np.where(ck[..., None] == 1, 236, 250)
    ox, oy = (TW - w) // 2, 6 + (TH - 34 - h) // 2
    a = img[..., 3:4].astype(np.float32) / 255
    reg = tile[oy:oy + h, ox:ox + w].astype(np.float32)
    tile[oy:oy + h, ox:ox + w] = (reg * (1 - a) + img[..., :3] * a).astype(np.uint8)
    cv2.putText(tile, os.path.basename(f)[:-4], (6, TH - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.45,
                (40, 20, 40), 1, cv2.LINE_AA)
    cv2.rectangle(tile, (0, 0), (TW - 1, TH - 1), (200, 200, 200), 1)
    tiles.append(tile)
cols = 6
rows = (len(tiles) + cols - 1) // cols
sheet = np.full((rows * TH, cols * TW, 3), 255, np.uint8)
for i, t in enumerate(tiles):
    r, c = divmod(i, cols)
    sheet[r * TH:(r + 1) * TH, c * TW:(c + 1) * TW] = t
cv2.imwrite(os.path.join(LAYERS, "_overview.png"), sheet)
print("overview:", sheet.shape, len(tiles), "layers")
