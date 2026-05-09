#!/usr/bin/env python3
"""Q072-F-02 — Q 72 corpus-rank-1 in jinn-lemma density (strict LEM:jin~).

Pre-reg: surahs/Q072-al-jinn/preregs/Q072-F-02-jinn-density-rank-prereg.md
Pre-reg SHA256: 0129c9a395bc084e4b6df785af3f97c3f0abd5054e8288ab1dc6357e72864e69

Rules-tuple: (no-tashkeel, QAC v0.4 morphological lemma filter, LEM:jin~ strict,
              per-surah word-count from quran-no-tashkeel.json, basmala-counted-only-in-Q1, Hafs-Kufan)
Seed: 20260509 (not used; deterministic)  |  Direction: PASS (Q 72 rank = 1/114)
"""
import hashlib
import json
import os
import re
import sys
from collections import Counter

PREREG = "/Users/grey/Downloads/quran/surahs/Q072-al-jinn/preregs/Q072-F-02-jinn-density-rank-prereg.md"
EXPECTED_SHA = "0129c9a395bc084e4b6df785af3f97c3f0abd5054e8288ab1dc6357e72864e69"

QURAN_NO_TASHKEEL = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
QAC_PATH = "/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q072-al-jinn/csv/Q072-F-02.json"


def verify_sha():
    actual = hashlib.sha256(open(PREREG, "rb").read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def count_lemma_per_surah(target_lemmas):
    """Count tokens whose LEM tag is in target_lemmas AND ROOT:jnn."""
    pat_loc = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")
    counter = Counter()
    with open(QAC_PATH) as f:
        for line in f:
            if "ROOT:jnn" not in line:
                continue
            parts = line.split("|")
            lem = None
            for p in parts:
                p = p.strip()
                if p.startswith("LEM:"):
                    lem = p[4:]
                    break
            if lem in target_lemmas:
                m = pat_loc.match(line)
                if m:
                    counter[int(m.group(1))] += 1
    return counter


def main():
    verify_sha()

    qd = json.load(open(QURAN_NO_TASHKEEL))
    surah_tokens = {s["id"]: sum(len(v["text"].split()) for v in s["verses"]) for s in qd}

    # Primary: strict LEM:jin~
    strict_counts = count_lemma_per_surah({"jin~"})
    densities_strict = []
    for sid in range(1, 115):
        j = strict_counts.get(sid, 0)
        t = surah_tokens.get(sid, 1)
        densities_strict.append({"surah": sid, "jin_count": j, "tokens": t, "density_per_1k": j / t * 1000.0})

    sorted_strict = sorted(densities_strict, key=lambda x: (-x["density_per_1k"], x["surah"]))
    rank_strict = next(i for i, r in enumerate(sorted_strict, 1) if r["surah"] == 72)
    q72_strict = next(r for r in sorted_strict if r["surah"] == 72)

    # Secondary (sensitivity): combined LEM:jin~ + LEM:jaA^n~
    combined_counts = count_lemma_per_surah({"jin~", "jaA^n~"})
    densities_combined = []
    for sid in range(1, 115):
        j = combined_counts.get(sid, 0)
        t = surah_tokens.get(sid, 1)
        densities_combined.append({"surah": sid, "jin_count": j, "tokens": t, "density_per_1k": j / t * 1000.0})

    sorted_combined = sorted(densities_combined, key=lambda x: (-x["density_per_1k"], x["surah"]))
    rank_combined = next(i for i, r in enumerate(sorted_combined, 1) if r["surah"] == 72)
    q72_combined = next(r for r in sorted_combined if r["surah"] == 72)

    # Verdicts
    primary_pass = rank_strict == 1
    secondary_pass = rank_combined <= 2  # pre-committed: rank >= 2 acceptable for secondary

    if primary_pass:
        verdict_primary = "PASS (rank=1/114 strict LEM:jin~)"
    elif rank_strict <= 3:
        verdict_primary = f"DIRECTIONAL (rank={rank_strict}/114)"
    else:
        verdict_primary = f"NULL (rank={rank_strict}/114)"

    out = {
        "test_id": "Q072-F-02",
        "prereg_sha": EXPECTED_SHA,
        "primary_lens": "strict LEM:jin~",
        "secondary_lens": "expanded LEM:jin~ + LEM:jaA^n~",
        "q72_strict": q72_strict,
        "q72_strict_rank": rank_strict,
        "q72_combined": q72_combined,
        "q72_combined_rank": rank_combined,
        "top10_strict": sorted_strict[:10],
        "top10_combined": sorted_combined[:10],
        "verdict_primary": verdict_primary,
        "primary_pass": primary_pass,
        "secondary_pass": secondary_pass,
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    json.dump(out, open(OUT_PATH, "w", encoding="utf-8"), ensure_ascii=False, indent=2)

    print(f"Q072-F-02 primary: {verdict_primary}")
    print(f"  Q 72 strict-LEM:jin~ density: {q72_strict['density_per_1k']:.3f}/1k ({q72_strict['jin_count']}/{q72_strict['tokens']})")
    print(f"  Q 72 expanded-lens density:   {q72_combined['density_per_1k']:.3f}/1k -> rank {rank_combined}/114")
    print("Top-5 strict:")
    for r in sorted_strict[:5]:
        print(f"  Q{r['surah']:3d}: {r['jin_count']:3d}/{r['tokens']:5d} = {r['density_per_1k']:6.2f}/1k")
    print(f"Written: {OUT_PATH}")


if __name__ == "__main__":
    main()
