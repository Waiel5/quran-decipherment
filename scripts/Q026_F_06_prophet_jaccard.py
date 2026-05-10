#!/usr/bin/env python3
"""
Q026-F-06: 7-prophet narrative root-Jaccard cohesion within Q 26 vs random
contiguous sub-blocks of comparable Meccan narrative surahs.

Pre-reg SHA locked: 85766b7fcfe42c39c7a93de619127f385e1c4664d218b4f740c4a8328073c912
Pre-reg file: surahs/Q026-al-shuara/Q026-F-06-prophet-jaccard-cohesion-prereg.md
Seed: 20260509.

Outputs to surahs/Q026-al-shuara/csv/Q026-F-06.json
"""

import hashlib
import json
import os
import random
import re
import sys
from itertools import combinations

BASE = "/Users/grey/Downloads/quran"
SEED = 20260509
N_PERM = 10000

PREREG = os.path.join(BASE, "surahs/Q026-al-shuara/Q026-F-06-prophet-jaccard-cohesion-prereg.md")
EXPECTED_SHA = "85766b7fcfe42c39c7a93de619127f385e1c4664d218b4f740c4a8328073c912"
OUT = os.path.join(BASE, "surahs/Q026-al-shuara/csv/Q026-F-06.json")

# 7 prophet-pericope ranges (inclusive both sides, verse ids in Q 26)
PROPHET_BLOCKS_Q26 = {
    "Musa":     (10, 68),
    "Ibrahim":  (69, 104),
    "Nuh":      (105, 122),
    "Hud":      (123, 140),
    "Salih":    (141, 159),
    "Lut":      (160, 175),
    "Shuayb":   (176, 191),
}

# Comparable Meccan narrative-prophet-cycle surahs (baseline pool)
BASELINE_SURAHS = [7, 11, 21, 38, 51]


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_prereg():
    actual = sha256_file(PREREG)
    if actual != EXPECTED_SHA:
        sys.stderr.write(f"SHA MISMATCH Q026-F-06: expected {EXPECTED_SHA}, got {actual}\n")
        sys.exit(2)
    print(f"[OK] Q026-F-06 pre-reg SHA verified: {actual[:16]}...")


def load_qac_verse_roots():
    """Returns (surah, verse) -> sorted list of distinct ROOT codes in that verse."""
    path = os.path.join(BASE, "data/morphology/quranic-corpus-morphology-0.4.txt")
    by_vk = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            loc = parts[0].strip("()")
            features = parts[3]
            m = re.search(r"ROOT:([^|]+)", features)
            if not m:
                continue
            root = m.group(1)
            try:
                s, v, _w, _p = [int(x) for x in loc.split(":")]
            except ValueError:
                continue
            by_vk.setdefault((s, v), set()).add(root)
    return {k: tuple(sorted(s)) for k, s in by_vk.items()}


def block_root_set(verse_roots, surah, v_start, v_end):
    out = set()
    for v in range(v_start, v_end + 1):
        out.update(verse_roots.get((surah, v), ()))
    return out


def mean_pairwise_jaccard(blocks):
    """blocks: list of sets. Returns mean Jaccard over all C(n,2) pairs."""
    n = len(blocks)
    if n < 2:
        return 0.0
    total = 0.0
    pairs = 0
    for i, j in combinations(range(n), 2):
        a, b = blocks[i], blocks[j]
        u = a | b
        if not u:
            j_ = 0.0
        else:
            j_ = len(a & b) / len(u)
        total += j_
        pairs += 1
    return total / pairs


def get_surah_verse_count(corpus, sid):
    for s in corpus:
        if s["id"] == sid:
            return s["total_verses"]
    return 0


def main():
    verify_prereg()

    rng = random.Random(SEED)

    with open(os.path.join(BASE, "quran-text/quran-no-tashkeel.json"), encoding="utf-8") as f:
        corpus = json.load(f)

    verse_roots = load_qac_verse_roots()

    # Compute Q 26 observed mean-pairwise-Jaccard over 7 prophet blocks
    q26_blocks = [block_root_set(verse_roots, 26, lo, hi)
                  for (lo, hi) in PROPHET_BLOCKS_Q26.values()]
    block_sizes = [(hi - lo + 1) for (lo, hi) in PROPHET_BLOCKS_Q26.values()]
    J_obs = mean_pairwise_jaccard(q26_blocks)

    # Per-block root-set sizes for transparency
    block_root_set_sizes = [len(b) for b in q26_blocks]

    # Null: 10,000 draws of 7 contiguous sub-blocks of matching sizes from
    # the baseline pool (random surah, random valid start, with replacement
    # across surahs).
    baseline_verse_counts = {sid: get_surah_verse_count(corpus, sid)
                             for sid in BASELINE_SURAHS}

    null_J = []
    for _ in range(N_PERM):
        blocks = []
        for size in block_sizes:
            # try draws until we find a surah long enough; should be quick
            for _attempt in range(50):
                sid = rng.choice(BASELINE_SURAHS)
                v_max = baseline_verse_counts[sid]
                if size > v_max:
                    continue
                v_start = rng.randint(1, v_max - size + 1)
                v_end = v_start + size - 1
                blocks.append(block_root_set(verse_roots, sid, v_start, v_end))
                break
            else:
                blocks.append(set())
        null_J.append(mean_pairwise_jaccard(blocks))

    null_mean = sum(null_J) / N_PERM
    null_sd = (sum((x - null_mean) ** 2 for x in null_J) / N_PERM) ** 0.5
    # one-sided upper tail p
    p_perm = sum(1 for x in null_J if x >= J_obs) / N_PERM

    direction_passed = (J_obs > null_mean)
    pass_criterion = (p_perm < 0.025 and J_obs >= null_mean + null_sd)
    if not direction_passed:
        verdict = "PRE-COMMIT VIOLATION: J_obs < null_mean (Q 26 prophet blocks LESS cohesive than random Meccan)"
    elif pass_criterion:
        verdict = f"CONFIRMED: J_obs={J_obs:.4f} > null_mean={null_mean:.4f} (+{(J_obs-null_mean)/null_sd:.2f} SD), p_perm={p_perm:.4f} < 0.025"
    else:
        verdict = f"NULL: J_obs={J_obs:.4f} vs null_mean={null_mean:.4f}, p_perm={p_perm:.4f} (not < 0.025)"

    result = {
        "test_id": "Q026-F-06",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "blocks_Q26": {name: list(rng_) for name, rng_ in PROPHET_BLOCKS_Q26.items()},
        "block_sizes": block_sizes,
        "block_root_set_sizes": block_root_set_sizes,
        "baseline_surahs": BASELINE_SURAHS,
        "J_obs_Q26": J_obs,
        "null_mean": null_mean,
        "null_sd": null_sd,
        "Z_obs": (J_obs - null_mean) / null_sd if null_sd > 0 else None,
        "p_perm_one_sided_upper": p_perm,
        "alpha_bonferroni": 0.025,
        "direction_passed": direction_passed,
        "pass_criterion_met": pass_criterion,
        "verdict": verdict,
    }

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(json.dumps({k: v for k, v in result.items() if k != "blocks_Q26"},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
