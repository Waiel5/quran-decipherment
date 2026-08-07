#!/usr/bin/env python3
"""H-NEW-2840 POST-HOC — descriptive diagnostics, computed AFTER the registered verdicts.

NOT CONFIRMATORY.  Nothing here enters any decision rule, changes any verdict, or is
counted in the Bonferroni family of the pre-registration.  It has its own run directory.

Six diagnostics, each written because reading the registered run raised the question:

  D1  null-overlap.  How many of the observed 29 does a matched null draw itself contain?
      This bounds the power of every matched arm in the registered run and is the number a
      reader needs beside every p-value there.
  D2  the FAM-c adjacency control is size-confounded, and this measures by how much.
      A random contiguous mushaf run is mostly short surahs, and short surahs are close
      under Dirichlet smoothing, so FAM-c reintroduces the very channel the finding
      controls.  A size-conditional adjacency arm is supplied in its place.
  D3  the actual distinguishing-root lists under weaker nulls, so the descriptive
      deliverable exists even though the registered max-statistic arm returned NULL.
  D4  the same for the hawamim against a size x period matched 7-set null.
  D5  leave-one-class-out Delta: where in the partition does the effect live?
  D6  sub-cluster membership at k = 2..6, named.
  D7  two sets the repository queued in April 2026 and never ran, both of which this
      harness answers for free: H-NEW-600 §9's ALMR-extended-6 (= ALR-5 union Q 13) and
      its Q 29-32 four-tuple, al-Biqai's "tight Meccan block" inside ALM.
  D8  H-NEW-600's own two headline sets under the matched null its published design
      lacked, beside a reproduction of its published numbers.

Write-once: run directory created with exist_ok=False, every file opened with mode 'x'.
"""
from __future__ import annotations

import hashlib
import json
import os
import random
import re
import sys
import time
from collections import Counter, defaultdict
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
RUNDIR = os.path.join(PROJECT, 'findings/phase-b-hypotheses/runs/h-new-2840-posthoc', RUNSTAMP)
N = H.N_PERM_QURAN
SEED = H.SEED_PRIMARY


def main():
    H.verify_locks()
    os.makedirs(RUNDIR, exist_ok=False)
    H.log('[posthoc] %s' % RUNDIR)
    t0 = time.time()

    Dfz = H.load_frozen_D()
    gm = np.array([s - 1 for s in H.SET_MUQ])
    obsset = set(int(x) for x in gm)

    import h_new_126_isolate_core as M126
    surahs_obj = H.load_quran('no-tashkeel')
    root_counts = M126.load_surah_root_counts()
    noldeke, period = M126.load_noldeke(), M126.load_period()
    triples = M126.compute_rhetorical_triples(surahs_obj)
    profiles = M126.compute_profiles(surahs_obj, root_counts, noldeke, period, triples)
    ids = list(range(1, 115))
    wc = np.array([float(profiles[s]['total_tokens']) for s in ids])
    lwc = np.log(wc)
    medinan = np.array([1.0 if period[s].lower().startswith('medin') else 0.0 for s in ids])
    bins5, bins10 = H.rank_bins(lwc, 5), H.rank_bins(lwc, 10)
    cross = bins5 * 2 + medinan.astype(int)
    NULLS = dict(N_PERIOD=cross, N_SIZE5=bins5, N_SIZE10=bins10)
    allpos = list(range(114))

    out = dict(finding_id='H-NEW-2840-POSTHOC', utc=RUNSTAMP,
               status='POST-HOC — descriptive only, no verdict, not in the Bonferroni family',
               rundir=os.path.relpath(RUNDIR, PROJECT))

    # ---------------- D1 null overlap ----------------
    H.log('[D1] null overlap ...')
    d1 = {}
    for name, b in NULLS.items():
        rng = np.random.default_rng(SEED + 11)
        draws, err = H.draw_stratified(rng, b, gm, allpos, N)
        if err:
            d1[name] = dict(estimable=False, note=err)
            continue
        ov = np.array([len(obsset & set(int(x) for x in d)) for d in draws], float)
        d1[name] = dict(mean_overlap=float(ov.mean()), sd=float(ov.std(ddof=1)),
                        min=int(ov.min()), max=int(ov.max()),
                        median=float(np.median(ov)), n_group=29,
                        frac_of_group=float(ov.mean() / 29.0))
    r570 = random.Random(H.SEED_570)
    pub = np.array([[x - 1 for x in r570.sample(ids, 29)] for _ in range(N)])
    ovp = np.array([len(obsset & set(int(x) for x in d)) for d in pub], float)
    d1['N_PUB_size_blind'] = dict(mean_overlap=float(ovp.mean()), sd=float(ovp.std(ddof=1)),
                                  min=int(ovp.min()), max=int(ovp.max()),
                                  frac_of_group=float(ovp.mean() / 29.0))
    out['D1_null_overlap'] = d1

    # ---------------- D2 adjacency, diagnosed and repaired ----------------
    H.log('[D2] adjacency control ...')
    d2 = dict(diagnosis={}, size_conditional={})
    for n in (2, 3, 5, 6, 7):
        rng = np.random.default_rng(SEED + 66)
        st = rng.integers(0, 114 - n + 1, size=N)
        runs = st[:, None] + np.arange(n)[None, :]
        v = H.set_stat_matrix(Dfz, runs)
        meanlog = lwc[runs].mean(axis=1)
        d2['diagnosis']['n%d' % n] = dict(
            run_null_mean=float(v.mean()),
            rho_dbar_vs_mean_log_word_count=H.spearman(v, meanlog),
            mean_log_wc_of_runs=float(meanlog.mean()),
            mean_log_wc_of_all_114=float(lwc.mean()))
    for fam, mem in list(H.P1.items()) + list(H.P2.items()):
        if len(mem) < 2:
            continue
        key = fam if fam in H.P1_MULTI else 'P2:' + fam
        fpos = np.array([s - 1 for s in mem])
        n = len(mem)
        obs = float(Dfz[np.ix_(fpos, fpos)].sum() / (n * (n - 1)))
        target = float(lwc[fpos].mean())
        rng = np.random.default_rng(SEED + 67)
        st = rng.integers(0, 114 - n + 1, size=200000)
        runs = st[:, None] + np.arange(n)[None, :]
        keep = np.abs(lwc[runs].mean(axis=1) - target) <= 0.25
        sel = runs[keep][:N]
        node = dict(family=key, n=n, observed=obs, target_mean_log_wc=target,
                    n_qualifying_runs=int(keep.sum()),
                    caliper=0.25)
        if len(sel) >= 200:
            v = H.set_stat_matrix(Dfz, sel)
            node.update(H.describe(v, obs), p_lower=H.p_lower(v, obs),
                        pct_le=H.pct_le(v, obs), n_used=len(sel), estimable=True)
        else:
            node.update(estimable=False,
                        note='only %d size-conditional runs qualify' % len(sel))
        d2['size_conditional'][key] = node
    out['D2_adjacency'] = d2

    # ---------------- roots ----------------
    per_surah_roots, glob = H.load_qac_roots()
    tested = [r for r, c in glob.items() if c >= H.ROOT_MIN_COUNT]
    tested.sort(key=lambda r: (-glob[r], r))
    ridx = {r: i for i, r in enumerate(tested)}
    CNT = np.zeros((114, len(tested)))
    for sid in range(1, 115):
        for r in per_surah_roots[sid]:
            j = ridx.get(r)
            if j is not None:
                CNT[sid - 1, j] += 1.0
    total = CNT.sum(axis=0)
    prior = H.PRIOR_A0 * (total / total.sum())

    def vocab(grouppos, restpos, nullname, label, ndraw=N, topn=45):
        yG = CNT[grouppos].sum(axis=0)
        yR = CNT[restpos].sum(axis=0)
        z = H.logodds_z(yG, yR, prior)
        node = dict(label=label, null=nullname, n_group=len(grouppos),
                    n_rest=len(restpos))
        if nullname == 'UNMATCHED':
            rng = np.random.default_rng(SEED + 200)
            draws = H.draw_unmatched(rng, allpos, len(grouppos), ndraw)
        else:
            rng = np.random.default_rng(SEED + 201)
            draws, err = H.draw_stratified(rng, NULLS[nullname], grouppos, allpos, ndraw)
            if err:
                node['estimable'] = False
                node['note'] = err
                return node
        tot = CNT.sum(axis=0)
        zn = np.empty((len(draws), len(tested)), np.float32)
        for a in range(0, len(draws), 500):
            d = draws[a:a + 500]
            g = CNT[d].sum(axis=1)
            zn[a:a + len(d)] = H.logodds_z(g, tot[None, :] - g, prior[None, :]).astype(np.float32)
        ge = (zn >= z[None, :].astype(np.float32)).sum(axis=0)
        le = (zn <= z[None, :].astype(np.float32)).sum(axis=0)
        p = np.minimum(1.0, 2.0 * np.minimum((1 + ge) / (1 + len(draws)),
                                             (1 + le) / (1 + len(draws))))
        keep = H.bh_reject(p, H.BH_Q)
        nG, nR = float(yG.sum()), float(yR.sum())
        node['max_abs_z_observed'] = float(np.abs(z).max())
        node['max_abs_z_null_mean'] = float(np.abs(zn).max(axis=1).mean())
        node['max_abs_z_p_upper'] = H.p_upper(np.abs(zn).max(axis=1), float(np.abs(z).max()))
        node['n_bh_surviving'] = int(keep.sum())
        rows = []
        for i in np.argsort(-np.abs(z))[:topn]:
            rows.append(dict(root=tested[i], arabic=H.bw2ar(tested[i]),
                             count_total=int(total[i]),
                             count_group=int(yG[i]), count_rest=int(yR[i]),
                             rate_per_10k_group=float(1e4 * yG[i] / nG),
                             rate_per_10k_rest=float(1e4 * yR[i] / nR),
                             z=float(z[i]), p_matched=float(p[i]),
                             bh_survives=bool(keep[i]),
                             direction='ENRICHED' if z[i] > 0 else 'DEPLETED'))
        node['top_by_abs_z'] = rows
        return node

    H.log('[D3] vocabulary, 29 vs 85 ...')
    rest85 = [s - 1 for s in ids if s not in H.SET_MUQ]
    out['D3_vocab_29_vs_85'] = {
        nm: vocab(list(gm), rest85, nm, 'muqattaat-29 vs the other 85')
        for nm in ('UNMATCHED', 'N_SIZE5', 'N_PERIOD')}

    H.log('[D4] vocabulary, hawamim ...')
    hm7 = [40, 41, 42, 43, 44, 45, 46]
    hpos = [s - 1 for s in hm7]
    out['D4_vocab_hawamim'] = dict(
        vs_all_107={nm: vocab(hpos, [s - 1 for s in ids if s not in hm7], nm,
                              'hawamim-7 vs the other 107')
                    for nm in ('UNMATCHED', 'N_PERIOD')},
        vs_other22=vocab(hpos, [s - 1 for s in H.SET_MUQ if s not in hm7], 'UNMATCHED',
                         'hawamim-7 vs the other 22 muqattaat'))

    # ---------------- D5 leave-one-class-out delta ----------------
    H.log('[D5] leave-one-class-out delta ...')
    Dsub = Dfz[np.ix_(gm, gm)]
    d5 = {}
    for pname, part in (('P1', H.P1), ('P2', H.P2)):
        lab, keys = H.class_label_vector(H.SET_MUQ, part)
        base = H.delta_stat(Dsub, lab)
        node = dict(full_delta=base[0], W=base[1], B=base[2], drops={})
        for drop in [k for k, v in part.items() if len(v) >= 2]:
            sub = {k: v for k, v in part.items() if k != drop}
            keep_ids = [s for k, v in sub.items() for s in v]
            keep_ids = [s for s in H.SET_MUQ if s in set(keep_ids)]
            pos = [H.SET_MUQ.index(s) for s in keep_ids]
            Dk = Dsub[np.ix_(pos, pos)]
            lab2, _ = H.class_label_vector(keep_ids, sub)
            d, w, b, npw, npb = H.delta_stat(Dk, lab2)
            rng = np.random.default_rng(SEED + 22)
            perm = H.perm_labels_free(rng, lab2, N)
            v = np.array([H.delta_stat(Dk, perm[i])[0] for i in range(N)])
            node['drops'][drop] = dict(n_remaining=len(keep_ids), delta=d, W=w, B=b,
                                       n_within_pairs=npw,
                                       p_lower_F1=H.p_lower(v, d))
        # restrict to members of multi-member classes only: the registered Delta is
        # diluted by classes of size 1, which contribute no within-pair by construction
        sub = {k: v for k, v in part.items() if len(v) >= 2}
        keep_ids = [s for s in H.SET_MUQ if any(s in v for v in sub.values())]
        pos = [H.SET_MUQ.index(s) for s in keep_ids]
        Dk = Dsub[np.ix_(pos, pos)]
        lab2, _ = H.class_label_vector(keep_ids, sub)
        d, w, b, npw, npb = H.delta_stat(Dk, lab2)
        rng = np.random.default_rng(SEED + 22)
        perm = H.perm_labels_free(rng, lab2, N)
        v = np.array([H.delta_stat(Dk, perm[i])[0] for i in range(N)])
        node['multi_member_only'] = dict(
            n_remaining=len(keep_ids), surahs=keep_ids, delta=d, W=w, B=b,
            n_within_pairs=npw, n_between_pairs=npb, p_lower_F1=H.p_lower(v, d))
        d5[pname] = node
    out['D5_leave_one_class_out'] = d5

    # ---------------- D6 named cuts ----------------
    merges, labk = H.upgma(Dsub)
    out['D6_cuts'] = {}
    for k in (2, 3, 4, 5, 6):
        groups = defaultdict(list)
        for i, s in enumerate(H.SET_MUQ):
            groups[int(labk[k][i])].append(s)
        out['D6_cuts'][str(k)] = {
            str(c): dict(surahs=v, n=len(v),
                         classes=sorted({cl for s in v for cl, mm in H.P1.items() if s in mm}),
                         within=float(Dsub[np.ix_([H.SET_MUQ.index(x) for x in v],
                                                  [H.SET_MUQ.index(x) for x in v])].sum()
                                      / (len(v) * (len(v) - 1))) if len(v) > 1 else None,
                         median_word_count=float(np.median(wc[[s - 1 for s in v]])))
            for c, v in sorted(groups.items())}
        out['D6_cuts'][str(k)]['silhouette'] = H.silhouette(Dsub, labk[k])

    # ---------------- D7/D8 sets the repository queued and never ran ----------------
    H.log('[D7/D8] queued sets ...')
    QUEUED = {
        'ALMR_extended_6':  dict(surahs=[10, 11, 12, 13, 14, 15],
                                 source='H-NEW-600 §9 queued as H-NEW-620'),
        'ALM_tight_block_4': dict(surahs=[29, 30, 31, 32],
                                  source='H-NEW-600 §9 queued as H-NEW-630; '
                                         'al-Biqai Nazm al-Durar "tight Meccan block"'),
        'ALM_6_published':   dict(surahs=[2, 3, 29, 30, 31, 32],
                                  source='H-NEW-600 PRIMARY, published %ile 43.15'),
        'ALR_5_published':   dict(surahs=[10, 11, 12, 14, 15],
                                  source='H-NEW-610 PRIMARY, published %ile 56.25'),
        'HM_7':              dict(surahs=[40, 41, 42, 43, 44, 45, 46],
                                  source='H-NEW-570 MW-5, published %ile 20.90'),
        'MW6_nonmuq_6':      dict(surahs=[5, 9, 17, 25, 33, 47],
                                  source='H-NEW-600 MW-6, published %ile 88.10'),
    }
    d7 = {}
    for name, meta in QUEUED.items():
        mem = meta['surahs']
        fpos = np.array([s - 1 for s in mem])
        n = len(mem)
        obs = float(Dfz[np.ix_(fpos, fpos)].sum() / (n * (n - 1)))
        node = dict(surahs=mem, n=n, observed=obs, source=meta['source'],
                    median_word_count=float(np.median(wc[fpos])),
                    n_medinan=int(medinan[fpos].sum()),
                    is_contiguous_run=bool(max(mem) - min(mem) + 1 == n))
        # the size-blind null H-NEW-600 and H-NEW-570 both used, regenerated
        rngu = np.random.default_rng(SEED + 300)
        vu = H.set_stat_matrix(Dfz, H.draw_unmatched(rngu, allpos, n, N))
        node['size_blind'] = dict(H.describe(vu, obs), pct_le=H.pct_le(vu, obs))
        for nm in ('N_PERIOD', 'N_SIZE5'):
            rng = np.random.default_rng(SEED + 44)
            draws, err = H.draw_stratified(rng, NULLS[nm], fpos, allpos, N)
            if err:
                node[nm] = dict(estimable=False, note=err)
                continue
            v = H.set_stat_matrix(Dfz, draws)
            node[nm] = dict(H.describe(v, obs), estimable=True,
                            p_lower=H.p_lower(v, obs), pct_le=H.pct_le(v, obs))
        d7[name] = node
    out['D7_queued_sets'] = d7

    out['elapsed_seconds'] = round(time.time() - t0, 1)
    with open(os.path.join(RUNDIR, 'results.json'), 'x', encoding='utf-8') as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=float)
    H.log('[posthoc done] %.0fs -> %s/results.json' % (out['elapsed_seconds'], RUNDIR))


if __name__ == '__main__':
    main()
