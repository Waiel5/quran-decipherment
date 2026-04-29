#!/usr/bin/env python3
"""H-NEW-264 — Q 1 "connects everything" follow-up via ḥā-mīm subset test.

Conservative preregistered question:
Does al-Fātiḥa's QAC-STEM root profile connect ANOMALOUSLY to the
pre-specified ḥā-mīm block (Q 40-46), despite Q 1's known structural
isolation in the H-NEW-89 cluster-membership taxonomy?

Two inferential cells, same locked subset:
  A. Mean unweighted recall of Q 1 roots within Q 40-46.
  B. Mean IDF-weighted recall of Q 1 roots within Q 40-46.

Null for both cells:
  10,000 random 7-surah subsets preserving exact period composition and
  coarse verse-count bins of Q 40-46. This makes the test conservative
  against trivial Meccan-only and mid-length-only explanations.

MW-5 positive control:
  Q 62 root profile against the musabbiḥāt inner-5 {Q 57, 59, 61, 64}
  under the same matched-null logic.
"""
from __future__ import annotations

import csv
import hashlib
import json
import math
import random
import statistics
import sys
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
SEED = 20260420
N_PERM = 10_000
BON_K = 2
ALPHA_BON = 0.05 / BON_K

PREREG_FILE = (
    ROOT
    / "findings/phase-b-hypotheses/h-new-264-q1-connects-everything-prereg.md"
)
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-264.json"
ROOT_GRAPH = ROOT / "data/morphology/surah-root-graph.json"
CORPUS_FILE = ROOT / "quran-text/quran-no-tashkeel.json"
REVELATION_FILE = ROOT / "data/revelation-order.csv"

HAWAMIM = [40, 41, 42, 43, 44, 45, 46]
MW5_MUSABBIHAT = [57, 59, 61, 64]  # anchor Q 62 excluded by design


def length_bin(n_verses: int) -> str:
    if n_verses < 10:
        return "lt10"
    if n_verses < 30:
        return "10_29"
    if n_verses < 60:
        return "30_59"
    if n_verses < 100:
        return "60_99"
    return "100p"


def mean(values: list[float]) -> float:
    return statistics.mean(values) if values else 0.0


def stdev(values: list[float]) -> float:
    return statistics.stdev(values) if len(values) > 1 else 0.0


def p_upper(null_values: list[float], observed: float) -> float:
    ge = sum(1 for x in null_values if x >= observed)
    return (1 + ge) / (1 + len(null_values))


def z_score(observed: float, null_values: list[float]) -> float:
    sd = stdev(null_values)
    if sd == 0:
        return 0.0
    return (observed - mean(null_values)) / sd


def matched_null_samples(
    subset: list[int],
    anchor: int,
    metric_fn,
    period_by_surah: dict[int, str],
    length_bin_by_surah: dict[int, str],
    rng: random.Random,
) -> tuple[list[float], dict[str, int], dict[str, int]]:
    counts_by_bucket: dict[tuple[str, str], int] = {}
    for sid in subset:
        key = (period_by_surah[sid], length_bin_by_surah[sid])
        counts_by_bucket[key] = counts_by_bucket.get(key, 0) + 1

    pools: dict[tuple[str, str], list[int]] = {}
    for key in counts_by_bucket:
        pools[key] = [
            sid
            for sid in range(1, 115)
            if sid != anchor
            and sid not in subset
            and (period_by_surah[sid], length_bin_by_surah[sid]) == key
        ]
        if len(pools[key]) < counts_by_bucket[key]:
            raise ValueError(
                f"Insufficient pool for bucket {key}: "
                f"need {counts_by_bucket[key]}, have {len(pools[key])}"
            )

    null_values = []
    for _ in range(N_PERM):
        sample = []
        for key, need in counts_by_bucket.items():
            sample.extend(rng.sample(pools[key], need))
        null_values.append(mean([metric_fn(sid) for sid in sample]))

    counts_str = {
        f"{period}|{bucket}": count
        for (period, bucket), count in sorted(counts_by_bucket.items())
    }
    pools_str = {
        f"{period}|{bucket}": len(pool)
        for (period, bucket), pool in sorted(pools.items())
    }
    return null_values, counts_str, pools_str


def main() -> int:
    prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
    print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)

    root_payload = json.loads(ROOT_GRAPH.read_text(encoding="utf-8"))
    surah_root_counts = {
        int(sid): dict(counts) for sid, counts in root_payload["surahs"].items()
    }
    surah_root_sets = {sid: set(counts) for sid, counts in surah_root_counts.items()}
    assert len(surah_root_sets) == 114

    corpus = json.loads(CORPUS_FILE.read_text(encoding="utf-8"))
    verse_count = {surah["id"]: len(surah["verses"]) for surah in corpus}
    assert len(verse_count) == 114

    period_by_surah: dict[int, str] = {}
    for row in csv.DictReader(REVELATION_FILE.open(encoding="utf-8")):
        sid = int(row["mushaf_order"])
        period_by_surah[sid] = row["period"].strip()
    assert len(period_by_surah) == 114

    length_bin_by_surah = {sid: length_bin(n) for sid, n in verse_count.items()}

    # Corpus-wide document frequency for IDF.
    df: dict[str, int] = {}
    for roots in surah_root_sets.values():
        for root in roots:
            df[root] = df.get(root, 0) + 1
    idf = {root: math.log(114 / count) for root, count in df.items()}

    q1_roots = surah_root_sets[1]
    q1_root_weight_total = sum(idf[root] for root in q1_roots)
    assert q1_root_weight_total > 0

    def q1_recall(sid: int) -> float:
        return len(q1_roots & surah_root_sets[sid]) / len(q1_roots)

    def q1_idf_recall(sid: int) -> float:
        inter = q1_roots & surah_root_sets[sid]
        return sum(idf[root] for root in inter) / q1_root_weight_total

    rng = random.Random(SEED)

    cell_a_null, counts_a, pools_a = matched_null_samples(
        subset=HAWAMIM,
        anchor=1,
        metric_fn=q1_recall,
        period_by_surah=period_by_surah,
        length_bin_by_surah=length_bin_by_surah,
        rng=rng,
    )
    cell_b_null, counts_b, pools_b = matched_null_samples(
        subset=HAWAMIM,
        anchor=1,
        metric_fn=q1_idf_recall,
        period_by_surah=period_by_surah,
        length_bin_by_surah=length_bin_by_surah,
        rng=rng,
    )

    cell_a_obs = mean([q1_recall(sid) for sid in HAWAMIM])
    cell_b_obs = mean([q1_idf_recall(sid) for sid in HAWAMIM])
    cell_a_p = p_upper(cell_a_null, cell_a_obs)
    cell_b_p = p_upper(cell_b_null, cell_b_obs)
    cell_a_pass = cell_a_p < ALPHA_BON
    cell_b_pass = cell_b_p < ALPHA_BON

    # MW-5 positive control: Q 62 vs musabbiḥāt inner-5 under same null logic.
    q62_roots = surah_root_sets[62]
    q62_weight_total = sum(idf[root] for root in q62_roots)

    def q62_recall(sid: int) -> float:
        return len(q62_roots & surah_root_sets[sid]) / len(q62_roots)

    def q62_idf_recall(sid: int) -> float:
        inter = q62_roots & surah_root_sets[sid]
        return sum(idf[root] for root in inter) / q62_weight_total

    mw5_a_null, mw5_counts, mw5_pools = matched_null_samples(
        subset=MW5_MUSABBIHAT,
        anchor=62,
        metric_fn=q62_recall,
        period_by_surah=period_by_surah,
        length_bin_by_surah=length_bin_by_surah,
        rng=rng,
    )
    mw5_b_null, _, _ = matched_null_samples(
        subset=MW5_MUSABBIHAT,
        anchor=62,
        metric_fn=q62_idf_recall,
        period_by_surah=period_by_surah,
        length_bin_by_surah=length_bin_by_surah,
        rng=rng,
    )

    mw5_a_obs = mean([q62_recall(sid) for sid in MW5_MUSABBIHAT])
    mw5_b_obs = mean([q62_idf_recall(sid) for sid in MW5_MUSABBIHAT])
    mw5_a_p = p_upper(mw5_a_null, mw5_a_obs)
    mw5_b_p = p_upper(mw5_b_null, mw5_b_obs)
    mw5_pass = mw5_a_p < 0.05 and mw5_b_p < 0.05

    q1_shared_root_coverage = []
    for root in sorted(q1_roots):
        hits = [sid for sid in HAWAMIM if root in surah_root_sets[sid]]
        q1_shared_root_coverage.append(
            {
                "root": root,
                "hawamim_hits": hits,
                "n_hawamim_hits": len(hits),
                "idf": round(idf[root], 4),
            }
        )
    q1_shared_root_coverage.sort(
        key=lambda row: (-row["n_hawamim_hits"], -row["idf"], row["root"])
    )

    hawamim_rows = []
    for sid in HAWAMIM:
        inter = sorted(q1_roots & surah_root_sets[sid])
        hawamim_rows.append(
            {
                "surah": sid,
                "n_verses": verse_count[sid],
                "period": period_by_surah[sid],
                "length_bin": length_bin_by_surah[sid],
                "shared_q1_roots_n": len(inter),
                "shared_q1_roots": inter,
                "cell_a_recall": round(q1_recall(sid), 4),
                "cell_b_idf_recall": round(q1_idf_recall(sid), 4),
            }
        )

    if not mw5_pass:
        verdict = "INSTRUMENT-SUSPECT"
    elif cell_a_pass and cell_b_pass:
        verdict = "CONFIRMED"
    elif cell_a_pass and not cell_b_pass:
        verdict = "PARTIAL-UNWEIGHTED-ONLY"
    else:
        verdict = "FAIL"

    results = {
        "id": "H-NEW-264",
        "title": "Q 1 root-profile linkage to the ḥā-mīm subset",
        "date": "2026-04-18",
        "seed": SEED,
        "n_perm": N_PERM,
        "prereg_sha256": prereg_sha,
        "rules_tuple": (
            "QAC v0.4 STEM roots via surah-root-graph.json; "
            "subset fixed as Q40-46 ḥm muqaṭṭāʿat; "
            "null preserves exact period composition and coarse verse-count bins "
            "<10/10-29/30-59/60-99/100+; "
            "Hafs-Kūfan; basmala-counted-only-in-surah-1"
        ),
        "bonferroni": {
            "k": BON_K,
            "alpha_bon": ALPHA_BON,
            "family": "h-new-264-q1-connects-everything",
        },
        "subset_tested": {
            "label": "ḥā-mīm block",
            "members": HAWAMIM,
            "n": len(HAWAMIM),
            "matching_counts": counts_a,
            "matching_pool_sizes": pools_a,
        },
        "q1_profile": {
            "n_distinct_roots": len(q1_roots),
            "roots": sorted(q1_roots),
        },
        "cell_a_unweighted_recall": {
            "statistic": "mean_shared_q1_root_fraction",
            "direction": "one-sided upper",
            "observed": cell_a_obs,
            "null_mean": mean(cell_a_null),
            "null_median": statistics.median(cell_a_null),
            "null_sd": stdev(cell_a_null),
            "z": z_score(cell_a_obs, cell_a_null),
            "p_one_sided_upper": cell_a_p,
            "pass": cell_a_pass,
        },
        "cell_b_idf_recall": {
            "statistic": "mean_idf_weighted_shared_q1_root_fraction",
            "direction": "one-sided upper",
            "observed": cell_b_obs,
            "null_mean": mean(cell_b_null),
            "null_median": statistics.median(cell_b_null),
            "null_sd": stdev(cell_b_null),
            "z": z_score(cell_b_obs, cell_b_null),
            "p_one_sided_upper": cell_b_p,
            "pass": cell_b_pass,
        },
        "mw5_positive_control": {
            "anchor_surah": 62,
            "subset_label": "musabbiḥāt inner-5 excluding anchor",
            "subset_members": MW5_MUSABBIHAT,
            "matching_counts": mw5_counts,
            "matching_pool_sizes": mw5_pools,
            "cell_a_unweighted_recall": {
                "observed": mw5_a_obs,
                "null_mean": mean(mw5_a_null),
                "null_sd": stdev(mw5_a_null),
                "z": z_score(mw5_a_obs, mw5_a_null),
                "p_one_sided_upper": mw5_a_p,
            },
            "cell_b_idf_recall": {
                "observed": mw5_b_obs,
                "null_mean": mean(mw5_b_null),
                "null_sd": stdev(mw5_b_null),
                "z": z_score(mw5_b_obs, mw5_b_null),
                "p_one_sided_upper": mw5_b_p,
            },
            "pass": mw5_pass,
        },
        "hawamim_per_surah": hawamim_rows,
        "q1_root_coverage_within_hawamim": q1_shared_root_coverage,
        "verdict": verdict,
    }

    OUT_JSON.write_text(
        json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8"
    )

    print(
        f"Cell A recall: obs={cell_a_obs:.4f} null={mean(cell_a_null):.4f} "
        f"z={z_score(cell_a_obs, cell_a_null):.2f} p={cell_a_p:.4f}",
        file=sys.stderr,
    )
    print(
        f"Cell B IDF recall: obs={cell_b_obs:.4f} null={mean(cell_b_null):.4f} "
        f"z={z_score(cell_b_obs, cell_b_null):.2f} p={cell_b_p:.4f}",
        file=sys.stderr,
    )
    print(
        f"MW-5: recall p={mw5_a_p:.4f}, idf p={mw5_b_p:.4f} -> "
        f"{'PASS' if mw5_pass else 'FAIL'}",
        file=sys.stderr,
    )
    print(f"FINAL: {verdict}", file=sys.stderr)
    print(f"Wrote: {OUT_JSON}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
