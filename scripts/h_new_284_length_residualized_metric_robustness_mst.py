#!/usr/bin/env python3
"""H-NEW-284 - length-residualized metric-robustness MST follow-up for OQ-19.

This run reuses the H-NEW-131.1 Cell B residualized simplex and reruns the
H-NEW-279 locked primary metric family only:
  - Fisher-Rao
  - Jensen-Shannon
  - Total variation
  - Euclidean L2
  - Cosine-angle

Primary statistic:
  C_LR = number of metrics for which rank(Q108) <= 3

The output is a bounded descriptive adjudication of whether the surviving
Q108 residue remains metric-robust after length equalization.
"""

import hashlib
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
SEED = 20260418
K_TOP = 500
ALPHA_BASE = 0.5
Q108 = 108

QAC_FILE = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
PREREG_FILE = (
    ROOT
    / "findings/phase-b-hypotheses/h-new-284-length-residualized-metric-robustness-mst-prereg.md"
)
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-284.json"

LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")

PRIMARY_METRICS = [
    "fisher_rao",
    "jensen_shannon",
    "total_variation",
    "euclidean_l2",
    "cosine_angle",
]


def fisher_rao(p, q):
    bc = 0.0
    for a, b in zip(p, q):
        if a > 0.0 and b > 0.0:
            bc += math.sqrt(a * b)
    bc = min(1.0, max(-1.0, bc))
    return 2.0 * math.acos(bc)


def jensen_shannon(p, q):
    s = 0.0
    for a, b in zip(p, q):
        m = 0.5 * (a + b)
        if a > 0.0:
            s += 0.5 * a * math.log(a / m)
        if b > 0.0:
            s += 0.5 * b * math.log(b / m)
    return math.sqrt(max(0.0, s))


def total_variation(p, q):
    return 0.5 * sum(abs(a - b) for a, b in zip(p, q))


def euclidean_l2(p, q):
    s = 0.0
    for a, b in zip(p, q):
        d = a - b
        s += d * d
    return math.sqrt(s)


def cosine_angle(p, q):
    dot = 0.0
    np = 0.0
    nq = 0.0
    for a, b in zip(p, q):
        dot += a * b
        np += a * a
        nq += b * b
    denom = math.sqrt(np) * math.sqrt(nq)
    if denom == 0.0:
        return 0.0
    cos = dot / denom
    cos = min(1.0, max(-1.0, cos))
    return math.acos(cos)


METRIC_FUNCS = {
    "fisher_rao": fisher_rao,
    "jensen_shannon": jensen_shannon,
    "total_variation": total_variation,
    "euclidean_l2": euclidean_l2,
    "cosine_angle": cosine_angle,
}


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


def build_distance_matrix(prob, metric_name):
    metric = METRIC_FUNCS[metric_name]
    d_matrix = [[0.0] * 115 for _ in range(115)]
    for i in range(1, 115):
        for j in range(i + 1, 115):
            d = metric(prob[i], prob[j])
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
    if len(mst_edges) != 113:
        raise RuntimeError(f"MST incomplete: {len(mst_edges)} edges")
    return mst_edges


def degree_vector(mst_edges):
    degrees = Counter()
    for i, j, _ in mst_edges:
        degrees[i] += 1
        degrees[j] += 1
    return degrees


def ranked_degrees(degrees):
    return sorted(
        ((sid, degrees[sid]) for sid in range(1, 115)),
        key=lambda item: (-item[1], item[0]),
    )


def competition_rank(degrees, sid):
    target = degrees[sid]
    return 1 + sum(1 for node in range(1, 115) if degrees[node] > target)


def residualized_probabilities(counts, total_tokens):
    mean_tokens = sum(total_tokens.values()) / len(total_tokens)
    probabilities = [[0.0] * K_TOP for _ in range(115)]
    effective_alpha = {}
    for sid in range(1, 115):
        n_i = total_tokens[sid]
        if n_i <= 0:
            raise RuntimeError(f"Surah {sid} has zero STEM-root tokens")
        alpha_i = ALPHA_BASE * (mean_tokens / n_i)
        effective_alpha[sid] = alpha_i
        smoothed = [value + alpha_i for value in counts[sid]]
        row_sum = sum(smoothed)
        probabilities[sid] = [v / row_sum for v in smoothed]
    return probabilities, mean_tokens, effective_alpha


def q108_neighbors(mst_edges):
    neighbors = []
    for i, j, weight in mst_edges:
        if i == Q108:
            neighbors.append((j, weight))
        elif j == Q108:
            neighbors.append((i, weight))
    return sorted(neighbors, key=lambda item: (item[1], item[0]))


def verdict_from_count(c_lr):
    if c_lr >= 4:
        return "METRIC-ROBUST RESIDUE"
    if c_lr >= 2:
        return "PARTIAL METRIC-ROBUST RESIDUE"
    if c_lr == 1:
        return "METRIC-SPECIFIC RESIDUE"
    return "NOT ROBUST AFTER LENGTH EQUALIZATION"


def main():
    prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
    print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
    print(f"SEED = {SEED}", file=sys.stderr)
    print(f"K_TOP = {K_TOP}", file=sys.stderr)
    print(f"ALPHA_BASE = {ALPHA_BASE}", file=sys.stderr)
    print(f"PRIMARY_METRICS = {PRIMARY_METRICS}", file=sys.stderr)

    per_surah_roots = defaultdict(list)
    global_root_counts = Counter()

    with open(QAC_FILE, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            match = LOC_RE.match(parts[0])
            if not match:
                continue
            sid = int(match.group(1))
            feat = parts[3]
            if "STEM" not in feat:
                continue
            rm = ROOT_RE.search(feat)
            if not rm:
                continue
            root = rm.group(1)
            per_surah_roots[sid].append(root)
            global_root_counts[root] += 1

    if len(per_surah_roots) != 114:
        raise RuntimeError(f"Expected 114 surahs, got {len(per_surah_roots)}")

    top_roots = [root for root, _ in global_root_counts.most_common(K_TOP)]
    top_root_index = {root: idx for idx, root in enumerate(top_roots)}

    counts = [[0.0] * K_TOP for _ in range(115)]
    total_tokens = {sid: len(per_surah_roots[sid]) for sid in range(1, 115)}
    top500_tokens = {sid: 0 for sid in range(1, 115)}

    for sid in range(1, 115):
        for root in per_surah_roots[sid]:
            idx = top_root_index.get(root)
            if idx is None:
                continue
            counts[sid][idx] += 1.0
            top500_tokens[sid] += 1

    prob, mean_tokens, effective_alpha = residualized_probabilities(counts, total_tokens)

    print(f"mean STEM-root tokens = {mean_tokens:.2f}", file=sys.stderr)
    print(f"Q108 total STEM-root tokens = {total_tokens[Q108]}", file=sys.stderr)
    print(f"Q108 top-{K_TOP} tokens = {top500_tokens[Q108]}", file=sys.stderr)
    print(
        f"Q108 top-{K_TOP} coverage = {top500_tokens[Q108] / total_tokens[Q108]:.4f}",
        file=sys.stderr,
    )
    print(
        f"Q108 effective alpha_i = {effective_alpha[Q108]:.4f}",
        file=sys.stderr,
    )
    print(
        f"Q2 effective alpha_i = {effective_alpha[2]:.4f}",
        file=sys.stderr,
    )
    print(
        f"alpha_i range = [{min(effective_alpha.values()):.4f}, {max(effective_alpha.values()):.4f}]",
        file=sys.stderr,
    )

    metric_results = {}
    top3_counts = Counter()

    for metric_name in PRIMARY_METRICS:
        print(f"\n[{metric_name}] building D and MST on length-residualized simplex...", file=sys.stderr)
        d_matrix = build_distance_matrix(prob, metric_name)
        mst_edges = mst_kruskal(d_matrix)
        degrees = degree_vector(mst_edges)
        q108_degree = degrees[Q108]
        q108_rank = competition_rank(degrees, Q108)
        top10 = degrees.most_common(10)
        q108_top3 = q108_rank <= 3
        for sid in range(1, 115):
            if competition_rank(degrees, sid) <= 3:
                top3_counts[sid] += 1
        metric_results[metric_name] = {
            "q108_degree": q108_degree,
            "q108_rank": q108_rank,
            "q108_top3": q108_top3,
            "top10_hubs": top10,
            "degree_distribution": dict(Counter(degrees.values())),
            "mst_edges": [[i, j, round(w, 12)] for i, j, w in mst_edges],
            "q108_neighbors": [[sid, round(weight, 12)] for sid, weight in q108_neighbors(mst_edges)],
        }
        print(
            f"  Q108 degree={q108_degree} rank={q108_rank} top3={q108_top3}",
            file=sys.stderr,
        )
        print(f"  top10={top10}", file=sys.stderr)
        print(f"  Q108 neighbors={q108_neighbors(mst_edges)}", file=sys.stderr)

    c_lr = sum(1 for metric_name in PRIMARY_METRICS if metric_results[metric_name]["q108_top3"])
    verdict = verdict_from_count(c_lr)

    consensus_top3 = sorted(
        ((sid, count) for sid, count in top3_counts.items()),
        key=lambda item: (-item[1], item[0]),
    )

    print("\n" + "=" * 72, file=sys.stderr)
    print(f"C_LR = {c_lr}/5", file=sys.stderr)
    print(f"FINAL VERDICT: {verdict}", file=sys.stderr)
    print("=" * 72, file=sys.stderr)

    out = {
        "finding_id": "h-new-284",
        "title": "Length-residualized metric-robustness MST follow-up for OQ-19",
        "pre_reg_sha256": prereg_sha,
        "seed": SEED,
        "date": "2026-04-18",
        "parent_backdrop": ["h-new-131.1", "h-new-279", "h-new-282"],
        "rules_tuple": (
            "(114 surahs Hafs-Kufan; K=500 top QAC-STEM roots; "
            "length-residualized Dirichlet alpha_i = alpha_base * (mean_surah_tokens / surah_i_tokens); "
            "alpha_base=0.5; MST via Kruskal; no-tashkeel; QAC v0.4)"
        ),
        "scope_note": (
            "Residualized simplex inherited from H-NEW-131.1 Cell B; "
            "metric family inherited from H-NEW-279; no new null is claimed."
        ),
        "primary_metric_family": PRIMARY_METRICS,
        "primary_statistic": "C_LR = number of metrics where rank(Q108) <= 3",
        "decision_rule": {
            "metric_robust_residue": "C_LR >= 4",
            "partial_metric_robust_residue": "C_LR in {2,3}",
            "not_robust": "C_LR <= 1",
        },
        "sanity_checks": {
            "q108_fisher_rao_degree": metric_results["fisher_rao"]["q108_degree"],
            "q108_fisher_rao_rank": metric_results["fisher_rao"]["q108_rank"],
            "q108_length_residualized_degree_expected_from_h131_1": 16,
        },
        "length_residualization": {
            "alpha_base": ALPHA_BASE,
            "mean_surah_tokens": mean_tokens,
            "q108_total_stem_tokens": total_tokens[Q108],
            "q108_top500_tokens": top500_tokens[Q108],
            "q108_top500_coverage": top500_tokens[Q108] / total_tokens[Q108],
            "q108_effective_alpha": effective_alpha[Q108],
            "q2_effective_alpha": effective_alpha[2],
            "alpha_i_min": min(effective_alpha.values()),
            "alpha_i_max": max(effective_alpha.values()),
        },
        "per_metric": metric_results,
        "primary_summary": {
            "c_lr_of_5": c_lr,
            "threshold_for_metric_robust_residue": 4,
            "verdict": verdict,
            "top3_appearance_counts": consensus_top3,
        },
    }

    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote: {OUT_JSON}", file=sys.stderr)


if __name__ == "__main__":
    main()
