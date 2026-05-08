#!/usr/bin/env python3
"""Extract Q010 Yūnus sections from each OpenITI tafsir raw file.

Outputs files of form `data/literature/classical-tafsir/raw/{tafsir}-openiti-Q010.txt`.
Boundary detection: per file, find the surah-section heading and the NEXT surah heading.
"""
import os, re, sys

RAW_DIR = '/Users/grey/Downloads/quran/data/literature/classical-tafsir/raw'

# (raw filename, output filename, surah-heading regex, next-heading regex)
TARGETS = [
    # ibn-kathir uses "### | تفسير سورة X"
    ('ibn-kathir-tafsir-quran.openiti.raw.txt', 'ibn-kathir-openiti-Q010.txt',
     r'### \| تفسير سورة يونس', r'### \| تفسير سورة هود'),
    # tabari -- check pattern
    ('tabari-jami-bayan.openiti.raw.txt', 'tabari-openiti-Q010.txt',
     r'سورة يونس|تفسير سورة يونس', r'سورة هود|تفسير سورة هود'),
    ('qurtubi-jami-ahkam.openiti.raw.txt', 'qurtubi-openiti-Q010.txt',
     r'سورة يونس|تفسير سورة يونس', r'سورة هود|تفسير سورة هود'),
    ('zamakhshari-kashshaf.openiti.raw.txt', 'zamakhshari-openiti-Q010.txt',
     r'سورة يونس|تفسير سورة يونس', r'سورة هود|تفسير سورة هود'),
    ('razi-mafatih-al-ghayb.openiti.raw.txt', 'razi-openiti-Q010.txt',
     r'سورة يونس|تفسير سورة يونس', r'سورة هود|تفسير سورة هود'),
    ('biqai-nazm-al-durar.openiti.raw.txt', 'biqai-openiti-Q010.txt',
     r'سورة يونس|تفسير سورة يونس', r'سورة هود|تفسير سورة هود'),
    ('suyuti-durr-manthur.openiti.raw.txt', 'suyuti-durr-openiti-Q010.txt',
     r'سورة يونس|تفسير سورة يونس', r'سورة هود|تفسير سورة هود'),
    ('thaclabi-kashf-bayan.openiti.raw.txt', 'thaclabi-openiti-Q010.txt',
     r'سورة يونس|تفسير سورة يونس', r'سورة هود|تفسير سورة هود'),
    ('tabarsi-majma-bayan.openiti.raw.txt', 'tabarsi-openiti-Q010.txt',
     r'سورة يونس|تفسير سورة يونس', r'سورة هود|تفسير سورة هود'),
    ('suyuti-itqan.openiti.raw.txt', 'suyuti-itqan-openiti-Q010.txt',
     None, None),  # itqan is non-tafsir; do whole-file (later filter Q10 mentions)
]


def find_first(lines, pattern):
    rx = re.compile(pattern)
    for i, ln in enumerate(lines):
        if rx.search(ln):
            return i
    return -1


def extract(raw_fn, out_fn, start_pat, end_pat):
    src = os.path.join(RAW_DIR, raw_fn)
    if not os.path.exists(src):
        print(f'  MISSING raw: {raw_fn}')
        return
    with open(src, encoding='utf-8') as f:
        lines = f.readlines()
    if start_pat is None:
        # whole-file pass-through with Q10 mention filter handled downstream
        # for itqan: extract paragraphs mentioning Yūnus/يونس
        out = []
        for ln in lines:
            if 'يونس' in ln or 'Yūnus' in ln:
                out.append(ln)
        body = ''.join(out)
        with open(os.path.join(RAW_DIR, out_fn), 'w', encoding='utf-8') as f:
            f.write(body)
        print(f'  {out_fn}: {len(out)} lines (filtered for يونس)')
        return
    s = find_first(lines, start_pat)
    if s < 0:
        print(f'  NO START in {raw_fn}: tried {start_pat!r}')
        return
    e = find_first(lines[s+1:], end_pat)
    if e < 0:
        print(f'  NO END in {raw_fn} after line {s}: tried {end_pat!r} -- writing to EOF')
        body = ''.join(lines[s:])
    else:
        body = ''.join(lines[s:s+1+e])
    with open(os.path.join(RAW_DIR, out_fn), 'w', encoding='utf-8') as f:
        f.write(body)
    print(f'  {out_fn}: lines {s}..{s+e if e>=0 else len(lines)} ({len(body)} chars)')


def main():
    for raw_fn, out_fn, sp, ep in TARGETS:
        extract(raw_fn, out_fn, sp, ep)


if __name__ == '__main__':
    main()
