#!/usr/bin/env python3
"""H-NEW-38 — Directed verse-to-verse pointwise predictability asymmetry.

Pre-reg: findings/phase-b-hypotheses/h-new-38-prereg.md (LOCKED 2026-04-13).

Test: G(v_i → v_{i+1}) = H(v_{i+1}) − H(v_{i+1} | v_i) where H is character-
level cross-entropy under a 5-gram add-one Laplace model with per-verse LOO.

Aggregate: f₊ = |{i : G_i > 0}| / 6122 verse-adjacent pairs (114 surah-
boundary gaps EXCLUDED). One-sided exact binomial vs H₀=0.5, α_bon=0.005.

Secondary: vs Bukhari/Jāḥiẓ/Mutanabbī line-adjacency f₊, two-prop z-test,
worst-baseline gap wins. Bonferroni k=2.

Shuffle null gate: 10k random re-pairings of v_{i+1} relative to v_i;
observed f₊ must exceed 99th percentile.

Seed 20260414. Compute < 5 min total.
"""
import json, math, random, re, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260414
random.seed(SEED)

NGRAM_N = 5
ALPHA_BON = 0.005
BONFERRONI_K = 2

# ---- Normalization (identical to H-NEW-25) ----
AR_LETTER = re.compile(r'[\u0621-\u064A]')
NORMALIZE = {
    'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا',
    'ء': 'ا',
    'ؤ': 'و', 'ئ': 'ي',
    'ى': 'ي', 'ة': 'ه',
}

def clean_consonants(text):
    out = []
    for ch in text:
        if AR_LETTER.match(ch):
            out.append(NORMALIZE.get(ch, ch))
    return ''.join(out)

# Sentinel for begin-of-verse padding (4 chars per pre-reg)
SENTINEL = '#'  # not in Arabic alphabet, safe
PAD = SENTINEL * (NGRAM_N - 1)

# ---- Load Quran ----
print("[H-NEW-38] Loading Quran...", file=sys.stderr)
Q = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text())

quran_verses = []  # list of normalized verse strings, in mushaf order
verse_surah = []   # parallel list of surah ids
for s in sorted(Q, key=lambda x: x['id']):
    sid = s['id']
    for v in s['verses']:
        text = clean_consonants(v['text'])
        if text:  # skip empty verses (none expected)
            quran_verses.append(text)
            verse_surah.append(sid)

print(f"  total Quran verses: {len(quran_verses)}", file=sys.stderr)
print(f"  surahs: {len(set(verse_surah))}", file=sys.stderr)

# ---- Verse-adjacent pairs (excluding surah-initial gaps) ----
# Pair (i, i+1) is included iff verse_surah[i] == verse_surah[i+1]
adjacent_pairs = []
for i in range(len(quran_verses) - 1):
    if verse_surah[i] == verse_surah[i + 1]:
        adjacent_pairs.append((i, i + 1))
print(f"  adjacent within-surah pairs: {len(adjacent_pairs)}", file=sys.stderr)
assert len(adjacent_pairs) == 6236 - 114, \
    f"expected 6122 pairs, got {len(adjacent_pairs)}"

# ---- Build global n-gram model with add-one Laplace ----
# Counts: dict mapping (n-1)-character context → Counter of next-char counts.
# Vocab includes the sentinel.

print(f"[H-NEW-38] Building global {NGRAM_N}-gram model...", file=sys.stderr)

def text_to_ngrams(text, n):
    """Yield (context, next_char) pairs from PAD+text. PAD is (n-1) sentinels."""
    padded = PAD + text
    for i in range(n - 1, len(padded)):
        ctx = padded[i - (n - 1):i]
        nxt = padded[i]
        yield ctx, nxt

def build_global_counts(verses, n):
    counts = defaultdict(Counter)
    vocab = set()
    for v in verses:
        vocab.update(v)
        for ctx, nxt in text_to_ngrams(v, n):
            counts[ctx][nxt] += 1
    vocab.add(SENTINEL)  # sentinel always in vocab via padding
    return counts, vocab

global_counts, vocab = build_global_counts(quran_verses, NGRAM_N)
V = len(vocab)
print(f"  vocab size (incl sentinel): {V}", file=sys.stderr)
print(f"  contexts: {len(global_counts)}", file=sys.stderr)

# ---- Cross-entropy of a verse under given counts ----
def verse_cross_entropy(text, counts, V, prefix_context=None):
    """Per-character cross-entropy of text under the n-gram model.

    prefix_context: an (n-1)-character string to use as initial context.
    If None, use PAD (begin-of-verse sentinels).
    """
    if not text:
        return 0.0
    if prefix_context is None:
        prefix = PAD
    else:
        prefix = prefix_context
    # Combined sequence for context lookup: prefix + text
    full = prefix + text
    total_logp = 0.0
    n = NGRAM_N
    for i in range(n - 1, len(full)):
        ctx = full[i - (n - 1):i]
        nxt = full[i]
        ctx_counter = counts.get(ctx, None)
        if ctx_counter is None:
            ctx_total = 0
        else:
            ctx_total = sum(ctx_counter.values())
        # Laplace add-one: P(nxt|ctx) = (count + 1) / (ctx_total + V)
        count_nxt = (ctx_counter.get(nxt, 0) if ctx_counter else 0)
        p = (count_nxt + 1) / (ctx_total + V)
        total_logp += math.log2(p)
    # Per-character entropy: only count characters of `text`, not the prefix
    text_chars = len(full) - (n - 1)  # = len(text)
    return -total_logp / text_chars

# ---- LOO subtraction helpers ----
def subtract_verse(counts, text):
    """Remove text's n-gram contributions from counts in place."""
    for ctx, nxt in text_to_ngrams(text, NGRAM_N):
        counts[ctx][nxt] -= 1
        if counts[ctx][nxt] == 0:
            del counts[ctx][nxt]
        if not counts[ctx]:
            del counts[ctx]

def add_verse(counts, text):
    """Re-add text's n-gram contributions to counts in place."""
    for ctx, nxt in text_to_ngrams(text, NGRAM_N):
        counts[ctx][nxt] += 1

# ---- Compute G for each adjacent pair ----
# G_i = H(v_{i+1}) - H(v_{i+1} | v_i)
# H(v_{i+1}) uses LOO model (v_{i+1} subtracted) with PAD prefix
# H(v_{i+1} | v_i) uses LOO model (v_{i+1} subtracted) with v_i's last 4 chars as prefix

def last_n_chars(text, n):
    """Return last n chars of text, padded with sentinel on the LEFT if shorter."""
    if len(text) >= n:
        return text[-n:]
    return PAD[:n - len(text)] + text

print("[H-NEW-38] Computing G for all 6122 adjacent pairs...", file=sys.stderr)

G_values = []  # parallel to adjacent_pairs
H_uncond_values = []
H_cond_values = []

for pair_idx, (i, j) in enumerate(adjacent_pairs):
    v_i = quran_verses[i]
    v_j = quran_verses[j]
    # LOO: remove v_j from counts (we are evaluating v_j)
    subtract_verse(global_counts, v_j)
    # H(v_j) — unconditional, PAD prefix
    h_uncond = verse_cross_entropy(v_j, global_counts, V, prefix_context=None)
    # H(v_j | v_i) — conditional, use last 4 chars of v_i as prefix
    prefix_ctx = last_n_chars(v_i, NGRAM_N - 1)
    h_cond = verse_cross_entropy(v_j, global_counts, V, prefix_context=prefix_ctx)
    # Restore
    add_verse(global_counts, v_j)
    G = h_uncond - h_cond
    G_values.append(G)
    H_uncond_values.append(h_uncond)
    H_cond_values.append(h_cond)
    if (pair_idx + 1) % 1000 == 0:
        print(f"  processed {pair_idx + 1}/{len(adjacent_pairs)}", file=sys.stderr)

print(f"  done. G stats: mean={sum(G_values)/len(G_values):+.5f}, "
      f"min={min(G_values):+.4f}, max={max(G_values):+.4f}", file=sys.stderr)

# ---- f₊ and exact binomial p ----
n_pos = sum(1 for g in G_values if g > 0)
n_total = len(G_values)
n_zero = sum(1 for g in G_values if g == 0)
f_plus = n_pos / n_total
print(f"\n[H-NEW-38] PRIMARY: f₊ = {n_pos}/{n_total} = {f_plus:.4f}", file=sys.stderr)
print(f"  n_zero (G=0 ties): {n_zero}", file=sys.stderr)

# Exact one-sided binomial: P(X >= n_pos | n=n_total, p=0.5)
# Use scipy for accuracy
try:
    from scipy.stats import binomtest
    bt = binomtest(n_pos, n_total, 0.5, alternative='greater')
    p_binom = bt.pvalue
except ImportError:
    # Manual: sum of binomial PMF from n_pos to n_total
    def log_choose(n, k):
        return math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1)
    log_p = math.log(0.5)
    log_q = math.log(0.5)
    log_terms = [log_choose(n_total, k) + k * log_p + (n_total - k) * log_q
                 for k in range(n_pos, n_total + 1)]
    max_lt = max(log_terms)
    p_binom = math.exp(max_lt) * sum(math.exp(lt - max_lt) for lt in log_terms)

print(f"  exact one-sided binomial p = {p_binom:.4e}", file=sys.stderr)
print(f"  α_bon = {ALPHA_BON}", file=sys.stderr)
primary_pass = p_binom < ALPHA_BON
print(f"  PRIMARY {'PASS' if primary_pass else 'FAIL'}", file=sys.stderr)

# ---- Shuffle null gate ----
print("\n[H-NEW-38] Shuffle null (10,000 random re-pairings)...", file=sys.stderr)
N_SHUFFLES = 10000

# We need to recompute G under random adjacencies. Strategy: randomly permute
# the j indices among themselves, keeping the i indices fixed. This produces
# a random adjacency assignment. Recompute G_shuffled for each pair under the
# new adjacency. f_plus_shuffled = fraction with G > 0.
#
# Optimization: H_uncond_values do NOT change under shuffling (H(v_j) depends
# only on v_j). H_cond_values DO change (depends on v_i). We need to recompute
# H(v_j | v_i_shuffled). Per-shuffle: 6122 verse re-evaluations × ~30 char
# evals = ~180k ops × 10k shuffles = 1.8B ops. Too slow.
#
# Better: precompute for EACH (i, j) pair across all i ∈ Quran_verses, the
# H(v_j | v_i) value. That's 6236 × 6236 = 39M entries × ~30 ops = 1.2B ops.
# Still too much.
#
# Cleanest: precompute H(v_j) for each verse v_j ∈ adjacent's right side
# (call this 6122 values, already in H_uncond_values). For each shuffle,
# recompute H(v_j | v_i_shuffled) for each pair. The inner loop is
# verse_cross_entropy with the LOO-adjusted model (v_j removed). For each
# shuffle, that's 6122 × ~30 char evals × n-gram lookup = ~180k cheap ops.
# 10k shuffles × 180k = 1.8B ops. At 3 ns/op, ~5 sec? Let's see.
#
# Most expensive: verse_cross_entropy per call. For ~30 chars, ~30 dict
# lookups. Python dict lookup is ~50 ns. So ~1.5 μs per verse_cross_entropy
# call. 6122 × 10k = 61M calls. 61M × 1.5 μs = 92 sec. OK, feasible.
# But subtract_verse + add_verse for each pair is also expensive. Let's
# precompute a CACHE: for each j ∈ {right-side verses}, with v_j subtracted
# from counts, store the model state. Actually, that's not easy.
#
# Simplest fix: precompute for each (i, j) where j is one of the 6122
# right-side verses and i is ANY verse (6236), H(v_j | v_i). That's
# 6122 × 6236 ≈ 38M entries. Storage: 38M floats × 8 bytes = 305 MB. Tight.
# Compute: 38M verse_cross_entropy calls × 1.5 μs = 57 seconds. OK.
# Then each shuffle is just a lookup × 6122 + a sum + a comparison. Fast.

# Even simpler: we only need H(v_j | v_i) for j ∈ {right-side verses},
# but the LOO subtracts v_j. The cache key is (i_idx, j_idx). Pre-compute
# this matrix once.

# To save memory and time, here's the optimization that makes it tractable:
# For each j ∈ right-side, fix the LOO state (subtract v_j) ONCE, then
# compute H(v_j | v_i) for all i ∈ {0..6235} (6236 calls), then restore v_j.
# That's 6122 × 6236 = 38M cross-entropy evaluations. Acceptable.

# Build set of right-side j indices (these are the indices into quran_verses)
right_side_j_set = set(j for _, j in adjacent_pairs)
right_side_j_list = sorted(right_side_j_set)
j_to_idx = {j: k for k, j in enumerate(right_side_j_list)}
M_RIGHT = len(right_side_j_list)
print(f"  unique right-side j: {M_RIGHT}", file=sys.stderr)

# For each j, compute H(v_j | v_i) for ALL i. This gives a 6236 x M_RIGHT matrix.
# But the H_uncond is already computed; we just need the conditional matrix.

import time
t0 = time.time()
print(f"  pre-computing 6236 × {M_RIGHT} conditional-H matrix...", file=sys.stderr)

# Cache: H_cond_matrix[j_idx][i] = H(v_j | v_i) under LOO(v_j)
# For memory: use a flat list of arrays. Each row is M_RIGHT floats.
# Total: 6236 × 6122 × 8 bytes ≈ 305 MB. Manageable but heavy.
# Alternative: compute on-the-fly in shuffle loop. Slower per shuffle but
# no upfront cost. Let's profile and decide.

# Actually, there's a much smarter approach. The shuffle null only NEEDS:
# for each shuffle, compute the SIGN of (H_uncond[k] - H_cond_shuffled[k])
# for each k ∈ 0..6121. The H_uncond values are FIXED. So we need
# H_cond_shuffled[k] = H(v_j_k | v_i_shuffled[k]) where v_j_k is the
# k-th right-side verse and v_i_shuffled[k] is some random Quran verse.
#
# Key insight: for each j (right-side verse), we need H(v_j | v_i) for the
# v_i that gets shuffled to it. Across 10k shuffles, each j gets 10k
# different v_i's. If we precompute H(v_j | v_i) for ALL (j, i), we have
# everything we need with O(1) lookup per shuffle iteration.
#
# Cost: 6122 × 6236 = 38M conditional cross-entropy evals.
# Each eval: ~30 char × dict lookup ≈ 50-100 μs (Python overhead).
# 38M × 80 μs = 3,000 sec = 50 min. TOO SLOW.
#
# Better idea: subset the i's. Each shuffle only uses 6122 of the 6236
# possible i's (a permutation). Across 10k shuffles, the total number of
# (j, i) pairs sampled is 6122 × 10k = 61M, but with HIGH redundancy
# (each j sees ~10k random i's). Caching is exactly what we want.
#
# Memoization with full pre-compute: 38M evals at ~10 μs each (optimized
# inner loop) = 380 sec ≈ 6.3 min. Tight but feasible.
#
# Let me try a faster path: rather than precomputing the FULL matrix,
# do online caching. Each shuffle picks 6122 random i's per j; over 10k
# shuffles each j sees ~10k i's. With 6122 unique j's and 6236 unique i's,
# nearly the entire matrix gets queried. So we might as well precompute.
#
# OPTIMIZATION: rewrite verse_cross_entropy in a tighter form.

# Tighter inner loop: precompute the "successor distribution" for each
# context. For each context ctx in counts, we have ctx_total and a Counter.
# We can pre-compute log_p_table[ctx][nxt] = log2((count + 1) / (ctx_total + V))
# for all (ctx, nxt) pairs that appear in the global counts. For pairs not
# in the table, p = 1 / (ctx_total + V) where ctx_total = 0 → p = 1/V.
# But under LOO subtraction, ctx_total changes. So this caching only works
# for the GLOBAL model, not LOO. The shuffle null does NOT need LOO at all
# — only the OBSERVED computation needs LOO. The shuffle null is comparing
# observed sign-fraction against random-adjacency sign-fractions, both
# under the SAME model. So the shuffle null can use the FULL global model
# without LOO, since the bias affects observed and shuffled equally.
#
# Wait — that's a subtle but critical point. The pre-reg says LOO for the
# primary observation. For the shuffle null, both observed and shuffled
# need to use the SAME model so that the comparison is fair. Two options:
#
# (a) LOO for both (observed and shuffled). Mathematically cleanest, but
#     requires the LOO matrix computation.
# (b) Non-LOO for both (observed and shuffled). The shuffle null becomes
#     non-LOO. The observed primary stays LOO. The two are then on
#     different scales but the shuffle null still answers "is the
#     observed sign fraction extreme under random adjacency?" question.
#
# The cleanest mathematical interpretation: use the SAME model state for
# observed and shuffled. So either do LOO for both (expensive) or non-LOO
# for both (cheap). Let me go with non-LOO for the shuffle null and LOO
# for the observed primary, and disclose this in the JSON output. This
# is defensible because the shuffle null is a TWO-DISTRIBUTION comparison,
# not an absolute claim.

print(f"  computing non-LOO H(v_j) and H(v_j|v_i) for shuffle null cache...", file=sys.stderr)

# Precompute non-LOO H_uncond for each right-side j
H_uncond_global = {}
for j in right_side_j_list:
    H_uncond_global[j] = verse_cross_entropy(quran_verses[j], global_counts, V, prefix_context=None)

# For shuffle null cache, we need H(v_j | v_i) for each (j ∈ right_side, i ∈ all).
# Compute as a flat list of 6236 entries per j.
# Memory: 6122 × 6236 × 4 bytes (float32) ≈ 153 MB. Use array.
import array

print(f"  building H_cond cache 6236 × {M_RIGHT} (non-LOO)...", file=sys.stderr)
H_cond_cache = {}  # j_idx -> array of 6236 floats (one per i)
total_evals = 0
t1 = time.time()
for k, j in enumerate(right_side_j_list):
    v_j = quran_verses[j]
    row = array.array('f', [0.0] * len(quran_verses))
    for i in range(len(quran_verses)):
        prefix_ctx = last_n_chars(quran_verses[i], NGRAM_N - 1)
        row[i] = verse_cross_entropy(v_j, global_counts, V, prefix_context=prefix_ctx)
        total_evals += 1
    H_cond_cache[j] = row
    if (k + 1) % 200 == 0:
        elapsed = time.time() - t1
        rate = (k + 1) / elapsed
        eta = (M_RIGHT - k - 1) / rate
        print(f"    j {k+1}/{M_RIGHT} ({rate:.1f} verses/s, ETA {eta:.0f}s)", file=sys.stderr)

t_cache = time.time() - t1
print(f"  cache built in {t_cache:.1f}s, total evals = {total_evals}", file=sys.stderr)

# ---- Run 10k shuffles using cache ----
print(f"\n[H-NEW-38] Running {N_SHUFFLES} shuffles...", file=sys.stderr)
shuffle_f_plus = []
all_i_indices = list(range(len(quran_verses)))
right_j_in_pair_order = [j for _, j in adjacent_pairs]  # length 6122

t2 = time.time()
for s in range(N_SHUFFLES):
    # Random permutation of i indices, sample 6122 without replacement
    # Pair the k-th adjacent pair's j with a random i
    sampled_i = random.sample(all_i_indices, len(adjacent_pairs))
    n_pos_s = 0
    for k, j in enumerate(right_j_in_pair_order):
        i_shuffled = sampled_i[k]
        h_cond = H_cond_cache[j][i_shuffled]
        h_uncond = H_uncond_global[j]
        if h_uncond - h_cond > 0:
            n_pos_s += 1
    shuffle_f_plus.append(n_pos_s / len(adjacent_pairs))
    if (s + 1) % 1000 == 0:
        elapsed = time.time() - t2
        rate = (s + 1) / elapsed
        eta = (N_SHUFFLES - s - 1) / rate
        print(f"  shuffle {s+1}/{N_SHUFFLES} ({rate:.0f}/s, ETA {eta:.0f}s)", file=sys.stderr)

shuffle_f_plus.sort()
shuffle_99 = shuffle_f_plus[int(0.99 * N_SHUFFLES)]
shuffle_mean = sum(shuffle_f_plus) / N_SHUFFLES
shuffle_min = shuffle_f_plus[0]
shuffle_max = shuffle_f_plus[-1]

# Also compute the OBSERVED f₊ under the same NON-LOO model for fair comparison
# with the shuffle null. (The LOO version is the primary; this is for the gate.)
print(f"\n[H-NEW-38] Computing OBSERVED f₊ under same non-LOO model for shuffle gate...", file=sys.stderr)
n_pos_nonloo = 0
for k, (i, j) in enumerate(adjacent_pairs):
    h_cond_nonloo = H_cond_cache[j][i]
    h_uncond_nonloo = H_uncond_global[j]
    if h_uncond_nonloo - h_cond_nonloo > 0:
        n_pos_nonloo += 1
f_plus_nonloo = n_pos_nonloo / len(adjacent_pairs)
print(f"  observed f₊ (non-LOO model): {f_plus_nonloo:.4f}", file=sys.stderr)
print(f"  shuffle null distribution: mean={shuffle_mean:.4f}, "
      f"99th pctile={shuffle_99:.4f}, min={shuffle_min:.4f}, max={shuffle_max:.4f}",
      file=sys.stderr)

shuffle_gate_pass = f_plus_nonloo > shuffle_99
print(f"  shuffle gate {'PASS' if shuffle_gate_pass else 'FAIL'}", file=sys.stderr)

# ---- Secondary: baselines ----
print("\n[H-NEW-38] Secondary: baseline corpora...", file=sys.stderr)
BASELINE_FILES = {
    'bukhari': 'bukhari-noquran.txt',
    'jahiz': 'jahiz-hayawan.txt',
    'mutanabbi': 'mutanabbi-diwan.txt',
}

baseline_results = {}
for name, fn in BASELINE_FILES.items():
    p = ROOT / 'data/baseline-corpora/raw' / fn
    if not p.exists():
        print(f"  [warn] missing: {fn} — marking baseline DEGENERATE", file=sys.stderr)
        baseline_results[name] = {'status': 'DEGENERATE', 'reason': 'file missing'}
        continue
    txt = p.read_text(encoding='utf-8', errors='replace')
    txt = re.sub(r'[\u064B-\u065F\u0670]', '', txt)
    # Split into "verses" by newline; strip empty
    raw_lines = [line.strip() for line in txt.split('\n') if line.strip()]
    lines = [clean_consonants(line) for line in raw_lines]
    lines = [l for l in lines if l]  # drop ones that became empty
    print(f"  {name}: {len(lines)} non-empty lines", file=sys.stderr)
    if len(lines) < 100:
        baseline_results[name] = {'status': 'DEGENERATE', 'reason': 'too few lines', 'n_lines': len(lines)}
        continue

    # Adjacent pairs (no surah-grouping; treat all consecutive lines as adjacent)
    base_pairs = [(i, i + 1) for i in range(len(lines) - 1)]

    # Build baseline-specific n-gram model
    base_counts, base_vocab = build_global_counts(lines, NGRAM_N)
    base_V = len(base_vocab)

    # Compute G_i for each pair (LOO)
    n_pos_b = 0
    n_zero_b = 0
    n_total_b = 0
    g_vals_b = []
    for i, j in base_pairs:
        v_j = lines[j]
        if not v_j:
            continue
        subtract_verse(base_counts, v_j)
        h_uncond_b = verse_cross_entropy(v_j, base_counts, base_V, prefix_context=None)
        prefix_ctx = last_n_chars(lines[i], NGRAM_N - 1)
        h_cond_b = verse_cross_entropy(v_j, base_counts, base_V, prefix_context=prefix_ctx)
        add_verse(base_counts, v_j)
        g = h_uncond_b - h_cond_b
        g_vals_b.append(g)
        n_total_b += 1
        if g > 0:
            n_pos_b += 1
        elif g == 0:
            n_zero_b += 1

    if n_total_b == 0:
        baseline_results[name] = {'status': 'DEGENERATE', 'reason': 'no valid pairs'}
        continue

    f_plus_b = n_pos_b / n_total_b

    # Two-proportion z-test: Quran f₊ (LOO) vs baseline f₊ (LOO)
    p1 = f_plus  # Quran (LOO)
    n1 = n_total
    p2 = f_plus_b
    n2 = n_total_b
    p_pool = (n_pos + n_pos_b) / (n1 + n2)
    se = math.sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))
    z_diff = (p1 - p2) / se if se > 0 else 0
    # One-sided right-tail p-value
    from math import erf, sqrt
    p_z = 0.5 * (1 - erf(z_diff / sqrt(2)))

    print(f"    {name}: f₊={f_plus_b:.4f} (n={n_total_b}); "
          f"vs Quran z={z_diff:+.3f}, p={p_z:.4e}", file=sys.stderr)

    baseline_results[name] = {
        'status': 'COMPUTED',
        'n_lines': len(lines),
        'n_pairs': n_total_b,
        'n_pos': n_pos_b,
        'n_zero': n_zero_b,
        'f_plus': f_plus_b,
        'mean_G': sum(g_vals_b) / len(g_vals_b),
        'z_vs_quran': z_diff,
        'p_one_sided': p_z,
        'passes_alpha_bon': p_z < ALPHA_BON,
    }

# Worst-baseline-wins secondary verdict
computed_baselines = [b for b in baseline_results.values() if b.get('status') == 'COMPUTED']
if not computed_baselines:
    secondary_verdict = 'DEGENERATE'
elif all(b['passes_alpha_bon'] for b in computed_baselines):
    secondary_verdict = 'PASS'
else:
    secondary_verdict = 'FAIL'

print(f"\n[H-NEW-38] SECONDARY worst-baseline verdict: {secondary_verdict}", file=sys.stderr)

# ---- Final verdict matrix ----
if primary_pass and secondary_verdict == 'PASS' and shuffle_gate_pass:
    final_verdict = 'PASS — DIRECTED COHESION CONFIRMED'
elif primary_pass and secondary_verdict != 'PASS' and shuffle_gate_pass:
    final_verdict = 'PARTIAL — Quran has internal directed cohesion but not specifically more than baseline'
elif primary_pass and not shuffle_gate_pass:
    final_verdict = 'NULL — observed f₊ within random-adjacency expectation (shuffle gate failed)'
elif not primary_pass and f_plus < 0.5:
    final_verdict = 'REVERSE-CANDIDATE — file h-new-38-reverse if binomial-significant'
else:
    final_verdict = 'NULL — no global directed cohesion'

print(f"\n[H-NEW-38] FINAL VERDICT: {final_verdict}", file=sys.stderr)

# ---- Output JSON ----
out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-new-38.json'
out_path.parent.mkdir(parents=True, exist_ok=True)

output = {
    'finding_id': 'h-new-38',
    'pre_reg': 'findings/phase-b-hypotheses/h-new-38-prereg.md',
    'pre_reg_compliance': 'PRE-REG-STANDARD-04',
    'rules_tuple': '(no-tashkeel, character-level, 28-letter-rasm, hamza→alif normalize, ى→ي, ة→ه, mushaf order, leave-one-out via per-verse subtraction)',
    'seed': SEED,
    'n_gram_order': NGRAM_N,
    'smoothing': 'add-one Laplace',
    'bonferroni_k': BONFERRONI_K,
    'alpha_bon': ALPHA_BON,
    'sided_test': 'one-sided positive (f₊ > 0.5 LOCKED)',
    'primary': {
        'description': 'sign(G_i > 0) fraction across all 6122 within-surah adjacent verse pairs',
        'n_pairs': n_total,
        'n_pos': n_pos,
        'n_zero': n_zero,
        'f_plus': f_plus,
        'p_binomial_one_sided': p_binom,
        'mean_G': sum(G_values) / len(G_values),
        'min_G': min(G_values),
        'max_G': max(G_values),
        'mean_H_uncond': sum(H_uncond_values) / len(H_uncond_values),
        'mean_H_cond': sum(H_cond_values) / len(H_cond_values),
        'pass': primary_pass,
    },
    'shuffle_null_gate': {
        'n_shuffles': N_SHUFFLES,
        'observed_f_plus_nonloo': f_plus_nonloo,
        'shuffle_mean': shuffle_mean,
        'shuffle_99th_pctile': shuffle_99,
        'shuffle_min': shuffle_min,
        'shuffle_max': shuffle_max,
        'pass': shuffle_gate_pass,
        'note': 'Shuffle null uses non-LOO model for both observed and shuffled (so bias is constant across the distribution comparison). Primary uses LOO. Disclosure: observed_f_plus_nonloo and primary f_plus may differ slightly because of LOO vs non-LOO.',
    },
    'secondary': {
        'description': 'Two-proportion z-test: Quran f₊ vs each baseline corpus f₊ (worst-baseline-wins)',
        'baselines': baseline_results,
        'verdict': secondary_verdict,
    },
    'final_verdict': final_verdict,
    'no_fork_protections_honored': [
        'sign locked to f₊ > 0.5 before script run',
        'n-gram order locked to 5',
        'smoothing locked to add-one Laplace',
        'surah-initial gaps excluded (114 gaps, leaving 6122 pairs)',
        'baselines locked to Bukhari-noquran, Jāḥiẓ Ḥayawān, Mutanabbī Dīwān',
        'LOO for primary observation',
        'shuffle null seed 20260414, 10000 shuffles',
    ],
    'data_reuse_disclosed': 'Reuses normalization from H-NEW-25 (clean_consonants), reuses Quran JSON loader. No data shared with H-NEW-20 statistical machinery.',
}

out_path.write_text(json.dumps(output, indent=2, default=str, ensure_ascii=False))
print(f"\n[saved] {out_path}", file=sys.stderr)
