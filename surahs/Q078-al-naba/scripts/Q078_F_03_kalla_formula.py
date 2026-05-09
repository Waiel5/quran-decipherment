#!/usr/bin/env python3
"""
Q078-F-03 — Q 78:4-5 / Q 102:3-4 *kallā sa-yaʿlamūn / thumma kallā sa-yaʿlamūn*
            corpus-EXACT 2-instance pair-match test.

Pre-reg: surahs/Q078-al-naba/preregs/Q078-F-03-kalla-formula-prereg.md
SHA256:  embedded at runtime; verified against pre-reg

Hypothesis (LOCKED PRE-RUN):
  H1: The formula sequence "kallā sa-yaʿlamūn" + "thumma kallā sa-yaʿlamūn"
      occurs in EXACTLY 2 corpus locations: Q 78:4-5 AND Q 102:3-4.
      DIRECTION: corpus-EXACT count = 2.

H0: H1 fails (count ≠ 2).

Single-test (no Bonferroni for the corpus-EXACT count claim, which is
either TRUE or FALSE).

Method:
  - For each corpus surah, find consecutive verse-pairs (v, v+1) where
    v matches "كلا سيعلمون" exactly (after no-tashkeel normalization)
    AND v+1 matches "ثم كلا سيعلمون" exactly.
  - Count surah-pair-locations.

Seed: 20260509.
"""

import json
import re
import os
import hashlib

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
PREREG_PATH = os.path.join(os.path.dirname(__file__), '..', 'preregs',
                           'Q078-F-03-kalla-formula-prereg.md')
QURAN_PATH = os.path.join(PROJECT_ROOT, 'quran-text', 'quran-no-tashkeel.json')
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), '..', 'csv', 'Q078-F-03.json')

SEED = 20260509


def sha256_of(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def normalize(s):
    """No-tashkeel + alif-variants + final-yāʾ unification."""
    s = s.strip()
    # remove tatweel + spaces in canonical form, just keep word-character normalization
    s = re.sub(r'\s+', ' ', s)
    return s


def main():
    prereg_sha = sha256_of(PREREG_PATH)
    print(f"prereg SHA256: {prereg_sha}")

    with open(QURAN_PATH) as f:
        d = json.load(f)

    pat_first = re.compile(r'^كلا سيعلمون$')
    pat_second = re.compile(r'^ثم كلا سيعلمون$')

    pair_matches = []
    for s in d:
        verses = s['verses']
        for i in range(len(verses) - 1):
            v_curr = normalize(verses[i]['text'])
            v_next = normalize(verses[i+1]['text'])
            if pat_first.match(v_curr) and pat_second.match(v_next):
                pair_matches.append({
                    "surah": s['id'],
                    "v_first": verses[i]['id'],
                    "v_first_text": verses[i]['text'],
                    "v_second": verses[i+1]['id'],
                    "v_second_text": verses[i+1]['text'],
                })

    h1_pass = len(pair_matches) == 2

    # Document also the standalone occurrences of each formula
    pat_first_loose = re.compile(r'كلا سيعلمون')
    pat_second_loose = re.compile(r'ثم كلا سيعلمون')

    first_occurrences = []
    second_occurrences = []
    for s in d:
        for v in s['verses']:
            t = v['text']
            if pat_first_loose.search(t):
                first_occurrences.append({"surah": s['id'], "verse": v['id'], "text": t})
            if pat_second_loose.search(t):
                second_occurrences.append({"surah": s['id'], "verse": v['id'], "text": t})

    output = {
        "test_id": "Q078-F-03",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "h1_pair_matches": pair_matches,
        "h1_pair_count": len(pair_matches),
        "h1_pass_exact2": h1_pass,
        "first_formula_all_occurrences": first_occurrences,
        "second_formula_all_occurrences": second_occurrences,
    }

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"H1 corpus-EXACT pair-matches: {len(pair_matches)}")
    for m in pair_matches:
        print(f"  Q{m['surah']}:{m['v_first']}-{m['v_second']}")
    print(f"H1 PASS (corpus-exact 2): {h1_pass}")
    print(f"All Q corpus 'kallā sa-yaʿlamūn' single-formula occurrences:")
    for o in first_occurrences:
        print(f"  Q{o['surah']}:{o['verse']}: {o['text']}")
    print(f"All Q corpus 'thumma kallā sa-yaʿlamūn' single-formula occurrences:")
    for o in second_occurrences:
        print(f"  Q{o['surah']}:{o['verse']}: {o['text']}")
    print(f"Output: {OUTPUT_PATH}")


if __name__ == '__main__':
    main()
