#!/usr/bin/env python3
"""H-NEW-279 — bounded MST metric-robustness pass for the Q108 hub anomaly.

Primary family (5 non-redundant metrics on the same alpha=0.5 simplex):
  - Fisher-Rao
  - Jensen-Shannon
  - Total variation
  - Euclidean L2
  - Cosine-angle

Diagnostic only:
  - Hellinger, expected to match Fisher-Rao MST exactly

The goal is a bounded descriptive robustness classification:
Q108 is a "metric-robust hub" iff it ranks top-3 by MST degree on at least
4 of the 5 primary metrics.

Seed 20260418. Deterministic.
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
DIRICHLET_ALPHA = 0.5
Q108 = 108

QAC_FILE = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
PREREG_FILE = (
    ROOT / "findings/phase-b-hypotheses/h-new-279-metric-robustness-mst-prereg.md"
)
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-279.json"

LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")

PRIMARY_METRICS = [
    "fisher_rao",
    "jensen_shannon",
    "total_variation",
    "euclidean_l2",
    "cosine_angle",
]
ALL_METRICS = PRIMARY_METRICS + ["hellinger"]


def fisher_rao(p, q):
    bc = 0.0
    for a, b in zip(p, q):
        bc += math.sqrt(a * b)
    bc = min(1.0, max(-1.0, bc))
    return 2.0 * math.acos(bc)


def hellinger(p, q):
    s = 0.0
    for a, b in zip(p, q):
        d = math.sqrt(a) - math.sqrt(b)
        s += d * d
    return math.sqrt(0.5 * s)


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
    "hellinger": hellinger,
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
    D = [[0.0] * 115 for _ in range(115)]
    for i in range(1, 115):
        for j in range(i + 1, 115):
            d = metric(prob[i], prob[j])
            D[i][j] = d
            D[j][i] = d
    return D


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
    if len(mst_edges) != 113:
        raise RuntimeError(f"MST incomplete: {len(mst_edges)} edges")
    return mst_edges


def degree_vector(mst_edges):
    deg = Counter()
    for i, j, _ in mst_edges:
        deg[i] += 1
        deg[j] += 1
    return deg


def competition_rank(deg, sid):
    target = deg[sid]
    return 1 + sum(1 for node in range(1, 115) if deg[node] > target)


def edge_set(mst_edges):
    return {
        (min(i, j), max(i, j))
        for i, j, _ in mst_edges
    }


def verdict_from_count(top3_count):
    if top3_count >= 4:
        return "METRIC-ROBUST HUB"
    if top3_count >= 2:
        return "PARTIAL METRIC-ROBUSTNESS"
    if top3_count == 1:
        return "METRIC-SPECIFIC"
    return "NOT ROBUST"


def main():
    prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
    print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
    print(f"SEED = {SEED}", file=sys.stderr)
    print(f"K_TOP = {K_TOP}", file=sys.stderr)
    print(f"DIRICHLET_ALPHA = {DIRICHLET_ALPHA}", file=sys.stderr)
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
            m = LOC_RE.match(parts[0])
            if not m:
                continue
            sid = int(m.group(1))
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

    top_roots = [r for r, _ in global_root_counts.most_common(K_TOP)]
    top_root_index = {r: i for i, r in enumerate(top_roots)}

    counts = [[0.0] * K_TOP for _ in range(115)]
    for sid in range(1, 115):
        for root in per_surah_roots.get(sid, []):
            idx = top_root_index.get(root)
            if idx is not None:
                counts[sid][idx] += 1.0

    prob = [[0.0] * K_TOP for _ in range(115)]
    for sid in range(1, 115):
        smoothed = [c + DIRICHLET_ALPHA for c in counts[sid]]
        row_sum = sum(smoothed)
        prob[sid] = [v / row_sum for v in smoothed]

    metric_results = {}
    top3_counts = Counter()
    fr_edges = None

    for metric_name in ALL_METRICS:
        print(f"\n[{metric_name}] building D and MST...", file=sys.stderr)
        D = build_distance_matrix(prob, metric_name)
        mst_edges = mst_kruskal(D)
        deg = degree_vector(mst_edges)
        rank = competition_rank(deg, Q108)
        top10 = deg.most_common(10)
        q108_top3 = rank <= 3

        if metric_name in PRIMARY_METRICS:
            for sid in range(1, 115):
                if competition_rank(deg, sid) <= 3:
                    top3_counts[sid] += 1

        if metric_name == "fisher_rao":
            fr_edges = edge_set(mst_edges)

        metric_results[metric_name] = {
            "q108_degree": deg[Q108],
            "q108_rank": rank,
            "q108_top3": q108_top3,
            "top10_hubs": top10,
            "degree_distribution": dict(Counter(deg.values())),
            "mst_edges": [[i, j, round(w, 12)] for i, j, w in mst_edges],
        }

        print(
            f"  Q108 degree={deg[Q108]} rank={rank} top3={q108_top3}",
            file=sys.stderr,
        )
        print(f"  top10={top10}", file=sys.stderr)

    fr_degree = metric_results["fisher_rao"]["q108_degree"]
    fr_replication_pass = fr_degree == 24
    if not fr_replication_pass:
        print(
            f"ERROR: Fisher-Rao replication failed, expected Q108 degree 24 got {fr_degree}",
            file=sys.stderr,
        )

    hellinger_edges = edge_set(
        [(i, j, w) for i, j, w in metric_results["hellinger"]["mst_edges"]]
    )
    hellinger_matches_fr = hellinger_edges == fr_edges
    if not hellinger_matches_fr:
        print("ERROR: Hellinger MST does not match Fisher-Rao MST", file=sys.stderr)

    q108_top3_count = sum(
        1 for metric_name in PRIMARY_METRICS if metric_results[metric_name]["q108_top3"]
    )
    verdict = verdict_from_count(q108_top3_count)

    consensus_top3 = sorted(
        ((sid, count) for sid, count in top3_counts.items()),
        key=lambda item: (-item[1], item[0]),
    )

    out = {
        "finding_id": "h-new-279",
        "title": "Metric-robustness MST — bounded five-metric pass for the Q108 hub anomaly",
        "pre_reg_sha256": prereg_sha,
        "seed": SEED,
        "date": "2026-04-18",
        "parent_backdrop": ["h-new-134", "h-new-131", "h-new-131.1"],
        "rules_tuple": "(114 surahs Hafs-Kufan; K=500 QAC-STEM roots; Dirichlet alpha=0.5; MST via Kruskal; QAC v0.4)",
        "scope_note": "Primary family locked to 5 non-redundant metrics; Hellinger diagnostic only; KL excluded because no symmetric metric convention was pre-locked for this MST line.",
        "primary_metric_family": PRIMARY_METRICS,
        "diagnostic_metric": "hellinger",
        "rank_method": "competition rank = 1 + number of surahs with strictly higher MST degree",
        "sanity_checks": {
            "fisher_rao_q108_degree_expected": 24,
            "fisher_rao_q108_degree_observed": fr_degree,
            "fisher_rao_replication_pass": fr_replication_pass,
            "hellinger_matches_fisher_rao_mst_edge_set": hellinger_matches_fr,
        },
        "per_metric": {
            metric_name: {
                "q108_degree": metric_results[metric_name]["q108_degree"],
                "q108_rank": metric_results[metric_name]["q108_rank"],
                "q108_top3": metric_results[metric_name]["q108_top3"],
                "top10_hubs": metric_results[metric_name]["top10_hubs"],
                "degree_distribution": metric_results[metric_name]["degree_distribution"],
            }
            for metric_name in ALL_METRICS
        },
        "primary_summary": {
            "q108_top3_count_of_5": q108_top3_count,
            "threshold_for_metric_robust_hub": 4,
            "verdict": verdict,
            "top3_appearance_counts": consensus_top3,
        },
    }

    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nWrote {OUT_JSON}", file=sys.stderr)
    print(
        f"Primary verdict: {verdict} (Q108 top-3 on {q108_top3_count}/5 primary metrics)",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
