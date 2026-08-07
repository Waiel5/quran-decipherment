#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2740 — declared ROBUSTNESS re-run.

The pre-registration (section 4.1) locked a *greedy* merge rule for the 363 verses
where Tanzil's simple text separates words the 'Uthmani text joins, and declared in
section 9.5 that the rule was "a heuristic, chosen for determinism ... verified only
by 6,236/6,236 coverage, not by hand-checking every merge."

That declared risk materialised. On four verses the greedy rule takes a locally
cheap m=1 merge and then shifts every remaining token of the verse by one
(Q 18:86, Q 18:94, Q 28:38, Q 40:36). This re-run replaces the greedy rule with an
EXACT dynamic-programming alignment that minimises total skeleton edit distance over
the whole verse, and re-runs every registered inference unchanged.

The primary run stands as pre-registered. This is reported beside it, never instead
of it. `findings/phase-b-hypotheses/scripts/h-new-2740.py` is imported unmodified
and only `align_verse` is overridden.

Author: Waiel Al-Shujaa    Date: 2026-08-07
"""
import datetime
import importlib.util
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location('h2740', os.path.join(HERE, 'h-new-2740.py'))
P = importlib.util.module_from_spec(spec)
spec.loader.exec_module(P)

MAX_MERGE = 4


def dp_align(u_line, s_line):
    """Exact minimum-total-edit-distance alignment of one 'Uthmani token to a run of
    1..MAX_MERGE simple tokens. Replaces prereg 4.1's greedy rule."""
    a, b = u_line.split(), s_line.split()
    if len(a) == len(b):
        return [(x, y, False) for x, y in zip(a, b)]
    ska = [P.skel(x) for x in a]
    na, nb = len(a), len(b)
    INF = float('inf')
    D = [[INF] * (nb + 1) for _ in range(na + 1)]
    B = [[0] * (nb + 1) for _ in range(na + 1)]
    D[0][0] = 0
    for i in range(na):
        for j in range(nb):
            if D[i][j] == INF:
                continue
            for m in range(1, MAX_MERGE + 1):
                if j + m > nb:
                    break
                cost = D[i][j] + P.levenshtein(ska[i], P.skel(''.join(b[j:j + m])))
                if cost < D[i + 1][j + m]:
                    D[i + 1][j + m] = cost
                    B[i + 1][j + m] = m
    if D[na][nb] == INF:
        return None
    out, i, j = [], na, nb
    while i > 0:
        m = B[i][j]
        out.append((a[i - 1], ' '.join(b[j - m:j]), m > 1))
        i -= 1
        j -= m
    return out[::-1]


if __name__ == '__main__':
    P.align_verse = dp_align
    seed = int(sys.argv[1]) if len(sys.argv) > 1 else P.SEED_PRIMARY
    stamp = datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    outdir = os.path.join(P.REPO, 'findings/phase-b-hypotheses/runs/h-new-2740',
                          f'{stamp}-robustness-dp-align-seed{seed}')
    res = P.main(seed, outdir)
    print('\nROBUSTNESS VERDICTS:', res['verdicts'])
