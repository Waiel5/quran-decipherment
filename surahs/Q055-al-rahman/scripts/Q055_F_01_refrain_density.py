#!/usr/bin/env python3
"""
Q055-F-01 — Refrain-density audit.

Hypothesis: The phrase "fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān" recurs
exactly 31 times in Q 55. Q 55 should rank #1 in single-phrase repetition
density across all 114 surahs.

Pre-reg locked: see preregs/Q055-F-01-prereg.md
Direction-of-effect: Q 55 ranks 1st in maximum-repeated-trigram-or-longer
density across the corpus. Counter-direction (Q 55 not in top-3) = NULL.

Rules-tuple: (no-tashkeel, orthographic-token, graphemes,
basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).
Cross-validation: rerun under min-tashkeel and full-tashkeel; expect same count.
"""
import json
import os
import re
import unicodedata
from collections import Counter, defaultdict

ROOT = '/Users/grey/Downloads/quran'
OUT = os.path.join(ROOT, 'surahs/Q055-al-rahman/csv/Q055-F-01.json')


def load_quran(variant):
    path = os.path.join(ROOT, 'quran-text', f'quran-{variant}.json')
    with open(path) as f:
        return json.load(f)


def strip_diacritics(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def normalize_alif(s):
    # Normalize alif variants for cross-tashkeel comparison
    s = re.sub(r'[إأآٱ]', 'ا', s)
    # standalone hamza followed by alif = madda alif (e.g. ءالاء = آلاء)
    s = re.sub(r'ءا', 'ا', s)
    s = re.sub(r'ى', 'ي', s)
    s = re.sub(r'ة', 'ه', s)  # tied taa
    return s


def count_refrain_in_q55(data, variant_name):
    """Locate Q55 and count exact refrain occurrences."""
    q55 = next(s for s in data if s['id'] == 55)
    refrains_norm = []
    matches = []
    # Refrain to test (variant-agnostic core)
    # In no-tashkeel: فبأي آلاء ربكما تكذبان
    # In min/full: فَبِأَيِّ آلَاءِ رَبِّكُمَا تُكَذِّبَانِ
    for v in q55['verses']:
        raw = v['text']
        norm = normalize_alif(strip_diacritics(raw)).strip()
        # All refrain verses are EXACTLY the refrain (not embedded)
        # Accept the normalized form 'فباي الاء ربكما تكذبان'
        if norm == 'فباي الاء ربكما تكذبان' or norm == 'فبي الاء ربكما تكذبان':
            refrains_norm.append(v['id'])
            matches.append((v['id'], raw))
    return refrains_norm, matches, q55


def compute_corpus_max_phrase_repetition():
    """For each surah, find the most-repeated multi-word phrase (length >=4 words)
    and report the count. Use no-tashkeel variant."""
    data = load_quran('no-tashkeel')
    results = {}
    for s in data:
        # All verses' texts joined with verse boundaries
        verses = [normalize_alif(strip_diacritics(v['text'])).strip() for v in s['verses']]
        # Count exact verse-level repetitions
        verse_counter = Counter(verses)
        if verse_counter:
            top_verse, top_count = verse_counter.most_common(1)[0]
        else:
            top_verse, top_count = '', 0
        # Count phrase-level repetitions (4-word phrases)
        phrase_counter = Counter()
        for v in verses:
            tokens = v.split()
            for L in range(4, min(8, len(tokens)+1)):
                for i in range(len(tokens)-L+1):
                    phrase = ' '.join(tokens[i:i+L])
                    phrase_counter[phrase] += 1
        # Find max-count phrase
        if phrase_counter:
            top_phrase, top_phrase_count = phrase_counter.most_common(1)[0]
        else:
            top_phrase, top_phrase_count = '', 0
        results[s['id']] = {
            'name': s['name'],
            'verses': len(verses),
            'top_verse': top_verse,
            'top_verse_count': top_count,
            'top_phrase': top_phrase,
            'top_phrase_count': top_phrase_count,
            'phrase_density_per_verse': top_phrase_count / max(1, len(verses)),
        }
    return results


def main():
    print("=== Q055-F-01: Refrain density audit ===\n")
    out = {'rules_tuple': '(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)'}

    # Cross-validate refrain count across 3 tashkeel variants
    print("[1] Cross-tashkeel refrain count")
    counts = {}
    for variant in ['no-tashkeel', 'min-tashkeel', 'full-tashkeel']:
        data = load_quran(variant)
        refrains, matches, q55 = count_refrain_in_q55(data, variant)
        counts[variant] = len(refrains)
        print(f"  {variant}: {len(refrains)} occurrences")
        if variant == 'no-tashkeel':
            out['refrain_verses'] = refrains
            out['refrain_text_no_tashkeel'] = matches[0][1] if matches else None
        if variant == 'min-tashkeel':
            out['refrain_text_min_tashkeel'] = matches[0][1] if matches else None
        if variant == 'full-tashkeel':
            out['refrain_text_full_tashkeel'] = matches[0][1] if matches else None
    out['refrain_counts_by_variant'] = counts
    out['refrain_count_consistent'] = len(set(counts.values())) == 1
    out['refrain_count'] = counts['no-tashkeel']

    print(f"\n  Cross-variant consistent: {out['refrain_count_consistent']}")
    print(f"  Verified count: {out['refrain_count']}")

    # Corpus-wide phrase repetition ranking
    print("\n[2] Corpus-wide max-phrase repetition")
    res = compute_corpus_max_phrase_repetition()
    # Rank by top_phrase_count
    sorted_phrase = sorted(res.items(), key=lambda x: -x[1]['top_phrase_count'])
    out['top10_phrase_repetition'] = []
    print("  Rank | SurahID | top_phrase_count | top_verse_count | top_phrase")
    for rank, (sid, info) in enumerate(sorted_phrase[:15], 1):
        print(f"  {rank:>4} | Q{sid:03d} | {info['top_phrase_count']:>4} | {info['top_verse_count']:>4} | {info['top_phrase'][:60]}")
        out['top10_phrase_repetition'].append({
            'rank': rank, 'surah': sid, 'name': info['name'],
            'top_phrase_count': info['top_phrase_count'],
            'top_verse_count': info['top_verse_count'],
            'top_phrase': info['top_phrase'],
            'verses': info['verses'],
            'phrase_density': info['phrase_density_per_verse'],
        })

    # Q55 rank
    q55_rank = next(rank for rank, (sid, _) in enumerate(sorted_phrase, 1) if sid == 55)
    out['Q55_phrase_repetition_rank'] = q55_rank
    print(f"\n  Q 55 rank in max-phrase repetition: {q55_rank}/114")

    # Verse-level repetition rank
    sorted_verse = sorted(res.items(), key=lambda x: -x[1]['top_verse_count'])
    q55_verse_rank = next(rank for rank, (sid, _) in enumerate(sorted_verse, 1) if sid == 55)
    out['Q55_verse_repetition_rank'] = q55_verse_rank
    out['top10_verse_repetition'] = [
        {'rank': r, 'surah': sid, 'name': info['name'],
         'top_verse_count': info['top_verse_count'],
         'top_verse': info['top_verse']}
        for r, (sid, info) in enumerate(sorted_verse[:10], 1)
    ]
    print(f"  Q 55 rank in identical-verse repetition: {q55_verse_rank}/114")

    # Verdict
    if out['refrain_count'] == 31 and out['refrain_count_consistent']:
        out['count_verdict'] = 'CONFIRMED — 31-refrain count exact, stable across 3 tashkeel variants'
    elif out['refrain_count_consistent']:
        out['count_verdict'] = f"DIRECTIONAL — count={out['refrain_count']}, stable, but != 31"
    else:
        out['count_verdict'] = 'NULL — count varies by tashkeel variant'

    if q55_rank == 1 and q55_verse_rank == 1:
        out['rank_verdict'] = 'CONFIRMED — Q 55 corpus-#1 in both phrase and verse repetition'
    elif q55_rank <= 3 or q55_verse_rank <= 3:
        out['rank_verdict'] = f'DIRECTIONAL — Q 55 in top-3 (phrase={q55_rank}, verse={q55_verse_rank})'
    else:
        out['rank_verdict'] = f'NULL — Q 55 not top-3 (phrase={q55_rank}, verse={q55_verse_rank})'

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\nWrote: {OUT}")
    print(f"\nFinal: {out['count_verdict']}")
    print(f"       {out['rank_verdict']}")


if __name__ == '__main__':
    main()
