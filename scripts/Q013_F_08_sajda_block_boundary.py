#!/usr/bin/env python3
"""
Q013-F-08 — Q 13:15 sajda-verse as within-surah block-boundary.

Pre-reg: /Users/grey/Downloads/quran/surahs/Q013-al-rad/Q013-F-08-sajda-block-boundary-prereg.md
SHA256:  bd7b8b34f7d3c35fb09ea7018afa37d0d07cb434aa607d2b41a46fb34f7225a4

Method: compute cosine-distance on TF-vectors of orthographic tokens between half-windows
adjacent to each internal verse-boundary in Q 13, then report sajda-boundary percentile.

Direction LOCKED: d_15 (boundary at v15→v16) ≥ 95th percentile of all 42 boundaries;
                  rank(d_15) ≤ 5.
"""

from __future__ import annotations
import hashlib
import json
import math
import sys
from collections import Counter
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "surahs/Q013-al-rad/Q013-F-08-sajda-block-boundary-prereg.md"
EXPECTED_SHA = "bd7b8b34f7d3c35fb09ea7018afa37d0d07cb434aa607d2b41a46fb34f7225a4"
OUT = ROOT / "surahs/Q013-al-rad/csv/Q013-F-08.json"


def sha_verify():
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FATAL: SHA mismatch.\n  expected: {EXPECTED_SHA}\n  actual:   {actual}", file=sys.stderr)
        sys.exit(1)
    return actual


def tf_vec(tokens):
    return Counter(tokens)


def cosine_distance(a: Counter, b: Counter) -> float:
    if not a or not b:
        return 1.0
    common = set(a) | set(b)
    dot = sum(a[k] * b[k] for k in common)
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    if na == 0 or nb == 0:
        return 1.0
    return 1.0 - dot / (na * nb)


def boundary_distance(verses_tokens, i, win_left=3, win_right=3):
    """Boundary between verse_i and verse_{i+1}. Indices 0-based; i ranges 0..n-2.
       Half-window includes win_left verses on the left (ending at i) and win_right on the right (starting at i+1).
       Truncated at surah edges."""
    n = len(verses_tokens)
    left_start = max(0, i - win_left + 1)
    right_end = min(n, i + 1 + win_right)
    left_tokens = []
    for j in range(left_start, i + 1):
        left_tokens.extend(verses_tokens[j])
    right_tokens = []
    for j in range(i + 1, right_end):
        right_tokens.extend(verses_tokens[j])
    return cosine_distance(tf_vec(left_tokens), tf_vec(right_tokens))


# 14 canonical sajda-verses (al-Bukhārī Kitāb sujūd al-Qurʾān standard).
SAJDA_14 = [(7, 206), (13, 15), (16, 50), (17, 109), (19, 58), (22, 18),
            (25, 60), (27, 26), (32, 15), (38, 24), (41, 38), (53, 62),
            (84, 21), (96, 19)]


def main():
    sha_actual = sha_verify()
    with (ROOT / "quran-text/quran-no-tashkeel.json").open(encoding="utf-8") as f:
        q = json.load(f)

    # Q 13
    q13_verses = [v["text"].split() for v in q[12]["verses"]]
    n13 = len(q13_verses)
    assert n13 == 43

    # All 42 internal boundaries with symmetric 3-verse half-windows
    boundary_dists = []
    for i in range(n13 - 1):  # boundary between v_{i+1} and v_{i+2} (1-based)
        d = boundary_distance(q13_verses, i, win_left=3, win_right=3)
        boundary_dists.append({"after_verse": i + 1, "distance": d})

    # Cell A: sajda is at v15→v16 → boundary index i where verse i+1 = 15 → i = 14 (0-based)
    sajda_idx = 14
    d_sajda = boundary_dists[sajda_idx]["distance"]
    sorted_desc = sorted(boundary_dists, key=lambda r: -r["distance"])
    percentile_d_sajda = 1.0 - (sum(1 for r in boundary_dists if r["distance"] > d_sajda) / len(boundary_dists))
    rank_d_sajda = next(i for i, r in enumerate(sorted_desc) if r["after_verse"] == sajda_idx + 1) + 1

    pass_a = percentile_d_sajda >= 0.95
    pass_b = rank_d_sajda <= 5

    # Cell A variant — asymmetric half-windows per pre-reg (left 4, right 3, where left includes sajda-verse)
    d_sajda_asymmetric = boundary_distance(q13_verses, sajda_idx, win_left=4, win_right=3)
    boundary_dists_asym = []
    for i in range(n13 - 1):
        d = boundary_distance(q13_verses, i, win_left=4, win_right=3)
        boundary_dists_asym.append({"after_verse": i + 1, "distance": d})
    sorted_desc_asym = sorted(boundary_dists_asym, key=lambda r: -r["distance"])
    rank_d_sajda_asym = next(i for i, r in enumerate(sorted_desc_asym) if r["after_verse"] == sajda_idx + 1) + 1
    percentile_d_sajda_asym = 1.0 - (sum(1 for r in boundary_dists_asym if r["distance"] > d_sajda_asymmetric) / len(boundary_dists_asym))

    # Cell C — 14-sajda corpus replication
    cellC = []
    for s, v in SAJDA_14:
        verses_s = [vv["text"].split() for vv in q[s - 1]["verses"]]
        n_s = len(verses_s)
        if v > n_s - 1:
            # sajda is the final verse (Q 96:19); no boundary "after" exists
            cellC.append({"surah": s, "verse": v, "skipped_reason": "sajda is final verse", "n_verses": n_s})
            continue
        bnd_idx = v - 1  # 0-based boundary "after verse v"
        d_v = boundary_distance(verses_s, bnd_idx, win_left=3, win_right=3)
        all_d = [boundary_distance(verses_s, i, win_left=3, win_right=3) for i in range(n_s - 1)]
        pct = 1.0 - (sum(1 for x in all_d if x > d_v) / len(all_d))
        rnk = sorted(all_d, reverse=True).index(d_v) + 1
        cellC.append({
            "surah": s, "verse": v, "n_verses": n_s,
            "d_sajda": d_v,
            "percentile_within_surah": pct,
            "rank_within_surah_desc": rnk,
            "top5_threshold_passed": rnk <= 5,
        })

    n_cellC_valid = sum(1 for r in cellC if "d_sajda" in r)
    n_cellC_top5 = sum(1 for r in cellC if r.get("top5_threshold_passed"))
    n_cellC_above_95pct = sum(1 for r in cellC if r.get("percentile_within_surah", 0) >= 0.95)

    if pass_a and pass_b:
        verdict = "PASS-DIRECTED (Cell A 95th-pct + Cell B top-5 both met)"
    elif pass_b:
        verdict = "PARTIAL — Cell B rank-5 met; Cell A 95th-pct not met"
    elif pass_a:
        verdict = "PARTIAL — Cell A 95th-pct met; Cell B rank-5 not met"
    else:
        verdict = "NULL — DIRECTION REVERSED on primary symmetric-window test"

    out = {
        "test_id": "Q013-F-08",
        "title": "Q 13:15 sajda-verse as within-surah block-boundary",
        "prereg_sha_expected": EXPECTED_SHA,
        "prereg_sha_actual": sha_actual,
        "seed": 20260509,
        "alpha_bon": 0.025,
        "instrument": "cosine-distance on TF-vectors of orthographic tokens (no-tashkeel)",
        "cell_A_symmetric_window_3_3": {
            "d_sajda": d_sajda,
            "percentile_within_surah": percentile_d_sajda,
            "threshold_95pct": 0.95,
            "pass_direction": pass_a,
            "all_42_boundary_distances": boundary_dists,
        },
        "cell_A_variant_asymmetric_4_3": {
            "d_sajda": d_sajda_asymmetric,
            "percentile_within_surah": percentile_d_sajda_asym,
            "rank_within_surah_desc": rank_d_sajda_asym,
            "all_42_boundary_distances": boundary_dists_asym,
        },
        "cell_B_within_surah_rank": {
            "rank_d_sajda_desc": rank_d_sajda,
            "threshold_top_5": True,
            "pass_direction_top5": pass_b,
            "top10_boundaries_by_distance": sorted_desc[:10],
        },
        "cell_C_14_sajda_corpus_replication": {
            "n_sajda_tested": n_cellC_valid,
            "n_top5_within_their_surah": n_cellC_top5,
            "n_above_95th_percentile_within_surah": n_cellC_above_95pct,
            "fraction_top5": n_cellC_top5 / n_cellC_valid if n_cellC_valid else 0.0,
            "fraction_above_95pct": n_cellC_above_95pct / n_cellC_valid if n_cellC_valid else 0.0,
            "table": cellC,
        },
        "verdict": verdict,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"WROTE {OUT}")
    print(f"verdict: {verdict}")
    print(f"d_sajda symmetric: {d_sajda:.4f}, percentile: {percentile_d_sajda:.4f}, rank-desc: {rank_d_sajda}")


if __name__ == "__main__":
    main()
