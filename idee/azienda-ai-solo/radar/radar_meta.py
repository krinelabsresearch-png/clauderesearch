"""Radar sulla libreria pubblicitaria Meta: chi sta spingendo di più in UE, e chi cresce.

Solo per le inserzioni consegnate in UE Meta espone tutte le inserzioni commerciali con la copertura
(eu_total_reach), per via del Digital Services Act. Serve un token: vedi ISTRUZIONI.md.
Esecuzione:  export META_TOKEN=...
             python3 radar_meta.py --paesi IT,ES,DE,FR --termini "AI,intelligenza artificiale,app"
Ogni esecuzione salva un'istantanea in dati/; dalla seconda in poi calcola la crescita per pagina.
"""

import argparse
import csv
import datetime as dt
import glob
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

CAMPI = ("id,page_id,page_name,ad_creation_time,ad_delivery_start_time,ad_creative_bodies,"
         "ad_creative_link_titles,ad_snapshot_url,eu_total_reach,languages,publisher_platforms")


def chiama(url):
    try:
        with urllib.request.urlopen(url, timeout=60) as r:
            return json.loads(r.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        corpo = e.read().decode("utf-8", "replace")
        sys.exit(f"Errore Meta {e.code}: {corpo[:500]}\n(Se parla di identità o permessi: vedi ISTRUZIONI.md)")


def scarica(token, versione, paese, termine, max_pagine):
    params = {
        "access_token": token, "ad_type": "ALL", "ad_active_status": "ACTIVE",
        "ad_reached_countries": json.dumps([paese]), "search_terms": termine,
        "fields": CAMPI, "limit": 250,
    }
    url = f"https://graph.facebook.com/{versione}/ads_archive?" + urllib.parse.urlencode(params)
    for _ in range(max_pagine):
        dati = chiama(url)
        for ad in dati.get("data", []):
            ad["_paese"], ad["_termine"] = paese, termine
            yield ad
        url = dati.get("paging", {}).get("next")
        if not url:
            break
        time.sleep(1.5)  # ritmo lento: niente raffiche di richieste


def per_pagina(ads):
    """Aggrega per inserzionista: numero di inserzioni attive e copertura UE totale."""
    agg = {}
    for ad in ads:
        k = ad.get("page_name") or ad.get("page_id")
        a = agg.setdefault(k, {"pagina": k, "inserzioni": 0, "copertura": 0, "paesi": set(),
                               "prima_inserzione": ad.get("ad_delivery_start_time", ""), "esempio": ""})
        a["inserzioni"] += 1
        a["copertura"] += int(ad.get("eu_total_reach") or 0)
        a["paesi"].add(ad["_paese"])
        inizio = ad.get("ad_delivery_start_time", "")
        if inizio and inizio < a["prima_inserzione"]:
            a["prima_inserzione"] = inizio
        if not a["esempio"]:
            a["esempio"] = (ad.get("ad_creative_link_titles") or ad.get("ad_creative_bodies") or [""])[0][:120]
    return agg


def crescita(oggi, ieri):
    """Variazione di copertura e numero di inserzioni rispetto all'istantanea precedente."""
    righe = []
    for k, a in oggi.items():
        prima = ieri.get(k, {"copertura": 0, "inserzioni": 0})
        righe.append({**a, "paesi": ",".join(sorted(a["paesi"])),
                      "delta_copertura": a["copertura"] - prima["copertura"],
                      "delta_inserzioni": a["inserzioni"] - prima["inserzioni"],
                      "nuovo": k not in ieri})
    return sorted(righe, key=lambda r: (-r["delta_copertura"], -r["copertura"]))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--paesi", default="IT,ES,DE,FR")
    ap.add_argument("--termini", default="AI,intelligenza artificiale,app")
    ap.add_argument("--versione", default="v21.0")
    ap.add_argument("--max-pagine", type=int, default=20)
    ap.add_argument("--out", default="radar_meta.csv")
    a = ap.parse_args()
    token = os.environ.get("META_TOKEN") or sys.exit("Manca META_TOKEN: vedi ISTRUZIONI.md")

    ads = []
    for paese in [p.strip().upper() for p in a.paesi.split(",")]:
        for termine in [t.strip() for t in a.termini.split(",")]:
            n = len(ads)
            ads.extend(scarica(token, a.versione, paese, termine, a.max_pagine))
            print(f"{paese} · '{termine}': {len(ads) - n} inserzioni attive")

    os.makedirs("dati", exist_ok=True)
    oggi_file = f"dati/meta_{dt.date.today().isoformat()}.jsonl"
    with open(oggi_file, "w", encoding="utf-8") as f:
        for ad in ads:
            f.write(json.dumps(ad, ensure_ascii=False) + "\n")

    precedenti = sorted(p for p in glob.glob("dati/meta_*.jsonl") if p != oggi_file)
    ieri = {}
    if precedenti:
        with open(precedenti[-1], encoding="utf-8") as f:
            ieri = per_pagina(json.loads(r) for r in f)
        print(f"Confronto con {precedenti[-1]}")

    righe = crescita(per_pagina(ads), ieri)
    with open(a.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(righe[0].keys()) if righe else ["pagina"])
        w.writeheader()
        w.writerows(righe)
    print(f"\nTop 25 inserzionisti per crescita della copertura → {a.out}")
    for r in righe[:25]:
        print(f"  {r['delta_copertura']:>10,}  {str(r['pagina'])[:40]:40} {r['inserzioni']:>4} ins.  {r['esempio'][:60]}")


if __name__ == "__main__":
    main()
