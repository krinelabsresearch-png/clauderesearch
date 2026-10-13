"""Radar B6: app AI che vanno forte negli USA e sono deboli o assenti in Italia, Spagna, Germania e Francia.

Usa solo API pubbliche di Apple, senza chiavi. Solo libreria standard di Python 3.9+.
Esecuzione:  python3 radar_appstore.py                 (paesi di default: it,es,de,fr)
             python3 radar_appstore.py --paesi it --out risultati_it.csv
Uscite: un CSV ordinato per "gap" e un'istantanea JSON in dati/ (per confrontare le settimane).
"""

import argparse
import csv
import datetime as dt
import json
import math
import os
import re
import sys
import time
import urllib.error
import urllib.request

# Classifica generale + categorie dove stanno quasi tutte le app AI consumer
GENERI = {
    "Tutte": None, "Produttività": 6007, "Foto e video": 6008, "Stile di vita": 6012,
    "Salute e fitness": 6013, "Istruzione": 6017, "Utility": 6002, "Social": 6005,
    "Intrattenimento": 6016, "Grafica e design": 6027, "Musica": 6011, "Viaggi": 6003,
    "Finanza": 6015,
}
LINGUA = {"it": "IT", "es": "ES", "de": "DE", "fr": "FR"}
AI_RE = re.compile(r"\bA\.?I\.?\b|artificial intelligence|\bGPT|chatbot|\bLLM\b|machine learning|neural", re.I)
PESO_GENERALE, PESO_GENERE = 1.0, 0.6


def get_json(url, tentativi=3):
    for t in range(tentativi):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (radar-b6)"})
            with urllib.request.urlopen(req, timeout=30) as r:
                return json.loads(r.read().decode("utf-8"))
        except (urllib.error.URLError, json.JSONDecodeError, TimeoutError) as e:
            if t == tentativi - 1:
                print(f"  ! errore su {url}: {e}", file=sys.stderr)
                return None
            time.sleep(2 * (t + 1))


def classifica(paese, genere_id):
    """Top 200 per incassi (feed RSS storico di Apple). Ritorna [(id_app, posizione)]."""
    g = f"/genre={genere_id}" if genere_id else ""
    dati = get_json(f"https://itunes.apple.com/{paese}/rss/topgrossingapplications/limit=200{g}/json")
    voci = (dati or {}).get("feed", {}).get("entry", [])
    if isinstance(voci, dict):
        voci = [voci]
    return [(int(e["id"]["attributes"]["im:id"]), i + 1) for i, e in enumerate(voci)]


def lookup(ids, paese):
    """Dettagli delle app nello store di un Paese (assenti = non disponibili lì)."""
    out, ids = {}, list(ids)
    for i in range(0, len(ids), 150):
        blocco = ",".join(map(str, ids[i:i + 150]))
        dati = get_json(f"https://itunes.apple.com/lookup?id={blocco}&country={paese}&entity=software")
        for r in (dati or {}).get("results", []):
            if "trackId" in r:
                out[r["trackId"]] = r
        time.sleep(1)
    return out


def forza(posizioni):
    """Da {genere: posizione} a un indice 0–1: conta di più la classifica generale."""
    migliore = 0.0
    for genere, pos in posizioni.items():
        peso = PESO_GENERALE if genere == "Tutte" else PESO_GENERE
        migliore = max(migliore, peso * (1 - (pos - 1) / 200))
    return migliore


def gap(forza_us, lingua_mancante, disponibile, pos_paese, recensioni_paese):
    """Quanto spazio lascia l'app in un Paese: alto = forte negli USA, debole lì."""
    f_lingua = 1.0 if lingua_mancante else 0.5
    if not disponibile:
        f_presenza = 1.0
    elif pos_paese is None:
        f_presenza = 0.8
    else:
        f_presenza = 0.3 * (pos_paese - 1) / 200
    f_recensioni = 1 / (1 + math.log10(1 + (recensioni_paese or 0)))
    return forza_us * f_lingua * f_presenza * f_recensioni


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paesi", default="it,es,de,fr")
    ap.add_argument("--out", default="radar_b6.csv")
    ap.add_argument("--tutte", action="store_true", help="includi anche app non AI")
    a = ap.parse_args()
    paesi = [p.strip().lower() for p in a.paesi.split(",")]

    pos = {}  # pos[paese][id][genere] = posizione
    for paese in ["us"] + paesi:
        pos[paese] = {}
        for genere, gid in GENERI.items():
            for app_id, p in classifica(paese, gid):
                pos[paese].setdefault(app_id, {})[genere] = p
            time.sleep(1)
        print(f"{paese.upper()}: {len(pos[paese])} app nelle classifiche")
    if not pos["us"]:
        sys.exit("Nessun dato dalle classifiche USA: controlla la connessione o il feed di Apple.")

    info_us = lookup(pos["us"].keys(), "us")
    candidati = {i: r for i, r in info_us.items()
                 if a.tutte or AI_RE.search(r.get("trackName", "") + " " + r.get("description", "")[:1500])}
    print(f"App AI tra le classifiche USA: {len(candidati)}")

    info = {p: lookup(candidati.keys(), p) for p in paesi}

    righe = []
    for app_id, r in candidati.items():
        lingue = set(r.get("languageCodesISO2A", []))
        f_us = forza(pos["us"][app_id])
        riga = {
            "app": r.get("trackName"), "venditore": r.get("sellerName"), "genere": r.get("primaryGenreName"),
            "prezzo_formattato": r.get("formattedPrice"), "forza_us": round(f_us, 3),
            "pos_us": json.dumps(pos["us"][app_id], ensure_ascii=False), "recensioni_us": r.get("userRatingCount"),
            "lingue": ",".join(sorted(lingue)), "url": r.get("trackViewUrl"),
        }
        gaps = []
        for p in paesi:
            disponibile = app_id in info[p]
            pos_p = min(pos[p].get(app_id, {}).values(), default=None)
            rec_p = info[p].get(app_id, {}).get("userRatingCount", 0)
            g = gap(f_us, LINGUA[p] not in lingue, disponibile, pos_p, rec_p)
            riga.update({f"{p}_disponibile": disponibile, f"{p}_lingua": LINGUA[p] in lingue,
                         f"{p}_pos": pos_p, f"{p}_recensioni": rec_p, f"{p}_gap": round(g, 3)})
            gaps.append(g)
        riga["gap_medio"] = round(sum(gaps) / len(gaps), 3)
        righe.append(riga)

    righe.sort(key=lambda x: -x["gap_medio"])
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(righe[0].keys()) if righe else ["app"])
        w.writeheader()
        w.writerows(righe)

    os.makedirs("dati", exist_ok=True)
    with open(f"dati/appstore_{dt.date.today().isoformat()}.json", "w", encoding="utf-8") as f:
        json.dump({"pos": pos, "candidati": list(candidati)}, f)

    print(f"\nTop 25 opportunità (gap medio su {', '.join(p.upper() for p in paesi)}) → {a.out}")
    for r in righe[:25]:
        print(f"  {r['gap_medio']:.3f}  {r['app'][:45]:45}  {r['genere'] or '':18}  lingue: {r['lingue'][:30]}")


if __name__ == "__main__":
    main()
