#!/usr/bin/env python3
"""Q044-F-02: mubīn-density extreme test.

Pre-reg: /Users/grey/Downloads/quran/surahs/Q044-al-dukhan/preregs/Q044-F-02-mubin-density-prereg.md
Pre-reg SHA256 (locked): 5bdd82e47c53745f649ac426fd6c413e8eb68c0e6ca6ca92e4bd7431550c5988
"""

import hashlib
import json
import math
import os
import re
import sys

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/preregs/Q044-F-02-mubin-density-prereg.md"
PREREG_SHA_EXPECTED = "5bdd82e47c53745f649ac426fd6c413e8eb68c0e6ca6ca92e4bd7431550c5988"

OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q044-al-dukhan/csv/Q044-F-02.json"
QURAN_NO_TASHKEEL = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        h.update(f.read())
    return h.hexdigest()


def main():
    actual = sha256_of(PREREG_PATH)
    if actual != PREREG_SHA_EXPECTED:
        print(f"FAIL: SHA mismatch\n  expected: {PREREG_SHA_EXPECTED}\n  actual:   {actual}", file=sys.stderr)
        sys.exit(1)
    print(f"Pre-reg SHA verified: {actual}")

    data = json.load(open(QURAN_NO_TASHKEEL))
    # Per-surah word count + mubin count (both مبين and المبين as locked)
    PATTERN = re.compile(r"(?:^|[\s])(?:ال)?مبين(?=[\s]|$)")
    per_surah = []
    for s in data:
        text = " " + " ".join(v["text"] for v in s["verses"]) + " "  # pad for boundary
        words = sum(len(v["text"].split()) for v in s["verses"])
        # Use a non-regex direct count of `مبين` as standalone token
        tokens = text.split()
        count = sum(1 for t in tokens if t == "مبين" or t == "المبين")
        density = count / words * 1000.0 if words else 0.0
        per_surah.append({"surah": s["id"], "name": s["name"], "n_verses": s["total_verses"],
                          "n_words": words, "mubin_count": count, "density_per_1000": density})

    # Sort by density
    sorted_by_density = sorted(per_surah, key=lambda x: -x["density_per_1000"])

    # Q44 stats
    q44 = [p for p in per_surah if p["surah"] == 44][0]
    others = [p for p in per_surah if p["surah"] != 44]
    other_densities = [p["density_per_1000"] for p in others]
    mean_other = sum(other_densities) / len(other_densities)
    var = sum((d - mean_other) ** 2 for d in other_densities) / (len(other_densities) - 1)
    sd = math.sqrt(var)
    z = (q44["density_per_1000"] - mean_other) / sd if sd > 0 else float("inf")

    # Rank Q44
    q44_rank = next(i for i, p in enumerate(sorted_by_density, 1) if p["surah"] == 44)

    print(f"\nQ44 mubīn count: {q44['mubin_count']} in {q44['n_words']} words")
    print(f"Q44 density: {q44['density_per_1000']:.3f} per 1000 words")
    print(f"Corpus mean (excl Q44): {mean_other:.3f}, SD: {sd:.3f}")
    print(f"Q44 z-score: {z:.3f}")
    print(f"Q44 rank: {q44_rank} / 114")
    print("\nTop-10 mubīn-densest surahs:")
    for i, p in enumerate(sorted_by_density[:10], 1):
        marker = " <- Q44" if p["surah"] == 44 else ""
        print(f"  {i}. Q{p['surah']:>3} {p['name']}: {p['density_per_1000']:.3f} ({p['mubin_count']}/{p['n_words']}){marker}")

    # Verdict
    if z >= 1.0 and q44_rank <= 3:
        verdict = "VINDICATED at corpus-extreme strength"
    elif z >= 0.5:
        verdict = "DIRECTIONAL"
    elif z < 0:
        verdict = "PRE-COMMIT VIOLATION + NULL"
    else:
        verdict = "NULL"

    out = {
        "finding_id": "Q044-F-02",
        "prereg_sha": actual,
        "prereg_sha_expected": PREREG_SHA_EXPECTED,
        "tashkeel_level": "no-tashkeel",
        "match_pattern": "مبين OR المبين as standalone orthographic token",
        "q44": q44,
        "corpus_mean_excluding_q44": mean_other,
        "corpus_sd_excluding_q44": sd,
        "q44_z_score": z,
        "q44_rank_density": q44_rank,
        "top_10_densest": sorted_by_density[:10],
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    json.dump(out, open(OUT_PATH, "w"), indent=2, ensure_ascii=False)
    print(f"\nVERDICT: {verdict}")
    print(f"Wrote {OUT_PATH}")


if __name__ == "__main__":
    main()
