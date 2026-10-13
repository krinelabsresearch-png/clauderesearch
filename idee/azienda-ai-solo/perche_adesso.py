"""Punteggi delle idee "perché adesso" 082–090 con la scheda v2 (pesi in scheda_v2.py).
Bisogni nati da poco o in arrivo, con una data precisa (vedi perche-adesso.md). La motivazione è una stima di Claude, da confermare con Lorenzo.
Esecuzione: python3 perche_adesso.py
"""
from scheda_v2 import PESI

IDEE = {
    "082 Compagno per chi prende i farmaci GLP-1 (iniezioni e pillole)": dict(mot=4, vant=4, dolore=4, mercato=5, margine=4, valid=4, solo1M=4, autom=4, dif=2),
    "083 Busta paga giusta: coach della trasparenza salariale":         dict(mot=3, vant=3, dolore=3, mercato=4, margine=5, valid=4, solo1M=3, autom=4, dif=3),
    "084 Analisi del sangue spiegate e seguite nel tempo":              dict(mot=3, vant=3, dolore=3, mercato=4, margine=4, valid=3, solo1M=3, autom=4, dif=1),
    "085 Coach di padel per gli occhiali AI":                           dict(mot=5, vant=4, dolore=2, mercato=2, margine=4, valid=3, solo1M=2, autom=4, dif=3),
    "086 Analisi delle pubblicità dei concorrenti (dati UE del DSA)":   dict(mot=2, vant=4, dolore=3, mercato=3, margine=5, valid=4, solo1M=3, autom=4, dif=2),
    "087 Scudo contro foto rubate e deepfake":                          dict(mot=3, vant=3, dolore=4, mercato=4, margine=4, valid=3, solo1M=3, autom=4, dif=3),
    "088 Certificato della batteria dell'auto elettrica usata":         dict(mot=1, vant=3, dolore=3, mercato=3, margine=4, valid=3, solo1M=2, autom=4, dif=2),
    "089 Guardiano digitale per le famiglie (AI e social dei figli)":   dict(mot=3, vant=2, dolore=4, mercato=4, margine=4, valid=4, solo1M=3, autom=4, dif=2),
    "090 Scanner delle dichiarazioni green vietate dal 27/9/2026":      dict(mot=3, vant=4, dolore=3, mercato=3, margine=5, valid=4, solo1M=3, autom=4, dif=2),
}

if __name__ == "__main__":
    for nome, v in sorted(IDEE.items(), key=lambda kv: -sum(PESI[k] * kv[1][k] for k in PESI)):
        s = sum(PESI[k] * v[k] for k in PESI)
        print(f"{nome:66} {s:.2f}  (motivazione 3: {s - PESI['mot'] * (v['mot'] - 3):.2f})")
