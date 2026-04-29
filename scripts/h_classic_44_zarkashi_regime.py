#!/usr/bin/env python3
"""H-CLASSIC-44 — al-Zarkashī canonical-distance-decay with 3-sub-test regime cut.

Pre-reg: findings/phase-b-hypotheses/h-classic-44-prereg.md
Spec:    task #95 updated 2026-04-13 with hierarchical Bonferroni and
         meta-analyst local-vs-distant regime cut.

Three sub-tests:
  A — macro-architectural: Spearman ρ(bucket_mid, mean_score) < 0
  B — local-pairwise d=1 seam coherence: mean d=1 > 99th pctile null
  C — regime-discrimination: R = mean(d=1)/mean(d=11+) > 99th pctile null
      secondary: D = mean(d=1) - mean(d=11+) (diagnostic, not verdict)

PRE-REG-STANDARD-05 hierarchical Bonferroni: α_bon = 0.00278
(= 0.05 / 6 outer / 3 inner).
Seeds: 20260414 / 20260415 / 20260416 (one per sub-test).
10,000 permutations each.

Munāsaba score (reused from pre-pilot, unchanged):
  M(A,B) = 0.5 * J_std + 0.5 * Δ_std
where J is root-Jaccard and Δ is length-residualized gzip pair compression.
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
ALPHA_BON = 0.00278  # = 0.05 / 6 / 3 per PRE-REG-STANDARD-05

MUQATTAAT = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29,
             30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}

LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

BUCKETS = [(1, 1, 1), (2, 2, 2), (3, 5, 4), (6, 10, 8), (11, 113, 50)]


# ---- Load QAC + Quran ----
print("[load] parsing QAC morphology...", file=sys.stderr)
surah_roots = defaultdict(set)
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

print(f"[load] {len(surah_roots)} surahs", file=sys.stderr)

Q = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text())
surah_text = {s['id']: ' '.join(v['text'] for v in s['verses']) for s in Q}
print(f"[load] {len(surah_text)} surah texts", file=sys.stderr)
assert len(surah_text) == 114
assert all(sid in surah_roots for sid in range(1, 115))


# ---- Compute pair scores (same as pre-pilot; reload if cached) ----
print("[compute] Jaccard + gzip Δ for all 6441 pairs...", file=sys.stderr)

def jaccard(a, b):
    return len(a & b) / len(a | b) if (a | b) else 0.0


def gzip_len(text):
    return len(gzip_mod.compress(text.encode('utf-8')))


individual_gzip = {sid: gzip_len(t) for sid, t in surah_text.items()}

pair_j = {}
pair_delta = {}
pair_log_prod = {}
pair_distance = {}

sids = list(range(1, 115))
for i, A in enumerate(sids):
    for B in sids[i + 1:]:
        j = jaccard(surah_roots[A], surah_roots[B])
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

print(f"[compute] {len(pair_j)} pairs computed", file=sys.stderr)


# ---- Length-residualize gzip Δ ----
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
pair_delta_resid = {p: pair_delta[p] - (intercept + slope * pair_log_prod[p])
                    for p in pairs_ordered}


# ---- Z-score and combine ----
def zscore_dict(d, keys):
    values = [d[k] for k in keys]
    m = statistics.mean(values)
    s = statistics.stdev(values)
    return {k: (d[k] - m) / s if s > 0 else 0.0 for k in keys}


j_z = zscore_dict(pair_j, pairs_ordered)
delta_z = zscore_dict(pair_delta_resid, pairs_ordered)
pair_score = {p: 0.5 * j_z[p] + 0.5 * delta_z[p] for p in pairs_ordered}


# ---- Bucket helpers ----
def compute_bucket_stats(score_dict, dist_dict, exclude=None):
    """Return (bucket_means, bucket_counts, d1_mean, d11_mean)."""
    exclude = exclude or set()
    sums = [0.0] * len(BUCKETS)
    counts = [0] * len(BUCKETS)
    for p, sc in score_dict.items():
        if p in exclude:
            continue
        d = dist_dict[p]
        for bi, (lo, hi, mid) in enumerate(BUCKETS):
            if lo <= d <= hi:
                sums[bi] += sc
                counts[bi] += 1
                break
    means = [sums[bi] / counts[bi] if counts[bi] > 0 else 0.0
             for bi in range(len(BUCKETS))]
    return means, counts, means[0], means[-1]


def compute_bucket_from_perm(perm_new_pos, exclude=None):
    """Given a permutation's new_pos array, compute bucket means by
    re-mapping pair distances via the permutation."""
    exclude = exclude or set()
    sums = [0.0] * len(BUCKETS)
    counts = [0] * len(BUCKETS)
    for (A, B), sc in pair_score.items():
        if (A, B) in exclude:
            continue
        new_d = abs(perm_new_pos[A] - perm_new_pos[B])
        for bi, (lo, hi, mid) in enumerate(BUCKETS):
            if lo <= new_d <= hi:
                sums[bi] += sc
                counts[bi] += 1
                break
    means = [sums[bi] / counts[bi] if counts[bi] > 0 else 0.0
             for bi in range(len(BUCKETS))]
    return means


# ---- Observed statistics ----
midpoints = [b[2] for b in BUCKETS]

# muqaṭṭaʿāt-adjacent d=1 exclusion set
muq_exclude = set()
for (A, B) in pair_score:
    if pair_distance[(A, B)] == 1 and (A in MUQATTAAT or B in MUQATTAAT):
        muq_exclude.add((A, B))
print(f"[muq] {len(muq_exclude)} d=1 muqaṭṭaʿāt-adjacent pairs excluded in flag run",
      file=sys.stderr)


def run_primary_and_muq_flag(condition_label, exclude):
    """Returns observed stats for sub-tests A, B, C under a given exclusion."""
    means, counts, d1, d11 = compute_bucket_stats(pair_score, pair_distance,
                                                    exclude=exclude)
    rho, _ = spearmanr(midpoints, means)
    ratio = d1 / d11 if d11 != 0 else float('inf')
    diff = d1 - d11
    return {
        'bucket_means': means,
        'bucket_counts': counts,
        'obs_rho_A': rho,
        'obs_d1_mean_B': d1,
        'obs_d11_mean': d11,
        'obs_ratio_C': ratio,
        'obs_diff_C_secondary': diff,
    }


obs_primary = run_primary_and_muq_flag('with_muqattaat', set())
obs_muqflag = run_primary_and_muq_flag('without_muqattaat', muq_exclude)

print("\n[primary obs] with muqaṭṭaʿāt (verdict-binding):", file=sys.stderr)
for bi, (lo, hi, mid) in enumerate(BUCKETS):
    label = f"{lo}-{hi}" if lo != hi else str(lo)
    if lo >= 11:
        label = f"{lo}+"
    print(f"  d={label}: n={obs_primary['bucket_counts'][bi]}, "
          f"mean={obs_primary['bucket_means'][bi]:+.4f}",
          file=sys.stderr)
print(f"[primary obs] ρ = {obs_primary['obs_rho_A']:+.4f}", file=sys.stderr)
print(f"[primary obs] d=1 mean = {obs_primary['obs_d1_mean_B']:+.4f}",
      file=sys.stderr)
print(f"[primary obs] d=11+ mean = {obs_primary['obs_d11_mean']:+.4f}",
      file=sys.stderr)
print(f"[primary obs] ratio = {obs_primary['obs_ratio_C']:+.4f}",
      file=sys.stderr)
print(f"[primary obs] diff = {obs_primary['obs_diff_C_secondary']:+.4f}",
      file=sys.stderr)

print("\n[flag obs] without muqaṭṭaʿāt-adjacent d=1 (diagnostic only):",
      file=sys.stderr)
for bi, (lo, hi, mid) in enumerate(BUCKETS):
    label = f"{lo}-{hi}" if lo != hi else str(lo)
    if lo >= 11:
        label = f"{lo}+"
    print(f"  d={label}: n={obs_muqflag['bucket_counts'][bi]}, "
          f"mean={obs_muqflag['bucket_means'][bi]:+.4f}",
          file=sys.stderr)
print(f"[flag obs] ρ = {obs_muqflag['obs_rho_A']:+.4f}", file=sys.stderr)
print(f"[flag obs] d=1 mean = {obs_muqflag['obs_d1_mean_B']:+.4f}",
      file=sys.stderr)
print(f"[flag obs] ratio = {obs_muqflag['obs_ratio_C']:+.4f}",
      file=sys.stderr)


# ---- Permutation null (three independent streams) ----
def run_null(sub_seed, n_perm):
    """Generates null distributions for ρ, d1, ratio, and diff."""
    rng = random.Random(SEED + sub_seed)
    nulls_rho = []
    nulls_d1 = []
    nulls_d11 = []
    nulls_ratio = []
    nulls_diff = []
    for iter_i in range(n_perm):
        perm = list(range(1, 115))
        rng.shuffle(perm)
        new_pos = [0] * 115
        for idx, sid in enumerate(perm):
            new_pos[sid] = idx + 1
        means = compute_bucket_from_perm(new_pos)
        rho, _ = spearmanr(midpoints, means)
        d1 = means[0]
        d11 = means[-1]
        ratio = d1 / d11 if d11 != 0 else float('inf')
        diff = d1 - d11
        nulls_rho.append(rho)
        nulls_d1.append(d1)
        nulls_d11.append(d11)
        nulls_ratio.append(ratio)
        nulls_diff.append(diff)
    return nulls_rho, nulls_d1, nulls_d11, nulls_ratio, nulls_diff


print(f"\n[perm A] {N_PERM} perms for sub-test A (ρ), seed+0...", file=sys.stderr)
nulls_A_rho, _, _, _, _ = run_null(0, N_PERM)
print(f"[perm B] {N_PERM} perms for sub-test B (d=1 mean), seed+1...",
      file=sys.stderr)
_, nulls_B_d1, _, _, _ = run_null(1, N_PERM)
print(f"[perm C] {N_PERM} perms for sub-test C (ratio), seed+2...",
      file=sys.stderr)
_, _, _, nulls_C_ratio, nulls_C_diff = run_null(2, N_PERM)


# ---- Compute p-values ----
def empirical_p_one_sided(nulls, observed, direction='lower_tail_ok'):
    """direction='lower' for ρ (want obs LOW); 'upper' for d1/ratio/diff (want obs HIGH)."""
    nulls_sorted = sorted(nulls)
    if direction == 'lower':
        return sum(1 for v in nulls_sorted if v <= observed) / len(nulls_sorted)
    else:  # upper
        return sum(1 for v in nulls_sorted if v >= observed) / len(nulls_sorted)


# Sub-test A: ρ < 0 (one-sided lower)
p_A = empirical_p_one_sided(nulls_A_rho, obs_primary['obs_rho_A'],
                              direction='lower')
A_pass = (obs_primary['obs_rho_A'] < 0) and (p_A < ALPHA_BON)
A_reverse = (obs_primary['obs_rho_A'] > 0) and (
    (1 - empirical_p_one_sided(nulls_A_rho, obs_primary['obs_rho_A'],
                                  direction='lower')) < ALPHA_BON)

# Sub-test B: d=1 mean > null (one-sided upper)
p_B = empirical_p_one_sided(nulls_B_d1, obs_primary['obs_d1_mean_B'],
                              direction='upper')
B_pass = p_B < ALPHA_BON

# Sub-test C primary (ratio): upper
p_C_ratio = empirical_p_one_sided(nulls_C_ratio, obs_primary['obs_ratio_C'],
                                    direction='upper')
C_pass = p_C_ratio < ALPHA_BON
C_reverse = (obs_primary['obs_ratio_C'] < 1.0) and (
    empirical_p_one_sided(nulls_C_ratio, obs_primary['obs_ratio_C'],
                           direction='lower') < ALPHA_BON)

# Sub-test C secondary (diff): upper
p_C_diff = empirical_p_one_sided(nulls_C_diff,
                                  obs_primary['obs_diff_C_secondary'],
                                  direction='upper')
C_diff_would_pass = p_C_diff < ALPHA_BON

# AMBIGUOUS-RATIO-NOISE-LIMIT: C primary fails but secondary would pass
C_ambiguous = (not C_pass) and C_diff_would_pass

print(f"\n=== SUB-TEST A (macro) ===", file=sys.stderr)
print(f"  obs ρ = {obs_primary['obs_rho_A']:+.4f}, "
      f"null mean = {statistics.mean(nulls_A_rho):+.4f}, "
      f"p = {p_A:.6f}", file=sys.stderr)
print(f"  PASS: {A_pass} (threshold α_bon={ALPHA_BON})", file=sys.stderr)

print(f"\n=== SUB-TEST B (local d=1) ===", file=sys.stderr)
print(f"  obs d=1 mean = {obs_primary['obs_d1_mean_B']:+.4f}, "
      f"null mean = {statistics.mean(nulls_B_d1):+.4f}, "
      f"p = {p_B:.6f}", file=sys.stderr)
print(f"  PASS: {B_pass}", file=sys.stderr)

print(f"\n=== SUB-TEST C (regime-cut ratio) ===", file=sys.stderr)
print(f"  obs ratio = {obs_primary['obs_ratio_C']:+.4f}, "
      f"null mean = {statistics.mean(nulls_C_ratio):+.4f}, "
      f"p = {p_C_ratio:.6f}", file=sys.stderr)
print(f"  PRIMARY PASS: {C_pass}", file=sys.stderr)
print(f"  obs diff (secondary) = {obs_primary['obs_diff_C_secondary']:+.4f}, "
      f"p_diff = {p_C_diff:.6f}, diff_would_pass = {C_diff_would_pass}",
      file=sys.stderr)
print(f"  AMBIGUOUS-RATIO-NOISE-LIMIT: {C_ambiguous}", file=sys.stderr)


# ---- 6-cell verdict routing ----
def route_verdict(A_pass, B_pass, C_pass, A_reverse, C_reverse, C_ambiguous):
    if A_reverse or C_reverse:
        return 'REVERSE — canonical distance has INVERSE munāsaba gradient'
    if A_pass and B_pass and C_pass:
        return 'STRONG PASS — both regimes survive, full al-Zarkashī thesis confirmed'
    if A_pass and B_pass and not C_pass:
        return ('PASS-FLAT — both regimes survive but no sharper local '
                'concentration (sub-test C does not fire)')
    if (not A_pass) and B_pass and C_pass:
        return ('PASS-LOCAL-ONLY — local-pairwise confirmed, macro refuted; '
                'regime-cut empirically validated; matches H-META-1 prior')
    if A_pass and (not B_pass) and (not C_pass):
        return ('PASS-MACRO-ONLY — surprise, contradicts H-META-1 prior; '
                'escalate to skeptical-auditor for H-META-1 self-audit')
    if (not A_pass) and (not B_pass):
        return ('NULL — al-Zarkashī munāsabāt al-suwar refuted at both scales; '
                'macro-prior reinforced')
    if C_ambiguous and (not C_pass):
        suffix = f' [AMBIGUOUS-RATIO-NOISE-LIMIT: diff passes but ratio does not]'
        base = 'PARTIAL'
        if A_pass and B_pass:
            base = 'PARTIAL-FLAT-with-diagnostic-flag'
        elif (not A_pass) and B_pass:
            base = 'PARTIAL-LOCAL-ONLY-ambiguous-regime-cut'
        elif A_pass and (not B_pass):
            base = 'PARTIAL-MACRO-ONLY-ambiguous-regime-cut'
        else:
            base = 'NULL-with-diff-flag'
        return base + suffix
    return (f'UNUSUAL — A={A_pass}, B={B_pass}, C={C_pass}, '
            f'reverse_A={A_reverse}, reverse_C={C_reverse}; inspect manually')


final_verdict = route_verdict(A_pass, B_pass, C_pass, A_reverse, C_reverse,
                                C_ambiguous)
print(f"\n=== FINAL VERDICT ===", file=sys.stderr)
print(f"  {final_verdict}", file=sys.stderr)


# ---- Muqaṭṭaʿāt-confound flag check ----
# Recompute A/B/C under muqaṭṭaʿāt-exclusion. If any sub-test flips,
# set a CONFOUND FLAG.
# For the flag diagnostic we use the SAME null distributions (since they
# were computed on the full pair-score matrix) — this is an approximation
# but honest given the pre-reg says the flag is diagnostic not verdict.
# More precisely, we recompute observations only and re-test against the
# same null.

p_A_flag = empirical_p_one_sided(nulls_A_rho, obs_muqflag['obs_rho_A'],
                                   direction='lower')
A_pass_flag = (obs_muqflag['obs_rho_A'] < 0) and (p_A_flag < ALPHA_BON)

p_B_flag = empirical_p_one_sided(nulls_B_d1, obs_muqflag['obs_d1_mean_B'],
                                   direction='upper')
B_pass_flag = p_B_flag < ALPHA_BON

p_C_flag = empirical_p_one_sided(nulls_C_ratio, obs_muqflag['obs_ratio_C'],
                                   direction='upper')
C_pass_flag = p_C_flag < ALPHA_BON

muq_flag_A = A_pass != A_pass_flag
muq_flag_B = B_pass != B_pass_flag
muq_flag_C = C_pass != C_pass_flag
muq_flag_any = muq_flag_A or muq_flag_B or muq_flag_C

print(f"\n=== MUQATTAAT-CONFOUND FLAG ===", file=sys.stderr)
print(f"  A: primary={A_pass}, flag={A_pass_flag} (p={p_A_flag:.6f}), "
      f"flipped={muq_flag_A}", file=sys.stderr)
print(f"  B: primary={B_pass}, flag={B_pass_flag} (p={p_B_flag:.6f}), "
      f"flipped={muq_flag_B}", file=sys.stderr)
print(f"  C: primary={C_pass}, flag={C_pass_flag} (p={p_C_flag:.6f}), "
      f"flipped={muq_flag_C}", file=sys.stderr)
print(f"  any-flag: {muq_flag_any}", file=sys.stderr)

if muq_flag_any:
    final_verdict = final_verdict + ' [MUQATTAAT-CONFOUND-FLAG]'
    print(f"  final verdict (with flag): {final_verdict}", file=sys.stderr)


# ---- Write JSON output ----
out = {
    'finding_id': 'h-classic-44',
    'pre_reg': 'findings/phase-b-hypotheses/h-classic-44-prereg.md',
    'pre_reg_compliance': 'PRE-REG-STANDARD-04 + STANDARD-05',
    'rules_tuple': '(no-tashkeel, root-level via QAC, hafs-kufan, mashriqi)',
    'seed': SEED,
    'n_perm': N_PERM,
    'bonferroni_k_outer': 6,
    'bonferroni_family_outer': 'h-classic-44-49',
    'bonferroni_k_inner': 3,
    'bonferroni_family_inner': 'h-classic-44',
    'alpha_bon': ALPHA_BON,
    'parent_dispatch': '2026-04-14-wave-1-3-meta-analyst',
    'regime_declaration': 'macro-architectural-primary-with-local-pairwise-stratification',
    'h_meta_1_prior': 'macro-regime-refuted-z-minus-2.51-local-pairwise-confirmed-z-plus-10.06',
    'transitive_prior_status': 'CONFIRMED-by-meta-analyst-2026-04-14-regime-level',
    'z_prior_source': 'task-21-T-002-direct-test',
    'sided_test': 'one-sided',
    'munasaba_score_composition': {
        'jaccard_weight': 0.5,
        'gzip_delta_resid_weight': 0.5,
        'gzip_residualization': 'OLS delta_norm ~ log(|A|*|B|)',
        'residualization_slope': slope,
        'residualization_intercept': intercept,
    },
    'buckets': [{'lo': b[0], 'hi': b[1], 'midpoint': b[2]} for b in BUCKETS],
    'pre_pilot_disclosure': {
        'pre_pilot_location': 'scratch/h_classic_44_pre_pilot/h-classic-44-pre-pilot-single-test.json',
        'pre_pilot_verdict_under_old_spec': 'PARTIAL-MUQATTAAT-DRIVEN',
        'pre_pilot_primary_rho': -1.0000,
        'pre_pilot_primary_p': 0.0062,
        'note': ('Single-test version run at α=0.0083 before discovering '
                 'task #95 hierarchical-Bonferroni 3-sub-test spec. '
                 'NOT used as verdict. This run supersedes.')
    },
    'sub_test_A': {
        'name': 'macro-architectural distance-decay Spearman ρ',
        'observed_bucket_means': obs_primary['bucket_means'],
        'observed_bucket_counts': obs_primary['bucket_counts'],
        'observed_rho': obs_primary['obs_rho_A'],
        'null_mean': statistics.mean(nulls_A_rho),
        'null_sd': statistics.stdev(nulls_A_rho),
        'empirical_p_one_sided': p_A,
        'passes': A_pass,
        'reverse': A_reverse,
    },
    'sub_test_B': {
        'name': 'local-pairwise d=1 seam coherence',
        'observed_d1_mean': obs_primary['obs_d1_mean_B'],
        'null_mean': statistics.mean(nulls_B_d1),
        'null_sd': statistics.stdev(nulls_B_d1),
        'empirical_p_one_sided': p_B,
        'passes': B_pass,
    },
    'sub_test_C': {
        'name': 'regime-discrimination ratio + secondary difference',
        'observed_d1_mean': obs_primary['obs_d1_mean_B'],
        'observed_d11_mean': obs_primary['obs_d11_mean'],
        'primary_ratio': {
            'observed': obs_primary['obs_ratio_C'],
            'null_mean': statistics.mean(nulls_C_ratio),
            'null_sd': statistics.stdev(nulls_C_ratio),
            'empirical_p_one_sided': p_C_ratio,
            'passes': C_pass,
            'reverse': C_reverse,
        },
        'secondary_difference': {
            'observed': obs_primary['obs_diff_C_secondary'],
            'null_mean': statistics.mean(nulls_C_diff),
            'null_sd': statistics.stdev(nulls_C_diff),
            'empirical_p_one_sided': p_C_diff,
            'would_pass_if_primary': C_diff_would_pass,
            'note': ('Diagnostic only; NOT verdict-entering per pre-reg '
                     'sub-test C secondary lock. Reported to flag '
                     'AMBIGUOUS-RATIO-NOISE-LIMIT cell if applicable.')
        },
        'ambiguous_ratio_noise_limit': C_ambiguous,
    },
    'muqattaat_confound_flag': {
        'n_excluded_pairs': len(muq_exclude),
        'without_muqattaat_obs': obs_muqflag,
        'without_muqattaat_A_pass': A_pass_flag,
        'without_muqattaat_B_pass': B_pass_flag,
        'without_muqattaat_C_pass': C_pass_flag,
        'any_flip': muq_flag_any,
        'note': ('If any flip, final_verdict carries MUQATTAAT-CONFOUND-FLAG '
                 'suffix. Flag is diagnostic, not verdict-overriding.')
    },
    'final_verdict': final_verdict,
    'no_fork_protections_honored': [
        'munāsaba score LOCKED 0.5*J_std + 0.5*Δ_std (length-residualized)',
        'distance buckets LOCKED {1, 2, 3-5, 6-10, 11+}',
        'sub-test A statistic LOCKED Spearman ρ across 5 bucket means',
        'sub-test B statistic LOCKED mean(d=1) vs permutation null',
        'sub-test C primary LOCKED ratio d1/d11, secondary diagnostic diff',
        f'seeds LOCKED {SEED}/{SEED+1}/{SEED+2}, {N_PERM} perms each',
        f'α_bon = {ALPHA_BON} (hierarchical: outer k=6, inner k=3)',
        f'muqaṭṭaʿāt set LOCKED {sorted(MUQATTAAT)}',
        'QAC v0.4 STEM-only root extraction LOCKED',
        '6-cell verdict matrix LOCKED per task #95 spec',
        'muqaṭṭaʿāt-exclusion is DIAGNOSTIC FLAG not verdict gate',
    ],
    'data_reuse_disclosed': (
        'Reuses QAC loader from h_classic_47_biqai_seam.py. Reuses '
        'pair-score computation method from pre-pilot run '
        '(scratch/h_classic_44_pre_pilot/). Reuses QAC morphology file '
        'and Quran JSON. Cross-refs scholar-convergence-tracker.md §2/3/5 '
        'per task #95 spec.'
    ),
}

out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-classic-44.json'
out_path.write_text(json.dumps(out, indent=2, default=str))
print(f"\n[output] saved: {out_path}", file=sys.stderr)
