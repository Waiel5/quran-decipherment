#!/usr/bin/env python3
"""H-NEW-2680b — ADDENDUM to h-new-2680.py: repaired baseline-control transports.

Why this file exists, stated plainly:

  (1) The L1 transport pre-registered in prereg-h-new-2680 §5 searched for a marker
      consisting of a SINGLE opening word-type covering 15-45 pseudo-surahs.  It
      FAILED ITS OWN CONTROL-OF-THE-CONTROL: run on the Qurʾān it returned
      `n_candidates: 0` and could not detect the muqaṭṭaʿāt, because the real marker
      is a CLASS of 14 opening types, not one type.  An instrument that cannot find
      the effect in the corpus that has it cannot license a claim about corpora that
      may not.  Repaired here as a greedy marker-CLASS search of up to 14 members,
      run identically on all corpora, Bonferroni-corrected by the number of
      hypergeometric evaluations actually performed.

  (2) The L2 transport measures whether a corpus's own running order is Fisher-Rao
      near-geodesic.  Every pseudo-surah in the baseline arm is a contiguous cut of a
      continuous source text, so adjacency shares vocabulary BY CONSTRUCTION.  That
      confound applies to the Qurʾān too — its surahs are also contiguous blocks of
      the received text.  The decisive diagnostic added here asks whether L2 survives
      when surah boundaries are replaced by arbitrary contiguous cuts of the same
      corpus, and when contiguity itself is destroyed.

The pre-registered run (h-new-2680.py) is NOT modified; its unrepaired L1-BL result
stands on disk as the record of what the locked instrument produced.

Pre-reg SHA-256: 012ca709fad64bc8369313486095cc092e30414eccf45b1eca4e1b978fd08f94
Seed 20260509 / replication 20260519.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import random
import re
import sys
import time
from collections import Counter, defaultdict
from datetime import datetime, timezone
from math import comb

import numpy as np

PROJECT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(PROJECT, 'findings/phase-b-hypotheses/prereg-h-new-2680-pillar-conjunction.md')
EXPECTED_SHA = '012ca709fad64bc8369313486095cc092e30414eccf45b1eca4e1b978fd08f94'
QAC = os.path.join(PROJECT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
QJSON = os.path.join(PROJECT, 'quran-text/quran-no-tashkeel.json')
BASE = os.path.join(PROJECT, 'data/baseline-corpora/raw')

SEED, SEED_REP = 20260509, 20260519
PERM_L2 = 2000
K_TOP, DIR_ALPHA = 500, 0.5
MAX_MARKER_MEMBERS = 14          # matches the muqaṭṭaʿāt letter-set cardinality
MARKER_COVER_BAND = (5, 57)      # a "marker" may not cover more than half the corpus

RUNSTAMP = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
RUNDIR = os.path.join(PROJECT, 'findings/phase-b-hypotheses/runs/h-new-2680b', RUNSTAMP)


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''):
            h.update(c)
    return h.hexdigest()


if sha256_file(PREREG) != EXPECTED_SHA:
    log('FAIL pre-reg SHA mismatch')
    sys.exit(1)
log(f'pre-reg SHA-256 verified: {EXPECTED_SHA}')


def hyper_upper(N, K, n, x):
    if x > min(K, n):
        return 0.0
    return sum(comb(K, i) * comb(N - K, n - i) for i in range(max(0, x), min(K, n) + 1)) / comb(N, n)


# ------------------------------------------------------------------ corpora
quran = json.load(open(QJSON, encoding='utf-8'))
NV = {s['id']: len(s['verses']) for s in quran}
QUNITS = [v['text'].split() for s in quran for v in s['verses']]
QWLEN = [len(u) for u in QUNITS]
STARTS = np.cumsum([0] + [NV[s] for s in range(1, 115)])[:114]
NVARR = np.array([NV[s] for s in range(1, 115)])
assert len(QUNITS) == 6236

# Written with explicit escapes: a literal Arabic character class is bidi-reordered by
# some editors, which silently turns the diacritic ranges into ranges that swallow the
# whole alphabet.  These are the Arabic combining marks + tatweel, and nothing else.
AR_DIAC = re.compile('[\u0610-\u061A\u064B-\u065F\u0670\u06D6-\u06ED\u0640]')
NON_AR = re.compile('[^\u0621-\u064A\\s]')
NARROW = [re.compile(r'كتب|كتاب|الكتاب|الكتب|كتابك|كتابه|كتابي|كتابنا|كتبنا|كتبه|كتابا'),
          re.compile(r'قرآن|القرآن|قرءان|القرءان|قرآنا|قرانا|اقرأ')]


def normalise_words(text):
    return NON_AR.sub(' ', AR_DIAC.sub('', text)).split()


def cut_to_profile(words):
    """Cut a word stream into 6236 units matching the Quranic verse word-length profile."""
    need = sum(QWLEN)
    if len(words) < need:
        raise SystemExit(f'insufficient words: {len(words)} < {need}')
    units, p = [], 0
    for L in QWLEN:
        units.append(words[p:p + L]); p += L
    return units


# ------------------------------------------------------------------ L1 repaired
def l1_marker_class_search(units):
    """Greedy search for an opening marker CLASS of up to 14 types predicting
    kitāb/qurʾān vocabulary in units 1-3.  Returns the best Bonferroni-corrected p."""
    openers = defaultdict(set)
    for sid in range(1, 115):
        st = STARTS[sid - 1]
        if units[st]:
            openers[units[st][0]].add(sid)
    target = set()
    for sid in range(1, 115):
        st = STARTS[sid - 1]
        txt = ' '.join(' '.join(units[st + j]) for j in range(min(3, NV[sid])))
        if any(p.search(txt) for p in NARROW):
            target.add(sid)
    K = len(target)
    cands = list(openers.items())
    n_tests = 0
    chosen, cover, best = [], set(), (1.0, set(), [])
    for _ in range(MAX_MARKER_MEMBERS):
        step_best = None
        for w, s in cands:
            if w in chosen:
                continue
            nc = cover | s
            if not (MARKER_COVER_BAND[0] <= len(nc) <= MARKER_COVER_BAND[1]):
                continue
            p = hyper_upper(114, K, len(nc), len(nc & target))
            n_tests += 1
            if step_best is None or p < step_best[0]:
                step_best = (p, w, nc)
        if step_best is None or step_best[0] >= best[0]:
            break
        best = (step_best[0], step_best[2], chosen + [step_best[1]])
        chosen = best[2][:]
        cover = best[1]
    p_bonf = min(1.0, best[0] * max(1, n_tests))
    return dict(n_hypergeom_tests=n_tests, n_target=K, marker_types=best[2],
                marker_coverage=len(best[1]), x=len(best[1] & target),
                p_raw=best[0], p_bonf=p_bonf, satisfied=bool(p_bonf < 0.05),
                marker_surahs=sorted(best[1]))


# ------------------------------------------------------------------ L2
def fr_from_units(units, boundaries):
    """boundaries: array of start indices for the 114 blocks."""
    types = Counter(w for u in units for w in u)
    top = [w for w, _ in types.most_common(K_TOP)]
    tix = {w: i for i, w in enumerate(top)}
    M = np.zeros((len(units), K_TOP))
    for i, u in enumerate(units):
        for w in u:
            j = tix.get(w)
            if j is not None:
                M[i, j] += 1.0
    C = np.add.reduceat(M, boundaries, axis=0)
    P = C + DIR_ALPHA
    P /= P.sum(axis=1, keepdims=True)
    S = np.sqrt(P)
    return 2.0 * np.arccos(np.clip(S @ S.T, -1.0, 1.0))


def law2(D, rng, nperm=PERM_L2):
    n = D.shape[0]
    m = np.arange(n)
    L = float(D[m[:-1], m[1:]].sum())
    idx = np.arange(n)
    nulls = np.empty(nperm)
    for i in range(nperm):
        rng.shuffle(idx)
        nulls[i] = D[idx[:-1], idx[1:]].sum()
    mu, sd = float(nulls.mean()), float(nulls.std(ddof=1))
    n_le = int((nulls <= L).sum())
    return dict(L=L, null_mean=mu, null_sd=sd, z=(L - mu) / sd if sd else float('nan'),
                p=(n_le + 1) / (nperm + 1), satisfied=bool((n_le + 1) / (nperm + 1) < 0.05))


def arbitrary_cut_boundaries(n_units=6236):
    """114 contiguous blocks with the canonical verse-count profile but ignoring surah
    boundaries — identical block sizes, identical contiguity, no surah information."""
    return STARTS


# ------------------------------------------------------------------ main
def main():
    os.makedirs(RUNDIR, exist_ok=True)
    out = {'finding_id': 'H-NEW-2680b', 'prereg_sha256': EXPECTED_SHA, 'run_utc': RUNSTAMP,
           'seed': SEED, 'note': __doc__.strip().splitlines()[0]}

    corpora = {'QURAN_surface': QUNITS}
    buk = normalise_words(open(os.path.join(BASE, 'bukhari-noquran.txt'), encoding='utf-8').read())
    corpora['BL_BUKHARI'] = cut_to_profile(buk)
    pfiles = sorted([f for f in os.listdir(BASE)
                     if (f.startswith('muallaqa-') or f.startswith('diwan-'))
                     and f.endswith('.txt') and '.raw.' not in f and '.openiti.' not in f])
    poetry = []
    for f in pfiles:
        poetry += normalise_words(open(os.path.join(BASE, f), encoding='utf-8').read())
    corpora['BL_POETRY'] = cut_to_profile(poetry)
    out['poetry_files'] = pfiles

    # ---- L1 repaired marker-class search
    log('--- L1 repaired marker-class search ---')
    out['L1_repaired'] = {}
    for name, units in corpora.items():
        r = l1_marker_class_search(units)
        out['L1_repaired'][name] = r
        log(f"  {name:14s} markers={r['marker_types'][:6]}... cover={r['marker_coverage']} "
            f"x={r['x']}/{r['marker_coverage']} target={r['n_target']} "
            f"p_raw={r['p_raw']:.3e} p_bonf={r['p_bonf']:.3e} sat={r['satisfied']}")

    # ---- L2 contiguity diagnostic
    log('--- L2 contiguity diagnostic ---')
    rng = np.random.default_rng(SEED)
    pyrng = random.Random(SEED)
    l2 = {}
    for name, units in corpora.items():
        # (a) source order, blocks = canonical verse-count profile (surahs for the Quran)
        l2[f'{name}::source_order_contiguous'] = law2(fr_from_units(units, STARTS), rng)
        # (b) contiguity destroyed: shuffle units, then cut identically
        sh = units[:]
        pyrng.shuffle(sh)
        l2[f'{name}::units_shuffled_then_cut'] = law2(fr_from_units(sh, STARTS), rng)
    # (c) the sharpest control: the Quran cut into 114 arbitrary contiguous blocks that
    #     ignore surah boundaries but keep the same block-size profile.  Because the
    #     canonical profile IS the surah profile, an offset is applied so the cuts fall
    #     off the real seams.
    off = 137
    rolled = QUNITS[off:] + QUNITS[:off]
    l2['QURAN_surface::offset_cut_ignoring_surah_seams'] = law2(fr_from_units(rolled, STARTS), rng)
    for k, v in l2.items():
        log(f"  {k:58s} L={v['L']:8.3f} z={v['z']:+7.2f} p={v['p']:.5f}")
    out['L2_contiguity_diagnostic'] = l2

    # ---- QAC-root version of the same contiguity control (the published instrument)
    log('--- L2 contiguity diagnostic on the PUBLISHED QAC-root instrument ---')
    LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
    ROOT_RE = re.compile(r'ROOT:([^|]+)')
    vstem = defaultdict(list)
    with open(QAC, encoding='utf-8') as f:
        for line in f:
            if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
                continue
            parts = line.rstrip('\n').split('\t')
            if len(parts) < 4:
                continue
            m = LOC_RE.match(parts[0])
            if not m or 'STEM' not in parts[3]:
                continue
            rm = ROOT_RE.search(parts[3])
            if rm:
                vstem[(int(m.group(1)), int(m.group(2)))].append(rm.group(1))
    keys = [(s['id'], v['id']) for s in quran for v in s['verses']]
    gc = Counter()
    for lst in vstem.values():
        gc.update(lst)
    top = [r for r, _ in gc.most_common(K_TOP)]
    tix = {r: i for i, r in enumerate(top)}
    VM = np.zeros((6236, K_TOP))
    for i, k in enumerate(keys):
        for r in vstem.get(k, ()):
            j = tix.get(r)
            if j is not None:
                VM[i, j] += 1.0

    def fr_from_mat(M):
        C = np.add.reduceat(M, STARTS, axis=0)
        P = C + DIR_ALPHA
        P /= P.sum(axis=1, keepdims=True)
        S = np.sqrt(P)
        return 2.0 * np.arccos(np.clip(S @ S.T, -1.0, 1.0))

    qac = {}
    qac['real_surah_boundaries'] = law2(fr_from_mat(VM), rng)
    qac['offset_cut_ignoring_surah_seams'] = law2(fr_from_mat(np.roll(VM, -off, axis=0)), rng)
    perm = np.arange(6236); np.random.default_rng(SEED).shuffle(perm)
    qac['verses_shuffled_then_cut'] = law2(fr_from_mat(VM[perm]), rng)
    for o in (37, 311, 1013, 2579):
        qac[f'offset_cut_{o}'] = law2(fr_from_mat(np.roll(VM, -o, axis=0)), rng)
    for k, v in qac.items():
        log(f"  QAC {k:42s} L={v['L']:8.3f} z={v['z']:+7.2f} p={v['p']:.5f}")
    out['L2_contiguity_diagnostic_QAC_roots'] = qac

    manifest = {'finding_id': 'H-NEW-2680b', 'run_utc': RUNSTAMP,
                'prereg_sha256': EXPECTED_SHA,
                'script_sha256': sha256_file(os.path.abspath(__file__)),
                'frozen_inputs': {}, 'python': sys.version, 'numpy': np.__version__}
    for p in [QAC, QJSON, os.path.join(BASE, 'bukhari-noquran.txt')] + \
             [os.path.join(BASE, f) for f in pfiles]:
        manifest['frozen_inputs'][os.path.relpath(p, PROJECT)] = sha256_file(p)

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
    json.dump(manifest, open(os.path.join(RUNDIR, 'manifest.json'), 'w', encoding='utf-8'),
              indent=2, ensure_ascii=False)
    log(f'wrote {RUNDIR}')


if __name__ == '__main__':
    main()
