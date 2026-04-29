#!/usr/bin/env python3
"""
H-NEW-140.1 — All-pair de-circularization of H-NEW-140.

Pre-registered at findings/phase-b-hypotheses/h-new-140-1-all-pair-decircularization-prereg.md

Enumerate C(20, 2) = 190 pairs, rank by z-score, compare top-16 to classical-anchor 16.
Leave-one-out sensitivity: remove ʿAzīz+Ḥakīm, recompute aggregate ratio.

Runtime < 1 min.
Seed: 20260417.
"""
from __future__ import annotations

import json
import math
from itertools import combinations
from pathlib import Path


QURAN_JSON = Path("/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json")
OUTPUT_JSON = Path("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-140-1.json")

# --- Locked 20-name list (see pre-reg) ---
# Each tuple: (label, primary_form, alt_forms...)
NAMES_20 = [
    ("al-Raḥmān", "الرحمن", "رحمن"),
    ("al-Raḥīm", "الرحيم", "رحيم"),
    ("al-ʿAzīz", "العزيز", "عزيز"),
    ("al-Ḥakīm", "الحكيم", "حكيم"),
    ("al-Samīʿ", "السميع", "سميع"),
    ("al-Baṣīr", "البصير", "بصير"),
    ("al-Ghafūr", "الغفور", "غفور"),
    ("al-Tawwāb", "التواب", "تواب"),
    ("al-ʿAlīm", "العليم", "عليم"),
    ("al-Ḥalīm", "الحليم", "حليم"),
    ("al-Shakūr", "الشكور", "شكور"),
    ("al-Wadūd", "الودود", "ودود"),
    ("al-Qadīr", "القدير", "قدير"),
    ("al-Khabīr", "الخبير", "خبير"),
    ("al-Laṭīf", "اللطيف", "لطيف"),
    ("al-Malik", "الملك", "ملك"),
    ("al-Quddūs", "القدوس", "قدوس"),
    ("al-Salām", "السلام", "سلام"),
    ("al-Muʾmin", "المؤمن", "مؤمن"),
    ("al-Muhaymin", "المهيمن", "مهيمن"),
]
assert len(NAMES_20) == 20

# --- Classical-anchor 16 pairs from H-NEW-140 ---
# Using labels; matched to NAMES_20 by label
CLASSICAL_PAIRS_16 = [
    ("al-Raḥmān", "al-Raḥīm"),
    ("al-ʿAzīz", "al-Ḥakīm"),
    ("al-Samīʿ", "al-Baṣīr"),
    ("al-Ghafūr", "al-Raḥīm"),
    ("al-Tawwāb", "al-Raḥīm"),
    ("al-ʿAzīz", "al-Ghafūr"),
    ("al-ʿAzīz", "al-ʿAlīm"),
    ("al-ʿAzīz", "al-Raḥīm"),
    ("al-ʿAlīm", "al-Ḥakīm"),
    ("al-Ḥalīm", "al-Ghafūr"),
    ("al-Shakūr", "al-Ḥalīm"),
    ("al-Wadūd", "al-Ghafūr"),
    ("al-Qadīr", "al-ʿAlīm"),
    ("al-Khabīr", "al-ʿAlīm"),
    ("al-Laṭīf", "al-Khabīr"),
    ("al-Samīʿ", "al-ʿAlīm"),
]
assert len(CLASSICAL_PAIRS_16) == 16


def verse_contains_name(verse_text: str, forms: tuple[str, ...]) -> bool:
    """Return True if any of the name forms appears as a whole word in the verse.
    Whole-word = surrounded by non-letter chars or at string boundaries.
    Arabic letter class: U+0621-U+064A.
    """
    import re
    for form in forms:
        # Anchor so the form does not appear as a substring of a longer word
        pattern = r"(^|[^\u0621-\u064A])" + re.escape(form) + r"($|[^\u0621-\u064A])"
        if re.search(pattern, verse_text):
            return True
    return False


def main() -> None:
    print("H-NEW-140.1 — all-pair de-circularization", flush=True)
    with QURAN_JSON.open() as f:
        quran = json.load(f)

    # Flatten verses
    verses = []
    for surah in quran:
        for v in surah["verses"]:
            verses.append({"surah": surah["id"], "verse": v["id"], "text": v["text"]})
    N = len(verses)
    print(f"Loaded {N} verses", flush=True)
    assert N >= 6230

    # Per-name presence vector
    print("Computing name presence per verse …", flush=True)
    presence = {}
    for label, *forms in NAMES_20:
        forms_tup = tuple(forms) if isinstance(forms, list) else tuple(forms)
        pv = [verse_contains_name(v["text"], tuple(forms)) for v in verses]
        presence[label] = pv
        n_verses = sum(pv)
        print(f"  {label}: {n_verses} verses", flush=True)

    # Compute all 190 pair stats
    print("\nComputing all 190 pair co-occurrences …", flush=True)
    labels = [lab for lab, *_ in NAMES_20]
    pair_stats = []
    for a, b in combinations(labels, 2):
        pa = presence[a]
        pb = presence[b]
        na = sum(pa)
        nb = sum(pb)
        obs = sum(1 for i in range(N) if pa[i] and pb[i])
        expected = na * nb / N
        if expected > 0:
            z = (obs - expected) / math.sqrt(expected)
        else:
            z = float("inf") if obs > 0 else 0.0
        pair_stats.append({
            "pair": (a, b),
            "name_a_count": na,
            "name_b_count": nb,
            "observed": obs,
            "expected": expected,
            "z": z,
            "ratio": (obs / expected) if expected > 0 else float("inf"),
        })

    # Rank by z
    pair_stats.sort(key=lambda d: -d["z"])
    print(f"\nTop 25 empirical pairs (by z-score):", flush=True)
    print(f"{'Rank':>4}  {'Pair':<40}  {'Obs':>4}  {'Exp':>8}  {'z':>8}  {'Classical?':<10}", flush=True)
    classical_set = set(frozenset(p) for p in CLASSICAL_PAIRS_16)
    for i, ps in enumerate(pair_stats[:25]):
        a, b = ps["pair"]
        is_classical = "YES" if frozenset((a, b)) in classical_set else ""
        print(f"{i+1:>4}  {a + ' + ' + b:<40}  {ps['observed']:>4}  {ps['expected']:>8.2f}  {ps['z']:>+8.2f}  {is_classical:<10}", flush=True)

    # Top-16 match rate
    top_16_empirical = set(frozenset(ps["pair"]) for ps in pair_stats[:16])
    match_count = sum(1 for cp in CLASSICAL_PAIRS_16 if frozenset(cp) in top_16_empirical)
    match_rate = match_count / 16
    print(f"\n=== Match count: {match_count}/16 = {match_rate*100:.1f}% ===", flush=True)

    # Decision
    if match_rate > 0.50:
        decision = "CIRCULARITY-NEUTRALIZED"
        interp = "Classical selection tracks the empirical strongest pairs. H-NEW-140 stands."
    elif match_rate >= 0.30:
        decision = "MIXED"
        interp = "Classical list partially tracks empirical signal; non-empirical considerations also play a role."
    else:
        decision = "CLASSICAL-SELECTION-BIASED"
        interp = "Classical selection reflects theological considerations, not empirical strength. H-NEW-140 demoted to descriptive."

    print(f"\nDecision: {decision}", flush=True)
    print(f"Interpretation: {interp}", flush=True)

    # Leave-one-out sensitivity: remove ʿAzīz+Ḥakīm from classical-pairs aggregate
    classical_pair_stats = [
        ps for ps in pair_stats
        if frozenset(ps["pair"]) in classical_set
    ]
    total_obs = sum(ps["observed"] for ps in classical_pair_stats)
    total_exp = sum(ps["expected"] for ps in classical_pair_stats)
    ratio_all = total_obs / total_exp if total_exp > 0 else float("inf")

    # Without ʿAzīz+Ḥakīm
    remove_pair = frozenset(("al-ʿAzīz", "al-Ḥakīm"))
    classical_pair_stats_loo = [
        ps for ps in classical_pair_stats
        if frozenset(ps["pair"]) != remove_pair
    ]
    total_obs_loo = sum(ps["observed"] for ps in classical_pair_stats_loo)
    total_exp_loo = sum(ps["expected"] for ps in classical_pair_stats_loo)
    ratio_loo = total_obs_loo / total_exp_loo if total_exp_loo > 0 else float("inf")

    print(f"\nLeave-one-out sensitivity (remove al-ʿAzīz+al-Ḥakīm):", flush=True)
    print(f"  All 16 classical pairs: obs={total_obs}, exp={total_exp:.2f}, ratio={ratio_all:.2f}×", flush=True)
    print(f"  Remove ʿAzīz+Ḥakīm (15 pairs): obs={total_obs_loo}, exp={total_exp_loo:.2f}, ratio={ratio_loo:.2f}×", flush=True)

    if ratio_loo > 5.0:
        loo_verdict = "ROBUST — main finding holds without the outlier"
    elif ratio_loo > 3.0:
        loo_verdict = "MODERATELY-ROBUST — main finding weakens without outlier but stays positive"
    else:
        loo_verdict = "OUTLIER-DRIVEN — main finding reduced substantially without outlier"
    print(f"  LOO verdict: {loo_verdict}", flush=True)

    # Output JSON
    pairs_out = []
    for i, ps in enumerate(pair_stats):
        a, b = ps["pair"]
        pairs_out.append({
            "rank": i + 1,
            "name_a": a,
            "name_b": b,
            "obs": ps["observed"],
            "expected": ps["expected"],
            "z": ps["z"],
            "ratio": ps["ratio"],
            "is_classical": frozenset((a, b)) in classical_set,
        })

    out = {
        "id": "H-NEW-140.1",
        "title": "All-pair de-circularization of H-NEW-140 divine-name pair cohesion",
        "seed": 20260417,
        "n_verses": N,
        "n_names": len(NAMES_20),
        "n_pairs_total": len(pair_stats),
        "n_classical_pairs": len(CLASSICAL_PAIRS_16),
        "names_20": [lab for lab, *_ in NAMES_20],
        "classical_pairs_16": [[a, b] for a, b in CLASSICAL_PAIRS_16],
        "name_verse_counts": {lab: sum(presence[lab]) for lab, *_ in NAMES_20},
        "all_pairs_ranked_by_z": pairs_out,
        "match_count_top16": match_count,
        "match_rate_top16": match_rate,
        "decision_primary": decision,
        "decision_interpretation": interp,
        "loo_sensitivity": {
            "all16_obs": total_obs,
            "all16_exp": total_exp,
            "all16_ratio": ratio_all,
            "loo_remove": "al-ʿAzīz+al-Ḥakīm",
            "loo15_obs": total_obs_loo,
            "loo15_exp": total_exp_loo,
            "loo15_ratio": ratio_loo,
            "loo_verdict": loo_verdict,
        },
    }
    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_JSON.open("w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\nWrote {OUTPUT_JSON}", flush=True)


if __name__ == "__main__":
    main()
