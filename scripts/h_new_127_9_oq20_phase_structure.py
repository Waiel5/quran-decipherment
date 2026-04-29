#!/usr/bin/env python3
"""H-NEW-127.9 - direct phase-structure test for locked compression z-scores.

Observable:
  z_s = -gzip_z from the locked compression summary JSON

Primary test:
  Kruskal-Wallis H across the exact locked neuwirth_phase labels

Outer null:
  shuffle phase labels across surahs, preserving class counts, and recompute H
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

PREREG_FILE = ROOT / "findings/phase-b-hypotheses/h-new-127-9-phase-structure-prereg.md"
COMPRESSION_JSON = ROOT / "findings/phase-b-hypotheses/csv/compression_self_ref_results.json"
GENRE_TSV = ROOT / "findings/classical-sources/neuwirth-sinai-genre-labels.tsv"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-127-9.json"


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
                "phase": phase,
                "sinai_genre": labels[sid]["sinai_genre"],
                "neuwirth_genre": labels[sid]["neuwirth_genre"],
                "tier": labels[sid]["jurjani_predicted_asyndeton_tier"],
            }
        )

    if len(records) != 114:
        raise RuntimeError(f"expected 114 records, found {len(records)}")

    phase_to_scores: dict[str, list[float]] = defaultdict(list)
    for rec in records:
        phase_to_scores[str(rec["phase"])].append(float(rec["z_s"]))

    phases_sorted = sorted(phase_to_scores, key=phase_sort_key)
    groups = [phase_to_scores[phase] for phase in phases_sorted]
    h_obs, df = kruskal_wallis(groups)

    phase_sequence = [str(rec["phase"]) for rec in records]
    z_values = [float(rec["z_s"]) for rec in records]
    rng = random.Random(SEED)
    h_null = []
    n_ge = 0
    for _ in range(N_PERM):
        perm_labels = phase_sequence[:]
        rng.shuffle(perm_labels)
        perm_groups: dict[str, list[float]] = defaultdict(list)
        for z_val, phase in zip(z_values, perm_labels):
            perm_groups[phase].append(z_val)
        perm_h, _ = kruskal_wallis([perm_groups[phase] for phase in phases_sorted])
        h_null.append(perm_h)
        if perm_h >= h_obs:
            n_ge += 1

    h_null_sorted = sorted(h_null)
    null_mean = statistics.mean(h_null)
    null_sd = statistics.pstdev(h_null)
    z_vs_null = (h_obs - null_mean) / null_sd if null_sd > 0 else 0.0
    p_perm = (n_ge + 1) / (N_PERM + 1)
    verdict = "POSITIVE" if p_perm < ALPHA else "NULL"

    phase_summary = []
    for phase in phases_sorted:
        vals = phase_to_scores[phase]
        phase_summary.append(
            {
                "phase": phase,
                "n": len(vals),
                "mean_z_s": statistics.mean(vals),
                "median_z_s": statistics.median(vals),
                "min_z_s": min(vals),
                "max_z_s": max(vals),
            }
        )

    out = {
        "finding_id": "h-new-127-9",
        "title": "H-NEW-127.9 direct phase-structure test for locked per-surah compression z-scores",
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
            "field": "neuwirth_phase",
            "note": "The exact locked phase labels are used as-is, including singleton disputed labels.",
        },
        "rules_tuple": "(no-tashkeel; locked per-surah compression z-scores from the repository-computed gzip null; primary label axis = neuwirth_phase; Kruskal-Wallis H; outer null permutes phase labels across surahs preserving class counts; 114 surahs)",
        "n_surahs": 114,
        "n_perm": N_PERM,
        "alpha": ALPHA,
        "n_phases": len(phases_sorted),
        "class_counts": {phase: len(phase_to_scores[phase]) for phase in phases_sorted},
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
                "q50": quantile(h_null_sorted, 0.50),
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
        "phase_summary": phase_summary,
        "surah_rows": records,
        "verdict": verdict,
    }

    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {OUT_JSON}", file=sys.stderr)
    print(json.dumps(out["primary_test"], indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
