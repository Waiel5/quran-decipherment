"""H-NEW-44 — observed-only properties (null deferred).

Computes the 6 combinatorial properties of the observed 14-muqaṭṭaʿāt family
AND the letter-frequency secondary. Skips the 10K null (bottlenecked by
exact boolean_rank; queued for numpy-vectorized rewrite as H-NEW-44.1).
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from collections import Counter
from itertools import combinations
from typing import List

REPO = "/Users/grey/Downloads/quran"
sys.path.insert(0, os.path.join(REPO, "analysis"))
from tools.loader import load_quran  # noqa: E402

UNIVERSE = list("احرسصطعقكلمنهي")
LETTER_BIT = {c: 1 << i for i, c in enumerate(UNIVERSE)}


def bits(s: str) -> int:
    return sum(LETTER_BIT[c] for c in s)


MUQ = [bits("ص"), bits("ق"), bits("ن"),
       bits("طه"), bits("يس"), bits("طس"), bits("حم"),
       bits("الم"), bits("الر"), bits("طسم"),
       bits("المص"), bits("المر"),
       bits("كهيعص"), bits("حمعسق")]


def is_antichain(f):
    for i in range(len(f)):
        for j in range(i + 1, len(f)):
            a, b = f[i], f[j]
            if a == b:
                continue
            if (a & b) == a or (a & b) == b:
                return False
    return True


def is_intersection_closed(f):
    fs = set(f)
    for i in range(len(f)):
        for j in range(i, len(f)):
            if (f[i] & f[j]) not in fs:
                return False
    return True


def union_size(f):
    u = 0
    for m in f:
        u |= m
    return bin(u).count("1")


def gf2_rank(f):
    rows = list(f)
    r = 0
    for c in range(14):
        p = -1
        for i in range(r, len(rows)):
            if rows[i] & (1 << c):
                p = i
                break
        if p < 0:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        for i in range(len(rows)):
            if i != r and (rows[i] & (1 << c)):
                rows[i] ^= rows[r]
        r += 1
    return r


def real_rank(f):
    from fractions import Fraction
    M = [[Fraction((m >> i) & 1) for i in range(14)] for m in f]
    r = 0
    for c in range(14):
        p = -1
        for i in range(r, len(M)):
            if M[i][c] != 0:
                p = i
                break
        if p < 0:
            continue
        M[r], M[p] = M[p], M[r]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                q = M[i][c] / M[r][c]
                M[i] = [a - q * b for a, b in zip(M[i], M[r])]
        r += 1
    return r


def poset_width(f):
    n = len(f)
    comp = [0] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            a, b = f[i], f[j]
            if (a & b) == a or (a & b) == b:
                comp[i] |= 1 << j
    best = 0
    for mask in range(1, 1 << n):
        k = bin(mask).count("1")
        if k <= best:
            continue
        ok = True
        for i in range(n):
            if not ((mask >> i) & 1):
                continue
            if comp[i] & mask:
                ok = False
                break
        if ok and k > best:
            best = k
    return best


def boolean_rank_within_F(f):
    """Min k s.t. some k-subset of F generates every f_i as OR.
    Exhaustive; worst case C(14,7)=3432 × 2^14=16384 ≈ 56M ops. Runs in ~60s."""
    n = len(f)
    target = set(f)
    for k in range(1, n + 1):
        for combo in combinations(range(n), k):
            gens = [f[i] for i in combo]
            unions = set()
            for sub in range(1 << k):
                u = 0
                for j in range(k):
                    if (sub >> j) & 1:
                        u |= gens[j]
                unions.add(u)
            if target.issubset(unions):
                return k
    return n


def quran_letter_frequency():
    quran = load_quran("no-tashkeel")
    c = Counter()
    for s in quran:
        for v in s.verses:
            for ch in v.text:
                if "\u0621" <= ch <= "\u064A" or "\u0671" <= ch <= "\u06D3":
                    if ch in "أإآ":
                        ch = "ا"
                    c[ch] += 1
    return c


def spearman_rho(x, y):
    n = len(x)
    def rankify(v):
        idx = sorted(range(n), key=lambda i: v[i])
        r = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and v[idx[j + 1]] == v[idx[i]]:
                j += 1
            avg = (i + j) / 2 + 1
            for k in range(i, j + 1):
                r[idx[k]] = avg
            i = j + 1
        return r
    rx, ry = rankify(x), rankify(y)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    dx = sum((rx[i] - mx) ** 2 for i in range(n))
    dy = sum((ry[i] - my) ** 2 for i in range(n))
    den = (dx * dy) ** 0.5
    return num / den if den > 0 else 0.0


def main():
    t0 = time.time()
    print("Observed family evaluate (fast bitmask)...")
    obs = {
        "antichain": is_antichain(MUQ),
        "intersection_closed": is_intersection_closed(MUQ),
        "real_rank": real_rank(MUQ),
        "gf2_rank": gf2_rank(MUQ),
        "union_size": union_size(MUQ),
        "poset_width": poset_width(MUQ),
        "unique_subsets": len(set(MUQ)),
    }
    print(f"  quick: {obs}")

    print("boolean_rank_within_F (exhaustive; may take ~60s)...")
    obs["boolean_rank"] = boolean_rank_within_F(MUQ)
    print(f"  boolean_rank = {obs['boolean_rank']}")

    obs["real_rank_14"] = obs["real_rank"] == 14
    obs["union_eq_14"] = obs["union_size"] == 14
    obs["poset_width_14"] = obs["poset_width"] == 14
    obs["boolean_rank_14"] = obs["boolean_rank"] == 14

    print("Letter frequency secondary...")
    lf = quran_letter_frequency()
    all_letters = sorted(lf.keys())
    freq_rank = {c: i + 1 for i, c in enumerate(sorted(all_letters, key=lambda c: -lf[c]))}
    is_muq = [1 if c in UNIVERSE else 0 for c in all_letters]
    ranks = [freq_rank[c] for c in all_letters]
    rho = spearman_rho(is_muq, ranks)

    quran_path = os.path.join(REPO, "quran-text/quran-no-tashkeel.json")
    with open(quran_path, "rb") as f:
        quran_sha = hashlib.sha256(f.read()).hexdigest()

    # compute mean letter frequency rank for muqattaat letters
    muq_ranks = [freq_rank[c] for c in UNIVERSE if c in freq_rank]
    non_muq_ranks = [freq_rank[c] for c in all_letters if c not in UNIVERSE]

    out = {
        "hypothesis_id": "H-NEW-44-observed-only",
        "run_date": "2026-04-15",
        "parent_preg": "findings/phase-b-hypotheses/h-new-44-muqattaat-combinatorial-closure-prereg.md",
        "null_status": "DEFERRED (compute-blocked; queued as H-NEW-44.1 numpy-vectorized rerun)",
        "rules_tuple": ["no-tashkeel", "orthographic-token", "graphemes",
                        "basmala-counted-only-in-surah-1", "hafs-kufan", "mashriqi"],
        "integrity_sha256": {"quran_json": quran_sha},
        "universe": UNIVERSE,
        "n_subsets": len(MUQ),
        "size_distribution": {1: 3, 2: 4, 3: 3, 4: 2, 5: 2},
        "observed_properties": obs,
        "secondary_letter_frequency": {
            "rho_is_muq_vs_freq_rank": rho,
            "n_letters_in_corpus": len(all_letters),
            "mean_freq_rank_muqattaat": sum(muq_ranks) / len(muq_ranks) if muq_ranks else None,
            "mean_freq_rank_non_muqattaat": sum(non_muq_ranks) / len(non_muq_ranks) if non_muq_ranks else None,
            "interpretation": "Negative rho and lower muqattaat mean-rank means muqattaat letters are MORE frequent on average",
            "letter_freq_rank_table": {c: {"freq": lf[c], "rank": freq_rank[c], "is_muq": c in UNIVERSE} for c in all_letters}
        },
        "runtime_seconds": time.time() - t0,
    }

    out_path = os.path.join(REPO, "findings/phase-b-hypotheses/csv/h-new-44-observed.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"wrote {out_path}")
    print(f"runtime = {time.time()-t0:.1f}s")
    print(f"Observed: {obs}")
    print(f"Spearman rho = {rho:.4f}")


if __name__ == "__main__":
    main()
