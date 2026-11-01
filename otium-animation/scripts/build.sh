#!/usr/bin/env bash
# Full pipeline: layers -> audio -> final MP4s (4:5 + 9:16, 60 fps + 30 fps, with sound).
set -euo pipefail
cd "$(dirname "$0")"

python3 extract_layers.py
python3 make_overview.py
python3 audio.py                      # must exist before the renders (muxed in directly)
python3 -u render.py --fmt 4x5
python3 -u render.py --fmt 9x16
ls -la ../out
