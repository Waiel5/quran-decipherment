#!/usr/bin/env python3
"""Q004-F-01 — Legal-density rank for Q 4 al-Nisāʾ.

Pre-reg locked at SHA256 cd73fcb03ba689b854649d8c4992c550372906a12e1f78a30e137a42630953b7.
"""

import hashlib
import json
import os
import random
import sys

ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(ROOT, 'surahs', 'Q004-al-nisa', 'preregs',
                     'Q004-F-01-legal-density-prereg.md')
EXPECTED_SHA = 'cd73fcb03ba689b854649d8c4992c550372906a12e1f78a30e137a42630953b7'
SEED = 20260507
N_PERM = 10000

LEGAL_IMPERATIVES = [
    'لا تأكلوا', 'لا تقتلوا', 'لا تنكحوا', 'لا تقربوا',
    'كتب عليكم', 'حرمت عليكم', 'أحلت لكم',
    'ولا تنكحوا', 'فاكتبوه', 'فليكتب',
    'فللذكر', 'للذكر', 'ليس عليكم', 'أوصاكم',
]

INHERITANCE_FRACTIONS = [
    'النصف', 'نصف', 'الثلث', 'ثلث',
    'الربع', 'ربع', 'الثمن', 'ثمن',
    'السدس', 'سدس', 'الثلثان', 'الثلثين', 'ثلثا',
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


def count_lexicon(text: str, lexicon) -> int:
    n = 0
    for term in set(lexicon):
        n += text.count(term)
    return n


def main():
    verify_prereg()

    with open(os.path.join(ROOT, 'quran-text', 'quran-no-tashkeel.json')) as f:
        quran = json.load(f)

    rows = []
    for surah in quran:
        sid = surah['id']
        text = ' '.join(v['text'] for v in surah['verses'])
        words = len(text.split())
        c_imp = count_lexicon(text, LEGAL_IMPERATIVES)
        c_frac = count_lexicon(text, INHERITANCE_FRACTIONS)
        score = (c_imp + c_frac) / words * 100 if words else 0.0
        rows.append({
            'surah': sid,
            'name_ar': surah['name'],
            'translit': surah['transliteration'],
            'type': surah['type'],
            'n_verses': surah['total_verses'],
            'n_words': words,
            'count_imperatives': c_imp,
            'count_fractions': c_frac,
            'count_total': c_imp + c_frac,
            'density_per_100w': score,
        })

    # Rank (HIGHER = more legal-dense)
    ranked = sorted(rows, key=lambda r: -r['density_per_100w'])
    for rk, r in enumerate(ranked, 1):
        r['rank_density'] = rk

    q4 = next(r for r in rows if r['surah'] == 4)
    q4_rank = q4['rank_density']

    # Permutation null: re-assign per-token "label" to a random surah,
    # rebuild count_total per surah, recompute density and rank.
    # Simplification: shuffle (count_total) values across surahs of equal-or-greater size class.
    # To keep this principled and pre-registered, we permute the count_total values
    # across all 114 surahs (no length matching) and report Q 4's rank distribution.
    rng = random.Random(SEED)
    counts = [r['count_total'] for r in rows]
    word_totals = [r['n_words'] for r in rows]
    surahs = [r['surah'] for r in rows]

    perm_q4_ranks = []
    perm_q4_density_vals = []
    for _ in range(N_PERM):
        shuffled = counts[:]
        rng.shuffle(shuffled)
        densities = [(shuffled[i] / word_totals[i] * 100 if word_totals[i] else 0.0,
                      surahs[i]) for i in range(len(rows))]
        densities.sort(reverse=True)  # higher = better rank
        ranks = {s: rk for rk, (_, s) in enumerate(densities, 1)}
        perm_q4_ranks.append(ranks[4])
        # Q4's permuted density = the count assigned to position 3 / Q4 words
        perm_q4_density_vals.append(shuffled[3] / word_totals[3] * 100)

    # Empirical p: how often does Q4 land at rank ≤ q4_rank under null?
    n_le = sum(1 for r in perm_q4_ranks if r <= q4_rank)
    p_perm = n_le / N_PERM

    # Top 10 + relevant comparators
    summary = {
        'finding_id': 'Q004-F-01',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'bonferroni_k': 5,
        'alpha_bon': 0.01,
        'lexicon_imperatives': LEGAL_IMPERATIVES,
        'lexicon_fractions': INHERITANCE_FRACTIONS,
        'q4': q4,
        'q4_rank_density': q4_rank,
        'q4_observed_density': q4['density_per_100w'],
        'top_10_density': ranked[:10],
        'comparators_legal_medinan': {sid: next(r for r in rows if r['surah'] == sid)
                                       for sid in [2, 3, 4, 5, 9, 24, 33, 58, 60, 65]},
        'permutation_null': {
            'p_rank_le_observed': p_perm,
            'q4_rank_distribution_under_null': {
                'mean_rank': sum(perm_q4_ranks) / N_PERM,
                'median_rank': sorted(perm_q4_ranks)[N_PERM // 2],
                'p10_rank': sorted(perm_q4_ranks)[N_PERM // 10],
                'p90_rank': sorted(perm_q4_ranks)[9 * N_PERM // 10],
            },
            'observed_q4_density_percentile_in_null': sum(
                1 for v in perm_q4_density_vals if v >= q4['density_per_100w']
            ) / N_PERM,
        },
        'verdict': ('CONFIRMED' if q4_rank <= 3 and p_perm < 0.01
                    else 'DIRECTIONAL' if q4_rank <= 6
                    else 'NULL'),
    }

    out_path = os.path.join(ROOT, 'surahs', 'Q004-al-nisa', 'csv',
                            'Q004-F-01-legal-density.json')
    with open(out_path, 'w') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f'Q4 rank (legal density): {q4_rank}/114')
    print(f'Q4 density: {q4["density_per_100w"]:.4f} per 100 words')
    print(f'Top 10:')
    for r in ranked[:10]:
        print(f'  rank {r["rank_density"]:3d}: Q{r["surah"]:3d} {r["translit"]:>15} '
              f'imp={r["count_imperatives"]:3d} frac={r["count_fractions"]:3d} '
              f'density={r["density_per_100w"]:.4f}')
    print(f'permutation p (Q4 rank ≤ {q4_rank} under null): {p_perm:.4f}')
    print(f'verdict: {summary["verdict"]}')
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
