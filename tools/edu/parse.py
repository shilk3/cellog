import re, html, json, os

L = json.load(open("list.json"))


def text(path):
    s = open(path, encoding="utf8", errors="ignore").read()
    s = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", s, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", s)
    t = html.unescape(t).replace(" ", " ").replace("​", "")
    return re.sub(r"\s+", " ", t)


def find_syntax(t, name):
    found = []
    si = t.find("Syntax")
    for seg in ([t[si:]] if si >= 0 else []) + [t]:
        for mm in re.finditer(r"(?<![A-Za-z0-9._])" + re.escape(name) + r"\s*\(", seg):
            i = mm.end(); depth = 1; j = i
            while j < len(seg) and depth:
                if seg[j] == "(": depth += 1
                elif seg[j] == ")": depth -= 1
                j += 1
            args = seg[i:j - 1].strip()
            if len(args) < 300 and "=" not in args and '"' not in args:
                found.append(args)
        if found: break
    nonempty = [a for a in found if a]
    return nonempty[0] if nonempty else ("" if found else None)


# Pages without a syntax line (the forecasting reference) or retired (FIND).
OVERRIDE = {
    "FIND": "find_text, within_text, [start_num]",
    "FORECAST.ETS": "target_date, values, timeline, [seasonality], [data_completion], [aggregation]",
    "FORECAST.ETS.CONFINT": "target_date, values, timeline, [confidence_level], [seasonality], [data_completion], [aggregation]",
    "FORECAST.ETS.SEASONALITY": "values, timeline, [data_completion], [aggregation]",
    "FORECAST.ETS.STAT": "values, timeline, statistic_type, [seasonality], [data_completion], [aggregation]",
    "FORECAST.LINEAR": "x, known_y's, known_x's",
}
SKIP_B = {"FINDB", "LEFTB", "LENB", "MIDB", "REPLACEB", "RIGHTB", "SEARCHB"}
out, bad = [], []
for o in L:
    lab = o["label"]
    base = re.sub(r"\s*\(.*?\)\s*", "", lab).strip()
    names = [n.strip().replace("BETA.INVn", "BETA.INV") for n in base.split(",")]
    cat, desc = o["cat_desc"].split(":", 1)
    t = text("pages/" + os.path.basename(o["href"]) + ".html")
    for name in names:
        if name in SKIP_B: continue
        args = OVERRIDE.get(name) or find_syntax(t, name)
        if args is None: bad.append(name)
        out.append({"name": name, "label": lab, "cat": cat.strip(), "desc": desc.strip(), "syntax": args, "href": o["href"]})
json.dump(out, open("parsed.json", "w"), indent=1)
print(len(out), "bad", len(bad), bad)
