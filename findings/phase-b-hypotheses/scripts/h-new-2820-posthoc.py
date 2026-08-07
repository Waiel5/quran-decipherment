#!/usr/bin/env python3
"""H-NEW-2820 POST-HOC — descriptive only, computed AFTER the locked verdicts.

Not in the pre-registration. Enters no decision rule. Two questions raised by the
locked run and answerable with the same frozen matrices:

  P1. H-NEW-126's Cell A MW-5 positive control is the hawamim {40..44}, which are
      themselves long surahs. If that control fires on size, the "VALID DETECTOR"
      certification of the Cell A instrument is confounded. Run it through the same
      matched nulls.
  P2. The mechanical ceiling on the Cell A statistic: Jaccard is bounded above by
      min|R|/max|R|, so quantify how much of the published 2.64x enrichment the bound
      alone accounts for.

Writes to its own immutable run directory, mode 'x', once.
"""
from __future__ import annotations

import json
import os
import random
import sys
from datetime import datetime, timezone

import numpy as np

PROJECT = '/Users/grey/Downloads/quran'
sys.path.insert(0, os.path.join(PROJECT, 'findings/phase-b-hypotheses/scripts'))
sys.path.insert(0, os.path.join(PROJECT, 'scripts'))
sys.path.insert(0, os.path.join(PROJECT, 'analysis'))

import importlib.util
spec = importlib.util.spec_from_file_location(
    'h2820', os.path.join(PROJECT, 'findings/phase-b-hypotheses/scripts/h-new-2820.py'))
H = importlib.util.module_from_spec(spec)
spec.loader.exec_module(H)

RUNSTAMP = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
RUNDIR = os.path.join(PROJECT, 'findings/phase-b-hypotheses/runs/h-new-2820-posthoc', RUNSTAMP)

HAWAMIM_5 = [40, 41, 42, 43, 44]     # H-NEW-126's own MW-5 set
SEED = 20260509


def main():
    H.verify_locks()
    os.makedirs(RUNDIR, exist_ok=False)

    import h_new_126_isolate_core as M126
    root_counts = M126.load_surah_root_counts()
    root_sets = {s: frozenset(root_counts[s].keys()) for s in range(1, 115)}
    surahs = H.load_quran('no-tashkeel')
    noldeke, period = M126.load_noldeke(), M126.load_period()
    triples = M126.compute_rhetorical_triples(surahs)
    profiles = M126.compute_profiles(surahs, root_counts, noldeke, period, triples)
    channels, raw, medinan = H.build_channels(profiles, noldeke, period)

    Jroot = H.jaccard_matrix([set(root_sets[s]) for s in range(1, 115)])

    # ---- P1: the MW-5 positive control through the same matched nulls.
    # Published null pool for the MW-5 arm is "all surahs not in the control set".
    pool = [s for s in range(1, 115) if s not in HAWAMIM_5]
    r = random.Random(M126.SEED + 1)
    # the published cell_a consumes 10000 target draws first, then 10000 control draws
    for _ in range(10000):
        r.sample([s for s in range(1, 115) if s not in M126.CORE_5], 5)
    draws = np.array([[x - 1 for x in r.sample(pool, 5)] for _ in range(10000)])

    arms = H.claim_arms('H-NEW-126 Cell A MW-5 hawamim{40..44}', Jroot, HAWAMIM_5, pool,
                        draws, channels, medinan, 'jaccard', SEED,
                        alpha=H.ALPHA_BON_126, do_caliper=True)

    # ---- P2: the mechanical Jaccard ceiling
    sizes = np.array([len(root_sets[s]) for s in range(1, 115)], dtype=float)
    ceil = np.minimum.outer(sizes, sizes) / np.maximum.outer(sizes, sizes)
    np.fill_diagonal(ceil, 0.0)

    def pair_mean(M, ids):
        g = np.array([s - 1 for s in ids])
        n = len(g)
        return float(M[np.ix_(g, g)].sum() / (n * (n - 1)))

    rng = np.random.default_rng(SEED)
    noncore_pos = [s - 1 for s in range(1, 115) if s not in M126.CORE_5]
    dr = H.draw_unmatched(rng, noncore_pos, 5, 10000)
    ceil_null = H.set_stat_matrix(ceil, dr)
    j_null = H.set_stat_matrix(Jroot, dr)
    p2 = dict(
        core5_jaccard=pair_mean(Jroot, M126.CORE_5),
        core5_ceiling=pair_mean(ceil, M126.CORE_5),
        core5_fill=pair_mean(Jroot, M126.CORE_5) / pair_mean(ceil, M126.CORE_5),
        null_jaccard_mean=float(j_null.mean()),
        null_ceiling_mean=float(ceil_null.mean()),
        null_fill_mean=float((j_null / ceil_null).mean()),
        enrichment_raw=pair_mean(Jroot, M126.CORE_5) / float(j_null.mean()),
        enrichment_of_ceiling=pair_mean(ceil, M126.CORE_5) / float(ceil_null.mean()),
        note=('"fill" is the observed Jaccard as a fraction of its own mechanical ceiling '
              'min|R|/max|R|; enrichment_of_ceiling is how much of the published enrichment '
              'the ceiling alone delivers'),
    )

    out = dict(finding_id='H-NEW-2820-POSTHOC', utc=RUNSTAMP, quarantine='DESCRIPTIVE ONLY',
               P1_mw5_matched=arms, P2_jaccard_ceiling=p2)
    with open(os.path.join(RUNDIR, 'results.json'), 'x', encoding='utf-8') as f:
        json.dump(out, f, indent=2, default=float)

    a = arms
    print('\n=== P1: H-NEW-126 Cell A MW-5 (hawamim 40-44) under the SAME matched nulls ===')
    print('  dominant channel: %s' % a['dominant_channel'])
    for tag, node in (('published null', a['published_null']),
                      ('A1 conditional', a['A1_conditional_exceedance']),
                      ('A2-k5', a['A2']['k5']), ('A2-k10', a['A2']['k10']),
                      ('A2b caliper', a['A2b_caliper']),
                      ('A2c x period', a['A2c_cross_period'])):
        if 'observed' not in node:
            print('  %-16s n_restricted=%s' % (tag, node.get('n_restricted')))
            continue
        print('  %-16s obs=%.5f null_mean=%.5f z=%+.3f ratio=%.3f p=%.5f n=%d'
              % (tag, node['observed'], node['null_mean'], node['z'],
                 node['ratio_obs_over_null_mean'], node['p_upper'], node['n_draws']))
    print('\n=== P2: the mechanical Jaccard ceiling ===')
    for k, v in p2.items():
        if k != 'note':
            print('  %-24s %s' % (k, round(v, 5)))
    print('\n%s/results.json' % RUNDIR)


if __name__ == '__main__':
    main()
