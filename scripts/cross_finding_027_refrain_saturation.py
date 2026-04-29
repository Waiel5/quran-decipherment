#!/usr/bin/env python3
"""
cross-finding-027: iʿjāz al-takrīr (refrain-saturation iʿjāz)

Tests whether per-surah refrain-saturation defines a third architectural axis
orthogonal to al-Bāqillānī's iʿjāz al-fawāṣil (sig_A) and moderately positively
correlated with UAS.

Pre-reg: findings/cross-finding/cross-finding-027-prereg.md
SHA256:  14b4ae8876f92c28081a1d54ab0f61eeddff215327d8bc66e37fc76633d9c1ec

Stdlib-only (json, hashlib, random, math, re, os, glob).
"""

import json
import hashlib
import random
import math
import re
import os
import glob

# ---- SHA-lock guard ----------------------------------------------------------
PREREG_PATH = "/Users/grey/Downloads/quran/findings/cross-finding/cross-finding-027-prereg.md"
EXPECTED_SHA = "14b4ae8876f92c28081a1d54ab0f61eeddff215327d8bc66e37fc76633d9c1ec"

with open(PREREG_PATH, "rb") as f:
    actual = hashlib.sha256(f.read()).hexdigest()
if actual != EXPECTED_SHA:
    raise SystemExit(
        f"PRE-REG SHA MISMATCH:\n  expected {EXPECTED_SHA}\n  actual   {actual}\n"
        "Pre-reg has been modified post-lock. Aborting per protocol."
    )

# ---- constants ---------------------------------------------------------------
SEED = 20260428
N_PERM = 10000
QURAN_NO_TASHKEEL = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
QURAN_MIN_TASHKEEL = "/Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json"
H750 = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json"
H840 = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-840.json"
BASELINE_DIR = "/Users/grey/Downloads/quran/data/baseline-corpora/raw"
OUT_JSON = "/Users/grey/Downloads/quran/findings/cross-finding/csv/cross-finding-027.json"

# nominated cluster (from Q 55 specialist proposal)
CLUSTER = [26, 55, 70, 77, 109]

# rules-tuple constant
RULES_TUPLE = [
    "no-tashkeel",
    "orthographic-token",
    "alif-normalized: ءا->ا, [إأآٱ]->ا, ى->ي",
    "words-as-units",
    "basmala-counted-only-in-Q1",
    "Hafs-Kufan",
    "Mashriqi",
]

# ---- utilities ---------------------------------------------------------------
ARABIC_DIACRITICS = re.compile(r"[ً-ْٰٖٗ٘ـ]")

def strip_tashkeel(s: str) -> str:
    return ARABIC_DIACRITICS.sub("", s)

def alif_normalize(s: str) -> str:
    s = s.replace("ءا", "ا")
    for ch in "إأآٱ":
        s = s.replace(ch, "ا")
    s = s.replace("ى", "ي")
    return s

def tokenize(text: str):
    text = alif_normalize(strip_tashkeel(text))
    # split on whitespace + punctuation
    toks = re.split(r"[\s؁-؏ؐ-؟٭‌‍\.\,\;\:\!\?\(\)\[\]\"\'\-]+", text)
    return [t for t in toks if t.strip()]

def saturation_score(words, n_range=(3, 4, 5, 6)):
    """Returns (sat_score, best_n, best_ngram, best_count, n_words)."""
    L = len(words)
    if L < min(n_range):
        return 0.0, None, None, 0, L
    best_score = 0.0
    best_n = None
    best_ngram = None
    best_count = 0
    for N in n_range:
        if L < N:
            continue
        counts = {}
        for i in range(L - N + 1):
            ng = tuple(words[i:i+N])
            counts[ng] = counts.get(ng, 0) + 1
        if not counts:
            continue
        ng, c = max(counts.items(), key=lambda kv: kv[1])
        cov = c * N / L
        if cov > best_score:
            best_score = cov
            best_n = N
            best_ngram = ng
            best_count = c
    return best_score, best_n, best_ngram, best_count, L

# ---- load data ---------------------------------------------------------------
print("[1/6] loading Quran (no-tashkeel)...")
with open(QURAN_NO_TASHKEEL, encoding="utf-8") as f:
    quran = json.load(f)

print("[2/6] loading H-NEW-750 (sig_A) and H-NEW-840 (UAS)...")
with open(H750) as f:
    h750 = json.load(f)
with open(H840) as f:
    h840 = json.load(f)

sig_A_by_surah = {row["surah"]: row["sig_A"] for row in h750["per_surah"]}
uas_by_surah = {row["surah"]: row["UAS"] for row in h840["all_uas"]}

# ---- compute per-surah saturation -------------------------------------------
print("[3/6] computing per-surah refrain-saturation (no-tashkeel)...")
results = []
for surah in quran:
    sid = surah["id"]
    # join verse texts; do NOT include surah name. Basmala only in Q1.
    verses_text = " ".join(v["text"] for v in surah["verses"])
    if sid != 1:
        # remove leading basmala if it appears in any non-Q1 verses (Q1 only by rule)
        # (the no-tashkeel JSON includes basmala only in Q1's verse 1; Q9 has none;
        # other surahs have it as a *separate* opening NOT in verse list. Confirmed.)
        pass
    words = tokenize(verses_text)
    sat, N, ngram, c, L = saturation_score(words)
    results.append({
        "surah": sid,
        "name": surah["name"],
        "n_words": L,
        "sat": sat,
        "best_N": N,
        "best_count": c,
        "best_ngram": " ".join(ngram) if ngram else None,
    })

# rank
results_sorted = sorted(results, key=lambda r: -r["sat"])
for rank, r in enumerate(results_sorted, 1):
    r["rank"] = rank

# attach sig_A and UAS
for r in results_sorted:
    r["sig_A"] = sig_A_by_surah.get(r["surah"])
    r["UAS"] = uas_by_surah.get(r["surah"])

# convenient lookup
sat_by_surah = {r["surah"]: r["sat"] for r in results_sorted}
rank_by_surah = {r["surah"]: r["rank"] for r in results_sorted}

# ---- min-tashkeel cross-validation (Q 55 only + top-10 stability) -----------
print("[4/6] min-tashkeel cross-validation for Q 55 + corpus top-10...")
with open(QURAN_MIN_TASHKEEL, encoding="utf-8") as f:
    quran_min = json.load(f)

cross_check = {}
top10_surahs = [r["surah"] for r in results_sorted[:10]]
for surah in quran_min:
    sid = surah["id"]
    if sid not in top10_surahs and sid != 55:
        continue
    verses_text = " ".join(v["text"] for v in surah["verses"])
    words = tokenize(verses_text)
    sat, N, ngram, c, L = saturation_score(words)
    cross_check[sid] = {
        "sat_min_tashkeel": sat,
        "sat_no_tashkeel": sat_by_surah[sid],
        "rel_delta": (sat - sat_by_surah[sid]) / max(sat_by_surah[sid], 1e-9),
        "best_N": N,
        "best_count": c,
        "best_ngram": " ".join(ngram) if ngram else None,
    }

# ---- correlation tests (Pearson + permutation null) -------------------------
print("[5/6] correlation tests + permutation nulls (10000 perms each)...")

def pearson(xs, ys):
    n = len(xs)
    mx = sum(xs)/n
    my = sum(ys)/n
    num = sum((x-mx)*(y-my) for x, y in zip(xs, ys))
    sx2 = sum((x-mx)**2 for x in xs)
    sy2 = sum((y-my)**2 for y in ys)
    den = math.sqrt(sx2 * sy2)
    return num/den if den > 0 else 0.0

# build aligned arrays in canonical surah order 1..114
ordered = sorted(results_sorted, key=lambda r: r["surah"])
sat_arr  = [r["sat"]   for r in ordered]
sigA_arr = [r["sig_A"] for r in ordered]
uas_arr  = [r["UAS"]   for r in ordered]

r_sat_sigA = pearson(sat_arr, sigA_arr)
r_sat_uas  = pearson(sat_arr, uas_arr)

# permutation nulls
rng = random.Random(SEED)
perm_geq_sigA = 0  # for two-sided test on |r|
perm_geq_uas = 0   # for one-sided test on r > 0
for _ in range(N_PERM):
    perm_sigA = sigA_arr[:]
    rng.shuffle(perm_sigA)
    if abs(pearson(sat_arr, perm_sigA)) >= abs(r_sat_sigA):
        perm_geq_sigA += 1
    perm_uas = uas_arr[:]
    rng.shuffle(perm_uas)
    if pearson(sat_arr, perm_uas) >= r_sat_uas:
        perm_geq_uas += 1

p_sat_sigA = (perm_geq_sigA + 1) / (N_PERM + 1)  # two-sided permutation
p_sat_uas  = (perm_geq_uas + 1) / (N_PERM + 1)   # one-sided positive

# ---- cross-corpus baseline (pre-Islamic poetry) -----------------------------
print("[6/6] cross-corpus refrain-saturation control (pre-Islamic poetry)...")

baseline_files = sorted([
    f for f in glob.glob(os.path.join(BASELINE_DIR, "*.txt"))
    if "muallaqa" in os.path.basename(f) or "diwan" in os.path.basename(f)
])
# avoid OpenITI raw duplicates -- use the .txt that is NOT .openiti.raw
baseline_files = [f for f in baseline_files if ".openiti.raw" not in f and ".raw.txt" not in f]

q55_word_count = next(r["n_words"] for r in results_sorted if r["surah"] == 55)
BLOCK = q55_word_count  # 350-ish words; matches Q55 length proxy
q55_sat = sat_by_surah[55]

baseline_block_results = []
for fp in baseline_files:
    with open(fp, encoding="utf-8") as f:
        text = f.read()
    words = tokenize(text)
    if len(words) < BLOCK:
        continue
    n_blocks = len(words) // BLOCK
    block_sats = []
    for b in range(n_blocks):
        block = words[b*BLOCK:(b+1)*BLOCK]
        sat, N, ngram, c, L = saturation_score(block)
        block_sats.append({
            "block": b,
            "sat": sat,
            "best_N": N,
            "best_count": c,
            "best_ngram": " ".join(ngram) if ngram else None,
        })
    if block_sats:
        baseline_block_results.append({
            "file": os.path.basename(fp),
            "n_blocks": n_blocks,
            "max_sat": max(b["sat"] for b in block_sats),
            "mean_sat": sum(b["sat"] for b in block_sats)/len(block_sats),
            "blocks_geq_q55": sum(1 for b in block_sats if b["sat"] >= q55_sat),
        })

total_blocks = sum(b["n_blocks"] for b in baseline_block_results)
blocks_geq_q55 = sum(b["blocks_geq_q55"] for b in baseline_block_results)
p_cross_corpus = (blocks_geq_q55 + 1) / (total_blocks + 1) if total_blocks > 0 else 1.0

# ---- decision rules ---------------------------------------------------------
ALPHA_BON = 0.05 / 3

# H1a passes if |r(sat, sig_A)| < 0.30 AND p_sat_sigA > ALPHA_BON
#   (i.e., correlation is small AND not significantly different from null)
H1a_pass = (abs(r_sat_sigA) < 0.30) and (p_sat_sigA > ALPHA_BON)

# H1b passes if 0.10 < r(sat, UAS) < 0.60 AND p_sat_uas < ALPHA_BON (positive direction sig)
H1b_pass = (0.10 < r_sat_uas < 0.60) and (p_sat_uas < ALPHA_BON)

# H1c (descriptive): count of CLUSTER in top-10
cluster_in_top10 = [s for s in CLUSTER if rank_by_surah[s] <= 10]
H1c_count = len(cluster_in_top10)
H1c_descriptive_pass = H1c_count >= 3

# H1d passes if Q55 sat > all baseline blocks (p < ALPHA_BON)
H1d_pass = (p_cross_corpus < ALPHA_BON)

passes = sum([H1a_pass, H1b_pass, H1d_pass])
if passes == 3:
    verdict = "CONFIRMED-3RD-AXIS"
elif passes == 2:
    verdict = "DIRECTIONAL"
else:
    verdict = "FALSIFIED"

# ---- POST-HOC: recurrence-restricted saturation (count >= 2) ----------------
# Rationale: the pre-registered coverage_N metric is dominated by inverse-length
# artifacts when count=1 (any 6-gram in a 10-word surah = 60% saturation).
# The intent of "refrain-saturation" was *recurrent* phrases. We re-compute
# under the constraint count >= 2 as a SECONDARY test under MW-7 single-test-α
# = 0.05 ceiling (post-hoc move; cannot upgrade verdict, only inform).
print("\n[POST-HOC, MW-7 capped] recurrence-restricted saturation (count>=2)...")

def saturation_score_recurrent(words, n_range=(3, 4, 5, 6), min_count=2):
    L = len(words)
    best_score = 0.0
    best_n = None
    best_ngram = None
    best_count = 0
    for N in n_range:
        if L < N:
            continue
        counts = {}
        for i in range(L - N + 1):
            ng = tuple(words[i:i+N])
            counts[ng] = counts.get(ng, 0) + 1
        if not counts:
            continue
        ng, c = max(counts.items(), key=lambda kv: kv[1])
        if c < min_count:
            continue
        cov = c * N / L
        if cov > best_score:
            best_score = cov
            best_n = N
            best_ngram = ng
            best_count = c
    return best_score, best_n, best_ngram, best_count, L

results_recurrent = []
for surah in quran:
    sid = surah["id"]
    verses_text = " ".join(v["text"] for v in surah["verses"])
    words = tokenize(verses_text)
    sat, N, ngram, c, L = saturation_score_recurrent(words)
    results_recurrent.append({
        "surah": sid,
        "name": surah["name"],
        "n_words": L,
        "sat_recurrent": sat,
        "best_N": N,
        "best_count": c,
        "best_ngram": " ".join(ngram) if ngram else None,
    })
results_recurrent_sorted = sorted(results_recurrent, key=lambda r: -r["sat_recurrent"])
for rank, r in enumerate(results_recurrent_sorted, 1):
    r["rank_recurrent"] = rank
    r["sig_A"] = sig_A_by_surah.get(r["surah"])
    r["UAS"] = uas_by_surah.get(r["surah"])

sat_rec_by_surah = {r["surah"]: r["sat_recurrent"] for r in results_recurrent_sorted}
rank_rec_by_surah = {r["surah"]: r["rank_recurrent"] for r in results_recurrent_sorted}

# correlations under recurrent metric
ord_rec = sorted(results_recurrent_sorted, key=lambda r: r["surah"])
sat_rec_arr = [r["sat_recurrent"] for r in ord_rec]
sigA_arr2   = [r["sig_A"]         for r in ord_rec]
uas_arr2    = [r["UAS"]           for r in ord_rec]

r_rec_sigA = pearson(sat_rec_arr, sigA_arr2)
r_rec_uas  = pearson(sat_rec_arr, uas_arr2)

rng2 = random.Random(SEED + 1)
perm_geq_sigA_rec = 0
perm_geq_uas_rec = 0
for _ in range(N_PERM):
    p1 = sigA_arr2[:]; rng2.shuffle(p1)
    if abs(pearson(sat_rec_arr, p1)) >= abs(r_rec_sigA):
        perm_geq_sigA_rec += 1
    p2 = uas_arr2[:]; rng2.shuffle(p2)
    if pearson(sat_rec_arr, p2) >= r_rec_uas:
        perm_geq_uas_rec += 1
p_rec_sigA = (perm_geq_sigA_rec + 1) / (N_PERM + 1)
p_rec_uas  = (perm_geq_uas_rec  + 1) / (N_PERM + 1)

cluster_in_top10_rec = [s for s in CLUSTER if rank_rec_by_surah[s] <= 10]

# ---- assemble output --------------------------------------------------------
output = {
    "id": "cross-finding-027",
    "title": "iʿjāz al-takrīr (refrain-saturation iʿjāz) — third axis test",
    "prereg_sha": EXPECTED_SHA,
    "seed": SEED,
    "n_permutations": N_PERM,
    "rules_tuple": RULES_TUPLE,
    "alpha_bonferroni_3": ALPHA_BON,
    "verdict": verdict,
    "tests": {
        "H1a_orthogonality_with_sig_A": {
            "pearson_r": r_sat_sigA,
            "perm_p_two_sided": p_sat_sigA,
            "criterion": "|r| < 0.30 AND p > 0.0167",
            "pass": H1a_pass,
        },
        "H1b_positive_correlation_with_UAS": {
            "pearson_r": r_sat_uas,
            "perm_p_one_sided_positive": p_sat_uas,
            "criterion": "0.10 < r < 0.60 AND p < 0.0167",
            "pass": H1b_pass,
        },
        "H1c_cluster_membership_descriptive": {
            "nominated_cluster": CLUSTER,
            "in_top10": cluster_in_top10,
            "count": H1c_count,
            "criterion_descriptive": ">=3 of 5 in top-10",
            "descriptive_pass": H1c_descriptive_pass,
        },
        "H1d_cross_corpus_distinct": {
            "q55_sat": q55_sat,
            "baseline_blocks_total": total_blocks,
            "baseline_blocks_geq_q55": blocks_geq_q55,
            "empirical_p": p_cross_corpus,
            "criterion": "p < 0.0167",
            "pass": H1d_pass,
        },
    },
    "top10_by_saturation": [
        {
            "rank": r["rank"],
            "surah": r["surah"],
            "name": r["name"],
            "sat": r["sat"],
            "best_N": r["best_N"],
            "best_count": r["best_count"],
            "best_ngram": r["best_ngram"],
            "n_words": r["n_words"],
            "sig_A": r["sig_A"],
            "UAS": r["UAS"],
        }
        for r in results_sorted[:10]
    ],
    "bottom10_by_saturation": [
        {
            "rank": r["rank"],
            "surah": r["surah"],
            "name": r["name"],
            "sat": r["sat"],
            "n_words": r["n_words"],
        }
        for r in results_sorted[-10:]
    ],
    "all_per_surah": [
        {
            "surah": r["surah"],
            "rank": r["rank"],
            "sat": r["sat"],
            "best_N": r["best_N"],
            "best_count": r["best_count"],
            "n_words": r["n_words"],
            "sig_A": r["sig_A"],
            "UAS": r["UAS"],
        }
        for r in sorted(results_sorted, key=lambda r: r["surah"])
    ],
    "min_tashkeel_cross_validation": cross_check,
    "baseline_corpora": baseline_block_results,
    "cluster_audit": {
        "nominated": CLUSTER,
        "ranks": {s: rank_by_surah[s] for s in CLUSTER},
        "sats": {s: sat_by_surah[s] for s in CLUSTER},
    },
    "post_hoc_recurrent_count_geq_2": {
        "rationale": ("pre-registered coverage_N is dominated by single-occurrence "
                      "inverse-length artifacts in tiny surahs (N/L). "
                      "Recurrence-restricted version (count>=2) is the intent "
                      "of 'refrain-saturation'. Reported under MW-7 single-test-α=0.05 "
                      "ceiling; cannot upgrade verdict."),
        "top10": [
            {
                "rank": r["rank_recurrent"],
                "surah": r["surah"],
                "name": r["name"],
                "sat_recurrent": r["sat_recurrent"],
                "best_N": r["best_N"],
                "best_count": r["best_count"],
                "best_ngram": r["best_ngram"],
                "n_words": r["n_words"],
                "sig_A": r["sig_A"],
                "UAS": r["UAS"],
            }
            for r in results_recurrent_sorted[:10]
        ],
        "tests_post_hoc": {
            "r_recurrent_sigA": r_rec_sigA,
            "perm_p_two_sided_sigA": p_rec_sigA,
            "r_recurrent_UAS": r_rec_uas,
            "perm_p_one_sided_UAS_positive": p_rec_uas,
        },
        "cluster_in_top10": cluster_in_top10_rec,
        "cluster_count_in_top10": len(cluster_in_top10_rec),
        "cluster_ranks": {s: rank_rec_by_surah[s] for s in CLUSTER},
        "cluster_sats": {s: sat_rec_by_surah[s] for s in CLUSTER},
    },
}

os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(output, f, ensure_ascii=False, indent=2)

# ---- console summary --------------------------------------------------------
print("\n" + "="*78)
print("CROSS-FINDING-027 — iʿjāz al-takrīr (refrain-saturation iʿjāz)")
print("="*78)
print(f"\nVerdict: {verdict}")
print(f"\nTop-10 by refrain-saturation:")
for r in results_sorted[:10]:
    print(f"  rank {r['rank']:3d}  Q{r['surah']:3d} ({r['name']})"
          f"  sat={r['sat']:.4f}  N={r['best_N']}  count={r['best_count']}"
          f"  words={r['n_words']}  sig_A={r['sig_A']:+.3f}  UAS={r['UAS']:+.3f}")

print(f"\nH1a orthogonality with sig_A: r={r_sat_sigA:+.4f}, p={p_sat_sigA:.4f}  [{'PASS' if H1a_pass else 'FAIL'}]")
print(f"H1b positive correlation with UAS: r={r_sat_uas:+.4f}, p={p_sat_uas:.4f}  [{'PASS' if H1b_pass else 'FAIL'}]")
print(f"H1c cluster {CLUSTER}: {H1c_count}/5 in top-10  ({cluster_in_top10})  [descriptive {'PASS' if H1c_descriptive_pass else 'FAIL'}]")
print(f"H1d cross-corpus distinct: Q55_sat={q55_sat:.4f}, baseline blocks total={total_blocks}, geq_Q55={blocks_geq_q55}, p={p_cross_corpus:.4f}  [{'PASS' if H1d_pass else 'FAIL'}]")

print("\n" + "-"*78)
print("POST-HOC (MW-7 capped, single-test-α): recurrence-restricted (count>=2)")
print("-"*78)
print("\nTop-10 by RECURRENT refrain-saturation:")
for r in results_recurrent_sorted[:10]:
    print(f"  rank {r['rank_recurrent']:3d}  Q{r['surah']:3d} ({r['name']})"
          f"  sat={r['sat_recurrent']:.4f}  N={r['best_N']}  count={r['best_count']}"
          f"  words={r['n_words']}  sig_A={r['sig_A']:+.3f}  UAS={r['UAS']:+.3f}")
print(f"\n[post-hoc] r(sat_recurrent, sig_A) = {r_rec_sigA:+.4f}, p={p_rec_sigA:.4f}")
print(f"[post-hoc] r(sat_recurrent, UAS)   = {r_rec_uas:+.4f}, p={p_rec_uas:.4f}")
print(f"[post-hoc] cluster in top-10: {cluster_in_top10_rec}")

print(f"\nOutput JSON: {OUT_JSON}")
