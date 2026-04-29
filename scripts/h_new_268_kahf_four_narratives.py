#!/usr/bin/env python3
"""H-NEW-268 — Q18 Al-Kahf four-narrative structural spacing test.

Exact ordered-placement null over all placements of four fixed-length
blocks (18, 13, 23, 16) inside a 110-verse surah.

Bonferroni-3 cells:
  A. d1 == d3
  B. d2 > max(d1, d3)
  C. d1 == d3 < d2

MW-5 positive control:
  planted gaps (0, 5, 35, 0, 0) -> starts (1, 24, 72, 95) -> gaps
  (23, 48, 23)
"""

from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path("/Users/grey/Downloads/quran")
QTEXT = ROOT / "quran-text" / "quran-no-tashkeel.json"
PREREG = ROOT / "findings" / "phase-b-hypotheses" / "h-new-268-kahf-four-narratives-prereg.md"
ATLAS = ROOT / "findings" / "verse-signature-atlas.csv"
OUT = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-268.json"

SURAH_ID = 18
SURAH_VERSES = 110
BLOCKS = [
    {"name": "sleepers", "start": 9, "end": 26},
    {"name": "gardens", "start": 32, "end": 44},
    {"name": "moses_khidr", "start": 60, "end": 82},
    {"name": "dhul_qarnayn", "start": 83, "end": 98},
]
ALPHA = 0.05
BONFERRONI_K = 3
ALPHA_BON = ALPHA / BONFERRONI_K
MW5_GAPS = (0, 5, 35, 0, 0)


def load_surah_verse_count() -> int:
    with QTEXT.open(encoding="utf-8") as f:
        data = json.load(f)
    surah = next(item for item in data if item["id"] == SURAH_ID)
    return len(surah["verses"])


def load_word_letter_totals() -> dict[str, dict[str, int | float]]:
    by_block = {}
    with ATLAS.open(encoding="utf-8") as f:
        rows = [row for row in csv.DictReader(f) if int(row["surah"]) == SURAH_ID]
    for block in BLOCKS:
        rows_block = [
            row for row in rows
            if block["start"] <= int(row["verse"]) <= block["end"]
        ]
        word_total = sum(int(row["length_words"]) for row in rows_block)
        letter_total = sum(int(row["length_letters"]) for row in rows_block)
        by_block[block["name"]] = {
            "words": word_total,
            "letters": letter_total,
        }
    return by_block


def enrich_blocks() -> list[dict[str, int | str]]:
    totals = load_word_letter_totals()
    enriched = []
    for block in BLOCKS:
        length = block["end"] - block["start"] + 1
        enriched.append(
            {
                "name": block["name"],
                "start": block["start"],
                "end": block["end"],
                "length_verses": length,
                "length_words": totals[block["name"]]["words"],
                "length_letters": totals[block["name"]]["letters"],
            }
        )
    return enriched


def block_lengths() -> list[int]:
    return [block["end"] - block["start"] + 1 for block in BLOCKS]


def gap_slots_from_ranges() -> list[int]:
    starts = [block["start"] for block in BLOCKS]
    ends = [block["end"] for block in BLOCKS]
    return [
        starts[0] - 1,
        starts[1] - ends[0] - 1,
        starts[2] - ends[1] - 1,
        starts[3] - ends[2] - 1,
        SURAH_VERSES - ends[3],
    ]


def starts_from_gaps(gaps: tuple[int, int, int, int, int], lengths: list[int]) -> tuple[int, int, int, int]:
    g0, g1, g2, g3, _ = gaps
    s1 = 1 + g0
    s2 = s1 + lengths[0] + g1
    s3 = s2 + lengths[1] + g2
    s4 = s3 + lengths[2] + g3
    return (s1, s2, s3, s4)


def start_gaps(starts: tuple[int, int, int, int]) -> tuple[int, int, int]:
    return (
        starts[1] - starts[0],
        starts[2] - starts[1],
        starts[3] - starts[2],
    )


def cell_a(gap_tuple: tuple[int, int, int]) -> bool:
    d1, _, d3 = gap_tuple
    return d1 == d3


def cell_b(gap_tuple: tuple[int, int, int]) -> bool:
    d1, d2, d3 = gap_tuple
    return d2 > max(d1, d3)


def cell_c(gap_tuple: tuple[int, int, int]) -> bool:
    d1, d2, d3 = gap_tuple
    return d1 == d3 and d2 > d1


def enumerate_placements(lengths: list[int]) -> dict[str, object]:
    residual = SURAH_VERSES - sum(lengths)
    total = 0
    count_a = 0
    count_b = 0
    count_c = 0
    tuple_counter: Counter[tuple[int, int, int]] = Counter()
    outer_diff_sum = 0
    middle_gap_sum = 0

    for g0 in range(residual + 1):
        for g1 in range(residual - g0 + 1):
            for g2 in range(residual - g0 - g1 + 1):
                for g3 in range(residual - g0 - g1 - g2 + 1):
                    g4 = residual - g0 - g1 - g2 - g3
                    gaps = (g0, g1, g2, g3, g4)
                    starts = starts_from_gaps(gaps, lengths)
                    gap_tuple = start_gaps(starts)
                    total += 1
                    tuple_counter[gap_tuple] += 1
                    outer_diff_sum += abs(gap_tuple[0] - gap_tuple[2])
                    middle_gap_sum += gap_tuple[1]
                    if cell_a(gap_tuple):
                        count_a += 1
                    if cell_b(gap_tuple):
                        count_b += 1
                    if cell_c(gap_tuple):
                        count_c += 1

    return {
        "residual_gap_verses": residual,
        "total_placements": total,
        "count_a": count_a,
        "count_b": count_b,
        "count_c": count_c,
        "tuple_counter": tuple_counter,
        "outer_diff_mean": outer_diff_sum / total,
        "middle_gap_mean": middle_gap_sum / total,
    }


def verdict_from_passes(pass_count: int) -> str:
    if pass_count == 0:
        return "NULL"
    if pass_count == 1:
        return "DIMENSION-SPECIFIC"
    if pass_count == 2:
        return "PASS-DIRECTED"
    return "STRONG PASS"


def exact_probability(count: int, total: int) -> float:
    return count / total if total else 0.0


def main() -> None:
    prereg_sha = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    q18_count = load_surah_verse_count()
    assert q18_count == SURAH_VERSES, f"Expected {SURAH_VERSES} verses, found {q18_count}"

    blocks = enrich_blocks()
    lengths = [int(block["length_verses"]) for block in blocks]
    observed_gap_slots = gap_slots_from_ranges()
    observed_starts = tuple(int(block["start"]) for block in blocks)
    observed_tuple = start_gaps(observed_starts)

    enum = enumerate_placements(lengths)
    total = int(enum["total_placements"])
    tuple_counter = enum["tuple_counter"]

    p_a = exact_probability(int(enum["count_a"]), total)
    p_b = exact_probability(int(enum["count_b"]), total)
    p_c = exact_probability(int(enum["count_c"]), total)

    pass_a = p_a < ALPHA_BON
    pass_b = p_b < ALPHA_BON
    pass_c = p_c < ALPHA_BON
    pass_count = sum([pass_a, pass_b, pass_c])

    mw5_starts = starts_from_gaps(MW5_GAPS, lengths)
    mw5_tuple = start_gaps(mw5_starts)

    result = {
        "id": "H-NEW-268",
        "title": "Q18 Al-Kahf four-narrative structural spacing test",
        "prereg_sha256": prereg_sha,
        "surah": SURAH_ID,
        "surah_verse_count": SURAH_VERSES,
        "rules_tuple": "(Q18 only; 110 verses; four locked narrative blocks 9-26 / 32-44 / 60-82 / 83-98; ordered-placement exact null with fixed lengths 18/13/23/16)",
        "bonferroni_k": BONFERRONI_K,
        "alpha": ALPHA,
        "alpha_bon": ALPHA_BON,
        "blocks": blocks,
        "observed": {
            "gap_slots": observed_gap_slots,
            "starts": list(observed_starts),
            "start_gap_tuple": list(observed_tuple),
            "outer_gap_difference": abs(observed_tuple[0] - observed_tuple[2]),
            "middle_gap": observed_tuple[1],
            "exact_tuple_count": int(tuple_counter[observed_tuple]),
            "exact_tuple_probability": exact_probability(int(tuple_counter[observed_tuple]), total),
            "cells": {
                "A_outer_equal": {
                    "observed": cell_a(observed_tuple),
                    "p_exact": p_a,
                    "pass_bonferroni": pass_a,
                },
                "B_middle_widest": {
                    "observed": cell_b(observed_tuple),
                    "p_exact": p_b,
                    "pass_bonferroni": pass_b,
                },
                "C_joint_palindromic_expansion": {
                    "observed": cell_c(observed_tuple),
                    "p_exact": p_c,
                    "pass_bonferroni": pass_c,
                },
            },
        },
        "null": {
            "residual_gap_verses": int(enum["residual_gap_verses"]),
            "total_placements": total,
            "outer_gap_difference_mean": enum["outer_diff_mean"],
            "middle_gap_mean": enum["middle_gap_mean"],
            "cell_counts": {
                "A_outer_equal": int(enum["count_a"]),
                "B_middle_widest": int(enum["count_b"]),
                "C_joint_palindromic_expansion": int(enum["count_c"]),
            },
        },
        "mw5": {
            "description": "Planted symmetric arrangement with maximal central expansion under zero outer padding.",
            "gap_slots": list(MW5_GAPS),
            "starts": list(mw5_starts),
            "start_gap_tuple": list(mw5_tuple),
            "exact_tuple_count": int(tuple_counter[mw5_tuple]),
            "exact_tuple_probability": exact_probability(int(tuple_counter[mw5_tuple]), total),
            "cells": {
                "A_outer_equal": cell_a(mw5_tuple),
                "B_middle_widest": cell_b(mw5_tuple),
                "C_joint_palindromic_expansion": cell_c(mw5_tuple),
            },
        },
        "verdict": verdict_from_passes(pass_count),
        "verdict_reason": (
            f"{pass_count}/3 Bonferroni cells passed. "
            "This is a spacing-geometry result only; it does not establish lexical or thematic symmetry."
        ),
    }

    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"prereg SHA-256: {prereg_sha}")
    print(f"Observed start-gap tuple: {observed_tuple}")
    print(f"Cell A p_exact={p_a:.6f} pass={pass_a}")
    print(f"Cell B p_exact={p_b:.6f} pass={pass_b}")
    print(f"Cell C p_exact={p_c:.6f} pass={pass_c}")
    print(f"Observed exact tuple probability={result['observed']['exact_tuple_probability']:.6f}")
    print(f"MW-5 tuple={mw5_tuple}, exact tuple probability={result['mw5']['exact_tuple_probability']:.8f}")
    print(f"Verdict: {result['verdict']}")


if __name__ == "__main__":
    main()
