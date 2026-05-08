#!/usr/bin/env python3
"""Q021-F-01 — Prophet-cycle completeness across 114 surahs.

Pre-reg: surahs/Q021-al-anbiya/Q021-F-01-prophet-cycle-completeness-prereg.md
Pre-reg SHA-256 (locked): 6417085b816096084978359223408d20c0f159205d7e94949508363059598dfa
Direction: MAX (Q 21 = rank 1 / 114)
Bonferroni k=1, α=0.05, seed=20260507
"""
import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'surahs/Q021-al-anbiya/Q021-F-01-prophet-cycle-completeness-prereg.md'
EXPECTED_SHA = '6417085b816096084978359223408d20c0f159205d7e94949508363059598dfa'
QAC = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
OUT = ROOT / 'surahs/Q021-al-anbiya/csv/Q021-F-01.json'

# SHA verify
sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
assert sha == EXPECTED_SHA, f'pre-reg SHA mismatch: got {sha}, expected {EXPECTED_SHA}'
print(f'pre-reg SHA verified: {sha}', file=sys.stderr)

# Locked canonical-prophet PN-lemma set (25 names)
PROPHET_LEMMAS = {
    'A^dam', 'nuwH', '<iboraAhiym', '<isomaAEiyl', '<isoHaAq', 'yaEoquwb', 'yuwsuf',
    'luwT', 'huwd', 'Sa`liH2', '$uEayob', 'muwsaY`', 'ha`ruwn', 'daAwud', 'sulayoma`n',
    '<iloyaAs', '<aloyasaE', 'yuwnus', 'zakariy~aA', 'yaHoyaY`', 'EiysaY`', '<idoriys',
    '>ay~uwb', 'muHam~ad', '>aHomad'
}

LOC = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')

per_surah_pn = defaultdict(set)
with open(QAC, encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
            continue
        parts = line.rstrip().split('\t')
        if len(parts) < 4:
            continue
        m = LOC.match(parts[0])
        if not m:
            continue
        sid = int(m.group(1))
        feat = parts[3]
        if 'POS:PN' not in feat:
            continue
        lm = re.search(r'LEM:([^|]+)', feat)
        if not lm:
            continue
        per_surah_pn[sid].add(lm.group(1))

# Per-surah canonical-prophet count
per_surah_count = {}
per_surah_set = {}
for s in range(1, 115):
    pset = per_surah_pn[s] & PROPHET_LEMMAS
    per_surah_count[s] = len(pset)
    per_surah_set[s] = sorted(pset)

# Rank Q 21
ranked = sorted(per_surah_count.items(), key=lambda x: -x[1])
q21_rank = next(i for i, (s, _) in enumerate(ranked) if s == 21) + 1
q21_count = per_surah_count[21]
top10 = ranked[:10]

# Direction lock check
direction_locked = 'MAX'
direction_pass = (q21_rank == 1)
verdict = 'CONFIRMED' if direction_pass else 'NULL_PRE_COMMIT_VIOLATION'

result = {
    'test_id': 'Q021-F-01',
    'pre_reg_sha': EXPECTED_SHA,
    'pre_reg_sha_verified': True,
    'seed': 20260507,
    'direction_locked': direction_locked,
    'direction_pass': direction_pass,
    'verdict': verdict,
    'q21_distinct_prophets': q21_count,
    'q21_rank': q21_rank,
    'q21_prophet_list': per_surah_set[21],
    'top_15_by_count': [
        {'surah': s, 'count': c, 'prophets': per_surah_set[s]}
        for s, c in ranked[:15]
    ],
    'rank1_corpus_max': {
        'surah': ranked[0][0],
        'count': ranked[0][1],
        'prophets': per_surah_set[ranked[0][0]]
    },
    'comparison_surahs': {
        f'Q{s}': {'count': per_surah_count[s], 'prophets': per_surah_set[s]}
        for s in [6, 7, 11, 12, 19, 21, 26, 37, 38]
    },
    'honest_limits': [
        '25-prophet set is a curated standard list; alternative curators might shift counts.',
        'Q 21:91 references Maryam + ʿĪsā but does not name them by PN-lemma; both excluded.',
        'Dhū-l-Kifl (Q 21:85) excluded due to ambiguous QAC PN tagging.',
        'PN tagging is QAC v0.4 specific; alternative morphological corpora might shift absolute counts.'
    ]
}

OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f'Q021-F-01 result: Q21 distinct prophets = {q21_count}, rank = {q21_rank}/114', file=sys.stderr)
print(f'Verdict: {verdict}', file=sys.stderr)
print(f'Output: {OUT}', file=sys.stderr)
