#!/usr/bin/env python3
"""
Q046-F-07 — Q 46:29-32 jinn-pericope ↔ Q 72 root-Jaccard pair test
            (cross-direction MW-5 replication of Q072-F-03).
Pre-reg SHA256: 8702e3dce71929b3a523b66684151b04153e160ca5943a66207097835291e852
Seed: 20260509; n_perm: 10000; Bonferroni-3 → α = 0.0167.
"""
import hashlib
import json
import os
import random
import re
import statistics
import sys
from collections import defaultdict

PREREG = "/Users/grey/Downloads/quran/surahs/Q046-al-ahqaf/preregs/Q046-F-07-jinn-pericope-pair-replication-prereg.md"
EXPECTED_SHA = "8702e3dce71929b3a523b66684151b04153e160ca5943a66207097835291e852"
QAC = "/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt"
OUT = "/Users/grey/Downloads/quran/surahs/Q046-al-ahqaf/csv/Q046-F-07.json"
SEED = 20260509
N_PERM = 10000
ALPHA = 0.05 / 3
PERICOPE = (46, 29, 32)  # surah, v_start, v_end
TARGET_SURAH = 72
WINDOW = PERICOPE[2] - PERICOPE[1] + 1  # 4

LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")

def verify():
    with open(PREREG, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")
    print(f"[OK] Pre-reg SHA verified.")

def parse_qac():
    verse_roots = defaultdict(set)
    verses_in_surah = defaultdict(set)
    with open(QAC, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            m = LOC_RE.match(parts[0])
            if not m:
                continue
            sid = int(m.group(1))
            vid = int(m.group(2))
            verses_in_surah[sid].add(vid)
            feat = parts[3]
            rm = ROOT_RE.search(feat)
            if rm:
                verse_roots[(sid, vid)].add(rm.group(1))
    return verse_roots, verses_in_surah

def block_roots(verse_roots, sid, v_start, v_end):
    s = set()
    for v in range(v_start, v_end+1):
        s |= verse_roots.get((sid, v), set())
    return s

def surah_all_roots(verse_roots, sid, verses_in_surah):
    s = set()
    for v in verses_in_surah[sid]:
        s |= verse_roots.get((sid, v), set())
    return s

def jaccard(a, b):
    if not a and not b:
        return 0.0
    return len(a & b) / len(a | b)

def main():
    verify()
    verse_roots, verses_in_surah = parse_qac()
    pericope_roots = block_roots(verse_roots, PERICOPE[0], PERICOPE[1], PERICOPE[2])
    q72_roots = surah_all_roots(verse_roots, TARGET_SURAH, verses_in_surah)
    observed = jaccard(pericope_roots, q72_roots)
    # Null: 10000 perms; sample 4 contiguous verses from non-Q46-non-Q72 surahs with >= WINDOW verses
    eligible = [sid for sid, vs in verses_in_surah.items()
                if sid not in (46, 72) and max(vs) >= WINDOW]
    rng = random.Random(SEED)
    null_jaccards = []
    for _ in range(N_PERM):
        sid = rng.choice(eligible)
        max_v = max(verses_in_surah[sid])
        v_start = rng.randint(1, max_v - WINDOW + 1)
        block = block_roots(verse_roots, sid, v_start, v_start + WINDOW - 1)
        null_jaccards.append(jaccard(block, q72_roots))
    null_sorted = sorted(null_jaccards)
    n_ge = sum(1 for v in null_jaccards if v >= observed)
    p_one_sided = n_ge / N_PERM
    null_median = statistics.median(null_jaccards)
    p25 = null_sorted[int(0.25 * N_PERM)]
    p75 = null_sorted[int(0.75 * N_PERM)]
    if observed > null_median and p_one_sided < ALPHA:
        verdict = "PASS-DIRECTED — replicates Q072-F-03 from Q 46 direction"
        replicates = True
    elif observed > null_median:
        verdict = "DIRECTIONAL"
        replicates = False
    else:
        verdict = "NULL — fails to replicate Q072-F-03 from Q 46 direction"
        replicates = False
    out = {
        "prereg_id": "Q046-F-07",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_bon": ALPHA,
        "pericope": list(PERICOPE),
        "target_surah": TARGET_SURAH,
        "pericope_roots": sorted(pericope_roots),
        "pericope_root_count": len(pericope_roots),
        "q72_root_count": len(q72_roots),
        "observed_jaccard": observed,
        "null_median": null_median,
        "null_p25": p25,
        "null_p75": p75,
        "p_one_sided_upper": p_one_sided,
        "pass_alpha": p_one_sided < ALPHA,
        "replicates_Q072_F_03": replicates,
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"observed_jaccard = {observed:.4f}")
    print(f"null_median      = {null_median:.4f}  (p25={p25:.4f}, p75={p75:.4f})")
    print(f"p_one_sided      = {p_one_sided:.4f}")
    print(f"VERDICT: {verdict}")

if __name__ == "__main__":
    main()
