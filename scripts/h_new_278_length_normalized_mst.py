#!/usr/bin/env python3
"""H-NEW-278 - literal NM-36 length-normalized MST rerun for OQ-19.

Pre-registered (Bonferroni k=2, alpha_bon=0.025):
  Cell A - top-3 replication check.
           PASS if Q108 remains top-3 and at least 2 of baseline top-3
           {108, 7, 112} remain in the length-normalized top-3.
  Cell B - Q108 vs Q7 degree check.
           PASS if deg(Q108) > deg(Q7) under the length-normalized MST.
  MW-5 - deterministic label-permutation control on the length-normalized
         probability vectors. PASS if the degree multiset is unchanged
         and Q108's permuted degree differs from its empirical degree.

Design note: this is the literal NM-36 transformation
  x[i,r] = count[i,r] / N_i
before adding flat Dirichlet alpha=0.5. It is intentionally distinct
from H-NEW-131.1's per-surah-alpha residualization.
"""
import hashlib
import json
import math
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
SEED = 20260418
K_TOP = 500
ALPHA = 0.5

QAC_FILE = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
PREREG_FILE = (
    ROOT / "findings/phase-b-hypotheses/h-new-278-length-normalized-mst-prereg.md"
)
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-278.json"

LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")


def fisher_rao(p, q):
    bc = 0.0
    for a, b in zip(p, q):
        if a > 0.0 and b > 0.0:
            bc += math.sqrt(a * b)
    bc = max(-1.0, min(1.0, bc))
    return 2.0 * math.acos(bc)


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


def compute_distance_matrix(probabilities):
    d_matrix = [[0.0] * 115 for _ in range(115)]
    for i in range(1, 115):
        for j in range(i + 1, 115):
            d = fisher_rao(probabilities[i], probabilities[j])
            d_matrix[i][j] = d
            d_matrix[j][i] = d
    return d_matrix


def mst_kruskal(d_matrix):
    edges = []
    for i in range(1, 115):
        for j in range(i + 1, 115):
            edges.append((d_matrix[i][j], i, j))
    edges.sort()
    dsu = DSU(114)
    mst_edges = []
    for weight, i, j in edges:
        if dsu.union(i, j):
            mst_edges.append((i, j, weight))
            if len(mst_edges) == 113:
                break
    assert len(mst_edges) == 113
    return mst_edges


def degree_vector(mst_edges):
    degrees = Counter()
    for i, j, _ in mst_edges:
        degrees[i] += 1
        degrees[j] += 1
    return degrees


def rank_degrees(degrees):
    return sorted(((sid, degrees[sid]) for sid in range(1, 115)), key=lambda x: (-x[1], x[0]))


def neighbors_of(target_sid, mst_edges):
    neighbors = []
    for i, j, weight in mst_edges:
        if i == target_sid:
            neighbors.append((j, weight))
        elif j == target_sid:
            neighbors.append((i, weight))
    return sorted(neighbors, key=lambda x: (x[1], x[0]))


prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
print(f"SEED = {SEED}", file=sys.stderr)
print(f"K_TOP = {K_TOP}", file=sys.stderr)
print(f"ALPHA = {ALPHA}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 1. Parse QAC and build raw count matrix
# ---------------------------------------------------------------------------
per_surah_roots = defaultdict(list)
global_root_counts = Counter()

with open(QAC_FILE, encoding="utf-8") as handle:
    for line in handle:
        if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
            continue
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 4:
            continue
        match = LOC_RE.match(parts[0])
        if not match:
            continue
        sid = int(match.group(1))
        features = parts[3]
        if "STEM" not in features:
            continue
        root_match = ROOT_RE.search(features)
        if not root_match:
            continue
        root = root_match.group(1)
        per_surah_roots[sid].append(root)
        global_root_counts[root] += 1

assert len(per_surah_roots) == 114, f"Expected 114 surahs, got {len(per_surah_roots)}"

top_roots = [root for root, _ in global_root_counts.most_common(K_TOP)]
top_root_index = {root: idx for idx, root in enumerate(top_roots)}

counts = [[0.0] * K_TOP for _ in range(115)]
surah_total_tokens = {sid: len(per_surah_roots[sid]) for sid in range(1, 115)}
surah_topk_tokens = {sid: 0 for sid in range(1, 115)}

for sid in range(1, 115):
    for root in per_surah_roots[sid]:
        idx = top_root_index.get(root)
        if idx is None:
            continue
        counts[sid][idx] += 1.0
        surah_topk_tokens[sid] += 1

print(f"Q108 total STEM-root tokens = {surah_total_tokens[108]}", file=sys.stderr)
print(f"Q108 top-{K_TOP} tokens = {surah_topk_tokens[108]}", file=sys.stderr)
print(
    f"Q108 top-{K_TOP} coverage = {surah_topk_tokens[108] / surah_total_tokens[108]:.4f}",
    file=sys.stderr,
)


def build_probabilities_baseline():
    probabilities = [[0.0] * K_TOP for _ in range(115)]
    for sid in range(1, 115):
        smoothed = [value + ALPHA for value in counts[sid]]
        total_mass = sum(smoothed)
        probabilities[sid] = [value / total_mass for value in smoothed]
    return probabilities


def build_probabilities_length_normalized():
    probabilities = [[0.0] * K_TOP for _ in range(115)]
    for sid in range(1, 115):
        n_i = surah_total_tokens[sid]
        normalized_counts = [value / n_i for value in counts[sid]]
        smoothed = [value + ALPHA for value in normalized_counts]
        total_mass = sum(smoothed)
        probabilities[sid] = [value / total_mass for value in smoothed]
    return probabilities


# ---------------------------------------------------------------------------
# 2. Baseline replication
# ---------------------------------------------------------------------------
print("\n[baseline] Replicating H-NEW-134 / H-NEW-131...", file=sys.stderr)
prob_baseline = build_probabilities_baseline()
d_baseline = compute_distance_matrix(prob_baseline)
mst_baseline = mst_kruskal(d_baseline)
deg_baseline = degree_vector(mst_baseline)
ranked_baseline = rank_degrees(deg_baseline)
baseline_top3 = ranked_baseline[:3]
print(f"  baseline top-10 hubs: {ranked_baseline[:10]}", file=sys.stderr)
print(
    f"  baseline degrees: Q108={deg_baseline[108]}, Q7={deg_baseline[7]}, Q112={deg_baseline[112]}",
    file=sys.stderr,
)

baseline_matches_parent = baseline_top3 == [(108, 24), (7, 10), (112, 8)]
print(f"  baseline matches expected top-3: {baseline_matches_parent}", file=sys.stderr)

# ---------------------------------------------------------------------------
# 3. Literal NM-36 length-normalized rerun
# ---------------------------------------------------------------------------
print("\n[length-normalized] Running literal NM-36 rerun...", file=sys.stderr)
prob_length_norm = build_probabilities_length_normalized()
d_length_norm = compute_distance_matrix(prob_length_norm)
mst_length_norm = mst_kruskal(d_length_norm)
deg_length_norm = degree_vector(mst_length_norm)
ranked_length_norm = rank_degrees(deg_length_norm)
length_norm_top3 = ranked_length_norm[:3]
print(f"  length-normalized top-10 hubs: {ranked_length_norm[:10]}", file=sys.stderr)
print(
    f"  length-normalized degrees: Q108={deg_length_norm[108]}, Q7={deg_length_norm[7]}, Q112={deg_length_norm[112]}",
    file=sys.stderr,
)
print(f"  Q108 neighbors: {neighbors_of(108, mst_length_norm)}", file=sys.stderr)

baseline_top3_ids = {sid for sid, _ in baseline_top3}
length_norm_top3_ids = {sid for sid, _ in length_norm_top3}
top3_overlap_ids = sorted(baseline_top3_ids & length_norm_top3_ids)
q108_is_top3 = 108 in length_norm_top3_ids

cell_a_pass = q108_is_top3 and len(top3_overlap_ids) >= 2
cell_b_pass = deg_length_norm[108] > deg_length_norm[7]

print(
    f"  Cell A overlap ids = {top3_overlap_ids} ; q108_is_top3 = {q108_is_top3} ; "
    f"{'PASS' if cell_a_pass else 'FAIL'}",
    file=sys.stderr,
)
print(
    f"  Cell B Q108 vs Q7 = {deg_length_norm[108]} vs {deg_length_norm[7]} ; "
    f"{'PASS' if cell_b_pass else 'FAIL'}",
    file=sys.stderr,
)

# ---------------------------------------------------------------------------
# 4. MW-5 deterministic label-permutation control
# ---------------------------------------------------------------------------
print("\n[MW-5] Deterministic label-permutation control...", file=sys.stderr)
rng = random.Random(SEED)
permutation = list(range(1, 115))
rng.shuffle(permutation)

prob_permuted = [[0.0] * K_TOP for _ in range(115)]
for target_sid, source_sid in enumerate(permutation, start=1):
    prob_permuted[target_sid] = prob_length_norm[source_sid]

d_permuted = compute_distance_matrix(prob_permuted)
mst_permuted = mst_kruskal(d_permuted)
deg_permuted = degree_vector(mst_permuted)
ranked_permuted = rank_degrees(deg_permuted)

mw5_degree_multiset_same = sorted(deg_length_norm.values()) == sorted(deg_permuted.values())
mw5_q108_degree_changed = deg_permuted[108] != deg_length_norm[108]
mw5_pass = mw5_degree_multiset_same and mw5_q108_degree_changed

print(f"  permuted top-10 hubs: {ranked_permuted[:10]}", file=sys.stderr)
print(
    f"  permuted Q108 degree = {deg_permuted[108]} (empirical {deg_length_norm[108]})",
    file=sys.stderr,
)
print(
    f"  source surah assigned to label Q108 = {permutation[107]}",
    file=sys.stderr,
)
print(
    f"  degree multiset same = {mw5_degree_multiset_same} ; "
    f"Q108 degree changed = {mw5_q108_degree_changed} ; "
    f"{'PASS' if mw5_pass else 'FAIL'}",
    file=sys.stderr,
)

# ---------------------------------------------------------------------------
# 5. Final verdict
# ---------------------------------------------------------------------------
if not mw5_pass:
    final_verdict = "INSTRUMENT-BROKEN - label-permutation control failed"
elif cell_a_pass and cell_b_pass:
    final_verdict = (
        "REPLICATES - Q108 remains a genuine top-tier hub under literal NM-36 "
        "length-normalization"
    )
elif cell_a_pass and not cell_b_pass:
    final_verdict = (
        "PARTIAL-REPLICATION - top-3 survives but Q108 no longer outranks Q7"
    )
elif not cell_a_pass and cell_b_pass:
    final_verdict = (
        "PARTIAL-REPLICATION - Q108 beats Q7 but broader top-3 structure reorganizes"
    )
else:
    final_verdict = (
        "COLLAPSE-UNDER-LITERAL-LENGTH-NORMALIZATION - Q108 hub anomaly does not "
        "survive the NM-36 rerun"
    )

print("\n" + "=" * 72, file=sys.stderr)
print(f"FINAL VERDICT: {final_verdict}", file=sys.stderr)
print("=" * 72, file=sys.stderr)

# ---------------------------------------------------------------------------
# 6. Write JSON
# ---------------------------------------------------------------------------
summary = {
    "finding_id": "h-new-278",
    "title": "Length-normalized MST rerun for OQ-19 (literal NM-36 operationalization)",
    "pre_reg_sha256": prereg_sha,
    "seed": SEED,
    "date": "2026-04-18",
    "parent_finding": "h-new-131",
    "grandparent": "h-new-134",
    "rules_tuple": (
        "(114 surahs Hafs-Kufan; K=500 top QAC-STEM roots; Fisher-Rao "
        "arccos-Bhattacharyya; MST via Kruskal; no-tashkeel; QAC v0.4)"
    ),
    "locked_params": {
        "k_top_roots": K_TOP,
        "alpha": ALPHA,
        "length_normalization": "count[i,r] / total_stem_root_tokens_in_surah_i",
        "tie_break_ranking": "degree desc, surah_id asc",
    },
    "bonferroni": {
        "k": 2,
        "alpha_bon": 0.025,
        "family": "h-new-278-length-normalized-mst",
        "inferential_slots": [
            "Cell A top-3 replication",
            "Cell B Q108>Q7 degree comparison",
        ],
        "note": "Both slots are locked bright-line decisions on deterministic outputs.",
    },
    "baseline_replication": {
        "top10_hubs": ranked_baseline[:10],
        "top3": baseline_top3,
        "q108_degree": deg_baseline[108],
        "q7_degree": deg_baseline[7],
        "q112_degree": deg_baseline[112],
        "matches_expected_top3": baseline_matches_parent,
    },
    "length_normalized_rerun": {
        "top10_hubs": ranked_length_norm[:10],
        "top3": length_norm_top3,
        "top3_overlap_with_baseline_ids": top3_overlap_ids,
        "top3_overlap_count": len(top3_overlap_ids),
        "q108_is_top3": q108_is_top3,
        "q108_degree": deg_length_norm[108],
        "q7_degree": deg_length_norm[7],
        "q112_degree": deg_length_norm[112],
        "q108_minus_q7_degree": deg_length_norm[108] - deg_length_norm[7],
        "q108_neighbors": neighbors_of(108, mst_length_norm),
        "q108_total_stem_tokens": surah_total_tokens[108],
        "q108_top500_tokens": surah_topk_tokens[108],
        "q108_top500_coverage": surah_topk_tokens[108] / surah_total_tokens[108],
    },
    "cell_A_top3_replication": {
        "baseline_top3_ids": sorted(baseline_top3_ids),
        "length_normalized_top3_ids": sorted(length_norm_top3_ids),
        "overlap_ids": top3_overlap_ids,
        "q108_is_top3": q108_is_top3,
        "pass": cell_a_pass,
    },
    "cell_B_q108_vs_q7": {
        "q108_degree": deg_length_norm[108],
        "q7_degree": deg_length_norm[7],
        "degree_gap_q108_minus_q7": deg_length_norm[108] - deg_length_norm[7],
        "pass": cell_b_pass,
    },
    "mw5_label_permutation": {
        "seed": SEED,
        "permutation": permutation,
        "permuted_top10_hubs": ranked_permuted[:10],
        "permuted_q108_degree": deg_permuted[108],
        "source_surah_assigned_to_q108": permutation[107],
        "degree_multiset_same": mw5_degree_multiset_same,
        "q108_degree_changed": mw5_q108_degree_changed,
        "pass": mw5_pass,
    },
    "final_verdict": final_verdict,
}

OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False))
print(f"Wrote: {OUT_JSON}", file=sys.stderr)
