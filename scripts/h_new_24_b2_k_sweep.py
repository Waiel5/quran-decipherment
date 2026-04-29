#!/usr/bin/env python3
"""H-NEW-24-B2 — K-sensitivity sweep for letter-multiset boundary detection.

audit-019 blocker B2 for H-NEW-24. At K=113 under 1-1 matching,
precision = recall = 36% by construction. This test disambiguates:

  - "a few strong peaks" (tight K=30 or K=60 retains signal) vs
  - "diffuse weak signal across many boundaries" (precision degrades as
    K/N_total regardless of K)

For each K in {30, 60, 113, 200, 300}, run the JS-scan top-K matching
against the 113 true boundaries at (w=2000, eps=500, stride=100) on:
  - real Quran
  - uniform-shuffle null (sub-c flavor) — 200 random K-placements
  - chance random-placement null

Report precision, recall, F1 for real vs chance at each K.

Seed 20260413.
"""

import json
import math
import random
import re
import statistics
import sys
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
random.seed(20260413)

AR_LETTER = re.compile(r'[\u0621-\u064A]')
NORMALIZE = {
    'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا',
    'ى': 'ي', 'ة': 'ه',
}


def clean_letters(text):
    out = []
    for ch in text:
        if AR_LETTER.match(ch):
            out.append(NORMALIZE.get(ch, ch))
    return ''.join(out)


Q = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text())

per_surah_letters = []
for s in sorted(Q, key=lambda x: x['id']):
    surah_text = ''.join(v['text'] for v in s['verses'])
    per_surah_letters.append(clean_letters(surah_text))

surah_lengths = [len(s) for s in per_surah_letters]
quran_str = ''.join(per_surah_letters)
N = len(quran_str)

true_boundaries = []
acc = 0
for L in surah_lengths[:-1]:
    acc += L
    true_boundaries.append(acc)

alphabet = sorted(set(quran_str))
ALPHA_IDX = {c: i for i, c in enumerate(alphabet)}
A = len(alphabet)

N_TRUE = len(true_boundaries)
print(f"N letters={N}, alphabet={A}, true boundaries={N_TRUE}", file=sys.stderr)


def js_divergence(p_counts, q_counts):
    tp = sum(p_counts)
    tq = sum(q_counts)
    if tp == 0 or tq == 0:
        return 0.0
    js = 0.0
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


def scan_boundaries(text, w, stride=100):
    positions = []
    scores = []
    nt = len(text)
    for i in range(w, nt - w, stride):
        left_counts = counts_of(text[i - w:i])
        right_counts = counts_of(text[i:i + w])
        positions.append(i)
        scores.append(js_divergence(left_counts, right_counts))
    return positions, scores


def top_k_local_maxima(positions, scores, k, min_separation):
    indexed = sorted(enumerate(scores), key=lambda x: -x[1])
    chosen_positions = []
    for idx, _ in indexed:
        p = positions[idx]
        too_close = any(abs(p - cp) < min_separation for cp in chosen_positions)
        if not too_close:
            chosen_positions.append(p)
            if len(chosen_positions) >= k:
                break
    return sorted(chosen_positions)


def detect(predictions, truths, epsilon):
    """One-to-one matching: each prediction matches at most one truth."""
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


def pr_metrics(hits, k, n_true):
    precision = hits / k if k > 0 else 0
    recall = hits / n_true if n_true > 0 else 0
    f1 = (2 * precision * recall / (precision + recall)) if (precision + recall) > 0 else 0
    return precision, recall, f1


PRIMARY_W = 2000
PRIMARY_EPS = 500
MIN_SEP = 500
STRIDE = 100
K_VALUES = [30, 60, 113, 200, 300]

# ---- Run the one-time real Quran JS scan ----
print("\n=== Scanning real Quran ===", file=sys.stderr)
positions_real, scores_real = scan_boundaries(quran_str, PRIMARY_W, STRIDE)
print(f"real Quran: {len(positions_real)} scan positions", file=sys.stderr)

# ---- Real Quran top-K extractions at each K ----
real_per_k = {}
for K in K_VALUES:
    preds = top_k_local_maxima(positions_real, scores_real, K, MIN_SEP)
    hits = detect(preds, true_boundaries, PRIMARY_EPS)
    p, r, f = pr_metrics(hits, K, N_TRUE)
    real_per_k[K] = {'hits': hits, 'precision': p, 'recall': r, 'f1': f, 'n_preds': len(preds)}
    print(f"real K={K}: hits={hits}, P={p:.3f}, R={r:.3f}, F1={f:.3f}, n_preds={len(preds)}",
          file=sys.stderr)

# ---- Chance-null: random K-placements per K, 2000 perms per K ----
print("\n=== Chance-null random K-placements (2000 perms per K) ===", file=sys.stderr)
N_PERM = 2000
rng_chance = random.Random(20260413)
chance_per_k = {}
for K in K_VALUES:
    hits_list = []
    valid_lo = PRIMARY_W
    valid_hi = N - PRIMARY_W
    for _ in range(N_PERM):
        preds = sorted(rng_chance.sample(range(valid_lo, valid_hi), K))
        hits_list.append(detect(preds, true_boundaries, PRIMARY_EPS))
    m = statistics.mean(hits_list)
    sd = statistics.stdev(hits_list) if len(hits_list) > 1 else 0
    obs = real_per_k[K]['hits']
    z = (obs - m) / sd if sd > 0 else 0
    p_emp = sum(1 for x in hits_list if x >= obs) / len(hits_list)
    sorted_null = sorted(hits_list)
    pct_999 = sorted_null[int(0.9975 * N_PERM)]
    passed = obs > pct_999
    chance_per_k[K] = {
        'null_mean': m, 'null_sd': sd, 'null_9975_pct': pct_999,
        'z': z, 'p_empirical': p_emp, 'passes_at_alpha_0025': passed,
    }
    print(f"chance K={K}: obs={obs}, null {m:.2f}±{sd:.2f}, z={z:+.2f}, "
          f"pct99.75={pct_999}, pass_0.0025={passed}", file=sys.stderr)

# ---- Uniform-shuffle null: 30 perms ----
print("\n=== Uniform-shuffle null (30 perms, each full JS scan) ===", file=sys.stderr)
N_SHUF = 30
shuf_per_k = {K: [] for K in K_VALUES}
rng_shuf = random.Random(20260413)
for si in range(N_SHUF):
    letters = list(quran_str)
    rng_shuf.shuffle(letters)
    shuf_str = ''.join(letters)
    positions_s, scores_s = scan_boundaries(shuf_str, PRIMARY_W, STRIDE)
    for K in K_VALUES:
        preds = top_k_local_maxima(positions_s, scores_s, K, MIN_SEP)
        hits = detect(preds, true_boundaries, PRIMARY_EPS)
        shuf_per_k[K].append(hits)
    if (si + 1) % 5 == 0:
        print(f"  shuf perm {si+1}/{N_SHUF}", file=sys.stderr)

shuf_stats_per_k = {}
for K in K_VALUES:
    hl = shuf_per_k[K]
    m = statistics.mean(hl)
    sd = statistics.stdev(hl) if len(hl) > 1 else 0
    obs = real_per_k[K]['hits']
    z = (obs - m) / sd if sd > 0 else 0
    shuf_stats_per_k[K] = {
        'hits': hl, 'mean': m, 'sd': sd, 'min': min(hl), 'max': max(hl),
        'z_real_vs_shuf': z,
    }
    print(f"shuf K={K}: obs={obs}, shuf {m:.2f}±{sd:.2f} (range {min(hl)}-{max(hl)}), z={z:+.2f}",
          file=sys.stderr)

# ---- Summarize localization ----
# Key question: does precision stay flat (localized) or degrade (diffuse)?
# Under "diffuse" hypothesis: expected precision = n_true * eps_ratio / K ?
# Chance precision: null_mean / K at each K.
print("\n=== Localization analysis ===", file=sys.stderr)
print("K      real_P    real_R    real_F1    chance_P    lift_P    lift_F1", file=sys.stderr)
localization = {}
for K in K_VALUES:
    rp = real_per_k[K]['precision']
    rr = real_per_k[K]['recall']
    rf = real_per_k[K]['f1']
    cp = chance_per_k[K]['null_mean'] / K
    cr = chance_per_k[K]['null_mean'] / N_TRUE
    cf = (2 * cp * cr / (cp + cr)) if (cp + cr) > 0 else 0
    lift_p = rp / cp if cp > 0 else 0
    lift_f = rf / cf if cf > 0 else 0
    localization[K] = {
        'real_precision': rp, 'real_recall': rr, 'real_f1': rf,
        'chance_precision': cp, 'chance_recall': cr, 'chance_f1': cf,
        'precision_lift': lift_p, 'f1_lift': lift_f,
    }
    print(f"{K:5d}  {rp:.3f}   {rr:.3f}   {rf:.3f}     {cp:.3f}    {lift_p:.3f}    {lift_f:.3f}",
          file=sys.stderr)

# Interpretation: if lift_P decreases as K grows, signal is localized (few strong peaks).
# If lift_P is flat, signal is diffuse.
k_vals_sorted = sorted(K_VALUES)
lifts = [localization[K]['precision_lift'] for K in k_vals_sorted]
# Monotone check — is lift[K=30] > lift[K=300]?
tight_lift = lifts[0]  # K=30
loose_lift = lifts[-1]  # K=300
ratio = tight_lift / loose_lift if loose_lift > 0 else 0
if ratio > 1.5:
    localization_verdict = "LOCALIZED — tight K retains higher precision-lift"
elif ratio > 1.1:
    localization_verdict = "MILDLY-LOCALIZED"
elif ratio > 0.9:
    localization_verdict = "DIFFUSE — signal is approximately uniform across K"
else:
    localization_verdict = "INVERTED — loose K has higher lift (unusual)"

print(f"\nlift@K=30 / lift@K=300 = {ratio:.3f} → {localization_verdict}", file=sys.stderr)

out = {
    'seed': 20260413,
    'hypothesis': 'H-NEW-24-B2 K-sensitivity sweep',
    'parent_finding': 'h-new-24',
    'rules_tuple': 'rasm no-tashkeel, whitespace-stripped, letter-level',
    'primary_w': PRIMARY_W,
    'primary_epsilon': PRIMARY_EPS,
    'stride': STRIDE,
    'min_separation': MIN_SEP,
    'K_values': K_VALUES,
    'N_true': N_TRUE,
    'N_letters': N,
    'alphabet_size': A,
    'real_per_k': real_per_k,
    'chance_null_per_k': chance_per_k,
    'shuffle_null_per_k': shuf_stats_per_k,
    'localization': localization,
    'localization_lift_ratio_30_over_300': ratio,
    'localization_verdict': localization_verdict,
}

out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-new-24-b2.json'
out_path.write_text(json.dumps(out, indent=2, default=str))
print(f"\nsaved: {out_path}", file=sys.stderr)
