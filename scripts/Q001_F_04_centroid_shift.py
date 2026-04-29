"""
Q001-F-04 — Q 1 centroid-anchor test: ranking surah-removal effects on corpus mean FR distance.

Pre-reg: surahs/Q001-al-fatiha/Q001-F-04-q1-removal-centroid-shift-prereg.md
Pre-reg SHA256: 3f8b31c0f9e4f4d8d2a1a96bc1ee71e5f283520fcd429bed8f71a7e1f99a0070
"""
import json
import hashlib
import os

PROJECT = "/Users/grey/Downloads/quran"
PREREG_PATH = f"{PROJECT}/surahs/Q001-al-fatiha/Q001-F-04-q1-removal-centroid-shift-prereg.md"
PREREG_SHA_EXPECTED = "3f8b31c0f9e4f4d8d2a1a96bc1ee71e5f283520fcd429bed8f71a7e1f99a0070"
OUT_PATH = f"{PROJECT}/surahs/Q001-al-fatiha/csv/Q001-F-04.json"
H111 = f"{PROJECT}/findings/phase-b-hypotheses/csv/h-new-111.json"


def sha256_file(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def main():
    sha = sha256_file(PREREG_PATH)
    assert sha == PREREG_SHA_EXPECTED, f"SHA mismatch {sha}"

    d = json.load(open(H111))
    triples = d["D_matrix_upper_triangular"]  # list of [i, j, dist], i<j, 1-indexed
    N = 114
    # Build symmetric distance matrix
    D = [[0.0] * (N + 1) for _ in range(N + 1)]  # 1-indexed
    for i, j, dist in triples:
        D[i][j] = dist
        D[j][i] = dist

    # Full corpus mean (excluding diagonal)
    sum_all = sum(D[i][j] for i in range(1, N + 1) for j in range(i + 1, N + 1))
    n_all = N * (N - 1) // 2
    mean_all = sum_all / n_all

    # mean over Q 1's row (Q 1 to all others)
    row_means = {}
    for x in range(1, N + 1):
        row_sum = sum(D[x][j] for j in range(1, N + 1) if j != x)
        row_means[x] = row_sum / (N - 1)
    q1_row_mean = row_means[1]

    # For each candidate X, compute mean over the 113-surah remainder
    d_bar = {}
    for X in range(1, N + 1):
        # remaining sum: full - sum of D[X][*]
        remain_sum = sum_all - sum(D[X][j] for j in range(1, N + 1) if j != X)
        remain_n = (N - 1) * (N - 2) // 2
        d_bar[X] = remain_sum / remain_n

    # Rank ascending — smaller = removing X most lowers corpus mean = X is least centroidal (anti-anchor)
    # Wait: removing a CENTROIDAL surah means OTHER surahs no longer have low distances pulled toward it,
    # so removing X with low row_mean LEAVES BEHIND a corpus whose REMAINING mean is HIGHER.
    # Logic check:
    #   d_bar(X) = (sum_all - row_sum(X)) / remain_n
    #   if row_sum(X) is LOW (X is central), then numerator drops less, but denominator also drops.
    # The TRUE test of "X is centroid-anchor" is: row_mean(X) is LOW relative to others.
    # The "removal shift" Δ = mean_all - d_bar(X).
    delta = {X: mean_all - d_bar[X] for X in range(1, N + 1)}

    # Rank by row_mean ascending (most central = smallest mean distance to others)
    ranked_centrality = sorted(row_means.items(), key=lambda kv: kv[1])
    q1_centrality_rank = next(i for i, (sid, _) in enumerate(ranked_centrality, 1) if sid == 1)

    # Rank by d_bar ascending (smallest residual mean → most "anchor-toward-low" effect when removed)
    # Actually: high row_mean(X) means X is FAR from others; removing X drops its high distances → residual mean DROPS more.
    # So removing a PERIPHERAL surah lowers d_bar most. Removing a CENTRAL surah lowers d_bar least.
    # Therefore Q 1 (central) should have HIGH d_bar after removal — meaning Q 1 holds the corpus close.
    ranked_dbar_asc = sorted(d_bar.items(), key=lambda kv: kv[1])
    q1_dbar_rank_asc = next(i for i, (sid, _) in enumerate(ranked_dbar_asc, 1) if sid == 1)
    ranked_dbar_desc = sorted(d_bar.items(), key=lambda kv: kv[1], reverse=True)
    q1_dbar_rank_desc = next(i for i, (sid, _) in enumerate(ranked_dbar_desc, 1) if sid == 1)

    # The pre-registered test was "Q 1 in BOTTOM-3 of d_bar" (i.e., low d_bar after Q 1 removal).
    # But by the logic above, Q 1 being centroid-anchor → HIGH d_bar after removal (top-3, not bottom).
    # PRE-COMMIT VIOLATION CHECK: pre-reg said BOTTOM-3. We honor the pre-reg as locked.
    # Honest reporting requires reporting BOTH directions.

    out = {
        "test_id": "Q001-F-04",
        "prereg_sha": sha,
        "corpus_mean_all": mean_all,
        "q1_row_mean": q1_row_mean,
        "q1_centrality_rank_smallest_first": q1_centrality_rank,
        "ranked_centrality_top10": [{"surah": s, "row_mean": rm} for s, rm in ranked_centrality[:10]],
        "ranked_centrality_bottom10": [{"surah": s, "row_mean": rm} for s, rm in ranked_centrality[-10:]],
        "q1_dbar_rank_ascending": q1_dbar_rank_asc,  # rank if smallest d_bar = rank 1
        "q1_dbar_rank_descending": q1_dbar_rank_desc,
        "ranked_dbar_top10_smallest": [{"surah": s, "d_bar": dv, "delta_from_mean_all": mean_all - dv} for s, dv in ranked_dbar_asc[:10]],
        "ranked_dbar_top10_largest": [{"surah": s, "d_bar": dv, "delta_from_mean_all": mean_all - dv} for s, dv in ranked_dbar_desc[:10]],
        "verdict_prereg_bottom3_of_dbar": ("VINDICATED" if q1_dbar_rank_asc <= 3 else ("DIRECTIONAL" if q1_dbar_rank_asc <= 10 else "NULL")),
        "honest_reframing_note": "Pre-reg direction (bottom-3 of d_bar) is LOGICALLY INVERTED for the centroid-anchor hypothesis. Removing a central surah RAISES d_bar (top-K), not lowers it. The pre-reg as written tests the WRONG direction. Reporting both ranks for transparency. The CORRECT centroid-anchor test is the row_mean rank (q1_centrality_rank).",
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Corpus mean (all pairs): {mean_all:.4f}")
    print(f"Q 1 row-mean (Q 1 to all 113 others): {q1_row_mean:.4f}")
    print(f"Q 1 centrality rank (1=most central, smallest row_mean): {q1_centrality_rank}/114")
    print(f"Q 1 d_bar-after-removal rank ascending: {q1_dbar_rank_asc}/114")
    print(f"Q 1 d_bar-after-removal rank descending: {q1_dbar_rank_desc}/114")
    print(f"Output: {OUT_PATH}")


if __name__ == "__main__":
    main()
