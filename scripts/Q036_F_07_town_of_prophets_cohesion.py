#!/usr/bin/env python3
"""
Q036-F-07 — Q 36:13-32 "town destroyed for rejecting prophets" lexical cohesion
            with parallel pericopes vs ambient Q 36.

Pre-reg: surahs/Q036-yasin/preregs/Q036-F-07-town-of-prophets-cohesion-prereg.md
SHA-256: 6f71e1877fff6e799a5a2b2c494452fb117198396468cc3284737fe68802e82d
Seed:    20260509
Perms:   10,000
"""

import hashlib
import json
import random
import re
import sys
from collections import defaultdict
from pathlib import Path

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
PREREG = PROJECT_ROOT / "surahs/Q036-yasin/preregs/Q036-F-07-town-of-prophets-cohesion-prereg.md"
EXPECTED_SHA = "6f71e1877fff6e799a5a2b2c494452fb117198396468cc3284737fe68802e82d"
QAC = PROJECT_ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"

PERICOPE_Q36 = (36, 13, 32)
PARALLEL_PERICOPES = [
    (7, 73, 93),
    (11, 42, 95),
    (27, 45, 58),
]
N_PERMS = 10_000
SEED = 20260509


def verify_prereg_sha():
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FATAL: pre-reg SHA mismatch.\n  expected: {EXPECTED_SHA}\n  actual:   {actual}",
              file=sys.stderr)
        sys.exit(1)
    print(f"[ok] pre-reg SHA verified: {actual[:16]}...")


def parse_qac_verse_roots():
    """Return dict[(surah, verse)] -> set of roots."""
    verse_roots = defaultdict(set)
    root_pat = re.compile(r"ROOT:([^|]+)")
    loc_pat = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)")
    with open(QAC) as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            loc_m = loc_pat.match(line)
            if not loc_m:
                continue
            surah = int(loc_m.group(1))
            verse = int(loc_m.group(2))
            root_m = root_pat.search(line)
            if not root_m:
                continue
            verse_roots[(surah, verse)].add(root_m.group(1).strip())
    return verse_roots


def roots_of(verse_roots, surah, v_start, v_end):
    out = set()
    for v in range(v_start, v_end + 1):
        out |= verse_roots.get((surah, v), set())
    return out


def jaccard(a, b):
    if not a and not b:
        return 0.0
    return len(a & b) / len(a | b)


def main():
    verify_prereg_sha()

    verse_roots = parse_qac_verse_roots()

    # 1. Build root-sets
    pericope_roots = roots_of(verse_roots, *PERICOPE_Q36)

    parallel_union = set()
    for s, vs, ve in PARALLEL_PERICOPES:
        parallel_union |= roots_of(verse_roots, s, vs, ve)

    q36_all = roots_of(verse_roots, 36, 1, 83)
    # Ambient = Q 36 minus the pericope; we use *root-set* difference,
    # which is the right operational definition for Jaccard.
    q36_ambient_block_a = roots_of(verse_roots, 36, 1, 12)
    q36_ambient_block_b = roots_of(verse_roots, 36, 33, 83)
    q36_ambient = q36_ambient_block_a | q36_ambient_block_b

    # 2. Observed J values
    j1 = jaccard(pericope_roots, parallel_union)
    j2 = jaccard(pericope_roots, q36_ambient)
    delta_obs = j1 - j2

    print(f"|pericope_roots| = {len(pericope_roots)}")
    print(f"|parallel_union| = {len(parallel_union)}")
    print(f"|q36_ambient|    = {len(q36_ambient)}")
    print(f"J(pericope, parallel_union) = {j1:.6f}")
    print(f"J(pericope, q36_ambient)    = {j2:.6f}")
    print(f"Δ (observed) = {delta_obs:+.6f}")

    # 3. Permutation null: random 20-verse contiguous spans of Q 36
    rng = random.Random(SEED)
    n_q36_verses = 83
    span_len = (PERICOPE_Q36[2] - PERICOPE_Q36[1] + 1)
    assert span_len == 20
    max_start = n_q36_verses - span_len + 1   # valid start positions
    count_at_least = 0
    perm_deltas = []
    for _ in range(N_PERMS):
        start = rng.randint(1, max_start)
        end = start + span_len - 1
        span_roots = roots_of(verse_roots, 36, start, end)
        # Build ambient = Q36 \ span (set difference on the union basis)
        # Operational definition: ambient_span = roots of (Q36 verses 1..n) excluding span verses
        amb_roots = set()
        for v in range(1, n_q36_verses + 1):
            if v < start or v > end:
                amb_roots |= verse_roots.get((36, v), set())
        d = jaccard(span_roots, parallel_union) - jaccard(span_roots, amb_roots)
        perm_deltas.append(d)
        if d >= delta_obs:
            count_at_least += 1
    p_perm = (count_at_least + 1) / (N_PERMS + 1)

    print(f"\nPermutation null (n={N_PERMS}, seed={SEED}):")
    print(f"  Δ_observed     = {delta_obs:+.6f}")
    print(f"  count(Δ ≥ obs) = {count_at_least}")
    print(f"  p_perm         = {p_perm:.5f}")

    # 4. Robustness: Q 11:42-95 alone (largest parallel)
    parallel_q11 = roots_of(verse_roots, 11, 42, 95)
    j1_q11only = jaccard(pericope_roots, parallel_q11)
    print(f"\nRobustness — Q 11:42-95 alone: J = {j1_q11only:.6f}")

    # 5. Verdict
    if delta_obs > 0 and p_perm <= 0.05:
        verdict = "PASS-DIRECTED"
    elif delta_obs < -0.05:
        verdict = "REVERSED-NULL (pre-commit reversal; published with prominence)"
    elif delta_obs > 0:
        verdict = f"DIRECTIONAL-NULL (Δ > 0 but p_perm = {p_perm:.4f} > 0.05)"
    else:
        verdict = "NULL (Δ ≤ 0; ambient cohesion ≥ parallel-pericope cohesion)"

    result = {
        "finding_id": "Q036-F-07",
        "pre_reg_sha256": EXPECTED_SHA,
        "seed": SEED,
        "n_permutations": N_PERMS,
        "date": "2026-05-09",
        "rules_tuple": "(no-tashkeel, QAC v0.4 stem-roots, basmala-counted-only-in-Q1, "
                       "Hafs-Kufan, Mashriqi, verse-range-inclusive)",
        "pericope": {"surah": 36, "v_start": 13, "v_end": 32, "n_roots": len(pericope_roots)},
        "parallel_pericopes": [
            {"surah": s, "v_start": vs, "v_end": ve} for s, vs, ve in PARALLEL_PERICOPES
        ],
        "parallel_union_size": len(parallel_union),
        "q36_ambient_size": len(q36_ambient),
        "j_pericope_vs_parallel_union": round(j1, 6),
        "j_pericope_vs_q36_ambient": round(j2, 6),
        "delta_observed": round(delta_obs, 6),
        "p_perm": round(p_perm, 5),
        "robustness_q11_alone": round(j1_q11only, 6),
        "verdict": verdict,
        "interpretation": (
            f"Q 36:13-32 (the aṣḥāb al-qarya pericope) shares "
            f"{j1*100:.1f}% Jaccard root-overlap with the union of three "
            f"parallel town-destruction pericopes (Q 7:73-93, Q 11:42-95, "
            f"Q 27:45-58), versus {j2*100:.1f}% with the rest of Q 36. "
            f"Δ = {delta_obs:+.4f}. Permutation null over 10,000 random "
            f"20-verse contiguous spans of Q 36 gives p = {p_perm:.4f}."
        ),
        "honest_limits": [
            "Q 11:42-95 dominates the parallel-union (54 of the 89 parallel verses).",
            "Mass-shared theological roots (Allāh, rabb, rasūl, qāla) inflate Jaccard regardless.",
            "Set-based Jaccard does not capture frequency; a TF-weighted cosine variant is queued.",
        ],
    }

    out = PROJECT_ROOT / "surahs/Q036-yasin/csv/Q036-F-07.json"
    out.write_text(json.dumps(result, indent=2, ensure_ascii=False))
    print(f"\nVerdict: {verdict}")
    print(f"Output: {out}")


if __name__ == "__main__":
    main()
