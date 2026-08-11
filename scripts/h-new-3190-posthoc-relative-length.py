#!/usr/bin/env python3
"""H-NEW-3190 POST-HOC diagnostic. NON-CONFIRMATORY; no registered verdict rests on it.

The §7.4 hand-check surfaced a defect in the POOL: at L>=5, d<=3 a "near-twin" can be two short
verses sharing only a function-word frame, e.g. Q 23:3 <-> Q 70:32, whose three differing tokens
are three of six. H-NEW-2380 set L>=8, d<=2 precisely to exclude "recognizably-different verses
sharing a stock phrase".

d is an ABSOLUTE edit count. d=3 on a 5-token verse is 60% of the verse; d=3 on a 20-token verse
is 15%. Stratifying on absolute d therefore merges unlike members -- cross-finding-030 mechanism 1
applied to the PREDICTOR side, which the locked design length-channelled only on the OUTCOME side.

This recomputes the primary contrast against RELATIVE edit distance and reports the whole curve.
"""
import json, os, re, sys, unicodedata
import numpy as np

ROOT = '/Users/grey/Downloads/quran'
RUN = sys.argv[1] if len(sys.argv) > 1 else \
    f'{ROOT}/findings/phase-b-hypotheses/runs/h-new-3190/20260809T121246Z'
OUT = RUN + '-posthoc'
LANGS = ['bn', 'en', 'es', 'fr', 'id', 'ru', 'sv', 'tr', 'ur', 'zh']
SEED, N_PERM = 20260509, 10000

rows = json.load(open(f'{RUN}/pool.json'))
T = {}
for L in LANGS:
    dd = json.load(open(f'{ROOT}/data/alt-text/risan-quran-json/dist/quran_{L}.json'))
    T[L] = {(s['id'], v['id']): v['translation'] for s in dd for v in s['verses']}


def key(x):
    return tuple(x) if isinstance(x, (list, tuple)) else \
        tuple(json.loads(x.replace('(', '[').replace(')', ']')))


def norm_tokens(s, lang):
    s = unicodedata.normalize('NFKC', s).lower()
    s = re.sub(r'\[[^\]]*\]', ' ', s); s = re.sub(r'\([^)]*\)', ' ', s)
    s = re.sub(r'[^\w\s]', ' ', s, flags=re.UNICODE)
    if lang == 'zh':
        s = ''.join(s.split()); return [s[i:i+2] for i in range(len(s)-1)] or list(s)
    return s.split()


def lev(a, b):
    if len(a) < len(b): a, b = b, a
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def pct(v):
    v = np.asarray(v, float); o = np.argsort(v, kind='mergesort'); out = np.empty(len(v)); i = 0
    while i < len(o):
        j = i
        while j + 1 < len(o) and v[o[j + 1]] == v[o[i]]: j += 1
        out[o[i:j + 1]] = (i + j) / 2.0 / max(len(v) - 1, 1); i = j + 1
    return out


A = [key(r['a']) for r in rows]; B = [key(r['b']) for r in rows]
d_arr = np.array([r['d'] for r in rows])
n_lex = np.array([r['n_lex'] for r in rows], float)
n_morph = np.array([r['n_morph'] for r in rows], float)
n_ind = np.array([r['n_indel'] for r in rows], float)
La = np.array([r['La'] for r in rows], float); Lb = np.array([r['Lb'] for r in rows], float)
Lmean = (La + Lb) / 2
rel = d_arr / Lmean                       # RELATIVE edit distance

CH = {'L1_raw_count': lambda e, x, y: float(e),
      'L2_div_max': lambda e, x, y: e / max(x, y, 1),
      'L3_div_mean': lambda e, x, y: 2.0 * e / max(x + y, 1)}
raw = {L: [(lambda x, y: (lev(x, y), len(x), len(y)))(norm_tokens(T[L][a], L), norm_tokens(T[L][b], L))
           for a, b in zip(A, B)] for L in LANGS}
pooled = {c: np.median(np.vstack([pct([f(*t) for t in raw[L]]) for L in LANGS]), axis=0)
          for c, f in CH.items()}
LENGTH = np.column_stack([np.log(np.maximum(La, Lb)), np.log(np.minimum(La, Lb)), np.abs(La - Lb)])


def _fit(X, y):
    b, *_ = np.linalg.lstsq(X, y, rcond=None); r = y - X @ b; return b, float(r @ r)


def contrast(y, lex, mor, mask, D, LEN):
    idx = np.flatnonzero(mask)
    if len(idx) < 12: return None
    Ds = D[idx]
    strata = [s for s in sorted(set(Ds.tolist()))
              if (Ds == s).sum() >= 5 and len(set(zip(lex[idx][Ds == s], mor[idx][Ds == s]))) > 1]
    if not strata: return None
    num = 0.0; w = 0
    for s in strata:
        m = Ds == s; ys = y[idx][m]
        if ys.std() == 0: continue
        ys = (ys - ys.mean()) / ys.std(); n = int(m.sum())
        X = np.column_stack([np.ones(n), LEN[idx][m], lex[idx][m], mor[idx][m]])
        b, _ = _fit(X, ys); num += (b[-2] - b[-1]) * n; w += n
    return num / w if w else None


print('POOL VALIDITY — what the L>=5, d<=3 window actually admitted')
for t in (0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 1.01):
    print(f'  relative edit distance d/mean_len <= {t:4.2f}: {int((rel <= t).sum()):4d} of {len(rows)} pairs')
print(f'  H-NEW-2380 window (d<=2, L>=8)          : {int(((d_arr<=2)&(La>=8)&(Lb>=8)).sum()):4d}')

print('\nPRIMARY CONTRAST vs POOL PURITY  (locked design stratifies on ABSOLUTE d)')
print(f'{"rel-edit cap":>13} {"n":>5}  ' + '  '.join(f'{c:>13}' for c in CH))
for t in (0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 1.01):
    m = rel <= t
    vals = [contrast(pooled[c], n_lex, n_morph, m, d_arr, LENGTH) for c in CH]
    print(f'{t:>13.2f} {int(m.sum()):>5}  ' +
          '  '.join('     n/a     ' if v is None else f'{v:>+13.5f}' for v in vals))

print('\nSAME, but STRATIFIED ON RELATIVE EDIT DISTANCE (quintiles) instead of absolute d')
q = np.digitize(rel, np.quantile(rel[d_arr > 0], [.2, .4, .6, .8]))
vals = [contrast(pooled[c], n_lex, n_morph, d_arr > 0, q, LENGTH) for c in CH]
print('  ' + '  '.join(f'{c}={v:+.5f}' if v is not None else f'{c}=n/a' for c, v in zip(CH, vals)))

print('\nTRANSLATOR-NOISE FLOOR on the 59 EXACT Arabic twins (d=0): per-language rank spread')
M = np.vstack([pct([CH['L2_div_max'](*t) for t in raw[L]]) for L in LANGS])
sp = M.max(axis=0) - M.min(axis=0)
print(f'  mean cross-language rank spread, d=0 pairs : {sp[d_arr==0].mean():.4f}')
print(f'  mean cross-language rank spread, d>=1 pairs: {sp[d_arr>0].mean():.4f}')
print(f'  d=0 pairs whose ten translations span >0.8 of the rank range: '
      f'{int((sp[d_arr==0]>0.8).sum())} of {int((d_arr==0).sum())}')

os.makedirs(OUT, exist_ok=True)
json.dump({'relative_edit_cap_curve': {
    str(t): {c: contrast(pooled[c], n_lex, n_morph, rel <= t, d_arr, LENGTH) for c in CH}
    for t in (0.15, 0.20, 0.25, 0.30, 0.40, 0.50, 1.01)},
    'relative_stratified': {c: v for c, v in zip(CH, vals)},
    'noise_floor_spread_d0': float(sp[d_arr == 0].mean()),
    'noise_floor_spread_d1plus': float(sp[d_arr > 0].mean())},
    open(f'{OUT}/relative-length.json', 'w'), indent=2)
print('\nwrote', f'{OUT}/relative-length.json')
