#!/usr/bin/env python3
"""H-NEW-2800 — the legal-formula frames: a closed inventory with positional structure.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2800-legal-formulae.md
Pre-reg SHA-256: 4eabc04e7977d9c932d38fed7094efb20d10e5c8daf828eef240044ffe3989bb

Seeds 20260509 (primary) / 20260519 (replication). 10000 permutations.
Bonferroni k = 5 over {H2, H3, H4, H5, H6}; alpha = 0.010.

Stdlib only (INVESTIGATION-PROTOCOL 7.1 — no deviation declared, none taken).
All frame matching is on QAC v0.4 morphological FEATURE FIELDS, never on raw substrings.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import random
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone

PROJECT = '/Users/grey/Downloads/quran'
PREREG = os.path.join(PROJECT, 'findings/phase-b-hypotheses/prereg-h-new-2800-legal-formulae.md')
EXPECTED_SHA = '4eabc04e7977d9c932d38fed7094efb20d10e5c8daf828eef240044ffe3989bb'

QAC = os.path.join(PROJECT, 'data/morphology/quranic-corpus-morphology-0.4.txt')
QJSON = os.path.join(PROJECT, 'quran-text/quran-no-tashkeel.json')
J2530 = os.path.join(PROJECT, 'findings/phase-b-hypotheses/csv/h-new-2530.json')
J2500 = os.path.join(PROJECT, 'findings/phase-b-hypotheses/csv/h-new-2500.json')
BUKHARI = os.path.join(PROJECT, 'data/baseline-corpora/raw/bukhari-noquran.txt')
REVORDER = os.path.join(PROJECT, 'data/revelation-order.csv')
ITQAN = os.path.join(PROJECT, 'data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt')

FROZEN = [QAC, QJSON, J2530, J2500, BUKHARI, REVORDER, ITQAN]

SEED_PRIMARY, SEED_REPLICATION = 20260509, 20260519
N_PERM = 10000
BONF_K = 5
ALPHA = 0.05 / BONF_K
N_OFFSETS = 200
TOP_K = 8
K_CURVE = [1, 2, 4, 8, 16, 32]

RUNSTAMP = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
RUNDIR = os.path.join(PROJECT, 'findings/phase-b-hypotheses/runs/h-new-2800', RUNSTAMP)


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
        raise SystemExit(
            f'FAIL pre-reg SHA mismatch\n  expected={EXPECTED_SHA}\n  actual  ={actual}')
    log(f'pre-reg SHA-256 verified: {actual}')


# =============================================================================
# statistics helpers (explicit, stdlib)
# =============================================================================
def rankdata(x):
    n = len(x)
    order = sorted(range(n), key=lambda i: x[i])
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and x[order[j + 1]] == x[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


def pearson(a, b):
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    num = sum((a[i] - ma) * (b[i] - mb) for i in range(n))
    da = math.sqrt(sum((v - ma) ** 2 for v in a))
    db = math.sqrt(sum((v - mb) ** 2 for v in b))
    return num / (da * db) if da > 0 and db > 0 else 0.0


def spearman(a, b):
    return pearson(rankdata(a), rankdata(b))


def perm_p_upper(obs, nulls):
    """One-sided upper-tail permutation p-value."""
    return (1 + sum(1 for v in nulls if v >= obs)) / (1 + len(nulls))


def perm_p_lower(obs, nulls):
    return (1 + sum(1 for v in nulls if v <= obs)) / (1 + len(nulls))


def mean(xs):
    return sum(xs) / len(xs) if xs else float('nan')


def quintiles(values, n_bins=5):
    """Assign each index to a bin by rank; bins as equal in size as possible."""
    n = len(values)
    order = sorted(range(n), key=lambda i: values[i])
    binof = [0] * n
    for pos, i in enumerate(order):
        binof[i] = min(n_bins - 1, pos * n_bins // n)
    return binof


# =============================================================================
# QAC loading — word-level segment model
# =============================================================================
def load_qac():
    """words[(s,v)] = list over word index (1-based, index 0 unused) of list-of-field-sets."""
    words = defaultdict(dict)
    forms = defaultdict(dict)
    with open(QAC, encoding='utf-8') as f:
        for line in f:
            if not line.startswith('('):
                continue
            parts = line.rstrip('\n').split('\t')
            if len(parts) != 4:
                continue
            s, v, w, _g = (int(x) for x in parts[0].strip('()').split(':'))
            fields = frozenset(parts[3].split('|'))
            words[(s, v)].setdefault(w, []).append(fields)
            forms[(s, v)].setdefault(w, []).append(parts[1])
    out, out_forms = {}, {}
    for key, wd in words.items():
        n = max(wd)
        out[key] = [wd.get(i, []) for i in range(1, n + 1)]
        out_forms[key] = [' '.join(forms[key].get(i, [])) for i in range(1, n + 1)]
    return out, out_forms


CONJ_PREFIXES = {'w:CONJ+', 'w:REM+', 'f:CONJ+', 'f:REM+', 'f:RSLT+',
                 'f:CAUS+', 'f:SUP+', 'w:CIRC+', 'w:SUP+'}
P2_SUFFIX = {'PRON:2MP', 'PRON:2MS', 'PRON:2FS', 'PRON:2FP', 'PRON:2MD', 'PRON:2FD'}
P2_STEM = {'2MP', '2MS', '2FS', '2FP', '2MD', '2FD'}


def seg_all(word, terms):
    """True if ANY single segment of the word carries ALL the given exact fields."""
    return any(all(t in fs for t in terms) for fs in word)


def is_2p(word):
    for fs in word:
        if fs & P2_SUFFIX:
            return True
        if 'POS:PRON' in fs and (fs & P2_STEM):
            return True
    return False


def has_prep_ala(word):
    return seg_all(word, ['POS:P', 'LEM:EalaY`'])


def has_prep_li(word):
    return any('l:P+' in fs for fs in word) or seg_all(word, ['POS:P', 'LEM:li'])


def head_is_bare(word, terms):
    """Strict no-strip variant: the FIRST segment of the word satisfies the head predicate."""
    return bool(word) and all(t in word[0] for t in terms)


# --- locked frame predicates (pre-reg §5) ------------------------------------
def m_A1(ws, i):
    return (seg_all(ws[i], ['POS:V', 'PERF', 'PASS', 'ROOT:ktb'])
            and i + 1 < len(ws) and has_prep_ala(ws[i + 1]) and is_2p(ws[i + 1]))


def m_A2(ws, i):
    return (seg_all(ws[i], ['POS:V', 'PERF', 'PASS', 'ROOT:Hrm'])
            and i + 1 < len(ws) and has_prep_ala(ws[i + 1]) and is_2p(ws[i + 1]))


def m_A3(ws, i):
    return (seg_all(ws[i], ['POS:V', 'PERF', 'PASS', 'ROOT:Hll'])
            and i + 1 < len(ws) and has_prep_li(ws[i + 1]) and is_2p(ws[i + 1]))


def m_B1(ws, i):
    return (seg_all(ws[i], ['POS:COND', 'LEM:man'])
            and i + 2 < len(ws)
            and seg_all(ws[i + 1], ['POS:NEG', 'LEM:lam'])
            and seg_all(ws[i + 2], ['POS:V', 'IMPF', 'ROOT:wjd']))


def m_B2(ws, i):
    return (seg_all(ws[i], ['LEM:>ay~uhaA'])
            and i + 2 < len(ws)
            and seg_all(ws[i + 1], ['POS:REL', 'LEM:{l~a*iY'])
            and seg_all(ws[i + 2], ['POS:V', 'PERF', 'ROOT:Amn']))


def m_B3(ws, i):
    if not (any('w:' in x for fs in ws[i] for x in fs) and has_prep_li(ws[i]) and is_2p(ws[i])):
        return False
    if i + 1 >= len(ws) or not seg_all(ws[i + 1], ['POS:P', 'LEM:fiY']):
        return False
    return any(seg_all(ws[j], ['POS:N', 'ROOT:Hyy'])
               for j in range(i + 2, min(i + 5, len(ws))))


def m_G1(ws, i):
    return (seg_all(ws[i], ['POS:V', 'PERF', 'PASS'])
            and i + 1 < len(ws)
            and (has_prep_ala(ws[i + 1]) or has_prep_li(ws[i + 1]))
            and is_2p(ws[i + 1]))


def m_G2(ws, i):
    return (seg_all(ws[i], ['LEM:>ay~uhaA'])
            and i + 1 < len(ws)
            and (seg_all(ws[i + 1], ['POS:REL']) or seg_all(ws[i + 1], ['POS:N'])))


def m_G3(ws, i):
    return seg_all(ws[i], ['POS:COND'])


FRAMES = [
    ('A1', 'kutiba ʿalaykum', 'A', m_A1),
    ('A2', 'ḥurrimat ʿalaykum', 'A', m_A2),
    ('A3', 'uḥilla lakum', 'A', m_A3),
    ('B1', 'fa-man lam yajid', 'B', m_B1),
    ('B2', 'yā ayyuhā alladhīna āmanū', 'B', m_B2),
    ('B3', 'wa-lakum fī … ḥayāt', 'B', m_B3),
    ('G1', '[PASS PERF] + prep + 2P (ikhbār template)', 'G', m_G1),
    ('G2', 'ayyuhā + REL/N (vocative address)', 'G', m_G2),
    ('G3', 'COND (conditional protasis)', 'G', m_G3),
]
PURGE = {'A1', 'B2'}          # the two markers that DEFINE the legal_medinan label


# =============================================================================
# census
# =============================================================================
def run_census(qacwords, verses):
    """occ[fid] = list of dicts {s, v, w, onset(bool), onset_strict(bool)}."""
    occ = {fid: [] for fid, _, _, _ in FRAMES}
    for (s, v) in verses:
        ws = qacwords[(s, v)]
        for fid, _name, _cls, fn in FRAMES:
            for i in range(len(ws)):
                if fn(ws, i):
                    occ[fid].append({
                        's': s, 'v': v, 'w': i + 1,
                        'onset': i == 0,
                        'onset_strict': i == 0 and not (ws[0] and (ws[0][0] & CONJ_PREFIXES)),
                    })
    return occ


# =============================================================================
# onset-bigram concentration (frame-list-free genre statistic)
# =============================================================================
AR_DIAC = re.compile('[ؐ-ًؚ-ٰٟۖ-ۭـ]')
NON_AR = re.compile('[^ء-ي\\s]')


def normalise_words(text):
    return NON_AR.sub(' ', AR_DIAC.sub('', text)).split()


def conj_strip(word):
    """Identical orthographic conjunction strip applied to EVERY corpus."""
    if len(word) >= 3 and word[0] in ('و', 'ف'):
        return word[1:]
    return word


def onset_bigram(unit, strip=True):
    if len(unit) < 2:
        return None
    a = conj_strip(unit[0]) if strip else unit[0]
    return (a, unit[1])


def topk_concentration(units, k=TOP_K, strip=True):
    bgs = [onset_bigram(u, strip) for u in units]
    bgs = [b for b in bgs if b is not None]
    if not bgs:
        return 0.0, 0, []
    c = Counter(bgs)
    top = c.most_common(k)
    return sum(n for _, n in top) / len(bgs), len(bgs), top


def onset_trigram(unit):
    if len(unit) < 3:
        return None
    return (conj_strip(unit[0]), unit[1], unit[2])


def topk_concentration_tri(units, k=TOP_K):
    tgs = [onset_trigram(u) for u in units]
    tgs = [t for t in tgs if t is not None]
    if not tgs:
        return 0.0, 0
    c = Counter(tgs)
    return sum(n for _, n in c.most_common(k)) / len(tgs), len(tgs)


# --- H-NEW-2680 build_pseudo_corpus, reused verbatim (offset added for the grid) ---
def build_pseudo_corpus(words, qverse_wlen, offset=0):
    """Cut a word stream into 6236 units matching the Quran verse word-length profile."""
    need = sum(qverse_wlen)
    if len(words) - offset < need:
        return None, f'insufficient words: have {len(words) - offset}, need {need}'
    units, p = [], offset
    for L in qverse_wlen:
        units.append(words[p:p + L])
        p += L
    return units, None


ISNAD_OPENERS = {'حدثنا',   # haddathana
                 'حدثني',   # haddathani
                 'أخبرنا',  # akhbarana
                 'أخبرني'}  # akhbarani


def split_real_boundaries(words, min_len=3):
    """Units = spans that BEGIN at an isnad opener, with the opener token DROPPED."""
    idx = [i for i, w in enumerate(words) if w in ISNAD_OPENERS]
    units = []
    for a, b in zip(idx, idx[1:] + [len(words)]):
        u = words[a + 1:b]
        if len(u) >= min_len:
            units.append(u)
    return units


# =============================================================================
# main
# =============================================================================
def main():
    verify_prereg()
    os.makedirs(RUNDIR, exist_ok=True)

    # ---------------- corpus -------------------------------------------------
    qjson = json.load(open(QJSON, encoding='utf-8'))
    NV, VTEXT, VERSES = {}, {}, []
    for su in qjson:
        sid = su['id']
        NV[sid] = len(su['verses'])
        for vv in su['verses']:
            VERSES.append((sid, vv['id']))
            VTEXT[(sid, vv['id'])] = vv['text']
    assert len(VERSES) == 6236, len(VERSES)

    qacwords, _qacforms = load_qac()
    missing = [k for k in VERSES if k not in qacwords]
    if missing:
        raise SystemExit(f'FAIL QAC/JSON verse mismatch: {len(missing)} missing, e.g. {missing[:5]}')
    log(f'corpus: 114 surahs, {len(VERSES)} verses, QAC aligned')

    # ---------------- register labels, via 2530's own pointer ----------------
    j2530 = json.load(open(J2530, encoding='utf-8'))
    pointer = j2530['genre_proxy_source']
    j2500 = json.load(open(J2500, encoding='utf-8'))
    gp = j2500['genre_proxy']
    surah_genre = {int(k): v for k, v in gp['surah_genre'].items()}
    assert len(surah_genre) == 114
    decision_procedure = gp['decision_procedure']
    legal_markers = gp['legal_markers']
    LEGAL = sorted([s for s in range(1, 115) if surah_genre[s] == 'legal_medinan'])
    log(f'register labels via "{pointer}"; legal_medinan = {LEGAL}')

    # ---------------- census -------------------------------------------------
    occ = run_census(qacwords, VERSES)
    census = {}
    for fid, name, cls, _fn in FRAMES:
        o = occ[fid]
        census[fid] = {
            'name': name, 'class': cls,
            'n_total': len(o),
            'n_onset': sum(1 for x in o if x['onset']),
            'n_onset_strict': sum(1 for x in o if x['onset_strict']),
            'n_verses': len({(x['s'], x['v']) for x in o}),
            'n_surahs': len({x['s'] for x in o}),
            'locations': [f"{x['s']}:{x['v']}:{x['w']}" for x in o],
            'by_register': dict(Counter(surah_genre[x['s']] for x in o)),
            'onset_by_register': dict(Counter(surah_genre[x['s']] for x in o if x['onset'])),
        }
        log(f"  {fid} {name}: total={len(o)} onset={census[fid]['n_onset']} "
            f"verses={census[fid]['n_verses']} surahs={census[fid]['n_surahs']}")

    # ---------------- unit-drift declaration (UNIT-DRIFT-DEFECT §5) ----------
    sur_nv = [NV[s] for s in range(1, 115)]
    sur_words = {s: sum(len(VTEXT[(s, v)].split()) for v in range(1, NV[s] + 1))
                 for s in range(1, 115)}
    sur_mvl = [sur_words[s] / NV[s] for s in range(1, 115)]
    legal_ind = [1.0 if surah_genre[s] == 'legal_medinan' else 0.0 for s in range(1, 115)]
    reg_mvl, reg_nv, reg_words = {}, {}, {}
    for r in ['narrative', 'legal_medinan', 'eschatological_mufassal', 'liturgical_didactic']:
        ss = [s for s in range(1, 115) if surah_genre[s] == r]
        tw = sum(sur_words[s] for s in ss)
        tv = sum(NV[s] for s in ss)
        reg_mvl[r] = tw / tv
        reg_nv[r] = tv
        reg_words[r] = tw
    unit_drift = {
        'denominator_is': 'number of verse ONSETS = number of verses; one onset per verse '
                          'regardless of verse word-length',
        'mean_verse_length_by_register': reg_mvl,
        'verses_by_register': reg_nv,
        'words_by_register': reg_words,
        'rho_surah_verse_count_vs_legal_indicator': spearman(sur_nv, legal_ind),
        'rho_surah_mean_verse_length_vs_legal_indicator': spearman(sur_mvl, legal_ind),
        'rho_surah_verse_count_vs_mean_verse_length': spearman(sur_nv, sur_mvl),
    }
    log(f"unit-drift: rho(nv, legal) = {unit_drift['rho_surah_verse_count_vs_legal_indicator']:.4f}, "
        f"rho(mvl, legal) = {unit_drift['rho_surah_mean_verse_length_vs_legal_indicator']:.4f}")

    # ---------------- H1 closure --------------------------------------------
    def onset_verse_set(fids, restrict=None):
        out = set()
        for fid in fids:
            for x in occ[fid]:
                if x['onset'] and (restrict is None or x['s'] in restrict):
                    out.add((x['s'], x['v']))
        return out

    ALL_AB = [f[0] for f in FRAMES if f[2] in ('A', 'B')]
    CLASS_A = [f[0] for f in FRAMES if f[2] == 'A']
    CLASS_B = [f[0] for f in FRAMES if f[2] == 'B']
    CLASS_G = [f[0] for f in FRAMES if f[2] == 'G']
    PURGED = [f for f in ALL_AB if f not in PURGE]

    legal_set = set(LEGAL)
    n_legal_verses = sum(NV[s] for s in LEGAL)

    def closure(fids, restrict, n_den):
        return len(onset_verse_set(fids, restrict)) / n_den if n_den else float('nan')

    h1 = {
        'n_legal_verses': n_legal_verses,
        'closure_full_AB': closure(ALL_AB, legal_set, n_legal_verses),
        'closure_purged': closure(PURGED, legal_set, n_legal_verses),
        'closure_classA': closure(CLASS_A, legal_set, n_legal_verses),
        'closure_classB': closure(CLASS_B, legal_set, n_legal_verses),
        'closure_classG': closure(CLASS_G, legal_set, n_legal_verses),
        'closure_ABG': closure(ALL_AB + CLASS_G, legal_set, n_legal_verses),
        'by_register': {},
        'corpus_wide_AB_onset_verses': len(onset_verse_set(ALL_AB)),
        'corpus_wide_AB_onset_fraction': len(onset_verse_set(ALL_AB)) / 6236,
        'ghazali_500_as_fraction_of_6236': 500 / 6236,
        'rival_150_as_fraction_of_6236': 150 / 6236,
    }
    for r in reg_mvl:
        ss = {s for s in range(1, 115) if surah_genre[s] == r}
        h1['by_register'][r] = {
            'n_verses': reg_nv[r],
            'closure_full_AB': closure(ALL_AB, ss, reg_nv[r]),
            'closure_purged': closure(PURGED, ss, reg_nv[r]),
            'closure_classG': closure(CLASS_G, ss, reg_nv[r]),
        }
    h1['label'] = ('CLOSURE-SUPPORTED' if h1['closure_purged'] >= 0.50 else
                   'CLOSURE-PARTIAL' if h1['closure_purged'] >= 0.20 else 'CLOSURE-FALSE')
    h1['label_full_inventory'] = ('CLOSURE-SUPPORTED' if h1['closure_full_AB'] >= 0.50 else
                                  'CLOSURE-PARTIAL' if h1['closure_full_AB'] >= 0.20 else
                                  'CLOSURE-FALSE')
    log(f"H1 closure purged = {h1['closure_purged']:.5f} ({h1['label']}); "
        f"full = {h1['closure_full_AB']:.5f}")

    # per-1000-word rates (the ratio-normalisation the defect rule asks for)
    rates = {}
    for fid, name, cls, _fn in FRAMES:
        per_reg = {}
        for r in reg_mvl:
            n = census[fid]['by_register'].get(r, 0)
            per_reg[r] = {
                'per_1000_words': 1000.0 * n / reg_words[r],
                'per_100_verses': 100.0 * n / reg_nv[r],
            }
        rates[fid] = per_reg

    # ---------------- H2 enrichment (stratified label permutation) ----------
    def enrichment(fids, strat_values, seed):
        onset_by_surah = defaultdict(int)
        for (s, v) in onset_verse_set(fids):
            onset_by_surah[s] += 1
        labels = [surah_genre[s] for s in range(1, 115)]
        binof = quintiles(strat_values)
        obs = sum(onset_by_surah[s] for s in LEGAL)
        rng = random.Random(seed)
        idx_by_bin = defaultdict(list)
        for i in range(114):
            idx_by_bin[binof[i]].append(i)
        nulls = []
        for _ in range(N_PERM):
            perm = [None] * 114
            for b, idxs in idx_by_bin.items():
                lab = [labels[i] for i in idxs]
                rng.shuffle(lab)
                for i, L in zip(idxs, lab):
                    perm[i] = L
            nulls.append(sum(onset_by_surah[i + 1] for i in range(114)
                             if perm[i] == 'legal_medinan'))
        return {
            'observed': obs,
            'null_mean': mean(nulls),
            'null_sd': math.sqrt(mean([(x - mean(nulls)) ** 2 for x in nulls])),
            'null_p95': sorted(nulls)[int(0.95 * len(nulls))],
            'rate_ratio': obs / mean(nulls) if mean(nulls) > 0 else float('inf'),
            'p': perm_p_upper(obs, nulls),
        }

    h2_purged = enrichment(PURGED, sur_nv, SEED_PRIMARY)
    h2_full = enrichment(ALL_AB, sur_nv, SEED_PRIMARY)
    h2_purged_mvl = enrichment(PURGED, sur_mvl, SEED_PRIMARY)
    h2_pass = (h2_purged['p'] <= ALPHA and h2_purged['observed'] > h2_purged['null_mean'])
    log(f"H2 purged: obs={h2_purged['observed']} null={h2_purged['null_mean']:.3f} "
        f"p={h2_purged['p']:.5f} -> {'PASS' if h2_pass else 'FAIL'}")

    # ---------------- H3 / H4 positional ------------------------------------
    # observed sample: (surah, verse, frame_type) over A u B, corpus-wide
    per_surah_type = defaultdict(lambda: defaultdict(set))
    for fid in ALL_AB:
        for x in occ[fid]:
            per_surah_type[x['s']][fid].add(x['v'])

    def rel(i, n):
        return (i - 0.5) / n

    obs_rels = []
    for s, d in per_surah_type.items():
        for fid, vs in d.items():
            for v in vs:
                obs_rels.append(rel(v, NV[s]))
    h3_obs = mean(obs_rels)

    def h3_null(seed):
        rng = random.Random(seed)
        out = []
        plan = [(s, NV[s], len(vs)) for s, d in per_surah_type.items() for vs in d.values()]
        for _ in range(N_PERM):
            tot, cnt = 0.0, 0
            for s, n, c in plan:
                for v in rng.sample(range(1, n + 1), c):
                    tot += rel(v, n)
                    cnt += 1
            out.append(tot / cnt)
        return out

    h3_nulls = h3_null(SEED_PRIMARY)
    h3_p_upper = perm_p_upper(h3_obs, h3_nulls)
    h3_p_lower = perm_p_lower(h3_obs, h3_nulls)
    h3_pass = (h3_obs > 0.5 and h3_p_upper <= ALPHA)
    h3_precommit_violation = (h3_obs < 0.5 and h3_p_lower <= ALPHA)
    log(f'H3 obs mean rel = {h3_obs:.5f} null = {mean(h3_nulls):.5f} '
        f'p_upper={h3_p_upper:.5f} -> {"PASS" if h3_pass else "FAIL"}'
        + ('  [PRE-COMMIT VIOLATION: significant in the REVERSE direction]'
           if h3_precommit_violation else ''))

    # H4 clustering on distinct frame-bearing verses per surah
    per_surah_distinct = {s: sorted({v for vs in d.values() for v in vs})
                          for s, d in per_surah_type.items()}
    h4_surahs = [(s, NV[s], len(vs)) for s, vs in per_surah_distinct.items() if len(vs) >= 2]

    def gaps_stat(sets):
        g = []
        for s, n, vs in sets:
            for a, b in zip(vs, vs[1:]):
                g.append((b - a) / n)
        return mean(g), len(g)

    h4_obs, h4_npairs = gaps_stat([(s, NV[s], per_surah_distinct[s]) for s, _n, _c in h4_surahs])

    def h4_null(seed):
        rng = random.Random(seed)
        out = []
        for _ in range(N_PERM):
            g, cnt = 0.0, 0
            for s, n, c in h4_surahs:
                vs = sorted(rng.sample(range(1, n + 1), c))
                for a, b in zip(vs, vs[1:]):
                    g += (b - a) / n
                    cnt += 1
            out.append(g / cnt)
        return out

    h4_nulls = h4_null(SEED_PRIMARY)
    h4_p = perm_p_lower(h4_obs, h4_nulls)
    h4_pass = (h4_obs < mean(h4_nulls) and h4_p <= ALPHA)
    log(f'H4 obs mean gap = {h4_obs:.5f} null = {mean(h4_nulls):.5f} '
        f'p={h4_p:.5f} -> {"PASS" if h4_pass else "FAIL"}')

    # scale-freeness check: E[rel] under the null must be 0.5 for every n
    h3_null_mean = mean(h3_nulls)

    # H3/H4 robustness arms
    def h3_arm(fids, restrict=None, onset_only=False, seed=SEED_PRIMARY):
        pst = defaultdict(lambda: defaultdict(set))
        for fid in fids:
            for x in occ[fid]:
                if onset_only and not x['onset']:
                    continue
                if restrict is not None and x['s'] not in restrict:
                    continue
                pst[x['s']][fid].add(x['v'])
        rl = [rel(v, NV[s]) for s, d in pst.items() for vs in d.values() for v in vs]
        if not rl:
            return None
        plan = [(s, NV[s], len(vs)) for s, d in pst.items() for vs in d.values()]
        rng = random.Random(seed)
        nulls = []
        for _ in range(2000):
            tot, cnt = 0.0, 0
            for s, n, c in plan:
                for v in rng.sample(range(1, n + 1), c):
                    tot += rel(v, n)
                    cnt += 1
            nulls.append(tot / cnt)
        o = mean(rl)
        return {'n': len(rl), 'observed': o, 'null_mean': mean(nulls),
                'p_upper': perm_p_upper(o, nulls), 'p_lower': perm_p_lower(o, nulls)}

    h3_robust = {
        'onset_only': h3_arm(ALL_AB, onset_only=True),
        'legal_medinan_only': h3_arm(ALL_AB, restrict=legal_set),
        'purged_inventory': h3_arm(PURGED),
        'class_A_only': h3_arm(CLASS_A),
    }

    # ---------------- H5 / H6 genre control ---------------------------------
    qverse_wlen = [len(VTEXT[k].split()) for k in VERSES]
    starts, acc = [], 0
    for s in range(1, 115):
        starts.append(acc)
        acc += NV[s]
    legal_pos = [s - 1 for s in LEGAL]

    def surah_units(units, sids):
        out = []
        for i in sids:
            out.extend(units[starts[i]:starts[i] + NV[i + 1]])
        return out

    quran_units_all = [VTEXT[k].split() for k in VERSES]
    quran_legal_units = surah_units(quran_units_all, legal_pos)
    q_conc, q_n, q_top = topk_concentration(quran_legal_units)
    q_tri, _ = topk_concentration_tri(quran_legal_units)
    q_curve = {k: topk_concentration(quran_legal_units, k)[0] for k in K_CURVE}
    log(f'H5 quran legal arm: top-{TOP_K} onset-bigram concentration = {q_conc:.5f} (n={q_n})')

    buk_words = normalise_words(open(BUKHARI, encoding='utf-8').read())
    need = sum(qverse_wlen)
    span = len(buk_words) - need
    if span <= 0:
        raise SystemExit('FAIL bukhari stream too short for a matched partition')
    offsets = [i * span // (N_OFFSETS - 1) for i in range(N_OFFSETS)]
    buk_conc, buk_tri = [], []
    for off in offsets:
        units, err = build_pseudo_corpus(buk_words, qverse_wlen, off)
        if err:
            raise SystemExit('FAIL ' + err)
        lu = surah_units(units, legal_pos)
        buk_conc.append(topk_concentration(lu)[0])
        buk_tri.append(topk_concentration_tri(lu)[0])
    h5 = {
        'quran_legal_topk_conc': q_conc,
        'quran_legal_n_units': q_n,
        'quran_legal_top_bigrams': [[' '.join(b), n] for b, n in q_top],
        'bukhari_matched_mean': mean(buk_conc),
        'bukhari_matched_min': min(buk_conc),
        'bukhari_matched_max': max(buk_conc),
        'n_offsets': N_OFFSETS,
        'n_baseline_ge_observed': sum(1 for c in buk_conc if c >= q_conc),
        'p': (1 + sum(1 for c in buk_conc if c >= q_conc)) / (1 + N_OFFSETS),
        'quran_trigram_conc': q_tri,
        'bukhari_trigram_mean': mean(buk_tri),
        'regime': 'boundary-sensitive; arbitrary cuts DESTROY the baseline\'s real onsets, '
                  'so this arm handicaps al-Bukhari (STATE 2026-08-07 §4.7)',
    }
    h5_pass = (q_conc > h5['bukhari_matched_mean'] and h5['p'] <= ALPHA)
    log(f"H5 bukhari matched mean = {h5['bukhari_matched_mean']:.5f} "
        f"p={h5['p']:.5f} -> {'PASS' if h5_pass else 'FAIL'}")

    real_units = split_real_boundaries(buk_words)
    n_take = min(q_n, len(real_units))
    rng6 = random.Random(SEED_PRIMARY)
    real_conc, real_tri = [], []
    for _ in range(N_OFFSETS):
        sub = rng6.sample(real_units, n_take)
        real_conc.append(topk_concentration(sub)[0])
        real_tri.append(topk_concentration_tri(sub)[0])
    _rc, _rn, real_top = topk_concentration(real_units)
    h6 = {
        'n_real_units_total': len(real_units),
        'n_subsampled': n_take,
        'mean_unit_len_bukhari_real': mean([len(u) for u in real_units]),
        'mean_unit_len_quran_legal': mean([len(u) for u in quran_legal_units]),
        'bukhari_real_mean': mean(real_conc),
        'bukhari_real_min': min(real_conc),
        'bukhari_real_max': max(real_conc),
        'bukhari_real_top_bigrams': [[' '.join(b), n] for b, n in real_top],
        'n_baseline_ge_observed': sum(1 for c in real_conc if c >= q_conc),
        'p': (1 + sum(1 for c in real_conc if c >= q_conc)) / (1 + N_OFFSETS),
        'bukhari_real_trigram_mean': mean(real_tri),
        'regime': 'baseline given its REAL authored boundaries; this arm handicaps THIS corpus, '
                  'so a baseline pass is strong evidence against the claim',
    }
    h6_pass = (q_conc > h6['bukhari_real_mean'] and h6['p'] <= ALPHA)
    log(f"H6 bukhari real-boundary mean = {h6['bukhari_real_mean']:.5f} "
        f"p={h6['p']:.5f} -> {'PASS' if h6_pass else 'FAIL'}")

    # within-corpus reference: the other three registers
    reg_conc = {}
    for r in reg_mvl:
        pos = [s - 1 for s in range(1, 115) if surah_genre[s] == r]
        u = surah_units(quran_units_all, pos)
        reg_conc[r] = {'topk_conc': topk_concentration(u)[0], 'n_units': len(u)}

    # ---------------- exploratory (EXCLUDED from every inference) -----------
    exp_c = Counter(b for b in (onset_bigram(u) for u in quran_legal_units) if b)
    exploratory = {
        'note': 'POST-HOC. Excluded from H1-H6. Published only to show what a post-hoc '
                'frame list would have looked like.',
        'top20_legal_onset_bigrams': [[' '.join(b), n] for b, n in exp_c.most_common(20)],
        'coverage_of_top20': sum(n for _, n in exp_c.most_common(20)) / sum(exp_c.values()),
    }

    # ---------------- replication -------------------------------------------
    h2_rep = enrichment(PURGED, sur_nv, SEED_REPLICATION)
    h3_rep_nulls = h3_null(SEED_REPLICATION)
    h4_rep_nulls = h4_null(SEED_REPLICATION)
    rng6b = random.Random(SEED_REPLICATION)
    real_conc_rep = [topk_concentration(rng6b.sample(real_units, n_take))[0]
                     for _ in range(N_OFFSETS)]
    offsets_rep = [(i * span // (N_OFFSETS - 1) + span // (2 * N_OFFSETS)) % max(span, 1)
                   for i in range(N_OFFSETS)]
    buk_conc_rep = []
    for off in offsets_rep:
        units, err = build_pseudo_corpus(buk_words, qverse_wlen, min(off, span))
        if err:
            continue
        buk_conc_rep.append(topk_concentration(surah_units(units, legal_pos))[0])
    replication = {
        'seed': SEED_REPLICATION,
        'h2': {**h2_rep, 'pass': h2_rep['p'] <= ALPHA and h2_rep['observed'] > h2_rep['null_mean']},
        'h3': {'observed': h3_obs, 'null_mean': mean(h3_rep_nulls),
               'p_upper': perm_p_upper(h3_obs, h3_rep_nulls),
               'p_lower': perm_p_lower(h3_obs, h3_rep_nulls),
               'pass': h3_obs > 0.5 and perm_p_upper(h3_obs, h3_rep_nulls) <= ALPHA},
        'h4': {'observed': h4_obs, 'null_mean': mean(h4_rep_nulls),
               'p': perm_p_lower(h4_obs, h4_rep_nulls),
               'pass': h4_obs < mean(h4_rep_nulls) and perm_p_lower(h4_obs, h4_rep_nulls) <= ALPHA},
        'h5': {'bukhari_matched_mean': mean(buk_conc_rep),
               'p': (1 + sum(1 for c in buk_conc_rep if c >= q_conc)) / (1 + len(buk_conc_rep)),
               'pass': q_conc > mean(buk_conc_rep)
                       and (1 + sum(1 for c in buk_conc_rep if c >= q_conc)) / (1 + len(buk_conc_rep)) <= ALPHA},
        'h6': {'bukhari_real_mean': mean(real_conc_rep),
               'p': (1 + sum(1 for c in real_conc_rep if c >= q_conc)) / (1 + N_OFFSETS),
               'pass': q_conc > mean(real_conc_rep)
                       and (1 + sum(1 for c in real_conc_rep if c >= q_conc)) / (1 + N_OFFSETS) <= ALPHA},
    }
    for k in ['h2', 'h3', 'h4', 'h5', 'h6']:
        log(f'  replication {k}: pass={replication[k]["pass"]}')

    # ---------------- VERDICT — literal transcription of pre-reg §7 ---------
    H1_purged = h1['closure_purged']
    H2, H3, H4, H5, H6 = h2_pass, h3_pass, h4_pass, h5_pass, h6_pass

    closed = (H1_purged >= 0.50) and H2 and (H3 or H4) and H5 and H6
    genre_shared = H2 and (H3 or H4) and ((not H5) or (not H6))
    positioned = (H1_purged < 0.50) and H2 and (H3 or H4)
    null_v = not H2

    if closed:
        verdict = 'CLOSED-INVENTORY-WITH-POSITION'
    elif genre_shared:
        verdict = 'GENRE-SHARED'
    elif positioned:
        verdict = 'POSITIONED-BUT-NOT-CLOSED'
    elif null_v:
        verdict = 'NULL'
    else:
        verdict = 'NULL'

    verdict_diff = {
        'prereg_section': 'prereg §7 (LOCKED)',
        'inputs': {'H1_purged': H1_purged, 'H1_threshold': 0.50,
                   'H2_pass': H2, 'H3_pass': H3, 'H4_pass': H4,
                   'H5_pass': H5, 'H6_pass': H6},
        'branch_evaluations': {
            'CLOSED-INVENTORY-WITH-POSITION': closed,
            'GENRE-SHARED': genre_shared,
            'POSITIONED-BUT-NOT-CLOSED': positioned,
            'NULL': null_v,
        },
        'precedence_applied': ['CLOSED-INVENTORY-WITH-POSITION', 'GENRE-SHARED',
                               'POSITIONED-BUT-NOT-CLOSED', 'NULL'],
        'verdict': verdict,
    }
    log('\n=== VERDICT DIFF against pre-reg §7 ===')
    for k, v in verdict_diff['inputs'].items():
        log(f'  {k} = {v}')
    for k, v in verdict_diff['branch_evaluations'].items():
        log(f'  branch {k}: {v}')
    log(f'  VERDICT = {verdict}\n')

    # ---------------- assemble ----------------------------------------------
    result = {
        'id': 'H-NEW-2800',
        'title': 'The legal-formula frames: a closed inventory with positional structure',
        'prereg': os.path.relpath(PREREG, PROJECT),
        'prereg_sha256': EXPECTED_SHA,
        'frontier_item': 'F-15',
        'seed_primary': SEED_PRIMARY,
        'seed_replication': SEED_REPLICATION,
        'n_perm': N_PERM,
        'bonferroni_k': BONF_K,
        'alpha_bonferroni': ALPHA,
        'rules_tuple': '(no-tashkeel surface; QAC v0.4 morphological FEATURE FIELDS as the only '
                       'matching layer — never raw substrings; orthographic-word indices; verse '
                       'unit; basmala-counted-only-in-Q1; Hafs-Kufan; Mashriqi)',
        'register_label_provenance': {
            'instructed_source': os.path.relpath(J2530, PROJECT),
            'pointer_field': pointer,
            'actual_label_file': os.path.relpath(J2500, PROJECT),
            'decision_procedure': decision_procedure,
            'legal_markers': legal_markers,
            'DECLARED_CIRCULARITY': 'legal_medinan is DEFINED as "medinan AND (O-believers + '
                                    'kutiba-alaykum) >= 1", i.e. by frames B2 and A1 of this '
                                    'inventory. Presence of A1/B2 in every legal_medinan surah '
                                    'is true BY CONSTRUCTION. The purged inventory (minus A1, '
                                    'B2) is the inference of record.',
            'legal_medinan_surahs': LEGAL,
        },
        'classical_anchor': {
            'work': 'al-Suyuti, al-Itqan fi ulum al-Quran, naw 65 '
                    '(al-ulum al-mustanbata min al-Quran), ed. Muhammad Abu al-Fadl Ibrahim, '
                    '1394/1974, vol. 4 pp. 39-40',
            'file': os.path.relpath(ITQAN, PROJECT),
            'naw_heading_line': 20725,
            'ghazali_500_line': 20976,
            'ibn_abd_al_salam_frames_page': 'PageV04P040',
            'ibn_abd_al_salam_names': ['uhilla lakum', 'hurrimat alaykum al-mayta',
                                       'kutiba alaykum al-siyam'],
            'zarkashi_data_gap': 'data/literature/classical-tafsir/'
                                 'zarkashi-al-burhan-fi-ulum-al-quran.pdf is an image-only scan '
                                 '(Producer: Adobe Acrobat 7.05 Image Conversion Plug-in); '
                                 'pdftotext yields 0 lines. NO page of al-Zarkashi is cited.',
        },
        'frame_predicates': {fid: {'name': name, 'class': cls} for fid, name, cls, _ in FRAMES},
        'census': census,
        'rates_per_register': rates,
        'unit_drift_declaration': unit_drift,
        'H1_closure': h1,
        'H2_enrichment': {
            'purged_primary_stratified_verse_count': h2_purged,
            'purged_secondary_stratified_mean_verse_length': h2_purged_mvl,
            'full_inventory_CONTAMINATED_not_evidence': h2_full,
            'pass': h2_pass,
        },
        'H3_position_location': {
            'observed_mean_rel': h3_obs,
            'null_mean_rel': h3_null_mean,
            'scale_free_check_null_mean_should_be_0.5': h3_null_mean,
            'n_occurrences': len(obs_rels),
            'p_upper_locked_direction': h3_p_upper,
            'p_lower_reverse': h3_p_lower,
            'pass': h3_pass,
            'precommit_violation_reverse_significant': h3_precommit_violation,
            'robustness': h3_robust,
        },
        'H4_position_clustering': {
            'observed_mean_normalised_gap': h4_obs,
            'null_mean': mean(h4_nulls),
            'n_pairs': h4_npairs,
            'n_surahs': len(h4_surahs),
            'p': h4_p,
            'pass': h4_pass,
        },
        'H5_genre_control_arbitrary_partition': {**h5, 'pass': h5_pass},
        'H6_genre_control_real_boundaries': {**h6, 'pass': h6_pass},
        'within_corpus_onset_concentration_by_register': reg_conc,
        'quran_legal_topk_curve': q_curve,
        'exploratory_EXCLUDED': exploratory,
        'replication': replication,
        'verdict_diff_against_prereg': verdict_diff,
        'verdict': verdict,
    }

    outp = os.path.join(RUNDIR, 'h-new-2800.json')
    with open(outp, 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=1, ensure_ascii=False)

    manifest = {
        'finding_id': 'H-NEW-2800',
        'seed_primary': SEED_PRIMARY,
        'seed_replication': SEED_REPLICATION,
        'n_perm': N_PERM,
        'utc': datetime.now(timezone.utc).isoformat(),
        'prereg': os.path.relpath(PREREG, PROJECT),
        'prereg_sha256': EXPECTED_SHA,
        'script': os.path.relpath(os.path.abspath(__file__), PROJECT),
        'script_sha256': sha256_file(os.path.abspath(__file__)),
        'frozen_inputs': {os.path.relpath(p, PROJECT): sha256_file(p) for p in FROZEN},
        'output': os.path.relpath(outp, PROJECT),
        'verdict': verdict,
    }
    with open(os.path.join(RUNDIR, 'manifest.json'), 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=1, ensure_ascii=False)

    log(f'wrote {outp}')
    log(f'VERDICT: {verdict}')


if __name__ == '__main__':
    main()
