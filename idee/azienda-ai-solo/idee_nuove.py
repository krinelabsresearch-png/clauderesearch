"""Punteggi delle idee nuove 072–081 con la scheda v2 (pesi in scheda_v2.py).
Revisione del 13/10/2026: motivazione dai commenti di Lorenzo e nuove prove (vedi risposte-idee-nuove.md). Esecuzione: python3 idee_nuove.py
"""
from scheda_v2 import PESI

IDEE = {
    "072 Delitto a cena su misura (gioco di società generato dall'AI)":   dict(mot=1, vant=4, dolore=2, mercato=3, margine=5, valid=5, solo1M=4, autom=5, dif=2),
    "073 Canzone-regalo personalizzata con AI":                          dict(mot=3, vant=3, dolore=2, mercato=3, margine=5, valid=5, solo1M=3, autom=5, dif=1),
    "074 Tutor AI per il semestre filtro di Medicina":                   dict(mot=4, vant=4, dolore=3, mercato=3, margine=5, valid=4, solo1M=2, autom=4, dif=1),
    "075 Perizia AI dell'auto usata prima dell'acquisto":                dict(mot=4, vant=4, dolore=3, mercato=4, margine=4, valid=4, solo1M=3, autom=5, dif=2),
    "076 Agente che taglia le bollette":                                 dict(mot=1, vant=4, dolore=4, mercato=4, margine=4, valid=3, solo1M=4, autom=4, dif=2),
    "077 Cene tra sconosciuti abbinati dall'AI, per una nicchia":        dict(mot=3, vant=4, dolore=3, mercato=4, margine=3, valid=4, solo1M=3, autom=2, dif=2),
    "078 Profumo su misura disegnato dall'AI":                           dict(mot=1, vant=3, dolore=2, mercato=4, margine=4, valid=2, solo1M=3, autom=3, dif=3),
    "079 Libro di viaggio impaginato dall'AI":                           dict(mot=1, vant=3, dolore=2, mercato=3, margine=3, valid=4, solo1M=3, autom=5, dif=2),
    "080 Seconda opinione AI sui preventivi di ristrutturazione":        dict(mot=2, vant=3, dolore=4, mercato=4, margine=5, valid=4, solo1M=3, autom=5, dif=1),
    "081 Detective delle recensioni e degli sconti falsi":               dict(mot=2, vant=5, dolore=3, mercato=4, margine=4, valid=4, solo1M=2, autom=5, dif=2),
}

if __name__ == "__main__":
    for nome, v in sorted(IDEE.items(), key=lambda kv: -sum(PESI[k] * kv[1][k] for k in PESI)):
        s = sum(PESI[k] * v[k] for k in PESI)
        print(f"{nome:66} {s:.2f}  (motivazione 3: {s - PESI['mot'] * (v['mot'] - 3):.2f})")
