#!/usr/bin/env python3
"""
Q036-F-02 — UAS-vs-fadāʾil divergence cell membership for Q 36.

Pre-reg SHA-256:
    6d2a50a502bff0a2440b18299da5c3b5805e8634e14926c8fcfb9d1ec41e060f
"""

import hashlib
import json
import os
import sys

PROJECT = '/Users/grey/Downloads/quran'

PREREG_PATH = os.path.join(PROJECT, 'surahs/Q036-yasin/preregs/Q036-F-02-uas-vs-fadail-corpus-divergence-prereg.md')
PREREG_SHA_EXPECTED = '6d2a50a502bff0a2440b18299da5c3b5805e8634e14926c8fcfb9d1ec41e060f'


def verify_prereg_sha():
    with open(PREREG_PATH, 'rb') as f:
        h = hashlib.sha256(f.read()).hexdigest()
    if h != PREREG_SHA_EXPECTED:
        print(f"PRE-REG SHA MISMATCH: expected {PREREG_SHA_EXPECTED}, got {h}", file=sys.stderr)
        sys.exit(1)
    return h


def main():
    sha = verify_prereg_sha()
    print(f"pre-reg SHA verified: {sha[:12]}...")

    # Load UAS rankings
    with open(os.path.join(PROJECT, 'findings/phase-b-hypotheses/csv/h-new-840.json')) as f:
        uas_data = json.load(f)
    all_uas = uas_data['all_uas']
    ranked_uas = sorted(all_uas, key=lambda x: -x['UAS'])
    uas_rank = {e['surah']: i + 1 for i, e in enumerate(ranked_uas)}
    uas_score = {e['surah']: e['UAS'] for e in all_uas}

    # Locked fadāʾil 10/10 set per Wave-D launch task and H-NEW-860
    fadail_10 = [1, 2, 36, 67, 112]

    # Load FR distance matrix
    with open(os.path.join(PROJECT, 'findings/phase-b-hypotheses/csv/h-new-111.json')) as f:
        fr_data = json.load(f)
    D_upper = fr_data['D_matrix_upper_triangular']
    fr = {}
    for i, j, d in D_upper:
        fr[(i, j)] = d
        fr[(j, i)] = d

    # 2a: Q 36 in divergence cell?
    q36_uas_rank = uas_rank[36]
    q36_uas_score = uas_score[36]
    cond_2a = q36_uas_rank > 25  # fadāʾil = 10 already given
    # 2b: Q 36 less divergent than Q 112 and Q 67?
    cond_2b = (q36_uas_rank < uas_rank[112]) and (q36_uas_rank < uas_rank[67])
    # 2c: Q 36's FR-nearest among fadāʾil-10 peers is Q 67 (not Q 1 or Q 2)
    fadail_distances = {peer: fr[(36, peer)] for peer in fadail_10 if peer != 36}
    nearest_fadail_peer = min(fadail_distances, key=fadail_distances.get)
    cond_2c = nearest_fadail_peer == 67

    # Verdict
    verdicts = {
        '2a_in_divergence_cell': 'CONFIRMED' if cond_2a else 'FAILED',
        '2b_less_divergent_than_q112_q67': 'CONFIRMED' if cond_2b else 'FAILED',
        '2c_meaning_ijaz_cluster_with_q67': 'CONFIRMED' if cond_2c else 'FAILED',
    }

    out = {
        'finding_id': 'Q036-F-02',
        'pre_reg_sha256': sha,
        'q36_uas_rank': q36_uas_rank,
        'q36_uas_score': q36_uas_score,
        'q36_fadail_score': 10,
        'fadail_10_peers': fadail_10,
        'fadail_10_uas_ranks': {str(s): uas_rank[s] for s in fadail_10},
        'fr_distances_q36_to_fadail_peers': fadail_distances,
        'nearest_fadail_peer': nearest_fadail_peer,
        'condition_2a': cond_2a,
        'condition_2b': cond_2b,
        'condition_2c': cond_2c,
        'verdicts': verdicts,
        'final_verdict': 'CONFIRMED' if all([cond_2a, cond_2b, cond_2c]) else (
            'PARTIAL' if any([cond_2a, cond_2b, cond_2c]) else 'NULL'),
    }

    out_path = os.path.join(PROJECT, 'surahs/Q036-yasin/csv/Q036-F-02.json')
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)

    print(f"wrote {out_path}")
    print(f"Q 36 UAS rank: {q36_uas_rank} (score {q36_uas_score:.4f})")
    print(f"Fadāʾil-10 peer UAS ranks: {out['fadail_10_uas_ranks']}")
    print(f"FR distances Q 36 -> peers: {fadail_distances}")
    print(f"Nearest fadāʾil-10 peer: Q {nearest_fadail_peer}")
    print(f"Verdicts: {verdicts}")
    print(f"FINAL: {out['final_verdict']}")


if __name__ == '__main__':
    main()
