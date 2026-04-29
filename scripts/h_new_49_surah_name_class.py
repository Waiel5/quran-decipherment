"""H-NEW-49 — Surah-name semantic classification.

Pre-reg: findings/phase-b-hypotheses/h-new-49-surah-name-class-prereg.md

Tests:
  Cell 1 — Class-distribution baseline (descriptive)
  Cell 2 — Muqaṭṭaʿāt vs name-class χ²
  Cell 3 — MUQATTAAT_LETTER class enrichment in muqaṭṭaʿāt-openers (MW-5 tautology)
  Cell 4 — Khawātim al-Ḥashr / mufaṣṣal divine-attribute enrichment Fisher exact
  Cell 5 — Lexical centrality of name-root in surah text

Seed: 20260416 ; Bonferroni k=5 ; α_bon = 0.01
"""
from __future__ import annotations

import json
import math
import os
import random
import sys
from collections import Counter
from typing import Dict, List, Tuple

REPO = "/Users/grey/Downloads/quran"
sys.path.insert(0, os.path.join(REPO, "analysis"))

from tools.loader import load_quran  # noqa: E402
from tools.tokenize import real_words  # noqa: E402

SEED = 20260416
N_PERM = 100_000
BON_K = 5
ALPHA_BON = 0.05 / BON_K  # 0.01
N_SURAHS = 114

# From H-NEW-46 (locked elsewhere)
MUQ_SURAHS = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
              36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
assert len(MUQ_SURAHS) == 29

# Locked taxonomy classes
CLASSES = [
    "PROPHET_PERSON",
    "ANIMAL_OBJECT",
    "DIVINE_ATTRIBUTE",
    "COSMOLOGICAL_NATURAL",
    "EVENT_ESCHATOLOGICAL",
    "SOCIAL_LEGAL",
    "REVELATION_RITUAL",
    "MUQATTAAT_LETTER",
    "OTHER_ABSTRACT",
]

# ============================================================================
# LOCKED CLASSIFICATION (from pre-reg principles, applied to canonical 114)
# Each (surah_id, transliteration_short, english_gloss, class, root_consonants)
# root_consonants = list of acceptable consonant skeletons (strings of Arabic
# letters in unvocalized form) that count as a "name-root match" for Cell 5.
# Empty list means Cell 5 not testable for that surah.
# ============================================================================
SURAH_CLASS: Dict[int, Tuple[str, str, str, List[str]]] = {
    1:  ("Al-Fatihah",     "the Opening",        "REVELATION_RITUAL",   ["فتح"]),
    2:  ("Al-Baqarah",     "the Cow",            "ANIMAL_OBJECT",       ["بقر"]),
    3:  ("Al-Imran",       "the Family of Imran","PROPHET_PERSON",      ["عمرن"]),
    4:  ("An-Nisa",        "the Women",          "SOCIAL_LEGAL",        ["نسا", "نسو"]),
    5:  ("Al-Maidah",      "the Table-spread",   "ANIMAL_OBJECT",       ["مايد", "ميد"]),
    6:  ("Al-Anam",        "the Cattle",         "ANIMAL_OBJECT",       ["نعم"]),
    7:  ("Al-Araf",        "the Heights",        "COSMOLOGICAL_NATURAL",["عرف"]),
    8:  ("Al-Anfal",       "the Spoils",         "SOCIAL_LEGAL",        ["نفل"]),
    9:  ("At-Tawbah",      "the Repentance",     "REVELATION_RITUAL",   ["توب"]),
    10: ("Yunus",          "Jonah",              "PROPHET_PERSON",      ["يونس"]),
    11: ("Hud",            "Hud",                "PROPHET_PERSON",      ["هود"]),
    12: ("Yusuf",          "Joseph",             "PROPHET_PERSON",      ["يوسف"]),
    13: ("Ar-Rad",         "the Thunder",        "COSMOLOGICAL_NATURAL",["رعد"]),
    14: ("Ibrahim",        "Abraham",            "PROPHET_PERSON",      ["ابرهيم", "إبرهيم"]),
    15: ("Al-Hijr",        "the Rocky Tract",    "COSMOLOGICAL_NATURAL",["حجر"]),
    16: ("An-Nahl",        "the Bee",            "ANIMAL_OBJECT",       ["نحل"]),
    17: ("Al-Isra",        "the Night Journey",  "REVELATION_RITUAL",   ["سرى", "اسر"]),
    18: ("Al-Kahf",        "the Cave",           "REVELATION_RITUAL",   ["كهف"]),
    19: ("Maryam",         "Mary",               "PROPHET_PERSON",      ["مريم"]),
    20: ("Ta-Ha",          "Ta-Ha",              "MUQATTAAT_LETTER",    []),
    21: ("Al-Anbiya",      "the Prophets",       "PROPHET_PERSON",      ["نبا", "نبي"]),
    22: ("Al-Hajj",        "the Pilgrimage",     "REVELATION_RITUAL",   ["حجج", "حج"]),
    23: ("Al-Muminun",     "the Believers",      "SOCIAL_LEGAL",        ["امن", "ءمن"]),
    24: ("An-Nur",         "the Light",          "DIVINE_ATTRIBUTE",    ["نور"]),
    25: ("Al-Furqan",      "the Criterion",      "REVELATION_RITUAL",   ["فرق"]),
    26: ("Ash-Shuara",     "the Poets",          "SOCIAL_LEGAL",        ["شعر"]),
    27: ("An-Naml",        "the Ant",            "ANIMAL_OBJECT",       ["نمل"]),
    28: ("Al-Qasas",       "the Stories",        "REVELATION_RITUAL",   ["قصص", "قص"]),
    29: ("Al-Ankabut",     "the Spider",         "ANIMAL_OBJECT",       ["عنكب"]),
    30: ("Ar-Rum",         "the Romans",         "SOCIAL_LEGAL",        ["روم"]),
    31: ("Luqman",         "Luqman",             "PROPHET_PERSON",      ["لقمن"]),
    32: ("As-Sajdah",      "the Prostration",    "REVELATION_RITUAL",   ["سجد"]),
    33: ("Al-Ahzab",       "the Confederates",   "SOCIAL_LEGAL",        ["حزب"]),
    34: ("Saba",           "Sheba",              "PROPHET_PERSON",      ["سبا"]),
    35: ("Fatir",          "the Originator",     "DIVINE_ATTRIBUTE",    ["فطر"]),
    36: ("Ya-Sin",         "Ya-Sin",             "MUQATTAAT_LETTER",    []),
    37: ("As-Saffat",      "the Ranks",          "SOCIAL_LEGAL",        ["صفف", "صف"]),
    38: ("Sad",            "Sad",                "MUQATTAAT_LETTER",    []),
    39: ("Az-Zumar",       "the Groups",         "SOCIAL_LEGAL",        ["زمر"]),
    40: ("Ghafir",         "the Forgiver",       "DIVINE_ATTRIBUTE",    ["غفر"]),
    41: ("Fussilat",       "Explained in Detail","REVELATION_RITUAL",   ["فصل"]),
    42: ("Ash-Shura",      "the Consultation",   "SOCIAL_LEGAL",        ["شور"]),
    43: ("Az-Zukhruf",     "the Gold Adornments","ANIMAL_OBJECT",       ["زخرف"]),
    44: ("Ad-Dukhan",      "the Smoke",          "COSMOLOGICAL_NATURAL",["دخن"]),
    45: ("Al-Jathiyah",    "the Kneeling",       "EVENT_ESCHATOLOGICAL",["جثو", "جثا"]),
    46: ("Al-Ahqaf",       "the Sand-dunes",     "COSMOLOGICAL_NATURAL",["حقف"]),
    47: ("Muhammad",       "Muhammad",           "PROPHET_PERSON",      ["محمد"]),
    48: ("Al-Fath",        "the Victory",        "EVENT_ESCHATOLOGICAL",["فتح"]),
    49: ("Al-Hujurat",     "the Chambers",       "SOCIAL_LEGAL",        ["حجر"]),
    50: ("Qaf",            "Qaf",                "MUQATTAAT_LETTER",    []),
    51: ("Adh-Dhariyat",   "the Scatterers",     "COSMOLOGICAL_NATURAL",["ذرو", "ذري"]),
    52: ("At-Tur",         "the Mount",          "COSMOLOGICAL_NATURAL",["طور"]),
    53: ("An-Najm",        "the Star",           "COSMOLOGICAL_NATURAL",["نجم"]),
    54: ("Al-Qamar",       "the Moon",           "COSMOLOGICAL_NATURAL",["قمر"]),
    55: ("Ar-Rahman",      "the Most Merciful",  "DIVINE_ATTRIBUTE",    ["رحمن", "رحم"]),
    56: ("Al-Waqiah",      "the Inevitable",     "EVENT_ESCHATOLOGICAL",["وقع"]),
    57: ("Al-Hadid",       "the Iron",           "ANIMAL_OBJECT",       ["حديد", "حدد"]),
    58: ("Al-Mujadilah",   "the Pleading Woman", "SOCIAL_LEGAL",        ["جدل"]),
    59: ("Al-Hashr",       "the Gathering",      "EVENT_ESCHATOLOGICAL",["حشر"]),
    60: ("Al-Mumtahanah",  "the Examined Woman", "SOCIAL_LEGAL",        ["محن"]),
    61: ("As-Saff",        "the Ranks",          "SOCIAL_LEGAL",        ["صف", "صفف"]),
    62: ("Al-Jumuah",      "the Friday",         "REVELATION_RITUAL",   ["جمع"]),
    63: ("Al-Munafiqun",   "the Hypocrites",     "SOCIAL_LEGAL",        ["نفق"]),
    64: ("At-Taghabun",    "Mutual Loss-Gain",   "EVENT_ESCHATOLOGICAL",["غبن"]),
    65: ("At-Talaq",       "the Divorce",        "SOCIAL_LEGAL",        ["طلق"]),
    66: ("At-Tahrim",      "the Prohibition",    "SOCIAL_LEGAL",        ["حرم"]),
    67: ("Al-Mulk",        "the Sovereignty",    "DIVINE_ATTRIBUTE",    ["ملك"]),
    68: ("Al-Qalam",       "the Pen",            "ANIMAL_OBJECT",       ["قلم"]),
    69: ("Al-Haqqah",      "the Reality",        "EVENT_ESCHATOLOGICAL",["حق"]),
    70: ("Al-Maarij",      "the Ascending",      "COSMOLOGICAL_NATURAL",["عرج"]),
    71: ("Nuh",            "Noah",               "PROPHET_PERSON",      ["نوح"]),
    72: ("Al-Jinn",        "the Jinn",           "OTHER_ABSTRACT",      ["جن"]),
    73: ("Al-Muzzammil",   "the Enwrapped",      "REVELATION_RITUAL",   ["زمل"]),
    74: ("Al-Muddaththir", "the Cloaked",        "REVELATION_RITUAL",   ["دثر"]),
    75: ("Al-Qiyamah",     "the Resurrection",   "EVENT_ESCHATOLOGICAL",["قوم", "قيم"]),
    76: ("Al-Insan",       "Man",                "SOCIAL_LEGAL",        ["انس", "ءنس"]),
    77: ("Al-Mursalat",    "Those Sent Forth",   "EVENT_ESCHATOLOGICAL",["رسل"]),
    78: ("An-Naba",        "the Tidings",        "EVENT_ESCHATOLOGICAL",["نبا"]),
    79: ("An-Naziat",      "Those who Pull Out", "EVENT_ESCHATOLOGICAL",["نزع"]),
    80: ("Abasa",          "He Frowned",         "EVENT_ESCHATOLOGICAL",["عبس"]),
    81: ("At-Takwir",      "the Folding Up",     "EVENT_ESCHATOLOGICAL",["كور"]),
    82: ("Al-Infitar",     "the Cleaving",       "EVENT_ESCHATOLOGICAL",["فطر"]),
    83: ("Al-Mutaffifin",  "the Defrauders",     "SOCIAL_LEGAL",        ["طفف"]),
    84: ("Al-Inshiqaq",    "the Splitting",      "EVENT_ESCHATOLOGICAL",["شقق", "شق"]),
    85: ("Al-Buruj",       "the Constellations", "COSMOLOGICAL_NATURAL",["برج"]),
    86: ("At-Tariq",       "the Night-comer",    "COSMOLOGICAL_NATURAL",["طرق"]),
    87: ("Al-Ala",         "the Most High",      "DIVINE_ATTRIBUTE",    ["علو", "علا"]),
    88: ("Al-Ghashiyah",   "the Overwhelming",   "EVENT_ESCHATOLOGICAL",["غشو", "غشي"]),
    89: ("Al-Fajr",        "the Dawn",           "COSMOLOGICAL_NATURAL",["فجر"]),
    90: ("Al-Balad",       "the City",           "COSMOLOGICAL_NATURAL",["بلد"]),
    91: ("Ash-Shams",      "the Sun",            "COSMOLOGICAL_NATURAL",["شمس"]),
    92: ("Al-Layl",        "the Night",          "COSMOLOGICAL_NATURAL",["ليل"]),
    93: ("Ad-Duha",        "the Forenoon",       "COSMOLOGICAL_NATURAL",["ضحى", "ضحو"]),
    94: ("Ash-Sharh",      "the Opening Forth",  "REVELATION_RITUAL",   ["شرح"]),
    95: ("At-Tin",         "the Fig",            "ANIMAL_OBJECT",       ["تين"]),
    96: ("Al-Alaq",        "the Clot",           "REVELATION_RITUAL",   ["علق"]),
    97: ("Al-Qadr",        "the Decree",         "REVELATION_RITUAL",   ["قدر"]),
    98: ("Al-Bayyinah",    "the Clear Proof",    "REVELATION_RITUAL",   ["بين"]),
    99: ("Az-Zalzalah",    "the Earthquake",     "EVENT_ESCHATOLOGICAL",["زلزل", "زلز"]),
    100:("Al-Adiyat",      "the Chargers",       "ANIMAL_OBJECT",       ["عدو", "عدا"]),
    101:("Al-Qariah",      "the Striking Calamity","EVENT_ESCHATOLOGICAL",["قرع"]),
    102:("At-Takathur",    "the Multiplication", "OTHER_ABSTRACT",      ["كثر"]),
    103:("Al-Asr",         "the Time",           "COSMOLOGICAL_NATURAL",["عصر"]),
    104:("Al-Humazah",     "the Slanderer",      "SOCIAL_LEGAL",        ["همز"]),
    105:("Al-Fil",         "the Elephant",       "ANIMAL_OBJECT",       ["فيل"]),
    106:("Quraysh",        "Quraysh",            "SOCIAL_LEGAL",        ["قريش"]),
    107:("Al-Maun",        "the Small Kindnesses","REVELATION_RITUAL",  ["معن", "ماعون"]),
    108:("Al-Kawthar",     "the Abundance",      "OTHER_ABSTRACT",      ["كثر", "كوثر"]),
    109:("Al-Kafirun",     "the Disbelievers",   "SOCIAL_LEGAL",        ["كفر"]),
    110:("An-Nasr",        "the Help",           "EVENT_ESCHATOLOGICAL",["نصر"]),
    111:("Al-Masad",       "the Palm Fibre",     "ANIMAL_OBJECT",       ["مسد"]),
    112:("Al-Ikhlas",      "the Sincerity",      "DIVINE_ATTRIBUTE",    ["خلص", "احد"]),
    113:("Al-Falaq",       "the Daybreak",       "COSMOLOGICAL_NATURAL",["فلق"]),
    114:("An-Nas",         "Mankind",            "SOCIAL_LEGAL",        ["نوس", "ناس"]),
}
assert len(SURAH_CLASS) == 114

# ============================================================================
# Statistical helpers
# ============================================================================

def chi2_p(chi2: float, df: int) -> float:
    """Chi-square upper-tail p via series expansion (no scipy)."""
    if df <= 0 or chi2 < 0:
        return 1.0
    # Use regularized upper incomplete gamma Q(df/2, chi2/2)
    # Compute via series for lower then 1 - P
    a = df / 2.0
    x = chi2 / 2.0
    if x == 0:
        return 1.0
    # Series for P(a,x) when x < a+1, otherwise continued fraction for Q
    if x < a + 1.0:
        # Series
        ap = a
        s = 1.0 / a
        term = s
        for _ in range(1000):
            ap += 1.0
            term *= x / ap
            s += term
            if abs(term) < abs(s) * 1e-15:
                break
        # P(a,x) = s * exp(-x + a*ln(x) - lgamma(a))
        log_p = -x + a * math.log(x) - math.lgamma(a)
        P = s * math.exp(log_p)
        return max(0.0, min(1.0, 1.0 - P))
    else:
        # Continued fraction for Q
        b = x + 1.0 - a
        c = 1.0 / 1e-300
        d = 1.0 / b
        h = d
        for i in range(1, 1000):
            an = -i * (i - a)
            b += 2.0
            d = an * d + b
            if abs(d) < 1e-300:
                d = 1e-300
            c = b + an / c
            if abs(c) < 1e-300:
                c = 1e-300
            d = 1.0 / d
            delta = d * c
            h *= delta
            if abs(delta - 1.0) < 1e-15:
                break
        log_q = -x + a * math.log(x) - math.lgamma(a)
        Q = h * math.exp(log_q)
        return max(0.0, min(1.0, Q))


def chi_square_test(observed: List[List[float]]) -> Tuple[float, int, float, List[List[float]]]:
    """Standard Pearson χ² for a contingency table.

    Returns (chi2, df, p, expected).
    """
    rows = len(observed)
    cols = len(observed[0]) if rows else 0
    row_tot = [sum(r) for r in observed]
    col_tot = [sum(observed[i][j] for i in range(rows)) for j in range(cols)]
    grand = sum(row_tot)
    if grand == 0:
        return (0.0, 0, 1.0, observed)
    expected = [[row_tot[i] * col_tot[j] / grand for j in range(cols)]
                for i in range(rows)]
    chi2 = 0.0
    for i in range(rows):
        for j in range(cols):
            e = expected[i][j]
            if e > 0:
                chi2 += (observed[i][j] - e) ** 2 / e
    df = (rows - 1) * (cols - 1)
    p = chi2_p(chi2, df)
    return (chi2, df, p, expected)


def fisher_exact_2x2(a: int, b: int, c: int, d: int) -> float:
    """Two-sided Fisher exact for 2x2 table [[a,b],[c,d]]."""
    n = a + b + c + d
    r1 = a + b
    c1 = a + c
    # hypergeom probability: P(X=k) = C(r1,k) * C(n-r1, c1-k) / C(n, c1)
    def logC(N, K):
        if K < 0 or K > N:
            return -float("inf")
        return math.lgamma(N + 1) - math.lgamma(K + 1) - math.lgamma(N - K + 1)
    log_denom = logC(n, c1)
    def logP(k):
        return logC(r1, k) + logC(n - r1, c1 - k) - log_denom
    obs = logP(a)
    # sum over all k whose logP <= obs (two-sided)
    kmin = max(0, c1 - (n - r1))
    kmax = min(r1, c1)
    p_sum = 0.0
    for k in range(kmin, kmax + 1):
        lp = logP(k)
        if lp <= obs + 1e-12:
            p_sum += math.exp(lp)
    return min(1.0, p_sum)


def binomial_p(k: int, n: int, p: float, one_sided: str = "upper") -> float:
    """One-sided binomial tail."""
    if n == 0:
        return 1.0
    if one_sided == "upper":
        # P(X >= k)
        s = 0.0
        for j in range(k, n + 1):
            s += math.exp(math.lgamma(n + 1) - math.lgamma(j + 1) - math.lgamma(n - j + 1)
                          + j * math.log(p) + (n - j) * math.log(1 - p) if 0 < p < 1 else 0.0)
        return min(1.0, s)
    else:
        s = 0.0
        for j in range(0, k + 1):
            s += math.exp(math.lgamma(n + 1) - math.lgamma(j + 1) - math.lgamma(n - j + 1)
                          + j * math.log(p) + (n - j) * math.log(1 - p) if 0 < p < 1 else 0.0)
        return min(1.0, s)


# ============================================================================
# Cell 1 — class distribution
# ============================================================================

def cell1_class_distribution() -> Dict[str, int]:
    counts: Counter = Counter()
    for sid in range(1, N_SURAHS + 1):
        cls = SURAH_CLASS[sid][2]
        counts[cls] += 1
    return {c: counts.get(c, 0) for c in CLASSES}


# ============================================================================
# Cell 2 — muqaṭṭaʿāt vs name-class χ²
# ============================================================================

def cell2_muqattaat_vs_class() -> dict:
    # 2 x K table: muqaṭṭaʿāt(Y/N) x classes
    table_y = []
    table_n = []
    for c in CLASSES:
        ny = sum(1 for sid in range(1, N_SURAHS + 1)
                 if SURAH_CLASS[sid][2] == c and sid in MUQ_SURAHS)
        nn = sum(1 for sid in range(1, N_SURAHS + 1)
                 if SURAH_CLASS[sid][2] == c and sid not in MUQ_SURAHS)
        table_y.append(ny)
        table_n.append(nn)

    # Pre-registered pooling rule: pool low-expected classes in fixed order
    # (OTHER_ABSTRACT, MUQATTAAT_LETTER, REVELATION_RITUAL) IF expected < 5.
    # First test full table; if min expected < 5, pool.
    obs = [list(table_y), list(table_n)]
    chi2, df, p, exp = chi_square_test(obs)
    min_exp = min(min(row) for row in exp)
    pooled_classes = list(CLASSES)
    if min_exp < 5.0:
        # Pool last three locked categories
        pool_idx = [CLASSES.index("OTHER_ABSTRACT"),
                    CLASSES.index("MUQATTAAT_LETTER"),
                    CLASSES.index("REVELATION_RITUAL")]
        keep_idx = [i for i in range(len(CLASSES)) if i not in pool_idx]
        # Build pooled table
        new_y, new_n, new_classes = [], [], []
        for i in keep_idx:
            new_y.append(table_y[i])
            new_n.append(table_n[i])
            new_classes.append(CLASSES[i])
        new_y.append(sum(table_y[i] for i in pool_idx))
        new_n.append(sum(table_n[i] for i in pool_idx))
        new_classes.append("POOLED_OTHER")
        obs2 = [new_y, new_n]
        chi2, df, p, exp = chi_square_test(obs2)
        pooled_classes = new_classes
        obs = obs2

    return {
        "table_full_observed_yes": list(table_y),
        "table_full_observed_no": list(table_n),
        "classes_full": list(CLASSES),
        "table_used_observed_yes": obs[0],
        "table_used_observed_no": obs[1],
        "classes_used": pooled_classes,
        "expected": exp,
        "chi2": chi2,
        "df": df,
        "p": p,
    }


# ============================================================================
# Cell 3 — MUQATTAAT_LETTER class permutation
# ============================================================================

def cell3_muqattaat_letter_perm(rng: random.Random) -> dict:
    # 4 surahs in MUQATTAAT_LETTER class: Q20, Q36, Q38, Q50
    ml_surahs = [sid for sid in range(1, N_SURAHS + 1)
                 if SURAH_CLASS[sid][2] == "MUQATTAAT_LETTER"]
    obs = sum(1 for sid in ml_surahs if sid in MUQ_SURAHS)
    n_ml = len(ml_surahs)
    # null: permute class labels across 114 surahs; how many of the
    # labels-assigned-to-MUQATTAAT_LETTER (random 4) fall in MUQ_SURAHS?
    all_sids = list(range(1, N_SURAHS + 1))
    hits = 0
    for _ in range(N_PERM):
        sample = rng.sample(all_sids, n_ml)
        c = sum(1 for s in sample if s in MUQ_SURAHS)
        if c >= obs:
            hits += 1
    p = (hits + 1) / (N_PERM + 1)
    return {
        "muqattaat_letter_surahs": ml_surahs,
        "n_in_muqattaat_set": obs,
        "n_total": n_ml,
        "p_one_sided_upper": p,
        "n_perm": N_PERM,
    }


# ============================================================================
# Cell 4 — Khawātim al-Ḥashr / mufaṣṣal divine-attribute enrichment
# ============================================================================

def cell4_khawatim_hashr() -> dict:
    # Sub-test (a): is Q 59 al-Ḥashr name in DIVINE_ATTRIBUTE? Pre-reg: NO.
    q59_class = SURAH_CLASS[59][2]
    pre_reg_pred = "EVENT_ESCHATOLOGICAL"
    sub_a_match = (q59_class == "DIVINE_ATTRIBUTE")

    # Sub-test (b): mufaṣṣal short region Q 50–114 vs long region Q 1–49
    # divine-attribute name fraction: Fisher exact 2x2.
    # rows: region (long Q1-49, short Q50-114); cols: DA (Y/N)
    long_da = sum(1 for sid in range(1, 50)
                  if SURAH_CLASS[sid][2] == "DIVINE_ATTRIBUTE")
    long_n = 49
    short_da = sum(1 for sid in range(50, 115)
                   if SURAH_CLASS[sid][2] == "DIVINE_ATTRIBUTE")
    short_n = 65
    # 2x2 table: [[long_da, long_n - long_da], [short_da, short_n - short_da]]
    p = fisher_exact_2x2(long_da, long_n - long_da, short_da, short_n - short_da)
    return {
        "q59_class": q59_class,
        "q59_pre_reg_prediction": pre_reg_pred,
        "q59_is_divine_attribute": sub_a_match,
        "long_region_da_count": long_da,
        "long_region_n": long_n,
        "short_region_da_count": short_da,
        "short_region_n": short_n,
        "fisher_p_two_sided": p,
    }


# ============================================================================
# Cell 5 — Lexical centrality of name-root
# ============================================================================

def normalize_alif(s: str) -> str:
    """Map alif variants (إ أ آ ا ٱ) to a single bare alif ا for matching."""
    out = []
    for ch in s:
        if ch in "إأآاٱ":
            out.append("ا")
        elif ch == "ى":
            out.append("ى")  # keep alif maqsura distinct? root lists use it
        else:
            out.append(ch)
    return "".join(out)


def root_in_token(root: str, token: str) -> bool:
    """Skeleton-match: do all letters of root appear in token in order?

    Rough proxy for root-detection without a full morphological analyser:
    check whether the root consonants appear as an in-order subsequence
    in the (alif-normalized) token. Strips tatweel/punctuation by relying
    on the loaded no-tashkeel orthography being already mostly clean.
    """
    if not root:
        return False
    root_n = normalize_alif(root)
    tok_n = normalize_alif(token)
    j = 0
    for ch in tok_n:
        if j < len(root_n) and ch == root_n[j]:
            j += 1
            if j == len(root_n):
                return True
    return False


def surah_token_lists(surahs) -> Dict[int, List[str]]:
    out: Dict[int, List[str]] = {}
    for s in surahs:
        toks: List[str] = []
        for v in s.verses:
            toks.extend(real_words(v.text))
        out[s.id] = toks
    return out


def cell5_lexical_centrality(surah_tokens: Dict[int, List[str]]) -> dict:
    per_surah = []
    for sid in range(1, N_SURAHS + 1):
        translit, gloss, cls, roots = SURAH_CLASS[sid]
        if not roots:
            per_surah.append({
                "surah": sid, "translit": translit, "class": cls,
                "testable": False, "reason": "no name-root (muqaṭṭaʿāt-letter or empty)",
            })
            continue
        tokens_in = surah_tokens[sid]
        n_in = len(tokens_in)
        hits_in = sum(1 for t in tokens_in
                      if any(root_in_token(r, t) for r in roots))
        # Corpus-rest baseline
        n_rest = 0
        hits_rest = 0
        for sid2 in range(1, N_SURAHS + 1):
            if sid2 == sid:
                continue
            for t in surah_tokens[sid2]:
                n_rest += 1
                if any(root_in_token(r, t) for r in roots):
                    hits_rest += 1
        p_rest = hits_rest / n_rest if n_rest else 0.0
        rate_in = hits_in / n_in if n_in else 0.0
        # One-sided binomial p: P(X >= hits_in | n_in, p_rest)
        if 0 < p_rest < 1 and n_in > 0:
            # Use sum of log-pmf
            log_pmf_terms = []
            for j in range(hits_in, n_in + 1):
                lp = (math.lgamma(n_in + 1) - math.lgamma(j + 1) - math.lgamma(n_in - j + 1)
                      + j * math.log(p_rest) + (n_in - j) * math.log(1 - p_rest))
                log_pmf_terms.append(lp)
            # sum exp safely
            if log_pmf_terms:
                lmax = max(log_pmf_terms)
                p = math.exp(lmax) * sum(math.exp(lp - lmax) for lp in log_pmf_terms)
                p = min(1.0, p)
            else:
                p = 1.0
        elif p_rest == 0 and hits_in > 0:
            p = 0.0
        else:
            p = 1.0
        per_surah.append({
            "surah": sid, "translit": translit, "class": cls,
            "testable": True,
            "roots": roots,
            "n_tokens": n_in,
            "hits": hits_in,
            "rate_in": rate_in,
            "rate_rest": p_rest,
            "ratio": (rate_in / p_rest) if p_rest > 0 else float("inf"),
            "p_one_sided": p,
        })
    n_test = sum(1 for r in per_surah if r["testable"])
    alpha_within = ALPHA_BON / n_test if n_test else 1.0
    n_sig = sum(1 for r in per_surah if r["testable"] and r["p_one_sided"] < alpha_within)
    return {
        "n_testable": n_test,
        "alpha_per_surah_bonferroni": alpha_within,
        "n_sig": n_sig,
        "frac_sig": n_sig / n_test if n_test else 0.0,
        "verdict": ("STRONG-PASS" if n_sig >= 2 * n_test / 3
                    else ("PASS" if n_sig >= n_test / 3
                          else ("EXPLORATORY" if n_sig > 0 else "NULL"))),
        "per_surah": per_surah,
    }


# ============================================================================
# Driver
# ============================================================================

def main():
    print(f"H-NEW-49 — Surah-name semantic class. Seed={SEED}, Bon-k={BON_K}, α_bon={ALPHA_BON}")
    rng = random.Random(SEED)
    surahs = load_quran("no-tashkeel")
    assert len(surahs) == N_SURAHS
    surah_tokens = surah_token_lists(surahs)

    # Cell 1
    c1 = cell1_class_distribution()
    print("\nCell 1 — Class distribution:")
    for cls in CLASSES:
        print(f"  {cls:25s} {c1[cls]:3d}")

    # Cell 2
    c2 = cell2_muqattaat_vs_class()
    print(f"\nCell 2 — muq×class χ² = {c2['chi2']:.3f}, df={c2['df']}, p={c2['p']:.6f}")
    print(f"  Classes used: {c2['classes_used']}")
    print(f"  Yes: {c2['table_used_observed_yes']}")
    print(f"  No:  {c2['table_used_observed_no']}")

    # Cell 3
    c3 = cell3_muqattaat_letter_perm(rng)
    print(f"\nCell 3 — MUQATTAAT_LETTER permutation: {c3['n_in_muqattaat_set']}/{c3['n_total']} hits, p={c3['p_one_sided_upper']:.6f}")

    # Cell 4
    c4 = cell4_khawatim_hashr()
    print(f"\nCell 4 — Q59 class={c4['q59_class']} (pre-reg pred {c4['q59_pre_reg_prediction']})")
    print(f"  Long Q1-49 DA: {c4['long_region_da_count']}/{c4['long_region_n']}; "
          f"Short Q50-114 DA: {c4['short_region_da_count']}/{c4['short_region_n']}; "
          f"Fisher p={c4['fisher_p_two_sided']:.6f}")

    # Cell 5
    c5 = cell5_lexical_centrality(surah_tokens)
    print(f"\nCell 5 — Lexical centrality: {c5['n_sig']}/{c5['n_testable']} surahs sig (α_per_surah={c5['alpha_per_surah_bonferroni']:.2e}); verdict={c5['verdict']}")

    # MW-5: check Q71 Nūḥ
    nuh = next(r for r in c5["per_surah"] if r["surah"] == 71)
    print(f"\nMW-5 control (Q71 Nūḥ): n={nuh['n_tokens']} hits={nuh['hits']} rate_in={nuh['rate_in']:.4f} rate_rest={nuh['rate_rest']:.6f} ratio={nuh['ratio']:.1f} p={nuh['p_one_sided']:.2e}")

    # Save output
    os.makedirs(os.path.join(REPO, "findings/phase-b-hypotheses/csv"), exist_ok=True)
    out_path = os.path.join(REPO, "findings/phase-b-hypotheses/csv/h-new-49.json")
    out = {
        "id": "H-NEW-49",
        "seed": SEED,
        "bonferroni_k": BON_K,
        "alpha_bon": ALPHA_BON,
        "rules_tuple": "(hafs-kufan; no-tashkeel; canonical 114; 29-muqaṭṭaʿāt set)",
        "n_surahs": N_SURAHS,
        "n_muqattaat_openers": len(MUQ_SURAHS),
        "muqattaat_set": sorted(MUQ_SURAHS),
        "classes": CLASSES,
        "surah_class_assignments": {
            str(sid): {"translit": SURAH_CLASS[sid][0], "gloss": SURAH_CLASS[sid][1],
                       "class": SURAH_CLASS[sid][2], "roots": SURAH_CLASS[sid][3]}
            for sid in range(1, N_SURAHS + 1)
        },
        "cell1_class_distribution": c1,
        "cell2_muqattaat_vs_class": c2,
        "cell3_muqattaat_letter_perm": c3,
        "cell4_khawatim_hashr_mufassal": c4,
        "cell5_lexical_centrality": c5,
    }
    with open(out_path, "w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, ensure_ascii=False)
    print(f"\nSaved -> {out_path}")


if __name__ == "__main__":
    main()
