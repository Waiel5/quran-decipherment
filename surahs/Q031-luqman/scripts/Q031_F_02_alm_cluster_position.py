#!/usr/bin/env python3
"""
Q031-F-02 — Q 31 FR-position within the 6-surah ALM cohort.

Pre-reg: surahs/Q031-luqman/preregs/Q031-F-02-alm-cluster-position-prereg.md
Pre-reg SHA256: d496f4a2d887f304cb973daaf69b1fdf3619b0c1b073d6a32e0389be37ae1fcc
Seed: 20260509
Direction: NULL (Q 31 has NO preferential FR-cohesion with ALM-siblings)
"""
import json
import hashlib
import random
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG_PATH = ROOT / 'surahs/Q031-luqman/preregs/Q031-F-02-alm-cluster-position-prereg.md'
EXPECTED_SHA = 'd496f4a2d887f304cb973daaf69b1fdf3619b0c1b073d6a32e0389be37ae1fcc'
OUT_PATH = ROOT / 'surahs/Q031-luqman/csv/Q031-F-02.json'
FR_PATH = ROOT / 'findings/phase-b-hypotheses/csv/h-new-111.json'
SEED = 20260509
N_PERM = 10000


def verify_prereg_sha():
    with open(PREREG_PATH, 'rb') as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {sha}")
    return sha


def load_fr_matrix():
    with open(FR_PATH) as f:
        data = json.load(f)
    n = 114
    D = [[0.0] * n for _ in range(n)]
    for triple in data['D_matrix_upper_triangular']:
        i, j, d = triple
        D[i-1][j-1] = d
        D[j-1][i-1] = d
    return D


def main():
    sha = verify_prereg_sha()
    print(f"PRE-REG SHA verified: {sha[:16]}...")

    rng = random.Random(SEED)
    D = load_fr_matrix()
    n = 114

    # Q 31's FR-row (0-indexed)
    q31_idx = 30
    q31_row = D[q31_idx]

    # ALM-siblings of Q 31 (1-indexed: 2, 3, 29, 30, 32 — exclude Q 31 itself)
    alm_siblings_1idx = [2, 3, 29, 30, 32]
    alm_siblings_0idx = [s - 1 for s in alm_siblings_1idx]
    d_alm_q31 = sum(q31_row[s] for s in alm_siblings_0idx) / len(alm_siblings_0idx)
    print(f"\nQ 31 mean FR to 5 ALM-siblings: {d_alm_q31:.4f}")
    for s in alm_siblings_1idx:
        print(f"  FR(Q31, Q{s}) = {q31_row[s-1]:.4f}")

    # Top-12 nearest non-ALM neighbors
    candidates = sorted(
        [(j+1, q31_row[j]) for j in range(n) if j != q31_idx and (j+1) not in alm_siblings_1idx],
        key=lambda x: x[1]
    )
    top12 = candidates[:12]
    d_top12_q31 = sum(d for _, d in top12) / len(top12)
    print(f"\nQ 31 top-12 non-ALM nearest neighbors:")
    for s, d in top12:
        print(f"  FR(Q31, Q{s}) = {d:.4f}")
    print(f"Mean of top-12: {d_top12_q31:.4f}")

    # H1 permutation null: 10,000 random 5-subsets from non-Q31 surahs
    pool = [j for j in range(n) if j != q31_idx]
    perm_means = []
    for _ in range(N_PERM):
        subset = rng.sample(pool, 5)
        m = sum(q31_row[j] for j in subset) / 5
        perm_means.append(m)
    p_one_tailed_low = sum(1 for m in perm_means if m <= d_alm_q31) / N_PERM
    null_mean = sum(perm_means) / len(perm_means)
    print(f"\nH1 — perm-null on 5-random-subset from 113 non-Q31 surahs:")
    print(f"  Null mean: {null_mean:.4f}")
    print(f"  Observed D_alm_q31: {d_alm_q31:.4f}")
    print(f"  One-tailed p (observed ≤ perm_mean): {p_one_tailed_low:.4f}")

    # H2: D_top12_q31 < D_alm_q31?
    h2_pass = d_top12_q31 < d_alm_q31
    print(f"\nH2 — top-12 < ALM?  D_top12={d_top12_q31:.4f} vs D_alm={d_alm_q31:.4f}: {h2_pass}")

    # Verdict
    alpha_bon = 0.025
    h1_null_pass = p_one_tailed_low >= alpha_bon  # NULL-direction pass = NO preferential cohesion
    h1_unexpected_cohesion = p_one_tailed_low < alpha_bon  # would falsify pre-reg

    if h1_null_pass and h2_pass:
        verdict = 'NULL CONFIRMED + H2 vindicated (Q 31 is NOT preferentially close to ALM-siblings; closer to top-12 non-ALM)'
    elif h1_null_pass and not h2_pass:
        verdict = 'NULL CONFIRMED but H2 reversed (Q 31 close to ALM but ALM also close to top-12)'
    elif not h1_null_pass:
        verdict = f'UNEXPECTED COHESION (perm-p={p_one_tailed_low:.4f} < {alpha_bon}; Q 31 IS preferentially ALM-cohesive)'
    else:
        verdict = 'INDETERMINATE'

    result = {
        'test_id': 'Q031-F-02',
        'title': 'Q 31 FR-position within ALM cohort',
        'pre_reg_sha256': sha,
        'pre_reg_sha_expected': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'q31_alm_siblings_fr': {f'Q{s}': q31_row[s-1] for s in alm_siblings_1idx},
        'd_alm_q31_mean': d_alm_q31,
        'top12_non_alm_neighbors': [{'surah': s, 'fr': d} for s, d in top12],
        'd_top12_q31_mean': d_top12_q31,
        'perm_null_mean': null_mean,
        'h1_perm_p_one_tailed_low': p_one_tailed_low,
        'h1_null_pass': h1_null_pass,
        'h1_unexpected_cohesion': h1_unexpected_cohesion,
        'h2_top12_lt_alm': h2_pass,
        'alpha_bon': alpha_bon,
        'bonferroni_k': 2,
        'verdict': verdict,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\nResult written to: {OUT_PATH}")
    print(f"Verdict: {verdict}")
    return result


if __name__ == '__main__':
    main()
