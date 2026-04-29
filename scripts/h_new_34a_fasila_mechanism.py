#!/usr/bin/env python3
"""H-NEW-34a — Test the fāṣila rhyme-class pigeonhole mechanism for the
reverse-under-dispersion signal observed in H-NEW-34.

Pre-registered predictions:
  Sub-a: Within each fāṣila rhyme-class (verses grouped by terminal
         consonant), verse-final abjad residue χ² for m∈{7,11,19} should
         be SMALLER (tighter pigeonhole) than H-NEW-34's cross-corpus χ².
         Gate: weighted-mean within-class χ² significantly smaller than
         cross-corpus χ² via bootstrap over 1000 random partitions of
         equivalent size distribution — PASS at 99% CI exclusion.

  Sub-b: Verse-INITIAL (word position 0) abjad residues should NOT show
         reverse-under-dispersion vs matched Arabic prose.
         Gate: |z| ≤ 2 vs Bukhari & Jahiz baselines for all three moduli
         — PASS; |z| > 2.58 — FAIL.

Joint PASS → fāṣila mechanism confirmed.
Either FAIL → mechanism questioned.

Seed: 20260414 (reusing H-NEW-34's seed for reproducibility).
"""

import json
import math
import random
import re
import statistics
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260414
random.seed(SEED)

ABJAD = {
    'ا': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9, 'ي': 10,
    'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90,
    'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700,
    'ض': 800, 'ظ': 900, 'غ': 1000,
}
HAMZA_CARRIER = {
    'أ': 1, 'إ': 1, 'آ': 1, 'ٱ': 1,
    'ؤ': 6,
    'ئ': 10,
    'ى': 10,
    'ة': 5,
}


def word_abjad(word):
    total = 0
    for ch in word:
        if ch in ABJAD:
            total += ABJAD[ch]
        elif ch in HAMZA_CARRIER:
            total += HAMZA_CARRIER[ch]
    return total


def clean_word(word):
    return ''.join(ch for ch in word if ch in ABJAD or ch in HAMZA_CARRIER)


def terminal_consonant(cleaned_word):
    """Return the terminal letter of the cleaned word, mapping common
    rhyme-ending variants to canonical forms.

    For rhyme-class grouping, the terminal letter after stripping silent
    final long-vowel markers is more linguistically meaningful. But since
    we want a simple operationalization that matches classical fāṣila
    taxonomy (rhyme by rawī = last CONSONANT), we use the following rule:

    1. Take the last character of the cleaned word.
    2. If it is ا، و، ي، ى (long-vowel / matres lectionis) and the word
       has ≥ 2 letters, use the penultimate letter instead (the rawī).
    3. Hamza carriers map to their carrier letter class for rhyme.
    """
    if not cleaned_word:
        return None
    LONG_VOWELS = {'ا', 'و', 'ي', 'ى'}
    last = cleaned_word[-1]
    # Normalize hamza carriers into their rhyme-letter class by carrier identity
    # (this matches classical fāṣila which groups by pronounced letter)
    if last in LONG_VOWELS and len(cleaned_word) >= 2:
        # Take penultimate — this is the rawī in classical saj' when the
        # final is a long vowel / ridf.
        return cleaned_word[-2]
    return last


def chi_square_residues(values, m):
    counts = [0] * m
    for v in values:
        counts[v % m] += 1
    n = len(values)
    if n == 0:
        return 0.0, counts
    expected = n / m
    chi2 = sum((c - expected) ** 2 / expected for c in counts)
    return chi2, counts


# -----------------------------------------------------------------------------
# Load the Quran
# -----------------------------------------------------------------------------
Q = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text())

verse_records = []
for s in sorted(Q, key=lambda x: x['id']):
    for v in s['verses']:
        text = v['text'].strip()
        words = text.split()
        if not words:
            continue
        last_raw = words[-1]
        last_clean = clean_word(last_raw)
        first_raw = words[0]
        first_clean = clean_word(first_raw)
        if not last_clean:
            continue
        rec = {
            'surah': s['id'],
            'verse': v['id'],
            'last_word': last_raw,
            'last_clean': last_clean,
            'last_abjad': word_abjad(last_clean),
            'first_word': first_raw,
            'first_clean': first_clean,
            'first_abjad': word_abjad(first_clean) if first_clean else None,
            'rhyme_letter': terminal_consonant(last_clean),
        }
        verse_records.append(rec)

N_verses = len(verse_records)
print(f"Loaded {N_verses} verses with extractable final word", file=sys.stderr)

# Extract verse-initial records (where first word was non-empty after cleaning)
verse_initial = [r for r in verse_records if r['first_abjad'] is not None]
print(f"Verse-initial extractable: {len(verse_initial)}", file=sys.stderr)

# Note on basmala: at surah 1 the first verse is already the basmala. We treat
# verse-initial simply as the first orthographic token of each verse as stored
# in the amrayn JSON (basmala-counted-only-in-surah-1).

# -----------------------------------------------------------------------------
# Sub-a: group by rhyme-class, compute within-class χ²
# -----------------------------------------------------------------------------
by_rhyme = defaultdict(list)
for r in verse_records:
    rl = r['rhyme_letter']
    if rl is None:
        continue
    by_rhyme[rl].append(r['last_abjad'])

rhyme_counts = {letter: len(vals) for letter, vals in by_rhyme.items()}
print(f"\nRhyme-class distribution (top 20):", file=sys.stderr)
for letter, n in sorted(rhyme_counts.items(), key=lambda x: -x[1])[:20]:
    print(f"  {letter!r}: {n}", file=sys.stderr)

MODULI = [7, 11, 19]

# Reproduce H-NEW-34's cross-corpus χ² for comparison
quran_abjads = [r['last_abjad'] for r in verse_records]
cross_corpus_chi2 = {}
for m in MODULI:
    chi2, counts = chi_square_residues(quran_abjads, m)
    cross_corpus_chi2[m] = {'chi2': chi2, 'counts': counts}
    print(f"  cross-corpus m={m}: χ²={chi2:.3f}", file=sys.stderr)

# For each rhyme-class with ≥ 100 verses, compute its χ²
LARGE_CLASS_MIN = 100
large_classes = {l: v for l, v in by_rhyme.items() if len(v) >= LARGE_CLASS_MIN}
print(f"\nLarge rhyme-classes (N≥{LARGE_CLASS_MIN}): {len(large_classes)}", file=sys.stderr)

within_class_chi2 = {m: {} for m in MODULI}
for letter, vals in large_classes.items():
    for m in MODULI:
        chi2, counts = chi_square_residues(vals, m)
        within_class_chi2[m][letter] = {'chi2': chi2, 'n': len(vals)}

# Weighted-mean within-class χ² (weighted by class size)
weighted_mean_within = {}
for m in MODULI:
    total_n = sum(d['n'] for d in within_class_chi2[m].values())
    wm = sum(d['chi2'] * d['n'] for d in within_class_chi2[m].values()) / total_n
    weighted_mean_within[m] = wm
    print(f"\nm={m}: weighted-mean within-class χ² = {wm:.3f}  "
          f"(cross-corpus = {cross_corpus_chi2[m]['chi2']:.3f})", file=sys.stderr)


# -----------------------------------------------------------------------------
# Bootstrap null for sub-a: random partitions of equivalent class-size
# distribution
# -----------------------------------------------------------------------------
class_sizes = sorted([len(v) for v in large_classes.values()], reverse=True)
print(f"\nClass-size distribution used for bootstrap: {class_sizes}", file=sys.stderr)

N_BOOT = 1000
boot_weighted_mean = {m: [] for m in MODULI}
all_abjads = list(quran_abjads)

for b in range(N_BOOT):
    # Shuffle the pool, then split into groups matching class_sizes
    pool = all_abjads[:]
    random.shuffle(pool)
    idx = 0
    groups = []
    for sz in class_sizes:
        g = pool[idx:idx + sz]
        idx += sz
        groups.append(g)
    for m in MODULI:
        total_n = sum(len(g) for g in groups)
        wm = sum(chi_square_residues(g, m)[0] * len(g) for g in groups) / total_n
        boot_weighted_mean[m].append(wm)

# Compute empirical p-values and 99% CI
boot_stats = {}
for m in MODULI:
    nulls = sorted(boot_weighted_mean[m])
    mean = statistics.mean(nulls)
    sd = statistics.stdev(nulls)
    # One-sided: fraction of bootstrap samples with wm ≤ observed
    obs = weighted_mean_within[m]
    p_left = sum(1 for x in nulls if x <= obs) / len(nulls)
    ci99_low = nulls[int(0.005 * len(nulls))]
    ci99_high = nulls[int(0.995 * len(nulls))]
    boot_stats[m] = {
        'observed_weighted_mean': obs,
        'null_mean': mean,
        'null_sd': sd,
        'p_left': p_left,
        'ci99_low': ci99_low,
        'ci99_high': ci99_high,
        'z': (obs - mean) / sd if sd else 0.0,
    }
    print(f"\nm={m}: obs={obs:.3f}, null μ={mean:.3f} sd={sd:.3f}, "
          f"99%CI=[{ci99_low:.3f}, {ci99_high:.3f}], p_left={p_left:.4f}, "
          f"z={(obs-mean)/sd:+.3f}", file=sys.stderr)


# Gate: PASS at 99% CI exclusion — observed within-class weighted mean χ²
# must be below the lower 99% CI of bootstrap null.
sub_a_per_m = {
    m: (boot_stats[m]['observed_weighted_mean'] < boot_stats[m]['ci99_low'])
    for m in MODULI
}
sub_a_pass = all(sub_a_per_m.values())
print(f"\n=== Sub-a per modulus 99%CI-exclusion: {sub_a_per_m}", file=sys.stderr)
print(f"=== Sub-a overall: {'PASS' if sub_a_pass else 'FAIL'}", file=sys.stderr)


# -----------------------------------------------------------------------------
# Sub-b: verse-initial control
# -----------------------------------------------------------------------------
init_abjads = [r['first_abjad'] for r in verse_initial]

init_chi2 = {}
for m in MODULI:
    chi2, counts = chi_square_residues(init_abjads, m)
    init_chi2[m] = {'chi2': chi2, 'counts': counts}
    print(f"\nverse-initial m={m}: χ²={chi2:.3f}", file=sys.stderr)

# Baseline corpora (same as H-NEW-34)
AR_LETTER_PAT = re.compile(r'[\u0621-\u064A]')

def clean_arabic_text(text):
    out = []
    for ch in text:
        if AR_LETTER_PAT.match(ch):
            out.append(ch)
        elif ch.isspace():
            out.append(' ')
    return re.sub(r'\s+', ' ', ''.join(out)).strip()


def load_baseline(path):
    raw = Path(path).read_text(encoding='utf-8', errors='replace')
    cleaned = clean_arabic_text(raw)
    words = [w for w in cleaned.split() if clean_word(w)]
    return words


bukhari_words = load_baseline(ROOT / 'data/baseline-corpora/raw/bukhari-noquran.txt')
jahiz_words = load_baseline(ROOT / 'data/baseline-corpora/raw/jahiz-hayawan.txt')
print(f"\nBukhari pool: {len(bukhari_words)}, Jahiz pool: {len(jahiz_words)}", file=sys.stderr)


def baseline_null(words_pool, N, m, n_perm=1000):
    if len(words_pool) < N:
        return None
    chi2_list = []
    for _ in range(n_perm):
        sample = random.sample(words_pool, N)
        vals = [word_abjad(clean_word(w)) for w in sample]
        c2, _ = chi_square_residues(vals, m)
        chi2_list.append(c2)
    return chi2_list


N_init = len(init_abjads)
print(f"\n=== Verse-initial baseline nulls (N={N_init}, 1000 perms) ===", file=sys.stderr)

init_baseline = {}
for corpus_name, pool in [('bukhari', bukhari_words), ('jahiz', jahiz_words)]:
    init_baseline[corpus_name] = {}
    for m in MODULI:
        nulls = baseline_null(pool, N_init, m, 1000)
        if nulls is None:
            init_baseline[corpus_name][m] = None
            continue
        mean = statistics.mean(nulls)
        sd = statistics.stdev(nulls)
        q_chi2 = init_chi2[m]['chi2']
        z = (q_chi2 - mean) / sd
        init_baseline[corpus_name][m] = {
            'mean': mean, 'sd': sd, 'quran_chi2': q_chi2, 'z': z,
        }
        print(f"  {corpus_name} m={m}: Quran-init χ²={q_chi2:.3f}, null μ={mean:.3f} sd={sd:.3f}, z={z:+.3f}", file=sys.stderr)

# Sub-b gate: |z| ≤ 2 → PASS (no reverse under-dispersion);
# |z| > 2.58 → FAIL
z_values = []
for corpus_name in ['bukhari', 'jahiz']:
    for m in MODULI:
        z = init_baseline[corpus_name][m]['z']
        z_values.append((corpus_name, m, z))

max_abs_z = max(abs(z) for _, _, z in z_values)
sub_b_pass = max_abs_z <= 2.0
sub_b_fail = max_abs_z > 2.58
print(f"\n=== Sub-b z values: {z_values}", file=sys.stderr)
print(f"=== max|z| = {max_abs_z:.3f}", file=sys.stderr)
print(f"=== Sub-b: {'PASS' if sub_b_pass else ('FAIL' if sub_b_fail else 'AMBIGUOUS')}", file=sys.stderr)


# -----------------------------------------------------------------------------
# Joint verdict
# -----------------------------------------------------------------------------
joint = 'CONFIRMED' if (sub_a_pass and sub_b_pass) else 'QUESTIONED'
print(f"\n{'='*60}", file=sys.stderr)
print(f"JOINT VERDICT: fāṣila mechanism {joint}", file=sys.stderr)
print(f"  sub-a (within-class << cross-corpus): {'PASS' if sub_a_pass else 'FAIL'}", file=sys.stderr)
print(f"  sub-b (verse-initial null): {'PASS' if sub_b_pass else ('FAIL' if sub_b_fail else 'AMBIGUOUS')}", file=sys.stderr)
print(f"{'='*60}", file=sys.stderr)

# Output JSON
out = {
    'seed': SEED,
    'hypothesis': 'H-NEW-34a: fāṣila rhyme-class pigeonhole mechanism test',
    'rules_tuple': 'hafs-kufan, no-tashkeel, orthographic-token, graphemes, mashriqi abjad, hamza-carrier-policy, basmala-counted-only-in-surah-1',
    'moduli': MODULI,
    'n_verses': N_verses,
    'rhyme_class_min_size': LARGE_CLASS_MIN,
    'n_large_rhyme_classes': len(large_classes),
    'rhyme_class_sizes': {l: len(v) for l, v in by_rhyme.items()},
    'large_classes_used': list(large_classes.keys()),
    'cross_corpus_chi2': {m: cross_corpus_chi2[m]['chi2'] for m in MODULI},
    'within_class_chi2': {
        m: {letter: {'chi2': d['chi2'], 'n': d['n']} for letter, d in within_class_chi2[m].items()}
        for m in MODULI
    },
    'weighted_mean_within_class_chi2': {m: weighted_mean_within[m] for m in MODULI},
    'bootstrap_n_perm': N_BOOT,
    'bootstrap_stats': {m: boot_stats[m] for m in MODULI},
    'sub_a_per_m_pass': sub_a_per_m,
    'sub_a_pass': sub_a_pass,
    'n_verse_initial': N_init,
    'verse_initial_quran_chi2': {m: init_chi2[m]['chi2'] for m in MODULI},
    'verse_initial_baseline': init_baseline,
    'sub_b_max_abs_z': max_abs_z,
    'sub_b_pass': sub_b_pass,
    'sub_b_fail': sub_b_fail,
    'joint_verdict': joint,
}

out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-new-34a.json'
out_path.write_text(json.dumps(out, indent=2, default=str))
print(f"\nsaved: {out_path}", file=sys.stderr)
