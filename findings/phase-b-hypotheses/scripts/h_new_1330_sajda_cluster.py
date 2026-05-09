#!/usr/bin/env python3
"""H-NEW-1330 — Sajda-surahs 14-surah cluster Fisher-Rao cohesion.

Pre-reg: findings/phase-b-hypotheses/h-new-1330-sajda-surahs-cluster-prereg.md
SHA256:  f56fd6446618b37485a6765f44d340e57888697eaa512ad876a95b48cbdc774f
"""

import hashlib
import json
import random
import sys
from pathlib import Path
from statistics import mean

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-1330-sajda-surahs-cluster-prereg.md"
EXPECTED_SHA = "f56fd6446618b37485a6765f44d340e57888697eaa512ad876a95b48cbdc774f"
FR_MATRIX = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
QURAN = ROOT / "quran-text/quran-no-tashkeel.json"
OUT = ROOT / "findings/phase-b-hypotheses/csv/h-new-1330.json"
SEED = 20260509
N_PERM = 10_000

SAJDA_CLUSTER = [7, 13, 16, 17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96]
H1200_CLUSTER = [56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104]


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
    return {int(e["id"]): int(e.get("total_verses") or len(e.get("verses", []))) for e in text}


def mean_intra(D, group):
    pairs = [D[a][b] for i, a in enumerate(group) for b in group[i + 1 :]]
    return mean(pairs)


def main() -> None:
    verify_prereg()
    D = load_fr_matrix()
    verse_counts = load_verse_counts()
    print(f"Loaded FR matrix from {FR_MATRIX}")

    obs = mean_intra(D, SAJDA_CLUSTER)
    cluster_total_verses = sum(verse_counts[s] for s in SAJDA_CLUSTER)
    print(f"\nObserved sajda-cluster intra mean ({SAJDA_CLUSTER}): {obs:.5f}")
    print(f"Cluster total verses: {cluster_total_verses}")

    rng_a = random.Random(SEED)
    rng_b = random.Random(SEED + 2)
    pool_no_q1 = list(range(2, 115))

    # Cell A
    a_nulls = [mean_intra(D, rng_a.sample(pool_no_q1, len(SAJDA_CLUSTER))) for _ in range(N_PERM)]
    p_a = sum(1 for x in a_nulls if x <= obs) / N_PERM

    # Cell B: ±15%
    lo = cluster_total_verses * 0.85
    hi = cluster_total_verses * 1.15
    b_nulls = []
    tries = 0
    while len(b_nulls) < N_PERM and tries < N_PERM * 200:
        sample = rng_b.sample(pool_no_q1, len(SAJDA_CLUSTER))
        total = sum(verse_counts[s] for s in sample)
        if lo <= total <= hi:
            b_nulls.append(mean_intra(D, sample))
        tries += 1
    p_b = sum(1 for x in b_nulls if x <= obs) / max(1, len(b_nulls))

    # MW-5 PC: H-NEW-1200 cluster (full 14 surahs)
    pc_obs = mean_intra(D, H1200_CLUSTER)
    rng_pc = random.Random(SEED + 3)
    pc_nulls = [mean_intra(D, rng_pc.sample(pool_no_q1, len(H1200_CLUSTER))) for _ in range(N_PERM)]
    p_pc = sum(1 for x in pc_nulls if x <= pc_obs) / N_PERM

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
        "id": "H-NEW-1330",
        "title": "Sajda-surahs 14-surah cluster Fisher-Rao cohesion",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "cluster": SAJDA_CLUSTER,
        "cluster_verse_counts": {s: verse_counts[s] for s in SAJDA_CLUSTER},
        "cluster_total_verses": cluster_total_verses,
        "obs_intra_cluster_FR_mean": obs,
        "cell_A_uniform_null": {
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
            "source": "H-NEW-1200 14-surah eschatology cluster (CONFIRMED p=0.00030)",
            "cluster": H1200_CLUSTER,
            "pc_obs_mean": pc_obs,
            "pc_null_mean": mean(pc_nulls),
            "pc_null_p5": sorted(pc_nulls)[int(0.05 * len(pc_nulls))],
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
    print(f"Cell B length-matched: p={p_b:.5f}  null_mean={mean(b_nulls):.5f}  null_p5={sorted(b_nulls)[int(0.05*len(b_nulls))]:.5f}  (n={len(b_nulls)})")
    print(f"MW-5 PC (H-NEW-1200 full 14): pc_obs={pc_obs:.5f}  p_pc={p_pc:.5f}  pass={pc_pass}")
    print(f"Wrote: {OUT}")


if __name__ == "__main__":
    main()
