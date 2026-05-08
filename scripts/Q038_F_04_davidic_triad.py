#!/usr/bin/env python3
"""Q038-F-04 — David-Solomon-Job inner-triad coherence test.

Pre-reg: surahs/Q038-sad/Q038-F-04-davidic-triad-prereg.md
Pre-reg SHA256: cf6f80d637c673638ec6b1f54ed95785d91b0f3c34fa65d74859ca5df2ea8bfb
Rules-tuple: (no-tashkeel, orthographic-token, TF-IDF on Q 38-internal vocabulary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import json, hashlib, sys, os, math, random
from collections import Counter

PREREG = '/Users/grey/Downloads/quran/surahs/Q038-sad/Q038-F-04-davidic-triad-prereg.md'
EXPECTED_SHA = 'cf6f80d637c673638ec6b1f54ed95785d91b0f3c34fa65d74859ca5df2ea8bfb'
SEED = 20260507
N_PERM = 10000

# Triad and contrast blocks (1-indexed verse ranges)
TRIAD = list(range(17, 45))  # vv. 17-44 inclusive
BLOCK_A = list(range(1, 17))  # vv. 1-16 (Quraysh-polemic)
BLOCK_C = list(range(45, 89))  # vv. 45-88 (Abrahamic + eschatology)


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def tokenize(text):
    # strip separators
    for sep in '۞۩ۭۚۖۗۘۙۜۤ':
        text = text.replace(sep, ' ')
    return [t for t in text.split() if t]


def cosine(a, b):
    keys = set(a) | set(b)
    if not keys:
        return 0.0
    dot = sum(a.get(k,0)*b.get(k,0) for k in keys)
    na = math.sqrt(sum(v*v for v in a.values()))
    nb = math.sqrt(sum(v*v for v in b.values()))
    return dot / (na*nb) if na and nb else 0.0


def mean_pairwise_cosine(verse_vectors):
    if len(verse_vectors) < 2:
        return 0.0
    sims = []
    for i in range(len(verse_vectors)):
        for j in range(i+1, len(verse_vectors)):
            sims.append(cosine(verse_vectors[i], verse_vectors[j]))
    return sum(sims) / len(sims)


def main():
    verify_sha()
    rng = random.Random(SEED)

    quran = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))
    q38 = next(s for s in quran if s['id']==38)

    # Tokenize each verse
    verse_tokens = {}  # 1-indexed vid -> list of tokens
    for v in q38['verses']:
        verse_tokens[v['id']] = tokenize(v['text'])

    # Compute IDF on Q 38 internal corpus (88 verses)
    df = Counter()
    for vid, toks in verse_tokens.items():
        for t in set(toks):
            df[t] += 1
    N = len(verse_tokens)
    idf = {t: math.log(N/df[t]) + 1.0 for t in df}

    # Build TF-IDF vectors per verse (skip muq verse 1 strip is already in token list since "ص" is its own token)
    verse_vec = {}
    for vid, toks in verse_tokens.items():
        tf = Counter(toks)
        vec = {t: tf[t] * idf[t] for t in tf}
        verse_vec[vid] = vec

    # Compute mean pairwise cosine for triad, blockA, blockC
    triad_vecs = [verse_vec[v] for v in TRIAD if v in verse_vec]
    blockA_vecs = [verse_vec[v] for v in BLOCK_A if v in verse_vec]
    blockC_vecs = [verse_vec[v] for v in BLOCK_C if v in verse_vec]

    triad_cohesion = mean_pairwise_cosine(triad_vecs)
    blockA_cohesion = mean_pairwise_cosine(blockA_vecs)
    blockC_cohesion = mean_pairwise_cosine(blockC_vecs)

    # Permutation null for Test 1: random 28-verse samples from Q 38
    n_triad = len(triad_vecs)
    all_vids = list(verse_tokens.keys())
    null_cohesions = []
    for _ in range(N_PERM):
        sample_vids = rng.sample(all_vids, n_triad)
        sample_vecs = [verse_vec[v] for v in sample_vids]
        null_cohesions.append(mean_pairwise_cosine(sample_vecs))
    null_mean = sum(null_cohesions)/N_PERM
    null_std = (sum((x-null_mean)**2 for x in null_cohesions)/N_PERM)**0.5
    p_test1 = sum(1 for x in null_cohesions if x >= triad_cohesion) / N_PERM

    # Test 2: triad cohesion / mean(A,C) > 1
    avg_AC = (blockA_cohesion + blockC_cohesion) / 2
    ratio = triad_cohesion / avg_AC if avg_AC > 0 else float('inf')

    # For test 2, derive a permutation p too: shuffle which 16+44 verse-block-assignments
    # are A/C; the test is whether the actual triad-vs-rest contrast is exceptional.
    # We do: re-sample 28-verse "triad" + 16-verse "A" + 44-verse "C" partitions of Q 38; compute ratio in each.
    null_ratios = []
    for _ in range(N_PERM):
        shuffled = rng.sample(all_vids, len(all_vids))
        nt = shuffled[:n_triad]
        na = shuffled[n_triad:n_triad+len(blockA_vecs)]
        nc = shuffled[n_triad+len(blockA_vecs):n_triad+len(blockA_vecs)+len(blockC_vecs)]
        ct = mean_pairwise_cosine([verse_vec[v] for v in nt])
        ca = mean_pairwise_cosine([verse_vec[v] for v in na])
        cc = mean_pairwise_cosine([verse_vec[v] for v in nc])
        avg = (ca+cc)/2
        if avg > 0:
            null_ratios.append(ct / avg)
    p_test2 = sum(1 for x in null_ratios if x >= ratio) / len(null_ratios)

    alpha_bon = 0.05/2
    pass_test1 = p_test1 < alpha_bon
    pass_test2 = p_test2 < alpha_bon and ratio > 1.0
    n_pass = int(pass_test1) + int(pass_test2)

    pre_commit_violation = triad_cohesion < null_mean

    if pre_commit_violation:
        verdict = 'PRE-COMMIT-VIOLATION'
    elif n_pass == 2:
        verdict = 'CONFIRMED'
    elif n_pass == 1:
        verdict = 'DIRECTIONAL'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q038-F-04',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, orthographic-token, TF-IDF on Q 38-internal vocabulary, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'method': 'TF-IDF on Q38 vocabulary; mean pairwise cosine; 10000 perms',
        'verses': {
            'triad_range': '17-44 (28 verses)',
            'blockA_range': '1-16 (16 verses)',
            'blockC_range': '45-88 (44 verses)',
        },
        'cohesions': {
            'triad': triad_cohesion,
            'blockA': blockA_cohesion,
            'blockC': blockC_cohesion,
            'ratio_triad_to_avg_AC': ratio,
        },
        'test1_internal_cohesion': {
            'null_mean': null_mean, 'null_std': null_std,
            'p_greater_perm': p_test1,
            'pass_alpha_bon': pass_test1,
        },
        'test2_distinctness': {
            'p_greater_perm': p_test2,
            'pass_alpha_bon': pass_test2,
        },
        'alpha_bon': alpha_bon,
        'pre_commit_violation': pre_commit_violation,
        'n_pass_of_2': n_pass,
        'verdict': verdict,
    }
    os.makedirs('/Users/grey/Downloads/quran/surahs/Q038-sad/csv', exist_ok=True)
    with open('/Users/grey/Downloads/quran/surahs/Q038-sad/csv/Q038-F-04.json', 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Triad cohesion: {triad_cohesion:.4f}; null mean: {null_mean:.4f} ± {null_std:.4f}")
    print(f"BlockA: {blockA_cohesion:.4f}; BlockC: {blockC_cohesion:.4f}")
    print(f"Test 1 (triad vs random-28): p={p_test1:.4f}, pass={pass_test1}")
    print(f"Test 2 (ratio = {ratio:.4f} > 1): p={p_test2:.4f}, pass={pass_test2}")
    print(f"Verdict: {verdict}")


if __name__ == '__main__':
    main()
