#!/usr/bin/env python3
"""Sintetizza gli effetti sonori del reel in un'unica traccia (public/sfx/sfx.wav).

Nessun campione registrato: ogni suono è costruito qui (oscillatori, rumore
filtrato, inviluppi). I tempi arrivano da src/sfx-events.ts, che li ricava dalle
stesse parole della voce su cui si muovono le animazioni.

Uso: npm run sfx
"""
import json
import math
import subprocess
import wave
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'public' / 'sfx' / 'sfx.wav'
SR = 48000
rng = np.random.default_rng(1010)


def load():
    js = "import('./src/sfx-events.ts').then(m => console.log(JSON.stringify({ev: m.sfxEvents(), meta: m.SFX_META})))"
    res = subprocess.run(['node', '--experimental-strip-types', '--no-warnings', '-e', js],
                         cwd=ROOT, capture_output=True, text=True, check=True)
    return json.loads(res.stdout)


def t_axis(dur):
    return np.arange(int(dur * SR)) / SR


def band(x, lo, hi):
    """Segnale filtrato in una banda, con fianchi morbidi."""
    f = np.fft.rfftfreq(len(x), 1 / SR)
    m = 1 / (1 + (lo / np.maximum(f, 1)) ** 4) / (1 + (f / hi) ** 4)
    return np.fft.irfft(np.fft.rfft(x) * m, len(x))


def sweep_lowpass(x, f0, f1):
    """Passa-basso a un polo con frequenza che scorre da f0 a f1 (esponenziale)."""
    n = len(x)
    fc = f0 * (f1 / f0) ** (np.arange(n) / max(n - 1, 1))
    a = 1 - np.exp(-2 * math.pi * fc / SR)
    y = np.empty(n)
    s = 0.0
    for i in range(n):
        s += a[i] * (x[i] - s)
        y[i] = s
    return y


def norm(x):
    p = np.max(np.abs(x)) if len(x) else 0
    return x / p if p > 0 else x


def bell(freqs, decays, dur, amps=None):
    t = t_axis(dur)
    out = np.zeros_like(t)
    for i, (f, d) in enumerate(zip(freqs, decays)):
        a = amps[i] if amps else 1 / (i + 1)
        out += a * np.sin(2 * math.pi * f * t + rng.random() * 6) * np.exp(-t / d)
    return out * (1 - np.exp(-t / 0.0015))


# ─── I suoni ──────────────────────────────────────────────────────────────────
def spin(dur, land, offset=0.0, fade_in=False):
    """Moneta che gira: lampi metallici due volte per giro, sempre più lenti."""
    t = t_axis(dur)
    tau = t + offset  # tempo della moneta, come in world.ts
    theta = 3.3 * np.clip(land - tau, 0, None) ** 2
    speed = np.clip(6.6 * (land - tau), 0, None) / 18
    face = (0.5 + 0.5 * np.cos(2 * theta)) ** 6
    metal = band(rng.standard_normal(len(t)), 2500, 9000)
    ring = 0.4 * np.sin(2 * math.pi * 3150 * t) + 0.25 * np.sin(2 * math.pi * 4720 * t)
    air = band(rng.standard_normal(len(t)), 150, 1200)
    y = norm(metal) * face * (0.35 + 0.65 * speed) + 0.25 * ring * face * speed + 0.5 * norm(air) * speed ** 1.5
    if fade_in:
        y *= np.clip(t / dur, 0, 1) ** 2
    return y


def clink():
    y = bell([2960, 4630, 6890, 9120], [0.7, 0.45, 0.3, 0.18], 1.2)
    # due piccoli rimbalzi mentre la moneta si assesta
    for dt, a in ((0.085, 0.35), (0.16, 0.15)):
        k = int(dt * SR)
        b = bell([3010, 4700, 6950], [0.3, 0.2, 0.12], 1.2 - dt)
        y[k:k + len(b)] += a * b[:len(y) - k]
    return y


def riser(dur):
    y = sweep_lowpass(rng.standard_normal(int(dur * SR)), 250, 6000)
    t = t_axis(dur)
    return norm(y) * (t / dur) ** 2


def boom():
    t = t_axis(1.2)
    f = 38 + 30 * np.exp(-t / 0.08)
    body = np.sin(2 * math.pi * np.cumsum(f) / SR) * np.exp(-t / 0.45)
    hit = band(rng.standard_normal(len(t)), 60, 2500) * np.exp(-t / 0.03)
    return body + 0.35 * norm(hit)


def thump():
    t = t_axis(0.5)
    f = 60 + 90 * np.exp(-t / 0.03)
    return np.sin(2 * math.pi * np.cumsum(f) / SR) * np.exp(-t / 0.14)


def whoosh():
    dur = 0.5
    t = t_axis(dur)
    up = sweep_lowpass(rng.standard_normal(len(t)), 400, 5000)
    env = np.sin(math.pi * np.clip(t / dur, 0, 1)) ** 2
    return norm(up - sweep_lowpass(up, 150, 900)) * env


def click():
    t = t_axis(0.25)
    snap = band(rng.standard_normal(len(t)), 1500, 12000) * np.exp(-t / 0.004)
    low = np.sin(2 * math.pi * 170 * t) * np.exp(-t / 0.04)
    return 0.8 * norm(snap) + 0.6 * low


def win():
    y = np.zeros(int(1.6 * SR))
    for i, f in enumerate((1318.5, 1661.2, 1975.5, 2637.0)):
        b = bell([f, f * 2, f * 3.01], [0.9, 0.4, 0.2], 1.6 - i * 0.07, [1, 0.3, 0.12])
        k = int(i * 0.07 * SR)
        y[k:k + len(b)] += b[:len(y) - k]
    t = t_axis(1.6)
    shimmer = band(rng.standard_normal(len(t)), 6000, 14000) * np.exp(-t / 0.5) * (1 - np.exp(-t / 0.05))
    return y + 0.2 * norm(shimmer)


def sparkler(dur):
    n = int(dur * SR)
    t = t_axis(dur)
    y = np.zeros(n)
    hits = rng.random(n) < 420 / SR
    y[hits] = rng.standard_normal(hits.sum())
    crackle = band(y, 2000, 14000)
    hiss = band(rng.standard_normal(n), 5000, 13000)
    env = np.clip(t / 0.25, 0, 1) * np.clip((dur - t) / 0.3, 0, 1)
    return (norm(crackle) + 0.25 * norm(hiss)) * env


def tap():
    t = t_axis(0.2)
    return np.sin(2 * math.pi * 1250 * t) * np.exp(-t / 0.035) + 0.4 * norm(band(rng.standard_normal(len(t)), 3000, 12000)) * np.exp(-t / 0.006)


def tink():
    return bell([2620, 5290, 7810], [0.2, 0.12, 0.07], 0.5, [1, 0.45, 0.2])


def tick():
    t = t_axis(0.06)
    sq = np.sign(np.sin(2 * math.pi * 1900 * t))
    return band(sq, 400, 9000) * np.exp(-t / 0.015)


SOUNDS = {'clink': clink, 'boom': boom, 'thump': thump, 'whoosh': whoosh, 'click': click, 'win': win, 'tap': tap, 'tink': tink, 'tick': tick}


def main():
    data = load()
    meta = data['meta']
    n = int(math.ceil(meta['duration'] * SR))
    L = np.zeros(n)
    R = np.zeros(n)
    for e in data['ev']:
        k = e['kind']
        if k == 'spin':
            y = spin(e['dur'], meta['land'])
        elif k == 'spinIn':
            # la moneta che torna: stesso suono dell'inizio, il tempo della moneta arriva a 0 sull'ultimo fotogramma
            y = spin(e['dur'], meta['land'], offset=-e['dur'], fade_in=True)
        elif k == 'riser':
            y = riser(e['dur'])
        elif k == 'sparkler':
            y = sparkler(e['dur'])
        else:
            y = SOUNDS[k]()
        y = norm(y) * e['gain']
        i = int(round(e['t'] * SR))
        if i >= n:
            continue
        y = y[:n - i]
        # piccola apertura stereo per i suoni d'ambiente
        pan = 0.5 + 0.18 * math.sin(e['t'] * 7.3) if k in ('whoosh', 'sparkler', 'riser') else 0.5
        L[i:i + len(y)] += y * math.sqrt(1 - pan)
        R[i:i + len(y)] += y * math.sqrt(pan)
    mix = np.stack([L, R], axis=1)
    # limitatore morbido, poi livello sotto la voce
    mix = np.tanh(mix * 1.1) / np.tanh(1.1)
    mix *= 0.5 / max(np.max(np.abs(mix)), 1e-9)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with wave.open(str(OUT), 'wb') as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((np.clip(mix, -1, 1) * 32767).astype('<i2').tobytes())
    print(f'Effetti: {len(data["ev"])} suoni, {n / SR:.2f} s -> {OUT.relative_to(ROOT)}')


if __name__ == '__main__':
    main()
