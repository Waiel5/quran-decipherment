#!/usr/bin/env python3
"""
Q044-F-05 — HM sibling-opener pericope Jaccard pair test (Q 41:1-8 / Q 44:1-8 / Q 46:1-8).
Pre-reg SHA256: 3ef9170973093f0eaec509b32fdf04eb05ec3370e7ff8d5210744e00159c8f2e
Seed: 20260509; n_perm: 10000; Bonferroni-3 → α = 0.0167.
"""
import hashlib
import json
import os
import random
import re
import sys
import statistics
from collections import defaultdict

PREREG = "/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/preregs/Q044-F-05-hawamim-opener-pericope-prereg.md"
EXPECTED_SHA = "3ef9170973093f0eaec509b32fdf04eb05ec3370e7ff8d5210744e00159c8f2e"
QAC = "/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt"
OUT = "/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/csv/Q044-F-05.json"
SEED = 20260509
N_PERM = 10000
ALPHA = 0.05 / 3
HM_TARGETS = [41, 44, 46]
WINDOW = 8

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

def jaccard(a, b):
    if not a and not b:
        return 0.0
    return len(a & b) / len(a | b)

def main():
    verify()
    verse_roots, verses_in_surah = parse_qac()
    # Observed: 3 pairwise Jaccards on Q 41:1-8, Q 44:1-8, Q 46:1-8
    blocks = {sid: block_roots(verse_roots, sid, 1, WINDOW) for sid in HM_TARGETS}
    pairs = [(HM_TARGETS[i], HM_TARGETS[j]) for i in range(len(HM_TARGETS)) for j in range(i+1, len(HM_TARGETS))]
    observed = [(a, b, jaccard(blocks[a], blocks[b])) for a, b in pairs]
    obs_mean = statistics.mean(j for _, _, j in observed)
    # Null: 10000 perms of 3 random blocks of WINDOW verses from non-HM surahs with >= WINDOW verses
    HM = {40, 41, 42, 43, 44, 45, 46}
    eligible_surahs = [sid for sid, vs in verses_in_surah.items() if sid not in HM and max(vs) >= WINDOW]
    rng = random.Random(SEED)
    null_means = []
    for _ in range(N_PERM):
        triple = []
        for _ in range(3):
            sid = rng.choice(eligible_surahs)
            max_v = max(verses_in_surah[sid])
            v_start = rng.randint(1, max_v - WINDOW + 1)
            triple.append(block_roots(verse_roots, sid, v_start, v_start + WINDOW - 1))
        m = statistics.mean(
            jaccard(triple[i], triple[j]) for i in range(3) for j in range(i+1, 3)
        )
        null_means.append(m)
    null_medians = statistics.median(null_means)
    n_ge = sum(1 for m in null_means if m >= obs_mean)
    p_one_sided = n_ge / N_PERM
    null_sorted = sorted(null_means)
    p25 = null_sorted[int(0.25 * N_PERM)]
    p75 = null_sorted[int(0.75 * N_PERM)]
    if obs_mean > null_medians and p_one_sided < ALPHA:
        verdict = "PASS-DIRECTED — HM opener-pericopes templated"
    elif obs_mean > null_medians:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL"
    out = {
        "prereg_id": "Q044-F-05",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_bon": ALPHA,
        "window_verses": WINDOW,
        "hm_targets": HM_TARGETS,
        "pericope_roots": {str(sid): sorted(blocks[sid]) for sid in HM_TARGETS},
        "pericope_root_counts": {str(sid): len(blocks[sid]) for sid in HM_TARGETS},
        "observed_jaccards": [{"pair": [a, b], "jaccard": j} for a, b, j in observed],
        "observed_mean": obs_mean,
        "null_median": null_medians,
        "null_p25": p25,
        "null_p75": p75,
        "p_one_sided_upper": p_one_sided,
        "pass_alpha": p_one_sided < ALPHA,
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"observed_mean = {obs_mean:.4f}")
    print(f"null_median   = {null_medians:.4f}  (p25={p25:.4f}, p75={p75:.4f})")
    print(f"p_one_sided   = {p_one_sided:.4f}")
    print(f"VERDICT: {verdict}")

if __name__ == "__main__":
    main()
