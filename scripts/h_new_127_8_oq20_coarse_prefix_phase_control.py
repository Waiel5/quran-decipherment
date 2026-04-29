#!/usr/bin/env python3
"""H-NEW-127.8 - phase-aware control for the coarse-prefix OQ-20 omnibus.

Observable:
  z_s = -gzip_z from the locked compression summary JSON

Primary test:
  Kruskal-Wallis H across coarse_prefix(sinai_genre)

Outer null:
  shuffle coarse-prefix labels only within neuwirth_phase blocks, preserving
  the observed coarse-prefix counts inside each phase block
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

PREREG_FILE = ROOT / "findings/phase-b-hypotheses/h-new-127-8-coarse-prefix-phase-aware-control-prereg.md"
COMPRESSION_JSON = ROOT / "findings/phase-b-hypotheses/csv/compression_self_ref_results.json"
GENRE_TSV = ROOT / "findings/classical-sources/neuwirth-sinai-genre-labels.tsv"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-127-8.json"


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
        phase = labels[sid]["neuwirth_phase"]
        if not sinai_label:
            raise RuntimeError(f"missing sinai_genre for surah {sid}")
        if not phase:
            raise RuntimeError(f"missing neuwirth_phase for surah {sid}")
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
                "phase": phase,
                "tier": labels[sid]["jurjani_predicted_asyndeton_tier"],
            }
        )

    if len(records) != 114:
        raise RuntimeError(f"expected 114 records, found {len(records)}")

    prefix_to_scores: dict[str, list[float]] = defaultdict(list)
    phase_to_counts: dict[str, Counter[str]] = defaultdict(Counter)
    phase_to_scores: dict[str, list[float]] = defaultdict(list)
    phase_blocks: dict[str, list[int]] = defaultdict(list)
    for idx, rec in enumerate(records):
        prefix = str(rec["coarse_prefix"])
        phase = str(rec["phase"])
        z_s = float(rec["z_s"])
        prefix_to_scores[prefix].append(z_s)
        phase_to_counts[phase][prefix] += 1
        phase_to_scores[phase].append(z_s)
        phase_blocks[phase].append(idx)

    prefixes_sorted = sorted(prefix_to_scores)
    groups = [prefix_to_scores[prefix] for prefix in prefixes_sorted]
    h_obs, df = kruskal_wallis(groups)

    prefix_labels = [str(rec["coarse_prefix"]) for rec in records]
    rng = random.Random(SEED)
    h_null = []
    n_ge = 0
    for _ in range(N_PERM):
        perm_labels = prefix_labels[:]
        for indices in phase_blocks.values():
            shuffled = [perm_labels[i] for i in indices]
            rng.shuffle(shuffled)
            for i, label in zip(indices, shuffled):
                perm_labels[i] = label
        perm_groups: dict[str, list[float]] = defaultdict(list)
        for rec, prefix in zip(records, perm_labels):
            perm_groups[prefix].append(float(rec["z_s"]))
        perm_h, _ = kruskal_wallis([perm_groups[prefix] for prefix in prefixes_sorted])
        h_null.append(perm_h)
        if perm_h >= h_obs:
            n_ge += 1

    h_null_sorted = sorted(h_null)
    null_mean = statistics.mean(h_null)
    null_sd = statistics.pstdev(h_null)
    z_vs_null = (h_obs - null_mean) / null_sd if null_sd > 0 else 0.0
    p_perm = (n_ge + 1) / (N_PERM + 1)
    verdict = "POSITIVE" if p_perm < ALPHA else "NULL"

    prefix_summary = []
    for prefix in prefixes_sorted:
        vals = prefix_to_scores[prefix]
        prefix_summary.append(
            {
                "coarse_prefix": prefix,
                "n": len(vals),
                "mean_z_s": statistics.mean(vals),
                "median_z_s": statistics.median(vals),
                "min_z_s": min(vals),
                "max_z_s": max(vals),
            }
        )
    prefix_summary.sort(key=lambda row: (row["median_z_s"], row["mean_z_s"], row["n"], row["coarse_prefix"]))

    phase_summary = []
    for phase in sorted(phase_to_counts):
        vals = phase_to_scores[phase]
        phase_summary.append(
            {
                "phase": phase,
                "n": len(vals),
                "coarse_prefixes_present": sorted(phase_to_counts[phase]),
                "n_coarse_prefixes_present": len(phase_to_counts[phase]),
                "mean_z_s": statistics.mean(vals),
                "median_z_s": statistics.median(vals),
            }
        )

    informative_phase_blocks = []
    frozen_phase_blocks = []
    for phase in sorted(phase_to_counts):
        row = {
            "phase": phase,
            "n": sum(phase_to_counts[phase].values()),
            "coarse_prefix_counts": {
                prefix: phase_to_counts[phase][prefix]
                for prefix in prefixes_sorted
                if phase_to_counts[phase][prefix] > 0
            },
        }
        if len(phase_to_counts[phase]) >= 2:
            informative_phase_blocks.append(row)
        else:
            frozen_phase_blocks.append(row)

    out = {
        "finding_id": "h-new-127-8",
        "title": "H-NEW-127.8 phase-aware control for the coarse-prefix OQ-20 omnibus",
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
            "note": "No manual pooling; coarse classes are generated mechanically from the locked labels exactly as in H-NEW-127.4.",
        },
        "control_axis": {
            "source_file": "findings/classical-sources/neuwirth-sinai-genre-labels.tsv",
            "field": "neuwirth_phase",
            "note": "Coarse-prefix labels are shuffled only within these phase blocks, preserving the observed coarse-prefix counts inside each phase.",
        },
        "rules_tuple": "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = coarse_prefix(sinai_genre); control axis = neuwirth_phase; Kruskal-Wallis H on raw z_s; outer null shuffles coarse-prefix labels only within phase blocks, preserving observed coarse-prefix counts inside each phase; 114 surahs)",
        "n_surahs": 114,
        "n_perm": N_PERM,
        "alpha": ALPHA,
        "n_coarse_classes": len(prefixes_sorted),
        "class_counts": {prefix: len(vals) for prefix, vals in prefix_to_scores.items()},
        "phase_control_diagnostics": {
            "n_phase_blocks": len(phase_blocks),
            "n_informative_phase_blocks": len(informative_phase_blocks),
            "n_frozen_phase_blocks": len(frozen_phase_blocks),
            "n_surahs_in_informative_phase_blocks": sum(item["n"] for item in informative_phase_blocks),
            "n_surahs_in_frozen_phase_blocks": sum(item["n"] for item in frozen_phase_blocks),
            "informative_phase_blocks": informative_phase_blocks,
            "frozen_phase_blocks": frozen_phase_blocks,
        },
        "primary_test": {
            "statistic": "Kruskal-Wallis H",
            "df": df,
            "observed_H": h_obs,
            "null_mean_H": null_mean,
            "null_sd_H": null_sd,
            "null_min_H": min(h_null),
            "null_max_H": max(h_null),
            "null_quantiles": {
                "q001": quantile(h_null_sorted, 0.001),
                "q005": quantile(h_null_sorted, 0.005),
                "q01": quantile(h_null_sorted, 0.01),
                "q025": quantile(h_null_sorted, 0.025),
                "q05": quantile(h_null_sorted, 0.05),
                "q50": quantile(h_null_sorted, 0.5),
                "q95": quantile(h_null_sorted, 0.95),
                "q99": quantile(h_null_sorted, 0.99),
                "q995": quantile(h_null_sorted, 0.995),
                "q999": quantile(h_null_sorted, 0.999),
            },
            "z_vs_null": z_vs_null,
            "n_perm_ge_obs": n_ge,
            "p_perm_upper": p_perm,
            "verdict": verdict,
        },
        "coarse_prefix_summary": prefix_summary,
        "phase_summary": phase_summary,
        "records": records,
    }
    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(
        json.dumps(
            {
                "verdict": verdict,
                "observed_H": h_obs,
                "df": df,
                "null_mean_H": null_mean,
                "null_sd_H": null_sd,
                "n_perm_ge_obs": n_ge,
                "p_perm_upper": p_perm,
                "n_phase_blocks": len(phase_blocks),
                "n_informative_phase_blocks": len(informative_phase_blocks),
                "n_surahs_in_informative_phase_blocks": sum(item["n"] for item in informative_phase_blocks),
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
