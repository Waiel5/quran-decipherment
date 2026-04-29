#!/usr/bin/env python3
"""H-NEW-288.2 - Q1 liturgical-separation inside the residualized Q108 pool."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
import sys

ROOT = Path("/Users/grey/Downloads/quran")
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.h_new_273_q1_q108_twin_liturgical_anchor import (
    DIVINE_ROOTS,
    load_imperative_density,
    load_root_counts,
)
from scripts.h_new_288_1_q108_residualized_pool_medoid import (
    METRIC_FUNCS,
    PRIMARY_METRICS,
    Q108,
    build_literal_probabilities,
    build_residualized_probabilities,
    load_pool,
    parse_qac_counts,
)

PREREG_FILE = (
    ROOT
    / "findings/phase-b-hypotheses/h-new-288-2-q1-liturgical-separation-prereg.md"
)
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-288-2.json"
DATE = "2026-04-19"
TARGET = 1
CONTRAST = 112


def divine_share(root_counts: dict[int, dict[str, int]], sid: int) -> float:
    counts = root_counts[sid]
    total = sum(counts.values())
    if total == 0:
        return 0.0
    divine = sum(counts.get(root, 0) for root in DIVINE_ROOTS)
    return divine / total


def competition_rank_by_distance(values: dict[int, float], sid: int) -> int:
    target = values[sid]
    return 1 + sum(
        1
        for other, value in values.items()
        if other != sid and (value < target or (value == target and other < sid))
    )


def top_sorted_positive(rows: list[dict], key: str, n: int = 10) -> list[dict]:
    positive_rows = [row for row in rows if row[key] > 0]
    return sorted(positive_rows, key=lambda row: (-row[key], row["surah"]))[:n]


def main() -> int:
    prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()

    root_counts = load_root_counts()
    imperative_density = load_imperative_density()
    counts, total_tokens, _ = parse_qac_counts()
    literal_prob = build_literal_probabilities(counts, total_tokens)
    residual_prob, mean_tokens, effective_alpha = build_residualized_probabilities(
        counts, total_tokens
    )
    pool, verse_counts = load_pool()
    candidates = [sid for sid in pool if sid != Q108]

    per_candidate = {
        sid: {
            "surah": sid,
            "verse_count": verse_counts[sid],
            "h273_divine_share": divine_share(root_counts, sid),
            "h273_imperative_density": imperative_density[sid],
        }
        for sid in candidates
    }
    for sid in candidates:
        d = per_candidate[sid]["h273_divine_share"]
        i = per_candidate[sid]["h273_imperative_density"]
        per_candidate[sid]["h273_surah_score"] = (d * i) ** 0.5
        per_candidate[sid]["per_metric"] = {}

    for metric_name in PRIMARY_METRICS:
        metric = METRIC_FUNCS[metric_name]
        literal_dist = {
            sid: metric(literal_prob[Q108], literal_prob[sid]) for sid in candidates
        }
        residual_dist = {
            sid: metric(residual_prob[Q108], residual_prob[sid]) for sid in candidates
        }
        for sid in candidates:
            lit_rank = competition_rank_by_distance(literal_dist, sid)
            res_rank = competition_rank_by_distance(residual_dist, sid)
            per_candidate[sid]["per_metric"][metric_name] = {
                "literal_distance_to_q108": literal_dist[sid],
                "literal_rank_to_q108": lit_rank,
                "residualized_distance_to_q108": residual_dist[sid],
                "residualized_rank_to_q108": res_rank,
                "delta_rank_res_minus_lit": res_rank - lit_rank,
                "separates_under_residualized": res_rank > lit_rank,
                "approaches_under_residualized": res_rank < lit_rank,
            }

    candidate_rows = []
    for sid in candidates:
        metric_rows = per_candidate[sid]["per_metric"]
        c_sep = sum(
            1 for metric_name in PRIMARY_METRICS if metric_rows[metric_name]["separates_under_residualized"]
        )
        c_app = sum(
            1 for metric_name in PRIMARY_METRICS if metric_rows[metric_name]["approaches_under_residualized"]
        )
        delta_sum = sum(
            metric_rows[metric_name]["delta_rank_res_minus_lit"] for metric_name in PRIMARY_METRICS
        )
        score = per_candidate[sid]["h273_surah_score"]
        row = {
            "surah": sid,
            "verse_count": per_candidate[sid]["verse_count"],
            "h273_divine_share": per_candidate[sid]["h273_divine_share"],
            "h273_imperative_density": per_candidate[sid]["h273_imperative_density"],
            "h273_surah_score": score,
            "c_sep": c_sep,
            "c_app": c_app,
            "delta_rank_sum_res_minus_lit": delta_sum,
            "delta_rank_mean_res_minus_lit": delta_sum / len(PRIMARY_METRICS),
            "liturgical_separation_score": score * c_sep,
            "liturgical_approach_score": score * c_app,
            "per_metric": metric_rows,
        }
        candidate_rows.append(row)

    target_row = next(row for row in candidate_rows if row["surah"] == TARGET)
    contrast_row = next(row for row in candidate_rows if row["surah"] == CONTRAST)

    rank_desc = 1 + sum(
        1
        for row in candidate_rows
        if row["liturgical_separation_score"] > target_row["liturgical_separation_score"]
    )
    p_exact = (
        sum(
            1
            for row in candidate_rows
            if row["liturgical_separation_score"] >= target_row["liturgical_separation_score"]
        )
        / len(candidate_rows)
    )
    verdict = "PASS-DIRECTED" if p_exact < 0.05 else "NULL"

    approach_rank_desc = 1 + sum(
        1
        for row in candidate_rows
        if row["liturgical_approach_score"] > contrast_row["liturgical_approach_score"]
    )
    approach_p_exact = (
        sum(
            1
            for row in candidate_rows
            if row["liturgical_approach_score"] >= contrast_row["liturgical_approach_score"]
        )
        / len(candidate_rows)
    )

    out = {
        "finding_id": "h-new-288-2",
        "title": "Q1 liturgical-separation test inside the residualized Q108 pool",
        "date": DATE,
        "pre_reg_sha256": prereg_sha,
        "parent_backdrop": ["h-new-273", "h-new-288", "h-new-288-1"],
        "rules_tuple": "(fixed H-NEW-288.1 pool P = {Early Meccan surahs with verse_count <= 17}; candidate family = P \\\\ {Q108}; literal and residualized probability families reused exactly from H-NEW-288.1; primary metrics = Fisher-Rao, Jensen-Shannon, Euclidean L2, cosine-angle; H-NEW-273 surah score reused exactly as S(s)=sqrt(divine_share_{Alh,rbb,rHm}(s) * imperative_density(s)); for each candidate s and primary metric m, compute rank_lit^m(s) and rank_res^m(s) by ascending distance to Q108 inside P \\\\ {Q108}; define C_sep(s)=#{m : rank_res^m(s) > rank_lit^m(s)} and L_sep(s)=S(s) * C_sep(s); exact candidate-family upper-tail over the 21 admissible surahs)",
        "pool_definition": {
            "pool_surahs": pool,
            "candidate_family_excluding_q108": candidates,
            "pool_size": len(pool),
            "candidate_family_size": len(candidates),
        },
        "family_reuse": {
            "literal_family": "count / N_i plus flat alpha=0.5",
            "residualized_family": "raw counts plus alpha_i = 0.5 * mean_tokens / N_i",
            "mean_surah_tokens": mean_tokens,
            "q108_effective_alpha_residualized": effective_alpha[Q108],
        },
        "primary_metrics": PRIMARY_METRICS,
        "primary_target": {
            "surah": TARGET,
            "h273_surah_score": target_row["h273_surah_score"],
            "c_sep": target_row["c_sep"],
            "liturgical_separation_score": target_row["liturgical_separation_score"],
            "rank_desc": rank_desc,
            "p_exact_upper": p_exact,
            "decision_rule": "PASS-DIRECTED iff p_exact_upper < 0.05",
        },
        "descriptive_contrast": {
            "surah": CONTRAST,
            "h273_surah_score": contrast_row["h273_surah_score"],
            "c_app": contrast_row["c_app"],
            "liturgical_approach_score": contrast_row["liturgical_approach_score"],
            "rank_desc": approach_rank_desc,
            "p_exact_upper": approach_p_exact,
            "note": "Descriptive only. This was not a second inferential cell.",
        },
        "candidate_rows": sorted(
            candidate_rows,
            key=lambda row: (-row["liturgical_separation_score"], row["surah"]),
        ),
        "top_liturgical_separation_candidates": top_sorted_positive(
            candidate_rows, "liturgical_separation_score"
        ),
        "top_liturgical_approach_candidates": top_sorted_positive(
            candidate_rows, "liturgical_approach_score"
        ),
        "verdict": verdict,
        "verdict_note": (
            "Q1 is tested as a directed inherited target, not as a discovery-clean "
            "new candidate. The candidate family is exact and small, so the minimum "
            "attainable upper-tail is 1/21."
        ),
    }

    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
