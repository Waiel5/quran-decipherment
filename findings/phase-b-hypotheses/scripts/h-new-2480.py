#!/usr/bin/env python3
"""H-NEW-2480 — Cycle-centrality ~ private-vocabulary regression.

Direct test of the cross-finding-027 / H-NEW-2430 mechanism:
elaboration ⇒ lexical periphery. For ALL pericopes across the prophet-cycles
(Nūḥ, Ibrāhīm, Hūd, Maryam, Yūnus + the Mūsā control cycle), compute per pericope:
  (a) centrality   = mean-pairwise root-Jaccard within its OWN cycle (medoid sense)
  (b) private_root = root-TYPES in p appearing in NO other pericope of the same cycle
  (c) length       = root-TOKEN count (with multiplicity)
Regress centrality on private_root_count and on length (Spearman), pooled +
per-cycle, with a partial correlation that distinguishes the private-vocab effect
from a pure length effect.

DIRECTION LOCKED (before computation):
  H1: ρ(centrality, private_root_count) < 0   (more private vocab ⇒ more peripheral)
  H2: ρ(centrality, length) < 0
  H3: partial ρ(centrality, private | length) < 0  (mechanism survives length control)
A positive ρ with reversed-direction p<0.05 = pre-commit VIOLATION, full prominence.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2480-centrality-regression.md
Pre-reg SHA-256: a861d7cdccbe21333d771eb48b1a29542daa92db947f51a2053f7357ad56cffb
Seed 20260509, n_perm=10000. Headline Bonferroni k=3: α = 0.05/3 = 0.0167.
Rules-tuple: (no-tashkeel, QAC v0.4 ROOT, verse-union pericope,
basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).
"""
import json
import hashlib
import sys
import os
import random
from collections import defaultdict
from itertools import combinations

ROOT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(ROOT, 'findings/phase-b-hypotheses/prereg-h-new-2480-centrality-regression.md')
EXPECTED_SHA = 'a861d7cdccbe21333d771eb48b1a29542daa92db947f51a2053f7357ad56cffb'
SEED = 20260509
N_PERM = 10000
BON_K = 3                       # headline family: pooled {H1, H2, H3}
ALPHA_BON = 0.05 / BON_K        # 0.016666...

MORPH = os.path.join(ROOT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
QURAN = os.path.join(ROOT, 'quran-text/quran-no-tashkeel.json')
OUT = os.path.join(ROOT, 'findings/phase-b-hypotheses/csv/h-new-2480.json')

# Cycles + pericopes — IDENTICAL boundaries to H-NEW-2430 (and Mūsā control).
# Each entry: (label, surah, v0, v1). Markers verified on disk at runtime.
CYCLES = {
    'NUH': {
        'marker': ['نوح', 'نوحا'],
        'pericopes': [
            ('Q 7:59-64',     7,  59,  64),
            ('Q 11:25-49',   11,  25,  49),
            ('Q 23:23-30',   23,  23,  30),
            ('Q 26:105-122', 26, 105, 122),
            ('Q 54:9-17',    54,   9,  17),
            ('Q 71:1-28',    71,   1,  28),
        ],
    },
    'IBRAHIM': {
        'marker': ['إبراهيم', 'ابراهيم'],
        'pericopes': [
            ('Q 6:74-83',     6,  74,  83),
            ('Q 14:35-41',   14,  35,  41),
            ('Q 19:41-50',   19,  41,  50),
            ('Q 21:51-70',   21,  51,  70),
            ('Q 26:69-104',  26,  69, 104),
            ('Q 37:83-113',  37,  83, 113),
        ],
    },
    'HUD': {
        'marker': ['هود', 'هودا', 'عاد', 'عادا'],
        'pericopes': [
            ('Q 7:65-72',     7,  65,  72),
            ('Q 11:50-60',   11,  50,  60),
            ('Q 26:123-140', 26, 123, 140),
            ('Q 46:21-26',   46,  21,  26),
            ('Q 54:18-21',   54,  18,  21),
        ],
    },
    'MARYAM': {
        'marker': ['مريم', 'عيسى', 'روحنا', 'وابنها'],
        'pericopes': [
            ('Q 3:35-47',     3,  35,  47),
            ('Q 19:16-34',   19,  16,  34),
            ('Q 21:91',      21,  91,  91),
            ('Q 23:50',      23,  50,  50),
            ('Q 66:12',      66,  12,  12),
        ],
    },
    'YUNUS': {
        'marker': ['يونس', 'النون', 'الحوت', 'حوت'],
        'pericopes': [
            ('Q 10:98',      10,  98,  98),
            ('Q 21:87-88',   21,  87,  88),
            ('Q 37:139-148', 37, 139, 148),
            ('Q 68:48-50',   68,  48,  50),
        ],
    },
    'MUSA': {  # H-NEW-2430 documented control cycle — included as ordinary pericopes
        'marker': ['موسى', 'موسي', 'فرعون'],
        'pericopes': [
            ('Q 20:9-36',  20,  9, 36),
            ('Q 27:7-14',  27,  7, 14),
            ('Q 28:29-35', 28, 29, 35),
            ('Q 79:15-26', 79, 15, 26),
        ],
    },
}
CYCLE_ORDER = ['NUH', 'IBRAHIM', 'HUD', 'MARYAM', 'YUNUS', 'MUSA']

# MW-5 replication anchors from H-NEW-2430 stored results.
NUH_Q71_RANK_STORED = 5
NUH_CENTROID_STORED = 'Q 7:59-64'
MUSA_Q20_HUB_STORED = 0.234


def verify_sha():
    actual = hashlib.sha256(open(PREREG, 'rb').read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FATAL: pre-reg SHA mismatch.\n  expected {EXPECTED_SHA}\n  actual   {actual}",
              file=sys.stderr)
        sys.exit(1)
    print(f"Pre-reg SHA-256 OK: {actual}")


def load_qac_roots_by_verse():
    """Returns (verse_root_types, verse_root_tokens):
       verse_root_types[(s,v)] = set of distinct roots in that verse
       verse_root_tokens[(s,v)] = list of roots WITH multiplicity (one per root-bearing token)
    """
    vtype = defaultdict(set)
    vtok = defaultdict(list)
    with open(MORPH, encoding='utf-8') as f:
        for line in f:
            line = line.rstrip()
            if not line or line.startswith('#') or line.startswith('LOCATION'):
                continue
            parts = line.split('\t')
            if len(parts) < 4:
                continue
            loc = parts[0].strip('()')
            try:
                s, v, w, seg = (int(x) for x in loc.split(':'))
            except ValueError:
                continue
            for tok in parts[3].split('|'):
                if tok.startswith('ROOT:'):
                    r = tok[len('ROOT:'):]
                    vtype[(s, v)].add(r)
                    vtok[(s, v)].append(r)
                    break
    return dict(vtype), dict(vtok)


def pericope_root_types(vtype, s, v0, v1):
    out = set()
    for v in range(v0, v1 + 1):
        out |= vtype.get((s, v), set())
    return out


def pericope_root_tokens(vtok, s, v0, v1):
    n = 0
    for v in range(v0, v1 + 1):
        n += len(vtok.get((s, v), []))
    return n


def jac(a, b):
    u = a | b
    return len(a & b) / len(u) if u else 0.0


def spearman(x, y):
    """Spearman rho with average ranks for ties."""
    n = len(x)
    rx = _rankdata(x)
    ry = _rankdata(y)
    return _pearson(rx, ry)


def _rankdata(a):
    order = sorted(range(len(a)), key=lambda i: a[i])
    ranks = [0.0] * len(a)
    i = 0
    while i < len(a):
        j = i
        while j + 1 < len(a) and a[order[j + 1]] == a[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0  # 1-based average rank
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def _pearson(x, y):
    n = len(x)
    mx = sum(x) / n
    my = sum(y) / n
    sxy = sum((xi - mx) * (yi - my) for xi, yi in zip(x, y))
    sxx = sum((xi - mx) ** 2 for xi in x)
    syy = sum((yi - my) ** 2 for yi in y)
    if sxx <= 0 or syy <= 0:
        return float('nan')
    return sxy / (sxx * syy) ** 0.5


def partial_spearman(x, y, z):
    """Partial Spearman of x,y controlling z, via rank-then-pearson-residual formula."""
    rx = _rankdata(x)
    ry = _rankdata(y)
    rz = _rankdata(z)
    rxy = _pearson(rx, ry)
    rxz = _pearson(rx, rz)
    ryz = _pearson(ry, rz)
    denom = ((1 - rxz ** 2) * (1 - ryz ** 2)) ** 0.5
    if denom <= 0:
        return float('nan'), rxy, rxz, ryz
    return (rxy - rxz * ryz) / denom, rxy, rxz, ryz


def perm_p_one_sided_neg(x, y, rho_obs, rng, n_perm):
    """Pairing-shuffle permutation null; one-sided p in the LOCKED negative direction:
       p = (#{rho_perm <= rho_obs} + 1) / (n_perm + 1)."""
    yperm = list(y)
    cnt = 0
    for _ in range(n_perm):
        rng.shuffle(yperm)
        if spearman(x, yperm) <= rho_obs:
            cnt += 1
    return (cnt + 1) / (n_perm + 1)


def perm_p_partial_neg(rx, ry, rz, rho_obs, rng, n_perm):
    """Permutation null for partial corr: shuffle y-rank pairing, recompute partial.
       One-sided negative-direction p."""
    yp = list(ry)
    cnt = 0
    for _ in range(n_perm):
        rng.shuffle(yp)
        rxy = _pearson(rx, yp)
        ryz = _pearson(yp, rz)
        rxz = _pearson(rx, rz)
        denom = ((1 - rxz ** 2) * (1 - ryz ** 2)) ** 0.5
        rp = (rxy - rxz * ryz) / denom if denom > 0 else 0.0
        if rp <= rho_obs:
            cnt += 1
    return (cnt + 1) / (n_perm + 1)


def perm_p_within_cycle_neg(records, key_x, key_y, rho_obs, rng, n_perm, cycle_ids):
    """Within-cycle pairing shuffle: permute key_y WITHIN each cycle block, recompute
       pooled Spearman. Preserves cycle structure."""
    by_cycle = defaultdict(list)
    for i, r in enumerate(records):
        by_cycle[r['cycle']].append(i)
    x = [r[key_x] for r in records]
    cnt = 0
    for _ in range(n_perm):
        yperm = [None] * len(records)
        for cyc, idxs in by_cycle.items():
            vals = [records[i][key_y] for i in idxs]
            rng.shuffle(vals)
            for i, val in zip(idxs, vals):
                yperm[i] = val
        if spearman(x, yperm) <= rho_obs:
            cnt += 1
    return (cnt + 1) / (n_perm + 1)


def ols_standardized(y, X_cols):
    """Standardized OLS (descriptive). y on each standardized predictor jointly.
       Two predictors only — closed-form via normal equations on standardized vars."""
    n = len(y)
    def z(a):
        m = sum(a) / n
        sd = (sum((v - m) ** 2 for v in a) / n) ** 0.5
        return [(v - m) / sd for v in a] if sd > 0 else [0.0] * n
    zy = z(y)
    zx1 = z(X_cols[0])
    zx2 = z(X_cols[1])
    r11 = sum(a * a for a in zx1) / n
    r22 = sum(a * a for a in zx2) / n
    r12 = sum(a * b for a, b in zip(zx1, zx2)) / n
    r1y = sum(a * b for a, b in zip(zx1, zy)) / n
    r2y = sum(a * b for a, b in zip(zx2, zy)) / n
    det = r11 * r22 - r12 * r12
    if abs(det) < 1e-12:
        return None
    b1 = (r22 * r1y - r12 * r2y) / det
    b2 = (r11 * r2y - r12 * r1y) / det
    return {'beta_z_private': b1, 'beta_z_length': b2, 'pred_corr_private_length': r12}


def verify_boundaries(sidx):
    failures = []
    for cyc, d in CYCLES.items():
        for label, s, v0, v1 in d['pericopes']:
            if s not in sidx:
                failures.append(f'{cyc} {label}: surah {s} missing')
                continue
            sv = {int(v['id']): v['text'] for v in sidx[s]['verses']}
            for v in range(v0, v1 + 1):
                if v not in sv:
                    failures.append(f'{cyc} {label}: verse {v} missing')
            joined = ' '.join(sv.get(v, '') for v in range(v0, v1 + 1))
            if not any(m in joined for m in d['marker']):
                failures.append(f'{cyc} {label}: no figure-marker {d["marker"]} found')
    if failures:
        print('FATAL: boundary verification failed:', file=sys.stderr)
        for fa in failures:
            print('  ' + fa, file=sys.stderr)
        sys.exit(1)
    print('Pericope boundaries + figure-markers OK for all 6 cycles (30 pericopes).')


def build_records(vtype, vtok):
    records = []
    per_cycle = {}
    for cyc in CYCLE_ORDER:
        pers = CYCLES[cyc]['pericopes']
        rtypes = {lab: pericope_root_types(vtype, s, v0, v1) for lab, s, v0, v1 in pers}
        rtok = {lab: pericope_root_tokens(vtok, s, v0, v1) for lab, s, v0, v1 in pers}
        labels = [p[0] for p in pers]
        # centrality (mean pairwise jaccard within cycle)
        J = {}
        for i, j in combinations(labels, 2):
            v = jac(rtypes[i], rtypes[j])
            J[(i, j)] = v
            J[(j, i)] = v
        cent = {a: sum(J[(a, b)] for b in labels if b != a) / (len(labels) - 1) for a in labels}
        # private roots: types not in ANY other pericope of the same cycle
        union_others = {}
        for a in labels:
            u = set()
            for b in labels:
                if b != a:
                    u |= rtypes[b]
            union_others[a] = u
        cycle_recs = []
        for (lab, s, v0, v1) in pers:
            priv = rtypes[lab] - union_others[lab]
            rec = {
                'cycle': cyc,
                'pericope': lab,
                'surah': s,
                'centrality': cent[lab],
                'private_root_count': len(priv),
                'unique_root_type_count': len(rtypes[lab]),
                'root_token_count': rtok[lab],
                'private_fraction': len(priv) / len(rtypes[lab]) if rtypes[lab] else 0.0,
            }
            records.append(rec)
            cycle_recs.append(rec)
        # per-cycle centrality rank (descending centrality)
        ranked = sorted(cycle_recs, key=lambda r: -r['centrality'])
        for k, r in enumerate(ranked):
            r['centrality_rank'] = k + 1
        per_cycle[cyc] = {
            'n': len(labels),
            'centroid': ranked[0]['pericope'],
            'centroid_centrality': ranked[0]['centrality'],
        }
    return records, per_cycle


def main():
    verify_sha()
    text = json.load(open(QURAN))
    sidx = {int(s['id']): s for s in text}
    verify_boundaries(sidx)

    vtype, vtok = load_qac_roots_by_verse()
    records, per_cycle = build_records(vtype, vtok)

    # ---- MW-5 replication assertions vs H-NEW-2430 ----
    nuh = [r for r in records if r['cycle'] == 'NUH']
    nuh_q71 = next(r for r in nuh if r['pericope'] == 'Q 71:1-28')
    assert nuh_q71['centrality_rank'] == NUH_Q71_RANK_STORED, \
        f"MW-5 FAIL: Nūḥ Q71 rank {nuh_q71['centrality_rank']} != {NUH_Q71_RANK_STORED}"
    assert per_cycle['NUH']['centroid'] == NUH_CENTROID_STORED, \
        f"MW-5 FAIL: Nūḥ centroid {per_cycle['NUH']['centroid']} != {NUH_CENTROID_STORED}"
    musa = [r for r in records if r['cycle'] == 'MUSA']
    musa_q20 = next(r for r in musa if r['pericope'] == 'Q 20:9-36')
    assert abs(musa_q20['centrality'] - MUSA_Q20_HUB_STORED) < 0.01, \
        f"MW-5 FAIL: Mūsā Q20 hub {musa_q20['centrality']:.4f} != ~{MUSA_Q20_HUB_STORED}"
    print(f"MW-5 replication OK: Nūḥ Q71 rank {nuh_q71['centrality_rank']}/6, "
          f"centroid {per_cycle['NUH']['centroid']}; Mūsā Q20 hub {musa_q20['centrality']:.4f}.")

    cent = [r['centrality'] for r in records]
    priv = [r['private_root_count'] for r in records]
    length = [r['root_token_count'] for r in records]

    rng = random.Random(SEED)

    # ---- Pooled H1: centrality ~ private_root_count ----
    rho_h1 = spearman(cent, priv)
    p_h1 = perm_p_one_sided_neg(cent, priv, rho_h1, random.Random(SEED), N_PERM)

    # ---- Pooled H2: centrality ~ length ----
    rho_h2 = spearman(cent, length)
    p_h2 = perm_p_one_sided_neg(cent, length, rho_h2, random.Random(SEED + 1), N_PERM)

    # ---- H3 partial: centrality ~ private | length ----
    par_pl, rxy_cl_priv, rxz_cl_priv, ryz_priv_len = partial_spearman(cent, priv, length)
    rc = _rankdata(cent); rp = _rankdata(priv); rl = _rankdata(length)
    p_h3 = perm_p_partial_neg(rc, rp, rl, par_pl, random.Random(SEED + 2), N_PERM)

    # symmetric partial: centrality ~ length | private
    par_lp, _, _, _ = partial_spearman(cent, length, priv)
    p_h3b = perm_p_partial_neg(rc, rl, rp, par_lp, random.Random(SEED + 3), N_PERM)

    # also: private vs length collinearity
    rho_priv_len = spearman(priv, length)

    # ---- within-cycle-preserving pooled permutation (MW-6 structure check) ----
    p_h1_wc = perm_p_within_cycle_neg(records, 'centrality', 'private_root_count',
                                      rho_h1, random.Random(SEED + 4), N_PERM, CYCLE_ORDER)

    # ---- OLS standardized sanity (MW-3) ----
    ols = ols_standardized(cent, [priv, length])

    # ---- Per-cycle correlations (secondary, MW-7-capped direction tallies) ----
    per_cycle_corr = {}
    neg_tally_priv = 0
    neg_tally_len = 0
    for cyc in CYCLE_ORDER:
        recs = [r for r in records if r['cycle'] == cyc]
        c = [r['centrality'] for r in recs]
        pv = [r['private_root_count'] for r in recs]
        ln = [r['root_token_count'] for r in recs]
        rho_p = spearman(c, pv)
        rho_l = spearman(c, ln)
        if rho_p < 0:
            neg_tally_priv += 1
        if rho_l < 0:
            neg_tally_len += 1
        per_cycle_corr[cyc] = {
            'n': len(recs),
            'rho_centrality_private': rho_p,
            'rho_centrality_length': rho_l,
            'sign_private_negative': rho_p < 0,
            'sign_length_negative': rho_l < 0,
        }

    # ---- Verdicts (LOCKED criteria) ----
    def verdict_pooled(rho, p):
        if rho > 0:
            # reversal check: reversed-direction p
            return 'REVERSAL — pre-commit violation' if p > (1 - 0.05) else 'POSITIVE (not sig)'
        if p <= ALPHA_BON:
            return 'CONFIRMED (negative, Bonferroni-3)'
        if p <= 0.05:
            return 'DIRECTIONAL (negative, raw 0.05)'
        return 'NULL'

    v_h1 = verdict_pooled(rho_h1, p_h1)
    v_h2 = verdict_pooled(rho_h2, p_h2)

    # H3 mechanism verdict
    if par_pl > 0:
        v_h3 = 'MECHANISM REVERSED — private flips positive once length controlled'
    elif par_pl >= -0.05:
        v_h3 = 'LENGTH-ARTEFACT — private partial collapses to ~0 once length controlled'
    elif p_h3 <= ALPHA_BON:
        v_h3 = 'MECHANISM VINDICATED — private negative BEYOND length (Bonferroni-3)'
    elif p_h3 <= 0.05:
        v_h3 = 'MECHANISM DIRECTIONAL — private negative beyond length (raw 0.05)'
    else:
        v_h3 = 'PARTIAL-WEAK — private partial negative but not significant'

    out = {
        'finding_id': 'H-NEW-2480',
        'title': 'Cycle-centrality ~ private-vocabulary regression (cross-finding-027 mechanism test)',
        'prereg_sha256': EXPECTED_SHA,
        'seed': SEED,
        'n_perm': N_PERM,
        'bonferroni_k_headline': BON_K,
        'alpha_bon_headline': ALPHA_BON,
        'rules_tuple': '(no-tashkeel, QAC v0.4 ROOT, verse-union pericope, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'extends': 'H-NEW-2430 + cross-finding-027 + Q071-F-01 + Q020-F-06',
        'direction_locked': 'NEGATIVE: centrality ~ private_root_count (more private vocab => more peripheral)',
        'n_pericopes': len(records),
        'n_cycles': len(CYCLE_ORDER),
        'records': records,
        'per_cycle_centroids': per_cycle,
        'pooled': {
            'H1_centrality_vs_private': {
                'spearman_rho': rho_h1,
                'perm_p_one_sided_negative': p_h1,
                'perm_p_within_cycle_preserving': p_h1_wc,
                'verdict': v_h1,
            },
            'H2_centrality_vs_length': {
                'spearman_rho': rho_h2,
                'perm_p_one_sided_negative': p_h2,
                'verdict': v_h2,
            },
            'H3_partial_private_given_length': {
                'partial_spearman_rho': par_pl,
                'perm_p_one_sided_negative': p_h3,
                'components': {
                    'rho_centrality_private': rxy_cl_priv,
                    'rho_centrality_length': rxz_cl_priv,
                    'rho_private_length': ryz_priv_len,
                },
                'verdict': v_h3,
            },
            'H3b_partial_length_given_private': {
                'partial_spearman_rho': par_lp,
                'perm_p_one_sided_negative': p_h3b,
            },
            'collinearity_private_vs_length_spearman': rho_priv_len,
            'ols_standardized_sanity': ols,
        },
        'per_cycle_correlations_MW7_capped': {
            'note': 'Secondary exploratory family (k=6, n<=6 per cycle). Direction-tallies only; not pass/fail.',
            'cycles': per_cycle_corr,
            'n_cycles_negative_private': neg_tally_priv,
            'n_cycles_negative_length': neg_tally_len,
            'n_cycles_total': len(CYCLE_ORDER),
        },
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    # ---- console report ----
    print(f"\nN = {len(records)} pericopes across {len(CYCLE_ORDER)} cycles. "
          f"Headline Bonferroni α = 0.05/{BON_K} = {ALPHA_BON:.4f}\n")
    print(f"{'pericope':14s} {'cyc':8s} {'cent':>8s} {'priv':>5s} {'tok':>5s} {'types':>6s} {'rank':>4s}")
    for r in records:
        print(f"{r['pericope']:14s} {r['cycle']:8s} {r['centrality']:8.5f} "
              f"{r['private_root_count']:5d} {r['root_token_count']:5d} "
              f"{r['unique_root_type_count']:6d} {r['centrality_rank']:4d}")
    print()
    print(f"POOLED H1  centrality ~ private_root_count: rho = {rho_h1:+.4f}  "
          f"perm_p(neg) = {p_h1:.4f}  [within-cycle p = {p_h1_wc:.4f}]  -> {v_h1}")
    print(f"POOLED H2  centrality ~ length(root-tokens): rho = {rho_h2:+.4f}  "
          f"perm_p(neg) = {p_h2:.4f}  -> {v_h2}")
    print(f"collinearity private~length: rho = {rho_priv_len:+.4f}")
    print(f"POOLED H3  partial(centrality, private | length): rho = {par_pl:+.4f}  "
          f"perm_p(neg) = {p_h3:.4f}  -> {v_h3}")
    print(f"POOLED H3b partial(centrality, length | private): rho = {par_lp:+.4f}  "
          f"perm_p(neg) = {p_h3b:.4f}")
    if ols:
        print(f"OLS standardized: beta_z(private) = {ols['beta_z_private']:+.4f}  "
              f"beta_z(length) = {ols['beta_z_length']:+.4f}")
    print(f"\nPer-cycle direction tallies (MW-7-capped): "
          f"{neg_tally_priv}/{len(CYCLE_ORDER)} cycles negative for private; "
          f"{neg_tally_len}/{len(CYCLE_ORDER)} negative for length.")
    for cyc in CYCLE_ORDER:
        pc = per_cycle_corr[cyc]
        print(f"  {cyc:8s} n={pc['n']}  rho_priv={pc['rho_centrality_private']:+.3f}  "
              f"rho_len={pc['rho_centrality_length']:+.3f}")
    print(f"\nResult written to {OUT}")


if __name__ == '__main__':
    main()
