#!/usr/bin/env python3
"""H-NEW-2760 — the muqaṭṭaʿāt book-reference law against a null matched to its
nuisance parameter, with a matched-partition genre control.

The claim under test is H-NEW-53 / cross-finding-008 / Pillar 1 (H-NEW-2680 L1):
24 of 29 muqaṭṭaʿāt-opened surahs reference kitāb/qurʾān in verses 1-3 against
10 of 85 others, hypergeometric p = 3.17e-12.

The defect is H-NEW-740's, not Pillar 4's: the claim HAS a null and the null is
wrong.  A hypergeometric over 114 surahs assumes the 29 are exchangeable with the
other 85.  This project's own H-NEW-46 established (STRONG-PASS, 4/4 length axes)
that they are not — muqaṭṭaʿāt surahs are the long ones, and a substring search
over a longer opening window has more chances to hit.

Nuisance parameters, named in prereg §4 before this file was written:
  N1  opening-window token budget (words in verses 1-3)   <- primary, held fixed
  N2  revelation phase (Nöldeke)                           <- crossed with N1
  N3  the surah's own target-token base rate               <- H5's within-surah null
  N4  whole-surah length                                   <- reported as covariate

Instrument is taken verbatim from scripts/h-new-2680b.py — the same AR_DIAC,
NON_AR, NARROW, normalise_words and cut_to_profile that the pillar-conjunction
control actually ran.  Nothing is re-designed.

Pre-reg SHA-256: a1e4419a674d254d3bf5f243d2891bafcd17986611eff94b31f6e35b8e5b9b3a
Seed 20260509 / replication 20260519.
"""
from __future__ import annotations

import hashlib
import json
import os
import random
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from math import comb

PROJECT = '/Users/grey/Downloads/quran'
REL_PREREG = 'findings/phase-b-hypotheses/prereg-h-new-2760-muqattaat-book-reference-nuisance.md'
EXPECTED_SHA = 'a1e4419a674d254d3bf5f243d2891bafcd17986611eff94b31f6e35b8e5b9b3a'

REL_QJSON = 'quran-text/quran-no-tashkeel.json'
REL_CHRONO = 'data/revelation-order.csv'
REL_BASE = 'data/baseline-corpora/raw'

SEED, SEED_REP = 20260509, 20260519
N_PERM = 10000
K_FAMILY = 6
ALPHA_BON = 0.05 / K_FAMILY          # 0.00833333
RAW_GATE = 0.005 / K_FAMILY          # 0.00083333 — project novelty rule

# The canonical 29 muqaṭṭaʿāt-opened surahs.
MUQ = frozenset({2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31,
                 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68})

# 14-file pre-Islamic poetry corpus — same list as scripts/h-new-2720.py
POETRY_FILES = [
    'diwan-amr-ibn-kulthum.txt', 'diwan-antara.txt', 'diwan-harith.txt',
    'diwan-imru-al-qais.txt', 'diwan-labid.txt', 'diwan-tarafa.txt',
    'diwan-zuhayr.txt', 'muallaqa-amr-bin-kulthum.txt', 'muallaqa-antara.txt',
    'muallaqa-harith.txt', 'muallaqa-imru-al-qais.txt', 'muallaqa-labid.txt',
    'muallaqa-tarafa.txt', 'muallaqa-zuhayr.txt',
]

RUNSTAMP = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
REL_RUNDIR = os.path.join('findings/phase-b-hypotheses/runs/h-new-2760', RUNSTAMP)
RUNDIR = os.path.join(PROJECT, REL_RUNDIR)


def log(*a):
    print(*a, file=sys.stderr, flush=True)


def sha256_file(rel):
    h = hashlib.sha256()
    with open(os.path.join(PROJECT, rel), 'rb') as f:
        for c in iter(lambda: f.read(1 << 20), b''):
            h.update(c)
    return h.hexdigest()


# --------------------------------------------------------------- prereg lock
actual = sha256_file(REL_PREREG)
if actual != EXPECTED_SHA:
    raise SystemExit(f'PRE-REG SHA MISMATCH\n  expected {EXPECTED_SHA}\n  actual   {actual}')
log(f'pre-reg SHA-256 verified: {EXPECTED_SHA}')

# ------------------------------------------------- instrument, verbatim 2680b
# Explicit escapes: a literal Arabic character class is bidi-reordered by some
# editors, which silently widens the diacritic ranges to swallow the alphabet.
AR_DIAC = re.compile('[ؐ-ًؚ-ٰٟۖ-ۭـ]')
NON_AR = re.compile('[^ء-ي\\s]')
NARROW = [re.compile(r'كتب|كتاب|الكتاب|الكتب|كتابك|كتابه|كتابي|كتابنا|كتبنا|كتبه|كتابا'),
          re.compile(r'قرآن|القرآن|قرءان|القرءان|قرآنا|قرانا|اقرأ')]


def normalise_words(text):
    return NON_AR.sub(' ', AR_DIAC.sub('', text)).split()


def hits_target(text):
    return any(p.search(text) for p in NARROW)


# ------------------------------------------------------------------- corpora
quran = json.load(open(os.path.join(PROJECT, REL_QJSON), encoding='utf-8'))
NV = {s['id']: len(s['verses']) for s in quran}
VTEXT = {(s['id'], i + 1): v['text'] for s in quran for i, v in enumerate(s['verses'])}
QUNITS = [v['text'].split() for s in quran for v in s['verses']]
QWLEN = [len(u) for u in QUNITS]
STARTS, _acc = [], 0
for sid in range(1, 115):
    STARTS.append(_acc)
    _acc += NV[sid]
assert len(QUNITS) == 6236 and _acc == 6236


def cut_to_profile(words):
    """Cut a word stream into 6236 units matching the Quranic verse word-length
    profile.  Taken verbatim from scripts/h-new-2680b.py."""
    need = sum(QWLEN)
    if len(words) < need:
        raise SystemExit(f'insufficient words: {len(words)} < {need}')
    units, p = [], 0
    for L in QWLEN:
        units.append(words[p:p + L]); p += L
    return units


def opening_text(sid):
    return ' '.join(VTEXT[(sid, j)] for j in range(1, min(3, NV[sid]) + 1))


def opening_words(sid):
    return sum(len(VTEXT[(sid, j)].split()) for j in range(1, min(3, NV[sid]) + 1))


SIDS = list(range(1, 115))
HIT = {s: hits_target(opening_text(s)) for s in SIDS}
OW = {s: opening_words(s) for s in SIDS}                       # N1
SURAH_WORDS = {s: sum(len(VTEXT[(s, j)].split()) for j in range(1, NV[s] + 1))
               for s in SIDS}                                   # N4

# N2 — Nöldeke phase
PHASE = {}
with open(os.path.join(PROJECT, REL_CHRONO), encoding='utf-8') as f:
    hdr = f.readline().rstrip('\n').split(',')
    im, ip = hdr.index('mushaf_order'), hdr.index('noldeke_phase')
    for line in f:
        parts = line.rstrip('\n').split(',')
        if len(parts) > max(im, ip):
            PHASE[int(parts[im])] = parts[ip].strip()
assert len(PHASE) == 114, f'chronology rows: {len(PHASE)}'


# --------------------------------------------------------------- statistics
def hyper_upper(N, K, n, x):
    if x > min(K, n):
        return 0.0
    return sum(comb(K, i) * comb(N - K, n - i)
               for i in range(max(0, x), min(K, n) + 1)) / comb(N, n)


def spearman(xs, ys):
    def rank(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        r = [0.0] * len(v)
        i = 0
        while i < len(order):
            j = i
            while j + 1 < len(order) and v[order[j + 1]] == v[order[i]]:
                j += 1
            avg = (i + j) / 2.0 + 1.0
            for k in range(i, j + 1):
                r[order[k]] = avg
            i = j + 1
        return r
    rx, ry = rank(xs), rank(ys)
    n = len(xs)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    dx = sum((a - mx) ** 2 for a in rx) ** 0.5
    dy = sum((b - my) ** 2 for b in ry) ** 0.5
    return num / (dx * dy) if dx and dy else 0.0


def quantile(sorted_v, q):
    if not sorted_v:
        return float('nan')
    p = q * (len(sorted_v) - 1)
    lo, hi = int(p), min(int(p) + 1, len(sorted_v) - 1)
    return sorted_v[lo] + (sorted_v[hi] - sorted_v[lo]) * (p - lo)


def bin_by_quantile(values, sids, nbins):
    """Assign each sid to one of nbins strata by rank of values[sid]."""
    order = sorted(sids, key=lambda s: (values[s], s))
    edges = [round(len(order) * i / nbins) for i in range(nbins + 1)]
    lab = {}
    for b in range(nbins):
        for s in order[edges[b]:edges[b + 1]]:
            lab[s] = b
    return lab


def stratified_perm_test(strata, seed, n_perm=N_PERM):
    """Permute the muqaṭṭaʿāt label WITHIN each stratum, so every draw takes
    exactly as many surahs from each stratum as the real set does.  The stratum
    profile is therefore identical by construction."""
    rng = random.Random(seed)
    members = defaultdict(list)
    for s in SIDS:
        members[strata[s]].append(s)
    n_muq_in = {k: sum(1 for s in v if s in MUQ) for k, v in members.items()}
    degenerate = {k: (n_muq_in[k] == 0 or n_muq_in[k] == len(v))
                  for k, v in members.items()}
    observed = sum(1 for s in MUQ if HIT[s])
    draws = []
    for _ in range(n_perm):
        tot = 0
        for k, pool in members.items():
            pick = rng.sample(pool, n_muq_in[k])
            tot += sum(1 for s in pick if HIT[s])
        draws.append(tot)
    draws.sort()
    ge = sum(1 for d in draws if d >= observed)
    mean = sum(draws) / len(draws)
    var = sum((d - mean) ** 2 for d in draws) / len(draws)
    return dict(
        observed=observed,
        null_mean=mean,
        null_sd=var ** 0.5,
        p_greater=(ge + 1) / (n_perm + 1),
        p_less=(sum(1 for d in draws if d <= observed) + 1) / (n_perm + 1),
        band95=[quantile(draws, 0.025), quantile(draws, 0.975)],
        rate_ratio=(observed / mean) if mean > 0 else float('inf'),
        z=((observed - mean) / (var ** 0.5)) if var > 0 else float('inf'),
        n_strata=len(members),
        n_degenerate_strata=sum(degenerate.values()),
        muq_per_stratum={str(k): n_muq_in[k] for k in sorted(members)},
        size_per_stratum={str(k): len(members[k]) for k in sorted(members)},
    )


# ============================================================ H1 reproduction
obs_muq = sum(1 for s in MUQ if HIT[s])
obs_non = sum(1 for s in SIDS if s not in MUQ and HIT[s])
K_TOTAL = obs_muq + obs_non
H1 = dict(
    observed_muq_hits=obs_muq, n_muq=29,
    observed_non_hits=obs_non, n_non=85,
    K_total=K_TOTAL,
    published_muq='24/29', published_non='10/85', published_K=34,
    reproduces_muq_exactly=(obs_muq == 24),
    non_matches_published=(obs_non == 10),
    muq_hit_surahs=sorted(s for s in MUQ if HIT[s]),
    muq_miss_surahs=sorted(s for s in MUQ if not HIT[s]),
    non_hit_surahs=sorted(s for s in SIDS if s not in MUQ and HIT[s]),
)

# ------------------------------------------- Null A, the published one, audited
NULL_A = dict(
    kind='uniform hypergeometric over 114 exchangeable surahs',
    p_rebuilt_K35=hyper_upper(114, K_TOTAL, 29, obs_muq),
    p_published_K34=hyper_upper(114, 34, 29, 24),
    expected_hits=K_TOTAL * 29 / 114,
    note='the null under audit; reproduced for comparison only',
)

# ================================================== H2 the nuisance is real
xs = [OW[s] for s in SIDS]
ys = [1.0 if HIT[s] else 0.0 for s in SIDS]
rho_ow = spearman(xs, ys)


def perm_rho_p(vals, labels, seed, locked_positive=True, n_perm=N_PERM):
    rng = random.Random(seed)
    obs = spearman(vals, labels)
    lab = list(labels)
    cnt = 0
    for _ in range(n_perm):
        rng.shuffle(lab)
        r = spearman(vals, lab)
        if (r >= obs) if locked_positive else (r <= obs):
            cnt += 1
    return obs, (cnt + 1) / (n_perm + 1)


_, p_rho_ow = perm_rho_p(xs, ys, SEED)
H2 = dict(rho_openwin_hit=rho_ow, p_greater=p_rho_ow,
          rho_surahlen_hit=spearman([SURAH_WORDS[s] for s in SIDS], ys),
          median_ow_muq=sorted(OW[s] for s in MUQ)[14],
          median_ow_non=sorted(OW[s] for s in SIDS if s not in MUQ)[42],
          passes=(rho_ow > 0 and p_rho_ow < RAW_GATE),
          direction_ok=(rho_ow > 0))

# ============================================ H3 primary — N1-matched Null B
STRATA_B = bin_by_quantile(OW, SIDS, 5)
H3 = stratified_perm_test(STRATA_B, SEED)
H3_REP = stratified_perm_test(STRATA_B, SEED_REP)
H3['passes'] = (H3['observed'] > H3['null_mean'] and H3['p_greater'] < RAW_GATE)
H3['direction_ok'] = H3['observed'] > H3['null_mean']
H3['outside_95_band'] = H3['observed'] > H3['band95'][1]

# ======================================== H4 — N1 x N2-matched Null C
PHASES = sorted(set(PHASE.values()))
OW_TERT = bin_by_quantile(OW, SIDS, 3)
STRATA_C = {s: (OW_TERT[s], PHASE[s]) for s in SIDS}
H4 = stratified_perm_test(STRATA_C, SEED)
H4_REP = stratified_perm_test(STRATA_C, SEED_REP)
H4['passes'] = (H4['observed'] > H4['null_mean'] and H4['p_greater'] < RAW_GATE)
H4['direction_ok'] = H4['observed'] > H4['null_mean']
H4['phases_present'] = PHASES

# ================================= H5 — front-loading, length-free (Null D)
def first_target_position(sid):
    """Normalised position (1-based verse index / n_verses) of the first verse
    containing a target token, or None if the surah has no target token."""
    for j in range(1, NV[sid] + 1):
        if hits_target(VTEXT[(sid, j)]):
            return j / NV[sid], j
    return None, None


POS = {}
for s in SIDS:
    frac, idx = first_target_position(s)
    if frac is not None:
        POS[s] = (frac, idx)

muq_pos = [POS[s][0] for s in MUQ if s in POS]
non_pos = [POS[s][0] for s in SIDS if s not in MUQ and s in POS]
obs_delta = (sum(muq_pos) / len(muq_pos)) - (sum(non_pos) / len(non_pos))

# Null D: within each surah holding >=1 target verse, place that surah's target
# verses uniformly at random among its own verses, keeping their count fixed.
def null_d(seed, n_perm=N_PERM):
    rng = random.Random(seed)
    cnts = {}
    for s in POS:
        cnts[s] = sum(1 for j in range(1, NV[s] + 1) if hits_target(VTEXT[(s, j)]))
    worse = 0
    draws = []
    for _ in range(n_perm):
        mp, npos = [], []
        for s in POS:
            picks = rng.sample(range(1, NV[s] + 1), min(cnts[s], NV[s]))
            frac = min(picks) / NV[s]
            (mp if s in MUQ else npos).append(frac)
        d = (sum(mp) / len(mp)) - (sum(npos) / len(npos))
        draws.append(d)
        if d <= obs_delta:
            worse += 1
    draws.sort()
    mean = sum(draws) / len(draws)
    return dict(p_less=(worse + 1) / (n_perm + 1), null_mean=mean,
                band95=[quantile(draws, 0.025), quantile(draws, 0.975)])


ND = null_d(SEED)
ND_REP = null_d(SEED_REP)
H5 = dict(
    n_muq_with_target=len(muq_pos), n_non_with_target=len(non_pos),
    mean_first_pos_muq=sum(muq_pos) / len(muq_pos),
    mean_first_pos_non=sum(non_pos) / len(non_pos),
    delta=obs_delta,
    null_mean=ND['null_mean'], band95=ND['band95'],
    p_less=ND['p_less'],
    direction_ok=(obs_delta < 0),
    passes=(obs_delta < 0 and ND['p_less'] < RAW_GATE),
)

# ================================ G1 — matched-partition genre control
def load_words(rel_files):
    ws = []
    for rf in rel_files:
        with open(os.path.join(PROJECT, REL_BASE, rf), encoding='utf-8', errors='ignore') as f:
            ws.extend(normalise_words(f.read()))
    return ws


def baseline_arm(label, rel_files):
    words = load_words(rel_files)
    units = cut_to_profile(words)
    ow, hit = [], []
    n_hit = 0
    for sid in range(1, 115):
        st = STARTS[sid - 1]
        k = min(3, NV[sid])
        window = [w for j in range(k) for w in units[st + j]]
        txt = ' '.join(window)
        h = hits_target(txt)
        ow.append(len(window)); hit.append(1.0 if h else 0.0)
        n_hit += int(h)
    rho, p = perm_rho_p(ow, hit, SEED, locked_positive=True)
    return dict(label=label, n_words=len(words), n_pseudosurah_hits=n_hit,
                rho_openwin_hit=rho, p_greater=p,
                direction_ok=(rho > 0), passes=(rho > 0 and p < RAW_GATE))


G1 = dict(
    quran=dict(label='this corpus (same instrument)', n_pseudosurah_hits=K_TOTAL,
               rho_openwin_hit=rho_ow, p_greater=p_rho_ow),
    bukhari=baseline_arm('al-Bukhārī', ['bukhari.txt']),
    jahiz=baseline_arm('al-Jāḥiẓ Kitāb al-Ḥayawān', ['jahiz-hayawan.txt']),
    poetry=baseline_arm('pre-Islamic poetry (14 files)', POETRY_FILES),
)
G1['baselines_positive'] = sum(1 for k in ('bukhari', 'jahiz', 'poetry')
                               if G1[k]['direction_ok'])
G1['baselines_passing_gate'] = sum(1 for k in ('bukhari', 'jahiz', 'poetry')
                                   if G1[k]['passes'])

# ===================================================== verdict — prereg §8
# Diffed line-by-line against prereg §8 before this block was written.
if not H1['reproduces_muq_exactly']:
    VERDICT = 'REBUILD-FAILED'
elif not H3['passes']:
    VERDICT = 'DOES-NOT-DISCRIMINATE'
elif H3['rate_ratio'] < 2.0 or not H5['passes']:
    VERDICT = 'GENRE-SHARED-BUT-LARGER'
elif H3['outside_95_band']:
    VERDICT = 'DISCRIMINATES'
else:
    VERDICT = 'GENRE-SHARED-BUT-LARGER'

PRECOMMIT_VIOLATIONS = [
    name for name, arm in (('H2', H2), ('H3', H3), ('H4', H4), ('H5', H5))
    if not arm['direction_ok']
] + [f'G1:{k}' for k in ('bukhari', 'jahiz', 'poetry') if not G1[k]['direction_ok']]

RESULT = dict(
    id='H-NEW-2760',
    prereg_sha256=EXPECTED_SHA,
    seed=SEED, seed_replication=SEED_REP, n_perm=N_PERM,
    bonferroni_k=K_FAMILY, alpha_bonferroni=ALPHA_BON, raw_gate=RAW_GATE,
    target_claim='H-NEW-53 / cross-finding-008 / Pillar 1 (H-NEW-2680 L1)',
    defect='null does not match the nuisance parameter (H-NEW-740 shape)',
    nuisance_primary='N1 opening-window token budget (words in verses 1-3)',
    H1=H1, NULL_A=NULL_A, H2=H2,
    H3=H3, H3_replication=H3_REP,
    H4=H4, H4_replication=H4_REP,
    H5=H5, H5_replication=ND_REP,
    G1=G1,
    verdict=VERDICT,
    precommit_violations=PRECOMMIT_VIOLATIONS,
)

os.makedirs(RUNDIR, exist_ok=False)
with open(os.path.join(RUNDIR, 'result.json'), 'w', encoding='utf-8') as f:
    json.dump(RESULT, f, ensure_ascii=False, indent=2, sort_keys=True)

MANIFEST = dict(
    id='H-NEW-2760',
    utc=RUNSTAMP,
    command='python3 findings/phase-b-hypotheses/scripts/h-new-2760.py',
    prereg=dict(path=REL_PREREG, sha256=EXPECTED_SHA),
    script=dict(path='findings/phase-b-hypotheses/scripts/h-new-2760.py',
                sha256=sha256_file('findings/phase-b-hypotheses/scripts/h-new-2760.py')),
    frozen_inputs=[
        dict(path=REL_QJSON, sha256=sha256_file(REL_QJSON)),
        dict(path=REL_CHRONO, sha256=sha256_file(REL_CHRONO)),
        dict(path=os.path.join(REL_BASE, 'bukhari.txt'),
             sha256=sha256_file(os.path.join(REL_BASE, 'bukhari.txt'))),
        dict(path=os.path.join(REL_BASE, 'jahiz-hayawan.txt'),
             sha256=sha256_file(os.path.join(REL_BASE, 'jahiz-hayawan.txt'))),
    ] + [dict(path=os.path.join(REL_BASE, f), sha256=sha256_file(os.path.join(REL_BASE, f)))
         for f in POETRY_FILES],
    instrument_source='findings/phase-b-hypotheses/scripts/h-new-2680b.py',
    run_dir=REL_RUNDIR,
    seeds=[SEED, SEED_REP],
    verdict=VERDICT,
)
with open(os.path.join(RUNDIR, 'manifest.json'), 'w', encoding='utf-8') as f:
    json.dump(MANIFEST, f, ensure_ascii=False, indent=2, sort_keys=True)

with open(os.path.join(PROJECT, 'findings/phase-b-hypotheses/csv/h-new-2760.json'),
          'w', encoding='utf-8') as f:
    json.dump(RESULT, f, ensure_ascii=False, indent=2, sort_keys=True)

log(f'run dir: {REL_RUNDIR}')
print(json.dumps(RESULT, ensure_ascii=False, indent=2, sort_keys=True))
