#!/usr/bin/env python3
"""H-NEW-151 — single-letter muq sub-cluster under char-4-gram.

Pre-registered single-test (Bonferroni k=1, α_bon=0.05):
  H_1: mean FR-char4gram distance (Q 38, Q 50, Q 68) is LOWER than
       mean FR-char4gram distance between these singletons and other 26
       muq surahs. Permutation null (shuffle singleton-assignment).
       1-sided lower-tail.

Seed 20260417. Deterministic.
"""
import hashlib
import json
import random
import statistics
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260417
N_PERMS = 10000

H111B_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111b.json'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-151-single-letter-muq-char4gram-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-151.json'

prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)

# Load char-4-gram FR D-matrix
h111b = json.loads(H111B_JSON.read_text())
D = {}
for e in h111b['D_matrix_upper_triangular']:
    i, j, d = int(e[0]), int(e[1]), float(e[2])
    D[(i, j)] = D[(j, i)] = d

MUQ_SURAHS = [2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29,
              30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68]
SINGLETON = [38, 50, 68]
NON_SINGLE = [s for s in MUQ_SURAHS if s not in SINGLETON]
assert len(MUQ_SURAHS) == 29
assert len(SINGLETON) == 3
assert len(NON_SINGLE) == 26

def within_pairs_mean(singles):
    pairs = [(singles[0], singles[1]), (singles[0], singles[2]), (singles[1], singles[2])]
    return statistics.mean(D[(i, j)] for i, j in pairs)

def between_mean(singles, non_singles):
    return statistics.mean(D[(s, ns)] for s in singles for ns in non_singles)

# Observed
d_within = within_pairs_mean(SINGLETON)
d_between = between_mean(SINGLETON, NON_SINGLE)
delta_obs = d_within - d_between
print(f"d_within (Q 38, 50, 68): {d_within:.4f}", file=sys.stderr)
print(f"d_between (singletons to other 26 muq): {d_between:.4f}", file=sys.stderr)
print(f"delta_obs = {delta_obs:+.4f}", file=sys.stderr)

# Show individual pair distances
print(f"\nPairwise distances among singletons:", file=sys.stderr)
print(f"  Q 38 <-> Q 50: {D[(38,50)]:.4f}", file=sys.stderr)
print(f"  Q 38 <-> Q 68: {D[(38,68)]:.4f}", file=sys.stderr)
print(f"  Q 50 <-> Q 68: {D[(50,68)]:.4f}", file=sys.stderr)

# Permutation null
rng = random.Random(SEED)
null_deltas = []
for _ in range(N_PERMS):
    shuffled = MUQ_SURAHS[:]
    rng.shuffle(shuffled)
    null_singles = shuffled[:3]
    null_non = shuffled[3:]
    d_w = within_pairs_mean(null_singles)
    d_b = between_mean(null_singles, null_non)
    null_deltas.append(d_w - d_b)

# 1-sided lower-tail
p_one_sided = sum(1 for d in null_deltas if d <= delta_obs) / N_PERMS
null_mean = statistics.mean(null_deltas)
null_sd = statistics.stdev(null_deltas)
z = (delta_obs - null_mean) / null_sd

print(f"\nNull (10K perms):", file=sys.stderr)
print(f"  null mean delta: {null_mean:+.4f}", file=sys.stderr)
print(f"  null SD: {null_sd:.4f}", file=sys.stderr)
print(f"  z-score: {z:.3f}", file=sys.stderr)
print(f"  1-sided lower-tail p: {p_one_sided:.4f}", file=sys.stderr)

# Verdict
if p_one_sided < 0.05:
    verdict = "REPLICATED"
elif p_one_sided < 0.10:
    verdict = "PARTIAL"
else:
    verdict = "NULL"

print(f"\n" + "=" * 70, file=sys.stderr)
print(f"H-NEW-146 root finding: Q 38/50/68 closer at p=0.031", file=sys.stderr)
print(f"H-NEW-151 char-4-gram replication: delta={delta_obs:+.4f} p={p_one_sided:.4f} z={z:.2f}", file=sys.stderr)
print(f"VERDICT: {verdict}", file=sys.stderr)
print("=" * 70, file=sys.stderr)

# Write JSON
summary = {
    'finding_id': 'h-new-151',
    'title': 'Single-letter muq sub-cluster under char-4-gram',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'date': '2026-04-17',
    'feature_space': 'char-4-gram (H-NEW-111b)',
    'bonferroni': {'k': 1, 'alpha_bon': 0.05, 'family': 'h-new-151-single-letter-muq-char4gram'},
    'd_within_pairs': {
        '(38,50)': D[(38,50)],
        '(38,68)': D[(38,68)],
        '(50,68)': D[(50,68)],
        'mean': d_within,
    },
    'd_between_mean': d_between,
    'delta_observed': delta_obs,
    'permutation_null': {
        'n_perms': N_PERMS,
        'null_mean_delta': null_mean,
        'null_sd': null_sd,
        'z_score': z,
        'p_one_sided_lower_tail': p_one_sided,
    },
    'parent_h_new_146_Cell_C_p': 0.031,
    'parent_feature_space': 'QAC-STEM root top-500',
    'verdict': verdict,
}
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False, default=str))
print(f"\nWrote: {OUT_JSON}", file=sys.stderr)
