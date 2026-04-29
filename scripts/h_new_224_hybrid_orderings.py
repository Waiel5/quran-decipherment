#!/usr/bin/env python3
"""H-NEW-224 — Hybrid orderings: mix mushaf + Nöldeke halves.

Pre-registered descriptive decomposition (Bonferroni k=1, α=0.05).

Hybrids (each a permutation of {1..114}):
  A = mushaf[0:57]   prefix + (Noldeke suffix with already-seen removed)
  B = Noldeke[0:57]  prefix + (mushaf  suffix with already-seen removed)
  C = mushaf[0:28]   prefix + (Noldeke suffix with already-seen removed)
  D = Noldeke[0:86]  prefix + (mushaf  suffix with already-seen removed)

D matrix inherited from H-NEW-111. Null: 10 000 uniform perms, seed 20260419.

Pre-reg SHA-256 emitted to stderr.
"""
import csv
import hashlib
import json
import math
import random
import statistics
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
PERMS = 10000
BONFERRONI_K = 1
ALPHA_BON = 0.05 / BONFERRONI_K

PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-224-hybrid-orderings-prereg.md'
H111_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111.json'
NOLDEKE_CSV = ROOT / 'data/revelation-order.csv'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-224.json'

# -----------------------------------------------------------------------------
# Pre-reg tamper-evidence
# -----------------------------------------------------------------------------
prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
h111_sha = hashlib.sha256(H111_JSON.read_bytes()).hexdigest()
print(f"prereg SHA-256:  {prereg_sha}", file=sys.stderr)
print(f"h-new-111 JSON SHA-256 (D matrix source): {h111_sha}", file=sys.stderr)
print(f"SEED = {SEED}", file=sys.stderr)
print(f"PERMS = {PERMS}", file=sys.stderr)
print(f"BONFERRONI_K = {BONFERRONI_K}, α_bon = {ALPHA_BON:.5f}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 1. Load D matrix from h-new-111.json
# -----------------------------------------------------------------------------
print("\nLoading D matrix from h-new-111.json ...", file=sys.stderr)
h111 = json.loads(H111_JSON.read_text())
D_up = h111['D_matrix_upper_triangular']
D = [[0.0] * 115 for _ in range(115)]
for i, j, d in D_up:
    D[i][j] = float(d)
    D[j][i] = float(d)
assert len(D_up) == 114 * 113 // 2, f"D upper-triangular has wrong size: {len(D_up)}"
print(f"  loaded {len(D_up)} pairs", file=sys.stderr)


def path_length(order):
    L = 0.0
    for i in range(len(order) - 1):
        L += D[order[i]][order[i + 1]]
    return L


# -----------------------------------------------------------------------------
# 2. Load orderings (mushaf + Nöldeke) from CSV
# -----------------------------------------------------------------------------
mushaf_to_noldeke = {}
with open(NOLDEKE_CSV, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        msid = int(row['mushaf_order'])
        mushaf_to_noldeke[msid] = int(row['noldeke_order'])

mushaf_order = list(range(1, 115))
noldeke_order = sorted(range(1, 115), key=lambda sid: mushaf_to_noldeke[sid])

L_mushaf = path_length(mushaf_order)
L_noldeke = path_length(noldeke_order)
print(f"\nL_mushaf   = {L_mushaf:.4f}", file=sys.stderr)
print(f"L_noldeke  = {L_noldeke:.4f}", file=sys.stderr)

# Cross-check vs stored H-NEW-111 values
L_mushaf_h111 = float(h111['primary']['L_mushaf'])
L_noldeke_h111 = float(h111['secondary_B']['L_noldeke'])
assert abs(L_mushaf - L_mushaf_h111) < 1e-4
assert abs(L_noldeke - L_noldeke_h111) < 1e-4


# -----------------------------------------------------------------------------
# 3. Build hybrid orderings
# -----------------------------------------------------------------------------
def hybrid(prefix_order, prefix_len, donor_order):
    """Take first prefix_len from prefix_order, then append donor_order
    with already-seen entries removed (preserving donor's relative order).
    Returns a permutation of {1..114}."""
    head = prefix_order[:prefix_len]
    seen = set(head)
    tail = [sid for sid in donor_order if sid not in seen]
    result = head + tail
    assert len(result) == 114
    assert set(result) == set(range(1, 115))
    return result


hyb_A = hybrid(mushaf_order, 57, noldeke_order)   # mushaf front 57 + noldeke tail
hyb_B = hybrid(noldeke_order, 57, mushaf_order)   # noldeke front 57 + mushaf tail
hyb_C = hybrid(mushaf_order, 28, noldeke_order)   # mushaf front 28 + noldeke tail 86
hyb_D = hybrid(noldeke_order, 86, mushaf_order)   # noldeke front 86 + mushaf tail 28

L_A = path_length(hyb_A)
L_B = path_length(hyb_B)
L_C = path_length(hyb_C)
L_D = path_length(hyb_D)

print(f"\nHybrid path lengths:", file=sys.stderr)
print(f"  A (mushaf[0:57] + noldeke tail):  L = {L_A:.4f}", file=sys.stderr)
print(f"  B (noldeke[0:57] + mushaf tail):  L = {L_B:.4f}", file=sys.stderr)
print(f"  C (mushaf[0:28] + noldeke tail):  L = {L_C:.4f}", file=sys.stderr)
print(f"  D (noldeke[0:86] + mushaf tail):  L = {L_D:.4f}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 4. Fresh null (seed 20260419, matches H-NEW-212 convention)
# -----------------------------------------------------------------------------
print(f"\nFresh null: {PERMS} perms, seed {SEED} ...", file=sys.stderr)
rng = random.Random(SEED)
null_L = []
base = list(range(1, 115))
for p in range(PERMS):
    perm = base[:]
    rng.shuffle(perm)
    null_L.append(path_length(perm))
    if (p + 1) % 2000 == 0:
        print(f"  perm {p+1}/{PERMS}", file=sys.stderr)

null_mean = statistics.mean(null_L)
null_sd = statistics.stdev(null_L)
null_sorted = sorted(null_L)


def q(sl, frac):
    n = len(sl)
    idx = max(0, min(n - 1, int(math.floor(frac * n))))
    return sl[idx]


null_quantiles = {
    'min': null_sorted[0],
    'q001': q(null_sorted, 0.001),
    'q01': q(null_sorted, 0.01),
    'q05': q(null_sorted, 0.05),
    'q50': q(null_sorted, 0.50),
    'q95': q(null_sorted, 0.95),
    'max': null_sorted[-1],
    'mean': null_mean,
    'sd': null_sd,
}

print(f"  null mean={null_mean:.4f} sd={null_sd:.4f}", file=sys.stderr)


def p_lower(L):
    n_le = sum(1 for x in null_L if x <= L)
    return (n_le + 1) / (PERMS + 1), n_le


# -----------------------------------------------------------------------------
# 5. Apply to hybrids + references
# -----------------------------------------------------------------------------
results = {}
for name, L, order in [
    ('mushaf', L_mushaf, mushaf_order),
    ('noldeke', L_noldeke, noldeke_order),
    ('hybrid_A_mushaf57_noldeke57', L_A, hyb_A),
    ('hybrid_B_noldeke57_mushaf57', L_B, hyb_B),
    ('hybrid_C_mushaf28_noldeke86', L_C, hyb_C),
    ('hybrid_D_noldeke86_mushaf28', L_D, hyb_D),
]:
    p, n_le = p_lower(L)
    z = (L - null_mean) / null_sd
    results[name] = {
        'L': L,
        'z': z,
        'n_perms_le': n_le,
        'p_one_sided_lower': p,
        'first20': order[:20],
        'last20': order[-20:],
    }
    print(f"  {name:32s}: L={L:.4f}  z={z:+.3f}  p={p:.6f}",
          file=sys.stderr)

# -----------------------------------------------------------------------------
# 6. Decomposition verdict
# -----------------------------------------------------------------------------
# Criterion-FRONT: L_A < L_B AND L_C < L_D  (mushaf front drives advantage)
# Criterion-BACK:  L_B < L_A AND L_D < L_C  (mushaf back drives advantage)
front_57 = L_A < L_B
front_28 = L_C < L_D
crit_front = front_57 and front_28
crit_back = (not front_57) and (not front_28)

verdict = (
    'FRONT-DRIVEN' if crit_front else
    'BACK-DRIVEN' if crit_back else
    'MIXED'
)
print(f"\n[57/57] mushaf-front wins?  {front_57}  (L_A={L_A:.4f}, L_B={L_B:.4f})",
      file=sys.stderr)
print(f"[28/86] mushaf-front wins?  {front_28}  (L_C={L_C:.4f}, L_D={L_D:.4f})",
      file=sys.stderr)
print(f"VERDICT: {verdict}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 7. Leaderboard
# -----------------------------------------------------------------------------
leaderboard = sorted(results.items(), key=lambda kv: kv[1]['L'])
print("\nRanked (shortest first):", file=sys.stderr)
for rank, (name, r) in enumerate(leaderboard, 1):
    tag = ""
    if name == 'mushaf':
        tag = "  <-- mushaf"
    elif name == 'noldeke':
        tag = "  <-- noldeke"
    print(f"  {rank}. {name:32s} L={r['L']:.4f} p={r['p_one_sided_lower']:.4f}{tag}",
          file=sys.stderr)

# -----------------------------------------------------------------------------
# 8. Pairwise deltas
# -----------------------------------------------------------------------------
deltas = {}
for name in ['hybrid_A_mushaf57_noldeke57', 'hybrid_B_noldeke57_mushaf57',
             'hybrid_C_mushaf28_noldeke86', 'hybrid_D_noldeke86_mushaf28']:
    L_h = results[name]['L']
    deltas[name] = {
        'L_minus_mushaf_raw': L_h - L_mushaf,
        'L_minus_mushaf_in_null_sd': (L_h - L_mushaf) / null_sd,
        'L_minus_noldeke_raw': L_h - L_noldeke,
        'L_minus_noldeke_in_null_sd': (L_h - L_noldeke) / null_sd,
    }

# -----------------------------------------------------------------------------
# 9. Write JSON
# -----------------------------------------------------------------------------
def round_floats(o, n=6):
    if isinstance(o, float):
        return round(o, n)
    if isinstance(o, dict):
        return {k: round_floats(v, n) for k, v in o.items()}
    if isinstance(o, list):
        return [round_floats(v, n) for v in o]
    return o


summary = {
    'finding_id': 'h-new-224',
    'title': 'Hybrid mushaf+Nöldeke orderings — which half carries the advantage?',
    'pre_reg_sha256': prereg_sha,
    'h_new_111_source_sha256': h111_sha,
    'seed': SEED,
    'permutations': PERMS,
    'bonferroni_k': BONFERRONI_K,
    'alpha_bon': ALPHA_BON,
    'date': '2026-04-17',
    'framing': 'DESCRIPTIVE',
    'rules_tuple': ('(no-tashkeel, QAC-STEM root tokens, QAC v0.4, '
                    'basmala-counted-only-in-surah-1, Hafs-Kufan, '
                    'D-matrix-inherited-from-H-NEW-111)'),
    'null_quantiles': null_quantiles,
    'results': results,
    'leaderboard_shortest_first': [
        {'rank': i + 1, 'name': n, 'L': r['L'], 'p': r['p_one_sided_lower']}
        for i, (n, r) in enumerate(leaderboard)
    ],
    'decomposition': {
        'criterion_front_57_mushaf_wins': front_57,
        'criterion_front_28_mushaf_wins': front_28,
        'crit_front_both': crit_front,
        'crit_back_both': crit_back,
        'verdict': verdict,
    },
    'pairwise_deltas_vs_references': deltas,
}
summary = round_floats(summary)
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"\nWrote: {OUT_JSON}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 10. Final stdout summary
# -----------------------------------------------------------------------------
print("\n" + "=" * 72, file=sys.stderr)
print("H-NEW-224 SUMMARY (descriptive hybrid decomposition)", file=sys.stderr)
print("=" * 72, file=sys.stderr)
print(f"  L_mushaf  = {L_mushaf:.4f}  (reference)", file=sys.stderr)
print(f"  L_noldeke = {L_noldeke:.4f}  (reference)", file=sys.stderr)
print(f"  L_A [mushaf-front-57 + nold-tail] = {L_A:.4f}", file=sys.stderr)
print(f"  L_B [nold-front-57 + mushaf-tail] = {L_B:.4f}", file=sys.stderr)
print(f"  L_C [mushaf-front-28 + nold-tail] = {L_C:.4f}", file=sys.stderr)
print(f"  L_D [nold-front-86 + mushaf-tail] = {L_D:.4f}", file=sys.stderr)
print(f"  VERDICT: {verdict}", file=sys.stderr)
print("=" * 72, file=sys.stderr)
