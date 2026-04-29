#!/usr/bin/env python3
"""H-NEW-286.2 — OQ-18 Q17 conditional bridge test.

Primary observable:
  Delta_pair(S) = mean_jaccard(++) - mean_jaccard(other pairs)

Primary null:
  exact enumeration over all C(9,5)=126 five-surah assignments inside
  Q16..Q25 with Q17 excluded from the positive side.

This is a conditioned follow-up to H-NEW-286.1. It asks whether the
locked nucleus becomes the exact optimum once the sole observed leak
surah, Q17, is barred from the positive class.
"""

from __future__ import annotations

import hashlib
import json
import statistics
from itertools import combinations
from pathlib import Path


ROOT = Path("/Users/grey/Downloads/quran")
PREREG = (
    ROOT
    / "findings"
    / "phase-b-hypotheses"
    / "h-new-286-2-q17-conditional-bridge-test-prereg.md"
)
ROOT_GRAPH = ROOT / "data" / "morphology" / "surah-root-graph.json"
H126_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-126.json"
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-286-2.json"

ZONE = tuple(range(16, 26))
TARGET = (16, 21, 22, 23, 25)
Q17 = 17
ALPHA = 0.05


def load_root_sets() -> dict[int, frozenset[str]]:
    payload = json.loads(ROOT_GRAPH.read_text(encoding="utf-8"))
    return {
        int(sid): frozenset(root_counts.keys())
        for sid, root_counts in payload["surahs"].items()
    }


def load_concept_object_ids() -> tuple[int, ...]:
    payload = json.loads(H126_JSON.read_text(encoding="utf-8"))
    concept_object_ids = []
    for row in payload["cell_b_genre_coherence"]["per_surah"]:
        if row["category"] in {"concept-name", "object-name"}:
            concept_object_ids.append(int(row["surah"]))
    return tuple(sorted(sid for sid in concept_object_ids if sid in ZONE))


def jaccard(roots_a: frozenset[str], roots_b: frozenset[str]) -> float:
    union = roots_a | roots_b
    return len(roots_a & roots_b) / len(union) if union else 0.0


def build_pair_rows(root_sets: dict[int, frozenset[str]]) -> list[dict[str, object]]:
    rows = []
    for a, b in combinations(ZONE, 2):
        rows.append(
            {
                "pair": [a, b],
                "jaccard": jaccard(root_sets[a], root_sets[b]),
            }
        )
    return rows


def assignment_summary(
    positive_subset: tuple[int, ...], pair_rows: list[dict[str, object]]
) -> dict[str, object]:
    positive = set(positive_subset)
    pos_pos = []
    pos_neg = []
    neg_neg = []

    for row in pair_rows:
        a, b = row["pair"]
        value = row["jaccard"]
        a_pos = a in positive
        b_pos = b in positive
        if a_pos and b_pos:
            pos_pos.append(value)
        elif a_pos or b_pos:
            pos_neg.append(value)
        else:
            neg_neg.append(value)

    other = pos_neg + neg_neg
    return {
        "positive_subset": list(positive_subset),
        "negative_subset": list(sorted(set(ZONE) - positive)),
        "mean_jaccard_pos_pos": statistics.mean(pos_pos),
        "mean_jaccard_pos_neg": statistics.mean(pos_neg),
        "mean_jaccard_neg_neg": statistics.mean(neg_neg),
        "mean_jaccard_other_pairs": statistics.mean(other),
        "delta_pair": statistics.mean(pos_pos) - statistics.mean(other),
    }


def exact_upper_p(values: list[float], observed: float) -> float:
    return sum(1 for value in values if value >= observed) / len(values)


def descending_rank(values: list[float], observed: float) -> int:
    return 1 + sum(1 for value in values if value > observed)


def best_single_swap_delta(
    outsider: int, pair_rows: list[dict[str, object]]
) -> dict[str, object]:
    rows = []
    for removed in TARGET:
        swapped = tuple(sorted((set(TARGET) - {removed}) | {outsider}))
        summary = assignment_summary(swapped, pair_rows)
        rows.append(
            {
                "outsider": outsider,
                "removed_from_target": removed,
                "swapped_subset": list(swapped),
                "delta_pair": summary["delta_pair"],
            }
        )
    rows.sort(
        key=lambda row: (-row["delta_pair"], row["removed_from_target"], row["swapped_subset"])
    )
    return rows[0]


def mean_jaccard_to_target(
    outsider: int, root_sets: dict[int, frozenset[str]]
) -> float:
    return statistics.mean(jaccard(root_sets[outsider], root_sets[member]) for member in TARGET)


def main() -> int:
    prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    root_sets = load_root_sets()
    concept_object_ids = load_concept_object_ids()
    if concept_object_ids != TARGET:
        raise ValueError(
            f"Observed concept/object ids {concept_object_ids} do not match locked target {TARGET}"
        )

    pair_rows = build_pair_rows(root_sets)
    all_assignments = [
        assignment_summary(positive_subset, pair_rows)
        for positive_subset in combinations(ZONE, 5)
    ]
    q17_excluded_assignments = [
        row for row in all_assignments if Q17 not in row["positive_subset"]
    ]
    q17_included_assignments = [
        row for row in all_assignments if Q17 in row["positive_subset"]
    ]

    target_row = next(
        row for row in all_assignments if tuple(row["positive_subset"]) == TARGET
    )

    excluded_values = [row["delta_pair"] for row in q17_excluded_assignments]
    observed = target_row["delta_pair"]
    n_ge_excluded = sum(1 for value in excluded_values if value >= observed)
    p_exact_excluded = exact_upper_p(excluded_values, observed)
    rank_desc_excluded = descending_rank(excluded_values, observed)
    tie_count_excluded = sum(1 for value in excluded_values if value == observed)

    q17_excluded_sorted = sorted(
        q17_excluded_assignments,
        key=lambda row: (
            -row["delta_pair"],
            -row["mean_jaccard_pos_pos"],
            row["positive_subset"],
        ),
    )
    q17_included_sorted = sorted(
        q17_included_assignments,
        key=lambda row: (
            -row["delta_pair"],
            -row["mean_jaccard_pos_pos"],
            row["positive_subset"],
        ),
    )

    outsider_rows = []
    for outsider in sorted(set(ZONE) - set(TARGET)):
        best_swap = best_single_swap_delta(outsider, pair_rows)
        outsider_rows.append(
            {
                "outsider": outsider,
                "mean_jaccard_to_target": mean_jaccard_to_target(outsider, root_sets),
                "best_single_swap": best_swap,
                "best_single_swap_gain_vs_target": best_swap["delta_pair"] - observed,
            }
        )
    outsider_rows.sort(
        key=lambda row: (
            -row["best_single_swap"]["delta_pair"],
            -row["mean_jaccard_to_target"],
            row["outsider"],
        )
    )

    verdict = "PASS-DIRECTED" if p_exact_excluded < ALPHA else "NULL"
    verdict_note = (
        "This branch was opened by the H-NEW-286.1 observation that all seven better "
        "full-space relabelings include Q17. The conditioned result is exact but still "
        "post-selection-bounded, so the ceiling remains PASS-DIRECTED."
    )

    out = {
        "id": "H-NEW-286.2",
        "title": "OQ-18 Q17 conditional bridge test",
        "date": "2026-04-19",
        "seed": 20260419,
        "prereg_file": str(PREREG.relative_to(ROOT)),
        "prereg_sha256": prereg_sha,
        "script_file": "scripts/h_new_286_2_oq18_q17_conditional_bridge_test.py",
        "label_source": {
            "source_file": "findings/phase-b-hypotheses/csv/h-new-126.json",
            "source_field": "cell_b_genre_coherence.per_surah",
            "concept_object_surahs_in_zone": list(concept_object_ids),
            "binary_label_definition": "1 = concept/object-named; 0 = other",
        },
        "rules_tuple": (
            "(QAC v0.4 root sets via surah-root-graph.json; fixed zone = Q16..Q25; "
            "target nucleus = {Q16,Q21,Q22,Q23,Q25}; primary statistic reused from "
            "H-NEW-286.1: Delta_pair(S)=mean_jaccard(++)-mean_jaccard(other pairs); "
            "primary null = exact enumeration over all C(9,5)=126 five-surah assignments "
            "with Q17 excluded from the positive side; one-sided upper-tail)"
        ),
        "zone": list(ZONE),
        "target_positive_subset": list(TARGET),
        "conditioned_exclusion": Q17,
        "exact_space_n_primary": len(q17_excluded_assignments),
        "exact_space_n_full_reference": len(all_assignments),
        "primary": {
            "statistic": "delta_pairwise_name_class_localization_conditioned_on_q17_excluded",
            "direction": "upper",
            "observed": observed,
            "observed_mean_jaccard_pos_pos": target_row["mean_jaccard_pos_pos"],
            "observed_mean_jaccard_other_pairs": target_row["mean_jaccard_other_pairs"],
            "observed_mean_jaccard_pos_neg": target_row["mean_jaccard_pos_neg"],
            "observed_mean_jaccard_neg_neg": target_row["mean_jaccard_neg_neg"],
            "n_ge_observed": n_ge_excluded,
            "exact_upper_p": p_exact_excluded,
            "rank_desc": rank_desc_excluded,
            "tie_count_at_observed": tie_count_excluded,
            "null_mean_full_space": statistics.mean(excluded_values),
            "null_median_full_space": statistics.median(excluded_values),
            "null_min_full_space": min(excluded_values),
            "null_max_full_space": max(excluded_values),
            "alpha": ALPHA,
            "verdict": verdict,
        },
        "observed_assignment_detail": target_row,
        "q17_excluded_stratum": {
            "n_assignments": len(q17_excluded_assignments),
            "n_strictly_above_observed": sum(
                1 for row in q17_excluded_assignments if row["delta_pair"] > observed
            ),
            "n_at_or_above_observed": n_ge_excluded,
            "mean_delta_pair": statistics.mean(excluded_values),
            "median_delta_pair": statistics.median(excluded_values),
            "min_delta_pair": min(excluded_values),
            "max_delta_pair": max(excluded_values),
            "top_assignments_by_delta_pair": [
                {
                    "positive_subset": row["positive_subset"],
                    "negative_subset": row["negative_subset"],
                    "delta_pair": row["delta_pair"],
                }
                for row in q17_excluded_sorted[:10]
            ],
        },
        "q17_included_stratum_descriptive": {
            "n_assignments": len(q17_included_assignments),
            "n_strictly_above_observed": sum(
                1 for row in q17_included_assignments if row["delta_pair"] > observed
            ),
            "n_at_or_above_observed": sum(
                1 for row in q17_included_assignments if row["delta_pair"] >= observed
            ),
            "mean_delta_pair": statistics.mean(
                row["delta_pair"] for row in q17_included_assignments
            ),
            "median_delta_pair": statistics.median(
                row["delta_pair"] for row in q17_included_assignments
            ),
            "min_delta_pair": min(row["delta_pair"] for row in q17_included_assignments),
            "max_delta_pair": max(row["delta_pair"] for row in q17_included_assignments),
            "top_assignments_by_delta_pair": [
                {
                    "positive_subset": row["positive_subset"],
                    "negative_subset": row["negative_subset"],
                    "delta_pair": row["delta_pair"],
                }
                for row in q17_included_sorted[:10]
            ],
            "note": (
                "Descriptive comparison stratum only. It is not the family driver for "
                "H-NEW-286.2."
            ),
        },
        "outsider_bridge_descriptive": outsider_rows,
        "verdict": verdict,
        "verdict_note": verdict_note,
    }

    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"prereg SHA-256: {prereg_sha}")
    print("H-NEW-286.2 — OQ-18 Q17 conditional bridge test")
    print(
        f"Observed delta_pair = {observed:.6f}; "
        f"Q17-excluded rank = {rank_desc_excluded}/{len(q17_excluded_assignments)}; "
        f"p_exact_upper = {p_exact_excluded:.6f}"
    )
    print(
        f"Q17-excluded null mean = {statistics.mean(excluded_values):.6f}; "
        f"median = {statistics.median(excluded_values):.6f}; "
        f"min = {min(excluded_values):.6f}; max = {max(excluded_values):.6f}"
    )
    print(
        "Best outsider by single-swap delta = "
        f"Q{outsider_rows[0]['outsider']} with delta_pair = "
        f"{outsider_rows[0]['best_single_swap']['delta_pair']:.6f}"
    )
    print(f"Verdict: {verdict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
