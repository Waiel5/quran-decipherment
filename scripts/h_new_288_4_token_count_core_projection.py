#!/usr/bin/env python3
"""H-NEW-288.4 - within-bin token-count projection into the residualized short-core."""

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

from scripts.h_new_288_1_q108_residualized_pool_medoid import (  # noqa: E402
    METRIC_FUNCS,
    PRIMARY_METRICS,
    build_residualized_probabilities,
    parse_qac_counts,
)


PREREG_FILE = (
    ROOT
    / "findings/phase-b-hypotheses/h-new-288-4-token-count-core-projection-prereg.md"
)
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-288-4.json"
DATE = "2026-04-19"

B = [1, 97, 105, 107, 109, 111, 113, 114]
K = [108, 106, 103, 112]


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

    counts, total_tokens, _ = parse_qac_counts()
    residual_prob, mean_tokens, effective_alpha = build_residualized_probabilities(
        counts, total_tokens
    )

    verse_counts = {}
    with open(ROOT / "data/hafs-verse-counts.tsv", encoding="utf-8") as handle:
        for line in handle:
            sid, n = line.rstrip("\n").split("\t")
            verse_counts[int(sid)] = int(n)

    token_vector = [total_tokens[sid] for sid in B]
    verse_vector = [verse_counts[sid] for sid in B]
    token_assignments = list(itertools.permutations(token_vector))
    verse_assignments = list(set(itertools.permutations(verse_vector)))

    per_metric = []
    token_rs = []
    verse_rs = []
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
                    "token_count": total_tokens[sid],
                    "verse_count": verse_counts[sid],
                    "mean_residualized_distance_to_core": mean_distance,
                    "residualized_core_closeness": closeness_value,
                }
            )
        r_tok = pearson(token_vector, closeness)
        r_verse = pearson(verse_vector, closeness)
        token_rs.append(r_tok)
        verse_rs.append(r_verse)
        closeness_vectors.append(closeness)
        per_metric.append(
            {
                "metric": metric_name,
                "r_token_obs": r_tok,
                "r_verse_obs_descriptive": r_verse,
                "per_surah": per_surah,
            }
        )

    t_tok_obs = statistics.mean(token_rs)
    token_null = []
    for assignment in token_assignments:
        rs = [pearson(list(assignment), closeness) for closeness in closeness_vectors]
        token_null.append(statistics.mean(rs))

    p_short = (1 + sum(1 for t in token_null if t <= t_tok_obs)) / (1 + len(token_null))
    rank_desc = 1 + sum(1 for t in token_null if t > t_tok_obs)
    rank_asc = 1 + sum(1 for t in token_null if t < t_tok_obs)
    verdict = "PASS-DIRECTED" if p_short < 0.05 else "NULL"

    t_verse_obs = statistics.mean(verse_rs)
    verse_null = []
    for assignment in verse_assignments:
        rs = [pearson(list(assignment), closeness) for closeness in closeness_vectors]
        verse_null.append(statistics.mean(rs))

    out = {
        "finding_id": "h-new-288-4",
        "title": "Within-bin token-count projection into the residualized Q108 short-core",
        "date": DATE,
        "pre_reg_sha256": prereg_sha,
        "parent_backdrop": ["h-new-288-1", "h-new-288-2", "h-new-288-3"],
        "rules_tuple": "(fixed H-NEW-273 5-7 verse side B = {Q1,Q97,Q105,Q107,Q109,Q111,Q113,Q114}; fixed H-NEW-288.1 residualized short-core K = {Q108,Q106,Q103,Q112}; residualized probability family reused exactly from H-NEW-288.1; primary metrics = Fisher-Rao, Jensen-Shannon, Euclidean L2, cosine-angle; token count N_tok(s) = total QAC STEM-root tokens from the same parse used by H-NEW-288.1; per metric core-closeness C_m(s) = -mean_{t in K} d_res,m(s,t); primary summary T_tok = mean_m Corr(N_tok, C_m) over B; exact null by permuting the observed token-count vector across B, yielding 8! = 40320 unique assignments; one-sided lower-tail for shorter-closer direction)",
        "fixed_sets": {"B": B, "K": K},
        "residualized_family_context": {
            "mean_surah_tokens": mean_tokens,
            "q108_effective_alpha_residualized": effective_alpha[108],
        },
        "token_counts": {sid: total_tokens[sid] for sid in B},
        "verse_counts": {sid: verse_counts[sid] for sid in B},
        "primary_metrics": PRIMARY_METRICS,
        "per_metric": per_metric,
        "primary_summary": {
            "t_tok_obs": t_tok_obs,
            "r_token_obs_per_metric": token_rs,
            "null_n_unique_assignments": len(token_assignments),
            "null_mean": statistics.mean(token_null),
            "null_min": min(token_null),
            "null_max": max(token_null),
            "rank_desc": rank_desc,
            "rank_asc": rank_asc,
            "p_short": p_short,
            "decision_rule": "PASS-DIRECTED iff p_short < 0.05",
        },
        "descriptive_verse_count_contrast": {
            "t_verse_obs": t_verse_obs,
            "r_verse_obs_per_metric": verse_rs,
            "null_n_unique_assignments": len(verse_assignments),
            "p_short": (1 + sum(1 for t in verse_null if t <= t_verse_obs)) / (1 + len(verse_null)),
        },
        "verdict": verdict,
    }

    OUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
