#!/usr/bin/env python3
"""Q006-F-01 — Prophet-density per verse across 114 surahs.

Pre-reg: surahs/Q006-al-anam/Q006-F-01-prophet-density-per-verse-prereg.md
Pre-reg SHA-256 (locked): 741af6d1309e07a7c28846bebd1662de94ecabb1c42db5e4341a233fdb1b332c
Direction: MAX (Q 6 = rank 1 / N)
Bonferroni k=2 (Cell A max-tokens-in-verse, Cell B densest-5-window), alpha_bon=0.025
Seed: 20260507
Rules-tuple: (no-tashkeel, QAC-PN-lemma, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'surahs/Q006-al-anam/Q006-F-01-prophet-density-per-verse-prereg.md'
EXPECTED_SHA = '741af6d1309e07a7c28846bebd1662de94ecabb1c42db5e4341a233fdb1b332c'
QAC = ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt'
OUT = ROOT / 'surahs/Q006-al-anam/csv/Q006-F-01.json'

sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
assert sha == EXPECTED_SHA, f'pre-reg SHA mismatch: {sha} != {EXPECTED_SHA}'
print(f'pre-reg SHA verified: {sha}', file=sys.stderr)

PROPHET_LEMMAS = {
    'A^dam', 'nuwH', '<iboraAhiym', '<isomaAEiyl', '<isoHaAq', 'yaEoquwb', 'yuwsuf',
    'luwT', 'huwd', 'Sa`liH2', '$uEayob', 'muwsaY`', 'ha`ruwn', 'daAwud', 'sulayoma`n',
    '<iloyaAs', '<aloyasaE', 'yuwnus', 'zakariy~aA', 'yaHoyaY`', 'EiysaY`', '<idoriys',
    '>ay~uwb', 'muHam~ad', '>aHomad'
}

LOC = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')

# (surah, verse) -> count of prophet PN-lemma tokens in that verse
verse_pn_count = defaultdict(int)
verse_pn_lemmas = defaultdict(list)

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
        vid = int(m.group(2))
        feat = parts[3]
        if 'POS:PN' not in feat:
            continue
        lm = re.search(r'LEM:([^|]+)', feat)
        if not lm:
            continue
        lemma = lm.group(1)
        if lemma in PROPHET_LEMMAS:
            verse_pn_count[(sid, vid)] += 1
            verse_pn_lemmas[(sid, vid)].append(lemma)

# Per-surah verse counts (Hafs-Kufan)
TXT = json.load(open(ROOT / 'quran-text/quran-no-tashkeel.json'))
verse_count = {s['id']: len(s['verses']) for s in TXT}

# Cell A: max prophet tokens in a single verse
# Cell B: densest 5-verse contiguous window — sum/5
per_surah = {}
for s in range(1, 115):
    n_v = verse_count.get(s, 0)
    if n_v == 0:
        continue
    counts = [verse_pn_count.get((s, v), 0) for v in range(1, n_v + 1)]
    cell_a = max(counts) if counts else 0
    # Cell B: max over 5-verse windows (use min(5, n_v))
    w = min(5, n_v)
    if n_v >= w and w > 0:
        max_window_sum = max(sum(counts[i:i + w]) for i in range(n_v - w + 1))
        cell_b = max_window_sum / w
    else:
        cell_b = 0.0
    total_tokens = sum(counts)
    per_surah[s] = {
        'surah': s,
        'n_verses': n_v,
        'total_prophet_tokens': total_tokens,
        'cell_A_max_tokens_in_verse': cell_a,
        'cell_B_densest_5verse_density': cell_b,
        'densest_verse_id': counts.index(cell_a) + 1 if cell_a > 0 else None,
    }

# Restrict ranking to surahs with ≥1 prophet token
qualifying = [v for v in per_surah.values() if v['total_prophet_tokens'] >= 1]
N_qual = len(qualifying)

# Ranking — Cell A (descending; ties broken by Cell B then surah-id)
def rank(items, key):
    sorted_items = sorted(items, key=lambda x: (-x[key], -x['cell_B_densest_5verse_density'], x['surah']))
    return [(i + 1, it) for i, it in enumerate(sorted_items)]

ranked_A = rank(qualifying, 'cell_A_max_tokens_in_verse')
ranked_B = rank(qualifying, 'cell_B_densest_5verse_density')

q6_a = next((r, it) for r, it in ranked_A if it['surah'] == 6)
q6_b = next((r, it) for r, it in ranked_B if it['surah'] == 6)

direction_pass_A = (q6_a[0] == 1)
direction_pass_B = (q6_b[0] == 1)
direction_pass_top3_A = (q6_a[0] <= 3)
direction_pass_top3_B = (q6_b[0] <= 3)

# Verdict logic per pre-reg §4
if direction_pass_A and direction_pass_B:
    verdict = 'CONFIRMED'
elif (direction_pass_top3_A and direction_pass_B) or (direction_pass_top3_B and direction_pass_A):
    verdict = 'DIRECTIONAL-strong'
elif direction_pass_top3_A or direction_pass_top3_B:
    verdict = 'DIRECTIONAL'
elif q6_a[0] >= 10 or q6_b[0] >= 10:
    verdict = 'PRE_COMMIT_VIOLATION'
else:
    verdict = 'NULL'

result = {
    'test_id': 'Q006-F-01',
    'pre_reg_sha': EXPECTED_SHA,
    'pre_reg_sha_verified': True,
    'seed': 20260507,
    'direction_locked': 'MAX',
    'bonferroni_k': 2,
    'alpha_bon': 0.025,
    'rules_tuple': '(no-tashkeel, QAC-PN-lemma, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
    'q6_n_verses': verse_count[6],
    'q6_total_prophet_tokens': per_surah[6]['total_prophet_tokens'],
    'q6_cell_A_max_tokens_in_verse': q6_a[1]['cell_A_max_tokens_in_verse'],
    'q6_cell_A_densest_verse_id': q6_a[1]['densest_verse_id'],
    'q6_cell_A_rank': q6_a[0],
    'q6_cell_B_densest_5window_density': q6_b[1]['cell_B_densest_5verse_density'],
    'q6_cell_B_rank': q6_b[0],
    'N_qualifying_surahs': N_qual,
    'verdict': verdict,
    'top10_cell_A': [
        {'rank': r, 'surah': it['surah'], 'max_tokens_in_verse': it['cell_A_max_tokens_in_verse'],
         'densest_verse_id': it['densest_verse_id'], 'n_verses': it['n_verses']}
        for r, it in ranked_A[:10]
    ],
    'top10_cell_B': [
        {'rank': r, 'surah': it['surah'], 'densest_5_density': it['cell_B_densest_5verse_density'],
         'total_prophet_tokens': it['total_prophet_tokens'], 'n_verses': it['n_verses']}
        for r, it in ranked_B[:10]
    ],
    'q6_densest_verse_lemmas': verse_pn_lemmas.get((6, q6_a[1]['densest_verse_id']), []),
    'comparison_q21': {
        'q21_total_prophet_tokens': per_surah[21]['total_prophet_tokens'],
        'q21_cell_A_max': per_surah[21]['cell_A_max_tokens_in_verse'],
        'q21_cell_B_density': per_surah[21]['cell_B_densest_5verse_density'],
        'q21_cell_A_rank': next(r for r, it in ranked_A if it['surah'] == 21),
        'q21_cell_B_rank': next(r for r, it in ranked_B if it['surah'] == 21),
    },
    'honest_limits': [
        '25-prophet QAC-PN-lemma set (locked from H-NEW-940 / Q021-F-01).',
        'Token = each PN-lemma occurrence in a verse, not unique types per verse.',
        'Cell B uses 5-verse contiguous windows; surahs <5 verses use total/n_verses.',
        'Pronominal anaphora excluded (deliberate operational choice favoring LIST-FORM).',
    ],
}

OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f'Q006-F-01: Cell A rank = {q6_a[0]}/{N_qual} (max_tokens_in_verse={q6_a[1]["cell_A_max_tokens_in_verse"]} at v.{q6_a[1]["densest_verse_id"]})', file=sys.stderr)
print(f'Q006-F-01: Cell B rank = {q6_b[0]}/{N_qual} (densest_5window_density={q6_b[1]["cell_B_densest_5verse_density"]:.3f})', file=sys.stderr)
print(f'Verdict: {verdict}', file=sys.stderr)
print(f'Output: {OUT}', file=sys.stderr)
