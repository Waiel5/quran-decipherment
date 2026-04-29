#!/usr/bin/env python3
"""H-NEW-65 — Fātiḥa-as-DNA: comprehensive 6-axis microcosm test.

Pre-reg: findings/phase-b-hypotheses/h-new-65-fatiha-as-dna-prereg.md
Locked: 2026-04-15.

6 axes (Bonferroni k=6, α_bon = 0.00833):
  1. LEXICAL    — mean log-token-frequency of distinct word-types in Fātiḥa
                  vs sliding 7-verse-window null. Direction: UPPER.
  2. SEMANTIC   — count of theme-classes (5) covered (locked keyword sets).
                  Direction: UPPER.
  3. PHONETIC   — log-likelihood of Fātiḥa's 7 verse-final letters under
                  corpus-wide rhyme distribution. Direction: UPPER.
  4. STRUCTURAL — KS statistic between Fātiḥa's 7 verse-word-counts and
                  corpus-wide CDF. Direction: LOWER (small KS = representative).
  5. COMPRESSION — gzip cross-compression gain g(prefix)=
                  (c(rest) - (c(prefix+rest) - c(prefix))) / c(rest).
                  Direction: UPPER. Null: 1000 random sliding-window prefixes.
  6. LETTER_COVERAGE — count of distinct pharyngeal/glottal letters
                  {ا,ه,ع,ح} appearing as first-letter-of-some-token.
                  Direction: UPPER.

Overall PASS criterion: ≥ 2 of 6 axes Bonferroni-significant.
   1 axis = REFUTED-WEAK; 0 axes = REFUTED-STRONG.

Rules tuple: (no-tashkeel; word-segment substring + first-letter-of-token
first-letter rule; hafs-kufan; 6236 verses; basmala-counted-only-in-surah-1;
mashriqi).
Seed: 20260416.
"""
from __future__ import annotations

import gzip
import json
import math
import random
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260416
BON_K = 6
ALPHA_BON = 0.05 / BON_K  # 0.008333...
PERCENTILE_PASS_UPPER = 1 - ALPHA_BON  # 0.99167
PERCENTILE_PASS_LOWER = ALPHA_BON       # 0.00833

# ---------- Load corpus ----------
with open(ROOT / 'quran-text/quran-no-tashkeel.json', encoding='utf-8') as f:
    corpus = json.load(f)
assert len(corpus) == 114, f"Expected 114 surahs, got {len(corpus)}"

# Flat verse list with global index
verses = []  # list of dicts: {gid, sid, vid, text, words, word_count, final_letter}
ARABIC_LETTERS = re.compile(r'[ء-ي]')

for surah in corpus:
    sid = surah['id']
    for v in surah['verses']:
        text = v['text']
        words = text.split()
        clean = ARABIC_LETTERS.findall(text)
        final = clean[-1] if clean else None
        verses.append({
            'gid': len(verses),
            'sid': sid,
            'vid': v['id'],
            'text': text,
            'words': words,
            'word_count': len(words),
            'final_letter': final,
        })

assert len(verses) == 6236, f"Expected 6236 verses, got {len(verses)}"

# Sliding 7-verse windows: [0..N-7] (inclusive) → N - 6 = 6230 windows
N_VERSES = len(verses)
WINDOW = 7
N_WINDOWS = N_VERSES - WINDOW + 1
assert N_WINDOWS == 6230

# Fātiḥa = first 7 verses (Q 1:1-7)
fatiha = verses[:7]
assert all(v['sid'] == 1 for v in fatiha)
fatiha_words = [w for v in fatiha for w in v['words']]
fatiha_distinct = set(fatiha_words)

# Pre-compute corpus-wide token frequency (over ALL tokens of ALL verses)
all_tokens = [w for v in verses for w in v['words']]
token_freq = Counter(all_tokens)
TOTAL_TOKENS = sum(token_freq.values())

# ============================================================
# AXIS 1 — LEXICAL: mean log-token-frequency of distinct word-types
# ============================================================
def axis1_metric(window_verses):
    """Mean log( token_freq(t) ) over distinct word-types in the window."""
    types = set()
    for v in window_verses:
        types.update(v['words'])
    if not types:
        return float('-inf')
    logs = [math.log(token_freq[t]) for t in types if t in token_freq]
    if not logs:
        return float('-inf')
    return sum(logs) / len(logs)

axis1_fatiha = axis1_metric(fatiha)
axis1_null = [axis1_metric(verses[i:i+WINDOW]) for i in range(N_WINDOWS)]
# percentile = fraction of null ≤ fatiha (one-sided UPPER → high percentile is significant)
axis1_pct = sum(1 for x in axis1_null if x <= axis1_fatiha) / len(axis1_null)
axis1_p = sum(1 for x in axis1_null if x >= axis1_fatiha) / len(axis1_null)
axis1_pass = axis1_pct >= PERCENTILE_PASS_UPPER

# ============================================================
# AXIS 2 — SEMANTIC: theme-class coverage (locked 5 keyword sets)
# ============================================================
THEMES = {
    'praise':       ['حمد', 'سبح', 'مجد', 'تبرك', 'تبارك'],
    'mercy':        ['رحم', 'رحمن', 'رحيم', 'غفر', 'غفور'],
    'judgment':     ['دين', 'حكم', 'يوم الدين', 'جزاء', 'ميزان'],
    'guidance':     ['هدى', 'هدي', 'اهد', 'صراط', 'مستقيم'],
    'supplication': ['دعا', 'دعو', 'ادع', 'اللهم', 'نعب'],
}

def axis2_metric(window_verses):
    """Count of theme-classes (out of 5) for which window contains ≥1 keyword (substring search)."""
    joined = ' '.join(v['text'] for v in window_verses)
    count = 0
    for theme, kws in THEMES.items():
        if any(kw in joined for kw in kws):
            count += 1
    return count

axis2_fatiha = axis2_metric(fatiha)
axis2_null = [axis2_metric(verses[i:i+WINDOW]) for i in range(N_WINDOWS)]
axis2_pct = sum(1 for x in axis2_null if x <= axis2_fatiha) / len(axis2_null)
axis2_p = sum(1 for x in axis2_null if x >= axis2_fatiha) / len(axis2_null)
axis2_pass = axis2_pct >= PERCENTILE_PASS_UPPER

# ============================================================
# AXIS 3 — PHONETIC: LL of verse-final letters under corpus rhyme distribution
# ============================================================
final_letter_counts = Counter(v['final_letter'] for v in verses if v['final_letter'])
TOTAL_FINALS = sum(final_letter_counts.values())
final_letter_p = {ch: c / TOTAL_FINALS for ch, c in final_letter_counts.items()}
LOG_EPS = math.log(1.0 / (10 * TOTAL_FINALS))  # smoothing for any unseen letter

def axis3_metric(window_verses):
    ll = 0.0
    for v in window_verses:
        ch = v['final_letter']
        if ch and ch in final_letter_p:
            ll += math.log(final_letter_p[ch])
        else:
            ll += LOG_EPS
    return ll

axis3_fatiha = axis3_metric(fatiha)
axis3_null = [axis3_metric(verses[i:i+WINDOW]) for i in range(N_WINDOWS)]
axis3_pct = sum(1 for x in axis3_null if x <= axis3_fatiha) / len(axis3_null)
axis3_p = sum(1 for x in axis3_null if x >= axis3_fatiha) / len(axis3_null)
axis3_pass = axis3_pct >= PERCENTILE_PASS_UPPER

# ============================================================
# AXIS 4 — STRUCTURAL: KS statistic of word-count distribution vs corpus
# ============================================================
all_word_counts = sorted(v['word_count'] for v in verses)
N_ALL_WC = len(all_word_counts)

def empirical_cdf(sorted_xs, x):
    """Right-continuous empirical CDF: fraction of sorted_xs ≤ x."""
    # binary search
    lo, hi = 0, len(sorted_xs)
    while lo < hi:
        mid = (lo + hi) // 2
        if sorted_xs[mid] <= x:
            lo = mid + 1
        else:
            hi = mid
    return lo / len(sorted_xs)

def ks_statistic(window_verses):
    wcs = sorted(v['word_count'] for v in window_verses)
    n = len(wcs)
    # KS = sup_x |F_window(x) - F_corpus(x)|.
    # Evaluate at all step-points (window x's and corpus x's of relevance).
    # Use union of unique values from both.
    candidates = set(wcs) | set(all_word_counts)
    d = 0.0
    for x in candidates:
        f_w = empirical_cdf(wcs, x)
        f_c = empirical_cdf(all_word_counts, x)
        d = max(d, abs(f_w - f_c))
    return d

axis4_fatiha = ks_statistic(fatiha)
axis4_null = [ks_statistic(verses[i:i+WINDOW]) for i in range(N_WINDOWS)]
# LOWER direction: percentile = fraction of null ≥ fatiha (smaller KS → more representative)
axis4_pct_lower = sum(1 for x in axis4_null if x <= axis4_fatiha) / len(axis4_null)
axis4_p = sum(1 for x in axis4_null if x <= axis4_fatiha) / len(axis4_null)
axis4_pass = axis4_pct_lower <= PERCENTILE_PASS_LOWER

# ============================================================
# AXIS 5 — COMPRESSION: gzip cross-compression gain
# ============================================================
SEP = '\n'

def gz_size(s: str) -> int:
    return len(gzip.compress(s.encode('utf-8'), compresslevel=9))

# Build full corpus text and chunked rest for prefix experiments
all_verse_texts = [v['text'] for v in verses]
fatiha_text = SEP.join(all_verse_texts[:7])
rest_text   = SEP.join(all_verse_texts[7:])
c_rest = gz_size(rest_text)

def compression_gain(prefix_text: str) -> float:
    c_prefix = gz_size(prefix_text)
    c_combined = gz_size(prefix_text + SEP + rest_text)
    return (c_rest - (c_combined - c_prefix)) / c_rest

axis5_fatiha = compression_gain(fatiha_text)

# Null: 1000 random sliding-window prefixes (seed 20260416)
rng = random.Random(SEED)
all_window_indices = list(range(N_WINDOWS))
sample_indices = rng.sample(all_window_indices, 1000)
axis5_null = []
for idx in sample_indices:
    prefix = SEP.join(all_verse_texts[idx:idx+WINDOW])
    axis5_null.append(compression_gain(prefix))
axis5_pct = sum(1 for x in axis5_null if x <= axis5_fatiha) / len(axis5_null)
axis5_p = sum(1 for x in axis5_null if x >= axis5_fatiha) / len(axis5_null)
axis5_pass = axis5_pct >= PERCENTILE_PASS_UPPER

# ============================================================
# AXIS 6 — LETTER COVERAGE: pharyngeal/glottal first-letter coverage
# ============================================================
PHAR_GLOT = {'ا', 'ه', 'ع', 'ح'}

def axis6_metric(window_verses):
    first_letters = set()
    for v in window_verses:
        for w in v['words']:
            arabic = ARABIC_LETTERS.findall(w)
            if arabic:
                first_letters.add(arabic[0])
    return len(first_letters & PHAR_GLOT)

axis6_fatiha = axis6_metric(fatiha)
axis6_null = [axis6_metric(verses[i:i+WINDOW]) for i in range(N_WINDOWS)]
axis6_pct = sum(1 for x in axis6_null if x <= axis6_fatiha) / len(axis6_null)
axis6_p = sum(1 for x in axis6_null if x >= axis6_fatiha) / len(axis6_null)
axis6_pass = axis6_pct >= PERCENTILE_PASS_UPPER

# ============================================================
# MW-5 sanity controls
# ============================================================
# Locate Q 59:22-24 window; Q 26:1-7 window
def find_window_for(sid, vid_start):
    for i, v in enumerate(verses):
        if v['sid'] == sid and v['vid'] == vid_start:
            return i
    return None

# Q 59:22-24 → use 7-verse window starting at v22 (so verses 22-28 inside surah 59 ideally;
# surah 59 has 24 verses, so the window will spill into next surah; that's expected for the
# sliding-window null which is corpus-wide). Anchor at 59:22.
idx_5922 = find_window_for(59, 22)
mw5_5922_axis1 = axis1_metric(verses[idx_5922:idx_5922+WINDOW]) if idx_5922 is not None else None
mw5_5922_axis2 = axis2_metric(verses[idx_5922:idx_5922+WINDOW]) if idx_5922 is not None else None

# Q 26:1-7
idx_26 = find_window_for(26, 1)
mw5_26_axis4 = ks_statistic(verses[idx_26:idx_26+WINDOW]) if idx_26 is not None else None

# ============================================================
# Assemble results
# ============================================================
def summarize_null(xs):
    xs_s = sorted(xs)
    n = len(xs_s)
    return {
        'n': n,
        'min': xs_s[0],
        'q01': xs_s[int(0.01 * n)],
        'q05': xs_s[int(0.05 * n)],
        'q25': xs_s[int(0.25 * n)],
        'median': xs_s[n // 2],
        'q75': xs_s[int(0.75 * n)],
        'q95': xs_s[int(0.95 * n)],
        'q99': xs_s[int(0.99 * n)],
        'max': xs_s[-1],
        'mean': sum(xs_s) / n,
    }

def axis_result(name, fatiha_val, null_xs, pct, p_value, passed, direction):
    return {
        'axis': name,
        'direction': direction,
        'fatiha_value': fatiha_val,
        'null_summary': summarize_null(null_xs),
        'percentile_lower_tail': pct,  # fraction of null ≤ fatiha
        'p_value_one_sided': p_value,
        'alpha_bon': ALPHA_BON,
        'pass': bool(passed),
    }

results = {
    'hypothesis_id': 'H-NEW-65',
    'title': 'Fātiḥa-as-DNA — 6-axis microcosm test',
    'rules_tuple': '(no-tashkeel; word-segment substring + first-letter-of-token; '
                   'hafs-kufan; 6236 verses; basmala-counted-only-in-surah-1; mashriqi)',
    'seed': SEED,
    'bonferroni_k': BON_K,
    'alpha_bon': ALPHA_BON,
    'fatiha_word_counts': [v['word_count'] for v in fatiha],
    'fatiha_final_letters': [v['final_letter'] for v in fatiha],
    'axes': [
        axis_result('1_lexical_mean_log_token_freq', axis1_fatiha, axis1_null,
                    axis1_pct, axis1_p, axis1_pass, 'upper'),
        axis_result('2_semantic_theme_coverage', axis2_fatiha, axis2_null,
                    axis2_pct, axis2_p, axis2_pass, 'upper'),
        axis_result('3_phonetic_rhyme_LL', axis3_fatiha, axis3_null,
                    axis3_pct, axis3_p, axis3_pass, 'upper'),
        axis_result('4_structural_KS_word_count', axis4_fatiha, axis4_null,
                    axis4_pct_lower, axis4_p, axis4_pass, 'lower'),
        axis_result('5_compression_gzip_gain', axis5_fatiha, axis5_null,
                    axis5_pct, axis5_p, axis5_pass, 'upper'),
        axis_result('6_letter_coverage_pharyngeal_glottal', axis6_fatiha, axis6_null,
                    axis6_pct, axis6_p, axis6_pass, 'upper'),
    ],
    'mw5_controls': {
        'Q59_22_window_axis1_lexical': mw5_5922_axis1,
        'Q59_22_window_axis2_semantic': mw5_5922_axis2,
        'Q26_1_window_axis4_KS': mw5_26_axis4,
    },
}

n_pass = sum(1 for a in results['axes'] if a['pass'])
results['n_axes_pass'] = n_pass
if n_pass >= 2:
    results['overall_verdict'] = 'PASS'
elif n_pass == 1:
    results['overall_verdict'] = 'REFUTED-WEAK'
else:
    results['overall_verdict'] = 'REFUTED-STRONG'

# Write JSON
out_json = ROOT / 'findings/phase-b-hypotheses/csv/h-new-65.json'
out_json.parent.mkdir(parents=True, exist_ok=True)
with open(out_json, 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

# Print human-readable summary to stdout
print("=" * 70)
print("H-NEW-65 — Fātiḥa-as-DNA (6 axes, Bonferroni k=6, α_bon=0.00833)")
print("=" * 70)
print(f"Fātiḥa word counts: {results['fatiha_word_counts']}")
print(f"Fātiḥa final letters: {results['fatiha_final_letters']}")
print()
for a in results['axes']:
    arrow = '↑' if a['direction'] == 'upper' else '↓'
    star = ' ***' if a['pass'] else ''
    print(f"Axis {a['axis']}  ({arrow})")
    print(f"  Fātiḥa value: {a['fatiha_value']:.6f}" if isinstance(a['fatiha_value'], float)
          else f"  Fātiḥa value: {a['fatiha_value']}")
    s = a['null_summary']
    print(f"  Null n={s['n']}  median={s['median']:.4f}  q99={s['q99']:.4f}  max={s['max']:.4f}")
    print(f"  Percentile (lower tail): {a['percentile_lower_tail']:.5f}")
    print(f"  p-value (one-sided): {a['p_value_one_sided']:.5f}{star}")
    print()
print(f"MW-5 controls:")
print(f"  Q 59:22 window axis-1 (lexical mean log-freq): {mw5_5922_axis1}")
print(f"  Q 59:22 window axis-2 (theme coverage): {mw5_5922_axis2}")
print(f"  Q 26:1 window axis-4 (KS): {mw5_26_axis4}")
print()
print(f"Axes Bonferroni-significant: {n_pass} / 6")
print(f"OVERALL VERDICT: {results['overall_verdict']}")
print()
print(f"Wrote {out_json}")
