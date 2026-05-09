#!/usr/bin/env python3
"""H-NEW-1350 — Allāh-token corpus-wide per-verse coverage distribution
and Medinan/Meccan separation (one-sided Mann-Whitney + label-permutation null).

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-1350-allah-density-corpus.md
SHA256:  b41ee6b93e09a1ab25655a50edb4ad0f6e14198e4a7a12f34d2e8b6a90bd434f

Rules-tuple: (no-tashkeel, orthographic-token, substring الله, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""

import csv
import hashlib
import json
import os
import random
import re
import sys
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/prereg-h-new-1350-allah-density-corpus.md"
EXPECTED_SHA = "b41ee6b93e09a1ab25655a50edb4ad0f6e14198e4a7a12f34d2e8b6a90bd434f"
QURAN_PATH = ROOT / "quran-text/quran-no-tashkeel.json"
CHRONOLOGY_PATH = ROOT / "data/revelation-order.csv"
OUT_PATH = ROOT / "findings/phase-b-hypotheses/csv/h-new-1350.json"

SEED = 20260509
N_PERM = 10000
ALLAH_PATTERN = re.compile(r"الله")


def verify_sha() -> None:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH:\n  expected={EXPECTED_SHA}\n  actual  ={actual}")
    print(f"pre-reg SHA verified: {EXPECTED_SHA[:16]}…")


def load_chronology() -> dict[int, str]:
    """Return {mushaf_order: period} where period ∈ {'Meccan','Medinan'}."""
    period: dict[int, str] = {}
    with CHRONOLOGY_PATH.open() as f:
        for row in csv.DictReader(f):
            sid = int(row["mushaf_order"])
            period[sid] = row["period"].strip()
    return period


def mann_whitney_u(x: list[float], y: list[float]) -> float:
    """Mann-Whitney U for x vs y. Returns U_x (the statistic for 'x > y' direction).

    Larger U_x → x tends to be larger than y. We pre-register: x = Medinan, y = Meccan,
    direction Medinan > Meccan → larger U_x = more extreme in pre-committed direction.
    """
    combined = [(v, 0) for v in x] + [(v, 1) for v in y]
    # rank with tie-correction (mid-rank)
    combined.sort(key=lambda t: t[0])
    ranks = [0.0] * len(combined)
    i = 0
    while i < len(combined):
        j = i
        while j + 1 < len(combined) and combined[j + 1][0] == combined[i][0]:
            j += 1
        avg = (i + j) / 2.0 + 1.0  # 1-based midrank
        for k in range(i, j + 1):
            ranks[k] = avg
        i = j + 1
    rank_x_sum = sum(r for r, (_, g) in zip(ranks, combined) if g == 0)
    n_x = len(x)
    u_x = rank_x_sum - n_x * (n_x + 1) / 2.0
    return u_x


def main() -> None:
    verify_sha()
    quran = json.loads(QURAN_PATH.read_text())
    period_by_sid = load_chronology()

    # Per-surah verse-coverage
    per_surah = []
    for s in quran:
        sid = int(s["id"])
        verses = s["verses"]
        n = len(verses)
        has_allah = [1 if ALLAH_PATTERN.search(v["text"]) else 0 for v in verses]
        n_has = sum(has_allah)
        cov = n_has / n if n else 0.0
        per_surah.append({
            "sid": sid,
            "n_verses": n,
            "n_verses_with_allah": n_has,
            "coverage": cov,
            "period": period_by_sid.get(sid, "UNKNOWN"),
        })

    # Sanity-check chronology coverage
    assert all(r["period"] in ("Meccan", "Medinan") for r in per_surah), \
        "Unknown period label encountered"

    # Corpus ranking (descending coverage; tie-break by sid asc)
    ranked = sorted(per_surah, key=lambda r: (-r["coverage"], r["sid"]))
    rank_map = {r["sid"]: i + 1 for i, r in enumerate(ranked)}
    for r in per_surah:
        r["corpus_rank"] = rank_map[r["sid"]]
    top_10 = ranked[:10]

    # Q 58 specifically
    q58 = next(r for r in per_surah if r["sid"] == 58)
    q58_rank = rank_map[58]

    # Split Meccan vs Medinan
    meccan_cov = [r["coverage"] for r in per_surah if r["period"] == "Meccan"]
    medinan_cov = [r["coverage"] for r in per_surah if r["period"] == "Medinan"]

    n_meccan = len(meccan_cov)
    n_medinan = len(medinan_cov)
    mean_meccan = sum(meccan_cov) / n_meccan
    mean_medinan = sum(medinan_cov) / n_medinan
    median_meccan = sorted(meccan_cov)[n_meccan // 2]
    median_medinan = sorted(medinan_cov)[n_medinan // 2]

    # Mann-Whitney: U for Medinan (the pre-committed "larger" group)
    u_observed = mann_whitney_u(medinan_cov, meccan_cov)
    u_max = n_medinan * n_meccan
    # Direction: Medinan > Meccan → expect u_observed > n_medinan*n_meccan / 2

    # Permutation null: shuffle the 114 period labels
    all_cov = [r["coverage"] for r in per_surah]
    labels = [r["period"] for r in per_surah]  # 86 Meccan + 28 Medinan
    rng = random.Random(SEED)
    perm_u_values: list[float] = []
    for _ in range(N_PERM):
        shuffled = labels[:]
        rng.shuffle(shuffled)
        med_perm = [c for c, lab in zip(all_cov, shuffled) if lab == "Medinan"]
        mec_perm = [c for c, lab in zip(all_cov, shuffled) if lab == "Meccan"]
        u_perm = mann_whitney_u(med_perm, mec_perm)
        perm_u_values.append(u_perm)

    # One-sided p (Medinan > Meccan → count perm-U ≥ observed)
    n_extreme = sum(1 for u in perm_u_values if u >= u_observed)
    p_perm = (1 + n_extreme) / (1 + N_PERM)

    # Direction check
    direction_observed = "Medinan > Meccan" if mean_medinan > mean_meccan else (
        "Meccan > Medinan" if mean_meccan > mean_medinan else "tied"
    )
    direction_matches_prereg = (direction_observed == "Medinan > Meccan")

    # Verdict
    if direction_matches_prereg and p_perm <= 0.05:
        verdict = "PASS-DIRECTED"
    elif direction_matches_prereg and p_perm > 0.05:
        verdict = "NULL"
    else:
        verdict = "NULL (reverse-direction or tied — pre-commit-honoring)"

    # Per-word descriptive density (secondary, not part of H1)
    per_word_density = []
    for s in quran:
        sid = int(s["id"])
        n_words = 0
        n_allah_subs = 0
        for v in s["verses"]:
            toks = [t for t in v["text"].split() if not all(c in "۞ۖۗۚ۟ۘ۠ۤۛ" for c in t)]
            n_words += len(toks)
            n_allah_subs += len(ALLAH_PATTERN.findall(v["text"]))
        per_word_density.append({
            "sid": sid,
            "n_words": n_words,
            "n_allah_substrings": n_allah_subs,
            "allah_per_word": (n_allah_subs / n_words) if n_words else 0.0,
            "period": period_by_sid.get(sid, "UNKNOWN"),
        })
    per_word_ranked = sorted(per_word_density, key=lambda r: -r["allah_per_word"])
    per_word_rank_map = {r["sid"]: i + 1 for i, r in enumerate(per_word_ranked)}
    for r in per_word_density:
        r["corpus_density_rank"] = per_word_rank_map[r["sid"]]

    out = {
        "finding_id": "H-NEW-1350",
        "pre_reg_sha256": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "rules_tuple": "(no-tashkeel, orthographic-token, substring الله, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "chronology_source": "data/revelation-order.csv (al-Suyūṭī / Tanzil Egyptian Standard + Nöldeke phase)",
        "hypothesis": "Medinan > Meccan per-verse Allāh-coverage (one-sided Mann-Whitney U)",
        "n_meccan": n_meccan,
        "n_medinan": n_medinan,
        "mean_meccan_coverage": mean_meccan,
        "mean_medinan_coverage": mean_medinan,
        "median_meccan_coverage": median_meccan,
        "median_medinan_coverage": median_medinan,
        "u_observed": u_observed,
        "u_max": u_max,
        "u_expected_under_null": n_medinan * n_meccan / 2.0,
        "direction_observed": direction_observed,
        "direction_matches_prereg": direction_matches_prereg,
        "p_perm_one_sided": p_perm,
        "n_extreme_perms": n_extreme,
        "verdict": verdict,
        "q58_corpus_rank": q58_rank,
        "q58_coverage": q58["coverage"],
        "q58_n_verses_with_allah": q58["n_verses_with_allah"],
        "q58_n_verses": q58["n_verses"],
        "top_10_by_coverage": [
            {
                "rank": i + 1,
                "sid": r["sid"],
                "n_verses": r["n_verses"],
                "n_verses_with_allah": r["n_verses_with_allah"],
                "coverage": r["coverage"],
                "period": r["period"],
            }
            for i, r in enumerate(ranked[:10])
        ],
        "bottom_10_by_coverage": [
            {
                "rank": 114 - 9 + i,
                "sid": r["sid"],
                "n_verses": r["n_verses"],
                "n_verses_with_allah": r["n_verses_with_allah"],
                "coverage": r["coverage"],
                "period": r["period"],
            }
            for i, r in enumerate(ranked[-10:])
        ],
        "per_surah_full_table": per_surah,
        "secondary_per_word_density_top_10": [
            {
                "rank": i + 1,
                "sid": r["sid"],
                "allah_per_word": r["allah_per_word"],
                "n_allah_substrings": r["n_allah_substrings"],
                "n_words": r["n_words"],
                "period": r["period"],
            }
            for i, r in enumerate(per_word_ranked[:10])
        ],
    }

    os.makedirs(OUT_PATH.parent, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False))

    print(f"H-NEW-1350 verdict: {verdict}")
    print(f"  Meccan n={n_meccan}, mean coverage={mean_meccan:.4f}, median={median_meccan:.4f}")
    print(f"  Medinan n={n_medinan}, mean coverage={mean_medinan:.4f}, median={median_medinan:.4f}")
    print(f"  Mann-Whitney U(Medinan vs Meccan) = {u_observed:.1f} (expected under null = {n_medinan*n_meccan/2:.1f}; max = {u_max})")
    print(f"  Direction observed: {direction_observed}  (matches pre-reg: {direction_matches_prereg})")
    print(f"  One-sided permutation p = {p_perm:.5f}  ({n_extreme}/{N_PERM} ≥ observed)")
    print(f"  Q 58 corpus rank (coverage): {q58_rank}/114  (coverage={q58['coverage']:.4f})")
    print(f"  Top-5 by coverage:")
    for i, r in enumerate(ranked[:5]):
        print(f"    #{i+1}: Q {r['sid']:>3}  cov={r['coverage']:.4f}  n={r['n_verses']:>3}  period={r['period']}")
    print(f"  Output: {OUT_PATH}")


if __name__ == "__main__":
    main()
