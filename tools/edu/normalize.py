import json, re
P = json.load(open("parsed.json"))

FIX = {
    "EXPAND": "array, rows, [columns], [pad_with]",
    "MAKEARRAY": "rows, cols, lambda",
    "MAP": "array1, [array2], ..., lambda",
    "MODE.MULT": "number1, [number2], ...",
    "PERMUTATIONA": "number, number_chosen",
    "REDUCE": "[initial_value], array, lambda",
    "SCAN": "[initial_value], array, lambda",
    "BYROW": "array, lambda",
    "BYCOL": "array, lambda",
    "RTD": "progID, server, topic1, [topic2], ...",
    "SWITCH": "expression, value1, result1, [default_or_value2], [result2], ...",
}

def parse_args(s):
    s = s.replace("…", "...").replace("…", "...")
    args, depth, cur, repeat = [], 0, "", False
    def flush(tok, opt):
        nonlocal repeat
        tok = tok.strip()
        if not tok: return
        if "..." in tok:
            before = tok.replace("...", "").strip(" ,")
            if before: flush(before, opt)
            if not repeat: args.append({"n": "...", "opt": True})
            repeat = True
            return
        tok = re.sub(r"\s+", "_", tok.strip("[] "))
        if tok != "progID": tok = tok.lower()
        if tok: args.append({"n": tok, "opt": opt})
    opt_here = False
    for ch in s:
        if ch == "[":
            flush(cur, depth > 0 or opt_here); cur = ""; depth += 1; continue
        if ch == "]":
            flush(cur, True); cur = ""; depth = max(0, depth - 1); continue
        if ch == ",":
            flush(cur, depth > 0); cur = ""; continue
        cur += ch
    flush(cur, depth > 0)
    return args, repeat

out = []
for p in P:
    if p["syntax"] is None: continue
    args, rep = parse_args(FIX.get(p["name"], p["syntax"]))
    ver = re.findall(r"\((.*?)\)", p["label"])
    out.append({"name": p["name"], "cat": p["cat"].replace("Look and reference", "Lookup and reference"), "desc": p["desc"], "ver": ver[0] if ver else "", "args": args, "repeat": rep})
json.dump(out, open("funcs.json", "w"), indent=1)
# anomalies
for f in out:
    odd = [a["n"] for a in f["args"] if not re.fullmatch(r"[a-z][a-z0-9_']*|\.\.\.|progID", a["n"])]
    dup = len({a["n"].lower() for a in f["args"]}) != len(f["args"])
    if odd or dup: print(f["name"], f["args"], f["repeat"], "ODD" if odd else "", "DUP" if dup else "")
print(len(out))
