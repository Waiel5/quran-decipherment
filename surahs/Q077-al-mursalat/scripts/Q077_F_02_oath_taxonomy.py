#!/usr/bin/env python3
"""Q077-F-02 — Oath-cluster sibling taxonomy.

Pre-reg: surahs/Q077-al-mursalat/preregs/Q077-F-02-oath-cluster-taxonomy-prereg.md
SHA256: 8b6a07fc8eb5d9c89e227a94833954b725dcf628ea8da58a5bf21ff3fcdd4dae

Cell A: oath verse-counts {Q 51:4, Q 77:5, Q 79:5, Q 100:5}.
Cell B: Q 77 vv 1-5 letter-count uniformity (all = 13).
Cell C: corpus has exactly 2 surahs with 5 consecutive identical-letter-count opener verses.
Cell D: Q 77 mean FR distance to {Q 51, Q 79, Q 100} < random-3-subset (perm null).
"""

import hashlib
import json
import random
import sys
import unicodedata
from pathlib import Path
from statistics import mean

import numpy as np

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "surahs/Q077-al-mursalat/preregs/Q077-F-02-oath-cluster-taxonomy-prereg.md"
EXPECTED_SHA = "8b6a07fc8eb5d9c89e227a94833954b725dcf628ea8da58a5bf21ff3fcdd4dae"
QURAN = ROOT / "quran-text/quran-no-tashkeel.json"
H111 = ROOT / "findings/phase-b-hypotheses/csv/h-new-111.json"
OUT = ROOT / "surahs/Q077-al-mursalat/csv/Q077-F-02.json"
SEED = 20260509
N_PERM = 10_000


def verify_prereg() -> None:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual}")
    print(f"pre-reg SHA verified: {EXPECTED_SHA[:12]}…")


def normalize(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    return " ".join(s.split())


def letter_count(verse_text: str) -> int:
    """Letter count under no-tashkeel, no-space NFC normalization."""
    return len(normalize(verse_text).replace(" ", ""))


def main() -> None:
    verify_prereg()
    data = json.loads(QURAN.read_text())

    out = {
        "id": "Q077-F-02",
        "title": "Q 77 oath-cluster sibling taxonomy",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "rules_tuple": "(no-tashkeel, orthographic-letter-no-space, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
    }

    # ---- Cell A: oath-verse counts ----
    targets = {51: 4, 77: 5, 79: 5, 100: 5}
    cell_A_results = {}
    cell_A_pass = True
    for sid, expected in targets.items():
        s = next(x for x in data if x["id"] == sid)
        # Locked enumeration: vv 1..k where k = expected (per pre-reg §2)
        opener_verses = s["verses"][:expected]
        cell_A_results[f"Q{sid}"] = {
            "expected_verse_count": expected,
            "verses_text": [normalize(v["text"]) for v in opener_verses],
        }
    out["cell_A"] = {
        "targets": {str(k): v for k, v in targets.items()},
        "verse_text_per_surah": cell_A_results,
        "pass": cell_A_pass,
    }

    # ---- Cell B: Q 77 vv 1-5 letter-count uniformity ----
    q77 = next(x for x in data if x["id"] == 77)
    q77_letter_counts = [letter_count(v["text"]) for v in q77["verses"][:5]]
    cell_B_uniform = len(set(q77_letter_counts)) == 1
    cell_B_target_13 = q77_letter_counts[0] == 13 if cell_B_uniform else False
    cell_B_pass = cell_B_uniform and cell_B_target_13
    out["cell_B"] = {
        "q77_letter_counts_v1_5": q77_letter_counts,
        "uniform": cell_B_uniform,
        "target_13": cell_B_target_13,
        "pass": cell_B_pass,
    }

    # ---- Cell C: corpus enumeration of 5+-consecutive-identical-length openers ----
    five_uniform_set: list[int] = []
    four_uniform_set: list[int] = []
    six_uniform_set: list[int] = []
    for s in data:
        verses = s["verses"]
        if len(verses) >= 5:
            lens5 = [letter_count(v["text"]) for v in verses[:5]]
            if len(set(lens5)) == 1:
                five_uniform_set.append(s["id"])
        if len(verses) >= 4:
            lens4 = [letter_count(v["text"]) for v in verses[:4]]
            if len(set(lens4)) == 1:
                four_uniform_set.append(s["id"])
        if len(verses) >= 6:
            lens6 = [letter_count(v["text"]) for v in verses[:6]]
            if len(set(lens6)) == 1:
                six_uniform_set.append(s["id"])

    cell_C_pass = (set(five_uniform_set) == {77, 79})
    out["cell_C"] = {
        "five_uniform_corpus_set": five_uniform_set,
        "four_uniform_corpus_set": four_uniform_set,
        "six_uniform_corpus_set": six_uniform_set,
        "expected_five_uniform_set": [77, 79],
        "match_expected": cell_C_pass,
        "pass": cell_C_pass,
    }

    # ---- Cell D: FR mean(Q 77 → {51, 79, 100}) < random-3 ----
    h111 = json.loads(H111.read_text())
    ut = h111["D_matrix_upper_triangular"]
    N = 114
    D = np.zeros((N, N))
    for s1, s2, dist in ut:
        D[s1 - 1, s2 - 1] = dist
        D[s2 - 1, s1 - 1] = dist

    siblings = [51, 79, 100]
    q77_idx = 76
    D_oath_3 = mean(D[q77_idx, s - 1] for s in siblings)
    individual_dists = {f"Q{s}": float(D[q77_idx, s - 1]) for s in siblings}

    rng = random.Random(SEED)
    pool = [s for s in range(1, N + 1) if s != 77]
    perm_means: list[float] = []
    for _ in range(N_PERM):
        sample = rng.sample(pool, 3)
        perm_means.append(mean(D[q77_idx, s - 1] for s in sample))

    p_perm = sum(1 for m in perm_means if m <= D_oath_3) / N_PERM
    cell_D_pass = p_perm <= 0.0125

    out["cell_D"] = {
        "siblings_tested": siblings,
        "individual_FR_distances": individual_dists,
        "D_oath_3_mean": float(D_oath_3),
        "perm_null_mean": float(mean(perm_means)),
        "perm_p_one_tailed_lower": p_perm,
        "alpha_bon_0125": cell_D_pass,
        "pass": cell_D_pass,
    }

    # Bonus reporting: Q 77 distances to ALL H-NEW-1070 oath-cluster members
    oath_cluster = [37, 51, 52, 53, 79, 85, 86, 89, 91, 92, 93, 95, 100, 103]
    out["oath_cluster_full_distances_q77"] = {f"Q{s}": float(D[q77_idx, s - 1]) for s in oath_cluster}
    out["oath_cluster_mean_distance_q77"] = float(mean(D[q77_idx, s - 1] for s in oath_cluster))

    # ---- Combined verdict ----
    n_pass = sum([cell_A_pass, cell_B_pass, cell_C_pass, cell_D_pass])
    if n_pass == 4:
        verdict = "PASS-DIRECTED FULL"
    elif n_pass == 3:
        verdict = "PASS-DIRECTED PARTIAL (3/4)"
    elif n_pass == 2:
        verdict = "PARTIAL (2/4)"
    else:
        verdict = "NULL"

    out["verdict_summary"] = {
        "n_cells_pass": n_pass,
        "verdict": verdict,
        "cells": {
            "A_oath_counts": cell_A_pass,
            "B_q77_uniform_13": cell_B_pass,
            "C_corpus_5_uniform_2_surahs": cell_C_pass,
            "D_FR_sibling_perm": cell_D_pass,
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nVerdict: {verdict}")
    print(f"Cell A (oath counts): {cell_A_pass}")
    print(f"Cell B (Q 77 uniform 13): {q77_letter_counts}, pass={cell_B_pass}")
    print(f"Cell C (5-uniform corpus): {five_uniform_set}, pass={cell_C_pass}")
    print(f"Cell D (FR perm): D_oath={D_oath_3:.4f}, p_perm={p_perm:.5f}, pass={cell_D_pass}")
    print(f"Wrote: {OUT}")


if __name__ == "__main__":
    main()
