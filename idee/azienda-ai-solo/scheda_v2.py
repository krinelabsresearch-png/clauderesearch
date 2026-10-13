"""Scheda pesata v2: obiettivo "azienda AI-nativa da 1 persona, > 1 M€ di fatturato, 5–10 h/sett a regime".

Rispetto alla v1: entrano "Potenziale > 1 M€ senza dipendenti" (15%) e "Automazione con AI" (10%);
escono "Scalabilità e territorio" e "Tempo al primo euro" (non serve reddito a breve); scendono
"Dolore" (15→10%) e "Mercato" (10→5%). Voti = stime di Claude; la motivazione va confermata da Lorenzo.
Esecuzione: python3 scheda_v2.py
"""

PESI = {"mot": .20, "vant": .15, "dolore": .10, "mercato": .05, "margine": .10,
        "valid": .10, "solo1M": .15, "autom": .10, "dif": .05}
assert abs(sum(PESI.values()) - 1) < 1e-9

MODELLI = {
    "A Dropshipping gestito da agenti (070)":           dict(mot=3, vant=4, dolore=3, mercato=4, margine=2, valid=4, solo1M=2, autom=3, dif=2),
    "B App consumer AI in abbonamento (web + app)":     dict(mot=4, vant=4, dolore=3, mercato=4, margine=4, valid=4, solo1M=5, autom=5, dif=2),
    "C Micro-SaaS B2B verticale con agenti":            dict(mot=2, vant=4, dolore=4, mercato=4, margine=5, valid=3, solo1M=4, autom=3, dif=3),
    "D Prodotti di dati e API (es. Apify, 044)":        dict(mot=2, vant=4, dolore=3, mercato=3, margine=4, valid=5, solo1M=3, autom=5, dif=2),
    "E Marchio fisico proprio gestito da agenti":       dict(mot=3, vant=3, dolore=3, mercato=4, margine=3, valid=2, solo1M=3, autom=3, dif=3),
    "F Siti di contenuti e affiliazione con AI":        dict(mot=2, vant=3, dolore=2, mercato=3, margine=4, valid=5, solo1M=2, autom=5, dif=1),
    "G Prodotti digitali (template, corsi)":            dict(mot=2, vant=2, dolore=2, mercato=3, margine=5, valid=5, solo1M=3, autom=3, dif=1),
}

if __name__ == "__main__":
    for nome, v in sorted(MODELLI.items(), key=lambda kv: -sum(PESI[k] * kv[1][k] for k in PESI)):
        s = sum(PESI[k] * v[k] for k in PESI)
        senza_mot = s - PESI["mot"] * v["mot"] + PESI["mot"] * 3
        print(f"{nome:48} {s:.2f}   (con motivazione neutra 3: {senza_mot:.2f})")
