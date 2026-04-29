#!/usr/bin/env python3
"""H-NEW-288.1 - Q108 residualized-pool medoid test."""

from __future__ import annotations

import csv
import hashlib
import json
import math
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path("/Users/grey/Downloads/quran")
SEED = 20260419
K_TOP = 500
ALPHA = 0.5
Q108 = 108

QAC_FILE = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
REVELATION_FILE = ROOT / "data/revelation-order.csv"
VERSE_COUNT_FILE = ROOT / "data/hafs-verse-counts.tsv"
PREREG_FILE = ROOT / "findings/phase-b-hypotheses/h-new-288-1-q108-residualized-pool-medoid-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-288-1.json"

LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")

PRIMARY_METRICS = [
    "fisher_rao",
    "jensen_shannon",
    "euclidean_l2",
    "cosine_angle",
]
DIAGNOSTIC_METRICS = ["total_variation"]


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
    return math.sqrt(sum((a - b) * (a - b) for a, b in zip(p, q)))


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


def load_pool():
    early_meccan = set()
    with open(REVELATION_FILE, encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            if row["noldeke_phase"] == "Early Meccan":
                early_meccan.add(int(row["mushaf_order"]))

    verse_counts = {}
    with open(VERSE_COUNT_FILE, encoding="utf-8") as handle:
        for line in handle:
            sid, n = line.rstrip("\n").split("\t")
            verse_counts[int(sid)] = int(n)

    pool = sorted(sid for sid in early_meccan if verse_counts[sid] <= 17)
    return pool, verse_counts


def mean_pairwise_distance(probabilities, pool, metric_name):
    metric = METRIC_FUNCS[metric_name]
    dbar = {}
    for sid in pool:
        dists = [metric(probabilities[sid], probabilities[other]) for other in pool if other != sid]
        dbar[sid] = statistics.mean(dists)
    return dbar


def competition_rank_from_scores(scores, sid):
    target = scores[sid]
    return 1 + sum(1 for other, value in scores.items() if other != sid and value < target)


def top_sorted(scores, n=5):
    return sorted(scores.items(), key=lambda item: (item[1], item[0]))[:n]


def main():
    prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
    print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
    print(f"SEED = {SEED}", file=sys.stderr)
    print(f"K_TOP = {K_TOP}", file=sys.stderr)
    print(f"ALPHA = {ALPHA}", file=sys.stderr)

    counts, total_tokens, top500_tokens = parse_qac_counts()
    pool, verse_counts = load_pool()
    literal_prob = build_literal_probabilities(counts, total_tokens)
    residual_prob, mean_tokens, effective_alpha = build_residualized_probabilities(counts, total_tokens)

    primary_rows = []
    diagnostic_rows = []
    rank_gaps = []
    c_res = 0

    for metric_name in PRIMARY_METRICS + DIAGNOSTIC_METRICS:
        lit_scores = mean_pairwise_distance(literal_prob, pool, metric_name)
        res_scores = mean_pairwise_distance(residual_prob, pool, metric_name)
        lit_rank = competition_rank_from_scores(lit_scores, Q108)
        res_rank = competition_rank_from_scores(res_scores, Q108)
        row = {
            "metric": metric_name,
            "literal_q108_mean_distance": lit_scores[Q108],
            "literal_q108_rank": lit_rank,
            "literal_top5_medoids": [[sid, score] for sid, score in top_sorted(lit_scores)],
            "residualized_q108_mean_distance": res_scores[Q108],
            "residualized_q108_rank": res_rank,
            "residualized_top5_medoids": [[sid, score] for sid, score in top_sorted(res_scores)],
            "rank_gap_literal_minus_residualized": lit_rank - res_rank,
        }
        if metric_name in PRIMARY_METRICS:
            primary_rows.append(row)
            rank_gaps.append(lit_rank - res_rank)
            if res_rank == 1:
                c_res += 1
        else:
            diagnostic_rows.append(row)
        print(
            f"[{metric_name}] lit_rank(Q108)={lit_rank} res_rank(Q108)={res_rank} gap={lit_rank - res_rank}",
            file=sys.stderr,
        )

    delta_med = statistics.median(rank_gaps)
    verdict = (
        "POOL-MEDOID-SEPARATION"
        if c_res >= 3 and delta_med >= 10
        else "NO-CLEAN-POOL-MEDOID-SEPARATION"
    )

    out = {
        "finding_id": "h-new-288-1",
        "title": "Q108 residualized-pool medoid test",
        "pre_reg_sha256": prereg_sha,
        "seed": SEED,
        "date": "2026-04-19",
        "parent_backdrop": ["h-new-273", "h-new-284", "h-new-288"],
        "rules_tuple": "(114 surahs; QAC v0.4 STEM roots; K=500 top roots; literal family = count/N_i plus flat alpha=0.5; residualized family = raw counts plus alpha_i = 0.5 * mean_tokens / N_i; fixed pool P defined from revelation-order.csv and hafs-verse-counts.tsv only; mean pairwise distance medoid ranks computed inside P; primary metrics = Fisher-Rao, Jensen-Shannon, Euclidean L2, cosine-angle; total variation diagnostic only)",
        "pool_definition": {
            "noldeke_phase": "Early Meccan",
            "verse_count_max": 17,
            "pool_surahs": pool,
            "pool_size": len(pool),
            "pool_verse_counts": {str(sid): verse_counts[sid] for sid in pool},
        },
        "length_context": {
            "mean_surah_tokens": mean_tokens,
            "q108_total_stem_tokens": total_tokens[Q108],
            "q108_top500_tokens": top500_tokens[Q108],
            "q108_top500_coverage": top500_tokens[Q108] / total_tokens[Q108],
            "q108_effective_alpha_residualized": effective_alpha[Q108],
        },
        "primary_metrics": PRIMARY_METRICS,
        "diagnostic_metrics": DIAGNOSTIC_METRICS,
        "primary_statistics": {
            "c_res_rank1": c_res,
            "delta_med_literal_minus_residualized": delta_med,
            "decision_rule": "POOL-MEDOID-SEPARATION iff C_res >= 3 and Delta_med >= 10",
        },
        "per_metric_primary": primary_rows,
        "per_metric_diagnostic": diagnostic_rows,
        "verdict": verdict,
    }

    OUT_JSON.write_text(json.dumps(out, indent=2), encoding="utf-8")
    print(f"Wrote {OUT_JSON}", file=sys.stderr)
    print(json.dumps(out["primary_statistics"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
