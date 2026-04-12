"""Phase B: Information-theoretic profile of the Quran.

Pure stdlib (math, json, gzip, zlib, random, csv, collections, statistics).
Run from project root or with absolute paths.
"""

from __future__ import annotations

import csv
import gzip
import json
import math
import os
import random
import sys
import zlib
from collections import Counter, defaultdict
from statistics import mean, pstdev

# Add tools to path
sys.path.insert(0, "/Users/grey/Downloads/quran/analysis")

from tools.loader import load_quran  # noqa: E402
from tools.tokenize import (  # noqa: E402
    is_letter,
    graphemes,
    real_words,
)

OUT_CSV = "/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv"
os.makedirs(OUT_CSV, exist_ok=True)

MORPH_PATH = "/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt"


# ----------------------------------------------------------------------
# Helpers
# ----------------------------------------------------------------------

def shannon_entropy(counter: Counter) -> float:
    """Shannon entropy in bits from a Counter."""
    total = sum(counter.values())
    if total == 0:
        return 0.0
    H = 0.0
    for c in counter.values():
        if c == 0:
            continue
        p = c / total
        H -= p * math.log2(p)
    return H


def letters_only(text: str) -> str:
    return "".join(ch for ch in text if is_letter(ch))


def all_letter_string(quran) -> str:
    parts = []
    for s in quran:
        for v in s.verses:
            parts.append(letters_only(v.text))
    return " ".join(parts)  # spaces between verses (won't be counted as letters)


def all_letter_concat_no_spaces(quran) -> str:
    return "".join(letters_only(v.text) for s in quran for v in s.verses)


# ----------------------------------------------------------------------
# Task 1: Letter frequency entropy
# ----------------------------------------------------------------------

def task1_letter_entropy(quran):
    text = all_letter_concat_no_spaces(quran)
    counter = Counter(text)
    H = shannon_entropy(counter)
    n_distinct = len(counter)
    H_max_28 = math.log2(28)
    H_max_actual = math.log2(n_distinct)
    redundancy_28 = 1 - H / H_max_28
    redundancy_actual = 1 - H / H_max_actual
    return {
        "total_letters": len(text),
        "distinct_letters": n_distinct,
        "H": H,
        "H_max_28": H_max_28,
        "H_max_actual": H_max_actual,
        "redundancy_vs_28": redundancy_28,
        "redundancy_vs_actual": redundancy_actual,
        "letter_counts": counter,
    }


# ----------------------------------------------------------------------
# Task 2: Conditional entropy / block entropy
# ----------------------------------------------------------------------

def block_entropy(text: str, n: int) -> float:
    """H of n-grams (joint entropy)."""
    if len(text) < n:
        return 0.0
    counter = Counter(text[i : i + n] for i in range(len(text) - n + 1))
    return shannon_entropy(counter)


def conditional_letter_entropy(text: str, order: int) -> float:
    """H(L_{n+1} | L_1...L_n) computed from block-entropy difference.

    H(X_{n+1}|X_1..X_n) = H(X_1..X_{n+1}) - H(X_1..X_n)
    """
    if order == 0:
        return block_entropy(text, 1)
    Hn = block_entropy(text, order)
    Hn1 = block_entropy(text, order + 1)
    return Hn1 - Hn


def task2_conditional(quran):
    text = all_letter_concat_no_spaces(quran)
    H1 = block_entropy(text, 1)
    H2 = block_entropy(text, 2)
    H3 = block_entropy(text, 3)
    H4 = block_entropy(text, 4)
    H5 = block_entropy(text, 5)
    H_cond_2 = H2 - H1  # H(L2|L1)
    H_cond_3 = H3 - H2  # H(L3|L1,L2)
    H_cond_4 = H4 - H3
    H_cond_5 = H5 - H4
    return {
        "H1": H1,
        "H2": H2,
        "H3": H3,
        "H4": H4,
        "H5": H5,
        "H(L2|L1)": H_cond_2,
        "H(L3|L1,L2)": H_cond_3,
        "H(L4|L1..L3)": H_cond_4,
        "H(L5|L1..L4)": H_cond_5,
    }


# ----------------------------------------------------------------------
# Task 3: Per-surah entropy
# ----------------------------------------------------------------------

def task3_per_surah_entropy(quran):
    rows = []
    for s in quran:
        text = "".join(letters_only(v.text) for v in s.verses)
        counter = Counter(text)
        H = shannon_entropy(counter)
        n_distinct = len(counter)
        rows.append({
            "id": s.id,
            "name": s.transliteration,
            "type": s.type,
            "n_letters": len(text),
            "n_verses": len(s.verses),
            "n_distinct_letters": n_distinct,
            "H": H,
        })
    return rows


# ----------------------------------------------------------------------
# Task 4: Zipf law on lemmas
# ----------------------------------------------------------------------

def parse_morphology(path: str):
    """Yield (location_tuple, form, tag, features) for each STEM line."""
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if not line.strip() or line.startswith("#"):
                continue
            if line.startswith("LOCATION"):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            loc = parts[0].strip("()").split(":")
            try:
                loc_t = tuple(int(x) for x in loc)
            except ValueError:
                continue
            yield loc_t, parts[1], parts[2], parts[3]


def extract_lemma(features: str) -> str | None:
    if "LEM:" not in features:
        return None
    for f in features.split("|"):
        if f.startswith("LEM:"):
            return f[4:]
    return None


def extract_root(features: str) -> str | None:
    if "ROOT:" not in features:
        return None
    for f in features.split("|"):
        if f.startswith("ROOT:"):
            return f[5:]
    return None


def collect_lemmas():
    """Returns list of (loc, surah, verse, lemma, root) for each lemma-bearing morpheme."""
    out = []
    for loc, form, tag, feats in parse_morphology(MORPH_PATH):
        if "STEM" not in feats:
            continue
        lem = extract_lemma(feats)
        if lem is None:
            continue
        root = extract_root(feats)
        out.append((loc, loc[0], loc[1], lem, root))
    return out


def task4_zipf(lemma_list):
    counter = Counter(lem for (_loc, _s, _v, lem, _r) in lemma_list)
    sorted_freqs = sorted(counter.values(), reverse=True)
    # Fit log(rank) vs log(freq), with rank starting at 1.
    # Truncate to first N=top, but use all distinct lemmas.
    xs = [math.log(r + 1) for r in range(len(sorted_freqs))]  # log(rank)
    ys = [math.log(f) for f in sorted_freqs]
    # OLS slope and intercept (and R^2)
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxy = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    sxx = sum((xs[i] - mx) ** 2 for i in range(n))
    syy = sum((ys[i] - my) ** 2 for i in range(n))
    slope = sxy / sxx
    intercept = my - slope * mx
    r2 = (sxy ** 2) / (sxx * syy)
    alpha = -slope  # Zipf exponent
    return {
        "n_distinct_lemmas": len(counter),
        "n_total_lemma_tokens": sum(sorted_freqs),
        "alpha": alpha,
        "intercept": intercept,
        "R2": r2,
        "top10": counter.most_common(10),
    }


# ----------------------------------------------------------------------
# Task 5: Heaps' law
# ----------------------------------------------------------------------

def task5_heaps(lemma_list, seed=42):
    """Sample contiguous prefix and random subsets of lemmas."""
    lemmas = [lem for (_loc, _s, _v, lem, _r) in lemma_list]
    N = len(lemmas)
    rng = random.Random(seed)
    sizes = [100, 500, 1000, 2000, 5000, 10000, 20000, 30000, 50000, N]
    sizes = [s for s in sizes if s <= N]

    # Use random sampling without replacement
    points = []
    for sz in sizes:
        sample = rng.sample(lemmas, sz)
        v = len(set(sample))
        points.append((sz, v))
    # Fit log V = log K + beta * log N
    xs = [math.log(n) for (n, _) in points]
    ys = [math.log(v) for (_, v) in points]
    n = len(xs)
    mx = sum(xs) / n
    my = sum(ys) / n
    sxy = sum((xs[i] - mx) * (ys[i] - my) for i in range(n))
    sxx = sum((xs[i] - mx) ** 2 for i in range(n))
    syy = sum((ys[i] - my) ** 2 for i in range(n))
    beta = sxy / sxx
    intercept = my - beta * mx
    K = math.exp(intercept)
    r2 = (sxy ** 2) / (sxx * syy)
    return {
        "points": points,
        "beta": beta,
        "K": K,
        "R2": r2,
    }


# ----------------------------------------------------------------------
# Task 6: KL divergence matrix between surahs (lemma distributions)
# ----------------------------------------------------------------------

def kl_divergence(p: dict, q: dict, vocab: list, alpha: float = 0.5) -> float:
    """Smoothed KL(p || q) over a fixed vocabulary, additive (Laplace) smoothing."""
    V = len(vocab)
    sum_p = sum(p.values()) + alpha * V
    sum_q = sum(q.values()) + alpha * V
    kl = 0.0
    for w in vocab:
        pi = (p.get(w, 0) + alpha) / sum_p
        qi = (q.get(w, 0) + alpha) / sum_q
        kl += pi * math.log2(pi / qi)
    return kl


def task6_kl(lemma_list, quran):
    # Per-surah lemma counters
    surah_counters = defaultdict(Counter)
    for (_loc, surah, verse, lem, _r) in lemma_list:
        surah_counters[surah][lem] += 1
    # Vocabulary = all distinct lemmas
    vocab = sorted({lem for (_loc, _s, _v, lem, _r) in lemma_list})
    print(f"  KL: {len(vocab)} distinct lemmas, {len(surah_counters)} surahs", flush=True)
    # Compute KL[i][j] = KL(P_i || P_j)
    matrix = [[0.0] * 114 for _ in range(114)]
    keys = sorted(surah_counters.keys())
    # Precompute smoothed probability vectors for speed
    alpha = 0.5
    V = len(vocab)
    vec_index = {w: i for i, w in enumerate(vocab)}
    probs = {}  # surah -> list of probabilities
    for sid, c in surah_counters.items():
        s_total = sum(c.values()) + alpha * V
        arr = [alpha / s_total] * V
        for w, n in c.items():
            arr[vec_index[w]] = (n + alpha) / s_total
        probs[sid] = arr
    # KL(p||q) = sum p * log2(p/q) = sum p*log2 p - sum p*log2 q
    # Precompute sum p*log2 p
    self_term = {}
    for sid, p in probs.items():
        self_term[sid] = sum(pi * math.log2(pi) for pi in p)
    for i, si in enumerate(keys):
        pi_arr = probs[si]
        for j, sj in enumerate(keys):
            if i == j:
                continue
            qj = probs[sj]
            cross = sum(pi_arr[k] * math.log2(qj[k]) for k in range(V))
            kl = self_term[si] - cross
            matrix[si - 1][sj - 1] = kl
    return matrix, keys


def task6_summary(matrix):
    # Symmetric matrix is the not the case; KL is asymmetric. Use Jensen-Shannon-like?
    # Just report: most-similar pair (min KL), most-dissimilar pair (max KL).
    n = len(matrix)
    min_val = float("inf")
    max_val = -float("inf")
    min_pair = None
    max_pair = None
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            v = matrix[i][j]
            if v < min_val:
                min_val = v
                min_pair = (i + 1, j + 1)
            if v > max_val:
                max_val = v
                max_pair = (i + 1, j + 1)
    return {"min_kl": min_val, "min_pair": min_pair,
            "max_kl": max_val, "max_pair": max_pair}


# ----------------------------------------------------------------------
# Task 7: Compression complexity
# ----------------------------------------------------------------------

def task7_compression(quran):
    rows = []
    for s in quran:
        text = " ".join(v.text for v in s.verses)
        b = text.encode("utf-8")
        gz = gzip.compress(b, compresslevel=9)
        zl = zlib.compress(b, level=9)
        rows.append({
            "id": s.id,
            "name": s.transliteration,
            "type": s.type,
            "raw_bytes": len(b),
            "gzip_bytes": len(gz),
            "zlib_bytes": len(zl),
            "gzip_ratio": len(gz) / len(b),
            "zlib_ratio": len(zl) / len(b),
        })
    return rows


# ----------------------------------------------------------------------
# Task 8: Mutual information between position-in-verse and letter
# ----------------------------------------------------------------------

def task8_position_mi(quran, max_pos: int = 30):
    """For each position p in [0, max_pos), tally letter distribution.

    Then compute MI(position; letter) using only positions 0..max_pos-1
    of each verse (truncate longer verses, exclude shorter).
    """
    pos_counters = [Counter() for _ in range(max_pos)]
    for s in quran:
        for v in s.verses:
            letters = letters_only(v.text)
            for i, ch in enumerate(letters[:max_pos]):
                pos_counters[i][ch] += 1
    # Joint distribution P(p, l)
    total = sum(sum(c.values()) for c in pos_counters)
    if total == 0:
        return None
    H_letter = Counter()
    for c in pos_counters:
        H_letter.update(c)
    H_L = shannon_entropy(H_letter)
    # H(P) - uniform over positions weighted by available data
    H_P = 0.0
    pos_total = [sum(c.values()) for c in pos_counters]
    for n in pos_total:
        if n == 0:
            continue
        p = n / total
        H_P -= p * math.log2(p)
    # H(P, L)
    joint = Counter()
    for i, c in enumerate(pos_counters):
        for ch, n in c.items():
            joint[(i, ch)] = n
    H_PL = shannon_entropy(joint)
    MI = H_P + H_L - H_PL
    return {
        "H_position": H_P,
        "H_letter": H_L,
        "H_joint": H_PL,
        "MI": MI,
        "MI_normalized": MI / min(H_P, H_L) if min(H_P, H_L) > 0 else 0.0,
        "max_pos": max_pos,
    }


# ----------------------------------------------------------------------
# Task 9 & 10: Verse-index entropy patterns within surahs
# ----------------------------------------------------------------------

def task10_verse_index_entropy(quran):
    """For each surah, compute per-verse letter entropy and then within-surah trend."""
    rows = []
    for s in quran:
        verses_data = []
        for v in s.verses:
            text = letters_only(v.text)
            counter = Counter(text)
            H = shannon_entropy(counter)
            verses_data.append((v.id, len(text), H))
        rows.append({
            "id": s.id,
            "name": s.transliteration,
            "type": s.type,
            "verses": verses_data,
        })
    return rows


def task9_outliers(quran, per_verse):
    """Find verses with extreme entropy (top/bottom 10) globally."""
    all_verses = []
    for surah in per_verse:
        for vid, n, H in surah["verses"]:
            if n >= 10:  # avoid trivially short verses
                all_verses.append((surah["id"], vid, n, H))
    by_H = sorted(all_verses, key=lambda x: x[3])
    return {
        "lowest_H": by_H[:15],
        "highest_H": by_H[-15:],
        "n_total": len(all_verses),
    }


# ----------------------------------------------------------------------
# Run everything
# ----------------------------------------------------------------------

def main():
    print("Loading Quran (no-tashkeel)...", flush=True)
    quran = load_quran("no-tashkeel")
    print(f"  {len(quran)} surahs, {sum(len(s.verses) for s in quran)} verses", flush=True)

    # Task 1
    print("Task 1: letter entropy", flush=True)
    t1 = task1_letter_entropy(quran)
    print(f"  total letters: {t1['total_letters']}, distinct: {t1['distinct_letters']}", flush=True)
    print(f"  H = {t1['H']:.4f} bits, H_max(28) = {t1['H_max_28']:.4f}", flush=True)
    print(f"  redundancy vs 28: {t1['redundancy_vs_28']:.4f}", flush=True)

    # Task 2
    print("Task 2: block / conditional entropies", flush=True)
    t2 = task2_conditional(quran)
    for k, v in t2.items():
        print(f"  {k} = {v:.4f}", flush=True)

    # Task 3
    print("Task 3: per-surah entropy", flush=True)
    t3 = task3_per_surah_entropy(quran)
    with open(os.path.join(OUT_CSV, "per-surah-entropy.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["id", "name", "type", "n_verses", "n_letters", "n_distinct_letters", "H"])
        w.writeheader()
        for r in t3:
            w.writerow(r)
    sorted_t3 = sorted(t3, key=lambda r: r["H"])
    print(f"  bottom 5: {[(r['id'], r['name'], round(r['H'],3)) for r in sorted_t3[:5]]}", flush=True)
    print(f"  top 5: {[(r['id'], r['name'], round(r['H'],3)) for r in sorted_t3[-5:]]}", flush=True)

    # Task 4 - need lemmas
    print("Loading morphology / lemmas...", flush=True)
    lemma_list = collect_lemmas()
    print(f"  {len(lemma_list)} lemma-bearing morphemes", flush=True)

    print("Task 4: Zipf fit", flush=True)
    t4 = task4_zipf(lemma_list)
    print(f"  alpha = {t4['alpha']:.4f}, R^2 = {t4['R2']:.4f}", flush=True)
    print(f"  distinct lemmas = {t4['n_distinct_lemmas']}, tokens = {t4['n_total_lemma_tokens']}", flush=True)

    # Task 5
    print("Task 5: Heaps' law", flush=True)
    t5 = task5_heaps(lemma_list)
    print(f"  beta = {t5['beta']:.4f}, K = {t5['K']:.4f}, R^2 = {t5['R2']:.4f}", flush=True)
    print(f"  points = {t5['points']}", flush=True)

    # Task 6 - KL matrix (this is the slow one)
    print("Task 6: KL matrix between surahs (this takes a while)", flush=True)
    matrix, keys = task6_kl(lemma_list, quran)
    # Save matrix
    with open(os.path.join(OUT_CSV, "kl-matrix.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["from\\to"] + [str(i) for i in range(1, 115)])
        for i, row in enumerate(matrix):
            w.writerow([i + 1] + [f"{x:.4f}" for x in row])
    t6summary = task6_summary(matrix)
    print(f"  min KL: {t6summary['min_kl']:.4f} between surahs {t6summary['min_pair']}", flush=True)
    print(f"  max KL: {t6summary['max_kl']:.4f} between surahs {t6summary['max_pair']}", flush=True)

    # Hierarchical clustering by symmetric KL (mean of KL i->j and j->i)
    sym = [[0.0] * 114 for _ in range(114)]
    for i in range(114):
        for j in range(114):
            sym[i][j] = 0.5 * (matrix[i][j] + matrix[j][i])

    # Naive single-linkage hierarchical clustering
    cluster_meccan = simple_2cluster(sym, quran)
    print(f"  2-cluster Meccan/Medinan match: {cluster_meccan}", flush=True)

    # Task 7
    print("Task 7: compression complexity", flush=True)
    t7 = task7_compression(quran)
    with open(os.path.join(OUT_CSV, "compression.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["id", "name", "type", "raw_bytes", "gzip_bytes", "zlib_bytes", "gzip_ratio", "zlib_ratio"])
        w.writeheader()
        for r in t7:
            w.writerow(r)
    sorted_t7 = sorted(t7, key=lambda r: r["gzip_ratio"])
    print(f"  most compressible (low gzip ratio): {[(r['id'], r['name'], round(r['gzip_ratio'],3)) for r in sorted_t7[:5]]}", flush=True)
    print(f"  least compressible: {[(r['id'], r['name'], round(r['gzip_ratio'],3)) for r in sorted_t7[-5:]]}", flush=True)

    # Correlation: gzip_ratio vs entropy vs length
    H_by_id = {r["id"]: r["H"] for r in t3}
    L_by_id = {r["id"]: r["n_letters"] for r in t3}
    pairs_he = [(t["gzip_ratio"], H_by_id[t["id"]]) for t in t7]
    pairs_hl = [(t["gzip_ratio"], L_by_id[t["id"]]) for t in t7]
    r_he = pearson(pairs_he)
    r_hl = pearson(pairs_hl)
    print(f"  Pearson(gzip_ratio, H_letter) = {r_he:.4f}", flush=True)
    print(f"  Pearson(gzip_ratio, length)   = {r_hl:.4f}", flush=True)

    # Task 8
    print("Task 8: position-letter MI", flush=True)
    t8 = task8_position_mi(quran, max_pos=30)
    print(f"  H(L) = {t8['H_letter']:.4f}, H(P) = {t8['H_position']:.4f}, MI = {t8['MI']:.4f}", flush=True)

    # Task 9 & 10
    print("Task 10: per-verse-index entropy patterns", flush=True)
    per_verse = task10_verse_index_entropy(quran)
    t9 = task9_outliers(quran, per_verse)
    print(f"  lowest H verses: {t9['lowest_H'][:5]}", flush=True)
    print(f"  highest H verses: {t9['highest_H'][-5:]}", flush=True)

    # Within-surah trend: correlation between verse index and entropy per surah
    trends = []
    for surah in per_verse:
        vs = surah["verses"]
        if len(vs) < 5:
            continue
        # Use only verses with >=10 letters
        filt = [(vid, n, H) for (vid, n, H) in vs if n >= 10]
        if len(filt) < 5:
            continue
        xs = list(range(len(filt)))
        ys = [H for (_, _, H) in filt]
        r = pearson_xy(xs, ys)
        trends.append((surah["id"], surah["name"], surah["type"], len(filt), r))
    # Mean r
    mean_r = sum(t[4] for t in trends) / len(trends)
    pos_trends = sum(1 for t in trends if t[4] > 0)
    print(f"  surahs analyzed: {len(trends)}, mean Pearson(verse_idx, H) = {mean_r:.4f}", flush=True)
    print(f"  surahs with positive trend: {pos_trends}/{len(trends)}", flush=True)

    # Save trend file
    with open(os.path.join(OUT_CSV, "verse-index-trend.csv"), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["surah_id", "name", "type", "n_verses_used", "pearson_r"])
        for row in trends:
            w.writerow(row)

    # Bundle output for the markdown step
    return {
        "t1": t1, "t2": t2, "t3": t3, "t4": t4, "t5": t5,
        "t6summary": t6summary, "t7": t7, "t8": t8,
        "t9": t9, "trends": trends, "mean_r": mean_r, "pos_trends": pos_trends,
        "per_verse": per_verse, "matrix": matrix,
        "r_he": r_he, "r_hl": r_hl,
        "cluster_meccan_match": cluster_meccan,
    }


# Pearson helpers
def pearson(pairs):
    n = len(pairs)
    mx = sum(p[0] for p in pairs) / n
    my = sum(p[1] for p in pairs) / n
    sxy = sum((p[0] - mx) * (p[1] - my) for p in pairs)
    sxx = sum((p[0] - mx) ** 2 for p in pairs)
    syy = sum((p[1] - my) ** 2 for p in pairs)
    if sxx == 0 or syy == 0:
        return 0.0
    return sxy / math.sqrt(sxx * syy)


def pearson_xy(xs, ys):
    return pearson(list(zip(xs, ys)))


def simple_2cluster(sym, quran):
    """K-means-ish split into 2 clusters based on first principal axis of distance matrix.

    Crude alternative: just sort surahs by mean distance to surah 1 (a Meccan)
    and split at the median. This is a smoke test for whether KL between
    surahs roughly tracks Meccan/Medinan classification.
    """
    n = 114
    # Distance to surah 1 vs distance to surah 2 (Al-Baqara, Medinan)
    d1 = [sym[i][0] for i in range(n)]
    d2 = [sym[i][1] for i in range(n)]
    # Cluster: closer to surah 1 (Fatiha, Meccan) vs closer to surah 2 (Baqara, Medinan)
    pred = ["meccan" if d1[i] < d2[i] else "medinan" for i in range(n)]
    actual = [quran[i].type for i in range(n)]
    correct = sum(1 for i in range(n) if pred[i] == actual[i])
    return correct / n


if __name__ == "__main__":
    results = main()
    # Save key results as a JSON sidecar so the report writer can read them
    with open(os.path.join(OUT_CSV, "info-theory-results.json"), "w", encoding="utf-8") as fh:
        # strip non-serializable bits
        slim = {
            "t1": {k: v for k, v in results["t1"].items() if k != "letter_counts"},
            "t1_letter_counts": dict(results["t1"]["letter_counts"]),
            "t2": results["t2"],
            "t3": results["t3"],
            "t4": {k: v for k, v in results["t4"].items() if k != "top10"},
            "t4_top10": [(w, c) for (w, c) in results["t4"]["top10"]],
            "t5": results["t5"],
            "t6summary": results["t6summary"],
            "t7": results["t7"],
            "t8": results["t8"],
            "t9": {k: v for k, v in results["t9"].items()},
            "trends_summary": {"mean_r": results["mean_r"], "pos_trends": results["pos_trends"], "n": len(results["trends"])},
            "trends": results["trends"],
            "r_he": results["r_he"],
            "r_hl": results["r_hl"],
            "cluster_meccan_match": results["cluster_meccan_match"],
        }
        json.dump(slim, fh, ensure_ascii=False, indent=2)
    print("Done. Results JSON saved.", flush=True)
