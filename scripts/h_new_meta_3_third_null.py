#!/usr/bin/env python3
"""H-NEW-META-3 — Third-Null Specification for Markov-Surprise Family (task #118 execution).

Pre-registered adjudication of three candidate nulls designed after H-META-2 (task #43)
BOTH_DISQUALIFIED verdict on Null-A (label-permutation) and Null-B (Markov-character-
permutation). Pre-reg file: findings/phase-c-structures/h-new-meta-3-prereg.md
(locked 2026-04-14 before null design, per PRE-REG-STANDARD-04).

===============================================================================
PRE-REGISTRATION ADDENDUM (pre-committed 2026-04-14 per audit-030, BEFORE first run)
===============================================================================

ADDENDUM NOTE 1 — Length-decile computation basis (pre-committed 2026-04-14 per audit-030 Note 1):

    "Length-deciles for Null-C stratification are computed on the pooled Quran
    corpus (full 6,236-verse Quran), NOT per-surah independently and NOT pooled
    across Quran + Mutanabbī + Jāḥiẓ. No post-hoc decile-basis change permitted
    without formal amendment in TEAM-AMENDMENTS-LOG.md."

Implementation consequence: decile breakpoints are derived from Quran verse-
length quantiles once, at script start, and applied uniformly to the Mutanabbī
and Jāḥiẓ corpora (which is where the H-META-3 calibration test actually runs).
Since neither baseline corpus is the Quran, this is a cross-corpus application
of Quran-derived breakpoints — the decile IS still a function of Quran-text, and
the stratification preserves the pre-reg discipline of using ONE frozen length-
quantile map throughout.

ADDENDUM NOTE 2 — Null-E Poisson goodness-of-fit threshold (pre-committed 2026-04-14 per audit-030 Note 2):

    "Null-E's goodness-of-fit diagnostic is operationalized as Poisson χ² test
    p-value > 0.05 for rate-model fit vs observed residual-surprise histogram.
    Bin count k=10 (Sturges-rule ceiling for n~6k observations). χ² statistic
    computed with df = k − p_params − 1 where p_params = number of fitted
    parameters in the rate model. Threshold: p > 0.05 → Null-E passes GoF;
    p ≤ 0.05 → Null-E DISQUALIFIED on GoF grounds, reported in output JSON as
    `null_e_gof_disqualified: true`. Downstream: if Null-E GoF-disqualified,
    Null-C and Null-D still run to completion; Bonferroni k=3 stays locked (NOT
    reduced to k=2 post-hoc)."

===============================================================================

THREE CANDIDATE NULLS (specs locked 2026-04-14):

    NULL-C: Stratified matched-pair permutation.
        For each verse v, stratum = (surah_id OR corpus-segment-id,
                                     length-decile ∈ 1..10,
                                     rhyme-cluster-id ∈ {break, conform}).
        Permute break/conform labels ONLY within stratum.
        Markov model frozen (trained once on observed).
        Test statistic = residual-mean-difference between classes.
        B = 1000 permutations per calibration run.
        Addresses Null-A's global-exchangeability failure: label swaps now
        respect the conditional joint marginal (surah × length × rhyme).

    NULL-D: Block-bootstrap on surah-segments.
        Block size 8 consecutive verses (pre-committed, not tuned).
        Per bootstrap draw: resample blocks with replacement within same surah/
        segment; Markov re-trained per draw; test statistic recomputed.
        B = 1000 bootstrap draws per calibration run.
        Addresses Null-B's character-level artifacts: preserves word-internal
        and verse-final joint structure by never touching the text itself,
        only resampling whole blocks of complete verses.

    NULL-E: Rate-matched parametric Poisson.
        Fit Poisson rate model for residual-Markov-surprise conditional on
        (length-decile, rhyme-cluster, surah_id or corpus-segment-id) under
        H0: class has no effect. Sample synthetic corpora from the fitted
        rate model, compute test statistic on each.
        B = 1000 parametric draws per calibration run.
        Goodness-of-fit diagnostic: Poisson χ² (addendum Note 2). If GoF fails,
        Null-E disqualifies pre-calibration; Null-C/D still run; Bonferroni
        k=3 stays locked.

CALIBRATION GATES (two-gate standard, same as H-META-2):

    Gate 1 — Type-I independence calibration:
        On each of Mutanabbī-Dīwān and Jāḥiẓ-Ḥayawān, B=1000 random rhyme-sets
        (5 of 28 letters). For each draw, compute |z| vs null; record fraction
        with |z| > 2.576 (nominal α=0.01 two-sided).
        Gate 1 PASS: rate ∈ [0.005, 0.02] on BOTH corpora.

    Gate 2 — Sign-and-magnitude calibration on planted signals:
        Plant break-class surprise boost at σ ∈ {0.5, 1.0, 2.0} on both corpora.
        6 cells total per candidate.
        PASS-strict: sign correct ALL 6 + |recovered − planted| < 2σ ALL 6.
        PASS-relaxed: sign correct ALL 6 + |recovered − planted| < 3σ ALL 6.
        FAIL: any sign-flip OR any magnitude deviation > 3σ.

JOINT VERDICT TABLE (pre-committed):
    Gate1 PASS + Gate2 PASS-strict   → CALIBRATED
    Gate1 PASS + Gate2 PASS-relaxed  → PROVISIONALLY CALIBRATED
    Gate1 PASS + Gate2 FAIL          → DISQUALIFIED (power mis-calibrated)
    Gate1 FAIL + *                   → DISQUALIFIED (Type-I mis-calibrated)

WINNER-SELECTION (if 2+ PASS):
    Tie-breaker = arithmetic mean absolute deviation |recovered − planted|
    across all 6 power cells. Null-C preferred on ties (most conservative).

FAILURE PROTOCOL (if all three DISQUALIFIED):
    Verdict = META-NULL-REINFORCED (verbatim, no soft-naming).
    H-NEW-1 / H-NEW-1-v2 z-magnitudes stay caveated under §3d STAGED.
    Separate finding file published at:
    findings/phase-c-structures/markov-surprise-family-uncalibratable.md
    H-NEW-META-4 follow-up task filed (conformal / Bayesian PPC / eulerian-shuffle).

EXECUTION PARAMETERS:
    Seed: 20260414 (fresh from H-META-2's 20260413)
    Bonferroni: k=3, α_bon=0.0167
    Rules tuple: (no-tashkeel, orthographic-token, hafs-kufan, mashriqi)
    Alphabet: 28 Arabic letters
    Markov order: 2 (matches H-META-2 and H-NEW-1-v2)
    Expected runtime: ~40-60 minutes single-threaded

OUTPUTS:
    JSON: findings/phase-c-structures/csv/h-new-meta-3.json
    Narrative: findings/phase-c-structures/h-new-meta-3-third-null.md (written separately)

Run: python3 scripts/h_new_meta_3_third_null.py
"""
import json
import math
import os
import random
import re
import statistics
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260414  # fresh from H-META-2's 20260413
random.seed(SEED)

# Pilot mode (env var H_META_3_PILOT=1): writes to scratch/, uses reduced
# B and N_inner, output paths divert from pre-reg paths. Pilot is pipeline
# shake-down ONLY — pilot results NEVER enter the verdict JSON.
PILOT_MODE = os.environ.get('H_META_3_PILOT', '0') == '1'

OUTPUT_JSON = (
    ROOT / 'scratch/h_new_meta_3_pilot/h-new-meta-3-pilot.json'
    if PILOT_MODE else
    ROOT / 'findings/phase-c-structures/csv/h-new-meta-3.json'
)
CHECKPOINT_DIR = (
    ROOT / 'scratch/h_new_meta_3_pilot'
    if PILOT_MODE else
    ROOT / 'findings/phase-c-structures/csv'
)


def log(msg):
    """stderr log with forced flush — prevents silent truncation on kill."""
    print(msg, file=sys.stderr, flush=True)


def checkpoint_path(stage, null_name, corpus):
    return CHECKPOINT_DIR / f'h-new-meta-3-checkpoint-{stage}-{null_name}-{corpus}.json'


def save_checkpoint(stage, null_name, corpus, payload):
    CHECKPOINT_DIR.mkdir(parents=True, exist_ok=True)
    p = checkpoint_path(stage, null_name, corpus)
    p.write_text(json.dumps(payload, indent=2, ensure_ascii=False, default=str))
    log(f"    [checkpoint] wrote {p.name}")


def load_checkpoint(stage, null_name, corpus):
    p = checkpoint_path(stage, null_name, corpus)
    if p.exists():
        try:
            return json.loads(p.read_text())
        except Exception:
            return None
    return None

# ===== Constants locked pre-execution =====
ARAB_LETTERS = list('ابتثجحخدذرزسشصضطظعغفقكلمنهوي')  # 28-letter Arabic alphabet
AR_RE = re.compile(r'[\u0621-\u064A]')
DIAC_RE = re.compile(r'[\u064B-\u065F\u0670\u06D6-\u06ED]')
ORDER = 2          # Markov order (matches H-META-2)
V_ALPHABET = 50    # smoothing vocabulary upper bound

# Gate thresholds (pre-committed in pre-reg frontmatter)
CRIT_Z = 2.576                    # nominal α=0.01 two-sided
CAL_WINDOW = (0.005, 0.02)        # Gate 1 acceptance window
PLANTED_SIGMAS = [0.5, 1.0, 2.0]  # Gate 2 planted-signal levels
GATE2_STRICT_K = 2.0              # |recovered − planted| < k·σ
GATE2_RELAXED_K = 3.0
BONFERRONI_K = 3
ALPHA_BON = 0.05 / BONFERRONI_K   # 0.0167

# Addendum Note 2 threshold
POISSON_GOF_P_THRESHOLD = 0.05
POISSON_GOF_BINS = 10             # Sturges-rule ceiling for n~6k observations

# Compute budget — calibration draws per corpus.
# Team-lead ruling 2026-04-13 (Option A, supersedes earlier Option-B-adjacent
# message): execute pre-reg VERBATIM. Both outer Gate-1 B AND inner N_PERM
# are pre-reg locked at 1000. AMEND-31 was considered and explicitly REJECTED
# as pattern-a (forbidden compute-pressure-driven redesign). Overnight run
# is the only protocol-consistent path.
#
# Pilot mode (env var H_META_3_PILOT=1) writes to scratch/, uses reduced
# B and N_inner — pipeline shake-down only, NOT a verdict run.
if PILOT_MODE:
    B_GATE1 = 200
    N_PERM_INNER_C = 100
    N_PERM_INNER_D = 30
    N_PERM_INNER_E = 100
else:
    # Pre-reg VERBATIM — Option A locked 2026-04-13 by team-lead.
    B_GATE1 = 1000
    N_PERM_INNER_C = 1000
    N_PERM_INNER_D = 1000
    N_PERM_INNER_E = 1000


def clean(text):
    return ''.join(AR_RE.findall(DIAC_RE.sub('', text)))


# ===== Corpus loaders (same as H-META-2 for direct comparability) =====
def load_mutanabbi():
    lines = []
    path = ROOT / 'data/baseline-corpora/raw/mutanabbi-diwan.txt'
    for ln in path.read_text(encoding='utf-8').splitlines():
        c = clean(ln)
        if 10 <= len(c) <= 200:
            lines.append(c)
    return lines


def load_jahiz():
    path = ROOT / 'data/baseline-corpora/raw/jahiz-hayawan.txt'
    text = path.read_text(encoding='utf-8')
    parts = re.split(r'[.!?؟،؛:\n]+', text)
    lines = []
    for p in parts:
        c = clean(p)
        if 10 <= len(c) <= 200:
            lines.append(c)
    return lines


def load_quran_for_deciles():
    """Addendum Note 1: deciles computed on pooled Quran, full 6,236 verses."""
    q = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text())
    verses = []
    for surah in q:
        for v in surah.get('verses', []):
            c = clean(v.get('text', ''))
            if c:
                verses.append(len(c))
    return verses


def compute_length_decile_breakpoints(quran_lengths):
    """Decile breakpoints derived from Quran (addendum Note 1 pre-committed)."""
    xs = sorted(quran_lengths)
    n = len(xs)
    breaks = []
    for q in range(1, 10):  # 9 breakpoints → 10 bins
        idx = int(n * q / 10)
        if idx >= n:
            idx = n - 1
        breaks.append(xs[idx])
    return breaks


def assign_decile(length, breaks):
    """Return decile 0..9 (10 bins) given length and the 9 breakpoints."""
    d = 0
    for b in breaks:
        if length > b:
            d += 1
        else:
            break
    return min(d, 9)


# ===== Markov machinery (shared with H-META-2) =====
def build_markov(seqs, order=ORDER):
    model = defaultdict(Counter)
    for s in seqs:
        for i in range(len(s) - order):
            model[s[i:i+order]][s[i+order]] += 1
    return model


def surprise(model, context, char):
    counter = model.get(context, Counter())
    total = sum(counter.values())
    p = (counter[char] + 1) / (total + V_ALPHABET)
    return -math.log2(p)


def compute_per_verse_residuals(verses, rhyme_set, order=ORDER):
    """Returns list of (is_break, length_decile, residual) per eligible verse.
    Markov model trained on text[:-1] of all eligible verses, then residual
    for each verse computed as observed − class-uniform-baseline.
    """
    pre_terminal = [v[:-1] for v in verses if len(v) > order]
    model = build_markov(pre_terminal, order)
    out = []
    for v in verses:
        if len(v) < order + 1:
            continue
        ctx = v[-order-1:-1]
        term = v[-1]
        s_obs = surprise(model, ctx, term)
        is_break = term not in rhyme_set
        class_alpha = [c for c in ARAB_LETTERS if (c not in rhyme_set) == is_break]
        if not class_alpha:
            continue
        s_class = statistics.mean(surprise(model, ctx, c) for c in class_alpha)
        out.append((is_break, len(v), s_obs - s_class))
    return out, model


def observed_diff(per_verse):
    br = [r for is_b, _, r in per_verse if is_b]
    cf = [r for is_b, _, r in per_verse if not is_b]
    if not br or not cf:
        return None
    return statistics.mean(br) - statistics.mean(cf)


# ===== Stratification helpers =====
def build_strata(per_verse, length_breaks, segment_ids):
    """Return dict {(segment_id, length_decile, rhyme_cluster): [indices]}."""
    strata = defaultdict(list)
    for idx, ((is_break, length, _), seg) in enumerate(zip(per_verse, segment_ids)):
        decile = assign_decile(length, length_breaks)
        rhyme_cluster = 'break' if is_break else 'conform'
        strata[(seg, decile, rhyme_cluster)].append(idx)
    return strata


# ===== Null-C: Stratified matched-pair permutation =====
def null_C_stratified_perm(per_verse, segment_ids, length_breaks, n_perm, seed):
    """Permute break/conform labels WITHIN (segment × decile) strata ONLY.
    Note the stratum used for permutation is (segment × decile) — NOT including
    rhyme_cluster, because the rhyme_cluster IS the label we're permuting. The
    stratum defines the exchangeable pool within which the label can be shuffled;
    rhyme_cluster is the label itself.
    Preserves marginals of (segment, decile) exactly.
    """
    rng = random.Random(seed)
    obs_d = observed_diff(per_verse)
    if obs_d is None:
        return None

    # Group indices by (segment, decile) — rhyme labels are what we permute.
    groups = defaultdict(list)
    for idx, ((_, length, _), seg) in enumerate(zip(per_verse, segment_ids)):
        decile = assign_decile(length, length_breaks)
        groups[(seg, decile)].append(idx)

    residuals = [r for _, _, r in per_verse]
    orig_labels = [is_b for is_b, _, _ in per_verse]

    null_diffs = []
    for _ in range(n_perm):
        shuffled = orig_labels[:]
        for idxs in groups.values():
            if len(idxs) < 2:
                continue
            local_labels = [orig_labels[i] for i in idxs]
            rng.shuffle(local_labels)
            for i, lab in zip(idxs, local_labels):
                shuffled[i] = lab
        br = [residuals[i] for i in range(len(residuals)) if shuffled[i]]
        cf = [residuals[i] for i in range(len(residuals)) if not shuffled[i]]
        if not br or not cf:
            continue
        null_diffs.append(statistics.mean(br) - statistics.mean(cf))
    if len(null_diffs) < 10:
        return None
    nm = statistics.mean(null_diffs)
    ns = statistics.stdev(null_diffs) if len(null_diffs) > 1 else 0
    return {
        'null': 'C_stratified_perm',
        'obs_diff': obs_d,
        'null_mean': nm,
        'null_sd': ns,
        'z': (obs_d - nm) / ns if ns > 0 else 0,
        'n_null_draws': len(null_diffs),
    }


# ===== Null-D: Block-bootstrap =====
BLOCK_SIZE = 8  # pre-committed in pre-reg


def null_D_block_bootstrap(verses, segment_ids, rhyme_set, n_perm, seed):
    """Block-bootstrap at block size 8 within each segment.
    Each bootstrap draw: for each segment, sample len(segment)//BLOCK_SIZE blocks
    with replacement from that segment's block pool. Retrain Markov. Recompute
    residual-mean-diff.
    """
    rng = random.Random(seed + 1)
    per_verse_obs, _ = compute_per_verse_residuals(verses, rhyme_set)
    obs_d = observed_diff(per_verse_obs)
    if obs_d is None:
        return None

    # Group verses by segment
    by_seg = defaultdict(list)
    for v, seg in zip(verses, segment_ids):
        by_seg[seg].append(v)

    # Pre-compute block pool per segment
    block_pool = {}
    for seg, seg_verses in by_seg.items():
        blocks = []
        for i in range(0, len(seg_verses) - BLOCK_SIZE + 1, BLOCK_SIZE):
            blocks.append(seg_verses[i:i + BLOCK_SIZE])
        if not blocks and seg_verses:
            blocks.append(seg_verses[:])  # segment shorter than block
        block_pool[seg] = blocks

    null_diffs = []
    for _ in range(n_perm):
        resampled = []
        for seg, blocks in block_pool.items():
            if not blocks:
                continue
            n_needed = max(1, len(by_seg[seg]) // BLOCK_SIZE)
            for _ in range(n_needed):
                resampled.extend(rng.choice(blocks))
        if len(resampled) < 10:
            continue
        pv, _ = compute_per_verse_residuals(resampled, rhyme_set)
        d = observed_diff(pv)
        if d is not None:
            null_diffs.append(d)
    if len(null_diffs) < 10:
        return None
    nm = statistics.mean(null_diffs)
    ns = statistics.stdev(null_diffs) if len(null_diffs) > 1 else 0
    return {
        'null': 'D_block_bootstrap',
        'obs_diff': obs_d,
        'null_mean': nm,
        'null_sd': ns,
        'z': (obs_d - nm) / ns if ns > 0 else 0,
        'n_null_draws': len(null_diffs),
    }


# ===== Null-E: Rate-matched parametric Poisson + GoF =====
def poisson_cdf(k, lam):
    """Poisson CDF via incomplete gamma (closed-form summation). k integer, lam>0."""
    if lam <= 0:
        return 1.0 if k >= 0 else 0.0
    s = 0.0
    term = math.exp(-lam)
    s += term
    for i in range(1, int(k) + 1):
        term *= lam / i
        s += term
    return s


def chi_sq_sf(x, df):
    """Survival function for χ² (1 − CDF) via series / asymptotic approximation.
    Wilson-Hilferty normal approximation: transforms χ² to approximately N(0,1).
    """
    if df <= 0 or x <= 0:
        return 1.0
    h = 2.0 / (9.0 * df)
    z = ((x / df) ** (1.0 / 3.0) - (1 - h)) / math.sqrt(h)
    # Normal survival via erfc
    return 0.5 * math.erfc(z / math.sqrt(2))


def null_E_parametric_poisson_gof(per_verse, n_perm, seed):
    """Null-E: fit Poisson rate model; GoF; if GoF passes, sample synthetic corpora.
    Residual Markov-surprises are not integer-counts, so we discretize for χ² GoF:
    bin residual values into POISSON_GOF_BINS bins and apply χ² against fitted
    Poisson of bin-count.
    """
    rng = random.Random(seed + 2)
    obs_d = observed_diff(per_verse)
    if obs_d is None:
        return None, None

    residuals = [r for _, _, r in per_verse]
    n = len(residuals)
    if n < 20:
        return None, None

    # ---- GoF (addendum Note 2) ----
    k_bins = POISSON_GOF_BINS
    r_min, r_max = min(residuals), max(residuals)
    if r_min == r_max:
        return None, {'null_e_gof_disqualified': True, 'reason': 'degenerate_residuals'}
    bin_width = (r_max - r_min) / k_bins
    hist = [0] * k_bins
    for r in residuals:
        idx = min(int((r - r_min) / bin_width), k_bins - 1)
        hist[idx] += 1

    bin_mean = n / k_bins                       # fitted Poisson mean (1 param)
    p_params = 1
    chi_sq = 0.0
    for c in hist:
        if bin_mean > 0:
            chi_sq += (c - bin_mean) ** 2 / bin_mean
    df = k_bins - p_params - 1                  # 10 - 1 - 1 = 8
    p_gof = chi_sq_sf(chi_sq, df)

    gof_info = {
        'chi_sq': chi_sq,
        'df': df,
        'p_gof': p_gof,
        'threshold': POISSON_GOF_P_THRESHOLD,
        'null_e_gof_disqualified': p_gof <= POISSON_GOF_P_THRESHOLD,
        'bin_count': k_bins,
        'p_params': p_params,
    }
    if gof_info['null_e_gof_disqualified']:
        return None, gof_info

    # ---- Parametric sampling under H0 (class has no effect) ----
    mean_r = statistics.mean(residuals)
    sd_r = statistics.stdev(residuals) if len(residuals) > 1 else 0.01
    if sd_r == 0:
        sd_r = 0.01

    class_labels = [is_b for is_b, _, _ in per_verse]
    null_diffs = []
    for _ in range(n_perm):
        synth = [rng.gauss(mean_r, sd_r) for _ in range(n)]
        br = [synth[i] for i in range(n) if class_labels[i]]
        cf = [synth[i] for i in range(n) if not class_labels[i]]
        if not br or not cf:
            continue
        null_diffs.append(statistics.mean(br) - statistics.mean(cf))
    if len(null_diffs) < 10:
        return None, gof_info
    nm = statistics.mean(null_diffs)
    ns = statistics.stdev(null_diffs) if len(null_diffs) > 1 else 0
    return {
        'null': 'E_parametric_poisson',
        'obs_diff': obs_d,
        'null_mean': nm,
        'null_sd': ns,
        'z': (obs_d - nm) / ns if ns > 0 else 0,
        'n_null_draws': len(null_diffs),
    }, gof_info


# ===== Gate 1: Type-I calibration via random-rhyme-set draws =====
def calibration_gate_1(verses, corpus_name, length_breaks, segment_ids, B, null_runner, null_name, extra_kwargs=None):
    """Execute B random-rhyme-set draws; measure Type-I rejection rate at |z|>2.576.
    null_runner is called as null_runner(verses, rhyme_set, ..., seed=...).
    """
    extra_kwargs = extra_kwargs or {}
    rng_top = random.Random(SEED)
    above = 0
    n_runs = 0
    z_list = []
    aux_flags = {}

    for b in range(B):
        rset = set(rng_top.sample(ARAB_LETTERS, 5))
        if null_name == 'C':
            pv, _ = compute_per_verse_residuals(verses, rset)
            if not pv:
                continue
            result = null_C_stratified_perm(pv, segment_ids, length_breaks,
                                            n_perm=N_PERM_INNER_C, seed=SEED + b)
        elif null_name == 'D':
            result = null_D_block_bootstrap(verses, segment_ids, rset,
                                            n_perm=N_PERM_INNER_D, seed=SEED + b)
        elif null_name == 'E':
            pv, _ = compute_per_verse_residuals(verses, rset)
            if not pv:
                continue
            result, gof = null_E_parametric_poisson_gof(pv, n_perm=N_PERM_INNER_E, seed=SEED + b)
            if gof is not None:
                # Record first GoF failure verbatim for reporting
                if gof.get('null_e_gof_disqualified') and 'first_gof_disqualify' not in aux_flags:
                    aux_flags['first_gof_disqualify'] = gof
        else:
            return None

        if result is None:
            continue
        z_list.append(result['z'])
        if abs(result['z']) > CRIT_Z:
            above += 1
        n_runs += 1

    if n_runs == 0:
        return {'corpus': corpus_name, 'null': null_name, 'error': 'all_runs_failed', 'aux_flags': aux_flags}
    rate = above / n_runs
    return {
        'corpus': corpus_name,
        'null': null_name,
        'n_draws_attempted': B,
        'n_draws_valid': n_runs,
        'n_above_crit': above,
        'rate_reject_at_alpha_01_two_sided': rate,
        'calibration_window': list(CAL_WINDOW),
        'in_window': CAL_WINDOW[0] <= rate <= CAL_WINDOW[1],
        'mean_z': statistics.mean(z_list) if z_list else None,
        'median_z': statistics.median(z_list) if z_list else None,
        'sd_z': statistics.stdev(z_list) if len(z_list) > 1 else 0,
        'max_abs_z': max((abs(z) for z in z_list), default=0),
        'aux_flags': aux_flags,
    }


# ===== Planted-signal injector (shared with H-META-2 logic) =====
def plant_signal(verses, rhyme_set, effect_sigma, baseline_sigma, seed):
    """Inject break-class surprise boost with p_flip calibrated to baseline σ."""
    rng = random.Random(seed)
    rare_boost = 5.0
    typical_baseline = 3.0
    delta_per_flip = rare_boost - typical_baseline
    if baseline_sigma <= 0 or delta_per_flip <= 0:
        return None
    n_break = sum(1 for v in verses if len(v) > ORDER and v[-1] not in rhyme_set)
    if n_break == 0:
        return None
    p_flip = (effect_sigma * baseline_sigma) / delta_per_flip
    p_flip = min(max(p_flip, 0.0), 0.5)
    RARE = list('ظضغ')
    planted = []
    for v in verses:
        if len(v) < ORDER + 1:
            planted.append(v)
            continue
        term = v[-1]
        is_break = term not in rhyme_set
        if is_break and rng.random() < p_flip:
            planted.append(v[:-1] + rng.choice(RARE))
        else:
            planted.append(v)
    return planted


def estimate_baseline_sigma_for_planting(verses, rhyme_set):
    """Use Null-A-style label-perm on observed data to estimate null_sd for
    planting calibration (same technique H-META-2 used)."""
    pv, _ = compute_per_verse_residuals(verses, rhyme_set)
    if not pv:
        return None
    residuals = [r for _, _, r in pv]
    labels = [is_b for is_b, _, _ in pv]
    rng = random.Random(SEED + 999)
    diffs = []
    for _ in range(100):
        s = labels[:]
        rng.shuffle(s)
        br = [r for l, r in zip(s, residuals) if l]
        cf = [r for l, r in zip(s, residuals) if not l]
        if br and cf:
            diffs.append(statistics.mean(br) - statistics.mean(cf))
    return statistics.stdev(diffs) if len(diffs) > 1 else None


# ===== Gate 2: Planted-signal power cells =====
RHYME_CLASSICAL = set('نلمردقستكب')  # same as H-META-2


def power_gate_2(verses, corpus_name, length_breaks, segment_ids):
    """6 cells per candidate (this corpus × 3 σ levels).
    Returns {null_name: {sigma_X: {recovered_z, deviation}}}.
    """
    baseline_sigma = estimate_baseline_sigma_for_planting(verses, RHYME_CLASSICAL)
    if baseline_sigma is None:
        return None

    out = {
        'corpus': corpus_name,
        'baseline_sigma_for_planting': baseline_sigma,
        'rhyme_set': ''.join(sorted(RHYME_CLASSICAL)),
        'cells': {'C': {}, 'D': {}, 'E': {}},
    }

    for sigma in PLANTED_SIGMAS:
        planted = plant_signal(verses, RHYME_CLASSICAL, sigma, baseline_sigma,
                               seed=SEED + int(sigma * 100))
        if planted is None:
            continue

        # Rebuild segment_ids for planted verses (same segmentation — plant_signal
        # preserves verse order and count).
        seg_ids_p = segment_ids

        # --- Null-C ---
        pv_p, _ = compute_per_verse_residuals(planted, RHYME_CLASSICAL)
        if pv_p:
            rc = null_C_stratified_perm(pv_p, seg_ids_p, length_breaks,
                                        n_perm=500, seed=SEED + int(sigma * 100) + 1)
        else:
            rc = None
        out['cells']['C'][f'sigma_{sigma}'] = _cell(rc, sigma)

        # --- Null-D ---
        rd = null_D_block_bootstrap(planted, seg_ids_p, RHYME_CLASSICAL,
                                    n_perm=100, seed=SEED + int(sigma * 100) + 2)
        out['cells']['D'][f'sigma_{sigma}'] = _cell(rd, sigma)

        # --- Null-E ---
        if pv_p:
            re_, gof = null_E_parametric_poisson_gof(pv_p, n_perm=500, seed=SEED + int(sigma * 100) + 3)
        else:
            re_, gof = None, None
        cell = _cell(re_, sigma)
        if gof is not None and gof.get('null_e_gof_disqualified'):
            cell['null_e_gof_disqualified'] = True
            cell['gof'] = gof
        out['cells']['E'][f'sigma_{sigma}'] = cell

    return out


def _cell(result, planted_sigma):
    if result is None:
        return {
            'recovered_z': None,
            'obs_diff': None,
            'deviation_abs': None,
            'sign_correct': None,
            'planted_sigma': planted_sigma,
        }
    rz = result['z']
    return {
        'recovered_z': rz,
        'obs_diff': result['obs_diff'],
        'null_mean': result['null_mean'],
        'null_sd': result['null_sd'],
        'deviation_abs': abs(abs(rz) - planted_sigma),
        'sign_correct': rz > 0,  # planted signal boosts break-class → positive
        'planted_sigma': planted_sigma,
    }


# ===== Joint verdict adjudication =====
def adjudicate_candidate(gate1_mut, gate1_jah, power_mut, power_jah, null_name):
    """Return (verdict, details) per pre-committed joint verdict table."""
    details = {
        'gate1_mutanabbi_rate': None,
        'gate1_jahiz_rate': None,
        'gate1_mutanabbi_in_window': None,
        'gate1_jahiz_in_window': None,
        'gate1_pass': None,
        'cells_6': [],
        'all_sign_correct': None,
        'max_dev_abs': None,
        'gate2_strict': None,
        'gate2_relaxed': None,
        'verdict': None,
    }

    m = gate1_mut.get(null_name) if gate1_mut else None
    j = gate1_jah.get(null_name) if gate1_jah else None
    if m and 'rate_reject_at_alpha_01_two_sided' in m:
        details['gate1_mutanabbi_rate'] = m['rate_reject_at_alpha_01_two_sided']
        details['gate1_mutanabbi_in_window'] = m['in_window']
    if j and 'rate_reject_at_alpha_01_two_sided' in j:
        details['gate1_jahiz_rate'] = j['rate_reject_at_alpha_01_two_sided']
        details['gate1_jahiz_in_window'] = j['in_window']
    gate1 = bool(details['gate1_mutanabbi_in_window']) and bool(details['gate1_jahiz_in_window'])
    details['gate1_pass'] = gate1

    # Assemble 6 power cells
    cells = []
    for corpus_power, corpus_tag in ((power_mut, 'mut'), (power_jah, 'jah')):
        if corpus_power is None:
            continue
        cells_by_null = corpus_power['cells'].get(null_name, {})
        for sigma in PLANTED_SIGMAS:
            cell = cells_by_null.get(f'sigma_{sigma}')
            if cell:
                cells.append({'corpus': corpus_tag, 'sigma': sigma, **cell})
    details['cells_6'] = cells

    valid = [c for c in cells if c.get('recovered_z') is not None]
    if len(valid) != 6:
        gof_disqualified = any(c.get('null_e_gof_disqualified') for c in cells)
        if gof_disqualified:
            details['verdict'] = 'DISQUALIFIED (Null-E parametric mis-specification — Poisson χ² GoF p<0.05)'
        elif not gate1:
            details['verdict'] = 'DISQUALIFIED (Type-I mis-calibrated and power-cell incomplete)'
        else:
            details['verdict'] = 'DISQUALIFIED (power-cell incomplete)'
        return details['verdict'], details

    all_sign = all(c['sign_correct'] for c in valid)
    max_dev = max(c['deviation_abs'] for c in valid)
    details['all_sign_correct'] = all_sign
    details['max_dev_abs'] = max_dev
    details['gate2_strict'] = all_sign and max_dev < GATE2_STRICT_K
    details['gate2_relaxed'] = all_sign and max_dev < GATE2_RELAXED_K

    if not gate1:
        details['verdict'] = 'DISQUALIFIED (Type-I mis-calibrated)'
    elif details['gate2_strict']:
        details['verdict'] = 'CALIBRATED'
    elif details['gate2_relaxed']:
        details['verdict'] = 'PROVISIONALLY CALIBRATED'
    else:
        details['verdict'] = 'DISQUALIFIED (Type-I OK but power mis-calibrated)'
    return details['verdict'], details


# ===== Segment-id helpers =====
def mutanabbi_segment_ids(verses):
    """Mutanabbī is flat; treat groups of 32 lines as one 'bayt-cluster segment'
    so Null-C has a meaningful stratum structure beyond pure-length. 32 lines
    ≈ one qaṣīda-section which the text has internal coherence. Frozen at
    script start, not tuned."""
    return [i // 32 for i in range(len(verses))]


def jahiz_segment_ids(verses):
    """Jāḥiẓ is segmented into sentence-'verses'; treat groups of 32 as one
    chapter-segment for Null-C strata. Same rationale as Mutanabbī."""
    return [i // 32 for i in range(len(verses))]


# =============================================================================
# MAIN
# =============================================================================
def main():
    t0 = time.time()
    log(f"[seed] {SEED}")
    log(f"[bonferroni] k={BONFERRONI_K}, α_bon={ALPHA_BON:.4f}")
    mode = 'PILOT (scratch/, NOT verdict)' if PILOT_MODE else 'VERDICT (pre-reg verbatim)'
    log(f"[mode] {mode}")
    log(f"[budget] B_GATE1={B_GATE1}, N_PERM_INNER C/D/E = {N_PERM_INNER_C}/{N_PERM_INNER_D}/{N_PERM_INNER_E}")
    log(f"[output] {OUTPUT_JSON}")
    log(f"[pid] {os.getpid()}")

    # ---- Addendum Note 1: compute length-decile breakpoints from pooled Quran ----
    log("\n[addendum-1] Computing length-decile breakpoints from pooled Quran...")
    quran_lengths = load_quran_for_deciles()
    length_breaks = compute_length_decile_breakpoints(quran_lengths)
    log(f"  Quran verses for deciles: {len(quran_lengths)}")
    log(f"  Decile breakpoints (9 values): {length_breaks}")

    # ---- Load H-META-2-comparability corpora ----
    log("\n[corpora] Loading H-META-2-comparability baselines...")
    MUT = load_mutanabbi()
    JAH = load_jahiz()
    rng0 = random.Random(SEED)
    if len(JAH) > 3000:
        JAH = rng0.sample(JAH, 3000)
    MUT_SEG = mutanabbi_segment_ids(MUT)
    JAH_SEG = jahiz_segment_ids(JAH)
    log(f"  Mutanabbī: {len(MUT)} lines, {max(MUT_SEG)+1 if MUT_SEG else 0} segments")
    log(f"  Jāḥiẓ:     {len(JAH)} segments, {max(JAH_SEG)+1 if JAH_SEG else 0} segment-clusters")

    # =======================================================================
    # GATE 1: Type-I independence calibration for C/D/E on both corpora
    # Resumable: per-(null × corpus) checkpoints
    # =======================================================================
    log(f"\n[gate-1] Type-I calibration @ B={B_GATE1}, α_bon={ALPHA_BON:.4f}")

    gate1_mut = {}
    gate1_jah = {}
    for null_name in ('C', 'D', 'E'):
        for corpus_label, verses, seg_ids, gate_dict in (
            ('mutanabbi', MUT, MUT_SEG, gate1_mut),
            ('jahiz', JAH, JAH_SEG, gate1_jah),
        ):
            t_cell = time.time()
            ckpt = load_checkpoint('gate1', null_name, corpus_label)
            if ckpt is not None:
                log(f"  [gate-1 / {null_name} / {corpus_label}] RESUMING from checkpoint")
                gate_dict[null_name] = ckpt
                rate_c = ckpt.get('rate_reject_at_alpha_01_two_sided')
                in_c = ckpt.get('in_window')
                log(f"    rate={rate_c}, in_window={in_c} (cached)")
                continue
            log(f"  [gate-1 / {null_name} / {corpus_label}] running B={B_GATE1}...")
            corpus_full = 'mutanabbi-diwan' if corpus_label == 'mutanabbi' else 'jahiz-hayawan'
            result = calibration_gate_1(verses, corpus_full, length_breaks, seg_ids,
                                        B=B_GATE1, null_runner=None, null_name=null_name)
            gate_dict[null_name] = result
            elapsed = time.time() - t_cell
            rate_c = result.get('rate_reject_at_alpha_01_two_sided')
            in_c = result.get('in_window')
            log(f"    rate={rate_c}, in_window={in_c}, elapsed={elapsed:.1f}s")
            save_checkpoint('gate1', null_name, corpus_label, result)

    # =======================================================================
    # GATE 2: Planted-signal power cells for C/D/E on both corpora
    # =======================================================================
    log("\n[gate-2] Planted-signal power cells @ σ ∈ {0.5, 1.0, 2.0}")

    power_mut = load_checkpoint('gate2', 'all', 'mutanabbi')
    if power_mut is not None:
        log("  Mutanabbī power RESUMING from checkpoint")
    else:
        t_pm = time.time()
        power_mut = power_gate_2(MUT, 'mutanabbi-diwan', length_breaks, MUT_SEG)
        log(f"  Mutanabbī power done elapsed={time.time()-t_pm:.1f}s")
        if power_mut is not None:
            save_checkpoint('gate2', 'all', 'mutanabbi', power_mut)

    power_jah = load_checkpoint('gate2', 'all', 'jahiz')
    if power_jah is not None:
        log("  Jāḥiẓ power RESUMING from checkpoint")
    else:
        t_pj = time.time()
        power_jah = power_gate_2(JAH, 'jahiz-hayawan', length_breaks, JAH_SEG)
        log(f"  Jāḥiẓ power done elapsed={time.time()-t_pj:.1f}s")
        if power_jah is not None:
            save_checkpoint('gate2', 'all', 'jahiz', power_jah)

    # =======================================================================
    # JOINT ADJUDICATION + winner-selection
    # =======================================================================
    log("\n[adjudication] Joint verdict per candidate...")
    adjudication = {}
    for null_name in ('C', 'D', 'E'):
        verdict, details = adjudicate_candidate(gate1_mut, gate1_jah, power_mut, power_jah, null_name)
        adjudication[null_name] = details
        log(f"  Null-{null_name}: {verdict}")

    # Winner selection among PASSes
    passes = [n for n in ('C', 'D', 'E') if 'CALIBRATED' in (adjudication[n].get('verdict') or '')
              and 'DISQUALIFIED' not in (adjudication[n].get('verdict') or '')]
    winner = None
    if passes:
        # tie-breaker = arithmetic mean absolute deviation across 6 cells
        def mean_abs_dev(n):
            cells = adjudication[n]['cells_6']
            devs = [c['deviation_abs'] for c in cells if c.get('deviation_abs') is not None]
            return statistics.mean(devs) if devs else float('inf')
        passes_sorted = sorted(passes, key=lambda n: (mean_abs_dev(n), 0 if n == 'C' else 1))
        winner = passes_sorted[0]

    # Family verdict
    all_disqualified = all('DISQUALIFIED' in (adjudication[n].get('verdict') or '') for n in ('C', 'D', 'E'))
    if all_disqualified:
        family_verdict = 'META-NULL-REINFORCED'
    elif winner is not None:
        family_verdict = f'WINNER={winner}'
    else:
        family_verdict = 'NO WINNER (mixed)'

    # =======================================================================
    # Output JSON
    # =======================================================================
    out = {
        'task_id': 118,
        'test_name': 'H-NEW-META-3 third-null specification for Markov-surprise family',
        'parent_task': 43,
        'parent_verdict': 'H-META-2 BOTH_DISQUALIFIED',
        'pre_registration_file': 'findings/phase-c-structures/h-new-meta-3-prereg.md',
        'seed': SEED,
        'rules_tuple': '(no-tashkeel, orthographic-token, hafs-kufan, mashriqi)',
        'bonferroni_k': BONFERRONI_K,
        'alpha_bon': ALPHA_BON,
        'calibration_window': list(CAL_WINDOW),
        'planted_sigmas': PLANTED_SIGMAS,
        'addendum_note_1': {
            'description': 'Length-decile breakpoints computed on pooled Quran full 6,236-verse corpus',
            'pre_committed': '2026-04-14 per audit-030 Note 1',
            'n_quran_verses': len(quran_lengths),
            'breakpoints': length_breaks,
        },
        'addendum_note_2': {
            'description': 'Null-E Poisson χ² GoF, k=10 bins, p>0.05 threshold',
            'pre_committed': '2026-04-14 per audit-030 Note 2',
            'bins': POISSON_GOF_BINS,
            'p_threshold': POISSON_GOF_P_THRESHOLD,
        },
        'gate_1_calibration': {
            'mutanabbi': gate1_mut,
            'jahiz': gate1_jah,
            'window': list(CAL_WINDOW),
            'crit_z': CRIT_Z,
            'n_draws': B_GATE1,
        },
        'gate_2_power': {
            'mutanabbi': power_mut,
            'jahiz': power_jah,
            'planted_sigmas': PLANTED_SIGMAS,
            'gate2_strict_threshold_k': GATE2_STRICT_K,
            'gate2_relaxed_threshold_k': GATE2_RELAXED_K,
        },
        'adjudication': adjudication,
        'winner_selection': {
            'passes': passes,
            'tie_breaker': 'arithmetic_mean_abs_deviation_across_6_cells',
            'null_c_preferred_on_ties': True,
            'winner': winner,
        },
        'family_verdict': family_verdict,
        'pilot_mode': PILOT_MODE,
        'garden_of_forking_paths': {
            'note': 'NO pre-reg threshold or B parameter changes. Both Gate-1 outer '
                    'B and inner N_PERM are pre-reg-locked at 1000 and executed '
                    'verbatim per team-lead Option-A ruling 2026-04-13.',
            'operational_infrastructure_added': [
                {
                    'change': 'Per-(null × corpus) JSON checkpointing added to gate-1 loop',
                    'rationale': 'Crash-recovery infrastructure. Re-launch reads existing '
                                 'checkpoints and skips already-completed cells. Does NOT '
                                 'change the test, the seed, the B values, or the verdict '
                                 'computation. Pure operational protection against silent '
                                 'kill (which destroyed the first launch).',
                    'verdict_independence': 'Same seed=20260414 → same rhyme-set draws → '
                                            'same z-statistics regardless of whether a '
                                            'cell ran fresh or resumed from checkpoint.',
                },
                {
                    'change': 'nohup + caffeinate -s launcher (macOS App-Nap protection)',
                    'rationale': 'First launch died silently in gate-1/C/mutanabbi after '
                                 '13 lines of output, no traceback. Diagnosed (arabic-'
                                 'specialist + computational-tester) as SIGHUP / App-Nap '
                                 'kill on background Python without controlling-terminal '
                                 'detachment.',
                },
                {
                    'change': 'stderr flush=True on all log calls',
                    'rationale': 'Prevent log truncation on future silent kills so any '
                                 'traceback is captured.',
                },
            ],
            'aborted_runs_disclosed': [
                {
                    'date': '2026-04-13',
                    'launch_id': 'first_launch_silent_kill',
                    'config': 'B_GATE1=1000, N_PERM_INNER=200/50/200',
                    'cause': 'Silent SIGHUP/App-Nap kill in gate-1/C/mutanabbi inner loop. '
                             'Killed before any JSON write. NO RESULTS RECORDED.',
                    'data_used_in_verdict': False,
                },
                {
                    'date': '2026-04-13',
                    'launch_id': 'second_launch_b500_killed_by_tester',
                    'config': 'B_GATE1=500, N_PERM_INNER=200/50/200',
                    'context': 'Launched after team-lead initial message (Option-B-adjacent '
                               'B=500 framing). Manually killed by computational-tester '
                               'after team-lead clarified Option A (pre-reg verbatim) '
                               'supersedes. Killed after gate-1/C/mutanabbi cell completed '
                               'with rate=0.666 in_window=False. THIS PARTIAL RESULT IS '
                               'EXPLICITLY POISONED AND NOT USED — it informed pilot '
                               'design only insofar as runtime calibration (~121s per '
                               'cell at B=500/N=200) extrapolated to B=1000/N=1000.',
                    'data_used_in_verdict': False,
                    'audit_031_check': 'Verify the rate=0.666 / in_window=False data '
                                       'point from this aborted run does NOT appear in '
                                       'gate_1_calibration.mutanabbi.C of this verdict '
                                       'JSON. The verdict run reruns gate-1/C/mutanabbi '
                                       'from scratch at B=1000/N=1000 with seed 20260414, '
                                       'producing a fresh rate value that supersedes the '
                                       'aborted-run data point.',
                },
                {
                    'date': '2026-04-13',
                    'launch_id': 'pilot_run',
                    'config': 'B_GATE1=200, N_PERM_INNER=100/30/100, output → scratch/',
                    'context': 'Pipeline shake-down for bug detection (segment-id '
                               'alignment, planted-signal injection, checkpoint I/O). '
                               'Output diverted to scratch/h_new_meta_3_pilot/ via '
                               'env var H_META_3_PILOT=1. NEVER touches pre-reg JSON path.',
                    'data_used_in_verdict': False,
                },
            ],
            'verdict_run': {
                'config': 'B_GATE1=1000, N_PERM_INNER=1000/1000/1000 — pre-reg verbatim',
                'launcher': 'nohup caffeinate -s python3 -u … (overnight)',
                'team_lead_ruling': 'Option A locked 2026-04-13',
                'data_used_in_verdict': True,
            },
        },
    }

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(out, indent=2, ensure_ascii=False, default=str))
    log(f"\nsaved: {OUTPUT_JSON}")
    log(f"\n=== FAMILY VERDICT: {family_verdict} ===")
    for n in ('C', 'D', 'E'):
        log(f"  Null-{n}: {adjudication[n].get('verdict')}")
    log(f"\ntotal elapsed: {time.time()-t0:.1f}s")


if __name__ == '__main__':
    main()
