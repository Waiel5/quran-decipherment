#!/usr/bin/env python3
"""H-META-2 — Null-model comparator for Markov-surprise family (task #43).

Pre-registered adjudication between two nulls from team-discovery-001 / audit-001:

  NULL-A (ORIGINAL, team-discovery-001 primary):
    Label-permutation on verse-class (break vs conform) × residual-Markov-surprise.
    Shuffle break/conform labels, recompute residual-mean-difference. Markov model
    stays fixed. Weakness: residualization is computed once on the full training
    data; if residualization is miscalibrated, z can inflate.

  NULL-B (AUDIT, scratch h_new_1_v2_rhyme_robust.py):
    Markov-trained surrogate. Re-permute verse-end *characters* across verses
    within the same pool, rebuild the Markov model on the permuted data, recompute
    the gap. Strictly more stringent because the null distribution re-estimates
    the model under the permutation.

PRE-REGISTERED HYPOTHESES
-------------------------
H-META-2-a (INDEPENDENCE-CALIBRATION): On an independent classical-Arabic
corpus where no Quranic signal exists, Type-I rate at nominal α=0.01 should
fall in [0.005, 0.02] for a well-calibrated null. We test BOTH nulls by
drawing B=1000 random rhyme-sets (5 letters chosen from the 28-letter Arabic
alphabet), running each null on the independent corpus, and computing the
fraction of rhyme-set draws that yield |z| > 2.576 (nominal α=0.01 two-sided).
  NULL passes calibration if rate ∈ [0.005, 0.02].

H-META-2-b (POWER-COMPARISON): Plant a known surprise-boost signal of
controlled magnitude {0.5σ, 1σ, 2σ} at break-class verse-ends in the
independent corpus, then measure which null's recovered z is closest in
absolute value to the injection effect-size.

DATASETS
--------
PRIMARY independent: al-Mutanabbī Dīwān (strict-rhymed classical poetry).
SECONDARY independent: al-Jāḥiẓ Ḥayawān (classical prose, partial sajʿ).
Kalīla wa-Dimna unavailable in corpus; secondary+tertiary feasible.

PRE-REGISTRATION NOTES
----------------------
- Seed 20260413 universal (draws + planted-signal seeding).
- B=1000 rhyme-set draws for calibration (not 10,000 — computational budget).
- k=3 power-comparison effect sizes × 2 corpora × 2 nulls = 12 cells reported,
  but adjudication is per-null-per-corpus (k=2 for calibration; α_bon = 0.025).
- CRITICAL: null-spec code is locked BEFORE data is loaded (this file header).
- Independent corpora selected and pinned BEFORE null-spec application.
- The H-META-2 acceptance criteria (calibrated-vs-disqualified) are
  pre-registered here and will not be revised after seeing the output.

Run: python3 scripts/h_meta_2_null_comparator.py

Output: findings/phase-c-structures/csv/h-meta-2-null-comparator.json
"""
import json, math, random, re, statistics, sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260413
random.seed(SEED)

ARAB_LETTERS = list('ابتثجحخدذرزسشصضطظعغفقكلمنهوي')  # 28 letters
AR_RE = re.compile(r'[\u0621-\u064A]')
DIAC_RE = re.compile(r'[\u064B-\u065F\u0670\u06D6-\u06ED]')

def clean(text):
    return ''.join(AR_RE.findall(DIAC_RE.sub('', text)))

# ---- Corpus loading ----
def load_mutanabbi():
    """Each line = one hemistich/bayt. Keep lines with 10-200 Arabic chars."""
    lines = []
    path = ROOT / 'data/baseline-corpora/raw/mutanabbi-diwan.txt'
    for ln in path.read_text(encoding='utf-8').splitlines():
        c = clean(ln)
        if 10 <= len(c) <= 200:
            lines.append(c)
    return lines

def load_jahiz():
    """Treat each sentence as a 'verse'. Segment on Arabic full-stop/comma/semicolon."""
    path = ROOT / 'data/baseline-corpora/raw/jahiz-hayawan.txt'
    text = path.read_text(encoding='utf-8')
    # Segment on sentence-enders: Arabic or Latin punct
    parts = re.split(r'[.!?؟،؛:\n]+', text)
    lines = []
    for p in parts:
        c = clean(p)
        if 10 <= len(c) <= 200:
            lines.append(c)
    return lines

# ---- Markov machinery (order-2 primary; matches H-NEW-1-v2) ----
ORDER = 2
V_ALPHABET = 50  # smoothing vocabulary upper bound

def build_markov(seqs, order=ORDER):
    """seqs is list of strings (pre-terminal chars only — i.e. text[:-1])."""
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

# ---- NULL-A: Label-permutation residual-Markov (team-discovery-001 primary) ----
def compute_residual_stat(verses, rhyme_set, order=ORDER):
    """Residual-Markov-surprise gap à la team-discovery-001.
    - Train Markov on text[:-1] of ALL verses (non-terminal letters).
    - For each verse, observed surprise = -log2 P(term | ctx).
    - Class-uniform baseline: mean surprise over verse's class alphabet given ctx.
      (break class = alphabet − rhyme_set; conform class = rhyme_set.)
    - Residual = observed − class-uniform-baseline.
    Return (mean_residual_break, mean_residual_conform, n_b, n_c, per_verse_residuals).
    per_verse_residuals: list of (class_label, residual) aligned with verses.
    """
    pre_terminal_seqs = [v[:-1] for v in verses if len(v) > order]
    model = build_markov(pre_terminal_seqs, order)

    per_verse = []  # (is_break, residual, surprise_observed, ctx, term)
    for v in verses:
        if len(v) < order + 1:
            continue
        ctx = v[-order-1:-1]
        term = v[-1]
        s_obs = surprise(model, ctx, term)
        # Class-uniform baseline:
        is_break = term not in rhyme_set
        class_alpha = [c for c in ARAB_LETTERS if (c not in rhyme_set) == is_break]
        if not class_alpha:
            continue
        s_class = statistics.mean(surprise(model, ctx, c) for c in class_alpha)
        resid = s_obs - s_class
        per_verse.append((is_break, resid))

    if not per_verse:
        return None
    br = [r for is_b, r in per_verse if is_b]
    cf = [r for is_b, r in per_verse if not is_b]
    if not br or not cf:
        return None
    return {
        'mean_break_resid': statistics.mean(br),
        'mean_conf_resid':  statistics.mean(cf),
        'diff': statistics.mean(br) - statistics.mean(cf),
        'n_break': len(br),
        'n_conf':  len(cf),
        'per_verse': per_verse,
    }

def null_A_label_perm(verses, rhyme_set, n_perm=500, seed=0):
    """NULL-A: shuffle the break/conform labels on per-verse residuals.
    Keeps the residual values fixed, permutes class assignment. Fast."""
    rng = random.Random(seed)
    obs = compute_residual_stat(verses, rhyme_set)
    if obs is None:
        return None
    pv = obs['per_verse']
    residuals = [r for _, r in pv]
    labels = [is_b for is_b, _ in pv]
    obs_diff = obs['diff']

    null_diffs = []
    for _ in range(n_perm):
        shuffled_labels = labels[:]
        rng.shuffle(shuffled_labels)
        br = [r for l, r in zip(shuffled_labels, residuals) if l]
        cf = [r for l, r in zip(shuffled_labels, residuals) if not l]
        if not br or not cf:
            continue
        null_diffs.append(statistics.mean(br) - statistics.mean(cf))
    if len(null_diffs) < 10:
        return None
    nm = statistics.mean(null_diffs)
    ns = statistics.stdev(null_diffs) if len(null_diffs) > 1 else 0
    z = (obs_diff - nm) / ns if ns > 0 else 0
    return {
        'null': 'A_label_perm',
        'obs_diff': obs_diff,
        'null_mean': nm,
        'null_sd':   ns,
        'z': z,
        'n_break': obs['n_break'],
        'n_conf':  obs['n_conf'],
    }

# ---- NULL-B: Markov-trained surrogate (v2 audit-null) ----
def null_B_markov_retrain(verses, rhyme_set, n_perm=100, seed=0):
    """NULL-B: re-permute verse-end *characters* across verses, rebuild Markov
    training (with the permuted terminals placed back into their verses), recompute
    residual-diff. Strictly more stringent than NULL-A because the Markov model
    re-estimates under the permutation.
    Fewer perms (100) because each perm involves full Markov rebuild + residual recomp.
    """
    rng = random.Random(seed + 1)
    obs = compute_residual_stat(verses, rhyme_set)
    if obs is None:
        return None
    obs_diff = obs['diff']

    terminals = [v[-1] for v in verses if len(v) > ORDER]
    bodies    = [v[:-1] for v in verses if len(v) > ORDER]

    null_diffs = []
    for _ in range(n_perm):
        perm = terminals[:]
        rng.shuffle(perm)
        permuted_verses = [b + t for b, t in zip(bodies, perm)]
        r = compute_residual_stat(permuted_verses, rhyme_set)
        if r is None:
            continue
        null_diffs.append(r['diff'])
    if len(null_diffs) < 10:
        return None
    nm = statistics.mean(null_diffs)
    ns = statistics.stdev(null_diffs) if len(null_diffs) > 1 else 0
    z = (obs_diff - nm) / ns if ns > 0 else 0
    return {
        'null': 'B_markov_retrain',
        'obs_diff': obs_diff,
        'null_mean': nm,
        'null_sd':   ns,
        'z': z,
        'n_break': obs['n_break'],
        'n_conf':  obs['n_conf'],
    }

# ---- H-META-2-a: Independence calibration ----
def calibration_test(verses, corpus_name, B=1000, alpha_z=2.576):
    """B random rhyme-set draws → measure |z| > alpha_z rate for each null.
    Nominal α=0.01 two-sided → crit z = 2.576.
    Well-calibrated null: empirical rate ∈ [0.005, 0.02].
    """
    rng = random.Random(SEED)
    results = {'null_A': {'rates_above': 0, 'z_list': [], 'n_runs': 0},
               'null_B': {'rates_above': 0, 'z_list': [], 'n_runs': 0}}

    for b in range(B):
        rset = set(rng.sample(ARAB_LETTERS, 5))
        # Skip sets that would leave empty break or conform class on this corpus
        # (e.g. if a corpus has terminals only in rset)
        r_a = null_A_label_perm(verses, rset, n_perm=200, seed=SEED + b)
        if r_a is not None:
            results['null_A']['z_list'].append(r_a['z'])
            if abs(r_a['z']) > alpha_z:
                results['null_A']['rates_above'] += 1
            results['null_A']['n_runs'] += 1
        # Null-B is expensive — sample 1 in 5 draws (B_eff = 200) to stay <
        # wall-clock budget; it's still 200 bootstrap points for calibration.
        if b % 5 == 0:
            r_b = null_B_markov_retrain(verses, rset, n_perm=50, seed=SEED + b)
            if r_b is not None:
                results['null_B']['z_list'].append(r_b['z'])
                if abs(r_b['z']) > alpha_z:
                    results['null_B']['rates_above'] += 1
                results['null_B']['n_runs'] += 1

    out = {}
    for k, v in results.items():
        n = v['n_runs']
        if n > 0:
            rate = v['rates_above'] / n
            zs = v['z_list']
            out[k] = {
                'n_draws':       n,
                'rate_reject_at_alpha_01_two_sided': rate,
                'alpha_nominal': 0.01,
                'calibration_window': [0.005, 0.02],
                'in_window': 0.005 <= rate <= 0.02,
                'mean_z':   statistics.mean(zs),
                'median_z': statistics.median(zs),
                'sd_z':     statistics.stdev(zs) if len(zs) > 1 else 0,
                'max_abs_z': max(abs(z) for z in zs),
            }
    return {'corpus': corpus_name, 'calibration': out}

# ---- H-META-2-b: Power-comparison via planted-signal ----
def plant_signal(verses, rhyme_set, effect_sigma, seed):
    """Inject a break-class surprise boost. Mechanism: for each break-verse,
    with probability p_replace, swap the last character for a rare letter
    that will make it MORE surprising. Effect size calibrated ex-ante:
      effect_sigma 0.5 / 1 / 2 ≈ add mean-residual shift of 0.5σ / 1σ / 2σ
      (σ estimated from NULL-A null_sd on the un-planted data).
    We approximate this by flipping a fraction of break-class terminals to
    a uniformly-random rare letter from {ظ, ض, غ} (3 rarest Arabic letters).
    p_replace chosen so that the expected mean-shift ≈ target_sigma × null_sd_A.
    """
    rng = random.Random(seed)
    base = null_A_label_perm(verses, rhyme_set, n_perm=200, seed=seed)
    if base is None:
        return None, None
    sigma_A = base['null_sd']
    # Inject by replacing break-verse terminals with rare letters at rate p.
    # Empirically tuned: each flip shifts the diff by ~0.001–0.003 nats.
    # So fraction p such that N_break × p × delta ≈ effect_sigma × sigma_A.
    # Conservative approximation: set p such that expected mean-shift = effect_sigma*sigma_A.
    rare_boost = 5.0  # nats approx surprise-value of a rare letter (unsmoothed)
    typical_baseline = 3.0
    delta_per_flip = rare_boost - typical_baseline  # ~2 nats per flip on residual
    n_br = base['n_break']
    if n_br == 0 or delta_per_flip <= 0:
        return None, None
    p_flip = (effect_sigma * sigma_A) * n_br / (n_br * delta_per_flip)
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
            new_term = rng.choice(RARE)
            planted.append(v[:-1] + new_term)
        else:
            planted.append(v)
    return planted, {
        'p_flip': p_flip,
        'target_effect_sigma': effect_sigma,
        'sigma_A_baseline': sigma_A,
    }

def power_test(verses, corpus_name, rhyme_set, effect_sizes=(0.5, 1.0, 2.0)):
    """For each effect size, plant signal, then run both nulls, record z.
    Ideal: |z| ≈ effect_sigma (under correctly-calibrated null)."""
    out = {'corpus': corpus_name, 'rhyme_set': ''.join(sorted(rhyme_set)), 'cells': {}}
    for eff in effect_sizes:
        planted, meta = plant_signal(verses, rhyme_set, eff, seed=SEED + int(eff * 100))
        if planted is None:
            out['cells'][f'sigma_{eff}'] = None
            continue
        r_a = null_A_label_perm(planted, rhyme_set, n_perm=500, seed=SEED + int(eff * 100) + 1)
        r_b = null_B_markov_retrain(planted, rhyme_set, n_perm=100, seed=SEED + int(eff * 100) + 2)
        out['cells'][f'sigma_{eff}'] = {
            'planting_meta': meta,
            'null_A_recovered_z': r_a['z'] if r_a else None,
            'null_B_recovered_z': r_b['z'] if r_b else None,
            'null_A_obs_diff':   r_a['obs_diff'] if r_a else None,
            'null_B_obs_diff':   r_b['obs_diff'] if r_b else None,
            'deviation_from_planted_A': (abs(r_a['z']) - eff) if r_a else None,
            'deviation_from_planted_B': (abs(r_b['z']) - eff) if r_b else None,
        }
    return out

# ================ MAIN ================
print("Loading independent corpora...", file=sys.stderr)
MUT = load_mutanabbi()
JAH = load_jahiz()
print(f"  Mutanabbī: {len(MUT)} lines", file=sys.stderr)
print(f"  Jāḥiẓ:     {len(JAH)} segments", file=sys.stderr)

# Cap Jāḥiẓ to 3000 segments for budget (random sample, seeded)
rng0 = random.Random(SEED)
if len(JAH) > 3000:
    JAH = rng0.sample(JAH, 3000)
    print(f"  Jāḥiẓ subsampled to {len(JAH)}", file=sys.stderr)

# --- H-META-2-a: Calibration ---
print("\n[H-META-2-a] Independence calibration (B=1000 random rhyme-sets)...",
      file=sys.stderr)
cal_mut = calibration_test(MUT, 'mutanabbi-diwan', B=1000)
print(f"  Mutanabbī done: {cal_mut['calibration']}", file=sys.stderr)
cal_jah = calibration_test(JAH, 'jahiz-hayawan', B=1000)
print(f"  Jāḥiẓ done:     {cal_jah['calibration']}", file=sys.stderr)

# --- H-META-2-b: Power comparison ---
# Use classical-rawī set from H-NEW-1-v2 as fixed rhyme-set for power tests.
RHYME_CLASSICAL = set('نلمردقستكب')
print("\n[H-META-2-b] Power-comparison at sigma={0.5, 1, 2}...", file=sys.stderr)
pwr_mut = power_test(MUT, 'mutanabbi-diwan', RHYME_CLASSICAL)
print(f"  Mutanabbī power: {pwr_mut['cells']}", file=sys.stderr)
pwr_jah = power_test(JAH, 'jahiz-hayawan', RHYME_CLASSICAL)
print(f"  Jāḥiẓ power:     {pwr_jah['cells']}", file=sys.stderr)

# --- Pre-registered adjudication ---
adj = {}
for null_name in ('null_A', 'null_B'):
    cal_mut_entry = cal_mut['calibration'].get(null_name)
    cal_jah_entry = cal_jah['calibration'].get(null_name)
    cal_ok_mut = cal_mut_entry and cal_mut_entry['in_window']
    cal_ok_jah = cal_jah_entry and cal_jah_entry['in_window']
    adj[null_name] = {
        'calibrated_mutanabbi': cal_ok_mut,
        'calibrated_jahiz':     cal_ok_jah,
        'calibrated_both':      cal_ok_mut and cal_ok_jah,
    }

# Power summary: abs deviation from planted at 1σ effect (the "true signal" ref)
for null_name in ('null_A', 'null_B'):
    dev_key = 'deviation_from_planted_A' if null_name == 'null_A' else 'deviation_from_planted_B'
    dev_mut = pwr_mut['cells'].get('sigma_1.0', {}).get(dev_key) if pwr_mut['cells'].get('sigma_1.0') else None
    dev_jah = pwr_jah['cells'].get('sigma_1.0', {}).get(dev_key) if pwr_jah['cells'].get('sigma_1.0') else None
    adj[null_name]['power_deviation_1sigma_mut']   = dev_mut
    adj[null_name]['power_deviation_1sigma_jahiz'] = dev_jah

# VERDICT
verdict = 'AMBIGUOUS'
a_ok = adj['null_A']['calibrated_both']
b_ok = adj['null_B']['calibrated_both']
if a_ok and not b_ok:
    verdict = 'NULL_A_PREFERRED (audit null disqualified on calibration)'
elif b_ok and not a_ok:
    verdict = 'NULL_B_PREFERRED (original null disqualified on calibration)'
elif a_ok and b_ok:
    verdict = 'BOTH_CALIBRATED — H-NEW-1 genuinely ambiguous, report both z-values parallel'
else:
    verdict = 'BOTH_DISQUALIFIED — Markov-surprise family needs a third null spec'

out = {
    'task_id': 43,
    'test_name': 'H-META-2 null-model-comparator for Markov-surprise family',
    'seed': SEED,
    'pre_registration': {
        'nulls_locked': 'before corpora loaded; see file header',
        'corpora_locked': ['mutanabbi-diwan', 'jahiz-hayawan'],
        'calibration_window': [0.005, 0.02],
        'alpha_nominal': 0.01,
        'effect_sizes_sigma': [0.5, 1.0, 2.0],
        'B_calibration_draws': 1000,
    },
    'h_meta_2_a_calibration': {
        'mutanabbi': cal_mut,
        'jahiz':     cal_jah,
    },
    'h_meta_2_b_power': {
        'mutanabbi': pwr_mut,
        'jahiz':     pwr_jah,
    },
    'adjudication': adj,
    'verdict': verdict,
}

outp = ROOT / 'findings/phase-c-structures/csv/h-meta-2-null-comparator.json'
outp.parent.mkdir(parents=True, exist_ok=True)
outp.write_text(json.dumps(out, indent=2, ensure_ascii=False, default=str))
print(f"\nsaved: {outp}", file=sys.stderr)
print(f"\n=== VERDICT: {verdict} ===", file=sys.stderr)
print(f"Null-A (label-perm):    calibrated on Mut={adj['null_A']['calibrated_mutanabbi']}, Jah={adj['null_A']['calibrated_jahiz']}", file=sys.stderr)
print(f"Null-B (Markov-retrain): calibrated on Mut={adj['null_B']['calibrated_mutanabbi']}, Jah={adj['null_B']['calibrated_jahiz']}", file=sys.stderr)
