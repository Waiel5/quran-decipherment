#!/usr/bin/env python3
"""Extra analyses for the rahma-114 rigor test:
  - Per-famous-N p-values and Bonferroni/Holm corrections
  - Compute how many counts N in 1..500 have exactly 1 Quran lemma, and
    what the "hit-rate" is if we allow any famous N ∈ {7,12,19,...,786}
  - Probability that SOME famous number happens to be a singleton
  - Compute the "semantically striking" question: how many of the 89 Quran
    singleton counts have a semantically meaningful lemma?
"""
from __future__ import annotations
import json
import math
import re
from collections import Counter
from pathlib import Path

QAC = Path("/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt")
OUT = Path("/Users/grey/Downloads/quran/data/baseline-corpora")

FAMOUS = [7, 12, 19, 28, 30, 40, 77, 99, 114, 147, 313, 365, 786]


def load_lemma_counts():
    lc: Counter[str] = Counter()
    lr: dict[str, str] = {}
    with QAC.open() as f:
        for line in f:
            if line.startswith("#") or line.startswith("LOCATION"):
                continue
            p = line.rstrip("\n").split("\t")
            if len(p) < 4:
                continue
            _, form, tag, feat = p
            if "STEM" not in feat:
                continue
            m = re.search(r"LEM:([^|]+)", feat)
            if not m:
                continue
            lem = m.group(1)
            lc[lem] += 1
            rm = re.search(r"ROOT:([^|]+)", feat)
            if rm and lem not in lr:
                lr[lem] = rm.group(1)
    return lc, lr


def main():
    lc, lr = load_lemma_counts()
    n_lemmas = len(lc)
    print(f"Total QAC lemmas: {n_lemmas}")

    # Counts histogram
    ch: Counter[int] = Counter()
    for c in lc.values():
        ch[c] += 1
    # Singleton counts (N with exactly 1 lemma)
    singletons = sorted([c for c, k in ch.items() if k == 1])
    print(f"Singleton counts: {len(singletons)}")
    print(f"Of which famous: {sorted(set(singletons) & set(FAMOUS))}")

    # Sibling counts vs famous
    print("\nFor each famous N: how many Quran lemmas at exactly N?")
    for n in FAMOUS:
        lemmas = [l for l, c in lc.items() if c == n]
        mark = " <-- UNIQUE" if len(lemmas) == 1 else ""
        print(f"  N={n:4d}: {len(lemmas)} lemma(s){mark}")

    # Load empirical null rates from previous run
    with (OUT / "rahma-114-test.json").open() as f:
        prev = json.load(f)
    null = prev["empirical_null"]["famous"]

    # ----- TEST E: Bonferroni / Holm on the famous-number family ------------
    print("\n" + "=" * 72)
    print("TEST E — Bonferroni / Holm on famous-number family")
    print("=" * 72)
    # Raw p-value per famous N = observed p-value of Quran having a UNIQUE
    # lemma at N (under random-baseline-slice null)
    k = len(FAMOUS)
    rows = []
    for n in FAMOUS:
        p_unique = null[str(n)]["p_unique"]
        # Quran observed: did we have a unique lemma?
        quran_types_at_n = [l for l, c in lc.items() if c == n]
        quran_unique = len(quran_types_at_n) == 1
        # Under the null, "unique at N" has empirical probability p_unique
        # The observation is simply "yes/no". The one-sided p-value of observing
        # the Quran property under the null = p_unique if unique (because we're
        # testing: is the Quran's 'unique at N' event rare?).
        # NOTE: we're NOT controlling for the specific IDENTITY of the lemma,
        # only the event "exists a unique lemma at this count". A stronger
        # test would require that specific lemma to be semantically related.
        raw_p = p_unique if quran_unique else 1 - p_unique
        rows.append({
            "N": n,
            "quran_types_at_N": len(quran_types_at_n),
            "quran_unique": quran_unique,
            "quran_lemma_if_unique": quran_types_at_n[0] if quran_unique else None,
            "null_p_unique": p_unique,
            "null_p_any": null[str(n)]["p_any"],
            "raw_p_for_unique_event": raw_p,
        })
    print(f"{'N':>5} {'Quran #types':>14} {'Quran UNIQUE':>13} "
          f"{'null p(unique)':>15} {'raw p':>8}")
    for r in rows:
        tag = "YES" if r["quran_unique"] else "no"
        print(f"{r['N']:5d} {r['quran_types_at_N']:14d} {tag:>13} "
              f"{r['null_p_unique']:15.3f} {r['raw_p_for_unique_event']:8.3f}")
    # Bonferroni and Holm on the events where the Quran "wins"
    winners = [(r["N"], r["raw_p_for_unique_event"]) for r in rows if r["quran_unique"]]
    print(f"\nWinners (Quran UNIQUE at N): {[w[0] for w in winners]}")
    print(f"Family size k = {k}")
    # Bonferroni-corrected p-values
    print("\nBonferroni-corrected p-values (raw * k):")
    for n, p in winners:
        print(f"  N={n}: raw={p:.3f}, bonf={min(1.0, p*k):.3f}")
    # Holm step-down
    print("\nHolm step-down (sort ascending, multiply by k-i+1):")
    sorted_wins = sorted(winners, key=lambda x: x[1])
    for i, (n, p) in enumerate(sorted_wins):
        holm = min(1.0, p * (k - i))
        print(f"  rank {i+1}: N={n}, raw={p:.3f}, holm={holm:.3f}")

    # ----- Probability at least one famous N is a singleton under null -----
    print("\n" + "=" * 72)
    print("Joint probability: P(≥1 famous N is singleton) under null")
    print("=" * 72)
    # Under independence assumption (approximate):
    p_none = 1.0
    for n in FAMOUS:
        p_none *= (1 - null[str(n)]["p_unique"])
    print(f"P(no famous N has unique lemma in random 77k slice) = {p_none:.4f}")
    print(f"P(≥1 famous N has unique lemma) = {1 - p_none:.4f}")
    # This is approximate because per-slice events are correlated

    # ----- TEST C: semantic weight -- scan singleton lemmas -----------------
    print("\n" + "=" * 72)
    print("TEST C — Semantic weight of the 89 Quran singleton counts")
    print("=" * 72)
    print("(showing the 89 lemmas that are UNIQUE at their count)")
    # For each singleton count, pull the lemma
    singleton_lemmas = []
    for c, k_at_c in ch.items():
        if k_at_c == 1:
            lem = [l for l, cnt in lc.items() if cnt == c][0]
            singleton_lemmas.append((c, lem, lr.get(lem, "?")))
    singleton_lemmas.sort(key=lambda x: x[0])
    for c, lem, root in singleton_lemmas:
        mark = " *FAMOUS*" if c in FAMOUS else ""
        print(f"  N={c:5d} -> {lem:20s} (root={root}){mark}")

    # ----- Effective lemma-count support ------------------------------------
    print("\n" + "=" * 72)
    print("Lemma-count support")
    print("=" * 72)
    max_c = max(lc.values())
    print(f"Max lemma count: {max_c} ({[l for l,c in lc.items() if c == max_c]})")
    print(f"Distinct counts observed: {len(ch)}")
    # How often is a count value "used"
    used = sum(1 for c in range(1, max_c + 1) if c in ch)
    unused = max_c - used
    print(f"Integers 1..{max_c} with ≥1 lemma: {used}")
    print(f"Integers 1..{max_c} with zero lemmas: {unused}")


if __name__ == "__main__":
    main()
