#!/usr/bin/env python3
"""H-NEW-1320 — Refrain-saturation corpus-rank.

Pre-reg: findings/phase-b-hypotheses/h-new-1320-refrain-saturation-corpus-rank-prereg.md
SHA256:  abc1630142b86b70f7bdec1edc51b2d17c7987d5e776e6bb6d8da069590abec4
"""

import hashlib
import json
import random
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from statistics import mean

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-1320-refrain-saturation-corpus-rank-prereg.md"
EXPECTED_SHA = "abc1630142b86b70f7bdec1edc51b2d17c7987d5e776e6bb6d8da069590abec4"
QURAN = ROOT / "quran-text/quran-no-tashkeel.json"
OUT = ROOT / "findings/phase-b-hypotheses/csv/h-new-1320.json"
SEED = 20260509
N_PERM = 10_000


def verify_prereg() -> None:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual}")
    print(f"pre-reg SHA verified: {EXPECTED_SHA[:12]}…")


def normalize(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    s = " ".join(s.split())
    return s


def main() -> None:
    verify_prereg()
    text = json.loads(QURAN.read_text())
    verses_per_surah: dict[int, list[str]] = {}
    for entry in text:
        s = int(entry["id"])
        verses_per_surah[s] = [normalize(v["text"]) for v in entry["verses"]]

    # Statistic
    per_surah_max = {s: max(Counter(vs).values()) if vs else 0 for s, vs in verses_per_surah.items()}
    per_surah_top_string = {s: Counter(vs).most_common(1)[0] if vs else ("", 0) for s, vs in verses_per_surah.items()}

    ranking = sorted(range(1, 115), key=lambda s: (-per_surah_max[s], s))
    rank_q55 = ranking.index(55) + 1
    rank_q26 = ranking.index(26) + 1
    rank_q77 = ranking.index(77) + 1
    obs_q55 = per_surah_max[55]

    # Permutation null
    rng = random.Random(SEED)
    all_verses: list[str] = []
    for s in range(1, 115):
        all_verses.extend(verses_per_surah[s])
    counts_per_surah = [(s, len(verses_per_surah[s])) for s in range(1, 115)]

    perm_max_overall: list[int] = []
    perm_q55_max: list[int] = []
    pool = all_verses.copy()
    for _ in range(N_PERM):
        rng.shuffle(pool)
        idx = 0
        per_surah_perm: dict[int, int] = {}
        for s, n_s in counts_per_surah:
            chunk = pool[idx : idx + n_s]
            idx += n_s
            per_surah_perm[s] = max(Counter(chunk).values()) if chunk else 0
        perm_max_overall.append(max(per_surah_perm.values()))
        perm_q55_max.append(per_surah_perm[55])

    p_perm_max = sum(1 for x in perm_max_overall if x >= obs_q55) / N_PERM
    p_perm_q55 = sum(1 for x in perm_q55_max if x >= obs_q55) / N_PERM

    # MW-5 instrument-control: the null mean-max should be ~1-2 (random shuffle ⇒ most verses unique)
    pc_null_mean = mean(perm_max_overall)
    pc_pass = pc_null_mean < 5  # extremely loose threshold; under random shuffle expect ~1-2

    cell_a_rank_pass = rank_q55 == 1
    cell_a_perm_pass = p_perm_max <= 0.025
    cell_a_pass = cell_a_rank_pass and cell_a_perm_pass

    cell_b_q26 = rank_q26 <= 5
    cell_b_q77 = rank_q77 <= 5
    cell_b_pass = cell_b_q26 and cell_b_q77
    cell_b_partial = cell_b_q26 or cell_b_q77

    if not pc_pass:
        verdict = "NULL-BROKEN (instrument-control failed)"
    elif cell_a_pass and cell_b_pass:
        verdict = "PASS-DIRECTED FULL"
    elif cell_a_pass and cell_b_partial:
        verdict = "PASS-DIRECTED CELL-A only (Cell B partial)"
    elif cell_a_pass:
        verdict = "PASS-DIRECTED CELL-A only"
    elif cell_b_pass:
        verdict = "PARTIAL (Cell B only)"
    elif cell_b_partial:
        verdict = "PARTIAL (Cell B 1-of-2)"
    else:
        verdict = "NULL"

    out = {
        "id": "H-NEW-1320",
        "title": "Refrain-saturation corpus-rank — Q 55 strict rank-1 + Q 26/Q 77 top-5",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "obs_q55_max_repeat_count": obs_q55,
        "rank_q55_of_114": rank_q55,
        "rank_q26": rank_q26,
        "rank_q77": rank_q77,
        "top_15_ranking": [
            {
                "rank": i + 1,
                "surah": s,
                "max_repeat_count": per_surah_max[s],
                "top_repeat_string": per_surah_top_string[s][0][:80],
                "n_verses": len(verses_per_surah[s]),
                "saturation": per_surah_max[s] / len(verses_per_surah[s]) if verses_per_surah[s] else 0,
            }
            for i, s in enumerate(ranking[:15])
        ],
        "cell_A_strict_rank": {
            "obs_q55": obs_q55,
            "rank_q55": rank_q55,
            "rank_pass_strict_1": cell_a_rank_pass,
        },
        "cell_A_permutation_null": {
            "p_perm_any_surah_ge_obs": p_perm_max,
            "p_perm_q55_ge_obs": p_perm_q55,
            "perm_max_overall_mean": mean(perm_max_overall),
            "perm_q55_mean": mean(perm_q55_max),
            "perm_pass": cell_a_perm_pass,
        },
        "cell_B_q26_q77_top5": {
            "q26_rank": rank_q26,
            "q77_rank": rank_q77,
            "q26_top5": cell_b_q26,
            "q77_top5": cell_b_q77,
            "pass_full": cell_b_pass,
            "partial": cell_b_partial,
        },
        "MW5_instrument_control": {
            "null_mean_max_overall": pc_null_mean,
            "pc_pass": pc_pass,
        },
        "verdict": verdict,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nVerdict: {verdict}")
    print(f"Q 55 max_repeat_count = {obs_q55}; rank = {rank_q55}/114")
    print(f"Q 26 rank = {rank_q26}; Q 77 rank = {rank_q77}")
    print("\nTop-15 by max_repeat_count:")
    for r in out["top_15_ranking"]:
        print(f"  #{r['rank']}: Q {r['surah']:>3}  count={r['max_repeat_count']:>2}  saturation={r['saturation']:.3f}  '{r['top_repeat_string'][:60]}'")
    print(f"\nCell A perm null: p_max_overall={p_perm_max:.5f}  p_q55={p_perm_q55:.5f}  null_mean_max={pc_null_mean:.3f}")
    print(f"Wrote: {OUT}")


if __name__ == "__main__":
    main()
