"""Base del generatore: numeri dal modello, formattazione italiana, stile, grafici."""
import sys, json, re
sys.path.insert(0, "/home/user/clauderesearch/analisi/modello")
from motore import scenario, simula, valore_cliente, vettori, per_ordine, curva_cumulata, costi_progetto, SCENARI, OFFERTE

N = json.load(open("/home/user/clauderesearch/analisi/modello/numeri.json"))
SIM = {nome: simula(scenario(nome)) for nome in SCENARI}
BASE = scenario("Base")

def fmt_num(x, dec=0):
    s = f"{x:,.{dec}f}"
    return s.replace(",", "X").replace(".", ",").replace("X", ".")
def eur(x, dec=0): return fmt_num(x, dec)
def e2(x): return fmt_num(x, 2)
def pct(x, dec=1): return fmt_num(x * 100, dec) + "%"
def k(x): return fmt_num(x / 1000, 1) + " k€"

HEAD_CSS = open("/home/user/clauderesearch/analisi/pdf/report-piano.html").read().split("<style>")[1].split("</style>")[0]
EXTRA_CSS = """
  .fig{ margin:3mm 0 4.5mm; page-break-inside:avoid; }
  .fig svg{ width:100%; height:auto; display:block; }
  .fig .cap{ font-family:"Liberation Sans",sans-serif; font-size:7.6pt; color:var(--ink-faint); margin-top:1.4mm; line-height:1.35; }
  .fig .ttl{ font-family:"Liberation Sans",sans-serif; font-size:9pt; font-weight:700; margin-bottom:1.2mm; }
  .legend{ font-family:"Liberation Sans",sans-serif; font-size:7.8pt; color:var(--ink-soft); display:flex; flex-wrap:wrap; gap:1.2mm 4.5mm; margin:0 0 1.5mm; }
  .legend span{ display:inline-flex; align-items:center; gap:1.4mm; }
  .legend i{ display:inline-block; width:6mm; height:0; border-top:2px solid; }
  .legend i.d{ border-top-style:dashed; }
  table.tight td, table.tight th{ padding:1.2mm 1.6mm; }
  table.small{ font-size:7.9pt; }
  .src{ font-family:"Liberation Sans",sans-serif; font-size:7.6pt; color:var(--ink-faint); word-break:break-all; }
  .pill{ font-family:"Liberation Sans",sans-serif; font-size:7pt; font-weight:700; padding:.3mm 1.3mm; border-radius:1mm; white-space:nowrap; }
  .pill.ok{ background:#e3eedb; color:#2f4d22; }
  .pill.no{ background:#f4e0dc; color:#7a2e20; }
  .pill.mid{ background:#f3ead4; color:#6b4f14; }
  .gate{ border:.8px solid var(--rule); border-left:3.5px solid var(--accent); padding:2.8mm 3.6mm; margin:3mm 0; page-break-inside:avoid; }
  .gate .h{ font-family:"Liberation Sans",sans-serif; font-weight:700; font-size:9.4pt; color:var(--accent); margin-bottom:1.4mm; }
  .gate ul{ margin:0; }
  .gate li{ margin-bottom:.8mm; font-size:9.6pt; }
  table.long{ page-break-inside:auto; }
  table.long tr{ page-break-inside:avoid; }
"""

COL = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4"]   # palette validata, ordine fisso

def svg_linee(serie, xs, y_max, y_step, y_fmt, x_ticks, h=230, w=640, dash=None, vlines=(), hlines=(), label_min_gap=11, x_label="mese"):
    """serie: lista di (nome, colore, valori). Etichette dirette a fine linea con distanza minima."""
    ml, mr, mt, mb = 52, 128, 12, 30
    pw, ph = w - ml - mr, h - mt - mb
    x0, x1 = min(xs), max(xs)
    X = lambda x: ml + (x - x0) / (x1 - x0) * pw
    Y = lambda y: mt + ph - (y / y_max) * ph
    out = [f'<svg viewBox="0 0 {w} {h}" xmlns="http://www.w3.org/2000/svg" font-family="Liberation Sans,Arial,sans-serif">']
    y = 0
    while y <= y_max + 1e-9:
        out.append(f'<line x1="{ml}" x2="{ml+pw}" y1="{Y(y):.1f}" y2="{Y(y):.1f}" stroke="#e4e0d6" stroke-width="0.8"/>')
        out.append(f'<text x="{ml-6}" y="{Y(y)+3.5:.1f}" font-size="9.5" fill="#6b675e" text-anchor="end">{y_fmt(y)}</text>')
        y += y_step
    for xt in x_ticks:
        out.append(f'<text x="{X(xt):.1f}" y="{mt+ph+14}" font-size="9.5" fill="#6b675e" text-anchor="middle">{xt}</text>')
    out.append(f'<text x="{ml+pw/2:.1f}" y="{h-3}" font-size="9" fill="#8a867c" text-anchor="middle">{x_label}</text>')
    for xv, lab in vlines:
        out.append(f'<line x1="{X(xv):.1f}" x2="{X(xv):.1f}" y1="{mt}" y2="{mt+ph}" stroke="#a09a8c" stroke-width="0.9" stroke-dasharray="3 3"/>')
        out.append(f'<text x="{X(xv)+3:.1f}" y="{mt+9}" font-size="8.5" fill="#6b675e">{lab}</text>')
    for yv, lab in hlines:
        out.append(f'<line x1="{ml}" x2="{ml+pw}" y1="{Y(yv):.1f}" y2="{Y(yv):.1f}" stroke="#8a867c" stroke-width="0.9" stroke-dasharray="5 3"/>')
        out.append(f'<text x="{ml+pw*0.60:.1f}" y="{Y(yv)-3:.1f}" font-size="8.5" fill="#52514e" stroke="#ffffff" stroke-width="3" paint-order="stroke">{lab}</text>')
    ends = []
    for i, (nome, col, vals) in reversed(list(enumerate(serie))):
        pts = " ".join(f"{X(x):.1f},{Y(v):.1f}" for x, v in zip(xs, vals))
        da = f' stroke-dasharray="{dash[i]}"' if dash and dash[i] else ""
        out.append(f'<polyline points="{pts}" fill="none" stroke="#ffffff" stroke-width="4.2" stroke-linejoin="round"/>')
        out.append(f'<polyline points="{pts}" fill="none" stroke="{col}" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"{da}/>')
        out.append(f'<circle cx="{X(xs[-1]):.1f}" cy="{Y(vals[-1]):.1f}" r="3.2" fill="{col}" stroke="#fff" stroke-width="1.2"/>')
        ends.append([Y(vals[-1]), nome, col])
    ends.sort()
    for j in range(1, len(ends)):
        if ends[j][0] - ends[j-1][0] < label_min_gap: ends[j][0] = ends[j-1][0] + label_min_gap
    for yy, nome, col in ends:
        out.append(f'<text x="{ml+pw+7}" y="{yy+3.5:.1f}" font-size="9" fill="#2b2a27">{nome}</text>')
    out.append("</svg>")
    return "\n".join(out)

def legenda(items):
    return '<div class="legend">' + "".join(
        f'<span><i class="{"d" if d else ""}" style="border-top-color:{c}"></i>{n}</span>' for n, c, d in items) + "</div>"
