#!/usr/bin/env python3
"""
Q049-F-04 — Q 49:13 universalist-verse rare-root concentration.
Pre-reg SHA: 314b36ee8c13491427f9ef57f860341639d8235a5d000e639cba0dded59504bd
Direction: POSITIVE — Q 49:13 contains ≥2 roots with corpus-total ≤ 50 AND shaʿb (ش-ع-ب)
  is corpus-EXACT-doubleton (total = 2).
Seed: 20260509  (corpus exhaustive enumeration of QAC v0.4 morphology).
"""

import json
import os
from collections import Counter, defaultdict

ROOT = '/Users/grey/Downloads/quran'
PRE_REG_SHA = '314b36ee8c13491427f9ef57f860341639d8235a5d000e639cba0dded59504bd'


def parse_qac_morphology():
    """Parse QAC v0.4 morphology.
    Returns: dict[(sura, verse, word, seg)] -> root, plus corpus_root_count Counter.
    """
    seg_root = {}
    corpus_count = Counter()

    with open(os.path.join(ROOT, 'data', 'morphology', 'quranic-corpus-morphology-0.4.txt')) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('LOCATION'):
                continue
            parts = line.split('\t')
            if len(parts) < 4:
                continue
            loc, form, tag, feats = parts[0], parts[1], parts[2], parts[3]
            root = None
            for ft in feats.split('|'):
                if ft.startswith('ROOT:'):
                    root = ft[5:]
                    break
            if not root:
                continue
            try:
                inside = loc.strip('()')
                sura, verse, word, seg = [int(x) for x in inside.split(':')]
            except Exception:
                continue
            seg_root[(sura, verse, word, seg)] = root
            corpus_count[root] += 1

    return seg_root, corpus_count


def main():
    seg_root, corpus_count = parse_qac_morphology()

    # Q 49:13 unique roots
    q49_13_segs = [(s, v, w, sg) for (s, v, w, sg) in seg_root if s == 49 and v == 13]
    q49_13_word_roots = defaultdict(list)
    for (s, v, w, sg) in q49_13_segs:
        q49_13_word_roots[w].append(seg_root[(s, v, w, sg)])

    unique_roots = sorted(set(r for roots in q49_13_word_roots.values() for r in roots))
    root_corpus = {r: corpus_count[r] for r in unique_roots}

    # Sub-test 1: shaʿb (ش-ع-ب, transliterated $Eb in QAC)
    # The QAC-v0.4 transliteration uses $ for ش, E for ع, b for ب
    shab_root = '$Eb'
    shab_total = corpus_count[shab_root]
    sub1_pass = shab_total == 2

    # Sub-test 2: ≥1 root with corpus-total ≤ 5 in Q 49:13
    rare_5 = [r for r in unique_roots if corpus_count[r] <= 5]
    sub2_pass = len(rare_5) >= 1

    # Sub-test 3: ≥2 roots with corpus-total ≤ 50 in Q 49:13
    rare_50 = [r for r in unique_roots if corpus_count[r] <= 50]
    sub3_pass = len(rare_50) >= 2

    # Sub-test 4: Q 49:13 mean root-rarity in bottom-decile of all 6,236 verses
    # rarity score per verse = mean(1/corpus_count[r] for r in unique_roots_in_verse)
    # iterate over all verses
    verse_roots = defaultdict(set)
    for (s, v, w, sg), root in seg_root.items():
        verse_roots[(s, v)].add(root)

    verse_rarity = {}
    for (s, v), roots in verse_roots.items():
        if not roots:
            continue
        # rarity score: mean of inverse-corpus-frequency
        rarity = sum(1.0 / corpus_count[r] for r in roots) / len(roots)
        verse_rarity[(s, v)] = rarity

    q49_13_rarity = verse_rarity.get((49, 13))
    sorted_rarity_desc = sorted(verse_rarity.values(), reverse=True)
    n_verses = len(verse_rarity)
    # Bottom-decile = top-decile of rarity (highest rarity)
    decile_threshold = sorted_rarity_desc[n_verses // 10]
    q49_13_rank = next((i + 1 for i, v in enumerate(sorted_rarity_desc) if v <= q49_13_rarity), n_verses)
    sub4_pass = q49_13_rarity >= decile_threshold

    n_pass = sum([sub1_pass, sub2_pass, sub3_pass, sub4_pass])

    if n_pass >= 3:
        verdict = 'CONFIRMED-VERSE-ANOMALY'
    elif n_pass >= 1:
        verdict = 'PARTIAL'
    else:
        verdict = 'NULL'

    # Build readable root-corpus table
    root_corpus_table = sorted(
        [(r, corpus_count[r]) for r in unique_roots],
        key=lambda x: x[1]
    )

    result = {
        'finding_id': 'Q049-F-04',
        'pre_reg_sha256': PRE_REG_SHA,
        'seed': 20260509,
        'rules_tuple': '(QAC-v0.4-morphology, root-from-feats-ROOT-tag, no-tashkeel, mushaf-order)',
        'bonferroni_k': 4,
        'alpha_bon': 0.0125,
        'q49_13_unique_roots': unique_roots,
        'q49_13_n_unique_roots': len(unique_roots),
        'q49_13_root_corpus_table': [{'root': r, 'corpus_total': c} for (r, c) in root_corpus_table],
        'sub1_shab_corpus_total': shab_total,
        'sub1_pass_doubleton_exact': sub1_pass,
        'sub2_rare_5_count': len(rare_5),
        'sub2_rare_5_roots': rare_5,
        'sub2_pass': sub2_pass,
        'sub3_rare_50_count': len(rare_50),
        'sub3_rare_50_roots': rare_50,
        'sub3_pass': sub3_pass,
        'sub4_q49_13_rarity_score': q49_13_rarity,
        'sub4_q49_13_verse_rank_descending': q49_13_rank,
        'sub4_n_verses_with_roots': n_verses,
        'sub4_top_decile_threshold': decile_threshold,
        'sub4_pass_in_top_decile': sub4_pass,
        'n_subtests_pass': n_pass,
        'verdict': verdict,
    }

    out_path = os.path.join(ROOT, 'surahs', 'Q049-al-hujurat', 'csv', 'Q049-F-04.json')
    with open(out_path, 'w') as f:
        json.dump(result, f, indent=2)

    print(f'Q049-F-04 verdict: {verdict}')
    print(f'  Sub-test 1: shaʿb (ش-ع-ب) corpus-total = {shab_total} (predicted = 2)  → {"PASS" if sub1_pass else "FAIL"}')
    print(f'  Sub-test 2: roots ≤5 in Q 49:13 = {len(rare_5)}: {rare_5}  → {"PASS" if sub2_pass else "FAIL"}')
    print(f'  Sub-test 3: roots ≤50 in Q 49:13 = {len(rare_50)}: {rare_50}  → {"PASS" if sub3_pass else "FAIL"}')
    print(f'  Sub-test 4: Q 49:13 rarity rank {q49_13_rank}/{n_verses}, top-decile threshold {decile_threshold:.4f}, q49:13 rarity {q49_13_rarity:.4f}  → {"PASS" if sub4_pass else "FAIL"}')
    print(f'  Pass count: {n_pass}/4')


if __name__ == '__main__':
    main()
