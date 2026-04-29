#!/usr/bin/env python3
"""H-NEW-127.10 - pooled within-phase rank test for residual coarse-prefix signal.

Observable:
  z_s = -gzip_z from the locked compression summary JSON

Primary statistic:
  T = sum(H_phase), where H_phase is Kruskal-Wallis H across
  coarse_prefix(sinai_genre) computed separately inside each informative
  neuwirth_phase block

Informative phase rule:
  a phase with at least two distinct coarse-prefix classes and at least one
  class count > 1

Outer null:
  shuffle coarse-prefix labels only within each informative phase block,
  preserving the exact observed counts inside that block, and recompute T
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import random
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path("/Users/grey/Downloads/quran")
SEED = 20260419
N_PERM = 20000
ALPHA = 0.05

PREREG_FILE = ROOT / "findings/phase-b-hypotheses/h-new-127-10-pooled-within-phase-rank-prereg.md"
COMPRESSION_JSON = ROOT / "findings/phase-b-hypotheses/csv/compression_self_ref_results.json"
GENRE_TSV = ROOT / "findings/classical-sources/neuwirth-sinai-genre-labels.tsv"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-127-10.json"


def load_compression_scores() -> dict[int, dict[str, float | int | str]]:
    payload = json.loads(COMPRESSION_JSON.read_text(encoding="utf-8"))
    out: dict[int, dict[str, float | int | str]] = {}
    for row in payload["task_A"]["surah_metrics"]:
        sid = int(row["surah"])
        gzip_z = float(row["gzip_z"])
        out[sid] = {
            "gzip_z": gzip_z,
            "z_s": -gzip_z,
            "gzip_ratio": float(row["gzip_ratio"]),
            "gzip_null_mean": float(row["gzip_null_mean"]),
            "gzip_null_std": float(row["gzip_null_std"]),
            "n_verses": int(row["n_verses"]),
            "n_chars": int(row["n_chars"]),
            "type": row["type"],
            "name": row["name"],
        }
    return out


def load_genre_labels() -> dict[int, dict[str, str]]:
    rows = [line for line in GENRE_TSV.read_text(encoding="utf-8").splitlines() if line and not line.startswith("#")]
    reader = csv.DictReader(rows, delimiter="\t")
    out: dict[int, dict[str, str]] = {}
    for row in reader:
        sid = int(row["surah_number"])
        out[sid] = row
    return out


def coarse_prefix(label: str) -> str:
    return label.split("-", 1)[0]


def phase_sort_key(phase: str) -> tuple[int, str]:
    order = {
        "liturgical-opening": 0,
        "early-Meccan": 1,
        "early-Meccan/Medinan-disputed": 2,
        "middle-Meccan": 3,
        "late-Meccan/middle-Meccan": 4,
        "late-Meccan": 5,
        "late-Meccan/Medinan-border": 6,
        "late-Meccan/Medinan-hybrid": 7,
        "Medinan-short": 8,
        "Medinan-long": 9,
    }
    return (order.get(phase, 999), phase)


def kruskal_wallis(groups: list[list[float]]) -> tuple[float, int]:
    all_vals: list[tuple[float, int]] = []
    for gi, group in enumerate(groups):
        for value in group:
            all_vals.append((value, gi))
    all_vals.sort(key=lambda item: item[0])
    n = len(all_vals)
    ranks = [0.0] * n
    i = 0
    tie_corr_sum = 0.0
    while i < n:
        j = i
        while j + 1 < n and all_vals[j + 1][0] == all_vals[i][0]:
            j += 1
        avg_rank = (i + j) / 2.0 + 1.0
        t = j - i + 1
        if t > 1:
            tie_corr_sum += t**3 - t
        for k in range(i, j + 1):
            ranks[k] = avg_rank
        i = j + 1
    sum_r = defaultdict(float)
    n_r = defaultdict(int)
    for idx, (_value, gi) in enumerate(all_vals):
        sum_r[gi] += ranks[idx]
        n_r[gi] += 1
    h = 12.0 / (n * (n + 1)) * sum((sum_r[gi] ** 2) / n_r[gi] for gi in sum_r) - 3.0 * (n + 1)
    if tie_corr_sum > 0 and n > 1:
        correction = 1.0 - tie_corr_sum / (n**3 - n)
        if correction > 0:
            h /= correction
    return h, len(groups) - 1


def quantile(sorted_values: list[float], frac: float) -> float:
    idx = max(0, min(len(sorted_values) - 1, int(math.floor(frac * len(sorted_values)))))
    return sorted_values[idx]


def is_informative_block(counts: Counter[str]) -> bool:
    return len(counts) >= 2 and max(counts.values()) > 1


def summarize_block(records: list[dict[str, object]], counts: Counter[str]) -> dict[str, object]:
    return {
        "n": len(records),
        "n_coarse_classes": len(counts),
        "coarse_prefix_counts": {prefix: counts[prefix] for prefix in sorted(counts)},
        "mean_z_s": statistics.mean(float(rec["z_s"]) for rec in records),
        "median_z_s": statistics.median(float(rec["z_s"]) for rec in records),
    }


def main() -> int:
    prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
    print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)
    print(f"SEED = {SEED}", file=sys.stderr)
    print(f"N_PERM = {N_PERM}", file=sys.stderr)
    print(f"ALPHA = {ALPHA}", file=sys.stderr)

    scores = load_compression_scores()
    labels = load_genre_labels()

    records = []
    for sid in range(1, 115):
        if sid not in scores or sid not in labels:
            continue
        phase = labels[sid]["neuwirth_phase"]
        sinai_label = labels[sid]["sinai_genre"]
        if not phase:
            raise RuntimeError(f"missing neuwirth_phase for surah {sid}")
        if not sinai_label:
            raise RuntimeError(f"missing sinai_genre for surah {sid}")
        records.append(
            {
                "surah": sid,
                "name": scores[sid]["name"],
                "type": scores[sid]["type"],
                "z_s": scores[sid]["z_s"],
                "gzip_z": scores[sid]["gzip_z"],
                "gzip_ratio": scores[sid]["gzip_ratio"],
                "phase": phase,
                "sinai_genre": sinai_label,
                "coarse_prefix": coarse_prefix(sinai_label),
                "neuwirth_genre": labels[sid]["neuwirth_genre"],
                "tier": labels[sid]["jurjani_predicted_asyndeton_tier"],
            }
        )

    if len(records) != 114:
        raise RuntimeError(f"expected 114 records, found {len(records)}")

    phase_records: dict[str, list[dict[str, object]]] = defaultdict(list)
    phase_counts: dict[str, Counter[str]] = defaultdict(Counter)
    for rec in records:
        phase = str(rec["phase"])
        prefix = str(rec["coarse_prefix"])
        phase_records[phase].append(rec)
        phase_counts[phase][prefix] += 1

    phases_sorted = sorted(phase_records, key=phase_sort_key)
    informative_phases = [phase for phase in phases_sorted if is_informative_block(phase_counts[phase])]
    excluded_single_class = [phase for phase in phases_sorted if len(phase_counts[phase]) == 1]
    excluded_all_singletons = [
        phase for phase in phases_sorted if len(phase_counts[phase]) >= 2 and max(phase_counts[phase].values()) == 1
    ]

    phase_contributions = []
    observed_by_phase: dict[str, float] = {}
    df_by_phase: dict[str, int] = {}
    phase_labels: dict[str, list[str]] = {}
    phase_z_values: dict[str, list[float]] = {}
    phase_prefix_order: dict[str, list[str]] = {}
    t_obs = 0.0
    df_total = 0

    for phase in informative_phases:
        block = phase_records[phase]
        counts = phase_counts[phase]
        prefixes = sorted(counts)
        groups = [[float(rec["z_s"]) for rec in block if str(rec["coarse_prefix"]) == prefix] for prefix in prefixes]
        h_obs, df = kruskal_wallis(groups)
        observed_by_phase[phase] = h_obs
        df_by_phase[phase] = df
        phase_labels[phase] = [str(rec["coarse_prefix"]) for rec in block]
        phase_z_values[phase] = [float(rec["z_s"]) for rec in block]
        phase_prefix_order[phase] = prefixes
        t_obs += h_obs
        df_total += df
        phase_contributions.append(
            {
                "phase": phase,
                "n": len(block),
                "df": df,
                "observed_H": h_obs,
                "coarse_prefix_counts": {prefix: counts[prefix] for prefix in prefixes},
                "mean_z_s": statistics.mean(float(rec["z_s"]) for rec in block),
                "median_z_s": statistics.median(float(rec["z_s"]) for rec in block),
            }
        )

    rng = random.Random(SEED)
    t_null = []
    n_ge = 0
    phase_null_sums = defaultdict(float)
    phase_null_sq_sums = defaultdict(float)
    phase_ge = defaultdict(int)
    for _ in range(N_PERM):
        perm_t = 0.0
        for phase in informative_phases:
            labels_phase = phase_labels[phase][:]
            rng.shuffle(labels_phase)
            perm_groups: dict[str, list[float]] = defaultdict(list)
            for z_s, prefix in zip(phase_z_values[phase], labels_phase):
                perm_groups[prefix].append(z_s)
            perm_h, _ = kruskal_wallis([perm_groups[prefix] for prefix in phase_prefix_order[phase]])
            perm_t += perm_h
            phase_null_sums[phase] += perm_h
            phase_null_sq_sums[phase] += perm_h * perm_h
            if perm_h >= observed_by_phase[phase]:
                phase_ge[phase] += 1
        t_null.append(perm_t)
        if perm_t >= t_obs:
            n_ge += 1

    t_null_sorted = sorted(t_null)
    null_mean = statistics.mean(t_null)
    null_sd = statistics.pstdev(t_null)
    z_vs_null = (t_obs - null_mean) / null_sd if null_sd > 0 else 0.0
    p_perm = (n_ge + 1) / (N_PERM + 1)
    verdict = "POSITIVE" if p_perm < ALPHA else "NULL"

    phase_contributions_out = []
    for row in phase_contributions:
        phase = str(row["phase"])
        phase_mean = phase_null_sums[phase] / N_PERM
        phase_var = max(0.0, phase_null_sq_sums[phase] / N_PERM - phase_mean * phase_mean)
        phase_sd = math.sqrt(phase_var)
        phase_contributions_out.append(
            {
                **row,
                "null_mean_H": phase_mean,
                "null_sd_H": phase_sd,
                "p_perm_upper_unadjusted": (phase_ge[phase] + 1) / (N_PERM + 1),
            }
        )

    excluded_blocks = []
    for phase in phases_sorted:
        if phase in informative_phases:
            continue
        counts = phase_counts[phase]
        excluded_blocks.append(
            {
                "phase": phase,
                "exclusion_reason": (
                    "single-class"
                    if len(counts) == 1
                    else "all-singletons"
                ),
                **summarize_block(phase_records[phase], counts),
            }
        )

    out = {
        "finding_id": "h-new-127-10",
        "title": "H-NEW-127.10 pooled within-phase rank test for residual coarse-prefix OQ-20 structure",
        "pre_reg_sha256": prereg_sha,
        "seed": SEED,
        "date": "2026-04-19",
        "parent_finding": "h-new-127",
        "audit_backdrop": "h-new-127-8",
        "observable": {
            "source_file": "findings/phase-b-hypotheses/csv/compression_self_ref_results.json",
            "source_field": "task_A.surah_metrics.gzip_z",
            "definition": "z_s = -gzip_z so larger values mean stronger compression relative to the locked length-matched null",
        },
        "label_axis": {
            "source_file": "findings/classical-sources/neuwirth-sinai-genre-labels.tsv",
            "field": "sinai_genre",
            "coarsening_rule": "literal first hyphen-delimited token of sinai_genre; labels without hyphens remain unchanged",
            "derived_field": "coarse_prefix(sinai_genre)",
            "note": "No manual pooling; coarse classes are generated mechanically from the locked labels exactly as in H-NEW-127.4 and H-NEW-127.8.",
        },
        "conditioning_axis": {
            "source_file": "findings/classical-sources/neuwirth-sinai-genre-labels.tsv",
            "field": "neuwirth_phase",
            "note": "The test statistic is computed separately within these exact locked phase blocks and then pooled.",
        },
        "rules_tuple": "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = coarse_prefix(sinai_genre); conditioning axis = neuwirth_phase; statistic = sum of within-phase Kruskal-Wallis H values over informative phase blocks only; informative block rule = at least two coarse-prefix classes present and at least one class count > 1; outer null shuffles coarse-prefix labels only within each informative phase block, preserving observed counts; 114 surahs)",
        "n_surahs": 114,
        "n_perm": N_PERM,
        "alpha": ALPHA,
        "n_phases_total": len(phases_sorted),
        "n_informative_phases": len(informative_phases),
        "n_excluded_single_class_phases": len(excluded_single_class),
        "n_excluded_all_singleton_phases": len(excluded_all_singletons),
        "n_surahs_in_informative_phases": sum(len(phase_records[phase]) for phase in informative_phases),
        "n_surahs_in_excluded_phases": sum(len(phase_records[phase]) for phase in phases_sorted if phase not in informative_phases),
        "phase_diagnostics": {
            "informative_phases": [
                {
                    "phase": phase,
                    **summarize_block(phase_records[phase], phase_counts[phase]),
                }
                for phase in informative_phases
            ],
            "excluded_phases": excluded_blocks,
        },
        "primary_test": {
            "statistic": "T = sum(H_phase) across informative phase blocks",
            "observed_T": t_obs,
            "df_sum_descriptive": df_total,
            "null_mean_T": null_mean,
            "null_sd_T": null_sd,
            "null_min_T": min(t_null),
            "null_max_T": max(t_null),
            "null_quantiles": {
                "q001": quantile(t_null_sorted, 0.001),
                "q005": quantile(t_null_sorted, 0.005),
                "q01": quantile(t_null_sorted, 0.01),
                "q025": quantile(t_null_sorted, 0.025),
                "q05": quantile(t_null_sorted, 0.05),
                "q50": quantile(t_null_sorted, 0.50),
                "q95": quantile(t_null_sorted, 0.95),
                "q99": quantile(t_null_sorted, 0.99),
                "q995": quantile(t_null_sorted, 0.995),
                "q999": quantile(t_null_sorted, 0.999),
            },
            "z_vs_null": z_vs_null,
            "n_perm_ge_obs": n_ge,
            "p_perm_upper": p_perm,
            "verdict": verdict,
        },
        "phase_contributions": phase_contributions_out,
        "surah_rows": records,
        "verdict": verdict,
    }

    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {OUT_JSON}", file=sys.stderr)
    print(json.dumps(out["primary_test"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
