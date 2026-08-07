#!/usr/bin/env python3
"""H-NEW-2840 POST-HOC — the contiguity control, at full strength.

NOT CONFIRMATORY.  Own run directory, no verdict, not in the Bonferroni family.  These
arms were specified AFTER the registered run had been executed and read, so they cannot
change the registered verdict and are not offered as if they could.

Why it exists.  The registered `FAM-c` control compared each letter class to random
contiguous mushaf runs and is size-confounded (rho = +0.838 between a run's d-bar and its
own mean log word count; POSTHOC D2).  The first repair added a size caliper but NOT
period, and never asked the decomposition question.  The hawamim are the consecutive run
Q 40-46 and are the one class that clears the registered bar, so the question "are they
tighter than ANY seven consecutive surahs of the same size and period would be?" decides
what that arm is worth.

Four arms:

  C1  EXACT ENUMERATION.  Every contiguous run of length n in the mushaf -- 114-n+1 of
      them, no sampling -- and the subset matching the class on mean log word count
      (caliper) AND on number of Medinan surahs exactly.  The class's rank among them is
      exact, not a Monte-Carlo estimate.
  C2  The same with Monte-Carlo size+period-stratified consecutive blocks, for the classes
      where the exact reference set is too small to rank against.
  C3  DECOMPOSITION of the muqattaat-29: within-run pairs against between-run pairs, and
      d-bar restricted to pairs at mushaf gap >= K for K in {2,5,10}, scored against the
      registered N_PERIOD null with the identical restriction applied to every draw.  At
      K = 10 no within-class pair survives except ALM's, by construction.
  C4  Delta (within-class vs between-class) under the same gap restrictions.
"""
from __future__ import annotations

import itertools
import json
import os
import sys
import time
from collections import Counter
from datetime import datetime, timezone

import numpy as np

PROJECT = '/Users/grey/Downloads/quran'
sys.path.insert(0, os.path.join(PROJECT, 'findings/phase-b-hypotheses/scripts'))
sys.path.insert(0, os.path.join(PROJECT, 'analysis'))
sys.path.insert(0, os.path.join(PROJECT, 'scripts'))

import importlib.util                                                   # noqa: E402
_spec = importlib.util.spec_from_file_location(
    'h2840', os.path.join(PROJECT, 'findings/phase-b-hypotheses/scripts/h-new-2840.py'))
H = importlib.util.module_from_spec(_spec)
sys.modules['h2840'] = H
_spec.loader.exec_module(H)

RUNSTAMP = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
RUNDIR = os.path.join(PROJECT,
                      'findings/phase-b-hypotheses/runs/h-new-2840-posthoc-contiguity', RUNSTAMP)
N = H.N_PERM_QURAN
SEED = H.SEED_PRIMARY
CALIPER = 0.25

SETS = {
    'HM_6':       [40, 41, 43, 44, 45, 46],
    'HAWAMIM_7':  [40, 41, 42, 43, 44, 45, 46],
    'ALR_5':      [10, 11, 12, 14, 15],
    'TAWASIN_3':  [26, 27, 28],
    'TSM_2':      [26, 28],
    'ALM_6':      [2, 3, 29, 30, 31, 32],
    'ALM_block_29_32': [29, 30, 31, 32],
    'ALM_block_2_3':   [2, 3],
    'MUQ_29':     H.SET_MUQ,
}


def maximal_runs(ids):
    ids = sorted(ids)
    runs, cur = [], [ids[0]]
    for x in ids[1:]:
        if x == cur[-1] + 1:
            cur.append(x)
        else:
            runs.append(cur)
            cur = [x]
    runs.append(cur)
    return runs


def main():
    H.verify_locks()
    os.makedirs(RUNDIR, exist_ok=False)
    H.log('[posthoc-contiguity] %s' % RUNDIR)
    t0 = time.time()

    Dfz = H.load_frozen_D()
    import h_new_126_isolate_core as M126
    surahs_obj = H.load_quran('no-tashkeel')
    root_counts = M126.load_surah_root_counts()
    noldeke, period = M126.load_noldeke(), M126.load_period()
    triples = M126.compute_rhetorical_triples(surahs_obj)
    profiles = M126.compute_profiles(surahs_obj, root_counts, noldeke, period, triples)
    ids = list(range(1, 115))
    lwc = np.log(np.array([float(profiles[s]['total_tokens']) for s in ids]))
    medinan = np.array([1 if period[s].lower().startswith('medin') else 0 for s in ids])
    cross_strata = H.rank_bins(lwc, 5) * 2 + medinan
    allpos = list(range(114))

    out = dict(finding_id='H-NEW-2840-POSTHOC-CONTIGUITY', utc=RUNSTAMP,
               status='POST-HOC — specified after the registered run was read; descriptive '
                      'only; carries no verdict and is not in the Bonferroni family',
               rundir=os.path.relpath(RUNDIR, PROJECT), caliper=CALIPER)

    # ---------------- C1 exact enumeration of every contiguous run ----------------
    H.log('[C1] exact enumeration of contiguous runs ...')
    c1 = {}
    for name, mem in SETS.items():
        n = len(mem)
        if n > 29:
            continue
        fpos = np.array([s - 1 for s in mem])
        obs = float(Dfz[np.ix_(fpos, fpos)].sum() / (n * (n - 1)))
        tgt_lwc = float(lwc[fpos].mean())
        tgt_med = int(medinan[fpos].sum())
        rows = []
        for start in range(0, 114 - n + 1):
            rp = np.arange(start, start + n)
            rows.append(dict(start=int(start) + 1,
                             dbar=float(Dfz[np.ix_(rp, rp)].sum() / (n * (n - 1))),
                             mean_lwc=float(lwc[rp].mean()),
                             n_medinan=int(medinan[rp].sum())))
        allv = np.array([r['dbar'] for r in rows])
        size_ok = [r for r in rows if abs(r['mean_lwc'] - tgt_lwc) <= CALIPER]
        both_ok = [r for r in size_ok if r['n_medinan'] == tgt_med]
        node = dict(surahs=mem, n=n, observed=obs,
                    is_contiguous_run=bool(max(mem) - min(mem) + 1 == n),
                    target_mean_log_wc=tgt_lwc, target_n_medinan=tgt_med,
                    all_runs=dict(n=len(rows), mean=float(allv.mean()),
                                  n_at_or_below_observed=int((allv <= obs).sum()),
                                  pct=float(100.0 * (allv <= obs).sum() / len(allv))))
        for tag, sub in (('size_matched_runs', size_ok), ('size_and_period_matched_runs', both_ok)):
            v = np.array([r['dbar'] for r in sub]) if sub else np.array([])
            node[tag] = (dict(n=len(sub), note='reference set too small to rank')
                         if len(sub) < 5 else
                         dict(n=len(sub), mean=float(v.mean()), min=float(v.min()),
                              max=float(v.max()),
                              n_at_or_below_observed=int((v <= obs).sum()),
                              pct=float(100.0 * (v <= obs).sum() / len(v)),
                              rank_of_observed=int((v < obs).sum()) + 1,
                              tightest_run_start=int(sub[int(np.argmin(v))]['start'])))
        c1[name] = node
    out['C1_exact_enumeration'] = c1

    # ---------------- C2 Monte-Carlo consecutive blocks, size x period stratified -------
    H.log('[C2] Monte-Carlo size+period matched consecutive blocks ...')
    c2 = {}
    rng = np.random.default_rng(SEED + 201)
    for name, mem in SETS.items():
        n = len(mem)
        if n > 29:
            continue
        fpos = np.array([s - 1 for s in mem])
        obs = float(Dfz[np.ix_(fpos, fpos)].sum() / (n * (n - 1)))
        tgt_lwc = float(lwc[fpos].mean())
        tgt_med = int(medinan[fpos].sum())
        st = rng.integers(0, 114 - n + 1, size=400000)
        runs = st[:, None] + np.arange(n)[None, :]
        ok = (np.abs(lwc[runs].mean(axis=1) - tgt_lwc) <= CALIPER) & \
             (medinan[runs].sum(axis=1) == tgt_med)
        sel = runs[ok][:N]
        node = dict(n=n, observed=obs, n_qualifying_draws=int(ok.sum()))
        if len(sel) >= 200:
            v = H.set_stat_matrix(Dfz, sel)
            node.update(H.describe(v, obs), p_lower=H.p_lower(v, obs),
                        pct_le=H.pct_le(v, obs), n_used=int(len(sel)), estimable=True)
        else:
            node.update(estimable=False,
                        note='only %d size+period matched consecutive blocks' % len(sel))
        c2[name] = node
    out['C2_mc_consecutive_size_period'] = c2

    # ---------------- C3 decomposition of the 29 ----------------
    H.log('[C3] run decomposition of the 29 ...')
    S = H.SET_MUQ
    runs29 = maximal_runs(S)
    runof = {s: i for i, r in enumerate(runs29) for s in r}
    pairs = list(itertools.combinations(range(29), 2))
    within = [(i, j) for i, j in pairs if runof[S[i]] == runof[S[j]]]
    between = [(i, j) for i, j in pairs if runof[S[i]] != runof[S[j]]]
    Dsub = Dfz[np.ix_(np.array(S) - 1, np.array(S) - 1)]
    wv = float(np.mean([Dsub[i, j] for i, j in within]))
    bv = float(np.mean([Dsub[i, j] for i, j in between]))
    c3 = dict(runs=[dict(length=len(r), surahs=r) for r in runs29],
              n_runs=len(runs29),
              n_surahs_in_a_run_ge_2=int(sum(len(r) for r in runs29 if len(r) > 1)),
              within_run_pairs=len(within), between_run_pairs=len(between),
              mean_within_run_d=wv, mean_between_run_d=bv, difference=wv - bv,
              gap_restricted={})

    # d-bar restricted to pairs at mushaf gap >= K, identical restriction on every draw
    rngg = np.random.default_rng(SEED + 202)
    draws, err = H.draw_stratified(rngg, cross_strata, np.array(S) - 1, allpos, N)
    if err:
        c3['gap_restricted'] = dict(estimable=False, note=err)
    else:
        # every pair index once; the gap test is applied to each draw's OWN mushaf positions,
        # so a null draw is restricted exactly as the observation is
        PI = np.array([i for i, j in pairs])
        PJ = np.array([j for i, j in pairs])
        for K in (1, 2, 5, 10):
            gpos = np.array(S) - 1
            keep = [(i, j) for i, j in pairs if abs(gpos[j] - gpos[i]) >= K]
            obsK = float(np.mean([Dsub[i, j] for i, j in keep]))
            vals = np.empty(len(draws))
            for a in range(0, len(draws), 2000):
                d = np.sort(draws[a:a + 2000], axis=1)
                pi, pj = d[:, PI], d[:, PJ]
                m = (pj - pi) >= K
                sub = Dfz[pi, pj]
                vals[a:a + len(d)] = np.where(m, sub, np.nan).mean(axis=1) if m.all() \
                    else np.nansum(np.where(m, sub, np.nan), axis=1) / m.sum(axis=1)
            c3['gap_restricted']['K%d' % K] = dict(
                n_pairs_observed=len(keep),
                **H.describe(vals, obsK), p_lower=H.p_lower(vals, obsK),
                pct_le=H.pct_le(vals, obsK))
    out['C3_decomposition'] = c3

    # ---------------- C4 Delta under the same gap restriction ----------------
    H.log('[C4] Delta under gap restriction ...')
    c4 = {}
    for pname, part in (('P1', H.P1), ('P2', H.P2)):
        lab, _ = H.class_label_vector(S, part)
        node = {}
        gpos = np.array(S) - 1
        for K in (1, 2, 5, 10):
            keep = [(i, j) for i, j in pairs if abs(gpos[j] - gpos[i]) >= K]
            same = np.array([lab[i] == lab[j] for i, j in keep])
            dv = np.array([Dsub[i, j] for i, j in keep])
            if same.sum() == 0 or (~same).sum() == 0:
                node['K%d' % K] = dict(estimable=False,
                                       note='no within-class pair survives the restriction')
                continue
            w, b = float(dv[same].mean()), float(dv[~same].mean())
            obsD = w - b
            rngp = np.random.default_rng(SEED + 203)
            perm = H.perm_labels_free(rngp, lab, N)
            nv = np.empty(N)
            ii = np.array([i for i, j in keep]); jj = np.array([j for i, j in keep])
            for t in range(N):
                sm = perm[t][ii] == perm[t][jj]
                nv[t] = dv[sm].mean() - dv[~sm].mean() if 0 < sm.sum() < len(sm) else 0.0
            keys = sorted(part)
            surviving = sorted({keys[lab[i]] for i, j in keep if lab[i] == lab[j]})
            node['K%d' % K] = dict(n_pairs=len(keep), n_within=int(same.sum()),
                                   W=w, B=b, delta=obsD,
                                   p_lower_F1=H.p_lower(nv, obsD),
                                   classes_still_contributing=surviving)
        c4[pname] = node
    out['C4_delta_gap_restricted'] = c4

    # ---------------- C5 cross-block pairs only, per class ----------------
    # Every letter class except TSM is partly a contiguous run. Setting adjacency aside
    # entirely: are the SEPARATED members of a class close to each other?  The null draws a
    # size x period matched substitute for every member and scores the same cross-block
    # pairs, so the block structure is held fixed by construction.
    H.log('[C5] cross-block pairs only ...')
    c5 = {}
    for name in ('ALM_6', 'ALR_5', 'HM_6', 'HAWAMIM_7', 'TSM_2'):
        mem = SETS[name]
        rr = maximal_runs(mem)
        if len(rr) < 2:
            c5[name] = dict(note='single contiguous run — no cross-block pair exists')
            continue
        blockof = {s: bi for bi, r in enumerate(rr) for s in r}
        idx = {s: k for k, s in enumerate(mem)}
        crosspairs = [(idx[a], idx[b]) for a, b in itertools.combinations(mem, 2)
                      if blockof[a] != blockof[b]]
        withinb = [(idx[a], idx[b]) for a, b in itertools.combinations(mem, 2)
                   if blockof[a] == blockof[b]]
        mpos = np.array(mem) - 1
        Dm = Dfz[np.ix_(mpos, mpos)]
        obsC = float(np.mean([Dm[i, j] for i, j in crosspairs]))
        obsW = (float(np.mean([Dm[i, j] for i, j in withinb])) if withinb else None)
        rngc = np.random.default_rng(SEED + 204)
        dr, er = H.draw_stratified(rngc, cross_strata, mpos, allpos, N)
        node = dict(surahs=mem, blocks=[r for r in rr],
                    n_cross_pairs=len(crosspairs), n_within_block_pairs=len(withinb),
                    mean_cross_block_d=obsC, mean_within_block_d=obsW)
        if er:
            node.update(estimable=False, note=er)
        else:
            # draw_stratified emits columns grouped by stratum id; map them back to member order
            memstrata = [int(cross_strata[p]) for p in mpos]
            col_member = [k for b in sorted(set(memstrata))
                          for k in range(len(mpos)) if memstrata[k] == b]
            inv = np.empty(len(mpos), int)
            inv[col_member] = np.arange(len(mpos))
            ii = np.array([i for i, j in crosspairs])
            jj = np.array([j for i, j in crosspairs])
            vals = np.empty(len(dr))
            for a in range(0, len(dr), 2000):
                d = dr[a:a + 2000][:, inv]
                vals[a:a + len(d)] = Dfz[d[:, ii], d[:, jj]].mean(axis=1)
            node.update(H.describe(vals, obsC), estimable=True,
                        p_lower=H.p_lower(vals, obsC), pct_le=H.pct_le(vals, obsC))
        c5[name] = node
    out['C5_cross_block_only'] = c5

    out['elapsed_seconds'] = round(time.time() - t0, 1)
    with open(os.path.join(RUNDIR, 'results.json'), 'x', encoding='utf-8') as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=float)
    H.log('[done] %.0fs -> %s/results.json' % (out['elapsed_seconds'], RUNDIR))

    print('\n=== C1 exact enumeration: rank among ALL contiguous runs of the same length ===')
    for k, v in c1.items():
        sp = v['size_and_period_matched_runs']
        print(' %-16s n=%2d obs=%.5f | all %3d runs: pct %6.2f | size+period matched: %s'
              % (k, v['n'], v['observed'], v['all_runs']['n'], v['all_runs']['pct'],
                 ('n=%d pct=%.2f rank %d/%d' % (sp['n'], sp['pct'], sp['rank_of_observed'],
                                                sp['n'])) if 'pct' in sp else sp.get('note')))
    print('\n=== C3 decomposition of the 29 ===')
    print(' %d maximal runs; %d of 29 in a run >= 2; within-run d = %.5f, between-run d = %.5f'
          % (c3['n_runs'], c3['n_surahs_in_a_run_ge_2'], wv, bv))
    for K, v in c3['gap_restricted'].items():
        if isinstance(v, dict) and 'observed' in v:
            print('  gap>=%-3s pairs=%3d obs=%.5f null=%.5f z=%+.2f p=%.5f pct=%.2f'
                  % (K[1:], v['n_pairs_observed'], v['observed'], v['null_mean'], v['z'],
                     v['p_lower'], v['pct_le']))
    print('\n=== C4 Delta under gap restriction (P1) ===')
    for K, v in c4['P1'].items():
        if v.get('estimable') is False:
            print('  gap>=%-3s %s' % (K[1:], v['note']))
        else:
            print('  gap>=%-3s within=%2d delta=%+.5f p=%.5f  classes: %s'
                  % (K[1:], v['n_within'], v['delta'], v['p_lower_F1'],
                     v['classes_still_contributing']))


if __name__ == '__main__':
    main()
