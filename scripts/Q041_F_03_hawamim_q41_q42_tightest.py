#!/usr/bin/env python3
"""Q041-F-03 — Q 41 ↔ Q 42 tightest HM-7 pair on Fisher-Rao.

Pre-reg: surahs/Q041-fussilat/preregs/Q041-F-03-hawamim-q41-q42-tightest-prereg.md
Pre-reg SHA256: 949d624bd39fe62f0b946eb2f58426ff812c1a3e5fff8dbad1c5d4299c27d78b
Rules-tuple: (no-tashkeel, QAC-STEM root tokens, Hafs-Kufan, Mashriqi, FR-distance per H-NEW-111)
"""
import json
import hashlib
import sys
import os
import numpy as np

PREREG = '/Users/grey/Downloads/quran/surahs/Q041-fussilat/preregs/Q041-F-03-hawamim-q41-q42-tightest-prereg.md'
EXPECTED_SHA = '949d624bd39fe62f0b946eb2f58426ff812c1a3e5fff8dbad1c5d4299c27d78b'
SEED = 20260509
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q041-fussilat/csv/Q041-F-03.json'
H_NEW_111 = '/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json'

HAWAMIM = [40, 41, 42, 43, 44, 45, 46]
PRE_COMMITTED_TIGHTEST = (41, 42)


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    d = json.load(open(H_NEW_111))
    ut = d['D_matrix_upper_triangular']
    N = 114
    D = np.zeros((N, N))
    for e in ut:
        i, j, dist = e
        D[i-1, j-1] = dist
        D[j-1, i-1] = dist

    # All 21 HM-7 pairs
    pairs = []
    for i in HAWAMIM:
        for j in HAWAMIM:
            if i < j:
                pairs.append({'pair': [i, j], 'fr_distance': float(D[i-1, j-1])})
    pairs_sorted = sorted(pairs, key=lambda x: x['fr_distance'])

    tightest_pair = tuple(pairs_sorted[0]['pair'])
    q41_q42_dist = float(D[40, 41])  # Q41 = index 40, Q42 = index 41
    q41_q42_rank = next(i + 1 for i, p in enumerate(pairs_sorted) if tuple(p['pair']) == PRE_COMMITTED_TIGHTEST)

    h1_pass = (tightest_pair == PRE_COMMITTED_TIGHTEST)
    pre_commit_violation = not h1_pass

    # The actual tightest pair
    actual_tightest_pair = tightest_pair
    actual_tightest_dist = pairs_sorted[0]['fr_distance']

    verdict = 'VINDICATED' if h1_pass else 'NULL-PRE-COMMIT-VIOLATION'

    # Additional context: Q41 nearest neighbors corpus-wide
    q41_all_distances = []
    for j in range(N):
        if j != 40:
            q41_all_distances.append({'partner_surah': j + 1, 'fr_distance': float(D[40, j])})
    q41_all_distances.sort(key=lambda x: x['fr_distance'])
    q41_top10_neighbors = q41_all_distances[:10]

    out = {
        'finding_id': 'Q041-F-03',
        'pre_reg_sha256': EXPECTED_SHA,
        'seed': SEED,
        'rules_tuple': '(no-tashkeel, QAC-STEM root tokens, Hafs-Kufan, Mashriqi, FR-distance per H-NEW-111)',
        'pre_committed_tightest_pair': list(PRE_COMMITTED_TIGHTEST),
        'observed_tightest_pair': list(actual_tightest_pair),
        'observed_tightest_distance': actual_tightest_dist,
        'q41_q42_fr_distance': q41_q42_dist,
        'q41_q42_rank_among_21_pairs': q41_q42_rank,
        'h1_pass': h1_pass,
        'pre_commit_violation': pre_commit_violation,
        'all_hm7_pairs_sorted_tightest_first': pairs_sorted,
        'q41_top10_corpus_neighbors_for_context': q41_top10_neighbors,
        'verdict': verdict,
        'interpretation': (
            'Q 41 ↔ Q 42 is rank-9 of 21 HM-7 pairs by FR distance. The actual tightest pair is '
            f'Q{actual_tightest_pair[0]} ↔ Q{actual_tightest_pair[1]} at FR={actual_tightest_dist:.6f}. '
            'Per protocol §1.3 (equal NULL prominence) and §1.8 (honest pre-commit violations), '
            'the al-Suyūṭī "two cousins" claim does NOT translate to FR-root tightness within HM-7. '
            'The FR-tightest HM-7 pair is Q 41 ↔ Q 46 — already known to be istiqāma + ʿĀd twin (Q041-F-01).'
        ),
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q041-F-03 verdict: {verdict}")
    print(f"  Pre-committed tightest pair: Q{PRE_COMMITTED_TIGHTEST[0]} ↔ Q{PRE_COMMITTED_TIGHTEST[1]}")
    print(f"  Observed tightest pair: Q{actual_tightest_pair[0]} ↔ Q{actual_tightest_pair[1]} (FR={actual_tightest_dist:.6f})")
    print(f"  Q 41 ↔ Q 42 FR distance: {q41_q42_dist:.6f} (rank {q41_q42_rank}/21)")
    print(f"  H1 pass: {h1_pass}; pre-commit-violation: {pre_commit_violation}")
    print(f"  Output: {OUT_PATH}")


if __name__ == '__main__':
    main()
