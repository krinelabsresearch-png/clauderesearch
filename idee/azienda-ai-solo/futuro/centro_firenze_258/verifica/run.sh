#!/bin/bash
b=$1
[ -s out_$b.json ] && exit 0
P="$(cat prompt.txt)
$(cat batch_$b.json)"
timeout 1500 codex --search exec -m gpt-6-luna --skip-git-repo-check -s read-only --output-schema schema.json -o out_$b.json "$P" > log_$b.txt 2>&1
echo "batch $b exit $?"
