#!/bin/sh
# Power Query M function bank (for the ⚡ Power Query invitational): fetch
# Microsoft's category pages and every function page into cats/ and fn/
# (not committed), then: python3 parse_pq.py && python3 levels.py
set -e
mkdir -p cats fn
for c in accessing-data binary combiner comparer date datetime datetimezone duration expression lines list logical number record replacer splitter table text time type uri value; do
  curl -sL --max-time 30 "https://learn.microsoft.com/en-us/powerquery-m/$c-functions" -o "cats/$c.html"
done
python3 - <<'PY'
import re, html, glob, json, os
out = []
for f in sorted(glob.glob("cats/*.html")):
    s = open(f).read(); cat = os.path.basename(f)[:-5]
    for tr in re.findall(r"<tr>(.*?)</tr>", s, re.S):
        tds = re.findall(r"<td[^>]*>(.*?)</td>", tr, re.S)
        if len(tds) < 2: continue
        a = re.search(r'href="([^"]+)"', tds[0])
        clean = lambda x: re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", x))).strip()
        out.append({"name": clean(tds[0]), "cat": cat, "desc": clean(tds[1]), "href": a.group(1) if a else None})
json.dump(out, open("list.json", "w"), indent=1)
print(len(out), "functions listed")
PY
python3 -c "import json; print('\n'.join(o['href'] for o in json.load(open('list.json')) if o['href']))" |
  xargs -P 10 -I{} sh -c 'f=fn/{}.html; [ -s "$f" ] || curl -sL --max-time 40 "https://learn.microsoft.com/en-us/powerquery-m/{}" -o "$f"'
