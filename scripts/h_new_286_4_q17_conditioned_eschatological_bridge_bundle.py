#!/usr/bin/env python3
"""H-NEW-286.4 — Q17-conditioned eschatological bridge-bundle exact test."""
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
    / "h-new-286-4-q17-conditioned-eschatological-bridge-bundle-prereg.md"
)
H125_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-125.json"
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-286-4.json"

ZONE = tuple(range(16, 26))
TARGET = (16, 17, 21, 22, 23, 25)
ALPHA = 0.05
AXIS = "eschatological_density"


def load_h125() -> dict:
    return json.loads(H125_JSON.read_text(encoding="utf-8"))


def zscore(values: list[float]) -> list[float]:
    mu = statistics.mean(values)
    sd = math.sqrt(sum((v - mu) ** 2 for v in values) / len(values)) or 1.0
    return [(v - mu) / sd for v in values]


def mean_of_subset(values: dict[int, float], subset: tuple[int, ...]) -> float:
    return statistics.mean(values[sid] for sid in subset)


def exact_upper_p(values: list[float], observed: float) -> float:
    return sum(1 for value in values if value >= observed) / len(values)


def descending_rank(values: list[float], observed: float) -> int:
    return 1 + sum(1 for value in values if value > observed)


def main() -> int:
    prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    h125 = load_h125()
    psv = h125["per_surah_axis_values"]

    ordered = [
        (int(sid), float(entry["axis_values"][AXIS]))
        for sid, entry in psv.items()
    ]
    ordered.sort()
    surahs = [sid for sid, _ in ordered]
    raw = [value for _, value in ordered]
    z = zscore(raw)
    axis_z = dict(zip(surahs, z))

    rows = []
    for subset in combinations(ZONE, 6):
        complement = tuple(sorted(set(ZONE) - set(subset)))
        subset_mean = mean_of_subset(axis_z, subset)
        complement_mean = mean_of_subset(axis_z, complement)
        delta_e = subset_mean - complement_mean
        rows.append(
            {
                "subset": list(subset),
                "complement_subset": list(complement),
                "mean_eschat_z_subset": subset_mean,
                "mean_eschat_z_complement": complement_mean,
                "delta_e": delta_e,
            }
        )

    rows_by_delta = sorted(
        rows,
        key=lambda row: (-row["delta_e"], -row["mean_eschat_z_subset"], row["subset"]),
    )
    target_row = next(row for row in rows if tuple(row["subset"]) == TARGET)
    delta_values = [row["delta_e"] for row in rows]
    observed = target_row["delta_e"]
    n_ge = sum(1 for value in delta_values if value >= observed)
    p_exact = exact_upper_p(delta_values, observed)
    rank_desc = descending_rank(delta_values, observed)
    tie_count = sum(1 for value in delta_values if value == observed)
    verdict = "PASS-DIRECTED" if p_exact < ALPHA else "NULL"

    zone_profile = {
        str(sid): {
            "eschat_z": axis_z[sid],
            "in_target_bundle": sid in TARGET,
        }
        for sid in ZONE
    }

    out = {
        "id": "H-NEW-286.4",
        "title": "Q17-conditioned eschatological bridge-bundle exact test",
        "date": "2026-04-19",
        "prereg_file": str(PREREG.relative_to(ROOT)),
        "prereg_sha256": prereg_sha,
        "script_file": "scripts/h_new_286_4_q17_conditioned_eschatological_bridge_bundle.py",
        "axis_source": {
            "source_file": "findings/phase-b-hypotheses/csv/h-new-125.json",
            "axis": AXIS,
            "standardization": "z-score across all 114 surahs using population mean and population standard deviation",
        },
        "rules_tuple": (
            "(H-NEW-125 per-surah eschatological_density reused from h-new-125.json; "
            "z-score computed across all 114 surahs using population mean and population standard deviation; "
            "exact within-zone enumeration over all C(10,6)=210 six-surah subsets of Q16..Q25; "
            "target bundle fixed to B*={Q16,Q17,Q21,Q22,Q23,Q25}; "
            "primary statistic Delta_E(S)=mean_{q in S} z_eschat(q)-mean_{q in Z\\S} z_eschat(q); "
            "one-sided upper-tail exact null)"
        ),
        "zone": list(ZONE),
        "target_subset": list(TARGET),
        "exact_space_n": len(rows),
        "primary": {
            "statistic": "delta_e_bridge_bundle",
            "direction": "upper",
            "observed": observed,
            "target_mean_eschat_z": target_row["mean_eschat_z_subset"],
            "complement_mean_eschat_z": target_row["mean_eschat_z_complement"],
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
        "top_subsets_by_delta": rows_by_delta[:10],
        "zone_profile": zone_profile,
        "verdict": verdict,
    }

    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"prereg SHA-256: {prereg_sha}")
    print("H-NEW-286.4 — Q17-conditioned eschatological bridge-bundle exact test")
    print(
        f"Observed delta = {observed:.12f}; "
        f"target mean = {target_row['mean_eschat_z_subset']:.12f}; "
        f"complement mean = {target_row['mean_eschat_z_complement']:.12f}; "
        f"rank = {rank_desc}/{len(rows)}; p_exact_upper = {p_exact:.12f}"
    )
    print(
        f"Null mean = {statistics.mean(delta_values):.12f}; "
        f"median = {statistics.median(delta_values):.12f}; "
        f"min = {min(delta_values):.12f}; max = {max(delta_values):.12f}"
    )
    print(f"Verdict: {verdict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
