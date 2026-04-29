"""
Q043-F-05: Q 43:57-65 ʿĪsā-passage christological-token density vs corpus 9-window null
Pre-reg SHA256: 87fcc04d19b68ef638f2ef83823c24d0b7ca46208fa37ca32604e7e87a668cac
Pre-reg path: surahs/Q043-al-zukhruf/preregs/Q043-F-05-isa-block-density-prereg.md
Seed: 20260428
"""
import hashlib
import json
import os
import sys

PREREG_PATH = "/Users/grey/Downloads/quran/surahs/Q043-al-zukhruf/preregs/Q043-F-05-isa-block-density-prereg.md"
EXPECTED_SHA = "87fcc04d19b68ef638f2ef83823c24d0b7ca46208fa37ca32604e7e87a668cac"
QURAN_PATH = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
OUT_PATH = "/Users/grey/Downloads/quran/surahs/Q043-al-zukhruf/csv/Q043-F-05.json"
WINDOW_LEN = 9
NEEDLES = ["عيسى", "مريم"]


def verify_prereg():
    with open(PREREG_PATH, "rb") as f:
        sha = hashlib.sha256(f.read()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: {sha} != {EXPECTED_SHA}")


def count_christ_tokens(words):
    n = 0
    for w in words:
        for needle in NEEDLES:
            if needle in w:
                n += 1
                break
    return n


def main():
    verify_prereg()
    with open(QURAN_PATH) as f:
        quran = json.load(f)

    # Per-verse: christological count + token count
    verse_records = []  # list of {surah, verse, n_chr, n_tok}
    for s in quran:
        sid = s["id"]
        for v in s["verses"]:
            words = v["text"].split()
            verse_records.append({
                "surah": sid,
                "verse": v["id"],
                "n_chr": count_christ_tokens(words),
                "n_tok": len(words),
            })

    # Build 9-windows within-surah only (not crossing surah boundaries)
    windows = []
    for s in quran:
        sid = s["id"]
        surah_verses = [r for r in verse_records if r["surah"] == sid]
        if len(surah_verses) < WINDOW_LEN:
            continue
        for i in range(len(surah_verses) - WINDOW_LEN + 1):
            block = surah_verses[i:i + WINDOW_LEN]
            n_chr = sum(r["n_chr"] for r in block)
            n_tok = sum(r["n_tok"] for r in block)
            density = (n_chr / n_tok * 1000) if n_tok > 0 else 0.0
            windows.append({
                "surah": sid,
                "v_start": block[0]["verse"],
                "v_end": block[-1]["verse"],
                "n_chr": n_chr,
                "n_tok": n_tok,
                "density": density,
            })

    # Find Q43:57-65
    q43_block = [w for w in windows if w["surah"] == 43 and w["v_start"] == 57 and w["v_end"] == 65]
    if not q43_block:
        sys.exit("Q43:57-65 window not found")
    q43_target = q43_block[0]

    # Percentile rank of Q43 target
    densities_sorted = sorted([w["density"] for w in windows])
    n_total = len(densities_sorted)
    # Count how many windows have density <= Q43_density
    n_le = sum(1 for d in densities_sorted if d <= q43_target["density"])
    percentile = n_le / n_total * 100

    # Top-10 windows by density
    top10 = sorted(windows, key=lambda w: -w["density"])[:10]

    # Verdict
    if percentile >= 99.0:
        verdict = "VINDICATED"
    elif percentile >= 95.0:
        verdict = "DIRECTIONAL"
    elif percentile >= 50.0:
        verdict = "NULL"
    else:
        verdict = "PRECOMMIT_VIOLATION"

    out = {
        "prereg_id": "Q043-F-05",
        "prereg_sha": EXPECTED_SHA,
        "seed": 20260428,
        "rules_tuple": "(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "needles": NEEDLES,
        "window_len": WINDOW_LEN,
        "Q43_57_65_n_chr": q43_target["n_chr"],
        "Q43_57_65_n_tok": q43_target["n_tok"],
        "Q43_57_65_density_per_1000": round(q43_target["density"], 4),
        "Q43_57_65_percentile_rank": round(percentile, 2),
        "n_total_9_windows_corpus": n_total,
        "n_windows_with_nonzero_chr_density": sum(1 for w in windows if w["density"] > 0),
        "top_10_christological_9_windows": [
            {"surah": w["surah"], "v_start": w["v_start"], "v_end": w["v_end"],
             "n_chr": w["n_chr"], "n_tok": w["n_tok"],
             "density_per_1000": round(w["density"], 4)}
            for w in top10
        ],
        "direction_predicted": "Q43:57-65 density ≥ 99th percentile",
        "verdict": verdict,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(json.dumps(out, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
