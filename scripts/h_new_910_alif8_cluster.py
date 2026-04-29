#!/usr/bin/env python3
"""
H-NEW-910 — Alif-8 cluster cohesion test (Bonferroni-5).

Pre-registered. Direction LOCKED. Seed=20260428.

Pre-reg path: findings/phase-b-hypotheses/h-new-910-alif8-cluster-prereg.md
Pre-reg SHA256: d3f08bada8705b2654810c0ffb89fc51de6970f7f22916e56dc1de6266f84fb9

Reads:
  - findings/phase-b-hypotheses/csv/h-new-111.json   (FR distance matrix)
  - findings/phase-b-hypotheses/csv/h-new-700.json   (rhyme/phoneme diagnostics)
  - quran-text/quran-min-tashkeel.json               (last-letter cluster verification + rhyme entropy)
  - quran-text/quran-no-tashkeel.json                (per-surah words/verses)
  - quran-text/quran-full-tashkeel.json              (phoneme density)
  - data/revelation-order.csv                        (al-Suyūṭī chronology)
  - data/hafs-verse-counts.tsv                       (verse counts)

Writes:
  - findings/phase-b-hypotheses/csv/h-new-910-alif8-cluster.json

No external deps (stdlib only).
"""

import csv
import hashlib
import itertools
import json
import math
import random
import sys
import time
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-910-alif8-cluster-prereg.md"
PREREG_SHA = "d3f08bada8705b2654810c0ffb89fc51de6970f7f22916e56dc1de6266f84fb9"
SEED = 20260428
N_PERMS = 10000
ALPHA_BON = 0.01
ALPHA_DIR = 0.1667

CLUSTER = [18, 48, 65, 72, 76, 87, 91, 92]
ALIF_FINALS = set(['ا', 'آ', 'أ', 'إ', 'ى', 'ٰ'])

# Tashkeel marks (excludes dagger-alif U+0670 because Q033-F-01 treats ٰ as alif-final).
TASHKEEL_NO_DAGGER = set([
    'ً','ٌ','ٍ','َ','ُ','ِ','ّ','ْ','ٓ','ٔ','ٕ',
    'ۖ','ۗ','ۘ','ۙ','ۚ','ۛ','ۜ','۟','۠','ۢ','ۣ','ۥ','ۦ','ۨ','۪','۫','۬','ۭ'
])

# Phoneme classes (orthographic-grapheme proxy; project default).
EMPHATIC = set(['ص','ض','ط','ظ'])
PHARYNGEAL = set(['ح','ع'])
SIBILANT = set(['س','ش','ز','ص','ث','ذ'])  # broader sibilant class
GLOTTAL = set(['ء','ه','أ','إ','آ','ؤ','ئ'])


def verify_sha():
    h = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if h != PREREG_SHA:
        print(f"FATAL: SHA256 mismatch.\n  expected {PREREG_SHA}\n  got      {h}", file=sys.stderr)
        sys.exit(1)
    print(f"[ok] pre-reg SHA verified: {h}")


def strip_diacritics(s):
    return ''.join(c for c in s if c not in TASHKEEL_NO_DAGGER)


def last_letter(verse_text):
    s = strip_diacritics(verse_text)
    s = s.rstrip(' .،؛؟!ــ')
    if not s:
        return None
    return s[-1]


def load_text(name):
    return json.loads((ROOT / "quran-text" / name).read_text())


def load_fr_matrix():
    """Returns 114x114 symmetric Fisher-Rao distance matrix (1-indexed)."""
    d = json.loads((ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json").read_text())
    M = [[0.0] * 115 for _ in range(115)]  # 1-indexed
    for i, j, v in d['D_matrix_upper_triangular']:
        M[i][j] = float(v)
        M[j][i] = float(v)
    return M


def load_rhyme_phoneme_diagnostics():
    """Per-surah summaries from h-new-700.json's rhyme_letter_diagnostics."""
    d = json.loads((ROOT / "findings/phase-b-hypotheses/csv/h-new-700.json").read_text())
    diag = d['rhyme']['rhyme_letter_diagnostics']
    out = {e['surah']: {'top_letter': e['top_letter'], 'frac': e['frac'], 'n_verses': e['n_verses']} for e in diag}
    return out


def load_revelation_order():
    out = {}
    with (ROOT / "data/revelation-order.csv").open() as f:
        for row in csv.DictReader(f):
            out[int(row['mushaf_order'])] = int(row['revelation_order'])
    return out


def load_verse_counts():
    out = {}
    with (ROOT / "data/hafs-verse-counts.tsv").open() as f:
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                out[int(parts[0])] = int(parts[1])
    return out


# ---------- Cluster verification ----------

def verify_cluster(min_tashkeel):
    """Re-derive 100%-alif-final cluster; abort if it differs from {18,48,65,72,76,87,91,92}."""
    rates = []
    for surah in min_tashkeel:
        sid = surah['id']
        verses = surah['verses']
        n = 0; alif = 0
        for v in verses:
            ll = last_letter(v['text'])
            if ll is None: continue
            n += 1
            if ll in ALIF_FINALS: alif += 1
        rate = alif / n if n else 0
        rates.append((sid, rate, alif, n))
    perfect = sorted([r[0] for r in rates if r[1] >= 0.99999])
    if perfect != CLUSTER:
        print(f"FATAL: cluster mismatch. expected {CLUSTER}, got {perfect}", file=sys.stderr)
        sys.exit(2)
    print(f"[ok] cluster verified: {perfect}")
    return rates


# ---------- H1: FR-roots cohesion ----------

def mean_pairwise(items, dist):
    n = len(items); s = 0.0; c = 0
    for i in range(n):
        for j in range(i+1, n):
            s += dist(items[i], items[j])
            c += 1
    return s / c if c else 0.0


def perm_test_lower_tail(observed, items_population, k, dist, n_perms, seed):
    rng = random.Random(seed)
    lower_or_equal = 0
    null_vals = []
    for _ in range(n_perms):
        sample = rng.sample(items_population, k)
        v = mean_pairwise(sample, dist)
        null_vals.append(v)
        if v <= observed:
            lower_or_equal += 1
    pct = lower_or_equal / n_perms
    null_mean = sum(null_vals) / len(null_vals)
    null_std = (sum((x - null_mean)**2 for x in null_vals) / len(null_vals)) ** 0.5
    return pct, null_mean, null_std, null_vals


def H1_fr_roots(M):
    pop = list(range(1, 115))
    obs = mean_pairwise(CLUSTER, lambda a, b: M[a][b])
    pct, null_mean, null_std, _ = perm_test_lower_tail(
        obs, pop, len(CLUSTER), lambda a, b: M[a][b], N_PERMS, SEED)
    return {
        'observed': obs,
        'percentile': pct,
        'null_mean': null_mean,
        'null_std': null_std,
        'effect_z': (obs - null_mean) / null_std if null_std > 0 else None,
        'gate_strict': pct <= ALPHA_BON,
        'gate_directional': pct <= ALPHA_DIR,
        'verdict': verdict_from_pct(pct),
    }


def verdict_from_pct(pct):
    if pct <= ALPHA_BON: return "VINDICATED"
    if pct <= ALPHA_DIR: return "DIRECTIONAL"
    return "NULL"


# ---------- H2: verse-count chi² + permutation ----------

def H2_verse_count(verse_counts):
    buckets = [(1,20), (21,50), (51,100), (101,200), (201,10000)]
    def bucket(n):
        for i, (lo, hi) in enumerate(buckets):
            if lo <= n <= hi: return i
        return None
    cluster_counts = [verse_counts[s] for s in CLUSTER]
    cluster_buckets = [bucket(n) for n in cluster_counts]
    obs_freq = [cluster_buckets.count(i) for i in range(5)]
    # corpus-baseline (114 surahs)
    corpus_buckets = [bucket(verse_counts[s]) for s in range(1,115)]
    corpus_freq = [corpus_buckets.count(i) for i in range(5)]
    expected = [8 * (corpus_freq[i] / 114) for i in range(5)]
    # Yates-corrected chi² with floor on expected
    chi2 = 0.0
    for o, e in zip(obs_freq, expected):
        if e > 0:
            chi2 += (o - e) ** 2 / e
    df = 4
    # permutation p-value (more robust for small N=8)
    rng = random.Random(SEED + 2)
    extreme = 0
    for _ in range(N_PERMS):
        sample = rng.sample(range(1,115), 8)
        s_buckets = [bucket(verse_counts[s]) for s in sample]
        s_freq = [s_buckets.count(i) for i in range(5)]
        c2 = 0.0
        for o, e in zip(s_freq, expected):
            if e > 0:
                c2 += (o - e) ** 2 / e
        if c2 >= chi2: extreme += 1
    pct = extreme / N_PERMS
    # also check pre-locked direction: short+medium concentration
    short_med_count = obs_freq[0] + obs_freq[1]
    direction_ok = short_med_count >= 6  # pre-committed: ≥6 of 8 short-medium
    return {
        'cluster_buckets': obs_freq,
        'corpus_buckets': corpus_freq,
        'expected_under_corpus': expected,
        'chi2': chi2,
        'df': df,
        'perm_p_chi2_geq_obs': pct,
        'short_med_count': short_med_count,
        'direction_locked_satisfied': direction_ok,
        'verdict': verdict_from_pct(pct),
    }


# ---------- H3: revelation-order cohesion ----------

def H3_chronology(rev_order):
    obs = mean_pairwise(CLUSTER, lambda a, b: abs(rev_order[a] - rev_order[b]))
    pct, null_mean, null_std, _ = perm_test_lower_tail(
        obs, list(range(1,115)), len(CLUSTER),
        lambda a, b: abs(rev_order[a] - rev_order[b]), N_PERMS, SEED + 3)
    return {
        'observed': obs,
        'percentile': pct,
        'null_mean': null_mean,
        'null_std': null_std,
        'effect_z': (obs - null_mean) / null_std if null_std > 0 else None,
        'cluster_rev_orders': {s: rev_order[s] for s in CLUSTER},
        'gate_strict': pct <= ALPHA_BON,
        'gate_directional': pct <= ALPHA_DIR,
        'verdict': verdict_from_pct(pct),
    }


# ---------- H4: mushaf-position cohesion ----------

def H4_mushaf():
    obs = mean_pairwise(CLUSTER, lambda a, b: abs(a - b))
    pct, null_mean, null_std, _ = perm_test_lower_tail(
        obs, list(range(1,115)), len(CLUSTER),
        lambda a, b: abs(a - b), N_PERMS, SEED + 4)
    return {
        'observed': obs,
        'percentile': pct,
        'null_mean': null_mean,
        'null_std': null_std,
        'effect_z': (obs - null_mean) / null_std if null_std > 0 else None,
        'gate_strict': pct <= ALPHA_BON,
        'gate_directional': pct <= ALPHA_DIR,
        'verdict': verdict_from_pct(pct),
    }


# ---------- H5: 4-axis composite cohesion ----------

def per_surah_axes(no_tashkeel, min_tashkeel, full_tashkeel, M):
    """Compute per-surah single-value summaries on 4 axes."""
    axes = {s: {} for s in range(1,115)}

    # content axis: mean FR distance from surah s to all other surahs (centroid-distance proxy)
    for s in range(1,115):
        vals = [M[s][t] for t in range(1,115) if t != s]
        axes[s]['content'] = sum(vals) / len(vals)

    # rhyme axis: Shannon entropy of last-letter distribution (lower = monorhyme)
    for surah in min_tashkeel:
        sid = surah['id']
        from collections import Counter
        lc = Counter()
        for v in surah['verses']:
            ll = last_letter(v['text'])
            if ll is not None:
                lc[ll] += 1
        n = sum(lc.values())
        if n == 0:
            axes[sid]['rhyme'] = 0.0
        else:
            H = 0.0
            for c in lc.values():
                p = c / n
                H -= p * math.log2(p) if p > 0 else 0
            axes[sid]['rhyme'] = H

    # phoneme axis: emphatic+pharyngeal density per total non-space chars
    for surah in full_tashkeel:
        sid = surah['id']
        total = 0; emph = 0; phar = 0; sib = 0; glot = 0
        for v in surah['verses']:
            for c in v['text']:
                if c in TASHKEEL_NO_DAGGER or c == 'ٰ' or c.isspace():
                    continue
                total += 1
                if c in EMPHATIC: emph += 1
                if c in PHARYNGEAL: phar += 1
                if c in SIBILANT: sib += 1
                if c in GLOTTAL: glot += 1
        denom = total if total else 1
        axes[sid]['phoneme'] = (emph + phar + sib + glot) / denom

    # verse-len axis: words per verse (mean)
    for surah in no_tashkeel:
        sid = surah['id']
        n_v = 0; n_w = 0
        for v in surah['verses']:
            n_v += 1
            n_w += len(v['text'].split())
        axes[sid]['verse_len_words'] = n_w / n_v if n_v else 0
    return axes


def H5_composite(axes):
    """Sum of within-cluster mean pairwise abs-diff across 4 axes (z-normed)."""
    keys = ['content', 'rhyme', 'phoneme', 'verse_len_words']
    # corpus stats per axis
    stats = {}
    for k in keys:
        vals = [axes[s][k] for s in range(1,115)]
        m = sum(vals)/len(vals)
        sd = (sum((x-m)**2 for x in vals)/len(vals))**0.5
        stats[k] = (m, sd if sd > 0 else 1.0)

    def composite(items):
        total = 0.0
        for k in keys:
            d = mean_pairwise(items, lambda a,b: abs(axes[a][k]-axes[b][k]))
            total += d / stats[k][1]
        return total

    obs = composite(CLUSTER)
    rng = random.Random(SEED + 5)
    nulls = []
    le = 0
    for _ in range(N_PERMS):
        sample = rng.sample(range(1,115), 8)
        v = composite(sample)
        nulls.append(v)
        if v <= obs: le += 1
    pct = le / N_PERMS
    null_mean = sum(nulls)/len(nulls)
    null_std = (sum((x-null_mean)**2 for x in nulls)/len(nulls))**0.5

    # also report per-axis individual within-cluster pairwise mean for transparency
    per_axis_obs = {}
    per_axis_pct = {}
    rng2 = random.Random(SEED + 6)
    null_per = {k: [] for k in keys}
    for _ in range(N_PERMS):
        sample = rng2.sample(range(1,115), 8)
        for k in keys:
            null_per[k].append(mean_pairwise(sample, lambda a,b: abs(axes[a][k]-axes[b][k])))
    for k in keys:
        ov = mean_pairwise(CLUSTER, lambda a,b: abs(axes[a][k]-axes[b][k]))
        per_axis_obs[k] = ov
        per_axis_pct[k] = sum(1 for v in null_per[k] if v <= ov) / N_PERMS

    return {
        'observed_composite': obs,
        'percentile': pct,
        'null_mean': null_mean,
        'null_std': null_std,
        'effect_z': (obs - null_mean) / null_std if null_std > 0 else None,
        'per_axis_within_cluster_mean': per_axis_obs,
        'per_axis_percentile': per_axis_pct,
        'corpus_stats': {k: {'mean': stats[k][0], 'std': stats[k][1]} for k in keys},
        'gate_strict': pct <= ALPHA_BON,
        'gate_directional': pct <= ALPHA_DIR,
        'verdict': verdict_from_pct(pct),
    }


# ---------- COMPARATOR-16 (post-hoc, capped) ----------

def comparator_16(M, rev_order, axes, verse_counts, rates_data):
    # next 8 surahs after the 8 perfect by rate (descending), excluding the 8.
    # rates_data is list of (sid, rate, alif, n)
    above = sorted([r for r in rates_data if 0.97 <= r[1] < 0.99999], key=lambda r: -r[1])
    extra = [r[0] for r in above[:8]]
    cluster16 = sorted(CLUSTER + extra)

    obs_fr = mean_pairwise(cluster16, lambda a, b: M[a][b])
    rng = random.Random(SEED + 16)
    le = 0; nulls = []
    for _ in range(N_PERMS):
        sample = rng.sample(range(1,115), 16)
        v = mean_pairwise(sample, lambda a, b: M[a][b])
        nulls.append(v)
        if v <= obs_fr: le += 1
    pct_fr = le / N_PERMS
    null_mean = sum(nulls)/len(nulls)
    null_std = (sum((x-null_mean)**2 for x in nulls)/len(nulls))**0.5

    obs_rev = mean_pairwise(cluster16, lambda a, b: abs(rev_order[a]-rev_order[b]))
    rng = random.Random(SEED + 17)
    le = 0
    for _ in range(N_PERMS):
        sample = rng.sample(range(1,115), 16)
        v = mean_pairwise(sample, lambda a, b: abs(rev_order[a]-rev_order[b]))
        if v <= obs_rev: le += 1
    pct_rev = le / N_PERMS

    obs_mu = mean_pairwise(cluster16, lambda a, b: abs(a-b))
    rng = random.Random(SEED + 18)
    le = 0
    for _ in range(N_PERMS):
        sample = rng.sample(range(1,115), 16)
        v = mean_pairwise(sample, lambda a, b: abs(a-b))
        if v <= obs_mu: le += 1
    pct_mu = le / N_PERMS

    return {
        'extra_8_added': extra,
        'extra_8_alif_rates': {r[0]: r[1] for r in above[:8]},
        'cluster16': cluster16,
        'fr_observed': obs_fr,
        'fr_null_mean': null_mean,
        'fr_null_std': null_std,
        'fr_percentile': pct_fr,
        'fr_verdict_capped_alpha_05': "DIRECTIONAL" if pct_fr <= 0.05 else "NULL",
        'rev_observed': obs_rev,
        'rev_percentile': pct_rev,
        'mushaf_observed': obs_mu,
        'mushaf_percentile': pct_mu,
        'note': "POST-HOC; single-test α=0.05 ceiling per Protocol §1.7 (MW-7).",
    }


# ---------- SUB-CLUSTER (Meccan-short tail) ----------

def sub_cluster_mushaf_tail(M, rev_order):
    sub = [s for s in CLUSTER if s >= 75]
    if len(sub) < 3:
        return {'note': 'sub-cluster too small'}
    obs_fr = mean_pairwise(sub, lambda a, b: M[a][b])
    rng = random.Random(SEED + 7)
    le = 0; nulls = []
    for _ in range(N_PERMS):
        sample = rng.sample(range(1,115), len(sub))
        v = mean_pairwise(sample, lambda a, b: M[a][b])
        nulls.append(v)
        if v <= obs_fr: le += 1
    pct = le / N_PERMS

    obs_mu = mean_pairwise(sub, lambda a, b: abs(a-b))
    rng = random.Random(SEED + 8)
    le2 = 0
    for _ in range(N_PERMS):
        sample = rng.sample(range(1,115), len(sub))
        v = mean_pairwise(sample, lambda a, b: abs(a-b))
        if v <= obs_mu: le2 += 1
    pct_mu = le2 / N_PERMS

    return {
        'sub_cluster': sub,
        'fr_observed': obs_fr,
        'fr_percentile': pct,
        'mushaf_observed': obs_mu,
        'mushaf_percentile': pct_mu,
        'note': "POST-HOC; single-test α=0.05 ceiling.",
    }


# ---------- RULES-TUPLE-VARIANT: no-tashkeel last-letter, no dagger-alif in alif-set ----------

def rules_variant_no_dagger(min_tashkeel, no_tashkeel):
    """Re-derive cluster excluding ٰ (dagger-alif) from alif-set, see if 8-cluster survives."""
    alif_set_strict = set(['ا', 'آ', 'أ', 'إ', 'ى'])  # no ٰ
    rates = []
    for surah in min_tashkeel:
        sid = surah['id']
        n = 0; alif = 0
        for v in surah['verses']:
            ll = last_letter(v['text'])
            if ll is None: continue
            n += 1
            if ll in alif_set_strict: alif += 1
        rate = alif / n if n else 0
        rates.append((sid, rate, alif, n))
    perfect_strict = sorted([r[0] for r in rates if r[1] >= 0.99999])

    # Also: full-tashkeel-strip + last-letter (more aggressive normalization)
    rates2 = []
    full_no_dia = set(TASHKEEL_NO_DAGGER) | {'ٰ'}
    for surah in no_tashkeel:
        sid = surah['id']
        n = 0; alif = 0
        for v in surah['verses']:
            s = ''.join(c for c in v['text'] if c not in full_no_dia)
            s = s.rstrip(' .،؛؟!ــ')
            if not s: continue
            ll = s[-1]
            n += 1
            if ll in alif_set_strict or ll == 'ٰ': alif += 1
        rate = alif / n if n else 0
        rates2.append((sid, rate, alif, n))
    perfect_no_tashkeel = sorted([r[0] for r in rates2 if r[1] >= 0.99999])

    return {
        'rules_variant_strict_alif_set_only': {
            'cluster_at_100pct': perfect_strict,
            'matches_canonical': perfect_strict == CLUSTER,
        },
        'rules_variant_no_tashkeel_text': {
            'cluster_at_100pct': perfect_no_tashkeel,
            'matches_canonical': perfect_no_tashkeel == CLUSTER,
        },
        'note': "rules-tuple sensitivity check; if EITHER variant breaks the cluster, the 100%-claim is rules-fragile.",
    }


# ---------- main ----------

def main():
    t0 = time.time()
    verify_sha()

    print("[load] texts...")
    no_tashkeel = load_text("quran-no-tashkeel.json")
    min_tashkeel = load_text("quran-min-tashkeel.json")
    full_tashkeel = load_text("quran-full-tashkeel.json")
    rates_data = verify_cluster(min_tashkeel)

    print("[load] FR matrix + auxiliaries...")
    M = load_fr_matrix()
    rev_order = load_revelation_order()
    verse_counts = load_verse_counts()
    rhyme_diag = load_rhyme_phoneme_diagnostics()

    print("[compute] per-surah 4-axis values...")
    axes = per_surah_axes(no_tashkeel, min_tashkeel, full_tashkeel, M)

    print("[run] H1 — FR-roots cohesion...")
    H1 = H1_fr_roots(M)
    print(f"   H1: obs={H1['observed']:.4f} pct={H1['percentile']*100:.2f}% verdict={H1['verdict']}")

    print("[run] H2 — verse-count cohesion...")
    H2 = H2_verse_count(verse_counts)
    print(f"   H2: chi2={H2['chi2']:.3f} perm_p={H2['perm_p_chi2_geq_obs']*100:.2f}% verdict={H2['verdict']}")

    print("[run] H3 — chronology cohesion...")
    H3 = H3_chronology(rev_order)
    print(f"   H3: obs={H3['observed']:.2f} pct={H3['percentile']*100:.2f}% verdict={H3['verdict']}")

    print("[run] H4 — mushaf-position cohesion...")
    H4 = H4_mushaf()
    print(f"   H4: obs={H4['observed']:.2f} pct={H4['percentile']*100:.2f}% verdict={H4['verdict']}")

    print("[run] H5 — 4-axis composite cohesion...")
    H5 = H5_composite(axes)
    print(f"   H5: obs_composite={H5['observed_composite']:.3f} pct={H5['percentile']*100:.2f}% verdict={H5['verdict']}")

    print("[post-hoc] comparator-16...")
    comp16 = comparator_16(M, rev_order, axes, verse_counts, rates_data)

    print("[post-hoc] sub-cluster (mushaf >= 75)...")
    sub = sub_cluster_mushaf_tail(M, rev_order)

    print("[post-hoc] rules-tuple variants...")
    rules_var = rules_variant_no_dagger(min_tashkeel, no_tashkeel)

    # Family verdict
    cells = [H1, H2, H3, H4, H5]
    n_pass = sum(1 for c in cells if c.get('verdict') == 'VINDICATED')
    n_dir = sum(1 for c in cells if c.get('verdict') == 'DIRECTIONAL')
    if n_pass >= 1:
        family_verdict = "CLUSTER-COHERENT (≥1 H_n PASSED Bonferroni-5)"
    elif n_dir >= 3:
        family_verdict = "DIRECTIONAL CLUSTER (≥3 sub-α DIRECTIONAL)"
    elif n_pass + n_dir == 0:
        family_verdict = "NULL CLUSTER — alif-monorhyme is a SURFACE feature only"
    else:
        family_verdict = "MIXED — partial directionality"

    out = {
        'finding_id': 'H-NEW-910',
        'title': 'Alif-8 cluster cohesion test (Bonferroni-5)',
        'pre_reg_sha256': PREREG_SHA,
        'seed': SEED,
        'n_perms': N_PERMS,
        'bonferroni_k': 5,
        'alpha_bon': ALPHA_BON,
        'alpha_directional': ALPHA_DIR,
        'rules_tuple_default': '(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'rules_tuple_cluster_definition': '(min-tashkeel, last-letter-of-verse, alif-set={ا,آ,أ,إ,ى,ٰ}, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'cluster': CLUSTER,
        'cluster_names_arabic': {
            18: 'الكهف', 48: 'الفتح', 65: 'الطلاق', 72: 'الجن',
            76: 'الإنسان', 87: 'الأعلى', 91: 'الشمس', 92: 'الليل'},
        'cluster_alif_rates_verified': {sid: rate for sid, rate, *_ in rates_data if sid in CLUSTER},
        'H1_fr_roots': H1,
        'H2_verse_count': H2,
        'H3_chronology': H3,
        'H4_mushaf': H4,
        'H5_4axis_composite': H5,
        'family_verdict': family_verdict,
        'comparator_16': comp16,
        'sub_cluster_tail': sub,
        'rules_tuple_variants': rules_var,
        'runtime_seconds': time.time() - t0,
    }

    out_path = ROOT / "findings/phase-b-hypotheses/csv/h-new-910-alif8-cluster.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"[ok] wrote {out_path}")
    print(f"\nFAMILY VERDICT: {family_verdict}")
    print(f"  H1 FR-roots:       {H1['verdict']:<12} pct={H1['percentile']*100:.2f}%")
    print(f"  H2 verse-count:    {H2['verdict']:<12} perm_p={H2['perm_p_chi2_geq_obs']*100:.2f}%")
    print(f"  H3 chronology:     {H3['verdict']:<12} pct={H3['percentile']*100:.2f}%")
    print(f"  H4 mushaf-pos:     {H4['verdict']:<12} pct={H4['percentile']*100:.2f}%")
    print(f"  H5 4-axis comp:    {H5['verdict']:<12} pct={H5['percentile']*100:.2f}%")
    print(f"\nRuntime: {out['runtime_seconds']:.1f}s")


if __name__ == "__main__":
    main()
