#!/usr/bin/env python3
"""H-NEW-285 - OQ-18 within-zone 5-vs-5 contrast test.

Primary observable:
  Delta(S) = mean_pairwise_root_jaccard(S) - mean_pairwise_root_jaccard(Z\\S)

Primary null:
  exact enumeration over all C(10,5)=252 five-surah subsets of Q16..Q25

This is a bounded follow-up to H-NEW-281 that stays entirely inside the
same fixed zone and compares the target split against its exact
complement under the same root-set Jaccard instrument.
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
    / "h-new-285-oq18-within-zone-contrast-prereg.md"
)
ROOT_GRAPH = ROOT / "data" / "morphology" / "surah-root-graph.json"
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-285.json"

ZONE = tuple(range(16, 26))
TARGET = (16, 21, 22, 23, 25)
COMPLEMENT = tuple(sorted(set(ZONE) - set(TARGET)))
ALPHA = 0.05


def load_root_sets() -> dict[int, frozenset[str]]:
    payload = json.loads(ROOT_GRAPH.read_text(encoding="utf-8"))
    return {
        int(sid): frozenset(root_counts.keys())
        for sid, root_counts in payload["surahs"].items()
    }


def pairwise_mean_root_jaccard(
    subset: tuple[int, ...], root_sets: dict[int, frozenset[str]]
) -> float:
    values = []
    for a, b in combinations(subset, 2):
        roots_a = root_sets[a]
        roots_b = root_sets[b]
        union = roots_a | roots_b
        values.append(len(roots_a & roots_b) / len(union) if union else 0.0)
    return statistics.mean(values) if values else 0.0


def exact_upper_p(values: list[float], observed: float) -> float:
    return sum(1 for value in values if value >= observed) / len(values)


def descending_rank(values: list[float], observed: float) -> int:
    return 1 + sum(1 for value in values if value > observed)


def main() -> int:
    prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    root_sets = load_root_sets()

    all_subsets = list(combinations(ZONE, 5))
    rows = []
    for subset in all_subsets:
        complement = tuple(sorted(set(ZONE) - set(subset)))
        target_mean = pairwise_mean_root_jaccard(subset, root_sets)
        complement_mean = pairwise_mean_root_jaccard(complement, root_sets)
        delta = target_mean - complement_mean
        rows.append(
            {
                "subset": list(subset),
                "complement_subset": list(complement),
                "mean_pairwise_root_jaccard_subset": target_mean,
                "mean_pairwise_root_jaccard_complement": complement_mean,
                "delta": delta,
            }
        )

    target_row = next(row for row in rows if tuple(row["subset"]) == TARGET)
    complement_row = next(row for row in rows if tuple(row["subset"]) == COMPLEMENT)
    delta_values = [row["delta"] for row in rows]

    rows_by_delta = sorted(
        rows,
        key=lambda row: (-row["delta"], -row["mean_pairwise_root_jaccard_subset"], row["subset"]),
    )

    observed = target_row["delta"]
    n_ge = sum(1 for value in delta_values if value >= observed)
    p_exact = exact_upper_p(delta_values, observed)
    rank_desc = descending_rank(delta_values, observed)
    tie_count = sum(1 for value in delta_values if value == observed)

    verdict = "PASS-DIRECTED" if p_exact < ALPHA else "NULL"
    verdict_note = (
        "Target split was surfaced by prior work, so a passing result is capped at "
        "PASS-DIRECTED under this new bounded exact null."
    )

    out = {
        "id": "H-NEW-285",
        "title": "OQ-18 within-zone 5-vs-5 contrast test",
        "date": "2026-04-18",
        "seed": 20260418,
        "prereg_file": str(PREREG.relative_to(ROOT)),
        "prereg_sha256": prereg_sha,
        "script_file": "scripts/h_new_285_oq18_within_zone_contrast.py",
        "rules_tuple": (
            "(QAC v0.4 root sets via surah-root-graph.json; exact enumeration over "
            "all C(10,5)=252 five-surah subsets of Q16..Q25; primary statistic = "
            "Delta(S)=mean_pairwise_root_jaccard(S)-mean_pairwise_root_jaccard(Z\\S); "
            "one-sided upper-tail)"
        ),
        "zone": list(ZONE),
        "target_subset": list(TARGET),
        "complement_subset": list(COMPLEMENT),
        "exact_space_n": len(rows),
        "zone_root_set_sizes": {str(sid): len(root_sets[sid]) for sid in ZONE},
        "primary": {
            "statistic": "delta_mean_pairwise_root_jaccard",
            "direction": "upper",
            "observed": observed,
            "target_mean_pairwise_root_jaccard": target_row["mean_pairwise_root_jaccard_subset"],
            "complement_mean_pairwise_root_jaccard": target_row["mean_pairwise_root_jaccard_complement"],
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
            "rank_desc": descending_rank(delta_values, complement_row["delta"]),
            "exact_upper_p": exact_upper_p(delta_values, complement_row["delta"]),
        },
        "top_subsets_by_delta": rows_by_delta[:10],
        "verdict": verdict,
        "verdict_note": verdict_note,
    }

    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"prereg SHA-256: {prereg_sha}")
    print("H-NEW-285 — OQ-18 within-zone 5-vs-5 contrast test")
    print(
        f"Primary observed delta = {observed:.6f}; "
        f"target mean = {target_row['mean_pairwise_root_jaccard_subset']:.6f}; "
        f"complement mean = {target_row['mean_pairwise_root_jaccard_complement']:.6f}; "
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
