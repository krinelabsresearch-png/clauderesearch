"""Punteggi delle proposte 234–254 (video in motion design fatti con Claude Code) con la scheda v2 (pesi in ../scheda_v2.py).
Verifica rapida del 30/10/2026 (circa 25 ricerche web in tutto), non il dossier completo: sopra 3,5 vuol dire
"merita la ricerca completa". Motivazione = stima di Claude, da confermare da Lorenzo. Testo in proposte-video-motion.md.
Esecuzione: python3 video_motion.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from scheda_v2 import PESI  # noqa: E402

SOGLIA = 3.5

PROPOSTE = {
    "234 SERATA: contenuti animati ogni settimana per discoteche e promoter": dict(mot=5, vant=5, dolore=3, mercato=3, margine=4, valid=5, solo1M=2, autom=4, dif=3),
    "235 PREVENTIVO: video personalizzato per ogni preventivo (fotovoltaico)": dict(mot=4, vant=3, dolore=3, mercato=4, margine=4, valid=4, solo1M=3, autom=5, dif=2),
    "236 ABSTRACT: video abstract degli articoli scientifici":                 dict(mot=4, vant=4, dolore=2, mercato=3, margine=4, valid=4, solo1M=3, autom=4, dif=2),
    "237 RILASCIO: un video per ogni release, da GitHub":                       dict(mot=4, vant=3, dolore=2, mercato=3, margine=5, valid=4, solo1M=3, autom=5, dif=1),
    "238 GUIDA VIVA: video tutorial che si rifanno quando cambia l'interfaccia": dict(mot=3, vant=4, dolore=3, mercato=4, margine=4, valid=3, solo1M=3, autom=5, dif=1),
    "239 TEOREMA: animazioni di matematica corrette per editori e docenti":     dict(mot=5, vant=4, dolore=2, mercato=3, margine=3, valid=3, solo1M=2, autom=4, dif=2),
    "240 SPOT: dal catalogo e-commerce agli annunci animati":                   dict(mot=4, vant=3, dolore=3, mercato=5, margine=3, valid=4, solo1M=2, autom=5, dif=1),
    "241 WRAPPED: il video personale di fine anno per app e negozi":            dict(mot=4, vant=3, dolore=2, mercato=4, margine=4, valid=3, solo1M=3, autom=4, dif=2),
    "242 ITINERARIO: il viaggio proposto dall'agenzia, in video con la mappa":  dict(mot=3, vant=3, dolore=2, mercato=4, margine=4, valid=4, solo1M=3, autom=5, dif=2),
    "243 LEDWALL: visual a tempo di musica col marchio della serata":           dict(mot=5, vant=4, dolore=2, mercato=2, margine=4, valid=4, solo1M=1, autom=3, dif=3),
    "244 IMMOBILI: un video per ogni annuncio dell'agenzia immobiliare":        dict(mot=3, vant=2, dolore=3, mercato=4, margine=4, valid=4, solo1M=3, autom=5, dif=2),
    "245 LOCALIZZA: anteprime animate per App Store in 40 lingue":              dict(mot=3, vant=3, dolore=2, mercato=3, margine=4, valid=4, solo1M=3, autom=5, dif=1),
    "246 INVITI: video inviti personalizzati venduti su Etsy":                  dict(mot=3, vant=3, dolore=2, mercato=4, margine=4, valid=5, solo1M=2, autom=5, dif=1),
    "247 MERCATI: video settimanale dei mercati per consulenti finanziari":     dict(mot=3, vant=3, dolore=2, mercato=3, margine=4, valid=3, solo1M=3, autom=5, dif=2),
    "248 MARCHIO: il motion design del marchio per i team marketing":           dict(mot=3, vant=3, dolore=3, mercato=4, margine=4, valid=3, solo1M=3, autom=4, dif=1),
    "249 PADEL: grafiche animate automatiche per tornei e circoli":             dict(mot=5, vant=3, dolore=2, mercato=2, margine=3, valid=4, solo1M=1, autom=4, dif=2),
    "250 LANCIO: dall'indirizzo del sito al video di lancio":                   dict(mot=3, vant=3, dolore=2, mercato=4, margine=4, valid=4, solo1M=2, autom=5, dif=1),
    "251 CANALE: canale YouTube di dati animati senza volto":                   dict(mot=4, vant=3, dolore=1, mercato=3, margine=3, valid=4, solo1M=2, autom=4, dif=2),
    "252 KIT: template e skill di motion design a pagamento":                   dict(mot=3, vant=3, dolore=1, mercato=3, margine=5, valid=5, solo1M=1, autom=4, dif=1),
    "253 BOLLETTA: video personalizzati per utility, telco e assicurazioni":    dict(mot=2, vant=2, dolore=3, mercato=4, margine=4, valid=2, solo1M=3, autom=4, dif=3),
    "254 STUDIO: studio di motion design con l'AI (servizio, escluso)":         dict(mot=3, vant=3, dolore=3, mercato=4, margine=3, valid=5, solo1M=1, autom=2, dif=1),
}


def punteggio(v):
    return sum(PESI[k] * v[k] for k in PESI)


if __name__ == "__main__":
    sopra = 0
    for nome, v in sorted(PROPOSTE.items(), key=lambda kv: -round(punteggio(kv[1]), 6)):
        s = punteggio(v)
        neutro = s - PESI["mot"] * (v["mot"] - 3)
        esito = "sopra 3,5" if s > SOGLIA + 1e-9 else "-"
        sopra += s > SOGLIA + 1e-9
        print(f"{nome:76} {s:.2f}  (motivazione 3: {neutro:.2f})  {esito}")
    print(f"\nSopra 3,5: {sopra} su {len(PROPOSTE)}")
