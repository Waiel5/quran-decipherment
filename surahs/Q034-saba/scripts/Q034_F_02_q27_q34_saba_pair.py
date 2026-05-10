#!/usr/bin/env python3
"""Q034-F-02 — Q 27 al-Naml + Q 34 Sabaʾ Saba-narrative pair FR cohesion test.

Pre-reg: surahs/Q034-saba/preregs/Q034-F-02-q27-q34-saba-pair-prereg.md
Pre-reg SHA256: a8fd1b2d5e99d2d605a2794af208a69296860e4b238ab92da2155d194d007600
Rules-tuple: (no-tashkeel, QAC-root, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)

H1: D[Q27, Q34] percentile <= 25.
H2: Q27 and Q34 mutually in each other's top-10 FR neighbors.
H3: length-residualized D[Q27,Q34] percentile <= 25.
Bonferroni k=3, alpha_bon=0.01667.
"""
import json, hashlib, sys, os, math

PREREG = '/Users/grey/Downloads/quran/surahs/Q034-saba/preregs/Q034-F-02-q27-q34-saba-pair-prereg.md'
EXPECTED_SHA = 'a8fd1b2d5e99d2d605a2794af208a69296860e4b238ab92da2155d194d007600'
SEED = 20260509
N_PERM = 10000
ALPHA_BON = 0.05 / 3


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()

    # Load FR matrix
    with open('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json') as f:
        d111 = json.load(f)
    ut = d111['D_matrix_upper_triangular']
    N = 114
    mat = [[0.0]*N for _ in range(N)]
    for entry in ut:
        i, j, v = entry
        mat[i-1][j-1] = v
        mat[j-1][i-1] = v

    # H1: D[Q27, Q34] percentile
    d_27_34 = mat[26][33]
    all_pairs = []
    for i in range(N):
        for j in range(i+1, N):
            all_pairs.append(mat[i][j])
    all_pairs_sorted = sorted(all_pairs)
    rank = sum(1 for p in all_pairs_sorted if p < d_27_34) + 1
    percentile = 100.0 * rank / len(all_pairs_sorted)
    h1_pass = percentile <= 25

    # H2: mutual top-10
    def top_k_neighbors(s_idx, k=10):
        # Return list of (other_surah_1indexed, dist) sorted ascending; exclude s_idx itself.
        nbrs = []
        for j in range(N):
            if j == s_idx:
                continue
            nbrs.append((j+1, mat[s_idx][j]))
        nbrs.sort(key=lambda x: x[1])
        return nbrs[:k]

    top10_27 = top_k_neighbors(26, 10)  # Q27 -> 0-index 26
    top10_34 = top_k_neighbors(33, 10)  # Q34 -> 0-index 33
    q34_in_q27 = any(s == 34 for s, _ in top10_27)
    q27_in_q34 = any(s == 27 for s, _ in top10_34)
    rank_q34_in_q27 = next(((rk for rk, (s, _) in enumerate(top10_27, 1) if s == 34)), None)
    rank_q27_in_q34 = next(((rk for rk, (s, _) in enumerate(top10_34, 1) if s == 27)), None)
    h2_pass = q34_in_q27 and q27_in_q34

    # H3: length-residualized
    verse_counts = {}
    with open('/Users/grey/Downloads/quran/data/hafs-verse-counts.tsv') as f:
        for line in f:
            sid, vc = line.strip().split('\t')
            verse_counts[int(sid)] = int(vc)

    all_pair_idx = []
    all_dists = []
    all_log_diffs = []
    for i in range(N):
        for j in range(i+1, N):
            all_pair_idx.append((i+1, j+1))
            all_dists.append(mat[i][j])
            all_log_diffs.append(abs(math.log(verse_counts[i+1]) - math.log(verse_counts[j+1])))

    # Simple linear regression
    n_pairs = len(all_dists)
    sum_x = sum(all_log_diffs)
    sum_y = sum(all_dists)
    sum_xy = sum(x*y for x, y in zip(all_log_diffs, all_dists))
    sum_xx = sum(x*x for x in all_log_diffs)
    b1 = (n_pairs * sum_xy - sum_x * sum_y) / (n_pairs * sum_xx - sum_x * sum_x)
    b0 = (sum_y - b1 * sum_x) / n_pairs

    residuals = [d - (b0 + b1 * x) for d, x in zip(all_dists, all_log_diffs)]

    # Q27, Q34 residual
    q27_q34_resid = None
    for k, (a, b) in enumerate(all_pair_idx):
        if (a, b) == (27, 34):
            q27_q34_resid = residuals[k]
            break

    residuals_sorted = sorted(residuals)
    rank_resid = sum(1 for r in residuals_sorted if r < q27_q34_resid) + 1
    percentile_resid = 100.0 * rank_resid / len(residuals_sorted)
    h3_pass = percentile_resid <= 25

    n_pass = sum([h1_pass, h2_pass, h3_pass])
    if n_pass == 3: verdict = 'CONFIRMED'
    elif n_pass == 2: verdict = 'DIRECTIONAL'
    elif n_pass == 1: verdict = 'DIRECTIONAL-WEAK'
    else: verdict = 'NULL'

    out = {
        'finding_id': 'Q034-F-02',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, QAC-root, FR-on-QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'seed': SEED,
        'alpha_bon': ALPHA_BON,
        'h1_pair_percentile': {
            'd_q27_q34': d_27_34,
            'percentile': percentile,
            'rank_of_6441': rank,
            'pass': h1_pass,
            'threshold': 25,
        },
        'h2_mutual_top10': {
            'top10_q27_neighbors': [{'surah': s, 'fr': dist} for s, dist in top10_27],
            'top10_q34_neighbors': [{'surah': s, 'fr': dist} for s, dist in top10_34],
            'q34_rank_in_q27_top10': rank_q34_in_q27,
            'q27_rank_in_q34_top10': rank_q27_in_q34,
            'q34_in_q27_top10': q34_in_q27,
            'q27_in_q34_top10': q27_in_q34,
            'pass': h2_pass,
        },
        'h3_length_residualized': {
            'regression_b0': b0,
            'regression_b1': b1,
            'q27_q34_residual': q27_q34_resid,
            'residual_percentile': percentile_resid,
            'pass': h3_pass,
        },
        'n_pass': n_pass,
        'verdict': verdict,
        'honest_limits': 'D[Q27,Q34]=0.8661 sits at 31.3rd percentile (pre-flight observed); H1 threshold 25th — likely FAIL. H2 pre-flight confirmed mutual top-10. H3 likely follows H1 trend. Verdict ceiling = DESCRIPTIVE-EMPIRICAL.',
    }

    print('=== Q034-F-02 Q27<->Q34 Saba-pair cohesion ===')
    print(f'H1: D[Q27,Q34]={d_27_34:.4f}, percentile={percentile:.2f}%, threshold=25% -> pass={h1_pass}')
    print(f'H2: Q34 in Q27 top-10? {q34_in_q27} (rank {rank_q34_in_q27}); Q27 in Q34 top-10? {q27_in_q34} (rank {rank_q27_in_q34}); both? {h2_pass}')
    print(f'H3: residual={q27_q34_resid:.4f}, percentile={percentile_resid:.2f}%, threshold=25% -> pass={h3_pass}')
    print(f'\nN pass: {n_pass}/3 -> {verdict}')

    os.makedirs('/Users/grey/Downloads/quran/surahs/Q034-saba/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q034-saba/csv/Q034-F-02.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)


if __name__ == '__main__':
    main()
