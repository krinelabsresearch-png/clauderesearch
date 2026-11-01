"""Step 3 - synthesise the 12 s, 100 BPM (5 bars) reggaeton loop + sound design, synced to the visuals.

Everything is generated from scratch (no samples) -> no licensing issues.
Output: out/otium_audio.wav (44.1 kHz stereo, seamless loop)
"""
import os
import numpy as np
from scipy import signal
from scipy.io import wavfile

from common import OUT, BEAT, DURATION
import render as R   # reuse the exact visual timeline

SR = 44100
B = BEAT
S16 = B / 4
N = int(SR * DURATION)
rng = np.random.RandomState(3)


def tt(d):
    return np.arange(int(d * SR)) / SR


def place(buf, x, t0, pan=0.0, gain=1.0):
    """add mono x at time t0 (s) into a stereo bus, wrapping around the loop point."""
    i0 = int(round(t0 * SR))
    l = gain * np.sqrt(0.5 * (1 - pan))
    r = gain * np.sqrt(0.5 * (1 + pan))
    idx = (np.arange(len(x)) + i0) % N       # tails of bar 4 ring into bar 1 -> seamless loop
    np.add.at(buf[0], idx, x * l)
    np.add.at(buf[1], idx, x * r)


def bp(x, lo, hi, order=2):
    return signal.sosfilt(signal.butter(order, [lo, hi], btype="band", fs=SR, output="sos"), x)


def hp(x, f, order=2):
    return signal.sosfilt(signal.butter(order, f, btype="high", fs=SR, output="sos"), x)


def lp(x, f, order=2):
    return signal.sosfilt(signal.butter(order, f, btype="low", fs=SR, output="sos"), x)


def noise(d):
    return rng.randn(int(d * SR))


def osc(freq_env):
    return np.sin(2 * np.pi * np.cumsum(freq_env) / SR)


# ------------------------------------------------------------------ instruments
def kick(gain=1.0):
    t = tt(0.45)
    x = osc(44 + 120 * np.exp(-t / 0.032)) * np.exp(-t / 0.30)
    click = hp(noise(0.004), 2000) * 0.25
    x[:len(click)] += click
    return np.tanh(1.8 * x) * gain


def snare():
    t = tt(0.32)
    body = osc(np.full(len(t), 185.0)) * np.exp(-t / 0.045) * 0.55
    nz = bp(noise(0.32), 900, 7000) * np.exp(-t / 0.11)
    clap = np.zeros_like(t)
    for k, dt in enumerate((0.0, 0.009, 0.019)):
        i = int(dt * SR)
        e = np.exp(-(t[: len(t) - i]) / (0.008 if k < 2 else 0.09))
        clap[i:] += bp(noise(0.32), 1100, 3800)[: len(t) - i] * e
    return np.tanh((body + nz * 0.5 + clap * 0.6) * 1.4) * 0.55


def hat(open_=False):
    d = 0.16 if open_ else 0.05
    t = tt(d)
    return hp(noise(d), 7500, 4) * np.exp(-t / (0.06 if open_ else 0.014)) * 0.22


def sub(f0, dur):
    t = tt(dur + 0.08)
    f = f0 * (1 + 0.6 * np.exp(-t / 0.012))
    env = np.minimum(1, t / 0.004) * np.where(t < dur, 1.0, np.exp(-(t - dur) / 0.03))
    return np.tanh(1.6 * osc(f) * env) * 0.55


def pluck(f0, dur=0.42, bright=1.0):
    """marimba-ish additive pluck: higher harmonics decay faster."""
    t = tt(dur)
    x = np.zeros_like(t)
    for h, a in ((1, 1.0), (2, 0.45 * bright), (3, 0.28 * bright), (4, 0.16 * bright), (6, 0.07 * bright)):
        x += a * np.sin(2 * np.pi * f0 * h * t + h) * np.exp(-t * (6 + 9 * h))
    return x * np.minimum(1, t / 0.002) * 0.33


def pad(freqs, dur):
    t = tt(dur)
    x = np.zeros_like(t)
    for f in freqs:
        for det in (-0.12, 0.0, 0.11):
            ff = f * 2 ** (det / 12)
            for h in range(1, 6):
                x += np.sin(2 * np.pi * ff * h * t + rng.rand() * 6) / (h * 1.6)
    env = np.minimum(1, t / 0.25) * np.minimum(1, (dur - t) / 0.3)
    return lp(x, 1400) * env * 0.035


def twinkle(gain=0.5):
    t = tt(0.5)
    x = np.zeros_like(t)
    for f, a, d in ((2637, 1.0, 0.18), (3951, 0.6, 0.12), (5274, 0.35, 0.08), (7040, 0.2, 0.05)):
        x += a * np.sin(2 * np.pi * f * t) * np.exp(-t / d)
    return x * np.minimum(1, t / 0.001) * 0.18 * gain


def whoosh(dur, f0, f1, gain=0.5, rev=False):
    t = tt(dur)
    nz = noise(dur)
    out = np.zeros_like(nz)
    blocks = 48
    edges = np.linspace(0, len(nz), blocks + 1).astype(int)
    zi = np.zeros((2, 2))
    for b in range(blocks):
        fc = f0 * (f1 / f0) ** (b / (blocks - 1))
        sos = signal.butter(2, [fc * 0.6, min(fc * 1.6, SR / 2 - 100)], btype="band", fs=SR, output="sos")
        out[edges[b]:edges[b + 1]], zi = signal.sosfilt(sos, nz[edges[b]:edges[b + 1]], zi=zi)
    env = np.sin(np.pi * np.clip(t / dur, 0, 1)) ** 1.5
    if rev:
        env = (t / dur) ** 2.2 * np.minimum(1, (dur - t) / 0.01)
    return out * env * gain


def thump(gain=1.0):
    """letterpress stamp: low body + paper slap."""
    t = tt(0.35)
    body = osc(60 + 70 * np.exp(-t / 0.02)) * np.exp(-t / 0.09)
    slap = lp(hp(noise(0.35), 300), 2600) * np.exp(-t / 0.025)
    return np.tanh((body * 0.9 + slap * 0.8) * 1.5) * 0.5 * gain


def tick(gain=0.3, f=3200):
    t = tt(0.03)
    return bp(noise(0.03), f * 0.7, f * 1.4) * np.exp(-t / 0.004) * gain


def impact(gain=1.0):
    t = tt(1.6)
    boom = osc(30 + 60 * np.exp(-t / 0.08)) * np.exp(-t / 0.55)
    crash = hp(noise(1.6), 3500) * np.exp(-t / 0.45) * 0.35
    return np.tanh((boom * 1.1 + crash) * 1.3) * 0.7 * gain


def reverb(x):
    """small Schroeder room (wet only)."""
    y = np.zeros_like(x)
    for d, g in ((1557, 0.80), (1617, 0.79), (1491, 0.81), (1422, 0.78)):
        a = np.zeros(d + 1); a[0] = 1; a[-1] = -g
        y += signal.lfilter([1.0], a, x)
    y /= 4
    for d, g in ((225, 0.5), (556, 0.5)):
        b = np.zeros(d + 1); b[0] = -g; b[-1] = 1
        a = np.zeros(d + 1); a[0] = 1; a[-1] = -g
        y = signal.lfilter(b, a, y)
    return lp(y, 5000)


# ------------------------------------------------------------------ arrangement
drums, bass, music, sfx, verb = (np.zeros((2, N)) for _ in range(5))

K = kick()
SN = snare()
NBARS = int(round(DURATION / (4 * B)))       # 5
for bar in range(NBARS):
    for st in (0, 4, 8, 12):
        place(drums, K, bar * 4 * B + st * S16, gain=0.95)
    for st in (3, 6, 11, 14):
        place(drums, SN, bar * 4 * B + st * S16, pan=0.05)
        place(verb, SN, bar * 4 * B + st * S16, gain=0.6)
    if bar >= 1:
        for st in range(0, 16, 2):
            place(drums, hat(open_=(st % 4 == 2)), bar * 4 * B + st * S16, pan=0.25,
                  gain=0.8 + 0.25 * (st % 4 == 2))
        for st in (5, 13):
            place(drums, hat(), bar * 4 * B + st * S16, pan=-0.2, gain=0.6)

roots = [55.0, 43.65, 65.41, 49.0, 55.0]               # Am  F  C  G  Am(drop)
for bar in range(1, NBARS):                            # bar 1 = intro, sub drops on bar 2
    for st, ln in [(0, 3), (3, 5), (8, 3), (11, 5)]:
        place(bass, sub(roots[bar], ln * S16 * 0.92), bar * 4 * B + st * S16)

chords = [[69, 72, 76, 81], [65, 69, 72, 77], [67, 72, 76, 79], [67, 71, 74, 79], [69, 72, 76, 81]]
motif = [(0, 3), (3, 1), (6, 2), (8, 0), (10, 2), (11, 3), (14, 1)]
for bar in range(NBARS):
    for st, deg in motif:
        f = 440 * 2 ** ((chords[bar][deg] - 69) / 12)
        x = pluck(f)
        place(music, x, bar * 4 * B + st * S16, pan=-0.25 + 0.5 * (deg / 3), gain=0.8)
        place(verb, x, bar * 4 * B + st * S16, gain=0.5)
    place(music, pad([440 * 2 ** ((n - 81) / 12) for n in chords[bar][:3]], 4 * B), bar * 4 * B)

# intro: low-pass sweep on the music through bar 1
tA = np.arange(N) / SR
cut = np.where(tA < 4 * B, 350 * (18000 / 350) ** (np.clip(tA / (4 * B), 0, 1) ** 2.2), 18000)
edges = np.linspace(0, N, 201).astype(int)
for ch in range(2):
    zi = np.zeros((1, 2))
    y = np.zeros(N)
    for b in range(200):
        sos = signal.butter(2, min(float(cut[edges[b]]), SR / 2 - 200), btype="low", fs=SR, output="sos")
        y[edges[b]:edges[b + 1]], zi = signal.sosfilt(sos, music[ch, edges[b]:edges[b + 1]], zi=zi)
    music[ch] = y

# ------------------------------------------------------------------ sound design (synced to render.py)
place(sfx, impact(0.75), 0.0)                                         # loop downbeat boom
place(sfx, whoosh(R.T_FLY1 - R.T_FLY0 + 0.15, 900, 5000, 0.35), R.T_FLY0 - 0.1, pan=-0.5)
place(sfx, whoosh(R.T_IRIS1 - R.T_IRIS0 + 0.3, 300, 2500, 0.25), R.T_IRIS0, pan=0.2)
for i, (name, th) in enumerate(R.LOGO_HITS):                          # letterpress stamps
    place(sfx, thump(0.9), th, pan=-0.6 + 0.3 * i)
place(sfx, whoosh(R.T_PAN1 - R.T_PAN0, 1800, 250, 0.28), R.T_PAN0)    # camera tilt
t_pr = tt(1.6)                                                        # riso press rattle
press = bp(noise(1.6), 1500, 6000) * (0.5 + 0.5 * np.sign(np.sin(2 * np.pi * t_pr / S16))) \
    * np.sin(np.pi * t_pr / 1.6) ** 2 * 0.05
place(sfx, press, R.T_REVEAL + 0.1, pan=0.3)
for i in range(R.META["n_atv"]):
    place(sfx, tick(0.18, 2600 + 150 * i), R.T_ATV + i * R.ATV_STAG + 0.05, pan=-0.6 + i * 0.1)
for i in range(R.META["n_fir"]):
    place(sfx, tick(0.12, 4200), R.T_FIR + i * R.FIR_STAG + 0.05, pan=0.6)
place(sfx, twinkle(0.9), R.T_SSTAR, pan=0.55)
place(verb, twinkle(0.9), R.T_SSTAR, pan=0.55)
place(sfx, whoosh(0.32, 2500, 600, 0.22), R.T_DOM, pan=-0.5)
place(sfx, thump(1.5), R.T_DATE, pan=-0.4)                           # 15/11 stamp
place(sfx, impact(0.35), R.T_DATE, pan=-0.3)
place(sfx, twinkle(1.0), R.T_BSTAR)
place(verb, twinkle(1.0), R.T_BSTAR)
for kk in range(8):                                                   # slot-machine ratchet
    start = R.T_ROLL0 + kk * 0.018
    stop = R.T_STOP0 + kk * (B / 16)
    n_g = 7 + kk
    for g in range(n_g):
        frac = (g + 1) / n_g                     # reel position n = n_g*(1-ease_out_cubic(u))
        u = 1 - (1 - frac) ** (1 / 3)
        place(sfx, tick(0.09, 3600), start + u * (stop - start), pan=0.2 + kk * 0.06)
    place(sfx, tick(0.32, 1800), stop, pan=0.2 + kk * 0.06)
for name, tg in R.GENRES:
    bullet = name.startswith("g_b")
    place(sfx, tick(0.22 if bullet else 0.16, 2200 if bullet else 3000), tg, pan=0.5)
riser_t0 = R.T_FLASH - 0.95                                           # riser into the drop
place(sfx, whoosh(0.95, 300, 9000, 0.32, rev=True), riser_t0)
t_r = tt(0.95)
place(sfx, np.sin(2 * np.pi * np.cumsum(220 * 2 ** (2.2 * t_r / 0.95)) / SR) * (t_r / 0.95) ** 2 * 0.06,
      riser_t0)
for i in range(18):                                                   # CTA typing
    place(sfx, tick(0.13, 2900 + rng.rand() * 600), R.T_TYPE0 + i * (R.T_TYPE1 - R.T_TYPE0) / 18, pan=0.4)
place(sfx, whoosh(R.T_FILL1 - R.T_FILL0 + 0.05, 600, 4000, 0.3), R.T_FILL0, pan=0.5)
place(sfx, impact(1.0), R.T_FLASH)                                    # strobe flash
place(verb, twinkle(1.2), R.T_FLASH + 0.02)
place(sfx, twinkle(0.6), R.T_SPIN, pan=-0.2)
place(sfx, whoosh(DURATION - R.T_CLOSE0 + 0.02, 400, 7000, 0.35, rev=True), R.T_CLOSE0 - 0.02)
for q in range(int((R.T_REVEAL + 1.5) / S16), int((R.T_CLOSE0 - 0.1) / S16)):   # ball sparkles
    if rng.rand() < 0.16:
        place(verb, twinkle(0.35), q * S16, pan=rng.uniform(-0.6, 0.6))

# ------------------------------------------------------------------ mix
# render the reverb on 2 loops so its tail wraps into the start
verb2 = np.concatenate([verb, verb], 1)
verb_w = np.stack([reverb(verb2[0]), reverb(verb2[1])])[:, N:]
duck = np.ones(N)                                     # kick sidechain on music + bass
for kt in R.KICKS:
    d = tt(0.22)
    idx = (np.arange(len(d)) + int(kt * SR)) % N
    duck[idx] = np.minimum(duck[idx], 1 - 0.45 * np.exp(-d / 0.08))
mix = drums * 0.9 + bass * duck * 0.95 + music * duck * 0.85 + sfx * 0.9 + verb_w * 0.35
mix = hp(np.concatenate([mix, mix], 1), 25)[:, N:]
mix = np.tanh(mix * 1.15) / np.tanh(1.15)
mix = mix / np.max(np.abs(mix)) * 0.89               # ~ -1 dBFS true-ish peak
os.makedirs(OUT, exist_ok=True)
path = os.path.join(OUT, "otium_audio.wav")
wavfile.write(path, SR, (mix.T * 32767).astype(np.int16))
print("wrote", path, mix.shape)
