#!/usr/bin/env python3
"""H-NEW-277 — Hijra lexical frontier broad-root ablation.

Child follow-up to H-NEW-267. Re-runs the exact same frontier instrument
after removing the five broadest absolute density-shift roots from the
published H-NEW-267 descriptive table:
  Alh, Amn, qwl, rbb, Ayy
"""
from __future__ import annotations

import csv
import hashlib
import json
import random
import sys
from pathlib import Path

import numpy as np

ROOT = Path("/Users/grey/Downloads/quran")
ROOT_GRAPH = ROOT / "data/morphology/surah-root-graph.json"
CHRONOLOGY_CSV = ROOT / "data/revelation-order.csv"
PREREG_FILE = (
    ROOT
    / "findings/phase-b-hypotheses/h-new-277-hijra-frontier-broad-root-ablation-prereg.md"
)
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-277.json"

SEED = 20260418
N_PERMS = 3000
MW5_N_PERMS = 1000
BONFERRONI_K = 3
ALPHA_BON = 0.05 / BONFERRONI_K
DIRICHLET_ALPHA = 0.5
MIN_COMBINED_TOKENS = 10
MIN_SURAHS_PER_SIDE = 2
EXCLUDED_ROOTS = ["Alh", "Amn", "qwl", "rbb", "Ayy"]

PHASE_ORDER = ["Early Meccan", "Middle Meccan", "Late Meccan", "Medinan"]


def round_float(value: float, digits: int = 6) -> float:
    return round(float(value), digits)


def average_ranks(values: np.ndarray) -> np.ndarray:
    order = np.argsort(values, kind="mergesort")
    ranks = np.empty(len(values), dtype=np.float64)
    i = 0
    while i < len(values):
        j = i
        while j + 1 < len(values) and values[order[j + 1]] == values[order[i]]:
            j += 1
        rank = (i + j) / 2.0 + 1.0
        ranks[order[i : j + 1]] = rank
        i = j + 1
    return ranks


def spearman_rho(x: np.ndarray, y: np.ndarray) -> float:
    if len(x) != len(y):
        raise ValueError("Spearman inputs must have the same length.")
    if len(x) < 2:
        return 0.0
    rx = average_ranks(np.asarray(x, dtype=np.float64))
    ry = average_ranks(np.asarray(y, dtype=np.float64))
    rx -= rx.mean()
    ry -= ry.mean()
    denom = float(np.sqrt((rx * rx).sum() * (ry * ry).sum()))
    if denom == 0.0:
        return 0.0
    return float((rx * ry).sum() / denom)


def auc_from_group_scores(pos_scores: np.ndarray, neg_scores: np.ndarray) -> float:
    wins = 0.0
    for score in pos_scores:
        wins += float((neg_scores < score).sum())
        wins += 0.5 * float((neg_scores == score).sum())
    return wins / (len(pos_scores) * len(neg_scores))


def empirical_p_upper(null_values: np.ndarray, observed: float) -> float:
    return (1.0 + float((null_values >= observed).sum())) / (len(null_values) + 1.0)


def load_root_matrices() -> tuple[list[str], np.ndarray, np.ndarray, np.ndarray]:
    payload = json.loads(ROOT_GRAPH.read_text(encoding="utf-8"))
    root_names = sorted(root for root in payload["roots"].keys() if root not in EXCLUDED_ROOTS)
    root_to_idx = {root: idx for idx, root in enumerate(root_names)}

    counts = np.zeros((114, len(root_names)), dtype=np.int64)
    rooted_tokens = np.zeros(114, dtype=np.int64)

    for sid in range(1, 115):
        root_counts = payload["surahs"][str(sid)]
        total = 0
        for root, count in root_counts.items():
            if root in root_to_idx:
                counts[sid - 1, root_to_idx[root]] = int(count)
                total += int(count)
        rooted_tokens[sid - 1] = total

    if np.any(rooted_tokens == 0):
        raise RuntimeError("Encountered surah with zero rooted tokens after ablation.")

    densities = counts / rooted_tokens[:, None]
    return root_names, counts, densities, rooted_tokens


def load_chronology() -> tuple[list[dict], dict[int, str], dict[int, str], dict[int, int]]:
    rows: list[dict] = []
    phase_by_sid: dict[int, str] = {}
    period_by_sid: dict[int, str] = {}
    rank_by_sid: dict[int, int] = {}

    with CHRONOLOGY_CSV.open(encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            sid = int(row["mushaf_order"])
            phase = row["noldeke_phase"].strip()
            period = row["period"].strip()
            rank = int(row["noldeke_order"])
            rows.append({"sid": sid, "phase": phase, "period": period, "rank": rank})
            phase_by_sid[sid] = phase
            period_by_sid[sid] = period
            rank_by_sid[sid] = rank

    rows.sort(key=lambda item: item["rank"])
    return rows, phase_by_sid, period_by_sid, rank_by_sid


def alternate_split(surah_ids: list[int], rank_by_sid: dict[int, int]) -> tuple[list[int], list[int]]:
    ordered = sorted(surah_ids, key=rank_by_sid.__getitem__)
    return ordered[::2], ordered[1::2]


def log_odds_weights(later_ids: list[int], earlier_ids: list[int], counts: np.ndarray) -> np.ndarray:
    later_counts = counts[np.array(later_ids, dtype=np.int64) - 1].sum(axis=0).astype(np.float64)
    earlier_counts = counts[np.array(earlier_ids, dtype=np.int64) - 1].sum(axis=0).astype(np.float64)
    n_roots = counts.shape[1]

    later_probs = (later_counts + DIRICHLET_ALPHA) / (
        later_counts.sum() + DIRICHLET_ALPHA * n_roots
    )
    earlier_probs = (earlier_counts + DIRICHLET_ALPHA) / (
        earlier_counts.sum() + DIRICHLET_ALPHA * n_roots
    )
    return np.log(later_probs / earlier_probs)


def support_mask(earlier_ids: list[int], later_ids: list[int], counts: np.ndarray) -> np.ndarray:
    earlier = counts[np.array(earlier_ids, dtype=np.int64) - 1]
    later = counts[np.array(later_ids, dtype=np.int64) - 1]
    pooled_tokens = earlier.sum(axis=0) + later.sum(axis=0)
    earlier_presence = (earlier > 0).sum(axis=0)
    later_presence = (later > 0).sum(axis=0)
    return (
        (pooled_tokens >= MIN_COMBINED_TOKENS)
        & (earlier_presence >= MIN_SURAHS_PER_SIDE)
        & (later_presence >= MIN_SURAHS_PER_SIDE)
    )


def score_surahs(surah_ids: list[int], densities: np.ndarray, weights: np.ndarray) -> np.ndarray:
    return np.array(
        [float(np.dot(densities[sid - 1], weights)) for sid in surah_ids],
        dtype=np.float64,
    )


def boundary_stats(
    earlier_ids: list[int],
    later_ids: list[int],
    counts: np.ndarray,
    densities: np.ndarray,
    rank_by_sid: dict[int, int],
) -> dict:
    earlier_a, earlier_b = alternate_split(earlier_ids, rank_by_sid)
    later_a, later_b = alternate_split(later_ids, rank_by_sid)

    weights_ab = log_odds_weights(later_a, earlier_a, counts)
    pos_scores_ab = score_surahs(later_b, densities, weights_ab)
    neg_scores_ab = score_surahs(earlier_b, densities, weights_ab)
    auc_ab = auc_from_group_scores(pos_scores_ab, neg_scores_ab)

    weights_ba = log_odds_weights(later_b, earlier_b, counts)
    pos_scores_ba = score_surahs(later_a, densities, weights_ba)
    neg_scores_ba = score_surahs(earlier_a, densities, weights_ba)
    auc_ba = auc_from_group_scores(pos_scores_ba, neg_scores_ba)

    mask = support_mask(earlier_ids, later_ids, counts)
    rho = spearman_rho(weights_ab[mask], weights_ba[mask])

    return {
        "auc_ab": float(auc_ab),
        "auc_ba": float(auc_ba),
        "rho": float(rho),
        "support_n": int(mask.sum()),
        "weights_ab": weights_ab,
        "weights_ba": weights_ba,
        "full_weights": log_odds_weights(later_ids, earlier_ids, counts),
        "support_mask": mask,
        "splits": {
            "earlier_a": earlier_a,
            "earlier_b": earlier_b,
            "later_a": later_a,
            "later_b": later_b,
        },
        "held_out_scores_ab": {
            "later": pos_scores_ab,
            "earlier": neg_scores_ab,
            "gap": float(pos_scores_ab.min() - neg_scores_ab.max()),
        },
        "held_out_scores_ba": {
            "later": pos_scores_ba,
            "earlier": neg_scores_ba,
            "gap": float(pos_scores_ba.min() - neg_scores_ba.max()),
        },
    }


def run_permutation_null(
    pool_ids: list[int],
    earlier_count: int,
    later_count: int,
    counts: np.ndarray,
    densities: np.ndarray,
    rank_by_sid: dict[int, int],
    n_perms: int,
    seed: int,
    label_names: tuple[str, str],
) -> np.ndarray:
    rng = random.Random(seed)
    labels = [label_names[0]] * earlier_count + [label_names[1]] * later_count
    null_values = np.zeros((n_perms, 3), dtype=np.float64)

    for perm_ix in range(n_perms):
        rng.shuffle(labels)
        earlier_ids = [sid for sid, lab in zip(pool_ids, labels, strict=True) if lab == label_names[0]]
        later_ids = [sid for sid, lab in zip(pool_ids, labels, strict=True) if lab == label_names[1]]
        stats = boundary_stats(earlier_ids, later_ids, counts, densities, rank_by_sid)
        null_values[perm_ix, 0] = stats["auc_ab"]
        null_values[perm_ix, 1] = stats["auc_ba"]
        null_values[perm_ix, 2] = stats["rho"]

        if (perm_ix + 1) % 500 == 0 or perm_ix == 0:
            print(
                f"  perm {perm_ix + 1}/{n_perms} "
                f"mean_auc_ab={null_values[: perm_ix + 1, 0].mean():.6f} "
                f"mean_rho={null_values[: perm_ix + 1, 2].mean():.6f}",
                file=sys.stderr,
            )

    return null_values


def summarize_cells(observed: np.ndarray, null_values: np.ndarray) -> dict[str, dict]:
    names = ["train_a_test_b_auc", "train_b_test_a_auc", "split_weight_rho"]
    summaries = {}
    q95 = np.quantile(null_values, 0.95, axis=0)
    p_values = np.array(
        [empirical_p_upper(null_values[:, idx], observed[idx]) for idx in range(len(names))],
        dtype=np.float64,
    )
    passes = (observed > q95) & (p_values < ALPHA_BON)

    for idx, name in enumerate(names):
        summaries[name] = {
            "observed": round_float(observed[idx]),
            "null_mean": round_float(null_values[:, idx].mean()),
            "null_sd": round_float(null_values[:, idx].std(ddof=1)),
            "null_q95": round_float(q95[idx]),
            "p_perm_upper": round_float(p_values[idx], 6),
            "pass": bool(passes[idx]),
        }
    return summaries


def main() -> None:
    prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()
    print(f"prereg SHA-256: {prereg_sha}", file=sys.stderr)

    root_names, counts, densities, rooted_tokens = load_root_matrices()
    chronology_rows, _, period_by_sid, rank_by_sid = load_chronology()

    phase_groups = {
        phase: [row["sid"] for row in chronology_rows if row["phase"] == phase]
        for phase in PHASE_ORDER
    }
    period_groups = {
        "Meccan": [row["sid"] for row in chronology_rows if period_by_sid[row["sid"]] == "Meccan"],
        "Medinan": [row["sid"] for row in chronology_rows if period_by_sid[row["sid"]] == "Medinan"],
    }

    print(
        f"Loaded {len(root_names)} ablated roots; rooted-token total={int(rooted_tokens.sum())}; "
        f"excluded={','.join(EXCLUDED_ROOTS)}",
        file=sys.stderr,
    )

    observed_stats = boundary_stats(
        earlier_ids=phase_groups["Late Meccan"],
        later_ids=phase_groups["Medinan"],
        counts=counts,
        densities=densities,
        rank_by_sid=rank_by_sid,
    )
    observed_cells = np.array(
        [observed_stats["auc_ab"], observed_stats["auc_ba"], observed_stats["rho"]],
        dtype=np.float64,
    )

    primary_pool = sorted(
        phase_groups["Late Meccan"] + phase_groups["Medinan"],
        key=rank_by_sid.__getitem__,
    )
    print("[1/3] Primary permutation null...", file=sys.stderr)
    primary_null = run_permutation_null(
        pool_ids=primary_pool,
        earlier_count=len(phase_groups["Late Meccan"]),
        later_count=len(phase_groups["Medinan"]),
        counts=counts,
        densities=densities,
        rank_by_sid=rank_by_sid,
        n_perms=N_PERMS,
        seed=SEED,
        label_names=("Late Meccan", "Medinan"),
    )

    print("[2/3] MW-5 permutation null...", file=sys.stderr)
    mw5_stats = boundary_stats(
        earlier_ids=period_groups["Meccan"],
        later_ids=period_groups["Medinan"],
        counts=counts,
        densities=densities,
        rank_by_sid=rank_by_sid,
    )
    mw5_observed = np.array(
        [mw5_stats["auc_ab"], mw5_stats["auc_ba"], mw5_stats["rho"]],
        dtype=np.float64,
    )
    mw5_pool = sorted(period_groups["Meccan"] + period_groups["Medinan"], key=rank_by_sid.__getitem__)
    mw5_null = run_permutation_null(
        pool_ids=mw5_pool,
        earlier_count=len(period_groups["Meccan"]),
        later_count=len(period_groups["Medinan"]),
        counts=counts,
        densities=densities,
        rank_by_sid=rank_by_sid,
        n_perms=MW5_N_PERMS,
        seed=SEED + 1,
        label_names=("Meccan", "Medinan"),
    )

    primary_cells = summarize_cells(observed_cells, primary_null)
    mw5_cells = summarize_cells(mw5_observed, mw5_null)
    mw5_pass = all(cell["pass"] for cell in mw5_cells.values())
    n_primary_pass = sum(int(cell["pass"]) for cell in primary_cells.values())

    if not mw5_pass:
        verdict = "NULL-BROKEN"
    elif n_primary_pass == BONFERRONI_K:
        verdict = "PASS-DIRECTED"
    elif n_primary_pass > 0:
        verdict = "MIXED"
    else:
        verdict = "NULL"

    payload = {
        "id": "h-new-277",
        "title": "Hijra lexical frontier broad-root ablation",
        "date": "2026-04-18",
        "seed": SEED,
        "prereg": str(PREREG_FILE.relative_to(ROOT)),
        "prereg_sha256": prereg_sha,
        "bonferroni_family": "h-new-277-hijra-frontier-broad-root-ablation",
        "bonferroni_k": BONFERRONI_K,
        "alpha_bon": ALPHA_BON,
        "n_perms": N_PERMS,
        "mw5_n_perms": MW5_N_PERMS,
        "excluded_roots": EXCLUDED_ROOTS,
        "excluded_root_count": len(EXCLUDED_ROOTS),
        "remaining_root_count": len(root_names),
        "remaining_rooted_tokens_total": int(rooted_tokens.sum()),
        "rules_tuple": (
            "H-NEW-267 scorer + split rule + nulls, but with fixed exclusion "
            "of {Alh, Amn, qwl, rbb, Ayy} from the root space"
        ),
        "primary": {
            "cells": primary_cells,
            "support_n": int(observed_stats["support_n"]),
            "held_out_score_gaps": {
                "train_a_test_b_gap": round_float(observed_stats["held_out_scores_ab"]["gap"]),
                "train_b_test_a_gap": round_float(observed_stats["held_out_scores_ba"]["gap"]),
            },
        },
        "mw5": {
            "cells": mw5_cells,
            "pass": mw5_pass,
        },
        "verdict": verdict,
    }
    OUT_JSON.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {OUT_JSON}", file=sys.stderr)
    print(f"verdict: {verdict}", file=sys.stderr)


if __name__ == "__main__":
    main()
