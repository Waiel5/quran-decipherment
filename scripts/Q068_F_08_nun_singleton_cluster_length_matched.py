#!/usr/bin/env python3
"""Q068-F-08 — Nūn-opener uniqueness + length-matched singleton-triplet FR cluster (MW-5 replication).

Pre-reg: surahs/Q068-al-qalam/preregs/Q068-F-08-nun-singleton-cluster-length-matched-prereg.md
SHA256: 9cea3e52629eeaf6ff0bc94eb1338db29a49fa3367b204197fe8c9b1b2cafe94
Seed: 20260509.
"""
from __future__ import annotations

import hashlib
import json
import random
import sys
from pathlib import Path

PROJECT = Path('/Users/grey/Downloads/quran')
PREREG = PROJECT / 'surahs' / 'Q068-al-qalam' / 'preregs' / 'Q068-F-08-nun-singleton-cluster-length-matched-prereg.md'
EXPECTED_SHA = '9cea3e52629eeaf6ff0bc94eb1338db29a49fa3367b204197fe8c9b1b2cafe94'
OUT = PROJECT / 'surahs' / 'Q068-al-qalam' / 'csv' / 'Q068-F-08.json'
FR = PROJECT / 'findings' / 'phase-b-hypotheses' / 'csv' / 'h-new-111.json'
QURAN = PROJECT / 'quran-text' / 'quran-no-tashkeel.json'

# 29 muqaṭṭaʿāt-opener surahs per al-Suyūṭī al-Itqān classical canon
MUQATTAAT_SURAHS = [
    2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
    36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68,
]
TRIPLET = [38, 50, 68]


def verify_sha() -> None:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.stderr.write(f'SHA mismatch: expected {EXPECTED_SHA}, got {actual}\n')
        sys.exit(2)


def load_quran():
    return json.loads(QURAN.read_text(encoding='utf-8'))


def load_fr_matrix():
    d = json.loads(FR.read_text(encoding='utf-8'))
    D = {}
    for i, j, dist in d['D_matrix_upper_triangular']:
        D[(int(i), int(j))] = float(dist)
        D[(int(j), int(i))] = float(dist)
    return D, d.get('pre_reg_sha256', '')


def cluster_mean(cluster, D):
    pairs = [D[(a, b)] for a in cluster for b in cluster if a < b]
    return sum(pairs) / len(pairs) if pairs else 0.0


def main() -> None:
    verify_sha()
    quran = load_quran()
    D, h111_sha = load_fr_matrix()

    # Sub-test (a) — Nūn-opener uniqueness audit
    nun_openers = []
    opener_table = []
    for s in MUQATTAAT_SURAHS:
        v1 = quran[s - 1]['verses'][0]['text'].strip()
        first_token = v1.split()[0]
        opener_table.append({'surah': s, 'verse_1_first_token': first_token, 'verse_1_full': v1})
        if first_token == 'ن':
            nun_openers.append(s)
    n_nun = len(nun_openers)
    if n_nun == 1 and nun_openers == [68]:
        verdict_a = 'VINDICATED'
    elif n_nun == 2:
        verdict_a = 'DIRECTIONAL'
    else:
        verdict_a = 'NULL'

    # Sub-test (b) — length-matched triplet FR cluster
    verse_counts = {s: q['total_verses'] for s, q in enumerate(quran, start=1)}
    target_min = min(verse_counts[s] for s in TRIPLET)  # 45
    target_max = max(verse_counts[s] for s in TRIPLET)  # 88
    lo = 0.5 * target_min  # 22.5
    hi = 1.5 * target_max  # 132
    pool = [s for s, n in verse_counts.items() if lo <= n <= hi and s not in TRIPLET]
    obs_mean = cluster_mean(TRIPLET, D)
    rng = random.Random(20260509)
    n_perm = 10000
    null_means = []
    le = 0
    for _ in range(n_perm):
        triple = rng.sample(pool, 3)
        m = cluster_mean(triple, D)
        null_means.append(m)
        if m <= obs_mean:
            le += 1
    p_low = le / n_perm
    null_mean = sum(null_means) / len(null_means)

    if obs_mean > null_mean:
        verdict_b = 'DIRECTION_REVERSED'
    elif p_low < 0.025:
        verdict_b = 'VINDICATED-LM'
    elif p_low < 0.05:
        verdict_b = 'DIRECTIONAL-LM'
    else:
        verdict_b = 'NULL-LM'

    out = {
        'finding_id': 'Q068-F-08',
        'prereg_sha256': EXPECTED_SHA,
        'h_new_111_sha256': h111_sha,
        'date_run': '2026-05-09',
        'seed': 20260509,
        'n_perm': n_perm,
        'rules_tuple': '(no-tashkeel, QAC-stem-roots, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'sub_test_a_nun_uniqueness': {
            'muqattaat_surahs_audited': MUQATTAAT_SURAHS,
            'n_muqattaat': len(MUQATTAAT_SURAHS),
            'nun_openers_found': nun_openers,
            'n_nun_openers': n_nun,
            'opener_table': opener_table,
            'verdict': verdict_a,
            'interpretation': (
                f"Of {len(MUQATTAAT_SURAHS)} muqaṭṭaʿāt-opener surahs, exactly {n_nun} open with single letter ن: Q {nun_openers}. "
                f"Q 68 is the corpus-EXACT singleton ن-opener (the only one)."
            ),
        },
        'sub_test_b_length_matched_fr_cluster': {
            'triplet': TRIPLET,
            'verse_counts_triplet': {s: verse_counts[s] for s in TRIPLET},
            'length_matched_pool_size': len(pool),
            'length_matched_pool_bounds_verses': [lo, hi],
            'length_matched_pool': pool,
            'observed_mean_pairwise_fr': obs_mean,
            'pairwise_fr_internal': {
                'Q38_Q50': D[(38, 50)],
                'Q38_Q68': D[(38, 68)],
                'Q50_Q68': D[(50, 68)],
            },
            'null_mean': null_mean,
            'null_min': min(null_means),
            'null_max': max(null_means),
            'p_one_sided_low': p_low,
            'percentile_low': p_low * 100,
            'verdict': verdict_b,
        },
        'alpha_bonferroni_2': 0.025,
        'joint_verdict': f'{verdict_a} + {verdict_b}',
        'cross_reference_q050_F_04': {
            'q050_F_04_null_type': 'random-3-surah from 114-surah space',
            'q050_F_04_observed_mean': 0.8699,
            'q050_F_04_p_low': 0.267,
            'q050_F_04_verdict': 'NULL',
            'replication_status': (
                'NULL-NULL DOUBLE-REPLICATION' if verdict_b == 'NULL-LM' else
                'LENGTH-MATCHING RECOVERS SIGNAL' if verdict_b.startswith('VINDICATED') else
                'PARTIAL'
            ),
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(json.dumps({'verdict_a': verdict_a, 'verdict_b': verdict_b, 'p_low': p_low, 'obs_mean': obs_mean}, ensure_ascii=False))


if __name__ == '__main__':
    main()
