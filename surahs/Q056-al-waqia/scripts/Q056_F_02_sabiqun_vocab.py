#!/usr/bin/env python3
"""
Q056-F-02 — Sābiqūn-block (Q 56:10-26) vocabulary uniqueness.
SHA-locked pre-reg: 2a21f274e459cd1244d7f7d72d4df7fac144830a164ec98a6b63bda9db6b018b
"""
import json, hashlib, re, os
from collections import Counter

PREREG = '/Users/grey/Downloads/quran/surahs/Q056-al-waqia/preregs/Q056-F-02-sabiqun-vocab-uniqueness-prereg.md'
EXPECTED_SHA = '2a21f274e459cd1244d7f7d72d4df7fac144830a164ec98a6b63bda9db6b018b'
with open(PREREG,'rb') as f:
    actual = hashlib.sha256(f.read()).hexdigest()
assert actual == EXPECTED_SHA, f'SHA mismatch: {actual}'

with open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json') as f:
    Q = json.load(f)

# Build corpus token-frequency
corpus_freq = Counter()
for surah in Q:
    for v in surah['verses']:
        for tok in v['text'].split():
            corpus_freq[tok] += 1

# Sābiqūn block tokens (Q56:10-26)
q56 = Q[55]
sabiqun_tokens = []
for v in q56['verses']:
    if 10 <= v['id'] <= 26:
        sabiqun_tokens.extend(v['text'].split())

# Filter for length ≥ 4 graphemes (excludes function words)
content_tokens = [t for t in set(sabiqun_tokens) if len(t) >= 4]
print(f'Total unique tokens in Sābiqūn block: {len(set(sabiqun_tokens))}')
print(f'Content-tokens (len>=4): {len(content_tokens)}')

# Tabulate corpus frequency for each
ranked = sorted([(t, corpus_freq[t]) for t in content_tokens], key=lambda x: x[1])

print('\nFrequency profile (sorted ascending):')
hapax_or_rare = []  # corpus_count <= 5
for t, c in ranked:
    marker = ''
    if c == 1: marker = ' [HAPAX corpus-wide]'
    elif c <= 5: marker = ' [RARE]'
    if c <= 5:
        hapax_or_rare.append((t,c))
    print(f'  {t}: corpus_count={c}{marker}')

print(f'\nTokens with corpus_count <= 5: {len(hapax_or_rare)}')
for t, c in hapax_or_rare:
    print(f'  - {t}: {c}')

verdict = 'VINDICATED' if len(hapax_or_rare) >= 3 else 'NULL'
print(f'\nVERDICT: {verdict} (pre-reg threshold: ≥ 3 rare tokens)')

# Hapax corpus-wide:
hapax = [(t,c) for t,c in hapax_or_rare if c == 1]
print(f'\nCorpus-hapax in Sābiqūn block: {len(hapax)}')
for t,c in hapax: print(f'  HAPAX: {t}')

result = {
    'test_id': 'Q056-F-02',
    'prereg_sha': EXPECTED_SHA,
    'unique_tokens_in_sabiqun': len(set(sabiqun_tokens)),
    'content_tokens_len_ge_4': len(content_tokens),
    'rare_threshold': 5,
    'rare_tokens': [{'token': t, 'corpus_count': c} for t,c in hapax_or_rare],
    'n_rare': len(hapax_or_rare),
    'corpus_hapax_in_block': [{'token': t, 'corpus_count': c} for t,c in hapax],
    'n_hapax': len(hapax),
    'verdict': verdict,
}

OUT = '/Users/grey/Downloads/quran/surahs/Q056-al-waqia/csv/Q056-F-02.json'
os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT,'w') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
print(f'\nWrote {OUT}')
