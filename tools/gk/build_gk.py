# Builds the general-knowledge bank (edu-general.js) for 📘 Knowledge mode:
# the hand-written topic questions (topics.py) plus two questions per
# Windows keyboard shortcut (shortcuts.py) — "what does it do?" and "which
# shortcut does it?" — with wrong answers from the same group. Each row:
# [id, skill, Titan skill, league tier (5 easiest … 0 the top), topic,
#  question, answer, wrong1, wrong2, wrong3]. Ids are a hash of the question,
# so editing a question starts its record afresh.
# Usage (from the repo root): python3 tools/gk/build_gk.py edu-general.js [review.json]
import hashlib, json, random, sys
sys.path.insert(0, "tools/gk")
from shortcuts import SHORTCUTS
from topics import T

rows = []
def add(skill, titan, tier, topic, question, answer, wrong):
    assert len(set([answer, *wrong])) == 4, (question, answer, wrong)
    qid = hashlib.sha1(question.encode()).hexdigest()[:8]
    rows.append([qid, skill, titan, tier, topic, question, answer, *wrong])

for skill, tier, topic, question, answer, wrong, titan in T:
    add(skill, titan, tier, topic, question, answer, wrong)

rng = random.Random(7)
groups = {}
for s in SHORTCUTS: groups.setdefault(s[4], []).append(s)
for keys, does, skill, tier, group in SHORTCUTS:
    same = [s for s in groups[group] if s[0] != keys and s[1] != does]
    others = [s for s in SHORTCUTS if s[0] != keys and s[1] != does and s not in same]
    pick = lambda n, pool: rng.sample(pool, n) if len(pool) >= n else pool + rng.sample(others, n - len(pool))
    wrong_does = [s[1] for s in pick(3, same)]
    add(skill, "speed", tier, "Keyboard shortcuts", f"What does {keys} do?", does, wrong_does)
    wrong_keys = [s[0] for s in pick(3, same)]
    add(skill, "speed", tier, "Keyboard shortcuts", f"Which shortcut: {does[0].lower() + does[1:]}?", keys, wrong_keys)

ids = [r[0] for r in rows]
assert len(ids) == len(set(ids)), "duplicate question"
js = """// General knowledge for 📘 Knowledge mode — one question in every
// Knowledge check. Built by tools/gk/build_gk.py from Microsoft's Excel help
// and its Windows keyboard-shortcut reference. Each row: [id, skill, Titan
// skill, league tier (5 easiest … 0 the top), topic, question, answer,
// wrong1, wrong2, wrong3].
const EDU_GENERAL = [
""" + "".join("  " + json.dumps(r, ensure_ascii=False) + ",\n" for r in rows) + "];\n"
open(sys.argv[1] if len(sys.argv) > 1 else "edu-general.js", "w").write(js)
import collections
print(len(rows), "questions;", "topics", dict(collections.Counter(r[4] for r in rows)))
print("tiers", sorted(collections.Counter(r[3] for r in rows).items()), "skills", dict(collections.Counter(r[1] for r in rows)))
print("skill x tier", {s: sorted(collections.Counter(r[3] for r in rows if r[1] == s).items()) for s in ["data", "map", "text", "games", "math", "time", "cards"]})
