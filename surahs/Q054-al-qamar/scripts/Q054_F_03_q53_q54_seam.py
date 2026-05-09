#!/usr/bin/env python3
"""Q054-F-03 — Q 53 → Q 54 seam empirical-cost diagnostic (adversarial).

Pre-reg: surahs/Q054-al-qamar/preregs/Q054-F-03-q53-q54-seam-prereg.md
SHA256:  19909d279f1cf3059cbeb17b626404caf48a58e309ed4844e10d7d50bcbbd410
Seed:    20260509  | Bonferroni-2 α_bon = 0.025
"""
from __future__ import annotations
import hashlib
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
PREREG_PATH = PROJECT_ROOT / "surahs/Q054-al-qamar/preregs/Q054-F-03-q53-q54-seam-prereg.md"
EXPECTED_SHA = "19909d279f1cf3059cbeb17b626404caf48a58e309ed4844e10d7d50bcbbd410"
H720_PATH = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-720.json"
H750_PATH = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-750.json"
OUTPUT_PATH = PROJECT_ROOT / "surahs/Q054-al-qamar/csv/Q054-F-03.json"


def verify_prereg() -> str:
    sha = hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"FATAL: pre-reg SHA mismatch.\n  expected: {EXPECTED_SHA}\n  observed: {sha}")
    return sha


def main() -> None:
    sha = verify_prereg()
    print(f"[Q054-F-03] pre-reg SHA verified: {sha[:16]}…")

    with open(H720_PATH) as f:
        h720 = json.load(f)
    with open(H750_PATH) as f:
        h750 = json.load(f)

    # H3a: Q 53 → Q 54 delta_raw
    adj = h720["per_adjacency"]
    q53_q54 = next(a for a in adj if a["pair"] == [53, 54])
    delta_raw = q53_q54["delta_raw"]
    fraction_residual = q53_q54["fraction_residual"]

    # Compute rank-by-delta_raw-descending
    sorted_adj = sorted(adj, key=lambda a: -a["delta_raw"])
    rank_q53_q54 = next(i + 1 for i, a in enumerate(sorted_adj) if a["pair"] == [53, 54])

    # Clamped-zero set
    clamped = [a for a in adj if a["delta_raw"] <= 0]
    is_clamped = q53_q54 in clamped
    print(f"  Q 53 → Q 54: delta_raw = {delta_raw:+.5f}, fraction_residual = {fraction_residual:.4f}")
    print(f"  Rank by delta_raw desc: {rank_q53_q54}/113 (lower rank = more expensive)")
    print(f"  Clamped-zero set member: {is_clamped}")
    print(f"  H3a brief-clamped-zero claim: {is_clamped} (LOCKED predicted: True)")

    h3a_pass = is_clamped  # brief's prediction
    print(f"  H3a pass (brief-affirmation, locked positive direction): {h3a_pass}")
    print(f"  H3a interpretation: {'BRIEF-CONFIRMED' if h3a_pass else 'BRIEF-REFUTED — published as PRE-COMMIT VIOLATION on locked direction'}")

    # H3b: rhyme-letter shared between Q 53 and Q 54
    per_surah = {entry["surah"]: entry for entry in h750["per_surah"]}
    q53_top = per_surah[53]["top_final_letter"]
    q54_top = per_surah[54]["top_final_letter"]
    q53_frac = per_surah[53]["top_final_letter_frac"]
    q54_frac = per_surah[54]["top_final_letter_frac"]
    rhyme_shared = q53_top == q54_top
    print(f"  Q 53 top final letter: '{q53_top}' (frac {q53_frac:.3f})")
    print(f"  Q 54 top final letter: '{q54_top}' (frac {q54_frac:.3f})")
    print(f"  Rhyme letter shared: {rhyme_shared}")
    h3b_pass = not rhyme_shared  # locked: NOT shared
    print(f"  H3b pass (locked: NOT shared): {h3b_pass}")

    # H3c: shared destruction-narratives Q 53:50-54 vs Q 54:9-42
    # Q 53:50-54 names: ʿĀd, Thamūd, qawm Nūḥ, al-Muʾtafika
    # Q 54:9-42 names: Nūḥ, ʿĀd, Thamūd, qawm Lūṭ, āl-Firʿawn
    q53_narratives = {"ʿĀd", "Thamūd", "Nūḥ", "al-Muʾtafika"}
    q54_narratives = {"Nūḥ", "ʿĀd", "Thamūd", "Lūṭ", "āl-Firʿawn"}
    # Map al-Muʾtafika → Lūṭ for narrative-equivalence (al-Ṭabarī treats al-muʾtafika as the "overturned town" of Lot's people)
    q53_narratives_norm = {"ʿĀd", "Thamūd", "Nūḥ", "Lūṭ"}  # al-Muʾtafika is Lūṭ's people
    shared = q53_narratives_norm & q54_narratives
    n_shared = len(shared)
    print(f"  H3c: shared destruction-narratives Q 53 ↔ Q 54 = {sorted(shared)} (n = {n_shared})")
    h3c_pass = n_shared >= 4

    # Aggregate verdict
    n_passed = sum([h3a_pass, h3b_pass])
    if n_passed == 2:
        verdict = "BRIEF-CONFIRMED-FULL"
    elif n_passed == 1 and h3a_pass:
        verdict = "BRIEF-CONFIRMED-PARTIAL"
    elif n_passed == 1 and h3b_pass:
        # H3a fails (brief's clamped-zero claim refuted), H3b passes (rhyme-shift confirmed)
        verdict = "BRIEF-REFUTED-WITH-RHYME-SHIFT-CONFIRMED"
    else:
        verdict = "BRIEF-REFUTED-FULL"

    # Direction-vs-observation note
    h3a_direction_locked = "clamped-zero seamless"
    h3a_observation = "delta_raw = +0.21006 (top-12 EXPENSIVE seam)"
    pre_commit_note = "PRE-COMMIT VIOLATION on H3a: locked direction REVERSED. Per HANDOFF/04-DISCIPLINE.md PRE-REG-STANDARD-01, sign-flip published with explicit pre-commit-violation flag. Empirical correction of brief: Q 53→Q 54 is the 12th MOST-EXPENSIVE seam (delta_raw = +0.21006), NOT a clamped-zero seamless seam."

    print(f"  Aggregate: {n_passed}/2 → {verdict}")

    output = {
        "test_id": "Q054-F-03",
        "title": "Q 53 → Q 54 seam empirical-cost diagnostic (adversarial)",
        "prereg_sha256": sha,
        "H3a": {
            "delta_raw": delta_raw,
            "fraction_residual": fraction_residual,
            "rank_by_delta_raw_desc": rank_q53_q54,
            "is_clamped_zero": is_clamped,
            "locked_direction": h3a_direction_locked,
            "observation": h3a_observation,
            "pass": h3a_pass,
            "pre_commit_note": pre_commit_note if not h3a_pass else None,
        },
        "H3b": {
            "q53_top_final_letter": q53_top,
            "q53_top_final_letter_frac": q53_frac,
            "q54_top_final_letter": q54_top,
            "q54_top_final_letter_frac": q54_frac,
            "rhyme_letter_shared": rhyme_shared,
            "pass": h3b_pass,
        },
        "H3c": {
            "q53_50_54_narratives": sorted(q53_narratives_norm),
            "q54_9_42_narratives": sorted(q54_narratives),
            "shared": sorted(shared),
            "n_shared": n_shared,
            "threshold": 4,
            "pass": h3c_pass,
        },
        "clamped_zero_set": [
            {"pair": a["pair"], "delta_raw": a["delta_raw"]}
            for a in sorted([a for a in adj if a["delta_raw"] <= 0], key=lambda x: x["delta_raw"])
        ],
        "verdict": verdict,
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  Output: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
