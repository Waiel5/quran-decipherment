#!/usr/bin/env python3
"""
Saj' (rhymed prose) analysis of the Quran.

For each verse, extract a 'fasila' (rhyme tail) by stripping all diacritics
and recitation marks from the LAST word, normalizing letter forms, and
taking the trailing 1, 2 and 3 consonants.

Outputs:
  - /Users/grey/Downloads/quran/findings/phase-b-hypotheses/saj-fasila-per-verse.csv
  - /Users/grey/Downloads/quran/findings/phase-b-hypotheses/saj-rhyme-analysis.md
  - intermediate JSON results for later inspection.
"""
import json
import os
import csv
import math
from collections import Counter, defaultdict

ROOT = "/Users/grey/Downloads/quran"
FULL = os.path.join(ROOT, "quran-text/quran-full-tashkeel.json")
NOTASH = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
TRANS = os.path.join(ROOT, "data/translations/en.sahih.txt")

OUT_CSV = os.path.join(ROOT, "findings/phase-b-hypotheses/saj-fasila-per-verse.csv")
OUT_MD = os.path.join(ROOT, "findings/phase-b-hypotheses/saj-rhyme-analysis.md")
OUT_JSON = os.path.join(ROOT, "analysis/notebooks/saj_rhyme_results.json")
CHIASTIC = os.path.join(ROOT, "analysis/notebooks/chiastic_audit_results.json")

# --- Letter normalization ---------------------------------------------------

# Diacritics, recitation marks, tatweel, shadda, sukun, maddah, etc.
# Anything in 064B..065F, 0670 (superscript alif), 0610..061A, 06D6..06ED, 0640 (tatweel)
DIACRITIC_RANGES = [
    (0x064B, 0x065F),
    (0x0670, 0x0670),  # superscript alif
    (0x06D6, 0x06ED),  # recitation marks
    (0x0610, 0x061A),
    (0x0640, 0x0640),  # tatweel
    (0x0656, 0x0657),  # subscript alif, inverted damma (these are diacritic-like)
]

def is_diacritic(cp):
    for lo, hi in DIACRITIC_RANGES:
        if lo <= cp <= hi:
            return True
    return False

# Letter normalization map: collapse hamza carriers, alif variants, alif maqsura.
NORM = {
    'أ': 'ا',  # alef with hamza above
    'إ': 'ا',  # alef with hamza below
    'آ': 'ا',  # alef with maddah
    'ٱ': 'ا',  # alef wasla
    'ٲ': 'ا',
    'ٳ': 'ا',
    'ؤ': 'و',  # waw with hamza
    'ئ': 'ي',  # yeh with hamza
    'ى': 'ا',  # alef maksura -> alef sound (pausal form rhymes with alif)
    'ة': 'ه',  # teh marbuta -> heh (pausal form is /h/ or null)
    'ٮ': 'ب',  # dotless beh (rare)
    'ك': 'ك',
}

# Real Arabic letter range: 0621..064A and 0671..06D3
def is_arabic_letter(c):
    cp = ord(c)
    return (0x0621 <= cp <= 0x064A) or (0x0671 <= cp <= 0x06D3)

def strip_to_consonants(word):
    """Strip diacritics and normalize letters; return consonant string."""
    out = []
    for c in word:
        if is_diacritic(ord(c)):
            continue
        if not is_arabic_letter(c):
            continue
        out.append(NORM.get(c, c))
    return "".join(out)

# --- Load data --------------------------------------------------------------

with open(FULL, encoding="utf-8") as f:
    surahs = json.load(f)

with open(TRANS, encoding="utf-8") as f:
    translations = [line.rstrip("\n") for line in f]

# build verse list with translation index
verses = []
trans_idx = 0
for s in surahs:
    sid = s["id"]
    for v in s["verses"]:
        text = v["text"]
        words = text.split()
        last_word = words[-1] if words else ""
        cons = strip_to_consonants(last_word)
        # word count for length analysis
        verses.append({
            "surah": sid,
            "verse": v["id"],
            "type": s["type"],
            "n_words": len(words),
            "last_word_raw": last_word,
            "last_word_cons": cons,
            "fasila_1": cons[-1:] if cons else "",
            "fasila_2": cons[-2:] if len(cons) >= 2 else cons,
            "fasila_3": cons[-3:] if len(cons) >= 3 else cons,
            "translation": translations[trans_idx] if trans_idx < len(translations) else "",
        })
        trans_idx += 1

assert len(verses) == 6236, f"verse count {len(verses)} != 6236"
print(f"Loaded {len(verses)} verses")

# --- Task 1: extraction & global frequency ---------------------------------

fasila3_counts = Counter(v["fasila_3"] for v in verses)
fasila2_counts = Counter(v["fasila_2"] for v in verses)
fasila1_counts = Counter(v["fasila_1"] for v in verses)

print(f"Distinct 3-cons fasila patterns: {len(fasila3_counts)}")
print(f"Distinct 2-cons fasila patterns: {len(fasila2_counts)}")
print(f"Distinct 1-cons fasila patterns: {len(fasila1_counts)}")

# Longest run of consecutive verses sharing fasila_2
def longest_run(verses, key):
    best_len = 0
    best_start = None
    best_pat = None
    cur_len = 0
    cur_start = 0
    cur_pat = None
    for i, v in enumerate(verses):
        p = v[key]
        if p == cur_pat and p:
            cur_len += 1
        else:
            if cur_len > best_len:
                best_len = cur_len
                best_start = cur_start
                best_pat = cur_pat
            cur_pat = p
            cur_len = 1
            cur_start = i
    if cur_len > best_len:
        best_len = cur_len
        best_start = cur_start
        best_pat = cur_pat
    return best_len, best_start, best_pat

# But runs across surah boundaries are not meaningful - restrict per-surah
def longest_run_within_surahs(verses, key):
    best = {"len": 0, "surah": None, "start_verse": None, "end_verse": None, "pat": None}
    by_surah = defaultdict(list)
    for v in verses:
        by_surah[v["surah"]].append(v)
    for sid, svs in by_surah.items():
        cur_len = 0
        cur_pat = None
        cur_start = None
        for v in svs:
            p = v[key]
            if p == cur_pat and p:
                cur_len += 1
            else:
                if cur_len > best["len"]:
                    best.update(len=cur_len, surah=sid, start_verse=cur_start, end_verse=cur_start + cur_len - 1, pat=cur_pat)
                cur_pat = p
                cur_len = 1
                cur_start = v["verse"]
        if cur_len > best["len"]:
            best.update(len=cur_len, surah=sid, start_verse=cur_start, end_verse=cur_start + cur_len - 1, pat=cur_pat)
    return best

longest_run_2 = longest_run_within_surahs(verses, "fasila_2")
longest_run_3 = longest_run_within_surahs(verses, "fasila_3")
print(f"Longest run (2-cons): {longest_run_2}")
print(f"Longest run (3-cons): {longest_run_3}")

# --- Task 2: per-surah rhyme uniformity score ------------------------------

surah_info = []
by_surah = defaultdict(list)
for v in verses:
    by_surah[v["surah"]].append(v)

for sid in sorted(by_surah):
    svs = by_surah[sid]
    n = len(svs)
    c1 = Counter(v["fasila_1"] for v in svs)
    c2 = Counter(v["fasila_2"] for v in svs)
    c3 = Counter(v["fasila_3"] for v in svs)
    top1_pat, top1_n = c1.most_common(1)[0]
    top2_pat, top2_n = c2.most_common(1)[0]
    top3_pat, top3_n = c3.most_common(1)[0]
    surah_info.append({
        "surah": sid,
        "name": surahs[sid-1]["transliteration"],
        "type": surahs[sid-1]["type"],
        "n_verses": n,
        "top_fasila1": top1_pat,
        "top_fasila1_count": top1_n,
        "uniformity1": top1_n / n,
        "top_fasila2": top2_pat,
        "top_fasila2_count": top2_n,
        "uniformity2": top2_n / n,
        "top_fasila3": top3_pat,
        "top_fasila3_count": top3_n,
        "uniformity3": top3_n / n,
        "n_distinct_fasila2": len(c2),
        "n_distinct_fasila3": len(c3),
    })

# Sort by uniformity1 (final-letter rhyme — closest to classical "rawi" notion) desc
surah_info_sorted_1 = sorted(surah_info, key=lambda r: -r["uniformity1"])
surah_info_sorted_2 = sorted(surah_info, key=lambda r: -r["uniformity2"])
top20_1 = surah_info_sorted_1[:20]
top20 = surah_info_sorted_2[:20]
bot20 = sorted(surah_info, key=lambda r: r["uniformity2"])[:20]
bot20_1 = sorted(surah_info, key=lambda r: r["uniformity1"])[:20]

# --- Task 3: rhyme-breakers in top-20 uniform surahs -----------------------

rhyme_breakers = []
for r in top20:
    sid = r["surah"]
    top_pat = r["top_fasila2"]
    for v in by_surah[sid]:
        if v["fasila_2"] != top_pat:
            rhyme_breakers.append({
                "surah": sid,
                "name": r["name"],
                "verse": v["verse"],
                "type": r["type"],
                "fasila_2": v["fasila_2"],
                "expected": top_pat,
                "n_words": v["n_words"],
                "translation": v["translation"],
            })

# --- Task 4: Ar-Rahman refrain --------------------------------------------

def normalize_full(text):
    out = []
    for c in text:
        if is_diacritic(ord(c)):
            continue
        if not is_arabic_letter(c):
            continue
        # Drop bare hamza (ء U+0621) from skeleton — orthographic variant
        if c == 'ء':
            continue
        out.append(NORM.get(c, c))
    return "".join(out)

# Use the corpus's own verse 55:13 as the gold refrain — avoids encoding mismatches
ar_rahman = surahs[54]  # surah 55, index 54
refrain_skel = normalize_full(ar_rahman["verses"][12]["text"])  # verse 13 (0-indexed 12)
print(f"Ar-Rahman refrain skeleton: {refrain_skel}")
refrain_verses = []
non_refrain = []
for v in ar_rahman["verses"]:
    skel = normalize_full(v["text"])
    is_refrain = (skel == refrain_skel)
    if is_refrain:
        refrain_verses.append(v["id"])
    else:
        non_refrain.append(v["id"])

print(f"Ar-Rahman: {len(refrain_verses)} refrain occurrences")
# Compute gaps between refrains
gaps = []
prev = 0
for r in refrain_verses:
    gap = r - prev - 1
    gaps.append((prev, r, gap))
    prev = r
gaps.append((prev, ar_rahman["total_verses"], ar_rahman["total_verses"] - prev))
print("Refrain gaps:", gaps)

# --- Task 5: rhyme-based ring score ---------------------------------------

def ring_score_rhyme(svs, key="fasila_2"):
    """Compute the average pair-match score: for surah length N, pair v_i and v_{N+1-i}.
    Score = 1 if same fasila, else 0. Average over floor(N/2) pairs."""
    n = len(svs)
    if n < 2:
        return None, 0
    pairs = n // 2
    matches = 0
    for i in range(pairs):
        a = svs[i][key]
        b = svs[n - 1 - i][key]
        if a and a == b:
            matches += 1
    return matches / pairs, pairs

import random

def ring_score_with_null(svs, key="fasila_2", n_trials=200, seed=0):
    obs, n_pairs = ring_score_rhyme(svs, key)
    if obs is None:
        return None
    rng = random.Random(seed)
    fasilas = [v[key] for v in svs]
    null_scores = []
    for t in range(n_trials):
        rng.shuffle(fasilas)
        n = len(fasilas)
        m = 0
        for i in range(n // 2):
            if fasilas[i] and fasilas[i] == fasilas[n - 1 - i]:
                m += 1
        null_scores.append(m / (n // 2))
    mean_null = sum(null_scores) / len(null_scores)
    var_null = sum((x - mean_null) ** 2 for x in null_scores) / len(null_scores)
    std_null = math.sqrt(var_null) if var_null > 0 else 0.0
    z = (obs - mean_null) / std_null if std_null > 0 else 0.0
    p_emp = sum(1 for x in null_scores if x >= obs) / len(null_scores)
    return {"obs": obs, "mean_null": mean_null, "std_null": std_null, "z": z, "p_emp": p_emp, "n_pairs": n_pairs}

ring_results = []
for sid in sorted(by_surah):
    svs = by_surah[sid]
    if len(svs) < 4:
        continue
    r = ring_score_with_null(svs, key="fasila_2", n_trials=500, seed=sid * 7919)
    r["surah"] = sid
    r["name"] = surahs[sid-1]["transliteration"]
    r["type"] = surahs[sid-1]["type"]
    r["n_verses"] = len(svs)
    ring_results.append(r)

ring_results_sorted = sorted(ring_results, key=lambda r: -r["z"])

# Compare with chiastic root-based scores
with open(CHIASTIC, encoding="utf-8") as f:
    chiastic_data = json.load(f)

root_z_by_surah = {s["id"]: s["z"] for s in chiastic_data["all_surah_scores"]}
rhyme_z_by_surah = {r["surah"]: r["z"] for r in ring_results}

# Compute Pearson correlation between root_z and rhyme_z over the surahs both have
common_surahs = sorted(set(root_z_by_surah) & set(rhyme_z_by_surah))
xs = [root_z_by_surah[s] for s in common_surahs]
ys = [rhyme_z_by_surah[s] for s in common_surahs]
nx = len(xs)
mx = sum(xs) / nx
my = sum(ys) / nx
sxy = sum((xs[i] - mx) * (ys[i] - my) for i in range(nx))
sxx = sum((xs[i] - mx) ** 2 for i in range(nx))
syy = sum((ys[i] - my) ** 2 for i in range(nx))
pearson_r = sxy / math.sqrt(sxx * syy) if sxx and syy else 0.0
print(f"Pearson r between root-ring z and rhyme-ring z (n={nx}): {pearson_r:.4f}")

# --- Task 6: fasila final letter histogram vs general letter freq ---------

verse_end_letters = Counter(v["fasila_1"] for v in verses if v["fasila_1"])

# General letter freq across the whole Quran (full-tashkeel, normalized to consonants)
all_consonants = Counter()
for s in surahs:
    for v in s["verses"]:
        for c in v["text"]:
            if is_diacritic(ord(c)):
                continue
            if not is_arabic_letter(c):
                continue
            n = NORM.get(c, c)
            all_consonants[n] += 1
total_letters = sum(all_consonants.values())
total_endings = sum(verse_end_letters.values())

letter_compare = []
for letter, freq in sorted(all_consonants.items(), key=lambda kv: -kv[1]):
    end_freq = verse_end_letters.get(letter, 0)
    letter_pct_text = freq / total_letters
    letter_pct_end = end_freq / total_endings
    over = letter_pct_end / letter_pct_text if letter_pct_text > 0 else 0.0
    letter_compare.append({
        "letter": letter,
        "freq_total": freq,
        "pct_text": letter_pct_text,
        "freq_end": end_freq,
        "pct_end": letter_pct_end,
        "over_rep": over,
    })
letter_compare.sort(key=lambda r: -r["over_rep"])

# --- Task 7: Meccan vs Medinan rhyme density (consecutive same-rhyme runs) -

def avg_run_length(svs, key="fasila_2"):
    n = len(svs)
    runs = []
    cur = 1
    for i in range(1, n):
        if svs[i][key] == svs[i-1][key] and svs[i][key]:
            cur += 1
        else:
            runs.append(cur)
            cur = 1
    runs.append(cur)
    return sum(runs) / len(runs), max(runs), runs

mec_runs = []
med_runs = []
mec_unif = []
med_unif = []
mec_unif1 = []
med_unif1 = []
mec_max = 0
med_max = 0
mec_vlen = []
med_vlen = []
mec_runs1 = []
med_runs1 = []
for sid in sorted(by_surah):
    svs = by_surah[sid]
    avg, mx, runs = avg_run_length(svs, "fasila_2")
    avg1, mx1, _ = avg_run_length(svs, "fasila_1")
    info = next(r for r in surah_info if r["surah"] == sid)
    mean_words = sum(v["n_words"] for v in svs) / len(svs)
    if surahs[sid-1]["type"] == "meccan":
        mec_runs.append(avg)
        mec_runs1.append(avg1)
        mec_unif.append(info["uniformity2"])
        mec_unif1.append(info["uniformity1"])
        mec_max = max(mec_max, mx)
        mec_vlen.append(mean_words)
    else:
        med_runs.append(avg)
        med_runs1.append(avg1)
        med_unif.append(info["uniformity2"])
        med_unif1.append(info["uniformity1"])
        med_max = max(med_max, mx)
        med_vlen.append(mean_words)

mec_mean = sum(mec_runs) / len(mec_runs)
med_mean = sum(med_runs) / len(med_runs)
mec_mean1 = sum(mec_runs1) / len(mec_runs1)
med_mean1 = sum(med_runs1) / len(med_runs1)
mec_unif_mean = sum(mec_unif) / len(mec_unif)
med_unif_mean = sum(med_unif) / len(med_unif)
mec_unif1_mean = sum(mec_unif1) / len(mec_unif1)
med_unif1_mean = sum(med_unif1) / len(med_unif1)
mec_vlen_mean = sum(mec_vlen) / len(mec_vlen)
med_vlen_mean = sum(med_vlen) / len(med_vlen)
print(f"Meccan: avg-run-len(2)={mec_mean:.3f}, avg-run-len(1)={mec_mean1:.3f}, U2={mec_unif_mean:.3f}, U1={mec_unif1_mean:.3f}, words/v={mec_vlen_mean:.2f}, n={len(mec_runs)}")
print(f"Medinan: avg-run-len(2)={med_mean:.3f}, avg-run-len(1)={med_mean1:.3f}, U2={med_unif_mean:.3f}, U1={med_unif1_mean:.3f}, words/v={med_vlen_mean:.2f}, n={len(med_runs)}")

# Welch's t test approximation
def welch_t(a, b):
    na, nb = len(a), len(b)
    ma, mb = sum(a)/na, sum(b)/nb
    va = sum((x-ma)**2 for x in a) / (na-1)
    vb = sum((x-mb)**2 for x in b) / (nb-1)
    se = math.sqrt(va/na + vb/nb)
    t = (ma - mb) / se if se > 0 else 0
    df = (va/na + vb/nb)**2 / ((va/na)**2/(na-1) + (vb/nb)**2/(nb-1))
    return t, df, ma - mb

t_stat, df, diff = welch_t(mec_runs, med_runs)
print(f"Welch t (avg-run-len_2) ={t_stat:.3f} df={df:.1f} diff={diff:.3f}")
t_stat1, df1, diff1 = welch_t(mec_runs1, med_runs1)
print(f"Welch t (avg-run-len_1) ={t_stat1:.3f} df={df1:.1f} diff={diff1:.3f}")
t_unif, df_u, diff_u = welch_t(mec_unif, med_unif)
print(f"Welch t (uniformity2) ={t_unif:.3f} df={df_u:.1f} diff={diff_u:.3f}")
t_unif1, df_u1, diff_u1 = welch_t(mec_unif1, med_unif1)
print(f"Welch t (uniformity1) ={t_unif1:.3f} df={df_u1:.1f} diff={diff_u1:.3f}")
t_vlen, df_vl, diff_vl = welch_t(mec_vlen, med_vlen)
print(f"Welch t (mean words/verse) ={t_vlen:.3f} df={df_vl:.1f} diff={diff_vl:.3f}")

# Permutation test on the type label
import random as pyrand
def perm_p(values, labels, obs_diff, n_perm=10000, seed=42):
    rng = pyrand.Random(seed)
    labs = list(labels)
    hits = 0
    for _ in range(n_perm):
        rng.shuffle(labs)
        a = [values[i] for i in range(len(values)) if labs[i]=="m"]
        b = [values[i] for i in range(len(values)) if labs[i]=="d"]
        diff_p = abs(sum(a)/len(a) - sum(b)/len(b))
        if diff_p >= obs_diff:
            hits += 1
    return (hits + 1) / (n_perm + 1)

all_runs = mec_runs + med_runs
all_runs1 = mec_runs1 + med_runs1
all_unif = mec_unif + med_unif
all_unif1 = mec_unif1 + med_unif1
all_vlen = mec_vlen + med_vlen
labels = ["m"]*len(mec_runs) + ["d"]*len(med_runs)

p_perm_runs = perm_p(all_runs, labels, abs(mec_mean - med_mean))
p_perm_runs1 = perm_p(all_runs1, labels, abs(mec_mean1 - med_mean1))
p_perm_unif = perm_p(all_unif, labels, abs(mec_unif_mean - med_unif_mean))
p_perm_unif1 = perm_p(all_unif1, labels, abs(mec_unif1_mean - med_unif1_mean))
p_perm_vlen = perm_p(all_vlen, labels, abs(mec_vlen_mean - med_vlen_mean))
p_perm = p_perm_runs1
print(f"Permutation p (Mec vs Med, run-len_2): {p_perm_runs:.5f}")
print(f"Permutation p (Mec vs Med, run-len_1): {p_perm_runs1:.5f}")
print(f"Permutation p (Mec vs Med, uniformity2): {p_perm_unif:.5f}")
print(f"Permutation p (Mec vs Med, uniformity1): {p_perm_unif1:.5f}")
print(f"Permutation p (Mec vs Med, mean words/verse): {p_perm_vlen:.5f}")

# --- Task 8: cross-surah rhyme linkage ------------------------------------

# For each rare fasila3 pattern (occurring < 10 times), record the set of surahs.
# Find pairs of surahs that share an unusual fasila3 NOT shared with the rest of the corpus.
fasila3_to_surahs = defaultdict(set)
for v in verses:
    fasila3_to_surahs[v["fasila_3"]].add(v["surah"])

# Cross-surah linkage candidates: fasila3 used in exactly 2 surahs, with > 1 occurrence in each
surah_pair_links = defaultdict(list)
for pat, ss in fasila3_to_surahs.items():
    if len(ss) == 2:
        # count occurrences
        counts = Counter(v["surah"] for v in verses if v["fasila_3"] == pat)
        if all(c >= 2 for c in counts.values()) and sum(counts.values()) >= 4:
            pair = tuple(sorted(ss))
            surah_pair_links[pair].append({
                "pat": pat,
                "counts": dict(counts),
                "total": sum(counts.values()),
            })

cross_linked_pairs = sorted(
    [(p, items) for p, items in surah_pair_links.items()],
    key=lambda x: -sum(it["total"] for it in x[1])
)[:20]

# --- Task 9: verse length vs rhyme adherence -------------------------------

# For each surah with uniformity2 > 0.5, compute Spearman/correlation between
# n_words and binary "matches top fasila".
length_rhyme_corr_per_surah = []
for r in surah_info:
    sid = r["surah"]
    if r["uniformity2"] < 0.5 or r["n_verses"] < 10:
        continue
    svs = by_surah[sid]
    matches = [1 if v["fasila_2"] == r["top_fasila2"] else 0 for v in svs]
    lens = [v["n_words"] for v in svs]
    n = len(svs)
    mn_l = sum(lens) / n
    mn_m = sum(matches) / n
    cov = sum((lens[i]-mn_l)*(matches[i]-mn_m) for i in range(n)) / n
    var_l = sum((x-mn_l)**2 for x in lens) / n
    var_m = sum((x-mn_m)**2 for x in matches) / n
    if var_l == 0 or var_m == 0:
        continue
    pr = cov / math.sqrt(var_l * var_m)
    length_rhyme_corr_per_surah.append({
        "surah": sid,
        "name": surahs[sid-1]["transliteration"],
        "n_verses": n,
        "uniformity2": r["uniformity2"],
        "mean_words_match": sum(lens[i] for i in range(n) if matches[i]) / max(1, sum(matches)),
        "mean_words_break": sum(lens[i] for i in range(n) if not matches[i]) / max(1, n - sum(matches)),
        "pearson_r_len_match": pr,
    })
# Sort by absolute pearson
length_rhyme_corr_per_surah.sort(key=lambda r: r["pearson_r_len_match"])

# Whole-corpus: long verses lax?
all_match_len = []
all_break_len = []
for r in surah_info:
    if r["uniformity2"] < 0.5 or r["n_verses"] < 10:
        continue
    sid = r["surah"]
    top = r["top_fasila2"]
    for v in by_surah[sid]:
        (all_match_len if v["fasila_2"] == top else all_break_len).append(v["n_words"])
mean_match = sum(all_match_len)/len(all_match_len) if all_match_len else 0
mean_break = sum(all_break_len)/len(all_break_len) if all_break_len else 0
print(f"Across uniform surahs: matching verse mean words = {mean_match:.2f}, breaking verse mean words = {mean_break:.2f}")
t_lr, df_lr, diff_lr = welch_t(all_match_len, all_break_len)
print(f"Welch t for length-vs-match: t={t_lr:.3f} df={df_lr:.1f} diff={diff_lr:.3f}")

# --- Save results ----------------------------------------------------------

# CSV per-verse
os.makedirs(os.path.dirname(OUT_CSV), exist_ok=True)
with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
    w = csv.writer(f)
    w.writerow(["surah", "verse", "fasila_2char", "fasila_3char", "ends_in_letter"])
    for v in verses:
        w.writerow([v["surah"], v["verse"], v["fasila_2"], v["fasila_3"], v["fasila_1"]])

# JSON
results = {
    "n_verses": len(verses),
    "n_distinct_fasila2": len(fasila2_counts),
    "n_distinct_fasila3": len(fasila3_counts),
    "top_fasila2": fasila2_counts.most_common(20),
    "top_fasila3": fasila3_counts.most_common(20),
    "longest_run_2": longest_run_2,
    "longest_run_3": longest_run_3,
    "surah_info_top20_uniform": top20,
    "surah_info_bot20_varied": bot20,
    "surah_info_top20_uniform_letter": top20_1,
    "surah_info_bot20_varied_letter": bot20_1,
    "surah_info_all": surah_info_sorted_1,
    "rhyme_breakers": rhyme_breakers,
    "rahman_refrain_count": len(refrain_verses),
    "rahman_refrain_verses": refrain_verses,
    "rahman_gaps": gaps,
    "ring_results_top20": ring_results_sorted[:20],
    "ring_results_bot10": ring_results_sorted[-10:],
    "pearson_root_vs_rhyme_z": pearson_r,
    "letter_compare_top": letter_compare[:30],
    "verse_end_letters": dict(verse_end_letters.most_common()),
    "mec_mean_run": mec_mean,
    "med_mean_run": med_mean,
    "mec_mean_run_letter": mec_mean1,
    "med_mean_run_letter": med_mean1,
    "mec_max_run": mec_max,
    "med_max_run": med_max,
    "mec_unif_mean": mec_unif_mean,
    "med_unif_mean": med_unif_mean,
    "mec_unif1_mean": mec_unif1_mean,
    "med_unif1_mean": med_unif1_mean,
    "mec_vlen_mean": mec_vlen_mean,
    "med_vlen_mean": med_vlen_mean,
    "welch_t_mec_med_runs": {"t": t_stat, "df": df, "diff": diff},
    "welch_t_mec_med_runs_letter": {"t": t_stat1, "df": df1, "diff": diff1},
    "welch_t_mec_med_unif": {"t": t_unif, "df": df_u, "diff": diff_u},
    "welch_t_mec_med_unif_letter": {"t": t_unif1, "df": df_u1, "diff": diff_u1},
    "welch_t_mec_med_vlen": {"t": t_vlen, "df": df_vl, "diff": diff_vl},
    "perm_p_runs": p_perm_runs,
    "perm_p_runs_letter": p_perm_runs1,
    "perm_p_unif": p_perm_unif,
    "perm_p_unif_letter": p_perm_unif1,
    "perm_p_vlen": p_perm_vlen,
    "cross_linked_pairs": [
        {"pair": list(p), "items": items} for p, items in cross_linked_pairs
    ],
    "length_match_break": {"mean_match": mean_match, "mean_break": mean_break, "welch_t": t_lr},
    "length_corr_per_surah": length_rhyme_corr_per_surah[:15],
}

with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2, default=str)
print(f"Wrote {OUT_JSON}")
print(f"Wrote {OUT_CSV}")
