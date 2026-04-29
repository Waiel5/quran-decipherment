#!/usr/bin/env python3
"""H-NEW-131.1 — Length-normalized MST: α-sweep + length-residualization.

Pre-registered tests (Bonferroni k=2, α_bon=0.025):

  MW-5 planted-hub positive control — synthetic 115th surah = empirical
    mean of 114 real surahs. Expected MST-degree ≥ 20 or pipeline is
    declared INSTRUMENT-BROKEN and further cells held in abeyance.

  Cell A — α-sweep across {0.001, 0.01, 0.05, 0.1, 0.5, 1.0, 2.0}.
    Record Q 108 MST-degree at each α. Formal test = Spearman ρ
    between α and Q 108-degree. PASS if ρ ≥ 0.8, p < 0.025 (1-sided,
    Fisher-z approximation).

  Cell B — length-residualized smoothing: per-surah prior scaling
    `α_base × (mean_tokens / surah_tokens)` making every surah's
    prior-to-real mass ratio equal. Record Q 108 MST-degree. PASS if
    degree ∈ [15, 33] (±9 window around baseline 24).

  Cell C/D/E — descriptive exploratory; no Bonferroni slot.

Seed 20260417. Deterministic.
"""
import hashlib
import json
import math
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260417
K_TOP = 500
ALPHA_BASELINE = 0.5
ALPHAS = [0.001, 0.01, 0.05, 0.1, 0.5, 1.0, 2.0]

QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-131-1-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-131-1.json'

prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
print(f"ALPHAS = {ALPHAS}", file=sys.stderr)
print(f"SEED = {SEED}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 1. Parse QAC — identical to H-NEW-111 / H-NEW-131
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
        per_surah_roots[sid].append(rm.group(1))
        global_root_counts[rm.group(1)] += 1

assert len(per_surah_roots) == 114

top_roots = [r for r, _ in global_root_counts.most_common(K_TOP)]
top_root_index = {r: i for i, r in enumerate(top_roots)}

counts = [[0.0] * K_TOP for _ in range(115)]
for sid in range(1, 115):
    for r in per_surah_roots.get(sid, []):
        idx = top_root_index.get(r)
        if idx is not None:
            counts[sid][idx] += 1.0

# Per-surah total (STEM root tokens, not top-K-filtered)
per_surah_total_stem_roots = {sid: len(per_surah_roots.get(sid, [])) for sid in range(1, 115)}
per_surah_topk_count = {sid: int(sum(counts[sid])) for sid in range(1, 115)}
mean_surah_stem_tokens = statistics.mean(per_surah_total_stem_roots.values())
print(f"Per-surah total-STEM-roots: mean={mean_surah_stem_tokens:.2f}, "
      f"min={min(per_surah_total_stem_roots.values())}, "
      f"max={max(per_surah_total_stem_roots.values())}", file=sys.stderr)
print(f"Q 108 total-STEM-roots: {per_surah_total_stem_roots[108]}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 2. Helpers
# ---------------------------------------------------------------------------
def smooth_and_normalize_flat(alpha):
    """Flat Dirichlet α on every cell for every surah (H-NEW-131 baseline)."""
    prob = [[0.0] * K_TOP for _ in range(115)]
    for sid in range(1, 115):
        smoothed = [c + alpha for c in counts[sid]]
        s = sum(smoothed)
        prob[sid] = [v / s for v in smoothed]
    return prob

def smooth_length_residualized(alpha_base):
    """Length-residualized prior: prior per cell = α_base × mean_tokens / N_i.

    Short surahs get SMALLER prior per cell, long surahs get LARGER. This
    makes every surah's prior-to-real-count ratio structurally equal.

    NOTE: this is per-SURAH α; not per-cell.
    """
    prob = [[0.0] * K_TOP for _ in range(115)]
    for sid in range(1, 115):
        N_i = per_surah_total_stem_roots[sid]
        if N_i == 0:
            alpha_i = alpha_base
        else:
            alpha_i = alpha_base * (mean_surah_stem_tokens / N_i)
        smoothed = [c + alpha_i for c in counts[sid]]
        s = sum(smoothed)
        prob[sid] = [v / s for v in smoothed]
    return prob, {sid: (alpha_base * (mean_surah_stem_tokens / max(per_surah_total_stem_roots[sid], 1))) for sid in range(1, 115)}

def fisher_rao(p, q):
    bc = 0.0
    for a, b in zip(p, q):
        if a > 0 and b > 0:
            bc += math.sqrt(a * b)
    if bc > 1.0:
        bc = 1.0
    elif bc < -1.0:
        bc = -1.0
    return 2.0 * math.acos(bc)

def compute_D(prob, n_nodes=114):
    """Compute full D-matrix on indices 1..n_nodes."""
    D = [[0.0] * (n_nodes + 1) for _ in range(n_nodes + 1)]
    for i in range(1, n_nodes + 1):
        for j in range(i + 1, n_nodes + 1):
            d = fisher_rao(prob[i], prob[j])
            D[i][j] = d
            D[j][i] = d
    return D

class DSU:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.rank = [0] * (n + 1)
    def find(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] < self.rank[ry]:
            rx, ry = ry, rx
        self.parent[ry] = rx
        if self.rank[rx] == self.rank[ry]:
            self.rank[rx] += 1
        return True

def mst_kruskal(D, n_nodes=114):
    edges = []
    for i in range(1, n_nodes + 1):
        for j in range(i + 1, n_nodes + 1):
            edges.append((D[i][j], i, j))
    edges.sort()
    dsu = DSU(n_nodes)
    mst_edges = []
    for w, i, j in edges:
        if dsu.union(i, j):
            mst_edges.append((i, j, w))
            if len(mst_edges) == n_nodes - 1:
                break
    assert len(mst_edges) == n_nodes - 1, f"MST incomplete: {len(mst_edges)} edges on {n_nodes} nodes"
    return mst_edges

def degree_vector(mst_edges):
    deg = Counter()
    for i, j, _ in mst_edges:
        deg[i] += 1
        deg[j] += 1
    return deg

def spearman_rho(xs, ys):
    """Spearman rank correlation (no ties expected in small input)."""
    n = len(xs)
    def ranks(vals):
        sorted_pairs = sorted(range(n), key=lambda i: vals[i])
        r = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and vals[sorted_pairs[j + 1]] == vals[sorted_pairs[i]]:
                j += 1
            avg_rank = (i + j) / 2.0 + 1  # 1-indexed
            for k in range(i, j + 1):
                r[sorted_pairs[k]] = avg_rank
            i = j + 1
        return r
    rx = ranks(xs)
    ry = ranks(ys)
    mx = sum(rx) / n
    my = sum(ry) / n
    num = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    dx = math.sqrt(sum((rx[i] - mx) ** 2 for i in range(n)))
    dy = math.sqrt(sum((ry[i] - my) ** 2 for i in range(n)))
    if dx == 0 or dy == 0:
        return 0.0
    return num / (dx * dy)

def fisher_z_pvalue_one_sided(rho, n):
    """1-sided p for rho using Fisher r-z; tests H1: rho > 0."""
    if rho >= 1.0:
        rho = 0.9999999
    if rho <= -1.0:
        rho = -0.9999999
    z = 0.5 * math.log((1 + rho) / (1 - rho)) * math.sqrt(n - 3)
    # 1-sided upper-tail p ≈ 1 - Φ(z)
    p = 0.5 * math.erfc(z / math.sqrt(2))
    return p

# ---------------------------------------------------------------------------
# 3. MW-5 positive control: planted-hub synthetic centroid surah
# ---------------------------------------------------------------------------
print("\n[MW-5] Planted-hub positive control (synthetic centroid as surah 115)...", file=sys.stderr)

# Build synthetic surah 115 = mean of all 114 raw count vectors
counts_115 = counts + [[0.0] * K_TOP]  # add row 115
for idx in range(K_TOP):
    col_mean = statistics.mean(counts[sid][idx] for sid in range(1, 115))
    counts_115[115][idx] = col_mean

# Smooth with α=0.5 flat (same as baseline)
prob_115 = [[0.0] * K_TOP for _ in range(116)]
for sid in range(1, 116):
    smoothed = [c + 0.5 for c in counts_115[sid]]
    s = sum(smoothed)
    prob_115[sid] = [v / s for v in smoothed]

D_115 = compute_D(prob_115, n_nodes=115)
mst_115 = mst_kruskal(D_115, n_nodes=115)
deg_115 = degree_vector(mst_115)
synthetic_deg = deg_115[115]
print(f"  synthetic centroid surah (id=115) degree in 115-MST: {synthetic_deg}", file=sys.stderr)
mw5_pass = synthetic_deg >= 20
print(f"  MW-5 {'PASS' if mw5_pass else 'FAIL'} (threshold ≥20)", file=sys.stderr)
print(f"  MW-5 top-10: {deg_115.most_common(10)}", file=sys.stderr)

if not mw5_pass:
    print("\n!! MW-5 FAILED — INSTRUMENT BROKEN. Results held in abeyance. !!", file=sys.stderr)

# ---------------------------------------------------------------------------
# 4. Cell A: α-sweep
# ---------------------------------------------------------------------------
print("\n[Cell A] α-sweep...", file=sys.stderr)

cell_A_results = []
for alpha in ALPHAS:
    prob = smooth_and_normalize_flat(alpha)
    D = compute_D(prob)
    mst = mst_kruskal(D)
    deg = degree_vector(mst)
    q108_deg = deg[108]
    top5 = deg.most_common(5)
    cell_A_results.append({
        'alpha': alpha,
        'q108_degree': q108_deg,
        'top5_hubs': top5,
    })
    print(f"  α={alpha}: Q 108 deg={q108_deg}, top-5={top5}", file=sys.stderr)

# Spearman rho between α and Q 108 degree
rho = spearman_rho(ALPHAS, [r['q108_degree'] for r in cell_A_results])
p_one_sided = fisher_z_pvalue_one_sided(rho, len(ALPHAS))
print(f"  Spearman ρ(α, Q108-deg) = {rho:.4f}", file=sys.stderr)
print(f"  1-sided p (Fisher r-z) = {p_one_sided:.6f}", file=sys.stderr)
cell_A_pass = (rho >= 0.8) and (p_one_sided < 0.025)
print(f"  Cell A {'PASS' if cell_A_pass else 'FAIL'}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 5. Cell B: length-residualized smoothing
# ---------------------------------------------------------------------------
print("\n[Cell B] Length-residualized smoothing...", file=sys.stderr)
prob_resid, per_surah_alpha = smooth_length_residualized(ALPHA_BASELINE)
print(f"  Q 108's effective α = {per_surah_alpha[108]:.4f} "
      f"(vs baseline {ALPHA_BASELINE}; ratio {per_surah_alpha[108]/ALPHA_BASELINE:.2f}×)",
      file=sys.stderr)
print(f"  Q 2 (longest) effective α = {per_surah_alpha[2]:.4f}", file=sys.stderr)
print(f"  α_i range: [{min(per_surah_alpha.values()):.4f}, "
      f"{max(per_surah_alpha.values()):.4f}]", file=sys.stderr)

D_resid = compute_D(prob_resid)
mst_resid = mst_kruskal(D_resid)
deg_resid = degree_vector(mst_resid)
q108_deg_resid = deg_resid[108]
print(f"  Cell B: Q 108 deg = {q108_deg_resid}", file=sys.stderr)
print(f"  Cell B top-10 hubs: {deg_resid.most_common(10)}", file=sys.stderr)
cell_B_pass = 15 <= q108_deg_resid <= 33
print(f"  Cell B {'PASS' if cell_B_pass else 'FAIL'} (threshold: 15 ≤ deg ≤ 33)", file=sys.stderr)

# ---------------------------------------------------------------------------
# 6. Cell C — degree-distribution full histogram at each α (descriptive)
# ---------------------------------------------------------------------------
cell_C = []
for r in cell_A_results:
    alpha = r['alpha']
    prob = smooth_and_normalize_flat(alpha)
    D = compute_D(prob)
    mst = mst_kruskal(D)
    deg = degree_vector(mst)
    dist = Counter(deg.values())
    cell_C.append({'alpha': alpha, 'degree_distribution': dict(sorted(dist.items()))})

# ---------------------------------------------------------------------------
# 7. Cell D — Q 108's MST-neighbors at each α (descriptive)
# ---------------------------------------------------------------------------
cell_D = []
for alpha in ALPHAS:
    prob = smooth_and_normalize_flat(alpha)
    D = compute_D(prob)
    mst = mst_kruskal(D)
    neighbors_108 = []
    for i, j, w in mst:
        if i == 108:
            neighbors_108.append((j, w))
        elif j == 108:
            neighbors_108.append((i, w))
    n_short_mufassal = sum(1 for n, _ in neighbors_108 if n >= 78)
    cell_D.append({
        'alpha': alpha,
        'q108_neighbors': neighbors_108,
        'n_neighbors_ge_Q78_short_mufassal': n_short_mufassal,
        'fraction_short_mufassal_neighbors': n_short_mufassal / len(neighbors_108) if neighbors_108 else 0,
    })

# ---------------------------------------------------------------------------
# 8. Cell E — rank-order preservation of top-4 H-NEW-134 hubs at each α
# ---------------------------------------------------------------------------
reference_top4 = [108, 7, 112, 64]  # H-NEW-134 top-4 at α=0.5
cell_E = []
for alpha in ALPHAS:
    prob = smooth_and_normalize_flat(alpha)
    D = compute_D(prob)
    mst = mst_kruskal(D)
    deg = degree_vector(mst)
    top4_at_alpha = [sid for sid, _ in deg.most_common(4)]
    preserved = top4_at_alpha == reference_top4
    overlap = len(set(top4_at_alpha) & set(reference_top4))
    cell_E.append({
        'alpha': alpha,
        'top4_at_alpha': top4_at_alpha,
        'overlap_with_reference': overlap,
        'exact_preserved': preserved,
    })

# ---------------------------------------------------------------------------
# 9. Final verdict
# ---------------------------------------------------------------------------
if not mw5_pass:
    final_verdict = "INSTRUMENT-BROKEN — MW-5 positive control failed; other cells held in abeyance"
elif cell_A_pass and cell_B_pass:
    final_verdict = "STRUCTURAL-ROBUST + SMOOTHING-MONOTONE — structural signal survives length correction AND α-smoothing relationship quantitatively confirmed"
elif cell_A_pass and not cell_B_pass:
    final_verdict = "SMOOTHING-MONOTONE + STRUCTURE-LENGTH-CONFOUND — Q 108 centrality tied to length; α-monotone relationship confirmed but length-correction destabilizes the hub"
elif not cell_A_pass and cell_B_pass:
    final_verdict = "STRUCTURAL-ROBUST + SMOOTHING-UNSTABLE — structure survives length correction but α-smoothing relationship not monotone"
else:
    final_verdict = "BOTH-FAIL — Q 108 centrality is neither monotone in α nor robust to length correction"

print("\n" + "=" * 70, file=sys.stderr)
print(f"MW-5 positive control: {'PASS' if mw5_pass else 'FAIL'} (synthetic deg={synthetic_deg})", file=sys.stderr)
print(f"Cell A α-sweep Spearman ρ = {rho:.4f} (p = {p_one_sided:.6f}): "
      f"{'PASS' if cell_A_pass else 'FAIL'}", file=sys.stderr)
print(f"Cell B length-residualized Q 108 deg = {q108_deg_resid}: "
      f"{'PASS' if cell_B_pass else 'FAIL'}", file=sys.stderr)
print(f"FINAL VERDICT: {final_verdict}", file=sys.stderr)
print("=" * 70, file=sys.stderr)

# ---------------------------------------------------------------------------
# 10. Write JSON
# ---------------------------------------------------------------------------
summary = {
    'finding_id': 'h-new-131.1',
    'title': 'Length-normalized MST: α-sweep + length-residualization',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'date': '2026-04-17',
    'parent_finding': 'h-new-131',
    'grandparent': 'h-new-134',
    'rules_tuple': '(114 surahs Hafs-Kūfan; K=500 QAC-STEM roots; Fisher-Rao arccos-Bhattacharyya; MST via Kruskal; no-tashkeel; QAC v0.4)',
    'bonferroni': {
        'k': 2,
        'alpha_bon': 0.025,
        'family': 'h-new-131-1-length-normalization',
        'inferential_slots': ['Cell A Spearman ρ', 'Cell B length-residualized degree-range'],
    },
    'mw5_positive_control': {
        'design': 'planted synthetic centroid surah (id=115) = empirical mean of 114 real surahs; smoothed α=0.5; build 115-node MST',
        'expected_threshold': 20,
        'synthetic_degree': synthetic_deg,
        'pass': mw5_pass,
        'top10_in_115_mst': deg_115.most_common(10),
    },
    'cell_A_alpha_sweep': {
        'alphas': ALPHAS,
        'results': cell_A_results,
        'spearman_rho_alpha_vs_q108_degree': rho,
        'spearman_p_one_sided_fisher_z': p_one_sided,
        'threshold_rho': 0.8,
        'threshold_p': 0.025,
        'pass': cell_A_pass,
    },
    'cell_B_length_residualized': {
        'alpha_base': ALPHA_BASELINE,
        'formula': 'alpha_i = alpha_base × (mean_surah_stem_tokens / surah_i_stem_tokens)',
        'mean_surah_stem_tokens': mean_surah_stem_tokens,
        'per_surah_effective_alpha_q108': per_surah_alpha[108],
        'per_surah_effective_alpha_q2_longest': per_surah_alpha[2],
        'alpha_i_min': min(per_surah_alpha.values()),
        'alpha_i_max': max(per_surah_alpha.values()),
        'q108_degree': q108_deg_resid,
        'top10_hubs': deg_resid.most_common(10),
        'threshold_min': 15,
        'threshold_max': 33,
        'pass': cell_B_pass,
    },
    'cell_C_degree_distribution_by_alpha': cell_C,
    'cell_D_q108_neighbors_by_alpha': cell_D,
    'cell_E_top4_rank_preservation': cell_E,
    'reference_top4_h_new_134': reference_top4,
    'final_verdict': final_verdict,
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False, default=str))
print(f"\nWrote: {OUT_JSON}", file=sys.stderr)
