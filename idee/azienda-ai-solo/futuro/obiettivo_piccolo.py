"""Esercizio del 01/11/2026: obiettivo "piccolo" al posto del milione.
Idee già valutate con automazione >= 4 (voti presi da punteggi.py e video_motion.py). Il criterio "solo1M"
(peso 0,15) è sostituito da "piccolo": 500–1.000 € netti al mese (circa 8–18 k€ lordi l'anno),
meno di 10 ore a settimana dopo il lancio, sotto 30 k€ lordi per restare nel forfettario.
Gli altri voti restano quelli dei dossier. Esecuzione: python3 obiettivo_piccolo.py
"""
import importlib.util
import sys
from pathlib import Path

QUI = Path(__file__).resolve().parent
sys.path.insert(0, str(QUI.parent))
from scheda_v2 import PESI  # noqa: E402

SOGLIA = 3.5
PESI_PICCOLO = {("piccolo" if k == "solo1M" else k): p for k, p in PESI.items()}

# Voto "piccolo" (1–5): quanto è probabile arrivare a 500–1.000 € netti al mese con pochi clienti e < 10 h/sett.
PICCOLO = {
    "234": 5,  # 10 locali a 99 €/mese bastano, e sono nella tua rete
    "107": 4,  # circa 100 pacchetti l'anno; stagionale (sessioni di laurea)
    "116": 4,  # 20–25 abbonati a 49 €/mese
    "113": 4,  # 5–6 club a 150 €/mese
    "127": 4,  # pochi acquirenti ad alto prezzo, mercato in inglese
    "096": 3, "092": 3, "093": 3, "109": 3, "117": 3, "235": 3, "236": 3, "237": 3, "238": 3,
    "255": 3, "246": 3, "197": 3, "100": 3, "249": 3, "242": 3, "244": 3, "247": 3, "111": 3,
    "122": 3, "153": 2, "239": 2, "240": 2, "241": 2, "245": 2, "248": 2, "250": 2, "251": 2,
    "252": 2, "253": 1, "091": 2, "095": 2, "098": 2, "099": 2, "101": 2, "102": 2, "104": 2,
    "258": 4,  # 15 locali a 59 €/mese; fuori dal filtro perché ha automazione 3 (3,55 se calcolata)
    "106": 2, "110": 2, "114": 2, "115": 2, "118": 2, "120": 2, "121": 2,
}


def carica(nome_file, attributo):
    spec = importlib.util.spec_from_file_location(nome_file, QUI / nome_file)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return getattr(modulo, attributo)


if __name__ == "__main__":
    idee = {**carica("punteggi.py", "CANDIDATI"), **carica("video_motion.py", "PROPOSTE")}
    righe = []
    for nome, v in idee.items():
        codice = nome[:3]
        if v["autom"] < 4 or codice not in PICCOLO:
            continue
        voti = {("piccolo" if k == "solo1M" else k): x for k, x in v.items()}
        voti["piccolo"] = PICCOLO[codice]
        s = sum(PESI_PICCOLO[k] * voti[k] for k in PESI_PICCOLO)
        righe.append((s, s - PESI["mot"] * (v["mot"] - 3), nome))
    for s, neutro, nome in sorted(righe, reverse=True):
        if s > SOGLIA + 1e-9:
            print(f"{nome[:74]:74} {s:.2f}  (motivazione 3: {neutro:.2f})")
    print(f"\nSopra 3,5: {sum(s > SOGLIA + 1e-9 for s, _, _ in righe)} su {len(righe)} idee con automazione >= 4")
