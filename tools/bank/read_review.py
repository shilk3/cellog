# Reads a filled-in review spreadsheet (from make_review.py) and writes
# tools/bank/sets.json: for each bank, the items marked "Keep? = No". Those
# aren't dropped: they're the completionist extras, while everything else is
# the default (esports) set. Comments and moves are listed for follow-up.
# Usage (from the repo root): python3 tools/bank/read_review.py review.xlsx
import json, sys
import openpyxl
# Removed outright (per the review): the Easter egg, and Excel's own LAMBDA
# functions, which are already in the Excel bank.
REMOVED = {"cmds": ["Eggy"], "lams": ["LAMBDA", "LET", "MAP", "REDUCE", "SCAN", "BYROW", "BYCOL", "MAKEARRAY", "ISOMITTED"]}
TABS = {"Excel": "excel", "Power Query": "pq", "VBA": "vba", "Robot commands": "cmds", "Lambdas": "lams", "Python": "py"}
wb = openpyxl.load_workbook(sys.argv[1], read_only=True)
out = {"extra": {}, "removed": REMOVED, "notes": {}}
for tab, key in TABS.items():
    rows = wb[tab].iter_rows(values_only=True)
    hdr = list(next(rows))
    keep = hdr.index("Keep?")
    note = next(i for i, h in enumerate(hdr) if h and h.startswith("Comments"))
    move = next((i for i, h in enumerate(hdr) if h and h.startswith("Change")), None)
    extra, kept, out["notes"][key] = [], set(), []
    for r in rows:
        if not r[0] or r[0] in REMOVED.get(key, []): continue
        if r[keep] == "No": extra.append(r[0])
        else: kept.add(r[0])
        if r[note] or (move is not None and r[move]):
            out["notes"][key].append({"name": r[0], "move": r[move] if move is not None else None, "note": r[note]})
    # A name listed twice (Power Query files a couple under two categories)
    # is kept if either listing was.
    out["extra"][key] = sorted(set(extra) - kept, key=extra.index)
json.dump(out, open("tools/bank/sets.json", "w"), indent=1, ensure_ascii=False)
print({k: len(v) for k, v in out["extra"].items()})
