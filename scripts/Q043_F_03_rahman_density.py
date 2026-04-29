"""
Q043-F-03: Q 43 *al-Raḥmān* lemma-density rank corpus-wide.
Pre-reg SHA256: a265de03d897060bb4a4c8ea591051966cc62fd30922ea9ccd3a5cd5e682639d
Pre-reg path: surahs/Q043-al-zukhruf/preregs/Q043-F-03-rahman-density-prereg.md
Seed: 20260428
"""
import hashlib
import json
import os
import sys

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q043-al-zukhruf/preregs/Q043-F-03-rahman-density-prereg.md"
EXPECTED_SHA = "a265de03d897060bb4a4c8ea591051966cc62fd30922ea9ccd3a5cd5e682639d"
QURAN_PATH = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q043-al-zukhruf/csv/Q043-F-03.json"
LEMMA_NEEDLE = "رحمن"


def verify_prereg():
    with open(PREREG_PATH, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")


def main():
    verify_prereg()

    with open(QURAN_PATH) as f:
        quran = json.load(f)

    rows = []
    for s in quran:
        sid = s["id"]
        token_count = 0
        rahman_count = 0
        for v in s["verses"]:
            words = v["text"].split()
            token_count += len(words)
            for w in words:
                if LEMMA_NEEDLE in w:
                    rahman_count += 1
        density = (rahman_count / token_count * 1000) if token_count > 0 else 0.0
        rows.append({
            "surah": sid,
            "rahman_count": rahman_count,
            "tokens": token_count,
            "density_per_1000": round(density, 4),
        })

    # Rank by density descending
    ranked = sorted(rows, key=lambda r: -r["density_per_1000"])
    for i, r in enumerate(ranked, start=1):
        r["rank"] = i

    q43 = next(r for r in ranked if r["surah"] == 43)
    rank = q43["rank"]

    if rank <= 5:
        verdict = "VINDICATED"
    elif rank <= 10:
        verdict = "DIRECTIONAL"
    elif rank > 50:
        verdict = "PRECOMMIT_VIOLATION"
    else:
        verdict = "NULL"

    out = {
        "prereg_id": "Q043-F-03",
        "prereg_sha": EXPECTED_SHA,
        "seed": 20260428,
        "rules_tuple": "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "lemma_needle": LEMMA_NEEDLE,
        "Q43_rahman_count": q43["rahman_count"],
        "Q43_tokens": q43["tokens"],
        "Q43_density_per_1000": q43["density_per_1000"],
        "Q43_rank": rank,
        "top_15_rahman_density_surahs": [
            {"rank": r["rank"], "surah": r["surah"], "count": r["rahman_count"],
             "tokens": r["tokens"], "density": r["density_per_1000"]}
            for r in ranked[:15]
        ],
        "direction_predicted": "Q43 rank in {1..5}",
        "direction_observed_rank": rank,
        "verdict": verdict,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
