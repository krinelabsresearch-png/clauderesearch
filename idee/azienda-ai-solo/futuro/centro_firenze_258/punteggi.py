"""Beneficio e Propensione per le attività del centro di Firenze senza sito proprio."""
import json, math, os, re, unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone

OGGI = datetime(2026, 11, 11, tzinfo=timezone.utc)
P = json.load(open("centro_siti.json"))
EN = json.load(open("recensioni_en.json")) if os.path.exists("recensioni_en.json") else {}

PREVENTIVO = {"Architetti e interior designer", "Professionisti tecnici e legali", "Artigiani e riparazioni",
              "Tecnici e installatori", "Antiquari e gallerie d'arte", "Agenzie di traduzioni", "Agenzie di comunicazione e grafici",
              "Torte su ordinazione", "NCC e transfer", "Medici e specialisti privati", "Falegnami", "Traslochi e sgomberi", "Idraulici", "Imprese di pulizie", "Imprese edili",
              "Serramenti e arredo su misura", "Fotografi e videomaker", "Imbianchini", "Elettricisti", "Fabbri",
              "Location ed eventi, wedding planner", "Dentisti", "Avvocati, commercialisti", "Agenzie immobiliari",
              "Onoranze funebri", "Botteghe artigiane artistiche", "Giardinieri", "Carrozzerie"}
PIATTAFORMA_TIPICA = {"Medici e specialisti privati", "Gestione affitti brevi", "Deposito bagagli", "NCC e transfer",
                      "Garage e parcheggi", "B&B, affittacamere, case vacanza", "Hotel", "Ristoranti e trattorie", "Dentisti", "Psicologi",
                      "Nutrizionisti", "Osteopati", "Fisioterapisti", "Centri estetici e nail", "Parrucchieri",
                      "Barbieri", "Guide turistiche e tour", "Noleggi", "Pizzerie e asporto", "Veterinari"}
PORTALI_COMMISSIONE = ["booking.", "airbnb.", "miodottore.", "doctolib.", "treatwell.", "fresha.", "uala.", "booksy.",
                       "thefork.", "getyourguide.", "viator.", "expedia.", "justeat.", "deliveroo.", "glovo", "planity."]
CATENE = ["tecnocasa", "tempocasa", "gabetti", "remax", "re/max", "engel", "coldwell", "carrefour", "conad", "coop",
          "despar", "pam ", "eurospin", "lidl", "mcdonald", "burger king", "starbucks", "venchi", "grom", "rossopomodoro",
          "old wild west", "toni&guy", "jean louis david", "compagnia della bellezza", "yves rocher", "kiko", "sephora",
          "douglas", "dentalpro", "vitaldent", "caf ", "mail boxes", "unieuro", "tim ", "vodafone", "windtre", "feltrinelli",
          "mondadori", "zara", "h&m", "calzedonia", "intimissimi", "tezenis", "carpisa", "yamamay", "benetton", "salmoiraghi",
          "grandvision", "nh ", "hilton", "marriott", "starhotels", "b&b hotels", "best western", "accor", "ibis", "mercure",
          "anytime fitness", "virgin active", "mcfit", "fitactive", "poke house", "alice pizza", "spontini", "eataly",
          "rinascente", "europcar", "hertz", "avis", "sixt", "lime", "bird", "dott ", "tier", "mobike", "rentalcars",
          "giunti", "moleskine", "pandora", "swarovski", "lush", "ladurée", "lindt", "illy", "segafredo", "cioccolati italiani",
          "la feltrinelli", "kodak", "italiana immobiliare", "frimm", "toscano ", "grimaldi", "aw lab", "foot locker", "decathlon", "ovs", "upim", "coin", "bershka", "pull&bear", "uniqlo"]

PERSA = [r"non rispond", r"nessuna risposta", r"impossibile (contattar|parlare|prenotar)", r"difficile (contattar|trovar|prenotar)",
         r"non (sono riuscit|riesco|si riesce) a (contattar|parlar|prenotar|trovar)", r"orari? (sbagliat|non aggiornat|errat)",
         r"non (c'è|ce) un sito", r"senza sito", r"non hanno un sito", r"nessun sito", r"prezzi non (indicat|espost|chiar)",
         r"(no|don't|didn't|never) (answer|respond|reply)", r"(hard|difficult|impossible) to (reach|contact|book|find)",
         r"couldn'?t (reach|contact|book|find)", r"no website", r"(wrong|incorrect|outdated) (opening )?hours",
         r"(was|were) closed (when|despite|even though)", r"chiuso nonostante", r"trovato chiuso"]
PIENO = [r"sempre pien", r"prenotare con (largo|molto) anticipo", r"lista d'attesa", r"settimane di attesa",
         r"mesi di attesa", r"always (busy|full|packed)", r"book (weeks|well) in advance", r"long wait(ing)? list",
         r"fully booked", r"tutto esaurito"]


def norm(s):
    s = unicodedata.normalize("NFKD", s.lower())
    return re.sub(r"[^a-z0-9& ]", " ", "".join(c for c in s if not unicodedata.combining(c))).strip()


def km(a, b):
    return math.hypot((a[0] - b[0]) * 111.2, (a[1] - b[1]) * 111.2 * math.cos(math.radians(a[0])))


def ts(r):
    return datetime.fromisoformat(r["publishTime"].replace("Z", "+00:00")) if r.get("publishTime") else None


CAT_B = {"Ristoranti e trattorie": 45, "Pizzerie e asporto": 40, "Bar e caffè": 15, "Parrucchieri": 35, "Barbieri": 35,
         "Centri estetici e nail": 45, "Dentisti": 60, "Veterinari": 55, "Agenzie immobiliari": 50, "Hotel": 90,
         "B&B, affittacamere, case vacanza": 60, "Botteghe artigiane artistiche": 60, "Abbigliamento e boutique": 40,
         "Fiorai": 40, "Palestre, yoga, pilates": 55, "Gelaterie": 30, "Pasticcerie": 30, "Autofficine": 35,
         "Avvocati, commercialisti": 45, "Fotografi e videomaker": 80, "Tatuatori": 40, "Alimentari, macellerie, panifici": 15,
         "Negozi vari": 30, "Cantine ed enoteche": 70, "Negozi": 35, "Artigiani e riparazioni": 45,
         "Antiquari e gallerie d'arte": 60, "Agenzie di viaggi": 50, "Assicurazioni": 40, "Noleggi": 70,
         "Garage e parcheggi": 50, "Medici e specialisti privati": 60, "Farmacie e sanitarie": 30, "Servizi vari": 25,
         "Guide turistiche e tour": 65, "Ottici": 45}
TYPE_CAT = [("sandwich_shop", "Alimentari, macellerie, panifici"), ("tea_house", "Bar e caffè"),
            ("deli", "Alimentari, macellerie, panifici"), ("grocery_store", "Alimentari, macellerie, panifici"),
            ("supermarket", "Alimentari, macellerie, panifici"), ("bakery", "Alimentari, macellerie, panifici"),
            ("food_store", "Alimentari, macellerie, panifici"), ("massage", "Centri estetici e nail"),
            ("book_store", "Negozi"), ("shoe_store", "Negozi"), ("gift_shop", "Negozi"), ("toy_store", "Negozi"),
            ("home_goods_store", "Negozi"), ("tailor", "Artigiani e riparazioni"), ("art_gallery", "Antiquari e gallerie d'arte"),
            ("travel_agency", "Agenzie di viaggi"), ("tour_agency", "Guide turistiche e tour"),
            ("insurance_agency", "Assicurazioni"), ("car_rental", "Noleggi"), ("parking_garage", "Garage e parcheggi"),
            ("parking_lot", "Garage e parcheggi"), ("hostel", "B&B, affittacamere, case vacanza"),
            ("doctor", "Medici e specialisti privati"), ("pharmacy", "Farmacie e sanitarie"), ("laundry", "Servizi vari"),
            ("optician", "Ottici"), ("pizza_restaurant", "Pizzerie e asporto"), ("bistro", "Ristoranti e trattorie"), ("sporting_goods_store", "Negozi vari"), ("*_restaurant", "Ristoranti e trattorie"), ("restaurant", "Ristoranti e trattorie"),
            ("bar", "Bar e caffè"), ("*_bar", "Bar e caffè"), ("pub", "Bar e caffè"), ("night_club", "Bar e caffè"),
            ("cafe", "Bar e caffè"), ("coffee_shop", "Bar e caffè"), ("hair_salon", "Parrucchieri"), ("barber_shop", "Barbieri"),
            ("beauty_salon", "Centri estetici e nail"), ("nail_salon", "Centri estetici e nail"), ("spa", "Centri estetici e nail"),
            ("dentist", "Dentisti"), ("dental_clinic", "Dentisti"), ("veterinary_care", "Veterinari"),
            ("real_estate_agency", "Agenzie immobiliari"), ("hotel", "Hotel"), ("bed_and_breakfast", "B&B, affittacamere, case vacanza"),
            ("guest_house", "B&B, affittacamere, case vacanza"), ("jewelry_store", "Botteghe artigiane artistiche"),
            ("clothing_store", "Abbigliamento e boutique"), ("florist", "Fiorai"), ("gym", "Palestre, yoga, pilates"),
            ("fitness_center", "Palestre, yoga, pilates"), ("yoga_studio", "Palestre, yoga, pilates"), ("ice_cream_shop", "Gelaterie"),
            ("pastry_shop", "Pasticcerie"), ("car_repair", "Autofficine"), ("lawyer", "Avvocati, commercialisti"),
            ("accounting", "Avvocati, commercialisti"), ("photographer", "Fotografi e videomaker"), ("body_art_service", "Tatuatori"),
            ("electronics_store", "Negozi vari"), ("wine_store", "Cantine ed enoteche"), ("liquor_store", "Cantine ed enoteche")]
name_count = Counter(norm(p["displayName"]["text"]) for p in P)
for p in P:
    best = min(p["hits"], key=lambda h: h["rank"])
    p["cat"], p["B"] = best["cat"], best["B"]
    t = p.get("primaryType", "")
    for key, cat in TYPE_CAT:
        if t == key or (key.startswith("*") and t.endswith(key[1:])):
            p["cat"], p["B"] = cat, CAT_B[cat]; break
    p["ll"] = (p["location"]["latitude"], p["location"]["longitude"])
by_cat = defaultdict(list)
for p in P:
    by_cat[p["cat"]].append(p)

rows, excl = [], Counter()
for p in P:
    if p["site_kind"] == "proprio":
        continue
    name = p["displayName"]["text"]; n = norm(name)
    if p.get("businessStatus", "OPERATIONAL") != "OPERATIONAL":
        excl["chiusa"] += 1; continue
    if any(c.strip() and (n.startswith(c.strip()) or f" {c.strip()} " in f" {n} ") for c in CATENE) or name_count[n] >= 3:
        excl["catena"] += 1; continue
    revs = list(p.get("reviews", []))
    seen = {r.get("name") for r in revs}
    revs += [r for r in EN.get(p["id"], []) if r.get("name") not in seen]
    dates = [d for d in (ts(r) for r in revs) if d]
    newest, oldest = (max(dates), min(dates)) if dates else (None, None)
    if newest and (OGGI - newest).days > 548:
        excl["ferma da 18+ mesi"] += 1; continue

    text = " ".join((r.get("originalText") or r.get("text") or {}).get("text", "") for r in revs).lower()
    langs = [(r.get("originalText") or r.get("text") or {}).get("languageCode", "it") for r in revs]
    foreign = sum(1 for l in langs if not l.startswith("it")) / len(langs) if langs else 0
    persa_hits = [k for k in PERSA if re.search(k, text)]
    pieno_hits = [k for k in PIENO if re.search(k, text)]
    neigh = [q for q in by_cat[p["cat"]] if q is not p and km(q["ll"], p["ll"]) <= 0.5]
    share = sum(1 for q in neigh if q["site_kind"] == "proprio") / len(neigh) if neigh else 0
    conc = 15 * share * min(1, len(neigh) / 3)
    price = p.get("priceLevel", "")
    if price in ("PRICE_LEVEL_EXPENSIVE", "PRICE_LEVEL_VERY_EXPENSIVE"): val = 10
    elif price == "PRICE_LEVEL_MODERATE": val = 6
    elif price == "PRICE_LEVEL_INEXPENSIVE": val = 2
    else: val = 8 if p["cat"] in PREVENTIVO else 4
    w = (p.get("websiteUri") or "").lower()
    comm = 10 if any(s in w for s in PORTALI_COMMISSIONE) else (4 if p["cat"] in PIATTAFORMA_TIPICA else 0)
    rt, rc = p.get("rating") or 0, p.get("userRatingCount") or 0
    rep = 10 if (rt >= 4.3 and rc >= 30) else (5 if (rt >= 4.0 and rc >= 10) else 0)
    ben = {"categoria": round(25 * min(p["B"], 90) / 90, 1),
           "domanda_persa": 15 if len(persa_hits) >= 2 else (8 if persa_hits else 0),
           "concorrenti_con_sito": round(conc, 1), "stranieri": round(10 * foreign, 1), "valore": val,
           "commissioni": comm, "reputazione": rep, "gia_pieno": -10 if (pieno_hits or rc >= 1000) else 0}
    beneficio = max(0, sum(ben.values()))

    hours = 8 if p.get("regularOpeningHours", {}).get("weekdayDescriptions") else 0
    photos = p.get("photos", [])
    ph = 7 if len(photos) >= 10 else round(7 * len(photos) / 10)
    ntok = {t for t in n.split() if len(t) > 3}
    own_ph = any(ntok & {t for t in norm(a.get("displayName", "")).split() if len(t) > 3}
                 for x in photos for a in x.get("authorAttributions", []))
    curata = hours + ph + (10 if own_ph else 0)
    if len(dates) >= 3 and (OGGI - oldest).days <= 548 and rc <= 100: nuova = 20
    elif newest and rc <= 40 and (OGGI - newest).days <= 180: nuova = 10
    else: nuova = 0
    social = 20 if p["site_kind"] == "social" else (10 if p["site_kind"] == "portale" else 0)
    tel = (p.get("nationalPhoneNumber") or "").replace(" ", "")
    if name_count[n] == 2: dim = 15
    else: dim = (7 if tel.startswith("0") else (3 if tel.startswith("3") else 0)) + (8 if rc >= 50 else (4 if rc >= 15 else 0))
    pro = {"scheda_curata": curata, "aperta_da_poco": nuova, "social_o_portale": social, "sito_rotto": 0, "dimensione": dim}
    propensione = sum(pro.values())
    rows.append({"id": p["id"], "nome": name, "cat": p["cat"], "B": p["B"], "indirizzo": p.get("formattedAddress", ""),
                 "dist_km": p["dist_km"], "sito": p["site_kind"], "url": p.get("websiteUri", ""), "tel": tel,
                 "voto": rt, "recensioni": rc, "prezzo": price.replace("PRICE_LEVEL_", ""), "vicini": len(neigh),
                 "quota_vicini_con_sito": round(share, 2), "lingue": langs, "persa": persa_hits, "pieno": pieno_hits,
                 "foto": len(photos), "foto_titolare": own_ph, "rec_piu_vecchia": oldest.date().isoformat() if oldest else None,
                 "rec_piu_recente": newest.date().isoformat() if newest else None, "details_letti": p.get("details_letti", True), "ben": ben, "beneficio": beneficio,
                 "pro": pro, "propensione": propensione, "score": round(beneficio * propensione / 100, 1),
                 "maps": p.get("googleMapsUri", ""), "reviews": revs, "types": p.get("types", [])})

rows.sort(key=lambda r: -r["score"])
json.dump(rows, open("candidati.json", "w"), ensure_ascii=False)
print("candidati:", len(rows), "esclusi:", dict(excl))
for i, r in enumerate(rows[:0], 1):
    print(i, r["score"], r["beneficio"], r["propensione"], r["cat"], "|", r["nome"], "|", r["sito"], r["recensioni"], r["voto"], r["dist_km"])
