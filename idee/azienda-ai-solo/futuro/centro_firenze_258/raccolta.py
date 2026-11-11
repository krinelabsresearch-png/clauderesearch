"""Raccoglie le schede Google Places del centro di Firenze per tutte le categorie (con recensioni e foto)."""
import json, os, sys, time, urllib.request, urllib.error

KEY = os.environ["GOOGLE_PLACES_API_KEY"]
URL = "https://places.googleapis.com/v1/places:searchText"
MASK = ",".join("places." + f for f in [
    "id", "displayName", "formattedAddress", "location", "websiteUri", "businessStatus", "primaryType",
    "types", "rating", "userRatingCount", "priceLevel", "regularOpeningHours.weekdayDescriptions",
    "nationalPhoneNumber", "photos", "reviews", "googleMapsUri"]) + ",nextPageToken"
OUT = os.getcwd()

# termine di ricerca -> (categoria della classifica, B)
TERMS = {
    "falegname": ("Falegnami", 65), "traslochi": ("Traslochi e sgomberi", 55), "idraulico": ("Idraulici", 45),
    "impresa di pulizie": ("Imprese di pulizie", 50), "nutrizionista": ("Nutrizionisti", 55),
    "noleggio bici": ("Noleggi", 70), "noleggio scooter": ("Noleggi", 70), "impresa edile": ("Imprese edili", 65),
    "osteopata": ("Osteopati", 55), "barbiere": ("Barbieri", 35), "parrucchiere": ("Parrucchieri", 35),
    "serramenti": ("Serramenti e arredo su misura", 65), "dentista": ("Dentisti", 60),
    "fotografo": ("Fotografi e videomaker", 80), "imbianchino": ("Imbianchini", 40),
    "fisioterapista": ("Fisioterapisti", 55), "elettricista": ("Elettricisti", 45), "tatuatore": ("Tatuatori", 40),
    "centro estetico": ("Centri estetici e nail", 45), "nail bar": ("Centri estetici e nail", 45),
    "pizzeria": ("Pizzerie e asporto", 40), "boutique abbigliamento": ("Abbigliamento e boutique", 40),
    "wedding planner": ("Location ed eventi, wedding planner", 85), "location eventi": ("Location ed eventi, wedding planner", 85),
    "avvocato": ("Avvocati, commercialisti", 45), "commercialista": ("Avvocati, commercialisti", 45),
    "scuola di lingue": ("Scuole guida, di lingue, corsi", 55), "autoscuola": ("Scuole guida, di lingue, corsi", 55),
    "bar caffè": ("Bar e caffè", 15), "alimentari": ("Alimentari, macellerie, panifici", 15),
    "macelleria": ("Alimentari, macellerie, panifici", 15), "panificio": ("Alimentari, macellerie, panifici", 15),
    "agenzia immobiliare": ("Agenzie immobiliari", 50), "hotel": ("Hotel", 90),
    "guida turistica": ("Guide turistiche e tour", 65), "pelletteria artigianale": ("Botteghe artigiane artistiche", 60),
    "gioielleria artigianale": ("Botteghe artigiane artistiche", 60), "restauro mobili": ("Botteghe artigiane artistiche", 60),
    "bottega artigiana": ("Botteghe artigiane artistiche", 60), "ceramica artigianale": ("Botteghe artigiane artistiche", 60),
    "ristorante": ("Ristoranti e trattorie", 45), "trattoria": ("Ristoranti e trattorie", 45),
    "bed and breakfast": ("B&B, affittacamere, case vacanza", 60), "affittacamere": ("B&B, affittacamere, case vacanza", 60),
    "fioraio": ("Fiorai", 40), "autofficina": ("Autofficine", 35), "carrozzeria": ("Carrozzerie", 35),
    "gommista": ("Gommisti", 35), "pasticceria": ("Pasticcerie", 30), "gelateria": ("Gelaterie", 30),
    "palestra": ("Palestre, yoga, pilates", 55), "yoga pilates": ("Palestre, yoga, pilates", 55),
    "psicologo": ("Psicologi", 55), "fabbro": ("Fabbri", 45), "giardiniere": ("Giardinieri", 35),
    "onoranze funebri": ("Onoranze funebri", 50), "veterinario": ("Veterinari", 55),
    "concessionario auto": ("Concessionari e auto usate", 55), "enoteca vendita vino": ("Cantine ed enoteche", 70),
}

RECT = {"low": {"latitude": 43.760, "longitude": 11.236}, "high": {"latitude": 43.786, "longitude": 11.274}}


def call(body):
    req = urllib.request.Request(URL, data=json.dumps(body).encode(), method="POST", headers={
        "Content-Type": "application/json", "X-Goog-Api-Key": KEY, "X-Goog-FieldMask": MASK})
    for i in range(5):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code < 500 or i == 4:
                raise
            time.sleep(2 ** (i + 1))


calls, places = 0, {}
for term, (cat, b) in TERMS.items():
    body = {"textQuery": term, "languageCode": "it", "regionCode": "IT", "pageSize": 20,
            "locationRestriction": {"rectangle": RECT}}
    rank = 0
    for _ in range(3):
        d = call(body); calls += 1
        for p in d.get("places", []):
            rank += 1
            hit = {"term": term, "cat": cat, "B": b, "rank": rank}
            if p["id"] in places:
                places[p["id"]]["hits"].append(hit)
            else:
                p["hits"] = [hit]; places[p["id"]] = p
        tok = d.get("nextPageToken")
        if not tok:
            break
        body["pageToken"] = tok
        time.sleep(1.5)
    print(term, rank, file=sys.stderr)

json.dump(list(places.values()), open(os.path.join(OUT, "centro_raw.json"), "w"), ensure_ascii=False)
print("chiamate:", calls, "schede uniche:", len(places), file=sys.stderr)
