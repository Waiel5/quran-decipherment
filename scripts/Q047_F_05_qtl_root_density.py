#!/usr/bin/env python3
"""
Q047-F-05 — Q 47 qitāl-root (qtl) density per 1000 words; corpus rank.

Pre-reg: /Users/grey/Downloads/quran/surahs/Q047-muhammad/Q047-F-05-qtl-root-density-prereg.md
Pre-reg SHA256: 252b11f712566aeb4a345abd759d14c9d4b8b2a4561ae234b369e3f528070005

Rules-tuple: (no-tashkeel, QAC-stem-root, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""

import json
import hashlib
import sys
import re
from pathlib import Path
from collections import Counter

PROJECT = Path('/Users/grey/Downloads/quran')
PREREG = PROJECT / 'surahs/Q047-muhammad/Q047-F-05-qtl-root-density-prereg.md'
EXPECTED_SHA = '252b11f712566aeb4a345abd759d14c9d4b8b2a4561ae234b369e3f528070005'
OUT = PROJECT / 'surahs/Q047-muhammad/csv/Q047-F-05.json'
SEED = 20260509

PAUSE_MARKERS = ['ۚ', 'ۖ', 'ۗ', 'ۙ', 'ۘ', 'ۛ', 'ۜ']


def verify_prereg_sha():
    with open(PREREG, 'rb') as f:
        h = hashlib.sha256(f.read()).hexdigest()
    if h != EXPECTED_SHA:
        sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {h}')
    print(f'[OK] pre-reg SHA verified: {h}')


def surah_word_count(verses):
    n = 0
    for v in verses:
        text = v['text']
        for c in PAUSE_MARKERS:
            text = text.replace(c, ' ')
        text = re.sub(r'\s+', ' ', text).strip()
        n += len([t for t in text.split() if t])
    return n


def main():
    verify_prereg_sha()
    with open(PROJECT / 'quran-text/quran-no-tashkeel.json', encoding='utf-8') as f:
        q = json.load(f)
    with open(PROJECT / 'data/morphology/root-index.json', encoding='utf-8') as f:
        rix = json.load(f)

    if 'qtl' not in rix:
        sys.exit('qtl root not found in QAC root-index.json')

    qtl_attests = rix['qtl']
    sur_counts = Counter()
    for s, v, w in qtl_attests:
        sur_counts[s] += 1

    surah_words = {s['id']: surah_word_count(s['verses']) for s in q}

    rates = []
    for sid in range(1, 115):
        c = sur_counts.get(sid, 0)
        w = surah_words[sid]
        rate = (c / w * 1000) if w > 0 else 0.0
        rates.append({'surah': sid, 'qtl_count': c, 'words': w, 'rate_per_1000w': rate})

    rates_sorted = sorted(rates, key=lambda x: -x['rate_per_1000w'])
    q47 = next(r for r in rates if r['surah'] == 47)
    q47_rank = next(i for i, r in enumerate(rates_sorted, 1) if r['surah'] == 47)
    top10 = rates_sorted[:10]

    if q47_rank <= 3:
        verdict = 'VINDICATED'
    elif q47_rank <= 10:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    # Also compute the rate with min-count >= 3 filter (MW-3 alternative model, REPORTED, not pre-registered)
    filt = [r for r in rates if r['qtl_count'] >= 3]
    filt_sorted = sorted(filt, key=lambda x: -x['rate_per_1000w'])
    q47_in_filt = q47['qtl_count'] >= 3
    q47_filt_rank = None
    if q47_in_filt:
        q47_filt_rank = next(i for i, r in enumerate(filt_sorted, 1) if r['surah'] == 47)
    abs_sorted = sorted(rates, key=lambda x: -x['qtl_count'])
    q47_abs_rank = next(i for i, r in enumerate(abs_sorted, 1) if r['surah'] == 47)

    out = {
        'test_id': 'Q047-F-05',
        'pre_reg_sha': EXPECTED_SHA,
        'seed': SEED,
        'rules_tuple': '(no-tashkeel, QAC-stem-root, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'root': 'qtl',
        'corpus_total_qtl_attestations': len(qtl_attests),
        'corpus_total_words': sum(surah_words.values()),
        'corpus_mean_rate_per_1000w': len(qtl_attests) / sum(surah_words.values()) * 1000,
        'Q47_record': q47,
        'Q47_rank_per_1000w': q47_rank,
        'top_10_per_1000w': top10,
        'mw3_alternative_min_count_3': {
            'Q47_in_filtered_set': q47_in_filt,
            'Q47_rank_in_filtered_set': q47_filt_rank,
            'filtered_set_size': len(filt),
            'top_10_min3': filt_sorted[:10],
        },
        'mw3_alternative_absolute_count': {
            'Q47_rank_absolute': q47_abs_rank,
            'top_10_absolute': abs_sorted[:10],
        },
        'verdict': verdict,
        'bonferroni_k': 1,
        'alpha_bon': 0.05,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f'[OK] wrote {OUT}')
    print(f'  Q 47: {q47}')
    print(f'  Q 47 rank per-1000w: {q47_rank}')
    print(f'  Q 47 rank (min-3 filter): {q47_filt_rank} (in_set={q47_in_filt})')
    print(f'  Q 47 rank (absolute count): {q47_abs_rank}')
    print(f'  Verdict: {verdict}')


if __name__ == '__main__':
    main()
