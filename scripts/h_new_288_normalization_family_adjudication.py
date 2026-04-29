#!/usr/bin/env python3
"""H-NEW-288 - normalization-family adjudication for OQ-19.

This run holds the H-NEW-279 five-metric MST panel fixed and compares:
  A. literal count / N_i normalization with flat alpha=0.5
  B. per-surah alpha_i residualized smoothing

Primary statistic:
  Delta_C = C_res - C_lit
where C_* is the number of the 5 primary metrics for which rank(Q108) <= 3.

The goal is a bounded descriptive separation of the two length-control
families already on the board after H-NEW-278 / 282 / 284.
"""

import hashlib
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
SEED = 20260419
K_TOP = 500
ALPHA = 0.5
Q108 = 108
Q7 = 7

QAC_FILE = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
PREREG_FILE = (
    ROOT
    / "findings/phase-b-hypotheses/h-new-288-normalization-family-adjudication-prereg.md"
)
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-288.json"

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


def build_distance_matrix(probabilities, metric_name):
    metric = METRIC_FUNCS[metric_name]
    d_matrix = [[0.0] * 115 for _ in range(115)]
    for i in range(1, 115):
        for j in range(i + 1, 115):
            d = metric(probabilities[i], probabilities[j])
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


def competition_rank(degrees, sid):
    target = degrees[sid]
    return 1 + sum(1 for node in range(1, 115) if degrees[node] > target)


def q108_neighbors(mst_edges):
    neighbors = []
    for i, j, weight in mst_edges:
        if i == Q108:
            neighbors.append((j, weight))
        elif j == Q108:
            neighbors.append((i, weight))
    return sorted(neighbors, key=lambda item: (item[1], item[0]))


def verdict_from_counts(c_lit, c_res):
    delta_c = c_res - c_lit
    if delta_c >= 3 and c_res >= 4:
        return "RESIDUALIZED-FAMILY-DOMINANCE"
    if delta_c in (1, 2) and c_res > c_lit:
        return "PARTIAL-RESIDUALIZED-ADVANTAGE"
    if delta_c == 0:
        return "NO-FAMILY-SEPARATION"
    return "LITERAL-FAMILY-ADVANTAGE"


def parse_qac_counts():
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

    return counts, total_tokens, top500_tokens


def build_literal_probabilities(counts, total_tokens):
    probabilities = [[0.0] * K_TOP for _ in range(115)]
    for sid in range(1, 115):
        n_i = total_tokens[sid]
        normalized_counts = [value / n_i for value in counts[sid]]
        smoothed = [value + ALPHA for value in normalized_counts]
        row_sum = sum(smoothed)
        probabilities[sid] = [value / row_sum for value in smoothed]
    return probabilities


def build_residualized_probabilities(counts, total_tokens):
    mean_tokens = sum(total_tokens.values()) / len(total_tokens)
    probabilities = [[0.0] * K_TOP for _ in range(115)]
    effective_alpha = {}
    for sid in range(1, 115):
        n_i = total_tokens[sid]
        alpha_i = ALPHA * (mean_tokens / n_i)
        effective_alpha[sid] = alpha_i
        smoothed = [value + alpha_i for value in counts[sid]]
        row_sum = sum(smoothed)
        probabilities[sid] = [value / row_sum for value in smoothed]
    return probabilities, mean_tokens, effective_alpha


def run_family(probabilities):
    per_metric = {}
    top3_count = 0

    for metric_name in PRIMARY_METRICS:
        print(f"[{metric_name}] building D and MST...", file=sys.stderr)
        d_matrix = build_distance_matrix(probabilities, metric_name)
        mst_edges = mst_kruskal(d_matrix)
        degrees = degree_vector(mst_edges)
        q108_rank = competition_rank(degrees, Q108)
        q108_top3 = q108_rank <= 3
        if q108_top3:
            top3_count += 1
        per_metric[metric_name] = {
            "q108_degree": degrees[Q108],
            "q108_rank": q108_rank,
            "q108_top3": q108_top3,
            "q7_degree": degrees[Q7],
            "top10_hubs": degrees.most_common(10),
            "degree_distribution": dict(Counter(degrees.values())),
            "q108_neighbors": [
                [sid, round(weight, 12)]
                for sid, weight in q108_neighbors(mst_edges)
            ],
        }
        print(
            f"  Q108 degree={degrees[Q108]} rank={q108_rank} top3={q108_top3} ; "
            f"Q7 degree={degrees[Q7]}",
            file=sys.stderr,
        )
        print(f"  top10={degrees.most_common(10)}", file=sys.stderr)
        print(f"  Q108 neighbors={q108_neighbors(mst_edges)}", file=sys.stderr)

    return per_metric, top3_count


def main():
    prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
    print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
    print(f"SEED = {SEED}", file=sys.stderr)
    print(f"K_TOP = {K_TOP}", file=sys.stderr)
    print(f"ALPHA = {ALPHA}", file=sys.stderr)
    print(f"PRIMARY_METRICS = {PRIMARY_METRICS}", file=sys.stderr)

    counts, total_tokens, top500_tokens = parse_qac_counts()

    print(f"Q108 total STEM-root tokens = {total_tokens[Q108]}", file=sys.stderr)
    print(f"Q108 top-{K_TOP} tokens = {top500_tokens[Q108]}", file=sys.stderr)
    print(
        f"Q108 top-{K_TOP} coverage = {top500_tokens[Q108] / total_tokens[Q108]:.4f}",
        file=sys.stderr,
    )

    print("\n[literal_family]", file=sys.stderr)
    literal_prob = build_literal_probabilities(counts, total_tokens)
    literal_per_metric, c_lit = run_family(literal_prob)

    print("\n[residualized_family]", file=sys.stderr)
    residualized_prob, mean_tokens, effective_alpha = build_residualized_probabilities(
        counts, total_tokens
    )
    residualized_per_metric, c_res = run_family(residualized_prob)

    literal_fr = literal_per_metric["fisher_rao"]
    residualized_fr = residualized_per_metric["fisher_rao"]
    literal_anchor_pass = (
        literal_fr["q108_degree"] == 1 and literal_fr["q7_degree"] == 15
    )
    residualized_anchor_pass = (
        residualized_fr["q108_degree"] == 16 and residualized_fr["q108_rank"] == 1
    )
    instrument_ok = literal_anchor_pass and residualized_anchor_pass

    delta_c = c_res - c_lit
    verdict = (
        verdict_from_counts(c_lit, c_res)
        if instrument_ok
        else "INSTRUMENT-BROKEN"
    )

    out = {
        "finding_id": "h-new-288",
        "title": "Normalization-family adjudication for OQ-19",
        "pre_reg_sha256": prereg_sha,
        "seed": SEED,
        "date": "2026-04-19",
        "parent_backdrop": ["h-new-278", "h-new-279", "h-new-282", "h-new-284"],
        "rules_tuple": "(114 surahs Hafs-Kufan; K=500 top QAC-STEM roots; MST via Kruskal; no-tashkeel; QAC v0.4; primary metrics = Fisher-Rao / Jensen-Shannon / total variation / Euclidean L2 / cosine-angle)",
        "scope_note": "Held-fixed metric panel, direct comparison of literal normalization versus residualized smoothing families only.",
        "primary_metric_family": PRIMARY_METRICS,
        "primary_statistics": {
            "c_lit": c_lit,
            "c_res": c_res,
            "delta_c": delta_c,
        },
        "decision_rule": {
            "residualized_family_dominance": "delta_c >= 3 and c_res >= 4",
            "partial_residualized_advantage": "delta_c in {1,2} and c_res > c_lit",
            "no_family_separation": "delta_c = 0",
            "literal_family_advantage": "delta_c < 0",
        },
        "sanity_checks": {
            "literal_fisher_rao_expected": {"q108_degree": 1, "q7_degree": 15},
            "literal_fisher_rao_observed": {
                "q108_degree": literal_fr["q108_degree"],
                "q7_degree": literal_fr["q7_degree"],
            },
            "literal_anchor_pass": literal_anchor_pass,
            "residualized_fisher_rao_expected": {"q108_degree": 16, "q108_rank": 1},
            "residualized_fisher_rao_observed": {
                "q108_degree": residualized_fr["q108_degree"],
                "q108_rank": residualized_fr["q108_rank"],
            },
            "residualized_anchor_pass": residualized_anchor_pass,
            "instrument_ok": instrument_ok,
        },
        "length_context": {
            "alpha": ALPHA,
            "mean_surah_tokens": mean_tokens,
            "q108_total_stem_tokens": total_tokens[Q108],
            "q108_top500_tokens": top500_tokens[Q108],
            "q108_top500_coverage": top500_tokens[Q108] / total_tokens[Q108],
            "q108_effective_alpha_residualized": effective_alpha[Q108],
            "q2_effective_alpha_residualized": effective_alpha[2],
        },
        "literal_family": {
            "family_label": "count / N_i then flat alpha=0.5",
            "c_top3": c_lit,
            "per_metric": literal_per_metric,
        },
        "residualized_family": {
            "family_label": "raw counts plus alpha_i = 0.5 * mean_tokens / N_i",
            "c_top3": c_res,
            "per_metric": residualized_per_metric,
        },
        "verdict": verdict,
    }

    OUT_JSON.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"\nWrote {OUT_JSON}", file=sys.stderr)
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
