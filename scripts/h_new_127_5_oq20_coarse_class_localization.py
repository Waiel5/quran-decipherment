#!/usr/bin/env python3
"""H-NEW-127.5 - coarse-class one-vs-rest localization after H-NEW-127.4.

Observable:
  z_s = -gzip_z from the locked compression summary JSON

Label axis:
  coarse_prefix(sinai_genre) = literal first hyphen-delimited token

Per-class statistic:
  T_c = |mean(z_s | c) - mean(z_s | not c)|

Outer null:
  shuffle coarse-prefix labels across surahs, preserving class counts,
  recompute all T_c, and use maxT familywise correction across all classes.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import random
import statistics
import sys
from collections import defaultdict
from pathlib import Path


ROOT = Path("/Users/grey/Downloads/quran")
SEED = 20260419
N_PERM = 20000
ALPHA = 0.05

PREREG_FILE = ROOT / "findings/phase-b-hypotheses/h-new-127-5-coarse-class-localization-prereg.md"
COMPRESSION_JSON = ROOT / "findings/phase-b-hypotheses/csv/compression_self_ref_results.json"
GENRE_TSV = ROOT / "findings/classical-sources/neuwirth-sinai-genre-labels.tsv"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-127-5.json"


def load_compression_scores() -> dict[int, dict[str, float]]:
    payload = json.loads(COMPRESSION_JSON.read_text(encoding="utf-8"))
    out: dict[int, dict[str, float]] = {}
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


def quantile(sorted_values: list[float], frac: float) -> float:
    idx = max(0, min(len(sorted_values) - 1, int(math.floor(frac * len(sorted_values)))))
    return sorted_values[idx]


def one_vs_rest_delta(class_sum: float, class_n: int, total_sum: float, total_n: int) -> float:
    mean_in = class_sum / class_n
    mean_out = (total_sum - class_sum) / (total_n - class_n)
    return mean_in - mean_out


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
        sinai_label = labels[sid]["sinai_genre"]
        records.append(
            {
                "surah": sid,
                "name": scores[sid]["name"],
                "type": scores[sid]["type"],
                "z_s": scores[sid]["z_s"],
                "gzip_z": scores[sid]["gzip_z"],
                "gzip_ratio": scores[sid]["gzip_ratio"],
                "sinai_genre": sinai_label,
                "coarse_prefix": coarse_prefix(sinai_label),
                "neuwirth_genre": labels[sid]["neuwirth_genre"],
                "phase": labels[sid]["neuwirth_phase"],
                "tier": labels[sid]["jurjani_predicted_asyndeton_tier"],
            }
        )

    if len(records) != 114:
        raise RuntimeError(f"expected 114 records, found {len(records)}")

    label_sequence = [rec["coarse_prefix"] for rec in records]
    z_values = [rec["z_s"] for rec in records]
    total_n = len(z_values)
    total_sum = sum(z_values)

    class_counts: dict[str, int] = defaultdict(int)
    class_sums: dict[str, float] = defaultdict(float)
    for rec in records:
        prefix = rec["coarse_prefix"]
        class_counts[prefix] += 1
        class_sums[prefix] += rec["z_s"]

    prefixes_sorted = sorted(class_counts)
    observed_rows = []
    observed_abs = {}
    for prefix in prefixes_sorted:
        class_n = class_counts[prefix]
        class_sum = class_sums[prefix]
        mean_z = class_sum / class_n
        mean_rest = (total_sum - class_sum) / (total_n - class_n)
        delta = mean_z - mean_rest
        t_stat = abs(delta)
        observed_abs[prefix] = t_stat
        observed_rows.append(
            {
                "coarse_prefix": prefix,
                "n": class_n,
                "mean_z_s": mean_z,
                "mean_z_s_rest": mean_rest,
                "delta_mean_vs_rest": delta,
                "abs_delta_mean_vs_rest": t_stat,
            }
        )

    rng = random.Random(SEED)
    raw_ge = {prefix: 0 for prefix in prefixes_sorted}
    max_ge = {prefix: 0 for prefix in prefixes_sorted}
    max_null = []

    for _ in range(N_PERM):
        perm_labels = label_sequence[:]
        rng.shuffle(perm_labels)
        perm_sums = {prefix: 0.0 for prefix in prefixes_sorted}
        for z_s, prefix in zip(z_values, perm_labels):
            perm_sums[prefix] += z_s

        perm_abs = {}
        perm_max = 0.0
        for prefix in prefixes_sorted:
            delta = one_vs_rest_delta(perm_sums[prefix], class_counts[prefix], total_sum, total_n)
            t_stat = abs(delta)
            perm_abs[prefix] = t_stat
            if t_stat > perm_max:
                perm_max = t_stat

        max_null.append(perm_max)
        for prefix in prefixes_sorted:
            if perm_abs[prefix] >= observed_abs[prefix]:
                raw_ge[prefix] += 1
            if perm_max >= observed_abs[prefix]:
                max_ge[prefix] += 1

    max_null_sorted = sorted(max_null)
    familywise_mean = statistics.mean(max_null)
    familywise_sd = statistics.pstdev(max_null)

    for row in observed_rows:
        prefix = row["coarse_prefix"]
        row["p_raw_two_sided"] = (raw_ge[prefix] + 1) / (N_PERM + 1)
        row["p_maxT_two_sided"] = (max_ge[prefix] + 1) / (N_PERM + 1)
        row["familywise_significant"] = row["p_maxT_two_sided"] < ALPHA
        row["direction"] = "positive" if row["delta_mean_vs_rest"] > 0 else "negative"

    by_abs = sorted(
        observed_rows,
        key=lambda row: (
            row["p_maxT_two_sided"],
            -row["abs_delta_mean_vs_rest"],
            -abs(row["mean_z_s"]),
            row["coarse_prefix"],
        ),
    )
    by_mean = sorted(observed_rows, key=lambda row: (row["mean_z_s"], row["coarse_prefix"]))
    familywise_hits = [row for row in by_abs if row["familywise_significant"]]

    verdict = "POSITIVE" if familywise_hits else "NULL"

    top_negative_by_mean = by_mean[:3]
    top_positive_by_mean = list(reversed(by_mean[-3:]))
    top_negative_by_delta = sorted(
        observed_rows, key=lambda row: (row["delta_mean_vs_rest"], row["coarse_prefix"])
    )[:3]
    top_positive_by_delta = list(
        reversed(
            sorted(observed_rows, key=lambda row: (row["delta_mean_vs_rest"], row["coarse_prefix"]))[-3:]
        )
    )

    out = {
        "finding_id": "h-new-127-5",
        "title": "H-NEW-127.5 coarse-class one-vs-rest localization of locked compression structure",
        "pre_reg_sha256": prereg_sha,
        "seed": SEED,
        "date": "2026-04-19",
        "parent_finding": "h-new-127",
        "audit_backdrop": "h-new-127-4",
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
            "note": "No manual pooling; coarse classes are generated mechanically from the locked labels.",
        },
        "rules_tuple": "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; coarse label axis = first hyphen-delimited token of sinai_genre; 18 fixed one-vs-rest coarse-class cells; two-sided localization statistic T_c = |mean(z_s in c) - mean(z_s outside c)|; outer label-shuffle null preserves coarse class counts; familywise maxT correction across all 18 cells; 114 surahs)",
        "n_surahs": total_n,
        "n_perm": N_PERM,
        "alpha": ALPHA,
        "n_coarse_classes": len(prefixes_sorted),
        "class_counts": {prefix: class_counts[prefix] for prefix in prefixes_sorted},
        "localization_test": {
            "statistic": "two-sided one-vs-rest mean difference",
            "cell_statistic": "T_c = |mean(z_s in c) - mean(z_s outside c)|",
            "familywise_correction": "single-step maxT over the 18 fixed coarse classes",
            "familywise_null_mean_maxT": familywise_mean,
            "familywise_null_sd_maxT": familywise_sd,
            "familywise_null_min_maxT": min(max_null),
            "familywise_null_max_maxT": max(max_null),
            "familywise_null_quantiles": {
                "q001": quantile(max_null_sorted, 0.001),
                "q005": quantile(max_null_sorted, 0.005),
                "q01": quantile(max_null_sorted, 0.01),
                "q025": quantile(max_null_sorted, 0.025),
                "q05": quantile(max_null_sorted, 0.05),
                "q50": quantile(max_null_sorted, 0.50),
                "q95": quantile(max_null_sorted, 0.95),
                "q99": quantile(max_null_sorted, 0.99),
                "q995": quantile(max_null_sorted, 0.995),
                "q999": quantile(max_null_sorted, 0.999),
            },
            "n_familywise_significant": len(familywise_hits),
            "familywise_significant_classes": [
                {
                    "coarse_prefix": row["coarse_prefix"],
                    "direction": row["direction"],
                    "delta_mean_vs_rest": row["delta_mean_vs_rest"],
                    "abs_delta_mean_vs_rest": row["abs_delta_mean_vs_rest"],
                    "p_maxT_two_sided": row["p_maxT_two_sided"],
                }
                for row in familywise_hits
            ],
            "verdict": verdict,
        },
        "class_results_by_abs_delta": by_abs,
        "class_results_by_mean_z_s": list(reversed(by_mean)),
        "top_positive_by_mean_z_s": top_positive_by_mean,
        "top_negative_by_mean_z_s": top_negative_by_mean,
        "top_positive_by_delta": top_positive_by_delta,
        "top_negative_by_delta": top_negative_by_delta,
        "records": records,
    }

    OUT_JSON.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"verdict = {verdict}")
    print(f"n_familywise_significant = {len(familywise_hits)}")
    for row in familywise_hits:
        print(
            "SIG",
            row["coarse_prefix"],
            row["direction"],
            f"delta={row['delta_mean_vs_rest']:.12f}",
            f"p_maxT={row['p_maxT_two_sided']:.12f}",
        )
    if top_positive_by_mean:
        top = top_positive_by_mean[0]
        print(
            f"top_positive_mean = {top['coarse_prefix']} "
            f"mean_z_s={top['mean_z_s']:.12f} delta={top['delta_mean_vs_rest']:.12f}"
        )
    if top_negative_by_mean:
        bottom = top_negative_by_mean[0]
        print(
            f"top_negative_mean = {bottom['coarse_prefix']} "
            f"mean_z_s={bottom['mean_z_s']:.12f} delta={bottom['delta_mean_vs_rest']:.12f}"
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
