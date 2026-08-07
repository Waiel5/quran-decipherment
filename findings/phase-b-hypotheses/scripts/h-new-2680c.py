#!/usr/bin/env python3
"""H-NEW-2680c — NULL-C: the composed joint null.

POST-HOC, and labelled as such.  It is not in prereg-h-new-2680, but it is the direct
consequence of that pre-registration's own §1 invariance table, and it was constructed
only after the pre-registered arms showed why each of them fails:

  NULL-A  (labels + order + titles randomised, text canonical)
          valid for L1 and L2; L3 EXACTLY INVARIANT (marginal 1.000); L4 destroyed.
  NULL-B  (verses after v1 reallocated, order canonical)
          valid for L3; INVALID for L2 (marginal 1.000) and for L1 (marginal 0.83).
  NULL-B' (all verses reallocated, order canonical)
          valid for L1 and L3; still INVALID for L2 (marginal 1.000).

L2's invalidity under B/B' has one cause: reallocation homogenises the surahs, so the
Fisher-Rao geometry becomes a pure function of surah SIZE, and the mushaf order — which
is roughly size-ordered — rides that geometry.  Randomising the ORDER as well removes
the confound, because a random order of any matrix is z ~ N(0,1) by construction.

NULL-C therefore composes B' with A:
    all 6236 verses reallocated across the canonical length profile,
    the 29 marker labels reassigned at random,
    the 89 titles reassigned at random,
    the reading order permuted at random.

This is the one process in the study that is a valid null for all four laws at once.
Its purpose is to settle whether a defensible single joint null EXISTS — not to supply
a small number.  Per MW-7 any claim resting on it carries a single-test ceiling.

Reuses the pre-registered code paths verbatim by importing h-new-2680.py as a module.
Pre-reg SHA-256: 012ca709fad64bc8369313486095cc092e30414eccf45b1eca4e1b978fd08f94
"""
from __future__ import annotations

import importlib.util
import json
import math
import os
import random
import sys
import time
from collections import defaultdict
from datetime import datetime, timezone
from itertools import combinations, permutations

import numpy as np

PROJECT = '/Users/grey/Downloads/quran'
MAIN = os.path.join(PROJECT, 'findings/phase-b-hypotheses/scripts/h-new-2680.py')

spec = importlib.util.spec_from_file_location('h2680', MAIN)
h = importlib.util.module_from_spec(spec)
spec.loader.exec_module(h)          # runs pre-reg SHA verify + canonical verification

N_C = 2000
RUNSTAMP = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
RUNDIR = os.path.join(PROJECT, 'findings/phase-b-hypotheses/runs/h-new-2680c', RUNSTAMP)


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def run_null_C(n_draws, seed):
    pyrng = random.Random(seed)
    nprng = np.random.default_rng(seed)
    ind = {k: [] for k in ('L1', 'L2', 'L3', 'L4')}
    npass3, rank1s, l2z = [], [], []
    t = time.time()
    for it in range(n_draws):
        idx = h.draw_nullB(pyrng, pin_first=False)          # all verses reallocated
        order, muq, tmap = h.draw_nullA(pyrng)              # labels, order, titles random
        r1 = h.law1(idx, muq)
        D = h.fr_matrix(idx)
        r2 = h.law2(D, order, nprng)
        per3, n3 = h.law3(idx, pyrng)
        r4 = h.law4(idx, tmap)
        ind['L1'].append(h.crit_L1(r1, 'lenient'))
        ind['L2'].append(h.crit_L2(r2, 'lenient'))
        ind['L3'].append(h.crit_L3(n3, 'lenient'))
        ind['L4'].append(h.crit_L4(r4, 'lenient'))
        npass3.append(n3); rank1s.append(r4['rank1']); l2z.append(r2['z'])
        if (it + 1) % max(1, n_draws // 10) == 0:
            log(f'  [NULL-C/{seed}] {it+1}/{n_draws}  {time.time()-t:.0f}s')

    keys = ['L1', 'L2', 'L3', 'L4']
    A = {k: np.array(v, dtype=bool) for k, v in ind.items()}
    marg = {k: float(v.mean()) for k, v in A.items()}
    joint = A['L1'] & A['L2'] & A['L3'] & A['L4']
    n_joint = int(joint.sum())
    C = np.eye(4)
    phi = {}
    for a, b in combinations(range(4), 2):
        v = h.phi_coeff(A[keys[a]], A[keys[b]])
        phi[f'{keys[a]}x{keys[b]}'] = v
        if v is not None:
            C[a, b] = C[b, a] = v
    shrink = defaultdict(list)
    for perm in permutations(keys):
        cur = np.ones(n_draws, dtype=bool)
        for depth, k in enumerate(perm, 1):
            cur = cur & A[k]
            shrink[depth].append(int(cur.sum()))
    # every non-empty subset, so the reader can form any sub-conjunction
    subsets = {}
    for r in range(1, 5):
        for cmb in combinations(keys, r):
            m = np.ones(n_draws, dtype=bool)
            for k in cmb:
                m = m & A[k]
            subsets['&'.join(cmb)] = int(m.sum())
    p_joint = (n_joint + 1) / (n_draws + 1)
    return dict(
        seed=seed, n_draws=n_draws, wall_seconds=time.time() - t,
        marginals=marg, marginal_counts={k: int(v.sum()) for k, v in A.items()},
        n_joint=n_joint, p_joint_exact=p_joint, p_joint_floor=1.0 / (n_draws + 1),
        rule_of_three_95_upper=(3.0 / n_draws) if n_joint == 0 else None,
        phi=phi, m_eff_nyholt=h.m_eff_nyholt(C),
        m_eff_multiplicativity=h._m_eff_mult(p_joint, marg, keys, n_draws),
        subset_counts=subsets,
        shrinkage={d: dict(min=min(v), median=float(np.median(v)), max=max(v))
                   for d, v in shrink.items()},
        L3_npass=dict(mean=float(np.mean(npass3)), max=int(np.max(npass3))),
        L4_rank1=dict(mean=float(np.mean(rank1s)), max=int(np.max(rank1s))),
        L2_z=dict(mean=float(np.mean(l2z)), sd=float(np.std(l2z))),
        validity_check=dict(
            L1_marginal_should_be_near_alpha_0_05=marg['L1'],
            L2_marginal_should_be_near_alpha_0_05=marg['L2'],
            L3_marginal_is_a_genuine_tail=marg['L3'],
            L4_marginal_fails_from_below=marg['L4']),
        indicators={k: ''.join('1' if x else '0' for x in A[k]) for k in keys},
    )


def main():
    os.makedirs(RUNDIR, exist_ok=True)
    out = {'finding_id': 'H-NEW-2680c', 'status': 'POST-HOC (labelled) — MW-7 single-test ceiling',
           'prereg_sha256': h.EXPECTED_SHA, 'run_utc': RUNSTAMP,
           'canonical_reference': {
               'L1_p_hyper': h.can_l1[2], 'L2_z': h.can_l2['z'],
               'L3_n_pass': h.can_l3_n, 'L4_rank1': h.can_l4['rank1']}}
    log('=== NULL-C primary ===')
    out['NULL_C_primary'] = run_null_C(N_C, h.SEED_PRIMARY)
    log('=== NULL-C replication ===')
    out['NULL_C_replication'] = run_null_C(N_C, h.SEED_REPLICATION)
    for arm in ('NULL_C_primary', 'NULL_C_replication'):
        r = out[arm]
        log(f"  {arm}: marginals={ {k: round(v,4) for k,v in r['marginals'].items()} } "
            f"joint={r['n_joint']}/{r['n_draws']}")

    def default(o):
        if isinstance(o, np.bool_):
            return bool(o)
        if isinstance(o, np.integer):
            return int(o)
        if isinstance(o, np.floating):
            return float(o)
        raise TypeError(str(type(o)))

    json.dump(out, open(os.path.join(RUNDIR, 'result.json'), 'w', encoding='utf-8'),
              indent=2, ensure_ascii=False, default=default)
    json.dump({'finding_id': 'H-NEW-2680c', 'run_utc': RUNSTAMP,
               'prereg_sha256': h.EXPECTED_SHA,
               'script_sha256': h.sha256_file(os.path.abspath(__file__)),
               'imports_verbatim': os.path.relpath(MAIN, PROJECT),
               'main_script_sha256': h.sha256_file(MAIN),
               'python': sys.version, 'numpy': np.__version__},
              open(os.path.join(RUNDIR, 'manifest.json'), 'w', encoding='utf-8'),
              indent=2, ensure_ascii=False)
    log(f'wrote {RUNDIR}')


if __name__ == '__main__':
    main()
