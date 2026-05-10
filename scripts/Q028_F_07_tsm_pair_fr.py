#!/usr/bin/env python3
"""Q028-F-07 — TSM pair {Q 26, Q 28} Fisher-Rao distance, closest-intra-cluster test.

Pre-reg: surahs/Q028-al-qasas/Q028-F-07-tsm-pair-fr-distance-prereg.md
Pre-reg SHA256: dacc213250309dd1b8fe45d08b5d57ea9012790eb2109bcad63e980eecf93d53
Rules-tuple: H-NEW-111 standard (QAC-STEM-roots, top-K=500, Dirichlet α=0.5, L1-normalised, Fisher-Rao angular distance)
Seed: 20260509
"""
import hashlib
import json
import math
import re
import sys
import os
from collections import Counter, defaultdict

PREREG = '/Users/grey/Downloads/quran/surahs/Q028-al-qasas/Q028-F-07-tsm-pair-fr-distance-prereg.md'
EXPECTED_SHA = 'dacc213250309dd1b8fe45d08b5d57ea9012790eb2109bcad63e980eecf93d53'
SEED = 20260509
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q028-al-qasas/csv/Q028-F-07.json'
QAC = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'

K_TOP = 500
DIRICHLET_ALPHA = 0.5

LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}",
              file=sys.stderr)
        sys.exit(1)


def build_fr_matrix():
    per_surah_roots = defaultdict(list)
    global_root_counts = Counter()

    with open(QAC, encoding='utf-8') as f:
        for line in f:
            if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
                continue
            parts = line.rstrip('\n').split('\t')
            if len(parts) < 4:
                continue
            m = LOC_RE.match(parts[0])
            if not m:
                continue
            sid = int(m.group(1))
            feat = parts[3]
            if 'STEM' not in feat:
                continue
            rm = ROOT_RE.search(feat)
            if not rm:
                continue
            root = rm.group(1)
            per_surah_roots[sid].append(root)
            global_root_counts[root] += 1

    assert len(per_surah_roots) == 114, f"Expected 114 surahs, got {len(per_surah_roots)}"

    top_roots = [r for r, _ in global_root_counts.most_common(K_TOP)]
    top_idx = {r: i for i, r in enumerate(top_roots)}

    counts = [[0.0] * K_TOP for _ in range(115)]
    for sid in range(1, 115):
        for r in per_surah_roots.get(sid, []):
            idx = top_idx.get(r)
            if idx is not None:
                counts[sid][idx] += 1.0

    prob = [[0.0] * K_TOP for _ in range(115)]
    for sid in range(1, 115):
        smoothed = [c + DIRICHLET_ALPHA for c in counts[sid]]
        s = sum(smoothed)
        prob[sid] = [v / s for v in smoothed]

    sqrt_prob = [[math.sqrt(p) for p in prob[sid]] for sid in range(115)]

    D = [[0.0] * 115 for _ in range(115)]
    for i in range(1, 115):
        for j in range(i + 1, 115):
            bc = sum(sqrt_prob[i][k] * sqrt_prob[j][k] for k in range(K_TOP))
            bc = max(-1.0, min(1.0, bc))
            d = 2.0 * math.acos(bc)
            D[i][j] = d
            D[j][i] = d

    return D


def main():
    verify_sha()
    print("Building 114×114 Fisher-Rao matrix (H-NEW-111 protocol)...", file=sys.stderr)
    D = build_fr_matrix()

    # The three intra-cluster pairs
    d_26_28 = D[26][28]
    d_26_27 = D[26][27]
    d_27_28 = D[27][28]

    # Q 28's full neighbor list
    q28_neighbors = sorted([(j, D[28][j]) for j in range(1, 115) if j != 28],
                            key=lambda x: x[1])
    q26_rank_in_q28_nbrs = 1 + next(i for i, (j, _) in enumerate(q28_neighbors) if j == 26)
    q27_rank_in_q28_nbrs = 1 + next(i for i, (j, _) in enumerate(q28_neighbors) if j == 27)

    # All-pairs corpus distribution
    all_pairs = []
    for i in range(1, 115):
        for j in range(i + 1, 115):
            all_pairs.append(D[i][j])
    all_pairs_sorted = sorted(all_pairs)
    # Percentile of d_26_28 among all 6,441 pairs
    n_pairs = len(all_pairs)
    pct_26_28 = (sum(1 for d in all_pairs if d <= d_26_28) - 1) / (n_pairs - 1) * 100.0

    # Verdicts
    h1_pass = (d_26_28 < min(d_26_27, d_27_28))
    h2_pass = (q26_rank_in_q28_nbrs <= 5)
    h3_pass = (pct_26_28 < 50.0)

    if h1_pass and h2_pass and h3_pass:
        verdict = 'CONFIRMED'
    elif h1_pass or h2_pass or h3_pass:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q028-F-07',
        'pre_reg_sha256': EXPECTED_SHA,
        'seed': SEED,
        'rules_tuple': 'H-NEW-111 standard (QAC-STEM-roots, K_TOP=500, Dirichlet α=0.5, L1-normalised, Fisher-Rao angular)',
        'k_top': K_TOP,
        'dirichlet_alpha': DIRICHLET_ALPHA,
        'fr_distance_26_28': d_26_28,
        'fr_distance_26_27': d_26_27,
        'fr_distance_27_28': d_27_28,
        'min_ts_only_pair': min(d_26_27, d_27_28),
        'q28_nearest_5_neighbors': [{'sid': j, 'fr': d} for j, d in q28_neighbors[:5]],
        'q28_farthest_5_neighbors': [{'sid': j, 'fr': d} for j, d in q28_neighbors[-5:]],
        'q26_rank_in_q28_neighbors': q26_rank_in_q28_nbrs,
        'q27_rank_in_q28_neighbors': q27_rank_in_q28_nbrs,
        'corpus_pair_percentile_26_28': pct_26_28,
        'n_corpus_pairs': n_pairs,
        'h1_tsm_pair_closest_in_cluster': h1_pass,
        'h2_q26_in_q28_top5_neighbors': h2_pass,
        'h3_pair_below_median_percentile': h3_pass,
        'verdict': verdict,
        'interpretation': (
            'NULL consolidates Wave-FALSIFIED §3.7 on a 6th independent axis (FR on tightest TSM specialisation)'
            if verdict == 'NULL' else
            ('DIRECTIONAL pending replication on other exact-letter-match clusters'
             if verdict == 'DIRECTIONAL' else
             'CONFIRMED — TSM letter-prefix-match indexes content-cluster on FR axis')
        ),
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    json.dump(out, open(OUT_PATH, 'w'), indent=2, ensure_ascii=False)

    print(f"Q028-F-07 verdict: {verdict}")
    print(f"  FR(Q 26, Q 28) = {d_26_28:.4f}")
    print(f"  FR(Q 26, Q 27) = {d_26_27:.4f}")
    print(f"  FR(Q 27, Q 28) = {d_27_28:.4f}")
    print(f"  min TS-only pair = {min(d_26_27, d_27_28):.4f}")
    print(f"  H1 TSM-pair closest in cluster: pass={h1_pass}")
    print(f"  Q 26 rank in Q 28's neighbors: {q26_rank_in_q28_nbrs}/113 (H2 ≤5 pass={h2_pass})")
    print(f"  Q 27 rank in Q 28's neighbors: {q27_rank_in_q28_nbrs}/113")
    print(f"  FR(Q26,Q28) corpus percentile: {pct_26_28:.1f}% (H3 <50% pass={h3_pass})")
    print(f"  Q 28 top-5 nearest: {[(j, round(d,3)) for j, d in q28_neighbors[:5]]}")
    print(f"  Output: {OUT_PATH}")


if __name__ == '__main__':
    main()
