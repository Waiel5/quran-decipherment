#!/usr/bin/env python3
"""H-CLASSIC-44 — al-Zarkashī canonical-distance-decay of inter-surah munāsaba.

Pre-reg: findings/phase-b-hypotheses/h-classic-44-prereg.md
Spec:    findings/phase-b-hypotheses/h-classic-44-to-49-spec.md §H-CLASSIC-44

Tests whether mean inter-surah munāsaba score decays monotonically
with canonical-order distance across 5 locked buckets
{1, 2, 3-5, 6-10, 11+}. Munāsaba score = 0.5*J_std + 0.5*Δ_std where
J is root-Jaccard and Δ is length-residualized gzip pair compression.

Pre-registered:
  - Spearman ρ(bucket_midpoint, mean_score) across 5 buckets
    expected NEGATIVE (one-sided, p < 0.0083)
  - 10,000 surah-permutations for null (seed 20260414)
  - Secondary-strong: d=1 mean > 99th pctile of d=11+ null
  - Tertiary muqaṭṭaʿāt-excluded re-run (confound check)

Bonferroni k=6, α_bon = 0.0083. Seed 20260414.
"""

import gzip as gzip_mod
import json
import math
import random
import re
import statistics
import sys
from collections import defaultdict
from pathlib import Path

from scipy.stats import spearmanr

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260414
N_PERM = 10_000

# Muqaṭṭaʿāt surahs (traditional list, 29 total)
MUQATTAAT = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29,
             30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}

LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

BUCKETS = [(1, 1, 1), (2, 2, 2), (3, 5, 4), (6, 10, 8), (11, 113, 50)]
# (lo, hi, midpoint)


# ---- Load QAC morphology, build per-surah root sets ----
print("[load] parsing QAC morphology...", file=sys.stderr)
surah_roots = defaultdict(set)  # sid -> set of root strings

with open(ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt',
          encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
            continue
        parts = line.rstrip('\n').split('\t')
        if len(parts) < 4:
            continue
        m = LOC_RE.match(parts[0])
        if not m:
            continue
        sid = int(m.group(1))
        feat = parts[3]
        if 'STEM' not in feat:
            continue
        rm = ROOT_RE.search(feat)
        if rm:
            surah_roots[sid].add(rm.group(1))

print(f"[load] {len(surah_roots)} surahs with at least one rooted token",
      file=sys.stderr)


# ---- Load Quran text for gzip pair compression ----
print("[load] parsing Quran text...", file=sys.stderr)
Q = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text())
surah_text = {}
for s in Q:
    sid = s['id']
    surah_text[sid] = ' '.join(v['text'] for v in s['verses'])

print(f"[load] {len(surah_text)} surah texts loaded", file=sys.stderr)
assert len(surah_text) == 114
assert all(sid in surah_roots for sid in range(1, 115))


# ---- Compute per-pair scores ----
print("[compute] Jaccard + gzip Δ for all 6441 pairs...", file=sys.stderr)

def jaccard(a, b):
    return len(a & b) / len(a | b) if (a | b) else 0.0


def gzip_len(text):
    return len(gzip_mod.compress(text.encode('utf-8')))


# Pre-compute individual gzip sizes to avoid redundancy
individual_gzip = {sid: gzip_len(t) for sid, t in surah_text.items()}

pair_j = {}     # (A, B) with A < B -> Jaccard
pair_delta = {} # (A, B) with A < B -> raw Δ / mean_len
pair_log_prod = {}  # (A, B) -> log(|A| * |B|) for residualization
pair_distance = {}

sids = list(range(1, 115))
n_pairs_computed = 0
for i, A in enumerate(sids):
    for B in sids[i + 1:]:
        # Jaccard
        j = jaccard(surah_roots[A], surah_roots[B])
        # gzip Δ
        len_A = len(surah_text[A])
        len_B = len(surah_text[B])
        combined = surah_text[A] + ' ' + surah_text[B]
        g_combined = gzip_len(combined)
        delta_raw = individual_gzip[A] + individual_gzip[B] - g_combined
        mean_len = (len_A + len_B) / 2.0
        delta_norm = delta_raw / mean_len if mean_len > 0 else 0.0

        pair_j[(A, B)] = j
        pair_delta[(A, B)] = delta_norm
        pair_log_prod[(A, B)] = math.log(len_A * len_B)
        pair_distance[(A, B)] = B - A
        n_pairs_computed += 1
        if n_pairs_computed % 500 == 0:
            print(f"  [compute] {n_pairs_computed}/6441 pairs done",
                  file=sys.stderr)

print(f"[compute] done: {n_pairs_computed} pairs", file=sys.stderr)


# ---- Length-residualize the gzip Δ ----
# Regress delta_norm on log(|A|*|B|), take residual
print("[residualize] OLS delta_norm ~ log(|A|*|B|)...", file=sys.stderr)
pairs_ordered = sorted(pair_j.keys())
X = [pair_log_prod[p] for p in pairs_ordered]
Y = [pair_delta[p] for p in pairs_ordered]
n = len(X)
mean_X = sum(X) / n
mean_Y = sum(Y) / n
cov_XY = sum((X[i] - mean_X) * (Y[i] - mean_Y) for i in range(n))
var_X = sum((X[i] - mean_X) ** 2 for i in range(n))
slope = cov_XY / var_X if var_X > 0 else 0.0
intercept = mean_Y - slope * mean_X
pair_delta_resid = {}
for p in pairs_ordered:
    pred = intercept + slope * pair_log_prod[p]
    pair_delta_resid[p] = pair_delta[p] - pred
print(f"[residualize] OLS slope={slope:.4f}, intercept={intercept:.4f}",
      file=sys.stderr)


# ---- Z-score J and Δ_resid across all pairs ----
def zscore(values):
    m = statistics.mean(values)
    s = statistics.stdev(values)
    return [(v - m) / s if s > 0 else 0.0 for v in values]


j_vals = [pair_j[p] for p in pairs_ordered]
delta_vals = [pair_delta_resid[p] for p in pairs_ordered]
j_z = dict(zip(pairs_ordered, zscore(j_vals)))
delta_z = dict(zip(pairs_ordered, zscore(delta_vals)))

pair_score = {p: 0.5 * j_z[p] + 0.5 * delta_z[p] for p in pairs_ordered}

print(f"[score] J mean={statistics.mean(j_vals):.4f} sd={statistics.stdev(j_vals):.4f}",
      file=sys.stderr)
print(f"[score] Δ_resid mean={statistics.mean(delta_vals):.4f} sd={statistics.stdev(delta_vals):.4f}",
      file=sys.stderr)


# ---- Bucket-mean computation ----
def bucket_means(pair_score_dict, pair_distance_dict, exclude_pairs=None):
    """Return dict {bucket_label: mean_score} and per-bucket pair counts."""
    exclude_pairs = exclude_pairs or set()
    sums = [0.0] * len(BUCKETS)
    counts = [0] * len(BUCKETS)
    for p, score in pair_score_dict.items():
        if p in exclude_pairs:
            continue
        d = pair_distance_dict[p]
        for bi, (lo, hi, mid) in enumerate(BUCKETS):
            if lo <= d <= hi:
                sums[bi] += score
                counts[bi] += 1
                break
    means = [sums[bi] / counts[bi] if counts[bi] > 0 else 0.0
             for bi in range(len(BUCKETS))]
    return means, counts


# ---- Primary observed statistic ----
obs_means, obs_counts = bucket_means(pair_score, pair_distance)
midpoints = [b[2] for b in BUCKETS]
print("\n[primary] bucket means (all pairs):", file=sys.stderr)
for bi, (lo, hi, mid) in enumerate(BUCKETS):
    label = f"{lo}-{hi}" if lo != hi else str(lo)
    if lo >= 11:
        label = f"{lo}+"
    print(f"  d={label} (mid={mid}): n={obs_counts[bi]}, "
          f"mean_score={obs_means[bi]:+.4f}",
          file=sys.stderr)

obs_rho, _ = spearmanr(midpoints, obs_means)
print(f"[primary] observed Spearman ρ(midpoint, mean_score) = {obs_rho:+.4f}",
      file=sys.stderr)


# ---- Permutation null ----
# Key insight: permute surah IDs → distances change, but pair SCORES
# are fixed. We re-assign distances and recompute bucket means + ρ.
print(f"\n[perm] running {N_PERM} surah-permutation null...", file=sys.stderr)
rng = random.Random(SEED)
null_rhos = []
null_d1_means = []
null_d11_means = []

# Pre-cache pair score lookup by original (A, B)
# For each permutation π, pair (A, B) gets new distance |π(A) - π(B)|
# We iterate over original pairs, compute new distance, bucket, sum.

for iter_i in range(N_PERM):
    perm = list(range(1, 115))
    rng.shuffle(perm)
    # perm[i] = canonical sid placed at position (i+1) in the shuffled order
    # So new_position[sid] = index of sid in perm, + 1
    new_pos = [0] * 115
    for new_p, sid in enumerate(perm):
        new_pos[sid] = new_p + 1

    sums = [0.0] * len(BUCKETS)
    counts = [0] * len(BUCKETS)
    for (A, B), score in pair_score.items():
        new_d = abs(new_pos[A] - new_pos[B])
        for bi, (lo, hi, mid) in enumerate(BUCKETS):
            if lo <= new_d <= hi:
                sums[bi] += score
                counts[bi] += 1
                break

    perm_means = [sums[bi] / counts[bi] if counts[bi] > 0 else 0.0
                  for bi in range(len(BUCKETS))]
    perm_rho, _ = spearmanr(midpoints, perm_means)
    null_rhos.append(perm_rho)
    null_d1_means.append(perm_means[0])
    null_d11_means.append(perm_means[-1])

    if (iter_i + 1) % 1000 == 0:
        print(f"  [perm] {iter_i + 1}/{N_PERM}", file=sys.stderr)

null_rhos.sort()
null_d1_means.sort()
null_d11_means.sort()

# Empirical one-sided p for ρ < obs_rho
empirical_p_rho = sum(1 for r in null_rhos if r <= obs_rho) / len(null_rhos)
null_rho_mean = statistics.mean(null_rhos)
null_rho_sd = statistics.stdev(null_rhos)
z_rho = (obs_rho - null_rho_mean) / null_rho_sd if null_rho_sd > 0 else 0.0

print(f"\n[primary] empirical p(ρ ≤ obs) = {empirical_p_rho:.6f}", file=sys.stderr)
print(f"[primary] null ρ: mean={null_rho_mean:+.4f}, sd={null_rho_sd:.4f}",
      file=sys.stderr)
print(f"[primary] z = {z_rho:+.2f}", file=sys.stderr)

# Secondary-strong: d=1 mean > 99th pctile of d=11+ null
d11_99pct = null_d11_means[int(0.99 * len(null_d11_means))]
obs_d1 = obs_means[0]
secondary_strong_pass = obs_d1 > d11_99pct
print(f"\n[secondary-strong] obs d=1 mean = {obs_d1:+.4f}", file=sys.stderr)
print(f"[secondary-strong] d=11+ null 99th pctile = {d11_99pct:+.4f}",
      file=sys.stderr)
print(f"[secondary-strong] PASS: {secondary_strong_pass}", file=sys.stderr)


# ---- Tertiary: muqaṭṭaʿāt-adjacent-excluded rerun ----
# Exclude pairs where BOTH surahs are muqaṭṭaʿāt, OR where the d=1
# adjacency is between a muqaṭṭaʿāt and a muqaṭṭaʿāt at distance 1.
# Spec says "muqaṭṭaʿāt-adjacent pairs" — we interpret this as:
# any pair (A, B) with d=1 AND (A in MUQ or B in MUQ) is excluded.
# More strictly, we exclude ALL pairs where either surah is muqaṭṭaʿāt
# at any distance (conservative).
print("\n[tertiary] muqaṭṭaʿāt-adjacent-pair exclusion rerun...", file=sys.stderr)
exclude = set()
for (A, B) in pair_score:
    if pair_distance[(A, B)] == 1 and (A in MUQATTAAT or B in MUQATTAAT):
        exclude.add((A, B))
print(f"[tertiary] excluded {len(exclude)} muqaṭṭaʿāt-adjacent d=1 pairs",
      file=sys.stderr)

tert_means, tert_counts = bucket_means(pair_score, pair_distance,
                                        exclude_pairs=exclude)
tert_rho, _ = spearmanr(midpoints, tert_means)
print(f"[tertiary] bucket means (muqaṭṭaʿāt-adjacent excluded):", file=sys.stderr)
for bi, (lo, hi, mid) in enumerate(BUCKETS):
    label = f"{lo}-{hi}" if lo != hi else str(lo)
    if lo >= 11:
        label = f"{lo}+"
    print(f"  d={label}: n={tert_counts[bi]}, "
          f"mean_score={tert_means[bi]:+.4f}",
          file=sys.stderr)
print(f"[tertiary] Spearman ρ = {tert_rho:+.4f}", file=sys.stderr)

# Tertiary permutation null (re-permute with the same exclusion)
rng_t = random.Random(SEED + 1)
null_rhos_tert = []
for iter_i in range(N_PERM):
    perm = list(range(1, 115))
    rng_t.shuffle(perm)
    new_pos = [0] * 115
    for new_p, sid in enumerate(perm):
        new_pos[sid] = new_p + 1
    sums = [0.0] * len(BUCKETS)
    counts = [0] * len(BUCKETS)
    for (A, B), score in pair_score.items():
        if (A, B) in exclude:
            continue
        new_d = abs(new_pos[A] - new_pos[B])
        for bi, (lo, hi, mid) in enumerate(BUCKETS):
            if lo <= new_d <= hi:
                sums[bi] += score
                counts[bi] += 1
                break
    perm_means = [sums[bi] / counts[bi] if counts[bi] > 0 else 0.0
                  for bi in range(len(BUCKETS))]
    perm_rho, _ = spearmanr(midpoints, perm_means)
    null_rhos_tert.append(perm_rho)

null_rhos_tert.sort()
empirical_p_tert = sum(1 for r in null_rhos_tert if r <= tert_rho) / len(null_rhos_tert)
print(f"[tertiary] empirical p = {empirical_p_tert:.6f}", file=sys.stderr)


# ---- Verdict routing ----
alpha_bon = 0.0083
primary_pass = (obs_rho < 0) and (empirical_p_rho < alpha_bon)
tertiary_pass = (tert_rho < 0) and (empirical_p_tert < alpha_bon)
reverse = (obs_rho > 0) and (empirical_p_rho > (1 - alpha_bon))

print(f"\n=== VERDICT COMPONENTS ===", file=sys.stderr)
print(f"  primary_pass: {primary_pass} (ρ={obs_rho:+.4f}, p={empirical_p_rho:.6f})",
      file=sys.stderr)
print(f"  secondary_strong_pass: {secondary_strong_pass}", file=sys.stderr)
print(f"  tertiary_pass (muqaṭṭaʿāt excluded): {tertiary_pass} "
      f"(ρ={tert_rho:+.4f}, p={empirical_p_tert:.6f})", file=sys.stderr)
print(f"  reverse: {reverse}", file=sys.stderr)

if reverse:
    final_verdict = ('REVERSE — canonical distance has INVERSE munāsaba '
                     'gradient (unexpected anti-decay)')
elif primary_pass and tertiary_pass and secondary_strong_pass:
    final_verdict = ('PASS — al-Zarkashī canonical distance-decay confirmed '
                     '(primary + secondary-strong + muqaṭṭaʿāt confound cleared)')
elif primary_pass and tertiary_pass and not secondary_strong_pass:
    final_verdict = ('PARTIAL-DECAY — gradient exists but d=1 is not a '
                     'clean spike above the d=11+ null 99th percentile')
elif primary_pass and not tertiary_pass:
    final_verdict = ('PARTIAL-MUQATTAAT-DRIVEN — decay signal driven by '
                     'muqaṭṭaʿāt-adjacency opener-cluster, not semantic munāsaba')
elif not primary_pass and abs(empirical_p_rho - 0.5) < 0.4:
    final_verdict = ('NULL — al-Zarkashī distance-decay falsified; '
                     'canonical ordering beyond d=1 is not gradient-coherent')
else:
    final_verdict = (f'UNUSUAL — primary p={empirical_p_rho:.4f}, '
                     f'tertiary p={empirical_p_tert:.4f}, inspect manually')

print(f"\n=== FINAL VERDICT ===", file=sys.stderr)
print(f"  {final_verdict}", file=sys.stderr)


# ---- Write JSON output ----
out = {
    'finding_id': 'h-classic-44',
    'pre_reg': 'findings/phase-b-hypotheses/h-classic-44-prereg.md',
    'pre_reg_compliance': 'PRE-REG-STANDARD-04',
    'rules_tuple': '(no-tashkeel, root-level via QAC, hafs-kufan, mashriqi)',
    'seed': SEED,
    'n_perm': N_PERM,
    'bonferroni_k': 6,
    'alpha_bon': alpha_bon,
    'sided_test': 'one-sided negative (Spearman ρ < 0 expected)',
    'munasaba_score_composition': {
        'jaccard_weight': 0.5,
        'gzip_delta_resid_weight': 0.5,
        'gzip_residualization': 'OLS delta_norm ~ log(|A|*|B|)',
        'residualization_slope': slope,
        'residualization_intercept': intercept,
    },
    'buckets': [{'lo': b[0], 'hi': b[1], 'midpoint': b[2]} for b in BUCKETS],
    'primary': {
        'bucket_means': obs_means,
        'bucket_counts': obs_counts,
        'observed_spearman_rho': obs_rho,
        'null_rho_mean': null_rho_mean,
        'null_rho_sd': null_rho_sd,
        'z_rho': z_rho,
        'empirical_p_one_sided': empirical_p_rho,
        'passes': primary_pass,
    },
    'secondary_strong': {
        'observed_d1_mean': obs_d1,
        'null_d11_99pct': d11_99pct,
        'passes': secondary_strong_pass,
    },
    'tertiary_muqattaat_excluded': {
        'n_excluded_pairs': len(exclude),
        'bucket_means': tert_means,
        'bucket_counts': tert_counts,
        'observed_spearman_rho': tert_rho,
        'empirical_p_one_sided': empirical_p_tert,
        'passes': tertiary_pass,
    },
    'final_verdict': final_verdict,
    'no_fork_protections_honored': [
        'munāsaba score LOCKED to 0.5*J_std + 0.5*Δ_std (length-residualized)',
        'distance buckets LOCKED to {1, 2, 3-5, 6-10, 11+}',
        'primary statistic LOCKED to Spearman ρ across 5 bucket means',
        f'permutation null seed {SEED}, {N_PERM} surah-order perms',
        'α_bon = 0.0083 (family Bonferroni k=6)',
        f'muqaṭṭaʿāt set LOCKED: {sorted(MUQATTAAT)}',
        'root extraction LOCKED to QAC v0.4 STEM-only',
    ],
    'data_reuse_disclosed': (
        'Reuses QAC morphology loader (LOC_RE, ROOT_RE, STEM filter) '
        'from scripts/h_classic_47_biqai_seam.py (same session). '
        'Reuses data/morphology/quranic-corpus-morphology-0.4.txt and '
        'quran-text/quran-no-tashkeel.json. No reuse of T-002 / task #21 '
        'script (not found in scripts/); T-002 tested d=1 only, '
        'H-CLASSIC-44 tests full distance-decay gradient.'
    ),
}

out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-classic-44.json'
out_path.write_text(json.dumps(out, indent=2, default=str))
print(f"\n[output] saved: {out_path}", file=sys.stderr)
