#!/usr/bin/env python3
"""
Q050-F-08 — Q 49 → Q 50 universal hinge re-verification (H-NEW-1262 / Q049-F-03 replication).

Pre-reg: surahs/Q050-qaf/preregs/Q050-F-08-q49-q50-hinge-reverify-prereg.md
Pre-reg SHA256 (locked): a5abbd2243712cbaa2bc355a132c8cb70a9427934b870418b043b902f40f8ed8

Verifies on disk that the Q049-F-03 result (in_all_three=True across H-NEW-130 root +
130b char-4-gram + 130c verse-length top-15 adjacencies) holds, AND independently
re-extracts the top-15 from h-new-130/130b/130c.json to check for STRONG-REPLICATION.
"""

import hashlib
import json
import sys
from pathlib import Path

PRE_REG = Path(__file__).resolve().parents[1] / "surahs" / "Q050-qaf" / "preregs" / "Q050-F-08-q49-q50-hinge-reverify-prereg.md"
EXPECTED_SHA = "a5abbd2243712cbaa2bc355a132c8cb70a9427934b870418b043b902f40f8ed8"
actual_sha = hashlib.sha256(PRE_REG.read_bytes()).hexdigest()
if actual_sha != EXPECTED_SHA:
    print(f"FATAL: pre-reg SHA mismatch.\n  expected: {EXPECTED_SHA}\n  actual:   {actual_sha}")
    sys.exit(1)

SEED = 20260509  # recorded; deterministic
ROOT = Path(__file__).resolve().parents[1]

# ---------------- Q049-F-03 JSON cross-read ----------------
Q049_JSON = ROOT / "surahs" / "Q049-al-hujurat" / "csv" / "Q049-F-03.json"
q049 = json.loads(Q049_JSON.read_text())

q049_in_all_three = bool(q049.get("primary_all_three", False))
q049_pair = q049.get("q49_q50_pair", [])
q049_root = bool(q049.get("in_h130_top15_root", False))
q049_char4 = bool(q049.get("in_h130b_top15_char4gram", False))
q049_verselen = bool(q049.get("in_h130c_top15_verselen", False))

# ---------------- Direct re-extraction from h-new-130/130b/130c ----------------
def has_49_50(j):
    d = json.loads(j.read_text())
    t15 = d.get("top15_largest_jumps", [])
    for e in t15:
        if isinstance(e, dict):
            a, b = e.get("i"), e.get("j")
            if {a, b} == {49, 50}:
                return True, e.get("distance"), len(t15)
    return False, None, len(t15)

H130 = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-130.json"
H130b = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-130b.json"
H130c = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-130c.json"

direct_h130, dist_root, n130 = has_49_50(H130)
direct_h130b, dist_char4, n130b = has_49_50(H130b)
direct_h130c, dist_verselen, n130c = has_49_50(H130c)

# ---------------- Verdict ----------------
json_all_ok = q049_root and q049_char4 and q049_verselen and q049_in_all_three and (sorted(q049_pair) == [49, 50])
direct_all_ok = direct_h130 and direct_h130b and direct_h130c
agreement = (q049_root == direct_h130) and (q049_char4 == direct_h130b) and (q049_verselen == direct_h130c)

if json_all_ok and direct_all_ok and agreement:
    verdict = "STRONG-REPLICATION"
elif json_all_ok and not direct_all_ok:
    verdict = "REPLICATED-JSON-ONLY"
elif not json_all_ok:
    verdict = "NULL-REPLICATION"
else:
    verdict = "DISAGREEMENT"

pre_commit_violation = not json_all_ok

out = {
    "finding_id": "Q050-F-08",
    "prereg_sha256": EXPECTED_SHA,
    "date_run": "2026-05-09",
    "rules_tuple": "(cross-feature replication; no parameter change from Q049-F-03)",
    "seed": SEED,
    "q049_f_03_json_cross_read": {
        "in_h130_top15_root": q049_root,
        "in_h130b_top15_char4gram": q049_char4,
        "in_h130c_top15_verselen": q049_verselen,
        "primary_all_three": q049_in_all_three,
        "pair": q049_pair,
        "all_ok": json_all_ok,
    },
    "direct_h130_root_top15": {
        "contains_49_50": direct_h130,
        "distance": dist_root,
        "top15_size": n130,
    },
    "direct_h130b_char4gram_top15": {
        "contains_49_50": direct_h130b,
        "distance": dist_char4,
        "top15_size": n130b,
    },
    "direct_h130c_verselen_top15": {
        "contains_49_50": direct_h130c,
        "distance": dist_verselen,
        "top15_size": n130c,
    },
    "direct_all_ok": direct_all_ok,
    "json_vs_direct_agreement": agreement,
    "pre_commit_violation": pre_commit_violation,
    "verdict": verdict,
}
OUT = ROOT / "surahs" / "Q050-qaf" / "csv" / "Q050-F-08.json"
OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
print(f"Q050-F-08: VERDICT={verdict}")
print(f"  Q049-F-03 JSON: in_all_three={q049_in_all_three}, pair={q049_pair}")
print(f"  Direct h-new-130 root: {direct_h130}; 130b char4g: {direct_h130b}; 130c verselen: {direct_h130c}")
print(f"  output: {OUT.relative_to(ROOT)}")
