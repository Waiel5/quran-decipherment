#!/usr/bin/env python3
"""
Q064-F-02: Q 64 H-NEW-1080 short-Medinan-block (Q 57-66) FR-centrality test.

Pre-reg: preregs/Q064-F-02-short-medinan-centrality-prereg.md
Source FR matrix: findings/phase-b-hypotheses/csv/h-new-111.json
Seed: 20260509
Bonferroni k=2, α_bon = 0.025
"""
import json
import random
import hashlib
from pathlib import Path

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
PREREG = PROJECT_ROOT / "surahs" / "Q064-al-taghabun" / "preregs" / "Q064-F-02-short-medinan-centrality-prereg.md"
H_NEW_111 = PROJECT_ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-111.json"
OUT = PROJECT_ROOT / "surahs" / "Q064-al-taghabun" / "csv" / "Q064-F-02.json"

SEED = 20260509
B = 10000
ALPHA_BON = 0.025
SHORT_MEDINAN_BLOCK = list(range(57, 67))  # Q 57-66

def sha256_of_file(p):
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
    target = 64

    other_9 = [s for s in SHORT_MEDINAN_BLOCK if s != target]
    D_block = sum(D[(target, s)] for s in other_9) / len(other_9)

    # H1 null: random 9-subset means (excluding Q 64)
    universe = [s for s in range(1, 115) if s != target]
    null_means = []
    for _ in range(B):
        sub = random.sample(universe, 9)
        null_means.append(sum(D[(target, s)] for s in sub) / len(sub))
    null_mean = sum(null_means) / len(null_means)
    p_h1 = sum(1 for x in null_means if x <= D_block) / B

    # H2: centrality rank within block
    centrality = []
    for s in SHORT_MEDINAN_BLOCK:
        others = [t for t in SHORT_MEDINAN_BLOCK if t != s]
        m = sum(D[(s, t)] for t in others) / len(others)
        centrality.append({"surah": s, "mean_FR_to_others_in_block": m})
    centrality.sort(key=lambda r: r["mean_FR_to_others_in_block"])
    q64_rank = next(i for i, r in enumerate(centrality) if r["surah"] == 64) + 1
    h2_pass = q64_rank <= 5

    # Per-surah pair table
    pair_table = []
    for s in other_9:
        pair_table.append({"pair": [64, s], "FR": D[(64, s)]})

    verdicts = {
        "H1_perm_p_le_alpha_bon": p_h1 <= ALPHA_BON,
        "H1_perm_p": p_h1,
        "H2_centrality_rank_le_5": h2_pass,
        "H2_q64_rank": q64_rank,
    }
    n_pass = sum([verdicts["H1_perm_p_le_alpha_bon"], verdicts["H2_centrality_rank_le_5"]])
    if n_pass == 2:
        verdict = "CONFIRMED"
    elif n_pass == 1:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL"

    out = {
        "test_id": "Q064-F-02",
        "title": "Q 64 short-Medinan-block (Q 57-66) FR-centrality test",
        "prereg_sha256": sha256_of_file(PREREG),
        "seed": SEED,
        "n_perm": B,
        "bonferroni_k": 2,
        "alpha_bon": ALPHA_BON,
        "rules_tuple": "(no-tashkeel, FR-on-QAC-stem-roots-K=500-Dirichlet-α=0.5, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "data_source": str(H_NEW_111.relative_to(PROJECT_ROOT)),
        "short_medinan_block": SHORT_MEDINAN_BLOCK,
        "H1_D_block": D_block,
        "H1_null_mean": null_mean,
        "H1_null_min": min(null_means),
        "H1_null_max": max(null_means),
        "H1_perm_p": p_h1,
        "H2_q64_rank_in_block": q64_rank,
        "centrality_within_block": centrality,
        "pair_table_q64": pair_table,
        "verdicts": verdicts,
        "verdict": verdict,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    json.dump(out, open(OUT, "w"), ensure_ascii=False, indent=2)
    print(f"Wrote {OUT}")
    print(f"  D_block = {D_block:.4f}, null_mean = {null_mean:.4f}, perm_p = {p_h1:.4f}")
    print(f"  Q 64 centrality rank in block = {q64_rank}/10")
    print(f"  VERDICT: {verdict}")

if __name__ == "__main__":
    main()
