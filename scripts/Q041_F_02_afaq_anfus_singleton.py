#!/usr/bin/env python3
"""Q041-F-02 — Q 41:53 *fī l-āfāqi wa-fī anfusihim*: āfāq corpus-singleton + co-occurrence.

Pre-reg: surahs/Q041-fussilat/preregs/Q041-F-02-afaq-anfus-singleton-prereg.md
Pre-reg SHA256: 786a861ef0f269c422614a511ec1ac35cc2b416b8accbfd1e7188f7469b4488b
Rules-tuple: (no-tashkeel, orthographic-substring, U+0622 alif-madda preserved, U+0623 hamza-alif preserved, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import json
import re
import hashlib
import sys
import os

PREREG = '/Users/grey/Downloads/quran/surahs/Q041-fussilat/preregs/Q041-F-02-afaq-anfus-singleton-prereg.md'
EXPECTED_SHA = '786a861ef0f269c422614a511ec1ac35cc2b416b8accbfd1e7188f7469b4488b'
SEED = 20260509
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q041-fussilat/csv/Q041-F-02.json'
QURAN_PATH = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'

# Patterns (Unicode-locked)
PAT_AFAQ = re.compile('آفاق')  # آفاق
PAT_ANFUS = re.compile('أنفس')  # أنفس
PAT_FULL_COLLOCATION = re.compile('في الآفاق وفي أنفس')  # في الآفاق وفي أنفس


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def main():
    verify_sha()
    quran = json.load(open(QURAN_PATH))

    afaq_hits = []
    anfus_hits = []
    cooc_hits = []
    full_colloc_hits = []

    for s in quran:
        for v in s['verses']:
            has_afaq = bool(PAT_AFAQ.search(v['text']))
            has_anfus = bool(PAT_ANFUS.search(v['text']))
            has_full = bool(PAT_FULL_COLLOCATION.search(v['text']))
            if has_afaq:
                afaq_hits.append({'surah': s['id'], 'verse': v['id'], 'text': v['text']})
            if has_anfus:
                anfus_hits.append({'surah': s['id'], 'verse': v['id']})
            if has_afaq and has_anfus:
                cooc_hits.append({'surah': s['id'], 'verse': v['id'], 'text': v['text']})
            if has_full:
                full_colloc_hits.append({'surah': s['id'], 'verse': v['id'], 'text': v['text']})

    # H1: āfāq corpus-singleton at Q 41:53
    h1_count = len(afaq_hits)
    h1_at_q41_53 = (h1_count == 1 and afaq_hits[0]['surah'] == 41 and afaq_hits[0]['verse'] == 53)
    h1_pass = h1_at_q41_53

    # H2: āfāq × anfus co-occurrence singleton at Q 41:53
    h2_count = len(cooc_hits)
    h2_at_q41_53 = (h2_count == 1 and cooc_hits[0]['surah'] == 41 and cooc_hits[0]['verse'] == 53)
    h2_pass = h2_at_q41_53

    # H3: full collocation singleton at Q 41:53
    h3_count = len(full_colloc_hits)
    h3_at_q41_53 = (h3_count == 1 and full_colloc_hits[0]['surah'] == 41 and full_colloc_hits[0]['verse'] == 53)
    h3_pass = h3_at_q41_53

    # Bonferroni-corrected alpha for k=3
    alpha_bonf = 0.05 / 3

    # Aggregate verdict
    n_pass = sum([h1_pass, h2_pass, h3_pass])
    if n_pass == 3:
        verdict = 'VINDICATED'
    elif n_pass >= 1:
        verdict = 'PARTIAL'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q041-F-02',
        'pre_reg_sha256': EXPECTED_SHA,
        'seed': SEED,
        'rules_tuple': '(no-tashkeel, orthographic-substring, U+0622 alif-madda preserved, U+0623 hamza-alif preserved, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'patterns': {
            'afaq': '\\u0622\\u0641\\u0627\\u0642 (آفاق)',
            'anfus': '\\u0623\\u0646\\u0641\\u0633 (أنفس)',
            'full_collocation': 'في الآفاق وفي أنفس',
        },
        'h1_afaq_corpus_singleton': {
            'pass': h1_pass,
            'count': h1_count,
            'attestations': afaq_hits,
            'at_q41_53': h1_at_q41_53,
        },
        'h2_afaq_anfus_cooccurrence_singleton': {
            'pass': h2_pass,
            'count': h2_count,
            'attestations': cooc_hits,
            'at_q41_53': h2_at_q41_53,
        },
        'h3_full_collocation_singleton': {
            'pass': h3_pass,
            'count': h3_count,
            'attestations': full_colloc_hits,
            'at_q41_53': h3_at_q41_53,
        },
        'anfus_summary': {
            'total_anfus_verses_corpus': len(anfus_hits),
            'note': 'anfus is corpus-common; āfāq is hapax. The COMBINATION is the unique feature.',
        },
        'bonferroni_alpha': alpha_bonf,
        'n_subhypotheses_pass': n_pass,
        'verdict': verdict,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q041-F-02 verdict: {verdict}")
    print(f"  H1 āfāq-singleton at Q 41:53: {h1_pass} (count={h1_count})")
    print(f"  H2 āfāq×anfus co-occur singleton at Q 41:53: {h2_pass} (count={h2_count})")
    print(f"  H3 full-collocation singleton at Q 41:53: {h3_pass} (count={h3_count})")
    print(f"  anfus alone: {len(anfus_hits)} verses (corpus-common)")
    print(f"  Output: {OUT_PATH}")


if __name__ == '__main__':
    main()
