"""Unisce la seconda raccolta alla prima, assegna categoria e B ai nuovi termini e legge recensioni e foto
(Place Details) solo per le nuove schede nel raggio che non hanno un sito proprio. Scrive centro_siti.json aggiornato."""
import json, os, sys, time, urllib.request, urllib.error, concurrent.futures as cf
sys.path.insert(0, os.getcwd())
from siti_lib import kind, km, DUOMO, MAX_KM

KEY = os.environ["GOOGLE_PLACES_API_KEY"]
CAP = int(os.environ.get("CAP_DETAILS", "600"))

G = {  # gruppo -> (categoria, B, termini)
    "ott": ("Ottici", 45, ["ottico", "negozio di occhiali da sole"]),
    "art": ("Artigiani e riparazioni", 45, ["calzolaio", "riparazioni sartoriali", "tappezziere", "vetraio", "legatoria",
            "corniciaio", "orologiaio", "liuteria", "restauratore", "doratore", "duplicazione chiavi", "sartoria"]),
    "bot": ("Botteghe artigiane artistiche", 60, ["orafo", "argentiere", "carta marmorizzata", "scultore", "pittore artista",
            "negozio di ceramiche", "bottega del cuoio", "sartoria su misura", "camiceria", "cappelleria", "guanti", "cravatte",
            "negozio di cappelli"]),
    "neg": ("Negozi", 35, ["libreria", "cartoleria", "profumeria", "erboristeria", "negozio di scarpe", "negozio di borse",
            "negozio di intimo", "negozio di giocattoli", "articoli per la casa", "ferramenta", "negozio di biciclette",
            "negozio di computer", "negozio di dischi", "strumenti musicali", "negozio di tessuti", "merceria",
            "negozio di souvenir", "tabaccheria", "negozio di cosmetici", "negozio vintage", "mercatino dell'usato",
            "bigiotteria", "cartoleria artistica", "profumeria artistica"]),
    "ant": ("Antiquari e gallerie d'arte", 60, ["antiquario", "galleria d'arte"]),
    "far": ("Farmacie e sanitarie", 30, ["farmacia", "sanitaria ortopedia"]),
    "ali": ("Alimentari, macellerie, panifici", 15, ["gastronomia", "salumeria", "pescheria", "fruttivendolo",
            "negozio biologico", "rosticceria", "panetteria"]),
    "gus": ("Botteghe del gusto (cioccolato, caffè, olio, vino)", 40, ["cioccolateria", "torrefazione caffè",
            "olio extravergine", "negozio di vini"]),
    "ris": ("Ristoranti e trattorie", 45, ["sushi", "ristorante etnico"]),
    "bar": ("Bar e caffè", 15, ["pub", "cocktail bar", "wine bar", "discoteca"]),
    "pro": ("Professionisti tecnici e legali", 45, ["notaio", "geometra", "ingegnere", "consulente del lavoro"]),
    "arc": ("Architetti e interior designer", 65, ["architetto"]),
    "via": ("Agenzie di viaggi", 50, ["agenzia di viaggi"]),
    "tra": ("Agenzie di traduzioni", 55, ["agenzia di traduzioni"]),
    "com": ("Agenzie di comunicazione e grafici", 60, ["agenzia di comunicazione", "studio grafico"]),
    "ass": ("Assicurazioni", 40, ["assicurazioni"]),
    "med": ("Medici e specialisti privati", 60, ["studio medico", "ginecologo", "dermatologo", "oculista", "pediatra",
            "logopedista", "podologo"]),
    "lab": ("Laboratori e centri diagnostici", 50, ["laboratorio analisi", "centro diagnostico"]),
    "est": ("Centri estetici e nail", 45, ["massaggi", "centro benessere spa", "extension ciglia", "trucco permanente",
            "solarium", "epilazione laser"]),
    "scu": ("Scuole guida, di lingue, corsi", 55, ["scuola di danza", "scuola di musica", "ripetizioni doposcuola",
            "asilo nido", "scuola d'arte", "corsi di pittura"]),
    "esp": ("Guide turistiche e tour", 65, ["corso di cucina", "tour in bici", "degustazione vino", "escape room"]),
    "ani": ("Animali (pet shop, toelettatura)", 35, ["pet shop", "toelettatura"]),
    "ric": ("B&B, affittacamere, case vacanza", 60, ["ostello", "casa vacanze", "residence"]),
    "aff": ("Gestione affitti brevi", 55, ["gestione affitti brevi"]),
    "nol": ("Noleggi", 70, ["noleggio auto"]),
    "ncc": ("NCC e transfer", 70, ["NCC transfer"]),
    "cow": ("Coworking e studi di registrazione", 55, ["coworking", "studio di registrazione"]),
    "sta": ("Copisterie e tipografie", 35, ["copisteria", "tipografia", "stampa digitale"]),
    "tec": ("Tecnici e installatori", 45, ["riparazione elettrodomestici", "condizionatori", "antennista",
            "riparazione biciclette"]),
    "sgo": ("Traslochi e sgomberi", 55, ["sgombero cantine"]),
    "dep": ("Deposito bagagli", 60, ["deposito bagagli"]),
    "ser": ("Servizi vari", 25, ["spedizioni", "lavaggio auto", "compro oro", "money transfer", "internet point",
            "riparazione cellulari", "lavanderia", "tintoria"]),
    "par": ("Garage e parcheggi", 50, ["garage parcheggio"]),
    "fot": ("Fotografi e videomaker", 80, ["fotografo matrimoni", "videomaker"]),
    "eve": ("Location ed eventi, wedding planner", 85, ["wedding planner", "catering", "noleggio attrezzature eventi",
            "dj per eventi", "agenzia hostess eventi"]),
    "fio": ("Fiorai", 40, ["fiorista eventi"]),
    "tor": ("Torte su ordinazione", 55, ["pasticceria su ordinazione", "torte personalizzate"]),
    "spo": ("Palestre, yoga, pilates", 55, ["personal trainer", "pilates", "yoga", "arti marziali", "piscina",
            "centro sportivo"]),
    "tat": ("Tatuatori", 40, ["tatuaggi piercing"]),
}
TERM = {t: (c, b) for c, b, ts in G.values() for t in ts}
OLD = json.load(open("centro_raw.json"))
OLD_TERM = {h["term"]: (h["cat"], h["B"]) for p in OLD for h in p["hits"]}
TERM.update(OLD_TERM)

old = {p["id"]: p for p in json.load(open("centro_siti.json"))}
new_raw = json.load(open("centro_raw2.json"))
added, todo = 0, []
for p in new_raw:
    hits = [{"term": t, "cat": TERM[t][0], "B": TERM[t][1], "rank": 999} for t in p["terms"] if t in TERM]
    if p["id"] in old:
        old[p["id"]]["hits"] += hits; continue
    if "location" not in p or not hits:
        continue
    d = km((p["location"]["latitude"], p["location"]["longitude"]), DUOMO)
    if d > MAX_KM:
        continue
    p["hits"] = hits; p["dist_km"] = round(d, 2); p["site_kind"] = kind(p.get("websiteUri"))
    old[p["id"]] = p; added += 1
    if p["site_kind"] != "proprio" and p.get("businessStatus", "OPERATIONAL") == "OPERATIONAL":
        todo.append(p)
todo.sort(key=lambda p: -max(h["B"] for h in p["hits"]))
print("nuove nel raggio:", added, "senza sito proprio da leggere:", len(todo), "cap:", CAP, file=sys.stderr)


def det(pid):
    for i in range(4):
        try:
            req = urllib.request.Request(f"https://places.googleapis.com/v1/places/{pid}",
                headers={"X-Goog-Api-Key": KEY, "X-Goog-FieldMask": "id,reviews,photos"})
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.load(r)
        except urllib.error.HTTPError as e:
            if e.code < 500:
                return {}
            time.sleep(2 ** i)
    return {}


with cf.ThreadPoolExecutor(8) as ex:
    for p, d in zip(todo[:CAP], ex.map(lambda q: det(q["id"]), todo[:CAP])):
        p["reviews"] = d.get("reviews", []); p["photos"] = d.get("photos", []); p["details_letti"] = True
for p in todo[CAP:]:
    p["details_letti"] = False
json.dump(list(old.values()), open("centro_siti.json", "w"), ensure_ascii=False)
print("letti:", min(CAP, len(todo)), "non letti per tetto:", max(0, len(todo) - CAP), "totale schede:", len(old), file=sys.stderr)
