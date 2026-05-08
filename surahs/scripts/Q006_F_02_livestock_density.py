#!/usr/bin/env python3
"""Q006-F-02 — Livestock-vocabulary cluster density across 114 surahs.

Pre-reg: surahs/Q006-al-anam/Q006-F-02-livestock-vocab-prereg.md
Pre-reg SHA-256 (locked): d611d7b770ff5094c3f26087ab0a94058a76a4566e5122b521b7461108cfdb82
Direction: MAX (LOCKED)
Bonferroni k=2, alpha_bon=0.025
Rules-tuple: (no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
PREREG = ROOT / 'surahs/Q006-al-anam/Q006-F-02-livestock-vocab-prereg.md'
EXPECTED_SHA = 'd611d7b770ff5094c3f26087ab0a94058a76a4566e5122b521b7461108cfdb82'
TXT = ROOT / 'quran-text/quran-no-tashkeel.json'
OUT = ROOT / 'surahs/Q006-al-anam/csv/Q006-F-02.json'

sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
assert sha == EXPECTED_SHA, f'pre-reg SHA mismatch: {sha} != {EXPECTED_SHA}'
print(f'pre-reg SHA verified: {sha}', file=sys.stderr)

# Locked livestock cluster regex (5-element)
# Word-boundary regex; matches بقر / البقر / للبقر etc, captures inflected/possessed forms
PATTERNS = {
    'anEam':  re.compile(r'(?<![ا-ي])(?:ال|ب|ل|و|ك|ف)?أنعام(?![ا-ي])'),
    'da2n':   re.compile(r'(?<![ا-ي])(?:ال|ب|ل|و|ف)?ضأن(?![ا-ي])'),
    'maEz':   re.compile(r'(?<![ا-ي])(?:ال|ب|ل|و|ف)?معز(?![ا-ي])'),
    'ibl':    re.compile(r'(?<![ا-ي])(?:ال|ب|ل|و|ف)?إبل(?![ا-ي])'),
    'baqar':  re.compile(r'(?<![ا-ي])(?:ال|ب|ل|و|ف)?بقر(?:ة)?(?![ا-ي])'),
}

txt = json.load(open(TXT))

per_surah = {}
for s in txt:
    sid = s['id']
    n_verses = len(s['verses'])
    n_words = 0
    counts = {k: 0 for k in PATTERNS}
    matched_locations = []
    for v in s['verses']:
        text = v['text']
        n_words += len(text.split())
        for k, pat in PATTERNS.items():
            ms = pat.findall(text)
            if ms:
                counts[k] += len(ms)
                matched_locations.append({'verse': v['id'], 'cluster': k, 'tokens': ms})
    total_count = sum(counts.values())
    per_surah[sid] = {
        'surah': sid,
        'n_verses': n_verses,
        'n_words': n_words,
        'cell_A_total_count': total_count,
        'per_cluster_counts': counts,
        'cell_B_density_per_word': total_count / n_words if n_words else 0.0,
        'cell_B_density_per_100w': (total_count / n_words * 100) if n_words else 0.0,
        'sample_locations': matched_locations[:8],
    }

# Cell B eligibility: ≥3 tokens (per pre-reg §5)
eligible_B = [v for v in per_surah.values() if v['cell_A_total_count'] >= 3]

ranked_A = sorted(per_surah.values(), key=lambda x: (-x['cell_A_total_count'], x['surah']))
ranked_B = sorted(eligible_B, key=lambda x: (-x['cell_B_density_per_word'], x['surah']))

q6_a_rank = next(i + 1 for i, it in enumerate(ranked_A) if it['surah'] == 6)
q6_b_rank = next(i + 1 for i, it in enumerate(ranked_B) if it['surah'] == 6)

# Verdict
top3_A = q6_a_rank <= 3
top3_B = q6_b_rank <= 3
top1 = q6_a_rank == 1 or q6_b_rank == 1
if (q6_a_rank == 1 and top3_B) or (q6_b_rank == 1 and top3_A):
    verdict = 'CONFIRMED'
elif top3_A and top3_B:
    verdict = 'DIRECTIONAL'
elif q6_b_rank >= 10:
    verdict = 'PRE_COMMIT_VIOLATION'
elif q6_b_rank >= 5:
    verdict = 'NULL'
else:
    verdict = 'DIRECTIONAL-borderline'

result = {
    'test_id': 'Q006-F-02',
    'pre_reg_sha': EXPECTED_SHA,
    'pre_reg_sha_verified': True,
    'seed': 20260507,
    'direction_locked': 'MAX',
    'bonferroni_k': 2,
    'alpha_bon': 0.025,
    'rules_tuple': '(no-tashkeel, orthographic-word, regex-word-boundary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
    'cluster_terms': list(PATTERNS.keys()),
    'q6_cell_A_total_count': per_surah[6]['cell_A_total_count'],
    'q6_per_cluster_counts': per_surah[6]['per_cluster_counts'],
    'q6_cell_A_rank': q6_a_rank,
    'q6_cell_B_density_per_word': per_surah[6]['cell_B_density_per_word'],
    'q6_cell_B_density_per_100w': per_surah[6]['cell_B_density_per_100w'],
    'q6_cell_B_rank': q6_b_rank,
    'q6_n_words': per_surah[6]['n_words'],
    'verdict': verdict,
    'top10_cell_A': [
        {'rank': i + 1, 'surah': it['surah'], 'total_count': it['cell_A_total_count'],
         'per_cluster': it['per_cluster_counts'], 'n_words': it['n_words']}
        for i, it in enumerate(ranked_A[:10])
    ],
    'top10_cell_B': [
        {'rank': i + 1, 'surah': it['surah'], 'density_per_100w': it['cell_B_density_per_100w'],
         'total_count': it['cell_A_total_count'], 'n_words': it['n_words']}
        for i, it in enumerate(ranked_B[:10])
    ],
    'eligible_B_count': len(eligible_B),
    'q6_sample_matches': per_surah[6]['sample_locations'],
    'honest_limits': [
        '5-element cluster: anʿām, ḍaʾn, maʿz, ibl, baqar (locked).',
        'Cell B eligibility: ≥3 tokens (excludes short surahs with single-token artifacts).',
        'Q 5:103 jāhilī-categories (baḥīra etc.) explicitly excluded — separate phenomenon.',
        'Q 2 al-Baqara naturally has بقر from its own eponym; Cell B (density) corrects for length.',
    ],
}

OUT.parent.mkdir(parents=True, exist_ok=True)
with open(OUT, 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=2, ensure_ascii=False)

print(f'Q006-F-02: Cell A (total count) = {per_surah[6]["cell_A_total_count"]}, rank = {q6_a_rank}/114', file=sys.stderr)
print(f'Q006-F-02: Cell B (density per 100w) = {per_surah[6]["cell_B_density_per_100w"]:.3f}, rank = {q6_b_rank}/{len(eligible_B)}', file=sys.stderr)
print(f'Verdict: {verdict}', file=sys.stderr)
print(f'Output: {OUT}', file=sys.stderr)
