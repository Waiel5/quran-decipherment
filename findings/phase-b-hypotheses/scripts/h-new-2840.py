#!/usr/bin/env python3
"""H-NEW-2840 — what IS the muqaṭṭaʿāt clustering?

Characterises the content-space structure H-NEW-2820 uncovered under a size-matched
null: sub-cluster structure, per-letter-class distance, distinguishing vocabulary,
singleton placement.  Every comparison uses a null that holds the set size fixed, and
the PRIMARY null additionally holds Meccan/Medinan period fixed.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2840-muqattaat-structure.md
Pre-reg SHA-256 embedded below and verified at runtime (SystemExit on mismatch).

Write-once discipline (UNIT-DRIFT-DEFECT.md §7): the run directory is created with
exist_ok=False, every file inside it is opened with mode 'x', and results.json is
written exactly once at completion.  Progress checkpoints go OUTSIDE the run directory
and are never rewritten.

Deviation from INVESTIGATION-PROTOCOL 7.1, declared in pre-reg §1 by inheritance from
H-NEW-2680/2720/2820: numpy is used for the distance matrices and permutation
arithmetic; all statistical logic is explicit (no scipy).
"""
from __future__ import annotations

import argparse
import csv
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

PREREG_REL = 'findings/phase-b-hypotheses/prereg-h-new-2840-muqattaat-structure.md'
PREREG_SHA = '321f7fe90f9f4f956b4ab91cf0e39179553175b895068ad69ac6d3e9c1e11c2a'

FROZEN = {
    'quran-text/quran-no-tashkeel.json':
        '253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a',
    'data/morphology/surah-root-graph.json':
        '8c39642ad8b0581d5962ffad6e3e727698a0e6a0e5a6b6a3ed947b254d6819be',
    'data/revelation-order.csv':
        '74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7',
    'findings/phase-b-hypotheses/csv/h-new-111.json':
        '4c366c414b82b0d0f3bcd06b68a7b5a87b500cf925b5088704a36c355d7f33fc',
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
# hashed at first run and recorded in the manifest (large file, no published SHA to inherit)
QAC_REL = 'data/morphology/quranic-corpus-morphology-0.4.txt'

SEED_PRIMARY, SEED_REPLICATION = 20260509, 20260519
N_PERM_QURAN = 10000          # pre-reg frontmatter
N_PERM_BASE = 2000            # pre-reg §6
N_OFFSET = 200                # pre-reg §6
K_TOP, DIR_ALPHA = 500, 0.5   # h-new-111 locked params
TESTS_IN_FAMILY = 12
ALPHA_BON = 0.05 / TESTS_IN_FAMILY          # 0.00416667
NOVELTY_GATE = ALPHA_BON / 10.0             # 0.000416667
PCT_BAR = 10.0                              # h-new-570's own bar, inherited
ROOT_MIN_COUNT = 20                         # pre-reg §5.1 R8
PRIOR_A0 = 1000.0                           # pre-reg §5.1 R8
BH_Q = 0.05

SET_MUQ = [2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
           36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68]
SEED_570 = 20260520

# pre-reg §4.1 — exact opening string, PRIMARY
P1 = {
    'ALM':     [2, 3, 29, 30, 31, 32],
    'ALMS':    [7],
    'ALR':     [10, 11, 12, 14, 15],
    'ALMR':    [13],
    'KHYAS':   [19],
    'TH':      [20],
    'TSM':     [26, 28],
    'TS':      [27],
    'YS':      [36],
    'SAD':     [38],
    'HM':      [40, 41, 43, 44, 45, 46],
    'HM-ASQ':  [42],
    'QAF':     [50],
    'NUN':     [68],
}
# pre-reg §4.2 — classical block naming, SECONDARY
P2 = {
    'ALM':      [2, 3, 29, 30, 31, 32],
    'ALR':      [10, 11, 12, 14, 15],
    'TAWASIN':  [26, 27, 28],
    'HAWAMIM':  [40, 41, 42, 43, 44, 45, 46],
    'S-ALMS':   [7], 'S-ALMR': [13], 'S-KHYAS': [19], 'S-TH': [20],
    'S-YS':     [36], 'S-SAD': [38], 'S-QAF': [50], 'S-NUN': [68],
}
P1_MULTI = ['ALM', 'ALR', 'TSM', 'HM']            # pre-reg §5, R4..R7 in this order
P1_ONEOFF = [19, 20, 36, 38, 50, 68]              # pre-reg §5.1 R9

ABLATE_NARROW = ['ktb', 'qrA']
ABLATE_WIDE = ['ktb', 'qrA', 'tlw', 'nzl', 'Ayy', '*kr', 'wHy', 'frq']

# Arabic glosses for the roots that surface in the vocabulary screen are attached at
# report time from data/morphology/root-stats.csv where available; the runner emits the
# raw Buckwalter root plus its Arabic form so nothing depends on a gloss table.
BW2AR = {'A': 'ا', 'b': 'ب', 't': 'ت', 'v': 'ث', 'j': 'ج', 'H': 'ح', 'x': 'خ',
         'd': 'د', '*': 'ذ', 'r': 'ر', 'z': 'ز', 's': 'س', '$': 'ش', 'S': 'ص',
         'D': 'ض', 'T': 'ط', 'Z': 'ظ', 'E': 'ع', 'g': 'غ', 'f': 'ف', 'q': 'ق',
         'k': 'ك', 'l': 'ل', 'm': 'م', 'n': 'ن', 'h': 'ه', 'w': 'و', 'y': 'ي',
         "'": 'ء', '>': 'أ', '<': 'إ', '&': 'ؤ', '}': 'ئ', '|': 'آ', 'Y': 'ى',
         'p': 'ة'}

RUNSTAMP = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
RUNDIR = os.path.join(PROJECT, 'findings/phase-b-hypotheses/runs/h-new-2840', RUNSTAMP)
PROGRESS = os.path.join(PROJECT, 'findings/phase-b-hypotheses/runs/h-new-2840-progress')


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


def bw2ar(root):
    return ''.join(BW2AR.get(c, c) for c in root)


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
    x = np.asarray(x, float); y = np.asarray(y, float)
    xc, yc = x - x.mean(), y - y.mean()
    d = np.sqrt((xc * xc).sum() * (yc * yc).sum())
    return float((xc * yc).sum() / d) if d > 0 else 0.0


def spearman(x, y):
    return pearson(rankdata(x), rankdata(y))


def describe(vals, obs):
    v = np.asarray(vals, float)
    sd = float(v.std(ddof=1))
    return dict(observed=float(obs), null_mean=float(v.mean()), null_sd=sd,
                q05=float(np.quantile(v, 0.05)), q50=float(np.quantile(v, 0.50)),
                q95=float(np.quantile(v, 0.95)),
                z=float((obs - v.mean()) / sd) if sd > 0 else 0.0,
                ratio_obs_over_null_mean=float(obs / v.mean()) if v.mean() != 0 else 0.0,
                n_draws=int(len(v)))


def p_lower(vals, obs):
    """One-sided: how often is a null draw at or BELOW the observation."""
    v = np.asarray(vals, float)
    return float((1 + int((v <= obs).sum())) / (1 + len(v)))


def p_upper(vals, obs):
    v = np.asarray(vals, float)
    return float((1 + int((v >= obs).sum())) / (1 + len(v)))


def p_two(vals, obs):
    return float(min(1.0, 2.0 * min(p_lower(vals, obs), p_upper(vals, obs))))


def pct_le(vals, obs):
    """h-new-570's percentile convention: % of null draws at or below the observed."""
    v = np.asarray(vals, float)
    return float(100.0 * int((v <= obs).sum()) / len(v))


def bh_reject(pvals, q=BH_Q):
    """Benjamini-Hochberg; returns a boolean mask."""
    p = np.asarray(pvals, float)
    m = len(p)
    order = np.argsort(p, kind='mergesort')
    thresh = q * (np.arange(1, m + 1) / m)
    passed = p[order] <= thresh
    k = int(np.max(np.nonzero(passed)[0]) + 1) if passed.any() else 0
    mask = np.zeros(m, bool)
    if k:
        mask[order[:k]] = True
    return mask


# ---------------------------------------------------------------------------
# draw machinery (same construction as H-NEW-2820)
# ---------------------------------------------------------------------------
def rank_bins(values, k):
    order = np.lexsort((np.arange(len(values)), np.asarray(values, float)))
    parts = np.array_split(order, k)
    b = np.empty(len(values), int)
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


def draw_unmatched(rng, pool, n, ndraws):
    pool = np.asarray(pool)
    idx = np.argsort(rng.random((ndraws, len(pool))), axis=1)[:, :n]
    return pool[idx]


def set_stat_matrix(M0, draws, chunk=2000):
    n = draws.shape[1]
    out = np.empty(len(draws), float)
    for a in range(0, len(draws), chunk):
        d = draws[a:a + chunk]
        sub = M0[d[:, :, None], d[:, None, :]]
        out[a:a + len(d)] = sub.sum(axis=(1, 2)) / (n * (n - 1))
    return out


# ---------------------------------------------------------------------------
# clustering — average linkage (UPGMA), pre-reg §5.1
# ---------------------------------------------------------------------------
def upgma(D):
    """Average-linkage agglomeration. Ties broken by the lowest (i, j) index pair.

    Returns (merges, labels_by_k) where labels_by_k[k] is a length-n integer label
    vector for the k-cluster cut.
    """
    n = D.shape[0]
    M = D.astype(float).copy()
    np.fill_diagonal(M, np.inf)
    size = np.ones(n)
    alive = np.ones(n, bool)
    members = {i: [i] for i in range(n)}
    labels_by_k = {n: np.arange(n)}
    merges = []
    for step in range(n - 1):
        flat = np.where(alive[:, None] & alive[None, :], M, np.inf)
        # lowest (i, j) index pair among ties: argmin on a C-ordered flat view does this
        idx = int(np.argmin(flat))
        i, j = divmod(idx, n)
        if i > j:
            i, j = j, i
        h = float(flat[i, j])
        merges.append(dict(step=step + 1, a=i, b=j, height=h,
                           size_a=int(size[i]), size_b=int(size[j])))
        # Lance-Williams for UPGMA
        new = (size[i] * M[i, :] + size[j] * M[j, :]) / (size[i] + size[j])
        M[i, :] = new
        M[:, i] = new
        M[i, i] = np.inf
        alive[j] = False
        size[i] += size[j]
        members[i] = members[i] + members[j]
        k = n - (step + 1)
        lab = np.empty(n, int)
        for c, (root, mem) in enumerate(sorted(
                ((r, m) for r, m in members.items() if alive[r]), key=lambda t: t[0])):
            for m in mem:
                lab[m] = c
        labels_by_k[k] = lab
    return merges, labels_by_k


def silhouette(D, labels):
    """Mean silhouette; s(i) = 0 for singleton clusters (pre-reg §5.1)."""
    n = len(labels)
    uniq = np.unique(labels)
    if len(uniq) < 2:
        return 0.0
    s = np.zeros(n)
    masks = {c: (labels == c) for c in uniq}
    counts = {c: int(masks[c].sum()) for c in uniq}
    for i in range(n):
        ci = labels[i]
        if counts[ci] <= 1:
            s[i] = 0.0
            continue
        own = masks[ci].copy()
        own[i] = False
        a = float(D[i, own].mean())
        b = np.inf
        for c in uniq:
            if c == ci:
                continue
            b = min(b, float(D[i, masks[c]].mean()))
        s[i] = 0.0 if max(a, b) == 0 else (b - a) / max(a, b)
    return float(s.mean())


def s1_stat(D, ks=(2, 3, 4, 5)):
    _, lab = upgma(D)
    vals = {k: silhouette(D, lab[k]) for k in ks}
    best = max(vals, key=lambda k: vals[k])
    return float(vals[best]), int(best), {int(k): float(v) for k, v in vals.items()}, lab


def pooled_within(D, labels):
    tot, npair = 0.0, 0
    for c in np.unique(labels):
        m = np.nonzero(labels == c)[0]
        if len(m) < 2:
            continue
        sub = D[np.ix_(m, m)]
        tot += sub.sum() / 2.0
        npair += len(m) * (len(m) - 1) // 2
    return tot / npair if npair else 0.0


def s2_stat(D):
    n = D.shape[0]
    _, lab = upgma(D)
    w1 = D.sum() / (n * (n - 1))
    w2 = pooled_within(D, lab[2])
    return float(1.0 - w2 / w1) if w1 > 0 else 0.0


# ---------------------------------------------------------------------------
# delta: within-class vs between-class, pre-reg §5.1
# ---------------------------------------------------------------------------
def class_label_vector(order_ids, partition):
    lab = np.empty(len(order_ids), int)
    keys = sorted(partition)
    for ci, k in enumerate(keys):
        for s in partition[k]:
            lab[order_ids.index(s)] = ci
    return lab, keys


def delta_stat(Dsub, lab):
    n = len(lab)
    iu = np.triu_indices(n, 1)
    same = lab[iu[0]] == lab[iu[1]]
    d = Dsub[iu]
    if same.sum() == 0 or (~same).sum() == 0:
        return 0.0, 0.0, 0.0, 0, 0
    w, b = float(d[same].mean()), float(d[~same].mean())
    return w - b, w, b, int(same.sum()), int((~same).sum())


def perm_labels_free(rng, lab, ndraws):
    out = np.empty((ndraws, len(lab)), int)
    for i in range(ndraws):
        out[i] = rng.permutation(lab)
    return out


def perm_labels_within_strata(rng, lab, strata, ndraws):
    """Permute class labels only among members sharing a stratum."""
    out = np.tile(lab, (ndraws, 1))
    for st in np.unique(strata):
        idx = np.nonzero(strata == st)[0]
        if len(idx) < 2:
            continue
        for i in range(ndraws):
            out[i, idx] = lab[rng.permutation(idx)]
    return out


# ---------------------------------------------------------------------------
# corpus + channels
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

# --- partition code lifted verbatim from the frozen H-NEW-2680 source
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
# QAC roots and the Fisher-Rao matrices
# ---------------------------------------------------------------------------
LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')


def load_qac_roots():
    per_surah = defaultdict(list)
    glob = Counter()
    with open(P(QAC_REL), encoding='utf-8') as f:
        for line in f:
            if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
                continue
            parts = line.rstrip('\n').split('\t')
            if len(parts) < 4:
                continue
            m = LOC_RE.match(parts[0])
            if not m:
                continue
            feat = parts[3]
            if 'STEM' not in feat:
                continue
            rm = ROOT_RE.search(feat)
            if not rm:
                continue
            per_surah[int(m.group(1))].append(rm.group(1))
            glob[rm.group(1)] += 1
    assert len(per_surah) == 114
    return per_surah, glob


def fr_from_roots(per_surah, glob, exclude=()):
    """h-new-111's recipe; `exclude` is removed BEFORE the top-K selection (pre-reg §5.1)."""
    ex = set(exclude)
    g2 = Counter({r: c for r, c in glob.items() if r not in ex})
    top = [r for r, _ in g2.most_common(K_TOP)]
    tix = {r: i for i, r in enumerate(top)}
    C = np.zeros((114, len(top)))
    for sid in range(1, 115):
        for r in per_surah[sid]:
            j = tix.get(r)
            if j is not None:
                C[sid - 1, j] += 1.0
    Pm = C + DIR_ALPHA
    Pm /= Pm.sum(axis=1, keepdims=True)
    S = np.sqrt(Pm)
    D = 2.0 * np.arccos(np.clip(S @ S.T, -1.0, 1.0))
    np.fill_diagonal(D, 0.0)
    return D, top


def load_frozen_D():
    d = json.load(open(P('findings/phase-b-hypotheses/csv/h-new-111.json'), encoding='utf-8'))
    M = np.zeros((114, 114))
    for i, j, dist in d['D_matrix_upper_triangular']:
        M[i - 1, j - 1] = dist
        M[j - 1, i - 1] = dist
    np.fill_diagonal(M, 0.0)
    return M


def content_matrix(surahs):
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
    S = np.sqrt(Pm)
    D = 2.0 * np.arccos(np.clip(S @ S.T, -1.0, 1.0))
    np.fill_diagonal(D, 0.0)
    return D


# ---------------------------------------------------------------------------
# vocabulary: Monroe-style weighted log-odds
# ---------------------------------------------------------------------------
def logodds_z(yG, yR, prior):
    """yG, yR: (..., R) count arrays. prior: (R,) informative Dirichlet."""
    a0 = prior.sum()
    nG = yG.sum(axis=-1, keepdims=True)
    nR = yR.sum(axis=-1, keepdims=True)
    tG = yG + prior
    tR = yR + prior
    oG = tG / (nG + a0 - tG)
    oR = tR / (nR + a0 - tR)
    delta = np.log(oG) - np.log(oR)
    var = 1.0 / tG + 1.0 / tR
    return delta / np.sqrt(var)


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--n-offsets', type=int, default=N_OFFSET)
    ap.add_argument('--smoke', action='store_true')
    args = ap.parse_args()
    if args.smoke:
        args.n_offsets = 2

    verify_locks()
    os.makedirs(PROGRESS, exist_ok=True)
    rundir = RUNDIR + ('-SMOKE' if args.smoke else '')
    os.makedirs(rundir, exist_ok=False)
    log('[run] %s' % rundir)
    t0 = time.time()

    qac_sha = sha256_file(P(QAC_REL))
    manifest = dict(
        finding_id='H-NEW-2840', utc=RUNSTAMP,
        prereg=dict(path=PREREG_REL, sha256=PREREG_SHA),
        frozen_inputs=[dict(path=r, sha256=s) for r, s in sorted(FROZEN.items())]
                      + [dict(path=QAC_REL, sha256=qac_sha)],
        seeds=dict(primary=SEED_PRIMARY, replication=SEED_REPLICATION),
        params=dict(n_perm_quran=N_PERM_QURAN, n_perm_baseline=N_PERM_BASE,
                    n_offsets=args.n_offsets, k_top=K_TOP, dirichlet_alpha=DIR_ALPHA,
                    tests_in_family=TESTS_IN_FAMILY, alpha_bonferroni=ALPHA_BON,
                    novelty_gate=NOVELTY_GATE, root_min_count=ROOT_MIN_COUNT,
                    prior_a0=PRIOR_A0, bh_q=BH_Q))
    with open(os.path.join(rundir, 'manifest.json'), 'x', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)

    R = dict(finding_id='H-NEW-2840', utc=RUNSTAMP,
             rundir=os.path.relpath(rundir, PROJECT),
             alpha_bonferroni=ALPHA_BON, novelty_gate=NOVELTY_GATE)

    # ---------------- R0 reproduction ----------------
    log('[R0] reproducing the frozen instrument ...')
    Dfz = load_frozen_D()
    import h_new_570_muqattaat_content_cluster as M570
    gm = np.array([s - 1 for s in SET_MUQ])
    lhs = float(Dfz[np.ix_(gm, gm)].sum() / (29 * 28))
    rhs = M570.mean_pairwise(M570.load_D(), SET_MUQ)
    if abs(lhs - rhs) > 1e-12:
        raise SystemExit('HARNESS FAIL: frozen matrix != published routine (%r vs %r)'
                         % (lhs, rhs))
    log('[harness] frozen matrix bit-identical to the published routine (%.15f)' % lhs)

    import h_new_126_isolate_core as M126
    surahs_obj = load_quran('no-tashkeel')
    root_counts = M126.load_surah_root_counts()
    noldeke, period = M126.load_noldeke(), M126.load_period()
    triples = M126.compute_rhetorical_triples(surahs_obj)
    profiles = M126.compute_profiles(surahs_obj, root_counts, noldeke, period, triples)

    ids = list(range(1, 115))
    wc = np.array([float(profiles[s]['total_tokens']) for s in ids])
    lwc = np.log(wc)
    medinan = np.array([1.0 if period[s].lower().startswith('medin') else 0.0 for s in ids])

    pub570 = json.load(open(P('findings/phase-b-hypotheses/csv/h-new-570.json'),
                            encoding='utf-8'))
    R['R0'] = dict(
        dbar_muq29_frozen=lhs, published=0.9388131231527093,
        matches_published_routine=True,
        published_percentile=pub570['primary']['percentile'],
        n_medinan_in_29=int(medinan[gm].sum()),
        median_wc_29=float(np.median(wc[gm])),
        median_wc_85=float(np.median(wc[[s - 1 for s in ids if s not in SET_MUQ]])))

    # ---------------- nulls ----------------
    bins5 = rank_bins(lwc, 5)
    bins10 = rank_bins(lwc, 10)
    cross = bins5 * 2 + medinan.astype(int)
    NULLS = dict(N_PERIOD=cross, N_SIZE5=bins5, N_SIZE10=bins10)
    R['strata'] = {k: dict(n_strata=int(len(np.unique(v))),
                           group_occupancy={str(b): int(c) for b, c in
                                            sorted(Counter(int(v[g]) for g in gm).items())},
                           pool_occupancy={str(b): int(c) for b, c in
                                           sorted(Counter(int(x) for x in v).items())})
                   for k, v in NULLS.items()}

    allpos = list(range(114))

    def matched_draws(rng, grouppos, nullname, ndraws=N_PERM_QURAN):
        return draw_stratified(rng, NULLS[nullname], grouppos, allpos, ndraws)

    # ---------------- the 29x29 submatrix and the descriptive layer ----------------
    Dsub = Dfz[np.ix_(gm, gm)]
    merges, labk = upgma(Dsub)
    s1_obs, s1_bestk, s1_all, _ = s1_stat(Dsub)
    s2_obs = s2_stat(Dsub)
    R['descriptive'] = dict(
        order=SET_MUQ,
        dendrogram=[dict(step=m['step'],
                         merged_a=[SET_MUQ[i] for i in
                                   np.nonzero(labk[29 - m['step'] + 1] ==
                                              labk[29 - m['step'] + 1][m['a']])[0]],
                         height=m['height']) if False else
                    dict(step=m['step'], height=m['height'],
                         size_a=m['size_a'], size_b=m['size_b'])
                    for m in merges],
        merge_heights=[m['height'] for m in merges],
        cuts={str(k): {str(SET_MUQ[i]): int(labk[k][i]) for i in range(29)}
              for k in (2, 3, 4, 5, 6)},
        silhouette_by_k=s1_all, S1=s1_obs, S1_best_k=s1_bestk, S2=s2_obs)

    # nearest / farthest neighbours
    nn = {}
    for a, s in enumerate(SET_MUQ):
        row = Dsub[a].copy(); row[a] = np.inf
        inn = int(np.argmin(row))
        row2 = Dsub[a].copy(); row2[a] = -np.inf
        ifar = int(np.argmax(row2))
        full = Dfz[s - 1].copy(); full[s - 1] = np.inf
        nn[str(s)] = dict(
            nearest_in_29=SET_MUQ[inn], nearest_in_29_d=float(Dsub[a, inn]),
            farthest_in_29=SET_MUQ[ifar], farthest_in_29_d=float(Dsub[a, ifar]),
            nearest_in_114=int(np.argmin(full)) + 1,
            nearest_in_114_d=float(full.min()),
            centrality=float((Dsub[a].sum()) / 28.0))
    R['descriptive']['neighbours'] = nn

    # ---------------- R1 sub-structure ----------------
    log('[R1] sub-structure ...')
    R['R1'] = {}
    for seed_label, seed in (('primary', SEED_PRIMARY), ('replication', SEED_REPLICATION)):
        R['R1'][seed_label] = {}
        for nullname in ('N_PERIOD', 'N_SIZE5', 'N_SIZE10'):
            rng = np.random.default_rng(seed + 11)
            draws, err = matched_draws(rng, gm, nullname)
            if err:
                R['R1'][seed_label][nullname] = dict(estimable=False, note=err)
                continue
            vals = np.empty(len(draws))
            v2 = np.empty(len(draws))
            for i, d in enumerate(draws):
                sub = Dfz[np.ix_(d, d)]
                vals[i] = s1_stat(sub)[0]
                v2[i] = s2_stat(sub)
                if (i + 1) % 2500 == 0:
                    log('    R1 %s %s %d/%d' % (seed_label, nullname, i + 1, len(draws)))
            e = describe(vals, s1_obs)
            e.update(estimable=True, p_upper=p_upper(vals, s1_obs),
                     pct_le=pct_le(vals, s1_obs),
                     S2=dict(describe(v2, s2_obs), p_upper=p_upper(v2, s2_obs)))
            R['R1'][seed_label][nullname] = e
        snap = os.path.join(PROGRESS, 'R1-%s-%s.json' % (RUNSTAMP, seed_label))
        if not os.path.exists(snap):
            with open(snap, 'x', encoding='utf-8') as f:
                json.dump(R['R1'][seed_label], f, indent=2, default=float)

    # ---------------- R2 / R3 / R12  delta ----------------
    log('[R2/R3/R12] within-class vs between-class ...')
    tert = rank_bins(lwc[gm], 3)          # tertiles computed ON THE 29 (pre-reg §5.1)
    R['delta'] = {}
    for pname, part in (('P1', P1), ('P2', P2)):
        lab, keys = class_label_vector(SET_MUQ, part)
        dobs, wobs, bobs, npw, npb = delta_stat(Dsub, lab)
        node = dict(partition=pname, classes=keys,
                    n_within_pairs=npw, n_between_pairs=npb,
                    W_within=wobs, B_between=bobs, delta=dobs,
                    per_class={k: dict(
                        n=len(v),
                        within=float(Dsub[np.ix_([SET_MUQ.index(x) for x in v],
                                                 [SET_MUQ.index(x) for x in v])].sum()
                                     / (len(v) * (len(v) - 1))) if len(v) > 1 else None,
                        surahs=v) for k, v in part.items()})
        node['seeds'] = {}
        for seed_label, seed in (('primary', SEED_PRIMARY),
                                 ('replication', SEED_REPLICATION)):
            rngf = np.random.default_rng(seed + 22)
            permF1 = perm_labels_free(rngf, lab, N_PERM_QURAN)
            vF1 = np.array([delta_stat(Dsub, permF1[i])[0] for i in range(N_PERM_QURAN)])
            rngs = np.random.default_rng(seed + 33)
            permF2 = perm_labels_within_strata(rngs, lab, tert, N_PERM_QURAN)
            vF2 = np.array([delta_stat(Dsub, permF2[i])[0] for i in range(N_PERM_QURAN)])
            node['seeds'][seed_label] = dict(
                F1=dict(describe(vF1, dobs), p_lower=p_lower(vF1, dobs)),
                F2=dict(describe(vF2, dobs), p_lower=p_lower(vF2, dobs)))
        R['delta'][pname] = node
    R['R2'] = {s: R['delta']['P1']['seeds'][s]['F1'] for s in ('primary', 'replication')}
    R['R3'] = {s: R['delta']['P1']['seeds'][s]['F2'] for s in ('primary', 'replication')}
    R['R12'] = {s: R['delta']['P2']['seeds'][s]['F1'] for s in ('primary', 'replication')}

    # ---------------- R4..R7 per-family + FAM-c adjacency ----------------
    log('[R4-R7] per-family ...')
    R['families'] = {}
    for fam in P1_MULTI:
        mem = P1[fam]
        fpos = np.array([s - 1 for s in mem])
        n = len(mem)
        obs = float(Dfz[np.ix_(fpos, fpos)].sum() / (n * (n - 1)))
        node = dict(family=fam, surahs=mem, n=n, observed=obs,
                    median_word_count=float(np.median(wc[fpos])),
                    n_medinan=int(medinan[fpos].sum()),
                    mushaf_span=[int(min(mem)), int(max(mem))],
                    is_contiguous_run=bool(max(mem) - min(mem) + 1 == n),
                    seeds={})
        for seed_label, seed in (('primary', SEED_PRIMARY),
                                 ('replication', SEED_REPLICATION)):
            e = {}
            for nullname in ('N_PERIOD', 'N_SIZE5'):
                rng = np.random.default_rng(seed + 44)
                draws, err = matched_draws(rng, fpos, nullname)
                if err:
                    e[nullname] = dict(estimable=False, note=err)
                    continue
                vals = set_stat_matrix(Dfz, draws)
                e[nullname] = dict(describe(vals, obs), estimable=True,
                                   p_lower=p_lower(vals, obs), pct_le=pct_le(vals, obs))
            # within-29 null: random n-subsets of the 29 themselves
            rng2 = np.random.default_rng(seed + 55)
            d29 = draw_unmatched(rng2, list(gm), n, N_PERM_QURAN)
            v29 = set_stat_matrix(Dfz, d29)
            e['within_29'] = dict(describe(v29, obs), p_lower=p_lower(v29, obs),
                                  pct_le=pct_le(v29, obs))
            # FAM-c adjacency: random contiguous mushaf runs of the same length
            rng3 = np.random.default_rng(seed + 66)
            starts = rng3.integers(0, 114 - n + 1, size=N_PERM_QURAN)
            runs = starts[:, None] + np.arange(n)[None, :]
            vrun = set_stat_matrix(Dfz, runs)
            e['FAM_c_adjacency'] = dict(describe(vrun, obs), p_lower=p_lower(vrun, obs),
                                        pct_le=pct_le(vrun, obs))
            node['seeds'][seed_label] = e
        R['families'][fam] = node

    # P2 families reported too (descriptive; only P1 carries R4-R7)
    R['families_P2'] = {}
    for fam, mem in P2.items():
        if len(mem) < 2:
            continue
        fpos = np.array([s - 1 for s in mem])
        n = len(mem)
        obs = float(Dfz[np.ix_(fpos, fpos)].sum() / (n * (n - 1)))
        rng = np.random.default_rng(SEED_PRIMARY + 44)
        draws, err = matched_draws(rng, fpos, 'N_PERIOD')
        node = dict(surahs=mem, n=n, observed=obs)
        if not err:
            vals = set_stat_matrix(Dfz, draws)
            node['N_PERIOD'] = dict(describe(vals, obs), p_lower=p_lower(vals, obs),
                                    pct_le=pct_le(vals, obs))
        else:
            node['N_PERIOD'] = dict(estimable=False, note=err)
        rng3 = np.random.default_rng(SEED_PRIMARY + 66)
        starts = rng3.integers(0, 114 - n + 1, size=N_PERM_QURAN)
        vrun = set_stat_matrix(Dfz, starts[:, None] + np.arange(n)[None, :])
        node['FAM_c_adjacency'] = dict(describe(vrun, obs), p_lower=p_lower(vrun, obs))
        R['families_P2'][fam] = node

    # ---------------- R8 distinguishing vocabulary ----------------
    log('[R8] distinguishing vocabulary ...')
    per_surah_roots, glob = load_qac_roots()
    tested = [r for r, c in glob.items() if c >= ROOT_MIN_COUNT]
    tested.sort(key=lambda r: (-glob[r], r))
    ridx = {r: i for i, r in enumerate(tested)}
    CNT = np.zeros((114, len(tested)))
    for sid in range(1, 115):
        for r in per_surah_roots[sid]:
            j = ridx.get(r)
            if j is not None:
                CNT[sid - 1, j] += 1.0
    total = CNT.sum(axis=0)
    prior = PRIOR_A0 * (total / total.sum())
    yG_obs = CNT[gm].sum(axis=0)
    yR_obs = CNT.sum(axis=0) - yG_obs
    z_obs = logodds_z(yG_obs, yR_obs, prior)
    maxabs_obs = float(np.abs(z_obs).max())

    R['R8'] = dict(n_tested_roots=len(tested), root_min_count=ROOT_MIN_COUNT,
                   prior_a0=PRIOR_A0, max_abs_z_observed=maxabs_obs, seeds={})
    voc_null_z = None
    for seed_label, seed in (('primary', SEED_PRIMARY), ('replication', SEED_REPLICATION)):
        rng = np.random.default_rng(seed + 77)
        draws, err = matched_draws(rng, gm, 'N_PERIOD')
        if err:
            R['R8']['seeds'][seed_label] = dict(estimable=False, note=err)
            continue
        maxabs = np.empty(len(draws))
        zn = np.empty((len(draws), len(tested)), dtype=np.float32)
        tot_all = CNT.sum(axis=0)
        for a in range(0, len(draws), 500):
            d = draws[a:a + 500]
            yG = CNT[d].sum(axis=1)
            yR = tot_all[None, :] - yG
            zz = logodds_z(yG, yR, prior[None, :])
            zn[a:a + len(d)] = zz.astype(np.float32)
            maxabs[a:a + len(d)] = np.abs(zz).max(axis=1)
        R['R8']['seeds'][seed_label] = dict(
            describe(maxabs, maxabs_obs), estimable=True,
            p_upper=p_upper(maxabs, maxabs_obs))
        if seed_label == 'primary':
            voc_null_z = zn
    # per-root two-sided empirical p against the matched null, BH q=0.05
    ge = (voc_null_z >= z_obs[None, :].astype(np.float32)).sum(axis=0)
    le = (voc_null_z <= z_obs[None, :].astype(np.float32)).sum(axis=0)
    n_d = voc_null_z.shape[0]
    p_root = np.minimum(1.0, 2.0 * np.minimum((1 + ge) / (1 + n_d), (1 + le) / (1 + n_d)))
    keep = bh_reject(p_root, BH_Q)
    nG_tok = float(yG_obs.sum())
    nR_tok = float(yR_obs.sum())
    rows = []
    for i in np.argsort(-np.abs(z_obs)):
        if not keep[i]:
            continue
        rows.append(dict(root=tested[i], arabic=bw2ar(tested[i]),
                         count_total=int(total[i]),
                         count_29=int(yG_obs[i]), count_85=int(yR_obs[i]),
                         rate_per_10k_29=float(1e4 * yG_obs[i] / nG_tok),
                         rate_per_10k_85=float(1e4 * yR_obs[i] / nR_tok),
                         z=float(z_obs[i]), p_matched=float(p_root[i]),
                         direction='ENRICHED' if z_obs[i] > 0 else 'DEPLETED'))
    R['R8']['bh_screen'] = dict(q=BH_Q, n_surviving=len(rows), rows=rows)

    # ḥawāmīm vs the other 22 muqaṭṭaʿāt — descriptive screen only
    hm7 = [40, 41, 42, 43, 44, 45, 46]
    hpos = np.array([s - 1 for s in hm7])
    opos = np.array([s - 1 for s in SET_MUQ if s not in hm7])
    yH = CNT[hpos].sum(axis=0)
    yO = CNT[opos].sum(axis=0)
    zH = logodds_z(yH, yO, prior)
    ordH = np.argsort(-np.abs(zH))[:40]
    R['R8']['hawamim_vs_other22_descriptive'] = [
        dict(root=tested[i], arabic=bw2ar(tested[i]), z=float(zH[i]),
             count_hm7=int(yH[i]), count_other22=int(yO[i]),
             direction='ENRICHED' if zH[i] > 0 else 'DEPLETED') for i in ordH]

    # ---------------- R9 singleton placement ----------------
    log('[R9] singleton placement ...')
    cent_obs = np.array([Dsub[a].sum() / 28.0 for a in range(29)])
    R['R9'] = dict(per_surah={}, seeds={})
    rng = np.random.default_rng(SEED_PRIMARY + 88)
    pct_matched = np.empty(29)
    pct_matched_excl = np.empty(29)
    others_all = set(int(x) for x in gm)
    for a, s in enumerate(SET_MUQ):
        spos = s - 1
        st = cross[spos]
        others = np.array([int(x) for x in gm if int(x) != spos])
        donors_lit = np.array([d for d in allpos if cross[d] == st])
        donors_exc = np.array([d for d in donors_lit
                               if d == spos or d not in others_all])
        def cent_of(dn):
            pick = dn[rng.integers(0, len(dn), size=N_PERM_QURAN)]
            return Dfz[np.ix_(pick, others)].mean(axis=1)
        vlit = cent_of(donors_lit)
        vexc = cent_of(donors_exc) if len(donors_exc) else vlit
        pct_matched[a] = pct_le(vlit, cent_obs[a])
        pct_matched_excl[a] = pct_le(vexc, cent_obs[a])
        # bridging label: the 3 nearest neighbours inside the 29
        row = Dsub[a].copy(); row[a] = np.inf
        nn3 = [SET_MUQ[i] for i in np.argsort(row)[:3]]
        fams = set()
        for x in nn3:
            for k in P1_MULTI:
                if x in P1[k]:
                    fams.add(k)
        lab = ('INSIDE' if pct_matched[a] <= 25 else
               'OUTSIDE' if pct_matched[a] >= 75 else 'INTERMEDIATE')
        R['R9']['per_surah'][str(s)] = dict(
            centrality=float(cent_obs[a]),
            pctile_matched=float(pct_matched[a]),
            pctile_matched_excl_other28=float(pct_matched_excl[a]),
            label=lab, nn3=nn3, nn3_families=sorted(fams),
            bridge=bool(len(fams) >= 2),
            p1_class=[k for k, v in P1.items() if s in v][0],
            p1_one_off=bool(s in P1_ONEOFF),
            n_donors_literal=int(len(donors_lit)),
            word_count=float(wc[spos]), medinan=bool(medinan[spos]))
    onepos = [SET_MUQ.index(s) for s in P1_ONEOFF]
    mempos = [i for i in range(29) if SET_MUQ[i] not in P1_ONEOFF]
    obs_gap = float(pct_matched[onepos].mean() - pct_matched[mempos].mean())
    rngp = np.random.default_rng(SEED_PRIMARY + 99)
    nullgap = np.empty(N_PERM_QURAN)
    for i in range(N_PERM_QURAN):
        perm = rngp.permutation(29)
        nullgap[i] = pct_matched[perm[:6]].mean() - pct_matched[perm[6:]].mean()
    R['R9']['inference'] = dict(
        mean_pctile_one_off=float(pct_matched[onepos].mean()),
        mean_pctile_class_members=float(pct_matched[mempos].mean()),
        gap=obs_gap, two_sided_p=p_two(nullgap, obs_gap),
        note='two-sided by pre-registration; direction was not locked')

    # ---------------- R10 / R11 ablation ----------------
    log('[R10/R11] Book-root ablation ...')
    Dreb, top_full = fr_from_roots(per_surah_roots, glob)
    R['ablation'] = dict(
        rebuilt_vs_frozen_max_abs_diff=float(np.abs(Dreb - Dfz).max()),
        note='the frozen matrix is published rounded to 6 dp; the ablation contrast is '
             'rebuilt-vs-rebuilt only')
    for tag, ex in (('R10_narrow', ABLATE_NARROW), ('R11_wide', ABLATE_WIDE)):
        Dab, top_ab = fr_from_roots(per_surah_roots, glob, exclude=ex)
        node = dict(excluded=ex, excluded_arabic=[bw2ar(r) for r in ex],
                    excluded_counts={r: int(glob[r]) for r in ex},
                    n_dims=len(top_ab), seeds={})
        for mat_tag, M in (('rebuilt_full', Dreb), ('ablated', Dab)):
            obs = float(M[np.ix_(gm, gm)].sum() / (29 * 28))
            rng = np.random.default_rng(SEED_PRIMARY + 111)
            draws, err = matched_draws(rng, gm, 'N_PERIOD')
            vals = set_stat_matrix(M, draws)
            node[mat_tag] = dict(describe(vals, obs), pct_le=pct_le(vals, obs),
                                 p_lower=p_lower(vals, obs))
            rng = np.random.default_rng(SEED_PRIMARY + 112)
            draws5, _ = matched_draws(rng, gm, 'N_SIZE5')
            v5 = set_stat_matrix(M, draws5)
            node[mat_tag + '_N_SIZE5'] = dict(describe(v5, obs), pct_le=pct_le(v5, obs))
        R['ablation'][tag] = node

    with open(os.path.join(PROGRESS, 'quran-arms-%s.json' % RUNSTAMP), 'x',
              encoding='utf-8') as f:
        json.dump({k: R[k] for k in ('R0', 'R1', 'R2', 'R3', 'R12', 'families',
                                     'R8', 'R9', 'ablation')}, f, indent=2, default=float)
    log('[checkpoint] Quran arms done  %.0fs' % (time.time() - t0))

    # ---------------- genre control ----------------
    log('[genre] matched partitions ...')
    lab_p1, _ = class_label_vector(SET_MUQ, P1)
    quran_units = [normalise_words(t) for t in QVERSE_TEXT]        # noqa: F821
    corpora = [('quran_surface', None, quran_units),
               ('bukhari', normalise_words(open(P('data/baseline-corpora/raw/'
                                                  'bukhari-noquran.txt'),
                                                encoding='utf-8').read()), None),  # noqa: F821
               ('jahiz', normalise_words(open(P('data/baseline-corpora/raw/'
                                                'jahiz-hayawan.txt'),
                                              encoding='utf-8').read()), None)]    # noqa: F821
    R['genre'] = {}
    for cname, words, fixed in corpora:
        rng = np.random.default_rng(SEED_PRIMARY)
        if fixed is not None:
            offsets = [0]
        else:
            need = sum(QVERSE_WLEN)
            slack = len(words) - need
            if slack < 0:
                R['genre'][cname] = dict(
                    error='insufficient words: have %d need %d' % (len(words), need))
                continue
            offsets = [0] + sorted(rng.integers(0, slack + 1,
                                                size=args.n_offsets - 1).tolist())
        log('[genre] %s: %d offsets' % (cname, len(offsets)))
        per_offset = []
        tg = time.time()
        # the strata depend only on the Quran's own profile, so the matched draws are
        # identical across offsets and are generated once
        rngd = np.random.default_rng(SEED_PRIMARY + 123)
        gdraws, gerr = draw_stratified(rngd, cross, gm, allpos, N_PERM_BASE)
        rngl = np.random.default_rng(SEED_PRIMARY + 124)
        glabs = perm_labels_free(rngl, lab_p1, N_PERM_BASE)
        for oi, off in enumerate(offsets):
            units, err = (fixed, None) if fixed is not None else partition_at(words, off)
            if err:
                continue
            Dg = content_matrix(group_matched(units))
            dsub = Dg[np.ix_(gm, gm)]
            obs_d = float(dsub.sum() / (29 * 28))
            obs_delta = delta_stat(dsub, lab_p1)[0]
            obs_s1 = s1_stat(dsub)[0]
            rec = dict(offset=int(off), dbar=obs_d, delta=obs_delta, S1=obs_s1)
            if gerr is None:
                vd = set_stat_matrix(Dg, gdraws)
                rec['dbar_matched_pct'] = pct_le(vd, obs_d)
                vs = np.array([s1_stat(Dg[np.ix_(d, d)])[0] for d in gdraws])
                rec['S1_matched_p_upper'] = p_upper(vs, obs_s1)
                rec['S1_matched_pct'] = pct_le(vs, obs_s1)
            vdel = np.array([delta_stat(dsub, glabs[i])[0] for i in range(N_PERM_BASE)])
            rec['delta_F1_p_lower'] = p_lower(vdel, obs_delta)
            per_offset.append(rec)
            if (oi + 1) % 25 == 0:
                log('  [%s] %d/%d  %.0fs' % (cname, oi + 1, len(offsets), time.time() - tg))
                snap = os.path.join(PROGRESS, 'genre-%s-%s-%04d.json'
                                    % (cname, RUNSTAMP, oi + 1))
                if not os.path.exists(snap):
                    with open(snap, 'x', encoding='utf-8') as f:
                        json.dump(dict(corpus=cname, done=oi + 1,
                                       elapsed=time.time() - tg), f)
        R['genre'][cname] = dict(n_offsets=len(per_offset), per_offset=per_offset)

    def summ(cname, key):
        node = R['genre'].get(cname, {})
        if 'per_offset' not in node:
            return None
        v = np.array([r[key] for r in node['per_offset'] if key in r], float)
        if not len(v):
            return None
        return dict(n=len(v), min=float(v.min()), median=float(np.median(v)),
                    max=float(v.max()), mean=float(v.mean()),
                    values=[float(x) for x in v])

    R['genre_summary'] = {c: {k: summ(c, k) for k in
                              ('dbar', 'delta', 'S1', 'dbar_matched_pct',
                               'S1_matched_p_upper', 'delta_F1_p_lower')}
                          for c in R['genre']}
    qs = R['genre_summary'].get('quran_surface', {})
    frac = {}
    for c in ('bukhari', 'jahiz'):
        n = R['genre_summary'].get(c, {})
        if not n or n.get('delta_F1_p_lower') is None:
            continue
        qd = qs.get('delta_F1_p_lower', {}).get('median') if qs.get('delta_F1_p_lower') else None
        qp = qs.get('dbar_matched_pct', {}).get('median') if qs.get('dbar_matched_pct') else None
        dv = np.array(n['delta_F1_p_lower']['values'])
        pv = (np.array(n['dbar_matched_pct']['values'])
              if n.get('dbar_matched_pct') else None)
        frac[c] = dict(
            frac_delta_p_below_alpha_bon=float((dv <= ALPHA_BON).mean()),
            frac_delta_p_below_quran=float((dv <= qd).mean()) if qd is not None else None,
            quran_surface_delta_p=qd,
            frac_dbar_pct_below_bar=float((pv <= PCT_BAR).mean()) if pv is not None else None,
            frac_dbar_pct_below_quran_root=float(
                (pv <= R['R1']['primary']['N_PERIOD'].get('pct_le', 100)).mean())
            if pv is not None else None,
            quran_surface_dbar_pct=qp)
    R['genre_fractions'] = frac

    # ---------------- verdicts ----------------
    def gate(p):
        return p is not None and p < ALPHA_BON

    verdicts = {}
    for seed_label in ('primary', 'replication'):
        p_r2 = R['R2'][seed_label].get('p_lower')
        p_r3 = R['R3'][seed_label].get('p_lower')
        fam_pass = [f for f in P1_MULTI
                    if gate(R['families'][f]['seeds'][seed_label]
                            .get('N_PERIOD', {}).get('p_lower'))]
        if not gate(p_r2):
            v = 'NO-SUB-STRUCTURE'
        elif gate(p_r3) and fam_pass:
            v = 'SUB-STRUCTURED'
        elif gate(p_r3) and not fam_pass:
            v = 'SUB-STRUCTURE-WEAK'
        else:
            v = 'SUB-STRUCTURE-WEAK'
        mods = []
        r1p = R['R1'][seed_label]
        if (gate(r1p.get('N_SIZE5', {}).get('p_upper'))
                and not gate(r1p.get('N_PERIOD', {}).get('p_upper'))):
            mods.append('-SIZE-EXPLAINED')
        qd = qs.get('delta_F1_p_lower', {}).get('median') if qs.get('delta_F1_p_lower') else None
        for c in ('bukhari', 'jahiz'):
            m = R['genre_summary'].get(c, {}).get('delta_F1_p_lower')
            if m and qd is not None and m['median'] <= qd and '-GENRE-SHARED' not in mods:
                mods.append('-GENRE-SHARED')
        if fam_pass:
            adj_all_fail = all(
                not gate(R['families'][f]['seeds'][seed_label]['FAM_c_adjacency']['p_lower'])
                for f in fam_pass)
            if adj_all_fail:
                mods.append('-ADJACENCY-EXPLAINED')
        verdicts[seed_label] = dict(
            verdict=v + ''.join(mods),
            base=v, modifiers=mods,
            p_R2_F1=p_r2, p_R3_F2=p_r3, families_passing=fam_pass,
            alpha_bonferroni=ALPHA_BON)
    pct_n = R['ablation']['R10_narrow']['ablated']['pct_le']
    pct_w = R['ablation']['R11_wide']['ablated']['pct_le']
    verdicts['independence'] = dict(
        label='PILLAR1-DISTINCT' if (pct_n <= PCT_BAR and pct_w <= PCT_BAR)
              else 'PILLAR1-ENTANGLED',
        pct_narrow=pct_n, pct_wide=pct_w, bar=PCT_BAR,
        binding_statement='Computed on the same 29 surahs in the same corpus as H-NEW-2760. '
                          'Not an independent confirmation of Pillar 1 under any label.')
    verdicts['seed_fragile'] = bool(
        verdicts['primary']['verdict'] != verdicts['replication']['verdict'])
    R['verdicts'] = verdicts

    R['elapsed_seconds'] = round(time.time() - t0, 1)
    with open(os.path.join(rundir, 'results.json'), 'x', encoding='utf-8') as f:
        json.dump(R, f, indent=2, ensure_ascii=False, default=float)
    log('[done] %.0fs -> %s/results.json' % (R['elapsed_seconds'], rundir))

    print('\n=== R0 ===  dbar=%.15f  (published 0.9388131231527093)' % R['R0']['dbar_muq29_frozen'])
    print('\n=== verdicts ===')
    for sl in ('primary', 'replication'):
        print(' %-12s %s' % (sl, verdicts[sl]['verdict']))
        print('              R2 p=%s  R3 p=%s  families=%s'
              % (verdicts[sl]['p_R2_F1'], verdicts[sl]['p_R3_F2'],
                 verdicts[sl]['families_passing']))
    print(' independence %s (narrow %.2f, wide %.2f)'
          % (verdicts['independence']['label'], pct_n, pct_w))


if __name__ == '__main__':
    main()
