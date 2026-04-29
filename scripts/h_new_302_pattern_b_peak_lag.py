#!/usr/bin/env python3
"""H-NEW-302 - Pattern-B marker-versus-content peak-lag test."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np


ROOT = Path("/Users/grey/Downloads/quran")
PREREG_FILE = (
    ROOT
    / "findings/phase-b-hypotheses/h-new-302-pattern-b-marker-content-peak-lag-prereg.md"
)
UPSTREAM_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-125.json"
CF012_JSON = ROOT / "findings/phase-b-hypotheses/csv/cross-finding-012.json"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-302.json"

DATE = "2026-04-20"
SEED = 20260420
N_PERM = 10_000
N_BINS = 8

MARKER_AXIS = "muq_cardinality"
CONTENT_AXES = [
    "qul_density",
    "book_reference_density",
    "eschatological_density",
    "loanword_density",
]


def rank_to_bin(rank_array: np.ndarray, edges: np.ndarray) -> np.ndarray:
    return np.digitize(rank_array, edges, right=False)


def per_bin_means(values: np.ndarray, bin_assignments: np.ndarray) -> np.ndarray:
    means = np.full(N_BINS, np.nan, dtype=float)
    for b in range(N_BINS):
        mask = bin_assignments == b
        if mask.sum() > 0:
            means[b] = float(values[mask].mean())
    return means


def smallest_peak_bin(means: np.ndarray) -> int:
    peak_value = float(np.nanmax(means))
    for idx, value in enumerate(means):
        if np.isclose(value, peak_value):
            return idx
    raise RuntimeError("peak bin resolution failed")


def compute_axis_profile(
    axis_values: dict[str, np.ndarray], axis_name: str, bins: np.ndarray
) -> dict[str, object]:
    means = per_bin_means(axis_values[axis_name], bins)
    peak_bin_idx = smallest_peak_bin(means)
    return {
        "axis": axis_name,
        "peak_bin_idx_0": peak_bin_idx,
        "peak_bin_label": f"B{peak_bin_idx + 1}",
        "means_by_bin": {f"B{i+1}": float(means[i]) for i in range(N_BINS)},
    }


def compute_l_peak(axis_values: dict[str, np.ndarray], bins: np.ndarray) -> dict[str, object]:
    marker = compute_axis_profile(axis_values, MARKER_AXIS, bins)
    contents = [compute_axis_profile(axis_values, axis, bins) for axis in CONTENT_AXES]
    content_peaks_1 = [row["peak_bin_idx_0"] + 1 for row in contents]
    marker_peak_1 = marker["peak_bin_idx_0"] + 1
    l_peak = float(sum(content_peaks_1) / len(content_peaks_1) - marker_peak_1)
    return {
        "marker": marker,
        "contents": contents,
        "content_peak_bins_1indexed": content_peaks_1,
        "marker_peak_bin_1indexed": marker_peak_1,
        "l_peak": l_peak,
    }


def main() -> int:
    prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()

    with open(UPSTREAM_JSON, encoding="utf-8") as handle:
        h125 = json.load(handle)
    with open(CF012_JSON, encoding="utf-8") as handle:
        cf012 = json.load(handle)

    per_surah = h125["per_surah_axis_values"]
    sids = sorted(int(k) for k in per_surah.keys())
    if sids != list(range(1, 115)):
        raise RuntimeError("expected 114 surahs indexed 1..114")

    noldeke_rank = np.array([per_surah[str(sid)]["noldeke_rank"] for sid in sids], dtype=int)
    axis_values = {
        axis: np.array(
            [per_surah[str(sid)]["axis_values"][axis] for sid in sids], dtype=float
        )
        for axis in [MARKER_AXIS] + CONTENT_AXES
    }

    edges = np.quantile(
        np.arange(1, 115), np.linspace(1 / N_BINS, (N_BINS - 1) / N_BINS, N_BINS - 1)
    )
    observed_bins = rank_to_bin(noldeke_rank, edges)
    observed = compute_l_peak(axis_values, observed_bins)

    expected_peak_bins = cf012["pattern_b"]["per_axis_peak_bin"]
    reproduced_peak_bins = {
        MARKER_AXIS: observed["marker"]["peak_bin_label"],
        **{row["axis"]: row["peak_bin_label"] for row in observed["contents"]},
    }
    positive_control_pass = reproduced_peak_bins == expected_peak_bins
    if not positive_control_pass:
        raise RuntimeError(
            f"positive control failed: reproduced {reproduced_peak_bins} vs expected {expected_peak_bins}"
        )

    rng = np.random.default_rng(SEED)
    l_perm = np.empty(N_PERM, dtype=float)
    config_counts: dict[str, int] = {}

    for i in range(N_PERM):
        perm_ranks = rng.permutation(noldeke_rank)
        perm_bins = rank_to_bin(perm_ranks, edges)
        stats = compute_l_peak(axis_values, perm_bins)
        l_perm[i] = stats["l_peak"]
        config_key = (
            f"muq=B{stats['marker_peak_bin_1indexed']};"
            f"content={[f'B{x}' for x in stats['content_peak_bins_1indexed']]}"
        )
        config_counts[config_key] = config_counts.get(config_key, 0) + 1

    l_obs = observed["l_peak"]
    p_lag = float((1 + np.sum(l_perm >= l_obs)) / (1 + N_PERM))
    rank_desc = int(1 + np.sum(l_perm > l_obs))
    verdict = "PASS-DIRECTED" if p_lag < 0.05 else "NULL"

    out = {
        "finding_id": "h-new-302",
        "title": "Pattern-B marker-versus-content peak-lag test",
        "date": DATE,
        "pre_reg_sha256": prereg_sha,
        "parent_backdrop": ["cross-finding-012", "cross-finding-017", "h-new-129"],
        "rules_tuple": "(reuse H-NEW-125 per-surah axis values exactly; reuse cross-finding-012 equal-count Noldke octile bins B1..B8 exactly; marker axis = muq_cardinality; content axes = qul_density, book_reference_density, eschatological_density, loanword_density; for each axis define peak_bin(a) as the smallest octile attaining the maximum observed bin mean; primary statistic L_peak = mean_content peak_bin(a) - peak_bin(marker); null by 10000 permutations of the 114 Noldke ranks across surahs with octile reassignment recomputed each time; one-sided upper-tail for content peaking later than marker; imported-family positive control = exact reproduction of cross-finding-012 observed Pattern-B peak bins under the inherited observed octile mapping)",
        "seed": SEED,
        "n_perm": N_PERM,
        "n_bins": N_BINS,
        "bin_rank_upper_edges": [float(x) for x in edges],
        "marker_axis": MARKER_AXIS,
        "content_axes": CONTENT_AXES,
        "positive_control": {
            "expected_peak_bins_from_cf012": expected_peak_bins,
            "reproduced_peak_bins": reproduced_peak_bins,
            "pass": positive_control_pass,
        },
        "observed": {
            "marker": observed["marker"],
            "contents": observed["contents"],
            "marker_peak_bin_1indexed": observed["marker_peak_bin_1indexed"],
            "content_peak_bins_1indexed": observed["content_peak_bins_1indexed"],
            "l_peak": l_obs,
        },
        "null_summary": {
            "mean": float(l_perm.mean()),
            "q95": float(np.quantile(l_perm, 0.95)),
            "q99": float(np.quantile(l_perm, 0.99)),
            "max": float(l_perm.max()),
            "rank_desc": rank_desc,
            "p_lag_upper": p_lag,
            "top_configurations": sorted(
                (
                    {"configuration": key, "count": value}
                    for key, value in config_counts.items()
                ),
                key=lambda row: (-row["count"], row["configuration"]),
            )[:10],
        },
        "verdict": verdict,
        "verdict_note": (
            "This is a post-hoc-noticed formalization of the already disclosed "
            "B6/B7 staircase, so the strongest honest positive reading is PASS-DIRECTED."
        ),
    }

    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
