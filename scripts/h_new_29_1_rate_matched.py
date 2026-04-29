#!/usr/bin/env python3
"""H-NEW-29.1 — rate-matched per-root Poisson null (independent follow-up to H-NEW-29).

Pre-reg (task #81, locked AMEND-20 retained body):
  1. For each of the 833 roots with n_R ≥ 5, simulate n_R uniform-random events
     over N = 49,968 ROOT tokens (the H-NEW-29 STEM sequence). 1000 sims/root.
  2. Per-root Δ_r = CV_observed(r) − E[CV_rate_matched(r)]
  3. n_R-weighted mean Δ; 1000-bootstrap 99% CI for the weighted mean.
  4. Per-frequency-bin Δ (rare/mid/frequent/super-frequent).

Three-way verdict (locked):
  - Δ < 0, 99% CI ABOVE 0 excluded   → Quran more REGULAR than rate-matched Poisson.
  - Δ ≈ 0, 99% CI crosses 0          → primary super-Poisson observation was finite-corpus
                                         artifact; H-NEW-29 MIXED stands; no upgrade.
  - Δ > 0, 99% CI BELOW 0 excluded   → genuine excess clumping beyond rate-matched Poisson.

Bonferroni k=1 for aggregate; per-bin exploratory without correction.

Data reuse: positional index from H-NEW-29's STEM-token loader is rebuilt; only the
rate-matched-null layer is new. Existing observed CV values are recomputed deterministically
under seed 20260414 (NOT 20260413 of the parent — this is an independent follow-up with
its own seed per the pre-reg).

Compute: < 1 second for 833 roots × 1000 sims (each sim is ~n_R coin-flips).
"""
import json, math, random, re, sys, statistics
from collections import defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260414
random.seed(SEED)

# ---- Load QAC morphology (same as h_new_29) ----
print("[H-NEW-29.1] Loading QAC morphology...", file=sys.stderr)
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')

token_seq = []
with open(ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt', encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
            continue
        parts = line.rstrip('\n').split('\t')
        if len(parts) < 4:
            continue
        m = LOC_RE.match(parts[0])
        if not m:
            continue
        feat = parts[3]
        if 'STEM' not in feat:
            continue
        rm = ROOT_RE.search(feat)
        if rm:
            token_seq.append(rm.group(1))
        else:
            token_seq.append(None)

root_tokens = [r for r in token_seq if r is not None]
N_ROOT_SEQ = len(root_tokens)
print(f"  total STEM tokens (with-or-without root): {len(token_seq)}", file=sys.stderr)
print(f"  root-bearing tokens N = {N_ROOT_SEQ}", file=sys.stderr)

# Build root positional index
positions = defaultdict(list)
for i, r in enumerate(root_tokens):
    positions[r].append(i)

# ---- CV per root (observed) ----
def cv(ds):
    if len(ds) < 2:
        return None
    m = statistics.mean(ds)
    if m == 0:
        return None
    s = statistics.stdev(ds)
    return s / m

def compute_root_cvs(positions_map, min_n=5):
    res = {}
    for r, poss in positions_map.items():
        if len(poss) < min_n:
            continue
        ds = [poss[i+1] - poss[i] for i in range(len(poss) - 1)]
        c = cv(ds)
        if c is None:
            continue
        res[r] = (len(poss), c)
    return res

observed_cvs = compute_root_cvs(positions, min_n=5)
print(f"  roots with n ≥ 5: {len(observed_cvs)}", file=sys.stderr)

# ---- Rate-matched Poisson null per root ----
# For each root with n_R occurrences, simulate n_R uniform-random integer positions
# in [0, N_ROOT_SEQ - 1] without replacement (so n_R distinct positions), compute CV
# from inter-arrival differences. Repeat 1000 times. E[CV_rate_matched(r)] = mean.
# This is the FAITHFUL Poisson-process null at finite N: not Poisson(λ) inter-arrivals,
# but the empirical inter-arrival distribution induced by uniform placement of n_R
# events over N positions, which automatically respects the finite-corpus bound.

print("[H-NEW-29.1] Running rate-matched Poisson null (1000 sims/root)...", file=sys.stderr)
N_SIMS = 1000

def rate_matched_cv_dist(n_R, N, n_sims=N_SIMS):
    """Return list of CV values for n_sims uniform placements of n_R events in [0,N)."""
    cvs = []
    for _ in range(n_sims):
        positions_sim = sorted(random.sample(range(N), n_R))
        ds_sim = [positions_sim[i+1] - positions_sim[i] for i in range(n_R - 1)]
        c = cv(ds_sim)
        if c is not None:
            cvs.append(c)
    return cvs

# Compute per-root expected CV under rate-matched null
expected_cvs = {}
delta_per_root = {}
n_processed = 0
for r, (n_R, c_obs) in observed_cvs.items():
    null_dist = rate_matched_cv_dist(n_R, N_ROOT_SEQ, n_sims=N_SIMS)
    if not null_dist:
        continue
    e_cv = statistics.mean(null_dist)
    expected_cvs[r] = (n_R, e_cv)
    delta_per_root[r] = (n_R, c_obs - e_cv)
    n_processed += 1
    if n_processed % 100 == 0:
        print(f"  processed {n_processed}/{len(observed_cvs)} roots", file=sys.stderr)

print(f"  total processed: {n_processed}", file=sys.stderr)

# ---- Aggregate: n_R-weighted mean Δ ----
def weighted_mean_delta(delta_dict):
    num = 0.0
    den = 0.0
    for r, (n, d) in delta_dict.items():
        num += n * d
        den += n
    return num / den if den > 0 else 0.0

w_delta = weighted_mean_delta(delta_per_root)
print(f"\n[H-NEW-29.1] AGGREGATE n_R-weighted Δ = {w_delta:+.4f}", file=sys.stderr)

# ---- Bootstrap 99% CI for weighted-mean Δ ----
print("[H-NEW-29.1] Bootstrapping 99% CI (1000 boots)...", file=sys.stderr)
def bootstrap_w_delta(delta_dict, n_boot=1000):
    items = list(delta_dict.items())
    n = len(items)
    boots = []
    for _ in range(n_boot):
        sample = [items[random.randrange(n)] for _ in range(n)]
        num = 0.0
        den = 0.0
        for r, (count, d) in sample:
            num += count * d
            den += count
        boots.append(num / den if den > 0 else 0)
    boots.sort()
    lo_99 = boots[int(0.005 * n_boot)]
    hi_99 = boots[int(0.995 * n_boot)]
    return lo_99, hi_99, boots

lo_99, hi_99, _ = bootstrap_w_delta(delta_per_root, n_boot=1000)
print(f"  99% CI for w_Δ: [{lo_99:+.4f}, {hi_99:+.4f}]", file=sys.stderr)

# ---- Three-way verdict ----
if hi_99 < 0:
    verdict = 'QURAN-MORE-REGULAR'
    interpretation = 'Quran is MORE REGULAR than rate-matched Poisson; H-NEW-29 sub-(b) PASS strengthened; absolute claim gets second-chance PASS under faithful null'
elif lo_99 > 0:
    verdict = 'GENUINE-EXCESS-CLUMPING'
    interpretation = 'Quran exhibits GENUINE excess clumping beyond rate-matched Poisson; absolute al-Jāḥiẓ refutation strengthened'
else:
    verdict = 'CI-CROSSES-ZERO-FINITE-CORPUS-ARTIFACT'
    interpretation = 'CI crosses 0; primary super-Poisson observation was finite-corpus artifact; H-NEW-29 MIXED stands; no upgrade, no demotion'

print(f"\n[H-NEW-29.1] VERDICT: {verdict}", file=sys.stderr)
print(f"  interpretation: {interpretation}", file=sys.stderr)

# ---- Per-frequency-bin Δ (exploratory, no correction) ----
print("\n[H-NEW-29.1] Per-frequency-bin Δ (exploratory, NOT in Bonferroni)...", file=sys.stderr)
BINS = [(5, 10, 'rare'), (10, 50, 'mid'), (50, 200, 'frequent'), (200, 10**6, 'super_frequent')]

bin_deltas = defaultdict(list)
bin_counts = defaultdict(list)
for r, (n_R, d) in delta_per_root.items():
    for lo, hi, name in BINS:
        if lo <= n_R < hi:
            bin_deltas[name].append(d)
            bin_counts[name].append(n_R)
            break

bin_summary = {}
for _, _, name in BINS:
    if name not in bin_deltas or not bin_deltas[name]:
        bin_summary[name] = None
        continue
    ds_ = bin_deltas[name]
    ns_ = bin_counts[name]
    w_d_bin = sum(n*d for n, d in zip(ns_, ds_)) / sum(ns_)
    med_d = statistics.median(ds_)
    bin_summary[name] = {
        'n_roots': len(ds_),
        'total_count': sum(ns_),
        'weighted_mean_delta': w_d_bin,
        'median_delta': med_d,
    }
    print(f"  {name}: n_roots={len(ds_)}, Σn={sum(ns_)}, w_Δ={w_d_bin:+.4f}, median_Δ={med_d:+.4f}", file=sys.stderr)

# ---- Diagnostic: average expected vs observed ----
all_obs = [c for _, (_, c) in observed_cvs.items()]
all_exp = [e for _, (_, e) in expected_cvs.items()]
print(f"\n[diagnostic] mean(observed CV) = {statistics.mean(all_obs):.4f}", file=sys.stderr)
print(f"[diagnostic] mean(expected CV) = {statistics.mean(all_exp):.4f}", file=sys.stderr)
print(f"[diagnostic] mean Δ            = {statistics.mean(c - e for c, e in zip(all_obs, all_exp)):+.4f}", file=sys.stderr)

# Also report the n_R-weighted observed and expected for direct contrast with H-NEW-29's wmcv = 1.370
def w_mean_pair(d):
    num = sum(n*v for _, (n, v) in d.items())
    den = sum(n for _, (n, _) in d.items())
    return num / den if den > 0 else 0
w_obs_cv = w_mean_pair(observed_cvs)
w_exp_cv = w_mean_pair(expected_cvs)
print(f"[diagnostic] weighted-mean observed CV = {w_obs_cv:.4f}", file=sys.stderr)
print(f"[diagnostic] weighted-mean expected CV = {w_exp_cv:.4f}", file=sys.stderr)
print(f"[diagnostic] weighted Δ                = {w_obs_cv - w_exp_cv:+.4f}", file=sys.stderr)

# ---- Output: append to existing h-new-29.json under top-level key 'h_new_29_1_rate_matched' ----
out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-new-29.json'
existing = json.loads(out_path.read_text())

existing['h_new_29_1_rate_matched'] = {
    'pre_reg_reference': 'task #81 (PRE-REG-STANDARD-04 compliant)',
    'seed': SEED,
    'rules_tuple': '(no-tashkeel, QAC roots, mushaf order, STEM sequence, n_R ≥ 5)',
    'description': 'Rate-matched per-root Poisson null. For each root with n_R≥5, '
                   'simulate n_R uniform placements over N root-bearing tokens, 1000 sims/root, '
                   'compute Δ_r = CV_observed(r) − E[CV_rate_matched(r)], then n_R-weighted aggregate.',
    'data_reuse_disclosed': 'Reuses positional index from H-NEW-29; only rate-matched null layer is new. '
                            'H-NEW-29 MIXED primary verdict stands verbatim regardless of this outcome.',
    'n_root_tokens_N': N_ROOT_SEQ,
    'n_roots_processed': n_processed,
    'n_sims_per_root': N_SIMS,
    'weighted_mean_delta': w_delta,
    'bootstrap_99_ci': {
        'lo': lo_99,
        'hi': hi_99,
    },
    'verdict': verdict,
    'interpretation': interpretation,
    'diagnostic_weighted_observed_cv': w_obs_cv,
    'diagnostic_weighted_expected_cv': w_exp_cv,
    'diagnostic_simple_mean_observed_cv': statistics.mean(all_obs),
    'diagnostic_simple_mean_expected_cv': statistics.mean(all_exp),
    'per_frequency_bin': bin_summary,
    'bonferroni_k_aggregate': 1,
    'bonferroni_note': 'Per-bin Δ is exploratory and NOT Bonferroni-corrected. Aggregate-only PASS/FAIL is the primary test.',
}

out_path.write_text(json.dumps(existing, indent=2, default=str, ensure_ascii=False))
print(f"\n[saved] appended h_new_29_1_rate_matched section to {out_path}", file=sys.stderr)
