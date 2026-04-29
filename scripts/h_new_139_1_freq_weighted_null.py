#!/usr/bin/env python3
"""H-NEW-139.1 — Frequency-weighted null replication of H-NEW-139.

audit-037 flagged: H-NEW-139's uniform-over-28-alphabet null overstates the
effect-size because fāṣila-letter distribution is NON-uniform (ن alone is 50%).

Re-run with frequency-weighted null: letters drawn with probability
proportional to their global fāṣila-frequency (over all 6,236 verses).

Pre-reg: findings/phase-b-hypotheses/h-new-139-1-prereg.md
Seed: 20260417 (+ 2 offset for RNG stream separation)
"""

from __future__ import annotations

import json
import random
import re
from collections import Counter
from math import sqrt
from pathlib import Path

SEED = 20260417
N_PERMS = 10_000
PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
QURAN_JSON = PROJECT_ROOT / "quran-text/quran-no-tashkeel.json"
OUTPUT = PROJECT_ROOT / "findings/phase-b-hypotheses/csv/h-new-139-1.json"
PREREG = PROJECT_ROOT / "findings/phase-b-hypotheses/h-new-139-1-prereg.md"

MUQ_OPENINGS = {
    2: "الم", 3: "الم", 7: "المص", 10: "الر", 11: "الر", 12: "الر",
    13: "المر", 14: "الر", 15: "الر", 19: "كهيعص", 20: "طه",
    26: "طسم", 27: "طس", 28: "طسم", 29: "الم", 30: "الم", 31: "الم",
    32: "الم", 36: "يس", 38: "ص", 40: "حم", 41: "حم", 42: "حمعسق",
    43: "حم", 44: "حم", 45: "حم", 46: "حم", 50: "ق", 68: "ن",
}

# Strip marks regex (from h-new-143 script)
STRIP_RE = re.compile(
    r"[\u06D6-\u06DF\u0610-\u061A\u0615-\u061A\u064B-\u065F\u0670"
    r"\u06D4-\u06E8\u06EA-\u06ED\u200F\u200E\s]+"
)
PUNCT_RE = re.compile(r"[.,?!;:،؛؟ۖۗۚۛۘۙۜ]+")


def final_letter(text: str) -> str | None:
    text = STRIP_RE.sub("", text)
    text = PUNCT_RE.sub("", text)
    if not text:
        return None
    return text[-1]


def main() -> None:
    with QURAN_JSON.open() as f:
        data = json.load(f)
    surahs = {s["id"]: s for s in data}

    # 1. Global fāṣila frequency
    global_freq: Counter[str] = Counter()
    for s in surahs.values():
        for v in s["verses"]:
            lf = final_letter(v["text"])
            if lf:
                global_freq[lf] += 1
    total_fasila = sum(global_freq.values())

    # 2. Per-surah TOP-3 verse-final letters (excluding v1)
    surah_top3: dict[int, list[str]] = {}
    for s_id in MUQ_OPENINGS:
        freq: Counter[str] = Counter()
        for v in surahs[s_id]["verses"]:
            if v["id"] == 1:
                continue
            lf = final_letter(v["text"])
            if lf:
                freq[lf] += 1
        surah_top3[s_id] = [letter for letter, _ in freq.most_common(3)]

    # 3. Observed match count
    observed = 0
    per_surah_observed = {}
    for s_id in sorted(MUQ_OPENINGS):
        opening = set(MUQ_OPENINGS[s_id])
        top3 = set(surah_top3[s_id])
        match = 1 if (opening & top3) else 0
        observed += match
        per_surah_observed[s_id] = {
            "opening": MUQ_OPENINGS[s_id],
            "opening_size": len(opening),
            "top3": surah_top3[s_id],
            "overlap": sorted(list(opening & top3)),
            "match": match,
        }

    # 4. Frequency-weighted null
    # Pre-committed method: weighted-independent-with-renormalization
    # For each surah, draw k_s letters independently with probability proportional
    # to global_freq, rejecting duplicates until we have k_s distinct letters.
    letters = list(global_freq.keys())
    weights = [global_freq[l] / total_fasila for l in letters]

    rng = random.Random(SEED + 2)

    def weighted_sample_without_replacement(k: int) -> set[str]:
        chosen: set[str] = set()
        # Weighted-reservoir: sort by -ln(U)/w keys
        import math
        keys = [(-math.log(rng.random()) / w if w > 0 else float("inf"), letter)
                for letter, w in zip(letters, weights)]
        keys.sort()
        return set(letter for _, letter in keys[:k])

    null_match_counts: list[int] = []
    for _ in range(N_PERMS):
        total = 0
        for s_id in MUQ_OPENINGS:
            k = len(set(MUQ_OPENINGS[s_id]))
            drawn = weighted_sample_without_replacement(k)
            top3 = set(surah_top3[s_id])
            if drawn & top3:
                total += 1
        null_match_counts.append(total)

    null_mean = sum(null_match_counts) / N_PERMS
    null_var = sum((c - null_mean) ** 2 for c in null_match_counts) / N_PERMS
    null_sd = sqrt(null_var)
    null_max = max(null_match_counts)
    null_min = min(null_match_counts)
    z = (observed - null_mean) / null_sd if null_sd > 0 else float("inf")
    n_ge = sum(1 for c in null_match_counts if c >= observed)
    p_upper = (n_ge + 1) / (N_PERMS + 1)

    # Per-surah null match probability (descriptive secondary)
    per_surah_null_prob = {}
    for s_id in MUQ_OPENINGS:
        k = len(set(MUQ_OPENINGS[s_id]))
        top3_set = set(surah_top3[s_id])
        # estimate via monte carlo
        hits = 0
        for _ in range(2000):
            drawn = weighted_sample_without_replacement(k)
            if drawn & top3_set:
                hits += 1
        per_surah_null_prob[s_id] = hits / 2000

    # Verdict
    primary_pass = p_upper < 0.05
    verdict = "PASS (survives frequency-weighted null)" if primary_pass else "NULL (fails under frequency-weighted null)"

    # Output
    output = {
        "finding_id": "h-new-139-1",
        "title": "H-NEW-139 frequency-weighted null replication",
        "pre_reg_path": str(PREREG),
        "parent_finding": "h-new-139",
        "audit_flag_source": "audit-037",
        "seed": SEED,
        "n_perms": N_PERMS,
        "global_fasila_frequency_top10": dict(global_freq.most_common(10)),
        "global_fasila_total_verses": total_fasila,
        "per_surah_observed": per_surah_observed,
        "per_surah_null_match_prob_freq_weighted": per_surah_null_prob,
        "observed_match_count": observed,
        "null_distribution": {
            "mean": null_mean,
            "sd": null_sd,
            "min": null_min,
            "max": null_max,
        },
        "primary": {
            "observed": observed,
            "null_mean": null_mean,
            "null_sd": null_sd,
            "z_score": z,
            "p_one_sided_upper": p_upper,
            "alpha_bon": 0.05,
            "pass_primary": primary_pass,
            "verdict": verdict,
        },
        "comparison_to_parent": {
            "parent_uniform_null_z": 5.96,
            "parent_uniform_null_p": "< 0.0001",
            "weighted_null_z": z,
            "weighted_null_p": p_upper,
            "z_difference_uniform_minus_weighted": 5.96 - z,
        },
    }

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT.open("w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print("=" * 70)
    print("H-NEW-139.1 — Frequency-weighted null replication")
    print("=" * 70)
    print(f"Observed match count: {observed} / 29")
    print(f"Weighted-null mean: {null_mean:.3f} ± {null_sd:.3f}")
    print(f"Null range: [{null_min}, {null_max}]")
    print(f"z-score: {z:+.3f}")
    print(f"p_one_sided_upper: {p_upper:.5f}")
    print(f"Pass α=0.05 single-test: {primary_pass}")
    print()
    print(f"Comparison to parent H-NEW-139:")
    print(f"  Parent (uniform null): z = +5.96, p < 0.0001")
    print(f"  This (weighted null):  z = {z:+.3f}, p = {p_upper:.5f}")
    print(f"  z dropped by: {5.96 - z:.2f}")
    print()
    print(f"VERDICT: {verdict}")
    print(f"Output: {OUTPUT}")


if __name__ == "__main__":
    main()
