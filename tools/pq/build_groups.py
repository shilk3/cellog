# Builds edu-pqgroups.js: Power Query asked in groups (tools/pq/groups.py).
# Each row: [group, what they do, what they take, 1 = a 📚 Completionist
# group, level (1 = has a Common function … 3), [[function, "Which one …?"], …]].
# Reads the functions' descriptions and levels from edu-banks.js.
# Usage (from the repo root): python3 tools/pq/build_groups.py edu-pqgroups.js
import json, re, sys
sys.path.insert(0, "tools/pq")
from groups import G, TEXT, clue

src = open("edu-banks.js").read()
block = src[src.index("  pq: [\n") + 8:src.index("\n  ],\n  vba: [")]
names = {r[0]: r for r in (json.loads(line.strip().rstrip(",")) for line in block.splitlines() if line.strip())}
rows = []
for name, ms in G:
    extra = {names[m][5] for m in ms}
    assert len(extra) == 1, name
    rows.append([name, *TEXT[name], extra.pop(), min(names[m][1] for m in ms), [[m, clue(m, names[m][3])] for m in ms]])
js = """// Power Query for 📘 Knowledge mode, in groups of look-alike functions —
// built by tools/pq/build_groups.py. A group check asks what they do, what
// they take, then "Which one …?" for each. Each row: [group, what they do,
// what they take, 1 = a 📚 Completionist group, level (1 = common … 3),
// [[function, question], …]].
const EDU_PQ_GROUPS = [
""" + "".join("  " + json.dumps(r, ensure_ascii=False) + ",\n" for r in rows) + "];\n"
open(sys.argv[1] if len(sys.argv) > 1 else "edu-pqgroups.js", "w").write(js)
print(len(rows), "groups,", sum(len(r[5]) for r in rows), "functions;", sum(1 for r in rows if not r[3]), "esports")
