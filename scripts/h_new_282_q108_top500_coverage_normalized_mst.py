#!/usr/bin/env python3
"""H-NEW-282 - top-500 coverage-normalized MST follow-up for OQ-19.

Bounded denominator-adjudication run:
  1. replicate the baseline alpha=0.5 MST
  2. replicate H-NEW-278's total-token denominator collapse
  3. test a top-500-mass denominator variant

The goal is not to claim a new canonical normalization family. It is to
ask whether the H-NEW-278 collapse is specifically driven by using total
STEM-root tokens in the denominator rather than the locked top-500 token
mass that the MST itself observes.
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
Q108 = 108
Q7 = 7

QAC_FILE = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
PREREG_FILE = (
    ROOT
    / "findings/phase-b-hypotheses/h-new-282-q108-top500-coverage-normalized-mst-prereg.md"
)
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-282.json"

LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")

EXPECTED_BASELINE_TOP3 = [(108, 24), (7, 10), (112, 8)]
EXPECTED_H278_TOP3 = [(7, 15), (2, 9), (17, 9)]


def fisher_rao(p, q):
    bc = 0.0
    for a, b in zip(p, q):
        if a > 0.0 and b > 0.0:
            bc += math.sqrt(a * b)
    bc = min(1.0, max(-1.0, bc))
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


def neighbors_of(target_sid, mst_edges):
    neighbors = []
    for i, j, weight in mst_edges:
        if i == target_sid:
            neighbors.append((j, weight))
        elif j == target_sid:
            neighbors.append((i, weight))
    return sorted(neighbors, key=lambda item: (item[1], item[0]))


def probability_row_from_values(values):
    smoothed = [value + ALPHA for value in values]
    total_mass = sum(smoothed)
    return [value / total_mass for value in smoothed]


def build_probabilities_baseline(counts):
    probabilities = [[0.0] * K_TOP for _ in range(115)]
    for sid in range(1, 115):
        probabilities[sid] = probability_row_from_values(counts[sid])
    return probabilities


def build_probabilities_total_mass_normalized(counts, total_tokens):
    probabilities = [[0.0] * K_TOP for _ in range(115)]
    for sid in range(1, 115):
        n_i = total_tokens[sid]
        normalized = [value / n_i for value in counts[sid]]
        probabilities[sid] = probability_row_from_values(normalized)
    return probabilities


def build_probabilities_top500_mass_normalized(counts, top500_tokens):
    probabilities = [[0.0] * K_TOP for _ in range(115)]
    for sid in range(1, 115):
        m_i = top500_tokens[sid]
        if m_i <= 0:
            raise RuntimeError(f"Surah {sid} has zero top-{K_TOP} mass; design invalid")
        normalized = [value / m_i for value in counts[sid]]
        probabilities[sid] = probability_row_from_values(normalized)
    return probabilities


def run_variant(probabilities):
    d_matrix = compute_distance_matrix(probabilities)
    mst_edges = mst_kruskal(d_matrix)
    degrees = degree_vector(mst_edges)
    ranked = ranked_degrees(degrees)
    return {
        "mst_edges": mst_edges,
        "degrees": degrees,
        "ranked": ranked,
        "top3": ranked[:3],
        "top10": ranked[:10],
    }


def permutation_control(probabilities, empirical_degrees):
    rng = random.Random(SEED)
    permutation = list(range(1, 115))
    rng.shuffle(permutation)

    prob_permuted = [[0.0] * K_TOP for _ in range(115)]
    for target_sid, source_sid in enumerate(permutation, start=1):
        prob_permuted[target_sid] = probabilities[source_sid]

    permuted_result = run_variant(prob_permuted)
    permuted_degrees = permuted_result["degrees"]
    multiset_same = sorted(empirical_degrees.values()) == sorted(permuted_degrees.values())
    q108_changed = permuted_degrees[Q108] != empirical_degrees[Q108]
    return {
        "permutation": permutation,
        "top10": permuted_result["top10"],
        "q108_degree": permuted_degrees[Q108],
        "source_surah_assigned_to_q108": permutation[Q108 - 1],
        "degree_multiset_same": multiset_same,
        "q108_degree_changed": q108_changed,
        "pass": multiset_same and q108_changed,
    }


def main():
    prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
    print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
    print(f"SEED = {SEED}", file=sys.stderr)
    print(f"K_TOP = {K_TOP}", file=sys.stderr)
    print(f"ALPHA = {ALPHA}", file=sys.stderr)

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

    print(f"Q108 total STEM-root tokens = {total_tokens[Q108]}", file=sys.stderr)
    print(f"Q108 top-{K_TOP} tokens = {top500_tokens[Q108]}", file=sys.stderr)
    print(
        f"Q108 top-{K_TOP} coverage = {top500_tokens[Q108] / total_tokens[Q108]:.4f}",
        file=sys.stderr,
    )
    print(f"Q7 total STEM-root tokens = {total_tokens[Q7]}", file=sys.stderr)
    print(f"Q7 top-{K_TOP} tokens = {top500_tokens[Q7]}", file=sys.stderr)
    print(
        f"Q7 top-{K_TOP} coverage = {top500_tokens[Q7] / total_tokens[Q7]:.4f}",
        file=sys.stderr,
    )

    print("\n[baseline] Replicating H-NEW-131...", file=sys.stderr)
    prob_baseline = build_probabilities_baseline(counts)
    baseline = run_variant(prob_baseline)
    baseline_matches_expected = baseline["top3"] == EXPECTED_BASELINE_TOP3
    print(f"  baseline top-10 hubs: {baseline['top10']}", file=sys.stderr)
    print(
        f"  baseline degrees: Q108={baseline['degrees'][Q108]}, Q7={baseline['degrees'][Q7]}",
        file=sys.stderr,
    )
    print(f"  baseline matches expected top-3: {baseline_matches_expected}", file=sys.stderr)

    print("\n[h278-comparator] Replicating count / N_i collapse...", file=sys.stderr)
    prob_total = build_probabilities_total_mass_normalized(counts, total_tokens)
    h278 = run_variant(prob_total)
    h278_matches_expected = h278["top3"] == EXPECTED_H278_TOP3
    print(f"  h278 top-10 hubs: {h278['top10']}", file=sys.stderr)
    print(
        f"  h278 degrees: Q108={h278['degrees'][Q108]}, Q7={h278['degrees'][Q7]}",
        file=sys.stderr,
    )
    print(f"  h278 matches expected top-3: {h278_matches_expected}", file=sys.stderr)

    print("\n[h282-candidate] Running count / M_i within top-500 space...", file=sys.stderr)
    prob_cov = build_probabilities_top500_mass_normalized(counts, top500_tokens)
    h282 = run_variant(prob_cov)
    print(f"  h282 top-10 hubs: {h282['top10']}", file=sys.stderr)
    print(
        f"  h282 degrees: Q108={h282['degrees'][Q108]}, Q7={h282['degrees'][Q7]}",
        file=sys.stderr,
    )
    print(f"  Q108 neighbors: {neighbors_of(Q108, h282['mst_edges'])}", file=sys.stderr)

    baseline_top3_ids = {sid for sid, _ in baseline["top3"]}
    h278_top3_ids = {sid for sid, _ in h278["top3"]}
    h282_top3_ids = {sid for sid, _ in h282["top3"]}

    q108_top3 = Q108 in h282_top3_ids
    q108_gt_q7 = h282["degrees"][Q108] > h282["degrees"][Q7]
    q108_degree_improved_vs_h278 = h282["degrees"][Q108] > h278["degrees"][Q108]
    q108_rank_h278 = competition_rank(h278["degrees"], Q108)
    q108_rank_h282 = competition_rank(h282["degrees"], Q108)
    q108_rank_improved_vs_h278 = q108_rank_h282 < q108_rank_h278

    print(
        f"  q108_top3={q108_top3} ; q108_gt_q7={q108_gt_q7} ; "
        f"q108_degree_improved_vs_h278={q108_degree_improved_vs_h278} ; "
        f"q108_rank {q108_rank_h278}->{q108_rank_h282}",
        file=sys.stderr,
    )

    print("\n[MW-5] Deterministic label-permutation control on h282...", file=sys.stderr)
    mw5 = permutation_control(prob_cov, h282["degrees"])
    print(f"  permuted top-10 hubs: {mw5['top10']}", file=sys.stderr)
    print(
        f"  permuted Q108 degree = {mw5['q108_degree']} "
        f"(empirical {h282['degrees'][Q108]})",
        file=sys.stderr,
    )
    print(
        f"  source surah assigned to label Q108 = {mw5['source_surah_assigned_to_q108']}",
        file=sys.stderr,
    )
    print(
        f"  degree multiset same = {mw5['degree_multiset_same']} ; "
        f"Q108 degree changed = {mw5['q108_degree_changed']} ; "
        f"{'PASS' if mw5['pass'] else 'FAIL'}",
        file=sys.stderr,
    )

    if not baseline_matches_expected or not h278_matches_expected or not mw5["pass"]:
        final_verdict = "INSTRUMENT-BROKEN - comparator replication or MW-5 failed"
    elif q108_top3 and q108_gt_q7:
        final_verdict = (
            "STRONG-DENOMINATOR-RESCUE - replacing total-token denominator with "
            "top-500-mass normalization restores Q108's hub standing"
        )
    elif q108_degree_improved_vs_h278 and q108_rank_improved_vs_h278:
        final_verdict = (
            "PARTIAL-DENOMINATOR-RESCUE - denominator choice matters, but the "
            "top-500-mass variant does not fully restore the original anomaly"
        )
    else:
        final_verdict = (
            "NO-DENOMINATOR-RESCUE - denominator choice alone does not explain the "
            "H-NEW-278 collapse"
        )

    print("\n" + "=" * 72, file=sys.stderr)
    print(f"FINAL VERDICT: {final_verdict}", file=sys.stderr)
    print("=" * 72, file=sys.stderr)

    summary = {
        "finding_id": "h-new-282",
        "title": "Top-500 coverage-normalized MST follow-up for OQ-19",
        "pre_reg_sha256": prereg_sha,
        "seed": SEED,
        "date": "2026-04-18",
        "parents": ["h-new-131", "h-new-131.1", "h-new-278", "h-new-279"],
        "rules_tuple": (
            "(114 surahs Hafs-Kufan; K=500 top QAC-STEM roots; Fisher-Rao "
            "arccos-Bhattacharyya; Dirichlet alpha=0.5; MST via Kruskal; "
            "no-tashkeel; QAC v0.4)"
        ),
        "design_role": (
            "bounded denominator-adjudication probe; not claimed as a canonical "
            "length-normalization family"
        ),
        "locked_params": {
            "k_top_roots": K_TOP,
            "alpha": ALPHA,
            "baseline": "raw top-500 counts + flat alpha=0.5",
            "h278_comparator": "count[i,r] / total_stem_root_tokens_in_surah_i",
            "h282_candidate": "count[i,r] / top500_token_mass_in_surah_i",
            "tie_break_ranking": "degree desc, surah_id asc",
        },
        "token_mass_summary": {
            "q108_total_stem_tokens": total_tokens[Q108],
            "q108_top500_tokens": top500_tokens[Q108],
            "q108_top500_coverage": top500_tokens[Q108] / total_tokens[Q108],
            "q7_total_stem_tokens": total_tokens[Q7],
            "q7_top500_tokens": top500_tokens[Q7],
            "q7_top500_coverage": top500_tokens[Q7] / total_tokens[Q7],
        },
        "baseline_replication": {
            "top10_hubs": baseline["top10"],
            "top3": baseline["top3"],
            "q108_degree": baseline["degrees"][Q108],
            "q7_degree": baseline["degrees"][Q7],
            "matches_expected_top3": baseline_matches_expected,
        },
        "h278_comparator_replication": {
            "top10_hubs": h278["top10"],
            "top3": h278["top3"],
            "q108_degree": h278["degrees"][Q108],
            "q7_degree": h278["degrees"][Q7],
            "q108_rank_competition": q108_rank_h278,
            "matches_expected_top3": h278_matches_expected,
        },
        "h282_candidate": {
            "top10_hubs": h282["top10"],
            "top3": h282["top3"],
            "baseline_top3_overlap_ids": sorted(baseline_top3_ids & h282_top3_ids),
            "h278_top3_overlap_ids": sorted(h278_top3_ids & h282_top3_ids),
            "q108_degree": h282["degrees"][Q108],
            "q7_degree": h282["degrees"][Q7],
            "q108_minus_q7_degree": h282["degrees"][Q108] - h282["degrees"][Q7],
            "q108_is_top3": q108_top3,
            "q108_rank_competition": q108_rank_h282,
            "q108_neighbors": neighbors_of(Q108, h282["mst_edges"]),
        },
        "denominator_adjudication": {
            "q108_top3": q108_top3,
            "q108_gt_q7": q108_gt_q7,
            "q108_degree_improved_vs_h278": q108_degree_improved_vs_h278,
            "q108_rank_h278": q108_rank_h278,
            "q108_rank_h282": q108_rank_h282,
            "q108_rank_improved_vs_h278": q108_rank_improved_vs_h278,
        },
        "mw5_label_permutation": {
            "seed": SEED,
            "permutation": mw5["permutation"],
            "permuted_top10_hubs": mw5["top10"],
            "permuted_q108_degree": mw5["q108_degree"],
            "source_surah_assigned_to_q108": mw5["source_surah_assigned_to_q108"],
            "degree_multiset_same": mw5["degree_multiset_same"],
            "q108_degree_changed": mw5["q108_degree_changed"],
            "pass": mw5["pass"],
        },
        "final_verdict": final_verdict,
    }

    OUT_JSON.write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")
    print(f"Wrote: {OUT_JSON}", file=sys.stderr)


if __name__ == "__main__":
    main()
