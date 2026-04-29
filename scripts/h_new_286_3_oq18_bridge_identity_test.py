#!/usr/bin/env python3
"""H-NEW-286.3 — OQ-18 Q17 bridge identity test.

Primary statistic:
  Delta_bridge(b) = mean_jaccard(predicted_high_edges_b)
                    - mean_jaccard(all_other_zone_pairs_b)

where predicted_high_edges_b = core-core pairs union bridge-to-core pairs
for a fixed core {Q16,Q21,Q22,Q23,Q25} and a candidate outsider bridge
b in {Q17,Q18,Q19,Q20,Q24}.

Primary exact space:
  the 5 admissible outsider bridges only.

This means the smallest attainable one-sided exact upper fraction is
1/5 = 0.20, so the test can establish only a descriptive rank result.
It cannot yield an inferential pass at alpha = 0.05.
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
    / "h-new-286-3-q17-bridge-identity-test-prereg.md"
)
ROOT_GRAPH = ROOT / "data" / "morphology" / "surah-root-graph.json"
H126_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-126.json"
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-286-3.json"

ZONE = tuple(range(16, 26))
CORE = (16, 21, 22, 23, 25)
OUTSIDERS = (17, 18, 19, 20, 24)
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


def build_pair_values(root_sets: dict[int, frozenset[str]]) -> dict[tuple[int, int], float]:
    return {
        (a, b): jaccard(root_sets[a], root_sets[b])
        for a, b in combinations(ZONE, 2)
    }


def bridge_candidate_summary(
    bridge: int, pair_values: dict[tuple[int, int], float]
) -> dict[str, object]:
    core_core_pairs = [tuple(sorted(pair)) for pair in combinations(CORE, 2)]
    bridge_core_pairs = [tuple(sorted((bridge, core_sid))) for core_sid in CORE]
    predicted_high_pairs = set(core_core_pairs + bridge_core_pairs)
    other_pairs = [
        pair for pair in sorted(pair_values) if pair not in predicted_high_pairs
    ]

    core_core_values = [pair_values[pair] for pair in core_core_pairs]
    bridge_core_values = [pair_values[pair] for pair in bridge_core_pairs]
    high_values = [pair_values[pair] for pair in sorted(predicted_high_pairs)]
    other_values = [pair_values[pair] for pair in other_pairs]

    delta_bridge = statistics.mean(high_values) - statistics.mean(other_values)

    return {
        "bridge": bridge,
        "core": list(CORE),
        "outsider_family": list(OUTSIDERS),
        "n_predicted_high_pairs": len(high_values),
        "n_other_pairs": len(other_values),
        "mean_jaccard_core_core": statistics.mean(core_core_values),
        "mean_jaccard_bridge_core": statistics.mean(bridge_core_values),
        "mean_jaccard_predicted_high": statistics.mean(high_values),
        "mean_jaccard_other_pairs": statistics.mean(other_values),
        "delta_bridge": delta_bridge,
        "predicted_high_core_core_pairs": [
            {"pair": list(pair), "jaccard": pair_values[pair]} for pair in core_core_pairs
        ],
        "predicted_high_bridge_core_pairs": [
            {"pair": list(pair), "jaccard": pair_values[pair]} for pair in bridge_core_pairs
        ],
    }


def exact_upper_fraction(values: list[float], observed: float) -> float:
    return sum(1 for value in values if value >= observed) / len(values)


def descending_rank(values: list[float], observed: float) -> int:
    return 1 + sum(1 for value in values if value > observed)


def assignment_summary(
    positive_subset: tuple[int, ...], pair_values: dict[tuple[int, int], float]
) -> dict[str, float]:
    positive = set(positive_subset)
    pos_pos = []
    pos_neg = []
    neg_neg = []

    for pair, value in pair_values.items():
        a, b = pair
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
        "mean_jaccard_pos_pos": statistics.mean(pos_pos),
        "mean_jaccard_pos_neg": statistics.mean(pos_neg),
        "mean_jaccard_neg_neg": statistics.mean(neg_neg),
        "mean_jaccard_other_pairs": statistics.mean(other),
        "delta_pair": statistics.mean(pos_pos) - statistics.mean(other),
    }


def best_single_swap_delta(
    outsider: int, pair_values: dict[tuple[int, int], float]
) -> dict[str, object]:
    rows = []
    for removed in CORE:
        swapped = tuple(sorted((set(CORE) - {removed}) | {outsider}))
        summary = assignment_summary(swapped, pair_values)
        rows.append(
            {
                "outsider": outsider,
                "removed_from_core": removed,
                "swapped_subset": list(swapped),
                "delta_pair": summary["delta_pair"],
            }
        )
    rows.sort(
        key=lambda row: (
            -row["delta_pair"],
            row["removed_from_core"],
            row["swapped_subset"],
        )
    )
    return rows[0]


def main() -> int:
    prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    root_sets = load_root_sets()
    concept_object_ids = load_concept_object_ids()
    if concept_object_ids != CORE:
        raise ValueError(
            f"Observed concept/object ids {concept_object_ids} do not match locked core {CORE}"
        )

    pair_values = build_pair_values(root_sets)
    candidate_rows = [
        bridge_candidate_summary(bridge, pair_values) for bridge in OUTSIDERS
    ]
    candidate_rows.sort(
        key=lambda row: (
            -row["delta_bridge"],
            -row["mean_jaccard_bridge_core"],
            row["bridge"],
        )
    )

    q17_row = next(row for row in candidate_rows if row["bridge"] == Q17)
    primary_values = [row["delta_bridge"] for row in candidate_rows]
    observed = q17_row["delta_bridge"]
    n_ge = sum(1 for value in primary_values if value >= observed)
    exact_upper = exact_upper_fraction(primary_values, observed)
    rank_desc = descending_rank(primary_values, observed)
    tie_count = sum(1 for value in primary_values if value == observed)
    min_attainable = 1 / len(candidate_rows)
    inferential_pass_possible = min_attainable < ALPHA
    inferential_verdict = "PASS-DIRECTED" if exact_upper < ALPHA else "NULL"

    core_pair_reference = assignment_summary(CORE, pair_values)["delta_pair"]

    descriptive_rows = []
    for row in candidate_rows:
        best_swap = best_single_swap_delta(row["bridge"], pair_values)
        descriptive_rows.append(
            {
                "bridge": row["bridge"],
                "mean_jaccard_bridge_core": row["mean_jaccard_bridge_core"],
                "best_single_swap": best_swap,
                "best_single_swap_gain_vs_h2862_core": best_swap["delta_pair"]
                - core_pair_reference,
            }
        )

    out = {
        "id": "H-NEW-286.3",
        "title": "OQ-18 Q17 bridge identity test",
        "date": "2026-04-19",
        "seed": 20260419,
        "prereg_file": str(PREREG.relative_to(ROOT)),
        "prereg_sha256": prereg_sha,
        "script_file": "scripts/h_new_286_3_oq18_bridge_identity_test.py",
        "label_source": {
            "source_file": "findings/phase-b-hypotheses/csv/h-new-126.json",
            "source_field": "cell_b_genre_coherence.per_surah",
            "concept_object_surahs_in_zone": list(concept_object_ids),
            "binary_label_definition": "1 = concept/object-named; 0 = other",
        },
        "rules_tuple": (
            "(QAC v0.4 root sets via surah-root-graph.json; fixed zone = Q16..Q25; "
            "fixed core = {Q16,Q21,Q22,Q23,Q25}; outsider family = {Q17,Q18,Q19,Q20,Q24}; "
            "candidate bridge score Delta_bridge(b)=mean_jaccard(core-core ∪ bridge-core) "
            "- mean_jaccard(all other zone pairs); exact outsider-family rank/upper "
            "fraction over the 5 admissible bridges; one-sided upper-tail reported "
            "descriptively because the minimum attainable exact upper fraction is 1/5 = 0.20)"
        ),
        "zone": list(ZONE),
        "core_subset": list(CORE),
        "outsider_family": list(OUTSIDERS),
        "exact_space_n_primary": len(candidate_rows),
        "primary": {
            "statistic": "delta_bridge_fixed_core_plus_bridge_mask",
            "direction": "upper",
            "observed_bridge": Q17,
            "observed": observed,
            "observed_mean_jaccard_predicted_high": q17_row["mean_jaccard_predicted_high"],
            "observed_mean_jaccard_other_pairs": q17_row["mean_jaccard_other_pairs"],
            "observed_mean_jaccard_bridge_core": q17_row["mean_jaccard_bridge_core"],
            "observed_mean_jaccard_core_core": q17_row["mean_jaccard_core_core"],
            "n_ge_observed": n_ge,
            "exact_upper_fraction": exact_upper,
            "rank_desc": rank_desc,
            "tie_count_at_observed": tie_count,
            "family_mean": statistics.mean(primary_values),
            "family_median": statistics.median(primary_values),
            "family_min": min(primary_values),
            "family_max": max(primary_values),
            "alpha": ALPHA,
            "minimum_attainable_exact_upper_fraction": min_attainable,
            "inferential_pass_possible_under_alpha": inferential_pass_possible,
            "inferential_verdict": inferential_verdict,
        },
        "pairwise_core_reference": {
            "statistic": "delta_pair_from_h_new_286_2",
            "core_subset": list(CORE),
            "observed": core_pair_reference,
        },
        "observed_bridge_detail": q17_row,
        "candidate_rank_table": candidate_rows,
        "descriptive_robustness": descriptive_rows,
        "verdict": "DESCRIPTIVE-ONLY",
        "verdict_note": (
            "Q17 is the unique rank-1 outsider bridge under the fixed core-plus-bridge "
            "mask, but the outsider family contains only five admissible candidates. "
            "So the best possible one-sided exact upper fraction is 0.20, which cannot "
            "support an inferential pass at alpha = 0.05. The honest inferential verdict "
            "is NULL; the positive statement is descriptive unique-best only."
        ),
    }

    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"prereg SHA-256: {prereg_sha}")
    print("H-NEW-286.3 — OQ-18 Q17 bridge identity test")
    print(
        f"Observed bridge = Q{Q17}; delta_bridge = {observed:.6f}; "
        f"rank = {rank_desc}/{len(candidate_rows)}; "
        f"exact_upper_fraction = {exact_upper:.6f}"
    )
    print(
        f"Minimum attainable exact upper fraction = {min_attainable:.6f}; "
        f"inferential verdict = {inferential_verdict}; "
        f"top two bridges = Q{candidate_rows[0]['bridge']} > Q{candidate_rows[1]['bridge']}"
    )
    print("Full outsider ranking by delta_bridge:")
    for row in candidate_rows:
        print(
            f"  Q{row['bridge']}: delta_bridge = {row['delta_bridge']:.6f}; "
            f"mean_bridge_core = {row['mean_jaccard_bridge_core']:.6f}"
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
