#!/usr/bin/env python3
"""Compute baseline structural metrics for Q4 al-Nisāʾ.

Rules-tuple: (no-tashkeel, orthographic-token, graphemes,
basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).

No external deps; stdlib only.
"""

import json
import os
import re
import sys

ROOT = '/Users/grey/Downloads/quran'
QPATH = os.path.join(ROOT, 'quran-text', 'quran-no-tashkeel.json')

# Pause-marks / Quranic punctuation that should not count as letters.
# Defensive: even though no-tashkeel JSON should be clean, strip these.
PAUSE_MARKS = 'ۖۗۘۙۚۛۜ۝۞ۣ۟۠ۡۢۤۥۦۧۨ۩۪ۭ۫۬'
ARABIC_DIGIT_RE = re.compile(r'[٠-٩]')


def clean(text: str) -> str:
    for ch in PAUSE_MARKS:
        text = text.replace(ch, '')
    text = ARABIC_DIGIT_RE.sub('', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def main():
    with open(QPATH) as f:
        quran = json.load(f)

    out = {}
    for surah in quran:
        sid = surah['id']
        verses = surah['verses']
        text = ' '.join(clean(v['text']) for v in verses)
        words = text.split()
        letters = text.replace(' ', '')
        out[sid] = {
            'name': surah['name'],
            'transliteration': surah['transliteration'],
            'type': surah['type'],
            'n_verses': surah['total_verses'],
            'n_words': len(words),
            'n_letters': len(letters),
            'words_per_verse': len(words) / surah['total_verses'] if surah['total_verses'] else 0,
            'letters_per_verse': len(letters) / surah['total_verses'] if surah['total_verses'] else 0,
        }

    # Print for Q4 + key comparators
    keys = [2, 3, 4, 5, 9, 24, 33, 65]
    for sid in keys:
        r = out[sid]
        print(f"Q{sid:3d} {r['transliteration']:>15} verses={r['n_verses']:4d} "
              f"words={r['n_words']:5d} letters={r['n_letters']:6d} "
              f"w/v={r['words_per_verse']:.2f} l/v={r['letters_per_verse']:.2f}  type={r['type']}")

    out_path = os.path.join(ROOT, 'surahs', 'Q004-al-nisa', 'csv', 'baseline-corpus-stats.json')
    with open(out_path, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f'\nwrote {out_path}')


if __name__ == '__main__':
    main()
