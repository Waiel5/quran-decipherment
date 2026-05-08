#!/usr/bin/env python3
"""
Q056-F-04 — Cosmic-time-marker density across 114 surahs.
SHA-locked pre-reg: 662f6b175d98c43c73495ecedd5a0ce6c6942810e49bde2d0d67506d9a6f7d27
"""
import json, hashlib, re, os

PREREG = '/Users/grey/Downloads/quran/surahs/Q056-al-waqia/preregs/Q056-F-04-cosmic-time-marker-prereg.md'
EXPECTED_SHA = '662f6b175d98c43c73495ecedd5a0ce6c6942810e49bde2d0d67506d9a6f7d27'
with open(PREREG,'rb') as f:
    actual = hashlib.sha256(f.read()).hexdigest()
assert actual == EXPECTED_SHA, f'SHA mismatch: {actual}'

with open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json') as f:
    Q = json.load(f)

# Pre-committed cosmic-time-marker tokens (orthographic, no-tashkeel)
COSMIC = {'النجم','النجوم','نجم','نجوم','موقع','مواقع','الشمس','شمس',
          'القمر','قمر','الفلك','فلك','البروج','برج','بمواقع'}

# Strip ornament markers (presentation detail; pre-reg garden-of-forking-paths note in F-03 applies)
ORNAMENT = re.compile(r'[۞ۚۖۗۘۙۛ]')

per_surah = []
for s in Q:
    sid = s['id']; name = s['name']
    total_words = 0
    cosmic_count = 0
    for v in s['verses']:
        text = ORNAMENT.sub('', v['text'])
        toks = text.split()
        total_words += len(toks)
        cosmic_count += sum(1 for t in toks if t in COSMIC)
    density = (cosmic_count/total_words)*100 if total_words > 0 else 0.0
    per_surah.append({'surah': sid, 'name': name, 'cosmic_count': cosmic_count,
                      'total_words': total_words, 'density_per_100': density})

# Rank by density
ranked = sorted(per_surah, key=lambda x: -x['density_per_100'])
print('Top-10 by cosmic-time-marker density (per 100 words):')
for i, r in enumerate(ranked[:15], 1):
    print(f"  rank {i}: Q{r['surah']:3d} ({r['name']}): count={r['cosmic_count']}, words={r['total_words']}, density={r['density_per_100']:.3f}%")

q56 = next(r for r in per_surah if r['surah']==56)
q56_rank = next(i for i, r in enumerate(ranked, 1) if r['surah']==56)
print(f'\nQ56 al-Waqiʿa: count={q56["cosmic_count"]}, words={q56["total_words"]}, density={q56["density_per_100"]:.3f}%')
print(f'Q56 RANK: {q56_rank}/114')

# Also report Q53, Q85 (named cosmic surahs) and absolute count rankings
print('\nReference points:')
for sid in [53, 56, 85, 91, 81, 84, 86]:
    r = next(p for p in per_surah if p['surah']==sid)
    rank = next(i for i, p in enumerate(ranked, 1) if p['surah']==sid)
    print(f'  Q{sid}: count={r["cosmic_count"]}, density={r["density_per_100"]:.3f}%, rank={rank}')

# Absolute count
ranked_abs = sorted(per_surah, key=lambda x: -x['cosmic_count'])
print('\nTop-10 by absolute cosmic-token count:')
for i, r in enumerate(ranked_abs[:10], 1):
    print(f"  rank {i}: Q{r['surah']:3d}: count={r['cosmic_count']}, density={r['density_per_100']:.3f}%")

verdict = 'VINDICATED' if q56_rank <= 5 else 'NULL'
print(f'\nVERDICT: {verdict} (pre-reg: Q56 rank ≤ 5 by density)')

result = {
    'test_id': 'Q056-F-04',
    'prereg_sha': EXPECTED_SHA,
    'cosmic_token_set': sorted(COSMIC),
    'q56_count': q56['cosmic_count'],
    'q56_total_words': q56['total_words'],
    'q56_density_per_100': q56['density_per_100'],
    'q56_density_rank': q56_rank,
    'top_10_density': ranked[:10],
    'top_10_absolute': ranked_abs[:10],
    'reference_points': {f'Q{s}': {
        'count': next(p for p in per_surah if p['surah']==s)['cosmic_count'],
        'density': next(p for p in per_surah if p['surah']==s)['density_per_100'],
        'rank': next(i for i,p in enumerate(ranked, 1) if p['surah']==s)
    } for s in [53,56,85,91,81,84,86]},
    'verdict': verdict,
}
OUT = '/Users/grey/Downloads/quran/surahs/Q056-al-waqia/csv/Q056-F-04.json'
with open(OUT,'w') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print(f'Wrote {OUT}')
