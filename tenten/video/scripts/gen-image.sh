#!/usr/bin/env bash
# Genera un'immagine con Codex (piano ChatGPT) e la salva in gen/<nome>/<nome>.png.
# Uso: scripts/gen-image.sh <nome> "<prompt>" [immagine di riferimento]
set -u
name=$1; prompt=$2; ref=${3:-}
dir=gen/$name
mkdir -p "$dir"
args=(exec --skip-git-repo-check --sandbox workspace-write -C "$dir")
[ -n "$ref" ] && { cp "$ref" "$dir/"; args+=(-i "$dir/$(basename "$ref")"); }
# il prompt passa da stdin: -i accetta più file e altrimenti lo leggerebbe come immagine
echo "Use your built-in image generation tool exactly once. $prompt When the image is generated, copy it from \$CODEX_HOME/generated_images into the current directory as $name.png (keep the alpha channel if any) and print its pixel size. Do not write any code to draw the image yourself." |
  codex "${args[@]}" - > "$dir/log.txt" 2>&1
ls -la "$dir/$name.png" 2>/dev/null || echo "MANCANTE $name"
