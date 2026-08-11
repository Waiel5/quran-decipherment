#!/usr/bin/env python3
"""
H-NEW-3190 — frontier item F-18. Does an Arabic near-twin distinction survive translation?

LOCKED to prereg findings/phase-b-hypotheses/prereg-h-new-3190-translation-invariance.md
SHA-256 73e92381880fee10edf98492122eac1e6729eef67e6e3060f8b219099481533c

Registered inferences (prereg §5):
  I1 PRIMARY  d-stratified composition contrast C = beta(n_lex) - beta(n_morph) > 0
  I2          beta(n_lex) > 0 within d-strata
  I3          per-language contrast positive in >= 9 of 10 languages (exact binomial)
Headline on every channel-bearing inference = WORST of length channels L1/L2/L3 (prereg §3.4).
Effect size is binding; p-values are decorative (prereg §4).
"""
import hashlib, json, math, os, re, sys, unicodedata
from collections import Counter, defaultdict
from datetime import datetime, timezone

import numpy as np

ROOT = '/Users/grey/Downloads/quran'
PREREG = f'{ROOT}/findings/phase-b-hypotheses/prereg-h-new-3190-translation-invariance.md'
EXPECTED_PREREG_SHA = '73e92381880fee10edf98492122eac1e6729eef67e6e3060f8b219099481533c'

SEED = 20260509
N_PERM = 10000
ALPHA = 0.05 / 3            # prereg §6.1 gate 2
DELTA_R2_FLOOR = 0.01       # prereg §6.1 gate 3, inherited from H-NEW-3160
LANGS = ['bn', 'en', 'es', 'fr', 'id', 'ru', 'sv', 'tr', 'ur', 'zh']
KMAX, LMIN = 3, 5
POOL_EXPECTED, POOL_TOL = 417, 5
TIE_ABORT = 0.50            # prereg §8 abort condition 5

# prereg §3.1 locked waqf set: U+06D6-U+06DE inclusive, plus U+06E9
WAQF_RE = re.compile('[' + re.escape(''.join(chr(c) for c in range(0x06D6, 0x06DF)) + '۩') + ']')


def sha256_file(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()


def abort(n, msg):
    raise SystemExit(f'ABORT (prereg §8 condition {n}): {msg}')


# ---------------------------------------------------------------- condition 1
actual = sha256_file(PREREG)
if actual != EXPECTED_PREREG_SHA:
    abort(1, f'pre-registration SHA-256 mismatch\n  expected {EXPECTED_PREREG_SHA}\n  actual   {actual}')
print(f'[ok] prereg SHA-256 verified: {actual}')

# ---------------------------------------------------------------- inputs
FROZEN = {
    'quran-no-tashkeel': f'{ROOT}/quran-text/quran-no-tashkeel.json',
    'qac-morphology-0.4': f'{ROOT}/data/morphology/quranic-corpus-morphology-0.4.txt',
    **{f'trans-{L}': f'{ROOT}/data/alt-text/risan-quran-json/dist/quran_{L}.json' for L in LANGS},
}
INPUT_SHA = {k: sha256_file(v) for k, v in FROZEN.items()}

qt = json.load(open(FROZEN['quran-no-tashkeel']))
verses = {(s['id'], v['id']): [w for w in WAQF_RE.sub(' ', v['text']).split() if w]
          for s in qt for v in s['verses']}
if len(verses) != 6236:
    abort(2, f'Arabic corpus has {len(verses)} verses, expected 6236')

word_root = {}
for line in open(FROZEN['qac-morphology-0.4'], encoding='utf-8'):
    if not line.startswith('('):
        continue
    p = line.rstrip('\n').split('\t')
    if len(p) < 4:
        continue
    loc = p[0].strip('()').split(':')
    if len(loc) != 4:
        continue
    s, v, w, _seg = (int(x) for x in loc)
    m = re.search(r'ROOT:([^|]+)', p[3])
    if m and (s, v, w) not in word_root:
        word_root[(s, v, w)] = m.group(1)

# ---------------------------------------------------------------- condition 2
T = {}
for L in LANGS:
    dd = json.load(open(FROZEN[f'trans-{L}']))
    if len(dd) != 114:
        abort(2, f'{L}: {len(dd)} surahs, expected 114')
    m = {(s['id'], v['id']): v['translation'] for s in dd for v in s['verses']}
    if len(m) != 6236:
        abort(2, f'{L}: {len(m)} verses, expected 6236')
    empty = [k for k, t in m.items() if not t.strip()]
    if empty:
        abort(2, f'{L}: {len(empty)} empty translations, first {empty[0]}')
    T[L] = m
print(f'[ok] 10 translations: 114 surahs / 6236 verses / 0 empty each')


def norm_tokens(s, lang):
    """prereg §3.3"""
    s = unicodedata.normalize('NFKC', s).lower()
    s = re.sub(r'\[[^\]]*\]', ' ', s)
    s = re.sub(r'\([^)]*\)', ' ', s)
    s = re.sub(r'[^\w\s]', ' ', s, flags=re.UNICODE)
    if lang == 'zh':
        s = ''.join(s.split())
        return [s[i:i + 2] for i in range(len(s) - 1)] or list(s)
    return s.split()


def lev(a, b):
    if len(a) < len(b):
        a, b = b, a
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def lev_trace(a, b):
    n, m = len(a), len(b)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        D[i][0] = i
    for j in range(m + 1):
        D[0][j] = j
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i - 1][j] + 1, D[i][j - 1] + 1, D[i - 1][j - 1] + (a[i - 1] != b[j - 1]))
    ops, i, j = [], n, m
    while i > 0 or j > 0:
        if i > 0 and j > 0 and D[i][j] == D[i - 1][j - 1] + (a[i - 1] != b[j - 1]):
            if a[i - 1] != b[j - 1]:
                ops.append(('sub', i, j))
            i, j = i - 1, j - 1
        elif i > 0 and D[i][j] == D[i - 1][j] + 1:
            ops.append(('del', i, j))
            i -= 1
        else:
            ops.append(('ins', i, j))
            j -= 1
    return D[n][m], ops


# ---------------------------------------------------------------- pool (prereg §3.1)
freq = Counter(t for toks in verses.values() for t in set(toks))
inv = defaultdict(list)
for key, toks in verses.items():
    if len(toks) < LMIN:
        continue
    for t in sorted(set(toks), key=lambda x: freq[x])[:4]:   # provably complete for d<=3
        inv[t].append(key)
cand = set()
for t, keys in inv.items():
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            a, b = keys[i], keys[j]
            if a[0] != b[0]:
                cand.add((a, b) if a < b else (b, a))

rows = []
for a, b in sorted(cand):
    ta, tb = verses[a], verses[b]
    if abs(len(ta) - len(tb)) > KMAX:
        continue
    dist, ops = lev_trace(ta, tb)
    if dist > KMAX:
        continue
    nm = nl = ni = 0
    nl_strict = n_noroot = 0
    for kind, i, j in ops:
        if kind == 'sub':
            ra, rb = word_root.get((a[0], a[1], i)), word_root.get((b[0], b[1], j))
            if ra and rb and ra == rb:
                nm += 1
            else:
                nl += 1
                if ra and rb:
                    nl_strict += 1        # both root-bearing, roots differ (prereg §7.6)
                else:
                    n_noroot += 1         # a root is absent
        else:
            ni += 1
    rows.append(dict(a=a, b=b, d=dist, n_morph=nm, n_lex=nl, n_indel=ni,
                     n_lex_strict=nl_strict, n_noroot=n_noroot,
                     La=len(ta), Lb=len(tb)))

# ---------------------------------------------------------------- conditions 3, 4
if not (POOL_EXPECTED - POOL_TOL <= len(rows) <= POOL_EXPECTED + POOL_TOL):
    abort(3, f'pool size {len(rows)} outside {POOL_EXPECTED} +/- {POOL_TOL}')
for r in rows:
    if r['n_morph'] + r['n_lex'] + r['n_indel'] != r['d']:
        abort(4, f'decomposition broken at {r["a"]}<->{r["b"]}')
print(f'[ok] pool n={len(rows)}  d-dist={dict(sorted(Counter(r["d"] for r in rows).items()))}')

# ---------------------------------------------------------------- outcome (prereg §3.3-3.5)
raw = {L: [] for L in LANGS}
for r in rows:
    for L in LANGS:
        x, y = norm_tokens(T[L][r['a']], L), norm_tokens(T[L][r['b']], L)
        raw[L].append((lev(x, y), len(x), len(y)))

CHANNELS = {
    'L1_raw_count': lambda e, x, y: float(e),
    'L2_div_max':   lambda e, x, y: e / max(x, y, 1),
    'L3_div_mean':  lambda e, x, y: 2.0 * e / max(x + y, 1),
}


def pct_rank(v):
    v = np.asarray(v, float)
    order = np.argsort(v, kind='mergesort')
    out = np.empty(len(v))
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
            j += 1
        out[order[i:j + 1]] = (i + j) / 2.0 / max(len(v) - 1, 1)
        i = j + 1
    return out


per_lang, pooled_y, tie_report = {}, {}, {}
for cname, f in CHANNELS.items():
    pl = {L: pct_rank([f(*t) for t in raw[L]]) for L in LANGS}
    per_lang[cname] = pl
    M = np.vstack([pl[L] for L in LANGS])
    pooled_y[cname] = np.median(M, axis=0)
    tie_pool = 1 - len(set(np.round(pooled_y[cname], 12))) / len(rows)
    tie_lang = float(np.mean([1 - len(set(np.round(pl[L], 12))) / len(rows) for L in LANGS]))
    tie_report[cname] = dict(pooled_tie=tie_pool, mean_per_language_tie=tie_lang)
    if tie_pool > TIE_ABORT:                                     # condition 5
        abort(5, f'{cname} pooled-outcome tie fraction {tie_pool:.4f} > {TIE_ABORT}')
    print(f'[ok] {cname}: pooled tie={tie_pool:.4f}  per-language tie={tie_lang:.4f}')

# ---------------------------------------------------------------- stratified model
d_arr = np.array([r['d'] for r in rows])
n_lex = np.array([r['n_lex'] for r in rows], float)
n_morph = np.array([r['n_morph'] for r in rows], float)
Lmax = np.array([max(r['La'], r['Lb']) for r in rows], float)
Lmin = np.array([min(r['La'], r['Lb']) for r in rows], float)
Ldiff = np.abs(np.array([r['La'] - r['Lb'] for r in rows], float))
LENGTH = np.column_stack([np.log(Lmax), np.log(Lmin), Ldiff])

STRATA = [s for s in sorted(set(d_arr.tolist()))
          if len(set(zip(n_lex[d_arr == s], n_morph[d_arr == s]))) > 1]
DROPPED = [s for s in sorted(set(d_arr.tolist())) if s not in STRATA]


def _fit(X, y):
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    resid = y - X @ beta
    return beta, float(resid @ resid)


def stratified(y, lex, mor, ind, D=None, LEN=None, STR=None):
    """Returns (contrast C, beta_lex_refIndel, beta_lex_noInt, dR2).

    D / LEN / STR default to the primary pool's stratifier, length block and strata list;
    the sensitivity block passes subsets so it runs identical math on a restricted pool.

    Prereg §5 says I2 is estimated with "n_indel and the length block present". Within a
    d-stratum n_lex + n_morph + n_indel = d exactly, so a model with an intercept AND all three
    counts is rank-deficient and that clause has no unique reading. Both full-rank readings are
    computed and the WORSE is taken for I2 (a tightening; disclosed in the finding):
      (a) intercept + n_lex + n_morph, n_indel as omitted reference  -> beta_lex_refIndel
      (b) no intercept + n_lex + n_morph + n_indel (spans the intercept) -> beta_lex_noInt
    The I1 CONTRAST beta_lex - beta_morph is algebraically identical under both, so I1 is
    unaffected by the ambiguity. dR2 is a model comparison and is likewise invariant."""
    D = d_arr if D is None else D
    LEN = LENGTH if LEN is None else LEN
    STR = STRATA if STR is None else STR
    num_c = num_b = num_b2 = 0.0
    sse_full = sse_red = sst = 0.0
    wtot = 0
    for s in STR:
        m = D == s
        ys = y[m]
        sd = ys.std()
        if sd == 0:
            continue
        ys = (ys - ys.mean()) / sd
        n = int(m.sum())
        base = np.column_stack([np.ones(n), LEN[m]])
        full = np.column_stack([base, lex[m], mor[m]])
        bf, ef = _fit(full, ys)
        _, er = _fit(base, ys)
        noint = np.column_stack([lex[m], mor[m], ind[m], LEN[m]])
        bn, _ = _fit(noint, ys)
        num_c += (bf[-2] - bf[-1]) * n
        num_b += bf[-2] * n
        num_b2 += bn[0] * n
        sse_full += ef
        sse_red += er
        sst += float(ys @ ys)
        wtot += n
    if wtot == 0:
        return 0.0, 0.0, 0.0, 0.0
    return (num_c / wtot, num_b / wtot, num_b2 / wtot, (sse_red - sse_full) / sst)


n_ind = np.array([r['n_indel'] for r in rows], float)
rng = np.random.default_rng(SEED)
PERM = []
for _ in range(N_PERM):
    lx, mr, iv = n_lex.copy(), n_morph.copy(), n_ind.copy()
    for s in STRATA:
        idx = np.flatnonzero(d_arr == s)
        p = rng.permutation(idx)
        lx[idx], mr[idx], iv[idx] = n_lex[p], n_morph[p], n_ind[p]
    PERM.append((lx, mr, iv))

results = {}
for cname in CHANNELS:
    y = pooled_y[cname]
    C, B, B2, dR2 = stratified(y, n_lex, n_morph, n_ind)
    nullC = np.empty(N_PERM); nullB = np.empty(N_PERM)
    nullB2 = np.empty(N_PERM); nullR = np.empty(N_PERM)
    for k, (lx, mr, iv) in enumerate(PERM):
        nullC[k], nullB[k], nullB2[k], nullR[k] = stratified(y, lx, mr, iv)
    results[cname] = dict(
        contrast=C, beta_lex_refIndel=B, beta_lex_noInt=B2, delta_r2=dR2,
        p_contrast=(1 + int((nullC >= C).sum())) / (N_PERM + 1),
        p_beta_lex_refIndel=(1 + int((nullB >= B).sum())) / (N_PERM + 1),
        p_beta_lex_noInt=(1 + int((nullB2 >= B2).sum())) / (N_PERM + 1),
        p_contrast_reverse=(1 + int((nullC <= C).sum())) / (N_PERM + 1),
        null_sd=float(nullC.std()), null_mean=float(nullC.mean()),
        S_star_contrast=C, S_max_contrast=float(nullC.max()),
        S_max_delta_r2=float(nullR.max()),
    )
    # I2 takes the WORSE of the two admissible parameterizations
    if B2 < B:
        results[cname]['beta_lex'] = B2
        results[cname]['p_beta_lex'] = results[cname]['p_beta_lex_noInt']
        results[cname]['beta_lex_param'] = 'no-intercept (worse)'
    else:
        results[cname]['beta_lex'] = B
        results[cname]['p_beta_lex'] = results[cname]['p_beta_lex_refIndel']
        results[cname]['beta_lex_param'] = 'indel-reference (worse)'
    print(f'[--] {cname}: C={C:+.5f} p={results[cname]["p_contrast"]:.6f} '
          f'dR2={dR2:.5f} beta_lex(worse)={results[cname]["beta_lex"]:+.5f}')

dr2s = [results[c]['delta_r2'] for c in CHANNELS]
DELTA_R2_LENGTHRULE = max(dr2s) - min(dr2s)

# ---------------------------------------------------------------- I3, exact binomial
def binom_ge(k, n, p=0.5):
    return sum(math.comb(n, i) * p ** n for i in range(k, n + 1))


i3 = {}
for cname in CHANNELS:
    signs = {}
    for L in LANGS:
        C, _, _, _ = stratified(per_lang[cname][L], n_lex, n_morph, n_ind)
        signs[L] = C
    pos = sum(1 for v in signs.values() if v > 0)
    i3[cname] = dict(positive=pos, per_language={k: float(v) for k, v in signs.items()},
                     exact_p=binom_ge(pos, 10))

# ---------------------------------------------------------------- verdict (prereg §6)
# "Headline = WORST" is applied PER GATE, not by first picking one channel: a gate passes only
# if it passes on the least favourable channel. This is the most conservative reading of
# prereg §3.4 + §6.1 and cannot select a favourable channel.
def gates(effect_key, p_key):
    ch_eff = min(CHANNELS, key=lambda c: results[c][effect_key])
    ch_p = max(CHANNELS, key=lambda c: results[c][p_key])
    ch_r2 = min(CHANNELS, key=lambda c: results[c]['delta_r2'])
    g = dict(
        worst_channel_effect=ch_eff, worst_channel_p=ch_p, worst_channel_dr2=ch_r2,
        effect=results[ch_eff][effect_key], p=results[ch_p][p_key],
        delta_r2=results[ch_r2]['delta_r2'],
        per_channel={c: dict(effect=results[c][effect_key], p=results[c][p_key],
                             delta_r2=results[c]['delta_r2']) for c in CHANNELS})
    g['gate_direction'] = g['effect'] > 0
    g['gate_p'] = g['p'] < ALPHA
    g['gate_floor'] = g['delta_r2'] >= DELTA_R2_FLOOR
    g['gate_lengthrule'] = g['delta_r2'] > DELTA_R2_LENGTHRULE
    g['PASS'] = all([g['gate_direction'], g['gate_p'], g['gate_floor'], g['gate_lengthrule']])
    return g


I1 = gates('contrast', 'p_contrast')
I2 = gates('beta_lex', 'p_beta_lex')
w3 = min(CHANNELS, key=lambda c: i3[c]['positive'])
I3 = dict(channel=w3, positive=i3[w3]['positive'], exact_p=i3[w3]['exact_p'],
          per_channel={c: i3[c]['positive'] for c in CHANNELS})
I3['PASS'] = I3['positive'] >= 9 and I3['exact_p'] < ALPHA

survivors = sum(1 for x in (I1, I2, I3) if x['PASS'])
if survivors == 3:
    verdict = 'CONFIRMED'
elif survivors == 2:
    verdict = 'SUPPORTED'
elif survivors == 1:
    verdict = 'PARTIAL'
else:
    verdict = 'NULL'
if not I1['PASS'] and verdict in ('CONFIRMED', 'SUPPORTED'):
    verdict = 'PARTIAL'                      # prereg §6.2 ceiling

reverse = any(results[c]['contrast'] < 0 and results[c]['p_contrast_reverse'] < ALPHA
              for c in CHANNELS)

# MDE (prereg §6.4): one-sided, 80% power
Z_ALPHA, Z_POWER = 2.128045, 0.841621
mde = {c: (Z_ALPHA + Z_POWER) * results[c]['null_sd'] for c in CHANNELS}
# prereg §6.4 S* vs S_max: if the observed effect misses the floor AND the largest effect this
# design matrix can produce from these outcome values ALSO misses it, the design was incapable
# of rejecting -> UNTESTABLE, not NULL. S_max is a Monte-Carlo lower bound (max over N_PERM).
untestable = {c: bool(results[c]['S_max_delta_r2'] < DELTA_R2_FLOOR) for c in CHANNELS}
headline_dr2_channel = min(CHANNELS, key=lambda c: results[c]['delta_r2'])
if verdict == 'NULL' and untestable[headline_dr2_channel]:
    verdict = 'UNTESTABLE'

# ------------------------------------------- sensitivities (prereg §7, NON-CONFIRMATORY)
def sens_contrast(mask, langs, lex=None, mor=None, ind=None):
    """Re-runs the identical estimator on a restricted pool / language set.
    Returns the WORST-channel contrast and dR2, or None if no stratum retains variation."""
    lex = n_lex if lex is None else lex
    mor = n_morph if mor is None else mor
    ind = n_ind if ind is None else ind
    idx = np.flatnonzero(mask)
    if len(idx) < 10:
        return None
    Ds, LENs = d_arr[idx], LENGTH[idx]
    strata = [s for s in sorted(set(Ds.tolist()))
              if len(set(zip(lex[idx][Ds == s], mor[idx][Ds == s]))) > 1
              and (Ds == s).sum() >= 5]
    if not strata:
        return None
    out = {}
    for cname in CHANNELS:
        M = np.vstack([per_lang[cname][L][idx] for L in langs])
        y = np.median(M, axis=0)
        C, _, _, dR2 = stratified(y, lex[idx], mor[idx], ind[idx], Ds, LENs, strata)
        out[cname] = (C, dR2)
    wc = min(out, key=lambda c: out[c][0])
    return dict(n=int(len(idx)), worst_channel=wc,
                contrast=out[wc][0], delta_r2=min(v[1] for v in out.values()),
                per_channel={c: dict(contrast=out[c][0], delta_r2=out[c][1]) for c in out})


La_ = np.array([r['La'] for r in rows]); Lb_ = np.array([r['Lb'] for r in rows])
n_lex_strict = np.array([r['n_lex_strict'] for r in rows], float)
n_noroot = np.array([r['n_noroot'] for r in rows], float)

SENS = {}
SENS['S2a_pool_d<=2_L>=8_(H-NEW-2380 window)'] = sens_contrast(
    (d_arr <= 2) & (La_ >= 8) & (Lb_ >= 8), LANGS)
SENS['S2b_pool_d<=3_L>=8'] = sens_contrast((La_ >= 8) & (Lb_ >= 8), LANGS)
SENS['S3_drop_English_(not independent of H-NEW-710)'] = sens_contrast(
    np.ones(len(rows), bool), [L for L in LANGS if L != 'en'])
SENS['S6_QAC_root_absence_strict'] = sens_contrast(
    np.ones(len(rows), bool), LANGS, lex=n_lex_strict, mor=n_morph,
    ind=n_ind + n_noroot)
for L in LANGS:
    SENS[f'S5_leave_out_{L}'] = sens_contrast(
        np.ones(len(rows), bool), [x for x in LANGS if x != L])

# descriptive: the translator-noise floor on the d=0 stratum (exact Arabic twins)
noise_floor = {}
for cname in CHANNELS:
    y = pooled_y[cname]
    noise_floor[cname] = dict(
        d0_mean=float(y[d_arr == 0].mean()), d0_n=int((d_arr == 0).sum()),
        d1plus_mean=float(y[d_arr > 0].mean()))

# ---------------------------------------------------------------- immutable run dir
STAMP = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
RUN = f'{ROOT}/findings/phase-b-hypotheses/runs/h-new-3190/{STAMP}'
os.makedirs(RUN, exist_ok=False)                                 # condition 6

payload = dict(
    id='H-NEW-3190', frontier_item='F-18', utc=STAMP, seed=SEED, permutations=N_PERM,
    prereg_sha256=actual, alpha_bonferroni=ALPHA, bonferroni_k=3,
    input_sha256=INPUT_SHA,
    pool=dict(n=len(rows), d_distribution=dict(sorted(Counter(r['d'] for r in rows).items())),
              n_morph_distribution=dict(sorted(Counter(r['n_morph'] for r in rows).items())),
              n_lex_distribution=dict(sorted(Counter(r['n_lex'] for r in rows).items())),
              n_indel_distribution=dict(sorted(Counter(r['n_indel'] for r in rows).items())),
              strata_used=STRATA, strata_dropped_no_variation=DROPPED,
              n_effective=int(sum(1 for r in rows if r['d'] in STRATA))),
    collinearity=dict(
        rho_nlex_nmorph=float(np.corrcoef(n_lex, n_morph)[0, 1]),
        rho_nlex_d=float(np.corrcoef(n_lex, d_arr)[0, 1]),
        rho_nmorph_d=float(np.corrcoef(n_morph, d_arr)[0, 1]),
        rho_nlex_Lmax=float(np.corrcoef(n_lex, Lmax)[0, 1])),
    tie_fractions=tie_report,
    channels=results,
    delta_r2_lengthrule=DELTA_R2_LENGTHRULE,
    I1=I1, I2=I2, I3=I3, i3_all_channels=i3,
    survivors=survivors, verdict=verdict, reverse_direction_flag=reverse,
    mde_80pct_power=mde, untestable_branch=untestable,
    delta_r2_floor=DELTA_R2_FLOOR,
    sensitivities_nonconfirmatory=SENS,
    translator_noise_floor_d0=noise_floor,
)
with open(f'{RUN}/result.json', 'x') as f:
    json.dump(payload, f, indent=2, default=str)
with open(f'{RUN}/pool.json', 'x') as f:
    json.dump(rows, f, indent=1, default=str)
with open(f'{RUN}/prereg-sha256.txt', 'x') as f:
    f.write(actual + '\n')

print('\n' + '=' * 78)
for nm_, g in (('I1', I1), ('I2', I2)):
    print(f'{nm_} {"PASS" if g["PASS"] else "FAIL"}  effect={g["effect"]:+.5f} '
          f'({g["worst_channel_effect"]})  p={g["p"]:.6f} ({g["worst_channel_p"]})  '
          f'dR2={g["delta_r2"]:.5f} ({g["worst_channel_dr2"]})  '
          f'gates dir={g["gate_direction"]} p={g["gate_p"]} floor={g["gate_floor"]} '
          f'lenrule={g["gate_lengthrule"]}')
print(f'I3 {"PASS" if I3["PASS"] else "FAIL"}  worst={I3["channel"]} '
      f'{I3["positive"]}/10 exact p={I3["exact_p"]:.7f}  per-channel={I3["per_channel"]}')
print(f'dR2_lengthrule = {DELTA_R2_LENGTHRULE:.5f} (max-min across L1/L2/L3)   '
      f'floor = {DELTA_R2_FLOOR}')
print(f'rho(n_lex, d) = {float(np.corrcoef(n_lex, d_arr)[0,1]):+.4f}   '
      f'[reported beside every p, per cross-finding-030 mechanism 3]')
print(f'SURVIVORS {survivors}/3  ->  VERDICT {verdict}   reverse_flag={reverse}')
print('S* vs S_max: ' + '  '.join(
    f'{c}: S*={results[c]["delta_r2"]:.5f} S_max={results[c]["S_max_delta_r2"]:.5f} '
    f'{"UNTESTABLE" if untestable[c] else "can-reject"}' for c in CHANNELS))
print(f'\n--- sensitivities (NON-CONFIRMATORY, prereg §7) ---')
for k, v in SENS.items():
    print(f'  {k}: {v}')
print(f'\nrun dir: {RUN}')
