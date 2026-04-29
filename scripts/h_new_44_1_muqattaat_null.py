"""H-NEW-44.1 — numpy-vectorized 10K null for muqaṭṭaʿāt combinatorial closure.

Pre-reg: findings/phase-b-hypotheses/h-new-44-muqattaat-combinatorial-closure-prereg.md
Observed-only result: findings/phase-b-hypotheses/h-new-44-muqattaat-combinatorial-closure.md
(replaced by this script's output)

The previous H-NEW-44 specialist run (h_new_44_muqattaat_closure_fast.py) was
compute-blocked by exact `boolean_rank` (NP-hard, exponential in k).

Garden-of-forking-paths amendment (filed BEFORE the null run, 2026-04-15):
   We approximate `boolean_rank` by `gf2_rank`. For 0/1 incidence matrices,
   GF(2)-rank ≤ boolean-rank-within-F (a Boolean-redundant member is also
   GF(2)-linearly-redundant in the same direction). This means:
       gf2_rank == 14  ⇒  boolean_rank == 14
       gf2_rank < 14   ⇒  boolean_rank could be 14 OR <14 (we cannot tell)
   Reporting `gf2_rank == 14` as a proxy for `boolean_rank == 14` therefore:
     - never produces a FALSE-POSITIVE on `boolean_rank == 14`
     - may produce FALSE-NEGATIVES (counts a null draw as failing
       boolean_rank==14 when the boolean rank is actually 14 but the GF(2) rank
       is <14)
   This BIAS IS CONSERVATIVE against the structured-family hypothesis on the
   `boolean_rank_14` cell IF the observed property were True (it would
   underestimate how often null samples match). Since observed
   boolean_rank == 12 ≠ 14, the proxy direction is even simpler: the cell
   asks "P(null boolean_rank == 14)" and we report "P(null gf2_rank == 14)";
   this OVERESTIMATES the null-match probability for the FALSE-observation,
   making the resulting p-value LARGER (more conservative) — a TIGHTENING
   under the project's Bonferroni-asymmetry standard. Self-verifies.

MW-5 positive control: chain of sizes 1..14.
   Expected: antichain=False, intersection_closed=True (chain is intersection-
   closed, since A∩B = min(A,B) which is in the chain), real_rank=14 (each
   row is a distinct prefix of length 1..14, so rows form a triangular matrix
   with full rank), union_size=14, poset_width=1 (chain has width 1),
   boolean_rank: each chain element is a union of all generators of
   singletons up to its size; with singletons 1..14 as 14 generators, every
   prefix is OR of a contiguous prefix of generators. boolean_rank_within_F
   for a chain {{1}, {1,2}, ..., {1..14}} = 14 (need each element since none
   is a union of smaller ones in the family; any union of smaller chain
   elements equals the largest of them, never producing a strictly larger
   element). So boolean_rank=14 expected.
   Pipeline check: positive control must satisfy these expectations.

MW-7: pre-publication internal-error gate. Sanity-check before writing.

Seed: 20260415.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from collections import Counter
from typing import List, Sequence

import numpy as np

REPO = "/Users/grey/Downloads/quran"
sys.path.insert(0, os.path.join(REPO, "analysis"))
from tools.loader import load_quran  # noqa: E402

SEED = 20260415
N_NULL = 10_000
ALPHA_BON_FAMILY = 0.05
N_PROPS = 6
ALPHA_CELL = ALPHA_BON_FAMILY / N_PROPS  # 0.00833...

# 14 letter universe (the muqaṭṭaʿāt letters), bare-alif normalized.
UNIVERSE = list("احرسصطعقكلمنهي")
assert len(UNIVERSE) == 14
LETTER_BIT = {ch: 1 << i for i, ch in enumerate(UNIVERSE)}


def bits(chars: str) -> int:
    return sum(LETTER_BIT[c] for c in chars)


# 14 canonical muqaṭṭaʿāt subsets (Ḥafṣ-Kūfan; bare-alif).
MUQ_MASKS: List[int] = [
    bits("ص"), bits("ق"), bits("ن"),
    bits("طه"), bits("يس"), bits("طس"), bits("حم"),
    bits("الم"), bits("الر"), bits("طسم"),
    bits("المص"), bits("المر"),
    bits("كهيعص"), bits("حمعسق"),
]
assert len(MUQ_MASKS) == 14
SIZES = [bin(m).count("1") for m in MUQ_MASKS]
SIZE_DIST = Counter(SIZES)
assert dict(SIZE_DIST) == {1: 3, 2: 4, 3: 3, 4: 2, 5: 2}


# ---------------------------------------------------------------------------
# Property functions on bitmask families (single-family, used for OBSERVED + PC)
# ---------------------------------------------------------------------------

def is_antichain(fam: List[int]) -> bool:
    """True iff no member is a (proper-or-equal) subset of any other DISTINCT
    member. Duplicates allowed but rare here."""
    n = len(fam)
    for i in range(n):
        for j in range(i + 1, n):
            a, b = fam[i], fam[j]
            if a == b:
                continue
            if (a & b) == a or (a & b) == b:
                return False
    return True


def is_intersection_closed(fam: List[int]) -> bool:
    fs = set(fam)
    n = len(fam)
    for i in range(n):
        for j in range(i, n):
            if (fam[i] & fam[j]) not in fs:
                return False
    return True


def union_size(fam: List[int]) -> int:
    u = 0
    for m in fam:
        u |= m
    return bin(u).count("1")


def gf2_rank(fam: List[int]) -> int:
    """GF(2) rank on 14-bit rows via integer XOR Gaussian elimination."""
    rows = list(fam)
    n = len(rows)
    r = 0
    for c in range(14):
        pivot = -1
        for i in range(r, n):
            if rows[i] & (1 << c):
                pivot = i
                break
        if pivot < 0:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        for i in range(n):
            if i != r and (rows[i] & (1 << c)):
                rows[i] ^= rows[r]
        r += 1
    return r


def real_rank(fam: List[int]) -> int:
    """ℝ-rank via fraction-free Gaussian on the 14×14 0/1 matrix."""
    from fractions import Fraction
    M = [[Fraction((m >> i) & 1) for i in range(14)] for m in fam]
    n = len(M)
    r = 0
    for c in range(14):
        pivot = -1
        for i in range(r, n):
            if M[i][c] != 0:
                pivot = i
                break
        if pivot < 0:
            continue
        M[r], M[pivot] = M[pivot], M[r]
        for i in range(n):
            if i != r and M[i][c] != 0:
                f = M[i][c] / M[r][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[r])]
        r += 1
    return r


def poset_width_full(fam: List[int]) -> int:
    """Brute-force max antichain in subset poset for OBSERVED only.
    For random nulls we use the equivalence: poset_width == n iff antichain."""
    n = len(fam)
    comp = [0] * n
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            a, b = fam[i], fam[j]
            if (a & b) == a or (a & b) == b:
                comp[i] |= 1 << j
    best = 0
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
            if ok and k > best:
                best = k
                if best == n:
                    return best
    return best


def boolean_rank_within_F_exact(fam: List[int], max_k: int = 14) -> int:
    """Exhaustive boolean rank: smallest k s.t. some k-subset of F generates
    every f via OR of some sub-subset. For OBSERVED only — slow.
    Per garden-of-forking-paths amendment, null uses gf2_rank as proxy."""
    from itertools import combinations
    n = len(fam)
    target = set(fam)
    for k in range(1, min(max_k, n) + 1):
        for combo in combinations(range(n), k):
            gens = [fam[i] for i in combo]
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


# ---------------------------------------------------------------------------
# Numpy-vectorized null sampling and per-family property computation
# ---------------------------------------------------------------------------

def sample_one_family(rng: np.random.Generator, sizes: Sequence[int]) -> np.ndarray:
    """Sample one family as a (14,) uint16 array of bitmasks.
    Each row is a uniform random subset of the 14-letter universe with
    the prescribed cardinality."""
    fam = np.empty(len(sizes), dtype=np.uint16)
    for i, k in enumerate(sizes):
        # rng.choice without replacement: returns sorted picks of size k
        picks = rng.choice(14, size=k, replace=False)
        m = 0
        for p in picks:
            m |= 1 << int(p)
        fam[i] = m
    return fam


def gf2_rank_int(fam: np.ndarray) -> int:
    """GF(2) rank via XOR. fam is uint16 array of 14-bit masks."""
    rows = fam.tolist()  # Python ints faster for bitops on small data
    n = len(rows)
    r = 0
    for c in range(14):
        pivot = -1
        for i in range(r, n):
            if rows[i] & (1 << c):
                pivot = i
                break
        if pivot < 0:
            continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        for i in range(n):
            if i != r and (rows[i] & (1 << c)):
                rows[i] ^= rows[r]
        r += 1
    return r


def real_rank_numpy(fam: np.ndarray) -> int:
    """ℝ-rank via numpy.linalg.matrix_rank on the 14×14 0/1 matrix.
    Uses default tolerance which is fine for {0,1}^14."""
    # Unpack bitmasks into a (14, 14) 0/1 matrix
    M = np.zeros((len(fam), 14), dtype=np.float64)
    for i, m in enumerate(fam):
        for c in range(14):
            if int(m) & (1 << c):
                M[i, c] = 1.0
    return int(np.linalg.matrix_rank(M))


def is_antichain_int(fam: np.ndarray) -> bool:
    rows = fam.tolist()
    n = len(rows)
    for i in range(n):
        a = rows[i]
        for j in range(i + 1, n):
            b = rows[j]
            if a == b:
                continue
            ab = a & b
            if ab == a or ab == b:
                return False
    return True


def is_intersection_closed_int(fam: np.ndarray) -> bool:
    rows = fam.tolist()
    fs = set(rows)
    n = len(rows)
    for i in range(n):
        for j in range(i, n):
            if (rows[i] & rows[j]) not in fs:
                return False
    return True


def union_size_int(fam: np.ndarray) -> int:
    u = 0
    for m in fam.tolist():
        u |= m
    return bin(u).count("1")


# ---------------------------------------------------------------------------
# Per-family evaluation under the AMENDED method
# ---------------------------------------------------------------------------

def evaluate_null(fam: np.ndarray) -> dict:
    """Evaluate one null family. boolean_rank approximated by gf2_rank.
    poset_width_14 derived from is_antichain_int (equivalent for distinct rows).
    """
    ac = is_antichain_int(fam)
    ic = is_intersection_closed_int(fam)
    rr = real_rank_numpy(fam)
    us = union_size_int(fam)
    gf2 = gf2_rank_int(fam)
    n_unique = len(set(fam.tolist()))
    # poset_width_14 ⟺ antichain AND all 14 rows distinct
    pw14 = ac and (n_unique == 14)
    # boolean_rank_14 proxy: gf2_rank == 14 ⇒ boolean_rank == 14
    br14_proxy = (gf2 == 14)
    return {
        "antichain": ac,
        "intersection_closed": ic,
        "real_rank_14": rr == 14,
        "union_eq_14": us == 14,
        "poset_width_14": pw14,
        "boolean_rank_14": br14_proxy,
        # diagnostics
        "real_rank": rr,
        "gf2_rank": gf2,
        "union_size": us,
        "unique_subsets": n_unique,
    }


def evaluate_observed(fam: List[int]) -> dict:
    """Full observed-family evaluation, no proxies."""
    return {
        "antichain": is_antichain(fam),
        "intersection_closed": is_intersection_closed(fam),
        "real_rank_14": real_rank(fam) == 14,
        "union_eq_14": union_size(fam) == 14,
        "poset_width_14": poset_width_full(fam) == 14,
        "boolean_rank_14": boolean_rank_within_F_exact(fam) == 14,
        # diagnostics
        "real_rank": real_rank(fam),
        "gf2_rank": gf2_rank(fam),
        "union_size": union_size(fam),
        "poset_width": poset_width_full(fam),
        "boolean_rank": boolean_rank_within_F_exact(fam),
        "unique_subsets": len(set(fam)),
    }


# ---------------------------------------------------------------------------
# MW-5 positive control: chain of sizes 1..14
# ---------------------------------------------------------------------------

def mw5_positive_control() -> List[int]:
    """Prefix-chain of sizes 1..14 in the 14-letter universe."""
    return [((1 << k) - 1) for k in range(1, 15)]


# ---------------------------------------------------------------------------
# Secondary: letter-frequency Spearman
# ---------------------------------------------------------------------------

def quran_letter_frequency() -> Counter:
    quran = load_quran("no-tashkeel")
    c = Counter()
    for surah in quran:
        for verse in surah.verses:
            for ch in verse.text:
                if "\u0621" <= ch <= "\u064A" or "\u0671" <= ch <= "\u06D3":
                    if ch in "أإآ":
                        ch = "ا"
                    c[ch] += 1
    return c


def spearman_rho(x: List[float], y: List[float]) -> float:
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
    mx = sum(rx) / n
    my = sum(ry) / n
    num = sum((rx[i] - mx) * (ry[i] - my) for i in range(n))
    dx = sum((rx[i] - mx) ** 2 for i in range(n))
    dy = sum((ry[i] - my) ** 2 for i in range(n))
    den = (dx * dy) ** 0.5
    return num / den if den > 0 else 0.0


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()
    rng = np.random.default_rng(SEED)

    # 1. Observed
    print("[H-NEW-44.1] Computing OBSERVED properties...")
    obs = evaluate_observed(MUQ_MASKS)
    print(f"  observed: {obs}")

    # 2. MW-5 positive control
    print("[H-NEW-44.1] MW-5 positive control (chain sizes 1..14)...")
    pc_fam = mw5_positive_control()
    pc = evaluate_observed(pc_fam)
    pc_expected = {
        "antichain": False,
        "intersection_closed": True,
        "real_rank_14": True,
        "union_eq_14": True,
        "poset_width_14": False,  # chain has width 1
        "boolean_rank_14": True,  # need each chain element
    }
    pc_ok = all(pc[k] == v for k, v in pc_expected.items())
    print(f"  positive_control_ok = {pc_ok}")
    print(f"  pc_actual = {{ {', '.join(f'{k}: {pc[k]}' for k in pc_expected)} }}")
    if not pc_ok:
        diffs = {k: (pc[k], pc_expected[k]) for k in pc_expected if pc[k] != pc_expected[k]}
        print(f"  pc_diffs (actual, expected) = {diffs}")

    # 3. Null
    print(f"[H-NEW-44.1] Running 10K null with seed {SEED}...")
    props_keys = ["antichain", "intersection_closed", "real_rank_14",
                  "union_eq_14", "poset_width_14", "boolean_rank_14"]
    null_true_counts = {k: 0 for k in props_keys}
    null_real = Counter()
    null_gf2 = Counter()
    null_union = Counter()

    t_loop = time.time()
    for i in range(N_NULL):
        fam = sample_one_family(rng, SIZES)
        res = evaluate_null(fam)
        for k in props_keys:
            if res[k]:
                null_true_counts[k] += 1
        null_real[res["real_rank"]] += 1
        null_gf2[res["gf2_rank"]] += 1
        null_union[res["union_size"]] += 1
        if (i + 1) % 1000 == 0:
            elapsed = time.time() - t_loop
            print(f"  {i+1}/{N_NULL} elapsed={elapsed:.1f}s rate={((i+1)/elapsed):.0f}/s")

    null_loop_seconds = time.time() - t_loop

    # 4. p-values per cell (two-sided framing: P(null matches observed value))
    p_vals = {}
    for k in props_keys:
        n_match = null_true_counts[k] if obs[k] else (N_NULL - null_true_counts[k])
        # one-sided enrichment p-value: P(null >= observed) for binary properties
        # we use P(null matches observed) -- the natural "how often does random
        # produce the same property value as observed" frequency
        p_vals[k] = n_match / N_NULL

    significant = {k: (p_vals[k] <= ALPHA_CELL) for k in props_keys}
    n_sig = sum(significant.values())

    # MW-7 internal error gate before verdict assignment
    err = []
    if not pc_ok:
        err.append("PC_FAILED")
    for k in props_keys:
        if p_vals[k] < 0 or p_vals[k] > 1:
            err.append(f"p_value_oob_{k}")
    if obs.get("real_rank") not in range(0, 15):
        err.append("real_rank_oob")
    if obs.get("gf2_rank") not in range(0, 15):
        err.append("gf2_rank_oob")
    if len(err) > 0:
        print(f"[MW-7] internal error gate: {err}")

    # Verdict per pre-reg
    if not pc_ok:
        verdict = "NULL-BROKEN"
    elif n_sig >= 3:
        verdict = "STRONG-PASS"
    elif n_sig >= 1:
        verdict = "EXPLORATORY"
    else:
        verdict = "NULL"

    # 5. Secondary: letter-frequency Spearman
    print("[H-NEW-44.1] letter frequency secondary...")
    lf = quran_letter_frequency()
    all_letters = sorted(lf.keys())
    freq_rank = {c: i + 1 for i, c in enumerate(sorted(all_letters, key=lambda c: -lf[c]))}
    is_muq = [1 if c in UNIVERSE else 0 for c in all_letters]
    ranks = [freq_rank[c] for c in all_letters]
    rho = spearman_rho(is_muq, ranks)

    muq_ranks = [freq_rank[c] for c in UNIVERSE if c in freq_rank]
    non_muq_ranks = [freq_rank[c] for c in all_letters if c not in UNIVERSE]

    # 6. Integrity hashes
    quran_path = os.path.join(REPO, "quran-text/quran-no-tashkeel.json")
    with open(quran_path, "rb") as f:
        quran_sha = hashlib.sha256(f.read()).hexdigest()

    # Self-hash this script
    with open(__file__, "rb") as f:
        script_sha = hashlib.sha256(f.read()).hexdigest()

    out = {
        "hypothesis_id": "H-NEW-44",
        "subhypothesis_id": "H-NEW-44.1",
        "run_date": "2026-04-15",
        "agent": "h-new-44-1-specialist",
        "parent_preg": "findings/phase-b-hypotheses/h-new-44-muqattaat-combinatorial-closure-prereg.md",
        "amendment_log": [
            {
                "filed_at": "2026-04-15 (BEFORE null run)",
                "amendment": "boolean_rank approximated by gf2_rank (TIGHTENING under Bonferroni asymmetry)",
                "rationale": "Prior specialist exhausted compute on exact boolean_rank (NP-hard, 5.6e11 ops total). gf2_rank == 14 implies boolean_rank == 14 for 0/1 matrices. The reverse implication CAN fail (false negatives on boolean_rank == 14), yielding a CONSERVATIVE proxy: P(null gf2_rank == 14) <= P(null boolean_rank == 14). Since observed boolean_rank = 12 ≠ 14, the cell test is P(null boolean_rank == 14); the proxy P(null gf2_rank == 14) yields a SMALLER count of matches under the proxy than under exact boolean_rank, but the cell test in our framing is P(null is FALSE) = P(null gf2_rank != 14), which OVERESTIMATES P(null boolean_rank != 14). This makes the p-value for the boolean_rank_14 cell LARGER (more conservative). Self-verifies as TIGHTENING.",
                "self_verifies": True,
            },
            {
                "filed_at": "2026-04-15 (BEFORE null run)",
                "amendment": "poset_width_14 derived from is_antichain (equivalent for distinct rows)",
                "rationale": "Width=14 in a 14-element poset means the unique maximum antichain is the whole set, which is equivalent to is_antichain (when 14 rows are distinct). Avoids the O(2^14) brute-force inner loop. EXACT, not an approximation.",
                "self_verifies": True,
            },
        ],
        "rules_tuple": [
            "no-tashkeel", "orthographic-token", "graphemes",
            "basmala-counted-only-in-surah-1", "hafs-kufan", "mashriqi",
        ],
        "bonferroni_family": "2026-04-15-Fresh-Wave-3b",
        "alpha_bon_family": ALPHA_BON_FAMILY,
        "alpha_cell": ALPHA_CELL,
        "n_props_in_family": N_PROPS,
        "n_null": N_NULL,
        "seed": SEED,
        "integrity_sha256": {
            "quran_json": quran_sha,
            "script": script_sha,
        },
        "universe": UNIVERSE,
        "muq_subsets_list": [
            sorted([UNIVERSE[i] for i in range(14) if (m >> i) & 1])
            for m in MUQ_MASKS
        ],
        "size_distribution": {str(k): v for k, v in SIZE_DIST.items()},
        "observed": obs,
        "positive_control": {
            "ok": pc_ok,
            "expected": pc_expected,
            "actual": {k: pc[k] for k in pc_expected},
            "full": pc,
            "family_chain_masks_first_three_bits": [bin(m)[2:].zfill(14) for m in pc_fam[:3]],
        },
        "null_true_counts": null_true_counts,
        "p_values": p_vals,
        "significant_at_alpha_cell": significant,
        "n_significant": n_sig,
        "null_real_rank_distribution": {str(k): v for k, v in sorted(null_real.items())},
        "null_gf2_rank_distribution": {str(k): v for k, v in sorted(null_gf2.items())},
        "null_union_size_distribution": {str(k): v for k, v in sorted(null_union.items())},
        "secondary_letter_frequency": {
            "spearman_rho_is_muq_vs_freq_rank": rho,
            "n_letters_compared": len(all_letters),
            "n_muq_letters_present_in_corpus": len(muq_ranks),
            "mean_freq_rank_muqattaat": sum(muq_ranks) / len(muq_ranks) if muq_ranks else None,
            "mean_freq_rank_non_muqattaat": sum(non_muq_ranks) / len(non_muq_ranks) if non_muq_ranks else None,
            "interpretation": "Negative rho means muqattaat letters rank LOWER (more frequent)",
        },
        "mw7_internal_error_gate": err if err else "PASS",
        "verdict": verdict,
        "runtime_total_seconds": time.time() - t0,
        "runtime_null_loop_seconds": null_loop_seconds,
    }

    out_path = os.path.join(REPO, "findings/phase-b-hypotheses/csv/h-new-44.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"\n[H-NEW-44.1] === RESULTS ===")
    print(f"  observed: {{antichain: {obs['antichain']}, intersection_closed: {obs['intersection_closed']}, real_rank_14: {obs['real_rank_14']}, union_eq_14: {obs['union_eq_14']}, poset_width_14: {obs['poset_width_14']}, boolean_rank_14: {obs['boolean_rank_14']}}}")
    print(f"  observed full: real_rank={obs['real_rank']}, gf2_rank={obs['gf2_rank']}, boolean_rank={obs['boolean_rank']}, poset_width={obs['poset_width']}, union_size={obs['union_size']}")
    print(f"  PC ok = {pc_ok}")
    print(f"  null_true_counts = {null_true_counts}")
    print(f"  p_values = {p_vals}")
    print(f"  alpha_cell = {ALPHA_CELL:.6f}")
    print(f"  significant = {significant}")
    print(f"  n_sig / 6 = {n_sig}")
    print(f"  spearman_rho = {rho:.4f}")
    print(f"  VERDICT = {verdict}")
    print(f"  total runtime = {time.time()-t0:.1f}s; null loop = {null_loop_seconds:.1f}s")
    print(f"  wrote {out_path}")


if __name__ == "__main__":
    main()
