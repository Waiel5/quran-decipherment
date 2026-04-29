#!/usr/bin/env python3
"""H-NEW-24-B1 — Length-confound orthogonalization (sub-e + sub-f).

audit-019 load-bearing blocker for H-NEW-24. Parent finding established
that letter-multiset JS-scan detects 41/113 surah boundaries at
(w=2000, eps=500), well above chance (null mean 24.6, sd 3.75, z=+4.39).
Sub-(c) uniform-shuffle control showed the signal is not a pure window-
size / position artifact (shuffled Quran → 28 hits, within 95% band).

Sub-(c) uniform shuffle destroys BOTH per-surah heterogeneity AND
ordering, so it cannot distinguish:
  - "per-surah letter inventories differ" (novel claim)
  - "long-to-short transitions cause sampling discontinuities" (trivial
     length confound)
  - "letter-order within a surah matters" (compositional claim)

Sub-(e) WITHIN-SURAH shuffle: preserve surah boundaries, shuffle letters
  within each surah. Per-surah multisets preserved, letter order destroyed.
  If hits stay near 41 -> signal is in multiset heterogeneity (novel claim).
  If hits drop to chance -> signal is in letter ordering.

Sub-(f) LENGTH-MATCHED i.i.d. null: build a synthetic corpus of 114 blocks
  with exact Quranic surah lengths, each block sampled i.i.d. from the
  global Quranic letter unigram distribution. Per-surah heterogeneity
  DESTROYED, length pattern PRESERVED.
  If hits near 41 -> finding collapses to trivial length confound.
  If hits near chance (24.6) -> per-surah heterogeneity is real.

Each null is re-run 50 times to get a distribution (not just one point).
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


# ---- Load Quran, extract per-surah letter strings ----
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
for i, L in enumerate(surah_lengths[:-1]):
    acc += L
    true_boundaries.append(acc)

print(f"total letter count: {N}", file=sys.stderr)
print(f"interior boundaries: {len(true_boundaries)}", file=sys.stderr)
print(f"shortest surah: {min(surah_lengths)} (surah {surah_lengths.index(min(surah_lengths))+1})",
      file=sys.stderr)
print(f"longest surah: {max(surah_lengths)} (surah {surah_lengths.index(max(surah_lengths))+1})",
      file=sys.stderr)

alphabet = sorted(set(quran_str))
ALPHA_IDX = {c: i for i, c in enumerate(alphabet)}
A = len(alphabet)
print(f"alphabet size: {A}", file=sys.stderr)

# Global unigram distribution for sub-(f)
global_counts = [0] * A
for ch in quran_str:
    global_counts[ALPHA_IDX[ch]] += 1
total_global = sum(global_counts)
global_probs = [c / total_global for c in global_counts]
# Cumulative for sampling
cum = []
s = 0.0
for p in global_probs:
    s += p
    cum.append(s)


# ---- JS divergence helper ----
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


# ---- Synthesizers for sub-(e) and sub-(f) ----
def synth_within_surah_shuffle(rng):
    """Sub-(e). Shuffle letters within each surah; surah order and lengths
    preserved; per-surah multisets preserved."""
    parts = []
    for s in per_surah_letters:
        letters = list(s)
        rng.shuffle(letters)
        parts.append(''.join(letters))
    return ''.join(parts)


def synth_length_matched_iid(rng):
    """Sub-(f). For each surah, draw len(surah) characters i.i.d. from global
    unigram. Surah lengths preserved; per-surah heterogeneity destroyed."""
    parts = []
    for L in surah_lengths:
        buf = []
        for _ in range(L):
            r = rng.random()
            lo, hi = 0, A - 1
            while lo < hi:
                mid = (lo + hi) // 2
                if cum[mid] < r:
                    lo = mid + 1
                else:
                    hi = mid
            buf.append(alphabet[lo])
        parts.append(''.join(buf))
    return ''.join(parts)


# ---- Main experiment ----
K = 113
MIN_SEP = 500
PRIMARY_W = 2000
PRIMARY_EPS = 500
N_PERMS = 50  # per-null (both sub-e and sub-f)

print(f"\n=== Running {N_PERMS} perms per null-type ===", file=sys.stderr)


def run_null(synth_fn, label):
    rng = random.Random(20260413)
    hit_list = []
    for i in range(N_PERMS):
        text = synth_fn(rng)
        positions, scores = scan_boundaries(text, PRIMARY_W)
        preds = top_k_local_maxima(positions, scores, K, MIN_SEP)
        hits = detect(preds, true_boundaries, PRIMARY_EPS)
        hit_list.append(hits)
        if (i + 1) % 10 == 0:
            print(f"  [{label}] perm {i+1}/{N_PERMS}: hits={hits}", file=sys.stderr)
    return hit_list


print("\n--- Sub-(e): within-surah shuffle ---", file=sys.stderr)
sub_e_hits = run_null(synth_within_surah_shuffle, 'e')
e_mean = statistics.mean(sub_e_hits)
e_sd = statistics.stdev(sub_e_hits) if len(sub_e_hits) > 1 else 0
print(f"sub-(e) hits: mean={e_mean:.2f} ± {e_sd:.2f}, min={min(sub_e_hits)}, max={max(sub_e_hits)}",
      file=sys.stderr)

print("\n--- Sub-(f): length-matched i.i.d. ---", file=sys.stderr)
sub_f_hits = run_null(synth_length_matched_iid, 'f')
f_mean = statistics.mean(sub_f_hits)
f_sd = statistics.stdev(sub_f_hits) if len(sub_f_hits) > 1 else 0
print(f"sub-(f) hits: mean={f_mean:.2f} ± {f_sd:.2f}, min={min(sub_f_hits)}, max={max(sub_f_hits)}",
      file=sys.stderr)

# Reference values from H-NEW-24 parent
OBSERVED_REAL_HITS = 41
CHANCE_MEAN = 24.57
CHANCE_SD = 3.75

# Interpretation
# Sub-(e): if e_mean ≈ 41 → multiset claim strong; if e_mean ≈ 24.6 → ordering
# Sub-(f): if f_mean ≈ 41 → length confound fully explains; if ≈ 24.6 → multiset real

# z against chance null
z_e_vs_chance = (e_mean - CHANCE_MEAN) / CHANCE_SD
z_f_vs_chance = (f_mean - CHANCE_MEAN) / CHANCE_SD

# z against real Quran (pre-registered: does null reach observed 41?)
z_e_vs_real = (OBSERVED_REAL_HITS - e_mean) / e_sd if e_sd > 0 else float('inf')
z_f_vs_real = (OBSERVED_REAL_HITS - f_mean) / f_sd if f_sd > 0 else float('inf')

print("\n=== Interpretation ===", file=sys.stderr)
print(f"Real Quran observed: {OBSERVED_REAL_HITS} hits", file=sys.stderr)
print(f"Chance null mean: {CHANCE_MEAN}", file=sys.stderr)
print(f"Sub-(e) mean: {e_mean:.2f}  z vs chance = {z_e_vs_chance:+.2f}", file=sys.stderr)
print(f"Sub-(f) mean: {f_mean:.2f}  z vs chance = {z_f_vs_chance:+.2f}", file=sys.stderr)

# Decomposition: fraction of real signal preserved by each null
real_excess = OBSERVED_REAL_HITS - CHANCE_MEAN  # 16.43
e_excess = e_mean - CHANCE_MEAN
f_excess = f_mean - CHANCE_MEAN
e_preserved_frac = e_excess / real_excess if real_excess > 0 else 0
f_preserved_frac = f_excess / real_excess if real_excess > 0 else 0
print(f"\nSignal decomposition:", file=sys.stderr)
print(f"  Real excess over chance: {real_excess:.2f}", file=sys.stderr)
print(f"  Sub-(e) preserves: {e_excess:.2f} ({100*e_preserved_frac:.1f}%) — multiset contribution",
      file=sys.stderr)
print(f"  Sub-(f) preserves: {f_excess:.2f} ({100*f_preserved_frac:.1f}%) — length contribution",
      file=sys.stderr)
letter_order_contribution = real_excess - e_excess
print(f"  Remaining: {letter_order_contribution:.2f} "
      f"({100*letter_order_contribution/real_excess:.1f}%) — letter-order contribution",
      file=sys.stderr)

# Verdict
NOVEL_CLAIM_THRESHOLD = 0.5  # e_preserved_frac >= 0.5 means multiset claim carries majority
TRIVIAL_CONFOUND_THRESHOLD = 0.5  # f_preserved_frac >= 0.5 means trivially length-driven

if e_preserved_frac >= NOVEL_CLAIM_THRESHOLD and f_preserved_frac < TRIVIAL_CONFOUND_THRESHOLD:
    verdict = "NOVEL-MULTISET-CLAIM-CONFIRMED"
elif f_preserved_frac >= TRIVIAL_CONFOUND_THRESHOLD and e_preserved_frac < NOVEL_CLAIM_THRESHOLD:
    verdict = "TRIVIAL-LENGTH-CONFOUND"
elif e_preserved_frac >= NOVEL_CLAIM_THRESHOLD and f_preserved_frac >= TRIVIAL_CONFOUND_THRESHOLD:
    verdict = "MIXED-BOTH-CONTRIBUTE"
else:
    verdict = "SIGNAL-LARGELY-IN-LETTER-ORDERING"

print(f"\n=== VERDICT: {verdict} ===", file=sys.stderr)

out = {
    'seed': 20260413,
    'hypothesis': 'H-NEW-24-B1 length-confound orthogonalization',
    'parent_finding': 'h-new-24',
    'rules_tuple': 'rasm no-tashkeel, whitespace-stripped, letter-level',
    'primary_w': PRIMARY_W,
    'primary_epsilon': PRIMARY_EPS,
    'K': K,
    'min_separation': MIN_SEP,
    'n_perms_per_null': N_PERMS,
    'alphabet_size': A,
    'total_letters': N,
    'true_boundaries_count': len(true_boundaries),
    'reference': {
        'real_quran_hits': OBSERVED_REAL_HITS,
        'chance_null_mean': CHANCE_MEAN,
        'chance_null_sd': CHANCE_SD,
    },
    'sub_e_within_surah_shuffle': {
        'description': 'Preserve surah lengths and per-surah multisets; shuffle letters within each surah',
        'hits': sub_e_hits,
        'mean': e_mean,
        'sd': e_sd,
        'min': min(sub_e_hits),
        'max': max(sub_e_hits),
        'z_vs_chance_null': z_e_vs_chance,
        'z_vs_real_observation': z_e_vs_real,
        'excess_over_chance': e_excess,
        'fraction_of_real_signal_preserved': e_preserved_frac,
        'interpretation': ('high fraction => signal lives in per-surah multiset inventories '
                           '(novel claim confirmed); low => signal lives in letter ordering'),
    },
    'sub_f_length_matched_iid': {
        'description': ('Preserve surah lengths; sample each surah i.i.d. from global unigram; '
                        'per-surah heterogeneity destroyed'),
        'hits': sub_f_hits,
        'mean': f_mean,
        'sd': f_sd,
        'min': min(sub_f_hits),
        'max': max(sub_f_hits),
        'z_vs_chance_null': z_f_vs_chance,
        'z_vs_real_observation': z_f_vs_real,
        'excess_over_chance': f_excess,
        'fraction_of_real_signal_preserved': f_preserved_frac,
        'interpretation': ('high fraction => length-sampling confound explains the finding; '
                           'low => per-surah heterogeneity is a real component'),
    },
    'decomposition': {
        'real_excess_over_chance': real_excess,
        'multiset_contribution': e_excess,
        'length_contribution': f_excess,
        'letter_ordering_contribution': letter_order_contribution,
        'multiset_fraction': e_preserved_frac,
        'length_fraction': f_preserved_frac,
        'letter_ordering_fraction': letter_order_contribution / real_excess if real_excess > 0 else 0,
    },
    'verdict': verdict,
}

out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-new-24-b1.json'
out_path.parent.mkdir(parents=True, exist_ok=True)
out_path.write_text(json.dumps(out, indent=2, default=str))
print(f"\nsaved: {out_path}", file=sys.stderr)
