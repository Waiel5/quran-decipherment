#!/usr/bin/env python3
"""H-NEW-24 — Letter-multiset surah-boundary detectability.

Tokenization-free, character-level test. Concatenate the Quran in canonical
mushaf order (letter-only, whitespace stripped), compute
JS(P_left ‖ P_right) divergence at stride s=100 using window w characters,
extract top K=113 local maxima as predicted interior boundaries, measure
detection at tolerance ε.

Sub-tests:
  (a) Above-chance detection vs random K=113 placements (10,000 perms)
  (b) Jonckheere-Terpstra monotonicity across w ∈ {500, 1000, 2000, 5000}
  (c) Shuffle-control: uniform-permute all letters, re-run (a)
  (d) Baseline classical corpus (Bukhari-noquran) with 113 random pseudo-breaks

Bonferroni k=4, per-test α=0.0025. Primary (w=2000, ε=500).

Seed 20260413.
"""
import json, math, random, re, statistics, sys
from collections import Counter
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
random.seed(20260413)

# Alphabet: Arabic consonants + hamza variants + alif/ya forms
# Use rasm-level normalization consistent with project rules-tuple
AR_LETTER = re.compile(r'[\u0621-\u064A]')
NORMALIZE = {
    'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا',
    'ى': 'ي', 'ة': 'ه',
    # hamza variants kept as-is
}

def clean_letters(text):
    out = []
    for ch in text:
        if AR_LETTER.match(ch):
            out.append(NORMALIZE.get(ch, ch))
    return ''.join(out)

# ---- Load Quran, concatenate in mushaf order, record true boundaries ----
Q = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text())

concat = []
true_boundaries = []  # positions in the final concat string where surah k+1 starts
pos = 0
for s in sorted(Q, key=lambda x: x['id']):
    sid = s['id']
    surah_text = ''.join(v['text'] for v in s['verses'])
    letters = clean_letters(surah_text)
    if pos > 0:
        true_boundaries.append(pos)  # this is where this new surah starts
    concat.append(letters)
    pos += len(letters)

quran_str = ''.join(concat)
N = len(quran_str)
print(f"total letter count: {N}", file=sys.stderr)
print(f"interior boundaries: {len(true_boundaries)}", file=sys.stderr)
print(f"first few boundary positions: {true_boundaries[:5]}", file=sys.stderr)

# Alphabet from observed characters
alphabet = sorted(set(quran_str))
ALPHA_IDX = {c: i for i, c in enumerate(alphabet)}
A = len(alphabet)
print(f"alphabet size: {A}", file=sys.stderr)

# ---- JS divergence helper ----
def js_divergence(p_counts, q_counts):
    """Jensen-Shannon divergence between two count distributions."""
    tp = sum(p_counts)
    tq = sum(q_counts)
    if tp == 0 or tq == 0:
        return 0.0
    js = 0.0
    # Assume A-length lists
    for i in range(A):
        p = p_counts[i] / tp
        q = q_counts[i] / tq
        m = 0.5 * (p + q)
        if m > 0:
            if p > 0:
                js += 0.5 * p * math.log2(p / m)
            if q > 0:
                js += 0.5 * q * math.log2(q / m)
    return js

def counts_of(s):
    c = [0] * A
    for ch in s:
        idx = ALPHA_IDX.get(ch)
        if idx is not None:
            c[idx] += 1
    return c

# ---- Boundary scanner ----
def scan_boundaries(text, w, stride=100):
    """Return (positions, js_scores) for every stride-step position with left+right window."""
    positions = []
    scores = []
    nt = len(text)
    for i in range(w, nt - w, stride):
        left_counts = counts_of(text[i-w:i])
        right_counts = counts_of(text[i:i+w])
        s = js_divergence(left_counts, right_counts)
        positions.append(i)
        scores.append(s)
    return positions, scores

def top_k_local_maxima(positions, scores, k, min_separation):
    """Greedy selection of k largest scores with min-separation constraint."""
    indexed = list(enumerate(scores))
    indexed.sort(key=lambda x: -x[1])
    chosen = []
    chosen_positions = set()
    for idx, _ in indexed:
        p = positions[idx]
        too_close = False
        for cp in chosen_positions:
            if abs(p - cp) < min_separation:
                too_close = True
                break
        if not too_close:
            chosen.append(p)
            chosen_positions.add(p)
            if len(chosen) >= k:
                break
    return sorted(chosen)

# ---- Detection against true boundaries ----
def detect(predictions, truths, epsilon):
    """Count how many truths have at least one prediction within epsilon chars."""
    # Use a greedy one-to-one matching (each prediction matches at most one truth)
    hits = 0
    used = set()
    for t in truths:
        for pi, p in enumerate(predictions):
            if pi in used:
                continue
            if abs(p - t) <= epsilon:
                hits += 1
                used.add(pi)
                break
    return hits

# ---- Run at multiple window sizes ----
K = 113
MIN_SEP = 500  # must be less than smallest expected surah length; Quran has some very short surahs
WINDOWS = [500, 1000, 2000, 5000]
EPSILONS = [200, 500, 1000]
PRIMARY_W = 2000
PRIMARY_EPS = 500

results_by_w = {}
print("\n=== Sub-test (a)/(b): JS-scan on real Quran ===", file=sys.stderr)
for w in WINDOWS:
    positions, scores = scan_boundaries(quran_str, w)
    preds = top_k_local_maxima(positions, scores, K, MIN_SEP)
    row = {}
    for eps in EPSILONS:
        hits = detect(preds, true_boundaries, eps)
        row[f'hits_eps{eps}'] = hits
    row['n_preds'] = len(preds)
    row['mean_score'] = statistics.mean(scores) if scores else 0
    row['max_score'] = max(scores) if scores else 0
    results_by_w[w] = row
    print(f"w={w}: preds={len(preds)}, hits@ε=200 {row['hits_eps200']}, "
          f"hits@ε=500 {row['hits_eps500']}, hits@ε=1000 {row['hits_eps1000']}", file=sys.stderr)

obs_primary_hits = results_by_w[PRIMARY_W][f'hits_eps{PRIMARY_EPS}']
print(f"\nPrimary (w={PRIMARY_W}, ε={PRIMARY_EPS}): observed hits = {obs_primary_hits}", file=sys.stderr)

# ---- Sub-test (a): random-placement null ----
def random_placement_null(n_perm=10000):
    """Sample K random positions within valid range, count hits at eps=PRIMARY_EPS."""
    hits_null = []
    valid_range = N - 2 * PRIMARY_W  # positions where scan could place a prediction
    for _ in range(n_perm):
        preds = sorted(random.sample(range(PRIMARY_W, N - PRIMARY_W), K))
        hits = detect(preds, true_boundaries, PRIMARY_EPS)
        hits_null.append(hits)
    return hits_null

print("\n=== Sub-test (a) null: 10,000 random K=113 placements ===", file=sys.stderr)
null_a = random_placement_null(10000)
null_mean = statistics.mean(null_a)
null_sd = statistics.stdev(null_a)
p999_a = sorted(null_a)[int(0.9975 * len(null_a))]
z_a = (obs_primary_hits - null_mean) / null_sd if null_sd > 0 else 0
p_a = sum(1 for x in null_a if x >= obs_primary_hits) / len(null_a)
print(f"null mean {null_mean:.2f} ± {null_sd:.2f}; 99.75 pct = {p999_a}", file=sys.stderr)
print(f"observed {obs_primary_hits} → z = {z_a:.3f}, p = {p_a:.5f}", file=sys.stderr)

# ---- Sub-test (b): Jonckheere-Terpstra monotonicity ----
def jonckheere_terpstra_one_sided(groups):
    """One-sided Jonckheere-Terpstra test for ordered alternative: group1 < group2 < ... < groupG.
    Returns (J, z, p). With only 1 obs per group (point estimates), we need a
    permutation null. Since we have 4 scalar observations, use a rank-sum approach.
    """
    # With one value per "group", Jonckheere-Terpstra reduces to testing whether
    # the sequence is monotonically ordered. Use Spearman vs identity.
    vals = [g for g in groups]
    n = len(vals)
    # Spearman rho
    ranks = sorted(range(n), key=lambda i: vals[i])
    rank_of = [0] * n
    for r, i in enumerate(ranks):
        rank_of[i] = r + 1
    # Spearman between ranks and natural order (1..n)
    d2 = sum((rank_of[i] - (i + 1)) ** 2 for i in range(n))
    rho = 1 - 6 * d2 / (n * (n * n - 1))
    # Approximate z
    z = rho * math.sqrt(n - 1)
    # One-sided p (positive direction)
    from math import erf, sqrt
    p = 0.5 * (1 - erf(z / sqrt(2)))
    return rho, z, p

hit_sequence = [results_by_w[w][f'hits_eps{PRIMARY_EPS}'] for w in WINDOWS]
rho_b, z_b, p_b = jonckheere_terpstra_one_sided(hit_sequence)
print(f"\n=== Sub-test (b): monotonicity ===", file=sys.stderr)
print(f"hits@ε={PRIMARY_EPS}: {hit_sequence}", file=sys.stderr)
print(f"Spearman ρ={rho_b:.3f}, z={z_b:.3f}, one-sided p={p_b:.5f}", file=sys.stderr)

# ---- Sub-test (c): uniform-shuffle control ----
print("\n=== Sub-test (c): shuffle-control ===", file=sys.stderr)
shuffled = list(quran_str)
random.shuffle(shuffled)
shuffled_str = ''.join(shuffled)
# Re-run at primary w
positions_sh, scores_sh = scan_boundaries(shuffled_str, PRIMARY_W)
preds_sh = top_k_local_maxima(positions_sh, scores_sh, K, MIN_SEP)
hits_sh = detect(preds_sh, true_boundaries, PRIMARY_EPS)
print(f"shuffled Quran hits@(w=2000, ε=500): {hits_sh}", file=sys.stderr)
# p_value under random-placement null
p_c = sum(1 for x in null_a if x >= hits_sh) / len(null_a)
z_c = (hits_sh - null_mean) / null_sd if null_sd > 0 else 0
within_95 = sorted(null_a)[int(0.025 * len(null_a))] <= hits_sh <= sorted(null_a)[int(0.975 * len(null_a))]
print(f"shuffled z={z_c:.3f}, p={p_c:.5f}, within 95% band: {within_95}", file=sys.stderr)

# ---- Sub-test (d): Bukhari baseline ----
print("\n=== Sub-test (d): Bukhari baseline ===", file=sys.stderr)
bukhari_raw = (ROOT / 'data/baseline-corpora/raw/bukhari-noquran.txt').read_text(
    encoding='utf-8', errors='replace')
bukhari_str = clean_letters(bukhari_raw)
# Trim to match Quran length
bukhari_str = bukhari_str[:N]
nb = len(bukhari_str)
print(f"Bukhari letter count: {nb}", file=sys.stderr)

# 113 random pseudo-boundaries
bukhari_truths = sorted(random.sample(range(PRIMARY_W, nb - PRIMARY_W), K))
positions_b, scores_b = scan_boundaries(bukhari_str, PRIMARY_W)
preds_b = top_k_local_maxima(positions_b, scores_b, K, MIN_SEP)
# Measure detection of the random pseudo-boundaries
hits_d = detect(preds_b, bukhari_truths, PRIMARY_EPS)
# Also compute random placement null for Bukhari
def random_placement_null_bukhari(truths, total_len, n_perm=2000):
    hits_null = []
    for _ in range(n_perm):
        preds = sorted(random.sample(range(PRIMARY_W, total_len - PRIMARY_W), K))
        hits = detect(preds, truths, PRIMARY_EPS)
        hits_null.append(hits)
    return hits_null

null_d = random_placement_null_bukhari(bukhari_truths, nb, 2000)
null_d_mean = statistics.mean(null_d)
null_d_sd = statistics.stdev(null_d)
z_d = (hits_d - null_d_mean) / null_d_sd if null_d_sd > 0 else 0
p_d = sum(1 for x in null_d if x >= hits_d) / len(null_d)
print(f"Bukhari JS-scan hits={hits_d}, null mean={null_d_mean:.2f}±{null_d_sd:.2f}, z={z_d:.3f}, p={p_d:.5f}", file=sys.stderr)

# ---- Position-stratified descriptive (AMEND-15 Addition 1) ----
def stratify_by_tercile(positions, truths, epsilon):
    third = N // 3
    bands = [(0, third), (third, 2*third), (2*third, N)]
    hits_per_band = [0] * 3
    total_per_band = [0] * 3
    for t in truths:
        for bi, (lo, hi) in enumerate(bands):
            if lo <= t < hi:
                total_per_band[bi] += 1
                for p in positions:
                    if abs(p - t) <= epsilon:
                        hits_per_band[bi] += 1
                        break
                break
    return hits_per_band, total_per_band

# Use primary w=2000 predictions
positions_2000, scores_2000 = scan_boundaries(quran_str, PRIMARY_W)
preds_2000 = top_k_local_maxima(positions_2000, scores_2000, K, MIN_SEP)
tercile_hits, tercile_totals = stratify_by_tercile(preds_2000, true_boundaries, PRIMARY_EPS)
print(f"\nTercile hits @ ε=500 (early/mid/late): {tercile_hits} / {tercile_totals}", file=sys.stderr)

# ---- Joint verdict ----
print("\n=== Joint verdict ===", file=sys.stderr)
a_pass = p_a < 0.0025 and obs_primary_hits > p999_a
b_pass = p_b < 0.0025
c_pass = within_95
d_pass = hits_d <= p_d  # Bukhari should fail: we expect NOT significant
d_fails_as_required = p_d > 0.05  # Bukhari should not exceed chance
print(f"(a) above-chance on Quran: {'PASS' if a_pass else 'FAIL'} (p={p_a:.5f}, obs={obs_primary_hits} vs 99.75 pct={p999_a})", file=sys.stderr)
print(f"(b) monotonic with w: {'PASS' if b_pass else 'FAIL'} (p={p_b:.5f})", file=sys.stderr)
print(f"(c) shuffle-control within 95% band: {'PASS' if c_pass else 'FAIL'} (shuffled hits={hits_sh})", file=sys.stderr)
print(f"(d) Bukhari fails to detect random pseudo-boundaries: {'PASS' if d_fails_as_required else 'FAIL'} (Bukhari p={p_d:.5f})", file=sys.stderr)
joint = a_pass and b_pass and c_pass and d_fails_as_required
print(f"Joint claim (a ∧ b ∧ c ∧ d): {'PASS' if joint else 'FAIL'}", file=sys.stderr)

# ---- Output ----
out = {
    'seed': 20260413,
    'hypothesis': 'H-NEW-24 letter-multiset surah-boundary detectability',
    'rules_tuple': 'rasm no-tashkeel, whitespace-stripped, letter-level',
    'alphabet_size': A,
    'total_letters': N,
    'true_boundaries_count': len(true_boundaries),
    'K': K,
    'min_separation': MIN_SEP,
    'windows': WINDOWS,
    'epsilons': EPSILONS,
    'primary_w': PRIMARY_W,
    'primary_epsilon': PRIMARY_EPS,
    'results_by_w': results_by_w,
    'sub_a': {
        'observed_hits': obs_primary_hits,
        'null_mean': null_mean,
        'null_sd': null_sd,
        'null_9975_pct': p999_a,
        'z': z_a,
        'p': p_a,
        'pass': a_pass,
    },
    'sub_b': {
        'hit_sequence': hit_sequence,
        'spearman_rho': rho_b,
        'z': z_b,
        'p_one_sided': p_b,
        'pass': b_pass,
    },
    'sub_c': {
        'shuffled_hits': hits_sh,
        'z': z_c,
        'p': p_c,
        'within_95_band': within_95,
        'pass': c_pass,
    },
    'sub_d': {
        'bukhari_hits': hits_d,
        'bukhari_null_mean': null_d_mean,
        'bukhari_null_sd': null_d_sd,
        'bukhari_z': z_d,
        'bukhari_p': p_d,
        'pass_fails_as_required': d_fails_as_required,
    },
    'tercile_hits': tercile_hits,
    'tercile_totals': tercile_totals,
    'joint_pass': joint,
    'bonferroni_k': 4,
    'alpha_bon': 0.01 / 4,
}

out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-new-24-hit-counts.json'
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, indent=2, default=str))
print(f"\nsaved: {out_path}", file=sys.stderr)
print(json.dumps(out, indent=2, default=str))
