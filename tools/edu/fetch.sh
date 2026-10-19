#!/bin/sh
# Step 1 of building edu-functions.js (📘 Education mode's function bank):
# download Microsoft's "Excel functions (alphabetical)" list and every
# function's page into tools/edu/pages/ (not committed). Run from tools/edu/.
#   sh fetch.sh && python3 parse.py && python3 normalize.py && python3 classify.py && python3 build.py ../../edu-functions.js
set -e
curl -sL "https://support.microsoft.com/en-us/excel/excel-functions-alphabetical" -o ms_funcs.html
python3 - <<'PY'
import re, html, json
s = open("ms_funcs.html").read()
out = []
for r in re.findall(r"<tr[^>]*>(.*?)</tr>", s, re.S):
    tds = re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)
    if len(tds) < 2: continue
    link = re.search(r'href="([^"]+)"', tds[0])
    clean = lambda x: re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x))).strip()
    out.append({"label": clean(tds[0]), "href": link.group(1) if link else None, "cat_desc": clean(tds[1])})
json.dump(out, open("list.json", "w"), indent=1)
print(len(out), "functions listed")
PY
mkdir -p pages
python3 -c "import json; print('\n'.join(sorted(set(o['href'] for o in json.load(open('list.json'))))))" |
  xargs -P 8 -I{} sh -c 'f=pages/$(basename {}).html; [ -s "$f" ] || curl -sL --max-time 40 "https://support.microsoft.com/en-us/excel/{}" -o "$f"'
