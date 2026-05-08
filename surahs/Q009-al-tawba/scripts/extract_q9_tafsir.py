#!/usr/bin/env python3
"""Extract Q9-specific sections from raw OpenITI tafsirs.

For each tafsir file in data/literature/classical-tafsir/raw/*.openiti.raw.txt,
locate the start of Q9 commentary (سورة التوبة or سورة براءة header) and
extract until the next surah header (سورة \\S+ : 10) or end of file.
"""
import re
import os
from pathlib import Path

RAW_DIR = Path('/Users/grey/Downloads/quran/data/literature/classical-tafsir/raw')
OUT_DIR = RAW_DIR

# Patterns: surah headers appear in many forms across the OpenITI tafsirs.
# We anchor on Q9 starts then scan forward for the next surah-10 (Yunus) header.
START_PATTERNS = [
    r'###\s*\|\s*\[?009\]?\s*سورة التوبة',
    r'###\s*\|\s*سورة التوبة',
    r'###\s*\|\s*\[?سورة التوبة',
    r'###\s*\|\s*تفسير سورة التوبة',
    r'###\s*\|\s*تفسير سورة براءة',
    r'###\s*\|\s*سورة براءة',
    r'###\s*\|\s*\[?سورة براءة',
    # Biqāʿī style: "# (سورة التوبة)"
    r'^#\s*\(سورة التوبة\)',
    r'^#\s*\(سورة براءة\)',
    # Tabarsi/other styles
    r'^#\s*سورة التوبة\b',
    r'^#\s*سورة براءة\b',
]

NEXT_SURAH_PATTERNS = [
    r'###\s*\|\s*\[?010\]?\s*سورة',
    r'###\s*\|\s*سورة يونس',
    r'###\s*\|\s*\[?سورة يونس',
    r'###\s*\|\s*تفسير سورة يونس',
    r'^#\s*\(سورة يونس\)',
    r'^#\s*سورة يونس\b',
    r'^#\s*10\s*-\s*سورة يونس',
    r'^#\s*\[?010\]?\s*-?\s*سورة يونس',
]

START_RE = re.compile('|'.join(START_PATTERNS), flags=re.MULTILINE)
NEXT_RE = re.compile('|'.join(NEXT_SURAH_PATTERNS), flags=re.MULTILINE)


def extract_q9(filepath: Path) -> str:
    text = filepath.read_text(encoding='utf-8', errors='replace')
    lines = text.splitlines()
    start_idx = None
    for i, ln in enumerate(lines):
        if START_RE.search(ln):
            start_idx = i
            break
    if start_idx is None:
        return ''
    # find next surah (Yunus, Q10) start AFTER our start
    end_idx = len(lines)
    for j in range(start_idx + 1, len(lines)):
        if NEXT_RE.search(lines[j]):
            end_idx = j
            break
    return '\n'.join(lines[start_idx:end_idx])


def main():
    for f in sorted(RAW_DIR.glob('*.openiti.raw.txt')):
        ex = extract_q9(f)
        if not ex:
            print(f'NOT FOUND  {f.name}')
            continue
        # name -> e.g. ibn-kathir-tafsir-quran.openiti.raw.txt -> ibn-kathir-Q009.txt
        base = f.name.replace('.openiti.raw.txt', '')
        # canonical short names
        rename_map = {
            'ibn-kathir-tafsir-quran': 'ibn-kathir-openiti',
            'tabari-jami-bayan': 'tabari-openiti',
            'qurtubi-jami-ahkam': 'qurtubi-openiti',
            'razi-mafatih-al-ghayb': 'razi-openiti',
            'biqai-nazm-al-durar': 'biqai-openiti',
            'tabarsi-majma-bayan': 'tabarsi-openiti',
            'thaclabi-kashf-bayan': 'thaclabi-openiti',
            'zamakhshari-kashshaf': 'zamakhshari-openiti',
            'suyuti-durr-manthur': 'suyuti-durr-openiti',
            'suyuti-itqan': 'suyuti-itqan-openiti',
        }
        short = rename_map.get(base, base)
        out = RAW_DIR / f'{short}-Q009.txt'
        out.write_text(ex, encoding='utf-8')
        n_lines = ex.count('\n') + 1
        print(f'{f.name} -> {out.name}  ({n_lines} lines)')


if __name__ == '__main__':
    main()
