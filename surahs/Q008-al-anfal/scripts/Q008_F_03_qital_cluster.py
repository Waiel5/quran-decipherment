#!/usr/bin/env python3
"""
Q008-F-03 — qitāl-fī-sabīl-Allāh cluster {Q 8, 9, 47, 48, 61} FR-cohesion test.

Pre-reg SHA: fd442dbfd1dc245b7d931e2501fbd91e8fb89c27466439cc25e0f32fff92488f
Seed: 20260509
"""
import json
import hashlib
import numpy as np
from pathlib import Path

EXPECTED_PREREG_SHA = "fd442dbfd1dc245b7d931e2501fbd91e8fb89c27466439cc25e0f32fff92488f"
PREREG_PATH = Path(__file__).parent.parent / "preregs" / "Q008-F-03-qital-cluster-prereg.md"
SEED = 20260509
N_PERM = 10000
ALPHA_BON = 0.0125

# Verify pre-reg SHA at runtime
with open(PREREG_PATH, 'rb') as f:
    actual = hashlib.sha256(f.read()).hexdigest()
assert actual == EXPECTED_PREREG_SHA, f"SHA mismatch: expected {EXPECTED_PREREG_SHA}, got {actual}"

# Load FR matrix
QURAN_ROOT = Path('/Users/grey/Downloads/quran')
with open(QURAN_ROOT / 'findings/phase-b-hypotheses/csv/h-new-111.json') as f:
    h111 = json.load(f)

ut = h111['D_matrix_upper_triangular']
n = 114
M = np.full((n+1, n+1), np.nan)
for entry in ut:
    i, j, v = entry
    M[i, j] = v
    M[j, i] = v
np.fill_diagonal(M[1:, 1:], 0)

# Cluster
cluster = [8, 9, 47, 48, 61]
n_c = len(cluster)

# Pairwise FR within cluster
intra_pairs = []
for i in range(n_c):
    for j in range(i+1, n_c):
        intra_pairs.append((cluster[i], cluster[j], float(M[cluster[i], cluster[j]])))
D_intra = float(np.mean([d for _, _, d in intra_pairs]))

# Q 8 specific
q8_to_others = [(s, float(M[8, s])) for s in cluster if s != 8]
D_q8_cluster = float(np.mean([d for _, d in q8_to_others]))
D_q8_corpus = float(np.mean([float(M[8, s]) for s in range(1, n+1) if s != 8]))

# Member centrality
member_means = []
for member in cluster:
    d_m = [float(M[member, s]) for s in cluster if s != member]
    member_means.append((member, float(np.mean(d_m))))
member_means_sorted = sorted(member_means, key=lambda x: x[1])

# Permutation null A: 10000 random 5-subsets
np.random.seed(SEED)
null_intra_means = []
for _ in range(N_PERM):
    idx5 = np.random.choice(range(1, n+1), 5, replace=False)
    pair_d = []
    for i in range(5):
        for j in range(i+1, 5):
            pair_d.append(M[idx5[i], idx5[j]])
    null_intra_means.append(float(np.mean(pair_d)))
null_intra_means = np.array(null_intra_means)
p_intra = float(np.mean(null_intra_means <= D_intra))

# Permutation null B: 10000 random 4-subsets, Q 8 mean to each
null_q8_means = []
candidates = [s for s in range(1, n+1) if s != 8]
for _ in range(N_PERM):
    idx4 = np.random.choice(candidates, 4, replace=False)
    null_q8_means.append(float(np.mean([float(M[8, s]) for s in idx4])))
null_q8_means = np.array(null_q8_means)
p_q8 = float(np.mean(null_q8_means <= D_q8_cluster))

# Verdicts
H1_pass = p_intra <= ALPHA_BON
H2_pass = D_q8_cluster < D_q8_corpus

if H1_pass and H2_pass:
    verdict = "CONFIRMED"
elif H1_pass or H2_pass:
    verdict = "DIRECTIONAL"
else:
    verdict = "NULL"

out = {
    "test_id": "Q008-F-03",
    "title": "qitāl-fī-sabīl-Allāh cluster FR-cohesion test",
    "prereg_sha256": EXPECTED_PREREG_SHA,
    "prereg_sha256_verified": True,
    "seed": SEED,
    "n_perm": N_PERM,
    "alpha_bon": ALPHA_BON,
    "cluster": cluster,
    "intra_cluster_pairs": [(s1, s2, d) for s1, s2, d in intra_pairs],
    "D_intra": D_intra,
    "null_intra_mean": float(np.mean(null_intra_means)),
    "null_intra_std": float(np.std(null_intra_means)),
    "null_intra_min": float(np.min(null_intra_means)),
    "null_intra_max": float(np.max(null_intra_means)),
    "p_intra": p_intra,
    "D_q8_cluster": D_q8_cluster,
    "D_q8_corpus": D_q8_corpus,
    "diff_q8": D_q8_cluster - D_q8_corpus,
    "p_q8_specific": p_q8,
    "member_centrality_ranking": [
        {"surah": s, "mean_dist_to_others": d} for s, d in member_means_sorted
    ],
    "H1_pass": H1_pass,
    "H2_pass": H2_pass,
    "verdict": verdict,
    "interpretation": (
        "Cluster cohesion test: {Q 8, 9, 47, 48, 61} qitāl-fī-sabīl-Allāh thematic group. "
        "If cohesive at FR level, Bonferroni-2 should pass."
    ),
}

OUT_DIR = Path(__file__).parent.parent / "csv"
OUT_DIR.mkdir(exist_ok=True)
with open(OUT_DIR / "Q008-F-03.json", 'w') as f:
    json.dump(out, f, indent=2, ensure_ascii=False)

print(f"Q008-F-03 verdict: {verdict}")
print(f"  D_intra = {D_intra:.4f}")
print(f"  p_intra = {p_intra:.4f} (alpha_bon = {ALPHA_BON})")
print(f"  D_q8_cluster = {D_q8_cluster:.4f}, D_q8_corpus = {D_q8_corpus:.4f}, diff = {D_q8_cluster - D_q8_corpus:+.4f}")
print(f"  H1 pass: {H1_pass}, H2 pass: {H2_pass}")
print(f"  Q 8 cluster centrality rank: {next(i+1 for i, (s, _) in enumerate(member_means_sorted) if s == 8)}/5")
print(f"Output: {OUT_DIR / 'Q008-F-03.json'}")
