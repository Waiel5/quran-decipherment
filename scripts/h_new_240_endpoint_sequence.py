#!/usr/bin/env python3
"""H-NEW-240: META-endpoint-sequence structural coherence.

Tests whether the ordered sequence of per-surah FIRST verses (post-muq) and LAST
verses, taken as two parallel 114-verse sequences in canonical mushaf order,
exhibit their own information-theoretic structure consistent with the parent
surah mushaf order.

Hypothesis: if the mushaf is a structured Hamiltonian cycle at the surah level
(cross-finding-013), then the first-verse-sequence and last-verse-sequence
should each also form partial cycles whose Fisher-Rao path length is
significantly below random permutation.

Pre-reg: bonferroni_k=2 (one for first-sequence, one for last-sequence),
alpha_bon=0.025, direction: empirical sequence z-score vs 500-permutation null
should be negative (shorter than random), i.e. z < -1.96 for each sequence.
Verdict: PENDING.

Seed: 20260419
"""
import json
import math
import random
from collections import Counter
from pathlib import Path

SEED = 20260419
random.seed(SEED)
DATA = Path('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json')
OUTPUT = Path('/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-240.json')

# Muqaṭṭaʿāt surahs (first verse is muq-opener): use v2 for these
MUQ_SURAHS = {
    2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
    36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68,
}


def load_corpus():
    with open(DATA) as f:
        data = json.load(f)
    return data


def tokenize(text):
    return [t for t in text.strip().split() if t.strip()]


def get_endpoint_verses(corpus):
    """For each of 114 surahs, return (first_content_verse_tokens, last_verse_tokens)."""
    first_verses = []
    last_verses = []
    for surah in corpus:
        surah_num = surah['id']
        verses = surah['verses']
        if surah_num in MUQ_SURAHS and len(verses) >= 2:
            first_text = verses[1]['text']
        else:
            first_text = verses[0]['text']
        last_text = verses[-1]['text']
        first_verses.append(tokenize(first_text))
        last_verses.append(tokenize(last_text))
    return first_verses, last_verses


def verse_as_char_4gram_bag(tokens):
    """Char-4-gram representation of a verse's concatenated tokens.

    Returns a normalized frequency distribution over 4-grams.
    """
    text = ''.join(tokens)  # concatenated no-space
    if len(text) < 4:
        return Counter([text])  # fallback for very short verses
    bag = Counter(text[i:i+4] for i in range(len(text) - 3))
    return bag


def fisher_rao_distance(bag1, bag2, smoothing=0.5):
    """Dirichlet-smoothed Fisher-Rao arccos-Bhattacharyya distance.

    d(p, q) = 2 * arccos( sum_i sqrt(p_i * q_i) )
    Smoothed: p_i_smooth = (n_i + alpha) / (N + alpha * V)
    with V = size of union vocabulary.
    """
    vocab = set(bag1) | set(bag2)
    if not vocab:
        return 0.0
    V = len(vocab)
    N1 = sum(bag1.values())
    N2 = sum(bag2.values())
    if N1 == 0 or N2 == 0:
        return math.pi / 2
    alpha = smoothing
    bc = 0.0
    for w in vocab:
        p1 = (bag1.get(w, 0) + alpha) / (N1 + alpha * V)
        p2 = (bag2.get(w, 0) + alpha) / (N2 + alpha * V)
        bc += math.sqrt(p1 * p2)
    bc = min(1.0, max(0.0, bc))
    return 2.0 * math.acos(bc)


def sequence_path_length(bags, order):
    total = 0.0
    for i in range(len(order) - 1):
        total += fisher_rao_distance(bags[order[i]], bags[order[i + 1]])
    return total


def permutation_null(bags, n_perms=500):
    n = len(bags)
    base = list(range(n))
    lengths = []
    for _ in range(n_perms):
        perm = list(base)
        random.shuffle(perm)
        lengths.append(sequence_path_length(bags, perm))
    mean = sum(lengths) / len(lengths)
    var = sum((x - mean) ** 2 for x in lengths) / (len(lengths) - 1)
    sd = math.sqrt(var)
    return {
        'n_perms': n_perms,
        'mean': mean,
        'sd': sd,
        'min': min(lengths),
        'max': max(lengths),
        'sample': lengths[:10],
    }


def main():
    print(f"Loading corpus from {DATA}")
    corpus = load_corpus()
    print(f"Corpus loaded: {len(corpus)} surahs")
    first_verses, last_verses = get_endpoint_verses(corpus)
    assert len(first_verses) == 114 and len(last_verses) == 114

    first_bags = [verse_as_char_4gram_bag(v) for v in first_verses]
    last_bags = [verse_as_char_4gram_bag(v) for v in last_verses]

    canonical_order = list(range(114))

    print("\n=== FIRST-VERSE-SEQUENCE ===")
    first_len = sequence_path_length(first_bags, canonical_order)
    first_null = permutation_null(first_bags, n_perms=500)
    first_z = (first_len - first_null['mean']) / first_null['sd']
    print(f"Canonical length: {first_len:.4f}")
    print(f"Null mean: {first_null['mean']:.4f}, sd: {first_null['sd']:.4f}")
    print(f"Z-score: {first_z:.4f}")
    print(f"Empirical p (one-sided, below-null): ~{sum(1 for x in [first_null['mean']] if x <= first_len)}")

    print("\n=== LAST-VERSE-SEQUENCE ===")
    last_len = sequence_path_length(last_bags, canonical_order)
    last_null = permutation_null(last_bags, n_perms=500)
    last_z = (last_len - last_null['mean']) / last_null['sd']
    print(f"Canonical length: {last_len:.4f}")
    print(f"Null mean: {last_null['mean']:.4f}, sd: {last_null['sd']:.4f}")
    print(f"Z-score: {last_z:.4f}")

    out = {
        'id': 'H-NEW-240',
        'seed': SEED,
        'first_sequence': {
            'canonical_length': first_len,
            'null_mean': first_null['mean'],
            'null_sd': first_null['sd'],
            'z_score': first_z,
        },
        'last_sequence': {
            'canonical_length': last_len,
            'null_mean': last_null['mean'],
            'null_sd': last_null['sd'],
            'z_score': last_z,
        },
        'bonferroni_k': 2,
        'alpha_bon': 0.025,
        'interpretation': (
            'Negative z = canonical endpoint-sequence shorter than random; '
            'positive evidence for meta-level mushaf coherence at endpoint layer.'
        ),
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT, 'w') as f:
        json.dump(out, f, indent=2)
    print(f"\nResults written to {OUTPUT}")


if __name__ == '__main__':
    main()
