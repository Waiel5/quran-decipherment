#!/usr/bin/env python3
"""H-NEW-223 — Edge-by-edge decomposition of H-NEW-212 mushaf-vs-Nöldeke gap.

Descriptive (Bonferroni k=1). Seed 20260419. Reuses Fisher-Rao distance
matrix D from H-NEW-111 (=inherited by H-NEW-212).

Given
    mushaf ordering M = [1, 2, 3, ..., 114]
    Nöldeke ordering N = [n_0, n_1, ..., n_113]
we compute
    mushaf_edge[k]  = D[ M[k], M[k+1] ]   for k in 0..112
    noldeke_edge[k] = D[ N[k], N[k+1] ]   for k in 0..112
and rank edges by
    delta[k] = mushaf_edge[k] - noldeke_edge[k]
(negative = mushaf shorter at that position-slot; positive = mushaf longer).

NB: This is a position-wise comparison of two independent 113-edge paths
over the same D matrix; it is NOT a claim that surah-pair (M[k],M[k+1])
in mushaf is "the same edge" as (N[k],N[k+1]) in Nöldeke. The interest
is diagnostic: at which local slots does each path rack up its length?

Outputs (under scratch/h-new-223/):
  h-new-223-edges.csv       per-k: slot, mushaf_pair, noldeke_pair,
                             mushaf_edge, noldeke_edge, delta
  h-new-223-top10-mushaf-wins.csv   delta most-negative (mushaf shorter)
  h-new-223-top10-noldeke-wins.csv  delta most-positive (mushaf longer)
  h-new-223-summary.json    aggregate stats
"""
import csv
import hashlib
import json
import statistics
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419  # descriptive — not used for any RNG draws here
BONFERRONI_K = 1  # descriptive; no hypothesis test

H111_JSON   = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111.json'
NOLDEKE_CSV = ROOT / 'data/revelation-order.csv'
OUT_DIR     = ROOT / 'scratch/h-new-223'
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_EDGES   = OUT_DIR / 'h-new-223-edges.csv'
OUT_TOP10_M = OUT_DIR / 'h-new-223-top10-mushaf-wins.csv'
OUT_TOP10_N = OUT_DIR / 'h-new-223-top10-noldeke-wins.csv'
OUT_SUMMARY = OUT_DIR / 'h-new-223-summary.json'

# ---- Provenance ------------------------------------------------------------
h111_sha    = hashlib.sha256(H111_JSON.read_bytes()).hexdigest()
noldeke_sha = hashlib.sha256(NOLDEKE_CSV.read_bytes()).hexdigest()
print(f"H-NEW-111 JSON SHA-256 (D source): {h111_sha}", file=sys.stderr)
print(f"revelation-order.csv SHA-256:      {noldeke_sha}", file=sys.stderr)
print(f"SEED = {SEED}  (descriptive only; no perms)", file=sys.stderr)
print(f"BONFERRONI_K = {BONFERRONI_K}  (descriptive)", file=sys.stderr)

# ---- 1. Load D matrix (114x114, indices 1..114) ----------------------------
h111 = json.loads(H111_JSON.read_text())
D_up = h111['D_matrix_upper_triangular']
D = [[0.0] * 115 for _ in range(115)]
for i, j, d in D_up:
    D[i][j] = float(d)
    D[j][i] = float(d)
assert len(D_up) == 114 * 113 // 2 == 6441
L_mushaf_h111  = float(h111['primary']['L_mushaf'])
L_noldeke_h111 = float(h111['secondary_B']['L_noldeke'])

def path_length(order):
    return sum(D[order[i]][order[i + 1]] for i in range(len(order) - 1))

# ---- 2. Build orderings ---------------------------------------------------
mushaf_order = list(range(1, 115))  # [1..114]

mushaf_to_noldeke = {}
with open(NOLDEKE_CSV, encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        mushaf_to_noldeke[int(row['mushaf_order'])] = int(row['noldeke_order'])

noldeke_order = sorted(range(1, 115), key=lambda sid: mushaf_to_noldeke[sid])

L_mushaf  = path_length(mushaf_order)
L_noldeke = path_length(noldeke_order)
assert abs(L_mushaf  - L_mushaf_h111)  < 1e-4, "mushaf L mismatch vs H-NEW-111"
assert abs(L_noldeke - L_noldeke_h111) < 1e-4, "nöldeke L mismatch vs H-NEW-111"
GAP = L_noldeke - L_mushaf  # positive: mushaf is the shorter path
print(f"L_mushaf  = {L_mushaf:.4f}", file=sys.stderr)
print(f"L_noldeke = {L_noldeke:.4f}", file=sys.stderr)
print(f"GAP (L_noldeke - L_mushaf) = {GAP:+.4f}", file=sys.stderr)

# ---- 3. Edge arrays -------------------------------------------------------
N_EDGES = 113
assert len(mushaf_order) - 1 == N_EDGES == len(noldeke_order) - 1

edges = []
for k in range(N_EDGES):
    a_m, b_m = mushaf_order[k], mushaf_order[k + 1]
    a_n, b_n = noldeke_order[k], noldeke_order[k + 1]
    e_m = D[a_m][b_m]
    e_n = D[a_n][b_n]
    edges.append({
        'slot_k': k,
        'mushaf_a': a_m, 'mushaf_b': b_m, 'mushaf_edge': e_m,
        'noldeke_a': a_n, 'noldeke_b': b_n, 'noldeke_edge': e_n,
        'delta_m_minus_n': e_m - e_n,
    })

# Sanity
sum_m = sum(e['mushaf_edge']  for e in edges)
sum_n = sum(e['noldeke_edge'] for e in edges)
sum_delta = sum(e['delta_m_minus_n'] for e in edges)
assert abs(sum_m - L_mushaf)  < 1e-6
assert abs(sum_n - L_noldeke) < 1e-6
assert abs(sum_delta - (L_mushaf - L_noldeke)) < 1e-6

# ---- 4. Per-edge CSV ------------------------------------------------------
with open(OUT_EDGES, 'w', newline='', encoding='utf-8') as f:
    w = csv.writer(f)
    w.writerow(['slot_k',
                'mushaf_a', 'mushaf_b', 'mushaf_edge',
                'noldeke_a', 'noldeke_b', 'noldeke_edge',
                'delta_m_minus_n'])
    for e in edges:
        w.writerow([e['slot_k'],
                    e['mushaf_a'], e['mushaf_b'], f"{e['mushaf_edge']:.6f}",
                    e['noldeke_a'], e['noldeke_b'], f"{e['noldeke_edge']:.6f}",
                    f"{e['delta_m_minus_n']:+.6f}"])
print(f"wrote {OUT_EDGES}", file=sys.stderr)

# ---- 5. Top-10 mushaf-wins (delta most negative) --------------------------
sorted_asc  = sorted(edges, key=lambda e: e['delta_m_minus_n'])         # mushaf wins
sorted_desc = sorted(edges, key=lambda e: -e['delta_m_minus_n'])        # nöldeke wins

def write_top(path, rows):
    with open(path, 'w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)
        w.writerow(['rank', 'slot_k',
                    'mushaf_pair', 'mushaf_edge',
                    'noldeke_pair', 'noldeke_edge',
                    'delta_m_minus_n'])
        for i, e in enumerate(rows, 1):
            w.writerow([i, e['slot_k'],
                        f"{e['mushaf_a']}→{e['mushaf_b']}",  f"{e['mushaf_edge']:.6f}",
                        f"{e['noldeke_a']}→{e['noldeke_b']}", f"{e['noldeke_edge']:.6f}",
                        f"{e['delta_m_minus_n']:+.6f}"])

write_top(OUT_TOP10_M, sorted_asc[:10])
write_top(OUT_TOP10_N, sorted_desc[:10])
print(f"wrote {OUT_TOP10_M}", file=sys.stderr)
print(f"wrote {OUT_TOP10_N}", file=sys.stderr)

# ---- 6. Aggregate summary -------------------------------------------------
deltas = [e['delta_m_minus_n'] for e in edges]
n_mushaf_shorter  = sum(1 for d in deltas if d < 0)
n_mushaf_longer   = sum(1 for d in deltas if d > 0)
n_tied            = sum(1 for d in deltas if d == 0)
sum_mushaf_wins   = sum(d for d in deltas if d < 0)   # negative contribution
sum_noldeke_wins  = sum(d for d in deltas if d > 0)   # positive contribution
# Net should equal L_mushaf - L_noldeke = -GAP
net = sum_mushaf_wins + sum_noldeke_wins
assert abs(net - (-GAP)) < 1e-6

summary = {
    'finding_id': 'h-new-223',
    'title': 'Edge-by-edge decomp of H-NEW-212 mushaf-vs-Nöldeke Fisher-Rao gap',
    'h_new_111_source_sha256': h111_sha,
    'revelation_order_csv_sha256': noldeke_sha,
    'seed': SEED,
    'bonferroni_k': BONFERRONI_K,
    'date': '2026-04-17',
    'rules_tuple': ('(no-tashkeel, QAC-STEM root tokens, QAC v0.4, '
                    'basmala-counted-only-in-surah-1, Hafs-Kufan, '
                    'D-matrix-inherited-from-H-NEW-111)'),
    'L_mushaf':  round(L_mushaf,  4),
    'L_noldeke': round(L_noldeke, 4),
    'GAP_noldeke_minus_mushaf':   round(GAP, 4),
    'n_edges': N_EDGES,
    'n_slots_mushaf_shorter': n_mushaf_shorter,
    'n_slots_mushaf_longer':  n_mushaf_longer,
    'n_slots_tied':           n_tied,
    'sum_delta_where_mushaf_wins':  round(sum_mushaf_wins, 6),
    'sum_delta_where_noldeke_wins': round(sum_noldeke_wins, 6),
    'net_sum_delta_m_minus_n': round(net, 6),
    'mean_delta':   round(statistics.mean(deltas), 6),
    'stdev_delta':  round(statistics.stdev(deltas), 6),
    'median_delta': round(statistics.median(deltas), 6),
    'min_delta':    round(min(deltas), 6),
    'max_delta':    round(max(deltas), 6),
    'top10_mushaf_wins': [
        {'rank': i + 1, 'slot_k': e['slot_k'],
         'mushaf_pair': f"{e['mushaf_a']}→{e['mushaf_b']}",
         'noldeke_pair': f"{e['noldeke_a']}→{e['noldeke_b']}",
         'mushaf_edge':  round(e['mushaf_edge'],  6),
         'noldeke_edge': round(e['noldeke_edge'], 6),
         'delta':        round(e['delta_m_minus_n'], 6)}
        for i, e in enumerate(sorted_asc[:10])
    ],
    'top10_noldeke_wins': [
        {'rank': i + 1, 'slot_k': e['slot_k'],
         'mushaf_pair': f"{e['mushaf_a']}→{e['mushaf_b']}",
         'noldeke_pair': f"{e['noldeke_a']}→{e['noldeke_b']}",
         'mushaf_edge':  round(e['mushaf_edge'],  6),
         'noldeke_edge': round(e['noldeke_edge'], 6),
         'delta':        round(e['delta_m_minus_n'], 6)}
        for i, e in enumerate(sorted_desc[:10])
    ],
    'interpretation_caveat': (
        'Position-slot comparison only. Slot k in mushaf is pair '
        '(M[k],M[k+1]); slot k in Nöldeke is (N[k],N[k+1]). These are '
        'different surah pairs unless by coincidence. Sign of delta '
        'indicates which ordering has the shorter Fisher-Rao hop at '
        'position k. Net across 113 slots equals L_mushaf − L_noldeke.'),
}

OUT_SUMMARY.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"wrote {OUT_SUMMARY}", file=sys.stderr)

# ---- 7. Stdout digest -----------------------------------------------------
print("\n" + "=" * 72, file=sys.stderr)
print("H-NEW-223 SUMMARY", file=sys.stderr)
print("=" * 72, file=sys.stderr)
print(f"  L_mushaf={L_mushaf:.4f}  L_noldeke={L_noldeke:.4f}  gap={GAP:+.4f}",
      file=sys.stderr)
print(f"  slots mushaf-shorter: {n_mushaf_shorter}/{N_EDGES}", file=sys.stderr)
print(f"  slots mushaf-longer:  {n_mushaf_longer}/{N_EDGES}",  file=sys.stderr)
print(f"  slots tied:           {n_tied}/{N_EDGES}",           file=sys.stderr)
print(f"  sum(Δ | mushaf wins)  = {sum_mushaf_wins:+.4f}", file=sys.stderr)
print(f"  sum(Δ | nöldeke wins) = {sum_noldeke_wins:+.4f}", file=sys.stderr)
print(f"  net sum Δ             = {net:+.4f}   [= L_mushaf - L_noldeke]",
      file=sys.stderr)
print(f"  mean Δ={statistics.mean(deltas):+.6f}  sd={statistics.stdev(deltas):.6f}",
      file=sys.stderr)
print("\n  TOP-10 mushaf beats nöldeke (most-negative Δ):", file=sys.stderr)
for i, e in enumerate(sorted_asc[:10], 1):
    print(f"    {i:2d}. slot {e['slot_k']:3d}: "
          f"mushaf {e['mushaf_a']:3d}→{e['mushaf_b']:3d} "
          f"(d={e['mushaf_edge']:.4f})  vs  "
          f"nöld {e['noldeke_a']:3d}→{e['noldeke_b']:3d} "
          f"(d={e['noldeke_edge']:.4f})  Δ={e['delta_m_minus_n']:+.4f}",
          file=sys.stderr)
print("\n  TOP-10 nöldeke beats mushaf (most-positive Δ):", file=sys.stderr)
for i, e in enumerate(sorted_desc[:10], 1):
    print(f"    {i:2d}. slot {e['slot_k']:3d}: "
          f"mushaf {e['mushaf_a']:3d}→{e['mushaf_b']:3d} "
          f"(d={e['mushaf_edge']:.4f})  vs  "
          f"nöld {e['noldeke_a']:3d}→{e['noldeke_b']:3d} "
          f"(d={e['noldeke_edge']:.4f})  Δ={e['delta_m_minus_n']:+.4f}",
          file=sys.stderr)
print("=" * 72, file=sys.stderr)
