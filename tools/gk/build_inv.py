# Builds edu-inv.js, the invitationals' own question sets for 📘 Knowledge
# mode, from inv_sets.py: a general set per invitational, and Mobile's
# "Excel on a phone" and function-picker sets. Rows as in edu-general.js:
# [id, skill, Titan skill, league tier, topic, question, answer, wrong1–3].
# Ids hash the set and question, so editing a question starts it afresh.
# Usage (from the repo root): python3 tools/gk/build_inv.py edu-inv.js
import hashlib, json, sys
sys.path.insert(0, "tools/gk")
from inv_sets import INFO, SETS, picker_rows

out, ids = {}, set()
def row(key, skill, titan, tier, topic, question, answer, wrong):
    qid = hashlib.sha1(f"{key}:{question}".encode()).hexdigest()[:8]
    assert qid not in ids and len({answer, *wrong}) == 4, question
    ids.add(qid)
    return [qid, skill, titan, tier, topic, question, answer, *wrong]
for key, qs in SETS.items():
    out[key] = [row(key, sk, INFO[key]["titan"], tier, INFO[key]["name"], qq, a, w) for tier, sk, qq, a, w, src in qs]
out["pick"] = [row("pick", sk, ti, tier, "Function picker", qq, a, w) for name, tier, sk, ti, qq, a, w, desc in picker_rows()]
js = """// The invitationals' own questions for 📘 Knowledge mode. Built by
// tools/gk/build_inv.py. Each invitational's general question comes from its
// set (Mobile: three "phone" questions in place of a function, then a
// "pick" question); once played, a set joins the general questions. Rows:
// [id, skill, Titan skill, league tier, topic, question, answer, wrong1–3].
const EDU_INV = {
""" + "".join(f"  {k}: [\n" + "".join("    " + json.dumps(r, ensure_ascii=False) + ",\n" for r in rows) + "  ],\n" for k, rows in out.items()) + "};\n"
open(sys.argv[1] if len(sys.argv) > 1 else "edu-inv.js", "w").write(js)
print({k: len(v) for k, v in out.items()})
