#!/usr/bin/env python3
"""Q096-F-03 — Q 96 ↔ Q 68 al-Qalam structural mirror via FR + revelation-order.

Pre-reg: Q096-F-03-q96-q68-qalam-prereg.md
SHA256:  e97e3b6381bac5ed1990a07038b19a2a1081d2552de71d2361fb22a4b5b331c8
Seed:    20260509
"""
import csv
import hashlib
import json
import random
from itertools import combinations
from pathlib import Path

REPO = Path("/Users/grey/Downloads/quran")
PREREG = REPO / "surahs/Q096-al-alaq/preregs/Q096-F-03-q96-q68-qalam-prereg.md"
EXPECTED_SHA = "e97e3b6381bac5ed1990a07038b19a2a1081d2552de71d2361fb22a4b5b331c8"
H111 = REPO / "findings/phase-b-hypotheses/csv/h-new-111.json"
QURAN = REPO / "quran-text/quran-no-tashkeel.json"
REV = REPO / "data/revelation-order.csv"
OUT = REPO / "surahs/Q096-al-alaq/csv/q096-f-03.json"
SEED = 20260509


def verify_sha():
    sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if sha != EXPECTED_SHA:
        raise SystemExit(f"PREREG SHA mismatch: {sha} != {EXPECTED_SHA}")


def load_fr_matrix():
    with open(H111) as f:
        d = json.load(f)
    ut = d["D_matrix_upper_triangular"]
    N = 114
    D = [[0.0] * N for _ in range(N)]
    for entry in ut:
        i, j, dist = entry
        D[i - 1][j - 1] = dist
        D[j - 1][i - 1] = dist
    return D


def load_period_and_verses():
    with open(QURAN) as f:
        q = json.load(f)
    verses = {s["id"]: s["total_verses"] for s in q}
    period = {}
    rev_order = {}
    with open(REV) as f:
        rdr = csv.DictReader(f)
        for r in rdr:
            sid = int(r["mushaf_order"])
            period[sid] = r.get("period", "")
            rev_order[sid] = int(r["revelation_order"])
    return verses, period, rev_order


def run():
    D = load_fr_matrix()
    verses, period, rev_order = load_period_and_verses()

    # Cell A — FR(Q 68, Q 96) vs length-matched Meccan pairs (verses ∈ [17, 53])
    obs_fr = D[67][95]  # Q 68 ↔ Q 96
    meccan_pool = [sid for sid in range(1, 115) if period.get(sid) == "Meccan" and 17 <= verses[sid] <= 53]
    # Generate all C(N, 2) pairs in pool
    pool_pairs = list(combinations(meccan_pool, 2))
    pair_dists = [(p[0], p[1], D[p[0] - 1][p[1] - 1]) for p in pool_pairs]
    n_le = sum(1 for _, _, d in pair_dists if d <= obs_fr)
    p_A = n_le / len(pair_dists)
    rank_A = sorted([d for _, _, d in pair_dists]).index(obs_fr) + 1 if obs_fr in [d for _, _, d in pair_dists] else None
    # If obs_fr is in the pool, rank it; otherwise count strict-le and add 1
    sorted_dists = sorted([d for _, _, d in pair_dists])
    rank_A = sum(1 for d in sorted_dists if d < obs_fr) + 1

    # Cell B — Tanzil rev-order consecutive pair (1, 2): rank Q 96-Q 68 FR among 113 consecutive pairs
    inv_rev = {v: k for k, v in rev_order.items()}
    consecutive_pairs = []
    for r in range(1, 114):
        s_a = inv_rev.get(r)
        s_b = inv_rev.get(r + 1)
        if s_a and s_b:
            consecutive_pairs.append((r, s_a, s_b, D[s_a - 1][s_b - 1]))
    sorted_consecutive = sorted(consecutive_pairs, key=lambda x: x[3])
    # Find Q 96-Q 68 (rev 1-2) rank
    rank_B = next(i for i, (r, _, _, _) in enumerate(sorted_consecutive, start=1) if r == 1)
    p_B = rank_B / len(consecutive_pairs)

    # MW-5 PC: musabbiḥāt cluster Q 57 ↔ Q 59, length-matched-Meccan-pair test
    # Q 57 verses=29 (Medinan), Q 59 verses=24 (Medinan); both Medinan, NOT in Meccan pool by definition
    # Use the actual cluster-test instead: pairwise FR for Q 57 ↔ Q 59 vs ALL pairs in {1..114} excluding Q 1
    musab_pair_dist = D[56][58]  # Q 57, Q 59
    all_pairs_dists = []
    for i in range(2, 115):  # exclude Q 1
        for j in range(i + 1, 115):
            all_pairs_dists.append(D[i - 1][j - 1])
    rank_pc = sum(1 for d in all_pairs_dists if d < musab_pair_dist) + 1
    p_pc = rank_pc / len(all_pairs_dists)

    pass_a = p_A <= 0.025
    pass_b = p_B <= 0.025
    pass_pc = p_pc <= 0.05  # PC single-test

    if not pass_pc:
        verdict = "NULL-BROKEN (positive control failed)"
    elif pass_a and pass_b:
        verdict = "PASS-DIRECTED (both cells)"
    elif pass_a:
        verdict = "PARTIAL — FR-near but chronologically-typical"
    elif pass_b:
        verdict = "PARTIAL — chronologically-near but FR-typical"
    else:
        verdict = "NULL"

    out = {
        "id": "Q096-F-03",
        "title": "Q 96 ↔ Q 68 al-Qalam structural mirror",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "obs_FR_q68_q96": obs_fr,
        "cell_A_meccan_pair_FR": {
            "pool_size": len(meccan_pool),
            "n_pairs": len(pair_dists),
            "obs_FR": obs_fr,
            "rank": rank_A,
            "p_perm": p_A,
            "alpha_bon": 0.025,
            "pass": pass_a,
        },
        "cell_B_consecutive_rev_order_FR": {
            "n_consecutive_pairs": len(consecutive_pairs),
            "q96_q68_rev_pair": (1, 2),
            "obs_FR": obs_fr,
            "rank": rank_B,
            "p_perm": p_B,
            "alpha_bon": 0.025,
            "pass": pass_b,
        },
        "mw5_positive_control_q57_q59": {
            "obs_FR": musab_pair_dist,
            "rank_in_all_pairs": rank_pc,
            "n_total_pairs": len(all_pairs_dists),
            "p_perm": p_pc,
            "pass": pass_pc,
        },
        "bonferroni_k": 2,
        "alpha_bon_per_cell": 0.025,
        "verdict": verdict,
        "top_5_meccan_pairs_by_low_FR": sorted([(p[0], p[1], p[2]) for p in pair_dists], key=lambda x: x[2])[:5],
        "top_5_consecutive_rev_pairs_by_low_FR": [(r, s_a, s_b, dist) for r, s_a, s_b, dist in sorted_consecutive[:5]],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Wrote {OUT}")
    print(json.dumps(out, indent=2, ensure_ascii=False)[:2500])


if __name__ == "__main__":
    verify_sha()
    run()
