import copy
from motore import *

def run(s): return simula(s)
b = scenario("Base")
print("BASE: min", round(run(b)['minimo']), run(b)['mese_min'], "m30", round(run(b)['cassa'][30]))
for nome in SCENARI:
    r = run(scenario(nome))
    print(f"{nome:24s} min {r['minimo']:>9,.0f} (mese {r['mese_min']:2d})  m24 {r['cassa'][24]:>9,.0f}  m30 {r['cassa'][30]:>9,.0f}  clienti {sum(r['nuovi'].values()):>6,.0f}  pubbl {sum(r['pubbl'].values()):>7,.0f}")
# tranche
t = copy.deepcopy(b); t["capitale"] = [(1, 100000.0), (10, 150000.0)]
r = run(t); print("tranche 100+150: min prima di m10", round(min(r['cassa'][m] for m in range(1, 10))), "min tot", round(r['minimo']), r['mese_min'])
# griglia CAC x quota percorsi
print("\nCAC \\ quota p6 -> cassa minima / cassa m30")
for cac in (40, 50, 60, 70, 85, 100):
    riga = []
    for q6 in (0.15, 0.25, 0.35):
        s = copy.deepcopy(b)
        resto = 1 - q6; base_resto = 0.10 + 0.45 + 0.20
        s["mix"] = {"p6": q6, "p3": 0.10 * resto / base_resto, "abb": 0.45 * resto / base_resto, "sing": 0.20 * resto / base_resto}
        s["tranche"] = [(a, n, imp, cac) for a, n, imp, _ in s["tranche"]]; s["cac_dopo"] = cac
        r = run(s); riga.append(f"{r['minimo']/1000:6.0f}/{r['cassa'][30]/1000:4.0f}")
    print(cac, riga)
# costo industriale
print("\ncosto flacone -> valore 12m, 24m, CAC max (24m/2)")
for c in (5.35, 8.50, 11.90):
    s = copy.deepcopy(b); s["costo_flacone"] = c
    v12 = valore_cliente(s, 12)["medio"]; v24 = valore_cliente(s, 24)["medio"]
    print(c, round(v12, 2), round(v24, 2), round(v24 / 2, 2))
# payback coorte media e abbonamento
for nome in ("Base", "Avverso senza arresto"):
    s = scenario(nome)
    curve = {o: curva_cumulata(s, o) for o in OFFERTE}
    media = [sum(s["mix"][o] * curve[o][a] for o in OFFERTE) for a in range(ETA)]
    print(nome, "coorte media cumulata:", [round(x, 1) for x in media[:13]])
    print(nome, "abbonamento cumulata:", [round(x, 1) for x in curve["abb"][:13]])
    v = vettori(s)
    print("ordini abb per età", [round(x, 3) for x in v["abb"]["ordini"][:14]], "tot", round(sum(v['abb']['ordini']), 2), "12m", round(sum(v['abb']['ordini'][:12]), 2))
    print("ordini sing", round(sum(v['sing']['ordini']), 2), "p3", round(sum(v['p3']['ordini']), 3), "p6", round(sum(v['p6']['ordini']), 3), "rimb p6", round(sum(v['p6']['rimborsi']), 4))
