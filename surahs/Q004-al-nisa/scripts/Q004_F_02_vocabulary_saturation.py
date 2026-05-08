#!/usr/bin/env python3
"""Q004-F-02 — Family-vocabulary saturation rank for Q 4 al-Nisāʾ.

Pre-reg locked at SHA256 f7a99cdb80353c36f5def2624ebd16f2b24ba4c463b8f18413a5d47fc2cef5e7.
"""

import hashlib
import json
import os
import random
import sys

ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(ROOT, 'surahs', 'Q004-al-nisa', 'preregs',
                     'Q004-F-02-nisa-vocabulary-saturation-prereg.md')
EXPECTED_SHA = 'f7a99cdb80353c36f5def2624ebd16f2b24ba4c463b8f18413a5d47fc2cef5e7'
SEED = 20260507
N_PERM = 10000

LEXICON = [
    'النساء', 'نساء', 'نسائكم', 'نساءهن',
    'الزوج', 'الزوجة', 'أزواج', 'أزواجا', 'زوجها',
    'اليتيم', 'اليتامى', 'يتيما', 'يتامى',
    'المهر', 'أجورهن', 'الصداق', 'صدقات',
    'الميراث', 'وارث', 'ورثة',
    'الطلاق', 'طلقتم', 'طلقتموهن', 'طلقها',
    'أمهات', 'بنات', 'أخت', 'أخوات', 'أخ', 'إخوة',
    'أب', 'آباؤكم', 'أمكم', 'أمهاتكم',
]


def sha256_of_file(path: str) -> str:
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def verify_prereg():
    actual = sha256_of_file(PREREG)
    if actual != EXPECTED_SHA:
        sys.exit(f'FATAL: pre-reg SHA mismatch.\n'
                 f'  expected = {EXPECTED_SHA}\n'
                 f'  actual   = {actual}')


def count_lexicon(text: str, lex) -> int:
    return sum(text.count(t) for t in set(lex))


def main():
    verify_prereg()

    with open(os.path.join(ROOT, 'quran-text', 'quran-no-tashkeel.json')) as f:
        quran = json.load(f)

    rows = []
    for surah in quran:
        sid = surah['id']
        text = ' '.join(v['text'] for v in surah['verses'])
        words = len(text.split())
        c = count_lexicon(text, LEXICON)
        rows.append({
            'surah': sid,
            'translit': surah['transliteration'],
            'type': surah['type'],
            'n_verses': surah['total_verses'],
            'n_words': words,
            'count_family_lex': c,
            'density_per_100w': c / words * 100 if words else 0.0,
        })

    by_density = sorted(rows, key=lambda r: -r['density_per_100w'])
    by_count = sorted(rows, key=lambda r: -r['count_family_lex'])
    for rk, r in enumerate(by_density, 1):
        r['rank_density'] = rk
    for rk, r in enumerate(by_count, 1):
        r['rank_count'] = rk

    q4 = next(r for r in rows if r['surah'] == 4)
    q65 = next(r for r in rows if r['surah'] == 65)

    # Permutation null: shuffle counts; how often does Q 4 land at rank 1 by density?
    rng = random.Random(SEED)
    counts = [r['count_family_lex'] for r in rows]
    word_totals = [r['n_words'] for r in rows]
    surahs = [r['surah'] for r in rows]

    perm_q4_ranks = []
    for _ in range(N_PERM):
        shuffled = counts[:]
        rng.shuffle(shuffled)
        densities = [(shuffled[i] / word_totals[i] * 100 if word_totals[i] else 0.0,
                      surahs[i]) for i in range(len(rows))]
        densities.sort(reverse=True)
        ranks = {s: rk for rk, (_, s) in enumerate(densities, 1)}
        perm_q4_ranks.append(ranks[4])

    p_perm = sum(1 for r in perm_q4_ranks if r <= q4['rank_density']) / N_PERM

    summary = {
        'finding_id': 'Q004-F-02',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'lexicon': LEXICON,
        'q4': q4,
        'q65': q65,
        'q4_q65_density_ratio': (q4['density_per_100w'] / q65['density_per_100w']
                                  if q65['density_per_100w'] else None),
        'q4_q65_count_ratio': (q4['count_family_lex'] / q65['count_family_lex']
                                if q65['count_family_lex'] else None),
        'top_10_density': by_density[:10],
        'top_10_count': by_count[:10],
        'permutation_null_p_q4_density_rank_le_observed': p_perm,
        'verdict': ('CONFIRMED' if q4['rank_density'] == 1 and p_perm < 0.01
                    else 'DIRECTIONAL' if q4['rank_density'] <= 5
                    else 'NULL'),
    }

    out_path = os.path.join(ROOT, 'surahs', 'Q004-al-nisa', 'csv',
                            'Q004-F-02-vocabulary-saturation.json')
    with open(out_path, 'w') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f'Q4 family-lex count: {q4["count_family_lex"]}, density: {q4["density_per_100w"]:.4f}')
    print(f'Q4 rank by density: {q4["rank_density"]}/114; rank by count: {q4["rank_count"]}/114')
    print(f'Q65 al-Talaq count: {q65["count_family_lex"]}, density: {q65["density_per_100w"]:.4f}')
    print(f'Top 10 by density:')
    for r in by_density[:10]:
        print(f'  rank {r["rank_density"]:3d}: Q{r["surah"]:3d} {r["translit"]:>15} '
              f'count={r["count_family_lex"]:4d} density={r["density_per_100w"]:.4f}')
    print(f'Top 10 by absolute count:')
    for r in by_count[:10]:
        print(f'  rank {r["rank_count"]:3d}: Q{r["surah"]:3d} {r["translit"]:>15} '
              f'count={r["count_family_lex"]:4d} density={r["density_per_100w"]:.4f}')
    print(f'permutation p: {p_perm:.4f}')
    print(f'verdict: {summary["verdict"]}')
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
