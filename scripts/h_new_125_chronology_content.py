#!/usr/bin/env python3
"""H-NEW-125 — Comprehensive chronology-content map: 15-axis Nöldeke correlation scan.

Pre-reg: findings/phase-b-hypotheses/h-new-125-chronology-content-prereg.md

Axes LOCKED (15):
  1.  surah_length                  (verses)
  2.  mean_verse_length             (tokens / verse)
  3.  muq_cardinality               (0 for non-muq; unique letters for muq)
  4.  allah_density                 (Allah-tokens / 100 verses)
  5.  qul_density                   (qul-imperatives / 100 verses)
  6.  prophet_narrative_density     (prophet-name tokens / 100 verses)
  7.  legal_term_density            (legal-root tokens / 100 verses)
  8.  eschatological_density        (eschat-root/lemma tokens / 100 verses)
  9.  book_reference_density        (book-root tokens / 100 verses)
 10.  oath_density                  (verse-initial wa-oath proxies / 100 verses)
 11.  divine_name_density           (99-name tokens / 100 verses)
 12.  personal_pronoun_density      (pronoun tokens / 100 verses)
 13.  rhyme_letter_diversity        (distinct verse-final letters in surah)
 14.  refrain_density               (intra-surah verse-text duplicates / 100 verses)
 15.  loanword_density              (Jeffery-218 match tokens / 100 verses)

Method: per-surah axis value → Spearman ρ vs Nöldeke rank → permutation null (10K, seed 20260417).
Bonferroni k=15, α_bon=0.00333. 2-sided.

Phase-transition scan: mean ± SD per axis per Nöldeke phase (Early/Middle/Late Meccan, Medinan).
"""
from __future__ import annotations
import csv
import json
import math
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
SEED = 20260417
N_PERM = 10_000
BON_K = 15
ALPHA_BON = 0.05 / BON_K  # 0.003333...

OUT_JSON = ROOT / 'findings/phase-b-hypotheses/csv/h-new-125.json'

random.seed(SEED)

# ==========================================================
# 0. Corpus load
# ==========================================================
with open(ROOT / 'quran-text/quran-no-tashkeel.json', encoding='utf-8') as f:
    corpus = json.load(f)
assert len(corpus) == 114, f"expected 114 surahs, got {len(corpus)}"

# Build per-surah verse structures
surahs = {}  # sid -> {'n_verses', 'verses': [ {'vid','text','words','wc','final_letter'} ... ]}
for s in corpus:
    sid = s['id']
    verses = []
    for v in s['verses']:
        text = v['text']
        words = text.split()
        wc = len(words)
        # Final Arabic grapheme of verse
        final_letter = ''
        if words:
            last_tok = words[-1]
            # Pick last Arabic letter character
            for ch in reversed(last_tok):
                if '\u0621' <= ch <= '\u064A':
                    final_letter = ch
                    break
        verses.append({
            'vid': v['id'],
            'text': text,
            'words': words,
            'wc': wc,
            'final_letter': final_letter,
        })
    surahs[sid] = {
        'name': s.get('name', ''),
        'transliteration': s.get('transliteration', ''),
        'type': s.get('type', ''),
        'n_verses': len(verses),
        'verses': verses,
    }

TOTAL_VERSES = sum(len(surahs[sid]['verses']) for sid in surahs)
TOTAL_WORDS = sum(v['wc'] for sid in surahs for v in surahs[sid]['verses'])
print(f"[H-NEW-125] Loaded {len(corpus)} surahs, {TOTAL_VERSES} verses, {TOTAL_WORDS} words",
      file=sys.stderr)

# ==========================================================
# 1. Chronology (Nöldeke rank)
# ==========================================================
noldeke_rank = {}     # sid -> Nöldeke rank (1..114)
noldeke_phase = {}    # sid -> phase string
period_mm = {}        # sid -> 'Meccan' / 'Medinan'

with open(ROOT / 'data/revelation-order.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        sid = int(row['mushaf_order'])
        noldeke_rank[sid] = int(row['noldeke_order'])
        noldeke_phase[sid] = row['noldeke_phase']
        period_mm[sid] = row['period']

assert len(noldeke_rank) == 114, f"expected 114 chronology rows, got {len(noldeke_rank)}"

# ==========================================================
# 2. QAC morphology load (for axes 5, 7, 8, 9)
# ==========================================================
print("[H-NEW-125] Loading QAC morphology...", file=sys.stderr)

# Structure: qac_tokens[(sid, vid)] = list of dicts {pos, features, root, lem}
qac_tokens = defaultdict(list)
with open(ROOT / 'data/morphology/quranic-corpus-morphology-0.4.txt', encoding='utf-8') as f:
    for line in f:
        if not line.startswith('('):
            continue
        parts = line.rstrip('\n').split('\t')
        if len(parts) < 4:
            continue
        loc, form, tag, features = parts
        m = re.match(r'\((\d+):(\d+):(\d+):(\d+)\)', loc)
        if not m:
            continue
        sid = int(m.group(1))
        vid = int(m.group(2))
        wid = int(m.group(3))
        pid = int(m.group(4))
        # Extract root & lemma
        root = None
        lem = None
        for feat in features.split('|'):
            if feat.startswith('ROOT:'):
                root = feat[5:]
            elif feat.startswith('LEM:'):
                lem = feat[4:]
        qac_tokens[(sid, vid)].append({
            'wid': wid, 'pid': pid, 'form': form, 'tag': tag,
            'features': features, 'root': root, 'lem': lem,
        })

N_QAC_VERSES = len(qac_tokens)
print(f"[H-NEW-125]   QAC covers {N_QAC_VERSES} verse keys", file=sys.stderr)

# ==========================================================
# 3. Muqaṭṭāʿat cardinality (axis 3)
# ==========================================================
# Locked map: surah -> set of unique letters in the muqaṭṭāʿat
MUQ_LETTERS = {
    2:   set('الم'),           # الم → {ا, ل, م}
    3:   set('الم'),
    7:   set('المص'),          # المص → 4
    10:  set('الر'),           # الر → 3
    11:  set('الر'),
    12:  set('الر'),
    13:  set('المر'),          # المر → 4
    14:  set('الر'),
    15:  set('الر'),
    19:  set('كهيعص'),         # كهيعص → 5
    20:  set('طه'),            # طه → 2
    26:  set('طسم'),           # طسم → 3
    27:  set('طس'),            # طس → 2
    28:  set('طسم'),
    29:  set('الم'),
    30:  set('الم'),
    31:  set('الم'),
    32:  set('الم'),
    36:  set('يس'),            # يس → 2
    38:  set('ص'),             # ص → 1
    40:  set('حم'),            # حم → 2
    41:  set('حم'),
    42:  set('حمعسق'),         # حم عسق → 5
    43:  set('حم'),
    44:  set('حم'),
    45:  set('حم'),
    46:  set('حم'),
    50:  set('ق'),             # ق → 1
    68:  set('ن'),             # ن → 1
}
assert len(MUQ_LETTERS) == 29

# Axis 3 value
axis_3_values = {sid: (len(MUQ_LETTERS[sid]) if sid in MUQ_LETTERS else 0) for sid in surahs}

# ==========================================================
# 4. Axis extractors
# ==========================================================
# Axis 1 — surah length
axis_1 = {sid: surahs[sid]['n_verses'] for sid in surahs}

# Axis 2 — mean verse length
axis_2 = {}
for sid in surahs:
    vs = surahs[sid]['verses']
    if vs:
        axis_2[sid] = sum(v['wc'] for v in vs) / len(vs)
    else:
        axis_2[sid] = 0.0

# Axis 3 — muq cardinality (done above)
axis_3 = axis_3_values

# Axis 4 — Allah-density (H-NEW-71 locked rule)
ALLOWED_PREFIXES_ALLAH = {'و','ف','ب','ت','أب','أف','أو','وت','فت','فب'}
ALLOWED_PREFIXES_LILLAH = {'و','ف'}

def is_allah_token(w):
    if not w:
        return False
    if w == 'الله': return True
    if w == 'اللهم': return True
    if w == 'آلله': return True
    if w == 'لله': return True
    if w.endswith('الله') and len(w) > 4:
        prefix = w[:-len('الله')]
        return prefix in ALLOWED_PREFIXES_ALLAH
    if w.endswith('لله') and not w.endswith('الله') and len(w) > 3:
        prefix = w[:-len('لله')]
        return prefix in ALLOWED_PREFIXES_LILLAH
    return False

axis_4 = {}
total_allah = 0
for sid in surahs:
    c = 0
    for v in surahs[sid]['verses']:
        for w in v['words']:
            if is_allah_token(w):
                c += 1
    total_allah += c
    axis_4[sid] = 100.0 * c / max(surahs[sid]['n_verses'], 1)
print(f"[H-NEW-125] Allah total = {total_allah} (expected ~2704 per H-NEW-71)", file=sys.stderr)

# Axis 5 — qul density via QAC (POS:V & IMPV & LEM:qaAla & 2MS)
axis_5 = {}
total_qul = 0
qul_per_surah = defaultdict(int)
for (sid, vid), toks in qac_tokens.items():
    for t in toks:
        feats = t['features']
        if ('POS:V' in feats and 'IMPV' in feats
                and 'LEM:qaAla' in feats and '|2MS' in feats):
            qul_per_surah[sid] += 1
            total_qul += 1
for sid in surahs:
    axis_5[sid] = 100.0 * qul_per_surah[sid] / max(surahs[sid]['n_verses'], 1)
print(f"[H-NEW-125] qul total = {total_qul} (expected 332 per H-NEW-74)", file=sys.stderr)

# Axis 6 — prophet-narrative density (surface tokens, prefix-tolerant)
PROPHET_CORES = [
    'موسى','عيسى','ابراهيم','نوح','يوسف','يونس','لوط','هود','صالح','شعيب',
    'داود','سليمان','زكريا','يحيى','اسماعيل','اسحاق','يعقوب','ادم','ايوب','ادريس',
    'الياس','اليسع','ذو','الكفل','فرعون','النبي','نبي','رسول','مرسل'
]
# Prefixes typical for names: ال, و, ف, ب, ل, و+ال, ف+ال, ب+ال, ل+ال, كال, سال
PROPHET_PREFIXES = ['', 'و','ف','ب','ل','ك','س','وال','فال','بال','لل','كال']

def token_matches_any(w, core_set):
    """Match if w == core OR w == prefix + core for prefix in allowed set."""
    if w in core_set:
        return True
    for p in PROPHET_PREFIXES:
        if p and w.startswith(p):
            rest = w[len(p):]
            if rest in core_set:
                return True
    return False

PROPHET_SET = set(PROPHET_CORES)
axis_6 = {}
total_prophet = 0
for sid in surahs:
    c = 0
    for v in surahs[sid]['verses']:
        for w in v['words']:
            if token_matches_any(w, PROPHET_SET):
                c += 1
    total_prophet += c
    axis_6[sid] = 100.0 * c / max(surahs[sid]['n_verses'], 1)
print(f"[H-NEW-125] prophet-narrative total = {total_prophet}", file=sys.stderr)

# Axis 7 — legal-term density via QAC roots
LEGAL_ROOTS = {'ktb', 'Hkm', 'Amr', 'nhy', 'frD'}
axis_7 = {}
legal_per_surah = defaultdict(int)
for (sid, vid), toks in qac_tokens.items():
    for t in toks:
        if t['root'] in LEGAL_ROOTS:
            legal_per_surah[sid] += 1
for sid in surahs:
    axis_7[sid] = 100.0 * legal_per_surah[sid] / max(surahs[sid]['n_verses'], 1)
total_legal = sum(legal_per_surah.values())
print(f"[H-NEW-125] legal-root total = {total_legal}", file=sys.stderr)

# Axis 8 — eschatological density
ESCHAT_ROOTS = {'ywm', 'Axr', 'qwm', 'nAr'}  # root-level
ESCHAT_LEMS = {'jahan~am', 'firodawos', 'jan~ah', 'qiya`mah'}  # lemma-level (QAC notation approximated)
axis_8 = {}
eschat_per_surah = defaultdict(int)
for (sid, vid), toks in qac_tokens.items():
    for t in toks:
        r = t['root']
        l = t['lem']
        if r in ESCHAT_ROOTS:
            eschat_per_surah[sid] += 1
        elif l and any(l.startswith(x[:6]) for x in ESCHAT_LEMS):
            eschat_per_surah[sid] += 1
for sid in surahs:
    axis_8[sid] = 100.0 * eschat_per_surah[sid] / max(surahs[sid]['n_verses'], 1)
total_eschat = sum(eschat_per_surah.values())
print(f"[H-NEW-125] eschatological total = {total_eschat}", file=sys.stderr)

# Axis 9 — book-reference density via QAC roots
BOOK_ROOTS = {'ktb', 'qrA', 'Ayy', 'nzl'}
axis_9 = {}
book_per_surah = defaultdict(int)
for (sid, vid), toks in qac_tokens.items():
    for t in toks:
        if t['root'] in BOOK_ROOTS:
            book_per_surah[sid] += 1
for sid in surahs:
    axis_9[sid] = 100.0 * book_per_surah[sid] / max(surahs[sid]['n_verses'], 1)
total_book = sum(book_per_surah.values())
print(f"[H-NEW-125] book-reference total = {total_book}", file=sys.stderr)

# Axis 10 — oath density (proxy: verse starts with "و" prefix on noun/celestial)
# Operational heuristic: verse-initial token begins with 'و' followed by a definite article or noun
# Pre-committed proxy per the pre-reg (noisy — locked as noisy proxy).
OATH_CORE = {'والسماء','والشمس','والقمر','والليل','والفجر','والنهار','والضحى','والنجم',
             'والتين','والعصر','والعاديات','والمرسلات','والصافات','والذاريات','والنازعات',
             'والمرسلت','والطور','والبلد','والسمآء','والكتاب','والقران','والقلم','وربك',
             'والسابحات','والقلم','والذكر','والحافظات'}
axis_10 = {}
oath_per_surah = defaultdict(int)
for sid in surahs:
    for v in surahs[sid]['verses']:
        if v['words']:
            first = v['words'][0]
            if first in OATH_CORE or (first.startswith('و') and len(first) > 3
                                      and first[1:3] == 'ال'):
                oath_per_surah[sid] += 1
for sid in surahs:
    axis_10[sid] = 100.0 * oath_per_surah[sid] / max(surahs[sid]['n_verses'], 1)
total_oath = sum(oath_per_surah.values())
print(f"[H-NEW-125] oath-verse total (proxy) = {total_oath}", file=sys.stderr)

# Axis 11 — 99 divine names density
# Load asma list (skip # comments)
asma_list = []
with open(ROOT / 'data/asma-al-husna.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        asma_list.append(line)
print(f"[H-NEW-125] Loaded {len(asma_list)} divine names", file=sys.stderr)

# Build a set of acceptable forms: name, and common proclitics on name
NAME_PREFIXES = ['', 'و','ف','ب','ل','ك','س','و','وال','فال','بال','لل']
name_forms = set()
for n in asma_list:
    for p in NAME_PREFIXES:
        name_forms.add(p + n)
    # Also drop leading "ال" to get al-less forms (some attested bare)
    if n.startswith('ال'):
        bare = n[2:]
        for p in NAME_PREFIXES:
            name_forms.add(p + bare)

axis_11 = {}
name_per_surah = defaultdict(int)
for sid in surahs:
    c = 0
    for v in surahs[sid]['verses']:
        for w in v['words']:
            if w in name_forms:
                c += 1
    name_per_surah[sid] = c
    axis_11[sid] = 100.0 * c / max(surahs[sid]['n_verses'], 1)
total_names = sum(name_per_surah.values())
print(f"[H-NEW-125] divine-name total = {total_names}", file=sys.stderr)

# Axis 12 — personal pronoun density (orthographic match)
PRONOUN_SET = {'انا','انت','هو','هي','نحن','انتم','انتما','هم','هما','انتن','هن'}
axis_12 = {}
pron_per_surah = defaultdict(int)
for sid in surahs:
    c = 0
    for v in surahs[sid]['verses']:
        for w in v['words']:
            if w in PRONOUN_SET:
                c += 1
    pron_per_surah[sid] = c
    axis_12[sid] = 100.0 * c / max(surahs[sid]['n_verses'], 1)
total_pron = sum(pron_per_surah.values())
print(f"[H-NEW-125] personal-pronoun total = {total_pron}", file=sys.stderr)

# Axis 13 — rhyme-letter diversity (distinct verse-final letters per surah)
axis_13 = {}
for sid in surahs:
    finals = set()
    for v in surahs[sid]['verses']:
        if v['final_letter']:
            finals.add(v['final_letter'])
    axis_13[sid] = len(finals)

# Axis 14 — refrain density (intra-surah exact-verse repeats)
axis_14 = {}
total_refrain = 0
for sid in surahs:
    text_counts = Counter(v['text'] for v in surahs[sid]['verses'])
    # count verses that belong to duplicate groups
    c = sum(n for n in text_counts.values() if n >= 2)
    # Subtract the first occurrence of each dup group so we count "repeats"
    repeats = sum((n - 1) for n in text_counts.values() if n >= 2)
    axis_14[sid] = 100.0 * repeats / max(surahs[sid]['n_verses'], 1)
    total_refrain += repeats
print(f"[H-NEW-125] total verse-exact-refrain repeats = {total_refrain}", file=sys.stderr)

# Axis 15 — loanword density (Jeffery 218)
loanword_set = set()
with open(ROOT / 'data/loanwords/jeffery-1938-loanwords.tsv', encoding='utf-8') as f:
    for line in f:
        if line.startswith('#') or line.startswith('arabic_lemma'):
            continue
        parts = line.rstrip('\n').split('\t')
        if not parts or not parts[0]:
            continue
        lem = parts[0].strip()
        if lem:
            loanword_set.add(lem)
print(f"[H-NEW-125] Loaded {len(loanword_set)} loanword lemmas", file=sys.stderr)

# Match with same proclitic policy as names
loan_forms = set()
for n in loanword_set:
    for p in NAME_PREFIXES:
        loan_forms.add(p + n)
    if n.startswith('ال'):
        bare = n[2:]
        for p in NAME_PREFIXES:
            loan_forms.add(p + bare)

axis_15 = {}
loan_per_surah = defaultdict(int)
for sid in surahs:
    c = 0
    for v in surahs[sid]['verses']:
        for w in v['words']:
            if w in loan_forms:
                c += 1
    loan_per_surah[sid] = c
    axis_15[sid] = 100.0 * c / max(surahs[sid]['n_verses'], 1)
total_loan = sum(loan_per_surah.values())
print(f"[H-NEW-125] loanword total = {total_loan}", file=sys.stderr)

# ==========================================================
# 5. Spearman ρ and permutation null
# ==========================================================
def rank_array(values):
    """Mean-rank with tie handling."""
    n = len(values)
    indexed = sorted(range(n), key=lambda i: values[i])
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and values[indexed[j+1]] == values[indexed[i]]:
            j += 1
        avg_rank = (i + j) / 2 + 1  # 1-indexed mean
        for k in range(i, j + 1):
            ranks[indexed[k]] = avg_rank
        i = j + 1
    return ranks

def spearman_rho(x, y):
    rx = rank_array(x)
    ry = rank_array(y)
    n = len(x)
    mean_rx = sum(rx) / n
    mean_ry = sum(ry) / n
    num = sum((rx[i] - mean_rx) * (ry[i] - mean_ry) for i in range(n))
    sx = math.sqrt(sum((r - mean_rx)**2 for r in rx))
    sy = math.sqrt(sum((r - mean_ry)**2 for r in ry))
    if sx == 0 or sy == 0:
        return 0.0
    return num / (sx * sy)

axes_list = [
    ('surah_length',              axis_1),
    ('mean_verse_length',         axis_2),
    ('muq_cardinality',           axis_3),
    ('allah_density',             axis_4),
    ('qul_density',               axis_5),
    ('prophet_narrative_density', axis_6),
    ('legal_term_density',        axis_7),
    ('eschatological_density',    axis_8),
    ('book_reference_density',    axis_9),
    ('oath_density',              axis_10),
    ('divine_name_density',       axis_11),
    ('personal_pronoun_density',  axis_12),
    ('rhyme_letter_diversity',    axis_13),
    ('refrain_density',           axis_14),
    ('loanword_density',          axis_15),
]
assert len(axes_list) == 15

sids = sorted(surahs.keys())
n_rank = [noldeke_rank[s] for s in sids]

# Pre-rank the Nöldeke x once (it's the same for all axes)
rx_nold = rank_array(n_rank)
mean_rx_nold = sum(rx_nold) / len(rx_nold)
sx_nold = math.sqrt(sum((r - mean_rx_nold)**2 for r in rx_nold))

# For permutation: pre-compute each axis rank vector once
results = {}
print("[H-NEW-125] Running 15 Spearman tests with 10K permutation null each...", file=sys.stderr)
for name, axis in axes_list:
    y = [axis[s] for s in sids]
    rho_obs = spearman_rho(n_rank, y)
    ry = rank_array(y)
    mean_ry = sum(ry) / len(ry)
    sy = math.sqrt(sum((r - mean_ry)**2 for r in ry))
    # Permutation: shuffle ranks of Nöldeke across the same axis
    rng = random.Random(SEED + hash(name) % 10000)
    perm_indices = list(range(len(sids)))
    n_ge = 0
    abs_obs = abs(rho_obs)
    for _ in range(N_PERM):
        rng.shuffle(perm_indices)
        # Compute rho with perm'd Nöldeke ranks
        rx_perm = [rx_nold[i] for i in perm_indices]
        num = sum((rx_perm[i] - mean_rx_nold) * (ry[i] - mean_ry) for i in range(len(sids)))
        rho_perm = num / (sx_nold * sy) if (sx_nold * sy) else 0.0
        if abs(rho_perm) >= abs_obs:
            n_ge += 1
    p_two_sided = (1 + n_ge) / (1 + N_PERM)
    passed = p_two_sided < ALPHA_BON

    # Phase means (descriptive)
    phase_vals = defaultdict(list)
    for s in sids:
        phase_vals[noldeke_phase[s]].append(axis[s])
    phase_means = {}
    for ph, vs in phase_vals.items():
        if vs:
            mu = sum(vs) / len(vs)
            if len(vs) > 1:
                var = sum((v - mu)**2 for v in vs) / (len(vs) - 1)
                sd = math.sqrt(var)
            else:
                sd = 0.0
            phase_means[ph] = {'mean': mu, 'sd': sd, 'n': len(vs)}
        else:
            phase_means[ph] = {'mean': 0.0, 'sd': 0.0, 'n': 0}

    # Classify trajectory
    phase_order = ['Early Meccan', 'Middle Meccan', 'Late Meccan', 'Medinan']
    mus = [phase_means[p]['mean'] for p in phase_order]
    # Monotone?
    monotone_up = all(mus[i] < mus[i+1] for i in range(3))
    monotone_dn = all(mus[i] > mus[i+1] for i in range(3))
    # Flat?
    mn, mx = min(mus), max(mus)
    flat = (mx / mn < 1.25) if mn > 0 else (mx - mn < 0.25 * max(abs(mx), 1e-9))
    # Peak/trough
    peak_idx = mus.index(max(mus))
    trough_idx = mus.index(min(mus))
    # Jump
    deltas = [abs(mus[i+1] - mus[i]) for i in range(3)]
    if deltas:
        max_d = max(deltas)
        others = [d for d in deltas if d != max_d]
        jump = (max_d > 2 * max(others)) if others else False
        jump_at = deltas.index(max_d) if jump else None
    else:
        jump = False
        jump_at = None
    if monotone_up:
        traj = 'MONOTONE_UP'
    elif monotone_dn:
        traj = 'MONOTONE_DOWN'
    elif flat:
        traj = 'FLAT'
    elif peak_idx in (1, 2) and mus[peak_idx] > mus[0] and mus[peak_idx] > mus[3]:
        traj = f'INVERTED_U_peak_{phase_order[peak_idx]}'
    elif trough_idx in (1, 2) and mus[trough_idx] < mus[0] and mus[trough_idx] < mus[3]:
        traj = f'U_SHAPED_trough_{phase_order[trough_idx]}'
    else:
        traj = 'IRREGULAR'
    if jump:
        traj = traj + f' + JUMP_between_{phase_order[jump_at]}_and_{phase_order[jump_at+1]}'

    results[name] = {
        'axis_name': name,
        'rho_spearman': rho_obs,
        'p_two_sided_perm': p_two_sided,
        'alpha_bon': ALPHA_BON,
        'bonferroni_survives': bool(passed),
        'n_ge_perm': n_ge,
        'n_perm': N_PERM,
        'phase_means': phase_means,
        'trajectory': traj,
        'phase_order': phase_order,
        'phase_mu_sequence': mus,
    }
    print(f"   {name:30s}  ρ={rho_obs:+.4f}  p={p_two_sided:.5f}  "
          f"{'PASS' if passed else 'null'}  [{traj}]", file=sys.stderr)

# ==========================================================
# 6. Summary
# ==========================================================
n_pass = sum(1 for r in results.values() if r['bonferroni_survives'])
pass_axes = [n for n, r in results.items() if r['bonferroni_survives']]
strongest = sorted(results.values(), key=lambda r: abs(r['rho_spearman']), reverse=True)

summary = {
    'id': 'H-NEW-125',
    'title': 'Comprehensive chronology-content map (15 axes)',
    'bonferroni_family': 'h-new-125-chronology-content',
    'bonferroni_k': BON_K,
    'alpha_bon': ALPHA_BON,
    'direction': '2-sided',
    'n_perm': N_PERM,
    'seed': SEED,
    'axes_tested': [n for n, _ in axes_list],
    'n_axes_passing_bonferroni': n_pass,
    'axes_passing': pass_axes,
    'strongest_3': [
        {'axis': r['axis_name'], 'rho': r['rho_spearman'], 'p': r['p_two_sided_perm'],
         'trajectory': r['trajectory']}
        for r in strongest[:3]
    ],
    'positive_control_axis_1_surah_length': {
        'rho': results['surah_length']['rho_spearman'],
        'p': results['surah_length']['p_two_sided_perm'],
        'mw5_pass': results['surah_length']['rho_spearman'] > 0.4 and results['surah_length']['p_two_sided_perm'] < 0.001,
    },
    'totals': {
        'allah_tokens': total_allah,
        'qul_tokens': total_qul,
        'prophet_tokens': total_prophet,
        'legal_tokens': total_legal,
        'eschat_tokens': total_eschat,
        'book_tokens': total_book,
        'oath_verse_starts': total_oath,
        'divine_name_tokens': total_names,
        'pronoun_tokens': total_pron,
        'loanword_tokens': total_loan,
        'refrain_verse_repeats': total_refrain,
    },
    'per_axis_results': results,
    'per_surah_axis_values': {
        sid: {
            'name': surahs[sid]['transliteration'],
            'noldeke_rank': noldeke_rank[sid],
            'noldeke_phase': noldeke_phase[sid],
            'axis_values': {name: axis[sid] for name, axis in axes_list},
        }
        for sid in sids
    },
}

OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
with open(OUT_JSON, 'w', encoding='utf-8') as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)

print(f"\n[H-NEW-125] Summary:", file=sys.stderr)
print(f"   Axes passing Bonferroni-15: {n_pass}/15", file=sys.stderr)
print(f"   Passing: {pass_axes}", file=sys.stderr)
print(f"   Strongest 3: {[(r['axis_name'], r['rho_spearman']) for r in strongest[:3]]}", file=sys.stderr)
print(f"   MW-5 (axis 1): ρ={results['surah_length']['rho_spearman']:+.4f}, "
      f"p={results['surah_length']['p_two_sided_perm']:.5f} — "
      f"{'PASS' if summary['positive_control_axis_1_surah_length']['mw5_pass'] else 'FAIL'}",
      file=sys.stderr)
print(f"   Output JSON: {OUT_JSON}", file=sys.stderr)
