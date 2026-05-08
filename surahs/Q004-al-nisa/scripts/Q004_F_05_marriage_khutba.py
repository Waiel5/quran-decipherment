#!/usr/bin/env python3
"""Q004-F-05 — Q 4:1 marriage-khutba liturgical citation distinctness.

Pre-reg locked at SHA256 51f1141498ac823f24f2296f397e071aef0ee6f0331e5ab164df7831fa669179.
"""

import hashlib
import json
import os
import re
import sys

ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(ROOT, 'surahs', 'Q004-al-nisa', 'preregs',
                     'Q004-F-05-marriage-khutba-prereg.md')
EXPECTED_SHA = '51f1141498ac823f24f2296f397e071aef0ee6f0331e5ab164df7831fa669179'
SEED = 20260507

HADITH_DIR = os.path.join(ROOT, 'data', 'literature', 'hadith',
                          'ahmedbaset-json', 'db', 'by_book', 'the_9_books')

# Distinctive phrases (locked in pre-reg)
PROBES = {
    'Q4:1':   'يا أيها الناس اتقوا ربكم الذي خلقكم من نفس واحدة',
    'Q1:1':   'الحمد لله رب العالمين',
    'Q2:255': 'الله لا إله إلا هو الحي القيوم',
    'Q2:284': 'لله ما في السماوات وما في الأرض',
    'Q36:1':  'يس',
    'Q112:1': 'قل هو الله أحد',
    'Q4:11':  'يوصيكم الله في أولادكم',
    'Q4:43':  'لا تقربوا الصلاة وأنتم سكارى',
    'Q4:148': 'لا يحب الله الجهر بالسوء',
    'Q4:176': 'يستفتونك قل الله يفتيكم في الكلالة',
    'Q113:1': 'قل أعوذ برب الفلق',
    'Q114:1': 'قل أعوذ برب الناس',
}

# Khawatim subset (per pre-reg) - used for {non-khawātim} ranking
KHAWATIM = {'Q1:1', 'Q2:255', 'Q2:284', 'Q36:1', 'Q112:1', 'Q113:1', 'Q114:1'}


PAUSE_MARKS = 'ۖۗۘۙۚۛۜ۝۞ۣ۟۠ۡۢۤۥۦۧۨ۩۪ۭ۫۬'
TASHKEEL = 'ًٌٍَُِّْٰٕٖٓٔٗ٘ۖۗۘۙۚۛۜ'


def sha256_of_file(path: str) -> str:
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def verify_prereg():
    actual = sha256_of_file(PREREG)
    if actual != EXPECTED_SHA:
        sys.exit(f'FATAL: pre-reg SHA mismatch.\n'
                 f'  expected = {EXPECTED_SHA}\n'
                 f'  actual   = {actual}')


def strip(text: str) -> str:
    if not isinstance(text, str):
        return ''
    for ch in PAUSE_MARKS + TASHKEEL:
        text = text.replace(ch, '')
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def iter_hadith_texts(book_path: str):
    with open(book_path) as f:
        data = json.load(f)
    if isinstance(data, dict):
        # Try common shapes
        if 'hadiths' in data:
            for h in data['hadiths']:
                yield h
        else:
            # nested chapters
            for v in data.values():
                if isinstance(v, list):
                    for h in v:
                        yield h
    elif isinstance(data, list):
        for h in data:
            yield h


def hadith_arabic(h):
    if not isinstance(h, dict):
        return ''
    # Try standard keys
    for k in ('arabic', 'matn', 'text_ar', 'text', 'hadith_arabic'):
        v = h.get(k)
        if isinstance(v, str) and v.strip():
            return v
    return ''


def main():
    verify_prereg()

    books = []
    for fn in sorted(os.listdir(HADITH_DIR)):
        if fn.endswith('.json'):
            books.append((fn[:-5], os.path.join(HADITH_DIR, fn)))

    # Pre-load all hadith arabic texts (stripped)
    print('Loading hadith corpora...')
    book_texts = {}
    n_total = 0
    for name, path in books:
        texts = []
        for h in iter_hadith_texts(path):
            t = strip(hadith_arabic(h))
            if t:
                texts.append(t)
        book_texts[name] = texts
        n_total += len(texts)
        print(f'  {name}: {len(texts)} hadith')
    print(f'  total: {n_total}')

    # Strip probes the same way
    probes_stripped = {k: strip(v) for k, v in PROBES.items()}

    # Count occurrences per probe per book
    results = {}
    for label, probe in probes_stripped.items():
        per_book = {}
        total = 0
        for name, texts in book_texts.items():
            c = sum(t.count(probe) for t in texts)
            per_book[name] = c
            total += c
        results[label] = {'probe': probe, 'per_book': per_book, 'total': total}

    # Rank
    by_total = sorted(results.items(), key=lambda kv: -kv[1]['total'])
    rank_all = {label: i + 1 for i, (label, _) in enumerate(by_total)}
    non_kh = [(label, info) for label, info in by_total if label not in KHAWATIM]
    rank_non_khawatim = {label: i + 1 for i, (label, _) in enumerate(non_kh)}

    q4_1_total = results['Q4:1']['total']
    q4_1_rank_all = rank_all['Q4:1']
    q4_1_rank_non_kh = rank_non_khawatim.get('Q4:1', None)

    summary = {
        'finding_id': 'Q004-F-05',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'hadith_corpus': '9-books (ahmedbaset-json)',
        'total_hadith_loaded': n_total,
        'probes': PROBES,
        'khawatim_excluded': sorted(KHAWATIM),
        'results': results,
        'rank_all': rank_all,
        'rank_non_khawatim': rank_non_khawatim,
        'q4_1': {
            'total_citations': q4_1_total,
            'rank_all': q4_1_rank_all,
            'rank_non_khawatim': q4_1_rank_non_kh,
        },
        'verdict': ('CONFIRMED' if q4_1_rank_non_kh and q4_1_rank_non_kh <= 5
                    else 'DIRECTIONAL' if q4_1_rank_non_kh and q4_1_rank_non_kh <= 10
                    else 'NULL'),
    }

    out_path = os.path.join(ROOT, 'surahs', 'Q004-al-nisa', 'csv',
                            'Q004-F-05-marriage-khutba.json')
    with open(out_path, 'w') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f'\nProbe citation totals (across 9 books):')
    for label, info in by_total:
        kh = ' [khawātim]' if label in KHAWATIM else ''
        rk_nk = rank_non_khawatim.get(label)
        rk_nk_s = f' (non-kh rank {rk_nk})' if rk_nk else ''
        print(f'  {label}: {info["total"]:5d}{kh}{rk_nk_s}')

    print(f'\nQ4:1 total: {q4_1_total}; rank-all: {q4_1_rank_all}; rank-non-khawātim: {q4_1_rank_non_kh}')
    print(f'verdict: {summary["verdict"]}')
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
