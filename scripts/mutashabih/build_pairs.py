#!/usr/bin/env python3
"""
Mutashabih lafzi pair finder.

For every pair of verses (v1, v2) from DIFFERENT surahs:
  - lemma-tokenize via Leeds Quranic Arabic Corpus morphology
  - require length ratio in [0.7, 1.3]
  - require token overlap >= 80% in either direction (multiset Jaccard-style)
  - emit (s1, v1, s2, v2, overlap, len1, len2, common_lemmas, only1, only2)

Token = lemma when present; falls back to surface form for particles/pronouns.
Stop-grams (proclitic conjunctions wa, fa, bi, li, ka, sa) are kept BUT
weighted normally — we want to detect particle-difference pairs as well.
"""
import json
import re
from collections import defaultdict, Counter
from itertools import combinations

MORPH = '/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt'
QURAN = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'
OUT_RAW = '/Users/grey/Downloads/quran/scripts/mutashabih/pairs_raw.json'

# ---------- 1. parse morphology -> verse_tokens ----------
verse_tokens = defaultdict(list)  # (s,v) -> ordered list of token-strings
verse_features = defaultdict(list)  # (s,v) -> ordered list of dict per token

with open(MORPH) as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
            continue
        parts = line.strip().split('\t')
        if len(parts) < 4:
            continue
        loc, form, tag, feats = parts
        m = re.match(r'\((\d+):(\d+):(\d+):(\d+)\)', loc)
        if not m:
            continue
        s, v, w, p = map(int, m.groups())
        # parse features
        d = {'form': form, 'tag': tag, 'lem': None, 'root': None, 'pos': None, 'feats': feats}
        for fld in feats.split('|'):
            if fld.startswith('LEM:'):
                d['lem'] = fld[4:]
            elif fld.startswith('ROOT:'):
                d['root'] = fld[5:]
            elif fld.startswith('POS:'):
                d['pos'] = fld[4:]
        # token-key for matching: prefer LEM, else POS+form (so particles match by form),
        # else just form
        if d['lem']:
            tok = f"L:{d['lem']}"
        else:
            # for particles: bi, li, fa, wa, sa, etc.
            tok = f"F:{form}"
        verse_tokens[(s, v)].append(tok)
        verse_features[(s, v)].append(d)

print(f'verses with morphology: {len(verse_tokens)}')

# ---------- 2. quick filter: build token-set index for candidate generation ----------
# To avoid O(N^2) over 6236*6235/2 = 19.4M pairs (still doable but slow on python),
# we use an inverted index: for each lemma token, the list of verses containing it.
# Pairs that share NO 4+ common tokens can't reach 80% overlap if both are length>=5.
inv = defaultdict(set)
for vk, toks in verse_tokens.items():
    for t in set(toks):
        inv[t].add(vk)

# ---------- 3. enumerate candidate pairs ----------
# For each verse, look at intersections via shared lemmas. We'll flag candidates
# where they share enough rare lemmas; then validate.
def overlap_ratio(toks1, toks2):
    """multiset intersection / max(len1,len2). symmetric."""
    c1 = Counter(toks1)
    c2 = Counter(toks2)
    common = sum((c1 & c2).values())
    return common / max(len(toks1), len(toks2)), common

def length_match(toks1, toks2, ratio=0.30):
    L1, L2 = len(toks1), len(toks2)
    if L1 == 0 or L2 == 0:
        return False
    short, long_ = (L1, L2) if L1 < L2 else (L2, L1)
    return short / long_ >= (1 - ratio)

MIN_LEN = 5
THRESHOLD = 0.80  # at least 80% of MAX(len1,len2) must be common

# Build candidate set: for each verse, iterate to other verses sharing a rare-ish lemma.
# To bound work: pick the rarest 30% of lemmas in each verse and union the verses they appear in.
lemma_freq = {t: len(s) for t, s in inv.items()}

candidates = set()  # (vk1, vk2) with vk1 < vk2 lexicographically
all_vk = sorted(verse_tokens.keys())
for vk in all_vk:
    toks = verse_tokens[vk]
    if len(toks) < MIN_LEN:
        continue
    # sort tokens by global frequency, take rarest 50%
    sorted_t = sorted(set(toks), key=lambda t: lemma_freq.get(t, 9999))
    cut = max(2, len(sorted_t) // 2)
    rare = sorted_t[:cut]
    cand_other = set()
    for t in rare:
        for other in inv[t]:
            if other == vk:
                continue
            if other[0] == vk[0]:  # different surahs only per spec
                continue
            cand_other.add(other)
    for o in cand_other:
        a, b = (vk, o) if vk < o else (o, vk)
        candidates.add((a, b))

print(f'candidate pairs: {len(candidates)}')

# ---------- 4. validate candidates ----------
hits = []
for (vk1, vk2) in candidates:
    t1 = verse_tokens[vk1]
    t2 = verse_tokens[vk2]
    if not length_match(t1, t2, 0.30):
        continue
    if max(len(t1), len(t2)) < MIN_LEN:
        continue
    ratio, common_count = overlap_ratio(t1, t2)
    if ratio < THRESHOLD:
        continue
    c1 = Counter(t1); c2 = Counter(t2)
    common = (c1 & c2)
    only1 = list((c1 - c2).elements())
    only2 = list((c2 - c1).elements())
    hits.append({
        's1': vk1[0], 'v1': vk1[1],
        's2': vk2[0], 'v2': vk2[1],
        'len1': len(t1), 'len2': len(t2),
        'overlap_ratio': round(ratio, 4),
        'common_count': common_count,
        'common_tokens': sorted(common.elements()),
        'only1': sorted(only1),
        'only2': sorted(only2),
    })

print(f'hits at >= {THRESHOLD}: {len(hits)}')
hits.sort(key=lambda h: (-h['overlap_ratio'], -max(h['len1'], h['len2'])))
with open(OUT_RAW, 'w') as f:
    json.dump(hits, f, ensure_ascii=False, indent=1)
print(f'wrote {OUT_RAW}')
