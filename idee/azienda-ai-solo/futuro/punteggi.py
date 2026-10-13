"""Punteggi dei candidati 091–111 (bisogni dei prossimi 1–5 anni) con la scheda v2 (pesi in ../scheda_v2.py).
Voti dopo la ricerca approfondita (dossier in dossier/); la motivazione è una stima prudente di Claude, da confermare con Lorenzo.
In lista solo i candidati con punteggio > 3,5. Esecuzione: python3 punteggi.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scheda_v2 import PESI  # noqa: E402

SOGLIA = 3.5

CANDIDATI = {
    "091 Voce amica: telefonata AI quotidiana agli anziani soli":         dict(mot=3, vant=3, dolore=3, mercato=4, margine=2, valid=4, solo1M=2, autom=4, dif=2),
    "092 Allenatore AI dell'esame orale":                                 dict(mot=4, vant=3, dolore=3, mercato=3, margine=3, valid=5, solo1M=2, autom=4, dif=2),
    "093 Tutor di matematica AI a voce per bambini 6-13":                 dict(mot=4, vant=4, dolore=3, mercato=3, margine=3, valid=4, solo1M=2, autom=4, dif=2),
    "094 Coach AI di lettura ad alta voce per bambini 6-10":              dict(mot=3, vant=3, dolore=3, mercato=2, margine=2, valid=4, solo1M=1, autom=3, dif=2),
    "095 Orientamento AI basato sui dati (università e lavoro)":          dict(mot=4, vant=4, dolore=3, mercato=2, margine=2, valid=4, solo1M=2, autom=4, dif=2),
    "096 Tutor AI per Analisi 1, Geometria e Fisica 1":                   dict(mot=4, vant=5, dolore=3, mercato=3, margine=3, valid=4, solo1M=2, autom=4, dif=2),
    "098 Coach AI per ADHD e funzioni esecutive (adulti)":                dict(mot=3, vant=3, dolore=3, mercato=3, margine=4, valid=4, solo1M=2, autom=4, dif=2),
    "099 Storie audio AI personalizzate senza schermo (Toniebox/Yoto)":   dict(mot=3, vant=3, dolore=2, mercato=3, margine=3, valid=4, solo1M=2, autom=4, dif=1),
    "100 Libro della vita dei nonni con interviste telefoniche AI":       dict(mot=3, vant=3, dolore=3, mercato=3, margine=3, valid=5, solo1M=2, autom=4, dif=2),
    "101 Palestra sociale AI per giovani adulti":                         dict(mot=4, vant=3, dolore=2, mercato=3, margine=3, valid=4, solo1M=2, autom=4, dif=1),
    "102 Tracker AI dei capelli":                                         dict(mot=3, vant=4, dolore=2, mercato=3, margine=2, valid=4, solo1M=2, autom=4, dif=1),
    "103 Assistente AI per i caregiver familiari":                        dict(mot=3, vant=3, dolore=3, mercato=4, margine=3, valid=4, solo1M=2, autom=3, dif=2),
    "104 Coach AI di forza ed equilibrio per over 60":                    dict(mot=3, vant=3, dolore=2, mercato=4, margine=2, valid=3, solo1M=1, autom=4, dif=2),
    "105 Assistente di viaggio per l'Europa delle nuove regole":          dict(mot=4, vant=3, dolore=2, mercato=4, margine=2, valid=4, solo1M=2, autom=3, dif=1),
    "106 Coach AI per perimenopausa e menopausa":                         dict(mot=3, vant=3, dolore=3, mercato=4, margine=3, valid=4, solo1M=2, autom=4, dif=2),
    "107 Assistente AI per la tesi con dati (statistica e metodo)":       dict(mot=4, vant=5, dolore=4, mercato=2, margine=4, valid=4, solo1M=2, autom=4, dif=2),
    "108 Preparazione AI ai concorsi pubblici":                           dict(mot=3, vant=3, dolore=3, mercato=3, margine=4, valid=4, solo1M=2, autom=3, dif=2),
    "109 Matematica per lavorare con l'AI (adulti)":                      dict(mot=4, vant=5, dolore=2, mercato=2, margine=4, valid=4, solo1M=2, autom=4, dif=1),
    "110 Laboratorio AI per ragazzi 9-14, sicuro per i minori":           dict(mot=3, vant=3, dolore=2, mercato=3, margine=3, valid=3, solo1M=2, autom=4, dif=2),
    "111 Preparazione atletica e prevenzione infortuni nel padel":        dict(mot=5, vant=4, dolore=2, mercato=2, margine=2, valid=4, solo1M=2, autom=4, dif=1),
}


def punteggio(v):
    return sum(PESI[k] * v[k] for k in PESI)


if __name__ == "__main__":
    in_lista = 0
    for nome, v in sorted(CANDIDATI.items(), key=lambda kv: -punteggio(kv[1])):
        s = punteggio(v)
        neutro = s - PESI["mot"] * (v["mot"] - 3)
        esito = "IN LISTA" if s > SOGLIA + 1e-9 else "scartato"
        in_lista += esito == "IN LISTA"
        print(f"{nome:70} {s:.2f}  (motivazione 3: {neutro:.2f})  {esito}")
    print(f"\nIn lista: {in_lista} su {len(CANDIDATI)}")
