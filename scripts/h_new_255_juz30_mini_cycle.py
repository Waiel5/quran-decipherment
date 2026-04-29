#!/usr/bin/env python3
"""H-NEW-255 — Juzʾ 30 mini-ring test.

Pre-registered tests (Bonferroni k=3, α_bon = 0.01667):
  T1  — L_juz30 / L_2opt_juz30 ratio in [1.05, 1.20]
  T2  — z(L_juz30 vs 1000 perm null) < −3.0 AND p < α_bon
  T3  — d_FR(Q 114, Q 78) short vs same 1000-perm wrap-edge null

Positive control (MW-5): greedy-NN from Q 78 on sub-matrix vs same null,
p < 0.001 required.

Rules: no-tashkeel, QAC v0.4 STEM root tokens K=500, Dirichlet α=0.5,
Fisher-Rao angular distance, sub-mushaf Q 78..Q 114 (37 surahs),
Hafs-Kufan. Seed 20260419.
"""
import csv
import hashlib
import json
import math
import random
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path
import re

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260419
PERMS = 1000

# Locked parameters (parent H-NEW-111)
K_TOP = 500
DIRICHLET_ALPHA = 0.5

# Juzʾ 30 surah set (canonical whole-surah definition)
JUZ30_FIRST = 78
JUZ30_LAST = 114
JUZ30_SURAHS = list(range(JUZ30_FIRST, JUZ30_LAST + 1))  # 37 surahs
N_JUZ = len(JUZ30_SURAHS)

# Paths
QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-255-juz30-mini-cycle-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-255.json'

# Pre-reg hash (tamper-evidence)
prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
print(f"K_TOP = {K_TOP}", file=sys.stderr)
print(f"DIRICHLET_ALPHA = {DIRICHLET_ALPHA}", file=sys.stderr)
print(f"SEED = {SEED}", file=sys.stderr)
print(f"PERMS = {PERMS}", file=sys.stderr)
print(f"Juzʾ 30 surahs: Q {JUZ30_FIRST}..Q {JUZ30_LAST} ({N_JUZ} surahs)", file=sys.stderr)

# ---------------------------------------------------------------------------
# 1. Parse QAC: per-surah STEM root tokens (same as H-NEW-111)
# ---------------------------------------------------------------------------
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

per_surah_roots = defaultdict(list)
global_root_counts = Counter()

with open(QAC_FILE, encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
            continue
        parts = line.rstrip('\n').split('\t')
        if len(parts) < 4:
            continue
        m = LOC_RE.match(parts[0])
        if not m:
            continue
        sid = int(m.group(1))
        feat = parts[3]
        if 'STEM' not in feat:
            continue
        rm = ROOT_RE.search(feat)
        if not rm:
            continue
        root = rm.group(1)
        per_surah_roots[sid].append(root)
        global_root_counts[root] += 1

assert len(per_surah_roots) == 114, f"Expected 114 surahs, got {len(per_surah_roots)}"

# ---------------------------------------------------------------------------
# 2. Top-K roots (global, identical to H-NEW-111)
# ---------------------------------------------------------------------------
top_roots = [r for r, _ in global_root_counts.most_common(K_TOP)]
top_root_index = {r: i for i, r in enumerate(top_roots)}

# ---------------------------------------------------------------------------
# 3. Per-surah probability vectors (Dirichlet smooth + L1 normalize)
# ---------------------------------------------------------------------------
counts = [[0.0] * K_TOP for _ in range(115)]
for sid in range(1, 115):
    for r in per_surah_roots.get(sid, []):
        idx = top_root_index.get(r)
        if idx is not None:
            counts[sid][idx] += 1.0

prob = [[0.0] * K_TOP for _ in range(115)]
for sid in range(1, 115):
    smoothed = [c + DIRICHLET_ALPHA for c in counts[sid]]
    s = sum(smoothed)
    prob[sid] = [v / s for v in smoothed]

sqrt_prob = [[math.sqrt(p) for p in prob[sid]] for sid in range(115)]

# ---------------------------------------------------------------------------
# 4. Fisher-Rao distance (full 114×114 for corpus-mean; sub-matrix used below)
# ---------------------------------------------------------------------------
def fr_distance(i, j):
    if i == j:
        return 0.0
    bc = 0.0
    si = sqrt_prob[i]
    sj = sqrt_prob[j]
    for k in range(K_TOP):
        bc += si[k] * sj[k]
    if bc > 1.0:
        bc = 1.0
    elif bc < -1.0:
        bc = -1.0
    return 2.0 * math.acos(bc)

print("\nBuilding 114×114 D matrix...", file=sys.stderr)
D = [[0.0] * 115 for _ in range(115)]
for i in range(1, 115):
    for j in range(i + 1, 115):
        d = fr_distance(i, j)
        D[i][j] = d
        D[j][i] = d

# Corpus mean (all 6441 pairs) for descriptive S3
all_d = [D[i][j] for i in range(1, 115) for j in range(i + 1, 115)]
corpus_mean_d = statistics.mean(all_d)
print(f"  corpus mean D = {corpus_mean_d:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 5. Juzʾ-30 sub-matrix and descriptive stats (S3)
# ---------------------------------------------------------------------------
juz_pairs = []
for a in range(N_JUZ):
    for b in range(a + 1, N_JUZ):
        juz_pairs.append(D[JUZ30_SURAHS[a]][JUZ30_SURAHS[b]])

juz_mean = statistics.mean(juz_pairs)
juz_median = statistics.median(juz_pairs)
juz_min = min(juz_pairs)
juz_max = max(juz_pairs)
print(f"  Juzʾ 30 sub-matrix ({len(juz_pairs)} pairs): mean={juz_mean:.4f} median={juz_median:.4f} min={juz_min:.4f} max={juz_max:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 6. Path length on Juzʾ 30 sub-path (Test 1 observed)
# ---------------------------------------------------------------------------
def path_length(order):
    L = 0.0
    for i in range(len(order) - 1):
        L += D[order[i]][order[i + 1]]
    return L

L_juz30 = path_length(JUZ30_SURAHS)
print(f"\nL_juz30 (canonical Q 78..Q 114) = {L_juz30:.4f}", file=sys.stderr)

# 36 consecutive-pair distances (for S1 hinge analysis)
consec_d = [(JUZ30_SURAHS[k], JUZ30_SURAHS[k + 1], D[JUZ30_SURAHS[k]][JUZ30_SURAHS[k + 1]])
            for k in range(N_JUZ - 1)]

# ---------------------------------------------------------------------------
# 7. 2-opt TSP on 37-node sub-graph (Test 1 denominator)
# ---------------------------------------------------------------------------
def greedy_nn_sub(start, nodes):
    unvisited = set(nodes)
    unvisited.remove(start)
    path = [start]
    cur = start
    while unvisited:
        nxt = min(unvisited, key=lambda v: D[cur][v])
        path.append(nxt)
        unvisited.remove(nxt)
        cur = nxt
    return path

def two_opt(path, max_passes=100):
    path = path[:]
    n = len(path)
    improved = True
    passes = 0
    while improved and passes < max_passes:
        improved = False
        passes += 1
        best_delta = 0.0
        best_ij = None
        for i in range(0, n - 2):
            a = path[i]
            b = path[i + 1]
            for j in range(i + 2, n):
                c = path[j]
                d = path[j + 1] if j + 1 < n else None
                if d is None:
                    delta = D[a][c] - D[a][b]
                else:
                    delta = (D[a][c] + D[b][d]) - (D[a][b] + D[c][d])
                if delta < best_delta - 1e-12:
                    best_delta = delta
                    best_ij = (i, j)
        if best_ij is not None:
            i, j = best_ij
            path[i + 1:j + 1] = list(reversed(path[i + 1:j + 1]))
            improved = True
    return path, passes

print("\nSecondary A: 2-opt TSP on Juzʾ 30 sub-graph...", file=sys.stderr)
L_2opt_best = None
opt_path_best = None
best_start = None
for start in JUZ30_SURAHS:
    greedy_path = greedy_nn_sub(start, JUZ30_SURAHS)
    L_greedy = path_length(greedy_path)
    opt_path, _ = two_opt(greedy_path)
    L_opt = path_length(opt_path)
    if L_2opt_best is None or L_opt < L_2opt_best:
        L_2opt_best = L_opt
        opt_path_best = opt_path[:]
        best_start = start

R_juz30 = L_juz30 / L_2opt_best
print(f"  L_2opt_juz30 (best over {N_JUZ} starts) = {L_2opt_best:.4f} (start Q {best_start})", file=sys.stderr)
print(f"  R_juz30 = L_juz30 / L_2opt = {R_juz30:.4f}", file=sys.stderr)
print(f"  Full-mushaf baseline (CF-011) = 1.107", file=sys.stderr)

T1_pass = 1.05 <= R_juz30 <= 1.20
print(f"  T1 ratio-band [1.05, 1.20]: {'PASS' if T1_pass else 'NULL'}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 8. 1000 permutations of Juzʾ 30 surah labels (Test 2 + Test 3 null)
# ---------------------------------------------------------------------------
print(f"\nNull: {PERMS} random permutations of Juzʾ 30 surah labels...", file=sys.stderr)
rng = random.Random(SEED)
null_L = []
null_wrap = []
for p in range(PERMS):
    perm = JUZ30_SURAHS[:]
    rng.shuffle(perm)
    null_L.append(path_length(perm))
    null_wrap.append(D[perm[-1]][perm[0]])  # wrap-edge: last -> first

null_mean = statistics.mean(null_L)
null_sd = statistics.stdev(null_L)
null_min = min(null_L)
null_max = max(null_L)
n_le_juz = sum(1 for L in null_L if L <= L_juz30)
p_primary = (n_le_juz + 1) / (PERMS + 1)
z_juz30 = (L_juz30 - null_mean) / null_sd

print(f"  null L: mean={null_mean:.4f} sd={null_sd:.4f} min={null_min:.4f} max={null_max:.4f}", file=sys.stderr)
print(f"  z(L_juz30) = {z_juz30:.4f}", file=sys.stderr)
print(f"  #{{L_perm <= L_juz30}} = {n_le_juz}", file=sys.stderr)
print(f"  p_T2 (one-sided lower) = {p_primary:.6f}", file=sys.stderr)
T2_pass = (z_juz30 < -3.0) and (p_primary < 0.01667)
print(f"  T2 verdict (z<-3.0 AND p<0.01667): {'PASS' if T2_pass else 'NULL'}", file=sys.stderr)

# Test 3 wrap-edge
w_wrap_obs = D[JUZ30_SURAHS[-1]][JUZ30_SURAHS[0]]  # d(Q 114, Q 78)
n_le_wrap = sum(1 for w in null_wrap if w <= w_wrap_obs)
p_wrap = (n_le_wrap + 1) / (PERMS + 1)
z_wrap = (w_wrap_obs - statistics.mean(null_wrap)) / statistics.stdev(null_wrap)
print(f"\nT3 wrap-edge d(Q 114, Q 78) = {w_wrap_obs:.4f}", file=sys.stderr)
print(f"  null wrap mean={statistics.mean(null_wrap):.4f} sd={statistics.stdev(null_wrap):.4f}", file=sys.stderr)
print(f"  z_wrap = {z_wrap:.4f}", file=sys.stderr)
print(f"  p_T3 = {p_wrap:.6f}", file=sys.stderr)
T3_pass = p_wrap < 0.01667
print(f"  T3 verdict (p<0.01667): {'PASS' if T3_pass else 'NULL'}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 9. MW-5 positive control: greedy-NN from Q 78
# ---------------------------------------------------------------------------
print("\nMW-5 positive control: greedy-NN from Q 78...", file=sys.stderr)
pos_path = greedy_nn_sub(JUZ30_FIRST, JUZ30_SURAHS)
L_pos = path_length(pos_path)
n_le_pos = sum(1 for L in null_L if L <= L_pos)
p_pos = (n_le_pos + 1) / (PERMS + 1)
z_pos = (L_pos - null_mean) / null_sd
mw5_broken = p_pos >= 0.001
print(f"  L_pos = {L_pos:.4f}, z = {z_pos:.4f}, p = {p_pos:.6f}", file=sys.stderr)
print(f"  MW-5: {'BROKEN' if mw5_broken else 'PASS'}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 10. Secondary S1: structural hinges (top-5 consecutive jumps)
# ---------------------------------------------------------------------------
consec_sorted = sorted(consec_d, key=lambda x: -x[2])
print("\nS1 — Juzʾ 30 structural hinges (top-5 consecutive jumps):", file=sys.stderr)
for a, b, d in consec_sorted[:5]:
    print(f"  Q {a:3d} -> Q {b:3d}: {d:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 11. Secondary S4: random 37-contiguous-arc null from full mushaf
# ---------------------------------------------------------------------------
print("\nS4 — random 37-contiguous-arc null (descriptive)...", file=sys.stderr)
contig_L = []
for start in range(1, 115 - N_JUZ + 1):
    arc = list(range(start, start + N_JUZ))
    contig_L.append(path_length(arc))
contig_mean = statistics.mean(contig_L)
contig_sd = statistics.stdev(contig_L)
n_le_juz_contig = sum(1 for L in contig_L if L <= L_juz30)
p_contig = (n_le_juz_contig + 1) / (len(contig_L) + 1)
z_contig = (L_juz30 - contig_mean) / contig_sd
print(f"  {len(contig_L)} contiguous 37-arcs: mean={contig_mean:.4f} sd={contig_sd:.4f}", file=sys.stderr)
print(f"  #{{L_contig <= L_juz30}} = {n_le_juz_contig}/{len(contig_L)}; p={p_contig:.4f}", file=sys.stderr)
print(f"  z_juz30_vs_contig = {z_contig:.4f}", file=sys.stderr)

# Also rank Juzʾ 30 among all 37-contiguous arcs
contig_rank = sorted(enumerate(contig_L), key=lambda x: x[1])
print(f"  Juzʾ 30 rank among 37-arcs: position {n_le_juz_contig + 1}/{len(contig_L)} from shortest", file=sys.stderr)

# ---------------------------------------------------------------------------
# 12. Joint verdict matrix
# ---------------------------------------------------------------------------
print("\n" + "=" * 70, file=sys.stderr)
print(f"T1 ratio:   R = {R_juz30:.4f}  (band [1.05, 1.20]) -> {'PASS' if T1_pass else 'NULL'}", file=sys.stderr)
print(f"T2 z/p:     z = {z_juz30:.3f}, p = {p_primary:.4f}  -> {'PASS' if T2_pass else 'NULL'}", file=sys.stderr)
print(f"T3 wrap:    d = {w_wrap_obs:.4f}, p = {p_wrap:.4f}  -> {'PASS' if T3_pass else 'NULL'}", file=sys.stderr)
print(f"MW-5:       p = {p_pos:.6f}  -> {'BROKEN' if mw5_broken else 'PASS'}", file=sys.stderr)

if mw5_broken:
    label = "INSTRUMENT-BROKEN"
elif T1_pass and T2_pass and T3_pass:
    label = "SELF-SIMILAR-RING"
elif T1_pass and T2_pass and not T3_pass:
    label = "MINI-GEODESIC-OPEN-PATH"
elif T1_pass and not T2_pass:
    label = "COMPOSITIONALLY-COHERENT-NON-SIGNIFICANT"
elif not T1_pass:
    label = "NOT-MINI-RING"
else:
    label = "MIXED"
print(f"LABEL:      {label}", file=sys.stderr)
print("=" * 70, file=sys.stderr)

# ---------------------------------------------------------------------------
# 13. Write JSON summary
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
    'finding_id': 'h-new-255',
    'title': 'Juzʾ 30 mini-ring test',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'n_perms': PERMS,
    'date': '2026-04-17',
    'rules_tuple': '(no-tashkeel, QAC-STEM root tokens K=500, QAC v0.4, Dirichlet α=0.5, Fisher-Rao angular, Q 78..Q 114 = 37 surahs, Hafs-Kufan)',
    'locked_params': {
        'K_top_roots': K_TOP,
        'dirichlet_alpha': DIRICHLET_ALPHA,
        'n_perm': PERMS,
        'distance': 'Fisher-Rao angular = 2·arccos(Σ sqrt(p_i·p_j))',
        'juz30_surahs': JUZ30_SURAHS,
        'n_surahs_juz30': N_JUZ,
    },
    'corpus_stats': {
        'corpus_mean_d_114': corpus_mean_d,
        'juz30_pairs': len(juz_pairs),
        'juz30_mean_d': juz_mean,
        'juz30_median_d': juz_median,
        'juz30_min_d': juz_min,
        'juz30_max_d': juz_max,
    },
    'T1_primary_ratio': {
        'L_juz30': L_juz30,
        'L_2opt_juz30': L_2opt_best,
        'R_juz30': R_juz30,
        'baseline_full_mushaf_1_107': 1.107,
        'deviation_from_baseline': R_juz30 - 1.107,
        'best_2opt_start': best_start,
        'band': [1.05, 1.20],
        'pass': T1_pass,
    },
    'T2_primary_permutation_null': {
        'null_mean': null_mean,
        'null_sd': null_sd,
        'null_min': null_min,
        'null_max': null_max,
        'z_juz30': z_juz30,
        'n_le_juz30': n_le_juz,
        'p_one_sided_lower': p_primary,
        'threshold_z': -3.0,
        'threshold_p': 0.01667,
        'pass': T2_pass,
    },
    'T3_primary_wrap_edge': {
        'w_wrap_q114_q78': w_wrap_obs,
        'null_wrap_mean': statistics.mean(null_wrap),
        'null_wrap_sd': statistics.stdev(null_wrap),
        'z_wrap': z_wrap,
        'p_one_sided_lower': p_wrap,
        'threshold_p': 0.01667,
        'pass': T3_pass,
    },
    'mw5_positive_control': {
        'method': 'greedy-NN from Q 78 on sub-graph',
        'L_pos': L_pos,
        'z_pos': z_pos,
        'p_pos': p_pos,
        'threshold': 0.001,
        'pass': not mw5_broken,
    },
    'S1_structural_hinges_top5': [
        {'from': a, 'to': b, 'd': d} for a, b, d in consec_sorted[:5]
    ],
    'S1_all_consecutive_pairs': [
        {'from': a, 'to': b, 'd': d} for a, b, d in consec_d
    ],
    'S2_vs_full_mushaf': {
        'R_juz30': R_juz30,
        'R_full_mushaf_CF011': 1.107,
        'diff': R_juz30 - 1.107,
        'self_similarity_band_pm_0_02': abs(R_juz30 - 1.107) < 0.02,
    },
    'S4_contiguous_37arc_null': {
        'n_arcs': len(contig_L),
        'mean': contig_mean,
        'sd': contig_sd,
        'n_le_juz30': n_le_juz_contig,
        'p_vs_contig': p_contig,
        'z_vs_contig': z_contig,
        'rank_from_shortest': n_le_juz_contig + 1,
    },
    'opt_path_best': opt_path_best,
    'canonical_juz30': JUZ30_SURAHS,
    'verdict_label': label,
    'verdict_primary': 'PASS' if (T1_pass and T2_pass and T3_pass) else 'NULL-OR-MIXED',
    'verdict_ceiling': 'PASS-DIRECTED (sub-scale replication of CF-013 M1 principle; independent feature-space replication = CONFIRMED queue)',
}

summary = round_floats(summary)
OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"\nWrote summary JSON: {OUT_JSON}", file=sys.stderr)
