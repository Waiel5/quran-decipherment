#!/usr/bin/env python3
"""
Q064-F-01: Q 64 H-NEW-58c musabbiḥāt cluster membership (FR axis) + Q 62↔Q 64 imperfect-tense pair.

Pre-reg: preregs/Q064-F-01-musabbihat-cluster-membership-prereg.md
Source FR matrix: findings/phase-b-hypotheses/csv/h-new-111.json
Seed: 20260509
Bonferroni k=3, α_bon = 0.01667
"""
import json
import itertools
import random
import hashlib
import os
from pathlib import Path

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
PREREG = PROJECT_ROOT / "surahs" / "Q064-al-taghabun" / "preregs" / "Q064-F-01-musabbihat-cluster-membership-prereg.md"
H_NEW_111 = PROJECT_ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-111.json"
OUT = PROJECT_ROOT / "surahs" / "Q064-al-taghabun" / "csv" / "Q064-F-01.json"

SEED = 20260509
B = 10000
ALPHA_BON = 0.05 / 3
MUSABBIHAT_5 = [57, 59, 61, 62, 64]  # H-NEW-58c inner cluster

def sha256_of_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()

def load_fr_matrix():
    d = json.load(open(H_NEW_111))
    D = {}
    for i, j, dij in d["D_matrix_upper_triangular"]:
        D[(i, j)] = dij
        D[(j, i)] = dij
    return D

def main():
    random.seed(SEED)
    D = load_fr_matrix()

    # H1: D_musabb vs random-4-subset null (excluding Q 64)
    target = 64
    other_4 = [s for s in MUSABBIHAT_5 if s != target]
    D_musabb = sum(D[(target, s)] for s in other_4) / len(other_4)

    universe = [s for s in range(1, 115) if s != target]
    null_means = []
    for _ in range(B):
        sub = random.sample(universe, 4)
        null_means.append(sum(D[(target, s)] for s in sub) / len(sub))
    p_h1 = sum(1 for x in null_means if x <= D_musabb) / B
    null_mean = sum(null_means) / len(null_means)

    # H2: pair-rank of Q 62-Q 64 in all 6441 pair-distances
    all_pairs = sorted([D[(i, j)] for i in range(1, 115) for j in range(i + 1, 115)])
    d_62_64 = D[(62, 64)]
    rank = sum(1 for x in all_pairs if x <= d_62_64)
    pct_rank = rank / len(all_pairs) * 100
    h2_pass = pct_rank <= 5.0

    # H3: Q 64 within-cluster centroid-or-better
    cluster_pairs = [D[(a, b)] for a, b in itertools.combinations(MUSABBIHAT_5, 2)]
    M_intra = sum(cluster_pairs) / len(cluster_pairs)
    M_q64 = sum(D[(target, s)] for s in other_4) / len(other_4)  # = D_musabb
    h3_pass = M_q64 <= M_intra

    # Per-surah centrality within cluster
    centrality = []
    for s in MUSABBIHAT_5:
        others = [t for t in MUSABBIHAT_5 if t != s]
        m = sum(D[(s, t)] for t in others) / len(others)
        centrality.append({"surah": s, "mean_FR_to_others": m})
    centrality.sort(key=lambda r: r["mean_FR_to_others"])
    q64_rank_in_cluster = next(i for i, r in enumerate(centrality) if r["surah"] == 64) + 1

    # Pair table for Q 64 with each of {57, 59, 61, 62}
    pair_table = []
    for s in other_4:
        pair_table.append({
            "pair": [64, s],
            "FR": D[(64, s)],
            "tense_class": "imperfect" if s == 62 else "perfect",
        })

    # Verdict
    verdicts = {
        "H1_perm_p_le_alpha_bon": p_h1 <= ALPHA_BON,
        "H1_perm_p": p_h1,
        "H2_pair_rank_le_5pct": h2_pass,
        "H2_pair_pct_rank": pct_rank,
        "H3_within_cluster_centroid": h3_pass,
        "H3_M_q64": M_q64,
        "H3_M_intra": M_intra,
    }
    n_pass = sum([
        verdicts["H1_perm_p_le_alpha_bon"],
        verdicts["H2_pair_rank_le_5pct"],
        verdicts["H3_within_cluster_centroid"],
    ])
    if n_pass == 3:
        verdict = "CONFIRMED"
    elif n_pass >= 1:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL"

    out = {
        "test_id": "Q064-F-01",
        "title": "Q 64 musabbiḥāt cluster membership (FR axis) + Q 62↔Q 64 imperfect-tense pair",
        "prereg_sha256": sha256_of_file(PREREG),
        "seed": SEED,
        "n_perm": B,
        "bonferroni_k": 3,
        "alpha_bon": ALPHA_BON,
        "rules_tuple": "(no-tashkeel, FR-on-QAC-stem-roots-K=500-Dirichlet-α=0.5, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "data_source": str(H_NEW_111.relative_to(PROJECT_ROOT)),
        "musabbihat_5_cluster": MUSABBIHAT_5,
        "pair_table_q64": pair_table,
        "H1_D_musabb": D_musabb,
        "H1_null_mean": null_mean,
        "H1_null_min": min(null_means),
        "H1_null_max": max(null_means),
        "H1_perm_p": p_h1,
        "H2_d_q62_q64": d_62_64,
        "H2_pair_rank_in_6441": rank,
        "H2_pair_pct_rank": pct_rank,
        "H3_M_intra": M_intra,
        "H3_M_q64": M_q64,
        "centrality_within_cluster": centrality,
        "q64_centrality_rank": q64_rank_in_cluster,
        "verdicts": verdicts,
        "verdict": verdict,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=2)
    print(f"Wrote {OUT}")
    print(f"  D_musabb = {D_musabb:.4f}, null_mean = {null_mean:.4f}, perm_p = {p_h1:.4f}")
    print(f"  D(Q 62, Q 64) = {d_62_64:.4f}, pct_rank = {pct_rank:.2f}%")
    print(f"  M_intra = {M_intra:.4f}, M_q64 = {M_q64:.4f}, q64_in_cluster_rank = {q64_rank_in_cluster}/5")
    print(f"  VERDICT: {verdict}")

if __name__ == "__main__":
    main()
