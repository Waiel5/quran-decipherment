#!/usr/bin/env python3
"""H-NEW-2420 — al-Biqāʿī WITHIN-surah sequential naẓm test.

Tests Burhān al-Dīn al-Biqāʿī's doctrine (*Naẓm al-durar fī tanāsub al-āyāt
wa-l-suwar*) that, WITHIN each sūra, each verse is munāsib (fitted) to its
neighbour — the sūra is an ORDERED naẓm, not a random verse-bag.

GENERATOR: for every surah, compute the mean adjacent-verse root-Jaccard
(consecutive pairs in CANONICAL Hafs-Kufan order) and compare it to a
within-surah verse-SHUFFLE null (the same verse-root-sets re-ordered at random).
A surah with real sequential naẓm has adjacent-cohesion ABOVE its own shuffle
distribution (z_surah > 0).

Direction LOCKED before computation: canonical adjacent-cohesion > shuffled
adjacent-cohesion (z > 0, one-tailed greater), aggregate and per-surah. A
reversed aggregate result (z < 0) is a pre-commit-violation published as NULL
with prominence — it would mean adjacent verses are NOT more lexically cohesive
than random within-surah orderings (naẓm is thematic/pronominal, or verses are
deliberately dispersed).

Complements H-NEW-2280 (al-Biqāʿī munāsabah at the BETWEEN-surah seam); this is
the WITHIN-surah intra-naẓm.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2420-within-surah-nazm.md
Pre-reg SHA256: 301f71184201dfa228912f3a65a1fd7de1e2dd9e675316acad7fcb32a904dce1

Seed 20260509, n_perm=10000.
Rules-tuple: (no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1,
Hafs-Kufan, Mashriqi).
"""
import json
import hashlib
import sys
import os
import csv
import math
import random
from collections import defaultdict

PROJECT_ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(
    PROJECT_ROOT,
    'findings/phase-b-hypotheses/prereg-h-new-2420-within-surah-nazm.md',
)
EXPECTED_SHA = '301f71184201dfa228912f3a65a1fd7de1e2dd9e675316acad7fcb32a904dce1'
SEED = 20260509
SEED_REPLICATE = 20260510
N_PERM = 10000

MORPH = os.path.join(PROJECT_ROOT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
QURAN_NO_TASHKEEL = os.path.join(PROJECT_ROOT, 'quran-text/quran-no-tashkeel.json')
REV_ORDER = os.path.join(PROJECT_ROOT, 'data/revelation-order.csv')
OUT_JSON = os.path.join(PROJECT_ROOT, 'findings/phase-b-hypotheses/csv/h-new-2420.json')

N_SURAHS = 114
MIN_L_ELIGIBLE = 4          # surahs with L < 4 excluded from significance family
# Eligible family size and Bonferroni alpha are computed from data at runtime.


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(
            f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}",
            file=sys.stderr,
        )
        sys.exit(1)


def load_surah_meta():
    text = json.load(open(QURAN_NO_TASHKEEL))
    lengths, names, types = {}, {}, {}
    for s in text:
        sid = int(s['id'])
        lengths[sid] = len(s['verses'])
        names[sid] = s.get('transliteration', s.get('name', str(sid)))
        types[sid] = s.get('type', '')
    assert len(lengths) == N_SURAHS, f'expected {N_SURAHS} surahs, got {len(lengths)}'
    return lengths, names, types


def load_revelation_order():
    """mushaf_order -> noldeke chronological rank (revelation_order column)."""
    rev = {}
    with open(REV_ORDER, newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            try:
                rev[int(row['mushaf_order'])] = int(row['revelation_order'])
            except (KeyError, ValueError):
                continue
    return rev


def load_qac_roots_by_verse():
    """Returns {(surah, verse): set(ROOT)} from QAC v0.4.

    Identical convention to h-new-2280.py: first ROOT-tagged feature per segment.
    """
    verse_roots = defaultdict(set)
    with open(MORPH, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if not line or line.startswith('#') or line.startswith('LOCATION'):
                continue
            parts = line.split('\t')
            if len(parts) < 4:
                continue
            loc = parts[0]
            features = parts[3]
            loc_clean = loc.strip('()')
            try:
                s, v, w, seg = (int(x) for x in loc_clean.split(':'))
            except ValueError:
                continue
            for tok in features.split('|'):
                if tok.startswith('ROOT:'):
                    root = tok[len('ROOT:'):]
                    verse_roots[(s, v)].add(root)
                    break
    return dict(verse_roots)


def jaccard(a, b):
    u = a | b
    if not u:
        return 0.0
    return len(a & b) / len(u)


def mean_adjacent_jaccard(order_rootsets):
    """Mean root-Jaccard over consecutive pairs in the given verse ordering."""
    n = len(order_rootsets)
    if n < 2:
        return 0.0
    tot = 0.0
    for i in range(n - 1):
        tot += jaccard(order_rootsets[i], order_rootsets[i + 1])
    return tot / (n - 1)


def run_surah(sid, length, verse_roots, rng):
    """Observed adjacent-cohesion vs within-surah shuffle null for one surah."""
    rootsets = [verse_roots.get((sid, v), set()) for v in range(1, length + 1)]
    obs = mean_adjacent_jaccard(rootsets)

    null_means = []
    idx = list(range(length))
    for _ in range(N_PERM):
        rng.shuffle(idx)
        permuted = [rootsets[i] for i in idx]
        null_means.append(mean_adjacent_jaccard(permuted))

    null_mean = sum(null_means) / len(null_means)
    var = sum((x - null_mean) ** 2 for x in null_means) / len(null_means)
    null_std = var ** 0.5
    z = (obs - null_mean) / null_std if null_std > 0 else 0.0
    n_ge = sum(1 for x in null_means if x >= obs)
    p_greater = n_ge / N_PERM
    # number of DISTINCT shuffle-mean values observed (resolution of the null)
    n_distinct = len(set(round(x, 12) for x in null_means))

    return {
        'surah': sid,
        'L': length,
        'A_obs': obs,
        'null_mean': null_mean,
        'null_std': null_std,
        'z_surah': z,
        'p_greater': p_greater,
        'n_perm_ge_obs': n_ge,
        'n_distinct_shuffle_means': n_distinct,
    }


def stouffer_z(pvals):
    """Combine one-tailed p-values into a Stouffer Z (floor p to 0.5/N_PERM)."""
    floor = 0.5 / N_PERM
    zs = []
    for p in pvals:
        pp = min(max(p, floor), 1 - floor)
        # one-tailed: small p -> large positive z
        zs.append(_inv_norm(1 - pp))
    return sum(zs) / math.sqrt(len(zs)), zs


def _inv_norm(p):
    """Acklam rational approximation of the inverse normal CDF."""
    if p <= 0:
        return -1e9
    if p >= 1:
        return 1e9
    a = [-3.969683028665376e+01, 2.209460984245205e+02, -2.759285104469687e+02,
         1.383577518672690e+02, -3.066479806614716e+01, 2.506628277459239e+00]
    b = [-5.447609879822406e+01, 1.615858368580409e+02, -1.556989798598866e+02,
         6.680131188771972e+01, -1.328068155288572e+01]
    c = [-7.784894002430293e-03, -3.223964580411365e-01, -2.400758277161838e+00,
         -2.549732539343734e+00, 4.374664141464968e+00, 2.938163982698783e+00]
    d = [7.784695709041462e-03, 3.224671290700398e-01, 2.445134137142996e+00,
         3.754408661907416e+00]
    plow, phigh = 0.02425, 1 - 0.02425
    if p < plow:
        q = math.sqrt(-2 * math.log(p))
        return (((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / \
               ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)
    if p > phigh:
        q = math.sqrt(-2 * math.log(1 - p))
        return -(((((c[0]*q+c[1])*q+c[2])*q+c[3])*q+c[4])*q+c[5]) / \
                ((((d[0]*q+d[1])*q+d[2])*q+d[3])*q+1)
    q = p - 0.5
    r = q * q
    return (((((a[0]*r+a[1])*r+a[2])*r+a[3])*r+a[4])*r+a[5])*q / \
           (((((b[0]*r+b[1])*r+b[2])*r+b[3])*r+b[4])*r+1)


def _norm_sf(z):
    """One-tailed survival function P(Z >= z)."""
    return 0.5 * math.erfc(z / math.sqrt(2))


def binomial_sign_p(n_pos, n_total):
    """One-tailed binomial P(X >= n_pos) under p=0.5 (more-positive)."""
    p = 0.0
    for k in range(n_pos, n_total + 1):
        p += math.comb(n_total, k) * (0.5 ** n_total)
    return p


def spearman(xs, ys):
    """Spearman rho with average-rank tie handling."""
    def ranks(vals):
        order = sorted(range(len(vals)), key=lambda i: vals[i])
        r = [0.0] * len(vals)
        i = 0
        while i < len(vals):
            j = i
            while j + 1 < len(vals) and vals[order[j + 1]] == vals[order[i]]:
                j += 1
            avg = (i + j) / 2.0 + 1
            for kk in range(i, j + 1):
                r[order[kk]] = avg
            i = j + 1
        return r
    rx, ry = ranks(xs), ranks(ys)
    n = len(xs)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    dx = math.sqrt(sum((rx[i] - mx) ** 2 for i in range(n)))
    dy = math.sqrt(sum((ry[i] - my) ** 2 for i in range(n)))
    if dx == 0 or dy == 0:
        return 0.0
    return num / (dx * dy)


def aggregate(per_surah_eligible, label):
    n = len(per_surah_eligible)
    n_pos = sum(1 for r in per_surah_eligible if r['z_surah'] > 0)
    n_neg = sum(1 for r in per_surah_eligible if r['z_surah'] < 0)
    sign_p = binomial_sign_p(n_pos, n)
    Z, _ = stouffer_z([r['p_greater'] for r in per_surah_eligible])
    stouffer_p = _norm_sf(Z)
    return {
        'label': label,
        'n_eligible': n,
        'n_pos_z': n_pos,
        'n_neg_z': n_neg,
        'n_zero_z': n - n_pos - n_neg,
        'sign_test_p_greater': sign_p,
        'stouffer_Z': Z,
        'stouffer_p_one_tailed': stouffer_p,
    }


def main():
    verify_sha()
    lengths, names, types = load_surah_meta()
    rev = load_revelation_order()
    verse_roots = load_qac_roots_by_verse()

    # Single master RNG, advanced surah-by-surah in ascending id order (locked).
    rng = random.Random(SEED)
    per_surah = []
    for sid in range(1, N_SURAHS + 1):
        r = run_surah(sid, lengths[sid], verse_roots, rng)
        r['name'] = names[sid]
        r['type'] = types[sid]
        r['noldeke_order'] = rev.get(sid)
        per_surah.append(r)

    eligible = [r for r in per_surah if r['L'] >= MIN_L_ELIGIBLE]
    excluded = [r for r in per_surah if r['L'] < MIN_L_ELIGIBLE]
    k_family = len(eligible)
    alpha_bonf = 0.05 / k_family

    # Per-surah verdicts
    for r in per_surah:
        if r['L'] < MIN_L_ELIGIBLE:
            r['eligible'] = False
            r['verdict'] = 'EXCLUDED (L<4; shuffle-null cannot resolve Bonferroni)'
        else:
            r['eligible'] = True
            if r['z_surah'] > 0 and r['p_greater'] < alpha_bonf:
                r['verdict'] = 'NAZM-TIGHT (Bonferroni PASS)'
            elif r['z_surah'] > 0 and r['p_greater'] < 0.05:
                r['verdict'] = 'tight-raw (p<0.05, misses Bonferroni)'
            elif r['z_surah'] > 0:
                r['verdict'] = 'loose / anthology-like'
            else:
                r['verdict'] = 'REVERSED (canonical < shuffle; dispersion)'

    # Observed corpus statistic
    obs_corpus_mean_eligible = sum(r['A_obs'] for r in eligible) / len(eligible)
    null_corpus_mean_eligible = sum(r['null_mean'] for r in eligible) / len(eligible)

    # Aggregate (primary seed)
    agg = aggregate(eligible, 'eligible(L>=4), seed20260509')

    # Aggregate verdict (H1)
    direction_ok = agg['stouffer_Z'] > 0 and (
        sum(1 for r in eligible if r['z_surah'] > 0) >
        sum(1 for r in eligible if r['z_surah'] < 0))
    if obs_corpus_mean_eligible < null_corpus_mean_eligible:
        h1_verdict = 'PRE-COMMIT-VIOLATION (aggregate reversed; NULL with prominence)'
    elif direction_ok and agg['stouffer_p_one_tailed'] < 0.05 and agg['sign_test_p_greater'] < 0.05:
        h1_verdict = 'PASS-DIRECTED'
    elif direction_ok:
        h1_verdict = 'DIRECTIONAL'
    else:
        h1_verdict = 'NULL'

    # MW-5 replicate at seed 20260510 (aggregate only)
    rng2 = random.Random(SEED_REPLICATE)
    per_surah_rep = []
    for sid in range(1, N_SURAHS + 1):
        per_surah_rep.append(run_surah(sid, lengths[sid], verse_roots, rng2))
    eligible_rep = [r for r in per_surah_rep if r['L'] >= MIN_L_ELIGIBLE]
    agg_rep = aggregate(eligible_rep, 'eligible(L>=4), seed20260510')

    # Rosters
    nazm_tight = sorted(
        [r for r in eligible if r['verdict'].startswith('NAZM-TIGHT')],
        key=lambda d: d['z_surah'], reverse=True)
    loose = sorted(
        [r for r in eligible if r['verdict'] == 'loose / anthology-like'],
        key=lambda d: d['z_surah'])
    reversed_surahs = sorted(
        [r for r in eligible if r['verdict'].startswith('REVERSED')],
        key=lambda d: d['z_surah'])
    tight_raw = sorted(
        [r for r in eligible if r['verdict'].startswith('tight-raw')],
        key=lambda d: d['z_surah'], reverse=True)

    # Descriptive correlations (locked in advance, MW-7 capped)
    zs = [r['z_surah'] for r in eligible]
    Ls = [r['L'] for r in eligible]
    rho_z_len = spearman(zs, Ls)
    meccan_z = [r['z_surah'] for r in eligible if r['type'] == 'meccan']
    medinan_z = [r['z_surah'] for r in eligible if r['type'] == 'medinan']
    mean_meccan = sum(meccan_z) / len(meccan_z) if meccan_z else None
    mean_medinan = sum(medinan_z) / len(medinan_z) if medinan_z else None
    rev_pairs = [(r['z_surah'], r['noldeke_order']) for r in eligible
                 if r['noldeke_order'] is not None]
    rho_z_chrono = spearman([a for a, _ in rev_pairs], [b for _, b in rev_pairs]) \
        if rev_pairs else None

    def light(r):
        return {
            'surah': r['surah'], 'name': r['name'], 'type': r['type'], 'L': r['L'],
            'A_obs': r['A_obs'], 'null_mean': r['null_mean'], 'z_surah': r['z_surah'],
            'p_greater': r['p_greater'], 'verdict': r['verdict'],
            'noldeke_order': r['noldeke_order'],
        }

    out = {
        'finding_id': 'H-NEW-2420',
        'title': 'al-Biqāʿī within-surah sequential naẓm — adjacent-verse cohesion vs within-surah shuffle null',
        'prereg_sha': EXPECTED_SHA,
        'seed_primary': SEED,
        'seed_replicate': SEED_REPLICATE,
        'n_perm': N_PERM,
        'rules_tuple': '(no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'null_model': 'within-surah uniform verse-order shuffle; same verse-root-sets, scrambled sequence; 10000 perms/surah',
        'adjacency_metric': 'mean root-Jaccard over consecutive verse pairs (canonical Hafs-Kufan order)',
        'aggregation_scale': 'within-surah adjacent verse-pairs',
        'classical_claim': 'al-Biqāʿī, Naẓm al-durar fī tanāsub al-āyāt wa-l-suwar — each verse is munāsib to its neighbour; the surah is an ordered naẓm, not a random verse-bag. Complements H-NEW-2280 (between-surah seam).',
        'direction_locked': 'canonical adjacent-cohesion > shuffled adjacent-cohesion (z>0, one-tailed greater), aggregate and per-surah',
        'eligibility_rule': 'L>=4 eligible for significance family; L<4 (Q103/108/110) excluded (shuffle-null cannot resolve Bonferroni)',
        'k_bonferroni_family': k_family,
        'alpha_bonferroni': alpha_bonf,
        'corpus_observed_mean_A_eligible': obs_corpus_mean_eligible,
        'corpus_null_mean_eligible': null_corpus_mean_eligible,
        'H1_aggregate': {
            'verdict': h1_verdict,
            'primary': agg,
            'replicate_seed20260510': agg_rep,
        },
        'H2_per_surah_summary': {
            'n_nazm_tight': len(nazm_tight),
            'n_tight_raw_only': len(tight_raw),
            'n_loose': len(loose),
            'n_reversed': len(reversed_surahs),
            'n_excluded': len(excluded),
        },
        'nazm_tight_roster': [light(r) for r in nazm_tight],
        'tight_raw_only_roster': [light(r) for r in tight_raw],
        'loose_anthology_roster': [light(r) for r in loose],
        'reversed_dispersion_roster': [light(r) for r in reversed_surahs],
        'excluded_short_surahs': [light(r) for r in excluded],
        'descriptive_correlations': {
            'note': 'MW-7 capped; descriptive context, not part of locked inferential family',
            'spearman_z_vs_length': rho_z_len,
            'mean_z_meccan': mean_meccan,
            'n_meccan': len(meccan_z),
            'mean_z_medinan': mean_medinan,
            'n_medinan': len(medinan_z),
            'spearman_z_vs_noldeke_revelation_order': rho_z_chrono,
        },
        'per_surah_full': [
            {
                'surah': r['surah'], 'name': r['name'], 'type': r['type'], 'L': r['L'],
                'A_obs': r['A_obs'], 'null_mean': r['null_mean'], 'null_std': r['null_std'],
                'z_surah': r['z_surah'], 'p_greater': r['p_greater'],
                'n_perm_ge_obs': r['n_perm_ge_obs'],
                'n_distinct_shuffle_means': r['n_distinct_shuffle_means'],
                'eligible': r['eligible'], 'verdict': r['verdict'],
                'noldeke_order': r['noldeke_order'],
            }
            for r in per_surah
        ],
    }
    os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
    with open(OUT_JSON, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    # Console summary
    print(f"SHA verified. k_family={k_family}  alpha_bonf={alpha_bonf:.3e}")
    print(f"corpus obs mean A (eligible) = {obs_corpus_mean_eligible:.6f}  "
          f"null mean = {null_corpus_mean_eligible:.6f}")
    print(f"H1 aggregate verdict = {h1_verdict}")
    print(f"  sign test: {agg['n_pos_z']}+/{agg['n_neg_z']}-  "
          f"binomial p={agg['sign_test_p_greater']:.3e}")
    print(f"  Stouffer Z={agg['stouffer_Z']:.3f}  p={agg['stouffer_p_one_tailed']:.3e}")
    print(f"  replicate seed{SEED_REPLICATE}: {agg_rep['n_pos_z']}+/{agg_rep['n_neg_z']}-  "
          f"Stouffer Z={agg_rep['stouffer_Z']:.3f}")
    print(f"H2 rosters: NAZM-TIGHT={len(nazm_tight)}  tight-raw-only={len(tight_raw)}  "
          f"loose={len(loose)}  reversed={len(reversed_surahs)}  excluded={len(excluded)}")
    print(f"  corr: z~L Spearman={rho_z_len:.3f}  "
          f"mean-z Meccan={mean_meccan:.3f} Medinan={mean_medinan:.3f}  "
          f"z~chrono Spearman={rho_z_chrono:.3f}")
    print("\nTop-15 naẓm-tight (by z):")
    for r in nazm_tight[:15]:
        print(f"  Q{r['surah']:>3} {r['name']:<16} L={r['L']:>3} "
              f"A={r['A_obs']:.4f} null={r['null_mean']:.4f} z={r['z_surah']:+.2f} "
              f"p={r['p_greater']:.4f} [{r['type']}]")
    print("\nMost loose / reversed (lowest z among eligible):")
    low = sorted(eligible, key=lambda d: d['z_surah'])[:15]
    for r in low:
        print(f"  Q{r['surah']:>3} {r['name']:<16} L={r['L']:>3} "
              f"A={r['A_obs']:.4f} null={r['null_mean']:.4f} z={r['z_surah']:+.2f} "
              f"p={r['p_greater']:.4f} [{r['type']}] {r['verdict']}")


if __name__ == '__main__':
    main()
