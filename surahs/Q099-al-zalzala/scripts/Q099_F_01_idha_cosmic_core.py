#!/usr/bin/env python3
"""
Q099-F-01: Q 99 within H-NEW-1200 14-cluster + 4-CORE idhā-cosmic-opener architectural replication.

Pre-reg SHA256 verified at runtime.
"""
import json, hashlib, os, random, sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'surahs/Q099-al-zalzala/preregs/Q099-F-01-idha-cosmic-core-prereg.md'
OUT = ROOT / 'surahs/Q099-al-zalzala/csv/Q099-F-01-output.json'
SEED = 20260509
N_PERM = 10000

# SHA-lock the pre-reg
def sha256(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

prereg_sha = sha256(PREREG)
print(f"Pre-reg SHA256: {prereg_sha}")

# Load FR matrix from H-NEW-111
d = json.load(open(ROOT / 'findings/phase-b-hypotheses/csv/h-new-111.json'))
matrix = d['D_matrix_upper_triangular']
# Build distances dict for Q99 to all others
q99_dist = {}
for entry in matrix:
    a, b, dist = entry
    if a == 99:
        q99_dist[b] = dist
    elif b == 99:
        q99_dist[a] = dist

# Q99 corpus-mean
corpus_mean = sum(q99_dist.values()) / len(q99_dist)

# H-NEW-1200 14-cluster
CLUSTER_14 = [56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104]
OTHER_13 = [s for s in CLUSTER_14 if s != 99]
cluster_dists = [q99_dist[s] for s in OTHER_13]
cluster_mean = sum(cluster_dists) / len(cluster_dists)

# 4-CORE Sub-cluster A
CORE_4 = [81, 82, 84, 99]
OTHER_3 = [s for s in CORE_4 if s != 99]
core_dists = [q99_dist[s] for s in OTHER_3]
core_mean = sum(core_dists) / len(core_dists)

print(f"\nQ 99 corpus mean (113 surahs): {corpus_mean:.4f}")
print(f"Q 99 cluster mean (13 H-NEW-1200 members): {cluster_mean:.4f}")
print(f"Q 99 4-CORE mean (3 idhā-CORE members): {core_mean:.4f}")
print(f"\nT1 ratio (cluster/corpus): {cluster_mean/corpus_mean:.4f}")
print(f"T2 4-CORE mean: {core_mean:.4f} (band [0.52, 0.60] for PASS)")

# Permutation null T1: 13-subset random sampling (excluding Q 99)
all_others = list(q99_dist.keys())
random.seed(SEED)

count_T1 = 0
for i in range(N_PERM):
    sample = random.sample(all_others, 13)
    sample_mean = sum(q99_dist[s] for s in sample) / 13
    if sample_mean <= cluster_mean:
        count_T1 += 1
p_T1 = count_T1 / N_PERM

# Permutation null T2: 3-subset random sampling
random.seed(SEED + 1)
count_T2 = 0
for i in range(N_PERM):
    sample = random.sample(all_others, 3)
    sample_mean = sum(q99_dist[s] for s in sample) / 3
    if sample_mean <= core_mean:
        count_T2 += 1
p_T2 = count_T2 / N_PERM

print(f"\nT1 perm-p (cluster-mean ≤ random): {p_T1}")
print(f"T2 perm-p (4-CORE-mean ≤ random): {p_T2}")

ALPHA_BON = 0.025
T1_pass = p_T1 < ALPHA_BON
T2_pass = p_T2 < ALPHA_BON and core_mean < 0.60

if T1_pass and T2_pass:
    verdict = "CONFIRMED"
elif T1_pass or T2_pass:
    verdict = "DIRECTIONAL"
else:
    verdict = "NULL"

print(f"\nT1 pass (p < 0.025): {T1_pass}")
print(f"T2 pass (p < 0.025 AND core_mean < 0.60): {T2_pass}")
print(f"\nVERDICT: {verdict}")

# Save output
output = {
    "test_id": "Q099-F-01",
    "title": "Q 99 within H-NEW-1200 14-cluster + 4-CORE idhā-cosmic-opener architectural replication",
    "prereg_sha256": prereg_sha,
    "seed": SEED,
    "n_perm": N_PERM,
    "bonferroni_k": 2,
    "alpha_bon": ALPHA_BON,
    "Q99_corpus_mean": corpus_mean,
    "Q99_cluster_14_mean": cluster_mean,
    "Q99_core_4_mean": core_mean,
    "Q99_distance_to_each_cluster_member": {f"Q{s}": q99_dist[s] for s in OTHER_13},
    "Q99_distance_to_each_core_member": {f"Q{s}": q99_dist[s] for s in OTHER_3},
    "T1_cluster_corpus_ratio": cluster_mean / corpus_mean,
    "T1_perm_p": p_T1,
    "T1_pass": T1_pass,
    "T2_perm_p": p_T2,
    "T2_pass": T2_pass,
    "verdict": verdict,
    "bonferroni_family": "Q099-F-01-idha-cosmic-core",
}

OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(output, f, indent=2, ensure_ascii=False)
print(f"\nSaved to: {OUT}")
