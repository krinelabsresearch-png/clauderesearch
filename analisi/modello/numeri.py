import json, copy
from motore import *
b = scenario("Base"); rb = simula(b)
out = {}
# economia per ordine
out["ordine"] = {o: per_ordine(o, 8.5) for o in OFFERTE}
out["ordine_primo"] = {o: per_ordine(o, 8.5, 0.05) for o in OFFERTE}
e1 = out["ordine_primo"]["p6"]
out["rimborsi_p6"] = [(q, e1["contrib"] - q * e1["netto"]) for q in (0.05, 0.121, 0.20, 0.30)]
out["pareggio_p6"] = {cac: (e1["contrib"] - cac) / e1["netto"] for cac in (50, 60, 80)}
# valore cliente
out["valore"] = {h: valore_cliente(b, h) for h in (1, 3, 6, 12, 24, 36)}
out["costo"] = {}
for cst in (5.35, 8.50, 11.90):
    s = copy.deepcopy(b); s["costo_flacone"] = cst
    out["costo"][cst] = (valore_cliente(s, 12)["medio"], valore_cliente(s, 24)["medio"], valore_cliente(s, 24)["medio"] / 2)
curve = {o: curva_cumulata(b, o) for o in OFFERTE}
out["curva_media"] = [sum(b["mix"][o] * curve[o][a] for o in OFFERTE) for a in range(ETA)]
out["curva_abb"] = curve["abb"]
sa = scenario("Avverso senza arresto"); ca = {o: curva_cumulata(sa, o) for o in OFFERTE}
out["curva_media_avv"] = [sum(sa["mix"][o] * ca[o][a] for o in OFFERTE) for a in range(ETA)]
out["valore_avv"] = {h: valore_cliente(sa, h)["medio"] for h in (6, 12, 24)}
def payback(curva, cac):
    for a, x in enumerate(curva):
        if x >= cac: return a + 1
    return None
out["payback"] = {cac: (payback(out["curva_media"], cac), payback(out["curva_abb"], cac)) for cac in (50, 55, 60, 70, 80)}
v = vettori(b)
out["abb_ordini_12"] = sum(v["abb"]["ordini"][:12]); out["abb_ordini_tot"] = sum(v["abb"]["ordini"])
out["sopravv_abb"] = []
sopr = 1
for k in range(1, 14):
    out["sopravv_abb"].append(sopr); sopr *= b["rinnovo"][min(k, 6) - 1]
out["sing_ordini"] = sum(v["sing"]["ordini"])
# scenari
sc = {}
for nome in SCENARI:
    r = simula(scenario(nome))
    sc[nome] = dict(minimo=r["minimo"], mese_min=r["mese_min"], assorbito=250000 - r["minimo"], c24=r["cassa"][24], c30=r["cassa"][30],
                    clienti=sum(r["nuovi"].values()), pagati=sum(r["nuovi_pag"].values()), pubbl=sum(r["pubbl"].values()),
                    ricavi=sum(r["R"]["ricavi_netti"].values()), incassi=sum(r["R"]["incassi"].values()),
                    rimborsi=sum(r["R"]["rimborsi_lordi"].values()), esp=max(r["esposizione"].values()),
                    cred=max(r["credito"].values()), lotti=sum(1 for q in r["ordinati"].values() if q),
                    mesi_lotti=[m for m, q in r["ordinati"].items() if q], cassa=[r["cassa"][m] for m in range(1, 31)],
                    operativo=[r["operativo"][m] for m in range(1, 31)])
out["scenari"] = sc
# tranche di capitale
t = copy.deepcopy(b); t["capitale"] = [(1, 100000.0), (10, 150000.0)]; rt = simula(t)
out["tranche"] = dict(min_prima=min(rt["cassa"][m] for m in range(1, 10)), mese=min(range(1, 10), key=lambda m: rt["cassa"][m]),
                      speso_m9=100000 - rt["cassa"][9])
# griglia CAC x quota percorso
grid = {}
for cac in (40, 50, 60, 70, 85, 100):
    for q6 in (0.15, 0.25, 0.35):
        s = copy.deepcopy(b); resto = 1 - q6
        s["mix"] = {"p6": q6, "p3": 0.10 * resto / 0.75, "abb": 0.45 * resto / 0.75, "sing": 0.20 * resto / 0.75}
        s["tranche"] = [(a, n, imp, cac) for a, n, imp, _ in s["tranche"]]; s["cac_dopo"] = cac
        r = simula(s); grid[f"{cac}|{q6}"] = (r["minimo"], r["cassa"][30], valore_cliente(s, 24)["medio"] / 2)
out["griglia"] = grid
# fonti e impieghi base fino al mese 24
M = 24; R = rb["R"]; sm = lambda d: sum(d[m] for m in range(1, M + 1))
cat = {}
for (m, voce, imp, q, tp) in costi_progetto(b):
    if m <= M:
        k = voce.split(":")[0].split(",")[0]
        cat[k] = cat.get(k, 0) + imp
out["progetto_voci"] = cat
out["fonti_impieghi"] = dict(
    capitale=250000, incassi=sm(R["incassi"]),
    progetto=sm(rb["progetto"]), progetto_iva=sm(rb["progetto_iva"]), fissi=sm(rb["fissi"]), fissi_iva=sm(rb["fissi_iva"]),
    produzione=sm(rb["acquisti"]), produzione_iva=sm(rb["acquisti_iva"]), pubbl=sm(rb["pubbl"]), creativi=sm(rb["creativi"]),
    logistica=sm(R["logistica"]) * 1.22, commissioni=sm(R["commissioni"]), assistenza=sm(R["assistenza"]),
    rimborsi=sm(R["rimborsi_lordi"]), iva_versata=sm(rb["iva_da_versare"]), credito_m24=rb["credito"][M], cassa_m24=rb["cassa"][M])
out["tappe"] = rb["tappe"]
out["pre_lancio"] = dict(uscite_fino_15=250000 - rb["cassa"][15], progetto_fino_15=sum(rb["progetto"][m] for m in range(1, 16)))
out["flaconi_base"] = sum(R["flaconi"].values()); out["scorta"] = [rb["scorta"][m] for m in range(1, 31)]
out["nuovi_base"] = [rb["nuovi"][m] for m in range(1, 31)]
out["tranche_clienti"] = dict(t1=10000 / 50, t2=20000 / 50, t3=30000 / 55)
json.dump(out, open("numeri.json", "w"), indent=1, default=float)
# stampa sintetica
import pprint
for k in ("ordine", "ordine_primo"):
    print(k, {o: {x: round(y, 2) for x, y in d.items()} for o, d in out[k].items()})
print("rimborsi p6", [(q, round(x, 2)) for q, x in out["rimborsi_p6"]], "pareggio", {k: round(x, 4) for k, x in out["pareggio_p6"].items()})
for h, vv in out["valore"].items(): print("valore", h, {o: round(vv[o]["valore"], 2) for o in OFFERTE}, round(vv["medio"], 2))
print("costo", {k: tuple(round(x, 2) for x in v) for k, v in out["costo"].items()})
print("curva media", [round(x, 1) for x in out["curva_media"][:13]])
print("curva abb", [round(x, 1) for x in out["curva_abb"][:13]])
print("curva media avv", [round(x, 1) for x in out["curva_media_avv"][:13]], out["valore_avv"])
print("payback (media, abb) per CAC", out["payback"])
print("abb ordini 12m", round(out["abb_ordini_12"], 2), "tot", round(out["abb_ordini_tot"], 2), "sopravv", [round(x, 3) for x in out["sopravv_abb"]])
for n, d in sc.items(): print(n, {k: (round(v) if isinstance(v, float) else v) for k, v in d.items() if k not in ("cassa", "operativo")})
print("tranche", out["tranche"])
print("fonti/impieghi m24", {k: round(v) for k, v in out["fonti_impieghi"].items()})
print("progetto voci", {k: round(v) for k, v in cat.items()}, "tot", round(sum(cat.values())))
print("pre-lancio", out["pre_lancio"], "tappe", out["tappe"])
print("flaconi base 30m", round(out["flaconi_base"]), "scorta", [round(x) for x in out["scorta"][13:]])
print("nuovi base", [round(x) for x in out["nuovi_base"][15:]])
print("operativo base", [round(x) for x in sc["Base"]["operativo"][13:]])
