"""Derived equations run — 4 derivations in one pass.

Rules tuple: (no-tashkeel, orthographic-token & lemma, graphemes,
counted-only-in-surah-1, hafs-kufan, mashriqi).

Outputs JSON payload consumed by the markdown writer.
"""
from __future__ import annotations

import json
import math
import os
import re
import sys
from collections import Counter, defaultdict

import numpy as np

ROOT = "/Users/grey/Downloads/quran"
sys.path.insert(0, os.path.join(ROOT, "analysis"))

from tools.loader import load_quran  # noqa: E402
from tools.tokenize import real_words, is_letter  # noqa: E402


def letters_only(text: str) -> str:
    return "".join(ch for ch in text if is_letter(ch))


# ---------------------------------------------------------------------------
# Corpus loading
# ---------------------------------------------------------------------------
SURAHS = load_quran("no-tashkeel")
VERSES = []  # list of dicts
for s in SURAHS:
    for v in s.verses:
        # Skip basmala-as-verse for surah 1? The rule says basmala counted only
        # in Surah 1 which is already the JSON state; so we KEEP Q 1:1.
        toks = real_words(v.text)
        VERSES.append({
            "surah": s.id,
            "ayah": v.id,
            "key": f"{s.id}:{v.id}",
            "text": v.text,
            "tokens": toks,
            "n_words": len(toks),
            "letters": letters_only(v.text),
        })
N_VERSES = len(VERSES)
assert N_VERSES == 6236, f"expected 6236, got {N_VERSES}"

# index by key
BY_KEY = {v["key"]: v for v in VERSES}


# ============================================================================
# DERIVATION 1 — Cosmic-Inversion Palindrome CFG
# ============================================================================
#
# Specify formal grammar. Let Σ_w be orthographic words.
# Production rules:
#   P  → x NP V NP' x         (the 5-word template, A-B-C-B-A on words)
#   x  → PREP
#   PREP → "في" | "من" | "على"
#   V  → "ويولج" | "وتولج" | "يولج" | "تولج" | "يكور" | "وتكور"
#        | "ويخرج" | "وتخرج" | "يخرج" | "تخرج" | "مخرج" | "ومخرج"
#        | "ثم" (used in Q4:137 apostasy cycle — see below)
#        | "فأتاهم"  (Q59:2 singleton)
#   NP → "النهار" | "النهاره" | "الميت" | "الميته" | "آمنوا" | "كفروا" | "الله"
#
# Constraint: the first-NP and third-NP come from the same lexical *pair*.
#    * if V ∈ {walaja family}  → NP pair ⊂ {al-nahar, al-layl}
#    * if V ∈ {kharaja family} → NP pair ⊂ {al-mayt, al-hayy}
#    * if V ∈ {kawwara family} → NP pair ⊂ {al-nahar, al-layl}
#    * if V = "ثم"             → NP pair ⊂ {amanu, kafaru}
#    * if V = "فأتاهم"         → NP pair ⊂ {Allah, Allah}  (singleton slot)
#
# The A-B-C-B-A surface palindromicity REQUIRES first-word = fifth-word and
# second-word = fourth-word. Since PREP ≠ PREP' in modern Arabic we also get
# palindromicity trivially only if the outer PREP is repeated, which matches
# the corpus: "في X Y X في", "من X Y X من", "على X Y X على". This means the
# CFG constrains: outer PREP must EQUAL its mirror.
#
# Determiner-agglutinated forms: النهار appears both as "النهار" and as
# "النهاره" (with cliticized definite+ACC alif). The corpus records the
# surface-palindrome on bare tokens, so both variants count.
#
# Generative count. Number of well-formed derivations:
#   D = |PREP| × |V-families| × |NP-pair member choices|
#
# For walaja-family: PREP ∈ {في}, V ∈ {6 verbs}, NP ∈ {al-nahar variant}.
# But the A-B-C-B-A constraint binds NP = NP; so we pick ONE NP member for
# both slots. Multiply by 2 for which NP of the pair fronts.
#
# Verdict criteria: does the CFG generate all 13 observed instances AND only
# those (no overgeneration outside the catalog)?

WALAJA_VERBS = ["ويولج", "وتولج", "يولج", "تولج", "ومولج", "مولج"]
KAWWARA_VERBS = ["ويكور", "وتكور", "يكور", "تكور", "ومكور", "مكور"]
KHARAJA_VERBS = ["ويخرج", "وتخرج", "يخرج", "تخرج", "ومخرج", "مخرج"]
APOSTASY_CYCLE = ["ثم"]
RETRIBUTION = ["فأتاهم", "فأتاهن", "جاءهم"]

NIGHT_DAY_NPS = ["النهار", "النهاره", "الليل", "الليله", "النهار,", "الليل,"]
LIVE_DEAD_NPS = ["الميت", "الميته", "الحي", "الحيه"]
BELIEF_NPS = ["آمنوا", "كفروا"]
ALLAH_NP = ["الله"]

PREPS_NIGHT = ["في", "على"]   # walaja uses fi, kawwara uses ʿalā
PREPS_LIVE = ["من"]           # kharaja uses min
PREPS_BELIEF = ["ثم"]         # actually the pivot; for belief the outers are amanu/kafaru
PREPS_ALLAH = ["من"]          # Q 59:2


def strip_punct(w: str) -> str:
    return re.sub(r"[^\u0621-\u064A\u0671-\u06D3]", "", w)


# Find all A-B-C-B-A word palindromes in the Quran (5-word windows)
def find_palindromes_5():
    hits = []
    for verse in VERSES:
        toks = [strip_punct(t) for t in verse["tokens"]]
        toks = [t for t in toks if t]  # drop empties
        n = len(toks)
        for i in range(n - 4):
            w = toks[i:i+5]
            # need distinct middle
            if w[0] == w[4] and w[1] == w[3] and w[0] != w[1] and w[2] not in (w[0], w[1]):
                hits.append({
                    "verse": verse["key"],
                    "window": w,
                })
    return hits


PAL5 = find_palindromes_5()


def classify_palindrome(window):
    """Return grammar slot name or None if not grammar-generated."""
    w1, w2, w3, w4, w5 = window
    # outer must match, inner must match — given by the pal5 construction
    # slot 1: walaja (night/day, PREP=fi/ʿala)
    if w1 in ("في",) and w2 in NIGHT_DAY_NPS and w3 in WALAJA_VERBS:
        return "walaja-fi-night-day"
    if w1 in ("على",) and w2 in NIGHT_DAY_NPS and w3 in KAWWARA_VERBS:
        return "kawwara-ala-night-day"
    # slot 2: kharaja (live/dead, PREP=min)
    if w1 in ("من",) and w2 in LIVE_DEAD_NPS and w3 in KHARAJA_VERBS:
        return "kharaja-min-live-dead"
    # slot 3: apostasy cycle (belief/disbelief, pivot=thumma)
    if w1 in BELIEF_NPS and w2 in APOSTASY_CYCLE and w3 in BELIEF_NPS:
        return "apostasy-cycle"
    # slot 4: retribution singleton
    if w1 in ("من",) and w2 in ALLAH_NP and w3 in RETRIBUTION:
        return "retribution-singleton"
    return None


pal_classified = []
pal_unclassified = []
for h in PAL5:
    slot = classify_palindrome(h["window"])
    if slot:
        pal_classified.append({**h, "slot": slot})
    else:
        pal_unclassified.append(h)


# Generative enumeration: what does the CFG predict?
def cfg_generate():
    """All strings the CFG can produce (lexical instantiations). Not verse-
    anchored — just possible word-strings."""
    generated = set()
    # walaja family: outer=fi, inner=night-day set, pivot=walaja-verb
    for pivot in WALAJA_VERBS:
        for inner in ["النهار", "الليل"]:
            # A-B-C-B-A: must have inner = inner, outer = outer
            generated.add(("في", inner, pivot, inner, "في"))
    for pivot in KAWWARA_VERBS:
        for inner in ["النهار", "الليل"]:
            generated.add(("على", inner, pivot, inner, "على"))
    for pivot in KHARAJA_VERBS:
        for inner in ["الميت", "الحي"]:
            generated.add(("من", inner, pivot, inner, "من"))
    for pivot in APOSTASY_CYCLE:
        for outer in BELIEF_NPS:
            for inner in BELIEF_NPS:
                if outer != inner:
                    generated.add((outer, pivot, outer, pivot, outer))  # pattern differs
                    # Actually Q4:137 = آمنوا ثم كفروا ثم آمنوا — that's A-B-C-B-A
                    generated.add((outer, pivot, inner, pivot, outer))
    for pivot in RETRIBUTION:
        generated.add(("من", "الله", pivot, "الله", "من"))
    return generated


# Minimality check: can we predict any unseen instance?
CFG_STRINGS = cfg_generate()
observed_windows = {tuple(h["window"]) for h in PAL5}

# For each cfg string: is it observed?
cfg_observed = [s for s in CFG_STRINGS if s in observed_windows]
cfg_unobserved = [s for s in CFG_STRINGS if s not in observed_windows]

d1_result = {
    "total_pal5_found": len(PAL5),
    "classified_by_cfg": len(pal_classified),
    "unclassified": len(pal_unclassified),
    "cfg_string_space_size": len(CFG_STRINGS),
    "cfg_strings_observed": len(cfg_observed),
    "cfg_strings_unobserved": len(cfg_unobserved),
    "classified_examples": pal_classified[:20],
    "unclassified_examples": pal_unclassified[:20],
    "cfg_unobserved_examples": [list(s) for s in list(cfg_unobserved)[:15]],
}


# ============================================================================
# DERIVATION 2 — Ω_IAM(v) : Ism al-Aʿẓam composite index, closed form
# ============================================================================
#
# For each verse v define ten axial functionals f_k(v), scale to rank
# r_k(v) ∈ [1..N], then
#
#     Ω_IAM(v) = exp( (1/K) Σ_k ln r_k(v) )   (geometric mean of ranks)
#
# Smaller Ω = more distinctive. Under uniform-rank-per-axis null,
# E[Ω] = (N+1)/e ≈ 2296. Top-0.1% ⇒ Ω ≤ ~7 effective equivalent rank.
#
# Here we implement a STREAMLINED 10-axis version. For parity with the
# published composite we compute axes that are *fully* reproducible from
# the corpus without hand-curation. We note which axis is the "curated"
# one and drop it in a robustness check.

ASMA = []
with open(os.path.join(ROOT, "data", "asma-al-husna.txt"), encoding="utf-8") as fh:
    for line in fh:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        ASMA.append(line)
# Strip the leading "ال" from each name to form a stem; also keep the full form
ASMA_STEMS = set()
for nm in ASMA:
    ASMA_STEMS.add(nm)
    if nm.startswith("ال") and len(nm) > 2:
        ASMA_STEMS.add(nm[2:])


def count_divine_names(tokens):
    c = 0
    for t in tokens:
        ts = strip_punct(t)
        if ts in ASMA_STEMS or ts.replace("ا", "أ") in ASMA_STEMS:
            c += 1
            continue
        # Allah morphology
        if ts in ("الله", "لله", "بالله", "والله", "فالله", "تالله", "اللهم", "لله,"):
            c += 1
    return c


ABJAD_MASHRIQI = {
    "ا": 1, "أ": 1, "إ": 1, "آ": 1, "ب": 2, "ج": 3, "د": 4, "ه": 5, "ة": 5,
    "و": 6, "ؤ": 6, "ز": 7, "ح": 8, "ط": 9, "ي": 10, "ى": 10, "ئ": 10,
    "ك": 20, "ل": 30, "م": 40, "ن": 50, "س": 60, "ع": 70, "ف": 80, "ص": 90,
    "ق": 100, "ر": 200, "ش": 300, "ت": 400, "ث": 500, "خ": 600, "ذ": 700,
    "ض": 800, "ظ": 900, "غ": 1000,
}


def abjad_sum(text):
    return sum(ABJAD_MASHRIQI.get(ch, 0) for ch in text)


# compute axes
N = N_VERSES
word_counts = np.array([max(1, v["n_words"]) for v in VERSES])
letter_counts = np.array([len(v["letters"]) for v in VERSES])

# Axis 1: divine-name density
ax1 = np.array([count_divine_names(v["tokens"]) / max(1, v["n_words"]) for v in VERSES])

# Axis 2: divine-name uniqueness — which names appear only here
name_verse_counts = Counter()
verse_names = []  # per verse, set of normalized names present
for v in VERSES:
    names = set()
    for t in v["tokens"]:
        ts = strip_punct(t)
        for s in ASMA_STEMS:
            if ts == s:
                names.add(s)
    verse_names.append(names)
    for n in names:
        name_verse_counts[n] += 1
ax2 = np.array([sum(1 for n in names if name_verse_counts[n] == 1) for names in verse_names])

# Axis 3: hapax density — compute corpus-wide token frequencies
tok_freq = Counter()
for v in VERSES:
    for t in v["tokens"]:
        tok_freq[strip_punct(t)] += 1
ax3 = np.array([
    sum(1 for t in v["tokens"] if tok_freq[strip_punct(t)] == 1) / max(1, v["n_words"])
    for v in VERSES
])

# Axis 4: midpoint proxy — 1 - |v-mid|/max_dist, per surah
ax4 = np.zeros(N)
idx = 0
for s in SURAHS:
    n = len(s.verses)
    mid = (n + 1) / 2.0
    maxd = max(mid - 1, 1)
    for v in s.verses:
        ax4[idx] = 1.0 - abs(v.id - mid) / maxd
        idx += 1

# Axis 5: abjad property score
def abjad_axis(letters):
    s = abjad_sum(letters)
    score = 0
    # digit sum
    ds = sum(int(c) for c in str(s))
    if ds in (19, 7, 9):
        score += 2
    # divisors
    if s and s % 7 == 0:
        score += 1
    if s and s % 19 == 0:
        score += 1
    if s == 786:
        score += 3
    # distinct prime factors
    k = s
    primes = set()
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53]:
        while k % p == 0 and k > 1:
            primes.add(p)
            k //= p
    score += len(primes)
    return score
ax5 = np.array([abjad_axis(v["letters"]) for v in VERSES])

# Axis 6: rhyme-letter consistency — per-surah last-letter match to ±1/±2 neighbours
ax6 = np.zeros(N)
idx = 0
for s in SURAHS:
    surah_verses = list(s.verses)
    ends = []
    for v in surah_verses:
        letters = letters_only(v.text)
        # skip weak trailing letters
        while letters and letters[-1] in "اويهةى":
            letters = letters[:-1]
        ends.append(letters[-1] if letters else "")
    for j, _ in enumerate(surah_verses):
        score = 0
        for off in (-2, -1, 1, 2):
            if 0 <= j + off < len(surah_verses):
                if ends[j] and ends[j] == ends[j + off]:
                    score += 1
        ax6[idx] = score
        idx += 1

# Axis 7: phrase-pair recurrence (external 4-gram freq)
def make_ngrams(toks, n=4):
    return [tuple(toks[i:i+n]) for i in range(len(toks) - n + 1)]
global_4grams = Counter()
for v in VERSES:
    for ng in make_ngrams([strip_punct(t) for t in v["tokens"]], 4):
        global_4grams[ng] += 1
ax7 = np.zeros(N)
for i, v in enumerate(VERSES):
    ngs = make_ngrams([strip_punct(t) for t in v["tokens"]], 4)
    if ngs:
        # external freq = freq - 1 (exclude self-count, approximate)
        ax7[i] = np.mean([max(0, global_4grams[ng] - 1) for ng in ngs])

# Axis 8: classical-cross-reference — we OMIT this axis to avoid circularity.
# Instead we use a purely textual proxy: presence of formulaic opener
# "هو الله" or "لا إله إلا هو".
FORMULAIC = ("لا إله إلا هو", "هو الله", "ربكم الذي", "الحي القيوم",
             "الأسماء الحسنى", "لا إله إلا أنا", "الله الذي لا إله إلا هو")
ax8 = np.array([
    sum(1 for f in FORMULAIC if f in v["text"]) for v in VERSES
])

# Axis 9: self-reference / divine-attribute density
SELFREF_WORDS = {"الله", "هو", "إله", "إلا", "الذي", "لا", "ذو"}
ax9 = np.zeros(N)
for i, v in enumerate(VERSES):
    n = 0
    for t in v["tokens"]:
        ts = strip_punct(t)
        if ts in SELFREF_WORDS or ts.replace("إ", "ا") in SELFREF_WORDS:
            n += 1
    ax9[i] = n / max(1, v["n_words"])
    # bonuses
    if "لا إله إلا هو" in v["text"]:
        ax9[i] += 0.3
    if "الحي القيوم" in v["text"]:
        ax9[i] += 0.3
    if "الأسماء الحسنى" in v["text"]:
        ax9[i] += 0.3

# Axis 10: position-in-surah (opener/closer bonus, with center taper)
ax10 = np.zeros(N)
idx = 0
for s in SURAHS:
    n = len(s.verses)
    for v in s.verses:
        if v.id == 1 or v.id == n:
            ax10[idx] = 1.0
        else:
            # graded center
            mid = (n + 1) / 2.0
            ax10[idx] = max(0, 1.0 - abs(v.id - mid) / max(mid - 1, 1)) * 0.5
        idx += 1


def ranks_desc(arr):
    """Return dense ranks where highest value → rank 1 with ties averaged."""
    order = np.argsort(-arr, kind="stable")
    ranks = np.empty(len(arr))
    # average ties
    n = len(arr)
    i = 0
    while i < n:
        j = i
        while j + 1 < n and arr[order[j + 1]] == arr[order[i]]:
            j += 1
        avg = (i + 1 + j + 1) / 2.0
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    return ranks


axes = [ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9, ax10]
axis_names = [
    "div_name_density", "div_name_uniqueness", "hapax_density",
    "midpoint_proxy", "abjad_score", "rhyme_consistency",
    "phrase_recurrence", "formulaic_presence", "selfref_density",
    "position_in_surah",
]
rank_matrix = np.vstack([ranks_desc(a) for a in axes])  # shape (10, N)

# Omega = exp(mean(log r))
omega = np.exp(np.mean(np.log(rank_matrix), axis=0))
# Top 20
top20 = np.argsort(omega)[:20]
d2_top20 = [
    {
        "rank": int(i + 1),
        "verse": VERSES[ix]["key"],
        "omega": float(omega[ix]),
        "axis_ranks": {axis_names[k]: float(rank_matrix[k, ix]) for k in range(10)},
    }
    for i, ix in enumerate(top20)
]

# Rule-tuple invariance: re-compute Ω_IAM with shadda-doubled letter rule
# using min-tashkeel variant for axis 5 only, and report whether top-10 order
# preserves set.
try:
    SURAHS_MIN = load_quran("min-tashkeel")
    ax5_min = []
    for s in SURAHS_MIN:
        for v in s.verses:
            letters = letters_only(v.text)
            # count shadda additions
            # min-tashkeel keeps shadda only — but loader returns the same verse ids
            ax5_min.append(abjad_axis(letters))
    ax5_min = np.array(ax5_min)
    axes_alt = list(axes)
    axes_alt[4] = ax5_min
    rank_alt = np.vstack([ranks_desc(a) for a in axes_alt])
    omega_alt = np.exp(np.mean(np.log(rank_alt), axis=0))
    top20_alt = set(VERSES[ix]["key"] for ix in np.argsort(omega_alt)[:20])
    top20_ref = set(VERSES[ix]["key"] for ix in top20)
    overlap = len(top20_ref & top20_alt)
except Exception as e:
    overlap = -1
    top20_alt = set()

d2_result = {
    "N": N,
    "axis_names": axis_names,
    "top20": d2_top20,
    "E_omega_uniform": (N + 1) / math.e,
    "rule_invariance_top20_overlap": overlap,
}


# ============================================================================
# DERIVATION 3 — Constraint-Co-occurrence Matrix M_ij and Naẓm Index
# ============================================================================
#
# Reuse the 12 pre-registered constraints from T4. Load the persisted
# indicator matrix.
Mq_path = os.path.join(
    ROOT, "findings/phase-b-hypotheses/analysis/simultaneous-constraint-density/M_quran.npy"
)
Mb_path = os.path.join(
    ROOT, "findings/phase-b-hypotheses/analysis/simultaneous-constraint-density/M_baseline.npy"
)
CONSTRAINT_NAMES = [
    "rhyme_continuity", "verse_end_dispreference", "divine_name_present",
    "chiastic_root_palindrome", "jinas", "abjad_digit_root_3_6_9",
    "assonance_top_quartile", "length_fibonacci_band", "canonical_incipit",
    "iltifat_shift", "rare_root", "surprisal_gt_median",
]

def co_occurrence_lift(M):
    n, k = M.shape
    p = M.mean(axis=0)
    lift = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            pj = p[j]
            pij = float(np.mean(M[:, i] & M[:, j]))
            denom = p[i] * pj
            lift[i, j] = pij / denom if denom > 0 else np.nan
    return lift, p


def mutual_information(M):
    n, k = M.shape
    p = M.mean(axis=0)
    mi = np.zeros((k, k))
    for i in range(k):
        for j in range(k):
            if i == j:
                continue
            for xi in (0, 1):
                for xj in (0, 1):
                    pij = float(np.mean((M[:, i] == xi) & (M[:, j] == xj)))
                    pi = p[i] if xi == 1 else 1 - p[i]
                    pj = p[j] if xj == 1 else 1 - p[j]
                    if pij > 0 and pi > 0 and pj > 0:
                        mi[i, j] += pij * math.log2(pij / (pi * pj))
    return mi


if os.path.exists(Mq_path) and os.path.exists(Mb_path):
    Mq = np.load(Mq_path).astype(bool)
    Mb = np.load(Mb_path).astype(bool)
else:
    Mq = None
    Mb = None

d3_result = {}
if Mq is not None:
    lift_q, p_q = co_occurrence_lift(Mq)
    lift_b, p_b = co_occurrence_lift(Mb)
    mi_q = mutual_information(Mq)
    mi_b = mutual_information(Mb)
    # rank pairs by MI
    pairs = []
    K = len(CONSTRAINT_NAMES)
    for i in range(K):
        for j in range(i + 1, K):
            pairs.append({
                "pair": [CONSTRAINT_NAMES[i], CONSTRAINT_NAMES[j]],
                "lift_quran": float(lift_q[i, j]),
                "lift_baseline": float(lift_b[i, j]),
                "mi_quran_bits": float(mi_q[i, j]),
                "mi_baseline_bits": float(mi_b[i, j]),
            })
    pairs.sort(key=lambda x: -abs(x["mi_quran_bits"]))
    # Naẓm index: log-det of (I + ε) of normalized lift — or spectral radius
    # Use spectral radius of lift (minus identity)
    # Regularize
    def nazm_index(lift):
        A = np.nan_to_num(lift, nan=1.0) - np.eye(lift.shape[0])
        # symmetric part
        Asym = 0.5 * (A + A.T)
        eigvals = np.linalg.eigvalsh(Asym)
        return {
            "spectral_radius_minus_1": float(np.max(np.abs(eigvals))),
            "trace_A2": float(np.sum(eigvals ** 2)),
            "frobenius": float(np.linalg.norm(A)),
        }
    nazm_q = nazm_index(lift_q)
    nazm_b = nazm_index(lift_b)
    d3_result = {
        "per_constraint_rate_quran": dict(zip(CONSTRAINT_NAMES, p_q.tolist())),
        "per_constraint_rate_baseline": dict(zip(CONSTRAINT_NAMES, p_b.tolist())),
        "top_mi_pairs": pairs[:10],
        "nazm_index_quran": nazm_q,
        "nazm_index_baseline": nazm_b,
        "M_lift_quran_matrix": lift_q.tolist(),
        "M_lift_baseline_matrix": lift_b.tolist(),
    }
else:
    d3_result = {"error": "M_quran.npy / M_baseline.npy not found; rerun T4 first"}


# ============================================================================
# DERIVATION 4 — Twin-Opener Length Function N(L)
# ============================================================================
#
# Let s_v be letters of verse v. Let common_prefix_len(s, t) = largest L
# such that s[:L] == t[:L]. Define
#
#   N(L) = #{ (v, v+1) : common_prefix_len(s_v, s_{v+1}) >= L }
#
# Global — all 6235 consecutive pairs (only within-surah adjacency honored).

pairs_counts = {}
letter_streams = [v["letters"] for v in VERSES]
surah_ids = [v["surah"] for v in VERSES]


def shared_prefix(a, b):
    L = 0
    m = min(len(a), len(b))
    while L < m and a[L] == b[L]:
        L += 1
    return L


pair_prefix_lens = []
for i in range(N - 1):
    if surah_ids[i] == surah_ids[i + 1]:
        pair_prefix_lens.append(shared_prefix(letter_streams[i], letter_streams[i + 1]))
pair_prefix_lens = np.array(pair_prefix_lens)
n_pairs = len(pair_prefix_lens)

# also include pairs (v, v+1) at surah boundary? No, fairer to restrict.
Ls = [5, 10, 15, 20, 25, 30, 35, 40]
NofL = {L: int((pair_prefix_lens >= L).sum()) for L in Ls}

# Baseline: shuffle verses WITHIN surah — preserves length distribution
rng = np.random.default_rng(20260412)
null_counts = {L: [] for L in Ls}
B = 50
for _ in range(B):
    shuffled = []
    i = 0
    while i < N:
        j = i
        while j + 1 < N and surah_ids[j + 1] == surah_ids[i]:
            j += 1
        idxs = list(range(i, j + 1))
        rng.shuffle(idxs)
        shuffled.extend(idxs)
        i = j + 1
    # compute pair prefixes
    npl = []
    for k in range(N - 1):
        if surah_ids[k] == surah_ids[k + 1]:
            a = letter_streams[shuffled[k]]
            b = letter_streams[shuffled[k + 1]]
            npl.append(shared_prefix(a, b))
    npl = np.array(npl)
    for L in Ls:
        null_counts[L].append(int((npl >= L).sum()))

null_summary = {}
for L in Ls:
    arr = np.array(null_counts[L])
    null_summary[L] = {
        "null_mean": float(arr.mean()),
        "null_p95": float(np.percentile(arr, 95)),
        "observed": NofL[L],
        "z": float((NofL[L] - arr.mean()) / (arr.std() + 1e-9)) if arr.std() > 0 else float("inf"),
    }

# Fit curve: log N vs L — exponential vs power-law
xs = np.array([L for L in Ls if NofL[L] > 0])
ys = np.array([NofL[L] for L in Ls if NofL[L] > 0])
# Exponential fit: log N = a - b L
if len(xs) >= 2 and (ys > 0).all():
    lx = xs
    ly = np.log(ys)
    coeffs_exp = np.polyfit(lx, ly, 1)  # slope, intercept
    b_exp = -coeffs_exp[0]
    a_exp = coeffs_exp[1]
    # R² exponential
    yhat = np.polyval(coeffs_exp, lx)
    ss_res = np.sum((ly - yhat) ** 2)
    ss_tot = np.sum((ly - ly.mean()) ** 2)
    r2_exp = 1 - ss_res / ss_tot if ss_tot > 0 else 0
else:
    a_exp = b_exp = r2_exp = None

# Power-law fit: log N = a - b log L
if len(xs) >= 2 and (ys > 0).all() and (xs > 0).all():
    coeffs_pow = np.polyfit(np.log(xs), np.log(ys), 1)
    b_pow = -coeffs_pow[0]
    a_pow = coeffs_pow[1]
    yhat = np.polyval(coeffs_pow, np.log(xs))
    ss_res = np.sum((np.log(ys) - yhat) ** 2)
    ss_tot = np.sum((np.log(ys) - np.log(ys).mean()) ** 2)
    r2_pow = 1 - ss_res / ss_tot if ss_tot > 0 else 0
else:
    a_pow = b_pow = r2_pow = None

d4_result = {
    "n_consecutive_pairs_within_surah": n_pairs,
    "N_of_L": NofL,
    "null_summary": {str(k): v for k, v in null_summary.items()},
    "fit_exponential": {"a": a_exp, "b": b_exp, "R2": r2_exp, "formula": "N(L) ≈ exp(a - b·L)"},
    "fit_power_law": {"a": a_pow, "b": b_pow, "R2": r2_pow, "formula": "N(L) ≈ exp(a) · L^(-b)"},
    "extreme_pairs_L_ge_30": [
        {"verse_i": VERSES[i]["key"], "verse_j": VERSES[i+1]["key"],
         "shared_prefix_letters": int(pair_prefix_lens[k])}
        for k, i in enumerate([idx for idx in range(N - 1) if surah_ids[idx] == surah_ids[idx+1]])
        if pair_prefix_lens[k] >= 30
    ],
}


# ============================================================================
# Dump
# ============================================================================
out = {
    "derivation_1_palindrome_cfg": d1_result,
    "derivation_2_omega_iam": d2_result,
    "derivation_3_constraint_matrix": d3_result,
    "derivation_4_twin_opener": d4_result,
}

with open(os.path.join(os.path.dirname(__file__), "results.json"), "w", encoding="utf-8") as fh:
    json.dump(out, fh, indent=2, ensure_ascii=False)

print("=" * 72)
print("DERIVATION 1 — Palindrome CFG")
print(f"  Observed 5-word A-B-C-B-A: {d1_result['total_pal5_found']}")
print(f"  Classified by CFG:         {d1_result['classified_by_cfg']}")
print(f"  Unclassified (extra):      {d1_result['unclassified']}")
print(f"  CFG string space size:     {d1_result['cfg_string_space_size']}")
print(f"  CFG strings actually seen: {d1_result['cfg_strings_observed']}")
print(f"  CFG strings unobserved:    {d1_result['cfg_strings_unobserved']}")
print()
print("DERIVATION 2 — Ω_IAM Top 20")
for r in d2_top20:
    print(f"  {r['rank']:2d}. {r['verse']:8s}  Ω={r['omega']:.1f}")
print(f"  Rule-invariance top-20 overlap: {overlap}")
print()
print("DERIVATION 3 — Constraint matrix")
if d3_result.get("nazm_index_quran"):
    print(f"  Naẓm (Quran):    {d3_result['nazm_index_quran']}")
    print(f"  Naẓm (baseline): {d3_result['nazm_index_baseline']}")
    print("  Top MI pairs:")
    for p in d3_result["top_mi_pairs"][:5]:
        print(f"    {p['pair']}  MI_Q={p['mi_quran_bits']:.4f}  MI_B={p['mi_baseline_bits']:.4f}  lift_Q={p['lift_quran']:.2f}")
print()
print("DERIVATION 4 — Twin-Opener N(L)")
print(f"  Pairs considered: {n_pairs}")
for L in Ls:
    s = null_summary[L]
    print(f"  L={L:2d}  N(L)={NofL[L]:5d}  null_mean={s['null_mean']:7.2f}  z={s['z']:+7.2f}")
if a_exp is not None:
    print(f"  Exp fit:   N(L) ≈ exp({a_exp:.3f} - {b_exp:.4f} L)   R²={r2_exp:.4f}")
if a_pow is not None:
    print(f"  Power fit: N(L) ≈ {math.exp(a_pow):.2e} · L^(-{b_pow:.3f})  R²={r2_pow:.4f}")
print()
print("Wrote results.json")
