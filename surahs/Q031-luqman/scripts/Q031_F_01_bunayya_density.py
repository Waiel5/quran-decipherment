#!/usr/bin/env python3
"""
Q031-F-01 — Q 31 Luqmān-pericope yā-bunayya density vs other yā-bunayya surahs.

Pre-reg: surahs/Q031-luqman/preregs/Q031-F-01-bunayya-density-prereg.md
Pre-reg SHA256: 1d483e8d6495fd406f3cd17f060cd0b74d581c221cb3ee3e10b0c63cc9858e97
Seed: 20260509
Direction: positive (Q 31 = corpus-MAX in yā-bunayya per-verse density within 5-surah cohort)
"""
import json
import re
import hashlib
import os
import random
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG_PATH = ROOT / 'surahs/Q031-luqman/preregs/Q031-F-01-bunayya-density-prereg.md'
EXPECTED_SHA = '1d483e8d6495fd406f3cd17f060cd0b74d581c221cb3ee3e10b0c63cc9858e97'
OUT_PATH = ROOT / 'surahs/Q031-luqman/csv/Q031-F-01.json'
CORPUS_PATH = ROOT / 'quran-text/quran-no-tashkeel.json'
SEED = 20260509
N_PERM = 10000


def verify_prereg_sha():
    with open(PREREG_PATH, 'rb') as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {sha}")
    return sha


def load_corpus():
    with open(CORPUS_PATH) as f:
        return json.load(f)


def find_yabunayya_singular(verse_text):
    """Find pure-singular father-to-son yā-bunayya. Filter out plural-vocatives banī isrāʾīl, banī ādam."""
    matches = list(re.finditer(r'(?<!\S)يا\s*بني(?:\s+(\S+))?', verse_text))
    hits = []
    for m in matches:
        nxt = m.group(1) or ''
        if 'إسرائيل' in nxt or 'آدم' in nxt:
            continue
        hits.append(m.group(0))
    return hits


def main():
    sha = verify_prereg_sha()
    print(f"PRE-REG SHA verified: {sha[:16]}...")

    rng = random.Random(SEED)
    corpus = load_corpus()

    # Find all singular yā-bunayya occurrences corpus-wide
    yabunayya_per_surah = {}
    yabunayya_total = 0
    for s_idx, surah in enumerate(corpus):
        s_id = s_idx + 1
        cnt = 0
        for v in surah['verses']:
            cnt += len(find_yabunayya_singular(v['text']))
        if cnt > 0:
            yabunayya_per_surah[s_id] = {
                'count': cnt,
                'verse_count': surah['total_verses'],
                'density': cnt / surah['total_verses'],
            }
            yabunayya_total += cnt

    cohort = sorted(yabunayya_per_surah.keys())
    print(f"\nCohort surahs (with at least 1 singular yā-bunayya): {cohort}")
    print(f"Total corpus singular yā-bunayya tokens: {yabunayya_total}")
    for s in cohort:
        d = yabunayya_per_surah[s]
        print(f"  Q{s}: count={d['count']}, verses={d['verse_count']}, density={d['density']:.4f}")

    # H1: per-verse density rank within cohort
    densities = [(s, yabunayya_per_surah[s]['density']) for s in cohort]
    densities.sort(key=lambda x: -x[1])
    print(f"\nDensity ranking (high to low):")
    for rank, (s, d) in enumerate(densities, 1):
        print(f"  rank {rank}: Q{s} = {d:.4f}")

    q31_density = yabunayya_per_surah[31]['density']
    q31_count = yabunayya_per_surah[31]['count']
    q31_rank = [s for s, _ in densities].index(31) + 1
    h1_pass = q31_rank == 1

    # H2: corpus-share
    q31_share = q31_count / yabunayya_total
    cohort_median_share = 1 / yabunayya_total  # most cohort-surahs have 1 occurrence
    h2_pass = q31_share >= 0.5  # not formally tested, but pre-reg notes it descriptively

    # H3: permutation null
    # Redistribute the yabunayya_total tokens across the 5 cohort surahs proportional to surah-length
    cohort_verse_counts = {s: yabunayya_per_surah[s]['verse_count'] for s in cohort}
    total_cohort_verses = sum(cohort_verse_counts.values())
    cohort_weights = {s: cohort_verse_counts[s] / total_cohort_verses for s in cohort}
    print(f"\nCohort verse-counts: {cohort_verse_counts}")
    print(f"Cohort weights (length-proportional): {cohort_weights}")
    print(f"Q 31 expected count under uniform-density null: {cohort_weights[31] * yabunayya_total:.3f}")

    perm_q31_densities = []
    cohort_keys = list(cohort)
    weights = [cohort_weights[s] for s in cohort_keys]
    for _ in range(N_PERM):
        # Distribute yabunayya_total tokens to cohort surahs by weights (multinomial)
        # Each token chooses a surah with prob = weight
        counts = {s: 0 for s in cohort}
        for _ in range(yabunayya_total):
            chosen = rng.choices(cohort_keys, weights=weights, k=1)[0]
            counts[chosen] += 1
        perm_q31_density = counts[31] / yabunayya_per_surah[31]['verse_count']
        perm_q31_densities.append(perm_q31_density)

    # One-tailed p: P(perm density ≥ observed)
    p_one_tailed = sum(1 for d in perm_q31_densities if d >= q31_density) / N_PERM
    print(f"\nObserved Q 31 density: {q31_density:.4f}")
    print(f"Permutation null mean: {sum(perm_q31_densities)/len(perm_q31_densities):.4f}")
    print(f"Permutation null max: {max(perm_q31_densities):.4f}")
    print(f"One-tailed permutation p (observed ≥ perm): {p_one_tailed:.4f}")

    # Verdict
    alpha_bon = 0.025
    h3_pass = p_one_tailed < alpha_bon

    if h1_pass and h3_pass:
        verdict = 'PASS-DIRECTED (post-hoc origin disclosed)'
    elif h1_pass:
        verdict = 'DIRECTIONAL (rank=1, but perm-p ≥ α_bon)'
    else:
        verdict = 'NULL'

    result = {
        'test_id': 'Q031-F-01',
        'title': 'Q 31 yā-bunayya density vs cohort',
        'pre_reg_sha256': sha,
        'pre_reg_sha_expected': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'corpus_total_yabunayya_tokens': yabunayya_total,
        'cohort_surahs': cohort,
        'cohort_data': yabunayya_per_surah,
        'q31_density': q31_density,
        'q31_count': q31_count,
        'q31_rank_in_cohort': q31_rank,
        'q31_share_of_corpus': q31_share,
        'cohort_density_ranking': [{'surah': s, 'density': d} for s, d in densities],
        'h1_rank_eq_1': h1_pass,
        'h2_share_ge_50pct': h2_pass,
        'h3_perm_p_lt_alpha_bon': h3_pass,
        'perm_p_one_tailed': p_one_tailed,
        'perm_null_mean': sum(perm_q31_densities) / len(perm_q31_densities),
        'perm_null_max': max(perm_q31_densities),
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
