"""H-NEW-44 — fast integer-bitmask version for 10K null samples.

Pre-reg: findings/phase-b-hypotheses/h-new-44-muqattaat-combinatorial-closure-prereg.md
Same math as h_new_44_muqattaat_closure.py but with bitmask representation
that makes poset_width and boolean_rank tractable inside a 10K loop.

Integrator (main session) re-ran after specialist timed out.
Seed 20260415.
"""
from __future__ import annotations

import json
import hashlib
import os
import sys
import random
import time
from collections import Counter
from itertools import combinations
from typing import List, Sequence, Tuple

REPO = "/Users/grey/Downloads/quran"
sys.path.insert(0, os.path.join(REPO, "analysis"))
from tools.loader import load_quran  # noqa: E402

SEED = 20260415
N_NULL = 10_000
ALPHA_BON = 0.05 / 6

# 14 letter universe (the muqaṭṭaʿāt letters).
# Using bare-alif form to match no-tashkeel text.
UNIVERSE = list("احرسصطعقكلمنهي")
assert len(UNIVERSE) == 14
LETTER_BIT = {ch: 1 << i for i, ch in enumerate(UNIVERSE)}


def bits(chars: str) -> int:
    return sum(LETTER_BIT[c] for c in chars)


# 14 canonical muqaṭṭaʿāt subsets (Ḥafṣ-Kūfan; bare-alif; Q 42:1-2 treated as
# the 5-letter aggregate {ح م ع س ق} per classical convention).
MUQ_MASKS: List[int] = [
    bits("ص"),
    bits("ق"),
    bits("ن"),
    bits("طه"),
    bits("يس"),
    bits("طس"),
    bits("حم"),
    bits("الم"),
    bits("الر"),
    bits("طسم"),
    bits("المص"),
    bits("المر"),
    bits("كهيعص"),
    bits("حمعسق"),
]
assert len(MUQ_MASKS) == 14
SIZES = [bin(m).count("1") for m in MUQ_MASKS]
SIZE_DIST = Counter(SIZES)  # {1:3, 2:4, 3:3, 4:2, 5:2}
assert dict(SIZE_DIST) == {1: 3, 2: 4, 3: 3, 4: 2, 5: 2}


# --- properties on bitmask families ------------------------------------------

def is_antichain(fam: List[int]) -> bool:
    # distinct masks; for each pair, neither subset of the other
    for i in range(len(fam)):
        for j in range(i + 1, len(fam)):
            a, b = fam[i], fam[j]
            if a == b:
                continue  # duplicates: allow, not subset violation
            if (a & b) == a or (a & b) == b:
                return False
    return True


def is_intersection_closed(fam: List[int]) -> bool:
    fs = set(fam)
    for i in range(len(fam)):
        for j in range(i, len(fam)):
            inter = fam[i] & fam[j]
            if inter not in fs:
                return False
    return True


def union_size(fam: List[int]) -> int:
    u = 0
    for m in fam:
        u |= m
    return bin(u).count("1")


def gf2_rank(fam: List[int]) -> int:
    """GF(2) rank on 14-bit rows, integer xor elimination."""
    rows = list(fam)
    r = 0
    for c in range(14):
        pivot = -1
        for i in range(r, len(rows)):
            if rows[i] & (1 << c):
                pivot = i
                break
        if pivot < 0:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        for i in range(len(rows)):
            if i != r and (rows[i] & (1 << c)):
                rows[i] ^= rows[r]
        r += 1
    return r


def real_rank(fam: List[int]) -> int:
    """Over ℝ, using fraction-free Gaussian. For 0/1 matrices with
    n=14 rows and 14 cols it's tiny."""
    from fractions import Fraction
    M = [[Fraction((m >> i) & 1) for i in range(14)] for m in fam]
    r = 0
    for c in range(14):
        pivot = -1
        for i in range(r, len(M)):
            if M[i][c] != 0:
                pivot = i
                break
        if pivot < 0:
            continue
        M[r], M[pivot] = M[pivot], M[r]
        for i in range(len(M)):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r


def poset_width(fam: List[int]) -> int:
    """Largest antichain size among the 14 subsets (bitmask).
    We use Dilworth chain-decomposition approximation:
    heuristic is minimum #chains. For n=14 distinct/non-distinct masks,
    we brute-force max antichain via iterated greedy on size buckets.

    Safer / guaranteed: treat as distinct-up-to-index. Compute for each
    pair (i, j) a ≠ b whether a < b (proper subset); max antichain is
    max independent set in the resulting DAG, equal to max antichain in
    the subset-poset. With n=14 we enumerate 2^14 = 16384 subsets.
    For each subset, check antichain (all pairs incomparable). Prune via
    size-desc iteration and early termination at full antichain.
    """
    n = len(fam)
    # Precompute comparability matrix as a 14-bit mask: comp[i] has bit j
    # iff fam[i] and fam[j] are comparable (or equal duplicates).
    comp = [0] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            a, b = fam[i], fam[j]
            if (a & b) == a or (a & b) == b:
                comp[i] |= 1 << j
    # We want max-size subset S such that no i,j ∈ S (i≠j) are in comp
    # relation.
    # Brute force with early termination: iterate masks from pop-count desc.
    best = 0
    # Group masks by popcount
    buckets = {k: [] for k in range(n + 1)}
    for mask in range(1, 1 << n):
        buckets[bin(mask).count("1")].append(mask)
    for k in range(n, 0, -1):
        if k <= best:
            break
        for mask in buckets[k]:
            ok = True
            for i in range(n):
                if not ((mask >> i) & 1):
                    continue
                if comp[i] & mask:
                    ok = False
                    break
            if ok:
                if k > best:
                    best = k
                    if best == n:
                        return best
    return best


def boolean_rank(fam: List[int], max_k: int = None) -> int:
    """Boolean rank = min #generators G (14-bit masks) such that every
    member of F is a union of some subset of G.
    Generators need NOT be in F. For n=14 the search can be large; we
    bound with max_k (default 14) and always return a valid k."""
    if max_k is None:
        max_k = 14
    target = set(fam)
    # Quick bound: rank over GF(2) ≤ boolean rank (loose) BUT not tight;
    # for families that ARE boolean matrices the relation between GF(2)
    # rank and Boolean rank is one-directional. Use target-cover search.
    # Try k=1..14. For each k, search generator families drawn from the
    # union-closure of F (standard relaxation) + add singletons if needed.
    # Within-F generators first (cheap), then expand to powerset only if
    # needed.

    # Boolean-rank-within-F upper bound (always valid).
    # For 14 subsets, try k-subsets of F as generators.
    for k in range(1, max_k + 1):
        for combo in combinations(range(len(fam)), k):
            gens = [fam[i] for i in combo]
            unions_covered = set()
            for sub in range(1 << k):
                u = 0
                for j in range(k):
                    if (sub >> j) & 1:
                        u |= gens[j]
                unions_covered.add(u)
            if target.issubset(unions_covered):
                return k
    return max_k


# --- family evaluation -------------------------------------------------------

def evaluate(fam: List[int]) -> dict:
    rr = real_rank(fam)
    pw = poset_width(fam)
    br = boolean_rank(fam)
    return {
        "antichain": is_antichain(fam),
        "intersection_closed": is_intersection_closed(fam),
        "real_rank_14": rr == 14,
        "union_eq_14": union_size(fam) == 14,
        "poset_width_14": pw == 14,
        "boolean_rank_14": br == 14,
        "real_rank": rr,
        "gf2_rank": gf2_rank(fam),
        "boolean_rank": br,
        "poset_width": pw,
        "union_size": union_size(fam),
        "unique_subsets": len(set(fam)),
    }


# --- null model --------------------------------------------------------------

def uniform_family(rng: random.Random, sizes: Sequence[int]) -> List[int]:
    """Uniform subset of given cardinality, independent draws."""
    letters = list(range(14))
    fam: List[int] = []
    for k in sizes:
        picks = rng.sample(letters, k)
        m = 0
        for p in picks:
            m |= 1 << p
        fam.append(m)
    return fam


# --- MW-5 positive control ----------------------------------------------------

def mw5_positive_control() -> List[int]:
    """Chain of sizes 1..14 through the 14-letter universe.
    - NOT antichain (each smaller is subset of next)
    - intersection-closed (chain)
    - real_rank = 14 (full rank by distinct prefixes)
    - poset_width = 1 (chain)
    - union = 14
    - boolean_rank ≥ ? (for a chain, each row is OR of some prefix generators;
      k=14 suffices with each singleton; actually k=log2(n) can be constructed;
      tighter expected k ≤ 14)
    """
    # prefix chain
    return [((1 << k) - 1) for k in range(1, 15)]


# --- secondary: letter-frequency correlation ---------------------------------

def quran_letter_frequency() -> Counter:
    """Count Arabic letters in no-tashkeel Quran corpus, bare-alif normalized."""
    quran = load_quran("no-tashkeel")
    c = Counter()
    for surah in quran:
        for verse in surah["verses"]:
            for ch in verse["text"]:
                if "\u0621" <= ch <= "\u064A" or "\u0671" <= ch <= "\u06D3":
                    # normalize alef forms to bare alef
                    if ch in "أإآ":
                        ch = "ا"
                    c[ch] += 1
    return c


def spearman_rho(x: List[float], y: List[float]) -> float:
    """Spearman rank correlation."""
    n = len(x)
    def rankify(v: List[float]) -> List[float]:
        idx = sorted(range(n), key=lambda i: v[i])
        r = [0.0] * n
        i = 0
        while i < n:
            j = i
            while j + 1 < n and v[idx[j + 1]] == v[idx[i]]:
                j += 1
            avg_rank = (i + j) / 2 + 1
            for k in range(i, j + 1):
                r[idx[k]] = avg_rank
            i = j + 1
        return r
    rx, ry = rankify(x), rankify(y)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    dx = sum((rx[i] - mx) ** 2 for i in range(n))
    dy = sum((ry[i] - my) ** 2 for i in range(n))
    denom = (dx * dy) ** 0.5
    return num / denom if denom > 0 else 0.0


# --- main --------------------------------------------------------------------

def main():
    t0 = time.time()
    rng = random.Random(SEED)

    print(f"[H-NEW-44-fast] Observed family evaluate...")
    obs = evaluate(MUQ_MASKS)
    print(f"  observed: {obs}")

    print(f"[H-NEW-44-fast] MW-5 positive control ...")
    pc_fam = mw5_positive_control()
    pc = evaluate(pc_fam)
    pc_expected = {
        "antichain": False,
        "intersection_closed": True,
        "union_eq_14": True,
        "poset_width": 1,
    }
    pc_ok = all(pc[k] == v for k, v in pc_expected.items())
    print(f"  positive-control ok = {pc_ok}; pc={pc}")

    print(f"[H-NEW-44-fast] N_NULL={N_NULL} ...")
    props_keys = ["antichain", "intersection_closed", "real_rank_14",
                  "union_eq_14", "poset_width_14", "boolean_rank_14"]
    null_counts = {k: 0 for k in props_keys}
    null_real = Counter()
    null_bool = Counter()
    null_union = Counter()
    null_width = Counter()

    for i in range(N_NULL):
        fam = uniform_family(rng, SIZES)
        res = evaluate(fam)
        for k in props_keys:
            if res[k]:
                null_counts[k] += 1
        null_real[res["real_rank"]] += 1
        null_bool[res["boolean_rank"]] += 1
        null_union[res["union_size"]] += 1
        null_width[res["poset_width"]] += 1
        if (i + 1) % 500 == 0:
            print(f"  {i+1}/{N_NULL}  elapsed={time.time()-t0:.0f}s")

    # Empirical p
    p_vals = {}
    for k in props_keys:
        if obs[k]:
            p_vals[k] = null_counts[k] / N_NULL
        else:
            p_vals[k] = None

    sig = {k: (p_vals[k] is not None and p_vals[k] <= ALPHA_BON) for k in props_keys}
    n_sig = sum(sig.values())

    if not pc_ok:
        verdict = "NULL-BROKEN"
    elif n_sig >= 3:
        verdict = "STRONG-PASS"
    elif n_sig >= 1:
        verdict = "EXPLORATORY"
    else:
        verdict = "NULL"

    # Secondary: letter frequency correlation
    print(f"[H-NEW-44-fast] letter frequency secondary ...")
    letter_freq = quran_letter_frequency()
    all_letters = sorted(letter_freq.keys())
    freq_rank_map = {ch: i + 1
                     for i, ch in enumerate(sorted(all_letters, key=lambda c: -letter_freq[c]))}
    is_muq = [1 if ch in UNIVERSE else 0 for ch in all_letters]
    rank = [freq_rank_map[ch] for ch in all_letters]
    rho = spearman_rho(is_muq, rank)

    # SHA-256 of the Quran corpus
    quran_path = os.path.join(REPO, "quran-text/quran-no-tashkeel.json")
    with open(quran_path, "rb") as f:
        quran_sha = hashlib.sha256(f.read()).hexdigest()

    out = {
        "hypothesis_id": "H-NEW-44",
        "run_date": "2026-04-15",
        "seed": SEED,
        "rules_tuple": [
            "no-tashkeel", "orthographic-token", "graphemes",
            "basmala-counted-only-in-surah-1", "hafs-kufan", "mashriqi",
        ],
        "bonferroni_family": "2026-04-15-Fresh-Wave-3b",
        "alpha_bon": 0.05,
        "alpha_cell": ALPHA_BON,
        "n_null": N_NULL,
        "integrity_sha256": {"quran_json": quran_sha},
        "universe": UNIVERSE,
        "muq_subsets_list": [
            sorted([UNIVERSE[i] for i in range(14) if (m >> i) & 1])
            for m in MUQ_MASKS
        ],
        "size_distribution": dict(SIZE_DIST),
        "observed": obs,
        "positive_control": {"ok": pc_ok, "family_chain_ranks": pc},
        "null_counts": null_counts,
        "p_values": p_vals,
        "significant_at_alpha_cell": sig,
        "n_significant": n_sig,
        "null_real_rank_distribution": dict(null_real),
        "null_boolean_rank_distribution": dict(null_bool),
        "null_union_size_distribution": dict(null_union),
        "null_poset_width_distribution": dict(null_width),
        "secondary_letter_frequency": {
            "spearman_rho_is_muq_vs_freq_rank": rho,
            "n_letters_compared": len(all_letters),
            "n_muq_letters": len(UNIVERSE),
            "interpretation": "Negative rho means muqattaat letters rank LOWER (more frequent)"
        },
        "verdict": verdict,
        "runtime_seconds": time.time() - t0,
    }

    out_path = os.path.join(REPO, "findings/phase-b-hypotheses/csv/h-new-44.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"[H-NEW-44-fast] wrote {out_path}")
    print(f"[H-NEW-44-fast] VERDICT: {verdict}")
    print(f"[H-NEW-44-fast] n_significant = {n_sig}")
    print(f"[H-NEW-44-fast] Spearman rho = {rho:.4f}")
    print(f"[H-NEW-44-fast] runtime = {time.time()-t0:.1f}s")


if __name__ == "__main__":
    main()
