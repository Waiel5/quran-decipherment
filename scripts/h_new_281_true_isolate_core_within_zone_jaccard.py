#!/usr/bin/env python3
"""H-NEW-281 — true-isolate core within-zone exact Jaccard test.

Primary observable:
  mean pairwise root-set Jaccard within the fixed target subset
  {Q16, Q21, Q22, Q23, Q25}

Primary null:
  exact enumeration over all C(10,5)=252 five-surah subsets of Q16..Q25

Secondary descriptive observable:
  shared-root spine count = number of roots present in all 5 surahs of a
  subset
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
    / "h-new-281-true-isolate-core-within-zone-jaccard-prereg.md"
)
ROOT_GRAPH = ROOT / "data" / "morphology" / "surah-root-graph.json"
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-281.json"

ZONE = tuple(range(16, 26))
TARGET = (16, 21, 22, 23, 25)
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
        inter = len(roots_a & roots_b)
        union = len(roots_a | roots_b)
        values.append(inter / union if union else 0.0)
    return statistics.mean(values) if values else 0.0


def shared_root_spine_roots(
    subset: tuple[int, ...], root_sets: dict[int, frozenset[str]]
) -> list[str]:
    shared = set(root_sets[subset[0]])
    for sid in subset[1:]:
        shared &= set(root_sets[sid])
    return sorted(shared)


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
        mean_jaccard = pairwise_mean_root_jaccard(subset, root_sets)
        spine_roots = shared_root_spine_roots(subset, root_sets)
        rows.append(
            {
                "subset": list(subset),
                "mean_pairwise_root_jaccard": mean_jaccard,
                "shared_root_spine_count": len(spine_roots),
                "shared_root_spine_roots": spine_roots,
            }
        )

    target_row = next(row for row in rows if tuple(row["subset"]) == TARGET)
    primary_values = [row["mean_pairwise_root_jaccard"] for row in rows]
    spine_values = [row["shared_root_spine_count"] for row in rows]

    rows_by_primary = sorted(
        rows,
        key=lambda row: (
            -row["mean_pairwise_root_jaccard"],
            -row["shared_root_spine_count"],
            row["subset"],
        ),
    )
    rows_by_spine = sorted(
        rows,
        key=lambda row: (
            -row["shared_root_spine_count"],
            -row["mean_pairwise_root_jaccard"],
            row["subset"],
        ),
    )

    complement_subset = tuple(sorted(set(ZONE) - set(TARGET)))
    complement_row = next(row for row in rows if tuple(row["subset"]) == complement_subset)

    primary_obs = target_row["mean_pairwise_root_jaccard"]
    spine_obs = target_row["shared_root_spine_count"]
    primary_n_ge = sum(1 for value in primary_values if value >= primary_obs)
    primary_p = exact_upper_p(primary_values, primary_obs)
    primary_rank = descending_rank(primary_values, primary_obs)
    primary_tie_count = sum(1 for value in primary_values if value == primary_obs)

    spine_n_ge = sum(1 for value in spine_values if value >= spine_obs)
    spine_rank = descending_rank(spine_values, spine_obs)
    spine_tie_count = sum(1 for value in spine_values if value == spine_obs)
    spine_p_like = exact_upper_p([float(v) for v in spine_values], float(spine_obs))

    verdict = "PASS-DIRECTED" if primary_p < ALPHA else "NULL"
    verdict_note = (
        "Target subset was surfaced by prior work, so a passing result is capped at "
        "PASS-DIRECTED under this new bounded exact null."
    )

    out = {
        "id": "H-NEW-281",
        "title": "true-isolate core within-zone exact Jaccard test",
        "date": "2026-04-18",
        "seed": 20260418,
        "prereg_file": str(PREREG.relative_to(ROOT)),
        "prereg_sha256": prereg_sha,
        "script_file": "scripts/h_new_281_true_isolate_core_within_zone_jaccard.py",
        "rules_tuple": (
            "(QAC v0.4 root sets via surah-root-graph.json; exact enumeration over "
            "all C(10,5)=252 five-surah subsets of Q16..Q25; primary statistic = "
            "mean pairwise root-set Jaccard; one-sided upper-tail)"
        ),
        "zone": list(ZONE),
        "target_subset": list(TARGET),
        "exact_space_n": len(rows),
        "zone_root_set_sizes": {str(sid): len(root_sets[sid]) for sid in ZONE},
        "primary": {
            "statistic": "mean_pairwise_root_jaccard",
            "direction": "upper",
            "observed": primary_obs,
            "n_ge_observed": primary_n_ge,
            "exact_upper_p": primary_p,
            "rank_desc": primary_rank,
            "tie_count_at_observed": primary_tie_count,
            "null_mean_full_space": statistics.mean(primary_values),
            "null_median_full_space": statistics.median(primary_values),
            "null_min_full_space": min(primary_values),
            "null_max_full_space": max(primary_values),
            "alpha": ALPHA,
            "verdict": verdict,
        },
        "secondary_descriptive": {
            "statistic": "shared_root_spine_count",
            "observed": spine_obs,
            "n_ge_observed_for_context_only": spine_n_ge,
            "rank_desc": spine_rank,
            "tie_count_at_observed": spine_tie_count,
            "exact_upper_fraction_for_context_only": spine_p_like,
            "shared_root_spine_roots_target": target_row["shared_root_spine_roots"],
            "note": (
                "Secondary descriptive only. Exact rank/fraction reported for context "
                "but does not drive the family verdict."
            ),
        },
        "target_subset_detail": target_row,
        "complement_subset_detail": {
            **complement_row,
            "rank_desc": descending_rank(
                primary_values, complement_row["mean_pairwise_root_jaccard"]
            ),
            "exact_upper_p": exact_upper_p(
                primary_values, complement_row["mean_pairwise_root_jaccard"]
            ),
        },
        "top_subsets_by_primary": rows_by_primary[:10],
        "top_subsets_by_shared_root_spine": rows_by_spine[:10],
        "verdict": verdict,
        "verdict_note": verdict_note,
    }

    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"prereg SHA-256: {prereg_sha}")
    print("H-NEW-281 — true-isolate core within-zone exact Jaccard test")
    print(
        f"Primary observed mean pairwise root-Jaccard = {primary_obs:.6f}; "
        f"rank = {primary_rank}/{len(rows)}; p_exact_upper = {primary_p:.6f}"
    )
    print(
        f"Secondary shared-root spine count = {spine_obs}; "
        f"rank = {spine_rank}/{len(rows)}; "
        f"exact upper fraction = {spine_p_like:.6f}"
    )
    print(f"Verdict: {verdict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
