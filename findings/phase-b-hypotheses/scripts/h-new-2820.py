#!/usr/bin/env python3
"""H-NEW-2820 — the two highest-citation flagged claims are GROUP comparisons.

Tests H-NEW-126 Cell A and H-NEW-570 PRIMARY against compositionally matched nulls.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2820-group-claims.md
Pre-reg SHA-256 embedded below and verified at runtime (SystemExit on mismatch).

Write-once discipline (UNIT-DRIFT-DEFECT.md §7): the run directory is created with
exist_ok=False, every file inside it is opened with mode 'x', and results.json is
written exactly once at completion.  Progress checkpoints go to a directory OUTSIDE
the run directory and are never rewritten.

Deviation from INVESTIGATION-PROTOCOL 7.1, declared in pre-reg §7 by inheritance from
H-NEW-2680/2720: numpy is used for the distance matrices and permutation arithmetic;
all statistical logic is explicit (no scipy).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import re
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from itertools import combinations

import numpy as np

PROJECT = '/Users/grey/Downloads/quran'

PREREG_REL = 'findings/phase-b-hypotheses/prereg-h-new-2820-group-claims.md'
PREREG_SHA = '45abd95012bbf520070685646af909428a183781d94c58c4638353281764b5f1'

FROZEN = {
    'quran-text/quran-no-tashkeel.json':
        '253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a',
    'data/morphology/surah-root-graph.json':
        '8c39642ad8b0581d5962ffad6e3e727698a0e6a0e5a6b6a3ed947b254d6819be',
    'data/revelation-order.csv':
        '74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7',
    'findings/phase-b-hypotheses/csv/h-new-111.json':
        '4c366c414b82b0d0f3bcd06b68a7b5a87b500cf925b5088704a36c355d7f33fc',
    'findings/phase-b-hypotheses/csv/h-new-126.json':
        '699b92b11ab66bd8dd385bbb2c0a44c2f7e39ec7b7aee3525b07dbb85b79f89a',
    'findings/phase-b-hypotheses/csv/h-new-570.json':
        'e157a18dd26b815d4ec34a7caef9bd07b603d42193e43d33b92855fba5c3d83c',
    'scripts/h_new_126_isolate_core.py':
        'e06102b97c5f664f14a02518be58bad0e8dd43683df65eb367f1a5157b9f9664',
    'scripts/h_new_570_muqattaat_content_cluster.py':
        'cdba61aecfe6cb4a985cdd89375d32da30e10ad0848fe163c0684350afd26a9a',
    'findings/phase-b-hypotheses/scripts/h-new-2680.py':
        '57d6b214344ea81433e9f840524e6259953657fbf60e8fd54fdd8d2706b88497',
    'data/baseline-corpora/raw/bukhari-noquran.txt':
        '0169b60de7585a51fc340161488534c4d909370c3dcc8951ca2ae3818c44a100',
    'data/baseline-corpora/raw/jahiz-hayawan.txt':
        '419095484df4e315eba889d38a9c2f6edff55c2f10f481ed9ad024e07bbff0cd',
}

SEED_PRIMARY, SEED_REPLICATION = 20260509, 20260519
N_PERM_QURAN = 10000      # pre-reg §4 A2
N_PERM_BASE = 2000        # pre-reg §4 A3
N_OFFSET = 200            # pre-reg §4 A3 (H-NEW-2720's constant)
K_TOP = 500               # top word types for the surface content instrument
DIR_ALPHA = 0.5
CALIPER_W = 11            # pre-reg §4 A2b

# published constants, read from the two findings (pre-reg §2)
CORE_5 = [16, 21, 22, 23, 25]
SET_MUQ = [2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
           36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68]
SEED_126, SEED_570 = 20260417, 20260520
ALPHA_BON_126 = 0.05 / 4
PCT_BAR_570 = 10.0

RUNSTAMP = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
RUNDIR = os.path.join(PROJECT, 'findings/phase-b-hypotheses/runs/h-new-2820', RUNSTAMP)
PROGRESS = os.path.join(PROJECT, 'findings/phase-b-hypotheses/runs/h-new-2820-progress')


def P(rel):
    return os.path.join(PROJECT, rel)


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''):
            h.update(c)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# 0. LOCKS
# ---------------------------------------------------------------------------
def verify_locks():
    got = sha256_file(P(PREREG_REL))
    if got != PREREG_SHA:
        raise SystemExit('PRE-REG SHA MISMATCH\n  expected %s\n  got      %s'
                         % (PREREG_SHA, got))
    for rel, want in FROZEN.items():
        got = sha256_file(P(rel))
        if got != want:
            raise SystemExit('FROZEN INPUT MISMATCH %s\n  expected %s\n  got      %s'
                             % (rel, want, got))
    log('[lock] pre-reg %s VERIFIED' % PREREG_SHA[:16])
    log('[lock] %d frozen inputs VERIFIED' % len(FROZEN))


# ---------------------------------------------------------------------------
# explicit statistics (no scipy)
# ---------------------------------------------------------------------------
def rankdata(a):
    a = np.asarray(a, dtype=float)
    order = np.argsort(a, kind='mergesort')
    ranks = np.empty(len(a), dtype=float)
    ranks[order] = np.arange(1, len(a) + 1, dtype=float)
    # average ties
    srt = a[order]
    i = 0
    while i < len(a):
        j = i
        while j + 1 < len(a) and srt[j + 1] == srt[i]:
            j += 1
        if j > i:
            ranks[order[i:j + 1]] = (i + j + 2) / 2.0
        i = j + 1
    return ranks


def pearson(x, y):
    x = np.asarray(x, dtype=float)
    y = np.asarray(y, dtype=float)
    xc, yc = x - x.mean(), y - y.mean()
    d = np.sqrt((xc * xc).sum() * (yc * yc).sum())
    return float((xc * yc).sum() / d) if d > 0 else 0.0


def spearman(x, y):
    return pearson(rankdata(x), rankdata(y))


def cohen_d(a, b):
    a, b = np.asarray(a, float), np.asarray(b, float)
    na, nb = len(a), len(b)
    sp2 = ((na - 1) * a.var(ddof=1) + (nb - 1) * b.var(ddof=1)) / (na + nb - 2)
    return float((a.mean() - b.mean()) / np.sqrt(sp2)) if sp2 > 0 else 0.0


def describe(vals, obs):
    v = np.asarray(vals, dtype=float)
    sd = float(v.std(ddof=1))
    return dict(
        observed=float(obs), null_mean=float(v.mean()), null_sd=sd,
        q05=float(np.quantile(v, 0.05)), q50=float(np.quantile(v, 0.50)),
        q95=float(np.quantile(v, 0.95)),
        z=float((obs - v.mean()) / sd) if sd > 0 else 0.0,
        ratio_obs_over_null_mean=float(obs / v.mean()) if v.mean() != 0 else 0.0,
        n_draws=int(len(v)),
    )


def p_upper(vals, obs):
    v = np.asarray(vals, dtype=float)
    return float((1 + int((v >= obs).sum())) / (1 + len(v)))


def pct_le(vals, obs):
    """H-NEW-570's percentile convention: % of null draws at or below the observed."""
    v = np.asarray(vals, dtype=float)
    return float(100.0 * int((v <= obs).sum()) / len(v))


# ---------------------------------------------------------------------------
# set-statistic machinery: mean over unordered pairs of a 114x114 matrix
# ---------------------------------------------------------------------------
def set_stat_matrix(M0, draws, chunk=2000):
    """Mean over unordered pairs of M0 restricted to each draw. M0 diagonal must be 0."""
    n = draws.shape[1]
    out = np.empty(len(draws), dtype=float)
    for a in range(0, len(draws), chunk):
        d = draws[a:a + chunk]
        sub = M0[d[:, :, None], d[:, None, :]]
        out[a:a + len(d)] = sub.sum(axis=(1, 2)) / (n * (n - 1))
    return out


def draw_unmatched(rng, pool, n, ndraws):
    pool = np.asarray(pool)
    idx = np.argsort(rng.random((ndraws, len(pool))), axis=1)[:, :n]
    return pool[idx]


def rank_bins(values, k):
    """Deterministic quantile bins by rank (ties broken by index)."""
    order = np.lexsort((np.arange(len(values)), np.asarray(values, dtype=float)))
    parts = np.array_split(order, k)
    b = np.empty(len(values), dtype=int)
    for i, part in enumerate(parts):
        b[part] = i
    return b


def draw_stratified(rng, bins, group_pos, donor_pos, ndraws):
    """Permute group membership within bins: take exactly the group's occupancy per bin."""
    occ = Counter(int(bins[g]) for g in group_pos)
    cols = []
    for b, need in sorted(occ.items()):
        donors = np.array([d for d in donor_pos if bins[d] == b])
        if len(donors) < need:
            return None, 'bin %d needs %d donors, has %d' % (b, need, len(donors))
        idx = np.argsort(rng.random((ndraws, len(donors))), axis=1)[:, :need]
        cols.append(donors[idx])
    return np.hstack(cols), None


def draw_caliper(rng, values, group_pos, donor_pos, ndraws, w=CALIPER_W):
    """For each group member, draw one donor from its w nearest neighbours by rank."""
    order = np.argsort(np.asarray(values, dtype=float), kind='mergesort')
    rank_of = np.empty(len(values), dtype=int)
    rank_of[order] = np.arange(len(values))
    donor_set = set(int(d) for d in donor_pos)
    windows = []
    for g in group_pos:
        cand = sorted((abs(rank_of[d] - rank_of[g]), int(d))
                      for d in donor_pos if d != g)
        windows.append([c[1] for c in cand[:w]])
    if any(len(win) == 0 for win in windows):
        return None, 'empty caliper window'
    out = np.empty((ndraws, len(group_pos)), dtype=int)
    for i in range(ndraws):
        chosen = []
        for win in windows:
            avail = [c for c in win if c not in chosen and c in donor_set]
            if not avail:
                avail = [c for c in donor_pos if c not in chosen]
            chosen.append(int(rng.choice(np.array(avail))))
        out[i] = chosen
    return out, None


# ---------------------------------------------------------------------------
# 1. CORPUS + channels
# ---------------------------------------------------------------------------
sys.path.insert(0, P('analysis'))
sys.path.insert(0, P('scripts'))
from tools.loader import load_quran            # noqa: E402
from tools.tokenize import real_words          # noqa: E402

QURAN = json.load(open(P('quran-text/quran-no-tashkeel.json'), encoding='utf-8'))
assert len(QURAN) == 114
NV = [len(s['verses']) for s in QURAN]
assert sum(NV) == 6236
STARTS = np.cumsum([0] + NV)[:114]
QVERSE_WLEN = [len(v['text'].split()) for s in QURAN for v in s['verses']]
QVERSE_TEXT = [v['text'] for s in QURAN for v in s['verses']]

# --- partition code lifted verbatim from the frozen H-NEW-2680 source (H-NEW-2720 mechanism)
SRC2680_REL = 'findings/phase-b-hypotheses/scripts/h-new-2680.py'
_SRC2680 = open(P(SRC2680_REL), encoding='utf-8').read()
_EXPECT_FRAGMENT_SHA = {
    'regex': '2cd4d0ca289fd137',
    'normalise_words': '8e49ae080acc6335',
    'build_pseudo_corpus': '6931e0863f09a79c',
}


def _grab_func(name):
    m = re.search(r'^def %s\(.*?(?=\n\ndef |\n\n# ===|\Z)' % name, _SRC2680, re.S | re.M)
    if not m:
        raise SystemExit('could not locate %s() in the frozen 2680 source' % name)
    return m.group(0).rstrip() + '\n'


_frag = {
    'regex': re.search(r"AR_DIAC = .*?\nNON_AR = .*?\n", _SRC2680, re.S).group(0),
    'normalise_words': _grab_func('normalise_words'),
    'build_pseudo_corpus': _grab_func('build_pseudo_corpus'),
}
for _k, _t in _frag.items():
    _got = hashlib.sha256(_t.encode()).hexdigest()[:16]
    if _got != _EXPECT_FRAGMENT_SHA[_k]:
        raise SystemExit('2680 fragment %r changed (sha %s, expected %s)'
                         % (_k, _got, _EXPECT_FRAGMENT_SHA[_k]))
exec(_frag['regex'], globals())
exec(_frag['normalise_words'], globals())
exec(_frag['build_pseudo_corpus'], globals())
log('[lift] 2680 partition code lifted verbatim, 3 fragments SHA-verified')


def partition_at(words, offset=0):
    return build_pseudo_corpus(words[offset:])          # noqa: F821


def group_matched(units):
    return [units[STARTS[i]:STARTS[i] + NV[i]] for i in range(114)]


# ---------------------------------------------------------------------------
# 2. INSTRUMENTS
# ---------------------------------------------------------------------------
def jaccard_matrix(surah_typesets):
    """114x114 Jaccard over per-surah type sets, diagonal zeroed."""
    vocab = sorted(set().union(*surah_typesets)) if surah_typesets else []
    vix = {w: i for i, w in enumerate(vocab)}
    B = np.zeros((114, len(vocab)), dtype=np.float32)
    for i, s in enumerate(surah_typesets):
        for w in s:
            B[i, vix[w]] = 1.0
    inter = (B @ B.T).astype(np.float64)
    sizes = np.array([len(s) for s in surah_typesets], dtype=np.float64)
    union = sizes[:, None] + sizes[None, :] - inter
    with np.errstate(divide='ignore', invalid='ignore'):
        J = np.where(union > 0, inter / union, 0.0)
    np.fill_diagonal(J, 0.0)
    return J


def content_matrix(surahs):
    """Per-surah probability vector over the top-K surface word types (H-NEW-2720)."""
    types = Counter(w for su in surahs for u in su for w in u)
    top = [w for w, _ in types.most_common(K_TOP)]
    tix = {w: i for i, w in enumerate(top)}
    C = np.zeros((114, K_TOP))
    for i, su in enumerate(surahs):
        for u in su:
            for w in u:
                j = tix.get(w)
                if j is not None:
                    C[i, j] += 1.0
    Pm = C + DIR_ALPHA
    Pm /= Pm.sum(axis=1, keepdims=True)
    return Pm


def fisher_rao(Pm):
    S = np.sqrt(Pm)
    D = 2.0 * np.arccos(np.clip(S @ S.T, -1.0, 1.0))
    np.fill_diagonal(D, 0.0)
    return D


# ---------------------------------------------------------------------------
# 3. A0 — reproduction of both published claims, headline + distinguishing outputs
# ---------------------------------------------------------------------------
def a0_reproduce():
    out = {}

    # ---- H-NEW-126, via its own frozen module (main() is never called: it writes JSON)
    import h_new_126_isolate_core as M126
    surahs = load_quran('no-tashkeel')
    root_counts = M126.load_surah_root_counts()
    root_sets = {s: frozenset(root_counts[s].keys()) for s in range(1, 115)}
    noldeke, period = M126.load_noldeke(), M126.load_period()
    triples = M126.compute_rhetorical_triples(surahs)

    a = M126.cell_a(root_sets, random.Random(M126.SEED + 1))
    c = M126.cell_c(triples, random.Random(M126.SEED + 3))
    profiles = M126.compute_profiles(surahs, root_counts, noldeke, period, triples)
    d = M126.cell_d(profiles)

    pub126 = json.load(open(P('findings/phase-b-hypotheses/csv/h-new-126.json'), encoding='utf-8'))
    checks = []

    def chk(name, got, want, tol, kind='stat'):
        ok = abs(got - want) <= tol
        checks.append(dict(claim='H-NEW-126', item=name, published=want,
                           recomputed=got, tol=tol, kind=kind, reproduced=bool(ok)))
        return ok

    chk('cellA.observed', a['observed'], 0.3414, 0.002)
    chk('cellA.null_mean', a['null_mean'], 0.1291, 0.002)
    chk('cellA.p', a['p_one_sided_upper'], 0.0009, 0.002, 'p')
    chk('cellA.mw5.observed', a['mw5_positive_control']['observed'], 0.3062, 0.002)
    chk('cellA.mw5.null_mean', a['mw5_positive_control']['null_mean'], 0.1298, 0.002)
    chk('cellA.mw5.p', a['mw5_positive_control']['p_one_sided_upper'], 0.0046, 0.002, 'p')
    chk('cellC.observed', c['observed'], 5.32, 0.005)
    chk('cellC.null_mean', c['null_mean'], 14.83, 0.005)
    chk('cellC.p', c['p_one_sided_lower'], 0.0157, 0.002, 'p')
    chk('cellC.mw5.observed', c['mw5_positive_control']['observed'], 16.08, 0.005)
    chk('cellC.mw5.null_mean', c['mw5_positive_control']['null_mean'], 14.53, 0.005)
    chk('cellC.mw5.p', c['mw5_positive_control']['p_one_sided_lower'], 0.6732, 0.002, 'p')
    # deterministic: exact identity against the frozen JSON, 12 significant figures
    for i, rec in enumerate(d['per_surah']):
        pub = pub126['cell_d_per_surah_uniqueness']['per_surah'][i]
        same_axis = rec['top_extremity_axis'] == pub['top_extremity_axis']
        checks.append(dict(claim='H-NEW-126',
                           item='cellD.Q%d.axis' % rec['surah'],
                           published=pub['top_extremity_axis'],
                           recomputed=rec['top_extremity_axis'], tol=0,
                           kind='exact', reproduced=bool(same_axis)))
        chk('cellD.Q%d.percentile' % rec['surah'], rec['top_extremity_percentile'],
            pub['top_extremity_percentile'], 1e-9, 'exact')
    for s, nv, mvl, ur in zip(CORE_5, [128, 112, 78, 118, 77],
                              [14.4, 10.5, 16.4, 8.9, 11.6],
                              [358, 284, 328, 271, 250]):
        chk('profile.Q%d.verses' % s, profiles[s]['surah_length'], nv, 0)
        chk('profile.Q%d.mean_verse_len' % s, profiles[s]['mean_verse_length'], mvl, 0.05)
        chk('profile.Q%d.unique_roots' % s, profiles[s]['unique_root_count'], ur, 0)

    out['h_new_126'] = dict(
        cell_a=dict(observed=a['observed'], null_mean=a['null_mean'],
                    p=a['p_one_sided_upper'],
                    mw5=dict(observed=a['mw5_positive_control']['observed'],
                             null_mean=a['mw5_positive_control']['null_mean'],
                             p=a['mw5_positive_control']['p_one_sided_upper'])),
        cell_c=dict(observed=c['observed'], null_mean=c['null_mean'],
                    p=c['p_one_sided_lower'],
                    mw5=dict(observed=c['mw5_positive_control']['observed'],
                             null_mean=c['mw5_positive_control']['null_mean'],
                             p=c['mw5_positive_control']['p_one_sided_lower'])),
        cell_d=[dict(surah=r['surah'], axis=r['top_extremity_axis'],
                     percentile=r['top_extremity_percentile']) for r in d['per_surah']],
    )

    # ---- H-NEW-570, via its own frozen module
    import h_new_570_muqattaat_content_cluster as M570
    D570 = M570.load_D()
    dM = M570.mean_pairwise(D570, M570.SET_MUQ)
    pM = M570.percentile_in_null(D570, dM, 29, M570.N_PERMS, random.Random(M570.SEED))
    dH = M570.mean_pairwise(D570, M570.SET_HM)
    pH = M570.percentile_in_null(D570, dH, 7, M570.N_PERMS, random.Random(M570.SEED + 1))
    dN = M570.mean_pairwise(D570, M570.SET_NONMUQ)
    pN = M570.percentile_in_null(D570, dN, 29, M570.N_PERMS, random.Random(M570.SEED + 2))

    def chk5(name, got, want, tol, kind='stat'):
        ok = abs(got - want) <= tol
        checks.append(dict(claim='H-NEW-570', item=name, published=want,
                           recomputed=got, tol=tol, kind=kind, reproduced=bool(ok)))

    chk5('primary.d', dM, 0.9388131231527093, 1e-12, 'exact')
    chk5('primary.pct', pM, 65.62, 1.0, 'pct')
    chk5('mw5.d', dH, 0.8672422857142857, 1e-12, 'exact')
    chk5('mw5.pct', pH, 20.90, 1.0, 'pct')
    chk5('mw6.d', dN, 1.0228183201970442, 1e-12, 'exact')
    chk5('mw6.pct', pN, 100.00, 1.0, 'pct')

    out['h_new_570'] = dict(primary=dict(d=dM, pct=pM), mw5_hm7=dict(d=dH, pct=pH),
                            mw6_nonmuq29=dict(d=dN, pct=pN))
    out['checks'] = checks
    out['n_failed'] = int(sum(1 for c in checks if not c['reproduced']))
    out['headline_reproduced'] = dict(
        h_new_126=all(c['reproduced'] for c in checks
                      if c['claim'] == 'H-NEW-126' and c['item'].startswith('cellA.observed')),
        h_new_570=all(c['reproduced'] for c in checks
                      if c['claim'] == 'H-NEW-570' and c['item'] == 'primary.d'),
    )
    return out, root_sets, D570, profiles, noldeke, period


# ---------------------------------------------------------------------------
# 4. channels
# ---------------------------------------------------------------------------
def build_channels(profiles, noldeke, period):
    ch = {}
    ids = list(range(1, 115))
    ch['log_mean_verse_length'] = np.array([np.log(profiles[s]['mean_verse_length']) for s in ids])
    ch['log_verse_count'] = np.array([np.log(profiles[s]['surah_length']) for s in ids])
    ch['log_word_count'] = np.array([np.log(profiles[s]['total_tokens']) for s in ids])
    ch['log_root_set_size'] = np.array([np.log(profiles[s]['unique_root_count']) for s in ids])
    raw = dict(
        mean_verse_length=np.array([profiles[s]['mean_verse_length'] for s in ids]),
        verse_count=np.array([float(profiles[s]['surah_length']) for s in ids]),
        word_count=np.array([float(profiles[s]['total_tokens']) for s in ids]),
        root_set_size=np.array([float(profiles[s]['unique_root_count']) for s in ids]),
        noldeke_rank=np.array([float(noldeke[s]) for s in ids]),
        mushaf_position=np.array([float(s) for s in ids]),
    )
    medinan = np.array([1.0 if period[s].lower().startswith('medin') else 0.0 for s in ids])
    return ch, raw, medinan


def characterise(group_ids, raw, medinan, label):
    gpos = [s - 1 for s in group_ids]
    opos = [s - 1 for s in range(1, 115) if s not in set(group_ids)]
    rows = []
    for name, v in raw.items():
        a, b = v[gpos], v[opos]
        logd = (cohen_d(np.log(a), np.log(b))
                if name in ('mean_verse_length', 'verse_count', 'word_count', 'root_set_size')
                else cohen_d(a, b))
        rows.append(dict(channel=name,
                         group_n=len(a), other_n=len(b),
                         group_mean=float(a.mean()), other_mean=float(b.mean()),
                         group_median=float(np.median(a)), other_median=float(np.median(b)),
                         group_sd=float(a.std(ddof=1)), other_sd=float(b.std(ddof=1)),
                         ratio_of_medians=float(np.median(a) / np.median(b))
                         if np.median(b) != 0 else None,
                         cohen_d=logd))
    rows.append(dict(channel='proportion_medinan', group_n=len(gpos), other_n=len(opos),
                     group_mean=float(medinan[gpos].mean()),
                     other_mean=float(medinan[opos].mean()),
                     group_median=None, other_median=None,
                     group_sd=None, other_sd=None, ratio_of_medians=None,
                     cohen_d=float(medinan[gpos].mean() - medinan[opos].mean())))
    return dict(label=label, group=group_ids, rows=rows)


# ---------------------------------------------------------------------------
# 5. per-claim harness
# ---------------------------------------------------------------------------
def claim_arms(tag, M0, group_ids, donor_ids, published_draws, channels,
               medinan, stat_kind, seed, alpha=None, pct_bar=None,
               do_caliper=False, extra_pools=None):
    """All Quran-side arms for one claim. M0: 114x114, diagonal zeroed."""
    rng = np.random.default_rng(seed)
    gpos = np.array([s - 1 for s in group_ids])
    dpos = [s - 1 for s in donor_ids]
    n = len(gpos)
    obs = float(M0[np.ix_(gpos, gpos)].sum() / (n * (n - 1)))
    res = dict(tag=tag, observed=obs, n_group=n, n_donor_pool=len(dpos), seed=int(seed))

    # ---- published null, regenerated draw-for-draw
    pub_stat = set_stat_matrix(M0, published_draws)
    res['published_null'] = describe(pub_stat, obs)
    res['published_null']['p_upper'] = p_upper(pub_stat, obs)
    res['published_null']['pct_le'] = pct_le(pub_stat, obs)

    # ---- dominant-channel ranking (pre-reg §3.1): rho(draw statistic, draw mean log channel)
    rank_rows = []
    for name, vals in channels.items():
        drawmean = vals[published_draws].mean(axis=1)
        rank_rows.append(dict(channel=name, rho=spearman(pub_stat, drawmean),
                              abs_rho=abs(spearman(pub_stat, drawmean))))
    rank_rows.sort(key=lambda r: -r['abs_rho'])
    top = rank_rows[0]
    for r in rank_rows[1:]:
        if abs(top['abs_rho'] - r['abs_rho']) < 0.02:
            r['tie_with_top'] = True
    dom = top['channel']
    res['channel_ranking'] = rank_rows
    res['dominant_channel'] = dom
    domvals = channels[dom]

    # ---- A1 conditional exceedance (parameter-free)
    gmean = float(domvals[gpos].mean())
    drawmean = domvals[published_draws].mean(axis=1)
    keep = drawmean >= gmean
    sub = pub_stat[keep]
    a1 = dict(channel=dom, group_mean_log_channel=gmean, n_restricted=int(keep.sum()),
              underpowered=bool(keep.sum() < 200))
    if keep.sum() > 0:
        a1.update(describe(sub, obs))
        a1['p_upper'] = p_upper(sub, obs)
        a1['pct_le'] = pct_le(sub, obs)
    res['A1_conditional_exceedance'] = a1

    # ---- A2 stratified matched nulls
    def score(vals):
        d = describe(vals, obs)
        d['p_upper'] = p_upper(vals, obs)
        d['pct_le'] = pct_le(vals, obs)
        return d

    res['A2'] = {}
    for k in (5, 10):
        bins = rank_bins(domvals, k)
        draws, err = draw_stratified(rng, bins, gpos, dpos, N_PERM_QURAN)
        res['A2']['k%d' % k] = (dict(estimable=False, note=err) if err else
                                dict(estimable=True, k=k, channel=dom,
                                     bin_occupancy=dict(Counter(int(bins[g]) for g in gpos)),
                                     **score(set_stat_matrix(M0, draws))))

    if do_caliper:
        draws, err = draw_caliper(rng, domvals, gpos, dpos, N_PERM_QURAN)
        res['A2b_caliper'] = (dict(estimable=False, note=err) if err else
                              dict(estimable=True, w=CALIPER_W, channel=dom,
                                   **score(set_stat_matrix(M0, draws))))

    # ---- A2c cross-stratified with period
    bins5 = rank_bins(domvals, 5)
    cross = bins5 * 2 + medinan.astype(int)
    draws, err = draw_stratified(rng, cross, gpos, dpos, N_PERM_QURAN)
    res['A2c_cross_period'] = (dict(estimable=False, note=err) if err else
                               dict(estimable=True, channel=dom + ' x period',
                                    **score(set_stat_matrix(M0, draws))))

    # ---- A2d alternate donor pools
    if extra_pools:
        res['A2d_pool_sensitivity'] = {}
        for pname, pool_ids in extra_pools.items():
            ppos = [s - 1 for s in pool_ids]
            bins = rank_bins(domvals, 5)
            draws, err = draw_stratified(rng, bins, gpos, ppos, N_PERM_QURAN)
            res['A2d_pool_sensitivity'][pname] = (
                dict(estimable=False, note=err) if err else
                dict(estimable=True, k=5, channel=dom, n_pool=len(ppos),
                     **score(set_stat_matrix(M0, draws))))

    # ---- bar
    if alpha is not None:
        res['own_bar'] = dict(kind='p_upper', alpha=alpha)
    if pct_bar is not None:
        res['own_bar'] = dict(kind='pct_le', bar=pct_bar)
    return res


# ---------------------------------------------------------------------------
# 6. genre control
# ---------------------------------------------------------------------------
def genre_arm(name, words, channels_base, medinan, seed, n_offset, n_perm, strat_channels,
              fixed_units=None):
    """fixed_units: the Quran's own verses, which are never re-partitioned (H-NEW-2720)."""
    rng = np.random.default_rng(seed)
    if fixed_units is not None:
        offsets = [0]
    else:
        need = sum(QVERSE_WLEN)
        slack = len(words) - need
        if slack < 0:
            return dict(corpus=name,
                        error='insufficient words: have %d need %d' % (len(words), need))
        offsets = [0] if n_offset <= 1 else \
            [0] + sorted(rng.integers(0, slack + 1, size=n_offset - 1).tolist())
    per_offset = []
    t0 = time.time()
    for oi, off in enumerate(offsets):
        if fixed_units is not None:
            units, err = fixed_units, None
        else:
            units, err = partition_at(words, off)
        if err:
            continue
        surahs = group_matched(units)
        typesets = [set(w for u in su for w in u) for su in surahs]
        J = jaccard_matrix(typesets)
        D = fisher_rao(content_matrix(surahs))
        chans = dict(channels_base)
        chans['log_type_set_size'] = np.log(np.array([max(len(t), 1) for t in typesets], float))
        rec = dict(offset=int(off))
        for stat_name, M0, group_ids, donor_ids in (
                ('jaccard_core5', J, CORE_5, [s for s in range(1, 115) if s not in CORE_5]),
                ('fisher_rao_muq29', D, SET_MUQ, list(range(1, 115)))):
            gpos = np.array([s - 1 for s in group_ids])
            dpos = [s - 1 for s in donor_ids]
            nn = len(gpos)
            obs = float(M0[np.ix_(gpos, gpos)].sum() / (nn * (nn - 1)))
            e = dict(observed=obs)
            un = set_stat_matrix(M0, draw_unmatched(rng, dpos, nn, n_perm))
            e['unmatched'] = dict(p_upper=p_upper(un, obs), pct_le=pct_le(un, obs),
                                  null_mean=float(un.mean()),
                                  z=float((obs - un.mean()) / un.std(ddof=1)))
            e['matched'] = {}
            for cname in strat_channels:
                if cname not in chans:
                    continue
                bins = rank_bins(chans[cname], 5)
                dr, er = draw_stratified(rng, bins, gpos, dpos, n_perm)
                if er:
                    e['matched'][cname] = dict(estimable=False, note=er)
                    continue
                mm = set_stat_matrix(M0, dr)
                e['matched'][cname] = dict(estimable=True, p_upper=p_upper(mm, obs),
                                           pct_le=pct_le(mm, obs),
                                           null_mean=float(mm.mean()),
                                           z=float((obs - mm.mean()) / mm.std(ddof=1)))
            rec[stat_name] = e
        per_offset.append(rec)
        if (oi + 1) % 25 == 0:
            log('  [%s] %d/%d offsets  %.0fs' % (name, oi + 1, len(offsets), time.time() - t0))
            snap = os.path.join(PROGRESS, 'genre-%s-seed%d-%04d.json' % (name, seed, oi + 1))
            if not os.path.exists(snap):
                with open(snap, 'x', encoding='utf-8') as f:
                    json.dump(dict(corpus=name, done=oi + 1, elapsed=time.time() - t0), f)
    return dict(corpus=name, n_offsets=len(per_offset), per_offset=per_offset)


def summarise_genre(per_offset, stat_name, key_path):
    vals = []
    for r in per_offset:
        node = r[stat_name]
        for k in key_path:
            if node is None:
                break
            node = node.get(k) if isinstance(node, dict) else None
        if isinstance(node, (int, float)):
            vals.append(float(node))
    if not vals:
        return None
    v = np.array(vals)
    return dict(n=len(v), min=float(v.min()), median=float(np.median(v)),
                max=float(v.max()), mean=float(v.mean()), values=[float(x) for x in v])


def frac_at_least_as_extreme(node, ref, lower_is_extreme=True):
    """Fraction of baseline offsets at least as extreme as a reference value."""
    if node is None or ref is None:
        return None
    v = np.array(node['values'])
    return float((v <= ref).mean()) if lower_is_extreme else float((v >= ref).mean())


# ---------------------------------------------------------------------------
# 7. verdicts — diffed clause-by-clause against pre-reg §6
# ---------------------------------------------------------------------------
def verdict_126(arms, genre_med_p):
    """Pre-reg §6.1. Own bar p < 0.0125."""
    a = ALPHA_BON_126
    p_k5 = arms['A2']['k5'].get('p_upper')
    p_k10 = arms['A2']['k10'].get('p_upper')
    p_cal = arms.get('A2b_caliper', {}).get('p_upper')
    p_a1 = arms['A1_conditional_exceedance'].get('p_upper')
    if p_k5 is None or p_k5 >= a:
        return 'DOES-NOT-SURVIVE', dict(p_A2_k5=p_k5, bar=a)
    clears_all = all(x is not None and x < a for x in (p_k5, p_k10, p_cal, p_a1))
    base_clear = [k for k, v in genre_med_p.items() if v is not None and v < a]
    if clears_all and not base_clear:
        return 'SURVIVES', dict(p_A2_k5=p_k5, p_A2_k10=p_k10, p_cal=p_cal, p_A1=p_a1)
    if clears_all and base_clear:
        return 'GENRE-SHARED', dict(p_A2_k5=p_k5, baselines_clearing=base_clear)
    return 'DOES-NOT-SURVIVE', dict(p_A2_k5=p_k5, p_A2_k10=p_k10, p_cal=p_cal, p_A1=p_a1,
                                    note='primary clears but a stricter arm does not; '
                                         'pre-reg 6.3 takes the stricter')


def verdict_570(arms):
    """Pre-reg §6.2. Own bar pct <= 10.0 (cluster) / >= 90.0 (over-dispersed)."""
    p5 = arms['A2']['k5'].get('pct_le')
    p10 = arms['A2']['k10'].get('pct_le')
    if p5 is None:
        return 'UNVERIFIABLE', {}
    if p5 <= PCT_BAR_570:
        return 'REVERSES-CLUSTERED', dict(pct_A2_k5=p5, pct_A2_k10=p10, bar=PCT_BAR_570)
    if p5 >= 100.0 - PCT_BAR_570:
        return 'REVERSES-OVERDISPERSED', dict(pct_A2_k5=p5, pct_A2_k10=p10)
    if p10 is not None and (p10 <= PCT_BAR_570 or p10 >= 100.0 - PCT_BAR_570):
        return 'SURVIVES-PRIMARY-ONLY', dict(pct_A2_k5=p5, pct_A2_k10=p10,
                                             note='pre-reg 6.3: the finer bin is the honest one')
    return 'SURVIVES', dict(pct_A2_k5=p5, pct_A2_k10=p10)


# ---------------------------------------------------------------------------
# 8. main
# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n-offsets', type=int, default=N_OFFSET)
    ap.add_argument('--smoke', action='store_true')
    args = ap.parse_args()
    if args.smoke:
        args.n_offsets = 3

    verify_locks()
    os.makedirs(PROGRESS, exist_ok=True)
    rundir = RUNDIR + ('-SMOKE' if args.smoke else '')
    os.makedirs(rundir, exist_ok=False)
    log('[run] %s' % rundir)
    t0 = time.time()

    manifest = dict(finding_id='H-NEW-2820', utc=RUNSTAMP,
                    prereg=dict(path=PREREG_REL, sha256=PREREG_SHA),
                    frozen_inputs=[dict(path=r, sha256=s) for r, s in sorted(FROZEN.items())],
                    seeds=dict(primary=SEED_PRIMARY, replication=SEED_REPLICATION),
                    params=dict(n_perm_quran=N_PERM_QURAN, n_perm_baseline=N_PERM_BASE,
                                n_offsets=args.n_offsets, k_top=K_TOP,
                                dirichlet_alpha=DIR_ALPHA, caliper_w=CALIPER_W))
    with open(os.path.join(rundir, 'manifest.json'), 'x', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)

    # ---- A0
    log('[A0] reproducing both published claims ...')
    a0, root_sets, D570, profiles, noldeke, period = a0_reproduce()
    log('[A0] %d checks, %d failed' % (len(a0['checks']), a0['n_failed']))
    for c in a0['checks']:
        if not c['reproduced']:
            log('     FAIL %s %s: published %s recomputed %s'
                % (c['claim'], c['item'], c['published'], c['recomputed']))

    channels, raw, medinan = build_channels(profiles, noldeke, period)

    # ---- root-instrument matrices, asserted identical to the published routines
    import h_new_126_isolate_core as M126
    import h_new_570_muqattaat_content_cluster as M570
    Jroot = jaccard_matrix([set(root_sets[s]) for s in range(1, 115)])
    Dmat = np.array(M570.load_D())[1:115, 1:115].copy()
    np.fill_diagonal(Dmat, 0.0)
    g = np.array([s - 1 for s in CORE_5])
    lhs = float(Jroot[np.ix_(g, g)].sum() / (5 * 4))
    rhs = M126.pairwise_mean_root_jaccard(CORE_5, root_sets)
    if abs(lhs - rhs) > 1e-12:
        raise SystemExit('HARNESS FAIL: Jaccard matrix != published routine (%r vs %r)' % (lhs, rhs))
    gm = np.array([s - 1 for s in SET_MUQ])
    lhs2 = float(Dmat[np.ix_(gm, gm)].sum() / (29 * 28))
    rhs2 = M570.mean_pairwise(M570.load_D(), SET_MUQ)
    if abs(lhs2 - rhs2) > 1e-12:
        raise SystemExit('HARNESS FAIL: FR matrix != published routine (%r vs %r)' % (lhs2, rhs2))
    log('[harness] both matrix paths bit-identical to the published routines '
        '(%.15f, %.15f)' % (lhs, lhs2))

    # ---- imbalance characterisation
    imb = dict(
        core5=characterise(CORE_5, raw, medinan, 'H-NEW-126 core-5 vs other 109'),
        muq29=characterise(SET_MUQ, raw, medinan, 'H-NEW-570 muqattaat-29 vs non-muqattaat-85'),
    )

    # ---- published null draws, regenerated draw-for-draw with the original RNGs
    r126 = random.Random(SEED_126 + 1)
    noncore = [s for s in range(1, 115) if s not in CORE_5]
    draws126 = np.array([[x - 1 for x in r126.sample(noncore, 5)] for _ in range(10000)])
    r570 = random.Random(SEED_570)
    allids = list(range(1, 115))
    draws570 = np.array([[x - 1 for x in r570.sample(allids, 29)] for _ in range(10000)])

    results = dict(finding_id='H-NEW-2820', utc=RUNSTAMP, rundir=os.path.relpath(rundir, PROJECT),
                   A0=a0, imbalance=imb, claims={}, genre={}, verdicts={})

    for seed_label, seed in (('primary', SEED_PRIMARY), ('replication', SEED_REPLICATION)):
        log('[A1/A2] claim arms, seed %d ...' % seed)
        results['claims'].setdefault(seed_label, {})
        results['claims'][seed_label]['h_new_126'] = claim_arms(
            'H-NEW-126 Cell A', Jroot, CORE_5, noncore, draws126, channels, medinan,
            'jaccard', seed, alpha=ALPHA_BON_126, do_caliper=True)
        results['claims'][seed_label]['h_new_570'] = claim_arms(
            'H-NEW-570 PRIMARY', Dmat, SET_MUQ, allids, draws570, channels, medinan,
            'fisher_rao', seed, pct_bar=PCT_BAR_570, do_caliper=False,
            extra_pools=dict(non_muqattaat_85=[s for s in range(1, 115) if s not in SET_MUQ]))

    # MW-5 (hawamim-7) is a registered distinguishing output; same matching, own published RNG
    r570h = random.Random(SEED_570 + 1)
    draws570h = np.array([[x - 1 for x in r570h.sample(allids, 7)] for _ in range(10000)])
    for seed_label, seed in (('primary', SEED_PRIMARY), ('replication', SEED_REPLICATION)):
        results['claims'][seed_label]['h_new_570_mw5_hm7'] = claim_arms(
            'H-NEW-570 MW-5 hawamim-7', Dmat, [40, 41, 42, 43, 44, 45, 46], allids,
            draws570h, channels, medinan, 'fisher_rao', seed, pct_bar=PCT_BAR_570)

    with open(os.path.join(PROGRESS, 'claims-%s.json' % RUNSTAMP), 'x', encoding='utf-8') as f:
        json.dump(results['claims'], f, indent=2)

    # ---- genre control
    dom126 = results['claims']['primary']['h_new_126']['dominant_channel']
    dom570 = results['claims']['primary']['h_new_570']['dominant_channel']
    strat = []
    for c in (dom126, dom570, 'log_word_count'):
        m = 'log_type_set_size' if c == 'log_root_set_size' else c
        if m not in strat:
            strat.append(m)
    log('[A3] genre stratifiers: %s' % strat)

    quran_units = [normalise_words(t) for t in QVERSE_TEXT]      # noqa: F821
    corpora = [('quran_surface', None, quran_units),
               ('bukhari', normalise_words(open(P('data/baseline-corpora/raw/bukhari-noquran.txt'),
                                                encoding='utf-8').read()), None),   # noqa: F821
               ('jahiz', normalise_words(open(P('data/baseline-corpora/raw/jahiz-hayawan.txt'),
                                              encoding='utf-8').read()), None)]     # noqa: F821
    for cname, words, fixed in corpora:
        nof = 1 if fixed is not None else args.n_offsets
        log('[A3] %s: %s, %d offsets'
            % (cname, ('%d own verses' % len(fixed)) if fixed is not None
               else '%d words' % len(words), nof))
        results['genre'][cname] = genre_arm(cname, words, channels, medinan,
                                            SEED_PRIMARY, nof, N_PERM_BASE, strat,
                                            fixed_units=fixed)

    # ---- genre summaries
    gsum = {}
    for cname, node in results['genre'].items():
        if 'per_offset' not in node:
            gsum[cname] = dict(error=node.get('error'))
            continue
        po = node['per_offset']
        gsum[cname] = dict(
            n_offsets=len(po),
            jaccard_core5=dict(
                observed=summarise_genre(po, 'jaccard_core5', ['observed']),
                unmatched_p=summarise_genre(po, 'jaccard_core5', ['unmatched', 'p_upper']),
                unmatched_z=summarise_genre(po, 'jaccard_core5', ['unmatched', 'z']),
                matched={c: dict(p=summarise_genre(po, 'jaccard_core5', ['matched', c, 'p_upper']),
                                 z=summarise_genre(po, 'jaccard_core5', ['matched', c, 'z']))
                         for c in strat}),
            fisher_rao_muq29=dict(
                observed=summarise_genre(po, 'fisher_rao_muq29', ['observed']),
                unmatched_pct=summarise_genre(po, 'fisher_rao_muq29', ['unmatched', 'pct_le']),
                unmatched_z=summarise_genre(po, 'fisher_rao_muq29', ['unmatched', 'z']),
                matched={c: dict(pct=summarise_genre(po, 'fisher_rao_muq29',
                                                     ['matched', c, 'pct_le']),
                                 z=summarise_genre(po, 'fisher_rao_muq29', ['matched', c, 'z']))
                         for c in strat}),
        )
    results['genre_summary'] = gsum

    # ---- fraction-of-offsets diagnostics (pre-reg §4 A3): how often does an arbitrary
    #      partition of a baseline reach the claim's own bar, and how often does it reach
    #      the Quran's own surface-word value in the same instrument?
    qs = gsum.get('quran_surface', {})
    frac = {}
    for cname in ('bukhari', 'jahiz'):
        node = gsum.get(cname, {})
        if 'jaccard_core5' not in node:
            continue
        e = {}
        j = node['jaccard_core5']
        qj = qs.get('jaccard_core5') if 'jaccard_core5' in qs else None
        e['jaccard_core5'] = dict(
            frac_unmatched_p_below_own_bar=frac_at_least_as_extreme(
                j['unmatched_p'], ALPHA_BON_126),
            frac_unmatched_p_below_quran=frac_at_least_as_extreme(
                j['unmatched_p'], qj['unmatched_p']['median'] if qj else None),
            matched={c: dict(
                frac_p_below_own_bar=frac_at_least_as_extreme(
                    j['matched'][c]['p'], ALPHA_BON_126),
                frac_p_below_quran=frac_at_least_as_extreme(
                    j['matched'][c]['p'],
                    qj['matched'][c]['p']['median'] if qj and qj['matched'].get(c)
                    and qj['matched'][c]['p'] else None),
                quran_surface_p=(qj['matched'][c]['p']['median']
                                 if qj and qj['matched'].get(c) and qj['matched'][c]['p']
                                 else None),
            ) for c in strat if c in j['matched']})
        f = node['fisher_rao_muq29']
        qf = qs.get('fisher_rao_muq29') if 'fisher_rao_muq29' in qs else None
        e['fisher_rao_muq29'] = dict(
            frac_unmatched_pct_below_own_bar=frac_at_least_as_extreme(
                f['unmatched_pct'], PCT_BAR_570),
            matched={c: dict(
                frac_pct_below_own_bar=frac_at_least_as_extreme(
                    f['matched'][c]['pct'], PCT_BAR_570),
                frac_pct_below_quran_root=frac_at_least_as_extreme(
                    f['matched'][c]['pct'],
                    results['claims']['primary']['h_new_570']['A2']['k5']['pct_le']),
                frac_pct_below_quran_surface=frac_at_least_as_extreme(
                    f['matched'][c]['pct'],
                    qf['matched'][c]['pct']['median'] if qf and qf['matched'].get(c)
                    and qf['matched'][c]['pct'] else None),
                quran_surface_pct=(qf['matched'][c]['pct']['median']
                                   if qf and qf['matched'].get(c) and qf['matched'][c]['pct']
                                   else None),
            ) for c in strat if c in f['matched']})
        frac[cname] = e
    results['genre_offset_fractions'] = frac

    # ---- verdicts
    for seed_label in ('primary', 'replication'):
        gm = {}
        for cname in ('bukhari', 'jahiz'):
            s = gsum.get(cname, {}).get('jaccard_core5')
            if not s:
                gm[cname] = None
                continue
            best = None
            for c in strat:
                node = s['matched'].get(c, {}).get('p')
                if node and (best is None or node['median'] < best):
                    best = node['median']
            gm[cname] = best
        v126, det126 = verdict_126(results['claims'][seed_label]['h_new_126'], gm)
        v570, det570 = verdict_570(results['claims'][seed_label]['h_new_570'])
        results['verdicts'][seed_label] = dict(
            h_new_126=dict(verdict=v126, detail=det126,
                           reproduction_partial=bool(any(
                               not c['reproduced'] for c in a0['checks']
                               if c['claim'] == 'H-NEW-126'))),
            h_new_570=dict(verdict=v570, detail=det570,
                           reproduction_partial=bool(any(
                               not c['reproduced'] for c in a0['checks']
                               if c['claim'] == 'H-NEW-570'))),
            genre_baseline_median_p_126=gm)

    results['elapsed_seconds'] = round(time.time() - t0, 1)
    with open(os.path.join(rundir, 'results.json'), 'x', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False, default=float)
    log('[done] %.0fs  ->  %s/results.json' % (results['elapsed_seconds'], rundir))

    # ---- console report
    print('\n=== A0 reproduction: %d checks, %d failed ===' % (len(a0['checks']), a0['n_failed']))
    print('\n=== dominant channels ===')
    for k in ('h_new_126', 'h_new_570'):
        a = results['claims']['primary'][k]
        print(' %-12s %s' % (k, a['dominant_channel']))
        for r in a['channel_ranking']:
            print('    %-24s rho=%+.4f' % (r['channel'], r['rho']))
    print('\n=== verdicts ===')
    for sl in ('primary', 'replication'):
        for k in ('h_new_126', 'h_new_570'):
            v = results['verdicts'][sl][k]
            print(' %-11s %-12s %s  %s' % (sl, k, v['verdict'], v['detail']))


if __name__ == '__main__':
    main()
