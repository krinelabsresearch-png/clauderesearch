#!/usr/bin/env bash
# Full pipeline: layers -> audio -> final MP4s with sound (60 fps + 30 fps each).
#   feed  = 4:5 flyer  (source/flyer.png)      -> OTIUM_4x5_*, OTIUM_9x16_*
#   reel  = 9:16 flyer (source/flyer_reel.png) -> OTIUM_reel_9x16_60fps only
set -euo pipefail
cd "$(dirname "$0")"

for v in feed reel; do
  OTIUM_VARIANT=$v python3 extract_layers.py
  OTIUM_VARIANT=$v python3 make_overview.py
done
python3 audio.py                      # must exist before the renders (muxed in directly)
OTIUM_VARIANT=feed python3 -u render.py --fmt 4x5 --fps30
OTIUM_VARIANT=feed python3 -u render.py --fmt 9x16 --fps30
OTIUM_VARIANT=reel python3 -u render.py --fmt 9x16
ls -la ../out
