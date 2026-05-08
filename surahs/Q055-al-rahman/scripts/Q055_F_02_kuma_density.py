#!/usr/bin/env python3
"""
Q055-F-02 — Dual-pronoun *kumā* density audit.

Hypothesis: Q 55, owing to its dual-jinn-and-mankind address, has the highest
density of dual-form pronominal suffixes (kumā / hu-mā / hum-ā) in the corpus.

Direction-locked: Q 55 ranks corpus-#1 in dual-pronoun-attached-to-noun density.
Not-top-3 = NULL.

Rules-tuple: (no-tashkeel, orthographic-token, graphemes,
basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).

Method: count dual-pronoun suffix patterns at WORD-FINAL position only:
  -kumā  ـكما (2nd-person-dual)
  -humā  ـهما (3rd-person-dual)
on no-tashkeel orthographic-token level. Density = matches / total_words.
"""
import json, os, re, unicodedata
from collections import Counter

ROOT = '/Users/grey/Downloads/quran'
OUT = os.path.join(ROOT, 'surahs/Q055-al-rahman/csv/Q055-F-02.json')


def strip_diacritics(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def normalize_alif(s):
    s = re.sub(r'[إأآٱ]', 'ا', s)
    s = re.sub(r'ءا', 'ا', s)
    s = re.sub(r'ى', 'ي', s)
    return s


def count_dual_suffixes(text):
    """Count word-final occurrences of -kumā (كما) and -humā (هما)."""
    n = strip_diacritics(text)
    n = normalize_alif(n)
    tokens = n.split()
    kuma = sum(1 for t in tokens if t.endswith('كما') and len(t) > 3)
    huma = sum(1 for t in tokens if t.endswith('هما') and len(t) > 3)
    return kuma, huma, len(tokens)


def main():
    print("=== Q055-F-02: Dual-pronoun kumā / humā density ===\n")
    out = {'rules_tuple': '(no-tashkeel, orthographic-token, graphemes, Hafs-Kufan)'}

    path = os.path.join(ROOT, 'quran-text', 'quran-no-tashkeel.json')
    with open(path) as f:
        data = json.load(f)

    rows = []
    for s in data:
        all_text = ' '.join(v['text'] for v in s['verses'])
        kuma, huma, words = count_dual_suffixes(all_text)
        total = kuma + huma
        rows.append({
            'surah': s['id'],
            'name': s['name'],
            'words': words,
            'kuma_count': kuma,
            'huma_count': huma,
            'dual_total': total,
            'dual_density_per_100w': 100 * total / max(1, words),
            'kuma_density_per_100w': 100 * kuma / max(1, words),
        })

    # Rank by total dual density and by kuma-only density
    by_kuma = sorted(rows, key=lambda r: -r['kuma_density_per_100w'])
    by_total = sorted(rows, key=lambda r: -r['dual_density_per_100w'])

    print(f"{'Rank':>4} | {'Surah':>5} | {'Verses':>4} | {'Words':>4} | {'kumā':>4} | {'humā':>4} | {'kumā/100w':>9}")
    print('-' * 60)
    for r, info in enumerate(by_kuma[:15], 1):
        print(f"{r:>4} | Q{info['surah']:03d} | {next(s['total_verses'] for s in data if s['id']==info['surah']):>4} | {info['words']:>4} | {info['kuma_count']:>4} | {info['huma_count']:>4} | {info['kuma_density_per_100w']:>9.2f}")

    q55_kuma_rank = next(i+1 for i, x in enumerate(by_kuma) if x['surah']==55)
    q55_total_rank = next(i+1 for i, x in enumerate(by_total) if x['surah']==55)
    q55 = next(r for r in rows if r['surah']==55)

    print(f"\nQ 55 kumā-density rank:   {q55_kuma_rank}/114")
    print(f"Q 55 dual-total rank:     {q55_total_rank}/114")
    print(f"Q 55 kumā count: {q55['kuma_count']}, humā count: {q55['huma_count']}")
    print(f"Q 55 kumā density: {q55['kuma_density_per_100w']:.2f}/100words")

    out['q55_metrics'] = q55
    out['q55_kuma_rank'] = q55_kuma_rank
    out['q55_dual_total_rank'] = q55_total_rank
    out['top10_by_kuma'] = by_kuma[:10]
    out['top10_by_dual_total'] = by_total[:10]

    if q55_kuma_rank == 1:
        out['verdict'] = 'CONFIRMED — Q 55 corpus-#1 in kumā density'
    elif q55_kuma_rank <= 3:
        out['verdict'] = f'DIRECTIONAL — Q 55 in top-3 (rank={q55_kuma_rank})'
    else:
        out['verdict'] = f'NULL — Q 55 not in top-3 (rank={q55_kuma_rank})'

    print(f"\nVerdict: {out['verdict']}")

    with open(OUT, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"Wrote: {OUT}")


if __name__ == '__main__':
    main()
