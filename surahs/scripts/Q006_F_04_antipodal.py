#!/usr/bin/env python3
"""Q006-F-04 — Q 6 ↔ Q 21 architectural antipodal-pair FR-distance test.

Pre-reg: surahs/Q006-al-anam/Q006-F-04-q6-q21-antipodal-prereg.md
Pre-reg SHA-256 (locked): bc63c8ee92e634997c59a3788c69bd8c09fa1b542441db0f067873ac752ec1c0
Direction: ABOVE-CORPUS-MEAN (genre-separation hypothesis, LOCKED)
Bonferroni k=1, alpha_bon=0.05
Rules-tuple: (no-tashkeel, QAC-STEM-root, top-500-Dirichlet-alpha=0.5, L1-normalize, Fisher-Rao, Hafs-Kufan, Mashriqi)
"""
import hashlib
import json
import math
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'surahs/Q006-al-anam/Q006-F-04-q6-q21-antipodal-prereg.md'
EXPECTED_SHA = 'bc63c8ee92e634997c59a3788c69bd8c09fa1b542441db0f067873ac752ec1c0'
H111 = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111.json'
OUT = ROOT / 'surahs/Q006-al-anam/csv/Q006-F-04.json'

sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
assert sha == EXPECTED_SHA, f'pre-reg SHA mismatch: {sha} != {EXPECTED_SHA}'
print(f'pre-reg SHA verified: {sha}', file=sys.stderr)

# Reconstruct 114x114 FR distance matrix from upper-triangular list
N = 114
D = [[0.0] * N for _ in range(N)]
h = json.load(open(H111))
for entry in h['D_matrix_upper_triangular']:
    i, j, dist = entry
    D[i - 1][j - 1] = D[j - 1][i - 1] = dist

# Cell A: d(Q6, Q21)
d_q6q21 = D[5][20]

# Corpus pairwise distance distribution (upper-triangular)
all_pairs = [D[i][j] for i in range(N) for j in range(i + 1, N)]
corpus_mean = sum(all_pairs) / len(all_pairs)
corpus_median = sorted(all_pairs)[len(all_pairs) // 2]
corpus_var = sum((d - corpus_mean) ** 2 for d in all_pairs) / len(all_pairs)
corpus_sd = math.sqrt(corpus_var)

# Cell B: rank of d(Q6, Q21) within Q6's distances to other 113 surahs (rank 1 = closest)
q6_dists = [(j, D[5][j]) for j in range(N) if j != 5]
q6_dists_sorted = sorted(q6_dists, key=lambda x: x[1])
rank_in_q6 = next(r + 1 for r, (j, _) in enumerate(q6_dists_sorted) if j == 20)

# Cell C: rank of d(Q6, Q21) within Q21's distances
q21_dists = [(j, D[20][j]) for j in range(N) if j != 20]
q21_dists_sorted = sorted(q21_dists, key=lambda x: x[1])
rank_in_q21 = next(r + 1 for r, (j, _) in enumerate(q21_dists_sorted) if j == 5)

# Q6's nearest 5
q6_nearest_5 = [(j + 1, d) for j, d in q6_dists_sorted[:5]]
# Q21's nearest 5
q21_nearest_5 = [(j + 1, d) for j, d in q21_dists_sorted[:5]]

# Verdict per pre-reg §3
diff = d_q6q21 - corpus_mean
diff_sd = diff / corpus_sd if corpus_sd > 0 else 0.0
above_mean = d_q6q21 > corpus_mean
above_median = d_q6q21 > corpus_median

if above_mean and above_median:
    if diff_sd > 0.5:
        verdict = 'CONFIRMED-strong'
    else:
        verdict = 'CONFIRMED'
elif above_mean:
    verdict = 'DIRECTIONAL'
elif d_q6q21 <= corpus_mean - corpus_sd:
    verdict = 'PRE_COMMIT_VIOLATION'
else:
    verdict = 'NULL'

result = {
    'test_id': 'Q006-F-04',
    'pre_reg_sha': EXPECTED_SHA,
    'pre_reg_sha_verified': True,
    'seed': 20260507,
    'direction_locked': 'ABOVE-CORPUS-MEAN',
    'bonferroni_k': 1,
    'alpha_bon': 0.05,
    'rules_tuple': '(no-tashkeel, QAC-STEM-root, top-500-Dirichlet-alpha=0.5, L1-normalize, Fisher-Rao, Hafs-Kufan, Mashriqi)',
    'cell_A_d_q6_q21': d_q6q21,
    'corpus_pairwise_mean': corpus_mean,
    'corpus_pairwise_median': corpus_median,
    'corpus_pairwise_sd': corpus_sd,
    'diff_from_mean': diff,
    'diff_in_sd_units': diff_sd,
    'cell_B_q6q21_rank_within_q6_distances': rank_in_q6,
    'cell_C_q6q21_rank_within_q21_distances': rank_in_q21,
    'q6_nearest_5_surahs': q6_nearest_5,
    'q21_nearest_5_surahs': q21_nearest_5,
    'q6_isolation_mean_d_to_5_nearest': sum(d for _, d in q6_nearest_5) / 5,
    'q21_isolation_mean_d_to_5_nearest': sum(d for _, d in q21_nearest_5) / 5,
    'verdict': verdict,
    'honest_limits': [
        'FR-distance from H-NEW-111 upper-triangular matrix.',
        'Corpus baseline includes all 6,441 unique pair-distances; not length-matched.',
        'Q 6 and Q 21 are both Meccan; mid-Meccan baseline would be a more conservative test.',
        'Single-pipeline FR-on-stem-roots-top-500-Dirichlet-0.5; alternative metrics may rank differently.',
    ],
}

OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f'Q006-F-04: d(Q6,Q21) = {d_q6q21:.4f}; corpus_mean = {corpus_mean:.4f} (sd = {corpus_sd:.4f})', file=sys.stderr)
print(f'  diff = {diff:+.4f} ({diff_sd:+.3f} SD)', file=sys.stderr)
print(f'  Cell B rank-within-Q6: {rank_in_q6}/113; Cell C rank-within-Q21: {rank_in_q21}/113', file=sys.stderr)
print(f'Verdict: {verdict}', file=sys.stderr)
print(f'Output: {OUT}', file=sys.stderr)
