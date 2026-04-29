"""H-NEW-86 — Surah-name-as-key-root, full 114 scan with proper morphology.

Pre-reg: findings/phase-b-hypotheses/h-new-86-surah-name-as-key-root-prereg.md

Method: For each surah, count Leeds-tagged tokens whose ROOT (or LEM for
proper-noun surahs) equals the surah-name's locked target. Per-surah
hypergeometric two-sided test, Bonferroni-114, plus 5 stratifications
(muqaṭṭaʿāt, taxonomy class, PN-vs-noun, Meccan/Medinan, length quartile).

Seed: 20260417 ; Bonferroni k=114 ; α_bon = 4.39e-4
"""
from __future__ import annotations

import csv
import json
import math
import os
import re
import sys
from collections import Counter, defaultdict
from typing import Dict, List, Optional, Tuple

REPO = "/Users/grey/Downloads/quran"
sys.path.insert(0, os.path.join(REPO, "analysis"))

from tools.loader import load_quran  # noqa: E402

SEED = 20260417
N_SURAHS = 114
BON_K = 114
ALPHA_BON = 0.05 / BON_K  # 4.39e-4
ALPHA_STRAT_BON = 0.05 / 5  # 0.01

# Locked muqaṭṭaʿāt-opener set (29 surahs; from H-NEW-44 etc.)
MUQ_SURAHS = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
              36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
assert len(MUQ_SURAHS) == 29

# H-NEW-49 locked taxonomy classes (re-used here)
CLASSES = [
    "PROPHET_PERSON", "ANIMAL_OBJECT", "DIVINE_ATTRIBUTE",
    "COSMOLOGICAL_NATURAL", "EVENT_ESCHATOLOGICAL", "SOCIAL_LEGAL",
    "REVELATION_RITUAL", "MUQATTAAT_LETTER", "OTHER_ABSTRACT",
]

# ============================================================================
# LOCKED ROOT/LEMMA MAPPING — 114 surahs
# (translit, gloss, class, type, target_buckwalter, notes)
# type: "ROOT" → use Leeds ROOT field; "LEM" → use Leeds LEM field; "NONE" → skip
# target_buckwalter is the Leeds Buckwalter encoded root or lemma string.
# ============================================================================
SURAH_MAP: Dict[int, Tuple[str, str, str, str, Optional[str], str]] = {
    1:   ("Al-Fatihah",     "the Opening",            "REVELATION_RITUAL",   "ROOT", "ftH",     "fath = opening"),
    2:   ("Al-Baqarah",     "the Cow",                "ANIMAL_OBJECT",       "ROOT", "bqr",     "baqar = cow"),
    3:   ("Aal-Imran",      "the Family of Imran",    "PROPHET_PERSON",      "LEM",  "Eimora`n","Imran is a PN"),
    4:   ("An-Nisa",        "the Women",              "SOCIAL_LEGAL",        "ROOT", "nsw",     "nisaa = women, root n-s-w"),
    5:   ("Al-Maidah",      "the Table-Spread",       "ANIMAL_OBJECT",       "ROOT", "myd",     "maidah = table, root m-y-d"),
    6:   ("Al-Anam",        "the Cattle",             "ANIMAL_OBJECT",       "ROOT", "nEm",     "anaam = cattle, root n-E-m"),
    7:   ("Al-Araf",        "the Heights",            "COSMOLOGICAL_NATURAL","ROOT", "Erf",     "aaraaf = heights, root E-r-f"),
    8:   ("Al-Anfal",       "the Spoils",             "SOCIAL_LEGAL",        "ROOT", "nfl",     "anfaal = spoils, root n-f-l"),
    9:   ("At-Tawbah",      "the Repentance",         "REVELATION_RITUAL",   "ROOT", "twb",     "tawbah = repentance, root t-w-b"),
    10:  ("Yunus",          "Jonah",                  "PROPHET_PERSON",      "LEM",  "yuwnus",  "Yunus PN"),
    11:  ("Hud",            "Hud",                    "PROPHET_PERSON",      "LEM",  "huwd",    "Hud PN; Leeds has huwd and huwd2"),
    12:  ("Yusuf",          "Joseph",                 "PROPHET_PERSON",      "LEM",  "yuwsuf",  "Yusuf PN"),
    13:  ("Ar-Rad",         "the Thunder",            "COSMOLOGICAL_NATURAL","ROOT", "rEd",     "raad = thunder"),
    14:  ("Ibrahim",        "Abraham",                "PROPHET_PERSON",      "LEM",  "<iboraAhiym","Ibrahim PN"),
    15:  ("Al-Hijr",        "the Rocky Tract",        "COSMOLOGICAL_NATURAL","ROOT", "Hjr",     "hijr = stone/rocky tract"),
    16:  ("An-Nahl",        "the Bee",                "ANIMAL_OBJECT",       "ROOT", "nHl",     "nahl = bee"),
    17:  ("Al-Isra",        "the Night Journey",      "REVELATION_RITUAL",   "ROOT", "sry",     "israa = night journey, root s-r-y"),
    18:  ("Al-Kahf",        "the Cave",               "REVELATION_RITUAL",   "ROOT", "khf",     "kahf = cave"),
    19:  ("Maryam",         "Mary",                   "PROPHET_PERSON",      "LEM",  "maroyam", "Maryam PN"),
    20:  ("Ta-Ha",          "Ta-Ha",                  "MUQATTAAT_LETTER",    "NONE", None,      "muqattaat letter"),
    21:  ("Al-Anbiya",      "the Prophets",           "PROPHET_PERSON",      "ROOT", "nbA",     "anbiyaa = prophets, root n-b-A"),
    22:  ("Al-Hajj",        "the Pilgrimage",         "REVELATION_RITUAL",   "ROOT", "Hjj",     "hajj = pilgrimage"),
    23:  ("Al-Muminun",     "the Believers",          "SOCIAL_LEGAL",        "ROOT", "Amn",     "muminun = believers, root A-m-n"),
    24:  ("An-Nur",         "the Light",              "DIVINE_ATTRIBUTE",    "ROOT", "nwr",     "nur = light"),
    25:  ("Al-Furqan",      "the Criterion",          "REVELATION_RITUAL",   "ROOT", "frq",     "furqaan = criterion"),
    26:  ("Ash-Shuara",     "the Poets",              "SOCIAL_LEGAL",        "ROOT", "$Er",     "shuaraa = poets, root sh-E-r"),
    27:  ("An-Naml",        "the Ant",                "ANIMAL_OBJECT",       "ROOT", "nml",     "naml = ant"),
    28:  ("Al-Qasas",       "the Stories",            "REVELATION_RITUAL",   "ROOT", "qSS",     "qasas = stories"),
    29:  ("Al-Ankabut",     "the Spider",             "ANIMAL_OBJECT",       "ROOT", "Enkb",    "ankabut = spider, root E-n-k-b (4-letter)"),
    30:  ("Ar-Rum",         "the Romans",             "SOCIAL_LEGAL",        "LEM",  "r~uwm",   "Rum is a PN/ethnonym in Leeds"),
    31:  ("Luqman",         "Luqman",                 "PROPHET_PERSON",      "LEM",  "luqoma`n","Luqman PN"),
    32:  ("As-Sajdah",      "the Prostration",        "REVELATION_RITUAL",   "ROOT", "sjd",     "sajdah = prostration"),
    33:  ("Al-Ahzab",       "the Confederates",       "SOCIAL_LEGAL",        "ROOT", "Hzb",     "ahzab = confederates"),
    34:  ("Saba",           "Sheba",                  "PROPHET_PERSON",      "LEM",  "saba<",   "Saba PN"),
    35:  ("Fatir",          "the Originator",         "DIVINE_ATTRIBUTE",    "ROOT", "fTr",     "fatir = originator"),
    36:  ("Ya-Sin",         "Ya-Sin",                 "MUQATTAAT_LETTER",    "NONE", None,      "muqattaat letter"),
    37:  ("As-Saffat",      "the Ranks",              "SOCIAL_LEGAL",        "ROOT", "Sff",     "saffat = ranks"),
    38:  ("Sad",            "Sad",                    "MUQATTAAT_LETTER",    "NONE", None,      "muqattaat letter"),
    39:  ("Az-Zumar",       "the Groups",             "SOCIAL_LEGAL",        "ROOT", "zmr",     "zumar = groups"),
    40:  ("Ghafir",         "the Forgiver",           "DIVINE_ATTRIBUTE",    "ROOT", "gfr",     "ghafir = forgiver"),
    41:  ("Fussilat",       "Explained in Detail",    "REVELATION_RITUAL",   "ROOT", "fSl",     "fussilat = explained in detail"),
    42:  ("Ash-Shura",      "the Consultation",       "SOCIAL_LEGAL",        "ROOT", "$wr",     "shura = consultation"),
    43:  ("Az-Zukhruf",     "the Gold Adornments",    "ANIMAL_OBJECT",       "ROOT", "zxrf",    "zukhruf = gold/adornment, 4-letter root"),
    44:  ("Ad-Dukhan",      "the Smoke",              "COSMOLOGICAL_NATURAL","ROOT", "dxn",     "dukhaan = smoke"),
    45:  ("Al-Jathiyah",    "the Kneeling",           "EVENT_ESCHATOLOGICAL","ROOT", "jvw",     "jathiyah = kneeling, root j-th-w"),
    46:  ("Al-Ahqaf",       "the Sand-Dunes",         "COSMOLOGICAL_NATURAL","ROOT", "Hqf",     "ahqaf = sand-dunes"),
    47:  ("Muhammad",       "Muhammad",               "PROPHET_PERSON",      "LEM",  "muHam~ad","Muhammad PN"),
    48:  ("Al-Fath",        "the Victory",            "EVENT_ESCHATOLOGICAL","ROOT", "ftH",     "fath = victory/opening"),
    49:  ("Al-Hujurat",     "the Chambers",           "SOCIAL_LEGAL",        "ROOT", "Hjr",     "hujurat = chambers, root H-j-r"),
    50:  ("Qaf",            "Qaf",                    "MUQATTAAT_LETTER",    "NONE", None,      "muqattaat letter"),
    51:  ("Adh-Dhariyat",   "the Scatterers",         "COSMOLOGICAL_NATURAL","ROOT", "*rw",     "dhariyat = scatterers, root *-r-w"),
    52:  ("At-Tur",         "the Mount",              "COSMOLOGICAL_NATURAL","ROOT", "Twr",     "tur = mount"),
    53:  ("An-Najm",        "the Star",               "COSMOLOGICAL_NATURAL","ROOT", "njm",     "najm = star"),
    54:  ("Al-Qamar",       "the Moon",               "COSMOLOGICAL_NATURAL","ROOT", "qmr",     "qamar = moon"),
    55:  ("Ar-Rahman",      "the Most Merciful",      "DIVINE_ATTRIBUTE",    "ROOT", "rHm",     "rahman = root r-H-m"),
    56:  ("Al-Waqiah",      "the Inevitable",         "EVENT_ESCHATOLOGICAL","ROOT", "wqE",     "waqiah = the falling/event, root w-q-E"),
    57:  ("Al-Hadid",       "the Iron",               "ANIMAL_OBJECT",       "ROOT", "Hdd",     "hadid = iron"),
    58:  ("Al-Mujadilah",   "the Pleading Woman",     "SOCIAL_LEGAL",        "ROOT", "jdl",     "jadal = dispute"),
    59:  ("Al-Hashr",       "the Gathering",          "EVENT_ESCHATOLOGICAL","ROOT", "H$r",     "hashr = gathering"),
    60:  ("Al-Mumtahanah",  "the Examined Woman",     "SOCIAL_LEGAL",        "ROOT", "mHn",     "mumtahanah = examined, root m-H-n"),
    61:  ("As-Saff",        "the Ranks",              "SOCIAL_LEGAL",        "ROOT", "Sff",     "saff = rank"),
    62:  ("Al-Jumuah",      "the Friday",             "REVELATION_RITUAL",   "ROOT", "jmE",     "jumuah = Friday/gathering, root j-m-E"),
    63:  ("Al-Munafiqun",   "the Hypocrites",         "SOCIAL_LEGAL",        "ROOT", "nfq",     "munafiqun = hypocrites, root n-f-q"),
    64:  ("At-Taghabun",    "Mutual Loss-Gain",       "EVENT_ESCHATOLOGICAL","ROOT", "gbn",     "taghabun = mutual loss"),
    65:  ("At-Talaq",       "the Divorce",            "SOCIAL_LEGAL",        "ROOT", "Tlq",     "talaq = divorce"),
    66:  ("At-Tahrim",      "the Prohibition",        "SOCIAL_LEGAL",        "ROOT", "Hrm",     "tahrim = prohibition, root H-r-m"),
    67:  ("Al-Mulk",        "the Sovereignty",        "DIVINE_ATTRIBUTE",    "ROOT", "mlk",     "mulk = sovereignty"),
    68:  ("Al-Qalam",       "the Pen",                "ANIMAL_OBJECT",       "ROOT", "qlm",     "qalam = pen"),
    69:  ("Al-Haqqah",      "the Reality",            "EVENT_ESCHATOLOGICAL","ROOT", "Hqq",     "haqqah = reality, root H-q-q"),
    70:  ("Al-Maarij",      "the Ascending Stairways","COSMOLOGICAL_NATURAL","ROOT", "Erj",     "maarij = ascending"),
    71:  ("Nuh",            "Noah",                   "PROPHET_PERSON",      "LEM",  "nuwH",    "Nuh PN"),
    72:  ("Al-Jinn",        "the Jinn",               "OTHER_ABSTRACT",      "ROOT", "jnn",     "jinn"),
    73:  ("Al-Muzzammil",   "the Enwrapped",          "REVELATION_RITUAL",   "ROOT", "zml",     "muzzammil = enwrapped"),
    74:  ("Al-Muddaththir", "the Cloaked",            "REVELATION_RITUAL",   "ROOT", "dvr",     "muddaththir = cloaked, root d-th-r"),
    75:  ("Al-Qiyamah",     "the Resurrection",       "EVENT_ESCHATOLOGICAL","ROOT", "qwm",     "qiyamah = resurrection, root q-w-m"),
    76:  ("Al-Insan",       "Man",                    "SOCIAL_LEGAL",        "ROOT", "Ans",     "insaan = man, root A-n-s"),
    77:  ("Al-Mursalat",    "Those Sent Forth",       "EVENT_ESCHATOLOGICAL","ROOT", "rsl",     "mursalat = those sent"),
    78:  ("An-Naba",        "the Tidings",            "EVENT_ESCHATOLOGICAL","ROOT", "nbA",     "naba = tiding"),
    79:  ("An-Naziat",      "Those who Pull Out",     "EVENT_ESCHATOLOGICAL","ROOT", "nzE",     "naziat = those who pull"),
    80:  ("Abasa",          "He Frowned",             "EVENT_ESCHATOLOGICAL","ROOT", "Ebs",     "abasa = frowned"),
    81:  ("At-Takwir",      "the Folding Up",         "EVENT_ESCHATOLOGICAL","ROOT", "kwr",     "takwir = folding"),
    82:  ("Al-Infitar",     "the Cleaving",           "EVENT_ESCHATOLOGICAL","ROOT", "fTr",     "infitar = cleaving, root f-T-r"),
    83:  ("Al-Mutaffifin",  "the Defrauders",         "SOCIAL_LEGAL",        "ROOT", "Tff",     "mutaffifin = defrauders"),
    84:  ("Al-Inshiqaq",    "the Splitting",          "EVENT_ESCHATOLOGICAL","ROOT", "$qq",     "inshiqaq = splitting"),
    85:  ("Al-Buruj",       "the Constellations",     "COSMOLOGICAL_NATURAL","ROOT", "brj",     "buruj = constellations"),
    86:  ("At-Tariq",       "the Night-Comer",        "COSMOLOGICAL_NATURAL","ROOT", "Trq",     "tariq = the knocker/night-comer"),
    87:  ("Al-Ala",         "the Most High",          "DIVINE_ATTRIBUTE",    "ROOT", "Elw",     "ala = most high, root E-l-w"),
    88:  ("Al-Ghashiyah",   "the Overwhelming",       "EVENT_ESCHATOLOGICAL","ROOT", "g$y",     "ghashiyah = overwhelming, root gh-sh-y"),
    89:  ("Al-Fajr",        "the Dawn",               "COSMOLOGICAL_NATURAL","ROOT", "fjr",     "fajr = dawn"),
    90:  ("Al-Balad",       "the City",               "COSMOLOGICAL_NATURAL","ROOT", "bld",     "balad = city/land"),
    91:  ("Ash-Shams",      "the Sun",                "COSMOLOGICAL_NATURAL","ROOT", "$ms",     "shams = sun"),
    92:  ("Al-Layl",        "the Night",              "COSMOLOGICAL_NATURAL","ROOT", "lyl",     "layl = night"),
    93:  ("Ad-Duha",        "the Forenoon",           "COSMOLOGICAL_NATURAL","ROOT", "DHy",     "duha = forenoon, root D-H-y"),
    94:  ("Ash-Sharh",      "the Opening Forth",      "REVELATION_RITUAL",   "ROOT", "$rH",     "sharh = opening"),
    95:  ("At-Tin",         "the Fig",                "ANIMAL_OBJECT",       "ROOT", "tyn",     "tin = fig"),
    96:  ("Al-Alaq",        "the Clot",               "REVELATION_RITUAL",   "ROOT", "Elq",     "alaq = clot"),
    97:  ("Al-Qadr",        "the Decree",             "REVELATION_RITUAL",   "ROOT", "qdr",     "qadr = decree/measure"),
    98:  ("Al-Bayyinah",    "the Clear Proof",        "REVELATION_RITUAL",   "ROOT", "byn",     "bayyinah = clear proof, root b-y-n"),
    99:  ("Az-Zalzalah",    "the Earthquake",         "EVENT_ESCHATOLOGICAL","ROOT", "zlzl",    "zalzalah = earthquake, 4-letter root"),
    100: ("Al-Adiyat",      "the Chargers",           "ANIMAL_OBJECT",       "ROOT", "Edw",     "adiyat = chargers, root E-d-w"),
    101: ("Al-Qariah",      "the Striking Calamity",  "EVENT_ESCHATOLOGICAL","ROOT", "qrE",     "qariah = striker"),
    102: ("At-Takathur",    "the Multiplication",     "OTHER_ABSTRACT",      "ROOT", "kvr",     "takathur = abundance, root k-th-r"),
    103: ("Al-Asr",         "the Time",               "COSMOLOGICAL_NATURAL","ROOT", "ESr",     "asr = time/era"),
    104: ("Al-Humazah",     "the Slanderer",          "SOCIAL_LEGAL",        "ROOT", "hmz",     "humazah = slanderer"),
    105: ("Al-Fil",         "the Elephant",           "ANIMAL_OBJECT",       "ROOT", "fyl",     "fil = elephant"),
    106: ("Quraysh",        "Quraysh",                "SOCIAL_LEGAL",        "LEM",  "qurayo$", "Quraysh PN/ethnonym"),
    107: ("Al-Maun",        "the Small Kindnesses",   "REVELATION_RITUAL",   "ROOT", "mEn",     "maun = small kindness"),
    108: ("Al-Kawthar",     "the Abundance",          "OTHER_ABSTRACT",      "ROOT", "kvr",     "kawthar = abundance, root k-th-r"),
    109: ("Al-Kafirun",     "the Disbelievers",       "SOCIAL_LEGAL",        "ROOT", "kfr",     "kafirun = disbelievers"),
    110: ("An-Nasr",        "the Help",               "EVENT_ESCHATOLOGICAL","ROOT", "nSr",     "nasr = help"),
    111: ("Al-Masad",       "the Palm Fibre",         "ANIMAL_OBJECT",       "ROOT", "msd",     "masad = palm fibre"),
    112: ("Al-Ikhlas",      "the Sincerity",          "DIVINE_ATTRIBUTE",    "ROOT", "xlS",     "ikhlas = sincerity"),
    113: ("Al-Falaq",       "the Daybreak",           "COSMOLOGICAL_NATURAL","ROOT", "flq",     "falaq = daybreak"),
    114: ("An-Nas",         "Mankind",                "SOCIAL_LEGAL",        "ROOT", "nws",     "nas = people, root n-w-s"),
}
assert len(SURAH_MAP) == 114


# ============================================================================
# Statistical helpers
# ============================================================================

def lgamma(x: float) -> float:
    return math.lgamma(x)


def hypergeom_pmf_log(k: int, K: int, n: int, N: int) -> float:
    """log P(X=k) for hypergeometric: N total, K success, n drawn."""
    if k < 0 or k > K or k > n or (n - k) > (N - K):
        return -float("inf")
    return (lgamma(K + 1) - lgamma(k + 1) - lgamma(K - k + 1)
            + lgamma(N - K + 1) - lgamma(n - k + 1) - lgamma(N - K - n + k + 1)
            - (lgamma(N + 1) - lgamma(n + 1) - lgamma(N - n + 1)))


def hypergeom_p_two_sided(k_obs: int, K: int, n: int, N: int) -> float:
    """Two-sided hypergeometric p-value (sum of all PMFs ≤ observed PMF)."""
    if K == 0 or n == 0 or N == 0:
        return 1.0
    log_obs = hypergeom_pmf_log(k_obs, K, n, N)
    if log_obs == -float("inf"):
        return 1.0
    kmin = max(0, n - (N - K))
    kmax = min(n, K)
    log_terms = []
    for k in range(kmin, kmax + 1):
        lp = hypergeom_pmf_log(k, K, n, N)
        if lp <= log_obs + 1e-12:  # add a tiny tolerance for numerical equality
            log_terms.append(lp)
    if not log_terms:
        return 1.0
    lmax = max(log_terms)
    s = sum(math.exp(lp - lmax) for lp in log_terms) * math.exp(lmax)
    return min(1.0, s)


def hypergeom_p_upper(k_obs: int, K: int, n: int, N: int) -> float:
    """One-sided upper-tail hypergeometric p-value: P(X >= k_obs)."""
    if K == 0 or n == 0 or N == 0:
        return 1.0
    kmin = max(0, n - (N - K))
    kmax = min(n, K)
    if k_obs > kmax:
        return 0.0
    if k_obs <= kmin:
        return 1.0
    log_terms = []
    for k in range(k_obs, kmax + 1):
        lp = hypergeom_pmf_log(k, K, n, N)
        log_terms.append(lp)
    if not log_terms:
        return 1.0
    lmax = max(log_terms)
    s = sum(math.exp(lp - lmax) for lp in log_terms) * math.exp(lmax)
    return min(1.0, s)


def poisson_p_upper(k_obs: int, lam: float) -> float:
    """Upper-tail Poisson p: P(X >= k_obs) for Poisson(lam)."""
    if lam <= 0:
        return 1.0 if k_obs == 0 else 0.0
    if k_obs == 0:
        return 1.0
    # P(X >= k) = 1 - sum_{j=0}^{k-1} exp(-lam) lam^j / j!
    log_lam = math.log(lam)
    log_terms = []
    for j in range(0, k_obs):
        log_terms.append(-lam + j * log_lam - lgamma(j + 1))
    if not log_terms:
        return 1.0
    lmax = max(log_terms)
    cdf = sum(math.exp(lp - lmax) for lp in log_terms) * math.exp(lmax)
    return max(0.0, min(1.0, 1.0 - cdf))


def fisher_exact_2x2(a: int, b: int, c: int, d: int) -> float:
    """Two-sided Fisher exact for 2x2 table [[a,b],[c,d]]."""
    n = a + b + c + d
    r1 = a + b
    c1 = a + c
    if n == 0 or r1 == 0 or c1 == 0:
        return 1.0
    log_denom = lgamma(n + 1) - lgamma(c1 + 1) - lgamma(n - c1 + 1)
    def logP(k):
        if k < 0 or k > r1 or (c1 - k) < 0 or (c1 - k) > (n - r1):
            return -float("inf")
        return (lgamma(r1 + 1) - lgamma(k + 1) - lgamma(r1 - k + 1)
                + lgamma(n - r1 + 1) - lgamma(c1 - k + 1) - lgamma(n - r1 - c1 + k + 1)
                - log_denom)
    obs = logP(a)
    kmin = max(0, c1 - (n - r1))
    kmax = min(r1, c1)
    p_sum = 0.0
    for k in range(kmin, kmax + 1):
        lp = logP(k)
        if lp <= obs + 1e-12:
            p_sum += math.exp(lp)
    return min(1.0, p_sum)


def chi_square_p(chi2: float, df: int) -> float:
    """Upper-tail chi-square p via series / continued fraction."""
    if df <= 0 or chi2 < 0:
        return 1.0
    a = df / 2.0
    x = chi2 / 2.0
    if x == 0:
        return 1.0
    if x < a + 1.0:
        ap = a
        s = 1.0 / a
        term = s
        for _ in range(2000):
            ap += 1.0
            term *= x / ap
            s += term
            if abs(term) < abs(s) * 1e-15:
                break
        log_p = -x + a * math.log(x) - lgamma(a)
        P = s * math.exp(log_p)
        return max(0.0, min(1.0, 1.0 - P))
    else:
        b = x + 1.0 - a
        c = 1.0 / 1e-300
        d = 1.0 / b
        h = d
        for i in range(1, 2000):
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
        log_q = -x + a * math.log(x) - lgamma(a)
        Q = h * math.exp(log_q)
        return max(0.0, min(1.0, Q))


def chi_square_test(observed: List[List[float]]) -> Tuple[float, int, float]:
    rows = len(observed)
    cols = len(observed[0]) if rows else 0
    row_tot = [sum(r) for r in observed]
    col_tot = [sum(observed[i][j] for i in range(rows)) for j in range(cols)]
    grand = sum(row_tot)
    if grand == 0:
        return (0.0, 0, 1.0)
    chi2 = 0.0
    for i in range(rows):
        for j in range(cols):
            e = row_tot[i] * col_tot[j] / grand
            if e > 0:
                chi2 += (observed[i][j] - e) ** 2 / e
    df = (rows - 1) * (cols - 1)
    p = chi_square_p(chi2, df)
    return (chi2, df, p)


# ============================================================================
# Morphology loader
# ============================================================================

MORPH_PATH = os.path.join(REPO, "data/morphology/quranic-corpus-morphology-0.4.txt")
LOC_RE = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")
ROOT_RE = re.compile(r"ROOT:([^|]+)")
LEM_RE = re.compile(r"LEM:([^|]+)")
POS_RE = re.compile(r"POS:([^|]+)")


def load_morphology() -> Dict[Tuple[int, int, int], dict]:
    """Aggregate morphology to one record per word (s,v,w).

    Each record: roots = set of roots seen across segments, lems = set of
    lems, pos_tags = set of POS tags, n_segments = number of segments.
    """
    out: Dict[Tuple[int, int, int], dict] = {}
    with open(MORPH_PATH, "r", encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.startswith("#") or line.startswith("LOCATION"):
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            loc_m = LOC_RE.match(parts[0])
            if not loc_m:
                continue
            s, v, w = int(loc_m.group(1)), int(loc_m.group(2)), int(loc_m.group(3))
            features = parts[3]
            key = (s, v, w)
            if key not in out:
                out[key] = {"roots": set(), "lems": set(), "pos": set(), "n_seg": 0}
            out[key]["n_seg"] += 1
            rm = ROOT_RE.search(features)
            if rm:
                out[key]["roots"].add(rm.group(1))
            lm = LEM_RE.search(features)
            if lm:
                out[key]["lems"].add(lm.group(1))
            pm = POS_RE.search(features)
            if pm:
                out[key]["pos"].add(pm.group(1))
    return out


# ============================================================================
# Per-surah testing
# ============================================================================

def per_surah_counts(morph: Dict[Tuple[int, int, int], dict]) -> Dict[int, int]:
    """Token count per surah (one count per (s,v,w))."""
    out: Dict[int, int] = defaultdict(int)
    for (s, v, w), rec in morph.items():
        out[s] += 1
    return dict(out)


def count_target(morph: Dict[Tuple[int, int, int], dict],
                 target: str, type_: str) -> Dict[int, int]:
    """Count tokens whose ROOT (or LEM) matches target, by surah.

    A token (s,v,w) counts as ONE hit if ANY of its segments has a
    matching ROOT/LEM.
    """
    out: Dict[int, int] = defaultdict(int)
    field = "roots" if type_ == "ROOT" else "lems"
    for (s, v, w), rec in morph.items():
        if target in rec[field]:
            out[s] += 1
    return dict(out)


def run_per_surah_tests(morph: Dict[Tuple[int, int, int], dict],
                        per_surah_n: Dict[int, int]) -> dict:
    n_total = sum(per_surah_n.values())
    results = []
    for sid in range(1, N_SURAHS + 1):
        translit, gloss, cls, type_, target, notes = SURAH_MAP[sid]
        n_in = per_surah_n.get(sid, 0)
        n_rest = n_total - n_in
        if type_ == "NONE" or target is None:
            results.append({
                "surah": sid, "translit": translit, "gloss": gloss, "class": cls,
                "type": type_, "target": target, "notes": notes,
                "testable": False, "n_in": n_in, "n_rest": n_rest,
                "hits_in": None, "hits_rest": None, "rate_in": None, "rate_rest": None,
                "ratio": None, "p_two": None, "p_upper": None, "p_poisson_upper": None,
                "sig_bon": False, "sig_raw": False,
            })
            continue
        counts = count_target(morph, target, type_)
        hits_in = counts.get(sid, 0)
        hits_rest = sum(c for s2, c in counts.items() if s2 != sid)
        K = hits_in + hits_rest
        rate_in = hits_in / n_in if n_in else 0.0
        rate_rest = hits_rest / n_rest if n_rest else 0.0
        ratio = (rate_in / rate_rest) if rate_rest > 0 else (float("inf") if hits_in > 0 else 0.0)
        p_two = hypergeom_p_two_sided(hits_in, K, n_in, n_total)
        p_upper = hypergeom_p_upper(hits_in, K, n_in, n_total)
        lam = K * n_in / n_total if n_total > 0 else 0.0
        p_poi = poisson_p_upper(hits_in, lam)
        results.append({
            "surah": sid, "translit": translit, "gloss": gloss, "class": cls,
            "type": type_, "target": target, "notes": notes,
            "testable": True, "n_in": n_in, "n_rest": n_rest,
            "hits_in": hits_in, "hits_rest": hits_rest,
            "rate_in": rate_in, "rate_rest": rate_rest, "ratio": ratio,
            "p_two": p_two, "p_upper": p_upper, "p_poisson_upper": p_poi,
            "sig_bon": p_two < ALPHA_BON,
            "sig_raw": p_two < 0.05,
        })
    return {
        "n_total_morph_tokens": n_total,
        "results": results,
    }


# ============================================================================
# Stratifications (5 pre-committed)
# ============================================================================

def stratify_muqattaat(per_surah_results: List[dict]) -> dict:
    """muqaṭṭaʿāt-Y/N × Bonferroni-pass/fail (testable only)."""
    a = b = c = d = 0  # a=muq+sig, b=muq+notsig, c=non+sig, d=non+notsig
    for r in per_surah_results:
        if not r["testable"]:
            continue
        muq = r["surah"] in MUQ_SURAHS
        sig = r["sig_bon"]
        if muq and sig: a += 1
        elif muq and not sig: b += 1
        elif (not muq) and sig: c += 1
        else: d += 1
    p = fisher_exact_2x2(a, b, c, d)
    return {
        "muq_sig": a, "muq_nonsig": b, "nonmuq_sig": c, "nonmuq_nonsig": d,
        "fisher_p": p,
    }


def stratify_class(per_surah_results: List[dict]) -> dict:
    """class × pass/fail χ²."""
    table = {c: {"sig": 0, "nonsig": 0} for c in CLASSES}
    for r in per_surah_results:
        if not r["testable"]:
            continue
        cls = r["class"]
        if r["sig_bon"]:
            table[cls]["sig"] += 1
        else:
            table[cls]["nonsig"] += 1
    # Drop empty rows
    rows_used = [c for c in CLASSES if table[c]["sig"] + table[c]["nonsig"] > 0]
    obs = [[table[c]["sig"], table[c]["nonsig"]] for c in rows_used]
    chi2, df, p = chi_square_test(obs)
    return {
        "table": table, "rows_used": rows_used,
        "chi2": chi2, "df": df, "p": p,
    }


def stratify_pn_vs_root(per_surah_results: List[dict]) -> dict:
    """LEM (PN) vs ROOT type × pass/fail Fisher 2x2."""
    a = b = c = d = 0  # a=PN+sig, b=PN+notsig, c=ROOT+sig, d=ROOT+notsig
    for r in per_surah_results:
        if not r["testable"]:
            continue
        is_pn = (r["type"] == "LEM")
        sig = r["sig_bon"]
        if is_pn and sig: a += 1
        elif is_pn and not sig: b += 1
        elif (not is_pn) and sig: c += 1
        else: d += 1
    p = fisher_exact_2x2(a, b, c, d)
    return {
        "pn_sig": a, "pn_nonsig": b, "root_sig": c, "root_nonsig": d,
        "fisher_p": p,
    }


def stratify_meccan_medinan(per_surah_results: List[dict],
                            surahs_meta: List) -> dict:
    """Meccan/Medinan × pass/fail Fisher."""
    type_by_id = {s.id: s.type for s in surahs_meta}
    a = b = c = d = 0  # a=meccan+sig, b=meccan+notsig, c=medinan+sig, d=medinan+notsig
    for r in per_surah_results:
        if not r["testable"]:
            continue
        t = type_by_id.get(r["surah"], "")
        sig = r["sig_bon"]
        if t == "meccan" and sig: a += 1
        elif t == "meccan" and not sig: b += 1
        elif t == "medinan" and sig: c += 1
        elif t == "medinan" and not sig: d += 1
    p = fisher_exact_2x2(a, b, c, d)
    return {
        "meccan_sig": a, "meccan_nonsig": b,
        "medinan_sig": c, "medinan_nonsig": d, "fisher_p": p,
    }


def stratify_length_quartile(per_surah_results: List[dict],
                             per_surah_n: Dict[int, int]) -> dict:
    """Length-quartile × pass/fail χ² (over testable surahs)."""
    testable = [r for r in per_surah_results if r["testable"]]
    sorted_by_len = sorted(testable, key=lambda r: per_surah_n[r["surah"]])
    n = len(sorted_by_len)
    quartile_for = {}
    for i, r in enumerate(sorted_by_len):
        q = (i * 4) // n  # 0..3
        quartile_for[r["surah"]] = q
    table = [[0, 0] for _ in range(4)]  # [sig, nonsig] per quartile
    for r in testable:
        q = quartile_for[r["surah"]]
        if r["sig_bon"]:
            table[q][0] += 1
        else:
            table[q][1] += 1
    obs = table
    chi2, df, p = chi_square_test(obs)
    # Also list quartile boundaries
    if n > 0:
        boundaries = [per_surah_n[sorted_by_len[(n * (q + 1)) // 4 - 1]["surah"]]
                      for q in range(4)]
    else:
        boundaries = []
    return {
        "table_q_sig_nonsig": table,
        "quartile_upper_bounds": boundaries,
        "chi2": chi2, "df": df, "p": p,
    }


# ============================================================================
# Driver
# ============================================================================

def main():
    print(f"H-NEW-86 — Surah-name-as-key-root. Seed={SEED}, Bon-k={BON_K}, α_bon={ALPHA_BON:.3e}")
    print("Loading morphology...")
    morph = load_morphology()
    per_surah_n = per_surah_counts(morph)
    n_total = sum(per_surah_n.values())
    print(f"  morph tokens total = {n_total}")
    print(f"  morph tokens Q12 = {per_surah_n[12]}, Q71 = {per_surah_n[71]}, Q114 = {per_surah_n[114]}")

    surahs_meta = load_quran("no-tashkeel")

    out = run_per_surah_tests(morph, per_surah_n)
    results = out["results"]

    # MW-5 controls
    yusuf = next(r for r in results if r["surah"] == 12)
    nuh = next(r for r in results if r["surah"] == 71)
    print("\nMW-5 positive (Q12 Yusuf, LEM=yuwsuf):")
    print(f"  hits_in={yusuf['hits_in']}, hits_rest={yusuf['hits_rest']}, ratio={yusuf['ratio']:.1f}, p_two={yusuf['p_two']:.3e}")
    print("MW-5 subtle (Q71 Nuh, LEM=nuwH):")
    print(f"  hits_in={nuh['hits_in']}, hits_rest={nuh['hits_rest']}, ratio={nuh['ratio']:.2f}, p_two={nuh['p_two']:.3e}")

    # Per-surah Bon
    n_test = sum(1 for r in results if r["testable"])
    n_sig = sum(1 for r in results if r["sig_bon"])
    n_raw = sum(1 for r in results if r["sig_raw"])
    frac_sig = n_sig / n_test if n_test else 0.0
    if n_sig >= 2 * n_test / 3:
        verdict = "STRONG-PASS"
    elif n_sig >= n_test / 3:
        verdict = "PASS"
    elif n_sig > 0:
        verdict = "EXPLORATORY"
    else:
        verdict = "NULL"
    print(f"\nPer-surah Bonferroni-114 (α={ALPHA_BON:.3e}): {n_sig}/{n_test} ({100*frac_sig:.1f}%) sig; verdict={verdict}")
    print(f"Raw α=0.05: {n_raw}/{n_test} ({100*n_raw/n_test:.1f}%) sig.")

    # Stratifications
    s_muq = stratify_muqattaat(results)
    print(f"\nStrat 1 — muqaṭṭaʿāt × pass: muq_sig={s_muq['muq_sig']}/{s_muq['muq_sig']+s_muq['muq_nonsig']}, "
          f"non_sig={s_muq['nonmuq_sig']}/{s_muq['nonmuq_sig']+s_muq['nonmuq_nonsig']}, Fisher p={s_muq['fisher_p']:.4f}")

    s_class = stratify_class(results)
    print(f"\nStrat 2 — class × pass χ²={s_class['chi2']:.3f}, df={s_class['df']}, p={s_class['p']:.4f}")
    for c in s_class["rows_used"]:
        t = s_class["table"][c]
        n_c = t["sig"] + t["nonsig"]
        print(f"  {c:25s} {t['sig']:3d}/{n_c:3d} ({100*t['sig']/n_c if n_c else 0:.0f}%)")

    s_pn = stratify_pn_vs_root(results)
    print(f"\nStrat 3 — PN(LEM) vs ROOT × pass: PN={s_pn['pn_sig']}/{s_pn['pn_sig']+s_pn['pn_nonsig']}, "
          f"ROOT={s_pn['root_sig']}/{s_pn['root_sig']+s_pn['root_nonsig']}, Fisher p={s_pn['fisher_p']:.4f}")

    s_mm = stratify_meccan_medinan(results, surahs_meta)
    print(f"\nStrat 4 — Meccan/Medinan × pass: M={s_mm['meccan_sig']}/{s_mm['meccan_sig']+s_mm['meccan_nonsig']}, "
          f"D={s_mm['medinan_sig']}/{s_mm['medinan_sig']+s_mm['medinan_nonsig']}, Fisher p={s_mm['fisher_p']:.4f}")

    s_len = stratify_length_quartile(results, per_surah_n)
    print(f"\nStrat 5 — length-quartile × pass χ²={s_len['chi2']:.3f}, df={s_len['df']}, p={s_len['p']:.4f}")
    print(f"  Q1..Q4 sig/nonsig: {s_len['table_q_sig_nonsig']}")
    print(f"  Quartile upper bounds: {s_len['quartile_upper_bounds']}")

    # Top-15 by enrichment ratio (filter testable, hits_in >= 1)
    finite_ratio = [r for r in results if r["testable"] and r["hits_in"] is not None
                    and r["hits_in"] >= 1 and r["ratio"] != float("inf")]
    inf_ratio = [r for r in results if r["testable"] and r["ratio"] == float("inf")]
    finite_ratio.sort(key=lambda r: r["ratio"], reverse=True)
    print("\nTop-15 by enrichment ratio (finite):")
    for r in finite_ratio[:15]:
        print(f"  Q{r['surah']:3d} {r['translit']:18s} hits={r['hits_in']:3d}/{r['n_in']:5d} "
              f"rest={r['hits_rest']:5d}/{r['n_rest']:6d} ratio={r['ratio']:8.1f} p={r['p_two']:.3e} "
              f"{'SIG' if r['sig_bon'] else ''}")
    print(f"\nInfinite-ratio (rest=0) testable surahs: {len(inf_ratio)}")
    for r in sorted(inf_ratio, key=lambda r: r["surah"]):
        print(f"  Q{r['surah']:3d} {r['translit']:18s} hits={r['hits_in']:3d}/{r['n_in']:5d} target={r['target']}")

    # Top-15 by p-value
    by_p = sorted([r for r in results if r["testable"]], key=lambda r: r["p_two"])
    print("\nTop-15 by p-value:")
    for r in by_p[:15]:
        print(f"  Q{r['surah']:3d} {r['translit']:18s} hits={r['hits_in']:3d}/{r['n_in']:5d} "
              f"ratio={r['ratio']:8.2f} p={r['p_two']:.3e} {'SIG' if r['sig_bon'] else ''}")

    # Save outputs
    os.makedirs(os.path.join(REPO, "findings/phase-b-hypotheses/csv"), exist_ok=True)
    out_json = {
        "id": "H-NEW-86",
        "title": "Surah-name-as-key-root, full 114-surah scan",
        "seed": SEED,
        "bon_k": BON_K,
        "alpha_bon": ALPHA_BON,
        "rules_tuple": "(hafs-kufan; canonical 114; Leeds QAC v0.4 morphology)",
        "n_total_morph_tokens": n_total,
        "n_testable": n_test,
        "n_sig_bonferroni_114": n_sig,
        "n_sig_raw_05": n_raw,
        "frac_sig": frac_sig,
        "verdict": verdict,
        "mw5_yusuf": yusuf,
        "mw5_nuh": nuh,
        "stratifications": {
            "muqattaat": s_muq,
            "class": s_class,
            "pn_vs_root": s_pn,
            "meccan_medinan": s_mm,
            "length_quartile": s_len,
        },
        "surah_root_map": {
            sid: {"translit": v[0], "gloss": v[1], "class": v[2],
                  "type": v[3], "target": v[4], "notes": v[5]}
            for sid, v in SURAH_MAP.items()
        },
        "per_surah_results": [
            {**r, "ratio": (None if r["ratio"] is None else
                            ("inf" if r["ratio"] == float("inf") else r["ratio"]))}
            for r in results
        ],
    }
    with open(os.path.join(REPO, "findings/phase-b-hypotheses/csv/h-new-86.json"), "w") as f:
        json.dump(out_json, f, indent=2)
    print(f"\nWrote h-new-86.json")

    # CSV table
    csv_path = os.path.join(REPO, "findings/phase-b-hypotheses/csv/h-new-86-per-surah.csv")
    with open(csv_path, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["surah", "translit", "gloss", "class", "muqattaat", "type", "target",
                    "n_in", "n_rest", "hits_in", "hits_rest", "rate_in", "rate_rest",
                    "ratio", "p_two", "p_upper", "p_poisson_upper", "sig_bon"])
        for r in results:
            w.writerow([
                r["surah"], r["translit"], r["gloss"], r["class"],
                int(r["surah"] in MUQ_SURAHS), r["type"], r["target"],
                r["n_in"], r["n_rest"],
                r["hits_in"] if r["hits_in"] is not None else "",
                r["hits_rest"] if r["hits_rest"] is not None else "",
                f"{r['rate_in']:.6f}" if r["rate_in"] is not None else "",
                f"{r['rate_rest']:.6f}" if r["rate_rest"] is not None else "",
                ("inf" if r["ratio"] == float("inf") else
                 (f"{r['ratio']:.3f}" if r["ratio"] is not None else "")),
                f"{r['p_two']:.3e}" if r["p_two"] is not None else "",
                f"{r['p_upper']:.3e}" if r["p_upper"] is not None else "",
                f"{r['p_poisson_upper']:.3e}" if r["p_poisson_upper"] is not None else "",
                int(r["sig_bon"]),
            ])
    print(f"Wrote h-new-86-per-surah.csv")


if __name__ == "__main__":
    main()
