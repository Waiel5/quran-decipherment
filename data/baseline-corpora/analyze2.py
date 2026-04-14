#!/usr/bin/env python3
"""
Second-pass tests:
  - Letter-frequency Quran-vs-baseline z-tests
  - Test 3: divisibility-by-19 in opening letter frequencies
  - Test 1 follow-up: confirm McKay-style denominator at root level
  - Comparable-size matched corpus assembly (~77800 tokens)
"""
from __future__ import annotations

import csv
import json
import math
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from analyze import (
    basic_stats, load_quran_text, normalize, tokenize, letter_freqs,
    is_arabic_letter, ARABIC_LETTERS, RAW, OUT
)

QURAN_BIG_LETTERS = ["ا", "ل", "م", "ن", "ر", "ك", "ه", "ع", "ص", "ط",
                      "ي", "ح", "ق", "س"]


def load_letter_freqs(name: str, text: str) -> tuple[dict[str, int], int]:
    """Return (per-letter counts, total letters)."""
    norm = normalize(text)
    lf = letter_freqs(norm)
    return lf, sum(lf.values())


def two_proportion_z(p1: float, n1: int, p2: float, n2: int) -> float:
    """Two-proportion z-test."""
    if n1 == 0 or n2 == 0:
        return float("nan")
    p = (p1 * n1 + p2 * n2) / (n1 + n2)
    se = math.sqrt(p * (1 - p) * (1 / n1 + 1 / n2))
    if se == 0:
        return 0.0
    return (p1 - p2) / se


def divisibility_19_score(letter_counts: dict[str, int]) -> dict:
    """For each Arabic letter, compute count and (count mod 19).
    Return a summary: how many letters have count divisible by 19,
    and what fraction is that.
    A 'random' letter-frequency vector should have ~1/19 of its
    entries divisible by 19 in expectation."""
    n = len(letter_counts)
    div = sum(1 for c in letter_counts.values() if c > 0 and c % 19 == 0)
    return {
        "n_letters": n,
        "n_div_19": div,
        "frac": div / n if n else 0.0,
        "expected_random": 1 / 19,
    }


def main():
    # ---------- Quran ----------
    q_text = load_quran_text()
    q_norm = normalize(q_text)
    q_lf = letter_freqs(q_norm)
    q_total = sum(q_lf.values())
    print(f"Quran letters: {q_total}")

    # ---------- baseline letter-frequency comparison ----------
    files = sorted(p for p in RAW.glob("*.txt") if "raw.txt" not in p.name)
    rows = []
    for f in files:
        text = f.read_text(encoding="utf-8")
        lf, total = load_letter_freqs(f.stem, text)
        rows.append((f.stem, lf, total))

    # Compute Quran-vs-merged-baseline two-proportion z for each letter
    merged_lf: Counter[str] = Counter()
    merged_total = 0
    for name, lf, tot in rows:
        # Drop the tiny per-Mu'allaqa files (we have full diwans)
        # but keep them too — they're real Arabic. We just merge ALL.
        for k, v in lf.items():
            merged_lf[k] += v
        merged_total += tot

    print(f"Merged baseline letters: {merged_total}")
    all_letters = sorted(set(q_lf) | set(merged_lf))
    out_path = OUT / "letter-z-tests.csv"
    with out_path.open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["letter", "quran_count", "quran_p", "baseline_count", "baseline_p",
                    "delta_pct", "z"])
        for L in all_letters:
            qc = q_lf.get(L, 0)
            bc = merged_lf.get(L, 0)
            qp = qc / q_total if q_total else 0
            bp = bc / merged_total if merged_total else 0
            z = two_proportion_z(qp, q_total, bp, merged_total)
            w.writerow([L, qc, round(qp, 5), bc, round(bp, 5),
                        round((qp - bp) * 100, 4), round(z, 2)])

    # Print top 10 strongest deviations
    print("\nTop 10 letters by |z| (Quran vs merged baseline):")
    devs = []
    for L in all_letters:
        qc = q_lf.get(L, 0)
        bc = merged_lf.get(L, 0)
        if qc + bc < 100:
            continue
        qp = qc / q_total
        bp = bc / merged_total
        z = two_proportion_z(qp, q_total, bp, merged_total)
        devs.append((abs(z), z, L, qp, bp))
    devs.sort(reverse=True)
    for _, z, L, qp, bp in devs[:15]:
        print(f"  {L}: q={qp*100:.3f}% base={bp*100:.3f}% z={z:+.1f}")

    # ---------- Test 3: divisibility by 19 in letter frequencies ----------
    print("\n=== Critical Test 3: divisibility-by-19 in letter freqs ===")
    div19_rows = [("quran-no-tashkeel", divisibility_19_score(q_lf))]
    for name, lf, tot in rows:
        div19_rows.append((name, divisibility_19_score(lf)))
    print(f"  expected (random): 1/19 ≈ {1/19:.4f}")
    for name, d in div19_rows:
        if d["n_letters"] >= 25:
            print(f"  {name}: {d['n_div_19']}/{d['n_letters']} = {d['frac']:.4f}")
    with (OUT / "test3-div19.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["name", "n_letters", "n_div_19", "frac", "expected"])
        for name, d in div19_rows:
            w.writerow([name, d["n_letters"], d["n_div_19"], round(d["frac"], 4),
                        round(1/19, 4)])

    # ---------- Comparable-size assembly: ~77800 tokens ----------
    target = 77797
    # Use Bukhari first, truncate to target
    bukhari_text = (RAW / "bukhari.txt").read_text(encoding="utf-8")
    bukhari_tokens = tokenize(normalize(bukhari_text))
    matched_tokens = bukhari_tokens[:target]
    matched_text = " ".join(matched_tokens)
    out_matched = RAW / "matched-bukhari-77k.txt"
    out_matched.write_text(matched_text, encoding="utf-8")
    print(f"\nMatched-size Bukhari corpus: {len(matched_tokens)} tokens, "
          f"saved {out_matched.name}")

    # Stats
    matched_lf = letter_freqs(matched_text)
    matched_total = sum(matched_lf.values())
    print(f"  letters: {matched_total}")
    print(f"  vocab: {len(set(matched_tokens))}")
    print(f"  Quran letters: {q_total}, ratio: {matched_total/q_total:.3f}")

    # Letter-by-letter comparison Quran vs matched-Bukhari
    print("\nQuran vs matched-Bukhari letter freq deltas (top 12 by |z|):")
    devs2 = []
    for L in sorted(set(q_lf) | set(matched_lf)):
        qc = q_lf.get(L, 0); bc = matched_lf.get(L, 0)
        if qc + bc < 50:
            continue
        qp = qc / q_total; bp = bc / matched_total
        z = two_proportion_z(qp, q_total, bp, matched_total)
        devs2.append((abs(z), z, L, qp, bp, qc, bc))
    devs2.sort(reverse=True)
    for _, z, L, qp, bp, qc, bc in devs2[:12]:
        print(f"  {L}: q={qc} ({qp*100:.2f}%) bk={bc} ({bp*100:.2f}%) z={z:+.1f}")

    # Save matched-comparison CSV
    with (OUT / "letter-z-quran-vs-matched-bukhari.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["letter", "quran_count", "quran_p", "matched_bukhari_count",
                    "matched_bukhari_p", "delta_pct", "z"])
        for L in sorted(set(q_lf) | set(matched_lf)):
            qc = q_lf.get(L, 0); bc = matched_lf.get(L, 0)
            qp = qc / q_total if q_total else 0
            bp = bc / matched_total if matched_total else 0
            z = two_proportion_z(qp, q_total, bp, matched_total)
            w.writerow([L, qc, round(qp, 5), bc, round(bp, 5),
                        round((qp - bp) * 100, 4), round(z, 2)])


if __name__ == "__main__":
    main()
