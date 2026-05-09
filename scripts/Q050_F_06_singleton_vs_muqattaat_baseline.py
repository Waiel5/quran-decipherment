#!/usr/bin/env python3
"""
Q050-F-06 — Singleton-letter triplet FR-cluster vs 28-muqaṭṭāʿat baseline.

Pre-reg: surahs/Q050-qaf/preregs/Q050-F-06-singleton-vs-muqattaat-baseline-prereg.md
Pre-reg SHA256 (locked): d058275499fc9f287f950a981b86ff63d49084fe0b3000732dbc35b7d7368ee7

Tests whether {Q 38, Q 50, Q 68} mean pairwise FR is tighter (lower) than:
  (a) full-corpus random 3-surah triplets (N=10000)
  (b) 26 non-singleton muqaṭṭāʿat surahs, exhaustive C(26,3) triplets

Bonferroni-2; α_per_cell = 0.025. Direction-locked LOW-S.
"""

import hashlib
import itertools
import json
import os
import random
import sys
from pathlib import Path

# ---------------- SHA lock ----------------
PRE_REG = Path(__file__).resolve().parents[1] / "surahs" / "Q050-qaf" / "preregs" / "Q050-F-06-singleton-vs-muqattaat-baseline-prereg.md"
EXPECTED_SHA = "d058275499fc9f287f950a981b86ff63d49084fe0b3000732dbc35b7d7368ee7"
actual_sha = hashlib.sha256(PRE_REG.read_bytes()).hexdigest()
if actual_sha != EXPECTED_SHA:
    print(f"FATAL: pre-reg SHA mismatch.\n  expected: {EXPECTED_SHA}\n  actual:   {actual_sha}")
    sys.exit(1)

SEED = 20260509
N_PERM_A = 10000
N_SURAHS = 114

SINGLETON = (38, 50, 68)
# 29 muqaṭṭāʿat-opener surahs (canonical, al-Suyūṭī al-Itqān)
MUQATTAAT = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
             36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
NON_SINGLETON_MUQATTAAT = sorted(MUQATTAAT - set(SINGLETON))  # 26 surahs
assert len(NON_SINGLETON_MUQATTAAT) == 26

# ---------------- Load FR matrix ----------------
ROOT = Path(__file__).resolve().parents[1]
H111 = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-111.json"
h111 = json.loads(H111.read_text())
D = [[0.0] * (N_SURAHS + 1) for _ in range(N_SURAHS + 1)]
for entry in h111["D_matrix_upper_triangular"]:
    i, j, dist = entry
    D[i][j] = dist
    D[j][i] = dist

def mean_pairwise(triplet):
    a, b, c = triplet
    return (D[a][b] + D[a][c] + D[b][c]) / 3.0

# ---------------- Observed ----------------
S_obs = mean_pairwise(SINGLETON)

# ---------------- Null A: full-corpus random triplets ----------------
rng = random.Random(SEED)
all_surahs = list(range(1, N_SURAHS + 1))
null_a_values = []
n_drawn = 0
attempted = 0
while n_drawn < N_PERM_A and attempted < N_PERM_A * 10:
    attempted += 1
    trip = tuple(sorted(rng.sample(all_surahs, 3)))
    if set(trip) == set(SINGLETON):
        continue  # exclude the test triplet itself
    null_a_values.append(mean_pairwise(trip))
    n_drawn += 1

null_a_mean = sum(null_a_values) / len(null_a_values)
null_a_sd = (sum((x - null_a_mean) ** 2 for x in null_a_values) / len(null_a_values)) ** 0.5
n_le_obs_a = sum(1 for x in null_a_values if x <= S_obs)
percentile_a = n_le_obs_a / len(null_a_values)

# ---------------- Null B: exhaustive non-singleton-muqaṭṭāʿat triplets ----------------
null_b_values = []
for trip in itertools.combinations(NON_SINGLETON_MUQATTAAT, 3):
    null_b_values.append(mean_pairwise(trip))
n_triplets_b = len(null_b_values)
assert n_triplets_b == 2600

null_b_mean = sum(null_b_values) / n_triplets_b
null_b_sd = (sum((x - null_b_mean) ** 2 for x in null_b_values) / n_triplets_b) ** 0.5
n_le_obs_b = sum(1 for x in null_b_values if x <= S_obs)
percentile_b = n_le_obs_b / n_triplets_b

# ---------------- Verdict ----------------
ALPHA_BON = 0.025
direction_a_ok = percentile_a < 0.50
direction_b_ok = percentile_b < 0.50
pass_a = percentile_a < ALPHA_BON
pass_b = percentile_b < ALPHA_BON
pre_commit_violation = not (direction_a_ok and direction_b_ok)

if pass_a and pass_b:
    verdict = "DUAL-CONFIRMED"
elif pass_a or pass_b:
    verdict = "PARTIAL"
elif direction_a_ok and direction_b_ok:
    verdict = "DIRECTIONAL"
else:
    verdict = "NULL"
if pre_commit_violation:
    verdict += "-PRE-COMMIT-VIOLATION"

# ---------------- Write JSON ----------------
out = {
    "finding_id": "Q050-F-06",
    "prereg_sha256": EXPECTED_SHA,
    "date_run": "2026-05-09",
    "rules_tuple": "(no-tashkeel, QAC-STEM root tokens, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
    "seed": SEED,
    "n_perm_a": N_PERM_A,
    "n_triplets_b": n_triplets_b,
    "bonferroni_k": 2,
    "alpha_bon": ALPHA_BON,
    "singleton_triplet": list(SINGLETON),
    "non_singleton_muqattaat": NON_SINGLETON_MUQATTAAT,
    "S_obs": round(S_obs, 6),
    "null_a_full_corpus": {
        "mean": round(null_a_mean, 6),
        "sd": round(null_a_sd, 6),
        "percentile": round(percentile_a, 6),
        "n_le_obs": n_le_obs_a,
        "n_total": len(null_a_values),
    },
    "null_b_muqattaat_only": {
        "mean": round(null_b_mean, 6),
        "sd": round(null_b_sd, 6),
        "percentile": round(percentile_b, 6),
        "n_le_obs": n_le_obs_b,
        "n_total": n_triplets_b,
    },
    "pass_a_bonferroni": pass_a,
    "pass_b_bonferroni": pass_b,
    "direction_a_locked_low": direction_a_ok,
    "direction_b_locked_low": direction_b_ok,
    "pre_commit_violation": pre_commit_violation,
    "verdict": verdict,
}
OUT = ROOT / "surahs" / "Q050-qaf" / "csv" / "Q050-F-06.json"
OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
print(f"Q050-F-06: VERDICT={verdict}")
print(f"  S_obs={S_obs:.4f}")
print(f"  null_a: mean={null_a_mean:.4f}, percentile={percentile_a:.4f}")
print(f"  null_b: mean={null_b_mean:.4f}, percentile={percentile_b:.4f}")
print(f"  output: {OUT.relative_to(ROOT)}")
