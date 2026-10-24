# Builds edu-banks.js for the game: the invitationals' question banks, each
# row marked 1 when it's a 📚 Completionist extra (tools/bank/sets.json).
#   pq:    [name, level (1 common … 3 rare), category, description, arguments, extra]
#   vba:   [name, level (1 common, 2 other), category, description, arguments, extra]
#   robot: [command, hard (1 = hard in plain Excel), group, add-in, description, extra]
#   lam:   [LAMBDA, description, arguments, extra]
# Arguments as in edu-functions.js: "a|[b]|..." ("[x]" optional, "..." repeats).
# Usage (from the repo root): python3 tools/bank/build_game_banks.py edu-banks.js
import json, re, sys
sys.path.insert(0, "tools/bank")
ns = {}
exec(open("tools/bank/build_bank.py").read().split("PQLV =")[0], ns)
parse_vba_args = ns["parse_vba_args"]

sets = json.load(open("tools/bank/sets.json"))
extra = {k: set(v) for k, v in sets["extra"].items()}
removed = {k: set(v) for k, v in sets["removed"].items()}

# Shorter descriptions for a phone: Microsoft's first sentence, less filler.
FILLER = [
    (r",? as determined by the current date and time on the system", ""),
    (r"^Returns a logical value indicating whether", "Whether"),
    (r"^Indicates whether", "Whether"),
    (r"^Returns a value that indicates whether", "Whether"),
    (r"\s+\(via [^)]*\)", ""),
    (r"\s+", " "),
]
def short(d):
    d = (d or "").strip()
    m = re.match(r"(.+?\.)(\s|$)", d)
    d = m.group(1) if m else d
    for a, b in FILLER: d = re.sub(a, b, d)
    return d.strip().rstrip(".")

def spec(labels):
    return "|".join("..." if a in ("…", "...") else a for a in labels)

pq = json.load(open("tools/pq/levelled.json"))
vba = json.load(open("tools/vba/levelled.json"))
rb = json.load(open("tools/robot/robot_clean.json"))
rows = {
    "pq": [[x["name"], x["level"], x["cat"].replace("-", " "), short(x["desc"]),
            spec([("[" + a["n"] + "]") if a["opt"] else a["n"] for a in x["args"]]), 1 if x["name"] in extra["pq"] else 0]
           for x in sorted(pq, key=lambda x: x["name"].lower())],
    "vba": [[v["name"], 1 if v["level"] == 1 else 2, v["cat"].replace(" functions", ""), short(v["desc"]),
             spec(parse_vba_args(v["syntax"])), 1 if v["name"] in extra["vba"] else 0]
            for v in sorted(vba, key=lambda v: v["name"].lower())],
    "robot": [[c["name"], 1 if c["hard"] else 0, c["group"], c["src"].split(" + ")[0], short(c["desc"]), 1 if c["name"] in extra["cmds"] else 0]
              for c in rb["cmds"] if c["name"] not in removed["cmds"] and c["desc"]],
    "lam": [[l["name"], short(l["desc"]), spec(l["params"] or []), 1 if l["name"] in extra["lams"] else 0]
            for l in rb["lams"] if l["desc"] and l["name"] not in removed["lams"]],
}
js = """// The invitationals' question banks for 📘 Knowledge mode — built by
// tools/bank/build_game_banks.py from Microsoft's Power Query M and VBA
// references and the OA Robot add-ins' own command and LAMBDA lists (names
// of people removed). The last column: 1 = a 📚 Completionist extra.
const EDU_BANKS = {
""" + "".join(f"  {k}: [\n" + "".join("    " + json.dumps(r, ensure_ascii=False) + ",\n" for r in v) + "  ],\n" for k, v in rows.items()) + "};\n"
open(sys.argv[1] if len(sys.argv) > 1 else "edu-banks.js", "w").write(js)
print({k: (len(v), sum(r[-1] for r in v)) for k, v in rows.items()}, len(js), "bytes")
