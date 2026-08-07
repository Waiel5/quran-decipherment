#!/usr/bin/env python3
"""H-NEW-2680 — joint improbability of the four pillar laws holding of one book.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2680-pillar-conjunction.md
Pre-reg SHA-256: 012ca709fad64bc8369313486095cc092e30414eccf45b1eca4e1b978fd08f94

Seeds 20260509 (primary) / 20260519 (replication).
Two joint nulls (NULL-A redactional, NULL-B verse-reallocation) + NULL-B' sensitivity
arm, plus the baseline-corpora control on Bukhari hadith and pre-Islamic poetry.

Deviation from INVESTIGATION-PROTOCOL 7.1 declared in pre-reg 7: numpy is used for
the Fisher-Rao matrix and permutation arithmetic; all statistical logic is explicit.
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
from itertools import combinations, permutations
from math import comb

import numpy as np

PROJECT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(PROJECT, 'findings/phase-b-hypotheses/prereg-h-new-2680-pillar-conjunction.md')
EXPECTED_SHA = '012ca709fad64bc8369313486095cc092e30414eccf45b1eca4e1b978fd08f94'

QAC = os.path.join(PROJECT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
QJSON = os.path.join(PROJECT, 'quran-text/quran-no-tashkeel.json')
T1820 = os.path.join(PROJECT, 'findings/phase-b-hypotheses/csv/h-new-1820.json')
BASE = os.path.join(PROJECT, 'data/baseline-corpora/raw')

SEED_PRIMARY, SEED_REPLICATION = 20260509, 20260519
N_A, N_B = 10000, 2000
PERM_L2, PERM_L3 = 2000, 1000

RUNSTAMP = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
RUNDIR = os.path.join(PROJECT, 'findings/phase-b-hypotheses/runs/h-new-2680', RUNSTAMP)


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def verify_prereg():
    actual = sha256_file(PREREG)
    if actual != EXPECTED_SHA:
        log(f'FAIL pre-reg SHA mismatch\n  expected={EXPECTED_SHA}\n  actual  ={actual}')
        sys.exit(1)
    log(f'pre-reg SHA-256 verified: {actual}')


# =============================================================================
# statistics helpers (explicit, no scipy)
# =============================================================================
def hyper_upper(N, K, n, x):
    """P(X >= x) under Hypergeometric(N, K, n)."""
    if K < 0 or n < 0 or x > min(K, n):
        return 0.0 if x > min(K, n) else 1.0
    denom = comb(N, n)
    return sum(comb(K, i) * comb(N - K, n - i) for i in range(max(0, x), min(K, n) + 1)) / denom


def binom_two_sided(r, n, p=0.5):
    """Exact two-sided binomial p-value by the method of small p (Sterne-free, standard)."""
    pmf = [comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(n + 1)]
    obs = pmf[r]
    tol = obs * (1 + 1e-9)
    return min(1.0, sum(v for v in pmf if v <= tol))


def phi_coeff(a, b):
    """Mean-square-contingency between two boolean arrays; None if a marginal is degenerate."""
    a = np.asarray(a, dtype=bool)
    b = np.asarray(b, dtype=bool)
    n11 = int((a & b).sum()); n10 = int((a & ~b).sum())
    n01 = int((~a & b).sum()); n00 = int((~a & ~b).sum())
    d = (n11 + n10) * (n01 + n00) * (n11 + n01) * (n10 + n00)
    if d == 0:
        return None
    return (n11 * n00 - n10 * n01) / math.sqrt(d)


def _m_eff_mult(p_joint, marg, keys, n_draws):
    """log p_joint / mean log p_marginal — 4.0 iff the laws multiply as independent."""
    floor = 1.0 / (n_draws + 1)
    denom = sum(math.log(max(marg[k], floor)) for k in keys) / 4.0
    if denom == 0.0:
        return None
    return math.log(p_joint) / denom


def m_eff_nyholt(corr):
    """Nyholt-Cheverud effective number of independent tests from a correlation matrix."""
    M = corr.shape[0]
    lam = np.linalg.eigvalsh(corr)
    return 1.0 + (M - 1.0) * (1.0 - float(np.var(lam, ddof=0)) / M)


# =============================================================================
# corpus load
# =============================================================================
verify_prereg()
T0 = time.time()

quran = json.load(open(QJSON, encoding='utf-8'))
assert len(quran) == 114
NV = {}
VTEXT = {}
VERSES = []
for s in quran:
    sid = s['id']
    NV[sid] = len(s['verses'])
    for v in s['verses']:
        VERSES.append((sid, v['id']))
        VTEXT[(sid, v['id'])] = v['text']
assert len(VERSES) == 6236
VIDX = {k: i for i, k in enumerate(VERSES)}
STARTS = np.cumsum([0] + [NV[s] for s in range(1, 115)])[:114]
NVARR = np.array([NV[s] for s in range(1, 115)])

LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')
verse_roots_all = defaultdict(set)
verse_stem_roots = defaultdict(list)
with open(QAC, encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('LOCATION') or not line.strip():
            continue
        parts = line.rstrip('\n').split('\t')
        if len(parts) < 4:
            continue
        m = LOC_RE.match(parts[0])
        if not m:
            continue
        s, v = int(m.group(1)), int(m.group(2))
        feat = parts[3]
        rm = ROOT_RE.search(feat)
        if not rm:
            continue
        r = rm.group(1)
        verse_roots_all[(s, v)].add(r)
        if 'STEM' in feat:
            verse_stem_roots[(s, v)].append(r)

# --- bitset representation of per-verse root sets (fast unions for L3)
ALL_ROOTS = sorted({r for st in verse_roots_all.values() for r in st})
RBIT = {r: 1 << i for i, r in enumerate(ALL_ROOTS)}
VBITS = np.zeros(6236, dtype=object)
for i, k in enumerate(VERSES):
    b = 0
    for r in verse_roots_all.get(k, ()):
        b |= RBIT[r]
    VBITS[i] = b

# --- dense per-verse STEM-root count matrix over top-K roots (for L2 + L4)
K_TOP, DIR_ALPHA = 500, 0.5
gcount = Counter()
for lst in verse_stem_roots.values():
    gcount.update(lst)
TOPR = [r for r, _ in gcount.most_common(K_TOP)]
TIDX = {r: i for i, r in enumerate(TOPR)}
VMAT = np.zeros((6236, K_TOP), dtype=np.float64)
for i, k in enumerate(VERSES):
    for r in verse_stem_roots.get(k, ()):
        j = TIDX.get(r)
        if j is not None:
            VMAT[i, j] += 1.0

# --- per-verse counts over ALL stem roots (for L4 density; sparse dict form)
ALL_STEM = sorted({r for lst in verse_stem_roots.values() for r in lst})
SIDX = {r: i for i, r in enumerate(ALL_STEM)}
VSTEM = np.zeros((6236, len(ALL_STEM)), dtype=np.float32)
for i, k in enumerate(VERSES):
    for r in verse_stem_roots.get(k, ()):
        VSTEM[i, SIDX[r]] += 1.0

log(f'[load] {time.time()-T0:.1f}s  roots={len(ALL_ROOTS)} stem-roots={len(ALL_STEM)}')

# =============================================================================
# LAW 1 — muqattaat -> book-introduction
# =============================================================================
MUQ_CANON = frozenset([2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31,
                       32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68])
NARROW = [re.compile(r'كتب|كتاب|الكتاب|الكتب|كتابك|كتابه|كتابي|كتابنا|كتبنا|كتبه|كتابا'),
          re.compile(r'قرآن|القرآن|قرءان|القرءان|قرآنا|قرانا|اقرأ')]


def law1(perm_idx, muq_set):
    """perm_idx: length-6236 int array giving, per slot, the canonical verse index."""
    hits = set()
    for sid in range(1, 115):
        st = STARTS[sid - 1]
        txt = ' '.join(VTEXT[VERSES[perm_idx[st + j]]] for j in range(min(3, NV[sid])))
        if any(p.search(txt) for p in NARROW):
            hits.add(sid)
    x = len(hits & muq_set)
    K = len(hits)
    return x, K, hyper_upper(114, K, len(muq_set), x)


# =============================================================================
# LAW 2 — Fisher-Rao geodesic optimality
# =============================================================================
def fr_matrix(perm_idx):
    C = np.add.reduceat(VMAT[perm_idx], STARTS, axis=0)
    P = C + DIR_ALPHA
    P /= P.sum(axis=1, keepdims=True)
    S = np.sqrt(P)
    return 2.0 * np.arccos(np.clip(S @ S.T, -1.0, 1.0))


def law2(D, order, rng, nperm=PERM_L2):
    o = np.asarray(order) - 1
    L = float(D[o[:-1], o[1:]].sum())
    idx = np.arange(114)
    nulls = np.empty(nperm)
    for i in range(nperm):
        rng.shuffle(idx)
        nulls[i] = D[idx[:-1], idx[1:]].sum()
    mu, sd = float(nulls.mean()), float(nulls.std(ddof=1))
    n_le = int((nulls <= L).sum())
    return dict(L=L, p=(n_le + 1) / (nperm + 1), z=(L - mu) / sd if sd else float('nan'),
                null_mean=mu, null_sd=sd, n_le=n_le)


def tsp_2opt_bound(D, n_starts=8, max_passes=25):
    """Cheap upper bound on L_min: greedy-NN from n_starts nodes + 2-opt on the best."""
    n = D.shape[0]
    best = None
    for start in range(0, n, max(1, n // n_starts)):
        unv = set(range(n)); unv.discard(start)
        path = [start]; cur = start
        while unv:
            nxt = min(unv, key=lambda v: D[cur][v])
            path.append(nxt); unv.discard(nxt); cur = nxt
        L = float(D[np.array(path[:-1]), np.array(path[1:])].sum())
        if best is None or L < best[0]:
            best = (L, path)
    path = best[1][:]
    for _ in range(max_passes):
        improved = False
        for i in range(n - 2):
            a, b = path[i], path[i + 1]
            for j in range(i + 2, n):
                c = path[j]
                d = path[j + 1] if j + 1 < n else None
                delta = (D[a][c] - D[a][b]) if d is None else (D[a][c] + D[b][d] - D[a][b] - D[c][d])
                if delta < -1e-12:
                    path[i + 1:j + 1] = path[i + 1:j + 1][::-1]
                    improved = True
                    a, b = path[i], path[i + 1]
        if not improved:
            break
    return float(D[np.array(path[:-1]), np.array(path[1:])].sum())


# =============================================================================
# LAW 3 — pericope-scoping (5 cf-026-formal-surviving classes)
# =============================================================================
IBLIS = [(2, 34, 34), (7, 11, 25), (15, 31, 44), (17, 61, 65), (18, 50, 50),
         (20, 115, 123), (38, 71, 85)]
SAJDA = [(7, 206), (13, 15), (16, 50), (17, 109), (19, 58), (22, 18), (22, 77),
         (25, 60), (27, 26), (32, 15), (38, 24), (41, 38), (53, 62), (84, 21), (96, 19)]
NABI = [(8, 64), (8, 65), (8, 70), (9, 73), (33, 1), (33, 28), (33, 45), (33, 50),
        (33, 59), (60, 12), (65, 1), (66, 1), (66, 9)]
HAMDU = [1, 6, 18, 34, 35]
HAWAMIM = [40, 41, 42, 43, 44, 45, 46]

L3_CLASSES = {
    'iblis': [(s, a, b) for (s, a, b) in IBLIS],
    'sajda': [(s, max(1, v - 2), min(NV[s], v + 2)) for (s, v) in SAJDA],
    'nabi': [(s, v, min(NV[s], v + 2)) for (s, v) in NABI],
    'hamdu': [(s, 1, 3) for s in HAMDU],
    'hawamim': [(s, 1, 3) for s in HAWAMIM],
}
# absolute slot ranges (position-based, so they transport to any reallocation)
L3_SLOTS = {name: [(STARTS[s - 1] + a - 1, STARTS[s - 1] + b) for (s, a, b) in wins]
            for name, wins in L3_CLASSES.items()}


def mean_pair_jac_bits(bits):
    tot, npair = 0.0, 0
    for i, j in combinations(range(len(bits)), 2):
        u = bits[i] | bits[j]
        npair += 1
        if u:
            tot += (bits[i] & bits[j]).bit_count() / u.bit_count()
    return tot / npair if npair else 0.0


def law3_class(vb, slots, rnd, nperm=PERM_L3):
    """vb: length-6236 object array of per-slot root bitsets, in reading order."""
    obs, lens = [], []
    for (a, b) in slots:
        u = 0
        for i in range(a, b):
            u |= vb[i]
        obs.append(u); lens.append(b - a)
    J = mean_pair_jac_bits(obs)
    n = len(vb)
    vals = []
    for _ in range(nperm):
        ns = []
        for Lw in lens:
            st = rnd.randrange(0, n - Lw + 1)
            u = 0
            for i in range(st, st + Lw):
                u |= vb[i]
            ns.append(u)
        vals.append(mean_pair_jac_bits(ns))
    mu = sum(vals) / len(vals)
    sd = (sum((x - mu) ** 2 for x in vals) / len(vals)) ** 0.5
    nge = sum(1 for v in vals if v >= J)
    return dict(J=J, null_mean=mu, z=(J - mu) / sd if sd else float('nan'),
                p=(nge + 1) / (nperm + 1), passed=bool(J > mu and (nge + 1) / (nperm + 1) < 0.05))


def law3(perm_idx, rnd):
    vb = VBITS[perm_idx]
    per = {name: law3_class(vb, slots, rnd) for name, slots in L3_SLOTS.items()}
    return per, sum(1 for v in per.values() if v['passed'])


# =============================================================================
# LAW 4 — title-density independence
# =============================================================================
t1820 = json.load(open(T1820, encoding='utf-8'))
TITLES = {r['sid']: r['root'] for r in t1820['title_density_results']}
TESTED_SIDS = sorted(TITLES)
assert len(TESTED_SIDS) == 89


def law4(perm_idx, title_map):
    C = np.add.reduceat(VSTEM[perm_idx], STARTS, axis=0)      # 114 x |stem roots|
    tot = C.sum(axis=1)
    dens = np.divide(C, tot[:, None], out=np.zeros_like(C), where=tot[:, None] > 0)
    r1, ranks = 0, {}
    for sid, root in title_map.items():
        j = SIDX.get(root)
        if j is None:
            ranks[sid] = None
            continue
        col = dens[:, j]
        own = col[sid - 1]
        higher = int((col > own + 1e-12).sum())
        ranks[sid] = higher + 1
        if higher == 0:
            r1 += 1
    n = len(title_map)
    p = binom_two_sided(r1, n, 0.5)
    return dict(rank1=r1, n=n, p_binom=p, satisfied=bool(p > 0.05), ranks=ranks)


# =============================================================================
# criteria
# =============================================================================
def crit_L1(res, tier):
    return res[2] < 0.05 if tier == 'lenient' else res[2] <= 1e-11


def crit_L2(res, tier):
    return res['p'] < 0.05 if tier == 'lenient' else (res['p'] < 1.0 / (PERM_L2 + 1) and res['z'] <= -11.46)


def crit_L3(npass, tier):
    return npass >= 4 if tier == 'lenient' else npass == 5


def crit_L4(res, tier):
    return res['satisfied']


# =============================================================================
# canonical verification (abort if the corpus fails its own criteria)
# =============================================================================
CANON_IDX = np.arange(6236)
log('--- canonical verification ---')
rng0 = np.random.default_rng(SEED_PRIMARY)
rnd0 = random.Random(SEED_PRIMARY)

can_l1 = law1(CANON_IDX, MUQ_CANON)
can_D = fr_matrix(CANON_IDX)
can_l2 = law2(can_D, list(range(1, 115)), rng0)
can_l2['L_2opt'] = tsp_2opt_bound(can_D)
can_l2['ratio'] = can_l2['L'] / can_l2['L_2opt']
can_l3_per, can_l3_n = law3(CANON_IDX, rnd0)
can_l4 = law4(CANON_IDX, TITLES)

log(f'  L1 x={can_l1[0]}/29 K={can_l1[1]} p={can_l1[2]:.3e}')
log(f"  L2 L={can_l2['L']:.3f} z={can_l2['z']:.2f} p={can_l2['p']:.5f} ratio={can_l2['ratio']:.4f}")
log(f'  L3 {can_l3_n}/5 pass: ' + ', '.join(f"{k}:z={v['z']:+.2f}" for k, v in can_l3_per.items()))
log(f"  L4 rank1={can_l4['rank1']}/89 p_binom={can_l4['p_binom']:.4f}")

CANON_SAT = {'L1': crit_L1(can_l1, 'lenient'), 'L2': crit_L2(can_l2, 'lenient'),
             'L3': crit_L3(can_l3_n, 'lenient'), 'L4': crit_L4(can_l4, 'lenient')}
CANON_SAT_STRICT = {'L1': crit_L1(can_l1, 'strict'), 'L2': crit_L2(can_l2, 'strict'),
                    'L3': crit_L3(can_l3_n, 'strict'), 'L4': crit_L4(can_l4, 'strict')}
log(f'  canonical LENIENT satisfaction: {CANON_SAT}')
log(f'  canonical STRICT  satisfaction: {CANON_SAT_STRICT}')
if not all(CANON_SAT.values()):
    log('FAIL: canonical corpus does not satisfy its own LENIENT criteria — aborting per pre-reg 3.')
    sys.exit(2)


# =============================================================================
# null-draw generators
# =============================================================================
def draw_nullA(pyrng):
    order = list(range(1, 115)); pyrng.shuffle(order)
    muq = frozenset(pyrng.sample(range(1, 115), 29))
    tsids = TESTED_SIDS[:]; pyrng.shuffle(tsids)
    title_map = {tsids[i]: TITLES[TESTED_SIDS[i]] for i in range(len(TESTED_SIDS))}
    return order, muq, title_map


def draw_nullB(pyrng, pin_first=True):
    idx = np.empty(6236, dtype=np.int64)
    if pin_first:
        firsts = [STARTS[s - 1] for s in range(1, 115)]
        firstset = set(firsts)
        pool = [i for i in range(6236) if i not in firstset]
        pyrng.shuffle(pool)
        k = 0
        for s in range(1, 115):
            st = STARTS[s - 1]
            idx[st] = st
            for j in range(1, NV[s]):
                idx[st + j] = pool[k]; k += 1
    else:
        pool = list(range(6236)); pyrng.shuffle(pool)
        idx[:] = pool
    return idx


# =============================================================================
# arms
# =============================================================================
def run_arm(name, n_draws, seed, kind):
    """kind in {'A','B','Bprime'}"""
    pyrng = random.Random(seed)
    nprng = np.random.default_rng(seed)
    rec = {k: [] for k in ('L1', 'L2', 'L3', 'L4')}
    diag = defaultdict(list)
    t = time.time()
    for it in range(n_draws):
        if kind == 'A':
            order, muq, tmap = draw_nullA(pyrng)
            r1 = law1(CANON_IDX, muq)
            r2 = law2(can_D, order, nprng)
            r4 = law4(CANON_IDX, tmap)
            # L3 is exactly invariant under NULL-A (pre-reg 2); verified on a subsample below
            n3 = can_l3_n
            rec['L3'].append(dict(lenient=crit_L3(n3, 'lenient'), strict=crit_L3(n3, 'strict'), npass=n3))
        else:
            idx = draw_nullB(pyrng, pin_first=(kind == 'B'))
            r1 = law1(idx, MUQ_CANON)
            D = fr_matrix(idx)
            r2 = law2(D, list(range(1, 115)), nprng)
            per3, n3 = law3(idx, pyrng)
            r4 = law4(idx, TITLES)
            rec['L3'].append(dict(lenient=crit_L3(n3, 'lenient'), strict=crit_L3(n3, 'strict'), npass=n3))
            diag['l3_npass'].append(n3)
            if it < 200:
                diag['l2_ratio'].append(float(r2['L'] / tsp_2opt_bound(D, n_starts=4, max_passes=8)))
        rec['L1'].append(dict(lenient=crit_L1(r1, 'lenient'), strict=crit_L1(r1, 'strict'), x=r1[0], K=r1[1], p=r1[2]))
        rec['L2'].append(dict(lenient=crit_L2(r2, 'lenient'), strict=crit_L2(r2, 'strict'), z=r2['z'], p=r2['p'], L=r2['L']))
        rec['L4'].append(dict(lenient=crit_L4(r4, 'lenient'), strict=crit_L4(r4, 'strict'),
                              rank1=r4['rank1'], p=r4['p_binom']))
        if (it + 1) % max(1, n_draws // 10) == 0:
            log(f'  [{name}] {it+1}/{n_draws}  {time.time()-t:.0f}s')

    out = {'arm': name, 'kind': kind, 'seed': seed, 'n_draws': n_draws,
           'wall_seconds': time.time() - t}
    for tier in ('lenient', 'strict'):
        ind = {k: np.array([r[tier] for r in rec[k]], dtype=bool) for k in ('L1', 'L2', 'L3', 'L4')}
        marg = {k: float(v.mean()) for k, v in ind.items()}
        joint = ind['L1'] & ind['L2'] & ind['L3'] & ind['L4']
        n_joint = int(joint.sum())
        # dependence
        keys = ['L1', 'L2', 'L3', 'L4']
        phi = {}
        C = np.eye(4)
        for a, b in combinations(range(4), 2):
            v = phi_coeff(ind[keys[a]], ind[keys[b]])
            phi[f'{keys[a]}x{keys[b]}'] = v
            if v is not None:
                C[a, b] = C[b, a] = v
        meff = m_eff_nyholt(C)
        # shrinkage over all 24 orderings
        shrink = defaultdict(list)
        for perm in permutations(keys):
            cur = np.ones(n_draws, dtype=bool)
            for depth, k in enumerate(perm, start=1):
                cur = cur & ind[k]
                shrink[depth].append(int(cur.sum()))
        shrink_summary = {d: dict(min=min(v), median=float(np.median(v)), max=max(v))
                          for d, v in shrink.items()}
        # multiplicativity
        prod_marg = 1.0
        for k in keys:
            prod_marg *= max(marg[k], 1.0 / (n_draws + 1))
        p_joint = (n_joint + 1) / (n_draws + 1)
        out[tier] = dict(
            marginals=marg,
            marginal_counts={k: int(v.sum()) for k, v in ind.items()},
            n_joint=n_joint,
            p_joint_exact=p_joint,
            p_joint_floor=1.0 / (n_draws + 1),
            rule_of_three_95_upper=(3.0 / n_draws) if n_joint == 0 else None,
            product_of_marginals=prod_marg,
            joint_over_product=(p_joint / prod_marg) if prod_marg > 0 else None,
            phi=phi,
            m_eff_nyholt=meff,
            m_eff_multiplicativity=_m_eff_mult(p_joint, marg, keys, n_draws),
            shrinkage=shrink_summary,
            indicators={k: ''.join('1' if x else '0' for x in ind[k]) for k in keys},
        )
    if diag:
        out['diagnostics'] = {k: dict(mean=float(np.mean(v)), sd=float(np.std(v)),
                                      min=float(np.min(v)), max=float(np.max(v)), n=len(v))
                              for k, v in diag.items()}
    # raw per-draw statistic summaries (for reader inspection)
    out['raw_summary'] = {
        k: dict(
            p_mean=float(np.mean([r.get('p', np.nan) for r in rec[k]])) if 'p' in rec[k][0] else None,
        ) for k in ('L1', 'L2', 'L4')
    }
    out['L2_z_distribution'] = dict(
        mean=float(np.mean([r['z'] for r in rec['L2']])),
        sd=float(np.std([r['z'] for r in rec['L2']])),
        min=float(np.min([r['z'] for r in rec['L2']])),
        max=float(np.max([r['z'] for r in rec['L2']])))
    out['L1_x_distribution'] = dict(
        mean=float(np.mean([r['x'] for r in rec['L1']])),
        max=int(np.max([r['x'] for r in rec['L1']])))
    out['L4_rank1_distribution'] = dict(
        mean=float(np.mean([r['rank1'] for r in rec['L4']])),
        sd=float(np.std([r['rank1'] for r in rec['L4']])),
        min=int(np.min([r['rank1'] for r in rec['L4']])),
        max=int(np.max([r['rank1'] for r in rec['L4']])))
    return out


def l2_length_confound_diagnostic(seed, n=200):
    """Does the FR path-length test stay length-controlled once content is scrambled?

    Under a content-destroying null every surah draws from the same global root
    distribution, so any residual FR structure must be a function of surah SIZE alone.
    Locked comparison, run identically on the canonical corpus and on NULL-B draws:
      L(mushaf)  vs  L(length-sorted ascending)  vs  null mean,
      plus Spearman-free rank correlation between D[i,j] and |log n_i - log n_j|.
    """
    lensort = sorted(range(1, 115), key=lambda s: NV[s])

    def probe(D):
        o = np.array(lensort) - 1
        L_len = float(D[o[:-1], o[1:]].sum())
        m = np.arange(114)
        L_mus = float(D[m[:-1], m[1:]].sum())
        iu = np.triu_indices(114, 1)
        d = D[iu]
        ln = np.log(NVARR.astype(float))
        gap = np.abs(ln[iu[0]] - ln[iu[1]])
        rd = np.argsort(np.argsort(d)).astype(float)
        rg = np.argsort(np.argsort(gap)).astype(float)
        rho = float(np.corrcoef(rd, rg)[0, 1])
        return L_mus, L_len, rho, float(d.mean())

    can = probe(can_D)
    pyrng = random.Random(seed)
    rows = []
    for _ in range(n):
        rows.append(probe(fr_matrix(draw_nullB(pyrng, pin_first=True))))
    a = np.array(rows)
    return dict(
        canonical=dict(L_mushaf=can[0], L_length_sorted=can[1],
                       rank_corr_FRdist_vs_logsize_gap=can[2], mean_FR=can[3]),
        null_B=dict(n=n,
                    L_mushaf_mean=float(a[:, 0].mean()), L_length_sorted_mean=float(a[:, 1].mean()),
                    rank_corr_mean=float(a[:, 2].mean()), rank_corr_sd=float(a[:, 2].std()),
                    mean_FR=float(a[:, 3].mean()),
                    frac_mushaf_shorter_than_lengthsorted=float((a[:, 0] < a[:, 1]).mean())),
        reading='If rank_corr is near 0 on the canonical corpus but large under NULL-B, the '
                'reallocation null has manufactured a size-driven geometry that the L2 statistic '
                'is sensitive to, and NULL-B is not a valid null for L2.')


def verify_L3_invariance_under_A(seed, n=50):
    """Pre-reg 2: L3 is claimed exactly invariant under NULL-A. Verify, do not assume."""
    pyrng = random.Random(seed + 1)
    same = 0
    for _ in range(n):
        draw_nullA(pyrng)                     # consumes randomness; corpus untouched
        _, n3 = law3(CANON_IDX, random.Random(SEED_PRIMARY))
        if n3 == can_l3_n:
            same += 1
    return dict(n_checked=n, n_identical=same,
                invariant=bool(same == n),
                note='NULL-A randomises only marker labels, reading order and title '
                     'assignment; none is an argument of the L3 statistic.')


# =============================================================================
# D4 — the reference L4 has never had
# =============================================================================
def diagnostic_D4(seed, n=2000):
    pyrng = random.Random(seed)
    # frequency band of the real title roots
    global_counts = Counter()
    for lst in verse_stem_roots.values():
        global_counts.update(lst)
    real_freqs = sorted(global_counts.get(TITLES[s], 0) for s in TESTED_SIDS)
    lo, hi = real_freqs[0], real_freqs[-1]
    # per-surah pool of own-attested roots inside the band
    C = np.add.reduceat(VSTEM[CANON_IDX], STARTS, axis=0)
    pools = {}
    for sid in TESTED_SIDS:
        pool = [r for r in ALL_STEM
                if C[sid - 1, SIDX[r]] > 0 and lo <= global_counts[r] <= hi]
        pools[sid] = pool if pool else [TITLES[sid]]
    rs = []
    for _ in range(n):
        tmap = {sid: pyrng.choice(pools[sid]) for sid in TESTED_SIDS}
        rs.append(law4(CANON_IDX, tmap)['rank1'])
    rs = np.array(rs)
    ge = int((rs >= can_l4['rank1']).sum())
    return dict(n_draws=n, observed_rank1=can_l4['rank1'],
                random_own_root_mean=float(rs.mean()), sd=float(rs.std()),
                q05=float(np.quantile(rs, 0.05)), q50=float(np.quantile(rs, 0.5)),
                q95=float(np.quantile(rs, 0.95)),
                p_observed_ge_random=(ge + 1) / (n + 1),
                band=[int(lo), int(hi)])


# =============================================================================
# BASELINE CONTROL — instrument-matched surface-word arm
# =============================================================================
AR_DIAC = re.compile(r'[ؐ-ًؚ-ٰٟۖ-ۭـ]')
NON_AR = re.compile(r'[^ء-ي\s]')

QVERSE_WLEN = [len(VTEXT[k].split()) for k in VERSES]


def normalise_words(text):
    text = AR_DIAC.sub('', text)
    text = NON_AR.sub(' ', text)
    return text.split()


def build_pseudo_corpus(words):
    """Cut a word stream into 6236 units matching the Quran verse word-length profile."""
    need = sum(QVERSE_WLEN)
    if len(words) < need:
        return None, f'insufficient words: have {len(words)}, need {need}'
    units, p = [], 0
    for L in QVERSE_WLEN:
        units.append(words[p:p + L]); p += L
    return units, None


def surface_law_suite(units, order_is_canonical=True, seed=SEED_PRIMARY, label=''):
    """All four laws on surface word-types. units: list of 6236 token lists."""
    pyrng = random.Random(seed)
    nprng = np.random.default_rng(seed)
    types = Counter(w for u in units for w in u)
    top = [w for w, _ in types.most_common(K_TOP)]
    tix = {w: i for i, w in enumerate(top)}
    M = np.zeros((6236, K_TOP))
    for i, u in enumerate(units):
        for w in u:
            j = tix.get(w)
            if j is not None:
                M[i, j] += 1.0
    # ---- L2
    C = np.add.reduceat(M, STARTS, axis=0)
    P = C + DIR_ALPHA
    P /= P.sum(axis=1, keepdims=True)
    S = np.sqrt(P)
    D = 2.0 * np.arccos(np.clip(S @ S.T, -1.0, 1.0))
    r2 = law2(D, list(range(1, 115)), nprng)
    r2['ratio'] = r2['L'] / tsp_2opt_bound(D)
    # ---- L1 generous best-marker search
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
    cands = {w: s for w, s in openers.items() if 15 <= len(s) <= 45}
    best = None
    for w, s in cands.items():
        p = hyper_upper(114, len(target), len(s), len(s & target))
        if best is None or p < best['p_raw']:
            best = dict(marker=w, n_marked=len(s), x=len(s & target), K=len(target), p_raw=p)
    if best is None:
        r1 = dict(n_candidates=0, best=None, p_bonf=1.0, satisfied=False,
                  note='no opening word-type marks 15-45 pseudo-surahs')
    else:
        pb = min(1.0, best['p_raw'] * len(cands))
        r1 = dict(n_candidates=len(cands), best=best, p_bonf=pb, satisfied=bool(pb < 0.05))
    # ---- L3 five best-shot marker classes
    unit_sets = [frozenset(u) for u in units]
    unit_surah = np.repeat(np.arange(1, 115), NVARR)
    attest = defaultdict(list)
    for i, s in enumerate(unit_sets):
        for w in s:
            attest[w].append(i)
    cand3 = []
    for w, idxs in attest.items():
        nsur = len({unit_surah[i] for i in idxs})
        if 5 <= nsur <= 15:
            cand3.append((len(idxs), w, idxs))
    cand3.sort(reverse=True)
    classes = cand3[:5]
    # bitset per unit over the top-4000 word types (memory-bounded)
    vocab = [w for w, _ in types.most_common(4000)]
    wbit = {w: 1 << i for i, w in enumerate(vocab)}
    ub = np.zeros(6236, dtype=object)
    for i, u in enumerate(unit_sets):
        b = 0
        for w in u:
            v = wbit.get(w)
            if v:
                b |= v
        ub[i] = b
    per3 = {}
    for cnt, w, idxs in classes:
        slots = []
        for i in idxs[:15]:
            a = max(0, i - 2); b = min(6236, i + 3)
            slots.append((a, b))
        per3[w] = law3_class(ub, slots, pyrng)
    n3 = sum(1 for v in per3.values() if v['passed'])
    # ---- L4 random own-vocabulary titles
    full_types = sorted(types)
    fix = {w: i for i, w in enumerate(full_types)}
    FM = np.zeros((6236, len(full_types)), dtype=np.float32)
    for i, u in enumerate(units):
        for w in u:
            FM[i, fix[w]] += 1.0
    CC = np.add.reduceat(FM, STARTS, axis=0)
    tot = CC.sum(axis=1)
    dens = np.divide(CC, tot[:, None], out=np.zeros_like(CC), where=tot[:, None] > 0)
    gcounts = types
    band_lo = min(gcounts[w] for w in gcounts) if False else None
    # frequency band taken from the Quranic title-root band, rescaled by corpus size
    qcounts = Counter()
    for lst in verse_stem_roots.values():
        qcounts.update(lst)
    qb = sorted(qcounts.get(TITLES[s], 0) for s in TESTED_SIDS)
    scale = sum(types.values()) / 77797.0
    lo, hi = qb[0] * scale, qb[-1] * scale
    pools = {}
    for sid in TESTED_SIDS:
        pool = [w for w in full_types if CC[sid - 1, fix[w]] > 0 and lo <= gcounts[w] <= hi]
        pools[sid] = pool
    r1s = []
    for _ in range(200):
        c = 0
        for sid in TESTED_SIDS:
            if not pools[sid]:
                continue
            w = pyrng.choice(pools[sid])
            col = dens[:, fix[w]]
            if not (col > col[sid - 1] + 1e-12).any():
                c += 1
        r1s.append(c)
    r1s = np.array(r1s)
    ps = [binom_two_sided(int(x), 89, 0.5) for x in r1s]
    r4 = dict(rank1_mean=float(r1s.mean()), rank1_sd=float(r1s.std()),
              rank1_min=int(r1s.min()), rank1_max=int(r1s.max()),
              frac_draws_satisfying=float(np.mean([p > 0.05 for p in ps])),
              satisfied=bool(np.mean([p > 0.05 for p in ps]) > 0.5))
    return dict(
        label=label,
        n_words=sum(types.values()), n_types=len(types),
        L1=r1, L2=dict(**r2, satisfied=bool(r2['p'] < 0.05)),
        L3=dict(classes={str(k): v for k, v in per3.items()}, n_pass=n3, satisfied=bool(n3 >= 4)),
        L4=r4,
        n_laws_satisfied=int(r1['satisfied']) + int(r2['p'] < 0.05) + int(n3 >= 4) + int(r4['satisfied']),
    )


# =============================================================================
# MAIN
# =============================================================================
def main():
    os.makedirs(RUNDIR, exist_ok=True)
    results = {
        'finding_id': 'H-NEW-2680',
        'prereg_sha256': EXPECTED_SHA,
        'run_utc': RUNSTAMP,
        'seeds': {'primary': SEED_PRIMARY, 'replication': SEED_REPLICATION},
        'N': {'NULL_A': N_A, 'NULL_B': N_B, 'NULL_Bprime': N_B},
        'inner_perms': {'L2': PERM_L2, 'L3': PERM_L3},
        'canonical': {
            'L1': dict(x=can_l1[0], K=can_l1[1], p_hyper=can_l1[2],
                       published='24/29, p=3.17e-12 (H-NEW-53/56)'),
            'L2': {k: v for k, v in can_l2.items()},
            'L3': {'per_class': can_l3_per, 'n_pass': can_l3_n},
            'L4': {k: v for k, v in can_l4.items() if k != 'ranks'},
            'satisfaction_lenient': CANON_SAT,
            'satisfaction_strict': CANON_SAT_STRICT,
        },
        'L3_invariance_check_under_NULL_A': verify_L3_invariance_under_A(SEED_PRIMARY, 25),
        'L2_length_confound_diagnostic': l2_length_confound_diagnostic(SEED_PRIMARY, 200),
    }
    log(f"  L2 length-confound: {results['L2_length_confound_diagnostic']['null_B']}")

    log('=== NULL-A (primary seed) ===')
    results['NULL_A_primary'] = run_arm('NULL-A/20260509', N_A, SEED_PRIMARY, 'A')
    log('=== NULL-B (primary seed) ===')
    results['NULL_B_primary'] = run_arm('NULL-B/20260509', N_B, SEED_PRIMARY, 'B')
    log("=== NULL-B' (primary seed) ===")
    results['NULL_Bprime_primary'] = run_arm("NULL-B'/20260509", N_B, SEED_PRIMARY, 'Bprime')

    log('=== D4 diagnostic ===')
    results['D4_random_own_root_titles'] = diagnostic_D4(SEED_PRIMARY, 2000)
    log(f"  D4: {results['D4_random_own_root_titles']}")

    log('=== replication seed ===')
    results['NULL_A_replication'] = run_arm('NULL-A/20260519', N_A, SEED_REPLICATION, 'A')
    results['NULL_B_replication'] = run_arm('NULL-B/20260519', N_B, SEED_REPLICATION, 'B')
    results['NULL_Bprime_replication'] = run_arm("NULL-B'/20260519", N_B, SEED_REPLICATION, 'Bprime')

    # ---------------- baseline control
    log('=== baseline control ===')
    bl = {}
    # instrument-matched Quran reference
    qunits = [VTEXT[k].split() for k in VERSES]
    bl['QURAN_surface_reference'] = surface_law_suite(qunits, label='Quran (surface word-types)')
    log(f"  Quran surface: {bl['QURAN_surface_reference']['n_laws_satisfied']}/4")

    buk = normalise_words(open(os.path.join(BASE, 'bukhari-noquran.txt'), encoding='utf-8').read())
    u, err = build_pseudo_corpus(buk)
    bl['BL_BUKHARI'] = surface_law_suite(u, label='Bukhari hadith (114 pseudo-surahs)') if u else {'error': err}
    if u:
        log(f"  Bukhari: {bl['BL_BUKHARI']['n_laws_satisfied']}/4")

    poetry_files = sorted([f for f in os.listdir(BASE)
                           if (f.startswith('muallaqa-') or f.startswith('diwan-'))
                           and f.endswith('.txt') and '.raw.' not in f and '.openiti.' not in f])
    poetry = []
    for f in poetry_files:
        poetry += normalise_words(open(os.path.join(BASE, f), encoding='utf-8').read())
    u, err = build_pseudo_corpus(poetry)
    bl['BL_POETRY'] = surface_law_suite(u, label='pre-Islamic poetry (114 pseudo-surahs)') if u else {'error': err}
    bl['BL_POETRY_files'] = poetry_files
    bl['BL_POETRY_word_count'] = len(poetry)
    if u:
        log(f"  Poetry: {bl['BL_POETRY']['n_laws_satisfied']}/4")
    results['baseline_control'] = bl

    # ---------------- manifest
    manifest = {
        'finding_id': 'H-NEW-2680',
        'run_utc': RUNSTAMP,
        'prereg_path': os.path.relpath(PREREG, PROJECT),
        'prereg_sha256': EXPECTED_SHA,
        'script_sha256': sha256_file(os.path.abspath(__file__)),
        'frozen_inputs': {},
        'python': sys.version,
        'numpy': np.__version__,
    }
    for p in [QAC, QJSON, T1820, os.path.join(BASE, 'bukhari-noquran.txt')] + \
             [os.path.join(BASE, f) for f in poetry_files]:
        manifest['frozen_inputs'][os.path.relpath(p, PROJECT)] = sha256_file(p)

    def default(o):
        if isinstance(o, (np.bool_,)):
            return bool(o)
        if isinstance(o, (np.integer,)):
            return int(o)
        if isinstance(o, (np.floating,)):
            return float(o)
        raise TypeError(str(type(o)))

    with open(os.path.join(RUNDIR, 'result.json'), 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False, default=default)
    with open(os.path.join(RUNDIR, 'manifest.json'), 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    log(f'\nwrote {RUNDIR}')
    log(f'total wall {time.time()-T0:.0f}s')


if __name__ == '__main__':
    main()
