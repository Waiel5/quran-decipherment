#!/usr/bin/env python3
"""H-NEW-1395 — Ḥawāmīm-7 cluster Fisher-Rao cohesion test.

Pre-registration: findings/phase-b-hypotheses/prereg-h-new-1395-hawamim-cluster.md
SHA-locked. Direction one-tailed lower. Bonferroni α_corr = 0.025 (k=2 cells).
"""

import hashlib
import json
import random
import sys
from pathlib import Path
from statistics import mean

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/prereg-h-new-1395-hawamim-cluster.md"
EXPECTED_SHA = "06bc435a00d5622d29c8e3d459ffe8083e020aafa0ef9fa0eac83583ea9f296f"
FR_MATRIX = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
QURAN = ROOT / "quran-text/quran-no-tashkeel.json"
OUT = ROOT / "findings/phase-b-hypotheses/csv/h-new-1395.json"
SEED = 20260509
N_PERM = 10_000

CLUSTER = [40, 41, 42, 43, 44, 45, 46]
ADRAKA = [69, 74, 77, 82, 83, 86, 90, 97, 101, 104]
PC_K = 4
LENGTH_TOL = 0.20


def main():
    actual_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual_sha != EXPECTED_SHA:
        sys.exit(f"SHA mismatch: expected {EXPECTED_SHA}, got {actual_sha}")

    h111 = json.loads(FR_MATRIX.read_text())
    D = [[0.0] * 115 for _ in range(115)]
    for a, b, dist in h111["D_matrix_upper_triangular"]:
        D[a][b] = D[b][a] = dist

    text = json.loads(QURAN.read_text())
    vc = {int(e["id"]): int(e.get("total_verses") or len(e.get("verses", [])))
          for e in text}

    def mean_intra(group):
        ps = [D[a][b] for i, a in enumerate(group) for b in group[i + 1:]]
        return mean(ps)

    obs = mean_intra(CLUSTER)

    rng_a = random.Random(SEED)
    rng_b = random.Random(SEED + 2)
    rng_pc = random.Random(SEED + 3)

    pool = list(range(1, 115))

    # Cell A — uniform 7-of-114
    a_n = [mean_intra(rng_a.sample(pool, len(CLUSTER))) for _ in range(N_PERM)]
    p_a = sum(1 for x in a_n if x <= obs) / N_PERM

    # Cell B — length-matched
    target = sum(vc[s] for s in CLUSTER)
    lo, hi = target * (1 - LENGTH_TOL), target * (1 + LENGTH_TOL)
    b_n = []
    tries = 0
    while len(b_n) < N_PERM and tries < N_PERM * 400:
        s = rng_b.sample(pool, len(CLUSTER))
        if lo <= sum(vc[x] for x in s) <= hi:
            b_n.append(mean_intra(s))
        tries += 1
    p_b = sum(1 for x in b_n if x <= obs) / max(1, len(b_n))

    # MW-5 PC — 4-of-10 sub-sample of H-NEW-1190 cluster
    pc_pick = sorted(random.Random(SEED).sample(ADRAKA, PC_K))
    pc_obs = mean_intra(pc_pick)
    pc_n = [mean_intra(rng_pc.sample(pool, PC_K)) for _ in range(N_PERM)]
    p_pc = sum(1 for x in pc_n if x <= pc_obs) / N_PERM

    pc_pass = p_pc <= 0.05
    a_pass = p_a <= 0.025
    b_pass = p_b <= 0.025

    if not pc_pass:
        verdict = "NULL-BROKEN (PC failed)"
    elif a_pass and b_pass:
        verdict = "PASS-DIRECTED"
    elif a_pass and not b_pass:
        verdict = "DESCRIPTIVE-ONLY (length confound)"
    elif b_pass and not a_pass:
        verdict = "PARTIAL"
    else:
        verdict = "NULL"

    out = {
        "id": "H-NEW-1395",
        "title": "Hawamim 7-surah cluster {Q 40-46} FR-roots cohesion",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "cluster": CLUSTER,
        "verse_counts": {s: vc[s] for s in CLUSTER},
        "total_verses": target,
        "obs": obs,
        "alpha_bonf": 0.025,
        "cell_A": {
            "p": p_a,
            "null_mean": mean(a_n),
            "null_p5": sorted(a_n)[int(0.05 * len(a_n))],
            "pass": a_pass,
        },
        "cell_B": {
            "p": p_b,
            "null_mean": mean(b_n) if b_n else None,
            "null_p5": sorted(b_n)[int(0.05 * len(b_n))] if b_n else None,
            "pass": b_pass,
            "n": len(b_n),
            "length_tolerance": LENGTH_TOL,
        },
        "MW5_PC": {
            "pool": ADRAKA,
            "subsample": pc_pick,
            "pc_obs": pc_obs,
            "p_pc": p_pc,
            "pass": pc_pass,
        },
        "verdict": verdict,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"H-NEW-1395 verdict: {verdict}")
    print(f"  obs d̄(HM-7) = {obs:.4f}")
    print(f"  Cell A: p={p_a:.4f}  null_mean={mean(a_n):.4f}  pass={a_pass}")
    print(f"  Cell B: p={p_b:.4f}  n={len(b_n)}  pass={b_pass}")
    print(f"  MW5 PC: subsample={pc_pick}  p_pc={p_pc:.4f}  pass={pc_pass}")


if __name__ == "__main__":
    main()
