"""258: quota di attività senza sito proprio a Firenze, per categoria (Google Places API, Text Search).

Uso: GOOGLE_PLACES_API_KEY=... python3 misura_places_258.py
Scrive risultati.json e raw_<categoria>.json nella cartella corrente.
"""
import json, os, re, sys, time, urllib.request
from urllib.parse import urlparse

KEY = os.environ["GOOGLE_PLACES_API_KEY"]
URL = "https://places.googleapis.com/v1/places:searchText"
MASK = "places.id,places.displayName,places.websiteUri,places.businessStatus,places.formattedAddress,places.primaryType,nextPageToken"
OUT = os.getcwd()

CATS = ["elettricista", "imbianchino", "fabbro", "giardiniere", "falegname",
        "centro estetico", "parrucchiere", "barbiere", "autofficina", "carrozzeria",
        "dentista", "psicologo", "nutrizionista", "osteopata", "palestra",
        "bed and breakfast", "fioraio", "pasticceria", "tatuatore", "fotografo"]

# Comune di Firenze, circa: lat 43.72-43.84, lng 11.15-11.34, in 2x2 zone
LAT = [43.72, 43.78, 43.84]
LNG = [11.15, 11.245, 11.34]
TILES = [((LAT[i], LNG[j]), (LAT[i + 1], LNG[j + 1])) for i in range(2) for j in range(2)]

NOT_OWN = ["facebook.", "fb.com", "instagram.", "linktr.ee", "linktree", "booking.", "tripadvisor.",
           "airbnb.", "wa.me", "whatsapp.", "tiktok.", "youtube.", "miodottore.", "dottori.it",
           "idoctors.", "paginegialle.", "paginebianche.", "prontopro.", "treatwell.", "uala.",
           "fresha.", "booksy.", "planity.", "houzz.", "instapro.", "habitissimo.", "starofservice.",
           "cylex", "misterimprese.", "virgilio.it", "tuttocitta.", "subito.it", "expedia.",
           "hotels.com", "linkedin.", "t.me", "g.page", "google.com", "goo.gl", "maps.app",
           "jameda", "psicologi-italia.", "guidapsicologi.", "dottorionline", "my-personaltrainer",
           "paginesi.", "infobel.", "yelp.", "kijiji", "trovaweb", "europages", "quandoo.", "thefork.",
           "doctolib.", "mynutritional.", "overplace.", "beb.it", "hotelsitalo."]


def call(body):
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), method="POST", headers={
        "Content-Type": "application/json", "X-Goog-Api-Key": KEY, "X-Goog-FieldMask": MASK})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.load(r)


def own_site(u):
    if not u:
        return False
    h = urlparse(u).netloc.lower() + urlparse(u).path.lower()[:30]
    return not any(d in h for d in NOT_OWN)


requests = 0
rows = {}
for cat in CATS:
    found = {}
    for lo, hi in TILES:
        body = {"textQuery": cat, "languageCode": "it", "regionCode": "IT", "pageSize": 20,
                "locationRestriction": {"rectangle": {"low": {"latitude": lo[0], "longitude": lo[1]},
                                                      "high": {"latitude": hi[0], "longitude": hi[1]}}}}
        for _ in range(3):
            d = call(body); requests += 1
            for p in d.get("places", []):
                found[p["id"]] = p
            tok = d.get("nextPageToken")
            if not tok:
                break
            body["pageToken"] = tok
            time.sleep(1.5)
    keep = [p for p in found.values()
            if p.get("businessStatus", "OPERATIONAL") == "OPERATIONAL"
            and re.search(r"\b501\d\d Firenze\b", p.get("formattedAddress", ""))]
    n = len(keep)
    no_site = sum(1 for p in keep if not p.get("websiteUri"))
    social = sum(1 for p in keep if p.get("websiteUri") and not own_site(p["websiteUri"]))
    rows[cat] = {"schede": n, "nessun_sito": no_site, "solo_social_portale": social,
                 "senza_sito_proprio": no_site + social,
                 "pct": round(100 * (no_site + social) / n, 1) if n else None,
                 "trovate_grezze": len(found)}
    print(cat, rows[cat], file=sys.stderr)
    with open(os.path.join(OUT, f"raw_{cat.replace(' ', '_')}.json"), "w") as f:
        json.dump(keep, f, ensure_ascii=False)

json.dump({"richieste": requests, "categorie": rows}, open(os.path.join(OUT, "risultati.json"), "w"),
          ensure_ascii=False, indent=1)
print("richieste API:", requests, file=sys.stderr)
