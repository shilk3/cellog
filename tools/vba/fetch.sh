#!/bin/sh
# VBA function bank (for the 💾 VBA invitational): Microsoft's VBA function
# list and each function's page into fn/ (not committed). list.json holds the
# list (category, page, name); then: python3 parse_vba.py
set -e
mkdir -p fn
python3 -c "import json; print('\n'.join(sorted(set(o['href'] for o in json.load(open('list.json'))))))" |
  xargs -P 10 -I{} sh -c 'f=fn/$(basename {}).html; [ -s "$f" ] || curl -sL --max-time 40 "https://learn.microsoft.com/en-us/office/vba/language/reference/{}" -o "$f"'
