#!/usr/bin/env python3
"""
Q031-F-03 — Q 31:12-19 Luqmān-pericope lexical-isolation from rest of Q 31.

Pre-reg: surahs/Q031-luqman/preregs/Q031-F-03-luqman-pericope-isolation-prereg.md
Pre-reg SHA256: e21dd7b4c587ba816c744677518bd7612b4736d124fdceba6aceccc12ff39575
Seed: 20260509
Direction: positive (pericope lexical-isolation > random 8-verse spans of Q 31)
"""
import json
import re
import hashlib
import random
import sys
import math
from pathlib import Path
from collections import Counter

ROOT = Path('/Users/grey/Downloads/quran')
PREREG_PATH = ROOT / 'surahs/Q031-luqman/preregs/Q031-F-03-luqman-pericope-isolation-prereg.md'
EXPECTED_SHA = 'e21dd7b4c587ba816c744677518bd7612b4736d124fdceba6aceccc12ff39575'
OUT_PATH = ROOT / 'surahs/Q031-luqman/csv/Q031-F-03.json'
CORPUS_PATH = ROOT / 'quran-text/quran-no-tashkeel.json'
SEED = 20260509
N_PERM = 10000


def verify_prereg_sha():
    with open(PREREG_PATH, 'rb') as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {sha}")
    return sha


def tokenize(text):
    cleaned = re.sub(r'[ۖۚۗۘۙۛۜ۝]', ' ', text)
    return [t for t in cleaned.split() if t]


def cosine_distance(c1, c2):
    """1 - cosine similarity between two Counters."""
    keys = set(c1.keys()) | set(c2.keys())
    dot = sum(c1.get(k, 0) * c2.get(k, 0) for k in keys)
    n1 = math.sqrt(sum(v * v for v in c1.values()))
    n2 = math.sqrt(sum(v * v for v in c2.values()))
    if n1 == 0 or n2 == 0:
        return 1.0
    return 1.0 - dot / (n1 * n2)


def main():
    sha = verify_prereg_sha()
    print(f"PRE-REG SHA verified: {sha[:16]}...")

    rng = random.Random(SEED)
    with open(CORPUS_PATH) as f:
        corpus = json.load(f)

    # Q 31 (0-idx 30)
    q31 = corpus[30]
    verses = [tokenize(v['text']) for v in q31['verses']]
    n_verses = len(verses)
    print(f"Q 31 has {n_verses} verses; tokens per verse range: {[len(v) for v in verses]}")

    pericope_start = 11  # v.12 is index 11 (0-indexed)
    pericope_end = 19  # exclusive (vv.12-19 = indices 11..18 inclusive = 8 verses)
    pericope_verses = verses[pericope_start:pericope_end]
    rest_verses = verses[:pericope_start] + verses[pericope_end:]

    pericope_tokens = Counter()
    for v in pericope_verses:
        pericope_tokens.update(v)
    rest_tokens = Counter()
    for v in rest_verses:
        rest_tokens.update(v)

    observed_isolation = cosine_distance(pericope_tokens, rest_tokens)
    print(f"\nPericope (vv.12-19, 8 verses) vs rest-of-Q31 (vv.1-11 + 20-34, 26 verses):")
    print(f"  Pericope token-types: {len(pericope_tokens)}")
    print(f"  Rest token-types: {len(rest_tokens)}")
    print(f"  Cosine distance: {observed_isolation:.4f}")

    # Permutation null: 10,000 random contiguous 8-verse windows of Q 31
    perm_isolations = []
    valid_starts = list(range(n_verses - 8 + 1))  # starts 0..26 (gives spans of 8 verses)
    for _ in range(N_PERM):
        start = rng.choice(valid_starts)
        span = verses[start:start + 8]
        comp = verses[:start] + verses[start + 8:]
        span_tok = Counter()
        comp_tok = Counter()
        for v in span:
            span_tok.update(v)
        for v in comp:
            comp_tok.update(v)
        perm_isolations.append(cosine_distance(span_tok, comp_tok))

    p_one_tailed = sum(1 for x in perm_isolations if x >= observed_isolation) / N_PERM
    null_mean = sum(perm_isolations) / len(perm_isolations)
    print(f"\nPerm null (10,000 random 8-verse contiguous spans):")
    print(f"  Mean: {null_mean:.4f}")
    print(f"  Max: {max(perm_isolations):.4f}")
    print(f"  Min: {min(perm_isolations):.4f}")
    print(f"  P(perm ≥ observed): {p_one_tailed:.4f}")

    # Verdict
    alpha = 0.05
    if p_one_tailed < alpha:
        verdict = 'PASS-DIRECTED (single-test α=0.05)'
    elif observed_isolation > null_mean:
        verdict = 'DIRECTIONAL (observed > null mean but p ≥ 0.05)'
    else:
        verdict = 'NULL'

    result = {
        'test_id': 'Q031-F-03',
        'title': 'Q 31 Luqmān-pericope lexical-isolation',
        'pre_reg_sha256': sha,
        'pre_reg_sha_expected': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'pericope_range_1idx': [12, 19],
        'pericope_n_verses': 8,
        'rest_n_verses': n_verses - 8,
        'observed_cosine_distance': observed_isolation,
        'perm_null_mean': null_mean,
        'perm_null_max': max(perm_isolations),
        'perm_null_min': min(perm_isolations),
        'perm_p_one_tailed': p_one_tailed,
        'alpha': alpha,
        'verdict': verdict,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(f"\nResult written to: {OUT_PATH}")
    print(f"Verdict: {verdict}")
    return result


if __name__ == '__main__':
    main()
