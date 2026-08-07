#!/usr/bin/env python3
"""H-NEW-2830 — is H-NEW-2820's muqaṭṭaʿāt content-clustering independent of Pillar 1?

Pillar 1 (H-NEW-53 / cross-finding-008 / H-NEW-2760) says the 29 muqaṭṭaʿāt surahs
announce the Book at the top: 24/29 mention kitāb or qurʾān in vv. 1–3, and all 29
place their first Book-mention at 0.0996 of the surah against 0.3403 for the other 40
Book-mentioning surahs.

H-NEW-2820 says the same 29 surahs are 3.6 % tighter in whole-surah root content than
size-matched surah sets (matched percentile 0.45), and the ḥawāmīm-7 10.7 % tighter
(0.05).

The two statistics share a vocabulary. The FR instrument runs over the top-500 QAC
roots; Pillar 1's two marker roots — ktb (rank 22, 319 tokens) and qrA (rank 126,
88 tokens) — are both inside it. If the muqaṭṭaʿāt surahs' shared Book-vocabulary is
what pulls their root distributions together, the two results are one signal measured
twice and must not be combined.

METHOD
  A. Rebuild the H-NEW-111 Fisher–Rao root matrix from QAC v0.4 and assert d̄(muq-29)
     is bit-identical to the published 0.938813123152709.
  B. Build a leave-out matrix with the ktb and qrA columns DROPPED from the count
     matrix before Dirichlet smoothing and renormalisation (498 dims, not 500 with two
     zeroed columns — a zeroed smoothed column is identical across surahs and would
     compress every distance uniformly).
  C. Re-run H-NEW-2820's A2-k5 stratified null on BOTH matrices: permute group
     membership within 5 rank-quantile bins of log word count (the dominant channel
     for d̄, ρ = +0.8998, per H-NEW-2820 §2.1), 10,000 draws, seed 20260509. Report the
     matched percentile with and without the Book roots.
  D. CONTROL — removing any two roots perturbs the matrix. Draw 200 frequency-matched
     random root pairs (each partner within ±20 % of ktb's and qrA's token counts,
     excluded from the muqaṭṭaʿāt marker family) and run the same matched null on each,
     giving a reference distribution for the shift produced by removing two arbitrary
     roots of the same weight. The Book pair is read against that distribution.

The question this answers is MECHANISM overlap, not statistical independence of the two
hypothesis tests. Both are computed on the same 29 surahs, selected the same way; that
alone forbids multiplying their p-values regardless of how D comes out.

Write-once discipline (UNIT-DRIFT-DEFECT §7): the run directory is created with
exist_ok=False, every file in it is opened with mode 'x', results.json is written
exactly once at completion, and progress goes OUTSIDE the run directory.
"""
import json
import os
import random
import re
import sys
import time
from collections import Counter, defaultdict

import numpy as np

PROJECT = '/Users/grey/Downloads/quran'
sys.path.insert(0, os.path.join(PROJECT, 'scripts'))

QAC = os.path.join(PROJECT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
H111 = os.path.join(PROJECT, 'findings/phase-b-hypotheses/csv/h-new-111.json')

RUNSTAMP = time.strftime('%Y%m%dT%H%M%SZ', time.gmtime())
RUNDIR = os.path.join(PROJECT, 'findings/phase-b-hypotheses/runs/h-new-2830-independence', RUNSTAMP)
PROGRESS = os.path.join(PROJECT, 'findings/phase-b-hypotheses/runs/h-new-2830-progress')

K_TOP = 500
DIR_ALPHA = 0.5
N_PERM = 10000
N_BINS = 5
SEED = 20260509
SEED_REP = 20260519
N_CONTROL_PAIRS = 200
FREQ_TOL = 0.20

# H-NEW-570's locked sets, verbatim
SET_MUQ = [2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36,
           38, 40, 41, 42, 43, 44, 45, 46, 50, 68]
SET_HM = [40, 41, 42, 43, 44, 45, 46]

# Pillar 1's marker roots. H-NEW-2760 §NARROW matches the surface families
#   كتب|كتاب|الكتاب|... and قرآن|القرآن|قرءان|... ; their QAC roots are ktb and qrA.
BOOK_ROOTS = ['ktb', 'qrA']

PUBLISHED_DBAR_MUQ = 0.938813123152709
PUBLISHED_DBAR_HM = 0.867242285714286


def log(*a):
    print(*a, flush=True)


# ---------------------------------------------------------------------------
# 1. QAC → per-surah root counts (H-NEW-111's parser, verbatim logic)
# ---------------------------------------------------------------------------
def load_roots():
    loc = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
    rt = re.compile(r'ROOT:([^|]+)')
    per = defaultdict(list)
    glob = Counter()
    with open(QAC, encoding='utf-8') as f:
        for line in f:
            if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
                continue
            p = line.rstrip('\n').split('\t')
            if len(p) < 4:
                continue
            m = loc.match(p[0])
            if not m:
                continue
            feat = p[3]
            if 'STEM' not in feat:
                continue
            r = rt.search(feat)
            if not r:
                continue
            per[int(m.group(1))].append(r.group(1))
            glob[r.group(1)] += 1
    return per, glob


def fr_matrix(per, top_roots, drop=()):
    """114x114 Fisher–Rao over per-surah root distributions on `top_roots` minus `drop`.

    Rounded to 6 decimals to match what is actually on disk: H-NEW-111 serialises its
    matrix through `round_floats(o, n=6)` (scripts/h_new_111_fisher_rao_mushaf.py:388),
    so H-NEW-570 — and H-NEW-2820 after it — compute d̄ from 6-decimal values. Rebuilding
    at full precision moves d̄(muq-29) by 2.2e-8, which is the rounding and nothing else.
    Rounding here keeps every arm on the published instrument.
    """
    keep = [r for r in top_roots if r not in set(drop)]
    ix = {r: i for i, r in enumerate(keep)}
    C = np.zeros((114, len(keep)))
    for sid in range(1, 115):
        for r in per.get(sid, []):
            j = ix.get(r)
            if j is not None:
                C[sid - 1, j] += 1.0
    P = C + DIR_ALPHA
    P /= P.sum(axis=1, keepdims=True)
    S = np.sqrt(P)
    D = 2.0 * np.arccos(np.clip(S @ S.T, -1.0, 1.0))
    np.fill_diagonal(D, 0.0)
    return np.round(D, 6)


def dbar(D, ids):
    pos = np.array([s - 1 for s in ids])
    sub = D[np.ix_(pos, pos)]
    n = len(ids)
    return float(sub.sum() / (n * (n - 1)))


# ---------------------------------------------------------------------------
# 2. H-NEW-2820's stratified null, lifted function-for-function
# ---------------------------------------------------------------------------
def rank_bins(values, k):
    order = np.lexsort((np.arange(len(values)), np.asarray(values, dtype=float)))
    parts = np.array_split(order, k)
    b = np.empty(len(values), dtype=int)
    for i, part in enumerate(parts):
        b[part] = i
    return b


def draw_stratified(rng, bins, group_pos, donor_pos, ndraws):
    occ = Counter(int(bins[g]) for g in group_pos)
    cols = []
    for b, need in sorted(occ.items()):
        donors = np.array([d for d in donor_pos if bins[d] == b])
        if len(donors) < need:
            return None, 'bin %d needs %d donors, has %d' % (b, need, len(donors))
        idx = np.argsort(rng.random((ndraws, len(donors))), axis=1)[:, :need]
        cols.append(donors[idx])
    return np.hstack(cols), None


def set_stat_matrix(M0, draws, chunk=2000):
    n = draws.shape[1]
    out = np.empty(len(draws), dtype=float)
    for a in range(0, len(draws), chunk):
        d = draws[a:a + chunk]
        sub = M0[d[:, :, None], d[:, None, :]]
        out[a:a + len(d)] = sub.sum(axis=(1, 2)) / (n * (n - 1))
    return out


def matched_pct(D, ids, bins, seed):
    """Matched percentile of d̄(ids) in the stratified null. Lower = tighter."""
    rng = np.random.default_rng(seed)
    gpos = [s - 1 for s in ids]
    donors = list(range(114))
    draws, err = draw_stratified(rng, bins, gpos, donors, N_PERM)
    if draws is None:
        return None, None, err
    vals = set_stat_matrix(D, draws)
    obs = dbar(D, ids)
    pct = 100.0 * float((vals <= obs).sum()) / len(vals)
    return pct, dict(obs=obs, null_mean=float(vals.mean()),
                     null_sd=float(vals.std(ddof=1)),
                     ratio=obs / float(vals.mean()),
                     z=(obs - float(vals.mean())) / float(vals.std(ddof=1))), None


def main():
    os.makedirs(PROGRESS, exist_ok=True)
    os.makedirs(RUNDIR, exist_ok=False)
    log('[run] %s' % RUNDIR)

    per, glob = load_roots()
    top = [r for r, _ in glob.most_common(K_TOP)]
    assert len(per) == 114 and sum(len(v) for v in per.values()) == 49968 \
        and len(glob) == 1642, 'QAC corpus stats do not match H-NEW-111'

    # ---- A. reproduce the published matrix, entry-by-entry and on both headline scalars
    D_full = fr_matrix(per, top)
    with open(H111) as f:
        stored = json.load(f)
    D_stored = np.zeros((114, 114))
    for i, j, d in stored['D_matrix_upper_triangular']:
        D_stored[i - 1, j - 1] = D_stored[j - 1, i - 1] = d
    max_entry_diff = float(np.abs(D_full - D_stored).max())
    rep_muq, rep_hm = dbar(D_full, SET_MUQ), dbar(D_full, SET_HM)
    ok_muq = abs(rep_muq - PUBLISHED_DBAR_MUQ) < 1e-12
    ok_hm = abs(rep_hm - PUBLISHED_DBAR_HM) < 1e-12
    ok_mat = max_entry_diff == 0.0
    log('[A] max |rebuilt - stored| over all 6441 pairs = %r  %s'
        % (max_entry_diff, 'IDENTICAL' if ok_mat else 'DIFFERS'))
    log('[A] d̄(muq-29) %.15f vs published %.15f  %s'
        % (rep_muq, PUBLISHED_DBAR_MUQ, 'OK' if ok_muq else 'MISMATCH'))
    log('[A] d̄(HM-7)   %.15f vs published %.15f  %s'
        % (rep_hm, PUBLISHED_DBAR_HM, 'OK' if ok_hm else 'MISMATCH'))
    if not (ok_muq and ok_hm and ok_mat):
        raise SystemExit('HARNESS FAIL: FR matrix does not reproduce H-NEW-570/111.')

    # ---- channel: log word count, from H-NEW-126's frozen profile builder
    import h_new_126_isolate_core as M126
    surahs = M126.load_quran('no-tashkeel')
    root_counts = M126.load_surah_root_counts()
    profiles = M126.compute_profiles(surahs, root_counts,
                                     M126.load_noldeke(), M126.load_period(),
                                     M126.compute_rhetorical_triples(surahs))
    logwc = np.array([np.log(profiles[s]['total_tokens']) for s in range(1, 115)])
    bins = rank_bins(logwc, N_BINS)

    # ---- C. matched null, full vs Book-roots-removed
    D_nobook = fr_matrix(per, top, drop=BOOK_ROOTS)
    arms = {}
    for label, D in (('full_500', D_full), ('book_roots_removed_498', D_nobook)):
        arms[label] = {}
        for sl, sd in (('primary', SEED), ('replication', SEED_REP)):
            for gname, gids in (('muq29', SET_MUQ), ('hm7', SET_HM)):
                pct, stats, err = matched_pct(D, gids, bins, sd)
                arms[label].setdefault(sl, {})[gname] = dict(
                    matched_percentile=pct, error=err, **(stats or {}))
                log('[C] %-24s %-10s %-6s pct=%s  ratio=%s'
                    % (label, sl, gname,
                       ('%.2f' % pct) if pct is not None else err,
                       ('%.4f' % stats['ratio']) if stats else '-'))

    # ---- D. frequency-matched control pairs
    ktb_n, qra_n = glob['ktb'], glob['qrA']
    pool_a = [r for r in top if r not in BOOK_ROOTS
              and abs(glob[r] - ktb_n) <= FREQ_TOL * ktb_n]
    pool_b = [r for r in top if r not in BOOK_ROOTS
              and abs(glob[r] - qra_n) <= FREQ_TOL * qra_n]
    log('[D] frequency-matched pools: %d near ktb(%d), %d near qrA(%d)'
        % (len(pool_a), ktb_n, len(pool_b), qra_n))
    rngc = random.Random(SEED)
    seen, ctrl = set(), []
    while len(ctrl) < N_CONTROL_PAIRS and len(seen) < 20 * N_CONTROL_PAIRS:
        pair = (rngc.choice(pool_a), rngc.choice(pool_b))
        if pair[0] == pair[1] or pair in seen:
            seen.add(pair)
            continue
        seen.add(pair)
        Dc = fr_matrix(per, top, drop=pair)
        row = dict(pair=list(pair), freq=[glob[pair[0]], glob[pair[1]]])
        for gname, gids in (('muq29', SET_MUQ), ('hm7', SET_HM)):
            pct, st, err = matched_pct(Dc, gids, bins, SEED)
            row[gname] = dict(matched_percentile=pct, ratio=st['ratio'] if st else None)
        ctrl.append(row)
        if len(ctrl) % 25 == 0:
            log('[D] %d/%d control pairs' % (len(ctrl), N_CONTROL_PAIRS))
            with open(os.path.join(PROGRESS, 'ctrl-%s-%04d.json' % (RUNSTAMP, len(ctrl))),
                      'x', encoding='utf-8') as f:
                json.dump(ctrl, f)

    summary = {}
    for gname in ('muq29', 'hm7'):
        base = arms['full_500']['primary'][gname]['matched_percentile']
        book = arms['book_roots_removed_498']['primary'][gname]['matched_percentile']
        shifts = [c[gname]['matched_percentile'] - base for c in ctrl]
        book_shift = book - base
        summary[gname] = dict(
            pct_full=base, pct_book_removed=book, book_shift=book_shift,
            control_shift_mean=float(np.mean(shifts)),
            control_shift_sd=float(np.std(shifts, ddof=1)),
            control_shift_min=float(np.min(shifts)),
            control_shift_max=float(np.max(shifts)),
            control_pcts=dict(mean=float(np.mean([c[gname]['matched_percentile'] for c in ctrl])),
                              p95=float(np.percentile([c[gname]['matched_percentile'] for c in ctrl], 95))),
            frac_controls_shift_ge_book=float(np.mean([s >= book_shift for s in shifts])),
        )
        log('[SUM] %s: full %.2f -> book-removed %.2f (shift %+.2f); '
            'control shift mean %+.2f sd %.2f, max %+.2f; '
            '%.1f%% of controls shift at least as far'
            % (gname, base, book, book_shift,
               summary[gname]['control_shift_mean'], summary[gname]['control_shift_sd'],
               summary[gname]['control_shift_max'],
               100 * summary[gname]['frac_controls_shift_ge_book']))

    out = dict(
        finding_id='H-NEW-2830-independence', utc=RUNSTAMP,
        question='Is H-NEW-2820 muqattaat content-clustering the same signal as Pillar 1 '
                 'book-reference, measured through a shared vocabulary?',
        method=dict(k_top=K_TOP, dirichlet_alpha=DIR_ALPHA, n_perm=N_PERM,
                    n_bins=N_BINS, channel='log word count (H-NEW-2820 dominant, rho=+0.8998)',
                    seeds=[SEED, SEED_REP], book_roots=BOOK_ROOTS,
                    n_control_pairs=len(ctrl), freq_tol=FREQ_TOL),
        reproduction=dict(dbar_muq29=rep_muq, dbar_hm7=rep_hm,
                          published_muq29=PUBLISHED_DBAR_MUQ,
                          published_hm7=PUBLISHED_DBAR_HM,
                          max_entry_diff_vs_stored=max_entry_diff,
                          bit_identical=bool(ok_muq and ok_hm and ok_mat)),
        book_root_ranks=dict(ktb=dict(rank=top.index('ktb') + 1, tokens=glob['ktb']),
                             qrA=dict(rank=top.index('qrA') + 1, tokens=glob['qrA'])),
        arms=arms, controls=ctrl, summary=summary,
    )
    with open(os.path.join(RUNDIR, 'results.json'), 'x', encoding='utf-8') as f:
        json.dump(out, f, indent=2)
    log('[done] %s' % RUNDIR)


if __name__ == '__main__':
    main()
