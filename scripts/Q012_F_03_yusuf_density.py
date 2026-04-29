#!/usr/bin/env python3
"""Q012-F-03 — Yūsuf-name token density across the 114 surahs.

Pre-reg: surahs/Q012-yusuf/Q012-F-03-yusuf-token-density-prereg.md
Pre-reg SHA256: 2b05dc7ad5c36b19e7bc42612bf13aec87be3f7775535526ad3605c49ccdb9ee
"""
import json, re, hashlib, sys, os

PREREG = '/Users/grey/Downloads/quran/surahs/Q012-yusuf/Q012-F-03-yusuf-token-density-prereg.md'
EXPECTED_SHA = '2b05dc7ad5c36b19e7bc42612bf13aec87be3f7775535526ad3605c49ccdb9ee'


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    d = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))
    names = {
        'يوسف': 'Yusuf', 'موسى': 'Musa', 'عيسى': 'Isa',
        'إبراهيم': 'Ibrahim', 'يعقوب': 'Yaqub', 'نوح': 'Nuh',
    }
    out_results = {}
    for ar, en in names.items():
        per_surah = []
        for s in d:
            text = ' '.join(v['text'] for v in s['verses'])
            n = len(re.findall(ar, text))
            n_words = len(text.split())
            per_surah.append({'surah': s['id'], 'name': s['transliteration'],
                              'tokens': n, 'n_words': n_words,
                              'density_per_1000': 1000 * n / n_words if n_words else 0})
        total = sum(x['tokens'] for x in per_surah)
        primary = max(per_surah, key=lambda x: x['tokens'])
        concentration = primary['tokens'] / total if total else 0
        out_results[en] = {
            'arabic': ar, 'total_tokens': total, 'primary_surah': primary['surah'],
            'primary_count': primary['tokens'], 'concentration': concentration,
            'per_surah_nonzero': [x for x in per_surah if x['tokens'] > 0],
        }
    out = {
        'finding_id': 'Q012-F-03', 'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, orthographic-exact-match, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'method': 'orthographic-exact-match per surah; concentration = max_count / total',
        'results': out_results,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q012-yusuf/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q012-yusuf/csv/Q012-F-03.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"يوسف: total={out_results['Yusuf']['total_tokens']}, "
          f"Q{out_results['Yusuf']['primary_surah']} = {out_results['Yusuf']['primary_count']}, "
          f"concentration={out_results['Yusuf']['concentration']:.4f}")


if __name__ == '__main__':
    main()
