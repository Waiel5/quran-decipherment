#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2720 — The genre-control sweep.

Do the remaining standing laws discriminate the Qurʾān from matched Arabic corpora?

Pre-reg : findings/phase-b-hypotheses/prereg-h-new-2720-genre-control-sweep.md
          SHA-256 verified at runtime; mismatch -> exit 1.
Parent  : H-NEW-2680. The partition functions are LIFTED VERBATIM from
          scripts/h-new-2680.py and their source text is SHA-checked, so the
          pseudo-surah construction is byte-identical to the one 2680 used.
Author  : Waiel Al-Shujaa
Seeds   : 20260509 primary / 20260519 replication

Deviation from INVESTIGATION-PROTOCOL 7.1, declared in pre-reg 8.8: numpy is used
for the Fisher-Rao matrices and permutation arithmetic, as in H-NEW-2680.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone

import numpy as np

PROJECT = '/Users/grey/Downloads/quran'
PREREG_REL = 'findings/phase-b-hypotheses/prereg-h-new-2720-genre-control-sweep.md'
PREREG_SHA = '24a5bc8dd2352151f6557a0415cb177f69e60f8fca5f1ccf39ff3c57b2e0040d'

SRC2680_REL = 'findings/phase-b-hypotheses/scripts/h-new-2680.py'

FROZEN = {
    'quran-text/quran-no-tashkeel.json':
        '253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a',
    'quran-text/quran-min-tashkeel.json':
        '87aaab41f78d1b148c8051b8afc1ee5fa66fd6d45f2f7a2984e3f9192c458b36',
    'data/morphology/quranic-corpus-morphology-0.4.txt':
        'a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46',
    'data/baseline-corpora/raw/bukhari-noquran.txt':
        '0169b60de7585a51fc340161488534c4d909370c3dcc8951ca2ae3818c44a100',
    'data/baseline-corpora/raw/jahiz-hayawan.txt':
        '419095484df4e315eba889d38a9c2f6edff55c2f10f481ed9ad024e07bbff0cd',
    SRC2680_REL:
        '57d6b214344ea81433e9f840524e6259953657fbf60e8fd54fdd8d2706b88497',
}

POETRY_FILES = [
    'diwan-amr-ibn-kulthum.txt', 'diwan-antara.txt', 'diwan-harith.txt',
    'diwan-imru-al-qais.txt', 'diwan-labid.txt', 'diwan-tarafa.txt',
    'diwan-zuhayr.txt', 'muallaqa-amr-bin-kulthum.txt', 'muallaqa-antara.txt',
    'muallaqa-harith.txt', 'muallaqa-imru-al-qais.txt', 'muallaqa-labid.txt',
    'muallaqa-tarafa.txt', 'muallaqa-zuhayr.txt',
]
POETRY_SHA = 'f6c5525ddfa8d06ca974cbc937ad1f7f96839418e2eabdd3b94f8fce66fb983a'

SEED, SEED_REP = 20260509, 20260519
N_OFFSET = 200          # offset partitions per resampleable baseline
N_RING_PERM = 1000      # within-unit order permutations per ring window
K_WIN = 15              # window size for the compression-tail laws
K_TOP = 500             # top word-types for the content instrument
DIR_ALPHA = 0.5

# pre-locked material-difference margins (pre-reg 4)
MARGIN_R2 = 0.10
MARGIN_R = 0.20
MARGIN_FRAC = 0.25


def P(rel):
    return os.path.join(PROJECT, rel)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''):
            h.update(c)
    return h.hexdigest()


def log(*a):
    print(*a, file=sys.stderr, flush=True)


# ---------------------------------------------------------------------------
# 0. LOCKS
# ---------------------------------------------------------------------------
def verify_locks():
    got = sha256_file(P(PREREG_REL))
    if got != PREREG_SHA:
        sys.exit('PRE-REG SHA MISMATCH\n  expected %s\n  got      %s' % (PREREG_SHA, got))
    for rel, want in FROZEN.items():
        got = sha256_file(P(rel))
        if got != want:
            sys.exit('FROZEN INPUT MISMATCH %s\n  expected %s\n  got      %s'
                     % (rel, want, got))
    h = hashlib.sha256()
    for f in POETRY_FILES:
        with open(P('data/baseline-corpora/raw/' + f), 'rb') as fh:
            h.update(fh.read())
    if h.hexdigest() != POETRY_SHA:
        sys.exit('POETRY CORPUS SHA MISMATCH: %s' % h.hexdigest())
    log('[lock] pre-reg %s VERIFIED' % PREREG_SHA[:16])
    log('[lock] %d frozen inputs + poetry corpus VERIFIED' % len(FROZEN))


# ---------------------------------------------------------------------------
# 1. PARTITION CODE LIFTED VERBATIM FROM H-NEW-2680 (MW-6)
# ---------------------------------------------------------------------------
# The two function bodies and the regex block are extracted from the frozen
# 2680 source, SHA-checked against the values recorded when this script was
# written, and exec'd.  Nothing is retyped, so the pseudo-surah construction
# cannot drift from the one 2680 used.
_SRC2680 = open(P(SRC2680_REL), encoding='utf-8').read()

_EXPECT_FRAGMENT_SHA = {
    'regex': '2cd4d0ca289fd137',
    'normalise_words': '8e49ae080acc6335',
    'build_pseudo_corpus': '6931e0863f09a79c',
}


def _grab_func(name):
    m = re.search(r'^def %s\(.*?(?=\n\ndef |\n\n# ===|\Z)' % name, _SRC2680, re.S | re.M)
    if not m:
        sys.exit('MW-6 FAIL: could not locate %s() in the frozen 2680 source' % name)
    return m.group(0).rstrip() + '\n'


_regex_block = re.search(r"AR_DIAC = .*?\nNON_AR = .*?\n", _SRC2680, re.S).group(0)
_frag = {'regex': _regex_block,
         'normalise_words': _grab_func('normalise_words'),
         'build_pseudo_corpus': _grab_func('build_pseudo_corpus')}
for _k, _t in _frag.items():
    _got = hashlib.sha256(_t.encode()).hexdigest()[:16]
    if _got != _EXPECT_FRAGMENT_SHA[_k]:
        sys.exit('MW-6 FAIL: 2680 fragment %r changed (sha %s, expected %s)'
                 % (_k, _got, _EXPECT_FRAGMENT_SHA[_k]))
log('[MW-6] 2680 partition code lifted verbatim, 3 fragments SHA-verified')


# ---------------------------------------------------------------------------
# 2. CORPUS
# ---------------------------------------------------------------------------
QURAN = json.load(open(P('quran-text/quran-no-tashkeel.json'), encoding='utf-8'))
QURAN_MIN = json.load(open(P('quran-text/quran-min-tashkeel.json'), encoding='utf-8'))
assert len(QURAN) == 114

NV = [len(s['verses']) for s in QURAN]
assert sum(NV) == 6236, sum(NV)
STARTS = np.cumsum([0] + NV)[:114]

QVERSE_WLEN = [len(v['text'].split()) for s in QURAN for v in s['verses']]
QVERSE_TEXT = [v['text'] for s in QURAN for v in s['verses']]

exec(_frag['regex'], globals())
exec(_frag['normalise_words'], globals())
exec(_frag['build_pseudo_corpus'], globals())

QURAN_UNITS = [normalise_words(t) for t in QVERSE_TEXT]        # noqa: F821


def load_words(rel):
    return normalise_words(open(P(rel), encoding='utf-8').read())   # noqa: F821


def load_poetry():
    txt = ''.join(open(P('data/baseline-corpora/raw/' + f), encoding='utf-8').read()
                  for f in POETRY_FILES)
    return normalise_words(txt)                                     # noqa: F821


def partition_at(words, offset=0):
    """2680's build_pseudo_corpus applied to a stream starting at `offset`."""
    units, err = build_pseudo_corpus(words[offset:])                # noqa: F821
    return units, err


# grouping of 6236 units into 114 pseudo-surahs
def group_matched(units):
    return [units[STARTS[i]:STARTS[i] + NV[i]] for i in range(114)]


UNIFORM_NV = [55] * 62 + [54] * 52          # 62*55 + 52*54 = 3410 + 2808 = 6218
UNIFORM_NV[0] += 6236 - sum(UNIFORM_NV)     # absorb the remainder in unit 0
assert sum(UNIFORM_NV) == 6236 and len(UNIFORM_NV) == 114
UNIFORM_STARTS = np.cumsum([0] + UNIFORM_NV)[:114]


def group_uniform(units):
    return [units[UNIFORM_STARTS[i]:UNIFORM_STARTS[i] + UNIFORM_NV[i]]
            for i in range(114)]


# ---------------------------------------------------------------------------
# 3. INSTRUMENTS (surface-word, identical for every corpus)
# ---------------------------------------------------------------------------
AR_LETTERS = [chr(c) for c in range(0x0621, 0x064B)]
LET_IDX = {c: i for i, c in enumerate(AR_LETTERS)}

# H-NEW-165 / 700 phoneme classes, surface-grapheme approximation
EMPHATIC = set('صضطظ')
PHARYNGEAL = set('حعغخ')
SIBILANT = set('سشزصث')
GLOTTAL = set('ءأإآهـ')


def content_matrix(surahs):
    """Per-surah probability vector over the top-K surface word-types."""
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
    return 2.0 * np.arccos(np.clip(S @ S.T, -1.0, 1.0))


def rhyme_matrix(surahs):
    """Per-surah 28-letter unit-final-letter distribution."""
    R = np.zeros((114, len(AR_LETTERS)))
    for i, su in enumerate(surahs):
        for u in su:
            if not u:
                continue
            ch = u[-1][-1] if u[-1] else ''
            j = LET_IDX.get(ch)
            if j is not None:
                R[i, j] += 1.0
    s = R.sum(axis=1, keepdims=True)
    s[s == 0] = 1.0
    return R / s


def phoneme_matrix(surahs):
    """Per-surah 4-class phoneme proportion vector."""
    Ph = np.zeros((114, 4))
    for i, su in enumerate(surahs):
        n = 0
        for u in su:
            for w in u:
                for ch in w:
                    n += 1
                    if ch in EMPHATIC:
                        Ph[i, 0] += 1
                    if ch in PHARYNGEAL:
                        Ph[i, 1] += 1
                    if ch in SIBILANT:
                        Ph[i, 2] += 1
                    if ch in GLOTTAL:
                        Ph[i, 3] += 1
        if n:
            Ph[i] /= n
    return Ph


def cosine_dist(M):
    nrm = np.linalg.norm(M, axis=1, keepdims=True)
    nrm[nrm == 0] = 1.0
    U = M / nrm
    return 1.0 - np.clip(U @ U.T, -1.0, 1.0)


def window_means(D, k=K_WIN):
    """d̄ for each of the 114-k+1 windows of k consecutive units."""
    out = []
    for s in range(0, 114 - k + 1):
        sub = D[s:s + k, s:s + k]
        iu = np.triu_indices(k, 1)
        out.append(float(sub[iu].mean()))
    return np.array(out)


def fit_kink(y, kink):
    """Two-piece linear fit d̄ = a + b*max(0, s-kink); s is 1-based window start."""
    s = np.arange(1, len(y) + 1, dtype=float)
    x = np.maximum(0.0, s - kink)
    X = np.column_stack([np.ones_like(x), x])
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    pred = X @ beta
    ss_res = float(((y - pred) ** 2).sum())
    ss_tot = float(((y - y.mean()) ** 2).sum())
    r2 = 1.0 - ss_res / ss_tot if ss_tot > 0 else float('nan')
    return dict(alpha=float(beta[0]), beta=float(beta[1]), r2=r2)


def pearson(a, b):
    a = np.asarray(a, float); b = np.asarray(b, float)
    a = a - a.mean(); b = b - b.mean()
    d = math.sqrt(float((a * a).sum()) * float((b * b).sum()))
    return float((a * b).sum() / d) if d else float('nan')


# ---------------------------------------------------------------------------
# 4. THE LAWS
# ---------------------------------------------------------------------------
def laws_G1_G5(surahs):
    """Gradient laws G1-G5 on one 114-unit partition."""
    Pm = content_matrix(surahs)
    Dc = fisher_rao(Pm)
    dc = window_means(Dc)

    Rm = rhyme_matrix(surahs)
    dr = window_means(cosine_dist(Rm))

    Phm = phoneme_matrix(surahs)
    dp = window_means(cosine_dist(Phm))

    letters = np.array([np.mean([sum(len(w) for w in u) for u in su]) if su else 0.0
                        for su in surahs])
    words = np.array([np.mean([len(u) for u in su]) if su else 0.0 for su in surahs])
    dl = np.array([letters[s:s + K_WIN].mean() for s in range(0, 114 - K_WIN + 1)])
    dw = np.array([words[s:s + K_WIN].mean() for s in range(0, 114 - K_WIN + 1)])

    return dict(
        G1_content=fit_kink(dc, 50),
        G2_rhyme=fit_kink(dr, 50),
        G3_phoneme=fit_kink(dp, 75),
        G4_letters=fit_kink(dl, 50),
        G4_words_DEGENERATE=fit_kink(dw, 50),
        G5_antitwin=dict(r_content_rhyme=pearson(dc, dr),
                         r_content_phoneme=pearson(dc, dp)),
        _dbar=dict(content=dc.tolist(), rhyme=dr.tolist(), phoneme=dp.tolist()),
    )


def law_G6_antichiasmus(surahs, rng, n_perm, sizes=(5, 7, 9, 11, 13)):
    """
    Transported cf-026 mechanism-2 statistic: for every window of w consecutive
    units inside a pseudo-surah, the ring score is the mean token-set Jaccard of
    mirror-paired units (i, w-1-i).  Null: permute the unit order within the
    window.  Reported as the mean permutation-z over all windows.
    Negative mean z = anti-chiastic (the published Qurʾān value is ~ -0.15).
    """
    zs = []
    for su in surahs:
        sets = [frozenset(u) for u in su]
        n = len(sets)
        for w in sizes:
            if n < w:
                continue
            for st in range(0, n - w + 1):
                blk = sets[st:st + w]
                if any(len(b) == 0 for b in blk):
                    continue

                def ring(order):
                    tot, cnt = 0.0, 0
                    for i in range(w // 2):
                        a, b = blk[order[i]], blk[order[w - 1 - i]]
                        un = len(a | b)
                        if un:
                            tot += len(a & b) / un
                            cnt += 1
                    return tot / cnt if cnt else 0.0

                obs = ring(list(range(w)))
                null = np.empty(n_perm)
                base = np.arange(w)
                for t in range(n_perm):
                    null[t] = ring(list(rng.permutation(base)))
                sd = null.std()
                if sd > 0:
                    zs.append((obs - null.mean()) / sd)
    zs = np.array(zs)
    return dict(n_windows=int(zs.size), mean_z=float(zs.mean()) if zs.size else float('nan'),
                frac_positive=float((zs > 0).mean()) if zs.size else float('nan'),
                median_z=float(np.median(zs)) if zs.size else float('nan'))


G7_FEATURES = ['إذ', 'لما', 'قالوا', 'إذا', 'ثم']
P1 = {'نا', 'انا', 'نحن'}
P2 = {'انت', 'انتم', 'كم', 'كنتم'}
P3 = {'هو', 'هم', 'هي', 'هن'}


def law_G7_register(surahs, labels):
    """
    Transported cf-028 statistic: per-unit 6-feature thin-grammar vector,
    leave-one-out nearest-centroid accuracy, reported as lift over the
    majority-class baseline of the SAME label vector.
    """
    X = np.zeros((114, 6))
    for i, su in enumerate(surahs):
        toks = [w for u in su for w in u]
        n = max(1, len(toks))
        c = Counter(toks)
        for j, f in enumerate(G7_FEATURES):
            X[i, j] = c.get(f, 0) / n
        shifts = 0
        prev = None
        for u in su:
            cur = None
            for w in u:
                if w in P1:
                    cur = 1
                elif w in P2:
                    cur = 2
                elif w in P3:
                    cur = 3
            if cur is not None:
                if prev is not None and cur != prev:
                    shifts += 1
                prev = cur
        X[i, 5] = shifts / max(1, len(su))
    mu, sd = X.mean(0), X.std(0)
    sd[sd == 0] = 1.0
    X = (X - mu) / sd
    y = np.asarray(labels)
    classes = sorted(set(y.tolist()))
    correct = 0
    for i in range(114):
        mask = np.ones(114, bool); mask[i] = False
        best, bestd = None, None
        for c in classes:
            sel = mask & (y == c)
            if not sel.any():
                continue
            d = float(np.linalg.norm(X[i] - X[sel].mean(0)))
            if bestd is None or d < bestd:
                best, bestd = c, d
        if best == y[i]:
            correct += 1
    acc = correct / 114
    maj = max(Counter(y.tolist()).values()) / 114
    return dict(accuracy=acc, majority=maj, lift=acc / maj if maj else float('nan'))


def law_G8_uas_dispersion(surahs):
    """
    H-NEW-840 is a composite ranking index with no null hypothesis, so no
    verdict is issued.  Diagnostic only: the dispersion of a transported
    3-component index z(|content-outlier|) + z(max neighbour cost) + z(|sig|).
    """
    Pm = content_matrix(surahs)
    D = fisher_rao(Pm)
    off = D.copy()
    np.fill_diagonal(off, np.nan)          # 0*nan is nan, so eye()*nan would blank D
    centroid = np.nanmean(off, axis=1)
    nb = np.array([max(D[i, i - 1] if i > 0 else 0.0,
                       D[i, i + 1] if i < 113 else 0.0) for i in range(114)])
    Rm = rhyme_matrix(surahs)
    ent = np.array([-(p[p > 0] * np.log(p[p > 0])).sum() for p in Rm])

    def z(v):
        s = v.std()
        return (v - v.mean()) / s if s > 0 else np.zeros_like(v)

    uas = np.abs(z(centroid)) + z(nb) + np.abs(z(ent))
    return dict(sd=float(uas.std()), iqr=float(np.subtract(*np.percentile(uas, [75, 25]))),
                rng=float(uas.max() - uas.min()))


def law_G9_pericope_flip(surahs, rng, n_perm=1000, n_classes=5):
    """
    Transported cf-025 pericope-flip, following H-NEW-2680's L3: take the five
    best-shot marker word-types (attested in 5-15 distinct pseudo-surahs, most
    attestations), and test whether the pericopes hosting them cohere above a
    random-pericope baseline.  Reports the flip z per class.
    """
    flat = [u for su in surahs for u in su]
    unit_sets = [frozenset(u) for u in flat]
    unit_surah = np.repeat(np.arange(114), [len(su) for su in surahs])
    attest = defaultdict(list)
    for i, s in enumerate(unit_sets):
        for w in s:
            attest[w].append(i)
    cands = []
    for w, idxs in attest.items():
        ns = len({unit_surah[i] for i in idxs})
        if 5 <= ns <= 15:
            cands.append((len(idxs), w, idxs))
    cands.sort(reverse=True)
    out = []
    N = len(flat)
    for _, w, idxs in cands[:n_classes]:
        peri = []
        for i in idxs:
            lo, hi = max(0, i - 2), min(N, i + 3)
            peri.append(frozenset().union(*unit_sets[lo:hi]))
        if len(peri) < 2:
            continue

        def jac(ps):
            t, c = 0.0, 0
            for a in range(len(ps)):
                for b in range(a + 1, len(ps)):
                    un = len(ps[a] | ps[b])
                    if un:
                        t += len(ps[a] & ps[b]) / un
                        c += 1
            return t / c if c else 0.0

        obs = jac(peri)
        null = np.empty(n_perm)
        for t in range(n_perm):
            pick = rng.choice(N, size=len(idxs), replace=False)
            rp = []
            for i in pick:
                lo, hi = max(0, i - 2), min(N, i + 3)
                rp.append(frozenset().union(*unit_sets[lo:hi]))
            null[t] = jac(rp)
        sd = null.std()
        out.append(dict(marker=w, n_host_surahs=len({unit_surah[i] for i in idxs}),
                        observed=obs, null_mean=float(null.mean()),
                        z=float((obs - null.mean()) / sd) if sd > 0 else float('nan'),
                        flips=bool(sd > 0 and (obs - null.mean()) / sd > 1.96)))
    return out


# ---------------------------------------------------------------------------
# 5. DRIVER
# ---------------------------------------------------------------------------
def run_corpus(name, words, n_offsets, rng, arm='matched', full=True,
               n_ring_perm=N_RING_PERM):
    """Run the law suite over `n_offsets` partitions of one word stream."""
    need = sum(QVERSE_WLEN)
    slack = len(words) - need
    if slack < 0:
        return dict(error='insufficient words: have %d need %d' % (len(words), need))
    offsets = [0] if n_offsets <= 1 else \
        [0] + sorted(rng.integers(0, slack + 1, size=n_offsets - 1).tolist())
    grouper = group_matched if arm == 'matched' else group_uniform
    draws = []
    for oi, off in enumerate(offsets):
        units, err = partition_at(words, off)
        if err:
            continue
        surahs = grouper(units)
        rec = laws_G1_G5(surahs)
        rec.pop('_dbar', None)
        rec['offset'] = int(off)
        if full and oi == 0:
            rec['G6'] = law_G6_antichiasmus(surahs, rng, n_ring_perm)
            rec['G8'] = law_G8_uas_dispersion(surahs)
            rec['G9'] = law_G9_pericope_flip(surahs, rng)
            thirds = np.repeat([0, 1, 2], [38, 38, 38])
            rec['G7'] = law_G7_register(surahs, thirds)
        draws.append(rec)
        if (oi + 1) % 25 == 0:
            log('  [%s/%s] %d/%d partitions' % (name, arm, oi + 1, len(offsets)))
    return dict(name=name, arm=arm, n_draws=len(draws), draws=draws)


def summarise(draws, path):
    """min/max/mean of a nested statistic across offset draws."""
    vals = []
    for d in draws:
        cur = d
        for k in path:
            cur = cur.get(k) if isinstance(cur, dict) else None
            if cur is None:
                break
        if isinstance(cur, (int, float)) and not math.isnan(cur):
            vals.append(float(cur))
    if not vals:
        return None
    return dict(n=len(vals), min=min(vals), max=max(vals),
                mean=sum(vals) / len(vals), first=vals[0])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--seed', type=int, default=SEED)
    ap.add_argument('--n-offsets', type=int, default=N_OFFSET)
    ap.add_argument('--n-ring-perm', type=int, default=N_RING_PERM)
    ap.add_argument('--tag', default='')
    args = ap.parse_args()

    t0 = time.time()
    verify_locks()

    stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    rundir = P('findings/phase-b-hypotheses/runs/h-new-2720/' + stamp +
               (('-' + args.tag) if args.tag else ''))
    os.makedirs(rundir, exist_ok=True)
    log('[run] %s' % rundir)

    rng = np.random.default_rng(args.seed)
    res = dict(id='H-NEW-2720', prereg_sha256=PREREG_SHA, seed=args.seed,
               n_offsets=args.n_offsets, n_ring_perm=args.n_ring_perm, utc=stamp)

    # ---- MW-6 instrument controls -----------------------------------------
    mw6 = dict(n_surahs=len(QURAN), n_verses=sum(NV),
               partition_words_required=sum(QVERSE_WLEN))
    if sum(NV) != 6236 or len(QURAN) != 114:
        sys.exit('MW-6 FAIL: corpus shape')

    # QAC-instrument reproduction of H-NEW-660 (R^2 must be ~0.986)
    ROOT_RE = re.compile(r'ROOT:([^|]+)')
    LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
    vroots = defaultdict(list)
    with open(P('data/morphology/quranic-corpus-morphology-0.4.txt'), encoding='utf-8') as f:
        for line in f:
            if not line.startswith('('):
                continue
            parts = line.rstrip('\n').split('\t')
            if len(parts) < 4:
                continue
            m = LOC_RE.match(parts[0])
            if not m or 'STEM' not in parts[3]:
                continue
            rm = ROOT_RE.search(parts[3])
            if rm:
                vroots[(int(m.group(1)), int(m.group(2)))].append(rm.group(1))
    gc = Counter()
    for lst in vroots.values():
        gc.update(lst)
    topr = [r for r, _ in gc.most_common(K_TOP)]
    tix = {r: i for i, r in enumerate(topr)}
    Cq = np.zeros((114, K_TOP))
    vi = 0
    for si, s in enumerate(QURAN):
        for v in s['verses']:
            for r in vroots.get((s['id'], v['id']), ()):
                j = tix.get(r)
                if j is not None:
                    Cq[si, j] += 1.0
            vi += 1
    Pq = Cq + DIR_ALPHA
    Pq /= Pq.sum(axis=1, keepdims=True)
    qac_fit = fit_kink(window_means(fisher_rao(Pq)), 50)
    mw6['quran_QAC_G1'] = qac_fit
    if not (0.95 <= qac_fit['r2'] <= 1.0):
        sys.exit('MW-6 FAIL: QAC G1 R^2 = %.4f, expected ~0.986' % qac_fit['r2'])
    log('[MW-6] QAC-instrument H-NEW-660 reproduced: R2=%.4f beta=%.5f'
        % (qac_fit['r2'], qac_fit['beta']))
    res['mw6'] = mw6

    # ---- QURAN-SURF (the comparator) --------------------------------------
    log('[QURAN-SURF] matched arm')
    qs = group_matched(QURAN_UNITS)
    quran = laws_G1_G5(qs)
    quran.pop('_dbar', None)
    quran['G6'] = law_G6_antichiasmus(qs, np.random.default_rng(args.seed), args.n_ring_perm)
    quran['G8'] = law_G8_uas_dispersion(qs)
    quran['G9'] = law_G9_pericope_flip(qs, np.random.default_rng(args.seed))
    quran['G7'] = law_G7_register(qs, np.repeat([0, 1, 2], [38, 38, 38]))
    res['QURAN_SURF'] = quran
    log('[QURAN-SURF] G1 R2=%.4f b=%.5f | G5 r=%.4f | G6 z=%.3f'
        % (quran['G1_content']['r2'], quran['G1_content']['beta'],
           quran['G5_antitwin']['r_content_rhyme'], quran['G6']['mean_z']))

    log('[QURAN-SURF] uniform arm (length-confound isolator)')
    quq = laws_G1_G5(group_uniform(QURAN_UNITS))
    quq.pop('_dbar', None)
    res['QURAN_SURF_uniform'] = quq
    log('[QURAN-SURF/uniform] G1 R2=%.4f b=%.5f'
        % (quq['G1_content']['r2'], quq['G1_content']['beta']))

    # ---- baselines ---------------------------------------------------------
    streams = dict(
        BL_POETRY=(load_poetry(), 1),
        BL_BUKHARI=(load_words('data/baseline-corpora/raw/bukhari-noquran.txt'),
                    args.n_offsets),
        BL_JAHIZ=(load_words('data/baseline-corpora/raw/jahiz-hayawan.txt'),
                  args.n_offsets),
    )
    res['baselines'] = {}
    res['baselines_uniform'] = {}
    for nm, (wd, k) in streams.items():
        log('[%s] %d words, %d partitions (matched arm)' % (nm, len(wd), k))
        res['baselines'][nm] = run_corpus(nm, wd, k,
                                          np.random.default_rng(args.seed), 'matched',
                                          n_ring_perm=args.n_ring_perm)
        log('[%s] uniform arm' % nm)
        res['baselines_uniform'][nm] = run_corpus(
            nm, wd, k, np.random.default_rng(args.seed), 'uniform', full=False)

    # ---- verdicts ----------------------------------------------------------
    res['summary'] = build_summary(res)
    res['walltime_sec'] = round(time.time() - t0, 1)

    with open(os.path.join(rundir, 'h-new-2720.json'), 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=1)
    manifest = dict(id='H-NEW-2720', utc=stamp, seed=args.seed,
                    prereg=dict(path=PREREG_REL, sha256=PREREG_SHA),
                    frozen_inputs={k: v for k, v in FROZEN.items()},
                    poetry_corpus=dict(files=POETRY_FILES, sha256=POETRY_SHA),
                    script='findings/phase-b-hypotheses/scripts/h-new-2720.py')
    with open(os.path.join(rundir, 'manifest.json'), 'w', encoding='utf-8') as f:
        json.dump(manifest, f, ensure_ascii=False, indent=1)
    if not args.tag:
        with open(P('findings/phase-b-hypotheses/csv/h-new-2720.json'),
                  'w', encoding='utf-8') as f:
            json.dump(res, f, ensure_ascii=False, indent=1)

    print_report(res)
    log('[done] %.1fs  %s' % (res['walltime_sec'], rundir))


def build_summary(res):
    q = res['QURAN_SURF']
    out = {}
    specs = [
        ('G1_content', ['G1_content', 'r2'], 'r2', MARGIN_R2, 'higher'),
        ('G2_rhyme', ['G2_rhyme', 'r2'], 'r2', MARGIN_R2, 'higher'),
        ('G3_phoneme', ['G3_phoneme', 'r2'], 'r2', MARGIN_R2, 'higher'),
        ('G4_letters', ['G4_letters', 'r2'], 'r2', MARGIN_R2, 'higher'),
    ]
    for key, path, _kind, margin, _dirn in specs:
        qv = q[path[0]][path[1]]
        row = dict(quran_surface=qv, margin=margin, baselines={})
        for nm, blk in res['baselines'].items():
            row['baselines'][nm] = summarise(blk.get('draws', []), path)
        out[key] = row
    # G5 anti-twin (more negative = stronger)
    row = dict(quran_surface=q['G5_antitwin']['r_content_rhyme'], margin=MARGIN_R,
               baselines={})
    for nm, blk in res['baselines'].items():
        row['baselines'][nm] = summarise(blk.get('draws', []),
                                         ['G5_antitwin', 'r_content_rhyme'])
    out['G5_antitwin'] = row
    # G6/G7/G8 single-partition statistics
    for key, path in (('G6_mean_z', ['G6', 'mean_z']),
                      ('G7_lift', ['G7', 'lift']),
                      ('G8_uas_sd', ['G8', 'sd'])):
        cur = q
        for k in path:
            cur = cur[k]
        row = dict(quran_surface=cur, baselines={})
        for nm, blk in res['baselines'].items():
            d = blk.get('draws', [])
            row['baselines'][nm] = summarise(d, path)
        out[key] = row
    # G9 flip counts
    row = dict(quran_surface=sum(1 for c in q['G9'] if c['flips']),
               quran_classes=len(q['G9']), baselines={})
    for nm, blk in res['baselines'].items():
        d = blk.get('draws', [])
        if d and 'G9' in d[0]:
            row['baselines'][nm] = dict(flips=sum(1 for c in d[0]['G9'] if c['flips']),
                                        classes=len(d[0]['G9']),
                                        max_z=max((c['z'] for c in d[0]['G9']),
                                                  default=None))
    out['G9_pericope_flip'] = row
    # uniform arm (length-confound isolator)
    out['uniform_arm'] = dict(
        quran=res['QURAN_SURF_uniform']['G1_content'],
        baselines={nm: summarise(b.get('draws', []), ['G1_content', 'r2'])
                   for nm, b in res['baselines_uniform'].items()})
    return out


def print_report(res):
    s = res['summary']
    print('\n=================== H-NEW-2720 — GENRE-CONTROL SWEEP ===================')
    print('%-14s %12s | %-34s' % ('law', 'Quran(surf)', 'baselines  min..max (first)'))
    for k in ('G1_content', 'G2_rhyme', 'G3_phoneme', 'G4_letters', 'G5_antitwin'):
        r = s[k]
        print('%-14s %12.4f |' % (k, r['quran_surface']), end='')
        for nm, b in r['baselines'].items():
            if b:
                print('  %s %.3f..%.3f' % (nm.replace('BL_', ''), b['min'], b['max']),
                      end='')
        print()
    for k in ('G6_mean_z', 'G7_lift', 'G8_uas_sd'):
        r = s[k]
        print('%-14s %12.4f |' % (k, r['quran_surface']), end='')
        for nm, b in r['baselines'].items():
            if b:
                print('  %s %.3f' % (nm.replace('BL_', ''), b['first']), end='')
        print()
    g9 = s['G9_pericope_flip']
    print('%-14s %5d/%d flips |' % ('G9_flip', g9['quran_surface'], g9['quran_classes']),
          end='')
    for nm, b in g9['baselines'].items():
        print('  %s %d/%d' % (nm.replace('BL_', ''), b['flips'], b['classes']), end='')
    print()
    u = s['uniform_arm']
    print('\nUNIFORM ARM (length-confound isolator), G1 R2:')
    print('  Quran own verse stream, equal-size cuts: R2=%.4f beta=%.5f'
          % (u['quran']['r2'], u['quran']['beta']))
    for nm, b in u['baselines'].items():
        if b:
            print('  %-12s R2 %.3f..%.3f' % (nm, b['min'], b['max']))


if __name__ == '__main__':
    main()
