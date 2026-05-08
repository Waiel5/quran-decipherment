#!/usr/bin/env python3
"""Q038-F-02 — Prophet-cycle saturation index across 114 surahs.

Pre-reg: surahs/Q038-sad/Q038-F-02-prophet-saturation-prereg.md
Pre-reg SHA256: afdee0bf62018ff88559d56d9f889bd65ee430772d7425dcd0719e980d2c6eb5
Rules-tuple: (no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import json, re, hashlib, sys, os

PREREG = '/Users/grey/Downloads/quran/surahs/Q038-sad/Q038-F-02-prophet-saturation-prereg.md'
EXPECTED_SHA = 'afdee0bf62018ff88559d56d9f889bd65ee430772d7425dcd0719e980d2c6eb5'

# Canonical 25 prophets named in the Quran. Use no-tashkeel exact-match orthographic forms.
# Word-boundary patterns to catch with optional ل/و/ف/ب prefixes (no shadow shadda since no-tashkeel).
PROPHET_NAMES = [
    'آدم', 'نوح', 'إدريس', 'هود', 'صالح', 'إبراهيم', 'لوط',
    'إسماعيل', 'إسحاق', 'يعقوب', 'يوسف', 'شعيب',
    'أيوب', 'موسى', 'هارون', 'داوود', 'سليمان',
    'إلياس', 'اليسع', 'يونس', 'زكريا', 'يحيى', 'عيسى', 'محمد',
    # Note Quranic orthography: داوود (two waws), يحيى (final yāʾ).
    # Dhū al-Kifl is a 2-token name handled below.
]
# Special multi-token: ذا الكفل / ذي الكفل
DHU_KIFL_PATTERNS = [r'ذا\s+الكفل', r'ذي\s+الكفل']


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    quran = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))

    # Build patterns: each prophet name with optional ل/و/ف/ب/ك prefix; word-boundary.
    # Use \b around each form. With prefixes prepended, we look for both bare and prefixed.
    name_patterns = []
    for name in PROPHET_NAMES:
        # bare-name and prefix-attached forms
        # In Arabic no-tashkeel, prefix attaches as one token: lieu  + name
        # We use a regex that matches name with optional preceding letters (only letters from {ل,و,ف,ب,ك}) at start of word
        pat = r'(?:^|\s)(?:[لوفبك])*' + re.escape(name) + r'(?=\s|$|[،.])'
        name_patterns.append((name, re.compile(pat)))

    dhu_kifl_pats = [re.compile(p) for p in DHU_KIFL_PATTERNS]

    results = []
    for s in quran:
        sid = s['id']
        full_text = ' '.join(v['text'] for v in s['verses'])
        n_words = sum(len(v['text'].split()) for v in s['verses'])
        n_verses = len(s['verses'])

        per_name = {}
        total_hits = 0
        unique_prophets = 0
        for name, pat in name_patterns:
            hits = pat.findall(full_text)
            cnt = len(hits)
            per_name[name] = cnt
            total_hits += cnt
            if cnt > 0:
                unique_prophets += 1
        # Dhu al-Kifl
        dhu_hits = 0
        for pat in dhu_kifl_pats:
            dhu_hits += len(pat.findall(full_text))
        per_name['ذا/ذي الكفل'] = dhu_hits
        if dhu_hits > 0:
            unique_prophets += 1
        total_hits += dhu_hits

        density = (total_hits / n_words * 100) if n_words else 0.0
        results.append({
            'surah': sid,
            'name': s.get('transliteration'),
            'n_verses': n_verses,
            'n_words': n_words,
            'prophet_token_total': total_hits,
            'unique_prophets': unique_prophets,
            'prophet_density_per_100w': density,
            'per_name': {k:v for k,v in per_name.items() if v > 0},
        })

    # Rank by density
    by_density = sorted(results, key=lambda x: -x['prophet_density_per_100w'])
    by_unique = sorted(results, key=lambda x: -x['unique_prophets'])

    # Q38 ranks
    q38_density_rank = next(i for i,r in enumerate(by_density,1) if r['surah']==38)
    q38_unique_rank = next(i for i,r in enumerate(by_unique,1) if r['surah']==38)
    q38_row = next(r for r in results if r['surah']==38)

    print(f"Q38 prophet_density_per_100w: {q38_row['prophet_density_per_100w']:.3f}, rank {q38_density_rank}/114")
    print(f"Q38 unique_prophets: {q38_row['unique_prophets']}, rank {q38_unique_rank}/114")
    print(f"Q38 prophet token total: {q38_row['prophet_token_total']}")
    print(f"Q38 per-name: {q38_row['per_name']}")

    print("\nTop 10 by density:")
    for r in by_density[:10]:
        print(f"  Q{r['surah']:3d} {r['name']:20s} density={r['prophet_density_per_100w']:.3f}, hits={r['prophet_token_total']}, uniq={r['unique_prophets']}, n_v={r['n_verses']}")

    print("\nReference comparison set (Q 7, 11, 21, 26, 37, 38):")
    for sid in [7,11,21,26,37,38,19,12]:
        r = next(x for x in results if x['surah']==sid)
        rk = next(i for i,x in enumerate(by_density,1) if x['surah']==sid)
        print(f"  Q{sid}: density={r['prophet_density_per_100w']:.3f}, rank={rk}/114, uniq={r['unique_prophets']}")

    # Verdict
    if q38_density_rank <= 3:
        verdict = 'CONFIRMED'
    elif q38_density_rank <= 6:
        verdict = 'DIRECTIONAL'
    elif q38_density_rank >= 25:
        verdict = 'NULL'
    else:
        verdict = 'DIRECTIONAL-WEAK'

    out = {
        'finding_id': 'Q038-F-02',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'method': 'prophet_density_per_100w; word-boundary regex on 25 canonical prophet names + ذا/ذي الكفل with optional ل/و/ف/ب/ك prefixes',
        'q38_density_rank': q38_density_rank,
        'q38_unique_rank': q38_unique_rank,
        'q38_row': q38_row,
        'top_10_by_density': by_density[:10],
        'top_10_by_unique_prophets': by_unique[:10],
        'reference_set': {sid: next(x for x in results if x['surah']==sid) for sid in [7,11,12,19,21,26,37,38]},
        'all_surahs': results,
        'verdict': verdict,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q038-sad/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q038-sad/csv/Q038-F-02.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nVerdict: {verdict}")


if __name__ == '__main__':
    main()
