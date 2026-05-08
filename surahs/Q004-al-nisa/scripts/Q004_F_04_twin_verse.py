#!/usr/bin/env python3
"""Q004-F-04 — Q 4:1 vs Q 39:6 twin-verse lexical similarity.

Pre-reg locked at SHA256 1741604624900cc15e0b02e75286daeaa00c1ccb1a2e066864d73c802dfdc0a7.
"""

import hashlib
import json
import os
import random
import re
import sys

ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(ROOT, 'surahs', 'Q004-al-nisa', 'preregs',
                     'Q004-F-04-q4-1-q39-6-twin-prereg.md')
EXPECTED_SHA = '1741604624900cc15e0b02e75286daeaa00c1ccb1a2e066864d73c802dfdc0a7'
SEED = 20260507
N_PERM = 10000

PAUSE_MARKS = 'ۖۗۘۙۚۛۜ۝۞ۣ۟۠ۡۢۤۥۦۧۨ۩۪ۭ۫۬'


def sha256_of_file(path: str) -> str:
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def verify_prereg():
    actual = sha256_of_file(PREREG)
    if actual != EXPECTED_SHA:
        sys.exit(f'FATAL: pre-reg SHA mismatch.\n'
                 f'  expected = {EXPECTED_SHA}\n'
                 f'  actual   = {actual}')


def tokenize(text: str):
    for ch in PAUSE_MARKS:
        text = text.replace(ch, '')
    text = re.sub(r'\s+', ' ', text).strip()
    return text.split()


def jaccard(a, b):
    A, B = set(a), set(b)
    if not A and not B:
        return 0.0
    return len(A & B) / len(A | B)


def overlap_coef(a, b):
    A, B = set(a), set(b)
    if not A or not B:
        return 0.0
    return len(A & B) / min(len(A), len(B))


def bigrams(tokens):
    return set(zip(tokens, tokens[1:])) if len(tokens) >= 2 else set()


def main():
    verify_prereg()

    with open(os.path.join(ROOT, 'quran-text', 'quran-no-tashkeel.json')) as f:
        quran = json.load(f)

    # Q4:1 -> surah index 3 (1-based 4), verse_id 1
    q4_1 = next(v['text'] for v in quran[3]['verses'] if v['id'] == 1)
    # Q39:6 -> surah index 38, verse_id 6
    q39_6 = next(v['text'] for v in quran[38]['verses'] if v['id'] == 6)

    a = tokenize(q4_1)
    b = tokenize(q39_6)
    j = jaccard(a, b)
    ov = overlap_coef(a, b)
    ba = bigrams(a)
    bb = bigrams(b)
    bj = (len(ba & bb) / len(ba | bb)) if (ba | bb) else 0.0

    # Build a flat verse pool (surah_id, verse_id, tokens)
    pool = []
    for s in quran:
        for v in s['verses']:
            toks = tokenize(v['text'])
            if toks:
                pool.append((s['id'], v['id'], toks))

    rng = random.Random(SEED)
    null_jaccards = []
    null_overlaps = []
    null_bigrams = []
    n_pool = len(pool)
    for _ in range(N_PERM):
        i = rng.randrange(n_pool)
        j_ = rng.randrange(n_pool)
        # require different surahs, non-empty tokens already guaranteed
        while pool[j_][0] == pool[i][0]:
            j_ = rng.randrange(n_pool)
        ti = pool[i][2]
        tj = pool[j_][2]
        null_jaccards.append(jaccard(ti, tj))
        null_overlaps.append(overlap_coef(ti, tj))
        bi = bigrams(ti)
        bjj = bigrams(tj)
        null_bigrams.append((len(bi & bjj) / len(bi | bjj)) if (bi | bjj) else 0.0)

    p_jacc = sum(1 for v in null_jaccards if v >= j) / N_PERM
    p_over = sum(1 for v in null_overlaps if v >= ov) / N_PERM
    p_bi = sum(1 for v in null_bigrams if v >= bj) / N_PERM

    # MW-6 control: random pair from same two surahs (Q4 and Q39, neither = the named verses)
    q4_others = [v for v in quran[3]['verses'] if v['id'] != 1]
    q39_others = [v for v in quran[38]['verses'] if v['id'] != 6]
    control_jaccards = []
    rng2 = random.Random(SEED + 1)
    for _ in range(2000):
        v4 = rng2.choice(q4_others)
        v39 = rng2.choice(q39_others)
        control_jaccards.append(jaccard(tokenize(v4['text']), tokenize(v39['text'])))
    control_mean_jacc = sum(control_jaccards) / len(control_jaccards)

    summary = {
        'finding_id': 'Q004-F-04',
        'prereg_sha': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'verses': {'Q4:1': q4_1, 'Q39:6': q39_6},
        'tokens': {'Q4:1': a, 'Q39:6': b, 'shared_tokens': sorted(set(a) & set(b))},
        'token_jaccard': j,
        'token_overlap_coefficient': ov,
        'bigram_jaccard': bj,
        'null_distribution_size': N_PERM,
        'null_jaccard_mean': sum(null_jaccards) / N_PERM,
        'null_jaccard_p95': sorted(null_jaccards)[int(0.95 * N_PERM)],
        'p_token_jaccard_ge_observed': p_jacc,
        'p_overlap_ge_observed': p_over,
        'p_bigram_jaccard_ge_observed': p_bi,
        'mw6_control_q4_q39_random_pair_mean_jaccard': control_mean_jacc,
        'mw6_control_pairs': len(control_jaccards),
        'verdict': ('CONFIRMED' if j >= 0.30 and p_jacc < 0.01
                    else 'DIRECTIONAL' if j > sum(null_jaccards) / N_PERM
                    else 'NULL'),
    }

    out_path = os.path.join(ROOT, 'surahs', 'Q004-al-nisa', 'csv',
                            'Q004-F-04-twin-verse.json')
    with open(out_path, 'w') as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)
    print(f'Q4:1 ({len(a)} tokens) vs Q39:6 ({len(b)} tokens)')
    print(f'shared tokens ({len(set(a) & set(b))}): {sorted(set(a) & set(b))}')
    print(f'token Jaccard:           {j:.4f}  (p={p_jacc:.4f})')
    print(f'token overlap-coef:      {ov:.4f}  (p={p_over:.4f})')
    print(f'bigram Jaccard:          {bj:.4f}  (p={p_bi:.4f})')
    print(f'null mean jaccard: {sum(null_jaccards) / N_PERM:.4f}; null 95th: {sorted(null_jaccards)[int(0.95*N_PERM)]:.4f}')
    print(f'MW6 control (Q4-other vs Q39-other) mean jaccard: {control_mean_jacc:.4f}')
    print(f'verdict: {summary["verdict"]}')
    print(f'wrote {out_path}')


if __name__ == '__main__':
    main()
