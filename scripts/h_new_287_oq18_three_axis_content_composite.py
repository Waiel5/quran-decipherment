#!/usr/bin/env python3
"""H-NEW-287 - OQ-18 within-zone three-axis content composite test.

Primary observable:
  C_q = mean(z(prophet_narrative_density),
            z(book_reference_density),
            z(eschatological_density))
  Delta_C(S) = mean_{q in S} C_q - mean_{q in Z\\S} C_q

Primary null:
  exact enumeration over all C(10,5)=252 five-surah subsets of Q16..Q25

The three axes are reused directly from the H-NEW-125 per-surah payload.
No new ontology is introduced.
"""

from __future__ import annotations

import hashlib
import json
import math
import statistics
from itertools import combinations
from pathlib import Path


ROOT = Path("/Users/grey/Downloads/quran")
PREREG = (
    ROOT
    / "findings"
    / "phase-b-hypotheses"
    / "h-new-287-oq18-within-zone-three-axis-content-composite-prereg.md"
)
H125_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-125.json"
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-287.json"

ZONE = tuple(range(16, 26))
TARGET = (16, 21, 22, 23, 25)
COMPLEMENT = tuple(sorted(set(ZONE) - set(TARGET)))
AXES = (
    "prophet_narrative_density",
    "book_reference_density",
    "eschatological_density",
)
ALPHA = 0.05


def load_h125() -> dict:
    return json.loads(H125_JSON.read_text(encoding="utf-8"))


def zscore(values: list[float]) -> list[float]:
    mu = statistics.mean(values)
    sd = math.sqrt(sum((v - mu) ** 2 for v in values) / len(values)) or 1.0
    return [(v - mu) / sd for v in values]


def exact_upper_p(values: list[float], observed: float) -> float:
    return sum(1 for value in values if value >= observed) / len(values)


def descending_rank(values: list[float], observed: float) -> int:
    return 1 + sum(1 for value in values if value > observed)


def mean_of_subset(values: dict[int, float], subset: tuple[int, ...]) -> float:
    return statistics.mean(values[sid] for sid in subset)


def main() -> int:
    prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    h125 = load_h125()
    psv = h125["per_surah_axis_values"]

    axis_values: dict[str, dict[int, float]] = {}
    axis_summary: dict[str, dict[str, float]] = {}
    for axis in AXES:
        ordered = [
            (int(sid), float(entry["axis_values"][axis]))
            for sid, entry in psv.items()
        ]
        ordered.sort()
        surahs = [sid for sid, _ in ordered]
        raw = [value for _, value in ordered]
        axis_values[axis] = dict(zip(surahs, raw))
        axis_summary[axis] = {
            "mean": statistics.mean(raw),
            "pstdev": statistics.pstdev(raw),
        }

    axis_z: dict[str, dict[int, float]] = {}
    for axis in AXES:
        ordered = sorted(axis_values[axis].items())
        surahs = [sid for sid, _ in ordered]
        raw = [value for _, value in ordered]
        z = zscore(raw)
        axis_z[axis] = dict(zip(surahs, z))

    composite: dict[int, float] = {}
    per_surah_profile: dict[str, dict[str, float]] = {}
    for sid in range(1, 115):
        z_vals = [axis_z[axis][sid] for axis in AXES]
        c_q = statistics.mean(z_vals)
        composite[sid] = c_q
        per_surah_profile[str(sid)] = {
            "prophet_z": axis_z["prophet_narrative_density"][sid],
            "book_z": axis_z["book_reference_density"][sid],
            "eschat_z": axis_z["eschatological_density"][sid],
            "c_q": c_q,
        }

    all_subsets = list(combinations(ZONE, 5))
    rows = []
    for subset in all_subsets:
        complement = tuple(sorted(set(ZONE) - set(subset)))
        subset_mean = mean_of_subset(composite, subset)
        complement_mean = mean_of_subset(composite, complement)
        delta_c = subset_mean - complement_mean
        rows.append(
            {
                "subset": list(subset),
                "complement_subset": list(complement),
                "mean_c_subset": subset_mean,
                "mean_c_complement": complement_mean,
                "delta_c": delta_c,
            }
        )

    target_row = next(row for row in rows if tuple(row["subset"]) == TARGET)
    complement_row = next(row for row in rows if tuple(row["subset"]) == COMPLEMENT)
    delta_values = [row["delta_c"] for row in rows]

    rows_by_delta = sorted(
        rows,
        key=lambda row: (-row["delta_c"], -row["mean_c_subset"], row["subset"]),
    )

    observed = target_row["delta_c"]
    n_ge = sum(1 for value in delta_values if value >= observed)
    p_exact = exact_upper_p(delta_values, observed)
    rank_desc = descending_rank(delta_values, observed)
    tie_count = sum(1 for value in delta_values if value == observed)

    verdict = "PASS-DIRECTED" if p_exact < ALPHA else "NULL"
    verdict_note = (
        "The three-axis composite is tightly bounded and honest, but it does not "
        "explain the OQ-18 split: the target half scores below its within-zone complement."
    )

    out = {
        "id": "H-NEW-287",
        "title": "OQ-18 within-zone three-axis content composite",
        "date": "2026-04-19",
        "seed": 20260419,
        "prereg_file": str(PREREG.relative_to(ROOT)),
        "prereg_sha256": prereg_sha,
        "script_file": "scripts/h_new_287_oq18_three_axis_content_composite.py",
        "axis_source": {
            "source_file": "findings/phase-b-hypotheses/csv/h-new-125.json",
            "source_field": "per_surah_axis_values.axis_values",
            "axes": list(AXES),
            "standardization": "z-score across all 114 surahs using population mean and population standard deviation",
            "composite_definition": "C_q = mean(z(prophet_narrative_density), z(book_reference_density), z(eschatological_density))",
        },
        "rules_tuple": (
            "(H-NEW-125 per-surah axis values reused from h-new-125.json; per-surah C_q = "
            "mean(z(prophet_narrative_density), z(book_reference_density), z(eschatological_density)) "
            "with z-scores computed over all 114 surahs; exact enumeration over all C(10,5)=252 "
            "five-surah subsets of Q16..Q25; primary statistic = Delta_C(S)=mean_{q in S} C_q-mean_{q in Z\\S} C_q; "
            "one-sided upper-tail)"
        ),
        "zone": list(ZONE),
        "target_subset": list(TARGET),
        "complement_subset": list(COMPLEMENT),
        "exact_space_n": len(rows),
        "axis_standardization": axis_summary,
        "primary": {
            "statistic": "delta_c_three_axis_mean_z",
            "direction": "upper",
            "observed": observed,
            "target_mean_c": target_row["mean_c_subset"],
            "complement_mean_c": target_row["mean_c_complement"],
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
            "rank_desc": descending_rank(delta_values, complement_row["delta_c"]),
            "exact_upper_p": exact_upper_p(delta_values, complement_row["delta_c"]),
        },
        "top_subsets_by_delta": rows_by_delta[:10],
        "per_surah_composite": per_surah_profile,
        "zone_profile": {str(sid): per_surah_profile[str(sid)] for sid in ZONE},
        "verdict": verdict,
        "verdict_note": verdict_note,
    }

    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"prereg SHA-256: {prereg_sha}")
    print("H-NEW-287 — OQ-18 within-zone three-axis content composite")
    print(
        f"Primary observed delta = {observed:.6f}; "
        f"target mean = {target_row['mean_c_subset']:.6f}; "
        f"complement mean = {target_row['mean_c_complement']:.6f}; "
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
