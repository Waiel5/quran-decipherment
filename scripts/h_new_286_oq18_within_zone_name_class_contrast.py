#!/usr/bin/env python3
"""H-NEW-286 — OQ-18 within-zone name-class contrast test.

Primary observable:
  Delta_name(S) = mean_{q in S} I[label(q)=concept/object]
                  - mean_{q in Z\\S} I[label(q)=concept/object]

Primary null:
  exact enumeration over all C(10,5)=252 five-surah subsets of Q16..Q25

The concept/object label set is reused from the on-disk H-NEW-126 Cell B
map. This is a bounded exact-null follow-up to H-NEW-281 and H-NEW-285.
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
    / "h-new-286-oq18-within-zone-name-class-contrast-prereg.md"
)
H126_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-126.json"
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-286.json"

ZONE = tuple(range(16, 26))
TARGET = (16, 21, 22, 23, 25)
ALPHA = 0.05


def load_concept_object_ids() -> tuple[int, ...]:
    payload = json.loads(H126_JSON.read_text(encoding="utf-8"))
    concept_object_ids = []
    for row in payload["cell_b_genre_coherence"]["per_surah"]:
        if row["category"] in {"concept-name", "object-name"}:
            concept_object_ids.append(int(row["surah"]))
    concept_object_ids = tuple(sorted(concept_object_ids))
    return concept_object_ids


def label_map(concept_object_ids: tuple[int, ...]) -> dict[int, int]:
    concept_object = set(concept_object_ids)
    return {sid: 1 if sid in concept_object else 0 for sid in ZONE}


def mean_label(subset: tuple[int, ...], labels: dict[int, int]) -> float:
    return statistics.mean(labels[sid] for sid in subset)


def exact_upper_p(values: list[float], observed: float) -> float:
    return sum(1 for value in values if value >= observed) / len(values)


def descending_rank(values: list[float], observed: float) -> int:
    return 1 + sum(1 for value in values if value > observed)


def main() -> int:
    prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    concept_object_ids = load_concept_object_ids()
    labels = label_map(concept_object_ids)

    all_subsets = list(combinations(ZONE, 5))
    rows = []
    for subset in all_subsets:
        complement = tuple(sorted(set(ZONE) - set(subset)))
        subset_mean = mean_label(subset, labels)
        complement_mean = mean_label(complement, labels)
        delta = subset_mean - complement_mean
        rows.append(
            {
                "subset": list(subset),
                "complement_subset": list(complement),
                "mean_concept_object_subset": subset_mean,
                "mean_concept_object_complement": complement_mean,
                "delta_name": delta,
            }
        )

    target_row = next(row for row in rows if tuple(row["subset"]) == TARGET)
    complement_row = next(row for row in rows if tuple(row["subset"]) == tuple(sorted(set(ZONE) - set(TARGET))))
    delta_values = [row["delta_name"] for row in rows]

    rows_by_delta = sorted(
        rows,
        key=lambda row: (
            -row["delta_name"],
            -row["mean_concept_object_subset"],
            row["subset"],
        ),
    )

    observed = target_row["delta_name"]
    n_ge = sum(1 for value in delta_values if value >= observed)
    p_exact = exact_upper_p(delta_values, observed)
    rank_desc = descending_rank(delta_values, observed)
    tie_count = sum(1 for value in delta_values if value == observed)

    verdict = "PASS-DIRECTED" if p_exact < ALPHA else "NULL"
    verdict_note = (
        "The target split is the full concept/object set within the zone, "
        "so the exact-null maximum is categorical rather than graded. "
        "The bounded test is still valid and remains PASS-DIRECTED only."
    )

    out = {
        "id": "H-NEW-286",
        "title": "OQ-18 within-zone name-class contrast",
        "date": "2026-04-18",
        "seed": 20260418,
        "prereg_file": str(PREREG.relative_to(ROOT)),
        "prereg_sha256": prereg_sha,
        "script_file": "scripts/h_new_286_oq18_within_zone_name_class_contrast.py",
        "label_source": {
            "source_file": "findings/phase-b-hypotheses/csv/h-new-126.json",
            "source_field": "cell_b_genre_coherence.per_surah",
            "concept_object_surahs": list(concept_object_ids),
            "binary_label_definition": "1 = concept/object-named; 0 = other",
        },
        "rules_tuple": (
            "(QAC v0.4 surah-name map reused from h-new-126 Cell B; binary label "
            "concept/object-named vs other; exact enumeration over all C(10,5)=252 "
            "five-surah subsets of Q16..Q25; primary statistic = "
            "Delta_name(S)=mean_{q in S} I[label(q)=concept/object]-mean_{q in Z\\S} I[label(q)=concept/object]; "
            "one-sided upper-tail)"
        ),
        "zone": list(ZONE),
        "target_subset": list(TARGET),
        "exact_space_n": len(rows),
        "zone_label_map": {str(sid): labels[sid] for sid in ZONE},
        "target_count_concept_object": sum(labels[sid] for sid in TARGET),
        "zone_count_concept_object": sum(labels.values()),
        "primary": {
            "statistic": "delta_name_concept_object",
            "direction": "upper",
            "observed": observed,
            "target_mean_concept_object": target_row["mean_concept_object_subset"],
            "complement_mean_concept_object": target_row["mean_concept_object_complement"],
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
        "target_detail": target_row,
        "complement_detail": {
            **complement_row,
            "rank_desc": descending_rank(delta_values, complement_row["delta_name"]),
            "exact_upper_p": exact_upper_p(delta_values, complement_row["delta_name"]),
        },
        "top_subsets_by_delta": rows_by_delta[:10],
        "verdict": verdict,
        "verdict_note": verdict_note,
    }

    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"prereg SHA-256: {prereg_sha}")
    print("H-NEW-286 — OQ-18 within-zone name-class contrast")
    print(f"Concept/object surahs in zone: {list(concept_object_ids)}")
    print(
        f"Primary observed delta = {observed:.6f}; "
        f"target mean = {target_row['mean_concept_object_subset']:.6f}; "
        f"complement mean = {target_row['mean_concept_object_complement']:.6f}; "
        f"rank = {rank_desc}/{len(rows)}; p_exact_upper = {p_exact:.6f}"
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
