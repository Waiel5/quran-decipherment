#!/usr/bin/env python3
"""H-NEW-1301 — IMPV-qrA 4-surah cluster Fisher-Rao cohesion.

Pre-reg: findings/phase-b-hypotheses/h-new-1301-impv-qra-cluster-prereg.md
SHA256:  ca4d3c763fa5c3f1185a3bb3fbf2b06672f414987e241abff48783f85647c8f4
"""

import hashlib
import json
import random
import sys
from itertools import combinations
from pathlib import Path
from statistics import mean

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-1301-impv-qra-cluster-prereg.md"
EXPECTED_SHA = "ca4d3c763fa5c3f1185a3bb3fbf2b06672f414987e241abff48783f85647c8f4"
FR_MATRIX = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
QURAN = ROOT / "quran-text/quran-no-tashkeel.json"
OUT = ROOT / "findings/phase-b-hypotheses/csv/h-new-1301.json"
SEED = 20260509
N_PERM = 10_000

CLUSTER = [17, 69, 73, 96]
HM_POSITIVE_CONTROL_POOL = [40, 41, 42, 43, 44, 45, 46]


def verify_prereg() -> None:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual}")
    print(f"pre-reg SHA verified: {EXPECTED_SHA[:12]}…")


def load_fr_matrix():
    h111 = json.loads(FR_MATRIX.read_text())
    D = [[0.0] * 115 for _ in range(115)]
    for a, b, dist in h111["D_matrix_upper_triangular"]:
        D[a][b] = dist
        D[b][a] = dist
    return D


def load_verse_counts():
    text = json.loads(QURAN.read_text())
    counts: dict[int, int] = {}
    for entry in text:
        s = int(entry["id"])
        counts[s] = int(entry.get("total_verses") or len(entry.get("verses", [])))
    return counts


def mean_intra(D, group):
    pairs = [D[a][b] for i, a in enumerate(group) for b in group[i + 1 :]]
    return mean(pairs)


def main() -> None:
    verify_prereg()
    D = load_fr_matrix()
    verse_counts = load_verse_counts()
    print(f"Loaded FR matrix from {FR_MATRIX} (114×114)")
    print(f"Verse counts: total={sum(verse_counts.values())}; cluster verses = {[verse_counts.get(s, 0) for s in CLUSTER]}")

    obs = mean_intra(D, CLUSTER)
    print(f"\nObserved intra-cluster FR mean ({CLUSTER}): {obs:.5f}")

    rng_a = random.Random(SEED)
    rng_b = random.Random(SEED + 1)
    pool_no_q1 = [s for s in range(2, 115)]

    # Cell A: uniform-random 4-surah samples
    a_nulls = []
    for _ in range(N_PERM):
        a_nulls.append(mean_intra(D, rng_a.sample(pool_no_q1, 4)))
    p_a = sum(1 for x in a_nulls if x <= obs) / N_PERM

    # Cell B: length-matched (±20% of total verse-count)
    target_total = sum(verse_counts.get(s, 0) for s in CLUSTER)
    lo = target_total * 0.8
    hi = target_total * 1.2

    b_nulls = []
    rng_b_sampler = random.Random(SEED + 2)
    tries = 0
    while len(b_nulls) < N_PERM and tries < N_PERM * 200:
        sample = rng_b_sampler.sample(pool_no_q1, 4)
        total = sum(verse_counts.get(s, 0) for s in sample)
        if lo <= total <= hi:
            b_nulls.append(mean_intra(D, sample))
        tries += 1

    p_b = sum(1 for x in b_nulls if x <= obs) / max(1, len(b_nulls))

    # MW-5 positive control: 4-of-7 random sub-samples of HM cluster
    rng_pc = random.Random(SEED + 1)
    hm_sample = sorted(rng_pc.sample(HM_POSITIVE_CONTROL_POOL, 4))
    hm_obs = mean_intra(D, hm_sample)
    pc_nulls = []
    rng_pc_null = random.Random(SEED + 3)
    for _ in range(N_PERM):
        pc_nulls.append(mean_intra(D, rng_pc_null.sample(pool_no_q1, 4)))
    p_pc = sum(1 for x in pc_nulls if x <= hm_obs) / N_PERM

    cell_a_pass = p_a <= 0.025
    cell_b_pass = p_b <= 0.025
    pc_pass = p_pc <= 0.05

    if not pc_pass:
        verdict = "NULL-BROKEN (positive control failed)"
    elif cell_a_pass and cell_b_pass:
        verdict = "PASS-DIRECTED"
    elif cell_a_pass and not cell_b_pass:
        verdict = "DESCRIPTIVE-ONLY (length-confound suspected)"
    elif not cell_a_pass and cell_b_pass:
        verdict = "PARTIAL (length-matched only)"
    else:
        verdict = "NULL"

    out = {
        "id": "H-NEW-1301",
        "title": "IMPV-qrA 4-surah cluster Fisher-Rao cohesion",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "cluster": CLUSTER,
        "cluster_verse_counts": {s: verse_counts.get(s, 0) for s in CLUSTER},
        "cluster_total_verses": target_total,
        "obs_intra_cluster_FR_mean": obs,
        "cell_A_uniform_4_surah_null": {
            "n_perm": len(a_nulls),
            "null_mean": mean(a_nulls),
            "null_p5": sorted(a_nulls)[int(0.05 * len(a_nulls))],
            "p_perm": p_a,
            "pass": cell_a_pass,
        },
        "cell_B_length_matched_null": {
            "lo_total_verses": lo,
            "hi_total_verses": hi,
            "n_perm": len(b_nulls),
            "null_mean": mean(b_nulls) if b_nulls else None,
            "null_p5": sorted(b_nulls)[int(0.05 * len(b_nulls))] if b_nulls else None,
            "p_perm": p_b,
            "pass": cell_b_pass,
        },
        "MW5_positive_control": {
            "hm_subsample": hm_sample,
            "hm_obs": hm_obs,
            "p_pc": p_pc,
            "pc_pass": pc_pass,
        },
        "alpha_bon_per_cell": 0.025,
        "verdict": verdict,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nVerdict: {verdict}")
    print(f"Cell A uniform null: p={p_a:.5f}  null_mean={mean(a_nulls):.5f}  null_p5={sorted(a_nulls)[int(0.05*len(a_nulls))]:.5f}")
    print(f"Cell B length-matched: p={p_b:.5f}  null_mean={mean(b_nulls):.5f}  null_p5={sorted(b_nulls)[int(0.05*len(b_nulls))]:.5f}  (n_perm_realized={len(b_nulls)})")
    print(f"MW-5 PC: hm_subsample={hm_sample}  hm_obs={hm_obs:.5f}  p_pc={p_pc:.5f}  pass={pc_pass}")
    print(f"Wrote: {OUT}")


if __name__ == "__main__":
    main()
