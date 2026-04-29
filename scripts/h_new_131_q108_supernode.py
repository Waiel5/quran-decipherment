#!/usr/bin/env python3
"""H-NEW-131 — Q 108 al-Kawthar MST super-hub robustness investigation.

Pre-registered (amended per audit-036 2026-04-17; Bonferroni k=2, α_bon=0.025):
  Cell A — DESCRIPTIVE-ROBUSTNESS bright-line check (not an inferential
           slot). MST-degree of Q 108 under Dirichlet α=0.01
           (near-no-smoothing). Pre-committed thresholds:
           ≤5 REFUTE, 6-14 WEAKLY-SURVIVE, ≥15 SURVIVE.
  Cell B — Inferential; Bonferroni k=2 over {JS, TV}.
           MST-degree of Q 108 under alternative metrics:
             Hellinger (rank-monotone consistency check w/ FR; excluded
               from inferential family),
             Jensen-Shannon (independent slot),
             Total variation L1 (independent slot).
           PASS if ≥2/3 of {FR, JS, TV} give Q 108 degree ≥15.
  Cell C — Descriptive: top-5 roots in Q 108, their global rank, and
           fraction of probability on top-50 globally-frequent roots.

Same input pipeline as H-NEW-111 (QAC v0.4, STEM segments, top-500 roots,
Hafs-Kūfan). Seed 20260417. Deterministic.

Pre-reg SHA-256 emitted to stderr.
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

# Locked parameters — match H-NEW-111 exactly except Dirichlet-α in Cell A
K_TOP = 500
ALPHA_BASELINE = 0.5       # as in H-NEW-111 / H-NEW-134
ALPHA_CELL_A = 0.01        # near-no-smoothing per pre-reg

# Paths
QAC_FILE = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
PREREG_FILE = ROOT / 'findings/phase-b-hypotheses/h-new-131-prereg.md'
OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-131.json'

# Pre-reg hash (tamper-evidence)
prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
print(f"K_TOP = {K_TOP}", file=sys.stderr)
print(f"ALPHA_BASELINE = {ALPHA_BASELINE}", file=sys.stderr)
print(f"ALPHA_CELL_A = {ALPHA_CELL_A}", file=sys.stderr)
print(f"SEED = {SEED}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 1. Parse QAC — identical to H-NEW-111
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

n_surahs = len(per_surah_roots)
assert n_surahs == 114, f"Expected 114 surahs, got {n_surahs}"
print(f"surahs: {n_surahs}", file=sys.stderr)
print(f"distinct global roots: {len(global_root_counts)}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 2. Top-K roots
# ---------------------------------------------------------------------------
top_roots = [r for r, _ in global_root_counts.most_common(K_TOP)]
top_root_index = {r: i for i, r in enumerate(top_roots)}
print(f"top-{K_TOP} roots selected (rank 1 = {top_roots[0]}, rank {K_TOP} = {top_roots[-1]})", file=sys.stderr)

# ---------------------------------------------------------------------------
# 3. Build raw count matrix
# ---------------------------------------------------------------------------
counts = [[0.0] * K_TOP for _ in range(115)]
for sid in range(1, 115):
    for r in per_surah_roots.get(sid, []):
        idx = top_root_index.get(r)
        if idx is not None:
            counts[sid][idx] += 1.0

# Q 108 raw token count sanity
q108_raw_total = int(sum(counts[108]))
q108_all_tokens = len(per_surah_roots[108])
print(f"Q 108: {q108_raw_total} tokens fall in top-{K_TOP} of {q108_all_tokens} total STEM root tokens", file=sys.stderr)

def smooth_and_normalize(alpha):
    prob = [[0.0] * K_TOP for _ in range(115)]
    for sid in range(1, 115):
        smoothed = [c + alpha for c in counts[sid]]
        s = sum(smoothed)
        prob[sid] = [v / s for v in smoothed]
    return prob

# ---------------------------------------------------------------------------
# 4. Distance functions
# ---------------------------------------------------------------------------
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

def hellinger(p, q):
    # D_H = sqrt( 1/2 · Σ (√p - √q)^2 )
    s = 0.0
    for a, b in zip(p, q):
        d = math.sqrt(a) - math.sqrt(b)
        s += d * d
    return math.sqrt(0.5 * s)

def js_distance(p, q):
    # sqrt( (KL(p||m) + KL(q||m)) / 2 )  where m = (p+q)/2
    s = 0.0
    for a, b in zip(p, q):
        m = 0.5 * (a + b)
        if m > 0:
            if a > 0:
                s += 0.5 * a * math.log(a / m)
            if b > 0:
                s += 0.5 * b * math.log(b / m)
    # guard float noise
    if s < 0:
        s = 0.0
    return math.sqrt(s)

def total_variation(p, q):
    return 0.5 * sum(abs(a - b) for a, b in zip(p, q))

# ---------------------------------------------------------------------------
# 5. MST via Kruskal
# ---------------------------------------------------------------------------
def compute_D(prob, dist_func):
    D = [[0.0] * 115 for _ in range(115)]
    for i in range(1, 115):
        for j in range(i + 1, 115):
            d = dist_func(prob[i], prob[j])
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

def mst_kruskal(D):
    edges = []
    for i in range(1, 115):
        for j in range(i + 1, 115):
            edges.append((D[i][j], i, j))
    edges.sort()
    dsu = DSU(114)
    mst_edges = []
    for w, i, j in edges:
        if dsu.union(i, j):
            mst_edges.append((i, j, w))
            if len(mst_edges) == 113:
                break
    assert len(mst_edges) == 113, f"Expected 113 MST edges on 114 nodes, got {len(mst_edges)}"
    return mst_edges

def degree_vector(mst_edges):
    deg = Counter()
    for i, j, _ in mst_edges:
        deg[i] += 1
        deg[j] += 1
    return deg

# ---------------------------------------------------------------------------
# 6. Sanity replication: H-NEW-134's Fisher-Rao α=0.5 MST (should give Q 108 deg 24)
# ---------------------------------------------------------------------------
print("\n[sanity] Replicating H-NEW-134 MST (FR, α=0.5)...", file=sys.stderr)
prob_base = smooth_and_normalize(ALPHA_BASELINE)
D_fr_base = compute_D(prob_base, fisher_rao)
mst_fr_base = mst_kruskal(D_fr_base)
deg_fr_base = degree_vector(mst_fr_base)
print(f"  FR α=0.5: Q 108 deg={deg_fr_base[108]} (expect 24)", file=sys.stderr)
print(f"  FR α=0.5 top-10 hubs: {deg_fr_base.most_common(10)}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 7. CELL A — Dirichlet α=0.01
# ---------------------------------------------------------------------------
print("\n[Cell A] Fisher-Rao MST with Dirichlet α=0.01...", file=sys.stderr)
prob_A = smooth_and_normalize(ALPHA_CELL_A)
D_fr_A = compute_D(prob_A, fisher_rao)
mst_A = mst_kruskal(D_fr_A)
deg_A = degree_vector(mst_A)
q108_deg_A = deg_A[108]
print(f"  Cell A: Q 108 deg={q108_deg_A}", file=sys.stderr)
print(f"  Cell A top-10 hubs: {deg_A.most_common(10)}", file=sys.stderr)

if q108_deg_A >= 15:
    cell_a_verdict = "SURVIVE"
elif q108_deg_A >= 6:
    cell_a_verdict = "WEAKLY-SURVIVE"
else:
    cell_a_verdict = "REFUTE"
print(f"  Cell A verdict: {cell_a_verdict}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 8. CELL B — alternative metrics (same α=0.5 as H-NEW-134)
# ---------------------------------------------------------------------------
print("\n[Cell B] Alternative-metric MSTs on α=0.5 probabilities...", file=sys.stderr)

D_hel = compute_D(prob_base, hellinger)
mst_hel = mst_kruskal(D_hel)
deg_hel = degree_vector(mst_hel)
q108_deg_hel = deg_hel[108]
print(f"  Hellinger: Q 108 deg={q108_deg_hel}", file=sys.stderr)
print(f"  Hellinger top-10: {deg_hel.most_common(10)}", file=sys.stderr)

D_js = compute_D(prob_base, js_distance)
mst_js = mst_kruskal(D_js)
deg_js = degree_vector(mst_js)
q108_deg_js = deg_js[108]
print(f"  Jensen-Shannon: Q 108 deg={q108_deg_js}", file=sys.stderr)
print(f"  JS top-10: {deg_js.most_common(10)}", file=sys.stderr)

D_tv = compute_D(prob_base, total_variation)
mst_tv = mst_kruskal(D_tv)
deg_tv = degree_vector(mst_tv)
q108_deg_tv = deg_tv[108]
print(f"  Total variation: Q 108 deg={q108_deg_tv}", file=sys.stderr)
print(f"  TV top-10: {deg_tv.most_common(10)}", file=sys.stderr)

# Cell B verdict: count {FR, JS, TV} with Q 108 deg >= 15
# (Hellinger is consistency-check; should match FR by rank-monotonicity)
fr_deg = deg_fr_base[108]
cell_b_hits = sum(1 for d in [fr_deg, q108_deg_js, q108_deg_tv] if d >= 15)
cell_b_verdict = "PASS" if cell_b_hits >= 2 else "FAIL"
print(f"  Cell B: {cell_b_hits}/3 metrics have Q 108 deg ≥ 15 → {cell_b_verdict}", file=sys.stderr)

# Sanity: confirm Hellinger MST equals FR MST (rank-monotone)
hel_edges_sorted = sorted([(min(i,j), max(i,j)) for i,j,_ in mst_hel])
fr_edges_sorted = sorted([(min(i,j), max(i,j)) for i,j,_ in mst_fr_base])
hellinger_matches_fr = (hel_edges_sorted == fr_edges_sorted)
print(f"  Hellinger MST == FR MST (consistency check): {hellinger_matches_fr}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 9. CELL C — Q 108 root-profile descriptive
# ---------------------------------------------------------------------------
print("\n[Cell C] Q 108 root-profile...", file=sys.stderr)
q108_roots_present = Counter(per_surah_roots[108])
print(f"  Q 108 distinct roots: {len(q108_roots_present)}", file=sys.stderr)
print(f"  Q 108 total STEM root tokens: {sum(q108_roots_present.values())}", file=sys.stderr)

# Top-5 by raw Q 108 count (ties → break by global-frequency rank, lowest-rank = higher global freq)
def global_rank_of(root):
    # rank in top-K list (1-indexed); return K+1 if not in top-K
    return top_root_index.get(root, K_TOP) + 1

q108_top5 = sorted(q108_roots_present.items(),
                   key=lambda rc: (-rc[1], global_rank_of(rc[0])))[:5]
q108_top5_report = []
for root, count in q108_top5:
    rnk = global_rank_of(root)
    gcount = global_root_counts.get(root, 0)
    q108_top5_report.append({
        'root': root,
        'q108_count': count,
        'global_rank_in_top500': rnk if rnk <= K_TOP else None,
        'global_corpus_count': gcount,
    })
    print(f"  root={root!r}: Q108 count={count}, global rank={rnk if rnk<=K_TOP else 'not-in-top-500'}, global count={gcount}", file=sys.stderr)

# Fraction of Q 108 α=0.5 probability on top-50 globally-frequent roots
q108_prob_baseline = prob_base[108]
top50_mass = sum(q108_prob_baseline[i] for i in range(50))
top100_mass = sum(q108_prob_baseline[i] for i in range(100))
print(f"  Q 108 α=0.5 probability on top-50 global roots: {top50_mass:.4f}", file=sys.stderr)
print(f"  Q 108 α=0.5 probability on top-100 global roots: {top100_mass:.4f}", file=sys.stderr)

# Also: fraction of RAW (unsmoothed) probability on top-50
q108_raw_total = sum(counts[108])
if q108_raw_total > 0:
    q108_raw_top50 = sum(counts[108][i] for i in range(50))
    raw_top50_frac = q108_raw_top50 / q108_raw_total
else:
    raw_top50_frac = 0.0
print(f"  Q 108 UNSMOOTHED fraction on top-50 global roots: {raw_top50_frac:.4f}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 10. Summary + final verdict
# ---------------------------------------------------------------------------
# Pre-committed acceptance matrix
if cell_a_verdict == "REFUTE":
    final_verdict = "REFUTED — Q 108 super-hub is smoothing artifact; demote H-NEW-134 claim"
elif cell_a_verdict == "SURVIVE" and cell_b_verdict == "PASS":
    final_verdict = "STRUCTURAL — super-hub confirmed robust across smoothing + metrics"
elif cell_a_verdict == "SURVIVE" and cell_b_verdict == "FAIL":
    final_verdict = "FISHER-RAO-SPECIFIC — survives smoothing but not metric change"
elif cell_a_verdict == "WEAKLY-SURVIVE" and cell_b_verdict == "PASS":
    final_verdict = "WEAKLY STRUCTURAL — mixed mechanical + structural origin"
else:
    final_verdict = "WEAKLY ARTIFACT — mostly mechanical, some metric-specific residual"

print("\n" + "=" * 70, file=sys.stderr)
print(f"Cell A (α=0.01, FR): Q 108 deg = {q108_deg_A}  → {cell_a_verdict}", file=sys.stderr)
print(f"Cell B cross-metric (α=0.5): FR={fr_deg}, Hellinger={q108_deg_hel}, JS={q108_deg_js}, TV={q108_deg_tv}  → {cell_b_verdict} ({cell_b_hits}/3)", file=sys.stderr)
print(f"Cell C: top root = {q108_top5_report[0]['root']}, top-50 mass = {top50_mass:.3f}", file=sys.stderr)
print(f"FINAL VERDICT: {final_verdict}", file=sys.stderr)
print("=" * 70, file=sys.stderr)

# ---------------------------------------------------------------------------
# 11. Write JSON
# ---------------------------------------------------------------------------
def degree_distribution(deg):
    dist = Counter(deg.values())
    # include 0-deg (isolated) if any — MST connected so there should be none
    return dict(sorted(dist.items()))

summary = {
    'finding_id': 'h-new-131',
    'title': 'Q 108 al-Kawthar MST super-hub robustness',
    'pre_reg_sha256': prereg_sha,
    'seed': SEED,
    'date': '2026-04-17',
    'parent_finding': 'h-new-134',
    'parent_data': 'findings/phase-b-hypotheses/csv/h-new-111.json',
    'rules_tuple': '(114 surahs Hafs-Kūfan; K=500 QAC-STEM roots; no-tashkeel; QAC v0.4)',
    'locked_params': {
        'K_top_roots': K_TOP,
        'alpha_baseline_h_new_134': ALPHA_BASELINE,
        'alpha_cell_A_no_smoothing': ALPHA_CELL_A,
    },
    'bonferroni': {
        'k': 2,
        'alpha_bon': 0.025,
        'family': 'h-new-131-q108-supernode',
        'inferential_slots': ['Cell B JS', 'Cell B TV'],
        'cell_A_role': 'DESCRIPTIVE-ROBUSTNESS bright-line check (not an inferential Bonferroni slot)',
        'hellinger_role': 'rank-monotone consistency-check with Fisher-Rao (excluded from inferential family)',
        'amendment_note': 'audit-036 2026-04-17: tightening self-verifying per feedback_bonferroni_tightening_vs_loosening',
    },
    'sanity_replication': {
        'h_new_134_mst_fr_alpha_05_q108_degree': deg_fr_base[108],
        'expected': 24,
        'matches': deg_fr_base[108] == 24,
        'top10_hubs_fr_alpha_05': deg_fr_base.most_common(10),
        'degree_distribution_fr_alpha_05': degree_distribution(deg_fr_base),
    },
    'cell_A_dirichlet_robustness': {
        'alpha': ALPHA_CELL_A,
        'metric': 'Fisher-Rao arccos-Bhattacharyya',
        'q108_degree': q108_deg_A,
        'top10_hubs': deg_A.most_common(10),
        'degree_distribution': degree_distribution(deg_A),
        'thresholds': {'REFUTE_le': 5, 'WEAKLY_SURVIVE_6_14': True, 'SURVIVE_ge': 15},
        'verdict': cell_a_verdict,
    },
    'cell_B_cross_metric': {
        'alpha': ALPHA_BASELINE,
        'fisher_rao': {'q108_degree': fr_deg, 'top10': deg_fr_base.most_common(10)},
        'hellinger': {
            'q108_degree': q108_deg_hel,
            'top10': deg_hel.most_common(10),
            'matches_fisher_rao_mst': hellinger_matches_fr,
            'role': 'consistency-check (monotone with Fisher-Rao)',
        },
        'jensen_shannon': {'q108_degree': q108_deg_js, 'top10': deg_js.most_common(10)},
        'total_variation': {'q108_degree': q108_deg_tv, 'top10': deg_tv.most_common(10)},
        'cell_B_hits_of_3': cell_b_hits,
        'cell_B_hits_count_rule': '{FR, JS, TV} with deg ≥ 15; Hellinger not counted (redundant with FR)',
        'verdict': cell_b_verdict,
    },
    'cell_C_q108_descriptive': {
        'n_distinct_roots': len(q108_roots_present),
        'n_total_stem_root_tokens': sum(q108_roots_present.values()),
        'tokens_in_top_500': q108_raw_total,
        'top5_roots_by_q108_count': q108_top5_report,
        'alpha_05_probability_on_top50_global': top50_mass,
        'alpha_05_probability_on_top100_global': top100_mass,
        'unsmoothed_fraction_on_top50_global': raw_top50_frac,
    },
    'pre_committed_acceptance_matrix': {
        'SURVIVE+PASS': 'STRUCTURAL',
        'SURVIVE+FAIL': 'Fisher-Rao-specific',
        'WEAKLY+PASS': 'Weakly structural',
        'WEAKLY+FAIL': 'Weakly artifact',
        'REFUTE+any': 'REFUTED — smoothing artifact',
    },
    'final_verdict': final_verdict,
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False, default=str))
print(f"\nWrote summary JSON: {OUT_JSON}", file=sys.stderr)
