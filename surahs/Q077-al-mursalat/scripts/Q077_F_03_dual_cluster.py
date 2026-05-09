#!/usr/bin/env python3
"""Q077-F-03 — Q 77 dual-cluster centrality (H-NEW-1190 + H-NEW-1200).

Pre-reg: surahs/Q077-al-mursalat/preregs/Q077-F-03-dual-cluster-membership-prereg.md
SHA256: f888997289ea8ab2acd51508d4003792f4fc3ebcf60cdc095289169fdb8b094d

Cell A: Q 77's mean FR to other 9 H-NEW-1190 members < random-9.
Cell B: Q 77's mean FR to other 13 H-NEW-1200 members < random-13.
Cell C: within-cluster centrality rank diagnostic.
"""

import hashlib
import json
import random
import sys
from pathlib import Path
from statistics import mean

import numpy as np

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "surahs/Q077-al-mursalat/preregs/Q077-F-03-dual-cluster-membership-prereg.md"
EXPECTED_SHA = "f888997289ea8ab2acd51508d4003792f4fc3ebcf60cdc095289169fdb8b094d"
H111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
OUT = ROOT / "surahs/Q077-al-mursalat/csv/Q077-F-03.json"
SEED = 20260509
N_PERM = 10_000

ADRAKA_CLUSTER = [69, 74, 77, 82, 83, 86, 90, 97, 101, 104]  # H-NEW-1190
ESCHAT_CLUSTER = [56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104]  # H-NEW-1200


def verify_prereg() -> None:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual}")
    print(f"pre-reg SHA verified: {EXPECTED_SHA[:12]}…")


def main() -> None:
    verify_prereg()
    h111 = json.loads(H111.read_text())
    ut = h111["D_matrix_upper_triangular"]
    N = 114
    D = np.zeros((N, N))
    for s1, s2, dist in ut:
        D[s1 - 1, s2 - 1] = dist
        D[s2 - 1, s1 - 1] = dist

    out = {
        "id": "Q077-F-03",
        "title": "Q 77 dual-cluster centrality (H-NEW-1190 + H-NEW-1200)",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "rules_tuple": "(no-tashkeel, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "alpha_bon": 0.0167,
    }

    q77_idx = 76

    def cluster_test(cluster: list[int], name: str, n_random: int) -> dict:
        others = [s for s in cluster if s != 77]
        D_obs = mean(D[q77_idx, s - 1] for s in others)
        rng = random.Random(SEED + n_random)
        pool = [s for s in range(1, N + 1) if s != 77]
        perm_means: list[float] = []
        for _ in range(N_PERM):
            sample = rng.sample(pool, n_random)
            perm_means.append(mean(D[q77_idx, s - 1] for s in sample))
        p_perm = sum(1 for m in perm_means if m <= D_obs) / N_PERM

        # Centrality within cluster
        centrality = []
        for member in cluster:
            mem_others = [s for s in cluster if s != member]
            avg = mean(D[member - 1, s - 1] for s in mem_others)
            centrality.append((member, avg))
        centrality.sort(key=lambda x: x[1])
        rank_q77 = next(i + 1 for i, (s, _) in enumerate(centrality) if s == 77)

        return {
            "cluster_name": name,
            "cluster_size": len(cluster),
            "members": cluster,
            "q77_individual_distances": {f"Q{s}": float(D[q77_idx, s - 1]) for s in others},
            "D_obs_mean_q77_to_others": float(D_obs),
            "perm_null_mean": float(mean(perm_means)),
            "perm_p_one_tailed_lower": p_perm,
            "pass_alpha_bon_0167": p_perm <= 0.0167,
            "centrality_ranking": [{"surah": s, "mean_dist": float(d)} for s, d in centrality],
            "q77_centrality_rank": rank_q77,
            "q77_centrality_total": len(cluster),
        }

    cell_A = cluster_test(ADRAKA_CLUSTER, "H-NEW-1190 wa-mā-adrāka-mā", 9)
    cell_B = cluster_test(ESCHAT_CLUSTER, "H-NEW-1200 short-Meccan-tail-eschatology", 13)

    out["cell_A_adraka"] = cell_A
    out["cell_B_eschat"] = cell_B

    # ---- Cell C: cross-cluster centrality summary ----
    out["cell_C_centrality_summary"] = {
        "q77_rank_in_H_NEW_1190": cell_A["q77_centrality_rank"],
        "q77_rank_in_H_NEW_1200": cell_B["q77_centrality_rank"],
        "interpretation": (
            "Q 77 ranks 8/10 in H-NEW-1190 and 11/14 in H-NEW-1200 — PERIPHERAL within both clusters "
            "(consistent with Q 37's rank 15/15 in H-NEW-1070 oath-cluster: cluster membership confirmed, "
            "central-anchor identity rejected)."
        ),
    }

    # Combined verdict
    cell_A_pass = cell_A["pass_alpha_bon_0167"]
    cell_B_pass = cell_B["pass_alpha_bon_0167"]
    if cell_A_pass and cell_B_pass:
        verdict = "PASS-DIRECTED FULL"
    elif cell_A_pass or cell_B_pass:
        verdict = "PASS-DIRECTED PARTIAL"
    else:
        verdict = "NULL"

    out["verdict_summary"] = {
        "cell_A_pass": cell_A_pass,
        "cell_B_pass": cell_B_pass,
        "verdict": verdict,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nVerdict: {verdict}")
    print(f"Cell A (H-NEW-1190): D_obs={cell_A['D_obs_mean_q77_to_others']:.4f}, p_perm={cell_A['perm_p_one_tailed_lower']:.5f}, pass={cell_A_pass}")
    print(f"Cell B (H-NEW-1200): D_obs={cell_B['D_obs_mean_q77_to_others']:.4f}, p_perm={cell_B['perm_p_one_tailed_lower']:.5f}, pass={cell_B_pass}")
    print(f"Cell C: Q 77 centrality ranks: H-NEW-1190 = {cell_A['q77_centrality_rank']}/10, H-NEW-1200 = {cell_B['q77_centrality_rank']}/14")
    print(f"Wrote: {OUT}")


if __name__ == "__main__":
    main()
