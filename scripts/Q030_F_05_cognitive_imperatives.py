#!/usr/bin/env python3
"""Q030-F-05 — Q 30 cognitive-imperative interrogative density.

Pre-reg: surahs/Q030-al-rum/Q030-F-05-cognitive-imperatives-prereg.md
Pre-reg SHA256: 850b16e6a4c5fee4e4d2828a3bf1da4c149798625cc933c9ae22b722a5608111
Rules-tuple: (no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, hafs-kufan, mashriqi)
"""
import json, re, hashlib, sys, os

PREREG = '/Users/grey/Downloads/quran/surahs/Q030-al-rum/Q030-F-05-cognitive-imperatives-prereg.md'
EXPECTED_SHA = '850b16e6a4c5fee4e4d2828a3bf1da4c149798625cc933c9ae22b722a5608111'
QURAN = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'

PATTERNS = [
    r'أفلا\s+يتفكرون', r'أفلا\s+تتفكرون',
    r'أفلا\s+يعقلون', r'أفلا\s+تعقلون',
    r'أفلا\s+يسمعون', r'أفلا\s+تسمعون',
    r'أفلا\s+يبصرون', r'أفلا\s+تبصرون',
    r'أفلا\s+ينظرون', r'أفلا\s+تنظرون',
    r'\bيتفكرون\b', r'\bتتفكرون\b',
    r'\bيعقلون\b', r'\bتعقلون\b',
    r'لا\s+يعقلون', r'لا\s+يتفكرون',
]


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    pat = re.compile('|'.join(PATTERNS))
    d = json.load(open(QURAN))
    results = []
    for s in d:
        nm = 0
        nw = 0
        for v in s['verses']:
            t = v['text']
            nw += len(t.split())
            nm += len(pat.findall(t))
        results.append({
            'surah': s['id'],
            'name': s.get('transliteration', ''),
            'cog_count': nm,
            'words': nw,
            'cog_rate_per_1000': (nm / nw * 1000) if nw else 0,
        })

    sorted_rate = sorted(results, key=lambda x: -x['cog_rate_per_1000'])
    sorted_count = sorted(results, key=lambda x: -x['cog_count'])

    q30 = next(r for r in results if r['surah'] == 30)
    q29 = next(r for r in results if r['surah'] == 29)
    rank30_rate = sorted_rate.index(q30) + 1
    rank30_count = sorted_count.index(q30) + 1
    rank29_rate = sorted_rate.index(q29) + 1
    rank29_count = sorted_count.index(q29) + 1

    if rank30_rate <= 3:
        verdict = 'PASS-DIRECTED'
    elif rank30_rate <= 10:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q030-F-05',
        'prereg_sha': EXPECTED_SHA,
        'patterns': PATTERNS,
        'all_surahs': results,
        'top_15_by_rate': sorted_rate[:15],
        'q30_rank_rate': rank30_rate,
        'q30_rank_count': rank30_count,
        'q29_rank_rate': rank29_rate,
        'q29_rank_count': rank29_count,
        'q30_cog_rate_per_1000': q30['cog_rate_per_1000'],
        'q30_cog_count': q30['cog_count'],
        'verdict': verdict,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q030-al-rum/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q030-al-rum/csv/Q030-F-05.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q030-F-05 results:")
    print(f"  Q 30: rate={q30['cog_rate_per_1000']:.3f}/1000, count={q30['cog_count']}")
    print(f"  Q 30 rank by rate: {rank30_rate}/114")
    print(f"  Q 29 rank by rate: {rank29_rate}/114")
    print(f"  Top 5 by rate:")
    for r in sorted_rate[:5]:
        print(f"    Q{r['surah']:03d}  rate={r['cog_rate_per_1000']:.3f}  count={r['cog_count']}  words={r['words']}")
    print(f"  Verdict: {verdict}")


if __name__ == '__main__':
    main()
