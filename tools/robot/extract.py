# OA Robot command collections -> robot_raw.json (not committed: it keeps the
# workbooks' full LAMBDA formulas and credits). Reads the workbooks only —
# no macros are run. Usage: python3 -I extract.py <folder with compbot.xlsm,
# formula_robot.xlsm, mewc_robot.xlsm, array_robot.xlsm, lambda_robot.xlam>
# Then: python3 -I build_robot.py <same folder>  ->  robot_clean.json
import sys, json, re
sys.path.insert(0, ".")
from xl import book
SRC = sys.argv[1].rstrip("/") + "/"
cmds, lams = [], []
sh, names = book(SRC + "compbot.xlsm")
for r, row in sorted(sh["Info_Commands"].items()):
    if r >= 9 and row.get("B"):
        cmds.append({"src": "CompBot", "name": row["B"], "group": "", "desc": row.get("D", ""), "params": row.get("E", ""), "code": row.get("F", "")})
for r, row in sorted(sh["Info_Lambdas"].items()):
    if r >= 9 and row.get("B"):
        lams.append({"src": "CompBot", "name": row["B"], "desc": row.get("D", ""), "params": row.get("E", ""), "formula": names.get(row["B"], {}).get("formula", "")})
for fn, src in [("formula_robot.xlsm", "Formula Robot"), ("mewc_robot.xlsm", "MEWC Robot")]:
    sh, names = book(SRC + fn)
    s = list(sh.values())[0]
    group = ""
    for r, row in sorted(s.items()):
        if r < 3: continue
        if row.get("B") and not row.get("C"):
            group = row["B"]; continue
        if row.get("B"):
            cmds.append({"src": src, "name": row["B"], "group": group, "desc": row.get("C", ""), "params": "", "code": ""})
    for n, v in names.items():
        lams.append({"src": src, "name": n, "desc": v["comment"], "params": "", "formula": v["formula"]})
sh, names = book(SRC + "array_robot.xlsm")
grid = sh["Commands"]
heads = dict(grid[3].items())
for r, row in sorted(grid.items()):
    if r < 5: continue
    for c, v in row.items():
        if c in heads:
            cmds.append({"src": "Array Robot", "name": v, "group": heads[c], "desc": "", "params": "", "code": ""})
for sname, rows in sh.items():
    if sname == "Commands": continue
    rr = sorted(rows.items())
    for i, (r, row) in enumerate(rr):
        b = row.get("B", "")
        m = re.match(r"^([A-Za-z][A-Za-z0-9_.]*)\((.*)\)$", b.strip())
        if m and not b.startswith("="):
            desc = rr[i + 1][1].get("B", "") if i + 1 < len(rr) else ""
            lams.append({"src": "Array Robot", "name": m.group(1), "desc": desc, "params": m.group(2), "formula": names.get(m.group(1), {}).get("formula", ""), "group": sname})
json.dump({"cmds": cmds, "lams": lams}, open("robot_raw.json", "w"), indent=1)
print(len(cmds), "commands,", len(lams), "lambdas")
