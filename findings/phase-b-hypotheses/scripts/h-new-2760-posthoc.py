#!/usr/bin/env python3
"""H-NEW-2760 POST-HOC DIAGNOSTICS — MW-7 capped, NOT part of the registered family.

Three questions the registered run raised and could not answer, computed because
leaving a known threat to my own headline uncomputed would be worse than labelling
it.  Every number here carries the MW-7 single-test ceiling and NONE of it may be
cited as confirmatory.  It exists to bound the registered result, not to extend it.

  D1  Stratum occupancy for Null C.  H4's rate ratio fell to 1.265; is that a real
      shrinkage or an over-adjustment artefact?  If the Late-Meccan stratum is mostly
      muqaṭṭaʿāt, the within-stratum permutation has almost no freedom and the null
      mean is dragged toward the observed count by construction.

  D2  H5 restricted within phase.  H5 is length-free and token-budget-free by
      construction, but it is NOT phase-controlled.  If Late-Meccan surahs front-load
      Book vocabulary as a register feature, that alone could produce it.

  D3  The two length channels compared directly.  H2 named the opening-window budget
      as the primary nuisance and it came back weak (rho = 0.168).  Whole-surah length
      is the stronger channel (rho = 0.458).  Re-stratify Null B on whole-surah length
      to see what the effect looks like against the nuisance I did NOT name primary.

Pre-reg SHA-256: a1e4419a674d254d3bf5f243d2891bafcd17986611eff94b31f6e35b8e5b9b3a
The registered run directory is NOT touched.
"""
from __future__ import annotations

import hashlib
import json
import os
import random
import re
import sys
from collections import defaultdict
from datetime import datetime, timezone

PROJECT = '/Users/grey/Downloads/quran'
REL_PREREG = 'findings/phase-b-hypotheses/prereg-h-new-2760-muqattaat-book-reference-nuisance.md'
EXPECTED_SHA = 'a1e4419a674d254d3bf5f243d2891bafcd17986611eff94b31f6e35b8e5b9b3a'
REL_QJSON = 'quran-text/quran-no-tashkeel.json'
REL_CHRONO = 'data/revelation-order.csv'

SEED, SEED_REP, N_PERM = 20260509, 20260519, 10000
MW7_CAP = 0.05

MUQ = frozenset({2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31,
                 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68})

RUNSTAMP = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
REL_RUNDIR = os.path.join('findings/phase-b-hypotheses/runs/h-new-2760',
                          RUNSTAMP + '-posthoc')
RUNDIR = os.path.join(PROJECT, REL_RUNDIR)


def sha256_file(rel):
    h = hashlib.sha256()
    with open(os.path.join(PROJECT, rel), 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''):
            h.update(c)
    return h.hexdigest()


actual = sha256_file(REL_PREREG)
if actual != EXPECTED_SHA:
    raise SystemExit(f'PRE-REG SHA MISMATCH\n  expected {EXPECTED_SHA}\n  actual   {actual}')
print(f'pre-reg SHA-256 verified: {EXPECTED_SHA}', file=sys.stderr)

AR_DIAC = re.compile('[ؐ-ًؚ-ٰٟۖ-ۭـ]')
NON_AR = re.compile('[^ء-ي\\s]')
NARROW = [re.compile(r'كتب|كتاب|الكتاب|الكتب|كتابك|كتابه|كتابي|كتابنا|كتبنا|كتبه|كتابا'),
          re.compile(r'قرآن|القرآن|قرءان|القرءان|قرآنا|قرانا|اقرأ')]


def hits_target(t):
    return any(p.search(t) for p in NARROW)


quran = json.load(open(os.path.join(PROJECT, REL_QJSON), encoding='utf-8'))
NV = {s['id']: len(s['verses']) for s in quran}
VTEXT = {(s['id'], i + 1): v['text'] for s in quran for i, v in enumerate(s['verses'])}
SIDS = list(range(1, 115))
HIT = {s: hits_target(' '.join(VTEXT[(s, j)] for j in range(1, min(3, NV[s]) + 1)))
       for s in SIDS}
OW = {s: sum(len(VTEXT[(s, j)].split()) for j in range(1, min(3, NV[s]) + 1)) for s in SIDS}
SW = {s: sum(len(VTEXT[(s, j)].split()) for j in range(1, NV[s] + 1)) for s in SIDS}

PHASE = {}
with open(os.path.join(PROJECT, REL_CHRONO), encoding='utf-8') as f:
    hdr = f.readline().rstrip('\n').split(',')
    im, ip = hdr.index('mushaf_order'), hdr.index('noldeke_phase')
    for line in f:
        p = line.rstrip('\n').split(',')
        if len(p) > max(im, ip):
            PHASE[int(p[im])] = p[ip].strip()


def quantile(v, q):
    p = q * (len(v) - 1)
    lo, hi = int(p), min(int(p) + 1, len(v) - 1)
    return v[lo] + (v[hi] - v[lo]) * (p - lo)


def bin_by_quantile(values, sids, nbins):
    order = sorted(sids, key=lambda s: (values[s], s))
    edges = [round(len(order) * i / nbins) for i in range(nbins + 1)]
    lab = {}
    for b in range(nbins):
        for s in order[edges[b]:edges[b + 1]]:
            lab[s] = b
    return lab


def stratified_perm_test(strata, seed, n_perm=N_PERM):
    rng = random.Random(seed)
    members = defaultdict(list)
    for s in SIDS:
        members[strata[s]].append(s)
    nm = {k: sum(1 for s in v if s in MUQ) for k, v in members.items()}
    observed = sum(1 for s in MUQ if HIT[s])
    draws = []
    for _ in range(n_perm):
        draws.append(sum(1 for k, pool in members.items()
                         for s in rng.sample(pool, nm[k]) if HIT[s]))
    draws.sort()
    mean = sum(draws) / len(draws)
    var = sum((d - mean) ** 2 for d in draws) / len(draws)
    return dict(observed=observed, null_mean=mean, null_sd=var ** 0.5,
                p_greater=(sum(1 for d in draws if d >= observed) + 1) / (n_perm + 1),
                rate_ratio=observed / mean if mean else float('inf'),
                z=(observed - mean) / var ** 0.5 if var else float('inf'),
                band95=[quantile(draws, 0.025), quantile(draws, 0.975)])


# ---------------------------------------------------------------- D1 occupancy
OW_TERT = bin_by_quantile(OW, SIDS, 3)
occ = defaultdict(lambda: [0, 0])
for s in SIDS:
    k = f'ow-tertile-{OW_TERT[s]} x {PHASE[s]}'
    occ[k][0] += 1
    occ[k][1] += 1 if s in MUQ else 0
D1 = dict(
    note='Null C stratum occupancy. A stratum that is mostly muqaṭṭaʿāt leaves the '
         'within-stratum permutation almost no freedom, so the null mean is dragged '
         'toward the observed count and the rate ratio shrinks by construction.',
    strata={k: dict(size=v[0], muqattaat=v[1],
                    muq_fraction=round(v[1] / v[0], 4) if v[0] else None)
            for k, v in sorted(occ.items())},
    phase_only={ph: dict(size=sum(1 for s in SIDS if PHASE[s] == ph),
                         muqattaat=sum(1 for s in SIDS if PHASE[s] == ph and s in MUQ))
                for ph in sorted(set(PHASE.values()))},
)
D1['late_meccan_muq_fraction'] = round(
    D1['phase_only']['Late Meccan']['muqattaat'] / D1['phase_only']['Late Meccan']['size'], 4)

# ------------------------------------------------- D2 H5 restricted within phase
def first_pos(sid):
    for j in range(1, NV[sid] + 1):
        if hits_target(VTEXT[(sid, j)]):
            return j / NV[sid]
    return None


POS = {s: first_pos(s) for s in SIDS if first_pos(s) is not None}
TCNT = {s: sum(1 for j in range(1, NV[s] + 1) if hits_target(VTEXT[(s, j)])) for s in POS}


def h5_on(subset, seed, n_perm=N_PERM):
    m = [POS[s] for s in subset if s in MUQ]
    n = [POS[s] for s in subset if s not in MUQ]
    if not m or not n:
        return dict(skipped='empty arm', n_muq=len(m), n_non=len(n))
    obs = sum(m) / len(m) - sum(n) / len(n)
    rng = random.Random(seed)
    draws = []
    for _ in range(n_perm):
        mp, np_ = [], []
        for s in subset:
            picks = rng.sample(range(1, NV[s] + 1), min(TCNT[s], NV[s]))
            (mp if s in MUQ else np_).append(min(picks) / NV[s])
        draws.append(sum(mp) / len(mp) - sum(np_) / len(np_))
    draws.sort()
    return dict(n_muq=len(m), n_non=len(n),
                mean_muq=sum(m) / len(m), mean_non=sum(n) / len(n), delta=obs,
                null_mean=sum(draws) / len(draws),
                band95=[quantile(draws, 0.025), quantile(draws, 0.975)],
                p_less=(sum(1 for d in draws if d <= obs) + 1) / (n_perm + 1))


D2 = dict(
    note='H5 restricted within revelation phase. MW-7 capped at alpha=0.05, single '
         'test, NOT confirmatory. Asks whether the front-loading survives when '
         'muqaṭṭaʿāt and non-muqaṭṭaʿāt surahs are compared inside the same phase.',
    all_target_bearing=h5_on([s for s in POS], SEED),
)
for ph in sorted(set(PHASE.values())):
    sub = [s for s in POS if PHASE[s] == ph]
    D2[ph.replace(' ', '_')] = h5_on(sub, SEED)
D2['meccan_late_plus_middle'] = h5_on(
    [s for s in POS if PHASE[s] in ('Late Meccan', 'Middle Meccan')], SEED)
D2['meccan_late_plus_middle_replication'] = h5_on(
    [s for s in POS if PHASE[s] in ('Late Meccan', 'Middle Meccan')], SEED_REP)

# ------------------------------------- D3 the length channel I did not name primary
D3 = dict(
    note='Null B re-stratified on WHOLE-SURAH length, the stronger of the two length '
         'channels (rho 0.458 vs the registered 0.168). MW-7 capped, NOT confirmatory: '
         'the registered primary is the opening-window stratification and it stands as '
         'run. This asks what the effect looks like against the nuisance I ranked second.',
    surah_length_quintiles=stratified_perm_test(bin_by_quantile(SW, SIDS, 5), SEED),
    surah_length_quintiles_replication=stratified_perm_test(bin_by_quantile(SW, SIDS, 5), SEED_REP),
    both_length_channels=stratified_perm_test(
        {s: (bin_by_quantile(OW, SIDS, 3)[s], bin_by_quantile(SW, SIDS, 3)[s]) for s in SIDS},
        SEED),
    surah_length_x_phase=stratified_perm_test(
        {s: (bin_by_quantile(SW, SIDS, 3)[s], PHASE[s]) for s in SIDS}, SEED),
)

OUT = dict(id='H-NEW-2760-POSTHOC', mw7_cap=MW7_CAP,
           status='POST-HOC DIAGNOSTIC — MW-7 capped, NOT part of the registered family, '
                  'NOT confirmatory, may not be cited as evidence for or against the '
                  'registered verdict without a fresh pre-registration',
           prereg_sha256=EXPECTED_SHA, seed=SEED, seed_replication=SEED_REP,
           n_perm=N_PERM, D1=D1, D2=D2, D3=D3)

os.makedirs(RUNDIR, exist_ok=False)
with open(os.path.join(RUNDIR, 'result.json'), 'w', encoding='utf-8') as f:
    json.dump(OUT, f, ensure_ascii=False, indent=2, sort_keys=True)
with open(os.path.join(RUNDIR, 'manifest.json'), 'w', encoding='utf-8') as f:
    json.dump(dict(id='H-NEW-2760-POSTHOC', utc=RUNSTAMP,
                   command='python3 findings/phase-b-hypotheses/scripts/h-new-2760-posthoc.py',
                   prereg=dict(path=REL_PREREG, sha256=EXPECTED_SHA),
                   script=dict(path='findings/phase-b-hypotheses/scripts/h-new-2760-posthoc.py',
                               sha256=sha256_file('findings/phase-b-hypotheses/scripts/h-new-2760-posthoc.py')),
                   frozen_inputs=[dict(path=REL_QJSON, sha256=sha256_file(REL_QJSON)),
                                  dict(path=REL_CHRONO, sha256=sha256_file(REL_CHRONO))],
                   run_dir=REL_RUNDIR, mw7_capped=True),
              f, ensure_ascii=False, indent=2, sort_keys=True)

print(f'run dir: {REL_RUNDIR}', file=sys.stderr)
print(json.dumps(OUT, ensure_ascii=False, indent=2, sort_keys=True))
