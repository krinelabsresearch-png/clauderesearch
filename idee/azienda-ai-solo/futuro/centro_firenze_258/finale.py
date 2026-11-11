"""Applica la verifica di Codex e produce la classifica finale."""
import json
R = json.load(open("candidati.json")); V = json.load(open("verifica.json"))
DEBOLI = ["business.site", "sites.google.com", "wixsite.com", "eatbu.com", "wordpress.com", "blogspot.", "jimdo", "altervista.org", "site123", "webnode", "weebly"]          # sito gratuito o dismesso: ha già provato
NON_SITO = ["sbp-menu.com", "beb.it/"]                                 # portali scambiati per sito
INDIPENDENTI = ["casa artigiana dell", "the social hub"]                # strutture che ospitano attività indipendenti
out, escl = [], []
for r in R:
    v = V.get(r["id"])
    r["verificato"] = bool(v)
    if v:
        s = (v["sito_ufficiale"] or "").lower(); parte = (v["fa_parte_di"] or "")
        r["codex"] = v
        if v["chiusa"]:
            escl.append((r["nome"], "chiusa")); continue
        if parte and not any(k in parte.lower() for k in INDIPENDENTI):
            escl.append((r["nome"], "fa parte di " + parte)); continue
        if s and any(k in s for k in DEBOLI):
            r["pro"]["sito_rotto"] = 20; r["nota_sito"] = "solo sito gratuito o dismesso: " + v["sito_ufficiale"]
        elif s and not any(k in s for k in NON_SITO):
            escl.append((r["nome"], "ha già un sito: " + v["sito_ufficiale"])); continue
        elif v["email_dominio_proprio"]:
            r["pro"]["sito_rotto"] = 20; r["nota_sito"] = "ha un dominio email proprio senza sito: " + v["email_dominio_proprio"]
    r["propensione"] = sum(r["pro"].values())
    r["beneficio"] = round(r["beneficio"], 1)
    r["score"] = round(r["beneficio"] * r["propensione"] / 100, 1)
    out.append(r)
out.sort(key=lambda r: -r["score"])
json.dump(out, open("classifica_finale.json", "w"), ensure_ascii=False)
json.dump(escl, open("esclusi_codex.json", "w"), ensure_ascii=False)
top = out[:50]
print("esclusi da Codex:", len(escl)); [print("  -", *e) for e in escl]
print("50° punteggio:", top[-1]["score"], "| non verificati nella top 50:", [r["nome"] for r in top if not r["verificato"]])
print("miglior non verificato:", next((r["score"], r["nome"]) for r in out if not r["verificato"]))
