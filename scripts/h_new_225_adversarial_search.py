#!/usr/bin/env python3
"""H-NEW-225 — Adversarial search: can we find ANY ordering shorter than mushaf?

Method:
  1. Reload the 114x114 Fisher-Rao D-matrix from H-NEW-111.
  2. MW-5: verify L_mushaf = 85.76 +/- 0.01
  3. Run 2-opt initialized AT the mushaf ordering; report whether ANY
     2-opt swap reduces L below 85.76.
  4. Run SA + 2-opt from 100 random starts (seeds 20260419..20260518).
  5. L_search_min := min over all searches (incl. parent L_2opt = 77.47).
  6. Compute gap_abs, gap_rel vs mushaf. PASS if gap_rel > 1.01.

Pre-reg: findings/phase-b-hypotheses/h-new-225-adversarial-search-prereg.md
Seed:    20260419
Bonferroni: k=1 (existence cell; descriptive alpha=0.05)
"""
import hashlib
import json
import math
import random
import statistics
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
N_RESTARTS = 100
SA_ITERS = 10000
SA_T0 = 5.0
SA_COOL = 0.995

PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-225-adversarial-search-prereg.md'
PARENT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111.json'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-225.json'

prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
print(f"SEED = {SEED}", file=sys.stderr)
print(f"N_RESTARTS = {N_RESTARTS}", file=sys.stderr)
print(f"SA_ITERS = {SA_ITERS}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 1. Load D-matrix from H-NEW-111 JSON
# ---------------------------------------------------------------------------
print("\nLoading parent D-matrix from H-NEW-111...", file=sys.stderr)
parent = json.loads(PARENT_JSON.read_text())
D = [[0.0] * 115 for _ in range(115)]
for entry in parent['D_matrix_upper_triangular']:
    i, j, d = entry
    i = int(i)
    j = int(j)
    D[i][j] = float(d)
    D[j][i] = float(d)
print(f"  loaded {len(parent['D_matrix_upper_triangular'])} pairs", file=sys.stderr)

L_MUSHAF_PARENT = float(parent['primary']['L_mushaf'])
L_2OPT_PARENT = float(parent['secondary_A']['L_2opt_best'])
print(f"  L_mushaf (parent report) = {L_MUSHAF_PARENT:.6f}", file=sys.stderr)
print(f"  L_2opt   (parent report) = {L_2OPT_PARENT:.6f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 2. Path-length helper
# ---------------------------------------------------------------------------
def path_length(order):
    L = 0.0
    for i in range(len(order) - 1):
        L += D[order[i]][order[i + 1]]
    return L

mushaf_order = list(range(1, 115))
L_mushaf = path_length(mushaf_order)
print(f"\nMW-5: reloaded L_mushaf = {L_mushaf:.6f}", file=sys.stderr)
mw5_pass = abs(L_mushaf - L_MUSHAF_PARENT) < 0.01
print(f"  MW-5 {'PASS' if mw5_pass else 'FAIL'}", file=sys.stderr)
assert mw5_pass, "MW-5 failed: D-matrix reload doesn't reproduce parent L_mushaf"

# ---------------------------------------------------------------------------
# 3. 2-opt local search (open path, best-improvement within each pass)
# ---------------------------------------------------------------------------
def two_opt(path, max_passes=200):
    path = path[:]
    n = len(path)
    passes = 0
    total_improvements = 0
    cumulative_delta = 0.0
    first_improving_swap = None
    while passes < max_passes:
        passes += 1
        best_delta = 0.0
        best_ij = None
        for i in range(0, n - 2):
            a = path[i]
            b = path[i + 1]
            dab = D[a][b]
            for j in range(i + 2, n):
                c = path[j]
                if j + 1 < n:
                    d = path[j + 1]
                    delta = (D[a][c] + D[b][d]) - (dab + D[c][d])
                else:
                    delta = D[a][c] - dab
                if delta < best_delta - 1e-12:
                    best_delta = delta
                    best_ij = (i, j)
        if best_ij is None:
            break
        i, j = best_ij
        path[i + 1:j + 1] = list(reversed(path[i + 1:j + 1]))
        total_improvements += 1
        cumulative_delta += best_delta
        if first_improving_swap is None:
            first_improving_swap = {'i': i, 'j': j, 'delta': best_delta}
    return path, passes, total_improvements, cumulative_delta, first_improving_swap

# ---------------------------------------------------------------------------
# 4. Adversarial 2-opt from the mushaf ordering itself
# ---------------------------------------------------------------------------
print("\n=== STEP 1: 2-opt initialized AT mushaf ===", file=sys.stderr)
mushaf_2opt_path, passes_m, n_impr_m, cum_delta_m, first_swap_m = two_opt(mushaf_order)
L_mushaf_2opt = path_length(mushaf_2opt_path)
print(f"  passes: {passes_m}", file=sys.stderr)
print(f"  improvements: {n_impr_m}", file=sys.stderr)
print(f"  cumulative delta: {cum_delta_m:.6f}", file=sys.stderr)
print(f"  first improving swap: {first_swap_m}", file=sys.stderr)
print(f"  L after 2-opt from mushaf: {L_mushaf_2opt:.6f}", file=sys.stderr)
mushaf_is_2opt_local = (n_impr_m == 0)
print(f"  mushaf is 2-opt local optimum? {mushaf_is_2opt_local}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 5. Simulated annealing + 2-opt polish from N random starts
# ---------------------------------------------------------------------------
def sa_search(start_seed, start_order, iters=SA_ITERS, T0=SA_T0, cool=SA_COOL):
    rng = random.Random(start_seed)
    cur = start_order[:]
    n = len(cur)
    cur_L = path_length(cur)
    best_L = cur_L
    best_order = cur[:]
    T = T0
    for it in range(iters):
        # Proposal: 50% 2-opt reversal, 50% simple swap
        if rng.random() < 0.5:
            # 2-opt reversal: pick i<j, reverse cur[i+1..j]
            i = rng.randint(0, n - 3)
            j = rng.randint(i + 2, n - 1)
            a = cur[i]
            b = cur[i + 1]
            c = cur[j]
            if j + 1 < n:
                d = cur[j + 1]
                delta = (D[a][c] + D[b][d]) - (D[a][b] + D[c][d])
            else:
                delta = D[a][c] - D[a][b]
            # Accept?
            if delta < 0 or rng.random() < math.exp(-delta / max(T, 1e-9)):
                cur[i + 1:j + 1] = list(reversed(cur[i + 1:j + 1]))
                cur_L += delta
                if cur_L < best_L - 1e-12:
                    best_L = cur_L
                    best_order = cur[:]
        else:
            # Simple swap of two positions i, j (non-adjacent to simplify delta calc — just recompute full L)
            i = rng.randint(0, n - 1)
            j = rng.randint(0, n - 1)
            if i == j:
                continue
            cur[i], cur[j] = cur[j], cur[i]
            new_L = path_length(cur)
            delta = new_L - cur_L
            if delta < 0 or rng.random() < math.exp(-delta / max(T, 1e-9)):
                cur_L = new_L
                if cur_L < best_L - 1e-12:
                    best_L = cur_L
                    best_order = cur[:]
            else:
                # revert
                cur[i], cur[j] = cur[j], cur[i]
        T *= cool
    # Polish best with 2-opt
    polished, _, _, _, _ = two_opt(best_order, max_passes=100)
    L_polished = path_length(polished)
    if L_polished < best_L:
        best_L = L_polished
        best_order = polished
    return best_L, best_order

print(f"\n=== STEP 2: SA + 2-opt from {N_RESTARTS} random starts ===", file=sys.stderr)
restart_results = []
L_sa_min = float('inf')
best_sa_order = None
best_sa_seed = None

rng_master = random.Random(SEED)
for k in range(N_RESTARTS):
    seed_k = SEED + k  # 20260419..20260518
    rng_k = random.Random(seed_k)
    start = list(range(1, 115))
    rng_k.shuffle(start)
    L_best, order_best = sa_search(seed_k, start, iters=SA_ITERS, T0=SA_T0, cool=SA_COOL)
    restart_results.append({'seed': seed_k, 'L': L_best})
    if L_best < L_sa_min:
        L_sa_min = L_best
        best_sa_order = order_best[:]
        best_sa_seed = seed_k
    if (k + 1) % 10 == 0:
        L_so_far = L_sa_min
        print(f"  restart {k+1}/{N_RESTARTS}, best so far = {L_so_far:.6f} (seed {best_sa_seed})", file=sys.stderr)

restart_Ls = [r['L'] for r in restart_results]
print(f"\n  SA + 2-opt over {N_RESTARTS} restarts:", file=sys.stderr)
print(f"    min    = {min(restart_Ls):.6f}", file=sys.stderr)
print(f"    median = {statistics.median(restart_Ls):.6f}", file=sys.stderr)
print(f"    mean   = {statistics.mean(restart_Ls):.6f}", file=sys.stderr)
print(f"    max    = {max(restart_Ls):.6f}", file=sys.stderr)
print(f"    sd     = {statistics.stdev(restart_Ls):.6f}", file=sys.stderr)
print(f"  best seed  = {best_sa_seed}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 6. Incorporate parent 2-opt bound (77.47)
# ---------------------------------------------------------------------------
L_search_min = min(L_mushaf_2opt, L_sa_min, L_2OPT_PARENT)
print(f"\n=== L_search_min = {L_search_min:.6f} ===", file=sys.stderr)
print(f"  (min of mushaf-2opt={L_mushaf_2opt:.4f}, SA-best={L_sa_min:.4f}, parent-2opt={L_2OPT_PARENT:.4f})", file=sys.stderr)

gap_abs = L_mushaf - L_search_min
gap_rel = L_mushaf / L_search_min
print(f"  gap_abs (L_mushaf - L_search_min) = {gap_abs:.6f}", file=sys.stderr)
print(f"  gap_rel (L_mushaf / L_search_min) = {gap_rel:.6f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 7. Rank mushaf among (mushaf, 100 restarts, mushaf-2opt)
# ---------------------------------------------------------------------------
all_Ls = sorted([L_mushaf] + restart_Ls + [L_mushaf_2opt])
rank_mushaf = all_Ls.index(L_mushaf) + 1
n_shorter_than_mushaf = sum(1 for L in all_Ls if L < L_mushaf)
print(f"\n  mushaf rank in pooled ({len(all_Ls)}) set (1=shortest): {rank_mushaf}", file=sys.stderr)
print(f"  #{{searches shorter than mushaf}} = {n_shorter_than_mushaf}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 8. Decision
# ---------------------------------------------------------------------------
if gap_rel <= 1.01:
    verdict = 'SURPRISE-NULL'  # mushaf is unbeatable
elif gap_rel > 1.15:
    verdict = 'EXTREME-GAP'
else:
    verdict = 'PASS'
print(f"\n  verdict: {verdict}", file=sys.stderr)

tightens_parent = L_search_min < L_2OPT_PARENT
if tightens_parent:
    print(f"  TIGHTENS parent H-NEW-111 bound: new upper bound {L_search_min:.4f} < {L_2OPT_PARENT:.4f}", file=sys.stderr)
else:
    print(f"  parent H-NEW-111 bound NOT tightened (parent L_2opt={L_2OPT_PARENT:.4f} remains lowest)", file=sys.stderr)

# ---------------------------------------------------------------------------
# 9. Write JSON
# ---------------------------------------------------------------------------
def round_floats(o, n=6):
    if isinstance(o, float):
        return round(o, n)
    if isinstance(o, dict):
        return {k: round_floats(v, n) for k, v in o.items()}
    if isinstance(o, list):
        return [round_floats(v, n) for v in o]
    return o

summary = {
    'finding_id': 'h-new-225',
    'title': 'Adversarial search — can ANY ordering beat the mushaf path length?',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'date': '2026-04-17',
    'rules_tuple': parent['rules_tuple'],
    'locked_params': {
        'K_top_roots': 500,
        'dirichlet_alpha': 0.5,
        'distance': 'Fisher-Rao arccos-Bhattacharyya (inherited from H-NEW-111)',
        'n_restarts': N_RESTARTS,
        'sa_iters_per_restart': SA_ITERS,
        'sa_T0': SA_T0,
        'sa_cooling': SA_COOL,
        'proposal_mix': '50% 2-opt reversal, 50% simple swap',
        'polish': '2-opt after SA',
    },
    'mw5': {
        'L_mushaf_reloaded': L_mushaf,
        'L_mushaf_parent': L_MUSHAF_PARENT,
        'delta': L_mushaf - L_MUSHAF_PARENT,
        'pass': mw5_pass,
    },
    'mushaf_init_2opt': {
        'L_after_2opt': L_mushaf_2opt,
        'passes': passes_m,
        'n_improvements': n_impr_m,
        'cumulative_delta': cum_delta_m,
        'first_improving_swap': first_swap_m,
        'mushaf_is_2opt_local_optimum': mushaf_is_2opt_local,
        'order_first20_after_2opt': mushaf_2opt_path[:20],
    },
    'sa_restarts': {
        'n_restarts': N_RESTARTS,
        'seeds': [SEED + k for k in range(N_RESTARTS)],
        'L_min': min(restart_Ls),
        'L_median': statistics.median(restart_Ls),
        'L_mean': statistics.mean(restart_Ls),
        'L_max': max(restart_Ls),
        'L_sd': statistics.stdev(restart_Ls),
        'best_seed': best_sa_seed,
        'best_order_first20': best_sa_order[:20] if best_sa_order else None,
        'per_restart_L_sorted_asc': sorted(restart_Ls),
    },
    'L_search_min': L_search_min,
    'L_mushaf': L_mushaf,
    'L_2opt_parent_h_new_111': L_2OPT_PARENT,
    'gap_abs': gap_abs,
    'gap_rel': gap_rel,
    'mushaf_rank_in_pooled': rank_mushaf,
    'n_searches_shorter_than_mushaf': n_shorter_than_mushaf,
    'n_pooled_searches': len(all_Ls),
    'verdict': verdict,
    'tightens_h_new_111_bound': tightens_parent,
    'ratio_parent_h_new_111': L_MUSHAF_PARENT / L_2OPT_PARENT,
    'ratio_updated_h_new_225': L_MUSHAF_PARENT / L_search_min,
}

summary = round_floats(summary)
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"\nWrote summary JSON: {OUT_JSON}", file=sys.stderr)

# Stdout summary
print("\n" + "=" * 70, file=sys.stderr)
print(f"L_mushaf         = {L_mushaf:.6f}", file=sys.stderr)
print(f"L_mushaf_2opt    = {L_mushaf_2opt:.6f}  ({n_impr_m} swaps)", file=sys.stderr)
print(f"L_SA_min         = {L_sa_min:.6f}  (seed {best_sa_seed})", file=sys.stderr)
print(f"L_2opt_parent    = {L_2OPT_PARENT:.6f}", file=sys.stderr)
print(f"L_search_min     = {L_search_min:.6f}", file=sys.stderr)
print(f"gap_abs          = {gap_abs:.4f}", file=sys.stderr)
print(f"gap_rel          = {gap_rel:.4f}", file=sys.stderr)
print(f"Verdict          = {verdict}", file=sys.stderr)
print("=" * 70, file=sys.stderr)
