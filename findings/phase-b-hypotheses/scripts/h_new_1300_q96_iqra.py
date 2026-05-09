#!/usr/bin/env python3
"""H-NEW-1300 — Q 96 al-ʿAlaq *qrʾ*-imperative corpus-distribution.

Pre-reg locked at:
  /Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-1300-q96-iqra-corpus-distribution-prereg.md
SHA256 (verified at runtime): 201d8a26cb063b2bd2c4d277ed90f65402bb89a1a3a61675e48955bfd4e64395
"""

import hashlib
import json
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-1300-q96-iqra-corpus-distribution-prereg.md"
EXPECTED_SHA = "201d8a26cb063b2bd2c4d277ed90f65402bb89a1a3a61675e48955bfd4e64395"
QAC = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
QURAN = ROOT / "quran-text/quran-no-tashkeel.json"
OUT = ROOT / "findings/phase-b-hypotheses/csv/h-new-1300.json"
SEED = 20260509
N_PERM = 10_000


def verify_prereg() -> None:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual}")
    print(f"pre-reg SHA verified: {EXPECTED_SHA[:12]}…")


def parse_qac():
    """Yield (surah, verse, word, segment, form, pos, features) tuples."""
    with QAC.open(encoding="utf-8") as fh:
        for line in fh:
            if not line.startswith("("):
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            loc = parts[0].strip("()").split(":")
            if len(loc) != 4:
                continue
            s, v, w, seg = (int(x) for x in loc)
            form = parts[1]
            pos = parts[2]
            features = parts[3]
            yield s, v, w, seg, form, pos, features


def main() -> None:
    verify_prereg()

    iqra_count: Counter[int] = Counter()  # surah -> IMPV qrA count
    impv_count: Counter[int] = Counter()  # surah -> total IMPV count (for null weights)
    iqra_lemma_count: Counter[int] = Counter()  # lemma 'qara>a' filter
    iqra_locations: list[tuple[int, int, int, str]] = []
    verse_set: set[tuple[int, int]] = set()

    for s, v, w, seg, form, pos, features in parse_qac():
        verse_set.add((s, v))
        if pos != "V":
            continue
        is_impv = "|IMPV|" in features or features.endswith("|IMPV") or "IMPV|" in features
        is_qra_root = "ROOT:qrA" in features
        is_qara_lemma = "LEM:qara>a" in features
        if is_impv:
            impv_count[s] += 1
            if is_qra_root:
                iqra_count[s] += 1
                iqra_locations.append((s, v, w, form))
            if is_qara_lemma:
                iqra_lemma_count[s] += 1

    verses_per_surah = Counter(s for s, _ in verse_set)

    # Cell A: absolute count
    ranking = sorted(range(1, 115), key=lambda s: (-iqra_count[s], s))
    obs_q96 = iqra_count[96]
    rank_q96 = ranking.index(96) + 1
    rank1_surah = ranking[0]
    rank1_count = iqra_count[rank1_surah]

    # Cell B: per-verse density
    density = {s: iqra_count[s] / verses_per_surah[s] for s in range(1, 115)}
    density_ranking = sorted(range(1, 115), key=lambda s: (-density[s], s))
    rank_q96_density = density_ranking.index(96) + 1

    # Permutation null: relocate IMPV+qrA segments to random surahs weighted by IMPV count
    rng = random.Random(SEED)
    surahs = list(range(1, 115))
    weights = [impv_count[s] for s in surahs]
    n_qra = sum(iqra_count.values())

    perm_q96_ge_obs = 0
    perm_max_ge_obs = 0
    perm_max_counts: list[int] = []
    perm_q96_counts: list[int] = []
    for _ in range(N_PERM):
        sample = rng.choices(surahs, weights=weights, k=n_qra)
        c = Counter(sample)
        m = max(c.values()) if c else 0
        perm_max_counts.append(m)
        perm_q96_counts.append(c.get(96, 0))
        if c.get(96, 0) >= obs_q96:
            perm_q96_ge_obs += 1
        if m >= obs_q96:
            perm_max_ge_obs += 1

    # The pre-reg p_perm: fraction of perms where (random rank-1 ≥ obs_q96 AND q96 random ≥ obs_q96)
    perm_joint = sum(
        1
        for q96, m in zip(perm_q96_counts, perm_max_counts)
        if q96 >= obs_q96 and m >= obs_q96
    )

    p_perm = perm_joint / N_PERM
    p_q96_alone = perm_q96_ge_obs / N_PERM
    p_max_alone = perm_max_ge_obs / N_PERM

    # Verdict
    if rank_q96 == 1 and p_perm <= 0.05:
        verdict = "PASS-DIRECTED"
    elif rank_q96 == 1:
        verdict = "DESCRIPTIVE-ONLY (rank-1 confirmed; p_perm > 0.05)"
    else:
        verdict = "NULL"

    out = {
        "id": "H-NEW-1300",
        "title": "Q 96 al-ʿAlaq *qrʾ*-imperative corpus-distribution",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "cell_A_absolute_count": {
            "obs_q96": obs_q96,
            "rank_q96_of_114": rank_q96,
            "rank_1_surah": rank1_surah,
            "rank_1_count": rank1_count,
            "top_10_ranking": [
                {"surah": s, "count": iqra_count[s]} for s in ranking[:10]
            ],
        },
        "cell_B_per_verse_density": {
            "q96_density": density[96],
            "rank_q96_of_114": rank_q96_density,
            "top_10_ranking": [
                {"surah": s, "count": iqra_count[s], "verses": verses_per_surah[s], "density": density[s]}
                for s in density_ranking[:10]
            ],
        },
        "permutation_null": {
            "p_perm_joint": p_perm,
            "p_q96_only": p_q96_alone,
            "p_rank1_only": p_max_alone,
            "perm_max_mean": mean(perm_max_counts),
            "perm_q96_mean": mean(perm_q96_counts),
        },
        "lemma_filter_check": {
            "q96_lemma_qara_a_count": iqra_lemma_count[96],
            "rank_q96_lemma": sorted(range(1, 115), key=lambda s: (-iqra_lemma_count[s], s)).index(96) + 1,
            "totals_root_vs_lemma": {"root_qrA_total": sum(iqra_count.values()), "lemma_qara_a_total": sum(iqra_lemma_count.values())},
        },
        "iqra_locations_full": iqra_locations,
        "verdict": verdict,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"\nVerdict: {verdict}")
    print(f"Q 96 IMPV qrA count: {obs_q96}  rank: {rank_q96}/114")
    print(f"Rank-1 surah: Q {rank1_surah}  count: {rank1_count}")
    print(f"Top-10 absolute: {[(r['surah'], r['count']) for r in out['cell_A_absolute_count']['top_10_ranking']]}")
    print(f"p_perm (joint): {p_perm:.5f}  p_q96-only: {p_q96_alone:.5f}  p_max-only: {p_max_alone:.5f}")
    print(f"All IMPV+qrA locations: {iqra_locations}")
    print(f"Wrote: {OUT}")


if __name__ == "__main__":
    main()
