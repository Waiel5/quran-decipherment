#!/usr/bin/env python3
"""
H-NEW-128 — Cross-axis distinctive-verse atlas.

13 locked axes:
1. divine_name_density     - Allah + 99-name / words
2. light_density            - light-vocab substr / words
3. eschatology_density      - yawm/akhira/qiyama/jahannam/firdaws/hisab/jaza / words
4. book_reference_density   - kitab/quran/ayat/nazala / words
5. oath_density             - 1 if verse starts wa-<oath-eligible>
6. rare_vocab_density       - tokens whose form-lemma appears <=3x in corpus / words
7. rhyme_density            - 1 if verse's final-letter matches preceding verse's
8. fasila_diversity         - 1 - (freq of verse's final-letter within its own surah)
9. imperative_density       - qul / ya / inna / verse-initial imperative markers / words
10. refrain_closeness       - Jaccard similarity to the verse's surah's mode verse
11. narrative_tense_density - kana/qala past-verb tokens / words
12. short_marker            - 1 if words < 3
13. long_marker             - 1 if words > 50

Outputs per-axis top-100, intersection atlas, harmonic-mean-rank superverse top-100,
classical-celebrated-verse hit rate, and permutation null p-values for Cells A and B.

Seed: 20260417. n_perm = 10000. Pre-reg: h-new-128-prereg.md.
"""

import json
import os
import re
import random
from collections import Counter, defaultdict
from math import fsum

SEED = 20260417
N_PERM = 10000
BASE = "/Users/grey/Downloads/quran"
QURAN_JSON = f"{BASE}/quran-text/quran-no-tashkeel.json"
OUT_JSON = f"{BASE}/findings/phase-b-hypotheses/csv/h-new-128.json"

# ------------------------------------------------------------------
# Load Quran
# ------------------------------------------------------------------
with open(QURAN_JSON, "r", encoding="utf-8") as f:
    Q = json.load(f)

VERSES = []   # list of (surah, verse, text, tokens)
for s in Q:
    sid = s["id"]
    for v in s["verses"]:
        vid = v["id"]
        text = v["text"]
        tokens = text.split()
        VERSES.append({"surah": sid, "verse": vid, "text": text, "tokens": tokens})

N = len(VERSES)
assert N == 6236, f"Expected 6236 verses, got {N}"

# ------------------------------------------------------------------
# Axis 1 — Divine-name density
# ------------------------------------------------------------------
# 99-name set (no-tashkeel consonantal forms)
# Anchored on classical Tirmidhi list; forms chosen to match no-tashkeel corpus
DIVINE_NAMES = [
    "الله", "الرحمن", "الرحيم", "الملك", "القدوس", "السلام", "المؤمن", "المهيمن",
    "العزيز", "الجبار", "المتكبر", "الخالق", "البارئ", "البارىء", "المصور",
    "الغفار", "القهار", "الوهاب", "الرزاق", "الفتاح", "العليم", "القابض",
    "الباسط", "الخافض", "الرافع", "المعز", "المذل", "السميع", "البصير",
    "الحكم", "العدل", "اللطيف", "الخبير", "الحليم", "العظيم", "الغفور",
    "الشكور", "العلي", "الكبير", "الحفيظ", "المقيت", "الحسيب", "الجليل",
    "الكريم", "الرقيب", "المجيب", "الواسع", "الحكيم", "الودود", "المجيد",
    "الباعث", "الشهيد", "الحق", "الوكيل", "القوي", "المتين", "الولي",
    "الحميد", "المحصي", "المبدئ", "المعيد", "المحيي", "المميت", "الحي",
    "القيوم", "الواجد", "الماجد", "الواحد", "الصمد", "القادر", "المقتدر",
    "المقدم", "المؤخر", "الأول", "الآخر", "الظاهر", "الباطن", "الوالي",
    "المتعالي", "البر", "التواب", "المنتقم", "العفو", "الرؤوف", "مالك",
    "الجلال", "الاكرام", "المقسط", "الجامع", "الغني", "المغني", "المانع",
    "الضار", "النافع", "النور", "الهادي", "البديع", "الوارث", "الرشيد",
    "الصبور", "رب", "ربك", "ربكم", "ربنا", "ربي", "ربها", "ربهم", "الرب",
]
# Normalize: strip hamzas/alef forms for matching
def normalize_ar(s):
    s = s.replace("ٱ", "ا").replace("أ", "ا").replace("إ", "ا").replace("آ", "ا")
    s = s.replace("ة", "ه")  # optional; we'll match with/without
    s = s.replace("ى", "ي")
    return s

DIVINE_NAME_SET = set(normalize_ar(x) for x in DIVINE_NAMES)
# Match tokens with leading proclitics (و, ف, ل, ب, ك, س)
PROCLITIC_RE = re.compile(r"^(?:و|ف|ل|ب|ك|س)+")
def strip_proclitics(tok):
    m = PROCLITIC_RE.match(tok)
    if m:
        rest = tok[m.end():]
        return rest if rest else tok
    return tok

def count_divine_names(tokens):
    c = 0
    for t in tokens:
        n = normalize_ar(t)
        # try whole
        if n in DIVINE_NAME_SET:
            c += 1; continue
        # strip proclitics
        n2 = strip_proclitics(n)
        if n2 in DIVINE_NAME_SET:
            c += 1
    return c

# ------------------------------------------------------------------
# Axis 2 — Light-vocab density
# ------------------------------------------------------------------
# Consonantal skeletons for light-family roots; substring match on no-tashkeel
LIGHT_SUBS = [
    "نور",   # nwr
    "ضوء", "ضيء", "ضيا",   # DwA / Dwa
    "مصباح", "صبح",   # SbH (lamp/morning)
    "سراج",   # srj
    "قبس",   # qbs (firebrand)
    "شهاب",   # shhb
    "رمد", "رماد",   # rmd (ashes)
    "صور",   # Swr (horn) — note: also picture; narrow via context; include
    "وقد", "يوقد", "توقد", "اوقد", "استوقد",   # wqd
    "ذوق", "ذاق",   # Dwq (taste/flavor - secondary light per H-NEW-92)
    "شمس",   # shms (sun)
    "قمر",   # qmr (moon)
    "نار", "نير",   # nwr-fire
]
def count_light(tokens):
    c = 0
    for t in tokens:
        n = normalize_ar(t)
        n = strip_proclitics(n)
        for sub in LIGHT_SUBS:
            if sub in n:
                c += 1
                break
    return c

# ------------------------------------------------------------------
# Axis 3 — Eschatology density
# ------------------------------------------------------------------
ESCHAT_SUBS = [
    "يوم", "يوما", "ايام", "اليوم",  # yawm
    "اخر", "اخره", "اخرة", "الاخر",  # akhira
    "قيم", "قيام", "قيامه", "قيامة",  # qiyama
    "جهنم",  # jahannam
    "فردوس",  # firdaws
    "حساب", "حاسب", "حسب",  # hisab
    "جزاء", "جزا", "يجز", "جزي", "نجز",  # jaza
    "نار", "النار",  # hellfire (overlaps light; contextually eschat)
    "جنة", "جنت", "الجنة",  # jannah
]
def count_eschat(tokens):
    c = 0
    for t in tokens:
        n = normalize_ar(t); n = strip_proclitics(n)
        for sub in ESCHAT_SUBS:
            if sub in n:
                c += 1; break
    return c

# ------------------------------------------------------------------
# Axis 4 — Book-reference density
# ------------------------------------------------------------------
BOOK_SUBS = [
    "كتب", "كتاب", "الكتاب", "كتبنا",  # kitab
    "قران", "القران", "قرا",  # quran/qara
    "ايات", "اية", "الايات", "اياتنا",  # ayat
    "نزل", "انزل", "منزل", "نزلنا", "انزلنا", "تنزيل", "المنزل",  # nazala
    "وحي", "وحى", "اوحى", "يوحي",  # wahy
]
def count_book(tokens):
    c = 0
    for t in tokens:
        n = normalize_ar(t); n = strip_proclitics(n)
        for sub in BOOK_SUBS:
            if sub in n:
                c += 1; break
    return c

# ------------------------------------------------------------------
# Axis 5 — Oath density (verse-initial wa-<noun>)
# ------------------------------------------------------------------
# Canonical oath surahs: Q 36, 37, 51, 52, 53, 68, 74, 75, 77, 79, 81, 84, 85, 86, 89, 90, 91, 92, 93, 95, 100, 103
# We operationalize: verse opens with a 2+char token beginning with "و" followed by a noun
# but to avoid waw-coordinator inflation, we use classical oath-opening-surah pattern:
# verse-1 of any surah from a pre-specified oath-opening list + any verse whose FIRST token
# starts with و and whose surah's verse 1 also starts with و (oath-surah heuristic)
OATH_OPENING_SURAHS = {37, 51, 52, 53, 68, 77, 79, 81, 85, 86, 89, 90, 91, 92, 93, 95, 100, 103}

def oath_score(v):
    # Rank-continuous: 1.0 if oath-opening-surah verse; 0.5 if verse starts with و in oath-opening-surah; 0 else
    s = v["surah"]
    if s in OATH_OPENING_SURAHS:
        toks = v["tokens"]
        if toks and toks[0].startswith("و") and len(toks[0]) >= 2:
            # strict: oath-opening verses
            return 1.0
        else:
            return 0.3
    return 0.0

# ------------------------------------------------------------------
# Axis 6 — Rare vocab density
# ------------------------------------------------------------------
# Build token-form frequency across the corpus (no-tashkeel, proclitic-stripped)
TOKEN_COUNTS = Counter()
for v in VERSES:
    for t in v["tokens"]:
        n = normalize_ar(t); n = strip_proclitics(n)
        TOKEN_COUNTS[n] += 1

def rare_score(tokens):
    if not tokens: return 0.0
    c = 0
    for t in tokens:
        n = normalize_ar(t); n = strip_proclitics(n)
        if TOKEN_COUNTS.get(n, 0) <= 3:
            c += 1
    return c / len(tokens)

# ------------------------------------------------------------------
# Axis 7 — Rhyme density (consecutive-match)
# ------------------------------------------------------------------
def last_letter(tok):
    # Strip final punctuation / tanwin-only; take last consonant
    s = normalize_ar(tok)
    s = re.sub(r"[^\u0600-\u06FF]", "", s)
    # drop trailing ها, ان, ين, ون, ات if we want "rhyme letter" the classic way, but
    # for consecutive-verse matching a raw last-letter is the simplest reproducible proxy
    return s[-1] if s else ""

VERSE_LAST = []
for v in VERSES:
    if v["tokens"]:
        VERSE_LAST.append(last_letter(v["tokens"][-1]))
    else:
        VERSE_LAST.append("")

# Consecutive within surah
RHYME_MATCH = [0] * N
for i, v in enumerate(VERSES):
    if v["verse"] == 1:
        RHYME_MATCH[i] = 0
        continue
    # previous verse in same surah = i-1 (always true since VERSES ordered)
    prev = VERSES[i-1]
    if prev["surah"] == v["surah"] and VERSE_LAST[i] and VERSE_LAST[i] == VERSE_LAST[i-1]:
        RHYME_MATCH[i] = 1

# ------------------------------------------------------------------
# Axis 8 — Fāṣila diversity (rarity of verse's final-letter in its surah)
# ------------------------------------------------------------------
SURAH_LAST_LETTER_FREQ = defaultdict(Counter)
for i, v in enumerate(VERSES):
    SURAH_LAST_LETTER_FREQ[v["surah"]][VERSE_LAST[i]] += 1

FASILA_DIV = []
for i, v in enumerate(VERSES):
    s = v["surah"]
    total = sum(SURAH_LAST_LETTER_FREQ[s].values())
    freq = SURAH_LAST_LETTER_FREQ[s][VERSE_LAST[i]] / total if total else 0
    FASILA_DIV.append(1.0 - freq)  # higher = rarer letter = more diverse

# ------------------------------------------------------------------
# Axis 9 — Imperative density
# ------------------------------------------------------------------
IMPERATIVE_FIRST = {"قل", "قال", "قلنا", "يا", "انا", "انا", "ان", "اذا"}  # verse-first
IMP_SUBS_ANY = ["قل", "يايها", "ياايها", "انا"]  # any-position
def imperative_score(tokens):
    if not tokens: return 0.0
    c = 0
    # verse-initial Qul
    first = normalize_ar(tokens[0])
    if first in {"قل", "قالوا", "قولوا", "فقل"}:
        c += 1
    # any-position ya-ayyuha / inna
    for t in tokens:
        n = normalize_ar(t); n = strip_proclitics(n)
        if n in {"يايها", "ياايها", "انا"} or n.startswith("يايها") or n.startswith("ياايها"):
            c += 1
        elif n == "قل" or n == "فقل":
            c += 1
    return c / len(tokens)

# ------------------------------------------------------------------
# Axis 10 — Refrain closeness (Jaccard to surah mode verse)
# ------------------------------------------------------------------
# For each surah, find the verse whose token-bag has the highest Jaccard similarity mean
# to other verses in the surah (the "centroid verse"). Then each verse's refrain_score =
# Jaccard to that centroid.
SURAH_VERSES = defaultdict(list)
for i, v in enumerate(VERSES):
    SURAH_VERSES[v["surah"]].append(i)

def jaccard(a_set, b_set):
    if not a_set and not b_set: return 0.0
    u = a_set | b_set
    if not u: return 0.0
    return len(a_set & b_set) / len(u)

REFRAIN_SCORE = [0.0] * N
for s, idxs in SURAH_VERSES.items():
    token_sets = [set(normalize_ar(t) for t in VERSES[i]["tokens"]) for i in idxs]
    # For short surahs, centroid = self (trivial); for longer surahs, the verse with
    # highest mean Jaccard to others is the "refrain anchor"
    if len(idxs) <= 1:
        continue
    mean_sims = []
    for k in range(len(idxs)):
        sims = [jaccard(token_sets[k], token_sets[j]) for j in range(len(idxs)) if j != k]
        mean_sims.append(sum(sims) / len(sims) if sims else 0.0)
    centroid_k = mean_sims.index(max(mean_sims))
    centroid_set = token_sets[centroid_k]
    for k, i in enumerate(idxs):
        REFRAIN_SCORE[i] = jaccard(token_sets[k], centroid_set)

# ------------------------------------------------------------------
# Axis 11 — Narrative tense density (kana/qala past)
# ------------------------------------------------------------------
NARR_SUBS = [
    "كان", "كانوا", "كانت", "كنا", "كنتم", "كنت",  # kana
    "قال", "قالوا", "قالت", "قلنا", "قلت",  # qala past
    "خلق", "ارسل", "بعث", "اوحى", "جعل", "فعل",  # other past action verbs
]
def narr_score(tokens):
    if not tokens: return 0.0
    c = 0
    for t in tokens:
        n = normalize_ar(t); n = strip_proclitics(n)
        if any(n == sub or n.startswith(sub) for sub in NARR_SUBS):
            c += 1
    return c / len(tokens)

# ------------------------------------------------------------------
# Axes 12, 13 — Short / Long markers
# ------------------------------------------------------------------
def short_score(tokens):
    return 1 if len(tokens) < 3 else 0
def long_score(tokens):
    return 1 if len(tokens) > 50 else 0

# ------------------------------------------------------------------
# Compute all axes
# ------------------------------------------------------------------
print("Computing axes...")
AXIS_NAMES = [
    "divine_name_density",
    "light_density",
    "eschatology_density",
    "book_reference_density",
    "oath_density",
    "rare_vocab_density",
    "rhyme_density",
    "fasila_diversity",
    "imperative_density",
    "refrain_closeness",
    "narrative_tense_density",
    "short_marker",
    "long_marker",
]

# Per-verse raw scores
AXIS_SCORES = {name: [0.0] * N for name in AXIS_NAMES}

for i, v in enumerate(VERSES):
    w = max(len(v["tokens"]), 1)
    AXIS_SCORES["divine_name_density"][i] = count_divine_names(v["tokens"]) / w
    AXIS_SCORES["light_density"][i] = count_light(v["tokens"]) / w
    AXIS_SCORES["eschatology_density"][i] = count_eschat(v["tokens"]) / w
    AXIS_SCORES["book_reference_density"][i] = count_book(v["tokens"]) / w
    AXIS_SCORES["oath_density"][i] = oath_score(v)
    AXIS_SCORES["rare_vocab_density"][i] = rare_score(v["tokens"])
    AXIS_SCORES["rhyme_density"][i] = float(RHYME_MATCH[i])
    AXIS_SCORES["fasila_diversity"][i] = FASILA_DIV[i]
    AXIS_SCORES["imperative_density"][i] = imperative_score(v["tokens"])
    AXIS_SCORES["refrain_closeness"][i] = REFRAIN_SCORE[i]
    AXIS_SCORES["narrative_tense_density"][i] = narr_score(v["tokens"])
    AXIS_SCORES["short_marker"][i] = float(short_score(v["tokens"]))
    AXIS_SCORES["long_marker"][i] = float(long_score(v["tokens"]))

# ------------------------------------------------------------------
# Rank verses per axis (descending; tie-break = verse index asc)
# ------------------------------------------------------------------
def rank_axis(scores):
    order = sorted(range(len(scores)), key=lambda i: (-scores[i], i))
    ranks = [0] * len(scores)
    for r, idx in enumerate(order, start=1):
        ranks[idx] = r
    return ranks, order

AXIS_RANKS = {}
AXIS_ORDER = {}
# Binary/near-binary axes where 0-scoring verses should receive rank=6236
# (to prevent tie-break-by-index from populating top-100 with null hits)
ZERO_AS_RANK_INF = {"short_marker", "long_marker", "rhyme_density", "oath_density"}
for name in AXIS_NAMES:
    ranks, order = rank_axis(AXIS_SCORES[name])
    if name in ZERO_AS_RANK_INF:
        # Any verse with score 0 gets rank = 6236 (non-distinctive on this axis)
        for i in range(len(ranks)):
            if AXIS_SCORES[name][i] == 0.0:
                ranks[i] = 6236
        # Trim order to only non-zero scorers for top-100 identification
        order = [i for i in order if AXIS_SCORES[name][i] > 0.0]
    AXIS_RANKS[name] = ranks
    AXIS_ORDER[name] = order

# ------------------------------------------------------------------
# Cell A — Cross-axis rank-1 convergence
# ------------------------------------------------------------------
# For each axis, identify top-1 verse. Count how many unique verses; find max multiplicity.
AXIS_TOP1 = {name: AXIS_ORDER[name][0] for name in AXIS_NAMES if AXIS_ORDER[name]}
# Count multiplicity: how many axes is each verse rank-1 on?
rank1_counter = Counter(AXIS_TOP1.values())
max_mult_obs = max(rank1_counter.values())
verses_at_max_mult = [idx for idx, c in rank1_counter.items() if c == max_mult_obs]

# ------------------------------------------------------------------
# Cell B — Top-100 intersection atlas
# ------------------------------------------------------------------
TOP100 = {name: set(AXIS_ORDER[name][:100]) for name in AXIS_NAMES}
intersection_count = Counter()
for name in AXIS_NAMES:
    for idx in TOP100[name]:
        intersection_count[idx] += 1

dist = Counter(intersection_count.values())
# Verses in >=3, >=5, >=8
ge3 = sum(1 for c in intersection_count.values() if c >= 3)
ge5 = sum(1 for c in intersection_count.values() if c >= 5)
ge8 = sum(1 for c in intersection_count.values() if c >= 8)

# ------------------------------------------------------------------
# Cell C — Harmonic mean rank superverse top-100
# ------------------------------------------------------------------
# HMR = K / sum(1/r_i); use rank floor to handle out-of-top-500 (assign r=6236)
# Actually pre-reg says "outside top-500 contribute negligibly, assigned rank = 6236"
K = len(AXIS_NAMES)
hmr_scores = []
for idx in range(N):
    inv_sum = 0.0
    for name in AXIS_NAMES:
        r = AXIS_RANKS[name][idx]
        if r > 500:
            r = 6236  # negligible contribution
        inv_sum += 1.0 / r
    hmr = K / inv_sum if inv_sum > 0 else float("inf")
    hmr_scores.append(hmr)

# Lower HMR = better
superverse_order = sorted(range(N), key=lambda i: (hmr_scores[i], i))
superverse_top100 = superverse_order[:100]

# ------------------------------------------------------------------
# Cell D — Classical celebrated-verse hit rate
# ------------------------------------------------------------------
# Build (surah, verse) -> verse-index map
SV_TO_IDX = {(v["surah"], v["verse"]): i for i, v in enumerate(VERSES)}
CLASSICAL_CLUSTERS = {
    "Q 1:1 (Bismillah)": [(1, 1)],
    "Q 2:255 (Kursi)": [(2, 255)],
    "Q 24:35 (Nur)": [(24, 35)],
    "Q 59:22-24 (Khawatim)": [(59, 22), (59, 23), (59, 24)],
    "Q 112:1-4 (Ikhlas)": [(112, 1), (112, 2), (112, 3), (112, 4)],
}
super_top_set = set(superverse_top100)
cluster_hits = {}
for cname, verses in CLASSICAL_CLUSTERS.items():
    hits = []
    for (s, v) in verses:
        if (s, v) in SV_TO_IDX:
            idx = SV_TO_IDX[(s, v)]
            if idx in super_top_set:
                hits.append({"verse": f"Q {s}:{v}", "rank": superverse_order.index(idx) + 1, "hmr": hmr_scores[idx]})
    cluster_hits[cname] = hits

cluster_hit_count = sum(1 for h in cluster_hits.values() if h)

# ------------------------------------------------------------------
# Permutation null for Cells A and B
# ------------------------------------------------------------------
print(f"Running {N_PERM} permutations...")
rng = random.Random(SEED)

null_A = []  # max rank-1 multiplicity under null
null_B = []  # count of verses in >=3 top-100s under null

# Pre-extract index lists
all_indices = list(range(N))

for p in range(N_PERM):
    # For each axis, shuffle the verse ordering, take top-1 and top-100
    rank1 = Counter()
    top100_count = Counter()
    for name in AXIS_NAMES:
        perm_order = all_indices[:]
        rng.shuffle(perm_order)
        rank1[perm_order[0]] += 1
        for idx in perm_order[:100]:
            top100_count[idx] += 1
    max_m = max(rank1.values()) if rank1 else 0
    null_A.append(max_m)
    ge3_null = sum(1 for c in top100_count.values() if c >= 3)
    null_B.append(ge3_null)
    if (p + 1) % 2000 == 0:
        print(f"  perm {p+1}/{N_PERM}")

p_A = sum(1 for x in null_A if x >= max_mult_obs) / N_PERM
p_B = sum(1 for x in null_B if x >= ge3) / N_PERM

# ------------------------------------------------------------------
# Format outputs
# ------------------------------------------------------------------
def vlabel(idx):
    v = VERSES[idx]
    return f"Q {v['surah']}:{v['verse']}"

per_axis_top100 = {}
for name in AXIS_NAMES:
    per_axis_top100[name] = [
        {
            "rank": r + 1,
            "verse": vlabel(idx),
            "surah": VERSES[idx]["surah"],
            "ayah": VERSES[idx]["verse"],
            "score": round(AXIS_SCORES[name][idx], 6),
            "tokens": len(VERSES[idx]["tokens"]),
        }
        for r, idx in enumerate(AXIS_ORDER[name][:100])
    ]

superverse_top100_list = [
    {
        "rank": r + 1,
        "verse": vlabel(idx),
        "surah": VERSES[idx]["surah"],
        "ayah": VERSES[idx]["verse"],
        "hmr": round(hmr_scores[idx], 4),
        "per_axis_ranks": {name: AXIS_RANKS[name][idx] for name in AXIS_NAMES},
        "in_top100_count": intersection_count.get(idx, 0),
        "tokens": len(VERSES[idx]["tokens"]),
        "text_preview": VERSES[idx]["text"][:120],
    }
    for r, idx in enumerate(superverse_top100)
]

intersection_atlas = {
    "distribution": {str(k): dist[k] for k in sorted(dist)},
    "verses_in_ge3_top100s": ge3,
    "verses_in_ge5_top100s": ge5,
    "verses_in_ge8_top100s": ge8,
    "top_30_by_intersection": [
        {"verse": vlabel(idx), "count": c,
         "axes": [name for name in AXIS_NAMES if idx in TOP100[name]]}
        for idx, c in intersection_count.most_common(30)
    ],
}

cell_A = {
    "per_axis_rank1": {name: vlabel(AXIS_TOP1[name]) for name in AXIS_NAMES},
    "rank1_multiplicity_distribution": {str(k): v for k, v in sorted(rank1_counter.items())},
    "max_multiplicity_obs": max_mult_obs,
    "verses_at_max_multiplicity": [vlabel(idx) for idx in verses_at_max_mult],
    "null_mean_max_mult": round(sum(null_A) / len(null_A), 3),
    "null_max_max_mult": max(null_A),
    "p_value_A": p_A,
    "verdict": "PASS" if (p_A < 0.0125 and max_mult_obs >= 3) else "FAIL-DIRECTED",
}

cell_B = {
    "obs_verses_in_ge3_top100s": ge3,
    "threshold": 20,
    "null_mean_ge3": round(sum(null_B) / len(null_B), 3),
    "null_p95": sorted(null_B)[int(N_PERM * 0.95)],
    "null_max": max(null_B),
    "p_value_B": p_B,
    "verdict": "PASS" if (p_B < 0.0125 and ge3 >= 20) else "FAIL-DIRECTED",
}

cell_D = {
    "cluster_hits": cluster_hits,
    "hit_count": cluster_hit_count,
    "threshold": 3,
    "verdict": "PASS" if cluster_hit_count >= 3 else "FAIL-DIRECTED",
}

output = {
    "id": "H-NEW-128",
    "seed": SEED,
    "n_perm": N_PERM,
    "alpha_bon": 0.0125,
    "n_verses": N,
    "n_axes": len(AXIS_NAMES),
    "axis_names": AXIS_NAMES,
    "per_axis_top100": per_axis_top100,
    "intersection_atlas": intersection_atlas,
    "superverse_top100": superverse_top100_list,
    "cell_A": cell_A,
    "cell_B": cell_B,
    "cell_D": cell_D,
}

with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

print(f"\nWrote {OUT_JSON}")
print("\n==== CELL A ====")
print(f"  Max rank-1 multiplicity observed: {max_mult_obs}")
print(f"  Verses at max mult: {cell_A['verses_at_max_multiplicity']}")
print(f"  Null mean max mult: {cell_A['null_mean_max_mult']}, null max: {cell_A['null_max_max_mult']}")
print(f"  p_A = {p_A:.4f} ; verdict: {cell_A['verdict']}")
print("\n==== CELL B ====")
print(f"  Verses in >=3 top-100s: {ge3} (>=5: {ge5}; >=8: {ge8})")
print(f"  Null mean: {cell_B['null_mean_ge3']}, null p95: {cell_B['null_p95']}, null max: {cell_B['null_max']}")
print(f"  p_B = {p_B:.4f} ; verdict: {cell_B['verdict']}")
print("\n==== CELL C (superverse top-10) ====")
for rec in superverse_top100_list[:10]:
    print(f"  #{rec['rank']} {rec['verse']}  HMR={rec['hmr']}  tokens={rec['tokens']}  in-top100s={rec['in_top100_count']}")
print("\n==== CELL D ====")
for cname, hits in cluster_hits.items():
    if hits:
        print(f"  HIT  {cname}: {hits}")
    else:
        print(f"  MISS {cname}")
print(f"  Hit count: {cluster_hit_count} / 5  verdict: {cell_D['verdict']}")
print("\n==== Per-axis rank-1 verses ====")
for name in AXIS_NAMES:
    idx = AXIS_TOP1[name]
    print(f"  {name:<28}: {vlabel(idx)}  (score={AXIS_SCORES[name][idx]:.4f}, tokens={len(VERSES[idx]['tokens'])})")
