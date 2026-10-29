#!/usr/bin/env python3
"""Genera la voce del reel con Gemini TTS e scrive src/voice-timings.ts.

Un file audio per periodo (vedi GROUPS in src/script.ts). Ogni file viene:
  1. generato con il modello vocale di Gemini;
  2. ripulito dai silenzi iniziali/finali e portato a volume uniforme;
  3. ritrascritto da Gemini e rigenerato se non corrisponde al testo;
  4. analizzato per trovare le pause reali tra una frase e l'altra.
I tempi risultanti guidano sottotitoli e animazioni del video.

Uso: npm run voice            (richiede GEMINI_API_KEY)
     VOICE_NAME=Kore npm run voice   per cambiare voce
I file già generati con lo stesso testo e la stessa voce vengono riusati.
"""
import array
import base64
import difflib
import hashlib
import io
import json
import math
import os
import re
import subprocess
import sys
import time
import urllib.error
import urllib.request
import wave
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'public' / 'voice'
RAW = ROOT / 'voice-raw'
TIMINGS = ROOT / 'src' / 'voice-timings.ts'

TTS_MODEL = os.environ.get('TTS_MODEL', 'gemini-3.8-flash-tts')
STT_MODEL = os.environ.get('STT_MODEL', 'gemini-3.6-flash')
VOICE_NAME = os.environ.get('VOICE_NAME', 'Charon')
# Accelerazione della voce (il tono non cambia): tiene il reel sotto i 60 secondi.
SPEED = float(os.environ.get('VOICE_SPEED', '1.1'))
API = 'https://generativelanguage.googleapis.com/v1beta/models/{}:generateContent'
MIN_MATCH = 0.82
ATTEMPTS = 3

HEADER = '''// File generato da scripts/make-voice.py (npm run voice): non modificarlo a mano.
// null = nessuna voce, i tempi del video sono stimati in script.ts.

export type VoiceTiming = {
  file: string;
  /** durata del file audio, in secondi */
  dur: number;
  /** inizio e fine di ogni frase del periodo, in secondi dall'inizio del file */
  phrases: {start: number; end: number}[];
};

'''


def write_timings(voice):
    body = 'null' if voice is None else json.dumps(voice, ensure_ascii=False, indent=2)
    TIMINGS.write_text(f'{HEADER}export const VOICE: VoiceTiming[] | null = {body};\n', encoding='utf-8')


def load_groups():
    js = "import('./src/script.ts').then(m => console.log(JSON.stringify(m.GROUPS)))"
    res = subprocess.run(['node', '--experimental-strip-types', '--no-warnings', '-e', js],
                         cwd=ROOT, check=True, capture_output=True, text=True)
    return json.loads(res.stdout)


def gemini(model, body, tries=5):
    key = os.environ.get('GEMINI_API_KEY')
    if not key:
        sys.exit('Manca GEMINI_API_KEY')
    for attempt in range(tries):
        req = urllib.request.Request(API.format(model), data=json.dumps(body).encode(),
                                     headers={'x-goog-api-key': key, 'Content-Type': 'application/json'})
        try:
            with urllib.request.urlopen(req, timeout=180) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            full = e.read().decode(errors='replace')
            msg = full[:400]
            if e.code in (429, 500, 502, 503, 504) and attempt < tries - 1:
                # sul piano gratuito la quota si azzera ogni minuto: attende quanto chiede il server
                m = re.search(r'"retryDelay":\s*"(\d+)s"', full)
                time.sleep(int(m.group(1)) + 2 if m else 3 * 2 ** attempt)
                continue
            if 'quotaId' in full:
                msg += ' | ' + ', '.join(sorted(set(re.findall(r'"quotaId":\s*"([^"]+)"', full))))
            sys.exit(f'Errore Gemini {e.code} ({model}): {msg}')


def tts(text):
    d = gemini(TTS_MODEL, {
        'contents': [{'parts': [{'text': text}]}],
        'generationConfig': {
            'responseModalities': ['AUDIO'],
            'speechConfig': {'voiceConfig': {'prebuiltVoiceConfig': {'voiceName': VOICE_NAME}}},
        },
    })
    data = base64.b64decode(d['candidates'][0]['content']['parts'][0]['inlineData']['data'])
    if data.startswith(b'RIFF'):
        return data
    # Alcuni modelli restituiscono PCM grezzo 16 bit, 24 kHz, mono.
    buf = io.BytesIO()
    with wave.open(buf, 'wb') as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(24000)
        w.writeframes(data)
    return buf.getvalue()


def clean(raw_path, out_path, speed=1.0):
    """Toglie i silenzi ai bordi, applica la velocità e porta il volume a -16 LUFS (standard per i social)."""
    af = (f'atempo={speed},' if speed != 1.0 else '') + (
          'silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.03,areverse,'
          'silenceremove=start_periods=1:start_threshold=-45dB:start_silence=0.08,areverse,'
          'loudnorm=I=-16:TP=-1.5:LRA=11')
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', str(raw_path), '-af', af, '-ar', '48000', '-ac', '1',
                    '-c:a', 'pcm_s16le', str(out_path)], check=True)


def read_wav(path):
    with wave.open(str(path)) as w:
        sr = w.getframerate()
        samples = array.array('h', w.readframes(w.getnframes()))
    return sr, samples


def pauses(path, thr_db=-40.0, min_len=0.09):
    """Pause interne (inizio, fine) in secondi, a blocchi da 10 ms."""
    sr, s = read_wav(path)
    hop = sr // 100
    quiet = []
    for i in range(len(s) // hop):
        seg = s[i * hop:(i + 1) * hop]
        rms = math.sqrt(sum(x * x for x in seg) / hop) or 1
        quiet.append(20 * math.log10(rms / 32768) < thr_db)
    out, run = [], None
    for i, q in enumerate(quiet + [False]):
        if q and run is None:
            run = i
        elif not q and run is not None:
            a, b = run / 100, i / 100
            if b - a >= min_len and a > 0.05 and b < len(quiet) / 100 - 0.05:
                out.append((a, b))
            run = None
    return out


def words(s):
    s = s.lower().replace('’', "'")
    return re.sub(r"[^\w' ]+", ' ', s).split()


def spoken_weight(s):
    letters = len(re.findall(r'\w', s))
    return 0.08 * len(s.split()) + 0.046 * letters + 0.16 * s.count(',')


def transcribe(path):
    b64 = base64.b64encode(path.read_bytes()).decode()
    d = gemini(STT_MODEL, {'contents': [{'parts': [
        {'inlineData': {'mimeType': 'audio/wav', 'data': b64}},
        {'text': 'Trascrivi esattamente le parole di questo audio in italiano. Scrivi i numeri in lettere '
                 'e le sigle in maiuscolo. Rispondi solo con la trascrizione.'},
    ]}]})
    return d['candidates'][0]['content']['parts'][0]['text'].strip()


def phrase_times(path, dur, says):
    """Inizio/fine di ogni frase: aggancia ogni confine alla pausa reale più vicina."""
    if len(says) == 1:
        return [{'start': 0.0, 'end': round(dur, 3)}]
    w = [spoken_weight(s) for s in says]
    total = sum(w)
    found = pauses(path)
    times, start, after = [], 0.0, 0.0
    for b in range(len(says) - 1):
        expected = dur * sum(w[:b + 1]) / total
        cands = [p for p in found if p[0] >= after]
        best = min(cands, key=lambda p: abs((p[0] + p[1]) / 2 - expected), default=None)
        if best and abs((best[0] + best[1]) / 2 - expected) <= max(0.4, 0.3 * dur):
            end, nxt = best[0], best[1]
            after = best[1]
        else:
            end = nxt = expected
        times.append({'start': round(start, 3), 'end': round(end, 3)})
        start = nxt
    times.append({'start': round(start, 3), 'end': round(dur, 3)})
    return times


def main():
    # I periodi si leggono senza voce: un voice-timings.ts vecchio potrebbe non coincidere.
    previous = TIMINGS.read_text(encoding='utf-8') if TIMINGS.exists() else None
    write_timings(None)
    try:
        groups = load_groups()
    except Exception:
        if previous:
            TIMINGS.write_text(previous, encoding='utf-8')
        raise
    OUT.mkdir(parents=True, exist_ok=True)
    RAW.mkdir(parents=True, exist_ok=True)

    voice, report = [], []
    for i, g in enumerate(groups):
        name = f'g{i:02d}.wav'
        out = OUT / name
        meta_path = RAW / f'g{i:02d}.json'
        sig = hashlib.sha256(f'{TTS_MODEL}|{VOICE_NAME}|{g["say"]}'.encode()).hexdigest()
        meta = json.loads(meta_path.read_text()) if meta_path.exists() else {}
        if meta.get('sig') == sig and 'raw' not in meta and out.exists():
            # Cache di una versione precedente: ritrova il tentativo scelto confrontando i file.
            same = [p for p in RAW.glob(f'g{i:02d}_try*_clean.wav') if p.read_bytes() == out.read_bytes()]
            if same:
                meta['raw'] = same[0].name.replace('_clean', '')
        if meta.get('sig') == sig and (RAW / meta.get('raw', '-')).exists():
            heard, score = meta['heard'], meta['score']
        else:
            best = None
            for attempt in range(ATTEMPTS):
                raw = RAW / f'g{i:02d}_try{attempt}.wav'
                raw.write_bytes(tts(g['say']))
                cand = RAW / f'g{i:02d}_try{attempt}_clean.wav'
                clean(raw, cand)
                sr, s = read_wav(cand)
                dur = len(s) / sr
                ratio = dur / spoken_weight(g['say'])
                heard = transcribe(cand)
                score = difflib.SequenceMatcher(None, words(g['say']), words(heard)).ratio()
                ok = score >= MIN_MATCH and 0.55 <= ratio <= 1.9
                print(f'  g{i:02d} tentativo {attempt + 1}: {dur:.2f}s, corrispondenza {score:.2f}'
                      f'{"" if ok else "  -> rifaccio"}', flush=True)
                if best is None or score > best[1]:
                    best = (raw, score, heard)
                if ok:
                    break
            raw, score, heard = best
            if score < MIN_MATCH:
                sys.exit(f'g{i:02d}: la voce non corrisponde al testo dopo {ATTEMPTS} tentativi.\n'
                         f'  atteso: {g["say"]}\n  sentito: {heard}')
            meta = {'sig': sig, 'heard': heard, 'score': score, 'raw': raw.name}
        meta_path.write_text(json.dumps(meta, ensure_ascii=False))
        clean(RAW / meta['raw'], out, SPEED)
        sr, s = read_wav(out)
        dur = round(len(s) / sr, 3)
        voice.append({'file': name, 'dur': dur, 'phrases': phrase_times(out, dur, g['says'])})
        report.append((i, dur, score, g['say'], heard))
        print(f'g{i:02d} {dur:5.2f}s  {score:.2f}  {g["say"]}', flush=True)

    for f in OUT.glob('g*.wav'):
        if f.name not in {v['file'] for v in voice}:
            f.unlink()
    write_timings(voice)
    total = sum(v['dur'] for v in voice)
    print(f'\nVoce: {len(voice)} periodi, {total:.1f} s di parlato, voce {VOICE_NAME} ({TTS_MODEL}).')
    low = [r for r in report if r[2] < 0.95]
    for i, dur, score, said, heard in low:
        print(f'  da controllare g{i:02d} ({score:.2f}): sentito "{heard}"')


if __name__ == '__main__':
    main()
