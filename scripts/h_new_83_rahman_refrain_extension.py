#!/usr/bin/env python3
"""
H-NEW-83: Q 55 al-Raḥmān refrain extension.
Pre-registered: findings/phase-b-hypotheses/h-new-83-rahman-refrain-extension-prereg.md

Tests:
  - Verify refrain count (31), positions, first-at-v13
  - Cross-corpus refrain substring check
  - Block segmentation + per-block stats
  - Sub-refrain n-gram detection
  - Refrain vs non-refrain length contrast (KS)
  - 4-part partition vs random 4-cuts (block-length variance test)
"""
import json, re, random, math, statistics
from collections import Counter

CORPUS = '/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'
SEED = 20260415

def norm(s):
    s = re.sub(r'[\u200c\u200d\u200e\u200f]', '', s)
    table = {'إ':'ا', 'أ':'ا', 'آ':'ا', 'ٱ':'ا',
             'ى':'ي', 'ة':'ه', 'ؤ':'و', 'ئ':'ي', 'ء':''}
    out = ''.join(table.get(c, c) for c in s)
    return re.sub(r'\s+', ' ', out).strip()

def ks_test(a, b):
    """Two-sample KS test, two-sided. Returns (D, p_approx)."""
    a, b = sorted(a), sorted(b)
    na, nb = len(a), len(b)
    all_v = sorted(set(a + b))
    cdf_a = lambda x: sum(1 for v in a if v <= x) / na
    cdf_b = lambda x: sum(1 for v in b if v <= x) / nb
    D = max(abs(cdf_a(x) - cdf_b(x)) for x in all_v)
    en = math.sqrt(na * nb / (na + nb))
    # asymptotic p-value
    lam = (en + 0.12 + 0.11/en) * D
    p = 2 * sum((-1)**(k-1) * math.exp(-2 * (lam*k)**2) for k in range(1, 101))
    p = max(0.0, min(1.0, p))
    return D, p

def main():
    with open(CORPUS) as f:
        q = json.load(f)
    s55 = q[54]
    assert s55['id'] == 55
    verses = s55['verses']
    n_verses = len(verses)
    print(f'Q 55 al-Raḥmān: {n_verses} verses')
    print(f'name: {s55["name"]}')

    refrain_text = verses[12]['text']
    refrain_norm = norm(refrain_text)
    print(f'\nv13 raw    : {refrain_text}')
    print(f'v13 norm   : {refrain_norm}')

    # === RP-1, RP-2: refrain count operationalization ===
    refrain_positions = [v['id'] for v in verses if norm(v['text']) == refrain_norm]
    print(f'\n=== H-83a (refrain count) ===')
    print(f'verse-level exact matches: {len(refrain_positions)}')
    print(f'positions: {refrain_positions}')

    # substring count check (does any verse contain refrain as proper substring?)
    substr_extra = []
    for v in verses:
        nv = norm(v['text'])
        if refrain_norm in nv and nv != refrain_norm:
            substr_extra.append((v['id'], v['text']))
    print(f'verses containing refrain as proper substring (not equal): {len(substr_extra)}')
    for vid, txt in substr_extra:
        print(f'  v{vid}: {txt}')

    # === H-83d: first refrain at v13 ===
    print(f'\n=== H-83d (first refrain at v13) ===')
    print(f'first refrain position: v{refrain_positions[0]}')
    assert refrain_positions[0] == 13, 'first refrain not at v13!'

    # === RP-3: cross-corpus refrain check ===
    print(f'\n=== H-83b/c (cross-corpus) ===')
    distinctive_3gram = norm('الاء ربكما تكذبان')  # core part of refrain
    # Use the actual normalized substring from the refrain
    # refrain_norm = 'فباي الا ربكما تكذبان' -- distinctive part is 'الا ربكما تكذبان'
    distinctive_substr = ' '.join(refrain_norm.split()[1:])  # drop 'فباي'
    print(f'distinctive substring (drop opener): {distinctive_substr}')

    cross_full = []
    cross_substr = []
    for surah in q:
        for v in surah['verses']:
            nv = norm(v['text'])
            if surah['id'] == 55:
                continue
            if refrain_norm in nv:
                cross_full.append((surah['id'], v['id'], v['text']))
            if distinctive_substr in nv:
                cross_substr.append((surah['id'], v['id'], v['text']))
    print(f'verses outside Q55 containing full refrain: {len(cross_full)}')
    for sid, vid, txt in cross_full[:5]:
        print(f'  Q{sid}:{vid}: {txt}')
    print(f'verses outside Q55 containing distinctive substring "{distinctive_substr}": {len(cross_substr)}')
    for sid, vid, txt in cross_substr[:5]:
        print(f'  Q{sid}:{vid}: {txt}')

    # Even more lenient: just "tukadhdhibān" (last word of refrain) anywhere
    last_word = refrain_norm.split()[-1]  # 'تكذبان'
    cross_lastword = []
    for surah in q:
        for v in surah['verses']:
            nv = norm(v['text'])
            if surah['id'] == 55:
                continue
            if last_word in nv.split():
                cross_lastword.append((surah['id'], v['id'], v['text']))
    print(f'verses outside Q55 containing "{last_word}" as a token: {len(cross_lastword)}')
    for sid, vid, txt in cross_lastword[:10]:
        print(f'  Q{sid}:{vid}: {txt}')

    # === RP-7: refrain vs non-refrain length contrast ===
    print(f'\n=== refrain vs non-refrain length ===')
    refrain_set = set(refrain_positions)
    refrain_lens = [len(v['text']) for v in verses if v['id'] in refrain_set]
    nonref_lens = [len(v['text']) for v in verses if v['id'] not in refrain_set]
    refrain_words = [len(v['text'].split()) for v in verses if v['id'] in refrain_set]
    nonref_words = [len(v['text'].split()) for v in verses if v['id'] not in refrain_set]
    print(f'refrain     n={len(refrain_lens):2d}  char-len mean={statistics.mean(refrain_lens):.2f}  sd={statistics.pstdev(refrain_lens):.2f}  word mean={statistics.mean(refrain_words):.2f}')
    print(f'non-refrain n={len(nonref_lens):2d}  char-len mean={statistics.mean(nonref_lens):.2f}  sd={statistics.pstdev(nonref_lens):.2f}  word mean={statistics.mean(nonref_words):.2f}')
    D_chars, p_chars = ks_test(refrain_lens, nonref_lens)
    D_words, p_words = ks_test(refrain_words, nonref_words)
    print(f'KS char-len: D={D_chars:.4f}  p={p_chars:.4g}')
    print(f'KS word    : D={D_words:.4f}  p={p_words:.4g}')

    # === RP-4: block segmentation ===
    print(f'\n=== block segmentation (refrain-leading) ===')
    boundaries = [0] + refrain_positions  # block ends just after refrain
    blocks = []  # (start_verse, end_verse, content_verses, refrain_verse)
    prev = 0  # 0 = before v1
    for r in refrain_positions:
        content = list(range(prev + 1, r))  # all non-refrain verses up to (not including) refrain
        blocks.append({
            'content': content,
            'refrain': r,
            'span': (prev + 1, r),
            'n_content': len(content),
        })
        prev = r
    # coda: v78 alone after last refrain v77
    if refrain_positions[-1] < n_verses:
        coda_content = list(range(refrain_positions[-1] + 1, n_verses + 1))
        blocks.append({
            'content': coda_content,
            'refrain': None,
            'span': (refrain_positions[-1] + 1, n_verses),
            'n_content': len(coda_content),
        })
    print(f'total blocks: {len(blocks)} (31 refrain-blocks + {1 if blocks[-1]["refrain"] is None else 0} coda)')
    for i, b in enumerate(blocks):
        ref_label = f'r{b["refrain"]}' if b['refrain'] else 'CODA'
        print(f'  block {i:2d}: vv {b["span"][0]:2d}-{b["span"][1]:2d}  content={b["n_content"]:2d}  ({ref_label})')

    # block bytes
    print(f'\n=== block content bytes (UTF-8) ===')
    block_bytes = []
    block_words = []
    for i, b in enumerate(blocks):
        content_text = ' '.join(verses[v - 1]['text'] for v in b['content'])
        bb = len(content_text.encode('utf-8'))
        bw = len(content_text.split())
        block_bytes.append(bb)
        block_words.append(bw)

    # === H-83f: 4-part partition variance check ===
    print(f'\n=== H-83f: classical 4-part partition vs random ===')
    # Classical partition by VERSE: vv 1-30 / 31-45 / 46-61 / 62-77 / coda 78
    # Map to refrain-block indices.
    # blocks 0..7 cover refrains at 13,16,18,21,23,25,28,30 → part A (vv 1-30)
    # blocks 8..14 cover refrains 32,34,36,38,40,42,45 → part B (vv 31-45)
    # blocks 15..22 cover refrains 47,49,51,53,55,57,59,61 → part C (vv 46-61)
    # blocks 23..30 cover refrains 63,65,67,69,71,73,75,77 → part D (vv 62-77)
    # block 31 = coda (v78)
    part_assignment = [0]*8 + [1]*7 + [2]*8 + [3]*8 + [4]  # 32 entries
    assert len(part_assignment) == len(blocks), (len(part_assignment), len(blocks))
    # exclude coda for variance test (leave as singleton)
    refrain_blocks = blocks[:31]
    refrain_block_words = block_words[:31]
    refrain_block_bytes = block_bytes[:31]

    parts_words = {0: [], 1: [], 2: [], 3: []}
    for i, b in enumerate(refrain_blocks):
        p = part_assignment[i]
        parts_words[p].append(refrain_block_words[i])
    print(f'classical partition (refrain count per part): {[len(parts_words[k]) for k in range(4)]}')
    print(f'words per block, by part:')
    for k in range(4):
        print(f'  part {chr(65+k)} ({len(parts_words[k])} blocks): {parts_words[k]}  mean={statistics.mean(parts_words[k]):.2f}  sd={statistics.pstdev(parts_words[k]):.2f}')

    def within_part_variance(assignment, vals):
        groups = {}
        for a, v in zip(assignment, vals):
            groups.setdefault(a, []).append(v)
        wpv = 0
        for g in groups.values():
            if len(g) > 1:
                wpv += statistics.pvariance(g) * len(g)
            # singleton contributes 0
        return wpv / len(vals)

    classical_assign = part_assignment[:31]
    obs_wpv = within_part_variance(classical_assign, refrain_block_words)
    print(f'\nobserved within-part variance (words): {obs_wpv:.4f}')

    random.seed(SEED)
    perm_wpvs = []
    n_perm = 1000
    n = 31
    for _ in range(n_perm):
        # 4-cut: pick 3 distinct cut points in 1..n-1
        cuts = sorted(random.sample(range(1, n), 3))
        assign = []
        prev_c = 0
        for k, c in enumerate(cuts):
            assign.extend([k]*(c - prev_c))
            prev_c = c
        assign.extend([3]*(n - prev_c))
        perm_wpvs.append(within_part_variance(assign, refrain_block_words))
    perm_wpvs.sort()
    rank = sum(1 for v in perm_wpvs if v <= obs_wpv)
    p_one_sided = (rank + 1) / (n_perm + 1)
    print(f'random 4-cuts (n={n_perm}): mean={statistics.mean(perm_wpvs):.4f}  median={statistics.median(perm_wpvs):.4f}  min={min(perm_wpvs):.4f}')
    print(f'observed at rank {rank}/{n_perm}, one-sided p (lower) = {p_one_sided:.4f}')

    # === RP-6: sub-refrain n-gram detection ===
    print(f'\n=== H-83e: sub-refrain n-grams ===')
    refrain_tokens = refrain_norm.split()
    refrain_ngrams_set = set()
    for nsz in (3, 4, 5):
        for i in range(len(refrain_tokens) - nsz + 1):
            refrain_ngrams_set.add(' '.join(refrain_tokens[i:i+nsz]))
    print(f'(refrain sub-n-grams to exclude: {refrain_ngrams_set})')

    for nsz in (3, 4, 5):
        cnt = Counter()
        for v in verses:
            tokens = norm(v['text']).split()
            for i in range(len(tokens) - nsz + 1):
                ng = ' '.join(tokens[i:i+nsz])
                cnt[ng] += 1
        repeated = [(ng, c) for ng, c in cnt.items() if c >= 2]
        # exclude n-grams that are substring of refrain (already covered)
        non_refrain = [(ng, c) for ng, c in repeated if ng not in refrain_ngrams_set]
        repeated.sort(key=lambda x: -x[1])
        non_refrain.sort(key=lambda x: -x[1])
        print(f'\n  n={nsz}: {len(repeated)} distinct ≥2-occurring n-grams; {len(non_refrain)} excluding refrain sub-n-grams')
        for ng, c in non_refrain[:10]:
            print(f'    [{c}x] {ng}')

    # === intra-Q55 phrase pairs (loose) ===
    # Look for any verse pair (non-refrain) with high lexical overlap
    print(f'\n=== high-overlap non-refrain verse pairs in Q55 (Jaccard ≥ 0.5) ===')
    nonref_verses = [(v['id'], norm(v['text'])) for v in verses if v['id'] not in refrain_set]
    pairs = []
    for i, (vi, ti) in enumerate(nonref_verses):
        ti_set = set(ti.split())
        for j in range(i+1, len(nonref_verses)):
            vj, tj = nonref_verses[j]
            tj_set = set(tj.split())
            if not ti_set or not tj_set: continue
            jacc = len(ti_set & tj_set) / len(ti_set | tj_set)
            if jacc >= 0.5:
                pairs.append((vi, vj, jacc, verses[vi-1]['text'], verses[vj-1]['text']))
    pairs.sort(key=lambda x: -x[2])
    for vi, vj, j, ti, tj in pairs[:15]:
        print(f'  v{vi} ↔ v{vj}  J={j:.3f}')
        print(f'    v{vi}: {ti}')
        print(f'    v{vj}: {tj}')

if __name__ == '__main__':
    main()
