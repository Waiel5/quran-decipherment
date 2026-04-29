#!/usr/bin/env python3
"""MW-6 reliability moderator — does verbatim-confidence tier predict confirmable rate?

Restricts to classical-medieval era to avoid era×tier confound (UNTAGGED is
dominantly project/contemporary-academic, not classical, so a flat tier comparison
would conflate scholarly era with citation hygiene).

Estimator: Beta-binomial Jeffreys posterior Beta(c+0.5, n-c+0.5).
Same protocol as findings/cross-finding/classical-modern-reliability-ratio.md (#127).
"""
import json
import math
import random
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260413
N_ITER = 20000
random.seed(SEED)

CORPUS = ROOT / 'findings/phase-c-structures/h-meta-1-corpus-120.tsv'

# Parse corpus, extract MW-6 tier from claim_source bracketed tag
TIER_RE = re.compile(r'\[([^]]+)\]')

def normalize_tier(raw):
    """First whitespace token of bracket content; preserve SECONDARY-TRIANGULATED."""
    parts = raw.strip().split()
    if not parts:
        return 'UNTAGGED'
    head = parts[0]
    if head == 'SECONDARY-TRIANGULATED':
        return 'SECONDARY-TRIANGULATED'
    return head  # VERIFIED, SECONDARY, PENDING, etc.

rows = []
with CORPUS.open() as fh:
    for line in fh:
        if line.startswith('#'):
            continue
        line = line.rstrip('\n')
        if not line:
            continue
        cols = line.split('\t')
        if cols[0] == 'claim_id':
            continue
        if len(cols) < 13:
            continue
        claim_id, claim_source, era = cols[0], cols[1], cols[2]
        verdict = cols[11]
        if not verdict:
            continue
        m = TIER_RE.search(claim_source)
        tier = normalize_tier(m.group(1)) if m else 'UNTAGGED'
        rows.append({
            'id': claim_id, 'source': claim_source, 'era': era,
            'verdict': verdict, 'tier': tier,
        })

# Restrict to classical-medieval era for clean tier comparison
classical = [r for r in rows if r['era'] == 'classical-medieval']

# Tier counts
def counts_by(rows_subset, key):
    d = defaultdict(lambda: {'CONFIRMED': 0, 'REFUTED': 0})
    for r in rows_subset:
        d[r[key]][r['verdict']] += 1
    return d

tier_counts = counts_by(classical, 'tier')

# Beta-binomial Jeffreys posterior sampler
def beta_sample(alpha, beta):
    # Use Marsaglia/Tsang gamma; for stability, use Python's random.gammavariate
    g1 = random.gammavariate(alpha, 1.0)
    g2 = random.gammavariate(beta, 1.0)
    return g1 / (g1 + g2)

def posterior_samples(c, n):
    a = c + 0.5
    b = (n - c) + 0.5
    return [beta_sample(a, b) for _ in range(N_ITER)]

def percentile(xs, q):
    s = sorted(xs)
    k = (len(s) - 1) * q
    f = math.floor(k); cl = math.ceil(k)
    if f == cl:
        return s[int(k)]
    return s[f] * (cl - k) + s[cl] * (k - f)

def summarize(samples):
    return {
        'mean': sum(samples) / len(samples),
        'median': percentile(samples, 0.5),
        'ci_low': percentile(samples, 0.025),
        'ci_high': percentile(samples, 0.975),
    }

# Per-tier posterior rates
tier_post = {}
for tier, cm in tier_counts.items():
    c = cm['CONFIRMED']; r = cm['REFUTED']; n = c + r
    if n == 0:
        continue
    samples = posterior_samples(c, n)
    s = summarize(samples)
    s.update({'n': n, 'confirmed': c, 'refuted': r, 'raw_rate': c/n if n else None})
    tier_post[tier] = s

# Cross-tier ratios: VERIFIED vs SECONDARY (the two largest non-trivial tiers)
def ratio_summary(num_samples, den_samples):
    ratios = [a/b if b > 0 else float('inf') for a, b in zip(num_samples, den_samples)]
    finite = [x for x in ratios if math.isfinite(x)]
    return {
        'median': percentile(finite, 0.5),
        'mean': sum(finite)/len(finite),
        'ci_low': percentile(finite, 0.025),
        'ci_high': percentile(finite, 0.975),
        'p_ratio_gt_1': sum(1 for x in finite if x > 1) / len(finite),
        'n_finite': len(finite),
    }

random.seed(SEED)  # Re-seed for reproducible cross-tier samples
tier_paired_samples = {}
for tier, cm in tier_counts.items():
    c = cm['CONFIRMED']; r = cm['REFUTED']; n = c + r
    if n == 0:
        continue
    tier_paired_samples[tier] = posterior_samples(c, n)

cross = {}
pairs_to_report = [
    ('VERIFIED', 'SECONDARY'),
    ('VERIFIED', 'PENDING'),
    ('SECONDARY', 'PENDING'),
    ('VERIFIED', 'SECONDARY-TRIANGULATED'),
]
for a, b in pairs_to_report:
    if a in tier_paired_samples and b in tier_paired_samples:
        cross[f'{a}_vs_{b}'] = ratio_summary(tier_paired_samples[a], tier_paired_samples[b])

# Sensitivity 1: collapse VERIFIED + SECONDARY-TRIANGULATED into "HIGH-CONFIDENCE"
hc_c = tier_counts['VERIFIED']['CONFIRMED'] + tier_counts['SECONDARY-TRIANGULATED']['CONFIRMED']
hc_r = tier_counts['VERIFIED']['REFUTED'] + tier_counts['SECONDARY-TRIANGULATED']['REFUTED']
random.seed(SEED + 1)
hc_samples = posterior_samples(hc_c, hc_c + hc_r)
hc_summary = summarize(hc_samples)
hc_summary.update({'n': hc_c + hc_r, 'confirmed': hc_c, 'refuted': hc_r,
                   'raw_rate': hc_c/(hc_c+hc_r) if hc_c+hc_r else None})

# Cross HIGH-CONFIDENCE vs SECONDARY
random.seed(SEED + 2)
hc_paired = posterior_samples(hc_c, hc_c + hc_r)
sec_paired = posterior_samples(tier_counts['SECONDARY']['CONFIRMED'],
                               tier_counts['SECONDARY']['CONFIRMED'] + tier_counts['SECONDARY']['REFUTED'])
hc_vs_sec = ratio_summary(hc_paired, sec_paired)

# Sensitivity 2: testability hypothesis check — what if we restrict to *specific*
# claims only (specificity >= 4)? Tests whether VERIFIED's lower rate is driven
# by VERIFIED claims being more specific/testable.
def parse_specificity(line_idx):
    return None  # placeholder, will reload corpus with specificity column

with CORPUS.open() as fh:
    spec_rows = []
    for line in fh:
        if line.startswith('#'):
            continue
        line = line.rstrip('\n')
        if not line:
            continue
        cols = line.split('\t')
        if cols[0] == 'claim_id':
            continue
        if len(cols) < 13:
            continue
        try:
            spec = int(cols[8])
        except ValueError:
            spec = None
        verdict = cols[11]
        if not verdict:
            continue
        m = TIER_RE.search(cols[1])
        tier = normalize_tier(m.group(1)) if m else 'UNTAGGED'
        spec_rows.append({
            'era': cols[2], 'tier': tier, 'verdict': verdict, 'specificity': spec,
        })

# Specificity distribution per tier (classical-medieval only)
spec_by_tier = defaultdict(list)
for r in spec_rows:
    if r['era'] != 'classical-medieval' or r['specificity'] is None:
        continue
    spec_by_tier[r['tier']].append(r['specificity'])

spec_means = {t: sum(v)/len(v) if v else None for t, v in spec_by_tier.items()}

# Restrict to specificity >= 4 and recompute tier rates
hi_spec = [r for r in spec_rows
           if r['era'] == 'classical-medieval' and (r['specificity'] or 0) >= 4]
hi_spec_counts = counts_by(hi_spec, 'tier')
random.seed(SEED + 3)
hi_spec_post = {}
for tier, cm in hi_spec_counts.items():
    c = cm['CONFIRMED']; r = cm['REFUTED']; n = c + r
    if n == 0:
        continue
    samples = posterior_samples(c, n)
    s = summarize(samples)
    s.update({'n': n, 'confirmed': c, 'refuted': r, 'raw_rate': c/n})
    hi_spec_post[tier] = s

# Sensitivity 3: drop classical UNTAGGED (only 2 rows, both REFUTED — outliers)
# Already handled by tier separation; report explicitly.

# Sensitivity 4: substance_type stratification — does the inversion hold within
# structural-formal claims only (excluding numerical-gematric)?
with CORPUS.open() as fh:
    subst_rows = []
    for line in fh:
        if line.startswith('#'):
            continue
        line = line.rstrip('\n')
        if not line:
            continue
        cols = line.split('\t')
        if cols[0] == 'claim_id' or len(cols) < 13:
            continue
        verdict = cols[11]
        if not verdict:
            continue
        m = TIER_RE.search(cols[1])
        tier = normalize_tier(m.group(1)) if m else 'UNTAGGED'
        subst_rows.append({
            'era': cols[2], 'tier': tier, 'verdict': verdict,
            'substance_type': cols[10],
        })

structural = [r for r in subst_rows
              if r['era'] == 'classical-medieval' and r['substance_type'] == 'structural-formal']
struct_counts = counts_by(structural, 'tier')
random.seed(SEED + 4)
struct_post = {}
for tier, cm in struct_counts.items():
    c = cm['CONFIRMED']; r = cm['REFUTED']; n = c + r
    if n == 0:
        continue
    samples = posterior_samples(c, n)
    s = summarize(samples)
    s.update({'n': n, 'confirmed': c, 'refuted': r, 'raw_rate': c/n})
    struct_post[tier] = s

# Output
out = {
    'meta': {
        'seed': SEED,
        'n_iter': N_ITER,
        'estimator': 'Beta-binomial Jeffreys posterior Beta(c+0.5, n-c+0.5)',
        'restriction': 'classical-medieval era only (avoids era×tier confound)',
        'rules_tuple': '(no-tashkeel, orthographic-token & lemma, graphemes, basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)',
    },
    'tier_counts_classical': {t: dict(cm) for t, cm in tier_counts.items()},
    'tier_posterior_rates': tier_post,
    'cross_tier_ratios': cross,
    'sensitivity_S1_high_confidence_collapsed': {
        'definition': 'VERIFIED + SECONDARY-TRIANGULATED merged into HIGH-CONFIDENCE',
        'high_confidence_rate': hc_summary,
        'high_confidence_vs_secondary_ratio': hc_vs_sec,
    },
    'sensitivity_S2_specificity_geq_4': {
        'definition': 'restrict to specificity >= 4 (more-testable claims only)',
        'tier_posterior_rates': hi_spec_post,
        'tier_specificity_means_classical': spec_means,
    },
    'sensitivity_S3_structural_formal_only': {
        'definition': 'restrict to substance_type=structural-formal (drops numerical-gematric)',
        'tier_posterior_rates': struct_post,
    },
}

outp = ROOT / 'findings/cross-finding/csv/mw6-reliability-moderator.json'
outp.parent.mkdir(parents=True, exist_ok=True)
outp.write_text(json.dumps(out, indent=2, default=str))

# Console summary
def fmt(s):
    if s is None: return '—'
    return f"{s:.3f}"

print(f"== MW-6 reliability moderator ==")
print(f"Seed: {SEED} | n_iter: {N_ITER} | restriction: classical-medieval only")
print()
print(f"{'tier':<25} {'n':>4} {'C':>3} {'R':>3} {'raw':>8} {'mean':>8} {'95% CrI':>22}")
for tier in ['VERIFIED', 'SECONDARY-TRIANGULATED', 'SECONDARY', 'PENDING', 'UNTAGGED']:
    if tier not in tier_post:
        continue
    s = tier_post[tier]
    ci = f"[{fmt(s['ci_low'])}, {fmt(s['ci_high'])}]"
    print(f"{tier:<25} {s['n']:>4} {s['confirmed']:>3} {s['refuted']:>3} {fmt(s['raw_rate']):>8} {fmt(s['mean']):>8} {ci:>22}")

print()
print(f"S1 HIGH-CONFIDENCE collapsed (VERIFIED+S-T):")
s = hc_summary
print(f"  n={s['n']} C={s['confirmed']} R={s['refuted']} raw={fmt(s['raw_rate'])} mean={fmt(s['mean'])} CrI=[{fmt(s['ci_low'])}, {fmt(s['ci_high'])}]")
r = hc_vs_sec
print(f"  HC vs SECONDARY ratio: median={fmt(r['median'])} CrI=[{fmt(r['ci_low'])}, {fmt(r['ci_high'])}] P(ratio>1)={r['p_ratio_gt_1']:.3f}")

print()
print(f"Cross-tier ratios:")
for k, r in cross.items():
    print(f"  {k}: median={fmt(r['median'])} CrI=[{fmt(r['ci_low'])}, {fmt(r['ci_high'])}] P(>1)={r['p_ratio_gt_1']:.3f}")

print()
print(f"S2 specificity>=4 tier rates (testability check):")
for tier in ['VERIFIED', 'SECONDARY-TRIANGULATED', 'SECONDARY', 'PENDING']:
    if tier not in hi_spec_post: continue
    s = hi_spec_post[tier]
    print(f"  {tier:<25} n={s['n']:>3} raw={fmt(s['raw_rate'])} mean={fmt(s['mean'])} CrI=[{fmt(s['ci_low'])}, {fmt(s['ci_high'])}]")
print(f"  Specificity means by tier: {spec_means}")

print()
print(f"S3 structural-formal only tier rates:")
for tier in ['VERIFIED', 'SECONDARY-TRIANGULATED', 'SECONDARY', 'PENDING']:
    if tier not in struct_post: continue
    s = struct_post[tier]
    print(f"  {tier:<25} n={s['n']:>3} raw={fmt(s['raw_rate'])} mean={fmt(s['mean'])} CrI=[{fmt(s['ci_low'])}, {fmt(s['ci_high'])}]")

print()
print(f"Output: {outp}")
