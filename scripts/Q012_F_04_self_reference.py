#!/usr/bin/env python3
"""Q012-F-04 — Q 12:3 aḥsan al-qaṣaṣ self-reference position test.

Pre-reg: surahs/Q012-yusuf/Q012-F-04-self-reference-position-prereg.md
Pre-reg SHA256: 5a261537b66c8cd7f139b482015661065e9fabb7a7a974889223205844861304
"""
import json, re, hashlib, sys, os

PREREG = '/Users/grey/Downloads/quran/surahs/Q012-yusuf/Q012-F-04-self-reference-position-prereg.md'
EXPECTED_SHA = '5a261537b66c8cd7f139b482015661065e9fabb7a7a974889223205844861304'


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL SHA", file=sys.stderr); sys.exit(1)


def main():
    verify_sha()
    d = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))
    # H1.a — phrase uniqueness
    phrase_hits = []
    for s in d:
        for v in s['verses']:
            if 'أحسن القصص' in v['text']:
                phrase_hits.append({'surah': s['id'], 'verse': v['id'], 'text': v['text']})

    # H1.b — root q-s-s in Q12
    q12 = d[11]
    qss_pat = re.compile(r'(نقص|قصص|قصصت|قصصنا|تقصص|قصة|اقصص)')
    qss_in_q12 = []
    for v in q12['verses']:
        if qss_pat.search(v['text']):
            qss_in_q12.append({'verse': v['id'], 'text': v['text'][:200],
                               'position_pct': v['id'] / 111.0 * 100})
    head_hits = [x for x in qss_in_q12 if x['verse'] <= 6]
    tail_hits = [x for x in qss_in_q12 if x['verse'] >= 106]

    out = {
        'finding_id': 'Q012-F-04', 'prereg_sha': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, orthographic-token, whitespace-tokenized, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'phrase_hits': phrase_hits,
        'phrase_uniqueness_confirmed': len(phrase_hits) == 1 and phrase_hits[0]['surah'] == 12 and phrase_hits[0]['verse'] == 3,
        'qss_in_q12': qss_in_q12,
        'head_zone_hits': head_hits,
        'tail_zone_hits': tail_hits,
        'head_tail_framing_confirmed': len(head_hits) > 0 and len(tail_hits) > 0,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q012-yusuf/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q012-yusuf/csv/Q012-F-04.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"phrase uniqueness: {out['phrase_uniqueness_confirmed']}")
    print(f"head-tail framing: {out['head_tail_framing_confirmed']}")


if __name__ == '__main__':
    main()
