#!/usr/bin/env python3
"""
Q049-F-01 — yā-ayyuhā-alladhīna-āmanū density test.
Pre-reg SHA: a5f2d8483f4ecddd820bf9565f7e92011ca3959d061afb13d1570d4025261a8a
Direction: POSITIVE — Q 49 hypothesized to be rank-1 of 95 surahs (verse-count ≥ 10).
Seed: 20260509  (deterministic; no random component required).
"""

import json
import os
import hashlib

ROOT = '/Users/grey/Downloads/quran'
TARGET_PATTERN = 'يا أيها الذين آمنوا'
TARGET_PATTERN_ALNAS = 'يا أيها الناس'
MARKS = ['ۖ', 'ۚ', 'ۗ', 'ۘ', 'ۙ', 'ۛ', 'ۜ', '۞', 'ۤ']
PRE_REG_SHA = 'a5f2d8483f4ecddd820bf9565f7e92011ca3959d061afb13d1570d4025261a8a'

MEDINAN = {2,3,4,5,8,9,22,24,33,47,48,49,55,57,58,59,60,61,62,63,64,65,66,76,98,99,110}


def strip_marks(text):
    for m in MARKS:
        text = text.replace(m, '')
    return text


def main():
    data = json.load(open(os.path.join(ROOT, 'quran-text', 'quran-no-tashkeel.json')))

    per_surah = []
    total_amanu = 0
    medinan_amanu = 0

    for s in data:
        sid = s['id']
        verses = s['verses']
        nv = len(verses)
        cnt_amanu = 0
        cnt_alnas = 0
        for v in verses:
            text = strip_marks(v['text'])
            if TARGET_PATTERN in text:
                cnt_amanu += 1
            if TARGET_PATTERN_ALNAS in text:
                cnt_alnas += 1
        density = cnt_amanu / nv if nv > 0 else 0.0
        per_surah.append({
            'surah': sid,
            'name': s.get('transliteration', ''),
            'verse_count': nv,
            'amanu_count': cnt_amanu,
            'alnas_count': cnt_alnas,
            'density': density,
            'is_medinan': sid in MEDINAN,
        })
        total_amanu += cnt_amanu
        if sid in MEDINAN:
            medinan_amanu += cnt_amanu

    # Filter to comparator pool (verse-count ≥ 10)
    pool = [r for r in per_surah if r['verse_count'] >= 10]
    pool_sorted = sorted(pool, key=lambda x: -x['density'])

    # Q 49's rank
    q49_rank = next(i for i, r in enumerate(pool_sorted, 1) if r['surah'] == 49)
    q49_entry = pool_sorted[q49_rank - 1]

    # Verdict
    if q49_rank == 1:
        verdict = 'CONFIRMED'
    elif q49_rank == 2:
        verdict = 'PASS-DIRECTED-WEAK'
    elif q49_rank <= 5:
        verdict = 'PARTIAL'
    else:
        verdict = 'NULL'

    # Full corpus density check & medinan-exclusivity
    medinan_only = (total_amanu == medinan_amanu)

    result = {
        'finding_id': 'Q049-F-01',
        'pre_reg_sha256': PRE_REG_SHA,
        'seed': 20260509,
        'rules_tuple': '(no-tashkeel, orthographic-token, exact-substring-after-mark-stripping, basmala-not-counted, Hafs-Kufan, length-control verse-count >= 10)',
        'pattern_amanu': TARGET_PATTERN,
        'pattern_alnas': TARGET_PATTERN_ALNAS,
        'corpus_total_amanu': total_amanu,
        'medinan_total_amanu': medinan_amanu,
        'meccan_total_amanu': total_amanu - medinan_amanu,
        'medinan_only_attestation': medinan_only,
        'q49_amanu_count': q49_entry['amanu_count'],
        'q49_verse_count': q49_entry['verse_count'],
        'q49_density': q49_entry['density'],
        'q49_rank_in_pool': q49_rank,
        'pool_size': len(pool),
        'top10_by_density': pool_sorted[:10],
        'all_amanu_surahs_count': sum(1 for r in per_surah if r['amanu_count'] > 0),
        'verdict': verdict,
    }

    out_path = os.path.join(ROOT, 'surahs', 'Q049-al-hujurat', 'csv', 'Q049-F-01.json')
    with open(out_path, 'w') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f'Q049-F-01 verdict: {verdict}')
    print(f'  Q49 rank in pool (n=95): {q49_rank}')
    print(f'  Q49 amanu count: {q49_entry["amanu_count"]}/{q49_entry["verse_count"]} verses (density={q49_entry["density"]:.4f})')
    print(f'  Corpus total amanu: {total_amanu} ({medinan_amanu} Medinan, {total_amanu - medinan_amanu} Meccan)')
    print(f'  Medinan-exclusivity: {medinan_only}')
    print(f'  Top-5 by density:')
    for i, r in enumerate(pool_sorted[:5], 1):
        print(f'    {i}. Q{r["surah"]:3d} {r["name"]:20s} {r["amanu_count"]}/{r["verse_count"]} = {r["density"]:.4f}')


if __name__ == '__main__':
    main()
