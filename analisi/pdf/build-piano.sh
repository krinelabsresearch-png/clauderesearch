#!/bin/sh
# Rigenera il piano: numeri dal modello, HTML, PDF.
# PY = interprete Python con PyMuPDF installato (serve a unire copertina e corpo).
set -e
cd "$(dirname "$0")"
(cd ../modello && python3 numeri.py > /dev/null)
python3 gen/genera.py
node render-piano.mjs
"${PY:-python3}" - <<'PYEOF'
import pymupdf
out = pymupdf.open(); out.insert_pdf(pymupdf.open("cover.pdf")); out.insert_pdf(pymupdf.open("body.pdf"))
out.save("Krine-Labs_Piano-di-progetto.pdf"); print("pagine", len(out))
PYEOF
rm -f cover.pdf body.pdf
