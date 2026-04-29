#!/usr/bin/env python3
"""H-NEW-16 — Cross-word phonetic palindromes.

Scan for palindromic consonant-substrings ℓ ≥ 7 that cross word boundaries
after basic tajwīd normalization (hamzat al-waṣl deletion via alif-removal
at word-start after connector). Compare vs word-shuffle null and bigram
Markov null.

Bonferroni k=3, α_bon = 0.01/3 = 0.00333.
Seed 20260413.
"""
import json, math, random, re, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
random.seed(20260413)

AR_LETTER = re.compile(r'[\u0621-\u064A]')
NORMALIZE = {
    'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا',
    'ء': 'ا',
    'ؤ': 'و', 'ئ': 'ي',
    'ى': 'ي', 'ة': 'ه',
}

def clean(text):
    return ''.join(NORMALIZE.get(c, c) for c in text if AR_LETTER.match(c))

def tajwid_normalize(verse_text):
    """Apply minimal tajwīd: strip tashkeel, collapse shadda-doubling,
    delete hamzat al-waṣl at internal word-start positions.
    Returns concatenated consonant string (word-boundaries erased)."""
    words = verse_text.split()
    out = []
    for i, w in enumerate(words):
        cleaned_w = clean(w)
        # Simple: if word starts with ا and previous word ends with a consonant,
        # drop the ا (hamzat al-waṣl)
        if i > 0 and cleaned_w.startswith('ا') and out and out[-1] not in ('ا', 'و', 'ي'):
            cleaned_w = cleaned_w[1:]
        out.append(cleaned_w)
    return ''.join(out)

# Pure word-level concatenation (control)
def raw_concat(verse_text):
    return clean(verse_text)

# ---- Load Quran ----
Q = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text())
verses = []
for s in sorted(Q, key=lambda x: x['id']):
    for v in s['verses']:
        verses.append((s['id'], v['id'], v['text']))

# Produce two strings per verse: raw concat (no word boundary erasure) and tajwid
verse_strings_tajwid = [(sid, vid, tajwid_normalize(t)) for sid, vid, t in verses]
# Also precompute per-verse concatenation with whitespace preserved (for word-shuffle null)
verse_words = [(sid, vid, [clean(w) for w in t.split() if clean(w)]) for sid, vid, t in verses]
print(f"verses: {len(verses)}", file=sys.stderr)
total_chars = sum(len(s) for _, _, s in verse_strings_tajwid)
print(f"total tajwid chars: {total_chars}", file=sys.stderr)

# ---- Palindrome finder ----
def find_palindromes(text, min_length=7):
    """Return list of (start, length, substring, crosses_word_boundary) for all
    maximal palindromic substrings of length >= min_length.
    Uses Manacher-like expansion from each center.
    For simplicity, brute-force: check each substring O(n^2)."""
    palindromes = []
    n = len(text)
    # Odd-length palindromes
    for center in range(n):
        r = 0
        while center - r >= 0 and center + r < n and text[center - r] == text[center + r]:
            length = 2 * r + 1
            if length >= min_length:
                palindromes.append((center - r, length, text[center - r:center + r + 1]))
            r += 1
    # Even-length palindromes
    for center in range(n - 1):
        l, r = center, center + 1
        while l >= 0 and r < n and text[l] == text[r]:
            length = r - l + 1
            if length >= min_length:
                palindromes.append((l, length, text[l:r + 1]))
            l -= 1
            r += 1
    return palindromes

def count_palindromes(text, min_length=7):
    """Count palindromic substrings of length >= min_length (non-unique positions)."""
    return len(find_palindromes(text, min_length))

# ---- Observed count ----
print("\n=== Observed palindrome counts per verse ===", file=sys.stderr)
total_pal = 0
per_verse_counts = []
for sid, vid, s in verse_strings_tajwid:
    c = count_palindromes(s, min_length=7)
    per_verse_counts.append((sid, vid, c, len(s)))
    total_pal += c

print(f"total palindromes ≥7: {total_pal}", file=sys.stderr)
# Sum of counts
total_chars_scanned = sum(v[3] for v in per_verse_counts)
rate = total_pal / total_chars_scanned if total_chars_scanned > 0 else 0
print(f"rate per char: {rate:.6f}", file=sys.stderr)

# ---- Null 1: Word-shuffle within verse ----
print("\n=== Null 1: within-verse word-shuffle (200 perms) ===", file=sys.stderr)
def word_shuffle_null(n_perm=200):
    null_counts = []
    for _ in range(n_perm):
        total = 0
        for sid, vid, words in verse_words:
            if len(words) < 2:
                continue
            shuffled = words[:]
            random.shuffle(shuffled)
            # Re-apply tajwid normalization on shuffled (use raw concat here
            # since word order changed — tajwid rules re-apply)
            # For consistency, use simple concatenation of cleaned words
            s = ''.join(shuffled)
            total += count_palindromes(s, min_length=7)
        null_counts.append(total)
    return null_counts

n1 = word_shuffle_null(200)
n1_mean = sum(n1) / len(n1)
n1_sd = (sum((x - n1_mean) ** 2 for x in n1) / (len(n1) - 1)) ** 0.5
z1 = (total_pal - n1_mean) / n1_sd if n1_sd > 0 else 0
from math import erf, sqrt
p1 = 0.5 * (1 - erf(z1 / sqrt(2)))
print(f"null1: mean={n1_mean:.1f} ± {n1_sd:.2f}, z={z1:.3f}, p={p1:.5f}", file=sys.stderr)

# ---- Null 2: Bigram Markov sampling ----
print("\n=== Null 2: bigram Markov (100 perms) ===", file=sys.stderr)
# Build bigram model from full Quran tajwid-normalized text
full_str = ''.join(s for _, _, s in verse_strings_tajwid)
bigram_model = defaultdict(Counter)
unigram = Counter(full_str)
for i in range(len(full_str) - 1):
    bigram_model[full_str[i]][full_str[i + 1]] += 1
alphabet = sorted(unigram.keys())

def sample_markov(n_chars):
    """Sample a bigram-Markov string of length n_chars."""
    # Start from unigram distribution
    syms = list(unigram.keys())
    weights = [unigram[s] for s in syms]
    first = random.choices(syms, weights=weights, k=1)[0]
    out = [first]
    for _ in range(n_chars - 1):
        counter = bigram_model.get(out[-1])
        if not counter:
            out.append(random.choices(syms, weights=weights, k=1)[0])
        else:
            ks = list(counter.keys())
            ws = [counter[k] for k in ks]
            out.append(random.choices(ks, weights=ws, k=1)[0])
    return ''.join(out)

def bigram_null(n_perm=100):
    null_counts = []
    for _ in range(n_perm):
        # Sample length-matched string per verse
        total = 0
        for sid, vid, s in verse_strings_tajwid:
            if len(s) < 7:
                continue
            sampled = sample_markov(len(s))
            total += count_palindromes(sampled, min_length=7)
        null_counts.append(total)
    return null_counts

n2 = bigram_null(100)
n2_mean = sum(n2) / len(n2)
n2_sd = (sum((x - n2_mean) ** 2 for x in n2) / (len(n2) - 1)) ** 0.5
z2 = (total_pal - n2_mean) / n2_sd if n2_sd > 0 else 0
p2 = 0.5 * (1 - erf(z2 / sqrt(2)))
print(f"null2: mean={n2_mean:.1f} ± {n2_sd:.2f}, z={z2:.3f}, p={p2:.5f}", file=sys.stderr)

# ---- Sub-analysis: verse-ends vs centers (Null 3 conditional) ----
print("\n=== Sub: verse-end cluster analysis ===", file=sys.stderr)
# For each palindrome found, compute distance from nearest verse boundary
# (in the full concat). Count palindromes whose midpoint is within 10 chars
# of a verse boundary.
# Use the tajwid-concatenated full string as baseline:
cumulative_pos = []
pos = 0
for sid, vid, s in verse_strings_tajwid:
    cumulative_pos.append((pos, pos + len(s), sid, vid))
    pos += len(s)
full_tajwid = ''.join(s for _, _, s in verse_strings_tajwid)

all_pals = find_palindromes(full_tajwid, min_length=7)
# For each palindrome, find which verse it belongs to and distance from verse end
near_end = 0
near_center = 0
for start, length, _ in all_pals:
    mid = start + length // 2
    for lo, hi, sid, vid in cumulative_pos:
        if lo <= mid < hi:
            verse_len = hi - lo
            dist_to_end = hi - mid
            dist_to_start = mid - lo
            if dist_to_end <= 10 or dist_to_start <= 10:
                near_end += 1
            else:
                near_center += 1
            break

total_full = len(all_pals)
print(f"full concat palindromes: {total_full}", file=sys.stderr)
print(f"near verse-boundary (≤10 chars): {near_end}", file=sys.stderr)
print(f"center (>10 chars): {near_center}", file=sys.stderr)

# ---- Verdicts ----
ALPHA_BON = 0.01 / 3
null1_pass = p1 < ALPHA_BON
null2_pass = p2 < ALPHA_BON
joint = null1_pass and null2_pass

print("\n=== Verdicts (Bonferroni k=3, α_bon=0.00333) ===", file=sys.stderr)
print(f"Null 1 (word-shuffle): z={z1:.3f}, p={p1:.5f}: {'PASS' if null1_pass else 'FAIL'}", file=sys.stderr)
print(f"Null 2 (bigram Markov): z={z2:.3f}, p={p2:.5f}: {'PASS' if null2_pass else 'FAIL'}", file=sys.stderr)
print(f"Joint: {'PASS' if joint else 'FAIL'}", file=sys.stderr)

# Top 10 longest palindromes
all_pals_sorted = sorted(all_pals, key=lambda x: -x[1])[:15]
print("\nTop 15 longest palindromes (full tajwid concat):", file=sys.stderr)
for start, length, substr in all_pals_sorted[:15]:
    print(f"  len {length}: '{substr}' at pos {start}", file=sys.stderr)

# ---- Output ----
out = {
    'seed': 20260413,
    'hypothesis': 'H-NEW-16 cross-word phonetic palindromes ℓ≥7',
    'rules_tuple': 'no-tashkeel, tajwid-normalized, rasm-consonant, hamza→alif, 28-letter',
    'total_chars_scanned': total_chars_scanned,
    'total_palindromes': total_pal,
    'full_concat_palindromes': total_full,
    'near_verse_boundary': near_end,
    'center': near_center,
    'null1_word_shuffle': {
        'mean': n1_mean, 'sd': n1_sd, 'z': z1, 'p': p1, 'pass': null1_pass,
    },
    'null2_bigram_markov': {
        'mean': n2_mean, 'sd': n2_sd, 'z': z2, 'p': p2, 'pass': null2_pass,
    },
    'joint_pass': joint,
    'top_15_palindromes': [[start, length, substr] for start, length, substr in all_pals_sorted],
    'bonferroni_k': 3,
    'alpha_bon': ALPHA_BON,
}
out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-new-16-palindromes.json'
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, indent=2, default=str))
print(f"\nsaved: {out_path}", file=sys.stderr)
