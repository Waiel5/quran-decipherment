#!/usr/bin/env python3
"""
Q031-F-04 — Q 31 divine-name-pair density (laṭīf-khabīr, ʿazīz-ḥakīm, ʿalīm-khabīr).

Pre-reg: surahs/Q031-luqman/preregs/Q031-F-04-divine-name-pair-density-prereg.md
Pre-reg SHA256: 6e7a14d1f704ba323c5fd87fb59ef753d68c5f6f8f55023b9f58fc5a555b05fd
Seed: 20260509
Direction: positive (Q 31 elevated paired-divine-name density vs corpus)
"""
import json
import re
import hashlib
import random
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG_PATH = ROOT / 'surahs/Q031-luqman/preregs/Q031-F-04-divine-name-pair-density-prereg.md'
EXPECTED_SHA = '6e7a14d1f704ba323c5fd87fb59ef753d68c5f6f8f55023b9f58fc5a555b05fd'
OUT_PATH = ROOT / 'surahs/Q031-luqman/csv/Q031-F-04.json'
CORPUS_PATH = ROOT / 'quran-text/quran-no-tashkeel.json'
SEED = 20260509
N_PERM = 10000


def verify_prereg_sha():
    with open(PREREG_PATH, 'rb') as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {sha}")
    return sha


# Divine-name pair definitions: (label, regex_for_name_a, regex_for_name_b)
# Note: lexical-roots in no-tashkeel orthography
PAIRS = [
    ('latif_khabir', r'لطيف', r'خبير'),
    ('aziz_hakim',   r'عزيز', r'حكيم'),
    ('alim_khabir',  r'عليم', r'خبير'),
]


def verse_has_pair(verse_text, pat_a, pat_b):
    return bool(re.search(pat_a, verse_text)) and bool(re.search(pat_b, verse_text))


def main():
    sha = verify_prereg_sha()
    print(f"PRE-REG SHA verified: {sha[:16]}...")

    rng = random.Random(SEED)
    with open(CORPUS_PATH) as f:
        corpus = json.load(f)

    # Build a flat list of (s_id, v_id, text) for all 6,236 verses
    all_verses = []
    for s_idx, surah in enumerate(corpus):
        for v in surah['verses']:
            all_verses.append((s_idx + 1, v['id'], v['text']))
    total_verses = len(all_verses)
    print(f"Total corpus verses: {total_verses}")

    q31_verses = [(s, v, t) for s, v, t in all_verses if s == 31]
    n_q31_verses = len(q31_verses)
    print(f"Q 31 verses: {n_q31_verses}")

    results_per_pair = {}
    for label, pat_a, pat_b in PAIRS:
        # Corpus-wide pair-bearing verses
        all_pair_verses_idx = [
            i for i, (s, v, t) in enumerate(all_verses)
            if verse_has_pair(t, pat_a, pat_b)
        ]
        n_corpus_pairs = len(all_pair_verses_idx)
        # Q 31 specific
        q31_pair_verses = [(s, v, t) for s, v, t in q31_verses if verse_has_pair(t, pat_a, pat_b)]
        n_q31_pair = len(q31_pair_verses)
        density_q31 = n_q31_pair / n_q31_verses
        print(f"\n=== {label} ===")
        print(f"  Corpus pair-bearing verses: {n_corpus_pairs}")
        print(f"  Q 31 pair-bearing verses: {n_q31_pair}")
        for s, v, t in q31_pair_verses:
            print(f"    Q{s}:{v} — {t[:120]}")
        print(f"  Q 31 density: {density_q31:.4f}")

        # Permutation null: 10,000 random 34-verse contiguous windows from any of the 114 surahs
        # (where a surah has ≥34 verses, draw a random 34-verse window starting at some position;
        # for surahs <34 verses, stitch verses from ≥34 verse pool — but pre-reg says contiguous so
        # we'll restrict to surahs with ≥34 verses).
        eligible_surahs = [i for i, sur in enumerate(corpus) if sur['total_verses'] >= 34]
        # For each perm, pick a random eligible surah and a random 34-verse contiguous window inside it.
        perm_densities = []
        for _ in range(N_PERM):
            s_idx = rng.choice(eligible_surahs)
            sur = corpus[s_idx]
            n = sur['total_verses']
            start = rng.randint(0, n - 34)
            window_verses = sur['verses'][start:start + 34]
            cnt = sum(1 for v in window_verses if verse_has_pair(v['text'], pat_a, pat_b))
            perm_densities.append(cnt / 34)

        p_one_tailed = sum(1 for d in perm_densities if d >= density_q31) / N_PERM
        null_mean = sum(perm_densities) / len(perm_densities)
        print(f"  Perm null mean: {null_mean:.4f}")
        print(f"  Perm null max: {max(perm_densities):.4f}")
        print(f"  P(perm ≥ observed): {p_one_tailed:.4f}")

        results_per_pair[label] = {
            'n_corpus_pair_verses': n_corpus_pairs,
            'n_q31_pair_verses': n_q31_pair,
            'q31_pair_verses': [{'surah': s, 'verse': v} for s, v, t in q31_pair_verses],
            'q31_density': density_q31,
            'perm_null_mean': null_mean,
            'perm_null_max': max(perm_densities),
            'perm_p_one_tailed': p_one_tailed,
        }

    alpha_bon = 0.05 / 3
    n_pass_alpha_bon = sum(1 for r in results_per_pair.values() if r['perm_p_one_tailed'] < alpha_bon)
    n_pass_alpha_05 = sum(1 for r in results_per_pair.values() if r['perm_p_one_tailed'] < 0.05)

    if n_pass_alpha_bon >= 1:
        verdict = f'PASS-PRIMARY ({n_pass_alpha_bon}/3 pairs at α_bon={alpha_bon:.4f})'
    elif n_pass_alpha_05 >= 1:
        verdict = f'DIRECTIONAL ({n_pass_alpha_05}/3 pairs at α=0.05 but not α_bon)'
    else:
        verdict = 'NULL (no pair passes α=0.05)'

    result = {
        'test_id': 'Q031-F-04',
        'title': 'Q 31 divine-name-pair density',
        'pre_reg_sha256': sha,
        'pre_reg_sha_expected': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'pairs_tested': [p[0] for p in PAIRS],
        'per_pair_results': results_per_pair,
        'alpha_bon': alpha_bon,
        'bonferroni_k': 3,
        'n_pass_alpha_bon': n_pass_alpha_bon,
        'n_pass_alpha_05': n_pass_alpha_05,
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
