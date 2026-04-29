#!/usr/bin/env python3
"""Q009-F-04 — "last-revealed verse" classical-citation density.

For each of 7 OpenITI tafsir files, find lines mentioning "آخر ما نزل" / "آخر آية"
/ "آخر سورة"; in each context window (8 lines), match the rival claim markers:
- Q9:128-129  (لقد جاءكم رسول | براءة آخر | آخر ما نزل من القرآن.*رسول من أنفسكم)
- Q4:176     (كلالة | يستفتونك)
- Q2:281     (آية الربا | اتقوا يوما)
- Q5:3        (اليوم أكملت | حجة الوداع.*أكملت)

Pre-reg SHA: f489aa91c6810e7cf19ac634330e949118c41be0634a1ab390b9ab512fbda6bd
"""
import re
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'surahs/Q009-al-tawba/Q009-F-04-last-revealed-prereg.md'
EXPECTED_SHA = 'f489aa91c6810e7cf19ac634330e949118c41be0634a1ab390b9ab512fbda6bd'

TAFSIR_RAW_DIR = ROOT / 'data/literature/classical-tafsir/raw'
SOURCES = [
    'tabari-jami-bayan.openiti.raw.txt',
    'qurtubi-jami-ahkam.openiti.raw.txt',
    'razi-mafatih-al-ghayb.openiti.raw.txt',
    'ibn-kathir-tafsir-quran.openiti.raw.txt',
    'suyuti-durr-manthur.openiti.raw.txt',
    'biqai-nazm-al-durar.openiti.raw.txt',
    'zamakhshari-kashshaf.openiti.raw.txt',
    'suyuti-itqan.openiti.raw.txt',
    'tabarsi-majma-bayan.openiti.raw.txt',
    'thaclabi-kashf-bayan.openiti.raw.txt',
]

LAST_RE = re.compile(r'آخر\s+(ما نزل|آية|سورة)')

CLAIM_PATTERNS = {
    'Q9:128-129': re.compile(r'لقد جاءكم رسول|براءة من آخر|آخر سورة.*براءة|براءة.*آخر|أنفسكم عزيز عليه|رؤوف رحيم'),
    'Q4:176': re.compile(r'كلالة|يستفتونك'),
    'Q2:281': re.compile(r'آية الربا|اتقوا يوما|واتقوا يوما ترجعون'),
    'Q5:3': re.compile(r'اليوم أكملت|حجة الوداع.*أكملت|أكملت لكم دينكم'),
}


def verify_sha(path, expected):
    h = hashlib.sha256(path.read_bytes()).hexdigest()
    if h != expected:
        print(f'PRE-COMMIT VIOLATION: {path.name} sha={h} != expected={expected}')
        sys.exit(1)
    print(f'pre-reg sha verified: {path.name}')


def scan_file(path: Path, window_lines=8):
    lines = path.read_text(encoding='utf-8', errors='replace').splitlines()
    hits = {claim: 0 for claim in CLAIM_PATTERNS}
    last_hits_total = 0
    for i, ln in enumerate(lines):
        if LAST_RE.search(ln):
            last_hits_total += 1
            ctx_start = max(0, i - window_lines)
            ctx_end = min(len(lines), i + window_lines + 1)
            ctx = '\n'.join(lines[ctx_start:ctx_end])
            for claim, pat in CLAIM_PATTERNS.items():
                if pat.search(ctx):
                    hits[claim] += 1
    return hits, last_hits_total


def main():
    verify_sha(PREREG, EXPECTED_SHA)
    per_source = {}
    totals = {claim: 0 for claim in CLAIM_PATTERNS}
    grand_last = 0
    for src in SOURCES:
        p = TAFSIR_RAW_DIR / src
        if not p.exists():
            print(f'SKIP missing {src}')
            continue
        hits, last_total = scan_file(p)
        per_source[src] = {'last_total': last_total, 'claim_hits': hits}
        for c, n in hits.items():
            totals[c] += n
        grand_last += last_total

    sorted_totals = sorted(totals.items(), key=lambda x: -x[1])
    top = sorted_totals[0]

    # Direction-locked: VINDICATED if Q9:128-129 > each rival
    q9_count = totals['Q9:128-129']
    rival_max = max(v for k, v in totals.items() if k != 'Q9:128-129')

    if q9_count > rival_max * 1.10:
        verdict = 'VINDICATED'
    elif rival_max > q9_count * 1.10:
        # which rival?
        rival_name = max((k for k in totals if k != 'Q9:128-129'), key=lambda k: totals[k])
        verdict = f'DIRECTIONAL_VIOLATION_dominant_claim_{rival_name}'
    else:
        verdict = 'NULL_no_clear_dominance'

    out = {
        'finding_id': 'Q009-F-04',
        'prereg_sha': EXPECTED_SHA,
        'method': 'For each "آخر ما نزل|آية|سورة" hit, scan 8-line context for rival-claim markers.',
        'sources': SOURCES,
        'per_source_hits': per_source,
        'totals': totals,
        'sorted_totals': sorted_totals,
        'q9_128_count': q9_count,
        'max_rival_count': rival_max,
        'verdict': verdict,
        'last_revealed_total_mentions': grand_last,
    }
    out_path = ROOT / 'surahs/Q009-al-tawba/csv/Q009-F-04-last-revealed.json'
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f'wrote {out_path}')
    print()
    print(f'F-04 verdict: {verdict}')
    print(f'  Total "last-revealed" mentions (across {len(per_source)} tafsirs): {grand_last}')
    print(f'  Co-occurrence with rival claims:')
    for c, n in sorted_totals:
        print(f'    {c}: {n}')


if __name__ == '__main__':
    main()
