#!/usr/bin/env python3
"""H-NEW-169 — NCD matrix of 114 surahs; cross-finding-011 third-axis replication.

NCD(x,y) = (C(xy) - min(C(x),C(y))) / max(C(x),C(y))  [Cilibrasi-Vitányi 2005]
C = lzma.compress length, preset=9|EXTREME (max compression).

Pre-registered (Bonferroni k=2, α_bon=0.025):
  PRIMARY    — L_mushaf < L_perm at p<0.025 (1-sided lower-tail)
  SECONDARY  — L_mushaf / L_2opt_best ratio (near-TSP-optimality)

Also reported: cycle length, cycle-2opt ratio, greedy-NN MW-5 control.

Seed 20260419 (distinct from parent FR tests' 20260417).
"""
import hashlib
import json
import lzma
import random
import sys
import time
from pathlib import Path

import numpy as np

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
PERMS = 10000

QURAN_JSON = ROOT / 'quran-text/quran-no-tashkeel.json'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-169-ncd-mushaf-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-169.json'
OUT_NPY = ROOT / 'findings/phase-b-hypotheses/csv/h-new-169-ncd-matrix.npy'

# -----------------------------------------------------------------------------
# Pre-reg tamper-evidence
# -----------------------------------------------------------------------------
prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
print(f"SEED = {SEED}", file=sys.stderr)
print(f"PERMS = {PERMS}", file=sys.stderr)
print(f"compressor: lzma preset=9|EXTREME", file=sys.stderr)

# -----------------------------------------------------------------------------
# 1. Load no-tashkeel Quran, build per-surah text (verses space-joined)
# -----------------------------------------------------------------------------
quran = json.loads(QURAN_JSON.read_text(encoding='utf-8'))
assert len(quran) == 114

assert quran[0]['verses'][0]['text'].startswith('بسم'), \
    "Surah 1 v1 should be basmala"
assert not quran[1]['verses'][0]['text'].startswith('بسم'), \
    "Surah 2 v1 should NOT be basmala"

per_surah_bytes = {}
for s in quran:
    sid = s['id']
    text = ' '.join(v['text'] for v in s['verses'])
    per_surah_bytes[sid] = text.encode('utf-8')

total_bytes = sum(len(b) for b in per_surah_bytes.values())
print(f"surahs: 114", file=sys.stderr)
print(f"total bytes (utf-8, no-tashkeel): {total_bytes}", file=sys.stderr)
print(f"mean surah bytes: {total_bytes / 114:.1f}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 2. Compressed length helpers
# -----------------------------------------------------------------------------
LZMA_PRESET = 9 | lzma.PRESET_EXTREME

def clen(b: bytes) -> int:
    return len(lzma.compress(b, preset=LZMA_PRESET))

# Per-surah compressed lengths (cache)
print("Computing per-surah compressed lengths...", file=sys.stderr)
t0 = time.time()
C_single = np.zeros(115, dtype=np.int64)  # 1-indexed
for sid in range(1, 115):
    C_single[sid] = clen(per_surah_bytes[sid])
dt = time.time() - t0
print(f"  per-surah C: range [{C_single[1:].min()}, {C_single[1:].max()}], "
      f"mean {C_single[1:].mean():.1f} bytes, took {dt:.1f}s", file=sys.stderr)

# -----------------------------------------------------------------------------
# 3. Build 114x114 NCD matrix (symmetrized)
# -----------------------------------------------------------------------------
# NCD(x,y) needs C(xy); we compute both C(xy) and C(yx) and symmetrize by mean
# to eliminate ordering artifacts.
print(f"Building 114x114 NCD matrix ({114*113//2} pairs, 2 concats each)...",
      file=sys.stderr)

SEP = b'\x00'  # explicit boundary byte
D = np.zeros((115, 115), dtype=np.float64)  # 1-indexed

t0 = time.time()
n_pairs = 114 * 113 // 2
done = 0
for i in range(1, 115):
    bi = per_surah_bytes[i]
    ci = C_single[i]
    for j in range(i + 1, 115):
        bj = per_surah_bytes[j]
        cj = C_single[j]
        c_ij = clen(bi + SEP + bj)
        c_ji = clen(bj + SEP + bi)
        lo = min(ci, cj)
        hi = max(ci, cj)
        ncd_ij = (c_ij - lo) / hi
        ncd_ji = (c_ji - lo) / hi
        d = 0.5 * (ncd_ij + ncd_ji)
        D[i, j] = d
        D[j, i] = d
        done += 1
    if i % 10 == 0:
        elapsed = time.time() - t0
        frac = done / n_pairs
        eta = elapsed / max(frac, 1e-9) - elapsed
        print(f"  row {i}/114, pairs {done}/{n_pairs} ({100*frac:.1f}%), "
              f"elapsed {elapsed:.0f}s, ETA {eta:.0f}s", file=sys.stderr)

dt_total = time.time() - t0
print(f"NCD matrix built in {dt_total:.0f}s", file=sys.stderr)

iu = np.triu_indices(114, k=1)
Dmat = D[1:, 1:]
all_d = Dmat[iu]
print(f"  NCD range: [{all_d.min():.4f}, {all_d.max():.4f}]", file=sys.stderr)
print(f"  NCD mean: {all_d.mean():.4f}, median: {np.median(all_d):.4f}",
      file=sys.stderr)

# Save the matrix for reproducibility
OUT_NPY.parent.mkdir(parents=True, exist_ok=True)
np.save(OUT_NPY, Dmat)
print(f"  saved matrix -> {OUT_NPY}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 4. Path length helpers
# -----------------------------------------------------------------------------
def path_length(order):
    a = np.asarray(order, dtype=np.int64)
    return float(D[a[:-1], a[1:]].sum())

def cycle_length(order):
    a = np.asarray(order, dtype=np.int64)
    base = float(D[a[:-1], a[1:]].sum())
    return base + float(D[a[-1], a[0]])

mushaf_order = list(range(1, 115))
L_mushaf = path_length(mushaf_order)
L_cycle_mushaf = cycle_length(mushaf_order)
print(f"\nL_mushaf (open path)  = {L_mushaf:.4f}", file=sys.stderr)
print(f"L_cycle_mushaf        = {L_cycle_mushaf:.4f}", file=sys.stderr)
print(f"  wrap edge D[114,1]  = {D[114, 1]:.4f}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 5. Null: 10,000 random permutations
# -----------------------------------------------------------------------------
print(f"\nNull: {PERMS} random permutations (seed={SEED})...", file=sys.stderr)
rng = random.Random(SEED)
null_L = np.empty(PERMS, dtype=np.float64)
null_L_cycle = np.empty(PERMS, dtype=np.float64)
perm = mushaf_order[:]
t0 = time.time()
for p in range(PERMS):
    rng.shuffle(perm)
    null_L[p] = path_length(perm)
    null_L_cycle[p] = cycle_length(perm)
    if (p + 1) % 2000 == 0:
        print(f"  perm {p+1}/{PERMS} ({time.time()-t0:.1f}s)", file=sys.stderr)

n_le_mushaf = int((null_L <= L_mushaf).sum())
p_primary = (n_le_mushaf + 1) / (PERMS + 1)
n_le_cycle = int((null_L_cycle <= L_cycle_mushaf).sum())
p_cycle = (n_le_cycle + 1) / (PERMS + 1)

null_mean = float(null_L.mean())
null_sd = float(null_L.std(ddof=1))
z_mushaf = (L_mushaf - null_mean) / null_sd

null_mean_c = float(null_L_cycle.mean())
null_sd_c = float(null_L_cycle.std(ddof=1))
z_cycle = (L_cycle_mushaf - null_mean_c) / null_sd_c

def q(arr, frac):
    return float(np.quantile(arr, frac))

null_quantiles = {
    'min': float(null_L.min()),
    'q001': q(null_L, 0.001),
    'q01':  q(null_L, 0.01),
    'q025': q(null_L, 0.025),
    'q05':  q(null_L, 0.05),
    'q25':  q(null_L, 0.25),
    'q50':  q(null_L, 0.50),
    'q75':  q(null_L, 0.75),
    'q95':  q(null_L, 0.95),
    'max':  float(null_L.max()),
    'mean': null_mean,
    'sd':   null_sd,
}
cycle_null_quantiles = {
    'min': float(null_L_cycle.min()),
    'q001': q(null_L_cycle, 0.001),
    'q01':  q(null_L_cycle, 0.01),
    'q05':  q(null_L_cycle, 0.05),
    'q50':  q(null_L_cycle, 0.50),
    'q95':  q(null_L_cycle, 0.95),
    'max':  float(null_L_cycle.max()),
    'mean': null_mean_c,
    'sd':   null_sd_c,
}

print(f"  null L mean={null_mean:.4f} sd={null_sd:.4f}", file=sys.stderr)
print(f"  null L min={null_L.min():.4f} max={null_L.max():.4f}", file=sys.stderr)
print(f"  #{{L_perm <= L_mushaf}} = {n_le_mushaf}", file=sys.stderr)
print(f"  p_primary = {p_primary:.6f}", file=sys.stderr)
print(f"  z(L_mushaf) = {z_mushaf:.4f}", file=sys.stderr)
print(f"  null cycle: mean={null_mean_c:.4f} sd={null_sd_c:.4f}", file=sys.stderr)
print(f"  z(L_cycle_mushaf) = {z_cycle:.4f}, p_cycle={p_cycle:.6f}", file=sys.stderr)

# -----------------------------------------------------------------------------
# 6. SECONDARY — greedy-NN + 2-opt TSP upper bound (open path)
# -----------------------------------------------------------------------------
print("\nSecondary: greedy-NN + 2-opt TSP approximation (open path)...",
      file=sys.stderr)

def greedy_nn(start, wrap=False):
    unvisited = set(range(1, 115))
    unvisited.remove(start)
    path = [start]
    cur = start
    while unvisited:
        nxt = min(unvisited, key=lambda v: D[cur, v])
        path.append(nxt)
        unvisited.remove(nxt)
        cur = nxt
    return path

def two_opt_open(path, max_passes=50):
    path = path[:]
    n = len(path)
    passes = 0
    while passes < max_passes:
        passes += 1
        best_delta = 0.0
        best_ij = None
        for i in range(0, n - 2):
            a = path[i]
            b = path[i + 1]
            d_ab = D[a, b]
            for j in range(i + 2, n):
                c = path[j]
                if j + 1 < n:
                    d = path[j + 1]
                    delta = (D[a, c] + D[b, d]) - (d_ab + D[c, d])
                else:
                    delta = D[a, c] - d_ab
                if delta < best_delta - 1e-12:
                    best_delta = delta
                    best_ij = (i, j)
        if best_ij is None:
            break
        i, j = best_ij
        path[i + 1:j + 1] = list(reversed(path[i + 1:j + 1]))
    return path, passes

def two_opt_cycle(path, max_passes=50):
    """Closed tour 2-opt (includes wrap-around edge)."""
    path = path[:]
    n = len(path)
    passes = 0
    while passes < max_passes:
        passes += 1
        best_delta = 0.0
        best_ij = None
        for i in range(0, n - 1):
            a = path[i]
            b = path[i + 1]
            d_ab = D[a, b]
            for j in range(i + 2, n):
                c = path[j]
                d = path[(j + 1) % n]
                if i == 0 and (j + 1) % n == 0:
                    continue
                delta = (D[a, c] + D[b, d]) - (d_ab + D[c, d])
                if delta < best_delta - 1e-12:
                    best_delta = delta
                    best_ij = (i, j)
        if best_ij is None:
            break
        i, j = best_ij
        path[i + 1:j + 1] = list(reversed(path[i + 1:j + 1]))
    return path, passes

# greedy from all 114 starts
greedy_paths = []
for start in range(1, 115):
    p = greedy_nn(start)
    greedy_paths.append((path_length(p), start, p))
greedy_paths.sort(key=lambda x: x[0])

L_greedy_best_open = greedy_paths[0][0]
best_start = greedy_paths[0][1]
best_greedy_path = greedy_paths[0][2][:]
print(f"  greedy best (open): start={best_start}, L={L_greedy_best_open:.4f}",
      file=sys.stderr)

# MW-5: greedy-NN from surah 1 (positive control)
L_greedy_s1 = next(Lg for Lg, s, _ in greedy_paths if s == 1)
print(f"  greedy from surah 1: L={L_greedy_s1:.4f}", file=sys.stderr)

# 2-opt on the best greedy
opt_path, n_passes = two_opt_open(best_greedy_path)
L_2opt_open = path_length(opt_path)
print(f"  2-opt on best: L={L_2opt_open:.4f} ({n_passes} passes)", file=sys.stderr)

L_2opt_best = L_2opt_open
opt_path_best = opt_path[:]
print("  running 2-opt on all 114 greedy starts (open)...", file=sys.stderr)
for L_g, start, p in greedy_paths:
    if L_g > L_2opt_best * 1.5:
        continue
    p2, _ = two_opt_open(p)
    Lp = path_length(p2)
    if Lp < L_2opt_best:
        L_2opt_best = Lp
        opt_path_best = p2[:]
        print(f"    improved: start={start}, L={Lp:.4f}", file=sys.stderr)

print(f"  final L_2opt_best (open): {L_2opt_best:.4f}", file=sys.stderr)
ratio_open = L_mushaf / L_2opt_best
print(f"  ratio L_mushaf / L_2opt_best = {ratio_open:.4f}", file=sys.stderr)

# Cycle 2-opt
print("\nCycle 2-opt upper bound...", file=sys.stderr)
L_cycle_2opt_best = cycle_length(opt_path_best)  # use best open path as seed
cycle_best = opt_path_best[:]
for L_g, start, p in greedy_paths:
    if L_g > L_2opt_best * 1.5:
        continue
    p2, _ = two_opt_cycle(p)
    Lp = cycle_length(p2)
    if Lp < L_cycle_2opt_best:
        L_cycle_2opt_best = Lp
        cycle_best = p2[:]
        print(f"    cycle improved: start={start}, L_cycle={Lp:.4f}",
              file=sys.stderr)
print(f"  L_cycle_2opt_best: {L_cycle_2opt_best:.4f}", file=sys.stderr)
ratio_cycle = L_cycle_mushaf / L_cycle_2opt_best
print(f"  ratio L_cycle_mushaf / L_cycle_2opt_best = {ratio_cycle:.4f}",
      file=sys.stderr)

# MW-5 dominance check: 2-opt solution should dominate greedy-NN-s1,
# both of which dominate random mean.
mw5_pass = (L_2opt_best < L_greedy_s1 < null_mean)
print(f"\nMW-5 dominance: L_2opt_best < L_greedy_s1 < null_mean ? "
      f"{L_2opt_best:.3f} < {L_greedy_s1:.3f} < {null_mean:.3f} -> {mw5_pass}",
      file=sys.stderr)

# -----------------------------------------------------------------------------
# 7. Decision
# -----------------------------------------------------------------------------
ALPHA_BON = 0.025  # Bonferroni k=2
primary_pass = (p_primary < ALPHA_BON) and (L_mushaf < null_mean)

# Parent FR results for comparison
fr_results = {
    'roots_K500': {'L_mushaf': 85.76, 'z': -11.46, 'ratio_2opt': 1.107},
    'char4gram_K2000': {'L_mushaf': 89.23, 'z': -11.41, 'ratio_2opt': 1.114},
    'verselen_8bin': {'L_mushaf': 77.66, 'z': -9.84, 'ratio_2opt': 2.71},
}

print("\n" + "="*72, file=sys.stderr)
print(f"PRIMARY: L_mushaf={L_mushaf:.4f}, z={z_mushaf:.3f}, "
      f"p={p_primary:.5f} → {'PASS' if primary_pass else 'FAIL'} "
      f"(α_bon=0.025)", file=sys.stderr)
print(f"SECONDARY: ratio_open (L/L_2opt) = {ratio_open:.4f}", file=sys.stderr)
print(f"CYCLE: ratio_cycle = {ratio_cycle:.4f}", file=sys.stderr)
print(f"MW-5 dominance: {mw5_pass}", file=sys.stderr)
print("="*72, file=sys.stderr)

# -----------------------------------------------------------------------------
# 8. Persist
# -----------------------------------------------------------------------------
out = {
    'hypothesis_id': 'H-NEW-169',
    'title': 'NCD matrix mushaf optimality (cross-finding-011 third-axis replication)',
    'prereg_sha256': prereg_sha,
    'seed': SEED,
    'n_perms': PERMS,
    'compressor': 'lzma preset=9|EXTREME',
    'ncd_separator_byte': '0x00',
    'ncd_symmetrization': 'arithmetic mean of NCD(x,y), NCD(y,x)',

    'matrix_stats': {
        'min': float(all_d.min()),
        'max': float(all_d.max()),
        'mean': float(all_d.mean()),
        'median': float(np.median(all_d)),
    },
    'L_mushaf': L_mushaf,
    'L_cycle_mushaf': L_cycle_mushaf,
    'wrap_edge_D_114_1': float(D[114, 1]),

    'null_open': {
        'quantiles': null_quantiles,
        'n_le_mushaf': n_le_mushaf,
        'p_primary': p_primary,
        'z_mushaf': z_mushaf,
    },
    'null_cycle': {
        'quantiles': cycle_null_quantiles,
        'n_le_cycle': n_le_cycle,
        'p_cycle': p_cycle,
        'z_cycle': z_cycle,
    },

    'secondary_2opt_open': {
        'L_greedy_best': L_greedy_best_open,
        'L_greedy_from_surah1': L_greedy_s1,
        'L_2opt_best': L_2opt_best,
        'ratio_L_mushaf_over_L_2opt': ratio_open,
    },
    'cycle_2opt': {
        'L_cycle_2opt_best': L_cycle_2opt_best,
        'ratio_L_cycle_over_L_cycle_2opt': ratio_cycle,
    },

    'mw5_dominance_L2opt_lt_greedyS1_lt_nullmean': mw5_pass,

    'alpha_bonferroni_k2': ALPHA_BON,
    'primary_verdict': 'PASS' if primary_pass else 'FAIL',

    'fr_parent_comparison': fr_results,
}

OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False))
print(f"\nwrote {OUT_JSON}", file=sys.stderr)
print(json.dumps(out, indent=2, ensure_ascii=False))
