#!/usr/bin/env python3
"""H-CLASSIC-47 — al-Biqāʿī verse-pair within-surah seam-Jaccard.

Pre-reg: findings/phase-b-hypotheses/h-classic-47-prereg.md
Spec:    findings/phase-b-hypotheses/h-classic-44-to-49-spec.md §H-CLASSIC-47

Tests al-Biqāʿī's verse-pair-within-surah munāsaba claim at the
4 priority Medinan surahs (Q 2, 3, 4, 5) where his commentary is
most explicit, with a 4-surah Meccan negative control (Q 6, 7, 26, 37).

Pre-registered:
  - Distance-1 mean root-Jaccard, two stopword conditions
    (with-stopwords / without-stopwords).
  - Per-surah within-surah verse-order permutation null (10,000 perms).
  - PASS rule: ≥ 3/4 priority surahs exceed per-surah 99th pctile
    in BOTH stopword conditions.
  - Negative control: ≤ 1/4 control surahs pass in either condition.

Bonferroni k=6, α_bon = 0.0083. Seed 20260414.
"""

import json
import random
import re
import statistics
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260414

PRIORITY_SURAHS = [2, 3, 4, 5]
CONTROL_SURAHS = [6, 7, 26, 37]
ALL_SURAHS = PRIORITY_SURAHS + CONTROL_SURAHS

# Locked stopword roots (per pre-reg)
STOPWORD_ROOTS = {'Alh', 'kwn', 'qwl', 'Eml', 'Amn', 'llh', 'xlq', 'Erf'}

LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')


# ---- Load QAC morphology, build per-verse root sets ----
print(f"[load] parsing QAC morphology...", file=sys.stderr)
verse_roots = defaultdict(set)  # (sid, vid) -> set of root strings

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
        sid, vid = int(m.group(1)), int(m.group(2))
        feat = parts[3]
        if 'STEM' not in feat:
            continue
        rm = ROOT_RE.search(feat)
        if rm:
            verse_roots[(sid, vid)].add(rm.group(1))

print(f"[load] {len(verse_roots)} verses with at least one rooted token",
      file=sys.stderr)

# Build per-surah verse-root-set lists in mushaf order
def surah_verse_root_lists(sid, strip_stopwords=False):
    verses = sorted([(vid, roots) for (s, vid), roots in verse_roots.items()
                      if s == sid], key=lambda x: x[0])
    if strip_stopwords:
        return [r - STOPWORD_ROOTS for vid, r in verses]
    return [r for vid, r in verses]


# Verify counts match Quran JSON for sanity
Q = json.loads((ROOT / 'quran-text/quran-no-tashkeel.json').read_text())
quran_counts = {s['id']: len(s['verses']) for s in Q}
for sid in ALL_SURAHS:
    qac_count = sum(1 for (s, vid) in verse_roots if s == sid)
    print(f"  Q{sid}: QAC rooted verses={qac_count}, "
          f"Quran JSON verses={quran_counts[sid]}", file=sys.stderr)


# ---- Jaccard helpers ----
def jaccard(a, b):
    """Set Jaccard. Returns None if both sets are empty."""
    if not a and not b:
        return None
    return len(a & b) / len(a | b)


def mean_jaccard_at_distance(seq, k):
    """Mean Jaccard for all pairs (i, i+k) in a list of root sets."""
    vals = []
    for i in range(len(seq) - k):
        j = jaccard(seq[i], seq[i + k])
        if j is not None:
            vals.append(j)
    return statistics.mean(vals) if vals else 0.0


def bucket_means(seq, buckets=((1, 1), (2, 2), (3, 5), (6, 10), (11, 999))):
    """Mean Jaccard per distance bucket. Returns dict {bucket_label: mean}."""
    out = {}
    n = len(seq)
    for lo, hi in buckets:
        vals = []
        for i in range(n):
            for j in range(i + max(1, lo), min(n, i + hi + 1)):
                d = j - i
                if d < lo or d > hi:
                    continue
                jc = jaccard(seq[i], seq[j])
                if jc is not None:
                    vals.append(jc)
        label = f'{lo}-{hi}' if lo != hi else str(lo)
        if hi >= 999:
            label = f'{lo}+'
        out[label] = statistics.mean(vals) if vals else 0.0
    return out


# ---- Per-surah within-surah verse-order permutation null at distance 1 ----
N_PERM = 10_000


def permutation_null_dist1(seq, n_perm, rng):
    """Returns (observed_mean, null_99pct, null_distribution)."""
    obs = mean_jaccard_at_distance(seq, 1)
    nulls = []
    indices = list(range(len(seq)))
    for _ in range(n_perm):
        rng.shuffle(indices)
        permuted = [seq[i] for i in indices]
        nulls.append(mean_jaccard_at_distance(permuted, 1))
    nulls.sort()
    pct99 = nulls[int(0.99 * len(nulls))]
    return obs, pct99, nulls


# ---- Run primary + secondary + tertiary ----
def run_surah(sid, label, sub_seed_offset):
    print(f"\n[{label}] Q{sid} processing...", file=sys.stderr)
    out_surah = {'sid': sid, 'label': label}

    for cond_label, strip_stop in [('with_stopwords', False),
                                     ('without_stopwords', True)]:
        seq = surah_verse_root_lists(sid, strip_stopwords=strip_stop)
        n = len(seq)

        # Bucket means (descriptive)
        buckets = bucket_means(seq)

        # Permutation null at distance 1
        rng = random.Random(SEED + sub_seed_offset)
        obs, pct99, nulls = permutation_null_dist1(seq, N_PERM, rng)

        passes = obs > pct99
        empirical_p = sum(1 for x in nulls if x >= obs) / len(nulls)
        null_mean = statistics.mean(nulls)
        null_sd = statistics.stdev(nulls)
        z = (obs - null_mean) / null_sd if null_sd > 0 else 0.0

        out_surah[cond_label] = {
            'n_verses': n,
            'observed_dist1_jaccard': obs,
            'null_99pct': pct99,
            'null_mean': null_mean,
            'null_sd': null_sd,
            'z_score': z,
            'empirical_p_one_sided': empirical_p,
            'passes': passes,
            'bucket_means': buckets,
        }
        marker = 'PASS' if passes else 'FAIL'
        print(f"  [{cond_label}] obs={obs:.4f}, 99pct={pct99:.4f}, "
              f"z={z:+.2f}, p_emp={empirical_p:.4f}, {marker}", file=sys.stderr)
        print(f"  [{cond_label}] buckets: " +
              ", ".join(f"{k}={v:.3f}" for k, v in buckets.items()),
              file=sys.stderr)

    return out_surah


# Run priority surahs
priority_results = {}
for offset, sid in enumerate(PRIORITY_SURAHS):
    priority_results[sid] = run_surah(sid, 'priority', offset)

# Run control surahs
control_results = {}
for offset, sid in enumerate(CONTROL_SURAHS):
    control_results[sid] = run_surah(sid, 'control', offset + 100)

# ---- Pass counts ----
def count_passes(results, condition):
    return sum(1 for sid, r in results.items() if r[condition]['passes'])


priority_with = count_passes(priority_results, 'with_stopwords')
priority_without = count_passes(priority_results, 'without_stopwords')
control_with = count_passes(control_results, 'with_stopwords')
control_without = count_passes(control_results, 'without_stopwords')

print(f"\n=== PASS COUNTS ===", file=sys.stderr)
print(f"Priority surahs (Q 2/3/4/5):", file=sys.stderr)
print(f"  with-stopwords:    {priority_with}/4", file=sys.stderr)
print(f"  without-stopwords: {priority_without}/4", file=sys.stderr)
print(f"Control surahs (Q 6/7/26/37):", file=sys.stderr)
print(f"  with-stopwords:    {control_with}/4", file=sys.stderr)
print(f"  without-stopwords: {control_without}/4", file=sys.stderr)


# ---- Verdict routing ----
primary_pass_with = priority_with >= 3
primary_pass_without = priority_without >= 3
primary_pass_both = primary_pass_with and primary_pass_without
control_clean_with = control_with <= 1
control_clean_without = control_without <= 1
control_clean_both = control_clean_with and control_clean_without

if primary_pass_both and control_clean_both:
    final_verdict = 'PASS — al-Biqāʿī verse-pair seam-Jaccard confirmed'
elif primary_pass_both and not control_clean_both:
    final_verdict = ('PARTIAL — verse-pair effect is real but generalizes '
                     'beyond priority surahs (not specifically Medinan-Biqāʿī)')
elif primary_pass_with and not primary_pass_without:
    final_verdict = ('PARTIAL-DECONFOUNDED — effect is driven by formulaic / '
                     'divine-name repetition, not semantic munāsaba '
                     '(without-stopwords FAILS)')
elif (not primary_pass_with) and primary_pass_without:
    final_verdict = ('UNUSUAL — without-stopwords passes but with-stopwords '
                     'does not. Inspect manually.')
else:
    final_verdict = ('NULL — al-Biqāʿī adjacent-verse seam-density falsified '
                     'at verse-pair scale')

print(f"\n=== FINAL VERDICT ===", file=sys.stderr)
print(f"  {final_verdict}", file=sys.stderr)

# ---- Write JSON output ----
def serialize_results(results):
    out = {}
    for sid, r in results.items():
        out[str(sid)] = {
            'sid': sid,
            'label': r['label'],
            'with_stopwords': r['with_stopwords'],
            'without_stopwords': r['without_stopwords'],
        }
    return out


out = {
    'finding_id': 'h-classic-47',
    'pre_reg': 'findings/phase-b-hypotheses/h-classic-47-prereg.md',
    'pre_reg_compliance': 'PRE-REG-STANDARD-04',
    'rules_tuple': '(no-tashkeel, root-level via QAC, hafs-kufan, mashriqi)',
    'seed': SEED,
    'priority_surahs': PRIORITY_SURAHS,
    'control_surahs': CONTROL_SURAHS,
    'stopword_roots': sorted(STOPWORD_ROOTS),
    'n_perm': N_PERM,
    'bonferroni_k': 6,
    'alpha_bon': 0.0083,
    'sided_test': 'one-sided positive',
    'priority_results': serialize_results(priority_results),
    'control_results': serialize_results(control_results),
    'pass_counts': {
        'priority_with_stopwords': priority_with,
        'priority_without_stopwords': priority_without,
        'control_with_stopwords': control_with,
        'control_without_stopwords': control_without,
    },
    'verdict_routing': {
        'primary_pass_with_stopwords': primary_pass_with,
        'primary_pass_without_stopwords': primary_pass_without,
        'primary_pass_both': primary_pass_both,
        'control_clean_with_stopwords': control_clean_with,
        'control_clean_without_stopwords': control_clean_without,
        'control_clean_both': control_clean_both,
    },
    'final_verdict': final_verdict,
    'no_fork_protections_honored': [
        'priority surahs LOCKED to Q 2, 3, 4, 5',
        'control surahs LOCKED to Q 6, 7, 26, 37',
        'distance-1 LOCKED as primary scale',
        f'stopword list LOCKED to {sorted(STOPWORD_ROOTS)}',
        f'permutation null seed {SEED}, 10000 within-surah perms per surah',
        'pass rule LOCKED to >= 3/4 priority surahs (both stopword conditions)',
        'root extraction LOCKED to QAC v0.4 STEM-only',
    ],
    'data_reuse_disclosed': (
        'Reuses QAC morphology loader pattern (LOC_RE, ROOT_RE, STEM filter) '
        'from scripts/h_new_29_root_cv.py. Reuses '
        'data/morphology/quranic-corpus-morphology-0.4.txt and '
        'quran-text/quran-no-tashkeel.json (verse count sanity check only). '
        'No reuse of T-002 / task #21 (different scale: '
        'verse-pair-within-surah, not surah-pair-cross-surah).'
    ),
}

out_path = ROOT / 'findings/phase-b-hypotheses/csv/h-classic-47.json'
out_path.write_text(json.dumps(out, indent=2, default=str))
print(f"\n[output] saved: {out_path}", file=sys.stderr)
