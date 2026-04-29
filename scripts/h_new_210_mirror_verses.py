#!/usr/bin/env python3
"""
H-NEW-210 — Levenshtein mirror-verses (optimized).

Strategy:
1. Load verses, filter min_len>=10.
2. Build character-3gram sets. Inverted index: 3gram -> list of verse_idx.
3. For each verse i, aggregate candidate verses j>i that share >=K 3grams
   AND whose length ratio is close enough.
4. Only run Levenshtein on candidates.
5. Keep cross-surah pairs with ratio < 0.30, rank top-50.
6. Permutation null (length-stratified surah shuffle, 1000 iters).

Seed: 20260419. Bonferroni k=1.
"""

import json
import csv
import random
import sys
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path("/Users/grey/Downloads/quran")
CORPUS = ROOT / "quran-text" / "quran-no-tashkeel.json"
OUT_CSV = ROOT / "findings" / "phase-b-hypotheses" / "h-new-210-top50.csv"
SEED = 20260419
THRESH = 0.30
MIN_LEN = 10
TOP_K = 50
PERMS = 1000


def levenshtein(a: str, b: str, max_d: int = None) -> int:
    """Levenshtein with optional early termination when min row > max_d."""
    if len(a) < len(b):
        a, b = b, a
    la, lb = len(a), len(b)
    if lb == 0:
        return la
    if max_d is not None and la - lb > max_d:
        return max_d + 1
    prev = list(range(lb + 1))
    for i in range(1, la + 1):
        curr = [i] + [0] * lb
        ca = a[i - 1]
        row_min = curr[0]
        for j in range(1, lb + 1):
            cb = b[j - 1]
            c = min(curr[j - 1] + 1,
                    prev[j] + 1,
                    prev[j - 1] + (0 if ca == cb else 1))
            curr[j] = c
            if c < row_min:
                row_min = c
        if max_d is not None and row_min > max_d:
            return max_d + 1
        prev = curr
    return prev[-1]


def ngrams(s: str, n: int = 3):
    s = "".join(s.split())  # strip whitespace for ngram shingles
    if len(s) < n:
        return [s]
    return [s[i:i + n] for i in range(len(s) - n + 1)]


def load_verses():
    data = json.loads(CORPUS.read_text(encoding="utf-8"))
    out = []
    for surah in data:
        s = surah["id"]
        for v in surah["verses"]:
            out.append((s, v["id"], v["text"].strip()))
    return out


def find_candidate_pairs(verses, min_shared_ngrams=3, jaccard_min=0.40):
    """Return list of (i, j) candidate pairs with i<j to run Levenshtein on."""
    shingles = [set(ngrams(t)) for (s, v, t) in verses]
    # Inverted index
    inv = defaultdict(list)
    for i, sh in enumerate(shingles):
        for g in sh:
            inv[g].append(i)

    # For each verse, sum co-occurrences via inverted index
    cand = set()
    n = len(verses)
    for i in range(n):
        sh_i = shingles[i]
        counts = Counter()
        for g in sh_i:
            for j in inv[g]:
                if j > i:
                    counts[j] += 1
        for j, c in counts.items():
            if c < min_shared_ngrams:
                continue
            union = len(sh_i | shingles[j])
            if union == 0:
                continue
            jac = c / union
            if jac >= jaccard_min:
                cand.add((i, j))
        if i % 1000 == 0:
            print(f"  ngram-scan i={i}/{n} cand={len(cand)}", file=sys.stderr)
    return cand


def main():
    random.seed(SEED)
    verses = load_verses()
    print(f"Loaded {len(verses)} verses", file=sys.stderr)
    verses = [(s, v, t) for (s, v, t) in verses if len(t) >= MIN_LEN]
    print(f"Post-filter: {len(verses)} verses >= {MIN_LEN} chars", file=sys.stderr)

    cand_pairs = find_candidate_pairs(verses, min_shared_ngrams=3, jaccard_min=0.40)
    print(f"Candidate pairs after ngram prefilter: {len(cand_pairs)}", file=sys.stderr)

    results = []
    for k, (i, j) in enumerate(cand_pairs):
        s1, v1, t1 = verses[i]
        s2, v2, t2 = verses[j]
        l1, l2 = len(t1), len(t2)
        mean_len = (l1 + l2) / 2.0
        # length-based lower bound on Levenshtein
        if abs(l1 - l2) >= THRESH * mean_len:
            continue
        max_d = int(THRESH * mean_len)
        d = levenshtein(t1, t2, max_d=max_d)
        if d > max_d:
            continue
        ratio = d / mean_len
        if ratio < THRESH:
            results.append((ratio, d, i, j, s1, v1, s2, v2, t1, t2, mean_len))
        if k % 20000 == 0:
            print(f"  lev-scan k={k}/{len(cand_pairs)} kept={len(results)}", file=sys.stderr)

    results.sort(key=lambda r: (r[0], -r[10]))
    print(f"Total pairs ratio<{THRESH}: {len(results)}", file=sys.stderr)

    # Cross-surah subset
    cross = [r for r in results if r[4] != r[6]]
    print(f"Cross-surah pairs: {len(cross)}", file=sys.stderr)

    top50 = cross[:TOP_K]

    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["rank", "s1", "v1", "s2", "v2", "lev_distance", "ratio",
                    "mean_len", "len1", "len2", "text1", "text2"])
        for k, (ratio, d, i, j, s1, v1, s2, v2, t1, t2, ml) in enumerate(top50, 1):
            w.writerow([k, s1, v1, s2, v2, d, f"{ratio:.4f}",
                        f"{ml:.1f}", len(t1), len(t2), t1, t2])
    print(f"Wrote {OUT_CSV}", file=sys.stderr)

    # Hotspot labeling (pre-registered)
    hits = {"prophet": [], "ablution": [], "rahman": [], "other_known": []}
    extra = [
        (6, 151, 17, 31), (6, 151, 17, 33),
        (2, 58, 7, 161),
        (2, 47, 2, 122),
    ]
    for k, (ratio, d, i, j, s1, v1, s2, v2, t1, t2, ml) in enumerate(top50, 1):
        if ((s1 == 2 and abs(v1 - 136) <= 2 and s2 == 3 and abs(v2 - 84) <= 2) or
            (s2 == 2 and abs(v2 - 136) <= 2 and s1 == 3 and abs(v1 - 84) <= 2)):
            hits["prophet"].append(k)
        if ((s1 == 4 and abs(v1 - 43) <= 2 and s2 == 5 and abs(v2 - 6) <= 2) or
            (s2 == 4 and abs(v2 - 43) <= 2 and s1 == 5 and abs(v1 - 6) <= 2)):
            hits["ablution"].append(k)
        if s1 == 55 or s2 == 55:
            hits["rahman"].append(k)
        for (es1, ev1, es2, ev2) in extra:
            if ((s1 == es1 and abs(v1 - ev1) <= 2 and s2 == es2 and abs(v2 - ev2) <= 2) or
                (s2 == es1 and abs(v2 - ev1) <= 2 and s1 == es2 and abs(v1 - ev2) <= 2)):
                hits["other_known"].append(k)

    surah_counter = Counter()
    for (ratio, d, i, j, s1, v1, s2, v2, t1, t2, ml) in top50:
        surah_counter[s1] += 1
        surah_counter[s2] += 1

    # Permutation: length-stratified surah shuffle. We reuse `results` (all ratio<threshold
    # pairs, both intra and cross). For each permutation, relabel surahs within 10-char length bins,
    # re-filter cross-surah, take top-50, count hotspot hits.
    observed_hotspot = len(set(hits["prophet"] + hits["ablution"] + hits["rahman"]))

    bins = {}
    for idx, (s, v, t) in enumerate(verses):
        b = len(t) // 10
        bins.setdefault(b, []).append(idx)

    # all_pairs (ratio<thresh) indexed by (i, j) with ratio and ml precomputed for re-ranking
    all_pairs = sorted(
        [(r[0], r[10], r[2], r[3]) for r in results],
        key=lambda x: (x[0], -x[1])
    )
    orig_surah = [s for (s, v, t) in verses]
    orig_verse = [v for (s, v, t) in verses]

    null_counts = []
    print(f"Running {PERMS} permutations...", file=sys.stderr)
    for perm in range(PERMS):
        new_s = list(orig_surah)
        new_v = list(orig_verse)
        for b, idxs in bins.items():
            shuffled = idxs[:]
            random.shuffle(shuffled)
            src_s = [orig_surah[x] for x in shuffled]
            src_v = [orig_verse[x] for x in shuffled]
            for k2, tgt in enumerate(idxs):
                new_s[tgt] = src_s[k2]
                new_v[tgt] = src_v[k2]
        top = []
        for (ratio, ml, i, j) in all_pairs:
            if new_s[i] == new_s[j]:
                continue
            top.append((i, j))
            if len(top) == TOP_K:
                break
        c = 0
        for (i, j) in top:
            s1, s2 = new_s[i], new_s[j]
            v1, v2 = new_v[i], new_v[j]
            ok = False
            if ((s1 == 2 and abs(v1 - 136) <= 2 and s2 == 3 and abs(v2 - 84) <= 2) or
                (s2 == 2 and abs(v2 - 136) <= 2 and s1 == 3 and abs(v1 - 84) <= 2)):
                ok = True
            if ((s1 == 4 and abs(v1 - 43) <= 2 and s2 == 5 and abs(v2 - 6) <= 2) or
                (s2 == 4 and abs(v2 - 43) <= 2 and s1 == 5 and abs(v1 - 6) <= 2)):
                ok = True
            if s1 == 55 or s2 == 55:
                ok = True
            if ok:
                c += 1
        null_counts.append(c)
        if perm % 100 == 0:
            print(f"  perm {perm}/{PERMS}", file=sys.stderr)

    null_counts.sort()
    mean_null = sum(null_counts) / len(null_counts)
    ge = sum(1 for x in null_counts if x >= observed_hotspot)
    p = (ge + 1) / (PERMS + 1)

    # Top distinct surahs involved
    report = {
        "total_candidate_pairs_ngram": len(cand_pairs),
        "total_ratio_lt_0.30_pairs": len(results),
        "total_cross_surah_pairs": len(cross),
        "top50_surah_frequency": surah_counter.most_common(15),
        "hits": {k: sorted(set(v)) for k, v in hits.items()},
        "observed_hotspot_count_top50": observed_hotspot,
        "null_mean": mean_null,
        "null_max": max(null_counts),
        "null_q95": null_counts[int(0.95 * PERMS)],
        "p_value": p,
        "perms": PERMS,
        "seed": SEED,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
