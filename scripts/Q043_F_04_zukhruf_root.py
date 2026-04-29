"""
Q043-F-04: Q 43 zukhruf-root (z-kh-r-f) named-after-root signature
Pre-reg SHA256: ff2dd6517aac6582a800cdb48218f07bf1604932d5161ff75cc53e217a2503ff
Pre-reg path: surahs/Q043-al-zukhruf/preregs/Q043-F-04-zukhruf-root-signature-prereg.md
Seed: 20260428
"""
import hashlib
import json
import os
import sys

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q043-al-zukhruf/preregs/Q043-F-04-zukhruf-root-signature-prereg.md"
EXPECTED_SHA = "ff2dd6517aac6582a800cdb48218f07bf1604932d5161ff75cc53e217a2503ff"
ROOT_INDEX_PATH = "/Users/grey/Downloads/quran/data/morphology/root-index.json"
QURAN_PATH = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q043-al-zukhruf/csv/Q043-F-04.json"
TARGET_ROOT = "zxrf"


def verify_prereg():
    with open(PREREG_PATH, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")


def main():
    verify_prereg()

    with open(ROOT_INDEX_PATH) as f:
        root_idx = json.load(f)
    with open(QURAN_PATH) as f:
        quran = json.load(f)

    attestations = root_idx.get(TARGET_ROOT, [])
    total_attestations = len(attestations)

    # Per-surah counts
    per_surah_count = {sid: 0 for sid in range(1, 115)}
    for att in attestations:
        sid = att[0]
        per_surah_count[sid] += 1

    # Per-surah token counts
    per_surah_tokens = {}
    for s in quran:
        sid = s["id"]
        per_surah_tokens[sid] = sum(len(v["text"].split()) for v in s["verses"])

    # Per-surah density
    rows = []
    for sid in range(1, 115):
        toks = per_surah_tokens[sid]
        cnt = per_surah_count[sid]
        density = (cnt / toks * 1000) if toks > 0 else 0.0
        rows.append({"surah": sid, "count": cnt, "tokens": toks, "density_per_1000": round(density, 5)})

    # Rank by density descending (then by count descending as tiebreak)
    ranked = sorted(rows, key=lambda r: (-r["density_per_1000"], -r["count"], r["surah"]))
    for i, r in enumerate(ranked, start=1):
        r["rank"] = i

    q43 = next(r for r in ranked if r["surah"] == 43)
    q43_rank = q43["rank"]

    nonzero = [r for r in ranked if r["count"] > 0]
    q43_rank_among_nonzero = None
    for i, r in enumerate(nonzero, start=1):
        if r["surah"] == 43:
            q43_rank_among_nonzero = i
            break

    # Verdict: pre-committed direction was Q43 rank > 1 by density (i.e., NOT densest).
    # We use rank-among-nonzero since most surahs are rank-tied at density 0.
    if q43_rank_among_nonzero == 1:
        verdict = "NAIVE_HYPOTHESIS_CONFIRMED"  # Q43 is densest — pre-commit-direction reversed
    elif q43_rank_among_nonzero > 1:
        verdict = "VINDICATED"  # symbolic-naming, not density-naming
    else:
        verdict = "ANOMALY"

    out = {
        "prereg_id": "Q043-F-04",
        "prereg_sha": EXPECTED_SHA,
        "seed": 20260428,
        "rules_tuple": "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "target_root": TARGET_ROOT,
        "total_corpus_attestations": total_attestations,
        "attestation_locations": attestations,
        "Q43_count": q43["count"],
        "Q43_tokens": q43["tokens"],
        "Q43_density_per_1000": q43["density_per_1000"],
        "Q43_rank_corpus_wide": q43_rank,
        "Q43_rank_among_nonzero_surahs": q43_rank_among_nonzero,
        "n_surahs_with_zxrf_attestation": len(nonzero),
        "nonzero_surahs_ranked": [
            {"rank": r["rank"], "surah": r["surah"], "count": r["count"],
             "tokens": r["tokens"], "density": r["density_per_1000"]}
            for r in nonzero
        ],
        "direction_predicted": "Q43 rank > 1 by zxrf density (surah-name is symbolic, not density-driven)",
        "verdict": verdict,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
