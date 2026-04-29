#!/usr/bin/env python3
"""H-NEW-288.3 - residualized short-core projection test."""

from __future__ import annotations

import hashlib
import itertools
import json
import statistics
import sys
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.h_new_273_q1_q108_twin_liturgical_anchor import (  # noqa: E402
    DIVINE_ROOTS,
    load_imperative_density,
    load_root_counts,
)
from scripts.h_new_288_1_q108_residualized_pool_medoid import (  # noqa: E402
    METRIC_FUNCS,
    PRIMARY_METRICS,
    build_residualized_probabilities,
    parse_qac_counts,
)


PREREG_FILE = (
    ROOT
    / "findings/phase-b-hypotheses/h-new-288-3-residualized-core-projection-prereg.md"
)
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-288-3.json"
DATE = "2026-04-19"

B = [1, 97, 105, 107, 109, 111, 113, 114]
K = [108, 106, 103, 112]


def divine_share(root_counts: dict[int, dict[str, int]], sid: int) -> float:
    counts = root_counts[sid]
    total = sum(counts.values())
    if total == 0:
        return 0.0
    divine = sum(counts.get(root, 0) for root in DIVINE_ROOTS)
    return divine / total


def pearson(xs: list[float], ys: list[float]) -> float:
    mx = statistics.mean(xs)
    my = statistics.mean(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    den = (
        sum((x - mx) ** 2 for x in xs) * sum((y - my) ** 2 for y in ys)
    ) ** 0.5
    return 0.0 if den == 0.0 else num / den


def main() -> int:
    prereg_sha = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()

    root_counts = load_root_counts()
    imperative_density = load_imperative_density()
    counts, total_tokens, _ = parse_qac_counts()
    residual_prob, mean_tokens, effective_alpha = build_residualized_probabilities(
        counts, total_tokens
    )

    score_map = {}
    for sid in B:
        d = divine_share(root_counts, sid)
        i = imperative_density[sid]
        score_map[sid] = (d * i) ** 0.5

    score_vector = [score_map[sid] for sid in B]
    unique_assignments = sorted(set(itertools.permutations(score_vector)))

    per_metric = []
    observed_rs = []
    closeness_vectors = []

    for metric_name in PRIMARY_METRICS:
        metric = METRIC_FUNCS[metric_name]
        closeness = []
        per_surah = []
        for sid in B:
            mean_distance = statistics.mean(
                metric(residual_prob[sid], residual_prob[tid]) for tid in K
            )
            closeness_value = -mean_distance
            closeness.append(closeness_value)
            per_surah.append(
                {
                    "surah": sid,
                    "h273_score": score_map[sid],
                    "mean_residualized_distance_to_core": mean_distance,
                    "residualized_core_closeness": closeness_value,
                }
            )
        r_obs = pearson(score_vector, closeness)
        observed_rs.append(r_obs)
        closeness_vectors.append(closeness)
        per_metric.append(
            {
                "metric": metric_name,
                "r_obs": r_obs,
                "per_surah": per_surah,
            }
        )

    t_obs = statistics.mean(observed_rs)
    null_t = []
    for assignment in unique_assignments:
        rs = [pearson(list(assignment), closeness) for closeness in closeness_vectors]
        null_t.append(statistics.mean(rs))

    p_same = (1 + sum(1 for t in null_t if t >= t_obs)) / (1 + len(null_t))
    p_comp = (1 + sum(1 for t in null_t if t <= t_obs)) / (1 + len(null_t))
    rank_desc = 1 + sum(1 for t in null_t if t > t_obs)
    rank_asc = 1 + sum(1 for t in null_t if t < t_obs)

    if p_same < 0.05:
        verdict = "PASS-SAME-MECHANISM"
    elif p_comp < 0.05:
        verdict = "PASS-COMPLEMENTARY"
    else:
        verdict = "NULL"

    out = {
        "finding_id": "h-new-288-3",
        "title": "Residualized short-core projection test for the H-NEW-273 speech-act score",
        "date": DATE,
        "pre_reg_sha256": prereg_sha,
        "parent_backdrop": ["h-new-273", "h-new-288-1", "h-new-288-2"],
        "rules_tuple": "(fixed H-NEW-273 5-7 verse Early-Meccan side B = {Q1,Q97,Q105,Q107,Q109,Q111,Q113,Q114}; fixed H-NEW-288.1 residualized short-core K = {Q108,Q106,Q103,Q112}; residualized probability family reused exactly from H-NEW-288.1; primary metrics = Fisher-Rao, Jensen-Shannon, Euclidean L2, cosine-angle; H-NEW-273 surah score reused exactly as S(s)=sqrt(divine_share_{Alh,rbb,rHm}(s) * imperative_density(s)); per metric core-closeness C_m(s) = -mean_{t in K} d_res,m(s,t); primary summary T_proj = mean_m Corr(S, C_m) over B; exact null by permuting the observed H-NEW-273 score multiset across B, yielding 8!/5! = 336 unique assignments; dual directional exact p_same and p_comp)",
        "fixed_sets": {
            "B": B,
            "K": K,
        },
        "residualized_family_context": {
            "mean_surah_tokens": mean_tokens,
            "q108_effective_alpha_residualized": effective_alpha[108],
        },
        "h273_score_map": score_map,
        "primary_metrics": PRIMARY_METRICS,
        "per_metric": per_metric,
        "summary": {
            "t_proj_obs": t_obs,
            "r_obs_per_metric": observed_rs,
            "null_n_unique_assignments": len(unique_assignments),
            "null_mean": statistics.mean(null_t),
            "null_min": min(null_t),
            "null_max": max(null_t),
            "rank_desc": rank_desc,
            "rank_asc": rank_asc,
            "p_same": p_same,
            "p_comp": p_comp,
            "decision_rule": "PASS-SAME-MECHANISM iff p_same < 0.05; PASS-COMPLEMENTARY iff p_comp < 0.05; NULL otherwise",
        },
        "verdict": verdict,
    }

    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
