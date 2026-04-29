#!/usr/bin/env python3
"""H-NEW-286.1 — OQ-18 pairwise name-class localization.

Primary observable:
  Delta_pair(L) = mean_jaccard(++) - mean_jaccard(other pairs)

Primary null:
  exact enumeration over all C(10,5)=252 positive-label assignments
  preserving the 5/5 split inside Q16..Q25

The positive label is reused exactly from H-NEW-126 / H-NEW-286:
concept/object-named vs other.
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
    / "h-new-286-1-oq18-pairwise-name-class-localization-prereg.md"
)
ROOT_GRAPH = ROOT / "data" / "morphology" / "surah-root-graph.json"
H126_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-126.json"
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-286-1.json"

ZONE = tuple(range(16, 26))
TARGET_POSITIVE = (16, 21, 22, 23, 25)
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
    pair_table = []

    for row in pair_rows:
        a, b = row["pair"]
        value = row["jaccard"]
        a_pos = a in positive
        b_pos = b in positive
        if a_pos and b_pos:
            label = "++"
            pos_pos.append(value)
        elif a_pos or b_pos:
            label = "+-"
            pos_neg.append(value)
        else:
            label = "--"
            neg_neg.append(value)
        pair_table.append(
            {
                "pair": [a, b],
                "jaccard": value,
                "pair_class": label,
            }
        )

    other = pos_neg + neg_neg
    delta = statistics.mean(pos_pos) - statistics.mean(other)
    pair_table.sort(key=lambda row: (-row["jaccard"], row["pair"]))

    return {
        "positive_subset": list(positive_subset),
        "negative_subset": list(sorted(set(ZONE) - positive)),
        "n_pairs_total": len(pair_table),
        "n_pos_pos_pairs": len(pos_pos),
        "n_pos_neg_pairs": len(pos_neg),
        "n_neg_neg_pairs": len(neg_neg),
        "mean_jaccard_pos_pos": statistics.mean(pos_pos),
        "mean_jaccard_pos_neg": statistics.mean(pos_neg),
        "mean_jaccard_neg_neg": statistics.mean(neg_neg),
        "mean_jaccard_other_pairs": statistics.mean(other),
        "delta_pair": delta,
        "pair_table_sorted_desc": pair_table,
    }


def exact_upper_p(values: list[float], observed: float) -> float:
    return sum(1 for value in values if value >= observed) / len(values)


def descending_rank(values: list[float], observed: float) -> int:
    return 1 + sum(1 for value in values if value > observed)


def main() -> int:
    prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    root_sets = load_root_sets()
    concept_object_ids = load_concept_object_ids()
    if concept_object_ids != TARGET_POSITIVE:
        raise ValueError(
            f"Observed concept/object ids {concept_object_ids} do not match "
            f"locked target {TARGET_POSITIVE}"
        )

    pair_rows = build_pair_rows(root_sets)
    assignments = []
    for positive_subset in combinations(ZONE, 5):
        summary = assignment_summary(positive_subset, pair_rows)
        assignments.append(summary)

    target_row = next(
        row for row in assignments if tuple(row["positive_subset"]) == TARGET_POSITIVE
    )
    delta_values = [row["delta_pair"] for row in assignments]
    rows_by_delta = sorted(
        assignments,
        key=lambda row: (
            -row["delta_pair"],
            -row["mean_jaccard_pos_pos"],
            row["positive_subset"],
        ),
    )

    observed = target_row["delta_pair"]
    n_ge = sum(1 for value in delta_values if value >= observed)
    p_exact = exact_upper_p(delta_values, observed)
    rank_desc = descending_rank(delta_values, observed)
    tie_count = sum(1 for value in delta_values if value == observed)

    verdict = "PASS-DIRECTED" if p_exact < ALPHA else "NULL"
    verdict_note = (
        "This is a bounded exact relabeling test inside Q16..Q25. "
        "Because the positive class was inherited from prior work, a passing "
        "result is capped at PASS-DIRECTED."
    )

    out = {
        "id": "H-NEW-286.1",
        "title": "OQ-18 pairwise name-class localization",
        "date": "2026-04-19",
        "seed": 20260419,
        "prereg_file": str(PREREG.relative_to(ROOT)),
        "prereg_sha256": prereg_sha,
        "script_file": "scripts/h_new_286_1_oq18_pairwise_name_class_localization.py",
        "label_source": {
            "source_file": "findings/phase-b-hypotheses/csv/h-new-126.json",
            "source_field": "cell_b_genre_coherence.per_surah",
            "concept_object_surahs_in_zone": list(concept_object_ids),
            "binary_label_definition": "1 = concept/object-named; 0 = other",
        },
        "rules_tuple": (
            "(QAC v0.4 root sets via surah-root-graph.json; binary concept/object-vs-other "
            "label reused from h-new-126 Cell B and H-NEW-286; exact enumeration over "
            "all C(10,5)=252 five-positive assignments inside Q16..Q25; primary statistic = "
            "Delta_pair(L)=mean_jaccard(++)-mean_jaccard(other pairs); one-sided upper-tail)"
        ),
        "zone": list(ZONE),
        "target_positive_subset": list(TARGET_POSITIVE),
        "exact_space_n": len(assignments),
        "zone_root_set_sizes": {str(sid): len(root_sets[sid]) for sid in ZONE},
        "primary": {
            "statistic": "delta_pairwise_name_class_localization",
            "direction": "upper",
            "observed": observed,
            "observed_mean_jaccard_pos_pos": target_row["mean_jaccard_pos_pos"],
            "observed_mean_jaccard_other_pairs": target_row["mean_jaccard_other_pairs"],
            "observed_mean_jaccard_pos_neg": target_row["mean_jaccard_pos_neg"],
            "observed_mean_jaccard_neg_neg": target_row["mean_jaccard_neg_neg"],
            "n_ge_observed": n_ge,
            "exact_upper_p": p_exact,
            "rank_desc": rank_desc,
            "tie_count_at_observed": tie_count,
            "null_mean_full_space": statistics.mean(delta_values),
            "null_median_full_space": statistics.median(delta_values),
            "null_min_full_space": min(delta_values),
            "null_max_full_space": max(delta_values),
            "alpha": ALPHA,
            "verdict": verdict,
        },
        "observed_assignment_detail": target_row,
        "top_assignments_by_delta_pair": [
            {
                "positive_subset": row["positive_subset"],
                "negative_subset": row["negative_subset"],
                "mean_jaccard_pos_pos": row["mean_jaccard_pos_pos"],
                "mean_jaccard_other_pairs": row["mean_jaccard_other_pairs"],
                "delta_pair": row["delta_pair"],
            }
            for row in rows_by_delta[:10]
        ],
        "verdict": verdict,
        "verdict_note": verdict_note,
    }

    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"prereg SHA-256: {prereg_sha}")
    print("H-NEW-286.1 — OQ-18 pairwise name-class localization")
    print(
        f"Observed delta_pair = {observed:.6f}; "
        f"mean(++) = {target_row['mean_jaccard_pos_pos']:.6f}; "
        f"mean(other) = {target_row['mean_jaccard_other_pairs']:.6f}; "
        f"rank = {rank_desc}/{len(assignments)}; p_exact_upper = {p_exact:.6f}"
    )
    print(
        f"Descriptive split: mean(+-) = {target_row['mean_jaccard_pos_neg']:.6f}; "
        f"mean(--) = {target_row['mean_jaccard_neg_neg']:.6f}"
    )
    print(
        f"Null mean = {statistics.mean(delta_values):.6f}; "
        f"median = {statistics.median(delta_values):.6f}; "
        f"min = {min(delta_values):.6f}; max = {max(delta_values):.6f}"
    )
    print(f"Verdict: {verdict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
