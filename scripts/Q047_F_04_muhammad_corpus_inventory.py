#!/usr/bin/env python3
"""
Q047-F-04 — Muḥammad corpus inventory: exact attestation count and verse-set match.

Pre-reg: /Users/grey/Downloads/quran/surahs/Q047-muhammad/Q047-F-04-muhammad-corpus-inventory-prereg.md
Pre-reg SHA256: 81bf3a4589017eaf4f9cc47780be170b2267a5b07362833092bf04934ca2200a

Rules-tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""

import json
import hashlib
import sys
import os
from pathlib import Path

PROJECT = Path('/Users/grey/Downloads/quran')
PREREG = PROJECT / 'surahs/Q047-muhammad/Q047-F-04-muhammad-corpus-inventory-prereg.md'
EXPECTED_SHA = '81bf3a4589017eaf4f9cc47780be170b2267a5b07362833092bf04934ca2200a'
OUT = PROJECT / 'surahs/Q047-muhammad/csv/Q047-F-04.json'
SEED = 20260509

PRE_LISTED_MUHAMMAD = {(3, 144), (33, 40), (47, 2), (48, 29)}
PRE_LISTED_AHMAD = (61, 6)


def verify_prereg_sha():
    with open(PREREG, 'rb') as f:
        h = hashlib.sha256(f.read()).hexdigest()
    if h != EXPECTED_SHA:
        sys.exit(f'PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {h}')
    print(f'[OK] pre-reg SHA verified: {h}')


def main():
    verify_prereg_sha()
    with open(PROJECT / 'quran-text/quran-no-tashkeel.json', encoding='utf-8') as f:
        q = json.load(f)

    muhammad_attests = []
    ahmad_attests = []
    for s in q:
        sid = s['id']
        for v in s['verses']:
            toks = v['text'].split()
            if 'محمد' in toks:
                muhammad_attests.append((sid, v['id']))
            if 'أحمد' in toks:
                ahmad_attests.append((sid, v['id']))

    muhammad_count = len(muhammad_attests)
    ahmad_count = len(ahmad_attests)
    muhammad_set = set(muhammad_attests)

    set_matches = (muhammad_set == PRE_LISTED_MUHAMMAD)
    ahmad_matches = (ahmad_count == 1 and ahmad_attests[0] == PRE_LISTED_AHMAD)

    verdict = 'VINDICATED' if (muhammad_count == 4 and set_matches and ahmad_matches) else (
        'DIRECTIONAL' if (muhammad_count in (3, 4) and len(muhammad_set & PRE_LISTED_MUHAMMAD) >= 3) else 'NULL')

    out = {
        'test_id': 'Q047-F-04',
        'pre_reg_sha': EXPECTED_SHA,
        'seed': SEED,
        'rules_tuple': '(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'muhammad_count_verse_internal': muhammad_count,
        'muhammad_attestations': sorted([list(x) for x in muhammad_attests]),
        'pre_listed_muhammad_verses': sorted([list(x) for x in PRE_LISTED_MUHAMMAD]),
        'muhammad_set_exact_match': set_matches,
        'ahmad_count_verse_internal': ahmad_count,
        'ahmad_attestations': [list(x) for x in ahmad_attests],
        'pre_listed_ahmad_verse': list(PRE_LISTED_AHMAD),
        'ahmad_set_exact_match': ahmad_matches,
        'note_title_line': 'Title-line "سورة محمد" of Q 47 is paratext, NOT counted (rules-tuple: paratext excluded; basmala counted only in Q 1).',
        'verdict': verdict,
        'bonferroni_k': 1,
        'alpha_bon': 0.05,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f'[OK] wrote {OUT}')
    print(f'  Muhammad: {muhammad_count} attestations at {muhammad_attests}')
    print(f'  Ahmad: {ahmad_count} attestation(s) at {ahmad_attests}')
    print(f'  Set match: muhammad={set_matches}, ahmad={ahmad_matches}')
    print(f'  Verdict: {verdict}')


if __name__ == '__main__':
    main()
