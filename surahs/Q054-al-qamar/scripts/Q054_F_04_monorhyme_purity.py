#!/usr/bin/env python3
"""Q054-F-04 — Q 54 al-Qamar 100% rāʾ-monorhyme corpus-uniqueness test.

Pre-reg: surahs/Q054-al-qamar/preregs/Q054-F-04-monorhyme-purity-prereg.md
SHA256:  8c1331667d6123c9290da740786d4321971c885c7307da9e9b19b4cf977a67ec
Seed:    20260509  | Bonferroni-2 α_bon = 0.025
"""
from __future__ import annotations
import hashlib
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
PREREG_PATH = PROJECT_ROOT / "surahs/Q054-al-qamar/preregs/Q054-F-04-monorhyme-purity-prereg.md"
EXPECTED_SHA = "8c1331667d6123c9290da740786d4321971c885c7307da9e9b19b4cf977a67ec"
H750_PATH = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-750.json"
QURAN_PATH = PROJECT_ROOT / "quran-text/quran-no-tashkeel.json"
OUTPUT_PATH = PROJECT_ROOT / "surahs/Q054-al-qamar/csv/Q054-F-04.json"


def verify_prereg() -> str:
    sha = hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"FATAL: pre-reg SHA mismatch.\n  expected: {EXPECTED_SHA}\n  observed: {sha}")
    return sha


def main() -> None:
    sha = verify_prereg()
    print(f"[Q054-F-04] pre-reg SHA verified: {sha[:16]}…")

    with open(H750_PATH) as f:
        h750 = json.load(f)
    with open(QURAN_PATH) as f:
        corpus = json.load(f)

    per_surah = {entry["surah"]: entry for entry in h750["per_surah"]}

    # H4a: top_final_letter_frac == 1.0
    q54 = per_surah[54]
    frac_q54 = q54["top_final_letter_frac"]
    top_letter = q54["top_final_letter"]
    rhyme_entropy = q54["rhyme_entropy_nats"]
    h4a_pass = frac_q54 == 1.0
    print(f"  H4a: Q 54 top final letter '{top_letter}' frac = {frac_q54:.4f}; pass (==1.0): {h4a_pass}")

    # H4b: rank_B == 114 (corpus minimum)
    rank_b = q54["rank_B"]
    rank_a = q54["rank_A"]
    sig_a = q54["sig_A"]
    sig_b = q54["sig_B"]
    h4b_pass = rank_b == 114
    print(f"  H4b: Q 54 rank_B = {rank_b}/114; sig_B = {sig_b:.3f}; pass (==114): {h4b_pass}")
    print(f"        Q 54 rank_A = {rank_a}/114; sig_A = {sig_a:.3f}")

    # H4c: corpus-share of top_final_letter_frac == 1.0 surahs
    perfect_monorhymes = []
    near_monorhymes = []
    for s_id, entry in per_surah.items():
        if entry["top_final_letter_frac"] == 1.0:
            perfect_monorhymes.append({"surah": s_id, "top_letter": entry["top_final_letter"], "n_verses": entry["n_verses"]})
        if entry["top_final_letter_frac"] >= 0.99:
            near_monorhymes.append({"surah": s_id, "top_letter": entry["top_final_letter"], "frac": entry["top_final_letter_frac"], "n_verses": entry["n_verses"]})
    print(f"  H4c: corpus surahs with perfect (==1.0) monorhyme: {len(perfect_monorhymes)}")
    for pm in perfect_monorhymes:
        print(f"    Q{pm['surah']:3d} on '{pm['top_letter']}' ({pm['n_verses']} verses)")
    print(f"  H4c: corpus surahs with near-perfect (≥0.99) monorhyme: {len(near_monorhymes)}")
    for nm in sorted(near_monorhymes, key=lambda x: -x["frac"]):
        print(f"    Q{nm['surah']:3d} '{nm['top_letter']}' frac={nm['frac']:.4f} ({nm['n_verses']} verses)")
    h4c_pass = len(perfect_monorhymes) <= 3

    # Sub-claim: Q 54 is corpus-uniquely-perfect-monorhyme among surahs with ≥ 50 verses
    perfect_with_50plus = [pm for pm in perfect_monorhymes if pm["n_verses"] >= 50]
    is_unique_among_long = (len(perfect_with_50plus) == 1) and (perfect_with_50plus[0]["surah"] == 54)
    print(f"  Sub-claim: perfect-monorhyme surahs with ≥50 verses: {len(perfect_with_50plus)}; Q 54 uniquely-such: {is_unique_among_long}")

    # MW-5 positive control: shuffle Q 54 verse-final-letters and verify monorhyme breaks
    import random
    rng = random.Random(20260509)
    q54_verses = corpus[53]["verses"]

    def get_final_letter(text: str) -> str:
        cleaned = ''.join(c for c in text.rstrip() if c.isalpha() or c in "ابتثجحخدذرزسشصضطظعغفقكلمنهويءأإآةىئؤ")
        return cleaned[-1] if cleaned else ""

    actual_finals = [get_final_letter(v["text"]) for v in q54_verses]
    # Build pool of corpus letter-frequencies for verse-finals
    pool = []
    for s in corpus:
        for v in s["verses"]:
            f = get_final_letter(v["text"])
            if f:
                pool.append(f)
    n_v = len(actual_finals)
    n_q54_perfect_under_null = 0
    N_PERM_MW5 = 10000
    for _ in range(N_PERM_MW5):
        sampled = rng.choices(pool, k=n_v)
        from collections import Counter
        c = Counter(sampled)
        most_common_n = c.most_common(1)[0][1]
        if most_common_n == n_v:
            n_q54_perfect_under_null += 1
    perm_p_perfect = n_q54_perfect_under_null / N_PERM_MW5
    print(f"  MW-5 positive control: under shuffled-final null, Q 54-length perfect-monorhyme prob = {perm_p_perfect:.5f}")
    print(f"    (low p means observed 100% monorhyme is corpus-extreme)")

    # Aggregate
    n_passed = sum([h4a_pass, h4b_pass])
    if n_passed == 2:
        verdict = "CONFIRMED"
    elif n_passed == 1:
        verdict = "PARTIAL"
    else:
        verdict = "NULL"
    print(f"  Aggregate: {n_passed}/2 → {verdict}")

    output = {
        "test_id": "Q054-F-04",
        "title": "Q 54 100% ر-monorhyme corpus-uniqueness",
        "prereg_sha256": sha,
        "H4a": {
            "top_final_letter": top_letter,
            "top_final_letter_frac": frac_q54,
            "rhyme_entropy_nats": rhyme_entropy,
            "pass": h4a_pass,
        },
        "H4b": {
            "rank_A": rank_a,
            "rank_B": rank_b,
            "sig_A": sig_a,
            "sig_B": sig_b,
            "pass": h4b_pass,
        },
        "H4c": {
            "n_perfect_monorhyme_surahs": len(perfect_monorhymes),
            "perfect_monorhyme_surahs": perfect_monorhymes,
            "n_near_monorhyme_surahs": len(near_monorhymes),
            "near_monorhyme_surahs": sorted(near_monorhymes, key=lambda x: -x["frac"]),
            "pass": h4c_pass,
        },
        "Q54_unique_long_surah_perfect_monorhyme": is_unique_among_long,
        "Q54_perfect_monorhyme_50plus_companions": perfect_with_50plus,
        "MW5_positive_control": {
            "n_perm": N_PERM_MW5,
            "perm_p_perfect_monorhyme_under_shuffle": perm_p_perfect,
        },
        "aggregate": {"n_passed": n_passed, "verdict": verdict},
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  Output: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
