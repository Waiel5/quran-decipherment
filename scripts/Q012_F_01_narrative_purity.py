#!/usr/bin/env python3
"""Q012-F-01 — Narrative-purity index across the 114 surahs.

Pre-reg: surahs/Q012-yusuf/Q012-F-01-narrative-purity-prereg.md
Pre-reg SHA256: b96658f95ad18cb0934660ac34a89f5ea587657aff9d43241b679891bf170e1b
Rules-tuple: (no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import json, re, hashlib, sys, os

PREREG = '/Users/grey/Downloads/quran/surahs/Q012-yusuf/Q012-F-01-narrative-purity-prereg.md'
EXPECTED_SHA = 'b96658f95ad18cb0934660ac34a89f5ea587657aff9d43241b679891bf170e1b'


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    markers = [
        r'\bقال\b', r'\bقالت\b', r'\bقالوا\b', r'\bقلنا\b', r'\bقل\b',
        r'\bفلما\b', r'\bولما\b',
        r'\bإذ\b', r'\bإذا\b',
        r'\bثم\b',
        r'\bبينما\b',
        r'\bوكان\b', r'\bكان\b',
        r'\bأرسل', r'\bبعث',
        r'\bجاء\b', r'\bجاءت\b', r'\bجاءوا\b',
        r'\bذهب\b', r'\bذهبوا\b',
        r'\bرأى\b', r'\bرأيت\b', r'\bرأوا\b',
        r'\bأتى\b', r'\bأتوا\b',
    ]
    pat = re.compile('|'.join(markers))
    d = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))
    results = []
    for s in d:
        verses = s['verses']
        n = len(verses)
        n_narr = 0
        n_marker = 0
        n_words = 0
        for v in verses:
            t = v['text']
            words = t.split()
            n_words += len(words)
            m = pat.findall(t)
            if m:
                n_narr += 1
                n_marker += len(m)
        frac = n_narr / n if n else 0
        dens = n_marker / n_words if n_words else 0
        results.append({
            'surah': s['id'], 'name': s['transliteration'], 'n_verses': n,
            'frac_narrative_verses': frac,
            'marker_density_per_word': dens,
            'narrative_purity_score': 0.5 * frac + 0.5 * (dens / 0.30),
        })
    out = {
        'finding_id': 'Q012-F-01',
        'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'method': 'narrative_purity = 0.5*frac_narrative_verses + 0.5*(marker_density/0.30)',
        'markers': markers,
        'results': results,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q012-yusuf/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q012-yusuf/csv/Q012-F-01.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    by_frac = sorted(results, key=lambda x: -x['frac_narrative_verses'])
    print(f"Q12 rank by frac_narrative_verses: {[i for i,r in enumerate(by_frac,1) if r['surah']==12][0]}/114")
    print(f"Q12 frac_narrative_verses: {[r for r in results if r['surah']==12][0]['frac_narrative_verses']:.4f}")


if __name__ == '__main__':
    main()
