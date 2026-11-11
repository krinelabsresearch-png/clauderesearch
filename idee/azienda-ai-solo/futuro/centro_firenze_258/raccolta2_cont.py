"""Seconda raccolta: tutte le attività del centro, con riquadri ricorsivi quando una ricerca satura (60 risultati).
Passata leggera: niente recensioni né foto (quelle si leggono dopo, solo per chi non ha un sito proprio)."""
import json, os, sys, time, urllib.request, urllib.error

KEY = os.environ["GOOGLE_PLACES_API_KEY"]
URL = "https://places.googleapis.com/v1/places:searchText"
MASK = ",".join("places." + f for f in ["id", "displayName", "formattedAddress", "location", "websiteUri",
    "businessStatus", "primaryType", "types", "rating", "userRatingCount", "priceLevel",
    "regularOpeningHours.weekdayDescriptions", "nationalPhoneNumber", "googleMapsUri"]) + ",nextPageToken"
BUDGET = int(os.environ.get("BUDGET", "700"))
RECT = ((43.760, 11.236), (43.786, 11.274))

OLD_SATURATED = ['nutrizionista', 'osteopata', 'fisioterapista', 'palestra', 'barbiere', 'parrucchiere', 'centro estetico',
    'dentista', 'fotografo', 'pizzeria', 'trattoria', 'ristorante', 'alimentari', 'panificio', 'boutique abbigliamento',
    'pelletteria artigianale', 'location eventi', 'avvocato', 'commercialista', 'scuola di lingue', 'bar caffè',
    'pasticceria', 'agenzia immobiliare', 'hotel', 'gioielleria artigianale', 'bed and breakfast', 'affittacamere',
    'gelateria', 'psicologo']
NEW = ["ottico", "calzolaio", "sartoria", "lavanderia", "tintoria", "libreria", "cartoleria", "copisteria", "tipografia",
    "antiquario", "galleria d'arte", "corniciaio", "orologiaio", "orafo", "argentiere", "profumeria", "erboristeria",
    "farmacia", "sanitaria ortopedia", "negozio di scarpe", "negozio di borse", "cappelleria", "negozio di intimo",
    "negozio di giocattoli", "articoli per la casa", "ferramenta", "negozio di biciclette", "riparazione biciclette",
    "riparazione cellulari", "negozio di computer", "negozio di dischi", "strumenti musicali", "liuteria",
    "negozio di tessuti", "merceria", "tappezziere", "vetraio", "legatoria", "carta marmorizzata", "negozio di souvenir",
    "tabaccheria", "gastronomia", "salumeria", "pescheria", "fruttivendolo", "negozio biologico", "cioccolateria",
    "torrefazione caffè", "rosticceria", "sushi", "ristorante etnico", "pub", "cocktail bar", "wine bar", "discoteca",
    "notaio", "architetto", "geometra", "ingegnere", "consulente del lavoro", "agenzia di viaggi", "agenzia di traduzioni",
    "agenzia di comunicazione", "studio grafico", "assicurazioni", "studio medico", "ginecologo", "dermatologo", "oculista",
    "pediatra", "logopedista", "podologo", "massaggi", "centro benessere spa", "scuola di danza", "scuola di musica",
    "corso di cucina", "ripetizioni doposcuola", "asilo nido", "pet shop", "toelettatura", "ostello", "casa vacanze",
    "residence", "gestione affitti brevi", "noleggio auto", "NCC transfer", "tour in bici", "degustazione vino",
    "escape room", "coworking", "studio di registrazione", "laboratorio analisi", "centro diagnostico",
    "stampa digitale", "duplicazione chiavi", "riparazione elettrodomestici", "condizionatori", "antennista",
    "sgombero cantine", "deposito bagagli", "spedizioni", "lavaggio auto", "garage parcheggio", "negozio vintage",
    "mercatino dell'usato", "compro oro", "money transfer", "internet point", "extension ciglia", "trucco permanente",
    "solarium", "epilazione laser", "tatuaggi piercing", "negozio di cosmetici", "negozio di occhiali da sole",
    "negozio di ceramiche", "bottega del cuoio", "scuola d'arte", "corsi di pittura", "fotografo matrimoni",
    "videomaker", "wedding planner", "catering", "pasticceria su ordinazione", "torte personalizzate", "fiorista eventi",
    "agenzia hostess eventi", "noleggio attrezzature eventi", "dj per eventi", "personal trainer", "pilates", "yoga",
    "arti marziali", "piscina", "centro sportivo", "sartoria su misura", "camiceria", "riparazioni sartoriali",
    "restauratore", "doratore", "scultore", "pittore artista", "bigiotteria", "negozio di cappelli", "guanti",
    "cravatte", "profumeria artistica", "cartoleria artistica", "negozio di vini", "olio extravergine", "panetteria"]


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


calls = 0
places = {}
saturated_tiles = []
DONE = set()
if os.environ.get("CONTINUA") and os.path.exists("centro_raw2.json"):
    for p in json.load(open("centro_raw2.json")):
        places[p["id"]] = p
    DONE = set(json.load(open("termini_fatti2.json")))


def quads(rect):
    (la0, lo0), (la1, lo1) = rect
    ma, mo = (la0 + la1) / 2, (lo0 + lo1) / 2
    return [((la0, lo0), (ma, mo)), ((la0, mo), (ma, lo1)), ((ma, lo0), (la1, mo)), ((ma, mo), (la1, lo1))]


def search(term, rect, depth):
    """Ricerca su un riquadro; se satura e la profondità lo consente, divide in 4."""
    global calls
    (la0, lo0), (la1, lo1) = rect
    body = {"textQuery": term, "languageCode": "it", "regionCode": "IT", "pageSize": 20,
            "locationRestriction": {"rectangle": {"low": {"latitude": la0, "longitude": lo0},
                                                  "high": {"latitude": la1, "longitude": lo1}}}}
    n = 0
    for _ in range(3):
        if calls >= BUDGET:
            return n
        d = call(body); calls += 1
        for p in d.get("places", []):
            n += 1
            if p["id"] in places:
                places[p["id"]]["terms"].append(term)
            else:
                p["terms"] = [term]; places[p["id"]] = p
        tok = d.get("nextPageToken")
        if not tok:
            break
        body["pageToken"] = tok
        time.sleep(1.2)
    if n >= 60:
        if depth < 2:
            for sub in quads(rect):
                search(term, sub, depth + 1)
        else:
            saturated_tiles.append((term, rect))
    return n


done_now = []
import importlib.util
B_OF = {}
try:
    spec = importlib.util.spec_from_file_location("u", "termini_b.json")
except Exception:
    pass
if os.path.exists("termini_b.json"):
    B_OF = json.load(open("termini_b.json"))
if os.environ.get("CONTINUA"):
    NEW = sorted([t for t in NEW if t not in DONE], key=lambda t: -B_OF.get(t, 0))
    OLD_SATURATED = sorted([t for t in OLD_SATURATED if t not in DONE], key=lambda t: -B_OF.get(t, 0))
    # le categorie vecchie sature con B alto vengono prima dei nuovi termini a B basso
    ORDER = sorted([("new", t) for t in NEW] + [("old", t) for t in OLD_SATURATED], key=lambda x: -B_OF.get(x[1], 0))
else:
    ORDER = [("new", t) for t in NEW] + [("old", t) for t in OLD_SATURATED]
for kind_, term in ORDER:
    if calls >= BUDGET:
        break
    start = calls
    if kind_ == "new":
        search(term, RECT, 0)
    else:
        for q in quads(RECT):
            search(term, q, 1)
    if calls < BUDGET:
        done_now.append(term)
    print(term, calls, len(places), file=sys.stderr)
NEW = []
OLD_SATURATED = []
for term in NEW:
    search(term, RECT, 0)
    print(term, calls, len(places), file=sys.stderr)
    if calls >= BUDGET:
        break
for term in OLD_SATURATED:            # già fatte sull'intero rettangolo: si riparte dai 4 riquadri
    for q in quads(RECT):
        search(term, q, 1)
    print(term, calls, len(places), file=sys.stderr)
    if calls >= BUDGET:
        break

json.dump(list(places.values()), open("centro_raw2.json", "w"), ensure_ascii=False)
json.dump(saturated_tiles, open("saturi2.json", "a"))
json.dump(sorted(DONE | set(done_now)), open("termini_fatti2.json", "w"))
print("chiamate:", calls, "schede:", len(places), "riquadri ancora saturi:", len(saturated_tiles), file=sys.stderr)
