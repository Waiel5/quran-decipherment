#!/usr/bin/env python3
"""Q024-F-07: Q 24 mean Fisher-Rao distance to UAS top-10 vs corpus (LOCKED pre-reg).

Tests whether Q 24 clusters with the other 9 UAS top-10 surahs on
Fisher-Rao distance. Permutation null over random 9-subsets.

Rules-tuple (inherited from H-NEW-111):
  no-tashkeel, QAC-STEM-roots-top-500, Dirichlet-α=0.5, L1-normalized
  probability vectors, FR-angular distance, Hafs-Kufan, mushaf-order.

Data: findings/phase-b-hypotheses/csv/h-new-111.json + h-new-840.json.
"""
import json, hashlib, os, random
import numpy as np

PROJECT = '/Users/grey/Downloads/quran'
PREREG = f"{PROJECT}/surahs/Q024-al-nur/preregs/Q024-F-07-fr-clustering-with-uas-top10-prereg.md"
EXPECTED_SHA = "9cc455db7a524c5b28a67c69d9bf4937c963d9c8056cc820cad08f53a55420de"
FR = f"{PROJECT}/findings/phase-b-hypotheses/csv/h-new-111.json"
UAS = f"{PROJECT}/findings/phase-b-hypotheses/csv/h-new-840.json"
OUT = f"{PROJECT}/surahs/Q024-al-nur/csv/Q024-F-07.json"

SEED = 20260509
N_PERM = 10000
ALPHA_BONF = 0.0125

# 1. SHA-lock
sha = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
print(f"Pre-reg SHA256:    {sha}")
print(f"Expected:          {EXPECTED_SHA}")
if sha != EXPECTED_SHA:
    raise SystemExit("FAIL: pre-reg SHA mismatch — abort.")
print("OK SHA verified.\n")

# 2. Load FR matrix
with open(FR) as f:
    fr = json.load(f)
D = np.zeros((115, 115))
for r in fr['D_matrix_upper_triangular']:
    i, j, d = r
    D[i][j] = d
    D[j][i] = d
print(f"FR matrix loaded, shape {D.shape}.")

# 3. Load UAS top-10 from h-new-840.json
with open(UAS) as f:
    uas = json.load(f)
top10 = [x['surah'] for x in uas['top_15'][:10]]
print(f"UAS top-10 (from h-new-840): {top10}")
assert 24 in top10, "Q 24 must be in the UAS top-10."

others_in_top10 = [s for s in top10 if s != 24]
all_others = [s for s in range(1, 115) if s != 24]

# 4. Observed Δ
d_top9 = float(np.mean([D[24][s] for s in others_in_top10]))
d_corpus = float(np.mean([D[24][s] for s in all_others]))
delta = d_top9 - d_corpus
print(f"\nQ 24 mean FR to UAS top-9 (excl self): {d_top9:.6f}")
print(f"Q 24 mean FR to all corpus (113):      {d_corpus:.6f}")
print(f"Observed Δ (top9 − corpus):            {delta:+.6f}")

# 5. Permutation null: random 9-subsets of all_others
rng = random.Random(SEED)
deltas = []
for _ in range(N_PERM):
    subset = rng.sample(all_others, 9)
    d_sub = np.mean([D[24][s] for s in subset])
    deltas.append(d_sub - d_corpus)
deltas = np.array(deltas)
# Two-sided p
p_two = float(np.mean(np.abs(deltas) >= abs(delta)))
# One-sided p (lower-tail, since direction is Δ < 0)
p_one = float(np.mean(deltas <= delta))
print(f"\nPermutation null: n_perm={N_PERM}, seed={SEED}")
print(f"  p_one-sided (Δ ≤ observed): {p_one:.4f}")
print(f"  p_two-sided:                {p_two:.4f}")
print(f"  Bonferroni α (k=4):         {ALPHA_BONF}")

# 6. Per-pair printout
print("\nPer-pair FR distances Q 24 → UAS top-9 (sorted ascending):")
for s in sorted(others_in_top10, key=lambda x: D[24][x]):
    print(f"  Q 24 ↔ Q{s:>3}: FR = {D[24][s]:.4f}")

# 7. Verdict
if delta < 0:
    if p_one < ALPHA_BONF:
        verdict = "CONFIRMED"
    elif p_one < 0.05:
        verdict = "DIRECTIONAL"
    else:
        verdict = "WEAK-DIRECTIONAL"
else:
    verdict = "NULL-pre-commit-violation"
print(f"\nVerdict: {verdict} (direction Δ {'<' if delta < 0 else '>'} 0; p_one-sided = {p_one:.4f})")

# 8. Write JSON
out = {
    'finding_id': 'Q024-F-07',
    'pre_reg_sha256': sha,
    'seed': SEED,
    'date': '2026-05-09',
    'rules_tuple': fr.get('rules_tuple'),
    'uas_top10': top10,
    'q24_mean_fr_to_top9': d_top9,
    'q24_mean_fr_to_corpus': d_corpus,
    'delta_top9_minus_corpus': delta,
    'p_one_sided_lower': p_one,
    'p_two_sided': p_two,
    'alpha_bonferroni': ALPHA_BONF,
    'n_perm': N_PERM,
    'per_pair_fr': {str(s): float(D[24][s]) for s in others_in_top10},
    'verdict': verdict,
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, 'w') as f:
    json.dump(out, f, indent=2)
print(f"\nWrote {OUT}")
