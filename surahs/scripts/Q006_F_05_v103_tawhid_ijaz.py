#!/usr/bin/env python3
"""Q006-F-05 — Q 6:103 lā tudrikuhu al-abṣār — divine-incomprehensibility 4-cell verse-rank audit.

Pre-reg: surahs/Q006-al-anam/Q006-F-05-q6v103-tawhid-ijaz-prereg.md
Pre-reg SHA-256 (locked): 8d9082b958c0681641c7930cf4b280e0040218e37444f5bae7b85251c269cde6
Direction: MAX (Q 6:103 = rank 1 / 6,236 verses, LOCKED)
Bonferroni k=4, alpha_bon=0.0125
Rules-tuple: (no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'surahs/Q006-al-anam/Q006-F-05-q6v103-tawhid-ijaz-prereg.md'
EXPECTED_SHA = '8d9082b958c0681641c7930cf4b280e0040218e37444f5bae7b85251c269cde6'
TXT = ROOT / 'quran-text/quran-no-tashkeel.json'
OUT = ROOT / 'surahs/Q006-al-anam/csv/Q006-F-05.json'

sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
assert sha == EXPECTED_SHA, f'pre-reg SHA mismatch: {sha} != {EXPECTED_SHA}'
print(f'pre-reg SHA verified: {sha}', file=sys.stderr)

# Locked 4 cells per pre-reg §2
C1 = re.compile(r'لا\s+تدركه')
C2_VERB = re.compile(r'(?<![ا-ي])يدرك(?![ا-ي])')
C2_OBJ = re.compile(r'(?<![ا-ي))(?:أبصار|الأبصار|قلوب|القلوب)(?![ا-ي])')
C3 = re.compile(r'(?<![ا-ي])اللطيف(?![ا-ي])')
C4 = re.compile(r'(?<![ا-ي])الخبير(?![ا-ي])')

# Note: C2_OBJ has a typo in pattern; rewrite cleanly
C2_OBJ = re.compile(r'(?<![ا-ي])(?:أبصار|الأبصار|قلوب|القلوب)(?![ا-ي])')

txt = json.load(open(TXT))

verse_scores = []  # list of dicts
for s in txt:
    sid = s['id']
    for v in s['verses']:
        text = v['text']
        c1 = 1 if C1.search(text) else 0
        c2 = 1 if (C2_VERB.search(text) and C2_OBJ.search(text)) else 0
        c3 = 1 if C3.search(text) else 0
        c4 = 1 if C4.search(text) else 0
        joint = c1 + c2 + c3 + c4
        verse_scores.append({
            'surah': sid,
            'verse': v['id'],
            'c1_la_tudrikuhu': c1,
            'c2_yudriku_obj': c2,
            'c3_al_latif': c3,
            'c4_al_khabir': c4,
            'joint_score': joint,
            'text_excerpt': text[:160] if joint > 0 else None,
        })

total_verses = len(verse_scores)
# Cell A: rank Q 6:103
ranked = sorted(verse_scores, key=lambda x: (-x['joint_score'], x['surah'], x['verse']))
q6v103 = next(it for it in verse_scores if it['surah'] == 6 and it['verse'] == 103)
q6v103_rank = next(i + 1 for i, it in enumerate(ranked) if it['surah'] == 6 and it['verse'] == 103)
q6v103_score = q6v103['joint_score']

# Cell B: corpus-wide perfect-score (=4) verses
perfect_score_verses = [it for it in verse_scores if it['joint_score'] == 4]
high_score_verses = [it for it in verse_scores if it['joint_score'] >= 3]

# Cell C: per-cell corpus counts
c1_count = sum(it['c1_la_tudrikuhu'] for it in verse_scores)
c2_count = sum(it['c2_yudriku_obj'] for it in verse_scores)
c3_count = sum(it['c3_al_latif'] for it in verse_scores)
c4_count = sum(it['c4_al_khabir'] for it in verse_scores)

# Verdict per pre-reg §3
n_at_max = sum(1 for it in verse_scores if it['joint_score'] == q6v103_score)
if q6v103_score == 4 and n_at_max == 1:
    verdict = 'CONFIRMED-UNIQUE-MAX'
elif q6v103_score == 4 and n_at_max <= 3:
    verdict = 'DIRECTIONAL'
elif q6v103_score == 4:
    verdict = 'NULL'
elif q6v103_score == 3:
    verdict = 'NULL-near-max'
elif q6v103_score <= 1:
    verdict = 'PRE_COMMIT_VIOLATION'
else:
    verdict = 'NULL'

result = {
    'test_id': 'Q006-F-05',
    'pre_reg_sha': EXPECTED_SHA,
    'pre_reg_sha_verified': True,
    'seed': 20260507,
    'direction_locked': 'MAX',
    'bonferroni_k': 4,
    'alpha_bon': 0.0125,
    'rules_tuple': '(no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
    'q6v103': {
        'c1_la_tudrikuhu': q6v103['c1_la_tudrikuhu'],
        'c2_yudriku_obj': q6v103['c2_yudriku_obj'],
        'c3_al_latif': q6v103['c3_al_latif'],
        'c4_al_khabir': q6v103['c4_al_khabir'],
        'joint_score': q6v103_score,
        'rank_among_6236': q6v103_rank,
        'n_tied_at_q6v103_score': n_at_max,
    },
    'cell_B_perfect_score_verses': [
        {'surah': it['surah'], 'verse': it['verse'], 'text': it['text_excerpt']}
        for it in perfect_score_verses
    ],
    'cell_B_high_score_verses_score3plus': [
        {'surah': it['surah'], 'verse': it['verse'], 'score': it['joint_score'], 'text': it['text_excerpt']}
        for it in high_score_verses
    ],
    'cell_C_per_cell_corpus_counts': {
        'c1_la_tudrikuhu_total': c1_count,
        'c2_yudriku_obj_total': c2_count,
        'c3_al_latif_total': c3_count,
        'c4_al_khabir_total': c4_count,
    },
    'total_verses_analyzed': total_verses,
    'verdict': verdict,
    'honest_limits': [
        '4-cell lexeme set is one operationalization of al-Bāqillānī\'s iʿjāz al-tawḥīd claim.',
        'Cell C2 disambiguation: requires both يدرك verb AND (abṣār OR qulūb) object in same verse.',
        'C3 (al-Laṭīf) and C4 (al-Khabīr) are paired in multiple verses (e.g., Q 33:34, Q 67:14) — these will appear as 2-cell verses.',
        'Lexical-density-only test; does not capture rhetorical chiasm structure of Q 6:103.',
    ],
}

OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f'Q006-F-05: Q6:103 joint_score = {q6v103_score} / 4', file=sys.stderr)
print(f'  Cell c1={q6v103["c1_la_tudrikuhu"]} c2={q6v103["c2_yudriku_obj"]} c3={q6v103["c3_al_latif"]} c4={q6v103["c4_al_khabir"]}', file=sys.stderr)
print(f'  Rank: {q6v103_rank}/{total_verses}; n_tied_at_score: {n_at_max}', file=sys.stderr)
print(f'  Perfect-score (=4) corpus count: {len(perfect_score_verses)}', file=sys.stderr)
print(f'  C1 corpus count: {c1_count} (la_tudrikuhu rare formula)', file=sys.stderr)
print(f'Verdict: {verdict}', file=sys.stderr)
print(f'Output: {OUT}', file=sys.stderr)
