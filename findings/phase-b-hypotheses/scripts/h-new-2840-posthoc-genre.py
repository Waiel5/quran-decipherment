#!/usr/bin/env python3
"""H-NEW-2840 POST-HOC — the per-class genre control the pre-registration did not register.

NOT CONFIRMATORY.  Own run directory, no verdict, not in the Bonferroni family.

Why it exists.  Pre-reg §6 registered the genre arm at the level of the whole 29-set
(d-bar, Delta, S1) and NOT per letter-class.  The registered run then found that the
whole Delta effect is one class — the hawamim — and the hawamim occupy the CONTIGUOUS
mushaf slots 40-46.  In a matched partition of a continuous stream, contiguous slots are
contiguous chunks of the same book and share local vocabulary by construction, so the
one result the finding rests on is exactly the one most likely to be reproduced by an
arbitrary cut.  Not running this would leave the load-bearing claim uncontrolled.

Per offset, per class, in the surface instrument: the class's d-bar over the same surah
slots, and its percentile against the same log-word-count x period stratified null the
registered run uses.  200 offsets per baseline; the Quran's own verses are never
re-partitioned.
"""
from __future__ import annotations

import json
import os
import sys
import time
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
                      'findings/phase-b-hypotheses/runs/h-new-2840-posthoc-genre', RUNSTAMP)
PROGRESS = os.path.join(PROJECT, 'findings/phase-b-hypotheses/runs/h-new-2840-progress')
N_OFFSET, N_PERM = 200, 2000
SEED = H.SEED_PRIMARY

CLASSES = {
    'ALM_6':      [2, 3, 29, 30, 31, 32],
    'ALR_5':      [10, 11, 12, 14, 15],
    'TSM_2':      [26, 28],
    'HM_6':       [40, 41, 43, 44, 45, 46],
    'HAWAMIM_7':  [40, 41, 42, 43, 44, 45, 46],
    'TAWASIN_3':  [26, 27, 28],
    'MUQ_29':     H.SET_MUQ,
}


def main():
    H.verify_locks()
    os.makedirs(PROGRESS, exist_ok=True)
    os.makedirs(RUNDIR, exist_ok=False)
    H.log('[posthoc-genre] %s' % RUNDIR)
    t0 = time.time()

    import h_new_126_isolate_core as M126
    surahs_obj = H.load_quran('no-tashkeel')
    root_counts = M126.load_surah_root_counts()
    noldeke, period = M126.load_noldeke(), M126.load_period()
    triples = M126.compute_rhetorical_triples(surahs_obj)
    profiles = M126.compute_profiles(surahs_obj, root_counts, noldeke, period, triples)
    ids = list(range(1, 115))
    lwc = np.log(np.array([float(profiles[s]['total_tokens']) for s in ids]))
    medinan = np.array([1.0 if period[s].lower().startswith('medin') else 0.0 for s in ids])
    cross = H.rank_bins(lwc, 5) * 2 + medinan.astype(int)
    allpos = list(range(114))

    # the strata come from the Quran's own profile, which every matched partition inherits
    # by construction, so the draws are identical across offsets and are generated once
    draws = {}
    for name, mem in CLASSES.items():
        rng = np.random.default_rng(SEED + 44)
        fpos = np.array([s - 1 for s in mem])
        d, err = H.draw_stratified(rng, cross, fpos, allpos, N_PERM)
        draws[name] = (fpos, d, err)

    out = dict(finding_id='H-NEW-2840-POSTHOC-GENRE', utc=RUNSTAMP,
               status='POST-HOC — descriptive only, no verdict, not in the Bonferroni family',
               rundir=os.path.relpath(RUNDIR, PROJECT),
               n_offsets=N_OFFSET, n_perm=N_PERM,
               classes={k: dict(surahs=v, n=len(v),
                                is_contiguous_run=bool(max(v) - min(v) + 1 == len(v)))
                        for k, v in CLASSES.items()},
               corpora={})

    quran_units = [H.normalise_words(t) for t in H.QVERSE_TEXT]         # noqa: F821
    corpora = [('quran_surface', None, quran_units),
               ('bukhari', H.normalise_words(open(                       # noqa: F821
                   os.path.join(PROJECT, 'data/baseline-corpora/raw/bukhari-noquran.txt'),
                   encoding='utf-8').read()), None),
               ('jahiz', H.normalise_words(open(                         # noqa: F821
                   os.path.join(PROJECT, 'data/baseline-corpora/raw/jahiz-hayawan.txt'),
                   encoding='utf-8').read()), None)]

    for cname, words, fixed in corpora:
        rng = np.random.default_rng(SEED)
        if fixed is not None:
            offsets = [0]
        else:
            need = sum(H.QVERSE_WLEN)
            slack = len(words) - need
            if slack < 0:
                out['corpora'][cname] = dict(
                    error='insufficient words: have %d need %d' % (len(words), need))
                continue
            offsets = [0] + sorted(rng.integers(0, slack + 1, size=N_OFFSET - 1).tolist())
        H.log('[%s] %d offsets' % (cname, len(offsets)))
        per_offset, tg = [], time.time()
        for oi, off in enumerate(offsets):
            units, err = (fixed, None) if fixed is not None else H.partition_at(words, off)
            if err:
                continue
            Dg = H.content_matrix(H.group_matched(units))
            rec = dict(offset=int(off))
            for name, (fpos, d, derr) in draws.items():
                n = len(fpos)
                obs = float(Dg[np.ix_(fpos, fpos)].sum() / (n * (n - 1)))
                e = dict(observed=obs)
                if derr is None:
                    v = H.set_stat_matrix(Dg, d)
                    e.update(matched_pct=H.pct_le(v, obs),
                             matched_p_lower=H.p_lower(v, obs),
                             null_mean=float(v.mean()),
                             z=float((obs - v.mean()) / v.std(ddof=1)))
                else:
                    e['note'] = derr
                rec[name] = e
            per_offset.append(rec)
            if (oi + 1) % 50 == 0:
                H.log('  [%s] %d/%d  %.0fs' % (cname, oi + 1, len(offsets), time.time() - tg))
                snap = os.path.join(PROGRESS, 'phgenre-%s-%s-%04d.json'
                                    % (cname, RUNSTAMP, oi + 1))
                if not os.path.exists(snap):
                    with open(snap, 'x', encoding='utf-8') as f:
                        json.dump(dict(corpus=cname, done=oi + 1), f)
        out['corpora'][cname] = dict(n_offsets=len(per_offset), per_offset=per_offset)

    # ---- summary: how often does an arbitrary cut reach the Quran's own surface value?
    summ = {}
    q = out['corpora'].get('quran_surface', {}).get('per_offset', [{}])
    qref = q[0] if q else {}
    for cname in ('bukhari', 'jahiz'):
        node = out['corpora'].get(cname, {})
        if 'per_offset' not in node:
            continue
        e = {}
        for name in CLASSES:
            v = np.array([r[name]['matched_pct'] for r in node['per_offset']
                          if 'matched_pct' in r[name]], float)
            if not len(v):
                continue
            qv = qref.get(name, {}).get('matched_pct')
            e[name] = dict(n=len(v), min=float(v.min()), median=float(np.median(v)),
                           max=float(v.max()),
                           quran_surface_pct=qv,
                           frac_at_or_below_quran=float((v <= qv).mean())
                           if qv is not None else None,
                           frac_at_or_below_10pct=float((v <= 10.0).mean()),
                           frac_at_or_below_1pct=float((v <= 1.0).mean()))
        summ[cname] = e
    out['summary'] = summ
    out['quran_surface'] = {name: qref.get(name) for name in CLASSES}

    out['elapsed_seconds'] = round(time.time() - t0, 1)
    with open(os.path.join(RUNDIR, 'results.json'), 'x', encoding='utf-8') as f:
        json.dump(out, f, indent=2, ensure_ascii=False, default=float)
    H.log('[done] %.0fs -> %s/results.json' % (out['elapsed_seconds'], RUNDIR))

    for cname, e in summ.items():
        print('\n=== %s (200 offsets) ===' % cname)
        for name, v in e.items():
            print(' %-11s quran=%6.2f  baseline median=%6.2f  <=quran %5.1f%%  '
                  '<=10%% %5.1f%%  <=1%% %5.1f%%'
                  % (name, v['quran_surface_pct'], v['median'],
                     100 * v['frac_at_or_below_quran'], 100 * v['frac_at_or_below_10pct'],
                     100 * v['frac_at_or_below_1pct']))


if __name__ == '__main__':
    main()
