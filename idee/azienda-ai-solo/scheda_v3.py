"""Scheda v3 (6/11/2026), decisa con Lorenzo dopo il "gioco inverso" su 107, 116 e 260.

Cambi rispetto alla v2:
- obiettivo 300–500 k€ l'anno al posto del milione ("obiettivo"); di default vale solo1M + 1 (massimo 5);
- ammessi B2B con un po' di vendita e nicchie regolamentate;
- la motivazione conta solo se l'ha indicata Lorenzo; altrimenti esce dal calcolo e gli altri pesi si ripesano;
- la difendibilità si divide in "conc" (difesa dai concorrenti, il vecchio "dif") e "diy" (difesa dal cliente
  che si arrangia con l'AI: 1 = gli basta un progetto Claude, 5 = impossibile da solo);
- soglie: se dolore, diy, conc o obiettivo è sotto 3 l'idea è scartata;
- chi passa le soglie riceve una media geometrica pesata, così un voto basso non si compensa.
Esecuzione: python3 scheda_v3.py
"""
import importlib.util
import math
import re
from pathlib import Path

QUI = Path(__file__).resolve().parent

PESI = {"mot": .15, "vant": .15, "dolore": .10, "mercato": .05, "margine": .10, "valid": .05,
        "obiettivo": .15, "autom": .10, "conc": .05, "diy": .10}
assert abs(sum(PESI.values()) - 1) < 1e-9
SOGLIE = ("dolore", "diy", "conc", "obiettivo")

# Motivazione indicata da Lorenzo: 072–081 (dai suoi commenti) e 5 per 092, 093, 096, 109.
MOT_LORENZO = {f"{n:03d}" for n in range(72, 82)} | {"092", "093", "096", "109"}

# Voti dei round rapidi 198–217 (verifiche dei workflow del 14/10/2026); 208 è in futuro/punteggi.py.
RAPIDI = {
    "198 CERTO: dimostratore matematico per modelli finanziari Excel": dict(mot=5, vant=4, dolore=3, mercato=2, margine=5, valid=3, solo1M=3, autom=3, dif=4),
    "199 Momenti 4D: bullet-time del bacio degli sposi":               dict(mot=4, vant=4, dolore=3, mercato=4, margine=4, valid=4, solo1M=3, autom=4, dif=3),
    "200 PEPTICA: peptidi cosmetici progettati con l'AI":              dict(mot=5, vant=4, dolore=3, mercato=3, margine=5, valid=3, solo1M=2, autom=3, dif=4),
    "201 Gioiello parlato: descrivi l'anello, lo ricevi stampato":     dict(mot=4, vant=4, dolore=3, mercato=4, margine=3, valid=4, solo1M=3, autom=2, dif=3),
    "202 Genius Loci: il profumo di un luogo italiano":                dict(mot=4, vant=4, dolore=2, mercato=3, margine=4, valid=4, solo1M=3, autom=3, dif=2),
    "203 TailBuyer: buyer AI che negozia per le PMI":                  dict(mot=3, vant=3, dolore=3, mercato=4, margine=4, valid=4, solo1M=2, autom=3, dif=2),
    "204 MEDITERRA SIGNAL: stime anticipate dei raccolti":             dict(mot=4, vant=3, dolore=3, mercato=2, margine=5, valid=3, solo1M=2, autom=4, dif=2),
    "205 PianoFabbrica: pianificatore di produzione per PMI":          dict(mot=4, vant=4, dolore=4, mercato=4, margine=4, valid=4, solo1M=3, autom=2, dif=3),
    "206 La voce della fondatrice: consulente beauty in video":        dict(mot=4, vant=4, dolore=3, mercato=3, margine=2, valid=3, solo1M=2, autom=3, dif=2),
    "207 First Dance AI: la vostra canzone, i vostri passi":           dict(mot=3, vant=3, dolore=3, mercato=3, margine=4, valid=4, solo1M=3, autom=4, dif=2),
    "209 CURVA: pilota automatico per le pompe di calore":             dict(mot=4, vant=3, dolore=3, mercato=4, margine=4, valid=4, solo1M=3, autom=2, dif=2),
    "210 SMALTO: anteprima degli smalti ceramici":                     dict(mot=4, vant=3, dolore=3, mercato=2, margine=4, valid=4, solo1M=2, autom=4, dif=2),
    "211 CONTROPROVA: due diligence sulle scoperte scientifiche":      dict(mot=5, vant=3, dolore=3, mercato=2, margine=4, valid=3, solo1M=2, autom=3, dif=2),
    "212 GLIFO: famiglia di caratteri da poche lettere":               dict(mot=4, vant=3, dolore=2, mercato=2, margine=5, valid=4, solo1M=2, autom=4, dif=2),
    "213 MORFO: grado delle vie di arrampicata":                       dict(mot=4, vant=3, dolore=2, mercato=3, margine=4, valid=3, solo1M=2, autom=4, dif=2),
    "214 GEMELLO: riordino del magazzino da un video":                 dict(mot=4, vant=4, dolore=3, mercato=3, margine=4, valid=3, solo1M=2, autom=2, dif=2),
    "215 RIVERBERO: acustica della sala con i pannelli":               dict(mot=4, vant=3, dolore=3, mercato=2, margine=4, valid=3, solo1M=2, autom=4, dif=2),
    "216 MISCELA: stessa miscela di caffè con lotti diversi":          dict(mot=3, vant=3, dolore=3, mercato=2, margine=4, valid=4, solo1M=2, autom=3, dif=3),
    "217 CARTELLO: test di sicurezza per i robot":                     dict(mot=4, vant=3, dolore=2, mercato=3, margine=4, valid=3, solo1M=2, autom=2, dif=2),
    "260 Revenue manager per tavoli e biglietti dei locali notturni":  dict(mot=3, vant=4, dolore=2, mercato=2, margine=4, valid=3, solo1M=1, autom=3, dif=3),
}

# Correzioni: critiche di Lorenzo del 6/11/2026 e KRINÉ che non esiste (vedi CLAUDE.md).
CORREZIONI = {
    "107": dict(vant=4, obiettivo=3, conc=1),   # si fa da soli con un progetto Claude
    "116": dict(vant=3, obiettivo=3, conc=1),   # i ricercatori usano l'AI ancora meglio
    "234": dict(dolore=2, margine=3, conc=2),   # i contenuti animati rendono poco; montatore a 20–30 € a video
    "260": dict(obiettivo=2),                   # prezzi abitudinari, 90% degli ingressi alla porta a Firenze
    "200": dict(vant=3), "202": dict(vant=3), "205": dict(vant=3), "206": dict(vant=3),  # senza la rete KRINÉ
}

# Difesa dal "fai da te con l'AI" (1–5). Voto ragionato per le idee che passano le altre soglie; 2 per le altre.
DIY = {
    "107": 1, "116": 1, "234": 2, "260": 4,
    "083": 2,  # il dipendente chiede a un chatbot i dati sugli stipendi
    "087": 4,  # monitorare il web di continuo e chiedere le rimozioni non si fa con una chat
    "208": 4,  # serve elaborare dati satellitari, dell'inverter e 3D: fuori dalla portata dei proprietari
    "253": 3,  # le utility hanno team interni, ma il rendering personalizzato in serie va costruito
    "198": 3,  # chi controlla i modelli Excel può chiedere a Claude una revisione, non un certificato
    "199": 5,  # servono le telecamere sincronizzate al matrimonio
    "200": 5,  # laboratorio, test e proprietà intellettuale
    "201": 4,  # serve la produzione fisica del gioiello
    "205": 3,  # un pianificatore con Claude e un solver può arrangiarsi, ma va integrato con il gestionale
    "216": 3,  # una torrefazione può farsi aiutare da Claude, ma servono i dati sensoriali dei lotti
}


def carica(percorso, attributo=None):
    if attributo is None:
        attributo = re.search(r"^(\w+)\s*=\s*\{", percorso.read_text(), re.M).group(1)
    spec = importlib.util.spec_from_file_location(percorso.stem, percorso)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return getattr(modulo, attributo)


def tutte_le_idee():
    idee = {}
    for percorso, attributo in [(QUI / "idee_nuove.py", "IDEE"), (QUI / "perche_adesso.py", None),
                                (QUI / "futuro" / "punteggi.py", "CANDIDATI"),
                                (QUI / "futuro" / "video_motion.py", "PROPOSTE")]:
        idee.update(carica(percorso, attributo))
    idee.update(RAPIDI)
    return {nome[:3]: (nome, voti) for nome, voti in idee.items()}


def voti_v3(codice, v):
    w = dict(vant=v["vant"], dolore=v["dolore"], mercato=v["mercato"], margine=v["margine"],
             valid=v["valid"], obiettivo=min(5, v["solo1M"] + 1), autom=v["autom"], conc=v["dif"],
             diy=DIY.get(codice, 2))
    if codice in MOT_LORENZO:
        w["mot"] = v["mot"]
    w.update(CORREZIONI.get(codice, {}))
    return w


def valuta(w):
    sotto = [k for k in SOGLIE if w[k] < 3]
    peso = sum(PESI[k] for k in w)
    geo = math.exp(sum(PESI[k] * math.log(w[k]) for k in w) / peso)
    return sotto, geo


if __name__ == "__main__":
    idee = tutte_le_idee()
    validi, scartati = [], 0
    for codice, (nome, v) in idee.items():
        w = voti_v3(codice, v)
        sotto, geo = valuta(w)
        if sotto:
            scartati += 1
        else:
            validi.append((geo, nome, w))
    for geo, nome, w in sorted(validi, key=lambda t: -t[0]):
        voti = " ".join(f"{k}={x}" for k, x in w.items())
        print(f"{nome[:66]:66} {geo:.2f}  [{voti}]")
    print(f"\nPassano le soglie: {len(validi)} su {len(idee)}; scartate: {scartati}")
