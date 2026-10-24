# Builds the CELLOG Question Bank review page (an Artifact) from the banks:
# edu-functions.js (Excel + Python), tools/pq/levelled.json,
# tools/vba/levelled.json and tools/robot/robot_clean.json, with the
# esports/extra split from tools/bank/sets.json.
# Usage (from the repo root): python3 tools/bank/build_bank.py out.html
import json, re, sys
def parse_vba_args(s):
    s = s.replace("…", "...")
    args, depth, cur = [], 0, ""
    def flush(tok, opt):
        tok = tok.strip().strip(",").strip()
        if not tok: return
        if tok == "...": args.append("…"); return
        args.append(("[" + tok + "]") if opt else tok)
    for ch in s:
        if ch == "[": flush(cur, depth > 0); cur = ""; depth += 1; continue
        if ch == "]": flush(cur, True); cur = ""; depth = max(0, depth - 1); continue
        if ch == ",": flush(cur, depth > 0); cur = ""; continue
        cur += ch
    flush(cur, depth > 0)
    return args
PQLV = {1: "Common", 2: "Everyday", 3: "Rare"}
pq = json.load(open("tools/pq/levelled.json"))
vba = json.load(open("tools/vba/levelled.json"))
rb = json.load(open("tools/robot/robot_clean.json"))
js = open("edu-functions.js").read()
excel = json.loads("[" + re.search(r"const EDU_FUNCS = \[(.*?)\];", js, re.S).group(1).strip().rstrip(",") + "]")
sets = json.load(open("tools/bank/sets.json"))
data = {
    "pq": [[x["name"], PQLV[x["level"]], x["cat"].replace("-", " "), [("[" + a["n"] + "]") if a["opt"] else a["n"] for a in x["args"]], x["desc"]] for x in pq],
    "vba": [[v["name"], "Common" if v["level"] == 1 else "Other", v["cat"].replace(" functions", ""), parse_vba_args(v["syntax"]), v["desc"]] for v in sorted(vba, key=lambda v: v["name"].lower())],
    "cmds": [[c["name"], "Robot-only" if c["hard"] else "Easy in Excel", c["group"] or "—", c["desc"], c["src"]] for c in rb["cmds"]],
    "lams": [[l["name"], l["src"], l["params"] or [], l["desc"]] for l in rb["lams"] if l["name"] != "ShowHighlights"],
    "extra": sets["extra"],
}
tpl = open("tools/bank/question_bank_tpl.html").read()
out = tpl.replace("__EXCEL__\n", js).replace("__BANK__\n", "const BANK = " + json.dumps(data, ensure_ascii=False) + ";\n")
open(sys.argv[1], "w").write(out)
print({k: len(v) for k, v in data.items() if k != "extra"})
